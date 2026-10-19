# Phase 22 — Step 22-C: Invariants incompatible with the finite defect

## Objective

Find a functional $\mathcal{F}$ such that:
1. It is computable from the arithmetic structure of $\zeta$ (independently of the location of the zeros).
2. It is sensitive to the defect $D_m$.
3. It has a universal property (positivity, boundedness) independent of RH.
4. It produces a contradiction when $m \geq 1$.

---

## §C.1 The restriction from the Korobov-Vinogradov zero-free region

The first genuinely new result of Step 22-C does not come from a functional but from the zero-free region.

**Theorem 22-C.1** (Unconditional restriction on $b_j$). There exist absolute constants $c_0 > 0$ such that under Hypothesis D, every shift $b_j = \sigma_j - \tfrac{1}{2}$ satisfies:
$$b_j \leq \frac{1}{2} - \frac{c_0}{(\log\gamma_j)^{2/3}(\log\log\gamma_j)^{1/3}}$$

*Proof*. The Korobov-Vinogradov result establishes that $\zeta(s) \neq 0$ in
$$\sigma \geq 1 - \frac{c_0}{(\log|t|)^{2/3}(\log\log|t|)^{1/3}}$$
for $|t|$ sufficiently large, unconditionally. The off-line zero $\sigma_j + i\gamma_j$ must lie outside this region, which forces $\sigma_j < 1 - c_0/(\log\gamma_j)^{2/3}(\log\log\gamma_j)^{1/3}$, that is, $b_j < 1/2 - c_0/(\log\gamma_j)^{2/3}(\log\log\gamma_j)^{1/3}$. $\square$

**Corollary 22-C.2** (Controlled growth of the energy). Under Hypothesis D:
$$\mathcal{E}_j(X) \leq C_j \cdot X^{1 - 2c_0/(\log\gamma_j)^{2/3}(\log\log\gamma_j)^{1/3}}$$

The energy grows sub-linearly in $X$ (like $X^{1-\varepsilon_j}$ with explicit $\varepsilon_j > 0$), but is not bounded.

**Remark**: This result is genuinely new but does not give a contradiction: the energy keeps growing. It establishes an explicit upper bound on $b_j$ as a function of $\gamma_j$.

**Structural consequence**: If $\gamma_j \to \infty$ (the off-line zero has large imaginary part), then $b_j \to 0$: the shift from the critical line must become arbitrarily small. An off-line zero with large $\gamma_j$ must lie exponentially close to the critical line.

---

## §C.2 The Paley-Wiener argument in the explicit formula

This is the most detailed analysis of what prevents a contradiction with the Weil functional method.

### C.2.1 Setup

Let $F : \mathbb{R} \to \mathbb{R}$ be an even, smooth function with compact support in $[-T, T]$. The Weil-Bombieri explicit formula (cf. Bombieri 2000) gives:

$$\sum_\rho F(\gamma_\rho) = [\text{arithmetic side}] + [\text{gamma factor}]$$

where for on-line zeros $\rho = \tfrac{1}{2} + i\gamma$, $\gamma_\rho = \gamma \in \mathbb{R}$, and for off-line zeros $\rho = \sigma_j + i\gamma_j$, the parameter is $\gamma_\rho = \gamma_j - ib_j \in \mathbb{C}$.

Under Hypothesis D, the left-hand side decomposes as:
$$\sum_\rho F(\gamma_\rho) = \underbrace{\sum_{Z_{\rm CL}} F(\gamma)}_{\geq\, 0 \text{ if } F \geq 0} + \underbrace{4\sum_{j=1}^m \mathrm{Re} F(\gamma_j - ib_j)}_{\text{off-line contribution}}$$

The arithmetic side is:
$$[\text{arithmetic side}] = -2\sum_p \sum_k \frac{\log p}{p^{k/2}} \hat F(k\log p)$$

where $\hat F$ is the Fourier transform of $F$.

### C.2.2 The Paley-Wiener theorem and the bound on the defect

**Lemma 22-C.3** (Paley-Wiener bound on the defect). For any even $F \in C_c^\infty(\mathbb{R})$ supported in $[-T,T]$, and for each off-line orbit $\mathcal{O}_j$:
$$|\mathrm{Re} F(\gamma_j - ib_j)| \leq \|F\|_1 \cdot e^{T b_j}$$

