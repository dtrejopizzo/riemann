# PROOF_L_SHARP_C_001 — Strategy C: the Mellin-multiplier viewpoint on L′♯

Phase 199, prover memo (pen and paper; no numerics). Target: **Lemma L′♯** (AUDIT_199): ∃κ>0, A≥0:
∀μ≥5, ∀g = Ef in the core, W_T(g) ≥ κμ^{−A}ℓ(g), ℓ(g) = inf{leak(f): Ef = g}. W_T is Paper 46's complete form
(eq:W, with the pole term 2Re(AB̄)). no equivalence of any
kind is invoked;

**Outcome in one line.** L′♯ is NOT proved. The brief's premise (ii) — "the zero sum vanishes identically and
W_T(Ef) reduces to archimedean + pole terms of ζ(s)f̃(s)" — is **false for the windowed function** (Prop 1.2): the
zero sum of Ef is transferred, not cancelled, to the exterior tail. The brief's premise (iii) — a representation
∫|f̃(½+it)|²ω(t)dt + pole terms — **cannot exist** for any locally integrable ω (Theorem 3.1). What the Mellin side
does give: the exact residual as an off-line multiplier form with −ζ′/ζ on Re s ∈ (1,2) (Theorem 2.1), the exact
comparison between leak(f) and the tail energy (Prop 4.1, one direction only, Prop 4.2), the exact Mellin algebra of
the falsifiers (§5), and a class NO-GO: every multiplier bound is TV-robust in the comb and is excluded by the
barrier (Theorem 6.1). The inequality that remains is stated exactly (§6) and is L′♯ itself on the exterior carrier.

## 0. Corpus check (rule ) and why this is not a retry
- **Index read.** README l.50 (coercivity walls), l.52 (N_018), l.160–164 (EI_002 Mellin expansion, symbol rigidity
  NO-GO), l.206 (abscissa transport 1→½ NO-GO), l.447 (C1 Guo identity), l.450 (MECH_001 + AUDIT_199), l.451
  (B_001), l.452 (A_001). 06_OPEN residues. Phase 170 exterior memos (R170_831/878: exterior Green formula, Möbius
  exterior loop — different object: the Tate predictor, not the summation map). Phase 163 R163_134 (Mellin torsion
  Γ-values — not this object).
- **Sources read.** MECH_001 §3–4, AUDIT_199 (gauge falsifier, L′♯, (d) F-DH), A_001 (Thm 1.1 half-line identity,
  Prop 2.1 gauge = radical, Thm 3.1 (L_ext), §3.2 Mellin truncation structure, Rem 3.3 on-line symbol, §6 Λ-table),
  B_001 (Lemma 4.1, Thm 4.2 barrier), D_001 (Sonin, not used), Guo §4 (Lemmas 4.2–4.4, Thm 4.5), §6 (Lemmas 6.1–6.2),
  (5.6) and the remark after it, §10.1; Paper 46 eq:symbol, eq:form, eq:W, lem:roughEF.
