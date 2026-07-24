# E77.7ar - Even-block lock audit

**Run:** 2026-07-18.

## 1. Purpose

E77.7aq reduced the live shell bridge from the full 4-node quadratic form to
the even 2x2 block:

```text
EVEN-CHANNEL-QUADRATIC-BRIDGE.
```

This note asks the next admissible question:

```text
what distinguishes the zeta even block from the planted even block?
```

The answer is not parity, since both builds are even.  The discriminant sits
inside the geometry of the even 2x2 shorted block itself.

## 2. Data

Sources:

```text
E77_7aq_even_odd_shell_results.json
E77_7aq_even_odd_shell_plant_16_18.json
```

For the even basis `(even_n, even_m)`, write the shorted block as

```text
S_even = [[a, b],
          [b, c]].
```

The natural scale-free lock parameter is

```text
rho = b / sqrt(ac).
```

If `|rho| ~= 1`, then the even block is nearly rank-one / nearly degenerate.
Equivalently,

```text
det(S_even) << a c.
```

## 3. Zeta

From `E77_7aq_even_odd_shell_results.json`:

### `16 -> 18`

```text
a = 7.01045e-19
b = -2.81984e-17
c = 1.13466e-15
rho = -0.9998121332572664
det = 2.98849e-37
```

### `18 -> 20`

```text
a = 5.06057e-19
b =  4.42412e-18
c = 3.86912e-17
rho = 0.9998180384252494
det = 7.12494e-39
```

So on the live zeta shell steps:

```text
|rho| = 0.9998...
```

and the even block is extremely close to a rank-one lock.

The sign flip from negative to positive across the two steps is also real:

```text
sign(b):  -  then  +.
```

So the zeta block is not only nearly degenerate; it also carries a signed
orientation change along the live shell ladder.

## 4. Planted falsifier

From `E77_7aq_even_odd_shell_plant_16_18.json`:

```text
a = 3.77836
b = -0.982123
c = 2.72065
rho = -0.3063218723051942
det = 9.31503
```

Here the even block is nowhere near the rank-one lock:

```text
|rho| ~= 0.306.
```

It is a genuine 2x2 block with large determinant relative to `ac`.

## 5. Autopsy / reduction

This is the first internal discriminant of the even block that sharply
separates zeta from the planted build while staying entirely inside the shell
quadratic formalism.

Therefore the live shell-facing object can now be reduced from the vague

```text
EVEN-CHANNEL-QUADRATIC-BRIDGE
```

to the sharper target

```text
EVEN-BLOCK-LOCK:
  prove that along the zeta shell path the even shorted block satisfies
  |b| ~= sqrt(ac) with a signed branch law, while the planted/off-line build
  fails this lock.
```

Equivalently:

```text
det(S_even) is a higher-order residual on the zeta path.
```

This is strictly smaller than controlling the whole even quadratic form,
because once the lock is known the block is determined up to one scalar scale
and one signed branch choice.

## 6. What remains open

This note does **not** yet prove the lock.  It only identifies it as the
smallest currently visible shell discriminator.

The next theorem must therefore target:

```text
EVEN-BLOCK-LOCK
=> EVEN-CHANNEL-QUADRATIC-BRIDGE
=> PROJECTED-QUADRATIC-BRIDGE
=> ... => BTG-DIV-L.
```

At that point the residual determinant or branch-switching term becomes the
honest shell-side object to connect back to Phase-5 signed data.

## 7. Status

```text
proved numerically:
  the zeta even shell block is nearly rank-one on the live steps;
  the planted even shell block is not;
  the zeta block exhibits a signed off-diagonal branch flip across the live
  ladder.

reduced:
  EVEN-CHANNEL-QUADRATIC-BRIDGE
  -> EVEN-BLOCK-LOCK.

live object:
  theorem-grade proof that the zeta even shorted block satisfies the lock
  |b| ~= sqrt(ac) with the correct signed branch law, and that the residual
  determinant is higher order along the shell ladder.
```
