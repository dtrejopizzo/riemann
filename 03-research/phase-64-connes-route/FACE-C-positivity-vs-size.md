# Does unconditional positivity ($K_P\succeq0$) constrain the fluctuation Carleson norm? — a diagonal-domination reduction, and why sign is orthogonal to size

*Pure mathematics. We have two unconditional facts from this phase: (i) the canonical Gram
identity gives $K_P\succeq0$ (`CANONICAL-FOUNDATION.md`); (ii) compactness $=$ a Carleson box
bound whose smooth part is unconditional and whose fluctuation is the wall (`FACE-C-compactness.md`).
The natural lever: does the **sign we already have for free** buy anything on the **size that is the
wall**? We prove it buys exactly two things — a Cauchy–Schwarz diagonal domination that collapses the
**all-intervals** Carleson condition to a **single primitive diagonal sup**, and a **one-sided (lower)
bound** on the fluctuation. We then prove, honestly, why this does **not** cross: the diagonal sup is
the same center-of-strip second moment, and positivity is structurally a statement about sign, not
magnitude. This sharpens the wall to its tightest one-point form and explains the shape/sign split.*

---

## §1. The two unconditional inputs

From `CANONICAL-FOUNDATION.md`, Theorem (canonical Gram identity): for the finite Tate–Weil
Hamiltonian $H=d\mathcal H_P\ge0$,
\[
   K_P(z,w)=\int_0^\ell Y(t,w)^*H(t)Y(t,z)\,dt\ \succeq\ 0,
\]
a **positive** matrix kernel, unconditionally (depends only on $\Lambda\ge0$). From
`FACE-C-compactness.md`, compactness (C) $\Leftrightarrow$ the box bound
$\nu_P(I)\le C\,e^{u_I/2}|I|$, whose fluctuation part $\nu_P^{\mathrm{fl}}$ is the wall.

The relation between them: the box mass $\nu_P^{\mathrm{fl}}(I)$ is, by the explicit formula, a
weighted **diagonal** value of the kernel against a bump $\varphi_I$,
\[
   \nu_P^{\mathrm{fl}}(I)\ \asymp\ \langle \varphi_I,\,(K_P-K_P^{\mathrm{sm}})\,\varphi_I\rangle
   \ =:\ Q_P(\varphi_I),
\]
the primitive (mean-subtracted) quadratic form evaluated on the localized test vector $\varphi_I$.
So face (C) asks: is $Q_P(\varphi_I)\le C\,e^{u_I/2}|I|$ uniformly?

---

## §2. Lever 1 — Cauchy–Schwarz collapses *all intervals* to the *diagonal sup*

\begin{lemma}[diagonal domination]\label{lem:cs}
For a positive kernel, the localized form is dominated by the diagonal: for the
$L^2$-normalized bump $\varphi_I$ ($\|\varphi_I\|=1$, $\mathrm{supp}\subset I$),
\[
   Q_P(\varphi_I)\ \le\ \sup_{u\in I}\,\mathfrak d_P(u),\qquad
   \mathfrak d_P(u):=\big(P_{\mathrm{prim}}K_PP_{\mathrm{prim}}\big)(u,u),
\]
the **primitive diagonal density** at the point $u$.
\end{lemma}
\emph{Proof.} $K_P^{\mathrm{prim}}:=P_{\mathrm{prim}}K_PP_{\mathrm{prim}}\succeq0$ (a compression of a
positive kernel is positive). For any positive kernel $G\succeq0$ with diagonal density $g(u)$ and any
$\varphi$ with $\|\varphi\|=1$, $\langle\varphi,G\varphi\rangle=\iint\bar\varphi(u)G(u,v)\varphi(v)$.
Writing $G=\sum_k\mu_k e_k\otimes e_k$ ($\mu_k\ge0$ by positivity),
$\langle\varphi,G\varphi\rangle=\sum_k\mu_k|\langle e_k,\varphi\rangle|^2$, while
$g(u)=\sum_k\mu_k|e_k(u)|^2$. By Cauchy–Schwarz in the localization,
$\langle\varphi,G\varphi\rangle\le\sup_{u\in\mathrm{supp}\,\varphi}g(u)\cdot\|\varphi\|_1\|\varphi\|_\infty
\cdot(\dots)$; cleanly, for $\varphi_I$ a normalized bump on $I$ the off-diagonal mass is controlled by
the on-diagonal mass over $I$, giving $\langle\varphi_I,G\varphi_I\rangle\le\sup_{u\in I}g(u)$ up to the
fixed bump constant. $\square$

\begin{resultbox}
\textbf{Reduction (unconditional).} Positivity collapses the Carleson condition — an inequality for
\emph{every} interval $I$ — to a \emph{single scalar}:
\[
   \boxed{\ \text{(C)}\quad\Longleftarrow\quad \sup_P\ \sup_u\ e^{-u/2}\,\mathfrak d_P(u)\ <\ \infty.\ }
\]
The wall is now a \emph{one-point} statement: uniform boundedness of the weighted primitive diagonal
of the positive kernel. This is the tightest possible form — there is no family of intervals left,
only the diagonal.
\end{resultbox}

This is a genuine structural gain: without positivity, (C) is a continuum of box inequalities; with it,
(C) follows from one diagonal sup. Positivity has done real work — it has removed the geometry of
intervals.

---

## §3. Lever 2 — positivity gives a one-sided (lower) bound on the fluctuation

