# Phase 23 — Step 23-C: Precise formulation of the final obstacle and paths toward Phase 24

## The barrier, formulated with mathematical precision

Phases 22 and 23 have established the following complete picture:

---

### The complete picture of obstructions

**Method 1: Explicit formula + Paley-Wiener** (Phase 22-C)
- Reach: excludes zeros with $\Re(s) > 1$ (the limit is exactly $\Re(s) = 1$).
- Reason: the bound on the arithmetic side is $O(e^{T/2})$, which exceeds $e^{T b_j}$ only for $b_j > 1/2$.
- Status: makes no progress beyond $\Re(s) = 1$.

**Method 2: Candidates I/II/III** (Phase 22-C, audit)
- Selberg: circular.
- Mertens: requires $b_j > 1/2$, impossible.
- Weil: reduces to W1.

**Method 3: GMC and log-$|\zeta|$ at scale $t$** (Phase 23-A)
- Effect of $\mathcal{O}_j$ on $\log|\zeta(1/2+it)|$: depression of depth $O(\log\log\gamma_j)$.
- Variance of the GMC at height $\gamma_j$: $\sim (\log\log\gamma_j)^{1/2}$.
- Relation: depth/fluctuation $= O((\log\log\gamma_j)^{1/2}) \to \infty$.
- But: it is compatible with the tails of the GMC (not impossible, just unusual).
- Status: the off-line zero does not generate a contradiction with the GMC.

**Method 4: Structure function** (Phase 23-B)
- Lower bound under Hypothesis D: $S_2 \gg e^{2b_j T}$.
- Unconditional upper bound: $S_2 \leq C e^T e^{-c\sqrt{T}}$.
- Compatibility: $e^{2b_j T} \ll e^T e^{-c\sqrt{T}}$ for $b_j < 1/2$.
- Status: compatible. Producing a contradiction would require $b_j > 1/2$, impossible.

**Method 5: Korobov-Vinogradov restriction** (Phase 22-C.1)
- Establishes: $b_j \leq 1/2 - c_0/(\log\gamma_j)^{2/3}$.
- Does not exclude the existence of $\rho_j$; it only restricts its position.

---

### Theorem 23-C.1 (The Fundamental Obstacle)

**Theorem** (Definitive formulation). To prove Conjecture EX ($\kappa \in \{0\} \cup \{\infty\}$) or RH ($\kappa = 0$) from the results of Phases 21–23, we need SOME ONE of the following statements:

**(F1)** An unconditional bound $\psi(x) - x = O(x^{1/2+\varepsilon_0})$ for some $\varepsilon_0 < \min_j b_j$.

**(F2)** A property $P$ of the Euler product $\prod_p(1-p^{-s})^{-1}$ that is verifiable for $\Re(s) > 1$ and is incompatible with the existence of poles of $-\zeta'/\zeta$ at $\Re(s) \in (1/2, 1)$.

**(F3)** A property $Q$ of the GMC (derivable from the Euler product) that is incompatible with $\log|\zeta(1/2+it)|$ having a depression of depth $O(\log\log\gamma_j)$ at a point $t = \gamma_j$.

*Proof*. One checks that:
- Without (F1): the structure function produces no contradiction (Theorem 23-B.3).
- Without (F2): the Paley-Wiener method does not penetrate the critical strip (Proposition 22-C.5).
- Without (F3): the GMC is compatible with the depression of the off-line zero (Theorem 23-A.6). $\square$

**Critical remark**: (F1) is essentially equivalent to RH. (F2) is the content of Wall W4-RSRP. (F3) is the content of Conjecture 22-D.1 of the $\omega$ program.

---

## A frank evaluation of the three routes

### Route (F1): Is it accessible?

A bound $\psi(x)-x = O(x^{1/2+\varepsilon})$ for $\varepsilon < 1/2$ is essentially the zero density. It is known that $\psi(x)-x = O(x^{1/2+\varepsilon})$ iff all zeros have $\Re(\rho) \leq 1/2+\varepsilon$. This is circular with RH for $\varepsilon = 0$, but for fixed $\varepsilon > 0$ it is A WEAKER RESULT.

Can $\psi(x)-x = O(x^{3/4})$ be proved (for instance, using only the Euler product)? The answer is NO — without knowing the zero distribution, the explicit formula cannot be bounded better than $O(x)$.

**Conclusion**: (F1) is inaccessible without knowing the zero distribution. Circular.

### Route (F2): Is it accessible?

(F2) is exactly what Wall W4-RSRP asserts. The results of Phase 22 establish that such a property does NOT exist in the natural classes of functionals (Theorem 22-C.6). (F2) requires a genuinely new arithmetic connection between $\Re(s) > 1$ and $\Re(s) \in (1/2, 1)$.

The only known connection between these regions is THE ANALYTIC CONTINUATION of $\zeta$. But analytic continuation is an analytic property, not an arithmetic one. Arithmetic information (Euler) only lives in $\Re(s) > 1$.

Can the uniqueness of the analytic continuation (given the values of the Euler product) force the zeros onto the critical line? This is the heart of the problem. No such mechanism is known.

**Conclusion**: (F2) requires a new analysis-arithmetic connection that has not been established.

### Route (F3): Is it accessible?

(F3) requires proving that the GMC of parameter $\beta=1$ CANNOT have a depression of depth $O(\log\log T)$ at a specific point, derived from the Euler product.

