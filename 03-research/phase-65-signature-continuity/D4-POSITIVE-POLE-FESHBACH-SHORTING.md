# D4 — Positive-pole Feshbach shorting and the determinant factorization

**Phase 65 / Signature-Continuity Package, deliverable D4.** Pure mathematics, full proofs. This is the
core structural construction: the one positive divergent pole is removed by **Feshbach/Schur shorting**,
never by subtraction. It absorbs and supersedes `M2-pole-relative-completion.md`, with the central
correction made canonical — M2 used a subtraction-style renormalization; D4 uses the Schur complement,
as forced by the $G_R$ counterexample (Stage 1, §2). We define the shorted kernel $\mathsf K_P^\circ$,
prove the determinant factorization $D_P=\Delta_P\cdot D_P^\circ$, and prove (via Haynsworth, lifted to
kernels) that shorting the positive pole does not raise the index.

> `ASSUMED` ledger (D4): see §5. Block-determinant identity for $\det_2$ carries an anomaly absorbed into
> $\Delta_P$, stated explicitly.

---

## §1. The pole splitting

\begin{definition}[pole block]\label{def:block}
By G4 the realization space splits $\mathcal H_P=\C H_P\oplus\mathcal H_P^\circ$ with $H_P$ the positive
pole line ($[H_P,H_P]_P>0$) and $\mathcal H_P^\circ=Q_P\mathcal H_P$ the primitive complement. In this
splitting the regularized operator block is
\[
   I+T_P(z)=\begin{pmatrix}\alpha_P(z)&\beta_P(z)^*\\ \beta_P(z)&B_P(z)\end{pmatrix},
   \qquad \alpha_P(z)\ \text{the (positive) pole block}.
\]
\end{definition}

\begin{definition}[Feshbach transform and shorted kernel]\label{def:short}
The \textbf{Feshbach transform} of $A_P$ at the pole is
\[
   F_P(z):=B_P(z)-\beta_P(z)\,\alpha_P(z)^{-1}\,\beta_P(z)^*,
\]
the Schur complement of the pole block. With $\Gamma_P(z)$ the realization map, the \textbf{shorted
kernel} is
\[
   \mathsf K_P^\circ(z,w):=[Q_P\Gamma_P(z),Q_P\Gamma_P(w)]_P
   =\mathsf K_P(z,w)-\frac{[\Gamma_P(z),H_P]_P\,[H_P,\Gamma_P(w)]_P}{[H_P,H_P]_P}.
\]
This is the kernel of $F_P$; it is the Schur complement, \textbf{not} the subtraction
$\mathsf K_P-(\text{pole block})$.
\end{definition}

\begin{redflag}[subtraction vs shorting — the canonical correction]
The earlier M2 used pole \emph{subtraction}. By Stage 1, Prop.~$G_R$, subtracting a divergent positive
rank-one block creates a spurious negative square; the Schur complement does not. \textbf{D4 supersedes
M2: every pole removal is $\operatorname{Short}_{H_P}$, the second formula of Def.~\ref{def:short}, with
the cross-term $\beta\alpha^{-1}\beta^*$, not just $-\alpha$.} The cross-term is the entire difference.
\end{redflag}

---

## §2. The determinant factorization

