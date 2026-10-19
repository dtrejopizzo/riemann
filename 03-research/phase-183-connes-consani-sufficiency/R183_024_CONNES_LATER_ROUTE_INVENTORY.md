# R183.024 — Connes's "later" route: inventory, implicit mechanism, and the C_T conjecture

Phase 183 (Connes–Consani sufficiency). Neither RH nor the closure of
row D is claimed.

Inputs: R183_017, R183_018 (§0, §3, §5, §6), R183_019 (§5 and "Answer to
question 5"), R183_020, R162_2602 (Thm 4, Thm 6, Prop 8), R162_2702,
120-source-inventory-of-the-connes-consani-moscovici §5. Normalization: that of R183_015/018. The
logarithmic coordinate t is used, with h ∈ C_c^∞(I_T), I_T=(−T,T), φ=ĥ
and c_h(x)=∫h(t)\overline{h(t−x)}dt. The form is

    E_S(h) = (1/2π)∫ m|φ|² − Σ_{p∈S} 2log p Σ_{k≥1} p^{−k/2} Re c_h(k log p),

with m = h_+ = 2θ' and S ⊇ {∞} ∪ {p < e^{2T}}.

---

## 0. Verdict

* **Inventory (§1).** No local source, including the 2022–2026 works of
  Connes, Consani, and Moscovici, explicitly proves or conjectures a Weil
  positivity inequality for supports beyond (2^{−1/2}, 2^{1/2}) via the
  Sonin/prolate route (CITED, negative search). What is actually in the
  source:
  (i) the semilocal Sonin space S_λ(X_S) and its Hilbertian stability
  θ_S: S_λ(R) ≅ S_λ(X_S) (CCM 2310.18423, Thm 4.6);
  (ii) the declared strategy: compare the trace of the semilocal prolate
  operator with Weil's functional (CCM, Intro p. 2–3);
  (iii) the UV prolate spectrum (CM 2022), whose counting law matches
  that of the zeros, and whose negative eigenfunctions lie in Sonin.
* **Implicit mechanism (§2).** The candidate positive part is the
  **semilocal Sonin trace** Son_S(h) := Tr(ϑ(g) Π_S ϑ(g)*), where Π_S is
  the projection onto S_1(X_S). A **model lemma** is proved (PROVED in
  the half-line model, to first order): passing from Son_∞ to Son_S
  produces exactly the prime term −2 log p · p^{−1/2} Re c_h(log p). The
  factor log p comes out as the length of the boundary layer left by
  translation by log p. The extension to all k uses Widom's formula
  (CONDITIONAL, sketched). Consequently the family of bump pairs from
  NO-GO R183_018 Thm 5.1 **is absorbed**: on that family the remainder is
  O(Nw)‖x‖² (§2.4).
* **Conjecture C_T (§2.5)**, with all its objects defined. It consists of
  an identity part, I_S (zero-free), and an inertia part, N_T: the
  remainder has at most one negative direction, aligned with ℓ(h)=∫h.
* **Classification (§3): (b), strictly stronger than D in each window.**
  Within C_T there is a sublemma of type (c), the identity I_S: it is
  zero-free, proved from source data, and blind to deletion. The inertia
  N_T carries all the arithmetic content. There is also a new **Szegő
  falsifier** (§3.4, CONDITIONAL): if the semilocal remainder's symbol is
  negative on a set of positive measure, n₋ grows linearly in T and C_T
  is false for large T, even under RH. CC's archimedean data
  (λ_max(K_I)≈1.0516>1) point in that direction.
* **First lemma (§4).** L1 (semilocal Widom identity) and, in parallel,
  L2 (sign of the remainder's symbol). L2 decides viability before more
  work is invested in the route.

---

## 1. Inventory of sources (CITED)

### 1.1 CCM, *Zeta zeros and prolate wave operators — semilocal adelic operators*, arXiv:2310.18423v2 (= Ann. Funct. Anal. 2024; the "final-2024" PDF has the same content)

| Place | Statement | Type |
|---|---|---|
| Intro (2), p. 3 | W_λ = −S² + 2πλ²(4N+1) − ¼ (formal), with S the scaling generator and N the grading of orthogonal polynomials of the cyclic pair (S, e^{−πx²}) | formal definition; domain not treated |
| Intro, p. 2–3 | "the operator theoretic aspect of the present paper provides a more precise strategy for addressing the semilocal Weil positivity by comparing the trace functional associated to the operator — which is automatically positive for a selfadjoint operator — with the Weil functional. The conditioning … will be implemented automatically by the orthogonality of the positive and the negative part of the spectrum of the semilocal prolate operator, whose negative eigenspace was identified in [12] to the Sonin space." | **declared strategy, not a theorem** |
| Thm 1 = Prop 4.1, 4.2 (eq. 44–48) | η_S(f) = class of 1_{R_S}⊗f; F_μ w_S η_S(f)(s) = ∏_{p∈S∖∞} L_p(½−is) · F_μ w_∞ f(s); η_S(P_λ) ⊂ P_λ^S, F_S η_S = η_S F; V_S = M_S U_S gives the canonical form of the cyclic pair (S, ξ_S) with measure dm_S = |∏_{v∈S} L_v(½−is)|² ds | PROVED in source |
| Thm 4.1 | semilocal Hermite operator N_S (grading); the semilocal S is Jacobi-type | PROVED; Jacobi coefficients "deferred" |
| Def 4.5, Prop 4.6 (57) | S_λ(X_S,α) = {f ∈ L²(X_S)^{K_S} : f = 0 and F_S f = 0 for \|x\|<λ}; θ_S(f) = σ_S⊗f, F_μ w_S θ_S(f)(s) = F_μ w_∞ f(s) · ∏_p (1−p^{−½−is}); in log-time w_S θ_S f(λ) = g(λ) − p^{−1/2} g(λ/p) | PROVED |
| Prop 4.7 (iii) | ⟨θ_S f \| η_S g⟩ = ⟨f\|g⟩, so η_S = (θ_S^*)^{−1} | PROVED |
| **Thm 4.6 (= Thm 2)** | θ_S: S_λ(R,e_∞) → S_λ(X_S,α) is a **Hilbertian isomorphism** (bounded with bounded inverse, **not isometric**) | PROVED |
| §4.8, Prop 4.8 | S_λ(X_S) ≅ B_λ (de Branges space as a set, via (60)); with the L²(ds/\|E_S\|²) norm it is a de Branges space B_λ^S; "the choice of S plays a key role in fixing the inner product" | PROVED |
| §3.6, Prop 3.6 | F_μ(E(ψ_ℓ^±)) = R_ℓ^±·Ξ; the spectrum of multiplication by s on H_{≤1}/closure is the set of critical zeros | PROVED (spectral, no positivity) |
| §5, Thm 5.2 | metaplectic: the discrepancy coefficients d_n vanish exactly for (S, ξ_∞); second semilocal candidate "in a forthcoming paper" | PROVED / program |

**What is NOT in 2310.18423** (full-text search): (a) no rigorously
defined self-adjoint semilocal prolate operator, because the Jacobi
coefficients for general S are deferred (p. 5); (b) no trace formula for
the semilocal Sonin projection; (c) no Weil positivity statement for
\|S\| ≥ 2 nor for supports larger than log 2; (d) no statement about the
negative index. The relation "negative spectrum of W ↔ Sonin" is taken
from [12] = CM 2022 and only holds in the archimedean case, modulo a
finite-dimensional discrepancy (p. 5, l. 229–232).

### 1.2 Connes–Moscovici, *The UV prolate spectrum matches the zeros of zeta*, PNAS 119 (2022)

* Thm 1.6: W_sa (the unique self-adjoint extension of W_min on S(R)) is
  self-adjoint, commutes with F_{e_R}, and has discrete spectrum
  unbounded in both directions. The negative eigenvalues are simple.
  PROVED.
* Cor 2.2: eigenfunctions of negative eigenvalue belong to the Sonin
  space. Sonin's orthogonal is positive except possibly for a finite
  number of exceptions. PROVED.
* Thm 5.1 (λ=√2): the counting function of the isospectral 2D Dirac
  operator 2D̸ satisfies N(E) ≈ (E/2π)log(E/2π) − E/2π + O(log E), the
  Riemann–von Mangoldt law. PROVED (semiclassical). The fine match with
  the zeros is **only numerical**.
* It contains no Weil positivity statement. It only says that compressing
  the scale to Sonin is the root of archimedean positivity [CC 2020] on
  [2^{−1/2}, 2^{1/2}].

### 1.3 CC 2020 (2006.13771), reference (already audited in R183_018 §1)

Tr(ϑ(f)S) = W_∞(f) + ∫f(ρ^{−1})ε(ρ)d*ρ for every f (Thm 4.7, (83)), with
ε from (84). The single-negative-direction bound is obtained on
\|I\| ≤ log 2 (Prop 5.5, Thm 6.11). CITED.

### 1.4 CCM, *Zeta spectral triples*, arXiv:2511.22755 (local: papers-ref-phase-60/…/arXiv-2511.22755v1.tex)

* Thm 1.1 (via 120-inventario §5.3): D_log^{(λ,N)} is self-adjoint and
  det_reg = −iλ^{−iz} ξ̂(z), with ξ̂ entire with real zeros. PROVED in the
  source.
* §"The missing steps" (l. 1385–1405): missing are (1) that QW_λ's
  minimal eigenvalue be simple with an even eigenvector, and (2) that
  k_λ (deformed prolate) approximate ξ_λ. Both are OPEN for them. QW_λ's
  positivity is **not** the goal: they work with QW_λ − ε_λ, "lower
  bounded", aiming at the convergence of zeros. **No positivity claim for
  λ > √2.**
* One piece of interest here: the declared "cornerstone" is [Co-zeta]'s
  trace formula, relating P_λ, P̂_λ, and the map E to QW_λ (l. 1406).

### 1.5 Connes–Consani, *Hochschild homology, trace map and ζ-cycles* (2207.10419) and *Knots, primes and the adele class space* (2401.08401)

* 2207.10419, l. 197–201: semilocal trace formula (Connes 1999, Thm 4):
  Tr(R_Λ U(h)) = h(1)∫_{|λ|∈[Λ^{−1},Λ]}d*λ + Σ_{v∈S}∫'_{Q_v^*} h(u^{−1})/\|1−u\| d*u + o(1).
  Accompanied by the "poles − Σ_ρ = Σ_v ∫'" form. CITED. The work gives a
  spectral realization (Thm spectralreal1intro), not positivity.
* 2401.08401: knot/prime geometry. Negative search for "positiv/Sonin/prolate".

### 1.6 Connes–Consani, *metaphysics of F_1* (2307.06748)

Contains only the positivity of the distribution N(u) on (1,∞)
(l. 203–250). Not Weil positivity. **Not relevant.**

### 1.7 Suzuki, 2301.00421v3

* Thm 1.1 (under RH): the completion H_W of C_c^∞ with ⟨·,·⟩_W is
  isomorphic to the de Branges space H(E_ξ), with
  E_ξ(z) = ξ(½−iz) + ξ'(½−iz). CONDITIONAL on RH in the source.
* Thm 1.4 / Cor 1.5: RH ⟺ ‖P̂Dψ‖² = π⟨ψ,ψ⟩_W ∀ψ ⟺ 2‖ψ‖² = ⟨ψ,ψ⟩_W on
  V°(0). It is a reformulation as equalities, of type (a). CITED.
* Relevance: Weil's form **is** (under RH) the norm of a de Branges
  space whose phase counts zeros. §2's candidate object is the **source**
  counterpart of that structure: the semilocal Sonin de Branges space B_1^S.

### 1.8 Local arXiv 2026 review (grep connes/prolate/sonin/weil positivity)

* Zhu 2608.24827v2: Q ≥ 8.9·10^{−18}‖f‖² for support in [−0.8, 0.8], i.e.
  T = 0.8 (computational certificate). It also certifies "simple and even
  ground state" at λ = e^{0.8} (CCM's missing step (1)). CITED. **Does
  not use Sonin.** Reminder (program memory): do not claim "first beyond
  log 2".
* Suzuki 2606.09096v3: "screw function" framework. Cites [CCM 2025+,
  Thm 3.6, Cor 3.7, Thm 5.10]: A_a self-adjoint with discrete spectrum
  bounded below. Formulates a limit a→∞ conjecture (zeros as spectrum).
  No positivity. CITED.
* Groskin 2607.02828v3: exact Galerkin ↔ sum-over-zeros dictionary and a
  totally positive archimedean tail. Certification tool. CITED.
* Desogus 2609.20367: "three gates" argument in the odd channel. Not
  audited here. Outside the scope of Sonin.

### 1.9 Corpus

* R162_2602 Thm 4 (PROVED): **Connes's semilocal trace carrier** (R_Λ)
  is blind to deletion and gives no lower bound. **Caution:** that
  theorem deals with the **cutoff** carrier R_Λ, not the **semilocal
  Sonin** projection Π_S, which was not available there. The present
  file deals with Π_S. The deletion warning is inherited: see §3.3.
* R162_2702: boundary triples for W_λ, classification, and Weyl
  function (PROVED). No extension invariant touches the contact (NO-GO).
  Consistent with what follows: the **archimedean** prolate does not know
  the primes.
* 120-inventario §5: semilocal positivity is "a declared strategy, not a
  theorem." Confirmed.

**Answer to task 1.** The only post-2020 material discussing extending
positivity is CCM's strategy phrase, p. 2–3, plus the proved structure of
semilocal Sonin: Thm 4.6, Prop 4.6–4.8. There is no theorem nor
conjecture stated about the negative spectrum of a semilocal prolate
related to Weil positivity. What follows is reconstruction.

---

## 2. The implicit mechanism, in R183_015/018's normalization

### 2.1 Mellin image (PROVED from CITED)

U_S := F_μ w_S: L²(X_S)^{K_S} → L²(R, ds) is unitary (CCM Prop 4.2). There
the scaling action ϑ(g) is multiplication by φ(s) (the same character
u^{−is} for every S). Let K := U_∞(S_1(R)) ⊂ L²(R,ds). By (57)–(58) and
Thm 4.6,

    K_S := U_S(S_1(X_S)) = m_S · K,   m_S(s) := ∏_{p∈S∖∞} (1 − p^{−1/2−is}),

where m_S is a bounded multiplication with bounded inverse. Its
complement is K_S^⊥ = (m_S^*)^{−1} K^⊥ = η_S(K^⊥), by Prop 4.7(iii). **The
semilocal Sonin complement is the image under the map E_S (eq. 46) of the
archimedean complement.** It is the same map E that, in [CC, CCM §3.6],
generates the approximate radical of Weil's form. This is the precise
form of CCM's statement that "the conditioning by the radical … will be
implemented automatically by the orthogonality."

In log-time, multiplication by p^{−is} is translation τ_{log p}. Thus
m_S = ∏(1 − p^{−1/2}τ_{log p}) is a causal operator: it preserves support
on u ≥ 1. By contrast, S_1(X_S)'s Fourier condition is, in Mellin, a
reflection s ↦ −s twisted by χ_S = χ_∞ ∏_p L_p(½−is)/L_p(½+is). That
twist contains the **anticausal** factor m_S^#(s) = ∏(1 − p^{−1/2+is}).

### 2.2 Candidate positive part

**Definition 2.1.** For h ∈ C_c^∞(I_T) and g(e^t) = h(t),

    Son_S(h) := Tr(ϑ(g) Π_S ϑ(g)^*) = Tr(M_φ Π_{K_S} M_φ^*) ≥ 0.

It is automatically positive, which is the point of CCM's strategy. For
S={∞} it coincides with R183_018's Son.

**Proposition 2.2 (phase reading; PROVED modulo standard de Branges
theory).** Let E^{(S)} be a de Branges structure function of the space
B_1^S (which exists by CCM §4.8.3 and de Branges's theorem), and let φ_S
be its continuous phase, so that
E^{(S)}(s) = \|E^{(S)}(s)\| e^{−iφ_S(s)} on R. Then

    Son_S(h) = (1/π) ∫ |φ(s)|² φ_S'(s) ds,     φ_S' > 0.

*Proof.* Π_{K_S} is unitarily equivalent to the inclusion of B_1^S in
L²(ds/\|L_S(½+is)\|²) (CCM (59), Prop 4.8). Its diagonal kernel in
L²(ds) is K^{(S)}(s,s)/\|E^{(S)}(s)\|² = φ_S'(s)/π (de Branges identity
for the reproducing kernel on the real diagonal). Since M_φ is a
multiplication, the trace is the integral of \|φ\|² against that
diagonal. The trace is finite because φ is Schwartz and φ_S' grows like
log, as does θ'. ∎

Hence **Son_S is a convolution form in the window with positive symbol**
2φ_S'(s), restricted by the support to the difference window (−2T, 2T).
E_S has symbol m(s) − Σ_p σ_p(s log p), which is indefinite. On all
h ∈ C_c^∞(I_T),

    E_S − Son_S = convolution form with kernel
                  F^{−1}[m − 2φ_S' − Σ_p σ_p]  restricted to (−2T,2T).

For S={∞}, CC (83) says precisely that F^{−1}[m − 2φ_∞'] = −ε(e^{\|x\|})
is **continuous** on the window (CITED; for the normalization constant
2π, see review point 1).

### 2.3 Model lemma: log p is a boundary layer

**Model.** K is replaced by H₋ := the image of L²(−∞,0) under the
reflection-twist. Only the anticausal condition is kept, the one the
twist m_S^# alters, and prolate nonlocality is discarded. Let P be the
projection onto H₋ (in log-time, multiplication by 1_{(−∞,0)} after
unitary conjugation), Q = 1−P, a = log p, V := τ_{−a}, ε := p^{−1/2}. P
is compared with the projection P' onto (1 − εV)H₋. Let C be convolution
by h, so that C^*C has kernel c_h(x−y).

**Lemma 2.3 (PROVED in the model, first order).**

    Tr(C(P'−P)C^*) = −2 ε a Re c_h(a) + O(ε²)
                   = −2 log p · p^{−1/2} Re c_h(log p) + O(p^{−1}).

*Proof.* For a projection P and bounded A, the projection onto
(1+εA)·Ran P is P + ε(QAP + PA^*Q) + O(ε²) (expansion of
P_{gK} = gP(Pg^*gP)^{−1}Pg^*). With A = −V,

    Tr(C QVP C^*) = Tr(QVP · C^*C) = ∫∫ (QVP)(x,y) c_h(y−x) dy dx.

With P = 1_{(−∞,0)}, Q = 1_{(0,∞)} and (Vf)(x) = f(x+a), QVP's kernel is
1_{x>0}·δ(y−x−a)·1_{y<0}, requiring x>0 and x+a<0: empty. With the
opposite direction (Vf)(x) = f(x−a), the one that breaks H₋, the kernel
lives on x ∈ (0,a), y = x−a. The trace equals ∫_0^a c_h(x−(x−a))dx =
a·c_h(a). The adjoint term gives a·\overline{c_h(a)}. Summing with
A = −V gives −2a Re c_h(a)·ε. ∎

The causal case serves as a control. If the shift preserves the
half-line (QVP = 0), the correction is zero. That is the case of the
support condition, which θ_S preserves (Prop 4.6(i)). **All of the prime
contribution comes from the Fourier condition** (from the m_S^# twist).
This fits the source: the support condition is S-invariant and the
Fourier one is not (Prop 4.7(i) versus (57)).

**Proposition 2.4 (all k; CONDITIONAL, sketch).** In the model, for
g = 1 − εV invertible and anticausal Wiener, Widom's trace formula for
Wiener–Hopf operators (Tr(W(a)W(b) − W(ab)) = Σ_n n a_n b_{−n}, continuous
version ∫ x·\hat{u}(x)…) applied to log g = −Σ_k ε^k V^k/k gives

    Tr(C(P_{gH₋} − P_{H₋})C^*) = −Σ_k 2(k a)(ε^k/k) Re c_h(ka)
                                = −2 log p Σ_k p^{−k/2} Re c_h(k log p).

This is **exactly E_S's p-term**, with all k. The weight k·a (layer
length) cancels the logarithm's 1/k, producing Λ(p^k) = log p. For
several primes, log m_S^# = Σ_p log(1 − p^{−1/2}τ_{−log p}) is additive
and the cross terms are of higher order in Widom's formula; they vanish
in the model because all shifts go in the same direction. This remains
CONDITIONAL: the verification of trace class and of the global sign in
the continuous model is missing.

### 2.4 Check against R183_018 Thm 5.1's NO-GO (PROVED, given I_S)

Assume identity I_S of §2.5: E_S = Son_S − ∫c_h ε_S with
ε_S ∈ L^∞(−2T,2T). Take Thm 5.1's family, x = Σ_j c_j h_j with
h_j = β(·−t_j) + β(·−t_j−log 2), β = c_w'' − c_w/4, of support width 2w.

1. In the family, c_x(k log q) = 0 for every (q,k) ≠ (2,1), and
   c_x(log 2) = Σ_j \|c_j\|²‖β‖₂². This is step 1 of R183_020.
2. By I_S, the prime part of E_S on the family,
   −2 log 2 · 2^{−1/2}Σ\|c_j\|²‖β‖₂², **lies inside Son_S**:
   Son_S(x) = Son_∞(x) − 2log2·2^{−1/2}Σ\|c_j\|²‖β‖² + O(‖x‖₁²).
   This is compatible with Son_S ≥ 0, because
   Son_∞(x) ≍ w^{−3}log(1/w)Σ\|c_j\|² dominates the prime term, which is
   ≍ w^{−3} (R183_020).
3. The remainder is R'_S(x) := E_S(x) − Son_S(x) = −∫c_x ε_S. With
   \|ε_S\| ≤ M_S and ‖x‖₁² ≤ 4N‖β‖₁²Σ\|c_j\|²,

       |R'_S(x)| ≤ 4 M_S N ‖β‖₁² Σ|c_j|² = O(N w) · ‖x‖₂²,

   because ‖β‖₁²/‖β‖₂² = O(w) (step 3 of R183_020). As w → 0 the ratio
   R'_S/‖x‖² tends to 0: **the pair family stops producing uniform
   negative directions**. In general, if ε_S is continuous, R'_S is a
   compact Hilbert–Schmidt integral operator on L²(I_T). Its negative
   spectrum only accumulates at 0, so n₋ below any −δ is finite. Thm
   5.1's mechanism (non-compact B_p, with eigenvalues ± of infinite
   multiplicity) **disappears**, because B_p has been absorbed into Son_S.

Conclusion of §2.4: the partition Son_S + R'_S avoids the NO-GO **if and
only if** Son_S reproduces E_S's prime atoms in the window. This is
necessary because if Son_S − Son_∞ lacks the atom at log p, R'_S contains
B_p and R183_018's Prop 4.1(iii) applies. Lemma 2.3 and Prop 2.4 say
that, in the model, they reproduce it exactly.

### 2.5 Conjecture C_T

Objects:
* T > 0; S = S(T) := {∞} ∪ {p < e^{2T}}.
* Son_S from Def 2.1 (Π_S the projection onto S_1(X_S), CCM Def 4.5).
* ℓ(h) := ∫h = ĥ(0), whose Riesz representative in the ξ metric is e_T
  (R183_019 §2: ‖ℓ‖² = T/2).
* X: the norm of the closed form Son_S + ‖·‖²_{L²(I_T)} on the
  primitive tests (∫h e^{±t/2} = 0), or, equivalently for the index, CC's
  ξ metric.

**Conjecture I_S (semilocal identity; OPEN, type (c)).** There exists
ε_S ∈ C([−2T,2T]), real and even, such that for every h ∈ C_c^∞(I_T)

    Son_S(h) = (1/2π)∫ m|φ|² − Σ_{p∈S} 2log p Σ_k p^{−k/2} Re c_h(k log p) + ∫ c_h(x) ε_S(x) dx,

i.e., **E_S(h) = Son_S(h) − ∫c_h ε_S**. For S={∞} this is CC (83) with
ε_{∞}(x) = ε(e^{\|x\|}) (CITED).

**Conjecture N_T (inertia; OPEN).** The remainder
R'_{S,T}(h) := −∫c_h ε_S satisfies, on primitives,

    R'_{S,T} ≥ −b|v⟩⟨v| + c(I − |v⟩⟨v|) in X,  with c > 0,  b ≥ 0,
    and δ_T := (b+c)|⟨v,e_T⟩|² − b > 0.

Equivalently (R183_019 Cor 3.2): λ₂(K_{S,T}) < 1 and the alignment
condition α_T² > (λ₁−1)/(λ₁−λ₂), where K_{S,T} is the compact integral
operator coming from ε_S after CC's (103) integration by parts.

**C_T := I_S ∧ N_T.**

**Proposition 2.5 (PROVED, given C_T).** C_T ⟹ E_S(h) ≥ δ_T·(…)‖h‖²_X > 0
for every nonzero primitive h in ker ℓ. That is, Weil positivity in
window T on the codimension-3 ideal (restricted D_T). *Proof:* Son_S ≥ 0,
and R183_019 Thm 3.1/Cor 3.2 applied to R'. ∎

---

## 3. Spectral reading and classification

### 3.1 Spectral side

On primitive tests, by the explicit formula (R183_015),
E_S(h) = Σ_ρ ĥ(γ_ρ)\overline{ĥ(\bar γ_ρ)} (zero side; the poles vanish on
primitives). By Prop 2.2, Son_S(h) = (1/π)∫\|ĥ\|²φ_S'. Hence, on the
window,

    R'_{S,T}(h) = Σ_ρ ĥ(γ_ρ)\overline{ĥ(\bar γ_ρ)} − (1/π)∫ |ĥ(s)|² φ_S'(s) ds.

The two measures have the **same mean density**: φ_S' ≈ θ' ≈ ½log(s/2π),
the zero density. This is the trace-formula version of CM 2022's UV
coincidence. If I_S holds, φ_S''s oscillating part also contains
−Σ_{p∈S} Σ_k log p · p^{−k/2} cos(ks log p), the Riemann–von Mangoldt
oscillation of S'(t) truncated to S. Thus (1/π)φ_S' is the **source
predictor** of the zero density at resolution 1/(2T), and R'_{S,T}
measures the discrepancy between the zeros and their predictor, tested
against \|ĥ\|² with ĥ of exponential type T.

For window tests, the explicit formula makes that discrepancy
**identically** equal to −∫c_hε_S. There is no zero information beyond
what is already on the source side. The spectral reading is a
dictionary, not a route.

### 3.2 Classification — **(b), strictly stronger than D (window by window); with a sublemma (c)**

1. **Not (a).** C_T is not equivalent to D_T. N_T requires
   E_S ≥ Son_S − (rank one), i.e. that the zero measure dominate the
   phase measure φ_S'ds/π on exponential type T, modulo one direction.
   Under RH only E_S ≥ 0 is known. Whether RH ⟹ N_T is unknown and not
   expected (see 3.4). It is the semilocal version of R183_019 §5's
   verdict: "W ≥ Tr(ϑSϑ^*) on ker ℓ is stronger than W ≥ 0." PROVED as
   implication C_T ⟹ D_T|ker ℓ (Prop 2.5). The non-implication
   RH ⟹ C_T remains OPEN, with evidence against in §3.4.
2. **∀T: C_T ⟹ RH.** By Prop 2.5 and CC's observation (comment after
   (4), l. 112–114; R183_019 §5): positivity on ker ℓ ∀T ⟺ RH, because
   ζ(½) ≠ 0. PROVED (from CITED).
3. **Sublemma (c): I_S.** It is a statement about the trace of the
   semilocal Sonin projection, built from purely source data: θ_S, the
   local factors, the archimedean prolates, and Widom's formula. It
   involves no zeros and is not equivalent to any form of RH. It is an
   **exact** analogue of CC (83) in the semilocal case. Proving it would
   be a new and independent result, and **is the only piece of the whole
   route that can be proved without touching the wall**.
4. **The arithmetic content is in N_T**, and cannot come from I_S (3.3).

### 3.3 Deletion (PROVED)

The construction Π_S and identity I_S make sense for **any** finite S
with ∞ ∈ S (CCM Thm 4.6 is uniform in S), in particular for
S' = S∖{p} with p < e^{2T}. If I_{S'} holds, then
E_{S'} = Son_{S'} − ∫c_hε_{S'}, and E_{S'} is the deletion form
ζ(s)(1−p^{−s}), with λ_A < 0 for large T (R162_2602 Prop 8(a)). Hence
**N_T must fail for S' at large T**, and any proof of N_T must use that S
contains every p < e^{2T}, through ε_S. I_S, by local multiplicative
construction (m_S = ∏_p), is blind to deletion. This is R183_018 §6's
warning (ii), now located: **the route reduces D_T to a spectral property
of a single compact operator K_{S(T),T}, built with no zeros, whose
verification ∀T is equivalent in strength to RH or stronger**.

### 3.4 Szegő falsifier (CONDITIONAL; new)

n₋ does not depend on the metric. Hence N_T requires
n₋(R'_{S,T}) ≤ 1 in the window. R'_{S,T} is the truncation to I_T of a
convolution with symbol r_S(τ) := −ε̂_S(τ) (in the ξ metric:
2ε_S'(1^+) − \widehat{Qε_S}(τ), cf. CC (103)). If ε_S ∈ L¹(R) and
r_S < 0 on a set of positive measure, the eigenvalue-distribution theorem
for Wiener–Hopf truncations (Landau–Widom/Szegő, as in R162_2602
Prop 8(b)) gives

    n₋(R'_{S,T}) ~ (T/π)·|{τ : r_S(τ) < 0}|  →  ∞,

and N_T is **false for large T** with fixed S, **even if RH holds**.

Archimedean datum (CITED, CC §6): λ_max(K_{I}) ≈ 1.05158 > 1 already at
\|I\| = log 2. By Cauchy monotonicity (R183_018 §5.1), sup_τ of K's
symbol is ≥ 1.0516, so r_∞ < 0 on a set of positive measure. This is
CONDITIONAL on ε ∈ L¹(R), and is R183_019's Prop 3.4 viewed as a symbol.
For the semilocal case, ε_S = ε + δε_S, where δε_S is the correction from
prolate nonlocality to the boundary layer of §2.3. **For N_T to survive,
δε_S must lower the symbol by at least ≈5% of 2ε'(1^+) throughout the
band where r_∞ < 0, and moreover S = S(T) grows with T.** There is no
known structural reason for this. It is the first question to answer (L2).

Reading: CCM's mechanism fixes the **infinite-dimensional, fixed-window**
NO-GO (§2.4), but in the regime T → ∞ it will likely run into the
Landau–Widom growth of the archimedean remainder. If so, the surviving
version would be "n₋(R'_{S,T}) = O(T)", which gives nothing:
n₋(E_S) < ∞ per window is already known (R162_2602 Cor 7(iii)).

---

## 4. First lemma to prove

**L1 (semilocal Widom identity = I_S, first order in one prime).** Let
S = {∞, p} and h ∈ C_c^∞(I_T). It must be proved that

    Son_S(h) − Son_∞(h) = −2 log p Σ_k p^{−k/2} Re c_h(k log p) + ∫ c_h δε_p,

with δε_p continuous and bounded on [−2T, 2T] and an explicit bound in
terms of CC's prolate data {λ(n), ξ_n, ζ_n} (84).

Why it is likely provable from source data:
* Π_S = 1 − Π_{η_S(K^⊥)} (Prop 4.7(iii), Thm 4.6) and
  η_S = Σ_{n S-smooth} n^{−1/2}τ_{log n} (eq. 46): everything is explicit
  and there are no zeros.
* The atom term is given by Lemma 2.3 / Prop 2.4 (boundary layer; Widom
  formula), a classical theorem about Wiener–Hopf operators.
* The difference between the true Sonin projection and the half-line
  model is controlled by the prolate decomposition of P P̂ P (CC (81),
  (84)). The eigenvalues λ(n) decay superexponentially (CC (100),
  Slepian), so the correction is a smooth kernel. It is the same
  argument giving ε's continuity in CC (84) and in R183_020's Lemma ε-L∞.
* Internal falsifier: with k = 1 and in the model, L1 reduces to Lemma
  2.3, already PROVED. A global sign error would be detected there.

**L2 (in parallel, decides viability).** The sign of the symbol r_S must
be computed in the archimedean case, deciding whether
sup_τ \widehat{Qε}(τ)/(2ε'(1^+)) > 1 over the whole real line. It is a
question about the transform of a function given by (84). It must also
be decided whether δε_p can compensate it. If r_∞ < 0 on a set of
positive measure and \|δε_S\| is small (O(Σ_p p^{−1}) by Prop 2.4 at
second order), C_T is refuted for large T. **Conditional NO-GO** of the
CCM route in its rank-one form, which would leave I_S's content (c) as
the only residue.

Recommended order: L2 first, because it is cheap and can kill the route.
Then L1, which has intrinsic value even if the route dies: it is the
exact semilocal Sonin trace formula, the ingredient CCM leave as a
program.

---

## Status

```text
CCM 2310.18423 / 2024 inventory: semilocal Sonin, θ_S, η_S, B_λ^S        CITED
Weil positivity beyond log 2 via Sonin/prolate in the sources              absent (CITED, negative search)
CM 2022: W_sa self-adjoint, negatives ⊂ Sonin, UV Riemann-type count       CITED
CCM 2511.22755: missing steps = simple-even + k_λ approximation            CITED
Suzuki 2301.00421: H_W ≅ H(E_ξ) under RH; RH ⟺ equalities                  CITED
K_S = m_S·K, complement = η_S(K^⊥) in Mellin                               PROVED (from CITED)
Prop 2.2: Son_S = (1/π)∫|ĥ|²φ_S' (positive phase symbol)                  PROVED modulo standard de Branges
Lemma 2.3: boundary layer → −2log p·p^{-1/2}Re c_h(log p), model, 1st order  PROVED (model)
Prop 2.4: all k via Widom (full p-term of E_S)                             CONDITIONAL (sketch)
§2.4: R183_018's NO-GO family absorbed, |R'| = O(Nw)‖x‖²                  PROVED given I_S
Conjecture I_S (semilocal identity, continuous ε_S)                        OPEN — type (c)
Conjecture N_T (one aligned negative direction)                            OPEN
C_T ⟹ D_T on ker ℓ; ∀T C_T ⟹ RH                                           PROVED
RH ⟹ C_T                                                                   OPEN, evidence against (§3.4)
Classification of C_T                                                       (b) strictly stronger than D; I_S is (c)
Deletion: I_S blind, N_T must fail for S∖{p}                               PROVED
Szegő falsifier: r_S<0 on positive measure ⇒ n₋ ~ cT ⇒ C_T false            CONDITIONAL (ε_S ∈ L¹, Landau–Widom)
Row D / RH                                                                   OPEN; not claimed
```

## Review points

1. **2π normalization in Prop 2.2.** It must be checked that the de
   Branges kernel diagonal gives φ_S'/π in the ds measure, and that, with
   R183_015's convention ((1/2π)∫m\|φ\|², m = 2θ'), the case S={∞}
   reproduces CC (83), i.e. that 2φ_∞' − m = transform of
   −ε(e^{\|x\|}). A factor of 2 here changes §3.4's threshold but not the
   classification.
2. **Sign and direction in Lemma 2.3.** The correction's sign depends on
   whether the semilocal Fourier condition is m_S^#·H₋ or
   (m_S^#)^{−1}·H₋. With (1−εV) one gets E_S's sign; with (1−εV)^{−1} one
   gets the opposite in the k=1 term. The deduction uses (57)–(58) and
   Prop 4.7(i). **It must be checked in the source which of the two it
   is**: if it is the opposite, the mechanism **adds** the prime term
   with the wrong sign and §2.4 reverses (immediate NO-GO).
3. **Prop 2.4 (Widom).** The formula
   Tr(W(a)W(b) − W(ab)) = Σ n a_n b_{−n} is stated for discrete Toeplitz
   operators with symbols in the weighted Wiener algebra. Here the
   continuous half-line version must be used, compressed with
   C = conv h. The claim that cross terms between primes vanish in the
   model **is not proved**.
4. **The model discards prolate nonlocality.** That the correction δε_S
   be continuous is exactly I_S. It is plausible by the decay of λ(n),
   but not demonstrated. In particular, that the projection onto an
   intersection (support ∧ Fourier) behaves, for trace purposes, like the
   sum of each condition's boundary layers plus a smooth kernel is a
   hypothesis.
5. **R162_2602 Thm 4 versus this file.** That theorem declares NO-GO for
   the semilocal **cutoff** carrier R_Λ. Here the **Sonin projection** Π_S
   is used, which is not a limit of c_Λ·Id − positive. There is no
   contradiction. Blindness to deletion is inherited, and §3.3 records it.
6. **§3.4 depends on ε ∈ L¹(R)** (decay of ε(ρ) as ρ → ∞), which CC do
   not control beyond [1,2]. If ε is not integrable, Szegő does not apply
   as is. The falsifier then remains CONDITIONAL, without changing
   classification (b).
7. **Corpus precedents**: R162_1201/1202 (Sonin range = E1 sink) and the
   grid's row 2A ("phase derivative of the semilocal Sonin trace:
   favorable sign, no exact identity"). Prop 2.2 + I_S is exactly the
   "exact identity" that row declared nonexistent. It must be checked
   that nothing incompatible was proved there.

## Note (R183_025–027)

* Lemma 2.3: minor conjugation slip (a·conj c_h(a) comes out); sum and
  sign correct (R183_027).
* N_T must be stated in the ξ metric, not in X (R183_026 §2).
* L1 remains CONDITIONAL on (Λ)+(E′) (R183_025). Low-band falsifier
  (R183_027, conditional on RH): "C_T for every T" is false unless
  ρ_{S(T)} is exponentially small on (−γ₁, γ₁).
