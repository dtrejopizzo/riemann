# E72.239 - Block-tail scaling

## Purpose

E72.238 gives a sufficient package:

```text
lowMargin = -[Tr(B^3)+3Tr(BCC^*)],
tailBound = Tr(D_+^3)+3||D_+||op||C||_HS^2.
```

This probe measures their scaling in `L`.

## Diagnostic

Script:

```text
E72_239_block_tail_scaling_probe.py
```

Output:

```text
E72.239 block/tail scaling probe
Reports core finite quantities against L. low=-[TrB3+3BCC], tailBound=TOB.
lam L low tailBound tB sB C_HS2 DposOp low*L tail*L tB*L sB*L
 12 4.969813 1.094348e-02 3.860581e-03 -2.018045e-01 4.716908e-02 3.690603e-03 1.033014e-01 5.438707e-02 1.918637e-02 -1.002931e+00 2.344215e-01
 16 5.545177 1.022382e-02 2.947212e-03 -1.908920e-01 4.745727e-02 3.465703e-03 8.165702e-02 5.669288e-02 1.634281e-02 -1.058530e+00 2.631590e-01
 20 5.991465 1.124246e-02 2.147375e-03 -2.119065e-01 4.919967e-02 2.346193e-03 7.637509e-02 6.735880e-02 1.286592e-02 -1.269630e+00 2.947781e-01
 24 6.356108 1.636695e-02 1.959834e-03 -2.375759e-01 6.369185e-02 2.731883e-03 7.628012e-02 1.040301e-01 1.245692e-02 -1.510058e+00 4.048322e-01
 28 6.664409 1.386423e-02 1.679917e-03 -2.162864e-01 5.773067e-02 2.183268e-03 7.424244e-02 9.239691e-02 1.119566e-02 -1.441421e+00 3.847408e-01
 32 6.931472 2.622823e-03 1.473216e-03 -1.153524e-01 1.627185e-02 3.199860e-03 6.253627e-02 1.818002e-02 1.021156e-02 -7.995621e-01 1.127879e-01
 36 7.167038 1.636806e-02 8.733170e-04 -2.388454e-01 6.387046e-02 1.415198e-03 5.322147e-02 1.173105e-01 6.259096e-03 -1.711814e+00 4.577620e-01
```

## Reading

The dominant stable scaling is:

```text
lowMargin ~ const/L,
tailBound ~ smaller const/L,
t_B ~ -const/L,
s_B ~ const/L.
```

The window `lambda=32` is a real finite dip in the low block, but the sufficient inequality still
passes:

```text
lowMargin / tailBound = 1.78.
```

The next proof should therefore split:

```text
finite delicate windows: exact fixed-cycle verification;
stable regime: prove scale constants lowMargin >= c_low/L,
               tailBound <= c_tail/L,
               c_low > c_tail.
```

This mirrors the earlier stable-certificate structure `NTC-8 + LM8-ASRP + XNEG-32`.
