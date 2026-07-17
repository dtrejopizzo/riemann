# E73.232 - Uniform closed-interval theorem target

Date: 2026-07-14.

## 1. Purpose

E73.230 closes the finite-window scalar interval wrapper.  This note states the
uniform theorem that would promote those finite certificates to the scalar WRL
gate and hence to Omega7 through the Phase 72 reductions.

This is not a new proxy.  It is the uniform version of the exact finite scalar
certificate already built.

## 2. Finite objects

For each admissible window `(L,N,w,a)` define:

```text
eta_w=(I-P_w)xi_L,
B_a(y)=q_a Q_L(y) eta_w
      =sum c_omega e^(iomega y)+y sum l_omega e^(iomega y),

C_a(L,N,w)=A_L^digamma[B_a]-P_L[B_a].
```

The finite closed interval wrapper is:

```text
C_a in B(C_a^0, R_closed),
R_closed=R_coeff+R_weight+R_prod.
```

## 3. Uniform theorem target

**UCT-FF (Uniform Closed TRANS-CELL Finite-Frequency Certificate).**  For every
admissible compact Cauchy-height range and every target `M`, there exist
constants

```text
N_0, L_0, A, B
```

such that for all `L>=L_0`, all admissible `N>=N_0(L)`, and all admissible rows
`w,a`,

```text
|C_a^0(L,N,w)| + R_closed(L,N,w) <= A L^(-M).       (1)
```

Then `TRANS-CELL` holds with arbitrary polynomial decay:

```text
Q_wH_model,L eta_w - Q_wPrime_L eta_w = O_M(L^(-M)).
```

By E73.188--E73.202 this gives scalar WRL in the Phase 72 channel, and by the
existing Omega chain it feeds Omega7.

## 4. Factorized sufficient conditions

UCT-FF follows from the following explicit factor bounds.

### U1. Uniform eigenline/coefficient radius

There is a certificate radius `rho_eta(L)` satisfying

```text
||eta_w-eta_{w,0}|| <= rho_eta(L),
rho_eta(L) <= L^(-M-B_1)
```

for arbitrarily large `M` after choosing the finite precision/order parameters.

This is the current main bottleneck: it is the uniform version of the
BALL-ENTRY-CERT + bordered Krawczyk chain.

### U2. Uniform coefficient-map growth

For the linear maps

```text
c_omega=u_omega eta,
l_omega=v_omega eta,
```

the weighted operator sum obeys a polynomial bound:

```text
sum_omega |W_omega| ||u_omega||
+sum_omega |V_omega| ||v_omega|| <= L^(B_1).        (2)
```

Then

```text
R_coeff <= L^(B_1) rho_eta(L).
```

### U3. Uniform weight-radius bound

The closed weights have outward radii satisfying

```text
sum_omega |c_omega|rad(W_omega)
+sum_omega |l_omega|rad(V_omega)
+sum products <= L^(-M)
```

after choosing `K,R` and finite precision as functions of `M`.

E73.227/E73.229 prove this in the tested finite windows; the uniform statement
needs only sector control for `z=R+1/4-iomega/2` and polynomial growth of the
frequency window.

### U4. Uniform center cancellation

The midpoint itself must satisfy

```text
|C_a^0(L,N,w)| <= A L^(-M).                         (3)
```

This is the true arithmetic content.  E73.230 certifies it in finite windows,
but a proof of U4 is the uniform version of the finite critical source
divisibility theorem from E73.161.

## 5. What remains load-bearing

Among U1--U4, the finite arithmetic wrappers make U2--U3 plausible technical
bounds.  The hard mathematical content is:

```text
U1: uniform bordered eigenline production,
U4: uniform center cancellation / finite critical source divisibility.
```

U4 is exactly where the program has always located the arithmetic wall:

```text
finite CCM/Feshbach equation for xi_L
=> critical source divisibility
=> NAT-PROJ
=> scalar WRL.
```

## 6. Status

```text
proved finite-window: E73.230 closed scalar interval wrapper;
stated uniform target: UCT-FF;
load-bearing open: U1 and U4.
```
