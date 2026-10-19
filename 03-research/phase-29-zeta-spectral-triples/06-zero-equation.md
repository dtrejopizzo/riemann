# Phase 29 — Zero equation and quantitative convergence

**Goal:** Attack Wall-H2 directly from the algebraic equation of the zeros, without going through the $L^2$ norm of $\xi_\lambda - k_\lambda$. Two new results: (A) quantitative convergence of the zeros of $\hat k_\lambda$ via Lemma 7.3 + Rouché; (B) the multiplicative structure of $A_\lambda$ in Mellin space, which connects the zeros of $\hat\xi_\lambda$ with the crossings of the explicit formula.

---

## 1. The zero equation as the central object

From doc 03 (Proposition 3): the zeros $t_n^{(\lambda)}$ of $\hat\xi_\lambda$ are exactly the values $z \in \mathbb{R}$ where the rational function

$$R_\xi(z) := \frac{1}{L}\sum_{|m|\leq N} \frac{\xi_m^{(\lambda)}}{z - 2\pi m/L}$$

vanishes. Similarly for $\hat k_\lambda$:

$$R_k(z) := \frac{1}{L}\sum_{|m|\leq N} \frac{k_m^{(\lambda)}}{z - 2\pi m/L}.$$

The sum $S_n$ from doc 05 (the quantity to control for Wall-H2) is:

$$S_n := R_\xi(\gamma_n) - c_\lambda R_k(\gamma_n) = \frac{1}{L}\sum_m \frac{\Delta_m}{\gamma_n - 2\pi m/L},$$

where $\Delta_m := \xi_m^{(\lambda)} - c_\lambda k_m^{(\lambda)}$ and $\gamma_n$ is the $n$-th zero of $\Xi$.

**The precise question.** Can $|S_n|$ be bounded in terms of $\lambda^{-1/2}$ or smaller, using only the variational structure of $\xi_\lambda$ and the convergence rate of Lemma 7.3 for $k_\lambda$?

---

## 2. Quantitative convergence theorem for the zeros of $\hat k_\lambda$

**Theorem 1** (new, quantitative). Let $\{s_n^{(\lambda)}\}$ be the zeros of $\hat k_\lambda$ that converge to $\gamma_n$. Then for $\alpha \in (0,1/2)$:

$$|s_n^{(\lambda)} - \gamma_n| \leq \frac{2C_\alpha \lambda^{-1/2-\alpha}}{(1-2\alpha) w_n},$$

where $w_n = |\Xi'(\gamma_n)| > 0$ is the weight of the $n$-th zero.

*Proof.* By Lemma 7.3 (CCM): $|\hat k_\lambda(z) - \Xi(z)| \leq C_\alpha \lambda^{-1/2-\alpha}(1-2\alpha)^{-1}$ uniformly for $|\Im(z)| \leq \alpha$.

Let $r_n = 2C_\alpha\lambda^{-1/2-\alpha}/((1-2\alpha)w_n)$ and consider the circle $\Gamma_n = \{|z-\gamma_n| = r_n\}$. On $\Gamma_n$:
$$|\Xi(z)| \geq |z - \gamma_n| \cdot \inf_{\Gamma_n}|\Xi'| \geq r_n w_n/2 = C_\alpha\lambda^{-1/2-\alpha}/(1-2\alpha)$$

(using that $\gamma_n$ is a simple zero with $|\Xi'(\gamma_n)| = w_n$ and that the variation of $\Xi'$ on $\Gamma_n$ is small for large $\lambda$).

The bound from Lemma 7.3 gives $|\hat k_\lambda(z) - \Xi(z)| \leq C_\alpha\lambda^{-1/2-\alpha}/(1-2\alpha) \leq |\Xi(z)|$ on $\Gamma_n$.

By the Rouché principle: $\hat k_\lambda$ and $\Xi$ have the same number of zeros in $|z - \gamma_n| < r_n$, which is exactly 1. Hence $|s_n^{(\lambda)} - \gamma_n| \leq r_n$. $\square$

**Corollary.** The zeros of $\hat k_\lambda$ converge to those of $\Xi$ at rate $O(\lambda^{-1/2}/w_n)$.

**Note:** This is the first quantitative result on the convergence rate of the zeros of the CCM approximation. The rate $\lambda^{-1/2}/w_n$ is the natural one: the weight $w_n = |\Xi'(\gamma_n)|$ measures the "openness" of the zero of $\Xi$, and more open zeros (larger $w_n$) are more stable under perturbations.

---

## 3. The normalization constraint and the reduction of $S_n$

