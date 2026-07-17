# E72.94 -- Moment shortcut audit

**Date:** 2026-07-09.
**Role:** test whether finite-band root transport is explained by cancellation of a few low moments.

## 0. Moment criterion versus usable proof

E72.93 gives a correct formal criterion:

```text
<r_s^even,phi> = M_phi(conjugate(s)).
```

For fixed finite band, vanishing of the Cauchy transform is equivalent to Stieltjes residue/moment
cancellation.

The tempting proof route is:

```text
the first few moments of phi are already small,
```

which would explain Cauchy invisibility by low-order cancellation.

## 1. Probe

The companion script:

```text
E72_93_moment_probe.py
```

computes normalized moment coherences:

```text
coh_m(phi)
 = |sum_{|d|<=H} phi_n d_n^{2m}|
   / sum_{|d|<=H}|phi_n| |d_n|^{2m}.
```

Small values indicate real cancellation; values near `1` indicate coherent, non-cancelled moments.

## 2. Result

Representative values:

```text
lambda=12:
  tau=0.825  coh0=1.08e-01  coh1=9.23e-01  coh2=9.58e-01  coh3=9.77e-01
  tau=2.135  coh0=2.24e-01  coh1=9.01e-01  coh2=9.80e-01  coh3=9.90e-01

lambda=20:
  tau=0.241  coh0=8.00e-01  coh1=9.91e-01  coh2=1.00e+00  coh3=1.00e+00
  tau=1.856  coh0=8.12e-02  coh1=8.66e-01  coh2=9.96e-01  coh3=1.00e+00

lambda=24:
  tau=1.522  coh0=4.64e-01  coh1=6.83e-01  coh2=6.19e-01  coh3=5.00e-01
  tau=9.167  coh0=1.62e-01  coh1=8.20e-02  coh2=2.38e-01  coh3=3.26e-01
```

There is not enough low-moment cancellation to close `(FBRT)` by a finite list of small moments.

## 3. Consequence

The moment criterion is mathematically correct, but the low-moment shortcut is not the mechanism.
The Cauchy invisibility, if true, must use the full root-specific kernel:

```text
Z_x(tau_j)
 = iS_tau_j k_x
   -(exp(i tau_jL)-1)L^(-1)M_k(tau_j)S_tau_j1,
```

and the finite Weyl-root condition:

```text
M_xi(tau_j)=0.
```

The next target is therefore not generic moment decay. It is a root-specific cofactor identity:

```text
B_xC_E^(-1)B_x^*P_HZ_x(tau_j)
```

must be Cauchy-invisible because `tau_j` is a finite Weyl root, not because its first few moments are
small.

## 4. Status

```text
rejected: low-moment cancellation as the proof mechanism;
kept:     exact Stieltjes criterion from E72.93;
next:     derive the root-specific cofactor identity for Z_x(tau_j).
```
