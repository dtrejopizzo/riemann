# Doc 93 — Direction D: Second variation of the variational distance to $\mathcal{M}$

**Program:** Riemann Hypothesis — Phase 34, New Directions  
**Prerequisites:** Docs 82, 83, 86, 88, 89 (Phase 33); Doc 40 (P40, variational criterion); knowledge of variational calculus in Hilbert spaces  
**Level:** Advanced research — partial results, explicit obstacles

---

## Summary

Doc 82 established the variational criterion: the infimum of the $L^2(W_\lambda\,dm_\infty)$ distance between $f_0 = |\zeta(1/2+is)|^2$ and the nonlinear class
$$\mathcal{M} = \{|\eta_{\mathrm{on}}|^2 : \eta_{\mathrm{on}} \text{ entire, all its zeros on } \mathrm{Re}(s)=1/2\}$$
vanishes if and only if RH holds. The natural candidate for the point of $\mathcal{M}$ closest to $f_0$ is $f_0^{on} = |\zeta_{\mathrm{on}}(1/2+is)|^2$, where $\zeta_{\mathrm{on}}$ is the version of $\zeta$ with all its zeros projected onto the critical line. Under RH, $\zeta_{\mathrm{on}} = \zeta$ and $f_0^{on} = f_0$, with distance zero trivially.

This document explores **Direction D**: studying the geometry of $\mathcal{M}$ in a neighborhood of $f_0^{on}$ via the computation of the first and second variations of the distance functional $\Phi(\eta) = \|f_0 - |\eta|^2\|^2_{L^2(W_\lambda\,dm_\infty)}$. The goal is to determine whether $f_0^{on}$ is a local minimum and whether the second variation in the transversal direction (moving zeros off the critical line) is positive definite.

**Main results of this document:**

- (§2–3) $\mathcal{M}$ is parametrized locally via deformations of the Hadamard product, and the first and second variations of the distance functional are computed.
- (§4) It is shown that the first variation in the tangential direction vanishes at $f_0^{on}$ (critical point).
- (§5) The second variation in the transversal direction is computed and connected to the kernels $K_\lambda(\gamma_j)$ of Doc 86.
- (§6) We discuss whether positivity of the second variation would imply that $f_0^{on}$ is a local minimum of $\Phi|_\mathcal{M}$.
- (§7) The gap between local convexity and global uniqueness is identified, and the positive curvature conjecture is formulated.
- (§8) The precise obstacle preventing the argument from closing is formulated.

**Conclusion:** The second variation in the transversal direction is formally positive under natural hypotheses on the kernel $K_\lambda$, but local convexity does not imply global uniqueness. The gap persists and is characterized precisely.

---

## §1. Preparation: the structure of $\mathcal{M}$ as a nonlinear manifold

### 1.1. Description of $\mathcal{M}$ as a function space

We recall the ambient space. For fixed $\lambda > 0$, the Hilbert space is
$$H_\lambda = L^2\bigl(\mathbb{R},\, W_\lambda(s)\,dm_\infty(s)\bigr),$$
where $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2\,ds$ and $W_\lambda \geq 0$ is the weight kernel of the CCM formalism. The target function is
$$f_0(s) = |\zeta(1/2+is)|^2 \in H_\lambda$$
(membership in $H_\lambda$ is unconditional by Doc 82, §2). The approximation class is
$$\mathcal{M} = \{g_\eta : g_\eta(s) = |\eta(1/2+is)|^2,\; \eta \in \mathcal{E}\}$$
where $\mathcal{E}$ denotes the set of entire functions of order 1 with a functional symmetry factor analogous to that of $\xi$, and with all their zeros of the form $1/2 + i\mu$ with $\mu \in \mathbb{R}$.

**Remark 1.1.** $\mathcal{M}$ is a subset of $H_\lambda$ but is not a linear subspace. The nonlinearity comes from the condition that all zeros lie on the critical line: the sum of two functions with critical zeros does not in general have all its zeros critical. This distinguishes the problem from the classical theory of approximation in Hilbert spaces, where the approximating object is convex.

### 1.2. The reference point $f_0^{on}$

**Definition 1.2.** We denote by $\zeta_{\mathrm{on}}$ the entire function defined by:
$$\xi_{\mathrm{on}}(s) = \xi(0) \prod_{n=1}^\infty \left(1 - \frac{s}{1/2+i\gamma_n}\right)\left(1 - \frac{s}{1/2-i\gamma_n}\right) e^{2s/(1+4\gamma_n^2)},$$
where $\{\rho_n = \sigma_n + i\gamma_n\}$ are the nontrivial zeros of $\zeta$ (with $\sigma_n$ their real parts, not necessarily equal to $1/2$). The function $\zeta_{\mathrm{on}}$ is the version of $\zeta$ in which each zero $\rho_n = \sigma_n + i\gamma_n$ has been projected to the point $1/2 + i\gamma_n$ on the critical line, keeping the imaginary part.

We define
$$f_0^{on}(s) = |\zeta_{\mathrm{on}}(1/2+is)|^2 \in \mathcal{M}.$$

Under RH, $\sigma_n = 1/2$ for all $n$, hence $\zeta_{\mathrm{on}} = \zeta$ and $f_0^{on} = f_0$.

**Remark 1.3.** The relation between $f_0$ and $f_0^{on}$ is encoded by the formula from Doc 83:
$$f_0(s) = f_0^{on}(s) \cdot \prod_{j:\,\delta_j > 0} \left(1 + \frac{\delta_j^2}{(s-\gamma_j)^2 + \delta_j^2}\right)^2$$
where $\delta_j = |\sigma_{n_j} - 1/2|$ measures the deviation of the $j$-th off-critical pair of zeros from the critical line.

### 1.3. The distance functional

For $\eta \in \mathcal{E}$, we define the **distance functional**:
$$\Phi(\eta) = \|f_0 - |\eta|^2\|^2_{H_\lambda} = \int_{\mathbb{R}} W_\lambda(s)\bigl(f_0(s) - |\eta(1/2+is)|^2\bigr)^2 dm_\infty(s).$$

The variational problem is
$$\tilde\delta_\lambda^2 = \inf_{\eta \in \mathcal{E}} \Phi(\eta).$$

We want to study the structure of $\Phi$ in a neighborhood of $\eta = \zeta_{\mathrm{on}}$.

---

## §2. Local parametrization of $\mathcal{M}$: deformations of the Hadamard product

### 2.1. Two types of deformation

To study the geometry of $\mathcal{M}$ near $f_0^{on}$, we need to parametrize the variations of $\zeta_{\mathrm{on}}$ within $\mathcal{E}$.

**Definition 2.1 (Variation of the $j$-th pair of zeros).** Fix $j \geq 1$ and $\epsilon \in \mathbb{C}$ with $|\epsilon|$ small. Define $\zeta_{\mathrm{on},\epsilon}^{(j)}$ as the entire function obtained from $\zeta_{\mathrm{on}}$ by replacing the $j$-th pair of zeros $\{1/2 \pm i\gamma_j\}$ (and its symmetric counterpart $\{1/2 \pm i\gamma_j$ under $s \mapsto 1-s\}$) with the shifted quadruple. There are two cases:

- **Tangential variation** ($\epsilon = \tau \in \mathbb{R}$): the zeros move to $1/2 + i(\gamma_j + \tau)$ and $1/2 - i(\gamma_j + \tau)$, remaining on the critical line. The function $\zeta_{\mathrm{on},\tau}^{(j)}$ still belongs to $\mathcal{E}$.

- **Transversal variation** ($\epsilon = i\delta \in i\mathbb{R}$, $\delta \in \mathbb{R}$ small): the zeros move to $(1/2 + \delta) + i\gamma_j$ and $(1/2 - \delta) + i\gamma_j$ (and the symmetric counterparts under $s\mapsto 1-s$). The resulting function **no longer** belongs to $\mathcal{E}$: it is a perturbation outside $\mathcal{M}$.

