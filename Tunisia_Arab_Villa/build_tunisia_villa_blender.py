import bpy
import bmesh
import math
import os
from mathutils import Vector, Matrix

OUT_DIR = "/Users/dianjulie/Documents/Map Project/Tunisia_Arab_Villa"
PH_MODELS = os.path.join(OUT_DIR, "ph_models")
PH_TEX = os.path.join(OUT_DIR, "ph_textures")
os.makedirs(OUT_DIR, exist_ok=True)

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
scene.unit_settings.system = 'METRIC'
scene.unit_settings.scale_length = 1.0

def make_col(name, parent=None):
    col = bpy.data.collections.new(name)
    if parent:
        parent.children.link(col)
    else:
        scene.collection.children.link(col)
    return col

col_arch = make_col("01_Architecture_Walls_Floor")
col_openings = make_col("02_Doors_And_Windows")
col_living = make_col("03_Living_Majlis_And_TV")
col_bedroom = make_col("04_Bedroom_And_MiddleZone")
col_kitchen = make_col("05_Kitchen_And_Fridge")
col_bathroom = make_col("06_Bathroom_Shower_Toilet")
col_lighting = make_col("07_Lamps_And_Wall_Switches")
col_rooftop = make_col("08_FlatRoof_And_Rooftop_Grill_Lounge")

def link_obj(obj, col):
    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    col.objects.link(obj)

# ==============================================================================
# PROCEDURAL MODERN ARABIC ARCHITECTURAL TEXTURES (MASHRABIYA, TRAVERTINE, RUG)
# ==============================================================================
def create_mashrabiya_image(name, width=1024, height=1024):
    img = bpy.data.images.new(name, width=width, height=height)
    pixels = [0.0] * (width * height * 4)
    tile_px = 128
    for y in range(height):
        for x in range(width):
            tx = (x % tile_px) / float(tile_px) - 0.5
            ty = (y % tile_px) / float(tile_px) - 0.5
            ax, ay = abs(tx), abs(ty)
            d = math.sqrt(tx*tx + ty*ty)
            ang = math.atan2(ty, tx)
            star8 = 0.28 + 0.08 * math.cos(8.0 * ang)
            oct_ring = abs(ax + ay - 0.42) < 0.032 or abs(max(ax, ay) - 0.34) < 0.026
            diag_rib = abs(ax - ay) < 0.024 or abs(ax + ay - 0.22) < 0.022
            star_rib = abs(d - star8) < 0.026 or abs(d - 0.12) < 0.022
            border = (x % tile_px < 4) or (y % tile_px < 4)
            if border or oct_ring or star_rib or diag_rib:
                r, g, b = 0.92, 0.86, 0.74
            elif d < 0.10:
                r, g, b = 0.85, 0.68, 0.38
            elif d < star8:
                r, g, b = 0.54, 0.42, 0.26
            else:
                r, g, b = 0.42, 0.32, 0.20
            idx = (y * width + x) * 4
            pixels[idx] = r
            pixels[idx+1] = g
            pixels[idx+2] = b
            pixels[idx+3] = 1.0
    img.pixels = pixels
    img.pack()
    return img

def create_marble_floor_image(name, width=512, height=512):
    img = bpy.data.images.new(name, width=width, height=height)
    pixels = [0.0] * (width * height * 4)
    tile_px = 128
    for y in range(height):
        for x in range(width):
            grout = (x % tile_px < 2) or (y % tile_px < 2)
            vein = math.sin(x * 0.045 + math.sin(y * 0.035) * 2.5) * 0.5 + 0.5
            if grout:
                r, g, b = 0.72, 0.67, 0.59
            else:
                v = 0.90 + 0.06 * vein
                r, g, b = v, v * 0.96, v * 0.90
            idx = (y * width + x) * 4
            pixels[idx] = r
            pixels[idx+1] = g
            pixels[idx+2] = b
            pixels[idx+3] = 1.0
    img.pixels = pixels
    img.pack()
    return img

def create_modern_courtyard_image(name, width=1024, height=1024):
    img = bpy.data.images.new(name, width=width, height=height)
    pixels = [0.0] * (width * height * 4)
    for y in range(height):
        for x in range(width):
            u = x / float(width) - 0.5
            v = y / float(height) - 0.5
            bu, bv = abs(u), abs(v)
            in_medallion = (bu < 0.28 and bv < 0.28)
            channel = (x % 256 < 14) or (y % 256 < 14)
            grout = (x % 64 < 2) or (y % 64 < 2)
            noise = math.sin(x * 0.08) * math.cos(y * 0.08) * 0.025
            if in_medallion:
                border_m = (abs(bu - 0.26) < 0.015) or (abs(bv - 0.26) < 0.015)
                d = math.sqrt(u*u + v*v)
                ang = math.atan2(v, u)
                star = 0.16 + 0.045 * math.cos(8.0 * ang)
                if border_m or abs(d - star) < 0.012 or abs(bu - bv) < 0.010:
                    r, g, b = 0.22, 0.24, 0.28
                elif d < star:
                    r, g, b = 0.84 + noise, 0.76 + noise, 0.62
                else:
                    r, g, b = 0.92 + noise, 0.89 + noise, 0.83
            elif channel:
                peb = 0.22 + 0.06 * math.sin(x * 0.7) * math.cos(y * 0.7)
                r, g, b = peb, peb * 0.98, peb * 0.95
            elif grout:
                r, g, b = 0.72, 0.68, 0.60
            else:
                r, g, b = 0.91 + noise, 0.86 + noise, 0.78 + noise
            idx = (y * width + x) * 4
            pixels[idx] = r
            pixels[idx+1] = g
            pixels[idx+2] = b
            pixels[idx+3] = 1.0
    img.pixels = pixels
    img.pack()
    return img

def create_zellige_image(name, width=512, height=512):
    img = bpy.data.images.new(name, width=width, height=height)
    pixels = [0.0] * (width * height * 4)
    tile_px = 64
    for y in range(height):
        for x in range(width):
            tx = (x % tile_px) / float(tile_px) - 0.5
            ty = (y % tile_px) / float(tile_px) - 0.5
            d = math.sqrt(tx*tx + ty*ty)
            ang = math.atan2(ty, tx)
            star8 = 0.27 + 0.075 * math.cos(8.0 * ang)
            grout = (x % tile_px < 2) or (y % tile_px < 2) or abs(d - star8) < 0.016
            if grout:
                r, g, b = 0.86, 0.82, 0.75
            elif d < 0.09:
                r, g, b = 0.82, 0.62, 0.24
            elif d < star8:
                r, g, b = 0.16, 0.36, 0.54
            else:
                r, g, b = 0.94, 0.91, 0.85
            idx = (y * width + x) * 4
            pixels[idx] = r
            pixels[idx+1] = g
            pixels[idx+2] = b
            pixels[idx+3] = 1.0
    img.pixels = pixels
    img.pack()
    return img

def create_rug_image(name, width=512, height=512):
    img = bpy.data.images.new(name, width=width, height=height)
    pixels = [0.0] * (width * height * 4)
    for y in range(height):
        for x in range(width):
            u = x / float(width) - 0.5
            v = y / float(height) - 0.5
            bx, by = abs(u), abs(v)
            d = abs(u * 1.35) + abs(v * 1.35)
            pat = math.sin(x * 0.25) * math.cos(y * 0.25)
            if bx > 0.45 or by > 0.45:
                r, g, b = 0.26, 0.20, 0.15
            elif bx > 0.41 or by > 0.41:
                r, g, b = 0.78, 0.62, 0.34
            elif abs(d - 0.26) < 0.03 or abs(d - 0.12) < 0.025:
                r, g, b = 0.55, 0.38, 0.22
            elif d < 0.24:
                r, g, b = 0.82 + 0.03*pat, 0.74, 0.62
            else:
                r, g, b = 0.92 - 0.02*pat, 0.88 - 0.02*pat, 0.80
            idx = (y * width + x) * 4
            pixels[idx] = r
            pixels[idx+1] = g
            pixels[idx+2] = b
            pixels[idx+3] = 1.0
    img.pixels = pixels
    img.pack()
    return img

def create_ao_decal_image(name, width=256, height=256):
    img = bpy.data.images.new(name, width=width, height=height)
    pixels = [0.0] * (width * height * 4)
    for y in range(height):
        for x in range(width):
            u = (x / float(width) - 0.5) * 2.0
            v = (y / float(height) - 0.5) * 2.0
            dist = max(abs(u), abs(v))
            alpha = max(0.0, min(1.0, (1.0 - dist) * 1.6)) ** 1.5 * 0.48
            idx = (y * width + x) * 4
            pixels[idx] = 0.04
            pixels[idx+1] = 0.03
            pixels[idx+2] = 0.02
            pixels[idx+3] = alpha
    img.pixels = pixels
    img.pack()
    return img

img_mashrabiya = create_mashrabiya_image("Tex_Modern_Mashrabiya")
img_zellige = create_zellige_image("Tex_Tunisian_Zellige")
img_marble = create_marble_floor_image("Tex_Carthage_Marble")
img_courtyard = create_modern_courtyard_image("Tex_Courtyard_Travertine")
img_rug = create_rug_image("Tex_Luxury_Berber_Rug")
img_ao = create_ao_decal_image("Tex_Contact_AO")

