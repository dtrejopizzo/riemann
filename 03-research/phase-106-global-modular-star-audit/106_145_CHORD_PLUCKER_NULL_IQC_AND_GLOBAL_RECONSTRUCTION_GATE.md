# 106.145 — Chord Pluecker null-IQC and global reconstruction gate

## 1. Purpose and verdict

Document 106.144 proves that every operation which acts separately on a
marked chord fiber is rigid after the complete radical anti-short.  This
note tests the first genuinely cross-chord algebraic candidate.

For a finite family of spatial vertices, the physical chord amplitude is

\[
 p_{ij}=\sqrt{K(x_i)K(x_j)}\{q(x_i)-q(x_j)\}.
 \tag{1}
\]

It is a two-by-two determinant and therefore satisfies all Pluecker
relations.  The decisive point is that one row of the determinant is fixed
by the theta ground state.  Consequently the apparent Grassmannian is in
fact a linear incidence space: after the fixed diagonal normalization,
\(p\) is an ordinary graph gradient.  Every Pluecker relation follows from
the weighted triangle relations.

This has two exact consequences.

1. Every Hermitian quadratic null-IQC obtained from the chord Pluecker
   relations is already a constraint-generated Hodge null-IQC.  It belongs
   to the class exhausted by 106.111 and 106.113.
2. The continuous chord-swap identity of 106.144 produces an exact global
   null-IQC, but only antisymmetrizes the displacement measure.  It leaves
   the compressed signed form unchanged and supplies no positive reserve.

There is nevertheless an exact nonlocal reconstruction identity.  If
\(Cq\) is the complete oriented chord field, then a convolutional operator
\(R\) satisfies

\[
 RCq=q-\frac{(hq)*K}{c_Kh}.
 \tag{2}
\]

Thus \(R\) is a left inverse on the mean-periodic complement.  This is a
genuine global identity, not a local Hodge decomposition.  Its direct
Gamma Schur realization is, however, unbounded: the exact fiber norm tends
to infinity double exponentially in the spatial tails.  More generally,
every left inverse agrees on the physical range, and its intrinsic norm is
at most \(\sqrt2\) if and only if the missing physical surplus holds.  An
alternative reconstruction kernel can change an ambient extension but
cannot lower this range norm.

Therefore neither chord Pluecker algebra nor the bare reconstruction
identity proves the surplus.  The surviving construction must add an
arithmetic estimate which is not a consequence of gradient integrability:
it must prove the critical \(\sqrt2\) range bound using the literal joint
prime--Gamma source after the complete anti-short.

No zero-location statement is used in the rigidity or unboundedness
proofs.

## 2. Semantic nonduplication audit

The following earlier results are close but distinct.

* 106.95 writes the finite crossing as a projected exterior-volume
  inequality and names a globally signed projected Pluecker estimate as a
  possible successor.  It does not identify the defining ideal of the
  physical chord field.
* 106.97 uses exterior products of observation and Krylov columns.  Those
  wedges measure spectral dispersion after one common regression; they
  are not the two-endpoint determinants in (1).
* E101.077 and the subsequent Phase-101 compound audit use jet Gram wedges
  to discriminate a resolved off-line point.  E101.078--E101.085 show that
  nonlinear wedges cannot be applied after unlabeled spectral aggregation.
  They do not contain the weighted chord-triangle theorem below.
* 106.111 proves finite-incidence Hodge rigidity, and 106.113 closes an
  infinite boundary-flux escape.  The result below connects the apparently
  nonlinear Pluecker candidate exactly to that already audited incidence
  class.
* 106.143 classifies bounded Hermitian IQCs abstractly, while 106.144 proves
  the full-chord symmetry and fiberwise rigidity.  The present note gives
  the missing finite defining equations, the continuous swap null-IQC, and
  the global reconstruction norm audit.

Thus the determinant representation and identity (2) are new coordinates
inside the phase.  The theorem they would still have to prove is not new:
it is the complementary contraction of 106.39.

## 3. The physical chord Grassmannian is linear

Fix distinct vertices \(x_1,\ldots,x_N\), put

\[
 w_i=\sqrt{K(x_i)}>0,
 \qquad
 v_i=(w_iq_i,w_i)^T,
 \tag{3}
\]

and orient every edge by \(p_{ji}=-p_{ij}\).  Then

\[
 \boxed{
 p_{ij}=\det(v_i,v_j)=w_iw_j(q_i-q_j).}
 \tag{4}
\]

### Theorem 1 — Weighted triangle equations are complete

A skew edge field \(p=(p_{ij})\) has the form (4) for some vertex field
\(q\) if and only if

\[
 \boxed{
 w_i p_{jk}-w_j p_{ik}+w_k p_{ij}=0
 \qquad(i,j,k\text{ distinct}).}
 \tag{5}
\]

