# E74.5 - Exact 2x2 Schur branch formula

Date: 2026-07-16.

## Purpose

E74.4 gives the exact row identity

```text
HPR row = r H_L.
```

For the projected eigenline

```text
eta=(I-P_w)xi_L,
```

the remaining scalar is therefore one component of

```text
Q_w H_L(I-P_w)xi_L.
```

This note reduces that vector to a 2x2 Schur branch formula.

## Formula

Let

```text
Q=Q_w,              G=QQ^*,
P=Q^*G^{-1}Q,
h=Qxi_L,
H_Lxi_L=mu_Lxi_L.
```

Then

```text
QH_L(I-P)xi_L
= QH_Lxi_L - QH_LQ^*G^{-1}Qxi_L
= (mu_L I_2 - QH_LQ^*G^{-1})h.                 (SCHUR-2)
```

Thus each HPR scalar is one component of

```text
S_w := B_w h,
B_w := mu_L I_2 - QH_LQ^*G^{-1}.
```

## Consequence

The terminal cancellation can be restated as:

```text
Schur-Branch Suppression.
For every admissible off-line Cauchy block w,

B_w h_w = O_M(L^(-M)).
```

This is exact and finite.  It does not prove the theorem by itself: neither
`h_w` nor `B_w` is individually negligible in a way that may be assumed.  The
proof must show that the finite pole-even equation forces their product to be
super-polynomially small, without estimating the two factors separately by an
incoherent ceiling.

## Why this is not circular

The objects `Q`, `G`, `B_w`, and `h_w` are built from the finite CCM matrix and
the fixed Cauchy block.  No zeta zero location or endpoint inverse is inserted.
The forbidden move would be replacing `B_w` by a pseudoinverse-selected
annihilator or assuming `h_w` is small.  The allowed next step is to derive an
explicit finite identity for `B_w h_w` from the CCM cell formula.

## Status

```text
proved: exact 2x2 formula (SCHUR-2);
verified: direct and Schur forms agree numerically;
open: prove Schur-Branch Suppression analytically.
```