\begin{theorem}[Feshbach determinant factorization]\label{thm:factor}
For each $A_P\in\mathcal C_1^+$,
\[
   \boxed{\ D_P(z)=\Delta_P(z)\cdot D_P^\circ(z),\qquad
   \Delta_P(z)=\det\nolimits_{\mathrm{reg}}\alpha_P(z)\cdot e^{\mathcal A_P^{\mathrm{pole}}(z)},\quad
   D_P^\circ(z)=\det\nolimits_{\mathrm{reg}}F_P(z).\ }
\]
Here $\mathcal A_P^{\mathrm{pole}}$ is the $\det_2$ (or $\zeta$) multiplicative anomaly of the block
factorization, absorbed into the pole factor $\Delta_P$. For the ordinary determinant
$\mathcal A_P^{\mathrm{pole}}=0$ and this is the classical block identity.
\end{theorem}
\emph{Proof.} Block $LDU$ factorization
\[
   \begin{pmatrix}\alpha&\beta^*\\ \beta&B\end{pmatrix}
   =\begin{pmatrix}1&0\\ \beta\alpha^{-1}&1\end{pmatrix}
   \begin{pmatrix}\alpha&0\\0&B-\beta\alpha^{-1}\beta^*\end{pmatrix}
   \begin{pmatrix}1&\alpha^{-1}\beta^*\\0&1\end{pmatrix}.
\]
The outer factors are unipotent (determinant $1$ for $\det_1$). Taking $\det_1$ gives $\det(I+T_P)=
\det\alpha_P\cdot\det F_P$. For $\det_2$ the multiplicative law is \emph{not} anomaly-free: for
Hilbert–Schmidt $A,B$,
\[
   \det\nolimits_2\big((I+A)(I+B)\big)=\det\nolimits_2(I+A)\,\det\nolimits_2(I+B)\,e^{-\operatorname{Tr}(AB)},
\]
so writing $I+T_P=(I+A_{\mathrm{pole}})(I+B_{\mathrm{Sch}})$ for the block-triangular $\times$ diagonal
$\times$ block-triangular factorization, the genuine anomaly is
\[
   \mathcal A_P^{\mathrm{pole}}(z)=-\sum\operatorname{Tr}(A_iB_j)\ \text{(the cross-traces of the three
   factors)},
\]
\emph{not} simply $\operatorname{Tr}(\beta\alpha^{-1}\beta^*)$. This is finite provided the Feshbach
blocks lie in $\mathfrak S_2$ (Hilbert–Schmidt); that membership is the content of the D4 ledger entry
(§5) and must be checked in the relevant Schatten class, not assumed. With $\mathcal A_P^{\mathrm{pole}}$
so defined, $D_P=\Delta_PD_P^\circ$ with $\Delta_P=\det_2\alpha_P\cdot e^{\mathcal A_P^{\mathrm{pole}}}$.
$\square$

\begin{remark}[the renormalized determinant]
$D_P^\circ=D_P/\Delta_P$ (modulo the recorded anomaly) is the \textbf{positive-pole-renormalized}
determinant. The scalar part of D8 is $D_P^\circ\to\Xi$, which is G3 with the pole factor divided out.
The \emph{sourced} version $\mathcal D_P^{\circ,\mathrm{src}}=\det_{\mathrm{reg}}(F_P+V)$ is the real
object of D8 (its $V=0$ slice is $D_P^\circ$).
\end{remark}

---

## §3. Shorting preserves the index (Haynsworth, lifted to kernels)

\begin{theorem}[positive-pole shorting is index-monotone]\label{thm:index}
For the positive pole ($\alpha_P(z)\succ0$ on the relevant set),
\[
   \operatorname{sq}_-\!\big(\mathsf K_P^\circ\big)=\operatorname{sq}_-\!\big(\mathsf K_P\big).
\]
In particular if $\mathsf K_P\succeq0$ (G2) then $\mathsf K_P^\circ\succeq0$, i.e. $\kappa(A_P^\circ)=0$.
\end{theorem}
\emph{Proof.} For any finite $z_1,\dots,z_m$ the Gram matrix of $\mathsf K_P$ has the block form
$\begin{psmallmatrix}a&b^*\\ b&C\end{psmallmatrix}$ with $a$ the (positive) pole block; the Gram matrix
of $\mathsf K_P^\circ$ is its Schur complement $C-ba^{-1}b^*$. By Haynsworth (Stage 1, Thm 1.1),
$\nu_-(C-ba^{-1}b^*)=\nu_-\begin{psmallmatrix}a&b^*\\ b&C\end{psmallmatrix}$ since $a\succ0$. Taking the
supremum over finite configurations gives $\operatorname{sq}_-(\mathsf K_P^\circ)=\operatorname{sq}_-(
\mathsf K_P)$. $\square$

