# E72.301 -- Archimedean residual collapse for FORM-DCB

**Purpose.** Collapse `LOWEXP-FORM + WR-FORM` from E72.300 into one exact archimedean residual
functional. This removes another artificial split.

## 1. WR on kernels with zero endpoint value

The CCM finite entry uses

```text
WR(Q)=1/2(LOG4PI+gamma)Q(0)
      + int_0^L (e^(y/2)Q(y)-Q(0))/(2sinh y)dy
      + 1/2 Q(0)log(tanh(L/2)).
```

For the FORM kernel of E72.299,

```text
F_tau(0)=0.
```

Therefore

```text
WR(F_tau)=int_0^L e^(y/2)F_tau(y)/(2sinh y)dy.        (1)
```

No constant, logarithmic, or endpoint renormalization term remains.

## 2. Collapse with the low exponential term

E72.300 gives

```text
FORM_actual(tau)
= -1/2 int_0^L e^(-y/2)F_tau(y)dy
   +1/2 WR(F_tau)
   -1/2 PNTERR_tau.
```

Using (1),

```text
1/2 WR(F_tau)-1/2 int_0^L e^(-y/2)F_tau(y)dy
= 1/2 int_0^L
   [ e^(y/2)/(2sinh y) - e^(-y/2) ] F_tau(y)dy.
```

Since

```text
e^(y/2)/(2sinh y)=e^(-y/2)/(1-e^(-2y)),
```

the bracket becomes

```text
e^(-y/2) e^(-2y)/(1-e^(-2y)).
```

Thus the exact combined archimedean residual is

```text
ARCH_tau
= 1/2 int_0^L e^(-5y/2)/(1-e^(-2y)) F_tau(y)dy.       (2)
```

The corrected FORM identity is

```text
FORM_actual(tau)=ARCH_tau - 1/2 PNTERR_tau.            (3)
```

## 3. Integrability at zero

The weight in (2) has a simple singularity:

```text
1/2 e^(-5y/2)/(1-e^(-2y)) = 1/(4y)+O(1),     y -> 0.
```

But `F_tau(0)=0`. More explicitly, from

```text
F_tau(y)
= sum_{m != n} xi_m xi_n (s_m-s_n)^2
   [sin(d_m y)-sin(d_n y)]/[pi(n-m)],
```

one has

```text
F_tau'(0)
= -2/L sum_{m != n} xi_m xi_n (s_m-s_n)^2.             (4)
```

Therefore the integrand in (2) is finite at zero. There is no hidden logarithmic divergence.

## 4. Final FORM-DCB target after arch collapse

The load-bearing estimates are now only:

```text
ARCH-FORM:
sup_{tau_j<=H} |ARCH_tau_j| <= C_H L^4,
```

and

```text
PNTERR-FORM:
sup_{tau_j<=H} |PNTERR_tau_j| <= C_H L^4,
```

where

```text
PNTERR_tau
= int_0^L E(e^y)e^(-y/2)(F_tau'(y)-F_tau(y)/2)dy.
```

Then

```text
FORM_actual(tau_j)=O_H(L^4).
```

## 5. Why this matters

The old split `LOWEXP-FORM + WR-FORM + PNTERR-FORM` still separated two archimedean terms that cancel
near the same endpoint. Equation (2) is the correct single archimedean object: it has no exponential
growth in `L`, no diagonal APCB obstruction, and no singular endpoint contribution beyond the
removable `F_tau(0)=0` factor.

E72.302 converts the remaining `PNTERR-FORM` term into the Mellin spectral transform

```text
M_tau(z)=int_0^L e^(zy)F_tau(y)dy
```

with a closed divided-difference formula. This is the finite divisibility target.
