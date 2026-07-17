# E73.225 - Weight radius budget

Date: 2026-07-14.

## 1. Purpose

E73.224 showed that the centers of the weights `W_omega,V_omega` do not
amplify coefficient balls dangerously.  This note audits the radii of the
weights themselves.

## 2. Weight radius model

For the unit modes

```text
e^(iomega y),          y e^(iomega y),
```

the weight radius is bounded by:

```text
rad(W_omega) <= R_finite(W_omega)
              + C_sec R_psi(D_1(R,omega))
              + R_exp(W_omega),

rad(V_omega) <= R_finite(V_omega)
              + C_sec R_psi(D_2(R,omega))
              + R_exp(V_omega).
```

Here:

```text
R_finite = heuristic outward rounding budget from E73.211 style accounting,
R_psi    = Bernoulli remainder from E73.210,
C_sec    = sector-constant inflation from E73.216,
R_exp    = exponentially small endpoint tail.
```

The proof-facing formal version replaces `R_finite` by native outward complex
balls, exactly as E73.215 did for matrix entries.

## 3. Scalar contribution

The weight-radius part of E73.222 is:

```text
R_weight =
sum_omega |c_omega| rad(W_omega)
+sum_omega |l_omega| rad(V_omega).
```

E73.225 computes this quantity using the actual coefficient centers.

## 4. Result

With `C_sec=1`, the total weight-radius contribution is around:

```text
L^-75 ... L^-86.
```

With the inflated `C_sec=10^6`, it is still only around:

```text
L^-67 ... L^-77.
```

Relative to the conservative coefficient l1 scale, the inflated ratio is about:

```text
4.5e-47.
```

Thus weight-radius uncertainty is far below both the coefficient-radius
contribution and the E73.219 scalar radius budget.

## 5. Status

```text
verified: weight radii are negligible in tested windows;
conditional: finite-rounding part still uses E73.211-style heuristic accounting;
next: package the finite local TRANS-CELL certificate and list the exact
      formal outward replacements still required.
```
