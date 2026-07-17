# E72.193 -- LM8-ASRP certificate

**Date:** 2026-07-09.
**Role:** replace diagonal ASRP by fixed degree-8 low-moment envelopes.

## 0. Gate

Define:

```text
LM8(K_0,K_1)
=0.90^2Tr P_0(K_0/0.90)+0.60^2Tr P_1(K_1/0.60),
```

where `P_0,P_1` are the certified degree-8 envelopes of E72.192.

Then:

```text
LM8-ASRP:
LM8(K_0,K_1)<0.9409.
```

implies:

```text
D-ASRP-0.03.
```

## 1. Output

The companion script:

```text
E72_193_lm8_asrp_probe.py
```

reports:

```text
E72.193 LM8-ASRP probe
certified degree-8 low-moment envelopes; target 0.9409
 lam    L dim exactBSE  LM8env  slack  pass
  12  4.97  32    0.898   0.937  0.039 YES
  16  5.55  40    0.794   0.817  0.023 YES
  20  5.99  48    0.735   0.754  0.019 YES
  24  6.36  56    0.740   0.764  0.023 YES
  28  6.66  64    0.636   0.663  0.027 YES
  32  6.93  72    0.492   0.526  0.034 YES
  36  7.17  80    0.648   0.684  0.036 YES
worst_LM8=0.937 at lambda=12
```

## 2. Updated final stable target

The stable arithmetic certificate can now be stated with only fixed-degree cycle inequalities plus
the mixed sign lemma:

```text
NTC-8:
Tr((K_0/0.90)^16)<1,
Tr((K_1/0.60)^16)<1.

LM8-ASRP:
0.90^2Tr P_0(K_0/0.90)+0.60^2Tr P_1(K_1/0.60)<0.9409.

XNEG:
Tr(G_{0,D_x}G_{1,D_x})<=0.
```

The first three inequalities have fixed cycle length at most `16` and `8`. Only `XNEG` still involves
the adaptive Chebyshev degree schedule.

## 3. Meaning

This is a major simplification of the diagonal energy. The long adaptive polynomial is no longer
needed to prove the size of `BSE`; it is only needed to formulate the mixed sign correction in a
sign-projection-free way.
