# E72.72 -- Weyl-null split of the two-resolvent certificate

**Date:** 2026-07-08.
**Role:** separate the HPAC residual at finite roots into an actual-divisor core and a model/actual
ground-state displacement term.

## 0. Starting point

E72.71 proved that:

```text
F_x(s;tau)=<v,A_x(tau)k>
```

has the two-resolvent form:

```text
F_x(s;tau)
 = alpha(tau) {
     i[<v,R_+(tau)k>+<v,R_-(tau)k>]
     -(E_tau-1)/L[
       <v,r_+(tau)><r_+(tau),k>
       +<v,r_-(tau)><r_-(tau),k> ] },
```

where:

```text
R_+(tau)=(tau I+D)^(-1),      r_+(tau)=R_+(tau)1,
R_-(tau)=(tau I-D)^(-1),      r_-(tau)=R_-(tau)1,
alpha(tau)=1/2+i tau.
```

## 1. Weyl-null input

At a finite CCM root:

```text
P_x(tau_j)=0,
```

the actual ground vector `xi_x` satisfies:

```text
<xi_x,r_-(tau_j)>=0.                                             (WN)
```

Thus:

```text
<r_-(tau_j),k_x>=<r_-(tau_j),k_x-xi_x>.                          (K-XI)
```

The `r_-` rank-one term is therefore entirely a model/actual displacement term.

## 2. Exact split

Write:

```text
h_x:=k_x-xi_x.
```

At a finite root `tau_j`:

```text
F_x(s;tau_j)=alpha(tau_j)[ C_xi(s;tau_j)+D_h(s;tau_j) ],          (SPLIT)
```

where the actual-divisor core is:

```text
C_xi
 := i[<v,R_+xi>+<v,R_-xi>]
    -(E-1)/L <v,r_+><r_+,xi>,                                    (CORE)
```

and the displacement term is:

```text
D_h
 := i[<v,R_+h>+<v,R_-h>]
    -(E-1)/L[
       <v,r_+><r_+,h>+<v,r_-><r_-,h> ].                          (DISP)
```

This is exact, because the missing term `<r_-,xi>` vanishes by `(WN)`.

## 3. New sufficient certificate

The HPAC finite-root certificate `(CERT0)` follows if, on compact height windows and the two Cauchy
heights:

```text
max_{P_x(tau_j)=0}|C_xi(s;tau_j)| -> 0,                          (CORE0)
```

and:

```text
max_{P_x(tau_j)=0}|D_h(s;tau_j)| -> 0.                           (DISP0)
```

with the one-`s`-derivative analogue and a normal quotient bound.

`CORE0` is an actual finite-divisor identity. `DISP0` is a one-family model/actual convergence
estimate in the HPAC norm; it is weaker than full vector convergence.

## 4. Numerical signal

In the current finite harness, the actual-divisor core is much smaller than the full HPAC residual.
Representative magnitudes:

```text
lambda=8:
  |full|     1.905e-2  1.373e-2  7.348e-3  3.244e-3
  |xi-core|  3.861e-4  1.071e-3  1.528e-3  2.803e-3

lambda=12:
  |full|     3.091e-3  3.799e-3  4.162e-4  7.870e-3
  |xi-core|  1.387e-4  2.116e-4  2.548e-4  1.578e-3

lambda=20:
  |full|     3.137e-2  5.553e-4  6.424e-3  2.346e-3
  |xi-core|  2.621e-5  7.045e-5  7.498e-5  4.656e-5
```

The data says that the actual-divisor core is already close to a finite identity; the larger residual
comes from the model/actual displacement `h_x`.

## 5. Interpretation

This split prevents a circular shortcut. One cannot simply assume `k_x≈xi_x`, because that is close to
the stable-divisor conclusion. But one also does not need full vector convergence. The displacement is
only tested against:

```text
R_+^*v, R_-^*v, r_+, r_-,
```

at finite roots. Therefore the remaining proof can target the HPAC displacement norm, not the whole
ambient norm.

## 6. Status

```text
proved: at finite roots, HPAC splits exactly into CORE plus DISP;
observed: CORE is already much smaller than the full residual in the finite harness;
open:   prove CORE0 as a finite actual-divisor identity and DISP0 as a reduced displacement estimate.
```
