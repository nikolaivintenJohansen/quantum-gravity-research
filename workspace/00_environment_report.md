# Environment report

Checked: 2026-08-02T15:44:47-04:00 (America/Detroit)

## Host and repository

- Host OS: macOS 26.5.1 (build 25F80), arm64.
- Repository: Git repository on branch `main`, with no commits at preflight time.
- Git: 2.50.1 (Apple Git-155).
- The pre-existing `AGENTS.md` is untracked and was not modified.

## Wolfram

- Local CLI check: `wolframscript -version` returned exit code 127 (`command not found`).
- Connected Wolfram MCP kernel: reachable and licensed.
- Kernel: Wolfram Language 15.0.0 for Linux x86-64, dated May 6, 2026; `$SystemID` is `Linux-x86-64`.
- Smoke test: `FullSimplify[D[x^3, x] - 3 x^2]` returned `0`; `Det[{{1,2},{3,4}}]` returned `-2`.
- Saved source and result: [`wolfram-notebooks/00_environment_smoke.wl`](../wolfram-notebooks/00_environment_smoke.wl) and [`results/00_environment_wolfram.json`](../results/00_environment_wolfram.json).
- Operational consequence: Wolfram checks must use the connected stateless kernel, so every evaluation must be self-contained. A local `.wl` source file will be saved for every material symbolic result. If that kernel becomes unavailable or a check cannot fit the stateless execution model, the relevant log must explicitly mark the cross-check as pending.

## Python

- System `python3`: CPython 3.9.6; the required scientific packages were absent.
- Selected reproducible runtime: bundled CPython 3.12.13 at `/Users/nikolaivintenjohansen/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`.
- Isolated environment: `python-code/.venv`.
- Direct pins: [`python-code/requirements.txt`](../python-code/requirements.txt).
- Full transitive lock: [`python-code/requirements-lock.txt`](../python-code/requirements-lock.txt).
- Required packages installed and import-tested: NumPy 2.5.1, SciPy 1.18.0, SymPy 1.14.0, Matplotlib 3.11.1, NetworkX 3.6.1, pandas 3.0.5, and pytest 9.1.1.
- Symbolic smoke test: `simplify(diff(x**3, x) - 3*x**2)` returned `0`.
- Saved verification source and result: [`python-code/verify_environment.py`](../python-code/verify_environment.py) and [`results/00_environment_python.json`](../results/00_environment_python.json).
- Matplotlib must use the writable cache `python-code/.mplconfig` in sandboxed runs. Set `MPLCONFIGDIR` to its absolute path when executing plotting code.

Recreate the Python environment from the repository root:

```bash
/Users/nikolaivintenjohansen/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -m venv python-code/.venv
python-code/.venv/bin/python -m pip install -r python-code/requirements.txt
```

## Literature and network access

- Outbound web access: available through the research web connector.
- arXiv reachability: confirmed on 2026-08-02 by retrieving search results and metadata from `arxiv.org`, including arXiv:1903.11544.
- The bundled arXiv skill instructions are installed, but no arXiv MCP methods are exposed in this session. Literature retrieval will therefore use direct arXiv pages and primary publisher/authoritative sources through the web connector. This limitation must be rechecked in a future session.
- The connected Wolfram service is available for computation but is not a substitute for primary-literature verification.

## Reproducibility policy for this workspace

- Save Python source under `python-code/`, Wolfram source under `wolfram-notebooks/`, raw/derived data under `data/`, and material outputs under `results/`.
- The phase workspace under `workspace/` stores comparisons, model logs, provenance, references, and reports. Model `code/` directories should point to canonical source paths rather than duplicate code.
- Every numerical run must record its command, package environment, parameters, units, assumptions, seed (if any), and validation checks.
- Raw source data are immutable. Transformations create documented derived files.
- No terminal-only calculation is a final result.

## Preflight status

The environment is ready for the framework-comparison phase. Wolfram and Python smoke tests passed, and verified literature access is available. Recheck this report briefly at the start of each new session.
