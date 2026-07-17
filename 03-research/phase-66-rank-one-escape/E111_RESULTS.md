# E111 — the rank-one escape-norm detector (Phase 66, Deliverable D2)

**Status: DETECTOR / CRITERION, not a proof.** `mu_max_prim → 1` for zeta is
RH-consistent; it is not a proof of RH. Reproducible: `python3 E111_escape_norm.py`
(uses the phase-61 engine cache; builds for λ∈{8,10,12,14,16,18,20,22} are cached).

## What is measured

The rank-one escape wall (phase-64 `CONSTRUCTION-TW-canonical-system.md §5`):
`N(P) := ‖P_prim K_P P_prim‖` bounded ⟺ RH, with `P_prim = I − |H⟩⟨H|/⟨H,H⟩`
removing the single pole/degree direction H.

**Honest object.** A fully faithful `K_P = ∫ Y_P* dH_P Y_P` needs the canonical ODE
(transfer matrix Y_P), which the validated engine does NOT integrate. Per the task's
authorised fallback, E111 uses the **best validated proxy = the E101 object**: the
generalized spectrum `L_pr x = μ L_arch x` and its mass past the contractive edge μ=1
(L_arch = archimedean+pole cell; L_pr = von Mangoldt prime cell; windowed Fourier
basis, L = 2 log λ). E111 adds the piece D2 needs: it removes the pole direction H and
reports the escape mass on the **primitive (pole-orthogonal) subspace**.

- **H (pole/degree cell)** = top eigenvector of L_arch. Not guessed: it carries the
  divergent archimedean mass (`Hmass` grows ≈ linearly in log λ, matching
  Tr K_P ~ ½(log P)²) and overlaps the DC mode n=0 by **0.95–0.97** (see table).
- **N(P)** = `μ_max_prim − 1` on H^⊥; also the primitive past-edge mass.

## Pre-registered vs actual

| | pre-registered | actual |
|---|---|---|
| (1) zeta | N(P) BOUNDED | **BOUNDED**: μ_max_prim ≡ 1.000; N(P) max = 0.11, fit exp −0.05 |
| (2) DH control MUST fail | grow ~ λ^{2β−1} | **FAILS as required**: N(P) 4.36 → 10.12, grows with positive power |

### Sanity — proxy reproduces E101 (no pole removal), exactly
zeta μ_max ≈ 1.000–1.031; DH μ_max 7.60→9.41 on λ=9..17; DH (μ_max−1) ~ λ^0.41
(E101 reported 0.41). Digit-for-digit match with E101.

### D2 table (pole H removed)

zeta:

| λ | dim | Hmass | ovlpDC | μ_max_full | μ_max_prim | N(P) | prim past-edge |
|---|---|---|---|---|---|---|---|
| 8 | 33 | 8.75 | 0.974 | 1.0000 | 1.0000 | 0.000 | 0.000 |
| 10 | 37 | 11.14 | 0.970 | 1.0000 | 1.0000 | 0.000 | 0.000 |
| 12 | 37 | 13.47 | 0.966 | 1.0000 | 1.0000 | 0.000 | 0.000 |
| 14 | 41 | 15.75 | 0.962 | 1.1086 | 1.1104 | 0.110 | 0.110 |
| 16 | 41 | 18.01 | 0.958 | 1.0000 | 1.0000 | 0.000 | 0.000 |
| 18 | 45 | 20.24 | 0.954 | 1.0498 | 1.0498 | 0.050 | 0.050 |
| 20 | 45 | 22.44 | 0.951 | 1.0000 | 1.0000 | 0.000 | 0.000 |
| 22 | 45 | 24.63 | 0.947 | 1.0000 | 1.0000 | 0.000 | 0.000 |

DH (control):

| λ | dim | Hmass | ovlpDC | μ_max_full | μ_max_prim | N(P) | prim past-edge |
|---|---|---|---|---|---|---|---|
| 8 | 33 | 7.14 | 0.974 | 5.356 | 5.357 | 4.357 | 25.95 |
| 10 | 37 | 9.53 | 0.970 | 7.754 | 7.755 | 6.755 | 38.07 |
| 12 | 37 | 11.86 | 0.966 | 8.079 | 8.081 | 7.081 | 34.01 |
| 14 | 41 | 14.15 | 0.962 | 8.867 | 8.868 | 7.868 | 47.15 |
| 16 | 41 | 16.40 | 0.958 | 10.035 | 10.035 | 9.035 | 45.83 |
| 18 | 45 | 18.63 | 0.954 | 11.120 | 11.120 | 10.120 | 57.74 |
| 20 | 45 | 20.84 | 0.951 | 10.343 | 10.344 | 9.344 | 55.11 |
| 22 | 45 | 23.02 | 0.947 | 11.110 | 11.110 | 10.110 | 51.93 |

## Fitted growth exponents

- **zeta:** N(P) max 0.11, fit exponent **−0.05** → BOUNDED. The 0.11/0.05 blips at
  λ=14,18 are non-monotone float64 edge noise (phase-64 AUDIT: float64 cannot resolve
  the marginal edge), not growth.
- **DH:** N(P) ~ λ^{**+0.76**}, primitive past-edge ~ λ^{+0.72}. On E101's own grid the
  raw (μ_max−1) fit is **0.41**.

## Honest caveats (do not over-read the exponent)

1. **The robust, faithful finding** is the *dichotomy*, not a precise exponent: after
   removing the pole H, zeta escape is O(0.1) noise-floor while DH escape is O(4–10)
   and clearly **unbounded and growing**. This is the O(1) robust FAILURE the phase-64
   AUDIT predicted, and it directly confirms Deliverable **D1** (sharp dichotomy): the
   off-line escape direction is **orthogonal to the pole H** — μ_max is essentially
   unchanged by P_prim (5.356→5.357, etc.), so P_prim cannot absorb it.
2. **The precise exponent is NOT reliably pinned** by this proxy. Estimates range
   ~0.4 (E101 grid, μ_max−1) to ~0.72–0.76 (wider grid, μ_max−1 / past-edge). μ_max
   is non-monotone and saturates near 10–11 for λ≥16 (finite-window/truncation ceiling,
   dim caps at 45). All estimates are positive and consistent with 2β−1>0 for an
   off-line β>½; none should be quoted as "the" exponent.
3. This is a **proxy**, not the faithful `K_P = ∫ Y_P* dH_P Y_P`. Building the true
   transfer-matrix Gram (integrating the canonical ODE) remains the correct future step
   for a fully faithful K_P; it was not attempted here (infeasible in the time budget),
   and the E101 proxy was used per the task's authorised fallback.
4. This is a **criterion**, not a proof of RH or of the escape theorem (which is
   RH-strength, phase-64 §5/§7).
