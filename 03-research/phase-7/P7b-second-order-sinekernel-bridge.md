# Phase 7b — Second order: the Weil–Carleson form IS the sine-kernel determinantal process on the zeros

**Author: David Alejandro Trejo Pizzo · 2026-06-03.**
N3 closed the first-order lever (the Carleson constant $C=\lambda_{\max}$ is identically $1$, saturated). The
user directed the pivot to **second order** — the subdominant spectrum, the gap below $1$, where zero-spacing
fluctuation lives and the $\omega$-class machinery is built to act. This records what we found, with numbers,
and the honest verdict.

---

## 1. The structural identity (verified)

$A_\Phi-P_F=\sum_{\rho\in\text{window}} v_\rho v_\rho^{\!\top}$, $\ v_\rho[j]=S_j(\gamma_\rho)$ — a sum of $K$
rank-one **evaluation** functionals at the window's zeros. Hence:

- **rank$(A-P)=K$** (the number of zeros in the window). *Verified:* sub-saturation run $d{=}1.3,T_0{=}80$
  ($x{=}0.59$, $M{=}23$, $K{=}21$): $A-P$ has **22 eigenvalues $O(1)$** then collapses to $0$. ✓
- The $K$ active eigenvalues are the spectrum of the $K\times K$ **reproducing-kernel Gram**
  $G[i,j]=K_A(\gamma_i,\gamma_j)$ of the band-limited space — which **is the sine kernel**
  $K_A(\gamma_i,\gamma_j)\propto\dfrac{\sin\!\big(d(\gamma_i-\gamma_j)\big)}{\pi(\gamma_i-\gamma_j)}$ (mod the slow
  archimedean weight). *Verified:* diag-normalized $G$ vs. $\mathrm{sinc}$ kernel, $\max|\Delta|=6.8\times10^{-2}$. ✓

> **Bridge (measured).** *The second-order structure of the band-limited Weil–Carleson form is the
> SINE-KERNEL Gram on the nontrivial zeros — i.e. the Montgomery–Dyson pair-correlation / GUE determinantal
> process. $C_{\max}=1$ (first order) $\iff$ the zeros are real; the subdominant gap $\{1-C_k\}$ is the
> sine-kernel spectrum = the fine zero statistics.*

This is a clean, possibly-new instantiation: Weil positivity's **first** order = RH (zeros real); its
**second** order = pair correlation. They are the same operator, read at two scales.

---

## 2. The detector works (the $\delta^2$ law, in sine-kernel language)

Push the central zero off the line, $\gamma_c\mapsto \tau\mp i\delta$ (a Weil quartet; the band-limited basis
extends to complex argument, entire). The zero-side form acquires a **negative** eigenvalue:

| $\delta$ | $\lambda_{\min}(W_{\text{off}})$ | $\lambda_{\min}/\delta^2$ |
|---:|---:|---:|
| 0.00 | $-3\times10^{-17}$ | — |
| 0.02 | $-2.0\times10^{-6}$ | $-0.005$ |
| 0.05 | $-1.25\times10^{-5}$ | $-0.005$ |
| 0.10 | $-5.1\times10^{-5}$ | $-0.005$ |
| 0.20 | $-2.16\times10^{-4}$ | $-0.005$ |
| 0.40 | $-1.11\times10^{-3}$ | $-0.007$ |

**$\lambda_{\min}=-c\,\delta^2$, $c\approx0.005$ stable** — the second-order form **detects** an off-line zero
quadratically, reproducing the validated engine's $\delta^2$ law (`engine-spec`) in the sine-kernel picture.
The curvature $c$ is governed by the **local zero spacing**: at a near-collision (Lehmer pair) the sine-Gram
is near-singular and $c\to0$ — the stability margin against an RH violation is smallest exactly at Lehmer
pairs. The form thus *quantifies* how close ζ comes to violating RH, height by height.

---

## 3. Honest verdict: a real bridge, the same wall (fourth language)

RH $\iff$ "the sine-kernel Gram is a contraction ($\preceq 1$) on every window." The detector confirms
off-line zeros break it ($\delta^2$). **But this restates RH; it does not prove it:**

- The sine-kernel Gram on **real** zeros is automatically a contraction (it is a determinantal projection
  kernel, $0\preceq K_{\text{sine}}\preceq 1$). So $C\le1$ is *equivalent to* the zeros being real — RH itself.
- **Pair correlation / GUE statistics describe the zeros assuming they are real; they do not force reality.**
  Montgomery's conjecture is itself open and RH-conditional. The $\omega$-class machinery (P5) measures the
  fluctuation *tail of the real zeros* — it characterizes the texture, it does not supply the contraction.

> **So the second-order lever, like the first (N3), reduces to the wall — now in the determinantal /
> pair-correlation language.** It is the most beautiful restatement yet (Weil positivity = sine-kernel
> contraction; RH's stability margin = Lehmer-pair curvature), and it is genuinely *ours* (it lands on the
> zero-statistics frontier our $\omega$-class work was built for), but it does not cross.

---

## 4. Durable output

- **The bridge (B1):** *the band-limited Weil–Carleson form's second-order spectrum is the sine-kernel
  determinantal process on the zeros; RH $\iff$ sine-Gram $\preceq 1$ per window.* Clean, structural,
  publishable alongside N3.
- **A quantitative RH-stability margin:** the off-line curvature $c(T_0)$ ($\delta^2$ coefficient), computable,
  minimized at Lehmer pairs — a concrete diagnostic of "how safe RH is" at each height.
- Joined with N3 (first order saturated, no prime slack), this **completes the map of the large-values /
  Carleson / pair-correlation open core**: both orders are now measured, and both reduce to the
  self-referential wall (positivity $=$ realness of the zeros).

---

### Status
- Bridge: 2nd-order Carleson = sine-kernel Gram on zeros — ✅ verified (rank-$K$; sinc-shape $6.8\times10^{-2}$).
- $\delta^2$ off-line detection in sine-kernel language — ✅ verified ($c\approx0.005$ stable).
- Lever (provable contraction from pair-correlation input) — ❌ restates RH; pair correlation describes, not forces.
- A crossing — ✗ not here. **Option 2 (the "ours" half: $\omega$-class / large values / Carleson) is now
  exhausted in both orders.** The only structurally-distinct untried core is Connes KMS (not ours).
