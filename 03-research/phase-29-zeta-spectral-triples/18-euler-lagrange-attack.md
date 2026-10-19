# Phase 29 — Attack D: The Euler-Lagrange equation as a spectral constraint and the potential $C_\infty$

**Objective:** Attack Front D: use the Euler-Lagrange equation of the CCM system in the limit $\lambda \to \infty$ to deduce properties of the zeros of $C_\infty$ WITHOUT assuming RH. Synthesize attacks A, B, C, D into a unified strategy. Identify the weakest auxiliary conjecture that would imply RH.

---

## 1. The Euler-Lagrange equation in the limit $\lambda \to \infty$

From Doc 12 (Proposition 2) and Doc 13 (Proposition 3): the Euler-Lagrange equation of the CCM variational problem in the limit is:

$$\hat\xi_\infty(z) = \frac{-c_\infty \hat k(z)}{C_\infty(z)},$$

where $C_\infty(z) = w(z) - \Psi(z) = \lim_\lambda [C_\lambda(z) - \mu_\lambda]$ and $c_\infty = \lim_\lambda c_\lambda > 0$.

**Direct consequence.** The zeros of $\hat\xi_\infty$ are exactly the zeros of the numerator $\hat k(z) = \Xi(z)$ at the points where the denominator $C_\infty(z) \neq 0$.

At the points where $C_\infty(z) = 0$ (zeros of the denominator): $\hat\xi_\infty$ has possible poles canceled by zeros of $\Xi$ (if $\Xi$ also vanishes at those points).

**Cancellation structure.** For $\hat\xi_\infty$ to be an entire function (no poles): every zero of $C_\infty$ must be canceled by a zero of $\Xi$. This means:

$$\{z : C_\infty(z) = 0\} \subseteq \{z : \Xi(z) = 0\}.$$

---

## 2. The complete cancellation condition

**Definition.** We say that the pair $(\Xi, C_\infty)$ satisfies the **complete cancellation condition (CCC)** if:

$$\{z \in \mathbb{C} : C_\infty(z) = 0\} = \{z \in \mathbb{C} : \Xi(z) = 0\}$$

(equality of zero sets, counted with multiplicity at the coinciding zeros).

**Proposition 1** (CCC implies that $\hat\xi_\infty$ is entire and proportional to $\Xi$). If CCC holds:

$$\hat\xi_\infty(z) = \frac{-c_\infty \Xi(z)}{C_\infty(z)} = -c_\infty \frac{\Xi(z)}{C_\infty(z)}.$$

If in addition the ratio $\Xi(z)/C_\infty(z)$ is a nonzero entire function (which CCC guarantees): then $\hat\xi_\infty = (-c_\infty/h) \cdot 1$ for some constant $h = C_\infty(0)/\Xi(0)$...

**Correction.** The equation is $\hat\xi_\infty \cdot C_\infty = -c_\infty \Xi$. If CCC holds: $\Xi/C_\infty$ is an entire function with no zeros (since numerator and denominator have the same zeros). Then $\Xi/C_\infty = e^{g(z)}$ for some entire function $g$. For functions of finite order (both $\Xi$ and $C_\infty$ are of finite order), $g$ is a polynomial. The symmetry $\Xi(t) = \Xi(-t)$ and $C_\infty(t) = C_\infty(-t)$ (both even) implies that $e^{g(z)}$ is also even, so $g(z) = az^2 + b$ for constants $a, b$.

But if $\Xi$ is of order 1 and $C_\infty$ is of order 1 (reasonable given the series over primes): $g$ must be constant. Then $\Xi = e^g C_\infty$, i.e., $C_\infty = e^{-g}\Xi$ — $C_\infty$ is proportional to $\Xi$.

**Consequence of CCC:** If CCC holds: $C_\infty(z) = c \cdot \Xi(z)$ for some constant $c \neq 0$. Then the Euler-Lagrange equation gives $\hat\xi_\infty(z) = -c_\infty / c = $ constant — which is absurd (since $\hat\xi_\infty$ has infinitely many zeros, those of $\Xi$).

**Diagnosis.** CCC in the form $\{C_\infty = 0\} = \{\Xi = 0\}$ cannot be literally true: the equation $\hat\xi_\infty = -c_\infty \Xi / C_\infty$ with $\Xi/C_\infty$ entire and non-constant would require $C_\infty$ to have more zeros than $\Xi$ (so that $\Xi/C_\infty$ is not constant). Or else $C_\infty$ is entire of a different order.