Consequently, for every four distinct vertices,

\[
 \boxed{
 p_{ij}p_{k\ell}-p_{ik}p_{j\ell}+p_{i\ell}p_{jk}=0,}
 \tag{6}
\]

and (6) is an algebraic consequence of the linear equations (5).

#### Proof

Substitution of (4) into the left side of (5) gives

\[
 w_iw_jw_k
 \{(q_j-q_k)-(q_i-q_k)+(q_i-q_j)\}=0.
 \tag{7}
\]

Conversely, divide by \(w_iw_jw_k\) and set

\[
 b_{ij}=\frac{p_{ij}}{w_iw_j}.
 \tag{8}
\]

Equation (5) becomes

\[
 b_{jk}-b_{ik}+b_{ij}=0.
 \tag{9}
\]

Choose a reference vertex \(r\), set \(q_r=0\) and
\(q_i=b_{ir}\).  Equation (9) with \(k=r\) gives
\(b_{ij}=q_i-q_j\), hence (4).

For (6), either substitute (4) directly or observe that the two-vector is

\[
 p=(wq)\wedge w.
 \tag{10}
\]

Therefore \(p\wedge p=0\).  Its four-coordinate components are (6).
Since (5) is equivalent to the representation (10), every component of
\(p\wedge p\) follows from (5). \(\square\)

The usual Pluecker variety is nonlinear because both rows of a two-by-
\(N\) matrix vary.  Here the second row \(w\) is fixed.  The physical
variety is the linear subspace \(w\wedge\mathbb C^N\).

## 4. Classification of chord Hermitian null-IQCs

Let \(\mathscr H_E=\mathbb C^{\binom N2}\), let
\(\mathscr S_w\subset\mathscr H_E\) be the range in Theorem 1, and let
\(P\) be the orthogonal projection onto \(\mathscr S_w\).  Write
\(C=I-P\).  The rows of \(C\) may equivalently be chosen from the weighted
triangle constraints (5).

### Theorem 2 — Every Hermitian Pluecker null is a Hodge null

Let \(M=M^*\) on \(\mathscr H_E\).  Then

\[
 \langle p,Mp\rangle=0\quad(p\in\mathscr S_w)
 \tag{11}
\]

if and only if

\[
 PMP=0.
 \tag{12}
\]

In that case, with

\[
 Y=M-\frac12CMC,
 \tag{13}
\]

one has the exact constraint representation

\[
 \boxed{M=C^*Y+Y^*C.}
 \tag{14}
\]

#### Proof

Complex polarization of (11) gives
\(\langle p,Mr\rangle=0\) for every \(p,r\in\mathscr S_w\), which is
(12).  Conversely (12) immediately implies (11).  Since \(C=C^*=C^2\),

\[
 C^*Y+Y^*C=CM+MC-CMC.
 \tag{15}
\]

Expanding \(M=(P+C)M(P+C)\) and using \(PMP=0\) shows that the right side
of (15) is exactly \(M\). \(\square\)

Polarizing (6) between two vertex fields and then taking the second field
to be the conjugate of the first does produce real and imaginary Hermitian
quadratic null relations.  Theorem 2 shows that all of them have the form
(14).  They are generated by the linear incidence constraints and do not
constitute an additional post-Hodge channel.

This is also an exact Finsler audit.  Adding \(C^*Y+Y^*C\) may change an
ambient edge matrix, but its compression to the physical gradient range is
zero.  A choice of \(Y\) which makes the ambient matrix positive exists
only if the original compressed matrix is already positive on
\(\mathscr S_w\).

### Four-vertex falsifier

Take \(w_i=1\), positive weights on the path edges
\(12,23,34\), and weight \(-1\) on edge \(14\).  For

\[
 q=(1,0,0,-1),
 \tag{16}
\]

the signed edge form is

\[
 (q_1-q_2)^2+(q_2-q_3)^2+(q_3-q_4)^2-(q_1-q_4)^2=-2.
 \tag{17}
\]

Every weighted triangle and every Pluecker relation holds, because the
edge field is an exact gradient.  Thus Pluecker algebra alone cannot
determine the sign of a signed chord measure.  The literal
von-Mangoldt--Gamma--pole coefficients must enter a new inequality.

## 5. The continuous chord-swap null-IQC

For \(a,c\geq0\), define the unsquared chord amplitude

\[
 \mathcal Tq(c,a)
 =\sqrt{2K(c+a)K(c-a)}
   \{q(c+a)-q(c-a)\}.
 \tag{18}
\]

For even \(K,q\),

\[
 \boxed{\mathcal Tq(c,a)=\mathcal Tq(a,c).}
 \tag{19}
\]

Let \(U\) exchange \(a\) and \(c\).  Equation (19) says

