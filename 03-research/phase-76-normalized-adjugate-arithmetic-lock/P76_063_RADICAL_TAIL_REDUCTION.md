# P76.063 - Radical-tail reduction of the safe prolate bridge

Let `Q_W` be the full Weil bilinear distribution and let `k=E(h)` be the
Connes/Riemann kernel whose transform is the completed function `Xi`.
The explicit-formula spectral expansion gives, for every admissible test
vector `phi`,

```text
Q_W(k,phi)=0.                                    (RTR-1)
```

This uses only that `Xi` vanishes on its own complete divisor; it does not
assume that the zeros lie on the critical line.

Let `k_lambda` be the compact/prolate approximation, `P_N` the Fourier
cutoff, and `M_{L,N}` the one-sided rectangular CCM block.  Insert and
subtract the full radical vector before taking any inverse:

```text
M_{L,N}P_N k_lambda
=P_rows Q_W(k_lambda-k)
 +P_rows(Q_{W,L}-Q_W)k
 +Fourier-shell_N(k_lambda).                    (RTR-2)
```

The three terms are respectively:

```text
PROLATE:     k_lambda-k;
WEIL-TAIL:   omitted archimedean/prime support beyond L;
FOURIER:     columns outside the finite mesh.
```

P76.062 shows that the last term is asymptotically shell supported.  The
safe bridge follows from the coupled theorem:

```text
RADICAL-TAIL:
the first two terms are o(1) in the normalized bordered Cauchy pairing;
the Fourier term is summable through SHELL-CAUCHY;
the interior remainder of a growing shell is o(1) in the same pairing.
```

Then, after matching at a safe reference point `z_0`,

```text
sup_{sigma in K}
|r_{i sigma}(y_{L,N}-alpha_{L,N}P_N k_lambda)|
/|r_{i sigma}y_{L,N}| ->0,                     (RTR-3)
```

which is `SAFE-PROLATE-BRIDGE`.

Combined with:

```text
Connes: transform(k_lambda) -> Xi on closed substrips;
P76.030-P76.034: bilateral real-rooted safe-ratio closure,
```

`(RTR-3)` implies Omega7.

## Remaining estimates

The decomposition `(RTR-2)` is the correct non-circular proof architecture.
It forbids the ambient bordered norm falsified in P76.061.  Each tail must be
paired with the selected Cauchy response before taking absolute values.
