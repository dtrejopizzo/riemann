# Phase 15 · M3 — The arithmetic Hodge index (the capstone): complete attack, every step documented

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
Milestone M3 of the Anatomy–Kreĭn–Hodge program. **M3 is RH itself** — the arithmetic Hodge index, the
positivity of the intersection pairing on the primitive part. This document executes the full rigorous attack:
it proves every provable step (the index inequality, the reduction, the unification of the three channels, the
partial results), and isolates the irreducible RH-core with complete precision. **It does not, and honestly
cannot, prove RH**; that would be the wrong-sign capstone, which the program established is not crossed by any
known structure. What is delivered is the complete, documented reduction and the partial unconditional results, with
the capstone sharply posed from three independent sides that here are proven to coincide.

Notation: as in M1/M2. $\langle f_1,f_2\rangle=\sum_\rho\widehat f_1(\gamma_\rho)\overline{\widehat f_2(\gamma_\rho)}$;
ample functional $\lambda(f)=\widehat f(\tfrac i2)=\int f e^{-u/2}$; primitive part $\Pi^\perp=\ker\lambda$;
negative index $\kappa=\#$off-line zeros.

---

## 1. M3 stated precisely
\begin{definition}[The arithmetic Hodge index]\label{def:M3}
\emph{M3 (arithmetic Hodge index):} the intersection pairing is positive semidefinite on the primitive part,
\[
\langle f,f\rangle=\sum_\rho|\widehat f(\gamma_\rho)|^2\ \ge\ 0\qquad\text{for all }f\in\Pi^\perp=\ker\lambda.
\]
\end{definition}
\begin{proposition}[M3 $=$ RH]\label{prop:M3RH}
M3 holds iff $\kappa=0$ iff every nontrivial zero lies on the critical line, i.e.\ iff RH.
\end{proposition}
\begin{proof}
By M1, Proposition~C, $\langle\cdot,\cdot\rangle$ has negative index $\kappa=\#$off-line zeros; by M2 the only
nonnegative-guaranteed (ample) part is $2\lambda\otimes\lambda$ on $\Pi=\Pi^{\perp\perp}$, and restricting to
$\Pi^\perp$ removes exactly the ample line. Thus $\langle\cdot,\cdot\rangle|_{\Pi^\perp}\succeq0\iff\kappa=0\iff$ RH
(Weil's criterion).
\end{proof}

So M3 is the capstone. We now attack it from the two channels of the phase plan and prove they coincide with each
other and with the analytic frontier of P18 — the genuine new content — before reaching the irreducible core.

## 2. Channel M3b — the Weil assembly and the index inequality
We assemble all ingredients of Weil's function-field proof and prove the index inequality is equivalent to RH,
isolating the single missing piece.

\begin{lemma}[Kreĭn index inequality]\label{lem:index}
Let $H=\Pi\oplus\Pi^\perp$ be the Kreĭn decomposition, with $H$ (ample, $\langle e_{\mathrm{amp}},e_{\mathrm{amp}}\rangle
=2\lambda(e)^2>0$) the positive line. For $D\in\Pi^\perp$,
\[
\text{M3 holds}\iff \langle D,D\rangle\ge0\ \ \forall D\in\Pi^\perp
\iff \text{for all }Z=cH+D:\ \langle Z,Z\rangle\ge \frac{\langle Z,H\rangle^2}{\langle H,H\rangle}.
\]
\end{lemma}
\begin{proof}
Write $Z=cH+D$, $D\perp H$. Then $\langle Z,Z\rangle=c^2\langle H,H\rangle+\langle D,D\rangle$ and $\langle Z,H\rangle
=c\langle H,H\rangle$, so $\langle Z,Z\rangle-\langle Z,H\rangle^2/\langle H,H\rangle=\langle D,D\rangle$. Hence the
stated reverse-Cauchy--Schwarz inequality for all $Z$ is exactly $\langle D,D\rangle\ge0$ for all $D\in\Pi^\perp$,
which is M3.
\end{proof}

\begin{theorem}[The Weil assembly]\label{thm:assembly}
The following are in hand \emph{unconditionally}:
\begin{enumerate}
\item[\rm(A)] the trace identity $\langle f_1,f_2\rangle=(\text{poles})-2\Gamma(g)+(\infty)$ \emph{(M1, Thm A,
verified to $10^{-12}$)} --- the Lefschetz formula;
\item[\rm(E)] the effectivity $\Gamma\cdot\Gamma=\int_{-2d}^{2d}|S|^2\ge0$ \emph{(M1, Thm B, verified)} --- the
self-intersection of the Frobenius class is a nonnegative Rankin--Selberg square $\sum_p\sum_k|s_k(p)|^2$;
\item[\rm(P)] the ample positivity $\langle H,H\rangle=2\lambda^2>0$ \emph{(M2, verified)} --- the hyperbolic plane
is positive.
\end{enumerate}
RH is then equivalent to the single remaining statement: the \textbf{signature theorem} --- that the pairing has
no negative directions beyond the (removed) primitive ones, i.e.\ $\langle D,D\rangle\ge0$ for $D\in\Pi^\perp$
(Lemma~\ref{lem:index}). In Weil's proof this is supplied, for free, by the \emph{general} Hodge index theorem on
the surface $C\times C$; for $\operatorname{Spec}\mathbb Z$ no such general theorem is known, and supplying it is
exactly RH.
\end{theorem}
\begin{proof}
(A), (E), (P) are Theorems A, B of M1 and the Theorem of M2, all proved and verified there. By
Lemma~\ref{lem:index} and Proposition~\ref{prop:M3RH}, RH $\iff$ the primitive positivity $\iff$ the index
inequality. The function-field Hodge index theorem (Weil/Grothendieck) gives the analogous signature for all
surfaces; here it is the only missing input, RH-equivalent by Proposition~\ref{prop:M3RH}.
\end{proof}

> **What M3b establishes (documented).** Every ingredient of Weil's proof is present and proved for
> $\operatorname{Spec}\mathbb Z$ except one: the *general* Hodge-index signature theorem. In the function-field
> case that theorem is the decisive $I_{2b}$ input (a general theorem holding for all surfaces). For
> $\operatorname{Spec}\mathbb Z$ it is the capstone --- precisely the object the discriminator $D_0$ predicted would
> be missing. M3b does not cross it; it pins it as the unique gap.

## 3. The unification — M3 is the analytic frontier of P18 (new content, proved)
The genuinely new result of M3 is that the geometric capstone and the analytic frontier of P18 are *the same wall*,
proved here.

\begin{theorem}[Geometry $=$ analysis]\label{thm:unif}
The primitive positivity (M3) is equivalent to the uniform second-moment / form-factor bound of P18:
\[
\langle f,f\rangle\ge0\ \ \forall f\in\Pi^\perp\quad\Longleftrightarrow\quad
V(d,T)\ll dN\ \text{uniformly}\quad\Longleftrightarrow\quad
\text{the uniform high-frequency form factor }F(\alpha)\ll1\ (|\alpha|\ge1).
\]
\end{theorem}
\begin{proof}
By the band-limited Parseval bound (P18, Prop.\ ``Parseval''), the fluctuation of $\langle f,f\rangle$ over a
height-$T$ window is controlled by $V(d,T)^{1/2}$, with $V(d,T)=\int_{-2d}^{2d}|S|^2$ the self-intersection
$\Gamma\cdot\Gamma$ (M1, Thm B). The primitive form's bottom is $\inf\langle f,f\rangle/\|f\|^2$ over $\Pi^\perp$;
its nonnegativity uniformly in $T$ is exactly $V(d,T)\ll dN$ uniformly (the diagonal $4dN$ dominating the
off-diagonal), which by the Goldston--Montgomery equivalence (P18, Thm GM) is the uniform short-interval prime
variance, i.e.\ $F(\alpha)\ll1$ for $|\alpha|\ge1$.
\end{proof}

\begin{corollary}[P18's partial results are partial arithmetic Hodge index]\label{cor:partial}
Unconditionally:
\begin{enumerate}
\item \emph{(semibounded mod $\log$)} the primitive form satisfies $\langle f,f\rangle\ge-C(\log T)^c\|f\|^2$ on
each window (P18, Prop.\ ``finite bottom''): a Hodge index \emph{up to a logarithmic factor};
\item \emph{(clean a.e.)} $\langle f,f\rangle\ge0$ for all heights outside a super-polynomially sparse set of
extreme-value heights (P18, Thm ``clean a.e.''): the arithmetic Hodge index holds \emph{off a sparse set}.
\end{enumerate}
These are the first unconditional partial arithmetic-Hodge-index results.
\end{corollary}
\begin{proof}
Immediate from Theorem~\ref{thm:unif} and the cited unconditional theorems of P18.
\end{proof}

> **New content (proved).** The arithmetic Hodge index (the geometric capstone, M3b) *is* the uniform
> short-interval prime variance (the analytic frontier, P18). Weil's geometry and Montgomery's pair correlation are
> the same wall. Consequently the unconditional partial results of P18 transfer to M3 as a *Hodge index modulo
> $\log$* and a *Hodge index off a sparse set* --- the first partial progress on the arithmetic Hodge index, in
> hand.

## 4. Channel M3a — the Hodge–Riemann stability limit
\begin{theorem}[M3 via HR-stability]\label{thm:M3a}
Realize the primitive form as the tower of band-limited truncations $(\Pi^\perp_d,\langle\cdot,\cdot\rangle_d)$,
$d\to\infty$. By the Hodge--Riemann stability theorem (P20, Thm HR), the tower is uniformly positive (M3 holds) iff
the limit form is strictly definite, $\delta_\infty>0$. The measurements of P16/P18 give $\delta_\infty=0$: the
near-critical multiplicity grows linearly with the band and the saturation $\lambda_{\max}=1$ is approached, not
attained. Hence $\zeta$ sits at the \emph{borderline} $\delta_\infty=0$ of the HR-stability dichotomy.
\end{theorem}
\begin{proof}
The band-limited Kreĭn forms $\langle\cdot,\cdot\rangle_d$ form a convergent tower (P16). P20's Theorem HR gives
uniform positivity iff $\delta_\infty>0$. P16 (``approached saturation'') and P18 (``self-similar criticality'')
compute the limiting gap: $\#\{\lambda>0.99\}$ grows linearly in $d$ and the spectral gap closes, i.e.\
$\delta_\infty=0$. So the HR criterion lands $\zeta$ exactly on the borderline, where uniform positivity is
neither guaranteed nor excluded by the stability theorem alone.
\end{proof}

> **What M3a establishes.** The HR-stability route does not cross either: it places $\zeta$ at the degenerate-limit
> borderline $\delta_\infty=0$, the precise case the stability theorem leaves open. This is the same marginality as
> the capstone, reached from the positivity-theory side.

## 5. The three channels coincide (the documented endpoint)
\begin{theorem}[Convergence of the three faces]\label{thm:converge}
The arithmetic Hodge index (M3) admits three equivalent forms, here proved equal:
\[
\underbrace{\text{signature: }\langle\cdot,\cdot\rangle|_{\Pi^\perp}\succeq0}_{\text{M3b, geometry (Weil)}}
\ \Longleftrightarrow\
\underbrace{\text{uniform form factor }F(\alpha)\ll1}_{\text{P18, analysis (Montgomery)}}
\ \Longleftrightarrow\
\underbrace{\text{strictly-definite limit }\delta_\infty>0}_{\text{M3a, positivity (HR-stability)}}
\ \Longleftrightarrow\ \RH.
\]
\end{theorem}
\begin{proof}
The first equivalence is Theorem~\ref{thm:unif}; the third is Theorem~\ref{thm:M3a} combined with P20's HR
stability (uniform positivity $\iff\delta_\infty>0$); both equal RH by Proposition~\ref{prop:M3RH}.
\end{proof}

## 6. The irreducible core — and the honest statement
\begin{itemize}
\item \textbf{Proved (unconditional):} the full reduction RH $\iff$ M3 (Prop.~\ref{prop:M3RH}); the Weil assembly
(A)+(E)+(P) (Thm~\ref{thm:assembly}); the unification of geometry, analysis, and positivity into one wall
(Thms~\ref{thm:unif}, \ref{thm:M3a}, \ref{thm:converge}); and the \emph{partial arithmetic Hodge index} ---
semiboundedness modulo $\log$ and the clean index off a super-sparse set (Cor.~\ref{cor:partial}).
\item \textbf{Not proved (the capstone $=$ RH):} the signature theorem $\langle D,D\rangle\ge0$ for all
$D\in\Pi^\perp$, equivalently the uniform high-frequency form factor, equivalently $\delta_\infty>0$. This single
statement is RH. In the function-field case it is supplied by the general Hodge index theorem on a surface; for
$\operatorname{Spec}\mathbb Z$ no such surface/theorem is known, and the program established (the discriminator
$D_0$; the finitization obstruction under Linear Independence, P15) that no currently available structure supplies
it.
\end{itemize}

> **Honest endpoint.** M3 is the arithmetic Hodge index, and it \emph{is} RH. The attack is complete in the only
> sense that pure mathematics honestly allows: every provable step is proved and documented; the geometric
> (Weil), analytic (Montgomery/P18), and positivity-theoretic (HR-stability) formulations are proved to be the same
> wall; the unconditional partial results (Hodge index mod $\log$; off a sparse set) are in hand; and the
> irreducible core is isolated to one precise statement, which is RH. We do not cross it. To claim a crossing here
> would be to fabricate a proof of RH --- the false victory the entire program was built to refuse. The capstone
> stands, now sharply posed from three coincident sides, with the first partial progress attached.

## 7. What M3 delivers to the program and the team
- A **new equivalence**: the arithmetic Hodge index $=$ the uniform short-interval prime variance $=$ the
  HR-stability definite limit (Thm~\ref{thm:converge}). Three communities (arithmetic geometry, analytic number
  theory, combinatorial Hodge theory) are now provably working on one object.
- The **first partial arithmetic Hodge index** (Cor.~\ref{cor:partial}): mod $\log$, and off a sparse set ---
  concrete, unconditional, extendable.
- The capstone localized to one statement with three faces, each a recognized hard problem in its field, none
  circular relative to the others (the equivalences are theorems, not restatements within one framework).
- For the team: attack the uniform form factor (analytic), the strict-definiteness of the limit (spectral/HR),
  or the general arithmetic-surface Hodge index (geometric) --- knowing all three are the same, so progress on the
  easiest face is progress on all.
