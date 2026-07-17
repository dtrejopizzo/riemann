# E73.237 - Balanced coefficient form of SECOND-ABEL

Date: 2026-07-14.

## 1. Purpose

E73.235--E73.236 reduce U4 to the coefficient divisibility statement

```text
ETA-DIV:
F_L[B]=sum c_omega W_omega+sum l_omega V_omega=O_M(L^-M),
```

for the transverse eta-packet satisfying

```text
B(0)=0,      B(L)=0.
```

E73.193 shows that the first endpoint derivative can be removed by a balanced
ramp `r_*` with `F_L[r_*]=0`.  This note writes that reduction entirely in
coefficient language and connects it to the second-Abel endpoint of E73.194.

## 2. Derivative moment

For

```text
B(y)=sum_omega c_omega e^(iomega y)
    +y sum_omega l_omega e^(iomega y),
```

the first derivative at the singular endpoint is

```text
B'(0)=sum_omega i omega c_omega + sum_omega l_omega.       (1)
```

By the finite Weyl kernel computation from E73.191, the same number is also

```text
B'(0)=-(2/L)(sum_m q_a(m))(sum_n eta_n).                    (2)
```

Equation (1) is the coefficient derivative moment; equation (2) is the
rank-one source form.

## 3. Balanced coefficient packet

Let

```text
r_0(y)=y(1-y/L),
r_1(y)=y^2(1-y/L),
c_L=-F_L[r_0]/F_L[r_1],
r_*(y)=r_0(y)+c_Lr_1(y).
```

Then

```text
r_*(0)=0,      r_*'(0)=1,      r_*(L)=0,      F_L[r_*]=0.
```

Define

```text
B^bal(y)=B(y)-B'(0)r_*(y).                         (3)
```

Using E73.236 and (1):

```text
B^bal(0)=0,
(B^bal)'(0)=0,
B^bal(L)=0,
F_L[B^bal]=F_L[B].                                 (4)
```

Thus ETA-DIV is equivalent to the balanced double-zero statement:

```text
F_L[B^bal]=O_M(L^-M).                              (BAL-ETA)
```

No cancellation has been split into large pieces because the subtracted ramp is
exactly neutral for `F_L`.

## 4. Curvature identity

The balanced packet has curvature

```text
(B^bal)''(t)
= sum_omega (-omega^2)c_omega e^(iomega t)
 + sum_omega (2iomega l_omega - t omega^2 l_omega)e^(iomega t)
 - B'(0) r_*''(t).                                (5)
```

Since

```text
r_*''(t)=-2/L + c_L(2-6t/L),
```

E73.194 gives the exact finite identity

```text
F_L[B]
= int_0^L K_L(t)(B^bal)''(t)dt.                  (6)
```

This is the proof-facing second-Abel form of ETA-DIV.

## 5. Finite identity to prove

The remaining theorem can now be stated without matrix notation:

```text
BSA-DIV:
For every admissible row/window, with coefficients satisfying

sum c_omega=0,
sum l_omega=0,
B'(0)=sum iomega c_omega+sum l_omega,

the finite signed pairing

int_0^L K_L(t)[
  sum (-omega^2)c_omega e^(iomega t)
 +sum (2iomega l_omega - t omega^2 l_omega)e^(iomega t)
 -B'(0)(-2/L+c_L(2-6t/L))
]dt

is O_M(L^-M).
```

Here `K_L` is the explicit finite second-Abel kernel:

```text
K_L(t)=int_t^L (y-t)W_L(y)dy
 -sum_{p^k: klog p>=t}(log p)p^(-k/2)(klog p-t).
```

This is a zero-free finite identity.  It contains:

```text
1. finite coefficients c_omega,l_omega;
2. endpoint/derivative moment constraints;
3. the balanced neutral ramp;
4. the exact model-prime kernel K_L.
```

## 6. Status

```text
proved: ETA-DIV <=> BAL-ETA <=> BSA-DIV;
proved: derivative moment and rank-one source are the same B'(0);
open: prove the signed second-Abel curvature orthogonality uniformly.
```

