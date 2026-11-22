# AUDIT_198 — audit of phase 198 (AA, CERT, BB, CC) and phase 197 tracks Y, Z

Every check below was made against
Paper 46 (`04-papers/46-row-d-dual-certificates/main.tex`): eq:Aform (l.402), C_0 = ψ(¼) − log π = −γ − π/2 − 3log2 − logπ,
K = ½/sinh(u/2) + ½/cosh(u/2), thm:S(iii), v_n = 2a(n)/√n, lem:degen (l.3249), lem:transfer (l.7647), thm:log5A,
the Liu citation (complete form, T ≤ 1 and T ≤ 17/16, preprint, CITED), subsec:shape-geom and sec:spec. Row D: **OPEN**.

## 0. Audit lemma (PROVED, elementary; used below to extend certificates)
**Lemma M (window monotonicity).** For a fixed comb a, T ↦ λ_A(T; a) and T ↦ μ_±(T; a) are non-increasing.
Proof: extend F ∈ P_T by zero to [−T′, T′] with T′ > T. The Tate moments are unchanged, and so is c_F. In eq:Aform,
Lev(c_F) does not depend on T, and the new contacts n with 2T ≤ log n < 2T′ contribute c_F(log n) = 0. Parity is
preserved, so the claim holds in each sector. □
Consequence: a certified negative quotient at T_0 is a certified falsifier at every T ≥ T_0 for the same comb.

## (a) Parity split (Z §1, AA §1): CORRECT
- R F(t) = F(−t) preserves c_F and swaps ∫F e^{±t/2}. So P_T = P_T^+ ⊕ P_T^−, with P^+ = {even, ∫F cosh(t/2) = 0} and
  P^− = {odd, ∫F sinh(t/2) = 0}, and λ_A = min(μ_+, μ_−). Verified. PROVED.
- AA §1: for odd F, ∫F e^{t/2} = ∫F sinh(t/2) = −∫F e^{−t/2}, so the single constraint already gives A = B = 0. The prime
  term −Σ v_n c_F(log n) is correctly rewritten through c_F(u) = (1/2π)∫cos(τu)|F̂|². PROVED. (The parenthetical about the
  even sector, "only A = B ≠ 0 is excluded", is garbled. In the even sector A = B automatically, and the constraint
  forces A = 0. Cosmetic.)
- Z §2 "converged for T ≤ 0.9": at T = 0.9, μ_even changes by 14% between M = 56 and M = 64 (5.8e−17 → 5.0e−17), which
  exceeds the stated ≲ 10%. Read the values at T = 0.9 as Galerkin upper bounds of the right order, not converged values.
  At T = 0.8 the change is 3%. Z's conclusion "splitting = level scale, no hidden symmetry" stays NUMÉRICO for T ≤ 0.8,
  is borderline at 0.9, and is OPEN for T ≥ 1. The memo already says OPEN for T ≥ 1.

## (b) CERT_FALSIFIERS_001: method GENUINELY RIGOROUS (spot-check: all of `cert_falsifiers.py` read; AA odd a_2, T = 1)
Checked item by item:
1. Formula. `quotient` evaluates C_0 c(0) + ∫_0^{2T}(c(0) − c)K + c(0)∫_{2T}^∞K − Σ v_n c(log n). This is eq:Aform with
   Lev split at 2T, which is legitimate because c ≡ 0 beyond 2T. The C_0 values in `quotient` and in `galerkin` agree.
   The tail is log coth(T/2) + 2 arctan e^{−T}, which agrees with thm:S(iii); I re-derived it. The script's docstring
   says π − 2 atan e^T, which is the same number. ‖F‖² = c(0). OK.
