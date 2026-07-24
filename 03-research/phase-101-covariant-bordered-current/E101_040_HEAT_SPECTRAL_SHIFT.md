# E101.040 - Heat spectral shift

## 1. Rank-one secular measure

For the right transfer, write

```text
K_N=D_N+(1/c_N)x_Nq_N^T,                             (1.1)
```

as in E78.152.  Its eigenvalues `kappa_(N,j)` are real.  Define the mass-zero
signed measure

```text
omega_N
 =sum_j delta_(kappa_(N,j))-sum_j delta_(d_(N,j)),  (1.2)
```

and its cumulative function

```text
Xi_N(u)=omega_N((minus infinity,u]).                 (1.3)
```

The transfer measure of E78.153 is

```text
nu_N=omega_N-delta_(d_(b,N)).                       (1.4)
```

## 2. Exact heat trace formula

### Proposition 2.1

For every `v>0`,

```text
Tr exp(-vK_N^2)-Tr exp(-vD_N^2)
 =integral_R exp(-vu^2)d omega_N(u)                 (2.1)

 =2v integral_R u exp(-vu^2)Xi_N(u)du.              (2.2)
```

Equivalently,

```text
Tr exp(-vK_N^2)
 =Tr exp(-vD_N^2)+exp(-vd_(b,N)^2)
  +integral_R exp(-vu^2)d nu_N(u).                  (2.3)
```

### Proof

Equation (2.1) is the definition of the two algebraic traces through their
real spectra.  Since `omega_N` has total mass zero and compact support,
Stieltjes integration by parts gives

```text
integral f d omega_N=-integral f'(u)Xi_N(u)du.       (2.4)
```

Take `f(u)=exp(-vu^2)` to obtain (2.2).  Equation (2.3) follows from (1.4).
`QED`

## 3. Exact decomposition of the open heat limit

Substitution into E101.039 gives

```text
R_(L,N)(v)
 =2v integral_R u exp(-vu^2)Xi_(L,N)(u)du
  +Tr exp(-vD_(L,N)^2)-H_A(v)+P_L(v).               (3.1)
```

Thus the matrix exponential is not a black box.  The only build-dependent
term is a Gaussian-weighted real spectral-shift count.  The other terms are
the explicit mesh, Gamma kernel and prime Gaussian sum.

At fixed `v`, the weight in (3.1) is concentrated at

```text
|u| comparable to 1/sqrt(v)                         (3.2)
```

and exponentially suppresses a spectral edge at `|u| comparable to N/L`.
This is the principal analytic difference from the Poisson kernel used in
GAP-Z.

## 4. Stable finite-section experiment

The construction was recomputed from the cell integrals at high precision for

```text
L=2log 6,
N=8,10,12,14,16,18.                                 (4.1)
```

The eigenvalues remained real to the working precision.  For zeta, the
increments

```text
Delta_N H(v)=H_(L,N+2)(v)-H_(L,N)(v)                (4.2)
```

were

```text
v       8->10          10->12         12->14         14->16

0.005   9.2310e-3      2.2746e-3      3.0115e-4      8.9196e-5
0.010   8.8197e-5      1.2050e-5      1.8057e-7      1.9430e-8
0.030   1.0000e-8      5.0530e-13     9.4679e-17     5.9037e-20
0.100   5.6684e-21     4.9851e-26     1.1546e-32     5.6002e-42.  (4.3)
```

The same computation for the planted system gave

```text
v       8->10          10->12         12->14         14->16

0.005   7.9809e-1      5.3726e-1      3.1523e-1      1.5905e-1
0.010   1.8035e-1      9.1334e-2      2.7816e-2      5.2858e-3
0.030  -4.5967e-2     -4.2978e-3     -4.0846e-3     -5.0892e-3
0.100  -2.0098e-2     -1.9494e-3     -2.6466e-3     -3.3579e-3.  (4.4)
```

The zeta increments exhibit Gaussian edge suppression.  The planted
increments also tend downward in magnitude but retain a visible signed
interior component.  This separates convergence rate from identification:
fixed-`L` heat convergence may be infrastructure, while its limiting value is
the discriminant.

## 5. Absolute defect audit

At the same `L`, direct evaluation of `H_A-P_L` and the secular trace gave the
following zeta defects:

```text
N       v=0.005       v=0.010       v=0.030       v=0.100

8      -1.1909e-2    -1.0045e-4    -1.0001e-8    -9.0402e-15
12     -4.0368e-4    -2.0037e-7    -9.4738e-17   -9.0401e-15
16     -1.3326e-5    -3.6491e-10   -5.2577e-24   -9.0401e-15. (5.1)
```

For `v=0.100`, the residual independent of `N` is the omitted prime tail
beyond the fixed cutoff.  At `v=1`, this tail is still large:

```text
H_(E,L)(1)=0.0922806488954,
H_(L,N)(1)=3.4130128627e-87,                         (5.2)
```

so `L` must grow; fixed-`L` stabilization cannot prove the cofinal theorem.

For the planted system at `N=16`, the defects at
`v=0.005,0.010,0.030,0.100,1` were respectively

```text
12.2574,
9.41440,
5.75843,
3.16506,
0.823200.                                            (5.3)
```

The experiment therefore passes the falsifier: the arithmetic heat identity
is not a universal consequence of finite real-rootedness.

## 6. Honest conclusion

The data support a rapid finite-section convergence theorem for the zeta heat
trace, but do not prove it.  Even such a theorem would close only the `N`
direction.  The coupled outer limit in `L`, including the prime Gaussian tail,
remains the force-bearing assertion.

## 7. Status

```text
proved:
  exact heat spectral-shift formula;
  exact separation of the build-dependent counting term;

observed with precision control:
  Gaussian finite-section suppression for zeta;
  persistent signed interior defect for the planted system;
  necessity of growing L at fixed large heat time;

open:
  a uniform proof of the zeta spectral-shift heat limit and its coupled outer
  identification.
```
