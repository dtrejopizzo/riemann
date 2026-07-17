# E72.283 -- Compact-root commutator bound

**Purpose.** Close the compact-root commutator term under the natural upper complement bound.

E72.277 splits the corrected HPAC residual into a diagonal term and a commutator term:

```text
K_x(s,tau_j)
= -i alpha(tau_j)mu_x^(-1)
   <a_s^perp,C_E^(-1)[C_E,S_tau_j]xi_x>.
```

The diagonal term is closed by E72.278--E72.282, assuming the pole-even lower gap.  This note gives a
simple sufficient bound for `K_x`.

## Sufficient theorem

Assume, for fixed compact Cauchy set `K` and root height `H`, that:

```text
1. Lower gap:       mu_x >= c L^2.
2. Upper complement: ||C_E|| <= C L^2.
3. VBG:             sup_{tau_j<=H}||S_tau_jxi_x|| <= C_H L.
```

Then the compact-root commutator term tends to zero uniformly on `K,H`.

Indeed,

```text
||[C_E,S_tau]xi||
= ||C_E S_tau xi - S_tau C_E xi||
<= ||C_E||||S_tau xi|| + mu_x||S_tau xi||
<= C_H L^3.
```

Also, by the same mesh Cauchy-Schwarz estimate used in E72.279,

```text
||a_s^perp|| <= ||a_s|| = O_K(L^(1/2)).
```

Therefore

```text
|K_x(s,tau_j)|
<= C_{K,H} mu_x^(-1) ||a_s^perp|| ||C_E^(-1)|| ||[C_E,S_tau_j]xi||
<= C_{K,H} L^(-2) L^(1/2) L^(-2) L^3
= O_{K,H}(L^(-1/2)) -> 0.                              (COMM)
```

This proof does not use the much stronger numerical cancellation of the commutator.  It only requires
the upper complement bound `||C_E||=O(L^2)`, which is the natural partner of the pole-even lower gap.

## Probe

Run:

```text
python3 E72_283_commutator_bound_probe.py
```

Output:

```text
E72.283 commutator-bound probe
Crude compact-root commutator scale: ||a|| ||C_E|| ||S_tau xi|| / mu^2.
lam L mu opC opC/L2 ||a|| max||Sxi|| crude
 16 5.545177 1.232544e+01 1.882543e+01 6.122293e-01 2.745413e+00 1.018889e-01 3.466364e-02
 20 5.991465 1.596102e+01 2.315760e+01 6.451008e-01 2.006613e+00 2.200618e-01 4.014027e-02
 24 6.356108 1.965549e+01 2.719209e+01 6.730699e-01 3.342492e+00 5.441412e-02 1.280139e-02
 28 6.664409 2.339219e+01 3.112734e+01 7.008396e-01 2.277885e+00 7.659785e-02 9.925413e-03
 32 6.931472 2.716069e+01 3.551406e+01 7.391787e-01 3.770799e+00 3.001751e-02 5.449124e-03
```

## Reading

The observed commutator itself is far smaller than this crude bound, often at roundoff, but the crude
bound already has the right asymptotic exponent once `||C_E||=O(L^2)` is available.

Thus the **compact-root HPAC theorem** is reduced to:

```text
lower gap:          mu_x >= cL^2,
upper complement:   ||C_E|| <= CL^2,
corrected source/gauge identities.
```

The lower gap is MCOER2-pole-even.  The upper complement is now the remaining model-size estimate
needed for the compact-root commutator.
