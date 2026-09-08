# 🍵 BEAN-CUP: VISUAL DASHBOARD & WORKFLOW TRACKER

Bean-Cup is a standalone tracking, visual dashboard, and state scanning plugin for the Antigravity CLI (`agy`).

## Capabilities
1. **Dynamic Stage Scanner:** Inspects `./plans/<feature>/<timestamp>/` to infer current SDLC stage, parse `05_PLAN.md` tasks, and report actionable "What's Next" recommendations.
2. **Unified Visual Dashboard:** Serves and manages `visual-dashboard.html` with tabs for Discovery, Glossary, PRD, Specs, Kanban, Verification, and Walkthrough.
3. **Local Web Server:** Serves `visual-dashboard.html` on `http://localhost:8080/` via `python3 bean_cup.py serve`.
4. **Dual-Write Artifact Mirroring:** Automatically syncs dashboard artifacts to `00_visual-dashboard.html` inside the AGY brain directory for instant UI viewing.
