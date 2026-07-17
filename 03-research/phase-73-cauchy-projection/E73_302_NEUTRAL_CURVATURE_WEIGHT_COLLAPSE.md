# E73.302 - Neutral curvature weight collapse

Date: 2026-07-16.

## 1. Purpose

E73.301 gives the correct local curvature form:

```text
(B^bal)''(t)=q[Q_t''+alpha_L(t)J]eta,
alpha_L(t)=(2/L)[-2/L+c_L(2-6t/L)].
```

This note records the corresponding frequency-weight consequence.  The
neutral ramp is load-bearing for integration by parts, but it does not create
a new scalar forcing mechanism.

## 2. Weight collapse

Let

```text
r_*(t)=r_0(t)+c_Lr_1(t),
F_L[r_*]=0.
```

By the second-Abel identity,

```text
R_*:=int_0^L K_L(t)r_*''(t)dt=F_L[r_*]=0.
```

For a coefficient packet

```text
B(t)=sum c_omega e^(iomega t)+t sum l_omega e^(iomega t),
B'(0)=sum iomega c_omega+sum l_omega,
```

the curvature representation gives

```text
F_L[B]
=sum c_omega U_omega+sum l_omega Z_omega-B'(0)R_*.
```

Since `R_*=0`, the balanced quotient weights reduce to:

```text
U^bal_omega=U_omega,
Z^bal_omega=Z_omega.
```

And because the second-Abel formula is exact,

```text
sum c_omega U_omega+sum l_omega Z_omega
=sum c_omega W_omega+sum l_omega V_omega
```

on the admissible coefficient subspace.

## 3. Interpretation

The `alpha_L(t)J` term is essential locally:

```text
it makes B^bal(0)=0, (B^bal)'(0)=0, B^bal(L)=0,
```

so integration by parts has no endpoint remainder.

But globally:

```text
int K_L alpha_L(t) dt
```

is exactly the neutral ramp contribution and vanishes in the scalar
coefficient pairing.  Therefore the neutral ramp does not supply the missing
orthogonality.  The missing theorem is still the original signed
Gamma-prime/eigenline pairing.

## 4. Numerical certification

`E73_238_curvature_weight_quotient_probe.py` verifies:

```text
fstarB = log_L |F_L[r_*]|,
diffB  = log_L |center-quotient|.
```

Representative output:

```text
 lam      L gamma row centerB quotientB diffB fstarB BpB
  12    4.970  14.13   0   -21.26    -21.26 -430.82 -430.82  -10.41
  16    5.545  21.02   0   -18.21    -18.21 -403.27 -403.27   -9.55
  20    5.991  21.02   1   -18.80    -18.80 -385.84 -385.84   -9.54
```

The quotient correction is at numerical floor.

## 5. Status

```text
proved: neutral ramp has zero scalar curvature weight R_*;
proved: frequency-weight endpoint remains the original W,V pairing;
kept:   alpha_L(t)J as the correct local second-Abel representative;
open:   prove the signed W,V / Gamma-prime eigenline pairing.
```

