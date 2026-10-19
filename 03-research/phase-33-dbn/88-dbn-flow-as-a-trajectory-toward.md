# Document 88 — The DBN flow as a trajectory toward the Hadamard-critical manifold

**Program:** Riemann Hypothesis — Phase 33 DBN-CCM  
**Prerequisites:** Docs 70, 71, 76, 79, 82, 85

---

## Summary

The previous documents of Path 3 have established two unconditional results — the completeness of the linear span of $\{e^{i\gamma_n s}\}$ in $L^2(W_\lambda dm_\infty)$ (Doc 85) and the variational reformulation $\tilde\delta_\lambda^2 = 0 \iff$ RH (Doc 82) — and have identified the precise barrier: the Hadamard-critical manifold $M = \{|\eta_{on}|^2 : \eta_{on} \text{ Hadamard-critical}\}$ is a non-linear submanifold of infinite codimension within the linear approximation space. The present document explores whether the De Bruijn-Newman flow, which already acted as a bridge between $\Lambda$ and the trace $T_\lambda$ in Doc 70, provides additional useful geometry: the trajectory $t \mapsto |\Xi_t|^2$ in $L^2(W_\lambda dm_\infty)$ enters $M$ exactly at $t = \Lambda$.

§1 establishes that $t \mapsto f_t := |\Xi_t|^2$ defines an analytic curve in $L^2(W_\lambda dm_\infty)$. §2 computes the derivative $\partial_t f_t|_{t=0}$ and connects it with the already known formula of Prop. 8.2 of Doc 70. §3 introduces the tangency condition to $M$ and shows its relation to RH. §4 proves that the trace $T_\lambda(t)$ is continuous in $t$ and establishes the equivalence $T_\lambda(t) = 0 \iff$ all zeros of $\Xi_t$ are real (extension of the CTP to each $t$). §5 studies the flow as a homotopy between $f_0$ and the manifold $M$. §6 examines the behavior of the trajectory as $t \to \infty$. §7 frankly analyzes the conjectural flow strategy and why it does not produce a proof of RH. §8 synthesizes Path 3 and formulates the residual obstacle.

---

## §1. The curve $t \mapsto f_t$ in $L^2(W_\lambda\,dm_\infty)$

### 1.1. Definition of the flow and notation

We recall from Doc 70 (§2.1) that the deformed De Bruijn-Newman function is

$$\Xi_t(s) = \int_{-\infty}^\infty e^{tu^2}\Phi(u)\,e^{isu}\,du, \qquad t \geq 0,$$

where

$$\Phi(u) = \sum_{n=1}^\infty \bigl(2\pi^2 n^4 e^{9u/2} - 3\pi n^2 e^{5u/2}\bigr)\,e^{-\pi n^2 e^{2u}}$$

is the Jacobi theta kernel. For $t = 0$: $\Xi_0 = \Xi$ (the standard Riemann xi function, $\Xi(s) = \frac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)|_{s=1/2+is}$ in the imaginary variable). For $t > \Lambda$: all zeros of $\Xi_t$ are real (De Bruijn 1950).

We define the curve

$$f_t : s \mapsto |\Xi_t(s)|^2, \qquad t \geq 0.$$

### 1.2. The curve takes values in $L^2(W_\lambda\,dm_\infty)$

**Proposition 1.1.** *For each $t \geq 0$, $f_t \in L^2(W_\lambda\,dm_\infty)$.*

*Proof.* The factor $e^{tu^2}$ multiplies the integrand of $\Xi_t$. The function $\Phi$ decays super-exponentially: by the estimate of Doc 70 (§2.1), $|\Phi(u)| = O(e^{-\pi e^{2u}})$ as $u \to +\infty$ and $|\Phi(u)| = O(e^{5|u|/2})$ as $u \to -\infty$, so that $|e^{tu^2}\Phi(u)| \leq C_T e^{-\pi e^{2u}/2}$ for $u \geq 0$ and $|e^{tu^2}\Phi(u)| \leq C_T e^{(t+1)u^2}$ for $u \leq 0$, with constant $C_T$ uniform in $t \in [0,T]$. By the Riemann-Lebesgue theorem applied to the Fourier transform of the integrand (which is integrable in $u$), $\Xi_t(s)$ decays rapidly as $|s| \to \infty$. In particular, $|f_t(s)| = O(e^{-c|s|})$ for some $c > 0$ depending on $t$. The measure $dm_\infty$ has density $w(s) \sim |s|^{-1/2}e^{-\pi|s|/2}$ and the weight $W_\lambda$ is bounded, so $\int W_\lambda f_t^2\,dm_\infty < \infty$. $\square$

