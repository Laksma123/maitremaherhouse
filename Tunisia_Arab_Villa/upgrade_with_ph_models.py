import bpy
import bmesh
import math
import os
from mathutils import Vector, Matrix

OUT_DIR = "/Users/dianjulie/Documents/Map Project/Tunisia_Arab_Villa"
PH_MODELS = os.path.join(OUT_DIR, "ph_models")
PH_TEX = os.path.join(OUT_DIR, "ph_textures")

# First rebuild clean base architecture from build_tunisia_villa_blender.py logic
blend_path = os.path.join(OUT_DIR, "tunisia_arab_villa.blend")
bpy.ops.wm.open_mainfile(filepath=blend_path)
scene = bpy.context.scene

# Remove all previously imported PH_ objects and AO_ decals so we place them cleanly
for o in list(bpy.data.objects):
    if o.name.startswith("PH_") or o.name.startswith("AO_"):
        bpy.data.objects.remove(o, do_unlink=True)

# Fix Wall & Floor Materials: Bright Tunisian Whitewashed Limestone + Normal Bump + Authentic Blue Zellige Motif
def configure_wall_and_floor_materials():
    # 1. Warm Bright Tunisian Chalk/Sand Plaster with subtle Clay Plaster Normal Map
    for mname, tint in [("Mat_Wall_Tadelakt_Sand", (0.96, 0.93, 0.87, 1.0)), ("Mat_Wall_Exterior_Limestone", (0.97, 0.95, 0.90, 1.0))]:
        mat = bpy.data.materials.get(mname)
        if not mat:
            continue
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links
        bsdf = nodes.get("Principled BSDF")
        # Remove any diffuse image connected to Base Color so wall stays bright Tunisian cream
        for l in list(links):
            if l.to_socket == bsdf.inputs["Base Color"]:
                links.remove(l)
        bsdf.inputs["Base Color"].default_value = tint
        bsdf.inputs["Roughness"].default_value = 0.52
        npath = os.path.join(PH_TEX, "clay_plaster_nor.jpg")
        if os.path.exists(npath):
            nimg = bpy.data.images.load(npath, check_existing=True)
            nimg.colorspace_settings.name = 'Non-Color'
            nimg.pack()
            ntex = nodes.new("ShaderNodeTexImage")
            ntex.image = nimg
            nmap = nodes.new("ShaderNodeNormalMap")
            nmap.inputs["Strength"].default_value = 0.45
            links.new(ntex.outputs["Color"], nmap.inputs["Color"])
            links.new(nmap.outputs["Normal"], bsdf.inputs["Normal"])

    # 2. Keep vibrant Tunisian Zellige Mosaic on Feature Wall + Real Tile Normal Map
    mat_z = bpy.data.materials.get("Mat_Wall_Arab_Zellige_Motif")
    if mat_z:
        nodes = mat_z.node_tree.nodes
        links = mat_z.node_tree.links
        bsdf = nodes.get("Principled BSDF")
        for l in list(links):
            if l.to_socket == bsdf.inputs["Base Color"]:
                links.remove(l)
        zimg = bpy.data.images.get("Tex_Tunisian_Zellige")
        if zimg:
            ztex = nodes.new("ShaderNodeTexImage")
            ztex.image = zimg
            links.new(ztex.outputs["Color"], bsdf.inputs["Base Color"])
        npath = os.path.join(PH_TEX, "blue_floor_tiles_01_nor.jpg")
        if os.path.exists(npath):
            nimg = bpy.data.images.load(npath, check_existing=True)
            nimg.colorspace_settings.name = 'Non-Color'
            nimg.pack()
            ntex = nodes.new("ShaderNodeTexImage")
            ntex.image = nimg
            nmap = nodes.new("ShaderNodeNormalMap")
            nmap.inputs["Strength"].default_value = 0.75
            links.new(ntex.outputs["Color"], nmap.inputs["Color"])
            links.new(nmap.outputs["Normal"], bsdf.inputs["Normal"])

