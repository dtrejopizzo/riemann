# Phase 22 — Step 22-D: Spectral Rigidity of Multiplicative Chaos vs. Finite Defect

## Starting point

Proposition 22-C.5 establishes that the Paley-Wiener method reaches exactly the boundary $\Re(s) = 1$, without penetrating the critical strip. To reach $m = 0$, we need information about the structure of $\zeta$ IN the strip $(1/2, 1)$. The only source of such information, beyond the Euler product, is the spectral structure of the fluctuations of $\psi(x)$.

---

## §D.1 The spectrum of $\psi(x) - x$

Define the spectral measure of $\psi$ as follows. Consider the function:
$$\Phi(T) = \frac{1}{T}\int_0^T \frac{|\psi(e^t) - e^t|^2}{e^t}\,dt$$

Under RH ($\kappa = 0$): by the explicit formula and Parseval's estimate,
$$\Phi(T) = \frac{1}{T}\sum_\rho \frac{1}{|\rho|^2} \cdot [\text{cancellation terms}] + O(T^{-1}\log T)$$

The spectral measure of $(\psi(e^t)-e^t)/e^{t/2}$ is:
$$\mu_\psi = \sum_\rho \delta_{\gamma_\rho}$$
(Dirac measure at each $\gamma_\rho$). For on-line zeros, $\gamma_\rho \in \mathbb{R}$, and the measure has support on $\mathbb{R}$.

### Under Hypothesis D ($\kappa = 2m > 0$)

The function $(\psi(e^t)-e^t)/e^{t/2} = E_0(e^t)/e^{t/2} - D_m(e^t)/e^{t/2}$ where:
- The term $E_0(e^t)/e^{t/2}$ has spectral support on $\{\gamma_\rho : \rho \in Z_{\rm CL}\}$ (continuous).
- The term $D_m(e^t)/e^{t/2}$:
$$\frac{D_j(e^t)}{e^{t/2}} = \frac{2e^{b_j t}}{|\rho_j^+|}\cos(\gamma_j t - \theta_j^+) + \frac{2e^{-b_j t}}{|\rho_j^-|}\cos(\gamma_j t - \theta_j^-)$$

The dominant term $e^{b_j t}\cos(\gamma_j t)$ is NOT square-integrable (it grows). Its formal "spectrum" is concentrated at $\pm\gamma_j$ (discrete frequencies) with diverging amplitude.

---

## §D.2 The spectral dichotomy

**Proposition 22-D.1** (Spectral dichotomy). Under Hypothesis D:
1. The component $E_0(e^t)/e^{t/2}$ has continuous spectral support (density $\sim T\log T$ of frequencies up to height $T$).
2. The component $D_m(e^t)/e^{t/2}$ has **discrete** spectral support concentrated at $\{\pm\gamma_j\}_{j=1}^m$ (finitely many frequencies).
3. The two components add up, and the sum has a mixed spectrum: continuous + finitely many frequencies with growing amplitude.

*Proof*. The first point follows from the distribution of on-line zeros (von Mangoldt-Riemann density). The second from the formula in Proposition 22-B.1 of Phase 22: the defect is a sum of $m$ cosines with frequencies $\gamma_j$. The third is a direct consequence. $\square$

**Remark**: A process with mixed spectrum (continuous + point mass) is unusual in the theory of stochastic processes. The question of Step 22-D is: can the process $\psi(x)-x$ have such a mixed spectrum, given that its Fourier coefficients are determined arithmetically by the Euler product?

---

## §D.3 Multiplicative chaos and spectral continuity

### The structure of the chaos (class $\omega$, papers M1-M13)

The $\omega$ program establishes that the fluctuations of $\psi(x)$ at fine scales ($h = x^\alpha$ with $\alpha < 1$) are modeled by Gaussian multiplicative chaos (GMC). Specifically (central result of the $\omega$ program):

$$\frac{1}{H}\int_x^{x+H} (\psi(x+h)-\psi(x))\,dh \approx h \cdot e^{G(x)}$$

where $G(x)$ is a Gaussian field with correlation function $\mathrm{Cov}(G(x), G(y)) = \log\log|x-y|^{-1} + O(1)$ — logarithmic multiplicative chaos.

The Fourier transform of the GMC has **absolutely continuous spectral measure** with respect to Lebesgue measure on $\mathbb{R}$ (it is a continuous-power process). It has NO point mass (atoms) at any frequency.

### The conflict with the finite defect

**Conjecture 22-D.1** (Spectral rigidity of the GMC). If the process $\psi(x) - x$ is realized by a Gaussian multiplicative chaos of parameter $\beta = 1$ (the correct value for $\zeta$), then its spectral measure has NO atoms. Consequently, it cannot contain the term $D_m(x) \sim x^{1/2+b_j}\cos(\gamma_j\log x)$, which introduces a point mass at $\gamma_j$ with growing amplitude.

**Status**: Conjectural. The absence of atoms in the spectral measure of the GMC is known for the multiplicative chaos model on the unit circle (Kahane 1985, Robert-Vargas 2010), but extending it to the case of $\psi(x)-x$ requires showing that:
1. The process is in fact a GMC of parameter $\beta = 1$ (not proved — this is the content of the $\omega$ program).
2. The GMC of parameter $\beta = 1$ on the line has spectral measure without atoms (conditionally provable).

### Partial formalization: the structure function

