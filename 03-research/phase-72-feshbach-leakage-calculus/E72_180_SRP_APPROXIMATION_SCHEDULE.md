# E72.180 -- Approximation schedule for adaptive SRP

**Date:** 2026-07-09.
**Role:** give a concrete degree schedule for the adaptive signed-residual polynomial gate.

**Note:** E72.181 supersedes the Bernstein schedule below with a sharper explicit Chebyshev schedule
`D_x=O(sqrt(d_x))`. This document remains as a conservative fallback and derivation of the
absolute-value reduction.

## 0. Reduction to absolute value

The signed residual function is:

```text
f_a(t)=t                  for t<0,
f_a(t)=(1-a)t             for t>=0.
```

It has the exact representation:

```text
f_a(t)=(1-a/2)t-(a/2)|t|.                         (ABS)
```

Therefore polynomial approximation of `f_a` is equivalent to polynomial approximation of `|t|`.

If `q_D` satisfies:

```text
sup_{|u|<=1} |q_D(u)-|u|| <= delta_D,
```

then on `[-M,M]`:

```text
g_{a,D,M}(t)
 := (1-a/2)t-(aM/2)q_D(t/M)
```

satisfies:

```text
sup_{|t|<=M} |g_{a,D,M}(t)-f_a(t)| <= (aM/2)delta_D.   (ERR)
```

For the Phase 72 intervals:

```text
M_0=0.90, a_0=0.70,
M_1=0.60, a_1=0.60,
```

so:

```text
eps_0(D)+eps_1(D)
 <= (0.70*0.90/2 + 0.60*0.60/2) delta_D
 = 0.495 delta_D.
```

## 1. A concrete schedule

Use the Bernstein polynomial on `[0,1]` for:

```text
h(v)=|2v-1|.
```

Then:

```text
q_D(u)=B_Dh((u+1)/2)
```

is a degree `D` polynomial in `u`.

Explicitly:

```text
q_D(u)=sum_{k=0}^D |2k/D-1| binom(D,k)
       ((1+u)/2)^k ((1-u)/2)^{D-k}.              (Bern-abs)
```

Since `h` is `2`-Lipschitz:

```text
|B_Dh(v)-h(v)|
 <= 2 E|X/D-v|,
 X~Bin(D,v).
```

By Cauchy-Schwarz:

```text
E|X/D-v| <= sqrt(v(1-v)/D) <= 1/(2sqrt(D)).
```

Therefore:

```text
delta_D := sup_{|u|<=1}|q_D(u)-|u|| <= D^{-1/2}.       (B)
```

This rate is intentionally not sharp; it is enough to make the certificate finite and explicit. It
also gives an explicit constant:

```text
C_abs=1.
```

Choose a target error margin:

```text
m_x = m_*,
```

with fixed `0<m_*<1`. It is sufficient to choose:

```text
D_x >= 0.495^2 d_x / m_*^2.                       (D-schedule)
```

Then:

```text
sqrt(d_x)(eps_0(D_x)+eps_1(D_x)) <= m_*.
```

Thus the adaptive SRP theorem can be stated with an explicit degree schedule linear in the finite
dimension `d_x`.

The corresponding signed-residual polynomials are explicit:

```text
g_{j,D}(t)
 = (1-a_j/2)t-(a_jM_j/2)
   sum_{k=0}^D |2k/D-1| binom(D,k)
   ((1+t/M_j)/2)^k ((1-t/M_j)/2)^{D-k}.          (Bern-SRP)
```

## 2. Finite identity under the schedule

With this schedule, the residual-polynomial gate is:

```text
G_{x,D_x}=g_{0,D_x,M_0}(K_0)+g_{1,D_x,M_1}(K_1),
```

and:

```text
||R_x||_HS
 <= ||G_{x,D_x}||_HS + m_*.
```

Therefore `F2B-PSD` follows from:

```text
Tr(G_{x,D_x}^2) < (1-m_*)^2.                      (ASRP-cycle)
```

By E72.177, `Tr(G_{x,D_x}^2)` expands as a finite mixed von Mangoldt cycle sum with length at most:

```text
2D_x = O(d_x).
```

## 3. What remains

E72.180 removes the approximation-theory ambiguity from E72.179. The remaining arithmetic theorem is:

```text
Adaptive cycle inequality:
Tr(G_{x,D_x}^2) < (1-m_*)^2
```

with:

```text
||K_0||<=0.90,
||K_1||<=0.60,
D_x >= 0.495^2 d_x / m_*^2.
```

This is still not a proof of Ω7. It is a finite, explicit, zero-free target whose only unproved part is
the mixed cycle inequality for the exact von Mangoldt cell operators. E72.181 improves the schedule
from `O(d_x)` to `O(sqrt(d_x))`.

## 4. Important calibration

The numerical Chebyshev approximants of E72.179 are much better than the conservative `D^{-1/2}`
schedule. The schedule above is for a rigorous existence/finite-identity statement, not for efficient
computation.
