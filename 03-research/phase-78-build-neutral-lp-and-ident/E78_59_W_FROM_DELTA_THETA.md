# E78.59 - The denominator core is exactly the normalized theta update

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.58 showed that the denominator descent has a fixed point at the centered
quadratic core

```text
2 Re(w_N) + |w_N|^2 < 0,                                  (WDT-1)
```

with

```text
w_N := Delta d_N / d_N,
d_N := 1-theta_N.                                         (WDT-2)
```

To make further progress, the core must be connected to something outside the
closed denominator reparameterization loop. The natural candidate is the
existing Phase-77 front for `Delta theta`.

## 2. Exact identity

Because

```text
d_N = 1-theta_N,                                          (WDT-3)
```

we have for one shell step

```text
Delta d_N
 := d_N+2 - d_N
 = (1-theta_N+2) - (1-theta_N)
 = -(theta_N+2 - theta_N)
 = -Delta theta_N.                                        (WDT-4)
```

Therefore

```text
w_N
 = Delta d_N / d_N
 = -Delta theta_N / (1-theta_N).                          (WDT-5)
```

This is exact.

So the full denominator core can be rewritten as

```text
2 Re( -Delta theta_N/(1-theta_N) )
 + |Delta theta_N/(1-theta_N)|^2 < 0.                     (WDT-6)
```

Equivalently, the inward-branch condition from E78.57 becomes

```text
Re( -Delta theta_N/(1-theta_N) ) < 0.                     (WDT-7)
```

Thus the denominator front is no longer a standalone denominator object. It is
exactly the normalized shell update of `theta_N`.

## 3. Why this matters

Phase 77 already localized the live `theta` dynamics:

- E77.5i: `Delta theta = A+B+C`, genuinely ternary.
- E77.5j: `Delta theta` is a coupled boundary/shell move, not a pure shell pair.

So `(WDT-5)` is the first exact bridge from the E78 denominator fixed point back
into that existing `Delta theta` machinery.

This is a genuine reduction in the sense of admissibility:

```text
denominator core
=> normalized Delta-theta shell law.                      (WDT-8)
```

It moves the live burden from “find another denominator coordinate” to “control
the signed normalized cocycle already named in Phase 77”.

## 4. Audit

The identity `(WDT-5)` was checked directly on the certified
`E77_5ac_theta_logderiv_coupling_{zeta,plant}.json` rows.

### Exactness

For both builds:

```text
max reconstruction error < 1e-14.                         (WDT-9)
```

### Zeta

Representative rows:

```text
sigma=1.0, N=10->12:
  w_N = -0.5057771152 + 0.0009740449 i
  -Delta theta_N/(1-theta_N)
      = -0.5057771152 + 0.0009740449 i

sigma=3.0, N=12->14:
  w_N = -0.3819257889 - 0.0046017479 i
  -Delta theta_N/(1-theta_N)
      = -0.3819257889 - 0.0046017479 i.                  (WDT-10)
```

### Planted build

Representative rows:

```text
sigma=1.0, N=10->12:
  w_N = 6.4534770235 + 2.2988076646 i
  -Delta theta_N/(1-theta_N)
      = 6.4534770235 + 2.2988076646 i.                   (WDT-11)
```

So the denominator core is exactly the normalized `Delta theta` update in both
builds, not just approximately.

## 5. Honest reading

This note does **not** yet prove the denominator core from the Phase-77 cocycle.
The ternary cancellation obstruction from E77.5i/E77.5j is still real.

What it does prove is that any further progress on the denominator side must now
pass through that obstruction:

```text
there is no remaining denominator-only mystery.           (WDT-12)
```

The next legitimate theorem-grade target is not another denominator reduction,
but a signed shell law for

```text
-Delta theta_N / (1-theta_N).                             (WDT-13)
```

## 6. Status

```text
proved:
  w_N = -Delta theta_N / (1-theta_N) exactly;

proved:
  the inward-branch and core-sign conditions can be rewritten entirely as
  signed statements about the normalized theta update;

connected:
  the E78 denominator fixed point back to the E77 ternary Delta-theta front;

reduced:
  further denominator progress to a shell law for the normalized cocycle
  -Delta theta_N/(1-theta_N);

next:
  combine E77.5i/E77.5j's exact Delta-theta anatomy with this normalization, or
  autopsy which cocycle term controls the sign of Re(-Delta theta_N/(1-theta_N)).
```
