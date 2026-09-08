# 🍵 Bean-Cup: Dashboard & Workflow Rules

Bean-Cup provides the unified visual dashboard, interactive Kanban board, and dynamic stage scanning capabilities across Antigravity SDLC workflows.

## 1. Unified Dashboard Lifecycle
* **Preserve and Update:** The `visual-dashboard.html` artifact retains all previously generated stage tabs (Discovery, Glossary, PRD, Extraction, Spec, Plan, Verification, Walkthrough) and updates only the active stage.
* **Dual-Write Guarantee:** All generated dashboards and markdown artifacts must be mirrored to the active AGY brain artifacts directory (`~/.gemini/antigravity-cli/brain/<conversation-id>/00_visual-dashboard.html`) for instant UI visibility.

## 2. Dynamic Workflow State Scanning
* When inspecting a feature plan directory, run `python3 bean_cup.py scan --plan-dir <dir>` to evaluate existing stage artifacts, compute slice completion percentages, and determine the exact recommended next step.
