# AUDIT_200_EPSTEIN_001 — Audit of LEMMA_E_EPSTEIN_001 (phase 200, round 7). Object audited:
`LEMMA_E_EPSTEIN_001.md`, `LEMMA_E_EPSTEIN_001_data/`, the `phase-198-parity-split/cert_falsifiers.py` pipeline, P47 lem:monoT
(l. 502) and lem:shape-epstein (l. 8525–8545).

## Summary (≤200 words)

**Verdict: Lemma E PROVED (stands).** I independently rederived the completion, C₀^Q = −4.607041911, the kernel
1/sinh(u/2), the tail 2·log coth(T/2), the polar term and P_T; I checked r_Q = 1∗χ₋₂₀ + χ₋₄∗χ₅ (n ≤ 200), the exact Λ_Q
(Λ_Q(2)=Λ_Q(3)=Λ_Q(7)=0, Λ_Q(36) = −4log6, negatives n ≤ 200 = {36,54,84,126,189,196}), Z_Q(0) = −1, the FE and the residue π/√5.
I re-ran the T = 8/5 certificate (degree 48, 2^240): [−0.0619395254, −0.0619395173], identical to the memo's. lem:monoT does
not use the sign of the comb. Necessary corrections (none affects Lemma E): (a) P47 attributes the values +5.049/+1.785/−3.479
to the T = 1.59 witness, but they belong to the T = 8/5 witness; (b) the phrase "any inequality surviving the average of two
Euler products is falsified" is an overclaim: it must be reformulated as C-E′ (below); (c) the series Λ_Q (and Λ_cosh) does
**not** converge for Re s > 1 (Z_Q has zeros with Re s > 1): the identity is formal / on Re s > σ₀; (d) notation collision Λ_Q
(completion vs. comb); (e) T = 1.59 was not re-run here (25 min), only the 8/5 one and the pipeline.

## 1. Window form

**Completion.** Γ_ℝ(s)Γ_ℝ(s+1) = π^{−s−½}Γ(s/2)Γ((s+1)/2) = π^{−s−½}·2^{1−s}√π·Γ(s) = 2(2π)^{−s}Γ(s) (duplication).
Then ½·20^{s/2}Γ_ℝ(s)Γ_ℝ(s+1) = (√20/2π)^sΓ(s): matches the classical Epstein completion (√|D|/2π)^sΓ(s)Z_Q for a
positive-definite binary form of discriminant D = −20. **Correct.** Numerically: |Λ(0.3+7.1i) − Λ(0.7−7.1i)| ≈ 7·10⁻²⁰
at 15 digits (the memo gives 10⁻³⁵ at higher precision). The factor ½ is irrelevant for the log-derivative.

**C₀^Q.** With P47's convention (2·Re of the archimedean log-derivative at ½+iτ; for ζ this gives ψ(¼) − logπ = −5.3722, which is
P47's C₀): 2·[½log20 + (−½logπ + ½ψ(s/2)) + (−½logπ + ½ψ((s+1)/2))] at s = ½ gives
log20 + ψ(¼) + ψ(¾) − 2logπ, and ψ(¼) + ψ(¾) = (−γ−π/2−3log2) + (−γ+π/2−3log2) = −2γ − 6log2. Evaluated: −4.60704191130755
by both expressions. **PROVED.** The conductor enters as +log20·‖F‖² = 2·log(√20)‖F‖²; the memo's form "2log(√20/2π)"
includes the −2logπ and is the same thing (no coefficient ambiguity).

**Lévy.** Kernels K_a(u) = 2e^{−2au}/(1−e^{−2u}) with u→u/... on the memo's scale: K_{1/4}+K_{3/4} =
2e^{−u/2}(1+e^{−u})/((1−e^{−u})(1+e^{−u})) = 2e^{−u/2}/(1−e^{−u}) = 1/sinh(u/2). **Correct.** Antiderivative 2log tanh(u/4), hence
∫_{2T}^∞ du/sinh(u/2) = −2log tanh(T/2) = 2log coth(T/2); verified by quadrature (T = 1.6: 0.818836). The script uses
log((e^T+1)/(e^T−1)) = log coth(T/2) on intervals. **Correct.**

**Pole and P_T.** Λ_Q (completed) has simple poles exactly at 0 and 1 (Z_Q(0) = −1 ≠ 0 compensates for the pole of Γ(s) at 0; the
poles of Γ at −1,−2,… fall at trivial zeros of Z_Q). The explicit formula sees the divisor of −Λ′/Λ, not the residue; the
polar contribution is Φ(0)+Φ(1), and the subspace that annihilates it is the same P_T = {∫F e^{±t/2} = 0}. **Correct.** The residue
π/√5 (= L(1,χ₋₂₀) = 2πh/(w√20)) only affects the full form through normalization, not the form on P_T.

