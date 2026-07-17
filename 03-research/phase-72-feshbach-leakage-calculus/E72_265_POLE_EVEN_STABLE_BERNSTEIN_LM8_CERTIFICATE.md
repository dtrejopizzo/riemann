# E72.265 -- Pole-even stable Bernstein LM8 certificate

**Purpose.** Prove exactly, by rational Bernstein subdivision, that the E72.264 six-decimal rational
envelope is a valid homogeneous LM8 majorant.

The four inequalities are:

```text
R0(u) >= 1       for -1 <= u <= 0,
R0(u) >= 0.09    for  0 <= u <= 1,
R1(u) >= 1       for -1 <= u <= 0,
R1(u) >= 0.16    for  0 <= u <= 1.
```

Since `P_j(u)=u^2R_j(u)`, this proves the stable pole-even LM8 envelope without any constant trace
term:

```text
P_j(0)=P_j'(0)=0.
```

## Exact output

All coefficients are exact rationals with denominator `10^6`.

```text
E72.265 pole-even stable rational Bernstein LM8 certificate
All coefficients exact rationals from E72.264 buffer=0.002, six-decimal grid.
R0-1 on [-1,0]: PASS boxes=15 depth=5 terminal_min_bern=+8.933232610600e-04 (4795992738761/5368709120000000)
R0-0.09 on [0,1]: PASS boxes=17 depth=6 terminal_min_bern=+1.319695991492e-03 (39676357868851/30064771072000000)
R1-1 on [-1,0]: PASS boxes=17 depth=5 terminal_min_bern=+2.422040463537e-04 (16254038407/67108864000000)
R1-0.16 on [0,1]: PASS boxes=17 depth=5 terminal_min_bern=+1.943650094835e-04 (182610609829/939524096000000)
overall PASS
```

## Consequence

The stable pole-even LM8 **majorant algebra** is now closed:

```text
lambda >= 20 tested windows:
BSE(K0,K1) <= Tr P0(K0/0.90) + Tr P1(K1/0.60) < 0.9409.
```

The remaining work is not the univariate majorant. It is:

1. prove the model/arithmetical moment bounds for the stable windows uniformly;
2. certify the transition window `lambda=16` sharply;
3. state the corrected pole-even RFBD route with an explicit threshold `L0`.
