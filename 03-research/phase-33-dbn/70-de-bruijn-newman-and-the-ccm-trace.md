# Document 70 — De Bruijn-Newman and the CCM trace: $\Lambda$ as the extinction time of $T_\lambda(t)$

**Program:** Riemann Hypothesis — Phase 33 DBN-CCM
**Prerequisites:** Docs 59–69 (Phase 32), especially Doc 64 (PTC) and Doc 68 (exact Wronskian)

---

## 1. Motivation: connecting two reformulations of RH

We have two equivalences:

**PTC (Doc 64):** RH $\iff T_\lambda = 0$ for all $\lambda > 0$.

**De Bruijn-Newman:** RH $\iff \Lambda \leq 0$ (and Rodgers-Tao 2018: $\Lambda \geq 0$, hence RH $\iff \Lambda = 0$).

The natural question is: is there a way to express $\Lambda$ in terms of the trace $T_\lambda$?

---

## 2. The De Bruijn-Newman flow

### 2.1. Standard definition

The De Bruijn-Newman function with parameter $t \in \mathbb{R}$ is

$$H_t(z) = \int_0^\infty e^{tu^2}\, \Phi(u)\cos(zu)\, du,$$

where $\Phi(u) = \sum_{n=1}^\infty (2\pi^2 n^4 e^{9u/2} - 3\pi n^2 e^{5u/2}) e^{-\pi n^2 e^{2u}}$ is the Jacobi theta kernel. For $t = 0$: $H_0(z) = \Xi(z/2)$ (the Riemann xi function).

The De Bruijn-Newman constant is defined as

$$\Lambda = \inf\{t \in \mathbb{R} : H_t \text{ has all its zeros real}\}.$$

Known facts: $-\infty < \Lambda \leq 1/2$ (De Bruijn 1950), $\Lambda \geq 0$ (Rodgers-Tao 2018), RH $\iff \Lambda = 0$.

### 2.2. Dynamics of the zeros under the flow

The zeros of $H_t$, denoted $\{z_n(t)\}$, satisfy the equation of motion (valid while they are simple):

$$\frac{dz_n}{dt} = \sum_{m \neq n} \frac{-2}{z_n(t) - z_m(t)}.$$

For $t > \Lambda$, all zeros are real and *repel* each other (Dyson-Calogero-Moser dynamics). Real zeros satisfy $\dot{z}_n > 0$ if $z_n$ is the local maximum of the zero density, indicating dispersion.

For $t < \Lambda$, there are complex zeros $z_n = \alpha_n + i\beta_n$ with $\beta_n \neq 0$ that "fall" toward the real line as $t \to \Lambda$.

---

## 3. The parametrized trace $T_\lambda(t)$

### 3.1. $t$-dependent measures

For each $t \geq 0$, we define the deformed full measure:

$$dm_{full}^t(s) = dm_\infty(s) \cdot |H_t(s)|^2 \cdot C_t^{-1},$$

where $C_t = \int |H_t(s)|^2\, dm_\infty(s)$ is the normalization constant. The measure $dm_{full}^{t=0} = dm_{full}$ is the measure of Doc 64 (before normalization).

The "on-critical" reference measure for the parameter $t$:

$$dm_{full,on}^t(s) = dm_\infty(s) \cdot |H_t^{on}(s)|^2 \cdot C_t^{-1},$$

where $H_t^{on}$ is built from $H_t$ by reflecting all its complex zeros onto the real line (the map $\rho \mapsto \frac{1}{2} + i\mathrm{Im}(\rho)$).

**Remark 3.1.** For $t > \Lambda$: all zeros of $H_t$ are real, so $H_t = H_t^{on}$ and $dm_{full}^t = dm_{full,on}^t$. By Prop. 2.1 of Doc 64 and Thm. 3.1: $T_\lambda(t) = 0$ for all $\lambda$.

### 3.2. Definition of the deformed trace

$$T_\lambda(t) := \sum_{n:\, \gamma_n(t) \leq \lambda} \left(\Delta_n^{full,t} - \Delta_n^{full,on,t}\right),$$

where $\Delta_n^{full,t} = (a_n^{full,t})^2 - (a_n^\infty)^2$ is the discrepancy of the Jacobi coefficients of $dm_{full}^t$ relative to the archimedean measure.

**Proposition 3.2** (Consistency with the PTC). Thm. 3.1 of Doc 64 applies to each fixed $t$: $T_\lambda(t) = 0$ for all $\lambda$ if and only if $dm_{full}^t = dm_{full,on}^t$, i.e., if and only if all zeros of $H_t$ are real.

*Proof.* Identical to that of Doc 64, replacing $H_0$ by $H_t$. $\square$

