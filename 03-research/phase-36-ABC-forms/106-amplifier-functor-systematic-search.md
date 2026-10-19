# Doc 106 — The amplifier functor ⊠: systematic search

**Phase 36 — Forms A/B/C ·**
**Status: systematic search completed — axiomatization, inventory of five candidates, collapse analysis, verdict**

---

## 0. Executive summary

This document executes the program of Form B of paper P41 (Problem 7.2): systematically
search for an operation $\boxtimes$ on the Pontryagin space $(\mathcal{K},Q)$
of Weil–Connes — or on the category of CCM triples — that realizes the Deligne
skeleton: integer invariant, superadditive amplification, sublinear uniform bound.

**Main findings:**

1. **(§1) Axiomatization.** The Deligne mechanism reduces to an elementary
   theorem (Theorem 1.4, with complete proof): if $\kappa(\psi^{\boxtimes k}) \geq k\,\kappa(\psi)$
   and $\kappa(\psi^{\boxtimes k}) \leq f(k)$ with $f(k)/k \to 0$, then $\kappa(\psi)=0$.
   The difficulty is never in the abstract theorem: it is in exhibiting $(\mathcal{C},
   \boxtimes, \kappa, f)$ with both properties **non-circularly**.

2. **(§3.1) The central computation.** For hermitian forms of signatures $(p_1,q_1)$ and
   $(p_2,q_2)$:
   $$\mathrm{neg.ind}(Q_1 \otimes Q_2) = p_1 q_2 + q_1 p_2.$$
   Immediate consequence: the tensor product of Kreĭn spaces is **strictly
   superadditive** in the negative index whenever $(p_1-1)q_2 + (p_2-1)q_1 > 0$.
   **The falsifier declared in P41 ("κ is exactly additive under every available ⊠")
   is REFUTED**: there exists a natural product with strict superadditivity — in fact,
   exponential: on $\mathcal{K}_{\mathrm{off}}$ (signature $(2m,2m)$),
   $\kappa(\mathcal{K}_{\mathrm{off}}^{\otimes k}) = (4m)^k/2$.

3. **(§3.1–3.2) The infinite-dimensional problem and its double edge.** On the full
   space ($p = \infty$, $q = 2m$), $\mathrm{neg.ind}(Q\otimes Q) = \infty$ already at $k=2$:
   the tensor product destroys the Pontryagin structure and with it the Kreĭn–Langer
   theorem. The forced regularization (restriction to $\mathcal{K}_{\mathrm{off}}$,
   legitimate by Theorem 8.1 of Doc 96) saves (a) but reveals the real problem: **the
   superadditivity and the growth of the index of the abstract tensor are computed from
   the same signature data; there is no independent input**, so no contradiction at all
   can come out of the abstract tensor (Proposition 3.9, the "sterility lemma").

4. **(§3.2) The analytic object of the product.** The "zeros" of $\mathcal{K}_{\mathrm{off}}
   \otimes \mathcal{K}_{\mathrm{off}}$ are sums $z_1+z_2$ of spectral parameters, i.e.
   points $\rho_1+\rho_2-1/2$. **No known L-function has those zeros.** The
   Rankin–Selberg convolution, which is the natural analytic realizer of ⊗, is
   *group-theoretic* on GL(1): $\mathbf{1} \boxtimes \mathbf{1} = \mathbf{1}$, $L(s, \mathbf{1}
   \times \mathbf{1}) = \zeta(s)$ — it returns $\zeta$ without amplifying anything. Any
   operation that stays inside the class of L-functions multiplies L-functions, and
   multiplying L-functions **unions** zero sets (direct sum, κ exactly additive), it does
   not **sum** them (tensor). Structural dichotomy: §3.2.4.

5. **(§3.3) The Frobenius correspondences of the scaling site** satisfy
   $\Psi(\lambda)\circ\Psi(\lambda') = \Psi(\lambda\lambda')$ (with the tangential
   deformation $\mathrm{Id}_\varepsilon$ in the mixed rational/irrational case) — verified
   in Connes–Consani. They are a **multiplicative monoid of endomorphisms**, not a binary
   product on objects: on $(\mathcal{K},Q)$ they induce (modulo V.1) isometries, and
   isometries **preserve** κ exactly. They do not amplify. The only place where the
   structure of the scaling site offers a genuinely binary ⊠ is the **square of the
   site** — and that is exactly the unfinished Riemann–Roch program of Connes–Consani
   (MW-5).

6. **(§3.4) The multiplicative convolution** on test functions collapses to
   CAP positivity by the transmutation pattern: making $Q$ a positive functional
   on the algebra $(\mathcal{S},\star)$ is literally Weil positivity (MW-1).
   FAIL I2a.

7. **(§5) Where the weight remains.** For the only candidate with (a) proved
   (relative tensor on $\mathcal{K}_{\mathrm{off}}$), **all the weight falls on (b)**:
   a family $\{\psi^{\boxtimes k}\}$ is needed with a C5-type finiteness bound whose
   source is independent of the position of the zeros. The exact analogue of "the poles
   of the L-function of the family do not move" (Grothendieck rationality in Weil I) would be a
   **rationality/Riemann–Roch on the square of the scaling site**. That theorem does not
   exist; it is MW-5. The gap is named precisely (Missing Lemma 5.3).

**VERDICT: PARTIAL** (§6). The decisive sub-question of P41 has an affirmative answer
— yes, there exists a natural product with strict superadditivity of the negative index, and
the computation is unconditional — but the sublinear bound (b) is structurally inaccessible
for that product without leaving the class of L-functions, and the available analytic
realizations either are exactly additive (direct sum / multiplication of L-functions),
or collapse to CAP (convolution), or require the unfinished CC program
(square of the scaling site). What remains is a precise falsifiable statement (Problem 6.2).

---

## 1. Axiomatization: the abstract amplification theorem

### 1.1 What is exactly in Weil I

We recall the logical skeleton of Deligne's proof of RH over function fields
[Deligne, *La conjecture de Weil. I*, Publ. Math. IHÉS 43 (1974), 273–307], in the form
already distilled in P41 §7:

1. **Integer invariant.** For a Frobenius eigenvalue $\alpha$ of an $\ell$-adic sheaf
   of weight $w$ on a curve, the "weight defect" is $\delta = 2\log_q|\alpha| - w$.
   RH (for that sheaf) is $\delta = 0$. The crucial datum: $\delta$ lives in a controlled
   discrete set (in fact, the final argument forces it into an interval
   $[0, c/k]$ for every $k$, and the only possibility is $0$; the clean categorical
   version uses that the relevant invariant is an integer, or a real number trapped by integers).

2. **Amplification.** The (even) tensor power $\mathcal{F}^{\otimes 2k}$ has
   eigenvalue $\alpha^{2k}$: the defect multiplies, $\delta \mapsto 2k\,\delta$.

3. **Sublinear uniform bound.** Grothendieck's rationality of the L-function of the
   family, $L(U, \mathcal{F}^{\otimes 2k}, T) = \prod P_i(T)^{(-1)^{i+1}}$, together with the
   absolute convergence of the Euler product on a fixed half-plane and control of the
   poles (which come from $H^2_c$, whose weight is known **a priori** and **does not
   depend on $k$** beyond linearly with a uniform additive constant), gives
   $2k\,\delta \leq C$ with $C$ **independent of $k$** (or $\leq C(k)$ with $C(k)/k\to0$).
   The structural point: the bound comes from an input **independent** of the eigenvalue
   $\alpha$ — the geometry of the curve and the weight theory of the $H^i_c$, which "do not
   move" as $k$ varies.

