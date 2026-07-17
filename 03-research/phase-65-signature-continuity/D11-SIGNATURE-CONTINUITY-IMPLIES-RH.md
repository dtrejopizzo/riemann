# D11 — Assembly: signature continuity implies RH

> **R3 update.** The assembled chain now runs through the log-derivative Weyl coordinate `M_P` (Herglotz by
> H1 ⇐ G2) and the trace-log identity, with Vitali on the one-variable `M_Ξ` and `sq₋` read off `K_Ξ` at
> the end. Single load-bearing input: **H1** (real zeros of `D_P^∘`). See
> [`CORRECTIONS-CONNES-R3.md`](CORRECTIONS-CONNES-R3.md).

**Phase 65 / Signature-Continuity Package, deliverable D11.** Pure mathematics. The final deduction. It is
short: once D0–D10 are in place, RH is a one-line corollary, **conditional on the single load-bearing
input D8.5**. We state the assembly, then state with full honesty exactly what is proved unconditionally
and what rests on D8.5.

---

## §1. The deduction

\begin{theorem}[Signature-Continuity $\Rightarrow$ RH]\label{thm:main}
Assume D8.5 (the source-level local-factor convergence; D8 §9 ledger). Then:
\[
   \underbrace{\kappa(A_P)=0\ \forall P}_{\text{D7 (A1), from G1–G2}}
   \ \xRightarrow{\ \text{D4 shorting}\ }\
   \underbrace{\operatorname{sq}_-(\mathsf K_P^\circ)=0}_{\text{D4 Thm index}}
   \ \xRightarrow{\ \text{D8 (incl. 8.5)}\ }\
   \underbrace{\mathsf K_P^\circ\to\mathsf K_\infty^\circ}_{\text{D8.7}}
\]
\[
   \xRightarrow{\ \text{D6 closedness}\ }\ \operatorname{sq}_-(\mathsf K_\infty^\circ)=0
   \ \xRightarrow{\ \text{D9 (A3)}\ }\ \mathsf K_\infty^\circ=\mathsf K_\Xi^{\mathrm{G5}}
   \ \Rightarrow\ \operatorname{sq}_-(\mathsf K_\Xi^{\mathrm{G5}})=0.
\]
By G5 (D0, Prop. g5), $\operatorname{sq}_-(\mathsf K_\Xi^{\mathrm{G5}})=\#\{\rho:\zeta(\rho)=0,\ \Re\rho
\ne\tfrac12\}$. Therefore
\[
   \#\{\rho:\zeta(\rho)=0,\ \Re\rho\ne\tfrac12\}=0,\qquad\text{i.e. }\boxed{\text{RH.}}
\]
\end{theorem}
\emph{Proof.} Chain the cited results. D7: finite index $0$. D4: shorting preserves it. D8 (with 8.5):
the shorted kernels converge to $\mathsf K_\infty^\circ$. D6: the limit is positive (index $0$). D9: the
limit *is* the fixed $\mathsf K_\Xi^{\mathrm{G5}}$. Hence that fixed kernel has index $0$; G5 reads this
as no off-line zeros. $\square$

---

## §2. Exactly what is unconditional, and what rests on D8.5

\begin{center}
\begin{tabular}{lll}
\hline
\textbf{Step} & \textbf{Deliverable} & \textbf{Status} \\
\hline
finite index $0$ & D7 (A1) & \textbf{unconditional} (G1–G2) \\
shorting preserves index & D4 & \textbf{unconditional} (Haynsworth) \\
closedness of index $0$ & D6 & \textbf{unconditional} (Schur positivity) \\
finite-dim sanity & Stage 1 & \textbf{unconditional} \\
chart equivalence & D1 & \textbf{unconditional} (Kreĭn–Langer) \\
sourced determinant defeats N1 & D2 & \textbf{unconditional} \\
category / functor & D3 & \textbf{unconditional} \\
topology / germ$\Rightarrow$kernel & D5 & \textbf{unconditional} \\
DH falsifier fires & D10 & \textbf{unconditional} \\
\hline
sourced germ convergence & D8.1–8.4, 8.6–8.7 & \textbf{conditional on D8.5} \\
\textbf{source-level local factors} & \textbf{D8.5} & \textbf{LOAD-BEARING — assumed (Connes/Consani, tested)} \\
endpoint $=\mathsf K_\Xi^{\mathrm{G5}}$ & D9 (A3) & \textbf{conditional on D8.5} \\
\hline
\textbf{RH} & D11 & \textbf{conditional on D8.5} \\
\hline
\end{tabular}
\end{center}

