# Direct A1 termwise sign obstruction

## Purpose

The direct A1 certificate in `226` has the form
\[
  \mathcal A_n-P_n+\sum_{m\le e^{T_n}}\Lambda(m)\Omega_n(m)\ge0.
\]

This note checks the simplest possible closure: positivity of the individual
prime-power coefficients \(\Omega_n(m)\).  The check fails for a structural
Laguerre reason.  This does not disprove the direct A1 route; it proves that
the route must use signed global compensation between prime powers, the pole
term, and the archimedean budget.

## High-block coefficient

For \(n\ge9\), put
\[
  N=n-1,\qquad
  G_N(u)=e^{-u}L_N^{(1)}(u).
\]

For prime powers in the high block \(\log m\ge T_8\), `226` gives
\[
\boxed{
  \Omega_n(m)=G_N(T_n)-G_N(\log m).
}
\tag{1}
\]

Thus termwise positivity in the high block would require
\[
  G_N(\log m)\le G_N(T_n)
  \qquad(T_8\le\log m\le T_n)
\tag{2}
\]
for every prime power in the block.

## Laguerre oscillation

The derivative identity
\[
  {d\over du}\left(e^{-u}L_N^{(1)}(u)\right)
  =
  -e^{-u}L_N^{(2)}(u)
\tag{3}
\]
shows that the critical points of \(G_N\) are precisely the positive zeros
of \(L_N^{(2)}\).  Since \(L_N^{(2)}\) has \(N\) simple positive zeros,
\(G_N\) has \(N\) alternating extrema.

Moreover, \(L_N^{(1)}\) has \(N\) simple positive zeros.  Hence \(G_N\)
changes sign on the positive axis.  Since
\[
  G_N(0)=L_N^{(1)}(0)=N+1>0,
\]
and
\[
  G_N(u)\to0
  \qquad(u\to\infty),
\]
the graph of \(G_N\) contains positive and negative lobes before decaying to
zero.

Consequently, whenever the moving cutoff \(T_n\) lies beyond values of
\(G_N\) both above and below \(G_N(T_n)\), the continuous coefficient
profile
\[
  a\mapsto G_N(T_n)-G_N(a)
\]
takes both signs on \(0<a<T_n\).  The Laguerre oscillation shows that this
is the generic high-block geometry; checking a particular \(n\) requires
locating \(T_n\) relative to the relevant lobes.

Thus the high-block coefficient formula is not a positive kernel identity.
At best, a proof would have to show an arithmetic avoidance statement for
the discrete prime-power points \(\log m\), or else a signed compensation
statement for the prime powers that do land in negative coefficient lobes.

## Why prime-power positivity cannot repair this locally

The weights \(\Lambda(m)\) are nonnegative, but the coefficient profile
\(\Omega_n(e^a)\) is not sign-definite as a function of the continuous
variable \(a\).  Therefore the implication
\[
  \Lambda(m)\ge0
  \quad\Longrightarrow\quad
  \sum_{m\le e^{T_n}}\Lambda(m)\Omega_n(m)\ge0
\]
has no coefficientwise proof.  It would require extra arithmetic input
showing that the prime-power support avoids the negative lobes, or a
signed cancellation theorem showing that the weighted positive lobes,
together with the pole and archimedean terms, dominate the negative ones.

The pole and archimedean terms also cannot be ignored.  A positive
coefficient subblock may be needed to compensate a negative coefficient
subblock, and the fixed continuous terms determine the required net margin.

Thus the direct A1 certificate is not certified by termwise Laguerre
positivity.  Its valid target is the signed correlation theorem
\[
\boxed{
  \mathcal A_n-P_n+\sum_{m\le e^{T_n}}\Lambda(m)\Omega_n(m)\ge0
  \qquad(n\ge9).
}
\tag{4}
\]

## Direct route still alive

The obstruction above eliminates only the naive continuous-kernel proof
\[
  \Omega_n(e^a)\ge0\quad\hbox{throughout the high block}.
\]

It does not eliminate direct A1.  The surviving direct route is one of:

1. prove a signed prime-power correlation for the oscillatory coefficients
   \(\Omega_n(m)\);
2. group adjacent Laguerre lobes before estimating;
3. prove the equivalent tail--margin inequality \(s_n\ge d_n\);
4. prove a stronger global positivity theorem that implies the direct
   coefficient inequality.

## Status

Closed as the termwise-sign audit for direct A1.

A1 remains open.  The direct path is now explicitly restricted to a global
signed compensation theorem, not coefficientwise positivity.
