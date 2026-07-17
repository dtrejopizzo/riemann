# E72.396 - Cauchy-Schur projection gate

## 1. Purpose

E72.395 reduces the compact branch to a finite natural-height nodal system.  A tempting next step is
to treat lower-real-part zeros as perturbative after a maximal-real-part cluster is chosen.  That is
not correct in the row-normalized nodal matrix.

This note records the corrected Schur structure.  The remaining finite assertion is not a real-part
gap estimate.  It is a Cauchy projection identity: the critical-line forcing must be annihilated by
the off-line Cauchy Schur complement.

## 2. Row-normalized nodal system

For every positive-real-part shifted zero representative `a`, E72.395 gives

```text
sum_{w in W_L} N^M_{a,w}(L)G_x(w)=O(L^B).
```

For the complete-mesh leading part,

```text
N^infty_{a,w}(L)= -e^(aL)/(a+w)+ lower terms.
```

Row-normalize by `e^(-aL)`.  Then for off-line rows:

```text
sum_{w in W_L} C(a,w)G_x(w) = O(e^(-aL)L^B)+lower,    (1)
```

where

```text
C(a,w)=1/(a+w)
```

with the Hermite/confluent convention when needed.

The crucial point is that after row-normalization **all columns have the same Cauchy size**.  A zero
with smaller positive real part is not automatically perturbative.  A critical-line zero is not
perturbative either, since `G_x(i gamma)` is only known to be polynomial.

## 3. Split into off-line and critical columns

Let

```text
O_L={w in W_L : Re w>0},
K_L={w in W_L : Re w=0}.
```

The row-normalized off-line equations have the finite form

```text
C_OO G_O + C_OK G_K = Small_O + E_tail,               (2)
```

where:

```text
C_OO(a,b)=1/(a+b),        a,b in O_L,
C_OK(a,k)=1/(a+k),        a in O_L, k in K_L.
```

E72.324--E72.325 imply that `C_OO` is invertible for every finite off-line window in the positive
shifted half-plane.  E72.392 makes `E_tail` perturbative after choosing polynomial mesh cutoff large
enough relative to `||C_OO^(-1)||`.

Solving (2) gives

```text
G_O = - C_OO^(-1) C_OK G_K
      + C_OO^(-1)(Small_O+E_tail).                    (3)
```

Therefore off-line nodal suppression is equivalent to the finite projection identity

```text
PROJ-K:
C_OO^(-1) C_OK G_K = O(e^(-Re O L)L^B).               (4)
```

Without (4), the right side of (3) is merely polynomial, not exponentially suppressed.

## 4. Why this is not optional

The earlier fixed-height Cauchy-block argument was sound only after assuming the error/remainder in
the off-line rows is polynomial **before row-normalization by the exponential block**.  In the
natural-height row-normalized system, critical-line columns produce polynomial data in (2), and this
data is not killed by Cauchy invertibility alone.

Thus the finite theorem left by Phase 72 is sharper:

```text
not:  C_OO invertible;
but:  C_OO invertible and the critical nodal vector lies in the exponentially small Cauchy
      projection kernel seen from O_L.
```

This is exactly where arithmetic must still enter.

## 5. Explicit finite criterion

For each natural-height window define

```text
Pi_{O<-K}(L):=C_OO^(-1)C_OK.
```

The remaining criterion is:

```text
NAT-PROJ:
|| Pi_{O<-K}(L) G_K ||_{exp}
<= L^B,
```

where

```text
||G_O||_{exp}:=max_{a in O_L} e^(Re a L)|G_O(a)|.
```

Equivalently,

```text
max_{a in O_L} e^(Re a L)
 |(C_OO^(-1)C_OKG_K)_a| <= L^B.                       (5)
```

This is finite and explicitly computable from:

```text
1. the shifted zero window W_L;
2. the Cauchy matrices C_OO, C_OK;
3. the critical-line values G_x(k), computed from the finite CCM pole-even vector.
```

No outside zero sum remains after E72.394.  No finite Fourier tail remains after E72.391--E72.392.

## 6. The corrected theorem

### Theorem 72.396

Assume:

1. high outside-zero tail is closed by E72.394;
2. finite Fourier tail is absorbed by E72.391--E72.392;
3. the finite projection condition `NAT-PROJ` holds in the natural-height window.

Then all off-line nodal values in the natural-height window satisfy

```text
G_x(a)=O(e^(-Re a L)L^B).
```

Consequently the `OFF-NODAL` hypothesis of E72.326 holds.

### Proof

Use the row-normalized system (2).  Invert `C_OO`, which is allowed by the Cauchy determinant and its
confluent version.  The tail term is perturbative by E72.392 after the polynomial cutoff is chosen so
that `||C_OO^(-1)||L^2/M^2=o(1)`.  The outside high tail is polynomial by E72.394 and becomes
exponentially small after row-normalization.  The remaining contribution is exactly
`C_OO^(-1)C_OKG_K`; by `NAT-PROJ` it is exponentially small in the weighted norm.  This proves the
claim. `QED`

## 7. Status

```text
corrected: lower-real-part couplings are not automatically perturbative;
proved: off-line suppression reduces to the finite Cauchy projection condition NAT-PROJ;
open:   prove NAT-PROJ from the finite CCM/Feshbach construction, or certify it as the final finite
        identity equivalent to the remaining scalar WRL obstruction.
```

