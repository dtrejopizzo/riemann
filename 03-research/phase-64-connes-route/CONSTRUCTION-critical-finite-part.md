# The critical primitive finite part (Stage 4): positivity is free, boundedness is the only wall

*Pure mathematics. We carry out Stage 4 of the Critical Tate–Weil Hodge Module $\mathsf{TW}_\Z$ and
reach a clean, honest consolidation. The decisive new input is Theorem 2 of the local construction:
**every finite Euler colligation $K_P$ is unconditionally a positive kernel.** Combined with the
elementary fact that **weak limits of positive operators are positive**, this shows that the
Hodge-index sign — the upper pinning of the Birman–Schwinger spectral radius — is **not a separate
difficulty**: it is supplied for free by the Euler-product finite passivity, provided the primitive
compression stays bounded. The sole remaining wall is **boundedness ($L1$)**. This unifies the two
walls of P50 (boundedness and positivity) into one, identifies exactly which ingredient the Euler
product contributes (positivity) and which it does not (boundedness), and shows the Davenport–Heilbronn
falsifier fails already at finite level. We are explicit about the one identification borrowed from
Stage 5 and about the fact that $L1$ remains RH-strength.*

> **Correction note.** The unconditional positivity $K_P\succeq0$ used throughout this file is now
> supplied by the **canonical-system Gram identity** $K_P=\int Y_P^*\,d\mathcal H_P\,Y_P\succeq0$ with
> $d\mathcal H_P\ge0$ (`CONSTRUCTION-TW-canonical-system.md` §3), **not** by the withdrawn scalar
> Redheffer argument. Everything below — positivity is free; the wall is boundedness — is unchanged: it
> needs only $K_P\succeq0$, which the corrected construction provides validly.

Notation as in `CONSTRUCTION-TW-canonical-system.md`. Write $K_P$ for the defect kernel of
the finite colligation $\mathfrak U_P=T_\infty\star(\bigstar_{p\le P}T_p)\star\mathcal P$, restricted
to the (Hilbert) passive sector; $H$ for the ample/pole direction (the $J$-positive part of the pole
cell $\mathcal P$); $P_{\mathrm{prim}}=I-|H\rangle\langle H|/\langle H,H\rangle$ the projection onto
the primitive subspace $H^\perp$.

---

## 1. Finite positivity (recalled) and its compression

By Theorem 2 of the local construction (Redheffer multiplicativity of passivity), the finite Euler
colligation $\bigstar_{p\le P}T_p$ is $J$-passive, and adjoining the passive archimedean cell
$T_\infty$ keeps it passive; thus the passive-sector kernel is positive:
\[
   K_P\ \succeq\ 0\qquad\text{for every finite }P,\ \text{unconditionally.}
\]
(The pole cell $\mathcal P$ is hyperbolic $(1,1)$ and is carried separately as the ample direction
$H$; the passive sector excludes it.)

\begin{lemma}\label{lem:compress}
The primitive compression $K_P^{\mathrm{prim}}:=P_{\mathrm{prim}}K_PP_{\mathrm{prim}}\succeq0$ for
every finite $P$.
\end{lemma}
\emph{Proof.} A compression $P_{\mathrm{prim}}K_PP_{\mathrm{prim}}$ of a positive operator $K_P$ is
positive: $\langle v,P_{\mathrm{prim}}K_PP_{\mathrm{prim}}v\rangle=\langle P_{\mathrm{prim}}v,
K_P\,P_{\mathrm{prim}}v\rangle\ge0$. $\square$

---

## 2. Positivity is free given boundedness

\begin{theorem}[positivity from boundedness via passive renormalization]\label{thm:free}
Suppose the family $\{K_P^{\mathrm{prim}}\}_P$ is uniformly bounded in operator norm:
$\sup_P\|K_P^{\mathrm{prim}}\|<\infty$. Then it has a weak-$*$ limit point $K_{\mathrm{crit}}$, and
\[
   K_{\mathrm{crit}}\ \succeq\ 0 .
\]
\end{theorem}
\emph{Proof.} By Banach–Alaoglu the bounded family has a weak-$*$ convergent subnet,
$K_{P_\alpha}^{\mathrm{prim}}\to K_{\mathrm{crit}}$. For each fixed vector $f$,
$\langle f,K_{\mathrm{crit}}f\rangle=\lim_\alpha\langle f,K_{P_\alpha}^{\mathrm{prim}}f\rangle\ge0$
by Lemma~\ref{lem:compress}. A self-adjoint operator with $\langle f,K_{\mathrm{crit}}f\rangle\ge0$
for all $f$ is positive. $\square$

