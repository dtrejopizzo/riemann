# Document 86 — Relative entropy and extremality of $dm_{full}$: synthesis of Path 1

**Program:** Riemann Hypothesis — Phase 33 DBN-CCM  
**Prerequisites:** Docs 74, 77, 80, 83

---

## Summary

Document 83 established the pointwise domination $dm_{full} \geq dm_{full,on}$ as measures and diagnosed that no measure-domination argument can, by itself, prove RH: the transition from $\geq$ to $=$ is precisely the non-trivial content of the hypothesis. The present document explores whether the language of information theory — in particular relative entropy (Kullback-Leibler divergence) and its variants — offers a new entry point to the problem.

The conclusion is no. The relative entropy $\mathcal{KL}(dm_{full}\|dm_{full,on})$, the Jensen-Shannon divergence, the Wasserstein distance, and the Herglotz function associated to the difference of measures are all reformulations of the same criterion: they are zero if and only if RH. Each adds a clean technical perspective, but none provides an independent means of verification. In §10 the obstacle is formalized as the "Hadamard barrier" and a precise open problem is formulated that summarizes the state of Path 1.

---

## §1. The relative entropy between $dm_{full}$ and $dm_{full,on}$

### 1.1. Definition and first formula

We adopt the notation of Doc 83. For $s \in \mathbb{R}$ we write $d m_{full}(s) = |\zeta(1/2+is)|^2 dm_\infty(s)$ and $dm_{full,on}(s) = |\zeta_{on}(1/2+is)|^2 dm_\infty(s)$, where $dm_\infty$ is the reference spectral measure of the Jacobi operator associated to the completed zeta function (normalized so that the two measures have the same finite mass; its exact value is not essential here).

The **Kullback-Leibler divergence** of $dm_{full}$ with respect to $dm_{full,on}$ is defined as

$$\mathcal{KL}(dm_{full} \| dm_{full,on}) = \int_{\mathbb{R}} \log\frac{dm_{full}}{dm_{full,on}}\, dm_{full} = \int_{\mathbb{R}} \log\left(\frac{|\zeta(1/2+is)|^2}{|\zeta_{on}(1/2+is)|^2}\right) |\zeta(1/2+is)|^2\, dm_\infty(s).$$

By Proposition 1.1 of Doc 83, the density ratio $R(s) := |\zeta(1/2+is)|^2/|\zeta_{on}(1/2+is)|^2$ is expressed via the Hadamard product as

$$R(s) = \prod_{j:\,\delta_j>0} \left(1 + \frac{\delta_j^2}{(s-\gamma_j)^2}\right)^2,$$

where the product runs over the off-critical zeros with real part $1/2+\delta_j > 1/2$ (one from each quartet). In particular $R(s) \geq 1$ for all real $s$ (away from the zeros of $\zeta_{on}$), with pointwise equality $R(s) = 1$ for all $s$ if and only if all $\delta_j = 0$, that is, if and only if RH.

The function $\log R(s)$ admits the representation

$$\log R(s) = 2\sum_{j:\,\delta_j>0} \log\left(1 + \frac{\delta_j^2}{(s-\gamma_j)^2}\right).$$

Each term is non-negative and vanishes if and only if $\delta_j = 0$.

### 1.2. The relative entropy is non-negative and vanishes exactly under RH

**Proposition 1.1.** $\mathcal{KL}(dm_{full}\|dm_{full,on}) \geq 0$, with equality if and only if $dm_{full} = dm_{full,on}$ $dm_\infty$-almost everywhere. This latter condition is equivalent to RH.

*Proof.* The inequality $\mathcal{KL} \geq 0$ is the standard Gibbs inequality: for any pair of probability measures $\mu \ll \nu$, one has $\int \log(d\mu/d\nu)\,d\mu \geq 0$ by the convexity of $x \mapsto x\log x$ and Jensen's inequality. (For non-unit finite-mass measures the argument is analogous.) Equality holds if and only if the density $d\mu/d\nu$ is constant $\mu$-a.e., which here means $R(s) = 1$ almost everywhere. But $R(s)$ is a real-analytic function (away from the $\gamma_j$, which form a discrete set), so $R \equiv 1$ a.e. implies $R \equiv 1$ on all of $\mathbb{R}$, and this is equivalent to all $\delta_j = 0$, that is, RH. $\square$