### 1.3. Analyticity in $t$

**Proposition 1.2.** *The curve $t \mapsto \Xi_t$ in $L^2(W_\lambda\,dm_\infty)$ is real-analytic in $t \geq 0$, and consequently $t \mapsto f_t = |\Xi_t|^2$ is real-analytic in $L^2(W_\lambda\,dm_\infty)$.*

*Proof.* To differentiate under the integral sign in the $L^2(W_\lambda\,dm_\infty)$ norm it suffices to verify that $\partial_t^k e^{tu^2} = u^{2k}e^{tu^2}$ and that the estimates $\|u^{2k}e^{Tu^2}\Phi(u)\|_{L^1(du)} < \infty$ for all $k \geq 0$ and $T < \infty$ are satisfied by the super-exponential decay of $\Phi$. The convergence of the Taylor series $\Xi_t = \sum_{k=0}^\infty \frac{t^k}{k!}\int u^{2k}\Phi(u)e^{isu}\,du$ in the norm of $L^2(W_\lambda\,dm_\infty)$ follows from the dominated convergence theorem and the estimate uniform in $s$ of the terms. The analyticity of $f_t = |\Xi_t|^2 = \Xi_t\overline{\Xi_t}$ is obtained from that of $\Xi_t$ by bilinearity. $\square$

### 1.4. The Hadamard-critical manifold as a subset of $L^2(W_\lambda\,dm_\infty)$

We recall from Doc 82 (§3) that the Hadamard-critical manifold is

$$M := \bigl\{|\eta_{on}|^2 : \eta_{on} \text{ is an entire function of order 1 with all its zeros on }\mathrm{Re}(\rho) = 1/2\bigr\} \cap L^2(W_\lambda\,dm_\infty).$$

More precisely, $\eta_{on}$ is a Hadamard-critical function if it has the same Hadamard factorization as $\Xi$ but with all its zeros projected onto the critical line: $\eta_{on}(s) = e^{A+Bs}\prod_n (1 - s/\gamma_n)e^{s/\gamma_n}$ where all the $\gamma_n$ are real.

**Proposition 1.3.** *For $t > \Lambda$: $f_t \in M$. For $t \in [0,\Lambda)$: $f_t \notin M$.*

*Proof.* For $t > \Lambda$: all zeros of $\Xi_t$ are real by definition of $\Lambda$, so $\Xi_t$ is Hadamard-critical and $f_t = |\Xi_t|^2 \in M$. For $t \in [0,\Lambda)$: by definition of $\Lambda$, $\Xi_t$ has at least one zero with non-zero imaginary part, so $f_t \notin M$. $\square$

The trajectory $t \mapsto f_t$ enters $M$ exactly at $t = \Lambda$: it is the first time at which the curve touches the Hadamard-critical manifold.

---

## §2. The derivative of the flow at $t = 0$

### 2.1. Computing $\partial_t\Xi_t|_{t=0}$

Differentiating under the integral sign:

$$\partial_t \Xi_t\big|_{t=0} = \int_{-\infty}^\infty u^2\Phi(u)\,e^{isu}\,du.$$

On the other hand, the second derivative of $\Xi_0 = \Xi$ with respect to $s$ is

$$\Xi_0''(s) = \frac{d^2}{ds^2}\int \Phi(u)e^{isu}\,du = \int (iu)^2\Phi(u)e^{isu}\,du = -\int u^2\Phi(u)e^{isu}\,du.$$

Therefore:

$$\partial_t\Xi_t\big|_{t=0} = -\Xi_0''(s).$$

### 2.2. The derivative of $f_t$ at $t = 0$

**Proposition 2.1.** *The derivative of the curve $f_t = |\Xi_t|^2$ at $t = 0$ is*

$$\partial_t f_t\big|_{t=0} = 2\mathrm{Re}\,\bigl[\overline{\Xi_0(s)}\,\partial_t\Xi_t|_{t=0}\bigr] = -2\mathrm{Re}\,\bigl[\overline{\Xi_0(s)}\,\Xi_0''(s)\bigr].$$

