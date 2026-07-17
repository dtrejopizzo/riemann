# E72.135 -- Sharp finite route to scalar WRL

**Date:** 2026-07-09.
**Role:** package the current minimal endpoint after the mass-gate compression.

## 0. Finite estimates

For fixed physical band `H`, compact Cauchy window `K`, and finite root-height window `T`, define:

```text
CGE-K:
  the Cauchy graph-energy tail vanishes as H->infty,

ROP:
  sup_{tau_j<=T} ||R_xY_x(tau_j)|| = O(1),

MCOER:
  C_model >= a_H L I,

RCOER:
  C_actual >= theta_H C_model,

MSB:
  sup_{tau_j<=T} ||b_{x,H}||||c_{x,H}^{pm}(tau_j)|| = O(1).
```

All five are finite statements.  No limiting zero and no Ω7 positivity is inserted.

## 1. Theorem 72.135

Assume `CGE-K`, `ROP`, `MCOER`, `RCOER`, and `MSB`.  Then scalar WRL resonance annihilation holds:

```text
x^rho L_x(s;x) - int_1^x u^rho partial_u L_x(s;u)du -> 0
```

for the scalar Weyl-Feshbach kernel, uniformly on the two Cauchy heights in `K`.

### Proof

By `MCOER` and `RCOER`:

```text
C_actual >= theta_H a_H L I.
```

This is `COER`.  By E72.132, `COER + MSB` imply the mass gain:

```text
MG:
sup_{tau_j<=T}|b_{x,H}^*C_actual^(-1)c_{x,H}^{pm}(tau_j)| -> 0.
```

By E72.127, `ROP + MG` imply post-main finite-band root transport, because the centered flux term
vanishes after the mesh summation-by-parts gain:

```text
h||Psi||_1 <= C_HL^(-1/2)||R_xY_x||_2 -> 0.
```

Finally, `CGE-K` removes the Cauchy-channel physical tail by E72.120 and E72.127.  Therefore scalar
WRL resonance annihilation follows. `QED`

## 2. What remains

The proof burden is now exactly:

```text
MCOER: model complement coercivity,
RCOER: relative actual/model coercivity,
MSB:   bounded post-main source product,
ROP:   bounded shorted flux,
CGE-K: Cauchy graph-energy tail.
```

The numerical status is:

```text
CGE-K: supported by E72.120/E72.121,
ROP:   supported by E72.112/E72.118,
MSB:   supported by E72.132,
MCOER: supported by E72.133/E72.134,
RCOER: supported by E72.134.
```

## 3. Status

```text
proved: the five finite estimates imply scalar WRL annihilation;
open:   prove the five estimates directly from the finite CCM construction.
```
