# E101.034 - Cofactor generating current

## 1. Disk transform of the integer defect

Fix `n_0>=1` and write

```text
x_k=n_0+k,
s_k=1/2+sqrt(x_k).                                   (1.1)
```

For one finite core approximant, define

```text
d_alpha(k)
 =D_(L,N)(s_k)/(2sqrt(x_k))
 =g_(L,N)(x_k)-g_(E,L)(x_k).                         (1.2)
```

Its generating current is

```text
mathcal D_alpha(q)
 =sum_(k>=0)q^k d_alpha(k),
|q|<1.                                               (1.3)
```

This scalar keeps the complete signed cofactor defect coupled before any
estimate is applied.

## 2. Exact secular heat side

Let

```text
H_alpha(v)=Tr exp(-vK_alpha^2).                      (2.1)
```

By E101.032 and Tonelli's theorem,

```text
mathcal G_alpha(q)
 :=sum_(k>=0)q^k g_(L,N)(x_k)
 =integral_0^infinity
    exp(-n_0v)H_alpha(v)/(1-q exp(-v))dv             (2.2)

 =integral_[0,1]d lambda_alpha(y)/(1-qy).            (2.3)
```

Thus the finite determinant side is a Cauchy transform of a positive compact
measure, although the difference (1.3) remains signed.

## 3. Exact Euler--Gamma side

Recall

```text
H_L(s)=A(s)-2sum_(2<=m<=exp(L))Lambda(m)m^(-s),      (3.1)

A(s)=2/s+2/(s-1)-log pi+psi(s/2).                   (3.2)
```

Hence

```text
mathcal G_(E,L)(q)
 :=sum_(k>=0)q^k g_(E,L)(x_k)                       (3.3)

 =sum_(k>=0)q^k A(s_k)/(2sqrt(x_k))
  -sum_(2<=m<=exp(L))
     Lambda(m)m^(-1/2)W_(n_0)(q,log m),             (3.4)
```

where

```text
W_(n_0)(q,u)
 =sum_(k>=0)
    q^k exp(-u sqrt(n_0+k))/sqrt(n_0+k).             (3.5)
```

The square-root subordination identity gives the exact positive kernel

```text
W_(n_0)(q,u)
 ={1/sqrt(pi)}integral_0^infinity
   [t^(-1/2)exp(-n_0t-u^2/(4t))]
   /[1-q exp(-t)]dt.                                 (3.6)
```

Indeed,

```text
exp(-u sqrt(x))/sqrt(x)
 ={1/sqrt(pi)}integral_0^infinity
   t^(-1/2)exp(-xt-u^2/(4t))dt,                     (3.7)
```

and the sum over `k` is geometric.  Formula (3.6) converts the prime part of
the integer current into a Gaussian sum in `log m`.

Combining (1.2)--(3.4) yields

```text
mathcal D_alpha(q)
 =mathcal G_alpha(q)-mathcal G_(E,L)(q).             (3.8)
```

Every term is either a finite secular heat trace, an archimedean scalar, or a
finite von-Mangoldt Gaussian sum.

## 4. Equivalence with integer identification

### Theorem 4.1

Along a resolved directed family with `L->infinity`, the following are
equivalent:

```text
(i)  d_alpha(k)->0 for every fixed k>=0;

(ii) mathcal D_alpha(q)->0 locally uniformly on |q|<1.  (4.1)
```

### Proof

Condition (i) at `k=0`, together with the independent Euler convergence,
bounds `g_(L,N)(n_0)`.  Positivity and monotonicity of the core Stieltjes
transform then give

```text
0<=g_(L,N)(n_0+k)<=C.                               (4.2)
```

The Euler terms are uniformly bounded for all `k` and all `L`: the prime sum
is dominated by the absolutely convergent series at
`s=1/2+sqrt(n_0)`, and the archimedean quotient is bounded on the same ray.
Thus

```text
|d_alpha(k)|<=C'                                    (4.3)
```

uniformly.  Dominated convergence in the geometric series proves (ii).

Conversely, local uniform convergence in the disk implies convergence of
every Taylor coefficient at the origin by Cauchy's formula, giving (i).
`QED`

By E101.031, either condition in (4.1) implies `Omega7`.

## 5. What the transform changes

The disk current does not weaken the remaining theorem.  It changes its proof
coordinate:

```text
INTEGER-COFACTOR-IDENT
 <=> local disk convergence of one coupled generating current.         (5.1)
```

This permits cancellation between all fixed integer tests to occur inside
the positive kernel `(1-q exp(-v))^(-1)`.  Estimating the secular and prime
pieces separately would discard precisely that cancellation and is not
licensed by (3.8).

## 6. Multiprecision check

At

```text
n_0=1,
q=0.4,
u=log 2,                                             (6.1)
```

direct summation of (3.5) and direct quadrature of (3.6) both give

```text
0.645499828925274091609341475235.                   (6.2)
```

Their residual at sixty decimal digits is

```text
7.78e-62.                                            (6.3)
```

This checks the factor `1/sqrt(pi)`, the power `t^(-1/2)`, and the Gaussian
scale `u^2/(4t)`.

## 7. Status

```text
proved:
  exact disk generating current for the integer cofactor defects;
  heat-trace representation of the secular side;
  Gaussian subordination of the von-Mangoldt side;
  equivalence of disk-current convergence and INTEGER-COFACTOR-IDENT;

open:
  locally uniform vanishing of the coupled current in (3.8).
```
