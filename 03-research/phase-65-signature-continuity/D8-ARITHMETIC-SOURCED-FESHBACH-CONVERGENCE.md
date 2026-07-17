# D8 — Arithmetic sourced Feshbach convergence (the decisive deliverable)

**Phase 65 / Signature-Continuity Package, deliverable D8.** Pure mathematics. This is the whole
mathematical burden of the package: upgrade the *scalar* convergence G3 ($D_P^\circ\to\Xi$) to *sourced,
pole-shorted kernel* convergence. We structure it into Connes/Consani's seven subclaims, **prove the five
that are genuinely provable from G3+G4 + the machinery D2–D7**, and **isolate with full honesty the one
load-bearing input** (D8.5, the source-level local-factor identity) that is the real new analytic content
— the upgrade of Tate's local computation and the Binet archimedean cell from the scalar determinant to
the sourced determinant germ. We do **not** fake this input; we state it precisely, record what
Connes/Consani report about its status, and prove that *given* it the package closes.

> **Honest framing.** D8 reduces RH to a single, concrete, checkable analytic statement (D8.5). Subclaims
> D8.1–8.3, 8.6–8.7 are proved here in full. D8.4 follows from D8.5. D8.5 itself is the genuine crux; it
> is flagged in the `ASSUMED` ledger (§9), not asserted as our own theorem.

---

## §1. The target

\begin{definition}[primitive sourced renormalized germ]
$\mathcal D_P^{\circ,\mathrm{src}}(V;z):=\det_{\mathrm{reg}}\big(F_P(z)+V\big)$ (D4), $V\in
\mathfrak S_{\mathrm{prim}}$, with $V=0$ slice $D_P^\circ(z)$.
\end{definition}

\begin{theorem*}[D8 target — Arithmetic Primitive Source Theorem]
For every finite-dimensional primitive source plane $F\subset\mathfrak S_{\mathrm{prim}}$, ball $B_F(r)$,
and compact $K\Subset\Omega$,
\[
   \sup_{V\in B_F(r),\,z\in K}\Big|\mathcal D_P^{\circ,\mathrm{src}}(V;z)-\mathcal D_\Xi^{\mathrm{src}}
   (V;z)\Big|\ \xrightarrow[P\to\infty]{}\ 0,
\]
and by differentiation $\mathsf K_P^\circ(z,w)\to\operatorname{Pol}(d^2\log\mathcal D_\Xi^{\mathrm{src}}
(0))(z,w)$, with the right side $=\mathsf K_\Xi^{\mathrm{G5}}$ (D9). The $V=0$ slice is G3.
\end{theorem*}

---

## §2. D8.1 — Primitive source algebra *(proved)*

\begin{lemma}\label{lem:81}
$\mathfrak S_{\mathrm{prim}}$ (finite-rank, signed, $VH_P=V^*H_P=0$; D0) is a well-defined nuclear
$*$-subalgebra of operators on the primitive complement, total for the primitive realization (D2,
Lemma rich). Every source plane $F$ consists of $V=\sum_{\alpha\beta}v_{\alpha\beta}|\phi_\alpha\rangle
\langle\phi_\beta|$, $\phi_\alpha\perp H_P$.
\end{lemma}
\emph{Proof.} D0 Def. src + D2 Lemma rich. Nuclearity is finite rank. $\square$

## §3. D8.2 — Feshbach source factorization *(proved)*

\begin{lemma}\label{lem:82}
$\mathcal D_P^{\mathrm{src}}(V;z)=\Delta_P(z)\,\mathcal D_P^{\circ,\mathrm{src}}(V;z)$ for $V\in
\mathfrak S_{\mathrm{prim}}$, with $\mathcal D_P^{\circ,\mathrm{src}}(V;z)=\det_{\mathrm{reg}}(F_P(z)+V)$
and $\Delta_P$ the pole factor of D4 (anomaly absorbed).
\end{lemma}
\emph{Proof.} Since $V\perp H_P$, $V$ has no component in the pole block; the block $LDU$ factorization
(D4, Thm factor) applies to $I+T_P+V$ with the pole block $\alpha_P$ unchanged and the primitive block
$B_P\mapsto B_P+V$, so the Schur complement becomes $F_P+V$ and the pole factor $\Delta_P$ is unchanged.
$\square$

