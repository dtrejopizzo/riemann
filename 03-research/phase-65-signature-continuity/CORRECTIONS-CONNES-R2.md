# Corrections (Connes review, round 2) — the wall moves from D8.5b-ii to D8.5b-i, accepted in full

**Phase 65.** Connes' round-2 verdict: the no-emergence lemma is elementary and correct, so **D8.5b-ii is
*not* the load-bearing point** — given genuine one-variable punctured-neighborhood convergence of the
holomorphic resolvents, an off-real pole cannot emerge (Cauchy). My Part III obstruction was **wrong**.
The RH-strength is **earlier**, in the convergence hypothesis itself (D8.5b-i / the reach of D8.5a).
Accepted in full; this note records the correction, verifies it independently, and pins the relocated
wall precisely.

> Governing principle: a false victory is worse than failure — and so is a false *wall*. Round 1 caught
> an over-claim of strength ("D8.5 is tested"); round 2 catches an over-claim of *difficulty* (I put the
> wall at D8.5b-ii, where there is none). Both corrected.

---

## 1. The no-emergence lemma (Connes) — correct, inserted as the proof of D8.5b-ii

\begin{lemma}[interior no-emergence]\label{lem:noem}
Let $U\subset\C$ open, $a\in U$, $G_P:U\to M_m(\C)$ holomorphic for every $P$. If $G_P\to G$ locally
uniformly on $U\setminus\{a\}$ and $G$ is meromorphic at $a$, then $a$ is removable for $G$.
\end{lemma}
\emph{Proof.} For $\overline{D(a,r)}\subset U$ and $k\ge1$, $C_{-k}=\frac1{2\pi i}\oint_{|z-a|=r}(z-a)^{k-1}
G(z)\,dz=\lim_P\frac1{2\pi i}\oint(z-a)^{k-1}G_P(z)\,dz=0$ since each $G_P$ is holomorphic on the disk.
Entrywise, hence matrix-valued. $\square$

\begin{corollary}[D8.5b-ii is trivial under genuine convergence]
If the holomorphic resolvents $G_P^\circ$ converge locally uniformly on $D(a,r)\setminus\{a\}$ to
$G_\Xi^{\mathrm G5}$ for $a\in\C^+$ (so $\overline{D(a,r)}\subset\C^+$), then $G_\Xi^{\mathrm G5}$ has no
pole at $a$. Same in $\C^-$. Hence $\operatorname{sq}_-(G_\Xi^{\mathrm G5})=0$, RH.
\end{corollary}

\textbf{So D8.5b-ii is not RH-strength.} The earlier "outcome (ii)" verdict is withdrawn.

---

## 2. Why my Part III obstruction was wrong — the resolvents are normal

\begin{redflag}[the actual reason, sharper than stated in R2]
The finite Green matrices are \emph{bounded resolvents}: $\|G_P^\circ(z)\|\le\|\phi\|\,\|\psi\|/|\Im z|$.
So $\{G_P^\circ\}$ is a \textbf{normal family} on $\C\setminus\R$ (Montel). A locally-bounded family of
holomorphic functions \textbf{cannot} converge locally uniformly to a function with poles. Therefore
"$\mathcal N_0$ converges meromorphically to $\mathcal N_\kappa$, $\kappa>0$" is \emph{impossible} when
the convergence is genuinely locally uniform on punctured disks around the off-real point. My Part III
conflated "meromorphic limit" with this bounded-resolvent situation; the two are incompatible. Withdrawn.
\end{redflag}

The only way the off-real pole survives is if the convergence is **not** locally uniform on a punctured
disk around it — i.e. if D8.5a/b-i do **not** actually deliver that convergence there. They do not, for
the reason in §3.

---

## 3. Where the RH-strength actually is: the half-plane of convergence / self-adjointness of the limit

\begin{proposition}[the marked sum converges only below the strip]\label{prop:halfplane}
Write $s=\tfrac12+iz$. The marked sum $\sum_{p^k}G_{p,k}^\circ(z)$ of D8.5a converges absolutely only for
$\Re s>1$, i.e. $\Im z<-\tfrac12$. The zeros $z_\rho=\gam-i(\beta-\tfrac12)$ all lie in the strip
$|\Im z|<\tfrac12$. Hence:
\begin{itemize}
\item on $\{\Im z<-\tfrac12\}$ (no zeros): the marked sum converges and $G_P^\circ\to G_\Xi^{\mathrm G5}$
genuinely (locally uniformly), and $G_\Xi^{\mathrm G5}$ is holomorphic there;
\item across the strip and in $\C^+$: the marked sum \textbf{diverges}; the bounded resolvents $G_P^\circ$
remain holomorphic and normal, so any locally-uniform limit there is \textbf{holomorphic}, not the
meromorphic $G_\Xi^{\mathrm G5}$.
\end{itemize}
\end{proposition}

