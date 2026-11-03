# INSTRUCTIONS FOR ALL AI AGENTS (MAÎTRE MAHER TUNISIA VILLA 3D PROJECT)

> **CRITICAL REQUIREMENT AT CONVERSATION START:**
> Every time you start a conversation or receive a task in this workspace, you **MUST IMMEDIATELY READ** the master brain and technical specification file:
> 📄 [PLAN_MAITRE_MAHER_HOUSE_3D.md](file:///Users/dianjulie/Documents/maitremaherhouse/PLAN_MAITRE_MAHER_HOUSE_3D.md)

---

## 1. Strict Visual Quality & Anti-Cartoon Mandate (NON-NEGOTIABLE)
* **AAA Realistic 3D Quality Only:** The user strictly expects realistic, high-contrast 3D architectural visualization powered by real Poly Haven GLTF 3D models (`PH_MANIFEST`), 1K PBR textures (`plastered_wall_04`, `wood_table_worn`, `large_floor_tiles_02`, procedural Carthage marble & Zellige normal/roughness maps), HDRI environment reflections (`scene.environment`), and ACES Filmic + AgX contrast post-processing (`AgxContrastShader`).
* **Never Downgrade Existing Visuals:** What is currently implemented in `Tunisia_Arab_House_Designer.html` is the locked baseline quality. **NEVER** strip out PBR textures, replace GLTF models with cartoon boxes, or flatten lighting/contrast.
* **Always Verify in a Real Browser:** Never rely only on `node --check`. Always verify runtime execution and visual rendering in a browser before concluding a task.

## 2. File Sync & Git Tracking Rule (MANDATORY)
* **Primary Files:** `/Users/dianjulie/Documents/maitremaherhouse/Tunisia_Arab_House_Designer.html` and `/Users/dianjulie/Documents/maitremaherhouse/index.html`.
* **Sync Rule:** Whenever you edit `Tunisia_Arab_House_Designer.html`, always copy it to `index.html` (`cp Tunisia_Arab_House_Designer.html index.html`).
* **GitHub Repository:** `https://github.com/Laksma123/maitremaherhouse`
* **Rule:** Always commit and push changes (`git add`, `git commit`, `git push`) to `https://github.com/Laksma123/maitremaherhouse` after every completed milestone.
