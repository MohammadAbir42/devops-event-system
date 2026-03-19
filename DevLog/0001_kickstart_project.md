# Kickstarting DevOps Practice Project
**Date:** 2026-03-20

## Objective
Start the first DevOps project locally. Initial setup with version control, basic documentation, and ignoring unnecessary files.

## Steps Completed

**1. Initialized Git repository**

```bash
git init
```

**2. Created `.gitignore`**
- **Ignoring:**
  - Node.js: `node_modules/`
  - Python: `__pycache__/`, `.venv/`
  - IDEs: `.vscode/`, `.idea/`
  - OS: `.DS_Store`, `Thumbs.db`
- `.gitignore` ready for multi-language DevOps stack.

**3. Created `README.md`**
- Project description: purpose, goals, and expected outcomes.

**4. Created `/DevLog` folder**
- Purpose: document all steps, decisions, and lessons learned during project development.

## Next Steps
- Add basic project structure (Python API, Node.js service, Nginx, Prometheus, Grafana).
- Create Dockerfile and `docker-compose` for local testing.
- Start CI/CD workflow experimentation (GitHub Actions or local scripts).