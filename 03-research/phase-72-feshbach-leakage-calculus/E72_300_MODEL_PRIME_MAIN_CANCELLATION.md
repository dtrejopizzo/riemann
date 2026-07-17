# E72.300 -- Model/prime main cancellation in FORM-DCB

**Purpose.** Correct E72.299: the arithmetic `MAIN-FORM` term should not be bounded by itself. Its
`e^(y/2)` PNT main is cancelled by the `e^(y/2)` part of the model operator. The load-bearing object is
the combined actual form.

## 1. Closed integral for the arithmetic main

For `d_m=2pi m/L`,

```text
int_0^L e^(y/2) sin(d_m y)dy
= d_m(1-e^(L/2))/(d_m^2+1/4).                         (1)
```

Therefore, with

```text
phi(d)=d/(d^2+1/4),
```

E72.299 gives

```text
int_0^L e^(y/2)F_tau(y)dy
= 2(e^(L/2)-1)/L
   sum_{m != n} xi_m xi_n (s_m-s_n)^2
   [phi(d_m)-phi(d_n)]/(d_m-d_n).                     (2)
```

Thus the arithmetic main can naturally carry the exponential factor `e^(L/2)/L`. It is not a safe
standalone target.

## 2. Why this is not an obstruction

The actual finite matrix entries have the form

```text
C_E = W02 - WR - Prime - e_pole I,
```

where

```text
W02(Q)=int_0^L Q_y(e^(y/2)+e^(-y/2))dy,
Prime(Q)=sum_{r<=e^L} Lambda(r)r^(-1/2)Q_{log r}.
```

The scalar pole shift commutes with `S_tau`, so it vanishes in the double-commutator form. Hence

```text
FORM_actual(tau)
= -1/2 W02(F_tau) + 1/2 WR(F_tau) + 1/2 Prime(F_tau).  (3)
```

Using the Abel identity from E72.299,

```text
Prime(F_tau)
= int_0^L e^(y/2)F_tau(y)dy
 - int_0^L E(e^y)e^(-y/2)(F_tau'(y)-F_tau(y)/2)dy.
```

Substituting into (3), the entire `e^(y/2)` main cancels:

```text
FORM_actual(tau)
= -1/2 int_0^L e^(-y/2)F_tau(y)dy
   +1/2 WR(F_tau)
   -1/2 int_0^L E(e^y)e^(-y/2)(F_tau'(y)-F_tau(y)/2)dy.     (4)
```

This is the corrected combined FORM identity.

## 3. Correct replacement for MAIN-FORM + REM-FORM

The load-bearing estimates are not `MAIN-FORM` and `REM-FORM` separately. They are:

```text
LOWEXP-FORM:
sup_{tau_j<=H} |int_0^L e^(-y/2)F_tau_j(y)dy| <= C_H L^4,
```

```text
WR-FORM:
sup_{tau_j<=H} |WR(F_tau_j)| <= C_H L^4,
```

and

```text
PNTERR-FORM:
sup_{tau_j<=H} |int_0^L E(e^y)e^(-y/2)
   (F_tau_j'(y)-F_tau_j(y)/2)dy| <= C_H L^4.
```

Together they imply

```text
FORM_actual(tau_j)=O_H(L^4).
```

## 4. Why this is the right cancellation

The false APCB route controlled `Prime` against the model after taking a global positive part. That
destroyed the exact cancellation between the `e^(y/2)` model mass and the PNT main of the primes.

The double-commutator route preserves this cancellation because it applies the same scalar kernel
`F_tau` to both sides before Abel summation. The exponential term (2) is not estimated; it disappears
algebraically in (4).

## 5. Updated target

The corrected finite analytic target for FORM-DCB is:

```text
LOWEXP-FORM + WR-FORM + PNTERR-FORM.
```

This is strictly better than E72.299's standalone `MAIN-FORM + REM-FORM`, and it is the first form in
this branch where the archimedean model and the prime current interact in the correct order.

E72.301 collapses the first two terms further:

```text
LOWEXP-FORM + WR-FORM = ARCH-FORM,
ARCH_tau=1/2 int_0^L e^(-5y/2)/(1-e^(-2y))F_tau(y)dy.
```

Thus the final FORM target is `ARCH-FORM + PNTERR-FORM`.
