# E73.072 - Paired packet gate

## 1. Correction of the packet endpoint

E73.070 used the unpaired notation

```text
ZPacket_x(z)=sum_rho M_{B_z^infty}(rho-1/2).
```

The actual finite transformed equation from E72.334 is paired under the functional equation.  In the
shifted zero variable

```text
w=rho-1/2,
Z(w)=xi(1/2+w),
```

zeros occur symmetrically under `w -> -w`, and the finite packet enters through

```text
Pair_z^M(w):=M_z^M(w)+M_z^M(-w).
```

Thus the load-bearing packet object is not the raw one-sided sum.  It is

```text
sum_{w in Div(Z)/+-} Pair_z^M(w).
```

This is the normalization used by E72.334--E72.340.

## 2. Exact finite packet equation

With endpoint normalization absorbed into

```text
Lambda_L=mu+e_pole-2kappa_L,
```

E72.334 gives the exact finite identity

```text
Lambda_L G_x(z)
= sum_{w in Div(Z)/+-} Pair_z^M(w).                  (1)
```

Here

```text
M_z^M(w)=M_z^infty(w)-M_z^tail(w).
```

Choose a finite paired zero window `W_T`.  Then

```text
Lambda_L G_x(z)
= sum_{w in W_T/+-} Pair_z^M(w) + Rem_T^M(z),         (2)
```

where

```text
Rem_T^M(z):=sum_{w notin W_T/+-} Pair_z^M(w).
```

E72.340 identifies `Rem_T^M` with the balanced finite explicit-formula remainder

```text
BER_T^M(z)
= Arch_L(B_z^M)
 - sum_{n<=e^L} Lambda(n)n^(-1/2)B_z^M(log n)
 - sum_{w in W_T/+-} Pair_z^M(w).                    (3)
```

This is finite once `W_T` is fixed.

## 3. Paired ROW-MAIN theorem

Let

```text
W_k(A,L)=Pref_k(A,L)/|Lambda_L|.
```

For the FAR3 nodes `z_k=i gamma_k`, the following paired estimate implies `ROW-MAIN-5`:

```text
PAIRED-PACKET-ROW-5:
sum_{gamma_k in FAR3(A,L)}
W_k(A,L)
| sum_{w in W_T/+-} Pair_{z_k}^M(w) + Rem_T^M(z_k) |
<= C L^-5.                                           (4)
```

Proof.  Equation (2) gives

```text
G_x(z_k)=Lambda_L^-1
 [ sum_{w in W_T/+-} Pair_{z_k}^M(w) + Rem_T^M(z_k) ].
```

Multiplying by `Pref_k(A,L)` and summing over FAR3 gives (4), which is exactly `ROW-MAIN-5`.

## 4. Finite balanced version

Using (3), (4) is equivalent to:

```text
BALANCED-PACKET-ROW-5:
sum_{gamma_k in FAR3(A,L)}
W_k(A,L)
| Arch_L(B_{z_k}^M)
  - sum_{n<=e^L} Lambda(n)n^(-1/2)B_{z_k}^M(log n) |
<= C L^-5.                                           (5)
```

This is the key finite identity: the explicit zero window cancels out after substitution.

Equation (5) contains no infinite zero sum.  It is a coupled archimedean-prime packet functional
attached to the actual finite CCM packet.

## 5. Why this is better than E73.070

E73.070 was correct as a sufficient unpaired formulation, but it is not the strongest algebraic
form.  The paired gate is better because:

```text
1. it uses the functional equation symmetry w -> -w;
2. it matches the actual finite equation E72.334;
3. it replaces the infinite zero sum by the finite balanced functional (5);
4. it keeps the prime and archimedean pieces coupled.
```

Thus the new endpoint is not:

```text
bound sum_rho M_z(w_rho) directly.
```

It is:

```text
prove BALANCED-PACKET-ROW-5 for the actual finite packet B_z^M.
```

## 6. Remaining work

The missing analytic theorem is now:

```text
BALANCED-PACKET-ROW-5:
the weighted FAR3 balanced packet functional is O(L^-5).
```

This is finite, explicit, and avoids the incoherent `L1` ceiling.  It is the current sharp form of
the Mellin spectral divisibility gate.

## 7. Status

```text
proved: paired packet equation implies ROW-MAIN-5;
proved: balanced explicit-formula remainder removes the infinite zero sum;
new endpoint: BALANCED-PACKET-ROW-5;
open: prove the coupled archimedean-prime packet bound for B_z^M.
```
