# E73.065 results - rowspace form of signed CMAIN

## 1. Purpose

E73.063 showed that the positive `L1` Cauchy ceiling is far too large.
E73.064 therefore moved the arithmetic core to the signed value

```text
C_signed(t)=sum_n xi_n/(t-d_n).
```

E73.065 tests the exact linear-algebra meaning of this cancellation.

Let

```text
E_x=H_x-mu_x I,
E_x xi_x=0,
k_t(n)=1/(t-d_n).
```

Since `H_x` is self-adjoint, `E_x` is self-adjoint and

```text
closure Row(E_x) = xi_x^perp
```

when the ground state is simple.  Therefore

```text
dist(k_t,Row(E_x)) = |<xi_x,k_t>| = |C_signed(t)|.
```

Thus signed CMAIN is not a mysterious cancellation of scalar fractions.  It is a rowspace
proximity statement for the finite CCM operator.

## 2. Representative output

```text
E73.065 ROW-CMAIN probe
Interprets signed Cauchy value as rowspace distance to E=H-mu I.
 lam     L tau   gamma  signedB rowNormB   relB    l1B  signed    rowNorm    relRow
  16   5.545   14.13   37.59  -10.595   -0.893  -9.702  -1.199 1.312e-08  2.166e-01 6.058e-08
  16   5.545   14.13   30.42  -13.619   -0.655 -12.963  -1.018 7.395e-11  3.255e-01 2.272e-10
  16   5.545   14.13   32.94  -10.301   -0.756  -9.545  -1.090 2.174e-08  2.741e-01 7.931e-08
  18   5.781   14.13   37.59  -12.041   -0.826 -11.216  -1.096 6.677e-10  2.349e-01 2.842e-09
  18   5.781   14.13   32.94  -12.421   -0.679 -11.742  -0.997 3.429e-10  3.038e-01 1.129e-09
  18   5.781   14.13   30.42   -9.085   -0.567  -8.519  -0.931 1.194e-07  3.701e-01 3.227e-07
  20   5.991   14.13   32.94  -12.000   -0.604 -11.396  -1.052 4.675e-10  3.394e-01 1.378e-09
  20   5.991   14.13   37.59  -10.618   -0.763  -9.855  -1.149 5.544e-09  2.551e-01 2.174e-08
  20   5.991   14.13   30.42   -9.413   -0.473  -8.940  -0.988 4.796e-08  4.286e-01 1.119e-07
  24   6.356   14.13   32.94  -12.438   -0.442 -11.996  -0.926 1.024e-10  4.417e-01 2.317e-10
  24   6.356   14.13   30.42  -13.608   -0.231 -13.377  -0.830 1.176e-11  6.521e-01 1.803e-11
  24   6.356   14.13   37.59   -8.902   -0.645  -8.257  -1.054 7.074e-08  3.033e-01 2.332e-07
```

Here `valueB` means `log(value)/log(L)`.

## 3. Diagnosis

The relative rowspace defect

```text
dist(k_t,Row(E_x))/||k_t||
```

is typically between `L^-8` and `L^-13` on the FAR3 nodes.

This is exactly the signed cancellation scale seen in E73.063, but it is now attached to a
structural object:

```text
the Cauchy row k_t is almost in Row(H_x-mu_x I).
```

The weak point is also clearer.  The earlier split

```text
PREF-5 + CMAIN-10
```

is sufficient but too rigid as an asymptotic target.  Some tested nodes have
`|C_signed(t)|` closer to `L^-9` than `L^-10`, while their full weighted term still satisfies the
main budget because the geometric prefactor is smaller there.

Therefore the next theorem should bind the actual product entering WCS, not an over-separated
Cauchy exponent.

## 4. Surviving target

The correct main theorem is:

```text
ROW-MAIN-5:
Pref_k(A,L) dist(k_t,Row(E_x)) <= C L^-5
```

for the three FAR nodes.

Since

```text
dist(k_t,Row(E_x))=|C_signed(t)|,
```

this is exactly the `Main_3` estimate in rowspace form.

## 5. Gauge correction

This table used the symmetric pole-even gauge vector.  E73.068 shows that the exact ground
eigenvector is the load-bearing object for the projection lemma, and that the symmetric gauge is
conservative in the tested windows.

Thus the algebraic lesson of E73.065 remains valid, but exact numerical budgets should be read from
E73.069.

## 6. Status

```text
proved algebraically: signed Cauchy value = rowspace distance;
observed numerically: FAR3 nodes have tiny rowspace defect;
replaces: over-strong standalone CMAIN-10 as the sharp main target;
open: prove ROW-MAIN-5 uniformly from the finite CCM equation.
```
