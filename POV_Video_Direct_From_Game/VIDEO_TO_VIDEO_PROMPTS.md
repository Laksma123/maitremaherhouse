# Panduan AI Video-to-Video (V2V) V3 — Kunci Geometri 1:1 + Anti-Glitch Objek Dekat / Mobil (Khusus Gemini / Flow / Veo)

Folder ini berisi rekaman **First-Person POV Walkthrough (`1920×1080`, `30 FPS`)** langsung dari simulasi **`Tunisia_Arab_House_Designer.html`** beserta **Prompt V3 Final** yang mempertahankan **100% akurasi bangunan & kolam dari V2** sekaligus memperbaiki **glitch mobil/objek dekat yang tiba-tiba melompat atau mengecil saat kamera berjalan melewatinya**.

---

## Mengapa Mobil Tiba-Tiba Melompat di Detik ke-1 pada V2? (Sudah Diperbaiki di V3)

Saat dicek per-frame (`detik 0.67 -> 1.00`), di awal klip posisi kamera berdiri sangat dekat di samping pintu mobil sehingga hanya bagian **kaca samping dan kap depan mobil** yang terlihat terpotong batas bawah layar. Karena di V2 tertulis kalimat kaku *"Do not delete or move any object"*, saat kamera berjalan maju dan bodi mobil mulai keluar dari batas bawah layar, AI panik mengira mobilnya tidak boleh terpotong lalu **melompatkan/mengecilkan seluruh bodi mobil lengkap dengan rodanya** agar muat di sudut kanan bawah layar.

**Di V3:** Aturan #1 diperbarui secara presisi agar AI paham bahwa **kamera sedang berjalan maju melewati objek yang diam terparkir di tanah**, sehingga bagian dekat yang berada di tepi layar harus **tetap berukuran besar (*close-up* konstan), terpotong secara alami oleh bingkai kamera, dan meluncur mulus keluar layar tanpa pernah melompat, bergeser, atau mengecil**.

---

## 1. PROMPT GLOBAL V3 — STRICT 1:1 GEOMETRY LOCK + ANTI-JUMP PASS-BY (Untuk Semua Klip `01` s/d `10`)

Salin **1 prompt global** di bawah ini saat mengunggah klip video ke **Gemini / Google Flow**:

```text
STRICT 1:1 VIDEO-TO-VIDEO RETEXTURING ONLY — DO NOT EMBELLISH, REDESIGN, OR ADD ANY NEW ARCHITECTURE OR OBJECTS.

Convert this first-person POV 3D walkthrough video into authentic real-world live-action footage filmed on a smooth gimbal Sony FX3 24mm f/4 camera walking forward in natural daylight, locking 100% of the exact camera trajectory, perspective, object silhouettes, wall boundaries, proportions, and color placement of the uploaded video frame-by-frame.

MANDATORY GEOMETRY, TEMPORAL CONTINUITY & ANTI-HALLUCINATION RULES:
1. Stationary 3D World-Space & Smooth Close-Up Cropping (Zero Object Jumping): Every parked object, structure, and piece of furniture must remain 100% motionless and anchored to the ground in 3D world space at a constant real-world scale from start to finish. Whenever the walking camera passes close beside a foreground object at the bottom or side edge of the screen, render ONLY the exact close-up cropped portion visible in each input frame (keeping its lower base off-screen below the frame) and let that close-up surface glide smoothly out of view — NEVER snap, jump, teleport, roll, or shrink a cropped foreground object into a smaller full-body object inside the corner of the frame, and do not invent or erase scene structures.
2. Empty Sky & Horizon Stay Empty: Keep all open sky and flat empty ground completely open and empty — NEVER invent or add extra buildings, neighboring houses, courtyard wings, extra walls, or upper floors.
3. Blank Solid Walls Stay Solid: Every flat white wall and solid diagonal stair side-wall in the input video must remain 100% solid, flat, and unbroken — NEVER add new windows, doors, shutters, wall niches, or open stair railings.
4. Closed Decorative Wall Panels Stay Closed: Any blue-patterned arch shapes on walls that are closed in the input video are flat decorative ceramic tile panels flush on a solid wall — NEVER open them into doorways, rooms, or windows.
5. Open-Air Spaces Stay Uncovered: Keep uncovered terraces and yards completely open to the sky — NEVER add roofs, canopies, or overhead frames where none exist in the input video.
6. Exact Pool & Furniture Proportions: Preserve the exact narrow rectangular boundary of any water basin inside its wide flat stone deck border without widening or reshaping the water, and keep low floor cushions flat on the ground at their exact height without swapping them for tall chairs or sofas.

PHOTOREALISTIC SURFACE & LIGHTING PASS ONLY:
Upgrade ONLY the surfaces already visible in each frame from synthetic 3D CGI shading into real-world physical materials: natural slightly textured whitewashed masonry, painted blue wood/trim only where already blue in the input video, real stone and polished marble, realistic rippling water with sunlight caustics, organic tree bark and leaves, natural gravel and soil, realistic fabric, glass, and metallic paint, natural sun shadows, and true optical lens exposure with zero CGI or video-game look.
```

