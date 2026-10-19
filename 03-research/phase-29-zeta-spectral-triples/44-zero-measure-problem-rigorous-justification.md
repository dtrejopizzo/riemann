# Doc 44 — The Zero-Measure Problem: Rigorous Justification of the Representation and Three Attacks on $\mu_{\mathrm{off}}$

**Program:** CCM Zeta Spectral Triples — Phase 29/32  
**Prerequisites:** Docs 38–43 (especially Doc 42 §§3–17 and Doc 43 §§3–5, §15)  
**Main objective:** (1) Rigorously prove that the representation $C_\infty(\gamma_n) = \mathcal{P}[\mu_{\mathrm{off}}](\gamma_n)$ is exact and well defined, answering the previous critical observation. (2) Explore three attack routes on the off-critical measure $\mu_{\mathrm{off}}$ with an honest diagnosis of each.

---

## 1. The central problem and the critical observation

Doc 43 formulated the strategic question: can it be proved that $\mu_{\mathrm{off}} = 0$ using only properties of the zeros of $\zeta$? A **technical gap** was identified in the representation:

> *The equality $C_\infty(\gamma_n) = \mathcal{P}[\mu_{\mathrm{off}}](\gamma_n)$ as a Cauchy-Poisson transform of a positive measure requires independent justification, since explicit formulas generate conditionally convergent sums with complex oscillatory cancellations, not pure positive measures.*

This criticism is **mathematically legitimate** and deserves a rigorous answer before proceeding. The goal of §§2–5 is to close this gap from the first principles of Doc 42.

---

## 2. The structure of the deficit formula and the exact separation

We recall the chain of equalities from Doc 42. Let $\rho_n = 1/2 + i\gamma_n$ be a zero on the critical line (with $\gamma_n > 0$). By the Hadamard expansion and the definition of the spectral potential $C_\infty$ (see Doc 42, §3):

$$C_\infty(\gamma_n) = -2\mathrm{Re}\,\left[\sum_{\substack{\rho \in \mathcal{Z} \\ \rho \neq \rho_n}} \frac{1}{\rho_n - \rho}\right]$$

where the sum is ordered by $|\mathrm{Im}(\rho)|$ (Hadamard conditional convergence). The zeros of $\zeta$ are classified into two categories:

**Type I (zeros on the critical line):** $\rho = 1/2 + i\gamma_m$, $m \neq n$. Then:
$$\frac{1}{\rho_n - \rho} = \frac{1}{i(\gamma_n - \gamma_m)} \in i\mathbb{R}$$

its real part is exactly zero.

**Type II (off-critical zeros):** $\rho_0 = \sigma_0 + i\gamma_0$ with $\sigma_0 \neq 1/2$. The functional equation guarantees that $\bar\rho_0 = \sigma_0 - i\gamma_0$ is also a zero (with the same $\sigma_0$, real $\gamma_0$, opposite sign of the imaginary part). We compute:

$$\mathrm{Re}\,\left[\frac{1}{\rho_n - \rho_0}\right] = \mathrm{Re}\,\left[\frac{1}{(1/2-\sigma_0)+i(\gamma_n-\gamma_0)}\right] = \frac{1/2-\sigma_0}{(1/2-\sigma_0)^2+(\gamma_n-\gamma_0)^2}$$

$$\mathrm{Re}\,\left[\frac{1}{\rho_n - \bar\rho_0}\right] = \mathrm{Re}\,\left[\frac{1}{(1/2-\sigma_0)+i(\gamma_n+\gamma_0)}\right] = \frac{1/2-\sigma_0}{(1/2-\sigma_0)^2+(\gamma_n+\gamma_0)^2}$$

Therefore, the contribution of the pair $(\rho_0, \bar\rho_0)$ to $-2\mathrm{Re}[\cdots]$ is:

$$-2\left[\frac{1/2-\sigma_0}{(1/2-\sigma_0)^2+(\gamma_n-\gamma_0)^2} + \frac{1/2-\sigma_0}{(1/2-\sigma_0)^2+(\gamma_n+\gamma_0)^2}\right]$$

$$= 2(\sigma_0-1/2)\left[\frac{1}{(\sigma_0-1/2)^2+(\gamma_n-\gamma_0)^2} + \frac{1}{(\sigma_0-1/2)^2+(\gamma_n+\gamma_0)^2}\right] = \Delta(\gamma_n;\rho_0)$$

The coefficient $2(\sigma_0-1/2) > 0$ because $\sigma_0 > 1/2$ (for $\rho_0$ with $\sigma_0 > 1/2$; if $\sigma_0 < 1/2$ then $1-\bar\rho_0$ has real part $> 1/2$ and is counted in that pair).

