# E73.122 Results - CRL Exponent Extractor

Date: 2026-07-12.

Script:

```text
E73_122_crl_exponent_extractor.py
```

Purpose:

Extract the quantities named in E73.121 on standard wide boxes:

```text
dist(-gamma, nearest Cauchy root),
sup |C_x'|,
|C_x(-gamma)|,
S_FAR^+,
NLC^+,
Gloc^+,
MAIN^+,
OUT^+.
```

The goal is not to add a new gate.  The goal is to identify the analytic
sublemma that a uniform proof must actually supply.

Output:

```text
E73.122 CRL exponent extractor
Standard wide boxes only; exponents are log(value)/log(L).
 lam     L tau      distB    derB      CB   SFARB    NLCB   GlocB   main   outB nTri
  20   5.991   14.13    0.401   0.980 -17.871   6.067 -16.551 -15.643 1.411e-01  -6.737    2
  24   6.356   14.13  -17.120  -0.122 -17.817   5.750 -16.916 -15.730 2.366e-01 -13.590    1
  28   6.664   14.13  -17.541   1.394 -17.254   5.558 -16.367 -14.890 1.912e-01 -13.337    1
  32   6.931   14.13    0.164   0.269 -17.656   5.445 -17.237 -15.259 8.587e-03 -13.592    1
  20   5.991   21.02    0.401   0.980 -17.871   6.054 -16.551 -15.643 1.348e-01  -6.903    2
  24   6.356   21.02  -17.120  -0.122 -17.817   5.667 -16.916 -15.730 2.542e-01 -13.356    1
  28   6.664   21.02  -17.541   1.394 -17.254   5.534 -16.367 -14.890 2.050e-01 -13.083    1
  32   6.931   21.02    0.164   0.269 -17.656   5.438 -17.237 -15.259 9.258e-03 -13.698    1
```

## Main diagnostic

The nearest-root distance is not the stable invariant:

```text
distB ranges from about -17.5 to +0.4.
```

In contrast, the Cauchy value itself is stable:

```text
CB = log(|C_x(-gamma)|)/log(L) is consistently about -17.
```

Therefore the asymptotic sublemma in E73.121 should be sharpened.
The primary target is not a uniform geometric root-lock statement

```text
dist(-gamma, Div(P_x)) <= C L^-d.
```

The primary target is the small-value statement

```text
|C_x(-gamma)| <= C_C L^-17
```

on natural-height local rows.  Root-lock can explain some rows, but it is
not the right uniform invariant.

## Consequences for GATE-73

The gate products are dominated by:

```text
S_FAR^+ ~ L^5.4 ... L^6.1,
NLC^+   ~ L^-16.3 ... L^-17.2,
Gloc^+  ~ L^-14.9 ... L^-15.7,
```

which explains:

```text
LOCK ~ S_FAR^+ * NLC^+          << L^-5,
TAIL ~ S_FAR^+ * Gloc^+ * L^2/M^2 << L^-5.
```

For `lambda>=24`, the compatible FAR triple is unique and the complement
is already at

```text
OUT <= L^-13.
```

At `lambda=20`, two compatible triples remain on the wide box, explaining
the finite subdivision in E73.120.

## Corrected analytic target

Replace the preliminary `CRL(L)` target by:

```text
CSV(L)  [Cauchy Small-Value]
For every natural-height standard box and every local row gamma,

|C_x(-gamma)| <= C_C L^-17,
```

together with elementary Hermite/FAR envelopes:

```text
S_FAR^+ <= C_F L^6,
Gloc^+  <= C_G L^-15,
OUT^+   <= C_O L^-13       after unique compatible FAR triple,
MAIN^+  <= C_M < 1.
```

Then:

```text
CSV(L) + elementary envelopes
=> Asymptotic Standard-Box Theorem
=> Uniform GATE-73
```

modulo the finite transition manifest E73.120.