4. **Conclusion.** $2k\,\delta \leq C$ for all $k \geq 1$ forces $\delta \leq C/2k \to 0$,
   hence $\delta = 0$.

None of the four steps is a CAP-type positivity: there is no quadratic form whose
non-negativity is equivalent to RH at any point of the argument. Step (3) is the non-trivial
core; (1), (2), (4) are structure.

### 1.2 The minimal categorical structure

**Definition 1.1 (Amplification datum).** An **amplification datum** is a quadruple
$(\mathcal{C}, \boxtimes, \kappa, \mathcal{F})$ where:

- $\mathcal{C}$ is a class of objects (a complete symmetric tensor category is not
  required; a class closed under the following operation suffices);
- $\boxtimes : \mathcal{C} \times \mathcal{C} \to \mathcal{C}$ is a binary operation
  (strict associativity is not required; it suffices that the powers $\psi^{\boxtimes k}$
  be coherently defined, e.g. by left iteration);
- $\kappa : \mathcal{C} \to \mathbb{N} \cup \{\infty\}$ is an invariant with
  non-negative integer values (or $+\infty$);
- $\mathcal{F} \subseteq \mathcal{C}$ is a subclass ("the bounded family").

**Definition 1.2 (Properties (a) and (b)).** The amplification datum satisfies:

- **(a) Superadditivity along powers** if for every $\psi \in \mathcal{C}$ and
  every $k \geq 1$:
  $$\kappa(\psi^{\boxtimes k}) \;\geq\; k\,\kappa(\psi).$$
  (Note: this is weaker than binary superadditivity
  $\kappa(\psi_1\boxtimes\psi_2) \geq \kappa(\psi_1)+\kappa(\psi_2)$, which implies it by
  induction. For the theorem the along-powers version suffices.)

- **(b) Sublinear uniform bound on $\mathcal{F}$** if there exists $f : \mathbb{N} \to
  [0,\infty)$ with $f(k)/k \to 0$ such that for every $\psi$ with $\psi^{\boxtimes k} \in
  \mathcal{F}$ for all $k$:
  $$\kappa(\psi^{\boxtimes k}) \;\leq\; f(k) \quad \text{for all } k \geq 1.$$

**Remark 1.3 (what is essential and what is not).** Not needed: unit, duality,
rigidity, braiding, not even functoriality of $\boxtimes$ on morphisms. What is needed
exactly: (i) that $\kappa$ take values in a set with the discrete Archimedean
property ($\mathbb{N}$, or any subset of $[0,\infty)$ with positive infimum on
its strictly positive part), (ii) inequality (a), (iii) inequality (b) with
**the same** $\boxtimes$-power on both sides. The classic trap is in (iii): if the
family $\mathcal{F}$ on which the bound is proved does not contain the powers of the
object of interest, the argument does not get off the ground.

### 1.3 The abstract theorem

**Theorem 1.4 (Abstract amplification).** Let $(\mathcal{C}, \boxtimes, \kappa,
\mathcal{F})$ be an amplification datum satisfying (a) and (b). Then for every
$\psi \in \mathcal{C}$ such that $\psi^{\boxtimes k} \in \mathcal{F}$ for all $k \geq 1$:
$$\kappa(\psi) = 0.$$

*Proof.* Let $\psi$ be such. By (a) and (b), for all $k \geq 1$:
$$k\,\kappa(\psi) \;\leq\; \kappa(\psi^{\boxtimes k}) \;\leq\; f(k),$$
hence $\kappa(\psi) \leq f(k)/k$ for all $k$. Taking $k \to \infty$ and using
$f(k)/k \to 0$: $\kappa(\psi) \leq 0$. Since $\kappa(\psi) \in \mathbb{N} \cup \{\infty\}$,
we conclude $\kappa(\psi) = 0$. $\square$

**Corollary 1.5 (RH instantiation).** If there exists an amplification datum with
$\mathcal{C} \ni \psi_\zeta$ (the object whose $\kappa$ is the negative index of the Weil
form, $\kappa(\psi_\zeta) = \kappa(Q) = 2m$ under Hypothesis D, by P35 and Doc 96
Theorem 8.1), with (a), (b), and $\psi_\zeta^{\boxtimes k} \in \mathcal{F}$ for all $k$,
then $2m = 0$, i.e. RH.

**Remark 1.6 (where circularity can hide).** Theorem 1.4 is elementary; all the
substance is in exhibiting the datum. The three possible escape points:

- **(C1)** $\kappa$ is not computable / the equality $\kappa(\psi_\zeta) = 2m$ already assumes
  conditional structure (in our case: Hypothesis D plus the V.1–V.4 program of P35 —
  assumed as the working framework throughout this document, as in P41).
- **(C2)** (a) is proved only using information about the zeros (circular).
- **(C3)** (b) is proved only assuming an RH-equivalent positivity for the family
  (the expected CAP collapse: see §4).

The program's discriminator (I2a: does there exist an independent unconditional input that
does the work?) must be applied separately to (a) and to (b) in each candidate. That is
the discipline of §3 and §4.

---

## 2. The object to amplify: structure of $(\mathcal{K}, Q)$ and of $\mathcal{K}_{\mathrm{off}}$

We fix the framework of P35 + Doc 96 + Doc 98, which is the framework of Form B:

- $(\mathcal{K}, Q)$: the Pontryagin space of Weil–Connes; $Q(f,g) =
  \mathcal{W}(f \star \tilde g)$ the Weil form; $H_C = -ix\partial_x$ the scaling
  operator, $Q$-symmetric modulo V.1.
- Under Hypothesis D with $m$ Klein orbits of off-critical zeros:
  $\kappa(Q) = \mathrm{neg.ind}(H_C) = 2m$ (P35, bridge conjecture, assumed as
  framework; the inequality $\leq$ is unconditional via Kreĭn–Langer).
- **Localization** (Doc 96, Theorem 8.1): $\mathcal{K} = \mathcal{K}_{\mathrm{crit}}
  \oplus_Q \mathcal{K}_{\mathrm{off}}$, with $Q|_{\mathcal{K}_{\mathrm{crit}}} \geq 0$ and
  $\mathrm{neg.ind}(Q|_{\mathcal{K}_{\mathrm{off}}}) = \kappa = 2m$.
- **Fine structure of $\mathcal{K}_{\mathrm{off}}$** (Doc 98, Proposition 6.1, case
  $m=1$, extended to $m$ quadruples by spectral orthogonality): each quadruple
  $\{1/2 \pm b_j \pm i\gamma_j\}$ generates a dimension-4 block with Gram matrix
  equal to **two hyperbolic planes**: signature $(2,2)$, $\kappa = 2$ per quadruple,
  independent of $b_j$. In total:
  $$\dim \mathcal{K}_{\mathrm{off}} = 4m, \qquad
    \mathrm{sig}(Q|_{\mathcal{K}_{\mathrm{off}}}) = (2m,\, 2m), \qquad
    \kappa = 2m.$$
