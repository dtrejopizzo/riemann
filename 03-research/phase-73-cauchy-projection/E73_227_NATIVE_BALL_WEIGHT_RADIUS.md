# E73.227 - Native-ball weight radius budget

Date: 2026-07-14.

## 1. Purpose

E73.225 bounded the weight radii

```text
rad(W_omega), rad(V_omega)
```

using an E73.211-style finite-rounding audit plus Bernoulli `psi/psi_1`
remainders.  This note replaces the finite-rounding audit by native complex-ball
propagation for the unit weights.

## 2. Method

For the unit modes

```text
e^(iomega y),          y e^(iomega y),
```

the finite elementary pieces are evaluated by the same ball primitives used in
E73.215:

```text
ball_exp,
ball_exp_int,
ball_y_exp_int,
finite prime sample balls.
```

The total radius remains:

```text
rad(W_omega) <= R_ball(W_omega)
              + C_sec R_psi(D_1(R,omega))
              + R_exp(W_omega),

rad(V_omega) <= R_ball(V_omega)
              + C_sec R_psi(D_2(R,omega))
              + R_exp(V_omega).
```

## 3. Result

The native finite-ball radius is far smaller than the Bernoulli tail:

```text
max R_ball(W,V) ~= L^-138 ... L^-156.
```

The total remains dominated by the Bernoulli term:

```text
C_sec=1    : R_weight ~= L^-75 ... L^-86,
C_sec=1e6  : R_weight ~= L^-67 ... L^-77.
```

Thus E73.227 does not change the numerical size of the E73.225 total, but it
does remove the heuristic finite-rounding component from the weight-radius
audit.

## 4. Consequence

The weight-radius ledger is now formally reduced to the same isolated
special-function issue as BALL-ENTRY-CERT:

```text
Bernoulli remainder lemma for psi/psi_1 with sector constant C_sec.
```

The finite elementary and prime-sample pieces have native complex-ball
radii with huge slack.

## 5. Status

```text
closed: finite elementary/prime rounding for W,V by native complex balls;
proved finite-window: Bernoulli sector lemma for psi/psi_1 in E73.229;
verified: weight radii remain negligible in tested windows.
```
