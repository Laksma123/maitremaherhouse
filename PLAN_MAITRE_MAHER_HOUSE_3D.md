# MAÎTRE MAHER — MODERN ARABIC & TUNISIA VILLA 3D SIMULATOR
## Master Brain, Architecture Specification & Strict Quality Standards
**Repository:** `https://github.com/Laksma123/maitremaherhouse`  
**Local Workspace Path:** `/Users/dianjulie/Documents/maitremaherhouse`  
**Primary Application Files:** `Tunisia_Arab_House_Designer.html` & `index.html` (must always be kept identical)

---

> [!IMPORTANT]
> ## MANDATORY VISUAL QUALITY & ANTI-CARTOON RULE (READ BEFORE ANY EDIT)
> 1. **STRICTLY AAA REALISTIC 3D QUALITY — NEVER CARTOON:**
>    The user strictly requires **realistic, high-contrast, physically-based 3D visuals** (real Poly Haven GLTF 3D furniture models, 1K PBR diffuse/normal/roughness maps, HDRI environment reflections, ACES Filmic / AgX tone-mapped contrast, and soft contact-shadow AO decals). **NEVER** replace Poly Haven GLTF models with basic geometric primitives/cartoon boxes, and **NEVER** flatten lighting or remove PBR textures.
> 2. **CURRENT VISUAL QUALITY IS THE LOCKED BASELINE — DO NOT DOWNGRADE:**
>    What is currently built and verified in `Tunisia_Arab_House_Designer.html` is the minimum acceptable visual baseline. When optimizing FPS or adding new features, **you must NEVER reduce texture resolution, remove PBR normal/roughness maps, disable shadows, or degrade material realism**.
> 3. **ALWAYS VERIFY IN A REAL BROWSER BEFORE REPORTING:**
>    Never rely solely on `node --check` (which only checks syntax, not runtime execution or WebGL rendering). Always verify changes in a real browser render.

---

## 1. Project Context & Purpose
* **Target User:** Built as an interactive, luxury 3D architectural & interior simulator for the user's boss (**Maître Maher**) showcasing his **Modern Arabic & Tunisian Villa** (*Sidi Bou Said / Carthage / Hammamet luxury aesthetic*).
* **Bilingual Support:** 100% English (`en`) ↔ 100% Tunisian Arabic (`ar`, `العربية التونسية`) instant language toggle (`toggleLanguage()`).
* **Core Capabilities:**
  * **4 Camera & Navigation Modes:**
    1. `3D Orbit View`: Free 360° orbit camera with 6 quick room presets (`Facade`, `Salon & TV`, `Bedroom`, `Kitchen`, `Bathroom`, `Rooftop`).
    2. `Top View: 1st Floor`: Orthographic/high-angle floorplan view with automatic roof cutaway (`setRoofVisible(false)`).
    3. `Top View: 2nd Floor (Roof)`: Top view focusing on the rooftop terrace lounge, pergola, and BBQ bar.
    4. `Walk Mode (WASD + Virtual Analog Joystick)`: First-person walkthrough (`eyeHeight = 1.68m`) with smooth wall-segment capsule collision, automatic proximity door swing, and interactive window open/close (`F` key or click).
  * **3 Realistic Time-of-Day Atmospheres (`setTimeOfDay`):**
    * `Sunset`: Golden-hour directional sunlight + per-pixel GLSL sunset sky dome + `venice_sunset_1k.hdr` PBR environment reflections.
    * `Day`: Bright Mediterranean noon sunlight + azure GLSL sky dome + `kloppenheim_06_puresky_1k.hdr` PBR environment reflections.
    * `Night (Full LED)`: Starry Sahara/Sidi Bou Said night sky dome + `moonless_golf_1k.hdr` + glowing 2700K architectural LED arch/window borders, chandeliers, and courtyard pathway lights.
  * **Cycles-Style 24-Sample Photoshoot Renderer (`startPhotoshootRender`):**
    * Progressive jittered sub-pixel anti-aliasing + soft area-light shadow accumulation + GI bounce fill lights, downloadable as high-res PNG inside `<dialog id="photoshoot-dialog" closedby="any">`.

---

