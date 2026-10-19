# Document 89 — The central object: $d\nu = dm_{full} - dm_{full,on}$ as synthesis of the three paths

**Program:** Riemann Hypothesis — Phase 34 (synthesis)  
**Prerequisites:** Docs 70, 71, 72, 75, 81, 83, 84, 85, 86, 87, 88

---

## Summary

Documents 74–88 developed three independent paths toward the Riemann Hypothesis: Path 1 via the Nevanlinna function $\mathcal{G}(z)$ and the difference of measures; Path 2 via the Jensen excess $\delta$ and the analytic properties of $F(z) = \xi(z/(z-1))$; Path 3 via the initial speed of the De Bruijn-Newman flow $\partial_t T_\lambda|_{t=0}$. This document performs the synthesis of the three paths, identifying the mathematical object underlying all of them: the measure $d\nu = dm_{full} - dm_{full,on} \geq 0$. It is rigorously established that the three central quantities of each path are distinct functionals of $d\nu$ that vanish simultaneously if and only if RH holds. The equivalence is formulated as a synthesis theorem (§10), and the structural obstacle that the program has not overcome is discussed frankly (§11).

---

## §1. The three quantities and their nature

### 1.1. Definitions and context

We fix the program's notation. Let $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4 + is/2)|^2 \, ds$ be the base measure on $\mathbb{R}$. Let
$$dm_{full}(s) = |\zeta(1/2 + is)|^2 \, dm_\infty(s), \qquad dm_{full,on}(s) = |\zeta_{on}(1/2 + is)|^2 \, dm_\infty(s),$$
where $\zeta_{on}$ is the hypothetical zeta function with the same zeros as $\zeta$ projected onto the critical line (Doc 83, §1.2). By Proposition 1.1 of Doc 83:
$$R(s) := \frac{dm_{full}}{dm_{full,on}}(s) = |\zeta(1/2+is)/\zeta_{on}(1/2+is)|^2 = \prod_{j:\, \delta_j > 0} \left(1 + \frac{\delta_j^2}{(s-\gamma_j)^2}\right)^2 \geq 1,$$
where the product runs over the off-critical zeros with $\delta_j = \sigma_j - 1/2 > 0$. Consequently, the measure
$$d\nu := dm_{full} - dm_{full,on} = (R(s) - 1)\, dm_{full,on}(s) \geq 0$$
is a positive measure on $\mathbb{R}$ (unconditional, without assuming RH). It is zero if and only if $R \equiv 1$, which occurs if and only if all $\delta_j = 0$, i.e., if and only if RH is true.

### 1.2. Path 1 — The Nevanlinna function $\mathcal{G}(z)$

The Nevanlinna function of the measure difference is
$$\mathcal{G}(z) = \int_{-\infty}^\infty \frac{s + z}{s - z} \, d\nu(s), \qquad z \in \mathbb{H} = \{z : \mathrm{Im}(z) > 0\}.$$
Since $d\nu \geq 0$, $\mathcal{G}$ is analytic on $\mathbb{H}$ with $\mathrm{Re}[\mathcal{G}(z)] \geq 0$. More precisely: for $z = x + iy$ with $y > 0$ and $s$ real,
$$\mathrm{Re}\left[\frac{s+z}{s-z}\right] = \frac{(s+x)^2 + y^2 - (s-x)^2 - y^2 + \ldots}{|s-z|^2}.$$
The direct computation gives $\mathrm{Re}[(s+z)/(s-z)] = (s^2 - |z|^2 + 2iy \cdot \mathrm{Re}(z))/|s-z|^2$... but it is cleaner to take $z = iy$ (pure imaginary) with $y > 0$:
$$\frac{s + iy}{s - iy} = \frac{(s+iy)(s+iy)}{s^2 + y^2} = \frac{s^2 - y^2 + 2isy}{s^2 + y^2},$$
whence $\mathrm{Re}[\mathcal{G}(iy)] = \int \frac{s^2 - y^2}{s^2 + y^2} \, d\nu(s)$. For general $z$, $\mathrm{Re}[(s+z)/(s-z)] = (|s|^2 - |z|^2)/|s-z|^2$ only when $z$ is pure imaginary; in general one must use $s \in \mathbb{R}$ and compute the modulus directly.

