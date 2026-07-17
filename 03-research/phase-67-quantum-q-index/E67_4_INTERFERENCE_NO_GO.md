# E67.4 — Interference no-go for the strict free-product CQG

**Date:** 2026-07-06.
**Role:** close the first post-group-like candidate. The prime-colored free-product CQG is useful as a
baseline, but it cannot be the final `QSC-exist + QSC-contract` mechanism if Haar orthogonality erases
the arithmetic interference of `P_lambda`.

## Problem

After rejecting group-like prime generators, the first compact noncommutative candidate was

```text
G_lambda = *_{p <= e^lambda} U_N^+(F_p),
```

with each prime carried by a non-trivial corepresentation and prime powers represented by tensor words.
This fixes the Bost-Connes collapse, but creates a new obstruction:

```text
free-product Haar orthogonality separates prime colors/words too strongly.
```

If the current is

```text
B = sum_{p^k} c_{p,k} X_{p,k} tensor W_{k log p},
```

and the `X_{p,k}` lie in mutually orthogonal Peter-Weyl blocks for Haar, then

```text
h(X_{p,k}^* X_{q,l}) = 0  unless (p,k)=(q,l),
```

so the Haar Gram of `B` becomes a diagonal/absolute sum of per-prime-power energies.

That is not the P52 prime Pick operator.

## Exact P52 structure

At an interior gauge `z0=t0-iy`, `y>1/2`, the P52 harness decomposes

```text
P_lambda = sum_m P_m,
P_m = herm(pick_jet(h_m)),
h_m(z) = i Lambda(m) m^{-1/2} exp(-i z log m).
```

Equivalently, in the leading Laguerre/Szego basis,

```text
(T_N)_{jk}
 =
 -1/log(|t0|/2pi)
 sum_{n>=2} Lambda(n)/sqrt(n)
 [
   n^{-it0} m_jk(log n)
   + n^{it0} conjugate(m_kj(log n))
 ]
 + archimedean remainder.
```

This is a coherent signed/oscillatory linear sum. Its small norm is not obtained by bounding each
prime-power block independently; it depends on phase interference among the terms.

## Numerical witness from the existing P52 harness

The existing script

```text
riemann-program/04-papers/P52-riemann-proof-audit/omega7_operator_interference.py
```

measures:

```text
T(N)      = || A_N^{-1/2} P_lambda A_N^{-1/2} ||,
S_abs(N) = sum_m Lambda(m) * per-term whitened ceiling,
I(N)     = S_abs(N)/T(N).
```

Partial run, `t0=10`, `y=1`, prime powers up to `2e6`:

```text
N=4  ||S P S|| = 0.99999993423   S_abs =   219.4407   I =   219.441
N=8  ||S P S|| = 1.0             S_abs = 18683.3261   I = 18683.326
```

The true whitened prime operator sits at the Omega_7 boundary (`~1`), while the non-interfering
absolute/orthogonalized ceiling is larger by factors `10^2` to `10^4` already at tiny `N`.

So a strict free-product Haar model cannot be the final mechanism: it destroys exactly the interference
that keeps `P_lambda` marginal.

## Formal no-go

Let `(A,h)` be a compact quantum group and suppose the prime-power coefficients `X_a`, `a=(p,k)`,
satisfy Haar orthogonality

```text
h(X_a^* X_b) = d_a^{-1} delta_ab.
```

Let

```text
B = sum_a c_a X_a tensor W_a
```

with `W_a` the Mellin-shift block. Then the Haar-induced Gram is

```text
(id tensor h)(B^*B)
  = sum_a |c_a|^2 d_a^{-1} W_a^* W_a.
```

It has no cross-phase channel and no linear oscillatory sum

```text
sum_a Lambda(a) e^{-it0 log a} M(log a) + conjugate.
```

Therefore it cannot reproduce `P_lambda` unless one of the following happens:

1. the `X_a` are collapsed to a counit/character channel, which returns to Bost-Connes/group-like;
2. the Haar state is not the state used to compute the Pick jet, so `QSC-contract` no longer comes from
   Haar;
3. an additional modular/coherent channel couples different Peter-Weyl blocks and preserves the
   arithmetic phases.

Only option 3 remains alive.

## Consequence

The free-product candidate is demoted:

```text
*_{p <= e^lambda} U_N^+(F_p)
```

is a **baseline/falsifier**, not the final CQG.

The next live route must keep both:

- **interference channel**: reproduces the coherent linear prime Pick operator;
- **Haar/q-dimension channel**: supplies a nontrivial contractivity inequality.

This points to Woronowicz characters/modular data rather than pure Haar orthogonalization.