This result is correct and its proof is elementary. The important observation is that there is no new content: the equivalence "$\mathcal{KL} = 0 \Leftrightarrow \text{RH}$" is a reformulation, not a proof.

---

## §2. Relation between $\mathcal{KL}$ and the trace $T_\lambda$

### 2.1. The two functionals compared

We recall from Doc 70 that the relevant trace of the CTP criterion is

$$T_\lambda = \int_{\mathbb{R}} W_\lambda(s)\, (dm_{full} - dm_{full,on})(s) = \int_{\mathbb{R}} W_\lambda(s)\, (R(s)-1)\, |\zeta_{on}(1/2+is)|^2\, dm_\infty(s),$$

where $W_\lambda \geq 0$ is the weight kernel of the De Bruijn-Newman operator at level $\lambda$.

The KL divergence can be rewritten as

$$\mathcal{KL}(dm_{full}\|dm_{full,on}) = \int_{\mathbb{R}} \log R(s)\cdot R(s)\cdot |\zeta_{on}(1/2+is)|^2\, dm_\infty(s).$$

### 2.2. Comparison via the inequality $\log x \leq x - 1$

For all $x > 0$ one has $\log x \leq x - 1$. Applying this to $x = R(s) \geq 1$:

$$\log R(s) \leq R(s) - 1.$$

Multiplying both sides by $R(s) \geq 1$ and by $|\zeta_{on}|^2 dm_\infty \geq 0$:

$$\log R(s) \cdot R(s) \cdot |\zeta_{on}|^2 \leq (R(s)-1)\cdot R(s)\cdot |\zeta_{on}|^2.$$

This gives

$$\mathcal{KL}(dm_{full}\|dm_{full,on}) \leq \int_{\mathbb{R}} (R(s)-1)\, R(s)\, |\zeta_{on}|^2\, dm_\infty = \int_{\mathbb{R}} (R(s)-1)\, |\zeta(1/2+is)|^2\, dm_\infty,$$

which does not involve $W_\lambda$ and which differs from $T_\lambda$ both by the weight (it is integrated against $|\zeta|^2 dm_\infty$ instead of $W_\lambda |\zeta_{on}|^2 dm_\infty$) and by the presence of the extra factor $R$.

**Proposition 2.1.** There is no direct comparison relation between $T_\lambda$ and $\mathcal{KL}(dm_{full}\|dm_{full,on})$ that holds unconditionally. The two functionals are comparable only if uniform bounds on $R(s)$ in $s$ are available, and such bounds depend on the position of the off-critical zeros.

*Argument.* $T_\lambda$ integrates $(R-1)|\zeta_{on}|^2$ with weight $W_\lambda$, while $\mathcal{KL}$ integrates $(\log R)\cdot R \cdot |\zeta_{on}|^2$ with weight 1. In regions where $R(s)$ is large (near an off-critical zero $\gamma_j$, where $R(s) \sim \delta_j^2/(s-\gamma_j)^2 \to \infty$), the integrand of $\mathcal{KL}$ dominates that of $T_\lambda$ (if $W_\lambda(\gamma_j)$ is finite). In regions where $R \approx 1$, the two integrands are comparable to first order in $\delta_j^2$. Without bounds on the $\delta_j$ and the $\gamma_j$, the global comparison cannot be established.

### 2.3. The first-order expansion in $\delta_j^2$

For small $\delta_j$, expanding $R(s) = 1 + 2\sum_j \delta_j^2/(s-\gamma_j)^2 + O(\delta_j^4)$ and $\log R(s) = 2\sum_j \delta_j^2/(s-\gamma_j)^2 + O(\delta_j^4)$:

$$\mathcal{KL} = \int_{\mathbb{R}} \left(2\sum_j \frac{\delta_j^2}{(s-\gamma_j)^2} + O(\delta_j^4)\right) |\zeta_{on}|^2\, dm_\infty + O(\delta_j^4),$$

$$T_\lambda = \int_{\mathbb{R}} W_\lambda(s) \left(2\sum_j \frac{\delta_j^2}{(s-\gamma_j)^2} + O(\delta_j^4)\right)|\zeta_{on}|^2\, dm_\infty + O(\delta_j^4).$$

To this order, $T_\lambda$ and $\mathcal{KL}$ differ only by the weight $W_\lambda$ versus $1$: if $W_\lambda \leq 1$ uniformly, then $T_\lambda \leq \mathcal{KL}$ to first order in $\delta_j^2$. But this comparison is only perturbative and transfers no new information.

