# P76.054 - Normalized shell Cauchy endpoint

Use the notation of P76.052.  Let

```text
G=B(z_0)^(-1),
g=G e_last,
w=G[:,D] R_0^(-1)(G e_last)_C,                 (NSC-1)
```

where `D` are the two deleted rows and `C` the two deleted columns.

Since

```text
B(z_0)g=e_last,
B(z_0)w is supported only on the deleted top shell rows,
```

their last-row equations are exactly

```text
r(z_0)g=1,
r(z_0)w=0.                                      (NSC-2)
```

Here `r(z)` is the complete last Cauchy row, including the new boundary
entry.  Therefore

```text
den(z)=1+[r(z)-r(z_0)]g=r(z)g,                  (NSC-3)

[r(z)-r(z_0)]w=r(z)w.                           (NSC-4)
```

The Sherman--Morrison scalar collapses to

```text
theta_N(z)=r(z)w/r(z)g.                         (NSC-5)
```

Thus the finite-section endpoint is the normalized directional estimate

```text
SHELL-CAUCHY:
sup_{z=i sigma, sigma in K}
|r(z)w|/|r(z)g| <=C_K L^2/N^2.                 (NSC-6)
```

Both vectors are canonical solutions of one bordered system:

```text
g: homogeneous CCM top equations, r(z_0)g=1;
w: forcing only on the two shell rows, r(z_0)w=0.
```

This formulation exposes the cancellation measured in P76.053.  It is not
the original critical Cauchy lock: `z,z_0` lie wholly in the Euler-safe
half-plane, the denominator fixes the scale, and the source is a known
two-row shell forcing rather than an unknown ground eigenline.
