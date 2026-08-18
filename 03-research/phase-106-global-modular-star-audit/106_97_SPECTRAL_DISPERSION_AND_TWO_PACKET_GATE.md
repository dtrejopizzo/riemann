# 106.97 — Spectral dispersion and the two-packet gate

## Purpose and verdict

Document 106.96 introduced the second Krylov certificate

\[
 Q_2=Q_1+
 { (m_0m_2-m_1^2)^2
  \over (m_0+m_1)D_2},
 \qquad
 D_2=(m_0+m_1)(m_2+m_3)-(m_1+m_2)^2.             \tag{1}
\]

This note identifies exactly what the correction in (1) measures.  It is
the spectral dispersion of the radical-conditioned response, divided by
the adaptive price of that dispersion.  In particular, if
\(Q_1<\delta_J\), then

\[
 \boxed{
 (m_0m_2-m_1^2)^2>
 (\delta_J-Q_1)(m_0+m_1)D_2}                     \tag{2}
\]

is exactly equivalent to \(Q_2>\delta_J\).

The note then derives a finite, signed two-packet condition which implies
(2), and expands all four moments using one common radical correction and
the literal ordinary-prime observation maps.  This is a genuine
strengthening of the matched filter.  It is not an automatic consequence
of positive Stieltjes moments: an exact three-point counterexample shows
that the true gain can cross while \(Q_2\) still misses the threshold.
Thus (2) is a falsifiable sufficient arithmetic target, while the exact
force-bearing condition remains \(G_J>\delta_J\).

## 1. Spectral pair identities

Retain the notation of 106.96:

\[
 B=\Pi UA^{-1}U^*\Pi\succeq0,
 \qquad z=\Pi v,
 \qquad m_j=\langle z,B^jz\rangle.                \tag{3}
\]

Let

\[
 d\rho(t)=d\langle z,E_B(t)z\rangle,
 \qquad R=m_0,
 \qquad \mu={m_1\over R},                        \tag{4}
\]

Throughout the nonzero-response case considered below, \(R=m_0>0\).

and put

\[
 N_2=m_0m_2-m_1^2.                                \tag{5}
\]

### Theorem 1 — Exact dispersion/cost decomposition

One has

\[
 \boxed{
 N_2={1\over2}\iint(s-t)^2\,d\rho(s)d\rho(t),}  \tag{6}
\]

and

\[
 \boxed{
 D_2={1\over2}\iint
 (s-t)^2(1+s)(1+t)\,d\rho(s)d\rho(t).}           \tag{7}
\]

If \(N_2>0\), define the dispersive pair probability

\[
 d\omega(s,t)=
 {(s-t)^2\over2N_2}\,d\rho(s)d\rho(t)           \tag{8}
\]

and its adaptive price

\[
 \kappa_\wedge=
 \int(1+s)(1+t)\,d\omega(s,t)={D_2\over N_2}.   \tag{9}
\]

Writing

\[
 \mathsf V={N_2\over R^2},                       \tag{10}
\]

the first two Krylov certificates satisfy

\[
 \boxed{
 Q_1={R\over1+\mu},
 \qquad
 Q_2={R\over1+\mu}
       \left(1+{\mathsf V\over\kappa_\wedge}\right).}       \tag{11}
\]

Consequently, when \(Q_1<\delta_J\), condition (2) is equivalently

\[
 \boxed{
 {\mathsf V\over\kappa_\wedge}>
 {\delta_J(1+\mu)\over R}-1.}                   \tag{12}
\]

#### Proof

Expand

\[
 {1\over2}\iint(s-t)^2\,d\rho(s)d\rho(t)
 =m_0m_2-m_1^2.
\]

The same expansion after multiplying by \((1+s)(1+t)\) gives

\[
 (m_0+m_1)(m_2+m_3)-(m_1+m_2)^2,
\]

which proves (6)--(7).  Substitute \(D_2=\kappa_\wedge N_2\) and
\(N_2=R^2\mathsf V\) in (1).  This gives (11), and rearranging
\(Q_2>\delta_J\) gives (12). \(\square\)

Thus \(\mathsf V\) is the dispersion recovered after MF, whereas
\(\kappa_\wedge\) is the exact price charged by the old-mode adaptation.

## 2. Exterior geometry and a quantitative lower bound

### Theorem 2 — Wedge representation

The two determinants in Theorem 1 are

