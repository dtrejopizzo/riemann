# 107.210 -- The local derived intersections have a global nuclear pushforward on the Euler half-plane

## 1. Global conormal representation

For each prime, let

\[
 L_p=\mathfrak m_p/\mathfrak m_p^2
 \]

be the conormal line of `107_209`.  On

\[
 \mathcal H_{\partial}=\widehat\bigoplus_p L_p
 \tag{1.1}
\]

define the diagonal scale operator

\[
 Q_s|_{L_p}=p^{-s}.
 \tag{1.2}
\]

Its trace norm is

\[
 \|Q_s\|_1=\sum_p p^{-\Re s}.
 \tag{1.3}
\]

This converges exactly for \(\Re s>1\).  Thus the sum of local
conormal representations has a canonical nuclear pushforward to a
point precisely on the Euler half-plane.

## 2. Product of derived self-intersections

For \(\Re s>1\), Fredholm multiplicativity gives

\[
 \begin{aligned}
 \det_{\mathrm F}(1-Q_s)
 &=\prod_p\det(1-Q_s|L_p)\\
 &=\prod_p(1-p^{-s})\\
 &=\zeta(s)^{-1}.
 \end{aligned}
 \tag{2.1}
\]

By `107_209`, every factor is the character of
\(\lambda_{-1}(L_p)=i_p^*i_{p,*}1\).  Hence (2.1) is not merely an
Euler-product identity: it is the nuclear determinant pushforward of
the family of actual local derived self-intersection classes.

Its logarithmic derivative is

\[
 {d\over ds}\log\det_{\mathrm F}(1-Q_s)
 =\sum_p\log p\,{p^{-s}\over1-p^{-s}}
 =-\frac{\zeta'(s)}{\zeta(s)}.
 \tag{2.2}
\]

This is the finite Green character transported in `107_206`.

### Theorem 2.1 (nuclear local-to-global assembly)

On \(\Re s>1\), the local equivariant intersections of `107_209`
possess a canonical trace-class direct-image representation whose
Fredholm determinant and trace character are respectively
\(\zeta^{-1}\) and \(-\zeta'/\zeta\).

## 3. Comparison with the balanced Dirac operator

`107_200` used balanced two-state blocks and a
Carleman--Fredholm determinant.  The present operator is the
one-state conormal quotient of those blocks.  On the common domain,

\[
 \det_{\mathrm F}(1-Q_s)=\det_2(1-D_s)=\zeta(s)^{-1}.
 \tag{3.1}
\]

The two constructions now have distinct roles: \(D_s\) retains the
balanced square-root geometry, while \(Q_s\) is the direct nuclear
pushforward of the derived fixed-point intersections.

## 4. Sharp limitation

At \(\Re s\le1\), (1.3) diverges.  Therefore this pushforward does not
continue as a trace-class Hilbert-space direct image to the critical
line.  Meyer's nuclear Frechet quotient (`107_204`) remains necessary
for continuation, and `107_203` already proves that continuation is not
an ordinary cofinal determinant limit.

Nor is (1.1) a proper pushforward from one arithmetic surface.  It is a
countable analytic direct sum of local classes.  A solution of rows
(a), (c), and (d) must still:

1. realize this nuclear direct image as the trace of a sheaf/complex on
   the arithmetic square;
2. incorporate the completed archimedean class in the same category;
3. construct a primitive intersection form and Hodge sign.

## 5. Falsifier

`107_210_global_nuclear_pushforward_of_local_intersections.py` computes
the operator from the first 9,592 actual primes, compares its determinant
and logarithmic trace independently with \(\zeta^{-1}\) and
\(-\zeta'/\zeta\), and confirms growth rather than convergence of the
trace norm at \(s=1\).  Omitted factors are controlled by explicit
integral majorants over all integers beyond the fixed cutoff; no
post-computation tolerance is used.