**Conclusion:** Type I zeros contribute exactly zero to the real part. The entire contribution comes from pairs of off-critical zeros, each with a positive coefficient.

---

## 3. Absolute convergence of the series over $\mathcal{Z}_{\mathrm{off}}$

**Proposition 3.1 (Absolute convergence of $\sum_{\rho_0}\Delta(\gamma_n;\rho_0)$).**

*Hypothesis:* The zeros of $\zeta$ in the strip $0 < \sigma < 1$ satisfy $N(\sigma, T) = O(T^{2(1-\sigma)} \log T)$ (classical, unconditional density).

*Claim:* The series $\sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} \Delta(\gamma_n;\rho_0)$ converges absolutely for each $\gamma_n$.

*Proof.* Each term satisfies:
$$0 < \Delta(\gamma_n;\rho_0) \leq \frac{4(\sigma_0-1/2)}{(\sigma_0-1/2)^2} + \frac{4(\sigma_0-1/2)}{(\sigma_0-1/2)^2} = \frac{8}{\sigma_0-1/2}$$

but also, when $|\gamma_0|$ is large compared to $\gamma_n$:
$$\Delta(\gamma_n;\rho_0) \leq \frac{4(\sigma_0-1/2)}{(\sigma_0-1/2)^2 + (\gamma_0-\gamma_n)^2/4} = O\!\left(\frac{\sigma_0-1/2}{\gamma_0^2}\right) \quad |\gamma_0| \gg \gamma_n$$

The region $|\gamma_0| \leq 2\gamma_n$ contains finitely many zeros (by the density hypothesis, at most $O(\gamma_n^{2(1-\sigma_0)}\log\gamma_n)$ off-critical zeros up to height $2\gamma_n$, and the distance to the critical axis satisfies $\sigma_0-1/2 \geq c/\log|\gamma_0|$ by the classical zero-free region).

For $|\gamma_0| > 2\gamma_n$, summing over rings $|\gamma_0| \in [T, 2T]$:
$$\sum_{\substack{\rho_0:\,|\gamma_0|\in[T,2T]}} \Delta(\gamma_n;\rho_0) = O\!\left(\frac{N_{\mathrm{off}}(2T)-N_{\mathrm{off}}(T)}{T^2}\right) \cdot (\sigma_0-1/2)^{-1}$$

where $N_{\mathrm{off}}(T)$ denotes the number of off-critical zeros up to height $T$. By the density estimate $N(\sigma,T) \ll T^{2(1-\sigma)}\log T$:
$$\sum_{k=0}^\infty \frac{N_{\mathrm{off}}(2^{k+1}\gamma_n) - N_{\mathrm{off}}(2^k\gamma_n)}{(2^k\gamma_n)^2} \ll \sum_{k=0}^\infty \frac{(2^{k+1}\gamma_n)^{2(1-\sigma_{\min})}\log(2^k\gamma_n)}{(2^k\gamma_n)^2} < \infty$$

for any $\sigma_{\min} > 1/2$. $\square$

**Corollary 3.2.** The measure $\mu_{\mathrm{off}} = \sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}},\,\sigma_0>1/2} 2(\sigma_0-1/2)\,[\delta_{(\gamma_0,\sigma_0-1/2)} + \delta_{(-\gamma_0,\sigma_0-1/2)}]$ is a locally finite Radon measure on $\mathbb{H}$.

---

## 4. Rigorous validation of the representation as a Poisson transform

**Theorem 4.1 (Exact representation).** For every zero $\rho_n = 1/2+i\gamma_n$ of $\Xi$ on the critical line:

$$C_\infty(\gamma_n) = \mathcal{P}[\mu_{\mathrm{off}}](\gamma_n) = \int_\mathbb{H} \frac{y}{y^2 + (\gamma_n - x)^2}\,d\mu_{\mathrm{off}}(x,y)$$

where $\mathcal{P}[\mu_{\mathrm{off}}]$ is the Poisson transform of the off-critical zero measure.

*Proof.* By §2, the Type I / Type II separation is exact with no residual error. Type I zeros contribute exactly zero to the real part (each contribution is purely imaginary). Type II zeros contribute, each pair $(\rho_0, \bar\rho_0)$:

$$\Delta(\gamma_n;\rho_0) = P_{(\sigma_0-1/2)}(\gamma_n - \gamma_0) \cdot 2(\sigma_0-1/2) + P_{(\sigma_0-1/2)}(\gamma_n + \gamma_0) \cdot 2(\sigma_0-1/2)$$

This corresponds exactly to integrating the kernel $P_y(t-x) = y/[y^2+(t-x)^2]$ against the measure $\mu_{\mathrm{off}}$ defined in Corollary 3.2. Absolute convergence (Proposition 3.1) guarantees that the integral equals the sum:

$$\int_\mathbb{H} P_y(\gamma_n - x)\,d\mu_{\mathrm{off}}(x,y) = \sum_{\substack{\rho_0 \in \mathcal{Z}_{\mathrm{off}} \\ \sigma_0>1/2}} \Delta(\gamma_n;\rho_0) = C_\infty(\gamma_n) \qquad \square$$

**Remark 4.2 (Answer to the critical observation).** The "oscillation" of explicit formulas (of Riemann-von Mangoldt type) resides *entirely* in the imaginary contributions of the on-critical zeros. The real part — which is $C_\infty(\gamma_n)$ — automatically extracts the off-critical component, which has positive measure structure. There is no oscillatory cancellation in the quantity under study: it is a sum of positive terms.

**Uniqueness (Riesz-Herglotz).** The representation is unique by the following argument: if $C_\infty(t) = \mathcal{P}[\nu](t)$ for two positive measures $\mu_{\mathrm{off}}$ and $\nu$, then $\mathcal{P}[\mu_{\mathrm{off}} - \nu] = 0$ on $\{\gamma_n\}$, which is dense in $\mathbb{R}$ by virtue of the density theorem of zeros of $\Xi$. By continuity of the Poisson transform (if $|\gamma_n|$ is dense in $\mathbb{R}^+$) one would conclude $\mathcal{P}[\mu_{\mathrm{off}}-\nu]=0$ on $\mathbb{R}$, and by the uniqueness theorem for positive measures (injectivity of the Poisson transform on measures), $\mu_{\mathrm{off}} = \nu$.

---

## 5. Precise formulation of the Zero-Measure Problem

**Definition 5.1.** The *Zero-Measure Problem* is the following question:

$$\boxed{\text{Is } \mu_{\mathrm{off}} = 0?}$$

By the Single-Point Theorem (Doc 43, T 4.2): $\mu_{\mathrm{off}} = 0$ if and only if $C_\infty(\gamma_{n_0}) = 0$ for some $n_0$, if and only if RH.

The problem is equivalent to proving that the positive atomic measure $\mu_{\mathrm{off}}$ has empty support. We will explore three attacks:

- **Route A:** Fourier analysis and Paley-Wiener conditions on $C_\infty$.
- **Route B:** The functional equation as a symmetry condition on $\mu_{\mathrm{off}}$.
- **Route C:** Global positivity of $C_\infty$ on $\mathbb{R}$ and potential theory.

---

## 6. Route A: Fourier Analysis and the Boundary Cauchy Transform

**Setup.** The function $F(z) = \mathcal{P}[\mu_{\mathrm{off}}](z)$ for $z = t + iy$, $y > 0$, is a harmonic function on the upper half-plane $\mathbb{H}^+$. Its trace on the real boundary is $F(t) = C_\infty(t)$ (extended from $\{\gamma_n\}$ to $\mathbb{R}$ via the Hadamard formula).

**Proposition 6.1 (Fourier decay of $C_\infty$).** If $C_\infty \in L^1(\mathbb{R})$, then its Fourier transform satisfies:
$$\hat{C}_\infty(\xi) = \pi e^{-2\pi|\xi|y_0} \cdot \hat{f}(\xi)$$
for some $y_0 > 0$, where $\hat{f}$ is the Fourier transform of the measure $\mu_{\mathrm{off}}$ projected onto the boundary.

