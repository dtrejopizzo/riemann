# E101.014 - Exact Stieltjes mesh cancellation

## 1. Right boundary transfer

Let the Fourier mesh be

```text
d_k=2 pi k/L.                                        (1.1)
```

For the right boundary completion at `k=N`, the transfer has poles at

```text
P_N={d_k:-N+1<=k<=N}.                                (1.2)
```

Write its real zeros, with multiplicity, as `kappa_j`.  The exact
spectral-shift formula of E78.152 is

```text
T_N'(z)/T_N(z)
 =sum_j 1/(z-kappa_j)
  -sum_(-N+1<=k<=N)1/(z-d_k).                        (1.3)
```

The identity is interpreted by continuity if the leading coefficient drops
and one zero moves to infinity.

## 2. Secular Stieltjes mass

At `z=i sigma`, `sigma>0`, taking the real part after multiplication by `i`
gives

```text
sum_j 1/(kappa_j^2+sigma^2)
 =sum_(-N+1<=k<=N)1/(d_k^2+sigma^2)
  +(1/sigma)Re{i T_N'(i sigma)/T_N(i sigma)}.         (2.1)
```

No estimate has been used.

## 3. Entire bilateral characteristic

Set

```text
Phi_(+,N)(z)=const_N sin(zL/2)T_N(z),
Psi_N(z)=Phi_(+,N)(z)Phi_(+,N)(-z).                  (3.1)
```

The sine zeros at the poles in (1.2) are cancelled.  The bilateral residual
lattice consists of

```text
one pair at d_N and -d_N;
two pairs at d_k and -d_k for every k>N.             (3.2)
```

Consequently its contribution to the canonical Stieltjes mass is

```text
R_(L,N)(sigma)
 =1/(d_N^2+sigma^2)
  +2 sum_(k>N)1/(d_k^2+sigma^2).                     (3.3)
```

The mesh poles and residual zeros partition the full lattice:

```text
sum_(-N+1<=k<=N)1/(d_k^2+sigma^2)
 +R_(L,N)(sigma)
 =sum_(k in Z)1/(d_k^2+sigma^2).                    (3.4)
```

## 4. Exact cancellation theorem

Let `M^raw_(L,N)(sigma)` be the canonical Stieltjes mass of the raw `Psi_N`.
Combining
(2.1)--(3.4) yields

```text
M^raw_(L,N)(sigma)
 =sum_(k in Z)1/(d_k^2+sigma^2)
  +(1/sigma)Re{i T_N'(i sigma)/T_N(i sigma)}.         (4.1)
```

The Mittag--Leffler expansion of `coth` gives

```text
sum_(k in Z)1/[(2 pi k/L)^2+sigma^2]
 ={L/(2 sigma)}coth(sigma L/2).                      (4.2)
```

Therefore

```text
M^raw_(L,N)(sigma)
 ={1/sigma}{
    (L/2)coth(sigma L/2)
    +Re[i T_N'(i sigma)/T_N(i sigma)]
  }.                                                 (4.3)
```

This is exact for the raw family at every finite `L,N`.  In particular, no
condition such as
`N/L^2->infinity` is needed to dispose of the sine tail; the tail cancels
the omitted mesh mass algebraically inside the raw mass formula.  The direct
anchor uses the core family; its separate formula is E101.025(3.5).

## 5. Root-free form

If `F_N(z)=(z-d_N)T_N(z)` is represented by the bordered determinant of
E78.152, then

```text
T_N'/T_N=F_N'/F_N-1/(z-d_N).                         (5.1)
```

Both terms at `z=i sigma` are safe cofactor ratios.  Hence (4.3) computes the
complete zero mass without finding a zero or using a spectral location.

## 6. Status

```text
proved:
  exact secular Stieltjes identity;
  exact bilateral residual-lattice ledger;
  complete cancellation of the finite mesh boundary;
  root-free cofactor formula for the raw total mass.
```