- The positive part of the full space is infinite-dimensional:
  $\mathrm{sig}(Q) = (\infty,\, 2m)$ in the sense that $p = \dim\mathcal{K}_+ = \infty$,
  $q = \dim\mathcal{K}_- = 2m$.

The eigenvalues of $H_C$ on $\mathcal{K}_{\mathrm{off}}$ are $z_j^{(\pm\pm)} =
\pm b_j \pm i\gamma_j$ (parameter $z = \rho - 1/2$, four per quadruple, paired in
the two hyperbolic planes by $z \leftrightarrow \bar z$; convention of Doc 98,
Rem. 6.2).

This is the object $\psi_\zeta$ of Corollary 1.5. The question of this document:
which $\boxtimes$?

---

## 3. Inventory of candidates

### 3.1 Candidate 1: tensor product of Kreĭn spaces

#### 3.1.1 The signature computation

**Proposition 3.1 (signature of the tensor product of hermitian forms).** Let
$(V_1, Q_1)$ and $(V_2, Q_2)$ be finite-dimensional complex vector spaces with
non-degenerate hermitian forms of signatures $(p_1, q_1)$ and $(p_2, q_2)$. Then the
hermitian form $Q_1 \otimes Q_2$ on $V_1 \otimes V_2$, defined by
$(Q_1 \otimes Q_2)(u_1 \otimes u_2,\, v_1 \otimes v_2) = Q_1(u_1, v_1)\,Q_2(u_2, v_2)$
and sesquilinear extension, is non-degenerate of signature
$$\mathrm{sig}(Q_1 \otimes Q_2) = \bigl(\,p_1 p_2 + q_1 q_2,\;\; p_1 q_2 + q_1 p_2\,\bigr).$$
In particular:
$$\boxed{\;\mathrm{neg.ind}(Q_1 \otimes Q_2) \;=\; p_1 q_2 + q_1 p_2.\;}$$

*Proof.* Choose $Q_i$-orthonormal bases $\{e^{(i)}_a\}$ of $V_i$ with
$Q_i(e^{(i)}_a, e^{(i)}_a) = \varepsilon^{(i)}_a \in \{+1, -1\}$ (they exist by Sylvester's
inertia theorem, valid for complex hermitian forms). The basis
$\{e^{(1)}_a \otimes e^{(2)}_b\}$ of $V_1 \otimes V_2$ is
$(Q_1\otimes Q_2)$-orthogonal with
$$(Q_1 \otimes Q_2)(e^{(1)}_a \otimes e^{(2)}_b,\, e^{(1)}_a \otimes e^{(2)}_b)
  = \varepsilon^{(1)}_a\,\varepsilon^{(2)}_b.$$
The sign is $-1$ exactly when the signs of the factors differ. The number of
pairs $(a,b)$ with different signs is $p_1 q_2 + q_1 p_2$; with equal signs,
$p_1 p_2 + q_1 q_2$. Non-degeneracy is immediate (no basis vector is
isotropic and the basis is orthogonal). $\square$

**Corollary 3.2 (strict superadditivity).** With the above notation, writing
$\kappa_i = q_i$:
$$\mathrm{neg.ind}(Q_1 \otimes Q_2) - (\kappa_1 + \kappa_2)
  = p_1 q_2 + q_1 p_2 - q_1 - q_2
  = (p_1 - 1)\,q_2 + (p_2 - 1)\,q_1 \;\geq\; 0,$$
with **strict inequality** if and only if $(p_1-1)q_2 + (p_2-1)q_1 > 0$, i.e. as soon as
some factor has both a positive part of dimension $\geq 2$ and the other factor has
negative index $\geq 1$.

*Proof.* Direct computation from Proposition 3.1. $\square$

**This refutes the first half of the P41 falsifier**: it is not true that κ is
exactly additive under every available product. The Kreĭn tensor product is
strictly superadditive as soon as there is a surplus of positive directions — which is
exactly the situation of $(\mathcal{K}, Q)$, with $p = \infty$.

#### 3.1.2 Tensor powers: exact growth

**Proposition 3.3 (negative index of the tensor power).** For $(V, Q)$ of
signature $(p, q)$, the $k$-th power has
$$\mathrm{neg.ind}(Q^{\otimes k})
  = \sum_{j \,\mathrm{odd}} \binom{k}{j} p^{\,k-j} q^{\,j}
  = \frac{(p+q)^k - (p-q)^k}{2}.$$

*Proof.* In the product basis, the sign of a basis vector is the product of the
signs of its $k$ factors; it is negative when the number $j$ of negative factors is
odd. The closed form is obtained from $(p+q)^k = \sum_j \binom{k}{j} p^{k-j} q^j$ and
$(p-q)^k = \sum_j (-1)^j \binom{k}{j} p^{k-j} q^j$. $\square$

Two readings:

- **If $q = 0$**: $\mathrm{neg.ind}(Q^{\otimes k}) = 0$ for all $k$. Positivity is
  stable under ⊗ (consistency: under RH nothing is generated).
- **If $q \geq 1$ and $p \geq 1$**: the index grows like $\tfrac12(p+q)^k$ —
  **exponentially**, much more than the linear amplification $k\kappa$ required by (a).

#### 3.1.3 The infinite-dimensional problem

**Proposition 3.4 (collapse of the Pontryagin structure).** If $(\mathcal{K}, Q)$ has
$p = \dim \mathcal{K}_+ = \infty$ and $q = \kappa \geq 1$, then every reasonable
completion of $(\mathcal{K} \otimes \mathcal{K},\, Q \otimes Q)$ has infinite negative index.

*Proof.* Let $v_- \in \mathcal{K}_-$ with $Q(v_-, v_-) = -1$ and let
$\{e_n\}_{n\geq1} \subset \mathcal{K}_+$ be orthonormal ($Q(e_n,e_n)=+1$). The vectors
$\{e_n \otimes v_-\}_{n \geq 1}$ are mutually $Q\otimes Q$-orthogonal with
$(Q\otimes Q)(e_n \otimes v_-, e_n \otimes v_-) = -1$: an infinite-dimensional negative
subspace. $\square$

**Consequence.** $(\mathcal{K}^{\otimes 2}, Q^{\otimes 2})$ **is not a Pontryagin
space**: $\kappa = \infty$, the Kreĭn–Langer theorem does not apply, and the invariant
$\kappa$ stops being a useful integer already at the first power. Taken naively, Candidate 1
dies here — not for lack of superadditivity but from excess: the
amplification is so violent that it destroys the invariant.

**Regularization options:**

- **(R1) Relative index:** define $\kappa_{\mathrm{rel}}(Q^{\otimes 2}) :=
  \mathrm{neg.ind}(Q^{\otimes 2}) - \mathrm{neg.ind}(Q_{\mathrm{ref}}^{\otimes 2})$
  relative to a reference form $Q_{\mathrm{ref}} \geq 0$ (e.g. the Weil form of
  $\zeta_{\mathrm{on}}$, Doc 83). Problem: both terms are $\infty$; a Fredholm-type
  relative index theory for pairs of forms would be needed (finite-rank perturbation:
  $Q - Q_{\mathrm{ref}}$ has "rank" $4m$ in the sense of Doc 98). It is developable but,
  note, the result of any consistent definition will be the index of the finite-rank
  part — i.e. option (R2). **It is not an independent route.**
- **(R2) Restriction to $\mathcal{K}_{\mathrm{off}}$:** legitimate and invariantly
  defined by Theorem 8.1 of Doc 96 (the decomposition is spectral, not a
  choice). This is Candidate 2.