---

## 2. PROMPT KHUSUS `Clip 01` ANTI-GLITCH MOBIL (Opsional Jika Ingin Mengunci Mobil di `Clip 01` 2x Lebih Ketat)

Karena mobil *close-up* **hanya ada di `Clip 01`** (`01_Exit_Car_Walk_To_Swimming_Pool.mp4`), Anda bisa mencoba `Prompt Global V3` di atas terlebih dahulu, atau langsung memakai prompt khusus `Clip 01` di bawah ini yang secara spesifik melarang mobil melompat/memunculkan roda:

```text
STRICT 1:1 VIDEO-TO-VIDEO RETEXTURING ONLY — DO NOT ADD BUILDINGS, DOORS, WINDOWS, OR ROOFS, AND DO NOT JUMP OR RESCALE THE PARKED CAR.

Convert this first-person POV 3D video into real-world Sony FX3 24mm gimbal daylight footage while locking 100% of exact geometry, camera movement, and proportions frame-by-frame:
- Stationary Close-Up Parked Car (CRITICAL — ZERO JUMPING): The metallic orange car in the lower-right foreground is 100% PARKED, ENGINE OFF, AND COMPLETELY MOTIONLESS on the ground behind/beside the walking camera. Keep the car at constant close-up 1:1 scale throughout the first 4 seconds — NEVER jump, snap, roll forward, or shrink the car into a full-body view, and NEVER reveal its wheels or tires. Render ONLY the close-up upper side window, side mirror, windshield corner, and front hood tip visible in each input frame as they glide smoothly downward and exit off the bottom-right edge of the screen as the viewer walks past.
- Left & background horizon: keep the area to the left of the pool as completely empty open gravel ground and clear sky (with only the small distant blue tractor visible early on) — DO NOT add any buildings, walls, or second stories.
- Swimming pool & deck: keep the exact narrow rectangular turquoise water strip recessed inside the wide flat white stone deck without widening the water; keep the small low wooden drink table with bottles and two flat floor cushions at the front corner of the white deck.
- Building walls, stairs & terrace: keep the diagonal exterior staircase wall 100% solid flat white masonry with thin blue top trim (NO open railings, NO doors or niches), keep the front terrace on the right completely uncovered under open sky (NO pergola or roof), and keep the blue-patterned wall arches flat and closed as ceramic wall tiles on a solid unbroken white wall.
Upgrade only lighting, dappled tree shadows, and real physical material textures with zero CGI look.
```

---

## 3. PROMPT SPESIFIK KLIP LAINNYA (`Clip 02` s/d `Clip 10`)

*(Untuk `Clip 02` s/d `Clip 10`, **`PROMPT GLOBAL V3`** di Bagian 1 sudah 100% akurat dan konsisten. Prompt per-klip di bawah ini hanya cadangan opsional bila diperlukan.)*

