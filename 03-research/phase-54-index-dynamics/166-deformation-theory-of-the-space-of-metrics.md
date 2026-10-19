# Doc 166 — Deformation theory of the space of metrics on the Kreĭn space of the Weil form: the incompatibility functional, the Gram flow, and the index conservation law

**Program:** Riemann Hypothesis — Phase 54: index dynamics.
**Role of the document:** CONSTRUCTOR. Mandate: after Phases 49–53 (every route that looks for ONE
operator, ONE metric, or ONE positivity ends up asking "why is the Weil form positive?" = RH), change
the object: study the **full space of metrics** 𝕄 over the Kreĭn space (𝒦,Q) of the Weil form, the
**incompatibility functional** 𝔇 that measures the failure of simultaneous unitarity of the functional
reflection J and the scale flow U_t (GAP 164.D), and the **deformation dynamics** (the Gram flow) on
𝕄. The director's question: *why is every deformation of the candidate metric expelled?* — turn it
into a stability/conservation theorem, not a re-questioning of existence.

**Labeling contract (absolute rule).** **[NEW-DEFINITION]** = total freedom.
**[THEOREM]/[PROPOSITION]/[LEMMA]** = genuinely proved here, complete proof; external ones with a
verifiable reference. **[CONSTRUCTION]** = precisely defined object. **[BRIDGE]** = connection with
an honest status. **[GAP]/[literature GAP]** = declared; never the premise of a theorem. **[WISH]** =
declared. PERMITTED (and expected) to end in B/C/D. **NO numerics/Python. [Spanish, translated to
English.] Absolute candor: a false victory is worse than a failure.**

**Prerequisites read from source this session:** Doc 164 (inverted Stone; J RH-free unitary but in
ℤ/2, blind to m; GAP 164.D: RH ⟺ the reflection metric = the evolution metric). Phase 26 memory
(bridge: κ=2m=neg.ind(Q)=neg.ind(H_C) in Pontryagin (𝒦,Q); items V.1–V.4 NOT proved).
Phase 28 memory (second variation of Q in direction b_j; DBN = gradient of E_log; Conj. A.15:
Λ = max b_j²/2). Phase 37 memory (architecture RH = (m<∞) ∧ (m<∞ ⟹ m=0)). Phase 53/D165 memory
(Stone does NOT give a real spectrum in Kreĭn with κ>0; Bognár; Azizov–Iokhvidov).

---

## 0. Executive summary and verdict stated in advance

> **VERDICT: B′ — the wall reappears, but NOT where the mandate feared.** The theory is built in
> full and is RH-free (modulo the declared hypotheses of the Phase 26 bridge): 𝕄 is a non-empty
> convex open cone, contractible, WITHOUT assuming RH (outcome C excluded, §2); 𝔇 is convex,
> Lipschitz, and 1-homogeneous (§3); the Gram flow exists and converges (§4). The anti-circularity
> test gives an UNEXPECTED AND CLEAN NEGATIVE result: **the second variation of 𝔇 is NOT the Weil
> form** — it is the operator L = ∫e^{−2|t|}A_t^*A_t dt + A_J^*A_J ≥ 0, manifestly positive
> semidefinite and RH-free (§5.1). The circularity is NOT in the curvature (the Hessian); it is in
> three other places, now precisely localized: (1) **the Weil form W is ALWAYS a critical point of
> the extended functional** — A_t(W)=0, A_J(W)=0 unconditionally — and RH is exactly the statement
> that this critical point **lies inside the cone 𝕄** (W>0) rather than outside; the existence of the
> critical point is free, its MEMBERSHIP in the cone is RH (Theorem 166.10). (2) **κ is an exact
> conservation law of every deformation of metrics** (Theorem 166.9, by Sylvester's law of inertia):
> as G ranges over 𝕄, the negative index of the pair (Q,G) is frozen at κ; it can only jump on the
> boundary ∂𝕄 (degenerate metrics). This ANSWERS the director's question: every deformation is
> expelled because it is trying to change a conserved topological charge — the expulsion is
> conservation of inertia, not an analytic accident. (3) The infimum of 𝔇 is bounded below by an
> EXPLICIT function of the off-line zeros: 𝔇(G) ≥ φ(|b_j|)·⟨Gv_j,v_j⟩ with φ(b)=2b(1−2b)^{(1−2b)/(2b)}
> ~ (2/e)b (Theorem 166.6), and the weight e^{−|t|} of the functional is **calibrated exactly by the
> critical strip** (φ(b)<∞ ⟺ b<1/2, which is Hadamard–de la Vallée Poussin's theorem). The Gram flow
> does not stall: it EXPELS the metric toward ∂𝕄, crushing exactly the eigendirections of the
> off-line zeros, with spectral rate ℓ(b_j)=2b_j²+O(b_j⁴) — a quantitative echo of Phase 28's
> conjecture A.15 (Λ = max b_j²/2). **What is new and not RH-equivalent:** the conservation law
> (166.9), the strip↔weight calibration (166.6), the rate 2b² (166.13), and the structural rewriting
> "RH ⟺ the infimum is attained" — isomorphic in FORM to Rodgers–Tao's Λ≥0 (RH as membership in the
> boundary of a variational problem, §4.4).
> **What is RH-rewritten (declared):** "∃G∈𝕄 with 𝔇(G)=0" ⟺ m=0 (Theorem 166.7) — that is GAP 164.D
> formalized, no new content. The document's new content is in the geometry around it (166.6, 166.9,
> 166.10, 166.12, 166.13).
> **The stability tool the mandate expected** (Łojasiewicz–Simon) turns out to be INAPPLICABLE for a
> good reason: when m≥1 there is no interior critical point to stabilize (Corollary 166.8); the tool
> the wall calls for is a different one, and it is now named: **boundary index-jump theory on 𝕄**
> (singular degenerations of metrics), the exact dual of the De Bruijn–Newman boundary Λ=0.

---

## 1. Framework and declared hypotheses

### 1.1 The background scenario (RH-free, with a non-degeneracy GAP)

I work on a complex vector space K with:

- **(H-W) The Weil form as a bounded, non-degenerate form.** A background hermitian inner product
  ⟨·,·⟩₀ (RH-free: for example the Haar L² of Connes's setting, or the L²(dτ) of the critical line —
  Doc 164 §2.2 verifies it exists without ζ) that makes K a Hilbert space, and the Weil form Q(·,·),
  hermitian, ⟨·,·⟩₀-bounded, represented by its **Gram operator**
  W = W* ∈ B(K): Q(x,y) = ⟨Wx,y⟩₀, with W **boundedly invertible**.
  [GAP 166.A] The Weil form on test functions may have a radical and W may not be invertible
  (0 in the continuous spectrum); the clean statement requires passing to the quotient by the radical
  and completing. This is the theory's standard move (Bognár 1974, ch. I §11), but the lower bound
  |W| ≥ ε is NOT verified for the concrete Weil form. Everything that follows is the theory on the
  model (K, ⟨·,·⟩₀, W) with W invertible; the transfer to the arithmetic object inherits this GAP.

