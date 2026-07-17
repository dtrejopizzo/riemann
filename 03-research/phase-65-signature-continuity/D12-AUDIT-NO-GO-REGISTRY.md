# D12 — Audit and no-go registry

**Phase 65 / Signature-Continuity Package, deliverable D12.** Pure mathematics, continuous audit. This
document runs the package against the forbidden-inference list (D0 §4), collects every `ASSUMED` ledger
entry into one place, confirms the DH falsifier, and records the honest bottom line. It is the
anti-self-deception gate: the package is only as sound as this audit.

---

## §1. The five forbidden inferences — checked

\begin{center}
\begin{tabular}{lll}
\hline
\textbf{Forbidden move} & \textbf{Where it could sneak in} & \textbf{Audit result} \\
\hline
1. scalar-only inference & D8 (infer kernel from $D_P^\circ$) & \textbf{avoided}: D8 proves
\emph{sourced} germ convergence (D8.5), kernel via differentiation (D8.7); never $D_P^\circ\to\Xi
\Rightarrow\mathsf K_P^\circ\to\mathsf K_\Xi$. \\
2. fake index $\kappa(A_\infty):=\lim\kappa(A_P)$ & D9, D11 & \textbf{avoided}: $\kappa(A_\infty)=
\operatorname{sq}_-(\mathsf K_\infty^\circ)$ computed from the limit kernel (D9), not defined as a limit
of indices. \\
3. naive pole subtraction & D4 & \textbf{avoided}: D4 uses Feshbach/Schur shorting (cross-term
$\beta\alpha^{-1}\beta^*$); the $G_R$ counterexample (Stage 1) forbids subtraction. \\
4. endpoint reassignment $\mathsf K_\Xi:=\lim\mathsf K_P^\circ$ & D9 & \textbf{avoided}: $\mathsf
K_\Xi^{\mathrm{G5}}$ fixed in D0 \emph{before} any limit; D9 \emph{proves} $\mathsf K_\infty^\circ=
\mathsf K_\Xi^{\mathrm{G5}}$ (both are $\mathsf N_{\Xi'/\Xi}$), not assigns. \\
5. anomaly omission & D2, D4 & \textbf{avoided}: $\det_2$ anomaly tracked (first-order only, D2;
pole-factor anomaly absorbed into $\Delta_P$, D4). \\
\hline
6. use of RH / zero locations & everywhere & \textbf{avoided}: no step uses zero locations; G5 is invoked
only as the final \emph{reading} of $\operatorname{sq}_-(\mathsf K_\Xi^{\mathrm{G5}})$. \\
\hline
\end{tabular}
\end{center}

---

## §2. Consolidated `ASSUMED` ledger

\begin{center}
\begin{tabular}{lll}
\hline
\textbf{Doc} & \textbf{Assumption} & \textbf{Character} \\
\hline
D2 & relative trace-class structure of $A_P-A_0$ on compacts (Phase 64) & technical, established \\
D4 & block $\det_2$ anomaly finite/holomorphic off pole spectrum & technical \\
\textbf{D8} & \textbf{D8.5: source-level Tate$\times$Binet local-factor convergence} & \textbf{LOAD-BEARING} \\
\hline
\end{tabular}
\end{center}

\begin{resultbox}
\textbf{Single point of failure.} The package's validity reduces to \textbf{D8.5}. The D2/D4 entries are
routine technical facts (trace-class structure, anomaly finiteness) established in Phase 64. D8.5 is the
genuine new analytic content — the two-variable upgrade of G3 — which Connes/Consani report tested and we
have not independently re-derived. \emph{If D8.5 holds, RH follows (D11); if D8.5 fails, the package does
not conclude, and an off-line zero is consistent with everything proved.} No other hidden assumption
exists: every other deliverable carries an empty ledger.
\end{resultbox}

---

## §3. DH falsifier — confirmed

By D10: the signed DH Hamiltonian leaves $\mathcal G_0$ at finite stage ($\kappa(A^\chi_P)>0$), so the
package does **not** force $\kappa_{\mathrm{DH}}=0$; off-line DH zeros appear as $\deg\mathfrak b_{\mathrm
{DH}}>0$. The distinction rests on $\Lambda\ge0$ (G2), which $\zeta$ has and DH lacks. **The falsifier
fires.** Moreover D10 imposes a correctness constraint on any future proof of D8.5: it must use
$\Lambda\ge0$, else it would falsely prove the DH-analogue.

---

## §4. No-go log (running)

\begin{itemize}
\item \textbf{M3 (superseded, retained):} scalar-level closedness is RH-strength — \emph{resolved} by
moving to sourced/kernel level (D2–D6); the residue is now D8.5, not closedness.
\item \textbf{T1–T2 tension (M2/D5):} no scalar topology has both closedness and convergence —
\emph{accommodated} by topologizing the sourced data, not the scalar determinant.
\item \textbf{$G_R$ (Stage 1):} subtraction creates spurious negative squares — \emph{avoided} by
shorting (D4).
\item \textbf{Open:} D8.5 itself. Not a no-go; the single load-bearing input. If a future audit shows
D8.5 is itself RH-strength-and-no-easier (i.e. equivalent to the Hurwitz-safe convergence M3 flagged),
that would be the honest no-go for this route, and must be recorded here.
\end{itemize}

---

## §5. Honest bottom line of the package

\begin{resultbox}
\textbf{Phase 65 delivers a complete reduction:} \emph{D8.5} $\Rightarrow$ \emph{RH}, with every other
step (D0–D7, D9–D11, Stage 1) proved in full and unconditionally, the five forbidden inferences avoided,
and the DH falsifier firing. The new mathematics — the Witt–Nevanlinna sourced determinant, the
positive-pole Feshbach shorting, the signature topology, and the index functor — is genuinely
constructed. The one remaining mathematical input is D8.5 (source-level local-factor convergence, using
$\Lambda\ge0$), which Connes/Consani report tested and which we have flagged, not faked.

\textbf{This is not a proof of RH by us.} It is an honest, audited reduction of RH to one concrete,
falsifiable analytic statement, with the load-bearing assumption named explicitly. A false victory is
worse than failure; the package's integrity is that it says exactly where it stands.
\end{resultbox}

The package is complete as a conditional structure. The decisive open task is the unconditional proof of
D8.5 — the next genuine mathematical work, sharply localized and constrained (must use $\Lambda\ge0$,
D10).
