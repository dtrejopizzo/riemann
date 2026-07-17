# E72.177 -- Mixed cycle identity for SRP

**Date:** 2026-07-09.
**Role:** express the signed residual polynomial gate as one finite mixed prime-power cycle identity.

## 0. Polynomial residual

Let:

```text
g_j(t)=sum_{r=0}^D alpha_{j,r}t^r,
D=28.
```

The SRP polynomial residual is:

```text
G_x = g_0(K_0)+g_1(K_1).
```

The stable SRP gate is:

```text
||G_x||_HS + sqrt(d)(eps_0+eps_1) < 1.                 (SRP)
```

Equivalently:

```text
Tr(G_x^2) < (1-sqrt(d)(eps_0+eps_1))^2.               (SRP-square)
```

## 1. Mixed trace expansion

Expanding:

```text
Tr(G_x^2)
= sum_{r,s=0}^D alpha_{0,r}alpha_{0,s}Tr(K_0^{r+s})
 +sum_{r,s=0}^D alpha_{1,r}alpha_{1,s}Tr(K_1^{r+s})
 +2sum_{r,s=0}^D alpha_{0,r}alpha_{1,s}Tr(K_0^rK_1^s).
```

The pure traces use E72.174:

```text
Tr(K_j^m)
=sum_{n_1,...,n_m in S_j(x)}
  Tr(A_{n_1}...A_{n_m}).
```

The mixed traces are:

```text
Tr(K_0^rK_1^s)
=sum_{n_1,...,n_r in S_0(x)}
  sum_{m_1,...,m_s in S_1(x)}
  Tr(A_{n_1}...A_{n_r}A_{m_1}...A_{m_s}).       (MCI)
```

For fixed degree `D=28`, `SRP-square` is a finite explicit identity over prime-power cycles of length
at most `56`. E72.179/E72.180 replace the fixed degree by an adaptive schedule `D_x`, in which case
the same identity has cycle length at most `2D_x`.

## 2. Verification

The companion script:

```text
E72_177_mixed_cycle_identity_probe.py
```

checks `(MCI)` by brute force for low mixed moments:

```text
E72.177 mixed cycle identity probe
verifies Tr(K0^r K1^s)=sum Tr(A0...A0 A1...A1)
lambda=6 cells0=6 cells1=12
  r=1 s=1 direct=-4.641206745311e-01 cycle=-4.641206745311e-01 relErr=0.000e+00
  r=2 s=1 direct=-2.746870368376e-01 cycle=-2.746870368376e-01 relErr=5.551e-17
  r=1 s=2 direct=+2.212772214150e-01 cycle=+2.212772214150e-01 relErr=1.665e-16
lambda=8 cells0=8 cells1=19
  r=1 s=1 direct=-1.635044506432e-01 cycle=-1.635044506432e-01 relErr=5.551e-17
  r=2 s=1 direct=+2.628003393862e-03 cycle=+2.628003393861e-03 relErr=2.992e-17
  r=1 s=2 direct=+4.227538707431e-02 cycle=+4.227538707431e-02 relErr=5.551e-17
```

The identity is algebraic; the probe audits the implementation.

## 3. Current finite reduction

The stable Phase 72 arithmetic gate can now be written without spectral sign projections:

```text
Norm intervals:
||K_0||<=0.90, ||K_1||<=0.60.

Uniform polynomial error:
eps_0=6.802249139526e-03,
eps_1=3.886999508300e-03.

Mixed cycle inequality:
SRP-square holds for G_x=g_0(K_0)+g_1(K_1).
```

Then:

```text
Stable-SRP => F2B-PSD => PSD-DIST => scalar WRL.
```

For a uniform theorem, E72.179/E72.180 replace the fixed errors by an adaptive family
`eps_j(D_x)`. This is the sharpest finite explicit reduction currently obtained in Phase 72. The
remaining proof is to establish the norm intervals and the adaptive mixed cycle inequality uniformly
for all sufficiently large `x`.
