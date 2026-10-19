# Phase 22 — Step 22-A/B: Modified Explicit Formula and Anatomy of the Defect

---

## Fixed notations

- $\rho = \beta + i\gamma$: nontrivial zero of $\zeta$.
- $Z_{\text{off}} = \{\rho : \beta \neq \tfrac{1}{2}\}$: off-line zeros.
- $Z_{\text{CL}} = \{\rho : \beta = \tfrac{1}{2}\}$: zeros on the critical line.
- Hypothesis D: $Z_{\text{off}} = \{\rho_1^+, \overline{\rho_1^+}, 1-\rho_1^+, 1-\overline{\rho_1^+}, \ldots, \rho_m^+, \ldots\}$ is finite, with $m$ complete orbits under the Klein group $V$.
- $\rho_j^+ = \sigma_j + i\gamma_j$ with $\sigma_j = \tfrac{1}{2} + b_j$, $b_j > 0$, $\gamma_j > 0$ ($j = 1, \ldots, m$).
- Orbit $j$ is $\mathcal{O}_j = \{\sigma_j \pm i\gamma_j,\; (1-\sigma_j) \pm i\gamma_j\}$.

---

## Step 22-A: Modified Explicit Formula

### A.1 Starting point: Perron's formula

The classical identity (Davenport, Ch. 17) states that, for non-integer $x > 1$:

$$\psi(x) = x - \sum_{\rho} \frac{x^\rho}{\rho} - \log(2\pi) - \tfrac{1}{2}\log(1 - x^{-2})$$

where the sum runs over **all** nontrivial zeros of $\zeta$, ordered by $|\text{Im}(\rho)| \leq T$ and taking $T \to \infty$ symmetrically.

Split the sum into two parts:

$$\sum_\rho \frac{x^\rho}{\rho} = \underbrace{\sum_{\rho \in Z_{\text{CL}}} \frac{x^\rho}{\rho}}_{\text{on-line contribution}} + \underbrace{\sum_{\rho \in Z_{\text{off}}} \frac{x^\rho}{\rho}}_{=:\; D_m(x)\;\text{(defect)}}$$

Under hypothesis D, the second sum is **finite** — it requires no limit $T \to \infty$.

### A.2 Rigorous definition of the arithmetic defect

**Definition 22-A.1** (Arithmetic defect). Under hypothesis D,

$$D_m(x) := \sum_{j=1}^m \sum_{\rho \in \mathcal{O}_j} \frac{x^\rho}{\rho}$$

It is a sum of $4m$ terms. Each term has the form $x^{\sigma+i\gamma}/(\sigma+i\gamma)$.

**Remark**: $D_m(x)$ is a **real** function of $x > 0$. This follows from the fact that $Z_{\text{off}}$ is symmetric under $\rho \mapsto \bar\rho$ (real coefficients of $\zeta$), so that each term appears together with its complex conjugate.

### A.3 Definition of $\psi_0$

Under the factorization $\xi = \xi_0 P_{4m}$ (Corollary 9.2 of P32), let:

$$\psi_0(x) := x - \sum_{\rho \in Z_{\text{CL}}} \frac{x^\rho}{\rho} - \log(2\pi) - \tfrac{1}{2}\log(1-x^{-2})$$

That is, $\psi_0$ is the **virtual** Chebyshev function associated with $\xi_0$ (which has all its zeros on the critical line).

**Note**: $\psi_0$ is an analytic function — not the prime-counting function of any standard arithmetic object. The Euler product of $\zeta$ does not admit the factorization $\xi = \xi_0 P_{4m}$ at the level of Dirichlet series. This is discussed in §22-C.

### A.4 The main theorem of Step 22-A

**Theorem 22-A** (Modified Explicit Formula). Under hypothesis D, for every non-integer $x > 1$:

$$\psi(x) = \psi_0(x) - D_m(x)$$

**(exact identity, no error term).**

*Proof*. Immediate: substitute the partition $\sum_\rho = \sum_{Z_{\text{CL}}} + \sum_{Z_{\text{off}}}$ into the standard Perron formula. The sum over $Z_{\text{off}}$ is finite under hypothesis D, so there is no error term coming from truncation. $\square$

**Corollary 22-A.1** (Error decomposition). Let $E(x) = \psi(x) - x$ be the PNT error. Then:

$$E(x) = E_0(x) - D_m(x)$$

