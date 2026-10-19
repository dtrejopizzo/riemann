# Doc 52 — Formalization of Direction III: The Concrete Category $\mathcal{MM}$ and the Deninger Program

**Program:** CCM Zeta Spectral Triples — Phase 29/32  
**Prerequisites:** Docs 42–51, especially Doc 49  
**Nature:** Formalization of the geometry — from analogy to concrete object. No empty conjectures: only the mathematical structure that can be built today and the exact boundary of what requires new work.  
**Objective:** Build the category $\mathcal{MM}$ of Motivic Measures as a concrete additive category with cohomology. Connect with the Deninger Program (the most relevant one in the literature). Define the arithmetic Frobenius as an endofunctor. Identify precisely what is missing for the CPC to become a theorem.

---

## 1. Diagnosis of the Doc 49 gap

Doc 49 used the analogy with Weil to motivate a cohomology and a Frobenius, but:
1. The trace $\mathrm{Tr}(\phi_\zeta|H^1) = \sum(\sigma_0-1/2)$ was not defined in any existing theory.
2. The "scheme $\mathcal{V}_\zeta$" had no concrete algebraic structure.
3. The CPC was an analogy, not a conjecture formulated within an existing theory.

This document builds the concrete objects possible today.

---

## 2. The Deninger Program: what exists in the literature

The most relevant program in the literature is that of Christopher Deninger (1991–present).

**Theorem 2.1 (Deninger, 1991).** There is a conjectural cohomological formalism in which:

1. There exists a space $X$ ("the Deninger space") with an action of $\mathbb{R}$ via a flow $\Phi^t: X\to X$.
2. The zeros of $\zeta_\mathbb{Q}(s)$ are the eigenvalues of $\Phi^1_*: H^1(X) \to H^1(X)$ (the map induced on cohomology by time $t=1$).
3. The trace of the Frobenius (the element $\Phi^1_*$) satisfies the Lefschetz trace formula:
$$\mathrm{Tr}(\Phi^1_* | H^1) = \sum_{\rho} 1 = N_\zeta$$

the number of zeros (counted with multiplicity).

**Current status of the Deninger program:** The space $X$ has not been built in any existing mathematical category. Deninger describes it through the properties it should have, but the explicit construction is open.

**The connection with our program:**

Our deficit space $\mathcal{V}_\zeta$ is *different* from the Deninger space: Deninger needs the eigenvalues of $\Phi^1_*$ to be the zeros of $\zeta$ (the Hilbert-Pólya problem), whereas our $\mathcal{V}_\zeta$ needs the absence of off-critical zeros to be equivalent to the triviality of the cohomology. These are distinct but related questions.

---

## 3. The category $\mathcal{MM}$: concrete construction

We do not build an abstract motivic category. We build a concrete category of analytic objects.

**Definition 3.1 (Objects of $\mathcal{MM}$).** An object of $\mathcal{MM}$ is a triple $(\mathcal{R}, \mu, F)$ where:
- $\mathcal{R} \subset \mathbb{H}$ is an admissible region (satisfies Axiom 3 of Doc 48).
- $\mu$ is a positive Borel measure on $\mathcal{R}$ with $\int y/(1+x^2)d\mu < \infty$.
- $F: \mathbb{H}^+ \to [0,\infty)$ is the harmonic extension $F = \mathcal{P}[\mu]$.

The triple must satisfy the *weak self-consistency* condition: the restriction of $F$ to the real line satisfies $F(t) \geq 0$ for every $t\in\mathbb{R}$.

**Definition 3.2 (Morphisms of $\mathcal{MM}$).** A morphism $\phi: (\mathcal{R}_1, \mu_1, F_1) \to (\mathcal{R}_2, \mu_2, F_2)$ is a measure map $\phi_*: M(\mathcal{R}_1) \to M(\mathcal{R}_2)$ satisfying:
1. $\phi_*(\mu_1) = \mu_2$ (measure morphism).
2. $F_2 = \mathcal{P}[\mu_2] = \mathcal{P}[\phi_*\mu_1]$ (compatibility with the harmonic extension).

