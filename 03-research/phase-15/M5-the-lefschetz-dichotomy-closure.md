# Phase 15 · M5 — The Lefschetz dichotomy: why the hard-Lefschetz route to RH for $\zeta$ does not close

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
M4 constructed, explicitly and verified, the full archimedean–modular scaffold: a positive bulk metric
$g_\infty=|\Psi|$ (M4.1), a hard-Lefschetz $\mathfrak{sl}_2$ on the continuum with raising operator $L=T_c\notin
W^*(\mathcal T)$ (M4.2, the first explicit clearing of the independence filter), and the exact transport identity
$Q=A_\infty-P$ (M4.3). M4.3 showed the discrete positivity $Q\ge0$ is the near-cancellation residual of
$A_\infty-P$ (CAP), not the transported upstairs positivity. M5 settles the one remaining handle — the **full**
Hodge–Riemann form across $\mathfrak{sl}_2$-degrees — and in doing so proves a clean structural dichotomy that closes
the direction honestly. No crossing.

---

## 1. The remaining handle and its two parts

M4.3 tested only the degree-$0$ metric $A_\infty(f,f)$. The Lefschetz machinery offers one more object: the **full
Hodge–Riemann form**, the alternating sum over the primitive $\mathfrak{sl}_2$-degrees,
$\mathrm{HR}(f)=\sum_k(-1)^k\,g_\infty(P_kf,\Lambda^kP_kf)$. The question: is the Weil form $Q$ the image of
$\mathrm{HR}$ (so the degree grading reorganizes the prime term into a manifest positivity), or does $\mathrm{HR}$
also miss $Q$? M5 answers in two parts.

## 2. Part 1 — the continuum $\mathfrak{sl}_2$ carries **no** Hodge–Riemann form

\begin{proposition}[Principal series, no lowest weight]\label{prop:ps}
The $\mathfrak{sl}_2$ of M4.2 ($L=T_c$, $H=\frac2c\mathcal T_{\mathrm{cont}}$, $\Lambda=T_{-c}\,m$,
$m(r)=\tfrac{r(c-r)}{c^2}$) is a **principal-series** representation: $\operatorname{spec}(H)=\frac2c\mathbb R=\mathbb
R$ is unbounded below, and the lowest-weight equation $\Lambda v=0$ forces $m(r)v(r)=0$, i.e.\ $v$ supported on the
measure-zero set $\{0,c\}$ — **no normalizable lowest-weight vector exists.** Hence there is no primitive
decomposition $V=\bigoplus_k L^k(\ker\Lambda)$, and **no Hodge–Riemann bilinear form is defined on this
representation.**
\end{proposition}

This is not an accident of the construction: **Hodge–Riemann positivity is a property of lowest-weight (equivalently
finite-dimensional / discrete-series, integer-graded) $\mathfrak{sl}_2$-representations only.** The HR signs come
from the finite Lefschetz string $\mathrm{Prim}^k\to L\,\mathrm{Prim}^k\to\cdots\to L^{n-k}\mathrm{Prim}^k$; a
principal series has no such finite strings. The "full HR form" the handle hoped to test **does not exist** here.

## 3. Part 2 — the only positive form the machinery yields is not $Q$

Even granting the most charitable concrete proxy — using the sign grading $S=\operatorname{sgn}(\mathcal
T_{\mathrm{cont}}^2-r_0^2)$ (M4.1b) to absorb the indefiniteness — the manifestly positive form one builds is
$g_\infty(f,f)=\frac1{2\pi}\int|\widehat f(r)|^2|\Psi(r)|\,dr\ge0$. Computed on the M4.3 primitives:

| $\sigma$ | $A_\infty$ (signed) | $g_\infty=\int|\widehat f|^2|\Psi|$ | $Q$ (Weil) | $g_\infty=Q$? |
|---|---|---|---|---|
| $2$ | $-6.2225$ | $6.2235$ | $1.6\times10^{-17}$ | no — by $4\times10^{17}$ |
| $3$ | $-21.677$ | $23.134$ | $1.83\times10^{-5}$ | no — by $1.3\times10^{6}$ |
| $4$ | $-24.239$ | $62.878$ | $0.3022$ | no — by $208$ |