---

## §3. Relative entropy as a functional over the Hadamard class

### 3.1. The class of Hadamard measures

We define the class

$$\mathcal{M}_{Hd} = \left\{d\mu = |\eta(1/2+is)|^2 dm_\infty(s) : \eta \text{ entire of order 1, same total mass as }\zeta \right\},$$

where the "same total mass" condition means $\int |\eta|^2 dm_\infty = \int |\zeta|^2 dm_\infty$. This class includes both $dm_{full}$ (with the real zero distribution of $\zeta$) and $dm_{full,on}$ (with all zeros projected onto the critical line).

The Shannon entropy of $\mu \in \mathcal{M}_{Hd}$ (with respect to $dm_\infty$) is defined as

$$H(\mu) = -\int \log\left(\frac{d\mu}{dm_\infty}\right) d\mu = -\int \log(|\eta|^2) |\eta|^2\, dm_\infty.$$

### 3.2. Is $dm_{full,on}$ the entropy maximizer?

**Proposition 3.1.** The measure $dm_{full,on}$ is not, in general, the maximizer of $H(\mu)$ in $\mathcal{M}_{Hd}$. The maximum entropy principle in this class does not impose that the zeros lie on the critical line.

*Argument.* The maximizer of $H(\mu) = -\int \log(|\eta|^2)|\eta|^2\, dm_\infty$ over the class $\mathcal{M}_{Hd}$ with the single constraint of fixed mass is the measure with constant density $|\eta|^2 = C$, that is, the measure absolutely continuous with respect to $dm_\infty$ with uniform density. This solution corresponds neither to $dm_{full}$ nor to $dm_{full,on}$ (whose densities are not constant, since they have zeros at the $\pm \gamma_j$ with multiplicity).

If constraints of the type "the moments of the zero distribution lie on the critical line" are added, the constrained maximization problem may have $dm_{full,on}$ as its solution. But such constraints are exactly equivalent to imposing RH as an a priori condition, so the argument is circular.

**Conclusion of §3.** The maximum entropy principle does not provide an independent characterization of $dm_{full,on}$ within $\mathcal{M}_{Hd}$. The relation between the zero distribution and the entropy of the spectral measure does not have the structure of a convex variational problem with a unique solution determined by the position of the zeros.

---

## §4. The Jensen-Shannon divergence

### 4.1. Definition

Let $dm_M = (dm_{full} + dm_{full,on})/2$ be the arithmetic mixture of the two measures. The **Jensen-Shannon divergence** is

$$\mathcal{JS}(dm_{full}, dm_{full,on}) = \frac{1}{2}\mathcal{KL}(dm_{full}\|dm_M) + \frac{1}{2}\mathcal{KL}(dm_{full,on}\|dm_M).$$

Unlike $\mathcal{KL}$, the divergence $\mathcal{JS}$ is symmetric and bounded: $0 \leq \mathcal{JS} \leq \log 2$.

### 4.2. Explicit expression using $R(s) \geq 1$

The relative densities are $dm_{full}/dm_M = 2R(s)/(R(s)+1)$ and $dm_{full,on}/dm_M = 2/(R(s)+1)$. Therefore

$$\mathcal{JS} = \frac{1}{2}\int \log\!\left(\frac{2R(s)}{R(s)+1}\right) R(s) |\zeta_{on}|^2 dm_\infty + \frac{1}{2}\int \log\!\left(\frac{2}{R(s)+1}\right) |\zeta_{on}|^2 dm_\infty.$$

Using $R(s) \geq 1$: the factor $2R(s)/(R(s)+1) \in [1,2)$ for $R \geq 1$, so $\log(2R/(R+1)) \geq 0$; the factor $2/(R(s)+1) \in (0,1]$ for $R \geq 1$, so $\log(2/(R+1)) \leq 0$. The two terms have opposite signs and the positivity of $\mathcal{JS}$ follows from the convexity of $x \mapsto x\log x$ (not from a term-by-term sign argument).

**Proposition 4.1.** $\mathcal{JS}(dm_{full}, dm_{full,on}) \geq 0$ with equality if and only if $R(s) \equiv 1$ (iff RH). The bound $\mathcal{JS} \leq \log 2$ is universal.

