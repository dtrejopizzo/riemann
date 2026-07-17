# E72.66 -- Falsifier for endpoint-only spectral divisibility

**Date:** 2026-07-08.
**Role:** prevent a false shortcut after the endpoint reflection identity.

## 0. Tested shortcut

After E72.61--E72.65, the tempting shortcut is:

```text
the endpoint post-main scalar
<v,[S_x^Lambda(rho)-S_x^cont(rho)]k>
```

might itself be divisible by the finite CCM spectral polynomial in the height variable:

```text
rho=1/2+i tau,
P_x(tau)=-det B_x(tau).
```

If true, the endpoint discrepancy would vanish at finite Weyl roots `tau_j`:

```text
<v,[S_x^Lambda(1/2+i tau_j)-S_x^cont(1/2+i tau_j)]k> = 0.
```

## 1. Numerical falsifier

Using the Phase 71 finite CCM harness, with `v=C_x^(-1)Q_x(sI-D_x)^(-1)1`, `s=10+0.2i`,
and `k` the prolate ground vector:

```text
lambda=6, N=18, finite roots:
  tau=1.0162   |D_endpoint|=2.375e-2
  tau=3.4414   |D_endpoint|=4.808e-2
  tau=5.9779   |D_endpoint|=1.421e-2
  tau=8.0360   |D_endpoint|=3.004e-3

lambda=8, N=24:
  tau=0.7284   |D_endpoint|=1.883e-3
  tau=2.7080   |D_endpoint|=2.751e-3
  tau=4.0531   |D_endpoint|=6.357e-3
  tau=5.9877   |D_endpoint|=5.116e-3

lambda=12, N=28:
  tau=0.8248   |D_endpoint|=8.865e-3
  tau=2.1349   |D_endpoint|=2.561e-3
  tau=3.2205   |D_endpoint|=7.930e-5
  tau=8.1177   |D_endpoint|=8.242e-3
```

The endpoint values may be small, but they are not zero at the finite divisor.

## 2. Interpretation

Endpoint reflection is an exact representation of LFDC, but it is not the full scalar WRL resonance.
The spectral divisibility target cannot be:

```text
endpoint post-main discrepancy alone is divisible by P_x.
```

The missing cancellation must involve the full Abel-WRL expression:

```text
x^rho L_x(s;x)-int_1^x u^rho partial_uL_x(s;u)du,
```

or its normalized height form:

```text
widehat M_x(s;tau)=R_x^{WRL}(s;1/2+i tau).
```

This matches E72.36: raw discrete Mellin divisibility failed; now endpoint-only renormalized
divisibility also fails. The viable object is narrower and more structured: the Abel boundary-minus-
bulk concomitant.

## 3. Consequence

E72.61--E72.63 remain useful because they prove that the endpoint LFDC estimate would close the current
route. But the algebraic divisibility proof of scalar WRL resonance annihilation must be built at the
level of the complete Abel kernel `L_x`, not by asking the endpoint piece alone to vanish at finite
Weyl roots.

## 4. Status

```text
falsified: endpoint-only divisibility by P_x;
survives:  endpoint LFDC as an analytic sufficient estimate;
open:      construct divisibility for the full Abel-WRL concomitant widehat M_x(s;tau).
```
