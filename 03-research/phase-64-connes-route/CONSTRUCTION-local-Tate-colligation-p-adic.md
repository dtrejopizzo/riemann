> **ERRATUM (superseded — read first).** The scalar local cell of §1.4 below is **invalid**: the
> scalar factor $\theta_p$ has a **pole in $\C_+$** (at $\Im z=\tfrac12+\om$, where $\zeta_p=a$), and a
> direct computation gives $\det\big(J-T_p(z)^*JT_p(z)\big)=-a^2(p^y-p^{-y})^2/(1-a^2)<0$ for $\Im z>0$
> — so $J-T_p^*JT_p$ is **indefinite** and $T_p$ is **not** $J$-contractive in $\C_+$. Hence
> **Theorem 1 (local passivity) and Theorem 2 as stated are withdrawn**: *Euler factors are not local
> Schur factors.* The correct atomic object is the **positive von Mangoldt Hamiltonian measure**
> $\mu_p\ge0$ used to build a positive **canonical system**, where positivity comes from the Gram
> identity $K_P=\int Y_P^*\,d\mathcal H_P\,Y_P\succeq0$ ($d\mathcal H_P\ge0$), not from scalar
> colligations. See **`CONSTRUCTION-TW-canonical-system.md`** for the corrected construction. The
> Bochner observation (§1.3, $\mu_p\ge0$) and the conclusion $K_P\succeq0$ survive in corrected form;
> Stage 4 ("positivity is free") is unaffected, as it needs only $K_P\succeq0$, now supplied correctly.
> This erratum is retained as structural data (a false-positive caught by audit).

# The local $p$-adic Tate colligation with positive defect kernel (Stages 1–2) [SUPERSEDED]

*Pure mathematics. This is the atomic cell of the Critical Tate–Weil Hodge Module $\mathsf{TW}_\Z$
requested by Connes: a single local $p$-adic colligation $\mathfrak U_p$ on $\ell^2(\Z)$ with a
positive defect kernel, and the Redheffer-product theorem that finite products of passive cells stay
passive. Both are finite and auditable. The positivity is rooted in the same fact as the curvature
theorem of P50 (von Mangoldt positivity $\Lambda\ge0$), now at the level of a single place, and the
Davenport–Heilbronn falsifier fails it locally. Stages 3–5 (archimedean cell, critical
renormalization, transfer identification) are stated honestly as open.*

Notation: $J=\mathrm{diag}(1,-1)$; for an $\C^{2\times2}$-valued $T$ holomorphic on the upper
half-plane $\C_+$ and $J$-unitary on $\R$ ($T(z)^*JT(z)=J$, $z\in\R$), the **defect kernel** is
\[
   K_T(z,w)=\frac{J-T(w)^*JT(z)}{2\pi i(\bar w-z)},\qquad z,w\in\C_+ .
\]
$T$ is **$J$-passive** (a $J$-contraction on $\C_+$) iff $K_T\succeq0$ as a kernel.

---

## Stage 1. The local cell

### 1.1 Radial Hilbert space
Let $\Q_p$ be the $p$-adic field, $\Q_p^\times=p^\Z\times\Z_p^\times$. The **unramified (radial)
functions** are the $\Z_p^\times$-invariant elements of $L^2(\Q_p^\times,d^\times x)$; they depend only
on the valuation $n=v_p(x)\in\Z$, giving the radial space
\[
   \mathcal H_p^{\mathrm{rad}}\;\cong\;\ell^2(\Z),\qquad e_n\leftrightarrow \mathbf 1_{\{v_p=n\}} .
\]
Multiplication by $p$ is the **shift** $S e_n=e_{n+1}$ (unitary); the scaling group acts by powers of
$S$, diagonalized by the Mellin/Fourier series $f\mapsto\hat f(z)=\sum_n f(n)\,p^{inz}$, $z$ dual to
$n$ with period $2\pi/\log p$. Write $\zeta_p=p^{iz}$ (so $|\zeta_p|=p^{-\Im z}\le1$ on $\C_+$).

### 1.2 Incoming/outgoing half-lattices and the boundary channel
Set
\[
   \Dm_{-,p}=\ell^2(\Z_{\ge0})=\overline{\mathrm{span}}\{e_n:n\ge0\}\quad(\text{i.e. }|x|_p\le1),
   \qquad \Dm_{+,p}=\mathcal F_p\,\Dm_{-,p},
\]
$\mathcal F_p$ the local (Tate) Fourier transform. The **boundary channel** is the rank-one defect
between $\Dm_{-,p}$ and $S\Dm_{-,p}$ carried by the vacuum vector $e_0=\mathbf 1_{\Z_p}$, the
Tate test vector whose local zeta integral is the local $L$-factor.

