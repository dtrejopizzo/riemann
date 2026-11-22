# Phase 192 — Exact identity: three constructions on the minimizer and on the phase-190 family, with column bookkeeping

Construction round: build an object respecting BOTH columns at once — an EXACT identity on the window minimizer h*_T (or on the
A_M-minimizer family s_w = m^{−½}w(m/M)) in which (Λ(n))_{n<e^{2T}} enters non-linearly, Euler product × FE(q=1) × ℤ-integrality enter jointly as a
mechanism, the margin comes out of the identity, and which is none of the MUST-NOT objects (estimate with remainder, O1–O15-invariant class
argument, symbol-statistic functional, shift-multiplier calculus, certificate, zero information, σ-transport, perturbative induction, REF-D
restatement). Pen and paper only; no numerics.
Mandatory reading done: P46 §20 (thm:shape, cor:shape, prob:region), routes index (now ROUTES-MASTER-INDEX.md; phases 190/191), 06_, SPEC_A, SPEC_B, EXP_005,
and the phase-188 memos L2_012, L2_014, L2_030, N_009, N_020, N_022, L2_008, R163_1001.

**Headline.** Three exact-identity objects were built, each PROVED as an identity, each with a self-review and a clause table.
**No sign is certified; no negative value of 𝔞_T for ζ was found or claimed; λ_A(T) is not moved for any T.** The round's result is bookkeeping:
for every object, the clause "Λ enters non-linearly" had to be passed from the YES column to the NO column on the symbol side — and EI_003
Theorem 2 turns that failure into a PROVED statement (symbol rigidity): no exact identity on the window symbol built from FE, Euler product,
Mellin, Poisson or Riemann–Siegel is non-linear in Λ; non-linearity can enter only through h*(Λ) (REF-D channel, SPEC_A Lemma S) or through
tests built from ζ's own coefficients (twisted second moments, EI_002/EI_003), where the symbol stays affine and indefinite (U_T ≠ ∅).

