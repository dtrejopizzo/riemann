# VK cutoff-ratio terminal scale

## Purpose

`207_A0_TERMINAL_CUTOFF_BRIDGE_AUDIT.md` reduces the terminal absolute
Laguerre load to the cutoff-ratio condition
\[
  \mathcal T_n(\varepsilon)
  \le
  {n^2\over12(n-1)^2}B_{n-1}
  \log {1+T_n\over1+T_{n-1}}.
\tag{1}
\]

This note evaluates the ratio term for the standard
Vinogradov--Korobov profile from `152`,
\[
  \eta(u)=a{u^{3/5}\over(\log u)^{1/5}}.
\tag{2}
\]

The outcome is positive but limited: for canonical minimal A0 cutoffs,
\[
  \log {1+T_n\over1+T_{n-1}}=O(1/n),
\]
so the terminal load in (1) is only \(O(\log n)\).  This removes the
possibility of a large terminal explosion from the cutoff ratio.  It does
not close A1, because one still needs a lower comparison against
\(\mathcal B_n\) and control of all earlier mixed intervals of
\(\mathcal H_n\).

## Canonical cutoff model

For the VK profile, the A0 condition for index \(n\) is
\[
  a{u^{3/5}\over(\log u)^{1/5}}
  \ge
  (n+1)\log(1+u)+\log {12A n^2\over B_n}.
\tag{3}
\]

Let \(T_n\) be the minimal cutoff beyond the monotonicity threshold at
which (3) holds.  Since the internal lower bound from `151` satisfies
\[
  B_n={1\over2}n\log n+O(n)
\tag{4}
\]
when the large-range expression is used, the final logarithmic term in
(3) is only \(O(\log n)\).  The dominant equation is therefore
\[
  a{T_n^{3/5}\over(\log T_n)^{1/5}}
  =
  n\log T_n+O(n+\log n).
\tag{5}
\]

More generally, for
\[
  \eta(u)=a{u^\alpha\over(\log u)^\beta},
  \qquad 0<\alpha<1,\quad \beta\ge0,
\tag{6}
\]
the cutoff equation
\[
  a{T_n^\alpha\over(\log T_n)^\beta}
  =
  n\log T_n+O(n+\log n)
\tag{7}
\]
has the scale
\[
\boxed{
  T_n
  =
  a^{-1/\alpha}\alpha^{-(\beta+1)/\alpha}
  n^{1/\alpha}(\log n)^{(\beta+1)/\alpha}
  \,(1+o(1)).
}
\tag{8}
\]

For (2), \(\alpha=3/5\) and \(\beta=1/5\), hence
\[
\boxed{
  T_n
  =
  {25\over9a^{5/3}}\,n^{5/3}(\log n)^2(1+o(1)).
}
\tag{9}
\]

Consequently
\[
\boxed{
  \log {1+T_n\over1+T_{n-1}}
  =
  {5\over3n}+{2\over n\log n}+o(1/n).
}
\tag{10}
\]

The same estimate holds if the chosen cutoffs are comparable to the
minimal cutoffs with a slowly varying multiplicative factor.  It is not
automatic for arbitrary oversized cutoffs; if \(T_n\) is chosen with large
uncontrolled jumps, (10) can fail.

## Terminal consequence

Substituting (10) into (1) gives, for canonical VK cutoffs,
\[
  \mathcal T_n(\varepsilon)
  \le
  {n^2\over12(n-1)^2}B_{n-1}
  \left(
    {5\over3n}+{2\over n\log n}+o(1/n)
  \right).
\tag{11}
\]

Using \(B_{n-1}={1\over2}n\log n+O(n)\), this becomes
\[
\boxed{
  \mathcal T_n(\varepsilon)
  \le
  {5\over72}\log n+O(1)
}
\tag{12}
\]
for the large-range internal \(B_n\) normalization.

Thus, under the canonical VK cutoff choice, the terminal absolute load is
logarithmic.  The terminal interval is not the source of an
\(n\log n\)-scale obstruction.

## Why this still does not close Theorem B

The absolute route from `196` requires
\[
  \mathcal B_n
  \ge
  \int_0^{T_n}\varepsilon(u)|\mathcal H_n(u)|\,du.
\tag{13}
\]
The terminal part of the right side is only one piece.  Even if (12) is
dominated by \(\mathcal B_n\), the proof still needs:

1. an explicit lower bound for \(\mathcal B_n\) strong enough to absorb
   \(O(\log n)\) and finite initial cases;
2. weighted \(L^1\) bounds for the earlier mixed intervals of
   \(\mathcal H_n\), where the kernel is a cumulative Laguerre mixture;
3. a fixed canonical cutoff policy, or a ratio theorem, preventing
   uncontrolled oversized jumps in \(T_n\).

Without these three items, (12) is only a terminal-scale estimate.

## Exact remaining terminal theorem

The terminal portion of the absolute route is reduced to the following
finite/asymptotic verification:
\[
\boxed{
  \mathcal B_n
  \ge
  {5\over72}\log n+O(1)
  \qquad(n\ge9),
}
\tag{14}
\]
with the \(O(1)\) made explicit and the finite range checked, or to a
sharper direct comparison using (11).

If (14) is proved, the terminal interval from `201` is controlled for
canonical VK cutoffs.  A1 would still require the mixed-interval domination
in (13), or a signed theorem avoiding the absolute \(L^1\) loss.

## Status

Closed as a VK cutoff-ratio scale audit.

The A0 cutoff ratio is not a fatal obstruction for the terminal interval
when canonical VK cutoffs are used.  A1 remains open because the absolute
route still needs a \(\mathcal B_n\) lower bound, finite initial checks,
and domination of the earlier cumulative Laguerre mixture loads.
