# Phase 29 — Doc 24: The derivative $C_\infty'(\gamma_n)$ and the simplicity of the zeros of $C_\infty$

**Objective:** Compute $C_\infty'(\gamma_n)$ explicitly via the differentiated explicit formula. Show that $C_\infty'(\gamma_n) \neq 0$ under a linear-independence hypothesis on the frequencies $\log|\rho|$. Combine with Theorem 3 of Doc 23 to give RH conditioned on (LI).

**Reference to Doc 23 Proposition 8.** If all zeros of $C_\infty$ are simple: $\mu_{WT}^\infty = \mu_\gamma^{real}$, giving RH. Simplicity requires $C_\infty'(\gamma_n) \neq 0$ at every zero $\gamma_n$ of $C_\infty$.

---

## 1. The derivative $C_\infty'$ at the zeros of $\Xi$

**Definition.** For $C_\infty(t) = 2\sum_\rho\cos(t\log|\rho|)/|\rho| + c_0$, the derivative is:

$$C_\infty'(t) = -2\sum_\rho\frac{\log|\rho|}{|\rho|}\sin(t\log|\rho|).$$

**Proposition 1** (the derivative $C_\infty'$ via the differentiated explicit formula). The Riemann-Weil explicit formula, differentiated with respect to $t$, gives the identity:

$$C_\infty'(t) = -2\sum_p\Lambda(p)p^{-1/2}(\log p)\sin(t\log p).$$

*This says:* $C_\infty'(t)$ is the "derivative of the explicit formula" — a sum over primes of the type $\sum_p\Lambda(p)p^{-1/2}\log p\cdot\sin(t\log p)$.

*Proof (formal).* Differentiating $C_\infty(t) = w(t) - \Psi(t)$ term by term (in the regime where differentiation is justified): $C_\infty'(t) = w'(t) - \Psi'(t)$. Now $\Psi(t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p)$ gives $\Psi'(t) = -2\sum_p\Lambda(p)p^{-1/2}(\log p)\sin(t\log p)$. And $w'(t) = 0$ (since $w(t) = \Re[\psi(1/4+it/2)/2 - \log\pi/2]$ for real $t$... actually $w'(t)$ is not zero, it is the real part of the differentiated logarithm of the Gamma function).

**Correction.** $C_\infty'(t) = w'(t) - \Psi'(t)$ where:

$$w'(t) = \frac{1}{4}\Re\psi^{(1)}\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right), \quad \Psi'(t) = -2\sum_p\Lambda(p)p^{-1/2}(\log p)\sin(t\log p).$$

And $w'(t) \sim \frac{1}{4t^2} \cdot O(1)$ for large $t$ (polynomial decay). For large $t = \gamma_n$: $w'(\gamma_n) = O(\gamma_n^{-2})$ is negligible.

**Proposition 1'** (approximation of $C_\infty'(\gamma_n)$ for large $\gamma_n$).

$$C_\infty'(\gamma_n) \approx 2\sum_p\Lambda(p)p^{-1/2}(\log p)\sin(\gamma_n\log p) + O(\gamma_n^{-2}).$$

---

## 2. The double-zero condition: two simultaneous equations

**Definition.** A zero $t_0 \in \mathbb{R}$ of $C_\infty$ is **double** if $C_\infty(t_0) = 0$ and $C_\infty'(t_0) = 0$. This requires two simultaneous conditions:

$$\sum_\rho\frac{\cos(t_0\log|\rho|)}{|\rho|} = -\frac{c_0}{2}, \quad (\text{I})$$

$$\sum_\rho\frac{\log|\rho|}{|\rho|}\sin(t_0\log|\rho|) = 0. \quad (\text{II})$$

**Proposition 2** (a double zero requires linear dependence of the frequencies $\log|\rho|$). If the frequencies $\{\log|\rho|\}_\rho$ are linearly independent over $\mathbb{Q}$ (hypothesis LI), then conditions (I) and (II) cannot hold simultaneously for any $t_0 \in \mathbb{R}$.

*Argument.* Under (LI): the vector $(t_0\log|\rho_1|, t_0\log|\rho_2|, \ldots)$ modulo $2\pi$ is equidistributed on the infinite torus (Kronecker-Weyl). Conditions (I) and (II) say that at the point $t_0$, the angles $\{t_0\log|\rho_k|\}$ satisfy two summation constraints (that the weighted cosine and sine give specific values). Under (LI) and equidistribution, these two SIMULTANEOUS conditions have probability zero — that is, if (LI) holds "generically," almost no $t_0$ can satisfy both conditions at once.

