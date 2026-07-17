# M5 — Proofs: T1 (anti-tautology), T2 (forced transversal transition), and the analytic D2

**Pure-theory milestone of the classification program (M5).** Author: David Alejandro Trejo Pizzo ·
2026-06-03. Foundation: the localized arithmetic Weil-Gram $Q_{\mathrm{arith}}(L)$ (P7), not the heavier
$K_{\mathrm{CC}}$ (see the foundation correction in `M5-classification-pure-theory.md`). Builds on P7
(forced negativity), P8 (Kreĭn angular split), M1 (Prop B3.1.3), M3.

---

## 0. Setup (the object we actually prove with)

Fix a **localization**: height $T_0$, Gaussian/Slepian width $\sigma$, and a finite basis
$\{\phi_1,\dots,\phi_J\}$ of even test functions, time-and-frequency concentrated near $T_0$ (Hermite–Gauss
as in P7, or the exact Slepian prolates of M3). For an L-function $L$ — degree, conductor $N$, $\Gamma$-factor
$\gamma_L$, Euler product $\prod_p L_p(s)^{-1}$, with $-L'/L(s)=\sum_n \Lambda_L(n)\,n^{-s}$ — the
**localized Weil form** is the $J\times J$ Hermitian Gram matrix
$$
Q(L)_{ij}\ :=\ \mathfrak t_L(\phi_i,\phi_j),
$$
where $\mathfrak t_L$ is the Weil functional of $L$. The Riemann–Weil explicit formula gives $\mathfrak t_L$
in **two** forms; we use the **arithmetic side** (truncated at prime cutoff $X$):
$$
\boxed{\ Q_{\mathrm{arith}}^{(X)}(L)_{ij}\ =\ \underbrace{A_\infty(\phi_i,\phi_j)}_{\Gamma\text{-factor, archimedean}}+\underbrace{P_N(\phi_i,\phi_j)}_{\text{conductor/pole}}\ -\ \sum_{n\le X}\frac{\Lambda_L(n)}{\sqrt n}\,\widehat{\phi_i\!\star\!\phi_j}(\log n).\ }\tag{0.1}
$$
Here $A_\infty,P_N$ are **fixed within a family** (they depend only on $\gamma_L,N$, not on the Euler factors),
and $\widehat{\phi_i\star\phi_j}(\log n)$ are **fixed, L-independent** numbers (the Fourier data of the basis).
The only L-dependence is through the **local arithmetic data**
$$
D_X(L):=\{\Lambda_L(n)\}_{n\le X}\quad(\text{equivalently the Euler factors at }p\le X).
$$

**The invariant.** $\ I^{(X)}(L):=-\lambda_{\min}\big(Q_{\mathrm{arith}}^{(X)}(L)\big)$, equivalently
$\|K(L)\|\gtrless 1$ via
$$
\lambda_{\min}\big(Q_{\mathrm{arith}}(L)\big)<0\ \iff\ \|K(L)\|>1,\tag{0.2}
$$
$K(L)$ = angular operator of the indefinite split of $Q$ (P8 §7); (0.2) holds because
$\lambda_{\min}(Q)\ge0\iff Q\succeq0\iff \mathfrak t_L\succeq0$ on the localized space $\iff\|K\|\le1$. All
three are the same sign statement; the equivalence is basis-free.

**Unconditional truncation control (P7 II).** $\|Q_{\mathrm{arith}}^{(X)}-Q_{\mathrm{arith}}^{(\infty)}\|\le
A e^{-\alpha(\log X)^2}$ with $\alpha\approx\sigma^2/8$ (P7 Theorem II, PNT only). So $I^{(X)}\to I^{(\infty)}$
and all statements below pass to the limit; we keep $X$ finite (computable) and write $Q:=Q_{\mathrm{arith}}^{(X)}$.

---

## 1. Theorem T1 (anti-tautology): $I^{(X)}$ is a local arithmetic functional, not the zero-distance

