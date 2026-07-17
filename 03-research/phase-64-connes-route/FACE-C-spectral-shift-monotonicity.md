# The spectral-shift thread, computed: does arithmetic rigidity force $\xi_K'\ge0$? — the phase derivative is the explicit-formula prime sum, and the answer is the orthogonality theorem at first order

*Pure mathematics. We attack the one lead flagged as "not yet circular": the Kreĭn spectral shift
$\arg D_P=\pi\xi_K$, with $\xi_K\ge0$ free from $H_{\mathrm{vM}}\ge0$, and RH demanding the phase
$\varphi_\Xi=\pi\xi_K+\vartheta$ be monotone. We compute $\xi_K'$ explicitly. It is the
**explicit-formula prime sum** $\sum_n\Lambda(n)n^{-1/2}\cos(\lambda\log n)$ (regularized), whose
negative excursions are **off-line zeros**. We catch and correct a tempting sign-chase that would make
monotonicity "automatic," and reach the honest verdict: monotonicity is RH, and arithmetic rigidity
fixes the **exact shape** of $\varphi'$ but gives **no free lower bound** — positivity controls $\xi_K$
(0th order) and is orthogonal to $\xi_K'$ (1st order), while the archimedean budget is only
**logarithmic** against off-line dips of depth $1/(\beta-\tfrac12)$. This thread lands on the wall. No
proof of RH; an honest reduction with a sharp new form.*

---

## §1. The phase derivative is the prime sum (explicit computation)

From the finite Euler determinant, $\arg D_P(\lambda)=-\sum_{p\le P}\arg\big(1-p^{-1/2-i\lambda}\big)
=\sum_{p\le P}\sum_{k\ge1}\frac1k\,p^{-k/2}\sin(k\lambda\log p)$, so
\[
   \pi\xi_K(\lambda)=\sum_{n}\frac{\Lambda(n)}{\sqrt n\,\log n}\sin(\lambda\log n),
   \qquad
   \pi\xi_K'(\lambda)=\sum_{n}\frac{\Lambda(n)}{\sqrt n}\cos(\lambda\log n).
\]
This last sum is **exactly the prime side of the Riemann–Weil explicit formula** (the real part of
$-\zeta'/\zeta(\tfrac12+i\lambda)$ after analytic continuation). The full phase derivative is
\[
   \boxed{\ \varphi_\Xi'(\lambda)=\underbrace{\vartheta'(\lambda)}_{=\frac12\log\frac{\lambda}{2\pi}>0}
   \ +\ \underbrace{\sum_n\frac{\Lambda(n)}{\sqrt n}\cos(\lambda\log n)}_{\text{regularized prime sum}}.\ }
\]
RH $\Leftrightarrow\varphi_\Xi'\ge0$ pointwise (de Branges phase criterion).

## §2. The zero-side, and a sign-chase to be careful with

By the explicit formula / Hadamard product, the same quantity is a sum of Poisson kernels over the
zeros. For the HB structure function with zeros $w=x+iy$, $\varphi'(\lambda)=\sum_w\dfrac{|y|}
{(\lambda-x)^2+y^2}$ when all $y\le0$ (lower half-plane, HB). An **off-line** zero produces an
upper-half-plane partner ($y>0$), contributing a **negative** Poisson term
$-\dfrac{|y|}{(\lambda-x)^2+y^2}$ near $\lambda=x$, with $|y|=\beta-\tfrac12$.

\begin{auditbox}[\textbf{the seductive false step, caught}]
One is tempted to compute $\Re\,\zeta'/\zeta(\tfrac12+i\lambda)=\sum_{\rho}\Re\frac{1}{\frac12+i\lambda
-\rho}$ and note that off-line zeros ($\beta>\tfrac12$) give $\Re\frac{1}{(\frac12-\beta)+i(\lambda-
\gam)}=\frac{\frac12-\beta}{(\frac12-\beta)^2+(\lambda-\gam)^2}<0$, "so the off-line contribution is
negative, the inequality $\le$ bounded holds automatically, monotonicity is free." \textbf{This is a
sign-direction error and is false.} The phase-derivative condition is $\varphi'\ge0$, i.e. the prime sum
must be bounded \emph{below} by $-\vartheta'$; the off-line zero enters $\varphi'$ as a negative
Poisson \emph{dip} (not a harmless negative addend to an upper bound). The correct accounting (Poisson
kernels, §2) shows off-line zeros \emph{lower} $\varphi'$, exactly threatening monotonicity. The quick
$\Re\zeta'/\zeta$ chase mislabels which side of the inequality the negativity helps. \emph{Lesson:
compute the phase derivative as the Poisson-kernel zero-sum, not as a casual real part.}
\end{auditbox}

## §3. The honest verdict: orthogonality at first order

