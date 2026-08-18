# 114.a.120 — H7: calibrated interpolation on every positive effective ray

```
+------------------------------------------------------------------------+
| RAY         D=t(p_1^*A+p_2^*B), with deg A=a>0 and deg B=b>0.          |
| BLOCK       Odd powers 1,3,9,... and small integer nodes 1,...,m.       |
| PRIME       A fresh p=2 mod 3 avoids one generalized Vandermonde.       |
| SATURATE    Genuine bounded sections hit the whole F_p^m block.         |
| CALIBRATE   Keep k=floor[tab/(2 log(3) log(p))] coordinates.            |
| RESULT      h_cal(tD)=t^2 ab/(2 log 3)+O(t) on every positive ray.      |
| LIMIT       Degreewise invariant; restriction/cohomology and Green RR   |
|             remain open.                                                |
+------------------------------------------------------------------------+
```

## 1. Fixed ray and orientation

Let

\[
 A=\sum_\ell a_\ell L_\ell,\qquad
 B=\sum_q b_qL_q                                                     \tag{1.1}
\]

be nonzero effective standard curve classes and put

\[
 P=\prod_\ell\ell^{a_\ell},\quad Q=\prod_qq^{b_q},\quad
 a=\log P,\quad b=\log Q.                                             \tag{1.2}
\]

First impose the primitive normalization

\[
 \gcd\bigl(\{a_\ell\}_\ell\cup\{b_q\}_q\bigr)=1.                     \tag{1.3}
\]

Every nonzero integral effective prime-generated divisor has a unique form
`t(p_1^*A+p_2^*B)` with (1.3): `t` is the common content of all coefficients.
Thus this is a normalization of the divisor itself, not a chosen
parametrization of its ray.

We treat the case `a>=b`; if `b>a`, exchange the two rulings.  Equality is
oriented toward the first ruling.  Write

\[
 c={1\over2\log3},\qquad C_-={5\over4}\log3,
 \qquad C_+={3\over2}\log3.                                          \tag{1.4}
\]

Define `mu` to be the midpoint of the following interval:

\[
 \sqrt{{cab\over C_-}}<\mu<{a\over C_+}.                              \tag{1.5}
\]

The interval is nonempty.  Indeed, after squaring, the required inequality
is

\[
 {cab\over C_-}<{a^2\over C_+^2}
 \quad\Longleftrightarrow\quad 9b<10a,                               \tag{1.6}
\]

which follows from `b<=a`.  For large integers `t`, set

\[
 m_t=\lfloor\mu t\rfloor.                                             \tag{1.7}
\]

The strict margins in (1.4) absorb the floor errors below.

## 2. A fresh prime avoiding the interpolation determinant

Put `e_r=3^r` for `0<=r<m=m_t` and let

\[
 \Delta_m=\det\bigl(j^{e_r}\bigr)_{
             0\le r<m,\ 1\le j\le m}\in\mathbb Z.                    \tag{2.1}
\]

### Lemma 2.1

`Delta_m` is nonzero and

\[
 \log|\Delta_m|\le m\log(m!)+{3^m-1\over2}\log m
                 =\exp((\log3+o(1))m).                                \tag{2.2}
\]

### Proof

For strictly increasing nonnegative exponents, the generalized Vandermonde
determinant is the ordinary Vandermonde times a Schur polynomial.  At the
positive, distinct nodes `1,...,m`, both factors are positive, so (2.1) is
nonzero.  Expanding the determinant into `m!` terms and bounding every node
by `m` gives (2.2), since `sum_(r<m)3^r=(3^m-1)/2`.  QED.

### Lemma 2.2 (fresh controlled prime)

For all sufficiently large `m`, there is a prime `p_m` such that

\[
 p_m\equiv2\pmod3,\qquad
 e^{C_-m}<p_m<e^{C_+m},\qquad
 p_m\nmid PQ\Delta_m.                                                 \tag{2.3}
\]

### Proof

The prime number theorem in the fixed progression `2 mod 3` gives
`exp(C_+m+o(m))` primes below the upper endpoint, while the lower interval
contains only `exp(C_-m+o(m))` primes.  The number of distinct prime divisors
of `Delta_m` is at most `log|Delta_m|/log2`, which by (2.2) is
`exp((log3+o(1))m)`.  Since

\[
 \log3<C_-<C_+,                                                       \tag{2.4}
\]

the primes in the interval eventually outnumber all forbidden divisors.
The fixed integer `PQ` removes only finitely many more primes.  QED.

Fix the least prime satisfying (2.3).  Because `p_m=2 mod 3`, every
`e_r=3^r` is invertible modulo `p_m-1`.  Hence all the required transported
odd-power bio structures exist.

## 3. Exact bounded saturation in the prescribed divisor

Abbreviate `p=p_m`.  The matrix