\[
 \boxed{
 N_2=\|z\wedge Bz\|^2,}                          \tag{13}
\]

\[
 \boxed{
 D_2=
 \left\|(I+B)^{1/2}z\wedge
             (I+B)^{1/2}Bz\right\|^2.}          \tag{14}
\]

If \(u=\|B\|\), then

\[
 N_2\le D_2\le(1+u)^2N_2,                       \tag{15}
\]

and hence

\[
 \boxed{
 {N_2\over(m_0+m_1)(1+u)^2}
 \le Q_2-Q_1
 \le {N_2\over m_0+m_1}.}                       \tag{16}
\]

#### Proof

Equation (13) is the Gram determinant of \(z,Bz\) in the original
Hilbert norm.  Equation (14) is the same Gram determinant in the
\((I+B)\)-norm.  On the second exterior power, the spectrum of
\(\bigwedge^2(I+B)\) lies in \([1,(1+u)^2]\).  This proves (15), and
(16) follows from (1). \(\square\)

The lower bound has a direct non-alignment form:

\[
 N_2=R\|P_{z^\perp}Bz\|^2.                       \tag{17}
\]

Thus the second filter improves MF precisely when the old-regression
image \(Bz\) has a component transverse to the new response \(z\).

## 3. A signed two-packet certificate

Let \(\phi_0,\phi_1\) be any two orthonormal vectors in the observation
space after the complete radical anti-short, and set

\[
 a_i=\langle\phi_i,z\rangle,
 \qquad
 b_i=\langle\phi_i,Bz\rangle
 =\langle A^{-1/2}U^*\Pi\phi_i,
          A^{-1/2}U^*z\rangle.                   \tag{18}
\]

The corresponding coordinate of the exterior vector gives

\[
 \boxed{
 N_2\ge |a_0b_1-a_1b_0|^2.}                     \tag{19}
\]

### Corollary 3 — Two-packet dispersion domination

If \(Q_1<\delta_J\) and

\[
 \boxed{
 |a_0b_1-a_1b_0|^2>
 (\delta_J-Q_1)(m_0+m_1)(1+\|B\|)^2,}           \tag{20}
\]

then

\[
 Q_2>\delta_J,
 \qquad
 \tau_{d+1}(Y)>\delta_J\tau_d(Y).               \tag{21}
\]

#### Proof

Equation (19) and the lower estimate in (16) imply

\[
 Q_2-Q_1\ge
 {|a_0b_1-a_1b_0|^2
  \over(m_0+m_1)(1+\|B\|)^2}.
\]

Condition (20) therefore gives \(Q_2-Q_1>\delta_J-Q_1\).
The determinant implication is Theorem 3 of 106.96. \(\square\)

The two theta phases remain combined inside the signed determinant
\(a_0b_1-a_1b_0\) until its final modulus square.  Condition (20) also uses a
single common regression \(A^{-1}U^*z\), rather than a separate
regression for each prime.

## 4. Support separation criteria

The spectral formula gives two convenient sufficient tests.  Suppose
\(\operatorname {supp}\rho\subset[0,u]\).  Then

\[
 \kappa_\wedge\le(1+u)^2.                        \tag{22}
\]

If the normalized measure \(d\rho/R\) has mass at least \(\eta\) in
\([0,a]\) and mass at least \(\theta\) in \([b,u]\), where \(b>a\),
then the law of total variance gives

\[
 \boxed{
 \mathsf V\ge {\eta\theta\over\eta+\theta}(b-a)^2.}          \tag{23}
\]

Indeed, restrict first to the union of the two sets.  Its conditional
variance is at least
\(\eta\theta(b-a)^2/(\eta+\theta)^2\), and multiplying by the mass
\(\eta+\theta\) proves (23).  If the actual two masses are larger than
the declared lower bounds, use that \(xy/(x+y)\) is increasing in each
positive variable.

Combining (12), (22), and (23) yields the sufficient cluster condition

\[
 {\eta\theta\over\eta+\theta}(b-a)^2
 >(1+u)^2\left({\delta_J(1+\mu)\over R}-1\right).              \tag{24}
\]

There is also a canonical zero cluster.  Put

\[
 C=\Pi UA^{-1/2},
 \qquad B=CC^*,
 \qquad
 \eta_0={\|P_{\ker C^*}z\|^2\over R}.           \tag{25}
\]