### Clip 02 — `02_Enter_Blue_Gate_Walk_Small_Olives.mp4` (`9.5s – 19.5s`)
```text
STRICT 1:1 VIDEO-TO-VIDEO RETEXTURING ONLY — DO NOT ADD EXTRA BUILDINGS, WINDOWS, OR DOORS.
Convert this first-person POV 3D video into real-world Sony FX3 24mm daylight footage while locking 100% of exact camera motion, smooth foreground cropping, and object geometry frame-by-frame: walking from the stone pool deck toward the painted blue wooden diamond-lattice fence, passing smoothly under the open blue wooden arch gate onto white rectangular stepping stones bordered by narrow green grass strips, surrounded by natural pebble soil and young unpotted olive trees. Keep all white building walls in the background at their exact single-story flat-roofed cubic outlines with closed blue-tile wall panels, empty sky above, and zero added upper floors or extra windows. Upgrade only surface textures, real olive leaves, wood grain, stone, and natural sunlight shadows.
```

### Clip 03 — `03_Enter_Front_Terrace_And_Main_Door.mp4` (`19.5s – 29.0s`)
```text
STRICT 1:1 VIDEO-TO-VIDEO RETEXTURING ONLY — DO NOT ADD WINDOWS OR EXTRA STRUCTURES ON BLANK WALLS.
Convert this first-person POV 3D video into real-world Sony FX3 24mm daylight footage while locking 100% of exact camera motion, smooth pass-by cropping, and geometry frame-by-frame: walking past young olive trees, a covered outdoor BBQ grill counter, and a two-level grey concrete cactus planter and grill in front of a completely blank solid white divider wall (keep all blank white walls 100% windowless and doorless), stepping through the white arched terrace entrance, and walking smoothly through the double painted-blue arched wooden front doors swinging inward into a bright marble room. Upgrade only real physical surface textures, natural daylight, and shadows with zero CGI look.
```

### Clip 04 — `04_Enter_Kitchen_And_Hammam_Bathroom.mp4` (`29.0s – 39.5s`)
```text
STRICT 1:1 VIDEO-TO-VIDEO RETEXTURING ONLY — DO NOT ALTER ROOM LAYOUT, CABINETS, OR FIXTURES.
Convert this first-person POV 3D interior video into real-world Sony FX3 24mm footage while locking 100% of exact camera motion, smooth doorway pass-by, walls, doors, and furniture placement frame-by-frame: walking across polished cream marble floors past a stainless fridge and dark wood L-shaped kitchen counter with patterned blue-and-white tile backsplash, stove, brass pot, and barstools, then passing smoothly through the open blue arched wooden bathroom door into a bright tiled bathroom with glass walk-in shower and dark wood vanity with brass vessel sink and ornate mirror. Do not add windows or extra props; upgrade only realistic marble, ceramic tile, wood, glass, brass reflections, and soft indoor lighting.
```

### Clip 05 — `05_Exit_Bathroom_Lie_On_Bed_Ceiling.mp4` (`39.5s – 50.5s`)
```text
STRICT 1:1 VIDEO-TO-VIDEO RETEXTURING ONLY — DO NOT ADD WINDOWS, DOORS, OR EXTRA FURNITURE.
Convert this first-person POV 3D interior video into real-world Sony FX3 24mm footage while locking 100% of exact camera motion, smooth foreground cropping, and room geometry frame-by-frame: panning past the white porcelain toilet and patterned blue bathroom floor tiles, walking out through the open blue arched doorway into the bright cream-marble bedroom with a dark carved wooden bed, woven rug, and nightstands, and reclining smoothly onto the bed looking straight up at the flat white ceiling and hanging brass chandelier. Keep all solid walls and flat blue-patterned decorative wall arches completely closed and windowless; upgrade only real fabric, wood, marble, brass, and natural indoor light.
```

### Clip 06 — `06_Stand_From_Bed_Sit_On_Sofa_Watch_TV.mp4` (`50.5s – 62.2s`)
```text
STRICT 1:1 VIDEO-TO-VIDEO RETEXTURING ONLY — KEEP ALL DECORATIVE WALL ARCHES FLAT AND CLOSED.
Convert this first-person POV 3D interior video into real-world Sony FX3 24mm footage while locking 100% of exact camera motion, stationary furniture scale, and wall geometry frame-by-frame: rising from the wooden bed, walking across cream marble floors into the living salon with woven rugs, carved sofas, armchairs, coffee tables, indoor potted plants, hanging chandeliers, and a flatscreen TV mounted on the wall playing a news broadcast, then sitting down facing the TV. CRITICAL: all large blue-and-white patterned arches along the white living room walls are flat, closed ceramic tile wall panels — NEVER turn them into windows, glass doors, or open hallways. Upgrade only realistic fabric, wood, marble, plant leaves, and indoor lighting.
```

