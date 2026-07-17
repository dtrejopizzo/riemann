# D1 — The generalized Hermite–Biehler / Nevanlinna / Schur / de Branges–Pontryagin substrate

**Phase 65 / Signature-Continuity Package, deliverable D1.** Pure mathematics, full proofs (plan
decision 2). This is the analytic substrate of the category $\mathcal G$: the four equivalent ways to
read the Kreĭn–Langer index $\kappa$ off an object — the de Branges kernel chart, the generalized
Nevanlinna chart, the generalized Schur chart, and the Pontryagin reproducing-kernel realization — and
the proof that they all give the same integer, with the same grading divisor $\mathfrak b$. This makes
"$\kappa(\Xi)$" (D0, Def. KG5) a chart-independent invariant and supplies the language for D2–D6.

> `ASSUMED` ledger: **empty.** D1 proves the chart equivalences from the definitions; we use only the
> classical Kreĭn–Langer factorization theorem, whose statement and proof we include (§4).

---

## §1. The four charts

Fix a domain symmetric under $z\mapsto\bar z$; $E^\#(z):=\overline{E(\bar z)}$, $M^\#(z):=
\overline{M(\bar z)}$.

\begin{definition}[charts]\label{def:charts}
\begin{enumerate}
\item[\textbf{(HB)}] \emph{de Branges kernel.} For entire $E$ with $E^\#$, the kernel
\[
   \mathsf K_E(z,w)=\frac{E(z)\overline{E(w)}-E^\#(z)\overline{E^\#(w)}}{2\pi i\,(\bar w-z)} .
\]
\item[\textbf{(N)}] \emph{generalized Nevanlinna.} For $M$ meromorphic on $\C\setminus\R$ with
$M^\#=M$ (real-symmetric), the Nevanlinna kernel
\[
   \mathsf N_M(z,w)=\frac{M(z)-\overline{M(w)}}{z-\bar w}.
\]
\item[\textbf{(S)}] \emph{generalized Schur.} $S(z)=\dfrac{M(z)-i}{M(z)+i}$ (Cayley transform), and the
Schur kernel $\mathsf S(z,w)=\dfrac{1-S(z)\overline{S(w)}}{1-z\bar w}$ in the disk model, or its
half-plane analogue.
\item[\textbf{(P)}] \emph{Pontryagin realization.} A triple $(\Pi,[\cdot,\cdot],\Gamma)$ with $\Pi$ a
Pontryagin space of negative index $\kappa$ and $\Gamma(z)\in\Pi$ a realization map such that
$\mathsf K(z,w)=[\Gamma(w),\Gamma(z)]$.
\end{enumerate}
The associated index in each chart: $\operatorname{sq}_-(\mathsf K_E)$, $\operatorname{sq}_-(\mathsf N_M)$,
$\operatorname{sq}_-(\mathsf S)$, $\operatorname{ind}_-\Pi$.
\end{definition}

---

## §2. HB $\to$ S: $E^\#/E$ is the *Schur* coordinate *(corrected, Connes R1.B)*

\begin{lemma}[kernel identity — Schur, not Nevanlinna]\label{lem:hbn}
With $S:=E^\#/E$ (where defined), up to the strictly positive gauge $g(z)\overline{g(w)}$ ($g=E/\sqrt{2\pi
i}$ on $\R$),
\[
   \mathsf K_E(z,w)=\frac{E(z)\overline{E(w)}}{2\pi i\,(\bar w-z)}\big(1-S(z)\overline{S(w)}\big)
   =g(z)\,\mathsf S(z,w)\,\overline{g(w)},
\]
i.e. $E^\#/E$ is a \textbf{generalized Schur} coordinate, \emph{not} the Nevanlinna coordinate. (The
earlier draft wrongly identified $E^\#/E$ with $M$; corrected here.)
\end{lemma}
\emph{Proof.} Factor $E(z)\overline{E(w)}$ out of $E(z)\overline{E(w)}-E^\#(z)\overline{E^\#(w)}$ using
$E^\#=SE$, $\overline{E^\#(w)}=\overline{S(w)}\,\overline{E(w)}$, giving $E(z)\overline{E(w)}(1-S(z)
\overline{S(w)})$. Divide by $2\pi i(\bar w-z)$. $\square$

