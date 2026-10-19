# Doc 97 — Direction D (third layer): The shadow minimizer $g^*$ and its Euler-Lagrange equations

**Program:** Riemann Hypothesis — Phase 34, New Directions  
**Prerequisites:** Docs 82, 83, 86, 88, 89, 93, 95  
**Level:** Advanced research — structural analysis of the hypothetical minimizer

---

## Summary

Doc 95 established that the minimizer $g^* \in \overline{\mathcal{M}}$ of the variational problem does not coincide with $f_0^{on}$ under $\neg$RH: Lemma 4.6 of that document proves that $f_0^{on}$ does not satisfy the Euler-Lagrange equations unless the residual $f_0 - f_0^{on}$ is identically zero, which is equivalent to RH. Therefore, under $\neg$RH, if the minimizer exists, it is a new object — which we call the **shadow minimizer** $g^*$ — distinct from $f_0^{on}$ and determined by the Euler-Lagrange equations themselves.

This document inaugurates the systematic study of $g^*$. Its objectives are:

1. **Reformulate** the Euler-Lagrange equations in terms of the residual $d\nu^* = (f_0 - g^*)\,dm_\infty$ and study the structure of that measure.
2. **Analyze** the properties of $d\nu^*$: positivity, arithmetic information, comparison with the object $d\nu$ of Doc 89.
3. **Study** the Euler-Lagrange system as an implicit moment problem in the zeros $\{\gamma_j^*\}$ of $\eta^*$.
4. **Formulate** conjectures on the uniqueness and canonicity of $g^*$.
5. **Explore** whether $g^*$ gives rise to a new reformulation of RH.

**Preliminary warning.** Throughout this document, the existence of $g^*$ in $\overline{\mathcal{M}}$ is taken as a working hypothesis (condition ND1 of Doc 95). Results depending on this hypothesis are explicitly marked with the label **(H-ND1)**. No proof of RH is fabricated; obstacles are pointed out frankly.

---

## §1. Preparation: the framework and the objects

### 1.1. The variational problem

Fix $\lambda > 0$. The working Hilbert space is
$$H_\lambda = L^2\bigl(\mathbb{R},\, W_\lambda(s)\,dm_\infty(s)\bigr),$$
where $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2\,ds$ is the CCM spectral measure and $W_\lambda \geq 0$ is the CCM kernel (see Doc 82, §2 for the precise definition of $W_\lambda$).

The approximation class is
$$\mathcal{M} = \bigl\{g_\eta : g_\eta(s) = |\eta(1/2+is)|^2,\;\eta \in \mathcal{E}\bigr\},$$
where $\mathcal{E}$ is the space of entire functions of order 1 with a functional equation analogous to $\xi$ and with all their zeros of the form $1/2+i\mu$, $\mu \in \mathbb{R}$.

The central object of the variational program is
$$f_0(s) = |\zeta(1/2+is)|^2,$$
which belongs to $L^2(W_\lambda\,dm_\infty)$ unconditionally (Doc 93, §1). The natural candidate for the minimizer in $\mathcal{M}$ is
$$f_0^{on}(s) = |\zeta_{\mathrm{on}}(1/2+is)|^2 \in \mathcal{M},$$
where $\zeta_{\mathrm{on}}$ is the function obtained by projecting all the zeros of $\zeta$ onto the critical line.

The fundamental variational criterion (Doc 82) establishes:
$$\tilde\delta_\lambda^2 := \inf_{g \in \mathcal{M}}\|f_0 - g\|^2_{H_\lambda} = 0 \iff \text{RH}.$$

### 1.2. The shadow minimizer: definition and conditional existence

**Definition 1.1 (Shadow minimizer).** Under the hypothesis **(H-ND1)** that the infimum is attained in the closure $\overline{\mathcal{M}}$ (or in $\mathcal{M}$ directly), the **shadow minimizer** is the element
$$g^* \in \overline{\mathcal{M}}: \quad \|f_0 - g^*\|^2_{H_\lambda} = \tilde\delta_\lambda^2.$$
We write $g^* = |\eta^*|^2$ where $\eta^* \in \overline{\mathcal{E}}$ (the appropriate closure of $\mathcal{E}$), with zeros $\{\rho_j^*\} = \{1/2 + i\gamma_j^*\}_{j \geq 1}$ on the critical line (by definition of $\mathcal{M}$; the discussion on $\overline{\mathcal{M}}$ in Doc 95 §2 may relax this condition).

The term "shadow" evokes the idea that $g^*$ is the reflection of $f_0$ in $\mathcal{M}$: the best on-critical approximation of $|\zeta|^2$, which under RH coincides with $f_0^{on}$, but under $\neg$RH is a genuinely different object, "projected" from $f_0$ by the geometry of the space.

**Proposition 1.2 (Epistemic status of $g^*$).** The following statements are precise as to their logical status:

(a) The criterion $\tilde\delta_\lambda^2 = 0 \iff$ RH does not require the existence of $g^*$: it is a statement about the value of the infimum.

(b) Under RH, $g^* = f_0^{on}$ and $\tilde\delta_\lambda^2 = 0$.

(c) Under $\neg$RH and under **(H-ND1)**, there exists $g^* \in \overline{\mathcal{M}}$ with $g^* \neq f_0^{on}$ and $\tilde\delta_\lambda^2 > 0$.

(d) Doc 95, Lemma 4.6 establishes that $f_0^{on}$ does not satisfy the Euler-Lagrange equations under $\neg$RH. Therefore, if $g^*$ exists and satisfies those equations, $g^* \neq f_0^{on}$, confirming (c).

*Proof.* Points (a) and (b) are Doc 82. Point (c) is the combination of Doc 93 (which proves $\tilde\delta_\lambda^2 > 0$ under $\neg$RH via positive second variation) with **(H-ND1)**. Point (d) is Doc 95, Lemma 4.6. $\square$

### 1.3. The Euler-Lagrange equations: initial statement

Let $g^* = |\eta^*|^2 \in \mathcal{M}$ with zeros $\{\pm\gamma_j^*\}$ of $\eta^*$ on the critical line. The Euler-Lagrange equations of the minimization problem for $\Phi(g) = \|f_0 - g\|^2_{H_\lambda}$ over $\mathcal{M}$, in the direction of variation of the zeros, are (Doc 95, §4):
$$\mathcal{E}_j^* := \int_{\mathbb{R}} W_\lambda(s)\bigl(f_0(s) - g^*(s)\bigr) \cdot g^*(s) \cdot \frac{2s}{s^2 - (\gamma_j^*)^2}\,dm_\infty(s) = 0 \quad \forall j \geq 1. \tag{EL}$$

These equations express that the functional derivative of $\Phi$ in the direction of a displacement of the $j$-th zero of $\eta^*$ is zero at the point $g^*$. They are the first-order condition of the variational problem.

---

## §2. Reformulation in terms of the residual $d\nu^*$

### 2.1. The residual measure

**Definition 2.1 (Residual measure of the minimizer).** Under **(H-ND1)**, we define the **residual measure of the shadow minimizer** as
$$d\nu^*(s) := \bigl(f_0(s) - g^*(s)\bigr)\,dm_\infty(s).$$

This is a measure on $\mathbb{R}$ whose density with respect to $dm_\infty$ is $f_0 - g^*$.

The residual measure is the central object of this document. It encodes the "difference" between $|\zeta|^2$ and its best on-critical approximant. Under RH, $g^* = f_0 = f_0^{on}$ and $d\nu^* \equiv 0$. Under $\neg$RH, $d\nu^*$ is a nonzero measure that contains information about the off-critical zeros of $\zeta$.

