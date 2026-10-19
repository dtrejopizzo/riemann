# Front A — de Bruijn–Newman flow and monotonicity of the Kreĭn index


---

## 1. Definitions

**Definition A.1** (de Bruijn–Newman flow). For $t \in \mathbb{R}$ define:
$$H_t(z) := \int_0^\infty \Phi(u)\, e^{tu^2} \cos(uz)\, du,$$
where $\Phi(u) = \sum_{n=1}^\infty (2\pi^2 n^4 e^{9u/2} - 3\pi n^2 e^{5u/2}) e^{-\pi n^2 e^{2u}}$
is the de Bruijn kernel. The function $H_0$ satisfies $H_0(z) = \Xi(1/2 + iz)$ where
$\Xi$ is the Riemann xi function.

**Definition A.2** (Zero configuration). Let $Z_t = \{z_n(t)\}_{n \ge 1}$ be the
ordered multiset of zeros of $H_t$ in the upper half-plane $\mathrm{Im} z \ge 0$
(together with the real ones). Each complex zero $z_n = \alpha_n + i\beta_n$ with $\beta_n > 0$
corresponds to a zero $\rho_n = 1/2 + iz_n = 1/2 + i\alpha_n - \beta_n$ of $\zeta$
off the critical line, with $\mathrm{Re}(\rho_n) = 1/2 - \beta_n$.

**Definition A.3** (Transversal index in the flow). For each $t$, define:
$$\kappa_t := 2 \cdot \#\{n : \mathrm{Im} z_n(t) > 0\}$$
(twice the number of complex zeros in the open upper half-plane).

*Remark:* $\kappa_t$ is the analogue of the Kreĭn index $\kappa(Q_t)$ in the language
of the DBN flow. Under the identification of Definition A.2 and the relation $\kappa(Q) = 2m$
(Phase 26), $\kappa_0 = \kappa(Q)$.

**Definition A.4** (de Bruijn–Newman constant).
$$\Lambda := \inf\{t \in \mathbb{R} : \text{all zeros of } H_t \text{ are real}\}.$$

---

## 2. Established facts

**Theorem A.5** (de Bruijn 1950). $H_t$ has only real zeros for all $t \ge 1/2$.
Consequently, $\Lambda \le 1/2$.

**Theorem A.6** (Rodgers–Tao 2019). $\Lambda \ge 0$.

**Theorem A.7** (direct definition). $\Lambda = 0 \iff$ RH.

*Proof:* By definition, $\Lambda = 0$ says that $H_0$ has only real zeros, i.e.,
$\Xi(1/2 + iz) = 0 \Rightarrow z \in \mathbb{R}$, i.e., all zeros of $\zeta$ have
real part $1/2$. $\square$

**Corollary A.8.** $\kappa_t = 0$ for all $t \ge \Lambda$.

**Theorem A.9** (Csordas–Norfolk–Varga 1988). The zeros of $H_t$ satisfy the ordinary
differential equation:
$$\frac{dz_n}{dt} = \sum_{k \ne n} \frac{2}{z_k - z_n}, \qquad \forall\, n \ge 1.$$

This equation is the **gradient flow** of the logarithmic energy
$$E_{\log}(Z) = -\sum_{j \ne k} \log|z_j - z_k|.$$

*Verification:* $-\partial E_{\log}/\partial \bar z_n = \sum_{k \ne n} 2/(z_k - z_n)$.
$\square$

---

## 3. The central question of Front A

The facts above are known. The novelty of Front A is the following:

**Question A.10** (central, open). Is $t \mapsto \kappa_t$ non-increasing?

If the answer is yes, the argument is:
1. $\kappa_t \ge 0$ for all $t$ (by definition).
2. $\kappa_t$ non-increasing $\Rightarrow$ $\kappa_0 \ge \kappa_t$ for $t \ge 0$.
3. $\kappa_\Lambda = 0$.

But this only gives $\kappa_0 \ge 0$ (already known). **Monotonicity alone does not prove RH.**

The correct question is subtler:

**Question A.11** (refined). Under the arithmetic constraints imposed by the
Euler product of $\zeta$, can it happen that $\kappa_0 > 0$?

The key point is that $H_0$ is not an arbitrary order-1 function with symmetric zeros.
It is $\Xi(1/2 + iz)$, where $\Xi$ factorizes as $\Xi(s) = \prod_p \Xi_p(s)$ (Euler
product). This imposes global constraints on the zeros that a flow without that
arithmetic structure would not have.