def make_mat(name, color=(0.9,0.9,0.9,1.0), rough=0.4, metal=0.0, emission=None, emission_strength=0.0, img=None, normal_jpg=None, normal_strength=0.45, alpha=1.0, is_ao=False):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    bsdf = nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = color
    bsdf.inputs["Roughness"].default_value = rough
    bsdf.inputs["Metallic"].default_value = metal
    if alpha < 1.0 or is_ao:
        if "Alpha" in bsdf.inputs:
            bsdf.inputs["Alpha"].default_value = alpha
        if hasattr(mat, 'surface_render_method'):
            mat.surface_render_method = 'BLENDED'
    if emission and "Emission Color" in bsdf.inputs:
        bsdf.inputs["Emission Color"].default_value = emission
        bsdf.inputs["Emission Strength"].default_value = emission_strength
    if img:
        tex = nodes.new("ShaderNodeTexImage")
        tex.image = img
        links.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
        if is_ao and "Alpha" in bsdf.inputs:
            links.new(tex.outputs["Alpha"], bsdf.inputs["Alpha"])
    if normal_jpg:
        npath = os.path.join(PH_TEX, normal_jpg)
        if os.path.exists(npath):
            nimg = bpy.data.images.load(npath, check_existing=True)
            nimg.colorspace_settings.name = 'Non-Color'
            nimg.pack()
            ntex = nodes.new("ShaderNodeTexImage")
            ntex.image = nimg
            nmap = nodes.new("ShaderNodeNormalMap")
            nmap.inputs["Strength"].default_value = normal_strength
            links.new(ntex.outputs["Color"], nmap.inputs["Color"])
            links.new(nmap.outputs["Normal"], bsdf.inputs["Normal"])
    return mat

mat_wall_plaster = make_mat("Mat_Wall_Tadelakt_Sand", (0.95, 0.92, 0.86, 1), rough=0.52, normal_jpg="clay_plaster_nor.jpg", normal_strength=0.35)
mat_wall_exterior = make_mat("Mat_Wall_Exterior_Limestone", (0.96, 0.93, 0.87, 1), rough=0.48, normal_jpg="clay_plaster_nor.jpg", normal_strength=0.40)
mat_mashrabiya = make_mat("Mat_Carved_Mashrabiya_Panel", (0.92, 0.85, 0.72, 1), rough=0.36, img=img_mashrabiya, normal_jpg="floor_pattern_01_nor.jpg", normal_strength=0.65)
mat_wall_motif = make_mat("Mat_Wall_Arab_Zellige_Motif", (0.95, 0.95, 0.95, 1), rough=0.18, img=img_zellige, normal_jpg="blue_floor_tiles_01_nor.jpg", normal_strength=0.55)
mat_stucco_relief = make_mat("Mat_Champagne_Limestone_Trim", (0.89, 0.84, 0.75, 1), rough=0.38)
mat_floor_marble = make_mat("Mat_Floor_Carthage_Marble", (0.93, 0.90, 0.84, 1), rough=0.15, img=img_marble, normal_jpg="marble_01_nor.jpg", normal_strength=0.25)
mat_floor_courtyard = make_mat("Mat_Floor_Courtyard_Patio", (0.92, 0.88, 0.81, 1), rough=0.28, img=img_courtyard, normal_jpg="large_floor_tiles_02_nor.jpg", normal_strength=0.45)
mat_floor_bath = make_mat("Mat_Floor_Hammam_Zellige", (0.92, 0.92, 0.92, 1), rough=0.18, img=img_zellige)
mat_cedar_wood = make_mat("Mat_Royal_Walnut_Wood", (0.24, 0.13, 0.06, 1), rough=0.28)
mat_dark_bronze = make_mat("Mat_Architectural_Bronze", (0.14, 0.12, 0.10, 1), rough=0.26, metal=0.82)
mat_brass_gold = make_mat("Mat_Brushed_Champagne_Brass", (0.84, 0.66, 0.30, 1), rough=0.22, metal=0.88)
mat_copper = make_mat("Mat_Polished_Copper", (0.82, 0.45, 0.25, 1), rough=0.20, metal=0.90)
mat_velvet_cream = make_mat("Mat_Majlis_Warm_Cream", (0.93, 0.89, 0.81, 1), rough=0.58)
mat_terracotta = make_mat("Mat_Warm_Terracotta", (0.68, 0.36, 0.22, 1), rough=0.52)
mat_rug = make_mat("Mat_Luxury_Berber_Carpet", (0.9, 0.9, 0.9, 1), rough=0.82, img=img_rug)
mat_glass = make_mat("Mat_Arch_Glass", (0.72, 0.88, 0.96, 1), rough=0.03, metal=0.15, alpha=0.26)
mat_tv_screen = make_mat("Mat_OLED_TV_Screen", (0.03, 0.05, 0.08, 1), rough=0.06, metal=0.2, emission=(0.14, 0.32, 0.50, 1), emission_strength=0.85)
mat_lamp_glow = make_mat("Mat_Warm_Arabian_Lamp_Glow", (1.0, 0.72, 0.28, 1), rough=0.15, emission=(1.0, 0.68, 0.22, 1), emission_strength=14.0)
mat_led_border = make_mat("Mat_Arch_Border_LED_Strip", (1.0, 0.74, 0.30, 1), rough=0.12, emission=(1.0, 0.68, 0.22, 1), emission_strength=13.5)
mat_fridge_led = make_mat("Mat_Fridge_Dispenser_LED", (0.20, 0.75, 1.0, 1), rough=0.1, emission=(0.20, 0.75, 1.0, 1), emission_strength=4.5)
mat_switch_on = make_mat("Mat_Switch_Indicator_ON", (0.10, 0.95, 0.42, 1), rough=0.2, emission=(0.10, 0.95, 0.42, 1), emission_strength=4.5)
mat_chrome = make_mat("Mat_Brushed_Steel", (0.68, 0.71, 0.75, 1), rough=0.22, metal=0.90)
mat_dark_steel = make_mat("Mat_Dark_Gunmetal_Steel", (0.22, 0.24, 0.27, 1), rough=0.25, metal=0.88)
mat_porcelain = make_mat("Mat_White_Porcelain", (0.96, 0.96, 0.98, 1), rough=0.10)
mat_charcoal = make_mat("Mat_Charcoal_Basalt", (0.12, 0.13, 0.15, 1), rough=0.30, metal=0.65)
mat_water = make_mat("Mat_Fountain_Water", (0.12, 0.38, 0.46, 1), rough=0.04, metal=0.15)
mat_ao = make_mat("Mat_Contact_AO_Decal", (0.02, 0.02, 0.02, 1), rough=0.95, img=img_ao, is_ao=True)

def apply_box_uv(obj, sx, sy, sz, uv_mode='WORLD', scale=0.5):
    mesh = obj.data
    bm = bmesh.new()
    bm.from_mesh(mesh)
    uv_layer = bm.loops.layers.uv.verify()
    for face in bm.faces:
        n = face.normal
        for loop in face.loops:
            co = loop.vert.co
            if uv_mode == 'FIT_TOP':
                u = (co.x / max(0.001, sx)) + 0.5
                v = (co.y / max(0.001, sy)) + 0.5
            else:
                if abs(n.z) > 0.7:
                    u = (co.x + sx*0.5) * scale
                    v = (co.y + sy*0.5) * scale
                elif abs(n.y) > 0.7:
                    u = (co.x + sx*0.5) * scale
                    v = (co.z + sz*0.5) * scale
                else:
                    u = (co.y + sy*0.5) * scale
                    v = (co.z + sz*0.5) * scale
            loop[uv_layer].uv = (u, v)
    bm.to_mesh(mesh)
    bm.free()

def add_box(name, size, loc, mat, col, rot=(0,0,0), bevel=0.012, uv_mode='WORLD', uv_scale=0.5):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=loc, rotation=rot)
    obj = bpy.context.active_object
    obj.name = name
    obj.scale = size
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    apply_box_uv(obj, size[0], size[1], size[2], uv_mode=uv_mode, scale=uv_scale)
    if bevel > 0:
        bev = obj.modifiers.new("Bevel", 'BEVEL')
        bev.width = bevel
        bev.segments = 2
    obj.data.materials.append(mat)
    link_obj(obj, col)
    return obj

def add_ao_decal(name, sx, sy, x, y, z, col):
    return add_box(name, (sx, sy, 0.004), (x, y, z + 0.003), mat_ao, col, bevel=0.0, uv_mode='FIT_TOP')

def add_cyl(name, r, h, loc, mat, col, rot=(0,0,0), verts=32):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=h, location=loc, rotation=rot)
    obj = bpy.context.active_object
    obj.name = name
    for p in obj.data.polygons:
        p.use_smooth = True
    obj.data.materials.append(mat)
    link_obj(obj, col)
    return obj

# ==============================================================================
# MATHEMATICAL ARCH HELPERS: SMOOTH ARCH FRAME, ARCH-CUT WALL SPANDREL & ARCH MULLIONS
# ==============================================================================
def arch_curve_z(x_local, inner_w, inner_h, pointed=0.14):
    """Returns exact Z height of the arch curve at horizontal offset x_local."""
    rx = inner_w * 0.5
    spring_z = max(0.35, inner_h - rx * (1.0 + pointed))
    rz = inner_h - spring_z
    u = max(-1.0, min(1.0, x_local / max(0.001, rx)))
    st = math.sqrt(max(0.0, 1.0 - u * u))
    apex_boost = pointed * rx * (st ** 2.2)
    return spring_z + st * rz + apex_boost

