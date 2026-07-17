# E72.70 -- Abel generator identity for HPAC

**Date:** 2026-07-08.
**Role:** remove the boundary term from the half-power Abel concomitant and expose the finite generator
whose Fourier transform must be divisible by the CCM spectral polynomial.

## 0. Starting point

E72.68 defines:

```text
A_x(tau)=Q_x(0)+(1/2+i tau)int_0^L exp(i tau y)Q_x(y)dy.
```

Set:

```text
a=i tau.
```

The CCM overlap cells satisfy:

```text
Q_x(L)=0.                                                        (END)
```

## 1. Boundary-free Abel identity

### Lemma 72.70.1

For every complex `tau`:

```text
A_x(tau)=int_0^L exp(i tau y)G_x(y)dy,                           (AG)
```

where:

```text
G_x(y):= (1/2)Q_x(y)-partial_y Q_x(y).                            (GEN)
```

### Proof

By integration by parts and `(END)`:

```text
a int_0^L exp(ay)Q_x(y)dy
 = [exp(ay)Q_x(y)]_0^L - int_0^L exp(ay)partial_yQ_x(y)dy
 = -Q_x(0)-int_0^L exp(ay)partial_yQ_x(y)dy.
```

Therefore:

```text
Q_x(0)+(1/2+a)int_0^L exp(ay)Q_x(y)dy
 = int_0^L exp(ay)((1/2)Q_x(y)-partial_yQ_x(y))dy.
```

This is `(AG)`. `QED`

## 2. Loewner form of the generator

Using E72.54:

```text
Q_x(y)=2cos(yD)-(2/L)Lo_y,
```

we get:

```text
G_x(y)
 = cos(yD)+2Dsin(yD)
   -(1/L)Lo_y+(2/L)partial_yLo_y.                                (G-Lo)
```

The differentiated Loewner term obeys:

```text
[D,partial_yLo_y]=[Dcos(yD),J].                                  (G-COMM)
```

Thus the complete HPAC concomitant is the Fourier transform of a single finite Loewner-commutator
generator.

## 3. Divisibility in generator form

Let:

```text
v_{x,s}=C_x^(-1)Q_x(sI-D_x)^(-1)1,
k=k_x,
F_x(s;tau)=<v_{x,s},A_x(tau)k_x>.
```

By `(AG)`:

```text
F_x(s;tau)
 = int_0^L exp(i tau y)<v_{x,s},G_x(y)k_x>dy.                    (F-GEN)
```

Therefore the finite-root certificate `(CERT0)` of E72.69 is equivalent to:

```text
max_{P_x(tau_j)=0, tau_j in K}
|int_0^L exp(i tau_j y)<v_{x,s},G_x(y)k_x>dy| -> 0.              (GEN-root)
```

with the one-`s`-derivative analogue and a normal quotient bound.

## 4. Why this is sharper than E72.68

E72.68 mixed a boundary term with a bulk integral. E72.70 shows that, because the CCM cell vanishes at
the endpoint, the Abel boundary term is exactly absorbed into the generator:

```text
(1/2)Q_x-partial_yQ_x.
```

So the remaining divisibility is no longer a boundary/bulk cancellation problem. It is a pure finite
Fourier divisibility problem for one explicitly known matrix-valued function.

## 5. The exact finite identity still missing

The root-level form of HPAC-DIV is now:

```text
int_0^L exp(i tau_j y)<C_x^(-1)Q_x(sI-D_x)^(-1)1,
                       G_x(y)k_x>dy = o(1)
```

for finite roots `tau_j` of the actual CCM Weyl numerator.

Equivalently, after clearing mesh denominators as in E72.69, the exponential-polynomial residual
belongs asymptotically to the determinant ideal:

```text
(P_x(tau)).
```

This is the present finite, explicit, verifiable identity.

## 6. Status

```text
proved: HPAC has the boundary-free generator form A_x(tau)=Fourier(G_x);
proved: G_x=(1/2)Q_x-Q_x' has an explicit Loewner-commutator formula;
reduced: HPAC divisibility to the finite generator-root identity (GEN-root);
open:   prove GEN-root from C_xv=Q_x(sI-D_x)^(-1)1 and the finite CCM construction.
```