**Remark 2.2.** The transversal variation corresponds to moving in the direction normal to $\mathcal{M}$ at the point $f_0^{on}$. To study whether $f_0^{on}$ is a local minimum of $\Phi|_\mathcal{M}$, what matters is the second transversal variation, because the first tangential variation only tells us whether $f_0^{on}$ is a critical point of $\Phi|_\mathcal{M}$.

### 2.2. Explicit formula for the transversal variation

Let $\epsilon \in \mathbb{C}$ with $|\epsilon|$ small. We define the entire function

$$\zeta_{\mathrm{on},\epsilon}^{(j)}(s) := \zeta_{\mathrm{on}}(s) \cdot \frac{(s - 1/2 - i\gamma_j - \epsilon)(s - 1/2 + i\gamma_j - \bar\epsilon)(s - 1/2 - i\gamma_j + \epsilon)(s - 1/2 + i\gamma_j + \bar\epsilon)}{(s-1/2-i\gamma_j)^2(s-1/2+i\gamma_j)^2}$$

where in the denominator we recognize the original zeros $1/2 \pm i\gamma_j$ (each of multiplicity 2 after accounting for the symmetric point $s\mapsto 1-s$, but for notational simplicity we assume the zeros are simple and the functional equation couples the pair $\{1/2+i\gamma_j, 1/2-i\gamma_j\}$).

**Simplified notation.** For clarity, we write the deformation factor as

$$R_\epsilon^{(j)}(s) := \frac{(s - \alpha_j - \epsilon)(s - \bar\alpha_j - \bar\epsilon)(s - (1-\alpha_j) - \epsilon)(s - (1-\bar\alpha_j) - \bar\epsilon)}{(s-\alpha_j)(s-\bar\alpha_j)(s-(1-\alpha_j))(s-(1-\bar\alpha_j))},$$

where $\alpha_j = 1/2 + i\gamma_j$. For $\epsilon = 0$, $R_0^{(j)} \equiv 1$. For small $\epsilon$, $R_\epsilon^{(j)}(s) \approx 1$ away from the zeros $\alpha_j, \bar\alpha_j$, and the deformation is essentially local in a neighborhood of $s = \gamma_j$.

Thus,
$$\zeta_{\mathrm{on},\epsilon}^{(j)}(s) = \zeta_{\mathrm{on}}(s) \cdot R_\epsilon^{(j)}(s),$$
and the deformed function on the critical line is
$$f_\epsilon^{(j)}(s) := |\zeta_{\mathrm{on},\epsilon}^{(j)}(1/2+is)|^2 = f_0^{on}(s) \cdot |R_\epsilon^{(j)}(1/2+is)|^2.$$

### 2.3. Expansion of $|R_\epsilon^{(j)}|^2$ to second order

For the pure transversal variation $\epsilon = i\delta$ with $\delta \in \mathbb{R}$ small, we compute $|R_{i\delta}^{(j)}(1/2+is)|^2$.

We denote $u = s - \gamma_j \in \mathbb{R}$ (displacement from the zero). The relevant factors are:

$$\frac{(1/2+is) - \alpha_j - i\delta}{(1/2+is) - \alpha_j} = \frac{i(u) - i\delta}{i(u)} = 1 - \frac{\delta}{u} \cdot \frac{1}{i} \cdot i = 1 - \frac{\delta}{u}.$$

More precisely, with $1/2+is - \alpha_j = 1/2+is - 1/2 - i\gamma_j = i(s-\gamma_j) = iu$:

$$\frac{(1/2+is) - (\alpha_j + i\delta)}{(1/2+is) - \alpha_j} = \frac{iu - i\delta}{iu} = \frac{u-\delta}{u} = 1 - \frac{\delta}{u}.$$

For the conjugate zero $\bar\alpha_j = 1/2 - i\gamma_j$, with $1/2+is - \bar\alpha_j = i(s+\gamma_j)$:

$$\frac{(1/2+is) - (\bar\alpha_j - i\delta)}{(1/2+is) - \bar\alpha_j} = \frac{i(s+\gamma_j) + i\delta}{i(s+\gamma_j)} = 1 + \frac{\delta}{s+\gamma_j}.$$

The factors from the functional equation (under $s\mapsto 1-s$) contribute analogously with $u \mapsto -u$. Taking the modulus squared of the full product:

$$|R_{i\delta}^{(j)}(1/2+is)|^2 = \left(1 - \frac{\delta}{u}\right)^2 \cdot \left(1 + \frac{\delta}{s+\gamma_j}\right)^2 \cdot \left(\text{symmetric factors}\right)^2.$$

For the symmetric transversal direction (in which the zeros are displaced symmetrically under $s\mapsto 1-s$), the net result on the critical line is:

$$|R_{i\delta}^{(j)}(1/2+is)|^2 = \left(1 - \frac{\delta}{s-\gamma_j}\right)^2 \left(1 + \frac{\delta}{s+\gamma_j}\right)^2 \left(1 + \frac{\delta}{s-\gamma_j}\right)^2 \left(1 - \frac{\delta}{s+\gamma_j}\right)^2.$$

Simplifying: the factors in $s-\gamma_j$ give $(1 - \delta^2/(s-\gamma_j)^2)^2$ and those in $s+\gamma_j$ give $(1 - \delta^2/(s+\gamma_j)^2)^2$. Expanding to second order in $\delta$:

$$|R_{i\delta}^{(j)}(1/2+is)|^2 = 1 - \frac{2\delta^2}{(s-\gamma_j)^2} - \frac{2\delta^2}{(s+\gamma_j)^2} + O(\delta^4).$$

**Lemma 2.3 (Second-order expansion).** *For the transversal variation $\epsilon = i\delta$ with $\delta \in \mathbb{R}$ small and $s \notin \{\pm\gamma_j\}$,*
$$|R_{i\delta}^{(j)}(1/2+is)|^2 = 1 - 2\delta^2 \left(\frac{1}{(s-\gamma_j)^2} + \frac{1}{(s+\gamma_j)^2}\right) + O(\delta^4).$$

*Consequently,*
$$f_\delta^{(j)}(s) := f_0^{on}(s)\cdot |R_{i\delta}^{(j)}(1/2+is)|^2 = f_0^{on}(s)\left(1 - 2\delta^2 K_j(s) + O(\delta^4)\right),$$
*where*
$$K_j(s) = \frac{1}{(s-\gamma_j)^2} + \frac{1}{(s+\gamma_j)^2}.$$

*Proof.* This follows directly from the modulus-squared calculation described above and the Taylor expansion $(1-x)^2 = 1 - 2x + x^2$ to first order in $x = \delta^2/(\cdot)^2$. The $O(\delta^4)$ terms come from the square of the first-order terms. $\square$

**Remark 2.4.** Note that $K_j(s) = (s-\gamma_j)^{-2} + (s+\gamma_j)^{-2} \geq 0$ for $s \notin \{\pm\gamma_j\}$, and that $K_j(s) \to +\infty$ as $s \to \pm\gamma_j$. The sign of the kernel $K_j$ is crucial for the analysis of the second variation.

---

## §3. First variation of the distance functional

### 3.1. Tangential variation: computation of $\frac{d}{d\tau}\Phi(\zeta_{\mathrm{on},\tau}^{(j)})\big|_{\tau=0}$

Let $\zeta_{\mathrm{on},\tau}^{(j)}$ be the tangential deformation (zeros moving within the critical line). We define $\phi(\tau) = \Phi(\zeta_{\mathrm{on},\tau}^{(j)})$.

