# E72.280 -- Variance-bracket gate

**Purpose.** State the correct remaining condition for the bracket in E72.278.

The Cauchy-factor identity contains

```text
B_x(z,tau)
= -2tau/(z^2-tau^2)-V_x(tau),
V_x(tau)=<xi_x,S_tau xi_x>,
S_tau=2tau(tau^2-D^2)^(-1).
```

The first term is uniformly bounded for fixed Cauchy compact `K subset C\R` and fixed height
`0<tau<=H`.  The issue is `V_x(tau)`.

## Correct gate

The operator norm of `S_tau` is the wrong object: roots may be extremely close to mesh points, so
`||S_tau||op` can be huge.  What matters is the vector channel:

```text
VBG(beta):
sup_{0<tau_j<=H} ||S_tau_j xi_x|| = O_{H}(L_x^beta)
```

for some

```text
beta < 3/2.
```

Indeed,

```text
|V_x(tau_j)| <= ||S_tau_j xi_x|| ||xi_x|| = ||S_tau_j xi_x||.
```

Together with E72.279,

```text
|M_x(z)|/mu_x = O_K(L_x^(-3/2)),
```

this gives

```text
mu_x^(-1)|M_x(z)B_x(z,tau_j)| -> 0
```

for fixed `K,H`.  Thus `VBG(beta<3/2)` closes the diagonal compact-root term.

The strongest numerically suggested version is much better:

```text
sup_{0<tau_j<=H} ||S_tau_j xi_x|| = O_H(1),
```

but the proof only needs sub-`L^(3/2)` growth.

## Probe

Run:

```text
python3 E72_280_variance_bracket_gate_probe.py
```

Output:

```text
E72.280 variance-bracket gate probe
Measures V_x(tau)=<xi,S_tau xi>, ||S_tau xi||, and ||S_tau||op on roots 0<tau<=8.
lam L roots maxV max||Sxi|| max||S||op maxV/L max||Sxi||/L
 16 5.545177     7 2.057616e-02 1.018889e-01 7.388196e+01 3.710641e-03 1.837432e-02
 20 5.991465     7 2.536685e-02 2.200618e-01 6.677508e+00 4.233831e-03 3.672922e-02
 24 6.356108     5 1.103267e-02 5.441412e-02 5.697349e+00 1.735758e-03 8.560918e-03
 28 6.664409     6 7.974738e-03 7.659785e-02 5.842513e+02 1.196616e-03 1.149357e-02
 32 6.931472     8 4.928516e-03 3.001751e-02 4.620271e+06 7.110345e-04 4.330611e-03
```

## Reading

The operator norm explodes in some windows (`lambda=32` has `||S_tau||op ~ 4.6e6`), but the vector
channel remains small (`||S_tau xi|| ~ 3e-2`).  Therefore the proof must exploit the actual ground
vector, not mesh separation.

This identifies the remaining diagonal theorem exactly:

```text
VBG(beta<3/2):   sup_{0<tau_j<=H} ||S_tau_j xi_x|| = O_H(L^beta).
```

Once VBG is proved, the diagonal compact-root term is closed by E72.278--E72.279.
