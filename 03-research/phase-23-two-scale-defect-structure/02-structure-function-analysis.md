# Phase 23 — Step 23-B: Analysis of the structure function $S_2$

## The central argument: lower and upper bound

Definition (from Phase 22):
$$S_2(\tau, T) = \frac{1}{T}\int_0^T |X(t+\tau)-X(t)|^2\,dt, \qquad X(t) = \frac{\psi(e^t)-e^t}{e^{t/2}}$$

### Lower bound (proved in Phase 22)

**Proposition 23-B.1** (Lower bound under Hypothesis D). For $\tau \neq 2\pi k/\gamma_j$ ($k \in \mathbb{Z}$):
$$S_2(\tau, T) \geq \frac{A_j^2(e^{2b_j T}-1)}{2b_j T} \sin^2(\gamma_j\tau/2) + O(e^{b_j T}/\sqrt{T})$$

where $A_j = 2/|\rho_j^+|$. Asymptotically $S_2(\tau,T) \gg e^{2b_j T}/T$.

*Proof*. From Proposition 22-D.2, the dominant term of $|X(t+\tau)-X(t)|^2$ is the square of the defect $|Y(t+\tau)-Y(t)|^2$ where $Y(t) = D_m(e^t)/e^{t/2}$. Direct computation gives the bound. $\square$

### Upper bound (from the Korobov-Vinogradov PNT)

**Proposition 23-B.2** (Unconditional upper bound). By the unconditional prime number theorem (Korobov-Vinogradov), for all $t > 0$:
$$|X(t)| = \frac{|\psi(e^t)-e^t|}{e^{t/2}} \leq C e^{t/2} \exp(-c_1\sqrt{t})$$

for absolute constants $c_1, C > 0$.

Hence:
$$S_2(\tau, T) \leq \frac{2}{T}\int_0^T (|X(t+\tau)|^2 + |X(t)|^2)\,dt \leq \frac{C}{T}\int_0^T e^t e^{-2c_1\sqrt{t}}\,dt$$

The integral: $\int_0^T e^t e^{-2c_1\sqrt{t}}\,dt \leq C_2 e^T e^{-2c_1\sqrt{T}}$ (dominated by the term $t=T$).

Hence:
$$S_2(\tau, T) \leq C_3 e^T e^{-2c_1\sqrt{T}}$$

*Proof*. Direct estimate using the Korobov-Vinogradov bound on $|X(t)|$. $\square$

---

## Compatibility analysis

**Theorem 23-B.3** (Compatibility of the bounds). The two bounds are compatible: the lower bound under Hypothesis D does not exceed the unconditional upper bound.

Under Hypothesis D: $S_2(\tau,T) \gg e^{2b_j T}$.
Unconditional: $S_2(\tau,T) \leq C e^T e^{-c\sqrt{T}}$.

For a contradiction we would need: $e^{2b_j T} \gg e^T e^{-c\sqrt{T}}$, i.e. $2b_j > 1 - c/\sqrt{T}$. For large $T$: $2b_j \geq 1$, i.e. $b_j \geq 1/2$. But $b_j = \sigma_j - 1/2 < 1/2$ always (since $\sigma_j < 1$). **There is no contradiction.**

*Proof*. For any $b_j \in (0, 1/2)$: $2b_j < 1$, so $e^{2b_j T} / (e^T e^{-c\sqrt{T}}) = e^{(2b_j-1)T+c\sqrt{T}} = e^{-(1-2b_j)T+c\sqrt{T}} \to 0$. The bounds are compatible. $\square$

**Remark**: This theorem is the precise analogue of Proposition 22-C.5 (Paley-Wiener boundary). Both establish the same conclusion: the exact boundary of current methods is $b_j = 1/2$ (i.e. $\sigma_j = 1$), which is impossible for zeros of $\zeta$.

---

## The spectrum of $X_0(t)$ and its structure function

To complete the picture, we compute the structure function of the on-line component $X_0(t) = -2\mathrm{Re}\,\sum_{Z_{\rm CL}} x^\rho/\rho|_{x=e^t}$.

