# P76.046-P76.047 - Cutoff cocycle and mu freezing

## Consecutive increments

At fixed `lambda=6`, the core safe-log increments satisfy numerically

```text
N->N+1    max |Delta J|    N^2 max|Delta J|/L^2
8->9       5.15e-3              0.0257
9->10      4.73e-3              0.0298
10->11     3.70e-3              0.0288
11->12     3.00e-3              0.0283
```

The stabilized scaled quantity supports

```text
|J_{L,N+1}-J_{L,N}| <= C_K L^2/N^2.             (CC-1)
```

If proved, summation gives a fixed-`L` finite-section tail
`O_K(L^2/N)`.

## Freezing the ground level

Replacing `mu_N` by zero inside the boundary Schur solve changes the safe
core trace by

```text
N=6:  1.48e-5
N=8:  1.46e-8
N=10: 4.10e-7
N=12: 6.79e-7.
```

These defects are much smaller than the cutoff increments.  They are not
monotone because both quantities arise from highly conditioned solves, but
the 100-digit rebuild resolves them well below the `1e-3` scale.

## Exact proof split

Define `J_{L,N}(sigma;mu)` by using
`(H_{N-1}-mu I)^(-1)` in the transfer.  Then

```text
J_{L,N}(mu_N)-J_{L,N}(0)
=int_0^mu_N partial_mu J_{L,N}(t)dt.             (CC-2)
```

At `mu=0`, consecutive matrices are nested and shell elimination gives an
exact rank-two Schur cocycle.  The live finite-section theorem splits into:

```text
SHELL-LOG:
|J_{L,N+1}(0)-J_{L,N}(0)|<=C_K L^2/N^2;

MU-DIR:
int_0^mu_N |partial_mu J_{L,N}(t)|dt=o_K(1).
```

Neither statement permits replacing the directional derivative by the full
inverse-gap norm.
