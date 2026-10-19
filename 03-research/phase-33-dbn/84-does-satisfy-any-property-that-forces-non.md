# Document 84 — Does $F(z)$ satisfy any property that forces non-zeros in the disk?

**Program:** Riemann Hypothesis — Phase 33 DBN-CCM (Path 2)
**Prerequisites:** Docs 75, 78, 81

---

## Summary

This document systematically explores the analytic properties of $F(z) = \xi(z/(z-1))$ in the unit disk $\{|z| < 1\}$ in order to determine whether any of them forces non-vanishing in the interior, without circular reference to the position of the zeros of $\xi$. §1 studies the question of differential equations for $\xi$ and $F$, concluding that $\xi$ satisfies no useful algebraic ODE. §2 establishes precisely the functional equation satisfied by $F$ under the Möbius transformation: $F(z) = F(1/z)$ (invariance under inversion), and draws its consequences for the zeros. §3 analyzes $F$ as an even function in the variable $\log|z|$. §4 studies the critical points of $F$ given by the functional equation. §5 formulates the Blaschke–Nevanlinna exteriority criterion and its equivalence with RH. §6 establishes the Jensen criterion as a computable condition equivalent to RH. §7 examines the minimum modulus principle. §8 analyzes the Bohr inequality. §9 studies the Kronecker index criterion. §10 synthesizes the results and formulates the most precise open question.

The frank conclusion is that the functional equation $F(z) = F(1/z)$ and the Jensen criterion provide the richest structure to date, but none of the properties studied implies non-vanishing without essentially assuming RH.

---

## §1. Differential equations for $\xi$ and for $F$

### 1.1. The function $\xi$ satisfies no algebraic ODE

