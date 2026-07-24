# E78.91 - The shell growth of `u` is exactly a numerator-vs-denominator radial gap

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.88 reduced the modulus quotient to the `u`-growth object

```text
GROWTH-QUOTIENT_N(sigma)
 := N * (-SAFEDELTA_N(i sigma))
    / [2 (|u_N+2|-|u_N|)].                              (URG-1)
```

The live burden was then the shell growth of `|u|` itself.

This note identifies the exact finite source of that growth. It is not a new
opaque scalar: it is the radial gap between the numerator and denominator shell
quotients of

```text
u_N = -theta'_N / (1-theta_N).                          (URG-2)
```

## 2. Exact quotient law

Define the raw shell quotients

```text
q_a,N := theta'_N+2 / theta'_N,                         (URG-3)
q_b,N := (1-theta_N+2) / (1-theta_N).                   (URG-4)
```

Then by `(URG-2)`,

```text
u_N+2 / u_N = q_a,N / q_b,N.                            (URG-5)
```

Taking moduli gives the exact radial law

```text
|u_N+2| / |u_N|
 = |q_a,N| / |q_b,N|.                                   (URG-6)
```

Therefore

```text
|u_N+2| - |u_N|
 = |u_N| ( |q_a,N|/|q_b,N| - 1 )
 = |u_N| ( |q_a,N| - |q_b,N| ) / |q_b,N|.              (URG-7)
```

So the sign of the shell growth is controlled exactly by the single real gap

```text
U-RADIAL-GAP_N
 := |q_a,N| - |q_b,N|.                                  (URG-8)
```

This is the smallest current exact source of the modulus growth.

## 3. Consequence for the growth quotient

Substituting `(URG-7)` into E78.88 gives

```text
GROWTH-QUOTIENT_N(sigma)
 = N * (-SAFEDELTA_N(i sigma)) * |q_b,N|
   / [2 |u_N| (|q_a,N|-|q_b,N|)].                       (URG-9)
```

So the growth side no longer depends on an unnamed shell modulus difference.
It depends explicitly on:

```text
1. the safe derivative numerator,
2. the old shell size |u_N|,
3. the denominator radial ratio |q_b,N|,
4. the radial gap |q_a,N|-|q_b,N|.                      (URG-10)
```

That is a genuine reduction because the sign and size of the shell growth are
now localized to one explicit numerator-vs-denominator radial competition.

## 4. Probe audit

Companion:

```text
E78_91_u_radial_gap_probe.py
E78_91_u_radial_gap_results.json
```

### Exactness

The radial law `(URG-6)` reconstructs to roundoff for both builds:

```text
max reconstruction error < 1e-15.                       (URG-11)
```

### Zeta

Across the certified zeta ladder:

```text
|q_a,N|     in [0.279289, 1.615691],
|q_b,N|     in [0.126754, 0.733019],
U-RADIAL-GAP_N
            in [0.152534, 0.921090],
|u_N+2|/|u_N|
            in [2.203389, 2.693753].                   (URG-12)
```

Representative endpoint rows:

```text
sigma=1.0, N= 8:
  |q_a| = 1.615691
  |q_b| = 0.694602
  gap   = 0.921090
  |u_new|/|u_old| = 2.326069

sigma=1.0, N=20:
  |q_a| = 0.279289
  |q_b| = 0.126754
  gap   = 0.152534
  |u_new|/|u_old| = 2.203389.                          (URG-13)
```

So on zeta the growth of `|u|` comes from a coherent strict inequality

```text
|q_a,N| > |q_b,N|.                                      (URG-14)
```

The denominator contracts more strongly than the numerator on every audited
row, and that exact radial gap drives the `u` growth.

### Planted build

The planted build does not preserve a coherent radial-gap regime:

```text
U-RADIAL-GAP_N
  min = -0.908427,
  max = 82.178964.                                      (URG-15)
```

In particular, the gap can even turn negative:

```text
sigma=1.0, N=12:
  |q_a| = 3.743380,
  |q_b| = 4.651807,
  gap   = -0.908427,
  |u_new|/|u_old| = 0.804715.                           (URG-16)
```

So the falsifier already breaks at the exact source of the growth law.

## 5. Honest reading

This note does **not** prove a cofinal lower bound for `U-RADIAL-GAP_N`.

What it proves is that the modulus-growth front has been reduced to the
explicit radial competition

```text
|q_a,N| - |q_b,N|.                                      (URG-17)
```

That is strictly smaller and more intrinsic than the raw shell difference
`|u_N+2|-|u_N|`.

## 6. Status

```text
proved:
  |u_N+2|/|u_N| = |q_a,N|/|q_b,N| exactly;

proved:
  therefore |u_N+2|-|u_N| is controlled exactly by the radial gap
  |q_a,N|-|q_b,N|;

observed:
  on the audited zeta ladder the radial gap stays strictly positive, so the
  denominator contracts more strongly than the numerator on every tested row;

observed:
  the planted build does not preserve a coherent radial-gap regime and can
  already make the gap negative;

reduced:
  the modulus-growth front to U-RADIAL-GAP plus the already isolated safe
  derivative numerator;

next:
  decide whether the endpoint weighted modulus quotient is better attacked
  through a direct law for U-RADIAL-GAP_N or through a sharper split of the
  safe derivative numerator against that gap.
```
