# E74.21 - Cauchy-jet no-go and critical numerator endpoint

Date: 2026-07-16.

## Bootstrap test

The proposed `BOOT-CELL(r)` mechanism would be credible if the critical
Cauchy transform were small together with a controlled hierarchy of
confluent derivatives.  Define normalized jet rows

```text
q_{gamma,r}^{+-}(d)=(i(d-gamma))^(-r), (i(d+gamma))^(-r),
r=1,...,5.
```

`E74_021_cauchy_jet_bootstrap_probe.py` pairs these rows with the CCM
ground eigenline.

## Result

The cancellation is isolated at the first resolvent value:

```text
r=1: L-exponents about -19 to -23,
r=2,...,5: typically L-exponents between 0 and -4.
```

Thus the Cauchy transform is not small in a confluent neighborhood of the
critical node.  The first-order value is a nodal/divisor phenomenon.

This agrees with E72.316: ordinary residue regularity cannot produce the
required Cauchy cancellation.  It also agrees with E72.364: the mechanism is
specific to the actual divisor eigenline and is not a universal invariant-line
property.

## Exact numerator formulation

Let

```text
D_L(z)=prod_n (z-d_n),
C_L(z)=sum_n xi_n/(z-d_n)=P_L(z)/D_L(z),
P_L(z)=sum_n xi_n prod_{m != n}(z-d_m).
```

Up to fixed factors of `i`, `Q_gamma xi` consists of `C_L(gamma)` and
`C_L(-gamma)`.  Hence

```text
CAUCHY-EIG-LOC
<=>
CRIT-NUM-DIV:
P_L(+-gamma)=O_M(L^(-M)) D_L(+-gamma)
```

for the admissible critical nodes.

This is the nodal restriction of the Phase 72 `PW-Cauchy/NUM-GROW` wall.  It
is weaker than a whole shifted-strip estimate, but it is still a divisor
theorem for the finite CCM numerator and cannot follow from generic
regularity.

## Correct next target

The remaining theorem should be attacked as an interpolation identity:

```text
CCM-CRIT-INTERP:
the normalized finite numerator P_L converges to, or is divisible to all
orders by, the critical Xi divisor on each fixed natural-height window.
```

The proof must come from the explicit Gamma-prime/prime-power eigenvector
equation.  Using prior convergence to `Xi` without a certified rate would be
circular.

## Status

```text
rejected: BOOT-CELL(r) based on neighborhood/confluent regularity;
identified: cancellation is nodal at the critical divisor;
reduced: CAUCHY-EIG-LOC to CRIT-NUM-DIV / CCM-CRIT-INTERP;
open: prove the finite numerator interpolation rate from the CCM equation.
```

