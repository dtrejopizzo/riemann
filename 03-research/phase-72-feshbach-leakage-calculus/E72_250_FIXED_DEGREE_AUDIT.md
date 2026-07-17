# E72.250 - Fixed-degree audit

## Purpose

This note reconciles E72.179 and E72.195 after the external audit.

## Finding

There are two different fixed-degree issues:

```text
SRP approximation error:
  fixed Chebyshev degree gives fixed operator error eps_D;
  HS error contains sqrt(dim) eps_D.

LM8 trace envelope:
  fixed degree is acceptable only if P(0)=P'(0)=0;
  otherwise dim P(0) drifts.
```

## SRP/XNEG

E72.179 is still the correct statement for polynomial approximation to the signed residual:

```text
sqrt(d_x)(eps_0(D_x)+eps_1(D_x)) <= m_x.
```

Thus a fixed signed-residual polynomial cannot be a uniform theorem merely because it passes the tested
range. It needs either:

```text
1. adaptive degree D_x;
2. an exact identity with no approximation error;
3. an effective-rank/Schatten replacement for sqrt(d_x).
```

The fixed XNEG-32 evidence remains useful, but it should be read as a diagnostic unless the mixed term
is no longer tied to a fixed approximation error.

## LM8

E72.247 shows the original LM8 majorants fail the dimensional-drift audit because:

```text
P_j(0)>0.
```

E72.248--E72.249 show the corrected route:

```text
P_j(u)=u^2R_j(u).
```

This removes both constant and linear drift:

```text
P_j(0)=P_j'(0)=0.
```

The homogeneous LM8 probe passes:

```text
lambda>=16:  P degree 10;
lambda=12:   P degree 12 finite exception.
```

## Corrected Stable Certificate

Replace the statement:

```text
NTC-8 + LM8-ASRP + XNEG-32
```

by the proof-facing version:

```text
NTC-8
+ homogeneous LM8
+ mixed gate with either adaptive degree or exact low-dimensional/tail mechanism.
```

The old E72.195 fixed certificate remains a useful stress diagnostic, but not the final uniform
theorem statement.

## Action Item

Future documents should avoid saying that E72.195 alone gives a fixed uniform target. The corrected
uniform target must explicitly include:

```text
no constant drift in majorants,
no fixed nonzero approximation error multiplied by sqrt(dim).
```