---

## 4. $\Lambda$ as the extinction time of $T_\lambda(t)$

### 4.1. The central statement

**Theorem 4.1** (Characterization of $\Lambda$ via the CCM trace).

$$\Lambda = \inf\{t \geq 0 : T_\lambda(t) = 0 \text{ for all } \lambda > 0\}.$$

*Proof.*

**"$\leq$":** If $t > \Lambda$, all zeros of $H_t$ are real, so $T_\lambda(t) = 0$ for all $\lambda$ (Rem. 3.1). Hence $\{t : T_\lambda(t) = 0 \ \forall\lambda\} \supseteq (\Lambda, \infty)$, and the infimum of the left-hand set is $\leq \Lambda$.

**"$\geq$":** If $t < \Lambda$, then $H_t$ has at least one complex zero $z_0 = \alpha_0 + i\beta_0$ with $\beta_0 \neq 0$. The argument of Cor. 7.5 of Doc 63 (now with $H_t$ instead of $H_0$) shows that $T_\lambda(t) > 0$ for $\lambda$ sufficiently large. (The proof is identical: $W_\lambda \geq 0$, the correction is absolutely continuous and nonzero, so the integral is positive.) Hence $t \notin \{t : T_\lambda(t) = 0 \ \forall\lambda\}$, and the infimum of the right-hand set is $\geq \Lambda$. $\square$

### 4.2. Reformulation of RH

Since $\Lambda \geq 0$ (Rodgers-Tao) and $\Lambda \leq 1/2$ (De Bruijn), Theorem 4.1 gives:

$$\text{RH} \iff \Lambda = 0 \iff T_\lambda(0) = 0 \text{ for all } \lambda > 0.$$

This is not new relative to the PTC of Doc 64 (it is the same equivalence at $t = 0$). What is new is that $\Lambda$ has a concrete spectral-variational description:

> **$\Lambda$ is the minimum time at which the CCM discrepancy trace becomes extinct.**

---

## 5. Monotonicity of $T_\lambda(t)$

### 5.1. The question

Is $T_\lambda(t)$ monotonically decreasing in $t$?

If $\partial_t T_\lambda(t) \leq 0$, the trace "converges to zero from above" as $t \to \Lambda^+$, which would give a more precise picture of the constant $\Lambda$.

### 5.2. The time-derivative formula

Differentiating $T_\lambda(t) = \int W_\lambda(s)\,(dm_{full}^t - dm_{full,on}^t)(s)$ with respect to $t$:

$$\partial_t T_\lambda(t) = \int W_\lambda(s)\, \partial_t(dm_{full}^t - dm_{full,on}^t)(s).$$

The derivative $\partial_t dm_{full}^t$ is computed using $\partial_t H_t = \partial_{ss} H_t$ (heat equation):

$$\partial_t |H_t(s)|^2 = 2\mathrm{Re}(\overline{H_t(s)}\, \partial_t H_t(s)) = 2\mathrm{Re}(\overline{H_t(s)}\, H_t''(s)).$$

Integrating by parts (using $W_\lambda$ smooth):

$$\partial_t T_\lambda(t) = 2\int W_\lambda(s)\mathrm{Re}(\overline{H_t}\, H_t'' - \overline{H_t^{on}}\, (H_t^{on})'')\, dm_\infty(s).$$

Integrating by parts in $s$ (the derivative acts on $W_\lambda$):

$$\partial_t T_\lambda(t) = -2\int W_\lambda'(s)\mathrm{Re}(\overline{H_t}\, H_t' - \overline{H_t^{on}}\, (H_t^{on})')\, dm_\infty(s) + \text{boundary}.$$

### 5.3. The sign of the derivative: analysis via zeros

For $t > \Lambda$, $H_t$ has all zeros real, so $H_t = H_t^{on}$ and $\partial_t T_\lambda(t) = 0$ consistently.

For $t < \Lambda$, the complex zeros of $H_t$ induce a nonzero perturbation. The equation of motion of the zeros (§2.2) describes the dynamics: the complex zeros move toward the real line as $t$ increases, reducing the contribution of the off-critical correction.

**Conjecture 5.1** (Monotonicity). For $0 \leq t_1 < t_2$:
$$T_\lambda(t_1) \geq T_\lambda(t_2) \geq 0.$$

This conjecture is plausible because:
- The heat flow "regularizes" $H_t$: it disperses the zeros away from the real line toward it.
- The quantity $dm_{full}^t - dm_{full,on}^t$ measures exactly how much the zeros of $H_t$ deviate from the real line, and this deviation decreases with $t$.

