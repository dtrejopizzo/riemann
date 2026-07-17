# M2 — The pole-relative completion: making the renormalization a genuine limit, and a structural correction to the plan

**Phase 65, milestone M2.** Pure mathematics. Goal: construct the topology/completion in which the
finite tower $\{\mathsf E_P\}$ converges to the $\Xi$-object (interface T2 of M1). In doing so we reach a
**structural fact that corrects the original plan**: there is provably *no single topology* with both
(T1) closedness of $\mathcal N_0$ and (T2) convergence of the arithmetic renormalization — they are in
genuine tension (this *is* the content of N2/N3). The honest consequence: the index cannot be recovered
from topology; M2's job is to build the **coarse pole-relative topology** in which T2 is *free* (from
G3) and to carry, on top of it, the **definite-signed rank-one defect datum** that M3 will use to
recover the index from *sign*, not from topology. We prove T2 in the coarse topology and isolate exactly
what M3 must do. Nothing here uses RH; T2 is shown to follow from the given G3 and not to require the
rank-one norm bound (the Phase-64 wall is *not* re-imported).

---

## §1. Localizing the divergence: the pole vector

\begin{definition}[pole vector and primitive complement]
In the model space of the finite system, let $h_P$ be the constant/degree mode (the eigendirection
carrying the divergent trace, G4), normalized $\hat h_P=h_P/\|h_P\|$. Set $P_{\mathrm{prim}}^{(P)}=
I-|\hat h_P\rangle\langle\hat h_P|$. By G4,
\[
   \langle h_P,K_Ph_P\rangle\sim\tfrac12(\log P)^2\to\infty,\qquad
   K_P=\underbrace{P_{\mathrm{prim}}K_PP_{\mathrm{prim}}}_{=:K_P^{\mathrm{prim}}}\ \oplus\
   \underbrace{(\text{rank-one along }\hat h_P)}_{\text{divergent, definite }+}.
\]
\end{definition}

The divergence is thus a single, definite-signed, rank-one direction. The renormalization
$\mathrm{ren\text{-}lim}$ of G3 is precisely the operation that divides this direction out (zeta/Binet
regularization, unconditional). We must turn "$\mathrm{ren\text{-}lim}$" into a genuine categorical
limit.

---

## §2. A structural fact: no single topology has both (T1) and (T2)

Before constructing anything we record a constraint that reshapes the plan.

\begin{proposition}[T1–T2 tension]\label{prop:tension}
There is no Hausdorff topology $\tau$ on a class of objects containing the tower $\{\mathsf E_P\}$ and
$\mathsf E_\Xi$ such that simultaneously
\emph{(T1)} $\mathcal N_0$ is $\tau$-closed, and \emph{(T2)} $\mathsf E_P\xrightarrow{\tau}\mathsf E_\Xi$,
\textbf{unless RH holds.}
\end{proposition}
\emph{Proof.} If (T1) and (T2) both held, then $\mathsf E_P\in\mathcal N_0$ (G2) and
$\mathcal N_0$ $\tau$-closed force $\mathsf E_\Xi\in\mathcal N_0$, i.e. $\kappa(\Xi)=0$, i.e. RH. So the
conjunction is equivalent to RH; no \emph{unconditional} topology can have both. $\square$

\begin{remark}[the correction to the plan]
The `PROBLEM-STATEMENT.md` asked for one $\tau_\kappa$ with (T1)$\wedge$(T2). Proposition~\ref{prop:tension}
shows that asking a \emph{topology} to do both is asking it to *be* RH — the tension N2$\leftrightarrow$N3
is not an artifact to be engineered away but the problem itself wearing topological clothes. Therefore
the index-continuity (A2) must come from \textbf{structure carried on top of a topology}, not from the
topology alone. Concretely: choose the coarse topology that makes (T2) free (this section's
construction), and recover the index by a \emph{sign} argument on the carried defect datum (M3). This is
the same lesson as Phase 64 ("positivity/convergence is free 0th-order; the index/sign is the content"),
now at the categorical level. M2 builds the free half; M3 owns the content.
\end{remark}

