# R162_790 — Audit, round 6 (R162_501, R162_502, R162_504)

Referee pass, line by line. Checked against Paper 47 main.tex: eq:symbol and eq:form
(s_T = m − Σ_{n∈N_T} v_n cos(τ log n), v_n = 2Λ(n)/√n, N_T = {log n < 2T}, 𝔞_T = (1/2π)∫s_T|F̂|²,
F̂(τ) = ∫F e^{iτt}, c_F(u) = ∫F(t)F̄(t−u)), the operator A_T (archimedean multiplier minus
Σ w_n(S_{log n}+S_{−log n}), w_n = v_n/2, compressed to I_T), P_T = ker A ∩ ker B, eq:W, def:W/eq:nuw
(only for conventions), thm:parityschur (o),(a),(b), eq:localweak, and R162_407 (3.1)/(REG).
No numerics. No commits.

## Verdict table

| item | verdict |
|---|---|
| R162_501 Lemma 2.1 (Selberg identity, W1–W3, DH analogue, E_a) | CORRECT |
| R162_501 Lemma 1.1, Lemma 1.2 (used by 2.2) | CORRECT WITH FIXES (analytic hypothesis) |
| R162_501 Thm 2.2 (Selberg–virial identity) | CORRECT WITH FIXES (algebra right; hypotheses, boundary term, λ≠0 sign) |
| R162_502 B1 (a)–(d) | CORRECT |
| R162_502 B2 (B2.1), (B2.2), (B2.3), (B2.4), (B2.5) | CORRECT WITH FIXES (definition of 𝔞^∞; "on P_T" should be "on L²(I_T)") |
| R162_502 B3 classification / Prop B3 | CORRECT WITH FIXES: downgrade to meta-classification, not a theorem |
| R162_502 A5 support-hull minimality lemma | CORRECT WITH FIXES (conclusion right, stated reason wrong) |
| R162_504 Thm 1 (Perron–Frobenius) | CORRECT WITH FIXES (Lévy–Khintchine kernel correct; sign/simplicity correct; the strict-positivity step as written is not a proof) |
| R162_504 Thm 2 (parity ladder) | CORRECT |
| R162_504 Thm 3 (first-contact dichotomy) | CORRECT WITH FIXES ("0 ∉ spec A^par" in Type II is not proved and not needed) |

No item is WRONG. No sign is claimed anywhere and none follows; the NO-GO verdicts of all three files stand.

---

## 1. R162_501

### Lemma 2.1 — CORRECT
- Derivation (f*g)log = (f log)*g + f*(g log); from Λ*1 = log: (Λlog)*1 + Λ*log = log², and
  Λ*log = Λ*Λ*1; Möbius gives Λlog + Λ*Λ = μ*log². Checked.
- (W3): μ*log²(p^k) = (k²−(k−1)²)log²p = (2k−1)log²p. For n = p^iq^j with a = log p, b = log q, L = log n:
  L² − (L−a)² − (L−b)² + (L−a−b)² = 2ab. Checked. (W2): μ*log^k vanishes for ω(n) > k. (W1) follows.
- General a: μ*((a*1)log) = a·log + a*Λ, so E_a = a*(a−Λ); since the Dirichlet ring is a domain, E_a = 0 iff
  a ∈ {0, Λ}, i.e. iff a*1 = log (for a ≠ 0). Consistent with the text; the file should write E_a = a*(a−Λ)
  explicitly (cosmetic).
- DH analogue: c*α = α·log ⇒ (c·log + c*c)*α = α·log², so W_DH = α^{−1}*(α log²); W_DH(p) = α(p)log²p = c(p)log p.
  Checked.
- F3 line: W_{Λ+η} = W + η log + 2Λ*η + η*η ≥ 0 for η ≥ 0. Checked.

### Lemma 1.1 / 1.2 — CORRECT WITH FIXES
- With Paper 47's conventions, (1/2π)∫cos(τu)|Ĝ|² = c_G(u) for real G, hence c_G'(u) = −(1/2π)∫τ sin(τu)|Ĝ|²,
  z' = −Σ v_n log n sin(τ log n), and the comb term of R162_407 (3.1) equals −(1/2π)∫τ z'|Ĝ|². Matches (3.1).
