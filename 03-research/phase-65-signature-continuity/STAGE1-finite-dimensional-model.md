# Stage 1 — The finite-dimensional sanity model: the whole machine on Hermitian matrices

**Phase 65 / Signature-Continuity Package, build Stage 1.** Pure mathematics, full proofs, no
computation. Before any operator theory or arithmetic, we verify the entire mechanism on finite Hermitian
matrices with one positive divergent line. Four things must hold, and we prove all four:
**(S1)** the sourced determinant separates signature (defeats N1 in finite dimensions);
**(S2)** Feshbach/Schur shorting of a positive line preserves the negative index (Haynsworth inertia);
**(S3)** the positive-pole chart closes the index-$0$ cone under convergence;
**(S4)** signed examples fail — a negative line *can* raise the index (the Davenport–Heilbronn shadow).
We also prove **the $G_R$ counterexample**: naive subtraction of the positive pole creates a spurious
negative square, so shorting is mandatory. This stage is the sanity layer for D2, D4, D5, D6; any
definitional error in the package surfaces here first.

> `ASSUMED` ledger: **empty.** Stage 1 is fully self-contained (elementary linear algebra).

---

## §0. Notation

$\mathrm{Herm}_n$ = $n\times n$ complex Hermitian matrices. For $G\in\mathrm{Herm}_n$, $\nu_-(G),
\nu_0(G),\nu_+(G)$ are the numbers of negative, zero, positive eigenvalues (the inertia
$\operatorname{In}(G)=(\nu_+,\nu_0,\nu_-)$). For a block form with a distinguished positive line we write
\[
   G=\begin{pmatrix} a & b^*\\ b & C\end{pmatrix},\qquad a>0\ (\text{scalar, the pole block}),\ \
   C\in\mathrm{Herm}_{n-1},\ b\in\C^{n-1}.
\]
The \textbf{Schur complement} (Feshbach short) of the pole block is
\[
   \operatorname{Short}_a(G)\ :=\ C-b\,a^{-1}b^*\ \in\ \mathrm{Herm}_{n-1}.
\]

---

## §1. (S2) Feshbach shorting preserves inertia off the pole — Haynsworth

\begin{theorem}[Haynsworth inertia additivity]\label{thm:haynsworth}
If $a>0$ then
\[
   \operatorname{In}(G)=\operatorname{In}(a)+\operatorname{In}\big(\operatorname{Short}_a(G)\big)
   =(1,0,0)+\operatorname{In}\big(C-ba^{-1}b^*\big).
\]
In particular $\nu_-(G)=\nu_-\!\big(\operatorname{Short}_a(G)\big)$ and $\nu_+(G)=1+\nu_+\!\big(
\operatorname{Short}_a(G)\big)$.
\end{theorem}
\emph{Proof.} Congruence by the block-triangular $T=\begin{psmallmatrix}1&0\\-ba^{-1}&I\end{psmallmatrix}$:
\[
   T\,G\,T^*=\begin{pmatrix}a&0\\0&C-ba^{-1}b^*\end{pmatrix}.
\]
Sylvester's law of inertia (congruence preserves $\operatorname{In}$) gives
$\operatorname{In}(G)=\operatorname{In}(a)\oplus\operatorname{In}(C-ba^{-1}b^*)$. With $a>0$,
$\operatorname{In}(a)=(1,0,0)$. $\square$

\begin{corollary}[positive pole shorting does not increase the negative index]\label{cor:shorting}
For $a>0$, $\ \nu_-\!\big(\operatorname{Short}_a(G)\big)=\nu_-(G)\le\nu_-(G)$. Hence if $G\succeq0$
(so $\nu_-(G)=0$) then $\operatorname{Short}_a(G)\succeq0$.
\end{corollary}

This is the finite-dimensional skeleton of D4/D6: \emph{shorting a positive line cannot create a negative
square.}

---

## §2. The $G_R$ counterexample: subtraction is wrong