def build_wall_arch_spandrel(name, span_w, bottom_arch_w, bottom_arch_h, top_z, thickness, loc, rot_z, mat, col, pointed=0.14, segments=48):
    """Builds the wall section ABOVE an arch opening so the wall itself is cut to the exact arch curve (NO flat rectangular header!)."""
    mesh = bpy.data.meshes.new(name)
    bm = bmesh.new()
    rx = bottom_arch_w * 0.5
    spring_z = max(0.35, bottom_arch_h - rx * (1.0 + pointed))
    rz = bottom_arch_h - spring_z
    hw = span_w * 0.5
    hy = thickness * 0.5

    # Build quad strips from left (-hw) to right (+hw) between the arch curve (bottom) and top_z (ceiling)
    xs = [-hw]
    for i in range(segments + 1):
        t = math.pi - (i / float(segments)) * math.pi
        xs.append(math.cos(t) * rx)
    xs.append(hw)

    rings = []
    for x in xs:
        if abs(x) >= rx:
            z_bot = spring_z
        else:
            z_bot = arch_curve_z(x, bottom_arch_w, bottom_arch_h, pointed=pointed)
        v0 = bm.verts.new((x, -hy, z_bot))
        v1 = bm.verts.new((x, -hy, top_z))
        v2 = bm.verts.new((x,  hy, top_z))
        v3 = bm.verts.new((x,  hy, z_bot))
        rings.append((v0, v1, v2, v3))

    for i in range(len(rings) - 1):
        a0, a1, a2, a3 = rings[i]
        b0, b1, b2, b3 = rings[i+1]
        bm.faces.new((a0, b0, b1, a1)) # Front face
        bm.faces.new((a1, b1, b2, a2)) # Top face
        bm.faces.new((a2, b2, b3, a3)) # Back face
        bm.faces.new((a3, b3, b0, a0)) # Curved Arch Intrados (underside)
    # Cap left & right ends
    L0, L1, L2, L3 = rings[0]
    bm.faces.new((L0, L1, L2, L3))
    R0, R1, R2, R3 = rings[-1]
    bm.faces.new((R0, R3, R2, R1))

    bm.normal_update()
    bm.to_mesh(mesh)
    bm.free()

    obj = bpy.data.objects.new(name, mesh)
    obj.location = loc
    obj.rotation_euler = (0, 0, rot_z)
    apply_box_uv(obj, span_w, thickness, top_z, scale=0.5)
    obj.data.materials.append(mat)
    col.objects.link(obj)
    return obj

def build_smooth_arch_ribbon(name, inner_w, inner_h, frame_w, depth, mat, col, pointed=0.14, segments=48):
    mesh = bpy.data.meshes.new(name)
    bm = bmesh.new()
    rx = inner_w * 0.5
    spring_z = max(0.35, inner_h - rx * (1.0 + pointed))
    rz = inner_h - spring_z

    pts_inner = [(rx, 0.0)]
    pts_outer = [(rx + frame_w, 0.0)]

    for i in range(segments + 1):
        t = (i / float(segments)) * math.pi
        ct = math.cos(t)
        st = math.sin(t)
        apex_boost = pointed * rx * (st ** 2.2)
        ix = ct * rx
        iz = spring_z + st * rz + apex_boost
        nx, nz = ct, st
        nlen = max(0.001, math.sqrt(nx*nx + nz*nz))
        nx /= nlen; nz /= nlen
        pts_inner.append((ix, iz))
        pts_outer.append((ix + nx * frame_w, iz + nz * frame_w))

    pts_inner.append((-rx, 0.0))
    pts_outer.append((-(rx + frame_w), 0.0))

    hy = depth * 0.5
    rings = []
    for (ix, iz), (ox, oz) in zip(pts_inner, pts_outer):
        v0 = bm.verts.new((ix, -hy, iz))
        v1 = bm.verts.new((ox, -hy, iz))
        v2 = bm.verts.new((ox,  hy, iz))
        v3 = bm.verts.new((ix,  hy, iz))
        rings.append((v0, v1, v2, v3))

    for i in range(len(rings) - 1):
        a0, a1, a2, a3 = rings[i]
        b0, b1, b2, b3 = rings[i+1]
        bm.faces.new((a0, a1, b1, b0))
        bm.faces.new((a1, a2, b2, b1))
        bm.faces.new((a2, a3, b3, b2))
        bm.faces.new((a3, a0, b0, b3))

    bm.normal_update()
    for f in bm.faces:
        f.smooth = True
    bm.to_mesh(mesh)
    bm.free()

    obj = bpy.data.objects.new(name, mesh)
    obj.data.materials.append(mat)
    col.objects.link(obj)
    return obj

def build_arch_backpanel(name, inner_w, inner_h, thickness, y_offset, mat, col, pointed=0.14, segments=48, z_start=0.0, z_end=None):
    """Builds a true arch-shaped panel (for arch-shaped glass, arch-shaped wooden door leaf, or Mashrabiya transom)."""
    mesh = bpy.data.meshes.new(name)
    bm = bmesh.new()
    rx = inner_w * 0.5
    spring_z = max(0.35, inner_h - rx * (1.0 + pointed))
    rz = inner_h - spring_z

    hy = thickness * 0.5
    pts = [(rx, z_start)]
    for i in range(segments + 1):
        t = (i / float(segments)) * math.pi
        ct = math.cos(t)
        st = math.sin(t)
        apex_boost = pointed * rx * (st ** 2.2)
        ix = ct * rx
        iz = spring_z + st * rz + apex_boost
        if z_end is not None:
            iz = min(iz, z_end)
        if iz >= z_start:
            pts.append((ix, iz))
    pts.append((-rx, z_start))

    verts_front = [bm.verts.new((px, y_offset - hy, pz)) for px, pz in pts]
    verts_back = [bm.verts.new((px, y_offset + hy, pz)) for px, pz in pts]

    f_front = bm.faces.new(verts_front)
    f_back = bm.faces.new(list(reversed(verts_back)))
    for i in range(len(pts)):
        jn = (i + 1) % len(pts)
        bm.faces.new((verts_front[i], verts_front[jn], verts_back[jn], verts_back[i]))

    uv_layer = bm.loops.layers.uv.verify()
    for face in bm.faces:
        for loop in face.loops:
            co = loop.vert.co
            loop[uv_layer].uv = (co.x * 0.65 + 0.5, co.z * 0.65)
    bm.normal_update()
    bm.to_mesh(mesh)
    bm.free()

    obj = bpy.data.objects.new(name, mesh)
    obj.data.materials.append(mat)
    col.objects.link(obj)
    return obj

def add_modern_arabic_arch(name, width, height, depth, loc, rot_z, mat_frame, col, has_led=True, infill_mat=None, infill_z_start=0.0, pointed=0.14):
    parent = bpy.data.objects.new(name, None)
    parent.location = loc
    parent.rotation_euler = (0, 0, rot_z)
    col.objects.link(parent)

    inner_w = width - 0.22
    inner_h = height - 0.11
    outer = build_smooth_arch_ribbon(f"{name}_Frame", inner_w, inner_h, 0.11, depth, mat_frame, col, pointed=pointed)
    outer.parent = parent

    if has_led:
        led = build_smooth_arch_ribbon(f"{name}_LED_Border", inner_w - 0.05, inner_h - 0.025, 0.045, depth * 0.92, mat_led_border, col, pointed=pointed)
        led.parent = parent

    if infill_mat is not None:
        panel = build_arch_backpanel(f"{name}_Infill", inner_w - 0.02, inner_h - 0.01, 0.025, 0.0, infill_mat, col, pointed=pointed, z_start=infill_z_start)
        panel.parent = parent

    return parent

def add_arched_window_assembly(name, width, height, depth, loc, rot_z, col, pointed=0.14):
    """Builds a 100% arch-shaped window where the glass pane, inner wood sash, vertical mullions, and radial fanlight bars follow the exact arch curve!"""
    parent = add_modern_arabic_arch(name, width, height, depth, loc, rot_z, mat_stucco_relief, col, has_led=True, infill_mat=mat_glass, infill_z_start=0.0, pointed=pointed)
    inner_w = width - 0.24
    inner_h = height - 0.12
    rx = inner_w * 0.5
    spring_z = max(0.35, inner_h - rx * (1.0 + pointed))

    # Inner dark walnut curved sash ribbon following the exact arch
    sash = build_smooth_arch_ribbon(f"{name}_WalnutSash", inner_w - 0.08, inner_h - 0.04, 0.045, 0.07, mat_cedar_wood, col, pointed=pointed)
    sash.parent = parent

    # Vertical mullions clipped to the exact height of the arch curve at their X coordinate!
    for mx in (-rx * 0.48, 0.0, rx * 0.48):
        z_top = arch_curve_z(mx, inner_w - 0.06, inner_h - 0.03, pointed=pointed)
        m_v = add_box(f"{name}_MullionV_{mx:.2f}", (0.035, 0.055, z_top), (mx, 0.0, z_top * 0.5), mat_cedar_wood, col, bevel=0.004)
        m_v.parent = parent

    # Horizontal transom bar at the arch spring line + lower horizontal bar
    for hz in (spring_z * 0.52, spring_z):
        m_h = add_box(f"{name}_MullionH_{hz:.2f}", (inner_w - 0.04, 0.055, 0.035), (0.0, 0.0, hz), mat_cedar_wood, col, bevel=0.004)
        m_h.parent = parent

    # Radial sunburst fanlight bars inside the curved arch top (like Reference Photo 4!)
    for ang_deg in (35, 68, 112, 145):
        ang = math.radians(ang_deg)
        ray_len = rx * 0.92
        cx = math.cos(ang) * (ray_len * 0.5)
        cz = spring_z + math.sin(ang) * (ray_len * 0.5)
        ray = add_box(f"{name}_FanRay_{ang_deg}", (ray_len, 0.045, 0.028), (cx, 0.0, cz), mat_cedar_wood, col, rot=(0, -(ang), 0), bevel=0.003)
        ray.parent = parent

    return parent