configure_wall_and_floor_materials()

def place_ph_model(asset_id, name, target_loc, target_span_xy=None, target_height=None, rot_z=0.0, col_name="03_Living_Majlis_And_TV"):
    gltf_file = os.path.join(PH_MODELS, asset_id, f"{asset_id}.gltf")
    if not os.path.exists(gltf_file):
        return None
    col = bpy.data.collections.get(col_name) or scene.collection

    before_names = set(o.name for o in bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=gltf_file)
    new_names = [o.name for o in bpy.data.objects if o.name not in before_names]
    imported = [bpy.data.objects[n] for n in new_names if n in bpy.data.objects and bpy.data.objects[n].type == 'MESH']
    if not imported:
        return None

    bpy.ops.object.select_all(action='DESELECT')
    for o in imported:
        o.select_set(True)
    bpy.context.view_layer.objects.active = imported[0]
    bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
    if len(imported) > 1:
        bpy.ops.object.join()
    obj = bpy.context.active_object
    obj.name = name

    for n in new_names:
        if n in bpy.data.objects and bpy.data.objects[n] != obj:
            bpy.data.objects.remove(bpy.data.objects[n], do_unlink=True)

    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

    # First apply rot_z so X and Y spans match world X and Y!
    obj.rotation_euler = (0.0, 0.0, rot_z)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

    verts = [v.co for v in obj.data.vertices]
    min_x = min(v.x for v in verts); max_x = max(v.x for v in verts)
    min_y = min(v.y for v in verts); max_y = max(v.y for v in verts)
    min_z = min(v.z for v in verts); max_z = max(v.z for v in verts)
    cx = 0.5 * (min_x + max_x)
    cy = 0.5 * (min_y + max_y)
    sx = max(0.001, max_x - min_x)
    sy = max(0.001, max_y - min_y)
    sz = max(0.001, max_z - min_z)

    for v in obj.data.vertices:
        v.co.x -= cx
        v.co.y -= cy
        v.co.z -= min_z
    obj.data.update()

    if target_span_xy:
        tx, ty, tz = target_span_xy
        obj.scale = (tx / sx, ty / sy, tz / sz)
    elif target_height:
        s = target_height / sz
        obj.scale = (s, s, s)

    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.location = target_loc

    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    col.objects.link(obj)
    return obj

# 1. KING BED ZONE ("King bedd": Headboard against West wall X=-5.80m, extending East along +X!)
place_ph_model("GothicBed_01", "PH_KingBed_Main", (-4.55, 2.50, 0.02), target_span_xy=(2.40, 2.05, 1.65), rot_z=math.pi/2, col_name="04_Bedroom_And_MiddleZone")
for ny in (1.10, 3.90):
    place_ph_model("ClassicNightstand_01", f"PH_Nightstand_{ny}", (-5.50, ny, 0.02), target_height=0.66, rot_z=math.pi/2, col_name="04_Bedroom_And_MiddleZone")
    place_ph_model("brass_diya_lantern", f"PH_Bed_Lantern_{ny}", (-5.50, ny, 0.68), target_height=0.35, rot_z=0.0, col_name="04_Bedroom_And_MiddleZone")

# 2. MIDDLE ZONE ("Sofa maybe, furniture etc": Narrow Vertical Daybed along Y-axis at X = 0.05m, Y = 0.50 .. 3.10m!)
place_ph_model("vintage_day_bed", "PH_Middle_Daybed", (0.05, 1.95, 0.02), target_span_xy=(0.88, 2.45, 0.86), rot_z=math.pi/2, col_name="04_Bedroom_And_MiddleZone")
place_ph_model("coffee_table_round_01", "PH_Middle_TeaTable", (0.05, 0.15, 0.02), target_height=0.50, rot_z=0.0, col_name="04_Bedroom_And_MiddleZone")
place_ph_model("brass_vase_01", "PH_Middle_BrassVase", (0.05, 0.15, 0.52), target_height=0.32, rot_z=0.0, col_name="04_Bedroom_And_MiddleZone")

