# Real-ray positivity versus a Stieltjes representation

## Purpose

This note tests whether the exact Li generator can be promoted from
positivity on the real interval to a positive moment representation.  Such
a promotion would be far stronger than RH and is incompatible even with the
critical-line singularity geometry.

## 1. What is true on the real ray

Let
\[
 \mathcal L(z)={d\over dz}\log\xi\!\left({1\over1-z}\right)
 =\sum_{n\ge1}\lambda_nz^{n-1}.
\]
For \(0<z<1\), put \(s=(1-z)^{-1}>1\).  The theta representation of
`103_15` gives \(\xi'(s)>0\), while \(ds/dz>0\).  Hence
\[
 \mathcal L(z)={\xi'(s)\over\xi(s)}{1\over(1-z)^2}>0
 \qquad(0<z<1).                                                       \tag{1}
\]
This is an unconditional one-dimensional positivity statement.

It is not coefficient positivity.  For example, the polynomial
\(1-z/2\) is strictly positive on \((0,1)\) but has a negative Taylor
coefficient.  A real-ray inequality cannot by itself control the signs of
the \(\lambda_n\).

## 2. The Hausdorff/Stieltjes target is overstrong

Suppose one had a finite positive measure \(\nu\) on \([0,1]\) such that
\[
 \mathcal L(z)=\int_0^1{d\nu(t)\over1-zt}.                          \tag{2}
\]
Then
\[
 \lambda_{n+1}=\int_0^1t^n\,d\nu(t)\ge0,                           \tag{3}
\]
and the necessary Hausdorff moment inequalities would hold:
\[
 (-1)^j\Delta^j\lambda_{n+1}\ge0\quad(n,j\ge0),                    \tag{4}
\]
as would every Hankel inequality
\[
 \sum_{j,k}c_j\overline{c_k}\lambda_{j+k+1}
 =\int_0^1\left|\sum_jc_jt^j\right|^2d\nu(t)\ge0.                 \tag{5}
\]
Thus (2) would imply Li positivity and RH.

But (2) is incompatible with the expected critical-line divisor, not just
with off-line zeros.  Its right side is analytic on
\(\mathbb C\setminus[1,\infty)\).  On the other hand, a nontrivial zero
\(\rho\) produces a pole of \(\mathcal L\) at
\[
 w_\rho=1-{1\over\rho}.                                             \tag{6}
\]
Under RH these points lie on the unit circle and are generically non-real,
so they are still outside \([1,\infty)\).  Therefore (2) cannot be a
representation of the Li generator even assuming RH.

More generally, an interior pole \(|w_\rho|<1\) from an off-line zero is
immediately excluded by (2), so any proof of a positive fixed-measure
representation would contain RH; its excessively narrow cut also excludes
the legitimate boundary poles on the critical circle.

## 3. Why the theta measure does not produce a fixed \(\nu\)

The theta formula instead gives
\[
 {\xi'(s)\over\xi(s)}=\mathbb E_s[U],
\]
where the probability law is the exponentially tilted measure
\[
 d\mu_s(u)={e^{(s-1/2)u}d\mu_0(u)\over\xi(s)}.
\]
Substitution \(s=(1-z)^{-1}\) makes this measure depend on \(z\).  It
does prove (1), but it cannot be rearranged into (2) without replacing a
moving exponential tilt by a fixed positive resolvent measure.  The
singularity audit above proves that no such replacement can be exact.

## Status

The Hausdorff/Stieltjes route is eliminated as an exact representation of
\(\mathcal L\).  Positivity of \(\mathcal L\) on \((0,1)\) remains true
but has no coefficient-sign consequence without a new complex-domain
positivity theorem, which would itself have to confront the zero divisor.
