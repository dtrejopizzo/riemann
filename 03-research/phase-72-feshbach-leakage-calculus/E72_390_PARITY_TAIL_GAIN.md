# E72.390 - Parity gain for the finite Fourier tail

## 1. Purpose

E72.331 showed that a pointwise finite Fourier tail estimate is false at polynomial cutoff.  E72.333
reduced the admissible tail theorem to the signed coefficient identity

```text
Lcal(B_z^tail)=sum_{|m|>M} a_m(z)Lcal(b_m),
a_m(z)=(1-e^(zL))/(iz-d_m).
```

The high-`m` expansion in E72.333 displayed an apparent `1/m` coefficient in `Lcal(b_m)`.  This note
proves that this leading coefficient vanishes identically by pole-even parity.  The finite Fourier
tail therefore starts one order later.

This is a real analytic gain: it does not prove `TAIL-POLY`, but it removes the first non-summable
coefficient that would otherwise force an exponentially large cutoff.

## 2. Tail coefficient recalled

For `m` outside the active mesh and `n` inside it,

```text
Lcal(b_m)
= sum_w (1-e^(wL))
   sum_n xi_n [Phi_w(d_m)-Phi_w(d_n)]/[pi(n-m)],       (1)
```

where the sum over `w` is the symmetric shifted divisor convention and

```text
Phi_w(d)=d/(w^2+d^2).
```

The pole-even data satisfy

```text
d_-n=-d_n,                 xi_-n=xi_n.                (2)
```

## 3. The apparent leading coefficient

For fixed `w` and fixed active `n`,

```text
1/(n-m)=-1/m-n/m^2+O(n^2/m^3),
```

and therefore

```text
[Phi_w(d_m)-Phi_w(d_n)]/[pi(n-m)]
= Phi_w(d_n)/(pi m)
  + [ n Phi_w(d_n)-Phi_w(d_m)m ]/(pi m^2)
  + O_w((1+n^2)(|Phi_w(d_m)|+|Phi_w(d_n)|)/m^3).      (3)
```

Only the first displayed term can produce the dangerous `1/m` coefficient after summing over `n`.
Its coefficient is

```text
S_1(w):=sum_n xi_n Phi_w(d_n).                         (4)
```

## 4. Parity cancellation

Since `Phi_w(d)` is odd in `d`, (2) gives

```text
xi_-n Phi_w(d_-n)+xi_n Phi_w(d_n)
= xi_n[-Phi_w(d_n)+Phi_w(d_n)]
=0.
```

The `n=0` term also vanishes because `Phi_w(0)=0`.  Hence

```text
S_1(w)=0                                               (5)
```

for every `w` away from removable singularities, and then by continuation at removable points.

## 5. Improved tail order

Substituting (5) into (3) yields:

```text
Lcal(b_m)
= sum_w (1-e^(wL))
   sum_n xi_n [ n Phi_w(d_n)-Phi_w(d_m)m ]/(pi m^2)
 + O_w(m^-3 weighted moments).                         (6)
```

Thus the finite tail has no `1/m` coefficient:

```text
Lcal(b_m)=O_spectral(m^-2),                            (7)
```

where `O_spectral` means that the remaining coefficient is the explicit symmetric zero functional in
(6), not an absolute-value estimate over zeros.

Consequently the outside mesh contribution has the formal summability profile

```text
a_m(z)Lcal(b_m)=O_spectral(e^(sigma L)m^-3).           (8)
```

The tail gate is now reduced to bounding the spectral coefficient in (6), not to overcoming a
harmonic tail.

## 6. The corrected tail target

The proof-facing target becomes:

```text
TAIL-PAR:
sum_{|m|>M} (1-e^(zL))/(iz-d_m)
sum_w (1-e^(wL))
   sum_n xi_n [ n Phi_w(d_n)-Phi_w(d_m)m ]/(pi m^2)
= O_K(L^B).
```

The first summation in `m` is absolutely convergent once the spectral coefficient is polynomially
controlled.  Therefore no pointwise Fourier cutoff of exponential size is needed after parity.

## 7. Status

```text
proved: the apparent 1/m coefficient of Lcal(b_m) vanishes exactly by pole-even parity;
improved: finite tail begins at order m^-2 before multiplication by a_m(z);
open:   prove polynomial control of the remaining spectral coefficient in TAIL-PAR.
```

