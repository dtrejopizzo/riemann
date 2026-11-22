# AA_001 — Parity split of row D: falsifiers on the odd sector, D_odd and D_even

Phase 198, track AA. Memo, not yet audited. Row D OPEN.
Script: `scripts/z001_parity_split.py` (copied from phase 197, unchanged; mpmath, monomial Galerkin, M = 24, dps = 80;
NUMÉRICO, not interval). Raw outputs: `scripts/r_*.txt`.

## 0. Corpus / index check and new reason
Index (README, 04_PHASES_100-189, 06_OPEN_RESIDUES) and corpus grep ("odd sector", "sector impar", "parity", "paridad",
"sinh(t/2)", "μ_odd", "even sector", "Theorem P", "n₋"): prior parity work = BARRIER_Z_001 (sector decoupling, Λ comb
only), BARRIER_X_001 X2/X4 (Kronecker parity d(p^j)↦(−1)^j d — a different involution, on comb weights, not on F),
Theorem P (n₋ counts on the full form, no sector resolution), R138/R184/R186 (parity of test functions in other
contexts; no sector-restricted falsifier analysis). Not in the index: whether the falsifiers of thm:shape survive
restriction to P_T^odd. New reason: if some falsifier were odd-positive for all T, D_odd would be a target outside
thm:shape(A) — a genuinely different method class. This is a new question, not a variant of a registered attempt.

## 1. Odd-sector form (PROVED, elementary)
For F odd on [−T,T]: B := ∫F e^{−t/2} = −A, so the single constraint ∫F sinh(t/2) = 0 forces A = B = 0 (both Tate
functionals vanish, while in the even sector only A = B ≠ 0 is excluded via A+B=0 ⇒ A=B=0 as well). c_F is even
(always), F̂ is odd, purely imaginary, F̂(0) = 0, and |F̂|² is even with a double zero at τ = 0. eq:Aform reads, on
P_T^odd,
  𝔞_T(F) = (1/2π)∫ m(τ)|F̂(τ)|² dτ − 2Σ_{n<e^{2T}} Λ(n) n^{−1/2} (1/2π)∫cos(τ log n)|F̂(τ)|² dτ,
with F̂(τ) = −2i∫_0^T F(t) sin(τt) dt (a sine transform). So D_odd is the sine-transform (Dirichlet-at-0) version of the
same quadratic form; no new term appears and none disappears except the vanishing τ = 0 mass.

## 2. Falsifiers restricted to the odd sector (NUMÉRICO; negative Galerkin values are genuine negative Rayleigh
quotients up to float error, i.e. falsifying witnesses)
| comb | T=½log2 | 0.5 | log2 | ½log5 | 1.0 | 1.2 |
|---|---|---|---|---|---|---|
| Λ (μ_even / μ_odd) | .547/.843 | .012/.191 | 1.3e-7/1.2e-5 | 6.0e-10/3.3e-8 | 1.2e-11/1.2e-9 | – |
| 0 (archimedean only) μ_odd | .843 | .476 | .148 | **−.0026** | **−.222** | **−.408** |
| a_2 (p=2 deleted) μ_odd | .843 | .476 | .061 | **−.411** | **−.523** | **−.548** |
| a_3 μ_odd | .843 | .191 | **−.083** | **−.159** | **−.598** | **−.637** |
| 1.15Λ μ_odd | .843 | .137 | **−.076** | **−.124** | **−.153** | **−.155** |
| 0.85Λ μ_odd | .843 | .243 | .032 | .006 | **−.029** | **−.058** |
| 2Λ μ_odd | .843 | **−.192** | **−.772** | **−1.02** | **−1.05** | **−1.05** |
(M=24 values for Λ are upper bounds, larger than the converged Z_001 values.)

Conclusions.
- Every tested falsifier (O_2 scaling both sides, O_1 deletion at p = 2, 3, the zero comb) is **negative in the odd
  sector** at T ≥ 1 (all of them), and already at ½log5 except 0.85Λ. The odd sector is never protected.
- Ordering: the odd bottom fails at a later T than the even one (e.g. zero comb: even negative from log2, odd from
  ≈½log5; 0.85Λ: even from log2, odd from ≈0.9). This is the F̂(0)=0 low-frequency gain, and it is quantitative only.
- Hence thm:shape(A) clauses for O_1 (p=2,3), O_2/O_4 (c-scaling, both sides of 1), and the zero comb hold verbatim
  for D_odd at T ≥ 1 (transfer argument of lem:transfer is sector-agnostic: a deduction class closed under O_j proves
  μ_odd(O(q_0)) ≥ 0, contradicted by the odd-sector negative values above). Windows shift upward relative to the
  even sector; the lemma windows in Paper 46 must be re-read with the odd thresholds (NUMÉRICO list above).
  Beurling, Ξ_Q, O_6–O_15: not computed here (OPEN); by the same mechanism (they break the Λ near-kernel at the
  first-contact scale while the odd margin is itself first-contact scale, 1e-9 at T=1) they are expected to transfer.
- Margin: μ_odd(Λ) decays at the same exponential rate as μ_even (Z_001), so thm:shape(B)/(B′) precision
  constraints apply to D_odd with the constant shifted by ≈ log(100–300). No clause of thm:shape is lost by
  restricting to odd F.

## 3. Direct attack on D_odd
(a) Range (PROVED, trivially inherited): μ_odd ≥ λ_A > 0 on every window where Paper 46 proves λ_A > 0
    (thm:log5A, T ≤ ½log5). No proof beyond ½log5 obtained.
(b) NO-GO (NUMÉRICO falsifier, sharp form): "odd F̂ kills the low-frequency region, so m(τ) dominates" — the
    archimedean part alone is odd-negative at T ≈ ½log5 (−0.0026) and −0.22 at T = 1. Any proof of D_odd beyond ≈ ½log5
    must use the primes in a load-bearing way; a Hardy/Dirichlet-at-0 inequality for sine transforms that does not see
    the comb is excluded (it would hold for the zero comb).
(c) NO-GO (same table): "the comb Σv_n cos(τ log n) against odd |F̂|² has a definite sign" — 2Λ and 1.15Λ are
    odd-negative from T ≈ 0.5 / log2; comb-monotone arguments are excluded (O_2/O_4 closure).
(d) What survives: the odd-sector gain is a constant factor 10²–10³ in the margin, not a change of regime. D_odd is
    the same problem as row D on a sine-transform space; it is not easier in kind.

## 4. D_even (quick)
Even sector carries the minimizer wherever converged (Z_001), constraint ∫F cosh(t/2) = 0 (⇔ A = B = 0), F̂ even,
cosine transform, F̂(0) free. All falsifiers above are even-negative at windows ≤ the odd ones. D_even is the binding
half; D_even ⇒ D_odd is NOT implied (sectors decoupled), but numerically μ_odd ≫ μ_even, so every resource should go
to D_even. Label: OPEN.

## 5. Labels
- §1 odd-sector form: PROVED.
- §2 table: NUMÉRICO. Transfer of thm:shape(A) clauses O_1(p=2,3), O_2/O_4, zero comb to D_odd at T ≥ 1: PROVED
  modulo the numerical negativity (CONDITIONAL on interval verification of the listed negative values).
- §3(a): PROVED (inherited). §3(b),(c): NO-GO (NUMÉRICO falsifiers). Beurling/Ξ_Q/O_6+ in odd sector: OPEN.
- D_odd, D_even: OPEN. Parity split gives no independent easier half.