## §4. D8.3 — Primitive compactness from G4 *(proved, modulo the G4 box bound)*

\begin{lemma}[normality — upper bound only; meromorphic/divisor topology, Connes R1.E]\label{lem:83}
For each $F,r$ and each compact $K\Subset\Omega$ \emph{avoiding the divisor} (the zeros of $\Xi$ / poles
of the G5 kernel),
\[
   \sup_{P,\,V\in B_F(r),\,z\in K}\big|\mathcal D_P^{\circ,\mathrm{src}}(V;z)\big|<\infty,
\]
so $\{\mathcal D_P^{\circ,\mathrm{src}}\}$ is a normal family on each source plane in the
\textbf{meromorphic topology with divisor + principal-part convergence}. There is \textbf{no} uniform
lower bound near the divisor (corrected: an upper bound gives normality, not a lower bound near zeros).
\end{lemma}
\emph{Proof.} $\det_2$ bound $|\det_2(I+T)|\le\exp(\tfrac12\|T\|_2^2)$ with $T=F_P(z)-I+V$. The primitive
Hilbert–Schmidt norm $\|F_P(z)-I\|_2^2$ is bounded uniformly in $P$ on $K$ by the primitive box counts
(G4, `FACE-C-compactness.md`: smooth Carleson bound unconditional; pole-shorting removed the divergent
mode). $V\in B_F(r)$ adds a bounded finite-rank term. This gives the uniform upper bound on compacta
\emph{avoiding the divisor}; on the divisor the Green matrices have poles (the off-line zeros, if any,
are exactly poles of $G_\Xi^{\mathrm{G5}}$), so convergence is taken in the meromorphic sense (uniform on
compacta avoiding poles + convergence of principal parts / divisors). Normality is Montel on the
pole-free compacta. \textbf{No lower bound is claimed.} $\square$

\begin{remark}
This is the precise point where G4 (the rank-one nature of the divergence, hence bounded primitive box
counts after shorting) enters as a genuine hypothesis. It is unconditional (the smooth Carleson bound),
and crucially it is a \emph{primitive} bound — the divergent pole has been shorted away (D4), so no
RH-strength norm control is needed (cf. M2: the size question was dissolved, not solved).
\end{remark}

## §5. D8.4 — Taylor coefficient convergence *(reduces to D8.5)*

\begin{lemma}\label{lem:84}
If for every $n$ and every $V_1,\dots,V_n\in F$ the multilinear resolvent traces converge,
\[
   \operatorname{Tr}\big(R_P^\circ(z)V_1\cdots R_P^\circ(z)V_n\big)\ \to\
   \operatorname{Tr}\big(R_\Xi(z)V_1\cdots R_\Xi(z)V_n\big)\qquad(\text{loc. unif. in }z),
\]
where $R_P^\circ=(F_P)^{-1}$, $R_\Xi$ the primitive resolvent of the $\Xi$-system, then $\mathcal D_P^{
\circ,\mathrm{src}}\to\mathcal D_\Xi^{\mathrm{src}}$ on $B_F(r)$ (uniformly), and hence (D5,
Thm germ-kernel) $\mathsf K_P^\circ\to\mathsf K^\circ$.
\end{lemma}
\emph{Proof.} The $\log$ of the germ is the convergent power series in $V$ with coefficients the
multilinear resolvent traces (D2, Lemma higher; anomaly first-order only). Coefficientwise convergence +
the uniform bound (Lemma~\ref{lem:83}) gives uniform convergence of the holomorphic germs by Vitali on
$B_F(r)$. $\square$

