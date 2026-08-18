# Candidate logarithmic Schur-angle theorem

## Status: CANDIDATE / OPEN

This note records the quantitative pattern found after the exact
constant/mean-zero decomposition. It is not labelled PROVED.

Let

\[
\mathfrak D_N=
\begin{pmatrix}d_N&b_N^*\\b_N&C_N\end{pmatrix}
\quad\text{on}\quad
E_N=\mathbb C u_N\oplus E_N^0,
\]

and, whenever the range condition is satisfied, define

\[
\rho_N=
\frac{b_N^*C_N^\dagger b_N}{d_N}
=\sup_{0\ne h\in E_N^0}
\frac{|b_N(h)|^2}{d_NC_N[h]}.
\]

The finite-dimensional data suggest the following theorem.

## Candidate theorem

For every \(N\ge3\),

\[
C_N\ge0,
\qquad
d_N>0,
\qquad
b_N\in\operatorname{Ran}C_N^{1/2},
\qquad
\boxed{\rho_N\le\frac1{20\log N}}.
\]

Since \(1/(20\log3)<1\), these estimates would imply

\[
d_N-b_N^*C_N^\dagger b_N
\ge d_N\left(1-\frac1{20\log N}\right)>0
\]

and therefore the unit Gamma--Tate estimate. At \(N=2\) the rational
leakage space is empty, so that threshold is separate and trivial for this
part of the argument.

## Numerical pattern

The six-bin seeded scan through \(N\le260\), the four-bin large-\(N\) scan
through \(N=2000\), and mesh refinements at selected thresholds give:

- \(\rho_N\log N<0.047\) in every recorded sample;
- the zero-mean generalized quotient grows roughly like
  \(\log N+\text{constant}\);
- the full minimum remains positive in every sampled finite-dimensional
  space;
- the dangerous profile is positive, symmetric, and close to the constant
  cell mode.

The initially guessed lower bound proportional to \(2\log N\) is not
supported at large \(N\): by \(N=400\) the measured zero-mean quotient is
already below \(2\log N\). The weaker logarithmic law remains consistent
with all data.

## What an analytic proof must establish

### 1. Weighted logarithmic uncertainty on the zero-mean output

The useful input identity is

\[
\widehat h(0)=0,
\qquad h\in E_N^0.
\]

It supplies linear suppression near zero but not hard spectral support. A
proof needs a weighted uncertainty inequality that remains valid after
multiplication by every positive arithmetic exponential polynomial:

\[
\sum_k\int g_\Gamma(\tau)|P_{N,k}(\tau)\widehat h(\tau)|^2
\frac{d\tau}{2\pi}
\ge
(\log N-c_0)
\sum_k\int |P_{N,k}(\tau)\widehat h(\tau)|^2
\frac{d\tau}{2\pi}
-\text{controlled Tate term}.
\]

The reciprocal-band theorem is relevant because it confines each connected
spatial component uniformly; an IMS or commutator localization for the
logarithmic multiplier must then control recombination errors between those
components.

### 2. Exact treatment of the Tate cross channel

For \(h\in E_N^0\),

\[
|M_\pm(h)|
\le
\|e^{\pm t/2}-1\|_{L^2(0,\delta_N)}\|h\|_2
=O(\delta_N^{3/2})\|h\|_2,
\]

and

\[
M_+(L_{N,k}h)=P_{N,k}(i/2)M_+(h),
\qquad
M_-(L_{N,k}h)=P_{N,k}(-i/2)M_-(h).
\]

This gives a prime-distribution-free route to bounding the Tate portion of
\(b_N\).

### 3. Full cross-functional estimate

It is not enough to apply Cauchy--Schwarz to the leakage term alone. One
must prove for every \(h\in E_N^0\)

\[
|b_N(h)|^2
\le \frac{d_N}{20\log N}\,C_N[h].
\]

This single estimate simultaneously gives the range condition and the
candidate angle bound. It must include the Gamma, Tate, and leakage cross
terms with their actual signs.

## Logical consequence if proved

Only after the three displayed analytic estimates have been proved may the
candidate theorem be promoted to PROVED and the abstract/status table be
changed to claim row (d). Numerical agreement, regardless of sample size,
does not itself justify that promotion.