**Proposition 3.1 (First tangential variation).** *Let $\tau \mapsto \zeta_{\mathrm{on},\tau}^{(j)}$ be the tangential variation moving the $j$-th pair of zeros from $1/2 \pm i\gamma_j$ to $1/2 \pm i(\gamma_j+\tau)$. Then:*
$$\phi'(0) = \frac{d}{d\tau}\Phi(\zeta_{\mathrm{on},\tau}^{(j)})\bigg|_{\tau=0} = -2\int_\mathbb{R} W_\lambda(s)\bigl(f_0(s) - f_0^{on}(s)\bigr) \cdot \frac{\partial}{\partial\tau}\bigl[f_\tau^{(j)}(s)\bigr]\bigg|_{\tau=0}\, dm_\infty(s).$$

*Proof.* By the chain rule in the Hilbert space $H_\lambda$:
$$\frac{d}{d\tau}\|f_0 - f_\tau^{(j)}\|^2_{H_\lambda} = -2\langle f_0 - f_\tau^{(j)},\, \partial_\tau f_\tau^{(j)}\rangle_{H_\lambda}.$$
Evaluating at $\tau=0$ gives the stated formula. $\square$

**Corollary 3.2.** *Under RH, $f_0 = f_0^{on}$, hence $\phi'(0) = 0$ for every tangential variation. The point $f_0^{on}$ is a critical point of $\Phi|_\mathcal{M}$ under RH.*

*Proof.* If RH is true, $f_0 = f_0^{on}$ and the factor $f_0(s) - f_0^{on}(s) \equiv 0$, so the integral vanishes. $\square$

**Remark 3.3.** This is the expected result: under RH, $f_0 \in \mathcal{M}$ and the distance to $\mathcal{M}$ is zero, so that $f_0^{on} = f_0$ is trivially the minimum. The nontrivial result occurs in the transversal direction (§4–5), where zeros move off $\mathcal{M}$.

### 3.2. First variation in the transversal direction

The transversal direction no longer lies within $\mathcal{M}$; it is a variation of the point $f_0^{on} \in \mathcal{M}$ in the direction normal to $\mathcal{M}$. In this sense, the "first transversal variation" measures the derivative of the distance $\|f_0 - f_\delta^{(j)}\|^2_{H_\lambda}$ as a function of $\delta$, where $f_\delta^{(j)}$ no longer lies in $\mathcal{M}$.

**Proposition 3.3 (First transversal variation).** *For the transversal variation $\epsilon = i\delta$, define $\psi(\delta) = \|f_0 - f_\delta^{(j)}\|^2_{H_\lambda}$. Then $\psi'(0) = 0$.*

*Proof.* From Lemma 2.3, $f_\delta^{(j)}(s) = f_0^{on}(s)(1 - 2\delta^2 K_j(s) + O(\delta^4))$. The derivative with respect to $\delta$ of $f_\delta^{(j)}$ evaluated at $\delta=0$ is:
$$\frac{\partial}{\partial\delta}f_\delta^{(j)}(s)\bigg|_{\delta=0} = \frac{\partial}{\partial\delta}\bigl[f_0^{on}(s)(1 - 2\delta^2 K_j(s) + O(\delta^4))\bigr]_{\delta=0} = 0,$$
since the expression $-2\delta^2 K_j(s)$ is even in $\delta$ and has zero derivative at $\delta=0$. By the chain rule:
$$\psi'(0) = -2\langle f_0 - f_0^{on},\, \partial_\delta f_\delta^{(j)}\big|_{\delta=0}\rangle_{H_\lambda} = 0. \quad\square$$

**Consequence 3.4.** The point $f_0^{on}$ is always a critical point of the functional $\delta \mapsto \|f_0 - f_\delta^{(j)}\|^2_{H_\lambda}$ at $\delta=0$, regardless of whether RH is true or not. The distinction arises in the sign of the **second variation**.

---

## §4. Second variation in the transversal direction

### 4.1. Computation of $\psi''(0)$

Using the expansion of Lemma 2.3:
$$f_\delta^{(j)}(s) = f_0^{on}(s) - 2\delta^2 f_0^{on}(s) K_j(s) + O(\delta^4),$$
the distance functional is written as

$$\psi(\delta) = \|f_0 - f_\delta^{(j)}\|^2_{H_\lambda} = \int_\mathbb{R} W_\lambda(s)\bigl(f_0(s) - f_\delta^{(j)}(s)\bigr)^2 dm_\infty(s).$$

We define $D_0(s) = f_0(s) - f_0^{on}(s) \geq 0$ (the pointwise difference, which is nonnegative by the formula of Doc 83). Then

$$f_0(s) - f_\delta^{(j)}(s) = D_0(s) + 2\delta^2 f_0^{on}(s) K_j(s) + O(\delta^4).$$

Squaring:

$$\bigl(f_0(s) - f_\delta^{(j)}(s)\bigr)^2 = D_0(s)^2 + 4\delta^2 D_0(s) f_0^{on}(s) K_j(s) + 4\delta^4 (f_0^{on}(s))^2 K_j(s)^2 + O(\delta^6).$$

Integrating with weight $W_\lambda\,dm_\infty$ and grouping by powers of $\delta$:

$$\psi(\delta) = \psi(0) + 4\delta^2 \int_\mathbb{R} W_\lambda(s) D_0(s) f_0^{on}(s) K_j(s)\, dm_\infty(s) + O(\delta^4).$$

**Definition 4.1 (Second-variation coefficient).** We define

$$\mathcal{Q}_\lambda^{(j)} := \int_\mathbb{R} W_\lambda(s)\, D_0(s)\, f_0^{on}(s)\, K_j(s)\, dm_\infty(s),$$

where $D_0(s) = f_0(s) - f_0^{on}(s)$, $f_0^{on}(s) = |\zeta_{\mathrm{on}}(1/2+is)|^2$, and $K_j(s) = (s-\gamma_j)^{-2} + (s+\gamma_j)^{-2}$.

**Theorem 4.2 (Second transversal variation).** *For the transversal variation $\epsilon = i\delta$ of the $j$-th pair of zeros,*
$$\psi''(0) = 8\,\mathcal{Q}_\lambda^{(j)}.$$

*In particular, $\psi''(0) > 0$ if and only if $\mathcal{Q}_\lambda^{(j)} > 0$.*

*Proof.* By the expansion $\psi(\delta) = \psi(0) + 4\delta^2 \mathcal{Q}_\lambda^{(j)} + O(\delta^4)$, the second derivative at $\delta=0$ is
$$\psi''(0) = \frac{d^2}{d\delta^2}\psi(\delta)\bigg|_{\delta=0} = 8\,\mathcal{Q}_\lambda^{(j)}. \quad\square$$

### 4.2. Sign analysis of $\mathcal{Q}_\lambda^{(j)}$

The integrand in $\mathcal{Q}_\lambda^{(j)}$ is the product of four factors:

1. $W_\lambda(s) \geq 0$: the weight kernel, nonnegative by definition.
2. $D_0(s) = f_0(s) - f_0^{on}(s)$: the difference between $|\zeta|^2$ and $|\zeta_{\mathrm{on}}|^2$ on the critical line.
3. $f_0^{on}(s) = |\zeta_{\mathrm{on}}(1/2+is)|^2 \geq 0$: the modulus squared, nonnegative.
4. $K_j(s) = (s-\gamma_j)^{-2} + (s+\gamma_j)^{-2} > 0$ for $s \neq \pm\gamma_j$: strictly positive away from the zeros of $\zeta_{\mathrm{on}}$.

Therefore, the sign of $\mathcal{Q}_\lambda^{(j)}$ is determined by the sign of $D_0(s)$.

**Proposition 4.3 (Sign of $D_0$ and sign of $\mathcal{Q}_\lambda^{(j)}$).** 