2. c(Ts) = T Σ g_j g_k ∫_{−1+s}^1 x^j (x − s)^k dx is computed in exact `Fraction` arithmetic and enters as intervals. OK.
3. Kernel moments. For k < 3000 the code uses the lower incomplete gamma. In the series branch the termination test
   m > 2x gives ratio ≤ ½, so the geometric remainder is ≤ the last term, and that remainder is added. The complement
   branch uses an exact identity. For k ≥ 3000 the integral-comparison bracket [∫_N^∞, f(N) + ∫_N^∞] is correct for
   decreasing f. The omitted incomplete part has relative size ≤ e^{−x}x^r/r! with x ≥ 6000·2T. It is covered by the
   1e−12 relative widening. Interchanging sum and integral is justified by absolute convergence. OK.
4. Tate moments. The Taylor remainder 4|c|^{121}/121! dominates 2e^{|c|}|c|^{121}/121!, since |c| = T/2 ≤ 0.55. The
   coefficients of x^0, x^1 (full) or x^1 (odd) are the interval solution of the exact constraint system. So the box
   contains the exact F ∈ P_T, and the interval quotient encloses its Rayleigh quotient. **Exact imposition: confirmed.**
   For odd G: ∫F sinh(t/2) = T∫G(x) sinh(Tx/2) dx. OK.
5. Comb. a(p^k) = log p and v_n = 2a/√n, with c(log n) by interval Horner. OK.
6. **Minor rigor gaps (do not affect the results).**
   (i) The contact set is decided by float comparison of interval endpoints, not by interval logic as the memo claims.
   This matters only when log n ≈ 2T, which happens at n = 9, T = log 3 and n = 5, T = ½log5. There c_F(2T) = 0 exactly,
   and the polynomial c(Ts) vanishes at s = 2, so including or excluding n gives the same value. Every other margin is
   ≥ 0.02.
   (ii) Float conversions such as `float(term.b)·1.0000001` and the remainder of `tate_mom` are rounded to nearest, not
   outward. Each is a bound that is loose by a factor ≥ 2, or is covered by an explicit safety factor. Acceptable.
   Recommended fix: replace the float tests by `iv` comparisons.
   **Verdict: the 10 enclosures are PROVED.** By Lemma M they extend upward: zero comb (odd) for T ≥ ½log5; a_3 (odd) for
   T ≥ ½log5; Λ − δ_3 for T ≥ 0.75; Λ − δ_7, a_2, 2Λ, 1.15Λ (odd) for T ≥ 1; Λ − δ_8 for T ≥ log3. Still NUMÉRICO:
   0.85Λ (odd), every falsifier at T < ½log5 other than q = 3 at T = 0.75, and Y's rows at log2, ½log5 − 10⁻⁴, 0.9,
   ½log11 − 0.01.

## AA_001: corrections
- §2 "every tested falsifier is odd-negative at T ≥ 1 (all of them)". This is PROVED (CERT + Lemma M) for the zero comb,
  a_2, a_3, 2Λ and 1.15Λ. It is NUMÉRICO for 0.85Λ (−0.029 at T = 1, uncertified). The transfer of thm:shape(A) clauses to
  D_odd is therefore PROVED at T ≥ 1 for O_1 (p = 2, 3), O_2/O_4 on the side c > 1, and the zero comb. The side c < 1
  of O_2/O_4 is CONDITIONAL (0.85Λ uncertified). The "windows" claims at T < 1 stay NUMÉRICO.
- §3(b) "archimedean-only odd positivity fails at ≈ ½log5". This is upgraded to **PROVED at T ≥ ½log5** (CERT row
  −0.0026653). The threshold location "≈ ½log5" is NUMÉRICO.
- §4 "μ_odd ≫ μ_even" holds only in the range resolved by Z (T ≤ 0.8–0.9). It does not hold at T ≥ 1.
- §2 "Beurling/Ξ_Q/O_6+ expected to transfer": ARGUED, not a result. Keep it OPEN.

## (c) BB_001
- Identity 1 and the concavity of λ(c): correct. Concavity is **CITED (P46 lem:degen restricted to the line cΛ)**, not
  new. The positivity set {c: λ(c) > 0} at T = 1 excludes c = 0, 2, 1.15 (PROVED via CERT; odd witnesses suffice
  because λ_A ≤ μ_odd). Excluding 0.85 is NUMÉRICO. That the set contains c = 1 at T = 1 is CITED (Liu, T ≤ 1).
