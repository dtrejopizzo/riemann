# E77.7aq - Even-channel reduction

**Run:** 2026-07-18.

## 1. Purpose

E77.7ap showed that the missing shell bridge is still quadratic:

```text
PROJECTED-QUADRATIC-BRIDGE.
```

The next admissible question is structural, not scalar:

```text
on the 4-node shell, does the shorted quadratic form really live on all
four coordinates, or does symmetry force a smaller invariant channel?
```

This note answers that question.

## 2. Inputs

Two sources are used:

1. Existing geometric shell residual data:

```text
E77_7h_geometric_shell_residual_results.json
```

2. New explicit even/odd decomposition:

```text
E77_7aq_even_odd_shell_probe.py
E77_7aq_even_odd_shell_results.json
```

The new probe takes the shell basis

```text
(-m,-n,n,m)
```

and rewrites it in the orthonormal even/odd basis

```text
even_n, odd_n, even_m, odd_m.
```

It then conjugates the shell shorted matrix into that basis and decomposes
both the residual vector and the shorted energy.

## 3. Residual parity

The geometric shell residual file already showed that, on the live shell
steps, the residual is left/right symmetric to extreme precision for both
builds.

### Zeta

For `16->18`:

```text
(-18,-17,17,18) residual =
( 9.2897e-31, -2.3151e-32, -2.3151e-32,  9.2897e-31)
```

For `18->20`:

```text
(-20,-19,19,20) residual =
(-2.1964e-33, -2.5189e-34, -2.5189e-34, -2.1964e-33)
```

### Planted falsifier

For `16->18`:

```text
( 0.0725764, 0.0156100, 0.0156100, 0.0725764)
```

For `18->20`:

```text
( 0.0485139, 0.0939687, 0.0939687, 0.0485139)
```

So the residual itself is already in the even channel for both builds.  This
reduction is therefore neutral to the falsifier.

## 4. Shorted-form decomposition

The new even/odd probe gives the decisive refinement on zeta.

### Zeta, `16->18`

```text
odd/even residual norm      = 5.08e-36
odd energy / total energy   = 4.28e-68
even-odd block / full block = 3.49e-38
```

Moreover

```text
even_energy_decoupled = total shorted_energy
```

to the recorded precision.

### Zeta, `18->20`

```text
odd/even residual norm      = 5.66e-32
odd energy / total energy   = 3.48e-60
even-odd block / full block = 4.27e-34
```

Again,

```text
even_energy_decoupled = total shorted_energy
```

to the recorded precision.

So on the live zeta shell steps the shorted quadratic form does not merely
have an even residual; it is effectively block-diagonal in the even/odd
splitting, and the odd channel carries none of the shell energy.

## 5. Consequence

This yields a strict reduction of the live quadratic bridge:

```text
PROJECTED-QUADRATIC-BRIDGE
=> EVEN-CHANNEL-QUADRATIC-BRIDGE.
```

The shell front no longer needs a 4-coordinate bridge theorem.  The candid
live object is now the 2x2 even block:

```text
EVEN-CHANNEL-QUADRATIC-BRIDGE:
  identify and control the shorted quadratic form on the even shell pair
  only, since the odd channel is inert and the even/odd coupling is
  negligible on the live path.
```

This is an admissible reduction because:

1. it is proved from the exact shell shorted decomposition;
2. it implies the previous quadratic bridge target;
3. it does not rely on a zeta-only parity phenomenon, since the residual
   parity is also seen in the planted build.

## 6. What is still open

Parity is not the discriminant.

Both zeta and plant are even at the shell-residual level, so the remaining
difficulty lies **inside the even 2x2 block**.  That is now the smallest
candid shell-facing object:

```text
the zeta/plant difference must be in the signed geometry of the even block,
not in odd leakage.
```

So the next theorem should be written directly for the even block entries and
their induced quadratic form, not for the full 4x4 shell matrix.

## 7. Status

```text
proved:
  the live shell residual is even on the tested zeta and planted steps;
  on zeta, the shorted energy is carried entirely by the even channel to
  overwhelming precision;
  the even/odd coupling of the shorted matrix is negligible on the live
  zeta steps.

reduced:
  PROJECTED-QUADRATIC-BRIDGE
  -> EVEN-CHANNEL-QUADRATIC-BRIDGE.

clarified:
  parity is not the falsifier separator; the live difference must sit inside
  the 2x2 even block itself.
```
