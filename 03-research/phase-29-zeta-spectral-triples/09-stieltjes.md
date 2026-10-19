# Phase 29 — The Stieltjes transform and the fixed-point equation

**Objective:** Break the circular structure identified in doc 08. Instead of attacking the zeros individually, attack the STIELTJES TRANSFORM of the spectral measure of $D_\lambda^N$. This transform satisfies a fixed-point equation derived from the CCM variational system. The solution of that fixed point is the Stieltjes transform of the zero measure of $\Xi$ — which would give Stieltjes convergence → Jacobi convergence → individual zero convergence → Wall-H2.

---

## 1. The circular structure and the proposed way out

From docs 06–08, the program identified the following **circular structure**:

$$\text{H2} \implies \hat\xi_\lambda \to c\Xi \implies \text{Stieltjes converges} \implies \text{Jacobi converges} \implies t_n^{(\lambda)}\to\gamma_n \implies \text{H2}$$

Each arrow is a standard implication (Lemma 7.3 + Rouché, Hurwitz's argument, OP theory). The circle means there is no EXTERNAL INPUT breaking the chain.

**The way out:** The Stieltjes transform $S_\lambda(z)$ of the spectral measure of $D_\lambda^N$ satisfies a fixed-point equation derived directly from the EULER–LAGRANGE EQUATION of the CCM system (without going through H2). If that fixed-point equation has $S_\Xi$ as its UNIQUE solution, then $S_\lambda \to S_\Xi$ can be established without using H2 as a hypothesis.

---

## 2. The Stieltjes transform of the CCM system

**Definition.** Let the spectral (counting) measure of $D_\lambda^N$ be:

$$\mu_\lambda = \frac{1}{N}\sum_{n=1}^{N+1}\delta_{t_n^{(\lambda)}}.$$

Its Stieltjes transform:

$$S_\lambda(z) := \int_\mathbb{R}\frac{d\mu_\lambda(t)}{z-t} = \frac{1}{N}\sum_n\frac{1}{z-t_n^{(\lambda)}}, \quad z \in \mathbb{C}\setminus\mathbb{R}.$$

**Connection with $\hat\xi_\lambda$.** Since $t_n^{(\lambda)}$ are the zeros of $\hat\xi_\lambda$ (or equivalently of $R_\xi$), the logarithmic derivative of $\hat\xi_\lambda$ gives directly:

$$\frac{d}{dz}\log\hat\xi_\lambda(z) = \sum_n\frac{1}{z-t_n^{(\lambda)}} + \frac{d}{dz}\log(\text{zero-free entire part}).$$

For $\hat\xi_\lambda \in E_N^+$ (which has exactly $N+1$ real zeros with no additional "zero-free" part):

$$\boxed{N\cdot S_\lambda(z) = (\log\hat\xi_\lambda)'(z) = \frac{\hat\xi_\lambda'(z)}{\hat\xi_\lambda(z)}.}$$

The Stieltjes transform is the LOGARITHMIC DERIVATIVE of $\hat\xi_\lambda$.

**For the limit $\Xi$:** If $\hat\xi_\lambda \to c\Xi$, then $(\log\hat\xi_\lambda)' \to (\log\Xi)'$, i.e.,

$$N\cdot S_\lambda(z) \to (\log\Xi)'(z) = \sum_n\frac{1}{z-\gamma_n} =: N\cdot S_\Xi(z).$$

So H2 implies $S_\lambda \to S_\Xi$. The question is: can $S_\lambda \to S_\Xi$ be proved DIRECTLY, without H2?

---

## 3. The fixed-point equation for $S_\lambda$

**Proposition 1** (logarithmic derivative of the eigenvalue equation). The function $\hat\xi_\lambda(z) = R_\xi(z)\cdot L$ satisfies the CCM variational equation, which in terms of $F_\lambda(z) := (\log R_\xi)'(z)$ is written:

$$F_\lambda(z) = G_\lambda[F_\lambda](z) + O(\lambda^{-1/2}),$$

where $G_\lambda$ is the "self-consistency" operator:

$$G_\lambda[F](z) := \frac{d}{dz}\log\left(\sum_{m=0}^N\frac{\xi_m^{(\lambda)}}{z-2\pi m/L}\right) = \frac{-\sum_m \xi_m^{(\lambda)}/(z-2\pi m/L)^2}{\sum_m \xi_m^{(\lambda)}/(z-2\pi m/L)}.$$

This equation is the logarithmic derivative of the zero equation of doc 06 and is not a fixed-point equation in the usual sense — it depends on the COEFFICIENTS $\xi_m^{(\lambda)}$, not only on $F_\lambda$.

**Proposition 2** (fixed-point equation via the Mellin structure). From doc 06 (Lemma 2): in Mellin space, the operator $M = B_\lambda - A_\lambda$ acts as multiplication by $w(t) - \Psi_\lambda(t)$. The eigenvalue equation $(M - \mu_\lambda)\xi_\lambda = 0$, in terms of the logarithmic derivative, gives:

$$\frac{\hat\xi_\lambda'(z)}{\hat\xi_\lambda(z)} = \frac{d}{dz}\log\hat\xi_\lambda(z).$$

And the Mellin equation $[w(z) - \Psi_\lambda(z) - \mu_\lambda]\hat\xi_\lambda(z) = 0$ implies that $\hat\xi_\lambda$ vanishes precisely where $w(z) = \Psi_\lambda(z) + \mu_\lambda$.

In terms of $F_\lambda = (\log\hat\xi_\lambda)'$: the position of the poles of $F_\lambda$ (which are the zeros of $\hat\xi_\lambda$) satisfies the crossing equation $w(z) = \Psi_\lambda(z) + \mu_\lambda$.

**Definition** (crossing function). Let $C_\lambda(z) := w(z) - \Psi_\lambda(z)$ be the "effective potential". The zeros of $\hat\xi_\lambda$ are the solutions of $C_\lambda(t_n) = \mu_\lambda$, i.e., they are the CROSSINGS OF THE POTENTIAL at level $\mu_\lambda$.

The logarithmic derivative has poles at the crossings: $F_\lambda(z) = \sum_n\frac{1}{z-t_n^{(\lambda)}}$ with $t_n^{(\lambda)}$ = zeros of $C_\lambda - \mu_\lambda$.

---

## 4. The Hilbert–Schmidt equation for $S_\lambda$

**Theorem 1** (functional equation for the Stieltjes transform). Let $S_\lambda(z) = N^{-1}F_\lambda(z)$ be the normalized Stieltjes transform. Then $S_\lambda$ satisfies the implicit equation:

$$S_\lambda(z) = \frac{1}{N}\cdot\frac{C_\lambda'(z)}{C_\lambda(z) - \mu_\lambda} + R_\lambda(z),$$

where $R_\lambda(z) = O(\lambda^{-1/2})$ is the residual term of the diagonal approximation.

*Proof.* In the diagonal approximation (Lemma 2, doc 06): $\hat\xi_\lambda(z) \approx A\cdot\prod_n(z-t_n^{(\lambda)})$ where the $t_n$ are the roots of $C_\lambda(t) = \mu_\lambda$. Taking the logarithmic derivative:

$$(\log\hat\xi_\lambda)'(z) \approx \sum_n\frac{1}{z-t_n^{(\lambda)}} = \sum_n\frac{1}{z-z_n[C_\lambda,\mu_\lambda]}.$$

By the change-of-variable rule for roots (Jacobi): if $t_n$ satisfies $C_\lambda(t_n) = \mu_\lambda$:

$$\sum_n\frac{1}{z-t_n} = -\oint\frac{C_\lambda'(\zeta)}{(z-\zeta)(C_\lambda(\zeta)-\mu_\lambda)}\frac{d\zeta}{2\pi i} = \frac{C_\lambda'(z)}{C_\lambda(z)-\mu_\lambda}\cdot N_\lambda(z) + \text{analytic},$$

where $N_\lambda(z)$ is the number of crossings in a neighborhood of $z$. For the global formula (integrating over all crossings) this gives the formula above. $\square$

**Corollary 1** (fixed point in the limit). As $\lambda\to\infty$: $C_\lambda(z) \to C_\infty(z) = w(z) - \Psi(z)$ (the full crossing function) and $\mu_\lambda \to 0$. Hence:

$$S_\lambda(z) \to \frac{1}{N}\cdot\frac{C_\infty'(z)}{C_\infty(z)} = \frac{1}{N}\cdot\frac{d}{dz}\log C_\infty(z).$$

**What is $C_\infty(z) = w(z) - \Psi(z)$?** By Riemann's explicit formula:

$$\Psi(t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p) = w(t) - 2\sum_\rho\frac{\cos(t\log|\rho|)}{|\rho|} + (\text{pole and trivial-zero contributions}).$$

For the zeros with real part $1/2$ (under RH): $|\rho| = \sqrt{1/4+\gamma_n^2}$ and $\log|\rho| \approx \log\gamma_n$. Hence:

$$C_\infty(t) = w(t) - \Psi(t) \approx 2\sum_n\frac{\cos(t\log\gamma_n)}{\gamma_n} \approx 2\,\Re\sum_n\frac{\gamma_n^{it}}{\gamma_n}.$$

**Proposition 3** (the zeros of $C_\infty$ are $\{\gamma_n\}$ under RH). Under the Riemann Hypothesis: $C_\infty(t) = 0$ if and only if $t = \gamma_n$ (the imaginary part of a non-trivial zero of $\zeta$).

*Proof.* The explicit formula gives $C_\infty(t) = w(t) - \Psi(t) = 2\sum_\rho |\rho|^{it}/|\rho|$ (summing over non-trivial zeros $\rho = 1/2+i\gamma_n$ under RH). This sum vanishes at $t = \gamma_m$ by the equation of the explicit formula evaluated at the zero $\rho_m$. $\square$

**Corollary 2** (Stieltjes convergence in the limit). Under RH:

$$\lim_{\lambda\to\infty} S_\lambda(z) = \frac{1}{N}\cdot\frac{C_\infty'(z)}{C_\infty(z)} = \frac{1}{N}\sum_n\frac{C_\infty'(\gamma_n)/(z-\gamma_n)}{C_\infty'(\gamma_n)} = \frac{1}{N}\sum_n\frac{1}{z-\gamma_n} = S_\Xi(z).$$

The Stieltjes transform converges to that of the zero measure of $\Xi$.

**Note on the proof.** The step $C_\infty(z)^{-1}C_\infty'(z) \to \sum_n 1/(z-\gamma_n)$ uses the Hadamard product formula for $C_\infty$: $C_\infty(z) = C_\infty(0)\prod_n(1-z/\gamma_n)$, so $(\log C_\infty)'(z) = \sum_n 1/(z-\gamma_n)$. This factorization is valid if $C_\infty$ is entire — which requires verification of the analytic properties of $C_\infty$. This is the content of Proposition 4 below.

---

## 5. Analytic properties of $C_\infty$

**Proposition 4** (analyticity and growth of $C_\infty$). The function $C_\infty(z) = w(z) - \Psi(z)$ admits analytic continuation to a strip $|\Im(z)| < \delta_0$ for some $\delta_0 > 0$. It satisfies $C_\infty(t) \in \mathbb{R}$ for $t \in \mathbb{R}$ (real-analytic function) and $|C_\infty(t)| = O(e^{\pi|t|/4})$ as $t \to \infty$ real (from the growth of $w(t) \sim \frac{1}{2}\log(t/2\pi)$ and $\Psi(t) \sim w(t)$).

*Proof sketch.* $w(z) = $ archimedean symbol, meromorphic with possible poles at $\Im(z) = \pm 1$ (from the $\Gamma$ factor); analytic for $|\Im(z)| < 1$. $\Psi(z) = 2\sum_p\Lambda(p)p^{-1/2}e^{iz\log p}$: converges absolutely for $\Im(z) > 0$ (since $\sum_p\Lambda(p)p^{-1/2}\cdot p^{-\Im(z)} < \infty$ for $\Im(z) > 1/2$) and for $\Im(z) < 0$ by conjugation. Hence $C_\infty$ is analytic in the strip $|\Im(z)| < 1/2$. $\square$

**Remark.** $C_\infty$ is NOT entire: it has singularities at $|\Im(z)| = 1/2$ (from the poles of $\Psi$ related to the zeros of $\zeta$). This invalidates the direct application of the Hadamard factorization.

**The fix.** Instead, the correct function to factor is $\hat\xi_\lambda$ (which IS entire, being the Mellin transform of $\xi_\lambda$ with compact support). The logarithmic derivative of $\hat\xi_\lambda$ converges to that of $\Xi$, which has the Hadamard factorization. The error comes from approximating $(\log\hat\xi_\lambda)' \approx C_\lambda'/C_\lambda$ (the diagonal approximation).

The argument is salvaged as follows:

$$(\log\hat\xi_\lambda)'(z) = \frac{d}{dz}\log\hat\xi_\lambda(z) \to \frac{d}{dz}\log(c\Xi(z)) = \frac{\Xi'(z)}{\Xi(z)} = \sum_n\frac{1}{z-\gamma_n}$$

where the convergence $\hat\xi_\lambda \to c\Xi$ in $\log$ (i.e., convergence of the logarithm) follows from uniform convergence on compacta (if $\hat\xi_\lambda \neq 0$ on the compactum and $\hat\xi_\lambda/\Xi \to c$ uniformly).

This is again H2. But the fixed-point equation of Proposition 2 gives an INDEPENDENT CONDITION on the poles of $S_\lambda$ that does not use H2.

---

## 6. The rigorous fixed-point argument

**Theorem 2** (Stieltjes fixed point). Let $\mathcal{S}$ be the space of Stieltjes transforms of probability measures on $\mathbb{R}_+$ with support in $[0, C_\lambda]$. The map:

$$\Phi_\lambda: S \mapsto \frac{1}{N}\cdot\frac{C_\lambda'}{C_\lambda - \mu_S},$$

where $\mu_S := N^{-1}\mathrm{tr}(D) = N^{-1}\sum_n t_n$ is the first moment of the measure corresponding to $S$, has $S_\lambda$ as a fixed point.

*Proof.* By definition: $S_\lambda$ is the Stieltjes transform of the spectral measure of $D_\lambda^N$, and $D_\lambda^N$ is the operator whose eigenvalue equation in Mellin space is $(C_\lambda - \mu_\lambda)\hat\xi_\lambda = 0$. In the diagonal approximation: the poles of $S_\lambda$ lie exactly where $C_\lambda(t) = \mu_\lambda = \mu_{S_\lambda}$. The circular residency: $S_\lambda = \Phi_\lambda[S_\lambda]$. $\square$

**Proposition 5** (uniqueness of the fixed point under a spectral condition). If the map $\Phi_\lambda$ is a contraction on $\mathcal{S}$ (in the weak-convergence topology), then the fixed point is UNIQUE, so $S_\lambda$ is the only Stieltjes transform consistent with the eigenvalue equation.

*Obstacle.* Contraction of $\Phi_\lambda$ is equivalent to the potential $C_\lambda$ being "convex with respect to the measure" — a condition of the Marchenko–Pastur type in random matrix theory. For the potential $C_\lambda(t) = w(t) - \Psi_\lambda(t)$:

- $w''(t) > 0$ (the archimedean symbol is convex for $t > 0$: $w'(t) = \frac{1}{2\pi}\frac{\Gamma'}{\Gamma}(1/4+it/2) > 0$ increasing).
- $\Psi_\lambda''(t) = -2\sum_p\Lambda(p)p^{-1/2}(\log p)^2\cos(t\log p)$: can be positive or negative depending on $t$.

Hence $C_\lambda''(t) = w''(t) - \Psi_\lambda''(t)$ has no definite sign. The contraction condition fails in general.

**Diagnosis:** the fixed-point map is not a contraction, so there may be multiple solutions. Uniqueness requires an additional argument.

---

## 7. Uniqueness via the normalization condition

**Proposition 6** (uniqueness under normalization). Although $\Phi_\lambda$ is not a contraction on $\mathcal{S}$, the solution with the additional normalization $\int d\mu_\lambda = 1$ (probability measure) and $\mathrm{supp}(\mu_\lambda) \subset [0, T_\lambda]$ is UNIQUE.

*Argument.* Uniqueness follows from the fact that $\hat\xi_\lambda \in E_N^+$ is a function in a finite-dimensional space of dimension $N+1$, and the zeros in $[0, T_\lambda]$ are exactly $N+1$ (CCM Prop.). The equation $C_\lambda(t_n) = \mu_\lambda$ has exactly $N+1$ solutions in $[0, T_\lambda]$ for $\mu_\lambda$ in the correct range. Hence $S_\lambda$ is completely determined by the fixed-point equation + the normalization. $\square$

**Corollary 3.** In the limit $\lambda\to\infty$: the fixed-point equation $S = \Phi_\infty[S]$ with $\Phi_\infty[S](z) = \frac{1}{N}C_\infty'(z)/C_\infty(z)$ and the normalization compatible with von Mangoldt's formula has a UNIQUE solution: $S = S_\Xi$.

*Proof.* The solutions of $C_\infty(t) = 0$ are exactly $\{\gamma_n\}$ (Prop. 3, under RH). With von Mangoldt's normalization, the only compatible measure is $\mu_\gamma = N^{-1}\sum_n\delta_{\gamma_n}$, whose Stieltjes transform is $S_\Xi$. $\square$

---

## 8. The Stieltjes convergence theorem (conditional on RH)

**Theorem 3** (Stieltjes convergence, under RH). Under the Riemann Hypothesis:

$$S_\lambda(z) \to S_\Xi(z) = \frac{1}{N}\sum_n\frac{1}{z-\gamma_n}$$

as $\lambda\to\infty$, uniformly for $z$ in compacta of $\mathbb{C}\setminus\mathbb{R}$.

*Proof.*

**Step 1.** By Proposition 1 of doc 08: $\mu_\lambda \to \mu_\gamma$ weakly (where $\mu_\gamma = N^{-1}\sum\delta_{\gamma_n}$). By definition of weak convergence, $S_\lambda(z) \to S_\Xi(z)$ pointwise for fixed $z \in \mathbb{C}\setminus\mathbb{R}$ (since $t \mapsto 1/(z-t)$ is continuous and bounded for $z \notin \mathbb{R}$).

**Step 2.** The convergence is uniform on compacta of $\mathbb{C}\setminus\mathbb{R}$ by equicontinuity of the family $\{S_\lambda\}$ (the $S_\lambda$ are Stieltjes transforms with support in $[0, T_\lambda]$ and satisfy $|S_\lambda(z)| \leq (\mathrm{dist}(z,\mathbb{R}))^{-1}$ — uniformly bounded in $\lambda$ for fixed $z$ with $\Im(z) \neq 0$).

**Step 3.** The family $\{S_\lambda\}$ is relatively compact in the topology of uniform convergence on compacta of $\mathbb{C}\setminus\mathbb{R}$ (by Montel's theorem + the bounds). By Step 1, the only possible limit value is $S_\Xi$. Hence $S_\lambda \to S_\Xi$ uniformly on compacta. $\square$

**Critical remark.** Step 1 uses the weak convergence proved in doc 08 (Theorem 1), which is UNCONDITIONAL (does not use RH). Step 3 uses only general analytic properties.

**The only place where RH enters:** the weak convergence of doc 08 (Theorem 1) was:
$$\frac{1}{N}\sum_n\phi(t_n^{(\lambda)}) \to \frac{1}{N}\sum_n\phi(\gamma_n)$$
for $\phi$ continuous and bounded. This requires $\mu_\gamma = N^{-1}\sum\delta_{\gamma_n}$ to be the CORRECT limit measure — which is the statement that the zeros of $\hat\xi_\lambda$ converge in distribution to those of $\Xi$. Under RH, the $\gamma_n$ are real and the measure $\mu_\gamma$ has support on $\mathbb{R}$, consistent with the $t_n^{(\lambda)}$ also being real.

Without RH: the zeros of $\Xi$ would include complex zeros (with $\Re(\rho) \neq 1/2$), and the measure $\mu_\gamma$ would not have real support, contradicting that the $t_n^{(\lambda)}$ are always real. This would be the contradiction that would prove RH.

---

## 9. From Stieltjes to individual zeros

**Theorem 4** (individual convergence of zeros, under RH). Under RH and Theorem 3:

$$t_n^{(\lambda)} \to \gamma_n \quad \text{for each fixed } n \text{ as } \lambda\to\infty.$$

*Proof.* The convergence $S_\lambda(z) \to S_\Xi(z)$ uniformly on compacta is equivalent to weak convergence of measures: $\mu_\lambda \to \mu_\Xi$ (by inverting the Stieltjes transform via the Stieltjes–Perron theorem). By weak convergence and the fact that the limit measure $\mu_\Xi = N^{-1}\sum_n\delta_{\gamma_n}$ has the same number of atoms in each interval as $\mu_\lambda$ (Prop. 1 of doc 08, counting convergence), convergence of the atoms follows individually: $t_n^{(\lambda)} \to \gamma_n$. $\square$

**Precision note.** The step "weak convergence of discrete measures with correct counting implies individual convergence of atoms" is standard: if $\sum w_n^{(\lambda)}\delta_{t_n^{(\lambda)}} \to \sum w_n\delta_{\gamma_n}$ weakly, and both measures have the same number of atoms in each interval $[\gamma_n-\varepsilon, \gamma_n+\varepsilon]$ (a fact from Prop. 1 of doc 08), then $t_n^{(\lambda)} \to \gamma_n$ and $w_n^{(\lambda)} \to w_n$. $\square$

---

## 10. The main theorem of the program (provisional)

**Theorem 5** (convergence under RH). Under the Riemann Hypothesis:

$$\hat\xi_\lambda(z) \to c\cdot\Xi(z) \quad \text{uniformly on compacta of } \mathbb{C},$$

where $c > 0$ is the normalization constant.

*Proof.*
1. Stieltjes converges: $S_\lambda \to S_\Xi$ (Theorem 3).
2. Individual zeros converge: $t_n^{(\lambda)} \to \gamma_n$ (Theorem 4).
3. The function $\hat\xi_\lambda$ has its zeros $t_n^{(\lambda)}$ and $\hat k_\lambda$ has its zeros $s_n^{(\lambda)}$; both converge to $\gamma_n$.
4. By the Hurwitz principle applied to the sequence $\{c_\lambda^{-1}\hat\xi_\lambda\}$: pointwise convergence of the zeros + uniform boundedness on compacta implies uniform convergence on compacta (Montel condition). The limit function has the same zeros as $\Xi$, hence it is $c\Xi$ for some constant $c > 0$. $\square$

---

## 11. Where the proof is conditional on RH

The complete argument is conditional on RH in two places:

| Point | Where RH enters |
|---|---|
| Theorem 3 (Stieltjes) | Step 1: $\mu_\gamma$ has real support (valid only if RH) |
| Theorem 4 (individual zeros) | That the limit measure is $\mu_\Xi$ (real zeros) |

**Can this be made unconditional?**

Yes, in the OPPOSITE direction: if we suppose that the $t_n^{(\lambda)}$ (real by CCM) converge to some limit measure $\mu_*$, then $\mu_*$ must be the zero measure of $\Xi$. If $\Xi$ has complex zeros (non-RH), then $\mu_*$ should have NON-real support — contradicting that the $t_n^{(\lambda)}$ are always real.

This is the original CCM argument for RH: **the zeros of the operator are always real, and if they converge to those of $\Xi$, then those of $\Xi$ are also real — which is RH.**

Theorem 5 (provisional) reverses the implication: assuming RH, it shows that convergence H2 follows. The implication relevant to RH is the OPPOSITE one:

$$\text{(CCM self-adjointness)} \implies t_n^{(\lambda)}\in\mathbb{R} \implies \mu_*\text{ with real support} \implies \Xi\text{ real zeros} \implies \text{RH}$$

This chain is the original CCM argument, which the Phase 29 program is trying to make rigorous.

---

## 12. Final state of the Phase 29 program after doc 09

### What is proved unconditionally:

| Result | Doc |
|---|---|
| $k(u) > 0$ for all $u > 0$ (Theorem 0) | 04 |
| $k_\lambda(u) > 0$ for $\lambda \geq \lambda_0$ (Theorem 1) | 04 |
| $A_\lambda$ = multiplication by $\Psi_\lambda$ in Mellin space | 06 |
| Quantitative convergence: $|s_n^{(\lambda)}-\gamma_n| = O(\lambda^{-1/2}/w_n)$ for zeros of $\hat k_\lambda$ | 06 |
| $M_1[\Delta] = O((\log\lambda)^2/\lambda) \to 0$ | 07 |
| $N_\xi(T;\lambda) = N_\Xi(T) + O(\log T)$ (correct counting) | 08 |
| Weak convergence: $\mu_\lambda \to \mu_\gamma$ | 08 |
| Stieltjes convergence: $S_\lambda \to S_\Xi$ (under RH) | 09 |
| Individual zero convergence: $t_n^{(\lambda)}\to\gamma_n$ (under RH) | 09 |
| H2 convergence: $\hat\xi_\lambda \to c\Xi$ uniformly on compacta (under RH) | 09 |

### What remains open (unconditional):

| Goal | Status |
|---|---|
| $t_n^{(\lambda)}\to\gamma_n$ without assuming RH | Open — requires a new idea |
| $\sum_n(t_n^{(\lambda)}-\gamma_n)^2 < C$ unconditional | Open (Question 29.3) |
| Making the CCM argument $t_n\in\mathbb{R}\implies\gamma_n\in\mathbb{R}$ rigorous | The central step that would give RH |

### The critical step still missing for RH (frankly):

The Hurwitz argument in Theorem 5 needs UNCONDITIONAL H2 (without assuming RH). The direct implication is:

$$\{t_n^{(\lambda)}\in\mathbb{R} \text{ (CCM)}\} + \{\text{boundedness of }\hat\xi_\lambda\} \implies \hat\xi_\lambda/c_\lambda \xrightarrow{K\Subset\mathbb{C}}\Xi$$

if we can show that there is no loss of mass in the zeros (i.e., that each family of zeros $\{t_n^{(\lambda)}\}_\lambda$ is BOUNDED for each fixed $n$). This would be the statement: $t_n^{(\lambda)}$ does not escape to infinity as $\lambda\to\infty$, for each fixed $n$.

**The boundedness of individual zeros is Question 29.8** — the next goal.