\[
 V_m=(j^{e_r})_{r,j}\in M_m(\mathbb F_p)                               \tag{3.1}
\]

is invertible by (2.3).  For any `y=(y_r) in F_p^m`, solve

\[
 \sum_{j=1}^m a_jj^{e_r}
   =P^tQ^{te_r}y_r\pmod p,\qquad 0\le r<m,                             \tag{3.2}
\]

and choose centered lifts `|a_j|<p/2`.  Define two rational vectors

\[
 \alpha_y=(a_1/P^t,\ldots,a_m/P^t),\qquad
 \beta=(1/Q^t,2/Q^t,\ldots,m/Q^t).                                   \tag{3.3}
\]

The choice of orientation and (1.4), (2.3) give

\[
 \|\alpha_y\|_2\le {\sqrt m,p\over2P^t}
 =\exp((C_+\mu-a)t+o(t))\longrightarrow0,                             \tag{3.4}
\]

while

\[
 \|\beta\|_2\le {m^{3/2}\over Q^t}
 =\exp(-bt+O(\log t))\longrightarrow0.                               \tag{3.5}
\]

Thus, for all sufficiently large `t`, the cross-contraction

\[
 C_y=p_1^*\alpha_y\circ(p_2^*\beta)^t                                 \tag{3.6}
\]

is a genuine bounded scalar pro-section of

\[
 tD=p_1^*(tA)+p_2^*(tB).                                               \tag{3.7}
\]

There are no auxiliary divisor primes: the exact denominators in (3.3) are
`P^t` and `Q^t`.  The fresh prime `p` divides neither.

Under the `e_r`-th homogeneous-endobio evaluation,

\[
 \varepsilon_{p,e_r}(C_y)
 =P^{-t}Q^{-te_r}\sum_ja_jj^{e_r}=y_r\pmod p.                         \tag{3.8}
\]

### Theorem 3.1 (all-ray block saturation)

For every positive effective ray and every sufficiently large `t`, genuine
bounded sections of `tD` map surjectively onto `F_p^m`.

The proof is (3.2)--(3.8).  Notice why this improves `a117`: small integer
nodes cost only `O(log t)` in the smaller ruling, while the centered
coefficient lifts use the larger exponential denominator.  No restriction
on the ratio `a/b` remains.

## 4. Canonical calibration and the RR coefficient

Set

\[
 k_t=\left\lfloor{c,ab,t^2\over\log p}\right\rfloor.                \tag{4.1}
\]

The lower bound in (2.3) and the left inequality of (1.4) imply

\[
 k_t\le {cabt^2\over C_-m_t}\le m_t                                  \tag{4.2}
\]

for all sufficiently large `t`.  Retain the first `k_t` intrinsically
ordered powers `1,3,9,...`.  Coordinate projection is a unital ring quotient,
and Theorem 3.1 makes its bounded image exactly `F_p^(k_t)`.  Therefore

\[
 h_{\rm ray}(tD)=k_t\log p
 ={ab\over2\log3}t^2+O(\log p)
 ={ab\over2\log3}t^2+O(t).                                           \tag{4.3}
\]

Equivalently,

\[
 \boxed{
 h_{\rm ray}(tD)
 ={\deg(tA)\deg(tB)\over2\log3}+o(t^2)
 }                                                                     \tag{4.4}
\]

on **every** ray with `a,b>0`.  If one degree is zero, the forced mixed
quadratic coefficient is zero and no positive block is requested.

The midpoint rule for `mu`, the least-prime convention, the ordered external
standard representative and the ordered powers make the degreewise
construction canonical on the **presentation lattice**.  As in `a118`,
products are reevaluated in the fresh target of the output degree, and odd
powers make the image cardinality invariant under the remaining sign choice.
Descent through a possible anti-diagonal relation in `Pic(Y^reg)` is not
asserted; `a121` proves that such descent is equivalent to anti-diagonal
faithfulness.

## 5. Exact remaining scope

This closes the all-positive-ray numerical and multiplicative calibration
left open by `a117`--`a118`.  It does **not** construct transition maps between
different fresh targets, kernels/cokernels under restriction, a long exact
cohomology sequence, or the geometric excess/Green complex realizing the RR
form.  It also does not descend the presentation invariant through a possible
anti-diagonal Picard relation.  These are now the narrower gates
H7-FRESH-EXACT, H7-REG-EXCESS-RR and the single common descent gate of `a121`.
Row A and RH remain open.

## 6. Verification scope

`114_a_120_h7_all_ray_calibrated_interpolation_verify.py` checks exact
generalized Vandermonde saturation over finite fields, the nonempty constant
window, both norm margins, `k_t<=m_t`, the sharp floor error and the scope
markers.  Lemma 2.2 is the asymptotic counting proof above, not a finite
prime-search inference.
