# 🎬 Panduan & Prompt Khusus Google Flow (`Start Frame + End Frame`)
**100% Konsistensi Ruang Tanpa Halusinasi (19 Foto Berantai = 18 Klip Mulus)**

> [!IMPORTANT]
> ### Mengapa Prompt Ini Berbeda dari Versi 1-Gambar?
> Pada fitur **Frames to Video (`Start Frame + End Frame`)** di Google Flow, AI **sudah melihat** isi foto awal dan foto tujuan akhir.
> * Jika menggunakan *prompt* lama (yang mendeskripsikan ulang seluruh perabot atau menyuruh dua aksi bolak-balik), AI justru bingung dan membuat efek **meleleh (*crossfade PowerPoint*)**.
> * Seluruh *prompt* di bawah ini dirancang khusus sebagai **Motion-Bridge Prompt** (hanya mendeskripsikan **lintasan jalan kaki, arah belokan kepala, dan gerak tubuh fisik** yang menjembatani `Start Frame` tepat menuju `End Frame` dengan paralaks kamera 3D nyata).
> * Kami juga menambahkan **5 Foto Jembatan (`05B`, `07B`, `09A`, `09B`, `10B`)** pada titik belokan tajam agar **tidak ada satu pun klip yang menembus tembok**.

---

## Cara Pakai di Google Flow (`labs.google/fx/tools/flow`)
1. Buka **https://labs.google/fx/tools/flow** menggunakan akun Google/Gemini Anda, lalu klik **New Project**.
2. Pada kotak kontrol bawah, ubah mode ke **Video** → pilih tab **Frames** (*Start & End Frames*), aspek rasio **16:9**, durasi **8s**.
3. Untuk setiap klip di bawah:
   * Masukkan file **`Start Frame`** ke kotak **`+ Add start frame`**.
   * Masukkan file **`End Frame`** ke kotak **`+ Add end frame`**.
   * *Copy-paste* **Prompt Jembatan Gerak** klip tersebut lalu klik **Generate**.
4. Gabungkan hasil `Klip 01` s/d `Klip 18` berurutan di editor video (CapCut / Premiere / iMovie)—karena `End Frame` Klip 1 adalah `Start Frame` Klip 2, sambungan antar klip akan menyatu seperti **satu rekaman *one-take walkthrough* tanpa putus**!

---

## Daftar 18 Klip Berantai (`Start Frame` → `End Frame`)

### Klip 01 — Turun dari Mobil Menuju Area Kolam Renang
* **Start Frame:** `01_Luar_Pagar_Turun_Mobil.jpg`
* **End Frame:** `02_Jalan_Melihat_Kolam_Renang.jpg`
* **Prompt Google Flow (Copy-Paste):**
```text
Continuous live-action first-person POV handheld shot in natural Mediterranean daylight, zero cuts or crossfades. Stepping away from beside the parked orange hatchback car in the foreground, walk steadily forward along the sunlit gravel path past the trunk of the giant green shade tree, approaching the white marble swimming pool deck and low poolside drink table ahead while keeping the whitewashed villa and blue diagonal staircase on the right. Natural human footstep cadence, subtle breeze in tree leaves, real-world parallax.
```

### Klip 02 — Dari Tepi Kolam Berbelok Menuju Gerbang Pagar Kayu Biru
* **Start Frame:** `02_Jalan_Melihat_Kolam_Renang.jpg`
* **End Frame:** `03_Masuk_Pagar_Biru_Sidi_Bou.jpg`
* **Prompt Google Flow (Copy-Paste):**
```text
Continuous live-action first-person POV handheld walking shot in natural Mediterranean daylight, zero cuts or crossfades. After admiring the turquoise swimming pool and drink table, smoothly turn the camera to the right past the corner of the pool deck and walk a few steps across the sunlit pebble ground to stand directly in front of the painted Sidi Bou Said blue wooden arched garden gate and diamond-lattice fence looking into the courtyard. Fluid physical camera rotation and natural footsteps.
```