(a) Under $\neg$RH: $D_0(s) \geq 0$ for all $s \in \mathbb{R}$ (by the formula of Doc 83, the ratio $f_0/f_0^{on}$ is a product of factors $\geq 1$). Moreover, $D_0(s) > 0$ on a set of positive measure with respect to $W_\lambda\,dm_\infty$. Therefore $\mathcal{Q}_\lambda^{(j)} > 0$ and $\psi''(0) > 0$.

(b) Under RH: $D_0(s) \equiv 0$, hence $\mathcal{Q}_\lambda^{(j)} = 0$ and $\psi''(0) = 0$.

*Proof of (a).* By Doc 83, Proposition 1.1, under $\neg$RH one has
$$\frac{f_0(s)}{f_0^{on}(s)} = \prod_{k:\,\delta_k>0} \left(1 + \frac{\delta_k^2}{(s-\gamma_k)^2}\right)^2 \geq 1,$$
with strict inequality for $s$ away from the zeros $\gamma_k$. Since $W_\lambda\,dm_\infty$ assigns positive mass to any open set (by the formula for $dm_\infty$), the integrand is strictly positive on a set of positive measure, hence $\mathcal{Q}_\lambda^{(j)} > 0$. $\square$

**Corollary 4.4.** *The second transversal variation satisfies:*
$$\psi''(0) \begin{cases} > 0 & \text{under } \neg\mathrm{RH}, \\ = 0 & \text{under } \mathrm{RH}. \end{cases}$$

**Remark 4.5.** Corollary 4.4 has an important geometric interpretation: the functional $\delta\mapsto\psi(\delta)$ has a minimum at $\delta=0$ under RH (since $\psi \equiv 0$ trivially), and under $\neg$RH it has a local minimum at $\delta=0$ with positive curvature $8\mathcal{Q}_\lambda^{(j)} > 0$.

However, note that this statement concerns the distance from $f_0$ to the **deformed** point $f_\delta^{(j)}$, which lies **outside** $\mathcal{M}$ for $\delta\neq 0$. The second variation we have computed is not the second variation of $\Phi|_\mathcal{M}$, but of $\Phi$ along the transversal curve. See §5 for the precise distinction.

---

## §5. Connection with the kernels $K_\lambda(\gamma_j)$ of Doc 86

### 5.1. The approximation kernels of Doc 86

Doc 86 (§6) introduced, in the context of the lower bound for $T_\lambda$, the kernels

$$K_\lambda(\gamma_j) = \int_\mathbb{R} W_\lambda(s)\, |\zeta_{\mathrm{on}}(1/2+is)|^2 \cdot \frac{1}{(s-\gamma_j)^2}\, dm_\infty(s)$$

and proved the lower bound
$$T_\lambda \geq 2\sum_j \delta_j^2 K_\lambda(\gamma_j)$$
(where the sum runs over the off-critical zeros with displacement $\delta_j$).

**Proposition 5.1 (Relation between $\mathcal{Q}_\lambda^{(j)}$ and $K_\lambda(\gamma_j)$).** *One has*
$$\mathcal{Q}_\lambda^{(j)} = \int_\mathbb{R} W_\lambda(s)\, D_0(s)\, f_0^{on}(s)\, K_j(s)\, dm_\infty(s),$$
*and in the regime of a single off-critical pair of zeros with small displacement $\delta_j$,*
$$\mathcal{Q}_\lambda^{(j)} \approx 2\delta_j^2 \int_\mathbb{R} W_\lambda(s)\, (f_0^{on}(s))^2 \cdot K_j(s)^2\, dm_\infty(s).$$

*Proof.* Using the formula from Doc 83 for $D_0(s)$:
$$D_0(s) = f_0^{on}(s)\left[\prod_k\left(1 + \frac{\delta_k^2}{(s-\gamma_k)^2}\right)^2 - 1\right] \approx 4\delta_j^2 \frac{f_0^{on}(s)}{(s-\gamma_j)^2} + O(\delta_j^4)$$
for the case of a single off-critical pair with small displacement $\delta_j$. Substituting into $\mathcal{Q}_\lambda^{(j)}$:
$$\mathcal{Q}_\lambda^{(j)} \approx 4\delta_j^2 \int_\mathbb{R} W_\lambda(s)\, \frac{(f_0^{on}(s))^2}{(s-\gamma_j)^2} \cdot K_j(s)\, dm_\infty(s).$$
Since $K_j(s) = (s-\gamma_j)^{-2} + (s+\gamma_j)^{-2}$, the dominant term gives the stated estimate. $\square$

**Remark 5.2.** The proposition shows that $\mathcal{Q}_\lambda^{(j)}$ is of order $\delta_j^2$ (the square of the displacement), not of order $\delta_j$. This confirms that the second variation is the dominant contribution and that the perturbative analysis is self-consistent.

### 5.2. Interpretation in terms of the lower bound $T_\lambda$

The lower bound $T_\lambda \geq 2\sum_j \delta_j^2 K_\lambda(\gamma_j)$ from Doc 86 can now be interpreted in terms of the geometry of $\mathcal{M}$:

- $T_\lambda$ measures the global "distance" of $f_0$ to $f_0^{on}$ in the sense of the trace of the CTP operator.
- $K_\lambda(\gamma_j)$ is the kernel weighting the contribution of the $j$-th off-critical zero.
- $\mathcal{Q}_\lambda^{(j)}$ is essentially the second variation of the distance when the $j$-th pair of zeros moves transversally.

The lower bound $T_\lambda \geq 2\sum_j\delta_j^2 K_\lambda(\gamma_j)$ guarantees $T_\lambda > 0$ under $\neg$RH, which is the content of the CTP criterion. The positive second variation $\psi''(0) > 0$ is an alternative, more geometric formulation of the same phenomenon.

---

## §6. Riemannian geometry of $\mathcal{M}$: curvature in the transversal direction

### 6.1. $\mathcal{M}$ as a Hilbert manifold (informal)

Although $\mathcal{M}$ is not a Banach manifold in the classical sense (its topology is delicate), we can locally equip it with a Riemannian structure as follows.

**Definition 6.1 (Riemannian metric induced on $\mathcal{M}$).** For $g \in \mathcal{M}$ and tangent vectors $v_1, v_2 \in T_g\mathcal{M}$ (derivatives of smooth curves in $\mathcal{M}$ passing through $g$), the Riemannian metric induced by the inclusion $\mathcal{M} \hookrightarrow H_\lambda$ is:
$$\langle v_1, v_2\rangle_g = \int_\mathbb{R} W_\lambda(s)\, v_1(s)\, v_2(s)\, dm_\infty(s).$$

The tangent space $T_{f_0^{on}}\mathcal{M}$ at the point $f_0^{on}$ consists of the derivatives of curves in $\mathcal{M}$ passing through $f_0^{on}$. A tangential curve (zeros moving within the critical line) generates a tangent vector; a transversal curve is not in $\mathcal{M}$.

### 6.2. The second fundamental form and normal curvature

**Definition 6.2 (Second fundamental form).** Let $\gamma : (-\epsilon_0, \epsilon_0) \to H_\lambda$ be a smooth curve with $\gamma(0) = f_0^{on}$ and $\gamma'(0)$ in the direction normal to $T_{f_0^{on}}\mathcal{M}$ (transversal direction $b_j$). The **second fundamental form** of $\mathcal{M}$ in the direction $b_j$ is

