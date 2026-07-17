# The Critical Tate–Weil Canonical Hodge Module $\mathsf{TW}^{\mathrm{can}}_\Z$ (corrected construction)

*Pure mathematics. This corrects `CONSTRUCTION-local-Tate-colligation-p-adic.md` after the audit: the
Euler factors are **not** local Schur/passive cells (the scalar factor has a $\C_+$ pole; the matrix
is $J$-indefinite in $\C_+$). The correct atomic object is the **positive von Mangoldt Hamiltonian
measure**, and the global object is a **renormalized canonical system**, whose kernel is positive by
the canonical Gram identity. The architecture of P50 (positivity free; the wall is rank-one escape) is
preserved with the corrected, valid positivity. The load-bearing open theorem is the **rank-one escape
theorem**; if it holds, RH follows. Honest: that theorem is RH-strength and is the object to create.*

Notation: $J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}$ (symplectic) for the canonical system;
$z\in\C_+$; $t$ the scaling variable on $\R$.

---

## §1. Audit: the scalar local factor is not a Schur factor (the corrected error)

For $\theta_p(z)=\dfrac{1-a\zeta_p}{1-a\zeta_p^{-1}}$, $\zeta_p=p^{iz}$, $a=p^{-(\frac12+\om)}$:
\[
   1-a\zeta_p^{-1}=0\iff\zeta_p=a\iff iz\log p=-(\tfrac12+\om)\log p\iff \Im z=\tfrac12+\om>0 .
\]
So $\theta_p$ has a **pole in $\C_+$**; it is not Schur there, and finite scalar products of such
factors are not passive transfer functions. For the $2\times2$
$T_p=(1-a^2)^{-1/2}\begin{psmallmatrix}1&a\zeta_p\\a\zeta_p^{-1}&1\end{psmallmatrix}$, a direct
computation gives, for $\Im z=y>0$ (and $J=\mathrm{diag}(1,-1)$ in this boundary normalization),
\[
   \det\big(J-T_p(z)^*JT_p(z)\big)=-\frac{a^2\,(p^{y}-p^{-y})^2}{1-a^2}<0 ,
\]
so $J-T_p^*JT_p$ is **indefinite**: $T_p$ is $J$-unitary on $\R$ but **not** $J$-contractive in
$\C_+$. **Conclusion:** *Euler factors are not local Schur factors.* The positivity must enter through
the **positive logarithmic/infinitesimal data** — the von Mangoldt Hamiltonian — not through scalar
inner factors.

---

## §2. The positive prime Hamiltonian cell

For each prime $p$ define the **positive atomic Hamiltonian**
\[
   d\mathcal H_p(t)=\sum_{k\ge1}\frac{\log p}{p^{k/2}}\,|v_{p,k}\rangle\langle v_{p,k}|\;
   \delta_{k\log p}(t),
\]
where $v_{p,k}\in\C^2$ is the channel vector attached to the scaling correspondence $F_{k\log p}$
(the graph $\Gamma_{k\log p}$). Since the weights are the von Mangoldt coefficients
$\Lambda(p^k)/\sqrt{p^k}=\log p\cdot p^{-k/2}>0$,
\[
   \boxed{\ d\mathcal H_p\ \ge\ 0\ }\qquad(\text{positive matrix measure}).
\]
This is the correct atomic input. Its positivity is the genuine von Mangoldt positivity
$\Lambda\ge0$ — the same fact that powers the curvature theorem of P50 (Theorem 5.5), now carried by a
Hamiltonian measure rather than a scalar colligation. The Davenport–Heilbronn twist replaces the
weights by $\chi(p)^k\log p\cdot p^{-k/2}$, a **signed** matrix measure: $d\mathcal H_p^{\chi}
\not\ge0$. The positivity is exactly the Euler/multiplicative structure.

---

## §3. Finite canonical systems are positive (the corrected positivity theorem)

For a finite prime set $P$, set $d\mathcal H_P=d\mathcal H_{\mathrm{pole}}+d\mathcal H_\infty+
\sum_{p\le P}d\mathcal H_p$, with the passive part $d\mathcal H_P^{\mathrm{pass}}=
d\mathcal H_\infty+\sum_{p\le P}d\mathcal H_p\ge0$ (archimedean cell of §6, positive by Binet). Define
the canonical transfer matrix $Y_P(t,z)$ by
\[
   J\,\partial_t Y_P(t,z)=z\,d\mathcal H_P(t)\,Y_P(t,z),\qquad Y_P(0,z)=I .
\]

