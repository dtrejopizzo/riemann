# E72.343 -- Signed tail finite collapse

**Purpose.** Remove the last infinite Fourier tail from the CFIR target.  The signed window tail of
E72.342 can be written as complete Fourier mesh minus active finite mesh.  The complete mesh is already
known in closed form from E72.318, so the tail becomes a finite, explicit, verifiable expression.

## 1. Basis packet

For one active index `n`, define the complete transformed basis packet

```text
KQ_z^infty(y;n)
= i/(z+i d_n)
   [ e^(z(L-y)) - e^(i d_n y)
     + e^(zL)e^(-i d_n y) - e^(zy) ].                (1)
```

This is E72.318(5).  For a shifted zero representative `a`, set

```text
P_{z,n}^infty(a)
:= int_0^L (e^(ay)+e^(-ay))KQ_z^infty(y;n)dy.        (2)
```

Let

```text
E_L(lambda):=(e^(lambda L)-1)/lambda,
```

with the removable value `E_L(0)=L`.  Substituting (1) gives the closed formula

```text
P_{z,n}^infty(a)
= i/(z+i d_n) [
   e^(zL)( E_L(a-z)+E_L(-a-z) )
 - ( E_L(a+i d_n)+E_L(-a+i d_n) )
 + e^(zL)( E_L(a-i d_n)+E_L(-a-i d_n) )
 - ( E_L(a+z)+E_L(-a+z) )
].                                                     (3)
```

No infinite series remains in (3).

## 2. Active mesh packet

For the active finite mesh `|m|<=M`, put

```text
a_m(z):=(1-e^(zL))/(iz-d_m),
Phi_a(d):=d/(a^2+d^2).
```

E72.333 gives, for `m != n`,

```text
M_{m,n}(a)+M_{m,n}(-a)
= [2-e^(aL)-e^(-aL)]
   [Phi_a(d_m)-Phi_a(d_n)]/[pi(n-m)].                (4)
```

For `m=n`, the value is obtained either from the original cell

```text
Q_y(n,n)=2(1-y/L)cos(d_n y),
```

or as the removable limit of (4).  Denote the result by `PairCell_{m,n}(a)`.

Then the active paired basis packet is the finite sum

```text
P_{z,n}^M(a)
:= sum_{|m|<=M} a_m(z) PairCell_{m,n}(a).             (5)
```

## 3. Tail collapse identity

The signed tail basis is

```text
TailBasis_{z,n}^M(a):=P_{z,n}^infty(a)-P_{z,n}^M(a).  (6)
```

This is exactly the outside-mesh sum:

```text
TailBasis_{z,n}^M(a)
= sum_{|m|>M} a_m(z)[M_{m,n}(a)+M_{m,n}(-a)].         (7)
```

The proof is just the decomposition of the complete Fourier mesh into active and outside indices,
using E72.318 for the complete side and E72.333 for the cell Mellin transform.

## 4. Finite formula for the window tail

The window tail from E72.342 becomes

```text
Tail_T^M(z)
= sum_{j=1}^J m_j sum_{n active} xi_n TailBasis_{z,n}^M(a_j).      (8)
```

Equations (3), (5), and (8) are finite.  The only operations are:

```text
1. evaluation of the elementary function E_L;
2. the active finite sum over |m|<=M;
3. the active finite sum over n;
4. the fixed finite zero-window sum over a_j.
```

Thus the signed tail is no longer an analytic tail estimate.  It is an explicit finite expression.

## 5. Updated CFIR endpoint

Insert (8) into E72.342:

```text
Def_CFIR,T
= J_T[
   T_W02(z)[xi] - T_WR(z)[xi] - T_Prime(z)[xi]
   - 2kappa_*G_x(z)
   - I_T^H G_x(z)
   + sum_j m_j sum_n xi_n TailBasis_{z,n}^M(a_j)
].
```

Every term is now finite.  Therefore the remaining theorem is not a tail theorem; it is the finite
Hermite cancellation

```text
||Def_CFIR,T|| <= C_TL^B
```

for a completely explicit vector.

## 6. Status

```text
proved: the signed outside Fourier tail equals complete closed packet minus active finite packet;
proved: Tail_T^M has the finite formula (8);
updated: FINITE-CFIR has no infinite tail left.
```