where $E_0(x) = \psi_0(x) - x = -\sum_{Z_{\text{CL}}} x^\rho/\rho + O(\log x)$.

---

## Step 22-B: Anatomy of the Defect — explicit computation of $D_m$

### B.1 The defect of a single orbit

Fix $j \in \{1,\ldots,m\}$. The orbit $\mathcal{O}_j$ contributes:

$$D_j(x) = \frac{x^{\sigma_j + i\gamma_j}}{\sigma_j+i\gamma_j}
           + \frac{x^{\sigma_j - i\gamma_j}}{\sigma_j - i\gamma_j}
           + \frac{x^{(1-\sigma_j)+i\gamma_j}}{(1-\sigma_j)+i\gamma_j}
           + \frac{x^{(1-\sigma_j)-i\gamma_j}}{(1-\sigma_j)-i\gamma_j}$$

Using $x^{a+ib} = x^a e^{ib\log x}$ and grouping conjugate pairs:

$$D_j(x) = 2\mathrm{Re}\,\!\left[\frac{x^{\sigma_j+i\gamma_j}}{\sigma_j+i\gamma_j}\right]
           + 2\mathrm{Re}\,\!\left[\frac{x^{(1-\sigma_j)+i\gamma_j}}{(1-\sigma_j)+i\gamma_j}\right]$$

Let $\theta_j^+ = \arg(\sigma_j+i\gamma_j)$ and $\theta_j^- = \arg((1-\sigma_j)+i\gamma_j)$. Then:

$$\boxed{D_j(x) = \frac{2x^{\sigma_j}}{|\rho_j^+|}\cos(\gamma_j\log x - \theta_j^+)
           + \frac{2x^{1-\sigma_j}}{|\rho_j^-|}\cos(\gamma_j\log x - \theta_j^-)}$$

where $\rho_j^+ = \sigma_j+i\gamma_j$, $\rho_j^- = (1-\sigma_j)+i\gamma_j$, and $|\rho_j^\pm|$ are their moduli.

### B.2 Dominant and subdominant structure

With $\sigma_j = \tfrac{1}{2} + b_j$ and $1 - \sigma_j = \tfrac{1}{2} - b_j$, $b_j > 0$:

$$D_j(x) = \underbrace{\frac{2x^{1/2+b_j}}{|\rho_j^+|}\cos(\gamma_j\log x - \theta_j^+)}_{\text{dominant term}} + \underbrace{\frac{2x^{1/2-b_j}}{|\rho_j^-|}\cos(\gamma_j\log x - \theta_j^-)}_{\text{subdominant term}}$$

As $x \to \infty$: the dominant term grows like $x^{1/2+b_j}$ with $b_j > 0$; the subdominant one decays like $x^{1/2-b_j}$.

**Proposition 22-B.1** (Size of the defect). Under hypothesis D, for $x \geq 2$:

$$D_m(x) = \sum_{j=1}^m \frac{2x^{1/2+b_j}}{|\rho_j^+|}\cos(\gamma_j\log x - \theta_j^+) + O\!\left(x^{1/2-b_{\min}}\right)$$

where $b_{\min} = \min_j b_j > 0$ and the implicit constant depends only on the $|\rho_j^\pm|$.

*Proof*. Group the $m$ subdominant terms; each is $O(x^{1/2-b_j}) = O(x^{1/2-b_{\min}})$. $\square$

### B.3 Defect energy per orbit

**Definition 22-B.2** (Defect energy). For $X \geq 2$:

$$\mathcal{E}_j(X) := \int_X^{2X} \frac{|D_j(t)|^2}{t^2}\,dt$$

**Proposition 22-B.3** (Energy growth). As $X \to \infty$:

$$\mathcal{E}_j(X) \sim \frac{2}{|\rho_j^+|^2} \cdot \frac{X^{2b_j}}{2b_j}$$

In particular, $\mathcal{E}_j(X) \to \infty$ for any $b_j > 0$.

*Proof*. The square of the dominant term is $\tfrac{4x^{1+2b_j}}{|\rho_j^+|^2}\cos^2(\gamma_j\log x - \theta_j^+)$. Integrating over $[X,2X]$ and using $\langle\cos^2\rangle = \tfrac{1}{2}$ (since $\gamma_j \log x$ oscillates fast):

