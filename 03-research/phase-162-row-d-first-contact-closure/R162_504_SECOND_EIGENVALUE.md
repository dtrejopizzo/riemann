# R162_504 — Route D5: the second eigenvalue of A_T at first contact

Route D5 of R160_010 (never written before; R162_590 §2 item 3).
**Status: PARTIAL.** Structural theorems PROVED (Thms 1–4). The sign mechanism is **NO-GO** (§5): the
second-eigenvalue target is RH restated (E1), the rank-2 Tate correction is exactly the polar term of
Paper 47 (restatement of thm:parityschur / prop:polarcap in resolvent language), and the only step that
uses the Euler product is Λ ≥ 0, which is DH-failing but blind to finite modifications a ≥ 0 (F3).
No sign is claimed.

Notation (Paper 47): a_T = eq:form, operator A_T on L²(I_T), P_T = ker A ∩ ker B,
φ_ev = cosh(t/2)1_{I_T}, φ_odd = sinh(t/2)1_{I_T}, ℓ_par = ⟨·,φ_par⟩, W_T = a_T + 2AB.
μ_1 ≤ μ_2 ≤ … eigenvalues of A_T on L²(I_T) (compact resolvent, Paper 47 thm:parityschur proof);
μ_k^par the same on the parity sector.

## 1. Corpus check

- The rank-2 correction relating the unconstrained and the complete form is W_T − a_T = 2AB =
  2(ℓ_ev² − ℓ_odd²) (thm:parityschur(o)). The Schur complement over P_T is S^Sch = diag(a_T(h_ev), a_T(h_odd))
  and 𝔊_T = S^Sch + diag(2,−2) (prop:polarcap). Everything in §4 below is these two statements rewritten
  through the Weinstein–Aronszajn function; it is recorded as such, not as new content.
- New here: the Perron–Frobenius structure of A_T (Thm 1) and its consequences for the parity ladder
  (Thm 2), the first-contact type dichotomy (Thm 3), the alignment bound (Prop 4.3). Not in phases 150–162.

## 2. Theorem 1 (Perron–Frobenius for A_T) — PROVED

**Theorem 1.** For every T>0 the bottom μ_1(T) of A_T is a simple eigenvalue, with an eigenfunction ψ_T
that is even and satisfies ψ_T > 0 a.e. on I_T.

*Proof.* (i) Lévy–Khintchine form of the Gamma symbol. From ψ(z) = ∫_0^∞(e^{-x}/x − e^{-zx}/(1−e^{-x}))dx,
Re ψ(a+iy) − ψ(a) = ∫_0^∞ e^{-ax}(1−cos xy)(1−e^{-x})^{-1}dx. With a=¼, y=τ/2, x=2|u| and symmetrisation,
  m(τ) = m(0) + ∫_R (1−cos τu) k(u) du,  k(u) = e^{-|u|/2}/(1−e^{-2|u|}) > 0 for all u ≠ 0.
(ii) Beurling–Deny. For real F in the form domain (extended by zero),
  a_T(F) = m(0)‖F‖² + ½∬_{R²}(F(t)−F(s))² k(t−s) dt ds − Σ_{n∈N_T} v_n c_F(log n),
and c_F(log n) = ∫F(t)F(t−log n)dt. (iii) Replace F by |F|: the jump term does not increase
(||F(t)|−|F(s)|| ≤ |F(t)−F(s)|), and since **v_n ≥ 0** the comb term does not increase
(−v_n c_{|F|} ≤ −v_n c_F). So a_T(|F|) ≤ a_T(F), with a defect
  a_T(F) − a_T(|F|) ≥ 2∬ F_+(t)F_−(s) k(t−s) dt ds.