def add_arched_door_assembly(name, width, height, depth, loc, rot_z, col, has_mashrabiya_fanlight=True, pointed=0.16):
    """Builds a 100% arch-shaped door portal where the door leaf / fanlight is curved to match the arch opening!"""
    inner_w = width - 0.24
    inner_h = height - 0.12
    rx = inner_w * 0.5
    spring_z = max(0.35, inner_h - rx * (1.0 + pointed))

    parent = add_modern_arabic_arch(
        name, width, height, depth, loc, rot_z, mat_stucco_relief, col,
        has_led=True,
        infill_mat=mat_mashrabiya if has_mashrabiya_fanlight else None,
        infill_z_start=spring_z if has_mashrabiya_fanlight else 0.0,
        pointed=pointed
    )
    # Inner dark walnut curved door jambs & arch sash
    sash = build_smooth_arch_ribbon(f"{name}_WalnutJamb", inner_w - 0.08, inner_h - 0.04, 0.05, 0.12, mat_cedar_wood, col, pointed=pointed)
    sash.parent = parent

    if has_mashrabiya_fanlight:
        # Door leaves up to spring_z + curved arch transom molding above
        leaf = add_box(f"{name}_DoorLeaf", (inner_w - 0.06, 0.08, spring_z), (0.0, 0.0, spring_z * 0.5), mat_cedar_wood, col, bevel=0.008)
        leaf.parent = parent
        transom = add_box(f"{name}_TransomBar", (inner_w, 0.12, 0.055), (0.0, 0.0, spring_z), mat_cedar_wood, col, bevel=0.006)
        transom.parent = parent
    else:
        # Full arch-shaped wooden door leaf all the way to the curved arch apex!
        leaf = build_arch_backpanel(f"{name}_ArchDoorLeaf", inner_w - 0.06, inner_h - 0.03, 0.08, 0.0, mat_cedar_wood, col, pointed=pointed, z_start=0.0)
        leaf.parent = parent

    # Center double-door vertical seam & Luxury Brushed Brass Pull Handles
    seam = add_box(f"{name}_CenterSeam", (0.018, 0.095, spring_z - 0.05), (0.0, 0.0, spring_z * 0.5), mat_dark_bronze, col, bevel=0.002)
    seam.parent = parent
    for side in (-1, 1):
        # Recessed decorative panels on each door leaf
        for pz, ph in ((0.55, 0.72), (1.52, 0.85)):
            pan = add_box(f"{name}_Panel_{side}_{pz}", (inner_w * 0.34, 0.10, ph), (side * inner_w * 0.24, 0.0, pz), mat_cedar_wood, col, bevel=0.01)
            pan.parent = parent
        h_bar = add_cyl(f"{name}_Handle_{side}", 0.016, 0.62, (side * 0.085, -0.065, 1.08), mat_brass_gold, col)
        h_bar.parent = parent
        h_in = add_cyl(f"{name}_HandleIn_{side}", 0.016, 0.62, (side * 0.085, 0.065, 1.08), mat_brass_gold, col)
        h_in.parent = parent

    return parent

# ==============================================================================
# 1. FLOORPLAN ARCHITECTURE + ARCH-CUT WALL OPENINGS
# ==============================================================================
WALL_H = 3.50
WALL_T = 0.24

add_box("Floor_Main_House", (12.0, 10.0, 0.20), (0.0, 0.0, -0.10), mat_floor_marble, col_arch, bevel=0.005, uv_scale=0.35)
add_box("Floor_Bathroom_Hammam", (3.90, 3.80, 0.025), (-4.05, -3.10, 0.012), mat_floor_bath, col_arch, bevel=0.002, uv_scale=0.85)
add_box("Floor_Front_Courtyard_Travertine", (4.80, 4.40, 0.20), (3.70, -7.10, -0.10), mat_floor_courtyard, col_arch, bevel=0.005, uv_mode='FIT_TOP')

for step_i, (sy, sz, sw) in enumerate([(-5.18, 0.06, 1.65), (-5.36, 0.03, 1.85)]):
    add_box(f"Entrance_Travertine_Step_{step_i}", (sw, 0.28, 0.06), (2.60, sy, sz), mat_floor_marble, col_arch)
    add_box(f"Entrance_Step_LED_{step_i}", (sw - 0.08, 0.02, 0.018), (2.60, sy - 0.14, sz - 0.01), mat_led_border, col_lighting, bevel=0.0)

for cx_led in (2.30, 3.70, 5.10):
    add_box(f"Courtyard_Ground_LED_{cx_led}", (0.035, 3.80, 0.008), (cx_led, -7.15, 0.004), mat_led_border, col_lighting, bevel=0.0)

add_box("Courtyard_Fountain_Rim", (1.25, 1.25, 0.34), (4.95, -7.85, 0.17), mat_wall_exterior, col_arch)
add_box("Courtyard_Fountain_Water", (1.05, 1.05, 0.28), (4.95, -7.85, 0.16), mat_water, col_arch)
add_cyl("Courtyard_Fountain_Bowl", 0.32, 0.18, (4.95, -7.85, 0.38), mat_charcoal, col_arch, verts=24)

# Baseboards & Crown Moldings
add_box("Crown_North", (11.8, 0.12, 0.14), (0.0, 4.84, WALL_H - 0.07), mat_cedar_wood, col_arch)
add_box("Crown_East", (0.12, 9.8, 0.14), (5.84, 0.0, WALL_H - 0.07), mat_cedar_wood, col_arch)
add_box("Crown_West", (0.12, 9.8, 0.14), (-5.84, 0.0, WALL_H - 0.07), mat_cedar_wood, col_arch)
add_box("Ceiling_LED_Cove_North", (11.4, 0.03, 0.025), (0.0, 4.77, WALL_H - 0.14), mat_led_border, col_lighting, bevel=0.0)
add_box("Baseboard_North", (11.8, 0.05, 0.12), (0.0, 4.86, 0.06), mat_cedar_wood, col_arch)
add_box("Baseboard_East", (0.05, 9.8, 0.12), (5.86, 0.0, 0.06), mat_cedar_wood, col_arch)

# NORTH WALL: EQUIDISTANT HORIZONTAL DISTRIBUTION CLEAR OF KING BED (X = -2.50, +0.55, +3.60)
add_box("Wall_North_Main", (12.24, WALL_T, WALL_H), (0.0, 5.0, WALL_H/2), mat_wall_plaster, col_arch)
for idx, ax in enumerate((-2.50, 0.55, 3.60)):
    add_modern_arabic_arch(
        f"Arch_Relief_North_{idx}", width=2.35, height=3.08, depth=0.11,
        loc=(ax, 4.84, 0.0), rot_z=0.0, mat_frame=mat_stucco_relief, col=col_arch,
        has_led=True, infill_mat=mat_mashrabiya, infill_z_start=0.0, pointed=0.14
    )

# EAST WALL
add_box("Wall_East_Main", (WALL_T, 10.0, WALL_H), (6.0, 0.0, WALL_H/2), mat_wall_plaster, col_arch)
add_modern_arabic_arch(
    "Arch_Relief_East_Majlis", width=2.85, height=3.08, depth=0.11,
    loc=(5.84, 1.85, 0.0), rot_z=math.pi/2, mat_frame=mat_stucco_relief, col=col_arch,
    has_led=True, infill_mat=mat_mashrabiya, infill_z_start=0.0, pointed=0.14
)

# WEST WALL WITH TRUE ARCH-CUT WINDOW OPENING AT Y = 0.0
add_box("Wall_West_NorthSeg", (WALL_T, 4.30, WALL_H), (-6.0, 2.85, WALL_H/2), mat_wall_plaster, col_arch)
add_box("Wall_West_SouthSeg", (WALL_T, 4.30, WALL_H), (-6.0, -2.85, WALL_H/2), mat_wall_plaster, col_arch)
add_box("Wall_West_WinSill", (WALL_T, 1.40, 0.85), (-6.0, 0.0, 0.425), mat_wall_plaster, col_arch)
build_wall_arch_spandrel(
    "Wall_West_WinArchSpandrel", span_w=1.40, bottom_arch_w=1.18, bottom_arch_h=1.93,
    top_z=WALL_H - 0.85, thickness=WALL_T, loc=(-6.0, 0.0, 0.85), rot_z=math.pi/2,
    mat=mat_wall_plaster, col=col_arch, pointed=0.14
)

# SOUTH WALL LEFT & CENTER (Bathroom + Refrigerator + Kitchen Set Back Wall)
add_box("Wall_South_Bath_And_Kitchen", (7.40, WALL_T, WALL_H), (-2.30, -5.0, WALL_H/2), mat_wall_plaster, col_arch)
for ext_x in (-4.40, -0.80):
    add_modern_arabic_arch(
        f"Exterior_South_Mashrabiya_Arch_{ext_x}", width=2.20, height=3.05, depth=0.09,
        loc=(ext_x, -5.14, 0.15), rot_z=0.0, mat_frame=mat_stucco_relief, col=col_arch,
        has_led=True, infill_mat=mat_mashrabiya, infill_z_start=0.0, pointed=0.15
    )

