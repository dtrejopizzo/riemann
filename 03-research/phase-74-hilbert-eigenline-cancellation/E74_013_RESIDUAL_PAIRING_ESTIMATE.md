# E74.13 - Residual pairing estimate target

Date: 2026-07-16.

## Purpose

E74.12 names the quotient-lift residual.  This note states the scalar estimate
that remains and records why the existing probes do not yet prove it.

## Target

For

```text
R^Q_{a,w,L} in QLIFT_L,
```

prove:

```text
QLIFT-DIV:
R^Q_{a,w,L}xi_L=O_M(L^(-M))
```

uniformly in the admissible natural-height rows and windows.

In cauchy0 coordinates this has the form:

```text
e^(alpha L)
| sum_{gamma in K_L} z_{a,w,L}(gamma)
  (1-exp(i gamma L)) sum_n xi_L(n)/(-gamma-d_n) |
<= L^B,
```

where `z_{a,w,L}` is the quotient-lift coefficient vector, not the raw
canonical `delta_A` from E73.164.

## Allowed proof source

The only admissible proof must use all of the following coupled data:

```text
1. the finite eigenline equation (H_L-mu_LI)xi_L=0;
2. the cell identity Q_y and Q_wR_wxi_L=0;
3. the Gamma-prime functional F_L without splitting into absolute
   archimedean and prime ceilings;
4. the explicit quotient-lift coordinates from E74.12.
```

## What current probes prove

E74.8 and E74.14 show a strong discriminator:

```text
eta=(I-P_w)xi_L cancels to about L^-18 ... L^-22,
generic ker(Q_w) vectors do not,
random replacement symbols do not.
```

This proves the cancellation is eigenline-specific and symbol-specific.  It
does not prove `QLIFT-DIV`, because the quotient-lift coefficients are not yet
available in closed algebraic form.

## What is still missing

The remaining proof obligation is:

```text
derive z_{a,w,L} symbolically and prove the signed cauchy0 pairing above.
```

Equivalently, replace the numerical projector in
`E74_011_algebraic_quotient_bridge_probe.py` by a partial-fraction quotient
basis and prove the resulting three scalar coefficient identities.

## Status

```text
not closed: QLIFT-DIV;
supported: eigenline/symbol specificity of the cancellation;
next:      symbolic quotient basis and three-coordinate signed estimate.
```

