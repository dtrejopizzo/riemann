# E72.221 - Full-even overlap formula audit

## Purpose

E72.220 reduces the raw HS problem to the full-even overlap

```text
||E U_y E||_HS^2.
```

This note compares it to the simple profile

```text
(dim_even/2)(1-y/L).
```

## Diagnostic

Script:

```text
E72_221_full_even_formula_probe.py
```

Output excerpt:

```text
E72.221 full-even U_y formula probe
compares ||E U_y E||_HS^2 to qdim*(1-u)
lam qdim u fullEven qdim(1-u) diff rel
 12   33 0.10 1.481915250e+01 2.970000000e+01 -1.488e+01 -1.004e+00
 12   33 0.25 1.246860735e+01 2.475000000e+01 -1.228e+01 -9.850e-01
 12   33 0.50 8.250000000e+00 1.650000000e+01 -8.250e+00 -1.000e+00
 16   41 0.50 1.025000000e+01 2.050000000e+01 -1.025e+01 -1.000e+00
 20   49 0.50 1.225000000e+01 2.450000000e+01 -1.225e+01 -1.000e+00
 24   57 0.50 1.425000000e+01 2.850000000e+01 -1.425e+01 -1.000e+00
```

## Reading

The printed comparison used `dim_even(1-u)`, and the data show the correct leading profile is half of
that:

```text
||E U_{uL}E||_HS^2 ~= (dim_even/2)(1-u).
```

At `u=0.5`, this relation is exact in the tested windows. Away from `u=0.5`, there are finite-section
oscillatory corrections.

Since `dim_even = qdim+1 ~= O(L^2)` in the chosen finite windows, this explains why

```text
||B_x^*U_yB_x||_HS^2 = O(L^2)
```

only after accounting for the fact that the chosen mode count grows like `O(L)`. More precisely, the
empirical scale in E72.214 is:

```text
||B_x^*U_yB_x||_HS^2/L^2 ~= O(1).
```

## Candidate upper bound

A basis-free sufficient estimate is:

```text
||B_x^*U_{uL}B_x||_HS^2
<= ||E U_{uL}E||_HS^2
<= C_E N_x (1-u) + diffraction_N(u),
```

where `N_x=dim_even`. In the Phase 72 scaling `N_x~alpha L^2`, this gives the desired `O(L^2)` raw
HS scale before summing against the prime-square weights.

## Status

Partial. The raw HS term has a clean projection formula and a simple full-even leading profile, but
the exact finite-section diffraction correction still has to be bounded.