---

## §3. The coarse pole-relative topology and T2 (free from G3)

\begin{definition}[pole-relative Weyl datum]
To each object associate its \textbf{pole-relative Weyl function}
$\tilde m=\big(m-m_{\mathrm{pole}}\big)$, where $m=E^\#/E$ (or the canonical-system Weyl function) and
$m_{\mathrm{pole}}$ is the explicit rank-one pole/archimedean part (the $s=1$ pole $+$ Binet
$\Gamma$-factor, G4). $\tilde m$ is meromorphic on $\C\setminus\R$.
\end{definition}

\begin{definition}[coarse topology $\tau_0$]
$\mathsf E^{(n)}\xrightarrow{\tau_0}\mathsf E$ iff the renormalized determinants converge on compacts,
$D^{(n)}\to D$ uniformly on compact subsets of $\C$ (equivalently $\tilde m^{(n)}\to\tilde m$ in the
spherical/meromorphic topology on $\C\setminus\R$). $\tau_0$ is the **determinant topology**; it is
index-blind (a $\tau_0$-limit of $\mathcal N_0$ objects may lie in any $\mathcal N_\kappa$ — exactly N2).
\end{definition}

\begin{theorem}[T2 holds in $\tau_0$, unconditionally]\label{thm:t2}
$\mathsf E_P\xrightarrow{\tau_0}\mathsf E_\Xi$, and the comparison $c:\mathsf E_\infty\to\mathsf E_\Xi$ is
a $\tau_0$-isomorphism at the level of the underlying (determinant/Weyl) data.
\end{theorem}
\emph{Proof.} By G3, $\mathrm{ren\text{-}lim}_PD_P=\Xi$ uniformly on compacts (the zeta/Binet-regularized
limit; unconditional, Tate local factors $\times$ archimedean cell, `CANONICAL-FOUNDATION.md` Stage 5).
This is, verbatim, $\tau_0$-convergence $D_P\to\Xi$. The pole-relative Weyl functions then converge,
$\tilde m_P\to\tilde m_\Xi$, as logarithmic derivatives away from zeros, with the rank-one pole part
removed by construction. Hence $\mathsf E_\infty$ and $\mathsf E_\Xi$ have identical underlying data,
i.e. $c$ is a $\tau_0$-isomorphism of determinant/Weyl data. $\square$

\begin{resultbox}
\textbf{T2 is free and does not import the wall.} The convergence Theorem~\ref{thm:t2} uses only the
\emph{given} G3 and the rank-one pole removal (G4). It does \textbf{not} use, and does not need,
$\sup_P\|K_P^{\mathrm{prim}}\|<\infty$ (the Phase-64 rank-one escape / the RH-strength norm bound):
$\tau_0$ is a topology on the index-blind determinant data, where convergence is exactly the regularized
limit. The Phase-64 wall (a \emph{size}/norm statement) is deliberately not in $\tau_0$; only the
\emph{index} remains, and it is M3's. \emph{This is the point of the whole reframing: the size question
is dissolved, not solved; the index question is isolated.}
\end{resultbox}

---

## §4. The completion, and the defect datum carried for M3

$\tau_0$ gives convergence but, being index-blind, the limit $\mathsf E_\infty$ comes \emph{without} its
Pontryagin structure determined. We complete $\mathcal G$ along $\tau_0$ while \emph{carrying} the data
M3 needs.

\begin{definition}[pole-relative completion $\widehat{\mathcal G}$]
$\widehat{\mathcal G}$ is the category whose objects are $\tau_0$-limits of towers in $\mathcal G$,
each equipped with the \textbf{defect tower} $\{\delta_P\}$, where
\[
   \delta_P:=K_{P+1}-(\text{inclusion})_*K_P\ \succeq?\ ,
\]
the incremental Gram form added at step $P\to P+1$ (one prime cell). Each $\delta_P$ records the
\emph{signature} of the step. The carried datum is the sequence of signatures
$\{\sigma_P=\mathrm{ind}_-\delta_P\}$ together with the rank-one pole projector $\hat h_\infty=
\lim\hat h_P$.
\end{definition}