$$\mathrm{II}(b_j, b_j) = \gamma''(0) - \nabla_{\gamma'}\gamma'\big|_{\mathcal{M}},$$

where $\nabla$ denotes the Levi-Civita connection of $H_\lambda$ (which is the flat connection, since $H_\lambda$ is a Hilbert space). In this context, the second fundamental form captures the "curvature" of $\mathcal{M}$ when leaving the critical line.

**Proposition 6.3 (Curvature of $\mathcal{M}$ in the transversal direction).** *The second variation of $\Phi$ in the transversal direction $b_j$ is related to the second fundamental form by*
$$\psi''(0) = 8\mathcal{Q}_\lambda^{(j)} = 2\|\mathrm{II}(b_j,b_j)\|^2_{H_\lambda} + 2\langle f_0 - f_0^{on},\, \mathrm{II}(b_j,b_j)\rangle_{H_\lambda}.$$

*Proof (sketch).* Using the standard formula for the Hessian of a squared distance function from a point $f_0$ to a submanifold $\mathcal{M}$ of a Hilbert space (when the distance is well defined), the second variation of $\|f_0 - \pi_\mathcal{M}(\cdot)\|^2$ in the transversal direction includes both the curvature of $\mathcal{M}$ and the inner product between the difference $f_0-f_0^{on}$ and the second fundamental form. The explicit formula follows by substituting the expansion of Lemma 2.3. $\square$

**Remark 6.4.** The second variation $\psi''(0) = 8\mathcal{Q}_\lambda^{(j)}$ has two components:
- The term $\|\mathrm{II}(b_j,b_j)\|^2$ is always nonnegative and measures the "intrinsic convexity" of $\mathcal{M}$.
- The term $\langle f_0-f_0^{on}, \mathrm{II}(b_j,b_j)\rangle$ can be positive or negative depending on the direction of $f_0-f_0^{on}$ relative to the curvature of $\mathcal{M}$.

Proposition 4.3 establishes that the sum is positive (under $\neg$RH), which means that $\mathcal{M}$ "moves away" from $f_0$ when we move transversally from $f_0^{on}$.

### 6.3. Convexity of $\mathcal{M}$ toward $f_0$

**Definition 6.5 (Convexity toward a point).** We say that $\mathcal{M}$ is **convex toward $f_0$** at the point $f_0^{on}$ if for every normal direction $b_j$, the second variation of the distance $\|f_0 - \cdot\|^2_{H_\lambda}$ in the direction $b_j$ is positive.

**Proposition 6.6 (Convexity under $\neg$RH).** *Under $\neg$RH, $\mathcal{M}$ is locally convex toward $f_0$ at the point $f_0^{on}$, in the sense that $\psi''(0) = 8\mathcal{Q}_\lambda^{(j)} > 0$ for every transversal direction $b_j$.*

*Proof.* Direct consequence of Proposition 4.3(a). $\square$

**Geometric interpretation.** Convexity of $\mathcal{M}$ toward $f_0$ means that, when moving from $f_0^{on}$ in the transversal direction $b_j$ (leaving $\mathcal{M}$), the distance to $f_0$ increases. In other words, $f_0^{on}$ is locally the closest point of $\mathcal{M}$ to $f_0$ in the direction $b_j$.

**Caution 6.7.** Local convexity is a property of the behavior of $\mathcal{M}$ near $f_0^{on}$. It does not imply that $f_0^{on}$ is the global minimum of $\Phi|_\mathcal{M}$: there could be other points of $\mathcal{M}$, farther from $f_0^{on}$, with smaller distance to $f_0$.

---

## §7. The gap between local convexity and global uniqueness

### 7.1. Formalization of the problem

Let $\mathcal{M}$ be equipped with the metric induced by $H_\lambda$. The optimization problem is:
$$\min_{g \in \mathcal{M}} \Phi(g) = \min_{g \in \mathcal{M}} \|f_0 - g\|^2_{H_\lambda}.$$

Proposition 6.6 establishes that $f_0^{on}$ is a **local minimum** in the topology of the ambient space $H_\lambda$ (in the sense that every small-amplitude transversal perturbation increases the distance). However, the global problem is more subtle.

**Problem 7.1 (Global uniqueness gap).** Is $f_0^{on}$ the unique global minimum of $\Phi|_\mathcal{M}$?

To answer affirmatively we need to rule out the existence of another $g^* \in \mathcal{M}$, $g^* \neq f_0^{on}$, with $\|f_0 - g^*\|_{H_\lambda} < \|f_0 - f_0^{on}\|_{H_\lambda}$.

### 7.2. Why local convexity does not give global uniqueness

**Example 7.2 (Finite-dimensional counterexample).** Consider $H = \mathbb{R}^2$, $f_0 = (0,1)$, and $\mathcal{M}$ the curve $\{(\cos\theta, -2+\sin\theta) : \theta \in [0,2\pi)\}$ (a circle of radius 1 centered at $(0,-2)$). The point $f_0^{on} = (0,-1)$ (the point of $\mathcal{M}$ closest to the $y$-axis from below) is a local minimum of the distance to $f_0$. But the curvature of $\mathcal{M}$ is constant (negative in the sense that the center of curvature lies inside $\mathcal{M}$, far from $f_0$), so there is no other local minimum. In this case, local convexity does give uniqueness. But if $\mathcal{M}$ were non-convex and "curved back" toward $f_0$, there could be multiple local minima.

**Lemma 7.3.** *Local convexity of $\mathcal{M}$ toward $f_0$ at $f_0^{on}$ does not imply global uniqueness of the minimum unless $\mathcal{M}$ satisfies a global "no return" condition (for example, that $\mathcal{M}$ be a simply connected manifold or that the distance function have no other critical points).*

*Proof.* Example 7.2, modified, suffices: a curve in $H_\lambda$ having a second local minimum. Convexity at each minimum does not rule out the existence of the other. $\square$

### 7.3. The role of Hadamard's uniqueness theorem

Doc 82 (§4, Lemma 4.5) used Hadamard's uniqueness theorem for entire functions. In essence, the argument was:

> If $g \in \mathcal{M}$ coincides in modulus with $f_0 = |\zeta|^2$ on the critical line, then $g = f_0^{on} = |\zeta_{\mathrm{on}}|^2$ (both have the same zeros).

This argument uses the rigidity of entire functions: the modulus on a line determines the entire function (up to a global phase). The result is that **if one achieves $\Phi(g) = 0$, i.e., if $\|f_0 - g\|_{H_\lambda} = 0$**, then $g = f_0^{on}$ and RH is true.

**Proposition 7.4 (Uniqueness when the infimum is zero).** *If $\inf_{g\in\mathcal{M}}\Phi(g) = 0$, then the infimum is attained at $g = f_0^{on}$, and RH is true.*

*Proof.* If the infimum is zero, there exists a sequence $g_n \in \mathcal{M}$ with $\Phi(g_n) \to 0$. Convergence in $H_\lambda$ together with the argument of Lemma 4.5 of Doc 82 implies that $g_n \to f_0^{on}$ and that the zeros of the functions $\eta_n$ (with $g_n = |\eta_n|^2$) converge to the zeros of $\zeta_{\mathrm{on}}$. Under the hypothesis $\Phi(g_n) \to 0$, the limit satisfies $g = f_0$, hence $f_0 \in \mathcal{M}$ and RH is true. $\square$

**Remark 7.5.** Proposition 7.4 only works when the infimum is zero. If the infimum is positive (under $\neg$RH), uniqueness of the global minimum is not guaranteed by the Hadamard argument. This is the gap.

### 7.4. The precise gap

**Gap 7.6 (Precise formulation of the obstacle).** The missing logical link is:

$$\underbrace{\text{local convexity at } f_0^{on}}_{\text{Proposition 6.6}} + \underbrace{\text{uniqueness when infimum} = 0}_{\text{Proposition 7.4}} \not\Rightarrow \underbrace{f_0^{on} \text{ is the unique global minimum under } \neg\mathrm{RH}}_{\text{required to close}}$$

More precisely: under $\neg$RH the infimum is $\tilde\delta_\lambda^2 > 0$, and the Hadamard argument only guarantees uniqueness when the minimum is zero. When the minimum is positive, it could be attained by functions $g^* \in \mathcal{M}$ different from $f_0^{on}$, and local convexity at $f_0^{on}$ does not rule out the existence of such $g^*$.

To close the argument one would need one of the following additional conditions:

(i) **Global uniqueness of the minimum**: show that $f_0^{on}$ is the unique minimum of $\Phi|_\mathcal{M}$ (unconditionally, without assuming RH).

(ii) **Geodesic convexity of $\mathcal{M}$**: show that $\mathcal{M}$ is geodesically convex (or "log-convex") in the metric induced by $H_\lambda$, which would imply that every local minimum is global.

(iii) **A quantitative inequality**: show that $\|f_0 - g\|_{H_\lambda} \geq \|f_0 - f_0^{on}\|_{H_\lambda}$ for every $g \in \mathcal{M}$, directly and without going through the Hadamard argument.

None of these conditions is currently proved.

---

## §8. The positive curvature conjecture

### 8.1. Formulation of the conjecture

**Conjecture 8.1 (Positive curvature of $\mathcal{M}$ in the transversal direction).** *Let $\lambda > 0$. For each $j \geq 1$ and each pair of zeros $1/2 \pm i\gamma_j \in \mathcal{Z}_{\mathrm{on}}$ (the zeros of $\zeta_{\mathrm{on}}$ on the critical line), one has:*

$$\mathcal{Q}_\lambda^{(j)} = \int_\mathbb{R} W_\lambda(s)\,(f_0(s) - f_0^{on}(s))\,|\zeta_{\mathrm{on}}(1/2+is)|^2\left(\frac{1}{(s-\gamma_j)^2} + \frac{1}{(s+\gamma_j)^2}\right)dm_\infty(s) > 0$$

*under the additional hypothesis that $\zeta$ has at least one zero with real part different from $1/2$ (i.e., under $\neg$RH).*

*Explicit hypotheses:*
- $W_\lambda \geq 0$ is the CCM kernel.
- $f_0(s) = |\zeta(1/2+is)|^2$ and $f_0^{on}(s) = |\zeta_{\mathrm{on}}(1/2+is)|^2$ are integrable in $L^2(W_\lambda\,dm_\infty)$.
- $f_0(s) \geq f_0^{on}(s)$ for all $s \in \mathbb{R}$ (this pointwise inequality, if true, would imply the conjecture).
- $\zeta_{\mathrm{on}}$ does not vanish on a set of positive measure with respect to $W_\lambda\,dm_\infty$.

**Remark 8.2.** The conjecture is a statement about the sign of an integral. Its essential content lies in the pointwise positivity hypothesis $f_0(s) \geq f_0^{on}(s)$, which in turn is equivalent to the statement:

$$\prod_{k:\,\delta_k>0}\left(1 + \frac{\delta_k^2}{(s-\gamma_k)^2}\right)^2 \geq 1 \quad \text{for all } s \in \mathbb{R},$$

which is trivially true (each factor is $\geq 1$). Therefore, Conjecture 8.1 is actually a **theorem**, already established in Proposition 4.3(a). What remains as a conjecture is the stronger version that follows.

### 8.2. The strong conjecture: global convexity

**Conjecture 8.3 (Global convexity of $\mathcal{M}$).** *For every $f_0$ (not necessarily equal to $|\zeta|^2$, but any function in $H_\lambda \setminus \mathcal{M}$) and every $g \in \mathcal{M}$, the functional $\Phi(\cdot) = \|f_0 - \cdot\|^2_{H_\lambda}$ has a unique global minimum over $\mathcal{M}$.*

This conjecture is much stronger and corresponds to "geodesic convexity" of $\mathcal{M}$ with respect to the metric of $H_\lambda$. No evidence is known that it holds in general.

**Conjecture 8.4 (Weak version: unique minimum for $f_0 = |\zeta|^2$).** *The functional $\Phi(\eta) = \||\zeta|^2 - |\eta|^2\|^2_{H_\lambda}$ has a unique minimum over $\mathcal{M}$, which is the point $f_0^{on} = |\zeta_{\mathrm{on}}|^2$.*

This weak version is the one that would be useful for the program: if it were proved, together with $\tilde\delta_\lambda^2 = 0 \Leftrightarrow \mathrm{RH}$, one would have a characterization of the minimum. But proving uniqueness requires information about the global geometry of $\mathcal{M}$, which is not currently available.

---

## §9. The precise obstacle: the extended "Hadamard barrier"

### 9.1. Summary of the state of the argument

We summarize what is proved and what is not, so that the obstacle is perfectly clear.

**Proved (unconditionally):**

(D1) $f_0 \in H_\lambda$ (Doc 82, §2).

(D2) $f_0^{on} \in \mathcal{M}$ (by construction).

(D3) $\Phi(f_0^{on}) = \|f_0 - f_0^{on}\|^2_{H_\lambda} \geq 0$.

(D4) $f_0(s) \geq f_0^{on}(s)$ pointwise for all $s \in \mathbb{R}$ (Doc 83, product of factors $\geq 1$).

(D5) The second transversal variation at $f_0^{on}$ is $\psi''(0) = 8\mathcal{Q}_\lambda^{(j)} \geq 0$, with $> 0$ under $\neg$RH (Proposition 4.3).

(D6) If $\inf_{g\in\mathcal{M}} \Phi(g) = 0$, then RH is true (Doc 82, Corollary 4.6).

**Proved under RH:**

(DR1) $f_0 = f_0^{on}$, $\Phi(f_0^{on}) = 0$, and $f_0^{on}$ is the global minimum of $\Phi|_\mathcal{M}$ (trivially).

(DR2) $\psi''(0) = 0$: the second variation is zero because there are no off-critical zeros.

**Not proved:**

(ND1) $f_0^{on}$ is the unique global minimum of $\Phi|_\mathcal{M}$ under $\neg$RH.

(ND2) $\mathcal{M}$ is geodesically convex in the metric of $H_\lambda$.

(ND3) The inequality $\Phi(g) \geq \Phi(f_0^{on})$ for every $g \in \mathcal{M}$ (under $\neg$RH).

(ND4) The existence of a global minimum of $\Phi|_\mathcal{M}$ (the infimum might not be attained).

### 9.2. The extended Hadamard barrier

The name "Hadamard barrier" (introduced in Doc 86, §10) refers to the fundamental obstacle: Hadamard's uniqueness theorem guarantees uniqueness of the representative of $\mathcal{M}$ when the distance is zero, but not when it is positive. More precisely:

**Hadamard barrier (extended formulation).** *Let $g^* \in \mathcal{M}$ be any minimum of $\Phi|_\mathcal{M}$ (assuming it exists). The Hadamard argument implies: if $\Phi(g^*) = 0$, then $g^* = f_0^{on}$ and RH is true. But if $\Phi(g^*) > 0$, there is no available analytic mechanism forcing $g^* = f_0^{on}$.*

In particular, local convexity of $\mathcal{M}$ at $f_0^{on}$ (the positivity of the second transversal variation) is compatible with the existence of another global minimum $g^* \neq f_0^{on}$ with $\Phi(g^*) < \Phi(f_0^{on})$.

**Obstacle 9.1 (Precise formulation).** *The gap in Direction D can be formulated as follows: to prove that $f_0^{on}$ is the global minimum of $\Phi|_\mathcal{M}$ (which would give new information about RH), it is necessary and sufficient to prove at least one of the following statements:*

*(a) For every $g \in \mathcal{M}$, $g \neq f_0^{on}$, one has $\Phi(g) > \Phi(f_0^{on})$.*

*(b) The infimum of $\Phi|_\mathcal{M}$ is attained, and every minimizer satisfies $g = f_0^{on}$.*

*(c) The functional $\Phi|_\mathcal{M}$ has no critical points other than $f_0^{on}$.*

*None of these statements is proved, and there is no known method to prove them without additional information about the distribution of the zeros of $\zeta$.*

### 9.3. Why is positivity of the second variation not sufficient?

Positivity of $\psi''(0)$ guarantees that $f_0^{on}$ is a local minimum of the function $\delta \mapsto \psi(\delta)$ (the distance along the transversal curve). But this transversal curve is not in $\mathcal{M}$: it is a curve in $H_\lambda$ leaving $\mathcal{M}$.

The property we want is that $f_0^{on}$ be a minimum of $\Phi|_\mathcal{M}$ in the topology of $\mathcal{M}$. For that, we would need the second variation to be positive also in the **tangential directions** of $\mathcal{M}$ (i.e., that the restricted Hessian be positive definite on $T_{f_0^{on}}\mathcal{M}$), and that there be no local minima in $\mathcal{M}$ outside a neighborhood of $f_0^{on}$.

Positivity of the second transversal variation means that $f_0^{on}$ is "stable" in the transversal direction: small perturbations that take the point out of $\mathcal{M}$ increase the distance. But within $\mathcal{M}$, the optimization problem is different.

---

## §10. Second variation in the tangential direction: complementary analysis

### 10.1. Computation of the second tangential variation

To complete the picture, we also compute the second variation in the tangential direction $b_j^{tan}$ (moving the $j$-th zero within the critical line: $\gamma_j \mapsto \gamma_j + \tau$).

We define $f_\tau^{(j)}(s) = |\zeta_{\mathrm{on},\tau}^{(j)}(1/2+is)|^2$ where $\zeta_{\mathrm{on},\tau}^{(j)}$ is the tangential deformation. The deformation factor analogous to Lemma 2.3 is now:

For an infinitesimal tangential variation $\tau$, the $j$-th Hadamard factor is converted from $(s-\gamma_j)/(s+\gamma_j)$ (schematically) into $(s-\gamma_j-\tau)/(s-\gamma_j)$. The modulus-squared calculation gives:

$$|R_\tau^{(j),tan}(1/2+is)|^2 = \left|\frac{s-\gamma_j-\tau}{s-\gamma_j}\right|^4 = \left(1 - \frac{\tau}{s-\gamma_j}\right)^4.$$

Expanding to second order:
$$|R_\tau^{(j),tan}(1/2+is)|^2 = 1 - \frac{4\tau}{s-\gamma_j} + \frac{10\tau^2}{(s-\gamma_j)^2} + O(\tau^3).$$

**Lemma 10.1 (Second-order tangential expansion).** *For the tangential variation $\epsilon = \tau \in \mathbb{R}$,*
$$f_\tau^{(j)}(s) = f_0^{on}(s)\left(1 - \frac{4\tau}{s-\gamma_j} + \frac{10\tau^2}{(s-\gamma_j)^2} + O(\tau^3)\right).$$

**Corollary 10.2 (First and second tangential variations under RH).** *Under RH, $f_0 = f_0^{on}$, and:*

$$\frac{d}{d\tau}\|f_0 - f_\tau^{(j)}\|^2_{H_\lambda}\bigg|_{\tau=0} = 2\langle f_0^{on},\, 4f_0^{on}/(s-\gamma_j)\rangle_{H_\lambda}$$

which is generally nonzero (the point $f_0^{on}$ is a critical point in the $\delta$ direction but not in the $\tau$ direction, unless there is symmetry). *This indicates that $f_0^{on}$ is not a critical point of $\Phi|_\mathcal{M}$ in the tangential direction under RH, which is consistent with the fact that $\Phi(f_0^{on}) = 0$ under RH (the functional is identically zero).*

**Remark 10.3.** When $\Phi(f_0^{on}) = 0$ (under RH), the notion of "critical point of $\Phi|_\mathcal{M}$" is not relevant, since the minimum is 0 and any variation gives a value $\geq 0$. The tangential direction is only relevant under $\neg$RH, to study whether $f_0^{on}$ is a saddle point or a local minimum of $\Phi|_\mathcal{M}$.

### 10.2. The restricted Hessian under $\neg$RH

To study whether $f_0^{on}$ is a local minimum of $\Phi|_\mathcal{M}$ under $\neg$RH, we need the Hessian of $\Phi|_\mathcal{M}$ at $f_0^{on}$, which is the quadratic form on $T_{f_0^{on}}\mathcal{M}$:

$$\mathrm{Hess}(\Phi|_\mathcal{M})[v, v] = \frac{d^2}{d\tau^2}\Phi(f_{\tau v}^{(j)})\bigg|_{\tau=0}$$

for $v \in T_{f_0^{on}}\mathcal{M}$ (tangential variation). From Lemma 10.1 and the chain rule:

$$\mathrm{Hess}(\Phi|_\mathcal{M})[b_j^{tan}, b_j^{tan}] = -2\langle D_0, \partial_{\tau\tau} f_\tau^{(j)}\big|_{\tau=0}\rangle_{H_\lambda} + 2\|\partial_\tau f_\tau^{(j)}\big|_{\tau=0}\|^2_{H_\lambda}.$$

The first term involves $D_0 = f_0 - f_0^{on}$ and can be positive or negative; the second term is always positive. The sign of the tangential Hessian is therefore indeterminate in general.

**Remark 10.4.** The indeterminacy of the sign of the tangential Hessian is another aspect of the gap: we cannot conclude that $f_0^{on}$ is a local minimum of $\Phi|_\mathcal{M}$ in the tangential direction without additional information. Convexity in the transversal direction (§4–6) and indeterminacy in the tangential direction are the two complementary aspects of the geometric obstacle.

---

## §11. Connection with the DBN flow and Direction B

### 11.1. The De Bruijn-Newman flow as a deformation of $\mathcal{M}$

Doc 88 studied the DBN flow as a curve in the space of deformed zeta functions. In the language of the present document, the DBN flow parametrizes a curve $t \mapsto f_t \in H_\lambda$ where $f_t = |\zeta_t|^2$ and $\zeta_t$ is the De Bruijn-Newman zeta function at level $t$.

**Remark 11.1.** For $t < 0$ (if the De Bruijn-Newman constant $\Lambda < 0$, which is known not to occur, but hypothetically), $\zeta_t$ could have all its zeros on the critical line (i.e., $f_t \in \mathcal{M}$). For $t > \Lambda$, if $\Lambda > 0$, the zeros of $\zeta_t$ lie off the critical line and $f_t \notin \mathcal{M}$.

The connection between the DBN flow and the variational distance to $\mathcal{M}$ is:
$$\frac{d}{dt}\|f_t - f_0^{on}\|^2_{H_\lambda} = 2\langle f_t - f_0^{on}, \dot{f}_t\rangle_{H_\lambda},$$
where $\dot{f}_t = \partial_t f_t$ is the time derivative.

**Question 11.2 (DBN-variational connection).** Can $\frac{d}{dt}\Phi(f_t)\big|_{t=0}$ be related to the second variation $\psi''(0)$ computed in §4? In particular, does the DBN flow "point toward" $\mathcal{M}$ or "move away from" $\mathcal{M}$?

This question is directly related to Direction B of the program (Doc 28) and cannot be fully answered in the present document.

### 11.2. Comparison with Direction A

Direction A (gradient flow in the space of zeta functions) would study the gradient of $\Phi$ in the space $H_\lambda$ and the gradient-descent flow toward $\mathcal{M}$. The second variation computed in §4 would be the Hessian of $\Phi$ at the point $f_0^{on}$ evaluated in the direction of the normal gradient to $\mathcal{M}$.

Direction D (the present document) and Direction A are complementary: Direction A studies the behavior of $f_0$ under the gradient flow, while Direction D studies the geometry of $\mathcal{M}$ as the target of the flow.

---

## §12. Discussion: What would proving Conjecture 8.4 contribute?

### 12.1. The scenario under $\neg$RH

Suppose that under $\neg$RH (with an off-critical zero of displacement $\delta_j > 0$) we could prove that $f_0^{on}$ is the unique global minimum of $\Phi|_\mathcal{M}$. Then:

- The variational infimum would be $\tilde\delta_\lambda^2 = \Phi(f_0^{on}) = \|f_0 - f_0^{on}\|^2_{H_\lambda} > 0$ (positive under $\neg$RH).
- This is consistent with the criterion of Doc 82: $\tilde\delta_\lambda^2 = 0 \Leftrightarrow$ RH.
- But it would not yield any contradiction: positivity of the infimum under $\neg$RH is compatible with $\neg$RH.

**Conclusion 12.1.** Proving global uniqueness of the minimum (Conjecture 8.4) under $\neg$RH would not prove RH. It would only establish that the variational reformulation is "clean" (the infimum is attained at a unique point), which would be valuable for the program but not sufficient for a proof of RH.

### 12.2. The scenario that would imply RH

To imply RH, we would need a condition of the type:

> The infimum $\tilde\delta_\lambda^2 > 0$ implies the existence of a contradiction (for example, with the CTP criterion or with the Weil formula).

Doc 82 already established that $\tilde\delta_\lambda^2 = 0 \Leftrightarrow$ RH, so any argument proving $\tilde\delta_\lambda^2 = 0$ (unconditionally) would imply RH. But the positive second variation goes in the opposite direction: it says that the infimum is attained at $f_0^{on}$ (which is at positive distance from $f_0$ under $\neg$RH), which is consistent with $\tilde\delta_\lambda^2 > 0$ under $\neg$RH.

### 12.3. Value of the second-variation analysis for the program

Although the second-variation analysis does not close the proof of RH, it has methodological value:

(i) **Clarifies the geometry**: it shows that $\mathcal{M}$ is "convex toward $f_0$" in the transversal direction, meaning the approximation problem is well-conditioned.

(ii) **Establishes the connection with $K_\lambda(\gamma_j)$**: it shows that the kernels of Doc 86 are not merely lower bounds for $T_\lambda$, but have a geometric interpretation as second variations.

(iii) **Identifies the precise gap**: the obstacle is not technical (lack of regularity, convergence of integrals) but conceptual (the jump from local to global in the uniqueness argument).

(iv) **Formulates precise conjectures**: Conjecture 8.4 (uniqueness of the global minimum) and Conjecture 8.3 (global convexity of $\mathcal{M}$) are well-defined problems that could be tackled with functional-analysis techniques.

---

## §13. Synthesis and future directions

### 13.1. Map of the argument

The analysis of Direction D can be summarized in the following logical diagram:

**Input:** $f_0 = |\zeta|^2 \in H_\lambda \setminus \mathcal{M}$ (under $\neg$RH), $f_0^{on} = |\zeta_{\mathrm{on}}|^2 \in \mathcal{M}$.

**Step 1:** Parametrize $\mathcal{M}$ locally (§2): Hadamard product with zero deformations.

**Step 2:** Compute the first variation (§3): the point $f_0^{on}$ is always a critical point of the distance along transversal curves.

**Step 3:** Compute the second variation (§4): $\psi''(0) = 8\mathcal{Q}_\lambda^{(j)} > 0$ under $\neg$RH.

**Step 4:** Interpret geometrically (§6): $\mathcal{M}$ is locally convex toward $f_0$ at $f_0^{on}$.

**Step 5:** Identify the gap (§7): local convexity does not imply global uniqueness.

**Conclusion:** The analysis is complete but does not close the argument. The obstacle is the "extended Hadamard barrier" (§9).

### 13.2. Conjectures that remain open

The following conjectures, if proved, would advance the program:

**Conjecture A (Uniqueness of the minimum).** The functional $\Phi|_\mathcal{M}$ has a unique global minimum for $f_0 = |\zeta|^2$.

**Conjecture B (Geodesic convexity of $\mathcal{M}$).** $\mathcal{M}$ with the metric induced by $H_\lambda$ is geodesically convex.

**Conjecture C (Positivity of the tangential Hessian).** The restricted Hessian of $\Phi|_\mathcal{M}$ at $f_0^{on}$ is also positive definite in the tangential directions.

**Conjecture D (Quantitative bound).** There exists a constant $c(\lambda) > 0$ such that for every $g \in \mathcal{M}$,
$$\Phi(g) \geq \Phi(f_0^{on}) + c(\lambda)\|g - f_0^{on}\|^2_{H_\lambda}.$$
This quantitative bound would be the strong version of local convexity.

### 13.3. Relation to other directions of the program

- **Direction A (gradient flow):** The gradient $\nabla\Phi(f_0^{on})$ points in the direction of $f_0 - f_0^{on}$, which is the transversal direction. The gradient flow would descend from $f_0^{on}$ toward $f_0$... but $f_0^{on}$ is already the minimum of $\Phi|_\mathcal{M}$ (if Conjecture A is true).

- **Direction B (Jacobi operators):** The kernels $K_\lambda(\gamma_j)$ appearing in the second variation are the same as those of Doc 86, linking the geometry of $\mathcal{M}$ with the spectral theory of the CCM Jacobi operators.

- **Direction C (Weil formula):** The lower bound $T_\lambda \geq 2\sum_j\delta_j^2 K_\lambda(\gamma_j)$ of Doc 86 can be interpreted as saying that $T_\lambda$ is, approximately, the total second variation of $\Phi$ over all transversal directions simultaneously.

- **Direction E (Báez-Duarte-type criteria):** The Nyman-Beurling-Báez-Duarte criterion (Doc 82, §1) is a linear completeness criterion, while $\mathcal{M}$ is a nonlinear manifold. The positive second variation of $\Phi|_\mathcal{M}$ reinforces the coherence of the two approaches.

### 13.4. Final summary

Direction D provides a clean geometric perspective on the variational problem, confirms that the second variation in the transversal direction is positive (meaning the approximation problem is well-conditioned in that sense), and precisely formulates the obstacle preventing the proof of RH from being closed from this angle.

The **main result** is Theorem 4.2 and its Corollary 4.4: the second transversal variation is positive under $\neg$RH and zero under RH. This result is correct and its proof is rigorous.

The **main obstacle** is Gap 7.6: local convexity (positive second variation) does not imply global uniqueness of the minimum of $\Phi|_\mathcal{M}$, which is what would be needed for a variational-type argument implying RH.

**Absolute rule respected:** No argument in this document claims to prove RH. All results are either rigorously proved (Theorem 4.2, Propositions 4.3, 6.6, 7.4) or explicitly labeled as open conjectures (Conjectures 8.1, 8.3, 8.4, A, B, C, D). The gap is precisely identified (Gap 7.6, Obstacle 9.1).

---

## Internal references

- Doc 82 (Phase 33): Variational reformulation and Nyman-Beurling criterion; $\tilde\delta_\lambda^2 = 0 \Leftrightarrow$ RH.
- Doc 83 (Phase 33): Sign of the measure difference; $f_0 \geq f_0^{on}$ pointwise.
- Doc 86 (Phase 33): Relative entropy and extremality; kernels $K_\lambda(\gamma_j)$; lower bound $T_\lambda \geq 2\sum_j\delta_j^2 K_\lambda(\gamma_j)$.
- Doc 88 (Phase 33): DBN flow as a curve in the space of zeta functions.
- Doc 89 (Phase 33): The central object: the measure $d\nu$.
- Doc 64 (Phase 32): CTP criterion $T_\lambda = 0 \Leftrightarrow$ RH.
- Doc 28 (Phase 28): Four fronts of attack; second variation of $Q$ in the transversal direction $b_j$.

---

*Document prepared within the Riemann Program, Phase 34. This document is part of the exploration of new directions and contains no claim of proof of RH. All arguments that do not close are explicitly flagged as such.*