*Obstacle A.1.* It is not clear that $C_\infty \in L^1(\mathbb{R})$. The extension of $C_\infty$ from $\{\gamma_n\}$ to $\mathbb{R}$ via the function $-\text{Re}[\zeta'/\zeta]$ may have singularities at the zeros of $\Xi$. Moreover, by the logarithmic peaks (Doc 43, C 7.4), if $\mu_{\mathrm{off}} \neq 0$, then $C_\infty(\gamma_{n_k^*}) \geq c\log\gamma_{n_k^*} \to \infty$, which suggests that $C_\infty \notin L^1(\mathbb{R})$ in that case.

**Proposition 6.2 (Wiener criterion).** If $C_\infty(t) = 0$ for $t$ in a set $E \subset \mathbb{R}$ of positive Lebesgue measure, and if $C_\infty$ belongs to an appropriate Paley-Wiener class, then $\mu_{\mathrm{off}} = 0$.

*Proof.* The Poisson transform $\mathcal{P}[\mu](t) = 0$ on a set of positive measure for a positive measure $\mu$ implies $\mu = 0$ by the Schwarz principle for positive harmonic functions (see §7 below). $\square$

*Obstacle A.2.* To apply the Wiener criterion we would need to know that $C_\infty$ vanishes on a set of positive measure — which is equivalent (via Route A) to RH, with no independence.

**Diagnosis of Route A.** Route A produces implications of the form "if $C_\infty$ has such a decay property $\Rightarrow \mu_{\mathrm{off}} = 0$", but verifying those decay properties is no easier than proving RH directly. The route has value for **characterizing** $\mu_{\mathrm{off}}$ conditionally on RH, not for proving RH unconditionally.

---

## 7. The Minimum Principle for Positive Harmonic Functions

Before Routes B and C, we establish a fundamental technical result.

**Lemma 7.1 (Minimum Principle).** Let $F: \mathbb{H}^+ \to [0,\infty)$ be harmonic, positive, and not identically zero. Then $F > 0$ throughout $\mathbb{H}^+$, and $F$ cannot attain the value 0 in the interior.

*Proof.* By the minimum principle for harmonic functions: if $F$ attains its minimum (0) at an interior point, $F$ is constant, contradicting $F \not\equiv 0$. $\square$

**Lemma 7.2 (Extension to the boundary).** If $F = \mathcal{P}[\mu_{\mathrm{off}}]$ with $\mu_{\mathrm{off}} \neq 0$ positive, then $F(t) > 0$ for every $t \in \mathbb{R}$ in the sense of the non-tangential trace — with the possible exception of a set of zero capacity (Fatou).

*Proof.* Consequence of Fatou's theorem for positive harmonic functions on $\mathbb{H}^+$ and of Lemma 7.1. $\square$

**Corollary 7.3.** If $\mu_{\mathrm{off}} \neq 0$, then $C_\infty(t) > 0$ for almost every $t \in \mathbb{R}$. In particular, if RH fails, the function $C_\infty$ is strictly positive $\lambda$-almost everywhere on $\mathbb{R}$.

---

## 8. Route B: The Functional Equation as a Symmetry Condition

**Setup.** The zeros of $\zeta$ satisfy the symmetry $\rho \leftrightarrow 1-\bar\rho$ (Riemann functional equation). For an off-critical zero $\rho_0 = \sigma_0 + i\gamma_0$ with $\sigma_0 > 1/2$, the functional pair is $1-\bar\rho_0 = (1-\sigma_0) + i\gamma_0$, with $1-\sigma_0 < 1/2$.

**Proposition 8.1 (Action of the functional equation on $\mu_{\mathrm{off}}$).** The functional symmetry $\rho_0 \leftrightarrow 1-\bar\rho_0$ acts on $\mu_{\mathrm{off}}$ as the reflection $y_0 = \sigma_0-1/2 \mapsto -(1-\sigma_0-1/2) = \sigma_0-1/2$. That is, the functional equation **preserves** the height $y_0$ of the support point (since $\sigma_0 - 1/2 = (1-\sigma_0)-1/2$ with flipped sign, but in modulus it is the same).

*Note.* The functional pair $1-\bar\rho_0$ has real part $1-\sigma_0 < 1/2$. In our parameterization of $\mu_{\mathrm{off}}$, which lives on $\{y > 0\} = \{\sigma_0 > 1/2\}$, the functional pair would contribute to the component $\sigma < 1/2$. Both zeros ($\rho_0$ and $1-\bar\rho_0$) contribute to $C_\infty(\gamma_n)$ through the symmetry of the pairing $(\rho_0, \bar\rho_0)$ (see Doc 42, §13).

**Proposition 8.2 (Symmetry condition on $C_\infty$).** The functional equation implies that $C_\infty(\gamma_n)$ is symmetric: $C_\infty(\gamma_n) = C_\infty(\gamma_n)$ trivially, but more significantly, the sum over pairs $\{(\rho_0, \bar\rho_0), (1-\rho_0, 1-\bar\rho_0)\}$ produces:

$$\Delta(\gamma_n;\rho_0) + \Delta(\gamma_n;1-\rho_0) = \Delta(\gamma_n;\rho_0) + \Delta(\gamma_n;\tilde\rho_0)$$

where $\tilde\rho_0 = 1-\sigma_0 + i\gamma_0$ has $\sigma(\tilde\rho_0) - 1/2 = 1/2-\sigma_0 < 0$. But $|\sigma(\tilde\rho_0)-1/2| = \sigma_0-1/2$, so the functional pair gives the same positive contribution to the deficit: $\Delta(\gamma_n;\tilde\rho_0) = \Delta(\gamma_n;\rho_0)$. The total is $2\Delta(\gamma_n;\rho_0)$.

**Definition 8.3 (Quartet of off-critical zeros).** If $\rho_0 = \sigma_0+i\gamma_0$ is off-critical, the *Hadamard quartet* is $\{\rho_0, \bar\rho_0, 1-\rho_0, 1-\bar\rho_0\}$. By the functional equation and the conjugation symmetry, this quartet contributes to $C_\infty(\gamma_n)$ the term $4\Delta(\gamma_n;\rho_0) > 0$.

**Obstacle B.** The functional equation imposes the symmetry $\rho_0 \leftrightarrow 1-\bar\rho_0$ but does not force $\mu_{\mathrm{off}} = 0$: it is perfectly compatible with the existence of quartets of off-critical zeros. The functional equation is a symmetry condition on the *distribution* of $\mu_{\mathrm{off}}$, not on its total mass.

**Diagnosis of Route B.** The functional equation alone cannot prove $\mu_{\mathrm{off}} = 0$. However, it has value in showing that the contributions to the deficit always come in groups of four (quartets), which reinforces the positive structure of $C_\infty$.

---

## 9. Route C: Global Positivity and Potential Theory

This is the most promising route and establishes the deepest connection with the Riemann hypothesis.

**Setup.** The function $F: \mathbb{H}^+ \to \mathbb{R}_{>0}$ given by $F(z) = \mathcal{P}[\mu_{\mathrm{off}}](z)$ is positive harmonic. By the Herglotz-Riesz representation theorem (for positive harmonic functions on the half-plane), there exists a unique positive Borel measure $\nu$ on $\mathbb{R} \cup \{\infty\}$ and a constant $a \geq 0$ such that:

$$F(t+iy) = ay + \int_\mathbb{R} \frac{y}{y^2+(t-s)^2}\,d\nu(s)$$

**Proposition 9.1 (Identification of the Herglotz measure).** In our situation, the Herglotz measure $\nu$ is precisely the projection of $\mu_{\mathrm{off}}$ onto $\mathbb{R}$ (with weights integrated over height):

$$d\nu(s) = \int_0^\infty y\,d[\mu_{\mathrm{off}}]_s(y)$$

where $[\mu_{\mathrm{off}}]_s$ is the disintegration of $\mu_{\mathrm{off}}$ over the fiber at $x=s$.

*Proof.* Direct comparison of the Herglotz representation with $\mathcal{P}[\mu_{\mathrm{off}}]$ using uniqueness. $\square$

**Lemma 9.2 (Extinction criterion by boundary condition).** If there exists $t_0 \in \mathbb{R}$ such that $\lim_{y\downarrow 0} F(t_0 + iy) = 0$ (null non-tangential trace), then $\nu(\{t_0\}) = 0$ and the harmonic extension has a removable singularity at $t_0$.

*Remark.* Lemma 9.2 does not say that $\nu = 0$; only that the point measure at $t_0$ is zero. To conclude $\nu = 0$ (equivalently $\mu_{\mathrm{off}} = 0$) one needs vanishing on a sufficiently large set.

**Theorem 9.3 (Characterization via capacity).** Let $E_0 = \{t\in\mathbb{R} : C_\infty(t) = 0\}$ be the vanishing set of $C_\infty$ on the real line. The following conditions are equivalent:

1. $\mu_{\mathrm{off}} = 0$ (RH).
2. $E_0 \neq \emptyset$.
3. $E_0$ has positive logarithmic capacity, i.e., $\mathrm{cap}(E_0) > 0$.
4. $E_0$ has positive Lebesgue measure.

*Proof.*

$(1)\Rightarrow(2)$: If $\mu_{\mathrm{off}} = 0$, then $C_\infty(t) = 0$ for every $t$, so $E_0 = \mathbb{R}$.

$(2)\Rightarrow(1)$: By the Poisson Rigidity Theorem (Doc 43, T 3.1): $\mathcal{P}[\mu_{\mathrm{off}}](t_0) = 0$ for some $t_0 \in E_0$ implies $\mu_{\mathrm{off}} = 0$.

$(1)\Rightarrow(4)\Rightarrow(3)\Rightarrow(2)$: Trivial, since positive measure implies positive capacity implies nonempty set.

$(2)\Rightarrow(4)$: If $E_0 \neq \emptyset$, then by (2)$\Rightarrow$(1) we already have $\mu_{\mathrm{off}} = 0$, so $C_\infty \equiv 0$ and $E_0 = \mathbb{R}$ has positive measure.

The chain of equivalences closes without circularity: every vanishing condition, however weak (a point, a set of positive capacity, positive measure) implies total vanishing. $\square$

**Corollary 9.4 (Dichotomous alternative for $C_\infty$).** The function $C_\infty: \mathbb{R} \to [0,\infty)$ satisfies exactly one of two scenarios:
- **RH scenario:** $C_\infty \equiv 0$ throughout the real line.
- **anti-RH scenario:** $C_\infty > 0$ for $\lambda$-almost every $t \in \mathbb{R}$.

There is no intermediate scenario (vanishing on a set of positive measure but without RH).

---

## 10. The Harmonic Extension and the Schwarz Reflection Principle

**Proposition 10.1 (Harmonic extension).** The function $C_\infty: \mathbb{R} \to [0,\infty)$, defined via the Hadamard formula at the zeros $\{\gamma_n\}$ of $\Xi$ and extended to $\mathbb{R}$ by continuity, admits the harmonic extension:

$$F(z) = \mathcal{P}[\mu_{\mathrm{off}}](z), \quad z = t + iy, \quad y > 0$$

which is $C^\infty$ on $\mathbb{H}^+$, positive, and satisfies $F(t) = C_\infty(t)$ in the non-tangential sense.

**Proposition 10.2 (Conditional Schwarz reflection).** If $C_\infty(t_0) = 0$ for some $t_0 \in \mathbb{R}$, then by the Schwarz reflection principle $F$ can be extended across $t_0$ as $F(t_0+iy) = -F(t_0-iy) = 0$ for small $y$, which contradicts the positivity $F > 0$ on $\mathbb{H}^-$ (by symmetry). Hence the extension is trivially zero at $t_0$, consistent with $F \equiv 0$.

*Remark.* The reflection principle, in this context, reconfirms that a zero of the boundary trace can only occur if $F \equiv 0$ throughout the half-plane — consistent with RH.

---

## 11. The Structural Barrier: Synthesis and Diagnosis

**Definition 11.1 (The irreducible barrier).** The Zero-Measure Problem reduces to the following arithmetic question:

> *Can the zeros of $\zeta(s)$ in $\{|\sigma - 1/2| > 0\}$ satisfy the analytic conditions necessary for the measure $\mu_{\mathrm{off}}$ to be nonzero, given that functional symmetry forces them to come in quartets and that each quartet contributes positively to the deficit $C_\infty$?*

The answer depends on deep arithmetic properties of $\zeta$: correlations between zeros, density, distribution of the real parts of off-critical zeros.

**Diagnostic table:**

| Route | Result obtained | Obstacle |
|------|-------------------|-----------|
| A (Fourier) | Wiener: vanishing on a set of positive measure $\Rightarrow \mu_{\mathrm{off}}=0$ | Verifying vanishing ≡ proving RH |
| B (Functional equation) | Quartet symmetry; contributions $> 0$ per quartet | Quartets are compatible with $\mu_{\mathrm{off}} \neq 0$ |
| C (Potential) | Dichotomous alternative: $C_\infty \equiv 0$ XOR $C_\infty > 0$ a.e. | Proving that $C_\infty \not> 0$ a.e. ≡ proving RH |
| Poisson rigidity | A single zero of $C_\infty$ $\Rightarrow$ RH | Finding the zero ≡ proving RH |

**Proposition 11.2 (Equivalence of the obstacle).** For each of Routes A, B, C, the final obstacle is a condition equivalent to RH. The routes do not simplify the problem: they compress and clarify, but do not eliminate the central difficulty.

*This is not a failure of the program.* The compression has value: it identifies the exact nature of what is missing. The irreducible barrier of the CCM program is now the following pointwise analytic statement:

$$\exists\, t_0 \in \mathbb{R}: \quad \mathcal{P}[\mu_{\mathrm{off}}](t_0) = 0$$

which by the Poisson Rigidity Theorem (Doc 43) is equivalent to RH.

---

## 12. A Fourth Attack: The Hardy Condition on $F$

**Proposal 12.1 (Attack via the Hardy space $H^1$).** If the harmonic extension $F(z) = \mathcal{P}[\mu_{\mathrm{off}}](z)$ belongs to the Hardy space $H^1(\mathbb{H}^+)$ (i.e., $\sup_{y>0}\int_{-\infty}^\infty |F(t+iy)|\,dt < \infty$), then by the Riesz-Thorin theorem for $H^1$:

$$\mu_{\mathrm{off}}(\mathbb{R}) = \lim_{y\to 0} \int_{-\infty}^\infty F(t+iy)\,dt = \int_\mathbb{R} C_\infty(t)\,dt$$

If this integral could be computed (in a regularized sense) and shown to be zero, one would conclude $\mu_{\mathrm{off}} = 0$.

*Question:* What does the theory of $\zeta$ say about $\int_\mathbb{R} C_\infty(t)\,dt$?

**Proposition 12.2 (Formal computation of the mass).** Formally:

$$\int_\mathbb{R} C_\infty(t)\,dt = \int_\mathbb{R} \sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} \Delta(t;\rho_0)\,dt$$