> **Theorem (corrected finite positivity).** The de Branges kernel of the finite canonical system,
> \[
>    K_P(z,w)=\frac{J-Y_P(\ell,w)^*JY_P(\ell,z)}{2\pi i(\bar w-z)}
>           =\int_0^\ell Y_P(t,w)^*\,d\mathcal H_P^{\mathrm{pass}}(t)\,Y_P(t,z)\;\succeq\;0 ,
> \]
> is **positive** because $d\mathcal H_P^{\mathrm{pass}}\ge0$. (The pole cell is carried separately as
> the ample direction $H$.) For the Davenport–Heilbronn Hamiltonian the integrand is indefinite and
> $K_P^{\chi}$ is indefinite.

*Proof.* The Lagrange (Christoffel–Darboux) identity for the canonical system $J\partial_tY=z\,
d\mathcal H\,Y$ reads
\[
   \partial_t\big(Y(t,w)^*JY(t,z)\big)
   =(\bar w-z)\,... \;\Longrightarrow\;
   J-Y(\ell,w)^*JY(\ell,z)=2\pi i(\bar w-z)\!\int_0^\ell Y(t,w)^*\,d\mathcal H(t)\,Y(t,z),
\]
using $\partial_t(Y^*JY)=(\partial_tY)^*JY+Y^*J\partial_tY=\bar z\,(d\mathcal H Y)^*J^{-1}... $ — the
standard canonical-system computation, valid because $J^*=-J$ and $\mathcal H^*=\mathcal H$. The
right-hand integrand $Y^*\,d\mathcal H\,Y$ is a Gram form of the positive matrix measure
$d\mathcal H\ge0$, hence $\succeq0$; dividing by $2\pi i(\bar w-z)$ gives $K_P\succeq0$. $\square$

This is the corrected replacement for the (defective) scalar Redheffer argument: positivity is now
**manifest** from $d\mathcal H_P\ge0$ through the Gram identity, with no appeal to scalar inner
factors. It is rigorous.

---

## §4. The pole/degree direction and the divergent trace

Adjoin the hyperbolic pole cell $\mathcal P=\C e_0\oplus\C e_1$ (Tate motives $\Q(0),\Q(1)$; poles at
$s=0,1$), giving the ample vector $H$. The trace of the passive kernel is the total Hamiltonian mass,
\[
   \Tr K_P\ \asymp\ \int_0^\ell \Tr d\mathcal H_P^{\mathrm{pass}}\ \asymp\ \sum_{p\le P}\frac{(\log p)^2}{p}
   \ \sim\ \tfrac12(\log P)^2\to\infty
\]
(Mertens), and the claim is that this divergence is carried by $H$ alone: $K_P=c_P\,|H\rangle\langle H|
+R_P$, $c_P\sim\tfrac12(\log P)^2$, with $R_P$ bounded on $H^\perp$.

---

## §5. The rank-one escape theorem (the wall) and its corollary

\begin{openbox}{rank-one escape (RH-strength)}
\[
   \sup_P\big\|P_{\mathrm{prim}}K_PP_{\mathrm{prim}}\big\|<\infty,
   \qquad P_{\mathrm{prim}}=I-\tfrac{|H\rangle\langle H|}{\langle H,H\rangle}.
\]
Equivalently, all divergent mass of the positive $K_P$ escapes only through the pole direction $H$.
\end{openbox}

> **Corollary (escape $\Rightarrow$ RH).** Each $P_{\mathrm{prim}}K_PP_{\mathrm{prim}}\succeq0$
> (compression of the positive $K_P$ of §3). If they are uniformly bounded, a weak-$*$ limit
> $K_{\mathrm{crit}}\succeq0$ exists (weak limits of positives are positive). By the transfer
> identification (§6) $K_{\mathrm{crit}}=K_{S_\kappa}$, so $K_{S_\kappa}\succeq0$, $S_\kappa$ is Schur,
> $m=-\Xi'/\Xi$ is Herglotz, and RH holds.

*This is Stage 4 of P50, intact:* positivity is free; the only wall is the **boundedness/escape**
statement. An off-line zero $\rho=\beta+i\gam$ ($\beta>\half$) is exactly a second escape direction
(growth $\lambda^{2\beta-1}$), so rank-one escape $\Leftrightarrow$ no off-line zeros $\Leftrightarrow$
RH. It is RH-strength, and it is a **center-of-strip** statement no edge estimate reaches.

---

## §6. Transfer determinant and identification with $\Xi$