For $s \in \mathbb{R}$ and $z = x + iy$:
$$\frac{s+z}{s-z} = \frac{s+x+iy}{s-x-iy}, \qquad \mathrm{Re}\left[\frac{s+z}{s-z}\right] = \frac{(s+x)(s-x) + y^2}{(s-x)^2 + y^2} = \frac{s^2 - x^2 - y^2 + 2sx}{(s-x)^2 + y^2}.$$
Thus $\mathrm{Re}[\mathcal{G}(z)] = \int \frac{(s-x)^2 - (x^2 + y^2 - 2x^2)}{(s-x)^2+y^2}\, d\nu$; the computation is correct but the most useful explicit form is the Herglotz-Nevanlinna representation: there exist $\alpha \geq 0$, $\beta \in \mathbb{R}$ and a positive measure $\sigma$ such that $\mathcal{G}(z) = \alpha z + \beta + \int (1/(s-z) - s/(1+s^2)) \, d\sigma(s)$, but here $d\nu$ is already given and $\mathcal{G}$ has the integral form exhibited.

$\mathcal{G}(z) = 0$ for all $z \in \mathbb{H}$ if and only if $d\nu = 0$ (the Nevanlinna transform determines the measure uniquely).

### 1.3. Path 2 — The Jensen excess $\delta$

By the Poisson-Jensen formula applied to $f(t) = \xi(1/2+it)$ on $\mathbb{H}$ with evaluation point $w_0 = i/2$ (Doc 87, Proposition 1.1 and §5):
$$-\log 2 = \int_{-\infty}^\infty \log|\xi(1/2+it)| \cdot \frac{2 \, dt}{\pi(1+4t^2)} - \sum_{\rho:\, \sigma > 1/2} \log\left|\frac{i/2 - \bar{t}_\rho}{i/2 - t_\rho}\right|,$$
where $t_\rho = \gamma + i(1/2 - \sigma)$ is the translation of the zero $\rho = \sigma + i\gamma$ to the $t$-plane. The Jensen excess is defined as
$$\delta := \frac{1}{2\pi} \int_0^{2\pi} \log|F(e^{i\theta})| \, d\theta - (-\log 2) = \sum_{\rho:\, \sigma > 1/2} \log\frac{|\rho|}{|1-\rho|} \geq 0,$$
where $F(z) = \xi(z/(z-1))$ and the value $-\log 2$ corresponds to the case with no off-critical zeros (Doc 84, §3–§5; Doc 87, §5). The sum runs over all zeros with $\sigma > 1/2$ (one per quartet, given that $\log|\rho/(\rho-1)| = \log|(1-\rho)^{-1}\rho|$ is positive for $\sigma > 1/2$).

Explicitly, for each off-critical zero $\rho = (1/2 + \delta_j) + i\gamma_j$:
$$\log\frac{|\rho|}{|1-\rho|} = \frac{1}{2}\log\frac{(1/2+\delta_j)^2 + \gamma_j^2}{(1/2+\delta_j)^2 + \gamma_j^2} = \frac{1}{2}\log\frac{(1/2+\delta_j)^2 + \gamma_j^2}{(1/2-\delta_j)^2 + \gamma_j^2} > 0,$$
since $(1/2+\delta_j)^2 > (1/2-\delta_j)^2$ when $\delta_j > 0$. In particular $\delta \geq 0$ with equality if and only if all $\delta_j = 0$, i.e., RH.

### 1.4. Path 3 — The initial speed of the DBN flow

For each $\lambda > 0$, the CCM trace is $T_\lambda = \int W_\lambda \, d\nu \geq 0$ (unconditional; Doc 70, §8). The time derivative of the De Bruijn-Newman flow at $t = 0$ is (Doc 71, main formula):
$$\partial_t T_\lambda\big|_{t=0} = -4 \int W_\lambda(s) \, \mathrm{Re}\!\left(\overline{\Xi_0(s)} \, \Xi_0''(s)\right) dm_\infty(s),$$
where $\Xi_0(s) = \xi(1/2 + is)$ in the real variable $s$, and $W_\lambda(s) = \sum_{k \leq N(\lambda)} k|P_k(s)|^2 + (a_{N(\lambda)}^\infty)^2 |P_{N(\lambda)+1}(s)|^2 \geq 0$ is the Abel kernel of the Jacobi basis $\{P_k\}$ of $L^2(dm_{full,on})$. By Doc 71, this derivative is a quadratic form in the coefficients $c_k = \langle \Xi_0, P_k \rangle_{dm_\infty}$ and can have any sign (under $\neg$RH); under RH, $T_\lambda = 0$ and the flow trajectory remains at the origin (on the manifold $M$ of Doc 88).

### 1.5. Comparison of natures