Assume first that \(0\le\eta_0<1\).  If \(\eta_0=1\), then \(Bz=0\),
\(\mu=\mathsf V=0\), and \(Q_2=Q_1=G_Y=R\), so no dispersion estimate
is needed.

Conditioning on the positive spectral part and applying Jensen gives

\[
 \boxed{
 \mathsf V\ge {\eta_0\over1-\eta_0}\mu^2.}      \tag{26}
\]

Thus

\[
 {\eta_0\mu^2\over
  (1-\eta_0)(1+\|C\|^2)^2}
 >{\delta_J(1+\mu)\over R}-1                    \tag{27}
\]

is another explicit sufficient condition for (21).

## 5. Literal theta--prime expansion after the radical

Let \(D=\bigoplus_nD_n\) be the literal observation map over the finite
prime-power block.  Write the complete radical correction once, before
separating primes, as

\[
 \widetilde q=q_J^*+\Psi\zeta^*,
 \qquad
 \widetilde\Phi=\Phi+\Psi Z,                     \tag{28}
\]

where

\[
 \zeta^*=-(W^*W)^{-1}W^*v,
 \qquad
 Z=-(W^*W)^{-1}W^*U.                             \tag{29}
\]

The Moore--Penrose inverse is used if the declared radical dictionary
contains redundant columns.  Define

\[
 x_n=D_n\widetilde q,
 \qquad
 F_n=D_n\widetilde\Phi A^{-1/2},                 \tag{30}
\]

and

\[
 a_n=F_n^*x_n,
 \quad S_n=F_n^*F_n,
 \quad \xi=\sum_na_n,
 \quad S=\sum_nS_n.                              \tag{31}
\]

Then the four moments are exactly

\[
 \boxed{
 \begin{aligned}
 m_0&=\sum_n\|x_n\|^2,\\
 m_1&=\|\xi\|^2,\\
 m_2&=\xi^*S\xi,\\
 m_3&=\xi^*S^2\xi.
 \end{aligned}}                                  \tag{32}
\]

In particular, (32) contains the literal double, triple, and quadruple
products of the ordinary weights \(\Lambda(n)\), but every product uses
the same radical correction (28).  No prime-wise shorting has occurred.

There is also an exact two-row identity.  Since \(Bz=F\xi\),

\[
 \boxed{
 N_2={1\over2}\sum_{n,\ell}\iint
 \left|x_n(s)(F_\ell\xi)(t)
       -(F_n\xi)(s)x_\ell(t)\right|^2\,ds\,dt.} \tag{33}
\]

This is the literal ordinary-prime form of \(\|z\wedge Bz\|^2\).

For each prime-power channel, let \(e_n\) be the normalized midpoint
packet of 106.73 and let \(P_n\) be its one-dimensional orthogonal
projection.  Define the exact packet coordinates by

\[
 P_nx_n=-\sqrt{\beta_n}\eta_ne_n,
 \qquad
 P_nF_n=-\sqrt{\beta_n}e_nr_n,                   \tag{34}
\]

where \(r_n\) is a row vector and \(\beta_n\) contains the actual von
Mangoldt weight.  Put

\[
 s_n=r_n\xi.                                     \tag{35}
\]

Because the projection \(P=\bigoplus_nP_n\) is contractive on the second
exterior power, (33) gives the rigorous full-system lower bound

\[
 \boxed{
 N_2\ge N_2^{\rm pkt}:=
 \sum_{n<\ell}\beta_n\beta_\ell
 \left|\eta_ns_\ell-\eta_\ell s_n\right|^2.}    \tag{36}
\]

Formula (36) is the desired nonlocal two-prime phase determinant.  It
uses the full common regression
\(\xi=F^*z\), not a regression recomputed in each packet.  Define the
exact packet remainders by

\[
 \eta_n=A_n(\widetilde q)+\rho_n(\widetilde q),
 \qquad
 r_n=A_n(\widetilde\Phi A^{-1/2})
       +\rho_n(\widetilde\Phi A^{-1/2}).          \tag{37}
\]

Thus no informal subtraction of a nonlinear ``compression error'' is
needed: retain the exact remainders inside \(\eta_n,r_n\), and estimate
the determinant only afterwards.  The uniform bounds of 106.73 and
106.81 apply to their declared zero-mode/jet blocks.  Extending those
bounds to the radical components of \(\widetilde q,\widetilde\Phi\) is a
separate analytic obligation; the exact lower bound (36) does not depend
on that extension.

## 6. Why the second level is nearly exact in the theta tail

