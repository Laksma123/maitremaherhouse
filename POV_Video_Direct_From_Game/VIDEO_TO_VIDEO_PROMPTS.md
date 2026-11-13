# Panduan AI Video-to-Video (V2V) — Rekaman Langsung dari Game HTML

Folder ini berisi rekaman **First-Person POV Walkthrough (`1920×1080`, `30 FPS`)** yang dirender langsung dari simulasi aktif **`Tunisia_Arab_House_Designer.html`** dengan tema warna **Sidi Bou Said** (putih bersih & biru langit musim panas) serta seluruh **121 objek personalisasi** Anda pada pencahayaan siang hari Mediterania yang natural.

---

## Daftar File Video

1. **`00_FULL_POV_Walkthrough_Master_1080p.mp4`** (`105.0 detik`, `1920×1080`, `30 FPS`)
   * Video utuh dari awal hingga akhir tanpa putus (mulai turun dari mobil di luar pagar hingga naik ke *rooftop*, menengok hewan ternak di bawah, dan menyapu pandangan keliling rumah).
2. **`Clips_For_AI_Video2Video/` (`01_...mp4` s/d `10_...mp4`)**
   * Potongan berurutan berdurasi **8.5 – 13.0 detik** per klip tanpa frame yang hilang (*seamless cut*).
   * Disiapkan khusus karena hampir semua platform **AI Video-to-Video** (**Runway Gen-4 / Gen-3 Video-to-Video**, **Luma Ray 2 Modify Video**, **Kling AI**, **DomoAI**, **Wan 2.1 V2V**) membatasi durasi input sekitar **10 detik per klip**.
   * Karena pergerakan kamera dan posisi objek 100% berasal dari video asli game HTML ini, **tidak akan ada lagi kejutan sudut pandang atau objek yang berubah posisi** antar-klip!

---

## Pengaturan Rekomendasi di AI Video-to-Video

* **Runway (Gen-3 Alpha / Gen-4 Video-to-Video):** Set *Structure Transformation* ke **Low / Adherence High** (`0.35 – 0.50`) agar tata ruang, pintu, pagar biru, dan furnitur tetap 100% akurat sesuai game namun permukaan material berubah menjadi foto/video dunia nyata.
* **Luma Dream Machine (Ray 2 — Modify Video):** Pilih tingkat perubahan **Adhere / Flex** agar geometri 3D terkunci rapat sementara pencahayaan, dedaunan, air kolam, kulit sofa, dan batu kerikil menjadi realistis nyata.

---

## Prompt Global Universal (Bekerja untuk SEMUA Klip Sekaligus — Indoor & Outdoor)

Gunakan **1 prompt global** di bawah ini untuk **seluruh klip (`01` s/d `10`)** tanpa perlu mengganti-ganti teks per klip. Rumusan kalimatnya dirancang secara adaptif (*reference-conditioned*) agar AI **hanya menerjemahkan objek dan ruangan yang sedang tampil pada video referensi** menjadi rekaman kamera dunia nyata tanpa menambah atau mengarang objek dari adegan lain:

### Opsi A — Prompt Global Lengkap (Runway Gen-4 / Luma Ray 2 / Kling / Gemini / Veo)
```text
Transform this 3D reference video into an ultra-realistic, live-action real-world first-person walkthrough video filmed on a Sony FX3 24mm f/2.8 gimbal camera under natural Mediterranean daylight. Strictly lock and preserve 100% of the reference video's exact camera movement, perspective, room geometry, object placement, door motion, and Sidi Bou Said white-and-blue color palette — do not add, remove, or invent any objects. Replace all synthetic 3D CGI textures with authentic real-world physical materials wherever they appear in frame: weathered lime-plastered whitewashed masonry walls, painted cobalt-blue timber doors, fences, stairs, and pergolas, genuine polished Carthage marble and glazed Zellige ceramic tiles, rich carved walnut wood, woven rugs and fabric cushions, realistic metallic car paint and glass, natural crushed limestone gravel and dry pebble soil, organic sun-dappled olive and broadleaf tree foliage, crystal-clear rippling pool water with sunlight caustics, natural wood smoke, and real living farm animals. True optical lens exposure, natural global illumination, soft sun shadows, micro-surface imperfections, photorealistic documentary cinematography, zero 3D render or video-game look.
```

### Opsi B — Prompt Global Ringkas (Untuk Platform dengan Batas Karakter Pendek seperti DomoAI / Pika)
```text
Convert this 3D reference video into a photorealistic real-world live-action POV video shot on Sony FX3 24mm under natural Mediterranean daylight. Strictly preserve exact camera motion, geometry, colors, and object layout from the reference video while transforming every visible indoor and outdoor surface into authentic real-world materials, real foliage, real water, real stone, wood, fabric, and natural sun shadows. Zero CGI look.
```

---

## Prompt Spesifik Per Klip (`Clips_For_AI_Video2Video/`)

