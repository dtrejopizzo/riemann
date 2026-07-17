# E67.6 — Normalization gates for the Woronowicz route

**Date:** 2026-07-06.
**Role:** prevent the modular route from hiding a scalar Euler/counit normalization.

## The normalization risk

The P52 prime Taylor coefficients use

```text
h_P(z) = i sum_{n>=2} Lambda(n) n^{-1/2} exp(-i z log n),
s = 1/2 + i z.
```

At `z0=t0-iy`, this coefficient is

```text
Lambda(n) n^{-1/2-y} exp(-i t0 log n).
```

So a Woronowicz character channel must not insert the same `n^{-1/2}` twice.

There are two possible normalizations:

## Normalization A — modular character carries full Dirichlet weight

```text
Phi_z(X_{p,k}) = p^{-k(1/2 + i z)}
```

and the current is

```text
B_lambda = sum_{p^k} (log p) Phi_z(X_{p,k}) arch_q(k log p).
```

This is closest to `-zeta'/zeta`. The danger is that it looks too much like a scalar character unless
`X_{p,k}` remains a nontrivial coefficient in the Haar bound.

## Normalization B — modular character carries only the oscillatory/Mellin shift

```text
Phi_z(X_{p,k}) = exp(-i z k log p),
```

and the current keeps the classical half-density:

```text
B_lambda = sum_{p^k} (log p) p^{-k/2} Phi_z(X_{p,k}) arch_q(k log p).
```

This matches the earlier Phase 67 notation. The danger is that the `p^{-k/2}` is then outside the CQG
and may be doing all the contractive work.

## Required gate

For either normalization, the same modular matrix `F_p` must satisfy three equations:

```text
(N1)  Woronowicz evaluation:
      Phi_z(X_{p,k}) gives exactly the required p,z dependence.

(N2)  Haar norm:
      h(X_{p,k}^* X_{p,k}) is explicitly d_q(p,k)^(-1) times F_p-weights.

(N3)  No scalar collapse:
      the Schur bound changes if X_{p,k} is replaced by the counit value.
```

The allowed proof shape is:

```text
Pick reproduction = N1 + Gamma_q Mellin calculus;
contractivity     = N2 + modular Cauchy-Schwarz;
new mechanism     = N3.
```

The forbidden proof shape is:

```text
Pick reproduction = choose Phi_z to be -zeta'/zeta;
contractivity     = observe the resulting matrix is contractive.
```

## First finite-prime target, revised by E67.7

For a tiny cutoff, e.g. `p in {2,3,5}`, `k<=2`, compute four objects:

```text
P_exact      = P52 prime Pick block from h8lab / truncated Euler sum;
P_mod_A      = Woronowicz normalization A block;
P_mod_B      = Woronowicz normalization B block;
P_counit     = same scalar/counit baseline.
```

Then report:

```text
repro_A = ||P_mod_A - P_exact|| / ||P_exact||,
repro_B = ||P_mod_B - P_exact|| / ||P_exact||,
mech_A  = ||A^{-1/2} P_mod_A A^{-1/2}|| - ||A^{-1/2} P_counit A^{-1/2}||,
mech_B  = ||A^{-1/2} P_mod_B A^{-1/2}|| - ||A^{-1/2} P_counit A^{-1/2}||.
```

E67.7 shows that `mech != 0` is not discriminating enough. A diagonal-but-different Haar operator can
pass it while still dying by the E67.4 interference no-go. The decisive observable is off-diagonal
coherence:

```text
offdiag_A =
  || offdiag(P_mod_A) - offdiag(P_exact) || / || offdiag(P_exact) ||,

offdiag_B =
  || offdiag(P_mod_B) - offdiag(P_exact) || / || offdiag(P_exact) ||.
```

If the model is expressed at the prime-power coefficient level, use instead

```text
G_mod[a,b]   = omega_{z0,q}(X_a^* X_b),
G_exact[a,b] = exp(-it0(log b-log a)) * arch_shift(a,b),
offdiag_G    = ||offdiag(G_mod-G_exact)|| / ||offdiag(G_exact)||.
```

Expected:

- If `offdiag` fails, the route is still E67.4: Haar has diagonalized away the interference.
- If `offdiag` passes but the dominating density is KMS-zeta/Bost-Connes, the route dies by Phase 51.
- If `offdiag` passes and the Haar domination is canonical and zeta-free, Phase 67 has a real
  finite-prime CQG effect to analyze.

## Current status

The Woronowicz route is not yet closed. After E67.7, the remaining work is not merely normalization. It
requires an off-diagonal coherent modular state `omega_{z0,q}` plus a non-circular Haar domination
density `D_{z0,q}`.