- Lemma 1.2: τ d/dτ = y d/dy, and d/dy[−(k+¼)/((k+¼)²+y²)] = 2y(k+¼)/((k+¼)²+y²)². Series correct; positivity,
  boundedness and the limit 1 (Riemann sum of ∫_0^∞2y²x/(x²+y²)²dx = 1) correct.
- **Fix L1.** (REG) of R162_407 is local near the comb points (C¹ of c_G there). It does **not** give
  ∫|τ||Ĝ|² < ∞. A first-contact vector with nonzero edge germ G(±T_*∓) ≠ 0 has |Ĝ(τ)|² ≍ τ^{−2}, so τ sin(τu)|Ĝ|²
  is only conditionally integrable. State: "all τ-integrals are improper, lim_{R→∞}∫_{−R}^{R}", and add
  (REG⁺) below where absolute convergence is used.

### Theorem 2.2 — CORRECT WITH FIXES
Algebra, step by step:
- Step 1: dz_c/dτ = −iΣΛ(n)log n·n^{−1/2−iτ}. Correct.
- Step 2: for n < X all divisors are < X, so Σ_{n<X}(Λ*Λ)(n)n^{−1/2−iτ} = z_c² − R_X. Correct.
- Step 3: Re(−iw) = Im w gives z' = 2Im Y − 2Im(z_c²) + 2Im R_X, and Im(z_c²) = 2Re z_c·Im z_c = z·Im z_c. Correct.
- Step 5: the Fourier transform of (M−Z)G = r_G + h_G is (m−z)Ĝ = r̂_G + ĥ_G. Substitution gives exactly the
  third and fourth lines of (2.1), with the prefactor 1/π. Correct; the Re is harmless because the total and the
  m-term are real.
- Step 6 / (2.3): Im Y = −ΣW(n)n^{−1/2}sin(τ log n) gives −(1/π)∫τ Im Y|Ĝ|² = −2ΣW(n)n^{−1/2}c_G'(log n). Correct.

Fixes:
- **Fix V1 (boundary term).** Step 4 says that when X = e^{2T_*} is an integer, the term from mk = X "is kept
  inside ĥ_G". That is false by definition: h_G = 1_{ℝ∖I}(M−Z)G does not contain R_X. Also c_G is generally
  not differentiable at u = 2T_* (the left derivative is −G(T_*−)G(−T_*+), the right derivative is 0). Replace it
  by an explicit term
  B_X(G) := −2 Σ_{m,k<X, mk=X} Λ(m)Λ(k)X^{−1/2}·c_G'(2T_*−)·(convention factor ½ if the improper integral
  gives the mean of the one-sided derivatives),
  added to (2.1). It vanishes if X ∉ ℕ, or under the R162_408 Prop 4.1 hypothesis. It is not a sign, so the
  NO-GO is unaffected.
- **Fix V2 (REG⁺).** Add as hypothesis: ∫|τ|log(2+|τ|)|Ĝ|² < ∞, or the improper-integral reading of Fix L1, and
  ∫|τ||Ĝ||r̂_G + ĥ_G| < ∞ (for example ĥ_G ∈ L¹). Without this the fourth line of (2.1) is not defined: r̂_G decays
  only like 1/τ, and h_G has at most a log singularity at ∂I, which makes it L² but not obviously gives ĥ_G ∈ L¹.
- **Fix V3 (sign).** For eigenvectors with (M−Z)G = λG + r + h, the substitution gives −(λ/π)∫τ Im z_c|Ĝ|², not
  +(λ/π)∫…. The F1 conclusion ("additive only") is unchanged.
- Prop 3.1(d) is labelled "sketch, NOT fully checked". It must stay out of the PROVED list (it is). Accepted as
  heuristic only.

---

## 2. R162_502

