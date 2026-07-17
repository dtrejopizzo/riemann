# E72.29 -- Rank-one formula for the bordered trace estimate

**Date:** 2026-07-08.
**Role:** compute the bordered trace estimate `(BTE)` from E72.28 and determine whether it is genuinely
weaker than vector convergence.

## 0. Same pole mesh model

Assume the actual and model bordered pencils use the same pole mesh `D_x` and the same lower-left
vector `1_x`, but different top-row vectors:

```text
B_x(s)  = [ 0        xi_x^T ]
          [ 1_x      R_x(s) ],

B_x^0(s)= [ 0        k_x^T  ]
          [ 1_x      R_x(s) ],

R_x(s)=sI-D_x.
```

Put

```text
delta_x := xi_x-k_x,
m_x^0(s):=k_x^T R_x(s)^(-1)1_x.
```

Then

```text
B_x-B_x^0 = [ 0        delta_x^T ]
            [ 0        0          ],
```

a rank-one border perturbation.

## 1. Inverse of the model bordered pencil

Solving

```text
B_x^0(s) [u;v] = [alpha;w]
```

gives

```text
v = R_x(s)^(-1)(w-1_x u),
u = ( k_x^T R_x(s)^(-1)w - alpha ) / m_x^0(s).
```

This formula is valid when

```text
m_x^0(s) != 0
```

and `s` is off the pole mesh.

## 2. Relative perturbation

The relative perturbation is

```text
K_x(s)=(B_x-B_x^0)(B_x^0(s))^(-1).
```

It maps `[alpha;w]` to

```text
[ delta_x^T v ; 0 ].
```

Therefore it has rank at most one, and its trace norm equals the operator norm of the scalar
functional

```text
L_x(s)[alpha,w]
 = delta_x^T R_x(s)^(-1)w
   - delta_x^T R_x(s)^(-1)1_x
     ( k_x^T R_x(s)^(-1)w - alpha )/m_x^0(s).     (L)
```

## 3. Basic bound

On the horizontal line `Im s=eta != 0`,

```text
||R_x(s)^(-1)|| <= 1/|eta|.
```

Hence

```text
||K_x(s)||_1
 <= C_eta
    ||delta_x|| *
    ( 1 + ||1_x|| ||k_x||/(|eta| |m_x^0(s)|) )
```

in the ambient finite Hilbert norm.

If `m_x^0(s)` is bounded away from zero on the compact under consideration, then:

```text
||delta_x|| -> 0  =>  sup_s ||K_x(s)||_1 -> 0.     (BTE-from-vector)
```

## 4. Consequence

In the same-mesh, same-lower-vector gauge, BTE follows from vector convergence

```text
xi_x -> k_x.
```

But the rank-one formula also shows that trace-norm BTE is not obviously weaker: the operator norm of
`L_x(s)` tests `delta_x` against a whole resolvent-generated family. Uniformly over the full bordered
space, this is close to a resolvent-weighted vector norm.

Therefore, if we demand full trace norm, we may have returned to the Phase 72 leakage/vector problem.

## 5. Weaker current norm

The determinant current does not require the full trace norm of `K_x`; it requires convergence of

```text
Tr((I+K_x)^(-1)K_x')
```

on two heights. For rank-one `K_x`, this depends only on the scalar Fredholm factor

```text
1 + L_x(s)e_0,
```

where `e_0` is the top bordered basis vector.

Thus the genuinely weaker target is not full BTE but:

### Scalar Bordered Factor Convergence

```text
L_x(s)e_0 -> 0
```

and the corresponding derivative convergence on two heights.

Using `(L)` with `[alpha,w]=e_0=[1,0]`,

```text
L_x(s)e_0
 = delta_x^T R_x(s)^(-1)1_x / m_x^0(s).          (SBF)
```

So the scalar bordered target is:

```text
delta_x^T (sI-D_x)^(-1)1_x -> 0                  (SB)
```

on two interior heights, after model normalization.

This is exactly convergence of the Weyl transform of the vector difference, not full vector norm.

## 6. New endpoint

The sharpest non-circular estimate is now:

### Weyl-weak ground convergence

For two interior heights and compactly supported tests in `t`,

```text
int varphi(t)
  (xi_x-k_x)^T (t+i eta-D_x)^(-1)1_x dt -> 0,
```

with the corresponding derivative estimate.

This is weaker than `||xi_x-k_x||->0` and directly tailored to divisor currents.

## 7. Status

```text
proved: full trace BTE follows from vector convergence and is probably too strong;
proved: scalar bordered current convergence reduces to a Weyl-weak transform of xi_x-k_x;
open:   prove Weyl-weak ground convergence from CCM data.
```

The route has now reached its weakest honest analytic target.
