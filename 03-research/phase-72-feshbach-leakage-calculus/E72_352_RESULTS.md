# E72.352 results - rowspace invariance certificate

Command:

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_349_cfir_row_candidate_probe.py
```

The probe adds the explicit rowspace row

```text
k_a(C_E-mu I)
```

to each `window_tail` candidate and compares the null component before and after the
addition.  The relative norm of the row may change, but the load-bearing amplitude

```text
R xi
```

must be invariant.

## Table

```text
lam    N roots node    maxBaseRel    maxAddedRel    maxDeltaAmp    maxRowspaceAmp
 6.0  10     2 root    1.28185e-16   1.46185e-16   2.23282e-16    3.25233e-17
 6.0  10     2 shift   1.20840e-01   1.21848e-01   1.40433e-15    2.05557e-16

 8.0  12     3 root    7.27820e-13   7.29920e-13   2.76508e-16    2.53725e-17
 8.0  12     3 shift   2.18073e-01   2.20085e-01   5.02430e-15    1.45588e-16

10.0  14     3 root    6.40950e-13   6.42853e-13   1.36628e-15    5.01877e-17
10.0  14     3 shift   1.89467e-01   1.91271e-01   3.33067e-15    2.22205e-16

12.0  16     3 root    3.55968e-15   3.51716e-15   2.98785e-15    2.76830e-15
12.0  16     3 shift   1.26997e-01   1.27577e-01   1.10309e-14    1.14596e-14
```

## Reading

The shifted controls still have large relative CFIR defects:

```text
1.27e-1 to 2.18e-1.
```

After adding explicit rowspace rows, the null amplitude changes only by roundoff:

```text
1e-15 to 1e-14.
```

This verifies the analytic lemma of E72.352.  Additive transformed-equation rows cannot
repair the CFIR defect.  They are already in `Row(C_E-mu I)`.

## Consequence

The next target is not to add the full transformed operator row to `window_tail`.  The
next target is to derive the exact finite residual row `R_T` before the rowspace test
and prove directly

```text
R_T in Row(C_E-mu I).
```

Equivalently, the determinant certificates must vanish for the exact row:

```text
R_T adj(C_E-mu I)=0,
det ReplaceRow(C_E-mu I; i, R_T)=0.
```
