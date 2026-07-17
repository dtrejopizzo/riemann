# E73.203 results - interval budget

Command:

```text
python3 E73_203_interval_budget_probe.py
```

Output:

```text
E73.203 interval budget probe
Eigenline gap and functional sensitivity for the E73.202 certificate.
 lam     L gamma row centerB gapB eigResB eigRadB sensB etaRadB totalRadB ratio
  12   4.970   14.13   0  -21.29 -22.12   -21.06     1.49    1.95     1.49      3.45  1.7e+17
  12   4.970   14.13   1  -21.18 -22.12   -21.06     1.49    1.95     1.49      3.45  1.4e+17
  12   4.970   21.02   0  -20.43 -22.12   -21.06     1.49    0.53     1.49      2.03  4.3e+15
  12   4.970   21.02   1  -19.87 -22.12   -21.06     1.49    0.53     1.49      2.03  1.8e+15
  16   5.545   14.13   0  -18.95 -20.30   -19.30     1.40    1.58     1.40      2.98  2.1e+16
  16   5.545   14.13   1  -20.03 -20.30   -19.30     1.40    1.58     1.40      2.98  1.3e+17
  16   5.545   21.02   0  -18.21 -20.30   -19.30     1.40    1.56     1.40      2.96  5.6e+15
  16   5.545   21.02   1  -19.13 -20.30   -19.30     1.40    1.56     1.40      2.96  2.7e+16
```


Reading:

```text
The naive Davis-Kahan certificate from the existing double eigensolver fails.
The gap is tiny (around L^-20--L^-22), while the floating eigen residual is of
comparable scale.  Therefore rho_xi=2 eps_eig/gap is O(L^1), and transporting
that radius through the scalar functional gives a useless enclosure.

This is not a failure of TRANS-CELL or of the digamma certificate.  It says the
full interval implementation cannot use the double matrix/eigenvector as the
certified eigenline source.  The near-radical ground branch must be certified
with high-precision matrix entries plus interval Newton/Riesz projection, or
by a bordered finite system that treats (mu,xi) as certified variables.
```
