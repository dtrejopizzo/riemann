# P76.037 - External mesh correction results

At fixed `lambda=6`, subtracting the exact external sine-zero trace gives
the following signed relative core errors:

```text
N=6:  approximately -0.62
N=9:  approximately -0.50
N=12: approximately -0.44
```

The variation across `sigma=0.6,...,2` is below `0.006` at `N=12`.  Before
subtraction the corresponding raw error is `+0.735`.

Interpretation:

```text
raw trace = finite arithmetic core + external sine tail;
Xi trace  = low Xi divisor       + high Xi tail.
```

The external sine tail overcompensates the missing high Xi tail at these
cutoffs.  This quantitatively explains the nearly scalar `1/N` defect seen
in P76.035 and confirms that separate absolute estimates are structurally
wrong.  The two tails must be compared as the signed second bracket in
`(RTS-4)`.
