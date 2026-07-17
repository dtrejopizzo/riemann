# P76.042 - Inhomogeneous Loewner reduction

Let

```text
A=2 diag(C_L)-(2/L)Loew(S_L)-mu I
```

on the inner mesh, and suppose `Aw=f`.  Define

```text
W(z)=sum_n w_n/(z-d_n),
M_S,w(z)=sum_n S_L(d_n)w_n/(z-d_n),
R_S,w(z)=S_L(z)W(z)-M_S,w(z).                  (IL-1)
```

Exactly as in P76.011, the removable nodal values satisfy

```text
R_S,w(d_n)=(Loew(S_L)w)_n.
```

The inhomogeneous equation gives the exact nodal law

```text
R_S,w(d_n)
=L(C_L(d_n)-mu/2)w_n-(L/2)f_n.                (IL-2)
```

No eigenline or small residual is assumed.

## The single coupled generator

For P76.041 put

```text
h_b=a_b u+b_b v,
f_b=a_b s+b_b 1.                               (IL-3)
```

Since `Au=s` and `Av=1`,

```text
A h_b=f_b.                                     (IL-4)
```

If

```text
H_b(z)=sum_n h_b(n)/(z-d_n),
H_b^bd=sum_n h_b(n)/(d_n-d_b),
```

then the exact boundary numerator becomes simply

```text
F_b(z)=1+H_b(z)+H_b^bd.                        (IL-5)
```

Thus `CORE-SR-LOG` depends on one inhomogeneous Loewner solution, not two
independent inverse columns.

## Exact interpolation residual

Let `I_w` interpolate `w_n` and `I_f` interpolate `f_n` on the mesh.  From
`(IL-2)`, the entire function

```text
E_w(z)
=R_S,w(z)-L(C_L(z)-mu/2)I_w(z)+(L/2)I_f(z)     (IL-6)
```

vanishes at every mesh point.  Hence

```text
E_w(z)=D(z)G_w(z).                              (IL-7)
```

For the coupled generator `h_b`, `(IL-6)`--`(IL-7)` are an exact scalar
Gamma-prime formula for `H_b`, and therefore for `F_b'/F_b`.

The remaining theorem is now:

```text
COUPLED-LOEWNER-REM:
evaluate the signed combination in (IL-6) for w=h_b on z=i sigma,
and prove that its logarithmic derivative converges to 2 Xi'/Xi after the
bilateral/core assembly.
```

Unlike the autopsied P76.012 route, the source term `(L/2)I_f` is retained;
it is part of the cancellation and may not be bounded separately.
