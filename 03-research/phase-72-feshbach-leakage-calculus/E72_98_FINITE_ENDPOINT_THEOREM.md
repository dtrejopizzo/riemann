# E72.98 -- Finite endpoint theorem

**Date:** 2026-07-09.
**Role:** state the final finite reduction obtained in Phase 72.

## 0. Finite data

For each finite CCM window `x`, choose:

```text
D_x, k_x, xi_x, C_E, B_x,
finite Weyl roots Tau_x={tau_j},
physical cutoff H.
```

For a compact `s`-window `K`, define:

```text
a_x(s)=B_x^*r_s^even,
K_H=B_x^*1_{|d|>H}B_x,
c_{x,H}(tau_j)=B_x^*1_{|d|<=H}Z_x(tau_j),
```

with:

```text
Z_x(tau)
 := iS_tau k_x
    -(exp(i tau L)-1)L^(-1)M_k(tau)S_tau1.
```

## 1. The two finite defects

Define:

```text
D1_x(H,s)
 := a_x(s)^*C_E^(-1)K_HC_E^(-1)a_x(s)
    / a_x(s)^*C_E^(-2)a_x(s),                                (D1)
```

and:

```text
D2_x(H,s;tau_j)
 := - det [ C_E       c_{x,H}(tau_j) ] / det(C_E).            (D2)
          [ a_x(s)^*  0                ]
```

Both are finite matrix expressions. `D1` is the physical Cauchy-channel tail. `D2` is the finite-band
root-specific Stieltjes defect.

## 2. Endpoint theorem

Assume:

```text
(A) CCGD:
    for every compact K,
    lim_{H->infty} limsup_{x->infty} sup_{s in K} D1_x(H,s)=0;

(B) FBRT:
    for every compact K, finite root-height window T, and fixed H,
    lim_{x->infty} sup_{s in K, tau_j<=T} |D2_x(H,s;tau_j)|=0.
```

Then scalar WRL resonance annihilation holds:

```text
x^rho L_x(s;x) - int_1^x u^rho partial_u L_x(s;u)du -> 0
```

for the scalar Weyl-Feshbach kernel of Phase 72. Consequently HPAC spectral divisibility holds in the
finite-root sense, hence the Phase 72 route closes the Ω7 terminal positivity criterion.

## 3. Proof chain

1. E72.68 reduces scalar WRL resonance annihilation to HPAC spectral divisibility.

2. E72.69--E72.74 reduce HPAC divisibility to the even finite-root certificate.

3. E72.75--E72.81 identify that certificate as the dual cofactor root transport residual.

4. E72.84--E72.88 show that `(A)` reduces the full cofactor residual to the finite physical band.

5. E72.91 identifies the finite-band residual as:

```text
<r_s^even,B_xC_E^(-1)c_{x,H}(tau_j)>.
```

6. E72.97 rewrites this residual exactly as the bordered determinant ratio `(D2)`.

7. Therefore `(A)+(B)` imply the finite-root HPAC residual vanishes. E72.68 then gives scalar WRL
annihilation. `QED`

## 4. What is closed and what is not

Closed:

```text
the route has been reduced to the two finite expressions D1 and D2;
both expressions are explicit and numerically verifiable from finite CCM data;
all earlier hidden inverses have been exposed as quadratic forms or bordered determinants.
```

Not closed:

```text
the asymptotic vanishing assumptions (A) and (B) are not proved here.
```

Thus this is a finite endpoint theorem, not a proof of RH.

## 5. Status

```text
achieved: finite explicit reduction of Phase 72;
open:     prove (A) and (B), or find the arithmetic source of their vanishing.
```
