# Round 11 B — Is the high-block gauge quotient K-uniform? A resolution-controlled decision test

Labels: everything in this memo is NUMERICAL unless stated otherwise. Nothing here is used in a proof.

## 0. Corpus check
Object and tool are those of ROUND_010_A §2.2–2.3 (consistent gauge quotient on admissible prolate data,
tools/prolate_gauge_adm.py). What changes: the Galerkin dimension Nb is raised to ≈ 2.5·K so that every reported
index k sits below the measured resolution cap k_* ≈ 0.4·Nb, and each K is evaluated at several Nb to give an error
bar. This is the step named in ROUND_010_A "Next concrete step"; it is a measurement, not a retried route.

## 1. Setup
T ∈ {0.8, 1.0} (4N = 19.8, 29.6). Runs: sine dimension Nb, working digits dps = 30 (reduced from 40 for time; the
quantities measured are O(1) ratios and λ_A ≥ 10⁻²³, far above the 10⁻⁵⁰ floor at dps 30), high block capped at
KTOP = 0.4·Nb. Quantities: α_HI(K) (all even k, and ℱ-class +1 alone), Γ′(K) in the ℓ_g metric, the two-block Schur
bound and θ_K = (2×2 bound)·μ/λ_A, and the Ritz bottom inf W/‖Ef‖² ÷ λ_A on the same span.

## 2. Run log (appended as runs finish)

Timings (one core per run): Galerkin build Nb = 200 at dps 30: 247 s; prolate sector Nb = 200, KMAX = 80: 64 s; the
gauge/Schur tool at Nb = 200: < 15 min. A build at Nb = 445 (needed for K = 6·4N at T = 1.0) was projected at > 30 min
and was stopped; that point is not reported.

### 2.1 T = 0.8, Nb = 200, KTOP = 80 (k_* ≈ 0.4·Nb = 80)
α_HI (all even k): 2.06 (30), 1.46 (40), 1.15 (50), 1.01 (60), 0.94 (64), 0.82 (70), 0.80 (74), 0.76 (80).
α_HI·K/4N: 3.1 (30), 2.94 (40), 2.89 (50), 3.06 (60), 2.90 (70), 3.08 (80).
Class +1 alone: 2.09 (40), 2.04 (52), 2.02 (60), 2.01 (72), 1.92 (80).
Falsifiers at the same Nb: 1.01Λ: α_HI(80) = 0.765 (Λ: 0.764), class +1 1.906; global inf W/ℓ_g ≈ −2.7·10⁸ (rejected,
low block). a_3: α_HI(80) = 0.601, class +1 2.66; global ≈ −2.8·10⁷ (rejected, low block).
Global inf W/ℓ_g (Λ) drops from 0.80 (k ≤ 72) to 0.47 (k ≤ 80): the last four indices sit at the resolution cap.

### 2.2 Tool changes (documented; values unchanged)
tools/prolate_gauge_adm.py gained three environment switches. FASTMUL=1 forms V^T(Arch − Π_w)V and V^TV in python-flint at
the same working precision (checked: the Nb = 200, T = 0.8 run reproduces the mpmath run digit for digit). LAMA=<value>
supplies the Galerkin λ_A from a smaller-Nb run (5.8443·10⁻¹² at T = 0.8, Nb = 200; 1.47·10⁻²³ at T = 1.0, Nb = 220,
ROUND_010_A); the full mp eigensolve at Nb ≥ 250 does not fit the budget; λ_A enters only the normalisation of the last two
Schur columns. STEP=s evaluates every s-th index of the scans. Builds: Nb = 250/300 (T = 0.8) 365/524 s, Nb = 300/370
(T = 1.0) 531/755 s; Nb = 445 (T = 1.0) did not finish in 900 s: K = 4·4N at T = 1.0 is out of reach this round.

### 2.3 Resolution cap re-measured (important)
The cap is not 0.4·Nb at larger Nb. Global inf W/ℓ_g on the admissible span collapses at k ≈ 88–96 for Nb = 250
(0.77 → 0.10), at k ≈ 96 for Nb = 300 at T = 0.8 (0.76 → 0.11), at k ≈ 90–96 for Nb = 300 at T = 1.0 (0.95 → 0.39) and at
k ≈ 100 for Nb = 370 (0.97 → 0.77). So k_* ≈ 0.32·Nb–0.35·Nb here, and the resolved K range is K ≤ 4.5·4N (T = 0.8) and
K ≤ 3.3·4N (T = 1.0). Points past k_* are discarded below.

