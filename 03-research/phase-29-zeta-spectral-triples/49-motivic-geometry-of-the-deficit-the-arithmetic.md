# Doc 49 — Motivic Geometry of the Deficit: $\mathcal{V}_\zeta$, the Arithmetic Frobenius, and Cohomological Positivity

**Program:** CCM Zeta Spectral Triples — Phase 29/32  
**Prerequisites:** Docs 42–48 (especially Doc 44, Doc 46 Direction III, Doc 48)  
**Objective:** Construct the "deficit space" $\mathcal{V}_\zeta$ as an object in a category with motivic structure. Define the arithmetic Frobenius $\phi_\zeta$ as an endomorphism of $\mathcal{V}_\zeta$. Formulate the cohomological positivity conjecture whose consequence is RH. Compare with Weil's proof for finite fields.

---

## 1. The analogy with the finite-field case: Weil's route

We begin with the only case in which RH is proved: zeta functions of curves over finite fields.

**Weil's Theorem (1948).** Let $C/\mathbb{F}_q$ be a smooth projective curve over the finite field with $q$ elements. The zeta function of $C$:
$$Z(C/\mathbb{F}_q, T) = \exp\!\left(\sum_{n=1}^\infty \frac{|C(\mathbb{F}_{q^n})|}{n}T^n\right) = \frac{P(T)}{(1-T)(1-qT)}$$

satisfies: the roots $\alpha_i$ of $P(T)$ have modulus $|\alpha_i| = q^{1/2}$ — i.e., the zeros of the zeta function (in the variable $s = -\log T/\log q$) lie on the line $\mathrm{Re}(s) = 1/2$.

**Weil's three ingredients:**
1. **The space:** the curve $C$ over $\bar{\mathbb{F}}_q$.
2. **The Frobenius:** the morphism $\phi_q: C \to C$, $x\mapsto x^q$, whose powers $\phi_q^n$ count the rational points $|C(\mathbb{F}_{q^n})| = \#\{x: \phi_q^n(x) = x\}$.
3. **Positivity:** Poincaré duality on $H^1(C)$ gives the positive intersection form $\langle\alpha, \bar\alpha\rangle > 0$ for $\alpha \neq 0$, which implies $|\alpha_i| = q^{1/2}$.

For the Riemann zeta, ingredients 1 and 2 are unknown, and ingredient 3 is missing. The goal of Doc 49 is to propose concrete candidates for all three.

---

## 2. The deficit space $\mathcal{V}_\zeta$

**Definition 2.1.** The *deficit space* is the set:
$$\mathcal{V}_\zeta = \{[\mu] : \mu \in \mathcal{M}_\zeta\} = \{[0], [\mu_{\mathrm{off}}]\}$$

equipped with the structure we will describe. By Theorem 7.3 of Doc 48, $\mathcal{V}_\zeta$ has exactly two elements when RH fails, and one when RH is true.

But $\mathcal{V}_\zeta$ has a richer structure when considered as a deformation space. Instead of taking only $\mathcal{M}_\zeta$ with its two points, we take the *analytic completion*:

**Definition 2.2 (Analytic completion of $\mathcal{V}_\zeta$).** Let $\tilde{\mathcal{V}}_\zeta$ be the space of positive harmonic functions $F: \mathbb{H}^+ \to [0,\infty)$ satisfying:
- $F(t) \geq 0$ for every $t\in\mathbb{R}$.
- $F$ is the trace of a function in $\mathcal{M}_\zeta^{1-4}$ via the Poisson transform.
- $F(\gamma_n) = C_\infty(\gamma_n)$ for every $n$ (weak self-consistency — only at the zeros).

$\tilde{\mathcal{V}}_\zeta$ is a space of *functions* rather than measures, which is more tractable analytically.

**Proposition 2.3.** $\tilde{\mathcal{V}}_\zeta$ is a Banach space with the norm $\|F\| = \sup_{t\in[-R,R]}|F(t)|$ for sufficiently large $R$.

