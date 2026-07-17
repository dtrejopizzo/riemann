# E72.93 -- Finite-band Stieltjes moment criterion

**Date:** 2026-07-09.
**Role:** convert finite-band Cauchy invisibility into a finite residue/moment identity.

## 0. Input

E72.91 and E72.92 reduce finite-band root transport to:

```text
<r_s^even,phi_{x,H,tau_j}> -> 0,
```

where:

```text
r_s^even=s(s^2I-D^2)^(-1)1,
phi_{x,H,tau}=B_xC_E^(-1)B_x^*P_HZ_x(tau).
```

The vector `phi` is not norm-small enough to close the proof. The correct object is its finite-band
Cauchy transform.

## 1. Stieltjes transform of phi

For an even vector `phi`, define:

```text
M_phi(w):=sum_n phi_n w/(w^2-d_n^2).
```

With the Hilbert convention linear in the second variable:

```text
<r_s^even,phi> = M_phi(conjugate(s)).                         (ST)
```

If `phi=P_Hphi`, then only the finite set:

```text
D_H={d_n: |d_n|<=H}
```

appears. Since `phi` is even, the poles pair at `+d` and `-d`. Grouping pairs gives:

```text
M_phi(w)
 = phi_0/w + sum_{0<d<=H} 2w Phi_d/(w^2-d^2),                (PAIR)
```

where:

```text
Phi_d = phi_n  for the pair d=|d_n|
```

after even normalization.

## 2. Residue criterion

For a fixed finite band, the following are equivalent:

```text
M_phi(w) identically 0;
all residues of M_phi at its finite poles vanish;
phi_n=0 for every |d_n|<=H.                                  (RES)
```

This is exact but too strong for the asymptotic theorem, because `(FBRT)` only asks that the transform
vanish in the limit when tested on compact `s`-windows.

## 3. Moment criterion away from the band

For `|w|>H`, expand:

```text
w/(w^2-d^2)=sum_{m>=0} d^{2m}/w^{2m+1}.
```

Therefore:

```text
M_phi(w)=sum_{m>=0} mu_m(phi)/w^{2m+1},
mu_m(phi):=sum_n phi_n d_n^{2m}.                             (MOM)
```

For a finite band of size `J_H`, the first `J_H` moments determine `phi` on the band. Thus:

```text
mu_m(phi)=0 for 0<=m<J_H
    <=> M_phi(w) identically 0
    <=> phi=0 on the finite band.                            (MOM-FIN)
```

For the asymptotic theorem, a weaker version is enough:

```text
for each fixed H and each fixed M,
mu_m(phi_{x,H,tau_j})->0 for 0<=m<M,
```

plus tightness/no-growth in the finite physical band, implies Cauchy invisibility on compact
`s`-windows outside the real mesh by polynomial approximation of the Cauchy kernel.

## 4. Current finite identity for FBRT

Combining E72.89--E72.93, finite-band root transport is reduced to the finite moment identities:

```text
mu_m(phi_{x,H,tau_j})
 = sum_{|d_n|<=H} d_n^{2m}
   [B_xC_E^(-1)B_x^*P_HZ_x(tau_j)]_n
 -> 0.                                                       (FB-MOM)
```

for enough moments to approximate the Cauchy tests in the fixed physical band.

This is the explicit finite identity behind the finite-band root remainder.

## 5. Status

```text
proved: finite-band Cauchy invisibility is equivalent to Stieltjes/moment cancellation;
reduced: FBRT to moment cancellation of the transported vectors phi_{x,H,tau_j};
open:   prove the moment identities (FB-MOM), or find their finite algebraic source.
```