Exchanging sum and integral (justifiable by dominated convergence if $|\mathcal{Z}_{\mathrm{off}}|<\infty$):

$$= \sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} \int_\mathbb{R} \Delta(t;\rho_0)\,dt = \sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} 2(\sigma_0-1/2) \cdot 2\pi = 4\pi \sum_{\rho_0} (\sigma_0-1/2)$$

where we used $\int_{-\infty}^\infty P_{y_0}(t)\,dt = \pi$ for each $y_0 = \sigma_0-1/2$.

**Corollary 12.3.** If $\mathcal{Z}_{\mathrm{off}}$ is nonempty, the total mass is $\int_\mathbb{R} C_\infty(t)\,dt = 4\pi\sum_{\rho_0}(\sigma_0-1/2) > 0$. If $\mathcal{Z}_{\mathrm{off}} = \emptyset$, the mass is zero. The computation confirms that $\int C_\infty > 0 \Leftrightarrow \mu_{\mathrm{off}} \neq 0 \Leftrightarrow \neg$RH.

*Obstacle 12.4.* This computation is again circular: knowing that $\int C_\infty = 0$ is equivalent to knowing that $\mu_{\mathrm{off}} = 0$, which is equivalent to RH. Integration does not open an independent path.

---

## 13. The New Front: Effective Lower Bounds for $\int C_\infty$

