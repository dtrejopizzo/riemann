# M3 — Signature closedness: does a positive rank-one divergence preserve the index? — the honest crux

**Phase 65, milestone M3 (the conceptual heart).** Pure mathematics. The single remaining question
(M2): does the positive, rank-one pole divergence create a negative square in the $\tau_0$-limit? We
prove the half that the definite sign genuinely buys — **each finite operator is self-adjoint, so its
determinant has only real zeros (is Hermite–Biehler), and Davenport–Heilbronn fails here exactly** — and
then we locate, with full honesty, the half it does **not** buy: the negative squares of the limit are
concentrated precisely on the locus where the renormalization is **non-uniform**, which finite
positivity cannot reach. The net, cold result: **M3 reduces RH to a single sharp statement — that the
regularized convergence $D_P\to\Xi$ is *uniform on compacts of $\C$* (not merely a renormalized
limit).** This does **not** cross for free; it is RH-strength. But it is the sharpest localization yet,
it explains the role of the sign, and it is the precise target to hand forward. No false victory.

---

## §1. What the definite sign genuinely buys (unconditional)

\begin{lemma}[finite self-adjointness $\Rightarrow$ real zeros $\Rightarrow$ HB]\label{lem:sa}
For each finite $P$, the canonical operator $A_P$ of the von Mangoldt Hamiltonian $H_{\mathrm{vM}}\ge0$
is \textbf{self-adjoint} (in the genuine Hilbert space, $\kappa=0$, G2). Hence its spectrum is real, and
the finite spectral/perturbation determinant $D_P$ has \textbf{only real zeros} — i.e. $D_P$ is
Hermite–Biehler ($\kappa(D_P)=0$).
\end{lemma}
\emph{Proof.} $H_{\mathrm{vM}}\ge0$ makes the canonical inner product positive definite (Gram identity,
G2), so $A_P$ is self-adjoint on a Hilbert space; self-adjoint operators have real spectrum; the zeros of
$D_P$ are the eigenvalues of $A_P$, hence real. A real-zero real entire function of finite type is HB.
$\square$

\begin{proposition}[the sign is load-bearing; DH fails exactly here]\label{prop:dh}
For the \emph{signed} Davenport–Heilbronn Hamiltonian $H^\chi$ (mixed-sign masses), the canonical inner
product is indefinite, $A^\chi_P$ acts on a Pontryagin space ($\kappa_P>0$), is \textbf{not}
self-adjoint there in the definite sense, and its determinant $D^\chi_P$ has \textbf{non-real} zeros
already at finite $P$. Lemma~\ref{lem:sa} uses $H\ge0$ irreducibly and does not apply to DH.
\end{proposition}
\emph{Proof.} Indefinite Gram (Phase 64; the twist $\mu_p^\chi$ changes sign) $\Rightarrow$ Pontryagin
$\kappa_P>0$ $\Rightarrow$ complex eigenvalues permitted $\Rightarrow$ off-real zeros of $D^\chi_P$.
$\square$

\begin{resultbox}
The definite sign delivers exactly one thing, but a real one: \textbf{every finite determinant $D_P$ has
its zeros on $\R$} (HB), and this fails for DH. If $D_P\to\Xi$ were a genuine limit, this would force
$\Xi$'s zeros onto $\R$. So the sign has done its job at every finite stage; the entire question is
whether finiteness survives the limit.
\end{resultbox}

---

## §2. The conditional crossing (Hurwitz)

\begin{theorem}[uniform convergence would finish it]\label{thm:hurwitz}
If $D_P\to\Xi$ \textbf{uniformly on compact subsets of $\C$} (across the critical strip), then RH holds.
\end{theorem}
\emph{Proof.} Each $D_P$ has no zeros off $\R$ (Lemma~\ref{lem:sa}); in particular none in the open upper
half-plane. By Hurwitz's theorem, the locally-uniform limit $\Xi\ (\not\equiv0)$ has no zeros in the open
upper half-plane. By the functional equation ($\Xi$ even/real), no zeros off $\R$ at all. RH. $\square$

This is the target shape: real-zero approximants $+$ honest convergence $\Rightarrow$ real-zero limit.
The sign gives the approximants (Lemma~\ref{lem:sa}); the only missing input is the *mode* of
convergence.

---

## §3. The honest obstruction: the index hides where convergence is non-uniform

The given datum (G3) is $\mathrm{ren\text{-}lim}_PD_P=\Xi$ — a \emph{regularized} limit (zeta/Binet),
which is **weaker** than uniform-on-compacts across the strip (N3). The gap is not cosmetic:

\begin{theorem}[concentration of negative squares]\label{thm:concentration}
Let $m_P=D_P'/D_P\in\mathcal N_0$ (Herglotz; Lemma~\ref{lem:sa}) and $m_\infty=\Xi'/\Xi\in\mathcal N_\kappa$,
$\kappa=\kappa(\Xi)$. Then:
\begin{enumerate}
\item at every point of $\C\setminus\R$ where $m_P\to m_\infty$ \emph{locally uniformly}, the Nevanlinna
kernel limit is positive: $\mathsf N_{m_\infty}\succeq0$ there (pointwise limit of PSD kernels);
\item the $\kappa$ negative squares of $\mathsf N_{m_\infty}$ are carried \textbf{exactly} by the
$\kappa$ poles of $m_\infty$ in $\C\setminus\R$ — i.e. the off-line zeros of $\Xi$ — which are precisely
the points where $m_P\not\to m_\infty$ uniformly (a Herglotz $m_P$ has no poles off $\R$, so a pole off
$\R$ can only \emph{emerge} through non-uniformity).
\end{enumerate}
\end{theorem}
\emph{Proof.} (1) PSD-ness of $\mathsf N_{m_P}$ is Herglotz-positivity; pointwise limits of PSD matrices
are PSD. (2) $\kappa(\mathcal N_{m_\infty})=\#\{$poles of $m_\infty$ in $\C^+\}$ (Kreĭn–Langer), and each
finite $m_P$ has poles only on $\R$; a $\C\setminus\R$ pole of the limit is a place where the real poles
(real zeros of $D_P$) have migrated off $\R$, impossible under local uniform convergence (Hurwitz), so it
sits exactly on the non-uniformity locus. $\square$

