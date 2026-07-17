# E72.82 -- Mesh cotangent shortcut audit

**Date:** 2026-07-09.
**Role:** test and reject the tempting shortcut that the HPAC boundary factor alone creates the root
transport cancellation.

## 0. The tempting identity

From E72.81, the root transport residual is:

```text
i C_{g,k}(tau)
-(exp(i tau L)-1)L^(-1)C_{g,1}(tau)M_k(tau).
```

A possible shortcut would be:

```text
(exp(i tau L)-1)L^(-1)M_1(tau) approx i,
```

because the infinite uniform mesh satisfies a cotangent summation formula:

```text
sum_{n in Z} 1/(tau-2pi n/L) = (L/2)cot(L tau/2).
```

If this shortcut were true in the finite CCM window, the vector:

```text
i k_x-(exp(i tau L)-1)L^(-1)M_k(tau)1
```

would look like a model Weyl-null direction for free.

## 1. Result

The shortcut is false in the finite windows that matter. Numerically:

```text
beta_1(tau):=(exp(i tau L)-1)L^(-1)M_1(tau)
```

does not approach `i` in the tested active roots. Representative values:

```text
lambda=12, N=28:
  tau=0.825  |beta_1-i|=8.88e-01
  tau=2.135  |beta_1-i|=8.30e-01
  tau=3.221  |beta_1-i|=9.91e-01

lambda=20, N=40:
  tau=0.241  |beta_1-i|=6.61e-01
  tau=1.856  |beta_1-i|=6.62e-01
  tau=3.844  |beta_1-i|=8.70e-01
```

## 2. Consequence

The HPAC boundary factor is not itself the missing annihilator. The root transport theorem must use
the dual cofactor vector `g_{x,s}` and the model vector `k_x` together:

```text
i C_{g,k}(tau)
 approx
(exp(i tau L)-1)L^(-1)C_{g,1}(tau)M_k(tau),
```

not a universal mesh identity independent of `g` and `k`.

## 3. Status

```text
rejected: scalar mesh-cotangent shortcut beta_1 approx i;
kept:     E72.81 dual cofactor transport as the current minimal theorem.
```
