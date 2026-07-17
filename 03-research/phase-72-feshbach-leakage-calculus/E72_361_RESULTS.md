# E72.361 results - alternating-rank CFIR probe

Command:

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_361_alternating_rank_probe.py
```

The probe checks the finite simple-window certificate:

```text
A=V(sk^T-ks^T)V^T.
```

Since `V` is invertible, `A=0` if and only if `s,k` are collinear.

## Table

```text
N kind          altNorm      minSing[s,k]    condV
2 collinear     1.00012e-15  3.17546e-17     1.2963e+00
2 perturbed     1.49506e+00  6.92135e-02     1.2963e+00

3 collinear     8.23263e-17  1.59926e-16     6.3651e+00
3 perturbed     1.56270e+00  9.36363e-02     6.3651e+00

5 collinear     4.88144e-14  2.34820e-15     7.6024e+00
5 perturbed     1.24801e+01  1.23066e-01     7.6024e+00

8 collinear     4.42475e-14  7.13128e-16     8.9707e+00
8 perturbed     3.27023e+01  2.44479e-01     8.9707e+00
```

## Reading

The alternating residue matrix is a faithful certificate:

```text
collinear  => altNorm at roundoff;
perturbed  => altNorm large.
```

Thus, on simple Xi-zero windows, `CFIR-DIV` can be checked as one skew matrix condition rather than a
raw list of all pairwise minors.

## Consequence

The next analytic expansion should target the skew form

```text
int int phi_p(z)phi_q(w)
[S(z)K(w)-S(w)K(z)] Z'/Z(z)Z'/Z(w) dw dz,
```

and preserve the antisymmetry.  Symmetric archimedean-prime pieces cancel before any absolute value is
taken.