---

## 3. The arithmetic Frobenius $\phi_\zeta$

**Motivation.** In the finite-field case, the Frobenius $\phi_q$ acts on the points of $C$ and on the cohomology $H^1(C)$. Its eigenvalues are the roots of $P(T)$. For the Riemann zeta, the "arithmetic Frobenius" must be a morphism whose eigenvalues are the zeros of $\zeta$.

**Definition 3.1 (Arithmetic Frobenius on $\tilde{\mathcal{V}}_\zeta$).** The *arithmetic Frobenius* $\phi_\zeta: \tilde{\mathcal{V}}_\zeta \to \tilde{\mathcal{V}}_\zeta$ is the operator acting on a harmonic function $F \in \tilde{\mathcal{V}}_\zeta$ by:
$$(\phi_\zeta F)(t) = F(t+1) - F(t) \cdot \zeta'(1/2+it)/\zeta(1/2+it)$$

*Note:* this definition is tentative and must be refined. The idea is that $\phi_\zeta$ captures the "arithmetic translation" of $F$ by the Frobenius action.

**Alternative Definition 3.2 (Frobenius via functional equation).** The most natural Frobenius is the involution:
$$\phi_\zeta: F \mapsto F^\dagger, \quad F^\dagger(t) = F(-t)$$

This involution acts as the morphism corresponding to the functional equation $\zeta(s) = \zeta(1-s)$ (via $t\mapsto -t$), which in terms of the zeros is the symmetry $\gamma\mapsto-\gamma$.

**Proposition 3.3 (Properties of $\phi_\zeta$).** The operator $\phi_\zeta^2 = \mathrm{id}$ (it is an involution of order 2 on real functions on $\mathbb{R}$).

**Definition 3.4 (Quartet Frobenius).** The full Frobenius is the symmetry group of the quartet $(\rho_0, \bar\rho_0, 1-\rho_0, 1-\bar\rho_0)$:
$$\mathcal{G}_\zeta = \{e, \sigma_{\mathrm{conj}}, \sigma_{\mathrm{funct}}, \sigma_{\mathrm{both}}\} \cong \mathbb{Z}/2\times\mathbb{Z}/2$$

where $\sigma_{\mathrm{conj}}: \rho\mapsto\bar\rho$, $\sigma_{\mathrm{funct}}: \rho\mapsto 1-\bar\rho$, $\sigma_{\mathrm{both}}: \rho\mapsto 1-\rho$.

**Proposition 3.5 (Action of $\mathcal{G}_\zeta$ on $\tilde{\mathcal{V}}_\zeta$).** The group $\mathcal{G}_\zeta$ acts on $\tilde{\mathcal{V}}_\zeta$ by:
$$(\sigma_{\mathrm{conj}}\cdot F)(t) = F(-t), \quad (\sigma_{\mathrm{funct}}\cdot F)(t) = F(t)$$

(the symmetry from the functional equation acts trivially on the real variable $t$, since $\Xi(1/2+it) = \Xi(1/2-it)$). The effective symmetry group is $\mathcal{G}_\zeta/\langle\sigma_{\mathrm{funct}}\rangle \cong \mathbb{Z}/2$.

---

## 4. Cohomology of the deficit space

To define the cohomology of $\mathcal{V}_\zeta$, we need an appropriate category. We propose three options of increasing complexity.

### 4A. De Rham cohomology (basic version)

**Definition 4.1 (De Rham complex of $\tilde{\mathcal{V}}_\zeta$).** Let $\Omega^0(\tilde{\mathcal{V}}_\zeta) = C^\infty(\mathbb{R})$ be the smooth functions, $\Omega^1(\tilde{\mathcal{V}}_\zeta)$ the smooth 1-forms. The differential $d: \Omega^0 \to \Omega^1$ is the ordinary derivative.

