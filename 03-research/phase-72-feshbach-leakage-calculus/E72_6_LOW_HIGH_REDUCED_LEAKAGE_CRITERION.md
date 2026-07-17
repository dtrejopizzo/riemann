# E72.6 -- Low/high criterion for reduced leakage

**Date:** 2026-07-08.
**Role:** turn the reduced leakage target into a finite-dimensional cancellation problem plus a uniform
tail estimate, without diagonalizing zeros or using additive Green assembly.

## 0. Why this criterion is needed

E72.4 states the exact missing estimate as

```text
||C_x^{-1}b_x|| -> 0,
b_x = Q_x(H_x-H_x^0)k_x.
```

This is still global. To attack it, we need a decomposition that respects the Feshbach audit:

- no local inverse;
- no additive Green matrix;
- no pointwise Christoffel localization;
- no row-column `l1` Schur bound.

The only safe split is spectral for the **actual compressed complement** `C_x`.

## 1. Abstract criterion

Let `C_x` be positive self-adjoint on `Q_xH`, with compact resolvent in the finite/restricted model, and
let

```text
C_x e_{x,j} = lambda_{x,j} e_{x,j},       0 < lambda_{x,1} <= lambda_{x,2} <= ...
```

For

```text
b_x = Q_x(H_x-H_x^0)k_x,
b_{x,j} = <e_{x,j}, b_x>,
```

define the reduced low and tail masses

```text
L_x(M)^2 := sum_{j<=M} |b_{x,j}|^2/lambda_{x,j}^2,
T_x(M)^2 := sum_{j>M}  |b_{x,j}|^2/lambda_{x,j}^2.
```

### Theorem 72.6 -- low/high reduced leakage criterion

Assume:

```text
(LH1)  for every fixed M,       L_x(M) -> 0 as x -> infinity;
(LH2)  uniform reduced tightness: lim_{M->infty} limsup_x T_x(M) = 0.
```

Then

```text
||C_x^{-1}b_x|| -> 0.
```

### Proof

By Parseval in the spectral basis of the actual `C_x`,

```text
||C_x^{-1}b_x||^2
  = sum_j |b_{x,j}|^2/lambda_{x,j}^2
  = L_x(M)^2 + T_x(M)^2.
```

Given `eps>0`, choose `M` so that `limsup_x T_x(M)<eps/2` by (LH2). For this fixed `M`, choose `x`
large enough that `L_x(M)<eps/2` by (LH1). Then `||C_x^{-1}b_x||<eps`. `QED`

## 2. Variational form

Let `E_x(M)` be the span of the first `M` complement modes of the actual `C_x`, and let
`E_x(M)^\perp_C` denote the spectral tail. The criterion is equivalent to:

### Low modes

For each fixed `M`,

```text
sup_{v in E_x(M), C_xv != 0}
 |<v,b_x>| / ||C_xv|| -> 0.
```

### High modes

The functionals are uniformly tight in the `C_x`-graph dual:

```text
lim_{M->infty} limsup_x
sup_{v in E_x(M)^\perp_C, C_xv != 0}
 |<v,b_x>| / ||C_xv|| = 0.
```

This is exactly the E72.4 dual norm, split into finite cancellation plus graph-tail compactness.

## 3. Why this is not the old Feshbach wall

The split is over the spectrum of the **actual** compressed complement:

```text
C_x = Q_x(H_x-mu_x^0-a_x)Q_x.
```

Therefore all cross terms and all non-additive Feshbach effects are already inside `C_x`.

We are not claiming:

```text
C_x^{-1} = sum_p C_{x,p}^{-1}.
```

We are only using the spectral theorem for the already-assembled complement operator.

## 4. What LH1 means arithmetically

LH1 is a finite-dimensional statement. For each fixed number of complement modes, one must prove

```text
<e_{x,j},(H_x-H_x^0)k_x> / lambda_{x,j} -> 0,
      j=1,...,M.
```

This is where the Sonin/Feshbach integration-by-parts identity should act. It does not need to control
all modes at once; it must annihilate the finitely many slow channels that can move the ground vector.

This is much weaker than raw leakage and avoids the incoherent ceiling.

## 5. What LH2 means arithmetically

LH2 is the genuine compactness/tightness statement. It says the residual force `b_x` does not place
macroscopic mass in complement modes whose inverse weight remains visible.

A usable sufficient condition is:

```text
there exists a stronger positive operator W_x with W_x <= C_x^2 on the high tail,
and <b_x, W_x^{-1} b_x> has vanishing tail.
```

In practice, `W_x` should come from the prolate/Sonin high-frequency energy, not from a local prime
decomposition. This matches Phase 60: high modes may be large in ambient norm but invisible in the
shorted/reduced norm.

## 6. Falsifier

For Davenport--Heilbronn or planted off-line data, failure can occur in either channel:

```text
LH1 fails: a fixed slow channel has nonzero reduced forcing;
LH2 fails: reduced forcing escapes into an infinite tail.
```

This is sharper than the old falsifier `liminf ||b_x||/g_x > 0`, because it ignores harmless high-mode
raw size and sees only the component capable of moving the eigenvector.

## 7. The next target

The Phase 72 proof is now reduced to two statements:

```text
Low-channel cancellation:
  for every fixed M, L_x(M)->0.

Reduced tightness:
  lim_{M->infty} limsup_x T_x(M)=0.
```

The first is finite and should be attacked by exact Sonin/Feshbach integration by parts. The second is a
compactness estimate in the actual Feshbach graph norm. Both avoid the prior Feshbach mistakes recorded
in E72.5.

