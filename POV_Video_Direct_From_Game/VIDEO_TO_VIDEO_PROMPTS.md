# Panduan AI Video-to-Video (V2V) V2 — Anti-Halusinasi & Pengunci Geometri 1:1 (Khusus Gemini / Flow / Veo)

Folder ini berisi rekaman **First-Person POV Walkthrough (`1920×1080`, `30 FPS`)** langsung dari simulasi **`Tunisia_Arab_House_Designer.html`** beserta **Prompt V2 Anti-Halusinasi** yang telah diperbaiki agar **Gemini / Google Flow / Runway / Luma** hanya mengubah tekstur & pencahayaan menjadi dunia nyata **tanpa menambah bangunan, tanpa melubangi dinding menjadi pintu/jendela baru, tanpa menambah kanopi, dan tanpa melebarkan kolam renang**.

---

## Mengapa Versi Sebelumnya Mengubah Objek di Gemini? (Sudah Diperbaiki di V2)

1. **Efek Kata Kunci Budaya (`"Sidi Bou Said Tunisian villa"`):** Saat membaca frasa tersebut, AI otomatis membayangkan kompleks perkampungan bertingkat sehingga mengarang gedung tambahan di langit kosong serta menambahkan jendela & pintu lengkung biru di dinding polos. **Di V2, kata pemicu tersebut dihapus total** (karena warna putih-biru sudah otomatis terbaca dari piksel video).
2. **Daftar Benda di Prompt Global Lama (`"doors, pergolas, stairs, walnut wood"`):** Menyebut kata *pergolas* dan *doors* di prompt global membuat Gemini memaksakan kanopi biru, sofa kayu tinggi, dan pintu tambahan pada `Clip 01` padahal objek itu milik klip lain. **Di V2, Prompt Global bebas 100% dari nama perabot/bangunan spesifik.**
3. **Lengkungan Keramik Dekoratif & Langit Kosong:** Dinding dekoratif bermotif biru yang rata sempat dikira pintu ruangan terbuka oleh AI, dan tepi dek batu kolam dikira air sehingga kolam melebar. **Di V2, batas siluet air, dinding masif polos, langit kosong, dan panel keramik rata dikunci secara eksplisit.**

---

## 1. PROMPT GLOBAL V2 — STRICT 1:1 GEOMETRY LOCK (Gunakan Ini untuk Semua Klip `01` s/d `10`)

Salin **1 prompt global** di bawah ini saat mengunggah klip video ke **Gemini / Google Flow**:

```text
STRICT 1:1 VIDEO-TO-VIDEO RETEXTURING ONLY — DO NOT EMBELLISH, REDESIGN, OR ADD ANY NEW ARCHITECTURE OR OBJECTS.

Convert this 3D walkthrough video into authentic real-world live-action footage filmed on a Sony FX3 24mm f/4 camera in natural daylight, while locking 100% of the exact camera trajectory, perspective, object silhouettes, wall boundaries, proportions, and color placement of the uploaded video frame-by-frame.

MANDATORY GEOMETRY & ANTI-HALLUCINATION RULES:
1. Exact Silhouette Lock: Treat every edge and shape in the input video as fixed physical reality. Do not add, delete, move, stretch, or replace any structure or object.
2. Empty Sky & Horizon Stay Empty: Keep all open sky and flat empty ground completely open and empty — NEVER invent or add extra buildings, neighboring houses, courtyard wings, extra walls, or upper floors.
3. Blank Solid Walls Stay Solid: Every flat white wall and solid diagonal stair side-wall in the input video must remain 100% solid, flat, and unbroken — NEVER add new windows, doors, shutters, wall niches, or open stair railings.
4. Closed Decorative Wall Panels Stay Closed: Any blue-patterned arch shapes on walls that are closed in the input video are flat decorative ceramic tile panels flush on a solid wall — NEVER open them into doorways, rooms, or windows.
5. Open-Air Spaces Stay Uncovered: Keep uncovered terraces and yards completely open to the sky — NEVER add roofs, canopies, or overhead frames where none exist in the input video.
6. Exact Pool & Furniture Proportions: Preserve the exact narrow rectangular boundary of any water basin inside its wide flat stone deck border without widening or reshaping the water, and keep low floor cushions flat on the ground at their exact height without swapping them for tall chairs or sofas.

PHOTOREALISTIC SURFACE & LIGHTING PASS ONLY:
Upgrade ONLY the surfaces already visible in each frame from synthetic 3D CGI shading into real-world physical materials: natural slightly textured whitewashed masonry, painted blue wood/trim only where already blue in the input video, real stone and polished marble, realistic rippling water with sunlight reflections, organic tree bark and leaves, natural gravel and soil, realistic fabric, glass, and metal, natural sun shadows, and true optical lens exposure with zero CGI or video-game look.
```

---

## 2. PROMPT SPESIFIK PER KLIP V2 (Opsional — Gunakan Jika Ada Klip Tertentu yang Ingin Dikunci Ekstra Ketat)

