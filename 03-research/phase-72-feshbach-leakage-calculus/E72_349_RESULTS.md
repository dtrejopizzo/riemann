# E72.349 RESULTS -- CFIR row-candidate stress

**Command**

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_349_cfir_row_candidate_probe.py
```

## Results

```text
 lam   N roots node       mode      maxNullAmp    maxRelNull    rmsRelNull
  6.0  10     2  root     base   3.09471e-31   6.10797e-17   4.56992e-17
  6.0  10     2  root     self   1.11826e-15   9.53695e-17   6.87642e-17
  6.0  10     2  root   window   8.95442e-16   7.58394e-17   5.46946e-17
  6.0  10     2 shift     base   1.76409e-15   1.11790e-01   8.02246e-02
  6.0  10     2 shift     self   3.29725e+00   1.11790e-01   8.02246e-02
  6.0  10     2 shift   window   3.34113e+00   1.15851e-01   8.42018e-02
  8.0  12     3  root     base   5.76105e-27   7.45573e-13   4.30552e-13
  8.0  12     3  root     self   1.35732e-11   7.45571e-13   4.30551e-13
  8.0  12     3  root   window   1.35838e-11   7.26450e-13   4.24393e-13
  8.0  12     3 shift     base   6.28661e-15   2.10336e-01   1.80640e-01
  8.0  12     3 shift     self   1.76493e+01   2.10336e-01   1.80640e-01
  8.0  12     3 shift   window   1.61703e+01   2.18963e-01   1.78236e-01
 10.0  14     3  root     base   1.47043e-26   6.49278e-13   3.76189e-13
 10.0  14     3  root     self   1.34811e-11   6.49288e-13   3.76194e-13
 10.0  14     3  root   window   1.33666e-11   6.32209e-13   3.66343e-13
 10.0  14     3 shift     base   2.09832e-14   2.00507e-01   1.34630e-01
 10.0  14     3 shift     self   1.81692e+01   2.00507e-01   1.34630e-01
 10.0  14     3 shift   window   1.74531e+01   1.81583e-01   1.25906e-01
 12.0  16     3  root     base   9.37417e-29   3.67268e-15   2.12491e-15
 12.0  16     3  root     self   8.76812e-14   3.68005e-15   2.12917e-15
 12.0  16     3  root   window   8.83754e-14   3.63430e-15   2.12953e-15
 12.0  16     3 shift     base   2.08515e-14   1.53257e-01   9.48468e-02
 12.0  16     3 shift     self   1.76244e+01   1.53257e-01   9.48468e-02
 12.0  16     3 shift   window   1.85270e+01   1.28800e-01   7.98047e-02
```

## Interpretation

At finite Cauchy roots, the relative null defect is tiny:

```text
root maxRelNull ~ 1e-17 to 1e-12.
```

This is expected because `k_a xi=G(a)=0` at those finite roots.  It confirms that the row-ideal
detector sees Cauchy invisibility correctly.

At shifted control nodes, the relative defect is large:

```text
shift maxRelNull ~ 0.11 to 0.22.
```

Thus the detector is not blind.  Moving off the finite root destroys row-ideal membership unless the
missing CFIR terms restore it.

## Consequence

The partial rows `base`, `self`, and `window` are not enough to certify the full transformed route away
from root nodes.  The collapsed tail and exact normalization terms in E72.342--E72.343 are genuinely
load-bearing.

## Status

```text
validated: row-ideal detector on the actual singular finite operator H_actual-lambda_0 I;
validated: finite root rows are Cauchy-invisible;
validated: shifted control nodes expose nontrivial row defects;
next: build the full R_T row including TailBasis and exact normalization.
```