**Evaluation of Candidate 1: (a) ✅ strict (Corollary 3.2) — (b) ✗ catastrophically
false ($\kappa = \infty$ at $k=2$). Status: redirects to Candidate 2.**

### 3.2 Candidate 2: the relative tensor on $\mathcal{K}_{\mathrm{off}}$

#### 3.2.1 The computation

By §2, $\mathrm{sig}(Q|_{\mathcal{K}_{\mathrm{off}}}) = (2m, 2m)$ (sum of $2m$ hyperbolic
planes). By Proposition 3.3 with $p = q = 2m$:

**Proposition 3.5.** $\mathrm{neg.ind}\bigl((Q|_{\mathcal{K}_{\mathrm{off}}})^{\otimes k}\bigr)
= \tfrac{(4m)^k - 0^k}{2} = \tfrac{(4m)^k}{2}$ for $k \geq 1$.

Amplification (a) holds with exponential slack:
$\tfrac{(4m)^k}{2} \geq k \cdot 2m$ for all $k \geq 1$, $m \geq 1$. **Ingredient
(a) of the Deligne skeleton is available, unconditionally, as pure linear
algebra.** And if $m = 0$, all powers have index 0: the invariant exactly distinguishes
RH from ¬RH at every level $k$.

#### 3.2.2 The sterility lemma

Here is the document's most important conceptual point.

**Proposition 3.6 (sterility of the abstract tensor).** Let $\mathcal{C}_0$ be the class of
finite-dimensional hermitian spaces with $\boxtimes = \otimes$ and $\kappa =
\mathrm{neg.ind}$. Then **there exists no** function $f$ with $f(k)/k \to 0$ such that
(b) holds on a family $\mathcal{F}$ containing the powers of some object with
$\kappa \geq 1$. In other words: within $\mathcal{C}_0$, (a) and (b) are
**jointly unsatisfiable** except in the trivial case $\kappa = 0$.

*Proof.* By Proposition 3.3, if $\kappa(\psi) = q \geq 1$ (and $p \geq 0$),
then $\kappa(\psi^{\otimes k}) = \tfrac{(p+q)^k - (p-q)^k}{2} \geq
\tfrac{(q+p)^k - |p-q|^k}{2} \to \infty$ with exponential growth (if $p\geq1$) or
$\kappa(\psi^{\otimes k}) = q^k/2 \cdot [1-(-1)^k]$... in every case
$\limsup_k \kappa(\psi^{\otimes k})/k = \infty$ for $q \geq 1$, $p+q \geq 2$, and for
$p=0,q=1$ we have $\kappa(\psi^{\otimes k}) = \tfrac{1-(-1)^k}{2}$, which is bounded but
then (a) fails ($k\kappa = k \not\leq 1$). In no case do (a) and (b) coexist with
$\kappa \geq 1$. $\square$

**Remark 3.7 (structural reading).** Proposition 3.6 is not accidental bad news:
it is the precise manifestation of the fact that in the abstract tensor **both sides of
the inequality of Theorem 1.4 are computed from the same data** (the signature). There is
nowhere to draw a contradiction from, because there are not two sources of information
that could disagree. In Weil I, (a) is linear algebra (eigenvalues of tensor powers) but
(b) is **geometry** (rationality of the L-function of the family, weights of $H^2_c$): two
independent sources. The operational conclusion:

> **Candidate 2 can only work if the powers $\psi^{\boxtimes k}$ are
> re-embodied in analytic objects whose index finiteness has a source of its own
> (of type C5), independent of the signature computation.**

This transfers the whole problem to the question: what analytic object is
$\mathcal{K}_{\mathrm{off}} \otimes \mathcal{K}_{\mathrm{off}}$?

#### 3.2.3 The analytic object of the product: zeros that add up

The generators of $\mathcal{K}_{\mathrm{off}}$ are rigidly indexed by the
off-critical zeros (Doc 98, Rem. 6.3): $v_z$ with eigenvalue $z = \rho - 1/2$ of $H_C$.
On $\mathcal{K}_{\mathrm{off}} \otimes \mathcal{K}_{\mathrm{off}}$ the natural operator
is
$$H^{(2)} \;=\; H_C \otimes I + I \otimes H_C,$$
(the generator of the diagonal scaling flow $U_\lambda \otimes U_\lambda$), with
eigenvalues $z_1 + z_2$ on $v_{z_1} \otimes v_{z_2}$. In the $s$ parameter: the "zeros"
of the product object are
$$s = \rho_1 + \rho_2 - \tfrac12, \qquad \rho_1, \rho_2 \text{ zeros of } \zeta.$$

**Question 3.8.** What L-function has zeros at $\{\rho_1 + \rho_2 - 1/2\}$?

**Answer (negative, with three comparisons):**

1. **Rankin–Selberg on GL(1).** The RS convolution of Hecke characters is
   group-theoretic: $L(s, \chi_1 \times \chi_2) = L(s, \chi_1\chi_2)$. For the object $\zeta$
   ($\chi = \mathbf{1}$): $L(s, \mathbf{1} \times \mathbf{1}) = \zeta(s)$. The zeros of the
   RS of $\zeta$ with itself are **the zeros of $\zeta$**, not their sums. This is the
   group-theoretic triviality noted in P41 §7.3, now seen from the analytic side: RS is
   the analytic realizer of the tensor product of **automorphic representations**
   (Jacquet–Shalika, etc.), and on GL(1) that tensor is the product of characters — the
   "zero" layer does not tensorize, it stays put.

2. **$\zeta(s)^k$.** It has the zeros of $\zeta$ **with multiplicity $k$**: that is
   multiplicity amplification, not summing of parameters. On the $(\mathcal{K},Q)$ side
   it corresponds to the **direct sum** $\mathcal{K}_{\mathrm{off}}^{\oplus k}$
   ($\kappa \mapsto k\kappa$, exact additivity: Candidate 5). Important: $\zeta^k$ is
   indeed "real multiplicity amplification" in the sense of task (iii), with
   linear index growth — taken up again in §5.

3. **Sums of zeros in the literature.** The combinations $\rho_1 + \rho_2$ appear in
   the Hadamard products of $\Xi(t_1)\Xi(t_2)$ and in the study of
   $\zeta(s)\zeta(s+w)$ (shifted moments), but **no known L-function with Euler
   product** has zero divisor $\{\rho_1+\rho_2-1/2\}$. We do not assert a non-existence
   theorem (we do not have one); we record that the object is not in the Selberg class
   enlarged by any known construction.
   **[OPEN GAP 3.8: no known analytic realizer; nor is there a proof that
   none exists.]**

#### 3.2.4 The multiply/sum dichotomy

**Remark 3.9 (structural dichotomy).** Let $\boxtimes$ be any operation on
objects $\psi_L$ associated to L-functions such that the object $\psi_{L_1} \boxtimes
\psi_{L_2}$ is again the object of an L-function, say $L_3$, built by
procedures of the theory (products, quotients, RS, automorphic induction, base
change). Then the zero set of $L_3$ (with multiplicity) is a **union** of
zero sets of individual L-functions — never a **Minkowski sum** of the
spectral parameter sets. In the dictionary of $(\mathcal{K},Q)$: operations internal
to the class of L-functions realize direct sums (and their
sub/quotients), never the tensor $H_C \otimes I + I \otimes H_C$.

