# E72.359 results - double-residue projector probe

Command:

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_359_double_residue_probe.py
```

The probe checks the double-residue certificate with nontrivial local units:

```text
Z(z)=(z-a)^m U(z),       W(w)=(w-b)^n V(w),
U(a),V(b) != 0.
```

It compares:

```text
taylorBlock = ||Delta mod ((z-a)^m,(w-b)^n)||,
projector   = ||double-residue principal part of Delta/(Z(z)W(w))||.
```

## Table

```text
m   n kind       taylorBlock   projector
1   1 member     0.00000e+00   0.00000e+00
1   1 nonmember  1.07703e+00   1.05591e+00

2   2 member     0.00000e+00   0.00000e+00
2   2 nonmember  1.07703e+00   1.06234e+00

3   1 member     0.00000e+00   0.00000e+00
3   1 nonmember  1.07703e+00   1.06555e+00

3   3 member     0.00000e+00   0.00000e+00
3   3 nonmember  1.07703e+00   1.06081e+00

5   2 member     0.00000e+00   0.00000e+00
5   2 nonmember  1.07703e+00   1.07727e+00
```

## Reading

The double-residue projector is calibrated with units included:

```text
ideal member    => projector=0;
ideal nonmember => projector>0.
```

Therefore `DCERT-CFIR` can be checked as a finite list of local contour coefficients.  Multiplicities
are handled by the powers `(z-a)^{m-r-1}` and `(w-b)^{n-s-1}` in the projector, not by extra analytic
estimates.

## Consequence

The next exact identity to prove is:

```text
Pi_{a,r;b,s}[Delta_CFIR]=O_T(L^B)
```

for all finite Xi-zero Hermite slots.  This is equivalent to `CFIR-DIV`, but is more directly
auditable because every `Pi` is a concrete local contour coefficient.