$g_\infty\ge0$ always, but it is **orders of magnitude larger than the Weil form $Q$** (factors $10^2$–$10^{18}$).
The degree/sign reorganization produces $g_\infty$, **not** $Q$. The Weil form remains the signed residual
$Q=A_\infty-P$; the grading does not convert it into a positive form. *(Certificate: `m5_full_HR.py`.)*

## 4. The dichotomy (the precise reason the route does not close)

M4.2a and M5 are the two horns of a single structural fact about $\zeta$:

\[
\boxed{
\begin{array}{ll}
\textbf{Discrete horn (M4.2a).} & \text{On the zeros }\{\gamma_\rho\}\text{, LI forbids any Tate-twist raising}\\
 & \text{operator: the spectrum is not translation-invariant. \emph{No }}\mathfrak{sl}_2\text{ at all.}\\[4pt]
\textbf{Continuum horn (M5).} & \text{On }L^2(\mathbb R,dr)\text{ a raising operator exists }(T_c)\text{, but the}\\
 & \mathfrak{sl}_2\text{ is principal series: \emph{no lowest weight, no Hodge--Riemann}.}
\end{array}}
\]

Hard-Lefschetz Hodge–Riemann lives **only** on integer-graded, lowest-weight $\mathfrak{sl}_2$-representations. The
Linear Independence of the $\zeta$-zeros (P15) forces a strict dichotomy:
- keep the arithmetic spectrum (the zeros) — there is **no grading at all** (no raising operator);
- gain a grading by passing to the continuum — the grading is **continuous** (principal series), and carries **no
  positivity**.

In the function-field case the Frobenius eigenvalues are Weil numbers of a **single integer weight** ($H^1$ is pure
of weight $1$); the Lefschetz $\mathfrak{sl}_2$ is lowest-weight and Hodge–Riemann applies. For $\zeta$, LI is
exactly the statement that no such integer weight structure exists on the zeros — and M5 shows that buying a grading
on the continuum costs the lowest-weight property that Hodge–Riemann needs. **The two requirements (arithmetic
spectrum + lowest-weight grading) are incompatible under LI.** That is the sharp, structural reason the
hard-Lefschetz route to RH for $\zeta$ does not close.

## 5. Status — honest terminus of the archimedean–modular direction

- **Built and verified (real gains):** the positive bulk metric $g_\infty=|\Psi|$ (M4.1, $\Psi$ = the smooth
  zero-density, positive on the spectrum); the **first explicit operator clearing the independence filter** — the
  continuum hard-Lefschetz $\mathfrak{sl}_2$ with $L=T_c\notin W^*(\mathcal T)$ (M4.2); the exact transport identity
  $Q=A_\infty-P$ (M4.3).
- **The dichotomy (new, clean):** no hard-Lefschetz Hodge–Riemann mechanism can simultaneously (i) act on the
  arithmetic zero-spectrum and (ii) be lowest-weight/integer-graded — LI forbids the overlap (M4.2a + M5). This
  sharpens P15 from "no finite model" to a precise representation-theoretic obstruction: **arithmetic spectrum and
  HR-carrying grading are LI-incompatible.**
- **No crossing.** The Weil positivity $Q\ge0$ remains the near-cancellation residual $A_\infty-P$ (CAP); the
  Lefschetz machinery yields the positive form $g_\infty\ne Q$, not $Q$ itself. The archimedean–modular direction is
  closed: it produced the explicit independent $\mathfrak{sl}_2$ and the sharp two-horned obstruction, and it does
  not manufacture a proof.

> The Anatomy–Kreĭn–Hodge program (M1–M5) has now built the entire Weil scaffold for $\operatorname{Spec}\mathbb Z$
> — pairing, trace identity, effectivity, ample cone, the zero-carrying cohomology, the Frobenius flow, an explicit
> independent hard-Lefschetz $\mathfrak{sl}_2$ on the continuum — and reduced RH to a single, now precisely
> characterized, structural incompatibility: **HR positivity needs a lowest-weight grading that LI forbids on the
> arithmetic spectrum.** This is the sharpest statement of the obstruction the program has reached, and it is a
> theorem about *why* RH resists the Lefschetz route, not a crossing of it.