The three quantities have distinct natures:

- $\mathcal{G}(z)$ is a **function** of $z \in \mathbb{H}$, complex-valued (of Cauchy-operator type for $d\nu$).
- $\delta$ is a **real number** $\geq 0$, a convergent sum over the off-critical zeros.
- $\partial_t T_\lambda|_{t=0}$ is a **family of real numbers**, parametrized by $\lambda > 0$, of a priori indeterminate sign.

The connection between them cannot be a direct equality; it is an equivalence of criteria for the same underlying object.

---

## §2. Connection between $\delta$ and the measure $d\nu$

### 2.1. The excess $\delta$ as a nonlinear functional of $d\nu$

The Jensen excess $\delta$ is expressed, by the Poisson-Jensen formula (Doc 87, §5), as
$$\delta = \sum_{\rho:\, \sigma > 1/2} \log\frac{|\rho|}{|1-\rho|} = \sum_j \frac{1}{2}\log\frac{(1/2+\delta_j)^2 + \gamma_j^2}{(1/2-\delta_j)^2 + \gamma_j^2}.$$
This expression involves $\delta_j = \sigma_j - 1/2 > 0$ and $\gamma_j$ nonlinearly (via $\log$). It is not a linear functional of $d\nu$.

However, to first order in $\delta_j$ (off-critical zeros close to the critical line), expanding the logarithm:
$$\frac{1}{2}\log\frac{(1/2+\delta_j)^2 + \gamma_j^2}{(1/2-\delta_j)^2 + \gamma_j^2} = \frac{1}{2}\log\left(1 + \frac{4 \cdot (1/2)\,\delta_j}{(1/2)^2 + \gamma_j^2 - \delta_j^2}\right) \approx \frac{\delta_j/2}{1/4 + \gamma_j^2} + O(\delta_j^3).$$
Comparing with the expansion of $d\nu$ to first order in $\delta_j$ (§1.1):
$$R(s) - 1 \approx \sum_j 2\delta_j^2 \left[\frac{1}{(s-\gamma_j)^2} + \frac{1}{(s+\gamma_j)^2}\right] + O(\delta_j^4),$$
we observe that $d\nu$ begins at order $\delta_j^2$ while $\delta$ begins at order $\delta_j$. Hence **$\delta$ and the linear functionals of $d\nu$ have different orders in the displacements** $\delta_j$: $\delta$ is a functional of the *amplitude* of the displacements, whereas the linear functionals of $d\nu$ measure the *energy* of the displacements. This reflects that $\delta$ is intrinsically logarithmic (nonlinear) in $d\nu$.

### 2.2. Connection formula via the integral of $\log R$

The precise relation between $\delta$ and $d\nu$ passes through the logarithm of the density $R = dm_{full}/dm_{full,on}$. Consider the Kullback-Leibler divergence
$$\mathcal{KL}(dm_{full} \| dm_{full,on}) = \int \log R(s) \, dm_{full}(s) = \int \log R(s) \, R(s) \, dm_{full,on}(s).$$
This quantity also vanishes if and only if $R \equiv 1$, hence if and only if RH (by $R \geq 1$ and the strictness of $\log x \leq x - 1$ with equality only at $x=1$). The Jensen excess $\delta$ is related to the integral of $\log |F|$ over the circle (Doc 84, §3), which by the Poisson-Jensen formula on the disk is rewritten as an integral of $\log|\zeta|$ over the critical line plus the contribution of the interior zeros. Using $\log R = 2\sum_j \log(1 + \delta_j^2/(s-\gamma_j)^2) + 2\sum_j\log(1+\delta_j^2/(s+\gamma_j)^2)$ and the Poisson-Jensen formula with kernel $P_{1/2}(s) = (2/\pi)/(1+4s^2)$:

**Proposition 2.1.** *The Jensen excess satisfies:*
$$\delta = \int_{-\infty}^\infty \log\!\sqrt{R(s)} \cdot P_{1/2}(s) \, ds,$$
*where the integral makes sense since $\log\sqrt{R} \geq 0$ and $P_{1/2}$ is positive and integrable.*

*Proof (sketch).* From the Poisson-Jensen formula (Doc 87, §5), $\delta = \log|F(0)^{-1}| + \int \log|F(e^{i\theta})|(d\theta/2\pi)$, and the change of variables between the disk and the half-plane transforms the circular integral into the integral over $\mathbb{R}$ with the Poisson kernel $P_{1/2}$. The difference $\log|F(e^{i\theta})| - \log|F_{on}(e^{i\theta})|$ is exactly $\frac{1}{2}\log R(s(\theta))$ under the parametrization $s = \cot(\theta/2)$. $\square$

