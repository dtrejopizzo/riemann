# E73.125 - CSV Displacement Identity Attempt

Date: 2026-07-12.

Status after E73.126:

```text
DEGRADED TO NO-GO / TAUTOLOGY.
```

The displacement-image idea below is useful as a record of the attempted
mechanism, but it cannot be the proof of CSV.

E73.122 isolated the needed asymptotic input:

```text
CSV: |C_x(-gamma)| <= C L^-17.
```

E73.124 shows that CSV is not geometric: the arch/free vector fails it by
about fifteen powers of `L`.  Therefore CSV must come from the arithmetic
cell equation.

## 1. The exact source of cancellation

Let

```text
C_E xi = mu xi
```

be the zeta-coupled finite CCM ground equation, and let

```text
k_gamma(d_n)=1/(-gamma-d_n).
```

Then

```text
C_x(-gamma)=<xi,k_gamma>.
```

The attempted mechanism was: if one can prove a finite displacement
decomposition

```text
k_gamma = (C_E-mu I)Y_gamma + R_gamma,                 (CSV-DISP)
```

then

```text
<xi,k_gamma>
 =
 <xi,(C_E-mu I)Y_gamma> + <xi,R_gamma>
 =
 <xi,R_gamma>.
```

then the range term vanishes against `xi`.  However E73.126 shows this is
precisely the problem: the scalar channel is invariant under adding any
range term,

```text
<xi,k_gamma-(C_E-mu I)Y_gamma> = <xi,k_gamma>.
```

Thus CSV does not follow from finding such a decomposition unless the
residual bound is independently equivalent to CSV.  The displacement
projection is scalar-invisible and therefore tautological for this target.

The attempted residual bound would have been:

```text
|<xi,R_gamma>| <= C L^-17.
```

But by the identity above this is the same number as the original CSV
quantity.  It does not explain it.

## 2. Why this is non-circular

`CSV-DISP` is a finite identity in the explicit CCM matrix:

```text
C_E = W02 - WR - Prime.
```

It uses no zeros of `Xi` as input.  The critical ordinates `gamma` enter as
test heights, not as roots of the finite Cauchy function.  The proof is a
finite rational/Loewner displacement computation.

The cancellation comes from the eigen-equation of the zeta-coupled vector,
not from assuming positivity or RH.

## 3. Source class

E73.017 already identified the correct source class:

```text
Y(d)=DD_gamma(d)/(d^2+beta^2)^r,
r=0,1,2,
```

plus endpoint residuals absorbed by Phase 72.

For CSV, the required source class is narrower.  Since

```text
k_gamma(d)=1/(-gamma-d),
```

one should allow rational generators

```text
Y_gamma(d)
 in span{
   1/(d+gamma),
   d/(d^2+gamma^2),
   1/(d^2+gamma^2),
   DD_gamma(d)/(d^2+gamma^2)^r, r=0,1,2
}
```

and endpoint modes already present in `R_72`.

## 4. Correct replacement target

CSV should instead be formulated as a finite characteristic interpolation
statement.  Define

```text
Phi_N(s) = (2/sqrt(L)) sin(sL/2) C_x(s).
```

Then

```text
CSV at s=-gamma
<=> |Phi_N(-gamma)| <= (2/sqrt(L)) |sin(gamma L/2)| C L^-17.
```

So the next viable theorem is:

```text
Characteristic Small-Value Theorem:
the finite CCM characteristic function Phi_N is small at the critical
ordinates in the natural-height local window, with the CSV_17 rate.
```

This connects back to E71.6/E71.12, but in a weaker and more local form:
not global locally-uniform convergence to `Xi`, only quantitative
interpolation at the critical ordinates used by the Phase 73 gate.

## 5. Lesson from the failed test

Do not use range projection through `(C_E-mu I)` to prove a scalar
orthogonality against `xi`.  It cannot change that scalar by self-adjointness.

The CSV proof must attack `<xi,k_gamma>` directly, or prove finite
characteristic interpolation for `Phi_N`.
