# E72.296 -- Directional commutator replacement for global UCB

**Purpose.** Replace the false global APCB/UCB route of E72.295 with the actual estimate needed in the
compact-root HPAC proof.

## 1. Where the false global bound entered

The compact-root residual is

```text
R_x(s,tau)=<a_s^perp,C_E^(-1)S_tau xi>.
```

The inverse-collapse identity gives

```text
R_x(s,tau)
= mu^(-1)<a_s^perp,S_tau xi>
 - mu^(-1)<a_s^perp,C_E^(-1)[C_E,S_tau]xi>.
```

The first term was closed by the Cauchy-factor identity and VBG. The second term was bounded in
E72.283 by the crude inequality

```text
||[C_E,S_tau]xi|| <= (||C_E||+mu)||S_tau xi||.
```

That is the only place where `||C_E||=O(L^2)` was used. E72.295 shows that this global upper bound is
false. Therefore the proof must estimate the vector

```text
[C_E,S_tau]xi
```

directly.

## 2. Exact commutator formula

Write

```text
C_E = C_model + Delta_arith,
Delta_arith = - sum_{n<=e^L} beta_n Q_{log n},
beta_n=Lambda(n)n^(-1/2).
```

Then

```text
[C_E,S_tau]xi
= [C_model,S_tau]xi
  - sum_{n<=e^L} beta_n [Q_{log n},S_tau]xi.              (2)
```

The diagonal operator `S_tau` has entries

```text
s_j(tau)=1/(tau-d_j)+1/(-tau-d_j)=2d_j/(tau^2-d_j^2).
```

Therefore, in the Fourier mesh,

```text
([Q_y,S_tau]xi)_m
= sum_j Q_y(m,j)(s_j(tau)-s_m(tau))xi_j.                 (3)
```

This formula is the new load-bearing object. It contains the smoothing factor
`s_j-s_m`, absent from APCB.

## 3. The commutator gain

For fixed `tau <= H`,

```text
s'(d)=2(tau^2+d^2)/(tau^2-d^2)^2.
```

Away from the finite pole neighborhood,

```text
|s_j-s_m| <= C_H |d_j-d_m| / ((1+|d_j|)^2(1+|d_m|)^2)
```

with the pole cells handled by the Weyl-root cancellation already used in VBG.

Since the off-diagonal kernel has

```text
Q_y(m,j) = [sin(d_m y)-sin(d_j y)]/[pi(j-m)]
```

and

```text
d_j-d_m = 2pi(j-m)/L,
```

the dangerous denominator cancels:

```text
Q_y(m,j)(s_j-s_m)
```

has an additional factor `L^(-1)` times high-frequency decay. This commutator gain is exactly what
global APCB could not see.

## 4. Directional theorem to prove

The corrected replacement for UCB is:

```text
DCB(H):
sup_{tau_j<=H} ||[C_E,S_tau_j]xi|| = O_H(L^alpha)
```

with any `alpha<7/2`. Indeed, under `mu>=cL^2`, `||a_s^perp||=O_K(L^(1/2))`, and
`||C_E^(-1)||<=mu^(-1)=O(L^(-2))`, the commutator residual is bounded by

```text
mu^(-1)||a_s^perp||||C_E^(-1)|| ||[C_E,S_tau]xi||
= O(L^(-2)) O(L^(1/2)) O(L^(-2)) O(L^alpha)
= O(L^(alpha-7/2)).
```

Thus `alpha<7/2` is enough, and the natural target from the commutator gain is much smaller:

```text
alpha <= 2.
```

## 5. Split of DCB

Using (2), DCB splits into:

```text
DCB-model:
sup_{tau_j<=H} ||[C_model,S_tau_j]xi|| = O_H(L^alpha_model),

DCB-arith:
sup_{tau_j<=H} ||sum_{n<=e^L} beta_n[Q_{log n},S_tau_j]xi|| = O_H(L^alpha_arith).
```

The arithmetic term should be attacked after the commutator difference `s_j-s_m` is inserted. Taking
absolute values before this insertion recreates the false APCB ceiling.

## 6. Consequence

The compact-root HPAC theorem should now read:

```text
GAP + corrected source/gauge + VBG + DCB
=> fixed-height compact-root HPAC decay.
```

No global upper complement bound is required.

This is a genuine improvement of the route: E72.295 removes a false global lemma, and E72.296 replaces
it with the exact source-local estimate that the proof actually needs.
