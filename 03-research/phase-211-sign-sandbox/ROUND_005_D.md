# Round 5, memo D: the window form as a jump Dirichlet form with the comb as atomic jump measure; ground-state representation; the sharp gap inequality

Object. For T > 0 and F ∈ L²(I_T) (extended by zero), with the notation of STATEMENT_001 (K, C_0, v_n, N_T = {n ≥ 2 : Λ(n) > 0,
log n < 2T}, c_F, A(F), B(F), P_T, a_T, λ_A), put A_T := Σ_{n∈N_T} v_n, u_n := log n, χ_±(t) := e^{±t/2}1_{I_T}(t),
χ_ev := cosh(t/2)1_{I_T}, χ_odd := sinh(t/2)1_{I_T}, and

    μ_T := K(u)du + Σ_{n∈N_T} v_n δ_{u_n}      (a positive measure on (0,∞)),
    𝔈_μ(F) := ∫_0^∞ (c_F(0) − Re c_F(u)) dμ_T(u)      (the Lévy energy of μ_T).

Target (★): λ_A(T) ≥ 0 for every T. Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL. No
equivalence of (★) with any statement outside STATEMENT_001 is used; nothing is reduced to zeros. All numerical
statements come from the N = 80 Galerkin matrices of this phase (Dirichlet sines, both parities; files
mats_80_key.pkl, mats_40_key.pkl, mats_40_scan.pkl; scripts r5d.py … r5d6.py in the scratch directory) and validate single
points only.

Throughout, μ_0 < μ_1 ≤ μ_2 ≤ … are the eigenvalues of a_T on all of L²(I_T) (no Tate constraint), e_k the
eigenfunctions, h_T := e_0 the ground state, and, sector by sector, μ_k^{par}, e_k^{par}, τ_k^{par} := ⟨e_k^{par}, χ_par⟩
(the Tate moment of the k-th eigenfunction); λ_A^{par} is the bottom of a_T on P_T^{par}, λ_{A,2}^{par} the second
constrained eigenvalue, so that λ_A = min(λ_A^{ev}, λ_A^{odd}) (Paper 47 lem:parity, CITED).

---------------------------------------------------------------------------------------------------------------------
## 0. Corpus check