*Explicitly:* $\partial_t f_t|_{t=0} = -2\bigl[\mathrm{Re}(\Xi_0)\mathrm{Re}(\Xi_0'') + \mathrm{Im}(\Xi_0)\mathrm{Im}(\Xi_0'')\bigr].$

*Proof.* Chain rule for $|\cdot|^2 = (\cdot)\overline{(\cdot)}$ and the formula of the previous section. The function $\Xi$ is real-valued on the critical line (imaginary part $\equiv 0$ when $s \in \mathbb{R}$ and $\Xi_0$ is real: see e.g. Doc 70, §2.1), so $\overline{\Xi_0(s)} = \Xi_0(s)$ for $s \in \mathbb{R}$ and the formula simplifies, but it is written in general form for clarity. $\square$

### 2.3. Consistency with Doc 71

Doc 71 (§1, main formula) proved that

$$\partial_t T_\lambda\big|_{t=0} = -4\int W_\lambda(s)\mathrm{Re}\,\bigl(\overline{H_0(s)}\,H_0''(s)\bigr)\,dm_\infty(s)$$

where $H_0 = \Xi_0$. This is precisely

$$\partial_t T_\lambda\big|_{t=0} = 2\int W_\lambda(s)\,\partial_t f_t\big|_{t=0}\,dm_\infty(s).$$

The time derivative of $T_\lambda$ coincides (up to the factor $2$) with the integral of the derivative of the curve $f_t$ against the weight $W_\lambda\,dm_\infty$. The coherence between the two formulations is immediate.

---

## §3. The tangency condition to $M$

### 3.1. The tangent space to $M$ at $f_0$

The manifold $M$ is locally parametrized by the positions $\{\gamma_n\} \subset \mathbb{R}$ of the critical zeros. If $f_0 = |\Xi_0|^2 \in M$ (that is, if all zeros of $\Xi_0$ are on the critical line, i.e., if RH holds), the tangent space at $f_0$ is

$$T_{f_0}M = \overline{\mathrm{span}}\bigl\{\partial_{\gamma_n}|\eta_{on}|^2\big|_{\eta_{on}=\Xi_0} : n \geq 1\bigr\}^{L^2(W_\lambda dm_\infty)}.$$

The derivative in the direction of the $n$-th zero is

$$\partial_{\gamma_n}|\eta_{on}|^2\big|_{\eta_{on}=\Xi_0} = 2\mathrm{Re}\,\bigl[\overline{\Xi_0(s)}\,\partial_{\gamma_n}\Xi_0(s)\bigr].$$

Since $\Xi_0(s) = A\prod_k(1 - s/\gamma_k)e^{s/\gamma_k}$ (Hadamard factorization with simple zeros $\{\pm\gamma_k\}$), the derivative with respect to $\gamma_n$ of the product gives

$$\partial_{\gamma_n}\Xi_0(s) = \Xi_0(s)\cdot\partial_{\gamma_n}\log\Xi_0(s) = \Xi_0(s)\cdot\Bigl(\frac{s}{\gamma_n^2} - \frac{s}{\gamma_n - s} \cdot \frac{1}{\gamma_n}\Bigr).$$

The tangent space $T_{f_0}M$ contains functions of the form $2\mathrm{Re}[\overline{\Xi_0}\Xi_0 \cdot g_n]$ where $g_n$ are meromorphic functions with poles at the zeros of $\Xi_0$.

### 3.2. The derivative of the flow as a tangent vector (under RH)

**Proposition 3.1.** *If RH holds ($\Lambda = 0$), then $\partial_t f_t|_{t=0} \in T_{f_0}M$.*

*Proof.* Under RH, $f_0 \in M$ (all zeros of $\Xi_0$ are critical) and the curve $t \mapsto f_t$ satisfies $f_t \in M$ for all $t \geq 0$ (since for $t \geq 0 = \Lambda$ all zeros of $\Xi_t$ are real). Consequently, the entire curve $t \mapsto f_t$ is contained in $M$ for $t \geq 0$, and its derivative at $t = 0$ is a vector tangent to $M$ at $f_0$. $\square$

