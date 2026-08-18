# E77.7as - Locked eigendirection audit

**Run:** 2026-07-18.

## 1. Purpose

E77.7ar identified the even 2x2 shell block as the live shell-facing object
and isolated the numerical lock

```text
|b| ~= sqrt(ac).
```

But the shell energy is not determined by the block alone.  For a positive
2x2 block, the quadratic inverse pairing also depends on **which eigenvector
the residual points toward**.

This note audits that directional component.

## 2. Setup

For the even block

```text
S_even = [[a,b],[b,c]],
```

let

```text
lambda_small <= lambda_large
```

be its eigenvalues, with orthonormal eigenvectors

```text
v_small, v_large.
```

Write the even residual as

```text
r_even = alpha_small v_small + alpha_large v_large.
```

Then the shell energy in the even channel is

```text
<r_even, S_even^{-1} r_even>
= |alpha_small|^2 / lambda_small + |alpha_large|^2 / lambda_large.
```

So a nearly degenerate block is not enough: if `alpha_small` is not
suppressed, the inverse pairing blows up through `1/lambda_small`.

## 3. Zeta

Using the even-block data from `E77_7aq_even_odd_shell_results.json`:

### `16 -> 18`

```text
lambda_small = 2.63219e-22
lambda_large = 1.13536e-15
alpha_small  = 9.09676e-35
alpha_large  = 1.31418e-30
|alpha_small| / |alpha_large| = 6.92e-5
```

Energy split:

```text
small-mode piece = 3.14e-47
large-mode piece = 1.52e-45
```

So despite the tiny `lambda_small`, the residual is almost orthogonal to the
small mode and the energy is carried by the large mode.

### `18 -> 20`

```text
lambda_small = 1.81772e-22
lambda_large = 3.91970e-17
alpha_small  = 1.04438e-36
alpha_large  = 3.12658e-33
|alpha_small| / |alpha_large| = 3.34e-4
```

Energy split:

```text
small-mode piece = 6.00e-51
large-mode piece = 2.49e-49
```

Again the zeta residual avoids the small mode.

## 4. Planted falsifier

From `E77_7aq_even_odd_shell_plant_16_18.json`:

```text
lambda_small = 2.13404
lambda_large = 4.36497
alpha_small  = -9.94374e-2
alpha_large  = 3.36784e-2
|alpha_small| / |alpha_large| = 2.95
```

Energy split:

```text
small-mode piece = 4.63e-3
large-mode piece = 2.60e-4
```

Here the planted residual points mainly **into** the small mode instead of
avoiding it.

## 5. Consequence

This isolates a stricter live object than E77.7ar.

The zeta shell mechanism is not merely:

```text
EVEN-BLOCK-LOCK.
```

It is:

```text
LOCKED-EIGENDIRECTION:
  the even block is nearly rank-one, and the even residual is aligned with
  the large eigendirection rather than the small one.
```

Equivalently:

```text
the coefficient of the residual on the small eigendirection is a higher-order
object on the zeta shell path.
```

This is strictly smaller than the raw block lock, because once the lock is
known, the remaining shell difficulty is exactly the suppression of the
small-mode coefficient.

## 6. Reduction

The shell front can therefore be reduced again:

```text
LOCKED-EIGENDIRECTION
=> EVEN-BLOCK-LOCK
=> EVEN-CHANNEL-QUADRATIC-BRIDGE
=> PROJECTED-QUADRATIC-BRIDGE
=> ... => BTG-DIV-L.
```

The smallest shell-facing object currently visible is:

```text
SMALL-MODE-SUPPRESSION:
  prove that on the zeta shell path the even residual coefficient on the
  small eigendirection is higher order than its large-mode coefficient.
```

## 7. Status

```text
proved numerically:
  zeta avoids the small eigendirection of the locked even block;
  planted does not;
  the zeta shell energy is carried by the large eigendirection even though
  the block itself is nearly singular.

reduced:
  EVEN-BLOCK-LOCK
  -> LOCKED-EIGENDIRECTION
  -> SMALL-MODE-SUPPRESSION.

live object:
  theorem-grade proof that the small-mode coefficient is a higher-order
  residual on the zeta shell ladder.
```
