# D.85 — Full-space certificate at the `log 2` endpoint

## Scope

This note closes the full Hilbert-space inequality at the endpoint
`T=log 2` for the two-contact mesh of D.79.  It is an endpoint theorem, not a
claim that row (d) is globally closed.  No finite Galerkin positivity is used
as a substitute for a full-space estimate.

Let `P` be the cellwise Legendre projection of degree nine and `Q=1-P`.
The moderate base uses the first 160 gamma resolvents and the positive tail
anchor

`B=320.5`, `c=B/4=80.125`.

The fixed vectors `v_1,v_2` in the even sector and `v_o` in the odd sector
are stored exactly as binary64 input data in the verifiers.  Floating point
is used only to select these vectors and precondition congruences; all stated
inequalities are recomputed with Arb balls.

## Directed ingredients

1. **Projected spectral separation.**  Arb congruence proves

   `P A_0 P + |v_1><v_1| + |v_2><v_2| >= 0.5 P`

   in the even sector, and

   `P A_0 P + |v_o><v_o| >= 0.05 P`

   in the odd sector.

2. **Full-space high block.**  Closed exponential Grams, rather than a
   uniform Taylor remainder, give

   `Q A_0 Q >= alpha Q`, `alpha > 1.5396358725`,

   `||Q A_0 P||^2 < 0.000365731342`.

   Consequently the even high block has gap greater than `0.4659`; the odd
   complement has gap greater than `0.0497`.

3. **Directed low-mode data.**  The analytic ODE assembly gives

   `-<v_1,A_0v_1> < 1.746475e-6`,

   `||(A_0-<v_1,A_0v_1>)v_1||^2 < 4.441e-24`,

   `<v_2,A_0v_2> > 0.0020336972824697`, with residual square below
   `8.623e-20`, and

   `<v_o,A_0v_o> > 8.13856175479e-6`, with residual square below
   `9.741e-22`.

   The two-level Feshbach estimate therefore gives a complement gap
   `g=0.0015` for `v_1`.

4. **Positive tail capacity.**  Put `eta=0.0003` and `h=g-eta=0.0012`.
   The Fourier transform of `v_1` is evaluated from its exact cellwise
   Legendre series.  On `[0,20]`, 2000 directed interval cells and the convex
   trapezoid tail remainder prove

   `delta_h > 1.27084620358308`.

   The adverse capacity threshold is below `1.2111`.  Hence the shorted
   capacity of the positive gamma-tail remainder exceeds the effective
   negative Rayleigh value.  The capacity--Feshbach lemma proves positivity
   in the even low channel.  The odd low channel is already strictly
   positive by its Rayleigh value and residual bound.

## Conclusion

Both parity restrictions are nonnegative on the full Hilbert space at
`T=log 2`; the even equality direction is controlled by the positive tail
capacity, not by a finite cutoff.  Together with the nesting lemma this
closes the corresponding endpoint cell.  The global row-(d) flag remains
false until the remaining support cells are certified.

## Reproduction

The directed scripts require `python-flint`.  In the current audit
environment it is exposed by

```text
PYTHONPATH=/tmp/d61-flint python3 <verifier.py>
```

The pure Decimal budget checker needs only the standard Python library.
