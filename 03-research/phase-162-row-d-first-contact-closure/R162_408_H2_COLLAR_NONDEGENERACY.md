# R162_408 — H2: collar nondegeneracy (NE) quantified

Mechanism H2.

Status: **(NE) PROVED in exact asymptotic form (Theorem 3.1, Schur/Feshbach on the collar), with
explicit κ'(δ). The ‖R_LG‖² form is DECIDED: it is cosmetic at a fixed G and FALSE as a universal
(Müntz-type) inequality (Prop. 5.1). Regime II atom: PROVED subleading (Prop. 4.3). Content of
Conjecture 7.1 is moved entirely to (LB) plus one new open item (UC_edge, edge non-flatness).**
Gate 1: OPEN. Row D: OPEN.

- PROVED (Thm 3.1). λ_A(T_*+δ) = −(1 + O(q_δ)) q_δ, q_δ := max eig of the Gram form
  Q_δ(F,F') = ⟨ξ_F^δ, A_δ^{−1}ξ_{F'}^δ⟩ on N, A_δ = 𝔞_{T'} compressed to (EN)^⊥ ∩ 𝒫_{T'}. Hence
  |⟨ξ_G^δ, F_δ|_{C_δ}⟩| = (1+o(1)) Q_δ(G,G) along the Lemma-5 sequence.
- PROVED (Thm 3.3). Q_δ(F,F) ≤ (1+o(1))·2‖ξ_F^δ‖²_{L²(C_δ^+)}/log(1/δ) for every F ∈ N, with
  equality asymptotically under the profile-regularity hypothesis (P).
  So κ'(δ) = 2‖ξ_G‖²_{L²(T_*,T_*+δ)} / log(1/δ) · (1+o(1)): **δ × (collar mean square of ξ_G) / log(1/δ).**
- The order is **not universal.** It is set by the edge germ of ξ_G:
  bounded ξ_G with ξ_0 ≠ 0 gives 2ξ_0²δ/log(1/δ). Jet order k gives ≍ δ^{2k+1}/log(1/δ). A log-type
  edge (heuristic generic case, §4.2) gives ≍ 2C²δ. A flat edge gives smaller than any power.
  The case "G(T_*−) = c ≠ 0" (which would give (c²/2)δ log(1/δ)) is **excluded** (Prop. 4.1, under a
  regularity hypothesis).
- DECIDED (Prop. 5.1). No inequality |edge jets of ξ_F| ≥ c‖R_LF‖ (or the reverse) holds on L²(I_{T_*}),
  nor on any subspace of codimension < L − k − 1. On the finite-dimensional N, ‖R_LG‖ ≍ ‖G‖ = 1 is a
  constant, so the factor ‖R_LG‖² in (NE) carries no information.
- F1 and F3 pass. The theorem is valid verbatim at positive strictly decreasing ground states and for
  every weight a (including DH). So (NE) is non-arithmetic, as R162_406 §7 predicted.

Notation as in R162_404–406. N = ker H_{T_*}, dim N < ∞, spectral gap g > 0 of H_{T_*} on N^⊥ ∩ 𝒫_{T_*}
(compact resolvent). T' = T_*+δ, C_δ = C_δ^+ ∪ C_δ^−, L(s) := log(1/s).

## 0. Corpus check

- **R162_405 §4.4** states the Schur-complement heuristic λ_δ ≈ −⟨ξ, 𝒞_δ^{−1}ξ⟩ with 𝒞_δ ≳ log(1/δ).
  It marks this as not proved for lack of a lower bound on the collar block. §§2–3 below supply that
  bound (Lemma 2.2, from the Lévy–Khintchine form of M and a sharp log-uncertainty estimate) and the
  Feshbach argument. This is the main new content.
- **R162_405 Lemma 1.1, Thm 3.1(d)** (ξ_G ≠ 0 on every collar) is the qualitative version of Thm 3.1.
- **R162_406 Remark 2(ii), §4.3, §7** (edge value c; log singularity; regime-II sub-question on the
  sign of εG(T_*−)(½log(1/s) − ℓ_{p^k})). Prop. 4.1 shows c = 0 under regularity, which makes that
  sub-question moot at leading order (Prop. 4.3).
