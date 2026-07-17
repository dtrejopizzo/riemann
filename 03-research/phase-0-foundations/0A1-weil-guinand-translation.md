# Phase 0.A.1 — Q in the Weil–Guinand language (normalization pinned)

**Status:** first rigorous draft. Classical material (confident); the one inference about the
exact engine convention is flagged ⚠ and must be checked against the v8 engine code.

---

## 1. The Riemann–Weil explicit formula

Let $g:\mathbb{R}\to\mathbb{C}$ be even, smooth, with compact support (or Schwartz with enough
decay). Define its transform
$$h(r) = \hat g(r) = \int_{-\infty}^{\infty} g(u)\,e^{iru}\,du .$$
Write the nontrivial zeros of $\zeta$ as $\rho = \tfrac12 + i\gamma$ (so $\gamma\in\mathbb{R}$
under RH; $\gamma\in\mathbb{C}$ in general). The Riemann–Weil explicit formula
(Weil 1952; Guinand 1948; see Iwaniec–Kowalski, *Analytic Number Theory*, §5.5, Thm 5.12) is:

$$\boxed{\;\sum_{\rho} h(\gamma_\rho)
\;=\;\underbrace{h\!\left(\tfrac{i}{2}\right)+h\!\left(-\tfrac{i}{2}\right)}_{\text{POLAR } P(g)}
\;+\;\underbrace{\frac{1}{2\pi}\int_{-\infty}^{\infty} h(r)\,\Omega(r)\,dr}_{\text{ARCHIMEDEAN } A(g)}
\;-\;\underbrace{2\sum_{n=2}^{\infty}\frac{\Lambda(n)}{\sqrt n}\,g(\log n)}_{\text{PRIME } \Pi(g)}\;}$$

where $\Lambda$ is von Mangoldt, and the archimedean density is
$$\Omega(r) \;=\; \operatorname{Re}\,\psi\!\left(\tfrac14+\tfrac{ir}{2}\right) - \log\pi ,
\qquad \psi=\Gamma'/\Gamma .$$
*(Constants/normalization to be pinned against a numeric reference; the structure
ZERO-SIDE = POLAR + ARCH − PRIME is the invariant content.)*

The two ways to read this are the whole point:
- **Zero side** $Z(g):=\sum_\rho h(\gamma_\rho)$ — needs the zeros.
- **Arithmetic side** $\mathcal A(g):=P(g)+A(g)-\Pi(g)$ — needs only primes + Γ-factor, no zeros.
They are **equal as an identity**. The detector exploits the *truncated* versions, where the
equality is only approximate and the off-line zeros break a positivity structure (below).

---

## 2. The Weil functional and the positivity criterion

For a test function $f$, set $\tilde f(x) := \overline{f(-x)}$ and let $\star$ be convolution.
The **Weil functional** is the Hermitian form
$$B(f_1,f_2) \;:=\; \big[\text{either side of the explicit formula applied to } g=f_1\star\tilde f_2\big].$$
With $g=f\star\tilde f$ the zero side becomes
$$Z(f\star\tilde f)=\sum_\rho \big|\hat f(\gamma_\rho)\big|^2 \quad(\text{when }\gamma_\rho\in\mathbb{R}),$$
manifestly $\ge 0$. **Weil's criterion (Weil 1952; Bombieri, *Remarks on Weil's quadratic
functional*):**
$$\boxed{\;\text{RH} \iff B(f,f)\ge 0 \ \text{ for all admissible } f\;}$$
i.e. the Weil functional is positive semidefinite. An off-line zero $\rho_0=\beta_0+i\gamma_0$,
$\beta_0>\tfrac12$, makes $\gamma_0$ complex, so its contribution to $Z$ is **not** of the form
$|\hat f|^2$ and can be made negative by a test function localized near $\gamma_0$ — this is the
exact mechanism the detector measures.

---

## 3. Our Q is the Gram matrix of B in the Hermite–Gauss basis

Take the localized basis $\{\varphi_j\}_{j=0}^{J-1}$ — Hermite functions of width $\sigma$
modulated to center $T_0$ in the spectral variable, e.g.
$$\varphi_j(u) \;\propto\; H_j\!\big(u/\sigma\big)\,e^{-u^2/2\sigma^2}\,e^{\,iT_0 u}.$$
Then our central object is exactly the Gram matrix of the Weil form:
$$\boxed{\,Q_{jk} \;=\; B(\varphi_j,\varphi_k) \;=\; \mathcal A(\varphi_j\star\tilde\varphi_k)
\;=\; Z(\varphi_j\star\tilde\varphi_k).}$$
- $\lambda_{\min}(Q)\ge 0$ for **all** centers/widths/dimensions $\iff$ $B\succeq 0$ $\iff$ RH.
- $\lambda_{\min}(Q)<0$ for **some** localized basis $\Longleftarrow$ an off-line zero near $T_0$.

**⚠ Engine-convention identification (to confirm against v8 code).** The report's
$M_{\text{zeros}}$ and $M_{\text{arith}}$ are the two sides evaluated on the pair $(\varphi_j,\varphi_k)$:
$$ (M_{\text{zeros}})_{jk}=Z(\varphi_j\star\tilde\varphi_k),\qquad
(M_{\text{arith}})_{jk}=P+A-\Pi \ \text{ for } \varphi_j\star\tilde\varphi_k .$$
By the explicit formula $M_{\text{zeros}}=M_{\text{arith}}$ **when complete**, so the *complete*
$Q=M_{\text{zeros}}-M_{\text{arith}}=0$. The detector therefore lives entirely in the
**truncation discrepancy** (finite zero cutoff $H$, finite prime cutoff $X$) — confirming why a
zero-side-only Gram matrix (inputting on-line zeros) is PSD-by-construction and carries no signal,
and why subtracting the arithmetic side is essential. *Confirm: does the v8 engine define Q as the
truncation residual, or as $M_{\text{arith}}$ alone (the genuinely zero-free form)? The latter is
the cleaner detector and the one whose positivity = RH.*

---

## 4. Dictionary entry (what to carry into 0.A.2–0.A.4)

| Our object | Weil–Guinand name |
|---|---|
| Hermite–Gauss test functions $\varphi_j$ | admissible test functions in the Weil class |
| $Q_{jk}$ | Gram matrix of the Weil quadratic functional $B$ |
| $M_{\text{zeros}}$ | zero side $Z$ |
| $M_{\text{arith}}$ | arithmetic side $P+A-\Pi$ |
| "$\lambda_{\min}(Q)\ge0$ everywhere" | Weil positivity $\equiv$ RH |
| "off-line zero $\Rightarrow \lambda_{\min}<0$" | the easy direction of Weil's criterion |
| the missing **(LB)** in PLAN-RH-MAXIMAL | "$B\succeq0$ unconditionally" — the hard direction |

**Verdict (0.A.1):** Q is **not** a new object — it is a *localized, finite-dimensional Gram
matrix of the classical Weil quadratic functional*. That is good: it plugs directly into 70 years
of machinery (Bombieri, Burnol, Connes, de Branges). The novelty is purely in the **localization +
quantitative calibration** (the $\delta^2$ law, the super-polynomial $J$-amplification), not in the
functional itself. Next: 0.A.2 (Connes trace) and 0.A.3 (de Branges) — both need expert check.

**References to pin:** Weil (1952) "Sur les formules explicites…"; Guinand (1948); Bombieri,
"Remarks on Weil's quadratic functional in the theory of prime numbers"; Iwaniec–Kowalski Ch. 5;
Connes (1999) "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function".
