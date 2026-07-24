# E101.020 - Safe Stieltjes transform

## 1. Squared safe variable

For a normalized finite core bilateral characteristic, put

```text
x=sigma^2,
g_alpha(x)
 =d/dx log Theta_alpha(i sqrt(x)).                   (1.1)
```

Its canonical product gives

```text
g_alpha(x)
 =sum_j 1/[x+r_(alpha,j)^2]
 =integral_[0,infinity) d mu_alpha(t)/(x+t),         (1.2)

mu_alpha=sum_j delta_(r_(alpha,j)^2).                (1.3)
```

Thus `g_alpha` is a Stieltjes transform of a positive finite discrete measure.
The raw family has in addition the explicit external lattice measure of
E101.025.

## 2. Target transform in the absolute region

Let

```text
sigma=sqrt(x),
s=1/2+sigma.                                         (2.1)
```

For the normalized square of the completed function, define

```text
g_Xi(x)
 =d/dx log[Xi(1/2+sqrt(x))^2]
 ={1/sigma}Xi'(s)/Xi(s).                             (2.2)
```

Using

```text
Xi(s)=const s(s-1)pi^(-s/2)Gamma(s/2)zeta(s),        (2.3)
```

one obtains, for `s>1`,

```text
g_Xi(x)
 ={1/sigma}{
    1/s+1/(s-1)-(1/2)log pi+(1/2)psi(s/2)
    -sum_(n>=2)Lambda(n)n^(-s)
  }.                                                 (2.4)
```

The prime series is absolutely convergent.  Equation (2.4) contains no zero
list.

## 3. Equivalence with local identification

### Theorem 3.1

On a safe interval, `LOCAL-COVARIANT-IDENT` is equivalent to

```text
g_alpha(x)->g_Xi(x)                                  (3.1)
```

locally uniformly in the corresponding `x` interval, together with the fixed
normalization at one point.

### Proof

Local identification bounds one second safe value.  By E101.018, the family
of canonical products is locally bounded on the plane.  Analytic convergence
then permits differentiation and gives (3.1).

Conversely, integrate (3.1) between the normalization point and any point in
the interval.  The integration constant is fixed by `Theta_alpha(i sigma_0)=1`.
This recovers local identification. `QED`

## 4. Moment expansion

At a fixed safe `x_0`, define

```text
m_(alpha,k)
 =sum_j 1/[x_0+r_(alpha,j)^2]^(k+1).                 (4.1)
```

Then

```text
(-1)^k g_alpha^(k)(x_0)=k! m_(alpha,k)>=0,           (4.2)
```

and, for `|x-x_0|<x_0`,

```text
log[Theta_alpha(i sqrt(x))/Theta_alpha(i sqrt(x_0))]
 =sum_(k>=1)(-1)^(k+1)
   (x-x_0)^k m_(alpha,k-1)/k.                        (4.3)
```

The first moment is the compactness scalar of E101.012.  The full hierarchy
is the local identification data.

## 5. Status

```text
proved:
  positive Stieltjes representation of every finite approximant;
  explicit arithmetic Euler--Gamma target transform;
  equivalence of transform convergence and local covariant identification;
  exact safe moment hierarchy.
```
