# E101.028 - Compact resolvent moment problem

## 1. Compactification at one safe point

Fix `x_0>1/4`.  For the positive core secular measure `mu_alpha`, set

```text
u=1/(t+x_0),
0<u<=1/x_0.                                          (1.1)
```

Define a finite positive measure `eta_alpha` on `[0,1/x_0]` by

```text
integral phi(u)d eta_alpha(u)
 =integral phi(1/(t+x_0))
          d mu_alpha(t)/(t+x_0).                     (1.2)
```

Its total mass is

```text
eta_alpha([0,1/x_0])=g_alpha(x_0).                   (1.3)
```

## 2. Exact moments

For every `k>=0`,

```text
int u^k d eta_alpha(u)
 =int d mu_alpha(t)/(t+x_0)^(k+1)
 ={(-1)^k/k!}g_alpha^(k)(x_0).                       (2.1)
```

If `kappa_(alpha,j)` are the core secular roots, this is

```text
m_(alpha,k)
 =sum_j1/(kappa_(alpha,j)^2+x_0)^(k+1).              (2.2)
```

Equivalently, for the secular pencil `K_alpha`,

```text
m_(alpha,k)
 =Tr[(K_alpha^2+x_0I)^(-(k+1))],                     (2.3)
```

where the trace is understood through the real algebraic spectrum or through
the corresponding determinant derivatives.  No eigenvector occurs.

## 3. Hausdorff uniqueness theorem

### Theorem 3.1

Assume

```text
m_(alpha,k)->m_(Xi,k)
for every k>=0.                                      (3.1)
```

Then the measures `eta_alpha` converge weakly to a unique positive measure on
`[0,1/x_0]`, their Stieltjes transforms converge near `x_0`, and `Omega7`
holds.

### Proof

The case `k=0` bounds the total masses by (1.3).  Compactness of the support
gives weak-* compactness.  Every subsequential limit has the moments
`m_(Xi,k)` by (3.1).  Polynomials are dense in the continuous functions on
`[0,1/x_0]`, so the Hausdorff moment problem is determinate and all sublimits
coincide.

Expanding

```text
1/(t+x)
 =sum_(k>=0)(x_0-x)^k/(t+x_0)^(k+1)                 (3.2)
```

for `|x-x_0|<x_0` identifies the limiting transform with `g_Xi`.  E101.021
then gives `Omega7`. `QED`

## 4. Arithmetic target moments

The required target numbers are explicit derivatives in the absolute region:

```text
m_(Xi,k)
 ={(-1)^k/k!}
  d^k/dx^k [
   Xi'(1/2+sqrt(x))/(sqrt(x)Xi(1/2+sqrt(x)))
  ]_(x=x_0).                                        (4.1)
```

Using E101.020(2.4), each fixed `m_(Xi,k)` is an absolutely convergent
Gamma--von-Mangoldt expression.

## 5. Hausdorff inequalities

Put

```text
b_k=x_0^k m_(Xi,k).                                  (5.1)
```

The sequence is the moment sequence of a positive measure on `[0,1]` if and
only if

```text
(-1)^j Delta^j b_k>=0
for every j,k>=0.                                    (5.2)
```

Thus the Stieltjes discriminant can be written entirely as a countable family
of explicit safe derivative inequalities.  Proving only finitely many of
them cannot establish the representing measure.

## 6. Status

```text
proved:
  compactification of the secular measures;
  exact resolvent-trace moment formula;
  determinate Hausdorff moment closure theorem;
  explicit arithmetic target hierarchy;

open:
  convergence of the complete moment hierarchy, equivalently Omega7.
```

