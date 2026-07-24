# E82.002 - Cluster-projective convergence theorem

## 1. Abstract setting

Let `V` be a domain, let `Phi_N` and `Psi_N` be holomorphic on `V`, and let
`t_N` be nonzero scalars.  Think of

```text
Phi_N(z)=L_{N,z}(P_N h_N),
Psi_N(z)=L_{N,z}((I-P_N)h_N),
G_N(z)=1+Phi_N(z)+Psi_N(z).                             (1.1)
```

### Theorem 1.1

Assume locally uniformly on `V` that

```text
t_N^(-1)Phi_N -> phi,
t_N^(-1)Psi_N -> 0,
t_N^(-1) -> tau,                                       (1.2)
```

where `g=tau+phi` is not identically zero.  Then

```text
t_N^(-1)G_N -> g                                      (1.3)
```

locally uniformly.  On every simply connected subdomain `W` on which `g` is
zero-free, the following limits hold locally uniformly, and the approximants
are zero-free on each fixed compact subset for all sufficiently large `N`:

```text
G_N(z)/G_N(z_*) -> g(z)/g(z_*),                        (1.4)

G_N'(z)/G_N(z) -> g'(z)/g(z)                           (1.5)
```

locally uniformly, for any `z_* in W`.

### Proof

Equation (1.3) follows by adding the three limits in (1.2).  On a compact
subset of `W`, the zero-free function `g` has positive minimum modulus.
Uniform convergence and Hurwitz imply that `t_N^{-1}G_N` is zero-free there
for large `N`.  Dividing (1.3) by its value at `z_*` gives (1.4).  Cauchy's
formula gives local uniform convergence of derivatives; division by the
uniformly nonvanishing functions gives (1.5). `QED`

## 2. Cluster criterion

In the CCM application, Theorem 1.1 proves `PG-CONV` from P1--P5 of E82.001.
It permits:

```text
- a cluster of arbitrary finite or growing dimension;
- a diverging scale t_N, in which case tau=0;
- a bounded scale, in which case the constant 1 survives through tau;
- cancellation inside the projected cluster before any absolute estimate.
```

## 3. Limitation

The theorem is a convergence mechanism only.  It does not identify `g` with
the Euler--Gamma target.  Replacing `g` by a fitted profile or by the inverse
Poisson transform of the desired current would be circular.

The remaining arithmetic statement is an independent equation for `g`,
derived from `M_N h_N=f_N` and the Gamma-prime symbols.

## 4. Status

```text
proved:
  the cluster-projective theorem with logarithmic-derivative convergence;
  no simplicity assumption is needed;

reduced:
  PG-CONV to P1--P5;

open:
  construction of P_N,t_N and the limits in (1.2) for the CCM system;
  arithmetic identification of g;

next:
  determine whether the exact cell equation supplies an independent equation
  for g or only recreates the autopsied interpolation residual.
```
