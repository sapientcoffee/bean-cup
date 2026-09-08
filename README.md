# 🍵 Bean-Cup

> Unified Visual Dashboard, Interactive Kanban Tracker, and Workflow State Scanner for Antigravity SDLC pipelines.

## 🚀 Features

- **Dynamic State Scanner:** Inspects any `plans/` directory, checks artifact presence across Stages 0–8, parses task checklists in `05_PLAN.md`, and computes the "What's Next" step.
- **Unified Visual Dashboard:** Rich single-file HTML dashboard (`visual-dashboard.html`) containing Discovery, Glossary, PRD, Technical Spec, Kanban, Test Verification, and Walkthrough tabs.
- **Local Dashboard Server:** Run `python3 bean_cup.py serve --plan-dir plans/my-feature/timestamp` to view the live dashboard in your browser.
- **Artifact Dual-Write:** Mirrors updates directly to the Antigravity Brain artifacts viewer.

## 📦 Installation

```bash
# Workspace local
./install.sh

# Or global install via agy
agy plugin install .
```

## 🛠️ Usage

```bash
# Scan a plan directory and report "What's Next"
python3 bean_cup.py scan --plan-dir plans/my-feature/2026-08-11_1230

# Serve the visual dashboard locally on port 8080
python3 bean_cup.py serve --plan-dir plans/my-feature/2026-08-11_1230

# Auto-sync all stage markdown files into visual-dashboard.html
python3 bean_cup.py auto-sync --plan-dir plans/my-feature/2026-08-11_1230 --moniker my-feature
```

## 📜 License
Apache-2.0 - Copyright 2026 Google LLC.