### Klip 03 — Masuk Gerbang Biru & Jalan Melihat Pohon Olives Kecil
* **Start Frame:** `03_Masuk_Pagar_Biru_Sidi_Bou.jpg`
* **End Frame:** `04_Jalan_Lihat_Pohon_Olives_Kecil.jpg`
* **Prompt Google Flow (Copy-Paste):**
```text
Continuous live-action first-person POV walking shot in bright natural Tunisian sunlight, zero cuts or crossfades. Walk straight forward directly underneath the blue wooden arched garden gate, stepping past the white limestone pavers onto the sunlit gravel courtyard inside the yard, angling slightly right to stroll alongside the row of young unpotted olive trees inside the blue diamond-lattice fence while keeping the whitewashed guest cabin, orange tree, and blue grapevine pergola ahead. Smooth forward 3D camera parallax and gentle breeze on olive leaves.
```

### Klip 04 — Dari Kebun Olives Kecil Belok Kiri ke Terrace Depan
* **Start Frame:** `04_Jalan_Lihat_Pohon_Olives_Kecil.jpg`
* **End Frame:** `05_Masuk_Terrace_Depan_Rumah.jpg`
* **Prompt Google Flow (Copy-Paste):**
```text
Continuous live-action first-person POV walking shot in natural Mediterranean daylight, zero cuts or crossfades. From the sunlit courtyard beside the young olive trees, smoothly pan and turn left following the manicured green grass and white limestone stepping-stone walkway toward the main villa, walking right up to the whitewashed lime-plaster entrance arch framing the front stone terrace, smoking covered BBQ grill on the right, and open blue front door ahead. Natural handheld walking motion.
```

### Klip 05 — Melewati Terrace Depan, Masuk Pintu Utama & Menengok ke Dapur
* **Start Frame:** `05_Masuk_Terrace_Depan_Rumah.jpg`
* **End Frame:** `05B_Masuk_Pintu_Belok_Dapur.jpg`
* **Prompt Google Flow (Copy-Paste):**
```text
Continuous live-action first-person POV walking shot transitioning smoothly from bright outdoor Tunisian sunlight into soft sunlit villa interior, zero cuts or crossfades. Walk straight forward underneath the white terrace arch past the smoking BBQ grill, step up through the wide-open Sidi Bou Said blue arched front doors into the cool marble-floored house, take three steps inside, and turn smoothly to the left to face the dark-walnut L-shaped kitchen and breakfast barstools. Realistic camera exposure adaptation and fluid walking turn.
```

### Klip 06 — Melangkah Masuk ke Area Dapur & Pintu Toilet
* **Start Frame:** `05B_Masuk_Pintu_Belok_Dapur.jpg`
* **End Frame:** `06_Masuk_Rumah_Dan_Dapur.jpg`
* **Prompt Google Flow (Copy-Paste):**
```text
Continuous live-action first-person POV indoor walking shot in soft natural daylight, zero cuts or crossfades. Walk smoothly forward around the corner of the dark-walnut kitchen island into the kitchen workspace, turning slightly left to face the white range stove with gentle steam rising from the brass pot, the glossy blue Zellige star-tile backsplash, and the open Sidi Bou Said blue arched bathroom door on the right. Smooth handheld eye-level footsteps and natural parallax.
```

### Klip 07 — Dari Dapur Masuk ke Dalam Toilet / Kamar Mandi Hammam
* **Start Frame:** `06_Masuk_Rumah_Dan_Dapur.jpg`
* **End Frame:** `07_Masuk_Toilet_Hammam.jpg`
* **Prompt Google Flow (Copy-Paste):**
```text
Continuous live-action first-person POV indoor walking shot in soft natural daylight, zero cuts or crossfades. From the kitchen, angle smoothly toward the right and walk straight through the open Sidi Bou Said blue arched doorway into the luxury Tunisian Hammam bathroom, turning slightly left inside the doorway to reveal the dark walnut marble vanity, carved cream limestone arched glass walk-in rain shower, white porcelain toilet, and mosaic brick floor. Fluid doorway pass-through motion.
```

### Klip 08 — Keluar dari Toilet Menuju Kasur Kamar Tidur Utama
* **Start Frame:** `07_Masuk_Toilet_Hammam.jpg`
* **End Frame:** `07B_Keluar_Toilet_Lihat_Kasur.jpg`
* **Prompt Google Flow (Copy-Paste):**
```text
Continuous live-action first-person POV indoor walking shot in soft natural Tunisian daylight, zero cuts or crossfades. Smoothly turn around to the right to step back out through the bathroom doorway into the open marble-floored villa hall, walking a few steps past the white partition wall corner and turning left to look directly at the carved dark-mahogany four-poster king bed on the Berber carpet with its blue arched window and blue Zellige wall arch. Natural human walking turn.
```

