# E73.150 Results - Constructive Rowspace Certificate

Date: 2026-07-12.

Script:

```text
E73_150_constructive_rowspace_certificate.py
```

Purpose:

Attempt to strengthen E73.149 by constructing

```text
r = yE + alpha xi^*
```

for the forced signed rows, with

```text
E=H-mu I,
E xi=0.
```

Output after using the full complement pseudoinverse:

```text
 lam     L gamma row  alphaB      yB    errB     d1B     d2B status
  16   5.545   14.13   0  -19.907   2.826  -0.781   0.157   0.425 PASS
  16   5.545   14.13   1  -20.529   0.491   0.243   0.124   0.372 PASS
  20   5.991   21.02   0  -18.868   1.562  -1.014   0.179   0.430 PASS
  24   6.356   25.01   1  -19.694   0.119  -1.325   0.256   0.565 PASS
  28   6.664   14.13   0  -16.886   2.401  -1.681   0.242   0.515 FAIL
  32   6.931   25.01   1  -17.570   0.005  -1.480   0.137   0.403 PASS
```

Full table is in the terminal output of the script.

## Reading

The algebraic decomposition is formally exact, but the full pseudoinverse is
not a useful proof object: it inverts very small complement eigenvalues and
produces unstable multipliers.  This is why the reconstruction exponent
`errB` is not at numerical roundoff in the direct finite computation.

The stable truncated pseudoinverse from the first run gave smaller
multipliers, but then the unreconstructed part is a near-null spectral tail.

Therefore the constructive route becomes:

```text
r = y_good E + alpha xi^* + near-null tail.
```

The next useful object is not the full Moore-Penrose inverse, but a spectral
cutoff certificate that separates:

```text
null coefficient alpha,
near-null complement tail,
bulk rowspace component.
```

This avoids pretending that `E^+` is a bounded analytic operator.
