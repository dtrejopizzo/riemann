# E72.192 -- Low-moment envelope certificate

**Date:** 2026-07-09.
**Role:** certify that the degree-8 envelopes from E72.191 majorize the split energy on the full
interval, not just the LP grid.

## 0. Certified inequalities

For `j=0,1`, the degree-8 polynomial `P_j` satisfies:

```text
P_j(u)>=u^2                    on [-1,0],
P_j(u)>=(1-a_j)^2u^2            on [0,1].
```

The companion script:

```text
E72_192_low_moment_envelope_certificate.py
```

checks endpoints and all real critical points of the two difference polynomials.

## 1. Output

```text
E72.192 low-moment envelope certificate
K0 degree-8 envelope:
  min p(u)-u^2 on [-1,0]       at -0.379501642378: +1.955032481880e-05
  min p(u)-r^2 u^2 on [0,1]    at +0.451502089136: +1.986941294181e-05
K1 degree-8 envelope:
  min p(u)-u^2 on [-1,0]       at -0.780500130119: +1.984606513358e-05
  min p(u)-r^2 u^2 on [0,1]    at +0.275501151427: +1.992058953033e-05
certificate: degree-8 envelopes majorize split energy on [-1,1]
```

Thus the scalar envelope is certified.

## 2. Consequence

Assuming:

```text
||K_0||<=0.90,
||K_1||<=0.60,
```

or equivalently the trace interval certificate `NTC-8`, we have:

```text
BSE <= 0.90^2Tr P_0(K_0/0.90)+0.60^2Tr P_1(K_1/0.60).
```

The right side is a fixed degree-8 trace/cycle expression.