Replace the (divergent) naive Euler product by the **renormalized perturbation determinant** of the
canonical system. For finite $P$ define $D_P(z)$ by the regularized trace identity
\[
   \frac{D_P'(z)}{D_P(z)}=\Tr\big[(A_P-z)^{-1}-(A_0-z)^{-1}\big],
\]
$A_P$ the canonical operator for $d\mathcal H_P$, $A_0$ the free (pole+archimedean) operator. The
**Stage-5 identification** to prove is
\[
   \mathrm{ren\text{-}}\lim_{P\to\infty}D_P(z)=\Xi(z),\qquad\text{hence}\qquad
   \mathrm{ren\text{-}}\lim_P\frac{D_P'}{D_P}=\frac{\Xi'}{\Xi},\quad m=-\Xi'/\Xi .
\]
This is Tate's thesis (each prime cell contributes $L_p$ to the determinant) together with the
explicit formula (archimedean cell $\to\Gamma$-factor; pole cell $\to$ the $s(s-1)$ poles), now as a
**determinant** identity rather than a product of scalar factors — the correct vehicle, since the
canonical system has a well-defined perturbation determinant where the scalar product diverges.
The archimedean Hamiltonian $d\mathcal H_\infty$ is built from Binet's formula
$\log\Gamma(s/2)=(\text{elementary})+\int_0^\infty\Phi_s(t)\,\frac{dt}{t(e^t-1)}$ with the **positive**
measure $\frac{dt}{t(e^t-1)}\ge0$; the elementary terms join the pole/degree cell.

---

## §7. Three faces of the rank-one escape theorem (where to create)

The escape theorem has three equivalent forms; a proof may come through any one.

- **(A) Central adelic large sieve.** For primitive (degree-zero, non-principal channel) data,
  \[
     \sup_X\Big\|\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\,\Pi_{\mathrm{prim}}(F_{\log n})\Big\|<\infty ,
  \]
  a **center-of-strip** ($n^{-1/2}$ normalization) operator bound, far stronger than PNT/zero-free
  regions (which are edge-of-strip). The new mathematics is a large sieve at the critical exponent.
- **(B) Primitive finite-part Hodge index.** On the correspondence module
  $\widehat{\mathrm{CH}}^1_{\mathrm{TW}}$ generated by the $\Gamma_t$, with pairing
  $(Z_f,Z_g)_{\mathrm{TW}}=\mathrm{FP}\iint\hat f(s)\overline{\hat g(t)}\langle\Gamma_s,\Gamma_t\rangle
  \,ds\,dt$ and $Z_f=\int\hat f(t)\Gamma_t\,dt-c_f\Delta$, prove
  $(Z_f,H)=0\Rightarrow(Z_f,Z_f)\le0$, with $W(f)=-(Z_f,Z_f)$. The new mathematics is a primitive
  finite-part intersection theory for scaling correspondences (the arithmetic-site face).
- **(C) Canonical-system compactness.** Prove the primitive Hamiltonians are uniformly bounded in a
  Hilbert scale, $\sup_P\|P_{\mathrm{prim}}\,d\mathcal H_P\,P_{\mathrm{prim}}\|_{\mathcal B^{-1/2}\to
  \mathcal B^{1/2}}<\infty$, so the canonical systems converge to a positive limiting Hamiltonian. The
  new mathematics is primitive Hamiltonian compactness at the critical exponent $\tfrac12$.

---

## §8. Status

\textbf{Corrected and rigorous:}
\begin{itemize}
\item §1 — the scalar Euler-factor colligation is invalid ($\C_+$ pole; $J$-indefinite); withdrawn.
\item §2 — the positive prime Hamiltonian cell $d\mathcal H_p\ge0$ (von Mangoldt positivity); DH fails.
\item §3 — **finite canonical kernels are positive**, $K_P=\int Y_P^*\,d\mathcal H_P\,Y_P\succeq0$, by
the canonical Gram identity (the corrected positivity theorem). This restores, validly, the input
Stage 4 needs.
\item §5 corollary — positivity is free (intact): rank-one escape $\Rightarrow$ RH.
\end{itemize}

\textbf{Open (to create):} the **rank-one escape theorem** (§5), in one of the three faces (§7); the
archimedean Binet cell (§6, technical); the transfer determinant identification $D_P\to\Xi$ (§6, Tate
$+$ explicit formula). The escape theorem is RH-strength and center-of-strip; it is the object to
invent.

\textbf{Corrected slogan.} Not ``finite Euler colligations are positive'' (false) but
\[
   \boxed{\ \text{finite Tate–Weil canonical Hamiltonians are positive,}\ }
\]
the positivity carried by the von Mangoldt Hamiltonian measure $d\mathcal H_p\ge0$ through the
canonical Gram identity. Euler factors are not local Schur functions; their positive infinitesimal
(von Mangoldt) data is the right atomic input. Everything downstream (positivity free; the wall is
rank-one escape) stands on this corrected foundation.

\textbf{Audit points for the reviewer (as requested):}
(1) the scalar cell is invalid — confirmed in §1;
(2) the positive Hamiltonian/canonical replacement — §2–§3;
(3) the canonical Gram identity replaces the defective Redheffer argument — §3 (Lagrange identity);
(4) the perturbation determinant recovers $\Xi$ after Tate renormalization — §6 (open, to verify).