*Remark.* Under $\neg$RH ($\Lambda > 0$), the curve $t \mapsto f_t$ reaches $M$ only at $t = \Lambda$. The derivative $\partial_t f_t|_{t=0}$ does not belong to $T_{f_0}M$ but rather points toward the interior of the complement $L^2(W_\lambda dm_\infty) \setminus M$ (if $f_0 \notin M$ the tangent space to $M$ at $f_0$ is not even defined).

---

## §4. Continuity of $T_\lambda(t)$ and extension of the CTP

### 4.1. The CTP criterion for each $t$

**Proposition 4.1.** *For each fixed $t \geq 0$: $T_\lambda(t) = 0$ for all $\lambda > 0$ if and only if all zeros of $\Xi_t$ are real.*

*Proof.* Identical to that of Thm. 3.1 of Doc 64, replacing $\Xi_0$ by $\Xi_t$ in all the arguments. The structure of the Jacobi coefficients of the measure $|\Xi_t|^2 dm_\infty$ is determined by the position of the zeros of $\Xi_t$ in exactly the same way as for $t = 0$. $\square$

### 4.2. Continuity of $T_\lambda(t)$ in $t$

**Proposition 4.2.** *The function $t \mapsto T_\lambda(t)$ is continuous on $[0,\infty)$ for each fixed $\lambda > 0$.*

*Proof.* By definition, $T_\lambda(t)$ is expressed in terms of the Jacobi coefficients of the measure $|\Xi_t|^2 dm_\infty$ (see Doc 70, §3.2). These coefficients depend continuously on $t$ if the measure $|\Xi_t|^2 dm_\infty$ varies continuously in $t$ in the weak sense. We have $|\Xi_t(s)|^2 = \bigl|\int e^{tu^2}\Phi(u)e^{isu}du\bigr|^2$, which is continuous in $t$ for each fixed $s$ by the continuity of the integrand $e^{tu^2}\Phi(u)$ in $t$. Dominated convergence applies for $t$ in compacts $[0,T]$: the dominator is $\bigl|\int e^{Tu^2}|\Phi(u)|\,du\bigr|^2$ which is finite by the super-exponential decay of $\Phi$. Hence $|\Xi_t(s)|^2 \to |\Xi_{t_0}(s)|^2$ in $L^1(W_\lambda\,dm_\infty)$ as $t \to t_0$, which implies weak convergence of the measures and continuity of the Jacobi coefficients. $\square$

**Corollary 4.3.** *$\lim_{t \to 0^+} T_\lambda(t) = T_\lambda(0)$ for each $\lambda > 0$.*

### 4.3. Reformulation of $\Lambda$ via continuity

Doc 70 (§4) established $\Lambda = \inf\{t \geq 0 : T_\lambda(t) = 0\;\forall\lambda\}$. The continuity of $T_\lambda(t)$ allows this infimum to be made more precise:

**Corollary 4.4.** *$\Lambda = \min\{t \geq 0 : T_\lambda(t) = 0\;\forall\lambda\}$ if the infimum is attained; i.e., if $\Lambda < \infty$ then $T_\lambda(\Lambda) = 0$ for all $\lambda > 0$.*

*Proof.* Let $\{t_n\}$ be a decreasing sequence with $t_n \to \Lambda$ and $T_\lambda(t_n) = 0$ for all $n$ and all $\lambda$. By continuity of $T_\lambda(\cdot)$, $T_\lambda(\Lambda) = \lim_{n} T_\lambda(t_n) = 0$. $\square$

This result is known indirectly (the zeros of $\Xi_\Lambda$ are all real, see De Bruijn 1950), but the proof via continuity of $T_\lambda$ is coherent with the CCM formalism.

---

## §5. The flow as a homotopy and the time of entry into $M$

### 5.1. The trajectory $[0,\infty) \to L^2(W_\lambda\,dm_\infty)$

The curve $\gamma : t \mapsto f_t$ is a real-analytic trajectory in $L^2(W_\lambda\,dm_\infty)$ (Prop. 1.2) that starts from $f_0 = |\Xi_0|^2 \in L^2(W_\lambda\,dm_\infty)$ and satisfies:

- For $t \in [0,\Lambda)$: $\gamma(t) \notin M$ (there are off-critical zeros, Prop. 1.3).
- For $t \geq \Lambda$: $\gamma(t) \in M$ (all zeros are real, Prop. 1.3).
- $\gamma(\Lambda) = f_\Lambda \in M$ (limit at $t = \Lambda$ by Prop. 4.2 and Cor. 4.3).

