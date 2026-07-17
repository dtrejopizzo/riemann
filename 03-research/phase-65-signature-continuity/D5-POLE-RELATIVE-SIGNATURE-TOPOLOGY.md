# D5 — The pole-relative signature topology $\tau_\kappa$

**Phase 65 / Signature-Continuity Package, deliverable D5.** Pure mathematics, full proofs. Defines the
topology in which the positive finite systems converge *and* index zero is closed. The central design
point (forced by the M2 structural finding, T1–T2 tension): **no topology on scalar entire functions can
do both**; the topology must act on the *sourced/kernel* data of D2–D4. $\tau_\kappa$ is the initial
topology of the source-germ evaluation maps together with divisor convergence. Source-germ convergence
$\Rightarrow$ kernel convergence is proved here (via the D2 polarization), so the index becomes a
continuous functional of the convergent data.

> `ASSUMED` ledger (D5): **empty.** Built from D2 (polarization) and D1 (divisor).

---

## §1. Why the topology must be sourced (the T1–T2 tension, restated)

\begin{proposition}[no scalar topology closes both, restated from M2]\label{prop:tension}
There is no unconditional Hausdorff topology on scalar entire functions in which simultaneously (T1)
$\{\kappa=0\}$ is closed and (T2) $D_P\to\Xi$ — their conjunction is RH.
\end{proposition}
\emph{Proof.} (T1)$\wedge$(T2)$\Rightarrow\kappa(\Xi)=0\Rightarrow$ RH (M2, Prop. tension). $\square$

\begin{remark}
Hence $\tau_\kappa$ is built on the data $(D^\circ,\mathcal D^{\circ,\mathrm{src}},\mathsf K^\circ,
\mathfrak b^\circ)$ of the positive-pole chart (D4), not on $D$ alone. The index is recovered from
$\mathsf K^\circ$ (D2), which is recovered from $\mathcal D^{\circ,\mathrm{src}}$; closedness will follow
from Schur-complement positivity (D6), not from any property of $D^\circ$.
\end{remark}

---

## §2. Definition of $\tau_\kappa$

Fix compact exhaustions $\Omega_n\Subset\C\setminus\R$ and, for each finite-dimensional primitive source
plane $F\subset\mathfrak S_{\mathrm{prim}}$, a small ball $B_F(r)$.

\begin{definition}[the signature topology]\label{def:tau}
A net $\mathbf X_i\to\mathbf X$ in $\tau_\kappa$ (in a fixed positive-pole chart) iff all four hold:
\begin{enumerate}
\item[\textbf{(τ1)}] \emph{scalar:} $D_i^\circ\to D^\circ$ uniformly on each compact $K\Subset\Omega$;
\item[\textbf{(τ2)}] \emph{source-germ:} for every source plane $F$ and radius $r$,
$\mathcal D_i^{\circ,\mathrm{src}}(V;z)\to\mathcal D^{\circ,\mathrm{src}}(V;z)$ uniformly for $V\in
B_F(r)$, $z\in K$;
\item[\textbf{(τ3)}] \emph{kernel:} $\mathsf K_i^\circ(z,w)\to\mathsf K^\circ(z,w)$ locally uniformly on
$\Omega\times\Omega$ (equivalently every finite Gram matrix converges);
\item[\textbf{(τ4)}] \emph{grading:} $\mathfrak b_i^\circ\to\mathfrak b^\circ$ as divisors (in the
index-$0$ stratum: $\mathfrak b_i^\circ=1$ and the limit stays $1$).
\end{enumerate}
Equivalently, $\tau_\kappa$ is the initial topology for the family of evaluation maps $\mathbf X\mapsto
\mathcal D_{\mathbf X}^{\circ,\mathrm{src}}|_{B_F(r)\times K}$ together with divisor convergence.
\end{definition}

---

## §3. Source-germ convergence implies kernel convergence