### Klip 09 — Jalan ke Kasur Lalu Tiduran Melihat Lampu Gantung & Atap
* **Start Frame:** `07B_Keluar_Toilet_Lihat_Kasur.jpg`
* **End Frame:** `08_Tiduran_Kasur_Lihat_Atap.jpg`
* **Prompt Google Flow (Copy-Paste):**
```text
Continuous live-action first-person POV indoor shot in soft natural daylight, zero cuts or crossfades. Walk smoothly up to the side of the carved dark-mahogany king bed, sit down onto the soft rumpled white cotton duvet, and gently lie back onto the pillows at the head of the bed while tilting gaze diagonally upward toward the ornate pierced brass chandelier on the white plaster ceiling, keeping the carved mahogany footboard at the bottom of the view. Natural human reclining motion.
```

### Klip 10 — Bangun dari Kasur, Berdiri & Duduk di Sofa Melihat TV
* **Start Frame:** `08_Tiduran_Kasur_Lihat_Atap.jpg`
* **End Frame:** `09_Duduk_Sofa_Nonton_TV.jpg`
* **Prompt Google Flow (Copy-Paste):**
```text
Continuous live-action first-person POV indoor shot in natural Tunisian daylight, zero cuts or crossfades. Tilt gaze down, sit up and rise smoothly off the side of the mahogany bed, walk straight forward across the polished cream marble floor toward the sunlit living salon sofas ahead, step onto the woven Berber carpet, turn left, and lower smoothly down to sit comfortably on the sofa facing the dark coffee table and 85-inch OLED flatscreen TV airing live Tunisian news. Fluid human standing, walking, and sitting motion.
```

### Klip 11 — Menonton TV Sebentar, Bangun dari Sofa & Menghadap Pintu Keluar
* **Start Frame:** `09_Duduk_Sofa_Nonton_TV.jpg`
* **End Frame:** `09A_Bangun_Sofa_Hadap_Pintu_Depan.jpg`
* **Prompt Google Flow (Copy-Paste):**
```text
Continuous live-action first-person POV indoor shot in natural Tunisian daylight, zero cuts or crossfades. Watch the live Tunisian news broadcast on the wall-mounted TV for two seconds while seated, then lean slightly forward, push up smoothly to stand upright from the living room sofa, and turn right-around to face the wide-open Sidi Bou Said blue arched main entrance doors looking out onto the sunny stone terrace and olive trees. Natural human standing and turning movement.
```

### Klip 12 — Keluar Rumah & Memutar Lewat Teras Samping ke Kaki Tangga Biru
* **Start Frame:** `09A_Bangun_Sofa_Hadap_Pintu_Depan.jpg`
* **End Frame:** `09B_Memutar_Teras_Ke_Tangga_Biru.jpg`
* **Prompt Google Flow (Copy-Paste):**
```text
Continuous live-action first-person POV walking shot transitioning from the villa interior out into bright Mediterranean sunlight, zero cuts or crossfades. Walk forward out through the open Sidi Bou Said blue arched front doors onto the sunlit terrace, immediately turn right to stroll westward along the side terrace past the ancient olive tree and colorful floor cushions, revealing the swimming pool on the left and the white-and-blue exterior diagonal rooftop staircase straight ahead. Smooth handheld walking trajectory.
```

### Klip 13 — Melangkah ke Kaki Tangga & Mulai Menaiki Tangga Luar
* **Start Frame:** `09B_Memutar_Teras_Ke_Tangga_Biru.jpg`
* **End Frame:** `10_Keluar_Naik_Tangga_Rooftop.jpg`
* **Prompt Google Flow (Copy-Paste):**
```text
Continuous live-action first-person POV walking shot in crisp Mediterranean sunlight, zero cuts or crossfades. Walk forward from the side terrace right up to the foot of the whitewashed exterior diagonal staircase, turn slightly right to align with the painted Sidi Bou Said blue wooden stair treads and blue masonry handrail, and begin climbing steadily up the lower steps alongside the sunlit white stucco villa wall. Authentic upward footstep cadence.
```

