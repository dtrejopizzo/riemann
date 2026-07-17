# E73.219 - Scalar TRANS-CELL radius budget

Date: 2026-07-14.

## 1. Purpose

E73.217 gives a certified eigenline ball and E73.218 shows that the Cauchy
projection does not enlarge it:

```text
eta_w=(I-P_w)xi,          rho_eta <= rho_xi.
```

This note propagates that ball through the final scalar functional

```text
C_a(eta)=q_a H eta,
H=H_model-Prime.
```

By E73.199 this scalar is the same object as the finite-frequency certificate

```text
A_L^digamma[B_a]-P_L[B_a].
```

## 2. Radius formula

Let `[H]` be an operator ball around `H_0`:

```text
||H-H_0|| <= epsH,
```

and let `[eta]` be a vector ball around `eta_0`:

```text
||eta-eta_0|| <= rho_eta.
```

Then for each Cauchy row `q_a`,

```text
C_a(eta)-q_aH_0eta_0
=q_aH_0(eta-eta_0)+q_a(H-H_0)eta_0+q_a(H-H_0)(eta-eta_0).
```

Thus a sufficient scalar radius is

```text
rad(C_a)
<= ||q_aH_0|| rho_eta
 + ||q_a|| epsH ||eta_0||
 + ||q_a|| epsH rho_eta.                         (1)
```

The first term is the eigenline/projection uncertainty.  The second term is
matrix-entry uncertainty.  The third is the mixed ball term.

## 3. Inputs

The script consumes the certified exponents from E73.217:

```text
epsH = dim * max_entry_radius,
rho_eta = rho_xi.
```

The displayed centers use the legacy matrix centers, which E73.206 already
audited against the closed high-precision entries.  This is a radius-budget
diagnostic; a final proof certificate should evaluate the center by outward
rounded closed entries as in E73.202.

## 4. Result

In the tested windows the total radius is much smaller than the scalar center:

```text
rad(C_a)/|center| <= 1.5e-15
```

even under the inflated Bernoulli-sector budget `C_sec=10^6`, and is far
smaller under `C_sec=1`.

Therefore the interval propagation chain does not fail at the last scalar
linearization step.  The remaining finite proof-facing work is not a radius
loss; it is to replace the diagnostic center by a fully outward-rounded
closed-center evaluation.

## 5. Status

```text
proved: scalar radius formula (1);
verified: certified radii are negligible relative to tested scalar centers;
open: outward-rounded closed-center interval for C_a itself;
open: uniform analytic production of TRANS-CELL bounds.
```

## 6. Prior-audit distinction

E73.203 already identified the linear sensitivity

```text
eta -> q_a H eta.
```

That route failed because it fed the sensitivity with a double-precision
Davis-Kahan eigenline radius:

```text
rho_xi = 2 eps_eig/gap = O(L^1).
```

E73.219 is not a repeat of that failed certificate.  It keeps the same correct
linear functional, but replaces the eigenline input by the certified bordered
Krawczyk radius from E73.217 and adds the missing matrix-entry terms involving
`epsH`.  The result is the opposite regime:

```text
rho_eta = L^(-41) ... L^(-56),
rad(C_a)/|center| << 1.
```