*Status:* a conjecture, not proved in this document. Its proof would require controlling $\mathrm{Re}(\overline{H_t}H_t'' - \overline{H_t^{on}}(H_t^{on})'')$ on the support of $dm_\infty$, which involves estimates on the distribution of the complex zeros of $H_t$.

---

## 6. Lower bound for $\Lambda$

### 6.1. Quantitative relation

If monotonicity (Conj. 5.1) holds, then for $t < \Lambda$:

$$T_\lambda(0) \geq T_\lambda(t) \geq 0.$$

From Cor. 7.5 of Doc 63 (adapted to $H_t$ with its dominant complex zero $z_0(t) = \alpha_0(t) + i\beta_0(t)$):

$$T_\lambda(t) \geq c_0 \cdot N(\lambda) \cdot w(\alpha_0(t)) \cdot |\beta_0(t)|^2,$$

where $|\beta_0(t)|$ is the size of the imaginary part of the zero closest to the real line.

Taking $t \to \Lambda^-$ and using $|\beta_0(\Lambda)| = 0$ (the zeros reach the real line exactly at $t = \Lambda$):

$$T_\lambda(0) \geq T_\lambda(\Lambda^-) = 0.$$

This is consistent but gives no new information about $\Lambda$.

### 6.2. The extinction rate as information about $\Lambda$

The new information would come from the **extinction rate**: if $T_\lambda(t) \sim C(\lambda) \cdot (\Lambda - t)^\alpha$ as $t \to \Lambda^-$, then $\alpha$ and $C(\lambda)$ encode quantitative information about $\Lambda$.

For the simplest model (a single complex zero at $z_0 = \alpha_0 + i\beta_0$ with trajectory $\beta_0(t) \sim \sqrt{2(\Lambda - t)}$ under the Dyson dynamics):

$$T_\lambda(t) \sim c \cdot N(\lambda) \cdot (\Lambda - t), \qquad t \to \Lambda^-.$$

Hence:

$$\Lambda = \lim_{t \to \Lambda^-} \frac{T_\lambda(t)}{c \cdot N(\lambda)}.$$

This is a way to "measure" $\Lambda$ via the CCM trace, although it requires knowing the trajectory of the zeros (which is a priori information as difficult as RH).

---

## 7. An upper bound for $\Lambda$ via the PTC

### 7.1. Statement

**Proposition 7.1** (Upper bound for $\Lambda$). If there exists $t_0 \geq 0$ such that $T_\lambda(t_0) = 0$ for all $\lambda > 0$, then $\Lambda \leq t_0$.

*Proof.* From Thm. 4.1, if $T_\lambda(t_0) = 0$ for all $\lambda$, then $t_0 \in \{t : T_\lambda(t) = 0 \ \forall\lambda\}$, so $\inf \geq t_0$... wait, the infimum of that set is $\leq t_0$, which implies $\Lambda \leq t_0$. $\square$

### 7.2. Practical consequence

To prove RH ($\Lambda = 0$) it suffices to prove $T_\lambda(0) = 0$ for all $\lambda$ (this is the PTC of Doc 64). Prop. 7.1 does not give a new path, but it reformulates the strategy: instead of working directly with $\Lambda$, one studies whether there is an arbitrarily small $t_0$ with $T_\lambda(t_0) = 0$.

---

## 8. The connection with the discrete Toda equation

### 8.1. The induced Jacobi flow

The flow $t \mapsto dm_{full}^t$ induces a flow $t \mapsto \{a_n^{full,t}\}_{n\geq 0}$ on the Jacobi coefficients. The natural question is what equation $(a_n^{full,t})_{n,t}$ satisfies.

For measures evolving according to the heat equation, the induced evolution on the Jacobi coefficients is related to the **Toda chain**:

$$\dot{a}_n = a_n(b_{n+1} - b_n), \qquad \dot{b}_n = 2(a_n^2 - a_{n-1}^2),$$

where $b_n$ are the diagonal coefficients (which are zero for symmetric measures at $t = 0$).

For symmetric measures (like ours, where $dm_\infty$ is even and $|H_t|^2$ is even): $b_n = 0$ for all $t$. The Toda chain reduces to:

$$\dot{a}_n = 0 \cdot (0 - 0) = 0?$$

No, this is incorrect: the Toda chain for symmetric measures with $b_n = 0$ has $\dot{b}_n = 2(a_n^2 - a_{n-1}^2) \neq 0$ in general, which generates $b_n \neq 0$ for $t > 0$. The symmetry $b_n = 0$ is broken under the flow (unless the $a_n$ are constant).

**Remark 8.1.** The De Bruijn-Newman flow does *not* preserve the symmetry of the measure. For $t > 0$, the measure $dm_{full}^t$ may lose the symmetry $s \mapsto -s$, which introduces $b_n \neq 0$ in the Jacobi chain. This complicates the analysis.

