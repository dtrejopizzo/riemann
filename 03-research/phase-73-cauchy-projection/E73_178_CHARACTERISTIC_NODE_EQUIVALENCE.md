# E73.178 - Characteristic node equivalence

Date: 2026-07-14.

## 1. Purpose

E73.177 reduced the current Phase 73 endpoint to the nodal statement

```text
SDI-node:
G_L(i gamma_j)
= (1-exp(i gamma_j L)) sum_m xi_L(m)/(-gamma_j-d_m)
= O(L^B exp(-alpha L))
```

for each fixed critical zero `gamma_j`.

This note identifies that Cauchy numerator with the finite CCM characteristic function already
isolated in E71.6.  The point is not to introduce a new mechanism.  It is to locate the remaining
theorem exactly inside stable divisor identification.

## 2. Finite characteristic numerator

For the same finite vector `xi_L` and spectral mesh `d_m=2*pi*m/L`, define

```text
f_L(s) = sum_m xi_L(m)/(s-d_m),
Phi_L(s) = (2/sqrt(L)) sin(sL/2) f_L(s).
```

The sine factor is the canonical pole-killer for the mesh.  Thus `Phi_L` is the raw finite entire
characteristic numerator of E71.6, before any Fredholm/de Branges normalization.

## 3. Exact identity

For every real `gamma` with the denominators defined,

```text
G_L(i gamma) = i sqrt(L) exp(i gamma L/2) Phi_L(-gamma).      (1)
```

Indeed,

```text
Phi_L(-gamma)
= (2/sqrt(L)) sin(-gamma L/2) sum_m xi_L(m)/(-gamma-d_m)
= -(2/sqrt(L)) sin(gamma L/2) sum_m xi_L(m)/(-gamma-d_m),
```

while

```text
1-exp(i gamma L)
= -2i exp(i gamma L/2) sin(gamma L/2).
```

Multiplying the first displayed line by `i sqrt(L) exp(i gamma L/2)` gives exactly the second
factor times the same Cauchy sum.  This proves (1).

Consequently,

```text
|G_L(i gamma)| = sqrt(L) |Phi_L(-gamma)|.                    (2)
```

## 4. Reformulated endpoint

`SDI-node` is equivalent to

```text
CHAR-node:
|Phi_L(-gamma_j)| <= L^(B-1/2) exp(-alpha L)
```

for the same fixed set of critical zeros.

Thus the Phase 73 endpoint is not a hidden quotient estimate anymore.  It is the local nodal
vanishing of the finite characteristic numerator at the true zeros of `Xi`.

## 5. Relation to E71.6

E71.6 already warned that the raw scalar normalization of `Phi_L` does not give a visible global
least-squares convergence to `Xi`.  Therefore E73.178 does **not** claim that raw `Phi_L` closes the
Hurwitz theorem.

The precise statement is:

```text
If a canonical normalization c_L Phi_L is polynomially bounded above and below
and converges to Xi locally uniformly with error O(L^B exp(-alpha L)) at the
fixed zeros gamma_j, then SDI-node follows.
```

Conversely, `SDI-node` for all zeros in compact windows is the nodal shadow of stable divisor
identification.  It is weaker than full local uniform convergence, but it is exactly the amount of
stable divisor information needed by the current scalar WRL route.

## 6. Audit against earlier phases

This does not re-use the old Sonin/prolate positivity route as a new theorem.  The inherited pieces
are:

```text
E71.6: Phi_L is the natural pole-killed finite CCM characteristic numerator.
E73.125--E73.129: characteristic CSV was already identified as the correct replacement for
                  the failed displacement-source proof.
E72.317--E72.318: transformed Cauchy packets give the same divided-difference row.
E72.319 / E73.175: boundary values identify Cauchy numerators with endpoint traces.
```

The new content here is only the exact node identity (1) after the quotient collapse of
E73.170--E73.177.  It turns the surviving `QG` theorem into the same characteristic nodal
convergence target, now with the complete chain from `CHAR-node` back to scalar WRL.

## 7. Status

```text
proved:   G_L(i gamma)=i sqrt(L) exp(i gamma L/2) Phi_L(-gamma);
proved:   SDI-node is equivalent to CHAR-node;
reduced:  the Phase 73 endpoint to finite characteristic nodal vanishing;
open:     prove the canonical normalized characteristic convergence/stable divisor theorem.
```
