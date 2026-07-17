# E72.395 results - natural-height nodal block

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_395_natural_nodal_probe.py
```

## Output

```text
E72.395 natural nodal block probe
   L    M      p   cluster  cond(CA)  relTailOp
  8.0   23   1.5    pair 1.029e+00  1.338e-02
  8.0   23   1.5  triple 1.074e+02  6.372e+01
  8.0   64   2.0    pair 1.029e+00  2.622e-04
  8.0   64   2.0  triple 1.074e+02  5.265e-02
 12.0   42   1.5    pair 1.029e+00  5.556e-03
 12.0   42   1.5  triple 1.074e+02  4.187e+00
 12.0  144   2.0    pair 1.029e+00  8.127e-05
 12.0  144   2.0  triple 1.074e+02  1.276e-02
 16.0   64   1.5    pair 1.029e+00  3.240e-03
 16.0   64   1.5  triple 1.074e+02  1.129e+00
 16.0  256   2.0    pair 1.029e+00  3.421e-05
 16.0  256   2.0  triple 1.074e+02  5.797e-03
```

## Interpretation

The diagnostic is

```text
relTailOp = || Lead_A^(-1) Tail_A ||_2,
```

where `Lead_A=diag(e^(a_jL))C_A` is the maximal Cauchy block and `Tail_A` is the absorbed finite-tail
matrix from E72.392.

For a conjugate pair the Cauchy block is well conditioned, and even `M=L^1.5` makes the tail
perturbative.  For a deliberately less friendly triple, `M=L^1.5` is not enough at small sizes, but
`M=L^2` makes the perturbation small and decreasing.

This confirms the condition added to E72.395:

```text
||C_A^(-1)|| L^2/M^2=o(1).
```

## Status

```text
verified: absorbed tail is perturbative once the cutoff power dominates Cauchy conditioning;
warning: natural-height NAT-NODAL must control Cauchy geometry, not just individual entries;
remaining: Schur-complement bound for lower-real-part couplings in the natural-height window.
```