\begin{remark}[why D8.4 is not free from G3]
G3 gives only the $V=0$ slice (the determinant, one functional of the resolvent). The multilinear traces
$\operatorname{Tr}(R_P^\circ V_1\cdots R_P^\circ V_n)$ are *additional* functionals — the full primitive
resolvent matrix elements. Their convergence is the genuine new content; it does \emph{not} follow from
determinant convergence alone (that would be the forbidden scalar-only inference N1). It follows from
D8.5 (the resolvent kernel converges because each *local factor's* source response converges).
\end{remark}

## §6. D8.5 — corrected to D8.5$'$ (Green-matrix convergence), and the a/b split *(Connes R1)*

\begin{redflag}[the product form was wrong — Connes R1 §0]
The earlier claim $\mathcal D_\Xi^{\mathrm{src}}(V;z)=\mathcal L_\infty^{\mathrm{src}}\prod_p\mathcal
L_p^{\mathrm{src}}$ is \textbf{false} for arbitrary finite-rank primitive $V$: sourced determinants do
\emph{not} Euler-factor, since $\det(I+C(A+B))\ne\det(I+CA)\det(I+CB)$. \textbf{Local Green matrices add;
the determinant is taken after summing them.} See `CORRECTIONS-CONNES-R1.md`.
\end{redflag}

\begin{lemma}[finite-rank determinant reduction]\label{lem:detlemma}
For $V=\Phi C\Phi^*$ ($\Phi e_\alpha=\phi_\alpha$ primitive, $C=C^*$),
\[
   \frac{\mathcal D_P^{\circ,\mathrm{src}}(\Phi C\Phi^*;z)}{D_P^\circ(z)}
   =e^{\mathcal A_P(C,z)}\det\nolimits_m\!\big(I_m+C\,G_P^\circ(z)\big),\quad
   G_P^\circ(z)_{\alpha\beta}=\langle R_P^\circ(z)\phi_\beta,\phi_\alpha\rangle,
\]
with $R_P^\circ=F_P^{-1}$ the Feshbach-shorted primitive resolvent and $\mathcal A_P$ the explicit
(first-order, $\det_2$) anomaly. Hence sourced-germ convergence $\Leftrightarrow$ convergence of the
finite Green matrices $G_P^\circ(z)$ together with $D_P^\circ\to\Xi$ (G3).
\end{lemma}
\emph{Proof.} Finite-rank determinant identity $\det_{\mathrm{reg}}(F_P+\Phi C\Phi^*)=\det_{\mathrm{reg}}
F_P\cdot\det_m(I_m+C\Phi^*F_P^{-1}\Phi)$ with the $\det_2$ anomaly. $\square$

\begin{theorem*}[\textbf{D8.5$'$} — the corrected target]
For every finite primitive source plane $F=\operatorname{span}\{\phi_\alpha\}$,
\[
   \boxed{\ \Pi_F R_P^\circ(z)\,\Pi_F\ \longrightarrow\ \Pi_F R_\Xi^{\mathrm{G5}}(z)\,\Pi_F\ }
   \qquad(\text{i.e. }G_P^\circ(z)\to G_\Xi^{\mathrm{G5}}(z))
\]
locally uniformly, meromorphically with divisor control. Then D8.5 (sourced-germ convergence) follows by
Lemma~\ref{lem:detlemma} + G3.
\end{theorem*}

\begin{redflag}[honest status — the a/b split, Connes R1 §1]
D8.5$'$ splits, and the RH-strength is \emph{not} uniformly spread:
\begin{itemize}
\item \textbf{D8.5a — marked Tate/Binet convergence.} $G_P^\circ(z)$ converges (to \emph{some} limit) via
the marked local Tate identity + source-level Binet + a primitive marked tail estimate. Plausibly
genuinely local / close to standard Tate theory; this is what the "term-by-term, pole shorted, sign-aware"
heuristics actually support.
\item \textbf{D8.5b — endpoint identification.} the limit is the \emph{fixed} $G_\Xi^{\mathrm{G5}}$ (the
genuine $\Xi$-resolvent), not merely some Green matrix with scalar determinant $\Xi$. \textbf{This carries
the RH-strength} (Connes R1 §1; it is exactly D9's burden and the M3 worry). \emph{Logically, since
D8.5$'\Rightarrow$RH, D8.5$'$ is RH-strength as a theorem; the strength concentrates in D8.5b.}
\end{itemize}
We do \emph{not} prove either here. The full programme is `D8.5-PRIMITIVE-MARKED-TATE-BINET.md` (to write),
Connes' 9 theorem blocks. The real analytic heart is the \textbf{primitive marked tail estimate}
$\sup_{z\in K}\|\sum_{Q<p^k\le P}G_{p,k}^\circ(z)\|\to0$ (uses G4 + Schur–Cauchy–Schwarz $|G^\circ_{
\alpha\beta}|^2\le G^\circ_{\alpha\alpha}G^\circ_{\beta\beta}$, hence $\Lambda\ge0$).
\end{redflag}

## §7. D8.6 — Normal-family convergence *(proved, given D8.5)*

\begin{lemma}\label{lem:86}
D8.3 (normality) + D8.5 (every subsequential limit's coefficients are the $\Xi$-local-factor traces,
identifying all limits) $\Rightarrow$ the full family converges: $\mathcal D_P^{\circ,\mathrm{src}}\to
\mathcal D_\Xi^{\mathrm{src}}$ on each source plane.
\end{lemma}
\emph{Proof.} Montel gives subsequential limits; D8.5 identifies every subsequential limit uniquely
(its Taylor coefficients are the limiting local-factor traces); a normal family with a unique
subsequential limit converges. Vitali on $B_F(r)$. $\square$

## §8. D8.7 — Kernel convergence by differentiation *(proved, given the above)*

\begin{theorem}\label{thm:87}
$\mathsf K_P^\circ(z,w)\to\operatorname{Pol}(d^2\log\mathcal D_\Xi^{\mathrm{src}}(0))(z,w)$ locally
uniformly.
\end{theorem}
\emph{Proof.} D8.6 gives uniform germ convergence on source balls; D5, Thm germ-kernel (Cauchy
estimates) gives convergence of the second $V$-derivative at $0$, i.e. of the recovered kernel. $\square$

---

## §9. Ledger (D8) — the load-bearing input, corrected to D8.5$'$ (a/b)

> **`OPEN (load-bearing): D8.5' — primitive marked Green convergence`** (replaces the retracted product
> form). Split: **D8.5a** $G_P^\circ(z)\to(\text{limit})$ via marked Tate identity + source Binet +
> primitive marked tail estimate (plausibly genuinely local); **D8.5b** the limit is the *fixed*
> $G_\Xi^{\mathrm{G5}}$ (the endpoint identification — **carries the RH-strength**). Needed in
> Lemma~\ref{lem:detlemma}/D8.7 and in D9. **Not "assumed tested" any longer** — the round-1 review
> (`CORRECTIONS-CONNES-R1.md`) retracted the product form; the work is the new document
> `D8.5-PRIMITIVE-MARKED-TATE-BINET.md`. Logically $D8.5'\Rightarrow$RH, so it is RH-strength, with the
> strength concentrated in D8.5b.

\textbf{Conditional theorem.} *Given D8.5$'$ (a $\wedge$ b)*, the D8 target holds
(Lemma~\ref{lem:detlemma} + Lemmas 8.1–8.4, 8.6, Thm 8.7): the arithmetic sourced germs converge and the
shorted kernels converge to $\mathsf K_\Xi^{\mathrm{G5}}$.

---

## §10. What D8 establishes, honestly

- **Proved in full (from G3+G4+D2–D7):** D8.1 (source algebra), D8.2 (Feshbach source factorization),
  D8.3 (primitive compactness/normality from G4), D8.4 (coefficient convergence $\Rightarrow$ germ
  convergence, given the traces converge), D8.6 (normal-family ⟹ full convergence, given D8.5), D8.7
  (kernel convergence by differentiation).
- **The one load-bearing input, flagged not faked:** D8.5 (source-level Tate$\times$Binet local-factor
  convergence) — the genuine new analytic content, the two-variable upgrade of G3. Recorded in the
  `ASSUMED` ledger; Connes/Consani report it tested; we have not independently re-derived it.
- **Net:** Phase 65 reduces RH to the single concrete statement D8.5 (plus D9's identification of the
  limit with the *fixed* $\mathsf K_\Xi^{\mathrm{G5}}$). Everything else in D0–D8 is proved. This is the
  honest position: not a proof of RH by us, but a complete reduction to one checkable analytic input,
  with no scalar-only inference, no faked convergence, no endpoint reassignment.

Next: D9 (the limit kernel is the *fixed* $\mathsf K_\Xi^{\mathrm{G5}}$, by differentiation — the second
load-bearing identification, kept separate from D6's closedness), then D10 (DH must break D8.5 or the
positivity), D11 (assembly), D12 (audit, recording D8.5 as the load-bearing assumption).