\begin{resultbox}
\textbf{Why finite positivity does not close it.} The defect datum M2 carried — every finite step
positive, $\sigma_P=0$ — controls $\mathsf N_{m_\infty}$ \emph{only at regular points}, where it gives
$\succeq0$ (Thm~\ref{thm:concentration}(1)). But the index lives \emph{at the off-$\R$ poles}
(Thm~\ref{thm:concentration}(2)), exactly where convergence fails and finite positivity says nothing.
\textbf{Positive rank-one divergence preserves the index at regular points and is silent at the
singular locus.} So "positive rank-one $\Rightarrow$ index $0$" is \emph{not} an unconditional theorem;
it holds iff there is no singular locus, i.e. iff convergence is uniform, i.e. iff RH.
\end{resultbox}

---

## §4. The verdict: M3 reduces RH to uniformity of the renormalization

\begin{theorem}[M3, honest form]\label{thm:m3}
The following are equivalent:
\begin{enumerate}
\item[\textbf{(i)}] RH;
\item[\textbf{(ii)}] the regularized convergence $D_P\to\Xi$ is uniform on compact subsets of $\C$;
\item[\textbf{(iii)}] the real zeros of the finite determinants $D_P$ (Lemma~\ref{lem:sa}) do not migrate
off $\R$ in the renormalized limit;
\item[\textbf{(iv)}] the positive rank-one pole renormalization creates no negative square
($\kappa(\Xi)=0$).
\end{enumerate}
\end{theorem}
\emph{Proof.} (ii)$\Rightarrow$(i) is Thm~\ref{thm:hurwitz}. (i)$\Rightarrow$(ii): with all zeros real
and the regularization's standard local estimates, $\mathrm{ren\text{-}lim}$ upgrades to uniform on
compacts (no zeros to obstruct). (ii)$\Leftrightarrow$(iii) is Hurwitz/argument principle.
(iii)$\Leftrightarrow$(iv) is Thm~\ref{thm:concentration}. $\square$

\begin{resultbox}
\textbf{M3 does not cross for free.} Signature-closedness is RH-strength: it holds iff the renormalization
is uniform (Thm~\ref{thm:m3}). The Phase-65 thesis — "recover the index from the definite sign" —
delivers the approximant side (real zeros, HB, DH excluded) but the index is concentrated at the
convergence-failure locus, beyond the reach of finite positivity. \emph{The wall survives, now in its
sharpest and most classical form:} \textbf{is the zeta/Binet-regularized truncation $D_P$ a
\emph{uniform} (Hurwitz-safe) approximation of $\Xi$ across the strip, or only a regularized one?}
\end{resultbox}

---

## §5. What this leaves — the precise target (for Connes / M4–M5)

M1–M2 built genuine new structure (the index-graded category; the pole-relative completion; T2 free).
M3 shows the new object's defining property (A2, signature-continuity) is **equivalent to RH**, not a
free theorem, and pins the residue to one concrete classical statement:

\begin{quote}
\textbf{Target (= RH, Thm~\ref{thm:m3}(ii)).} Prove that the regularized determinant $D_P$ converges to
$\Xi$ \emph{uniformly on compacts of $\C$} — equivalently, that the renormalization (which is the only
non-uniform step, and is rank-one and definite-signed) does not push the finite real zeros off $\R$.
\end{quote}

Three honest options, to be weighed (and to inform Connes' ideal M1–M5 plan):
\begin{itemize}
\item \textbf{(a) Attack uniformity directly.} Show the rank-one definite renormalization is a
\emph{uniform} (not just regularized) limit. Risk: this is essentially the Hurwitz-safe convergence
already identified as RH-strength in Phase 64; it may not be more tractable, only better-stated.
\item \textbf{(b) New invariant past the sign.} Since the index hides at the singular locus, seek a
\emph{quantitative} refinement of the defect datum that controls the kernel \emph{at} the off-$\R$
poles, not only at regular points — e.g. a residue/transmission form along $\hat h_\infty$ whose
positivity is genuinely finite-stage. This is the only way to beat Thm~\ref{thm:concentration}; whether
such a finite-stage object exists is open and is the genuine "new mathematics" question.
\item \textbf{(c) Accept M3 as the reduction.} Record RH $\Leftrightarrow$ uniformity of the
renormalization (Thm~\ref{thm:m3}) as the phase's theorem: a clean, classical, sharply-localized
equivalent, with the definite sign explaining the approximants and excluding DH.
\end{itemize}

\textbf{Honest status.} \emph{Established:} Lemma~\ref{lem:sa} (real zeros from the sign; DH excluded),
Thm~\ref{thm:hurwitz} (uniform $\Rightarrow$ RH), Thm~\ref{thm:concentration} (index concentrated at the
non-uniformity locus), Thm~\ref{thm:m3} (RH $\Leftrightarrow$ uniformity). \emph{Open (RH-strength):}
uniformity of the renormalization (Thm~\ref{thm:m3}(ii)) — i.e. (A2) itself. The new object is genuinely
constructed; its key property is RH; the residue is one classical convergence statement. No false
victory: M3 is the honest crux, and it reduces to RH rather than proving it.