The upper bound $\mathcal{JS} \leq \log 2$ is interesting since it bounds the "relative distance" between $dm_{full}$ and $dm_{full,on}$ independently of the zero distribution. But, again, the condition $\mathcal{JS} = 0$ is equivalent to RH and provides no new route to a proof.

---

## §5. The ratio $R(s)$ and its analytic properties

### 5.1. Structure of $R(s)$ as a real-analytic function

The ratio $R(s) = |\zeta(1/2+is)|^2/|\zeta_{on}(1/2+is)|^2$ is a real-analytic function on $\mathbb{R} \setminus \{\gamma_j\}_{j}$. At the points $s = \gamma_j$ (zeros of $\zeta_{on}$ on the critical line), the function $|\zeta_{on}(1/2+is)|^2$ vanishes, while $|\zeta(1/2+is)|^2$ may or may not vanish depending on whether $\gamma_j$ is also a zero of $\zeta$ (in which case the vanishing orders are compared).

For the purposes of this section we consider the generic points $s \neq \gamma_j$ where $R(s)$ is well defined.

**Proposition 5.1.** $R(s) = 1$ for all $s \in \mathbb{R} \setminus \{\gamma_j\}$ if and only if all $\delta_j = 0$ (RH). Under $\neg$RH, $R(s) > 1$ for all $s \in \mathbb{R} \setminus \{\gamma_j\}$, and $\inf_{s \in \mathbb{R}} R(s) = 1$ (the infimum is attained in the limit $|s| \to \infty$, where all factors tend to 1).

*Proof.* The Hadamard product shows that $R(s) = \prod_j (1+\delta_j^2/(s-\gamma_j)^2)^2 \geq 1$ with pointwise equality only if all $\delta_j = 0$. As $|s| \to \infty$, each factor $(1+\delta_j^2/(s-\gamma_j)^2) \to 1$, and convergence of the product (which requires $\sum_j \delta_j^2/\gamma_j^2 < \infty$, valid by the density of zeros of $\zeta$) guarantees $R(s) \to 1$. $\square$

### 5.2. The function $\log R$ near $s = \gamma_j$

Near $s = \gamma_j$, the $j$-th factor of $R(s)$ is $(1+\delta_j^2/(s-\gamma_j)^2)^2 \sim \delta_j^4/(s-\gamma_j)^4$, so $\log R(s) \sim 4\log(\delta_j/(s-\gamma_j)) \to +\infty$. The singularity is logarithmic and the integral $\int \log R(s)\, |\zeta_{on}|^2\, dm_\infty$ converges because $|\zeta_{on}(1/2+is)|^2 \sim (s-\gamma_j)^2$ near $s = \gamma_j$ (simple zero of $\zeta_{on}$), and $(s-\gamma_j)^2 \log(1/(s-\gamma_j)) \to 0$.

This convergence is another way of seeing that $\mathcal{KL}$ is well defined.

---

## §6. The function $\log R$ and the trace $T_\lambda$ to all orders

### 6.1. Representation of $T_\lambda$ in terms of the ratio $R$

Using $R(s) - 1 = (|\zeta|^2 - |\zeta_{on}|^2)/|\zeta_{on}|^2$:

$$T_\lambda = \int_{\mathbb{R}} W_\lambda(s)\, (R(s)-1)\, |\zeta_{on}(1/2+is)|^2\, dm_\infty(s).$$

### 6.2. Series expansion in $\delta_j^2$

For off-critical zeros with arbitrary (not necessarily small) displacements $\delta_j$, the expansion of the Hadamard product gives

$$R(s) - 1 = \prod_j \left(1+\frac{\delta_j^2}{(s-\gamma_j)^2}\right)^2 - 1 = \sum_j \frac{2\delta_j^2}{(s-\gamma_j)^2} + \sum_{j<k}\frac{4\delta_j^2\delta_k^2}{(s-\gamma_j)^2(s-\gamma_k)^2} + \cdots$$

where the higher-order terms in $\delta^2$ are positive. In particular $R(s)-1 \geq \sum_j 2\delta_j^2/(s-\gamma_j)^2$.

**Proposition 6.1.** One has the lower bound

$$T_\lambda \geq 2\sum_{j:\,\delta_j>0} \delta_j^2 \int_{\mathbb{R}} \frac{W_\lambda(s)}{(s-\gamma_j)^2}\, |\zeta_{on}(1/2+is)|^2\, dm_\infty(s).$$

