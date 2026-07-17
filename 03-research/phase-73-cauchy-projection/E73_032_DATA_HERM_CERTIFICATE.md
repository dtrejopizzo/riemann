# E73.032 - DATA-HERM certificate

## 1. Final Hermite projection form

After E73.026--E73.031, the remaining natural-height projection is:

```text
DATA-HERM:
e^(alpha L)
||Pi_conf(A,K_L)G_K||_Herm <= L^B,
```

where:

```text
A       is an off-line Hermite cluster with Re A=alpha>0,
K_L     is the natural-height critical-line window,
G_K(k)  = g_cancelled(k),
Pi_conf is the confluent Cauchy projection operator.
```

This is equivalent to `NAT-PROJ`, but in the correct coordinates.

## 2. Why this is the right final finite identity

The previous alternatives have been resolved:

```text
separated Pi blow-up:
coordinate artifact, fixed by Hermite coordinates;

absolute Hermite geometry:
insufficient, because e^(alpha L) remains;

CRIT-POLY:
insufficient, because it is only polynomial.
```

Therefore the only remaining source of the required exponential suppression is the actual critical
data vector `g_cancelled(K_L)`.

## 3. Explicit formula

For a simple Hermite cluster centered at `a`, the contribution of a critical node `k` is:

```text
h(k)=C_conf(a)^(-1)v_k,
v_k[q]=(-1)^q/(a+k)^(q+1).
```

Thus:

```text
Pi_conf(A,K_L)G_K
= sum_{k in K_L} h(k) g_cancelled(k).
```

By E73.023,

```text
g_cancelled(k)
=(1-e^(kL))sum_n xi_n/(ik-d_n).
```

So the final identity is fully finite:

```text
e^(alpha L)
|| sum_{k in K_L} C_conf(A)^(-1)v_k
   (1-e^(kL))sum_n xi_n/(ik-d_n)
||_Herm
<= L^B.
```

## 4. Numeric reading

E73.032 shows that the Hermite projection of actual cancelled data is small in tested windows, but
the gain over the absolute ceiling is modest:

```text
gain roughly 0.05 to 0.44.
```

Thus the finite data support the formulation, not a proof.

## 5. Status

```text
closed: correct Hermite coordinates for Cauchy clusters;
closed: local confluent Taylor formula;
closed: absolute geometry route falsified;
remaining: prove DATA-HERM / CRIT-DIV.
```

This is the current sharp endpoint of Phase 73.

## 6. Update from E73.033

E73.033 tests whether `DATA-HERM` is caused by a universal Hermite moment cancellation.  It is not:
the exact `l1` ratio is often close to one.

Thus the remaining theorem should be named more sharply:

```text
CRIT-DIV:
the finite cancelled Cauchy transform g_cancelled has the off-line Hermite divisibility required by
Pi_conf.
```

This is still the same finite inequality as `DATA-HERM`, but its proof cannot rely on generic
Hermite cancellation.
