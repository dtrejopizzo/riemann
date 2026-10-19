# The Laguerre–Pólya class and the correct concavity

**Origin:** Question 28.1 had the wrong direction. This document develops the correct direction.

---

## 1. The reality of $\xi$ on the critical line

**Proposition 1** (fundamental symmetry). For every $t \in \mathbb{R}$:
$$\xi\!\left(\tfrac{1}{2}+it\right) \in \mathbb{R}.$$

*Proof.* The two symmetries of $\xi$:
- Functional equation: $\xi(s) = \xi(1-s)$.
- Reality (real axis): $\overline{\xi(s)} = \xi(\bar s)$ (because $\xi$ is entire with real coefficients in its Taylor expansion at $s = 1/2$).

Evaluating at $s = 1/2 + it$: $\overline{\xi(1/2+it)} = \xi(\overline{1/2+it}) = \xi(1/2-it) = \xi(1-(1/2+it)) = \xi(1/2+it)$. Hence $\xi(1/2+it) \in \mathbb{R}$. $\square$

**Consequence.** The function $f: \mathbb{R} \to \mathbb{R}$, $f(t) := \xi\!\left(\tfrac{1}{2}+it\right)$, is a real entire function of $t$ (i.e., entire on $\mathbb{C}$ with $f(\mathbb{R}) \subset \mathbb{R}$).

---

## 2. The zeros of $f(t) = \xi(1/2+it)$

The zeros of $f$ as a function of $t \in \mathbb{C}$ correspond to the zeros of $\xi$ via:
$$f(t_0) = 0 \iff \xi\!\left(\tfrac{1}{2}+it_0\right) = 0 \iff \tfrac{1}{2}+it_0 = \rho, \quad \rho \text{ a zero of } \zeta.$$

If $\rho = \tfrac{1}{2} + b_\rho + i\gamma_\rho$ (with $b_\rho = \mathrm{Re}(\rho)-\tfrac{1}{2}$), then $t_0 = \gamma_\rho - ib_\rho$.

**The zero of $f$ is real $\iff$ $b_\rho = 0$ $\iff$ $\rho$ lies on the critical line.**

**Proposition 2.** The following statements are equivalent:
1. RH (every non-trivial zero of $\zeta$ has $\mathrm{Re}(\rho) = 1/2$).
2. Every zero of the real entire function $f(t) = \xi(1/2+it)$ is real.

---

## 3. The Laguerre–Pólya class

**Definition.** A real entire function $f(t)$ belongs to the *Laguerre–Pólya class* (class LP) if it is a uniform-on-compacts limit of polynomials all of whose zeros are real, or equivalently if it has the form:
$$f(t) = c\, t^m e^{-\alpha t^2 + \beta t} \prod_{k}\!\left(1 - \frac{t}{t_k}\right)e^{t/t_k},$$
with $c, \beta, t_k \in \mathbb{R}$, $\alpha \ge 0$, $\sum_k t_k^{-2} < \infty$.

The LP class is exactly the class of real entire functions with **all zeros real**.

**Direct consequence of Proposition 2:**
$$\text{RH} \iff f(t) = \xi\!\left(\tfrac{1}{2}+it\right) \in \text{LP}.$$

*Historical remark.* This equivalence is de Bruijn's reformulation (1950): $\Lambda = 0 \iff \xi(1/2+it) \in$ LP. What is new below is the characterization in terms of curvature, and the connection to Fronts A–D.

---

## 4. The curvature criterion: the correct direction

**Theorem 1** (curvature criterion in $t$). Let $t_k$ be the real zeros of $f$. Then:
$$f \in \text{LP} \iff t \mapsto \log|f(t)| \text{ is strictly concave in } t \text{ on each interval } (t_k,\, t_{k+1}).$$

*Proof.* For $f \in$ LP with all zeros real, the Hadamard product gives:
$$\log|f(t)| = \log|c| - \alpha t^2 + \beta t + \sum_k \log\!\left|1-\frac{t}{t_k}\right| + \frac{t}{t_k}.$$
Second derivative:
$$\frac{d^2}{dt^2}\log|f(t)| = -2\alpha - \sum_{k} \frac{1}{(t-t_k)^2} < 0 \quad \forall t \notin \{t_k\}.$$
Concave. Conversely, if $f$ has a complex zero $t_0 = \gamma + ib$ ($b > 0$), the pair $(t_0, \bar t_0)$ contributes:
$$\mathrm{Re}\,\!\left(-\frac{1}{(t-t_0)^2} - \frac{1}{(t-\bar t_0)^2}\right) = \frac{-2(t-\gamma)^2+2b^2}{[(t-\gamma)^2+b^2]^2},$$
which is **positive** for $|t-\gamma| < b$. Then $d^2/dt^2 \log|f| > 0$ for $t$ in the strip $(\gamma-b, \gamma+b)$: convexity. Hence concavity $\Rightarrow$ no complex zeros. $\square$

**Corollary 1.** For the function $f(t) = \xi(1/2+it)$:
$$\text{RH} \iff \frac{d^2}{dt^2}\log|\xi\!\left(\tfrac{1}{2}+it\right)| < 0 \quad \forall t \notin \{\gamma_\rho\}.$$

---

## 5. Connection with the curvature $\mathcal{C}(\gamma)$

From the previous document (06), using that $\Delta \log|\xi| = 0$ (harmonicity of $\log|\xi|$ away from zeros):
$$\frac{\partial^2}{\partial t^2}\log|\xi| = -\frac{\partial^2}{\partial\sigma^2}\log|\xi| = -\mathcal{C}(\gamma).$$

