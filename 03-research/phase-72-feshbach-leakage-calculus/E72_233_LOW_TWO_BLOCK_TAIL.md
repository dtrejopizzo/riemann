# E72.233 - Low-two block tail

## Purpose

E72.232 gives an explicit two-dimensional negative block. This probe decomposes the high plus-current
with respect to:

```text
P = span_Q{0,1},  R=P^\perp,
A_1 = [[B,C],[C^*,D]].
```

## Diagnostic

Script:

```text
E72_233_low_two_block_tail_probe.py
```

Output:

```text
E72.233 low-two block/tail probe
P=Q-projected even Fourier modes {0,1}; R=P^perp.
lam minA minP negP posR negR ||PR||2 posA negA
 12 -2.226316e-01 -2.166748e-01 1.017244e-02 2.716847e-03 1.723364e-03 5.248e-02 3.366945e-03 1.281930e-02
 16 -2.186781e-01 -2.163538e-01 1.012730e-02 2.098215e-03 1.687502e-03 5.542e-02 2.904490e-03 1.221008e-02
 20 -2.243125e-01 -2.215981e-01 1.088174e-02 1.609803e-03 1.366648e-03 4.195e-02 1.947962e-03 1.271266e-02
 24 -2.542393e-01 -2.519621e-01 1.599578e-02 1.334669e-03 9.964089e-04 4.729e-02 1.797834e-03 1.748630e-02
 28 -2.409324e-01 -2.391790e-01 1.368262e-02 1.193644e-03 9.335013e-04 4.279e-02 1.626326e-03 1.494318e-02
 32 -1.368453e-01 -1.270259e-01 2.049637e-03 8.728945e-04 7.352863e-04 5.397e-02 1.229703e-03 3.340248e-03
```

## Reading

The negative cubic budget of `B=PAP` is already comparable to, and usually much larger than, the full
positive cubic budget of `A`:

```text
negCube(B) >= posCube(A)
```

in the tested windows except that the margin is tightest at `lambda=32`. The complement has small
positive cubic mass and the coupling `C` is moderate.

This motivates an exact block-cubic identity.
