# P76.049 - Exact mixed shell cocycle

Fix `L` and `mu=0`.  Let `A=H_{N-1}` on the inner nodes and add the shell
`e=(-N,+N)`:

```text
H_N=[[A,U],[U^T,C]],
Sigma=C-U^T A^(-1)U.                            (MSC-1)
```

For the next right boundary node `w=+(N+1)`, split its CCM coupling column
as `(g_A,g_e)`.  Split the Cauchy row as `(r_A(z),r_e(z))` and put

```text
t_0(z,w)=1/(z-d_w)-r_A(z)A^(-1)g_A,
tau(z)=r_e(z)-r_A(z)A^(-1)U,
kappa(w)=g_e-U^T A^(-1)g_A.                     (MSC-2)
```

Block inversion gives the exact update

```text
T_{N+1,+}(z;0)
=t_0(z,w)-tau(z)Sigma^(-1)kappa(w).              (MSC-3)
```

Differentiating only the Cauchy rows gives

```text
T_{N+1,+}'(z;0)
=t_0'(z,w)-tau'(z)Sigma^(-1)kappa(w).            (MSC-4)
```

This is the correct shell cocycle.  It is mixed: the left residual is
Cauchy and the right residual is CCM.  Replacing either by the other would
be an invalid symmetric-kernel assumption.

The bilateral logarithmic increment must be formed from `(MSC-3)` and
`(MSC-4)` before taking absolute values.  The candidate `N^-2` gain is in
the signed scalar `tau Sigma^-1 kappa`, not in the norm of `Sigma^-1`.