- **(H-Π) Pontryagin regime: m < ∞.** The negative index of Q is κ = 2m < ∞ (Phase 26; the
  program's convention: m Klein orbits of off-line zeros ↦ κ=2m). This is NOT free: Phase 37's
  architecture is RH = (m<∞) ∧ (m<∞ ⟹ m=0). **This document lives entirely in the second
  conjunct**: I assume m<∞ and study the deformation of metrics in Π_κ. With κ<∞, (K,Q) is a
  Pontryagin space and the classical theory applies (Pontryagin 1944; Iokhvidov–Krein 1956;
  Bognár 1974; Azizov–Iokhvidov 1989).

- **(H-26) The dynamical bridge of Phase 26 (declared, not proved).** The two symmetries of D164:
  (i) a one-parameter group U_t ∈ B(K), **Q-unitary** (Q(U_tx,U_ty)=Q(x,y), equivalently
  U_t^*WU_t = W, with * the background adjoint) — the scale flow —, and an involution J = J^{−1},
  **both Q-unitary and ⟨·,·⟩₀-unitary** (D164 Prop 164.6: the functional reflection is RH-free
  unitary), with the reflection relation J U_t J = U_{−t};
  (ii) for each off-line zero ρ_j = (½+b_j) + iγ_j (j=1,…,m′, with m′ counting the Klein quadruple
  according to Phase 26's convention) a **genuine eigenvector** v_j ∈ K of the group:
  U_t v_j = e^{itλ_j} v_j with λ_j = γ_j + i b_j, b_j ≠ 0 — this is Phase 26's V.2, NOT proved
  (the characters x^{b+iγ} might only be generalized/isotropic eigenvectors);
  (iii) growth bound ‖U_t‖₀ ≤ C(1+|t|)^d e^{b_max|t|} with b_max = max_j|b_j| < ½ — the
  quantitative form of U_t being π-unitary in Π_κ with non-real spectrum confined to the strip
  (Iokhvidov–Krein 1956: π-unitaries are bounded; the group's exponential growth is governed by the
  imaginary parts of the generator's non-real eigenvalues, with a polynomial factor from the Jordan
  blocks in the root subspaces, of total dimension ≤ 2κ).
  **Every proposition using (H-26) cites it explicitly.** That b_max < ½ strictly for each zero is
  unconditional: there are no zeros on Re s = 1 or Re s = 0 (Hadamard 1896; de la Vallée Poussin
  1896), so each b_j ∈ (−½,½) — though sup b_j = ½ is not excluded if m=∞; under (H-Π) the maximum is
  attained and b_max < ½.

- **(H-26⁺) Concentration of the index (reinforcement, declared).** The root subspace N ⊂ K of the
  generator's non-real spectrum (dim N ≤ 2κ < ∞) is Q-non-degenerate (this part IS general theory:
  the root subspace of the non-real spectrum of a π-self-adjoint operator is non-degenerate and the
  root subspaces of λ and λ̄ pair hyperbolically — Azizov–Iokhvidov 1989, ch. 2 §2; Krein–Langer
  1973), ALL of the negative index of Q lives in N, and Q is **uniformly positive** on the
  Q-orthocomplement K₁ = N^{[⊥]}: Q|_{K₁} ≥ ε₁ > 0. [GAP 166.B] The concentration of the index in N
  is not automatic (real eigenvalues can carry negative eigenvectors) and the uniformity ε₁>0 is
  exactly GAP 166.A restricted to K₁. (H-26⁺) is used only in Proposition 166.11 (collapse) and is
  flagged.

### 1.2 Anti-circularity of the framework

⟨·,·⟩₀ is RH-free (Haar/Lebesgue). W is the Weil form: an unconditional object (the quadratic form of
the explicit formula), RH-free AS A FORM; what would be RH is its positivity, which is NOT assumed.
U_t and J are RH-free as operators (D164); what is conditional is (H-26)(ii) — that the off-line
zeros give eigenvectors in K — which is a hypothesis about the SPACE, not about RH (if m=0 the
hypothesis is vacuous and the whole document still holds trivially). The framework passes the guard.

---

## 2. The space 𝕄 of metrics

### 2.1 [NEW-DEFINITION 166.1 — the space of metrics and its boundary]

$$\mathbb{M} \;=\; \{\,G \in B(K) \;:\; G = G^{*},\ \exists\, \varepsilon>0:\ G \geq \varepsilon I\,\}$$

(admissible Gram operators with respect to the background; the associated metric is
⟨x,y⟩_G = ⟨Gx,y⟩₀, a positive-definite inner product with a norm equivalent to the background one if
G is also bounded — both conditions in the definition). Two subobjects:

- **The boundary** ∂𝕄 = {G ≥ 0, G = G*, G not boundedly invertible}: the **degenerate metrics**
  (seminorms). They do not belong to 𝕄; they are the limits of its sequences.
- **The Q-adapted subspace** 𝕄_Q = {G ∈ 𝕄 : G = WS for some involution S (S²=I) with WS > 0}
  — equivalently, the metrics of the form ⟨x,y⟩_S = Q(Sx,y) with S a **fundamental symmetry**
  of the Kreĭn space (K,Q) (Bognár 1974, ch. IV; Azizov–Iokhvidov 1989, ch. 1 §3). These are the
  metrics "that read Q": in them Q is block-diagonalized into positive ⊕ negative.

### 2.2 [PROPOSITION 166.2 — 𝕄 is non-empty, open convex cone, contractible; RH-free]

**Statement.** Under (H-W) alone (no RH, no (H-26)): (a) 𝕄 ≠ ∅ (it contains I). (b) 𝕄 is a convex
open cone in the real Banach space B_h(K) of bounded ⟨·,·⟩₀-self-adjoint operators.
(c) 𝕄 is contractible (in fact, convex). (d) In finite dimension n, 𝕄 ≅ GL(n,ℂ)/U(n), the symmetric
space of metrics; in general it is the Banach version of that homogeneous space, with transitive
GL(K)-action G ↦ T*GT.

**Proof.** (a) I ∈ 𝕄. (b) If G₁ ≥ ε₁, G₂ ≥ ε₂, then sG₁+(1−s)G₂ ≥ min(ε₁,ε₂) > 0, and λG₁ ≥ λε₁
for λ>0: a convex cone. Open: if G ≥ ε and ‖H−G‖ < ε/2 with H self-adjoint, then H ≥ ε/2. (c)
Convex ⟹ contractible. (d) Transitivity: given G₁,G₂ ∈ 𝕄, T = G₁^{−1/2}G₂^{1/2} satisfies T*G₁T = G₂
(direct calculation with positive square roots, continuous functional calculus); the stabilizer of I
is {T: T*T = I} = the background unitary group. In finite dimension this is the classical
identification of the cone of positive-definite matrices with GL(n,ℂ)/U(n). ∎

### 2.3 [PROPOSITION 166.3 — 𝕄_Q is non-empty and contractible without RH: the Kreĭn parametrization by angle operators]

**Statement.** Under (H-W) and (H-Π) (κ<∞), without RH: (a) 𝕄_Q ≠ ∅. (b) 𝕄_Q is in bijection with
the set of κ-dimensional maximal Q-negative-definite subspaces, and this with the open unit ball of
strict contractions {T ∈ B(K₋⁰, K₊⁰) : ‖T‖ < 1}, where K = K₊⁰ ⊕ K₋⁰ is a reference fundamental
decomposition (dim K₋⁰ = κ). In particular 𝕄_Q is non-empty, connected, and contractible. (c) All
metrics in 𝕄_Q induce equivalent norms (among themselves and with the background one). (d) **No
G ∈ 𝕄_Q makes Q positive**: in every fundamental decomposition the negative part has dimension
exactly κ.

**Proof.** (a) W = W* invertible; spectral decomposition W = W₊ − W₋ with W± ≥ 0 of complementary
spectral ranges; S₀ := sign(W) (Borel functional calculus over W's spectrum, which does not contain
0) satisfies S₀² = I and WS₀ = |W| ≥ ε > 0; hence G₀ = WS₀ ∈ 𝕄_Q. This uses only (H-W). Under
(H-Π), dim ran(negative spectral projector) = κ. (b) This is the classical angle-operator theory:
every fundamental decomposition K = K₊ [+] K₋ is determined by its negative part K₋ (the positive
part is the Q-orthocomplement), K₋ is a maximal Q-negative-definite subspace of dimension κ
(Pontryagin 1944: in Π_κ every maximal non-positive subspace has dimension κ), and
K₋ = {x + Tx : x ∈ K₋⁰} for a unique T: K₋⁰ → K₊⁰ with Q(x+Tx, x+Tx) = ‖Tx‖²_+ − ‖x‖²_- < 0 for
x ≠ 0, which in finite dimension of K₋⁰ is equivalent to ‖T‖ < 1 (compactness of the sphere of
K₋⁰). Conversely every strict contraction gives a maximal negative part. (Azizov–Iokhvidov 1989,
ch. 1 §8; Bognár 1974, ch. V.) The ball {‖T‖<1} is convex, hence contractible. (c) Equivalence of
norms between fundamental symmetries: Bognár 1974, ch. IV, Thm 6.4 (in Π_κ, a consequence of the
finite dimension of the defect). (d) Inertia law in Π_κ (Pontryagin 1944): κ is an invariant of the
form, not of the decomposition. ∎

**Interpretation.** **Outcome C is excluded**: the space of metrics does NOT collapse without RH — it
is huge (an infinite-dimensional convex cone), and even its Q-adapted part is a non-empty, contractible
ball of contractions. What does not exist without RH is not "metrics" but *a metric compatible with
the dynamics* — that is §3. And (d) already announces the conservation law: no deformation of the
metric moves κ.

### 2.4 [REMARK 166.4 — the Haar escape and why it does not trivialize the problem]

On the LARGE space L²(ℝ₊*, d*λ), both U_t (dilations) and J (inversion v↦1/v, since d*λ is
inversion-invariant) are unitary with respect to the Haar metric: there 𝔇 = 0 with an RH-free
metric. This does NOT contradict anything that follows: on that space the generator has continuous
spectrum ℝ and NO eigenvector with non-real eigenvalue — it is the ζ-blind flow of D164 §2.2(i). The
theory of this document lives in K = the space of the Phase 26 bridge, where (H-26)(ii) places the
off-line zeros as eigenvalues. **The metric incompatibility is born exactly when passing from the
blind space to the arithmetic space**; the functional 𝔇 measures the cost of that passage.

---

## 3. The incompatibility functional 𝔇

### 3.1 [NEW-DEFINITION 166.5 — the defects and the functional]

For G ∈ B_h(K) I define the **defect operators** (linear in G):

$$A_t(G) \;=\; U_t^{*} G\, U_t - G \qquad (t\in\mathbb{R}), \qquad A_J(G) \;=\; J^{*} G\, J - G,$$

and the **incompatibility functional**

$$\boxed{\;\mathfrak{D}(G) \;=\; \sup_{t\in\mathbb{R}} e^{-|t|}\,\bigl\|A_t(G)\bigr\|_0 \;+\; \bigl\|A_J(G)\bigr\|_0\;}$$

Meaning: A_t(G) = 0 ∀t ⟺ U_t is G-unitary; A_J(G) = 0 ⟺ J is G-unitary. 𝔇(G) = 0 ⟺ G is the
common metric of GAP 164.D. The weight e^{−|t|} will be justified in Theorem 166.6: it is calibrated
by the critical strip.

**[PROPOSITION 166.5′ — structural properties].** Under (H-26)(i),(iii):
(a) 𝔇 is well-defined (finite) on B_h(K) and is Lipschitz: 𝔇(G) ≤ c_U‖G‖ with
c_U = sup_t e^{−|t|}(1+‖U_t‖₀²) + (1+‖J‖₀²) < ∞ (finite because 2b_max < 1 by (H-26)(iii)).
(b) 𝔇 is **convex** and positively 1-homogeneous.
(c) 𝔇 is invariant under the isometric involution σ(G) = J^*GJ, and **the J term is free**: for
every G ∈ 𝕄, the average G′ = ½(G + σG) ∈ 𝕄 satisfies A_J(G′) = 0 and 𝔇(G′) ≤ 𝔇(G). Hence
inf_𝕄 𝔇 = inf{ sup_t e^{−|t|}‖A_t(G)‖ : G ∈ 𝕄, J^*GJ = G }.

**Proof.** (a) ‖A_t(G)‖ ≤ (‖U_t‖₀²+1)‖G‖ and e^{−|t|}‖U_t‖₀² ≤ C²(1+|t|)^{2d}e^{(2b_max−1)|t|} → 0;
the supremum is finite. The difference |𝔇(G)−𝔇(H)| ≤ c_U‖G−H‖ by the triangle inequality in each term.
(b) G ↦ A_t(G) and G ↦ A_J(G) are linear; the norm is convex; the supremum of convex functions is
convex; the sum preserves this. Homogeneity is evident. (c) J is ⟨·,·⟩₀-unitary and involutive
((H-26)(i)), so σ is a linear isometric involution of B_h(K) preserving 𝕄. With JU_t = U_{−t}J:
U_t^*J^*GJU_t = (JU_t)^*G(JU_t) = (U_{−t}J)^*G(U_{−t}J) = J^*A_{−t}(G)J + J^*GJ, whence
A_t(σG) = J^*A_{−t}(G)J and ‖A_t(σG)‖ = ‖A_{−t}(G)‖; since the weight is even in t, the first term of
𝔇 is σ-invariant; also A_J(σG) = J^*(J^*GJ)J − J^*GJ = G − J^*GJ = −J^*A_J(G)J... directly
‖A_J(σG)‖ = ‖A_J(G)‖. Hence 𝔇∘σ = 𝔇. For the average: A_J(G′) = ½(A_J(G) + A_J(σG)) =
½(J^*GJ − G + G − J^*GJ) = 0, and 𝔇(G′) ≤ ½𝔇(G) + ½𝔇(σG) = 𝔇(G) by convexity and invariance. ∎

**Interpretation of (c).** This recovers quantitatively D164: the functional reflection is the CHEAP
symmetry (its compatibility is achieved for free by averaging); all of 𝔇's cost is in the scale flow
term. GAP 164.D concentrates, with no loss, on the dynamical term.

### 3.2 [THEOREM 166.6 — universal lower bound: incompatibility sees every off-line zero, with weight calibrated by the strip]

**Statement.** Under (H-26). Let G ∈ 𝕄 and let v_j be the eigenvector of an off-line zero with
b_j ≠ 0. Then

$$\mathfrak{D}(G) \;\geq\; \varphi(|b_j|)\,\frac{\langle G v_j, v_j\rangle_0}{\|v_j\|_0^2}, \qquad
\varphi(b) := \sup_{t>0} e^{-t}\bigl(e^{2bt}-1\bigr) \;=\; 2b\,(1-2b)^{\frac{1-2b}{2b}},$$

where φ: (0,½) → (0,1) is strictly increasing, φ(b) = (2/e)\,b\,(1+O(b)) as b→0⁺,
φ(b) → 1 as b→½⁻, **and φ(b) = +∞ if b ≥ ½**. Consequences:

(i) (calibration) The weight e^{−|t|} is exactly the weakest weight that keeps 𝔇 finite over
π-unitary groups whose non-real spectrum lies in the critical strip: finiteness of 𝔇 uses b_max < ½,
i.e., the Hadamard–de la Vallée Poussin theorem. The critical strip IS the integrability region of
the functional.

(ii) (pointwise positivity) If m ≥ 1, then 𝔇(G) > 0 for EVERY G ∈ 𝕄: **the functional has no zeros
in the interior of the cone.**

(iii) (normalized bound) inf{𝔇(G) : G ∈ 𝕄, G ≥ I} ≥ φ(b_max) > 0 if m ≥ 1.

**Proof.** Let λ_j = γ_j + ib_j, U_t v_j = e^{itλ_j}v_j, |e^{itλ_j}|² = e^{−2b_jt}. Then

⟨A_t(G)v_j, v_j⟩₀ = ⟨G U_t v_j, U_t v_j⟩₀ − ⟨Gv_j,v_j⟩₀ = (e^{−2b_j t} − 1)⟨Gv_j,v_j⟩₀.

Choosing the sign of t with b_j t < 0 (both signs available in the supremum), the factor is
e^{2|b_j||t|} − 1 > 0, and since ‖A_t(G)‖₀ ≥ |⟨A_t(G)v_j,v_j⟩₀|/‖v_j‖₀²,

𝔇(G) ≥ sup_{s>0} e^{−s}(e^{2|b_j|s} − 1)·⟨Gv_j,v_j⟩₀/‖v_j‖₀².

Computing φ: g(s) = e^{(2b−1)s} − e^{−s} with 0<b<½; g(0)=0, g(∞)=0, g′(s) = (2b−1)e^{(2b−1)s} +
e^{−s} = 0 ⟺ e^{−2bs} = 1−2b ⟺ s_* = −log(1−2b)/(2b); value
φ(b) = e^{−s_*}(e^{2bs_*}−1) = (1−2b)^{1/(2b)}·\frac{2b}{1−2b} = 2b(1−2b)^{(1−2b)/(2b)}.
Monotonicity: the integrand e^{−s}(e^{2bs}−1) is increasing in b for each s>0, hence so is the
supremum. Asymptotics: (1−2b)^{1/(2b)} → e^{−1} (b→0) gives φ ~ 2b/e; as b→½⁻ the exponent
(1−2b)/(2b) → 0 gives φ → 2·½·1 = 1. If b ≥ ½, g(s) does not decay and the supremum is ∞ — hence
(i): for a group with an eigenvalue at distance ≥ ½ from ℝ, the functional with weight e^{−|t|}
diverges over EVERY G (same identity with ⟨Gv,v⟩ > 0); that this does not occur is exactly b_j < ½
for every zero, i.e. the non-vanishing on Re s = 1. (ii): G ≥ εI with ε>0 depending on G gives
⟨Gv_j,v_j⟩₀ ≥ ε‖v_j‖₀² > 0, hence 𝔇(G) ≥ εφ(|b_j|) > 0. (iii): with uniform ε = 1,
𝔇(G) ≥ max_j φ(|b_j|) = φ(b_max). ∎

### 3.3 [THEOREM 166.7 — the zero of 𝔇 is RH rewritten (the honestly-declared part)]

**Statement.** Under (H-26): there exists G ∈ 𝕄 with 𝔇(G) = 0 ⟹ m = 0. Conversely, if m = 0 AND
the Weil form is uniformly positive (W ≥ ε, GAP 166.A), then G = W ∈ 𝕄 and 𝔇(W) = 0. In sum,
modulo (H-26) and the uniformity GAP: **∃G ∈ 𝕄: 𝔇(G)=0 ⟺ RH.** This statement is GAP 164.D
formalized; it is declared RH-rewritten, with no new content. The document's new content is in the
geometry around it (166.6, 166.9, 166.10, 166.12, 166.13).

**Proof.** (⟹) Contrapositive of 166.6(ii). (⟸) U_t is Q-unitary ((H-26)(i)) ⟺ U_t^*WU_t = W ⟺
A_t(W) = 0 ∀t; J Q-unitary gives A_J(W) = 0. If W ≥ ε then W ∈ 𝕄 and 𝔇(W) = 0. ∎

**[PROPOSITION 166.7′ — Pontryagin–Stone reading in 𝕄_Q: compatibility = invariant decomposition].**
Under (H-26), if G = WS ∈ 𝕄_Q and sup_t‖A_t(G)‖ = 0, then [S, U_t] = 0 ∀t, the fundamental
decomposition K = K₊ [+] K₋ associated with S is U_t-invariant, and U_t splits into two genuine
unitary groups: on (K₊, Q) and on (K₋, −Q), both Hilbert spaces (the second of finite dimension κ).
By Stone (on K₋, finite-dimensional: linear algebra) both generators have real spectrum; hence
there is no eigenvector v_j of (H-26)(ii) with b_j ≠ 0, i.e. m = 0.
**Proof.** A_t(WS) = U_t^*WSU_t − WS = W(U_t^{−1}SU_t − S) using U_t^*W = WU_t^{−1} (from
U_t^*WU_t = W and W invertible); since W is invertible, A_t(WS) = 0 ⟺ U_t^{−1}SU_t = S ⟺ [S,U_t]=0.
Then the eigenspaces K_± = ker(S ∓ I) are U_t-invariant; on K₊ the form Q is the inner product
⟨·,·⟩_S restricted (positive, complete: Bognár 1974 ch. V) and U_t preserves it (Q-unitarity +
invariance) ⟹ unitary group ⟹ self-adjoint generator ⟹ real spectrum (Stone 1932; Reed–Simon I
Thm VIII.8); on K₋, −Q is an inner product in dimension κ and the same holds by linear algebra. An
eigenvector with non-real eigenvalue would have components in K₊ or K₋ that would be non-real
eigenvectors of unitary groups: impossible. ∎

**Interpretation.** The wall mechanism in deformation language: *metric compatibility = existence of
a fundamental decomposition invariant under the flow* — and that splits the flow into two unitary
blocks with real spectrum. It is the metric version of D165's theorem ("Stone does not give a real
spectrum in Kreĭn with κ>0"): here one sees WHY — the flow with non-real spectrum leaves no maximal
negative definite part invariant (it leaves non-positive maximal subspaces invariant — Pontryagin
1944 — but those are isotropic in the root directions, not definite, and do not induce a metric).

### 3.4 [COROLLARY 166.8 — when m ≥ 1 there is no interior critical point: Łojasiewicz–Simon does not apply, for a good reason]

If m ≥ 1, by 166.6(ii) the convex functional 𝔇 is strictly positive on all of 𝕄; since it is also
1-homogeneous, it has no nontrivial local interior minima (a local minimum of a convex function is
global; the global value with normalization G ≥ I is ≥ φ(b_max) and is not attained in general —
§3.5). **The tool the mandate proposed importing (Łojasiewicz 1963; Simon 1983) presupposes a
critical point to stabilize around; here, in the case m ≥ 1, NO interior critical point exists.**
The problem is not stability of an equilibrium: it is boundary behavior. (If m=0 + uniformity, there
is a minimum W, and by the quadratic convexity of the smooth substitute §4 the Łojasiewicz
inequality holds trivially with exponent ½ — but then RH is already given; the tool arrives late in
both scenarios.)

### 3.5 [PROPOSITION 166.11 — the directed collapse: the normalized infimum is 0 and is not attained; RH ⟺ it is attained]

**Statement.** Under (H-26) and (H-26⁺). With normalization ‖G‖₀ = 1 (instead of G ≥ I):

(a) inf{𝔇(G) : G ∈ 𝕄, ‖G‖₀ = 1} = 0 **even if m ≥ 1**, realized by sequences G_δ that degenerate
exactly on N (the root subspace of the off-line zeros): G_δ = δ·g_N ⊕ W₁ with
𝔇(G_δ) ≤ Cδ → 0, where W₁ = the Gram operator of Q|_{K₁} and g_N any J-invariant metric on N.

(b) Every minimizing sequence crushes the off-line eigenvectors: 𝔇(G_n) → 0 ⟹
⟨G_n v_j, v_j⟩₀ → 0 for every j, with rate ⟨G_nv_j,v_j⟩₀ ≤ 𝔇(G_n)‖v_j‖₀²/φ(|b_j|).

(c) The infimum IS ATTAINED in 𝕄 ⟺ m = 0 (modulo the uniformity GAP of 166.7).

**Proof.** (a) Under (H-26⁺), K = N [+]_Q K₁ with both summands U_t- and J-invariant (N is a sum
of root subspaces of the non-real spectrum: invariant under the group and under J since J conjugates
the spectrum γ↦−γ permuting those root subspaces; K₁ is its Q-orthocomplement, invariant because U_t
and J are Q-unitary). I choose the background product so that the sum is ⟨·,·⟩₀-orthogonal (licit:
equivalent norms, dim N < ∞). Then everything is block-diagonal: A_t(G_δ) = δ·A_t^N(g_N) ⊕
A_t^1(W₁). The second block is 0: U_t|_{K₁} is Q₁-unitary and W₁ is the Gram operator of Q₁
(positive ≥ ε₁ by (H-26⁺), hence G_δ ∈ 𝕄 for every δ>0). The first: ‖A_t^N(g_N)‖ ≤ ‖g_N‖(1+‖U_t|_N‖²)
≤ C(1+|t|)^{2d}e^{2b_max|t|}, and with the weight, sup_t e^{−|t|}δ(⋯) ≤ C′δ because 2b_max<1. The J
term vanishes by averaging g_N under J|_N (Prop. 166.5′(c), in finite dimension the average is a
metric). ‖G_δ‖₀ ≈ ‖W₁‖ is renormalized to 1 without affecting the orders. Hence 𝔇(G_δ) ≤ C′δ → 0.
(b) Immediate from 166.6. (c) (⟸) 166.7. (⟹) If G ∈ 𝕄 attains the infimum 0, 166.6(ii) forces
m = 0. ∎

**Interpretation (the document's structural result, together with 166.9).** The variational problem
has the structure **"infimum zero, attained ⟺ RH"**: the critical value is attainable only on the
boundary ∂𝕄 (degenerate metrics whose kernel is exactly N). Minimizing sequences do not choose just
any degeneration: **they crush exactly the directions of the off-line zeros** — the optimization
dynamics tries to EXPEL from the space the vectors that carry κ, via the quotient K → K/N. The
failure mode predicted by the mandate ("the only critical point is the spectral metric built from
the zeros") is confirmed but with precise geometry: the limit object is the Weil metric over the
positive part K₁, degenerate on N — and that object is now characterized as the **boundary
attractor of an RH-free dynamics**, not as a choice.

---

## 4. The Gram flow and the index conservation law

### 4.1 [THEOREM 166.9 — κ is an exact conservation law of EVERY deformation of metrics]

**Statement.** Under (H-W) and (H-Π), without RH and without (H-26). For G ∈ 𝕄 define the **visible
index** κ(G) := the dimension of the negative spectral subspace of G^{−1/2} W G^{−1/2} (the Gram
operator of Q in G's geometry). Then:

$$\kappa(G) \;=\; \kappa \qquad \text{for EVERY } G \in \mathbb{M}.$$

In particular κ(G(s)) is constant along any curve (continuous, not even needed) in 𝕄 — under the
Gram flow, under any flow. **The negative index is not deformable by metrics: it is a topological
charge of the pair (Q, 𝕄), and can only jump on ∂𝕄.**

**Proof.** T := G^{−1/2} is invertible; G^{−1/2}WG^{−1/2} = T^*WT is congruent to W. Inertia is
invariant under congruence: if M ⊂ K is a subspace on which ⟨T^*WTx,x⟩₀ < 0 (x≠0), then T(M) is a
subspace of the same dimension on which ⟨Wy,y⟩₀ < 0, and conversely with T^{−1}; taking suprema of
dimensions gives n_−(T^*WT) = n_−(W) = κ (Sylvester's law of inertia; in Π_κ, Pontryagin 1944 /
Bognár 1974 ch. IV: all maximal negative parts have dimension κ). On ∂𝕄 the argument dies exactly
where it should: T = G^{−1/2} ceases to be bounded/invertible and the congruence ceases to be an
isomorphism — the eigenvalues of G^{−1/2}WG^{−1/2} can reach 0 and cross. ∎

**Interpretation — the answer to the director's question.** *"Why is every deformation of the
candidate metric expelled?"* Proved answer: because the defect the deformation is trying to
eliminate (κ > 0, visible in the incompatibility 𝔇 > 0, Theorem 166.6) is a **conserved quantity**
of the metric deformation. It is not that the good point is unstable or elusive: it is that the
class of allowed deformations (G ∈ 𝕄, Q fixed) exactly conserves the obstruction. The expulsion is
conservation of inertia. This also PROVES a new, useful no-go: **no scheme that deforms only the
metric (with the Weil form fixed) can reduce κ** — the only way out is through the boundary
(degenerating the metric = quotienting the space) or by moving the FORM (the De Bruijn–Newman flow).

### 4.2 [BRIDGE 166-DBN — exact duality with the De Bruijn–Newman flow]

| | DBN flow (function) | Gram flow (metric) |
|---|---|---|
| dynamical variable | the form: W_t (Gram operator of the Weil form of H_t, the heat flow on Ξ) | the metric: G(s), with W FIXED |
| what is frozen | the ambient metric (DBN is blind to the metric) | the Weil form W |
| index κ | can DECREASE: the reality of the zeros is monotone in t (de Bruijn 1950, Thm 13: if H_{t₀} has only real zeros, so does H_t for t ≥ t₀); κ(t) non-increasing in the sense of counting non-real pairs | CONSERVED exactly (Theorem 166.9) |
| RH as a boundary | RH ⟺ Λ = 0: Λ ≤ 0 (Newman's definition, 1976) and Λ ≥ 0 (Rodgers–Tao 2020) — "RH barely true", the arithmetic point is ON the boundary | RH ⟺ the infimum of 𝔇 (which is 0) IS ATTAINED — the minimizer is ON the boundary ∂𝕄 (166.11) |
| crossing mechanism | heat pushes the zeros onto the line (collisions at t>Λ) | the degeneration crushes N and quotients the off-line zeros out of the space |

**Honest status.** The row "κ(t) non-increasing" on the DBN side is the translation of de Bruijn's
monotonicity theorem into index language via the Phase 26 bridge, which is NOT proved
([BRIDGE], not a theorem; the fine equality is Phase 28's conjecture A.15: Λ = max b_j²/2). The dual
structure is crisp: **DBN moves the form with the metric frozen and the index can drop; Gram moves
the metric with the form frozen and the index cannot drop.** The dynamical variable of one is the
conserved quantity of the other. Both place RH at the BOUNDARY of their deformation space. Whether
there is a coupled flow (W_t, G_s) that swaps the two boundaries, I do not know: [WISH 166.C].

### 4.3 [CONSTRUCTION 166.12 — the Gram flow; smooth substitute]

The functional 𝔇 is convex but not differentiable (norms, supremum). For the dynamics I use the
**smooth quadratic substitute**

$$\mathfrak{D}_2(G) \;=\; \tfrac12\int_{\mathbb{R}} e^{-2|t|}\,\|A_t(G)\|_{HS}^2\,dt \;+\; \tfrac12\|A_J(G)\|_{HS}^2,$$

with ‖·‖_{HS} the Hilbert–Schmidt norm. [GAP 166.D] In infinite dimension ‖A_t(G)‖_{HS} may be
infinite for generic G; the flow theory is established with a complete proof in the
**finite-dimensional model** (K_fin, Q_fin, U_t, J) — in particular on the block N ⊕ (a finite piece
of K₁), which is where the whole obstruction lives — and is stated as formal in general. In the
model:

𝔇₂ is a quadratic form ≥ 0 on the real space H_h := {G hermitian} with the HS product:
𝔇₂(G) = ½⟨LG, G⟩_{HS}, where

$$L \;=\; \int_{\mathbb{R}} e^{-2|t|} A_t^{*}A_t\,dt + A_J^{*}A_J \;\geq\; 0,
\qquad A_t^{*}(M) = U_t M U_t^{*} - M,$$

(the HS adjoint of A_t; direct calculation: ⟨A_t(G),M⟩_{HS} = ⟨G, A_t^*(M)⟩_{HS}). The **Gram flow**
is the gradient flow

$$\dot G \;=\; -\nabla \mathfrak{D}_2(G) \;=\; -LG, \qquad G(0)=G_0\in\mathbb{M},$$

which is **linear**: G(s) = e^{−sL}G₀. (For the non-smooth 𝔇, the subgradient flow of a convex
function exists and is contractive — Brezis 1973 — but the linear one suffices to extract the full
structure.)

### 4.4 [THEOREM 166.13 — dynamics of the Gram flow in the model: the universal critical point is W; the flow expels toward the boundary; rate 2b²]

**Statement.** In the finite-dimensional model, under (H-26) restricted to the model:

(a) **(The universal critical point is the Weil form.)** ker L = {G hermitian : A_t(G)=0 ∀t,
A_J(G)=0}, and **W ∈ ker L unconditionally** (without RH). The set of fixed points of the flow
always contains the Weil form — as a hermitian FORM, not necessarily as a metric.

(b) **(Structure of ker L: only λ↔λ̄ pairings.)** If the generator is semisimple with eigenvectors
{v_μ} forming a ⟨·,·⟩₀-orthonormal basis (normal model), then G ∈ ker L ⟺
⟨Gv_μ, v_ν⟩ = 0 unless λ_μ = λ̄_ν. In particular, every G ∈ ker L satisfies ⟨Gv_j, v_j⟩ = 0 on each
off-line eigenvector (b_j ≠ 0): the elements of ker L are "hyperbolic" on N, exactly like W.

(c) **(Expulsion.)** If m ≥ 1, **no element of ker L is positive definite** (G ∈ ker L, G ≥ 0 ⟹
Gv_j = 0, propagated through Jordan chains ⟹ G vanishes on N). The flow G(s) = e^{−sL}G₀ converges
to G_∞ = P_{ker L}G₀, which is either degenerate (∈ ∂𝕄 with kernel ⊇ N if G_∞ ≥ 0) or indefinite —
in which case the flow LEAVES the cone 𝕄 in finite time. In either case: **the Gram flow expels
every initial metric toward (or through) the boundary ∂𝕄**, in exact consistency with the
conservation of κ (166.9): inside 𝕄 the defect cannot vanish, so gradient descent can only exit.

(d) **(Expulsion rate = 2b².)** In the normal model, the diagonal direction E_j = ⟨·,v_j⟩₀v_j of an
off-line zero is an eigenvector of L with exact eigenvalue

$$\ell(b_j) \;=\; \frac{1}{1-4b_j^2} \;-\; \frac{2}{1-b_j^2} \;+\; 1 \;=\; 2b_j^2 + O(b_j^4),$$

increasing in |b_j| and diverging as |b_j| → ½. The flow crushes the direction of off-line zero j at
exponential rate e^{−ℓ(b_j)s}.

**Proof.** (a) ⟨LG,G⟩ = 2𝔇₂(G) = ∫e^{−2|t|}‖A_t(G)‖²dt + ‖A_J(G)‖²; since L ≥ 0, LG = 0 ⟺
⟨LG,G⟩=0 ⟺ A_t(G)=0 for almost every t — and by continuity in t, for every t — and A_J(G)=0. W:
the Q-unitarity of U_t and J ((H-26)(i)) is A_t(W)=0, A_J(W)=0. (b) For G with A_t(G)=0:
⟨Gv_μ,v_ν⟩ = ⟨GU_tv_μ, U_tv_ν⟩ = e^{it(λ_μ−\bar\lambda_ν)}⟨Gv_μ,v_ν⟩ for all t, so either
⟨Gv_μ,v_ν⟩=0 or λ_μ = λ̄_ν. Diagonal μ=ν with non-real λ_μ: λ_μ ≠ λ̄_μ forces ⟨Gv_μ,v_μ⟩=0.
(c) If G ∈ ker L and G ≥ 0: ⟨Gv_j,v_j⟩=0 and Cauchy–Schwarz for semidefinite forms give Gv_j = 0. If
w is a Jordan vector with (H−λ_j)w = v_j (non-semisimple case), U_tw = e^{itλ_j}(w + it v_j) and
⟨GU_tw,U_tw⟩ = e^{−2b_jt}(⟨Gw,w⟩ + 2Re(it̄⟨Gv_j,w⟩) + |t|²⟨Gv_j,v_j⟩) = e^{−2b_jt}⟨Gw,w⟩ (using
Gv_j=0); constancy in t forces ⟨Gw,w⟩=0 ⟹ Gw=0; induction along the chain: G|_N = 0. Then:
G_∞ = lim e^{−sL}G₀ = P_{ker L}G₀ (spectral decomposition of L ≥ 0 in finite dimension; the
component in (ker L)^⊥ decays like e^{−s·gap}). G_∞ ∈ ker L; G_∞ is hermitian, a limit of... the
linear flow does NOT preserve the cone in general, and that is the content: if G_∞ ≥ 0, by the
above ker G_∞ ⊇ N ≠ 0 and G_∞ ∈ ∂𝕄; if G_∞ is not ≥ 0, by continuity of eigenvalues there exists
s_* < ∞ with λ_min(G(s_*)) = 0: the flow crosses ∂𝕄 in finite time. In both cases the trajectory
does not stay in 𝕄 with 𝔇₂ → 0: consistent with 166.6(ii) (no interior zeros) and 166.9 (κ frozen
in the interior). (d) In the normal model U_t^*v_j = e^{i t \bar\lambda_j}... with an orthonormal
eigenvector basis, U_t is diagonal, so is U_t^*, and A_t acts diagonally on the matrix units
E_{μν}: A_t(E_{μν}) = (e^{it(\bar\lambda_μ−λ_ν)}... compute on the diagonal E_j := E_{jj}:
U_t^*E_jU_t = |e^{itλ_j}|²E_j = e^{−2b_jt}E_j, hence A_t(E_j) = (e^{−2b_jt}−1)E_j and A_t^*A_t(E_j) =
(e^{−2b_jt}−1)²E_j. The J term permutes E_j with the unit of the reflected eigenvector and vanishes
on the J-symmetric average; on the relevant component the eigenvalue of L is

ℓ(b) = ∫_ℝ e^{−2|t|}(e^{−2bt}−1)² dt = ∫₀^∞ e^{−2t}(e^{2bt}−1)²dt + ∫₀^∞ e^{−2t}(e^{−2bt}−1)²dt.

First integral: ∫₀^∞ e^{−2t}(e^{4bt}−2e^{2bt}+1)dt = 1/(2−4b) − 2/(2−2b) + ½; second with b↦−b.
Sum: [1/(2−4b)+1/(2+4b)] − 2[1/(2−2b)+1/(2+2b)] + 1 = 1/(1−4b²) − 2/(1−b²) + 1. Taylor:
(1+4b²) − 2(1+b²) + 1 + O(b⁴) = 2b² + O(b⁴). Pole at b=½: divergence, consistent with 166.6(i). ∎

**Interpretation.** (a)+(c) give the complete picture of the wall in this theory: **the fixed point of
the Gram flow ALWAYS exists and is canonical — it is the Weil form W. RH is not the existence of the
critical point: it is its MEMBERSHIP in the cone of metrics (W > 0).** The RH-free flow finds it
(converges to the W-paired part of G₀), but if m ≥ 1 it finds it OUTSIDE the cone, and the
trajectory crosses ∂𝕄. (d) quantifies this: each off-line zero is crushed at rate 2b_j² — the same
quadratic scale b² as the DBN energy (Phase 28, Conj. A.15: Λ = max b_j²/2). **[BRIDGE 166-E,
honest]:** the coincidence of scale 2b_j² ↔ b_j²/2 is a structural echo (both are the first even
power allowed by the symmetry γ↦−γ), not a proved identity; the factor-4 discrepancy is not
explained. It remains as a datum for [WISH 166.C] (coupled flow).

---

## 5. The anti-circularity test: is the second variation Q?

### 5.1 [THEOREM 166.10 — the second variation is NOT the Weil form; the circularity is localized elsewhere]

**Statement.** (a) The Hessian of 𝔇₂ at ANY point G (in particular at the candidate critical point)
is the constant operator L = ∫e^{−2|t|}A_t^*A_t dt + A_J^*A_J ≥ 0: a positive semidefinite quadratic
form, RH-free, defined solely by the dynamics (U_t, J) and the weight. **It is not Q.** There is no
identification "second variation of 𝔇 = Weil form": the answer to the mandate's question 4 is NO.
(b) The Weil form appears in the theory in exactly three places, all distinct from the Hessian:
(1) as the universal fixed point of the flow (166.13(a): W ∈ ker L — the POSITION of the critical
point, not its curvature); (2) as a conserved charge (166.9: κ = n_−(W) frozen in 𝕄); (3) as the
scale of the critical value (166.6: 𝔇 ≥ φ(|b_j|)⟨Gv_j,v_j⟩, with b_j the spectral datum of Q). (c)
Consequently, the wall does NOT reappear as "rigidity of a fixed point" (positive curvature = Weil
positivity): the curvature is positive FOR FREE (L ≥ 0 is a square). It reappears as **membership in
the cone + conservation law**: RH ⟺ W ∈ 𝕄 (the universal fixed point falls inside the cone) ⟺ the
infimum 0 is attained (166.11(c)); and meanwhile κ is frozen for every interior deformation (166.9).

**Proof.** (a) 𝔇₂ is quadratic: 𝔇₂(G) = ½⟨LG,G⟩_{HS}; its Hessian is L at every point, and
⟨LM,M⟩ = ∫e^{−2|t|}‖A_t(M)‖² + ‖A_J(M)‖² ≥ 0 is a square (a sum of squares of linear maps). That
L ≠ "Q as a form over deformations" is seen in the content: ker L is described by commutation with
the dynamics (166.13(b)) and contains W; Q as a quadratic form on K has index κ; L as a form on H_h
has kernel = the paired commutant and NO negative index. Objects of different type, with different
signatures, on different spaces. (b) These are the cited theorems.
(c) Combination of 166.6(ii), 166.7, 166.9, 166.11(c), 166.13(a)(c). ∎

### 5.2 Relation with Phase 28's second variation — and why the same wall is not re-found in the same place

Phase 28 (Question D.15) asked about the second variation of Q in the transversal direction b_j: the
Hessian of an ENERGY of the function (E_log) with respect to the movement of the ZEROS — and found
that the arithmetic sector G_ζ is uncontrollable without RH (Wall A). Here the variable is different
(the metric, with the zeros fixed) and the b_j enter at FIRST order in the value of the functional
(φ(b) ~ 2b/e, 166.6) and at SECOND order in the rate of the flow (ℓ(b) ~ 2b², 166.13(d)) — not as a
Hessian that must be proved positive. The positivity that in Phase 28 was the problem (Hessian of E
at b=0) is here free (L ≥ 0); the problem is transferred entirely to MEMBERSHIP IN THE CONE of the
fixed point. The wall did not disappear: it changed logical type — from "proving an inequality" to
"proving that a canonical fixed point of an RH-free dynamics falls in a given convex cone." I am not
claiming this is more tractable; I am claiming it is a DIFFERENT statement with different tools
(convex geometry of the cone of metrics and index-jump theory at its boundary, instead of positivity
of forms).

### 5.3 [GAP 166.F — the missing tool, named]

What this theory leaves as the only way out within its own language: a **boundary index-jump
mechanism on ∂𝕄**. Within 𝕄, κ is frozen (166.9); the flow reaches ∂𝕄 (166.13(c)); ON the boundary
inertia can jump (the congruence ceases to be an isomorphism). The precise open question: *does
there exist a notion of "renormalized degenerate metric" (a blow-up of ∂𝕄, in the style of
moduli-space compactifications) in which the limit of the Gram flow G_∞ (degenerate on N) re-expands
into a genuine metric on a MODIFIED space, such that the re-expanded dynamics has strictly smaller
κ?* This is a question of geometric analysis of degenerations (not of positivity), structurally
parallel to crossing Λ=0 in DBN. I do not know of literature treating this for pairs (fixed Kreĭn
form, degenerating metric) [literature GAP: Langer's theory of definitizable operators (Langer 1982)
classifies spectra for ONE given Kreĭn metric; there is, as far as I know, no theory of limits of
families of fundamental symmetries degenerating with control of the index]. It is the natural
successor to this document.

---

## 6. Verdict

**VERDICT: B′ (between A and B, closer to B, with genuine type-A dividends).**

- **It is not C:** 𝕄 and 𝕄_Q are non-empty, convex/contractible, RH-free (166.2, 166.3).
- **It is not full A:** the central piece "∃G: 𝔇(G)=0 ⟺ RH" (166.7) is GAP 164.D formalized = RH
  rewritten, as the mandate warned could happen; I declare it without embellishment.
- **It is not B as anticipated:** the expected failure mode was "second variation of 𝔇 = Weil form =
  RH again". **That is FALSE** (166.10): the Hessian is L ≥ 0, RH-free, a square. The circularity is
  not in the curvature; it is in the membership-in-the-cone of the universal fixed point W and in the
  conservation law of κ. That is why Łojasiewicz/center-manifold are not the missing tools (166.8):
  there is no interior equilibrium to stabilize when m ≥ 1.
- **The non-RH-equivalent dividends (why B′ and not B):**
  1. **[THEOREM 166.9]** κ is an exact conservation law of every metric deformation (Sylvester's
     inertia): a new no-go — deforming the metric with the form fixed cannot reduce κ; it answers
     the director's question (the expulsion IS conservation).
  2. **[THEOREM 166.6]** an explicit lower bound 𝔇 ≥ φ(|b_j|)⟨Gv_j,v_j⟩ with
     φ(b)=2b(1−2b)^{(1−2b)/(2b)}, and the calibration of the weight e^{−|t|} by the critical strip
     (φ < ∞ ⟺ b < ½ = Hadamard–de la Vallée Poussin): the functional's geometry encodes the only
     zero-localization result humanity has, and uses it as an integrability condition.
  3. **[THEOREM 166.13]** the Gram flow is linear, its universal fixed point is W (it ALWAYS
     exists; RH = that it falls inside the cone), it expels every metric toward/through ∂𝕄,
     crushing exactly the off-line directions, with rate ℓ(b_j) = 2b_j² + O(b_j⁴) — a scale echo
     with Λ = max b_j²/2 (Phase 28 A.15), unexplained (factor of 4), noted as a datum.
  4. **[PROP 166.11] + [BRIDGE 166-DBN]** the structure "infimum 0, attainment ⟺ RH" places RH at
     the boundary of a variational problem over metrics, in exact formal duality with Rodgers–Tao
     (Λ ≥ 0: RH at the boundary of the function-deformation problem). Two dual deformations (form vs
     metric), one quantity (κ) that is dynamic in one and conserved in the other.
- **The named successor:** boundary index-jump theory on ∂𝕄 (blow-up of degenerate metrics,
  GAP 166.F) — and the possible coupled form+metric flow (WISH 166.C) that would put DBN and Gram
  into a single phase portrait.

**Where RH sits in this theory (one sentence):** not in the existence of the critical point (free:
W), not in its stability (free: L ≥ 0), but in the fact that **the universal critical point of the
metric dynamics belongs to the cone of metrics** — and while deforming inside the cone, the
obstruction κ is a conserved charge that no metric deformation can discharge; only the boundary
(degeneration of the space) or the other flow (DBN, which moves the form) can touch it.

---

## 7. Appendix: label table and RH-free audit

### 7.1 Labels

| Label | Statement | Status |
|---|---|---|
| [DEF 166.1] 𝕄, ∂𝕄, 𝕄_Q | cone of admissible Gram operators; degenerate ones; fundamental symmetries | defined |
| [PROP 166.2] structure of 𝕄 | non-empty, open convex cone, contractible, GL/U | **proved** (only H-W) |
| [PROP 166.3] structure of 𝕄_Q | ≅ ball of strict contractions ℂ^κ→K₊; non-empty without RH; κ invariant | **proved** (H-W, H-Π; Pontryagin/Bognár/Azizov–Iokhvidov) |
| [REMARK 166.4] Haar escape | free compatibility in the blind space; the cost is born in K | **established** |
| [DEF 166.5] 𝔇 | defects A_t, A_J; weight e^{−|t|} | defined |
| [PROP 166.5′] | 𝔇 convex, Lipschitz, 1-homog; J term free | **proved** (H-26 i,iii) |
| [THEOREM 166.6] lower bound | 𝔇 ≥ φ(\|b_j\|)⟨Gv_j,v_j⟩/‖v_j‖²; exact φ; strip↔weight calibration; no interior zeros | **proved** (H-26) |
| [THEOREM 166.7] zero of 𝔇 | ∃G∈𝕄: 𝔇=0 ⟺ m=0 (⟸ with uniformity GAP) | **proved**; **declared RH-rewritten (= GAP 164.D)** |
| [PROP 166.7′] Pontryagin–Stone | compatibility in 𝕄_Q = invariant fundamental decomposition ⟹ real spectrum | **proved** (H-26) |
| [COR 166.8] | m≥1 ⟹ no interior critical point; Łojasiewicz–Simon inapplicable | **proved** |
| [THEOREM 166.9] conservation | κ(G) = κ throughout 𝕄 (Sylvester); jump only on ∂𝕄 | **proved** (H-W, H-Π; without H-26, without RH) |
| [BRIDGE 166-DBN] | form/metric duality with De Bruijn–Newman; RH at the boundary in both | honest, translation via unproved Phase 26 bridge |
| [PROP 166.11] collapse | normalized inf = 0 without attainment if m≥1; minimizers crush N; attainment ⟺ RH | **proved under (H-26⁺)**, flagged |
| [CONSTR 166.12] Gram flow | Ġ = −LG, smooth substitute; complete theory in the finite model | defined; [GAP 166.D] HS in infinite dim |
| [THEOREM 166.13] dynamics | W ∈ ker L always; ker L paired λ↔λ̄; expulsion toward/through ∂𝕄; rate ℓ(b)=2b²+O(b⁴) | **proved in the model** (H-26 restricted) |
| [THEOREM 166.10] anti-circularity | Hessian = L ≥ 0 ≠ Q; circularity in cone-membership + conservation + value scale | **proved** |
| [BRIDGE 166-E] | echo 2b² ↔ Λ=b²/2 (A.15); factor of 4 unexplained | honest, not an identity |
| [GAP 166.A] | non-degeneracy/uniformity of the Weil Gram operator (radical, W ≥ ε) | declared |
| [GAP 166.B] | concentration of the index in N + uniformity in K₁ (H-26⁺) | declared |
| [WISH 166.C] | coupled flow (W_t, G_s) DBN+Gram | declared |
| [GAP 166.D] | HS finiteness of the smooth substitute in infinite dim | declared |
| [GAP 166.F] | index-jump theory on ∂𝕄 (blow-up of degenerate metrics) | declared; [literature GAP] no known theory of limits of degenerating fundamental symmetries |

### 7.2 RH-free audit, piece by piece

| Object | RH-free? |
|---|---|
| ⟨·,·⟩₀ (Haar/Lebesgue background) | YES (D164) |
| W (Weil form as a form) | YES as a form; its positivity is NOT used in any theorem |
| U_t, J | YES as operators (D164); their Q-unitarity is (H-26)(i) = Phase 26's V.1, declared hypothesis |
| v_j (off-line eigenvectors) | hypothesis (H-26)(ii) = Phase 26's V.2; vacuous if m=0 |
| 𝕄, 𝕄_Q, ∂𝕄 | YES (166.2, 166.3 use only H-W, H-Π) |
| 𝔇, 𝔇₂, L, the flow | YES: defined solely by (U_t, J, ⟨·,·⟩₀, weight) |
| κ(G) and its conservation | YES (166.9 uses neither H-26 nor RH) |
| The value inf 𝔇 and its attainment | ATTAINMENT is RH (declared, 166.7/166.11(c)); the rest of the geometry (bounds, rates, conservation) is RH-free |

---

**References (real).**
- L.S. Pontryagin, "Hermitian operators in spaces with indefinite metric", *Izv. Akad. Nauk SSSR,
  Ser. Mat.* **8** (1944) 243–280.
- I.S. Iokhvidov, M.G. Krein, "Spectral theory of operators in spaces with an indefinite metric I",
  *Trudy Moskov. Mat. Obshch.* **5** (1956) 367–432 (AMS Transl. (2) 13).
- J. Bognár, *Indefinite Inner Product Spaces*, Ergebnisse der Mathematik 78, Springer 1974 —
  fundamental symmetries (ch. IV–V), quotient by the radical (ch. I §11).
- T.Ya. Azizov, I.S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric*, Wiley 1989 —
  angle operators (ch. 1 §8), root subspaces of the non-real spectrum (ch. 2 §2), boundedness of
  π-unitaries.
- M.G. Krein, H. Langer, "Über die Q-Funktion eines π-hermiteschen Operators im Raume Π_κ", *Acta
  Sci. Math. (Szeged)* **34** (1973) 191–230.
- H. Langer, "Spectral functions of definitizable operators in Krein spaces", in *Functional
  Analysis (Dubrovnik 1981)*, Lecture Notes in Math. **948**, Springer 1982, pp. 1–46.
- M.H. Stone, "On one-parameter unitary groups in Hilbert space", *Ann. of Math.* **33** (1932)
  643–648; M. Reed, B. Simon, *Methods of Modern Mathematical Physics I*, Academic Press 1980,
  Thm VIII.7–VIII.8.
- N.G. de Bruijn, "The roots of trigonometric integrals", *Duke Math. J.* **17** (1950) 197–226 —
  monotonicity in t of the reality of the zeros (§13).
- C.M. Newman, "Fourier transforms with only real zeros", *Proc. Amer. Math. Soc.* **61** (1976)
  245–251 — existence of Λ and the conjecture Λ ≥ 0.
- B. Rodgers, T. Tao, "The de Bruijn–Newman constant is non-negative", *Forum Math. Pi* **8** (2020)
  e6 — Λ ≥ 0.
- S. Łojasiewicz, "Une propriété topologique des sous-ensembles analytiques réels", in *Les Équations
  aux Dérivées Partielles* (Paris 1962), Colloques Internationaux du CNRS **117** (1963) 87–89.
- L. Simon, "Asymptotics for a class of non-linear evolution equations, with applications to
  geometric problems", *Ann. of Math.* **118** (1983) 525–571.
- H. Brezis, *Opérateurs maximaux monotones et semi-groupes de contractions dans les espaces de
  Hilbert*, North-Holland Math. Studies 5, 1973 — subgradient flows of convex functionals.
- J. Hadamard, "Sur la distribution des zéros de la fonction ζ(s) et ses conséquences arithmétiques",
  *Bull. Soc. Math. France* **24** (1896) 199–220; Ch.-J. de la Vallée Poussin, "Recherches
  analytiques sur la théorie des nombres premiers", *Ann. Soc. Sci. Bruxelles* **20** (1896) 183–256
  — non-vanishing on Re s = 1 (⟹ b_j < ½ for every zero).
- A. Connes, "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function",
  *Selecta Math. (N.S.)* **5** (1999) 29–106 — the scale flow and the background space.
- [literature GAP]: I do not know of (i) a formulation of the common-metric problem for the two
  groups (J, U_t) as a variational problem over the space of fundamental symmetries, (ii) a theory of
  degeneration of families of fundamental symmetries with control of the index jump
  (GAP 166.F), nor (iii) the functional 𝔇 with a weight calibrated by the strip. The references
  anchor the tools (Pontryagin/Krein/Langer, Stone, DBN, Łojasiewicz–Simon); the metric deformation
  theory of this document is new.
