# E72.235 - Block cubic identity

## Purpose

This note gives the exact algebraic decomposition that replaces the rough spectral budget.

Let

```text
P = span_Q{0,1},  R=P^\perp,
A=A_1,
A = [[B,C],[C^*,D]]
```

with respect to `P \oplus R`. Then:

```text
Tr(A^3)
= Tr(B^3) + Tr(D^3)
  + 3 Tr(B C C^*) + 3 Tr(D C^* C).              (BCI)
```

This is just block multiplication and cyclicity of trace.

## Diagnostic

Script:

```text
E72_235_block_cubic_identity_probe.py
```

Output:

```text
E72.235 block cubic identity probe
P=Q-projected even modes {0,1}; A=[[B,C],[C*,D]].
TrA3 = TrB3 + TrD3 + 3Tr(BCC*) + 3Tr(D C*C)
lam TrA3 TrB3 TrD3 3BCC 3DCC check
 12 -9.452352e-03 -1.016915e-02 +9.934832e-04 -7.743330e-04 +4.976480e-04 -9.452352e-03
 16 -9.305587e-03 -1.011079e-02 +4.107135e-04 -1.130253e-04 +5.075155e-04 -9.305587e-03
 20 -1.076469e-02 -1.088083e-02 +2.431546e-04 -3.616291e-04 +2.346102e-04 -1.076469e-02
 24 -1.568847e-02 -1.599281e-02 +3.382603e-04 -3.741454e-04 +3.402209e-04 -1.568847e-02
 28 -1.331685e-02 -1.367062e-02 +2.601427e-04 -1.936095e-04 +2.872394e-04 -1.331685e-02
 32 -2.110545e-03 -2.048046e-03 +1.376082e-04 -5.747763e-04 +3.746699e-04 -2.110545e-03
```

## Reading

The sign comes from the explicit two-mode block:

```text
Tr(B^3)<0.
```

The remaining three terms are small. At `lambda=32`, the coupling term `3Tr(BCC^*)` supplies the extra
negative mass needed beyond `Tr(B^3)`.

## Exact Proof Target

HOC3 is now reduced to the finite block inequality:

```text
Tr(B^3) + Tr(D^3) + 3Tr(BCC^*) + 3Tr(DC^*C) <= 0.       (BCI-HOC)
```

where:

```text
B=P_L A_1 P_L,          P_L=span_Q{0,1},
D=R_L A_1 R_L,
C=P_L A_1 R_L.
```

This is the sharpest current form of the high-block odd lemma. It uses no zeros and no diagonalization
of the full matrix. The next mathematical task is to prove:

```text
Tr(B^3) + 3Tr(BCC^*) <= -[Tr(D^3)+3Tr(DC^*C)]_+.
```

The left side is low-rank and explicit; the right side is a compressed tail estimate.
