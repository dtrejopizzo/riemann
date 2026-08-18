# 106.165 — White-light relative GNS and the no-sign theorem

## 1. Purpose

Document 106.164 constructs the global rooted-Jacobian polarization and
the positive coherent kernel
\[
 K_\varepsilon(t,u)
 =\frac{\zeta(1+\varepsilon+i(u-t))}
        {\zeta(1+\varepsilon)},
 \qquad \varepsilon>0.
 \tag{1}
\]
Its critical limit is the white-light kernel
\(\mathbf1_{t=u}\).  A natural next attempt is to subtract that leading
kernel and use the first finite correction as the positive metric on
relative cohomology.  This note proves that such a sign does not follow:
the white-light limit is full rank on every finite set of distinct times,
so positivity places no restriction on its first correction.

## 2. Fixed-frequency expansion

Fix distinct real numbers \(t_1,\dots,t_m\).  Let
\[
 \mathbf K_\varepsilon
 =\bigl(K_\varepsilon(t_i,t_j)\bigr)_{i,j=1}^m.
 \tag{2}
\]

### Theorem 2.1 — The arithmetic finite part is an unconstrained tangent

As \(\varepsilon\downarrow0\),
\[
 \boxed{
 \mathbf K_\varepsilon
 =I_m+\varepsilon\mathbf A+O(\varepsilon^2),}
 \tag{3}
\]
where
\[
 A_{ii}=0,
 \qquad
 A_{ij}=\zeta(1+i(t_j-t_i))\quad(i\ne j).
 \tag{4}
\]
The matrices \(\mathbf K_\varepsilon\) are positive semidefinite, but
their positivity implies no sign condition on \(\mathbf A\).

#### Proof

The diagonal of (1) is identically one.  For \(i\ne j\), the numerator
is holomorphic at \(1+i(t_j-t_i)\), while
\[
 \zeta(1+\varepsilon)
 =\varepsilon^{-1}+\gamma+O(\varepsilon).
\]
Therefore
\[
 K_\varepsilon(t_i,t_j)
 =\varepsilon\zeta(1+i(t_j-t_i))+O(\varepsilon^2),
\]
uniformly on the fixed finite set, proving (3) and (4).  Hermitian
symmetry follows from
\(\overline{\zeta(1+i\tau)}=\zeta(1-i\tau)\).

For the last statement, let \(B=B^*\) be any fixed matrix.  Then
\(I_m+\varepsilon B\) is positive definite for all sufficiently small
positive \(\varepsilon\), independently of the inertia of \(B\).
Since the leading matrix in (3) is \(I_m\), the positivity of
\(\mathbf K_\varepsilon\) cannot constrain the inertia of its tangent
\(\mathbf A\). \(\square\)

This differs sharply from a family tending to the all-ones matrix.  In
that case the leading form vanishes on the codimension-one zero-sum
subspace and positivity constrains the derivative there.  White light
has no such nullspace.

## 3. The only positive blow-up is universal

One can avoid the orthogonal limit by scaling the time difference with
\(\varepsilon\).  Put
\[
 u-t=\varepsilon x.
\]
Then
\[
 \boxed{
 \lim_{\varepsilon\downarrow0}
 K_\varepsilon(t,t+\varepsilon x)
 =\frac1{1+ix}.}
 \tag{5}
\]

#### Proof

The Laurent expansion at the pole gives
\[
 \zeta(1+\varepsilon(1+ix))
 =\frac1{\varepsilon(1+ix)}+\gamma+O(\varepsilon),
\]
and division by
\(\zeta(1+\varepsilon)=\varepsilon^{-1}+\gamma+O(\varepsilon)\)
gives (5). \(\square\)

The right side of (5) is the characteristic function of the exponential
law on \([0,\infty)\), so it is positive definite.  It is determined only
by the pole of \(\zeta\).  All fixed arithmetic frequencies have been
compressed out.  Thus the only nontrivial positive tangent limit is the
universal Cauchy/exponential module already found in 106.154; it cannot
carry the resonant divisor.

## 4. Consequence for relative cohomology

There are two canonical critical limits of the positive root states:

1. at fixed scaling frequency, the limit is white light and the
   arithmetic finite part has no inherited sign;
2. at the blown-up frequency \(u-t=O(\varepsilon)\), the limit is a
   universal positive kernel determined only by the pole at \(s=1\).

Neither produces the CCM Rosati polarization.  In particular, defining a
``renormalized positive metric'' by subtracting \(I_m\) from (3) and
dividing by \(\varepsilon\) is invalid: subtraction of the full-rank
positive leading form does not preserve positivity.

The missing relative polarization must therefore use an additional
intersection theorem coupling the finite places to the archimedean and
polar pages.  It cannot be the tangent metric of the finite-place GNS
states alone.

## 5. Status

Proved:

* the exact fixed-frequency expansion of the polarized Euler kernel;
* the absence of an inherited sign on its arithmetic finite part;
* the universal positive blow-up limit;
* exclusion of relative-GNS differentiation as a proof of CCM Rosati
  positivity.

Still required:

* a source-defined intersection pairing for the pair
  \((\operatorname{Pic}_{\rm ar},\eta)\) which includes Gamma and the
  polar plane before renormalization;
* a Hodge-index statement for that pairing whose primitive part is the
  finite Rosati form of 106.163.