Each term on the right-hand side is non-negative (since $W_\lambda \geq 0$, $|\zeta_{on}|^2 \geq 0$ and $(s-\gamma_j)^{-2} \geq 0$). If some $\delta_j > 0$ and the integral is strictly positive (which occurs whenever $\zeta_{on}$ is not identically zero in a neighborhood of $\gamma_j$), then $T_\lambda > 0$.

This confirms the CTP criterion of Docs 70–72: $T_\lambda > 0$ under $\neg$RH. But, as noted in Doc 83, the reverse implication ($T_\lambda = 0 \Rightarrow$ RH) is the non-trivial content of the criterion and does not follow from this estimate.

We define the generalized Poisson kernel

$$K_\lambda(\gamma_j) := \int_{\mathbb{R}} \frac{W_\lambda(s)}{(s-\gamma_j)^2}\, |\zeta_{on}(1/2+is)|^2\, dm_\infty(s) > 0,$$

so that $T_\lambda \geq 2\sum_j \delta_j^2 K_\lambda(\gamma_j)$. The inequality is strict if some $\delta_j > 0$.

---

## §7. The Wasserstein distance

### 7.1. Definition

The **order-2 Wasserstein distance** between $dm_{full}$ and $dm_{full,on}$ is

$$W_2(dm_{full}, dm_{full,on})^2 = \inf_{\pi} \int_{\mathbb{R}^2} (s-t)^2\, d\pi(s,t),$$

where the infimum is over all couplings (measures with margins $dm_{full}$ and $dm_{full,on}$ respectively).

### 7.2. The domination coupling

Since $dm_{full} \geq dm_{full,on}$ as positive measures, one can construct the domination coupling: write $dm_{full} = dm_{full,on} + d\nu$ where $d\nu = (R(s)-1)|\zeta_{on}|^2\, dm_\infty \geq 0$. A natural coupling is the sum of the diagonal coupling $\delta_{s=t}$ over $dm_{full,on}$ plus a coupling of the extra mass $d\nu$ to any point. For the diagonal coupling over $dm_{full,on}$ plus the "excess" coupled to its origin:

$$\pi^*(s,t) = dm_{full,on}(s)\,\delta_s(dt) + d\nu(s)\,\delta_{s_0}(dt)$$

for some reference point $s_0$. This coupling is not optimal in general, but it gives the bound

$$W_2^2 \leq \int (s-t)^2\, d\pi^* = \int (s-s_0)^2\, d\nu(s) = \int (s-s_0)^2(R(s)-1)|\zeta_{on}|^2\, dm_\infty.$$

The optimal bound requires solving the optimal transport problem, which is non-trivial in this context.

**Proposition 7.1.** $W_2(dm_{full}, dm_{full,on}) = 0$ if and only if $dm_{full} = dm_{full,on}$ (iff RH). Without additional information about the off-critical zeros, $W_2$ cannot be computed explicitly.

### 7.3. Comparison with $T_\lambda$

The trace $T_\lambda = \int W_\lambda (dm_{full} - dm_{full,on})$ is the first moment of the difference measure $dm_{full} - dm_{full,on}$ against the weight $W_\lambda$. The Wasserstein distance $W_2$ is the second moment of the optimal transport. They are quantities of a different nature and are not directly comparable without additional hypotheses.

---

## §8. The extremal Radon-Nikodym condition

### 8.1. Setup

The Radon-Nikodym density of $dm_{full}$ with respect to $dm_{full,on}$ is $R(s) \geq 1$. RH is equivalent to this density being identically 1. The question is: does there exist a spectral or analytic condition on $R$ that is easier to verify than RH itself and that implies $R \equiv 1$?

### 8.2. The Helson-Szegő theorem and its scope

The Helson-Szegő theorem (1960) characterizes, on the unit circle, the measures $d\mu = w\,dm$ for which the Hardy projection operator (Szegő operator) is bounded on $L^2(d\mu)$: the condition is that $\log w = u + \tilde{v}$ where $u \in L^\infty$, $v \in L^\infty$ real with $\|v\|_\infty < \pi/2$, and $\tilde{v}$ is the harmonic conjugate of $v$.

In our context, $w(s) = R(s) = |\zeta|^2/|\zeta_{on}|^2$ and the base measure is $dm_{full,on}$. An application in the spirit of the Helson-Szegő theorem would require:

1. Transferring the problem from the real line to the unit circle (via a Möbius transformation).
2. Identifying the associated Szegő operator with the relevant Jacobi operator.
3. Verifying that the boundedness condition for the Szegő operator can be checked without knowing the zeros of $\zeta$.

Step 3 is the one that fails. The boundedness of the Szegő operator for the measure $dm_{full}$ in $L^2(dm_{full,on})$ is equivalent to conditions on $R(s)$ that depend on the global structure of the off-critical zeros. No autonomous criterion for this boundedness is available.

**Conclusion of §8.** The Helson-Szegő theorem suggests an interesting direction (connecting the Radon-Nikodym density $R$ with the boundedness of Szegő operators) but does not provide a direct route to RH with the tools available.

---

## §9. The Herglotz function and extremality

### 9.1. The Herglotz function associated to $dm_{full}$

For $z \in \mathbb{C}$ with $\mathrm{Im}(z) > 0$, the **Herglotz function** (also called the Cauchy-Stieltjes or Carathéodory function, depending on the normalization) associated to $dm_{full}$ is

$$\mathcal{F}(z) = \int_{\mathbb{R}} \frac{s+z}{s-z}\, dm_{full}(s).$$

This function satisfies $\mathrm{Re}\,\mathcal{F}(z) > 0$ for $\mathrm{Im}(z) > 0$ (it is a Carathéodory function). Similarly, $\mathcal{F}_{on}(z)$ is defined with $dm_{full,on}$.

### 9.2. The difference $\mathcal{F}(z) - \mathcal{F}_{on}(z)$

**Proposition 9.1.** The difference

$$\mathcal{G}(z) := \mathcal{F}(z) - \mathcal{F}_{on}(z) = \int_{\mathbb{R}} \frac{s+z}{s-z}\, (dm_{full} - dm_{full,on})(s)$$

is also a Herglotz function: $\mathrm{Re}\,\mathcal{G}(z) \geq 0$ for $\mathrm{Im}(z) > 0$, with $\mathrm{Re}\,\mathcal{G}(z) = 0$ (identically) if and only if $dm_{full} = dm_{full,on}$ (iff RH).

*Proof.* For $\mathrm{Im}(z) > 0$ and $s \in \mathbb{R}$, the ratio $(s+z)/(s-z)$ has real part $\mathrm{Re}[(s+z)/(s-z)] = [(s^2-|z|^2)/|s-z|^2 + 2s\mathrm{Im}(z)/|s-z|^2\cdot\mathrm{Re}(z/z)]$... let us compute directly: write $z = x+iy$, $y > 0$. Then $s-z = (s-x)-iy$ and $s+z = (s+x)+iy$. The ratio

$$\frac{s+z}{s-z} = \frac{(s+x+iy)(s-x+iy)}{(s-x)^2+y^2} = \frac{(s^2-x^2+y^2) + 2iys}{(s-x)^2+y^2}.$$

The real part is $(s^2-x^2+y^2)/((s-x)^2+y^2)$, whose sign can be positive or negative depending on $s$. Let us correct the claim.

For $z = iy$ purely imaginary with $y > 0$: $\mathrm{Re}[(s+iy)/(s-iy)] = (s^2-y^2+y^2)/(s^2+y^2) = s^2/(s^2+y^2) \geq 0$. For general $z$ the real part is not necessarily non-negative.

The relevant correction is the following: $\mathcal{G}(z)$ is a Nevanlinna function (with non-negative imaginary part) in the upper half-plane, not necessarily a Carathéodory function. But for the Nevanlinna representation:

$$\mathrm{Im}\,\mathcal{G}(z) = \int_{\mathbb{R}} \mathrm{Im}\,\!\left[\frac{s+z}{s-z}\right] (dm_{full}-dm_{full,on})(s).$$

For $z = x+iy$, $y > 0$:

$$\mathrm{Im}\,\!\left[\frac{s+z}{s-z}\right] = \mathrm{Im}\,\!\left[\frac{(s+x+iy)(s-x+iy)}{|s-z|^2}\right] = \frac{y(s+x) + y(s-x)}{|s-z|^2} = \frac{2ys}{|s-z|^2}.$$

This has the sign of $s$, and is not non-negative in general.

The correct Nevanlinna representation uses the Poisson-Stieltjes formula. What can be asserted is that $\mathcal{G}$ has a Nevanlinna representation with spectral measure $dm_{full} - dm_{full,on} \geq 0$, which is a Nevanlinna function with positive spectral measure — this corresponds to the class of Pick functions with positive representing measure.