# SOUTH WALL RIGHT WITH TRUE ARCH-CUT DOOR & WINDOW SPANDRELS (NO FLAT HEADER BOXES!)
add_box("Wall_South_DoorLeftPier", (0.52, WALL_T, WALL_H), (1.66, -5.0, WALL_H/2), mat_wall_exterior, col_arch)
build_wall_arch_spandrel(
    "Wall_South_DoorArchSpandrel", span_w=1.36, bottom_arch_w=1.14, bottom_arch_h=2.93,
    top_z=WALL_H, thickness=WALL_T, loc=(2.60, -5.0, 0.0), rot_z=0.0,
    mat=mat_wall_exterior, col=col_arch, pointed=0.16
)
add_box("Wall_South_MidPier", (0.76, WALL_T, WALL_H), (3.66, -5.0, WALL_H/2), mat_wall_exterior, col_arch)
add_box("Wall_South_WinSill", (1.32, WALL_T, 0.85), (4.70, -5.0, 0.425), mat_wall_exterior, col_arch)
build_wall_arch_spandrel(
    "Wall_South_WinArchSpandrel", span_w=1.32, bottom_arch_w=1.10, bottom_arch_h=1.93,
    top_z=WALL_H - 0.85, thickness=WALL_T, loc=(4.70, -5.0, 0.85), rot_z=0.0,
    mat=mat_wall_exterior, col=col_arch, pointed=0.14
)
add_box("Wall_South_EastPier", (0.64, WALL_T, WALL_H), (5.68, -5.0, WALL_H/2), mat_wall_exterior, col_arch)

# COURTYARD WALLS
add_box("Wall_Teal_Interior_Kitchen_Divider", (0.22, 3.40, WALL_H), (1.40, -3.30, WALL_H/2), mat_wall_plaster, col_arch)
add_box("Wall_Courtyard_West_Wing", (0.24, 4.20, 2.65), (1.40, -7.10, 1.325), mat_wall_exterior, col_arch)
add_box("Wall_Courtyard_West_Coping", (0.30, 4.28, 0.08), (1.40, -7.10, 2.68), mat_stucco_relief, col_arch)
add_modern_arabic_arch(
    "Courtyard_West_Wall_Niche", width=2.40, height=2.25, depth=0.08,
    loc=(1.54, -7.10, 0.15), rot_z=math.pi/2, mat_frame=mat_stucco_relief, col=col_arch,
    has_led=True, infill_mat=mat_mashrabiya, infill_z_start=0.0, pointed=0.14
)
add_box("Wall_Courtyard_East_Low", (0.24, 4.20, 1.15), (6.00, -7.10, 0.575), mat_wall_exterior, col_arch)
add_box("Wall_Courtyard_South_Low", (2.65, 0.24, 1.15), (4.68, -9.20, 0.575), mat_wall_exterior, col_arch)
add_modern_arabic_arch(
    "Courtyard_Welcome_Arch", width=1.95, height=2.85, depth=0.32,
    loc=(2.38, -9.20, 0.0), rot_z=0.0, mat_frame=mat_wall_exterior, col=col_arch,
    has_led=True, infill_mat=None, pointed=0.18
)

# SHOWER AND TOILET ENCLOSED ROOM WALLS WITH ARCH-CUT DOOR SPANDREL
add_box("Wall_Bathroom_North", (3.90, 0.18, WALL_H), (-4.05, -1.20, WALL_H/2), mat_wall_plaster, col_arch)
add_box("Wall_Bathroom_East_SouthSeg", (0.18, 2.62, WALL_H), (-2.10, -3.69, WALL_H/2), mat_wall_plaster, col_arch)
build_wall_arch_spandrel(
    "Wall_Bathroom_East_DoorArchSpandrel", span_w=1.06, bottom_arch_w=0.84, bottom_arch_h=2.43,
    top_z=WALL_H, thickness=0.18, loc=(-2.10, -1.85, 0.0), rot_z=math.pi/2,
    mat=mat_wall_plaster, col=col_arch, pointed=0.14
)
add_box("Wall_Bathroom_East_NorthCorner", (0.18, 0.12, WALL_H), (-2.10, -1.26, WALL_H/2), mat_wall_plaster, col_arch)

# ==============================================================================
# 2. TRUE ARCH-SHAPED DOORS & ARCH-SHAPED GLASS WINDOWS WITH CURVED FANLIGHTS
# ==============================================================================
add_arched_door_assembly("Door_Main_ArchPortal", 1.36, 3.05, 0.32, (2.60, -5.00, 0.0), 0.0, col_openings, has_mashrabiya_fanlight=True, pointed=0.16)
add_arched_door_assembly("Door_Bath_ArchPortal", 1.06, 2.55, 0.24, (-2.10, -1.85, 0.0), math.pi/2, col_openings, has_mashrabiya_fanlight=False, pointed=0.14)
add_arched_window_assembly("Window_West_Arch", 1.40, 2.05, 0.30, (-6.00, 0.0, 0.85), math.pi/2, col_openings, pointed=0.14)
add_arched_window_assembly("Window_South_Arch", 1.32, 2.05, 0.30, (4.70, -5.00, 0.85), 0.0, col_openings, pointed=0.14)

# ==============================================================================
# 3. LUXURY FRENCH-DOOR SMART REFRIGERATOR & CHEF'S KITCHEN WITH COOKING ACCESSORIES
# ==============================================================================
add_ao_decal("AO_KingBed", 3.10, 2.60, -4.55, 2.50, 0.0, col_bedroom)
add_box("Bed_Kairouan_Rug", (3.40, 3.10, 0.016), (-4.20, 2.50, 0.010), mat_rug, col_bedroom, bevel=0.004, uv_mode='FIT_TOP')
add_ao_decal("AO_Middle_Daybed", 1.15, 2.85, 0.55, 1.95, 0.0, col_bedroom)

add_ao_decal("AO_TV_Console", 2.60, 0.75, 3.60, 4.50, 0.0, col_living)
add_box("TV_OLED_85_Frame", (1.95, 0.05, 1.12), (3.60, 4.76, 1.65), mat_charcoal, col_living)
add_box("TV_OLED_85_Screen", (1.86, 0.06, 1.04), (3.60, 4.75, 1.65), mat_tv_screen, col_living)

add_box("Living_Kairouan_Grand_Rug", (3.95, 4.20, 0.016), (3.25, 1.65, 0.010), mat_rug, col_living, bevel=0.004, uv_mode='FIT_TOP')
add_ao_decal("AO_Majlis_South", 3.10, 1.15, 3.25, 0.08, 0.015, col_living)
add_ao_decal("AO_Majlis_East", 1.15, 2.80, 4.72, 1.85, 0.015, col_living)
add_ao_decal("AO_Majlis_CoffeeTable", 1.65, 1.15, 3.25, 1.75, 0.015, col_living)

# --- DETAILED FRENCH-DOOR SMART REFRIGERATOR (X = -1.55, Y = -4.50) ---
add_ao_decal("AO_Kitchen_South", 3.10, 1.05, -0.65, -4.50, 0.0, col_kitchen)
add_ao_decal("AO_Kitchen_Vert", 1.05, 3.00, 0.90, -3.50, 0.0, col_kitchen)

# Outer Walnut & Brass Built-In Fridge Enclosure
add_box("Fridge_Cabinet_Housing", (0.98, 0.78, 2.15), (-1.55, -4.52, 1.075), mat_cedar_wood, col_kitchen)
add_box("Fridge_Body_Carcass", (0.90, 0.70, 1.98), (-1.55, -4.50, 1.00), mat_dark_steel, col_kitchen)
# Upper Left & Right French Doors (Z = 0.78 .. 1.96)
add_box("Fridge_FrenchDoor_Left", (0.435, 0.06, 1.16), (-1.775, -4.13, 1.37), mat_chrome, col_kitchen, bevel=0.01)
add_box("Fridge_FrenchDoor_Right", (0.435, 0.06, 1.16), (-1.325, -4.13, 1.37), mat_chrome, col_kitchen, bevel=0.01)
# Bottom Freezer Pull-Out Drawers (Z = 0.06 .. 0.75)
add_box("Fridge_FreezerDrawer_Top", (0.89, 0.06, 0.33), (-1.55, -4.13, 0.58), mat_chrome, col_kitchen, bevel=0.01)
add_box("Fridge_FreezerDrawer_Bot", (0.89, 0.06, 0.34), (-1.55, -4.13, 0.22), mat_chrome, col_kitchen, bevel=0.01)
# Brushed Brass Tubular Handles (2 vertical + 2 horizontal)
for hx in (-1.59, -1.51):
    add_cyl(f"Fridge_Handle_V_{hx}", 0.014, 0.78, (hx, -4.07, 1.38), mat_brass_gold, col_kitchen)
for hz in (0.62, 0.26):
    add_cyl(f"Fridge_Handle_H_{hz}", 0.014, 0.68, (-1.55, -4.07, hz), mat_brass_gold, col_kitchen, rot=(0, math.pi/2, 0))
# Ice & Water Dispenser Niche + Glowing Smart Screen on Left Door
add_box("Fridge_Dispenser_Niche", (0.20, 0.04, 0.28), (-1.78, -4.10, 1.32), mat_charcoal, col_kitchen)
add_box("Fridge_Smart_TouchScreen", (0.16, 0.01, 0.22), (-1.32, -4.095, 1.45), mat_fridge_led, col_kitchen, bevel=0.002)