Index and grid hits for the keywords of this object (ROUTES-TRIED-INDEX/*.md, grid R162_2300_MASTER_GRID.md):

- **Identity and Markov structure.** Paper 47 prop:nyq-LK (ρ_T = K1_{(0,2T)}du + Σ v_nδ_{log n} positive measure, s_T = c_T + ψ_T);
  Paper 47 prop:nodes(i) (the comb-free part C_0‖F‖² + Lev(c_F) is a regular pure-jump Dirichlet form with killing κ on
  L²(I_T), Beurling–Deny, positivity improving, simple positive ground state); Paper 47 remark "a ceiling for curvature
  methods" (𝔞_T = 𝓔_T + ∫W_T F², 𝓔_T censored jump form with kernel K plus ½Σv_nδ_{±log n}, W_T killing potential);
  CA_I_001 Thm 1 (phase 193: the full form with the comb is Markov on L²(I_T), positivity improving, λ_0 simple, h_0 > 0,
  λ_0 < λ_A ≤ λ_2; PROVED); P60-1 (Perron–Frobenius simplicity, "gives simplicity, not sign"); CA_R1_001 (Markov criterion
  = jump measure ≥ 0; (1+c)Λ is Markov for every T with λ_A → −∞).
- **Ground-state / Doob transform and Poincaré.** Paper 41 thm:doob (Doob–variance identity on the whole line with a FIXED
  Doob function K and the Lévy measure ν_ζ; "sharp Poincaré inequality", REF-D; grid cell 2C: "corridor signed nonlocal
  never executed; CD(0,∞) flat, no gap"); K11 "Doob transform, retry Paper 41"; INV_N_001 (Bakry–Émery Γ₂ / Poincaré of
  the censored jump part: NO-GO class 𝒦_BE, gap ceiling g_T + ess inf W_T < 0 at ½log3 for DECOUPLED transfers; "do not
  retry Γ₂/CD/log-Sobolev/Poincaré of the jump part without an input that couples E_T and W_T"); G2D/G2A (phase 106,
  positivity-preserving semigroups + Lévy + Hardy/Picone: DEAD, one-atom jump countermodel; pole kernel violates
  Beurling–Deny); INV_D_001 (Lévy/Green of the killed process dismissed); Paper 35 thm:gamma2kernel/thm:CD0 (CD(0,∞) for the
  prime kernel after Doob conjugation, unconditional, no sign).
- **The class NO-GO.** CA_I_001 Thm 2: the deduction class 𝒦_M (Beurling–Deny, irreducibility, Perron–Frobenius, non-local
  maximum principle, domination, parity, Tate data, class-generic minimiser properties) is closed under O2 (adding
  positive comb mass) and proves nothing; Prop 1.1 (Krein–Rutman does not reach the constrained problem; the
  Weinstein–Aronszajn count is the polar-capacity restatement 𝔊_T, REF-D); Prop 5 (rearrangement and polarisation
  inadmissible).
- **Where the constrained statement lands.** Polar capacity 𝔊_T: Paper 47 prop:polarcap, thm:parityschur; phase 156
  ("converse = 2×2 polar-capacity condition"); phase 199 PROOF_L_SHARP_OO_001 ("Tate triple = polar capacity"); H1_TRACT_001
  and H1PLUS_001 (H1⁺ := n₋(𝔄_ev(T)) ≤ 1 and 𝔄_odd ≻ 0: necessary, "H1⁺ as an independent route NO-GO (REF-D by P4)").
- Absent as words in index and grid: "Dirichlet form", "supersolution", "Allegretto", "Frank–Lenz–Wingert",
  "positivity-improving" (the concept is present under Beurling–Deny / Perron–Frobenius).

What is new in this memo, and why it is not a retry.
(a) The ground-state representation is taken with respect to the ground state h_T of the FULL window form (comb atoms
    included), on the window, with the two Tate constraints carried through the transform exactly. Paper 47 prop:nodes
    treats the comb-free part; Paper 41 thm:doob conjugates by a fixed function K on the whole line (the comb and the
    constraints are not transformed); INV_N_001 decouples the jump part from the potential and bounds a sum of separate
    infima. Here h_T solves the eigen-equation of the whole form, so the "input that couples E_T and W_T" demanded by
    INV_N_001 is exactly what the transform supplies. This is the corridor the grid records as never executed.
(b) The exact content of the resulting "weighted Poincaré inequality on the two-constraint complement" is computed
    (Theorem 3.1, Corollary 3.2): it is a genuine spectral-gap inequality for the transformed jump form, g_1 ≥ |μ_0| + τ_1²/D,
    with an explicit non-negative correction. In this form it is the recorded polar capacity / H1⁺ statement; the memo
    does not claim a new route. What it adds is the explicit correction term, the interlacing λ_A ≤ μ_1 ≤ λ_{A,2}, and the
    precise reason the Poincaré toolbox cannot close the inequality (§6).
(c) An exact formula for a_T applied to the Tate functions (Proposition 4.2): a_Tχ_+ = χ_+·ω_+ with ω_+ explicit,
    containing ψ(e^{T−t}) and Σ_{n<e^{T+t}}Λ(n)/n. Not found in the index under these names; related to Λ∗1 = log
    (INV_V_002, rem:ext-killing) and to the "ψ − x" west end of README §2, but not the same identity.
(d) A numerical finding not in the record in this form: the Tate moments of the low cluster of unconstrained
    eigenfunctions vanish to the order of their eigenvalues (τ_1/τ_0 ≈ 0.3 μ_1 at log 2 and ½log5), so that the
    unconstrained and constrained low spectra coincide to all digits except for the single polar eigenvalue μ_0 (§5).

---------------------------------------------------------------------------------------------------------------------
## 1. The identity and the Dirichlet-form structure

**Lemma 1.1 (PROVED).** For every F ∈ L²(I_T) in the form domain,

    a_T(F) = (C_0 − A_T)‖F‖² + 𝔈_μ(F),      𝔈_μ(F) ≥ 0.

*Proof.* By STATEMENT_001 §1 (Paper 47 thm:A, CITED), a_T(F) = C_0‖F‖² + ∫_0^∞(c_F(0) − Re c_F(u))K(u)du − Σ_{N_T} v_n Re c_F(u_n).
Write −v_n Re c_F(u_n) = v_n(c_F(0) − Re c_F(u_n)) − v_n c_F(0) and use c_F(0) = ‖F‖². Non-negativity: for u > 0,
c_F(0) − Re c_F(u) = ½∫_ℝ |F̃(t) − F̃(t−u)|²dt ≥ 0 (F̃ the zero extension), and μ_T ≥ 0. ∎

In jump-kernel form (PROVED, same computation as Paper 47 prop:nodes(i)): with the symmetric kernel
J(x) := ½K(|x|) on ℝ∖{0} and the symmetric atoms ¼v_n(δ_{u_n} + δ_{−u_n}), i.e. the measure J(dx) := ½μ̄_T(dx), μ̄_T the
even extension of μ_T,

    𝔈_μ(F) = ½∬_{I_T×I_T} |F(x) − F(y)|² J(x−y) dx dy + ∫_{I_T} κ(x)|F(x)|² dx,
    κ(x) = ∫_{|y|>T} J(x−y)dy = ½[ μ_T((T−x,∞)) + μ_T((T+x,∞)) ]
         = ½[∫_{T−x}^∞K + ∫_{T+x}^∞K] + ½Σ_{n∈N_T} v_n [1_{u_n > T−x} + 1_{u_n > T+x}].

(Here ∬J(x−y)|F(x)−F(y)|² with an atom at u_n means ½v_n∫|F(x) − F(x−u_n)|²dx over the pairs inside the window; the comb
atoms contribute to κ a step function increasing towards the edges, with jumps ½v_n at |x| = T − u_n.) Both terms are
non-negative; the archimedean killing is logarithmically divergent at the edges,
∫_{T−x}^∞K(u)du = log coth((T−x)/4) + 2arctan e^{−(T−x)} = log(4/(T−x)) + π/2 + o(1) as x ↑ T (Paper 47 thm:S(iii), CITED).

**Proposition 1.2 (CITED: CA_I_001 Thm 1, Paper 47 prop:nodes(i); PROVED for the parts marked).**
(i) F ↦ 𝔈_μ(F) is a regular Dirichlet form on L²(I_T) of pure-jump type (jump kernel J ≥ 0, killing κ ≥ 0, no diffusion
    part, no δ-kernel since ∫_0^{2T}K = +∞); its form domain is {F : ∫ m(τ)|F̂|² < ∞} (the comb part is bounded by A_T‖F‖²).
(ii) (Beurling–Deny) e^{−t𝔈_μ} is positivity preserving; since K > 0 on (0,∞) and I_T is connected it is irreducible, hence
    positivity improving.
(iii) The resolvent is compact (m increasing to +∞, Riesz–Kolmogorov, as in prop:nodes(i)); the spectrum of a_T on
    L²(I_T) is discrete, μ_0 < μ_1 ≤ …, each eigenvalue of finite multiplicity.
(iv) μ_0 is simple and h_T = e_0 can be taken a.e. strictly positive (Perron–Frobenius for positivity-improving semigroups).
(v) (PROVED) h_T is even: the form is invariant under J: F ↦ F(−·) (K even, atoms symmetric, I_T symmetric), so Jh_T is a
    ground state; by simplicity Jh_T = ±h_T, and h_T > 0 forces +.
(vi) (PROVED) λ_A > μ_0 strictly, λ_A ≤ μ_2: ⟨h_T, χ_+⟩ > 0 so h_T ∉ P_T, and a constrained minimiser with value μ_0
    would be a ground state; the span of e_0, e_1, e_2 meets P_T (codimension two).
(vii) (PROVED) The archimedean and the arithmetic parts of μ_T are not separable in h_T: h_T solves the eigen-equation
    of §4.1 in which K and the atoms v_nδ_{u_n} enter the same non-local operator; the overlap of h_T with the comb-free
    ground state is 0.984–0.989 at the four windows (NUMERICAL, §5).

The comparison asked for: Paper 47 states (i)–(iv) for the comb-free form only (prop:nodes(i), "the archimedean part
alone"); with the comb, (i)–(iv) are CA_I_001 Thm 1 (phase 193), which Paper 47 uses only in the remark on the curvature
ceiling. Nothing in (i)–(vii) distinguishes Λ from any positive comb (CA_I_001 Thm 2).

---------------------------------------------------------------------------------------------------------------------
## 2. The ground-state representation with the comb atoms (PROVED)

**Theorem 2.1.** Let h = h_T > 0 a.e. be the ground state of 𝔈_μ on L²(I_T) with eigenvalue λ_0 := μ_0 − (C_0 − A_T), i.e.
𝔈_μ(h, G) = λ_0⟨h, G⟩ for all G in the form domain. For every bounded Lipschitz φ on I_T,

    𝔈_μ(hφ) − λ_0‖hφ‖² = Q_h(φ) := ½∬_{I_T×I_T} (φ(x) − φ(y))² h(x)h(y) J(x−y) dx dy,

with no residual killing term, all integrals absolutely convergent. Equivalently, with F = hφ,

    a_T(F) = μ_0‖F‖² + Q_h(φ).

*Proof.* Put G := hφ². Since φ² is bounded Lipschitz, G lies in the form domain:
(G(x) − G(y)) = (h(x) − h(y))φ(x)² + h(y)(φ(x)² − φ(y)²), and ∬h(y)²min(C|x−y|²,C)J(x−y) < ∞ because ∫_0^∞min(u²,1)dμ_T < ∞
(K(u) ~ 1/u at 0, K ~ 2e^{−u/2} at ∞, finitely many atoms). The pointwise identity

    (h(x)φ(x) − h(y)φ(y))² = h(x)h(y)(φ(x) − φ(y))² + (h(x) − h(y))(G(x) − G(y))

is checked by expansion. Integrating against ½J(x−y)dxdy over I_T×I_T and adding the killing term ∫κh²φ²:

    𝔈_μ(hφ) = Q_h(φ) + [½∬(h(x)−h(y))(G(x)−G(y))J + ∫κ hG] = Q_h(φ) + 𝔈_μ(h, G) = Q_h(φ) + λ_0⟨h, G⟩ = Q_h(φ) + λ_0‖hφ‖²,

using hG = h²φ². The bracket is the polarised form evaluated on (h, G), both in the form domain, hence finite; Q_h(φ) ≤
‖φ‖²_{Lip}·∬ h h' min(C|x−y|², C)J < ∞ by hh' ≤ (h² + h'²)/2. ∎

Extension (CITED: ground-state representation for non-local Dirichlet forms, Frank–Lenz–Wingert, J. Funct. Anal. 2014):
the identity extends to all φ with hφ in the form domain, Q_h being then the closure of the right side; the map
φ ↦ hφ is unitary from L²(I_T, h²dx) onto L²(I_T), and Q_h is a Dirichlet form on L²(h²dx) without killing, with
spectrum {μ_k − μ_0}_{k≥0}, ground state the constant 1 (eigenvalue 0), and spectral gap

    g_1 := μ_1 − μ_0 > 0.

**Corollary 2.2 (the Tate constraints after the transform; PROVED).** For F = hφ,

    F ∈ P_T  ⟺  ⟨φ, ψ_+⟩_{h²} = ⟨φ, ψ_−⟩_{h²} = 0,     ψ_±(t) := e^{±t/2}/h(t)  ∈ L²(I_T, h²dx),

and (★) at T is equivalent to the weighted Poincaré inequality with the exact constant

    Q_h(φ) ≥ (A_T − C_0 − λ_0)·‖φ‖²_{h²} = |μ_0|·‖φ‖²_{h²}     for all φ ⊥_{h²} {ψ_+, ψ_−}      (2.1)

(if μ_0 ≥ 0 there is nothing to prove; μ_0 < 0 for every T ≥ 0.4608 by Paper 47 prop:archneg, since a_T ≤ 𝔄_∞ on the odd
function used there — CITED; at the four windows μ_0 ∈ [−4.29, −2.82], NUMERICAL).

*Proof.* ⟨hφ, e^{±t/2}⟩ = ∫φ e^{±t/2}h = ⟨φ, ψ_±⟩_{h²}; (2.1) is Theorem 2.1 rearranged. ∎

Remark 2.3. (2.1) is the window, comb-included, constraint-carrying version of the "sharp Poincaré inequality" of Paper 41
thm:doob (there: whole line, fixed Doob function, constraints not transformed). The identity holds for every positive
comb; the sign is entirely in (2.1).

---------------------------------------------------------------------------------------------------------------------
## 3. The exact content of (2.1): a spectral-gap inequality with a rank-one correction (PROVED)

Because P_T splits into parity sectors orthogonal for ‖·‖ and for a_T (lem:parity, CITED), (2.1) splits into one
constraint per sector: φ ⊥_{h²} χ_ev/h in the even sector and φ ⊥_{h²} χ_odd/h in the odd one. Fix a sector and drop the
superscript; the constraint on F = hφ is ⟨F, χ⟩ = 0 with χ ∈ {χ_ev, χ_odd}.

**Theorem 3.1 (rank-one reduction; PROVED).** Let n₋ := #{k : μ_k < 0} in the sector and W(z) := Σ_k τ_k²/(μ_k − z),
τ_k = ⟨e_k, χ⟩ (the series converges absolutely for z off the spectrum since Σ τ_k² = ‖χ‖²).
(i) If n₋ ≥ 2 then λ_A^{par} < 0. (ii) If n₋ = 0 then λ_A^{par} ≥ 0.
(iii) If n₋ = 1 and τ_1 ≠ 0, then λ_A^{par} is the unique root of W in (μ_0, μ_1), and

    λ_A^{par} ≥ 0  ⟺  W(0) ≤ 0  ⟺  ⟨χ, a_T^{−1}χ⟩ ≤ 0   (when 0 ∉ spec),

with the convention W(0) = +∞ (hence λ_A^{par} < 0) if some μ_k = 0 with τ_k ≠ 0. If τ_1 = 0 then λ_A^{par} = μ_1 (e_1 ∈ P_T).

*Proof.* (i) a negative 2-plane meets the hyperplane {⟨F,χ⟩ = 0}. (ii) inclusion. (iii) A constrained critical point with
value z ∉ spec(a_T) satisfies (a_T − z)F = βχ, ⟨F,χ⟩ = 0, β ≠ 0 (else F is an unconstrained eigenfunction with τ = 0), so
F = β(a_T − z)^{−1}χ and 0 = ⟨F,χ⟩ = βW(z). W is strictly increasing between consecutive poles (W′ = Στ_k²/(μ_k − z)² > 0) and
runs from −∞ (as z ↓ μ_0, since τ_0 = ⟨h_T, χ⟩ > 0 in the even sector by positivity of h_T; in the odd sector τ_0 ≠ 0 is the
hypothesis "n₋ = 1 with τ_0 ≠ 0", otherwise the single negative eigenfunction lies in P_T and λ_A^{par} < 0 directly) to +∞
(as z ↑ μ_1, τ_1 ≠ 0). So W has exactly one root in (μ_0, μ_1); by interlacing (one linear constraint) λ_A^{par} ∈ [μ_0, μ_1],
and λ_A^{par} = μ_0 is excluded by Prop. 1.2(vi). Hence λ_A^{par} is that root, and λ_A^{par} ≥ 0 iff W(0) ≤ 0 since W < 0
to the left of its root. ∎

**Corollary 3.2 (the gap form; PROVED).** In case (iii), with D(z) := τ_0²/(|μ_0| + z) − Σ_{k≥2} τ_k²/(μ_k − z),

    μ_1 − λ_A^{par} = τ_1² / D(λ_A^{par}),      D(λ_A^{par}) > 0,                                              (3.1)

so that

    (★)_par at T  ⟺  g_1 = μ_1 − μ_0 ≥ |μ_0| + τ_1²/D(λ_A^{par}),                                               (3.2)

and in every case λ_A^{par} ≤ μ_1 ≤ λ_{A,2}^{par} (interlacing: the span of the two lowest constrained eigenvectors lies in P_T^{par}
and a_T ≤ λ_{A,2}^{par} on it).
*Proof.* W(λ_A) = 0 rearranged; the left side of (3.1) is positive, so D(λ_A) > 0. ∎

**Corollary 3.3 (a two-level sufficient condition; PROVED).** If n₋ = 1, μ_1 > 0 and

    cos²∠(h_T, χ) := τ_0²/‖χ‖²  ≥  |μ_0| / (μ_1 − μ_0) = |μ_0|/g_1,                                               (3.3)

then λ_A^{par} ≥ 0.
*Proof.* Write φ = c + φ_1 with φ_1 ⊥_{h²} 1. The constraint gives c = −⟨φ_1, ψ⟩/⟨1,ψ⟩ with ⟨1,ψ⟩ = τ_0, and (2.1) becomes
Q_h(φ_1) ≥ |μ_0|(‖φ_1‖² + ⟨φ_1,ψ⟩²/τ_0²). The gap gives Q_h(φ_1) ≥ g_1‖φ_1‖², and ⟨φ_1,ψ⟩² ≤ ‖φ_1‖²(‖ψ‖² − τ_0²) by
Cauchy–Schwarz in 1^⊥ (‖ψ‖²_{h²} = ‖χ‖²); so it suffices that g_1 ≥ |μ_0|(1 + (‖χ‖² − τ_0²)/τ_0²) = |μ_0|‖χ‖²/τ_0². ∎

Remark 3.4 (identification with the record). W(0) = ⟨χ_par, a_T^{−1}χ_par⟩ is the diagonal entry of the polar capacity 𝔊_T in
the parity basis (Paper 47 prop:polarcap / thm:parityschur; phase 156; CA_I_001 Prop 1.1 "Weinstein–Aronszajn = polar
capacity"); Theorem 3.1 is therefore a restatement of a recorded reformulation, not a new route. The condition "n₋ ≤ 1 in
the even sector" is H1⁺ and "n₋ = 0 in the odd sector" is 𝔄_odd ⪰ 0 (H1_TRACT_001), both recorded as necessary. What
(3.1)–(3.2) add is the exact size of the step from the necessary condition μ_1 ≥ 0 to (★): the non-negative number
τ_1²/D, a functional of the Tate moment of the FIRST EXCITED unconstrained eigenfunction.

---------------------------------------------------------------------------------------------------------------------
## 4. The ground state h_T: eigen-equation, Tate image, provable properties

### 4.1 The eigen-equation (PROVED as a weak identity; pointwise where the principal value exists)

For x ∈ I_T, with h extended by zero outside I_T,

    μ_0 h(x) = C_0 h(x) + p.v.∫_ℝ (h(x) − h(y)) K(|x−y|) dy − ½ Σ_{n∈N_T} v_n [h(x + u_n) + h(x − u_n)],          (4.1)

i.e. (s_T(D)h)|_{I_T} = μ_0 h: the archimedean operator m(D) = C_0 + (log-Laplacian-type operator with kernel K ~ 1/|u|,
symbol m(τ) − C_0 ~ log|τ|) minus the comb operator Π = Σ v_n cos(u_n D) compressed to the window. The killing is the part
of the integral and of the comb sum that falls outside I_T. In the multiplicative variable y = e^x, h̃(y) := h(log y),
g(y) := y^{1/2}h̃(y) (so h = e^{−x/2}g(e^x)), the comb term reads

    ½ Σ_n v_n [h̃(ny) + h̃(y/n)] = y^{−1/2} Σ_{n∈N_T} Λ(n) [ g(ny)/n + g(y/n) ],

a Λ-twisted dilation operator on (e^{−T}, e^{T}) with zero extension: the same operator whose value on g ≡ 1 is
ψ(e^T/y)-type sums (4.2 below). (4.1) is a non-local functional equation mixing h at x and at x ± log n with weights
2Λ(n)/√n; no closed form is claimed.

### 4.2 The window operator on the Tate functions (PROVED; validated NUMERICALLY)

**Proposition 4.2.** χ_+ = e^{t/2}1_{I_T} lies in the operator domain of a_T, and

    a_T χ_+ = χ_+ · ω_+,      ω_+(t) = C_0 + ∫_0^∞ [1 − ½e^{−u/2}1_{u<T+t} − ½e^{u/2}1_{u<T−t}] K(u) du − ψ(e^{T−t}) − ψ_1(e^{T+t}),

where ψ(x) = Σ_{n<x}Λ(n), ψ_1(x) = Σ_{n<x}Λ(n)/n (sums over n ∈ N_T; for x ≥ e^{2T} they are the full sums over N_T), and the
u-integrand equals (1 − cosh(u/2))K(u) for u < T − |t| (integrable at 0) and is integrable at ∞. By symmetry a_Tχ_−(t) =
(a_Tχ_+)(−t), and a_Tχ_ev = ½(Ψ_+ + Ψ_−), a_Tχ_odd = ½(Ψ_+ − Ψ_−), Ψ_± := a_Tχ_±. Equivalently

    ω_+(t) = σ_T + ½[w_L(t) + w_R(t)] + Σ_{n∈N_T, n>e^{T+t}} Λ(n)/n + Σ_{n∈N_T, n>e^{T−t}} Λ(n),
    σ_T = C_0 − T − 2 log cosh(T/2) + arctan(sinh T) + ∫_{2T}^∞K − Σ_{N_T} Λ(n)(1 + 1/n),
    w_L(t) = ∫_{T+t}^{2T} e^{−u/2}K(u)du,   w_R(t) = ∫_{T−t}^{2T} e^{u/2}K(u)du,

so ω_+ − σ_T ≥ 0 is a sum of edge terms, logarithmically divergent at both edges, and of comb steps.

*Proof.* For real F ∈ L²(I_T) in the form domain and G = χ_+, the polarised Lévy form (Paper 47 thm:A, CITED) is
a_T(F,G) = C_0⟨F,G⟩ + ∫_0^∞[⟨F,G⟩ − ½⟨F,(τ_u + τ_{−u})G⟩]K(u)du − Σv_n ½⟨F,(τ_{u_n}+τ_{−u_n})G⟩, τ_u the translation of the zero
extension. Since τ_uχ_+ = e^{−u/2}e^{t/2}1_{[−T+u, T+u]}, one has ⟨F, τ_uχ_+⟩ = e^{−u/2}[A(F) − ∫_{−T}^{−T+u}Fe^{t/2}] for 0 < u < 2T
and = 0 for u ≥ 2T, and ⟨F, τ_{−u}χ_+⟩ = e^{u/2}[A(F) − ∫_{T−u}^{T}Fe^{t/2}]. The bracket in the u-integral is thus
A(F)(1 − cosh(u/2)) + ½e^{−u/2}∫_{−T}^{−T+u}Fe^{t/2} + ½e^{u/2}∫_{T−u}^{T}Fe^{t/2} for u < 2T and A(F) for u ≥ 2T; it is
O(u^{1/2}‖F‖) at 0 by Cauchy–Schwarz, so the u-integral converges absolutely against K for EVERY F ∈ L²(I_T). Fubini
(t ∈ [−T, −T+u] ⟺ u ≥ T+t, etc.) turns each term into ∫F(t)e^{t/2}(·)dt, giving a_T(F,χ_+) = ⟨F, χ_+ω_+⟩ with ω_+ as stated;
the comb terms are the same computation with the atoms. χ_+ω_+ ∈ L²(I_T) (logarithmic edge singularities), so χ_+ is in the
operator domain and a_Tχ_+ = χ_+ω_+. The two forms of ω_+ agree by ∫_0^{2T}(1 − cosh(u/2))K = −T − 2log cosh(T/2) + arctan(sinh T)
(elementary) and Σ v_n cosh(u_n/2) = Σ Λ(n)(1 + 1/n), ½v_n e^{∓u_n/2} = Λ(n)/n, Λ(n). ∎

Validation (NUMERICAL): the Galerkin vector M r_+ (M = Arch − Π, r_+ the coefficients of χ_+) and the projection of the
explicit χ_+ω_+ onto the sine basis agree in direction to cosine 0.99986 ± 0.00003 at the five saved windows, with a norm
discrepancy of 1.7–1.9 % attributable to the Gibbs error of representing χ_+ (non-zero at the edges) in the Dirichlet
basis; the weak-form check (1/2π)∫s_T F̂ conj χ̂_+ = ⟨F, χ_+ω_+⟩ on an interior C³ bump is reported in §5. Rayleigh quotients
⟨a_Tχ_+,χ_+⟩/‖χ_+‖² = −2.71, −3.14, −3.15, −3.56, −3.95 at T = log 2, ½log5 ∓ 10⁻³, 0.9, 1.0 (explicit formula), against
μ_0 = −2.82, −3.32, −3.32, −3.80, −4.28.

Reading. a_T acts on the Tate function as multiplication by ω_+: a constant σ_T (which carries C_0, the archimedean
constants and the full prime sums Σ_{n<e^{2T}}Λ(n)(1+1/n)) plus a non-negative "defect" ω_+ − σ_T consisting of the two
edge weights and of the partial Chebyshev sums ψ(e^{2T}) − ψ(e^{T−t}), ψ_1(e^{2T}) − ψ_1(e^{T+t}). Were the defect zero,
a_T^{−1}χ = χ/σ_T and W(0) = ‖χ‖²/σ_T < 0, i.e. (★) would hold trivially in both sectors. The sign problem is therefore,
in this coordinate, the question whether the defect ω_+ − σ_T (edges + Chebyshev partial sums) can push ⟨χ, a_T^{−1}χ⟩
through 0. This is a restatement; it is recorded here because it exhibits the Chebyshev function inside the exact
operator identity without any smoothing and at the sharp scale e^{T−t}, which is where the record locates the sign
(README §2, west end).

### 4.3 Provable properties of h_T

- Even, a.e. positive, simple: Prop. 1.2 (PROVED/CITED).
- Not monotone on [0, T) (NUMERICAL, robust): h_T(0) = 0.800, 0.833, 0.830, 0.720, 0.648 and h_T(T/2) = 0.823, 0.828, 0.826,
  0.727, 0.685 (‖h‖ = 1) at T = log 2, ½log5∓10⁻³, 0.9, 1.0; h_T rises from the centre (T ≥ 0.9) or is flat (T ≈ 0.7–0.8)
  before dropping to ≈ 0.44–0.49 at 0.99T and to 0 at the edge. Monotonicity cannot be obtained by rearrangement: the
  atomic jump kernel is not symmetric decreasing (CA_I_001 Prop. 5, rearrangement inadmissible, CITED). OPEN as a
  theorem; the numerics say it is false.
- Log-concavity: OPEN; not expected (the comb steps in κ and the atoms make the profile non-concave in log; NUMERICAL
  profile has an interior maximum off the centre at T ≥ 0.9).
- Edge behaviour: the total killing κ(x) ~ ½log(1/(T−|x|)) (PROVED, §1); h_T → 0 at the edge in the sense of the form domain
  (zero extension); the rate is OPEN (order-zero operator; the log-Laplacian boundary theory, Chen–Weth 2019, gives
  continuity up to the boundary for bounded right sides, CITED, but the comb term Πh is only in L²). Numerically
  h_T(0.99T)/max h_T ≈ 0.52–0.60, a very slow approach to 0.
- Proximity to the Tate function: cos²∠(h_T, χ_ev) = 0.9951, 0.9948, 0.9947, 0.9983, 0.9974 (NUMERICAL); h_T/cosh(t/2)
  ranges over [0, 0.91]; h_T is not proportional to cosh(t/2) (which is not in the form domain's kernel of anything).
- Dependence on the comb: overlap ⟨h_T, h_T^{arch}⟩ = 0.989, 0.988, 0.988, 0.985, 0.984 with the comb-free ground state;
  the comb-free bottom is −2.12, −2.32, −2.32, −2.47, −2.61 against μ_0 = −2.82, −3.32, −3.32, −3.80, −4.28 (NUMERICAL).

---------------------------------------------------------------------------------------------------------------------
## 5. Numerical validation and the values of the quantities of §3 (NUMERICAL)

Set-up. N = 80 Dirichlet sines on I_T (40 per parity), Arch by spectral quadrature to τ = 6000, comb matrix by exact
t-space quadrature, Tate functionals by 800-node Gauss–Legendre; eigenvalues at round-off floor ≈ 10⁻¹⁵ are noise.
Windows: T = log 2, ½log5 ∓ 10⁻³ (contact 5 absent / present), 0.9, 1.0. χ_ev = cosh(t/2) (the table lists τ_0² for this
normalisation; r5d.py uses 2cosh, so its W-values are 4× these).

5.1 Identity checks.
- Theorem 3.1(iii): the root of W_ev in (μ_0, μ_1) and the constrained bottom λ_A^{ev} computed directly agree to all printed
  digits at every window and for every falsifier comb (e.g. 0.9Λ at log 2: −9.753·10⁻³ both; "no 2" at 0.9: −0.5260 both).
- Corollary 3.2: λ_A^{ev} ≤ μ_1^{ev} ≤ λ_{A,2}^{ev} holds at every window (e.g. ½log5+10⁻³: 3.089·10⁻¹² ≤ 3.090·10⁻¹² ≤ 3.18·10⁻⁷).
- Proposition 4.2 (weak form, independent quadrature): (1/2π)∫ s_T F̂ conj χ̂_+ against ⟨F, χ_+ω_+⟩ for the interior C³ bump
  F = (1 − (t/0.8T)²)⁴(1 + ½ sin 3t): −1.30366610 vs −1.30366609 (log 2), −1.78756204 vs −1.78756202 (½log5+10⁻³),
  −2.84158673 vs −2.84158672 (T = 1); relative difference 5–7·10⁻⁹.

5.2 The even sector for the exact comb (χ_ev = cosh(t/2); ‖χ_ev‖² = 1.435, 1.687, 1.692, 1.915, 2.162).

| T | μ_0 | μ_1 = λ_A^{ev} | λ_{A,2}^{ev} | τ_0² | τ_1/τ_0 | τ_1²/D | W_ev(0) = ⟨χ, a^{−1}χ⟩ | |μ_0|/g_1 | cos²∠(h_T,χ) |
|---|---|---|---|---|---|---|---|---|---|
| log 2 | −2.8227 | 1.114·10⁻⁷ | 2.3·10⁻³ | 1.4282 | 3.4·10⁻⁸ | 3·10⁻¹⁵ | −0.50000 | 1.00000 | 0.9951 |
| ½log5−10⁻³ | −3.3156 | 3.83·10⁻¹² | 3.9·10⁻⁷ | 1.6785 | 1.1·10⁻¹² | 4·10⁻²⁴ | −0.50000 | 1.00000 | 0.9948 |
| ½log5+10⁻³ | −3.3238 | 3.09·10⁻¹² | 3.2·10⁻⁷ | 1.6830 | 8.5·10⁻¹³ | 2·10⁻²⁴ | −0.50000 | 1.00000 | 0.9947 |
| 0.9 | −3.8030 | 3.4·10⁻¹⁵ | 1.3·10⁻¹¹ | 1.9121 | 2·10⁻¹⁵ | 10⁻²⁹ | −0.50000 | 1.00000 | 0.9983 |
| 1.0 | −4.2819 | (−8·10⁻¹⁶) | 7·10⁻¹⁵ | 2.1566 | 4·10⁻¹⁵ | 6·10⁻²⁹ | −0.50000 | 1.00000 | 0.9974 |

Unconstrained even eigenvalues below 10⁻³ (count): {−2.82, 1.1·10⁻⁷} (2); {−3.32, 3.8·10⁻¹², 3.9·10⁻⁷} (3); same at
½log5+10⁻³; {−3.80, 3·10⁻¹⁵, 1.3·10⁻¹¹, 4.1·10⁻⁷} (4); {−4.28, −8·10⁻¹⁶, 6·10⁻¹⁵, 1.7·10⁻¹², 4.3·10⁻⁸, 2.4·10⁻⁴} (6). In every
case the constrained even spectrum below 10⁻³ is the same list with μ_0 removed, digit for digit: the cluster
eigenfunctions are Tate-null to the order of their eigenvalues (τ_k/τ_0 = 3.4·10⁻⁸, −4.1·10⁻⁴, … at log 2; 10⁻¹², 7·10⁻⁸,
2.6·10⁻⁴ at ½log5; ratios τ_1/(μ_1τ_0) = 0.30, 0.28, 0.28 at the first three windows, i.e. ⟨e_1, a_T^{−1}χ⟩ ≈ 0.36 stable).

Odd sector: the unconstrained odd bottom is μ_0^{odd} = 1.29·10⁻⁵, 7.9·10⁻¹⁰, 6.5·10⁻¹⁰, 2.4·10⁻¹⁴, 1.6·10⁻¹⁵ and equals
λ_A^{odd} to all digits; the odd ground state is Tate-null (τ_0^{odd} ≈ 0); n₋(a_T|odd) = 0 at all five windows;
W_odd(0) = ⟨χ_odd, a_T^{−1}χ_odd⟩ = +0.50000 at all five windows.

5.3 The falsifiers (even sector; all at the same five windows).

| comb | μ_1^{ev} (log 2 / ½log5+ / 0.9 / 1.0) | λ_A^{ev} | |μ_0|/g_1 | W_ev(0) (log 2 … 1.0) | τ_1/τ_0 (log 2) |
|---|---|---|---|---|---|
| Λ | +1.1e−7 / +3e−12 / +3e−15 / −8e−16 | same | 1.0000 (all) | −0.5000 (all) | 3.4·10⁻⁸ |
| 0.9Λ | −0.0094 / −0.0261 / −0.0383 / −0.0498 | −0.0098 / −0.0264 / −0.0386 / −0.0500 | 1.003–1.012 | −0.529 … −0.519 | 1.1·10⁻² |
| 1.1Λ | −0.0537 / −0.0940 / −0.1124 / −0.1411 | ≈ μ_1 | 1.019–1.033 | −0.474 … −0.482 | |
| no 2 (a_P-type) | −0.436 / −0.507 / −0.524 / −0.532 | ≈ μ_1 | 1.18–1.23 | −0.605 … −0.665 | |
| no 3 | −0.063 / −0.366 / −0.590 / −0.632 | ≈ μ_1 | 1.02–1.22 | −0.500 / −0.499 / −0.460 / −0.602 | |
| Λ(2)+0.5 | −0.336 / −0.429 / −0.445 / −0.488 | ≈ μ_1 | 1.11–1.13 | −0.432 … −0.446 | |
| swap v_2↔v_3 | −0.133 / −0.240 / −0.265 / −0.272 | ≈ μ_1 | 1.05–1.08 | −0.483 … −0.482 | |
| Beurling 3→3.2 | −0.124 / −0.239 / −0.242 / −0.351 | ≈ μ_1 | 1.05–1.09 | −0.500 / −0.498 / −0.506 / −0.508 | |

Reading of the tables.
(1) For the exact comb the gap inequality (3.2) holds with EQUALITY to the available precision: g_1 = |μ_0|(1 + 4·10⁻⁸)
    at log 2, (1 + 10⁻¹²) at ½log5, and to round-off beyond. The correction τ_1²/D is 10⁻¹⁵ or smaller. The sign of
    (★)_ev at these windows is the sign of μ_1^{ev}, the second even eigenvalue of a_T on L²(I_T) without any Tate
    constraint, and that eigenvalue sits at 0⁺.
(2) For every falsifier the inequality fails at the first step: μ_1^{ev} < 0 (n₋(a_T|even) = 2), by 0.3 % to 23 % of |μ_0|.
(3) The clause W_ev(0) ≤ 0 of Theorem 3.1(iii) is comb-generic on the tested set: it holds for all eight combs with
    values in [−0.67, −0.43]. For the exact comb W_ev(0) = −0.50000 and W_odd(0) = +0.50000 at all five windows; in Paper 47's
    notation this is 𝔞_T(h_ev) = 1/W_ev(0) = −2.0000 and 𝔞_T(h_odd) = +2.0000, i.e. 𝔤_ev = 𝔞_T(h_ev) + 2 ≈ 0 and
    𝔤_odd = 𝔞_T(h_odd) − 2 ≈ 0: the polar capacity 𝔊_T of prop:polarcap vanishes to 5 digits at every window, the complete
    form of thm:parityschur is at its degenerate point in both sectors (λ_W ≈ 0), and the "converse pair"
    𝔞_T(h_odd) ≥ 2, 𝔞_T(h_ev) ≥ −2 of Paper 47 holds with equality. The deviation 𝔊_T from 0 is of the order of λ_A
    (CONDITIONAL on the Galerkin precision; the record expected 𝔊_T ≻ 0 beyond ½log5 with ε tiny, index line "polar
    capacity > ½log5", and the present values are consistent with that ε being ≤ 10⁻⁵).
(4) The two-level sufficient condition (3.3) fails for the exact comb by 0.2–0.5 % (cos² − |μ_0|/g_1 = −0.0049, −0.0052,
    −0.0053, −0.0017, −0.0026) and by 1–24 % for the falsifiers, as it must: at tangency no sufficient condition with
    slack can hold.
(5) The ground state and the constant under the falsifiers: μ_0 moves by −0.07 to +0.50 (cΛ: ≈ (c−1)·(−0.75)), the
    overlap of h_T with cosh(t/2) is unchanged to 10⁻³ (cos² ∈ [0.981, 0.998] for all combs), and the gap g_1 moves by
    0.3–23 % of |μ_0|. So the identity and the ground state are insensitive to the modifications; the sign is decided by
    the second eigenvalue alone.

5.4 The polar capacity across windows and basis sizes (NUMERICAL; scripts r5d5.py, r5d6.py).
- Stability in N: W_ev(0) = −0.50000 and W_odd(0) = +0.50000 for the exact comb at the five windows with N = 40 and with
  N = 80 (all digits equal); the falsifier values move by ≤ 2·10⁻³ between N = 40 and 80 (e.g. "empty comb": −0.8899 →
  −0.8836 at log 2), so the ∓½ is not a basis artefact.
- T-scan (N = 40, 17 windows T = 0.600, 0.625, …, 1.000, contacts {2,3} → {2,3,4,5,7}): W_ev(0) = −0.500000 at every window;
  W_odd(0) = +0.499985, +0.499998, then +0.500000 from T = 0.65 on; μ_1^{ev} = 8.0·10⁻⁵, 1.6·10⁻⁵, 2.7·10⁻⁶, 5.2·10⁻⁷,
  6.6·10⁻⁸, 7.1·10⁻⁹, 9.0·10⁻¹⁰, 1.0·10⁻¹⁰, 7.6·10⁻¹², 5.7·10⁻¹³, 3.4·10⁻¹⁴, then round-off; μ_0^{odd} = 3.6·10⁻³, 1.1·10⁻³,
  2.3·10⁻⁴, 4.1·10⁻⁵, 8.1·10⁻⁶, 1.0·10⁻⁶, 1.1·10⁻⁷, 1.5·10⁻⁸, 1.5·10⁻⁹, 1.2·10⁻¹⁰, 8.7·10⁻¹², 4.6·10⁻¹³, then round-off.
  Both low eigenvalues decay by a factor ≈ 8–10 per ΔT = 0.025 on this range (the record's bound λ_A ≤ 4·10⁹ T e^{−15.449T}
  is far weaker here), and the deviation of W_odd(0) from +½ decays with μ_0^{odd}.
- Comb dependence: the comb-free window form has W_ev(0) = −0.88, −0.80, −0.80, −0.80, −0.77 and W_odd(0) = −0.05, −0.003,
  −0.0001, −0.51, −0.23; the modifications of §5.3 give W_ev(0) ∈ [−0.66, −0.43] and W_odd(0) anywhere in [−2.5, +0.7]
  (and +561, −1049 at log 2 for 0.9Λ, where an odd eigenvalue crosses 0). Only the exact comb sits at (−½, +½), and an
  atom whose overlap window 2T − u_n is short (3 at T = log 2: 0.29) is felt only at 10⁻⁵ ("no 3": −0.49999 at log 2,
  −0.4992 at ½log5, −0.460 at 0.9, −0.602 at 1.0): the exactness is per atom and weighted by the overlap length.
- Identification. In Paper 47 thm:parityschur / prop:polarcap, 𝔞_T(h_par) = 1/W_par(0) with h_par the 𝔞_T-orthogonal complement
  of P_T^{par} normalised to ℓ_par = 1, and 𝔊_T = S^{Sch}_T + D_pol, D_pol = diag(2, −2). The values above say

      S^{Sch}_T = diag(𝔞_T(h_ev), 𝔞_T(h_odd)) = diag(−2, +2) + O(10⁻⁵) = −D_pol,     i.e.  𝔊_T = 0 to 5–6 digits on [0.60, 1.00]:

  the Schur complement of the primitive window form over P_T is the negative of the polar form, the complete form
  W_T = a_T + 2AB is at its degenerate point in both sectors (λ_W ≈ 0; under the hypotheses of (a4) of thm:parityschur, λ_A^{par} > 0, 𝔤_par > 0, 2λ_W < λ_A^{par}, one has
  𝔤_par/‖h_par‖² ≤ 2λ_W),
  and the "converse pair" 𝔞_T(h_odd) ≥ 2, 𝔞_T(h_ev) ≥ −2 holds with equality. This is the complete-form face of the same
  tangency the record describes for the primitive form (c*_T = 1, Θ_T = λ_A); it is consistent with Paper 47
  §subsec:mult (optimal multipliers tending to the polar value) and with the index line "polar capacity > ½log5 … ε
  tiny". It is reported here because the value is exact to the digits available at every window, which the record
  does not state. No sandbox mechanism for S^{Sch}_T = −D_pol is known; a proof of it would be a proof that λ_W = 0, which
  is not weaker than (★).

---------------------------------------------------------------------------------------------------------------------
## 6. The sign lemma and the Poincaré toolbox: NO-GO with class

**The sign lemma (exact statement; OPEN).** For every T with n₋(a_T|even) = 1 and n₋(a_T|odd) = 0,

    g_1^{ev}(T) := μ_1^{ev} − μ_0^{ev} ≥ |μ_0^{ev}| + τ_1²/D(λ_A^{ev})     and     μ_0^{odd} ≥ 0,

where g_1^{ev} is the spectral gap of the Dirichlet form Q_h (Theorem 2.1) on L²(I_T, h_T²dx) restricted to even φ. By §3
this is (★) exactly (and the parity assumptions are themselves necessary for (★)). By §5 the first inequality is
satisfied with equality to 10⁻⁸ … 10⁻¹⁵ relative at the four windows beyond log 2.

**Theorem 6.1 (NO-GO for lossy gap bounds; PROVED modulo the NUMERICAL size of the slack).** Let 𝒦_gap be the class of
deductions that establish a lower bound g_1 ≥ (1 − ε)·c with a constant c that is itself ≤ |μ_0| + τ_1²/D (any bound
that does not exceed the truth) and a method-intrinsic loss ε > 0 independent of the specific comb (a universal
constant, or a constant depending only on structural data of (h_T, J, κ)). Then no deduction in 𝒦_gap proves the sign
lemma at a window where the slack s_T := (g_1 − |μ_0| − τ_1²/D)/|μ_0| is below ε. By §5, s_T ≤ 4·10⁻⁸ at log 2 and
≤ 10⁻¹² at ½log5. In particular:
- Cheeger-type isoperimetry (g_1 ≥ Φ_h²/2·(rate)⁻¹ or Lawler–Sokal g ≥ Φ²/(8M)): the form Q_h has infinite total jump rate
  (∫_0 K = ∞), so the bounded-rate versions do not apply; the versions for unbounded kernels (Cheeger for stable-like
  forms) carry a universal loss factor < 1 relative to the isoperimetric profile and cannot reach equality. Moreover
  Cheeger's upper bound g_1 ≤ 2Φ_h would force Φ_h ≥ |μ_0|/2 — a statement as hard as the target.
- Lyapunov functions (g_1 ≥ inf (−L_hV)/V over V > 0 in the complement of constants): the bound is attained only when V
  is the first excited state e_1/h_T itself; any explicit V has a positive loss. A proof in this class would have to
  produce e_1 in closed form, i.e. solve (4.1) for the second eigenfunction, which is the problem.
- Coupling / contraction rates: sharp only when the coupling realises e_1; same obstruction.
- Bakry–Émery / curvature-dimension: the jump form is at best CD(0,∞) (Paper 35 thm:CD0; INV_N_001; grid 2C "flat, no
  gap"); CD(K,∞) with K > 0 would give g_1 ≥ K, but K ≤ ess inf of a curvature that vanishes somewhere on the window
  (INV_N_001 Thm 3.3 for the decoupled version; the h-transform does not create curvature where J is translation
  invariant away from the atoms).
- Hardy / Allegretto–Piepenbrink (positive supersolution ⟺ form bounded below by the constant): characterises the
  BOTTOM μ_0 (ground state h_T), not the second eigenvalue; on the Tate-constrained space P_T no positivity structure
  survives (CA_I_001 Prop. 1.1(c): the constrained operator is not Markov). A supersolution characterisation of μ_1 would
  need a nodal-domain theory for the non-local operator (Courant for the codimension-two problem: OPEN, CA_I_001 §4).
*Proof.* The equality case leaves no room: a bound with loss ε ≥ s_T is false or insufficient; a bound sharper than the
truth would contradict the min-max value. The bullets check each tool's intrinsic loss or its target (μ_0 vs μ_1). ∎

**Why the equality is not accidental, and where the sign lives.** By Corollary 3.2, μ_1^{ev} ∈ [λ_A^{ev}, λ_{A,2}^{ev}]; the record
(ROUND_003_A (P1), ROUND_005_B precision caveat) has both constrained eigenvalues at 10⁻⁷ to 10⁻¹⁵, and (★) requires
λ_A ≥ 0. So, GIVEN those sizes, g_1 = |μ_0| + O(λ_{A,2}) is forced: the sharp Poincaré inequality has slack at most
λ_{A,2}^{ev}/|μ_0|, and the sign lemma asks for the sign of a quantity sitting at the edge of its own feasible interval.
Every tool listed above is monotone in the jump measure or blind to the comb's exact values (CA_I_001 Thm 2: the
Markov class is closed under O2); the equality tells the same thing quantitatively: there is no comb-generic margin.

**Falsifier test (rule 4).** (a) cΛ, c ≠ 1: the identity (Lemma 1.1, Theorem 2.1) holds with μ_T^{(c)}; the sign lemma
fails because μ_1^{ev}(c) < 0 (NUMERICAL: −0.009 at c = 0.9, −0.054 at c = 1.1, at log 2); for c → ∞, μ_1/c → −π_1 < 0, the
second eigenvalue of −Π on even functions (PROVED: Π is indefinite with at least two positive eigenvalues on L²_ev(I_T)
for 2T > log 2, by CA_I_001 Thm 2's construction), so the lemma fails for all large c. (b) a_P (primes below P deleted):
"no 2" has μ_1^{ev} = −0.44 … −0.53 (fails). (c) Beurling system reaching the line: the shift 3 → 3.2 fails (μ_1 = −0.12 …
−0.35); a general Beurling system has the identity and Prop. 1.2 verbatim, and nothing in §1–§4 uses more than
positivity of the weights, so §1–§4 survive — as they must, being identities; the sign lemma is where it fails.
(d) Finite modification Λ(2) + 0.5: μ_1 = −0.34 … −0.49 (fails). Where a putative argument would have to use the exact
values: in the single number μ_1^{ev}(T), which is a non-linear functional of (v_n)_{n∈N_T}; any argument that bounds
g_1 from below using only (h_T > 0, J ≥ 0, κ ≥ 0, parity) is in CA_I_001's 𝒦_M and is wrong.

---------------------------------------------------------------------------------------------------------------------
## 7. Assessment against R1–R5 of OBJECT_SPEC_001; the next lemma

- R1 (dim E_T → ∞): the object of this memo is a single eigenvalue inequality on L²(I_T); it is exact (R3(ii)), so R1 is
  not needed for the reduction; but the cluster of Tate-null unconstrained eigenfunctions at 0⁺ grows with T (2, 3, 3, 4,
  6 below 10⁻³ at the five windows; 26 at T = 1.4 by ROUND_005_B), and a proof of μ_1 ≥ 0 must control all of them.
- R2 (exact Λ, non-linear): μ_1^{ev}(T) is a non-linear functional of the exact weights; the deduction tools of §6 are
  not, hence the NO-GO. The memo supplies no object with Λ-specific entries beyond the eigen-equation (4.1).
- R3 (exact or with margin): Theorem 3.1 / Corollary 3.2 is exact ((ii) of R3). Margin: none (equality to 10⁻⁸–10⁻¹⁵).
- R4 (archimedean and arithmetic jointly): they enter jointly in h_T and in μ_1 through the single non-local operator
  (4.1); Proposition 4.2 shows the joint entry on the Tate functions explicitly (C_0 and the Γ-kernel K against
  ψ(e^{T−t}) and ψ_1(e^{T+t})). No handle on μ_1 follows.
- R5: done in §6.

What this route is, after this memo. The ground-state representation turns (★) into the sharp gap inequality
g_1 ≥ |μ_0| + τ_1²/D for the h_T-transformed jump form, which is numerically an equality to the precision of λ_{A,2};
equivalently (Remark 3.4) H1⁺ with the exact correction, or the polar capacity 𝔊_T, which sits at 0. The Poincaré
toolbox is excluded by Theorem 6.1. The route does not produce the sign. The honest residue is the pair of NUMERICAL
facts (i) μ_1^{ev}(T) = 0⁺ and μ_0^{odd}(T) = 0⁺ to 10⁻¹²–10⁻¹⁵ for the exact comb, (ii) the low cluster is Tate-null to the
order of its eigenvalues, for which no sandbox mechanism is known (the record names it tangency / near-null pair /
cluster).

Next lemma (concrete, within the sandbox). Explain (ii) exactly: prove or refute that the Tate function is in the
range of a_T on L²(I_T) with a preimage of controlled norm uniformly in T, i.e. that y_T := a_T^{−1}χ_ev exists with
‖y_T‖ bounded by an explicit function of T (NUMERICAL: ‖y_T‖ = 0.60, 0.59, 0.59, 0.88 at the first four windows; 6.4 at
T = 1.0 where a cluster eigenvalue of 10⁻¹⁶ is at round-off), using Proposition 4.2 as the starting point: a_Tχ_+ = χ_+ω_+
suggests the ansatz y = χ_+ν with ν solving L_+ν = 1, L_+ the conjugated operator of §4.1 (comb part the Λ-dilation
ν̃ ↦ Σ_n Λ(n)[ν̃(ny) + ν̃(y/n)/n]). If ‖y_T‖ is bounded then τ_k = μ_k⟨e_k, y_T⟩ = O(μ_k) for every cluster eigenfunction,
which is (ii), and W_ev(0) = ⟨χ, y_T⟩. This is an identity-level question (no sign) and is the only piece of this route
that is not in the record; if it closes, the sign question becomes: show ⟨χ_ev, y_T⟩ ≤ 0 together with μ_1 ≥ 0, which is
again H1⁺ — so the lemma clarifies, it does not decide. Index entries to add: this memo's NO-GO class 𝒦_gap (Theorem 6.1)
and the identity of Proposition 4.2.

---------------------------------------------------------------------------------------------------------------------
## Result

NO-GO with class, plus PROVED pieces. Class: lower bounds on the spectral gap of the ground-state-transformed jump
form with a method-intrinsic loss (Cheeger, Lyapunov, coupling, curvature-dimension, supersolution), 𝒦_gap of
Theorem 6.1; the required inequality is an equality to 10⁻⁸–10⁻¹⁵ relative at the tested windows, so no such bound can
reach it. The route (ground-state representation + weighted Poincaré on the two-constraint complement) is executed to
its end and lands on the recorded polar-capacity / H1⁺ statement with an explicit correction term; it carries no sign.

## What was proved

- Lemma 1.1: a_T = (C_0 − A_T)‖F‖² + 𝔈_μ(F) with μ_T = K du + Σ v_nδ_{log n}, and the jump-kernel/killing form of 𝔈_μ (PROVED).
- Prop. 1.2(v)–(vii): h_T even; λ_A > μ_0; comb and Γ-kernel inseparable in h_T (PROVED); the rest CITED (CA_I_001 Thm 1).
- Theorem 2.1: ground-state representation with the comb atoms, no residual killing, on bounded Lipschitz φ (PROVED);
  Corollary 2.2: (★) ⟺ Q_h(φ) ≥ |μ_0|‖φ‖²_{h²} on φ ⊥_{h²} {e^{±t/2}/h_T} (PROVED).
- Theorem 3.1: rank-one reduction per parity sector; (★)_par ⟺ W_par(0) ≤ 0 when n₋ = 1 (PROVED; = polar capacity).
- Corollary 3.2: μ_1 − λ_A = τ_1²/D exactly; (★)_par ⟺ g_1 ≥ |μ_0| + τ_1²/D; interlacing λ_A ≤ μ_1 ≤ λ_{A,2} (PROVED).
- Corollary 3.3: two-level sufficient condition cos²∠(h_T, χ) ≥ |μ_0|/g_1 (PROVED; fails numerically by 0.2–0.5 %).
- Proposition 4.2: a_Tχ_+ = χ_+ω_+ with ω_+ explicit, containing ψ(e^{T−t}) and Σ_{n<e^{T+t}}Λ(n)/n (PROVED; validated to 6·10⁻⁹).
- Theorem 6.1: NO-GO for 𝒦_gap (PROVED modulo the NUMERICAL size of the slack).

## What failed and why

The weighted Poincaré inequality is a genuine spectral-gap inequality (plus an explicit correction ≤ 10⁻¹⁵) whose
constant |μ_0| is attained to 10⁻⁸–10⁻¹⁵: g_1 = |μ_0| + μ_1 with μ_1 ∈ [λ_A, λ_{A,2}] and both tiny. Every Poincaré tool has a
loss larger than that, and every structural input (positivity, irreducibility, parity, killing monotone to the edge)
is shared by the falsifier combs, for which μ_1 < 0 by 0.3–23 % of |μ_0|. The route therefore reproduces H1⁺ / the polar
capacity with precision but adds no mechanism; the Λ-specific facts remain the NUMERICAL ones: μ_1^{ev} = 0⁺, μ_0^{odd} = 0⁺,
𝔊_T = 0 to 5 digits, and the Tate-nullness of the low cluster.

## Next concrete step

Prove or refute the uniform range statement for the Tate function: y_T = a_T^{−1}χ_ev ∈ L²(I_T) with ‖y_T‖ ≤ C(T) explicit,
via the ansatz y = χ_+ν, L_+ν = 1, starting from Proposition 4.2 (identity level; explains the Tate-nullness of the
cluster if true). Record in the index: NO-GO class 𝒦_gap (Theorem 6.1); Proposition 4.2; the NUMERICAL values
W_ev(0) = −½, W_odd(0) = +½ (𝔊_T = 0, S^{Sch}_T = −D_pol to 5–6 digits) at the 17 windows T = 0.600, …, 1.000 and at
log 2, ½log5∓10⁻³, with N = 40 and N = 80.
