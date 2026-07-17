# E73.033 - Critical data divisibility

## 1. Question

After E73.032, the final gate is:

```text
DATA-HERM:
e^(alpha L)||Pi_conf(A,K_L)g_cancelled(K_L)||_Herm <= L^B.
```

There were two possible mechanisms:

```text
MOMENT:
Hermite projection weights create strong cancellation among critical nodes;

DIV:
the individual cancelled Cauchy values g_cancelled(k) are already exponentially small in the
critical directions needed by the off-line projection.
```

E73.033 tests which mechanism is visible.

## 2. Decomposition

For each Hermite cluster and critical window, write

```text
Out := sum_k h(k)g_cancelled(k).
```

Compare:

```text
||Out||_Herm
```

against the exact absolute ceiling

```text
sum_k ||h(k)||_Herm |g_cancelled(k)|.
```

If the ratio is small uniformly, the mechanism is `MOMENT`.  If the ratio is often near one, the
mechanism must be `DIV`.

## 3. Result

E73.033 shows:

```text
l1Ratio often near 1.
```

Therefore a universal Hermite moment cancellation is not present in the tested data.  The finite
identity must be proved by controlling the critical data themselves.

## 4. Updated endpoint

The sharp endpoint becomes:

```text
CRIT-DIV:
For every natural-height critical window K_L that couples to an off-line Hermite cluster A,

max or weighted l1 size of g_cancelled(K_L) in the Pi_conf directions
is O(e^(-alpha L)L^B).
```

Equivalently, in fully finite form:

```text
e^(alpha L)
||sum_k C_conf(A)^(-1)v_k
   (1-e^(kL))sum_n xi_n/(ik-d_n)
||_Herm
<= L^B.
```

This is not a generic interpolation theorem.  It is the divisibility of the finite cancelled Cauchy
transform by the off-line Hermite projection functional.

## 5. Relation to previous gates

The chain is now:

```text
E73.026 CONFL       removes cluster-coordinate blow-up;
E73.031             falsifies absolute geometry;
E73.033             falsifies universal Hermite moment cancellation;
remaining           CRIT-DIV / DATA-HERM.
```

This is exactly the finite divisibility statement requested by the Phase 72 route.