The Krylov variational formula has the approximation interpretation

\[
 G_Y-Q_k=
 \inf_{\deg p<k}
 \int(1+t)\left|p(t)-{1\over1+t}\right|^2d\rho(t).             \tag{38}
\]

Taking the truncated Neumann polynomial

\[
 p_{k-1}(t)=1-t+\cdots+(-t)^{k-1}
\]

gives the rigorous estimate

\[
 \boxed{
 0\le G_Y-Q_k
 \le\int {t^{2k}\over1+t}\,d\rho(t)
 \le m_0\|B\|^{2k}.}                            \tag{39}
\]

For \(k=2\),

\[
 \boxed{
 Q_2\ge m_0-m_1+m_2-m_3,
 \qquad
 0\le G_Y-Q_2\le m_0\|B\|^4.}                 \tag{40}
\]

This explains the near equality between \(Q_2\) and the exact gain in
the finite theta diagnostics.  If a tail block has scale
\(m_0=O(\Theta)\), \(\|B\|=O(\Theta)\), then

\[
 Q_2-Q_1=O(\Theta^3),
 \qquad
 G_Y-Q_2=O(\Theta^5).                            \tag{41}
\]

These orders require constants uniform in the moving row, including the
norms of \(A^{-1}\), the selected residual, and the radical dictionary.
The fixed-block asymptotic of 106.73 alone does not provide that
uniformity.  More generally, if \(m_0=O(\Theta_q)\) and
\(\|B\|=O(\Theta_U)\), then the two orders are
\(O(\Theta_q\Theta_U^2)\) and
\(O(\Theta_q\Theta_U^4)\), respectively.

Near equality alone does not determine on which side of \(\delta_J\)
the two quantities lie.  A closure through (2) still requires the
matched scale

\[
 \delta_J-Q_1=O(\Theta^3)                        \tag{42}
\]

as a necessary scale match, followed by a leading constant strictly
smaller than the two-row energy in (33) or (36).

## 7. Exact countergate

The condition \(Q_2>\delta\) is not forced by \(G>\delta\).  Take

\[
 B=\operatorname {diag}(1,2,3),
 \qquad
 z=\sqrt{12/13}\,(1,1,1),
 \qquad
 \delta={649\over650}.                           \tag{43}
\]

Then

\[
 G=\langle z,(I+B)^{-1}z\rangle=1>{649\over650},               \tag{44}
\]

whereas

\[
 (m_0,m_1,m_2,m_3)={1\over13}(36,72,168,432),
 \qquad
 Q_2={324\over325}={648\over650}<\delta.         \tag{45}
\]

Indeed, the two sides of (2) are respectively

\[
 {746496\over28561}
 \quad\hbox{and}\quad
 {762048\over28561}.                             \tag{46}
\]

Thus even a \(0.31\%\) relative Krylov error may contain the complete
sign margin.  This also agrees with the earlier Phase-77 warning that a
uniformly fixed number of cyclic moments need not resolve a critical
spectral window.  The operator here is different, so that warning is a
semantic prior rather than a direct no-go theorem; (43)--(46) is the
direct finite countergate for the present row.

## 8. The next arithmetic statement

For every negative physical pivot there are now three nested options:

1. prove \(Q_1>\delta_J\) by MF;
2. if MF misses, prove the spectral-dispersion inequality (2), preferably
   through the signed two-packet determinant (20) or the literal two-row
   sum (33);
3. if level two misses, increase the Krylov depth and use the exact error
   bound (39), without claiming that a fixed depth is universal.

At level two, the new literal theorem is precisely a theta-tail matched
lower bound of the form

\[
 \boxed{
 N_2>
 (\delta_J-Q_1)(m_0+m_1)(1+\|B\|)^2,}           \tag{47}
\]

or its sharper exact version (2).  Positivity proves only \(N_2\ge0\);
observability proves only \(N_2>0\).  The missing information is the
quantitative comparison with \(\delta_J-Q_1\), at the common theta scale
and with Gamma, the pole, and the retained prime head still coupled in
the definition of that deficit.

## 9. Reproduction

The spectral pair identities, the closed formula for \(Q_2\), and the
exact rational countergate are checked by

```bash
cd 03-research/phase-106-global-modular-star-audit
python3 tools/q2_dispersion_identity_check.py
```

The random rows are floating-point algebraic diagnostics.  The
countergate itself uses `fractions.Fraction` throughout and is exact.
