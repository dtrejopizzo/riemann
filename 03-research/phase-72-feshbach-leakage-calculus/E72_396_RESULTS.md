# E72.396 results - Cauchy projection gate

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_396_cauchy_projection_probe.py
```

## Output

```text
E72.396 Cauchy projection probe
 lam     L    nO nK   cond(COO)    max|GK|     max|Proj|   expWeighted
   8   4.159    2  4   1.029e+00  2.615e-09  6.381e-11    1.466e-10
  10   4.605    2  4   1.029e+00  2.605e-09  6.076e-11    1.526e-10
  12   4.970    2  4   1.029e+00  1.329e-09  3.286e-11    8.878e-11
  14   5.278    2  4   1.029e+00  3.146e-09  1.000e-10    2.874e-10
```

## Interpretation

The diagnostic is the finite projection

```text
Pi_{O<-K}G_K = C_OO^(-1)C_OKG_K.
```

The column `expWeighted` measures

```text
max_{a in O} e^(Re a L)|(Pi_{O<-K}G_K)_a|.
```

For this synthetic off-line pair and the first four true critical heights, the projection is small in
the tested windows.  This is consistent with `NAT-PROJ`, but it is not a uniform proof.  The value of
the test is diagnostic: it confirms that the remaining condition is exactly a finite Cauchy projection
condition on the critical nodal vector, not a consequence of Cauchy invertibility alone.

## Status

```text
verified: finite projection operator and weighted diagnostic are computable;
observed: no immediate numerical obstruction for the tested critical vector;
remaining: prove NAT-PROJ uniformly or make it the final finite identity for Phase 73.
```