# --- TEXTURED L-SHAPED CHEF'S KITCHEN CABINETRY, COUNTERTOP & COOKING ACCESSORIES ---
add_box("Kitchen_Base_South", (1.72, 0.68, 0.86), (-0.20, -4.54, 0.43), mat_cedar_wood, col_kitchen)
add_box("Kitchen_Counter_South", (1.78, 0.74, 0.05), (-0.20, -4.54, 0.885), mat_floor_marble, col_kitchen)
add_box("Kitchen_Base_Vertical", (0.68, 2.05, 0.86), (0.94, -3.85, 0.43), mat_cedar_wood, col_kitchen)
add_box("Kitchen_Counter_Vertical", (0.74, 2.10, 0.05), (0.94, -3.85, 0.885), mat_floor_marble, col_kitchen)
# Shaker Cabinet Doors & Brushed Brass Handles along South & Vertical Counters
for dx in (-0.82, -0.40, 0.02, 0.44):
    add_box(f"Kitchen_Door_S_{dx}", (0.38, 0.03, 0.72), (dx, -4.19, 0.45), mat_stucco_relief, col_kitchen, bevel=0.008)
    add_cyl(f"Kitchen_Knob_S_{dx}", 0.012, 0.18, (dx, -4.16, 0.72), mat_brass_gold, col_kitchen, rot=(0, math.pi/2, 0))
for dy in (-4.45, -4.00, -3.55, -3.10):
    add_box(f"Kitchen_Door_V_{dy}", (0.03, 0.40, 0.72), (0.59, dy, 0.45), mat_stucco_relief, col_kitchen, bevel=0.008)
    add_cyl(f"Kitchen_Knob_V_{dy}", 0.012, 0.18, (0.56, dy, 0.72), mat_brass_gold, col_kitchen, rot=(math.pi/2, 0, 0))

# Toe-Kick LED Strips under Kitchen Counters
add_box("Kitchen_ToeKick_LED_S", (1.68, 0.02, 0.02), (-0.20, -4.22, 0.04), mat_led_border, col_lighting, bevel=0.0)
add_box("Kitchen_ToeKick_LED_V", (0.02, 2.00, 0.02), (0.62, -3.85, 0.04), mat_led_border, col_lighting, bevel=0.0)

# Carved Mashrabiya & Zellige Backsplash + Upper Lit Cabinets
add_box("Kitchen_Zellige_Backsplash_S", (1.72, 0.03, 0.62), (-0.20, -4.86, 1.22), mat_mashrabiya, col_kitchen, uv_scale=1.1)
add_box("Kitchen_Zellige_Backsplash_V", (0.03, 2.70, 0.62), (1.27, -3.50, 1.22), mat_mashrabiya, col_kitchen, uv_scale=1.1)
add_box("Kitchen_Upper_Cabinet_S", (1.68, 0.38, 0.82), (-0.20, -4.68, 2.15), mat_cedar_wood, col_kitchen)
for ux in (-0.75, -0.20, 0.35):
    add_box(f"Kitchen_UpperGlassDoor_{ux}", (0.50, 0.03, 0.74), (ux, -4.48, 2.15), mat_stucco_relief, col_kitchen, bevel=0.008)
add_box("Kitchen_UnderCabinet_LED", (1.64, 0.03, 0.025), (-0.20, -4.55, 1.72), mat_led_border, col_lighting, bevel=0.0)
add_box("Kitchen_Range_Hood_Brass", (0.72, 0.56, 0.78), (0.94, -2.50, 2.25), mat_brass_gold, col_kitchen)
add_box("Kitchen_Range_Hood_Chimney", (0.34, 0.32, 0.85), (0.94, -2.50, 3.05), mat_dark_steel, col_kitchen)

# Double-Basin Sink & High-Arc Gooseneck Brass Faucet
add_box("Kitchen_Sink_Basin_1", (0.42, 0.36, 0.04), (0.94, -3.75, 0.90), mat_dark_steel, col_kitchen)
add_box("Kitchen_Sink_Basin_2", (0.42, 0.36, 0.04), (0.94, -4.15, 0.90), mat_dark_steel, col_kitchen)
add_cyl("Kitchen_Faucet_Stem", 0.022, 0.34, (1.16, -3.95, 1.07), mat_brass_gold, col_kitchen)
add_cyl("Kitchen_Faucet_Spout", 0.018, 0.22, (1.06, -3.95, 1.22), mat_brass_gold, col_kitchen, rot=(0, math.pi/2, 0))

# --- COOKING ACCESSORIES: ESPRESSO MACHINE, CUTTING BOARD, KNIFE BLOCK, SPICE JARS, SKILLET ---
# Luxury Espresso / Arabic Coffee Machine at (-0.75, -4.52, 0.91)
add_box("Kitchen_Espresso_Body", (0.32, 0.34, 0.36), (-0.75, -4.52, 1.09), mat_charcoal, col_kitchen, bevel=0.02)
add_box("Kitchen_Espresso_BrassTrim", (0.33, 0.35, 0.05), (-0.75, -4.52, 1.25), mat_brass_gold, col_kitchen)
add_cyl("Kitchen_Espresso_GroupHead", 0.045, 0.08, (-0.75, -4.32, 1.12), mat_brass_gold, col_kitchen)
for cup_x in (-0.81, -0.69):
    add_cyl(f"Kitchen_CoffeeCup_{cup_x}", 0.032, 0.065, (cup_x, -4.32, 0.95), mat_porcelain, col_kitchen)

# Walnut Cutting Board + Knife Block + Spice Rack at (-0.15, -4.50, 0.91)
add_box("Kitchen_Cutting_Board", (0.42, 0.30, 0.025), (-0.15, -4.45, 0.92), mat_cedar_wood, col_kitchen, bevel=0.008)
add_box("Kitchen_Knife_Block", (0.14, 0.18, 0.22), (0.22, -4.62, 1.01), mat_cedar_wood, col_kitchen, rot=(0.25, 0, 0.2))
for sj_idx, sj_x in enumerate((-0.38, -0.28, -0.18, -0.08, 0.02)):
    add_cyl(f"Kitchen_SpiceJar_{sj_idx}", 0.032, 0.11, (sj_x, -4.74, 0.96), mat_terracotta if sj_idx%2==0 else mat_brass_gold, col_kitchen)

# Copper Frying Pan / Skillet on Stove Burner (at X = 0.85, Y = -2.35, Z = 0.93)
add_cyl("Kitchen_Copper_Skillet", 0.14, 0.05, (0.85, -2.35, 0.94), mat_copper, col_kitchen)
add_cyl("Kitchen_Skillet_Handle", 0.012, 0.22, (0.68, -2.35, 0.96), mat_brass_gold, col_kitchen, rot=(0, math.pi/2, 0))

# Bathroom Shower & Toilet Fixtures
add_box("Shower_Tray_Marble", (1.68, 1.72, 0.08), (-5.00, -4.00, 0.04), mat_floor_marble, col_bathroom)
add_box("Shower_Glass_Partition", (0.04, 1.65, 2.25), (-4.18, -4.00, 1.15), mat_glass, col_bathroom)
add_modern_arabic_arch("Shower_Hammam_Arch", 1.62, 2.40, 0.10, (-4.18, -4.00, 0.0), math.pi/2, mat_brass_gold, col_bathroom, has_led=True, pointed=0.12)
add_cyl("Shower_Brass_Pipe", 0.022, 2.10, (-5.75, -4.00, 1.15), mat_brass_gold, col_bathroom)
add_cyl("Shower_Rain_Disc", 0.19, 0.03, (-5.45, -4.00, 2.18), mat_brass_gold, col_bathroom)
add_box("Toilet_Tank", (0.24, 0.44, 0.82), (-5.68, -1.85, 0.41), mat_porcelain, col_bathroom, bevel=0.03)
add_cyl("Toilet_Bowl", 0.23, 0.44, (-5.35, -1.85, 0.22), mat_porcelain, col_bathroom, verts=24)
add_cyl("Toilet_Lid_GoldTrim", 0.235, 0.04, (-5.35, -1.85, 0.45), mat_porcelain, col_bathroom, verts=24)
add_box("Bath_Vanity_Cabinet", (1.35, 0.56, 0.82), (-3.15, -4.56, 0.41), mat_cedar_wood, col_bathroom)
add_box("Bath_Vanity_MarbleTop", (1.40, 0.60, 0.05), (-3.15, -4.56, 0.84), mat_floor_marble, col_bathroom)
add_cyl("Bath_Brass_Vessel_Sink", 0.22, 0.16, (-3.15, -4.56, 0.94), mat_brass_gold, col_bathroom, verts=28)

# ==============================================================================
# 4. ROOFTOP MODERN ARABIC PARAPET, MASHRABIYA SCREENS, LOUVERS & LOUNGE
# ==============================================================================
add_box("Roof_Flat_Slab", (12.30, 10.30, 0.24), (0.0, 0.0, 3.62), mat_wall_exterior, col_rooftop)
add_box("Roof_Terrace_Floor_Tile", (11.70, 9.70, 0.03), (0.0, 0.0, 3.755), mat_floor_courtyard, col_rooftop, uv_scale=0.45)

add_box("Roof_Parapet_North", (12.30, 0.22, 1.05), (0.0, 5.04, 4.26), mat_wall_exterior, col_rooftop)
add_box("Roof_Parapet_South", (12.30, 0.22, 1.05), (0.0, -5.04, 4.26), mat_wall_exterior, col_rooftop)
add_box("Roof_Parapet_West", (0.22, 10.30, 1.05), (-6.04, 0.0, 4.26), mat_wall_exterior, col_rooftop)
add_box("Roof_Parapet_East", (0.22, 10.30, 1.05), (6.04, 0.0, 4.26), mat_wall_exterior, col_rooftop)

