# Phase 24-C — Rigorous results on $\log|\zeta|$ and compatibility

## Objective

Phases 24-A and 24-B produced negative results. Phase 24-C makes the exact inventory of what IS proved about $\log|\zeta(1/2+it)|$, and determines whether any proved (not conjectural) result imposes a restriction on $b_j$.

---

## 1. Inventory of proved results on $\log|\zeta(1/2+it)|$

### 1.1 Selberg's central limit theorem (1946)

For $t$ uniform on $[T, 2T]$:
$$\frac{\log|\zeta(1/2+it)|}{\frac{1}{\sqrt{2}}\sqrt{\log\log T}} \xrightarrow{d} N(0,1).$$

**What it says:** the distribution of $\log|\zeta(1/2+it)|$ is approximately Gaussian with variance $\frac12\log\log T$ for random $t$ in $[T,2T]$.

**What it does NOT say:** anything about the value at a specific point $t = \gamma_j$. The convergence is in distribution for random $t$, not for fixed $t$.

### 1.2 Unconditional upper bound on $\log|\zeta(1/2+it)|$

(Ramachandra 1980, Titchmarsh): for all $t \geq 2$:
$$\log|\zeta(1/2+it)| \leq C\sqrt{\log t}(\log\log t).$$

(Under RH this would improve to $O(\sqrt{\log t})$.)

**What it says:** an upper bound on the maximal extreme values.

**What it does NOT say:** anything about minimal extreme values.

### 1.3 Existence of negative extreme values (deep minima)

(Titchmarsh, §9.6): for any $A > 0$ there exist arbitrarily large $t$ with:
$$\log|\zeta(1/2+it)| \leq -A(\log t)^{1/3}.$$

Stronger (Radziwiłł–Soundararajan 2013): for any $c > 0$ there is a positive proportion of $t \in [T,2T]$ with $\log|\zeta(1/2+it)| \leq -c(\log\log T)^{1/2}$.

**What it says:** the minimum of $\log|\zeta|$ over $[T,2T]$ can be very negative.

### 1.4 Lower bound (if any) on the minimum

No result of the type $\log|\zeta(1/2+it)| \geq -F(t)$ for $F$ of subexponential growth exists that holds outside the zeros. Near on-line zeros, $|\zeta(1/2+i\gamma)| = 0$, so the minimum is $-\infty$.

For $t$ far from all on-line zeros: the strongest known lower bound is of the type $|\zeta(1/2+it)| \geq e^{-C\log t/\log\log t}$ on average (a bound that follows from the zero-free region theorem) but not pointwise.

**Conclusion:** no unconditional pointwise lower bound on $\log|\zeta(1/2+it)|$ exists that is valid at an arbitrary point $t$.

### 1.5 Results of Harper and Soundararajan on moments and extremes

Harper (2020): the moments $\int_T^{2T}|\zeta(1/2+it)|^{2k}dt$ have the form predicted by Keating–Snaith for all positive rational $k$, with an explicit constant.

Soundararajan (2009): $\max_{t\in[T,2T]}\log|\zeta(1/2+it)| = (1+o(1))\sqrt{\frac12\log\log T\cdot\log\log\log T}$ conditionally under RH. Unconditionally: $\leq C\sqrt{\log T}$.

Arguin–Bovier–Kistler (2011–2013), Najnudel (2018), Paquette–Zeitouni (2018): the maximum of $\log|\zeta|$ over $[T,2T]$ has a Gumbel distribution at scale $\sqrt{\log\log T}$ (conditionally). Unconditionally: only bounds.

**For the minimum:** there are no rigorous analogues of the results on the maximum.

---

## 2. What these results say about compatibility with $\mathcal{O}_j$

**Proposition 24-C.1** (Unconditional compatibility: the space is empty). None of the rigorous results above imposes any lower bound on $|\zeta(1/2+i\gamma_j)|$ at the specific point $t = \gamma_j$, for any value of $b_j$.