**Proposition 9.1 (corrected).** The function $\mathcal{G}(z) = \mathcal{F}(z) - \mathcal{F}_{on}(z)$ admits the Nevanlinna representation

$$\mathcal{G}(z) = \int_{\mathbb{R}} \frac{1+sz}{s-z}\, (dm_{full}-dm_{full,on})(s) + \alpha + \beta z$$

for certain real constants $\alpha, \beta \geq 0$ (with the standard normalizations). The spectral measure of $\mathcal{G}$ is the positive measure $dm_{full} - dm_{full,on} \geq 0$.

$\mathcal{G}(z) \equiv 0$ if and only if $dm_{full} = dm_{full,on}$ as measures, that is, if and only if RH.

### 9.3. Jacobi operators and the function $\mathcal{G}$

The Nevanlinna function $\mathcal{G}$ with spectral measure $dm_{full} - dm_{full,on} \geq 0$ defines a third Jacobi operator $J_\mathcal{G}$ whose coefficients $\{a_k^\mathcal{G}, b_k^\mathcal{G}\}$ are determined by the moments of the difference measure. The relations between $J_\mathcal{G}$, $J_{full}$ and $J_{on}$ are not simple (the Jacobi coefficients are not linear in the spectral measure).

The condition RH $\equiv \mathcal{G} \equiv 0 \equiv J_\mathcal{G} = 0$ could — in principle — be connected with properties of the CCM Jacobi operator. But no direct route is known.

---

## §10. Synthesis: Path 1 and the final obstacle formalized

### 10.1. The chain of equivalences

**Theorem 10.1 (synthesis of Path 1).** The following conditions are mutually equivalent:

1. **RH:** all non-trivial zeros of $\zeta$ have real part $1/2$.
2. **Equality of measures:** $dm_{full} = dm_{full,on}$ (as measures on $\mathbb{R}$).
3. **CTP criterion:** $T_\lambda = 0$ for all $\lambda \geq 0$.
4. **Zero relative entropy:** $\mathcal{KL}(dm_{full}\|dm_{full,on}) = 0$.
5. **Zero JS divergence:** $\mathcal{JS}(dm_{full}, dm_{full,on}) = 0$.
6. **Zero Wasserstein:** $W_2(dm_{full}, dm_{full,on}) = 0$.
7. **Trivial density:** $R(s) \equiv 1$ for $dm_\infty$-a.e. $s \in \mathbb{R}$.
8. **Zero Herglotz:** $\mathcal{G}(z) \equiv 0$ in the upper half-plane.

*Proof.* The implications $1 \Leftrightarrow 2$ and $2 \Rightarrow$ all the others are immediate from the definitions. The reverse implications ($3,4,5,6,7,8 \Rightarrow 2$) all follow from the strict positivity of the respective functionals under $\neg$RH (established in the previous propositions and in Doc 83) and from the analyticity of $R$ (which prevents $R \equiv 1$ a.e. without $R \equiv 1$ everywhere). The equivalence $2 \Leftrightarrow 3$ is the CTP criterion of Docs 64 and 70. $\square$

### 10.2. What each reformulation adds

Each reformulation of conditions 2–8 illuminates a different aspect of the structure:

- Conditions 2 and 7 (equality of measures / trivial density) are the most direct: RH in terms of spectral measures.
- Condition 3 (CTP criterion) is the entry point of the DBN-CCM program and connects with the De Bruijn-Newman flow.
- Conditions 4 and 5 (relative entropy and JS) place the problem within the framework of information theory: RH is the condition of "informational indistinguishability" between the two measures.
- Condition 6 (Wasserstein) places it within the framework of optimal transport.
- Condition 8 (Herglotz) connects it with the theory of Nevanlinna functions and Jacobi operators.

None of these reformulations by itself provides a route to a proof. What they offer is a precise vocabulary for articulating the obstacle.

### 10.3. The Hadamard barrier

**Problem 10.1 (Hadamard Barrier).** Does there exist a property $\mathcal{P}$ of the function $\zeta$ that simultaneously satisfies:

(a) $\mathcal{P}$ is verifiable from known analytic properties of $\zeta$ (the functional equation, the order of growth, the asymptotic distribution of zeros, the moment estimates of the zeta function) without assuming the position of the non-trivial zeros;

