# E72.87 -- CCGD quadratic certificate

**Date:** 2026-07-09.
**Role:** express Cauchy-channel Green decay as an exact finite quadratic inequality.

## 0. Motivation

E72.86 shows that physical tightness should not be proved through a full operator-norm estimate:

```text
||T_H C_E^(-1)S_R|| -> 0
```

is too strong for the finite data. The theorem must use the specific Cauchy source:

```text
r_s^even=s(s^2I-D^2)^(-1)1.
```

This note turns that channel statement into a finite algebraic certificate.

## 1. Coordinate form

Let `B_x` be an orthonormal basis of the even `Q_x`-space, and write:

```text
C_E = B_x^*C_xB_x,
a_x(s)=B_x^*r_s^even,
y_x(s)=C_E^(-1)a_x(s),
g_x(s)=B_xy_x(s).
```

For a physical-height cutoff `H`, let:

```text
T_H = diag(1_{|d_n|>H}),
K_H = B_x^*T_HB_x.
```

Then the Cauchy-channel physical tail is exactly:

```text
Tail_H(s)
 := ||T_H g_x(s)||^2
 = y_x(s)^*K_Hy_x(s)
 = a_x(s)^*C_E^(-1)K_HC_E^(-1)a_x(s).                       (QTail)
```

The total channel norm is:

```text
Tot(s)
 := ||g_x(s)||^2
 = y_x(s)^*y_x(s)
 = a_x(s)^*C_E^(-2)a_x(s).                                  (QTot)
```

Therefore:

```text
CCGD_H(s)
 := Tail_H(s)/Tot(s)
 = a_x(s)^*C_E^(-1)K_HC_E^(-1)a_x(s)
   / a_x(s)^*C_E^(-2)a_x(s).                                (QR)
```

This is finite, explicit, and contains no hidden inverse beyond the fixed finite matrix `C_E`.

## 2. Rationality in s

Each coordinate of `a_x(s)` is a finite linear combination of:

```text
s/(s^2-d_n^2).
```

Thus, after clearing the mesh denominator:

```text
D_x(s)=prod_n(s^2-d_n^2),
```

both numerator and denominator of `(QR)` become finite Hermitian quadratic forms in rational functions
of `s`. On any compact set away from the mesh poles, `(QR)` is a completely explicit finite rational
inequality.

## 3. The exact theorem now needed

The Cauchy-channel Green decay theorem is:

```text
CCGD:
For every compact s-window K,

lim_{H->infty} limsup_{x->infty} sup_{s in K}
  CCGD_H(s) = 0.                                             (CCGD)
```

Equivalently, using `(QR)`:

```text
lim_{H->infty} limsup_{x->infty} sup_{s in K}
  a_x(s)^*C_E^(-1)K_HC_E^(-1)a_x(s)
  / a_x(s)^*C_E^(-2)a_x(s) = 0.                              (CCGD-QR)
```

This is the exact finite inequality that replaces the failed full operator-norm Green decay.

## 4. Numerical verification

The companion script:

```text
E72_87_ccgd_certificate_probe.py
```

checks `(QTail)` against direct tail computation.

Representative output:

```text
lambda=20, N=40:
  s=5,  H=8   tail=3.355e-02  diff=3.5e-17
  s=10, H=12  tail=4.387e-02  diff=6.2e-17
  s=10, H=18  tail=7.927e-03  diff=1.2e-17
  s=15, H=18  tail=2.819e-02  diff=5.6e-17
  s=15, H=24  tail=1.155e-02  diff=3.5e-18

lambda=24, N=48:
  s=5,  H=8   tail=1.004e-02  diff=8.7e-18
  s=10, H=12  tail=1.348e-02  diff=4.7e-17
  s=15, H=18  tail=1.067e-02  diff=3.3e-17
  s=15, H=24  tail=2.470e-03  diff=1.1e-17
```

The data match the expected physical-height pattern: the tail is large when `H` lies below the spectral
height of `s`, and small once `H` passes that height by a fixed buffer.

## 5. How it feeds the WRL route

If `(CCGD)` holds, E72.81's root transport identity reduces to a finite physical-height band:

```text
|d_n|<=H.
```

Then scalar WRL annihilation is reduced to proving the finite-band root transport law:

```text
i C_{P_Hg,k}(tau_j)
-(exp(i tau_jL)-1)L^(-1)C_{P_Hg,1}(tau_j)M_k(tau_j) -> 0,
```

followed by `H->infty`.

Thus the remaining route splits cleanly into:

```text
1. CCGD-QR: prove physical tightness of the Cauchy channel;
2. finite-band transport: prove E72.81 after replacing g by P_Hg.
```

## 6. Status

```text
proved: exact finite quadratic formula for CCGD;
verified: quadratic certificate equals direct tail to roundoff;
open:   prove the CCGD-QR inequality uniformly, then prove finite-band transport.
```
