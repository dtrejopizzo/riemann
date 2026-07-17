# P76.062 - Prolate residual localization

The rectangular residual `f_N=M_N k_lambda` becomes shell dominated.  The
fractions of residual energy in the outer rows are:

```text
N    outer 2+2 rows    outer 4+4 rows
6        0.385              0.741
10       0.788              0.843
15       0.982              0.992
```

At `N=15` the largest entry is the left shell row `-14` and carries `91.4%`
of the energy by itself.  Hence the exact source required by the prolate
bridge is asymptotically a shell source, the class controlled by the Jacobi/
Sherman--Morrison cocycle.

The nonmonotone intermediate values mean that a fixed two-row truncation is
not sufficient at every finite `N`; a theorem must allow a slowly growing
shell width and control the remaining interior tail.