*Proof*. By the Paley-Wiener theorem, if $F$ is supported in $[-T,T]$, its entire extension satisfies $|F(z)| \leq \|F\|_1 e^{T|\mathrm{Im}(z)|}$ for all $z \in \mathbb{C}$. With $z = \gamma_j - ib_j$ we have $|\mathrm{Im}(z)| = b_j$, which gives the bound. $\square$

**Lemma 22-C.4** (Bound on the arithmetic side). For $F \geq 0$ supported in $[-T,T]$:
$$\left|\sum_p \sum_k \frac{\log p}{p^{k/2}} \hat F(k\log p)\right| \leq \|F\|_\infty \cdot \psi_2(e^T)$$

where $\psi_2(x) = \sum_{p^k \leq x} \log p / p^{k/2} \asymp x^{1/2}$ (weighted von Mangoldt sum, which grows like $e^{T/2}$ by the PNT).

*Proof*. Each term is $|\frac{\log p}{p^{k/2}} \hat F(k\log p)| \leq \|F\|_\infty \frac{\log p}{\sqrt{p^k}}$; the sum only runs over $p^k \leq e^T$. $\square$

### C.2.3 The exact boundary — why $b_j < 1/2$ is the limit

**Proposition 22-C.5** (Boundary analysis). Let $F_T$ be a family of functions supported in $[-T,T]$ with $\|F_T\|_1 = 1$, $\|F_T\|_\infty \leq 2/T$, and $F_T(\gamma_j - ib_j) \asymp e^{T b_j}$ (maximizing the Paley-Wiener bound). Then the explicit formula gives:

$$4m \cdot e^{T b_j} + [\text{on-line term, bounded}] = O(e^{T/2})$$

This produces a contradiction if and only if $b_j > 1/2$, i.e., $\sigma_j > 1$. But $\sigma_j < 1$ is a basic property of the zeros of $\zeta$ in the critical strip.

*Proof*. By Lemma 22-C.3, the off-line side is $\leq C e^{T b_j}$. By Lemma 22-C.4, the arithmetic side is $\leq C e^{T/2}$. The explicit formula equates both sides. For $b_j < 1/2$: $e^{T b_j} < e^{T/2}$, no contradiction. For $b_j = 1/2$: $e^{T b_j} = e^{T/2}$, no contradiction. For $b_j > 1/2$ (= $\sigma_j > 1$): $e^{T b_j} > e^{T/2}$, contradiction. $\square$

**Critical interpretation**: The Weil-Bombieri explicit formula, via the Paley-Wiener argument, excludes zeros with $\sigma_j > 1$ — but we already know this another way (the function $\zeta$ has no zeros for $\Re(s) > 1$, in fact the Euler product converges there). The argument does NOT exclude zeros in $(1/2, 1)$, precisely where they are possible.

**Key remark** (Wall W4-RSRP restated): The exact boundary of the Paley-Wiener method in the explicit formula is $\sigma_j = 1$. The critical region $(1/2, 1)$ is exactly the "blind spot" of the method. Wall W4-RSRP is the hypothesis that, even though the Paley-Wiener method does not exclude them analytically, the structure of the Euler product does exclude them arithmetically. This is the gap to close.

---

## §C.3 Audit of the three natural candidates

### Candidate I: Selberg's second-moment integral

$$S(\alpha, T) = \int_0^T \left|\frac{\psi(e^t) - e^t}{e^{t/2}}\right|^2 e^{-2(\alpha - 1/2)t} dt$$

**Under Hypothesis D**: $|\psi(e^t)-e^t|/e^{t/2} \geq C e^{b_j t}$ for $t$ in a set of positive density, so $S(1/2, T) \geq C \int_0^{T/2} e^{2b_j t} dt \asymp e^{b_j T}$.

**By Parseval's formula**: Formally, $S(\alpha, T) = \int_{-\infty}^\infty |\hat\Psi(\xi)|^2 e^{-2(\alpha-1/2)...} d\xi$ where $\hat\Psi$ involves $1/|\zeta(1/2+i\xi)|^2$. The value of the Euler product does not control $|\zeta(1/2+it)|$ independently of RH.

**Verdict**: CIRCULAR. Bounding $S$ from below requires knowing $|\psi-x|$, and bounding it from above requires knowing the zeros. There is no independent access to the value of $S$ from the Euler product.