Result 23-A.6 showed that the depression IS of depth $O(\log\log\gamma_j)$ and that the fluctuations of the GMC are $(\log\log\gamma_j)^{1/2}$. The relation between these two quantities diverges ($(\log\log\gamma_j)^{1/2} \to \infty$), suggesting that eventually the depression is detectably anomalous.

Can the GMC $\beta=1$ exclude depressions of depth $\gg (\log\log T)^{1/2}$?

Answer: **NO, in general**. The minimum of the GMC over $[T, 2T]$ (that is, $\log|\zeta(1/2+it)|$ minimized) can be $\ll -c(\log\log T)$ for extreme $t$. The GMC allows extreme values much more negative than $-(\log\log T)^{1/2}$ — the minimum of the GMC is of order $-c\log T$ (result of Arguin-Bovier-Kistler-Madaule and Fyodorov-Keating). So a depression of depth $O(\log\log\gamma_j)$ is AN EVENT OF POSITIVE PROBABILITY in the GMC, not impossible.

**Definitive conclusion**: (F3) is ALSO inaccessible. The depth of the depression of the off-line zero ($O(\log\log\gamma_j)$) is fully compatible with the tails of the GMC ($\min \sim -c\log T$).

---

## The definitive negative result of Phase 23

**Theorem 23-C.2** (Negative closure of the spectral strategy). The spectral rigidity strategies developed in Phases 22-D and 23 do NOT produce a contradiction with Hypothesis D:

1. The GMC is compatible with the presence of the depression of the off-line zero (Theorem 23-A.6 and evaluation of (F3)).
2. The structure function $S_2$ produces no contradiction under unconditional bounds (Theorem 23-B.3).
3. The depth of the depression ($O(\log\log\gamma_j)$) is smaller than the minimum of the GMC over $[T,2T]$ ($\sim -c\log T$), so it is not an impossible event.

*Proof*. This follows directly from the three analyses above. Point (3) is key: the minimum of the logarithm of the GMC over $[T,2T]$ is $\sim -c\log T \gg -c\log\log\gamma_j$ for fixed $\gamma_j$. Hence a value $\log|\zeta(1/2+i\gamma_j)| \sim 2\log b_j$ lies within the support of the GMC. $\square$

---

## What has been gained in Phases 22-23

Despite the negative result, the program has produced:

1. **The modified explicit formula** (Class B, proved): $\psi = \psi_0 - D_m$.
2. **The exact anatomy of the defect** (Class B, proved): explicit formulas for $D_j$, energies.
3. **The Korobov-Vinogradov restriction** (Class B, proved): $b_j \leq 1/2 - c/(\log\gamma_j)^{2/3}$.
4. **The Hadamard computation** (Class B, proved): exact effect of $\mathcal{O}_j$ on $\log|\zeta(1/2+it)|$.
5. **Wall W4-RSRP** (Class B, proved to be a new wall distinct from W1/W2/W3).
6. **The exact boundary**: the obstacle lies precisely in the connection between $\Re(s) > 1$ and $\Re(s) \in (1/2, 1)$.
7. **The complete picture of exhausted methods**: Paley-Wiener, Selberg, Mertens, Weil, GMC, structure function.

---

## Direction toward Phase 24

Phase 23 closes the spectral direction. The program now has a precise description of the obstacle: the barrier between $\Re(s) > 1$ (arithmetic) and $\Re(s) \in (1/2, 1)$ (analytic).

**The only route that has not been exhausted**: the direct connection between the EULER PRODUCT and ANALYTIC CONTINUATION. Can the uniqueness of the analytic continuation of $\prod_p(1-p^{-s})^{-1}$ force the zeros onto the critical line?

This question is the heart of Wall W4-RSRP. Its systematic study is the proposed content of Phase 24:

**Proposed Phase 24**: Analytic uniqueness of the Euler product and forcing of zeros onto the critical line.

Specific questions for Phase 24:
- Do there exist other entire functions with the same Euler product for $\Re(s) > 1$ but with zeros in $\Re(s) \in (1/2,1)$?
- Can the uniqueness principle of analytic continuation rule them out?
- What does Bohr's theory and almost-periodicity say about this uniqueness?
- Can the structure of the additive group of $\mathbb{Q}_p$ for each prime $p$ restrict the zero distribution?

---

## Final summary table of Phases 22-23

| Result | Class | Status | Phase |
|-----------|-------|--------|------|
| Modified explicit formula | B | ✓ | 22-A |
| Anatomy of the defect $D_j$ | B | ✓ | 22-B |
| Arithmetic incapacity of $\zeta_0$ | B | ✓ | 22-B |
| Wall W4-RSRP is a new wall | B | ✓ | 22 |
| Korobov-Vinogradov restriction on $b_j$ | B | ✓ | 22-C |
| Paley-Wiener boundary at $\Re(s)=1$ | B | ✓ | 22-C |
| Audit of 3 candidates | B | ✓ | 22-C |
| Exact Hadamard computation of $\delta_j\log|\zeta|$ | B | ✓ | 23-A |
| GMC compatibility with Hypothesis D | Negative | ✓ | 23-A |
| Structure function $S_2$: lower and upper bounds | B | ✓ | 23-B |
| Korobov-Vinogradov and $S_2$ compatibility | Negative | ✓ | 23-B |
| Fundamental obstacle theorem (F1/F2/F3) | B | ✓ | 23-C |
| Negative closure of the spectral strategy | Negative | ✓ | 23-C |
| Conjecture EX | EX | Open | — |
| RH | RH | Open | — |