(iv) If ψ is a real minimiser, |ψ| is one too, so the defect vanishes; since k > 0 everywhere this forces
F_+ = 0 or F_− = 0 a.e.: every real ground state has a sign. Two orthogonal ground states of one sign have
disjoint supports and their difference is a ground state without a sign; hence μ_1 is simple. Strict
positivity: for ψ ≥ 0 a ground state and 0 ≤ G ∈ C_c^∞ supported where ψ vanishes on a set of positive
measure, a_T(ψ,G) = −∬ψ(s)G(t)k(t−s) − Σ v_n⟨ψ(·−log n)+ψ(·+log n),G⟩/2·… < 0 while μ_1⟨ψ,G⟩ = 0 would be
required at every density point; the standard form of this step is Reed–Simon IV, Thm XIII.44, with the
semigroup e^{−sA_T} positivity improving (Beurling–Deny for the Dirichlet part, k>0 for irreducibility,
Dyson expansion for the bounded positivity-preserving comb). (v) J commutes with A_T; a simple eigenvalue
has a parity eigenvector, and a positive function is even. ∎

**DH line (Theorem 1).** Step (iii), "v_n ≥ 0". For Davenport–Heilbronn (and Epstein) the comb coefficients
of −f′/f are real but sign-changing (no Euler product; zeros in Re s > 1 make the coefficients not even
those of a convergent Λ-type series), so the comb is not positivity preserving and Theorem 1 fails there.
For Λχ₂ likewise (χ₂ changes sign). **F3 line:** step (iii) holds verbatim for every a ≥ 0, in
particular for the deletion and amplification models of Paper 47 thm:finmod, which have genuine first
contacts. So Theorem 1 is orientation-sensitive (fails under Λ → −Λ, unlike the (PC) square of F2) but
arithmetic-blind within a ≥ 0.

## 3. Theorem 2 (parity ladder) — PROVED

**Theorem 2.** For every T:
(a) μ_1^odd ≥ μ_2, hence λ_min(A_T|P_T^odd) ≥ μ_1^odd ≥ μ_2(A_T);
(b) μ_1 = μ_1^ev < λ_min(A_T|P_T^ev) ≤ μ_2^ev, the first inequality strict.
Hence λ_A(T) ≥ min(λ_min(A_T|P_T^ev), μ_2(A_T)) and the odd primitive sector is controlled by the second
eigenvalue alone.

*Proof.* (a) The ground state is even (Thm 1), so every odd eigenvalue is ≥ μ_2; compression to the
codimension-one subspace ker ℓ_odd only raises the bottom. (b) Cauchy interlacing for the codimension-one
compression to ker ℓ_ev gives μ_1 ≤ λ ≤ μ_2^ev; equality λ = μ_1 would need an eigenvector for μ_1 in
ker ℓ_ev, i.e. ⟨ψ_T,φ_ev⟩ = 0, impossible as both are > 0. ∎

**Corollary 2.1 (the D5 target is E1).** RH ⇒ μ_2(A_T) ≥ 0 for all T. Conversely μ_2(A_T) ≥ 0 ∀T ⇒
λ_min(A_T|P_T^odd) ≥ 0 ∀T.
*Proof.* RH ⇒ W_T ≥ 0 (Weil). On the odd sector a_T = W_T + 2ℓ_odd² ≥ 0; on the even sector
a_T = W_T − 2ℓ_ev² has n_− ≤ 1. With Thm 2(a), n_−(a_T) ≤ 1, i.e. μ_2 ≥ 0. The converse is Thm 2(a). ∎
Remark: odd tests alone detect off-line zeros (for real odd F, W_T(F) = −Σ_ρ Φ_F(ρ)², an off-line quartet
contributes −4 Re Φ_F(ρ)², of either sign), so the odd-sector Weil criterion is expected to be equivalent
to RH by the usual localisation; granted that, "μ_2(A_T) ≥ 0 ∀T" is **equivalent to RH**. Not re-proved here;
either way D5's target is a restatement (E1), not a weakening.

## 4. The first contact in resolvent form

