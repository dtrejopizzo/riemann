# D6 — Positive-pole closedness: index zero is closed in $\tau_\kappa$

**Phase 65 / Signature-Continuity Package, deliverable D6.** Pure mathematics, full proofs. This is M3 in
its correct form. It absorbs and supersedes `M3-signature-closedness.md` — whose honest finding (closedness
is RH-strength *at the scalar level*) is exactly *why* D2–D5 moved everything to the sourced/kernel level.
With the D4 shorting and the D5 kernel topology, closedness becomes a clean **Schur-complement positivity
theorem**: a $\tau_\kappa$-limit of positive shorted kernels is positive. The decisive arithmetic content
(that the limit kernel is the *fixed* endpoint $\mathsf K_\Xi^{\mathrm{G5}}$, not merely *some* positive
kernel) is **not** here — it is D8/D9. D6 proves only: *if* the shorted kernels converge to the endpoint,
*then* the endpoint has index $0$.

> **M3 preserved (the motivation).** Scalar-level closedness is RH-strength; the cure is to work with the
> shorted kernel $\mathsf K_P^\circ$ (D4) in the topology $\tau_\kappa$ (D5), where closedness is
> Schur-complement positivity (Stage 1, S3 lifted). The RH-strength residue M3 identified is now isolated
> as the *convergence* D8, not the *closedness* D6.

> `ASSUMED` ledger (D6): **empty.**

---

## §1. The closedness theorem (index $0$)

\begin{theorem}[positive-pole closedness]\label{thm:closed}
Let $\mathbf X_i\in\mathcal G_0$ (so $\mathsf K_i^\circ\succeq0$, $\kappa=0$) and $\mathbf X_i\to\mathbf X$
in $\tau_\kappa$. Then $\mathbf X\in\mathcal G_0$: $\mathsf K^\circ\succeq0$ and $\kappa(\mathbf X)=0$.
\end{theorem}
\emph{Proof.} Fix any finite $z_1,\dots,z_m\in\Omega$ and coefficients $c_1,\dots,c_m\in\C$. For each $i$,
the shorted kernel has the realization $\mathsf K_i^\circ(z,w)=[Q_i\Gamma_i(z),Q_i\Gamma_i(w)]_i$ (D4,
Def. short), with $[\cdot,\cdot]_i$ \emph{positive} on the primitive complement because the pole line is
positive and $\mathsf K_i\succeq0$ (Haynsworth/Schur, D4 Thm index). Hence
\[
   \sum_{j,k}c_j\overline{c_k}\,\mathsf K_i^\circ(z_j,z_k)
   =\Big\|\,Q_i\!\sum_j c_j\Gamma_i(z_j)\,\Big\|_i^2\ \ge\ 0.
\]
By (τ3), $\mathsf K_i^\circ(z_j,z_k)\to\mathsf K^\circ(z_j,z_k)$, so passing to the limit
\[
   \sum_{j,k}c_j\overline{c_k}\,\mathsf K^\circ(z_j,z_k)\ \ge\ 0.
\]
As the configuration was arbitrary, $\mathsf K^\circ\succeq0$, i.e. $\operatorname{sq}_-(\mathsf K^\circ)
=0$. By (τ4) the grading divisor stays $\mathfrak b^\circ=1$, so no negative square vanished silently and
$\kappa(\mathbf X)=0$. $\square$

\begin{remark}[why this is now clean and was not before]
The positivity $\sum c_j\bar c_k\mathsf K_i^\circ\ge0$ is a *finite Gram* statement, stable under the
*pointwise* (τ3) limit — no uniformity across the strip, no operator-norm bound, no zero-location input.
The M3 obstruction ("the index hides at the non-uniformity locus") does not arise here because the object
that converges is the *kernel* (τ3), recovered from the *germ* (τ2), not the scalar determinant. The
scalar non-uniformity that defeated M3 is decoupled from the kernel positivity. \textbf{The price is that
τ3 must be *established* for the arithmetic tower — that is D8, and it is the whole remaining content.}
\end{remark}