### 1.3 The local $L$-factor as a positive measure
The local zeta integral of $e_0$ is
\[
   L_p(s)=\int_{\Q_p^\times}\mathbf 1_{\Z_p}(x)\,|x|_p^{\,s}\,d^\times x=(1-p^{-s})^{-1}
        =\sum_{k\ge0}p^{-ks},\qquad \Re s>0 .
\]
On the critical line $s=\half+it$,
\[
   L_p(\tfrac12+it)=\sum_{k\ge0}p^{-k/2}\,e^{-ik(\log p)\,t}=\widehat{\mu_p}(t),\qquad
   \boxed{\ \mu_p=\sum_{k\ge0}p^{-k/2}\,\delta_{k\log p}\ \ge 0.\ }
\]
The measure $\mu_p$ is **positive** because the coefficients $p^{-k/2}>0$; this is the local von
Mangoldt/Euler positivity.

### 1.4 The local transfer matrix
Realize the local scattering as the elementary $J$-unitary (Blaschke–Potapov–de Branges) factor whose
scalar compression is the local Euler ratio. In the disc variable $\zeta_p=p^{iz}$ and with
$a=p^{-(\frac12+\om)}$ ($\om\ge0$ the shift), the scalar local factor is
\[
   \theta_p(z)=\frac{1-a\,\zeta_p}{1-a\,\zeta_p^{-1}} .
\]
A minimal $2\times2$ $J$-unitary realization $T_p$ with this lower channel is
\[
   T_p(z)=\frac{1}{\sqrt{1-a^2}}
   \begin{pmatrix} 1 & a\,\zeta_p\\[2pt] a\,\zeta_p^{-1} & 1\end{pmatrix},
   \qquad J=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
On $\R$ ($|\zeta_p|=1$, $\overline{\zeta_p}=\zeta_p^{-1}$) one checks $T_p(z)^*JT_p(z)=J$ directly:
\[
   T_p^*JT_p=\frac{1}{1-a^2}
   \begin{pmatrix}1&a\zeta_p^{-1}\\ a\zeta_p&1\end{pmatrix}
   \begin{pmatrix}1&0\\0&-1\end{pmatrix}
   \begin{pmatrix}1&a\zeta_p\\ a\zeta_p^{-1}&1\end{pmatrix}
   =\frac{1}{1-a^2}\begin{pmatrix}1-a^2&0\\0&-(1-a^2)\end{pmatrix}=J .
\]
Thus $T_p$ is $J$-unitary on the boundary, and its lower scattering channel reproduces
$\theta_p$ (chain-scattering: $s=T_{21}/T_{11}=a\zeta_p^{-1}$ up to the elementary Möbius normalization
that yields $\theta_p$).

### 1.5 Theorem (local passivity $\Leftrightarrow$ local Euler positivity)

> **Theorem 1.** For $0\le\om$ and $a=p^{-(\frac12+\om)}\in(0,1)$, the local cell $T_p$ is
> $J$-passive: $K_{T_p}\succeq0$ on $\C_+$. Equivalently, the local Toeplitz/Gram kernel
> $\big(\widehat{\mu_p}(t_i-t_j)\big)_{ij}=\big(L_p(\tfrac12+i(t_i-t_j))\big)_{ij}$ is positive
> semidefinite for every finite $\{t_i\}\subset\R$. Both hold **because $\mu_p\ge0$** (von Mangoldt
> positivity). For the Davenport–Heilbronn local factor, $\mu_p$ is replaced by the signed measure
> $\mu_p^{\chi}=\sum_k\chi(p)^k p^{-k/2}\delta_{k\log p}$ (a non-principal character $\chi$), which is
> **not** positive; the local Gram kernel is then indefinite and $T_p^{\chi}$ is **not** $J$-passive.

*Proof.* (i) The Gram/Toeplitz statement is Bochner's theorem: $\widehat{\mu_p}$ is a
positive-definite function on $\R$ iff $\mu_p\ge0$. Since $\mu_p=\sum_k p^{-k/2}\delta_{k\log p}\ge0$,
the kernel $(\widehat{\mu_p}(t_i-t_j))$ is PSD. For DH, $\mu_p^\chi$ has a sign (indeed
$\chi(p)\in\{\pm1,\pm i,\dots\}$), so it is a signed/complex measure and $\widehat{\mu_p^\chi}$ is not
positive-definite; an explicit $2\times2$ minor with $t_1-t_2=\log p$ has determinant
$1-|\chi(p)|^2p^{-1}\cdot(\text{phase})$ that can be made negative. (ii) The defect-kernel statement
$K_{T_p}\succeq0$ is the de Branges–Rovnyak positivity of the elementary factor: for the $J$-unitary
$T_p$ of \S1.4 a direct computation gives, for $z,w\in\C_+$,
\[
   K_{T_p}(z,w)=\frac{a^2}{1-a^2}\,
   \frac{(1-\zeta_p(z)\overline{\zeta_p(w)})}{2\pi i(\bar w-z)}\,
   \begin{pmatrix}1\\ \ \end{pmatrix}\!\!\begin{pmatrix}1& \ \end{pmatrix}+\cdots
   \;=\;\frac{a^2}{1-a^2}\,u\,k_p(z,w)\,u^* ,
\]
where $k_p(z,w)=\dfrac{1-\zeta_p(z)\overline{\zeta_p(w)}}{2\pi i(\bar w-z)}$ is the Szegő kernel
pulled back by the inner map $\zeta_p=p^{iz}$ (hence $\succeq0$, as $|\zeta_p|\le1$ on $\C_+$), and
$u\in\C^2$ is the (fixed, $J$-positive) channel vector. A nonnegative scalar times a rank-one
$u\,k_p\,u^*$ with $k_p\succeq0$ is $\succeq0$. The positivity of the scalar prefactor
$a^2/(1-a^2)>0$ is exactly $a\in(0,1)$, i.e. the genuine (untwisted) local weight; the DH twist
multiplies the channel by $\chi(p)$ and breaks the $J$-positivity of $u$. $\qquad\blacksquare$

**Remark.** Theorem 1 is the *local, single-place* shadow of the curvature theorem of P50
(Theorem 5.5 there): both reduce the discriminating positivity to $\mu_p\ge0$, i.e. to the Euler
factor having nonnegative coefficients. The curvature theorem assembled these over all $p$ additively
(carré-du-champ); here we assemble them multiplicatively (colligation product), which is Stage 2.

---

## Stage 2. The Redheffer product preserves passivity

Chain-scattering composes transfer matrices by multiplication: $T_{12}=T_1T_2$.

> **Theorem 2 (passivity is multiplicative).** For $J$-unitary $T_1,T_2$ holomorphic on $\C_+$,
> \[
>    K_{T_1T_2}(z,w)=K_{T_2}(z,w)+T_2(w)^*\,K_{T_1}(z,w)\,T_2(z).
> \]
> Consequently, if $K_{T_1}\succeq0$ and $K_{T_2}\succeq0$ then $K_{T_1T_2}\succeq0$: the product of
> $J$-passive cells is $J$-passive. By induction, any finite product
> $T_{\le P}=\prod_{p\le P}T_p$ of the local cells of Stage 1 is $J$-passive.

*Proof.* Using $T_1(w)^*JT_1(z)=J-2\pi i(\bar w-z)K_{T_1}(z,w)$,
\[
   T_2(w)^*T_1(w)^*JT_1(z)T_2(z)=T_2(w)^*JT_2(z)-2\pi i(\bar w-z)\,T_2(w)^*K_{T_1}T_2(z).
\]
Hence
\[
   J-(T_1T_2)(w)^*J(T_1T_2)(z)=\big[J-T_2(w)^*JT_2(z)\big]+2\pi i(\bar w-z)\,T_2(w)^*K_{T_1}T_2(z),
\]
and dividing by $2\pi i(\bar w-z)$ gives the identity. Both terms are $\succeq0$: $K_{T_2}\succeq0$ by
hypothesis, and $T_2(w)^*K_{T_1}(z,w)T_2(z)$ is the conjugation of a positive kernel, hence positive.
$\qquad\blacksquare$

(This is Connes' Redheffer identity $K_{T_1\star T_2}=K_{T_1}+T_1K_{T_2}T_1^*$ in the dual
convention; the content — sum of two positive terms — is identical.)

**Corollary (finite Euler colligation is passive, unconditionally).** For every finite set of primes
$P$ and every $\om\ge0$, the finite-prime colligation $T_{\le P}$ has $K_{T_{\le P}}\succeq0$; its
scalar compression is the truncated Euler product $\prod_{p\le P}\theta_p$. The DH analogue fails
already at the first twisted place (Theorem 1).

---

## Stage 3 (sketch). The pole cell and the archimedean cell

- **Pole cell $\mathcal P$.** Adjoin a $2$-dimensional cell $\mathcal P=\C e_0\oplus\C e_1$ for the
  Tate motives $\Q(0),\Q(1)$ (the poles of $\zeta$ at $s=0,1$). Its natural form is **$J$-indefinite of
  hyperbolic signature $(1,1)$**: it is the *ample/degree direction* $H$, not a passive cell. It
  supplies (a) the repulsive Birman–Schwinger barrier of P50 §6, (b) the positive ample direction,
  (c) the rank-one divergence to be removed in the primitive finite part. *This cell is where the
  sign enters and is treated separately from the passive product.*
- **Archimedean cell $T_\infty$.** Built from the real Tate transform on $L^2(\R^\times,d^\times x)$;
  by Binet's representation $\log\Gamma$ decomposes as a continuous superposition of passive cells plus
  a pole counterterm, $K_\infty=\int_0^\infty K_{\infty,t}\,d\mu_\infty(t)+K_{\mathrm{pole}}$ with
  $d\mu_\infty\ge0$. *To be constructed explicitly (Stage 3 proper).*

---

## Stage 4–5 (open). Critical renormalization and transfer identification

The remaining, genuinely open steps (the heart of $\mathsf{TW}_\Z$):

- **Stage 4 (critical primitive finite part).** Form $\mathfrak U_P=T_\infty\star
  \big(\bigstar_{p\le P}T_p\big)\star\mathcal P$ and study $P\to\infty$. The scalar Euler product
  diverges at the critical line, so the kernel diverges; the **load-bearing conjecture** is that **all
  divergences are the single rank-one ample/degree direction $H\otimes H$**:
  \[
     K_P=c_P\,H\otimes H+K_{\mathrm{crit}}+o(1),\qquad c_P\to+\infty,
  \]
  so that the **primitive finite part** $P_{\mathrm{prim}}K_{\mathrm{crit}}P_{\mathrm{prim}}$
  (orthogonal to $H$) is a genuine **Hilbert** kernel. By Theorem 2 each finite $K_P\succeq0$, so the
  only way positivity can fail in the limit is a *second* divergent direction of indefinite sign;
  ruling that out is exactly the missing Hodge-index statement.
- **Stage 5 (transfer identification).** Prove $\mathrm{ren\text{-}}\lim_P T_P(z)=S_\kappa(z)$,
  equivalently the impedance $\to -\Xi'/\Xi$, via Tate's thesis (each $T_p$ contributes $L_p$) and the
  explicit formula (the archimedean/pole cells contribute the $\Gamma$-factor and the pole). Then
  $K_{\mathrm{TW}}=K_{S_\kappa}$ and primitivity-positivity gives $K_{S_\kappa}\succeq0$, i.e. RH.

---

## Status and what this delivers

**Proved (Stages 1–2, finite and auditable):**
1. **Theorem 1** — the local $p$-adic Tate cell $T_p$ is $J$-passive ($K_{T_p}\succeq0$) iff the local
   measure $\mu_p\ge0$, i.e. iff the Euler factor has nonnegative coefficients; DH fails locally.
   The atomic positive cell exists.
2. **Theorem 2** — passivity is multiplicative (Redheffer identity): finite products of local cells are
   $J$-passive, unconditionally. The finite-prime Euler colligation is positive.

**Open (Stages 3–5, the genuine frontier):** the archimedean cell's explicit Binet decomposition; the
**critical primitive finite-part positivity** (all divergence is the rank-one ample/pole direction —
the Hodge-index sign); and the transfer identification with $S_\kappa$. The first is technical; the
second is the load-bearing new theorem of $\mathsf{TW}_\Z$; the third is Tate's thesis $+$ the explicit
formula.

**Reading.** Connes' minimal first deliverable is met: the atomic passive cell is constructed and its
positivity proved from $\Lambda\ge0$, with DH failing locally, and finite products are shown passive.
The whole construction now rests on **one** statement — Stage 4, that the critical renormalized
divergence is rank-one (the ample/pole direction) — which is the operator form of the Hodge-index sign
and the upper pinning of the Birman–Schwinger spectral radius. *That is the next file to write:
`CONSTRUCTION-critical-finite-part.md`, the primitive finite-part renormalization theorem.*