## Files
| file | object | exact identity | PROVED content | sign |
|---|---|---|---|---|
| EI_001_EXTERIOR_FIELD_IDENTITY.md | exterior field E = σ_T(D)h* outside I_T (SPEC_A's C*_A object) | E = (polar edge moment) − e^{−t/2}·(Chebyshev fluctuation of ψ−u at scale e^t tested by the minimizer, truncated at X) − (archimedean tail, exponent 5/2); Ê = (σ_T−λ)ĥ* − Tate, σ_T = R_X(½+iτ)+R_X(½−iτ) meromorphic with poles only at ±i(2k+½) | Thm 1, Thm 2, P1–P3 (Tate kills exactly the e^{−|t|/2} term and the full polar term; zeros invisible; polar partner of the atom n_j is the opposite-collar Tate moment, correcting SPEC_A §2(d)) | none; C*_A unchanged (REF-D as content) |
| EI_002_LATTICE_MELLIN_IDENTITY.md | Q_M(w) on s_w (SPEC_B T*₃) | Q = (1/π)∫F̂₀²\|ζ_w\|²Re R_{X′}; polar-free split (2.1); ζ_w = cζ + M^{½−iτ}W(½−iτ) + ρ_M (exact Mellin = ℤ-Poisson); ℤ²-Poisson of atom sums with second-order Tate vanishing of (0,0); dual near-coincidences −ℓ₂ ≈ ℓ₁n (self-duality) | Thms 1–4; Fact N2 (phase 190) upgraded NUMERICAL → PROVED (descriptive); SPEC_B Line 2 made exact in the bulk and corrected at the edge; Thm 5: no termwise sign (U_T ≠ ∅), Mellin split not estimable below M^{−3} | none; T*₃/C*₃ unchanged |
| EI_003_WINDOW_HARDY_FUNCTION.md | beyond-window Euler product Z_X = ζ/Z_{<X}, phase Θ_X, window Hardy function Z_T | σ_T = 2Θ_X′; R_X(½+iτ) = Θ_X′ + iZ_T′/Z_T; comb absorbed exactly into the Γ-factor; (2.1): the (iii) object as twisted second moment of the smoothed partial sum against the Euler tail; RS saddle at τ ≈ 2πM = integer resolution | Thm 1; **Thm 2 (symbol rigidity, NO-GO for "non-linear in Λ" on the symbol side)**; Corollary (shape of the mandate) | none |

## What moved between columns (requested bookkeeping)
| clause (mandate YES column) | EI_001 | EI_002 | EI_003 | verdict |
|---|---|---|---|---|
| exact identity, no remainder | YES | YES (ρ_M kept as contour integral) | YES | kept |
| Λ enters non-linearly | **NO** (linear at fixed h*; non-linear only via h*(Λ)) | NO on symbol / YES on test (coefficients 1) | **NO on symbol, PROVED impossible** (Thm 2) | moved to NO column on the symbol side; survives only via h* (REF-D) or via the test |
| Euler × FE × ℤ jointly as mechanism | NO (FE only as m; ℤ unused) | partial (three exact factors in one integrand) | partial (θ, Z_{<X}, coefficients 1) | moved to "jointly as factors, not as one mechanism" |
| ℤ-integrality as mechanism | NO (any positive dψ works) | YES (Mellin pole/polar term/dual modes; ℤ²-Poisson) | YES (coefficients 1) | kept for EI_002–003, lost for EI_001 |
| doubly-exponential margin from the identity | NO | NO (polynomial M^{−3} on the family, in the beyond-Nyquist tail + ρ_M; ARGUED) | NO | moved to NO column for all three |
| wins by fluctuation, not density | YES (structure exhibited) | YES ((0,0) term vanishes to 2nd order) | YES | kept |
| 10⁻⁵-sensitive | YES (inherited) | YES | YES | kept |
| names ζ vs ζ_K | NO | YES (named) | YES (named) | kept for 002–003 |
| not an estimate / not a class / not a certificate / no zeros / not REF-D | YES for the identities; the **sign content** of each is REF-D (C*_A = Lemma S; T*₃ = (S)) | same | same (Thm 2 is a NO-GO, not a deduction) | identities comply; their sign content does not |

## Why these are not retries (index check)
"exterior field": only R163_1001 (C) (NO-GO, exterior samples free) and SPEC_A (statement only) — EI_001 writes the identity those did not.
"Poisson summation / Mellin / theta / Riemann–Siegel / AFE": L2_012 (AFE class NO-GO; coefficient-1 AFE = Poisson), N_009 (self-duality),
N_020 (dual positions), R163_603 (Hardy coupling DEAD), N_012 §3(b) (AFE cited for packets) — none has EI_002 Thms 2–4 or EI_003 Thm 2.
Dead sub-routes of 06_ R1/R9 not reused (no sieve, no 2×2, no Near-as-operator, no SOS, no termwise bound).

## Flags
- No certified negative value for ζ anywhere in this phase.
- Corrections to the record: SPEC_A §2(d) (polar partner of n_j: EI_001 P2); SPEC_B §4 Line 2 (second-order vanishing holds in the bulk, not atom by
  atom at the edge; the y ≥ 1 cut is essential: EI_002 Thm 3(iii)); phase-190 Fact N2 is now PROVED (descriptive, zero-side) for |γ| ≤ M^{1−ε}.
- New index rows proposed (not written to 04_): P192-EI1 (exterior-field identity, PROVED, no sign, W-functional-of-h*), P192-EI2 (Mellin/ℤ²-Poisson
  on the family, PROVED, no sign, REF-D content), P192-EI3 (symbol rigidity NO-GO: non-linear-in-Λ identities on σ_T do not exist).

## Residual after this round
The only place an exact object can be non-linear in Λ and not REF-D by construction is the test side: twisted second moments
∫F̂₀²|ζ_w|²Re R_{X′} (EI_002 Thm 1, EI_003 (2.1)), i.e. problem (S) on the family — whose sign is T*₃(η) (OPEN; REF-D for η ≤ η₀). What such an
object would need beyond the record is a sign statement about the low-frequency twisted second moment of ζ against the beyond-window Euler
tail that is not the explicit formula; nothing in the corpus or the literature sweep supplies one.