Per sector put f_par(z) = ⟨(A_T^par − z)^{-1}φ_par, φ_par⟩ (Weinstein–Aronszajn function); f′ = ‖(A−z)^{-1}φ‖² > 0.
Eigenvalues of the compression to ker ℓ_par are the zeros of f_par (plus eigenvalues of A^par whose
eigenvectors lie in ker ℓ_par); eigenvalues of W^par = A^par + 2ε_par φφ* are the zeros of 1 + 2ε_par f_par.

**Theorem 3 (first-contact dichotomy) — PROVED.** Let F be a parity first-contact vector at T_*
(λ_min(A_{T_*}|P^par) = 0, H_{T_*}F = 0) and r = the Tate residue of eq:localweak, A_{T_*}F = r ∈ Rφ_par.
- Type I (r = 0): F is an eigenvector of the unconstrained A_{T_*} with eigenvalue 0 = μ_k, k ≥ 2, F ⊥ ψ_T.
  This is exactly the range condition α(F) = 0 of thm:parityschur(b).
- Type II (r = cφ_par, c ≠ 0): F = c(A_{T_*}^par)^{-1}φ_par, 0 ∉ spec A^par, and f_par(0) = 0. Then
  W_{T_*}F = cφ_par with ℓ(F) = 0, so α(F) = c ≠ 0 and λ_W(T_*) < 0 (thm:parityschur(b)).
Moreover: an **odd** first contact forces μ_2(A_{T_*}) ≤ 0 (Thm 2(a)); an **even** one forces
μ_2^ev(A_{T_*}) ≥ 0 and μ_1(T_*) < 0 (Thm 2(b)).
*Proof.* By eq:localweak, A F = r with r ∈ P^⊥ ∩ (parity sector) = Rφ_par. If r = 0, F is an eigenvector
with eigenvalue 0; in the even case 0 = λ_min(A|P^ev) > μ_1 (Thm 2(b)), in the odd case 0 ≥ μ_1^odd ≥ μ_2 > μ_1
(Thm 2(a), simplicity); so 0 ≠ μ_1, k ≥ 2 and F ⊥ ψ_T. If r ≠ 0 and 0 ∈ spec A^par with eigenvector E, then ⟨r,E⟩ = ⟨F,AE⟩ = 0 forces
E ⊥ φ; restricting to the complement gives F = cA^{-1}φ and ℓ(F) = c f(0) = 0. The W-statement is
W F = AF + 2εφℓ(F) = cφ. ∎

Since λ_W ≥ 0 for T ≤ 0.8 (Zhu) and T_* > ½log5 (R162_303), Theorem 3 does not exclude Type II.

**Proposition 4.1 (resolvent criterion; restatement of prop:polarcap).** Assume μ_1 < 0 < μ_2 (T large).
Then λ_min(A_T|P^odd) > 0 automatically, and
  λ_A(T) ≥ 0 ⟺ f_ev(0) ≤ 0;  W_T ≥ 0 ⟺ f_ev(0) ≤ −½ and f_odd(0) ≤ ½.
*Proof.* f increases from −∞ to +∞ on (μ_1, μ_2^ev); its zero is λ_min(A|P^ev), which is ≥ 0 iff f(0) ≤ 0.
a_T(h_par) = 1/f_par(0) (h = A^{-1}φ/f(0)), and prop:polarcap needs a_T(h_ev) ≥ −2, a_T(h_odd) ≥ 2; on the
odd sector f_odd(0) > 0 because A^odd ≥ μ_2 > 0. ∎
In spectral coordinates: λ_A,ev ≥ 0 ⟺ ⟨ψ_T,φ_ev⟩²/|μ_1| ≥ Σ_{k≥2} ⟨ψ_k,φ_ev⟩²/μ_k^ev.

**Proposition 4.3 (Perron–Tate alignment bound) — PROVED.** With c_T = ⟨ψ_T, φ_ev/‖φ_ev‖⟩ ∈ (0,1],
  λ_min(A_T|P^ev) ≥ c_T² μ_2^ev + (1 − c_T²) μ_1.
