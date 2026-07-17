# D7 — Finite von Mangoldt compatibility (axiom A1)

**Phase 65 / Signature-Continuity Package, deliverable D7.** Pure mathematics, full proofs. This pins the
finite endpoint of the construction to the given data: every finite von Mangoldt system is an object of
$\mathcal G_0$ (index $0$), and its sourced determinant germ's recovered kernel **is** the canonical Gram
kernel. This is axiom A1 of the package. It uses only G1–G2 (proved Phase 64).

> `ASSUMED` ledger (D7): **empty** beyond the G1–G2 inputs themselves.

---

## §1. Finite positivity and index zero

\begin{theorem}[A1: finite systems are in $\mathcal G_0$]\label{thm:a1}
For each finite $P$, $\widetilde D(A_P)=(E_P,\mathcal D_{A_P}^{\mathrm{src}},\mathsf K_{A_P},1,\mathcal
R_P)\in\mathcal G_0$, with
\[
   \mathsf K_{A_P}(z,w)=\int_0^{\ell_P}Y_P(t,w)^*H_P(t)Y_P(t,z)\,dt\ \succeq\ 0,\qquad
   \kappa(A_P)=\operatorname{sq}_-(\mathsf K_{A_P})=0,\qquad\mathfrak b_P=1.
\]
\end{theorem}
\emph{Proof.} G2 (canonical Gram identity, `CANONICAL-FOUNDATION.md` Thm) gives the displayed integral
representation, manifestly $\succeq0$ since $H_P\ge0$ (G1): for any finite $\{z_i\}$, $\{c_i\}$,
$\sum_{i,j}\bar c_i c_j\mathsf K_{A_P}(z_i,z_j)=\int_0^{\ell_P}\big\|H_P(t)^{1/2}\sum_j c_jY_P(t,z_j)
\big\|^2dt\ge0$. Hence $\operatorname{sq}_-(\mathsf K_{A_P})=0$, so the Kreĭn–Langer divisor is empty,
$\mathfrak b_P=1$ (D1, Def. divisor), and $E_P$ is Hermite–Biehler (D1, Thm d1). $\square$

---

## §2. Sourced determinant $=$ canonical Gram response

\begin{theorem}[germ–Gram compatibility]\label{thm:compat}
The recovered kernel of the sourced determinant germ (D2, Def. rec) coincides with the canonical Gram
kernel:
\[
   \operatorname{Pol}\big(d^2\log\mathcal D_{A_P}^{\mathrm{src}}(0)\big)(z,w)=\mathsf K_{A_P}(z,w)
   =\int_0^{\ell_P}Y_P(t,w)^*H_P(t)Y_P(t,z)\,dt.
\]
\end{theorem}
\emph{Proof.} By D2, Prop. cansys, the first variation of $\mathcal D_{A_P}^{\mathrm{src}}$ along a
finite-rank signed source $\delta H$ is the canonical pairing
\[
   \partial_\varepsilon\log\mathcal D_{A_P,\varepsilon}^{\mathrm{src}}(0)
   =\int_0^{\ell_P}\operatorname{tr}\big(Y_P(t,\cdot)^*\,\delta H(t)\,Y_P(t,\cdot)\big)\,dt
\]
(Duhamel/variation-of-parameters for $J\partial_tY=z(H_P+\varepsilon\delta H)Y$). Polarizing the second
variation in two such sources reconstructs the bilinear form $\int Y_P^*H_PY_P$, which is $\mathsf
K_{A_P}$. The anomaly is first-order only ($\det_2$, D2 Lemma higher), so the second-order (kernel) term
is exactly the Gram form. $\square$

\begin{corollary}[the chart at finite $P$]\label{cor:chart}
After pole-shorting (D4), $\chi_H(\widetilde D(A_P))=(D_P^\circ,\mathcal D_P^{\circ,\mathrm{src}},\mathsf
K_P^\circ,1)$ with $\mathsf K_P^\circ\succeq0$ (D4, Thm index, since $\mathsf K_{A_P}\succeq0$ and the
pole is positive). So the entire finite tower lies in $\mathcal G_0$ and is a tower of monotone (positive
extension) morphisms in $\mathcal G^+$ (one prime cell per step).
\end{corollary}
\emph{Proof.} Thm~\ref{thm:a1} + D4 Thm index for the shorted kernel; each step $A_P\to A_{P+1}$ adjoins a
positive von Mangoldt atom $d\mathcal H_{p_{P+1}}\ge0$, a positive extension (D3, Def. mor (P+)). $\square$

---

## §3. The diagram, ready for the limit

\begin{resultbox}
\textbf{A1 secured.} The finite von Mangoldt systems form a tower in $\mathcal G_0$:
\[
   \widetilde D(A_2)\xrightarrow{\ \mathcal G^+\ }\widetilde D(A_3)\xrightarrow{\ \mathcal G^+\ }\cdots,
   \qquad \mathsf K_P^\circ\succeq0,\ \ \kappa(A_P)=0,\ \ \mathfrak b_P=1,
\]
each arrow a positive extension, and the recovered kernel is the canonical Gram kernel
(Thm~\ref{thm:compat}). By D3, Lemma functor, $\kappa$ is preserved along every \emph{finite} arrow; the
question is solely whether it is preserved in the \emph{limit}, i.e. whether the renormalization morphism
$\Phi_\infty$ is in $\mathcal G^+$. By D6 (closedness) this follows \emph{once} the shorted kernels are
shown to $\tau_\kappa$-converge to the fixed endpoint $\mathsf K_\Xi^{\mathrm{G5}}$. That convergence is
D8 + D9.
\end{resultbox}

---

## §4. What D7 establishes

- **A1** (Thm~\ref{thm:a1}): finite von Mangoldt systems are index-$0$ objects of $\mathcal G_0$, with
  Gram kernel $\succeq0$ and trivial grading divisor, from G1–G2.
- **Germ–Gram compatibility** (Thm~\ref{thm:compat}): the sourced determinant's recovered kernel is the
  canonical Gram kernel — so D8's *sourced* convergence is genuinely *Gram-kernel* convergence.
- The tower lies in $\mathcal G_0$ with monotone arrows (Cor.~\ref{cor:chart}); everything is staged for
  the limit.

This completes the formal scaffolding D0–D7. The remaining deliverables D8 (the decisive arithmetic
sourced convergence) and D9 (endpoint $=$ fixed $\mathsf K_\Xi^{\mathrm{G5}}$) carry the entire
mathematical burden of the package.
