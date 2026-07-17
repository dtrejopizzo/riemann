# E72.71 -- Two-resolvent identity for HPAC

**Date:** 2026-07-08.
**Role:** collapse the half-power Abel concomitant from a full matrix transform to two diagonal
resolvents plus two rank-one terms.

## 0. One-sided translation overlap

Let:

```text
e_n(t)=L^(-1/2)exp(i d_n t),        d_n=2*pi*n/L.
```

For `0<=y<=L`, define the one-sided overlap:

```text
U_y(m,n)=int_0^(L-y) e_m(t+y) conjugate(e_n(t)) dt.
```

Then:

```text
Q_x(y)=U_y+U_y^*.                                                 (TR)
```

Indeed, for `m=n`:

```text
U_y(n,n)+U_y(n,n)^*
 = 2(1-y/L)cos(d_ny),
```

and for `m != n`:

```text
U_y(m,n)+U_y(m,n)^*
 = [sin(d_my)-sin(d_ny)]/[pi(n-m)].
```

This recovers exactly the CCM overlap cells.

## 1. Closed form for the HPAC matrix

Let:

```text
alpha(tau)=1/2+i tau,
E_tau=exp(i tau L),
r_+(tau)=(tau I+D)^(-1)1,
r_-(tau)=(tau I-D)^(-1)1.
```

### Lemma 72.71.1

The half-power Abel matrix of E72.68 is:

```text
A_x(tau)
 = 2I
   + i alpha(tau)[(tau I+D)^(-1)+(tau I-D)^(-1)]
   - alpha(tau)(E_tau-1)/L
       [ r_+(tau)r_+(tau)^T + r_-(tau)r_-(tau)^T ].              (2R)
```

### Proof

For the one-sided overlap:

```text
U_y(m,n)
 = [exp(i d_n y)-exp(i d_m y)]/[iL(d_m-d_n)],       m != n,
U_y(n,n)=(1-y/L)exp(i d_ny).
```

For `m != n`:

```text
int_0^L exp(i tau y)U_y(m,n)dy
 = -(E_tau-1)/[L(tau+d_m)(tau+d_n)].
```

For `m=n`:

```text
int_0^L exp(i tau y)U_y(n,n)dy
 = i/(tau+d_n) -(E_tau-1)/[L(tau+d_n)^2].
```

Thus:

```text
I+(1/2+i tau)int exp(i tau y)U_y dy
 = I+i alpha(tau)(tau I+D)^(-1)
   - alpha(tau)(E_tau-1)L^(-1)r_+r_+^T.
```

Applying the same calculation to `U_y^*`, equivalently replacing `D` by `-D`, gives:

```text
I+i alpha(tau)(tau I-D)^(-1)
 - alpha(tau)(E_tau-1)L^(-1)r_-r_-^T.
```

Adding the two one-sided contributions proves `(2R)`. `QED`

## 2. Scalar certificate

For:

```text
v=v_{x,s}=C_x^(-1)Q_x(sI-D)^(-1)1,
k=k_x,
F_x(s;tau)=<v,A_x(tau)k>,
```

the compressed gauge gives:

```text
<v,k>=0.
```

Therefore the `2I` term in `(2R)` drops out and:

```text
F_x(s;tau)
 = i alpha(tau)
     [ <v,(tau I+D)^(-1)k> + <v,(tau I-D)^(-1)k> ]
   - alpha(tau)(E_tau-1)/L
     [ <v,r_+><r_+,k> + <v,r_-><r_-,k> ].                       (2R-F)
```

This is the finite scalar certificate equivalent to `GEN-root`.

At a finite CCM root `tau_j`, the second vector:

```text
r_-(tau_j)=(tau_jI-D)^(-1)1
```

is the Weyl null vector:

```text
xi_x^T r_-(tau_j)=0.
```

Thus the remaining cancellation is now localized to the two-resolvent scalar identity `(2R-F)` at
Weyl-null vectors.

## 3. New exact target

### Two-Resolvent HPAC Cancellation

For compact height windows and the two Cauchy heights:

```text
max_{P_x(tau_j)=0}
| i [ <v,(tau_j I+D)^(-1)k> + <v,(tau_j I-D)^(-1)k> ]
  - (E_j-1)/L
    [ <v,r_+(tau_j)><r_+(tau_j),k>
      + <v,r_-(tau_j)><r_-(tau_j),k> ] | -> 0,                 (2R-CERT)
```

after dividing by the harmless bounded factor `alpha(tau_j)` when the window avoids `tau=i/2`.

This is strictly sharper than E72.69:

```text
matrix exponential-polynomial residual
```

has become:

```text
two diagonal resolvent pairings + two rank-one Weyl-vector products.
```

## 4. Status

```text
proved: Q_x(y) is the symmetrized one-sided translation overlap U_y+U_y^*;
proved: HPAC matrix has the exact two-resolvent form (2R);
reduced: GEN-root/CERT0 to the scalar two-resolvent cancellation (2R-CERT);
open:   prove (2R-CERT) from C_xv=Q_x(sI-D)^(-1)1 and xi_x^T r_-(tau_j)=0.
```