**Proposition 3.3.** $\mathcal{MM}$ is a category: composition of morphisms is the push-forward of measures, which is associative and has units (identity = identity of measures).

**Definition 3.4 (The trivial object and the zeta object).** The *trivial object* is $(R, 0, 0)$. The *zeta object* is $(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty)$. RH is equivalent to the zeta object coinciding with the trivial one.

---

## 4. Cohomology on $\mathcal{MM}$

**Definition 4.1 (The functor $H^0$).** For an object $(\mathcal{R}, \mu, F) \in \mathcal{MM}$:
$$H^0(\mathcal{R}, \mu, F) := F|_\mathbb{R} \in C(\mathbb{R}, \mathbb{R}_{\geq 0})$$

is the boundary trace of the harmonic function.

**Definition 4.2 (The functor $H^1$).** To define $H^1$, we use the Mayer-Vietoris exact sequence. Cover $\mathcal{R} = U_1 \cup U_2$ by two open sets. Then:
$$H^1(\mathcal{R}, \mu, F) := \ker(\delta^1: C^1(\mathcal{U}, \mathcal{F}_\mathcal{MM})\to C^2(\mathcal{U}, \mathcal{F}_\mathcal{MM}))/\mathrm{im}(\delta^0)$$

where $\mathcal{F}_\mathcal{MM}$ is the sheaf that assigns to each open set $U\subset\mathcal{R}$ the space of positive harmonic functions on $U$ representable as $\mathcal{P}[\mu|_U]$.

**Proposition 4.3 (Explicit computation of $H^1$ for the trivial object).** For the trivial object $(R, 0, 0)$:
$$H^1(\mathcal{R}, 0, 0) = 0$$

*Proof.* If $\mu = 0$, the sheaf $\mathcal{F}_\mathcal{MM}$ has only sections $\equiv 0$, hence all cohomology is trivial. $\square$

**Proposition 4.4 (Computation of $H^1$ for the zeta object).** If $\mu_{\mathrm{off}} \neq 0$:
$$H^1(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty) \neq 0$$

*Proof (sketch).* The sheaf $\mathcal{F}_\mathcal{MM}$ has nontrivial sections determined by $\mu_{\mathrm{off}}$. The cohomology $H^1$ measures the obstruction to extending local sections — which is nontrivial when $\mu_{\mathrm{off}} \neq 0$ since the measure has positive mass. $\square$

**Corollary 4.5.** RH $\iff H^1(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty) = 0$.

---

## 5. The arithmetic Frobenius as an endofunctor

**Definition 5.1 (The endofunctor $\Phi_\zeta$).** The *arithmetic Frobenius* is the endofunctor $\Phi_\zeta: \mathcal{MM} \to \mathcal{MM}$ acting on objects by:
$$\Phi_\zeta(\mathcal{R}, \mu, F) = (\mathcal{R}, \Phi[\mu], \mathcal{P}[\Phi[\mu]])$$

where $\Phi[\mu]$ is the self-consistency operator of Doc 51.

**Proposition 5.2 (Fixed points of $\Phi_\zeta$ as objects of $\mathcal{MM}$).** The fixed points of $\Phi_\zeta$ in $\mathcal{MM}$ are exactly the objects $(\mathcal{R}, \mu, F)$ with $\Phi[\mu] = \mu$, namely:
- The trivial object $(R, 0, 0)$.
- The zeta object $(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty)$ if RH fails.

**Proposition 5.3 (Action of $\Phi_\zeta$ on cohomology).** The endofunctor $\Phi_\zeta$ induces a map on cohomology:
$$\Phi_\zeta^*: H^1(\mathcal{R}, \mu, F) \to H^1(\mathcal{R}, \Phi[\mu], \mathcal{P}[\Phi[\mu]])$$