### Clip 01 — `01_Exit_Car_Walk_To_Swimming_Pool.mp4` (`0.0s – 9.5s`)
```text
Photorealistic live-action first-person POV video stepping out beside a real metallic sunset-orange Peugeot 308 hatchback parked on a country gravel road outside a whitewashed Sidi Bou Said Tunisian villa, walking beneath a giant Mediterranean shade tree toward a raised white marble swimming pool with shimmering turquoise water ripples and a low wooden poolside drink table under natural sunlit sky. Strictly preserve input geometry and camera movement.
```

### Clip 02 — `02_Enter_Blue_Gate_Walk_Small_Olives.mp4` (`9.5s – 19.5s`)
```text
Photorealistic live-action first-person POV video walking from the poolside toward a painted cobalt-blue wooden diamond-lattice fence, passing directly under the blue arched wooden garden gate into a sunny Tunisian courtyard with white marble stepping stones, green grass trim, natural pebble soil, and young unpotted Mediterranean olive trees swaying gently in natural daylight. Strictly preserve input geometry and camera movement.
```

### Clip 03 — `03_Enter_Front_Terrace_And_Main_Door.mp4` (`19.5s – 29.0s`)
```text
Photorealistic live-action first-person POV video strolling past young olive trees and an outdoor covered stone BBQ grill with light charcoal smoke, stepping through a whitewashed Tunisian welcome arch onto a stone terrace, and walking through double cobalt-blue arched wooden doors opening inward into a bright luxury marble villa interior. Strictly preserve input geometry and camera movement.
```

### Clip 04 — `04_Enter_Kitchen_And_Hammam_Bathroom.mp4` (`29.0s – 39.5s`)
```text
Photorealistic live-action first-person POV video walking across polished cream Carthage marble floors into a luxury Tunisian chef's kitchen with dark walnut cabinets, blue-and-white Zellige tile backsplash, marble L-countertop, brass pots on the stove, and barstools, then walking through an open blue arched wooden door into a bright Hammam bathroom with glass walk-in rain shower and walnut brass vanity. Strictly preserve input geometry and camera movement.
```

### Clip 05 — `05_Exit_Bathroom_Lie_On_Bed_Ceiling.mp4` (`39.5s – 50.5s`)
```text
Photorealistic live-action first-person POV video panning across a luxury Tunisian Hammam bathroom with Zellige mosaic floor tiles and white porcelain toilet, walking back out into the sunlit villa hallway toward the master bedroom with a carved dark mahogany king bed and Kairouan rug, and lying down on the bed gazing up at the plastered ceiling and glowing brass crystal chandelier. Strictly preserve input geometry and camera movement.
```

### Clip 06 — `06_Stand_From_Bed_Sit_On_Sofa_Watch_TV.mp4` (`50.5s – 62.2s`)
```text
Photorealistic live-action first-person POV video rising from a carved king bed in a sunlit Tunisian bedroom, walking across polished marble floors into a grand Majlis living salon with blue Zellige wall arches, ornate chandeliers, Berber carpet, and carved sofas, then sitting down on the sofa facing a wall-mounted flatscreen TV playing a live Tunisian news broadcast. Strictly preserve input geometry and camera movement.
```

### Clip 07 — `07_Exit_House_Circle_To_Blue_Stairs.mp4` (`62.2s – 75.2s`)
```text
Photorealistic live-action first-person POV video standing up from the living room sofa after watching TV, walking out through the open cobalt-blue arched front doors onto the sunlit Tunisian villa terrace, and circling to the west exterior wall at the base of a whitewashed and Sidi Bou Said blue diagonal outdoor staircase. Strictly preserve input geometry and camera movement.
```

### Clip 08 — `08_Climb_Stairs_Sit_On_Rooftop_Sofa.mp4` (`75.2s – 86.5s`)
```text
Photorealistic live-action first-person POV video climbing up exterior whitewashed masonry stairs with painted Sidi Bou Said blue treads and handrail under a crisp blue sky, stepping onto a spacious sunlit Mediterranean rooftop terrace with stone BBQ bar and blue wooden pergola, and sitting down on a traditional Tunisian low floor sofa with woven kilim rug and marble tea table. Strictly preserve input geometry and camera movement.
```

### Clip 09 — `09_Stand_Rooftop_Look_Down_At_Livestock.mp4` (`86.5s – 96.5s`)
```text
Photorealistic live-action first-person POV video standing up from a Tunisian rooftop floor lounge under a blue wooden pergola, walking to the whitewashed east rooftop parapet wall, and looking down into a real sunlit farm paddock enclosed by a white wall and blue wooden lattice fence where live white goats, chickens, and rabbits roam on natural pebble soil. Strictly preserve input geometry and camera movement.
```

### Clip 10 — `10_Rooftop_Panorama_Around_Entire_Villa.mp4` (`96.5s – 105.0s`)
```text
Photorealistic live-action first-person POV video walking along the sunlit whitewashed rooftop terrace parapet of a Sidi Bou Said Tunisian villa, sweeping panoramically across the surrounding countryside estate: olive tree groves, grapevine pergola, glowing stone bonfire, blue tractor, turquoise swimming pool, giant green shade tree, country gravel road, and parked orange hatchback car under natural Mediterranean daylight. Strictly preserve input geometry and camera movement.
```
