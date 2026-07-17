# E72.236 - Low-block arithmetic formula

## Purpose

E72.235 identifies the two-dimensional block

```text
B=P_L A_1 P_L,      P_L=span_Q{0,1}
```

as the source of the high-block cubic sign. This probe records `B` and compares it with elementary
high-window arithmetic sums.

## Diagnostic

Script:

```text
E72_236_low_block_arithmetic_formula_probe.py
```

Output:

```text
E72.236 low-block arithmetic formula probe
B=P01 A_1 P01 in an orthonormal Q-projected {0,1} basis
lam cnt B00 B01 B11 eig0 eig1 TrB3 s0 s1mu sc ss sc1 ss1
 12  35 -7.056942e-02 +1.117282e-01 -1.312351e-01 -2.166748e-01 +1.487028e-02 -1.016915e-02 1.476796e+01 2.407336e+00 +6.218948e+00 -9.786565e+00 +1.622610e-01 -1.995709e+00
 16  55 -3.424915e-02 +1.042768e-01 -1.566428e-01 -2.163538e-01 +2.546185e-02 -1.011079e-02 2.144825e+01 3.581329e+00 +8.582921e+00 -1.405209e+01 +7.640519e-02 -2.903650e+00
 20  79 -1.065918e-01 +1.156431e-01 -1.053147e-01 -2.215981e-01 +9.691673e-03 -1.088083e-02 2.823639e+01 4.623809e+00 +1.169798e+01 -1.821165e+01 +1.273307e-01 -3.736280e+00
 24 105 -1.161942e-01 -1.331489e-01 -1.213817e-01 -2.519621e-01 +1.438618e-02 -1.599281e-02 3.426429e+01 5.470014e+00 +1.496238e+01 -2.208181e+01 +3.413885e-01 -4.443670e+00
 28 136 -7.898858e-02 +1.277513e-01 -1.372979e-01 -2.391790e-01 +2.289259e-02 -1.367062e-02 4.102826e+01 6.422647e+00 +1.850925e+01 -2.617349e+01 +4.895674e-01 -5.218954e+00
 32 171 -3.151826e-02 +6.422728e-02 -8.383416e-02 -1.270259e-01 +1.167349e-02 -2.048046e-03 4.806295e+01 7.439486e+00 +2.202827e+01 -3.032284e+01 +5.763854e-01 -6.025426e+00
```

## Reading

The entries of `B` depend on the orthonormalization of `span_Q{0,1}`, so the sign of the off-diagonal
entry is not invariant. The invariant data are:

```text
eig_-(B)<0<eig_+(B),
|eig_-(B)| >> eig_+(B),
Tr(B^3)<0.
```

The elementary sums show the expected high-window phase: the sine component over the high block is
large and negative. But the exact block is model-whitened, so the proof should be written in invariant
matrix form rather than by raw trigonometric entries.

## Consequence

Use the `2x2` trace invariants of `B`, not its basis-dependent entries.