\[
 (I-U)\mathcal Tq=0.
 \tag{20}
\]

Let \(d\bar\sigma(a)\) be the pushforward of the common-cutoff physical
signed displacement measure under \(u=2a\), and let \(d\lambda\) denote
Lebesgue measure on the positive half-line.  Whenever the common-cutoff
integrals are finite, variable exchange gives

\[
\boxed{
 \iint|\mathcal Tq(c,a)|^2,d\lambda(c)d\bar\sigma(a)
 =
 \iint|\mathcal Tq(c,a)|^2,d\bar\sigma(c)d\lambda(a).}
 \tag{21}
\]

Thus the antisymmetric part of
\(d\lambda\otimes d\bar\sigma\) is an exact global null-IQC.  But (21)
also gives

\[
\boxed{
 Q_{\rm phys}(q)
 ={1\over2}\iint|\mathcal Tq(c,a)|^2
 \{d\lambda(c)d\bar\sigma(a)
   +d\bar\sigma(c)d\lambda(a)\}.}
 \tag{22}
\]

Equation (22) is only the symmetric representative of the same signed
form.  It does not turn the signed measure into a positive measure.  The
swap multiplier is zero on the physical range by (20), exactly as in
Theorem 2.

## 6. An exact global reconstruction

Put

\[
 h(x)=\cosh(x/2),
 \qquad
 c_K=\int_{\mathbb R}h(u)K(u)\,du=\frac12,
 \tag{23}
\]

and define the oriented chord observation

\[
 (Cq)(u,x)=\sqrt{K(x)K(x-u)}\{q(x)-q(x-u)\},
 \qquad u,x\in\mathbb R.
 \tag{24}
\]

For a chord field \(z\), define formally

\[
 (Rz)(x)=\frac1{c_Kh(x)}
 \int_{\mathbb R}
 \frac{h(x-u)K(u)}{\sqrt{K(x)K(x-u)}}z(u,x)\,du.
 \tag{25}
\]

### Theorem 3 — Mean-periodic reconstruction identity

On every core on which the integrals are justified,

\[
 \boxed{
 RCq=q-\frac{(hq)*K}{c_Kh}.}
 \tag{26}
\]

In particular,

\[
 (hq)*K=0\quad\Longrightarrow\quad RCq=q.
 \tag{27}
\]

#### Proof

Evenness of \(K\) gives

\[
 \int h(x-u)K(u)\,du=c_Kh(x).
 \tag{28}
\]

Indeed, expand \(h(x-u)\) into its hyperbolic addition formula; the odd
\(\sinh(u/2)K(u)\) integral vanishes and the even integral is \(c_K\).
Substitution of (24) into (25) therefore gives

\[
 \begin{aligned}
 RCq(x)
 &=q(x)-{1\over c_Kh(x)}
   \int h(x-u)K(u)q(x-u)\,du\\
 &=q(x)-{((hq)*K)(x)\over c_Kh(x)}.
 \end{aligned}
 \tag{29}
\]

This proves (26)--(27). \(\square\)

The identity uses all chord centers at once and is not covered by the
finite incidence theorem.  It therefore passes the algebraic nonlocality
gate.  Its norm is the next issue.

## 7. The direct Gamma Schur realization is unbounded

Use the oriented Gamma input norm

\[
 \|z\|_\Gamma^2
 ={1\over2}\iint_{mathbb R^2}
 r_\Gamma(|u|)|z(u,x)|^2\,du\,dx,
 \qquad
 r_\Gamma(t)={e^{-5t/2}\over1-e^{-2t}},
 \tag{30}
\]

and the output norm in

\[
 d\mu_K(x)={h(x)K(x)\over c_K}\,dx.
 \tag{31}
\]

The prime channels, when adjoined, are orthogonal positive channels.  A
field supported only in the Gamma component therefore gives the same lower
bound for the norm of any direct full-source extension.

### Theorem 4 — Exact fiber norm and tail blowup

As a decomposable operator from the Gamma chord space to
\(L^2(\mu_K)\), the operator (25) has

\[
 \boxed{
 \|R\|^2
 =\operatorname*{ess\,sup}_{x\in\mathbb R}\mathcal S_\Gamma(x),}
 \tag{32}
\]

where

\[
 \boxed{
 \mathcal S_\Gamma(x)
 ={2\over c_K^3h(x)}
 \int_{\mathbb R}
 {K(u)^2h(x-u)^2
  \over K(x-u)r_\Gamma(|u|)}\,du.}
 \tag{33}
\]

Moreover,

\[
 \boxed{\mathcal S_\Gamma(x)\longrightarrow\infty
 \quad(x\to+\infty),}
 \tag{34}
\]

at least double exponentially.  Hence \(R\) is unbounded.