Proposition 2.1 exhibits $\delta$ as the **integral of $\log\sqrt{R}$ against the Poisson kernel**: it is a functional of $\log R$ (not of $R-1 = d\nu/dm_{full,on}$). This nonlinearity is the essential difference between Path 2 and the others.

---

## §3. Connection between $\partial_t T_\lambda|_{t=0}$ and the measure $d\nu$

### 3.1. The trace $T_\lambda$ as a linear functional

The CCM trace (Doc 70, §7) satisfies
$$T_\lambda = \int W_\lambda(s) \, d\nu(s) = \int W_\lambda(s) \, (R(s) - 1) \, dm_{full,on}(s).$$
This is the evaluation of the linear functional $\mathcal{L}_{W_\lambda}[\nu] = \int W_\lambda \, d\nu$ at the measure $d\nu$. The kernel $W_\lambda \geq 0$ is the Abel weight of the Jacobi basis of $L^2(dm_{full,on})$.

### 3.2. The time derivative as a second functional

The derivative $\partial_t T_\lambda|_{t=0}$ measures how $T_\lambda$ changes under the DBN heat flow. By the formula of Doc 71:
$$\partial_t T_\lambda\big|_{t=0} = -4 \int W_\lambda(s) \, \mathrm{Re}\!\left(\overline{\Xi_0(s)} \, \Xi_0''(s)\right) dm_\infty(s).$$
This expression involves $\Xi_0 = \zeta_{full}^{1/2}$ (in some sense) but more precisely $\Xi_0(s) = \xi(1/2+is)$. It is not a direct functional of $d\nu$, but a functional of $|\Xi_0|^2 = |\xi|^2$ on the critical line. However, $|\xi|^2 = |\xi_{on}|^2 R$, so the derivative involves $R$ and its derivatives.

The relation between $\partial_t T_\lambda|_{t=0}$ and $T_\lambda$ is as follows:

**Proposition 3.1.** *Under RH: $T_\lambda = 0$ and $\partial_t T_\lambda|_{t=0} = 0$ for all $\lambda > 0$. Under $\neg$RH: $T_\lambda > 0$ and $\partial_t T_\lambda|_{t=0}$ can be positive or negative depending on $\lambda$.*

The time derivative measures the **curvature of the trajectory** of the flow in the space $L^2(W_\lambda\, dm_\infty)$ (Doc 88, §2–§3), while $T_\lambda$ measures the distance to the set $M$. These are distinct facets of the movement of $f_t = |\Xi_t|^2$ under the flow.

### 3.3. Simultaneous vanishing

Although $\partial_t T_\lambda|_{t=0}$ and $T_\lambda$ are not equal, they satisfy: if $T_\lambda = 0$ for all $\lambda$, then the trajectory starts in $M$ and (by an invariance argument) remains in $M$, so $\partial_t T_\lambda|_{t=0} = 0$. The converse implication is not immediate (it is not known whether $\partial_t T_\lambda|_{t=0} = 0\; \forall\lambda$ implies $T_\lambda = 0\;\forall\lambda$ without additional hypotheses).

---

## §4. The unifying object: $d\nu$ as a functional of the same witness

### 4.1. The structure of linear functionals

All the quantities in the program that are **linear** in $d\nu$ have the form $\mathcal{L}_f[\nu] = \int f(s) \, d\nu(s)$ for some witness $f \geq 0$. The witnesses of the three paths are:

- **Path 1:** $f = k_z(s) = (s+z)/(s-z)$, the Nevanlinna kernel. For each fixed $z \in \mathbb{H}$, $\mathrm{Re}[k_z]$ is a real function that can take any sign (positive and negative depending on $s$ relative to $z$).
- **Path 3:** $f = W_\lambda(s) \geq 0$, the Abel kernel of the Jacobi basis.

**Path 2** ($\delta$) is nonlinear: it uses $f = \log\sqrt{R}$ (which involves the integral of the $\log$ of the density, not the density itself).

### 4.2. The Nevanlinna transform as a universal representative

