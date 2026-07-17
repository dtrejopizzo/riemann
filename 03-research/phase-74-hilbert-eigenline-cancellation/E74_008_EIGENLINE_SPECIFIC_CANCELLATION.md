# E74.8 - Eigenline-specific Gamma-prime cancellation

Date: 2026-07-16.

## Purpose

E74.7 showed that the raw condition `Qeta=0` does not create enough
divisibility in the cell packet

```text
B(y)=qQ_yeta.
```

This note asks the next discriminating question:

```text
Is the Gamma-prime cancellation special to eta=(I-P)xi_L,
or does it hold for generic eta in ker Q?
```

If generic `eta in ker Q` also cancels, the theorem would be a functional/cell
identity.  If only the projected eigenline cancels, the proof must use the
pole-even eigenline equation in an essential way.

## Probe

For each tested window:

1. compute `eta=(I-P)xi_L`;
2. compute `F_L[qQ_yeta]=arch-prime`;
3. sample random vectors `v in ker Q` with `||v||=||eta||`;
4. compare `F_L[qQ_yv]`.

## Status

```text
tested: generic ker(Q) vectors against eta=(I-P)xi_L;
result: cancellation is eigenline-specific, not a ker(Q) cell identity;
next: explicit coborder for qH_L(I-P), without pseudoinverse.
```