**Definition 5.4 (Trace of the Frobenius).** The trace of $\Phi_\zeta^*$ on $H^1$ is:
$$\mathrm{Tr}(\Phi_\zeta^* | H^1) := \dim_\mathbb{R}(H^1(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty))$$

*Note:* this definition is weaker than the trace of a linear operator on a finite-dimensional space — $H^1$ may be infinite-dimensional. The correct definition requires specifying the notion of "trace" in infinite dimension (trace-class operator trace).

---

## 6. The Cohomological Positivity Conjecture: precise formulation

**Definition 6.1 (Weil form on $\mathcal{MM}$).** The *Weil form* on $H^1(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty)$ is the pairing:
$$\langle\alpha, \beta\rangle_W := \int_\mathbb{H} \alpha(x,y)\cdot\beta(x,y)\,d\mu_{\mathrm{off}}(x,y)$$

where $\alpha, \beta \in H^1$ are represented as functions on $\mathcal{R}_\eta$.

**Proposition 6.2 (Positivity of the Weil form is automatic for $H^0$).** For $H^0 = C_\infty$:
$$\langle C_\infty, C_\infty\rangle_W = \int |C_\infty|^2\,d\mu_{\mathrm{off}} = \mathcal{E}[\mu_{\mathrm{off}}] \geq 0$$

with equality only if $\mu_{\mathrm{off}} = 0$ (RH).

**Cohomological Positivity Conjecture (CPC) — precise version:**
$$\langle\alpha, \Phi_\zeta^*\alpha\rangle_W > 0 \quad \forall \alpha \in H^1 \setminus\{0\}$$

*This is a version of the Weil-Petersson pairing for the moduli space of measures.*

**Theorem 6.3 (CPC $\Rightarrow$ RH).** If the CPC is true and $H^1(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty) \neq 0$ (i.e. RH fails), then:
$$\langle\alpha, \Phi_\zeta^*\alpha\rangle_W > 0 \quad \Rightarrow \quad \mathrm{Tr}(\Phi_\zeta^*|H^1) > 0$$

But a positive trace is $\sum(\sigma_0-1/2) > 0$, which contradicts... nothing, because a positive trace is perfectly compatible with RH failing.

*Correction to the Doc 49 argument.* Theorem 6.2 of Doc 49 had a logical error: positivity of the trace does NOT imply that the trace is zero (and hence RH). In the Weil case, positivity of $\langle\alpha, \bar\alpha\rangle > 0$ implies $|\lambda|^2 = q$ for the eigenvalues — which uses *Poincaré duality* in a specific way that relates $H^1$ to $H^1 \otimes \mathbb{Q}(-1)$. Without this duality in the category $\mathcal{MM}$, the argument does not close.

---

## 7. Poincaré Duality on $\mathcal{MM}$: the missing ingredient

**Definition 7.1 (Poincaré duality on $\mathcal{MM}$).** A *Poincaré duality* on $\mathcal{MM}$ would be an isomorphism:
$$H^1(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty) \cong H^1(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty)^\vee \otimes \omega$$

where $\omega$ is a "dualizing object" — the analogue of the Tate torsor $\mathbb{Q}(-1)$ in $\ell$-adic theory.

**Proposition 7.2 (The dualizing object in $\mathcal{MM}$).** The natural candidate for the dualizing object is:
$$\omega = (0, \lambda_{\mathrm{Leb}}, 1)$$

the object with Lebesgue measure (restricted to $\mathcal{R}_\eta$) and constant harmonic function $\equiv 1$.

**Conjecture 7.3 (Poincaré duality for $\mu_{\mathrm{off}}$).** If there is a canonical isomorphism:
$$H^1(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty) \cong \mathrm{Hom}(H^1(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty), \omega)$$

then the combination CPC + Poincaré duality would give:
$$|\lambda_i|^2 = \langle\alpha_i, \Phi_\zeta^*\alpha_i\rangle / \|\alpha_i\|^2 = \text{const}$$