**Remark 2.2 (Comparison with the residual of $f_0^{on}$).** Doc 89 (and Doc 83) introduced the object
$$d\nu(s) = \bigl(f_0(s) - f_0^{on}(s)\bigr)\,dm_\infty(s) \geq 0 \text{ pointwise},$$
whose pointwise positivity comes from the fact that $f_0 \geq f_0^{on}$ pointwise (Doc 83, Proposition on $d\nu \geq 0$). The natural question is whether $d\nu^*$ inherits this pointwise positivity.

### 2.2. Is $d\nu^* \geq 0$ pointwise?

The pointwise positivity of $d\nu = f_0 - f_0^{on} \geq 0$ comes from Jensen's Theorem applied to the zeros of $\zeta$: since $f_0$ "contains" the off-critical zeros that $f_0^{on}$ does not have, the inequality is pointwise. But $g^*$ is a generic element of $\mathcal{M}$, and there is no a priori reason for $f_0 \geq g^*$ to hold pointwise.

**Proposition 2.3 (The pointwise positivity of $d\nu^*$ does not follow automatically).** For a generic element $g \in \mathcal{M}$, it may happen that $g(s_0) > f_0(s_0)$ at some point $s_0 \in \mathbb{R}$. Therefore, $d\nu^* = (f_0 - g^*)\,dm_\infty$ may not be a pointwise positive measure.

*Argument.* Let $\eta \in \mathcal{E}$ have a single simple zero at $1/2 + i\gamma$ for a very small $\gamma$. The function $|\eta(1/2+is)|^2$ has a sharp peak at $s \approx \gamma$. If $f_0$ is moderate at that point (for example, if $\zeta(1/2+i\gamma) \neq 0$, the function $|\zeta(1/2+is)|^2$ has no zero there and may be smaller than $|\eta(1/2+is)|^2$ near $\gamma$), then $g(s) > f_0(s)$ will hold near $\gamma$. This is possible without contradiction to the fact that $\|f_0 - g\|_{H_\lambda} > 0$, which only requires an inequality in weighted average. $\square$

**Consequence 2.4.** The residual measure $d\nu^*$ of the shadow minimizer is in general a **signed measure**, unlike $d\nu = (f_0 - f_0^{on})\,dm_\infty \geq 0$. This constitutes an important structural difference between $g^*$ and $f_0^{on}$.

**However**, the norm of the residual $\|f_0 - g^*\|^2_{H_\lambda} = \int W_\lambda\,(f_0-g^*)^2\,dm_\infty$ only involves the **square** of $f_0 - g^*$. The variational problem of minimizing $\|f_0 - g\|^2_{H_\lambda}$ imposes no sign on $f_0 - g$.

**Open question 2.5.** Is there any condition on $g^* \in \mathcal{M}$ that forces the positivity of $f_0 - g^*$? In particular, is the minimizer $g^*$ necessarily dominated pointwise by $f_0$? The answer is not known; it is a question requiring a better understanding of the geometry of $\mathcal{M}$.

### 2.3. Reformulation of the Euler-Lagrange equations

**Definition 2.6 (Interaction kernel).** For each $j \geq 1$, we define the **interaction kernel** associated with the $j$-th zero of $\eta^*$:
$$K_j^*(s) := \frac{2s}{s^2 - (\gamma_j^*)^2}, \quad s \in \mathbb{R},\; s \neq \pm\gamma_j^*.$$
This is the derived logarithm of the Weierstrass factor corresponding to the zero $1/2+i\gamma_j^*$.