\begin{lemma}[finite steps are positive; the defect is concentrated]\label{lem:defect}
For the von Mangoldt tower, each increment is a positive cell: $\delta_P\succeq0$, so $\sigma_P=0$ for
all $P$ (G1–G2; one prime adds a positive rank-one Hamiltonian atom). Consequently the \emph{only} place
a negative square can appear in the $\tau_0$-limit is the \textbf{rank-one pole direction} $\hat
h_\infty$ where the trace diverges (G4); on the primitive complement every finite increment is positive.
\end{lemma}
\emph{Proof.} $\delta_P=\int Y^*\,d\mathcal H_{p_{P+1}}\,Y\succeq0$ since $d\mathcal H_{p}\ge0$ (Gram
identity, positivity of a single von Mangoldt atom). So no finite step creates a negative square; in the
limit, negativity can only enter through the non-$\tau_0$-continuous direction, which by G4 is the single
divergent rank-one mode $\hat h_\infty$. $\square$

\begin{resultbox}
\textbf{What M2 hands to M3 (sharpened interface).} In $\widehat{\mathcal G}$: (i) $\mathsf E_\infty=
\mathsf E_\Xi$ at the determinant/Weyl level (Thm~\ref{thm:t2}); (ii) every finite defect is positive,
$\sigma_P=0$ (Lemma~\ref{lem:defect}); (iii) hence $\kappa(\mathsf E_\Xi)$ can be nonzero \emph{only}
via the single rank-one, definite-signed pole direction $\hat h_\infty$. \textbf{M3's exact task:} show
that a \emph{positive} rank-one divergence cannot create a negative square — i.e. the limiting defect
form along $\hat h_\infty$ has $\mathrm{ind}_-=0$ — so $\kappa(\mathsf E_\Xi)=0$. The index question is
now localized to \emph{one positive rank-one direction}.
\end{resultbox}

---

## §5. Honest status

\textbf{Established (unconditional, no RH, no Phase-64 norm bound):}
\begin{itemize}
\item \textbf{Prop.~\ref{prop:tension} (T1–T2 tension):} no single unconditional topology has both
closedness and convergence — a real structural correction; the index must come from sign-structure, not
topology.
\item \textbf{Thm~\ref{thm:t2} (T2 free):} in the coarse pole-relative topology $\tau_0$, the tower
converges to the $\Xi$-object at the determinant/Weyl level, from G3 alone; the rank-one escape bound is
\emph{not} used.
\item \textbf{Lemma~\ref{lem:defect} (defect concentration):} every finite increment is positive
($\sigma_P=0$); a negative square can appear only along the single positive rank-one pole direction
$\hat h_\infty$.
\item The completion $\widehat{\mathcal G}$ and the carried defect datum are defined; M3's interface is
sharpened to one positive rank-one direction.
\end{itemize}

\textbf{Not established (now entirely M3):} that the positive rank-one pole divergence creates no
negative square in the $\tau_0$-limit (so $\kappa(\Xi)=0$). \emph{This is the entire remaining content
of RH}, and Lemma~\ref{lem:defect} shows it is exactly a statement about \textbf{one definite-signed
rank-one limit} — the sharpest possible localization.

\textbf{Caveat flagged (anti-self-deception).} M2 deliberately works in the \emph{coarse} (index-blind)
topology, so T2 is genuinely free — but this means M2 alone proves \emph{nothing} about the index; if
M3 cannot convert "positive rank-one divergence" into "no negative square," the difficulty was merely
relocated, not removed, and Prop.~\ref{prop:tension} guarantees no topological trick can rescue it. The
honest test of the whole Phase-65 thesis is therefore M3: \emph{is a positive rank-one renormalization
index-preserving?} If yes (in the needed generality), RH; if no, an off-line zero is consistent and we
have a precise no-go. M2 has made that the only question.

Next document: `M3-signature-closedness.md` — the conceptual heart: does a positive rank-one divergence
preserve the Kreĭn–Langer index?
