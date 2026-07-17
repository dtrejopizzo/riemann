# E73.035 - CRIT-DIV factor split

## 1. Critical data factorization

The critical data are

```text
g_cancelled(i gamma)
=(1-exp(i gamma L)) C_raw(gamma),
```

with

```text
C_raw(gamma)=sum_n xi_n/(-gamma-d_n).
```

Thus the final `CRIT-DIV` gate can be split into two possible sources of smallness:

```text
FINROOT:
C_raw(gamma) is small because gamma is close to a finite Cauchy root;

MESH:
1-exp(i gamma L) is small because gamma L is close to 2 pi Z.
```

## 2. Relation to DATA-HERM

The Hermite projection gate is:

```text
e^(alpha L)
||sum_k h(k)g_cancelled(k)||_Herm <= L^B.
```

After factorization:

```text
e^(alpha L)
||sum_k h(k)(1-exp(kL))C_x(ik)||_Herm <= L^B.
```

Therefore a proof of `CRIT-DIV` must show enough combined smallness from:

```text
finite Cauchy divisor alignment,
mesh-resonance factors,
and any residual signed cancellation.
```

## 3. What is not enough

E72.327 gives only:

```text
|g_cancelled(k)| <= L^B.
```

This is insufficient after the off-line weight `e^(alpha L)`.

E73.033 shows no uniform Hermite moment cancellation.  Therefore the proof must target the factors
above directly.

## 4. Updated sharp endpoint

The remaining theorem is:

```text
CRIT-DIV-FACT:
For every natural-height off-line Hermite cluster A with real part alpha,

||sum_k h_A(k)(1-exp(kL))C_x(ik)||_Herm
<= e^(-alpha L)L^B.
```

This is a finite statement about:

```text
1. the finite Cauchy transform C_x;
2. the mesh phase multiplier;
3. the Hermite Cauchy projection weights h_A(k).
```

## 5. Status

```text
observed: FINROOT and MESH both occur in tested windows;
remaining: prove their combined natural-height bound, or show this is equivalent to the final
           scalar WRL obstruction.
```

This is the current most explicit factorized form of the remaining problem.
