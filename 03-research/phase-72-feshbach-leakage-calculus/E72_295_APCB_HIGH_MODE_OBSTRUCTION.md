# E72.295 -- High-mode obstruction to global APCB

**Purpose.** Prove analytically that the global positive-part ceiling

```text
APCB: lambda_max(Delta_arith)_+ = O(L^2)
```

cannot be the correct asymptotic lemma in the full pole-even complement. The obstruction is not
numerical. It is the diagonal Fourier main term of the one-sided autocorrelation kernel.

## 1. Diagonal one-sided main term

For the Fourier mesh

```text
omega_m = 2pi m/L,
```

the exact diagonal cell is

```text
Q_y(m,m)=2(1-y/L)cos(omega_m y).
```

The PNT main contribution to the diagonal of

```text
Delta_arith = - sum_{n<=e^L} Lambda(n)n^(-1/2) Q_{log n}
```

is therefore

```text
D_main(m)
= -2 Re int_0^L e^((1/2+i omega_m)y)(1-y/L) dy.
```

Set `a=1/2+i omega_m`. Since `omega_m L=2pi m`,

```text
exp(aL)=exp(L/2).
```

A direct integration gives

```text
int_0^L e^(ay)(1-y/L)dy
= -1/a + (e^(L/2)-1)/(L a^2).                       (1)
```

Hence, for fixed `|omega_m|>1/2`,

```text
D_main(m)
= -2 Re[-1/a + (e^(L/2)-1)/(L a^2)]
=  2(e^(L/2)-1)(omega_m^2-1/4)/(L(omega_m^2+1/4)^2) + O(1).
```

Thus

```text
D_main(m) >= c(omega_m) e^(L/2)/L
```

for every fixed high mesh frequency `|omega_m|>1/2`.

## 2. Arithmetic sum has the same main term

Let

```text
F_L(u)=u^(-1/2)(1-log u/L)cos(omega_m log u),      1<=u<=e^L.
```

The endpoint at `u=e^L` vanishes because of the taper. Partial summation gives

```text
sum_{n<=e^L} Lambda(n)F_L(n)
= int_1^(e^L) F_L(u)du
  + error_L.
```

Using the classical de la Vallee Poussin form

```text
psi(u)=u+O(u exp(-c sqrt(log u))),
```

and the bound `F_L'(u)=O_{omega}(u^(-3/2))`, one obtains

```text
error_L = O_omega(e^(L/2) exp(-c' sqrt(L))) = o_omega(e^(L/2)/L).
```

Therefore the actual diagonal Rayleigh quotient along the Fourier mode has the same leading term as
`D_main(m)`.

## 3. Consequence

For any fixed mesh-frequency window containing a frequency `|omega|>1/2`,

```text
lambda_max(Delta_arith)_+ >= c(omega)e^(L/2)/L + o(e^(L/2)/L).
```

In particular,

```text
lambda_max(Delta_arith)_+ != O(L^2).
```

So global APCB is false as an asymptotic statement in the full pole-even complement.

## 4. Interpretation

This does not contradict the finite windows in E72.285--E72.292. In those windows `L` is small enough
that `e^(L/2)/L` is not yet separated from an `L^2` budget. But asymptotically the high Fourier
diagonal wins.

It also explains why the absolute Gershgorin and signed-main attempts were unstable: the one-sided
endpoint taper turns the high-frequency PNT main term into a positive diagonal contribution to
`Delta_arith`.

## 5. Route correction

The upper-complement route

```text
||C_E|| <= ||C_model|| + lambda_max(Delta_arith)_+
```

is too global for compact-root HPAC. It tries to control high Fourier modes that the HPAC source need
not excite. The compact-root proof used this bound only inside the crude commutator estimate

```text
||[C_E,S_tau]xi|| <= (||C_E||+mu)||S_tau xi||.
```

Therefore the corrected target is not APCB. It is the directional commutator bound

```text
DCB:
||[C_E,S_tau]xi|| = O_H(L^3)
```

or any sharper estimate that makes

```text
mu^(-1)||a_s^perp||||C_E^(-1)|| ||[C_E,S_tau]xi|| = o(1)
```

under `mu >= cL^2` and `||a_s^perp||=O_K(L^(1/2))`.

The route must now replace global upper complement control by a source-local commutator theorem.
