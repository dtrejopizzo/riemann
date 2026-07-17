# E73.160 - Scalar dual termwise audit

Date: 2026-07-12.

## 1. Purpose

After E73.157--E73.159, the final scalar source is

```text
<xi,S_b>
=sum_{k in K_L} Pi(b,k)(exp(i gamma_k L)-1)F_x(gamma_k).
```

This note checks whether the smallness of this scalar comes from strong
cancellation between critical nodes `k`, or whether the termwise absolute
ceiling is already of the same order.

## 2. Result

The termwise `l1` norm and the signed scalar are nearly identical in the
tested current windows:

```text
sum_k |term_k|  ~=  |sum_k term_k|.
```

Thus this scalar dual endpoint is not currently showing a hidden multi-node
phase cancellation.  Its size is governed mainly by:

```text
1. the individual cancelled Cauchy values g_cancelled(k);
2. the weighted Cauchy projection kernel Pi(b,k).
```

This agrees with E73.024:

```text
CRIT-POLY + PI-LEB-NH => CC-PROJ.
```

## 3. Consequence

The next proof should not search first for cancellation among the critical
`k` terms.  The sufficient route is still:

```text
E72.327 CRIT-POLY
+ CONFL-PI-NH / PI-LEB-NH
=> CC-PROJ
=> NAT-PROJ
=> scalar WRL
=> Omega_7.
```

E73.025 explains why raw `PI-LEB-NH` is not automatic: clustered off-line
nodes can make separated-coordinate Cauchy Lebesgue constants blow up.
E73.026 says this is a coordinate singularity locally, fixed by Hermite /
confluent coordinates.

Therefore the honest remaining geometric theorem is:

```text
CONFL-PI-NH:
the Hermite-normalized confluent Cauchy projection has polynomial weighted
Lebesgue size through the natural-height window.
```

If `CONFL-PI-NH` fails globally, the fallback is `DATA`: the critical vector
must annihilate the bad singular directions of `Pi`.

## 4. Status

kept:

```text
CRIT-POLY + CONFL-PI-NH as the clean sufficient closure route.
```

deprioritized:

```text
searching for large signed cancellation over k in the scalar dual formula.
```

open:

```text
prove CONFL-PI-NH or isolate the DATA cancellation in the bad Hermite modes.
```