### 2.4 α_HI(K) across Nb (all even k, Λ)  — the error bar is the spread over Nb
| T | K | K/4N | Nb = 160/220 (ROUND_010_A) | Nb = 200 | Nb = 250 | Nb = 300 | Nb = 370 |
|---|---|---|---|---|---|---|---|
| 0.8 | 40 | 2.02 | 1.41 | 1.458 | 1.468 | 1.469 | — |
| 0.8 | 60 | 3.03 | 0.87 | 1.012 | 1.052 | 1.053 | — |
| 0.8 | 70 | 3.53 | — | 0.822 | 0.857 | 0.872 | — |
| 0.8 | 80 | 4.04 | — | 0.764 | 0.814 | 0.838 | — |
| 0.8 | 88 | 4.44 | — | — | 0.762 | 0.799 | — |
| 1.0 | 40 | 1.35 | 3.09 (220) | — | — | 3.17 | 3.15 |
| 1.0 | 60 | 2.03 | 1.52 (220) | — | — | 1.583 | 1.726 |
| 1.0 | 72 | 2.44 | — | — | — | 1.229 | 1.326 |
| 1.0 | 80 | 2.71 | 1.05 (220) | — | — | 1.124 | 1.203 |
| 1.0 | 88 | 2.98 | — | — | — | 1.023 | 1.092 |
| 1.0 | 96 | 3.25 | — | — | — | (0.73, past cap) | 1.013 |
Reading. α_HI at fixed K INCREASES with Nb and converges from below (T = 0.8: K = 60 settles at 1.05 by Nb = 250; K = 80
moves 0.764 → 0.814 → 0.838; T = 1.0: K = 60 moves 1.52 → 1.58 → 1.73, not yet settled at Nb = 370). Every value at
the top of a run is an under-estimate; the ROUND_010_A product α_HI·K/4N ≈ 2.6–3.0 was biased low by this.
Falsifiers at T = 0.8, Nb = 250, K = 80 = 4.04·4N: α_HI = 0.814 (Λ), 0.814 (1.01Λ, Δ < 0.1%), class +1 1.906 / 1.906;
a_3: class +1 2.654; global inf W/ℓ_g ≈ −2.0·10⁸ (1.01Λ), −1.7·10⁷ (a_3).
Correction to the falsifier line above: under a_3 at the same point α_HI (all even k) = 0.614, class +1 2.654.

### 2.5 Fits of α_HI(K), x = K/4N (weights = Nb spread, floor 0.01; resolved points only)
T = 0.8 (x = 2.0–4.4, Nb = 300 values, error = |Nb300 − Nb250|):
| model | parameters | χ²/dof |
|---|---|---|
| c/x | c = 3.04 ± 0.01 | 13.6 |
| a + b/x | a = 0.17 ± 0.02, b = 2.60 ± 0.06 | 5.9 |
| c·x^{−p} | c = 2.65 ± 0.05, p = 0.85 ± 0.02 | 6.4 |
α_HI·x: 2.97, 3.00, 2.94, 3.19, 3.20, 3.08, 3.30, 3.38, 3.55 (x = 2.0 → 4.4): the product rises; since every top value is
still converging upward in Nb, the rise is if anything understated.
T = 1.0 (x = 1.6–3.25, Nb = 370 values, error = |Nb370 − Nb300|):
| model | parameters | χ²/dof |
|---|---|---|
| c/x | c = 3.43 ± 0.06 | 0.73 |
| a + b/x | a = −0.21 ± 0.11, b = 3.85 ± 0.23 | 0.14 |
| c·x^{−p} | c = 3.77 ± 0.19, p = 1.14 ± 0.07 | 0.09 |
α_HI·x: 3.53, 3.44, 3.30, 3.23, 3.26, 3.25, 3.29 (x = 1.6 → 3.25): flat at ≈ 3.27 past x ≈ 2.2.
Class +1 alone (both T, all Nb): flat — 2.10 → 1.90 (T = 0.8, k ≤ 92), 3.30 → 2.91 (T = 1.0, k ≤ 100). The K-decrease is
entirely the ℱ-class mixing above the plunge, as in ROUND_010_A.