**Proposition 23-B.4** (Structure function of $X_0$). Under the hypothesis that the on-line zeros satisfy $\sum_\rho 1/|\rho|^2 < \infty$ (which follows from the standard zero distribution):
$$\lim_{T\to\infty} S_2^{X_0}(\tau, T) = 8\sum_{\rho \in Z_{\rm CL}} \frac{\sin^2(\gamma\tau/2)}{|\rho|^2} < \infty$$

*Proof*. $X_0(t) = -2\sum_\gamma |\rho|^{-1}\cos(\gamma t - \theta)$. The structure function:
$$S_2^{X_0}(\tau, T) = \frac{1}{T}\int_0^T |X_0(t+\tau)-X_0(t)|^2 dt$$
$$= \frac{16}{T}\sum_{\gamma,\gamma'} \frac{\sin(\gamma\tau/2)\sin(\gamma'\tau/2)}{|\rho||\rho'|} \int_0^T \sin(\gamma t)\sin(\gamma't) dt + O(1)$$

The diagonal terms contribute $8\sin^2(\gamma\tau/2)/|\rho|^2$ (using $\frac{1}{T}\int_0^T \sin^2(\gamma t)dt \to 1/2$). The off-diagonal terms are $O(1/(T|\gamma-\gamma'|))$, which tend to 0. The convergence of $\sum_\rho 1/|\rho|^2$ guarantees that the limit exists and is finite. $\square$

**Corollary 23-B.5**: $S_2^{X_0}(\tau, T) = C_\tau + O(1/T)$ where $C_\tau = 8\sum_\rho \sin^2(\gamma\tau/2)/|\rho|^2$ is a finite constant depending on $\tau$.

**Consequence**: The structure function of the on-line component $X_0$ is BOUNDED (converges to a constant). The exponential divergence of $S_2^X$ under Hypothesis D comes ENTIRELY from the defect $D_m$.

---

## Summary: the three scales of the defect

| Scale | Variable | Effect of the off-line zero | Unconditional bound | Contradiction? |
|--------|----------|-------------------------------|-------------------|-----------------|
| $x$ (prime counting) | $D_j(x) \asymp x^{1/2+b_j}$ | Algebraic growth | $\psi-x = O(xe^{-c\sqrt{\log x}})$ | No ($b_j < 1/2$) |
| $t = \log x$ (structure function) | $S_2 \gg e^{2b_j T}$ | Exponential growth | $S_2 \leq Ce^T e^{-c\sqrt{T}}$ | No ($2b_j < 1$) |
| $t$ (imaginary heights of $\zeta$) | $\delta_j\log|\zeta| \sim 2\log b_j$ | Local depression of depth $O(\log\log\gamma_j)$ | GMC: fluctuation $\sim (\log\log T)^{1/2}$ | No (compatible) |

**Conclusion of Step 23-B**: The three scales are internally consistent and none produces a contradiction.

---

## The precise fundamental obstacle

**Theorem 23-B.6** (Precise formulation of the obstacle). The following three statements are simultaneously consistent with known results:

1. $\zeta$ has a zero at $\sigma_j + i\gamma_j$ with $\sigma_j \in (1/2, 1)$.
2. $S_2(\tau, T) \gg e^{2b_j T}$ (exponential divergence of the structure function).
3. $S_2(\tau, T) \leq C e^T e^{-c\sqrt{T}}$ (Korobov-Vinogradov upper bound).

To obtain a contradiction between (2) and (3) we need a bound $\psi(x)-x = o(x^{1/2+\varepsilon})$ for some $\varepsilon < b_j$. Such a bound is equivalent to there being no zeros with $\Re(\rho) > 1/2 + \varepsilon$. This is **circular**.

*Proof*. (1)–(3) are compatible as shown by Theorem 23-B.3. To contradict (1)+(2) with (3), we would need $e^{2b_j T} \gg e^T e^{-c\sqrt{T}}$, which requires $b_j > 1/2$, impossible. Alternatively, a bound $\psi-x = O(x^{1/2+\varepsilon})$ with $\varepsilon < b_j$ would give $S_2 \leq C e^{(1+2\varepsilon)T/2}$ (instead of $e^T$), and for $\varepsilon < b_j$ this would contradict (2). But such a bound is exactly the non-existence of zeros with $\Re(\rho) > 1/2+\varepsilon$. Circular. $\square$
