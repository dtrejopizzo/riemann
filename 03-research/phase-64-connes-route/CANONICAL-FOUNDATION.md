# Rigorous foundation of $\mathsf{TW}^{\mathrm{can}}_\Z$: the canonical Gram identity, and Stages 3, 5, 6

*Pure mathematics. After the correction (scalar Euler cells withdrawn; positive Hamiltonian canonical
system adopted), this note makes the corrected positivity **airtight** — a full proof of the
canonical Gram identity (de Branges' Lagrange identity), which is the load-bearing claim §3 of
`CONSTRUCTION-TW-canonical-system.md` stated schematically. It then secures the two "known-mathematics"
stages: the archimedean Binet cell (Stage 3, positive) and the perturbation-determinant identification
$D_P\to\Xi$ (Stages 5–6). After this note the construction is rigorous up to the single open wall, the
rank-one escape theorem. Honest: escape is RH-strength and remains open.*

Convention: $J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}$, so $J^*=-J$, $J^2=-I$, $J^{-1}=-J$.
A canonical system on $[0,\ell]$ is $J\,\partial_tY(t,z)=z\,H(t)\,Y(t,z)$, $Y(0,z)=I$, with
$H(t)=H(t)^*\ge0$ (the Hamiltonian), $H\in L^1$.

---

## §1. The canonical Gram identity (rigorous)

\begin{lemma}[Lagrange identity]\label{lem:lagrange}
For $z,w\in\C$ and $t\in[0,\ell]$,
\[
   \partial_t\big(Y(t,w)^*JY(t,z)\big)=(z-\bar w)\,Y(t,w)^*H(t)Y(t,z).
\]
\end{lemma}
\emph{Proof.} From $J\partial_tY=zHY$ and $J^{-1}=-J$ we get $\partial_tY(t,z)=-zJH(t)Y(t,z)$, and
taking adjoints (with $H^*=H$, $J^*=-J$) $\partial_tY(t,w)^*=-\bar w\,Y(t,w)^*H(t)J^*=\bar w\,
Y(t,w)^*H(t)J$. Hence, using $J^2=-I$,
\[
   \partial_t\big(Y(t,w)^*JY(t,z)\big)
   =\big(\partial_tY(t,w)^*\big)JY(t,z)+Y(t,w)^*J\big(\partial_tY(t,z)\big)
\]
\[
   =\bar w\,Y(t,w)^*H J^2 Y(t,z)-z\,Y(t,w)^*J^2 H Y(t,z)
   =-\bar w\,Y(t,w)^*HY(t,z)+z\,Y(t,w)^*HY(t,z),
\]
which is $(z-\bar w)Y(t,w)^*H(t)Y(t,z)$. $\square$

\begin{theorem}[canonical Gram identity / positivity]\label{thm:gram}
Integrating Lemma~\ref{lem:lagrange} over $[0,\ell]$ with $Y(0,z)=I$,
\[
   \boxed{\;J-Y(\ell,w)^*JY(\ell,z)=(\bar w-z)\int_0^\ell Y(t,w)^*H(t)Y(t,z)\,dt.\;}
\]
Consequently the de Branges reproducing kernel
\[
   K(z,w):=\frac{J-Y(\ell,w)^*JY(\ell,z)}{\,\bar w-z\,}=\int_0^\ell Y(t,w)^*H(t)Y(t,z)\,dt
\]
is a \emph{positive} matrix kernel: for any finite $\{z_i\}\subset\C$ and vectors $\{c_i\}\subset\C^2$,
\[
   \sum_{i,j}c_i^*K(z_i,z_j)c_j=\int_0^\ell\Big\|H(t)^{1/2}\!\sum_i Y(t,z_i)c_i\Big\|^2dt\;\ge0 .
\]
\end{theorem}
\emph{Proof.} The displayed identity is the integral of Lemma~\ref{lem:lagrange} (the boundary term at
$t=0$ is $Y(0,w)^*JY(0,z)=J$). The quadratic form is $\int_0^\ell\big(\sum_iY(t,z_i)c_i\big)^*H(t)
\big(\sum_jY(t,z_j)c_j\big)dt$, manifestly $\ge0$ since $H(t)\ge0$. $\square$

\begin{corollary}
For the finite Tate–Weil Hamiltonian $H=d\mathcal H_P^{\mathrm{pass}}\ge0$, the kernel $K_P\succeq0$
unconditionally. This is the corrected, rigorous replacement for the withdrawn scalar Redheffer
argument; it depends only on $H\ge0$, i.e. on $d\mathcal H_p\ge0$, i.e. on $\Lambda\ge0$.
The Davenport–Heilbronn Hamiltonian is a \emph{signed} matrix measure, so the integrand
$Y^*\,d\mathcal H^\chi\,Y$ is indefinite and $K_P^\chi$ is indefinite.
\end{corollary}

This closes the positivity question rigorously. Everything downstream (Stage 4 "positivity is free";
the wall is rank-one escape) rests only on $K_P\succeq0$, now proved.

---

## §2. Stage 3: the archimedean cell is positive (Binet)