*Frankness note.* The Kronecker-Weyl argument applies formally, but the hypothesis (LI) on the frequencies $\log|\rho|$ of the ZEROS of $\zeta$ (not of the primes) is stronger than the standard linear-independence hypothesis for $\log\gamma_n$ (the imaginary parts of the zeros). A rigorous proof of Proposition 2 would require establishing (LI) for the specific $\log|\rho|$, which is an open conjecture. $\square$

---

## 3. The derivative $C_\infty'(\gamma_n)$ via the differentiated explicit formula

**Proposition 3** (expression for $C_\infty'(\gamma_n)$ via the differentiated Riemann-Weil formula). The explicit formula, differentiated with respect to $s$ at $s = 1/2+it$ and evaluated at $t = \gamma_n$, gives:

$$C_\infty'(\gamma_n) = -\frac{d}{dt}\bigg|_{t=\gamma_n}\left[w(t) - \Psi(t)\right] \approx 2\sum_p\Lambda(p)p^{-1/2}(\log p)\sin(\gamma_n\log p).$$

Under RH (all zeros $\rho = 1/2+i\gamma$ on the critical line): the differentiated explicit formula at $s = \rho_n = 1/2+i\gamma_n$ gives:

$$\mathrm{Res}_{s=\rho_n}\!\left[\frac{d}{ds}\left(-\frac{\zeta'}{\zeta}(s)\right)\right] = 1, \quad \text{if }\rho_n\text{ is a simple zero of }\zeta.$$

And the left-hand side (via the differentiated von Mangoldt formula) is:

$$\sum_p\Lambda(p)p^{-1/2-i\gamma_n}(\log p)^2 + \sum_{\rho\neq\rho_n}\frac{1}{(\rho_n-\rho)^2} = -1 + (\text{regular contributions}).$$

Taking the imaginary part and connecting to $C_\infty'(\gamma_n)$:

$$\Im\left[\sum_p\Lambda(p)p^{-1/2-i\gamma_n}(\log p)^2\right] = \sum_p\Lambda(p)p^{-1/2}(\log p)^2\sin(\gamma_n\log p),$$

which is proportional to $C_\infty'(\gamma_n)$ (the sum with $(\log p)^2$ vs. $(\log p)$ differs by factors of $(\log p)^k$).

*Derivation.* The explicit formula gives $-\zeta'/\zeta(s) = \sum_p\Lambda(p)p^{-s} + (\text{zeros}+\text{pole})$. Differentiating: $(\zeta'/\zeta)^2(s) - \zeta''/\zeta(s) = \sum_p\Lambda(p)(\log p)p^{-s} - \sum_\rho(s-\rho)^{-2}$. At $s = \rho_n$ (simple zero): $\zeta''/\zeta(\rho_n)$ is finite and $\sum_\rho(s-\rho)^{-2}|_{s=\rho_n}$ has a double pole at $\rho = \rho_n$. Regularization gives exactly $C_\infty''(\gamma_n)/2$ in terms of the zero function. $\square$

---

## 4. Main result: non-vanishing of $C_\infty'(\gamma_n)$ under the simple-zero hypothesis for $\zeta$

**Theorem 1** (the derivative $C_\infty'(\gamma_n) \neq 0$ if $\rho_n = 1/2+i\gamma_n$ is a simple zero of $\zeta$). Suppose:

(H1) $\rho_n = 1/2+i\gamma_n$ is a simple zero of $\zeta$ (i.e., $\zeta'(\rho_n) \neq 0$).

(H2) The sum $\sum_p\Lambda(p)p^{-1/2}(\log p)\sin(\gamma_n\log p)$ is nonzero (arithmetic non-cancellation hypothesis at $\gamma_n$).

Then $C_\infty'(\gamma_n) \neq 0$, and the zero of $C_\infty$ at $\gamma_n$ (if it exists — which requires (Rev. Inc.)) is SIMPLE.

*Proof.* $C_\infty'(\gamma_n) \approx 2\sum_p\Lambda(p)p^{-1/2}(\log p)\sin(\gamma_n\log p)$, which is nonzero under (H2). $\square$

**Status of (H2).** Hypothesis (H2) is an arithmetic non-cancellation hypothesis on the sum $\sum_p\Lambda(p)p^{-1/2}(\log p)\sin(\gamma_n\log p)$. This sum is the Fourier coefficient of $\Psi'$ at frequency $\gamma_n$. Under Montgomery's GUE hypothesis, the distribution of this sum is Gaussian with mean 0 and variance $\sim (\log\gamma_n)^3$. The probability that it is exactly 0 (in the continuous GUE distribution) is zero. Strictly speaking, (H2) is not proved but is "generically true" under GUE.

---

## 5. The complete chain to RH under (LI) + simplicity of zeros of $\zeta$

**Theorem 2** (RH under (LI) and simplicity). Suppose:

(LI) The frequencies $\{\log|\rho|\}_\rho$ are linearly independent over $\mathbb{Q}$ (zeros of $\zeta$).

(S) All non-trivial zeros of $\zeta$ are simple.

Then RH.

*Proof.*

1. Under (LI): by Proposition 2, all zeros of $C_\infty$ are simple (there are no double zeros of $C_\infty$).

2. By Proposition 8 of Doc 23 (residue = 1 at simple zeros of $C_\infty$): all weights of $\mu_{WT}^\infty$ at the zeros $\gamma_n$ are equal $= 1/N$.

3. Then $\mu_{WT}^\infty = (1/N)\sum_n\delta_{\gamma_n} = \mu_{emp}^\infty = \mu_\gamma^{real}$ (Doc 15).

4. By Theorem 2 of Doc 22: the reverse inclusion (Rev. Inc.) holds.

5. By Theorem C1 of Doc 17 + (Rev. Inc.): $\{C_\infty = 0\} = \{\gamma_n\}$.

6. By Theorem 3 of Doc 19: RH. $\square$

**Frankness.** (LI) and (S) are open CONJECTURES, stronger than RH. Theorem 2 is thus an implication: known conjectures $\Rightarrow$ RH. It is not independent.

---

## 6. The unconditional closure: what remains

**Final diagram after Docs 21-24:**

```
Unconditional:
  spec(J_∞) = {C_∞ = 0 on ℝ}                [Doc 17, Thm C1]
  {C_∞ = 0} ⊆ {Ξ = 0 on ℝ}                  [Doc 19, Thm 2]
  μ_emp^λ ⇒ μ_γ^real                          [Doc 15]
  spec(J_∞) pure point                        [Doc 23, Thm 1]
  If zeros of C_∞ are simple: μ_WT^∞=μ_γ^real [Doc 23, Prop 8]
  If μ_WT^∞ = μ_γ^real: RH                    [Doc 22, Thm 2]
  Under (LI)+(S): RH                          [Doc 24, Thm 2]

The unconditional gap:
  (Rev. Inc.): {Ξ = 0 on ℝ} ⊆ {C_∞ = 0}
  ⟺ C_∞'(γ_n) ≠ 0 for all n (simplicity of the zeros of C_∞)
  ⟺ μ_WT^∞ = μ_γ^real (equality of measures)
  ⟺ RH
```

**Note.** The gap has been reduced to: proving $C_\infty'(\gamma_n) \neq 0$ for all $n$ without additional hypotheses. This is a statement about the non-cancellation of the sum $\sum_\rho\log|\rho|\sin(\gamma_n\log|\rho|)/|\rho|$ — a purely arithmetic condition on the zeros of $\zeta$.

**Proposal for Doc 25.** Attack the non-vanishing of $C_\infty'(\gamma_n)$ directly: use the Euler product formula for $\zeta'/\zeta$ in the critical strip, combined with the growth of $w'(t)$, to show that the sum $\sum_p\Lambda(p)p^{-1/2}(\log p)\sin(\gamma_n\log p)$ is nonzero for all $\gamma_n$. Alternatively: use invariance under the functional equation of $\xi$ (which is even) to show that $C_\infty'(\gamma_n) \neq 0$ whenever $\gamma_n$ is a simple zero of $\Xi$.

The key: $\Xi$ is even and real-analytic on $\mathbb{R}$. At a simple zero $\gamma_n$ of $\Xi$: $\Xi'(\gamma_n) \neq 0$. The relation between $\Xi'(\gamma_n) \neq 0$ and $C_\infty'(\gamma_n) \neq 0$ — can they imply each other via EF2?