- **Not duplicated.** A_001 already proved W_T(Ef) = 𝒲_ext[Ψ_f] (quadratic form of Guo's Thm 4.5) and
  H_Ψ(s) = Σ_n n^{s−1}R_{nλ}(s). This memo takes those as CITED and does what A did not: (1) states the Mellin
  identity for the *windowed* function and what windowing does to the zero sum (Prop 1.1–1.2); (2) writes the
  residual as an **off-line** contour form with the multiplier −ζ′/ζ on a line of absolute convergence (Thm 2.1),
  which is a different object from A's on-line formal symbol; (3) proves that no on-line diagonal weight exists
  (Thm 3.1); (4) proves the one-directional comparison leak ≤ 18‖ℓ‖²_X/μ and its failure in the other direction
  (Props 4.1–4.2), which fixes the exact functional-analytic shape of L′♯; (5) gives the falsifier algebra in
  multiplier form (§5); (6) proves a class NO-GO for multiplier bounds (Thm 6.1). None of these is in the index.

## 1. The Mellin multiplier and what the window does

**Notation.** λ = e^T, μ = λ², I = (−T,T). Admissible f: real, even, f ∈ C²(ℝ), supp f ⊂ [−λ,λ], f(0) = f̂(0) = 0
(so f(λ) = f′(λ) = 0; the case f(λ) ≠ 0 is Guo's β-correction, A_001 Rem 1.1(iv), not needed here).
f̃(s) := ∫_0^λ f(t)t^{s−1}dt (Mellin on the half-line). Φ_f(x) := e^{x/2}Σ_{n≥1}f(ne^x), x ∈ ℝ; g := Φ_f·1_I = Ef;
ℓ := Φ_f·1_{(−∞,−T)} (exterior tail). For a function Ψ on ℝ, Φ_Ψ(s) := ∫Ψ(x)e^{(s−½)x}dx (Paper 46's Φ_F).
r := f̂·1_{|ξ|>λ}, leak(f) = ‖r‖² = 2∫_λ^∞|f̂|². H(u) := Σ_{n≥1}f(nu) = u^{−1/2}Φ_f(log u), u > 0.

**Proposition 1.1 (Mellin factorisation and the window split; PROVED).**
(a) Φ_f = 0 on [T,∞); |Φ_f(x)| ≤ 2C_f e^{3x/2} with C_f = (4π²)^{−1}∫|f″|; Φ_f is locally Lipschitz; and for all x,
 Φ_f(x) = e^{−x/2}Σ_{n≥1}f̂(ne^{−x})  (Poisson; Guo Lemma 4.3, CITED).
(b) Φ_{Φ_f}(s) = ζ(s)f̃(s) for Re s > −1 (Guo Lemma 4.4, "A Mellin identity", CITED): for Re s > 1 by termwise
 integration (∫|f(nu)|u^{σ−1}du = n^{−σ}∫|f|t^{σ−1}), then by continuation; f̃ is holomorphic on Re s > −2 (f = O(t²)
 at 0) and f̃(1) = ½f̂(0) = 0 cancels the pole of ζ. **On the Mellin side E is multiplication by ζ.**
(c) Window split: for Re s > −1,
 ζ(s)f̃(s) = Φ_g(s) + Φ_ℓ(s),  Φ_g(s) = ∫_{1/λ}^{λ}H(u)u^{s−1}du (entire),  Φ_ℓ(s) = ∫_0^{1/λ}H(u)u^{s−1}du.
 On u < 1/λ every n/u > λ, so by (a) H(u) = u^{−1}Σ_n r(n/u): **ℓ depends on f only through r** (Guo Rem 4.6(i)).
 In multiplier form (A_001 §3.2): Φ_ℓ(s) = Σ_{n≥1}n^{s−1}R_{nλ}(s), R_c(s) := ∫_c^∞ r(ξ)ξ^{−s}dξ.
(d) Support: Φ_f lives on (−∞,T]; the window I keeps [−T,T) and discards exactly the aliasing tail below −T.
 Restriction to |x| < T does nothing on the right (nothing is there) and cuts the Poisson tail on the left.
*Proof.* (a), (b) are Guo's lemmas, proofs read. (c): split ∫_0^λ = ∫_0^{1/λ} + ∫_{1/λ}^λ in Φ_{Φ_f}(s) =
∫_0^∞H(u)u^{s−1}du (H = 0 for u > λ); Φ_g is the Mellin transform of a bounded function on a compact subinterval of
(0,∞), hence entire; u = e^x converts to Φ_g, Φ_ℓ. (d) is (a). □

**Proposition 1.2 (what the zero sum does under windowing; PROVED).** For admissible f, g = Ef is in the C² core
and Paper 46 lem:roughEF applies:
 W_T(g) = Σ_ρ Φ_g(ρ)Φ_g(1−ρ) = Σ_ρ Φ_ℓ(ρ)Φ_ℓ(1−ρ),  absolutely convergent,
because Φ_g(ρ) = ζ(ρ)f̃(ρ) − Φ_ℓ(ρ) = −Φ_ℓ(ρ) for every nontrivial zero ρ (Prop 1.1(c); Φ_ℓ is holomorphic on
Re s > −1 ⊃ the strip). *The zero sum of the windowed function does not vanish; it equals the zero sum of the
exterior tail.* What vanishes is the full-line value W(Φ_f) = 0 (Guo Lemma 4.4), and W_T(g) = 𝒲_ext[ℓ] is its
quadratic shadow (A_001 Thm 1.1, CITED). □

**Correction to the brief (PROVED by Prop 1.2).** "W_T(Ef) reduces to archimedean + pole terms of ζ(s)f̃(s)" is
false: those terms are not even finite for Φ_f in the window form (Φ_f is not in L²(I)); for g the zero sum is
Σ_ρ|Φ_ℓ(ρ)|²-type and is exactly as unknown in sign as any zero sum. The ζ-specific fact "Mellin(E f) = ζ·f̃" is
used only to move the zero sum from g to ℓ. The whole content of L′♯ is therefore the full Weil form on the
half-line (−∞,−T) evaluated on aliasing tails (A_001 (L_ext)); the rest of this memo analyses that object on the
Mellin side.

## 2. The exact residual as an off-line multiplier form

**Theorem 2.1 (contour form of the residual; PROVED).** Let f be admissible and ℓ its exterior tail. Then Φ_ℓ is
holomorphic on Re s > −1, |Φ_ℓ(σ+it)| = O_σ(1/|t|) locally uniformly in σ, and for every σ ∈ (1,2)
 **W_T(Ef) = 𝒲_ext[ℓ] = (1/2π)∫_ℝ m(τ)|Φ_ℓ(½+iτ)|²dτ − (1/πi)∫_{Re s=σ}(−ζ′/ζ)(s) Φ_ℓ(s)Φ_ℓ(1−s) ds + 2Φ_ℓ(0)Φ_ℓ(1),**
with m(τ) = Re ψ(¼+iτ/2) − log π (Paper 46 eq:symbol). The three terms converge absolutely.
*Proof.* 𝒲_ext[ℓ] = (1/2π)∫m|ℓ̂|² − Σ_{q≥2}2c_q c_ℓ(log q) + 2A(ℓ)B(ℓ) with c_q = Λ(q)q^{−1/2}, c_ℓ(a) = ∫ℓ(y)ℓ(y−a)dy,
A(ℓ) = Φ_ℓ(1), B(ℓ) = Φ_ℓ(0) (A_001 §1; all prime powers q occur because ℓ has unbounded support to the left;
absolute convergence by |ℓ(y)| ≤ 2C_f e^{3y/2}). Holomorphy and the 1/|t| decay: ℓ e^{(σ−½)y} ∈ L¹∩L² for σ > −1,
ℓ is Lipschitz on (−∞,−T) with one jump at −T, so one integration by parts gives O(1/|t|). Mellin inversion
ℓ(y) = (2πi)^{−1}∫_{(σ)}Φ_ℓ(s)e^{−(s−½)y}ds (L² sense) and Plancherel on the line Re s = σ give, for −1 < σ < 2,
 c_ℓ(a) = (2πi)^{−1}∫_{(σ)}Φ_ℓ(s)Φ_ℓ(1−s)e^{−(s−½)a}ds
(both Φ_ℓ(s) and Φ_ℓ(1−s) are defined there; the integrand is O(|t|^{−2})). Insert a = log q, multiply by 2c_q, sum:
for σ > 1, Σ_qΛ(q)q^{−σ} < ∞, so Fubini applies and Σ_q 2c_q c_ℓ(log q) = (1/πi)∫_{(σ)}Φ_ℓ(s)Φ_ℓ(1−s)Σ_qΛ(q)q^{−s}ds,
and Σ_qΛ(q)q^{−s} = (−ζ′/ζ)(s). The archimedean term is the line Re s = ½ (ℓ̂(τ) = Φ_ℓ(½+iτ)); |m| = O(log) and
|Φ_ℓ|² = O(τ^{−2}) give convergence. □

**Remarks (PROVED / classical).**
(i) *Contour shift.* Moving the prime line from σ ∈ (1,2) to Re s = ½ crosses the pole s = 1 (residue
+Φ_ℓ(1)Φ_ℓ(0), which cancels the pole term) and the zeros ρ (residue −m_ρΦ_ℓ(ρ)Φ_ℓ(1−ρ)); on Re s = ½ the functional
equation gives (−ζ′/ζ)(s) + (−ζ′/ζ)(1−s) = −m(τ) off the zeros (A_001 Rem 3.3), so the remaining line integral
cancels the archimedean term. The result is Prop 1.2 again: W_T(Ef) = Σ_ρ Φ_ℓ(ρ)Φ_ℓ(1−ρ). The multiplier form of
Thm 2.1 is the *same number computed on a line where the comb converges absolutely*; nothing has been gained in
sign, but the form is now a genuine three-term expression with bounded, explicit multipliers.
(ii) *Where the brief's "weight ω built from ζ and Γ_ℝ" would sit.* On Re s = ½ the only pointwise symbol is
m(τ) + 2Re(ζ′/ζ)(½+iτ) = 0 off the zeros: the Weil distribution has no density there. Off the line the pairing is
Φ_ℓ(s)Φ_ℓ(1−s) = Φ_ℓ(σ+it)·\overline{Φ_ℓ(1−σ+it)}, a pairing of ℓ with itself across two different exponential
weights e^{±(σ−½)y}; it is not |·|² of anything, so no sign can be read off the multiplier (−ζ′/ζ)(σ+it), whose
real part is not even of one sign.
(iii) *Two-sided bound (TV-robust).* By Cauchy–Schwarz on the σ-line with σ = 3/2 and the support of ℓ in y < −T:
|prime term| ≤ 2(−ζ′/ζ)(3/2)·λ^{−1}‖ℓ‖_{L²}‖ℓ‖_{X}, ‖ℓ‖²_X := ∫e^{−2y}|ℓ|²dy (Guo's X_a norm); the archimedean term
is ≥ b_∞‖ℓ‖² and ≤ ∫(log(2+|τ|)+C_∞)|ℓ̂|²/2π; the pole term is ≤ 2λ^{−1/2}·(3λ³)^{−1/2}‖ℓ‖²_X-type (Guo Lemma 6.1).
This reproduces Guo's linear-in-amplitude estimate |W_T(Ef)| ≤ Cλ^k‖ℓ‖²_X-scale from the Mellin side; it is an
upper bound on |W_T(Ef)|, two-sided, and says nothing about the sign (Guo §10.1; Thm 6.1 below).

## 3. No on-line diagonal representation exists

**Theorem 3.1 (PROVED).** There is no locally integrable ω on ℝ such that, for every admissible f,
 W_T(Ef) = (1/2π)∫_ℝ|f̃(½+it)|²ω(t)dt + P(f),  P(f) := 2Re(A(Ef)\overline{B(Ef)})  (the pole term of Ef),
with the integral absolutely convergent. The same holds with P replaced by any quadratic form in finitely many
values of the Tate moments of Ef.
*Proof.* Dilate: f_a(t) := f(at), a > 1. Then f_a is admissible (support [−λ/a,λ/a], f_a(0) = 0,
f̂_a(0) = a^{−1}f̂(0) = 0) and f̃_a(s) = a^{−s}f̃(s), so |f̃_a(½+it)|² = a^{−1}|f̃(½+it)|². For a > μ the support of f_a
lies in (−1/λ,1/λ), so Ef_a = 0 (MECH Prop 3.1: ne^x ≥ 1/λ on I), hence W_T(Ef_a) = 0 and P(f_a) = 0. The assumed
identity at f_a gives (1/2π)∫|f̃|²ω = 0, and at f gives W_T(Ef) = P(f), i.e. 𝔞_T(Ef) = 0 for every admissible f.
By MECH Prop 3.1 (E is onto the C² core, AUDIT_199(c) checked) 𝔞_T would vanish on the core, which is false
(𝔞_T(g) ≥ ‖P_>g̃‖²·(λ+1) − K‖g‖² is unbounded above, A_001 Lemma 4.1; or directly s_T(τ) → ∞). □

So the brief's step (iii) has no object: the quadratic form f ↦ W_T(Ef) is **not diagonal in the Mellin variable**.
The reason is structural: dilation of f is translation of Φ_f (Ef_a = a^{−1/2}Φ_f(·+log a)|_I), and the window
breaks translation invariance; the only translation-invariant object is the full form W, whose on-line symbol is
zero (Rem 2.1(ii)). Everything in L′♯ is a window (truncation) effect, in the Mellin picture exactly as in A_001 §3.2.

## 4. Leakage against tail energy: the exact comparison (Paley–Wiener / Möbius)

Write w = e^{−y} > λ, H(w) = w^{−1/2}ℓ(−log w) = Σ_n r(nw), so ‖ℓ‖²_X = ∫_λ^∞ w²|H(w)|²dw and ‖ℓ‖²_{L²} = ∫_λ^∞|H|²dw.

**Proposition 4.1 (tail energy controls leakage; PROVED).** For admissible f,
 leak(f) = 2‖r‖²_{L²(λ,∞)} ≤ 18 μ^{−1}‖ℓ_f‖²_X.
*Proof.* |r(ξ)| ≤ C_fξ^{−2} (Guo Lemma 4.3), so H(w) = O(w^{−2}) and the Möbius inversion r(w) = Σ_mμ(m)H(mw), w > λ,
converges absolutely (Σ_kH... = Σ_k r(kw)Σ_{m|k}μ(m) = r(w)). Then ‖r‖_{L²(λ,∞)} ≤ Σ_m‖H(m·)‖_{L²(λ,∞)} =
Σ_m m^{−1/2}‖H‖_{L²(mλ,∞)} ≤ Σ_m m^{−1/2}(mλ)^{−1}‖wH‖_{L²(mλ,∞)} ≤ ζ(3/2)λ^{−1}‖ℓ‖_X, and ζ(3/2) < 3. □

**Proposition 4.2 (leakage does not control tail energy; PROVED).** The summation map r ↦ H = Σ_n r(n·) on (λ,∞)
is not bounded, nor everywhere defined, on L²(λ,∞): r_ε(ξ) = ξ^{−1/2−ε}1_{ξ>λ}, 0 < ε < ½, has ‖r_ε‖² = λ^{−2ε}/(2ε) < ∞
and H(w) = w^{−1/2−ε}Σ_n n^{−1/2−ε} = ∞. It is bounded from L²((λ,∞), ξ^αdξ) for every α > 1 (A_001 §5, Guo Lemma
6.2 for α = 2), and Guo notes after (5.6) that the α = 2 norm is not controlled by ‖r‖. No finite-loss inequality
‖ℓ_f‖_X ≤ C(μ)·leak(f)^{1/2} holds on the admissible class (take f whose out-of-band part approximates r_ε on a long
range; the C² class is dense enough since only the ξ^{−1/2−ε} profile on [λ, R] is needed and R → ∞). □

**Corollary 4.3 (the exact shape of L′♯; PROVED).** Let 𝓡 = {Φ_φ : φ gauge} be the radical subspace (A_001 Prop
2.1) and for a tail ℓ put N_X(ℓ) := inf_{d∈𝓡}‖ℓ + d‖_X. Then
 (R_X)  𝒲_ext[ℓ_f] ≥ c(μ) N_X(ℓ_f)²  for all admissible f   ⟹   L′♯ with κμ^{−A} = c(μ)μ/18,
because 𝒲_ext[ℓ_f + d] = 𝒲_ext[ℓ_f] and leak(f+φ) ≤ 18‖ℓ_f + Φ_φ‖²_X/μ for every gauge φ (Prop 4.1 applied to f+φ).
The converse implication fails as a norm statement (Prop 4.2): L′♯ bounds the form below by the *weaker* functional
leak = dist²(r,𝒢̄), which is why it is consistent with Guo's upper bound |𝒲_ext[ℓ]| ≤ Cλ^k‖ℓ‖_X·‖g‖ (linear in the
amplitude; Guo Thm 1.6 + Lemma 4.1 there) for every A ≥ 0. The Paley–Wiener input (f̂ entire of exponential type λ,
f ∈ C² ⇒ |f̂| ≤ C_fξ^{−2}) enters only through the α-weighted norms; it is what makes ℓ_f finite in X, not what
gives a sign.

## 5. Where Λ is used, in multiplier form (falsifiers)

Let a ≥ 0 be a comb on prime powers with Dirichlet series D_a(s) = Σ_q a(q)q^{−s} (= −L_a′/L_a for the formal Euler
product L_a), and W^{(a)}_T the window form with comb a (same archimedean and pole data as ζ).

**Proposition 5.1 (same E, other comb; PROVED).** For admissible f and 1 < σ < 2,
 W^{(a)}_T(Ef) = W_T(Ef) − (1/πi)∫_{(σ)}[D_a(s) − (−ζ′/ζ)(s)]Φ_g(s)Φ_g(1−s)ds,  g = Ef,
the extra term being a quadratic form in g of size O(‖D_{a−Λ}(σ)‖·‖g‖²), not of tail size. *Proof.* Thm 2.1's
derivation applied to the compactly supported g (its Mellin transform is entire; for q ≥ μ the correlation
c_g(log q) vanishes identically, so the full Dirichlet series may be used). □
So for cΛ, a_P, Beurling the identity W^{(a)}_T(Ef) = 𝒲^{(a)}_ext[ℓ] is **false**: the full-line value W^{(a)}(Φ_f)
= −(1/πi)∫D_{a−Λ}Φ_{Φ_f}Φ_{Φ_f}(1−·) ≠ 0 (MECH §4, A_001 §6, now in multiplier form).

**Proposition 5.2 (adapted E, other comb; PROVED).** Let E_a f(x) := e^{x/2}Σ_n d_a(n)f(ne^x) with d_a the Dirichlet
coefficients of L_a (for cΛ: L_a = ζ^c, d_c = c-fold divisor function; for a_P: L_a = ζΠ_{p∈P}(1−p^{−s}),
d_a = 1_{P-free}). Then Mellin(Φ^{(a)}_f) = L_a(s)f̃(s) vanishes at every zero of ζ (c-fold, resp. simply), but
 W^{(cΛ)}(F) = c·Σ_ρΦ_F(ρ)Φ_F(1−ρ) − (c−1)[𝔞_∞(F) + 2Re(A\overline{B})(F)],
 W^{(a_P)}(F) = Σ_ρΦ_F(ρ)Φ_F(1−ρ) − Σ_{p∈P,k≥1}2Λ(p^k)p^{−k/2}c_F(k log p),
for every test F for which the explicit formula holds (write the comb term as (arch + pole − zero sum) by the
explicit formula). Hence W^{(cΛ)}(Φ^{(c)}_f) = −(c−1)[𝔞_∞ + pole](Φ^{(c)}_f) ≠ 0 and W^{(a_P)}(Φ^{(P)}_f) =
−(deleted prime terms) ≠ 0: *the vanishing of the zero sum is available for every Dirichlet series, but the
residual identity "window form = exterior form" needs the comb to be the log-derivative of the same function whose
archimedean and pole data the form carries, i.e. L_a = ζ.* (For cΛ there is the additional additive failure:
Σ_nd_c(n)f(nu) has no Poisson cancellation, A_001 §6.) □

**F-DH.** AUDIT_199(d): the conductor-5 analogue of Prop 1.1(b) and of the half-line identity holds (CITED, ARGUED
there) with its own archimedean kernel and no pole; so by §2–§4 the F-DH exterior form is as explicit as ζ's, and
negative at a = 9/5 (CITED Ziad, UNVERIFIED). Therefore nothing in §1–§4 (identity, multiplier form, non-diagonality,
leak comparison) is ζ-specific beyond "L_a = ζ": the ζ-specific content of L′♯ is the sign of 𝒲_ext on tails, which
must use what F-DH lacks (pole / conductor 1 / Λ ≥ 0 on prime powers; AUDIT_199(d), A_001 §6).

## 6. The inequality that remains, and a class NO-GO for Strategy C

**The remaining inequality (OPEN; = L′♯ verbatim by A_001 Thm 3.1).** For all μ ≥ 5 and admissible f, with
Φ_ℓ(s) = Σ_n n^{s−1}R_{nλ}(s) and any σ ∈ (1,2):
 (R_C)  (1/2π)∫m(τ)|Φ_ℓ(½+iτ)|²dτ − (1/πi)∫_{(σ)}(−ζ′/ζ)(s)Φ_ℓ(s)Φ_ℓ(1−s)ds + 2Φ_ℓ(0)Φ_ℓ(1) ≥ κμ^{−A}·dist²(r_f,𝒢̄).
It is **not comb-generic**: for cΛ (c > 1) the left side is the exterior form of a comb whose window form is
certified negative (CERT_FALSIFIERS, CITED), and by Prop 5.1 the exterior form with comb cΛ differs from
W^{(cΛ)}_T(Ef) by a term that is not of tail size, so (R_C) for cΛ is a different, false, statement. Good: the
remaining inequality is Λ-exact, as required by the brief. Sufficient: (R_X) of Cor 4.3 with c(μ) polynomial.

**Theorem 6.1 (class NO-GO for multiplier bounds; PROVED given B_001 Thm 4.2 / BARRIER_EST Thm 4, CITED).** Let 𝒫
be a proof of (R_C), or of its sign version, in which the comb enters only through bounds on its multiplier on
lines Re s = σ > 1 (|D_a(σ+it)| ≤ D_a(σ), ‖D_{a−Λ}(σ+i·)‖_∞ ≤ Σ|a−Λ|(q)q^{−σ}, Schur/Cauchy–Schwarz/Plancherel on
the lines), together with comb-independent facts (m, Γ_ℝ, Paley–Wiener, Möbius, the identity of Thm 2.1). Then 𝒫
cannot exist at any μ ≥ 5. *Proof.* Every such bound holds uniformly for combs a with Σ|a−Λ|(q)q^{−σ} ≤ r, hence on
a TV-ball of radius r(μ) around Λ independent of the zero data; B_001 Lemma 4.1 (the complete form is of the shape
𝒜 − ∫c dν) gives a comb ν′ at TV-distance ≤ ½(1+ε)λ^W_T with W^{(ν′)}_T negative at the bottom vector, and λ^W_T ≤
κ₊μ^{9/2}e^{−4πμ} (rem:moriceiling, CITED) while any multiplier bound has slack ≥ a fixed power of μ^{−1} times
constants; so 𝒫 would prove the sign for a comb for which it is false. □
In words: on Re s = σ > 1 the comb is a bounded function whose TV-perturbations are uniformly small, so the
Mellin-multiplier picture is *exactly* the TV-robust class the barrier excludes. The sign of (R_C) must come from
the truncation at ξ = nλ in Φ_ℓ(s) = Σ_n n^{s−1}R_{nλ}(s) — the boundary n ≈ λ/u where the lattice (Poisson) and the
monoid (Möbius, ζ) act on the same integers (semiring principle; A_001 Rem 3.3) — and not from any bound on the
multipliers. This memo does not supply that sign.

## 7. Labels and verdict
- **PROVED:** Prop 1.1(c)(d), Prop 1.2 (zero sum transferred, not cancelled), Thm 2.1 (off-line multiplier form),
  Rem 2.1(i)–(iii), Thm 3.1 (no diagonal weight), Prop 4.1 (leak ≤ 18‖ℓ‖²_X/μ), Prop 4.2 (no converse), Cor 4.3
  ((R_X) ⟹ L′♯), Prop 5.1, Prop 5.2, Thm 6.1 (given the CITED ceiling).
- **CITED:** Guo Lemmas 4.3–4.4, Thm 4.5, Lemmas 6.1–6.2, (5.6); A_001 Thm 1.1, Prop 2.1, Thm 3.1, Rem 3.3,
  Lemma 4.1; B_001 Lemma 4.1, Thm 4.2; Paper 46 eq:W, lem:roughEF, rem:moriceiling; CERT_FALSIFIERS; AUDIT_199(d).
- **ARGUED:** the density step in Prop 4.2's last sentence (the explicit example r_ε is PROVED).
- **NO-GO (class, PROVED):** Strategy C as "bound the Mellin multipliers and compare with leak by Paley–Wiener":
  excluded by Thm 6.1. The brief's steps (ii) and (iii) are false as formulated (Prop 1.2, Thm 3.1).
- **OPEN:** (R_C) = L′♯; (R_X). No sign is claimed. Row D OPEN.

**Verdict.** The Mellin-multiplier viewpoint is exact and clarifying — E is multiplication by ζ, the window moves the
zero sum to the exterior tail, the residual is an explicit three-term form with −ζ′/ζ on a line of absolute
convergence, and leak is dominated by the tail energy but not conversely — but it contains no sign source: the on-line
symbol is zero, the off-line pairing is not a square, and every multiplier estimate is TV-robust. L′♯ is not proved
here. Do not retry "Mellin multiplier bounds + Paley–Wiener loss" as a route to L′♯.
