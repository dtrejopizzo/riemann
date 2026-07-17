# Phase 2 — The anatomy profile vs the local Euler factor: Slepian, the $R_p\leftrightarrow a_p$ factorization, and a stability theorem

**Route B / M5, Phase 2 (analytic, no engine).** Author: David Alejandro Trejo Pizzo · 2026-06-03.
Follows T3 (`T3-anatomy.md`). Steps A/B/C per the advisor. **The question Phase 2 must answer honestly:**
*does the anatomy profile $\{R_p\}$ carry new information, or is it merely the coefficients $\{a_p\}$
re-packaged?*

> **Verdict, up front (honest).** To leading order **the anatomy profile factorizes as $R_p\approx a_p\,W(\log p)$**
> with $W$ a *universal window weight* — so the leading term is the coefficient $a_p$ re-weighted, i.e.
> **partly the reformulation the advisor feared.** But three things are genuinely *not* just $\{a_p\}$ and are
> the real content: **(i)** the higher-frequency corrections probe the full **local factor $L_p$** (Satake
> $\alpha_p,\beta_p$, prime powers), not only $a_p$; **(ii)** the window weight $W=W[u_0]$ is **self-consistent**
> (it depends on the global minimizer); and — decisively — **(iii) the *factorizability itself* reflects the
> Euler product**: for an Euler-product $L$ the profile factors ($R_p=$ windowed local factor); for the
> RH-violator $L_{\mathrm{DH}}$ (no Euler product) it **does not** — *one direction only*; the converse
> ("factorization $\Rightarrow$ Euler") is a **conjecture**, not proved. So the surviving invariant is
> sharpened to *the windowed local-factor profile and its multiplicative structure* — tied to the Euler
> product, the conjectured RH discriminant.

---

## A. The Slepian reformulation (removing the Hermite envelope ambiguity)

**The anatomy identity is subspace-determined, not basis-dependent.** For a *fixed* $J$-dimensional
localization subspace $\mathcal V$, the operator $Q=Q_{\mathrm{arith}}^{(X)}|_{\mathcal V}$, its minimizer
$u_0\in\mathcal V$, and hence $\widehat{u_0}(x)$ and $R_p(u_0)$ are intrinsic to $\mathcal V$ — independent of
which orthonormal basis of $\mathcal V$ one writes them in. The "Hermite vs Slepian" choice is therefore a
choice of **subspace $\mathcal V$**, not a change of basis.

- **Hermite-Gauss $\mathcal V_{\mathrm H}$:** soft support; $\widehat{u_0}$ carries the turning-point envelope
  $|x|\lesssim\sqrt{2J-1}/\sigma$ (T3.4). The apparent band $\log p\approx3.3$–$3.7$ rides this envelope.
- **Slepian $\mathcal V_{\mathrm S}$:** the prolate spheroidal functions $\{\psi_n^{(c)}\}$ of time–band
  product $c=\sigma W$ are the *maximally concentrated* functions on the joint window (frequency $[T_0-W,T_0+W]$,
  log-frequency $|x|\le T$). Their concentration eigenvalues $\lambda_n\in(0,1)$ are $\approx1$ for
  $n\lesssim 2c/\pi$ then drop sharply. On $\mathcal V_{\mathrm S}=\mathrm{span}\{\psi_n:\lambda_n\approx1\}$
  the envelope is a **near-flat box** $|x|\le T$, **not** a soft turning point.

> **A-criterion (the band test, made precise).** Read the anatomy density $|\widehat{u_0}(\log p)|^2$ on
> $\mathcal V_{\mathrm S}$ with the flat-box envelope divided out. **If the $\log p\approx3.3$–$3.7$
> concentration persists relative to the flat envelope, it is operator/arithmetic structure; if it flattens,
> it was the Hermite turning point.** This conceptual experiment is worth more than raising $X$: it decides
> whether the band is real with *no* new engine, only the change of subspace.

**Deliverable A.** The Slepian-anatomy is $R_p^{\mathrm S}(u_0^{\mathrm S})=\sum_k\frac{\Lambda_L(p^k)}{\sqrt{p^k}}|\widehat{u_0^{\mathrm S}}(k\log p)|^2$
with $u_0^{\mathrm S}$ the minimizer over $\mathcal V_{\mathrm S}$; all of T3.1–T3.3 hold verbatim, now with a
flat envelope so that *concentration within the window is meaningful*.

---

## B. The $R_p\leftrightarrow$ local-factor factorization (Step B)

