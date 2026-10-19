# Validation

This folder holds the reproducibility notebook for the foundations layer. It reruns the core
numerical checks (engine output against tabulated zeta zeros) so that any reader can confirm the
base computations before relying on them in a research phase.

## Contents

- `reproducibility_notebook.ipynb` — Jupyter notebook that loads the zeros tables, runs the
  engine, and compares the results.

## Related folders

- [../engine/](../engine/) — the code being validated.
- [../zeros-data/](../zeros-data/) — the reference zero tables.
- [../README.md](../README.md) — overview of the foundations folder.
