# E72.105 -- Post-main HPAC gauge correction

**Date:** 2026-07-09.
**Role:** correct the final HPAC target after the model-background audits E72.101--E72.104.

## 0. Conflict exposed by the last audits

E72.98 reduced the half-power Abel certificate to two explicit finite defects:

```text
D1_x(H,s),        D2_x(H,s;tau_j).
```

This theorem is correct as a sufficient endpoint theorem.  But E72.101--E72.104 show that its second
assumption is stronger than the scalar WRL problem actually asks for.

The evidence is structural:

```text
D2_actual(tau_j) is already present in the prolate/model background,
D2_model(tau_j) is of the same size as D2_actual(tau_j),
root matching does not remove it,
unweighted and derivative-weighted root-current subtractions do not remove it.
```

This is not a numerical accident.  E72.31, E72.59, E72.61 and E72.62 all say that the scalar WRL
problem is a **post-main Chebyshev-discrepancy** problem:

```text
dE(u)=dPsi(u)-du,
```

whereas E72.68--E72.98 built the finite HPAC certificate for the absolute Abel cell:

```text
F_x(s;tau)=<v_{x,s},A_x(tau)k_x>.
```

Thus E72.98 asks the absolute cell to vanish at the finite Weyl roots.  The scalar WRL route only needs
the post-main cell to vanish.

## 1. What remains valid

The following implication remains valid:

```text
absolute D1 -> 0 and absolute D2 -> 0
    => HPAC divisibility
    => scalar WRL resonance annihilation.
```

So E72.98 is a valid sufficient theorem.

The new point is that the converse is not expected.  Absolute root vanishing contains a model/PNT
background which scalar WRL subtracts before the arithmetic resonance is tested.  Therefore proving
absolute `D2 -> 0` is likely an over-strong route.

## 2. Correct post-main object

Let:

```text
L=log x,       y=log u,       rho=1/2+i tau,
v_{x,s}=C_x^(-1)Q_x(sI-D_x)^(-1)1_x.
```

The half-power absolute HPAC concomitant is:

```text
F_x^{abs}(s;tau)
 = L_x(s;1)+(1/2+i tau)int_0^L exp(i tau y)<v_{x,s},Q_x(y)k_x>dy.
```

The scalar WRL formula E72.31 instead uses:

```text
WRL_x(s)
 = -int_{1^-}^x L_x(s;u)dE(u)+err_x(s),
E(u)=Psi(u)-u.
```

Therefore the finite concomitant that must enter the divisor ideal is not the absolute `F_x^{abs}` but
the post-main Abel-Stieltjes concomitant:

```text
F_x^{pm}(s;tau)
 := L_x(s;1)E(1^-)
    + int_{1^-}^x u^(1/2+i tau)d_u L_x(s;u) dE_ab(u),
```

where `dE_ab` denotes the endpoint Abel-Stieltjes error measure after the model main is removed.  In
the reflected endpoint coordinate `r=L-log u`, this is equivalently the Loewner-discrepancy matrix
of E72.62:

```text
K_x^E(z)
 := int_0^L exp(-(z-1/2)r)Lo_r dE_x^leftarrow(r),
```

paired against:

```text
<v_{x,s},K_x^E(z)k_x>.
```

This is the post-main HPAC gauge.

## 3. Why root-current subtraction failed

E72.103 and E72.104 subtracted model and actual quantities after root evaluation:

```text
sum_{actual roots} D2_actual - sum_{model roots} D2_model,
sum_{actual roots} D2_actual/M'_actual - sum_{model roots} D2_model/M'_model.
```

This is too late.  Root evaluation and Feshbach shorting are nonlinear in the background data:

```text
c(tau)=B_x^*P_HZ_x(tau),
D2(tau)=-det[[C_E,c(tau)],[a^*,0]]/det(C_E).
```

The PNT main must be removed at the operator/concomitant level, before:

```text
projection to the finite band,
shorting through C_E^(-1),
evaluation at finite Weyl roots,
optional residue weighting.
```

Thus the correct finite column is not:

```text
c_actual(tau)-c_model(tau)
```