that is, all eigenvalues of $\Phi_\zeta^*$ have the same modulus — the analogue of the zeros lying on the critical line.

**The frank status:** Conjecture 7.3 is the missing ingredient for Direction III to close the argument. There is no direct mathematical evidence that $\mathcal{MM}$ has Poincaré duality — it is the central question of this direction.

---

## 8. The precise connection with Deninger

**Proposition 8.1 (Relation between $\mathcal{MM}$ and the Deninger space).** The "Deninger space" $X$ (if it existed) and our deficit space $\mathcal{V}_\zeta$ would be related by:
- In $X$: the eigenvalues of $\Phi^t_*|_{H^1(X)}$ are the zeros of $\zeta$ (including the possible off-critical ones).
- In $\mathcal{V}_\zeta$: the dimension of $H^1(\mathcal{V}_\zeta)$ measures how many off-critical zeros there are.

*These are complementary questions:* Deninger wants to find all the zeros; we want to prove there are no off-critical zeros.

**Proposition 8.2 (Lefschetz trace formula on $\mathcal{MM}$).** Assuming the existence of Poincaré duality on $\mathcal{MM}$ and that the Frobenius $\Phi_\zeta$ has a Lefschetz trace given by the count of fixed points:

$$\sum_{i=0}^{\dim} (-1)^i \mathrm{Tr}(\Phi_\zeta^*|H^i) = \#\{\text{fixed points of } \Phi_\zeta\} = 1 + \#\mathcal{Z}_{\mathrm{off}}$$