The trajectory enters $M$ exactly at time $t = \Lambda$, and remains in $M$ for all subsequent $t$.

### 5.2. Formulation as a first-arrival-time problem

The De Bruijn-Newman constant can be read as the **first arrival time** of the trajectory $\gamma$ to the submanifold $M$:

$$\Lambda = \inf\{t \geq 0 : \gamma(t) \in M\}.$$

This geometric formulation in $L^2(W_\lambda\,dm_\infty)$ is equivalent to the original definition of $\Lambda$ (via the position of the zeros of $\Xi_t$) and equivalent to that of Doc 70 (via the extinction of $T_\lambda(t)$). The three formulations are reformulations of the same fact.

### 5.3. The case RH $\iff$ starting from $M$

**Proposition 5.1.** *$\Lambda = 0$ if and only if $\gamma(0) = f_0 \in M$, which is equivalent to RH.*

*Proof.* $\Lambda = 0 \iff$ all zeros of $\Xi_0$ are real $\iff f_0 \in M \iff$ RH. The equivalence between $\Lambda = 0$ and RH is the result of Rodgers-Tao (2018: $\Lambda \geq 0$) combined with the statement $\Lambda \leq 0 \iff$ RH. $\square$

Under RH, the trajectory starts in $M$ and remains in $M$ for all $t \geq 0$. Under $\neg$RH, the trajectory starts outside $M$ and reaches $M$ for the first time at $t = \Lambda > 0$.

---

## §6. Asymptotic behavior of the trajectory as $t \to \infty$

### 6.1. Growth of $\Xi_t$ and dispersion of zeros

As $t \to \infty$ the factor $e^{tu^2}$ concentrates the mass of the integrand of $\Xi_t$ at the values of $u$ that maximize $tu^2 - \pi n^2 e^{2u}$ (competition between the Gaussian factor and the decay of $\Phi$). The saddle-point analysis gives that the dominant contribution comes from $u^* \sim \frac{1}{2}\log(t/(2\pi n^2))$, and the function $\Xi_t$ grows like $e^{t(\log t)^2/4}$ as $t \to \infty$ (super-exponential growth).

The zeros of $\Xi_t$ for $t \to \infty$ are distributed with increasing density: the $n$-th imaginary part of the zeros satisfies $\gamma_n(t) \sim c\sqrt{t}\cdot h(n)$ where $h(n)$ depends on the zero distribution of $\Xi_0$. The spacing between consecutive zeros grows like $\sqrt{t}$, so the zeros disperse as $t$ increases.

### 6.2. The function $f_t$ as $t \to \infty$ as an element of $M$

For each $t > \Lambda$, $f_t \in M$, but the elements of $M$ parametrizing $f_t$ have zeros at $\{\pm\gamma_n(t)\}$ that disperse to infinity as $t \to \infty$. In the limit $t \to \infty$, the function $f_t/\|f_t\|$ converges weakly to zero in $L^2(W_\lambda\,dm_\infty)$ (the mass escapes to infinity). The trajectory $\gamma(t)$ does not converge in norm to any point of $M$ as $t \to \infty$; instead, $\|f_t\|_{L^2} \to \infty$ and the trajectory "escapes" to infinity in the space.

The homotopy between $f_0$ and $M$ provided by the DBN flow is therefore a homotopy toward a point of $M$ that depends on $t$, not toward a fixed point. The trajectory enters $M$ at $t = \Lambda$ but continues moving within $M$ indefinitely.

---

## §7. The conjectural flow strategy and its obstacle

### 7.1. The idea and why it does not work

The continuity of $T_\lambda(t)$ (Prop. 4.2) and the fact that $T_\lambda(t) = 0$ for $t > \Lambda$ suggest the following strategy for proving RH: if one could show that $T_\lambda(t) = 0$ for some $t > 0$ (by arguments independent of the position of the zeros of $\Xi_0$), then by continuity $T_\lambda(0) = 0$, that is, RH.

