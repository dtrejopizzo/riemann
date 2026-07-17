# E73.040 - Optimized mesh-root audit

## 1. Purpose

E73.039 introduced `MRC`, a mesh-root covering estimate.  The first optimization is to assign each
critical height to the best available local root certificate, instead of choosing intervals by hand.

The pointwise diagnostic is:

```text
|C_x(gamma)| = slope_point(gamma,rho)|gamma-rho|.
```

This is exact but tautological, because

```text
slope_point(gamma,rho)=|C_x(gamma)|/|gamma-rho|.
```

Therefore it cannot be used as a proof.

## 2. Non-circular derivative envelope

A non-circular replacement is the fundamental theorem of calculus:

```text
C_x(gamma)-C_x(rho)=int_rho^gamma C_x'(t)dt.
```

Since `C_x(rho)=0`,

```text
|C_x(gamma)|
<= |gamma-rho| sup_{t in [rho,gamma]} |C_x'(t)|.
```

Using only absolute residues gives

```text
sup |C_x'(t)|
<= sum_n |xi_n| / dist([rho,gamma],d_n)^2.
```

This is non-circular but incoherent.

## 3. Result

E73.040 shows that this absolute derivative envelope is too coarse.  The optimized certificate
almost always chooses the trivial value `|C_x(gamma)|` instead of the root derivative bound.

Representative output:

```text
E73.040 optimized mesh-root covering probe
pointDiag is tautological; intervalMRC uses a non-circular derivative envelope.
 lam     L sigma     tau  m nK roots rootUse  pointDiag intervalMRC     actual  int/act
   8   4.159  0.05   14.13  2  6    12       0  2.395e-07  2.395e-07  2.395e-07 1.00e+00
  16   5.545  0.20   21.02  3  6    20       0  2.858e-05  2.858e-05  2.858e-05 1.00e+00
  24   6.356  0.20   21.02  3  6    34       2  1.726e-05  1.726e-05  1.726e-05 1.00e+00
```

## 4. Conclusion

The local finite-root mechanism is real as an identity, but the proof cannot use the absolute
derivative envelope

```text
sum |xi_n|/dist^2.
```

That envelope loses the signed structure of the finite CCM vector and gives no improvement over the
trivial `|C_x(gamma)|` bound.

## 5. Status

```text
proved: pointwise root representation is tautological;
tested: absolute derivative root envelope is non-circular but too weak;
remaining: use signed rational variation or direct weighted Cauchy smallness.
```
