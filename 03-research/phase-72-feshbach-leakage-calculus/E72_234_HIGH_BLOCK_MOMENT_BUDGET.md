# E72.234 - High-block moment budget

## Purpose

This probe tests whether a crude global moment inequality can replace the block decomposition.

For the high plus-current `A=A_1`, one has:

```text
posCube(A) <= lambda_max(A_+) Tr(A^2).
```

## Diagnostic

Script:

```text
E72_234_high_block_moment_budget_probe.py
```

Output:

```text
E72.234 high-block moment budget probe
A=A_1 high plus-current. posInf=max positive eigenvalue.
lam TrA TrA2 TrA3 posInf negInf posCube bound_posInf_TrA2
 12 -1.203914e-01 1.169855e-01 -9.452352e-03 1.196589e-01 2.226316e-01 3.366945e-03 1.399836e-02
 16 -1.501617e-01 1.174954e-01 -9.305587e-03 1.092589e-01 2.186781e-01 2.904490e-03 1.283741e-02
 20 -1.885802e-01 1.100463e-01 -1.076469e-02 9.118153e-02 2.243125e-01 1.947962e-03 1.003419e-02
 24 -2.009591e-01 1.166779e-01 -1.568847e-02 9.623115e-02 2.542393e-01 1.797834e-03 1.122805e-02
 28 -1.912598e-01 1.089138e-01 -1.331685e-02 9.368238e-02 2.409324e-01 1.626326e-03 1.020331e-02
 32 -1.029478e-01 6.442615e-02 -2.110545e-03 8.374987e-02 1.368453e-01 1.229703e-03 5.395682e-03
```

## Reading

The global bound `posInf*TrA2` is too coarse in the smaller and largest tested windows. It can be useful
as a component, but it does not close HOC3 by itself.

The block route is sharper.
