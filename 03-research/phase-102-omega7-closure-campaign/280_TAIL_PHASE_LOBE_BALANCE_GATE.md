# Tail-phase lobe balance gate

## Purpose

`254_TAIL_SIGN_EXPLICIT_FORMULA_PHASE_GATE.md` rewrites the one-sided tail
condition as a phase inequality over zeros.  `258` shows that critical-line
support alone does not imply that inequality.

This note records the exact signed-lobe balance that remains.  It is the
tail analogue of the Fejer distribution gates: once the kernel is signed,
compact A1 requires dominance of the negative phase lobes over the positive
phase lobes by an explicit margin.

## Critical-line phase kernel

Assume the zero-side expression has been restricted to the critical line,
as in `258`.  Put
\[
  W_{n,T}(\gamma)
  =
  {\Phi_{n,T}(1/2+i\gamma)\over 1/2+i\gamma},
\]
and define the real phase kernel
\[
\boxed{
  q_{n,T}(\gamma)=\Re W_{n,T}(\gamma).
}
\tag{1}
\]

Let \(\mu_\zeta\) be the positive counting measure of ordinates
\(\gamma>0\), whenever such a critical-line representation is available.
Then `254` gives
\[
\boxed{
  I_n(T)
  =
  -2\int_{\gamma>0}q_{n,T}(\gamma)\,d\mu_\zeta(\gamma)
  -\mathcal T_{n,T}.
}
\tag{2}
\]

Here \(\mathcal T_{n,T}\) is the real archimedean/trivial-zero tail from
`254`.

## Positive and negative phase lobes

Write
\[
  q_{n,T}=q_{n,T}^+-q_{n,T}^-,
  \qquad
  q_{n,T}^\pm\ge0,
  \qquad
  q_{n,T}^+q_{n,T}^-=0,
\]
and define
\[
  P_{n,T}^+
  =
  \int_{\gamma>0}q_{n,T}^+(\gamma)\,d\mu_\zeta(\gamma),
  \qquad
  P_{n,T}^-
  =
  \int_{\gamma>0}q_{n,T}^-(\gamma)\,d\mu_\zeta(\gamma).
\tag{3}
\]

Then (2) becomes
\[
\boxed{
  I_n(T)=2(P_{n,T}^- - P_{n,T}^+)-\mathcal T_{n,T}.
}
\tag{4}
\]

Therefore the nonpositive-tail gate
\[
  I_n(T_n)\ge0
\]
is exactly
\[
\boxed{
  P_{n,T_n}^- - P_{n,T_n}^+
  \ge {1\over2}\mathcal T_{n,T_n}.
}
\tag{5}
\]

The deficit-compensating A1 tail gate from `254`,
\[
  I_n(T_n)\ge \left(d_n-{1\over4}\right)A_n,
\]
is exactly
\[
\boxed{
  P_{n,T_n}^- - P_{n,T_n}^+
  \ge
  {1\over2}
  \left(
    \mathcal T_{n,T_n}
    +
    \left(d_n-{1\over4}\right)A_n
  \right).
}
\tag{6}
\]

This is the signed phase-balance form of compact A1.

## Why support and modulus do not close the balance

Critical-line support identifies the measure space for (3), but it does not
compare \(P^-\) with \(P^+\).  A total mass bound, zero-counting bound, or
absolute-value estimate controls
\[
  P_{n,T}^-+P_{n,T}^+
  =
  \int |q_{n,T}|\,d\mu_\zeta,
\]
whereas (5)--(6) require the oriented difference
\[
  P_{n,T}^- - P_{n,T}^+.
\]

These are different pieces of data.  In particular, an upper bound for
\(\int |q_{n,T}|\,d\mu_\zeta\) cannot imply a lower bound for
\(P^- - P^+\) unless an additional sign-distribution theorem is supplied.
This is the lobe-balance version of the no-go in `258`.

## Sufficient phase-lobe theorems

The tail route can close through any one of the following genuinely signed
inputs:

1. pointwise nonpositivity plus enough negative mass,
   \[
     q_{n,T_n}(\gamma)\le0
     \quad\hbox{and}\quad
     P_{n,T_n}^-\ge {1\over2}\mathcal T_{n,T_n};
   \]
2. a direct lobe dominance theorem (5);
3. the deficit-compensating dominance theorem (6);
4. an equivalent margin-tail theorem \(s_n\ge d_n\) from `240` and `255`.

Each alternative is a signed theorem about the actual arithmetic zero
measure.  None follows from support on the critical line by itself.

## Relation to compact A1

For \(T=T_n\), (4) inserted into the compact coefficient identity gives
the same A1 gate as `244` and `255`.  Thus the exact remaining tail theorem
is
\[
\boxed{
  P_{n,T_n}^- - P_{n,T_n}^+
  \ge
  {1\over2}
  \left(
    \mathcal T_{n,T_n}
    +
    \left(d_n-{1\over4}\right)A_n
  \right)
  \qquad(n\ge8),
}
\tag{7}
\]
or a stronger theorem implying it.

This is not a new proof of A1.  It is the minimal signed lobe-balance
statement that any zero-side tail proof must establish.

## Status

Closed as the signed lobe-balance normal form for the tail-phase route.
A1 remains open until the arithmetic zero measure is shown to satisfy
(7), or until another surviving route proves the equivalent pointwise
compact inequality.