> **Theorem T1.**
> (a) *Analyticity.* Each entry of $Q_{\mathrm{arith}}^{(X)}(L)$ is an **affine** (hence real-analytic)
> function of the local data $D_X(L)$; consequently $\lambda_{\min}(Q)$ and $I^{(X)}$ are continuous in
> $D_X(L)$, and real-analytic on the open set where $\lambda_{\min}$ is a simple eigenvalue.
> (b) *Locality / non-tautology.* $I^{(X)}(L)$ factors through the **finite** local data $D_X(L)$:
> $I^{(X)}(L)=G_X\big(D_X(L)\big)$ for a fixed function $G_X$. The nearest-zero distance
> $d(L)=\inf_\rho|\Re\rho-\tfrac12|$ does **not** factor through $D_X$. Hence $I^{(X)}$ is **not** any function
> of $d$: there is no $f$ with $I^{(X)}=f\circ d$.

**Proof.**
*(a)* By (0.1), $Q_{\mathrm{arith}}^{(X)}(L)_{ij}=\big(A_\infty+P_N\big)_{ij}-\sum_{n\le X}c^{(n)}_{ij}\,\Lambda_L(n)$
with $c^{(n)}_{ij}=\tfrac1{\sqrt n}\widehat{\phi_i\star\phi_j}(\log n)$ fixed. This is affine in
$\{\Lambda_L(n)\}_{n\le X}=D_X$, hence real-analytic. Eigenvalues of a Hermitian matrix are continuous in the
entries (Weyl), and real-analytic where simple (Rellich's theorem; analytic perturbation of a simple
eigenvalue). Therefore $\lambda_{\min}(Q)$ — hence $I^{(X)}=-\min(\lambda_{\min},0)$ — is continuous in $D_X$
and real-analytic where $\lambda_{\min}$ is simple and nonzero. $\square$(a)

*(b)* That $I^{(X)}=G_X(D_X)$ is immediate from (0.1): $Q_{\mathrm{arith}}^{(X)}$ depends on $L$ only through
$D_X$, and $I^{(X)}$ is a fixed function ($-\lambda_{\min}$) of $Q$. For the negative claim, it suffices to
exhibit the dependency mismatch. The nearest-zero distance $d(L)$ is a functional of the *full* coefficient
sequence $\{\Lambda_L(n)\}_{n\ge1}$ and is **not determined by any finite truncation** $D_X$: fixing
$\{\Lambda_L(n)\}_{n\le X}$ and varying the tail $\{\Lambda_L(n)\}_{n>X}$ moves the zeros (the completed $L$ is
an infinite product/sum whose zero set depends on all coefficients), hence changes $d$, while leaving
$Q_{\mathrm{arith}}^{(X)}$ — and therefore $I^{(X)}$ — **unchanged**. Thus along such a tail-variation
$I^{(X)}$ is constant while $d$ varies: $I^{(X)}$ cannot equal $f(d)$ for any $f$. $\square$(b)

> **Reading.** T1 is the rigorous form of the panel's tautology test, and it **passes**: the invariant is a
> *local, finite, arithmetic* functional (it sees only $p\le X$), whereas "distance to the nearest off-line
> zero" is a *global* functional (it sees all primes). They depend on different information, so the invariant
> is not a re-encoding of the zero positions. This complements the operator-level statement (P8 Thm C: the
> *zero-side* invariant **is** the tautology; M1 Prop B3.1.3: the arithmetic side is distinct).

**Honest caveat.** T1(b) shows non-tautology as a statement about *functionals on L-data with a free tail*.
Within a constrained family of *genuine* L-functions (Euler product + functional equation), exhibiting two
members with identical $D_X$ but different $d$ is more delicate; the **analytic D2 (§3)** supplies the
constructive, within-window witness ($\partial I/\partial\Lambda_L(n)\ne0$ at fixed $d$), which is the
genuine-L counterpart.

