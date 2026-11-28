# Proof Log — LaTeX edition

Typeset LaTeX rendering of the running research bitácora `../00-PROOF-LOG.md`
(Days 0–46 of the Riemann program).

- `PROOF-LOG.tex` — the LaTeX source (auto-generated, faithful to the .md).
- `PROOF-LOG.pdf` — compiled, 88 pages.
- `build_proof_log_tex.py` — the converter (markdown → LaTeX; no pandoc needed).

**Rebuild:** `python3 build_proof_log_tex.py && pdflatex PROOF-LOG.tex` (twice).

The `.md` remains the canonical, append-only diary; this LaTeX edition is a
regenerable typeset mirror. To refresh after new `.md` entries, just re-run the
build script.