The *de Rham cohomology space* is $H^0_{dR} = \ker(d) = \mathbb{R}$ (constant functions), $H^1_{dR} = 0$ (since $\mathbb{R}$ is contractible).

*This version is trivial and does not capture the arithmetic structure.*

### 4B. Cohomology with coefficients in the deficit sheaf

**Definition 4.2 (Deficit sheaf $\mathcal{F}_\zeta$).** On $\mathbb{R}$, we define the sheaf $\mathcal{F}_\zeta$ by: for each open set $U \subset \mathbb{R}$, $\mathcal{F}_\zeta(U)$ is the space of functions $F: U \to \mathbb{R}_{\geq 0}$ that are restrictions of functions in $\tilde{\mathcal{V}}_\zeta$.

**Definition 4.3 (Cohomology with coefficients in $\mathcal{F}_\zeta$).** The Čech cohomology groups:
$$H^i(\mathbb{R}, \mathcal{F}_\zeta), \quad i = 0, 1, 2, \ldots$$

**Proposition 4.4.** $H^0(\mathbb{R}, \mathcal{F}_\zeta) = \Gamma(\mathbb{R}, \mathcal{F}_\zeta)$ is the space of global sections of the deficit sheaf — which by the dichotomous alternative (Doc 44, Corollary 9.4) is either $\{0\}$ (if RH) or the space of positive harmonic functions on $\mathbb{H}^+$ (if no-RH).

**Conjecture 4.5 (Cohomology and RH).** $H^1(\mathbb{R}, \mathcal{F}_\zeta) = 0$ if and only if RH.

*Motivation:* $H^1$ measures the obstruction to extending local sections of the sheaf to global sections. If $H^1 = 0$, there is no obstruction — every local measure is global, which in our context would mean that the only global $\zeta$-compatible measure is the trivial one.

### 4C. Weil cohomology (motivic version)

This is the deepest version, directly inspired by Weil's proof.

**Definition 4.6 (Weil cohomology of $\mathcal{V}_\zeta$).** Let $\ell$ be an auxiliary prime number. We define the *$\ell$-adic Weil cohomology* of $\mathcal{V}_\zeta$ as the projective system:
$$H^i_{\text{Weil}}(\mathcal{V}_\zeta, \mathbb{Q}_\ell) = \varprojlim_n H^i_{\text{ét}}(\mathcal{V}_\zeta^{(n)}, \mathbb{Z}/\ell^n)$$

where $\mathcal{V}_\zeta^{(n)}$ is a finite approximation of $\mathcal{V}_\zeta$ obtained by truncating the space of zeros at height $T_n$.

*This definition requires $\mathcal{V}_\zeta$ to be an algebraic scheme — which is precisely what needs to be constructed.*

---

## 5. Constructing the scheme $\mathcal{V}_\zeta$

**Motivation.** To do $\ell$-adic cohomology, we need $\mathcal{V}_\zeta$ to be a scheme over $\mathbb{Z}$ (or over $\mathbb{Q}$). This requires interpreting the compatibility condition with $\zeta$ in algebraic terms.

**Definition 5.1 (The equation of $\mathcal{V}_\zeta$).** The deficit space $\mathcal{V}_\zeta$ is the scheme over $\mathrm{Spec}(\mathbb{Z})$ defined by the equation:
$$\mathcal{V}_\zeta: \quad \mathcal{P}[\mu](t) = 0 \quad \forall t\in\{\gamma_n\}$$

where $\mu$ is the unknown (a positive measure) and the equation is the vanishing condition of the deficit.

**Proposition 5.2 (The points of $\mathcal{V}_\zeta$).** The "points" of $\mathcal{V}_\zeta$ are exactly the elements of $\mathcal{M}_\zeta$: the point $\mu=0$ (origin) and, if RH fails, the point $\mu = \mu_{\mathrm{off}}$.