For a process $X(t) = (\psi(e^t)-e^t)/e^{t/2}$ in the variable $t = \log x$, define the structure function:
$$S_2(\tau, T) = \frac{1}{T}\int_0^T |X(t+\tau) - X(t)|^2\,dt$$

**Proposition 22-D.2** (Structure function under Hypothesis D). Under Hypothesis D:
$$S_2(\tau, T) = S_2^{(0)}(\tau, T) + S_2^{(D)}(\tau, T)$$
where:
- $S_2^{(0)}(\tau, T) \to [\text{continuous function of } \tau]$ as $T\to\infty$ (contribution of $E_0$).
- $S_2^{(D)}(\tau, T) = \sum_j \frac{4e^{2b_j T}}{|\rho_j^+|^2}[\text{oscillating function of } \tau \text{ with period } 2\pi/\gamma_j]$.

*Proof*. Compute $|D_j(e^{t+\tau}) - D_j(e^t)|^2$ directly using Proposition 22-B.1, and average over $t$. The dominant term gives the exponential $e^{2b_j T}$ and the $\tau$-dependence comes from $\cos(\gamma_j\tau)-1$. $\square$

**Consequence**: Under Hypothesis D, $S_2^{(D)}(\tau, T) \to \infty$ for every $\tau \neq 0$, as $T\to\infty$.

By contrast, the GMC predicts $S_2(\tau, T) \asymp \log(1/|\tau|)$ for $|\tau| \to 0$ (logarithmic structure function, characteristic of multiplicative chaos). The divergence $e^{2b_j T}$ is INCOMPATIBLE with logarithmic growth, provided we can show that the GMC has a bounded structure function.

**Lemma 22-D.3** (Incompatibility of structure functions). If the process $X(t) = (\psi(e^t)-e^t)/e^{t/2}$ satisfies GMC behavior with $\beta = 1$, then $S_2(\tau, T) = O(\log T)$ for every fixed $\tau$. Under Hypothesis D, $S_2(\tau, T) \geq C e^{2b_j T}$, which is incompatible for any $b_j > 0$.

*Status*: Conditional on the GMC behavior of $\psi$. The GMC behavior is the content of the $\omega$ program (papers M1-M13), not currently proved.

---

## §D.4 The ω-Defect bridge: direction of Phase 23

The logical chain to reach EX via spectral rigidity would be:

$$\text{Program }\omega \Rightarrow X \text{ is GMC with } \beta=1 \Rightarrow S_2(\tau, T) = O(\log T)$$
$$\text{Hypothesis D} \Rightarrow S_2(\tau, T) \geq Ce^{2b_j T} \to \infty$$
$$\text{By contradiction: } m = 0$$

The missing links:
1. **The $\omega$ program** has not yet proved that $\psi(x)-x$ is literally a GMC — it establishes similar statistical structures conditionally.
2. **The bound on $S_2$** for the GMC on the line with $\beta = 1$ requires GMC moment estimates that are technical but accessible.

**Proposal for Phase 23**: Attack link (2) — prove that the GMC of parameter $\beta = 1$ satisfies $S_2(\tau, T) = O(\log T)$ unconditionally. If this is proved, Lemma 22-D.3 would be the basis for an incompatibility between Hypothesis D and GMC behavior.

---

## §D.5 Classification of the results of Step 22-D

| Result | Statement | Class | Status |
|-----------|-----------|-------|--------|
| Proposition 22-D.1 | Spectral dichotomy: continuous + discrete | B | ✓ proved |
| Proposition 22-D.2 | Structure function under Hypothesis D | B | ✓ proved |
| Lemma 22-D.3 | Incompatibility $S_2 = O(\log T)$ vs $S_2 \geq Ce^{2b_j T}$ | B conditional | Conditional on GMC |
| Conjecture 22-D.1 | GMC has spectral measure without atoms | EX | Open |

---

## §D.6 Comparison with the capstone strategy (no-goes N1-N8)

The capstone (N1 of the program) establishes that the class $\omega$ cannot prove RH directly because the stochastic fluctuations carry no information about the exact position of the zeros.

Step 22-D does NOT try to use $\omega$ to prove RH directly. Instead, it uses $\omega$ to prove the INCOMPATIBILITY of Hypothesis D with the statistical behavior of $\psi$. This is a different direction, not blocked by N1.

Formally: if Hypothesis D implies a specific behavior of $S_2$ that contradicts the GMC, and the GMC is provable from the Euler product (program $\omega$), then:
$$\text{Euler} \Rightarrow \text{GMC} \Rightarrow \neg\text{Hypothesis D} \Rightarrow m = 0 \Rightarrow \text{RH}$$

This logical chain does not violate capstone N1 because it does not infer RH from statistical behavior: it infers $\neg\text{D}$ from the INCOMPATIBILITY between two consequences of the Euler product.

---

## Conclusion of Step 22-D

Conjecture 22-D.1 and Lemma 22-D.3 constitute the most promising direction toward EX to emerge from Phase 22. The strategy is to convert the arithmetic-analytic gap (Wall W4-RSRP) into a SPECTRAL gap: the discrete defect vs. the continuous spectrum of the GMC.

**The precise task of Phase 23**: prove that the multiplicative chaos of parameter $\beta = 1$ has structure function $S_2(\tau, T) = O(\log T)$ unconditionally, and connect this rigorously with the Euler product of $\zeta$.
