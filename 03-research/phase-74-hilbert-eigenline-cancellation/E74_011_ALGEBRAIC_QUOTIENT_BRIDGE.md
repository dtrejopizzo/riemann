# E74.11 - Algebraic quotient bridge

Date: 2026-07-16.

## Purpose

E73.277 left three possible moves.  This note implements the first one:

```text
N1. Prove or falsify that the APR principal residual maps to the same
    three-dimensional cauchy0 quotient as QUOT-CRIT-DIV.
```

The probe is `E74_011_algebraic_quotient_bridge_probe.py`.

## Coefficient model

Use the canonical Phase 73 source basis:

```text
cauchy0_gamma(d)=DD_L(-gamma,d),
rat_{gamma,beta,r}(d)=DD_L(-gamma,d)/(d^2+beta^2)^r,
endpoint_{gamma,q}(d)=d^(2q)DD_L(-gamma,d).
```

Let

```text
C_L = span{cauchy0_gamma : gamma in K_L},
M_L = Image((H_L-mu_LI) acting on the finite rational primitive module),
Q_L = C_L/(C_L cap M_L).
```

The APR row is

```text
rho_{a,w}=q_aH_L(I-P_w).
```

The tested bridge is stronger than merely saying that `rho` has a small scalar:
it asks whether the principal coefficient class of `rho` modulo `M_L` is
represented by the canonical cauchy0 quotient.

## Probe metrics

For each row, the probe prints:

```text
fitRel     = row representation error in the canonical source basis
imageRel   = local action image representation error
resB       = size exponent of the principal residual modulo M_L
cauchyRel  = quotient size from the row's raw cauchy0 coefficients
bridgeRel  = residual left after replacing APR by its raw cauchy0 part
quotMiss   = residual missed by the abstract quotient span (I-P_M)C_L
```

Interpretation:

```text
bridgeRel close to 0:
    APR principal residual is directly the raw cauchy0 quotient.

quotMiss close to 0 but bridgeRel large:
    APR residual lies in the same quotient span, but not with its raw
    cauchy0 coefficients.  A new quotient-lift residual is needed.

quotMiss large:
    APR does not reduce to the old cauchy0 quotient in this model.
```

## Result

The direct bridge is falsified in the tested windows:

```text
bridgeRel is usually 0.8--1.1.
```

However, in the better-conditioned windows the abstract quotient miss is much
smaller:

```text
quotMiss is often 0.007--0.20 for lam <= 16.
```

The row representation itself is reliable there:

```text
fitRel and imageRel are typically 1e-7--1e-4 before the larger diagnostic
windows.
```

## Meaning

The bridge does not close in the naive form:

```text
rho mod M_L != raw-cauchy0(rho) mod M_L.
```

But the APR residual is still compatible with the same three-dimensional
quotient:

```text
rho mod M_L belongs numerically to (C_L+M_L)/M_L.
```

Thus the next residual is not the old canonical `delta_A` coefficients.  It is
a quotient-lift residual: the unique cauchy0 representative whose class equals
the APR principal residual modulo `M_L`.

## Status

```text
rejected: direct APR-to-raw-cauchy0 bridge;
supported numerically: APR-to-abstract-cauchy0-quotient bridge in trusted
                     windows;
open: replace the numerical quotient projector by an explicit partial-fraction
      basis for C_L cap M_L and write the exact quotient lift.
```

