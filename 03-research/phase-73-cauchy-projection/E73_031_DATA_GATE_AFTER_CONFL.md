# E73.031 - DATA gate after CONFL

## 1. Correction

E73.026--E73.030 proved that Hermite/confluent coordinates remove artificial cluster blow-up.
However, this does not close the natural-height projection.

The reason is simple: for a fixed off-line shifted zero

```text
a=sigma+it,       sigma>0,
```

the natural weighted norm contains

```text
e^(sigma L).
```

The confluent Cauchy projection coefficients for fixed `a` and critical `k` do not contain a matching
factor `e^(-sigma L)`.  They are geometric quantities depending on `a,k`, multiplicity, and Hermite
normalization, but not on the finite mesh length `L`.

Thus an absolute estimate of the form

```text
e^(sigma L) sum_k ||C_conf^(-1)v_k|| |g_cancelled(k)| <= L^B
```

cannot follow from E72.327 `CRIT-POLY`, because `CRIT-POLY` gives only a polynomial bound for
`g_cancelled(k)`.

## 2. What CONFL actually achieved

`CONFL` remains valuable.  It proves:

```text
cluster blow-up is a coordinate singularity;
Hermite normalization is the correct natural-height coordinate system;
separated-node Lebesgue explosion should not be treated as a real obstruction.
```

But it does not supply the missing exponential smallness.

## 3. The surviving theorem

The remaining gate is `DATA`, in Hermite-normalized form:

```text
DATA-HERM:
For every natural-height off-line Hermite cluster A with real part alpha,

e^(alpha L)
|| Pi_conf(A,K_L) G_K ||_Herm
<= L^B.
```

Here `Pi_conf(A,K_L)` is the confluent Cauchy projection operator and

```text
G_K(k)=g_cancelled(k).
```

This is exactly `NAT-PROJ`, but in the right coordinates.

## 4. Equivalent scalar identity

Using E73.023,

```text
G_K(k)=g_cancelled(k)
=(1-e^(kL))sum_n xi_n/(ik-d_n).
```

Therefore the theorem is the finite identity:

```text
DATA-HERM:
e^(alpha L)
|| sum_{k in K_L} Pi_conf(A,k)
   (1-e^(kL))sum_n xi_n/(ik-d_n)
||_Herm
<= L^B.
```

This is the sharp finite form of the remaining scalar WRL obstruction.

## 5. Status

```text
closed: artificial separated-cluster blow-up by CONFL;
falsified: absolute geometry plus CRIT-POLY as a closing route;
remaining: DATA-HERM, the Hermite-normalized critical-data cancellation identity.
```

The remaining work is not generic positivity and not Cauchy conditioning.  It is the cancellation of
the actual cancelled Cauchy data in the Hermite projection directions.
