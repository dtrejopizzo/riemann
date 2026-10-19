# BB_001 — Reading the pairing Π(T) through the Euler–Lagrange equation; multiplicative closure (track BB, phase 198)

Status: memo, not yet audited. Labels: PROVED / CONDITIONAL / ARGUED / NO-GO / OPEN.
Row D remains OPEN.

## 0. Corpus / index check (mandatory)
- ROUTES-TRIED-INDEX/README read (families, phases 194–198, sign-carrier spec (1)–(6)).
- Phase 186: Theorem X / W-fam: every first-order discriminant is a functional of h*, not σ.
- Phase 190: near-coincidence matrix A_M, identity C3 (Div+Near), "no ζ-specific fact on the prime side".
- Phase 193: first-contact obstruction (near-cancellation of minimizer translates by log2..log5).
- INV_I_001 Thm I2/I4 (integrality, O_4^ℕ-closure, Selberg = first non-homogeneous relation, excluded);
  R186_005 TB3-neg (generalized Selberg holds for every b); N_018 (identities + Bochner/Cauchy–Schwarz).
- New reason for this track: questions (1)–(3) are asked **at the minimizer h*, through its EL equation**
  (minimizer-level, not test-family or coefficient-level), and the closure question is tested against the
  **certified** falsifiers of CERT_FALSIFIERS_001. Where a step coincides with an indexed route it is flagged.

## 1. Set-up (P47 eq:Aform)
a_T(F) = Arch_T(F) − Σ_{n<e^{2T}} v_n c_F(log n), v_n = 2a(n)/√n, on P_T = {F ∈ L²[−T,T]: ∫F e^{±t/2} = 0}.
Write a_T(F) = ⟨A F,F⟩ − ⟨C_a F,F⟩ with (C_a F)(t) = ½Σ v_n [F(t−log n)+F(t+log n)] (on ℝ), so
⟨C_a F,F⟩_{L²(ℝ)} = Σ v_n c_F(log n). h* = normalized minimizer, λ_A = a_T(h*). R F(t)=F(−t) commutes with A, C_a, and
the Tate pair {e^{t/2},e^{−t/2}} spans an R-invariant plane, so the even-sector EL equation carries one Tate multiplier
(on cosh(t/2)): BARRIER_Z (PROVED).

## 2. Identity 1 (PROVED, trivial): Π(T) = Arch_T(h*) − λ_A(T).
Pair EL with h*; the multiplier term vanishes because h* ∈ P_T. This is the Rayleigh/homogeneity identity (lem:degen
type) — confirmed, nothing new. Hellmann–Feynman along the family cΛ: λ(c) := λ_A(T;cΛ) is a minimum of affine
functions of c, hence **concave**; at a simple minimizer ∂_cλ = −Σ v_n^Λ c_{h*_c}(log n),
so c ↦ Σ v_n^Λ c_{h*_c}(log n) is non-decreasing (PROVED, superdifferential form in general).
Consequence: the positivity set {c: λ(c) > 0} is an interval; at T = 1 it contains neither 0.85 nor 1.15 nor 0 nor 2
(odd-sector certificates). Concavity gives only upper bounds on λ(1) from the falsifier values ⇒ no sign (REF-D).

## 3. Identity 2 (PROVED modulo regularity, CONDITIONAL on A h* ∈ L²(I_T)): the squared EL identity.
Strong EL on I = [−T,T]: 1_I C_a h* = 1_I(A h* − λ_A h* − α cosh(t/2))  (even sector).
Split ‖C_a h*‖²_{L²(ℝ)} = ‖1_I C_a h*‖² + ‖1_{I^c} C_a h*‖², and expand the left side:
  ½ Σ_{m,n} v_m v_n [ c_{h*}(log(m/n)) + c_{h*}(log(mn)) ]
      = ‖1_I(A − λ_A)h* − α cosh(t/2)‖² + ‖1_{I^c} C_a h*‖².            (BB2)
This is the first identity in the track where **+ meets ·** at the minimizer: lags log(mn) (product, supported mn<e^{2T},
coefficient 4(a⋆a)(N)/√N at N=mn) and lags log(m/n) (near-coincidences m≈kn, the phase-190 / problem (S) object).
Both sides are quadratic in a; the out-of-window term is ≥ 0.