- **P124_004 §5** (birth terms have no divided rate): consistent. The rate here is quadratic in ξ
  (second order), not a first-order birth term.
- R160 survey / brief: no entry on the collar Schur complement.

## 1. Two structural inputs

**(M1) Lévy–Khintchine form of M.** κ(x) = −Σ_{j≥0}e^{−a_j|x|} < 0, κ(x) = −1/(2|x|) + O(1) as x → 0,
and κ is integrable at ∞. For w ∈ 𝒬 supported in a bounded interval I (zero extension),

    𝔪(w) = c_loc‖w‖² + ½∬_{I×I}(w(t)−w(u))²|κ(t−u)| du dt + ∫_I w(t)² k_I(t) dt,
    k_I(t) := ∫_{ℝ∖I}|κ(t−u)| du = ½ log(1/dist(t,∂I)) + O(1).                          (1.1)

This is the standard rewriting of the archimedean term (a conditionally negative-definite symbol
m(ξ) = log|ξ| + O(1) as |ξ| → ∞, with Lévy density |κ|). The coefficient of log|ξ| is exactly 1,
because ∫(1−cos xξ)|κ(x)|dx = ∫_0^1(1−cos xξ)x^{−1}dx + O(1) = log|ξ| + O(1).

**(M2) Hilbert's inequality.** For adjacent or disjoint intervals J_1, J_2,
|∬_{J_1×J_2}κ(t−u)v(t)w(u)| ≤ C_H‖v‖‖w‖, with C_H = π/2 + O(1), uniformly in the lengths ≤ 1.
In particular F ↦ γ_F|_{C_δ^+} is bounded L²(I_{T_*}) → L²(C_δ^+), and ξ_F^δ ∈ L²(C_δ) for every
F ∈ L²(I_{T_*}), with ‖ξ_F^δ‖_{L²(C_δ)} → 0 as δ → 0.

## 2. The collar block

**Lemma 2.1 (sharp log-uncertainty).** If w ∈ L²(ℝ) is supported in an interval of length δ ≤ 1,
then for every ε ∈ (0,1),
∫ log(1+|ξ|)|ŵ(ξ)|² dξ/2π ≥ (1−ε)log(1/δ)(1 − 2δ^ε/π)‖w‖².

*Proof.* ‖ŵ‖_∞² ≤ δ‖w‖². So the mass of ŵ in |ξ| ≤ δ^{ε−1} is at most 2δ^{ε−1}·δ‖w‖²/2π. On the
complement, log(1+|ξ|) ≥ (1−ε)log(1/δ). ∎

