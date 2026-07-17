# E72.92 -- Phi invisibility audit

**Date:** 2026-07-09.
**Role:** decide whether the low-band cofactor identity can be closed by proving norm-smallness of
the transported vector.

## 0. Input

E72.91 writes finite-band transport as:

```text
R_{x,H}(s;tau)=<r_s^even,phi_{x,H,tau}>,
```

where:

```text
phi_{x,H,tau}=B_xC_E^(-1)B_x^*P_HZ_x(tau).
```

A tempting closure would be:

```text
||phi_{x,H,tau_j}|| -> 0.
```

Then every Cauchy pairing would vanish automatically.

## 1. Numerical audit

The companion script:

```text
E72_92_phi_invisibility_probe.py
```

measures `||phi||`, `|<r_s,phi>|`, and their ratio.

Representative output:

```text
lambda=12:
  tau=0.825  ||phi||=1.328e-01  |pair|=3.092e-03  ratio=2.33e-02
  tau=8.118  ||phi||=2.174e-02  |pair|=7.891e-03  ratio=3.63e-01

lambda=20:
  tau=0.241  ||phi||=1.497e-01  |pair|=3.137e-02  ratio=2.10e-01
  tau=3.844  ||phi||=3.536e-02  |pair|=6.462e-03  ratio=1.83e-01

lambda=24:
  tau=6.889  ||phi||=8.967e-03  |pair|=3.897e-03  ratio=4.35e-01
  tau=9.167  ||phi||=1.017e-02  |pair|=9.460e-03  ratio=9.30e-01
```

## 2. Conclusion

Norm-smallness is not the right theorem. The vector `phi` can be small in absolute norm for some roots,
but the Cauchy pairing can still be a large fraction of that norm.

Thus `(FBRT)` must be proved as:

```text
Cauchy invisibility of phi,
```

not as:

```text
phi -> 0 in Hilbert norm.
```

## 3. Next reduction

Since:

```text
<r_s^even,phi>
 = sum_n conjugate(s/(s^2-d_n^2)) phi_n,
```

finite-band invisibility is a finite Stieltjes/moment statement for the signed vector `phi`. The next
target is the finite-band moment criterion:

```text
all Cauchy tests vanish
  <=> all finite-band Stieltjes residues/moments vanish.
```

## 4. Status

```text
rejected: norm-small phi as the proof route;
kept:     Cauchy invisibility as the exact FBRT content;
next:     finite-band Stieltjes moment criterion.
```