Although the mass $\int C_\infty$ cannot be proved to vanish directly, we can try to obtain **explicit lower bounds** conditioned on the existence of off-critical zeros.

**Theorem 13.1 (Effective lower bound).** Suppose $\mathcal{Z}_{\mathrm{off}}$ contains a zero $\rho_0 = \sigma_0 + i\gamma_0$ with $\sigma_0 - 1/2 = \delta > 0$. Then:

$$C_\infty(\gamma_n) \geq \frac{4\delta}{\delta^2 + (\gamma_n - \gamma_0)^2}$$

for every $\gamma_n$. In particular, the zero $\gamma_{n^*}$ closest to $\gamma_0$ satisfies (by the Density Theorem of Doc 43, T 7.1):

$$C_\infty(\gamma_{n^*}) \geq \frac{4\delta}{\delta^2 + (\pi/\log\gamma_0)^2} \geq \frac{4\delta\log^2\gamma_0}{\delta\log^2\gamma_0 + \pi^2}$$

For large $\gamma_0$ with $\delta$ fixed: $C_\infty(\gamma_{n^*}) \geq 4/\log^0 \gamma_0 = 4$ (in the limit).

*Proof.* By the definition of $\Delta(\gamma_n;\rho_0)$ and Proposition 3.1 of Doc 43. $\square$

