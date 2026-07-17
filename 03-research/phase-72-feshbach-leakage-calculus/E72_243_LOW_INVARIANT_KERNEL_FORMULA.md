# E72.243 - Low invariant kernel formula

## Purpose

E72.242 leaves the stable low-side proof in terms of two invariants of the `2x2` block:

```text
t_B=Tr(B),        s_B=Tr(B^2).
```

This note expands them as explicit finite kernel sums over the high prime-power measure.

## Kernel Formula

Let:

```text
A_1 = - sum_{n in S_1} beta_n M_{u_n},
beta_n = Lambda(n)/sqrt(n),
u_n = log n/L,
B = P A_1 P,
P=span_Q{0,1}.
```

Define the `2x2` compressed kernels:

```text
G(u)=P M_u P,
K1(u)=Tr(G(u)),
K2(u,v)=Tr(G(u)G(v)).
```

Then:

```text
t_B = - sum_n beta_n K1(u_n),
s_B =   sum_{m,n} beta_m beta_n K2(u_m,u_n).      (LIK)
```

## Diagnostic

Script:

```text
E72_243_low_invariant_kernel_formula_probe.py
```

Output:

```text
E72.243 low invariant kernel formula probe
A_1=-sum beta M_u; B=P A_1 P. Checks tB and sB from K1,K2 sums.
lam cells tDirect tKernel errT sDirect sKernel errS minK1 maxK1 minK2diag maxK2diag
 12    35 -2.018045e-01 -2.018045e-01 2.8e-17 4.716908e-02 4.716908e-02 2.8e-17 -1.072e-02 +2.680e-02 4.191e-05 8.534e-04
 16    55 -1.908920e-01 -1.908920e-01 5.6e-17 4.745727e-02 4.745727e-02 6.2e-17 -5.581e-03 +1.623e-02 7.918e-34 6.011e-04
 20    79 -2.119065e-01 -2.119065e-01 8.3e-17 4.919967e-02 4.919967e-02 1.4e-16 -1.247e-04 +1.440e-02 1.080e-09 2.508e-04
 24   105 -2.375759e-01 -2.375759e-01 1.1e-16 6.369185e-02 6.369185e-02 2.1e-16 -2.383e-03 +1.278e-02 1.426e-08 2.342e-04
 28   136 -2.162864e-01 -2.162864e-01 5.6e-17 5.773067e-02 5.773067e-02 6.8e-16 -6.610e-03 +1.097e-02 2.395e-08 1.646e-04
 32   171 -1.153524e-01 -1.153524e-01 4.2e-17 1.627185e-02 1.627185e-02 3.6e-16 -9.184e-04 +9.773e-03 4.380e-33 9.968e-05
 36   206 -2.388454e-01 -2.388454e-01 5.6e-17 6.387046e-02 6.387046e-02 1.4e-16 -2.263e-03 +7.595e-03 8.065e-10 9.298e-05
```

## Reading

The kernel formula is exact to roundoff.

The first low condition is:

```text
t_B<0  <=>  sum_n beta_n K1(u_n)>0.
```

The second low condition is essentially automatic from dimension. For a Hermitian `2x2` matrix:

```text
t_B^2 <= 2s_B,
```

so:

```text
3s_B-t_B^2 >= s_B >= 0.
```

Thus the only nontrivial low-block sign input is the positive average of `K1` against the high
prime-power measure, plus quantitative size of the low margin.

## Consequence

The stable proof of HOC3 reduces to:

```text
1. prove sum beta_n K1(u_n) >= a/L;
2. use 2x2 dimension to control 3s_B-t_B^2;
3. prove the tail norm bound <= c/L with c<a-compatible;
4. verify finite delicate windows sharply.
```

This is a kernel-average problem, not a full spectral problem.