after two separately formed root problems.  It must be:

```text
c_pm(tau)=B_x^*P_H Z_x^{pm}(tau),
```

with `Z_x^{pm}` constructed directly from `dE_x^leftarrow=dPsi_x^leftarrow-xe^(-r)dr`.

## 4. Correct finite endpoint theorem

Define the post-main finite-band column:

```text
c_{x,H}^{pm}(tau)
 := B_x^*1_{|d|<=H}Z_x^{pm}(tau),
```

where `Z_x^{pm}(tau)` is the HPAC/Loewner source obtained by replacing the absolute Lebesgue cell
measure in E72.91 by the reflected Chebyshev-discrepancy measure of E72.61--E72.62.

Then define:

```text
D2_x^{pm}(H,s;tau_j)
 := - det [ C_E       c_{x,H}^{pm}(tau_j) ] / det(C_E).
          [ a_x(s)^*  0                    ]
```

### Theorem 72.105 -- Post-main finite endpoint criterion

Assume:

```text
(A) the Cauchy-channel tail D1_x(H,s) vanishes as in E72.98;

(B_pm) for every compact s-window K, finite root-height window T, and fixed H,
       lim_{x->infty} sup_{s in K, tau_j<=T}|D2_x^{pm}(H,s;tau_j)|=0;

(Q_pm) the corresponding quotient by P_x(tau) is locally normal after one s-derivative.
```

Then scalar WRL resonance annihilation holds:

```text
x^rho L_x(s;x)-int_1^x u^rho partial_uL_x(s;u)du -> 0
```

for the scalar Weyl-Feshbach kernel.

### Proof

The proof is the E72.98 proof with one change: every absolute HPAC column is replaced before shorting
by the post-main column constructed from `dE_x^leftarrow`.

1. E72.31 reduces WRL to the Abel-Chebyshev discrepancy with measure `dE=dPsi-du`.

2. E72.61 reflects this discrepancy exactly to the endpoint Loewner-Stieltjes matrix `K_x^E`.

3. E72.62 rewrites `K_x^E` as the finite integrated commutator:

```text
[D,K_x^E(z)]=[Sigma_x^E(z),J].
```

4. The same Feshbach shorting used in E72.91--E72.97 applies to the resulting post-main source
`Z_x^{pm}(tau)`, giving the bordered determinant `D2_x^{pm}`.

5. `(A)` removes the high physical Cauchy tail.  `(B_pm)` removes the finite-band root residual.
`(Q_pm)` promotes finite-root vanishing to local HPAC divisibility in the post-main gauge.

6. E72.68 then applies to the post-main scalar cell, which is exactly the scalar WRL resonance after
the model-main matching of E72.31. `QED`

## 5. New exact remaining identity

The endpoint theorem to prove is therefore not the absolute FBRT of E72.98, but:

```text
Post-main finite-band root transport:
for fixed H and finite root-height windows,
max_{tau_j<=T} |<r_s^even,B_xC_E^(-1)c_{x,H}^{pm}(tau_j)>| -> 0.
```

Equivalently:

```text
max_{tau_j<=T}
|det[[C_E,c_{x,H}^{pm}(tau_j)],[a_x(s)^*,0]]|/|det(C_E)| -> 0.
```

Using E72.62, this can be written without hidden background terms as:

```text
<v_{x,s},K_x^E(z)k_x>
 = sum_n alpha_n(v,k)sigma_n^E(z)
   + sum_n beta_n(v,k)partial_{d_n}sigma_n^E(z),
```

where:

```text
sigma_n^E(z)=int_0^L exp(-(z-1/2)r)sin(d_nr)dE_x^leftarrow(r).
```

Thus the corrected missing theorem is an integrated Loewner-Feshbach discrepancy cancellation, not
pointwise absolute root annihilation.

## 6. Status

```text
corrected: absolute D2 is a sufficient but over-strong endpoint;
explained: E72.101--E72.104 fail because the background was subtracted after root evaluation;
new target: construct Z_x^{pm}(tau) from dE_x^leftarrow before shorting;
open: prove post-main finite-band root transport from the integrated Loewner commutator.
```
