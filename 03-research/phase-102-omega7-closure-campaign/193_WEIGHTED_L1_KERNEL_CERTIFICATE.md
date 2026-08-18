# Weighted L1 kernel certificate

## Purpose

`191_ABSOLUTE_DIAGONAL_BUDGET_SCALE_AUDIT.md` reduces the absolute diagonal
route to the weighted \(L^1\) condition
\[
  \mathcal B_n
  \ge
  W_n(R)
  :=
  \int_0^{T_n}R(u)e^{-u}|\mathcal H_n(u)|\,du.
\tag{1}
\]

This note makes \(W_n(R)\) into an exact finite certificate.  It also
isolates the missing uniform theorem: control the sign partitions and
weighted \(L^1\) mass of the cumulative Laguerre kernel
\(\mathcal H_n\).

## Piecewise polynomial structure

The cumulative kernel is
\[
  \mathcal H_n(u)=\sum_{k=8}^{n-1}w_{n,k}\mathcal K_k(u),
\tag{2}
\]
where each \(\mathcal K_k\) is piecewise a Laguerre polynomial
combination on the intervals cut out by
\[
  T_7,T_8,\ldots,T_n.
\]

Let
\[
  0=a_0<a_1<\cdots<a_M=T_n
\tag{3}
\]
be the ordered cutoff partition.  On each open interval
\((a_\ell,a_{\ell+1})\),
\[
  \mathcal H_n(u)=P_{\ell,n}(u),
\tag{4}
\]
where \(P_{\ell,n}\) is an explicit polynomial of degree at most \(n-1\).

The endpoint values do not matter for \(W_n(R)\).

## Zero refinement

Let
\[
  Z_{\ell,n}
  =
  \{x\in(a_\ell,a_{\ell+1}):P_{\ell,n}(x)=0\}.
\tag{5}
\]

Counting multiplicity is unnecessary for the integral; only the distinct
zeros matter.  Order them as
\[
  a_\ell=z_{\ell,0}<z_{\ell,1}<\cdots<z_{\ell,q_\ell}<z_{\ell,q_\ell+1}
  =a_{\ell+1}.
\tag{6}
\]

On every subinterval
\[
  I_{\ell,r}=(z_{\ell,r},z_{\ell,r+1}),
\]
the sign of \(P_{\ell,n}\) is constant.  Choose
\[
  \sigma_{\ell,r}
  =
  \mathrm{sgn}\,P_{\ell,n}(u)
  \qquad(u\in I_{\ell,r}).
\tag{7}
\]

Then the exact weighted load is
\[
\boxed{
  W_n(R)
  =
  \sum_{\ell=0}^{M-1}
  \sum_{r=0}^{q_\ell}
  \sigma_{\ell,r}
  \int_{z_{\ell,r}}^{z_{\ell,r+1}}
  R(u)e^{-u}P_{\ell,n}(u)\,du.
}
\tag{8}
\]

This is exact because \(\sigma_{\ell,r}P_{\ell,n}=|P_{\ell,n}|\) on each
subinterval.

## Relative PNT profile

For a relative envelope
\[
  R(u)=e^u\varepsilon(u),
\tag{9}
\]
(8) becomes
\[
\boxed{
  W_n(\varepsilon)
  =
  \sum_{\ell,r}
  \sigma_{\ell,r}
  \int_{z_{\ell,r}}^{z_{\ell,r+1}}
  \varepsilon(u)P_{\ell,n}(u)\,du.
}
\tag{10}
\]

Thus the absolute route is exactly
\[
\boxed{
  \mathcal B_n
  \ge
  \sum_{\ell,r}
  \sigma_{\ell,r}
  \int_{z_{\ell,r}}^{z_{\ell,r+1}}
  \varepsilon(u)P_{\ell,n}(u)\,du
  \qquad(n\ge9).
}
\tag{11}
\]

## Elementary cases

If \(\varepsilon(u)=C\), then
\[
  W_n=C
  \sum_{\ell,r}\sigma_{\ell,r}
  \int_{z_{\ell,r}}^{z_{\ell,r+1}}P_{\ell,n}(u)\,du.
\tag{12}
\]
Since \(P_{\ell,n}\) is a Laguerre polynomial combination, all antiderivatives
are explicit polynomials.

If
\[
  \varepsilon(u)=C(1+u)^{-A}
\tag{13}
\]
with integer \(A\ge1\), the integrals reduce to finite sums of
\[
  \int_a^b u^q(1+u)^{-A}\,du,
\tag{14}
\]
which are elementary for fixed \(q,A\), with logarithms only when the power
\((1+u)^{-1}\) occurs.

If
\[
  \varepsilon(u)=C\exp(-a u^\theta),
\tag{15}
\]
the exact certificate is still (10), but the interval integrals are no
longer polynomial endpoint expressions for general \(\theta\).  They can be
bounded by monotonicity of \(\varepsilon\) on each subinterval:
\[
  \varepsilon(z_{\ell,r+1})
  \int_{I_{\ell,r}}|P_{\ell,n}(u)|\,du
  \le
  \int_{I_{\ell,r}}\varepsilon(u)|P_{\ell,n}(u)|\,du
  \le
  \varepsilon(z_{\ell,r})
  \int_{I_{\ell,r}}|P_{\ell,n}(u)|\,du.
\tag{16}
\]

This reduces the Vinogradov--Korobov absolute route to the same sign
partition plus unweighted lobe masses, with explicit monotone weights.

## Uniform theorem needed

The absolute diagonal route is now equivalent to the following uniform
kernel-mass theorem for the chosen envelope:
\[
\boxed{
  \sup_{n\ge9}
  \left[
    W_n(R)-\mathcal B_n
  \right]
  \le0.
}
\tag{17}
\]

Using (8), this becomes a statement about:

1. the roots of finitely many explicit polynomials \(P_{\ell,n}\);
2. the signed antiderivatives of those polynomials on the sign subintervals;
3. the growth of the base-archimedean budget \(\mathcal B_n\);
4. the decay profile of the PNT envelope.

No theorem currently in the phase controls these four objects uniformly.

## Why cutoff positivity still does not follow

The sign partition certifies \(|\mathcal H_n|\), not \(\mathcal H_n\).
Therefore it deliberately removes all cancellation among adjacent lobes and
among the component kernels \(\mathcal K_k\).

Consequently, (17) is a strong sufficient route.  If it succeeds, it closes
A1 by an absolute estimate.  If it fails, it does not disprove A1; it only
shows that the signed arithmetic route is necessary.

In particular, the roots of \(P_{\ell,n}\) are roots of cumulative Laguerre
combinations, not the standard zeros of one Laguerre polynomial.  Standard
interlacing of neighboring Laguerre families does not by itself give the
uniform \(L^1\) domination (17).

## Status

Closed as a finite weighted-\(L^1\) certificate for the absolute diagonal
route.

A1 remains open.  The exact new target is the uniform bound (17), computed
through the sign-partition formula (8).