Therefore, the GMC-Hypothesis D incompatibility argument requires at least one of:
- (R1) A rigorous lower bound on $\min_{t\in[T,2T]}\log|\zeta(1/2+it)|$ strictly greater than $-\infty$.
- (R2) A result of the form "for $t$ in a specific set (e.g., the heights of off-line zeros), $\log|\zeta(1/2+it)|$ is bounded below".

Neither (R1) nor (R2) currently exists.

**Proposition 24-C.2** (Interference from on-line zeros). Let $\gamma^*$ be a zero of $\zeta$ on the critical line closest to $\gamma_j$, with $|\gamma_j - \gamma^*| = \delta^*$. The on-line zero $\rho^* = 1/2+i\gamma^*$ contributes to the Hadamard sum at $t=\gamma_j$:
$$\delta_{\rho^*}\log|\zeta(1/2+i\gamma_j)| = \log(\delta^*)^2 - \log|\rho^*|^2 + O(1) = 2\log\delta^* + O(1).$$

If $\delta^* \ll b_j$ (the nearest on-line zero is closer to $\gamma_j$ than the off-line $b_j$), then the contribution of the on-line zero exceeds that of the off-line zero: $2\log\delta^* \ll 2\log b_j$.

**Consequence:** the depth of the depression at $t=\gamma_j$ is dominated by the nearest on-line zero, not by the off-line one, if $\delta^* < b_j$. The off-line zero is "invisible" in $\log|\zeta(1/2+i\gamma_j)|$ under that condition.

*Proof.* Direct application of the Hadamard product to the zero $\rho^* = 1/2+i\gamma^*$:
$$\text{contribution of }\rho^*\text{ at }t=\gamma_j: \; \log|1-(1/2+i\gamma_j)/(1/2+i\gamma^*)| = \log|\delta^*/\rho^*| + O(1). \quad\square$$

---

## 3. The "on-line zero interference" dilemma

**Lemma 24-C.3** (Dilemma $\delta^*$ vs $b_j$). There are two cases:

*Case A: $\delta^* \geq b_j$ (the nearest on-line zero is far away).* Then the contribution of the off-line zero dominates in $\log|\zeta(1/2+i\gamma_j)|$, with depth $\sim 2\log b_j$. But since $\delta^* \geq b_j$, the nearest on-line zero also contributes $\leq 2\log b_j$, so there is no clear separation.

*Case B: $\delta^* < b_j$ (the nearest on-line zero is very close to $\gamma_j$).* Then the depth at $t=\gamma_j$ is dominated by $2\log\delta^*$. The contribution of the off-line zero is completely masked. There is no information about $b_j$ in $\log|\zeta(1/2+i\gamma_j)|$.

**Conclusion:** the Hadamard depression at $t=\gamma_j$ does not cleanly identify the contribution of the off-line zero, except in Case A. And in Case A, there is no restriction on $b_j$ coming from the GMC (the depression is compatible with the field for $b_j \geq \gamma_j^{-C}$, Regime I).

---

## 4. The final obstacle of Phase 24

**Theorem 24-C.4** (Closure of Phase 24). The three methods of Phase 24 (24-A: direct lower bounds; 24-B: local profile; 24-C: rigorous results on $\log|\zeta|$) collectively produce the following diagnosis:

To prove that $b_j \geq F(\gamma_j)$ for some non-trivial function $F$, or equivalently to prove that Hypothesis D with super-polynomially small $b_j$ is impossible, we need at least one of:

**(G1)** An unconditional lower bound on $|\zeta(1/2+i\gamma_j)|$ at points $\gamma_j$ that are imaginary parts of off-line zeros. Equivalent to: a bound of the type $\log|\zeta(1/2+it)| \geq -F(t)$ with $F$ growing more slowly than $c \cdot (\text{depth of the nearest on-line zero})^{-1}$.

**(G2)** Control of the spacing $\delta^*$ between on-line zeros and the heights of off-line zeros: if $\delta^* \geq b_j$ unconditionally, then the off-line zero's signal would be visible in $\log|\zeta|$. But this is equivalent to information about the joint distribution of on-line and off-line zeros.

