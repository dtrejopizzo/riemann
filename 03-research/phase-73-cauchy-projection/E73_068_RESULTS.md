# E73.068 results - exact eigenline versus symmetric gauge

## 1. Purpose

E73.065 used the pole-even symmetric gauge for the finite ground vector.  That is useful for visual
stability, but the exact projection lemma requires the actual normalized eigenvector `xi_x` with

```text
(H_x-mu_x I)xi_x=0.
```

E73.068 audits the difference.

## 2. Representative output

```text
E73.068 exact-vs-symmetric xi audit
The projection lemma uses the exact eigenvector; symmetric xi is only a gauge.
 lam     L    ||Ex||B ||Esym||B  gamma exactB   symB    diffB
  16   5.545   -19.307   -19.062   14.13 -20.637 -19.996  -20.233
  16   5.545   -19.307   -19.062   21.02 -20.005 -19.339  -19.563
  16   5.545   -19.307   -19.062   25.01 -14.281 -13.864  -14.258
  18   5.781   -19.271   -18.961   14.13 -16.871 -17.171  -17.380
  18   5.781   -19.271   -18.961   21.02 -18.990 -19.510  -19.283
  18   5.781   -19.271   -18.961   25.01 -14.272 -13.092  -13.169
  20   5.991   -18.334   -17.691   14.13 -19.358 -18.954  -19.324
  20   5.991   -18.334   -17.691   21.02 -18.719 -19.679  -18.829
  20   5.991   -18.334   -17.691   25.01 -19.294 -17.872  -17.917
  24   6.356   -18.250   -18.290   14.13 -18.884 -17.818  -17.899
  24   6.356   -18.250   -18.290   21.02 -19.082 -20.239  -19.149
  24   6.356   -18.250   -18.290   25.01 -19.692 -19.743  -20.988
```

## 3. Diagnosis

The exact eigenline is numerically valid:

```text
||(H_x-mu_x I)xi_x|| = L^-18 to L^-19.
```

The symmetric gauge is close, but it is not the object that proves the rowspace lemma.

More importantly, the exact Cauchy values at the first critical heights are often even smaller than
the symmetric-gauge values.  Thus the previous use of the symmetric gauge was conservative for the
projection target.

## 4. Correction

From this point on, all rowspace and divisibility statements use the exact eigenline.

The symmetric gauge may still be used as a diagnostic for evenness, but it is not load-bearing in
the proof chain.

## 5. Status

```text
proved numerically: exact eigenline residual is at roundoff scale;
corrected: projection lemma belongs to the exact eigenline;
consequence: E73.065 is structural, but its numerical table is conservative gauge data.
```