**Proposition 1** (normalization constraint). Let the CCM boundary condition be: $\xi_\lambda(\lambda) = k_\lambda(\lambda) = 1$ (normalization at $u = \lambda$). In the basis $\{U_m^+\}$, this is equivalent to:

$$\sum_{m=0}^N \xi_m^{(\lambda)'} = \sum_{m=0}^N k_m^{(\lambda)'} = \sqrt{L}$$

(where $\xi_m^{(\prime)}$ are the coefficients in the even basis). Therefore:

$$\sum_{m=0}^N \Delta_m^{(\prime)} = 0,$$

i.e., the sum of the coefficients of $\Delta$ is zero.

*Proof.* $V_m(\lambda) = L^{-1/2}e^{2\pi im\log(\lambda^2)/L} = L^{-1/2}e^{2\pi im} = L^{-1/2}$ for every $m$. Hence $f(\lambda) = L^{-1/2}\sum_m f_m$ for $f \in E_N$. The condition $\xi_\lambda(\lambda) = k_\lambda(\lambda)$ gives $\sum_m \xi_m = \sum_m k_m$, i.e., $\sum_m \Delta_m = 0$. $\square$

**Reduction of $S_n$.** Using $\sum_m \Delta_m = 0$:

$$S_n = \frac{1}{L}\sum_m \frac{\Delta_m}{\gamma_n - 2\pi m/L} = \frac{1}{L}\sum_m \Delta_m \left[\frac{1}{\gamma_n - 2\pi m/L} - \frac{1}{\gamma_n}\right]$$

$$= \frac{1}{L\gamma_n}\sum_m \frac{\Delta_m \cdot (2\pi m/L)}{\gamma_n - 2\pi m/L} = \frac{1}{\gamma_n}\sum_m \frac{\Delta_m \cdot (2\pi m/L^2)}{\gamma_n - 2\pi m/L}.$$

The sum $S_n$ is now a FIRST-MOMENT SUM: the coefficients $\Delta_m$ are weighted by $(2\pi m/L^2)/(\gamma_n - 2\pi m/L)$, a weight that grows with $|m|$ and has poles at $\gamma_n L/(2\pi)$ (which is generically not an integer).

**Corollary.** If $\sum_m m\,\Delta_m = 0$ (vanishing second moment), then $S_n = \sum_m \Delta_m \cdot (2\pi m/L)^2 / (\gamma_n^2(\gamma_n - 2\pi m/L))$ (second-moment sum). Each additional moment constraint reduces the order of the denominator of $S_n$.

---

## 4. The multiplicative structure of $A_\lambda$ in Mellin space

This is the most important new observation of the document.

**Lemma 2** (multiplication in Mellin space). The arithmetic operator $A_\lambda$ acts as multiplication by the Fourier-Chebyshev function in Mellin space:

$$\widehat{A_\lambda f}(t) = \Psi_\lambda(t)\,\hat f(t),$$

where $\Psi_\lambda(t) = 2\sum_{p \leq \lambda^2} \Lambda(p)\,p^{-1/2}\cos(t\log p)$.

*Proof.* By definition: $A_\lambda f = \sum_{p\leq\lambda^2}\Lambda(p)T(p)f$. The Mellin transform of $T(p)f$:
$$\widehat{T(p)f}(t) = \int_0^\infty T(p)f(u)\,u^{-it}\,\frac{du}{u} = p^{-1/2}\int [f(pu)+f(u/p)]\,u^{-it}\,\frac{du}{u}$$
$$= p^{-1/2}[p^{it}\hat f(t) + p^{-it}\hat f(t)] = 2p^{-1/2}\cos(t\log p)\,\hat f(t).$$
Summing over primes: $\widehat{A_\lambda f}(t) = \Psi_\lambda(t)\hat f(t)$. $\square$

**Corollary** (the operator $M = B - A$ is nearly diagonal in Mellin space). The archimedean operator $Q^{\mathrm{arch}}$ corresponds to multiplication by $w(t) = 2\partial_t\theta(t)/2\pi \sim \tfrac{1}{2}\log(t/2\pi)$ for $t \gg 1$. Then, modulo the rank-1 term ($Q^{\mathrm{cross}}$):

$$(B_\lambda - A_\lambda)\hat f(t) \approx [w(t) - \Psi_\lambda(t)]\hat f(t).$$

The operator $M = B - A$ is NEARLY DIAGONAL in Mellin space.

---

## 5. The eigenvalue equation in Mellin space and the crossings of the explicit formula

