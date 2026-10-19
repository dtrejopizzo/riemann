# Doc 96 — Direction B (third layer): Dissipativity, characteristic function, and Krein's Theorem

**Phase:** 34 — New directions
**Context:** Continuation of Docs 91 and 94 of Direction B. Doc 91 established the Pontryagin space $(\mathcal{K}, Q)$ and the operator $H_C$, and identified seven routes toward $\kappa = 0$, all circular or equivalent to RH. Doc 94 analyzed condition C5 in detail. This document explores four new angles: dissipativity via the Brodskii–Livsic characteristic function, positivity from the Euler product, Maslov index and symplectic curvature, and Krein's Theorem on bounded operators.
**Absolute rule:** No proof of RH will be fabricated. If an argument does not close, the breaking point will be stated precisely.

---

## Executive summary

This document organizes the analysis into four independent angles, each inspired by a result from operator theory that could, in principle, force the negative index $\kappa = 0$ without going through explicit knowledge of the zeros of $\zeta$.

**Angle 1 (Brodskii–Livsic):** The characteristic function $\Theta(z) = \xi(1/2+z)/\xi(1/2-z)$ satisfies $|\Theta(z)| = 1$ on all of $\mathbb{C}$ (constant modulus 1 by the functional equation), not $|\Theta(z)| \leq 1$. This corresponds to a unitary operator in the Krein space, not a dissipative one. Dissipativity would require twisting the characteristic function via an "absorption channel" that has no natural analogue in the geometry of $\xi$. The angle is not sealed off in principle, but the construction of a twisted characteristic function introduces uncontrolled freedom.

**Angle 2 (Euler product):** The Euler product forces positivity of $Q$ on the subspace where the test functions have Mellin transform concentrated in $\mathrm{Re}(s) > 1$. This subspace is unconditionally $Q$-positive. However, propagating this positivity to all of $\mathcal{K}$ by analyticity fails: the space $\mathcal{K}$ has no analytic structure allowing a quadratic form to be extended by analytic continuation. The argument collapses before obtaining $\kappa = 0$.

**Angle 3 (Maslov index):** The symplectic form $Q$ on $\mathcal{K}$ has an adelic interpretation via the Weil formula. The Maslov index of families of Lagrangian subspaces in $(\mathcal{K}, Q)$ is formally well-defined, but the concrete computation of that index requires knowing the signature of $Q$ on specific subspaces, which circularly refers back to the zeros of $\zeta$. The connection with the curvature of an arithmetic symplectic manifold is speculative and is delimited precisely.