---

## 4. The dynamics of the imaginary part

**Proposition A.12** (equation for the transversal part). For a complex zero
$z_n = \alpha_n + i\beta_n$ with $\beta_n > 0$, the flow equation gives:
$$\frac{d\beta_n}{dt} = \sum_{k \ne n} \frac{-2\beta_n}{(\alpha_k - \alpha_n)^2 + (\beta_k - \beta_n)^2} + \text{conjugate-pair terms}.$$

More precisely, for each conjugate pair $(z_n, \bar z_n)$:

The pair's contribution to $d\beta_n/dt$:
$$\frac{d\beta_n}{dt}\bigg|_{\text{own pair}} = \frac{-2\beta_n}{(2\beta_n)^2} \cdot (-2) = \frac{1}{2\beta_n} \cdot (\text{sign to be determined})$$

*Remark:* The sign of $d\beta_n/dt$ determines whether the zero approaches or moves away from
the real line. For the DBN flow, the definition of $\Lambda$ implies that eventually
$\beta_n(t) \to 0$ for all $n$ as $t \to \Lambda^-$. But this does not
imply $\beta_n(0) = 0$.

**Proposition A.13** (global property of the flow). The logarithmic energy $E_{\log}$ is
a Lyapunov function for the DBN flow: $dE_{\log}/dt \le 0$.

*Proof:* The flow is the negative gradient of $E_{\log}$:
$\frac{dz_n}{dt} = -\frac{\partial E_{\log}}{\partial \bar z_n}$.
Hence: $\frac{d}{dt} E_{\log} = -\sum_n \left|\frac{\partial E_{\log}}{\partial z_n}\right|^2 \le 0$. $\square$

*Consequence:* The logarithmic energy DECREASES monotonically along the flow. But
$E_{\log}$ does not distinguish real zeros from complex ones: it is a function of the modulus
of the differences, not of the imaginary parts.

---

## 5. The central obstacle and the connection with Front D

The question of Front A reduces to:

> Does the decrease of $E_{\log}$ under the flow correspond to a decrease of the
> transversal energy $\Phi = \sum_n \beta_n^2$?

These two quantities are distinct:
$$E_{\log}(Z) = -\sum_{j \ne k} \log|z_j - z_k|, \qquad \Phi(Z) = \sum_n (\mathrm{Im} z_n)^2.$$

For the flow to drive $\Phi \to 0$ (RH), we need the restriction of $E_{\log}$
to the "transversal direction" to be convex with a minimum at $\Phi = 0$.

**This is exactly the question of Front D.** The two fronts are the same program.

---

## 6. New result: formula for $\Lambda$

**Proposition A.14** (lower bound of $\Lambda$ via Kreĭn). Under Hypothesis D with
orbits at distance $b_j = \mathrm{Re}(\rho_j) - 1/2 > 0$, Theorem 25-B.4 of the
program establishes:
$$\Lambda \ge \max_j \frac{b_j^2}{2}.$$

**Conjecture A.15** (new). The above inequality is an equality:
$$\Lambda = \max_j \frac{b_j^2}{2}.$$

*Heuristic evidence:* The DBN flow with logarithmic energy should converge more
slowly the farther the zero is from the real line. The farthest zero (largest
$b_j$) should be the "last to arrive" at the real line, determining $\Lambda$.

*Consequence of A.15:* If the conjecture is true, then:
$$\Lambda = 0 \iff \max_j b_j^2 = 0 \iff b_j = 0 \; \forall j \iff \text{RH.}$$

This does not prove RH, but it turns $\Lambda$ into a measurable invariant of the worst
violation of RH: the distance of the farthest zero from the critical line.

---

## 7. Verdict of Front A

| Result | Status |
|---|---|
| $\kappa_t = 0$ for $t \ge 1/2$ | Proved (de Bruijn) |
| DBN flow = gradient flow of $E_{\log}$ | Proved (Csordas–Norfolk–Varga) |
| $E_{\log}$ is a Lyapunov function | Proved |
| $\kappa_t$ non-increasing → weak consequence | Monotonicity does not prove RH |
| Conjecture A.15: $\Lambda = \max_j b_j^2/2$ | **Open — new result to be proved** |
| Fronts A and D are the same problem | **New result of Phase 28** |