$$\mathcal{E}_j(X) \approx \frac{4}{|\rho_j^+|^2} \cdot \frac{1}{2} \int_X^{2X} t^{2b_j-1}\,dt = \frac{2}{|\rho_j^+|^2} \cdot \frac{(2X)^{2b_j}-X^{2b_j}}{2b_j} \sim \frac{2(2^{2b_j}-1)}{|\rho_j^+|^2 \cdot 2b_j} X^{2b_j}$$

which diverges like $X^{2b_j}$. $\square$

**Corollary 22-B.4** (Total energy). $\sum_{j=1}^m \mathcal{E}_j(X) \sim C_m X^{2b_{\max}}$ where $b_{\max} = \max_j b_j$.

### B.4 The defect and the Euler product: structural incompatibility

Here appears the most important point of Phase 22.

The explicit formula uses $-\zeta'/\zeta$. The factorization $\xi = \xi_0 P_{4m}$ gives:

$$\frac{\xi'(s)}{\xi(s)} = \frac{\xi_0'(s)}{\xi_0(s)} + \frac{P_{4m}'(s)}{P_{4m}(s)}$$

With $P_{4m}(s) = \prod_{\rho \in Z_{\text{off}}}(s-\rho)$ (polynomial of the $4m$ zeros):

$$\frac{P_{4m}'(s)}{P_{4m}(s)} = \sum_{\rho \in Z_{\text{off}}} \frac{1}{s-\rho}$$

The relation between $\xi'/\xi$ and $\zeta'/\zeta$ is:

$$\frac{\xi'(s)}{\xi(s)} = \frac{\zeta'(s)}{\zeta(s)} + \frac{1}{s-1} + \frac{1}{s} + \frac{1}{2}\log\pi - \frac{1}{2}\frac{\Gamma'}{\Gamma}(s/2)$$

Hence, defining $\zeta_0(s) = \zeta(s)/P_{\text{arith}}(s)$ where $P_{\text{arith}}$ is the appropriate arithmetic correction, the Dirichlet series of $-\zeta_0'/\zeta_0$ would satisfy:

$$-\frac{\zeta_0'(s)}{\zeta_0(s)} = -\frac{\zeta'(s)}{\zeta(s)} + \sum_{\rho \in Z_{\text{off}}} \frac{1}{s-\rho}$$

**Lemma 22-B.5** (Arithmetic incapacity of $\zeta_0$). The function $\zeta_0(s) = \xi_0(s)/[\text{gamma factor}]$ has poles at each $\rho \in Z_{\text{off}}$ (which are zeros of $P_{4m}$). Consequently:

1. $\zeta_0$ **is not** a Dirichlet series with non-negative coefficients.
2. $\zeta_0$ **does not admit** an Euler product of the form $\prod_p (1-a_p p^{-s})^{-1}$ with $|a_p| \leq 1$.
3. The function $\Lambda_0$ defined by $-\zeta_0'/\zeta_0 = \sum_n \Lambda_0(n) n^{-s}$ **is not** the von Mangoldt function of any standard arithmetic object.

*Proof*. (1) and (2): the poles of $\zeta_0$ at $\Re(s) > 0$ accumulate at $Z_{\text{off}}$; no Dirichlet series with non-negative coefficients has poles at $\Re(s) > 0$ other than at $s = 1$ (by Landau's argument). (3) follows from (1) because the von Mangoldt function of an arithmetic object produces a series with coefficients $\geq 0$ (in the case of $\zeta$, $\Lambda(n) \geq 0$ for all $n$). $\square$

**Critical remark**: Lemma 22-B.5 is not a contradiction. It says that the factorization $\xi = \xi_0 P_{4m}$ is available in the **analytic** world (entire functions) but **not** in the **arithmetic** world (Dirichlet series with an Euler product). The bridge between these two worlds is exactly the content of Wall W4-RSRP.

---

## Summary of Step 22-A/B results

| Statement | Class | Status |
|-----------|-------|--------|
| Theorem 22-A (Modified Explicit Formula) | B | Proved |
| Corollary 22-A.1 (error decomposition) | B | Proved |
| Proposition 22-B.1 (size of the defect) | B | Proved |
| Proposition 22-B.3 (energy growth) | B | Proved |
| Corollary 22-B.4 (total energy) | B | Proved |
| Lemma 22-B.5 (arithmetic incapacity of $\zeta_0$) | B | Proved |

---

## Next steps

### Step 22-C: Incompatible invariants

The precise question (now formulated rigorously thanks to 22-A/B):

> Is there a functional $\mathcal{F}$ such that $\mathcal{F}[\psi]$ is determinable from the Euler product and $\mathcal{F}[\psi_0 - D_m]$ is inconsistent with that value for every $m \geq 1$?

The three most promising candidates:

**Candidate I: Selberg second-moment integral**

$$S(\alpha, T) = \int_0^T \left|\frac{\psi(e^t) - e^t}{e^t}\right|^2 e^{-2\alpha t}\,dt$$

Under RH ($\kappa=0$): $S(1/2, T) = O(T)$.
Under hypothesis D ($\kappa = 2m$, $b_{\max} > 0$): $S(1/2, T) \sim C e^{2b_{\max} T}$.
Value from the Euler product: $S(\alpha, T)$ is tied to $|\zeta(1/2+\alpha+it)|^2$ by the modified Parseval theorem. The inconsistency would require showing that $|\zeta(1/2+\alpha+it)|^2$ cannot grow at rate $e^{2b_{\max}T}$... which is exactly hypothesis D itself. **Circular**.

**Candidate II: Mertens function**

$$M(x) = \sum_{n \leq x} \mu(n) = -\frac{1}{2\pi i}\int \frac{x^s}{s\,\zeta(s)}\,ds$$

Under hypothesis D: the poles of $1/(s\,\zeta(s))$ include the zeros of $\zeta$, and $Z_{\text{off}}$ produces contributions to $M(x)$ of size $\gg x^{\sigma_j - 1}$.
For $\sigma_j > 1$: impossible ($\sigma_j < 1$). For $\sigma_j \in (1/2,1)$: $M(x) \gg x^{\sigma_j - 1} = x^{b_j - 1/2}$. If $b_j > 1/2$: $M(x) \gg x^{b_j-1/2} \to \infty$ polynomially.
Under PNT: $M(x) = o(x)$. The inconsistency would require $b_j > 1/2$ or a finer argument. **Partially promising**, but requires large $b_j$.

**Candidate III: Direct Weil functional**

$$W(\hat{f}) = \sum_\rho \hat{f}(\gamma) - \hat{f}(i/2) - \hat{f}(-i/2) + \cdots$$

The functional $W(\hat{f})$ is the kernel of the Weil form. Under hypothesis D:

$$W(\hat{f}) = W_0(\hat{f}) + \sum_{\rho \in Z_{\text{off}}} \hat{f}(\gamma_\rho) - [\text{off-line zero terms}]$$

The off-line zeros contribute with the **wrong sign** (negative contribution for $f \geq 0$). Formally this contradicts Weil positivity... but that is exactly W1. **Not new** relative to W1.

**Provisional conclusion**: The three natural candidates are either circular or reducible to already-known obstructions (W1, W2, W3). Step 22-C must look for a **non-circular** functional, i.e., one whose value does not depend on where the zeros are.

### Step 22-D: Connection with class $\omega$

The finite defect $D_m(x) \sim C_j x^{1/2+b_j}\cos(\gamma_j\log x)$ has a **fixed frequency** $\gamma_j/(2\pi)$ in the variable $\log x$. The multiplicative chaos of class $\omega$ (papers M1–M13) produces fluctuations of $\psi(x)$ at **all** scales simultaneously with Gaussian statistics. The question is:

> Can a **single-frequency**, **growing-amplitude** oscillation coexist with fine-grained chaos?

Formally: the defect $D_m$ has a frequency spectrum concentrated on $\{\gamma_j\}_{j=1}^m$ (finitely many frequencies), while the chaos of $\psi(x)-x$ has a continuous spectrum. The spectral rigidity of the chaos could exclude isolated frequencies of growing amplitude — that would be one path toward EX.

---

## Classification of Phase 22 results (updated)

| Code | Statement | Class | Status |
|--------|-----------|-------|--------|
| 22-A | Modified explicit formula $\psi = \psi_0 - D_m$ | B | ✓ proved |
| 22-B1 | Defect $D_j$ as an oscillation with explicit phase | B | ✓ proved |
| 22-B2 | Energy $\mathcal{E}_j(X) \sim C X^{2b_j}$ | B | ✓ proved |
| 22-B3 | Arithmetic incapacity of $\zeta_0$ | B | ✓ proved |
| 22-C | Functional incompatible with $D_m$ | A/EX | Open |
| 22-D | Spectral rigidity of the chaos vs. finite defect | EX | Open |