### Theorem BB3 (NO-GO, PROVED): (BB2) and every identity obtained from EL by polynomials in C_a is comb-generic.
Proof: the derivation uses only linearity of C_a in a and the EL equation for the minimizer of a_T(·;a); it holds verbatim
for every comb a with its own minimizer h*_a. The only Λ-arithmetic it can import is through a⋆a, a⋆a⋆a, …; for any
a = log-derivative coefficients of an Euler-type series, a·L + a⋆a = (coefficients of F''/F) is a formal identity
(generalized Selberg, = R186_005 TB3-neg, INV_I I4). Hence clause (1) of the sign-carrier spec fails. Any inequality
read off (BB2) by dropping the ≥0 out-of-window term is a Bessel/Cauchy–Schwarz bound (N_018 family). □

## 4. Multiplicative closure (question (2))
### Proposition BB4 (PROVED, elementary): the closure data are shared by the certified falsifiers.
Let 𝒞_sr = combs a with (i) supp a ⊆ prime powers and closed under p^j,p^k ↦ p^{j+k} inside the window, (ii)
a(p^k) = κ_p log p independent of k, (iii) exp(Σ a(n) n^{−s}/log n) has coefficients in ℤ_{≥0}.
Then a_P (κ_p=0 at one p; series ζ(s)(1−p^{−s}), coefficients 1_{p∤n}) and 2Λ (ζ², coefficients d(n)) lie in 𝒞_sr.
By CERT_FALSIFIERS_001 (interval-PROVED): a_2 and 2Λ have explicit odd F ∈ P_1 with a_T(F) < 0 at T = 1
([−0.5227840], [−1.0465246]). Hence **no inequality forced by (i)–(iii) can give λ_A(1) > 0** (NO-GO PROVED for class
𝒞_sr at T = 1). This sharpens INV_I I2 (𝒞_ℤ, O_4^ℕ) to explicit certificates at T = 1 in the odd sector; it is a
consistency upgrade, not a new route.
What remains Λ-specific after (i)–(iii): κ_p = 1 for **all** p < e^{2T} (completeness + normalization). On this residue the
c-family (§2) shows the separating datum is the scalar position of 1 inside the positivity interval of λ(c) — REF-D.

### Remark BB5 (ARGUED): where a multiplicative closure could bite.
In (BB2) the product lags give Σ_N 4(a⋆a)(N)N^{−1/2}c_{h*}(log N); for N = p^k, (Λ⋆Λ)(p^k) = (k−1)log²p — determined by κ_p
alone, so p-power closure is κ-linear and O_4-blind. Cross terms N = p^i q^j (distinct primes) are the only places where
two different κ's multiply; a sign could only come from a lower bound on Σ_{p≠q} κ_pκ_q (…)c_{h*}(log p^iq^j) that fails
when one κ_p = 0. With T ≤ ~1.2, N = 6, 10, 12 are the first such lags (6<e^{2T} needs T>0.896). OPEN, no inequality known;
it inherits Theorem X (h*-functional) unless the bound uses the EL equation of h* at those lags.

## 5. Self-check
Six clauses: (1) fails for BB2/BB3 (comb-generic); (2) not a cone on log ζ; (3) BB4 is integrality and dies (I2);
(4) n/a; (5) no FE coupling; (6) no ∂log crossing. Barrier (BARRIER_001 Thm 3): BB2 is (i) comb-generic; BB4 is (i);
BB1 concavity is (iii) REF-D. Residue BB5 is the only live item (OPEN).

## 6. Verdict
Identity 1 PROVED (trivial); concavity of λ(c) and monotonicity of Π in c PROVED; Identity 2 (squared EL, product and
quotient lags) PROVED modulo the regularity A h* ∈ L²(I_T) (CONDITIONAL); BB3 NO-GO PROVED; BB4 NO-GO PROVED at T = 1 by
certified falsifiers; BB5 OPEN (cross-prime lags N=p^iq^j, T>½log6). No sign obtained. Row D OPEN.