#### Proof

For fixed \(x\), (25) is a linear functional on
\(L^2(\frac12r_\Gamma(|u|)du)\).  Its squared functional norm, multiplied
by the output density \(h(x)K(x)/c_K\), is exactly (33).  Direct-integral
operator theory, or localization of \(z\) in an arbitrarily small spatial
set and alignment with the row kernel, gives (32).

Choose \(u\in[1,2]\).  The continuous function

\[
 {K(u)^2\over r_\Gamma(u)}
 \tag{35}
\]

has a strictly positive minimum there.  The theta bound of 106.67 gives
constants \(A,a>0\) such that

\[
 K(y)\le A\exp\{-ae^{2y}\}
 \qquad(y\ge1).
 \tag{36}
\]

For \(x\ge3\), (33), restricted to \(1\le u\le2\), therefore gives

\[
 \mathcal S_\Gamma(x)
 \ge C h(x)^{-1}
       \exp\{ae^{2(x-2)}\}
 \ge C e^{-x/2}\exp\{ae^{2(x-2)}\}.
 \tag{37}
\]

This proves (34) and unboundedness. \(\square\)

As a floating-point normalization check, direct theta quadrature gives

\[
 \mathcal S_\Gamma(0)\approx4.3897457.
 \tag{38}
\]

This numerical value is not used in the theorem.  The exact conclusion
\(\|R\|=\infty\) is stronger than failure of the desired squared norm
bound \(2\).

## 8. Every alternative left inverse has the same intrinsic gate

Let

\[
 \mathscr N_0={q:(hq)*K=0,\ \mu_K(q)=0\}
 \tag{39}
\]

inside the common form domain, and let \(C_+\) be the complete positive
ordinary-prime--Gamma observation, normalized by

\[
 \|C_+q\|^2=\mathscr E_K(q).
 \tag{40}
\]

The Gamma continuum makes \(C_+\) injective on the centered space.  Hence
there is one algebraic inverse on its physical range,

\[
 R_0(C_+q)=q,
 \qquad q\in\mathscr N_0.
 \tag{41}
\]

### Theorem 5 — Reconstruction norm is the physical surplus

One has

\[
 \boxed{
 \|R_0\|^2
 =\sup_{0\ne q\in\mathscr N_0}
 {\|q\|_{\mu_K}^2\over\mathscr E_K(q)}.}
 \tag{42}
\]

Consequently,

\[
 \boxed{
 \|R_0\|\le\sqrt2
 \quad\Longleftrightarrow\quad
 \mathscr E_K(q)\ge{1\over2}\|q\|_{\mu_K}^2
 \quad(q\in\mathscr N_0).}
 \tag{43}
\]

Any other operator \(\widetilde R\) satisfying

\[
 \widetilde R C_+q=q\qquad(q\in\mathscr N_0)
 \tag{44}
\]

agrees with \(R_0\) on \(C_+\mathscr N_0\), and therefore

\[
 \|\widetilde R\|\ge\|R_0\|.
 \tag{45}
\]

#### Proof

Formula (42) is the definition of the operator norm of the inverse (41).
Rearranging its bound by \(2\) gives (43).  Equation (44) fixes the value
of every alternative inverse on the range, proving (45). \(\square\)

The known critical-line modes saturate (43), so no valid construction may
replace \(\sqrt2\) by a smaller constant.  After the exact radical
anti-short, the common saturated radical block is removed from both sides;
the remaining norm condition is precisely the complementary contraction
of 106.39(20).  A different convolution kernel can alter an ambient
extension of \(R_0\), but it cannot alter (42).

## 9. Consequence for the active construction

The chord determinant has now been audited at all three relevant levels.

* **Algebraic:** its Pluecker relations are consequences of weighted
  triangle incidence.
* **IQC:** every Hermitian Pluecker null is a Hodge constraint null, and
  the continuous swap is an exact but sign-neutral null-IQC.
* **Analytic:** the global mean-periodic reconstruction is exact, but its
  direct Gamma extension is unbounded; the best possible range norm is the
  physical surplus itself.

This does not exclude every globally signed source-specific multiplier.
It excludes the claim that determinant integrability or reconstruction
alone supplies its norm.  A surviving proof must estimate the canonical
inverse on the mean-periodic, radically anti-shorted range by using the
literal joint distribution of \(\Lambda(p^k)\), Gamma, and the pole.  In
equivalent source language, it must construct the complementary contraction
of 106.39 rather than another null reparametrization of its domain.

## 10. Reproduction

The floating-point normalization check (38) is reproduced by

```bash
cd 03-research/phase-106-global-modular-star-audit
python3 tools/chord_reconstruction_schur_probe.py
```

It uses only `numpy`.  It is not part of the proof of Theorem 4.
