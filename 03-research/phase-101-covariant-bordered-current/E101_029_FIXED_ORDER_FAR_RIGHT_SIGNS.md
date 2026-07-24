# E101.029 - Fixed-order far-right signs

## 1. Safe asymptotic

Let

```text
g_Xi(x)
 ={1/sqrt(x)}Xi'(1/2+sqrt(x))/Xi(1/2+sqrt(x)).        (1.1)
```

Stirling's expansion for the digamma term and absolute convergence of the
prime series give, with all fixed-order derivatives,

```text
g_Xi(x)
 ={log x-2log(2 pi)}/{4 sqrt(x)}+O(x^(-1))           (1.2)
```

as `x->infinity`.

## 2. Derivative asymptotic

For every fixed integer `k>=0`, define

```text
H_k^(1/2)=sum_(j=0)^(k-1)1/(j+1/2),
H_0^(1/2)=0.                                         (2.1)
```

Differentiating (1.2) gives

```text
(-1)^k g_Xi^(k)(x)
 ={(1/2)_k}/{4 x^(k+1/2)}
   [log x-2log(2 pi)-H_k^(1/2)]
  +O_k(x^(-k-1)).                                    (2.2)
```

### Proof

The identity

```text
d^k/dx^k[x^(-1/2)log x]
 =(-1)^k(1/2)_k x^(-k-1/2)
  [log x-H_k^(1/2)]                                  (2.3)
```

follows by differentiating the parameter formula for `x^(-a)` at `a=1/2`.
The complete digamma expansion may be differentiated a fixed number of times,
and the von Mangoldt series and all its fixed derivatives are exponentially
small in `sqrt(x)`.  This proves (2.2). `QED`

## 3. Fixed-order theorem

### Theorem 3.1

For every fixed `k>=0`, there exists `X_k` such that

```text
(-1)^k g_Xi^(k)(x)>0
for all x>=X_k.                                      (3.1)
```

### Proof

For fixed `k`, the bracket in (2.2) tends to infinity, while the error is
smaller than the main term by `O_k(1/(sqrt(x)log x))`. `QED`

## 4. Quantifier wall

The Hausdorff closure theorem E101.028 requires all derivative moments at one
fixed safe point.  Theorem 3.1 has the different quantifiers

```text
for every k there exists X_k such that the sign holds beyond X_k.   (4.1)
```

It does not give

```text
there exists x_0 such that every k-sign holds at x_0.               (4.2)
```

Moving `x` beyond `X_k` as `k` grows is another far-right drift and loses the
fixed determining point required by E101.023.  Thus every finite initial
segment of the derivative-sign hierarchy is unconditional sufficiently far
right, while the full hierarchy at one point remains the RH-strength step.

## 5. Status

```text
proved:
  differentiated safe asymptotic;
  eventual Stieltjes sign at every fixed derivative order;

closed as insufficient:
  passage from order-dependent far-right thresholds to one fixed point;

open:
  the simultaneous infinite Hausdorff hierarchy at a fixed safe point.
```