# 3. LIVING MAJLIS SALON & TV ZONE ("Sofa, main room accessories and beautiful furniture" + "TV")
place_ph_model("modern_wooden_cabinet", "PH_TV_Media_Cabinet", (3.15, 4.48, 0.02), target_span_xy=(2.90, 0.52, 0.62), rot_z=0.0, col_name="03_Living_Majlis_And_TV")
place_ph_model("Sofa_01", "PH_Majlis_Sofa_South", (3.05, 0.08, 0.02), target_span_xy=(2.80, 0.98, 0.92), rot_z=0.0, col_name="03_Living_Majlis_And_TV")
place_ph_model("Sofa_01", "PH_Majlis_Sofa_East", (4.72, 1.85, 0.02), target_span_xy=(0.98, 2.55, 0.92), rot_z=math.pi/2, col_name="03_Living_Majlis_And_TV")
place_ph_model("ArmChair_01", "PH_Majlis_Armchair_West", (1.62, 2.35, 0.02), target_height=0.88, rot_z=-math.pi/2.2, col_name="03_Living_Majlis_And_TV")
place_ph_model("Ottoman_01", "PH_Majlis_Ottoman_1", (1.72, 1.20, 0.02), target_height=0.42, rot_z=0.4, col_name="03_Living_Majlis_And_TV")
place_ph_model("CoffeeTable_01", "PH_Majlis_CoffeeTable", (3.05, 1.75, 0.02), target_span_xy=(1.45, 0.92, 0.48), rot_z=0.0, col_name="03_Living_Majlis_And_TV")
place_ph_model("brass_pot_01", "PH_Majlis_BrassPot", (2.85, 1.75, 0.50), target_height=0.26, rot_z=0.0, col_name="03_Living_Majlis_And_TV")
place_ph_model("ceramic_vase_01", "PH_Majlis_CeramicVase", (3.28, 1.75, 0.50), target_height=0.28, rot_z=0.0, col_name="03_Living_Majlis_And_TV")
place_ph_model("throw_pillows_01", "PH_Majlis_Pillows_S", (3.05, 0.02, 0.48), target_height=0.38, rot_z=0.0, col_name="03_Living_Majlis_And_TV")
place_ph_model("potted_plant_02", "PH_Living_Plant_NE", (5.25, 4.15, 0.02), target_height=1.35, rot_z=0.5, col_name="03_Living_Majlis_And_TV")
place_ph_model("potted_plant_01", "PH_Living_Plant_SW", (1.65, -0.65, 0.02), target_height=1.15, rot_z=-0.4, col_name="03_Living_Majlis_And_TV")

# 4. KITCHEN STOVE & BATHROOM ORNATE MIRROR
place_ph_model("electric_stove", "PH_Kitchen_Stove", (0.92, -2.90, 0.02), target_span_xy=(0.68, 0.72, 0.90), rot_z=-math.pi/2, col_name="05_Kitchen_And_Fridge")
place_ph_model("ornate_mirror_01", "PH_Bath_Ornate_Mirror", (-3.15, -4.82, 1.02), target_height=1.25, rot_z=0.0, col_name="06_Bathroom_Shower_Toilet")

# 5. REAL CHANDELIERS & LANTERN SCONCES
place_ph_model("Chandelier_03", "PH_Chandelier_Living", (3.05, 1.75, 2.38), target_height=1.08, rot_z=0.0, col_name="07_Lamps_And_Wall_Switches")
place_ph_model("Chandelier_01", "PH_Chandelier_Bedroom", (-4.10, 2.50, 2.42), target_height=1.02, rot_z=0.0, col_name="07_Lamps_And_Wall_Switches")
place_ph_model("lantern_chandelier_01", "PH_Chandelier_Middle", (0.05, 1.85, 2.52), target_height=0.92, rot_z=0.0, col_name="07_Lamps_And_Wall_Switches")
place_ph_model("chinese_chandelier", "PH_Chandelier_Kitchen", (-0.25, -3.50, 2.55), target_height=0.88, rot_z=0.0, col_name="07_Lamps_And_Wall_Switches")
place_ph_model("Chandelier_02", "PH_Chandelier_Bathroom", (-3.85, -2.85, 2.58), target_height=0.85, rot_z=0.0, col_name="07_Lamps_And_Wall_Switches")