\begin{corollary}\label{cor:hbn}
A strictly positive scalar gauge $g(z)\overline{g(w)}$ does not change negative squares (congruence of
every finite Gram matrix by $\operatorname{diag}(g(z_i))$). Hence $\operatorname{sq}_-(\mathsf K_E)=
\operatorname{sq}_-(\mathsf S)$.
\end{corollary}

This is the gauge morphism of D3, here at the kernel level.

---

## §3. S $\to$ N: the Cayley transform to the Nevanlinna coordinate *(corrected order)*

The Nevanlinna function is obtained from the Schur coordinate by the **inverse Cayley transform**
\[
   M:=i\,\frac{1+S}{1-S}\qquad(\text{equivalently }S=\frac{M-i}{M+i}),
\]
\emph{not} by setting $M=E^\#/E$. The chart order is therefore $E\to S=E^\#/E\to M=i(1+S)/(1-S)$.

\begin{lemma}[Cayley invariance]\label{lem:ns}
The Schur kernel and the Nevanlinna kernel of the Cayley-related $S,M$ have equal negative squares:
$\operatorname{sq}_-(\mathsf S)=\operatorname{sq}_-(\mathsf N_M)$.
\end{lemma}
\emph{Proof.} The Cayley transform is a Möbius map; the corresponding kernel transformation is a
congruence by the nonvanishing multiplier $(1-S(z))^{-1}$ (equivalently $(M(z)+i)^{-1}$):
\[
   \mathsf N_M(z,w)=\frac{M(z)-\overline{M(w)}}{z-\bar w}
   =\frac{2i}{(1-S(z))\overline{(1-S(w))}}\cdot\frac{\big(1-S(z)\overline{S(w)}\big)}{z-\bar w}\cdot(\dots),
\]
a congruence by a nonvanishing multiplier, which preserves the negative-square count of every finite Gram
matrix (Sylvester, Stage 1 Thm 1.1). $\square$

---

## §4. The Kreĭn–Langer factorization and the grading divisor

We include the classical theorem (statement and proof sketch in full enough form to be self-contained).

\begin{theorem}[Kreĭn–Langer]\label{thm:kl}
Let $S$ be a generalized Schur function with $\operatorname{sq}_-(\mathsf S)=\kappa<\infty$. Then $S$ has
a unique coprime factorization
\[
   S=\frac{S_0}{B},\qquad B(z)=\prod_{j=1}^\kappa\frac{z-\alpha_j}{1-\bar\alpha_j z}\ (\,|\alpha_j|<1\,),
\]
where $S_0$ is an ordinary Schur function ($\operatorname{sq}_-=0$, i.e. $\|S_0\|_\infty\le1$) and $B$ is
a finite Blaschke product of degree $\kappa$. The zeros $\alpha_j$ of $B$ are exactly the points where
the kernel $\mathsf S$ carries its negative squares (the generalized poles of $M$ in $\C\setminus\R$).
\end{theorem}
\emph{Proof (sketch, standard).} The reproducing-kernel Pontryagin space $\mathcal P(\mathsf S)$ has
negative index $\kappa$. A maximal negative subspace is $\kappa$-dimensional; its associated
finite-dimensional invariant structure produces the Blaschke denominator $B$ (the characteristic
function of the negative part), and dividing it out yields a positive-definite kernel, i.e. an ordinary
Schur $S_0$. Uniqueness is coprimeness of $S_0,B$. (Kreĭn–Langer 1977; Alpay–Dijksma–Rovnyak–de Branges,
\emph{Schur functions, operator colligations, and reproducing kernel Pontryagin spaces}.) $\square$

\begin{definition}[grading divisor]\label{def:divisor}
$\mathfrak b:=B$, the Blaschke denominator, regarded as a divisor $\sum_j[\alpha_j]$ on $\C\setminus\R$
(equivalently on the disk model). Its degree is $\deg\mathfrak b=\kappa$. For an ordinary
(positive-definite) object, $\mathfrak b=1$ ($\deg=0$).
\end{definition}

---

## §5. P: the Pontryagin realization computes the same $\kappa$

