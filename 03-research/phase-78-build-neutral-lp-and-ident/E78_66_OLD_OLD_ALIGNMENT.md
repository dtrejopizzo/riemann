# E78.66 - The cocycle aligns with the `old-old` shell chain, and there the transfer-ratio polarization is exact

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.65 autopsied a naive shortcut:

```text
use the `old -> new` rows from E77.5ac to rewrite PAIRNUM_N directly through
q_N := 1-theta_N.
```

That failed on the certified artifacts.

This note identifies the missing convention. The E77.5i cocycle is **not**
aligned with the `old -> new` chain in E77.5ac. It is aligned with the
`old -> old` chain:

```text
theta_old(N) - theta_old(N+2).                           (OOA-1)
```

Once that alignment is used, the transfer-ratio polarization of `PAIRNUM_N`
becomes exact.

## 2. Exact alignment statement

Let

```text
Delta theta_cocycle,N := A_N + B_N + C_N                 (OOA-2)
```

from E77.5i, and let `theta_old(N)` denote the `tag="old"` shell row stored in
E77.5ac/E77.5g at section size `N`.

Then on the common certified ladder,

```text
Delta theta_cocycle,N
 = theta_old(N) - theta_old(N+2)                         (OOA-3)
```

to roundoff.

So the cocycle is aligned with the **old-old shell chain**, not with the mixed
`old-new` chain that caused the E78.65 failure.

## 3. Consequence for `PAIRNUM_N`

Write

```text
q_old(N) := 1-theta_old(N).                              (OOA-4)
```

Then E78.63 gives

```text
PAIRNUM_N
 = -Re(Delta theta_cocycle,N conj(q_old(N))).            (OOA-5)
```

Using `(OOA-3)` and `Delta theta_cocycle,N = -(q_old(N)-q_old(N+2))`, we obtain

```text
PAIRNUM_N
 = Re((q_old(N)-q_old(N+2)) conj(q_old(N))).             (OOA-6)
```

and therefore the exact polarization identity

```text
PAIRNUM_N
 = ( |q_old(N)|^2 - |q_old(N+2)|^2
     + |q_old(N)-q_old(N+2)|^2 ) / 2.                    (OOA-7)
```

So the transfer-ratio bridge from E78.65 was conceptually right but used the
wrong chain. The correct bridge is the `old-old` chain.

## 4. Probe audit

Companion:

```text
E78_66_old_old_alignment_probe.py
E78_66_old_old_alignment_results.json
```

On the common certified ladder (`sigma in {1.0,3.0}`, `N=8,10,...,20`):

```text
zeta:
  max theta alignment error   <= 1.60e-16
  max pairnum alignment error <= 7.79e-14

plant:
  max theta alignment error   <= 1.11e-15
  max pairnum alignment error <= 1.71e-13.               (OOA-8)
```

Representative zeta row (`sigma=1.0, N=10`):

```text
Delta theta_cocycle = 5.331457752402686e-2
                     +1.925190732943468e-4 i

theta_old(10)-theta_old(12)
                   = 5.331457752402686e-2
                    +1.925190732943468e-4 i

PAIRNUM_10         = 1.464427009841529e-2
polarized old-old  = 1.464427009833739e-2.               (OOA-9)
```

So the alignment and the corrected polarization both hold to roundoff.

## 5. Consequence

This is a genuine reduction.

It repairs the failed shortcut from E78.65 and reanchors the live shell
numerator in the invariant transfer language:

```text
PAIRNUM-SIGN
<=>
old-old transfer-ratio contraction for q_old(N)=T_N/t0_N. (OOA-10)
```

The active burden is now to derive `(OOA-7)` directly from the
moving-boundary/LOGT-CELL transfer identity, without re-expanding into Schur
pieces.

## 6. Honest reading

This note does not prove the sign of `PAIRNUM_N`. The ternary cancellation
burden is still real.

What it does prove is that the correct transfer-ratio endpoint exists and is
already encoded in the certified artifacts, once the right shell chain is used.

So the next admissible step is no longer vague `TRANSFER-RATIO-ALIGNMENT`. It is
the sharper target:

```text
OLD-OLD-TRANSFER-CONTRACTION:
  derive the sign/contraction law for q_old(N)=T_N/t0_N along the old-old shell
  chain from the invariant moving-boundary LOGT-CELL update.  (OOA-11)
```

## 7. Status

```text
proved:
  the E77.5i cocycle aligns with theta_old(N)-theta_old(N+2), not with the
  mixed old-new chain;

proved:
  on that old-old chain, PAIRNUM_N is exactly the quadratic polarization of
  q_old(N)=1-theta_old(N)=T_N/t0_N;

reduced:
  PAIRNUM-SIGN to OLD-OLD-TRANSFER-CONTRACTION;

next:
  derive the old-old transfer-ratio contraction law from E77.5l's invariant
  LOGT-CELL update.
```
