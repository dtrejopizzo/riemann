# E101.039 - Heat cofactor defect

## 1. Finite arithmetic heat kernel

For a finite Euler cutoff `L`, define

```text
P_L(v)
 ={1/sqrt(pi v)}sum_(2<=m<=exp(L))
   Lambda(m)m^(-1/2)
   exp(-(log m)^2/(4v)),                             (1.1)

H_(E,L)(v)=H_A(v)-P_L(v).                            (1.2)
```

By the same subordination calculation as E101.036,

```text
g_(E,L)(x)
 =integral_0^infinity exp(-xv)H_(E,L)(v)dv,
x>1/4.                                               (1.3)
```

For every fixed `v>0`, monotone convergence in the positive prime sum gives

```text
H_(E,L)(v)->H_Xi(v).                                 (1.4)
```

## 2. Exact finite defect

Let

```text
H_(L,N)(v)=Tr exp(-vK_(L,N)^2)                      (2.1)
```

be the positive core secular heat trace.  Define the signed heat defect

```text
R_(L,N)(v)
 =H_(L,N)(v)-H_(E,L)(v)
 =H_(L,N)(v)-H_A(v)+P_L(v).                         (2.2)
```

### Theorem 2.1

For every `x>1/4`, with `s=1/2+sqrt(x)`,

```text
D_(L,N)(s)/(2sqrt(x))
 =integral_0^infinity exp(-xv)R_(L,N)(v)dv.          (2.3)
```

### Proof

The heat representation of the core resolvent gives

```text
g_(L,N)(x)
 =integral_0^infinity exp(-xv)H_(L,N)(v)dv.          (2.4)
```

Subtract (1.3) and use the exact cofactor identity
E101.022(1.5). `QED`

No zero of the limiting target occurs in (2.2)--(2.3).  The finite heat trace
is a trace of a known matrix exponential, and the other two terms are Gamma
and von-Mangoldt quantities.

## 3. Disk current as a smoothed heat defect

The generating current of E101.034 satisfies exactly

```text
mathcal D_(L,N)(q)
 =integral_0^infinity
   [exp(-n_0v)/(1-q exp(-v))]R_(L,N)(v)dv,
|q|<1.                                               (3.1)
```

Thus the integer route observes one signed heat defect through a complete
family of positive smoothing kernels.

## 4. Heat identification theorem

Define

```text
HEAT-COFACTOR-IDENT:
R_(L_alpha,N_alpha)(v)->0
for every fixed v>0.                                (4.1)
```

### Theorem 4.1

`HEAT-COFACTOR-IDENT` implies `Omega7`.

### Proof

By (1.4) and (2.2), (4.1) gives

```text
H_(L_alpha,N_alpha)(v)->H_Xi(v)                     (4.2)
```

for every `v>0`.  Each function on the left is completely monotone because
it is a finite sum of `exp(-tv)` with `t>=0`.  The cone of finite-valued
completely monotone functions is closed under pointwise convergence on
`(0,infinity)`.  Hence `H_Xi` is completely monotone.  E101.036 gives
`Omega7`. `QED`

This theorem needs neither a safe interval nor a separate normal-family
argument.

## 5. Equivalence with the normalized integer package

### Theorem 5.1

Along one resolved family, `INTEGER-COFACTOR-IDENT` is equivalent to

```text
HEAT-COFACTOR-IDENT
and
D_(L_alpha,N_alpha)(1/2+sqrt(n_0))->0.              (5.1)
```

### Proof

Assume integer identification.  E101.032 gives weak convergence of

```text
d nu_alpha(t)=d mu_alpha(t)/(n_0+t).                 (5.2)
```

For fixed `v>0`, the function

```text
(n_0+t)exp(-tv)                                     (5.3)
```

extends continuously to `[0,infinity]` with value zero at infinity.
Integration against (5.2) therefore gives convergence of the secular heat
traces to `H_Xi(v)`, hence (4.1).  The base identity is one of the integer
conditions.

Conversely, assume (5.1).  Pointwise heat convergence makes `H_Xi`
nonnegative.  The base identity and independent Euler convergence give

```text
integral_0^infinity exp(-n_0v)H_alpha(v)dv
 ->integral_0^infinity exp(-n_0v)H_Xi(v)dv.          (5.4)
```

The nonnegative densities in (5.4) also converge pointwise.  Scheffe's lemma
therefore gives convergence in `L^1(dv)`.  Multiplication by
`exp(-kv)<=1` yields

```text
g_alpha(n_0+k)->g_Xi(n_0+k)                         (5.5)
```

for every `k>=0`.  E101.022 then recovers every integer cofactor identity.
`QED`

## 6. Remaining estimate

The force-bearing assertion is now the pointwise finite-matrix limit

```text
Tr exp(-vK_(L,N)^2)
 -H_A(v)+P_L(v)->0
for every fixed v>0.                                (6.1)
```

The three terms must remain coupled.  Separate upper bounds on the positive
secular trace and the positive prime Gaussian sum do not prove their signed
cancellation against the archimedean kernel.

## 7. Status

```text
proved:
  exact finite heat form of the cofactor defect;
  exact disk smoothing identity;
  HEAT-COFACTOR-IDENT implies Omega7;
  equivalence of normalized heat identification and integer identification;

open:
  the pointwise coupled heat limit (6.1).
```
