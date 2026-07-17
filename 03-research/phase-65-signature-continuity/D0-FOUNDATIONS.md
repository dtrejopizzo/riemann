# D0 — Foundations ledger: conventions, the fixed endpoint kernel, admissible sources, and the no-circularity discipline

**Phase 65 / Signature-Continuity Package, deliverable D0.** Pure mathematics, no computation. This
document freezes the language *before* any construction, so that no later step can smuggle in RH. It
fixes: (i) the spectral variable and determinant conventions; (ii) **the endpoint kernel
$\mathsf K_\Xi^{\mathrm{G5}}$, pinned now, once and for all, before any limit is taken**; (iii) the
admissible finite-rank source class and the positive pole line $H$; (iv) the dependency ledger recording
exactly where the given facts G1–G5 (proved in Phases 60–64) enter; (v) the `ASSUMED` ledger template.

> **Governing principle.** A false victory is worse than failure. The endpoint kernel is fixed here; the
> theorem to prove (D9) is that a certain *limit* equals this *pre-fixed* object — never that the limit
> *defines* it. Every use of G1–G5 is logged; **no step may use RH or the location of the zeros of
> $\Xi$.**

---

## §1. Spectral variable and the function $\Xi$

\begin{convention}[spectral variable]
Write $s=\tfrac12+iz$, so the critical line $\Re s=\tfrac12$ is the real axis $z\in\R$, and a nontrivial
zero $\rho=\beta+i\gam$ of $\zeta$ corresponds to $z_\rho=\gam-i(\beta-\tfrac12)$. The functional equation
$s\mapsto1-s$ is $z\mapsto-z$. RH $\Leftrightarrow$ all $z_\rho\in\R$.
\end{convention}

\begin{convention}[completed function]
$\Xi(z):=\xi(\tfrac12+iz)$ where $\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(\tfrac s2)\zeta(s)$. Then $\Xi$
is entire of order $1$, real on $\R$, even ($\Xi(-z)=\Xi(z)$), and its zeros are the $z_\rho$.
RH $\Leftrightarrow\Xi$ has only real zeros.
\end{convention}

\begin{convention}[regularized determinant]
$\det_{\mathrm{reg}}$ denotes the $2$-modified (Carleman) determinant $\det_2$ unless stated otherwise;
$\zeta$-regularization is used for the archimedean cell. \textbf{All multiplicative anomalies are tracked
explicitly} (the anomaly term $\mathcal A_n$ of D2; the pole-factor anomaly absorbed into $\Delta_P$ of
D4). No identity below silently assumes the anomaly vanishes.
\end{convention}

---

## §2. The endpoint kernel $\mathsf K_\Xi^{\mathrm{G5}}$ — fixed now, before any limit

This section exists to prevent the single most dangerous circularity: *defining* a positive kernel as the
limit and then *calling* its index $\kappa(\Xi)$. We forbid that by pinning the endpoint object here.

\begin{definition}[negative squares]\label{def:sq}
A Hermitian kernel $\mathsf K$ on a domain $\Omega$ (matrix- or scalar-valued) has \textbf{at most
$\kappa$ negative squares} if for every finite $z_1,\dots,z_m\in\Omega$ and vectors $u_1,\dots,u_m$ the
Gram matrix $G_{ij}=\langle\mathsf K(z_i,z_j)u_j,u_i\rangle$ has at most $\kappa$ strictly negative
eigenvalues; \textbf{exactly $\kappa$} if some finite Gram matrix attains $\kappa$. Write
$\operatorname{sq}_-(\mathsf K)=\kappa$.
\end{definition}

\begin{definition}[the fixed endpoint kernel — sign corrected, Connes R1.A]\label{def:KG5}
Let $M_\Xi(z):=-\,\Xi'(z)/\Xi(z)$ (the \emph{Herglotz} log-derivative coordinate; the sign is essential,
see below), meromorphic on $\C\setminus\R$ with poles exactly at the zeros $z_\rho$. Define
\[
   \boxed{\ \mathsf K_\Xi^{\mathrm{G5}}(z,w):=\frac{M_\Xi(z)-\overline{M_\Xi(w)}}{z-\bar w}\ }
\]
(the generalized Nevanlinna kernel of $M_\Xi$), equivalently the de Branges kernel of the
Hermite–Biehler companion $E_\Xi$ of $\Xi$. This is the \textbf{G5 kernel}: defined directly from $\Xi$
by classical formulas, with no reference to any canonical system, limit, or positivity assumption.