(the 1 comes from the trivial fixed point $\mu=0$; $\#\mathcal{Z}_{\mathrm{off}}$ comes from the off-critical zeros).

If $H^0 = \mathbb{R}$ (trace = 1), $H^2 = 0$ (nothing in dimension 2), $H^1$ gives $\#\mathcal{Z}_{\mathrm{off}}$:
$$1 - \#\mathcal{Z}_{\mathrm{off}} + 0 = 1 + \#\mathcal{Z}_{\mathrm{off}}$$

This gives $\#\mathcal{Z}_{\mathrm{off}} = 0$ only if $\#\mathcal{Z}_{\mathrm{off}} = 0$ — circular. *The Lefschetz argument is not sufficient by itself.*

**Remark 8.3 (Why the Weil proof is not circular).** In the Weil case for curves over $\mathbb{F}_q$:
$$1 - \mathrm{Tr}(\phi_q|H^1) + q = q + 1 - \sum_{i=1}^{2g}\alpha_i = |C(\mathbb{F}_q)|$$

Here the key is not the count (which is circular), but the *estimate* $|\mathrm{Tr}(\phi_q|H^1)| \leq 2g\sqrt{q}$, which follows from positivity and gives the Riemann hypothesis for the curve. For the Riemann zeta, the analogous estimate would be $|\mathrm{Tr}(\Phi_\zeta^*|H^1)| \leq C$ — which would give information about $\#\mathcal{Z}_{\mathrm{off}}$ if $C$ could be taken $= 0$.

---

## 9. The three concrete missing steps

**Step III.A: Build Poincaré duality on $\mathcal{MM}$.**

This requires:
1. Defining the "dual" of an object $(\mathcal{R}, \mu, F)$ as $(\mathcal{R}, \mu^\vee, F^\vee)$ where $\mu^\vee$ is the "conjugate" measure in some sense.
2. Building a canonical pairing $H^1 \times H^1 \to \omega$.
3. Proving the pairing is non-degenerate.

The candidate for $\mu^\vee$: the complementary measure under the functional equation $\mu^\vee = \mu \circ \sigma_{\mathrm{funct}}$ (the reflection of the quartet). By Axiom 2 of Doc 48, $\mu^\vee$ lives in $\mathbb{H}^-$, not in $\mathbb{H}^+$ — so the duality would connect objects in $\mathbb{H}^+$ with objects in $\mathbb{H}^-$.

**Step III.B: Compute the Weil form on $H^1 \otimes H^1 \to \omega$.**

This requires computing the pairing $\langle\alpha, \beta\rangle_W$ explicitly and checking whether it is positive-definite (CPC).

**Step III.C: Derive the estimate $|\mathrm{Tr}(\Phi_\zeta^*|H^1)| \leq C_0$.**

With $C_0 = 0$, this would give $\sum(\sigma_0-1/2) = 0$, hence RH. The estimate $C_0 = 0$ would be the analogue of Weil positivity. It requires the Schwarz Lemma inequality for the Weil form.

---

## 10. Exact status of Direction III

| Statement | Status | Tool |
|------------|--------|-------------|
| Category $\mathcal{MM}$ well defined | ✓ | This document |
| $H^0$ and $H^1$ defined on $\mathcal{MM}$ | ✓ | Sheaf cohomology |
| RH $\iff H^1 = 0$ | ✓ | Direct construction |
| Frobenius $\Phi_\zeta$ as an endofunctor | ✓ | Operator $\Phi$ from Doc 51 |
| Lefschetz trace formula | ✓ conditional | Poincaré duality |
| Poincaré duality on $\mathcal{MM}$ | ❌ Open | — |
| CPC for the Weil form of $\mathcal{MM}$ | ❌ Open | — |
| Estimate $|\mathrm{Tr}| \leq 0$ | ❌ Open — equivalent to RH | — |

**The precise reduction:**

> Direction III reduces RH to: *building Poincaré duality on $\mathcal{MM}$ and proving that the Weil form $\langle\alpha, \Phi_\zeta^*\alpha\rangle_W$ satisfies the Schwarz Lemma estimate that gives $|\mathrm{Tr}(\Phi_\zeta^*|H^1)| = 0$.*

---

## 11. Convergence of the three directions: the unified obstacle

**Theorem 11.1 (Unification).** The three obstacles are formally equivalent:

| Direction | Obstacle |
|-----------|-----------|
| II (Completeness) | Is $F = \sum a_k P_{y_k}(\cdot-x_k)$ of definite sign if $F(\gamma_n)=0$ $\forall n$? |
| I (Fixed point) | Does $\mathcal{E}[\Phi[\mu]] \leq \mathcal{E}[\mu]$ hold for every $\mu \neq 0$? |
| III (Motivic) | Does Poincaré duality exist on $\mathcal{MM}$ with CPC? |

*All three are versions of the same positivity problem:*

> Can a positive harmonic function, built from Poisson kernels of off-critical zeros of $\zeta$, be forced to be zero by the distribution of the on-critical zeros?

---

## 12. The next concrete question

The three directions have converged on ONE well-defined analytic problem:

**Central Problem (CP):**

> Let $F: \mathbb{R} \to \mathbb{R}_{\geq 0}$ be a continuous function with $F \geq 0$, $F(\gamma_n) = 0$ for every $n \geq 1$, and $F$ representable as $F = \mathcal{P}[\mu]$ for some positive measure $\mu$ supported on $\mathcal{R}_\eta$. Does it follow that $F \equiv 0$?

**Known answer:** Yes, trivially — since if $F \geq 0$ and $F(\gamma_n) = 0$ at at least one point, the Poisson Rigidity Theorem (Doc 43) gives $\mu = 0$, hence $F = 0$.

**The nontrivial version of the Central Problem:**

> Let $F: \mathbb{R} \to \mathbb{R}$ (with no sign hypothesis) satisfy $F(\gamma_n) = 0$ for every $n\geq 1$, and $F = \mathcal{P}[\mu] - \mathcal{P}[\nu]$ for positive measures $\mu, \nu$. Does it follow that $\mu = \nu$?

This is the signed version — the obstacle shared by the three directions, which does not follow from general principles.

---

*Doc 53 will attack the Central Problem without a sign hypothesis: sufficient conditions for $\mathcal{P}[\mu] = \mathcal{P}[\nu]$ on $\{\gamma_n\}$ to imply $\mu = \nu$.*