The function $\xi(s)$ satisfies no ordinary differential equation of the form
$$P(\xi, \xi', \xi'', \ldots, \xi^{(n)}) = 0$$
with $P$ a polynomial with rational coefficients in $s$. This qualitatively distinguishes it from hypergeometric functions, Bessel functions, $\Gamma$, $\zeta$ (which satisfies the equation $s(s-1)\zeta'' + \ldots$ via the functional equation), or any function of an algebraic $D$-module.

The reason is the following: solutions of algebraic ODEs have zero sets with special algebraic structure (uniform spacing, recurrence relations, etc.), whereas the zeros $1/2 + i\gamma_n$ of $\xi$ on the critical line have a distribution that reflects the distribution of the prime numbers (via the Riemann–Weil explicit formula) and satisfies no known algebraic relation. If $\xi$ satisfied $\xi'' = P(s, \xi, \xi')$, the zeros $\gamma_n$ would satisfy recurrence relations that are incompatible with the irregularity observed in their distribution.

**Proposition 1.1.** *The function $\xi(s)$ satisfies no linear ODE with polynomial coefficients, nor any first-order polynomial ODE. In particular, there is no equation $\xi'' = R(s)\xi$ with $R$ rational that $\xi$ satisfies globally.*

*Justification.* A second-order linear ODE $\xi'' = R(s)\xi$ with $R$ rational would have the solution $\xi$ as a function with algebraic monodromy around each pole of $R$. But $\xi$ is entire (no singularities) and of order 1: if $R$ were a polynomial of degree $d$, the solutions would be entire functions of order $(d+2)/2$; for $d=0$ (constant coefficient) one obtains exponentials of order 1, but the exponentials $e^{as+b}$ have no zeros, while $\xi$ has infinitely many zeros. For $d \geq 1$, the order of the solution would be greater than 1, contradicting the exact order 1 of $\xi$. $\square$

### 1.2. The integral representation and its derivatives

The Riemann integral representation
$$\xi(s) = 2\int_1^\infty \phi(t)\, t^{(s-1)/2}\, dt, \qquad \phi(t) = \sum_{n=1}^\infty (2\pi^2 n^4 t^2 - 3\pi n^2 t) e^{-\pi n^2 t},$$
allows differentiation under the integral sign: $\xi'(s) = \int_1^\infty \phi(t) t^{(s-1)/2} \log t\, dt$. This gives a relation between $\xi'$ and $\xi$ only in the integral sense (not differential), which does not constitute an ODE.

### 1.3. The differential equation of $F$

Since $F(z) = \xi(z/(z-1))$ and $\xi$ satisfies no algebraic ODE, $F$ likewise satisfies no algebraic ODE in $z$ whose solutions are automatically zero-free in the disk. Any differential relation for $F$ inherited from the integral representation of $\xi$ is of integral type and does not provide the local information (in $z$) needed to control zeros.

**Conclusion of §1.** The study of differential equations offers no direct route to proving the non-vanishing of $F$ in the disk.

---

## §2. The functional equation of $F$ and its consequences

### 2.1. Derivation of $F(z) = F(1/z)$

Let $s = z/(z-1) = \tau(z)$. The functional equation of $\xi$ is $\xi(s) = \xi(1-s)$. The point $1-s$ corresponds, in disk coordinates, to the point $z'$ such that $\tau(z') = 1 - \tau(z)$, that is:
$$\frac{z'}{z'-1} = 1 - \frac{z}{z-1} = 1 + \frac{z}{1-z} = \frac{1-z+z}{1-z} = \frac{1}{1-z}.$$
Solving for $z'$: from $z'/(z'-1) = 1/(1-z)$, one gets $z'(1-z) = z'-1$, that is, $z' - z'z = z' - 1$, that is, $z'z = 1$, so $z' = 1/z$.

**Proposition 2.1.** *For all $z \neq 0$, $F(1/z) = F(z)$. The function $F$ is invariant under the inversion $z \mapsto 1/z$.*

*Proof.* $F(1/z) = \xi(\tau(1/z)) = \xi(1 - \tau(z)) = \xi(\tau(z)) = F(z)$, where the functional equation of $\xi$ and the computation $\tau(1/z) = 1 - \tau(z)$ shown above have been used. $\square$

### 2.2. Zeros of $F$ in inversive pairs

**Corollary 2.2.** *If $z_0$ is a zero of $F$, then $1/z_0$ is also a zero of $F$. In particular:*
- *If $|z_0| < 1$ (zero in the disk), then $|1/z_0| > 1$ (zero outside the disk).*
- *If $|z_0| = 1$ (zero on the boundary), then $1/z_0 = \bar{z}_0$ is also on the boundary.*

*Proof.* Immediate consequence of Proposition 2.1. $\square$

### 2.3. The functional equation and RH

Under $\neg$RH, there exist zeros $\rho_0 = \sigma_0 + i\gamma_0$ of $\xi$ with $\sigma_0 > 1/2$. These map to $z_0 = \tau(\rho_0) = \rho_0/(\rho_0-1)$ with $|z_0| > 1$ (outside the disk, by Proposition 1.1 of Doc 81). Its inverse $1/z_0 = (\rho_0-1)/\rho_0 = 1 - 1/\rho_0$ satisfies $|1/z_0| < 1$.

**Direct verification.** $|1/z_0|^2 = |(\rho_0-1)/\rho_0|^2 = ((\sigma_0-1)^2 + \gamma_0^2)/(\sigma_0^2 + \gamma_0^2)$. The condition $|1/z_0| < 1$ is equivalent to $(\sigma_0-1)^2 + \gamma_0^2 < \sigma_0^2 + \gamma_0^2$, that is, $(\sigma_0-1)^2 < \sigma_0^2$, that is, $-2\sigma_0 + 1 < 0$, that is, $\sigma_0 > 1/2$. $\checkmark$

**Corollary 2.3.** *$\neg$RH is equivalent to $F$ having zeros in $\{|z| < 1\}$, which are exactly the points $1-1/\rho_0$ for each off-critical zero $\rho_0$ with $\mathrm{Re}(\rho_0) > 1/2$.*

### 2.4. What the functional equation does not imply

The functional equation $F(z) = F(1/z)$ pairs zeros in the disk with zeros outside the disk. This is a symmetry of the zeros, not a restriction that eliminates them from the disk. In particular, the functional equation alone does not exclude the existence of zeros in $\{|z| < 1\}$: any function that is even under $z \mapsto 1/z$ may or may not have zeros in the disk.

---

## §3. $F$ as an even function in $\log|z|$

### 3.1. Structure under the polar parametrization

Writing $z = re^{i\theta}$ with $r > 0$, $\theta \in [0, 2\pi)$, the invariance $F(re^{i\theta}) = F(e^{i\theta}/r)$ says that $F$ evaluated at radius $r$ and angle $\theta$ coincides with $F$ evaluated at radius $1/r$ and angle $\theta$. If the variable $u = \log r$ is introduced, this translates into $F(e^{u+i\theta})$ being an even function of $u$ for each fixed $\theta$:
$$F(e^{u+i\theta}) = F(e^{-u+i\theta}).$$

### 3.2. The function $H(u, \theta)$

Let us formally define $H(u, \theta) = F(e^{u+i\theta})$ for $u \in \mathbb{R}$ and $\theta \in [0, 2\pi)$. The analyticity condition of $F$ (as a function of $z = e^{u+i\theta} = re^{i\theta}$) is expressed in terms of $H$ as the Cauchy-Riemann equations in logarithmic-polar coordinates. The parity $H(u, \theta) = H(-u, \theta)$ implies that the Fourier-Laurent series of $F$ around $z = 0$ has only powers $z^k + z^{-k}$:

If $F(z) = \sum_{k=-\infty}^{\infty} c_k z^k$ (in the annulus $0 < |z| < 1$, but $F$ is analytic in the disk, so $c_k = 0$ for $k < 0$ and $F(z) = \sum_{k=0}^\infty c_k z^k$), the condition $F(1/z) = F(z)$ implies $\sum_{k=0}^\infty c_k z^{-k} = \sum_{k=0}^\infty c_k z^k$. Since $F$ is analytic in the disk, the only way for this to be consistent with the analyticity of $F$ in the disk and that of $F(1/z)$ outside the disk is for $F$ to be constant, which is false.

**Clarification.** The equation $F(z) = F(1/z)$ does not imply that $F$ is a function of $z + 1/z$, because $F$ is not analytic on all of $\mathbb{C} \setminus \{0\}$ (it has singularities at $z = 1$ and $z = \infty$). The equality $F(z) = F(1/z)$ relates values of $F$ in the disk to values outside the disk, and is perfectly consistent with $F$ being analytic only in the disk.

### 3.3. Correct consequence for the Taylor coefficients

Let $F(z) = \sum_{k=0}^\infty c_k z^k$ be the Taylor expansion in the disk. The condition $F(z) = F(1/z)$ for $|z| = 1$ (that is, on the boundary) gives:
$$\sum_{k=0}^\infty c_k e^{ik\theta} = \sum_{k=0}^\infty c_k e^{-ik\theta} \quad \text{for almost every } \theta.$$
This implies $c_k = \bar{c}_{-k}$, but since $c_k = 0$ for $k < 0$ (by analyticity in the disk), the condition reduces to $c_k = \bar{c}_{-k} = 0$ for $k > 0$... which would imply $c_k = 0$ for all $k > 0$, a contradiction.

**Resolution.** The equality $F(e^{i\theta}) = F(e^{-i\theta})$ is the correct condition on the boundary (that $F$ be real on the circle), and holds only if the coefficients $c_k$ are real. The Taylor coefficients of $F$ at $z = 0$ are the values $\xi^{(k)}(0)/k!$, which are real (since $\xi$ is real on the real line). Therefore $c_k \in \mathbb{R}$ and the boundary condition $F(e^{i\theta}) = \overline{F(e^{i\theta})}$ (that $F$ be real on the boundary) is equivalent to $c_k \in \mathbb{R}$, which is automatic.

The stronger condition $F(z) = F(1/z)$ for $z$ in the interior of the disk holds as an identity between the value at $z$ (interior) and the value at $1/z$ (exterior), and is a direct consequence of $\xi(s) = \xi(1-s)$.

---

## §4. Critical points of $F$ and local geometry

### 4.1. The fixed points of $z \mapsto 1/z$ in the disk

The fixed points of the involution $z \mapsto 1/z$ are the points with $z = 1/z$, that is, $z^2 = 1$, that is, $z = \pm 1$. The point $z = +1$ is on the boundary of the disk (where $F$ is not defined, since $\tau(1) = \infty$). The point $z = -1$ is on the boundary of the disk.

The derivative: $\frac{d}{dz}F(1/z) = -\frac{1}{z^2}F'(1/z)$. The equality $F(z) = F(1/z)$ differentiated gives:
$$F'(z) = -\frac{1}{z^2}F'(1/z).$$
Evaluating at $z = -1$: $F'(-1) = -F'(-1)$, which implies $F'(-1) = 0$.

**Proposition 4.1.** *The point $z = -1$ is a critical point of $F$: $F'(-1) = 0$.*

### 4.2. The meaning of $z = -1$

The point $z = -1$ corresponds to $s = \tau(-1) = (-1)/(-1-1) = (-1)/(-2) = 1/2$. Therefore, $F(-1) = \xi(1/2)$. The critical point $z = -1$ of $F$ corresponds to the center of the critical strip, which is the symmetry point of the functional equation of $\xi$.

**Remark 4.2.** The value $\xi(1/2)$ can be computed explicitly: $\xi(1/2) = \frac{1}{2}\cdot\frac{1}{2}\cdot(-\frac{1}{2})\cdot\pi^{-1/4}\Gamma(1/4)\zeta(1/2)$... No. More directly, from the standard normalization, $\xi(1/2) \approx 0.4971$. The critical point of $F$ at $z = -1$ has value $F(-1) \approx 0.4971 \neq 0$, which is consistent with non-vanishing on the boundary (RH says nothing about zeros of $\xi$ at real $s = 1/2$; $\xi(1/2) \neq 0$).

### 4.3. Local behavior at $z = 0$

The point $z = 0$ corresponds to $s = \tau(0) = 0$, and $F(0) = \xi(0) = 1/2$. The Taylor series of $F$ at $z = 0$ is:
$$F(z) = \xi(0) + \xi'(0)\cdot\frac{d\tau}{dz}\bigg|_{z=0} z + O(z^2) = \frac{1}{2} + \xi'(0)\cdot\frac{-1}{(z-1)^2}\bigg|_{z=0}\cdot z + O(z^2) = \frac{1}{2} - \xi'(0) z + O(z^2).$$
Since $\xi(0) = 1/2$ and $\xi'(0) = 0$ (as $\xi$ is symmetric about $s = 1/2$ and the point $s = 0$ corresponds to $z = 0$, while the symmetry of $\xi$ about $s = 1/2$ gives $\xi'(s) = -\xi'(1-s)$, and at $s = 0$: $\xi'(0) = -\xi'(1)$; both by the functional relation, and since $\xi$ is real on the real line one can verify numerically that $\xi'(0) \neq 0$ in general). Note that $F(0) = 1/2 > 0$, which guarantees that $F$ does not vanish at $z = 0$.

---

## §5. Blaschke factorization and the exteriority condition

### 5.1. The Nevanlinna factorization

If $F \in H^\infty(\mathbb{D})$ (Hardy), the Nevanlinna-Pick factorization decomposes $F$ as
$$F(z) = B(z) \cdot G(z),$$
where $B(z) = e^{i\phi}\prod_{k} \frac{z - z_k}{1 - \bar{z}_k z}$ is the Blaschke product associated to the zeros $\{z_k\}$ of $F$ with $|z_k| < 1$ (counted with multiplicity), and $G(z)$ is a function in $H^\infty$ with no zeros in the disk (an exterior function if $F$ is in the class $N^+$).

Under RH, $F$ has no zeros in the disk, so $B(z) \equiv 1$ and $F = G$ is a zero-free (exterior) function.

**Proposition 5.1.** *RH is equivalent to $F(z)$ being a zero-free function in $H(\mathbb{D})$, that is, to the Blaschke-Nevanlinna factorization of $F$ having trivial Blaschke product: $B \equiv 1$.*

### 5.2. Exterior functions in $H^2$

A zero-free function $G \in H^2(\mathbb{D})$ is said to be exterior if it is completely determined by its modulus on the boundary via the Poisson formula:
$$\log G(z) = \frac{1}{2\pi}\int_0^{2\pi} \frac{e^{i\theta}+z}{e^{i\theta}-z} \log|F(e^{i\theta})|\, d\theta, \qquad |z| < 1.$$
(with an appropriate phase constant). The necessary and sufficient condition for $G$ to be exterior (and not merely zero-free) is that the right-hand side converge and define a function in $H^2$.

**Note of caution.** The function $F$ is not in $H^2$ nor in $H^\infty$: $F(z) = \xi(\tau(z))$ grows without bound as $z \to 1$ (since $\xi(s) \to \infty$ as $s \to \infty$). Therefore, the standard theory of exterior functions in $H^2$ or $H^\infty$ does not apply directly. Proposition 5.1 asserts non-vanishing (equivalence with RH) but not exteriority in the $H^2$ sense.

---

## §6. The Jensen formula as a computable criterion

### 6.1. The Jensen formula for $F$

Let $F$ be analytic in the disk $\{|z| \leq r\}$ for $r < 1$ (which is true for every $r < 1$ since $F$ is analytic in $\{|z|<1\}$). The Jensen formula establishes:
$$\frac{1}{2\pi}\int_0^{2\pi}\log|F(re^{i\theta})|\, d\theta = \log|F(0)| + \sum_{|z_k| < r}\log\frac{r}{|z_k|},$$
where the sum runs over the zeros $z_k$ of $F$ in the disk $\{|z| < r\}$ (counted with multiplicity).

Taking $r \to 1^-$, and assuming that $\log|F(e^{i\theta})|$ is integrable on the boundary (which requires verification, given the singularity at $\theta$ corresponding to $z = 1$), one obtains in the limit:
$$\frac{1}{2\pi}\int_0^{2\pi}\log|F(e^{i\theta})|\, d\theta = \log|F(0)| + \sum_{|z_k| < 1}\log\frac{1}{|z_k|}.$$

### 6.2. The numerical criterion

Since $\log(1/|z_k|) > 0$ for $|z_k| < 1$, the sum is non-negative, and is exactly zero if and only if there are no zeros in the disk.

**Proposition 6.1.** *Assuming $\log|F(e^{i\theta})|$ is integrable on $[0, 2\pi)$,*
$$\text{RH} \iff \frac{1}{2\pi}\int_0^{2\pi}\log|F(e^{i\theta})|\, d\theta = \log|F(0)| = \log\frac{1}{2} = -\log 2.$$

*If $\neg$RH, the integral is strictly greater than $-\log 2$.*

### 6.3. Integrability of $\log|F(e^{i\theta})|$

The function $\log|F(e^{i\theta})| = \log|\xi(1/2 + it_\theta)|$, where $t_\theta$ is the parametrization of the critical line. This function has logarithmic singularities at the $\theta$ corresponding to the zeros of $\xi$, which are of the form $\log|e^{i\theta} - e^{i\theta_n}|$ near each $\theta_n$. Such singularities are integrable (since $\int_0^\epsilon |\log t|\, dt < \infty$). The zeros of $\xi$ are simple (believed unconditionally, and proved for all known zeros), which ensures that the singularities are $\sim \log|t - \gamma_n|$ and integrable. Therefore, $\log|F(e^{i\theta})|$ is integrable.

### 6.4. The integral in terms of $\xi$ over the critical line

The integral over the boundary of the disk corresponds, via the change of variable $z(t) = -e^{2i\arctan(2t)}$ (Proposition 1.3 of Doc 81), to an integral over the critical line:
$$\frac{1}{2\pi}\int_0^{2\pi}\log|\xi(1/2+it_\theta)|\, d\theta = \int_{-\infty}^{\infty}\log|\xi(1/2+it)|\, \frac{2\, dt}{\pi(1+4t^2)}.$$
(The Jacobian of the change of variable $\theta \mapsto t$ is $|d\theta/dt| = 4/(1+4t^2)$, the density of the standard scaled Cauchy distribution.) The RH criterion then becomes:
$$\text{RH} \iff \int_{-\infty}^{\infty}\log|\xi(1/2+it)|\cdot\frac{2\, dt}{\pi(1+4t^2)} = -\log 2.$$

**Remark 6.2.** This integral has the form of a weighted average of $\log|\xi(1/2+it)|$ with weight $2/(\pi(1+4t^2))$ (a Cauchy distribution, of total mass 1). The RH criterion is exactly that this weighted average equal $\log|\xi(0)| = \log(1/2)$.

### 6.5. Evaluation via the explicit formula and the logarithm of $|\xi|$

The logarithm of $|\xi(1/2+it)|$ can be expressed via the Riemann explicit formula:
$$\log|\xi(1/2+it)| = \text{Re}\log\xi(1/2+it) = \text{Re}\left[\log\xi(0) + \sum_\rho\log\left(1 - \frac{1/2+it}{\rho}\right)\right].$$

Integrating this against the weight $2/(\pi(1+4t^2))$ and comparing with $\log\xi(0) = -\log 2$ requires showing that:
$$\sum_\rho \int_{-\infty}^{\infty}\text{Re}\log\left(1 - \frac{1/2+it}{\rho}\right)\cdot\frac{2\, dt}{\pi(1+4t^2)} = 0.$$
By the symmetry of the Hadamard product $\xi(s) = \xi(0)\prod_\rho (1 - s/\rho)(1 - s/(1-\rho))$ (pairing $\rho$ with $1-\rho$), the condition reduces to showing that for each pair $(\rho, 1-\rho)$:
$$\int_{-\infty}^{\infty}\text{Re}\left[\log\left(1-\frac{1/2+it}{\rho}\right) + \log\left(1-\frac{1/2+it}{1-\rho}\right)\right]\frac{2\, dt}{\pi(1+4t^2)} = 0.$$

**Proposition 6.3.** *The above condition is equivalent to the weighted Cauchy average of $\log|1 - (1/2+it)/\rho| + \log|1 - (1/2+it)/(1-\rho)|$ being zero, for each pair $(\rho, 1-\rho)$.*

The explicit evaluation of this integral by the residue theorem or by properties of the Poisson transform of the disk is possible in principle, but its result depends on the position of $\rho$: if $\mathrm{Re}(\rho) = 1/2$ (RH), the symmetry guarantees the cancellation; if $\mathrm{Re}(\rho) \neq 1/2$, the cancellation fails. This makes the criterion exact but circular.

---

## §7. The minimum modulus principle

### 7.1. Statement

The minimum modulus principle states: if $g$ is analytic and zero-free in a domain $\Omega$, then $|g|$ has no strict local minimum in the interior of $\Omega$; the minimum of $|g|$ over a compact $K \subset \Omega$ is attained on the boundary $\partial K$.

Applied to $F$: if $F$ had no zeros in $\{|z| < 1\}$ (under RH), the minimum of $|F(z)|$ for $|z| \leq r$ would be attained at $|z| = r$. As $r \to 1^-$, the infimum of $|F|$ on the boundary is 0 (since $F$ has zeros at $|z| = 1$, corresponding to the zeros of $\xi$ on the critical line). Therefore, the minimum principle only guarantees that $|F(z)| \geq \inf_{|z|=r}|F(z)|$, and as $r \to 1$, this lower bound tends to 0.

### 7.2. Why it gives no useful information

The minimum modulus principle cannot prove non-vanishing in the interior because it gives a trivial lower bound (0). For it to be useful, a strict lower bound $|F(z)| \geq c > 0$ would be needed on some circle $|z| = r$ for $r < 1$, which would amount to knowing non-vanishing in $|z| < r$, an easier problem (since $\tau$ maps $|z| < r < 1$ to the region $\mathrm{Re}(s) < \sigma_r < 1/2$, where non-vanishing of $\xi$ is known for sufficiently small $\sigma_r$ but not for $\sigma_r$ close to $1/2$).

**Proposition 7.1.** *The minimum modulus principle does not provide a sufficient condition for the non-vanishing of $F$ in the unit disk in the presence of zeros of $F$ on the boundary.*

---

## §8. The Bohr inequality

### 8.1. The classical statement

The Bohr inequality states: if $f(z) = \sum_{k=0}^\infty a_k z^k$ is analytic in the disk with $|f(z)| < 1$ for all $|z| < 1$, then
$$\sum_{k=0}^\infty |a_k| r^k \leq 1 \quad \text{for all } r \leq 1/3,$$
and the constant $1/3$ is optimal (Bohr radius).

### 8.2. Inapplicability to $F$

The function $F$ does not satisfy the hypothesis $|F(z)| < 1$ in the disk: at $z = 0$, $|F(0)| = 1/2 < 1$, but as $|z| \to 1$, $|F(z)| = |\xi(1/2 + it_\theta)|$ is not bounded by 1 (the maximum of $|\xi|$ over the critical line exceeds 1). Consequently, the Bohr inequality does not apply.

**Proposition 8.1.** *The function $F(z)$ does not satisfy the hypotheses of the Bohr inequality in the unit disk, and the Bohr inequality provides no information about the zeros of $F$.*

---

## §9. The Kronecker index criterion

### 9.1. The winding number and the zeros in the disk

By the argument principle, the number of zeros of $F$ in $\{|z| < r\}$ (counted with multiplicity) is:
$$N(r) = \frac{1}{2\pi i}\oint_{|z|=r}\frac{F'(z)}{F(z)}\, dz = \frac{1}{2\pi}\Delta_{|z|=r}\arg F.$$
If $F$ had no zeros in the disk ($N(r) = 0$ for all $r < 1$), the argument of $F(re^{i\theta})$ would accumulate no total variation when traversing $|z| = r$. Taking $r \to 1^-$, the number of zeros in the disk would be the Kronecker index of the curve $F(e^{i\theta})$ (for $\theta \in [0, 2\pi)$) around the origin.

### 9.2. The index of the curve $F(e^{i\theta})$ in the presence of boundary zeros

The curve $F(e^{i\theta}) = \xi(1/2 + it_\theta)$, for $\theta \in (0, 2\pi)$, passes through the origin at each $\theta_n$ corresponding to a zero of $\xi$ on the critical line. The argument of $\xi(1/2 + it)$ is a continuous function of $t$ except at the zeros, where it has jumps of $\pm \pi$ (argument jumps when crossing a simple zero). The total variation of the argument of $F(e^{i\theta})$ as $\theta$ traverses $[0, 2\pi)$ involves infinitely many discontinuities.

When the curve passes through the origin (at the zeros of $\xi$ on the critical line), the Kronecker index is not well defined as an integer by the standard contour integral formula. The definition of the index for curves passing through the origin requires special treatment (intersection index, regularization).

**Proposition 9.1.** *The Kronecker index criterion does not apply directly to $F$ because the curve $F(e^{i\theta})$ passes through the origin (at the boundary points corresponding to the zeros of $\xi$ on the critical line), which makes the index ill-defined by the standard integral formula.*

**Corollary 9.2.** *It is not possible to deduce the non-vanishing of $F$ in the disk from the computation of the Kronecker index of the boundary curve, because of the zeros of $F$ on the boundary.*

---

## §10. Synthesis and the most precise open question

### 10.1. Table of results

| Tool | Result |
|---|---|
| Algebraic ODE for $\xi$ or $F$ | Does not exist; inapplicable |
| Functional equation $F(z) = F(1/z)$ | Proved; pairs zeros but does not eliminate them |
| Critical points of $F$ | $F'(\pm 1) = 0$; geometrically clear; does not imply non-zeros |
| Blaschke factorization | RH $\iff$ $B \equiv 1$; exact but circular |
| Jensen formula | Computable criterion; exact but circular |
| Minimum modulus principle | Trivial lower bound (0); inapplicable |
| Bohr inequality | Hypotheses not satisfied; inapplicable |
| Kronecker index | Ill-defined due to boundary zeros |

### 10.2. The consolidated theorem of Path 2

**Theorem 10.1.** *Let $\xi$ be the Riemann xi function and $F(z) = \xi(z/(z-1))$. Then:*

*(i) $F$ is analytic in the open disk $\{|z| < 1\}$.*

*(ii) $F(0) = 1/2$.*

*(iii) $F(z) = F(1/z)$ for all $z \neq 0, 1$ (functional equation).*

*(iv) $F'(-1) = 0$ (critical point at $z = -1$, corresponding to $s = 1/2$).*

*(v) The Jensen formula holds for $F$, and the Jensen criterion gives:*
$$\text{RH} \iff \int_{-\infty}^{\infty}\log|\xi(1/2+it)|\cdot\frac{2\, dt}{\pi(1+4t^2)} = -\log 2.$$

*(vi) RH $\iff$ $F$ has no zeros in $\{|z| < 1\}$ (Proposition 2.1 of Doc 81).*

*(vii) None of properties (i)–(iv) implies (vi); property (v) is equivalent to (vi) and to RH.*

### 10.3. The most precise open question

The properties established in Theorem 10.1 reformulate RH exactly but offer no proof. The question that remains, in the most precise formulation that can be given in this document, is the following:

**Question 10.2 (central to Path 2).** *Can the equality*
$$\int_{-\infty}^{\infty}\log|\xi(1/2+it)|\cdot\frac{2\, dt}{\pi(1+4t^2)} = -\log 2 \eqno{(*)}$$
*be proved using only the properties of $\xi$ as an entire function of order 1 with the functional equation $\xi(s) = \xi(1-s)$, the Hadamard product, and the known asymptotic behavior of $\xi$, without knowing the precise position of the zeros?*

### 10.4. Why $(*)$ is difficult

The equality $(*)$ can be written, using the Hadamard product $\xi(s) = \xi(0)\prod_\rho(1 - s/\rho)(1 - s/(1-\rho))$, as:

$$\int_{-\infty}^{\infty}\log\xi(0)\cdot\frac{2\, dt}{\pi(1+4t^2)} + \sum_\rho\int_{-\infty}^{\infty}\text{Re}\left[\log\left(1-\frac{1/2+it}{\rho}\right) + \log\left(1-\frac{1/2+it}{1-\rho}\right)\right]\frac{2\, dt}{\pi(1+4t^2)} = -\log 2.$$

The first term is $\log\xi(0) = \log(1/2) = -\log 2$. Therefore, $(*)$ is equivalent to the sum over the zeros being zero:
$$\sum_\rho\int_{-\infty}^{\infty}\text{Re}\left[\log\left(1-\frac{1/2+it}{\rho}\right) + \log\left(1-\frac{1/2+it}{1-\rho}\right)\right]\frac{2\, dt}{\pi(1+4t^2)} = 0. \eqno{(**)}$$

For a pair $(\rho, 1-\rho)$ with $\rho = \sigma + i\gamma$, the integral in $(**)$ can in principle be evaluated via the residue theorem. The pole of the integrand in the upper half-plane (where $\text{Im}(t) > 0$) comes from the weight $2/(\pi(1+4t^2)) = 2/(\pi(2it+1)(-2it+1))$, which has simple poles at $t = \pm i/2$. The integral is:

$$I(\rho) = \text{Re}\left[\log\left(1 - \frac{1/2 + i(i/2)}{\rho}\right) + \log\left(1 - \frac{1/2 + i(i/2)}{1-\rho}\right)\right] = \text{Re}\left[\log\left(1 - \frac{1}{\rho}\right) + \log\left(1 - \frac{1}{1-\rho}\right)\right].$$

Simplifying: $1 - 1/\rho = (\rho-1)/\rho$ and $1 - 1/(1-\rho) = -\rho/(1-\rho)$. Therefore:
$$I(\rho) = \text{Re}\left[\log\frac{\rho-1}{\rho} + \log\frac{-\rho}{1-\rho}\right] = \text{Re}\left[\log\frac{(\rho-1)(-\rho)}{\rho(1-\rho)}\right] = \text{Re}\left[\log\frac{-(rho-1)}{1-\rho}\right] = \text{Re}[\log 1] = 0.$$

(Since $(\rho-1)(-\rho)/(\rho(1-\rho)) = -(\rho-1)\rho/(\rho(1-\rho)) = -(\rho-1)/(1-\rho) = (\rho-1)/(\rho-1) = 1$.)

**Proposition 10.3.** *For each pair of zeros $(\rho, 1-\rho)$ of $\xi$, the individual contribution to the left-hand side of $(**)$ is exactly zero, regardless of the position of $\rho$ in the critical strip.*

**Corollary 10.4.** *The equality $(*)$ — equivalent to RH via the Jensen criterion — holds for every entire function of the form $\xi(s) = c\prod_\rho (1-s/\rho)(1-s/(1-\rho))$ with $c = \xi(0)$, regardless of whether the zeros $\rho$ lie on the critical line or not.*

### 10.5. The collapse of the Jensen criterion as a tool for RH

Proposition 10.3 and Corollary 10.4 are the central result of this document, and its content is negative: the Jensen criterion $(*)$, although equivalent to RH in the formal sense of Proposition 6.1, holds unconditionally for $\xi$ thanks to the structure of the Hadamard product and the functional equation $\xi(s) = \xi(1-s)$.

**The resolution of the apparent contradiction** is as follows. Proposition 6.1 establishes:
$$\text{RH} \iff \frac{1}{2\pi}\int_0^{2\pi}\log|F(e^{i\theta})|\, d\theta = -\log 2,$$
but this equivalence depends on the limit $r \to 1^-$ in the Jensen formula being valid. If $F$ has zeros in the disk (under $\neg$RH), the Jensen formula with $r < 1$ gives $\frac{1}{2\pi}\int\log|F(re^{i\theta})|d\theta = -\log 2 + \sum_{|z_k|<r}\log(r/|z_k|)$. Taking $r \to 1^-$, the right-hand side would tend to $-\log 2 + \sum_{|z_k|<1}\log(1/|z_k|) > -\log 2$. However, the integral $\int\log|F(e^{i\theta})|d\theta$ with $r = 1$ exactly also reflects the boundary zeros, and the cancellation of Proposition 10.3 occurs in the computation with $r = 1$ exact, not for $r < 1$.

Strictly speaking, the computation of Proposition 10.3 evaluates the integral $\int_{-\infty}^\infty \log|\xi(1/2+it)| \cdot 2/(\pi(1+4t^2))dt$ using the residue at $t = i/2$, which corresponds to evaluating $\log|\xi(s)|$ at $s = 1/2 + i(i/2) = 1/2 - 1/2 = 0$... There is a sign error: the pole of the weight $2/(\pi(1+4t^2))$ in the upper half-plane is $t = i/2$, which corresponds to $s = 1/2 + i(i/2) = 1/2 - 1/2 = 0$, not to $s$ in the critical strip. The residue integral evaluates the analytically continued function beyond the critical line, not the value of $\log|\xi|$ on the line.

**Proposition 10.5 (correction).** *The residue computation of Proposition 10.3 is valid only if $\log|\xi(1/2+it)|$ extends analytically to the upper half-plane as a function of $t$, which is not the case: $\log|\xi(1/2+it)|$ is a real function of the real parameter $t$ and has no singularity-free holomorphic extension (its singularities are exactly the zeros of $\xi$ on the critical line, at $t = \gamma_n$, where $\log|\xi|$ has logarithmic singularities).*

*Therefore, the integral $\int_{-\infty}^\infty \log|\xi(1/2+it)| \cdot 2/(\pi(1+4t^2))dt$ cannot be evaluated directly by residues.*

Consequently, the Jensen criterion is neither trivially verifiable nor trivially circular: its direct verification requires controlling the distribution of the zeros $\gamma_n$ on the critical line, which is precisely the information that RH provides (and $\neg$RH would deny).

### 10.6. Frank summary

The properties of $F$ studied in this document are:
1. **Functional equation $F(z) = F(1/z)$:** proved, does not force non-zeros in the disk.
2. **Jensen criterion:** equivalent to RH, computable in principle, but direct verification requires knowing the zeros or their distribution on the critical line.
3. **Additional analytic properties** (Bohr, minimum modulus, Kronecker): not applicable due to unsatisfied hypotheses or degeneration at the boundary.

**The state of Path 2 at the close of Doc 84 is as follows:** there is an exact and elegant reformulation of RH in terms of the function $F(z)$ in the disk, with the Jensen criterion as the most transparent condition. The barrier is that every verification of that condition requires information about the zeros of $\xi$, and no property of $F$ has been identified that is verifiable without such information and that implies non-vanishing in the disk.

The most promising direction for the next phase is Question P1 of Doc 81: the search for a functional or differential equation for $F$ that is stronger than $F(z) = F(1/z)$ and whose solutions are automatically zero-free in the disk. Such an equation, if it existed, would have to use arithmetic properties of $\xi$ (via the zeta function and the prime numbers) beyond the pure functional equation.

---

*Doc 84 completed. Next: Phase 35, exploration of P1 (differential equation of $F$) and arithmetic connection via the Green's function of the disk.*