\emph{Sign (corrected).} With $M=+\Xi'/\Xi$ the kernel has the wrong sign — a real zero contributes a
\emph{negative} square (check $F(z)=z$, $M=1/z$, $z=w=i$: $(M(i)-\overline{M(i)})/(i-\bar i)=(-i-i)/(2i)
=-1$); indeed $1/z$ is anti-Herglotz on $\C^+$. Using $M_\Xi=-\Xi'/\Xi$ (Herglotz, $\Im(-1/z)>0$ on
$\C^+$) makes real zeros contribute \emph{positively}, while nonreal (off-line) zeros produce the
Kreĭn–Langer negative squares — as required.
\end{definition}

\begin{proposition}[G5 restated]\label{prop:g5}
$\operatorname{sq}_-\!\big(\mathsf K_\Xi^{\mathrm{G5}}\big)=\#\{\rho:\zeta(\rho)=0,\ \Re\rho\ne\tfrac12\}
=:\kappa(\Xi)$, with the standard counting (functional-equation/conjugate symmetry collapses each
off-line quadruple appropriately). This is the Kreĭn–Langer index of $M_\Xi$; it is the *given* G5
(Phase 64, E108). RH $\Leftrightarrow\kappa(\Xi)=0$.
\end{proposition}

\begin{redflag}
The target theorem D9 is $\displaystyle\lim_P\operatorname{Short}_{H_P}\mathsf K_{A_P}=
\mathsf K_\Xi^{\mathrm{G5}}$, with the right-hand side the object of Def.~\ref{def:KG5}, fixed here.
\textbf{It is forbidden} to set $\mathsf K_\Xi:=\lim_P\operatorname{Short}_{H_P}\mathsf K_{A_P}$ and then
assert its index is $\kappa(\Xi)$; D9 must prove equality with the pre-fixed Def.~\ref{def:KG5}.
\end{redflag}

---

## §3. The canonical systems, the pole line, and admissible sources

\begin{definition}[the given systems $A_P$]
For each finite $P$, $A_P$ is the self-adjoint canonical operator of the positive von Mangoldt
Hamiltonian $H_P=\sum_{p^k\le P^2}(\log p)p^{-k/2}|v_{p,k}\rangle\langle v_{p,k}|\,\delta_{k\log p}\ge0$
(G1). Its reproducing kernel is $\mathsf K_{A_P}(z,w)=\int_0^{\ell_P}Y_P(t,w)^*H_P(t)Y_P(t,z)\,dt
\succeq0$ (G2, canonical Gram identity).
\end{definition}

\begin{definition}[pole line $H$]\label{def:pole}
$H$ is the constant/degree mode carrying the divergent trace, $\langle H,K_PH\rangle\sim\tfrac12(\log P)^2$
(G4). It is \textbf{positive}: $[H,H]_{A_P}>0$. Its normalization is $\hat h_P=H/\|H\|$; the primitive
projection is $Q_P=I-|\hat h_P\rangle\langle\hat h_P|$. The pole is rank-one and definite-signed (G4).
\end{definition}

\begin{definition}[admissible primitive sources $\mathfrak S_{\mathrm{prim}}$]\label{def:src}
An \textbf{admissible source} is a finite-rank operator $V=\sum_{\alpha,\beta}v_{\alpha\beta}
|\phi_\alpha\rangle\langle\phi_\beta|$ with all $\phi_\alpha\perp H$ (so $VH=V^*H=0$: sources live on the
primitive complement) and $v_{\alpha\beta}=\overline{v_{\beta\alpha}}$ allowed of \emph{either} sign
(signed probes). $\mathfrak S_{\mathrm{prim}}$ is the (nuclear) space of such $V$; a \textbf{source plane}
$F\subset\mathfrak S_{\mathrm{prim}}$ is a finite-dimensional subspace. The sourced determinant germ of
D2 is the holomorphic map $V\mapsto\det_{\mathrm{reg}}(I+A_P+V)$ on a neighborhood of $0$ in each $F$.
\end{definition}

