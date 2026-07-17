# E72.224 - Cubic plus-current sign

## Purpose

E72.199 and E72.208 showed that the high-block cubic moment is purely non-resonant and negative. This
note rewrites that cubic moment in terms of the aggregated plus-current.

For one block, define:

```text
A = sum_{n in S_j} A_n^+,
K = A + A^*.
```

Then the cubic trace decomposes as:

```text
Tr(K^3)
= Tr(A^3)+Tr((A^*)^3)
 +3Tr(A^2A^*)+3Tr(A(A^*)^2).
```

Numerically, for the Phase 72 signed one-sided current:

```text
Re Tr(A^2A^*) = Re Tr(A^3),
Re Tr(A(A^*)^2) = Re Tr(A^3).
```

Therefore:

```text
Tr(K^3)=8 Re Tr(A^3).                            (CPLUS)
```

The high-block cubic sign becomes:

```text
Re Tr(A_1^3) < 0.
```

## Diagnostic

Script:

```text
E72_224_cubic_sign_decomposition_probe.py
```

Output:

```text
E72.224 cubic sign decomposition probe
High block: K=A+A*, decompose Tr(K^3) by cyclic sign types
lam dim total +++ --- ++- +-- mixed totalCheck
 12  32 -7.561881e-02 -9.452352e-03 -9.452352e-03 -2.835706e-02 -2.835706e-02 -5.671411e-02 -7.561881e-02
 16  40 -7.444470e-02 -9.305587e-03 -9.305587e-03 -2.791676e-02 -2.791676e-02 -5.583352e-02 -7.444470e-02
 20  48 -8.611756e-02 -1.076469e-02 -1.076469e-02 -3.229408e-02 -3.229408e-02 -6.458817e-02 -8.611756e-02
 24  56 -1.255078e-01 -1.568847e-02 -1.568847e-02 -4.706541e-02 -4.706541e-02 -9.413082e-02 -1.255078e-01
 28  64 -1.065348e-01 -1.331685e-02 -1.331685e-02 -3.995055e-02 -3.995055e-02 -7.990110e-02 -1.065348e-01
 32  72 -1.688436e-02 -2.110545e-03 -2.110545e-03 -6.331634e-03 -6.331634e-03 -1.266327e-02 -1.688436e-02
```

Additional check:

```text
block 0:
  Tr(K_0^3)=8 Re Tr(A_0^3)>0.

block 1:
  Tr(K_1^3)=8 Re Tr(A_1^3)<0.
```

through the tested stable windows.

## Reading

The high-block cubic sign is not a complicated eight-term phenomenon. It is the sign of one complex
plus-current cubic:

```text
Re Tr(A_1^3).
```

The sign flip between blocks is also clean:

```text
low block:  Re Tr(A_0^3)>0,
high block: Re Tr(A_1^3)<0.
```

Thus the odd sign sublemma should not be stated as a word-by-word displacement cancellation. It should
be stated as a plus-current phase theorem.

## New target

Prove:

```text
Re Tr A_j^3 has the sign of the block:
  positive for j=0,
  negative for j=1.
```

For the certificate, the essential part is:

```text
Re Tr(A_1^3) <= 0.                              (HOC)
```

This is a finite matrix trace inequality for the aggregated high-block plus-current.

## Status

Strong simplification:

```text
high-block odd sign -> Re Tr(A_1^3)<0.
```