**Validity of the explicit formula without Euler.** Audit: −Z_Q′/Z_Q has poles for Re s > 1 (Davenport–Heilbronn), so its
Dirichlet series converges absolutely only for Re s > σ₀ > 1. The derivation still holds: with a compact-support test one
integrates at Re s = c > σ₀ (Z_Q/2 → 1, the zeros have bounded real part), the comb is expanded (finite sum, log n < 2T) and it is
shifted to 1−c, collecting **all** zeros (including those with Re s > 1). The memo should state this explicitly in §1.3;
"log-differentiable" is not enough. Label for the form: PROVED (standard derivation, with this precision).

## 2. Coefficients and normalization

Direct count of (x,y) ≠ 0: r_Q(1..30) = 2,0,0,2,2,4,0,0,6,0,0,0,0,4,0,2,0,0,0,2,8,0,0,4,2,0,0,0,4,4, and equality
r_Q = (1∗χ₋₂₀) + (χ₋₄∗χ₅) for n ≤ 200 (independent of `epstein_coeffs.py`). With Σ over all (x,y) ≠ 0 (which counts ±):
Z_Q = ζ_K + L_ψ, and Z_Q/2 = ½(ζ_K+L_ψ) has constant term 1. Both of the memo's forms are consistent; the comb is the
log-derivative of Z_Q/2, which is that of Z_Q. Residue of Z_Q at 1 = L(1,χ₋₂₀) = π/√5 (area: 2π/√20 ✓), Z_Q(0) = ζ_K(0)+L_ψ(0) =
−L(0,χ₋₂₀)/... numerically −1.0000 ✓ (standard value Z_Q(0) = −1 for the sum without ½).

Λ_Q recomputed via the recursion a(n)log n = Σ a(d)Λ_Q(n/d), exact: Λ_Q(2) = Λ_Q(3) = Λ_Q(7) = 0, Λ_Q(4) = 2log2,
Λ_Q(6) = 2log2+2log3, Λ_Q(9) = 6log3, Λ_Q(14) = 2log14, Λ_Q(21) = 4log21, Λ_Q(36) = −4log6, Λ_Q(126) = −8log2−16log3−8log7.
Negatives n ≤ 200: {36, 54, 84, 126, 189, 196} — matches the memo. **PROVED.**

**Notation (correction).** The memo and P47 use Λ_Q both for the completion Λ_Q(s) and for the coefficients Λ_Q(n). P47
also calls something Ξ_Q that is never defined in the lemma. Rename: completion 𝚲_Q or ξ_Q; coefficients Λ_Q(n).

## 3. Certificate

Reproduction: `DENBITS=240 IVDPS=120 DPS=160 cert_epstein.py cert 8 5 full 49` ⇒
**[−0.0619395254109, −0.0619395173403], NEGATIVE: PROVED**, contacts {4,5,6,9,14,16,21}, pieces const −4.6070, Lévy +8.5837,
comb 4.0386 — identical to the memo. The T = 159/100 certificate was not re-run here (same code, same pipeline; the log
`cert_T1.59_full57.txt` is consistent); I recommend the editor re-run it once before closing.

Rigor of the code:
- **F ∈ P_T exact:** the coefficients g₂,…,g₅₆ are fixed rationals; g₀, g₁ are solved for in intervals from the 2×2 Tate
  system (`tate_mom`). There exists a unique real (g₀,g₁) inside the intervals giving F ∈ P_T exactly, and the ratio is enclosed for
  the whole box, hence for that F. Correct (for even G, g₁ ∋ 0 by symmetry).
- **Lévy:** moments ∫₀^{2T}u^r/sinh(u/2) = 2Σ_k γ(r+1,(k+½)2T)/(k+½)^{r+1}: k < 6000 with the incomplete-γ series truncated with
  a remainder bound (ratio < ½ if m > 2x, remainder ≤ last term, added); k ≥ 6000 bounded by integral comparison
  [∫, f(a_N)+∫] (valid: decreasing summand; the lower bound uses γ ≈ r!, error e^{−19000}, absorbed by the 10⁻¹² margin).
  The tail u > 2T is the closed form 2log coth(T/2). **There is no untracked truncation.**