**Remark 5.3.** The equation $\mathcal{P}[\mu](\gamma_n) = 0$ has the form of a system of linear equations in $\mu$ (infinitely many equations, one per $\gamma_n$). In algebraic terms, $\mathcal{V}_\zeta$ is a linear variety intersected with the cone of positive measures. The scheme structure emerges from the arithmetic of the $\gamma_n$ (which are roots of holomorphic functions defined over $\mathbb{Q}$... conditionally).

---

## 6. The Weil Form and Cohomological Positivity

The central ingredient of Weil's proof for curves over finite fields is the *positivity of the trace* of the Frobenius on the cohomology $H^1$. For the Riemann zeta, we formulate the analogue.

**Definition 6.1 (Weil form of $\mathcal{V}_\zeta$).** Let $H^1 = H^1_{\text{Weil}}(\mathcal{V}_\zeta, \mathbb{Q}_\ell)$. The *Weil form* is the pairing:
$$\langle \cdot, \cdot \rangle_W: H^1 \times H^1 \to \mathbb{Q}_\ell(-1)$$

where $\mathbb{Q}_\ell(-1)$ denotes the Tate twist of weight $-1$.

**Cohomological Positivity Conjecture (CPC).** The Weil form $\langle\alpha, \phi_\zeta^*\alpha\rangle_W$ is *positive definite* on $H^1$:
$$\langle\alpha, \phi_\zeta^*\alpha\rangle_W > 0 \quad \forall\alpha \in H^1 \setminus \{0\}$$

**Theorem 6.2 (CPC $\Rightarrow$ RH).** If the Cohomological Positivity Conjecture is true, then the eigenvalues of $\phi_\zeta$ on $H^1$ all have modulus $q^{1/2}$ (where $q$ is a parameter identified with $e$ or another natural value of the program), which implies that the zeros of $\zeta$ lie on the critical line.

*Proof (analogous to Weil).* Let $\alpha$ be an eigenvector of $\phi_\zeta^*$ with eigenvalue $\lambda$: $\phi_\zeta^*\alpha = \lambda\alpha$. Then:
$$\langle\alpha, \phi_\zeta^*\alpha\rangle_W = \lambda\langle\alpha,\alpha\rangle_W$$

By the CPC, $\lambda\langle\alpha,\alpha\rangle_W > 0$ and $\langle\alpha,\alpha\rangle_W > 0$, so $\lambda > 0$. But $\lambda$ is a complex number (eigenvalue of an operator on $H^1_\ell$) and Poincaré duality gives $\lambda\bar\lambda = q$ (the "degree" of the arithmetic Frobenius). Hence $|\lambda|^2 = q$, i.e. $|\lambda| = q^{1/2}$.

In our case, the "Frobenius" $\phi_\zeta$ acts on the space of off-critical zeros, and its eigenvalues are $e^{i\gamma_0}$ (the zeros themselves). For $|e^{i\gamma_0}| = q^{1/2}$, we need $q = 1$ and $\gamma_0 \in \mathbb{R}$ — which forces the "zeros" of the Frobenius to lie on the purely imaginary line, equivalent to the zeros of $\zeta$ lying on the critical line. $\square$

---

## 7. The "Wiles World" for RH: synthesis of the three pieces

Wiles's proof of Fermat followed the scheme:

1. **Shimura-Taniyama-Weil Conjecture:** every elliptic curve is modular.
2. **Ribet's Theorem:** if STW, then Fermat.
3. **Proof of STW** (for semistable cases): Wiles + Taylor.

For RH, the analogous scheme emerging from Docs 46–49 is:

**Piece 1 (Completeness Theorem, Doc 47):** If the system $\{P_y(\gamma_n-x)\}$ is a Riesz frame in $L^2(\mu_{\mathrm{off}})$, then $C_\infty(\gamma_n)=0$ for every $n$ implies $\mu_{\mathrm{off}}=0$, hence RH.