### 2.6 Two-block Schur (Λ), resolved spans; Γ′ is converged in Nb to ≈ 1%
| T | Nb | K (K/4N) | α_HI | Γ′ | Γ′²/(κ_LMα_HI) | 2×2 bound | true inf W/ℓ_g | θ_K | Ritz inf W/‖Ef‖² ÷ λ_A |
|---|---|---|---|---|---|---|---|---|---|
| 0.8 (κ_LM 2.12) | 300 | 30 (1.5) | 2.05 | 0.31 | 0.022 | 1.77 | 1.89 | 0.87 | 1.46 |
| | 300 | 46 (2.3) | 1.29 | 0.81 | 0.24 | 0.79 | 1.28 | 0.39 | 1.41 |
| | 300 | 62 (3.1) | 1.02 | 1.04 | 0.50 | 0.40 | 1.02 | 0.20 | 1.35 |
| | 300 | 78 (3.9) | 0.84 | 1.17 | 0.76 | 0.15 | 0.84 | 0.073 | 1.33 |
| | 250 | 84 (4.2) | 0.80 | 1.22 | 0.88 | 0.071 | 0.80 | 0.035 | 1.33 |
| | 300 | 92 (4.6)* | 0.79 | 1.31 | 1.02 | −0.010 | 0.79 | −0.005 | 1.31 |
| 1.0 (κ_LM 3.12) | 370 | 40 (1.35) | 3.15 | 0.45 | 0.021 | 2.69 | 2.95 | 0.88 | 1.52 |
| | 370 | 56 (1.9) | 1.82 | 1.19 | 0.25 | 1.11 | 1.80 | 0.36 | 1.50 |
| | 370 | 72 (2.4) | 1.33 | 1.59 | 0.61 | 0.39 | 1.32 | 0.13 | 1.47 |
| | 370 | 88 (3.0) | 1.09 | 1.73 | 0.88 | 0.10 | 1.09 | 0.033 | 1.45 |
| | 370 | 100 (3.4)* | 0.98 | 1.74 | 0.996 | 0.003 | 0.97 | 0.001 | 1.41 |
(* within 5% of the measured cap; the trend of Γ′²/(κ_LMα_HI) through the resolved points already reaches 0.88 and
extrapolates to 1 at K ≈ 4.5·4N (T = 0.8) and ≈ 3.3·4N (T = 1.0) without these points.)
Readings. (i) θ_K is not K-uniform: it falls monotonically and reaches 0 (T = 0.8, K ≈ 4.6·4N; T = 1.0, K ≈ 3.4·4N).
(ii) The loss is the coupling: Γ′ is still growing at T = 0.8 (1.04 → 1.31) and flattens near 1.74 at T = 1.0, while
α_HI keeps decreasing, so Γ′²/(κ_LMα_HI) crosses 1. (iii) Positivity itself is not lost: the true infimum of W/ℓ_g on
LM_adm ⊕ HI_adm equals α_HI to two digits at every K, and the Ritz bottom on the span stays 1.31–1.52 λ_A, decreasing
by ≈ 10% over the whole range. The two-block Schur bound becomes useless while the form stays positive: the decoupling
inequality, not the sign, is what fails.

### 2.7 Falsifiers at K ≈ 4·4N
T = 0.8, K = 80 (4.04·4N), Nb = 300: α_HI = 0.838 (Λ), 0.838 (1.01Λ), 0.622 (a_3); class +1 1.92 (Λ, 1.01Λ), 2.69 (a_3);
global inf W/ℓ_g = −2.7·10⁸ (1.01Λ), −2.8·10⁷ (a_3). T = 1.0, K = 100 (3.4·4N; 4·4N not reachable), Nb = 370: α_HI = 0.978
(Λ), 0.979 (1.01Λ), 0.793 (a_3); class +1 2.91 / 2.87 / 4.56; global −7.6·10¹⁹ (1.01Λ), −2.8·10²¹ (a_3). As in ROUND_010_A:
the high block does not see 1.01Λ (Δ < 0.1%); a_3 lowers the all-k α_HI by 20–25% (new at these K; at K ≤ 60 it raised
it) and raises class +1; every falsifier is rejected only through the low block.