### B1 — CORRECT
- (a) (Pτ_aPτ_bPF)(t) = 1_I(t)1_I(t+a)1_I(t+a+b)F(t+a+b), and convexity for a, b ≥ 0 gives Pτ_aPτ_bP = Pτ_{a+b}P.
  Terms with log(mk) ≥ 2T vanish on both sides, because a shift by ≥ 2T maps L²(I) to functions vanishing on I.
  M_T(1) and M_T(μ) are automatically finite sums (n < X). Correct.
- (b) (Xτ_c − τ_cX)F(t) = tF(t+c) − (t+c)F(t+c) = −cτ_cF. Correct.
- (c) M_T(1)M_T(μ) = M_T(δ_1) = P = Id_{L²(I)}, and likewise in the other order. Correct.
- (d) is the definition. With c_F(u) = ∫F(t)F(t+u), which equals Paper 47's c_F for real F (it is even). Correct.

### B2 — CORRECT WITH FIXES
- (B2.1): M_T(Λ)Z = M_T(Λ*1) = M_T(log) = −[X,Z], so M_T(Λ) = −(XZ−ZX)Z^{−1} = ZXZ^{−1} − X. Correct.
- The identity is invariant under X → X+T. S² = X+T ≥ 0 on I_T and S is bounded (‖S‖ ≤ √(2T)). Correct.
- (B2.2): ⟨F,M_T(Λ)F⟩ = ⟨F,ZS²Z^{−1}F⟩ − ‖SF‖² = ⟨SZ*F, SZ^{−1}F⟩ − ‖SF‖², and the polarisation
  4⟨a,b⟩ = ‖a+b‖² − ‖a−b‖² (real F). Correct.
- (B2.3): the prime side of eq:form is −Σ_{N_T}v_n c_F(log n) = −2Σ Λ(n)n^{−1/2}c_F(log n) = −2⟨F,M_T(Λ)F⟩. Correct.
- (B2.5): the operator of the quadratic form −2⟨F,M_T(Λ)F⟩ is −(M_T(Λ) + M_T(Λ)*) = −(ZXZ^{−1} + Z^{−*}XZ* − 2X), and
  eq:localweak gives A_TF = r ∈ Tate space. Hence A^∞F = ZXZ^{−1}F + Z^{−*}XZ*F − 2XF + r. Correct.
- **Fix H1.** "𝔞_T^∞ is everything except the prime side (archimedean, collar and Tate endpoint terms)" is wrong
  against eq:form, which has **no** collar or Tate endpoint terms. It should read
  𝔞_T^∞(F) = (1/2π)∫m|F̂|² (archimedean form only), and A^∞ = its operator compressed to I_T.
- **Fix H2.** (B2.3) holds on all of L²(I_T) (form domain), not only on P_T. Primitivity is used only in (B2.4)–(B2.5).
- **Fix H3.** The "reading" (aligned/misaligned squares, "would vanish if |ζ| = 1") is interpretation. Z is
  unipotent (identity plus strictly causal part), so Z* = Z^{−1} forces Z = I. Label it heuristic.

### B3 / Prop B3 — CORRECT WITH FIXES (downgrade)
- B1–B2 are formal in (a, b) with b*a = a·log and a(1) ≠ 0. Checked, including for real Beurling integers
  (the convexity argument uses only nonnegative shifts).
- **Fix H4.** "The estimates that can distinguish Z are exactly these" is an enumeration, not a theorem. No
  exhaustiveness proof is possible. Relabel as "classification of the inputs considered (meta-level)".