## 2. Spatial Coordinate Convention & Villa Layout (`12.0m × 10.0m` Main Footprint)
The code uses helper `bPos(bx, by, bz)` which maps Floorplan coordinates `(bx, by, bz)` to Three.js world coordinates `(x = bx, y = bz, z = -by)`:
* **Main Villa Interior (`bx = -6.00m .. +6.00m`, `by = -5.00m .. +5.00m`, wall height `H = 3.50m`):**
  * **King Master Bedroom (North-West):** `bx = -6.00m .. -2.00m`, `by = -1.10m .. +5.00m`. Contains `GothicBed_01`, 2× `ClassicNightstand_01`, 2× `brass_diya_lantern`, `Chandelier_01`/`02`/`03`, Berber rug, and West Arched Window (`bx = -6.00, by = 0.00`).
  * **Hammam Luxury Bathroom (South-West):** `bx = -6.00m .. -2.10m`, `by = -5.00m .. -1.10m`. Features blue-gold Zellige floor tiles (`matBathFloor`), glass walk-in shower with brass rain head, porcelain toilet, walnut vanity with brass vessel sink, `ornate_mirror_01`, and East Arched Bathroom Door (`bx = -2.10, by = -2.85`).
  * **Center Lounge / Daybed Area (Mid-North):** `bx = -1.50m .. +1.50m`, `by = -1.00m .. +4.50m`. Contains `vintage_day_bed`, round marble tea table (`coffee_table_round_01`), and `brass_vase_01`.
  * **Chef's L-Shaped Kitchen (Mid-South):** `bx = -2.00m .. +1.40m`, `by = -5.00m .. -1.60m`. Contains French-door smart refrigerator (`fridgeGroup`), walnut & Emperador marble L-counter (`kGroup`), `electric_stove`, `brass_pot_01`, `ceramic_vase_01`, `brass_vase_01`, espresso machine, and `bar_chair_round_01`.
  * **Grand Majlis Living Salon & TV Wall (East):** `bx = +1.50m .. +6.00m`, `by = -1.00m .. +5.00m`. Contains South & East Majlis Sofas (`Sofa_01`/`sofa_02`/`sofa_03`), `ArmChair_01`, `CoffeeTable_01`, `Ottoman_01`, TV console + wall-mounted flatscreen TV (`tvGroup` at `bx = 3.60, by = 4.50`), and potted plants.
* **South Entrance Courtyard, Left Concrete Terrace & Stepped Front Yard (`3-Tier 25cm Elevations`):**
  * **3-Tier Stepped Elevations (`25cm` per tier):**
    1. **Main Villa Base Floor (`bz = 0.00m`):** Raised `+25cm` above both terraces (`+50cm` above exterior soil), supported by a travertine/concrete architectural podium slab with stepped threshold stairs at the main entrance door (`bx = 2.60, by = -5.00`).
    2. **Right Arched Courtyard (`bx = +1.40..+6.00m, by = -9.20..-5.00m, bz = -0.25m`) & Left Concrete Terrace (`bx = -6.00..+1.40m, by = -7.10..-5.00m, bz = -0.25m`):** Both sit `+25cm` above the exterior soil ground (`bz = -0.50m`). The left courtyard wall supporting the welcome arch (`bx = 1.40, by = -7.10`) is half-height (`1.15m`), matching the right courtyard wall (`bx = 6.00, by = -7.10`). The left terrace uses Poly Haven 1K PBR `concrete_pavement_02` and spans from the West edge of the villa (`bx = -6.00`) to the left arch wall (`bx = +1.40`) with a depth equal to half the left wall (`2.10m`).
    3. **Exterior Soil Ground (`bz = -0.50m`):** Textured with Poly Haven 1K PBR `brown_mud_rocks_01`, featuring specular rainwater puddles (`wetRingMat` & `puddleWaterMat` with organic multi-lobe alpha masks), manicured lawn beds (`matLawnBed`, `bz = -0.468m`) & travertine stepping stones leading to the welcome arch (`bx = 3.70, by = -9.20`), a **3m Ancient Unpotted Olive Tree** (`bx = -0.50, by = -8.25, floorY = -0.455`) with gnarled `bark_willow` 1K PBR trunks, root-heaved earth (`tree_stump_01` + `grass_bermuda_01`/`grass_medium_01` 3D tufts), and volumetric 3D canopy (`shrub_02`/`shrub_04` + curved 3D spherical dome shells) immediately left of the arched terrace, and a horizontal row of **5 Small Potted Olive Trees (~1.5m scale)** in alternating wooden & terracotta planters (`planter_box_01` + `planter_pot_clay` + `shrub_02`/`shrub_04`) at `by = -15.20m` (`bx = [-4.90, -2.45, 0.00, 2.45, 4.90], floorY = -0.455`). All 6 olive trees are registered as draggable/rotatable items with `localStorage` persistence.
* **2nd Floor Rooftop Terrace (`roofGroup`, elevation `bz = 3.78m`):**
  * Walnut pergola (`bx = 0.60..5.10m, by = -1.20..4.00m`), 3 rooftop lounge sofas (`r1`, `r1e`, `r2`), rooftop coffee table (`rt`), outdoor BBQ bar counter & `stone_fire_pit` (`bx = -4.65, by = 2.65`), and 3 barstools (`bar_chair_round_01`).

---

## 3. Critical Technical Rules in `Tunisia_Arab_House_Designer.html`
1. **Three.js r128 `EffectComposer` Color Space Rule:**
   * In Three.js r128, `EffectComposer` renders into an offscreen `WebGLRenderTarget`, which automatically bypasses `renderer.toneMapping` (`ACESFilmicToneMapping`) and `renderer.outputEncoding` (`sRGBEncoding`).
   * Therefore, `AgxContrastShader` (the final `ShaderPass` in `composer`) **MUST** keep `ACESFilm(tex.rgb * exposure)` and `pow(col, vec3(1.0 / 2.2))` inside its fragment shader. Never remove this, or the entire scene will look washed-out and linear.