---

## §2. The finite-index version

\begin{theorem}[upper semicontinuity of the index]\label{thm:usc}
If $\mathbf X_i$ have $\operatorname{sq}_-(\mathsf K_i^\circ)\le\kappa$ and $\mathbf X_i\to\mathbf X$ in
$\tau_\kappa$, then $\operatorname{sq}_-(\mathsf K^\circ)\le\kappa$.
\end{theorem}
\emph{Proof.} Each finite Gram matrix of $\mathsf K_i^\circ$ has $\nu_-\le\kappa$; the set $\{M:\nu_-(M)
\le\kappa\}$ is closed (Stage 1, Thm 4.1: $\lambda_{\kappa+1}(M)\ge0$ is closed and $\lambda_{\kappa+1}$
is continuous). The (τ3) limit of each Gram matrix therefore has $\nu_-\le\kappa$; supremum over
configurations gives $\operatorname{sq}_-(\mathsf K^\circ)\le\kappa$. $\square$

\begin{remark}[upper semicontinuity vs continuity, and where the divisor is needed]
Thm~\ref{thm:usc} gives $\operatorname{sq}_-(\mathsf K^\circ)\le\liminf\operatorname{sq}_-(\mathsf K_i^\circ)$
— a negative square can \emph{vanish} in the limit but cannot \emph{appear}. For the index-$0$ stratum
this is already equality ($0\le0$), so Thm~\ref{thm:closed} needs nothing more. For genuine
\emph{continuity} at $\kappa>0$ (needed only if one wanted to track DH's index through a limit, D10) one
uses divisor convergence (τ4): $\deg\mathfrak b$ is locally constant under divisor convergence away from
collisions, upgrading semicontinuity to continuity. The assembly D11 uses only the index-$0$ case, where
Thm~\ref{thm:closed} suffices.
\end{remark}

---

## §3. Acceptance criteria (the honesty gate for D6)

D6 is accepted only if its proof uses exactly: (i) positivity of the finite kernels $\mathsf K_i$ (G2);
(ii) positivity of the pole line (G4); (iii) Feshbach shorting (D4, not subtraction); (iv) pointwise
(finite-Gram) convergence (τ3). It must **not** use:
\begin{itemize}
\item RH or any property of the zeros of $\Xi$ — \emph{checked}: the proof is pure Gram-matrix positivity;
\item scalar determinant convergence to infer kernel convergence — \emph{checked}: τ3 is a hypothesis
supplied by D8, not derived from τ1;
\item operator-norm boundedness of the primitive part — \emph{checked}: only pointwise limits are used.
\end{itemize}

\begin{redflag}
D6 proves \emph{closedness of index $0$}, i.e. "limit of positive shorted kernels is positive." It does
\textbf{not} prove that the limit kernel equals the genuine $\mathsf K_\Xi^{\mathrm{G5}}$ — that is D9,
and without it D6 would only show "some positive kernel attached to the limit has index $0$," which is
\emph{not} RH (the forbidden endpoint reassignment, D0). The two must be kept separate: D6 = positivity
is closed; D9 = the closed-positive limit *is* the $\Xi$ kernel.
\end{redflag}

---

## §4. What D6 establishes

- **Positive-pole closedness** (Thm~\ref{thm:closed}): a $\tau_\kappa$-limit of positive shorted kernels
  is positive; index $0$ is closed. Clean Schur-complement positivity, no RH, no uniformity, no norm
  bound.
- **Upper semicontinuity** of the index in general (Thm~\ref{thm:usc}); continuity via the divisor at
  $\kappa>0$ (for D10).
- The honest localization, completing the M3 story: **closedness is free; the entire remaining content is
  the convergence τ3 of the arithmetic shorted kernels to the fixed endpoint** — D8 (that they converge)
  and D9 (that the limit is $\mathsf K_\Xi^{\mathrm{G5}}$).

Next: D7 (the finite von Mangoldt systems are in $\mathcal G_0$, A1), then the decisive D8.