- **Fix H5.** Prop B3 asserts that Λχ₂ (with ζ's archimedean data) and a Beurling DMV system with ζ's m both have
  primitive first contacts. That is not proved in the file. For the Beurling system with m fixed it needs (i) that
  off-line zeros force λ_A(T) < 0 for some T in this mixed model (no explicit formula links m to the Beurling zeros),
  and (ii) continuity of λ_A (Paper 47 lem:contA transfers, since it uses only the finite comb). State (i) as a
  hypothesis or give a direct negative test. Without it, Prop B3 is conditional.
- **Fix H6 (stronger, simpler).** Row (iii): every 0 ≠ F ∈ P_T changes sign, because A(F) = ∫F e^{t/2} = 0 with
  e^{t/2} > 0. So the restriction to "ε = −1 kernels" is unnecessary.

### A5 support-hull minimality — CORRECT WITH FIXES
- **The stated reason is wrong.** "The primitive constraints depend only on c_F" is false: A(F), B(F) are linear in F.
  The correct reason is that translation F ↦ F(·−s) multiplies A(F) by e^{s/2} and B(F) by e^{−s/2}. So
  {A = B = 0} is translation invariant, while 𝔞 depends only on c_F. The form domain is translation invariant too.
- Correct proof: extension by zero embeds P_{T'} in P_T for T' < T, and 𝔞_T = 𝔞_{T'} there (contacts with
  log n ≥ 2T' see c_F = 0). So λ_A is nonincreasing. If F ∈ N had hull length L < 2T_0, a translate lies in
  P_{L/2} with 𝔞 = 0, so λ_A(L/2) ≤ 0, which contradicts the minimality of T_0. This requires T_0 to be defined as
  inf{T : λ_A(T) ≤ 0} (equivalently the first zero, with λ_A > 0 before it). Say this explicitly.

---

## 3. R162_504

### Theorem 1 (Perron–Frobenius) — CORRECT WITH FIXES
- (i) Lévy–Khintchine. From ψ(z) = ∫_0^∞(e^{−x}/x − e^{−zx}/(1−e^{−x}))dx:
  Re ψ(a+iy) − ψ(a) = ∫_0^∞ e^{−ax}(1−cos xy)/(1−e^{−x})dx. With a = ¼, y = τ/2, x = 2u (dx = 2du):
  m(τ) − m(0) = ∫_0^∞ 2e^{−u/2}(1−cos τu)/(1−e^{−2u})du = ∫_ℝ(1−cos τu)k(u)du, k(u) = e^{−|u|/2}/(1−e^{−2|u|}) > 0.
  **Checked.** k ~ 1/(2|u|) at 0 (non-integrable, which is fine against 1−cos), and k ~ e^{−|u|/2} at ∞.
  m(0) = ψ(¼) − log π ≈ −5.372, consistent with Paper 47 (line ≈2067).
- (ii) Beurling–Deny. (1/2π)∫(m−m(0))|F̂|² = ∫k(u)(‖F‖² − c_F(u))du = ½∬_{ℝ²}(F(t)−F(s))²k(t−s). This includes the
  killing part t ∈ I, s ∉ I. Checked.
- (iii) Checked. The defect is in fact ≥ 4∬F_+(t)F_−(s)k(t−s) (the file writes 2, which is weaker but true). The
  comb uses c_{|F|} ≥ c_F and v_n ≥ 0. The form domain is closed under |·| (normal contraction of a jump form).
- (iv) "Every real ground state has a sign" and simplicity (orthogonal nonnegative ground states have disjoint
  supports, so their difference is a sign-changing ground state): **correct**. Real parts suffice, because A_T is a
  real operator. The bottom is attained because of the compact resolvent (m ~ log|τ| and I bounded; the comb is a
  finite sum of bounded shifts).
- **Fix P1 (strict positivity).** The argument "0 ≤ G ∈ C_c^∞ supported where ψ vanishes" is invalid: the zero set
  of ψ is only measurable and need not contain an interval. The expression written is also not an argument. Replace
  it with this:
  (1) e^{−sA^0} is positivity preserving (Beurling–Deny: the form 𝔞^0 = m(0)‖F‖² + jump form is invariant under
  normal contractions up to the constant m(0)).
  (2) It is irreducible (ergodic): a closed invariant ideal L²(E) forces ∬_{E×(I∖E)}k = 0, hence |E| = 0 or
  |I∖E| = 0, since k > 0.
  (3) C = Σw_n(S_{log n}+S_{−log n}) compressed is bounded and positivity preserving. Dyson/Trotter gives
  e^{−s(A^0−C)} ≥ e^{−sA^0} ≥ 0 in the lattice sense, so e^{−sA_T} is positivity preserving and irreducible.
  (4) Reed–Simon IV Thm XIII.44 (positivity preserving + ergodic ⟺ simple bottom with a strictly positive
  eigenvector) then gives ψ_T > 0 a.e. Positivity *improving* is not needed.
  Alternatively, an Euler–Lagrange argument: with E = {ψ = 0}, |E| > 0, test against G = 1_{E∩K}·χ for a suitable
  form-domain truncation. This is more delicate (1_E need not be in the log-form domain), so use the semigroup route.
- (v) J commutes with A_T (m even, symmetric comb, symmetric I); the simple eigenvector is J-invariant, and positive
  implies even. Correct.
- DH/F3 lines: accurate (DH does have zeros in σ > 1; the sign-changing comb breaks (iii)).

### Theorem 2 — CORRECT
- (a) The ground state is even and simple ⇒ odd spectrum ⊂ [μ_2,∞). P^odd = ker ℓ_odd ∩ odd sector (for odd F,
  A(F) = ℓ_odd(F) = −B(F)). A codimension-one compression raises the bottom. Checked.
- (b) Interlacing on ker ℓ_ev (for even F, A = B = ℓ_ev). Strictness: an attaining minimiser with value μ_1 would be
  ∝ ψ_T, but ⟨ψ_T, φ_ev⟩ > 0. Checked (the compression also has compact resolvent, so the bottom is attained).
- λ_A ≥ min(λ_ev, μ_2) follows from thm:parityschur(o). Checked.
- Cor 2.1 (not in the audit list): the signs 2AB = +2ℓ_ev² (even) and −2ℓ_odd² (odd) agree with thm:parityschur(o).
  Correct.

### Theorem 3 — CORRECT WITH FIXES
- r ∈ (P_T)^⊥ ∩ parity sector = ℝφ_par: from eq:localweak. Type I ⟺ r = 0 ⟺ α(F) = 0 in thm:parityschur(b)
  (there a(F,G) = α(F)ℓ(G), so α = c). Checked. The eigenvalue bookkeeping (0 > μ_1 even, 0 ≥ μ_1^odd ≥ μ_2 > μ_1 odd)
  is checked.
- **Fix P2.** Type II: the argument shows only that every E ∈ ker A^par satisfies E ⊥ φ_par. It does **not**
  show 0 ∉ spec A^par. Correct statement:
  F = c(A^par)^+φ_par + E, with E ∈ ker A^par ∩ ker ℓ_par ((A^par)^+ the reduced inverse), ℓ(F) = c f^red_par(0) = 0.
  Here f^red is the reduced Weinstein–Aronszajn function. If ker A^par ≠ 0, then E is itself a Type I contact vector.
  The W-statement W F = cφ, α = c ≠ 0 ⇒ λ_W < 0 (thm:parityschur(b)) is unaffected.
- "Odd contact ⇒ μ_2 ≤ 0" and "even contact ⇒ μ_2^ev ≥ 0, μ_1 < 0": checked.
- Prop 4.1 and 4.3 (not in the list): the statement of 4.3 is checked. For 4.1, f_odd(0) > 0 needs μ_1^odd > 0, which
  follows from μ_2 > 0. Fine.

---

## 4. Net effect on the record
- Labels after fixes: 501 Lemma 2.1 PROVED; Thm 2.2 PROVED under (REG)+(REG⁺), with the boundary term B_X.
  502 B1, B2 PROVED (with H1, H2); B3 = meta-classification, conditional on H5; A5 PROVED with the corrected reason.
  504 Thms 1–3 PROVED with P1, P2.
- No fix creates or removes a sign. The NO-GO verdicts (Gate 1 OPEN, row D OPEN) stand.
- Process note: H1 is exactly the kind of drift to watch for. R162_501 described 𝔞^∞ with
  terms that eq:form does not have.