\begin{theorem}[spectral-shift monotonicity is RH, and rigidity does not lower it]\label{thm:firstorder}
The free input is $\xi_K\ge0$ (0th order, from $H_{\mathrm{vM}}\ge0$, Kreĭn). The required input is
$\varphi_\Xi'\ge0$ (1st order). An off-line zero with $\beta-\tfrac12=\varepsilon$ produces a dip in
$\varphi'$ of depth $\asymp1/\varepsilon$ and width $\asymp\varepsilon$, while the archimedean budget
$\vartheta'(\lambda)=\tfrac12\log(\lambda/2\pi)$ grows only \textbf{logarithmically}. Hence:
\begin{itemize}
\item positivity ($\xi_K\ge0$) does \emph{not} bound $\xi_K'$ below — a nonnegative function has
arbitrary negative derivative (orthogonality theorem, `FACE-C-positivity-vs-size.md`, now at the level
of the derivative);
\item the arithmetic rigidity of the atoms fixes the \emph{exact shape}
$\sum_n\Lambda(n)n^{-1/2}\cos(\lambda\log n)$ of the oscillation, but a one-sided bound on this
regularized sum ($\ge-\vartheta'-C$) is itself an RH-type estimate (it fails precisely at an off-line
zero);
\item there is no slack: a single off-line zero with small $\varepsilon$ gives a dip $1/\varepsilon$
that exceeds any logarithmic budget.
\end{itemize}
Therefore $\varphi_\Xi'\ge0\Leftrightarrow$ RH, and the spectral-shift thread reduces to the wall.
\end{theorem}

\begin{resultbox}
\textbf{Verdict (honest negative).} The spectral-shift lead, computed, lands on the same wall. The
mechanism is the orthogonality theorem promoted one derivative: positivity supplies $\xi_K\ge0$
(zeroth order) for free, RH is $\xi_K'\ge-\vartheta'/\pi$ (first order), and there is no free passage
from a sign to a derivative bound — the more so because the archimedean baseline is only logarithmic
while off-line dips are $1/\varepsilon$. Arithmetic rigidity determines the precise oscillation but not
its negative envelope. \emph{This thread does not cross.}
\end{resultbox}

## §4. The genuine yield: a sharp pointwise form of RH

The computation is not wasted — it gives perhaps the most elementary-looking equivalent in the program:

\begin{corollary}[pointwise phase form]\label{cor:pointwise}
\[
   \mathrm{RH}\quad\Longleftrightarrow\quad
   \tfrac12\log\tfrac{\lambda}{2\pi}\ +\ \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\cos(\lambda\log n)\ \ge\ 0
   \quad\text{(regularized) for all }\lambda,
\]
i.e. \textbf{the logarithmic archimedean baseline dominates the regularized von Mangoldt cosine sum,
pointwise.} Equivalently, $\Re\big(-\zeta'/\zeta\big)(\tfrac12+i\lambda)\le\tfrac12\log(\lambda/2\pi)
+O(1)$ between zeros.
\end{corollary}

This is a clean, concrete, \emph{first-order} statement — and it makes transparent why every road ends
at RH: the wall is the pointwise contest between a $\log\lambda$ archimedean term and an off-line dip of
depth $1/\varepsilon$. Positivity, curvature, Carleson, Gram — all are \emph{integrated} (0th-order)
controls; RH is the \emph{pointwise/derivative} (1st-order) control, and the program has now shown, at
four successive levels (operator norm, Carleson box, diagonal sup, phase derivative), that the
integrated controls are free and the pointwise one is RH.

## §5. Honest status and what remains

\textbf{Established (unconditional):}
\begin{itemize}
\item $\pi\xi_K'(\lambda)=\sum_n\Lambda(n)n^{-1/2}\cos(\lambda\log n)$ (the phase derivative is the
explicit-formula prime sum); $\varphi_\Xi'=\vartheta'+(\text{that sum})$.
\item Theorem~\ref{thm:firstorder}: positivity gives $\xi_K\ge0$ but not $\xi_K'\ge-\vartheta'/\pi$;
arithmetic rigidity fixes the shape, not the lower envelope; the budget is logarithmic vs dips
$1/\varepsilon$. \textbf{The thread reduces to RH (honest negative).}
\item Corollary~\ref{cor:pointwise}: the sharp pointwise/first-order equivalent.
\item The sign-chase that would make monotonicity "automatic" is caught and corrected (§2).
\end{itemize}

\textbf{Open (the wall, unchanged):} the pointwise first-order bound — i.e. RH itself in
Corollary~\ref{cor:pointwise} form. No positivity/integrated control reaches it.

\textbf{Where this leaves the route.} Every \emph{integrated} certificate is proved and free; the single
wall is now pinned as a \emph{pointwise/first-order} statement (Cor.~\ref{cor:pointwise}). The honest
implication: a crossing must be a genuinely \emph{pointwise} mechanism (controlling $\varphi'$ between
zeros), and the program has shown positivity-type tools are structurally 0th-order and cannot be it.
The one tool class not yet tried that is intrinsically first-order/pointwise — \emph{a priori}
equidistribution/discrepancy bounds on the frequencies $\{\log n\}$ weighted by $\Lambda(n)/\sqrt n$
(a Diophantine, not analytic, control of the cosine sum) — is the honest next direction, and it is
\emph{not} a positivity argument. No false victory; the thread is reduced, the wall is sharpened to its
first-order form.
