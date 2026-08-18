# E101.037 - Finite heat-order wall

## 1. Explicit derivative hierarchy

For `u>0`, set

```text
phi_u(v)=v^(-1/2)exp(-u^2/(4v)).                    (1.1)
```

The Gaussian prime source of E101.036 is a positive weighted sum of these
functions.  For every `j>=0`,

```text
(-1)^j partial_v^j phi_u(v)
 =j! v^(-j-1/2)exp(-u^2/(4v))
   L_j^(-1/2)(u^2/(4v)),                             (1.2)
```

where `L_j^(-1/2)` is the generalized Laguerre polynomial.

### Proof

The standard Rodrigues identity, applied after the substitution
`w=u^2/(4v)`, gives

```text
partial_v^j[v^(-beta)exp(-a/v)]
 =(-1)^j j!v^(-beta-j)exp(-a/v)
   L_j^(beta-1)(a/v).                                (1.3)
```

Take `beta=1/2` and `a=u^2/4`. `QED`

Consequently, the order-`j` prime side of the heat discriminant is

```text
(-1)^j P^(j)(v)
 ={j!/(sqrt(pi)v^(j+1/2))}
  sum_(m>=2)Lambda(m)m^(-1/2)
   exp(-(log m)^2/(4v))
   L_j^(-1/2)((log m)^2/(4v)).                       (1.4)
```

The Laguerre factor changes sign.  Positivity of the weights in (1.4) does
not settle the sign of any higher derivative.

## 2. No finite truncation can imply complete monotonicity

### Theorem 2.1

For every finite `J>=0`, there is a real smooth function `H_J` on
`[0,infinity)` such that

```text
(-1)^j H_J^(j)(v)>0
for 0<=j<=J and every v>=0,                          (2.1)
```

but `H_J` is not completely monotone.

### Proof

Fix `T>0` and put

```text
alpha=-3T/2-i(3sqrt(3)T/2),
-alpha=3T exp(i pi/3).                               (2.2)
```

Choose

```text
0<epsilon<1/(4 times 3^J),                           (2.3)
```

and define

```text
H_J(v)=exp(-Tv)+2epsilon Re exp(alpha v).            (2.4)
```

For `0<=j<=J`,

```text
(-1)^j H_J^(j)(v)
 =T^j exp(-Tv)
  +2epsilon Re[(-alpha)^j exp(alpha v)]              (2.5)

 >=T^j exp(-Tv)
   [1-2epsilon 3^j exp(-Tv/2)]

 >={1/2}T^j exp(-Tv)>0.                              (2.6)
```

Now choose arbitrarily large integers `ell>J` with

```text
ell=2, 3, or 4 modulo 6.                             (2.7)
```

For those indices,

```text
Re[(-alpha)^ell]
 =3^ell T^ell cos(ell pi/3)<0.                       (2.8)
```

Since `epsilon 3^ell` is unbounded, one such `ell` satisfies

```text
(-1)^ell H_J^(ell)(0)<0.                             (2.9)
```

Thus (2.1) holds while complete monotonicity fails. `QED`

## 3. Interpretation of the model

The first term in (2.4) is a positive real-rate heat mode.  The second is a
conjugate nonreal-rate pair.  By reducing its amplitude, the pair becomes
invisible to any prescribed finite initial set of derivative inequalities,
but its factor `|alpha|^j` forces detection at a later order.

This is the heat-coordinate analogue of the geometric amplification of one
off-line zero in the Li coefficients.  It proves that no theorem of the form

```text
verify (5.1) of E101.036 only for j<=J
 =>Omega7                                               (3.1)
```

can hold for a fixed finite `J` without an additional structure theorem that
propagates those signs to every order.

## 4. Proof-search consequence

A valid closure must supply at least one of the following:

```text
1. one positive-measure representation of H_Xi;
2. a total-positivity theorem propagating all heat orders;
3. a coupled cofactor limit which imports complete monotonicity from the
   finite real-rooted approximants.                  (4.1)
```

Separate verification of finitely many Laguerre-weighted prime inequalities
is diagnostic only.

## 5. Status

```text
proved:
  exact Laguerre formula for every heat derivative of the prime source;
  global counterexample to every finite derivative truncation;
  necessity of an all-order propagation or positive-measure theorem;

open:
  an all-order arithmetic mechanism for H_Xi.
```
