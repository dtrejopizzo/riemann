# E73.070 - Packet reduction of ROW-MAIN

## 1. Purpose

E73.066 states the sharp main target:

```text
ROW-MAIN-5:
sum_{gamma_k in FAR3(A,L)}
Pref_k(A,L) dist(k_{-gamma_k},Row(H_x-mu_x I))
<= C L^-5.
```

By the projection lemma this is

```text
sum_k Pref_k(A,L)|G_x(z_k)| <= C L^-5,
```

where `z_k=i gamma_k` up to the fixed sign convention of the Cauchy transform.

E72.317--E72.319 give an exact transformed eigenvector equation for `G_x(z)`.  This note connects
that equation directly to `ROW-MAIN-5`, so the remaining theorem becomes a packet Abel estimate
instead of a raw rowspace estimate.

## 2. Endpoint-corrected packet equation

E72.319 gives

```text
(mu+e_pole-2 kappa_L)G_x(z)
= ZPacket_x(z)-TailPacket_x(z),                       (1)
```

where

```text
ZPacket_x(z):=sum_rho M_{B_z^infty}(rho-1/2),
TailPacket_x(z):=Lcal(B_z^tail).
```

The left coefficient is the pole-even scalar gap.  Write

```text
Gap_x:=|mu+e_pole-2 kappa_L|.
```

Then

```text
|G_x(z)| <= Gap_x^-1 ( |ZPacket_x(z)|+|TailPacket_x(z)| ).       (2)
```

## 3. Direct sufficient theorem

For FAR3 nodes define

```text
W_k(A,L):=Pref_k(A,L)/Gap_x.
```

The following packet estimate implies `ROW-MAIN-5`:

```text
PACKET-ROW-5:
sum_{gamma_k in FAR3(A,L)}
W_k(A,L)
( |ZPacket_x(i gamma_k)|+|TailPacket_x(i gamma_k)| )
<= C L^-5.                                             (3)
```

Proof.  Apply (2) at each FAR3 node and multiply by `Pref_k(A,L)`.  Summing gives exactly
`ROW-MAIN-5`.

This is an analytic strengthening of the current endpoint because it uses the transformed CCM
eigenvector equation before taking absolute values.

## 4. Closed form for `M_{B_z^infty}(w)`

E72.318 gives

```text
B_z^infty(y)
= i[ (e^(z(L-y))-e^(zy))H_0(z)
     - H_+(z;y)
     + e^(zL)H_-(z;y) ],
```

with

```text
H_0(z)=sum_n xi_n/(z+i d_n),
H_+(z;y)=sum_n xi_n e^(i d_n y)/(z+i d_n),
H_-(z;y)=sum_n xi_n e^(-i d_n y)/(z+i d_n).
```

Therefore

```text
M_{B_z^infty}(w)=int_0^L e^(wy)B_z^infty(y)dy
```

equals

```text
i H_0(z)
  [ e^(zL)(e^((w-z)L)-1)/(w-z)
    - (e^((w+z)L)-1)/(w+z) ]

- i sum_n xi_n/(z+i d_n)
    (e^((w+i d_n)L)-1)/(w+i d_n)

+ i e^(zL) sum_n xi_n/(z+i d_n)
    (e^((w-i d_n)L)-1)/(w-i d_n).                    (4)
```

Removable values are interpreted by the limit

```text
(e^(aL)-1)/a -> L
```

at `a=0`.

## 5. Resonant simplification on CCM mesh

Since

```text
d_n=2 pi n/L,
```

one has

```text
e^(i d_n L)=1.
```

Thus (4) becomes

```text
M_{B_z^infty}(w)
= i(e^(wL)-e^(zL))H_0(z)/(w-z)
 - i(e^((w+z)L)-1)H_0(z)/(w+z)

 - i(e^(wL)-1) sum_n xi_n/((z+i d_n)(w+i d_n))
 + i e^(zL)(e^(wL)-1) sum_n xi_n/((z+i d_n)(w-i d_n)).
```

The first term is removable at `w=z`.

The key point is that every nontrivial-zero contribution is now a linear combination of only three
Cauchy packet sums:

```text
H_0(z),
R_+(z,w):=sum_n xi_n/((z+i d_n)(w+i d_n)),
R_-(z,w):=sum_n xi_n/((z+i d_n)(w-i d_n)).
```

## 6. New theorem target

The remaining theorem can be stated without hidden matrix language:

```text
PACKET-ZERO-FAR3:
For z=i gamma_k on FAR3(A,L),

sum_k W_k(A,L)
|sum_rho M_{B_z^infty}(rho-1/2)|
<= C L^-5.
```

together with

```text
PACKET-TAIL-FAR3:
sum_k W_k(A,L)|Lcal(B_z^tail)| <= C L^-5.
```

Then `PACKET-ROW-5`, hence `ROW-MAIN-5`, follows.

## 7. Why this is progress

The old rowspace target asked for

```text
|<xi_x,k_t>|
```

to be small directly.  The packet target rewrites this value through the finite CCM equation as a
zero-sum transform with explicit packet kernels.

This prevents the illegal step that E73.063 ruled out: taking the absolute `L1` ceiling of the
Cauchy fractions.  The cancellation is kept in

```text
sum_rho M_{B_z^infty}(rho-1/2).
```

## 8. Status

```text
proved: PACKET-ROW-5 implies ROW-MAIN-5;
proved: closed formula for M_{B_z^infty}(w);
open: prove PACKET-ZERO-FAR3 and PACKET-TAIL-FAR3 uniformly.
```