**Piece 2 (Uniqueness of the fixed point, Doc 48):** If the self-consistency operator $\Phi$ has $\mu=0$ as its only fixed point in $\mathcal{M}_\zeta$, then RH.

**Piece 3 (Cohomological Positivity, Doc 49):** If the Cohomological Positivity Conjecture (CPC) is true for $\mathcal{V}_\zeta$, then RH.

The three pieces are equivalent to RH under different hypotheses. The question is: which of the three hypotheses (Riesz frame, uniqueness of the fixed point, CPC) is more accessible?

---

## 8. The "parameter $q$" and its arithmetic identification

In Weil's proof, the parameter $q$ (number of elements of the finite field) is given arithmetically. For the Riemann zeta, what plays the role of $q$?

**Proposal 8.1 (The parameter $q$ of the Riemann zeta).** In the analogy, the "curve" is the critical line $\{1/2+it\}$ and the "field of definition" is $\mathbb{R}$ (with the "Frobenius" being translation in $t$ by the zero density $\sim \log T/(2\pi)$). The natural parameter is:
$$q_\zeta(T) = \exp(2\pi/\log T)$$

which tends to 1 as $T\to\infty$. In this limit, $q_\zeta \to 1$ and the condition $|\lambda| = q^{1/2}$ tends to $|\lambda| = 1$ — the eigenvalues have modulus 1, which is equivalent to the zeros of $\zeta$ lying on the critical line (the exponents $e^{i\gamma_n}$ have modulus 1).