### 8.2. The small-$t$ case: linear perturbation

For $t \ll 1$, we expand $H_t \approx H_0 + t H_0'' + O(t^2)$:

$$|H_t|^2 \approx |H_0|^2 + 2t\mathrm{Re}(\overline{H_0} H_0'') + O(t^2).$$

The first-order correction to $dm_{full}^t$ is:

$$\delta dm^{(1)}(s) = 2t\mathrm{Re}(\overline{H_0(s)} H_0''(s)) dm_\infty(s) \cdot C_0^{-1}.$$

By the CD representation (Doc 61, Thm. 2.1), the first-order correction to $(a_n^{full,t})^2$ is:

$$\delta(a_n^2)^{(1)} = 2t \int (|P_{n+1}|^2 - |P_n|^2) \mathrm{Re}(\overline{H_0} H_0'') dm_\infty.$$

Using integration by parts ($H_0'' = -\mathcal{L}_0 H_0$ where $\mathcal{L}_0$ is the Schrödinger operator):

$$\delta(a_n^2)^{(1)} = -2t \int (|P_{n+1}|^2 - |P_n|^2) \mathrm{Re}(\overline{H_0} \mathcal{L}_0 H_0) dm_\infty.$$

Expanding $H_0 = \sum_k c_k P_k$ (where $c_k = \langle \Xi, P_k \rangle_{dm_\infty}$, as in Doc 65):

$$\mathrm{Re}(\overline{H_0} \mathcal{L}_0 H_0) = \mathrm{Re}\,\left(\sum_{k,l} \bar{c}_k c_l P_k \mathcal{L}_0 P_l\right) = \mathrm{Re}\,\left(\sum_k |c_k|^2 \mu_k P_k^2 + \text{cross terms}\right),$$

where $\mu_k$ are the eigenvalues of $\mathcal{L}_0$ on $P_k$ (Doc 65, §2.3).

**Proposition 8.2** (Time derivative of the trace at $t = 0$).

$$\partial_t T_\lambda \bigg|_{t=0} = -4\int W_\lambda(s) \mathrm{Re}(\overline{H_0(s)} H_0''(s)) dm_\infty(s).$$

If this derivative is negative (which would require $\mathrm{Re}(\overline{H_0}H_0'') > 0$ on the support of $W_\lambda$, i.e., that $H_0$ and $H_0''$ have real part of the same sign), then $T_\lambda(t)$ decreases initially, consistent with Conj. 5.1.

---

## 9. Conditional result: a quantitative bound for $\Lambda$

**Theorem 9.1** (Lower bound for $\Lambda$ via $T_\lambda(0)$, conditional on Conj. 5.1).

Assuming the monotonicity of Conj. 5.1, for all $\lambda > 0$ and all $t < \Lambda$:

$$T_\lambda(0) \geq T_\lambda(t) \geq c_0 \cdot N(\lambda) \cdot (2\pi)^{-2}|\Gamma(1/4 + i\alpha_0/2)|^2 \cdot |\beta_0(t)|^2,$$

where $z_0(t) = \alpha_0(t) + i\beta_0(t)$ is the zero of $H_t$ closest to the real line.

*Consequence:* if $T_\lambda(0) = o(N(\lambda))$ as $\lambda \to \infty$, then $\Lambda = 0$ (RH).

This is the first statement connecting RH to a *quantitative* condition on the growth rate of $T_\lambda(0)$. However, it still depends on the unproved monotonicity.

---

## 10. Summary and direction for Doc 71

**Central result (unconditional):**
$$\Lambda = \inf\{t \geq 0 : T_\lambda(t) = 0 \;\forall\lambda > 0\}.$$

This is a new characterization of the De Bruijn-Newman constant in terms of the CCM-Jacobi formalism.

**Conditional result (assuming Conj. 5.1):** $T_\lambda(0) = o(N(\lambda)) \implies \Lambda = 0$.

**Still open:**
1. Prove the monotonicity $\partial_t T_\lambda(t) \leq 0$.
2. Compute $\partial_t T_\lambda(0)$ explicitly in terms of $c_k = \langle\Xi, P_k\rangle$.
3. Connect the Jacobi dynamics with the Toda or Ablowitz-Ladik chain.

**Doc 71** should address point 2: the derivative $\partial_t T_\lambda(0)$ is explicit via Prop. 8.2 and the coefficients $c_k$. If $\partial_t T_\lambda(0) < 0$ under $\neg$RH, this would give a differential condition on $T_\lambda$ that bounds $\Lambda$ from below.

---

*End of Document 70.*