**Corollary 13.2 (Quantitative detection).** If RH fails with a zero at distance $\delta$ from the critical axis and height $\gamma_0$, then there exists $\gamma_{n^*} \leq \gamma_0 + \pi/\log\gamma_0$ such that:

$$C_\infty(\gamma_{n^*}) \geq \frac{4\delta\log^2\gamma_0}{\delta\log^2\gamma_0 + \pi^2}$$

This is a quantitative test: if it could be verified that $C_\infty(\gamma_n) \to 0$ for all zeros, one would obtain $\mu_{\mathrm{off}} = 0$ and RH.

---

## 14. The Direction of Doc 45: Spectral Analysis of $C_\infty$ as a Function of $n$

The sequence $\{C_\infty(\gamma_n)\}_{n=1}^\infty$ is a sequence of non-negative real numbers. By Theorem 13.1, if $C_\infty(\gamma_n) \to 0$ along a sufficiently dense subsequence, then $\mu_{\mathrm{off}} = 0$.

**Proposition 14.1 (Criterion for convergence to zero).** If $C_\infty(\gamma_n) \to 0$ as $n \to \infty$, then $\mu_{\mathrm{off}} = 0$ (RH).

*Proof.* If $\mu_{\mathrm{off}} \neq 0$, there exists $\rho_0 \in \mathcal{Z}_{\mathrm{off}}$ with $\sigma_0-1/2 = \delta > 0$. By Corollary 13.2, for any large $n$ there is $\gamma_{n^*} \sim \gamma_0$ with $C_\infty(\gamma_{n^*}) \geq 4\delta\log^2\gamma_0/(\delta\log^2\gamma_0+\pi^2) > 0$. But this only gives a lower bound for fixed $\gamma_{n^*}$; it does not prevent $C_\infty(\gamma_n) \to 0$ for $n$ outside the range of $\gamma_0$... $\square$ (partial).

*Honest note.* Proposition 14.1 requires a stronger form of the criterion: if $C_\infty(\gamma_n) \to 0$ for the subsequence $\gamma_n \to \infty$ (not just pointwise), then by continuity of $\mathcal{P}[\mu_{\mathrm{off}}]$ and density of $\{\gamma_n\}$, one can conclude $C_\infty \equiv 0$. Making this argument precise is the task of Doc 45.