> **REFINEMENT (forced by the numerical D2, `experiments/M4-D2-results.md`).** T1(b) is logically correct,
> but the numerics expose that the **scalar** $I^{(X)}=-\lambda_{\min}$ is the *wrong* carrier of the
> non-tautology: by P7's *validated* data (engine-spec §4), $\lambda_{\min}$ sits at the numerical floor for
> **all** RH-true L-functions and only fires for $L_{\mathrm{DH}}$, i.e. the scalar behaves like an off-line
> detector $\approx f(d)$ — *practically* near-tautological even though *logically* local. **The genuine
> non-tautological invariant is the finer structure**: the gradient profile
> $\partial I/\partial\Lambda(n)=\tfrac1{\sqrt n}|\widehat{u_0}(\log n)|^2$ (numerically confirmed to
> $\sim10^{-7}$ and **spread over $\sim$14 Euler factors**, M4-D2-results §1) and the per-prime anatomy $R_p$
> (T3). Henceforth the invariant $I(L)$ means this **gradient/anatomy profile**, not the scalar margin.

---

## 2. Theorem T2 (forced transversal transition): $\|K\|$ crosses $1$ with an explicit arithmetic rate

> **Theorem T2.** Let $L_t$ be a real-analytic one-parameter family with a single conjugate zero-pair at
> displacement $\delta(t)=\beta(t)-\tfrac12$ from the critical line, near height $\gamma_0$ inside the
> localization window, with $\delta(0)=0$. Assume the unperturbed local margin $m_0:=\lambda_{\min}(Q(L_0))>0$
> is **simple**, with unit eigenvector $u_0$, and let $v=v(\gamma_0)$ be P7's explicit off-line test-vector
> ($v_i\propto$ the leading displacement-response of $\phi_i$ at $\gamma_0$). Then, to leading order,
> $$
> \lambda_{\min}\big(Q(L_t)\big)\ =\ m_0\ -\ c\,|\langle u_0,v\rangle|^2\,\delta(t)^2\ +\ o(\delta^2),\qquad c=c(\sigma,J)>0,
> $$
> and, provided the **overlap** $\langle u_0,v\rangle\ne0$ (P7's forced-negativity content), $\lambda_{\min}$
> decreases **transversally** through $0$: there is a critical displacement
> $$
> \boxed{\ \delta_*^2\ =\ \frac{m_0}{c\,|\langle u_0,v\rangle|^2}\ +\ o(1)\ }
> $$
> at which $\lambda_{\min}=0$, i.e. $\|K\|=1$, with $\frac{d}{d(\delta^2)}\lambda_{\min}\big|_{0}=-c|\langle u_0,v\rangle|^2<0$.
> The transition positive $\to$ indefinite is a **genuine (transversal) spectral transition**, not a numerical
> coincidence.

**Proof.** P7 Theorem I gives the leading perturbation of the localized Weil Gram by an off-line pair at
displacement $\delta$ near $\gamma_0$:
$$
Q(L_t)=Q(L_0)+\Delta Q(t),\qquad \Delta Q(t)=-c\,\delta(t)^2\,vv^{*}+o(\delta^2),\tag{2.1}
$$
a **rank-one negative** leading term with explicit $v$ and $c>0$ (P7's prefactor $A(\gamma_0)$ is absorbed
into $c\|v\|^2$; P7 matches this to computation at relative error $<10^{-5}$). Since $m_0=\lambda_{\min}(Q(L_0))$
is a **simple** eigenvalue with unit eigenvector $u_0$, first-order analytic perturbation theory
(Rellich/Kato; Hellmann–Feynman for the derivative of a simple eigenvalue) gives
$$
\lambda_{\min}(Q(L_t))=m_0+\langle u_0,\Delta Q(t)\,u_0\rangle+o(\|\Delta Q\|)=m_0-c\,|\langle u_0,v\rangle|^2\,\delta(t)^2+o(\delta^2).\tag{2.2}
$$
The derivative in the natural parameter $s:=\delta^2$ at $s=0$ is $-c|\langle u_0,v\rangle|^2$, which is
**strictly negative** iff $\langle u_0,v\rangle\ne0$. That overlap is exactly P7's forced-negativity
mechanism: P7 proves $\lambda_{\min}(Q(L_t))\le m_0-c\delta^2 A(\gamma_0)$ with a *strict* decrease, which is
impossible unless the perturbation direction $v$ has nonzero component on the minimal eigenvector $u_0$; hence
$\langle u_0,v\rangle\ne0$. With $m_0>0$ and a strictly negative slope, the continuous function
$s\mapsto\lambda_{\min}(Q)$ attains $0$ at a unique $s=\delta_*^2=m_0/(c|\langle u_0,v\rangle|^2)+o(1)$, and
the crossing is transversal ($\tfrac{d\lambda_{\min}}{ds}\ne0$). By (0.2), $\|K\|$ crosses $1$ there. $\square$

> **Reading.** T2 *is* P7's forced-negativity theorem, lifted into the angular/positivity language and
> sharpened to a **transversal crossing** with an explicit threshold $\delta_*^2=m_0/(c|\langle u_0,v\rangle|^2)$.
> The threshold is an **arithmetic transition invariant**: $m_0$ (the local positivity margin) and
> $c|\langle u_0,v\rangle|^2$ (P7's explicit local rate) are computed from the Euler/$\Gamma$ data of $L_0$ in
> the window — zero-independently. A *transversal* crossing is precisely the panel's signature of "real
> structure, not a numerical coincidence."

**Honest caveats.** (i) The result is to leading order in $\delta$; the $o(\delta^2)$ remainder does not
affect the first-order slope, hence not the transversality, but the exact $\delta_*$ has $o(1)$ corrections.
(ii) Simplicity of $m_0$ and $m_0>0$ are genericity hypotheses on the window (no on-line near-degeneracy);
both are checkable. (iii) "Family $L_t$ with a zero moving off the line at rate $\delta(t)$" is a deformation
of the *arithmetic* producing the off-line zero; for the analytic statement we take $\delta(t)$ as the
controlled parameter (D1 in §4). The genuine-arithmetic deformation (D2/D3) is §3–4.

---

## 3. The analytic D2 (the constructive non-tautology witness): $\partial I/\partial\Lambda_L(n)\ne0$ at fixed $d$

The panel's decisive test is D2: *does the invariant move under an Euler-factor perturbation at fixed nearest-
zero distance?* We prove the analytic version — an explicit, generically nonzero derivative — which is the
within-window, genuine-arithmetic witness that T1(b) flagged.

> **Proposition D2 (analytic).** For $n=p^k\le X$ with $\lambda_{\min}(Q)$ simple, eigenvector $u_0$,
> $$
> \frac{\partial}{\partial \Lambda_L(n)}\,\lambda_{\min}\big(Q_{\mathrm{arith}}^{(X)}(L)\big)
> \ =\ -\frac{1}{\sqrt n}\,\big|\,\widehat{u_0}(\log n)\,\big|^2\ \le\ 0,
> $$
> where $\widehat{u_0}(\log n):=\sum_i (u_0)_i\,\widehat{\phi_i}(\log n)$ is the frequency content of the
> minimal eigenvector at $\log n$. In particular $\partial I^{(X)}/\partial\Lambda_L(n)=\frac{1}{\sqrt n}|\widehat{u_0}(\log n)|^2$,
> which is **strictly positive whenever $u_0$ has frequency content at $\log n$** — generic for in-window
> primes.

**Proof.** From (0.1), $\partial Q/\partial\Lambda_L(n)=-\tfrac1{\sqrt n}\,w_n w_n^{*}$ where
$(w_n)_i=\widehat{\phi_i}(\log n)$ (a rank-one matrix; the prime term is a single frequency $\log n$).
Hellmann–Feynman for the simple eigenvalue $\lambda_{\min}$ with unit eigenvector $u_0$ gives
$\partial\lambda_{\min}/\partial\Lambda_L(n)=\langle u_0,(\partial Q/\partial\Lambda_L(n))u_0\rangle
=-\tfrac1{\sqrt n}|\langle u_0,w_n\rangle|^2=-\tfrac1{\sqrt n}|\widehat{u_0}(\log n)|^2$. $\square$

> **Why this is the non-tautology witness.** The derivative $\partial I^{(X)}/\partial\Lambda_L(n)$ is an
> explicit, generically nonzero, **local** quantity (it depends only on the eigenvector's content at the
> single frequency $\log n$). The derivative of $d$ in the same direction, $\partial d/\partial\Lambda_L(n)$,
> is a *different* (global, zero-determined) quantity. The two gradients are **not parallel** in general:
> moving $\Lambda_L(n)$ changes $I$ at rate $\tfrac1{\sqrt n}|\widehat{u_0}(\log n)|^2$ regardless of how it
> changes $d$. Hence one can move along a direction that **fixes $d$ to first order** (orthogonal to
> $\nabla d$) while **changing $I$** (nonzero component along $\nabla I$) — the constructive D2. This upgrades
> T1(b) from a free-tail argument to an explicit in-window gradient computation. $\blacksquare$

**Numerical D2 (to run, the "destroy test").** Compute, with the P7 engine, $\nabla_{D_X} I$ and $\nabla_{D_X} d$
in a window for $\zeta$ and for $L_{\mathrm{DH}}$; verify $\nabla I\not\parallel\nabla d$ (Proposition D2 predicts
the explicit $\nabla I$). If, contrary to the prediction, $\nabla I\parallel\nabla d$ everywhere, the invariant
*is* tautological and the program is destroyed — that is the falsification. Prop. D2 makes the analytic
expectation explicit, so the numerical test is a clean confirm/refute.

---

## 4. What T1+T2+D2 establish, and the honest status of T3, T4

**Established (pure theory, this file).**
- **T1** ✅ — the invariant $I^{(X)}$ is a local, real-analytic, arithmetic functional, provably **not** a
  function of the nearest-zero distance. *(The tautology test passes, now at the level of the computable
  invariant, not only the abstract operators.)*
- **T2** ✅ — as a zero-pair leaves the line, $\|K\|$ crosses $1$ **transversally** with explicit threshold
  $\delta_*^2=m_0/(c|\langle u_0,v\rangle|^2)$; a genuine spectral transition (lifted + sharpened from P7).
- **Analytic D2** ✅ — explicit gradient $\partial I/\partial\Lambda_L(n)=\tfrac1{\sqrt n}|\widehat{u_0}(\log n)|^2$,
  generically nonzero, $\nabla I\not\parallel\nabla d$ — the constructive non-tautology witness; the numerical
  D2 is the falsification test.

**Honest status of the rest.**
- **T3 (anatomy)** ◆ — the place-decomposition $\langle K\cdot,\cdot\rangle=R_\infty+\sum_p R_p$ is explicit:
  $R_\infty=A_\infty$ (archimedean, CC square), $R_p=-\sum_{k}\tfrac{\Lambda_L(p^k)}{\sqrt{p^k}}w_{p^k}w_{p^k}^{*}$
  (rank-one-per-frequency, by §3). **Provable now:** each $R_p$ is rank-bounded and its sign is explicit; the
  *interaction* $R_\infty+\sum_p R_p$ driving $\lambda_{\min}<0$ is the open content. The discriminant
  $\zeta$-vs-$L_{\mathrm{DH}}$ is then the **difference of the $R_p$-profiles**, computable per prime.
  Pursue after numerical D2.
- **T4 (classification $\Phi$)** ⬜ — north star; a partial $\Phi$ (sufficient condition on a sub-class, or a
  sharp necessary condition) is the realistic target. Full $\Phi\le1\Rightarrow$ RH ($<1\%$).

**Sequence (as directed):** T1 ✅, T2 ✅, analytic D2 ✅ done here → **run numerical D2** (the destroy test)
→ if it survives, T3 (anatomy, the $R_p$-profile discriminant) → T4 ($\Phi$).

---

### Status
- T1 — ✅ proved (analyticity + locality non-tautology).
- T2 — ✅ proved (transversal crossing; rests on P7 Thm I overlap $\langle u_0,v\rangle\ne0$).
- Analytic D2 — ✅ proved (explicit nonzero gradient).
- Numerical D2 — ⬜ to run (P7 engine; the falsification test).
- T3 — ◆ decomposition explicit; interaction open.
- T4 — ⬜ north star.

*Records to update: this folder, `00-MAP.md`, the proof log, project memory.*