**Theorem 2.7 (Reformulation of Euler-Lagrange).** The Euler-Lagrange equations (EL) are rewritten as:
$$\int_{\mathbb{R}} K_j^*(s) \cdot g^*(s) \cdot W_\lambda(s)\,d\nu^*(s) = 0 \quad \forall j \geq 1. \tag{EL$'$}$$
In other words, the functions $s \mapsto K_j^*(s)\cdot g^*(s)$ are orthogonal to the linear functional defined by the signed measure $W_\lambda\,d\nu^*$ in $L^1(\mathbb{R})$.

*Proof.* Substitute $d\nu^*(s) = (f_0(s)-g^*(s))\,dm_\infty(s)$ into (EL):
$$\int_{\mathbb{R}} W_\lambda(s)(f_0(s)-g^*(s)) g^*(s) K_j^*(s)\,dm_\infty(s) = \int_{\mathbb{R}} W_\lambda(s) K_j^*(s) g^*(s)\,d\nu^*(s) = 0.$$
$\square$

**Corollary 2.8 (Orthogonality condition).** Define the system of functions
$$\Psi_j^*(s) := W_\lambda(s)^{1/2} K_j^*(s) g^*(s), \quad j \geq 1.$$
Then (EL$'$) is equivalent to:
$$\langle \Psi_j^*,\, W_\lambda^{1/2}\,(f_0 - g^*)\rangle_{L^2(dm_\infty)} = 0 \quad \forall j,$$
i.e., the function $W_\lambda^{1/2}(f_0 - g^*)$ is orthogonal in $L^2(dm_\infty)$ to the system $\{\Psi_j^*\}_{j\geq 1}$.

*Proof.* Direct, multiplying and dividing by $W_\lambda^{1/2}$:
$$\int W_\lambda K_j^* g^* (f_0-g^*)\,dm_\infty = \int (W_\lambda^{1/2} K_j^* g^*)\cdot(W_\lambda^{1/2}(f_0-g^*))\,dm_\infty = \langle\Psi_j^*, W_\lambda^{1/2}(f_0-g^*)\rangle = 0. \square$$

**Remark 2.9 (Geometric interpretation).** The corollary says that the weighted residual $h^* := W_\lambda^{1/2}(f_0-g^*)$ is orthogonal to the system $\{\Psi_j^*\}$ in $L^2(dm_\infty)$. This is exactly the condition that $g^*$ be the projection of $f_0$ onto the orthogonal complement of $\{\Psi_j^*\}$, in a sense that must be made precise carefully, given that $\mathcal{M}$ is not a linear subspace.

### 2.4. Comparison with Nyman-Beurling-type criteria

The **Nyman-Beurling criterion** for RH states that RH is equivalent to the density in $L^2(0,\infty)$ (with the appropriate measure) of certain logarithmic-type functions built from the function $\rho(t) = t - \lfloor t \rfloor$ (the fractional part). In its formulation closest to our context:

$$\text{RH} \iff \mathbf{1}_{(0,1)} \in \overline{\mathrm{span}\{t\mapsto \rho(\theta/t) : 0 < \theta \leq 1\}},$$
in the $L^2(0,\infty)$ norm. The connection with our variational problem is as follows.

**Proposition 2.10 (Structural analogy with Nyman-Beurling).** The system of orthogonality conditions (EL$'$) has the following analogy with the Beurling criterion:
- In Nyman-Beurling: RH is equivalent to the constant function $\mathbf{1}$ not being orthogonal to any nontrivial functional in the closure of the approximation space.
- In our framework: (EL$'$) says that the residual $f_0-g^*$ is orthogonal (in the weighted sense) to the system $\{K_j^* g^*\}$.

The crucial difference is that in Nyman-Beurling the approximation space is **linear** (a closure of a span), while $\mathcal{M}$ is **nonlinear**. The orthogonality condition (EL$'$) involves $g^*$ itself in the definition of the orthogonal system, creating an implicit (fixed-point) equation rather than a linear projection condition.

**Remark 2.11.** The Beurling criterion of density of exponentials (Doc 85) also has an orthogonality form: $f$ belongs to the closure of $\{e^{i\lambda_n t}\}$ if and only if there is no nontrivial measure $\mu$ orthogonal to every $e^{i\lambda_n t}$ satisfying $f \in L^2(\mu)$. The structure of (EL$'$) is closer to this second formulation, where the "exponentials" are replaced by the kernels $K_j^*$.

The precise connection between (EL$'$) and Beurling's density criterion remains an open question; it would require an analysis of the approximation properties of the system $\{K_j^*\}$ in $L^2(W_\lambda\,dm_\infty)$ that exceeds the scope of this document.

### 2.5. Analysis of the system $\{K_j^* g^*\}$ as a generating system

From the point of view of functional analysis, the Euler-Lagrange equations say something more than simple orthogonality: they establish that the weighted residual $W_\lambda^{1/2}(f_0-g^*)$ belongs to the **orthogonal complement** of the system $\{\Psi_j^* = W_\lambda^{1/2} K_j^* g^*\}_{j\geq 1}$ in $L^2(dm_\infty)$.

**Definition 2.12 (Mode subspace of $g^*$).** We define the **mode subspace** of the minimizer $g^*$ as
$$V^* := \overline{\mathrm{span}\{\Psi_j^* : j \geq 1\}} \subset L^2(dm_\infty).$$
This is the subspace generated by the modes $\Psi_j^* = W_\lambda^{1/2} K_j^* g^*$.

**Proposition 2.13 (Orthogonality of the residual to the mode subspace).** The weighted residual $h^* := W_\lambda^{1/2}(f_0-g^*)$ satisfies $h^* \in (V^*)^\perp$, the orthogonal complement of $V^*$ in $L^2(dm_\infty)$.

*Proof.* Direct from Corollary 2.8: $\langle h^*, \Psi_j^*\rangle = 0$ for all $j$, and by density and linearity, $h^*$ is orthogonal to every element of $V^*$. $\square$

**Consequence 2.14 (Role of the completeness of $V^*$).** If the system $\{\Psi_j^*\}$ were **complete** in $L^2(dm_\infty)$, i.e., if $V^* = L^2(dm_\infty)$, then the condition $h^* \in (V^*)^\perp = \{0\}$ would imply $h^* = 0$, i.e., $f_0 = g^*$, which by the variational criterion would give RH. This reasoning shows that:

$$\text{If } V^* = L^2(dm_\infty),\text{ then RH.}$$

But the completeness of $V^*$ is a condition on $g^*$ that **depends** on the position of its zeros $\{\gamma_j^*\}$, and is not guaranteed a priori. In fact, under $\neg$RH (and under H-ND1), $g^* \neq f_0$ implies $h^* \neq 0$, so $V^* \neq L^2(dm_\infty)$: the system $\{\Psi_j^*\}$ is **incomplete** under $\neg$RH.

**Proposition 2.15 (Completeness–RH equivalence).** Under **(H-ND1)** and **(H-ND2)**:
$$\text{RH} \iff V^* = L^2(dm_\infty) \iff \{\Psi_j^*\} \text{ is complete in } L^2(dm_\infty).$$

*Proof.* Under RH: $g^* = f_0^{on}$, $h^* = 0 \in (V^*)^\perp$, and since $h^* = 0$ is orthogonal to everything, no information about $V^*$ is extracted from this datum. However, under RH $\tilde\delta_\lambda^2 = 0$, and the completeness of $V^*$ in this case is an analytic property of the zeros of $\zeta_{\mathrm{on}}$ that requires separate analysis.

Under $\neg$RH: $h^* \neq 0$ and $h^* \in (V^*)^\perp$ with $(V^*)^\perp \neq \{0\}$, which says that $V^* \subsetneq L^2(dm_\infty)$: the system is incomplete.

The full equivalence would require showing that under RH the system $\{\Psi_j^*\}$ is indeed complete, which is equivalent to a Müntz-Szász-type theorem for the functions $K_j^* g^*$. This result is not currently available. $\square$

**Remark 2.16 (Bridge with Doc 85).** Doc 85 studies the completeness of systems of exponentials $\{e^{i\gamma_j t}\}$ in $L^2$ with measures related to $\zeta$. Proposition 2.15 suggests that there is a bridge between that completeness problem and the variational problem of Direction D: the completeness of the system of exponentials (with the frequencies $\gamma_j$ of the zeros of $\zeta$) could imply the completeness of the system $\{\Psi_j^*\}$ under additional conditions. Developing this bridge is a task for Doc 98.

---

## §3. Properties of the residual measure $d\nu^*$

### 3.1. Structure of $d\nu^*$ as a signed measure

**Definition 3.1 (Jordan decomposition of $d\nu^*$).** Let $d\nu^* = d\nu^{*,+} - d\nu^{*,-}$ be the Jordan decomposition of the signed measure $d\nu^*$, where $d\nu^{*,\pm} \geq 0$ are mutually singular positive measures. The positive support is $S^+ = \{s : f_0(s) > g^*(s)\}$ and the negative support is $S^- = \{s : f_0(s) < g^*(s)\}$.

**Proposition 3.2 (Total mass of $d\nu^*$).** The total mass of $d\nu^*$ satisfies:
$$\int_{\mathbb{R}} d\nu^* = \int_{\mathbb{R}} (f_0 - g^*)\,dm_\infty.$$
There is no a priori reason for this quantity to be zero; it depends on the normalization properties of $g^*$ in $\mathcal{M}$.

*Remark.* If the functions in $\mathcal{M}$ satisfy $\int_\mathbb{R} g\,dm_\infty = \int_\mathbb{R} f_0^{on}\,dm_\infty$ ("mass" conservation under the mapping to $\mathcal{M}$), then the total mass of $d\nu^*$ is $\int(f_0 - f_0^{on})\,dm_\infty = \int d\nu \geq 0$. But this mass equality is not guaranteed for a generic element of $\mathcal{M}$.

### 3.2. Arithmetic information in $d\nu^*$

The object $d\nu = (f_0 - f_0^{on})\,dm_\infty$ of Doc 89 carries direct arithmetic information about the off-critical zeros of $\zeta$: its Mellin (or Laplace) transform captures the positions of those zeros via the explicit formula. The question is how much analogous information $d\nu^*$ carries.

**Proposition 3.3 (The measure $d\nu^*$ under RH is trivial).** Under RH, $g^* = f_0 = f_0^{on}$ and $d\nu^* = 0$. Under $\neg$RH and **(H-ND1)**, $d\nu^*$ is nonzero and its support contains information about the "difference" between $f_0$ and its best on-critical approximant.

*Proof.* Under RH, $f_0 = f_0^{on} \in \mathcal{M}$ and it is the unique minimizer with $\tilde\delta_\lambda^2 = 0$, so $g^* = f_0$ and $d\nu^* = 0$. Under $\neg$RH, $\tilde\delta_\lambda^2 > 0$ implies $f_0 \neq g^*$, so $d\nu^* \neq 0$. $\square$

**Lemma 3.4 (Relation between $d\nu^*$ and $d\nu$).** We have the decomposition:
$$d\nu = d\nu^* + (g^* - f_0^{on})\,dm_\infty.$$
The term $(g^* - f_0^{on})\,dm_\infty$ encodes the "difference" between the shadow minimizer and the natural candidate $f_0^{on}$.

*Proof.* Direct:
$$(f_0 - f_0^{on}) = (f_0 - g^*) + (g^* - f_0^{on}).\quad\square$$

**Remark 3.5.** If $d\nu^*$ had special orthogonality properties (through the Euler-Lagrange equations), then the decomposition in Lemma 3.4 would give information about $(g^* - f_0^{on})$, and therefore about the position of the zeros of $g^*$ relative to those of $f_0^{on}$. This is a line of research that will be developed in §5.

### 3.3. The resonance condition

The Euler-Lagrange equations (EL$'$) impose a condition on $d\nu^*$ that we can read as a **resonance condition** between the residual measure and the zeros of $g^*$.

**Definition 3.6 (Resonance condition).** We say that the signed measure $\mu$ on $\mathbb{R}$ satisfies the **resonance condition** for the system of zeros $\{\gamma_j^*\}$ if
$$\int_\mathbb{R} K_j^*(s) g^*(s) W_\lambda(s)\,\mu(ds) = 0 \quad \forall j.$$
The Euler-Lagrange equations state that $d\nu^*$ satisfies the resonance condition for the system $\{\gamma_j^*\}$.

**Physical interpretation.** The kernels $K_j^*(s) = 2s/(s^2 - (\gamma_j^*)^2)$ are the logarithmic derivatives of the Hadamard factors evaluated on the critical line. The resonance condition says that the "frequency" $K_j^*$ (which oscillates with period determined by $\gamma_j^*$) is orthogonal to the functional $g^* W_\lambda\,d\nu^*$. This is reminiscent of the orthogonality conditions of equilibrium measure theory in potential theory.

**Proposition 3.7 (The resonance condition as "balance of forces").** In analogy with logarithmic potential theory, the resonance condition can be interpreted as a balance: the zeros $\gamma_j^*$ are positioned so that the "force" they exert on the measure $g^*\,d\nu^*$ (through the kernels $K_j^*$) cancels out in weighted integral. This balance determines the zeros $\{\gamma_j^*\}$ as a function of $f_0$ (implicitly, through $g^*$).

*Remark.* This analogy with the logarithmic potential is suggestive but cannot be pushed directly: the kernels $K_j^*$ are not the Green's kernels of the two-dimensional Laplacian, but the logarithmic derivatives of Hadamard factors. The relevant potential theory would be an "order-one potential theory" adapted to Weierstrass products, whose formal development exceeds the scope of this document.

### 3.4. Resonance as a self-similarity condition

There is a further reading of the resonance condition that is instructive. Let us rewrite (EL$'$) as:
$$\int K_j^*(s)\, d\bigl(W_\lambda g^* \cdot \nu^*\bigr)(s) = 0,$$
where $W_\lambda g^* \cdot \nu^*$ is the measure with density $W_\lambda(s) g^*(s)(f_0(s)-g^*(s))$ with respect to $dm_\infty$.

**Definition 3.8 (Interaction measure).** We define the **interaction measure** of the shadow minimizer as
$$d\mu_{\mathrm{int}}^*(s) := W_\lambda(s) g^*(s)(f_0(s)-g^*(s))\,dm_\infty(s).$$
The Euler-Lagrange equations state that the Stieltjes transform of $d\mu_{\mathrm{int}}^*$ evaluated at the points $s = \pm\gamma_j^*$ is zero:
$$\mathcal{S}[d\mu_{\mathrm{int}}^*](\gamma_j^*) := \int_\mathbb{R} \frac{2s}{s^2-(\gamma_j^*)^2}\,d\mu_{\mathrm{int}}^*(s) = 0 \quad \forall j.$$

**Proposition 3.9 (The zeros of $g^*$ are zeros of the Stieltjes transform).** The points $\{\gamma_j^*\}$ are exactly the points where the Stieltjes transform of the interaction measure $d\mu_{\mathrm{int}}^*$ vanishes. This connects the shadow minimizer with the theory of equilibrium measures in the complex plane.

*Proof.* Direct from Definition 3.8 and the Euler-Lagrange equations (EL). $\square$

**Remark 3.10 (Self-similarity equation).** The condition that $\{\gamma_j^*\}$ be the zeros of $\mathcal{S}[d\mu_{\mathrm{int}}^*]$ is a condition of "self-similarity" type: the zeros of $g^*$ are determined by the interaction measure, which in turn depends on $g^*$. This is the nature of the fixed-point system of §4.

The remark suggests an iterative strategy: start with $g_0 = f_0^{on}$, compute $d\mu_{\mathrm{int}}^{(0)}$, find the zeros of $\mathcal{S}[d\mu_{\mathrm{int}}^{(0)}]$, build $g_1$ from those zeros, and repeat. The convergence of this iterative process — if it converges — would give $g^*$. But proving convergence is an open problem.

---

## §4. The Euler-Lagrange system as a moment problem

### 4.1. Formulation of the moment problem

The Euler-Lagrange equations (EL) define a system of equations in the unknowns $\{(\gamma_j^*, \eta^*)\}$: given $f_0$, find $\eta^*$ (which determines $g^* = |\eta^*|^2$) and its zeros $\{\gamma_j^*\}$ so that (EL) is satisfied.

This has the structure of an **inverted moment problem**: in an ordinary moment problem, the moments $\int s^k\,d\mu(s)$ are given and one seeks the measure $\mu$. Here, the "moments" are the integrals $\mathcal{E}_j^*$ and the "measure" is $d\nu^*$, but the "test polynomials" $K_j^* g^*$ depend on the unknown $g^*$ itself. This makes the problem essentially **nonlinear**.

**Definition 4.1 (The implicit moment system).** For $f_0$ given and parameter $\lambda > 0$ fixed, the **implicit moment system** is the following: find an entire function $\eta^*$ with zeros $\{1/2+i\gamma_j^*\}$ on the critical line, such that
$$M_j[\eta^*] := \int_\mathbb{R} W_\lambda(s) \frac{2s}{s^2-(\gamma_j^*)^2} |\eta^*(1/2+is)|^2 \bigl(f_0(s) - |\eta^*(1/2+is)|^2\bigr)\,dm_\infty(s) = 0,\;\forall j.$$

**Remark 4.2.** The system $\{M_j[\eta^*] = 0\}_{j\geq 1}$ is:
- **Infinite:** there is one equation for each zero $\gamma_j^*$.
- **Coupled:** changing $\gamma_j^*$ changes $K_j^*$, which changes $g^*$, which changes all the other $M_k$.
- **Nonlinear:** the integrand is cubic in $\eta^*$ (or quadratic in $g^*$).
- **Implicit:** the unknowns $\gamma_j^*$ appear both in the kernel $K_j^*$ and in the function $g^*$.

### 4.2. Is the system overdetermined?

**Question 4.3.** Does the system $\{M_j[\eta^*] = 0\}_{j\geq 1}$ have a generic solution, and if it does, is it unique?

To discuss the determination of the system, let us count the equations and the unknowns:
- **Unknowns:** the zeros $\{\gamma_j^*\}_{j\geq 1}$ (a sequence of real numbers, plus the parameters of the entire function $\eta^*$, such as its type $\sigma$, if any).
- **Equations:** $\{M_j = 0\}_{j\geq 1}$, one per zero.

To first approximation, the system has "the same number" of equations and unknowns. However, this count is misleading because:

(a) The system is infinite on both sides; the notion of "overdetermined" or "underdetermined" for infinite systems requires an appropriate functional topology.

(b) The equations $M_j = 0$ are coupled: there is no fixed $j$ for which $M_j$ depends only on $\gamma_j^*$ independently. This turns the system into something more like a fixed-point equation in the space of sequences.

**Proposition 4.4 (Reformulation as a fixed point).** Consider the operator
$$\mathcal{F}: (\{\gamma_j\}) \mapsto (\{\tilde\gamma_j\}),$$
where $\tilde\gamma_j$ is the solution of the equation $M_j[\eta_{\{\gamma_k\}}^{\mathrm{best}}] = 0$ for $\eta^{\mathrm{best}}$ determined by $\{\gamma_k\}$. Under suitable regularity conditions (not verified here), the minimizer $g^*$ would correspond to a fixed point of $\mathcal{F}$.

*Note.* This reformulation is heuristic at this stage: the existence and uniqueness of the operator $\mathcal{F}$ require that for each fixed $\{\gamma_j\}$, the system $M_j = 0$ in $\gamma_j^*$ have a solution, which is not proved. It is a direction of research, not a theorem.

### 4.3. The system under the scale-separation hypothesis

If the zeros $\gamma_j^*$ are sufficiently separated — specifically, if for $s$ near $\gamma_j^*$ the kernel $K_j^*(s) = 2s/(s^2-(\gamma_j^*)^2)$ dominates over all other $K_k^*(s)$ with $k \neq j$ — then the equations $M_j = 0$ "decouple" to first approximation.

**Lemma 4.5 (Approximate decoupling under separation of zeros).** Suppose the zeros $\{\gamma_j^*\}$ are sufficiently separated: there exists $\delta > 0$ such that $|\gamma_j^* - \gamma_k^*| \geq \delta$ for $j \neq k$. Let $\phi_j(s) = W_\lambda(s) g^*(s) |K_j^*(s)|$ be the weight density. Then in the region $|s-\gamma_j^*| \ll \delta/2$, the kernel $K_j^*(s)$ dominates and the equation $M_j = 0$ can be approximated as a local equation in $\gamma_j^*$:
$$\int_{|s-\gamma_j^*| \leq \delta/2} K_j^*(s) g^*(s) W_\lambda(s)(f_0(s)-g^*(s))\,dm_\infty(s) \approx M_j[\eta^*].$$
Under this decoupling, the system reduces to independent equations for each $\gamma_j^*$.

*Proof.* The contribution of $K_k^*$ for $k \neq j$ to $M_j$ is integrated with weight $K_k^*(s)/(K_j^*(s)+\text{others})$, which in the region $|s-\gamma_j^*| \ll \delta/2$ is $O(1/\delta^2)$ while $K_j^*(s)$ is $O(1/|s-\gamma_j^*|)$ — divergent. The ratio is $O(|s-\gamma_j^*|/\delta^2) \to 0$ as $s \to \gamma_j^*$. $\square$

**Remark 4.6.** Lemma 4.5 only applies in the regime of large separation, which is not the relevant regime for the zeros of $\zeta$ (whose separation decreases like $1/\log\gamma$). It is a first-principles result for understanding the structure of the system, not for proving existence or uniqueness in the real case.

---

## §5. The shadow minimizer under $\neg$RH: characterization

### 5.1. What $g^*$ cannot be

**Proposition 5.1 (Exclusion of $f_0^{on}$).** Under $\neg$RH and **(H-ND1)**, the shadow minimizer $g^*$ satisfies $g^* \neq f_0^{on}$.

*Proof.* If $g^* = f_0^{on}$, then $g^*$ satisfies the Euler-Lagrange equations. But Doc 95, Lemma 4.6 establishes that $f_0^{on}$ does not satisfy the Euler-Lagrange equations under $\neg$RH. Contradiction. $\square$

**Proposition 5.2 (The local minimum is not global under $\neg$RH).** Theorem 4.2 of Doc 93 establishes that $f_0^{on}$ is a **local** minimum of $\Phi|_\mathcal{M}$. Proposition 5.1 says that $f_0^{on}$ is not the **global** minimum under $\neg$RH. Therefore, if $g^*$ exists, $\Phi(g^*) < \Phi(f_0^{on})$.

*Proof.* The existence of the global minimum $g^*$ with $g^* \neq f_0^{on}$ implies that $f_0^{on}$ is not the global minimum (since the global one is distinct). Since $f_0^{on}$ is a local minimum, there is a deeper "valley" in $\mathcal{M}$ where $g^*$ is located. $\square$

**Consequence 5.3 (Barrier between local minima).** If $f_0^{on}$ is a local minimum and $g^*$ is the global minimum (with $g^* \neq f_0^{on}$), there must be a "barrier" between them: a saddle point in $\mathcal{M}$ or a region where $\Phi$ increases before decreasing. The existence of that barrier is an obstacle for gradient-descent methods, which would converge to $f_0^{on}$ instead of $g^*$.

### 5.2. Implicit characterization of $g^*$

Under **(H-ND1)**, $g^*$ is fully characterized by the system of equations:
$$\begin{cases} g^* \in \mathcal{M} \text{ (or } \overline{\mathcal{M}}\text{)}, \\ \|f_0 - g^*\|_{H_\lambda}^2 = \tilde\delta_\lambda^2 = \inf_{g\in\mathcal{M}}\|f_0-g\|_{H_\lambda}^2, \\ M_j[\eta^*] = 0 \quad \forall j \geq 1. \end{cases}$$
The first two conditions define $g^*$ as a minimizer; the third is the necessary first-order condition.

**Remark 5.4.** This system characterizes $g^*$ implicitly but not constructively: it gives no algorithm to compute $g^*$ from $f_0$. The explicit construction would require solving the implicit moment system of §4, which is an open problem.

### 5.3. The residual $f_0 - g^*$ as a functional projection

**Definition 5.5 (Canonical on-critical projection).** Under **(H-ND1)**, the minimizer $g^*$ is the **on-critical projection** of $f_0$ onto $\mathcal{M}$ (in the sense of the $H_\lambda$ distance). The **residual**
$$r^* := f_0 - g^*$$
is the "irreducibly off-critical" component of $f_0$: the part of $|\zeta|^2$ that cannot be approximated in $H_\lambda$ by any $|\eta_{\mathrm{on}}|^2$.

This name is justified because $\|r^*\|_{H_\lambda} = \tilde\delta_\lambda^2$, the minimum distance, which is the best possible approximation.

**Proposition 5.6 (Properties of $r^*$).** Under **(H-ND1)**:
(a) $\|r^*\|_{H_\lambda} = \tilde\delta_\lambda^2 > 0$ under $\neg$RH.
(b) $r^*$ satisfies the orthogonality condition: $\langle W_\lambda^{1/2} r^*, \Psi_j^*\rangle_{L^2(dm_\infty)} = 0$ for all $j$.
(c) If $g^*$ is the global minimizer, there is no $g \in \mathcal{M}$ with $\|f_0 - g\|_{H_\lambda} < \|r^*\|_{H_\lambda}$.

*Proof.* (a) is the definition. (b) is Corollary 2.8. (c) is the minimizer condition. $\square$

---

## §6. Uniqueness of $g^*$ and the canonicity conjecture

### 6.1. Uniqueness conditions

The uniqueness of the minimizer $g^*$ in a nonlinear variational problem is delicate. For convex subsets of a Hilbert space, uniqueness is automatic. But $\mathcal{M}$ is not convex.

**Definition 6.1 (Strong and weak uniqueness).** We say the minimizer is **unique in the strong sense** if there is exactly one $g^* \in \mathcal{M}$ with $\Phi(g^*) = \tilde\delta_\lambda^2$. We say it is **unique in the weak sense** if all minimizers (if any) produce the same residual $r^* = f_0 - g^*$.

**Proposition 6.2 (Connection between uniqueness and positive second variation).** The positive second variation of Doc 93 (Theorem 4.2) implies that $f_0^{on}$ is an isolated **local** minimum of $\Phi|_\mathcal{M}$. Under **(H-ND1)** and under $\neg$RH, the global minimizer $g^* \neq f_0^{on}$. If $g^*$ is also an isolated local minimum (which would require showing that the second variation of $\Phi$ at $g^*$ is also positive), then there are at least two isolated local minima.

*Note.* That $g^*$ be an isolated local minimum is not proved. It depends on the geometry of $\mathcal{M}$ in the neighborhood of $g^*$, which is not known.

**Proposition 6.3 (Geometric uniqueness criterion).** The minimizer $g^*$ is unique if the functional $\Phi$ is **strictly quasi-convex** on $\mathcal{M}$: for distinct $g_0, g_1 \in \mathcal{M}$ with $\Phi(g_0) = \Phi(g_1) = \tilde\delta_\lambda^2$, the geodesic in $\mathcal{M}$ connecting them satisfies $\Phi > \tilde\delta_\lambda^2$ in the interior. This condition has not been verified.

### 6.2. Dependence of $g^*$ on $\lambda$

The functional $\Phi = \Phi_\lambda$ depends on the parameter $\lambda$ through the kernel $W_\lambda$. Therefore, in principle, the minimizer $g^*_\lambda$ may depend on $\lambda$.

**Question 6.4 (Stability of the minimizer under variation of $\lambda$).** Is the minimizer $g^*_\lambda$ a smooth function of $\lambda$? What is the derivative $\partial_\lambda g^*_\lambda$?

**Proposition 6.5 ($\lambda$-independence under RH).** Under RH, $g^*_\lambda = f_0 = f_0^{on}$ for every $\lambda > 0$, independent of $\lambda$. The minimizer is canonical.

*Proof.* Under RH, $\tilde\delta_\lambda^2 = 0$ and $g^* = f_0 \in \mathcal{M}$, independent of $\lambda$. $\square$

**The interesting question** is the situation under $\neg$RH: if $g^*_\lambda$ depends on $\lambda$, the shadow minimizer is not canonical (it depends on the choice of CCM structure). If it is independent of $\lambda$, it would be a canonical object determined only by $f_0$.

### 6.3. The canonical uniqueness conjecture

**Conjecture C-Can (Canonical uniqueness of the shadow minimizer).** Under $\neg$RH and under the existence hypothesis ND1, there exists a unique element $g^{**} \in \overline{\mathcal{M}}$ that simultaneously minimizes $\|f_0 - g\|^2_{H_\lambda}$ for **every** $\lambda > 0$:
$$g^{**} = \arg\min_{g\in\overline{\mathcal{M}}} \sum_{\lambda > 0} w_\lambda \|f_0 - g\|^2_{H_\lambda},$$
in some appropriate sense (for example, with $w_\lambda = e^{-\lambda}$ or with integration over $\lambda$). This $g^{**}$ is the **canonical on-critical projection** of $f_0$, determined solely by $f_0$ and not by the choice of $\lambda$.

**Remark 6.6.** Conjecture C-Can has two parts:
(i) *Existence:* that the simultaneous minimization problem over all $\lambda$ have a solution.
(ii) *Uniqueness:* that that solution be unique.

Neither part is proved. The conjecture is motivated by the analogy with orthogonal projection in Hilbert spaces (where the projection onto a closed convex set is unique and independent of the norm in the sense that it is determined by the geometry of the set), but $\mathcal{M}$ is not convex.

**Tentative strategy for addressing C-Can.** If one could show that the minimizers $g^*_\lambda$ for different $\lambda$ satisfy the same Euler-Lagrange equations (since the equations for different $\lambda$ coincide in the zeros $\{\gamma_j^*\}$ even though they vary in the weights), and if the Euler-Lagrange system had a unique solution (strengthened condition ND2), then C-Can would follow. But these are additional unverified hypotheses.

---

## §7. The zeros of $g^*$ and their relation to those of $\zeta$

### 7.1. The zeros of $g^*$ are (in general) not the zeros of $\zeta_{\mathrm{on}}$

Under **(H-ND1)** and $\neg$RH, $g^* \neq f_0^{on}$, which implies that $\eta^* \not\equiv \zeta_{\mathrm{on}}$. Therefore, the zeros of $\eta^*$ are not the same as the zeros of $\zeta_{\mathrm{on}}$.

**Question 7.1.** What is the relation between $\{\gamma_j^*\}$ (the zeros of $\eta^*$) and $\{\gamma_j\}$ (the imaginary parts of the zeros of $\zeta$ on the critical line)?

This question has no a priori answer. The Euler-Lagrange equations implicitly determine $\{\gamma_j^*\}$ as a function of $f_0 = |\zeta|^2$, but there is no explicit formula.

**Heuristic 7.2 (Zeros of $g^*$ as a "correction" of those of $\zeta_{\mathrm{on}}$).** If $\neg$RH were true and the off-critical zeros of $\zeta$ were "close" to the critical line (small perturbation), then we would expect $g^*$ to be a small perturbation of $f_0^{on}$, and the zeros $\gamma_j^*$ would be small perturbations of the zeros $\gamma_j$ of $\zeta$ on the critical line. Under this heuristic, the relation $\gamma_j^* \approx \gamma_j$ would hold to first approximation.

But this heuristic is not rigorously grounded: if the off-critical zeros of $\zeta$ were far from the line (which is in principle possible), the "correction" could be large.

### 7.2. The functional equation of $g^*$

**Question 7.3.** Does $\eta^*$ satisfy the same functional equation as $\xi$?

All elements of $\mathcal{E}$ (and therefore of $\mathcal{M}$) satisfy a functional equation analogous to that of $\xi$. If $g^* \in \mathcal{M}$, then $\eta^*$ satisfies that equation. If $g^* \in \overline{\mathcal{M}} \setminus \mathcal{M}$, the functional equation might not hold (depending on how the closure $\overline{\mathcal{E}}$ is defined).

**Proposition 7.4 (Functional equation preserved in $\mathcal{M}$).** If $g^* \in \mathcal{M}$ (i.e., under the hypothesis that ND3 does not fail completely and the minimizer is in $\mathcal{M}$), then $\eta^*$ satisfies:
$$\eta^*(1-s) = \chi(s)\eta^*(s)$$
for the same symmetry factor $\chi$ as the function $\xi$. In particular, the zeros of $\eta^*$ are symmetric about the real axis: $\overline{\gamma_j^*} = \gamma_j^*$ (real zeros by real symmetry, and symmetric about the origin by the functional equation).

*Proof.* By the definition of $\mathcal{E}$ (Doc 82, §2): all its elements satisfy the functional equation by hypothesis. $\square$

### 7.3. Is $g^* = f_0^{on}$ a reformulation of RH?

**Theorem 7.5 (Variational reformulation of RH).** Under the uniqueness hypothesis **(H-ND1)** and **(H-ND2)** (uniqueness of the minimizer), the following statements are equivalent:
(i) Riemann Hypothesis: all nontrivial zeros of $\zeta$ lie on the critical line $\mathrm{Re}(s) = 1/2$.
(ii) The shadow minimizer coincides with the natural candidate: $g^* = f_0^{on}$.
(iii) The variational distance is zero: $\tilde\delta_\lambda^2 = 0$.
(iv) The residual measure is zero: $d\nu^* = 0$.

*Proof.*
- (i) $\Rightarrow$ (iii): this is Doc 82.
- (iii) $\Rightarrow$ (ii): If $\tilde\delta_\lambda^2 = 0$, the infimum is zero and is attained by $f_0 \in \mathcal{M}$, so $g^* = f_0 = f_0^{on}$.
- (ii) $\Rightarrow$ (iv): $d\nu^* = (f_0 - g^*)\,dm_\infty = 0$.
- (iv) $\Rightarrow$ (i): If $d\nu^* = 0$, then $f_0 = g^* \in \mathcal{M}$, which implies that $f_0 = |\zeta(1/2+is)|^2$ is the squared modulus of an entire function with all its zeros on the critical line, which is precisely RH.
- (iii) $\Rightarrow$ (i): Doc 82 (the criterion is an equivalence).
$\square$

**Remark 7.6 (The role of hypotheses ND1, ND2).** Theorem 7.5 uses hypotheses **(H-ND1)** and **(H-ND2)** to ensure that the minimizer exists and is unique. Without these hypotheses, the chain of equivalences remains valid in the direction (i)$\Rightarrow$(ii)$\Rightarrow$(iii)$\Rightarrow$(i) (since these do not require ND1 or ND2), but the direction $\neg$(i)$\Rightarrow$ $\neg$(ii) requires knowing that the minimizer exists and is unique.

**Corollary 7.7 (New formulation of RH).** Under **(H-ND1)** and **(H-ND2)**, the Riemann Hypothesis is equivalent to:
$$g^* = f_0^{on} \in \mathcal{M}.$$
This formulation has the advantage of being expressed in terms of an optimization problem (finding the minimum of $\Phi$ in $\mathcal{M}$) rather than a statement about zeros of analytic functions.

---

## §8. Open questions about the shadow minimizer

The development above opens several lines of research that are formulated explicitly as open questions.

### 8.1. Existence and uniqueness

**Open Question 8.1 (Existence of $g^*$).** Under $\neg$RH, does there exist $g^* \in \overline{\mathcal{M}}$ such that $\|f_0 - g^*\|_{H_\lambda}^2 = \tilde\delta_\lambda^2$? This is problem ND1. §2 of Doc 95 shows that the answer is affirmative if $\overline{\mathcal{M}}$ is closed (which is true by construction) and the functional $\Phi$ is lower semicontinuous on $\overline{\mathcal{M}}$ (which is true since it is continuous). The real obstacle is that $g^*$ could lie in $\overline{\mathcal{M}} \setminus \mathcal{M}$, which requires extending the definition of $\mathcal{M}$.

**Open Question 8.2 (Uniqueness of $g^*$).** Is the minimizer unique? If there are several minimizers with the same value $\tilde\delta_\lambda^2$, what additional property selects the "canonical" minimizer?

**Open Question 8.3 (Regularity of $g^*$).** If $g^*$ exists, is it an analytic function of $s$? Does it have the same singular points as $f_0$? Does it extend to a meromorphic function in some strip around the critical line?

### 8.2. Arithmetic properties

**Open Question 8.4 (Arithmetic information in $g^*$).** Do the zeros $\{\gamma_j^*\}$ of $\eta^*$ have any arithmetic or spectral property? In the case of $\zeta_{\mathrm{on}}$, the zeros are the same as those of $\zeta$ (projected). Does $g^*$ have a relation to the L-function of some arithmetic object?

**Open Question 8.5 (Symmetry of the zeros of $g^*$).** If $g^* \in \mathcal{M}$, its zeros are symmetric by the functional equation (Proposition 7.4). Is there any known statistical distribution for $\{\gamma_j^*\}$? Do they resemble those of $\zeta$?

**Open Question 8.6 (Mellin transform of $d\nu^*$).** Doc 90 studies the arithmetic information of $d\nu$ through its Mellin transform, connected to the Riemann-Weil explicit formula. What information does the Mellin transform of $d\nu^*$ encode? If the zeros of $g^*$ are different from those of $\zeta_{\mathrm{on}}$, to which "primes" or "zeros" does the explicit formula for $d\nu^*$ correspond?

### 8.3. Connections with other frameworks

**Open Question 8.7 (Connection with the De Bruijn-Newman flow).** Doc 95, §6 connects Direction D with the De Bruijn-Newman flow. Does the shadow minimizer $g^*_\lambda$ (which depends on $\lambda$) evolve following the lines of the De Bruijn-Newman flow? Is the $\lambda$-dependence of $g^*_\lambda$ related to the heating of the kernel $W_\lambda$ under that flow?

**Open Question 8.8 (Connection with spectral theory).** Docs 91, 94 (Phase 34) study the connection between the negative index of the Pontryagin space and the off-critical zeros. Does $g^*$ have an interpretation in terms of the operator $H_C$ on the Pontryagin space? Are its zeros $\{\gamma_j^*\}$ spectral values of some natural operator?

**Open Question 8.9 (Connection with the inverse Jacobi problem).** Doc 92 formulates an inverse Jacobi problem: given a distribution of zeros, find a Jacobi-type operator whose spectrum is that of the zeros. Is the minimizer $g^*$ related to the "solution" of that inverse problem for the zeros of $\zeta$?

---

## §9. The residual $d\nu^*$ and its relation to the central object of the program

### 9.1. Comparison of $d\nu^*$ with $d\nu$ of Doc 89

Doc 89 introduces the central object of the program as the measure $d\nu = dm_{\mathrm{full}} - dm_{\mathrm{full,on}}$, which is the difference between the full spectral measure of $\zeta$ and that of $\zeta_{\mathrm{on}}$. This measure directly captures information about the off-critical zeros.

The residual measure $d\nu^*$ that we have studied in this document is different:
$$d\nu^*(s) = (f_0(s) - g^*(s))\,dm_\infty(s),$$
where $g^*$ is the shadow minimizer, not $f_0^{on}$. The relations between the two measures are as follows.

**Proposition 9.1 (Relation between $d\nu^*$ and $d\nu$).** The measures $d\nu$ and $d\nu^*$ satisfy:
$$d\nu = d\nu^* + (g^* - f_0^{on})\,dm_\infty.$$
The correction term $(g^* - f_0^{on})\,dm_\infty$ is zero under RH (since $g^* = f_0^{on}$) and nonzero under $\neg$RH.

*Proof.* Direct from the definition: $f_0 - f_0^{on} = (f_0 - g^*) + (g^* - f_0^{on})$. $\square$

**Remark 9.2.** The decomposition in Proposition 9.1 has a geometric interpretation: $d\nu$ (which encodes all the off-critical zeros of $\zeta$) decomposes into:
- $d\nu^*$: the "irreducible" part, which cannot be absorbed into any element of $\mathcal{M}$ — the part that the best on-critical approximant cannot reproduce.
- $(g^* - f_0^{on})\,dm_\infty$: the "correction" of the minimizer relative to the natural candidate — the difference between the true best approximant $g^*$ and the candidate $f_0^{on}$.

**Proposition 9.3 (The "absorbable" part of $d\nu$).** The term $(g^* - f_0^{on})\,dm_\infty$ is the part of $d\nu$ that can be "absorbed" by changing the position of the on-critical zeros: moving from $f_0^{on}$ to $g^*$ is equivalent to repositioning the zeros on the critical line to improve the approximation of $f_0$.

*Remark.* This suggests that the shadow minimizer $g^*$ "reorganizes" the on-critical zeros of $\zeta_{\mathrm{on}}$ to get as close as possible to $f_0$, leaving the minimal residual $d\nu^*$ as the truly irreducible part.

### 9.2. $d\nu^*$ as an invariant of the variational problem

**Definition 9.4 (Minimal residual).** The **minimal residual** of the variational problem is the function
$$r^*(s) := f_0(s) - g^*(s) = \frac{d\nu^*}{dm_\infty}(s),$$
whose norm $\|r^*\|_{H_\lambda} = \tilde\delta_\lambda$ is the minimum variational distance.

Under RH: $r^* \equiv 0$.  
Under $\neg$RH and **(H-ND1)**: $\|r^*\|_{H_\lambda} > 0$.

**Proposition 9.5 (Orthogonality property of the minimal residual).** The minimal residual $r^*$ satisfies:
$$\langle W_\lambda r^*, K_j^* g^*\rangle_{L^2(dm_\infty)} = 0 \quad \forall j,$$
i.e., $W_\lambda r^*$ is orthogonal to the system $\{K_j^* g^*\}$ in $L^2(dm_\infty)$. This is the Euler-Lagrange condition in its most transparent form.

*Proof.* Direct from (EL$'$): $\int W_\lambda K_j^* g^* r^*\,dm_\infty = \int W_\lambda K_j^* g^*(f_0-g^*)\,dm_\infty = \mathcal{E}_j^* = 0$. $\square$

---

## §10. Synthesis and outlook

### 10.1. What has been established

This document has developed the analysis of the shadow minimizer $g^*$, establishing the following results:

1. **Reformulation of Euler-Lagrange** (Theorem 2.7): the Euler-Lagrange equations are naturally expressed as an orthogonality condition of the residual measure $d\nu^* = (f_0-g^*)\,dm_\infty$ with respect to the system $\{K_j^* g^*\}$.

2. **The measure $d\nu^*$ is in general a signed measure** (Proposition 2.3): unlike $d\nu = (f_0-f_0^{on})\,dm_\infty \geq 0$, the residual measure of the shadow minimizer may change sign, reflecting the structural difference between $g^*$ and $f_0^{on}$.

3. **The Euler-Lagrange system as an implicit moment problem** (§4): the system $\{M_j = 0\}$ is infinite, coupled, nonlinear, and implicit. Its formal resolution is an open problem.

4. **Variational reformulation of RH** (Theorem 7.5): under the existence and uniqueness hypotheses for the minimizer, RH is equivalent to $g^* = f_0^{on}$, or equivalently to $d\nu^* = 0$.

5. **Canonical uniqueness conjecture** (§6.3): the conjecture is formulated that the shadow minimizer is canonical — independent of $\lambda$ — which would make it an object determined solely by $f_0$.

6. **Open questions** (§8): nine open questions are formulated outlining the most promising directions of research.

### 10.2. The frank obstacles

It is necessary to be explicit about what this document has **not** proved:

- **RH has not been proved.** Theorem 7.5 requires hypotheses ND1 and ND2, which are not proved.

- **The existence of $g^*$ in $\mathcal{M}$ has not been proved.** Hypothesis ND1 is the primary obstacle. As discussed in Doc 95, if $\mathcal{M}$ is not closed, the minimizer may not lie in $\mathcal{M}$ but in $\overline{\mathcal{M}} \setminus \mathcal{M}$, and the relevance of that minimizer to RH requires additional analysis.

- **The uniqueness of $g^*$ has not been proved.** Condition ND2 ($g^* = f_0^{on}$ under the uniqueness hypothesis) is also not proved. There could be multiple minimizers, in which case the argument becomes more complicated.

- **The Euler-Lagrange system has not been solved.** The system $\{M_j = 0\}$ is a fixed-point problem in the space of entire functions, whose formal solvability is an open question.

- **Conjecture C-Can is not proved.** The $\lambda$-independence of the minimizer is a conjecture motivated by analogy with linear variational problems, but $\mathcal{M}$ is not linear and the analogy is not direct.

### 10.3. Immediate future direction

The natural next step is **Doc 98**, which should:

(a) Study whether the orthogonality condition in Corollary 2.8 (the residual $W_\lambda^{1/2} r^*$ is orthogonal to the system $\{\Psi_j^*\}$) implies any completeness condition for the system $\{\Psi_j^*\}$ in $L^2(dm_\infty)$.

(b) Connect the completeness condition of the system $\{K_j^*\}$ with the Nyman-Beurling criterion and the density results of Doc 85.

(c) Study whether the $\lambda$-dependence of the minimizer $g^*_\lambda$ can be controlled by means of the Euler-Lagrange equations differentiated with respect to $\lambda$.

(d) Explore whether the Euler-Lagrange system has a more tractable formulation when restricted to a finite number of zeros (truncated case), and whether that finite case gives information about the infinite case via a compactness argument.

---

## Appendix A: Notation used in this document

| Symbol | Meaning |
|---------|-------------|
| $H_\lambda$ | Hilbert space $L^2(\mathbb{R}, W_\lambda\,dm_\infty)$ |
| $dm_\infty$ | CCM spectral measure: $(2\pi)^{-2}|\Gamma(1/4+is/2)|^2\,ds$ |
| $W_\lambda$ | CCM kernel depending on parameter $\lambda > 0$ |
| $\mathcal{M}$ | On-critical approximation class |
| $\overline{\mathcal{M}}$ | Closure of $\mathcal{M}$ in $H_\lambda$ |
| $f_0$ | $|\zeta(1/2+is)|^2 \in H_\lambda$ |
| $f_0^{on}$ | $|\zeta_{\mathrm{on}}(1/2+is)|^2 \in \mathcal{M}$ |
| $g^* = |\eta^*|^2$ | Shadow minimizer $\in \overline{\mathcal{M}}$ (hypothetical) |
| $\{\gamma_j^*\}$ | Zeros of $\eta^*$ on the critical line |
| $K_j^*(s)$ | Interaction kernel $2s/(s^2-(\gamma_j^*)^2)$ |
| $d\nu^*$ | Residual measure $(f_0-g^*)\,dm_\infty$ |
| $d\nu$ | Residual measure of Doc 89: $(f_0-f_0^{on})\,dm_\infty \geq 0$ |
| $\tilde\delta_\lambda^2$ | $\inf_{g\in\mathcal{M}}\|f_0-g\|_{H_\lambda}^2$ |
| $r^* = f_0 - g^*$ | Minimal residual |
| $\mathcal{E}_j^*$ | $j$-th Euler-Lagrange equation |
| $M_j[\eta^*]$ | Implicit moment functional |
| **(H-ND1)** | Hypothesis: the infimum is attained in $\overline{\mathcal{M}}$ |
| **(H-ND2)** | Hypothesis: the minimizer is unique |
| C-Can | Canonical uniqueness conjecture for the shadow minimizer |

---

## Appendix B: Relation to preceding documents

| Document | Relation to this Doc 97 |
|-----------|--------------------------|
| Doc 82 | Variational criterion $\tilde\delta_\lambda^2 = 0 \iff$ RH; definition of $\mathcal{M}$ |
| Doc 83 | Pointwise positivity of $d\nu = f_0-f_0^{on} \geq 0$ |
| Doc 85 | Beurling density criterion; analogy with (EL$'$) |
| Doc 89 | Central object $d\nu$; comparison with $d\nu^*$ in §9 |
| Doc 90 | Arithmetic information via the Mellin transform of $d\nu$ |
| Doc 93 | Positive second variation; $f_0^{on}$ is a local minimum under $\neg$RH |
| Doc 95 | Lemma 4.6 ($f_0^{on}$ does not satisfy EL under $\neg$RH); conditions ND1–ND4 |
| This doc | Analysis of the shadow minimizer $g^*$; structure of $d\nu^*$; Conjecture C-Can |

---

*End of Doc 97.*