*Justification.* Every L-function of the class is an Euler product with a gamma
archimedean factor; its zero divisor comes from its own functional equation. The
constructions listed operate at the level of representations/Euler factors, and
the divisor of the result is the divisor of a function of **one** variable $s$; the
zeros of a product $\prod_i L_i^{n_i}$ are the union with multiplicity. The Minkowski
sum $\{\rho_1+\rho_2-1/2\}$ would require a bilinear operation at the level of
**divisors**, not of functions — an "additive product of spectra" that L-function
theory does not provide. $\square$ (structural, not a formal theorem: it
depends on the list of admitted constructions)

**Consequence.** Candidate 2 faces an exact bifurcation:

- Either $\boxtimes$ stays in the class of L-functions $\Rightarrow$ direct
  sum $\Rightarrow$ κ exactly additive $\Rightarrow$ the (a)-strict half of the P41
  falsifier is triggered (there is no strict superadditivity within the class);
- or $\boxtimes$ is the genuine tensor $\Rightarrow$ (a) strict and exponential,
  but the product object leaves the class of L-functions and **loses the only known
  mechanism for C5 finiteness** (Doc 94: C5 is formulated for the Weil form of an
  L-function via the prime tail of **its own** explicit formula; without an explicit
  formula, there is no C5).

**Evaluation of Candidate 2: (a) ✅ strict, exponential, unconditional — (b) total
OPEN GAP: with no analytic realizer there is no source for a bound. It is the most
promising candidate and its gap is named in §5.**

### 3.3 Candidate 3: Frobenius correspondences of the scaling site

#### 3.3.1 Verified facts

