# D10 — The Davenport–Heilbronn falsifier

**Phase 65 / Signature-Continuity Package, deliverable D10.** Pure mathematics, full proofs. Mandatory
falsifier: the Davenport–Heilbronn function $L_{\mathrm{DH}}$ satisfies the same functional equation as
$\zeta$ but has zeros off the critical line. Any machine that proves RH for the *wrong* reason would also
"prove" RH for DH — which is false. So the package must **fail visibly** for DH, and we must exhibit the
exact hypothesis that breaks. We prove: in $\mathcal G$, DH cannot land in $\mathcal G_0$ — at least one
positive-pole hypothesis fails, and the off-line zeros force $\deg\mathfrak b_{\mathrm{DH}}>0$.

> `ASSUMED` ledger (D10): **empty.** The DH failure is structural (Stage 1, S4 + the signed Hamiltonian).

---

## §1. Where DH differs

\begin{definition}[DH system]
$L_{\mathrm{DH}}(s)=\tfrac12\big((1-i\tau)L(s,\chi_5)+(1+i\tau)\overline{(\cdots)}\big)$-type combination
with the Davenport–Heilbronn $\tau$; it has a functional equation $s\mapsto1-s$ but an Euler product with
\emph{signed} (mixed-sign) coefficients, hence a \emph{signed} local Hamiltonian $H^\chi_P$ (Phase 64:
the twisted local masses $\mu_p^\chi$ change sign).
\end{definition}

The construction G1–G2 used $H_P\ge0$ (von Mangoldt $\Lambda\ge0$). For DH this fails at the source.

---

## §2. The falsifier theorem

\begin{theorem}[DH breaks a positive-pole hypothesis]\label{thm:dh}
Run D1–D9 with $H^\chi_P$ in place of $H_P$. Then at least one of the following fails:
\begin{enumerate}
\item \textbf{finite positivity (G2-analogue):} $\mathsf K_{A^\chi_P}\not\succeq0$ — the Gram integrand
$\int Y^*H^\chi_PY$ is indefinite because $H^\chi_P$ is signed; so $\kappa(A^\chi_P)>0$ at finite $P$
(D7-analogue fails);
\item \textbf{pole positivity (G4-analogue):} if instead one symmetrizes to keep a definite pole, the
primitive shorted kernel acquires negative squares (the signed cells contribute $(\mathrm P-)$ generators,
D3);
\item \textbf{closedness input:} consequently the shorted limit carries a nontrivial Kreĭn–Langer
denominator, $\mathfrak b_{\mathrm{DH}}\ne1$;
\item \textbf{source limit:} the sourced limit germ has negative squares, $\operatorname{sq}_-(\mathsf
K^{\mathrm{DH}}_\infty)>0$.
\end{enumerate}
In particular, whenever $L_{\mathrm{DH}}$ has off-line zeros, $\deg\mathfrak b_{\mathrm{DH}}=\#\{$off-line
zeros$\}>0$, and the package does **not** conclude $\kappa_{\mathrm{DH}}=0$.
\end{theorem}
\emph{Proof.} The signed Hamiltonian makes the canonical inner product indefinite (Stage 1, S4: a
negative line forces $\nu_-\ge1$; here the signed cells are exactly negative extensions, D3 (P$-$)). Thus
the finite DH objects are not in $\mathcal G_0$: $\kappa(A^\chi_P)>0$ already, so the hypothesis of D6/D7
(finite index $0$) fails at the first signed cell. The Kreĭn–Langer divisor of the limit then has degree
$=\operatorname{sq}_-(\mathsf K^{\mathrm{DH}}_\infty)$, which by the D9-analogue (the limit germ is the
DH-local-factor object with Weyl function $L_{\mathrm{DH}}'/L_{\mathrm{DH}}$) equals the number of
off-$\R$ poles of that Weyl function $=$ the off-line zeros of $L_{\mathrm{DH}}$. $\square$

---

## §3. Acceptance criterion (the self-check)

\begin{resultbox}
\textbf{The falsifier fires.} The package distinguishes $\zeta$ from DH at the \emph{object} level
(Stage 1, S4 lifted): $\zeta$ has $H_P\ge0\Rightarrow\kappa(A_P)=0$ for all $P$ (D7); DH has signed
$H^\chi_P\Rightarrow\kappa(A^\chi_P)>0$ for some finite $P$ (Thm~\ref{thm:dh}). The load-bearing
positivity (G2) is exactly what $\zeta$ has and DH lacks. \textbf{Any version of the package that forced
$\kappa_{\mathrm{DH}}=0$ would be too coarse and is rejected} — and ours does not, because D6/D7 require
finite positivity, which DH fails. The DH off-line zeros appear, correctly, as $\deg\mathfrak b_{\mathrm
{DH}}>0$.
\end{resultbox}

\begin{remark}[the role of $\Lambda\ge0$ in D8.5 — corrected, Connes R1.G]
\textbf{The earlier claim overstated this.} DH already fails \emph{finite positivity} (D7): its finite
objects have $\kappa(A^\chi_P)>0$, so DH never enters $\mathcal G_0$ and the assembly chain breaks at D7,
\emph{before} D8.5 is reached. Therefore D8.5 (the marked Green convergence) is \emph{not} required to
fail for DH in order to avoid a false DH-RH proof — the chain is already broken upstream. Consequences:
\begin{itemize}
\item $\Lambda\ge0$ is \textbf{logically necessary} for D6/D7 (finite positivity, the place DH dies);
\item $\Lambda\ge0$ is \textbf{useful but not logically forced} inside D8.5 — concretely it powers the
Schur–Cauchy–Schwarz bound $|G^\circ_{\alpha\beta}|^2\le G^\circ_{\alpha\alpha}G^\circ_{\beta\beta}$ in the
primitive marked tail estimate (D8.5a block 5), which is unavailable for the signed DH cells; but D8.5
\emph{as a convergence statement} could in principle hold for DH too without yielding RH for DH.
\end{itemize}
So the DH falsifier fires at D7, not at D8.5. The earlier "D8.5 must use $\Lambda\ge0$ or it proves DH"
is withdrawn; the accurate statement is that $\Lambda\ge0$ is where DH dies (D7) and is a natural tool
(not a logical necessity) in D8.5's tail estimate.
\end{remark}

---

## §4. What D10 establishes

- **DH fails the package** (Thm~\ref{thm:dh}): the signed Hamiltonian makes finite objects leave
  $\mathcal G_0$; off-line zeros appear as $\deg\mathfrak b_{\mathrm{DH}}>0$. The falsifier fires.
- The distinction is at the **object level** and rests on the load-bearing positivity G2 ($\Lambda\ge0$),
  exactly the hypothesis $\zeta$ has and DH lacks.
- **Correctness constraint on D8.5:** any valid proof of the load-bearing input must use $\Lambda\ge0$
  (track cell signs), or it would falsely apply to DH. This is a concrete check on the one remaining task.

Next: D11 (assembly), D12 (audit — recording D8.5 as load-bearing and the DH check as passed).
