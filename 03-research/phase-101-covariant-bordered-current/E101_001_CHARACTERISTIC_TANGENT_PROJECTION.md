# E101.001 - Characteristic tangent projection

## 1. Simple characteristic point

Let

```text
K=H-mu I,
chi(H,mu)=det K,                                     (1.1)
```

and assume

```text
det K=0,
chi_mu=partial_mu chi !=0.                           (1.2)
```

Define

```text
G=adj(K)/chi_mu.                                     (1.3)
```

Since `partial_mu K=-I`,

```text
chi_mu=-Tr(adj K),
Tr G=-1.                                             (1.4)
```

## 2. Horizontal projection

For every matrix direction `Y`, put

```text
Hor_K(Y)=Y+Tr(GY)I.                                  (2.1)
```

### Theorem 2.1

The map `Hor_K` is a projection with

```text
range Hor_K={V:Tr(adj(K)V)=0},
kernel Hor_K=span{I}.                                (2.2)
```

Thus its range is exactly the tangent hyperplane to `det K=0` at `K`.

### Proof

Write `c=Tr(GY)`.  From `Tr G=-1`,

```text
Tr[G Hor_K(Y)]
 =Tr(GY)+c Tr G
 =c-c=0.                                             (2.3)
```

Multiplication by the nonzero scalar `chi_mu` shows that `Hor_K(Y)` lies in
the hyperplane in (2.2).  Applying (2.1) again and using (2.3) gives

```text
Hor_K(Hor_K(Y))=Hor_K(Y).                            (2.4)
```

Also `Hor_K(I)=0`.  Conversely, if `Hor_K(Y)=0`, then `Y` is a scalar
multiple of `I`.  The range of a projection is the kernel of its complementary
linear functional, proving (2.2). `QED`

## 3. Spectral form

If `K` is real symmetric, E100.001 gives `G=-Pi`, where `Pi` projects onto
`ker K`.  Therefore

```text
Hor_K(Y)=Y-Tr(Pi Y)I.                                (3.1)
```

No reduced resolvent, eigenvalue gap or eigenvector normalization occurs.

## 4. Status

```text
proved:
  canonical characteristic tangent projection;
  exact range and kernel;
  signed spectral form.
```

