# E72.337 -- Dirichlet-Cauchy packet form of BULK-SMOOTH

**Purpose.** Rewrite the finite packet `B_z^M` and its derivatives in one-dimensional Fourier packet
language. This replaces the dangerous double sum in `BULK-SMOOTH` by products of two explicit packets:
one Cauchy-Dirichlet packet from the multiplier `(1-e^(zL))/(iz-d_m)`, and one source packet from
`xi`.

## 1. Packet definitions

Let the active finite mesh be `|m|<=M`. Define

```text
a_m(z):=(1-e^(zL))/(iz-d_m),
A_z(r):=sum_{|m|<=M} a_m(z)e^(id_m r),
X(r):=sum_{|n|<=M} xi_n e^(id_n r).
```

Then, from the integral representation of `Q_y`,

```text
B_z^M(y)
= (1/L) int_0^(L-y)
   [ A_z(t+y) overline{X(t)}
     + A_z^#(t+y) X(t) ] dt,                         (1)
```

where

```text
A_z^#(r):=sum_m a_m(z)e^(-id_m r).
```

This is exactly the finite transformed packet, not an approximation.

## 2. Cauchy-Dirichlet differential identity

Let

```text
D_M(r):=sum_{|m|<=M}e^(id_m r).
```

Since

```text
d_m/(iz-d_m)=iz/(iz-d_m)-1,
```

equivalently

```text
i d_m a_m(z)= -z a_m(z)-i(1-e^(zL)),
```

we get the exact identity

```text
A_z'(r)= -z A_z(r) - i(1-e^(zL))D_M(r).              (2)
```

Similarly,

```text
(A_z^#)'(r)= z A_z^#(r) + i(1-e^(zL))D_M(r).         (3)
```

Differentiating again,

```text
A_z''(r)= z^2A_z(r)+iz(1-e^(zL))D_M(r)-i(1-e^(zL))D_M'(r),
```

and similarly for `A_z^#`.

These identities are the correct way to differentiate the packet: no powers of `d_m` should be exposed
without first converting them to `A_z`, `D_M`, and `D_M'`.

## 3. First derivative of `B_z^M`

Differentiate (1). The moving endpoint contributes no term at `t=L-y` because the interval collapses
against `Q_L=0`; the remaining derivative is

```text
(B_z^M)'(y)
= (1/L) int_0^(L-y)
   [ A_z'(t+y) overline{X(t)}
     + (A_z^#)'(t+y) X(t) ]dt
   - boundary_y,                                      (4)
```

where

```text
boundary_y=(1/L)[A_z(L)overline{X(L-y)}+A_z^#(L)X(L-y)].
```

At `y=0,L`, (4) collapses to the rank-one endpoint identity of E72.336.

## 4. Second derivative and BULK-SMOOTH

A second derivative of (1), using (2)--(3), expresses `(B_z^M)''` as a finite sum of terms of the form

```text
int_0^(L-y) A_z(t+y) X(t)dt,
int_0^(L-y) D_M(t+y) X(t)dt,
int_0^(L-y) D_M'(t+y) X(t)dt,
```

plus explicit boundary terms involving `A_z`, `D_M`, and `X` at endpoints.

Therefore `BULK-SMOOTH` follows from the packet estimates:

```text
DC-PACKET:
int_0^L |A_z(r)|dr <= C_KL^B,

DIR-PACKET:
int_0^L |D_M(r)X(t-r)|dr <= C_KL^B
and the same with D_M',

SRC-PACKET:
||X||_2 <= C,  ||X'||_2 <= C L^B,
```

with the endpoint rank-one term controlled by E72.336.

## 5. Why this is progress

A direct `Q''` estimate exposes `d_m^2 a_m(z)` and recreates the exponential incoherent ceiling.
Equations (2)--(3) show that those powers are fake: after using the Cauchy denominator, derivatives
produce only:

```text
A_z,
D_M,
D_M'.
```

So `PACK-SMOOTH` is now a finite harmonic-analysis estimate for a Dirichlet kernel acting on the source
packet `X`, not a raw matrix tail bound.

## 6. Status

```text
proved: exact packet representation (1);
proved: differential identities (2)--(3);
reduced: BULK-SMOOTH to Dirichlet-Cauchy packet bounds.
```

The next target is to prove the Dirichlet packet bounds using the fixed active bandwidth and
`||xi||_2=1`, without losing the right-strip cancellation.
