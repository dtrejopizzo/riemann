# E72.90 -- Finite-band transport scaling

**Date:** 2026-07-09.
**Role:** test whether the finite-band root transport residual visibly decays after CCGD-style
truncation.

## 0. Question

E72.89 reduced the second half of the proof to:

```text
R_{x,H}(s;tau_j)->0
```

for fixed physical height `H`, finite Weyl roots `tau_j`, and then `H->infty`.

The first sanity check is whether the finite-band residual decays in the finite harness once the Cauchy
tail is already small.

## 1. Probe

The companion script:

```text
E72_90_fbrt_scaling_probe.py
```

fixes:

```text
s=10+0.2i,
tau_j <= 10,
H in {12,18,24},
```

and measures:

```text
max_j |R_{x,H}(s;tau_j)|,
rms_j |R_{x,H}(s;tau_j)|,
tail energy of g outside H.
```

## 2. Result

Representative output:

```text
lambda   H   roots   max|R_H|   rms|R_H|   tail-energy
8       18     6     1.904e-02  1.157e-02  6.084e-03
10      18     6     2.852e-02  1.772e-02  1.471e-02
12      18     5     1.566e-02  8.140e-03  1.786e-03
16      18     8     2.656e-02  1.136e-02  2.655e-03
20      18     7     3.137e-02  1.424e-02  7.927e-03
24      18     4     9.460e-03  6.390e-03  3.299e-03
```

Changing `H` from `18` to `24` barely changes `R_H` once the physical tail is small.

## 3. Interpretation

This is a useful negative result:

```text
the remaining obstruction is not the CCGD tail.
```

After the Cauchy channel has been physically truncated, the residual is still mostly an internal
finite-band quantity. Therefore `(FBRT)` cannot be proved merely by tightening `H`; it needs an
additional finite-band cofactor identity.

## 4. Next target

The finite-band residual must be written as:

```text
R_{x,H}(s;tau)
 = <P_HB_xC_E^(-1)B_x^*r_s^even, Z_x(tau)>,
```

where:

```text
Z_x(tau)
 = iS_tau k_x
   -(exp(i tau L)-1)L^(-1)M_k(tau)S_tau1.
```

Equivalently:

```text
R_{x,H}(s;tau)
 = <r_s^even, B_xC_E^(-1)B_x^*P_HZ_x(tau)>.
```

The new theorem must therefore prove that the transport vectors:

```text
B_xC_E^(-1)B_x^*P_HZ_x(tau_j)
```

are asymptotically invisible to the Cauchy tests `r_s^even` at finite Weyl roots.

## 5. Status

```text
observed: finite-band residual does not visibly decay just from physical truncation;
conclusion: FBRT requires a new finite-band cofactor identity;
next: derive the exact low-band cofactor form.
```