### Clip 07 — `07_Exit_House_Circle_To_Blue_Stairs.mp4` (`62.2s – 75.2s`)
```text
STRICT 1:1 VIDEO-TO-VIDEO RETEXTURING ONLY — DO NOT ADD ROOFS, PERGOLAS, DOORS, OR EXTRA BUILDINGS.
Convert this first-person POV 3D video into real-world Sony FX3 24mm daylight footage while locking 100% of exact camera motion, smooth doorway pass-by, and geometry frame-by-frame: standing up from the living room sofa, walking out through the open blue arched front doors onto the outdoor stone terrace, turning right past the uncovered low floor cushions (keep terrace open to the sky with NO roof or pergola overhead, and keep blue-tiled wall arches flat and closed on the solid white wall), and walking to the base of the exterior white-and-blue diagonal staircase beside the narrow rectangular pool. Keep open sky and empty ground on the left completely free of extra buildings. Upgrade only real stone, plaster, wood, foliage, and sunlight.
```

### Clip 08 — `08_Climb_Stairs_Sit_On_Rooftop_Sofa.mp4` (`75.2s – 86.5s`)
```text
STRICT 1:1 VIDEO-TO-VIDEO RETEXTURING ONLY — KEEP STAIR WALLS SOLID AND HORIZON EMPTY.
Convert this first-person POV 3D video into real-world Sony FX3 24mm daylight footage while locking 100% of exact camera motion, smooth foreground cropping, and geometry frame-by-frame: walking up the exterior stairs between two completely solid flat white masonry walls with painted blue step treads and a solid blue-capped parapet wall on the left (NO open railings, NO windows or doors on the house wall), stepping onto the flat sunlit rooftop terrace past the tiled outdoor bar counter with three wooden barstools, walking under the existing blue wooden pergola frame, and sitting down on the low floor cushions beside a low marble tea table on a woven rug. Keep surrounding sky horizons completely empty with NO added neighbor buildings.
```

### Clip 09 — `09_Stand_Rooftop_Look_Down_At_Livestock.mp4` (`86.5s – 96.5s`)
```text
STRICT 1:1 VIDEO-TO-VIDEO RETEXTURING ONLY — DO NOT ADD EXTRA BUILDINGS ON THE HORIZON.
Convert this first-person POV 3D video into real-world Sony FX3 24mm daylight footage while locking 100% of exact camera motion and geometry frame-by-frame: standing up from the low rooftop floor cushions under the blue wooden pergola, walking across the flat rooftop tile floor to the solid white parapet wall, and looking down into the enclosed farm paddock below (bounded by a low white wall topped with a blue wooden diamond-lattice fence) where real white goats, chickens, and rabbits roam on pebble soil. Keep the distant landscape and sky open and flat with NO invented buildings, roofs, or extra animals beyond those visible in the video.
```

### Clip 10 — `10_Rooftop_Panorama_Around_Entire_Villa.mp4` (`96.5s – 105.0s`)
```text
STRICT 1:1 VIDEO-TO-VIDEO RETEXTURING ONLY — PRESERVE EXACT DISTANT LAYOUT, FOREGROUND POTS, AND EMPTY HORIZON.
Convert this first-person POV 3D video into real-world Sony FX3 24mm daylight footage while locking 100% of exact camera motion, stationary close-up rooftop potted plants sliding smoothly along the bottom edge of the frame, white parapet walls, and surrounding yard layout frame-by-frame: walking along the sunlit white rooftop parapet while panning across the open yard below — preserving the exact positions and sizes of the young olive trees, blue wooden lattice fences, grapevine-covered terrace pergola, glowing stone fire pit, moving blue tractor on soil, narrow rectangular swimming pool inside its wide white stone deck, large green shade tree, gravel road, and parked orange hatchback car. Keep the open horizon completely free of extra houses or hills; upgrade only real-world textures, foliage, water reflections, and natural sunlight.
```