The obstacle is that the condition $T_\lambda(t) = 0$ for $t > 0$ is precisely equivalent to all zeros of $\Xi_t$ being real (Prop. 4.1), which is true for $t > \Lambda$, but that $\Lambda = 0$ (i.e., that $t = 0^+$ already has $T_\lambda = 0$) is again RH. There is no way to verify $T_\lambda(t) = 0$ for fixed $t > 0$ without knowing the position of the zeros of $\Xi_t$, and knowing that position for small $t$ is equivalent to knowing the position of the zeros of $\Xi_0$ (by continuity of the zeros in $t$).

### 7.2. The monotonicity conjecture and its insufficiency

Doc 70 formulated the conjecture:

**Monotonicity Conjecture.** *$t \mapsto T_\lambda(t)$ is non-increasing on $[0,\infty)$.*

If this conjecture were true:
- For $t > \Lambda$: $T_\lambda(t) = 0$.
- For $0 \leq t \leq \Lambda$: $T_\lambda(t) \geq T_\lambda(\Lambda) = 0$ (by monotonicity).
- In particular, $T_\lambda(0) \geq 0$.

But this is already known: $T_\lambda(0) \geq 0$ is the inequality proved in Doc 83 (the measure domination $dm_{full} \geq dm_{full,on}$ implies $T_\lambda(0) \geq 0$). Monotonicity would confirm that the trajectory is non-increasing but would not prove that $T_\lambda(0) = 0$.

To prove RH from monotonicity, an additional argument would be needed to force $T_\lambda(0)$ to be zero, not merely non-negative. No such argument is known.

### 7.3. The zero-derivative condition and its coherence

Under RH ($\Lambda = 0$): the curve $\gamma$ is in $M$ for all $t \geq 0$, so $T_\lambda(t) = 0$ for all $t \geq 0$, and in particular $\partial_t T_\lambda|_{t=0} = 0$.

Doc 71 computed that

$$\partial_t T_\lambda\big|_{t=0} = -4\int W_\lambda(s)\mathrm{Re}\,\bigl(\overline{\Xi_0(s)}\,\Xi_0''(s)\bigr)\,dm_\infty(s)$$

and proved that this expression is a quadratic form in the coefficients $c_k = \langle \Xi_0, P_k\rangle_{dm_\infty}$ that cancels exactly when the zeros of $\Xi_0$ are critical (algebraic condition on the $c_k$). The condition $\partial_t T_\lambda|_{t=0} = 0$ is therefore another reformulation of RH, not a new result.

**Proposition 7.1.** *The following conditions are equivalent:*
*(i) RH;*
*(ii) $T_\lambda(0) = 0$ for all $\lambda > 0$;*
*(iii) $T_\lambda(t) = 0$ for all $t \geq 0$ and all $\lambda > 0$;*
*(iv) $\partial_t T_\lambda|_{t=0} = 0$ for all $\lambda > 0$;*
*(v) $f_0 \in M$;*
*(vi) $\Lambda = 0$.*

*Proof.* The equivalence (i) $\iff$ (ii) is the CTP (Doc 64). The equivalence (ii) $\iff$ (vi) is the characterization of Doc 70. The equivalence (vi) $\iff$ (v) is Prop. 5.1. The implication (iii) $\implies$ (ii) is immediate. The implication (i) $\implies$ (iii): under RH, $T_\lambda(t) = 0$ for $t \geq 0$ because $\Lambda = 0$ and $T_\lambda(t) = 0$ for $t \geq \Lambda = 0$. The equivalence (ii) $\iff$ (iv): Doc 71 shows that $\partial_t T_\lambda|_{t=0} = 0$ iff the coefficients $c_k$ satisfy the cancellation condition, which is equivalent to all zeros of $\Xi_0$ being critical. $\square$

The multiplicity of equivalent formulations reflects the internal coherence of the formalism, not a gain of information.

---

## §8. Synthesis of Path 3 and the residual obstacle

### 8.1. Unconditional results established

Path 3 has produced the following rigorous, unconditional results:

**R1 (Doc 82, Cor. 4.6).** The variational infimum $\tilde\delta_\lambda^2 := \inf\{\||\zeta|^2 - |\eta_{on}|^2\|^2_{L^2(W_\lambda dm_\infty)} : \eta_{on} \in M\}$ satisfies $\tilde\delta_\lambda^2 = 0 \iff$ RH.