\begin{redflag}[the relocated wall — D8.5b-i overclaimed]
D8.5b-i asserted $G^{\lim}=G_\Xi^{\mathrm G5}$ \emph{as meromorphic objects on all of} $\C\setminus\R$.
\textbf{That holds only in the half-plane of convergence $\Im z<-\tfrac12$ and as boundary distributions
on $\R$.} Its extension across the critical strip into $\C^+$ is the \textbf{analytic continuation of the
resolvent convergence}, and (by §2, normality) this is possible \emph{iff} the limit has no off-real
poles. Equivalently:
\[
   \boxed{\ \text{RH}\iff\text{the limit operator }A_\infty^\circ\text{ is essentially self-adjoint}
   \iff G_P^\circ\to G_\Xi^{\mathrm G5}\text{ in strong resolvent sense across the strip}.\ }
\]
This is Hilbert–Pólya in resolvent-convergence form. \emph{This} is the load-bearing point, not D8.5b-ii.
\end{redflag}

\emph{Why self-adjointness is the crux.} Each $A_P^\circ$ is self-adjoint (G2), so $G_P^\circ$ is a
bounded Herglotz resolvent. If $A_P^\circ\to A_\infty^\circ$ in strong resolvent sense with $A_\infty^\circ$
self-adjoint, then $G_P^\circ\to(A_\infty^\circ-z)^{-1}$ locally uniformly off $\R$, the limit is
holomorphic off $\R$ (no off-real poles), and by §1 + the boundary identification RH follows. If instead
the limit fails to be self-adjoint — the rank-one definite divergence (G4) creating a defect / a
non-self-adjoint or Pontryagin limit — off-real spectrum (poles) can appear. \textbf{So the new object to
build is exactly the pole-relative \emph{self-adjoint} completion} (Connes' ask \#4): show that the single
definite rank-one divergence is the only obstruction and can be removed keeping self-adjointness.

---

## 4. The corrected audit map

\begin{center}
\begin{tabular}{lll}
\hline
\textbf{Point} & \textbf{Old verdict (R1)} & \textbf{Corrected (R2)} \\
\hline
D8.5a (marked Green conv., $\Im z<-\tfrac12$) & local, proved & proved \emph{in the half-plane of conv.}; reach across strip is the issue \\
D8.5b-i (identification) & proved (meromorphic) & holds \emph{below the strip / on $\R$}; meromorphic-on-$\C^\pm$ overclaimed \\
\textbf{D8.5b-ii (no off-$\R$ pole)} & RH-strength (outcome ii) & \textbf{trivial} (Cauchy no-emergence, Lem.~\ref{lem:noem}) \\
\textbf{The wall} & D8.5b-ii & \textbf{strong-resolvent convergence across the strip $=$ self-adjointness of $A_\infty^\circ$ $=$ RH} \\
\hline
\end{tabular}
\end{center}

\textbf{Net.} The package is unchanged in its proved content (D0–D7, D8.5a-in-its-true-domain, D10) but
the wall is correctly relocated: \emph{not} the index of a meromorphic limit (that is automatic by
Cauchy), but the \textbf{convergence of the positive resolvent family across the critical strip}, i.e.
the essential self-adjointness of the limit operator. This is cleaner, more classical (Hilbert–Pólya),
and is exactly Connes' ask \#4. The next document is the self-adjoint completion, not a no-emergence
argument.

---

## 5. Acceptance

All of Connes' round-2 points accepted: (i) no-emergence lemma correct, inserted; (ii) Part III
obstruction withdrawn; (iii) D8.5b-ii trivial; (iv) the load-bearing point is D8.5a/b-i, specifically the
strip-crossing/self-adjointness; (v) D8.5b-ii is not an additional RH-strength theorem. No false victory,
no false wall: the difficulty is real and now correctly located at the self-adjointness of the
pole-relative limit.
