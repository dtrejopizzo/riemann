# C127.001 — there are no corner terms, and the reason is irrationality

Date: 2026-09-12.  Status: `PROVED`.  Full statement: Paper 45 §5, Thm. 5.4.

## The discrepancy nobody had computed

The carrier's zero-count filtration (P123.048) has strata `Z_J`.  A class of
modulus `1/n` has its modulus in the real coordinate (Paper 45 Thm. 4.2), so it
can fix a point of `Z_J` only if the tangential translation `log n` is undone by
a gauge label `γ = n ∈ Γ_J`, forcing `P(n) ⊆ J`; the transverse factors are
`p^{−v_p(n)/2}` and each normal direction carries the covolume `log p`.  A naive
count therefore assigns to the label `n` the weight

    n^{−1/2} · ∏_{p|n} log p.

For `n = p^k` this is `Λ(n)n^{−1/2}` — correct.  For every composite `n` it is
nonzero while the explicit formula has `Λ(n) = 0` — wrong, at every composite
label.  P123.046 §5 and P123.048 §5 both record that the value on the
multiple-zero complement was not given; this is what was hiding there.

## The vanishing

For `|J| ≥ 2`, `[Z_J/Γ_S] ≅ [Y_{J,p_0}/Z^{|J|−1}]` with `Y` a compact mapping
torus of mass `log p_0` and the residual generators translating by `log p`,
`p ∈ J∖{p_0}`.  Those ratios are **irrational**, since `m log p = n log p_0`
would give `p^m = p_0^n` (P123.047 §1).  So the residual action is a free
minimal irrational rotation, its invariant probability measure is unique, and
the canonical trace `τ_J(Σf_nV^n) = ∫f_0 dμ_J` (P123.048 (2.1)) annihilates
every nonzero label.

`p_0` is a choice, and P123.048 §1 says no preferred zero coordinate is part of
the source.  So a functional attached to the source must agree with `τ_J^{p_0}`
for every `p_0 ∈ J`.  Given `γ ≠ 1`, pick `p` with `v_p(γ) ≠ 0` and then
`p_0 ∈ J∖{p}` (possible because `|J| ≥ 2`): `γ` has a nonzero exponent outside
`p_0`, so it is annihilated.  **Every nontrivial label dies at every corner.**

For `|J| = 1` the action of `p^Z` is free and **proper** with compact quotient,
the residual group is trivial, nothing is annihilated, and the tangential factor
is the orbit length `log p`.  The dividing line between the two regimes is
exactly the irrationality of `log p / log q`.

## Consequence

`Λ(n) = 0` for composite `n` is, on the carrier, the multiplicative
independence of distinct primes.  Paper 44 Thm. 5.3 proves the same vanishing
algebraically, by primary decomposition in the divisor cube.  The two proofs
share no input.