**R2 (Doc 85, Thm. 5.1).** The linear span of $\{e^{i\gamma_n s}\}_{n \geq 1}$ is dense in $L^2(W_\lambda\,dm_\infty)$. The $\gamma_n = \mathrm{Im}(\rho_n)$ are always real by the functional equation, independently of RH.

**R3 (this document, Prop. 1.2 and Prop. 4.2).** The curve $t \mapsto f_t = |\Xi_t|^2$ is real-analytic in $L^2(W_\lambda\,dm_\infty)$ and the trace $t \mapsto T_\lambda(t)$ is continuous on $[0,\infty)$.

**R4 (this document, Prop. 5.1).** $\Lambda = \inf\{t \geq 0 : f_t \in M\}$, and $\Lambda = 0 \iff f_0 \in M \iff$ RH.

**R5 (this document, Prop. 7.1).** Conditions (i)–(vi) of Prop. 7.1 are all equivalent to RH.

### 8.2. The gap that persists

Results R1–R5 are equivalent reformulations of RH in the space $L^2(W_\lambda\,dm_\infty)$. The gap is always the same: passing from linear approximation (R2: dense linear span) to membership in the non-linear class $M$ (R1: the infimum $\tilde\delta_\lambda^2$ is zero).

Linear approximation says: $|\zeta|^2$ can be approximated in $L^2$ norm by linear combinations of functions that include elements of $M$. Membership in $M$ says: $|\zeta|^2$ is exactly an element of $M$, that is, $\zeta$ has all its zeros on the critical line. The distance from a linear class to a non-linear submanifold can be zero without the point belonging to the submanifold (one can approximate arbitrarily well without reaching it). The equivalence $\tilde\delta_\lambda^2 = 0 \iff$ RH asserts that in this specific case the distance is zero exactly when the manifold is reached, but this is the content of RH, not a consequence of approximation theory.

### 8.3. The open question that summarizes Path 3

The only non-circular route identified in Path 3 requires unconditionally proving one of the following:

**(Q1)** That $\partial_t T_\lambda|_{t=0} \leq 0$ (non-positive time derivative), or more strongly, that the Monotonicity Conjecture holds. This would not prove RH but would restrict the behavior of $T_\lambda$ and could be combined with other arguments.

**(Q2)** That $T_\lambda(t) = 0$ for some specific $t > 0$ without using the position of the zeros of $\Xi_t$. This would imply RH by continuity, but it is unknown how to do this: the only tool for proving $T_\lambda(t) = 0$ goes through knowing the zeros, which is precisely what is not known.

**(Q3)** That the function $t \mapsto \Lambda(f_t, M)$ (distance from $f_t$ to $M$ in $L^2(W_\lambda\,dm_\infty)$) has a rate of decrease that forces $\Lambda(f_0, M) = 0$ by a comparison argument. Such an argument would require a quantitative estimate of the geometry of $M$ (curvature, injectivity radius) that is not currently available.

None of the three routes is unblocked. The DBN flow as a curve in $L^2(W_\lambda\,dm_\infty)$ provides a clean geometric picture of RH ($f_0 \in M$) and of $\Lambda$ (first arrival time to $M$), but not a new proof strategy.

---

## §9. Conclusion

Document 88 closes Path 3 with the following geometric description of its content:

In the space $L^2(W_\lambda\,dm_\infty)$, the Riemann hypothesis is equivalent to the point $f_0 = |\Xi_0|^2$ belonging to the non-linear submanifold $M$ of infinite codimension. The De Bruijn-Newman flow defines an analytic curve $t \mapsto f_t$ that enters $M$ exactly at time $\Lambda$ (the De Bruijn-Newman constant). The trace $T_\lambda(t)$ measures the distance from $f_t$ to $M$ (in the sense of the Jacobi coefficients) and is continuous in $t$.

The reformulation is coherent, complete, and frank: each of the equivalent criteria for RH that Path 3 has produced (the variational one, the completeness one, the flow one, the time-derivative one) are different formulations of the same thing. The geometry of the DBN flow in $L^2(W_\lambda\,dm_\infty)$ does not open a new route toward the proof; it illustrates the equivalence $\Lambda = 0 \iff$ RH in geometric language, without adding tools to verify that equivalence non-circularly.

The fundamental obstacle of Path 3 — the gap between linear approximation and membership in the non-linear class — remains open.

---

*End of Document 88.*
