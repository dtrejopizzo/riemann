# E72.54 -- Loewner commutator identity for the CCM overlap cells

**Date:** 2026-07-08.
**Role:** expose the finite commutator structure hidden in the Hilbert coefficients of E72.52.

## 0. Mesh notation

Let:

```text
D = diag(d_n),        d_n=2*pi*n/L.
```

Write:

```text
s_n(y)=sin(d_n y),
c_n(y)=cos(d_n y).
```

The CCM overlap cell entries are:

```text
q_nn(y)=2(1-y/L)c_n(y),
q_mn(y)= [s_m(y)-s_n(y)]/[pi(n-m)]        (m != n).
```

Since:

```text
d_m-d_n = 2*pi(m-n)/L = -2*pi(n-m)/L,
```

for `m != n`:

```text
q_mn(y)= - (2/L) [s_m(y)-s_n(y)]/(d_m-d_n).
```

## 1. Loewner matrix

Define the Loewner divided-difference matrix:

```text
Lo_y(m,n)
 = [sin(d_m y)-sin(d_n y)]/(d_m-d_n),     m != n,
Lo_y(n,n)= y cos(d_n y).
```

Then the full overlap matrix is exactly:

```text
Q_x(y) = 2 cos(yD) - (2/L) Lo_y.                 (LC)
```

### Proof

For `m != n`, the diagonal term `2cos(yD)` contributes zero, so `(LC)` gives the off-diagonal formula.
For `m=n`,

```text
2cos(d_ny) - (2/L)ycos(d_ny)
 = 2(1-y/L)cos(d_ny).
```

`QED`

## 2. Fréchet derivative form

Let `J=11^T`. The Loewner matrix is the Fréchet derivative of `sin(yD)` in direction `J`:

```text
Lo_y = D(sin(yD))[J],
```

entrywise:

```text
D f(D)[J]_{mn}=f^[1](d_m,d_n)J_{mn}.
```

Equivalently, it solves the commutator equation:

```text
[D,Lo_y] = [sin(yD),J].                          (COMM)
```

The diagonal of `Lo_y` is fixed by the Fréchet derivative, not by the commutator.

## 3. Scalar channel decomposition

For:

```text
a_{x,s}(y)=<v_{x,s},Q_x(y)k_x>,
```

the identity `(LC)` gives:

```text
a_{x,s}(y)
 = 2<v_{x,s},cos(yD)k_x>
   - (2/L)<v_{x,s},Lo_y k_x>.                   (A-LC)
```

The first term is diagonal overlap. The second is exactly the Hilbert/Loewner term.

## 4. Why this matters

The coefficient obstruction from E72.52 is not an arbitrary discrete Hilbert transform. It is a
Fréchet derivative / commutator object tied to the pole mesh `D`.

The next possible proof can use:

```text
C_x v_{x,s}=Q_x(sI-D)^(-1)1,
H_x^0 k_x=mu_x^0 k_x,
[D,Lo_y]=[sin(yD),J].
```

This is a finite algebraic identity, not an asymptotic guess.

## 5. New target

### Loewner-Feshbach Cancellation

Show that the scalar endpoint transform of:

```text
2< v,cos(yD)k > - (2/L)<v,Lo_yk>
```

has half-power size by applying the Feshbach equation for `v` and the prolate equation for `k` to the
commutator identity `(COMM)`.

## 6. Status

```text
proved: exact Loewner identity Q_x(y)=2cos(yD)-(2/L)Lo_y;
proved: Hilbert coefficients are a finite commutator/Fréchet derivative of sin(yD);
open: use C_xv=Qr_s and H_x^0k=mu k to prove Loewner-Feshbach cancellation.
```

This is the first explicit finite identity that can plausibly carry the missing compressed
half-power.