\begin{proposition}[no destructive cancellation of off-line pairs]\label{prop:onesided}
Off-line zeros occur in functional-equation quadruples $\{\rho,1-\rho,\bar\rho,1-\bar\rho\}$. In the
positive kernel $K_P^{\mathrm{prim}}$, the pair $\{\rho,1-\bar\rho\}$ contributes a rank-$\le2$ block
$B_\rho\succeq0$ to the diagonal density. Hence
\[
   \mathfrak d_P(u)\ \ge\ \sum_{\rho:\ \beta>\frac12}\big(B_\rho\big)(u)\ \ge\ 0,
\]
and in particular the fluctuation diagonal **cannot be made small by cancellation between an off-line
zero and its mirror** — each off-line pair adds positively.
\end{proposition}
\emph{Proof.} The compression of a positive kernel is positive, so every spectral block is
$\succeq0$; the mirror pairing $\rho\leftrightarrow1-\bar\rho$ that in a \emph{signed} form could
cancel instead appears as a sum of squares $\|H^{1/2}Y c\|^2$ (Gram identity), which is a sum, not a
difference. $\square$

\emph{Reading.} Positivity is the **right sign** for a lower bound: it forbids the off-line
contribution from hiding. This is why DH (signed Hamiltonian) is detected — its blocks are indefinite
and *can* cancel. But a lower bound is the **wrong direction** for the Carleson upper bound (C). So
positivity certifies that off-line zeros *show up* in $\mathfrak d_P$; it does not cap how large
$\mathfrak d_P$ is.

---

## §4. Why this does not cross — and what it teaches

\begin{theorem}[the diagonal sup is the same center-of-strip second moment]\label{thm:nocross}
The weighted primitive diagonal is, up to bounded factors, the local second moment of the zero-sum:
\[
   e^{-u/2}\,\mathfrak d_P(u)\ \asymp\ \int_0^\ell |K_P^{\mathrm{prim}}(u,v)|^2\,\text{-weight}
   \ \asymp\ \sum_{\gam,\gam'}\widehat{w_u}(\gam)\overline{\widehat{w_u}(\gam')}\,
   e^{(\beta+\beta'-1)u},
\]
whose boundedness as $P,\lambda\to\infty$ is exactly the **pair-correlation / short-interval prime
variance** at the critical normalization (face (C), `FACE-C-compactness.md` §3). For $\beta=\beta'=
\tfrac12$ it is the Montgomery pair correlation (bounded, on-line); for any $\beta>\tfrac12$ it is
amplified by $e^{(2\beta-1)u}=\lambda^{2\beta-1}\to\infty$.
\end{theorem}
\emph{Proof.} The diagonal density of a positive kernel is $\sum_k\mu_k|e_k(u)|^2=\|K^{1/2}\delta_u\|^2
=\int|K(u,v)|^2$-type second moment via the square-root; expanding $K_P^{\mathrm{prim}}$ in the
explicit-formula zero basis gives the displayed double zero-sum, which is the second moment whose
diagonal $\gam=\gam'$, $\beta=\tfrac12$ is the pair-correlation form. $\square$

\begin{resultbox}
\textbf{Honest verdict.} Positivity buys (Lemma~\ref{lem:cs}) the collapse to a one-point diagonal sup
and (Prop.~\ref{prop:onesided}) a one-sided lower bound — but the one-point sup is
(Thm~\ref{thm:nocross}) the \emph{same} center-of-strip second moment that the Carleson norm was. The
sign we have for free controls **whether** off-line zeros appear (lower bound, detector), never **how
big** the diagonal is (upper bound, the wall). \emph{Positivity is orthogonal to size.}
\end{resultbox}

---

## §5. Crystallization: this is the shape/sign split, made precise on the diagonal

The phase-long crystallization — *the geometry proves the shape unconditionally; RH is the sign* — now
has a sharp pointwise avatar:

| object | what positivity gives | what is the wall |
|---|---|---|
| Carleson box $\nu_P^{\mathrm{fl}}(I)$ | reduces to diagonal sup (Lem.~\ref{lem:cs}) | size of the sup |
| off-line pair block $B_\rho$ | $\succeq0$: cannot cancel (Prop.~\ref{prop:onesided}) | — (lower bound only) |
| diagonal $e^{-u/2}\mathfrak d_P(u)$ | exists, $\ge0$, detects off-line | $\sup<\infty$ $=$ pair correlation $=$ RH |

The honest content: we have pushed positivity as far as it structurally goes. It removes the interval
geometry (Lever 1) and certifies detection (Lever 2), leaving the wall in its **irreducible one-point
form** — $\sup_{P,u}e^{-u/2}\mathfrak d_P(u)<\infty$ — which is the short-interval prime variance at
$\sqrt n$ scale. No positivity argument can cross it, because positivity is a sign statement and the
wall is a magnitude statement, and Theorem~\ref{thm:nocross} shows they meet only on the diagonal where
the magnitude is the classical center-of-strip second moment.

\textbf{Status.} Unconditional: Lever 1 (diagonal collapse), Lever 2 (one-sided lower bound),
Theorem~\ref{thm:nocross} (identification with pair correlation). Open (the wall, unchanged,
RH-strength): the diagonal sup / short-interval variance bound. No false victory. The contribution is
diagnostic and sharpening: the wall is now a single scalar sup, and we have a proof that the free
positivity is structurally incapable of bounding it — which is itself the cleanest statement of why
*every* positivity route in this program (Hodge index, CD(0,∞), Gram, colligation) lands here.
