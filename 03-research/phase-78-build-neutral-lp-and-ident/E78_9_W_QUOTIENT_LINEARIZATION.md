# E78.9 - Exact linearization of W-QUOTIENT-DELTA

**Run:** 2026-07-18.
**Scope:** IDENT, fixed-L finite front.

## 1. Purpose

E78.7 reduced the fixed-L arithmetic front to the invariant quotient-delta

```text
W-QUOTIENT-DELTA:
  Delta [ W'_{L,N}(i sigma)/(1+W_{L,N}(i sigma)) ].
```

E78.8 showed that the denominator `1+W` stays safely away from zero on the
tested ladder.  This note derives the exact increment identity that splits the
quotient-delta into a linear term and a mixed correction, and audits which part
dominates numerically on the zeta/planted builds.

## 2. Exact identity

For one fixed `L`, one safe point `z=i sigma`, and one consecutive step
`N -> N+2`, define

```text
W_N = W_{L,N}(z),          W_M = W_{L,N+2}(z),
W_N' = W'_{L,N}(z),        W_M' = W'_{L,N+2}(z),

Delta W   = W_N - W_M,
Delta W'  = W_N' - W_M'.                                  (WQ-1)
```

Then:

```text
W_N'/(1+W_N) - W_M'/(1+W_M)
= Delta W'/(1+W_N)
 -W_M' Delta W / ((1+W_N)(1+W_M)).                        (WQ-2)
```

### Proof

Write

```text
A=W_N',   B=1+W_N,   C=W_M',   D=1+W_M.
```

Then

```text
A/B - C/D
= (A-C)/B + C(D-B)/(BD).                                  (WQ-3)
```

Using `(WQ-1)` and

```text
D-B = W_M - W_N = -Delta W,
```

gives `(WQ-2)`.  QED.

## 3. Consequence

The exact invariant target splits into:

```text
linear increment:   Delta W'/(1+W_N),
mixed correction:  -W_M' Delta W / ((1+W_N)(1+W_M)).      (WQ-4)
```

So the honest next fixed-L target is no longer the full quotient-delta, but
the pair of shell increments

```text
Delta W, Delta W',
```

measured against a healthy denominator.

## 4. Probe

Companion:

```text
E78_9_w_quotient_delta_probe.py
E78_9_w_quotient_delta_results.json
```

The probe computes the exact decomposition `(WQ-2)` on the safe grid

```text
sigma in {0.55,0.6,0.75,1.0,1.5,2.0,3.0}
```

for `lambda=6`, sections `N=8,10,12,14`, in both the zeta and planted builds.

## 5. Status

## 5. First audit

On the cheapest certified step `N=8 -> 10` at `lambda=6`, safe grid

```text
sigma in {0.55,0.6,0.75,1.0,1.5,2.0,3.0},
```

the decomposition gives:

### Zeta

```text
max |Q_delta|   = 4.58e-2
max |linear|    = 8.19
max |mixed|     = 8.20
reconstruction  = 6.22e-61.
```

### Planted build

```text
max |Q_delta|   = 5.32e-1
max |linear|    = 4.05e-1
max |mixed|     = 7.23e-1
reconstruction  = 1.17e-61.
```

So the exact identity is numerically certified, and the two builds have
different anatomy:

```text
zeta:   the quotient-delta is small because two O(1e1) terms cancel very
        strongly;

plant:  no such strong cancellation; the quotient-delta remains the same order
        as its linear/mixed pieces.
```

## 6. Reading

This rules out one tempting simplification:

```text
W-QUOTIENT-DELTA is not controlled by Delta W' alone.
```

Nor is it honestly reduced to the mixed term alone.  In the zeta build the live
mechanism is the **signed cancellation between the linear and mixed pieces**.

That is exactly compatible with the rest of the ledger:

```text
- hard absolute estimates were already known to be too weak;
- the invariant LOGT quantity is a signed object;
- the planted falsifier fails the signed cancellation anatomy.
```

So the smallest honest next object is:

```text
LINEAR-MIXED-CANCELLATION:
prove a summable envelope for

  Delta W'/(1+W_N)
 -W_{N+2}' Delta W / ((1+W_N)(1+W_{N+2}))

as a signed shell identity, not by bounding the two pieces separately.
```

## 7. Status

```text
proved:
  exact quotient-delta linearization into linear plus mixed terms;

observed:
  on zeta, the quotient-delta is much smaller than either component, so the
  mechanism is strong signed cancellation;

observed:
  on the planted build, the cancellation anatomy is absent or much weaker;

refuted:
  reduction of W-QUOTIENT-DELTA to Delta W' alone;

reduced:
  W-QUOTIENT-DELTA to the signed two-term shell object
  LINEAR-MIXED-CANCELLATION;

next:
  search the two-generator/shell algebra for an exact identity producing that
  cancellation before any absolute estimate.
```