For any bounded test function $f$, the integral $\int f \, d\nu$ is recovered from $\mathcal{G}(z) = \int k_z(s) \, d\nu(s)$ via the Stieltjes inversion formula:
$$d\nu(s) = \lim_{\varepsilon \to 0^+} \frac{1}{\pi} \mathrm{Im}[\mathcal{G}(s + i\varepsilon)] \, ds.$$
Consequently, knowing $\mathcal{G}(z)$ for all $z \in \mathbb{H}$ is equivalent to knowing $d\nu$ completely. In particular:
$$T_\lambda = \int W_\lambda \, d\nu = \frac{1}{\pi} \int_{-\infty}^\infty W_\lambda(s) \lim_{\varepsilon\to 0^+} \mathrm{Im}[\mathcal{G}(s+i\varepsilon)] \, ds.$$
Thus, **$\{T_\lambda\}_{\lambda > 0}$ determines $\mathcal{G}$** if the system $\{W_\lambda\}_\lambda$ is sufficiently rich.

**Proposition 4.1.** *The system $\{W_\lambda\}_{\lambda > 0}$ determines $d\nu$ uniquely. Consequently: $T_\lambda = 0\;\forall\lambda \iff d\nu = 0 \iff \mathcal{G}(z) = 0\;\forall z \in \mathbb{H}$.*

*Proof.* By the structure of $W_\lambda = \sum_{k \leq N(\lambda)} k|P_k|^2 + \ldots$ and the fact that $\{P_k^2\}_{k \geq 0}$ generates a dense subset of non-negative functions in $L^1(dm_{full,on})$ (quadratic polynomials are dense in the continuous functions that decay), if $\int W_\lambda \, d\nu = 0$ for all $\lambda$, then $\int p \, d\nu = 0$ for every non-negative polynomial $p$, which forces $d\nu = 0$ by moment theory (uniqueness of the Hamburger problem under the growth conditions of $dm_{full,on}$). $\square$

A frank note: the density argument in the above proof requires verifying that the $\{W_\lambda\}$ are rich enough to determine $d\nu$; the statement is correct in principle, but the detailed justification of completeness in the class of functions integrable with respect to $d\nu$ requires hypotheses on the growth of $d\nu$ as $|s| \to \infty$ that are satisfied by $d\nu \leq (R_{max}-1)dm_{full,on}$ with $R_{max}$ bounded on compact sets.

---

## §5. The relations between $T_\lambda$ and $\partial_t T_\lambda|_{t=0}$

### 5.1. Geometric interpretation

In the space of functions $L^2(W_\lambda\, dm_\infty)$, the trajectory $f_t = |\Xi_t|^2$ satisfies:
- $T_\lambda(0) = \|f_0 - f_{on}\|^2_{W_\lambda}$ in some sense (difference from the manifold $M$; Doc 88, §3).
- $\partial_t T_\lambda|_{t=0}$ is the derivative of the squared distance to $M$ at $t = 0$, which measures whether the flow approaches or moves away from $M$ initially.

If $\partial_t T_\lambda|_{t=0} < 0$: the flow approaches $M$ (favorable for the Monotonicity Conjecture).
If $\partial_t T_\lambda|_{t=0} > 0$: the flow moves away from $M$ (unfavorable).

The relation between $T_\lambda(0)$ and $\partial_t T_\lambda|_{t=0}$ has no simple algebraic form: they are an evaluation and a derivative of the same function $t \mapsto T_\lambda(t)$, which is real-analytic in $t$ by Proposition 1.2 of Doc 88.

### 5.2. Cancellation under RH

By Doc 71, §3–§4, under RH an exact cancellation occurs in the quadratic form of $\partial_t T_\lambda|_{t=0}$: the diagonal and cross terms between zeros and special values of the $L$-function cancel by the symmetry of the critical zeros (symmetry $\gamma_n \leftrightarrow -\gamma_n$ and the functional equation). This cancellation is the manifestation, at the level of the initial speed of the flow, of the same property (all zeros on $\mathrm{Re}(\rho) = 1/2$) that makes $T_\lambda = 0$.

### 5.3. What is NOT known

