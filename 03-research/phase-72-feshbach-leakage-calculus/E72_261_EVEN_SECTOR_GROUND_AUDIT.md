# E72.261 -- Even-sector ground audit

**Purpose.** Audit the construction of the model complement used in the RFBD/LM8 stress tests.

The old helper `setup_pair` diagonalizes the full model matrix, takes the global ground vector, and
then symmetrizes it:

```text
k := even_part(v_0(H_model)).
```

But in the tested windows the global model ground is odd. Hence `even_part(v_0)` has norm about
`1e-16`; normalizing it creates an essentially arbitrary even direction.

## Diagnostic

For `include_arith=False`, the first model eigenvectors alternate parity:

```text
lambda=6:   O, E, O, E, ...
lambda=8:   O, E, O, E, ...
lambda=12:  O, E, O, E, ...
lambda=16:  O, E, O, E, ...
```

The norm of the even part of the global ground is:

```text
lambda=6    2.21e-16
lambda=8    4.50e-16
lambda=12   3.66e-16
lambda=16   4.59e-16
```

Thus the old complement accidentally removes a numerical even line rather than a canonical physical
line.

## Pure even alternative

If one instead diagonalizes the model inside the even sector and subtracts the even ground energy, then
the compressed complement satisfies exactly:

```text
lambda_min(C_model_even) = lambda_1^even - lambda_0^even.
```

The audit output confirms this identity:

```text
lam  evenMinC     evenGap      relGapErr
  6  7.393588e-01 7.393588e-01 1.35e-15
  8  7.932627e-01 7.932627e-01 1.54e-15
 12  8.929373e-01 8.929373e-01 4.97e-16
 16  9.783221e-01 9.783221e-01 3.40e-16
 20  1.051033e+00 1.051033e+00 1.06e-15
```

But this pure even-ground complement has scale `O(1)`, not `L^2`. Therefore it is not the complement
used by the pole-relative route.

## Consequence

The previous `L^2` coercivity measurements were not measurements of the pure even spectral gap. They
came from subtracting the odd pole energy while working in the even sector, with one extra accidental
even line removed.

That means the correct pole-relative object must be rebuilt explicitly:

```text
energy base = global odd pole energy e_pole,
physical space = full even sector,
no numerical even line removed.
```

This repair is E72.262.

## Status

The audit finds a real setup bug in the old helper. Results depending only on algebraic majorants
survive as polynomial facts, but RFBD/LM8 stress values computed through `setup_pair` must be rechecked
in the corrected pole-relative even geometry.
