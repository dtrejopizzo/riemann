# 06-grafico — Visualization and sonification

Exploratory visual and audio material from July 2026, produced alongside the research phases
but not itself part of the numbered phase sequence (`03-research/phase-*`). **Nothing here is a
result** — no file in this folder proves, refutes, or advances any claim about RH. It exists to
make the corpus's ideas visible and audible: spectral plots of the zeros, a sonification of their
gaps, and one design note on a candidate Hilbert–Pólya operator.

## Contents

| File(s) | What it is |
|---|---|
| `DISENO_OPERADOR.md` | Design note on the Bender–Brody–Müller candidate operator `H` for Hilbert–Pólya. States plainly what BBM built and what remains unsolved: proving `H`'s spectrum is real (`= RH`). Not a route the program pursued further — see `NO-GO-LIST.md` §MW-4 (Arc B, Hilbert–Pólya) for why this family of approaches stalls, and `MASTER-PLAN.md` Part 1B / `OPTIONS.md` for what remains genuinely open instead. |
| `berry_keating_xp.py` / `.png` | The Berry–Keating `xp` semiclassical heuristic, visualized. |
| `barkhausen_riemann.py`, `zeta_barkhausen*.py`, `espectro_ceros.py`, `espec_*.png` | Treats the zero sequence as a signal; FFT/wavelet analysis and an audio rendering (`ceros.wav`) of the zero spacings — a "sound of the primes" illustration. |
| `formula_explicita.py` | Visualizes the explicit formula (primes ↔ zeros as Fourier duals) — see `EXPLANATION.md` Layer 2 for the plain-language version of what this plot shows. |
| `positividad_li.py`, `oleaje_rigidez.py`, `rigidez.py`, `rebotes.py` | Illustrations of Li-coefficient positivity, spectral rigidity (GUE statistics), and pair-repulsion of the zeros. |
| `pi_vs_li.py`, `primos_predicen_ceros.py`, `ceros_vs_pares_plano.py` | Prime-counting vs. the explicit-formula approximation; how primes constrain zero locations. |
| `sucesiones*.py` | Sequence/statistics exploration scripts (early, exploratory). |
| `porque_offline.py`, `por_que_no_alcanza.py`, `factor_forma.py`, `gue_no_es_unico.py`, `selector_weil.py`, `calcular_ceros.py`, `analisis_espectral.py` | Assorted supporting scripts for the plots above and for the explicit-formula/Weil-selector illustrations. |
| `paper.tex` / `paper.pdf` | A standalone write-up of this visualization set. **Not part of the `04-papers/` publishable corpus** — it was not numbered, indexed, or carried into `04-papers/README.md`, and should not be cited as one of the program's papers. |
| `zeros_10000.txt` | The first 10,000 nontrivial zeros of ζ, used by the scripts above. |

## Status

Illustrative only. For the actual research record, see `03-research/`; for the publishable
results, see `04-papers/README.md`; for what is currently open, see `OPTIONS.md`.