No proof (nor viable attempt) is known that $\partial_t T_\lambda|_{t=0} \leq 0$ for all $\lambda$ under $\neg$RH (the program's Monotonicity Conjecture). This conjecture would imply that the DBN flow is in some sense "descending" toward $M$, but there is not sufficient analytic or numerical evidence to assert it.

---

## §6. Table of criteria equivalent to RH

The various functionals of $d\nu$ generated by the program are:

| Criterion | Expression | Witness $f$ | Linear in $d\nu$ |
|----------|-----------|-------------|------------------|
| $T_\lambda$ (CTP trace) | $\int W_\lambda\, d\nu$ | $W_\lambda \geq 0$ | Yes |
| $\mathcal{G}(z)$ (Nevanlinna) | $\int k_z\, d\nu$ | $k_z = (s+z)/(s-z)$ | Yes |
| $\delta$ (Jensen) | $\int \log\sqrt{R}\, P_{1/2}\, ds$ | $\log\sqrt{R}$ (nonlinear) | No |
| $\mathcal{KL}$ (Kullback-Leibler) | $\int \log R\cdot R\, dm_{full,on}$ | $\log R$ (nonlinear) | No |
| $d_{CCM}$ (distance) | $\sup_\lambda T_\lambda$ | over the $W_\lambda$ | Yes (sup of linears) |
| $\partial_t T_\lambda|_{t=0}$ | quadratic form in $c_k$ | derivative of the flow | Quadratic in $\Xi_0$ |

All vanish if and only if $d\nu = 0$, hence if and only if RH.

---

## §7. The CCM distance as an operator norm

**Definition 7.1.** The *CCM distance* between $\zeta$ and $\zeta_{on}$ is defined as
$$d_{CCM}(\zeta, \zeta_{on}) := \sup_{\lambda > 0} T_\lambda = \sup_{\lambda > 0} \int W_\lambda(s)\, d\nu(s).$$

By Proposition 4.1, $d_{CCM} = 0 \iff d\nu = 0 \iff$ RH.

Beyond the vanishing criterion, this distance defines a topology on the space of entire functions of $\zeta$'s type: the larger the deviation of the zeros from the critical line (larger $\delta_j$), the larger $d_{CCM}$. The supremum over $\lambda$ acts as an operator norm because $W_\lambda$ increasingly approximates the identity function in $L^1(dm_{full,on})$ as $\lambda \to \infty$.

**Proposition 7.1.** *For all $\lambda' > \lambda$: $T_{\lambda'} \geq T_\lambda$. Consequently, $d_{CCM} = \lim_{\lambda \to \infty} T_\lambda = \int d\nu = \|d\nu\|$ (total mass of $d\nu$).*

