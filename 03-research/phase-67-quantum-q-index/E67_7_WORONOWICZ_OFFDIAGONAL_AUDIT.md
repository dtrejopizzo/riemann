# E67.7 — Off-diagonal audit of the Woronowicz route

**Date:** 2026-07-06.
**Role:** resolve the tension between E67.4 and E67.5 before running finite-prime numerics.

## Verdict

The Woronowicz-character route, as written in E67.5, does **not** yet escape the E67.4 no-go.

The reason is precise:

```text
Woronowicz F-matrices weight Haar/Peter-Weyl orthogonality;
they do not, by themselves, create the arithmetic off-diagonal coherence of P_lambda.
```

So a contractivity proof based on a modular Cauchy-Schwarz inequality through Haar still gives an
incoherent/absolute ceiling of the same type as `S_abs`, not the true marginal operator of norm `~1`.

## The conflict

E67.4 showed that if prime-power coefficients `X_a`, `a=(p,k)`, are Haar-orthogonal, then

```text
(id tensor h)(B^* B)
  = sum_a |c_a|^2 h(X_a^*X_a) W_a^* W_a,
```

and all cross-phase terms disappear.

E67.5 proposed a modular inequality

```text
|Phi_z(X)|^2 <= C * h(X^* F X) / d_q.
```

But summing this over prime powers still produces

```text
sum_a |c_a|^2 h(X_a^* F X_a) / d_q,
```

which is the same incoherent mechanism unless the right side contains cross terms

```text
h(X_a^* F X_b) != 0,  a != b,
```

with the correct arithmetic phases.

The true P52 prime Pick operator is not diagonal in prime powers. It is a coherent oscillatory sum:

```text
sum_n Lambda(n) n^{-1/2}
  [ n^{-it0} M(log n) + n^{it0} M(log n)^* ].
```

The gap `S_abs/T(N)` measured in E67.4 is exactly the size of the missing interference.

## What Woronowicz F can and cannot do

For an irreducible unitary corepresentation `u^alpha`, compact quantum group theory gives weighted
orthogonality schematically of the form

```text
h((u^alpha_ij)^* u^beta_kl)
  = 0                         if alpha != beta,
  = F_alpha-weighted constants / d_q(alpha)   if alpha = beta.
```

Thus:

1. If different primes live in inequivalent blocks, Haar kills cross-prime coherence.
2. If different prime powers live in different tensor-word irreps, Haar kills cross-power coherence
   except for the fusion coincidences allowed by the category.
3. Inside a single irreducible block, `F_alpha` can create weighted matrix entries, but after
   diagonalizing the positive matrix `F_alpha` this is still a positive modular weighting, not an
   arbitrary phase matrix.

Therefore `F` is not an automatic source of the phases `e^{-it0(log n-log m)}`. Those phases come from
the Mellin/evaluation channel, not from Haar.

## The only possible escape

The route can remain alive only if the prime powers are not separated into Haar-orthogonal blocks.
There must be a **coherent modular state** or **matrix coefficient state**

```text
omega_{z0,q}(X_a^* X_b)
```

such that:

```text
omega_{z0,q}(X_a^* X_b)
  carries the Mellin phase e^{-it0(log b-log a)}
```

and the same state is controlled by Haar through a nontrivial Radon-Nikodym/modular density:

```text
|omega_{z0,q}(Y)|^2 <= h(Y^* D_{z0,q} Y)
```

with `D_{z0,q}` canonical and zeta-free.

This is no longer "Haar alone". It is a coherent-state problem:

```text
Pick reproduction comes from omega_{z0,q};
contractivity must come from a Haar-dominated bound for omega_{z0,q}.
```

## New no-go boundary

If `D_{z0,q}` is chosen from the target prime kernel or from `-zeta'/zeta`, the construction is circular.

If `D_{z0,q}` is the KMS density whose partition function is

```text
product_p (1-p^{-beta})^{-1} = zeta(beta),
```

the construction falls back to Phase 51 / MW-5.

So the density must be:

```text
canonical from CQG modular data + Gamma_q Mellin covariance,
not from zeta, not from P_lambda, not from zeros.
```

## Revised Woronowicz gates

### W0 — off-diagonal source

Identify the state `omega_{z0,q}`. Haar alone is not enough.

### W1 — off-diagonal reproduction

For finite `{2,3,5}`, `k<=2`, compute

```text
G_mod[a,b] = omega_{z0,q}(X_a^* X_b),
G_exact[a,b] = exp(-it0(log b-log a)) * archimedean shift factor.
```

Then report

```text
offdiag_error =
  || offdiag(G_mod) - offdiag(G_exact) || / || offdiag(G_exact) ||.
```

This replaces the weaker `mech != 0` test.

### W2 — Haar domination

Prove or refute a canonical inequality

```text
|omega_{z0,q}(Y)|^2 <= h(Y^* D_{z0,q} Y),
```

where the resulting bound is not the incoherent `S_abs`.

### W3 — anti-KMS-zeta

Check that

```text
h(D_{z0,q}) != zeta(beta)
```

or any Euler product/partition function equivalent to Bost-Connes.

### W4 — DH falsifier

DH must fail either the Euler/fusion source of `X_a` or the canonical construction of
`omega_{z0,q}`.

## Consequence

The E67.5 claim must be weakened:

```text
Woronowicz characters identify a possible Mellin/modular vocabulary,
but Haar-weighted Cauchy-Schwarz alone cannot prove Omega_7.
```

The live mathematical object, if it exists, is not just `(A,h,F)`.

It is:

```text
(A, h, F, omega_{z0,q}, D_{z0,q})
```

with `omega` preserving arithmetic interference and `D` giving a non-circular Haar domination.

This is the new exact bottleneck of Phase 67.

## Conditional no-go statement

If every canonical state available from the chosen compact quantum group is generated from Haar,
Woronowicz characters, and blockwise `F_alpha` matrices in a way that preserves Peter-Weyl block
orthogonality, then Phase 67-W is dead:

```text
canonical CQG modular data only
  => no arithmetic off-diagonal
  => incoherent S_abs ceiling
  => no QSC-contract.
```

To stay alive, the construction must exhibit a canonical state whose GNS vector is coherent across the
prime-power labels. This state must be more structured than Haar but less arithmetically loaded than
`-zeta'/zeta`.

That is the fine line:

```text
too little coherence  -> E67.4 no-go;
too much encoded data  -> Phase 51/MW-5 or Omega_7 circularity.
```
