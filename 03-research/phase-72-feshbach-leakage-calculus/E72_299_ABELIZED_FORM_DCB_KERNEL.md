# E72.299 -- Abelized scalar kernel for FORM-DCB

**Purpose.** Reduce the arithmetic part of `FORM-DCB` to an exact scalar Abel problem. This is the
first post-APCB arithmetic target with the commutator difference already inserted.

## 1. The scalar FORM kernel

From E72.298,

```text
FORM_arith(tau)
= 1/2 sum_{r<=e^L} Lambda(r)r^(-1/2) F_tau(log r),
```

where

```text
F_tau(y)
 := sum_{m,n} xi_m xi_n (s_m(tau)-s_n(tau))^2 Q_y(m,n).        (1)
```

Using the closed entries of `Q_y`,

```text
Q_y(m,m)=2(1-y/L)cos(d_m y),
```

and, for `m != n`,

```text
Q_y(m,n)= [sin(d_m y)-sin(d_n y)]/[pi(n-m)].
```

The diagonal part of (1) vanishes because `(s_m-s_m)^2=0`. Hence

```text
F_tau(y)
= sum_{m != n} xi_m xi_n (s_m-s_n)^2
   [sin(d_m y)-sin(d_n y)]/[pi(n-m)].                  (2)
```

This is the scalar finite kernel that replaces the false APCB high-band operator.

## 2. Endpoint cancellation

The kernel has exact endpoint cancellation:

```text
F_tau(0)=0,       F_tau(L)=0.                            (3)
```

Indeed, `sin(d_m*0)=0`, and `sin(d_m L)=sin(2pi m)=0`.

This is the structural gain over the APCB diagonal obstruction. The dangerous one-sided diagonal
kernel `2(1-y/L)cos(d_m y)` is gone before arithmetic summation begins.

## 3. Abel form

Let

```text
G_tau(u)=u^(-1/2)F_tau(log u),       1<=u<=e^L.
```

Then

```text
FORM_arith(tau)=1/2 int_1^(e^L) G_tau(u) d psi(u).
```

Write

```text
psi(u)=u+E(u).
```

By (3), `G_tau(1)=G_tau(e^L)=0`, so partial summation gives the exact identity

```text
FORM_arith(tau)
= 1/2 int_0^L e^(y/2)F_tau(y)dy
 -1/2 int_0^L E(e^y)e^(-y/2)
       (F_tau'(y)-1/2 F_tau(y))dy.                    (4)
```

There are no endpoint terms.

## 4. Exact finite target

Therefore the arithmetic component alone would follow from the two scalar estimates

```text
MAIN-FORM:
sup_{tau_j<=H} |int_0^L e^(y/2)F_tau_j(y)dy| <= C_H L^4,
```

and

```text
REM-FORM:
sup_{tau_j<=H} |int_0^L E(e^y)e^(-y/2)
       (F_tau_j'(y)-1/2F_tau_j(y))dy| <= C_H L^4.
```

Both are statements about the single explicit kernel (2). They do not ask for positivity of Weil, do
not control the full complement, and do not take absolute values before the commutator difference is
inserted.

## 5. Status after E72.300

The standalone arithmetic route would have required:

```text
1. prove MAIN-FORM by integrating the sine-difference kernel against e^(y/2);
2. prove REM-FORM using only PNT-strength information on E(u), after bounding
   F_tau'(y)-F_tau(y)/2 with the commutator gain.
```

E72.300 corrects the load-bearing use of this identity: `MAIN-FORM` should not be bounded separately.
Its `e^(y/2)` term cancels exactly against the `e^(y/2)` part of the model operator. The final target is
the combined identity `LOWEXP-FORM + WR-FORM + PNTERR-FORM`.

Thus (4) is retained as an exact Abel identity, but not as the final proof split.
