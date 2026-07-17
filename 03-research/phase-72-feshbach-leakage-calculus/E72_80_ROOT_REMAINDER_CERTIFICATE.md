# E72.80 -- Root remainder certificate

**Date:** 2026-07-09.
**Role:** replace informal divisibility by an exact finite remainder on the finite Weyl roots.

## 0. Input from E72.79

The shorted HPAC residual at a finite Weyl root is:

```text
F_x(s;tau_j)/alpha_j
 = - N_x(s;tau_j)/det(C_E),
```

with:

```text
N_x(s;z)=det [ C_E       b_x(z) ]
              [ a_s^*    0      ].
```

Here:

```text
a_s  = B_x^* r_s^even,
b_x(z)=B_x^*W_x(z),
W_x(z)= iS_zk_x-(exp(izL)-1)L^(-1)S_z1 <(zI-D)^(-1)1,h_x>.
```

Thus all remaining content is in the scalar function:

```text
R_x(s;z):=N_x(s;z)/det(C_E).
```

This function is not a polynomial: it is rational in `z` plus `exp(izL)` times a rational function.
So ordinary polynomial divisibility is the wrong language.

## 1. Correct finite replacement for divisibility

Let the positive finite Weyl roots in the active window be:

```text
Tau_x={tau_1,...,tau_J},
P_{x,+}(z)=prod_{j=1}^J(z-tau_j).
```

For any scalar function `R(z)` defined on `Tau_x`, define its root remainder:

```text
Rem_{Tau_x}R(z)
 := sum_{j=1}^J R(tau_j) ell_j(z),

ell_j(z)
 := P_{x,+}(z)/(P_{x,+}'(tau_j)(z-tau_j)).
```

This is the unique polynomial of degree `<J` interpolating `R` on the finite root set:

```text
Rem_{Tau_x}R(tau_j)=R(tau_j).
```

Therefore:

```text
R(tau_j)=0 for every tau_j in Tau_x
    <=> Rem_{Tau_x}R(z) identically 0.                          (RR)
```

No zero of `Xi` is used here. The roots `tau_j` are finite Weyl roots of the CCM divisor.

## 2. The exact certificate

Apply `(RR)` to:

```text
R_x(s;z)=N_x(s;z)/det(C_E).
```

Then the even HPAC certificate is equivalent, in every finite window, to:

```text
Rem_{Tau_x} R_x(s;z) -> 0                                       (RRC)
```

locally uniformly in the allowed `s`-strip and uniformly over the active root window.

The core and displacement pieces are:

```text
R_x^core(s;z)=N_x^core(s;z)/det(C_E),
R_x^disp(s;z)=N_x^disp(s;z)/det(C_E),
R_x=R_x^core+R_x^disp,
```

so:

```text
CORE-C  <=> Rem_{Tau_x}R_x^core -> 0,
DISP-C  <=> Rem_{Tau_x}R_x^disp -> 0,
EV-CERT <=> Rem_{Tau_x}R_x      -> 0.                           (RRC-split)
```

## 3. Why this is the right algebraic endpoint

Earlier forms asked for:

```text
P_x(z) divides a scalar transform.
```

That phrase was too coarse because the transform contains:

```text
exp(izL).
```

The finite root remainder is the exact replacement:

```text
"divisible by P_x on the active finite divisor"
```

means:

```text
the interpolation remainder on the roots of P_x is zero.
```

This is stronger than a norm estimate and weaker than an illegal polynomial claim. It is the precise
finite algebraic statement needed for scalar WRL resonance annihilation.

## 4. Relation to scalar WRL annihilation

Combining:

```text
E72.68  HPAC divisibility => scalar WRL resonance annihilation,
E72.74  HPAC collapses to EV-CERT,
E72.79  EV-CERT equals a bordered minor ratio,
E72.80  root vanishing equals root-remainder vanishing,
```

the remaining theorem can now be stated without hidden inverse or hidden divisibility:

```text
Shorted root-remainder theorem:
For every compact s-window in the admissible strip,

  ||Rem_{Tau_x}(N_x(s;.)/det(C_E))||_{Tau_x} -> 0.

Then scalar WRL resonance annihilation holds.
```

Here any finite-dimensional norm on the coefficient vector of the interpolation polynomial is
equivalent once the active root window is fixed. For growing windows one must specify a stable norm,
for example the sup norm on a fixed compact height interval away from the mesh.

## 5. Status

```text
proved: finite root vanishing is exactly root-remainder vanishing;
proved: the shorted HPAC target is an explicit bordered-minor remainder;
open:   prove the shorted root-remainder theorem uniformly as x -> infinity.
```