\begin{proposition}[naive subtraction creates a spurious negative square]\label{prop:GR}
Let, for $R>0$,
\[
   G_R=\begin{pmatrix}R&\sqrt R\\ \sqrt R&1\end{pmatrix}\succeq0
   \qquad(\det G_R=R-R=0,\ \operatorname{tr}=R+1>0).
\]
\textbf{Subtracting} the pole block $R\,e_1e_1^*$ gives
$\begin{psmallmatrix}0&\sqrt R\\ \sqrt R&1\end{psmallmatrix}$, with determinant $-R<0$, hence
$\nu_-=1$: a negative square has been \emph{created}. \textbf{Shorting} the pole block gives
$\operatorname{Short}_R(G_R)=1-(\sqrt R)R^{-1}(\sqrt R)=1-1=0\succeq0$: the index is preserved
(Cor.~\ref{cor:shorting}).
\end{proposition}
\emph{Proof.} Direct computation; $\det\begin{psmallmatrix}0&\sqrt R\\\sqrt R&1\end{psmallmatrix}=-R<0$
forces one negative eigenvalue. $\square$

\begin{redflag}
$G_R$ is the finite shadow of the divergent pole ($R\sim\tfrac12(\log P)^2\to\infty$). It shows the
catastrophe the package must avoid: \textbf{as $R\to\infty$, subtraction produces a negative square that
is pure artifact}, whereas shorting is stable and index-preserving. Every pole removal in D4/D6/D8 must
be a Schur complement, never a subtraction. This is why "positive rank-one divergence" does \emph{not}
trivially preserve the index unless one uses the correct (Feshbach) removal.
\end{redflag}

---

## §3. (S1) The sourced determinant separates signature

In finite dimensions the "sourced determinant" of $G\in\mathrm{Herm}_n$ is the polynomial germ
\[
   \mathcal D_G^{\mathrm{src}}(V)=\det(I+G+V),\qquad V\in\mathrm{Herm}_n\ \text{near }0,
\]
and its scalar shadow is $\mathcal D_G^{\mathrm{src}}(0)=\det(I+G)$.

\begin{proposition}[scalar determinant is signature-blind; the germ is not]\label{prop:sep}
\emph{(a)} There exist $G\ne G'$ in $\mathrm{Herm}_n$ with $\det(I+G)=\det(I+G')$ but $\nu_-(G)\ne
\nu_-(G')$. \emph{(b)} If $\mathcal D_G^{\mathrm{src}}=\mathcal D_{G'}^{\mathrm{src}}$ as germs at $0$,
then $G=G'$, hence $\nu_-(G)=\nu_-(G')$.
\end{proposition}
\emph{Proof.} (a) Take $n=2$, $G=\operatorname{diag}(1,-\tfrac12)$ and $G'=\operatorname{diag}(0,0)$.
Then $\det(I+G)=(1+1)(1-\tfrac12)=2\cdot\tfrac12=1=\det(I+G')$, while $\nu_-(G)=1\ne0=\nu_-(G')$. The
scalar determinant, depending only on the product $\prod_i(1+\lambda_i)$, loses the sign pattern of the
$\lambda_i$. (b) The first variation $d\mathcal D_G^{\mathrm{src}}(0)[V]=\det(I+G)\operatorname{tr}\!
\big((I+G)^{-1}V\big)$
determines $(I+G)^{-1}$ as a linear functional on all $V\in\mathrm{Herm}_n$, hence determines $G$;
$\nu_-$ is then a function of $G$. $\square$

\begin{remark}[the separation mechanism, made precise]
The map $V\mapsto\operatorname{tr}((I+G)^{-1}V)$ \emph{is} the resolvent, and by polarization the second
variation recovers the two-variable Hermitian form. So the germ sees the whole of $G$, in particular its
inertia, while $\det(I+G)$ sees only $\prod(1+\lambda_i)$. This is N1 defeated in finite dimensions and
the template for D2.
\end{remark}

---

## §4. (S3) The positive-pole chart closes the index-$0$ cone

Model the chart of D5 in finite dimensions: to $G$ (with pole block $a>0$) associate
$\chi(G)=\operatorname{Short}_a(G)\in\mathrm{Herm}_{n-1}$, and topologize by entrywise convergence.

