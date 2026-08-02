# Research log

This file is append-only. Timestamps use ISO 8601 with an explicit UTC offset.

## 2026-08-02T15:44:47-04:00 — Program initialization and preflight

### Tried

- Read and adopted the attached Quantum–Gravity Bridge Research Agent objective.
- Inspected the repository and preserved the pre-existing untracked `AGENTS.md`.
- Checked the local Wolfram CLI, the connected Wolfram kernel, system and bundled Python runtimes, required Python packages, Git, host OS, and outbound literature access.
- Created an isolated Python 3.12 environment and installed/froze the requested scientific stack.
- Ran independent elementary symbolic smoke tests in Wolfram Language and SymPy.

### Found

- No local `wolframscript` is available, but a stateless Wolfram Language 15.0.0 kernel is connected and passed the smoke test.
- The system Python was unsuitable; the workspace virtual environment is functional with exact dependency pins.
- Direct arXiv access works. The arXiv MCP skill is present but its MCP methods are not exposed, so direct primary-source retrieval is the documented fallback.

### Judgment calls

- Selected the bundled CPython 3.12.13 runtime over macOS system Python 3.9.6 because the former is current, isolated from the OS, and compatible with the installed scientific wheels.
- Kept canonical executable code in `python-code/` and `wolfram-notebooks/` to honor repository policy; `workspace/` will hold phase records and model-local provenance pointers.
- Will begin comparison with fixed, explicitly justified criteria and only choose toy models after comparison/ranking evidence is saved. This avoids prematurely favoring a framework.

### Next

- Retrieve a bounded set of load-bearing primary sources/reviews for each framework.
- Write the framework comparison with claim-level citations, obstacles, tractable toy models, and tests.