2. **Sky Dome vs. HDRI Environment:**
   * Always keep `skyDomeMesh` (`skyDomeMat` GLSL shader) for the visible sky background so Day/Sunset/Night skies are crisp at 4K without 8-bit RGBE blockiness, while `hdriCache[mode].envMap` is assigned strictly to `scene.environment` for realistic PBR reflections.
3. **File Synchronization Rule:**
   * Always copy `Tunisia_Arab_House_Designer.html` to `index.html` (`cp Tunisia_Arab_House_Designer.html index.html`) before committing and pushing to `https://github.com/Laksma123/maitremaherhouse.git` so GitHub Pages always serves the latest version.

---

## 4. Completed Milestones (Verified in Real Browser)
1. **✅ Enhance FPS Without Reducing Visual Quality:**
   * Set `renderer.shadowMap.autoUpdate = false` and trigger `requestShadowUpdate()` (`renderer.shadowMap.needsUpdate = true`) only when GLTF models finish loading, objects move/rotate, doors/windows animate, or time-of-day/roof changes.
   * Removed redundant `archLights` and `openingLights` `PointLight` arrays (relying on emissive LED materials + half-res `UnrealBloomPass` + the 6 primary `zoneLights`) to cut fragment shader light-loop overhead by >60%.
   * Froze `matrixAutoUpdate = false` (`freezeStaticMeshes`) on static architectural meshes.
2. **✅ Live Tunisian News Broadcast on the Salon TV (~1-Minute Loop, 480p):**
   * Positioned `tvScr` on the front face of `tvFrame` (`z = -0.205`) facing the Majlis sofas and rendered a 480p looping Tunisian news broadcast video (`THREE.VideoTexture`) with an automatic live-rendered 480p Tunisian TV News `<canvas>` broadcast fallback (`updateTunisiaNewsBroadcast`, live news studio + Sidi Bou Said report + Arabic/French/English breaking news ticker *"الأخبار التونسية • الوطنية 1"*).
3. **✅ Fix Object Rotation & Clean Up Bottom Selection Toolbar (`#selection-hud`):**
   * Removed the 4 directional nudge buttons (`▲`, `▼`, `◀`, `▶`) from `#selection-hud`.
   * Prevented `window`'s `pointerup` listener from firing `deselectObject()` when clicking UI buttons (`if (!isDraggingObject && !walkState.looking && e.target !== renderer.domElement) return;`).
   * Centered bounding-box horizontal pivots inside `registerDraggable(...)` so all selectable objects rotate cleanly in place.
4. **✅ Replace Bottom-Right 4-Way D-Pad with a Fixed-Position MOBA Virtual Analog Joystick:**
   * Dual-circle virtual analog stick (`#walk-dpad` + `#joystick-knob`) in the bottom-right corner: fixed outer ring (`118px × 118px`) + 360° draggable inner thumb knob (`48px × 48px`) that smoothly drives proportional WASD movement/camera panning and springs back to center on release.
5. **✅ Fix Reversed Sofa Orientations (Ground Floor & Rooftop) & Make 100% of Objects Selectable/Movable/Rotatable (Except Walls, Doors, and Windows):**
   * Fixed the rotation of the Majlis South (`Math.PI`) & East (`-Math.PI/2`) sofas and the Rooftop North (`0`), East (`-Math.PI/2`), and South (`Math.PI`) sofas so all sofas face inward toward their coffee tables/TV.
   * Removed doors & windows (`openingsGroup.children`) from `draggableObjects` (they only open/close on click or `F`), and registered all non-structural furniture, lamps, wall sconces, plants, olive trees, kitchen counters, bathroom fixtures, fountain, rugs, and rooftop items via `registerDraggable(...)`.
6. **✅ Exterior Landscaping, 3-Tier 25cm Stepped Elevations, Left Concrete Terrace, Half-Height Left Arch Wall, 5 Potted Olive Trees & 3m Ancient Olive Tree:**
   * Lowered the left courtyard entrance wall (`bx = 1.40, by = -7.10`) to `1.15m` (half height, matching the right courtyard wall).
   * Built the left concrete terrace (`concrete_pavement_02` 1K PBR, `bx = -6.00..+1.40, by = -5.00..-7.10`) and implemented the 3-tier `25cm` elevation steps (`0.00m` Villa Floor -> `-0.25m` Concrete & Arched Terraces -> `-0.50m` Exterior Soil Ground).
   * Added the 3m unpotted Ancient Olive Tree (`bx = -0.05, by = -8.25, bz = -0.50`) immediately left of the arched wall with realistic root flare (`tree_stump_01` + surface roots), radial soil cracks, and thick uprooted 3D grass (`grass_bermuda_01`, `grass_medium_01`), plus 5 small potted ~1.5m olive trees (`planter_box_01` + `planter_pot_clay` + `shrub_02`/`shrub_04`) in a horizontal row across the front (`by = -15.20m`), realistic exterior soil (`brown_mud_rocks_01` 1K PBR) with specular rainwater puddles, and manicured grass borders.