add_box("Roof_Mashrabiya_Frieze_South", (12.34, 0.04, 0.48), (0.0, -5.16, 4.35), mat_mashrabiya, col_rooftop, uv_scale=0.9)
add_box("Roof_Mashrabiya_Frieze_East", (0.04, 10.34, 0.48), (6.16, 0.0, 4.35), mat_mashrabiya, col_rooftop, uv_scale=0.9)
add_box("Roof_Coping_North", (12.42, 0.30, 0.08), (0.0, 5.04, 4.82), mat_stucco_relief, col_rooftop)
add_box("Roof_Coping_South", (12.42, 0.30, 0.08), (0.0, -5.04, 4.82), mat_stucco_relief, col_rooftop)
add_box("Roof_Coping_West", (0.30, 10.42, 0.08), (-6.04, 0.0, 4.82), mat_stucco_relief, col_rooftop)
add_box("Roof_Coping_East", (0.30, 10.42, 0.08), (6.04, 0.0, 4.82), mat_stucco_relief, col_rooftop)
add_box("Roof_Cornice_LED_South", (12.20, 0.04, 0.03), (0.0, -5.17, 4.76), mat_led_border, col_rooftop, bevel=0.0)
add_box("Roof_Cornice_LED_East", (0.04, 10.20, 0.03), (6.17, 0.0, 4.76), mat_led_border, col_rooftop, bevel=0.0)

for lx_idx in range(11):
    lx = -5.20 + lx_idx * 0.42
    add_box(f"Facade_Cantilever_Louver_L_{lx_idx}", (0.10, 0.55, 0.14), (lx, -5.32, 3.65), mat_cedar_wood, col_rooftop)
for rx_idx in range(9):
    rx = 1.85 + rx_idx * 0.44
    add_box(f"Facade_Cantilever_Louver_R_{rx_idx}", (0.10, 0.55, 0.14), (rx, -5.32, 3.65), mat_cedar_wood, col_rooftop)

for px in (0.6, 5.1):
    for py in (-1.2, 4.0):
        add_cyl(f"Roof_Pergola_Post_{px}_{py}", 0.095, 2.55, (px, py, 5.02), mat_cedar_wood, col_rooftop)
for beam_y in (-1.2, 0.1, 1.4, 2.7, 4.0):
    add_box(f"Roof_Pergola_Beam_{beam_y}", (4.80, 0.12, 0.16), (2.85, beam_y, 6.28), mat_cedar_wood, col_rooftop)
for slat_x in range(8):
    sx = 0.85 + slat_x * 0.56
    add_box(f"Roof_Pergola_Slat_{slat_x}", (0.08, 5.50, 0.06), (sx, 1.40, 6.38), mat_cedar_wood, col_rooftop)

add_box("Roof_Rug_Kilim", (4.10, 4.40, 0.02), (2.85, 1.40, 3.78), mat_rug, col_rooftop, uv_mode='FIT_TOP')
add_box("Roof_Grill_Counter_Zellige", (1.10, 3.40, 0.92), (-4.65, 2.20, 4.22), mat_mashrabiya, col_rooftop, uv_scale=0.9)
add_box("Roof_Grill_Marble_Top", (1.16, 3.48, 0.06), (-4.65, 2.20, 4.71), mat_floor_marble, col_rooftop)
add_box("Roof_BBQ_Brass_Hood", (0.92, 1.30, 0.65), (-4.65, 2.65, 5.85), mat_brass_gold, col_rooftop)

# ==============================================================================
# 5. PLACE ALL REAL POLY HAVEN 3D MODELS (FURNITURE, LAMPS, KITCHEN COOKWARE, PLANTS)
# ==============================================================================
def place_ph_model(asset_id, name, target_loc, target_span_xy=None, target_height=None, rot_z=0.0, col=col_living):
    gltf_file = os.path.join(PH_MODELS, asset_id, f"{asset_id}.gltf")
    if not os.path.exists(gltf_file):
        return None
    before_names = set(o.name for o in bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=gltf_file)
    new_names = [o.name for o in bpy.data.objects if o.name not in before_names]
    for n in new_names:
        if n in bpy.data.objects and bpy.data.objects[n].animation_data:
            bpy.data.objects[n].animation_data_clear()
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
    if obj.animation_data:
        obj.animation_data_clear()
    obj.name = name

    for n in new_names:
        if n in bpy.data.objects and bpy.data.objects[n] != obj:
            bpy.data.objects.remove(bpy.data.objects[n], do_unlink=True)

    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
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
    link_obj(obj, col)
    return obj

# King Bed Zone
place_ph_model("GothicBed_01", "PH_KingBed_Main", (-4.55, 2.50, 0.02), target_span_xy=(2.35, 2.02, 1.62), rot_z=math.pi/2, col=col_bedroom)
for ny in (1.12, 3.88):
    place_ph_model("ClassicNightstand_01", f"PH_Nightstand_{ny}", (-5.50, ny, 0.02), target_height=0.66, rot_z=math.pi/2, col=col_bedroom)
    place_ph_model("brass_diya_lantern", f"PH_Bed_Lantern_{ny}", (-5.50, ny, 0.68), target_height=0.35, rot_z=0.0, col=col_bedroom)

# Middle Daybed Zone (Aligned with Center Arch at X = +0.55m)
place_ph_model("vintage_day_bed", "PH_Middle_Daybed", (0.55, 1.95, 0.02), target_span_xy=(0.86, 2.40, 0.86), rot_z=math.pi/2, col=col_bedroom)
place_ph_model("coffee_table_round_01", "PH_Middle_TeaTable", (0.55, 0.15, 0.02), target_height=0.50, rot_z=0.0, col=col_bedroom)
place_ph_model("brass_vase_01", "PH_Middle_BrassVase", (0.55, 0.15, 0.52), target_height=0.32, rot_z=0.0, col=col_bedroom)

# Living Majlis & TV Zone (Centered at X = +3.60m inside the Right North Arch!)
place_ph_model("modern_wooden_cabinet", "PH_TV_Media_Cabinet", (3.60, 4.50, 0.02), target_span_xy=(2.10, 0.48, 0.62), rot_z=0.0, col=col_living)
place_ph_model("Sofa_01", "PH_Majlis_Sofa_South", (3.40, 0.08, 0.02), target_span_xy=(2.65, 0.98, 0.92), rot_z=0.0, col=col_living)
place_ph_model("Sofa_01", "PH_Majlis_Sofa_East", (4.88, 1.85, 0.02), target_span_xy=(0.98, 2.55, 0.92), rot_z=math.pi/2, col=col_living)
place_ph_model("ArmChair_01", "PH_Majlis_Armchair_West", (1.92, 2.35, 0.02), target_height=0.88, rot_z=-math.pi/2.2, col=col_living)
place_ph_model("Ottoman_01", "PH_Majlis_Ottoman_1", (1.98, 1.20, 0.02), target_height=0.42, rot_z=0.4, col=col_living)
place_ph_model("CoffeeTable_01", "PH_Majlis_CoffeeTable", (3.40, 1.75, 0.02), target_span_xy=(1.45, 0.92, 0.48), rot_z=0.0, col=col_living)
place_ph_model("brass_pot_01", "PH_Majlis_BrassPot", (3.20, 1.75, 0.50), target_height=0.26, rot_z=0.0, col=col_living)
place_ph_model("ceramic_vase_01", "PH_Majlis_CeramicVase", (3.60, 1.75, 0.50), target_height=0.28, rot_z=0.0, col=col_living)
place_ph_model("throw_pillows_01", "PH_Majlis_Pillows_S", (3.40, 0.02, 0.48), target_height=0.38, rot_z=0.0, col=col_living)
place_ph_model("potted_plant_02", "PH_Living_Plant_NE", (5.32, 4.20, 0.02), target_height=1.35, rot_z=0.5, col=col_living)
place_ph_model("potted_plant_01", "PH_Living_Plant_SW", (1.65, -0.65, 0.02), target_height=1.15, rot_z=-0.4, col=col_living)

# Kitchen Stove, Pots, Vases & Bathroom Ornate Mirror
place_ph_model("electric_stove", "PH_Kitchen_Stove", (0.92, -2.50, 0.02), target_span_xy=(0.68, 0.72, 0.90), rot_z=-math.pi/2, col=col_kitchen)
place_ph_model("brass_pot_01", "PH_Kitchen_CookingPot", (0.98, -2.65, 0.92), target_height=0.22, rot_z=0.4, col=col_kitchen)
place_ph_model("ceramic_vase_01", "PH_Kitchen_CounterJar", (0.42, -4.55, 0.91), target_height=0.26, rot_z=0.2, col=col_kitchen)
place_ph_model("brass_vase_01", "PH_Kitchen_OilPitcher", (0.94, -3.35, 0.91), target_height=0.25, rot_z=0.0, col=col_kitchen)
place_ph_model("ornate_mirror_01", "PH_Bath_Ornate_Mirror", (-3.15, -4.82, 1.02), target_height=1.25, rot_z=0.0, col=col_bathroom)

# Chandeliers & Wall Lanterns
place_ph_model("Chandelier_03", "PH_Chandelier_Living", (3.40, 1.75, 2.38), target_height=1.08, rot_z=0.0, col=col_lighting)
place_ph_model("Chandelier_01", "PH_Chandelier_Bedroom", (-4.10, 2.50, 2.42), target_height=1.02, rot_z=0.0, col=col_lighting)
place_ph_model("lantern_chandelier_01", "PH_Chandelier_Middle", (0.55, 1.85, 2.52), target_height=0.92, rot_z=0.0, col=col_lighting)
place_ph_model("chinese_chandelier", "PH_Chandelier_Kitchen", (-0.25, -3.50, 2.55), target_height=0.88, rot_z=0.0, col=col_lighting)
place_ph_model("Chandelier_02", "PH_Chandelier_Bathroom", (-3.85, -2.85, 2.58), target_height=0.85, rot_z=0.0, col=col_lighting)