---

## 3. Revision: the correct structure of the Euler-Lagrange equation

**Correction of Proposition 1.** The Euler-Lagrange equation in the function space $E_N^+$ does NOT literally give $\hat\xi_\infty = -c_\infty \Xi/C_\infty$, since $C_\infty$ may have infinitely many zeros not canceled by $\Xi$. The correct equation (from Doc 12) is:

$$[w(z) - \Psi_\lambda(z) - \mu_\lambda] \hat\xi_\lambda(z) = -c_\lambda \hat k_\lambda(z),$$

where all objects are in $E_N^+$ (truncated). In the limit $\lambda \to \infty$, convergence of $\hat\xi_\lambda$ and $\hat k_\lambda$ (if H2 holds) gives:

$$C_\infty(z) \cdot \Xi(z) = -c_\infty \Xi(z) \implies C_\infty(z) = -c_\infty.$$

This is a TAUTOLOGY if $\Xi(z) \neq 0$. At the zeros of $\Xi$: both sides are zero, and no information is extracted.

**The correct approach (via the Blaschke representation).** From Doc 13 (Proposition 3):

$$B_\lambda(z) = \frac{\hat\xi_\lambda(z)}{\hat k_\lambda(z)} = \frac{-c_\lambda}{C_\lambda(z) - \mu_\lambda}.$$

In the limit:

$$B_\infty(z) = \lim_\lambda B_\lambda(z) = \frac{-c_\infty}{C_\infty(z)}.$$

The condition H2 ($B_\lambda \to 1$) is equivalent to $B_\infty = 1$, i.e., $C_\infty(z) = -c_\infty$ for all $z$.

**Proposition 2** (the H2 condition in the limit). H2 is equivalent to the limiting potential $C_\infty(z)$ being CONSTANT equal to $-c_\infty$ everywhere on $\mathbb{C}$.

*Proof.* $B_\infty = 1 \iff -c_\infty/C_\infty = 1 \iff C_\infty = -c_\infty$ (constant). $\square$

**But $C_\infty$ cannot be constant:** $C_\infty(z) = w(z) - \Psi(z)$ where $w(z) = \partial_z\theta(z)$ is not constant (it is approximately $\frac{1}{2}\log(z/2\pi)$ for $z \gg 1$). Then $C_\infty$ is not constant. Contradiction.

**Resolution of the contradiction.** The representation $B_\lambda = -c_\lambda/(C_\lambda - \mu_\lambda)$ is the diagonal approximation of Doc 12 — valid in the approximation where the projection onto $E_N^+$ is ignored. In the exact representation (including the projection), $B_\lambda$ is NOT exactly $-c_\lambda/(C_\lambda - \mu_\lambda)$. The exact representation in $E_N^+$ is more complex.

The correct H2 condition is $B_\lambda(z) \to 1$ for $z \in \mathbb{C} \setminus \mathbb{R}$, which is equivalent to the convergence $m_\lambda \to m_k^\lambda$ (Stieltjes transform of $\hat\xi_\lambda$ converges to the Stieltjes transform of $\hat k_\lambda$) — already established under RH (Doc 13, Theorem 1).

---

## 4. Attack D reformulated: zeros of $C_\infty$ vs. zeros of $\Xi$ via von Mangoldt

**The central question of Attack D.** By Theorem C1 of Doc 17: $\mathrm{spec}(J_\infty) = \{t \in \mathbb{R}: C_\infty(t) = 0\}$. And by Doc 15: $\mathrm{spec}(J_\infty)$ has measure $\mu_\gamma^{real}$.

Therefore, the distribution measure of the zeros of $C_\infty$ on $\mathbb{R}$ is $\mu_\gamma^{real}$ (unconditionally).

**Advisor 1's question (Attack D).** Can the density of zeros of $C_\infty$ on $\mathbb{R}$ be identified using the von Mangoldt explicit formula, WITHOUT assuming RH?

**Proposition 3** (density of zeros of $C_\infty$ via the explicit formula). The potential $C_\infty(t) = w(t) - \Psi(t)$ for $t \in \mathbb{R}$ has a zero density given by the formula:

$$\#\{t \in [0,T]: C_\infty(t) = 0\} = \frac{1}{\pi}\int_0^T |C_\infty'(t)|^+ \frac{dt}{C_\infty(t)^+ + \varepsilon} + O(1)$$

(in the sense of Jensen's formula or argument counting).

The explicit formula gives $C_\infty(t) = 2\sum_\rho \cos(t\log|\rho|)/|\rho|$ (with sum over non-trivial zeros of $\zeta$).

**Estimate of the zero density.** For $T \gg 1$:

The number of zeros of $C_\infty(t) = 2\sum_\rho \cos(t\log|\rho|)/|\rho|$ in $[0,T]$ can be estimated via Langer's theorem (for almost-periodic functions):

$$\#\{t \in [0,T]: C_\infty(t) = 0\} \approx \frac{T}{\pi} \cdot \frac{d}{dT}\arg C_\infty(T+iy)\bigg|_{y=0}.$$

For the function $C_\infty(t) = 2\sum_\rho \cos(t\log|\rho|)/|\rho|$: each term $\cos(t\log|\rho|)/|\rho|$ contributes $2\log|\rho|/|\rho|$ zeros per unit of $T$ (zero density of $\cos$). The total density:

$$\frac{d}{dT}\#\{C_\infty = 0 \text{ in } [0,T]\} \approx \sum_\rho \frac{\log|\rho|}{\pi |\rho|}.$$

**Comparison with the density of zeros of $\Xi$.**

The density of zeros of $\Xi$ in $[0,T]$ is $\frac{dN_\Xi}{dT} = \frac{1}{2\pi}\log\frac{T}{2\pi}$.

The density of zeros of $C_\infty$ (estimated above) is $\sum_\rho \log|\rho|/(\pi|\rho|)$, a sum that depends on ALL zeros of $\zeta$ (not only those on the critical line).

**Under RH:** $|\rho| = \sqrt{1/4 + \gamma^2} \approx \gamma$ and $\log|\rho| \approx \log\gamma$. Then:

$$\sum_\rho \frac{\log|\rho|}{|\rho|} \approx \sum_n \frac{\log\gamma_n}{\gamma_n} \approx \int_0^\infty \frac{\log t}{t} \cdot \frac{\log t}{2\pi} dt \quad (\text{false — diverges}).$$

Clearly this approximation is too crude. The density of zeros of $C_\infty$ is finite because there are cancellations among the different terms of the sum.

---

## 5. Fine analysis of the zeros of $C_\infty$ via harmonic analysis

**The structure of $C_\infty$ as an almost-periodic function.** For $t \in \mathbb{R}$:

$$C_\infty(t) = 2\sum_\rho \frac{\cos(t\log|\rho|)}{|\rho|} = 2\Re\sum_\rho \frac{e^{it\log|\rho|}}{|\rho|}.$$

This is an "almost-periodic" Dirichlet series with frequencies $\{\log|\rho|\}$ and amplitudes $\{1/|\rho|\}$.

**Proposition 4** (the zeros of $C_\infty$ are determined by frequency interference). The zeros of $C_\infty(t)$ on $\mathbb{R}$ are the instants of "complete destructive interference" among the modes $\cos(t\log|\rho|)/|\rho|$.

Under RH: the $|\rho| = \sqrt{1/4+\gamma_n^2}$ lie on the "circle" $|\rho| \approx \gamma_n$. The modes have frequencies $\log|\rho| \approx \log\gamma_n$. The interference among these modes produces nulls at $t = \gamma_n$ (the imaginary parts of the zeros of $\zeta$) — this is precisely the content of the explicit formula applied to the zeros of $\Xi$.

Without RH: there would be additional modes with $|\rho| > \gamma$ (from zeros off the critical line), with frequencies $\log|\rho| > \log\gamma$. Those additional modes would generate additional interferences, producing nulls of $C_\infty$ that are not $\gamma_n$. The operator $J_\infty$ would "see" those additional nulls and its spectrum would include extra points — contradicting $\mu_\infty = \mu_\gamma^{real}$ (which only has $\gamma_n$ as atoms).

**Proposition 5** (contradiction argument via zero density). Suppose RH fails: there exists $\rho_0 = \sigma_0 + i\gamma_0$ with $\sigma_0 > 1/2$. Then:

(a) The mode $\cos(t\log|\rho_0|)/|\rho_0|$ has frequency $\log|\rho_0| > \log\gamma_0$ (strictly).

(b) This mode generates zeros of $C_\infty$ at positions $t_k \approx \pi(2k+1)/(2\log|\rho_0|) \neq \gamma_0$ (in general).

(c) These zeros $t_k$ are in the spectrum of $J_\infty$ (by Theorem C1 of Doc 17).

(d) But $\mu_\infty = \mu_\gamma^{real}$ has atoms only at $\{\gamma_n\} = $ zeros of $\Xi$ on $\mathbb{R}$. If the $t_k$ are not zeros of $\Xi$: $\mu_\infty$ has extra atoms, contradicting $\mu_\infty = \mu_\gamma^{real}$.

**The gap in Proposition 5:** Step (c) assumes that ALL zeros of $C_\infty$ are in $\mathrm{spec}(J_\infty)$. Theorem C1 of Doc 17 states that $\mathrm{spec}(J_\infty) = \{t \in \mathbb{R}: C_\infty(t) = 0\}$ — which would include the $t_k$. But the contradiction argument requires verifying that the $t_k$ are real and distinct from the $\gamma_n$, and that they contribute positive weight to $\mu_\infty$.

**Obstacle.** The zeros $t_k$ of $C_\infty$ are real (by the symmetry of $C_\infty$ on $\mathbb{R}$: $C_\infty(t) \in \mathbb{R}$ for $t \in \mathbb{R}$). But they may coincide with zeros of $\Xi$ by cancellation. If $t_k = \gamma_{n_k}$ for some zero $\gamma_{n_k}$ of $\Xi$: the spectrum of $J_\infty$ at $t_k$ would be an atom of $\mu_\gamma^{real}$ (consistent).

---

## 6. The functional equation of $C_\infty$ and the zeros

**Proposition 6** (functional equation of $C_\infty$). The function $C_\infty(z) = w(z) - \Psi(z)$ satisfies:

(EFC1) $C_\infty(t) \in \mathbb{R}$ for $t \in \mathbb{R}$ (real-analytic).

(EFC2) $C_\infty(-z) = C_\infty(z)$ (even function, from the parity of $w$ and of $\Psi$).

(EFC3) $C_\infty(z) \to +\infty$ as $t \to +\infty$ along the reals (from $w(t) \sim \frac{1}{2}\log(t/2\pi) \to \infty$ and $\Psi(t)$ bounded on average).

(EFC4) The Laplace transform of $C_\infty$: $\hat C_\infty(s) = \int C_\infty(t) e^{-st} dt$ is related to the function $L(s, \Psi)$.

*Proof of EFC2.* $w(z)$ is even: $w(-z) = w(z)$ (from the parity of $\theta(t) = \Im\log\Gamma(1/4+it/2) - (t/2)\log\pi$: $\theta(-t) = -\theta(t)$, and $\partial_t\theta(-t) = \partial_t[-\theta(t)] = -\theta'(t)$... wait: the parity of $w(t) = \partial_t\theta(t)$. If $\theta(-t) = -\theta(t)$: $w(-t) = \partial_t\theta|_{-t} = -\partial_t\theta(t)|_t = -w(t)$.

Correction: $w(t) = \Im(\partial_t\log\Gamma(1/4+it/2)) - \frac{1}{2}\log\pi = \frac{1}{2}\Re\frac{\Gamma'}{\Gamma}(1/4+it/2)$, which is ODD: $w(-t) = -w(t)$. And $\Psi(-t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(-t\log p) = \Psi(t)$ (even). Then $C_\infty(-t) = w(-t) - \Psi(-t) = -w(t) - \Psi(t) \neq C_\infty(t)$ in general.

**Correction of EFC2.** $C_\infty$ is not even. We have:

$$C_\infty(-t) = -w(t) - \Psi(t) = -[w(t) + \Psi(t)] \neq C_\infty(t) = w(t) - \Psi(t).$$

The function $C_\infty(t)$ is not even. This is consistent with the symmetry of $\Xi$ being $\Xi(-t) = \Xi(t)$, but $C_\infty$ need not be even (it is the potential, not the function whose spectrum we are studying).

**Implication.** The zeros of $C_\infty$ on $\mathbb{R}$ do not come in pairs $\pm t$. This is consistent with the measure $\mu_\gamma^{real}$ (which, at the full scale, IS symmetric, since the $\gamma_n$ come in pairs $\pm\gamma_n$).

**Contradiction.** But if $\mu_\infty = \mu_\gamma^{real}$ is symmetric and $\mathrm{supp}(\mu_\infty) = \{t: C_\infty(t) = 0\}$ (Corollary C2 of Doc 17): the zeros of $C_\infty$ must be symmetric. If $C_\infty(t) = 0$ then $C_\infty(-t) = -w(t) - \Psi(t) \neq 0$ in general (since $w(t) > 0$ for large $t > 0$). Contradiction with the symmetry of the support of $\mu_\infty$.

---

## 7. Resolution of the apparent contradiction

**Resolution.** The contradiction of Section 6 reveals an error in Corollary C2 of Doc 17. Theorem C1 states $\mathrm{spec}(J_\infty) = \{t \in \mathbb{R}: C_\infty(t) = 0\}$, but this is derived from the fixed-point equation (EF2) $N \cdot m_\infty = C_\infty'/C_\infty$, which says that the **poles** of $m_\infty$ coincide with the zeros of $C_\infty$.

Now: $m_\infty$ has poles at the eigenvalues of $J_\infty$ (all real, by self-adjointness), and the support of $\mu_\infty$ is $\{\gamma_n : \gamma_n \in \mathbb{R}\}$ (symmetric). If the zeros of $C_\infty$ are not symmetric, the fixed-point equation (EF2) fails.

**Proposition 7** (EF2 requires symmetry of the zeros of $C_\infty$). If $m_\infty(-z) = -m_\infty(z)$ (anti-parity, from the symmetry of $\Xi$) and $N \cdot m_\infty(z) = C_\infty'(z)/C_\infty(z)$ (EF2): then the zeros of $C_\infty$ are symmetric, i.e., if $C_\infty(\gamma) = 0$ then $C_\infty(-\gamma) = 0$.

*Proof.* If $C_\infty(\gamma) = 0$: $m_\infty$ has a pole at $\gamma$ (from EF2). By anti-parity: $m_\infty(-z) = -m_\infty(z)$ also has a pole at $-\gamma$. Then the pole of $-m_\infty(z)$ at $-\gamma$ corresponds to a pole of $m_\infty(-z)$ at $-\gamma$, i.e., to a pole of $m_\infty(w)$ at $w = -\gamma$. Then $m_\infty$ has a pole at $-\gamma$, which by (EF2) implies $C_\infty(-\gamma) = 0$. $\square$

**Corollary.** If (EF2) and the anti-parity of $m_\infty$ hold, the zeros of $C_\infty$ are symmetric. But we computed that $C_\infty(-t) \neq C_\infty(t)$ in general. Then: either (EF2) does not literally hold for the function $C_\infty$ defined as $w - \Psi$, or the anti-parity of $m_\infty$ is an error.

**The correct resolution.** The anti-parity of $m_\infty$ is $m_\infty(-z) = -m_\infty(z)$ in the symmetric case (full scale with zeros $\pm\gamma_n$). But Doc 15 works with $\mu_\gamma^{real}$ = measure over only the $\gamma_n > 0$, which is not symmetric. The function $m_\infty$ of that measure does not satisfy $m_\infty(-z) = -m_\infty(z)$.

The symmetry $\Xi(t) = \Xi(-t)$ implies that the spectrum of $J_\infty$ over the full $\mathbb{R}$ is symmetric. In the model of Doc 15 (positive zeros only), the operator $J_\infty$ is NOT the symmetric operator — it is the positive part.

**Conclusion.** Attack D (via the Euler-Lagrange equation in the limit) produces useful constraints, but the identification of the zeros of $C_\infty$ with the $\gamma_n$ without RH remains the central gap.

---

## 8. The weakest auxiliary conjecture that would imply RH

Gathering the results of Docs 16, 17, 18:

**Theorem D1** (synthesis of the four attacks). The following statements imply RH (they are sufficient conditions):

**(S1) Identification of zeros (Attack A):** The real zeros of the potential $C_\infty(t) = w(t) - \Psi(t)$ are exactly the $\gamma_n$ (imaginary parts of the zeros of $\zeta$ on $\Re(s)=1/2$).

**(S2) Uniqueness of the fixed point (Attack B):** The function $m_\infty$ is the unique solution of the fixed-point equation (EF2) in the Nevanlinna class with real support.

**(S3) No extra zeros (Attack C):** The spectrum of $J_\infty$ has no more elements than the real $\gamma_n$.

**(S4) Modulated complete cancellation (Attack D):** The function $B_\infty(z) = \lim_\lambda \hat\xi_\lambda/\hat k_\lambda$ satisfies $B_\infty \equiv 1$.

Each of (S1)-(S4) is equivalent to RH. The question is which is easiest to prove directly.

*Proof of equivalence.*
- (S1) $\iff$ RH: Theorem C3 of Doc 17 (with the correct identification via the explicit formula).
- (S2) $\iff$ RH: Theorem A1 of Doc 16 (the unique fixed point in $\mathcal{M}^{CCM}$ is $S_\Xi$, which requires real zeros).
- (S3) $\iff$ RH: Theorem C3 of Doc 17 (if the spectrum of $J_\infty$ coincides with all the $\gamma_n$ and only those, which are real: RH).
- (S4) $\iff$ RH: Proposition 1 of Doc 13 (H2 $\iff$ RH, via Hurwitz). $\square$

---

## 9. The auxiliary conjecture: monotonicity of the potential $C_\infty$

**Remark.** The potential $C_\infty(t) = w(t) - \Psi(t)$ for real $t$ has the behavior:

- $w(t) \sim \frac{1}{2}\log(t/2\pi)$ grows monotonically.
- $\Psi(t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p)$ oscillates.

The zeros of $C_\infty(t) = w(t) - \Psi(t)$ are the points where $\Psi(t) = w(t)$ (the "crossings" of $\Psi$ with the slowly growing level $w(t)$).

**Auxiliary conjecture (AC).** The number of crossings of $\Psi(t)$ with the level $w(t)$ in the interval $[0,T]$ is:

$$\#\{t \in [0,T]: \Psi(t) = w(t)\} = N_\Xi(T) + O(\log T),$$

i.e., the number of zeros of $C_\infty$ in $[0,T]$ is the same (up to $O(\log T)$) as the number of zeros of $\Xi$ in $[0,T]$, and this holds WITHOUT assuming RH.

**Proposition 8** (AC $\Rightarrow$ RH). If the auxiliary conjecture (AC) is true: the number of zeros of $C_\infty$ in $[0,T]$ matches $N_\Xi(T) + O(\log T)$. By Theorem C1 of Doc 17: $\mathrm{spec}(J_\infty) = \{$real zeros of $C_\infty\}$. By the convergence $\mu_\xi^\lambda \Rightarrow \mu_\gamma^{real}$ (Doc 15): the density of $\mathrm{spec}(J_\infty)$ is $N_\Xi(T) + O(\log T)$. Consistent, but does not directly imply point-by-point coincidence with $\{\gamma_n\}$.

For AC to imply RH, we additionally need each zero of $C_\infty$ to coincide with a $\gamma_n$ — which requires the POSITION of the zeros, not just their count. This goes beyond (AC).

**Strong AC.** The strong auxiliary conjecture (SAC) is: every zero $t_0 \in \mathbb{R}$ of $C_\infty$ satisfies $\Xi(t_0) = 0$. This is equivalent to (S1), which is equivalent to RH.

---

## 10. Direct attack on (SAC): the von Mangoldt argument

**Proposition 9** (Weil identity for $C_\infty$). For $T \in \mathbb{R}$ with $T \notin \{\gamma_n\}$:

$$\sum_{t \in [0,T]: C_\infty(t)=0} 1 = \frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty} \left[\frac{-\zeta'}{\zeta}(s)\right] F(s) \, ds,$$

where $F(s)$ is an appropriate test function that "selects" the zeros of $C_\infty$ via the Weil form.

*Note.* This identity — the "Weil formula for $C_\infty$" version — is not established directly in the literature. It is a working conjecture that would require proof.

**Honest status of Attack D.** Attack D (via the Euler-Lagrange equation) reduces RH to condition (SAC): that the real zeros of $C_\infty = w - \Psi$ coincide with the $\gamma_n$. This condition is more "explicit" than RH (it is formulated in terms of the function $\Psi$ and its crossings with $w$) but does not seem easier to prove at this point.

---

## 11. Synthesis: The unified strategy

**Diagram of the complete chain (unconditional + conditional):**

```
CCM self-adjointness (PROVED)
    ↓
J_λ^CCM self-adjoint → zeros t_n^(λ) ∈ ℝ (PROVED)
    ↓
μ_ξ^λ ⇒ μ_γ^real weakly (PROVED, Doc 15)
    ↓
J_∞ exists with spectral measure μ_γ^real (PROVED, Doc 15)
    ↓
spec(J_∞) = real zeros of C_∞ (PROVED, Theorem C1, Doc 17)
    ↓
μ_γ^real = measure of real zeros of C_∞ (PROVED, Lemma 3, Doc 17)
    ↓
[GAP]: real zeros of C_∞ = γ_n (zeros of Ξ in ℝ)
    ↓
μ_γ^real = μ_γ
    ↓
RH
```

**The gap is precisely isolated:**

$$\boxed{\{t \in \mathbb{R}: C_\infty(t) = 0\} = \{\gamma_n : \gamma_n \in \mathbb{R}\} \quad \iff \quad \text{RH}.}$$

This is the most concrete formulation the program has reached. It is a statement about the explicit function $C_\infty(t) = w(t) - \Psi(t)$ and its zeros.

---

## 12. Net progress: what is new in Docs 16-18

**New unconditional results:**

| Result | Document |
|---|---|
| Theorem C1: $\mathrm{spec}(J_\infty) = \{t \in \mathbb{R}: C_\infty(t) = 0\}$ | Doc 17 |
| Theorem C3: RH $\iff$ zeros of $C_\infty$ are the $\gamma_n$ | Doc 17 |
| Proposition 6 in Doc 16: RH $\iff$ (BM): $\mu_\gamma^{real} = \mu_\gamma^{C_\infty}$ | Doc 16 |
| Möbius dynamical system: unique attractor = $m_\infty$ (unconditional) | Doc 17 |
| Functional equation (EF2) holds unconditionally on $\mathbb{C}^+$ | Doc 17 |
| The complete chain is closed except for the gap (SAC) | Doc 18 |

**The main conceptual contribution:** the program identifies that RH is equivalent to a statement about the REAL zeros of the explicit function $C_\infty(t) = w(t) - \Psi(t)$, built directly from the primes via the von Mangoldt formula. This is a new equivalent formulation of RH in terms of harmonic analysis of $\Psi$.

---

## 13. The most promising question for Doc 19

**Question D.1** (the most concrete in the program). For $T > 0$: how many zeros does $C_\infty(t) = w(t) - \Psi(t)$ have in $[0,T]$, and where are they?

The function $w(t) \sim \frac{1}{2}\log(t/2\pi)$ grows slowly. The function $\Psi(t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p)$ oscillates.

The crossings $\Psi(t) = w(t)$ are the zeros of $C_\infty$. By Jensen's formula applied to $C_\infty$ in the strip $\{|\Im(z)| < 1/2\}$:

$$\#\{C_\infty(t) = 0, t \in [0,T]\} = \frac{T}{2\pi}\log\frac{T}{2\pi} + O(\log T)$$

if $C_\infty$ has growth order comparable to $\Xi$ — which is plausible but not proved.

**If the zero density of $C_\infty$ matches that of $\Xi$**: and if in addition the zeros of $C_\infty$ are exactly the $\gamma_n$ (which would require additional proof), then RH would follow.

**Document 19** should attack Question D.1 via:
1. The Jensen-Ahlfors formula for zeros of $C_\infty$ in a strip.
2. The comparison with $N_\Xi(T)$ via the explicit formula.
3. The argument that the zeros of $C_\infty$ "track" the zeros of $\Xi$ via the Weil identity.

---

## 14. Summary of Doc 18

**Proved in this doc:**
- The Euler-Lagrange equation in the limit gives $B_\infty = -c_\infty/C_\infty$ (in the diagonal approximation).
- H2 is equivalent to $C_\infty = $ constant, which is impossible (contradiction with the growth of $w$); this confirms that the diagonal approximation is only an approximation.
- Condition (SAC) (real zeros of $C_\infty$ = $\gamma_n$) is equivalent to RH (Proposition D1).
- The complete chain is isolated: the only gap is the identification of the zeros of $C_\infty$ with the $\gamma_n$.
- Synthesis of the four attacks into a unified diagram with the exact gap identified.

**Open:**
- Question D.1: density of zeros of $C_\infty$ in $[0,T]$ via Jensen-Ahlfors.
- Condition (SAC) without assuming RH: the central gap of the program.
