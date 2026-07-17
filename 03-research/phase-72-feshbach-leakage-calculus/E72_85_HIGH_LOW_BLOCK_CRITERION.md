# E72.85 -- High/low block criterion

**Date:** 2026-07-09.
**Role:** turn physical cofactor tightness into a block estimate for the pole-relative even complement.

## 0. Setup

Let:

```text
P_H = physical-height projection onto |d_n|<=H,
T_H = I-P_H.
```

Inside the even `Q_x`-space, choose orthonormal bases for the projected low and high spaces:

```text
L_H = orth(Q_even P_H),
H_H = orth((I-L_HL_H^*)Q_even T_H).
```

The compressed complement has blocks:

```text
C_LL = L_H^*C_E L_H,
C_LH = L_H^*C_E H_H,
C_HL = H_H^*C_E L_H,
C_HH = H_H^*C_E H_H.
```

The dual cofactor equation is:

```text
C_E g = Q_even r_s^even.
```

Splitting `g=g_L+g_H` gives:

```text
g_H = C_HH^(-1)a_H - C_HH^(-1)C_HL g_L,                       (HL)
```

where:

```text
a_H=H_H^*Q_even r_s^even.
```

Therefore:

```text
||g_H|| <= ||C_HH^(-1)a_H|| + eta_H ||g_L||,
eta_H:=||C_HH^(-1)C_HL||.                                     (HLC)
```

This is the exact high/low graph criterion.

## 1. What would prove PDCT

E72.84's physical cofactor tightness `(PDCT)` follows if:

```text
||C_HH^(-1)a_H||/||g|| -> 0,
eta_H -> 0,
```

as `H->infty`, uniformly for large `x` and `s` in compact windows.

The first condition is source-tail control. Since:

```text
r_s^even(n)=O(d_n^-2)
```

it is plausible once `C_HH^(-1)` is uniformly controlled on physical tails.

The second condition is high/low decoupling.

## 2. Numerical probe

The companion script:

```text
E72_85_high_low_block_probe.py
```

measures:

```text
eta_H = ||C_HH^(-1)C_HL||
```

and the relative high source tail.

Representative output:

```text
lambda=12, N=28:
  H=18  eta_H=8.95e-02  max source-tail=8.72e-02
  H=24  eta_H=8.55e-02  max source-tail=3.85e-02

lambda=20, N=40:
  H=18  eta_H=1.25e-01  max source-tail=1.08e-01
  H=24  eta_H=1.36e-01  max source-tail=5.05e-02
```

The graph coupling is small but does not visibly decay in these finite windows.

## 3. Interpretation

The two-block criterion is correct, but too coarse as a proof mechanism:

```text
eta_H small
```

explains why high tails are modest, but:

```text
eta_H not visibly -> 0
```

does not prove `(PDCT)`.

The finite data suggest that the real cancellation is not a uniform statement for every low source.
It is a statement for the specific Cauchy source:

```text
r_s^even=s(s^2I-D^2)^(-1)1.
```

## 4. Status

```text
proved: exact high/low graph identity (HL);
observed: high/low graph coupling is small in the finite harness;
not enough: two-block operator decoupling alone does not currently prove PDCT;
next: test and formulate Cauchy-channel Green decay.
```