- **Comb:** `contacts` runs through all keys n of `lambdaQ_exact.json` (n ≤ 500 ≫ e^{3.2} ≈ 24.5) and decides log n < 2T by
  interval comparison with a no-ambiguity assertion; it uses exact Λ_Q (rational × log p) of either sign. For T ≤ 1.6 there
  are no negatives in the window (the first, 36, enters at ½log36 ≈ 1.79). Correct.
- **2^280 denominators.** The witness is a degree-56 polynomial in the monomial basis in x = t/T ∈ [−1,1]: the coefficients are
  ~10^{2–3} with massive cancellation (Hilbert/Vandermonde conditioning ~10^{30+}). Rounding to 2⁻⁴⁰ changes F by a
  vector of large relative norm, and the ratio rises to +4.61 (memo datum). This **does not invalidate** the certificate: the
  certificate makes no claim about the Galerkin minimizer, it only evaluates the ratio of the concrete rational F in intervals;
  the box width (≈ 10⁻⁸) shows that the working precision (IVDPS 120–140) dominates the conditioning loss.
  It is poor numerical practice (a Legendre/Chebyshev basis would suffice with 2⁶⁰), not a logical defect.

**Verdict §3: PROVED** for T = 8/5 (re-run) and, with the caveat of re-execution, for T = 159/100.

## 4. Lemma M / lem:monoT

The proof (P47 l. 506–514) extends F by zero: the norm, the Tate moments and c_F do not change; the new contacts have
c_F(log n) = 0; the archimedean part is ∫₀^{2T}(c(0)−c)K + c(0)∫_{2T}^∞K, invariant when passing to T′ because c ≡ 0 on
[2T,2T′]. It never uses Λ(n) ≥ 0 or Euler; only the structure "constant + Lévy with a positive kernel integrable at ∞ + comb
evaluated at log n". With K = 1/sinh(u/2) it is identical. **PROVED for 𝔞^Q, ∀T ≥ 1.59.**

## 5. Cosh decomposition

Identity ½(A+B) = √(AB)cosh(½log(B/A)): trivial. As an identity of **formal Dirichlet series**: y = ½log(L_ψ/ζ_K) has
constant term 0 (both factors start at 1), so log cosh y = Σ_j c_j y^{2j} converges in the formal topology (y^k
supported on n ≥ 2^k) with no branch issue. Real coefficients ✓. Local computation verified: p ∈ 𝒩 split
(χ₋₄(p) = χ₅(p) = −1): ratio ((1−p^{−s})/(1+p^{−s}))², e_p = 2; p = 2: χ₋₄(2) = 0, χ₅(2) = −1, e₂ = 1; p = 5: ratio 1.
"Even in y, starts at y²" is correct as a formal statement.

**Correction:** "convergent for Re s > 1" would be **false** for Λ_cosh and Λ_Q: both have poles where Z_Q vanishes, including
zeros with Re s > 1; also y → −∞ as s → 1⁺ (pole of ζ_K), so the power series of log cosh in y does not converge
analytically near 1. The memo does not claim convergence for Re s > 1, but it does not delimit it either; it should say "formal identity,
absolutely convergent for Re s > σ₀ := sup Re of zeros of Z_Q (>1)". For the window form only finitely many
coefficients are used, so nothing is lost.

Sum: ½(5.04913 + 1.78519) − 3.47910 = −0.06194 = the T = 8/5 certificate value ✓. Archimedean: ζ_K = ζ·L(χ₋₂₀) (Γ_ℝ(s)Γ_ℝ(s+1),
χ₋₂₀ odd, conductor 20); L_ψ = L(χ₋₄)L(χ₅) (Γ_ℝ(s+1)·Γ_ℝ(s), conductor 4·5 = 20). **Confirmed:** same C₀^Q, same kernel,
same P_T (ζ_K has a pole at 1; L_ψ is entire — the form on P_T does not see the difference, but the *full* form of L_ψ carries no
polar term: in §3 of the memo the table adds the "pole 2AB" term also in the L_ψ column, which is incorrect for L_ψ as a function
in its own right; at g* it is not in P_T. Label that table NUMERICAL; correct the column or note it).

**Witness discrepancy:** the values +5.049/+1.785/−3.479 come from the **T = 8/5** witness, not T = 159/100. The memo says so
(§4.1.3), but the memo's summary and P47 lem:shape-epstein ("on the witness", immediately after the T = 159/100 witness) do not.

## 6. Constraint C-E

The phrase "any inequality that survives averaging two Euler products with the same Γ is falsified" is false
as stated: averaging Z (½(ζ_K+L_ψ)) is not an operation on combs, and a linear inequality on the comb stable under
Λ ↦ ½(Λ₁+Λ₂) **would hold for Epstein only if Λ_cosh contributed with favorable sign**, which is not a property of the
average but of the extra term. Precise formulation:

**C-E′.** Let 𝓛 be a class of combs Λ (with archimedean part Γ_ℝ(s)Γ_ℝ(s+1), conductor 20, same P_T). If 𝓛 contains
½(Λ_K + Λ_ψ) + Λ_cosh with Λ_cosh := −(log cosh y)′ formal, then no statement "𝔞_T^Λ ≥ 0 on P_T ∀Λ ∈ 𝓛" is true
for T ≥ 1.59. In particular false are: (a) any positivity statement that only uses properties of the comb stable
under convex combination of log-derivatives of Euler products **plus** a nonnegative comb supported on composites (at order 2,
Λ_cosh ≥ 0 supported on {4,6,9,14,21,…}); (b) "Λ ≥ 0 on the window". A positivity proof must use that Λ is the log-derivative of
a **single** Euler product (Λ_cosh ≡ 0), or an equivalent condition for the given window. Label: PROVED as falsifier of
(a),(b) (they are a direct consequence of Lemma E + the identity); ARGUED as a design principle.

Sign note: the memo says the defect "enters with a fixed sign"; only order 2 has a fixed sign (≥ 0); order 4 is ≤ 0
(n = 36,…). In the window T ≤ 1.79 only order 2 acts, which is why the statement holds there.

## 7. P47 lem:shape-epstein (l. 8525–8545)

- Completion, Γ factor, conductor 20: backed up ✓ (corrects the old "Γ(s/2)").
- "Ξ_Q": not defined — use the completion's name.
- "zeros in Re s > 1 [DH1936]": correct. Davenport–Heilbronn (1936) prove infinitely many zeros for σ > 1 for the Epstein
  zeta of a binary form with class number h > 1; x²+5y² has h = 2 ✓. The memo's numerical zeros (Re ≈ 0.93) lie in the strip; they
  do not contradict DH (those with σ > 1 are higher). CITED ✓.
- "nonnegative Dirichlet coefficients" (r_Q ≥ 0) ✓; "Λ_Q(n) < 0 first at n = 36" ✓.
- Certificate and monoT ✓. "every contact … has Λ_Q(n) ≥ 0" ✓ (Λ_Q(16) = 2log2 > 0; its term is negative because c(log16) < 0, not
  because of the sign of Λ).
- "on the witness the two Euler-product forms are positive (+5.049, +1.785) … (−3.479)": **attribution error** — those are
  the values at the T = 8/5 witness. Correct to "on the degree-48 witness at T = 8/5" or recompute at the 1.59 one.
- "Hence any inequality … that survives averaging two Euler products … is falsified": **overclaim**, replace with C-E′.
- "Euler removal; proved": honest for the negativity statement on P_T ∀T ≥ 1.59 (interval certificate + monoT); it would help to
  leave CITED for FE/Z_Q = ζ_K + L_ψ/DH in the text. The lemma's label remains **proved**.

## 8. Overall verdict

| item | verdict |
|---|---|
| Form 𝔞_T^Q, C₀^Q = −4.607041911, 1/sinh(u/2), 2log coth(T/2), P_T | PROVED (add derivation with c > σ₀) |
| Λ_Q(n), r_Q, Z_Q(0) = −1, residue π/√5, normalization | PROVED / verified |
| Lemma E, T = 8/5 | PROVED (re-run) |
| Lemma E, T = 159/100 | PROVED (pipeline audited; re-run once) |
| monoT for Epstein | PROVED |
| Cosh identity, Λ_cosh even | PROVED (formal; not for Re s > 1) |
| Values 𝔞^K, 𝔞^ψ, defect | PROVED, but at the T = 8/5 witness |
| C-E | reformulate as C-E′ |
| Table §3 (Mori) L_ψ column with pole | NUMERICAL, correct/annotate |
| P47 lem:shape-epstein | proved, with 4 text corrections |

Mandatory corrections: (1) P47: attribute the decomposition values to the T = 8/5 witness; (2) P47 and memo: replace the
averaging phrase with C-E′; (3) P47: define/rename Ξ_Q and separate completion/comb notation; (4) memo §1.3/§4.1: explicit
formula with c > σ₀ and convergence of Λ_Q, Λ_cosh only for Re s > σ₀ (formal identity); (5) memo: "fixed sign" only at order 2.
None of these affects the result: **Lemma E remains PROVED.** Nothing here gives a sign for ζ; L′♯ and row D remain OPEN.