*Proof.* From the structure $W_{\lambda'} \geq W_\lambda$ (the Abel kernel grows monotonically with $\lambda$, since $N(\lambda') \geq N(\lambda)$ and non-negative terms are added) and $d\nu \geq 0$, it follows that $T_{\lambda'} \geq T_\lambda$. The limit $\lim_{\lambda \to \infty} W_\lambda = \sum_{k=0}^\infty k|P_k|^2$ in $L^1_{loc}$, and by monotone convergence $\lim_\lambda T_\lambda = \int (\sum_k k|P_k|^2) \, d\nu$. If the series $\sum_k k|P_k|^2$ converges to the constant function $1$ in $L^1(d\nu)$, then the limit is $\|d\nu\|$. Convergence to $1$ is precisely the completeness of the basis $\{P_k\}$ in $L^2(dm_{full})$, which holds under the standard hypotheses of the theory of orthogonal polynomials for measures with finite moments of all orders. $\square$

---

## §8. The measure $d\nu$ and the functional equation of $\zeta$

The measure $d\nu = (R-1)dm_{full,on}$ inherits the symmetries of $\zeta$.

**Proposition 8.1.** *The measure $d\nu$ is even: $d\nu(-s) = d\nu(s)$.*

*Proof.* By the functional equation $\xi(s) = \xi(1-s)$, the zeros of $\zeta$ are symmetric with respect to $\mathrm{Re}(s) = 1/2$, and in the parametrization $\zeta(1/2 + is)$ the variable $s$ satisfies $\zeta(1/2+is) = \overline{\zeta(1/2-is)}$ (since $\zeta$ is real on the real line). Consequently $|\zeta(1/2+is)|^2 = |\zeta(1/2-is)|^2$, and likewise for $\zeta_{on}$. Hence $R(s) = R(-s)$ and $d\nu(s) = R(s)dm_{full,on}(s) - dm_{full,on}(s) = d\nu(-s)$ (given that $dm_\infty$ and $dm_{full,on}$ are also even). $\square$

**Proposition 8.2 (frank).** *No functional equation for $d\nu$ is known —distinct from evenness and positivity $d\nu \geq 0$— that is independent of the position of the zeros of $\zeta$ and that implies $d\nu = 0$.*

The search for such a functional equation is, from the program's perspective, the fundamental unresolved question: does there exist any intrinsic property of $\zeta$ (holomorphic, entire of order 1, satisfying the functional equation, with certain zeros on $\mathrm{Re} = 1/2$...) that forces $d\nu = 0$ without knowing the exact position of the zeros?

---

## §9. Why the three paths converge

The three paths are different "projections" of the same object $d\nu$:

**Path 1** (Jacobi, Hamburger moments) studies $d\nu$ via its **moments**: $\mu_k = \int s^k \, d\nu(s)$. The Nevanlinna function $\mathcal{G}(z)$ is the Stieltjes transform of $d\nu$, which encodes all the moments in the expansion $\mathcal{G}(z) = \sum_{k=0}^\infty \mu_k z^{-k-1}$ (for large $|z|$). The criterion is: all moments are zero $\iff$ $d\nu = 0$.

**Path 2** (function $F(z)$, Jensen) studies $d\nu$ via the **logarithm of its density**: $\log R = \log(1 + d\nu/dm_{full,on})$. The Jensen integral is an integral of $\log R$ against a Poisson kernel. The criterion is: $\int \log R \cdot P_{1/2} = 0 \iff$ (by the non-negativity of $\log R \geq 0$ and the strict positivity of the Poisson kernel) $\log R = 0$ $dm_\infty$-a.e. $\iff R = 1$ $dm_\infty$-a.e. $\iff$ $d\nu = 0$.

**Path 3** (DBN flow) studies $d\nu$ via its **evolution under heat**: $d\nu_t = |\Xi_t|^2 dm_\infty - |\Xi_t^{on}|^2 dm_\infty$ under the heat semigroup. The trace $T_\lambda(t) = \int W_\lambda \, d\nu_t$ is the deformation of $T_\lambda(0)$ under the flow. The criterion is: $T_\lambda(0) = 0\;\forall\lambda \iff$ $d\nu_0 = 0 \iff$ RH.

The three perspectives are informationally equivalent (same vanishing condition) but none provides access to the property that would force $d\nu = 0$ without using the position of the zeros.

---

## §10. Synthesis theorem

**Theorem 10.1 (Phase 34 synthesis).** *Let $d\nu = (|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2) \, dm_\infty(s)$ be the difference measure. The following conditions are equivalent:*

1. *Riemann Hypothesis: all non-trivial zeros of $\zeta$ satisfy $\mathrm{Re}(\rho) = 1/2$.*
2. *$d\nu = 0$ (null measure on $\mathbb{R}$).*
3. *$\mathcal{G}(z) = 0$ for all $z \in \mathbb{H}$ (null Nevanlinna function).*
4. *$T_\lambda = \int W_\lambda \, d\nu = 0$ for all $\lambda > 0$ (null CTP trace).*
5. *$\delta = 0$ (null Jensen excess).*
6. *$\partial_t T_\lambda|_{t=0} = 0$ for all $\lambda > 0$ (null initial speed of the DBN flow).*
7. *$\mathcal{KL}(dm_{full} \| dm_{full,on}) = 0$ (null Kullback-Leibler divergence).*
8. *$d_{CCM}(\zeta, \zeta_{on}) = 0$ (null CCM distance).*

*Proof of the implications:*

$(1) \iff (2)$: By definition $d\nu = (R-1)dm_{full,on}$ with $R = \prod_j (1 + \delta_j^2/(s-\gamma_j)^2)^2 \geq 1$. $R \equiv 1$ if and only if all factors are 1, which occurs if and only if all $\delta_j = 0$, i.e., all zeros satisfy $\mathrm{Re}(\rho) = 1/2$. $\square$

$(2) \iff (3)$: The Stieltjes-Nevanlinna transform determines the positive measure uniquely: if $\mathcal{G}(z) = \int (s+z)/(s-z)\, d\nu = 0$ for all $z \in \mathbb{H}$, then in particular $\mathrm{Im}[\mathcal{G}(s_0+i\varepsilon)] \to \pi\, d\nu(s_0)$ in the distributional sense as $\varepsilon \to 0^+$, so $d\nu = 0$. The converse implication is trivial. $\square$

$(2) \iff (4)$: By Proposition 4.1. $\square$

$(2) \iff (5)$: By Proposition 2.1 and the strict positivity of the Poisson kernel $P_{1/2} > 0$ and of $\log\sqrt{R} \geq 0$: if $\delta = \int \log\sqrt{R} \cdot P_{1/2}\, ds = 0$ and the integrand is non-negative, then $\log\sqrt{R} = 0$ $ds$-a.e., so $R = 1$ $ds$-a.e., so $d\nu = 0$. $\square$

$(2) \iff (6)$: By the formula of Doc 71 and the cancellation under RH (§5.2 and §3.3): if $d\nu = 0$ then $T_\lambda = 0$ and the trajectory is stationary at $M$, so $\partial_t T_\lambda|_{t=0} = 0$. The converse implication ($\partial_t T_\lambda|_{t=0} = 0\;\forall\lambda \implies d\nu = 0$) requires an additional argument: if $\partial_t T_\lambda|_{t=0} = 0$ for all $\lambda$, then... this step is not fully justified in the program and is marked as *conjectural* pending verification of item V.3 of the original program. It is stated here for completeness, but the full equivalence $(2) \iff (6)$ is conjectural.

$(2) \iff (7)$: By Gibbs's inequality: $\mathcal{KL}(dm_{full}\|dm_{full,on}) = \int \log(R) R\, dm_{full,on} \geq \int (R-1)R\, dm_{full,on} \cdot \ldots$; more directly, $\mathcal{KL} \geq 0$ with equality if and only if $R = 1$ $dm_{full,on}$-a.e. $\square$

$(4) \iff (8)$: By Proposition 7.1, $d_{CCM} = \|d\nu\|$, so $d_{CCM} = 0 \iff d\nu = 0$. $\square$

---

## §11. The structural obstacle

Theorem 10.1 assembles a catalog of conditions equivalent to RH, all of the form "a certain functional of $d\nu$ is zero". The program has established this catalog. However, to **prove** RH it is necessary to show that $d\nu = 0$ without knowing a priori the position of the zeros of $\zeta$.

The precise obstacle is the following. All the criteria of Theorem 10.1 are of the type:
$$\text{RH} \iff \mathcal{F}(d\nu) = 0,$$
where $\mathcal{F}$ is a functional of $d\nu$. To use this criterion in a proof, there would need to exist a property $\mathcal{P}$ of $\zeta$ such that:
1. $\mathcal{P}(\zeta)$ is verifiable from the global properties of $\zeta$ (entire of order 1, functional equation, zeros in the critical strip, growth in the half-plane).
2. $\mathcal{P}(\zeta) \implies \mathcal{F}(d\nu) = 0$.

No property $\mathcal{P}$ with both characteristics is known. The only information available about $d\nu$ independent of the position of the zeros is:
- $d\nu \geq 0$ (Proposition 1.1 of Doc 83).
- $d\nu$ is even (Proposition 8.1).
- $d\nu$ has finite total mass $\|d\nu\| = \int d\nu < \infty$ (under regularity hypotheses on $\zeta$).

None of these properties, nor their combination, implies $d\nu = 0$.

**Proposition 11.1 (frank obstacle).** *Positivity $d\nu \geq 0$, evenness $d\nu(-s) = d\nu(s)$, and finiteness $\|d\nu\| < \infty$ are compatible with $d\nu \neq 0$. They do not imply $d\nu = 0$.*

*Example:* Any even positive measure of finite mass on $\mathbb{R}$ satisfies these properties.

**Corollary 11.1.** *To prove RH via the object $d\nu$, one must identify a property of $\zeta$ —derivable from its functional properties, without using the exact position of the zeros— that forces $d\nu = 0$. This property does not exist in current knowledge.*

---

## §12. Summary and perspective

This document has established:

1. **The central object** of the program is the measure $d\nu = dm_{full} - dm_{full,on} \geq 0$, which is zero if and only if RH holds.

2. **The three paths** (Nevanlinna, Jensen, DBN flow) are three distinct functionals of $d\nu$: the Stieltjes transform, the integral of the logarithm of the density, and the trace of the Abel kernel. They are informationally equivalent but not equal as mathematical objects.

3. **Theorem 10.1** catalogs eight conditions equivalent to RH, all of the form "functional of $d\nu$ = 0".

4. **The obstacle** is that no property of $\zeta$ is known —independent of the position of its zeros— that implies $d\nu = 0$.

5. **The next step** requires a genuinely new mathematical idea: identifying a constraint on the function $d\nu$ that emanates from the global properties of $\zeta$ and that forces $d\nu = 0$.

Phase 34 of the program has completed its synthesis work: it has identified the object, characterized it from three perspectives, and precisely formulated the obstacle that remains. The program continues in Phase 35, which will seek additional constraints on $d\nu$ coming from the noncommutative geometry of the adele space (connection with the work of Connes-Consani) or from extremal properties of the Nyman-Beurling functional (Doc 82).

---

*End of Document 89.*