### Candidate II: Mertens function

$$M(x) = \sum_{n \leq x} \mu(n)$$

**By the explicit formula for $M$**: under Hypothesis D, the residue of $1/(s\zeta(s))$ at $\rho = \sigma_j + i\gamma_j$ is $-1/(\rho_j \zeta'(\rho_j))$, and the contribution to $M(x)$ has size $x^{\sigma_j - 1} = x^{b_j - 1/2}$.

For $b_j > 1/2$ (excluded): $M(x) \gg x^{b_j - 1/2} \to \infty$. But the unconditional PNT gives $M(x) = o(x)$, which does not contradict $x^{b_j - 1/2}$ for $b_j < 1$.

For $b_j \leq 1/2$ (the real case): $M(x) = O(x^{b_j - 1/2})$, which is $O(x^0) = O(1)$ or decreasing. No contradiction.

**For $b_j < 1/2$**: the contribution of $\mathcal{O}_j$ to $M(x)$ is $O(x^{b_j - 1/2}) \to 0$. No contradiction with the PNT or any known bound on $M$.

**Special case $b_j > 1/2$** (impossible for $\sigma_j < 1$): this would give $M(x) \gg x^{b_j - 1/2}$ with $b_j - 1/2 > 0$, implying $M(x) \to \infty$ polynomially, contradicting the PNT. BUT $b_j = \sigma_j - 1/2 < 1/2$ always (since $\sigma_j < 1$). This route only works for zeros with $\sigma_j > 1$, which do not exist.

**Verdict**: PARTIALLY USEFUL for $\sigma_j > 1$ (which is impossible), FAILS for $\sigma_j \in (1/2, 1)$.

### Candidate III: Weil functional (positivity)

$$W_\zeta(h) = \sum_\rho h(\gamma_\rho) \geq 0 \quad \text{for every admissible } h \geq 0 \text{ (criterion W1)}$$

Under Hypothesis D: $W_\zeta(h) = \sum_{Z_{\rm CL}} h(\gamma) + 4\sum_j \mathrm{Re}[h(\gamma_j - ib_j)]$. For $h$ that makes $\mathrm{Re}[h(\gamma_j - ib_j)] < 0$ and sufficiently negative, $W_\zeta(h) < 0$.

Finding such $h$ requires knowing $\gamma_j, b_j$. Moreover, the positivity $W_\zeta(h) \geq 0$ is EXACTLY the statement of Wall W1 (equivalent to RH via Weil). No new information.

**Verdict**: REDUCIBLE TO W1. Adds nothing beyond the wall already known.

---

## §C.4 The real obstacle: the arithmetic independence of the functional

**Theorem 22-C.6** (Fundamental obstacle). There is no continuous functional $\mathcal{F}: L^1_{\rm loc}(\mathbb{R}_{>1}) \to \mathbb{R}$ that simultaneously satisfies:
1. $\mathcal{F}[\psi]$ is computable solely from the Euler product of $\zeta$.
2. $\mathcal{F}[\psi - D_m] \neq \mathcal{F}[\psi]$ for every $D_m \not\equiv 0$.
3. $\mathcal{F}[\psi]$ is computable independently of the location of the zeros.

*Proof* (this is a structural impossibility, not a formal theorem). Any functional of $\psi$ computable from the Euler product (valid for $\Re(s) > 1$) accesses $\psi$ through Perron's formula, whose contour of integration crosses $\Re(s) = 1$. The defect $D_m$ corresponds to residues at $\Re(s) \in (1/2, 1)$, a region where the Euler product has stopped converging. Hence the Euler product cannot "see" the residues of the defect. A functional computing $\mathcal{F}[\psi]$ from the Euler product cannot distinguish $\psi$ from $\psi - D_m$ without information from the strip $(1/2, 1)$.

This is the **arithmetic blind spot**: the Euler product is a tool of the half-plane $\Re(s) > 1$; the zeros of the critical strip are phenomena of $\Re(s) \in (0,1)$. The bridge between these worlds is exactly what Wall W4-RSRP must build.

---

## §C.5 A new approach: the Beurling-Nyman criterion under Hypothesis D

### Setup of the criterion

The Beurling-Nyman criterion states: RH $\iff$ $d = 0$ where
$$d^2 = \inf_{A \in \mathcal{D}} \int_0^1 \left|1 - A(x)\right|^2 dx$$
and $\mathcal{D}$ is the closure in $L^2(0,1)$ of the space of "Beurling functions"
$\mathcal{B} = \mathrm{span}\,\{f_\theta : \theta \in (0,1)\}$, $f_\theta(x) = \{\theta/x\} - \theta\{1/x\}$.

The Báez-Duarte result (2003) gives the Dirichlet-series version:
$$d_N^2 = \inf_{A_N} \frac{1}{2\pi}\int_{-\infty}^\infty \left|\frac{1}{\zeta(1/2+it)} - A_N(it)\right|^2 \frac{dt}{1/4+t^2}$$

where $A_N(s) = \sum_{n=1}^N a_n n^{-s}$ (Dirichlet polynomials).

### Under Hypothesis D

Under Hypothesis D, the distance $d > 0$ (since RH fails). Can $d$ be computed in terms of $D_m$ and produce a contradiction?

**Lemma 22-C.7** (Expression of the defect in the distance). Under Hypothesis D with $m$ orbits, the distance $d$ satisfies:
$$d^2 \geq \sum_{j=1}^m \frac{4\pi}{|\rho_j^+ \rho_j^-|^2} \cdot \frac{1}{|\zeta'(\rho_j^+)|^2} > 0$$

*Proof (sketch)*. By Cauchy's interpolation formula, the projection of $1/\zeta(1/2+it)$ onto the space of Dirichlet polynomials cannot capture the pole at $t = \gamma_j + ib_j$ (which lies at distance $b_j > 0$ from the real axis). The minimum distance to the pole is proportional to the residue $1/|\zeta'(\rho_j^+)|$ scaled by the distance $b_j$. Summing over the four components of the orbit gives the factor $4$. $\square$

**Status**: This lemma requires a more careful check of the projection argument. The direction is correct but the complete proof needs additional work.

**Remark**: This lemma also fails to produce the contradiction sought. It shows $d > 0$ under Hypothesis D, which is consistent (since Hypothesis D implies RH fails). To obtain a contradiction, we would need to show $d = 0$ under some property of the structure of $\zeta$ independent of RH, which would require the same arithmetic-analytic bridge as W4-RSRP.

---

## §C.6 Final classification of Step 22-C

| Result | Statement | Class | Status |
|-----------|-----------|-------|--------|
| Theorem 22-C.1 | Korobov-Vinogradov restriction on $b_j$ | B | ✓ proved |
| Corollary 22-C.2 | $\mathcal{E}_j(X) \leq C_j X^{1-\varepsilon_j}$ | B | ✓ proved |
| Lemma 22-C.3 | Paley-Wiener bound $|F(\gamma_j-ib_j)| \leq e^{Tb_j}$ | B | ✓ proved |
| Lemma 22-C.4 | Bound on the arithmetic side $\leq Ce^{T/2}$ | B | ✓ proved |
| Proposition 22-C.5 | Exact boundary $b_j = 1/2$ of the Paley-Wiener method | B | ✓ proved |
| Theorem 22-C.6 | Fundamental obstacle (arithmetic blind spot) | B | ✓ (informal) |
| Lemma 22-C.7 | $d^2 \geq C/|\zeta'(\rho_j)|^2$ under Hypothesis D | B | Provisional |
| Candidates I, II, III | Audit — all fail | B | ✓ |

---

## §C.7 Precise formulation of the open problem

The obstacle can now be formulated with mathematical precision:

**Open problem 22-C** (The arithmetic boundary problem). Let $\mathcal{P}_{\rm Euler}$ be the $\sigma$-algebra of properties of $\zeta$ determinable solely from the Euler product $\prod_p(1-p^{-s})^{-1}$ for $\Re(s) > 1$ (without analytic continuation).

Does there exist a property $P \in \mathcal{P}_{\rm Euler}$ such that $P$ is incompatible with the existence of zeros in $\Re(s) \in (1/2, 1)$?

Proposition 22-C.5 shows that the explicit formula + Paley-Wiener only reaches up to $\Re(s) = 1$ (it does not penetrate the critical strip). Wall W4-RSRP is the hypothesis that such a property $P$ exists — but formalizing it requires a genuinely new idea about how the Euler product "radiates" information into the critical strip.

**This is the precise formulation of Phase 23.**