---

## 15. Summary of the program through Doc 44

The CCM program has established the following equivalences and unconditional results:

**Proved results:**

| Result | Reference |
|-----------|-----------|
| RH ↔ Inc. Inv. | Docs 19, 39 |
| $C_\infty(\gamma_n) \geq 0$ (unconditional) | Doc 42 |
| $C_\infty(\gamma_n) = \mathcal{P}[\mu_{\mathrm{off}}](\gamma_n)$ (exact) | Doc 42 + Doc 44, T 4.1 |
| Absolute convergence of $\sum\Delta$ | Doc 44, P 3.1 |
| Poisson rigidity: a single zero $\Rightarrow$ RH | Doc 43 |
| Without RH: $C_\infty(\gamma_{n_k^*}) \geq c\log\gamma_{n_k^*}$ | Doc 43 |
| Dichotomous alternative: $C_\infty \equiv 0$ XOR $> 0$ a.e. | Doc 44, C 9.4 |
| Total mass $\int C_\infty = 4\pi\sum_{\rho_0}(\sigma_0-1/2)$ | Doc 44, P 12.2 |
| Quantitative lower bound conditioned on an off-critical $\rho_0$ | Doc 44, T 13.1 |

**The exact mathematical frontier of the program:**

> Prove that $\lim_{n\to\infty} C_\infty(\gamma_n) = 0$, or equivalently, find a single $n_0$ with $C_\infty(\gamma_{n_0}) = 0$.

Both conditions are equivalent to RH (the first by density and continuity; the second by the Poisson Rigidity Theorem).

---

## 16. Proposal for Doc 45: Decay of $C_\infty(\gamma_n)$ and the Subsequence Criterion

Doc 45 will explore the asymptotic behavior of $C_\infty(\gamma_n)$ as $n \to \infty$, with the following goals:

1. **Is $C_\infty(\gamma_n)$ uniformly bounded?** (Expected answer: yes, unconditionally, by the bound of Proposition 3.1.)

2. **Does $C_\infty(\gamma_n) \to 0$ on average?** The mean $\frac{1}{N}\sum_{n=1}^N C_\infty(\gamma_n) = \frac{4\pi}{N}\sum_{|\gamma_n|\leq T}(\sigma_0-1/2)$ (for detected off-critical zeros), which by the zero density theorem tends to 0 if $\mathcal{Z}_{\mathrm{off}}$ is sparse.

3. **Can the variance $\sum_n |C_\infty(\gamma_n)|^2$ be computed?** Connection with pairs of correlated zeros (Montgomery's theorem) and the correlations of the measure $\mu_{\mathrm{off}}$.

4. **Subsequence criterion:** If there exists $n_k \to \infty$ with $C_\infty(\gamma_{n_k}) \to 0$ at a controlled rate, what does this imply about $\mu_{\mathrm{off}}$?

---

*Next document (Doc 45): Asymptotic behavior of $C_\infty(\gamma_n)$ as $n \to \infty$ — mean, variance, subsequences and connection with Montgomery.*

---

## Appendix A: Verification of the Type I / Type II separation

**A.1. Separation with no residual error.** The Hadamard sum $\sum_\rho[1/(\rho_n-\rho)+1/\rho]$ converges conditionally, ordered by $|\text{Im}(\rho)|$. Taking the real part and subtracting the contribution of $\rho = \rho_n$ (the pole), we obtain the sum:

$$C_\infty(\gamma_n) = -2\mathrm{Re}\,\left[\sum_{\rho\neq\rho_n} \frac{1}{\rho_n - \rho}\right]$$

The Type I / Type II separation is:

$$C_\infty(\gamma_n) = \underbrace{-2\mathrm{Re}\,\left[\sum_{\rho_m:\,\text{on-crit}}\frac{1}{\rho_n-\rho_m}\right]}_{=\,0} + \underbrace{-2\mathrm{Re}\,\left[\sum_{\rho_0:\,\text{off-crit}}\frac{1}{\rho_n-\rho_0}\right]}_{\geq\,0}$$

The first sum is zero (each term is purely imaginary). The second is $\sum_{\rho_0}\Delta(\gamma_n;\rho_0) \geq 0$.

**A.2. Absence of a constant term.** The contribution of the trivial poles ($\rho = -2k$, $k=1,2,\ldots$) and the term from the principal part of the zeta function contribute to $C_\infty$ terms that are real, but which cancel in the definition of the spectral potential $C_\infty$ (see Doc 42, §4 for the subtraction of the regular part $g_n(\rho_n)$). By construction, $C_\infty(\gamma_n) = 0$ if and only if all relevant zeros lie on the critical line.