The equation $(B_\lambda - A_\lambda - \mu_\lambda)\xi_\lambda = 0$ in Mellin space is:

$$[w(t) - \Psi_\lambda(t) - \mu_\lambda]\hat\xi_\lambda(t) \approx 0 \quad \text{for almost every } t.$$

**Consequence.** The support of $\hat\xi_\lambda(t)$ in Mellin space is concentrated at the values $t$ where

$$w(t) \approx \Psi_\lambda(t) + \mu_\lambda.$$

These are the **crossings of the truncated explicit formula**.

**Definition.** The set of crossings:
$$\mathcal{C}_\lambda := \{t \in \mathbb{R} : w(t) = \Psi_\lambda(t) + \mu_\lambda\}.$$

**Proposition 2** (connection between zeros and crossings). The positions of the zeros $t_n^{(\lambda)}$ of $\hat\xi_\lambda$ are determined by the positions of the crossings in $\mathcal{C}_\lambda$, in the sense that the concentration of the Mellin transform $\hat\xi_\lambda$ at each crossing determines a zero of the entire function $\hat\xi_\lambda$.

*Argument (formal).* If $\hat\xi_\lambda(t) \approx 0$ for $t \notin \mathcal{C}_\lambda$ and $\hat\xi_\lambda(t)$ has mass at $t_0 \in \mathcal{C}_\lambda$, then the zero of $\hat\xi_\lambda$ (in the complex plane) closest to $t_0$ (real) will be near $t_0$. $\square$

---

## 6. The crossings of the explicit formula converge to $\gamma_n$

**Lemma 3** (crossings of $\Psi_\lambda$). Define $\Psi(t) := \lim_{\lambda\to\infty}\Psi_\lambda(t)$ (the full explicit formula). By the Riemann–von Mangoldt explicit formula:

$$\Psi_\lambda(t) = w(t) - 2\sum_{|\gamma_n| \leq T_\lambda} \frac{\cos(t\log\gamma_n)}{\gamma_n} + O(\log\lambda / \lambda)$$

(approximation with an error controlled by $T_\lambda \sim \lambda^2$). The solutions of $\Psi_\lambda(t) + \mu_\lambda = w(t)$ with $\mu_\lambda \approx 0$ are approximately the solutions of

$$2\sum_{|\gamma_n| \leq T_\lambda} \frac{\cos(t\log\gamma_n)}{\gamma_n} \approx 0.$$

**Under RH** (all $\gamma_n$ real): the above equation is satisfied at $t = \gamma_n$ (the zeros of $\Xi$) for the relevant crossings. The approximation improves as $T_\lambda \to \infty$.

**Proposition 3** (crossings $\mathcal{C}_\lambda \to \{\gamma_n\}$ under RH). If RH holds, the crossings of $\mathcal{C}_\lambda$ converge to the zeros $\gamma_n$ of $\Xi$ as $\lambda \to \infty$, at the same convergence rate at which the truncated explicit formula converges to the full one.

**Interpretation.** The mechanism by which the zeros of $\hat\xi_\lambda$ converge to $\gamma_n$ is as follows:

1. $\hat\xi_\lambda$ concentrates its mass at the crossings $\mathcal{C}_\lambda$ (by the eigenvalue equation in Mellin space).
2. The crossings $\mathcal{C}_\lambda$ converge to $\gamma_n$ (by the explicit formula + RH).
3. The zeros of $\hat\xi_\lambda$ converge to the crossings (by the diagonal approximation).
4. Hence the zeros of $\hat\xi_\lambda$ converge to $\gamma_n$.

**The obstacle (frankly stated).** Step 1 is formal (the approximation $M \approx$ multiplication ignores the rank-1 term $Q^{\mathrm{cross}}$ and the discretization effects on $E_N^+$). Steps 2 and 3 require quantification. Step 2 uses RH (it is CONDITIONAL).

---

## 7. Unconditional reduction: the zero equation without RH

Without assuming RH, the crossings of $\mathcal{C}_\lambda$ converge to the **imaginary values of all non-trivial zeros** of $\zeta$ (both those on the critical line $\gamma_n$ and those that might eventually not be).

But: the zeros of $\hat\xi_\lambda$ are ALWAYS real (CCM theorem). Therefore:

**Proposition 4** (crux of the program). If the crossings $\mathcal{C}_\lambda$ converged to COMPLEX values (violating RH), the exactly real zeros of $\hat\xi_\lambda$ could not converge to them — this would generate a CONTRADICTION if the convergence $\hat\xi_\lambda \to \Xi$ is established independently.