**Lemma 2.2 (collar block).** For w_c ∈ 𝒬 supported in C_δ,
(log(1/δ))(1 − o(1))‖w_c‖² ≤ 𝔞_{T'}(w_c) ≤ 𝔪(w_c) + C‖w_c‖². The upper bound is attained,
𝔞_{T'}(w_c) = log(1/δ)(1+o(1))‖w_c‖², for w_c(T_*+δu) = δ^{−1/2}φ(u) with φ fixed, or more generally
under (P) of §3.

*Proof.* Lower bound: 𝔪 ≥ ∫m(ξ)|ŵ|² and Lemma 2.1 with ε = ε(δ) → 0 slowly (ε = 1/√log(1/δ)).
The prime part: ⟨(B_{T'}+B_{T'}^*)w_c, w_c⟩ is O(‖w_c‖²), because the shifts are by log d ≥ log 2 > 2δ.
Only the pair C_δ^− → C_δ^+ with log d ∈ (2T_*, 2T_*+2δ) can overlap, which is d = n_0 in regime II,
with weight ℓ_{n_0}. Upper bound: scaling in (1.1). ∎

**Lemma 2.3 (uniform positivity of the complement).** Let W_δ = (EN)^⊥ ∩ 𝒫_{T'} ∩ 𝒬 and A_δ = 𝔞_{T'}|_{W_δ}.
For δ small, A_δ(w) ≥ (g/2)‖w‖² on W_δ, and A_δ(w) ≍ 𝔪(w) + ‖w‖² uniformly in δ.

*Proof.* Write w = w_i + w_c (interior/collar). w ⊥ EN iff w_i ⊥ N, since the supports are disjoint.
Primitivity on I_{T'} gives ⟨e^{±t/2}, w_i⟩ = −⟨e^{±t/2}, w_c⟩ = O(δ^{1/2}‖w_c‖). So w_i = p + φ,
with p ∈ 𝒫_{T_*} ⊥ N and φ in a fixed 2-dimensional interior span, ‖φ‖_𝒬 = O(δ^{1/2}‖w_c‖).
Then 𝔞_{T'}(w) = 𝔞_{T_*}(p) + 𝔞_{T'}(w_c) + 2𝔞(p, w_c) + O(δ^{1/2}‖w‖²_𝒬).
Here 𝔞_{T_*}(p) ≥ g‖p‖² (spectral gap). The collar term is ≥ (log(1/δ) − o)‖w_c‖² (Lemma 2.2).
The cross term is ≤ 2C‖p‖‖w_c‖, by (M2) for the kernel and the finiteness of the comb (B-shifts map
the collar into the interior with norm ≤ Σℓ_d). For log(1/δ) ≥ 4C²/g + g, the 2×2 form is
≥ (g/2)(‖p‖² + ‖w_c‖²). Comparability with 𝔪 + ‖·‖²: 𝔞 ≤ 𝔪 + C‖·‖², and
𝔞 = θ𝔞 + (1−θ)𝔞 ≥ θ(𝔪 − C‖·‖²) + (1−θ)(g/2)‖·‖², with θ small. ∎

**Corollary 2.4 (collar Schur complement).** For w_c supported in C_δ, put
S_δ(w_c) := inf{A_δ(w) : w ∈ W_δ, w|_{C_δ} = w_c}. Then
S_δ(w_c) = 𝔞_{T'}(w_c) + O(‖w_c‖²) and S_δ(w_c) ≥ log(1/δ)(1−o(1))‖w_c‖².

*Proof.* Minimise over p in the 2×2 bound. The cross term removes at most C²‖w_c‖²/g. ∎

## 3. Exact asymptotics of the collar pairing (PROVED)

By R162_405 Lemma 2.1, 𝔞_{T'}(EF, w) = ⟨ξ_F^δ, w_c⟩ for F ∈ N and w ∈ 𝒫_{T'} ∩ 𝒬. Also
𝔞_{T'}(EF, EF') = 0. With respect to 𝒫_{T'} = EN ⊕ W_δ, the form is therefore the block form
[[0, b_δ],[b_δ^*, A_δ]], with b_δ(F, w) = ⟨ξ_F^δ, w_c⟩. Define the N × N Gram form

    Q_δ(F, F') := ⟨b_δ(F,·), A_δ^{−1} b_δ(F',·)⟩ = sup_{w∈W_δ} ⟨ξ_F^δ, w_c⟩²/A_δ(w)   (diagonal),
    q_δ := max_{F∈N, ‖F‖=1} Q_δ(F,F).                                                     (3.1)

By Cor. 2.4, Q_δ(F,F) = sup_{w_c} ⟨ξ_F, w_c⟩²/S_δ(w_c), a pure collar quantity.

**Theorem 3.1 (Feshbach asymptotics).** Let T_* be a first-contact window. As δ ↓ 0, q_δ → 0 and

    λ_A(T_*+δ) = −q_δ(1 + O(q_δ)).                                                        (3.2)

The negative spectrum of H_{T'} near 0 consists of dim N eigenvalues −σ_i(1+O(q_δ)), where the σ_i are
the eigenvalues of Q_δ. For the Lemma-5 sequence F_δ → G (G the limit of the normalised top
eigenvectors of Q_δ),

    ⟨ξ_G^δ, F_δ|_{C_δ}⟩ = λ_δ⟨F_δ, EG⟩ = −Q_δ(G,G)(1+o(1)).                              (3.3)

*Proof.* q_δ ≤ sup_F ‖ξ_F^δ‖²_{L²}/(log(1/δ)(1−o(1))) → 0, by (M2) and Cor. 2.4.
Let λ < g/4. By Lemma 2.3, A_δ − λ ≥ g/4 on W_δ. The Schur complement shows that λ is an eigenvalue
iff 0 is an eigenvalue of the N×N matrix −λ − b_δ(A_δ−λ)^{−1}b_δ^*. Now
(A_δ−λ)^{−1} = A_δ^{−1}(1 + O(λ)), and λ = O(q_δ) on any such root. So the roots are
λ = −σ_i(1+O(q_δ)). The eigenvector is (F, −(A_δ−λ)^{−1}b_δ^*F), with norm² = ‖F‖² + O(q_δ).
All other spectrum is ≥ g/4. (3.3) follows from R162_405 (2.2). The eigenvector's N-component
converges to the top eigenvector of Q_δ, which identifies G along subsequences. ∎

So **(NE) holds with κ'(δ) = Q_δ(G,G)**, up to (1+o(1)), for every first contact. It is an identity,
not an inequality. What remains is the size of Q_δ.

**Hypothesis (P) (profile regularity).** Let φ_δ(u) := ξ_G(T_*+δu)·δ^{1/2}/‖ξ_G‖_{L²(C_δ^+)}, u ∈ (0,1).
(P) means 𝔪(δ^{−1/2}φ_δ((·−T_*)/δ)) = log(1/δ)(1+o(1)), that is, the rescaled log-seminorm
½∬|φ_δ(u)−φ_δ(v)|²/(2|u−v|) du dv + ∫φ_δ²·½log(1/dist(u,{0,1})) is o(log(1/δ)).
(P) holds when ξ_G(T_*+s) is (i) continuous at s = 0 with nonzero value, (ii) ~ ξ_k s^k, or
(iii) ~ C·L(s)^β for any β ∈ ℝ (in each case φ_δ converges in the log-Sobolev space, or tends to a
constant with log-small oscillation).

**Theorem 3.3 (size of κ').** For every F ∈ N,
Q_δ(F,F) ≤ (1+o(1))·2‖ξ_F^δ‖²_{L²(C_δ^+)}/log(1/δ). Under (P) for F = G, equality holds:

    κ'(δ) = Q_δ(G,G) = (2/log(1/δ))·∫_{T_*}^{T_*+δ}|ξ_G(t)|² dt · (1+o(1)).                 (3.4)

*Proof.* The factor 2 comes from the two collars: w = w_+ + εJw_+, ⟨ξ,w⟩ = 2⟨ξ_+,w_+⟩, and
S_δ(w) = 2 log(1/δ)(1+o(1))‖w_+‖² (the inter-collar coupling is O(‖w‖²), including the regime-II
atom). Upper bound: Cauchy–Schwarz and Cor. 2.4. Lower bound: take w_+ = ξ_G1_{C_δ^+}. Under (P) and
Lemma 2.2, S_δ(w) = 2 log(1/δ)(1+o(1))‖ξ_+‖². ∎

**Corollary 3.4 (models; exact leading terms).** With L = log(1/δ):
(a) ξ_G(T_*+s) → ξ_0 ≠ 0: κ' = 2ξ_0²δ/L.
(b) ξ_G(T_*+s) = ξ_k s^k(1+o(1)): κ' = 2ξ_k²δ^{2k+1}/((2k+1)L).
(c) ξ_G(T_*+s) = −C L(s)^{1/2}(1+o(1)) (the heuristic generic case, §4.2): κ' = 2C²δ(1+o(1)).
(d) ξ_G(T_*+s) = −(c/2)L(s)(1+o(1)) (an edge value c ≠ 0 of G): κ' = (c²/2)δL. This is excluded by
Prop. 4.1.
(e) ξ_G flat at T_*+ (not excluded): κ' = o(δ^n) for every n.

This matches R162_405 §4.4: λ_δ = O(δ/log(1/δ)) for bounded ξ, with first δ-derivative 0.

## 4. Edge behaviour of G and the three regimes

**Proposition 4.1 (no edge value).** Let G ∈ N. Assume G is Dini-continuous on (T_*−η, T_*) with a
one-sided limit c = G(T_*−). Then c = 0.

*Proof.* On I_{T_*}, H_{T_*}G = 0 holds as the distributional equation MG − (B+B^*)G = r. Under the
Dini hypothesis it holds pointwise near T_*−. By (1.1), at t = T_*−s,
MG(t) = c_locG(t) + p.v.-regional part + k_I(t)G(t). The regional part is
∫_I(G(t)−G(u))|κ(t−u)|du, which is bounded by Dini continuity. And k_I(t)G(t) = ½cL(s) + O(1).
(B+B^*)G and r are bounded near the edge: the translates read G at interior points, or vanish. So
½cL(s) = O(1), which forces c = 0. ∎

(Without the Dini hypothesis the statement is open. G ∈ 𝒬 does not have traces in general.)

**4.2 (heuristic generic edge profile, HEURISTIC).** Wiener–Hopf factorisation of the symbol log|ξ|
(the "α → 0" limit of the s^α edge law for |ξ|^{2α}) predicts G(T_*−s) ≍ C'·L(s)^{−1/2}. Then
γ_G(T_*+s) ≈ ½∫_0 G(T_*−v)(s+v)^{−1}dv ≈ C'L(s)^{1/2}. This is Cor. 3.4(c), with C = C' and
κ' ≍ δ. The half-power of the log is not proved. Only the dichotomy "(d) excluded, (a)–(c)/(e)
possible" is proved.

**Proposition 4.2 (regimes I, I′).** In regimes I and I′ the collar germ is
ξ_G(T_*+s) = −γ_G(T_*+s) − Σ_{d<e^{2T_*}}ℓ_dG(T_*+s−log d) − r(T_*+s).
The comb is evaluated strictly inside I_{T_*} (R162_406 Lemma 1.1(ii)). So its jets at s = 0 are
interior jets of G at the points T_*−log d. The germ of ξ_G at T_*+ is therefore
(Gamma boundary germ) + (interior jets of G at T_* − log d) + (jet of r). In I′ the composite threshold
contributes nothing (R162_406 Prop. 3.3).

**Proposition 4.3 (regime II: the new atom is subleading).** In regime II, ξ_G gains
−εℓ_{p^k}G(T_*−s). Assume the hypothesis of Prop. 4.1, so G(T_*−s) = o(1).
(i) If γ_G + comb + r → ξ_0 ≠ 0, then the atom changes κ' by the factor 1 + o(1).
(ii) In case 4.2 the cross term in (3.4) is 2εℓ_{p^k}·C·C'·δ·(1+o(1)), divided by L. That is
relative order 1/L, below the unresolved relative error O(L^{−1/2}) of the bounded part.
(iii) In block form the atom also enters A_δ, through the inter-collar coupling ℓ_{p^k}⟨J-reflected
w_−, w_+⟩ = O(‖w‖²). That is relative order 1/L in S_δ.
So at the orders proved, the Λ-weight that meets the Gamma edge in regime II **does not affect κ'**.
The R162_406 §7 sub-question on the sign of εG(T_*−)(½L − ℓ_{p^k}) is void, because G(T_*−) = 0,
and because Q_δ > 0 is a square, which carries no sign.

## 5. Can κ' be expressed through ‖R_LG‖²? (DECIDED)

**Fixed G.** N is finite-dimensional and R_L is injective on N, so ‖R_LG‖ ≍_N ‖G‖ = 1. So
"κ'(δ)‖R_LG‖²" differs from κ'(δ) by an N-dependent constant. The δ-dependence of (NE) comes
entirely from the edge germ of ξ_G (Thm 3.3). In particular, (NE) with some κ' > 0 is **equivalent**
to λ_δ < 0 (by (3.3)), which is R162_405 Thm 3.1(a).

**Proposition 5.1 (no universal Müntz/Laplace-type inequality).** Fix L and k, and let
J_0, …, J_k be the edge-jet functionals F ↦ ∂_s^jξ_F(T_*+s)|_{s=0}, defined on C_c^∞(I_{T_*}).
(a) There is no C with Σ_j|J_jF| ≤ C‖R_LF‖ on C_c^∞(I_{T_*}) ∩ L²-unit sphere, whenever some
d ∈ [2, e^{2T_*}) is a prime power.
(b) There is no c > 0 with Σ_j|J_jF| ≥ c‖R_LF‖ on any subspace of codimension < L − k − 1.
So edge jets and Gamma moments are **linearly independent** data, and neither controls the other
outside a finite-dimensional set (such as N) fixed in advance.

*Proof.* (a) Take F_ε = ε^{−1/2}ψ((t−t_0)/ε) + parity image, with t_0 = T_* − log d. Then ‖F_ε‖ ≍ 1,
|K_{F_ε}(a_m)| = O(ε^{1/2}), and γ_{F_ε} is analytic at T_* with jets O(ε^{1/2}). But
J_jF_ε ∋ −ℓ_dF_ε^{(j)}(t_0) ≍ ε^{−1/2−j}ψ^{(j)}(0). (b) R_L: C_c^∞ → ℂ^L is onto, because the
exponentials are independent. Its restriction to ∩ker J_j (codim ≤ k+1) has rank ≥ L−k−1 > 0, and
on this subspace the left side is 0. ∎

**Consequence for Conjecture 7.1.** The ‖R_LG‖² normalisation cannot be the mechanism. Any argument
must use a property of the unknown N. Combined with Thm 3.1, Conjecture 7.1 is **equivalent** to:

    (LB*)  λ_A(T_*+δ) ≥ −κ(δ) with κ(δ) = o(Q_δ(G,G)) along δ ↓ 0.

By (3.2) this is literally false at any first contact, which is the intended contradiction. So
(NE) is now a theorem, and all the content sits in (LB*). Because κ' can be o(δ^n) (Cor. 3.4(e)), a
universal κ in (LB) needs a companion statement:

**Open item UC_edge (edge non-flatness).** For G ∈ N at a first contact, ξ_G does not vanish to
infinite order at T_*+. Quantitatively: ‖ξ_G‖²_{L²(C_δ^+)} ≥ c δ^{A} for some A that is universal,
or at least computable from T_*. This is a unique-continuation statement at the edge for 𝓗EG, where
𝓗 = M − B − B^* − r is the free operator on ℝ, 𝓗EG = 0 on I_{T_*}, and ξ_G = 𝓗EG on the collar.
Given UC_edge with exponent A, (LB) needs κ(δ) = o(δ^{A}/log(1/δ)). In the generic case 4.2 it needs
κ = o(δ).

## 6. Falsifiers

**F1.** At a window T with ground state F, λ_A(T) = λ > 0 and strict decrease, the block form is
[[λ, b],[b^*, A]] with A − λ ≥ gap > 0 on the complement. The proof of Thm 3.1 gives
λ_A(T+δ) − λ = −Q_δ(F,F)(1+o(1)) verbatim, and Thm 3.3 holds verbatim. At a plateau window ξ = 0, so
Q_δ = 0 and λ_A is constant, which is consistent. The theorem proves nothing false. It confirms that
(NE) holds at non-first-contact windows, so it is not the arithmetic input. **PASSED.**

**F3.** The ingredients are (M1) (archimedean only), (M2), the gap, finiteness of the comb, and
R162_405 Lemma 2.1. They hold for a = Λ + η_0 and for Davenport–Heilbronn data (whose first
contacts exist). Changing a(n_0) at a composite threshold adds an atom −n_0^{−1/2}a(n_0)G(T_*−s),
which is subleading by Prop. 4.3. Nothing is Λ-specific. **PASSED** (as a non-arithmetic theorem).

## 7. Status

- PROVED: Lemmas 2.1–2.3, Cor. 2.4, Thm 3.1 (exact Feshbach asymptotics, (NE) as an identity),
  Thm 3.3 (upper bound always; equality under (P)), Cor. 3.4, Prop. 4.2, Prop. 5.1.
- PROVED under the Dini edge hypothesis: Prop. 4.1 (G(T_*−) = 0) and Prop. 4.3 (regime-II atom
  subleading).
- HEURISTIC: §4.2 (edge profile L^{−1/2}, κ' ≍ δ).
- Inputs used as standard: (M1), the Lévy–Khintchine form of the archimedean term (normalisation
  constant c_loc irrelevant); (M2), Hilbert's inequality.
- OPEN: (LB*); UC_edge; (P) for the actual G; the Dini regularity of kernel vectors at the edge.
- Answer to the task. (1) κ'(δ) = 2‖ξ_G‖²_{L²(T_*,T_*+δ)}/log(1/δ): order δ/log(1/δ) × (edge germ of
  ξ_G)². It is not universal: δ·(log)^{±} to super-polynomial, and δ log δ is excluded. (2) It is
  expressible only through edge germs. ‖R_LG‖² is a constant on N, and no universal Müntz inequality
  links the two. Regime II is subleading.

GATE 1: OPEN. Row D: OPEN.

Files edited: this file only.
