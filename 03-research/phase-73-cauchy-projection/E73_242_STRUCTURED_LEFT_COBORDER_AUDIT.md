# E73.242 - Structured left-coborder audit for the transverse residual

Date: 2026-07-14.

## 1. Purpose

E73.241 identifies the valid `CURV-COB` target:

```text
rho_a=q_aH_L(I-P_w)
```

must be represented as a structured left-coborder

```text
rho_a = Y_{a,w}^*E + endpoint residual,
E=H_L-mu_L I,
```

where `Y_{a,w}` belongs to a fixed symbolic primitive module.

This note tests the smallest natural module and compares it to the forbidden
ambient rowspace baseline.

## 2. Primitive module tested

Let

```text
q_1=q_w,       q_2=q_-w,       D=diag(d_n).
```

The first symbolic left primitive module is:

```text
P_deg(r)=span{ D^k q_j^* : j=1,2, 0<=k<=r }.
```

This module is fixed by the Cauchy plane and the pole mesh.  It does not use
`xi`, `h=Qxi`, the final scalar center, or a pseudoinverse of `E`.

For each row `rho_a`, compute the best least-squares representation inside
this fixed module:

```text
rho_a approx Y^*E,       Y in P_deg(r).
```

The residual is measured both in row norm and in scalar pairing against
`xi_L`.

## 3. Forbidden baseline

For calibration only, compare with the full ambient rowspace solution.  Since

```text
Row(E)=xi_L^perp,
```

the full pseudoinverse can make the residual norm essentially equal to the
null component.  This is not proof-facing; it is only a scale baseline.

## 4. Result

The small symbolic module does not reproduce the transverse residual.  Its
residual pairing remains at essentially the full center scale.  The forbidden
ambient baseline, by contrast, removes everything except the scalar
obstruction by construction.

Thus:

```text
P_deg(r) with small r is too small;
ambient rowspace is tautological;
CURV-COB requires a richer symbolic primitive module.
```

## 5. Consequence

The next primitive module must include the finite Loewner/divided-difference
structure of `H_L`, not only polynomial multiples of the Cauchy rows.  The
natural enlargement is:

```text
P_rat(r,s)=span{ D^k q_j^*/(D^2+beta^2)^m,
                 D^k q_j^* : 0<=k<=r, 1<=m<=s, j=1,2 },
```

with beta parameters fixed by the Cauchy/endpoint geometry, not chosen from
the final residual.

## 6. Status

```text
tested:  polynomial Cauchy primitive module P_deg(r);
failed:  small r does not give CURV-COB;
guarded: full pseudoinverse baseline is tautological;
next:    test rational Loewner primitive modules with fixed denominators.
```

