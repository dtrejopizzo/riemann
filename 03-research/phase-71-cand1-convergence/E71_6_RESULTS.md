# E71.6 -- characteristic-function convergence probe results

**Date:** 2026-07-07.
**Script:** `E71_6_characteristic_convergence_probe.py`.

## Output

The script tested the raw entire function

```text
Phi_N(s) = (2/sqrt(L)) sin(sL/2) sum_k xi_k/(s-d_k)
```

at `lambda=5` on the real grid `[0,42]`, fitting one scalar against `Xi`.

```text
grid: [0,42.0] with 260 points, max|Xi|=4.971208e-01
   N      |c|        relL2        relSup       maxAbsErr
  14  1.065e-02 9.999528e-01 9.994814e-01 4.968630e-01
  18  2.212e-02 9.994794e-01 9.946426e-01 4.944575e-01
  24  3.587e-01 9.983141e-01 9.914473e-01 4.928690e-01
  40  1.600e-02 9.997957e-01 9.987583e-01 4.965035e-01
```

## Reading

The raw `Phi_N` does **not** show function-level convergence to `Xi` under a single least-squares
scalar normalization. The relative error stays essentially `1`.

This does not contradict E71.2-E71.4: zero locking can happen without global function convergence of
this raw normalization.

It does mean the Hurwitz closure theorem from E71.5 cannot use this naive `Phi_N` as-is.

## Consequence

The CAND-1 closure target sharpens again:

```text
not enough: roots of raw Phi_N lock numerically;
needed:     a canonical CCM characteristic/determinant normalization
            forming a normal family and converging locally uniformly to Xi.
```

The next object must be the actual Fredholm/determinant-like characteristic function of `H_lambda`,
or a de Branges/Hermite-Biehler normalization, not the unnormalized ground-vector rational numerator.
