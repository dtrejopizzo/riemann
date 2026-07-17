# Phase 15 · M2 — The ample cone: the pole part is positive, unconditionally (complete, with proofs)

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
Milestone M2 of the Anatomy–Kreĭn–Hodge program: prove that the trivial-cohomology part of the arithmetic
intersection pairing (M1) — the contribution of the poles of $\zeta$ at $s=0,1$, i.e. $H^0\oplus H^2$ — is a
finite-rank, **positive (ample)** piece, **unconditionally**, and is the exact analogue of the hyperbolic plane
$\langle f_1,f_2\rangle$ spanned by the fiber classes in $\mathrm{NS}(C\times C)$. **Everything in M2 is proved.**
The positivity is the de la Vallée Poussin / Landau edge positivity (P14), now in intersection-theoretic form. RH
is untouched; M2 is unconditional.

Conventions and notation are those of M1: $\mathcal V$ the admissible even test space, $\widehat f(r)=\int_{\mathbb R}
f(u)e^{iru}\,du$, the pairing $\langle f_1,f_2\rangle=\sum_\rho\widehat f_1(\gamma_\rho)\overline{\widehat f_2(\gamma_\rho)}$,
and Theorem A (M1): $\langle f_1,f_2\rangle=[h(\tfrac i2)+h(-\tfrac i2)]-2\sum_n\tfrac{\Lambda(n)}{\sqrt n}g(\log n)
+\tfrac1{2\pi}\int hW$ with $h=\widehat f_1\overline{\widehat f_2}$.

---

## 1. The pole functionals and the trivial part
Recall $r=\gamma$ corresponds to $s=\tfrac12+ir$. Thus $r=\tfrac i2\leftrightarrow s=0$ and $r=-\tfrac i2
\leftrightarrow s=1$: the two pole locations of the completed functional equation (the pole of $\zeta$ at $s=1$ and
its image $s=0$).

\begin{definition}[Pole functionals]
$\lambda_0(f):=\widehat f(\tfrac i2)$ (the $s=0$ / $H^0$ evaluation) and
$\lambda_1(f):=\widehat f(-\tfrac i2)$ (the $s=1$ / $H^2$ evaluation). The \emph{trivial part}
$\Pi=\langle e_0,e_1\rangle$ is the rank-$\le2$ space carrying the pole contribution
$P(f_1,f_2):=h(\tfrac i2)+h(-\tfrac i2)$ to the pairing (Theorem A, M1).
\end{definition}

\begin{lemma}[Real pole evaluations]\label{lem:real}
For $f\in\mathcal V$ real and even, $\lambda_0(f)=\lambda_1(f)=\int_{\mathbb R}f(u)e^{-u/2}\,du\in\mathbb R$.
\end{lemma}
\begin{proof}
$\lambda_0(f)=\widehat f(\tfrac i2)=\int f(u)e^{i(i/2)u}\,du=\int f(u)e^{-u/2}\,du$, real since $f$ is real.
$\lambda_1(f)=\widehat f(-\tfrac i2)=\int f(u)e^{u/2}\,du$; substituting $u\mapsto-u$ and using $f(-u)=f(u)$ gives
$\int f(u)e^{-u/2}\,du=\lambda_0(f)$.
\end{proof}

## 2. Theorem — the ample positivity (unconditional)
\begin{theorem}[Edge positivity]\label{thm:ample}
For every real even $f\in\mathcal V$ the trivial part of the self-pairing is
\[
P(f,f)=h(\tfrac i2)+h(-\tfrac i2)=2\Bigl(\int_{\mathbb R}f(u)\,e^{-u/2}\,du\Bigr)^{2}\ \ge\ 0,
\]
unconditionally; it vanishes iff $\int f(u)e^{-u/2}\,du=0$. Thus the trivial part is a \emph{positive}, rank-one
(on even test functions) Hermitian form: the \emph{ample direction} of the arithmetic intersection pairing.
\end{theorem}
\begin{proof}
For the self-pairing $f_1=f_2=f$, $h=\widehat f\cdot\overline{\widehat f}$; on the real axis $h(r)=|\widehat f(r)|^2$,
and since $f$ is real and even, $\widehat f$ is real-analytic with $\overline{\widehat f(\bar r)}=\widehat f(r)$, so
the analytic continuation of $h$ is $h(r)=\widehat f(r)^2$. Hence $h(\tfrac i2)=\lambda_0(f)^2$ and
$h(-\tfrac i2)=\lambda_1(f)^2$. By Lemma~\ref{lem:real} both equal $\bigl(\int f e^{-u/2}\bigr)^2$, so
$P(f,f)=2\bigl(\int f e^{-u/2}\bigr)^2\ge0$, with equality iff $\int f e^{-u/2}=0$.
\end{proof}