Jika pada klip tertentu Gemini masih mencoba berimprovisasi saat memakai Prompt Global di atas, gunakan prompt khusus klip tersebut di bawah ini:

### Clip 01 — `01_Exit_Car_Walk_To_Swimming_Pool.mp4` (`0.0s – 9.5s`)
```text
STRICT 1:1 VIDEO-TO-VIDEO RETEXTURING ONLY — DO NOT ADD BUILDINGS, DOORS, WINDOWS, OR ROOFS.
Convert this 3D video into real-world Sony FX3 24mm daylight footage while preserving 100% of exact geometry, camera movement, and proportions frame-by-frame:
- Foreground right: realistic metallic orange 5-door hatchback car parked on natural gravel soil, passing a large gnarled green shade tree with roots and grass tufts, and a painted blue wooden diamond-lattice fence with a blue arched gate on the far right.
- Left & background horizon: keep the area to the left of the pool as completely empty open gravel ground and clear sky (with only the small distant blue tractor visible early on) — DO NOT add any buildings, walls, or second stories on the left.
- Swimming pool: keep the exact narrow rectangular turquoise water strip recessed inside the wide flat white stone deck — DO NOT widen the pool water and DO NOT add underwater steps; keep the tiny low wooden drink table with glass bottles and two flat floor cushions at the front corner of the white deck.
- Building walls & stairs: keep the diagonal exterior staircase wall 100% solid flat white masonry with thin blue top trim (NO open railings, NO doors or niches cut into the stair wall, only the single narrow vertical slit window near the back corner).
- Front terrace on the right: keep completely open to the sky with NO overhead roof or pergola, low floor cushions on the terrace, and flat closed blue-tile decorative arch panels on a solid unbroken white wall (DO NOT open the wall into a room or doorway).
Upgrade only lighting, shadows, and real physical material textures with zero CGI look.
```

### Clip 02 — `02_Enter_Blue_Gate_Walk_Small_Olives.mp4` (`9.5s – 19.5s`)
```text
STRICT 1:1 VIDEO-TO-VIDEO RETEXTURING ONLY — DO NOT ADD EXTRA BUILDINGS, WINDOWS, OR DOORS.
Convert this 3D video into real-world Sony FX3 24mm daylight footage while locking 100% of exact camera motion and object geometry frame-by-frame: walking from the stone pool deck toward the painted blue wooden diamond-lattice fence, passing directly under the open blue wooden arch gate onto white rectangular stepping stones bordered by narrow green grass strips, surrounded by natural pebble soil and young unpotted olive trees. Keep all white building walls in the background at their exact single-story flat-roofed cubic outlines with closed blue-tile wall panels, empty sky above, and zero added upper floors or extra windows. Upgrade only surface textures, real olive leaves, wood grain, stone, and natural sunlight shadows.
```

### Clip 03 — `03_Enter_Front_Terrace_And_Main_Door.mp4` (`19.5s – 29.0s`)
```text
STRICT 1:1 VIDEO-TO-VIDEO RETEXTURING ONLY — DO NOT ADD WINDOWS OR EXTRA STRUCTURES ON BLANK WALLS.
Convert this 3D video into real-world Sony FX3 24mm daylight footage while locking 100% of exact camera motion and geometry frame-by-frame: walking past young olive trees, a covered outdoor BBQ grill counter, and a two-level grey concrete cactus planter and grill in front of a completely blank solid white divider wall (keep all blank white walls 100% windowless and doorless), stepping through the white arched terrace entrance, and walking through the double painted-blue arched wooden front doors swinging inward into a bright marble room. Upgrade only real physical surface textures, natural daylight, and shadows with zero CGI look.
```

### Clip 04 — `04_Enter_Kitchen_And_Hammam_Bathroom.mp4` (`29.0s – 39.5s`)
```text
STRICT 1:1 VIDEO-TO-VIDEO RETEXTURING ONLY — DO NOT ALTER ROOM LAYOUT, CABINETS, OR FIXTURES.
Convert this 3D interior video into real-world Sony FX3 24mm footage while locking 100% of exact camera motion, walls, doors, and furniture placement frame-by-frame: walking across polished cream marble floors past a stainless fridge and dark wood L-shaped kitchen counter with patterned blue-and-white tile backsplash, stove, brass pot, and barstools, then passing through the open blue arched wooden bathroom door into a bright tiled bathroom with glass walk-in shower and dark wood vanity with brass vessel sink and ornate mirror. Do not add windows or extra props; upgrade only realistic marble, ceramic tile, wood, glass, brass reflections, and soft indoor lighting.
```

### Clip 05 — `05_Exit_Bathroom_Lie_On_Bed_Ceiling.mp4` (`39.5s – 50.5s`)
```text
STRICT 1:1 VIDEO-TO-VIDEO RETEXTURING ONLY — DO NOT ADD WINDOWS, DOORS, OR EXTRA FURNITURE.
Convert this 3D interior video into real-world Sony FX3 24mm footage while locking 100% of exact camera motion and room geometry frame-by-frame: panning past the white porcelain toilet and patterned blue bathroom floor tiles, walking out through the open blue arched doorway into the bright cream-marble bedroom with a dark carved wooden bed, woven rug, and nightstands, and reclining onto the bed looking straight up at the flat white ceiling and hanging brass chandelier. Keep all solid walls and flat blue-patterned decorative wall arches completely closed and windowless; upgrade only real fabric, wood, marble, brass, and natural indoor light.
```