- **Identity 2: coefficient error.** ‖C_a h*‖² = ½Σ_{m,n} v_m v_n [c(log m/n) + c(log mn)] is correct (the four
  ± translations pair up). The product-lag coefficient, however, is ½·Σ_{mn=N} v_m v_n = **2(a⋆a)(N)/√N**, not 4(a⋆a)(N)/√N.
  The same error appears in BB5. The identity needs strong EL, i.e. 1_I A h* ∈ L² (CONDITIONAL, correctly flagged), and
  it uses the even-sector multiplier cosh. At T ≥ 1 the parity of h* is undetermined (Z), so the identity should be
  stated for the minimizing sector, with multiplier cosh or sinh. Label CONDITIONAL is kept.
- BB3. "Every EL-polynomial identity is comb-generic": PROVED; the derivation is literally comb-independent. The clause
  "any inequality read off by dropping the out-of-window term is Bessel/CS (N_018)" is **ARGUED**, not proved. NO-GO label:
  PROVED for identities, ARGUED for the inequality class.
- BB4. a_P ↦ ζ(s)(1 − p^{−s}) (coefficients 1_{p∤n}) and 2Λ ↦ ζ² (coefficients d(n)) satisfy (i)–(iii). Both have
  certified odd witnesses at T = 1, as does the zero comb, which also lies in 𝒞_sr. **NO-GO PROVED** at every T ≥ 1 by
  Lemma M. For T ∈ [½log5, 1), the zero comb (odd) gives it as well. Correctly called a consistency upgrade of INV_I I2.
- BB5 residue: closed by CC (see (d)) within the declared class only.

## (d) CC_001
- CC1. a(6) = 0, so the lag log 6 is absent from λ and ∇λ: PROVED (trivial). The window list {2,3,4,5,7} (+8 for
  T > ½log8) is right for T ≤ 17/16. The concavity on ℝ⁴ is **CITED (lem:degen)**.
- CC2. With S(κ) = S_0 − Σκ_p C_p compressed to a parity sector, second-order Rayleigh–Schrödinger perturbation gives
  ∂²λ/∂κ_p∂κ_q = −2⟨C_p h*, R_⊥ C_q h*⟩, where R_⊥ = (S − λ)^{-1}|_{h*^⊥} ≥ 0. So H ≼ 0, and CS holds. Formula and sign
  verified, and the script implements exactly −2Σ_j ⟨h, C_p ψ_j⟩⟨h, C_q ψ_j⟩/(E_j − E_0). PROVED **at a simple isolated
  bottom**. "Neither fixes the sign of H_23" is correct.
- CC3 edge bound: CS, PROVED.
- CC4. Continuity in positions gives the stated conclusion: a strict sign of H_23 at ℤ persists on an open set. This is
  PROVED **only where the bottom is simple**. At Λ, simplicity is **OPEN** (it is neither proved nor disproved). The
  memo's support "ARGUED at Λ (near-degenerate numerically)" rests on an artefact (see (e)) and is withdrawn. Correct
  label: CC4 PROVED for simple bottoms (this covers the falsifiers a_2, a_3 and the Beurling δ ≠ 0 tests, where gaps are
  O(0.1)); CONDITIONAL on simplicity at Λ. The NO-GO on the class "second-order κ-interaction at the minimizer" stands
  at that strength.