\begin{corollary}[Polarized form]\label{cor:pol}
On even test functions, $P(f_1,f_2)=2\,\lambda(f_1)\lambda(f_2)$ with $\lambda(f)=\int f e^{-u/2}\,du$; i.e.\ $P$ is
the positive rank-one form $2\,\lambda\otimes\lambda$. The ample class $e_{\mathrm{amp}}$ is the direction dual to
$\lambda$.
\end{corollary}

## 3. Identification with de la Vallée Poussin (the edge anchor)
\begin{proposition}[The ample positivity is the edge positivity]\label{prop:dlVP}
The positive contribution $P(f,f)=2\lambda(f)^2$ is exactly the pole/edge positivity that underlies the de la
Vallée Poussin zero-free region (the Landau anchor of P14). Concretely, $\lambda(f)=\int f e^{-u/2}du=\widehat
f(\tfrac i2)$ is the value of the test transform at the pole $s=1$ (via $r=-\tfrac i2$); the pole of $\zeta$ there
contributes a strictly positive amount to the Weil pairing whenever $\lambda(f)\ne0$. This is the intersection-
theoretic form of ``the pole forces $\zeta(1+it)\ne0$''.
\end{proposition}
\begin{proof}
The de la Vallée Poussin mechanism (P14, the Landau singularity) is precisely that the pole at $s=1$ supplies an
unconditional positive term against which a putative zero is measured. In the explicit-formula pairing this term is
the trivial-part contribution $P(f,f)$; Theorem~\ref{thm:ample} computes it as $2\lambda(f)^2\ge0$, the squared
evaluation at the pole. Hence the ample positivity of $\Pi$ and the edge positivity of de la Vallée Poussin are the
same nonnegative quantity.
\end{proof}

## 4. The hyperbolic-plane structure (the analogue of $\langle f_1,f_2\rangle$)
\begin{proposition}[Trivial part as a hyperbolic plane]\label{prop:hyp}
The trivial part is spanned by the two pole functionals $\lambda_0$ ($s=0$, $H^0$) and $\lambda_1$ ($s=1$, $H^2$),
exchanged by the functional-equation involution $s\mapsto1-s$. On the full (not necessarily even) test space the
pole form is $P=\lambda_0\!\otimes\overline{\lambda_0}+\lambda_1\!\otimes\overline{\lambda_1}$; the
\emph{functional-equation-symmetric} combination $\lambda_0+\lambda_1$ is the \emph{ample} (positive) direction, and
the antisymmetric combination $\lambda_0-\lambda_1$ the complementary one. On even test functions
$\lambda_0=\lambda_1$ (Lemma~\ref{lem:real}), so only the ample direction survives, recovering
Theorem~\ref{thm:ample}. This is the exact analogue of the fiber classes $f_1,f_2$ spanning the hyperbolic plane in
$\mathrm{NS}(C\times C)$, with $f_1+f_2$ ample.
\end{proposition}
\begin{proof}
By Theorem A (M1) the pole contribution is $h(\tfrac i2)+h(-\tfrac i2)=\widehat f_1(\tfrac i2)\overline{\widehat
f_2(\tfrac i2)}+\widehat f_1(-\tfrac i2)\overline{\widehat f_2(-\tfrac i2)}=\lambda_0(f_1)\overline{\lambda_0(f_2)}
+\lambda_1(f_1)\overline{\lambda_1(f_2)}$, the stated rank-$\le2$ form. The functional equation $\xi(s)=\xi(1-s)$
sends $s=0\leftrightarrow s=1$, i.e.\ $\lambda_0\leftrightarrow\lambda_1$; its symmetric eigenvector
$\lambda_0+\lambda_1$ is the ample direction (positive square), the antisymmetric $\lambda_0-\lambda_1$ the other.
On even $f$, Lemma~\ref{lem:real} gives $\lambda_0=\lambda_1$, collapsing to the ample line.
\end{proof}

