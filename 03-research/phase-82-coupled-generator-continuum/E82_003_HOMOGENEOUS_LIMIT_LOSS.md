# E82.003 - Homogeneous-limit loss and radical re-entry

## 1. Weak limit theorem

Let `M` be a densely defined self-adjoint operator on a Hilbert space and let
`P_N` be increasing finite-rank projections whose union is a core for `M`.
Suppose

```text
M_N=P_N M P_N,
M_N h_N=f_N,
k_N=t_N^(-1)h_N,                                      (1.1)
```

where `t_N` is nonzero.  Extend `k_N` by zero outside `P_N`.

### Theorem 1.1

Assume

```text
k_N -> k weakly,
t_N^(-1)f_N -> 0 weakly,                              (1.2)
```

and for every vector `phi` in a core of `M`,

```text
<M P_N phi,k_N> -> <M phi,k>.                         (1.3)
```

Then `k` is a weak solution of

```text
M k=0.                                                 (1.4)
```

### Proof

For a core vector `phi` and all sufficiently large `N`,

```text
<M P_N phi,k_N>
 = <P_N phi,M_N k_N>
 = <P_N phi,t_N^(-1)f_N>.                              (1.5)
```

The right side tends to zero by (1.2), while the left side tends to
`<M phi,k>` by (1.3).  Thus `<M phi,k>=0` on a core.  Self-adjointness gives
the weak equation (1.4). `QED`

The theorem includes the common case `|t_N|->infinity` with bounded sources.
The inhomogeneous source disappears at leading projective order.

## 2. Consequence for the coupled generator

If the cluster scale in E82.002 diverges, the limiting profile is controlled
by a vector in the kernel of the infinite fixed-`L` CCM equation.  The
generator equation alone does not say which kernel vector it is.

Let

```text
E_L=ker M_L,
ell_0(k)=safe Cauchy normalization at z_*.              (2.1)
```

If safe Cauchy rows separate square-summable vectors, then the following data
are sufficient:

```text
H1  dim E_L=1;
H2  ell_0 is nonzero on E_L;
H3  the radical vector k_L belongs to E_L;
H4  the finite projective profiles converge to E_L.     (2.2)
```

### Corollary 2.1

Under `H1`--`H4`, the normalized generator limit is

```text
k_L/ell_0(k_L),                                        (2.3)
```

and its safe Cauchy profile is unique.

### Proof

`H1` and `H3` give `E_L=span{k_L}`.  `H2` fixes the unique normalization.
`H4` places every sublimit in that normalized class. `QED`

## 3. Radical membership is not free

The full radical identity gives an untruncated equation for the full Riemann
kernel.  Passing it to the fixed-`L`, finite-Fourier generator system requires
exactly the three inherited controls

```text
PROLATE,
WEIL-TAIL,
FOURIER through RDP-SHELL.                              (3.1)
```

Because the bordered response is unbounded in ambient norm, ordinary tail
smallness does not prove `H3`--`H4`.  The directional estimates isolated in
E80.008 are necessary for this route.

## 4. Second loop theorem

The direct projective generator route has the implication

```text
BTG-DIV + MU-FREE-COMPLETENESS
+ RDP-SHELL + DIRECTIONAL-TAIL-CONTINUITY
=> H1--H4
=> identified projective generator limit.              (4.1)
```

After the known transform limit of the prolate kernel, this is the original
`SAFE-PROLATE-BRIDGE` route to `SR-SAFE`.

Thus the coupled generator continuum does not bypass the remaining LP and
radical-tail theorems.  It recovers them as the precise hypotheses needed to
identify the homogeneous projective limit.

## 5. What remains possible

An independent arithmetic proof would need a two-term expansion

```text
h_N=t_N k_L+r_N,                                       (5.1)
```

in which the correction `r_N` retains the inhomogeneous Gamma-prime source and
determines the outer logarithmic derivative without assuming `H3`--`H4`.
No such expansion is proved in the archive.

## 6. Status

```text
proved:
  the homogeneous-limit loss theorem;
  uniqueness of the radical profile under H1--H4;

closed:
  the leading projective generator limit as an independent shortcut to the
  arithmetic anchor;

reduced:
  its identification to the already isolated LP and directional-tail cut;

open:
  the theorems in (4.1);
  alternatively, a source-retaining two-term expansion (5.1);

next:
  decide between attacking directional radical membership and constructing a
  genuine two-term generator expansion.
```

