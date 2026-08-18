# E80.002 - Independent finite Euler--Gamma product

## 1. Definition

On the half-plane

```text
D = {s in C : Re s>1},
```

define

```text
E_L(s)
  = s^2(s-1)^2 pi^{-s} Gamma(s/2)^2
    exp(2 sum_{2<=n<=exp(L)} Lambda(n)n^{-s}/log n).    (1.1)
```

The sum is finite.  Thus `E_L` is constructed from the pole factors, the
archimedean Gamma factor and a finite list of prime-power weights.  It contains
no zero of `Xi` and no finite CCM spectral datum.

## 2. Zero-free holomorphy

### Proposition 2.1

`E_L` is holomorphic and zero-free on `D`.

### Proof

On `D`, neither `s` nor `s-1` vanishes.  The Gamma function is holomorphic and
zero-free there, `pi^{-s}` is an exponential, and the last factor in (1.1) is
the exponential of an entire Dirichlet polynomial.  Every factor is therefore
holomorphic and nonzero on `D`.  Their product has the same properties. `QED`

## 3. Exact logarithmic derivative

Put

```text
A(s) = 2/s + 2/(s-1) - log pi + psi(s/2),              (3.1)
H_L(s) = A(s) - 2 sum_{2<=n<=exp(L)} Lambda(n)n^{-s}.  (3.2)
```

### Theorem 3.1

For every `s in D`,

```text
E_L'(s)/E_L(s) = H_L(s).                               (3.3)
```

### Proof

Differentiate the logarithm of (1.1).  The first four factors give

```text
2/s + 2/(s-1) - log pi + psi(s/2).
```

For each `n`,

```text
d/ds [2 Lambda(n)n^{-s}/log n] = -2 Lambda(n)n^{-s}.
```

The sum is finite, so differentiation term by term is exact.  Adding the
terms gives (3.3). `QED`

## 4. Outer limit

Let

```text
xi(s) = (1/2)s(s-1)pi^{-s/2}Gamma(s/2)zeta(s).          (4.1)
```

### Theorem 4.1

Locally uniformly on `D`,

```text
E_L(s) -> [2 xi(s)]^2                                  (4.2)
```

as `L->infinity`.

### Proof

Absolute Euler convergence on `D` gives

```text
log zeta(s)
  = sum_{n>=2} Lambda(n)n^{-s}/log n.                  (4.3)
```

Let `K` be compact in `D` and choose `delta>0` with
`Re s>=1+delta` on `K`.  Since

```text
0 <= Lambda(n)/log n <= 1
```

for every `n>=2`,

```text
sup_{s in K}
 sum_{n>exp(L)} |Lambda(n)n^{-s}/log n|
 <= sum_{n>exp(L)} n^{-1-delta}
 <= C_delta exp(-delta L).                            (4.4)
```

Hence the exponent in (1.1) converges locally uniformly to
`2 log zeta(s)`.  Exponentiation preserves local uniform convergence.  The
remaining factors satisfy

```text
s^2(s-1)^2 pi^{-s}Gamma(s/2)^2 zeta(s)^2 = [2xi(s)]^2.
```

This proves (4.2). `QED`

### Corollary 4.2

Locally uniformly on `D`,

```text
H_L(s) -> 2 xi'(s)/xi(s).                             (4.5)
```

### Proof

The quantitative tail bound (4.4), after multiplication by `log n`, is not
the needed estimate for derivatives; instead use (3.2) directly and the
absolutely convergent identity

```text
-zeta'(s)/zeta(s) = sum_{n>=2} Lambda(n)n^{-s}.
```

Uniform convergence on compact subsets of `D` follows from the standard
Dirichlet-series estimate there.  Combining with the logarithmic derivative of
(4.1) gives (4.5). `QED`

## 5. Independence and limitation

Theorems 3.1 and 4.1 construct the exact primitive required by the arithmetic
target without using zero locations.  They do not compare `E_L` with the finite
CCM characteristic.  That comparison is precisely RDI and remains open.

Thus the construction closes the primitive problem but does not close the
identification problem.

## 6. Status

```text
proved:
  E_L is holomorphic and zero-free on Re s>1;
  E_L'/E_L = H_L exactly;
  E_L -> (2xi)^2 locally uniformly;
  H_L -> 2xi'/xi locally uniformly;

closed:
  construction of an independent finite Euler--Gamma primitive;

open:
  comparison of the independent primitive with the finite CCM characteristic;

next:
  prove the exact equivalence between that comparison and SAFE-GAMMA-IDENT.
```

