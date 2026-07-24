# E101.030 - Coherence signature autopsy

## 1. The ceiling coefficient controls only an escaping root

Let `Q(z)` and `P(z)` be real polynomials with

```text
deg Q=deg P+1,
P(d_b)Q(d_b)!=0.                                    (1.1)
```

For any nonzero real sequence `c_N->0`, define

```text
R_N=d_b-Q(d_b)/[c_NP(d_b)],                          (1.2)

F_N(z)=c_N(z-R_N)P(z)/Q(z).                          (1.3)
```

Then

```text
F_N(infinity)=c_N,
F_N(d_b)=1.                                          (1.4)
```

Thus `F_N` has the normalization and leading ceiling coefficient of a
boundary transfer numerator.  However, on compact sets away from the poles
and zeros of `P`,

```text
F_N'/F_N
 =1/(z-R_N)+P'/P-Q'/Q
 ->P'/P-Q'/Q.                                        (1.5)
```

The root `R_N` escapes to infinity, while every finite zero of the arbitrary
polynomial `P` survives.

### Consequence

The condition

```text
c_N=F_N(infinity)->0                                 (1.6)
```

records one degree loss at infinity.  It does not identify the finite
logarithmic derivative or its limiting divisor.

## 2. Single-signed increments do not identify a target

Fix any `a>0` and define

```text
Theta_N^a(z)
 =product_(j=1)^N(1-z^2/(j+a)^2).                   (2.1)
```

Every `Theta_N^a` is even and real-rooted.  Its safe Stieltjes transform is

```text
g_N^a(x)=sum_(j=1)^N1/[x+(j+a)^2].                  (2.2)
```

The consecutive increment is the positive measure

```text
mu_(N+1)^a-mu_N^a=delta_((N+1+a)^2).                (2.3)
```

Hence every counting increment is single-signed and every safe transform
converges monotonically.  Nevertheless,

```text
g_N^a(x)->g^a(x)=sum_(j>=1)1/[x+(j+a)^2],            (2.4)
```

and the limit depends on the arbitrary parameter `a`.  Except for a target
chosen to equal this product, it is not `g_Xi`.

## 3. Combined insufficiency

The constructions may be combined: attach one escaping root with coefficient
`c_N->0` to any monotone real-rooted family such as (2.1).  Then both signatures

```text
ceiling coefficient tends to zero;
spectral increments are single-signed                              (3.1)
```

hold, while the finite limiting Stieltjes transform remains freely chosen.

## 4. Consequence for the proposed discriminant

The signatures isolated before Phase 80 are valuable diagnostics and may
prove convergence.  They cannot, by themselves, imply arithmetic
identification.  Any valid strengthening must add an anchor that distinguishes

```text
g_limit=g_Xi                                         (4.1)
```

from every other positive Stieltjes limit.

E101.021 shows that (4.1) is exactly the RH-strength statement.  Therefore
the proposed equivalence

```text
single-signed coherence <=> SAFE-GAMMA-IDENT         (4.2)
```

is false without an additional arithmetic identity.  The true discriminant
is `STIELTJES-IDENT`, not coherence alone.

## 5. Status

```text
proved:
  c_N->0 controls only an escaping root;
  single-signed spectral increments give convergence but not identification;
  both properties together still permit arbitrary real-rooted limits;

refuted as stated:
  identification of the arithmetic limit from the two coherence signatures
  alone;

retained:
  the signatures as convergence infrastructure and falsifier diagnostics;

open:
  the arithmetic anchor STIELTJES-IDENT.
```