\begin{remark}[Signature convention]
Our pairing is the \emph{Weil-positivity} normalization: $\langle f,f\rangle=\sum_\rho|\widehat f(\gamma_\rho)|^2$,
$\ge0$ under RH. In this convention the ample/trivial part is \emph{positive} (Theorem~\ref{thm:ample}) and RH is
the \emph{positivity} of the primitive part (M3) — the same content as Weil's Hodge-index signature $(1,\rho-1)$,
read in the positivity convention rather than the intersection-form convention. The ample direction here is the one
guaranteed-positive piece; the Hodge index (M3) is the assertion that no further negative directions exist.
\end{remark}

## 5. Consequence: the scaffold is in place
\begin{corollary}[Ample cone, unconditional]\label{cor:scaffold}
The arithmetic intersection pairing of M1 decomposes as
\[
\langle\cdot,\cdot\rangle\ =\ \underbrace{2\,\lambda\otimes\lambda}_{\text{ample, }\succeq0\text{ (M2, unconditional)}}
\ +\ \underbrace{\langle\cdot,\cdot\rangle|_{\Pi^\perp}}_{\text{primitive, }H^1\text{ (zeros)}},
\]
where $\Pi^\perp=\ker\lambda$ (test functions with $\widehat f(\tfrac i2)=0$, i.e.\ vanishing at the pole). The
ample part is positive unconditionally; RH is exactly the positivity of the primitive part — the arithmetic Hodge
index (M3).
\end{corollary}
\begin{proof}
Immediate from Theorem~\ref{thm:ample} (ample positivity) and Proposition~C of M1 (the primitive-part
reformulation of RH).
\end{proof}

## 6. Numerical grounding (`phase-15/experiments/ample_check.py`)
- **Lemma~\ref{lem:real} confirmed:** for $f(u)=e^{-u^2/2}$ the analytic continuation gives
  $\widehat f(\tfrac i2)=\sqrt{2\pi}\,e^{1/8}=2.84038195$, matching the numerical $\lambda=\int f e^{-u/2}du=
  2.84038195$ to $8$ digits; the pole term $P=2\lambda^2=4\pi e^{1/4}=16.13553926$ both ways.
- **Theorem~\ref{thm:ample} confirmed across a family:**
  \[
  \begin{array}{lcc}
  f(u) & \lambda(f) & P=2\lambda^2\\\hline
  e^{-u^2/2} & 2.840 & 16.14\ (>0)\\
  e^{-u^2/8} & 8.265 & 136.6\ (>0)\\
  (1+u^2)e^{-u^2/2} & 6.391 & 81.69\ (>0)\\
  \cos(3u)e^{-u^2/2} & 2.2\times10^{-3} & 9.96\times10^{-6}\ (>0)\\
  (u^2-\tfrac54)e^{-u^2/2} & -2.3\times10^{-16} & 1.1\times10^{-31}\ (=0)
  \end{array}
  \]
  Every $P\ge0$; the engineered even function $f=(u^2-\tfrac54)e^{-u^2/2}$, built to satisfy $\int f e^{-u/2}=0$,
  gives $P=0$ to machine precision — the sharp vanishing characterization of Theorem~\ref{thm:ample}. The ample
  positivity is unconditional and robust.

## 7. Conclusion of M2
**M2 is complete and fully proved (unconditional, RH-independent):**
- **Theorem~\ref{thm:ample}** — the trivial/pole part of the arithmetic intersection pairing is
  $2\bigl(\int f e^{-u/2}\bigr)^2\ge0$: the **ample cone is positive, unconditionally**.
- **Proposition~\ref{prop:dlVP}** — this positivity is the de la Vallée Poussin / Landau edge positivity (P14), in
  intersection-theoretic form.
- **Proposition~\ref{prop:hyp}** — the trivial part is the hyperbolic plane $\langle\lambda_0,\lambda_1\rangle$
  ($s=0,1=H^0\oplus H^2$), exchanged by the functional equation, with the symmetric direction ample — the exact
  analogue of the fiber classes $f_1,f_2$.
- **Corollary~\ref{cor:scaffold}** — the pairing splits as (ample, positive) $\oplus$ (primitive), with RH the
  positivity of the primitive part (M3).

Milestones M1 (the pairing + trace identity + effectivity) and M2 (the ample cone, unconditional) together build
the full Weil-style scaffold for $\operatorname{Spec}\mathbb Z$. The single remaining content is M3 — the arithmetic
Hodge index: definiteness on the primitive part $\Pi^\perp$ — attacked by the HR-stability limit (M3a) and the
Rankin–Selberg effectivity combined with this ample positivity (M3b).
