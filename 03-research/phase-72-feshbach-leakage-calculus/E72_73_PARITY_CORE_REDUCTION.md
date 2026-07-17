# E72.73 -- Parity reduction of the HPAC actual-divisor core

**Date:** 2026-07-08.
**Role:** simplify the actual-divisor core of E72.72 using the parity symmetry of the finite CCM
matrices.

## 0. Parity

Let `Pi` be the flip:

```text
(Pi a)_n=a_(-n).
```

The finite CCM matrices commute with `Pi`, so the ground vectors may be chosen even:

```text
Pi k_x=k_x,          Pi xi_x=xi_x.
```

Moreover:

```text
Pi D Pi=-D.
```

Therefore:

```text
Pi r_-(tau)=r_+(tau),
```

where:

```text
r_-(tau)=(tau I-D)^(-1)1,
r_+(tau)=(tau I+D)^(-1)1.
```

## 1. Root orthogonality on both sides

At a finite root `P_x(tau_j)=0`:

```text
<xi_x,r_-(tau_j)>=0.
```

Since `xi_x` is even:

```text
<xi_x,r_+(tau_j)>
 = <Pi xi_x,Pi r_-(tau_j)>
 = <xi_x,r_-(tau_j)>
 = 0.                                                           (WN+-)
```

Thus both rank-one terms involving `xi_x` vanish in the actual-divisor core.

## 2. Core collapse

Recall the core from E72.72:

```text
C_xi
 := i[<v,R_+xi>+<v,R_-xi>]
    -(E-1)/L <v,r_+><r_+,xi>.
```

By `(WN+-)`:

```text
C_xi
 = i<v,[R_+(tau_j)+R_-(tau_j)]xi_x>.                            (CORE1)
```

But:

```text
R_+(tau)+R_-(tau)
 = (tau I+D)^(-1)+(tau I-D)^(-1)
 = 2tau(tau^2I-D^2)^(-1).                                      (EVEN-R)
```

This operator is even. Therefore:

```text
C_xi(s;tau_j)
 = i <v_even, 2tau_j(tau_j^2I-D^2)^(-1)xi_x>,                  (CORE2)
```

where:

```text
v_even=(v+Pi v)/2.
```

## 3. New core target

### Even Cauchy-Feshbach Suppression

For compact height windows and the two Cauchy heights:

```text
max_{P_x(tau_j)=0}
|<v_even, 2tau_j(tau_j^2I-D^2)^(-1)xi_x>| -> 0.                 (ECFS)
```

Then `CORE0` of E72.72 holds.

This is sharper than `CORE0`: it says the actual-divisor core is only testing the even part of the
Cauchy-Feshbach vector.

## 4. Why this is plausible

The source:

```text
r_s=(sI-D)^(-1)1
```

has even part:

```text
r_s^even=s(s^2I-D^2)^(-1)1,
```

and odd part:

```text
r_s^odd=D(s^2I-D^2)^(-1)1.
```

The projection `Q_x=I-k_xk_x^T` removes the even ground line. Since `C_x` commutes with parity:

```text
v_even = C_even^(-1)Q_even r_s^even.
```

Thus `(ECFS)` is a reduced even-sector estimate, not a full vector estimate.

## 5. Status

```text
proved: finite-root orthogonality holds for both r_- and r_+ by parity;
proved: actual-divisor core collapses to an even-sector pairing (CORE2);
reduced: CORE0 to Even Cauchy-Feshbach Suppression (ECFS);
open:   prove ECFS from the even-sector gap/ground-line removal in C_x.
```
