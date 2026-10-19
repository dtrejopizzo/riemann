# R184_014 — Erratum on chaos/Witt levels (PROVED) and route O184.093a toward L\*\_comp (isolated obstruction)

Pure mathematics, no numerics, no web.
Inputs: R184_010 (+ editor's note), R184_013 §1–§5, R184_093 §1.6–§1.7, R184_001 §1 and Prop 2.2, R164_201 §1–§3,
R163_803 §1 (Witt identity, eq. (1.2)), R163_891 §5. RH is not asserted, nor the closure of row D.

## State

| # | Statement | Label |
|---|---|---|
| A1 | Order-k chaos (level 1, m squarefree, ω(m)=k) in T(X): Var ≍_k X^{1−2a}(log log X)^{k−1}/((k−1)! log X), with a = θ/(1−θ) | PROVED (§A.2; lower constant with variance rounding ≥ v₀, or CITED-EQ) |
| A2 | Sum over all orders: Var ≍ X^{1−2a}(log X)^{v−1} (v = mean variance of ε_p ≤ 1); peak at k ≈ v log log X. No order dominates in power | PROVED (Selberg–Delange, standard CITED) |
| A3 | Witt level k (linear): contribution to N ≍ x^{(1−θ)/(2k)}(log x)^{−1/2} if θ < 1/(2k+1); ≍ x^θ(log log)^{1/2} at θ = 1/(2k+1); O(x^θ) if θ > 1/(2k+1) | PROVED |
| A4 | Mixed components with one level-1 linear prime and a fixed cofactor n: same power X^{1−2a}; components with squarefull support: power ≤ X^{1/2−2a}+; deterministic part E T(X) ≪ X^{1/2−a} | PROVED (upper bounds) |
| A5 | E\|T(X)\|² ≪ X^{1−2a}(log X)^{O(1)} and ≫ X^{1−2a}/log X: the exponent (1−θ)/2 of the random method **does not change**; Theorem L (lower bound) **does not change** | PROVED |
| A6 | Mandatory amendments: R164_201 §1 (l. 33), R184_001 item 1, §1.1 and §1.3 row 1 | PROVED (text in §A.4) |
| B1 | Steps (i)–(iii) of O184.093a: necessity of polynomial growth (Prop 2.2), one-sided bound of log\|R\| (no branches), and for the Dirichlet **polynomial** P_N = Σ_{p≤N} ε_p p^{−u}: second and fourth moment, mean of Re P_N, Paley–Zygmund ⟹ Re P_N ≥ cT^{(1−2σ_u)/2}/√log T on measure ≫ T | PROVED (§B.2) |
| B2 | Step (iv) "log\|R(σ+it)\| ≈ Re P_N(t) for almost all t" | **FAILS in general** (§B.3) |
| B3 | Counterexample to the route in the relaxed class (no integrality, \|ε_p\| = 1 ≥ ‖p^a‖, ε bounded at all Witt levels): R = L(u,χ). Polynomial growth of ζ_𝒫; error N_𝒫 − cx ≪ x^{max(2/5,(1+θ)/3)+ε} < x^{(1−θ)/2} for θ < 1/5 | PROVED (growth: exact; error: van der Corput + Vaaler, standard) |
| B4 | Consequence: no proof of L\*\_comp can use only "\|ε_p\| ≤ C, \|ε_p\| ≥ ‖p^a‖"; it must use ε_p ≡ −p^a (mod 1) | PROVED (from B3) |
| B5 | Exact obstruction: the zeros of ζ_𝒫 in the strip that are **not** target zeros (divisor of R = ζ_𝒫/ζ_target). **Theorem B.4:** if R is holomorphic and zero-free in Re u > σ₁ with σ₁ < ½ (hypothesis (ZF_R)), then N_𝒫 − cx ≠ O(x^{σ}) for every σ < (1−θ)/2 | CONDITIONAL on (ZF_R); with (ZF_R) the proof is written (§B.4) using CITED: Titchmarsh 9.6, Montgomery–Vaughan, EQ |
| B6 | Reformulation: L\*\_comp ⟺ (with loss ε) the class of R₀ = ∏_p(1−p^{−u})^{−(⌊p^a⌉−p^a)} in the group {tame R}/{bounded integer Euler products} is nontrivial | ARGUED (§B.5) |
| B7 | L\*\_comp (every admissible rounding) | **OPEN** |
| B8 | FLAG equidistribution of p^a mod 1 | CITED from memory (Vinogradov); used only in the lower constant of A1 and in B1 for general roundings |
| B9 | Row D | unchanged |

---

# Part A — Erratum: chaos and Witt-level bookkeeping

## A.1 Setup
Notation from R163_803/R164_201: a = θ/(1−θ) ∈ (0,½), X = x^{1−θ}, x^θ = X^a, u = s/(1−θ), w = u − a.
ζ_𝒫(s) = ζ(w)F(w)G(w), F a finite product (exceptional set 𝓔 ⊂ {2,3}×finite),
G(w) = ∏_{p,k}(1 − p^{−k(w+a)})^{−ε_{p,k}}, H = FG = Σ γ_m m^{−w}, and

  N_𝒫(x) = (1−θ)xΣ_{m≤X}γ_m/m + ζ(−a)Σ_{m≤X}γ_m m^a + x^θ T(X),  T(X) = Σ_{m≤X}γ_m Φ(X/m).

Write γ = f * g, with g the coefficients of G. Since log G = Σ_{p,k,j} j^{−1}ε_{p,k}p^{−jk(w+a)} is **linear** in ε,
g is multiplicative with g(p) = ε_{p,1}p^{−a} and, for m squarefree, g(m) = ∏_{p|m}ε_{p,1}·m^{−a}.
At p² we have g(p²) = p^{−2a}(ε_{p,1}²/2 + ε_{p,1}/2 + ε_{p,2}): degree 2 in the same variable plus the level-2 term.
F only convolves with f̃(d)d^{−a}, f̃ supported on {2,3}-smooth integers with polynomial growth in the exponents;
since Σ_d|f̃(d)|d^{−a−η} < ∞ for every η > 0, F does not alter any exponent and we omit it.

Random model: ε_{p,k} independent, mean 0, |ε| ≤ C, v_p := Var ε_{p,1}. For the lower constant a rounding with
v_p ≥ v₀ > 0 suffices, e.g. b ∈ {⌊z⌋−1, ⌊z⌋+2} with P(⌊z⌋+2) = ({z}+1)/3: mean z, variance ≥ 2, |ε| ≤ 3.
With the unbiased rounding of R163_803 (v_p = {p^a}(1−{p^a})), the lower bound uses the equidistribution of p^a mod 1
(CITED-EQ, FLAG from R184_010 #8).

**Lemma A.0.** For Y ∈ [1, 6/5] one has Φ(Y) ≥ 0.17.
*Proof.* −ψ(Y) = 3/2 − Y ∈ [0.3, 0.5] and |r(Y)| ≤ a/(4Y) ≤ 1/8. ∎

## A.2 Order-k chaos at level 1 (A1, A2)
Let T^{(k)}(X) := Σ_{m≤X, μ²(m)=1, ω(m)=k} (∏_{p|m}ε_{p,1}) m^{−a}Φ(X/m). Products of distinct variables are
orthogonal, so

  E|T^{(k)}|² = Σ_{m≤X, μ²=1, ω=k} (∏_{p|m}v_p) m^{−2a}Φ(X/m)².

*Upper bound.* |Φ| ≤ 1 and v_p ≤ C². By Landau (π_k(y) ~ y(log log y)^{k−1}/((k−1)! log y), standard CITED) and
partial summation:

  E|T^{(k)}|² ≤ C^{2k} Σ_{m≤X, ω=k} m^{−2a} ≍ C^{2k} X^{1−2a}(log log X)^{k−1}/((1−2a)(k−1)! log X).

*Lower bound.* Restrict to m ∈ (5X/6, X], where Φ(X/m) ≥ 0.17 (Lemma A.0). Then
E|T^{(k)}|² ≫ v₀^k X^{−2a}·#{m ∈ (5X/6, X] : ω(m)=k} ≫_k X^{1−2a}(log log X)^{k−1}/((k−1)! log X).

For k = 2 this gives X^{1−2a}log log X/log X: **the same order** as the linear one (k = 1: X^{1−2a}/log X), with one extra
log log factor. This confirms the erratum of R184_093 §1.6.

*All orders.* Σ_k E|T^{(k)}|² ≤ Σ_{m≤X}μ²(m)C^{2ω(m)}m^{−2a} ≍ X^{1−2a}(log X)^{C²−1}. With v_p ≡ v (or v on average),
Selberg–Delange gives ≍ X^{1−2a}(log X)^{v−1}. The general term is Poisson-type in k with parameter v log log X. The
maximum is at k ≈ v log log X. **No fixed order dominates, and all have power X^{1−2a}.**

## A.3 Witt levels and mixed components (A3, A4, A5)
*Linear level k.* W_k(X) := Σ_{p^k≤X} ε_{p,k}p^{−ka}Φ(X/p^k) has

  E W_k² ≍ Σ_{p≤X^{1/k}} p^{−2ka} ≍ X^{(1−2ka)/k}/log X  (a < 1/(2k)),  ≍ log log X  (a = 1/(2k)),  ≍ 1  (a > 1/(2k)).

The upper bound is immediate. The lower bound comes from restricting to p^k ∈ (5X/6, X] and using Lemma A.0.
Hence x^θ·rms W_k ≍ X^{1/(2k)}(log X)^{−1/2} = x^{(1−θ)/(2k)}(log x)^{−1/2} if θ < 1/(2k+1). This is > x^θ
exactly when θ < 1/(2k+1) (k = 2: θ < 1/5; k = 3: θ < 1/7), and is always ≤ x^{(1−θ)/4} = o(x^{(1−θ)/2}).

*Mixed.* Let m = q·n with q a linear level-1 prime, q ∤ n, and n a fixed cofactor (any pattern). The component
has variance ≍ |coef(n)|²n^{−2a}·(X/n)^{1−2a}/log X, the same power. Example: n = p² at level 2 gives
X^{1−2a}/log X·Σ_p p^{−2}. On the other hand, if m is squarefull (every prime with total exponent ≥ 2), Σ_{m≤X sqfull}m^{−2a}
≍ X^{1/2−2a} (for a < 1/4) is a lower power.

*Deterministic part.* E g(p^α) can be ≠ 0 for α ≥ 2 (e.g. E g(p²) = v_p p^{−2a}/2). So
E T(X) = Σ_{s≤X sqfull} E g(s)·Φ(X/s)·(…) ≪ Σ_{s≤X sqfull}|E g(s)| ≪ X^{1/2−a+ε}: there is a bias of size at most
X^{1/2−a}, i.e. at most x^{(1−θ)/2} in N. (Whether it is a genuine secondary term or cancels: ARGUED/OPEN, not needed here.)

*Total (A5).* E[g(m)g(m′)] = 0 unless every prime dividing exactly one of m, m′ does so with exponent ≥ 2.
Also |g(p^α)| ≤ P_C(α)p^{−αa}, with P_C the coefficients of ∏_k(1−z^k)^{−C}, which are subexponential (Lemma W(ii)).
Write m = ns, m′ = ns′ with n squarefree common and s, s′ squarefull:

  E|T|² ≪ Σ_{n≤X} n^{−2a}C^{2ω(n)}(Σ_{s≤X/n, sqfull}P(s)s^{−a})² ≪ Σ_n n^{−2a}C^{2ω(n)}(X/n)^{1−2a+ε} ≪ X^{1−2a+2ε}.

The lower bound ≫ X^{1−2a}/log X comes from k = 1. Hence x^θ·rms T = x^{(1−θ)/2+o(1)}: **the exponent (1−θ)/2 is left
intact**, and only the log powers change (from (log X)^{−1/2} to (log X)^{(v−1)/2+o(1)}).

## A.4 What is amended and what is not (A6)
- **R164_201 §1, l. 33.** The sentence "The higher chaos (j ≥ 2, k ≥ 2) converges for every a > 0" is **false** in
  the sense of the variance of T. The correct statement: *log G* minus its level-1 linear term converges absolutely for
  Re w > ½ − a (j ≥ 2) and Re w > 1/k − a (level k), and this is indeed true. But exp mixes the orders: in T(X), every
  chaos term with one level-1 linear prime has variance of power X^{1−2a}, and the linear level k contributes x^{(1−θ)/(2k)}
  for θ < 1/(2k+1). It should read: "the exponent (1−θ)/2 comes from the critical line Re w = ½ − a of log G, shared by
  the linear term and all the chaos generated by exp; the linear term is the minimal-order representative, not the
  dominant one".
- **R184_001 item 1 and §1.1.** "The only piece that depends on θ is the linear chaos" becomes: "the power X^{1−2a} is
  common to every chaos order containing a level-1 linear prime; levels k ≥ 2 depend on θ for
  θ < 1/(2k+1)".
- **R184_001 §1.3 row 1** ("k ≥ 2, all p: O(x^{θ+ε}) PROVED"): replace with "level k: O(x^{θ+ε}) if
  θ ≥ 1/(2k+1); ≍ x^{(1−θ)/(2k)}(log)^{−1/2} if θ < 1/(2k+1); always o(x^{(1−θ)/2})".
- **What does not change.**
  - The random upper bound e(θ) ≤ max(θ, (1−θ)/2) + ε: R163_803 proves it from the convergence of log G in
    Re w > ½ − a (R163_891 §5), not from the convergence of the chaos. Moreover A5 confirms it directly.
  - **Theorem L**: its proof (§3 of R164_201) uses E in full, via the distribution in residues, Lemma W and Franel. It does not use
    the chaos decomposition.
  - The exponent of L\*: (1−θ)/2.
  - R184_010 §5 and R184_013 §1 were already correct: the composites do not cancel separately; they are exp(log R).

---

# Part B — L\*\_comp via route O184.093a

## B.1 Target statement
**L\*\_comp.** Let θ < 1/3 and 𝒫 ∈ 𝒦_θ(C). Then N_𝒫(x) − cx ≠ O(x^{σ}) for every σ < (1−θ)/2.

In the variable u: σ_u := σ/(1−θ) < ½. The useful range is 1/3 < σ_u < ½, corresponding to (1−θ)/3 < σ < (1−θ)/2.
Write D(u) := ζ_𝒫((1−θ)u), D_tar(u) := ζ(u−a)F(u−a) and R := D/D_tar = G(u−a). In Re u > 1:

  log R(u) = Σ_{p,k,j} j^{−1}ε_{p,k}p^{−jku} = P(u) + L₂(u) + A(u),  P(u) := Σ_p ε_p p^{−u},

with L₂ the level-2 term and the j = 2 term of level 1, and A absolutely convergent in Re u > 1/3.

## B.2 What does hold (B1, PROVED)
(i) *Necessity (R184_001 Prop 2.2).* If N_𝒫 − cx = O(x^{(1−θ)σ₀}), then D(u) − c′/(u−1−a) is holomorphic in
Re u > σ₀ and |D(σ+it)| ≪_δ |t| for σ ≥ σ₀ + δ, |t| ≥ 1.

(ii) *One-sided bound without branches.* log|R| = log|D| − log|D_tar| is a single-valued function away from zeros and poles, and
log|R(σ+it)| ≤ log|t| + O(1) − log|ζ(σ−a+it)| − log|F|. F is a finite product bounded above and below on Re u ≥ 1/3.
The set {t ∈ [T,2T] : log|ζ(σ−a+it)| < −log²T} has measure o(T). This follows from the Titchmarsh 9.6 lemma
(log|ζ(w)| = Σ_{|γ−t|<1}log|w−ρ| + O(log T)), CITED. **log R need not be defined** for this step.

(iii) *The polynomial.* Let P_N(t) := Σ_{p≤N} ε_p p^{−σ−it}, with 1/3 < σ < ½, N = T/K, K large, and |ε_p| ≥ ¼ on a
positive proportion of each dyadic block (integrality + CITED-EQ). By Montgomery–Vaughan
(∫_T^{2T}|Σb_n n^{−it}|² = Σ|b_n|²(T + O(n))):
- ∫_T^{2T}|P_N|² ≍ T Σ_{p≤N}ε_p²p^{−2σ} ≍ T·N^{1−2σ}/log N =: T·V.
- P_N² is a polynomial of length N² with coefficients ≤ 2C²: ∫|P_N|⁴ ≪ (T + N²)(Σ_{p≤N}ε_p²p^{−2σ})² ≪ T²V².
  Since N² = T²/K² ≥ T, this is ≪ N²V² ≤ (TV)²: the fourth moment is ≪ (∫|P_N|²)²/T on average, which is what
  Paley–Zygmund needs (normalizing by measure T).
- ∫_T^{2T}Re P_N = O(Σ_p p^{−σ}/log p) = O(N^{1−σ}) = o(T√V).
- ∫Re(P_N²) = Re Σ_{p,q}ε_pε_q(pq)^{−σ}∫(pq)^{−it} = O(N^{2−2σ}) = O(TV/K), hence ∫(Re P_N)² = ½TV(1 + O(1/K)).
- Paley–Zygmund applied to (Re P_N)² and the near-exact symmetry of the mean give
  meas{t ∈ [T,2T] : Re P_N(t) ≥ c√V} ≫ T.

Up to this point the target is correct.

## B.3 The step that fails (B2, B3, B4)
To conclude, one would need (iv): log|R(σ+it)| = Re P_N(t) + o(√V) for almost every t. For σ < ½ this is **not a
consequence** of anything above. The series Σ ε_p p^{−u} diverges in general, and the logarithm of the continuation need
not resemble its partial sums.

**Proposition B.3 (counterexample to the route in the relaxed class, PROVED).** Let χ be a real non-principal character mod q.
Define ε_{p,1} = χ(p) and ε_{p,2} = 1 if χ(p) = −1, and 0 otherwise (and ε = 0 for p | q and at levels
k ≥ 3). Then:
(a) R(u) = L(u, χ) exactly, because (1 − p^{−u})(1 − p^{−2u})^{−1} = (1 + p^{−u})^{−1}. The multiplicities
    b = c + ε ≥ 0 are **real**, not integer. One has |ε| ≤ 1 and |ε_{p,1}| = 1 ≥ ‖p^a‖ for p ∤ q.
(b) D = ζ(u−a)F(u−a)L(u,χ) is meromorphic on ℂ with a single pole at u = 1+a and polynomial growth in each vertical
    strip. Hence log|R(σ+it)| = log|L(σ+it,χ)| ≤ ((1−σ)/2 + ε)log|t| + O(1) (convexity, 0 < σ < ½).
    By contrast, by B.2(iii), Re P_N ≥ cT^{(1−2σ)/2}/√log T on a set of measure ≫ T. **Step (iv) is false.**
(c) The error is small. We have γ = f * (χ(m)m^{−a}), so Σ_{m≤X}γ_m m^a = O(1) and x·Σ_{m>X}γ_m/m = O(X^ε).
    For T(X) = Σ_{m≤X}(f̃*χ)(m)m^{−a}Φ(X/m) (it suffices to treat f̃ = δ₁) we split into dyadic blocks M:
    - M ≥ M₀: χ has bounded partial sums and p ↦ Φ(X/·) has variation ≪ X/M + 1 on [M, 2M] (R184_010 §2).
      Abel summation gives ≪ qM^{−a}(X/M + 1).
    - X^{1/3} ≤ M ≤ M₀: we use Φ = −ψ + r, Vaaler and the second-derivative van der Corput estimate on each class mod q
      (f(ℓ) = X/(qℓ + r_0), f″ ≍ hX/M³). This gives Σ_{m∼M}χ(m)ψ(X/m) ≪_q X^{1/3} + M^{3/2}X^{−1/2}, and the part r
      contributes ≪ M^{2−a}/X.
    - M < X^{1/3}: the trivial bound gives ≪ X^{(1−a)/3}.
    With M₀ = X^{3/5}: T(X) ≪ X^{(1−a)/3} + X^{(2−3a)/5}log X. In the variable x:

      N_𝒫(x) − cx ≪ x^{max((1+θ)/3, 2/5)+ε},

    and this is < x^{(1−θ)/2} ⟺ θ < 1/5. (Conjecturally, of Gauss-circle type: x^{(1+θ)/4+ε} for every
    θ < 1/3, the same exponent as the linear Theorem D; ARGUED.)

**Corollary B.3′ (PROVED).** Any argument that uses only "|ε_{p,k}| ≤ C and |ε_{p,1}| ≥ ‖p^a‖" (or ≥ ¼ on a positive
proportion) cannot prove L\*\_comp, not even for θ < 1/5. A proof of L\*\_comp **must** use the congruence
ε_{p,1} ≡ −p^a (mod 1), i.e. that b_{p,1} be an integer. Moreover (b) shows that the one-sided bound of the route gives no
contradiction for L-functions. The probabilistic part of O184.093a (moments, Paley–Zygmund) is correct, but it
governs the **polynomial**, not the continuation.

*Mechanism.* In the example, D has ≍ T log T extra zeros on Re u = ½ (those of L(u,χ)). Those zeros lie to the right
of σ, and Selberg's formula for log R picks up terms y^{β−σ} from each one. These terms cancel Re P_N.

## B.4 The exact obstruction: the divisor of R (B5)
**(ZF_R; σ₁).** R = D/D_tar extends holomorphically and zero-free to Re u > σ₁. Equivalently: in that region the zeros
of ζ_𝒫 are exactly those of ζ_target, with multiplicity, and ζ_𝒫 has no poles.

> **Theorem B.4 (CONDITIONAL on (ZF_R)).** Let θ < 1/3, 𝒫 ∈ 𝒦_θ(C), and suppose (ZF_R; σ₁) with σ₁ < ½. Then
> N_𝒫(x) − cx ≠ O(x^{(1−θ)σ₀}) for every σ₀ < ½. That is, the exponent is ≥ (1−θ)/2.

*Proof.* Suppose the contrary and fix σ′ ∈ (max(σ₀, σ₁), ½) and δ > 0 with σ′ − 2δ > max(σ₀, σ₁).
1. By (ZF_R) there exists 𝓛 := log R, holomorphic in Re u > σ₁, agreeing with the Dirichlet series Σℓ(n)n^{−u} in
   Re u > 1. Its coefficients satisfy ℓ(p) = ε_p and |ℓ(n)| ≤ C′ at prime powers.
2. *Upper bound of Re 𝓛.* By B.2(i)–(ii), Re 𝓛 = log|D| − log|D_tar| ≤ 2log T + C log T log log T at every point
   of Re u ≥ σ′ − 2δ, |Im u − t| ≤ 3, t ∈ [T, 2T], at distance ≥ (log T)^{−2} from the zeros of ζ(u−a). This uses
   Titchmarsh 9.6: there are ≪ log T zeros in the window and each contributes log|w−ρ| ≥ −2 log log T.
3. *Borel–Carathéodory.* Take disks centered at u₀ = 2 + it, with radius r ∈ [2−σ′+δ, 2−σ′+2δ] chosen so that
   the circle avoids the (log T)^{−2}-neighborhoods of the ≪ log T zeros. The measure of bad radii is
   ≪ (log T)^{−1}, so a good r always exists. With |𝓛(u₀)| = O(1) and inner radius 2 − σ′ + δ/2 one obtains
   |𝓛(σ′ + it)| ≪_δ log T log log T, uniformly in t ∈ [T, 2T]. The same holds on Re u = σ′ − δ.
4. *Coefficient recovery.* Let N = T/(K log log T). Then
   A(t) := Σ_n ℓ(n)n^{−σ′−it}e^{−n/N} = (2πi)^{−1}∫_{(2)}𝓛(σ′+it+z)Γ(z)N^z dz. Shift to Re z = −δ (holomorphy
   by step 1, growth by step 3, decay of Γ) to obtain A(t) = 𝓛(σ′+it) + O(N^{−δ}log² T).
   Hence ∫_T^{2T}|A|² ≪ T log³ T.
5. *Montgomery–Vaughan.* With b_n = ℓ(n)n^{−σ′}e^{−n/N}: ∫_T^{2T}|A|² = Σ|b_n|²(T + O(n)). One has
   Σ_{n>N log log N} n|b_n|² ≪ N^{2−2σ′}(log N)^{−2}, and Σ_n n|b_n|² ≤ 2N log log N·Σ|b_n|² + (that). For K large,
   ∫|A|² ≥ (T/2)Σ|b_n|² ≥ (T/2)e^{−2}Σ_{p≤N, |ε_p|≥¼}p^{−2σ′}/16 ≫ T·N^{1−2σ′}/log N = T^{2−2σ′−o(1)}.
6. Since σ′ < ½, step 5 contradicts step 4. ∎

*Remarks.*
- Under (ZF_R) neither the fourth moment nor Paley–Zygmund is needed. The second moment of the continuation suffices.
- Example B.3 violates (ZF_R) (zeros of L(u,χ) at Re u = ½ > σ₁), so this is consistent.
- The dither of R184_010/013 satisfies (ZF_R) with σ₁ = ½ a.s. (R184_013 §2), but nothing is known for σ₁ < ½.
- A density version suffices: ≪ T^{1−η} zeros/poles of R in [σ₁, 1] × [T, 2T] allows redoing 2–5 in most
  windows, with fixed-radius disks. This is ARGUED, not written out.

**Conclusion:** L\*\_comp ⟸ (ZF_R) (or its density version) for some σ₁ < ½. The only missing piece is to **exclude
extra zeros of ζ_𝒫 in the strip (1−θ)/3 < Re s < 1 (zeros that are not target zeros), induced by the rounding**. The
example B.3 shows that, without integrality, such zeros exist and salvage the growth.

## B.5 Reformulation in terms of integrality (B6, ARGUED)
Two admissible roundings differ by a bounded **integer** sequence (m_{p,k}). Hence

  R = R₀·E,  R₀ := ∏_p(1 − p^{−u})^{−(⌊p^a⌉ − p^a)} (plus the level ≥ 2 Witt correction),
  E := ∏_{p,k}(1 − p^{−ku})^{−m_{p,k}},  m ∈ ℤ bounded.

The E's are bounded integer Euler products, e.g. L(u,χ)^{±1} and products of these (B.3(a)). We say R is
*tame at σ₁* if D_tar·R has polynomial growth and at most one pole in Re u > σ₁. Then:
- L\*\_comp ⟺ (with loss ε) for no bounded integer E is R₀E tame at any σ₁ < ½.
- All the arithmetic sits in R₀, the series of **forced** fractional parts:
  log R₀ ∋ −Σ_p({p^a} − ½)p^{−u} − ½ log ζ(u) + …
- The term −½ log ζ(u) forces E to contain ζ^{1/2}·(…). The half-integers ½ ± ½χ(p) give square roots of
  L-functions, with branch points at their zeros: a first hint, ARGUED, that integrality does obstruct.
- The part Σ_p e(hp^a)p^{−u} of ({p^a} − ½), via the explicit formula, involves the zeros of ζ with stationary-phase
  factors ≍ |t|^{(β−σ)/a}. Its continuation is neither "random" nor "L-function"-like. This is the real
  arithmetic question, and it is **OPEN**.

## B.6 Honest summary
- Erratum (Part A): PROVED. The exponent (1−θ)/2 and Theorem L do not change; the cited proofs are amended as in A.4.
- O184.093a: the probabilistic part is PROVED, but the identification log|R| ≈ polynomial is **false in general**.
  Relaxed counterexample B.3, with error < x^{(1−θ)/2} proved for θ < 1/5.
- L\*\_comp: CONDITIONAL on (ZF_R) (Theorem B.4, proof written modulo standard citations). Unconditionally: **OPEN**. The
  exact obstruction is that of the extra zeros of ζ_𝒫 in the strip created by the rounding, and excluding them requires using
  the integrality b_{p,1} ∈ ℤ.
- The discrete frontier at 1/3 for the lattice method is **not** declared sharp: it stands at Theorem L (PROVED) + L\*\_comp
  (OPEN).
- Row D: unchanged.

## For the audit
1. A.2, lower bound: check Lemma A.0 (Φ ≥ 0.17 on [1, 6/5]) and that Landau on (5X/6, X] gives the order
   (log log)^{k−1}/((k−1)! log X) for fixed k.
2. A.3, total: verify the orthogonality rule E[g(m)g(m′)] = 0 unless the non-common primes appear with
   exponent ≥ 2, and the count Σ_n n^{−2a}(X/n)^{1−2a} ≪ X^{1−2a}log X.
3. A.3, deterministic bias E T ≪ X^{1/2−a+ε}: is it a genuine secondary term of size x^{(1−θ)/2}/log x? Not
   needed, but worth recording.
4. A.4: confirm that the proof of Theorem L (R164_201 §3) does not use the erroneous sentence of §1. My reading is that it does not.
5. B.2(iii), fourth moment: check the MV inequality for P_N² with length N² = T²/K² > T. The factor
   (T + N²) ≍ N² is acceptable because it is compared with (T·V)²/T.
6. B.3(c), van der Corput: verify the balance M₀ = X^{3/5} and the range θ < 1/5. Also check that the term
   r of Φ for M ≥ M₀ stays within the variation ≪ X/M + 1.
7. B.4, step 3: Borel–Carathéodory needs sup Re 𝓛 on the circle. Check that the Titchmarsh 9.6 bound
   holds for ζ(w) with Re w = σ′ − a − 2δ ∈ (−1, 2), which lies in or to the left of ζ's critical strip (a < ½).
8. B.4, step 5: the lower bound uses CITED-EQ (‖p^a‖ ≥ ¼ on a positive proportion of each block). Without EQ,
   Σ_{p≤N}‖p^a‖²p^{−2σ′} ≫ N^{1−2σ′−o(1)} suffices, which is weaker and perhaps provable by Weyl/van der Corput over primes.
9. B.5: the claim "the half-integers force roots of L-functions" is heuristic. An E mixing infinitely many
   characters might avoid it.