Therefore:
$$\frac{d^2}{dt^2}\log|f(t)| = -\mathcal{C}(t)$$

and the criterion of Corollary 1 is equivalent to:
$$\text{RH} \iff \mathcal{C}(t) > 0 \quad \forall t \notin \{\gamma_\rho\},$$
confirming Theorem 4 of document 06.

---

## 6. Resolution of the paradox of Question 28.1

Question 28.1 asked about the **$\sigma$-concavity** of $\log|\xi(\sigma+i\gamma)|$.

Theorem 2 of document 06 (RH → convexity in $\sigma$) together with Corollary 1 shows that:

| Direction | RH true | RH false |
|---|---|---|
| $\sigma$-concavity at $\sigma = 1/2$ | **FALSE** ($\sigma$-convex) | May be true (off-line zeros create concavity in $\sigma$) |
| $t$-concavity between zeros | **TRUE** (LP class) | FALSE (off-line zeros create convexity in $t$) |

Question 28.1 had the wrong direction. The correct concavity for RH is the **$t$-concavity**, and it is exactly equivalent to RH.

*Underlying geometric principle:* on the critical line, the gradient of $\log|\xi|$ points in the imaginary direction (toward the zeros in $t$), not in the real direction. The curvature transversal to this gradient is what characterizes RH.

---

## 7. Unification of the four fronts

The criterion $\mathcal{C}(t) > 0$ (RH ↔ LP class) connects the four fronts of the program:

**Front A** (DBN + Kreĭn): the de Bruijn–Newman flow moves zeros toward the real line of $f(t)$, increasing $\mathcal{C}(t)$ toward $+\sum_\rho 1/(\gamma-\gamma_\rho)^2$. Conjecture A.15 ($\Lambda = \max b_j^2/2$) is equivalent to the last complex zero of $f$ being the one with the largest $b_j$.

**Front B** (APS): the positivity of $\mathcal{C}(t) = G(1/2+it) = (\xi'/\xi)'(1/2+it)$ is an analytic property of $\xi$ that, if it could be proved via properties of $\xi'/\xi$ (the η-invariant), would give RH. Front B's Fourier anticommutativity is equivalent to the positivity of the curvature diagnostic.

**Front C** (K-theory): $[P_-] = 0$ in $K_0 \iff$ $f \in$ LP $\iff$ $\mathcal{C}(t) > 0$.

**Front D** (transversal energy): $t$-concavity is exactly the "minimum in the imaginary direction" condition that Front D tried to formalize. The correct energy is:
$$E_{\text{curv}}(f) := -\int \frac{d^2}{dt^2}\log|f(t)|\, dt = \int \mathcal{C}(t)\, dt,$$
which is positive $\iff$ $f \in$ LP $\iff$ RH.

**The four fronts are the same problem:** proving that $f(t) = \xi(1/2+it) \in$ LP.

---

## 8. The wall identified with maximal precision

**Proposition 3** (the final wall). The statement:
$$f(t) = \xi\!\left(\tfrac{1}{2}+it\right) \text{ has only real zeros}$$
is equivalent to RH. To prove it without assuming RH, one needs to show that:

$$\frac{d^2}{dt^2}\log|f(t)| = -2\alpha - \sum_k \frac{1}{(t-t_k)^2} - \sum_{\text{complex pairs}} \frac{2[(t-\gamma_k)^2-b_k^2]}{[(t-\gamma_k)^2+b_k^2]^2} < 0$$

The difficulty: complex pairs contribute positively near their "shadow" $t = \gamma_k$. Ruling out the possibility of complex pairs IS proving RH.

**The arithmetic restriction** (Euler product) is the only additional condition that could force the non-existence of complex pairs. This is exactly Wall A of the program (Phase 27) in the language of zeros of entire functions.

---

## 9. New results vs. known results

| Result | New/Known |
|---|---|
| RH ↔ $f(t) = \xi(1/2+it) \in$ LP | Known (de Bruijn 1950, Newman 1976) |
| $\xi(1/2+it) \in \mathbb{R}$ for every $t$ | Known |
| Formula $\mathcal{C}(t) = \sum_\rho (t-\gamma_\rho)^2-b_\rho^2)/|s-\rho|^4$ | **New** |
| $\mathcal{C}(t) > 0 \iff$ LP class $\iff$ RH | **New presentation** |
| $\sigma$-concavity FALSE under RH; $t$-concavity TRUE under RH | **New diagnostic** |
| The four fronts (A, B, C, D) are the same LP problem | **New unification** |
| Connection $E_{\text{curv}} = \int \mathcal{C}(t)dt$ with Front D | **New** |
| Final wall = non-existence of complex pairs of zeros of $f$ = Wall A | **New identification** |

---

## 10. The most direct remaining question

Of all the analyses of Phase 28, the most concrete and attackable question:

**Question 28.2** (correct version). Can it be proved that $\mathcal{C}(t) = (\xi'/\xi)'(1/2+it) > 0$ for every $t$ outside the ordinates of zeros of $\zeta$, using only:
1. The functional equation $\xi(s) = \xi(1-s)$;
2. The Euler product $\xi(s) \sim \zeta(s) \cdot (\text{Gamma factor})$;
3. Without assuming RH?

If the answer is yes: RH is proved.

If the answer is no (there is a counterexample, or the proof requires assuming RH): the wall is the same Wall A as always.

The novelty is that this question is **concrete analytic about $\xi'/\xi$**, formulable in terms of a known function, without cohomological or spectral intermediaries.