\begin{theorem}[realization]\label{thm:realiz}
Every kernel $\mathsf K$ with $\operatorname{sq}_-(\mathsf K)=\kappa<\infty$ admits a Pontryagin
realization $(\Pi,[\cdot,\cdot],\Gamma)$ with $\operatorname{ind}_-\Pi=\kappa$ and $\mathsf K(z,w)=
[\Gamma(w),\Gamma(z)]$, unique up to isomorphism (minimal realization). Conversely any such realization
gives $\operatorname{sq}_-(\mathsf K)=\operatorname{ind}_-\Pi$.
\end{theorem}
\emph{Proof.} The reproducing-kernel space construction: span $\{\mathsf K(\cdot,w)\}$ with the inner
product $[\mathsf K(\cdot,w),\mathsf K(\cdot,z)]:=\mathsf K(z,w)$, completed to a Pontryagin space; by
definition of $\operatorname{sq}_-$ its negative index is $\kappa$. Minimality and uniqueness are the
standard reproducing-kernel argument. $\square$

---

## §6. Main theorem of D1: all charts agree

\begin{theorem}[chart equivalence]\label{thm:d1}
For an object presented in any of the four charts (Def.~\ref{def:charts}) with the standard transforms
$E\leftrightarrow M=E^\#/E\leftrightarrow S=(M-i)/(M+i)\leftrightarrow(\Pi,\Gamma)$,
\[
   \boxed{\ \operatorname{sq}_-(\mathsf K_E)=\operatorname{sq}_-(\mathsf N_M)=\operatorname{sq}_-(\mathsf S)
   =\operatorname{ind}_-\Pi=\deg\mathfrak b\ =:\ \kappa.\ }
\]
The integer $\kappa$ and the divisor $\mathfrak b$ are therefore chart-independent invariants of the
object.
\end{theorem}
\emph{Proof.} Cor.~\ref{cor:hbn} (HB $=$ S), Lemma~\ref{lem:ns} (S $=$ N), Thm~\ref{thm:kl} ($\deg
\mathfrak b$ from the Schur chart), Thm~\ref{thm:realiz} (P $=$ sq$_-$). Chaining the equalities gives the
boxed identity. $\square$

\begin{corollary}[the endpoint, in charts]\label{cor:xi}
For $\Xi$ with $M_\Xi=-\Xi'/\Xi$ (Herglotz, D0 sign-corrected) and $\mathsf K_\Xi^{\mathrm{G5}}=\mathsf
N_{M_\Xi}$ (D0, Def. KG5),
$\kappa(\Xi)=\operatorname{sq}_-(\mathsf K_\Xi^{\mathrm{G5}})=\deg\mathfrak b_\Xi$, and RH $\Leftrightarrow
\mathfrak b_\Xi=1$. The grading divisor $\mathfrak b_\Xi$ is supported exactly on the off-line zeros
(the off-$\R$ generalized poles of $M_\Xi$).
\end{corollary}

\begin{remark}[why the divisor matters downstream]
Theorem~\ref{thm:d1} gives not just the integer $\kappa$ but the \emph{divisor} $\mathfrak b$. Plain
$\operatorname{sq}_-$ is only upper semicontinuous under limits (Stage 1, Thm 4.1: a negative square can
vanish in a limit but cannot appear from a positive limit). The divisor $\mathfrak b$ refines this to
\emph{exact} continuity: tracking $\mathfrak b$ (D5's divisor-convergence requirement) prevents negative
squares from disappearing invisibly, which is what "index continuity," not just "index upper
semicontinuity," requires for a genuine identification of the endpoint (D9). In the index-$0$ stratum
$\mathfrak b=1$ and there is nothing to track — closedness of $\{\kappa=0\}$ is then unconditional
(Stage 1, S3), which is all the assembly D11 needs.
\end{remark}

---

## §7. What D1 establishes

- The four charts (HB / N / S / P) define one index $\kappa$ and one divisor $\mathfrak b$
  (Thm~\ref{thm:d1}); gauge and Cayley moves preserve them (Cor.~\ref{cor:hbn}, Lemma~\ref{lem:ns}).
- $\kappa(\Xi)$ and $\mathfrak b_\Xi$ are well-defined chart-independent invariants of the *fixed*
  endpoint (Cor.~\ref{cor:xi}); RH $\Leftrightarrow\mathfrak b_\Xi=1$.
- The grading divisor gives the path from index *upper semicontinuity* (Stage 1) to index *continuity*
  needed for D9; in the index-$0$ stratum the two coincide.

This is the language layer. D2 next: the sourced determinant that *reads $\kappa$ off the operator* (so
that the category $\mathcal G$ in D3 carries this invariant functorially, defeating signature-blindness
N1 at the operator level — the finite-dimensional template being Stage 1, S1).