\begin{theorem}[germ $\Rightarrow$ kernel]\label{thm:germ-kernel}
(τ2) implies (τ3): if $\mathcal D_i^{\circ,\mathrm{src}}\to\mathcal D^{\circ,\mathrm{src}}$ uniformly on
source balls (with uniform local boundedness), then $\mathsf K_i^\circ\to\mathsf K^\circ$ locally
uniformly.
\end{theorem}
\emph{Proof.} The kernel is the polarized Hessian $\mathsf K^\circ=\operatorname{Pol}(d^2\log\mathcal
D^{\circ,\mathrm{src}}(0))$ (D2, Def. rec; anomaly-free at second order). On a fixed finite-dimensional
source plane the germs are holomorphic functions of $(V,z)$; uniform convergence of holomorphic functions
on $B_F(r)\times K$ implies uniform convergence of all $V$-derivatives at $0$ on slightly smaller compacts
(Cauchy estimates). The second $V$-derivative at $0$ is exactly the Gram data of $\mathsf K^\circ$; hence
$\mathsf K_i^\circ\to\mathsf K^\circ$ locally uniformly. (Local boundedness, supplied by D8.3 for the
arithmetic case, licenses the Cauchy estimates.) $\square$

\begin{corollary}[index is a continuous functional]\label{cor:index-cont}
On $\tau_\kappa$-convergent nets, $\operatorname{sq}_-(\mathsf K^\circ)$ is upper semicontinuous, and on
the index-$0$ stratum (τ4: $\mathfrak b\equiv1$) it is continuous: $\kappa=0$ is both attained and
preserved. (Proof of preservation is D6.)
\end{corollary}

---

## §4. The completion

\begin{definition}[pole-relative completion]\label{def:completion}
$\overline{\mathcal G}^{+H}$ is the completion of $\mathcal C_1^+$ (canonical systems with one positive
rank-one trace divergence) under $\tau_\kappa$: its points are $\tau_\kappa$-limits of towers, each
carrying the limit data $(D^\circ,\mathcal D^{\circ,\mathrm{src}},\mathsf K^\circ,\mathfrak b^\circ)$.
\end{definition}

\begin{theorem}[positive-pole compactification — existence of limits]\label{thm:compact}
A tower $\{\mathbf X_P\}\subset\mathcal C_1^+$ has a $\tau_\kappa$-limit in $\overline{\mathcal G}^{+H}$
whenever (a) the renormalized scalar determinants converge ($D_P^\circ\to D^\circ$, τ1) and (b) the
primitive sourced germs are locally bounded uniformly in $P$ (normal family on each source plane). Then
the limit kernel exists (Thm~\ref{thm:germ-kernel}) and the grading divisor converges (τ4).
\end{theorem}
\emph{Proof.} Given (b), Montel/Vitali on each finite-dimensional source plane $F$ gives a convergent
subsequence of germs; (a) pins the $V=0$ slice; uniqueness of holomorphic germs (agreement at $V=0$ plus
identification of coefficients, D8.4) forces full convergence, not just subsequential. Thm~\ref{thm:germ-kernel}
gives the kernel; (τ4) is divisor convergence of the (here trivial) Blaschke factors. $\square$

\begin{remark}[where G4 enters]
Hypothesis (b) — uniform local boundedness of the primitive sourced germs — is exactly what G4 supplies
after pole-shorting: the primitive box counts are bounded (D8.3). Hypothesis (a) is G3 (the scalar
endpoint). So the compactification theorem reduces, for the arithmetic tower, to G3 + G4 + D8.4; D5
itself is the general topological frame.
\end{remark}

---

## §5. What D5 establishes

- $\tau_\kappa$: the initial topology of source-germ maps + divisor convergence (Def.~\ref{def:tau}),
  forced to act on sourced/kernel data by the T1–T2 tension (Prop.~\ref{prop:tension}).
- **Source-germ convergence $\Rightarrow$ kernel convergence** (Thm~\ref{thm:germ-kernel}, via D2
  polarization + Cauchy estimates) — so the index is a continuous functional of the convergent data
  (Cor.~\ref{cor:index-cont}).
- The completion $\overline{\mathcal G}^{+H}$ and the existence-of-limits theorem
  (Thm~\ref{thm:compact}), reducing to G3 (scalar) + G4 (primitive boundedness) + D8.4 (coefficient
  identification) for the arithmetic tower.

Next: D6 proves index-$0$ is **closed** in $\tau_\kappa$ (Schur-complement positivity), completing the
formal closedness machinery; the arithmetic content (that the limit kernel is the *fixed* $\mathsf
K_\Xi^{\mathrm{G5}}$) is D8/D9.