*Proof.* F ⊥ φ, ‖F‖ = 1, F = αψ + G, G ⊥ ψ: |α|c ≤ ‖G‖√(1−c²) ⇒ α² ≤ 1−c²; a(F) ≥ μ_1α² + μ_2^ev(1−α²). ∎
So a sufficient condition for WP_T is 1 − c_T² ≤ μ_2^ev/(μ_2^ev − μ_1), an angle of size O(e^{−T/2})
between the Perron vector and the Tate vector (|μ_1| ≍ e^T: μ_1 ≥ C_0 − A_T with A_T ~ 4e^T, and
μ_1 ≤ a_T(φ_ev)/‖φ_ev‖²). The angle is Λ-sensitive: ψ_T − φ_ev is driven by the comb minus its PNT main term.
**Killed by Theorem M:** λ_A(T) ≤ exp(−exp((2−ε)T)), so the bound must be tight to super-exponential
precision; no estimate of c_T can prove it. Kept only as a structural statement.

## 5. Mechanism search with Λ*1 = log — NO-GO

(i) *Arithmetic rank-2 correction.* The PNT main term of the comb, Σ v_n c_F(log n) with Λ(n) → dx,
is ∫_0^∞ 2e^{u/2}c_F(u)du = 2A(F)B(F) + O(‖F‖²) (the e^{−u/2} half is bounded): the rank-2 Tate correction
**is** the pole of ζ, and the exact version a_T + 2AB = W_T is the explicit formula. Any interlacing identity
between a_T and a_T + (rank-2 arithmetic correction) is therefore interlacing between a_T and the zero sum,
whose bottom sign is RH at T. Restatement (E1).
(ii) *Where Λ*1 = log could enter μ_2.* Spectral data of A_T depend on Λ only through v_T(Λ) ∈ R^{N_T}
(prop:finite). Λ*1 = log is a relation between v_T(Λ) and the one-sided comb of 1; on the window it is a
Dirichlet-multiplier (symbol) identity plus compression defects. Symbol identities fail F1 (R162_403),
compression defects are symbol-independent (R162_301), and test-side convolution identities are window
shifts (D4 Thm 5.1). None of them is a statement about the second eigenvector ψ_2 ⊥ ψ_T. We found no
channel by which Λ*1 = log reaches μ_2 other than through ψ_T (Prop 4.3), where Theorem M blocks it.
(iii) *Perron is the only Euler-product input that survived,* and it uses Λ ≥ 0 only (§2 F3 line):
deletion a = Λ1_{n≥N} (comb empty for T ≤ ½log N, first contacts at T ≈ 0.58–0.60) satisfies Thms 1–3
verbatim, so no conclusion of §§2–4 can force sign.

**DH line, summary.** Thm 1 step (iii) (v_n ≥ 0) is the unique line failing for DH/Epstein/Λχ₂; Thms 2–3
and Prop 4.1–4.3 then lose the Perron ladder (the ground state need not be even, the odd sector is no longer
controlled by μ_2, c_T may vanish). Every formulation that does not pass through step (iii) passes DH and
is discarded. Every formulation passing through step (iii) passes a ≥ 0 finite modifications (F3).

## 6. Open residue (for the map)

(O504.1) A sign-carrying statement must use Λ ≥ 0 (to get Thm 1) *and* Λ*1 = log in a way that is not a
symbol identity, acting on the Perron–Tate angle c_T. The only Λ-sensitive scalar exposed by D5 is
f_ev(0) (equivalently the polar capacity); D5 adds the Perron decomposition of it,
f_ev(0) = −c_T²‖φ_ev‖²/|μ_1| + Σ_{k≥2}⟨ψ_k,φ_ev⟩²/μ_k. No mechanism for its sign is known.
Verdict for R162_590: add D5 to §1c — "second eigenvalue / interlacing: E1 (Cor 2.1, Prop 4.1 =
prop:polarcap); Perron–Frobenius Thm 1 new, DH-failing, F3-blind (a ≥ 0); quantitative alignment killed by M".