(b) $\mathcal{P}$ implies one of the equivalent conditions of Theorem 10.1?

Path 1 has found no property satisfying (a) and (b) simultaneously. All the criteria of conditions 2–8 are verifiable conditionally on RH (trivially: if RH, then $R \equiv 1$, etc.) but not unconditionally.

The obstacle is structural: the Hadamard product expresses $R(s)-1$ as a sum of contributions from the off-critical zeros with weight $\delta_j^2/(s-\gamma_j)^2$. To prove $R \equiv 1$ without information about the zeros one must prove that no zero can be off the critical line, which is exactly RH. There is no shortcut.

### 10.4. Final diagnosis of Path 1

Path 1 has produced the following positive, entirely unconditional results:

- **Pointwise domination** $|\zeta(1/2+is)|^2 \geq |\zeta_{on}(1/2+is)|^2$ for all $s \in \mathbb{R}$ (Proposition 1.1, Doc 83).
- **Measure domination** $dm_{full} \geq dm_{full,on}$ as positive measures (Corollary 1.2, Doc 83).
- **Positivity of $T_\lambda$** under $\neg$RH: $T_\lambda \geq 2\sum_j \delta_j^2 K_\lambda(\gamma_j) > 0$ (Proposition 6.1 of the present document).
- **Equivalences** among multiple formulations of the RH criterion: relative entropy, Wasserstein distance, Herglotz function (Theorem 10.1).
- **Formalization of the obstacle** as the Hadamard Barrier (Problem 10.1).

What Path 1 has not achieved: any argument that does not use the position of the zeros and that implies one of conditions 2–8 of Theorem 10.1. The barrier is robust: any function $\zeta$ with an off-critical zero has $R(s) > 1$ at every point, $\mathcal{KL} > 0$, $T_\lambda > 0$, etc., and none of these strict inequalities can be refuted by global properties of $\zeta$ known unconditionally.

### 10.5. The most promising connection: $\mathcal{G}$ and Path 2

The Nevanlinna function $\mathcal{G}(z) = \mathcal{F}(z) - \mathcal{F}_{on}(z)$ with spectral measure $dm_{full} - dm_{full,on}$ is the natural object that "measures" the departure from RH from the perspective of Path 1. This function has a positive spectral representation and is connected to the Jacobi operator $J_\mathcal{G}$.

On the other hand, Path 2 (L-functions and reciprocity) works directly with the zeta function as an analytic function in the complex plane and with its relations to the distribution of primes. The possible connection is the following: if the Jacobi coefficients of $J_\mathcal{G}$ can be expressed in terms of sums over primes (as suggested by the Weil explicit formula of Doc 72), then the condition $\mathcal{G} \equiv 0$ could be reformulated as an identity between sums over primes and sums over zeros — an identity that might be accessible via reciprocity.

This connection is not developed and remains the most promising direction for future work.

---

## Appendix: summary of objects and notation of Path 1

| Symbol | Definition |
|---------|-----------|
| $dm_{full}$ | Spectral measure $\lvert\zeta(1/2+is)\rvert^2 dm_\infty$ |
| $dm_{full,on}$ | Same with zeros of $\zeta$ projected onto the critical line |
| $R(s)$ | Ratio $\lvert\zeta(1/2+is)\rvert^2/\lvert\zeta_{on}(1/2+is)\rvert^2 \geq 1$ |
| $\delta_j$ | Distance of the $j$-th off-critical zero to the critical line |
| $T_\lambda$ | Trace $\int W_\lambda\,(dm_{full}-dm_{full,on})$ |
| $\mathcal{KL}$ | Kullback-Leibler divergence of $dm_{full}$ with respect to $dm_{full,on}$ |
| $\mathcal{JS}$ | Jensen-Shannon divergence (symmetric) between the two measures |
| $W_2$ | Order-2 Wasserstein distance between the two measures |
| $\mathcal{F}$, $\mathcal{F}_{on}$ | Herglotz/Nevanlinna functions of $dm_{full}$ and $dm_{full,on}$ |
| $\mathcal{G}$ | $\mathcal{F} - \mathcal{F}_{on}$: Nevanlinna function with spectral measure $dm_{full}-dm_{full,on}$ |
| Hadamard barrier | Problem 10.1: known non-existence of an unconditional verification of $R \equiv 1$ |

---

**End of Document 86**
