# E78.88 - The modulus quotient has an exact growth/sector split, but the sector factor is an old detector

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.87 reduced the open modulus branch to

```text
SIGMA-MONOTONE-MODULUS-QUOTIENT
+ LEFT-ENDPOINT-MODULUS-QUOTIENT.                       (MGS-1)
```

Before trying to prove monotonicity directly, we should expose the exact
anatomy of the modulus quotient itself.

This note does that. The result explains the observed `1/N` scale exactly, and
it also shows where the next inadmissible shortcut would re-enter.

## 2. Exact split

From E78.32,

```text
modulus_term_N
 = 2 (|u_N+2| - |u_N|) s_N+2,                           (MGS-2)
```

where

```text
s_N := Im(u_N)/|u_N|.                                   (MGS-3)
```

Therefore the modulus quotient from E78.85 becomes

```text
MODULUS-QUOTIENT_N(sigma)
 = (-SAFEDELTA_N(i sigma))
   / [2 (|u_N+2|-|u_N|) s_N+2].                         (MGS-4)
```

Multiplying and dividing by `N` yields

```text
MODULUS-QUOTIENT_N(sigma)
 = GROWTH-QUOTIENT_N(sigma) * SECTOR-FACTOR_N(sigma),   (MGS-5)
```

with

```text
GROWTH-QUOTIENT_N(sigma)
 := N * (-SAFEDELTA_N(i sigma))
    / [2 (|u_N+2|-|u_N|)],                              (MGS-6)

SECTOR-FACTOR_N(sigma)
 := 1 / [N s_N+2].                                      (MGS-7)
```

Equivalently,

```text
N * MODULUS-QUOTIENT_N(sigma)
 = GROWTH-QUOTIENT_N(sigma) / s_N+2.                    (MGS-8)
```

This is the exact source of the `1/N` behavior seen earlier: the bare modulus
quotient carries an explicit `1/N` factor before any extra estimate is used.

## 3. Probe audit

Companion:

```text
E78_88_modulus_growth_split_probe.py
E78_88_modulus_growth_split_results.json
```

### Exactness

The split reconstructs to roundoff:

```text
max reconstruction error          < 6e-17,
max weighted reconstruction error < 6e-16.             (MGS-9)
```

### Zeta size on the certified ladder

Across the current zeta ladder:

```text
GROWTH-QUOTIENT_N
  min    = 1.928708,
  median = 2.232599,
  max    = 2.572961,                                   (MGS-10)

SECTOR-FACTOR_N
  min    = 0.062513,
  median = 0.086551,
  max    = 0.125232.                                   (MGS-11)
```

Representative rows:

```text
sigma=1.0, N= 8:
  growth quotient = 2.556047,
  sector factor   = 0.125232,
  modulus quotient= 0.320100

sigma=1.0, N=20:
  growth quotient = 2.179983,
  sector factor   = 0.051548,
  modulus quotient= 0.112374.                          (MGS-12)
```

So the observed decay of the modulus quotient is driven largely by the explicit
`1/N` sector factor, while the growth quotient itself remains an `O(1)` object.

## 4. Consequence

This gives a stricter reduced target:

```text
GROWTH-QUOTIENT-CONTROL
+ SECTOR-FACTOR-CONTROL
=> MODULUS-QUOTIENT.                                   (MGS-13)
```

More explicitly, any theorem-grade bounds

```text
GROWTH-QUOTIENT_N(sigma) <= C_1,                        (MGS-14)
s_N+2 >= c_0 > 0                                        (MGS-15)
```

would imply

```text
MODULUS-QUOTIENT_N(sigma) <= C_1 / (N c_0).             (MGS-16)
```

That is stronger than the earlier opaque endpoint formulation because the
`1/N` scale is now exact, not guessed from numerics.

## 5. Candid autopsy

There is also a warning here.

The factor

```text
s_N+2 = Im(u_N+2)/|u_N+2|                               (MGS-17)
```

is precisely the safe-axis sector share that Phase 77 already identified as a
build-separating certificate. On zeta it stays close to `1`; on the standard
planted falsifier it can be tiny or negative.

So `(MGS-15)` is **not** an innocent bookkeeping estimate. If pursued as the
main forcing mechanism, it risks re-entering the old sector-positivity wall:
the falsifier already breaks there.

That means the candid use of `(MGS-5)` is:

```text
1. expose the exact 1/N scale,
2. localize the nontrivial modulus burden to GROWTH-QUOTIENT,
3. treat the sector factor only as already-isolated side bookkeeping, not as
   the new main theorem to chase.                        (MGS-18)
```

## 6. Status

```text
proved:
  the modulus quotient has the exact growth/sector split (MGS-5);

proved:
  the split reconstructs to roundoff on the certified zeta ladder;

observed:
  the explicit 1/N factor explains the scale of the modulus quotient, while
  the growth quotient itself stays O(1) on the audited ladder;

autopsied:
  the sector factor is the old build-separating sector share, so it should
  not be promoted to the new main forcing mechanism;

reduced:
  MODULUS-QUOTIENT to GROWTH-QUOTIENT-CONTROL plus sector bookkeeping;

next:
  attack GROWTH-QUOTIENT-CONTROL directly, and only import sector data as
  subordinate bookkeeping after that burden is localized.
```