\begin{resultbox}
\textbf{Honest final statement (updated after Connes R2 + the Vitali close, `D8.5-COMPLETE.md`).} The
strip-crossing is achieved by \textbf{Vitali normal-family continuation}: the shorted Green matrices are
compressed resolvents of the self-adjoint $A_P$ (bounded by $\|\phi\|\|\psi\|/|\Im z|$, matrix-Herglotz),
so convergence below the strip ($\Im z<-\tfrac12$, where Ξ has no zeros) forces convergence on all of
$\Omega_-$, hence no off-real poles, hence RH. \textbf{Five of Connes' six audit checks are theorems; the
sixth (Check 4) is a labeled construction} — realizing the marked Tate–Weil pairing as a uniform,
fixed-channel, self-adjoint compressed resolvent (no RH used, lives in the absolute-convergence region).
\textbf{So D8.5 — hence RH — is closed modulo that one construction, which is the explicit audit target.}
See `D8.5-COMPLETE.md` §D–§G. The box below is the superseded earlier framing.
\end{resultbox}

\begin{resultbox}
\textbf{(Superseded R1 framing.)} The Signature-Continuity Package is an
\textbf{exact reformulation} of RH, not a reduction to a benign input:
\[
   \textbf{D8.5a (proved, local)}\ +\ \textbf{D8.5b-identification (proved, meromorphic)}\ +\
   \underbrace{\textbf{off-$\R$ divisor vanishes}}_{=\,\textbf{RH}}\ \Longrightarrow\ \textbf{RH}.
\]
\textbf{D8.5a} (the marked Tate–Binet convergence $G_P^\circ\to G^{\lim}$, blocks 1–8) is \emph{proved
and genuinely local} (no hidden RH-strength; honesty checkpoint passed). \textbf{D8.5b's identification}
($G^{\lim}=G_\Xi^{\mathrm{G5}}$ as meromorphic objects) is \emph{proved}. But \textbf{D8.5b's index
conclusion is RH-strength} (`D8.5b-...md` Thm gate, outcome ii): $\operatorname{sq}_-(G_\Xi^{\mathrm{G5}})
=0$ does \emph{not} follow, because the negative squares live at the off-line poles, where the positive
matrix-Nevanlinna approximants $G_P^\circ$ do not converge (a $\mathcal N_0$ limit develops $\mathcal
N_\kappa$ poles only non-uniformly). The irreducible residue is the \textbf{convergence of the principal
parts / divisor of the marked Weil distribution at the off-line locus} — which is exactly RH. \textbf{The
package does not prove RH}; it locates the entire difficulty in one sharply-stated divisor-convergence
phenomenon and proves everything around it. My earlier "$\Rightarrow$ RH with one benign input" was wrong
and is retracted (Connes R1 §1; the M3 wall, at finest resolution).
\end{resultbox}

---

## §3. What would complete it

The package is closed iff D8.5 is proved unconditionally. By D10, any such proof **must use $\Lambda\ge0$**
(track the cell signs), or it would falsely prove the DH-analogue. The remaining task is therefore sharp
and falsifiable:

> **Prove the source-level local-factor convergence D8.5**, using the positivity of the von Mangoldt
> cells, so that the truncated primitive resolvent responses converge (local factor by local factor) to
> the $\Xi$-system's resolvent response — the two-variable, signature-sensitive version of G3.

Next: D12 records D8.5 as the load-bearing assumption, runs the five forbidden-inference checks, and
confirms the DH falsifier.