## 3. Decision
(HR)(a). The data do NOT support a K-uniform positive α_HI established numerically, and do not cleanly support pure
4N/K decay either. At T = 1.0 the resolved data (x ≤ 3.25) are fitted by c/x with c = 3.43 ± 0.06 (χ²/dof 0.7) and the
positive-limit model returns a = −0.21 ± 0.11; at T = 0.8, where the range is longer (x ≤ 4.4) and better converged, the
product α_HI·x rises from 2.95 to 3.55 and the floor model returns a = 0.17 ± 0.02, exponent p = 0.85 ± 0.02. The honest
reading: α_HI decays at least like a power x^{−0.85…−1.14} on the resolved range; a positive limit, if any, is ≤ ≈ 0.2
(T = 0.8) and not seen at T = 1.0. For any proof plan this means (HR)(a) must be stated with a K-dependent normalisation
(α_HI ≳ c·4N/K is consistent with every point at both T: min α_HI·x = 2.94 at T = 0.8, 3.23 at T = 1.0), not as a
uniform constant. The class +1 part is uniform (≈ 1.9 and ≈ 2.9): the decay is the class mixing.
θ_K. The two-block Schur bound does not stay positive with a K-uniform constant: θ_K → 0 at K ≈ 4.5·4N (T = 0.8) and
≈ 3.3·4N (T = 1.0), driven by Γ′²/(κ_LMα_HI) → 1, while the true infimum and the Ritz bottom (≈ 1.3–1.5 λ_A) stay
positive and nearly flat. The 2×2 decoupling is the wrong assembly beyond ≈ 3–4·4N.

## Result
NO-GO (class: two-block LM/HI Schur assembly with block-diagonal ℓ_g normalisation, NUMERICAL) for K-uniform θ_K;
(HR)(a) as a K-uniform statement is not supported (decay ≥ x^{−0.85}; K-dependent normalisation α_HI ≳ 3·4N/K fits all
resolved data).

### What was proved
Nothing new is PROVED here. NUMERICAL: Tables 2.4–2.7; resolution cap k_* ≈ 0.32–0.35·Nb at Nb = 250–370 (not 0.4·Nb);
α_HI converges from below in Nb (ROUND_010_A products were biased low); Γ′ converged in Nb to ≈ 1%.

### What failed and why
- K-uniform θ_K: Γ′²/(κ_LMα_HI) reaches 1.02 (T = 0.8, K = 92) and 0.996 (T = 1.0, K = 100); the bound goes to zero
  while the form stays positive (true inf = α_HI, Ritz ≈ 1.3–1.4 λ_A).
- Uniform (HR)(a): α_HI(K) keeps decreasing; positive-limit fits give 0.17 ± 0.02 (T = 0.8) and −0.21 ± 0.11 (T = 1.0).
- Reach: K = 5–6·4N at T = 1.0 needs Nb ≥ 450 (build > 15 min at dps 30); K = 6·4N at T = 0.8 needs Nb ≈ 350–380.

### Next concrete step
Replace the two-block Schur by a three-block (or banded) assembly in which the high block is split at the class level:
class +1 (flat α ≈ 2–3) separated from class −1 above the plunge, with the coupling measured per class pair; test
whether the class −1 high part carries both the 4N/K decay and the growth of Γ′. In parallel, state (HR)(a) with the
normalisation α_HI ≥ c·4N/K and check what the assembly then requires of the coupling (Γ′² ≲ κ_LM·c·4N/K).

## Reproducibility
tools/prolate_sector.py T Nb 30 KMAX; FASTMUL=1 LAMA=<λ_A> KTOP=<cap> STEP=<s> tools/prolate_gauge_adm.py T Nb 30 KMAX 12 [w].
Runs: (0.8; Nb 200/250/300; KMAX 80/100/120; KTOP 80/84–100/80–96), (1.0; Nb 300/370; KMAX 120/148; KTOP 88–120/100–148);
w ∈ {L, 1.01, a3}; each ≤ 900 s (several full-step scans were cut at 900 s and their values past k_* discarded).
