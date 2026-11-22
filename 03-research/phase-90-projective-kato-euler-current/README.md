# Phase 90 - Projective Kato--Euler current

## 1. Objective

Replace the transported Feshbach eigenline by an exact spectral line of the
full inner matrix and expand its projective rotation current in the prime-cell
algebra.

## 2. Main reduction

For

```text
M_t=H_A^in-tH_P^in-mu_t I,                            (2.1)
```

the scalar derivative `-dot mu_t I` changes eigenvalues but has no
off-diagonal matrix element between orthogonal eigenvectors.  Hence it does
not rotate a simple spectral line.  The exact projective current is driven
only by `H_P^in`.

## 3. Work order

```text
E90.001  full spectral residue and projective dominance;
E90.002  exact prime-driven Kato current;
E90.003  prime-cell expansion of the base-point current;
E90.004  bilateral Euler-matching defect;
E90.005  comparison with the static Feshbach coordinate.
```

## Outcome

Closed; see [`PHASE_90_CLOSURE.md`](PHASE_90_CLOSURE.md) (“Prime-response localization”). No positivity statement toward Ω7 is proved here; the phase is an exact reduction.
Open items carried forward: DOM-M and matched-layer uniformity; complementary resolvent and profile nonvanishing; `PROJECTIVE-KATO-EULER`; RDI-ANCHOR and Omega7.

## Contents

- `E90_001_FULL_SPECTRAL_RESIDUE.md` — E90.001 - Full spectral residue
- `E90_002_PRIME_DRIVEN_KATO_CURRENT.md` — E90.002 - Exact prime-driven Kato current
- `E90_003_PRIME_CELL_EXPANSION.md` — E90.003 - Prime-cell expansion of the projective current
- `E90_004_BILATERAL_MATCHING_DEFECT.md` — E90.004 - Bilateral Euler-matching defect
- `E90_005_FESHBACH_FULL_LINE_COMPARISON.md` — E90.005 - Feshbach and full-line comparison
- `PHASE_90_CLOSURE.md` — Phase 90 closure - Prime-response localization

## Relation to other phases

Continues [`phase-89-projective-layer-rotation`](../phase-89-projective-layer-rotation/); its open target passes to [`phase-91-kato-coboundary-equivalence`](../phase-91-kato-coboundary-equivalence/). The chain of phases 80–101 is the finite real-rooted CCM route to Ω7 (the Li–Keiper positivity statement), opened in phases 71–79.