From the Connes–Consani corpus, verified against public sources
([The Arithmetic Site, arXiv:1405.4527](https://arxiv.org/pdf/1405.4527);
[CRAS 352 (2014) 971–975](https://alainconnes.org/wp-content/uploads/The-arithmetic-site-2014.pdf);
[The Scaling Site, arXiv:1507.05818](https://arxiv.org/pdf/1507.05818);
[Geometry of the scaling site, arXiv:1603.03191](https://arxiv.org/pdf/1603.03191);
[Connes, An essay on the Riemann Hypothesis, arXiv:1509.05576](https://arxiv.org/pdf/1509.05576)):

- The **arithmetic site** is $(\widehat{\mathbb{N}^\times},\, \mathbb{Z}_{\max})$ with
  $\mathbb{N}^\times$ acting by Frobenius endomorphisms on the semiring
  $\mathbb{Z}_{\max} = (\mathbb{Z}\cup\{-\infty\}, \max, +)$ of characteristic 1.
- The **scaling site** is obtained by extension of scalars to the tropical
  semifield $\mathbb{R}_{\max}^+$; its points over $\mathbb{R}_{\max}^+$ give the
  quotient $[0,\infty) \rtimes \mathbb{R}_+^*$ related to the idele class space.
- The **Frobenius correspondences** $\Psi(\lambda)$, $\lambda \in \mathbb{R}_+^*$,
  are constructed for rational $\lambda = n/m$ by composing with $Fr_{n,m}$, and for
  irrational $\lambda$ by Diophantine approximation (curves in the square of the site).
- **Composition law** (verified): $\Psi(\lambda) \circ \Psi(\lambda') =
  \Psi(\lambda\lambda')$ when $\lambda\lambda' \notin \mathbb{Q}$, and also when
  both are rational; in the mixed case ($\lambda, \lambda' \notin \mathbb{Q}$,
  $\lambda\lambda' \in \mathbb{Q}$) the **tangential deformation** appears:
  $\Psi(\lambda) \circ \Psi(\lambda') = \Psi(\lambda\lambda') \circ \mathrm{Id}_\varepsilon$,
  where $\mathrm{Id}_\varepsilon$ is the tangential deformation of the identity.
- The **λ-ring** structure of the semiring of correspondences, and the analogy with
  Frobenius in characteristic $p$, is the stated motivation for the CC Riemann–Roch
  strategy. The details of the λ-ring structure beyond the composition law
  above: **[NOT VERIFIED in detail; not used further below].**

#### 3.3.2 Action on $(\mathcal{K}, Q)$ and the index

The bridge with our framework: the scaling action $U_\lambda$ on $L^2(C_\mathbb{Q})$
**is** the Hilbertian shadow of Frobenius $\Psi(\lambda)$ (it is the action of
$\mathbb{R}_+^*$ whose generator is $H_C$; P35 §3).

**Proposition 3.10 (Frobenius operators do not amplify κ).** Suppose V.1 (scale
invariance of the Weil form: $Q(U_\lambda f, U_\lambda g) = Q(f,g)$; Goal V.1 of P35,
open). Then each $U_\lambda$ is a $Q$-isometry of $(\mathcal{K},Q)$, and for
every subspace $V \subseteq \mathcal{K}$:
$$\mathrm{neg.ind}(Q|_{U_\lambda V}) = \mathrm{neg.ind}(Q|_V).$$
In particular $\kappa(U_\lambda \psi) = \kappa(\psi)$: the Frobenius correspondences
induce on $(\mathcal{K},Q)$ **isometries**, which preserve the negative index
exactly. There is no $\mu$ with non-trivial behavior on κ.

*Proof.* A bijective linear isometry carries negative subspaces into
negative subspaces of the same dimension, in both directions. $\square$

**Remark 3.11 (why this was expected, and what remains).** The $\Psi(\lambda)$ form a
**one-parameter monoid of endomorphisms**: they are the analogue of the Frobenius
$\mathrm{Fr}^k$, not of the tensor product $\mathcal{F}^{\otimes k}$. In Weil I the
Frobenius does not amplify the defect either: it *measures* it. The one that amplifies is ⊗.
Conflating the two roles would be a type error. What the correspondences do offer is the
structure on which a binary ⊠ could be defined geometrically: the **square
of the site** (arithmetic or scaling), where the $\Psi(\lambda)$ live as
correspondences (subobjects of the square) and where CC develop Newton polygons
with their two operations (convex hull of the union = tropical sum; Minkowski
sum = tropical product). Note the exact echo of the dichotomy of Remark
3.9: **union vs. Minkowski sum** — the tropical geometry of the square of the site is
the only place in the verified corpus where the operation "Minkowski sum of divisors"
exists as a native structure. If the genuine tensor of Candidate 2 has a
geometric realizer, it is here. But the cohomological apparatus (Riemann–Roch on
the square, divisor theory with indices and the expected formula type $\dim H^0 - \dim H^1 =
\deg + \ldots$) is exactly the unfinished CC program = **MW-5**.

**Evaluation of Candidate 3: as an operation on $(\mathcal{K},Q)$: (a) ✗ (isometries,
κ exactly invariant — not even additive: it is not a binary operation). As a
provider of geometry for Candidate 2: the only live structural lead, blocked
by MW-5.**

### 3.4 Candidate 4: multiplicative convolution on the idele class group

The natural operation on the test-function side: $(f_1 \star f_2)(x) =
\int_0^\infty f_1(y) f_2(x/y)\, dy/y$ (and its adelic version on $C_\mathbb{Q}$). It makes
$\mathcal{S}$ a commutative algebra with involution $f \mapsto \tilde f$, and the
Weil form is the functional $\tau = \mathcal{W}$ evaluated on the algebra:
$Q(f,g) = \tau(f \star \tilde g)$.

**Proposition 3.12 (what ⋆ does to the form).** On the Mellin side,
$\widehat{f_1 \star f_2}(s) = \hat f_1(s)\,\hat f_2(s)$. Therefore:
$$Q(f_1 \star f_2,\, f_1 \star f_2) = \mathcal{Z}[f_1\star f_2] - \mathcal{P}[\cdot] +
\mathcal{A}[\cdot], \qquad
\mathcal{Z}[f_1 \star f_2] = \sum_\rho |\hat f_1(\rho)|^2\,|\hat f_2(\rho)|^2.$$
The zeros that weigh in are **the same zeros of $\zeta$**, reweighted
multiplicatively. There is no amplification of zeros or multiplicities: the operation
is internal to the object $\zeta$, diagonal on the spectrum.

**Proposition 3.13 (relation to κ: null as an amplifier, exact as a module).** For
fixed $h$ with $\hat h(\rho_j) \neq 0$ at the $4m$ off-critical zeros, the map
$f \mapsto f \star h$ preserves $\mathcal{K}_{\mathrm{off}}$ (it scales the residues $v_z$
by $\hat h(1/2+z)$) and the hyperbolic blocks of Doc 98 go to hyperbolic blocks
($q_j \mapsto q_j\, \hat h(1/2+z_j)\overline{\hat h(1/2+\bar z_j)}$, non-vanishing
off-diagonal entries): $\kappa$ **does not change**. If $\hat h$ vanishes at some
off-critical zero, κ can only **go down** (never up). In no case is there superadditivity:
$\star$ does not combine the indices of two arguments — the index of the product is
bounded by that of each factor.

*Proof.* Direct computation on the generators $v_z$ ($\widehat{f\star h} =
\hat f \hat h$ multiplies the residual functional at $z$ by the scalar
$\hat h(1/2+z)$); a block $\bigl(\begin{smallmatrix}0&q\\\bar q&0\end{smallmatrix}\bigr)$
with $q \neq 0$ has signature $(1,1)$ for every $q \neq 0$, and signature $(0,0)$
(degenerate) if $q = 0$. $\square$

**Application of the discriminator.** What statement would have to be proved to extract RH from
$\star$? The only one available: "$\tau$ is a positive functional on the involutive
algebra $(\mathcal{S}, \star, \tilde{\ })$", i.e. $\tau(f \star \tilde f) \geq 0$
for every $f$. That **is** Weil positivity, character by character: MW-1. The
transmutation pattern of Doc 99 applies in its pure form: the new algebraic
structure (the convolution algebra, GNS states, C*-completions) does not weaken the
statement; it reformulates it. The structural hypothesis that would make the candidate work
is CAP in disguise. **FAIL I2a.**

**Evaluation of Candidate 4: (a) ✗ (submultiplicative in κ, not superadditive) — and the
only possible use collapses to CAP. CLOSED.**

### 3.5 Candidate 5: direct sum (baseline for comparison)

$(\mathcal{K}_1 \oplus \mathcal{K}_2,\, Q_1 \oplus Q_2)$:
$\mathrm{neg.ind}(Q_1 \oplus Q_2) = q_1 + q_2$, exactly additive. Analytic
realizer: $L_1 \cdot L_2$ (product of L-functions; for $\psi_\zeta^{\oplus k}$:
$\zeta^k$, zeros with multiplicity $k$). Here (a) holds with equality —
$\kappa(\psi^{\oplus k}) = k\kappa(\psi)$, the "real multiplicity amplification" of
task (iii) — and hence **all the weight falls on (b)**: is there a provable
sublinear bound $\kappa(\psi_{\zeta^k}) \leq f(k)$? But $\kappa(\psi_{\zeta^k}) =
k \cdot 2m$ is computed trivially from $\psi_\zeta$: the "family" $\{\zeta^k\}$ contains no
new information — its zeros are those of $\zeta$. A sublinear bound for the
family **is** $m = 0$, i.e. RH. Circular by content (the same sterility
phenomenon of Proposition 3.6: a single data source).

**Evaluation of Candidate 5: (a) with equality (not strict), (b) RH-equivalent. It is the
yardstick: any candidate whose analysis reduces it to a direct sum is closed.**

---

## 4. Collapse risk: transmutation and discriminator, candidate by candidate

We apply the Doc 99 pattern (circularity is not eliminated: it is transmuted and
reappears under its wall name) and the I2a discriminator (FAIL = the structural
hypothesis is CAP positivity in disguise).

| Candidate | (a) superadditivity | (b) sublinear bound | Where does the wall reappear? | I2a |
|---|---|---|---|---|
| 1. Full Kreĭn ⊗ | ✅ strict (Cor. 3.2) | ✗ false ($\kappa=\infty$, Prop. 3.4) | infinite dimension destroys Π_κ (echo of MW-3) | passes (unconditional linear algebra) but the datum dies |
| 2. Relative ⊗ on $\mathcal{K}_{\mathrm{off}}$ | ✅ exponential (Prop. 3.5) | GAP: no analytic realizer, no C5 source | MW-5 (square of the site) or MW-7 (without its own explicit formula, finiteness would require knowing the zeros) | (a) passes I2a; (b) no candidate input |
| 3. Frobenius $\Psi(\lambda)$ | ✗ (isometries, Prop. 3.10) | n/a | Frobenius's role is to measure, not amplify | n/a |
| 4. convolution ⋆ | ✗ (Prop. 3.13) | n/a | direct MW-1: positivity of the functional τ = Weil | **FAIL I2a** |
| 5. direct sum | exact equality | RH-equivalent | sterility: a single data source | FAIL (circular by content) |

**The expected collapse, documented precisely (task iv).** The suspicion stated in
the task was: "if the sublinear bound (b) turns out to be equivalent to a generalized Weil
positivity (GRH for the Rankin–Selberg family), document it". The analysis shows
something finer:

1. For the genuine RS family there is nothing to document **because the RS family of
   $\zeta$ is $\zeta$ itself** (group-theoretic triviality of GL(1), §3.2.3.1). The collapse
   "(b) = GRH of the RS family" cannot even be formulated: the family does not exist
   as a distinct object. This is the specific death mode for GL(1), distinct from the
   CAP collapse: not circularity, but **vacuity**.
2. For the genuine tensor (Candidate 2), (b) is not equivalent to a known
   positivity: it is **inexpressible** with current tools, because the object
   $\psi^{\boxtimes k}$ has no explicit formula of its own. If someday it has one (via the
   square of the scaling site), that formula will have to be run through the
   discriminator: the concrete risk is that the "rationality" proved will contain, hidden in its
   poles, the position of the zeros of $\zeta$ (MW-7 re-encoding).
3. For the convolution (Candidate 4) the collapse is pure and simple CAP, already documented.

Comparison with the only non-CAP mechanism in the corpus (Doc 102, Bagchi amplifier):
Bagchi amplifies by **ergodic recurrence** (one off-critical zero → $\gg T$ zeros) and
runs into $N(\sigma,T) = o(T)$, which is an unconditional ceiling with an independent
source (Carlson/Ingham). Its premise (SR) is RH-equivalent: FAIL I2b. Candidate 2 has
the mirror-image structure: its "premise" (a) is unconditional (better than Bagchi!), but its
**ceiling** (b) does not exist yet. Bagchi has a ceiling without a premise; the relative tensor
has a premise without a ceiling. This exact complementarity is the central
comparative result of the document.

---

## 5. The most promising candidate: specifying the gap

The survivor is **Candidate 2** (relative tensor on
$\mathcal{K}_{\mathrm{off}}$), eventually realized geometrically via the square
of the scaling site (Candidate 3 as infrastructure). We specify what would have to be
proved, with the weight already distributed by the preceding analysis.

### 5.1 What is already proved (side (a))

**Theorem 5.1 (summary of (a); unconditional modulo the P35/Doc 96/Doc 98 framework).**
Under Hypothesis D with $m \geq 1$ orbits, let $\psi = (\mathcal{K}_{\mathrm{off}},
Q|_{\mathcal{K}_{\mathrm{off}}})$, of signature $(2m, 2m)$. With $\boxtimes = \otimes$ of
hermitian spaces:
$$\kappa(\psi^{\boxtimes k}) = \frac{(4m)^k}{2} \;\geq\; k \cdot 2m = k\,\kappa(\psi)
  \quad (k \geq 1),$$
with equality only at $k=1$. Superadditivity is strict for $k \geq 2$ and the
amplification is exponential. Moreover $m = 0 \Rightarrow \kappa(\psi^{\boxtimes k}) = 0\;
\forall k$: the power invariant detects RH at every level.

There is nothing to prove here: it is Proposition 3.5. (a) **is not the gap.**

### 5.2 The exact gap (side (b))

**Missing Lemma 5.2 (analytic realization of the square).** *Construct an
analytic-geometric object $X_2$ (natural candidate: a "collapsed two-variable
L-function"-type structure, or a divisor on the square of the scaling site with its
tropical Minkowski sum) such that:*

1. *its own "explicit formula" expresses a functional $\mathcal{W}_2$ whose associated
   quadratic form $Q_2$ contains $(Q|_{\mathcal{K}_{\mathrm{off}}})^{\otimes 2}$
   as a spectral block (the eigenvalues $z_1 + z_2$ of
   $H_C \otimes I + I \otimes H_C$);*
2. *$\mathcal{W}_2$ has a computable "geometric/arithmetic" side without knowing the
   positions of the zeros of $\zeta$ (the analogue of the prime side of the
   Weil explicit formula).*

**Missing Lemma 5.3 (C5 finiteness for the family).** *Prove for the family
$\{X_k\}_{k\geq1}$ (powers) a C5-type bound (Doc 94): the negative index of
$Q_k$ is bounded by the contribution of a finite "head" controlled
uniformly in $k$,*
$$\kappa(Q_k) \;\leq\; f(k), \qquad f(k)/k \to 0,$$
*where $f$ comes from data that "do not move with $k$" — the exact analogue of "the
poles of the L-function of the family do not move" from Weil I. Candidate source: a
Riemann–Roch-type formula on the square of the scaling site, where $f(k)$ would be an
Euler characteristic (dimension of a tropical $H^0$ minus a tropical $H^1$) whose
growth in $k$ is geometrically budgeted, not spectral.*

**Why all the weight falls on 5.3 and not on 5.2+a.** If the zeros of the product
object included those of $\zeta$ with multiplicity $k$ (the $\zeta^k$ = direct
sum case), the index grows linearly and sublinear (b) is RH (§3.5): circular. The only
non-circular configuration is that of the genuine tensor, where (a) gives
**exponential** growth $\;(4m)^k/2$; then (b) does not even need to be sublinear — it would
suffice to have $f(k) = o((4m)^k)$ *for some fixed $m\geq1$*… but since $m$ is unknown, the
robust form of the contradiction remains the sublinear one against $k\kappa$: any
$f(k)/k \to 0$ kills all $m \geq 1$ at once via $k\cdot 2m \leq \kappa(\psi^{\boxtimes k})
\leq f(k)$... **caution**: this chain uses (a) in the form $k\kappa \leq
\kappa(\psi^{\boxtimes k})$ and (b) on the same object. If $X_k$ realizes the tensor,
then under ¬RH its index IS $(4m)^k/2$ (Theorem 5.1), so (b) with any
subexponential $f$ already gives the contradiction. That is: **the strength of (a) cheapens (b)**
— sublinear is not needed, subexponential suffices — but in exchange (b) must be proved for
an object whose existence (Lemma 5.2) is itself the problem. The total budget of
difficulty does not go down; it concentrates.

**Comparison with Deligne's rationality (task iii, direct answer).** In Weil I
the analogue of 5.2 is free (the category of $\ell$-adic sheaves has an internal ⊗ and
every tensor power is again a sheaf on the same curve), and 5.3 is
Grothendieck's rationality plus the known purity of $H^0, H^2_c$: "the poles do not
move" means that the poles of $L(U, \mathcal{F}^{\otimes 2k}, T)$ are at
$|T| = q^{-1-kw}$ exactly (coinvariants of known weight), with uniform additive
error in $k$. The machinery that guarantees this is **cohomological finiteness** (the
$H^i_c$ are finite-dimensional with budgeted weights). The analogue conjectured here:
tropical cohomological finiteness on the square of the scaling site. CC proved
Riemann–Roch on the curve (the scaling site itself, in its versions for divisors
on $\mathbb{R}_{\max}$-modules); **the square is open** and is the precise
formulation of MW-5 in this context. It is not a coincidence: Weil's proof for curves
uses intersection on the surface $C \times C$; CC explicitly state that their strategy
seeks the analogue of $C \times C$ — the square of the site — and the Hodge-index-type
positivity there. Form B lands on the same square, but asking for another
thing: not positivity (Hodge index = direct CAP risk), but **finiteness + rationality**
(index budgeting). This distinction is the document's specific contribution:

> **Within the square of the scaling site there are two possible theorems: the
> positivity one (Hodge index, the declared CC route, direct CAP risk) and the
> finiteness one (Euler characteristic bounding the negative index of the tensor
> power, the Form B route). The second is not a positivity: it is a count. If
> the cohomological apparatus of the square comes to exist, Form B offers an
> alternative non-CAP consumer of the same apparatus.**

### 5.3 Falsifiable statement

**Problem 5.4 (the decisive experiment, finite and frank).** Take the toy model of
Doc 98 ($m = 1$, one quadruple, $\mathcal{K}_{\mathrm{off}}$ of dimension 4,
signature $(2,2)$). Explicitly construct the space
$\mathcal{K}_{\mathrm{off}}^{\otimes 2}$ (dimension 16, negative index 8 by
Proposition 3.5) and ask: does there exist a functional $\mathcal{W}_2$ on test
functions of **two** variables $(x_1, x_2) \in (\mathbb{R}_+^*)^2$, built from
arithmetic data of $\zeta$ (primes, pole, gamma factor — without positions of zeros), whose
diagonal restriction reproduces the 8 negative blocks? The Weil explicit formula in
two variables applied to $h(x_1, x_2) = f_1(x_1) f_2(x_2)$ factorizes
($\mathcal{W} \otimes \mathcal{W}$), and the zero term is
$\sum_{\rho_1, \rho_2} \hat f_1(\rho_1) \hat f_2(\rho_2) \cdot (\ldots)$ — the pairs
$(\rho_1, \rho_2)$ appear, and the sum $\rho_1 + \rho_2$ appears if the diagonal
kernel $h(x_1, x_2) = g(x_1 x_2)$ is inserted (the Minkowski sum of spectra is
the restriction to the product $x_1 x_2$!): indeed, $\int g(x_1 x_2) x_1^{\rho_1-1}
x_2^{\rho_2-1} dx_1 dx_2 = \hat g(\rho_1 + \rho_2 - 1) \cdot B(\ldots)$ after the change
$u = x_1 x_2$. **This one-page computation — which bilinear functional results from the
double Weil formula restricted to the diagonal multiplicative kernel, and whether its
prime side is autonomous (sums $\log p_1 + \log p_2 = \log p_1p_2$: the prime side of
the product lives on the integers $p_1 p_2$, not on primes!)** — is the first test of
Lemma 5.2 and is executable with the program's tools. If the "arithmetic" side of
the diagonal functional turns out expressible on the semigroups $\{p_1 p_2\}$ (almost-prime
numbers) with computable coefficients, Lemma 5.2 has a candidate; if the
arithmetic side requires the positions of the zeros to close, MW-7 reappears and the
candidate 2 dies at the same wall as all the others.

---

## 6. Verdict

**VERDICT: PARTIAL.**

**Precise reason.** The decisive question of P41 ("does ANY natural product on
$(\mathcal{K},Q)$ make the negative index strictly superadditive?") has the answer
**YES, unconditional and with a closed computation**: the Kreĭn tensor product, with
$\mathrm{neg.ind}(Q_1 \otimes Q_2) = p_1q_2 + q_1p_2$ (Proposition 3.1), strictly
superadditive as soon as $(p_1-1)q_2 + (p_2-1)q_1 > 0$, and on
$\mathcal{K}_{\mathrm{off}}$ (signature $(2m,2m)$) with exponential growth
$\kappa(\psi^{\otimes k}) = (4m)^k/2$. The first half of the P41 falsifier is
refuted: κ is NOT exactly additive under every available ⊠. Form B does **not die from
(a)**.

But the route does not remain ALIVE without qualification, for three equally
precise facts:

1. **Sterility of the abstract tensor** (Proposition 3.6): (a) and (b) of the pure
   tensor are computed from the same signature data; no amplification datum entirely
   internal to linear algebra can produce a contradiction. A second
   source — analytic or geometric — is needed for (b).
2. **Multiply/sum dichotomy** (Remark 3.9): every operation that stays in the
   class of L-functions realizes the direct sum (κ exactly additive, with no
   extractable contradiction: the second half of the falsifier, which does hold *within the
   class*); the genuine tensor (zeros $\rho_1+\rho_2-1/2$) leaves the class, and with it
   loses the explicit formula and the C5 mechanism. The group-theoretic triviality of GL(1)
   reappears on the analytic side as the **vacuity of the Rankin–Selberg family of
   $\zeta$** ($\mathbf{1}\boxtimes\mathbf{1}=\mathbf{1}$): the expected collapse "(b) = GRH of the
   RS family" cannot even be formulated.
3. **The only conceivable geometric realizer of the genuine tensor is the square of the
   scaling site** (tropical Minkowski sum of divisors; Frobenius correspondences as
   infrastructure, which on $(\mathcal{K},Q)$ are isometries and do not
   amplify — Proposition 3.10), and the cohomological apparatus of the square is MW-5:
   unfinished, not refuted.

**The falsifiable statement that remains** (Problem 5.4): the Weil formula in two
variables restricted to the diagonal multiplicative kernel $h(x_1,x_2) = g(x_1x_2)$ produces
the sum spectrum $\{\rho_1+\rho_2-1\}$ on the zero side; is its arithmetic side (supported
on products $p_1p_2$, i.e. almost-primes) **autonomous** — computable without
positions of zeros — or does it re-encode MW-7? A finite, executable computation, with two
clean outcomes: a concrete candidate for Missing Lemma 5.2, or the death of Candidate 2 at the same
wall as the others. Until that computation is done, Form B is **PARTIAL: alive in
(a) with a theorem, open in (b) with a named gap (Lemmas 5.2–5.3) and a decisive finite
test (Problem 5.4)**.

---

## References

**Internal (backward-only):** P35 (bridge theorem $\kappa(Q)=\mathrm{neg.ind}(H_C)$,
Hypothesis D, program V.1–V.4); P39 (trace criterion); P41 §7 (Form B, Problem 7.2,
falsifier); Doc 83 (quadruple factor, $d\nu \geq 0$); Doc 91 (Pontryagin space
of Weil–Connes, Kreĭn–Langer); Doc 94 (condition C5, Azizov–Iokhvidov perturbation,
finiteness→nullity gap, Conjecture $\mathbf{C}_B$); Doc 96 (Theorem 8.1: localization of
the index in $\mathcal{K}_{\mathrm{off}}$; obstacle $\mathbf{O}_D$); Doc 98 (Proposition
6.1: two hyperbolic planes per quadruple, $\kappa=2$, dim 4); Doc 99 (transmutation
pattern; discriminator I2a; CF rigidity); Doc 102 (Bagchi amplifier, the only
non-CAP mechanism in the corpus, FAIL I2b); meta-docs/DISCRIMINATOR-hardening-phase-A.md
(criteria I1–I4).

**Verified literature:**
- P. Deligne, *La conjecture de Weil. I*, Publ. Math. IHÉS **43** (1974), 273–307.
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm.
  Sém. Math. Univ. Lund (1952).
- T. Ya. Azizov, I. S. Iokhvidov, *Linear Operators in Spaces with an Indefinite
  Metric*, Wiley, 1989 (inertia and perturbation theorem in Pontryagin spaces).
- A. Connes, C. Consani, [*The Arithmetic Site*, arXiv:1405.4527](https://arxiv.org/pdf/1405.4527)
  and [CRAS 352 (2014) 971–975](https://alainconnes.org/wp-content/uploads/The-arithmetic-site-2014.pdf)
  (arithmetic site, $\mathbb{Z}_{\max}$, Frobenius $\mathbb{N}^\times$; composition
  law $\Psi(\lambda)\circ\Psi(\lambda')=\Psi(\lambda\lambda')$ with tangential
  deformation $\mathrm{Id}_\varepsilon$ in the mixed case — verified).
- A. Connes, C. Consani, [*The Scaling Site*, arXiv:1507.05818](https://arxiv.org/pdf/1507.05818);
  [*Geometry of the scaling site*, arXiv:1603.03191](https://arxiv.org/pdf/1603.03191)
  (tropical extension $\mathbb{R}_{\max}^+$, $[0,\infty)\rtimes$ structure,
  Riemann–Roch on the tropical curve — verified at the level of general statements).
- A. Connes, [*An essay on the Riemann Hypothesis*, arXiv:1509.05576](https://arxiv.org/pdf/1509.05576)
  (Riemann–Roch strategy, role of the square of the site).
- H. Jacquet, J. Shalika, on Rankin–Selberg for $\mathrm{GL}(n)$ — cited only for
  the standard fact $L(s, \chi_1 \times \chi_2) = L(s, \chi_1\chi_2)$ on GL(1)
  [standard; any RS reference contains it].
- Fine λ-ring structure of the semiring of CC correspondences beyond the
  composition law: **[NOT VERIFIED; not used in any argument]**.

*End of Doc 106.*