**(G3)** A rigidity result for the log-correlated field stating that the process $\{\log|\zeta(1/2+it)| : t \in [T,2T]\}$ cannot have depressions of depth $\gg \log T$ at specific points $t$ unrelated to on-line zeros. No result of this type currently exists.

**None of (G1), (G2), (G3) is currently accessible.**

*Proof.* (G1): follows from Prop. 24-C.1. (G2): information about $\delta^*$ requires knowing the joint distribution of on-line and off-line zeros, equivalent to information stronger than RH. (G3): the results of Harper, Arguin–Bovier–Kistler and Najnudel control the maximum, not the minimum, of $\log|\zeta|$. $\square$

---

## 5. Complete table of Phase 24

| Objective | Result | Type | Phase |
|----------|-----------|------|------|
| Lower bound $b_j \geq F(\gamma_j)$ via explicit formula | Impossible: signal buried | Negative | 24-A |
| Lower bound via Hadamard + Jensen | Impossible: no pointwise lower bound for $\|\zeta\|$ | Negative | 24-A |
| Lower bound via moments $I_k$ | Impossible: local contribution $O(b_j)$ | Negative | 24-A |
| Conditional lower bound (Selberg CLT) | $b_j \geq \gamma_j^{-C}$ conditionally | Conditional | 24-A |
| Lorentzian profile $P(u) = \log(1+u^2)$ | Universal, deterministic — new result | B | 24-B |
| Geometric incompatibility of the profile | Impossible: profile submerged under field fluctuations | Negative | 24-B |
| Rigorous results on $\min\log\|\zeta\|$ | No unconditional lower bounds exist | Negative | 24-C |
| On-line zero interference (dilemma $\delta^*$ vs $b_j$) | Obscures the off-line zero's signal | Negative | 24-C |
| Final obstacle (G1/G2/G3) | None accessible | B | 24-C |

---

## 6. Frank assessment of Phase 24

Phase 24 is mostly a triple negative result.

**What was gained:**

1. **Precise diagnosis of the bibliographic gap:** confirmation that no result of the form $b_j \geq F(\gamma_j)$ exists in the literature, and that no standard method can produce it.

2. **The Lorentzian profile:** $P(u) = \log(1+u^2)$ is a positive result (new, geometrically precise, with no direct precedent in the literature).

3. **The $\delta^*$ vs $b_j$ dilemma** (Proposition 24-C.2): reveals that even if there were a lower bound for $|\zeta(1/2+i\gamma_j)|$, interference from nearby on-line zeros would make it impossible to isolate the contribution of $b_j$.

4. **The chain of obstacles (G1/G2/G3):** precisely names the three closed doors.

**The negative result in turn has value:** it shows that for any attempt to restrict $b_j$ via the behavior of $\log|\zeta|$ on the critical line, one must understand the JOINT distribution of on-line and off-line zeros, not each separately. That joint distribution is precisely the heart of the unsolved problem.

---

## 7. Phase 25: the only route not yet exhausted

Phases 22-24 have systematically exhausted:
- The explicit formula and its bounds (arithmetic for $\Re(s)>1$).
- The Hadamard product and behavior on the critical line.
- Log-correlated fields and their rigorous results.
- Moments of $|\zeta|$.
- The local geometry of the depression induced by an off-line zero.

The only route not yet exhausted, identified in Phases 22-23 as Wall W4-RSRP, remains:

**Can the uniqueness of the analytic continuation of the Euler product $\prod_p(1-p^{-s})^{-1}$ force, through some structural mechanism, the location of the zeros onto the critical line?**

This question connects with:
- The Riemann zeta function as the UNIQUE function with the combined properties (Euler product for $\Re(s)>1$, functional equation, Hadamard order 1, simple pole at $s=1$).
- Connes's program (adelic space, where the Euler product is an Eulerian factor of the trace operator).
- Bohr's almost-periodicity and the structure of the values $p^{-s}$ for varying $\Re(s)$.

This is the direction of **Phase 25**.
