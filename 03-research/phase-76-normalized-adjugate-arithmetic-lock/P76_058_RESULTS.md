# P76.058 - Prolate safe-ratio bridge

At `lambda=6`, with safe reference `sigma_0=1`, maximum relative errors are:

```text
N    boundary vs Xi^2    prolate vs Xi^2    boundary vs prolate
6       2.707e-1            5.514e-3             2.637e-1
8       1.867e-1            2.786e-4             1.871e-1
10      1.380e-1            3.243e-5             1.380e-1
12      1.068e-1            1.377e-6             1.068e-1
```

Once the Fourier cutoff resolves the prolate vector, its safe ratio is
already indistinguishable from normalized `Xi^2` at the tested precision.
The entire remaining boundary error is the directional boundary-to-prolate
defect.

This replaces the failed `L2` eigenvector perturbation target by the weaker
and exact topology required for closure:

```text
SAFE-PROLATE-BRIDGE:
sup_{sigma in K}
| [E_boundary(i sigma)/E_boundary(i sigma_0)]
  /[E_prolate(i sigma)/E_prolate(i sigma_0)] -1| ->0.
```

Combined with Connes's prolate-transform convergence, this bridge implies
the safe-ratio theorem of P76.034.