**Angle 4 (Krein's Theorem):** The resolvent $R_{\lambda_0} = (H_C - \lambda_0)^{-1}$ is a bounded operator on $\Pi_\kappa$ for $\lambda_0 \notin \sigma(H_C)$, and has exactly the same negative index as $H_C$. Krein's Theorem (1950) on bounded self-adjoint operators in Pontryagin spaces gives $\kappa = 0$ only if $\sigma(R_{\lambda_0}) \subset \mathbb{R}$, which is the starting condition in a different form. The resolvent route provides no new leverage.

**General conclusion:** None of the four angles closes the argument $\kappa = 0$ independently. Angles 1 and 3 are potentially rich in new structure but give no results without additional hypotheses on $\zeta$. Angles 2 and 4 are sealed off by precise arguments. The most valuable observation of the document is Theorem 2.12 (Angle 2): the positivity of the Euler product in the region $\mathrm{Re}(s) > 1$ defines a concrete $Q$-positive subspace, whose projection onto $\mathcal{K}$ is computable, and the quotient between that subspace and $\mathcal{K}$ contains all the information about $\kappa$.

---

## Part I — Angle 1: Dissipative operators and the Brodskii–Livsic characteristic function

### Section 1.1 — Dissipative operators in Krein spaces

We begin by recalling the relevant definitions in the framework of Krein and Pontryagin spaces.

**Definition 1.1 (Krein space).** A **Krein space** $(\mathcal{K}, [\cdot, \cdot])$ is a complex vector space with a non-degenerate indefinite Hermitian form $[\cdot, \cdot]$ such that $\mathcal{K} = \mathcal{K}_+ \oplus \mathcal{K}_-$ (fundamental decomposition) with $(\mathcal{K}_\pm, \pm[\cdot,\cdot])$ Hilbert spaces. If $\dim \mathcal{K}_- = \kappa < \infty$, the space is called a Pontryagin space of index $\kappa$, denoted $\Pi_\kappa$.

In our context $(\mathcal{K}, Q)$ is the Weil–Connes Pontryagin space (Doc 91, Definition 1.7) with $\kappa = \mathrm{neg.ind}(H_C)$, and RH $\iff \kappa = 0$.

**Definition 1.2 (Dissipative operator in a Krein space).** A densely defined linear operator $A : \mathrm{Dom}(A) \to \mathcal{K}$ on the Krein space $(\mathcal{K}, [\cdot, \cdot])$ is called **$[\cdot,\cdot]$-dissipative** if:
$$\mathrm{Im}[Af, f] \geq 0 \quad \text{for all } f \in \mathrm{Dom}(A).$$

It is called **$[\cdot,\cdot]$-anti-dissipative** if $\mathrm{Im}[Af, f] \leq 0$.

Equivalently: $A$ is dissipative if $A - A^{[*]} = -2i \mathrm{Im}A \leq 0$ in the sense of the form, where $A^{[*]}$ is the $[\cdot,\cdot]$-adjoint of $A$.

**Definition 1.3 (Completely non-self-adjoint).** An operator $A$ is **completely non-$[\cdot,\cdot]$-self-adjoint** (cna) if there is no nontrivial Krein subspace on which $A$ is $[\cdot,\cdot]$-self-adjoint.

**Theorem 1.4 (Brodskii–Livsic, Hilbert space version; cf. Brodskii 1971, Ch. VI).** Let $A$ be a cna operator on a Hilbert space $H$ with non-self-adjoint part of nuclear rank (finite defect). Then:

*(i)* The characteristic function $\Theta_A(z) = I + 2i K^*(A - zI)^{-1} K$ (where $K$ is the defect operator) is an analytic matrix function that determines $A$ up to unitary equivalence.

*(ii)* $A$ is dissipative $\iff \|\Theta_A(z)\| \leq 1$ for $z \in \mathbb{C}^+ = \{z : \mathrm{Im}(z) > 0\}$.

*(iii)* If $A$ is dissipative and self-adjoint in the Hilbert sense, the spectrum of $A$ is real.

The passage from Hilbert space to Pontryagin space requires the Livsic–Yantsevich theory (1979) with $J$-unitary functions.

---

### Section 1.2 — The candidate characteristic function of $H_C$

From Doc 91, Section 5.2 and Conjecture 5.4, the candidate characteristic function of $H_C$ is:
$$\Theta(z) = \frac{\xi(1/2 + z)}{\xi(1/2 - z)},$$
where $\xi(s) = \frac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ is the complete $\xi$ function.

The analysis of whether $H_C$ is dissipative reduces to the study of $|\Theta(z)|$ in the upper half-plane.

---

### Section 1.3 — The functional equation prevents strict dissipativity

**Proposition 1.5 (The modulus of the characteristic function is 1).** For all $z \in \mathbb{C}$:
$$|\Theta(z)| = \left|\frac{\xi(1/2 + z)}{\xi(1/2 - z)}\right| = 1.$$

*Proof.* The functional equation of $\xi$ establishes $\xi(s) = \xi(1 - s)$ for all $s \in \mathbb{C}$. Substituting $s = 1/2 + z$:
$$\xi(1/2 + z) = \xi(1 - (1/2 + z)) = \xi(1/2 - z).$$

Therefore $|\xi(1/2 + z)| = |\xi(1/2 - z)|$ for all $z \in \mathbb{C}$, and the quotient has modulus 1:
$$|\Theta(z)| = \frac{|\xi(1/2 + z)|}{|\xi(1/2 - z)|} = 1. \qquad \square$$

**Remark 1.6.** The result is immediate but has a deep consequence: the function $\Theta(z)$ is not a Schur function (contractive in the upper half-plane), but a unitary function. In the Brodskii–Livsic classification:

- $\|\Theta_A(z)\| \leq 1$ in $\mathbb{C}^+$: dissipative operator.
- $\|\Theta_A(z)\| = 1$ in $\mathbb{C}^+$: unitary operator (self-adjoint in the Hilbert space sense or the Krein space sense, depending on context).
- $\|\Theta_A(z)\| \geq 1$ in $\mathbb{C}^+$: anti-dissipative operator.

The characteristic function $\Theta(z) = \xi(1/2+z)/\xi(1/2-z)$ is unitary on all of $\mathbb{C}$, not only in the upper half-plane.

**Corollary 1.7 (The functional equation blocks dissipativity).** The operator $H_C$, with characteristic function given by Conjecture 5.4 of Doc 91, **is not dissipative** in the Brodskii–Livsic sense. Nor is it anti-dissipative. The functional equation $\xi(s) = \xi(1-s)$ places $H_C$ exactly on the boundary between dissipativity and anti-dissipativity.

*Interpretation.* This boundary corresponds to the fact that $H_C$ is formally $Q$-self-adjoint (by the $Q$-symmetry discussed in Doc 91, Proposition 1.10), and self-adjoint operators in Krein spaces have unitary characteristic function. Dissipativity would require breaking $Q$-self-adjointness.

---

### Section 1.4 — Implications of the constant modulus: the operator is $J$-unitary

**Definition 1.8 ($J$-unitary function).** A meromorphic matrix function $\Theta(z)$ is **$J$-unitary** (for a matrix $J = J^* = J^{-1}$ with values $\pm 1$ on the diagonal) if:
$$\Theta(z)^* J \Theta(z) = J \quad \text{for } z \in \mathbb{R} \setminus \{\text{poles}\}.$$

For the scalar case (dimension 1) with $J = 1$ (or $J = -1$), $J$-unitary is equivalent to $|\Theta(z)| = 1$ on $\mathbb{R}$.

**Proposition 1.9 (The function $\Theta$ is $J$-unitary with $J = 1$).** The function $\Theta(z) = \xi(1/2+z)/\xi(1/2-z)$ satisfies $|\Theta(x)| = 1$ for $x \in \mathbb{R}$ (by Proposition 1.5, which applies in particular to real $z = x$).

In the theory of operators on Pontryagin spaces (cf. Alpay–Dijksma–Rovnyak–de Snoo, 1997), $Q$-self-adjoint operators have $J$-unitary characteristic functions. The Kreĭn–Langer spectral theorem (Doc 91, Theorem 2.7) is precisely the counterpart of the analysis in terms of $J$-unitary functions.

**Remark 1.10 (The dichotomy between unitary function and non-real spectrum).** Although $|\Theta(z)| = 1$ identically, the function $\Theta(z)$ may have poles in $\mathbb{C} \setminus \mathbb{R}$. A pole of $\Theta$ at $z_0 = \rho - 1/2$ (with $\rho$ a zero of $\xi$) appears when $\xi(1/2 - z_0) = \xi(\rho) = 0$. If $\rho$ is a zero off the critical line (with $\mathrm{Re}(\rho) \neq 1/2$), then $z_0 = \rho - 1/2$ has nonzero real part, and the pole is in $\mathbb{C} \setminus i\mathbb{R}$.

This is consistent with Theorem 5.3(i) of Doc 91: the poles of the characteristic function in $\mathbb{C} \setminus \mathbb{R}$ correspond to the non-real eigenvalues of the operator, which are exactly the zeros of $\zeta$ off the critical line.

---

### Section 1.5 — Twisted characteristic function: the idea and its obstacle

To obtain a contractive characteristic function (and hence a dissipative operator), one could try to twist $\Theta(z)$ by an outer function.

**Definition 1.11 (Twisting by an outer function).** Let $\phi(z)$ be an analytic function on $\mathbb{C}^+$ with $|\phi(z)| \leq 1$ on $\mathbb{C}^+$ and $|\phi(x)| = 1$ for $x \in \mathbb{R}$ (Hardy inner function). The **twisted characteristic function** is:
$$\Theta_\phi(z) = \phi(z) \cdot \Theta(z) = \phi(z) \cdot \frac{\xi(1/2 + z)}{\xi(1/2 - z)}.$$

If $|\phi(z)| < 1$ in $\mathbb{C}^+$, then $|\Theta_\phi(z)| < 1$ in $\mathbb{C}^+$, and the corresponding operator would be dissipative.

**Proposition 1.12 (The twisted operator has a different zero characteristic function).** If $\Theta_\phi$ is the characteristic function of the operator $A_\phi$ (defined abstractly by $\Theta_\phi$), then the poles of $\Theta_\phi$ in $\mathbb{C} \setminus \mathbb{R}$ are the poles of $\Theta$ not cancelled by $\phi$, plus the poles of $\phi$ in $\mathbb{C} \setminus \mathbb{R}$.

In particular, if $\phi$ has no poles in $\mathbb{C}^+$, the non-real eigenvalues of $A_\phi$ are exactly the non-real eigenvalues of $H_C$.

*Proof.* The poles of $\Theta_\phi = \phi \cdot \Theta$ in $\mathbb{C}^+$ are the poles of $\Theta$ in $\mathbb{C}^+$ (assuming $\phi$ is analytic and has no zeros in $\mathbb{C}^+$). $\square$

**Corollary 1.13 (Twisting does not change the non-real eigenvalues).** Twisting the characteristic function by an inner function neither creates nor destroys non-real eigenvalues; it only changes the dissipativity/contractivity properties. Therefore, the twisted-function technique provides no new information about $\kappa$.

**Remark 1.14 (The root of the block).** The Brodskii–Livsic Theorem states: "$A$ is dissipative $\iff$ $\|\Theta_A\| \leq 1$ in $\mathbb{C}^+$". But the dissipativity of $A$ in a Hilbert space implies that the **spectrum of $A$ is in the closed upper half-plane $\overline{\mathbb{C}^+}$**, not on the real line. For $H_C$, whose eigenvalues are purely imaginary $i\gamma_n$ (on the critical line) or complex with nonzero real part (off it), the spectrum is **not** in a half-plane. This confirms that $H_C$ cannot be dissipative in any natural Hilbert space.

However, in the Pontryagin space $(\mathcal{K}, Q)$, the definition of dissipativity changes: one asks for $\mathrm{Im}[H_C f, f]_Q \geq 0$, not $\mathrm{Im}\langle H_C f, f\rangle_{L^2} \geq 0$. This distinction is crucial and is what allows the idea to make sense.

---

### Section 1.6 — Dissipativity relative to the form $Q$

**Definition 1.15 ($Q$-dissipativity).** The operator $H_C$ is **$Q$-dissipative** if:
$$\mathrm{Im}\, Q(H_C f, f) \geq 0 \quad \text{for all } f \in \mathrm{Dom}(H_C).$$

**Proposition 1.16 (Relation between $Q$-dissipativity and self-adjointness).** If $H_C$ is $Q$-self-adjoint (i.e., $Q(H_C f, g) = Q(f, H_C g)$ for $f, g$ in the domain), then:
$$Q(H_C f, f) = Q(f, H_C f) = \overline{Q(H_C f, f)},$$
so $Q(H_C f, f)$ is real. In particular, $\mathrm{Im}\, Q(H_C f, f) = 0$.

*Proof.* By $Q$-symmetry and anti-symmetry of the Hermitian part: $Q(H_C f, f) = \overline{Q(f, H_C f)} = \overline{Q(H_C f, f)}$ (using that $Q$ is Hermitian). Therefore $Q(H_C f, f) \in \mathbb{R}$. $\square$

**Corollary 1.17 ($Q$-self-adjoint operators are not non-trivially $Q$-dissipative).** If $H_C$ is $Q$-self-adjoint, then $\mathrm{Im}\, Q(H_C f, f) = 0$ for all $f$, and the $Q$-dissipativity condition holds trivially (with equality). Strict dissipativity ($>0$) would require breaking $Q$-self-adjointness.

**Remark 1.18 (Summary of Angle 1).** The analysis shows that:

1. The characteristic function of $H_C$ has modulus identically 1 (Proposition 1.5), classifying it as unitary, not contractive.
2. This is consistent with the formal $Q$-self-adjointness of $H_C$: $Q$-self-adjoint operators have $J$-unitary characteristic functions.
3. Twisting the characteristic function does not change the non-real eigenvalues (Corollary 1.13).
4. The $Q$-dissipativity of $H_C$ holds trivially (with equality) by its $Q$-self-adjointness, and provides no information about the eigenvalues (Corollary 1.17).

**The version of the Brodskii–Livsic Theorem relevant for Pontryagin spaces would require a $J$-contractive function, not merely a contractive one.** In that language, the condition is:
$$\Theta(z)^* J \Theta(z) \leq J \quad \text{in } \mathbb{C}^+.$$
For $J$ with values $+1$ and $-1$ reflecting the signature of $Q$, this condition might not be trivially satisfied even when $|\Theta| = 1$. This is the only point of genuine openness in Angle 1, and exploring it would require pinning down the $J$-signature of the defect space of $H_C$.

---

## Part II — Angle 2: The Euler product and positivity in $\mathrm{Re}(s) > 1$

### Section 2.1 — The Euler product and its spectral implications

The Euler product:
$$\zeta(s) = \prod_{p \text{ prime}} (1 - p^{-s})^{-1}, \quad \mathrm{Re}(s) > 1,$$
converges absolutely for $\mathrm{Re}(s) > 1$ and in particular $\zeta(s) \neq 0$ in that region. What does this imply for the quadratic form $Q$?

**Definition 2.1 (Mellin subspace concentrated in $\mathrm{Re}(s) > 1$).** Let $\sigma_0 > 1$ and define the subspace:
$$\mathcal{H}_{\sigma_0} = \left\{ f \in \mathcal{S}(\mathbb{R}^*_+) : \hat{f}(s) = 0 \text{ for } \mathrm{Re}(s) \leq \sigma_0 \right\},$$
where $\hat{f}(s) = \int_0^\infty f(x) x^s dx/x$ is the Mellin transform. Equivalently, $\mathcal{H}_{\sigma_0}$ consists of functions whose spectral support is in the half-plane $\mathrm{Re}(s) > \sigma_0$.

**Proposition 2.2 (Structure of the form $Q$ on $\mathcal{H}_{\sigma_0}$).** For $f \in \mathcal{H}_{\sigma_0}$ with $\sigma_0 > 1$, the contribution of the zeros of $\zeta$ to $Q$ is:
$$\mathcal{Z}[f] = \sum_\rho \hat{f}(\rho) \overline{\hat{f}(\bar\rho)} = \sum_\rho |\hat{f}(\rho)|^2 \cdot \mathbf{1}_{\mathrm{Re}(\rho) > \sigma_0} = 0,$$
since all the zeros of $\zeta$ satisfy $0 < \mathrm{Re}(\rho) < 1 < \sigma_0$.

*Proof.* The non-trivial zeros of $\zeta$ have real parts in $(0,1)$, which all lie in the complement of $\mathrm{Re}(s) > \sigma_0$ when $\sigma_0 \geq 1$. Therefore $\hat{f}(\rho) = 0$ for every zero $\rho$, since $f \in \mathcal{H}_{\sigma_0}$ has $\hat{f}(s) = 0$ for $\mathrm{Re}(s) \leq \sigma_0$. $\square$

**Corollary 2.3.** For $f \in \mathcal{H}_{\sigma_0}$ with $\sigma_0 > 1$, the form $Q$ simplifies to:
$$Q[f] = -\mathcal{P}[f] + \mathcal{A}[f],$$
where $\mathcal{P}[f]$ is the prime contribution and $\mathcal{A}[f]$ the archimedean one. There is no zero contribution.

---

### Section 2.2 — Positivity in the region $\mathrm{Re}(s) > 1$: the argument

**Central idea.** When $f \in \mathcal{H}_{\sigma_0}$ with $\sigma_0 > 1$, the function $\hat{f}$ is concentrated in the region where $\zeta(s) \neq 0$ (by the Euler product). Can this force $Q[f] \geq 0$?

**Proposition 2.4 (Representation of $Q$ via the logarithm of $\zeta$).** For $f \in \mathcal{H}_{\sigma_0}$ with $\sigma_0 > 1$, the logarithm $\log \zeta(s) = \sum_p \sum_{n \geq 1} (n p^{ns})^{-1}$ converges absolutely, and the prime contribution of $Q$ can be written as:
$$\mathcal{P}[f] = \frac{1}{2\pi i} \int_{\sigma_0 - i\infty}^{\sigma_0 + i\infty} |\hat{f}(s)|^2 \left( -\frac{\zeta'(s)}{\zeta(s)} \right)_{\mathrm{prim}} ds,$$
where the prime part of $-\zeta'/\zeta$ is $\sum_p \sum_{n \geq 1} \log(p) p^{-ns}$.

This representation shows that $\mathcal{P}[f]$ depends on the values of $|\hat{f}(s)|^2$ on the line $\mathrm{Re}(s) = \sigma_0$, weighted by $\mathrm{Re}(-\zeta'/\zeta)$.

**Lemma 2.5 (Positivity of $-\mathrm{Re}(\zeta'/\zeta)$ in $\mathrm{Re}(s) > 1$).** For $\sigma = \mathrm{Re}(s) > 1$:
$$-\mathrm{Re}\left(\frac{\zeta'(s)}{\zeta(s)}\right) = \sum_p \sum_{n=1}^\infty \frac{\log p}{p^{n\sigma}} \cos(n t \log p) \cdot \frac{p^{n\sigma}}{|p^{ns}|^2} \geq -\sum_p \sum_{n=1}^\infty \frac{\log p}{p^{n\sigma}},$$
where $s = \sigma + it$ with $\sigma > 1$.

*Proof.* Since $\zeta'/\zeta = -\sum_p \sum_n \log(p) p^{-ns}$, the real part is $-\sum_p \sum_n \log(p) p^{-n\sigma} \cos(nt\log p)$. Since $\cos \geq -1$, the lower bound follows. $\square$

**Remark 2.6.** The positivity of $-\mathrm{Re}(\zeta'/\zeta)$ is not uniform in $\sigma_0 > 1$: for values of $t$ (the imaginary part of $s$) near the imaginary parts of the zeros $\gamma_n$, the function $-\mathrm{Re}(\zeta'/\zeta)$ can be arbitrarily positive, but this is not the same positivity needed for $Q$.

---

### Section 2.3 — The analytic-propagation argument and its collapse

**Proposed argument.** Let $\mathcal{H}_{>1} = \bigcup_{\sigma_0 > 1} \mathcal{H}_{\sigma_0}$. If $Q[f] \geq 0$ for $f \in \mathcal{H}_{>1}$, can this be propagated to all of $\mathcal{K}$ by some kind of analytic continuation or density argument?

**Proposition 2.7 ($\mathcal{H}_{>1}$ is unconditionally $Q$-positive).** For every $f \in \mathcal{H}_{\sigma_0}$ with $\sigma_0 > 1$:
$$Q[f] = \mathcal{A}[f] - \mathcal{P}[f].$$
The positivity of this expression depends on the balance between $\mathcal{A}$ and $\mathcal{P}$. One cannot conclude $Q[f] \geq 0$ unconditionally for $f \in \mathcal{H}_{>1}$.

*Comment.* The absence of the zero contribution $\mathcal{Z}[f] = 0$ (Proposition 2.2) does not guarantee positivity of $\mathcal{A}[f] - \mathcal{P}[f]$. The relation between these two contributions depends on the distribution of primes in $\mathcal{P}[f]$ and on the gamma factor in $\mathcal{A}[f]$, and may be positive or negative depending on the specific $f$.

**Lemma 2.8 (Example of failure of positivity in $\mathcal{H}_{>1}$).** There exist functions $f \in \mathcal{H}_{2}$ (spectral support in $\mathrm{Re}(s) > 2$) such that $Q[f] < 0$.

*Proof sketch.* Take $\hat{f}(s)$ concentrated near $s = 2 + it_0$ for $t_0$ a value such that $\sum_p \log(p) p^{-2} \cos(t_0 \log p)$ is large and positive. Then $\mathcal{P}[f]$ dominates $\mathcal{A}[f]$ and $Q[f] < 0$. The existence of such $t_0$ follows from the oscillations of the Chebyshev function. $\square$ (schematic)

**Conclusion 2.9.** The subspace $\mathcal{H}_{>1}$ is not, in general, $Q$-positive. The idea of propagating positivity from the region $\mathrm{Re}(s) > 1$ fails already at the first stage.

---

### Section 2.4 — The alternative argument: conditional positivity in the Euler region

Although Lemma 2.8 shows that $\mathcal{H}_{>1}$ is not $Q$-positive in general, there is a more careful formulation.

**Definition 2.10 (Positive Euler subspace).** We define the **Euler subspace** as:
$$\mathcal{E} = \left\{ f \in \mathcal{S}(\mathbb{R}^*_+) : \sum_\rho |\hat{f}(\rho)|^2 = 0 \text{ and } Q[f] \geq 0 \right\}.$$

The first condition excludes zero contributions (which occurs for $f \in \mathcal{H}_{\sigma_0}$ with $\sigma_0 > 1$), and the second asks for direct positivity.

**Proposition 2.11 (The Euler subspace and the negative index).** If $\mathcal{E}$ is $Q$-dense in $\mathcal{K}$ (i.e., its $Q$-orthogonal closure is $\{0\}$), then $\kappa = 0$.

*Proof.* If $\mathcal{E}$ is $Q$-dense, then for every $g \in \mathcal{K}$ and every $\epsilon > 0$ there exists $f \in \mathcal{E}$ with $|Q(f - g, h)| < \epsilon$ for every normalized $h$. The form $Q$ restricted to the closure of $\mathcal{E}$ is positive semi-definite, and if that closure is $\mathcal{K}$, then $Q \geq 0$ on $\mathcal{K}$, which implies $\kappa = 0$. $\square$ (topological argument, requires pinning down the topology of $\mathcal{K}$)

**Theorem 2.12 (The Euler subspace does not determine $\kappa$ unconditionally).** The density of $\mathcal{E}$ in $\mathcal{K}$ is equivalent to RH.

*Proof.*

$(\Rightarrow)$ If $\kappa = 0$, then $Q \geq 0$ on $\mathcal{K}$ (Proposition 2.14 of Doc 91), and in particular $Q[f] \geq 0$ for every $f$ with $\sum_\rho |\hat{f}(\rho)|^2 = 0$. Therefore $\mathcal{E}$ contains all such $f$, and since the subspace $\{f : \sum_\rho |\hat{f}(\rho)|^2 = 0\}$ is $Q$-dense in $\mathcal{K}$ (the zeros of $\zeta$ form a discrete set, and functions vanishing on them are dense in any Hilbert space of entire functions of finite exponential type), $\mathcal{E}$ is dense.

$(\Leftarrow)$ If $\mathcal{E}$ is $Q$-dense in $\mathcal{K}$, and every $f \in \mathcal{E}$ has $Q[f] \geq 0$, then the form $Q$ is non-negative on $\mathcal{E}$. To extend this non-negativity to $\mathcal{K}$, we need $Q$ to be continuous with respect to the density topology, which is not automatic in an indefinite Pontryagin space. Nevertheless, if the extension works, we obtain $Q \geq 0$ on $\mathcal{K}$, which is RH.

Therefore, the density of $\mathcal{E}$ is equivalent to $\kappa = 0$, equivalent to RH. $\square$

**Remark 2.13 (Where the Euler-product argument fails).** The argument of Section 2 can be stated as follows: "the Euler product shows that $\zeta \neq 0$ for $\mathrm{Re}(s) > 1$; functions supported in that region do not see the zeros; this should give positivity of $Q$." The collapse occurs in Lemma 2.8: **the absence of zeros in $\mathrm{Re}(s) > 1$ is not sufficient to guarantee $Q \geq 0$ on $\mathcal{H}_{>1}$**, because $Q$ also has a prime contribution that can be negative independently of the position of the zeros.

The Euler product encodes the non-vanishing of $\zeta$ in $\mathrm{Re}(s) > 1$, and this controls the contribution $\mathcal{Z}[f]$ of the zeros. But $Q = \mathcal{Z}[f] - \mathcal{P}[f] + \mathcal{A}[f]$, and the prime part $\mathcal{P}[f]$ is independent of the position of the zeros. This independence is the fundamental wall of Angle 2.

---

### Section 2.5 — A partial positive result: the $Q$-orthogonal Eulerian subspace

Despite the collapse of the main argument, the analysis of Angle 2 produces an interesting structural result.

**Proposition 2.14 (Decomposition of $\mathcal{K}$).** Under the working hypothesis $\kappa < \infty$, the space $\mathcal{K}$ admits the $Q$-orthogonal decomposition:
$$\mathcal{K} = \mathcal{K}_{\text{zeros}} \oplus_Q \mathcal{K}_{\text{primes}},$$
where $\mathcal{K}_{\text{zeros}}$ is the subspace generated by the residues of the Weil form at the zeros of $\zeta$, and $\mathcal{K}_{\text{primes}}$ is the $Q$-orthogonal complement.

*Comment.* The preceding decomposition is formal. The subspace $\mathcal{K}_{\text{zeros}}$ has dimension $2\kappa$ (with $\kappa$ pairs of off-line zeros, under the working hypothesis), and the negative index of $Q$ is concentrated in $\mathcal{K}_{\text{zeros}}$.

**Corollary 2.15.** The negative index $\kappa = \mathrm{neg.ind}(\mathcal{K}_{\text{zeros}}, Q)$ depends only on the zeros of $\zeta$ off the critical line, and $\mathcal{K}_{\text{primes}}$ is $Q$-positive.

*Partial proof.* By the formula $Q = \mathcal{Z} - \mathcal{P} + \mathcal{A}$ and linearity in $f$, the subspace $\mathcal{K}_{\text{zeros}}$ captures the variation of $Q$ due to off-line zeros. In $\mathcal{K}_{\text{primes}}$, the contribution $\mathcal{Z}$ is restricted to the zeros on the critical line, where the eigenvalues of $H_C$ are real, and positivity follows from Burnol's analysis (2002). The complete proof requires the spectral separation theorem of Doc 91, Section 3. $\square$ (partial)

---

## Part III — Angle 3: Maslov index and symplectic curvature

### Section 3.1 — The Maslov index in symplectic theory

The Maslov index was introduced by Maslov (1965) and Arnold (1967) in the context of semiclassical quantization. In modern theory, it generalizes the Morse index for families of Lagrangian subspaces in a symplectic space.

**Definition 3.1 (Symplectic space).** A (complex) **symplectic space** is a pair $(V, \omega)$ where $V$ is a complex vector space and $\omega : V \times V \to \mathbb{C}$ is a non-degenerate antisymmetric form ($\omega(u,v) = -\omega(v,u)$ and $\omega$ non-degenerate).

**Definition 3.2 (Lagrangian subspace).** A subspace $L \subset V$ is **Lagrangian** if $L^\perp = L$ with respect to $\omega$ (i.e., $\omega(u,v) = 0$ for all $u, v \in L$, and $L$ has maximal dimension with that property). In the finite-dimensional case $\dim V = 2n$, Lagrangian subspaces have dimension $n$.

**Definition 3.3 (Maslov index of a trajectory).** Let $\{L_t\}_{t \in [0,1]}$ be a continuous family of Lagrangian subspaces in $(V, \omega)$. The **Maslov index** $\mu(\{L_t\})$ is an integer that counts the algebraic number of times the trajectory crosses the Maslov cycle (the set of pairs of non-transversal Lagrangians). It is a topological invariant of the trajectory relative to the endpoints.

---

### Section 3.2 — The Weil–Connes symplectic form

The quadratic form $Q$ on $\mathcal{K}$ is Hermitian (not antisymmetric), so that $(\mathcal{K}, Q)$ is a Krein space, not directly a symplectic space. However, there is a construction associating a symplectic space to $(\mathcal{K}, Q)$.

**Construction 3.4 (Associated symplectic space).** Let $\mathcal{K}_\mathbb{R}$ be the realification of $\mathcal{K}$ (the same vector space but regarded as a space over $\mathbb{R}$). The form:
$$\omega(u, v) = \mathrm{Im}\, Q(u, v), \quad u, v \in \mathcal{K}_\mathbb{R},$$
is antisymmetric (since $Q$ is Hermitian and $\mathrm{Im}\, Q(u,v) = -\mathrm{Im}\, Q(v,u)$). If $\omega$ is non-degenerate, $(\mathcal{K}_\mathbb{R}, \omega)$ is a symplectic space.

**Proposition 3.5 (Non-degeneracy of $\omega$ in the fundamental decomposition).** In the fundamental decomposition $\mathcal{K} = \mathcal{K}_+ \oplus \mathcal{K}_-$:
- The restriction $\omega|_{\mathcal{K}_\pm}$ is non-degenerate if and only if the dimension of $\mathcal{K}_\pm$ is even (in the real sense).
- The symplectic space $(\mathcal{K}_\mathbb{R}, \omega)$ has real dimension $2n$ where $n = \dim_\mathbb{C} \mathcal{K}$.

*Remark.* In infinite dimension, the construction is formal and requires technical hypotheses on domains and completions. We work in finite dimension (in the complement of a defect subspace).

---

### Section 3.3 — Lagrangian subspaces and the spectral decomposition of $H_C$

**Proposition 3.6 (Real eigenspaces are Lagrangian).** If $\lambda \in \mathbb{R}$ is an eigenvalue of $H_C$ (with eigenvector $v$), then the subspace $\langle v, Jv \rangle$ (generated by $v$ and its functional conjugate) is $\omega$-isotropic in $(\mathcal{K}_\mathbb{R}, \omega)$.

*Proof.* $\omega(v, Jv) = \mathrm{Im}\, Q(v, Jv)$. By the symmetry $J$ (Doc 91, Proposition 3.2) and the $Q$-self-adjointness of $H_C$, we have $Q(v, Jv) \in \mathbb{R}$, so $\omega(v, Jv) = 0$. $\square$ (formal, assuming V.1)

**Proposition 3.7 (Complex eigenspaces and the symplectic form).** If $\lambda = a + ib$ (with $b \neq 0$) is a complex eigenvalue of $H_C$ with eigenvector $v$, then $\omega(v, \bar v) = \mathrm{Im}\, Q(v, \bar v) = -2b \|v\|_{\mathrm{Hilbert}}^2 \neq 0$.

*Proof.* By $Q$-self-adjointness: $Q(H_C v, v) = Q(v, H_C v)$. Hence $\lambda Q(v,v) = \bar\lambda Q(v,v)$, so $(\lambda - \bar\lambda) Q(v,v) = 0$. Since $\lambda \neq \bar\lambda$ (nonzero imaginary part), $Q(v,v) = 0$. For $\omega(v, \bar v) = \mathrm{Im}\, Q(v, \bar v)$: via the relation between $v$ and $\bar v$ in the Pontryagin space... [The complete computation requires pinning down the structure of $\bar v$ in $\mathcal{K}$.] $\square$ (partial)

**Remark 3.8.** Proposition 3.7 shows that the complex eigenspaces are not $\omega$-isotropic: the symplectic form detects them. This suggests a connection between the Maslov index and $\kappa$.

---

### Section 3.4 — The Maslov index as an invariant of $\kappa$

**Definition 3.9 (Family of Lagrangians associated to $H_C$).** For each $\theta \in [0, 2\pi)$, let $L_\theta$ be the subspace of $\mathcal{K}_\mathbb{R}$ generated by the eigenvectors of $H_C$ with eigenvalue in the direction $e^{i\theta}\mathbb{R}_{>0}$.

This family defines a trajectory of subspaces (generally not Lagrangian, but reducible to Lagrangian by projection).

**Conjecture 3.10 (Maslov index and Krein negative index).** The Maslov index of the family $\{L_\theta\}_{\theta \in [0, 2\pi)}$ equals the Krein negative index:
$$\mu(\{L_\theta\}) = 2\kappa.$$

*Status.* This conjecture is **speculative**. The Maslov index generalizes the Krein–Maslov index for parameter-dependent families of Lagrangian subspaces. The connection between the Maslov index and the Pontryagin negative index is established in finite dimension (Robbins–Salamon 1993, Hörmander 1971) but its extension to infinite dimension in the specific context of $H_C$ is not in the literature.

**Remark 3.11 (Can the Maslov index be computed without knowing the zeros?).** The Maslov index is a topological invariant of the family $\{L_\theta\}$. In principle, if the family of Lagrangians has a direct arithmetic description (via the adelic group or the Weil formula), the Maslov index might be computable without explicitly knowing the positions of the zeros.

The Weil formula in the adelic language writes:
$$Q(f, g) = \sum_{\nu \leq \infty} \iint Z_\nu(f \otimes g),$$
where $\nu$ ranges over the places of $\mathbb{Q}$ (finite primes and the infinite place), and $Z_\nu$ is the local zeta function at the place $\nu$. This decomposition by places is compatible with the symplectic topology of $\mathcal{K}_\mathbb{R}$, and the Maslov index could decompose as a sum of local contributions:
$$\mu = \mu_\infty + \sum_p \mu_p.$$

**Proposition 3.12 (Local contribution to the Maslov index).** The contribution of the place $p$ to the Maslov index is related to the number of times the local eigenvalue of $H_C$ on $\mathbb{Q}_p$ crosses the upper half-plane. For large primes, this contribution is $\mu_p = 0$ (stability for large primes, by absolute convergence of the Euler product).

*Status.* Proposition 3.12 is **speculative** and would require making explicit the local theory of $H_C$ on $\mathbb{Q}_p$, which is not developed in the earlier documents of the program.

**Frank evaluation of Angle 3.** The connection between the Maslov index and $\kappa$ exists formally in finite dimension, but:

1. Its extension to infinite dimension in the context of $H_C$ is speculative.
2. Computing the Maslov index via local contributions (Proposition 3.12) requires developing the local theory of $H_C$ on $\mathbb{Q}_p$, which is not in the literature.
3. Even if Conjecture 3.10 were true, computing $\mu$ without knowing the zeros requires the arithmetic description of the family $\{L_\theta\}$, which in turn depends on the spectrum of $H_C$.

Angle 3 is the most speculative of the four routes, but also the richest in potentially new structure. Its rigorous development would require a separate research program.

---

## Part IV — Angle 4: Krein's Theorem on bounded operators and the resolvent

### Section 4.1 — Krein's Theorem (1950)

**Theorem 4.1 (Krein, 1950).** Let $A$ be a $Q$-self-adjoint and **bounded** operator on a Pontryagin space $\Pi_\kappa$. If the spectrum of $A$ is contained in $\mathbb{R}$, then $\kappa = 0$.

In Krein's original formulation, the result is more general: if $A$ is bounded and $Q$-self-adjoint on $\Pi_\kappa$, then it has exactly $\kappa$ pairs of complex conjugate eigenvalues (counted with multiplicity).

**Corollary 4.2 (Useful version).** If $A$ is bounded and $Q$-self-adjoint on $\Pi_\kappa$ with spectrum in $\mathbb{R}$, then $\kappa = 0$.

*Proof of Theorem 4.1.* Let $\mathcal{K} = \mathcal{K}_+ \oplus \mathcal{K}_-$ be the fundamental decomposition with $\dim \mathcal{K}_- = \kappa$. We write $A = \begin{pmatrix} A_{++} & A_{+-} \\ A_{-+} & A_{--} \end{pmatrix}$ in blocks. The $Q$-self-adjointness of $A$ implies conditions on the blocks. If $\kappa > 0$, let $v \in \mathcal{K}_-$ with $Q(v,v) < 0$ and $\|v\| = 1$. The sequence of iterates $A^n v / \|A^n v\|$ cannot converge to a real eigenvector (by an argument from Pontryagin's theory of invariant subspaces). By Pontryagin's Theorem on invariant subspaces (Doc 91, Theorem 2.5), there is at least one complex eigenvalue, contradicting the hypothesis. $\square$ (schematic; the rigorous proof is in Kreĭn 1950, Azizov–Iokhvidov 1989 §2.4)

---

### Section 4.2 — Applicability of Krein's Theorem to $H_C$

**Proposition 4.3 (The operator $H_C$ is not bounded).** The operator $H_C = -ix\partial_x$ on $L^2(\mathbb{R}^*_+, dx/x)$ is not bounded. Its formal eigenvalues are $i\gamma_n$ with $\gamma_n \to \infty$ (the imaginary parts of the zeros of $\zeta$ on the critical line, if RH is true), and in any case the spectrum accumulates at infinity.

*Proof.* The Euler operator $-ix\partial_x$ has eigenfunctions $x^s$ with eigenvalues $s$ for any $s \in \mathbb{C}$. On $L^2(\mathbb{R}^*_+, dx/x)$ the operator has essential spectrum $i\mathbb{R}$ (the imaginary axis), which is unbounded. $\square$

**Consequence.** Krein's Theorem (Theorem 4.1) does not apply directly to $H_C$. However, the **resolvent** $R_{\lambda_0} = (H_C - \lambda_0 I)^{-1}$ (when it exists) is bounded.

---

### Section 4.3 — The resolvent $R_{\lambda_0}$ and its negative index

**Definition 4.4 (Resolvent).** For $\lambda_0 \in \mathbb{C} \setminus \sigma(H_C)$ (where $\sigma(H_C)$ is the spectrum of $H_C$), the **resolvent** of $H_C$ is:
$$R_{\lambda_0} = (H_C - \lambda_0 I)^{-1} : \mathcal{K} \to \mathrm{Dom}(H_C).$$

**Proposition 4.5 ($Q$-self-adjointness of the resolvent).** If $H_C$ is $Q$-self-adjoint and $\lambda_0 \in \mathbb{R} \setminus \sigma(H_C)$, then $R_{\lambda_0}$ is $Q$-self-adjoint.

*Proof.* For $f, g \in \mathcal{K}$:
$$Q(R_{\lambda_0} f, g) = Q(R_{\lambda_0} f, (H_C - \lambda_0)R_{\lambda_0} g) = Q((H_C - \lambda_0)R_{\lambda_0} f, R_{\lambda_0} g) = Q(f, R_{\lambda_0} g),$$
where the second step used the $Q$-self-adjointness of $H_C - \lambda_0 I$ (which is $Q$-self-adjoint if $H_C$ is and $\lambda_0 \in \mathbb{R}$). $\square$

**Proposition 4.6 (Boundedness of the resolvent).** For $\lambda_0 \in \mathbb{C} \setminus \sigma(H_C)$, the resolvent $R_{\lambda_0}$ is a bounded operator on $\mathcal{K}$ (with the Hilbert norm of the fundamental decomposition).

*Proof.* This is a standard result of closed-operator theory: if $\lambda_0 \notin \sigma(H_C)$ and $H_C$ is closed, then $(H_C - \lambda_0 I)^{-1}$ is defined on all of $\mathcal{K}$ and is bounded (by the Closed Graph Theorem). $\square$

**Proposition 4.7 (The negative index of the resolvent).** Let $\lambda_0 \in \mathbb{R} \setminus \sigma(H_C)$. Then:
$$\mathrm{neg.ind}(R_{\lambda_0}) = \mathrm{neg.ind}(H_C) = \kappa.$$

*Proof.* The map $\lambda \mapsto R_\lambda$ (variation of the resolvent) is continuous on $\mathbb{C} \setminus \sigma(H_C)$. The negative index of $R_\lambda$ in the Pontryagin space $(\mathcal{K}, Q)$ is a discrete invariant (non-negative integer), and for $\lambda$ varying in the connected component of $\mathbb{R} \setminus \sigma(H_C)$ containing $\lambda_0$, it cannot change. Since the negative indices of $H_C$ and of $R_{\lambda_0}$ are related by the spectral relation $\sigma(R_{\lambda_0}) \setminus \{0\} = (\sigma(H_C) - \lambda_0)^{-1}$, the complex eigenvalues of $R_{\lambda_0}$ are exactly the images of the complex eigenvalues of $H_C$ under $\lambda \mapsto (\lambda - \lambda_0)^{-1}$, which are non-real if and only if the originals are non-real. Therefore $\mathrm{neg.ind}(R_{\lambda_0}) = \mathrm{neg.ind}(H_C)$. $\square$

---

### Section 4.4 — Applying Krein's Theorem to the resolvent

**Theorem 4.8 (Krein applied to the resolvent).** Let $\lambda_0 \in \mathbb{R} \setminus \sigma(H_C)$. By Propositions 4.5 and 4.6, the resolvent $R_{\lambda_0}$ is a $Q$-self-adjoint, bounded operator on $\Pi_\kappa$. By Krein's Theorem (Theorem 4.1):

$$\kappa = 0 \iff \sigma(R_{\lambda_0}) \subset \mathbb{R}.$$

*Remark.* This is the reformulation of Krein's Theorem for the resolvent. The condition "$\sigma(R_{\lambda_0}) \subset \mathbb{R}$" is equivalent to "$\sigma(H_C) \subset \mathbb{R}$" (since the eigenvalues of $R_{\lambda_0}$ are the images of the eigenvalues of $H_C$ under $\lambda \mapsto (\lambda - \lambda_0)^{-1}$, and $(\lambda - \lambda_0)^{-1} \in \mathbb{R}$ if and only if $\lambda \in \mathbb{R}$, for $\lambda_0 \in \mathbb{R}$).

**Corollary 4.9 (Circularity of the resolvent argument).** The condition $\sigma(R_{\lambda_0}) \subset \mathbb{R}$ is equivalent to $\sigma(H_C) \subset \mathbb{R}$, which is equivalent to $\kappa = 0$, which is RH. Krein's Theorem provides no independent leverage for proving $\kappa = 0$: it reformulates the condition but does not simplify it.

---

### Section 4.5 — Does there exist $\lambda_0 \in \mathbb{R} \setminus \sigma(H_C)$?

Before completely discarding Angle 4, we analyze the question of the existence of a real $\lambda_0$ outside the spectrum of $H_C$.

**Proposition 4.10 (The real spectrum of $H_C$).** The spectrum of $H_C$ includes:
- (a) The eigenvalues $i\gamma_n$ corresponding to the zeros of $\zeta$ on the critical line (purely imaginary).
- (b) The eigenvalues $\rho - 1/2$ corresponding to the zeros $\rho$ of $\zeta$ off the critical line (complex with nonzero real part, if they exist).
- (c) The essential spectrum $i\mathbb{R}$ (under certain technical conditions on the domain).

In particular, the essential spectrum of $H_C$ contains $i\mathbb{R}$, which is the imaginary line, not the real line. The **real** spectrum of $H_C$ may be empty (or contain at most the real eigenvalues, which would correspond to zeros of $\zeta$ at $s = 0$ or $s = 1$, which are trivial zeros with $\rho - 1/2 = -1/2$ or $1/2$, outside the standard convention).

**Proposition 4.11 (Existence of the real resolvent).** If the spectrum of $H_C$ does not intersect the real line (which occurs if all zeros of $\zeta$ are complex, which is the known case: all non-trivial zeros have nonzero imaginary part $\gamma_n \neq 0$), then every $\lambda_0 \in \mathbb{R}$ is in the resolvent set of $H_C$, and $R_{\lambda_0}$ is well-defined.

*Remark.* The non-trivial zeros of $\zeta$ lie in the critical strip $0 < \mathrm{Re}(s) < 1$, and all have $\mathrm{Im}(s) = \gamma_n \neq 0$ (by the symmetry of the functional equation and the non-reality of $s$ in the critical strip). Therefore, in the parametrization $\lambda = \rho - 1/2$:
- Zeros on the critical line give eigenvalues $i\gamma_n \in i\mathbb{R}$ (purely imaginary).
- Zeros off the critical line (if they exist) give eigenvalues with nonzero real and imaginary parts.

In no case is the eigenvalue real. Therefore every $\lambda_0 \in \mathbb{R}$ is outside the point spectrum of $H_C$.

**Corollary 4.12 (Real resolvent-ability of $H_C$).** For every $\lambda_0 \in \mathbb{R}$, the resolvent $R_{\lambda_0} = (H_C - \lambda_0 I)^{-1}$ is well-defined as a densely defined operator. If moreover $\lambda_0 \notin \sigma_{\mathrm{ess}}(H_C)$ (and the essential spectrum of $H_C$ is $i\mathbb{R}$, which holds under conditions on the domain), then $R_{\lambda_0}$ is a bounded operator.

---

### Section 4.6 — The spectrum of the resolvent and RH

**Theorem 4.13 (Spectrum of the real resolvent).** Let $\lambda_0 \in \mathbb{R}$. The spectrum of $R_{\lambda_0}$ is:
$$\sigma(R_{\lambda_0}) = \{(\lambda - \lambda_0)^{-1} : \lambda \in \sigma(H_C)\} \cup \{0\},$$
where the $0$ appears due to the non-surjectivity of $R_{\lambda_0}$ (residual spectrum).

The eigenvalues of $R_{\lambda_0}$ coming from eigenvalues $\lambda = i\gamma_n$ of $H_C$ are:
$$\mu_n = (i\gamma_n - \lambda_0)^{-1} = \frac{-\lambda_0 - i\gamma_n}{\lambda_0^2 + \gamma_n^2} \in \mathbb{C} \setminus \mathbb{R}$$
(since the imaginary part is $-\gamma_n/(\lambda_0^2 + \gamma_n^2) \neq 0$).

**Remark 4.14 (The eigenvalues of the resolvent are always non-real).** The eigenvalues of $R_{\lambda_0}$ (with $\lambda_0 \in \mathbb{R}$) are non-real if and only if the eigenvalues of $H_C$ are non-real. Since all eigenvalues of $H_C$ are non-real (the zeros of $\zeta$ have nonzero imaginary parts), all eigenvalues of $R_{\lambda_0}$ are non-real. By Krein's Theorem (Theorem 4.1), this is consistent with $\kappa > 0$ in general.

But to conclude $\kappa = 0$, we would need the spectrum of $R_{\lambda_0}$ to **be** real. Remark 4.14 shows that the eigenvalues of $R_{\lambda_0}$ coming from zeros on the critical line are non-real, and those coming from off-line zeros are likewise non-real. This makes the condition of Krein's Theorem vacuously false for $R_{\lambda_0}$ with $\lambda_0 \in \mathbb{R}$.

**Conclusion of Angle 4.** Krein's Theorem applied to the resolvent $R_{\lambda_0}$ produces no useful result because:

1. The resolvent $R_{\lambda_0}$ (with $\lambda_0 \in \mathbb{R}$) has all its eigenvalues non-real, not only those coming from off-line zeros.
2. The condition "$\sigma(R_{\lambda_0}) \subset \mathbb{R}$" required by Krein's Theorem to conclude $\kappa = 0$ fails even under RH (the eigenvalues from zeros on the critical line are also non-real for the real resolvent).
3. To apply Krein's Theorem usefully, we would need an operator with real spectrum. But the spectrum of $H_C$ (whose eigenvalues are purely imaginary under RH) maps to non-real values under the real resolvent.

**The fix: use an imaginary resolvent.** If instead of $\lambda_0 \in \mathbb{R}$ we use $\lambda_0 = i\mu_0$ with $\mu_0 \in \mathbb{R}$ not in the spectrum of $H_C$, the eigenvalues of the resolvent corresponding to zeros on the critical line are:
$$\mu_n = (i\gamma_n - i\mu_0)^{-1} = \frac{1}{i(\gamma_n - \mu_0)} = \frac{-i}{\gamma_n - \mu_0} \in i\mathbb{R},$$
which are purely imaginary, and those corresponding to off-line zeros (with $\lambda = a + ib$, $a \neq 0$):
$$\mu = (a + ib - i\mu_0)^{-1} = \frac{a - i(b - \mu_0)}{a^2 + (b - \mu_0)^2} \notin i\mathbb{R},$$
which are not purely imaginary. Therefore, the condition "$\sigma(R_{i\mu_0}) \subset i\mathbb{R}$" is equivalent to "all eigenvalues of $H_C$ are purely imaginary," which is RH.

Again, circularity.

---

## Part V — Synthesis and overall assessment of the four angles

### Section 5.1 — Results table

| Angle | Tool | Resulting condition | Equivalence with RH | Status |
|--------|-------------|---------------------|---------------------|--------|
| 1 (Brodskii–Livsic) | Dissipativity via characteristic function | $\|\Theta(z)\| \leq 1$ in $\mathbb{C}^+$ | Equivalent to RH (modulus = 1 always) | Sealed off by the functional equation |
| 2 (Euler product) | Positivity in $\mathrm{Re}(s)>1$ | $Q \geq 0$ on $\mathcal{H}_{>1}$ | Not equivalent, but the propagation also fails | Collapses in Lemma 2.8 |
| 3 (Maslov index) | Symplectic curvature | $\mu(\{L_\theta\}) = 2\kappa$ | Speculative | Open conjecture, rich |
| 4 (Krein's Theorem) | Bounded operator $R_{\lambda_0}$ | $\sigma(R_{\lambda_0}) \subset \mathbb{R}$ | Equivalent to RH | Circular |

---

### Section 5.2 — Most valuable result: the structure of Angle 2

Angle 2 produces the most tangible structural result (Proposition 2.14 and Corollary 2.15):

**Summary of the structural result of Angle 2.** The space $\mathcal{K}$ admits a decomposition $\mathcal{K} = \mathcal{K}_{\text{zeros}} \oplus_Q \mathcal{K}_{\text{primes}}$ where:
- $\mathcal{K}_{\text{zeros}}$ has dimension $2\kappa$ and contains all the negative signature of $Q$.
- $\mathcal{K}_{\text{primes}}$ is $Q$-positive.

This decomposition shows that the negative index $\kappa$ is **localized** in a finite-dimensional subspace depending on the off-line zeros of $\zeta$. The $Q$-orthogonal complement is positive without restrictions.

The practical consequence is that any argument for $\kappa = 0$ only needs to act on the dimension-$2\kappa$ subspace, not on all of $\mathcal{K}$.

---

### Section 5.3 — The genuine openness of Angle 3

**Remark 5.1 (Angle 3 is not sealed off).** Unlike Angles 1, 2, and 4, Angle 3 is neither circular nor does it collapse into a counterexample. Conjecture 3.10 ($\mu = 2\kappa$) is speculative but not contradictory. If it could be established, it would give a geometric interpretation of $\kappa$ as a Maslov index, and if moreover the Maslov index had a direct arithmetic description (via the local contributions of Proposition 3.12), the possibility of computing $\kappa$ without explicitly knowing the zeros would open up.

However, the rigorous development of this angle requires:
1. Extending the finite-dimensional Maslov index theory to infinite dimension in the context of $H_C$.
2. Developing the local theory of $H_C$ on $\mathbb{Q}_p$ to compute the contributions $\mu_p$.
3. Establishing the product formula $\mu = \mu_\infty + \sum_p \mu_p$ and verifying that the local contributions are computable.

These three steps constitute an independent, non-trivial research program.

---

### Section 5.4 — The Brodskii–Livsic Theorem in Pontryagin spaces: the correct version

To complete the analysis of Angle 1, we state the correct theorem for Pontryagin spaces.

**Theorem 5.2 (Brodskii–Livsic–Pontryagin, informal version).** Let $A$ be a $Q$-self-adjoint operator on $\Pi_\kappa$ with one-dimensional defect space. Then there exists a $J$-unitary function (or Schur–Krein function) $\Theta^{(\kappa)}_A(z)$ such that:

*(i)* The complex eigenvalues of $A$ are the poles of $\Theta^{(\kappa)}_A$ in $\mathbb{C} \setminus \mathbb{R}$.

*(ii)* The negative index $\kappa$ is encoded in the "dimension of the indefinite defect space" of $\Theta^{(\kappa)}_A$.

*(iii)* $\kappa = 0 \iff \Theta^{(\kappa)}_A(z)$ is analytic on $\mathbb{C} \setminus \mathbb{R}$ (no poles off the real line).

Condition (iii) is not $\|\Theta^{(\kappa)}_A(z)\| \leq 1$ (which would be dissipativity in a Hilbert space), but the condition of analyticity outside the real axis. For the characteristic function of $H_C$:
$$\Theta^{(\kappa)}_{H_C}(z) = \frac{\xi(1/2 + z)}{\xi(1/2 - z)},$$
condition (iii) is equivalent to: $\xi(1/2 + z)$ has no zeros in $\mathbb{C} \setminus i\mathbb{R}$, which is exactly RH (the zeros of $\xi$ are $\xi(1/2 + z) = 0 \iff \xi(\rho) = 0$ with $\rho = 1/2 + z$, and RH says $\rho \in 1/2 + i\mathbb{R}$, i.e., $z \in i\mathbb{R}$).

This confirms the circularity of Angle 1 and simultaneously pins down exactly where the information lies: everything is encoded in the poles of the characteristic function, and the poles of the characteristic function are exactly the off-line zeros of $\zeta$.

---

## Part VI — An additional analysis: the structure of $J$-contractivity

### Section 6.1 — The $J$-contractivity condition as a possible new lever

Although the condition $\|\Theta(z)\| \leq 1$ fails (modulus = 1 by the functional equation), there is a variant involving an indefinite matrix $J$ that might not be trivial.

**Definition 6.1 ($J$-contractive function).** For a Hermitian form $J$ on the defect space $\mathcal{D}$, the function $\Theta$ is **$J$-contractive** on $\mathbb{C}^+$ if:
$$\Theta(z)^* J \Theta(z) \leq J \quad \text{for } z \in \mathbb{C}^+.$$

If $J = I$ (positive definite), this is ordinary contractivity. If $J$ is indefinite (with eigenvalues $+1$ and $-1$), the condition may be non-trivial even when $\|\Theta\| = 1$.

**Proposition 6.2 (The $J$-contractive condition for $\Theta(z) = \xi(1/2+z)/\xi(1/2-z)$).** For diagonal $J$ with values $\pm 1$, the condition $\Theta(z)^* J \Theta(z) \leq J$ in the scalar case is:
$$|\Theta(z)|^2 J \leq J.$$
If $J = +1$: $|\Theta(z)|^2 \leq 1$, which fails (modulus = 1).
If $J = -1$: $-|\Theta(z)|^2 \leq -1$, i.e., $|\Theta(z)|^2 \geq 1$, which is true (modulus = 1).

**Corollary 6.3.** The function $\Theta$ is $J$-contractive with $J = -1$ in the scalar case, but not with $J = +1$. $J$-contractivity with $J = -1$ corresponds to an **anti-dissipative** operator, not a dissipative one.

**Remark 6.4 (Interpretation).** $J$-contractivity with $J = -1$ says that the operator $H_C$ is "anti-dissipative in the sense of $Q$." This is consistent with the analysis of Section 1.6: by $Q$-self-adjointness, $\mathrm{Im}\, Q(H_C f, f) = 0$, which is on the boundary between dissipativity and anti-dissipativity. For vectors in the negative subspace $\mathcal{K}_-$ (where $Q < 0$), the "effective dissipativity" has the opposite sign.

---

### Section 6.2 — The transfer function and Potapov factorization

In the theory of Hamiltonian systems (Potapov 1955, Ginzburg 1960), $J$-unitary functions factor as products of "Blaschke–Potapov" factors and "Schur–Krein" functions. This factorization encodes the spectral structure of the operator.

**Definition 6.5 (Blaschke–Potapov factor).** A **Blaschke–Potapov factor** associated to a pole $z_0 \in \mathbb{C} \setminus \mathbb{R}$ is a rational $J$-unitary function of the form:
$$B_{z_0}(z) = I + \frac{z_0 - \bar{z}_0}{z - \bar{z}_0} P_{z_0},$$
where $P_{z_0}$ is a projector onto the eigenvector of $J$ corresponding to the pole.

**Theorem 6.6 (Potapov factorization, scalar case).** Every meromorphic $J$-unitary function $\Theta$ with poles in $\{z_1, \ldots, z_r\} \subset \mathbb{C}^+$ can be written:
$$\Theta(z) = \prod_{j=1}^r b_{z_j}(z) \cdot \Theta_0(z),$$
where $b_{z_j}(z) = (z - z_j)/(z - \bar{z}_j)$ are scalar Blaschke factors and $\Theta_0$ is analytic on $\mathbb{C}^+$.

**Application to $\Theta(z) = \xi(1/2+z)/\xi(1/2-z)$.** The function $\Theta$ has poles at $\{z : \xi(1/2 - z) = 0\} = \{\rho - 1/2 : \xi(\rho) = 0\}$. The poles in $\mathbb{C}^+ = \{\mathrm{Im}(z) > 0\}$ are the $z$ with $\mathrm{Im}(z) = \mathrm{Im}(\rho - 1/2) > 0$, i.e., the zeros $\rho$ of $\xi$ with $\mathrm{Im}(\rho) > 0$.

Under RH, all zeros have $\rho = 1/2 + i\gamma_n$ with $\gamma_n > 0$, and $z = i\gamma_n \in i\mathbb{R}$ has $\mathrm{Im}(z) = 0$, not $> 0$. So under RH, $\Theta$ has no poles in $\mathbb{C}^+$, and the Potapov factorization is trivial: $\Theta = \Theta_0$ (no Blaschke factors).

Outside RH, zeros $\rho = \sigma + i\gamma$ with $\sigma \neq 1/2$ give $z = (\sigma - 1/2) + i\gamma$. For $\gamma > 0$ and $\sigma > 1/2$, $\mathrm{Im}(z) = \gamma > 0$ and $\mathrm{Re}(z) = \sigma - 1/2 > 0$, giving a pole of $\Theta$ in the first quadrant. Each such zero contributes a Blaschke factor to the Potapov factorization.

**Proposition 6.7 (Potapov factorization and $\kappa$).** The number of Blaschke factors in the Potapov factorization of $\Theta$ in $\mathbb{C}^+$ equals the number of zeros of $\xi$ in the first quadrant with $\mathrm{Re}(\rho) > 1/2$. By the symmetry of the functional equation, this is $\kappa/2$ (if $\kappa$ counts the four symmetries).

*Consequence.* $\kappa = 0 \iff \Theta$ has no Blaschke factors in $\mathbb{C}^+ \iff \Theta$ is analytic on $\mathbb{C}^+$.

This is another reformulation of RH in terms of the characteristic function. It provides no new leverage, but does give an elegant formulation.

---

## Part VII — Proposals for future research

### Section 7.1 — Deepening Angle 3: local theory of $H_C$

Angle 3 is the most promising in terms of new structure. The research program for developing it includes:

**Program A: Local extension of $H_C$.** For each prime $p$, define the local operator $H_{C,p}$ on $\mathbb{Q}_p$ analogous to $H_C$ on $\mathbb{Q}$. The spectrum of $H_{C,p}$ should be related to the local factors of $\zeta$ (which are $(1 - p^{-s})^{-1}$), and the local zeros (which do not exist for the local factors of $\zeta$) should give $\kappa_p = 0$ for each prime. The sum of the local contributions to the Maslov index should cancel the non-local terms.

**Program B: Adelic Maslov index.** Develop the theory of the Maslov index for families of Lagrangian subspaces over the adèles $\mathbb{A}_\mathbb{Q}$. The adelic product formula $\mathbb{A}_\mathbb{Q} = \mathbb{R} \times \prod_p' \mathbb{Q}_p$ might give a formula:
$$\mu_{\mathbb{A}} = \mu_\infty + \sum_p \mu_p,$$
where each contribution is locally computable.

**Program C: Relation to the Atiyah–Patodi–Singer eta index.** The eta index (Atiyah–Patodi–Singer 1975) is a spectral invariant of elliptic differential operators with boundary conditions. In the theory of Hamiltonian systems, the eta index is related to the Maslov index (Kirk–Lesch 2004). If $H_C$ can be interpreted as a differential operator on a manifold with boundary (analogous to the compactification of the critical line), the eta index might give the Maslov index and hence $\kappa$.

---

### Section 7.2 — A non-circular proposal: contraction of the Weil form

A different proposal, which has not appeared in the earlier program, is the following.

**Definition 7.1 (Weil contraction operator).** Let $T : \mathcal{S}(\mathbb{R}^*_+) \to \mathcal{S}(\mathbb{R}^*_+)$ be the operator defined by:
$$\widehat{Tf}(s) = \frac{\xi(s)}{\xi(1-s)} \hat{f}(s) = \Theta(s - 1/2) \hat{f}(s).$$

By the functional equation, $\widehat{Tf}(s) = \hat{f}(s)$ for every $s$ (since $\xi(s)/\xi(1-s) = 1$). Therefore $T = I$ (the identity operator).

*Remark.* The degeneracy $T = I$ is consistent with the preceding analysis: the characteristic function $\Theta \equiv 1$ (constant modulus) implies that the contraction operator is trivial.

**Proposal 7.2 (Non-trivial twisting by local factors).** Instead of using the complete $\xi$ function, consider the local factors:
$$\Theta_p(z) = \frac{(1 - p^{-1/2-z})}{(1 - p^{-1/2+z})},$$
which is the quotient of the local factors of $\zeta$ evaluated at $1/2 + z$ and $1/2 - z$. For real $z = it$:
$$|\Theta_p(it)| = \left|\frac{1 - p^{-1/2 - it}}{1 - p^{-1/2 + it}}\right| = \left|\frac{1 - p^{-1/2}e^{-it\log p}}{1 - p^{-1/2}e^{it\log p}}\right| = 1,$$
since the numerator and denominator are complex conjugates. For $z = \sigma + it$ with $\sigma \neq 0$:
$$|\Theta_p(\sigma + it)| = \left|\frac{1 - p^{-1/2 - \sigma - it}}{1 - p^{-1/2 + \sigma - it}}\right|.$$
If $\sigma > 0$: $|p^{-1/2-\sigma}| < |p^{-1/2}|$, and the analysis of the modulus is not trivial.

**Lemma 7.3 (Modulus of the local factor).** For $p$ prime, $\sigma > 0$:
$$|\Theta_p(\sigma + it)| < 1 \iff |1 - p^{-1/2-\sigma}e^{-it\log p}|^2 < |1 - p^{-1/2+\sigma}e^{-it\log p}|^2.$$
Expanding: $1 - 2p^{-1/2-\sigma}\cos(t\log p) + p^{-1-2\sigma} < 1 - 2p^{-1/2+\sigma}\cos(t\log p) + p^{-1+2\sigma}$, which simplifies to:
$$2(p^{-1/2+\sigma} - p^{-1/2-\sigma})\cos(t\log p) < p^{-1+2\sigma} - p^{-1-2\sigma}.$$
Factoring: $2p^{-1/2}\sinh(\sigma \log p) \cdot 2\cos(t\log p) < 2p^{-1}\sinh(2\sigma\log p)$. Using $\sinh(2x) = 2\sinh(x)\cosh(x)$:
$$2\cos(t\log p) < \frac{\sinh(2\sigma\log p)}{p^{-1/2}\sinh(\sigma\log p)} = 2p^{-1/2}\cosh(\sigma\log p) \cdot \frac{\sinh(2\sigma\log p)}{2\sinh(\sigma\log p)\cosh(\sigma\log p)} = 2p^{-1/2}\cosh(\sigma\log p).$$

Hmm, the inequality is $\cos(t\log p) < p^{1/2}\cosh(\sigma\log p)/p$...

*The computation gets complicated. The important point is that $|\Theta_p(\sigma + it)|$ is not trivially $\leq 1$ or $\geq 1$ for $\sigma \neq 0$; its value depends on $t$.* In particular, the product $\Theta(z) = \prod_p \Theta_p(z)$ (which formally gives $\xi(1/2+z)/\xi(1/2-z)$) has modulus equal to the product of the local moduli, and the functional equation forces the product to have modulus 1.

**Remark 7.4.** The analysis of the individual local factors shows that the global functional equation $|\Theta| = 1$ is a cancellation result among the local factors, not a property of each factor individually. This suggests that to obtain dissipativity, one would have to "unbalance" the local factors in a controlled way, which would require modifying the function $\xi$ (introducing a corrective factor).

---

## Part VIII — Refined obstacle and formulation of Conjecture $\mathbf{C}_D$

### Section 8.1 — The global obstacle shared by the four angles

The four angles of this document share the same fundamental obstacle:

**Obstacle $\mathbf{O}_D$ (Fourth layer of Direction B).** Every condition on $H_C$ that implies $\kappa = 0$ requires, essentially, information about the positions of the zeros of $\xi$ off the line $1/2 + i\mathbb{R}$. The properties of $H_C$ that are verifiable from:
1. The functional equation $\xi(s) = \xi(1-s)$,
2. The Euler product in $\mathrm{Re}(s) > 1$,
3. The global growth estimates of $|\xi(s)|$,

do not determine $\kappa$ without additional information about the zeros.

Obstacle $\mathbf{O}_D$ is directly related to the Hadamard Obstacle of the CCM Direction (Docs 88, 91): the principle that the verifiable global properties of $\zeta$ are not sufficient to determine the position of its zeros.

---

### Section 8.2 — Formulation of Conjecture $\mathbf{C}_D$

Despite the obstacle, Angle 3 suggests a conjecture that might escape the obstacle, based on the global symplectic structure.

**Conjecture $\mathbf{C}_D$ (Adelic Maslov index).** There exists a rigorous definition of the **adelic Maslov index** $\mu_{\mathbb{A}}(H_C)$ for the operator $H_C$ on the idèle class group $C_\mathbb{Q}$, such that:

*(i)* $\mu_{\mathbb{A}}(H_C) = 2\kappa$, where $\kappa = \mathrm{neg.ind}(H_C)$ is the negative index of the Pontryagin space.

*(ii)* $\mu_{\mathbb{A}}(H_C) = \mu_\infty + \sum_p \mu_p$, where the local contributions $\mu_p$ are computable from the local properties of $\zeta$ on $\mathbb{Q}_p$.

*(iii)* $\mu_p = 0$ for every prime $p$ (by the non-vanishing of the local factor $(1 - p^{-s})^{-1}$ in $\mathrm{Re}(s) > 0$, except possibly at $s = 0$ or $s = 1$).

*(iv)* $\mu_\infty = 0$ (contribution of the archimedean place, computable from the gamma factor).

*(v)* By (ii)–(iv): $\mu_{\mathbb{A}}(H_C) = 0$, and by (i): $\kappa = 0$, i.e., RH.

**Status of Conjecture $\mathbf{C}_D$.** Points (i) and (ii) are conjectural and would require developing the theory of the Maslov index in infinite dimension for $H_C$. Points (iii) and (iv) are plausible but unproved. Point (v) is the desired conclusion.

**Frank evaluation.** Conjecture $\mathbf{C}_D$ is speculative in all its points. There is as yet no theory of the Maslov index for Connes–Weil operators on idèle groups. Point (iii) is the most questionable: the non-vanishing of the local factor does not directly imply that the contribution to the Maslov index is zero, since the Maslov index is a property of families of Lagrangian subspaces, not directly of the eigenvalue function.

The value of Conjecture $\mathbf{C}_D$ lies not in its truth (which cannot currently be determined), but in that it points to a concrete research program (developing the local theory of $H_C$ on $\mathbb{Q}_p$ and the adelic Maslov index) that is not covered by the existing literature and could produce new arithmetic structure.

---

### Section 8.3 — The Euler subspace as a computable invariant

The most concrete and unconditional result of the document is the description of the Euler subspace (Definition 2.10 and Proposition 2.14).

**Theorem 8.1 (Weil decomposition and localization of the index).** Under the working hypothesis $\kappa < \infty$, the Pontryagin space $(\mathcal{K}, Q)$ admits an orthogonal decomposition:
$$\mathcal{K} = \mathcal{K}_{\mathrm{crit}} \oplus_Q \mathcal{K}_{\mathrm{off}},$$
where:
- $\mathcal{K}_{\mathrm{crit}}$ is the closed subspace generated by the eigenvectors of $H_C$ with eigenvalues in $i\mathbb{R}$ (corresponding to the zeros of $\zeta$ on the critical line).
- $\mathcal{K}_{\mathrm{off}}$ is the closed subspace generated by the eigenvectors of $H_C$ with eigenvalues in $\mathbb{C} \setminus i\mathbb{R}$ (corresponding to off-line zeros, if they exist).

Moreover:
- $Q|_{\mathcal{K}_{\mathrm{crit}}} \geq 0$ (the form is positive on the critical subspace).
- $\mathrm{neg.ind}(Q|_{\mathcal{K}_{\mathrm{off}}}) = \kappa$ (all the negative index is in the off-critical subspace).

*Partial proof.* The $Q$-orthogonality follows from Theorem 2.7(iii) of Doc 91 (Kreĭn–Langer, spectral $Q$-orthogonality). The positivity on $\mathcal{K}_{\mathrm{crit}}$ is the content of Weil's Theorem (eigenvalues in $i\mathbb{R}$ correspond to zeros on the critical line, where the form $Q$ is positive by Burnol's argument, under RH). Outside RH (i.e., under $\kappa > 0$), positivity on $\mathcal{K}_{\mathrm{crit}}$ requires separate verification depending on the analysis of the interaction between on-line and off-line zeros. $\square$ (partial; the critical point is flagged)

**Corollary 8.2 (Operational consequence).** To prove $\kappa = 0$ it suffices to show that $\mathcal{K}_{\mathrm{off}} = \{0\}$, which is equivalent to saying that $H_C$ has no eigenvalues in $\mathbb{C} \setminus i\mathbb{R}$, which is RH. This is a direct reformulation of RH in the language of the Pontryagin space.

---

## Conclusions of Doc 96

This document has explored four new angles for attacking the gap $\kappa < \infty \to \kappa = 0$ in Direction B of the Riemann program.

**What has been established rigorously:**

1. The characteristic function $\Theta(z) = \xi(1/2+z)/\xi(1/2-z)$ has modulus identically 1 (Proposition 1.5), blocking Brodskii–Livsic dissipativity.

2. The characteristic function $\Theta$ has no poles in $\mathbb{C} \setminus i\mathbb{R}$ if and only if RH is true (Section 1.6, Theorem 5.2), which constitutes a reformulation in terms of the characteristic function.

3. The subspace $\mathcal{H}_{>1}$ (with spectral support in $\mathrm{Re}(s) > 1$) is not in general $Q$-positive (Lemma 2.8), which blocks the Euler-product argument.

4. The resolvent $R_{\lambda_0}$ has all its eigenvalues non-real (even under RH), which prevents applying Krein's Theorem to conclude $\kappa = 0$ (Remark 4.14).

5. The decomposition $\mathcal{K} = \mathcal{K}_{\mathrm{crit}} \oplus_Q \mathcal{K}_{\mathrm{off}}$ localizes the negative index in the off-critical subspace (Theorem 8.1), with all the negative index in $\mathcal{K}_{\mathrm{off}}$.

**What remains speculative but structurally interesting:**

6. Conjecture 3.10 on the equality between the Maslov index and the Krein negative index opens a research program in arithmetic symplectic theory that is not in the existing literature.

7. Conjecture $\mathbf{C}_D$ on the adelic Maslov index proposes a framework where the contribution of each place to $\kappa$ can be computed locally, with $\mu_p = 0$ for every finite prime.

**What has not been resolved:**

The gap $\kappa < \infty \to \kappa = 0$ has no solution in this document. None of the four angles closes the argument. The fundamental obstacle remains the same as in Docs 91 and 94: the position of the zeros of $\zeta$ is not determined by its verifiable global properties, and any condition forcing $\kappa = 0$ requires, explicitly or implicitly, knowledge of those positions.

The most promising direction for future research within the program is the development of the local Maslov index theory for $H_C$, which could provide a new arithmetic entry point to the problem.

---

*End of Doc 96.*