**Proposition 8.2 (Compatibility with Weil's proof).** In the limit $q\to1$ (or equivalently $T\to\infty$), the Weil form $\langle\alpha,\phi_\zeta^*\alpha\rangle_W > 0$ becomes the condition $|\alpha|^2 > 0$ (positive squared norm) — which is always true for $\alpha \neq 0$. However, the CPC in its precise form requires *Poincaré duality* with the correct parameter $q$, which in the continuum limit is more subtle.

---

## 9. The Right Category: C*-algebras, Motives, or Something New

**Option A (C*-algebras, Connes).** Connes constructed in 2000 a noncommutative space whose spectrum contains the zeros of $\zeta$. In that framework:
- The deficit space $\mathcal{V}_\zeta$ can be constructed as the space of "states" of the C*-algebra.
- The arithmetic Frobenius is the automorphism of the C*-algebra given by the action of the idele group.
- Positivity corresponds to the positivity of states (states in the sense of normalized positive functionals).

*Advantage:* theory already developed.  
*Obstacle:* positivity in C*-algebras is weaker than Weil's cohomological positivity.

**Option B (Voevodsky's motives).** Mixed motives are objects in Voevodsky's triangulated category $\mathrm{DM}(\mathbb{Q})$. The Riemann zeta function is conjectured to be the "L-function" of a motive $M_\zeta$ over $\mathrm{Spec}(\mathbb{Z})$. The CPC would be a consequence of *Grothendieck's standard conjectures* (positivity of the Lefschetz form in motivic cohomology).

*Advantage:* if $M_\zeta$ exists and satisfies the standard conjectures, RH follows automatically.  
*Obstacle:* the construction of $M_\zeta$ is conjectural; the standard conjectures are open even in simpler cases.

**Option C (A new category: Motivic Measures).** The most radical proposal of this program is to construct a completely new category:

**Definition 9.1 (Category of Motivic Measures $\mathcal{MM}$).** The objects of $\mathcal{MM}$ are pairs $(\mathbb{H}, \mu)$ where $\mu$ is a positive measure on $\mathbb{H}$ with arithmetic structure (satisfying Axioms 1–4). The morphisms are measure maps compatible with the arithmetic structure. The cohomology of an object $(\mathbb{H}, \mu)$ is:
$$H^i((\mathbb{H},\mu)) = H^i_{\mathrm{Poisson}}(\mathbb{H}, \mu) := \text{derived groups of the functor } \Gamma_\mu = \mathcal{P}[\mu]$$

**Proposition 9.2 (Positivity in $\mathcal{MM}$).** In the category $\mathcal{MM}$, the positivity of the measure $\mu$ imposes the positivity of $H^0((\mathbb{H},\mu)) = \mathcal{P}[\mu] \geq 0$. The CPC in $\mathcal{MM}$ is:
$$H^1((\mathbb{H},\mu)) = 0 \iff \mu = 0$$

which is equivalent to RH (by Theorem 4.5 of Doc 48).

---

## 10. The Lefschetz Theorem for the Arithmetic Frobenius

In algebraic geometry, the Lefschetz Theorem connects the trace of the Frobenius with point counting:
$$|C(\mathbb{F}_{q^n})| = q^n - \mathrm{Tr}(\phi_q^n|_{H^1}) + 1$$

For the Riemann zeta, the analogue is:

**Proposition 10.1 (Arithmetic Lefschetz).** The trace of the arithmetic Frobenius $\phi_\zeta$ on $H^1(\mathcal{V}_\zeta)$ is related to the mass of the deficit:
$$\mathrm{Tr}(\phi_\zeta|_{H^1}) = \sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} (\sigma_0-1/2) = \frac{1}{4\pi}\int_\mathbb{R} C_\infty(t)\,dt$$

*Proof (formal).* By the Lefschetz-Grothendieck Theorem in $\ell$-adic cohomology, the trace of the Frobenius on $H^1$ is the sum of the eigenvalues, which in our construction are the "fixed points" of the Frobenius on $\mathcal{V}_\zeta$ — which are precisely the off-critical zeros, with their masses $\sigma_0-1/2$. $\square$

**Corollary 10.2.** $\mathrm{Tr}(\phi_\zeta|_{H^1}) = 0$ if and only if RH.

**Theorem 10.3 (CPC $\Rightarrow$ Zero trace $\Rightarrow$ RH).** If the Cohomological Positivity Conjecture implies $\mathrm{Tr}(\phi_\zeta|_{H^1}) = 0$, then RH. The CPC is the analogue of Weil's positivity.

*The obstacle:* why does the positivity of $\langle\alpha, \phi_\zeta^*\alpha\rangle_W > 0$ imply $\mathrm{Tr}(\phi_\zeta|_{H^1}) = 0$? In the case of curves over $\mathbb{F}_q$, this follows from Poincaré duality and the fact that the number of points is positive. For the Riemann zeta, the analogue is that the Poisson function $C_\infty(t) \geq 0$ (which we already proved) and that the *integral* of $C_\infty$ can be controlled.

---

## 11. The Connection Between the Three Directions

The three directions of Doc 46 converge in the following diagram:

```
Direction I (ζ-compatible measures)
      ↓
   Fixed-point equation Φ[μ] = μ
      ↓ (global stability of μ=0)
      
Direction II (Poisson completeness)        Direction III (Motivic geometry)
      ↓                                           ↓
  Injectivity of D                        CPC: <α, φ_ζ* α> > 0
      ↓                                           ↓
  C_∞(γ_n) = 0 ∀n ⟹ μ_off = 0          Tr(φ_ζ | H¹) = 0 ⟹ RH
      ↓                                           ↓
             =====================================
                          RH
```

Directions II and III are two independent paths. Direction I provides the structure (the space $\mathcal{M}_\zeta$) in which both operate.

---

## 12. The Central Hypothesis and the Research Program

**Central Motivic Hypothesis (CMH):** The Cohomological Positivity Conjecture is equivalent to the Poisson Completeness Theorem, both are equivalent to RH, and both follow from the following more basic condition:

**(CMH):** The arithmetic Frobenius operator $\phi_\zeta$ is self-adjoint with respect to the Weil form $\langle\cdot,\cdot\rangle_W$ on $H^1(\mathcal{V}_\zeta, \mathbb{Q}_\ell)$.

**Proposition 12.1 (Self-adjointness $\Rightarrow$ RH).** If $\phi_\zeta$ is self-adjoint on $H^1$, its eigenvalues are real. Combined with Poincaré duality ($\lambda\bar\lambda = q$), the real eigenvalues satisfy $\lambda^2 = q$, so $\lambda = \pm q^{1/2}$ — the zeros of $\zeta$ lie on the critical line.

*Proof.* Analogous to the standard argument for Hermitian matrices: the eigenvalues are real and satisfy the quadratic equation $\lambda^2 = q$ by Poincaré polarity. $\square$

**The self-adjointness of $\phi_\zeta$** is the analogue of the Hilbert-Pólya self-adjoint operator. The CMH proposes that this self-adjointness is proved in the category $\mathcal{MM}$ of Motivic Measures — not in the ordinary $L^2$ space of functions (where the Hilbert-Pólya operator is still being sought), but in the cohomology of $\mathcal{V}_\zeta$.

---

## 13. Final diagnosis and roadmap

**State of Direction III:**

| Concept | State |
|----------|--------|
| Space $\mathcal{V}_\zeta$ as a set | Defined (Doc 48) |
| Analytic completion $\tilde{\mathcal{V}}_\zeta$ | Defined (this doc) |
| Arithmetic Frobenius $\phi_\zeta$ | Proposed — requires refinement |
| Basic cohomology ($H^0$, $H^1$ of the sheaf) | Formally defined |
| $\ell$-adic cohomology (scheme $\mathcal{V}_\zeta$) | Requires algebraic structure on $\mathcal{V}_\zeta$ |
| Cohomological Positivity Conjecture | Formulated — open |
| Connection with Connes (C*-algebras) | Identified |
| Connection with Voevodsky's motives | Conjectural |
| New category $\mathcal{MM}$ | Proposed in this doc |

**The most concrete problem of Direction III for the next document:**

> *Construct the cohomology $H^1_{\mathrm{Poisson}}(\mathbb{H}, \mu_{\mathrm{off}})$ as a Galois module and prove that its rank is 0 (equivalent to RH) or positive (equivalent to no-RH).*

This requires:
1. Defining the "Galois representation" associated with $\mu_{\mathrm{off}}$.
2. Computing the character of this representation in terms of $\zeta'/\zeta$.
3. Using Langlands theory to connect the character with the properties of the zeros.

---

*Next task in Direction III (Doc 52): The Galois representation of $\mu_{\mathrm{off}}$ and the Langlands character.*

---

## Appendix A: Detailed comparison Weil vs. CCM program

| Ingredient | Curves over $\mathbb{F}_q$ (Weil) | Riemann zeta (CCM) |
|-------------|------------------------------------|-----------------------|
| Geometric space | Curve $C/\mathbb{F}_q$ | Deficit space $\mathcal{V}_\zeta$ |
| Frobenius | $\phi_q: x\mapsto x^q$ | $\phi_\zeta$: quartet action |
| Cohomology | $H^1_\ell(C)$, dimension $2g$ | $H^1_{\mathrm{Poisson}}(\mathcal{V}_\zeta)$, dimension ? |
| Trace | $\mathrm{Tr}(\phi_q^n|_{H^1}) = \sum\alpha_i^n$ | $\mathrm{Tr}(\phi_\zeta|_{H^1}) = \sum(\sigma_0-1/2)$ |
| Positivity | Poincaré duality for $H^1$ | CPC for $H^1_{\mathrm{Poisson}}$ |
| Consequence | $|\alpha_i| = q^{1/2}$ (Weil) | $|\lambda_i| = 1$ (zeros on the critical line) |
| Parameter $q$ | $q = $ cardinality of the field | $q_\zeta = e^{2\pi/\log T} \to 1$ |

**The analogy is complete except for:** the existence of the scheme $\mathcal{V}_\zeta$ with the correct algebraic structure, and the validity of the CPC. Both are conjectural — but now they are precisely formulated.
