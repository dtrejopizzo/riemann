# R163_801 — The node-pair system W(H_a,H_b)=0 on the prime side and on the zero side

*Pure mathematics, no numerics, no , no commits. Only this file was written; no label of record moves.
Inputs: R163_603 (L3.1, L3.2, T5.1, T5.2, R5.3, box (A-loc)), R163_790 (F10: L3.2 holds for any two distinct nodes,
4-point quartet sum; F12: T5.2 restricted to zero statistics), R163_401 (§1.1 conventions, (1.1), 2.4(iii)–(iii′), 3.4, 4.4–4.7),
Paper 47 `eq:symbol`, `eq:form`, `eq:W`.*

**Notation (R163_401 §1.1).** $T=T_c$, $F\in E_c$ the real, parity-definite, real-rooted witness, $G$ the real-on-$\mathbb R$
normalisation of $\widehat F$ (so that $\widehat\Phi\widehat\Psi^\#$-products of node tests are $G^2/((z-a)(z-b))$, R163_401 4.4),
$X=Z(G)\subset\mathbb R$ (simple nodes; multiple nodes as in 2.4(iii′)), $\widehat H_x=G/(z-x)$, $d_x:=W(H_x)\ge0$.
For a product $\Psi=\widehat\Phi\widehat\Psi'^\#$ of two tests in $\mathcal D_T$ the explicit formula reads

$$\sum_\rho\Psi(t_\rho)=\Psi(\tfrac i2)+\Psi(-\tfrac i2)+\frac1{2\pi}\int_{\mathbb R}m\,\Psi\,d\tau-\sum_{n\in\mathcal N_T}\frac{\Lambda(n)}{\sqrt n}\big(\check\Psi(\log n)+\check\Psi(-\log n)\big),\qquad \check\Psi(u)=\frac1{2\pi}\int\Psi(\tau)e^{-i\tau u}d\tau ,\tag{0.1}$$

which is `eq:W`+`eq:symbol` ($\frac1{2\pi}\int\sigma_T\Psi$ plus the polar pair, $\Psi(\pm\frac i2)$ giving $2\mathrm{Re}A\bar B$), and the left side is
(1.1). Only $n<e^{2T}$ occur because $\check\Psi$ is supported in $[-2T,2T]$.

## 0. Status table

| # | statement | label |
|---|---|---|
| Thm 1 | **Collapse.** $[W(H_a,H_b)]_{a,b\in X}$ is the Loewner (divided-difference) matrix of the single function $\Omega(x)=W(F,G/(z-x))$; $\Omega|_X\equiv0$, $\Omega'|_X=d$. The whole off-diagonal system is the linear consequence of the countable node system $\Omega|_X=0$, which is the kernel equation tested on $\{H_x\}$ | PROVED |
| Prop 2 | prime-side form of every entry: finite combination of $\Lambda(n)$, $n<e^{2T}$, times values at $\pm\log n$ of the cross-correlation kernels $\kappa_{ab}=(\kappa_a-\kappa_b)/(a-b)$, plus archimedean and polar terms | PROVED |
| Thm 3 | **Interpolation identity.** For $\mathrm{Im}\,x>\frac12$: $\sum_\rho\frac{G(t_\rho)^2}{t_\rho-x}=C_T(x)-iG(x)^2\mathcal T_T(x)$, $C_T$ = Cauchy transform of $\sigma_TG^2$ + polar, $\mathcal T_T(x)=\sum_{\log n\ge2T}\Lambda(n)n^{-1/2+ix}$ | PROVED for $F\in C^1_c(I_T)$; for the witness ARGUED (approximation, as Lemma 3.0) |
| Cor 3.1 | on $X$ the tail term vanishes identically (exact form of R5.3 locality for the node system); every off-line residue is carried by the tail $G^2\mathcal T_T$, i.e. by $\Lambda(n)$, $n\ge e^{2T}$; the band part $C_T$ is holomorphic off $\mathbb R$ | PROVED (given Thm 3) |
| Prop 4 | Pick/Loewner split $L_{\rm on}+L_{\rm off}=\mathrm{diag}(d)$ on $X$; $L_{\rm on}\succ0$ on every finite $S\subset X$; this is the quadrature 2.4(iii) rewritten, no new inequality | PROVED |
| Prop 4.1 | no finite-rank / finite-span property of the prime-side matrix separates $M_m$ (it adds exactly one more matrix, itself a sum of $4m$ exponentials) | PROVED |
| Thm 5 | **$M_m$ falsifier, exact.** $M_m$'s prime side = ζ's prime side + the windowed density $\beta_m(u)=\sum_j4\cos(\gamma_ju)\cosh(\delta_ju)\mathbf 1_{|u|<2T}$ (non-atomic, nonzero on every subinterval). Thm 1, Prop 2 (as structure), Thm 3, Prop 4 do **not** use this difference | PROVED |
| Prop 5.1 | the only finite-vector inequality the system yields at cell scale: local count $\big|\sum_\rho\Psi(t_\rho)-\frac1{2\pi}\int m\Psi-{\rm pol}\big|\le\frac{V_T}{2\pi}\lVert\Psi\rVert_1$; it uses atomicity (budget $V_T=\sum_{\mathcal N_T}v_n$), fails for clustered $M_m$, but carries no sign of $\mathrm{Re}\,G(t_q)^2$ | PROVED (bound); "single quartet not separated at $T\approx0.8$" ARGUED |
| §6 | the separating property is "atomic prime side **and** integer zero multiplicities"; real-weight compensation of $\beta_m$ by on-line moves exists | ARGUED |
| (A-loc) | | **OPEN** |
| Row D | | **OPEN** |

**Outcome in one sentence.** The infinite node-pair system is not new information: it is the Loewner matrix of one
function vanishing on $X$, hence equivalent to $W(F,H_x)=0$ for $x\in X$; on the prime side it involves only the $N=|\mathcal N_T|$
atoms, the infinite arithmetic tail drops out exactly on $X$ and carries exactly the off-line residues, and no rank,
positivity or finite-span property of the system separates $M_m$; the one genuinely atomic consequence (a local count with
budget $V_T$) has no sign.

---

## 1. Theorem 1 (collapse). PROVED

For real $x$ put $\Psi_x:=G^2/(z-x)$ and, for $x\notin X$, $\Omega(x):=\mathrm{PV}\frac1{2\pi}\int\sigma_TG^2\frac{d\tau}{\tau-x}+\Psi_x(\tfrac i2)+\Psi_x(-\tfrac i2)$;
for $x\in X$ this is $W(F,H_x)$ (no PV needed). Then for $a\ne b$ in $X$:
$$W(H_a,H_b)=\frac{\Omega(a)-\Omega(b)}{a-b}=0,\qquad W(H_a,H_a)=\Omega'(a)=d_a .$$

*Proof.* $\widehat H_a\widehat H_b^\#=G^2/((z-a)(z-b))=\frac1{a-b}(\Psi_a-\Psi_b)$, and (0.1) is linear in $\Psi$; so the first identity
holds, and $\Omega(a)=W(F,H_a)=0$ because $F\in\ker W_T$ and $W_T\ge0$ (Cauchy–Schwarz). For the diagonal, $\sigma_TG^2$ is
real-analytic on $\mathbb R$ and vanishes to order 2 at $a$, so $\Omega$ is real-analytic near $a$ (Plemelj: real part of the
boundary value of a function holomorphic in $\mathrm{Im}>0$) and differentiation under the integral is legitimate:
$\Omega'(a)=\frac1{2\pi}\int\sigma_TG^2/(\tau-a)^2+\Psi_{aa}(\pm\frac i2)=W(H_a)$. ∎

*Consequences (PROVED).*
- (a) The family $\{W(H_a,H_b)=0\}_{a\ne b}$ (R163_790's corrected L3.2) is implied by the countable node system
  $\Omega|_X=0$, and adds nothing to it. At multiple nodes the same holds for the Hankel blocks of 2.4(iii′) (confluent divided
  differences).
- (b) The Gram matrix on $\mathrm{span}\{H_x\}$ is $\mathrm{diag}(d_x)$: its rank is $\#\{d_x>0\}$, its positivity is $d\ge0$.
  **Every rank or positivity property of $[W(H_a,H_b)]$ is a property of the node-weight vector $d$**, which R163_401 §4.4
  shows is $\delta$-blind to first order.
- (c) The node system itself is the kernel equation (§4.6 of 401) tested against $\{H_x\}$; it is equivalent to the full kernel
  equation iff $\{H_x\}$ spans $\mathcal D_T$ modulo $F$, which is hypothesis (Q) (OPEN, RH-neutral, not used).

So "Gram/Hankel structure on the node set" is the Loewner structure of $\Omega$ on its own zero set. This is the reason
the infinite system cannot be overdetermined in a useful way: it is one scalar equation per node.

## 2. Proposition 2 (prime side of the entries). PROVED

With $\widehat H_x=G/(z-x)$ and $F$ supported in $[-T,T]$, $H_x(t)=\mp i\,e^{-ixt}\int_{-T}^{t}F(s)e^{ixs}ds$ (sign by the transform
convention), supported in $[-T,T]$ because $G(x)=0$ (Volterra form; this is the $k_F$ of R163_401 2.4(iv)). Put
$\kappa_x:=\check\Psi_x=$ the cross-correlation of $F$ and $H_x$, supported in $[-2T,2T]$. Then for $a\ne b$
$$W(H_a,H_b)=\underbrace{\frac1{2\pi}\int m\,\frac{G^2\,d\tau}{(\tau-a)(\tau-b)}}_{\mathrm{Arch}_{ab}}+\underbrace{\sum_\pm\frac{G(\pm\frac i2)^2}{(\pm\frac i2-a)(\pm\frac i2-b)}}_{\mathrm{Pol}_{ab}}-\sum_{n<e^{2T}}\frac{\Lambda(n)}{\sqrt n}\,k^{(n)}_{ab},\qquad k^{(n)}_{ab}=\frac{(\kappa_a-\kappa_b)(\log n)+(\kappa_a-\kappa_b)(-\log n)}{a-b}.$$
*Proof.* (0.1) with $\Psi=\Psi_{ab}$ and $\check\Psi_{ab}=(\kappa_a-\kappa_b)/(a-b)$. ∎

*Reading.* Given $F$, the system $\{W(H_a,H_b)=0\}$ is linear in the $N$ unknowns $(\Lambda(n))_{n<e^{2T}}$ with infinitely many
equations; consistency holds because $F$ was built from those $\Lambda(n)$. If the $N$ functions $k^{(n)}|_{X}$ are linearly
independent, $F$ determines the vector $(\Lambda(n))_{n<e^{2T}}$ (an inverse statement, ARGUED; no sign). The "finitely many atoms
vs infinitely many nodes" count is therefore a statement about the *determination* of $\Lambda$ by $F$, not about the zeros.

## 3. Theorem 3 (interpolation identity). PROVED for $F\in C^1_c(I_T)$ real with $\widehat F$ even or odd

Let $\mathrm{Im}\,x>\frac12$. Then
$$\Phi(x):=\sum_\rho\frac{G(t_\rho)^2}{t_\rho-x}=C_T(x)-i\,G(x)^2\,\mathcal T_T(x),\tag{3.1}$$
$$C_T(x)=\frac1{2\pi}\int_{\mathbb R}\frac{\sigma_T(\tau)G(\tau)^2}{\tau-x}\,d\tau+\sum_\pm\frac{G(\pm\frac i2)^2}{\pm\frac i2-x},\qquad
\mathcal T_T(x)=\sum_{\log n\ge2T}\Lambda(n)\,n^{-\frac12+ix}=-\frac{\zeta'}{\zeta}(\tfrac12-ix)-\sum_{\log n<2T}\Lambda(n)n^{-\frac12+ix}.$$

*Proof.* $h:=G^2/(\tau-x)$ is holomorphic in $|\mathrm{Im}\,\tau|\le\frac12+\varepsilon$ ($\varepsilon<\mathrm{Im}\,x-\frac12$) and $O(|\tau|^{-3})$ there
($F\in C^1_c$ gives $G=O(|\tau|^{-1})$ on strips), so Weil's explicit formula (0.1) holds for $h$ with **all** $n$ (the support
truncation is no longer automatic). Compute $\check h(u)$ for $|u|>2T$ by contour shift: $G^2e^{-i\tau u}$ is bounded by $e^{(2T-u)\mathrm{Im}(-\tau)}$-type
factors, so for $u>2T$ close downward, no pole, $\check h(u)=0$; for $u<-2T$ close upward around the pole $x$:
$\check h(u)=iG(x)^2e^{-ixu}$. Hence the terms $\log n\ge2T$ contribute $-\sum\frac{\Lambda(n)}{\sqrt n}\,iG(x)^2n^{ix}$, which converges since
$|n^{ix}|=n^{-\mathrm{Im}x}$, $\mathrm{Im}\,x>\frac12$. The terms $\log n<2T$ with the archimedean term give $\frac1{2\pi}\int\sigma_Th$; the polar terms are
$h(\pm\frac i2)$. ∎

For the witness ($F\in\mathcal D_T$ only) the identity follows by approximation in $\mathcal D_T$ if the zero sum converges
uniformly on compacta of $\mathrm{Im}\,x>\frac12$; the argument is that of R163_401 Lemma 3.0 with the extra factor $|t_\rho-x|^{-1}$
(which only helps). ARGUED.

**Corollary 3.1. PROVED (given (3.1)).**
- (a) *Continuation.* Both sides continue meromorphically to $\mathrm{Im}\,x>0$. $C_T$ is holomorphic there except at $x=\frac i2$;
  the pole of $\mathcal T_T$ at $x=\frac i2$ (from $s=1$) cancels it; the poles of $\Phi$ at the upper-half-plane zero ordinates
  $\gamma\pm i\delta$ are exactly those of $-iG^2\mathcal T_T$, with matching residues $-G(t)^2\cdot\mathrm{mult}$ (a tautology of (3.1)).
- (b) *Locality on the node set.* For $x_0\in X$, as $x\to x_0$ from above, $G(x)^2\mathcal T_T(x)\to0$ ($G^2$ has a double zero,
  $\mathcal T_T$ at most a simple pole on $\mathbb R$), and $C_T(x_0+i0)=\Omega(x_0)$ (the Plemelj jump $\frac i2\sigma_TG^2$ vanishes at
  $x_0$). So (3.1) restricted to $X$ **is** the node system, and the infinite arithmetic tail $(\Lambda(n))_{n\ge e^{2T}}$ drops out
  exactly there. This is the precise form of R163_603 R5.3 for the node system.
- (c) *Where the off-line zeros live.* The band part $C_T$ (all the finite-vector arithmetic) is holomorphic off $\mathbb R$;
  every off-line residue $G(t_q)^2$ is carried by the tail term $G^2\mathcal T_T$. So on the prime side of (3.1) the quantity
  whose sign (A-loc) concerns, $\mathrm{Re}\,G(t_q)^2$, appears only multiplied by the tail of the Dirichlet series and never in the
  finite-atomic part. No evaluation of (3.1) on $X$ (where the system lives) reaches it individually.

## 4. Proposition 4 (zero-side Loewner split). PROVED

On the zero side $\Omega|_X$ splits as $R_{\rm on}+R_{\rm off}$, $R_{\rm on}(x)=\sum_{\rm on}\frac{G(\gamma)^2}{\gamma-x}$,
$R_{\rm off}(x)=\sum_q\sum_{t\in q}\frac{G(t)^2}{t-x}$ (4-point quartets, R163_790 F10). Then on $X$
$$L_{R_{\rm on}}+L_{R_{\rm off}}=\mathrm{diag}(d),\qquad c^{\!\top}L_{R}c=\sum_k\mu_k\,r_c(t_k)^2,\ \ r_c(z)=\sum_{a\in S}\frac{c_a}{z-a},$$
and $L_{R_{\rm on}}|_S\succ0$ for every finite $S\subset X$.
*Proof.* $L_R(a,b)=\sum_k\mu_k/((t_k-a)(t_k-b))$ for $R=\sum\mu_k/(t_k-x)$. For $R_{\rm on}$, $\mu_k=G(\gamma_k)^2\ge0$, and $r_c$ (rational,
$\le|S|-1$ zeros) cannot vanish at the infinitely many on-line $\gamma$ with $G(\gamma)\ne0$ (balance, 401 §4.1, plus Jensen against
$\gg R\log R$ distinct ordinates). ∎

*Reading.* $c^\top(L_{\rm on}+L_{\rm off})c=W(\sum c_aH_a)$: this is the quadrature 2.4(iii) on $\mathrm{span}\{H_a\}_{a\in S}$, i.e.
$\sum_k\mu_kr_c(t_k)^2=\sum_ac_a^2d_a$. The resulting inequality $c^\top L_{\rm off}c<c^\top\mathrm{diag}(d)c$ bounds the in-cone defect by node weights; it is
not a sign on any quartet. In the RH picture ($L_{\rm off}=0$) $R_{\rm on}$ is a Pick function, increasing between its poles, and
$\Omega|_X=0$ is Stieltjes interlacing; the off-line part is what breaks Pick-ness, and nothing in the system controls by how much.

**Proposition 4.1 (rank arguments do not separate $M_m$). PROVED.** Write the prime-side off-diagonal system as
$\mathrm{Arch}+\mathrm{Pol}=\sum_{n<e^{2T}}\frac{\Lambda(n)}{\sqrt n}k^{(n)}$ on $X\times X$ (Prop 2): the archimedean+polar Loewner matrix lies in an $N$-dimensional
span. For $M_m$ (Thm 5) the same holds with one more matrix $k^{(\beta)}$, the Loewner matrix of $x\mapsto\sum_{t\ \rm added}G(t)^2/(t-x)$, of rank $\le4m$.
So "finite span / finite rank of the arithmetic part" holds for $M_m$ with $N+1$ terms (or $N+4m$ rank-one terms). Any argument
whose only arithmetic input is *finiteness* of the prime-side dictionary is therefore $M_m$-blind. Also $L_{R_{\rm off}}$ has rank
$\le4m$ for $M_m$ and rank $=4\cdot\#\{q\}$ for ζ, which is unknown (finitely many off-line zeros is not excluded for ζ), so rank of
$L_{\rm off}$ does not separate either.

## 5. Theorem 5 (the $M_m$ falsifier, made precise). PROVED

$M_m=\xi\cdot\prod_{j\le m}R_j$ with $R_j$ the rational quartet factor adding $q_j=\{t_j,\bar t_j,-t_j,-\bar t_j\}$, $t_j=\gamma_j-i\delta_j$.
(Record: $M_m$ has a first contact, Paper 48 Tab. 1.) Its window form is $W^{M}_T=W_T+Q_m$, $Q_m(F)=\sum_j\sum_{t\in q_j}(\widehat F\widehat F^\#)(t)$.
- (a) *Prime side.* $Q_m(F)=\int c_F(u)\beta_m(u)\,du$ with $\beta_m(u)=\sum_j\sum_{t\in q_j}e^{-itu}=\sum_j4\cos(\gamma_ju)\cosh(\delta_ju)$ on $(-2T,2T)$
  (from $(\widehat F\widehat F^\#)(t)=\int c_F(u)e^{itu}du$; the sign of the exponent is immaterial after summing the quartet). Equivalently $\sigma^M_T=\sigma_T+\widehat{\beta_m\mathbf 1_{(-2T,2T)}}$ modulo symbols annihilating $PW_T$-products.
  So **$M_m$'s prime side is ζ's atomic comb plus an absolutely continuous density which is a real-analytic exponential polynomial,
  nonzero on every subinterval of $(-2T,2T)$** (an exponential polynomial vanishing on an interval is $\equiv0$). On the τ-side the added
  symbol is a sum of sinc-type bumps of width $\asymp1/T$ centred at $\pm\gamma_j$: it is **cell-localised exactly at the added quartets**,
  whereas $\sigma_T-m$ is almost periodic with frequencies $\log n$ and total variation budget $V_T$ at every height.
- (b) *Node level.* $M_m$'s node system on its own node set $X_M$ is $C^\zeta_T[G_M](x)+\sum_j\sum_{t\in q_j}\frac{G_M(t)^2}{t-x}=0$; the extra term
  is a rational function of $x$ with poles at the added points. In (3.1) this term sits in the band part, not in the tail: for ζ the
  band part $C_T$ has no non-real poles but $\pm\frac i2$, for $M_m$ it has $4m$ more. This is the exact place where the prime sides differ.
- (c) *Does §§1–4 use the difference?* **No.** Thm 1, Prop 4, Prop 4.1 and the structure of Prop 2 hold for every symbol $\sigma$ with
  $W^\sigma\ge0$, a nonzero kernel, and a zero-side identity; $\sigma^M$ is such a symbol. Thm 3 holds for $M_m$ with the
  tail $\mathcal T_T$ replaced by $-\frac{\Xi_M'}{\Xi_M}$-tail and $C_T$ by $C_T+$(added rational term); Cor 3.1(b) holds verbatim.
  So no identity or Gram-matrix property of §§1–4 can force (A-loc): it would force it for $M_m$, whose witness violates it (balance,
  401 Cor 4.1 applied to $M_m$, with ζ's on-line zeros and only the added quartets off line if ζ satisfies RH; and in either case, by T5.2).
  This is T5.2 for the node-pair system, now with value-level (not only zero-statistic) prime-side inputs, answering F12.

**Proposition 5.1 (the one atomic consequence: a local count without sign).** For every $\Psi=\widehat\Phi\widehat\Phi^\#\ge0$ on $\mathbb R$ of type $2T$,
$$\Big|\sum_\rho\Psi(t_\rho)-\frac1{2\pi}\int m\Psi-\Psi(\tfrac i2)-\Psi(-\tfrac i2)\Big|\le\frac{V_T}{2\pi}\lVert\Psi\rVert_{L^1(\mathbb R)},\qquad V_T=\sum_{n<e^{2T}}\frac{2\Lambda(n)}{\sqrt n}.$$
PROVED: (0.1) and $|\check\Psi|\le\frac1{2\pi}\lVert\Psi\rVert_1$. This uses atomicity (finitely many atoms with total mass $V_T$, height-independent),
and $M_m$ satisfies it only if $\big|\sum_{t\ \rm added}\Psi(t)\big|$ stays within $2\cdot\frac{V_T}{2\pi}\lVert\Psi\rVert_1$ when $\Psi$ is centred at an added quartet.
For a Fejér bump $\Psi(0)\le\frac T\pi\lVert\Psi\rVert_1$, so one quartet contributes $\lesssim\frac{2T}\pi\cosh(2T\delta)\lVert\Psi\rVert_1$, against the budget
$\frac{V_T}\pi\lVert\Psi\rVert_1$; at $T\approx0.8$ ($V_T\approx3.6$) a single quartet is **not** separated, a cluster of $\gtrsim3$ quartets in one cell is
(ARGUED, constants not certified). In any case Prop 5.1 is a two-sided bound on the *total* local mass at resolution $1/T$; at heights
$\gamma_q>3\cdot10^{12}$ a cell of length $\pi/T\approx3.9$ contains $\approx17$ on-line ordinates, which can absorb $\mathrm{Re}\,\Psi(t_q)$ of either sign.
It does not see $\mathrm{Re}\,G(t_q)^2$ individually. So the one place where atomicity enters gives no (A-loc).

## 6. What the separating property must be. ARGUED

- The deletion model $\zeta_a$ ($\Lambda\mathbf 1_{n\ge5}$) has an atomic prime side and a first contact in $[0.4608,0.60]$ but **no** zero side
  (record; check: Poisson summation over the zero lines of $1-p^{-s}$ produces $c_F(0)$ and $p^{+m/2}$ terms, never $p^{-m/2}c_F(m\log p)$ alone).
  $M_m$ has a zero side but a non-atomic prime side. ζ has both. So any argument for (A-loc) must use the **conjunction** "atomic band
  symbol and zero-side identity with positive integer multiplicities".
- The $M_m$ density $\beta_m$ can be cancelled on $(-2T,2T)$ by moving on-line points with **real** weights: $\nu=\sum_kh\,\check\phi(kh)\delta_{kh}$
  with $\phi=\beta_m\chi$ smooth, $\mathrm{supp}\,\phi\subset(-\pi/h,\pi/h)$, $\pi/h>2T$, has window transform $\beta_m$ exactly (Poisson). So the
  configuration "ζ's zeros + $q_j$ − ν" has ζ's atomic prime side and violates (A-loc) at its witness, **but has non-integer multiplicities**.
  Hence: an argument from the finite vector $(\Lambda(n))_{n<e^{2T}}$ plus the node system can separate only through the integrality of
  zero multiplicities (equivalently: through the fact that the zero side is a sum of point evaluations with weights in $\mathbb Z_{>0}$).
  This places (A-loc) inside the integrality-defect question of phase 163 and nowhere else.
- Whether some configuration with integer multiplicities, ζ's atomic window functional, and an (A-loc)-violating witness exists is
  equivalent (by the window non-identifiability: the witness depends only on the window functional) to the failure of every
  window-data proof of (A-loc). OPEN.

## 7. Answer to the task

- Prime side and zero side of the full system written: Thm 1, Prop 2 (prime), Prop 4 (zero), Thm 3 (both at once, with the tail).
- Identity/inequality from the atomic finite vector forcing (A-loc): **none found**, and the following are excluded:
  rank/positivity of $[W(H_a,H_b)]$ (it is $\mathrm{diag}(d)$, Thm 1(b)); finite-span/"finitely many atoms vs infinite $X$" (Prop 4.1, $M_m$ has
  the same property); evaluations of (3.1) on $X$ (tail and off-line residues invisible, Cor 3.1). The only atomic inequality (Prop 5.1) is a
  sign-free local count.
- Falsifier: $M_m$'s prime side differs exactly by $\beta_m$ (Thm 5(a)); §§1–4 do not use it; Prop 5.1 uses it but gives no sign; the
  only remaining handle is integer multiplicities (§6).

**(A-loc): OPEN. Row D: OPEN.** New here: the collapse theorem (node-pair system = Loewner matrix of one function on its zero set),
the interpolation identity (3.1) with the exact tail $G^2\mathcal T_T$, the localisation of off-line residues in the tail, the exact
prime-side difference $\beta_m$ for $M_m$, and the real-weight compensation showing that only integrality of zero multiplicities can separate.