Let $L$ have local factor $L_p(s)^{-1}=\prod_{j}(1-\alpha_{p,j}p^{-s})$ (degree $r$ Satake parameters
$\alpha_{p,j}$), so that
$$
-\frac{L'}{L}(s)=\sum_{p,k}\Big(\textstyle\sum_j \alpha_{p,j}^k\Big)\frac{\log p}{p^{ks}},\qquad
\Lambda_L(p^k)=\Big(\sum_j\alpha_{p,j}^k\Big)\log p =: a_{p^k}\log p .
$$
For $\mathrm{GL}(1)$/$\mathrm{GL}(2)$: $a_p=\sum_j\alpha_{p,j}$ is the normalized coefficient; for $\mathrm{GL}(2)$
with $\alpha_p\beta_p=1$, $a_{p^2}=a_p^2-2$, etc. (Hecke recursion). Then, with $x=\log p$ and
$\sqrt{p^k}=e^{kx/2}$:

> **Proposition B1 (anatomy = windowed local factor).**
> $$
> R_p(u_0)=\sum_{k\ge1} a_{p^k}\,\underbrace{x\,e^{-kx/2}\,|\widehat{u_0}(kx)|^2}_{=:W_k(x)}
> \ \overset{\text{lead}}{=}\ a_p\,W_1(\log p)\ +\ \sum_{k\ge2}a_{p^k}\,W_k(\log p),
> $$
> where $W_k(x)=x\,e^{-kx/2}|\widehat{u_0}(kx)|^2$ are **universal window weights** (independent of $L$,
> determined by $u_0$). The leading ($k=1$) term is $a_p\,W_1(\log p)$; the $k\ge2$ corrections carry the
> **prime powers** $a_{p^2},a_{p^3},\dots$ (the Satake structure), and are $O(e^{-kx/2})=O(p^{-k/2})$ smaller
> *and* edge-suppressed (they evaluate $\widehat{u_0}$ at $kx$, near/beyond the window edge).

**Proof.** Substitute $\Lambda_L(p^k)=a_{p^k}\log p$ into $R_p(u_0)=\sum_k\frac{\Lambda_L(p^k)}{\sqrt{p^k}}|\widehat{u_0}(k\log p)|^2$
and collect $W_k$. $\square$

**Reading — the honest answer to the critical question.**
- **Leading order is $a_p$ re-weighted.** $R_p\approx a_p W_1(\log p)$: the first-order anatomy *is* the
  coefficient $a_p$ times a window factor. For $\zeta$ ($a_p\equiv1$) the leading anatomy is **pure window**
  (no arithmetic modulation); for $L(\chi)$ it is $a_p=\chi(p)$ modulated; for automorphic $L$, $a_p=$ Satake
  trace. So at leading order the profile is *not new* — it is the coefficients through the window. The advisor's
  deflation risk is **real and confirmed at leading order.**
- **The genuine new content is beyond leading order:**
  1. **(local factor, not just $a_p$)** the $k\ge2$ corrections inject $a_{p^2}=a_p^2-2,\dots$ — the *full
     local factor* $L_p$, i.e. the individual Satake parameters, not only their sum $a_p$.
  2. **(self-consistency)** $W_k=W_k[u_0]$ and $u_0=u_0[\{a_p\}_{\text{all}}]$: the window weights are a
     **nonlinear functional of the entire coefficient set**, so $R_p$ couples $a_p$ to *all* other primes
     through $u_0$. This is not present in the bare $\{a_p\}$.
  3. **(multiplicativity — ONE direction only; the converse is a conjecture, not proved)** Prop. B1 *assumed
     an Euler product*; what is **proved** is the single implication
     $$\text{Euler product }(\Lambda_L(p^k)=a_{p^k}\log p)\ \Longrightarrow\ R_p=\textstyle\sum_k a_{p^k}W_k\ \ (\text{profile factors}).$$
     For $\zeta$/Dirichlet/automorphic $L$ the profile factors; $L_{\mathrm{DH}}$ has **no** Euler product
     ($\tfrac{1-i}2 L(\chi)+\tfrac{1+i}2 L(\bar\chi)$, $-L_{\mathrm{DH}}'/L_{\mathrm{DH}}$ non-multiplicative),
     so Prop. B1 does not apply to it. **⚠️ Correction (advisor, fair):** this is only one direction. The
     **converse** — *observable factorization of $\{R_p\}\Rightarrow$ Euler product* — which is what a genuine
     *discriminant* needs, is **NOT proved**. It is recorded as a **conjecture (T4-level)**:
     $$\textbf{Conjecture B2.}\quad\text{a robustly factorizing anatomy profile detects/forces the Euler product.}$$
     So Phase 2 establishes "Euler $\Rightarrow$ factorization", not "factorization $\Rightarrow$ Euler".

> **B-conclusion.** The anatomy profile is a **windowed functional of the local factor $L_p$** — a *function
> of the arithmetic*, not more than it, so it cannot manufacture information. Its value is **diagnostic, not
> generative**: (i) it linearizes to $a_p$ (tautological part), (ii) its corrections expose the full local
> factor (Satake), and (iii) **its factorizability encodes the Euler product**, which is the candidate RH
> discriminant. The program's invariant is hereby sharpened from "the profile $\{R_p\}$" to **"the
> multiplicative structure of the windowed local-factor profile"** — the part that is *not* reducible to a
> single $a_p$ and that $L_{\mathrm{DH}}$ breaks.

---

## C. The stability theorem (Step C)

> **Theorem C (anatomy stability under shared local data).** Let $L,L'$ have identical local data up to $P$:
> $\Lambda_L(n)=\Lambda_{L'}(n)$ for all $n\le P$. Then:
> 1. **(exact, truncated)** the truncated profiles coincide: $R_p^{(X)}(L)=R_p^{(X)}(L')$ for all $p$ whenever
>    $X\le P$ — because $Q_{\mathrm{arith}}^{(X)}$ (hence $u_0$, hence every $R_p$) depends only on
>    $\{\Lambda_L(n)\}_{n\le X}$ (T1 locality).
> 2. **(untruncated)** for the full ($X=\infty$) profiles,
>    $$
>    \big\|\mathcal R(L)-\mathcal R(L')\big\|\ \le\ C\,e^{-\alpha(\log P)^2},\qquad \alpha\approx\sigma^2/8,
>    $$
>    with $C=C(\sigma,J,T_0)$.

**Proof.** (1) is immediate from the locality of $Q_{\mathrm{arith}}^{(X)}$ (T1(b)). (2): by P7 Theorem II,
$\|Q_{\mathrm{arith}}^{(\infty)}(L)-Q_{\mathrm{arith}}^{(P)}(L)\|\le \tfrac12 A e^{-\alpha(\log P)^2}$ and same
for $L'$; since $Q^{(P)}(L)=Q^{(P)}(L')$ (shared local data), $\|Q^{(\infty)}(L)-Q^{(\infty)}(L')\|\le A e^{-\alpha(\log P)^2}$.
If $\lambda_{\min}$ is simple with gap $g$, eigenvector perturbation (Davis–Kahan) gives
$\|u_0(L)-u_0(L')\|\le \tfrac{1}{g}A e^{-\alpha(\log P)^2}$, and each $R_p$ is Lipschitz in $u_0$ on the unit
sphere; summing the (window-weighted, summable) $R_p$ contributions gives the stated bound. $\square$

**Reading.** Theorem C is the **quantitative form of T1**: the anatomy profile is not just *logically* a local
functional, it is **exponentially stable** in the local arithmetic. Two L-functions agreeing on small primes
have near-identical anatomy — the profile is a *smooth, local, arithmetic* fingerprint, robust to the
(unknowable) tail. This is exactly the property a useful classification invariant must have, and it is now a
theorem.

---

## D. What Phase 2 settled, and the sharpened forward question

**Settled (analytic, this file).**
- **A** — the anatomy is subspace-intrinsic; the **Slepian subspace** gives a flat envelope, turning the
  "band" into a clean, decidable test (no engine needed).
- **B** — $R_p=\sum_k a_{p^k}W_k(\log p)$: a **windowed functional of the local factor**; leading order $=a_p$
  (the tautological part, honestly conceded); new content $=$ Satake corrections, self-consistent window, and
  **factorizability $\equiv$ Euler product** (the $\zeta$-vs-$L_{\mathrm{DH}}$ discriminant).
- **C** — the profile is **exponentially stable** in the shared local data (quantitative T1).

**The sharpened forward question (T4 seed).** The invariant is now precisely the **multiplicative/windowed
structure** of $\{R_p\}$, not the raw profile or the retired scalar. The decisive, well-posed question:
$$
\boxed{\ \text{Is local Weil positivity }(\lambda_{\min}\ge0)\ \text{more transparent in the }\{R_p\}\text{-coordinates than in }\{a_p\}\text{?}\ }
$$
i.e. does the *windowed local-factor repackaging* make the positivity (the sign) readable — does
factorizability $+$ a Ramanujan-type bound $|a_p|\le2$ force $\sum_p R_p\le R_\infty$ on a structural
sub-class? That is T4, and it is the first point where the repackaging could *earn its keep* — by making the
sign visible where $\{a_p\}$ does not. Honest prior: this is hard (it is RH on the full class), but a partial
result on a positivity-structured sub-class (e.g. $L$ with $a_p\ge0$, or Rankin–Selberg squares) is the
realistic, publishable target.

**Phasing (unchanged):** Phase 2 done (analytic) → **Phase 3** builds the validated engine to *measure* the
multiplicative structure / run the A-criterion band test on $\mathcal R(\zeta)$ vs $\mathcal R(L_{\mathrm{DH}})$.
Then the panel.

---

### Status
- A (Slepian, subspace-intrinsic, flat-envelope band test) — ✅ analytic.
- B (Prop B1: $R_p=$ windowed local factor; leading $=a_p$; factorizability $\equiv$ Euler product) — ✅ proved.
- C (stability $\|\mathcal R(L)-\mathcal R(L')\|\le C e^{-\alpha(\log P)^2}$) — ✅ proved (T1 + P7 II + Davis–Kahan).
- T4 seed (is positivity transparent in $\{R_p\}$?) — ⬜ the forward target.
- Phase 3 (validated engine: measure multiplicative structure / band test) — ⬜ after T4-seed analytic work.