\begin{theorem}[closedness of the PSD cone under shorting limits]\label{thm:closed}
Let $G^{(k)}\succeq0$ with pole blocks $a^{(k)}>0$, and suppose the shorted matrices converge,
$\operatorname{Short}_{a^{(k)}}(G^{(k)})\to S$. Then $S\succeq0$; i.e. $\nu_-(S)=0$. More generally if
$\nu_-(G^{(k)})\le\kappa$ for all $k$ then $\nu_-(S)\le\kappa$.
\end{theorem}
\emph{Proof.} By Cor.~\ref{cor:shorting}, $\nu_-\!\big(\operatorname{Short}_{a^{(k)}}(G^{(k)})\big)
=\nu_-(G^{(k)})\le\kappa$. The set $\{M\in\mathrm{Herm}_{n-1}:\nu_-(M)\le\kappa\}$ is closed (it is
$\{M:\lambda_{\kappa+1}(M)\ge0\}$, and the $(\kappa{+}1)$-st smallest eigenvalue is continuous in $M$).
The entrywise limit $S$ therefore satisfies $\nu_-(S)\le\kappa$; for $\kappa=0$, $S\succeq0$. $\square$

\begin{remark}[why the divisor is needed for *exact* continuity]
Theorem~\ref{thm:closed} gives upper semicontinuity $\nu_-(S)\le\liminf\nu_-(G^{(k)})$, which is all M3/D6
need for the index-$0$ statement ($0\le0$). Exact continuity (no negative square \emph{vanishing}
silently) is the role of the grading divisor $\mathfrak b$ (D1/D5); in the index-$0$ stratum
$\mathfrak b\equiv1$ and there is nothing to vanish, so $\kappa=0$ is genuinely closed, not merely upper
semicontinuous.
\end{remark}

---

## §5. (S4) Signed examples fail — the Davenport–Heilbronn shadow

\begin{proposition}[a negative line raises the index]\label{prop:signed}
Let the pole block be \emph{negative}, $a<0$, $G=\begin{psmallmatrix}a&b^*\\ b&C\end{psmallmatrix}$ with
$C\succ0$ and $b\ne0$. Then $\operatorname{In}(G)=(\nu_+(\operatorname{Short}_a G),0,1+\nu_-(
\operatorname{Short}_a G))$ by Haynsworth with $\operatorname{In}(a)=(0,0,1)$; in particular $\nu_-(G)\ge1$.
Even if every \emph{primitive} increment is positive, a single negative pole line forces
$\nu_-\ge1$.
\end{proposition}
\emph{Proof.} Haynsworth (Thm~\ref{thm:haynsworth}) with $a<0$ contributes $(0,0,1)$ to the inertia.
$\square$

\begin{resultbox}
\textbf{Falsifier confirmed at the finite level.} The whole mechanism turns on the \emph{sign} of the
pole block: $a>0$ (von Mangoldt, G4) $\Rightarrow$ shorting preserves $\nu_-=0$ (S2, S3); $a<0$
(the Davenport–Heilbronn shadow / a signed Hamiltonian) $\Rightarrow$ $\nu_-\ge1$ (S4). A construction
that gave $\nu_-=0$ regardless of the sign of $a$ would be too coarse and is rejected. Stage 1 shows the
sign is load-bearing exactly where D4/D6/D10 will need it.
\end{resultbox}

---

## §6. What Stage 1 establishes (sanity layer secured)

\begin{itemize}
\item \textbf{S1} (Prop.~\ref{prop:sep}): scalar determinant blind, sourced germ separates signature —
N1 defeated in finite dimensions; template for D2.
\item \textbf{S2} (Thm~\ref{thm:haynsworth}, Cor.~\ref{cor:shorting}): Feshbach shorting of a positive
line preserves $\nu_-$; template for D4.
\item \textbf{$G_R$} (Prop.~\ref{prop:GR}): naive subtraction creates a spurious negative square as
$R\to\infty$; shorting does not — \emph{shorting is mandatory}.
\item \textbf{S3} (Thm~\ref{thm:closed}): the index-$\le\kappa$ set is closed under shorting limits;
template for D6, with the divisor handling exact continuity.
\item \textbf{S4} (Prop.~\ref{prop:signed}): a negative pole line raises the index — the sign is
load-bearing; template for D10.
\end{itemize}

Every later deliverable is the infinite-dimensional / arithmetic lift of one of these five finite facts.
No definitional error survives Stage 1: in particular, the package uses shorting (not subtraction) and
relies on the positivity of the pole, both verified here. Proceed to D1 (the analytic substrate that
makes "$\nu_-$ of a Hermitian matrix" into "$\operatorname{sq}_-$ of a kernel").