### Klip 14 — Sampai di Puncak Tangga & Masuk ke Area Rooftop Atas
* **Start Frame:** `10_Keluar_Naik_Tangga_Rooftop.jpg`
* **End Frame:** `10B_Puncak_Tangga_Masuk_Rooftop.jpg`
* **Prompt Google Flow (Copy-Paste):**
```text
Continuous live-action first-person POV climbing shot in bright Mediterranean daylight, zero cuts or crossfades. Climb steadily up the remaining painted Sidi Bou Said blue exterior steps onto the top whitewashed landing, then turn 90 degrees right to step through the rooftop parapet opening onto the sunny stone-tiled rooftop terrace, revealing the blue Zellige BBQ bar counter on the left and the blue wooden pergola lounge ahead. Natural stair-climbing rhythm and smooth right turn.
```

### Klip 15 — Jalan Melintasi Rooftop & Duduk Santai di Sofa Rooftop Atas
* **Start Frame:** `10B_Puncak_Tangga_Masuk_Rooftop.jpg`
* **End Frame:** `11_Duduk_Sofa_Rooftop_Atas.jpg`
* **Prompt Google Flow (Copy-Paste):**
```text
Continuous live-action first-person POV walking shot in bright natural Tunisian sunlight, zero cuts or crossfades. Walk smoothly across the pale stone rooftop tiles past the blue Zellige BBQ bar counter into the dappled shade beneath the painted Sidi Bou Said blue wooden pergola, step onto the woven rug beside the crimson-and-emerald Tunisian floor cushions, turn around to face back toward the marble mint-tea table and Zellige BBQ bar, and lower down smoothly to sit on the low floor sofa. Authentic human walking and sitting motion.
```

### Klip 16 — Bangun dari Sofa Rooftop & Melihat ke Bawah ke Ternak Hewan
* **Start Frame:** `11_Duduk_Sofa_Rooftop_Atas.jpg`
* **End Frame:** `12_Rooftop_Lihat_Ternak_Hewan.jpg`
* **Prompt Google Flow (Copy-Paste):**
```text
Continuous live-action first-person POV shot on a sunlit Mediterranean rooftop, zero cuts or crossfades. Smoothly rise and stand up from the low Tunisian rooftop floor sofa beneath the blue wooden pergola, turn around to the right toward the whitewashed outer rooftop parapet wall just behind the pergola, walk two steps right up to the parapet edge, and tilt the camera downward over the white stucco wall to look down into the farm paddock where white goats, a white hen, and brown rabbits roam near the open blue barn doors. Fluid standing, turning, and downward tilt.
```

### Klip 17 — Mengangkat Pandangan & Melihat Sekeliling Sisi Timur (Kabin & Kebun Zaitun)
* **Start Frame:** `12_Rooftop_Lihat_Ternak_Hewan.jpg`
* **End Frame:** `13_Rooftop_Keliling_Timur_Kebun_Zaitun.jpg`
* **Prompt Google Flow (Copy-Paste):**
```text
Continuous live-action first-person POV rooftop shot in natural Mediterranean daylight, zero cuts or crossfades. From leaning over the parapet looking down at the farm animals, smoothly lift gaze upward and walk slowly to the right along the rooftop edge, panning across the whitewashed adjacent cabin roofs, the smoking outdoor BBQ grill canopy below, the Sidi Bou Said blue wooden fence, rows of silvery-green olive trees, the blue farm tractor, and rolling Tunisian hills on the horizon. Smooth cinematic walking pan.
```

### Klip 18 — Melihat Sekeliling Rumah Sisi Barat (Penutup: Pot, Pohon Rindang, Kolam & Mobil)
* **Start Frame:** `13_Rooftop_Keliling_Timur_Kebun_Zaitun.jpg`
* **End Frame:** `14_Rooftop_Keliling_Barat_Kolam_Mobil.jpg`
* **Prompt Google Flow (Copy-Paste):**
```text
Continuous live-action first-person POV panoramic rooftop closing shot in warm natural Mediterranean daylight, zero cuts or crossfades. Walk slowly westward across the sunny rooftop terrace while panning smoothly to the right, bringing into view the weathered terracotta potted plant beside the whitewashed parapet wall and looking down past the swaying branches of the giant green shade tree toward the sparkling turquoise swimming pool, poolside drink table, and parked metallic orange Peugeot hatchback on the country gravel road. Calm, steady cinematic finish.
```
