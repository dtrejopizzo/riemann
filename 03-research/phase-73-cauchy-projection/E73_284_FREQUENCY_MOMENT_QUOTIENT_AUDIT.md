# E73.284 - Frequency moment quotient audit

Date: 2026-07-14.

## 1. Purpose

E73.283 identifies the exact source coordinate for APR-U4:

```text
B_{a,w}(y)=q_aQ_yR_wxi_L
=sum_omega c_omega e^(iomega y)
 +y sum_omega l_omega e^(iomega y).
```

E73.236 proved the first two endpoint moment identities:

```text
sum_omega c_omega=0,
sum_omega l_omega=0.
```

E73.284 asks whether higher derivative moments also vanish or are small
enough to explain `FREQ-DIV`.

## 2. Test

For each exact packet, compute the moment rows:

```text
M_c,k = sum_omega (i omega)^k c_omega,
M_l,k = sum_omega (i omega)^k l_omega.
```

The probe reports:

```text
momNormB = exponent of ||(M_c,k,M_l,k)_{k<=K}||,
B0B      = B(0),
BLB      = B(L),
d0B      = B'(0).
```

The closed center itself is computed in exact frequency coordinates using the
validated `arch_closed_series - prime_modes` path.

## 3. Result

Only the endpoint moments are small:

```text
sum c_omega ~ 0,
sum l_omega ~ 0.
```

Higher moments are not small.  In fact, as soon as derivative moments are
included, the moment norm jumps to the size of `B'(0)` and then grows rapidly:

```text
momK=1: about L^-9 to L^-11,
momK=2: about L^-5 to L^-7,
momK>=4: order 1 or larger in several windows.
```

This matches E73.190:

```text
B'(0)=-(2/L)(sum_m q_a(m))(sum_n eta_n),
```

so the derivative data are not killed by the Cauchy constraints.

## 4. Meaning

There is no free tower of frequency moment divisibility.  The exact endpoint
constraints only allow constant gauges:

```text
W_omega -> W_omega-alpha,
V_omega -> V_omega-beta.
```

They do not allow quotienting out polynomial or derivative pieces of the
Gamma-prime weights.

Therefore `FREQ-DIV` cannot be proved by saying that many low frequency
moments vanish.  A proof must use the full signed structure of:

```text
1. the exact coefficient map eta -> (c,l);
2. the specific eta=R_wxi_L from the Gamma-prime eigenline;
3. the nonconstant Gamma-prime weights (W,V), modulo only constants.
```

## 5. Corrected theorem target

The remaining finite theorem is:

```text
GAUGE-FREQ-DIV:
For the endpoint-gauged weights

W'_omega=W_omega-alpha_L,
V'_omega=V_omega-beta_L,

prove

sum c_omega W'_omega + sum l_omega V'_omega
=O_M(L^(-M))
```

for the exact eta-packet coefficients.  The gauges may be chosen to optimize
the quotient weights, but only constants are justified by exact endpoint
moments.

## 6. Status

```text
proved earlier: endpoint moments sum c=sum l=0;
tested: higher derivative/frequency moments;
rejected: high-moment quotient explanation of FREQ-DIV;
current endpoint: prove GAUGE-FREQ-DIV with only constant gauges removed.
```