\begin{remark}[why signed probes on the primitive complement]
Signed probes are what read off the *signature* of the kernel (a positive-only probe could not detect a
negative square); restricting to $\phi\perp H$ keeps the probe away from the divergent pole, so the
sourced germ stays finite after pole-shorting. Source richness (totality of $\mathfrak S_{\mathrm{prim}}$
for the primitive kernel) is a named lemma to be proved in D2; without it, sourced convergence would
control the kernel only on a subspace.
\end{remark}

---

## §4. Dependency ledger: where G1–G5 enter, and what is forbidden

\begin{center}
\begin{tabular}{lll}
\hline
\textbf{Given} & \textbf{Statement (proved Phases 60–64)} & \textbf{Used in} \\
\hline
G1 & positive von Mangoldt canonical system $H_P\ge0$, $\det Y_P\equiv1$ & D7 \\
G2 & Gram identity $\mathsf K_{A_P}=\int Y^*H_PY\succeq0$; finite HB, $\kappa(A_P)=0$ & D7, D6 \\
G3 & $\mathrm{ren\text{-}lim}_PD_P=\Xi$ (Tate $\times$ Binet, unconditional) & D8 ($V=0$ case) \\
G4 & divergence rank-one, definite $+$, on the pole mode $H$; primitive box bounds & D4, D8.3 \\
G5 & $\kappa(\Xi)=\#\{$off-line zeros$\}$ (Prop.~\ref{prop:g5}) & D0 (Def.~\ref{def:KG5}), D9, D11 \\
\hline
\end{tabular}
\end{center}

\begin{redflag}[forbidden moves — enforced by D12]
\begin{enumerate}
\item \textbf{No scalar-only inference:} never infer $\mathsf K_P^\circ\to\mathsf K_\Xi$ from
$D_P^\circ\to\Xi$ alone (that is N1, signature-blindness — the whole reason D2 exists).
\item \textbf{No fake index:} never set $\kappa(A_\infty):=\lim_P\kappa(A_P)$.
\item \textbf{No naive subtraction:} the pole is removed by Feshbach/Schur \emph{shorting} (D4), never by
subtracting the pole block (which creates spurious negative squares; the $G_R$ counterexample, Stage 1).
\item \textbf{No endpoint reassignment:} $\mathsf K_\Xi^{\mathrm{G5}}$ is Def.~\ref{def:KG5}; D9 proves
equality, never assigns.
\item \textbf{No anomaly omission:} every $\det_2/\zeta$ anomaly is carried explicitly.
\item \textbf{No use of RH or zero locations} of $\Xi$ anywhere except the final substitution via G5.
\end{enumerate}
\end{redflag}

---

## §5. The `ASSUMED` ledger (template, per-document)

Default posture (plan decision 2): **full proofs**. When a Connes/Consani-tested input is genuinely
needed and not re-derivable inline, it is used and logged here in the document that uses it, in the form:

> `ASSUMED (Connes/Consani, tested): <precise statement>. — needed in <step>; re-derivation deferred
> because <reason>; does not use RH.`

D12 collects all `ASSUMED` entries across documents into a single audited list. An empty ledger in a
document means it is fully self-contained. **D0 itself assumes nothing beyond G1–G5** (which are the
proved Phase 60–64 inputs, themselves logged in the program's prior records).

---

## §6. Acceptance criterion for D0

D0 is complete iff:
\begin{itemize}
\item the endpoint kernel $\mathsf K_\Xi^{\mathrm{G5}}$ is fixed (Def.~\ref{def:KG5}) \emph{before} any
construction or limit;
\item the index $\kappa(\Xi)$ is identified with off-line zeros via G5 (Prop.~\ref{prop:g5}), not via any
new positivity;
\item the pole line $H$ and admissible sources $\mathfrak S_{\mathrm{prim}}$ are defined;
\item the dependency ledger (§4) and the forbidden-move list are in force for all of D1–D12.
\end{itemize}
All four hold. D0 is the fixed frame; construction begins at the finite-dimensional sanity model
(Stage 1) and D1.