lantern_positions = [
    (-0.98, 4.78, 2.05, 0.0),
    (2.07, 4.78, 2.05, 0.0),
    (5.78, 1.85, 2.05, -math.pi/2),
    (-5.78, 2.50, 2.05, math.pi/2),
    (1.82, -5.18, 2.05, math.pi),
    (3.38, -5.18, 2.05, math.pi),
    (5.52, -5.18, 2.05, math.pi),
]
for idx, spos in enumerate(lantern_positions):
    place_ph_model("Lantern_01", f"PH_Wall_Lantern_{idx}", (spos[0], spos[1], spos[2]), target_height=0.44, rot_z=spos[3], col=col_lighting)

# Rooftop Lounge Furniture
place_ph_model("sofa_03", "PH_Roof_Sofa_North", (2.85, 3.35, 3.78), target_span_xy=(3.20, 0.95, 0.85), rot_z=math.pi, col=col_rooftop)
place_ph_model("sofa_03", "PH_Roof_Sofa_East", (4.35, 1.40, 3.78), target_span_xy=(0.95, 3.20, 0.85), rot_z=math.pi/2, col=col_rooftop)
place_ph_model("sofa_02", "PH_Roof_Sofa_South", (2.85, -0.55, 3.78), target_span_xy=(2.80, 0.92, 0.85), rot_z=0.0, col=col_rooftop)
place_ph_model("modern_coffee_table_01", "PH_Roof_Family_Table", (2.65, 1.40, 3.78), target_span_xy=(1.85, 1.10, 0.52), rot_z=0.0, col=col_rooftop)
place_ph_model("stone_fire_pit", "PH_Roof_BBQ_Grill", (-4.65, 2.65, 4.72), target_span_xy=(0.88, 1.15, 0.55), rot_z=0.0, col=col_rooftop)
for stool_y in (0.95, 1.95, 2.95):
    place_ph_model("bar_chair_round_01", f"PH_Roof_BarStool_{stool_y}", (-3.65, stool_y, 3.78), target_height=0.76, rot_z=0.0, col=col_rooftop)

for tidx, (asset, tpos, th) in enumerate([
    ("potted_plant_02", (1.82, -5.55, 0.02), 1.45),
    ("potted_plant_04", (3.38, -5.55, 0.02), 1.35),
    ("potted_plant_02", (5.45, -8.55, 0.02), 1.75),
    ("potted_plant_01", (1.80, -8.55, 0.02), 1.35),
    ("potted_plant_02", (-4.80, -3.50, 3.76), 1.60),
    ("potted_plant_04", (5.00, -3.80, 3.76), 1.55),
]):
    place_ph_model(asset, f"PH_Villa_Plant_{tidx}", tpos, target_height=th, rot_z=tidx*0.9, col=col_rooftop)

# ==============================================================================
# 6. CEILING LIGHTS, EXTERIOR PORTAL LIGHTS & WALL SWITCHES
# ==============================================================================
ceiling_lamp_zones = [
    ("Lamp_Ceiling_LivingMajlis", (3.40, 1.75, 3.08), 165.0),
    ("Lamp_Ceiling_Bedroom", (-4.10, 2.50, 3.08), 150.0),
    ("Lamp_Ceiling_MiddleZone", (0.55, 1.85, 3.08), 135.0),
    ("Lamp_Ceiling_Kitchen", (-0.25, -3.50, 3.08), 145.0),
    ("Lamp_Ceiling_Bathroom", (-3.85, -2.85, 3.08), 120.0),
    ("Lamp_Exterior_EntrancePortal", (2.60, -5.45, 2.85), 140.0),
    ("Lamp_Exterior_Courtyard", (3.70, -7.10, 2.60), 110.0),
]
for lname, lpos, lenergy in ceiling_lamp_zones:
    ldata = bpy.data.lights.new(name=f"{lname}_Light", type='POINT')
    ldata.energy = lenergy
    ldata.color = (1.0, 0.86, 0.64)
    ldata.shadow_soft_size = 0.30
    lobj = bpy.data.objects.new(name=f"{lname}_LightObj", object_data=ldata)
    lobj.location = (lpos[0], lpos[1], lpos[2] - 0.15)
    col_lighting.objects.link(lobj)

wall_switches = [
    ("Living_North_Switch", (2.07, 4.82, 1.35)),
    ("Living_East_Switch", (5.82, 0.55, 1.35)),
    ("Bedroom_West_Switch", (-5.82, 1.05, 1.35)),
    ("Kitchen_Wall_Switch", (1.26, -2.15, 1.35)),
    ("Bathroom_Wall_Switch", (-1.98, -2.55, 1.35)),
    ("Entrance_MainDoor_Switch", (1.80, -4.82, 1.35)),
]
for sname, sw_pos in wall_switches:
    add_box(f"SwitchPlate_{sname}", (0.11, 0.11, 0.15), sw_pos, mat_brass_gold, col_lighting)
    add_box(f"SwitchLED_{sname}", (0.04, 0.04, 0.04), (sw_pos[0], sw_pos[1], sw_pos[2]+0.03), mat_switch_on, col_lighting)

# ==============================================================================
# 7. WORLD LIGHTING & HIGH-CONTRAST REALISTIC RENDERING SETUP
# ==============================================================================
world = bpy.data.worlds.new("Tunisia_Mediterranean_World")
scene.world = world
world.use_nodes = True
bg = world.node_tree.nodes.get("Background")
bg.inputs["Color"].default_value = (0.64, 0.76, 0.92, 1.0)
bg.inputs["Strength"].default_value = 0.58

sun_data = bpy.data.lights.new("Tunisia_Sun", type='SUN')
sun_data.energy = 4.2
sun_data.color = (1.0, 0.93, 0.80)
sun_data.angle = math.radians(1.5)
sun_obj = bpy.data.objects.new("Tunisia_Sun", object_data=sun_data)
sun_obj.rotation_euler = (math.radians(48), math.radians(-26), math.radians(32))
col_lighting.objects.link(sun_obj)

for fill_idx, fpos in enumerate([(-3.0, 1.5, 3.25), (3.0, 1.5, 3.25), (-0.5, -3.2, 3.25), (-4.0, -3.1, 3.25)]):
    adata = bpy.data.lights.new(f"Fill_Area_{fill_idx}", type='AREA')
    adata.energy = 65.0
    adata.color = (1.0, 0.95, 0.86)
    adata.size = 3.2
    adata.use_shadow = False
    aobj = bpy.data.objects.new(f"Fill_Area_{fill_idx}", object_data=adata)
    aobj.location = fpos
    col_lighting.objects.link(aobj)

scene.render.engine = 'BLENDER_EEVEE'
scene.view_settings.view_transform = 'AgX'
scene.view_settings.look = 'AgX - Medium High Contrast'
scene.view_settings.exposure = 0.12
scene.render.resolution_x = 1600
scene.render.resolution_y = 1000

blend_path = os.path.join(OUT_DIR, "tunisia_arab_villa.blend")
glb_path = os.path.join(OUT_DIR, "tunisia_arab_villa.glb")
bpy.ops.wm.save_as_mainfile(filepath=blend_path)
bpy.ops.export_scene.gltf(filepath=glb_path, export_format='GLB')

cam_data = bpy.data.cameras.new("RenderCam")
cam_data.lens = 24
cam_obj = bpy.data.objects.new("RenderCam", cam_data)
scene.collection.objects.link(cam_obj)
scene.camera = cam_obj

def look_at(obj, target):
    direction = Vector(target) - obj.location
    rot_quat = direction.to_track_quat('-Z', 'Y')
    obj.rotation_euler = rot_quat.to_euler()

# Render 1: Hero Modern Arabic Villa Exterior Facade, Arch-Cut Windows/Doors & Rooftop Lounge
col_rooftop.hide_render = False
cam_obj.data.lens = 22
cam_obj.location = (8.8, -14.8, 5.8)
look_at(cam_obj, (0.5, -2.2, 2.1))
scene.render.filepath = os.path.join(OUT_DIR, "render_rooftop_and_exterior.png")
bpy.ops.render.render(write_still=True)

# Render 2: Interior Cutaway Floorplan View (showing Detailed Chef's Kitchen, French-Door Fridge, Arch Windows & All Rooms)
col_rooftop.hide_render = True
cam_obj.data.lens = 24
cam_obj.location = (0.3, -12.2, 12.2)
look_at(cam_obj, (0.0, -0.3, 0.6))
scene.render.filepath = os.path.join(OUT_DIR, "render_interior_floorplan_cutaway.png")
bpy.ops.render.render(write_still=True)

# Render 3: Interior Eye-Level View showing Equidistant North Wall Arches (X=-2.5, +0.55, +3.60), TV + Cabinet Centered in Right Arch
cam_obj.location = (0.2, -1.10, 1.80)
cam_data.lens = 16
look_at(cam_obj, (0.2, 2.8, 1.30))
scene.render.filepath = os.path.join(OUT_DIR, "render_interior_majlis_and_bedroom.png")
bpy.ops.render.render(write_still=True)

col_rooftop.hide_render = False
bpy.ops.wm.save_as_mainfile(filepath=blend_path)
print("SUCCESS: Built Modern Arabic Villa with true arch-cut windows/doors & detailed Chef's Kitchen!")