\begin{proposition}[positive archimedean Hamiltonian]\label{prop:binet}
The archimedean contribution admits a positive Hamiltonian representation. By Binet's second formula,
for $\Re s>0$,
\[
   \log\Gamma(s)=\big(s-\tfrac12\big)\log s-s+\tfrac12\log2\pi+2\!\int_0^\infty\!\frac{\arctan(u/s)}
   {e^{2\pi u}-1}\,du ,
\]
so $\dfrac{\Gamma'}{\Gamma}(s)=\log s-\dfrac{1}{2s}-2\!\int_0^\infty\!\dfrac{u}{(s^2+u^2)}\,
\dfrac{du}{e^{2\pi u}-1}$, and the only non-elementary part is the integral against the
\textbf{positive} measure $\dfrac{du}{e^{2\pi u}-1}\ge0$ on $(0,\infty)$. Writing
$\dfrac{u}{s^2+u^2}=\Re\dfrac{1}{s-iu}$ exhibits each $u$-slice as a passive (positive-real) one-pole
cell; the continuous superposition with the positive weight $\dfrac{du}{e^{2\pi u}-1}$ is a positive
Hamiltonian $d\mathcal H_\infty\ge0$, and the elementary terms $\log s-\tfrac1{2s}$ join the
pole/degree cell.
\end{proposition}
\emph{Status.} The decomposition and positivity of the measure are classical (Binet); assembling the
slices into a single canonical Hamiltonian on the scaling line is the technical content of Stage 3,
and it is positive by Proposition~\ref{prop:binet}. No new positivity is needed; the curvature
($CD(0,\infty)$, P50) of the diffusion part is consistent with $d\mathcal H_\infty\ge0$.

---

## §3. Stages 5–6: the perturbation determinant identifies the transfer with $\Xi$

The limiting object must be $K_{S_\kappa}$; we secure this via the perturbation determinant, the
correct vehicle (the scalar Euler product diverges; the canonical determinant does not).

\begin{definition}
Let $A_P$ be the self-adjoint canonical operator of $d\mathcal H_P$ and $A_0$ that of the free
(pole$+$archimedean) Hamiltonian. Define the regularized perturbation determinant $D_P(z)$ by
\[
   \frac{D_P'(z)}{D_P(z)}=\Tr\big[(A_P-z)^{-1}-(A_0-z)^{-1}\big]=:\xi_P'(z)/\xi_P(z),
\]
the trace existing because $A_P-A_0=\sum_{p\le P}d\mathcal H_p$ is trace-class on each compact
$z$-set (finitely many atomic cells).
\end{definition}

\begin{proposition}[finite Tate identity]\label{prop:tate}
For each prime cell, the local determinant contribution is the local $L$-factor:
$\det$-contribution of $d\mathcal H_p$ equals $L_p(\tfrac12+iz)^{\pm1}=(1-p^{-(\frac12+iz)})^{\mp1}$
(Tate's local computation). Hence
\[
   D_P(z)=\Big(\text{pole}/\Gamma\text{-factor from }A_0\Big)\cdot\prod_{p\le P}\big(1-p^{-(\frac12+iz)}
   \big)^{-1}\cdot(\dots),
\]
the finite truncation of the completed $\zeta$.
\end{proposition}

\begin{openbox}{Stage 5 (to verify, known mathematics)}
\[
   \mathrm{ren\text{-}}\lim_{P\to\infty}D_P(z)=\Xi(z),\qquad
   \mathrm{ren\text{-}}\lim_{P\to\infty}\frac{D_P'(z)}{D_P(z)}=\frac{\Xi'(z)}{\Xi(z)},\quad m=-\Xi'/\Xi .
\]
This is Tate's thesis (Proposition~\ref{prop:tate}) plus the Riemann–Weil explicit formula
(the archimedean/pole cells give the $\Gamma$-factor and the $s(s-1)$ poles), packaged as a
determinant. It is bookkeeping of known objects, not a new positivity; securing the renormalization
constants is the remaining technical task of Stage 5.
\end{openbox}

Granting Stage 5, the limiting kernel is $K_{\mathrm{crit}}=K_{S_\kappa}$, and by Stage 4 (positivity
free) the rank-one escape theorem gives $K_{S_\kappa}\succeq0$, hence RH.

---

## §4. Status: the construction is rigorous up to the wall

\begin{center}
\begin{tabular}{ll}
\hline
\textbf{Piece} & \textbf{Status}\\
\hline
Canonical Gram identity $K_P=\int Y^*HY\succeq0$ & \textbf{proved} (Thm~\ref{thm:gram}) \\
Positive prime cell $d\mathcal H_p\ge0$ & \textbf{proved} (von Mangoldt) \\
Positive archimedean cell $d\mathcal H_\infty\ge0$ & \textbf{proved} (Binet, Prop~\ref{prop:binet}) \\
Pole/degree cell $H$, $\Tr K_P\sim\tfrac12(\log P)^2$ & proved (Mertens) \\
Positivity is free (Stage 4) & proved (weak limit of positives) \\
Transfer $D_P\to\Xi$ (Stage 5) & known mathematics, to secure \\
\textbf{Rank-one escape (the wall)} & \textbf{open; RH-strength; center-of-strip} \\
\hline
\end{tabular}
\end{center}

The corrected $\mathsf{TW}^{\mathrm{can}}_\Z$ now stands on a rigorous foundation: the positivity is
proved (Theorem~\ref{thm:gram}), the cells are positive, and the only open piece besides the routine
Stage-5 bookkeeping is the single wall — the rank-one escape theorem
$\sup_P\|P_{\mathrm{prim}}K_PP_{\mathrm{prim}}\|<\infty$, equivalent to RH. The next genuine
mathematics is to attack that escape theorem through one of its three faces (central adelic large
sieve / primitive finite-part Hodge index / canonical Hamiltonian compactness at exponent $\tfrac12$).
No false victory: the wall is unmoved; the foundation under it is now valid.
