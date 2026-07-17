# E72.178 -- Stable SRP reduction theorem

**Date:** 2026-07-09.
**Role:** package the current Phase 72 endpoint as a precise reduction theorem.

## 0. Objects

Use the fixed arithmetic split:

```text
I_0=[0,0.60L],
I_1=(0.60L,L],
K_rel=K_0+K_1,
a_0=0.70,
a_1=0.60.
```

Let:

```text
f_a(t)=t                  for t<0,
f_a(t)=(1-a)t             for t>=0.
```

Then the exact fixed-weight residual is:

```text
R_x=f_{a_0}(K_0)+f_{a_1}(K_1).
```

For each degree `D`, let `g_{0,D},g_{1,D}` be the Chebyshev polynomial approximants to the two signed
residual functions, with certified errors:

```text
eps_0(D),
eps_1(D).
```

## 1. Stable-SRP

`Adaptive-Stable-SRP` is the following uniform assertion for all sufficiently large `x`:

```text
(S1) ||K_0||<=0.90 and ||K_1||<=0.60.

(S2) There is a degree D_x and a margin m_x such that
     sqrt(d_x)(eps_0(D_x)+eps_1(D_x)) <= m_x
     and
     ||g_{0,D_x}(K_0)+g_{1,D_x}(K_1)||_HS + m_x < 1.
```

Equivalently, by E72.177, `(S2)` can be written as one finite mixed-cycle inequality:

```text
Tr(G_{x,D_x}^2) < (1-m_x)^2,
G_{x,D_x}=g_{0,D_x}(K_0)+g_{1,D_x}(K_1),
```

where `Tr(G_{x,D_x}^2)` expands into prime-power cell cycles of length at most `2D_x`.

## 2. Finite-F2B

`Finite-F2B` is the direct finite verification of:

```text
||K_rel-a_0K_0^+-a_1K_1^+||_HS < 1
```

for the finitely many pre-stable windows. In the current numerical grid these are:

```text
lambda=6,8,10.
```

E72.165 verifies them directly with the fixed cut and weights.

## 3. Theorem

```text
Finite-F2B + Adaptive-Stable-SRP => uniform F2B-PSD.
```

Consequently, along the Phase 72 chain:

```text
Finite-F2B + Adaptive-Stable-SRP
=> F2B-PSD
=> PSD-DIST
=> scalar WRL resonance annihilation
```

provided the already isolated non-arithmetic gates of E72.146/E72.157 remain in force:

```text
GCOER + B-scale + Y-scale + OPM + UKERN + ROP + CGE-K.
```

## 4. Proof

Assume `Adaptive-Stable-SRP`. From `(S1)` and the certified scalar polynomial errors:

```text
||f_{a_j}(K_j)-g_{j,D_x}(K_j)||_op <= eps_j(D_x).
```

Therefore:

```text
||f_{a_j}(K_j)-g_{j,D_x}(K_j)||_HS <= sqrt(d_x)eps_j(D_x).
```

By the triangle inequality:

```text
||R_x||_HS
 = ||f_{a_0}(K_0)+f_{a_1}(K_1)||_HS
 <= ||g_{0,D_x}(K_0)+g_{1,D_x}(K_1)||_HS
    +sqrt(d_x)(eps_0(D_x)+eps_1(D_x))
 <= ||g_{0,D_x}(K_0)+g_{1,D_x}(K_1)||_HS + m_x
 < 1.
```

But:

```text
R_x=K_rel-a_0K_0^+-a_1K_1^+.
```

Thus:

```text
||K_rel-a_0K_0^+-a_1K_1^+||_HS < 1.
```

Since:

```text
a_0K_0^+ + a_1K_1^+ >= 0,
```

this implies `PSD-DIST`, hence the Phase 72 scalar WRL conclusion. The pre-stable windows are covered
by `Finite-F2B`. `QED`

## 5. Exact open statement

The remaining arithmetic theorem is now:

```text
Prove Adaptive-Stable-SRP uniformly.
```

In expanded form:

```text
||K_0||<=0.90,
||K_1||<=0.60,
Tr(G_{x,D_x}^2) < (1-m_x)^2,
```

where `Tr(G_{x,D_x}^2)` is the explicit mixed von Mangoldt cycle sum from E72.177, now of length at
most `2D_x`. E72.181 gives an explicit Chebyshev schedule with `D_x=O(sqrt(d_x))` for any fixed
approximation margin `m_x=m_*`. E72.183 replaces the interval hypotheses `||K_j||<=M_j` by fixed
trace-power certificates `Tr((K_j/M_j)^16)<1`.

This is a finite explicit, zero-free, sign-projection-free target. It is not yet proved uniformly.
