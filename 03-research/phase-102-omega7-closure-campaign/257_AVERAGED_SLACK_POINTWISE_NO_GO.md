# Averaged slack pointwise no-go

## Purpose

`255_TAIL_MARGIN_CORRELATION_SLACK_FORM.md` proves that compact A1 needs
the pointwise tail--margin slack
\[
  h_n\ge(-M_n)_+
  \qquad(n\ge8).
\]

This note records a formal no-go: averaged, density-one, cofinal, or purely
asymptotic slack information does not imply compact A1 unless it is
converted into the pointwise inequality at every index.

## Pointwise gate

Let
\[
  A_n=\lambda_n^{\rm arch}>0,\qquad
  M_n=\lambda_n-\frac12A_n,
\]
and suppose a signed tail theorem supplies
\[
\boxed{
  R_n(T_n)\le {1\over4}A_n-h_n.
}
\tag{1}
\]

Then
\[
  C_n(T_n)\ge M_n+h_n.
\tag{2}
\]

Therefore A1 follows exactly from the pointwise condition
\[
\boxed{
  h_n\ge(-M_n)_+
  \qquad(n\ge8).
}
\tag{3}
\]

Equivalently, in normalized variables, A1 is
\[
\boxed{
  s_n\ge d_n
  \qquad(n\ge8).
}
\tag{4}
\]

## Averaged slack is insufficient

Suppose instead one proves only that for some weights \(w_n>0\),
\[
\boxed{
  \sum_{n=8}^{N} w_n h_n
  \ge
  \sum_{n=8}^{N} w_n(-M_n)_+
}
\tag{5}
\]
for large \(N\), or in the limit as \(N\to\infty\).

This does not imply (3).  Indeed, choose two indices \(a,b\) and set
\[
  h_a=(-M_a)_+-\varepsilon,\qquad
  h_b=(-M_b)_+ + {w_a\over w_b}\varepsilon,
\]
with all other slacks equal to their deficits.  Then the weighted average
in (5) is unchanged, but the pointwise A1 gate fails at \(a\).

Thus average surplus can be moved from one index to another without
repairing the failed compact coefficient at the deficient index.

## Density-one or cofinal information is insufficient

If (3) is proved only on a cofinal subset
\[
  \mathcal N\subset\{8,9,\ldots\}
\]
or on a density-one set, then A1 remains unproved at the exceptional
indices.

The Li criterion and the compact A1 assembly are coefficientwise:
\[
  \lambda_n\ge0\quad\hbox{for every }n,
  \qquad
  C_n(T_n)\ge0\quad\hbox{for every }n\ge8.
\]

No density theorem excludes the possibility that a missed exceptional
index has
\[
  h_n<(-M_n)_+,
\]
and hence
\[
  C_n(T_n)<0
\]
under the lower bound (2).

Therefore any cofinal or density-one theorem must be accompanied by a
finite or exceptional-set certificate for the omitted indices.

## Pure asymptotic slack is insufficient

An asymptotic statement of the form
\[
  h_n-(-M_n)_+=o(A_n)
\]
or
\[
  h_n\ge(-M_n)_+-o(A_n)
\]
does not imply (3).  Since A1 is a sign condition, an error term of
unknown sign can dominate an arbitrarily small true margin.

An asymptotic theorem becomes usable only after it is made effective:
there must exist an explicit \(N_0\) such that
\[
  h_n\ge(-M_n)_+
  \qquad(n\ge N_0),
\]
and a finite interval certificate for
\[
  8\le n<N_0.
\]

This is the same finite-threshold logic already isolated for the terminal
absolute interval in `245`, now applied to the signed compact slack.

## Relation to zero-side or global routes

Global Li positivity gives at most
\[
  (-M_n)_+\le {1\over2}A_n.
\]
It does not provide a pointwise lower bound for \(h_n\).

Similarly, a global Herglotz/RH proof may close Omega7 externally through
Li, but it does not certify compact A1 unless it is supplemented by the
pointwise bridge (3), or unless A1 is bypassed as an internal obligation by
the global closure mode.

## Status

Closed as the averaged/cofinal/asymptotic slack no-go.

A1 remains open.  Any tail--margin proof must produce the pointwise
inequality \(h_n\ge(-M_n)_+\), equivalently \(s_n\ge d_n\), for every
\(n\ge8\), or provide an effective tail theorem plus a finite exceptional
certificate.