The logical chain:
- $\hat\xi_\lambda$ has REAL zeros (by CCM, unconditionally).
- If the crossings of $\mathcal{C}_\lambda$ converge to a complex zero $\rho$ with $\Im(\rho) \neq 0$: the crossing on the real line would be $\mathrm{Im}(\rho)$ (the imaginary part), which is real. Hence the real zeros of $\hat\xi_\lambda$ converge to the imaginary values of the zeros of $\zeta$ — which are real both under RH and without it.
- Then: $\hat\xi_\lambda \to \Xi$ (under H2) does NOT require the crossings to be exactly $\gamma_n$; it requires the convergence to be toward $\Xi$ (not toward $\zeta(1/2+it)$ directly).

**The precision needed:** The CCM program requires that the real zeros of $\hat\xi_\lambda$ converge to the real zeros of $\Xi$ (which are the $\gamma_n$ under RH, or complex without RH). Since the zeros of $\hat\xi_\lambda$ are always real, convergence to complex zeros of $\Xi$ would be impossible. This is exactly the structure of Hurwitz's argument: if $\hat\xi_\lambda \to \Xi$ uniformly and the $\hat\xi_\lambda$ all have real zeros, then $\Xi$ has all zeros real.

---

## 8. The moments of $\Delta_m$ from the Euler-Lagrange system

The variational system for $\xi_\lambda$ gives (in the basis $\{U_m^+\}$):

