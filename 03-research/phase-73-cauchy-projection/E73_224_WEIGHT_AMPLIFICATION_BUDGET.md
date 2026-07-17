# E73.224 - Weight amplification budget

Date: 2026-07-14.

## 1. Purpose

E73.223 proves that coefficient balls are tiny.  This note checks whether the
closed-center weights

```text
W_omega, V_omega
```

amplify those tiny coefficient radii into a dangerous scalar interval.

## 2. Method

For this audit, weights are not rederived by hand.  They are computed by
definition:

```text
W_omega = (A_L^digamma-P_L)[e^(iomega y)],
V_omega = (A_L^digamma-P_L)[y e^(iomega y)].
```

Then the coefficient-radius contribution to the scalar interval is

```text
R_coeff =
sum_omega |W_omega| rad(c_omega)
+sum_omega |V_omega| rad(l_omega).
```

This is only the coefficient side of the E73.222 radius formula; weight radii
are audited separately.

## 3. Result

The weight magnitudes are modest in the tested windows:

```text
max |W_omega| = L^(-0.43) ... L^(0.09),
max |V_omega| = L^(-1.18) ... L^(0.71).
```

Consequently the coefficient-radius contribution remains tiny.  Even under
the inflated `C_sec=10^6` budget, the worst ratio is about

```text
R_coeff/|center| = 1.6e-14.
```

## 4. Consequence

The coefficient side of the closed-center interval is safe even after
weighting by the exact functional.  The remaining center-side task is now
localized to the radii of the weights themselves:

```text
rad(W_omega), rad(V_omega).
```

Those radii come from elementary exponential integrals, finite prime samples,
and the `psi/psi_1` tail enclosures.

## 5. Status

```text
verified: weight centers do not dangerously amplify coefficient radii;
open: weight-radius budget for W_omega,V_omega.
```