\begin{corollary}[independence of normalization]\label{cor:norm}
$\mathsf K_P^\circ$ and the factorization $D_P=\Delta_PD_P^\circ$ are independent of harmless
normalizations of $H_P$ (rescaling $H_P\mapsto cH_P$, $c\ne0$): the Schur complement is invariant under
scaling the pivot, and $\Delta_P$ absorbs the compensating scalar. Hence the chart $\chi_H(\widetilde
D(A_P))=(D_P^\circ,\mathcal D_P^{\circ,\mathrm{src}},\mathsf K_P^\circ,\mathfrak b_P^\circ)$ is
well-defined.
\end{corollary}
\emph{Proof.} $C-b(c a c)^{... }$: the Schur complement $C-\beta\alpha^{-1}\beta^*$ is unchanged when
$\alpha\mapsto c^2\alpha$, $\beta\mapsto c\beta$ (the pole-line rescaling), since $\beta\alpha^{-1}
\beta^*$ is scale-invariant. $\square$

---

## §4. The chart and the interface to D5/D6

\begin{definition}[positive-pole chart]\label{def:chart}
$\chi_H(\widetilde D(A_P)):=\big(D_P^\circ,\ \mathcal D_P^{\circ,\mathrm{src}},\ \mathsf K_P^\circ,\
\mathfrak b_P^\circ\big)$, the shorted data. By Thm~\ref{thm:index}, $\mathfrak b_P^\circ=\mathfrak b_P=1$
for the von Mangoldt systems (index $0$ at every finite stage).
\end{definition}

\begin{resultbox}
\textbf{What D4 secures.} The positive pole is removed by Schur complement (Def.~\ref{def:short}), the
determinant factors as $D_P=\Delta_PD_P^\circ$ with the anomaly tracked (Thm~\ref{thm:factor}), and
shorting preserves the index (Thm~\ref{thm:index}: the finite von Mangoldt shorted kernels are still
$\succeq0$). The construction is normalization-independent (Cor.~\ref{cor:norm}). This is the correct
renormalization — the M2 subtraction error is fixed. \emph{What remains is convergence:} whether the
shorted kernels $\mathsf K_P^\circ$ converge to the fixed endpoint $\mathsf K_\Xi^{\mathrm{G5}}$ (D8), and
whether index-$0$ is closed under that convergence (D6). D4 supplies the objects; it does not yet take
the limit.
\end{resultbox}

---

## §5. `ASSUMED` ledger (D4)

> `OPEN (technical, Connes R1.D): the Feshbach factors $A_{pole},B_{Sch}$ of $I+T_P$ lie in $\mathfrak
> S_2$ on compact $z$-sets away from the pole spectrum, so the genuine det₂ anomaly $\mathcal
> A_P^{pole}=-\sum\operatorname{Tr}(A_iB_j)$ is finite and holomorphic.` — needed for
> Thm~\ref{thm:factor}; expected from the trace-class structure of the primitive block (D2 ledger) and
> $\alpha_P\succ0$, but must be verified in the Schatten class $\mathfrak S_2$, not assumed in the naive
> $\operatorname{Tr}(\beta\alpha^{-1}\beta^*)$ form (which was wrong). Does not use RH.

---

## §6. What D4 establishes

- The shorted kernel $\mathsf K_P^\circ$ via **Schur complement** (Def.~\ref{def:short}), with the
  subtraction error of M2 corrected (the cross-term $\beta\alpha^{-1}\beta^*$).
- The **determinant factorization** $D_P=\Delta_P D_P^\circ$ with the anomaly explicit
  (Thm~\ref{thm:factor}).
- **Index-monotonicity of shorting** (Thm~\ref{thm:index}): positive-pole shorting preserves
  $\operatorname{sq}_-$; finite von Mangoldt shorted kernels stay $\succeq0$.
- Normalization-independence and the well-defined positive-pole chart (Cor.~\ref{cor:norm},
  Def.~\ref{def:chart}).

Next: D5 builds the topology $\tau_\kappa$ on these charts in which source-germ convergence implies
kernel convergence, and D6 proves index-$0$ is closed there.