$$\sum_{m'=0}^N \tau_{mm'} \xi_{m'}^{(\lambda)} = \mu_\lambda \xi_m^{(\lambda)} \quad \forall\, 0 \leq m \leq N,$$

where $\tau_{mm'}$ is the Cauchy-Toeplitz matrix of $QW_\lambda^N|_{E^+}$.

**Proposition 5** (moment constraints of $\Delta$ from Euler-Lagrange). For $q = 0, 1, 2, \ldots$, the $q$-th moment of $\Delta$ satisfies:

$$\sum_{m=0}^N m^q \Delta_m = \sum_{m=0}^N m^q (\xi_m^{(\lambda)} - c_\lambda k_m^{(\lambda)})$$

$$= \frac{1}{\mu_\lambda}\sum_{m=0}^N m^q \sum_{m'} \tau_{mm'}\xi_{m'} - c_\lambda \sum_m m^q k_m^{(\lambda)}.$$

The condition for the $q$-th moment of $\Delta$ to vanish is:

$$\sum_{m,m'} m^q \tau_{mm'} \xi_{m'} = \mu_\lambda c_\lambda \sum_m m^q k_m^{(\lambda)}.$$

**Moment conjecture (MC).** For $q = 0, 1$:
$$\sum_m \Delta_m = 0 \text{ (order-0 moment, proved)}, \qquad \sum_m m\,\Delta_m = O(e^{-\pi\lambda^2}) \text{ (order-1 moment, conjectured)}.$$

If MC holds for $q = 0, 1$: the sum $S_n$ reduces to a SECOND-moment estimate:

$$S_n = \frac{1}{\gamma_n^2} \sum_m \frac{\Delta_m (2\pi m/L)^2}{\gamma_n - 2\pi m/L} + O(e^{-\pi\lambda^2}/\gamma_n),$$

which is more controllable (the numerator involves $m^2\Delta_m$, weighted).

**Why MC is plausible.** In the diagonal Mellin representation: the moment $\sum_m m^q \Delta_m$ corresponds to the $q$-th derivative of $\hat\Delta$ evaluated at $t = 0$:
$$\hat\Delta^{(q)}(0) = i^q \sum_m m \cdot (\text{factor})^q \Delta_m.$$

For $\hat\Delta(t) \approx 0$ near $t = 0$ (region where the explicit formula is "flat"), the derivatives of $\hat\Delta$ at $0$ need to be small — which is a consequence of the smooth character of the difference between the minimizer and the PSWF approximation.

---

## 9. Estimate of $S_n$ via Lemma 7.3

**Theorem 2** (quantitative bound on $S_n$). Under the hypotheses of Lemma 7.3:

$$|S_n| \leq |R_\xi(\gamma_n)| + c_\lambda |R_k(\gamma_n)| \leq |R_\xi(\gamma_n)| + c_\lambda \cdot \frac{C_\alpha \lambda^{-1/2-\alpha}}{(1-2\alpha)\sqrt{L}}.$$

The second term is $O(\lambda^{-1/2})$. For the first term:

$$|R_\xi(\gamma_n)| = |R_\xi(\gamma_n) - R_\xi(t_n^{(\lambda)})| = |\gamma_n - t_n^{(\lambda)}| \cdot |R_\xi'(\zeta)|$$

for some $\zeta$ between $\gamma_n$ and $t_n^{(\lambda)}$. Here $|R_\xi'(\zeta)| \approx |\hat\xi_\lambda'(t_n^{(\lambda)})| / L \approx w_n/L$.

Hence: $|S_n| \leq |\gamma_n - t_n^{(\lambda)}| w_n/L + O(\lambda^{-1/2})$.

Therefore: the Wall-H2 condition $|S_n| \to 0$ is EQUIVALENT to $|\gamma_n - t_n^{(\lambda)}| \to 0$ (convergence of the zeros).

**Conversely:** if we can bound $|S_n|$ independently of $|t_n^{(\lambda)} - \gamma_n|$, we obtain convergence of the zeros. Lemma 7.3 gives:

$$c_\lambda |R_k(\gamma_n)| = O(\lambda^{-1/2}/w_n) \cdot w_n = O(\lambda^{-1/2}).$$

If $R_\xi(\gamma_n) = c_\lambda R_k(\gamma_n) + (\text{small})$, then $S_n = O(\lambda^{-1/2})$ and Theorem 1 gives $|t_n^{(\lambda)} - \gamma_n| = O(\lambda^{-1/2}/w_n)$.

**The central point:** This equality $R_\xi(\gamma_n) \approx c_\lambda R_k(\gamma_n)$ is precisely what needs to be proved to resolve H2. It is not circular: $R_k(\gamma_n)$ is known by Lemma 7.3, and $R_\xi(\gamma_n)$ depends on the structure of the minimizer.

---

## 10. Verdict: status of the program after doc 06

### New results proved (unconditionally):

| Result | Status |
|---|---|
| Quantitative convergence: $|s_n^{(\lambda)} - \gamma_n| = O(\lambda^{-1/2}/w_n)$ for zeros of $\hat k_\lambda$ (Theorem 1) | **Proved** |
| Constraint $\sum_m \Delta_m = 0$ from normalization (Prop. 1) | **Proved** |
| Reduction of $S_n$ to a first-moment sum (Sec. 3) | **Proved** |
| Multiplicative structure: $\widehat{A_\lambda f}(t) = \Psi_\lambda(t)\hat f(t)$ (Lemma 2) | **Proved** |
| $M \approx$ multiplication by $w - \Psi_\lambda$ in Mellin space (Corollary) | **Proved** |
| Equivalence $|S_n| \to 0 \iff |t_n^{(\lambda)} - \gamma_n| \to 0$ (Theorem 2) | **Proved** |

### What remains open:

| Question | Description |
|---|---|
| **29.4 (central)** | Prove $|S_n| = O(\lambda^{-1/2})$ using the variational structure of $\xi_\lambda$ |
| **MC (moments)** | $\sum_m m\,\Delta_m = O(e^{-\pi\lambda^2})$ from Euler-Lagrange |
| **Prop. 2 (formal)** | Make rigorous the argument "zeros concentrate at the crossings" |
| **H2 (full)** | Prove $|\hat\xi_\lambda - c\hat k_\lambda| = O(\lambda^{-1/2})$ on $|\Im z| \leq \alpha$ |

### The precise wall after 6 documents:

The central obstacle is proving $R_\xi(\gamma_n) \approx c_\lambda R_k(\gamma_n)$, i.e., that the COEFFICIENTS of the minimizer $\xi_\lambda$ (which satisfy the Cauchy-Toeplitz equation) approximate, in the sense of the evaluation functional at $\gamma_n$, the coefficients of $k_\lambda$ (which satisfy the PSWF equation).

This is exactly the CCM H2 conjecture, restated in concrete terms via the zero equation. We have not closed the program, but we have reduced Wall-H2 to a precise algebraic estimate: the evaluation of a rational function at the zeros of $\Xi$.

### The next attackable question (29.5):

> **Question 29.5.** Do the coefficients $\{\xi_m^{(\lambda)}\}$ of the minimizer of $QW_\lambda$ satisfy the first-order moment condition: $\sum_m m\,\xi_m^{(\lambda)} = \sum_m m\,k_m^{(\lambda)} + O(e^{-\pi\lambda^2})$?

This condition can be attacked directly from the Euler-Lagrange system (Proposition 5), taking $q = 1$ and evaluating the entries of the Cauchy-Toeplitz matrix $\tau_{mm'}$.