## (e) Inconsistency: Z (μ_even ≈ 5e−17 at T = 0.9, M ≤ 64) vs CC (λ ≈ 1e−7 at T = 1, M = 12–16)
Both are Galerkin **upper bounds**, from monomial bases split by parity. CC's bases contain 6–8 functions per sector,
against 24–32 in Z. Z itself shows that the bottom keeps falling with M down to ≤ 2.5e−22 at T = 1, M = 64. CC's
1e−7 is therefore over-estimated by ≥ 15 orders: the near-kernel is **unresolved**. Consequences:
- CC §4, all Λ rows (λ, gap, H_23, corr, c_{h*}(log 6)) are **not data about the Λ minimizer**. The shrinking "gap" with M
  is the basis resolving further near-kernel directions. It is not evidence of near-degeneracy. Z, which is resolved at
  T ≤ 0.8, finds the two sectors separated by a factor of 10²–10³, which goes against CC's reading. Readings (a) and (c)
  at Λ: **WITHDRAWN** as evidence (they become "unresolved"). The bound |c_{h*}(log 6)| ≲ 7e−4 is unsupported.
- What survives in CC numerics: the negative values at a_2, a_3 and Beurling δ = ±0.02, +0.1. Negative upper bounds are
  genuine falsifiers (NUMÉRICO; a_2 and a_3 match the certified values). The H_23 signs at those combs (gap O(0.1))
  are plausibly resolved but unconverged in M; NUMÉRICO. Reading (d) "position-fragile" is NUMÉRICO and valid.
- BB §2 does not depend on unresolved numerics. Y §2 already declared T ≥ 0.9 undecided, which is correct.
- Y §1 quotes "λ_A ≤ 3.1e−12 past ½log5 (P46 App. num)". P46 l.164 and l.10145 give λ_A(½log5) ≈ 3.10e−12 (NUMÉRICO). By
  Lemma M this is an upper bound for every T ≥ ½log5. Correct as a NUMÉRICO bound.

## BARRIER_Y_001
- §1 Farkas dual: PROVED (unchanged from the memo). The lem:degen inequality is quoted with the correct sign and
  normalisation.
- §3 / Y1(b): **inputs upgraded**. Λ − δ_3 at 0.75 and at ½log5 + 0.01, Λ − δ_7 at 1, and Λ − δ_8 at log3 are PROVED (CERT).
  By Lemma M they hold at all larger T, wherever the deletion is an admitted move. NO-GO 𝒦_Y^{01}: PROVED at T ∈ {0.75,
  ½log5 + 0.01, 1, log3} for the certified q. At the remaining tested windows (log2, ½log5 − 10⁻⁴, 0.9, ½log11 − 0.01) and
  for the other q it is NUMÉRICO. Note that the q = 3 certificate at T = 0.75 lies inside the certified window
  T ≤ ½log5 (thm:log5A). The method defect is therefore PROVED there, independently of the sign at Λ.

## Label table (corrections only)
| item | memo | audited |
|---|---|---|
| AA §2 transfer, O_1(2,3), cΛ c>1, zero comb, T≥1 | CONDITIONAL | PROVED (CERT + Lemma M) |
| AA §2, 0.85Λ odd | NUMÉRICO | NUMÉRICO (side c<1 CONDITIONAL) |
| AA §3(b) arch-only odd failure | NO-GO NUMÉRICO | NO-GO PROVED for T ≥ ½log5 |
| BB §2 concavity / CC1 concavity | PROVED | CITED (lem:degen) |
| BB Identity 2 | CONDITIONAL | CONDITIONAL; coefficient 2(a⋆a)(N)/√N (not 4) |
| BB3 inequality clause | PROVED | ARGUED |
| CC2 | PROVED | PROVED at simple isolated bottom |
| CC4 at Λ | ARGUED (near-degenerate) | CONDITIONAL on simplicity (OPEN); numerical support withdrawn |
| CC §4 Λ rows | NUMÉRICO | unresolved (≥15 orders above Z) — no evidence |
| Y1 inputs, 4 certified rows | NUMÉRICO | PROVED |
| Z §2 "converged T ≤ 0.9" | NUMÉRICO | NUMÉRICO for T ≤ 0.8; 0.9 borderline |
| CERT contact set "interval comparison" | — | float comparison; harmless (boundary contacts have c = 0) |

No sign obtained in phases 197–198. Row D: **OPEN**.