### Clip 06 — `06_Stand_From_Bed_Sit_On_Sofa_Watch_TV.mp4` (`50.5s – 62.2s`)
```text
STRICT 1:1 VIDEO-TO-VIDEO RETEXTURING ONLY — KEEP ALL DECORATIVE WALL ARCHES FLAT AND CLOSED.
Convert this 3D interior video into real-world Sony FX3 24mm footage while locking 100% of exact camera motion, furniture placement, and wall geometry frame-by-frame: rising from the wooden bed, walking across cream marble floors into the living salon with woven rugs, carved sofas, armchairs, coffee tables, indoor potted plants, hanging chandeliers, and a flatscreen TV mounted on the wall playing a news broadcast, then sitting down facing the TV. CRITICAL: all large blue-and-white patterned arches along the white living room walls are flat, closed ceramic tile wall panels — NEVER turn them into windows, glass doors, or open hallways. Upgrade only realistic fabric, wood, marble, plant leaves, and indoor lighting.
```

### Clip 07 — `07_Exit_House_Circle_To_Blue_Stairs.mp4` (`62.2s – 75.2s`)
```text
STRICT 1:1 VIDEO-TO-VIDEO RETEXTURING ONLY — DO NOT ADD ROOFS, PERGOLAS, DOORS, OR EXTRA BUILDINGS.
Convert this 3D video into real-world Sony FX3 24mm daylight footage while locking 100% of exact camera motion and geometry frame-by-frame: standing up from the living room sofa, walking out through the open blue arched front doors onto the outdoor stone terrace, turning right past the uncovered low floor cushions (keep terrace open to the sky with NO roof or pergola overhead, and keep blue-tiled wall arches flat and closed on the solid white wall), and walking to the base of the exterior white-and-blue diagonal staircase beside the narrow rectangular pool. Keep open sky and empty ground on the left completely free of extra buildings. Upgrade only real stone, plaster, wood, foliage, and sunlight.
```

### Clip 08 — `08_Climb_Stairs_Sit_On_Rooftop_Sofa.mp4` (`75.2s – 86.5s`)
```text
STRICT 1:1 VIDEO-TO-VIDEO RETEXTURING ONLY — KEEP STAIR WALLS SOLID AND HORIZON EMPTY.
Convert this 3D video into real-world Sony FX3 24mm daylight footage while locking 100% of exact camera motion and geometry frame-by-frame: walking up the exterior stairs between two completely solid flat white masonry walls with painted blue step treads and a solid blue-capped parapet wall on the left (NO open railings, NO windows or doors on the house wall), stepping onto the flat sunlit rooftop terrace past the tiled outdoor bar counter with three wooden barstools, walking under the existing blue wooden pergola frame, and sitting down on the low floor cushions beside a low marble tea table on a woven rug. Keep surrounding sky horizons completely empty with NO added neighbor buildings.
```

### Clip 09 — `09_Stand_Rooftop_Look_Down_At_Livestock.mp4` (`86.5s – 96.5s`)
```text
STRICT 1:1 VIDEO-TO-VIDEO RETEXTURING ONLY — DO NOT ADD EXTRA BUILDINGS ON THE HORIZON.
Convert this 3D video into real-world Sony FX3 24mm daylight footage while locking 100% of exact camera motion and geometry frame-by-frame: standing up from the low rooftop floor cushions under the blue wooden pergola, walking across the flat rooftop tile floor to the solid white parapet wall, and looking down into the enclosed farm paddock below (bounded by a low white wall topped with a blue wooden diamond-lattice fence) where real white goats, chickens, and rabbits roam on pebble soil. Keep the distant landscape and sky open and flat with NO invented buildings, roofs, or extra animals beyond those visible in the video.
```

### Clip 10 — `10_Rooftop_Panorama_Around_Entire_Villa.mp4` (`96.5s – 105.0s`)
```text
STRICT 1:1 VIDEO-TO-VIDEO RETEXTURING ONLY — PRESERVE EXACT DISTANT LAYOUT AND EMPTY HORIZON.
Convert this 3D video into real-world Sony FX3 24mm daylight footage while locking 100% of exact camera motion, rooftop potted plants, white parapet walls, and surrounding yard layout frame-by-frame: walking along the sunlit white rooftop parapet while panning across the open yard below — preserving the exact positions and sizes of the young olive trees, blue wooden lattice fences, grapevine-covered terrace pergola, glowing stone fire pit, moving blue tractor on soil, narrow rectangular swimming pool inside its wide white stone deck, large green shade tree, gravel road, and parked orange hatchback car. Keep the open horizon completely free of extra houses or hills; upgrade only real-world textures, foliage, water reflections, and natural sunlight.
```