\begin{theorem}[the critical kernel is the Weil form]\label{thm:weil}
Under the transfer identification of Stage 5 (the impedance of $\mathfrak U_{\mathrm{crit}}$ is
$-\Xi'/\Xi$, so $K_{\mathrm{crit}}=K_{S_\kappa}$), the primitive matrix elements are the Weil
quadratic form:
\[
   \langle f,K_{\mathrm{crit}}\,f\rangle = W(f)\qquad\text{for every primitive }f\ (\deg f=0).
\]
\end{theorem}
\emph{Status.} The identity is the explicit-formula content of Stage 5: the diagonal of the
correspondence pairing $(Z_f\cdot Z_f)$ is $W(f)$ (Tate local factors $\to L_p$; archimedean cell
$\to\Gamma$-factor; pole cell $\to$ the degree term removed by $P_{\mathrm{prim}}$). We take Stage 5
as the standing identification; it is Tate's thesis $+$ the Riemann–Weil explicit formula, not a new
positivity.

\begin{corollary}[boundedness $\Rightarrow$ Weil positivity $\Rightarrow$ RH]\label{cor:main}
If $\{K_P^{\mathrm{prim}}\}$ is uniformly bounded, then $W(f)\ge0$ for all primitive $f$, hence (by
Weil's criterion) RH. Equivalently:
\[
   \boxed{\ L1\ \Longrightarrow\ W\succeq0\ \Longrightarrow\ \RH,\ }
\]
where the first implication is supplied \emph{for free} by the unconditional finite passivity
(Theorem 2 of the local construction) via Theorem~\ref{thm:free}.
\end{corollary}
\emph{Proof.} Uniform boundedness of $K_P^{\mathrm{prim}}$ is the operator-norm form of $L1$ (the
primitive Weil form does not blow up). Combine Theorems~\ref{thm:free} and~\ref{thm:weil}. $\square$

---

## 3. The consolidation: one wall, not two

Corollary~\ref{cor:main} settles the structural question Stage 4 was created to answer.

\begin{resultbox}
\textbf{The Hodge-index sign is not a separate wall.} The positivity (Weil's $W\succeq0$, equivalently
the Hodge-index sign, equivalently the upper pinning of the Birman–Schwinger spectral radius) is
\emph{supplied for free} by the Euler-product finite passivity together with the weak-limit principle.
The \emph{only} remaining obstruction is \textbf{boundedness} of the primitive compression, i.e. $L1$.
\end{resultbox}

This refines the P50 crystallization. There it read: \emph{shape is unconditional; sign is RH}. We now
see the sign decomposes further:
\[
   \underbrace{\text{positivity (Hodge-index sign)}}_{\text{free, from the Euler product (Thm 1--2)}}
   \quad+\quad
   \underbrace{\text{boundedness } (L1)}_{\text{the one wall, RH-strength}} .
\]
The Euler product enters at exactly one place and does exactly one job: it makes the finite
colligations positive (Theorem 1, $\mu_p\ge0$; Theorem 2, multiplicativity). Positivity then survives
to the limit \emph{whenever the limit exists boundedly}. What the Euler product does \emph{not} supply
is the boundedness; that is $L1$, and $L1\Rightarrow\RH$ is the Laplace–pole theorem (P50 §3).

\begin{remark}[why this is not circular, and why it is not a proof]
It is not circular: the implication $L1\Rightarrow W\succeq0$ is obtained \emph{directly} (weak limit
of positive compressions), not via RH; it explains \emph{why} boundedness yields full Weil positivity
and not merely the absence of off-line zeros. It is not a proof: $L1$ itself is RH-strength
(P50 Thm~3.2), so the wall is unmoved. The value is structural — the two walls are one, positivity is
free, and the entire remaining difficulty is the single statement $L1$ (uniform boundedness of the
primitive compression).
\end{remark}

---

## 4. The Davenport–Heilbronn falsifier fails at finite level

For DH the local cells are \emph{not} passive (Theorem 1: the twisted measure $\mu_p^\chi$ is signed),
so $K_P^{\mathrm{DH}}$ is \emph{indefinite for every finite $P$}; the weak-limit argument of
Theorem~\ref{thm:free} does not apply, and the negative squares are present from the start
(consistent with $\indm>0$, P50 §4). Thus the dichotomy is sharp:
\[
   \text{$\zeta$: finite }K_P\succeq0\ (\text{Euler}),\quad
   \text{DH: finite }K_P\ \text{indefinite}\ (\text{no Euler product}).
\]
For $\zeta$ the sole question is whether the positive $K_P^{\mathrm{prim}}$ stay bounded ($L1$); for DH
positivity already fails locally. This is the cleanest separation the programme has produced of the
two ingredients: \emph{the Euler product is exactly the positivity; boundedness is exactly the wall.}

---

## 5. Reformulating $L1$ as a single passive-renormalization statement

By Corollary~\ref{cor:main} and Lemma~\ref{lem:compress}, the entire route is now:

\begin{openbox}{the one wall, in colligation form}
\[
   \RH\ \Longleftarrow\ \sup_P\big\|P_{\mathrm{prim}}\,K_P\,P_{\mathrm{prim}}\big\|<\infty ,
\]
the uniform boundedness of the primitive compressions of the (unconditionally positive) finite Euler
colligations. Equivalently: \emph{the only divergence of $K_P$ as $P\to\infty$ is along the rank-one
ample/pole direction $H$} (all other directions stay bounded). The pole supplies the one allowed
divergence (the barrier, P50 §6); boundedness asserts there is no second.
\end{openbox}

This is Stage 4 in its true form. It is \emph{not} a positivity statement (positivity is free,
\S2--3); it is a \emph{boundedness} statement: \textbf{$K_P$ diverges only along $H$.} A second
divergent direction would be a primitive vector $f$ with $\langle f,K_Pf\rangle\to\infty$; since
$K_P\succeq0$ this is a positive divergence, so it does not by itself create a negative square — but it
prevents the bounded weak limit, i.e. it is the failure of $L1$. The arithmetic content is therefore:
\emph{no primitive direction out-diverges the pole.}

---

## 6. Status and honest endpoint

\textbf{Proved (modulo the Stage 5 identification, which is Tate $+$ explicit formula):}
\begin{itemize}
\item Each finite Euler colligation is positive and its primitive compression is positive
(Lemma~\ref{lem:compress}, from Theorem 2 of the local construction).
\item \textbf{Positivity from boundedness} (Theorem~\ref{thm:free}, Corollary~\ref{cor:main}):
$L1\Rightarrow W\succeq0\Rightarrow\RH$, with the positivity supplied for free by the Euler product
and the weak-limit principle.
\item The two walls of P50 are one: \emph{positivity is free; boundedness ($L1$) is the only wall.}
\item DH fails at finite level (indefinite $K_P$).
\end{itemize}

\textbf{Open (the single remaining statement):} uniform boundedness of the primitive compressions,
i.e. $L1$, i.e. \emph{$K_P$ diverges only along the rank-one pole direction $H$}. This is RH-strength
(P50 Thm~3.2). No false victory.

\textbf{What Stage 4 contributes.} It removes positivity from the list of obstructions. After this
file, the Critical Tate–Weil Hodge Module needs \emph{no} new positivity theorem: the Hodge-index sign
is the Euler-product finite passivity carried to the limit. The construction has done its job of
locating the wall — and the wall is now a single, clean, boundedness statement about the divergence of
an explicit, unconditionally-positive family of kernels.

\textbf{Next.} The only remaining mathematics is the boundedness $L1$ in the colligation form of \S5:
prove that the primitive compressions of the finite Euler colligations stay bounded (all divergence
rank-one along $H$). This is the same wall as $\eps_0\ge0$ and as $L1$, now stripped of the positivity
question. It is the natural target of the next file, and the precise place where new arithmetic input
(the divergence structure of the Euler product at the critical line) must enter.