for idx, spos in enumerate([(1.65, 4.78, 2.05, 0.0), (5.78, 1.85, 2.05, -math.pi/2), (-5.78, 2.50, 2.05, math.pi/2), (1.80, -4.78, 2.05, math.pi)]):
    place_ph_model("Lantern_01", f"PH_Wall_Lantern_{idx}", (spos[0], spos[1], spos[2]), target_height=0.45, rot_z=spos[3], col_name="07_Lamps_And_Wall_Switches")

# 6. ROOFTOP LOUNGE, FAMILY TABLE, GRILL & POTTED PLANTS
place_ph_model("modern_coffee_table_01", "PH_Roof_Family_Table", (2.65, 1.40, 3.78), target_span_xy=(1.85, 1.10, 0.52), rot_z=0.0, col_name="08_FlatRoof_And_Rooftop_Grill_Lounge")
place_ph_model("stone_fire_pit", "PH_Roof_BBQ_Grill", (-4.65, 2.65, 4.72), target_span_xy=(0.88, 1.15, 0.55), rot_z=0.0, col_name="08_FlatRoof_And_Rooftop_Grill_Lounge")
for stool_y in (0.95, 1.95, 2.95):
    place_ph_model("bar_chair_round_01", f"PH_Roof_BarStool_{stool_y}", (-3.65, stool_y, 3.78), target_height=0.76, rot_z=0.0, col_name="08_FlatRoof_And_Rooftop_Grill_Lounge")
for tidx, tpos in enumerate([(-4.8, -3.5, 3.76), (5.0, -3.8, 3.76), (5.1, -8.2, 0.0)]):
    place_ph_model("potted_plant_02", f"PH_Villa_Plant_{tidx}", tpos, target_height=1.65, rot_z=tidx*1.1, col_name="08_FlatRoof_And_Rooftop_Grill_Lounge")

bpy.ops.wm.save_as_mainfile(filepath=blend_path)
glb_path = os.path.join(OUT_DIR, "tunisia_arab_villa.glb")
bpy.ops.export_scene.gltf(filepath=glb_path, export_format='GLB')

cam_obj = scene.camera
col_rooftop = bpy.data.collections.get("08_FlatRoof_And_Rooftop_Grill_Lounge")

def look_at(obj, target):
    direction = Vector(target) - obj.location
    rot_quat = direction.to_track_quat('-Z', 'Y')
    obj.rotation_euler = rot_quat.to_euler()

col_rooftop.hide_render = False
cam_obj.data.lens = 24
cam_obj.location = (11.2, -13.2, 10.8)
look_at(cam_obj, (0.5, -1.0, 2.2))
scene.render.filepath = os.path.join(OUT_DIR, "render_rooftop_and_exterior.png")
bpy.ops.render.render(write_still=True)

col_rooftop.hide_render = True
cam_obj.data.lens = 24
cam_obj.location = (0.3, -12.2, 12.2)
look_at(cam_obj, (0.0, -0.3, 0.6))
scene.render.filepath = os.path.join(OUT_DIR, "render_interior_floorplan_cutaway.png")
bpy.ops.render.render(write_still=True)

cam_obj.location = (0.2, -1.15, 1.95)
cam_obj.data.lens = 16
look_at(cam_obj, (0.0, 2.5, 1.15))
scene.render.filepath = os.path.join(OUT_DIR, "render_interior_majlis_and_bedroom.png")
bpy.ops.render.render(write_still=True)

col_rooftop.hide_render = False
bpy.ops.wm.save_as_mainfile(filepath=blend_path)
print("SUCCESS: Cleanly oriented all Poly Haven 3D models & bright Tunisian walls!")
