# E78.22 - Theta dominance as the structural source of sign coherence

**Run:** 2026-07-18.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.21 reduced the denominator side to

```text
SIGN-COHERENT-BALANCE:
  sign coherence of (Q_ext,Q_logT)
  + ratio-to-one control for |Q_logT|/|Q_ext|.            (TD-1)
```

Since `Q_ext` is positive on the audited rows, the first clause is equivalent
there to

```text
Q_logT > 0.                                               (TD-2)
```

This note identifies the smallest honest structural explanation available in
the current exact split

```text
Q_logT = Q_t0 + Q_theta.                                  (TD-3)
```

## 2. Exact sign forcing by theta dominance

If

```text
Q_theta > 0,
|Q_theta| > |Q_t0|,                                       (TD-4)
```

then `(TD-3)` forces

```text
Q_logT > 0.                                               (TD-5)
```

More generally, if

```text
sign(Q_theta) is fixed
and |Q_theta| > |Q_t0|,                                   (TD-6)
```

then `Q_logT` must have the same sign as `Q_theta`.

So the sign-coherence part of E78.21 reduces to the exact Schur-side target

```text
THETA-DOMINANCE:
  prove that the signed theta block dominates the transfer block:

    sign(Q_theta) fixed,
    |Q_theta| > |Q_t0|                                    (TD-7)

on the zeta cofinal path.
```

## 3. Probe audit

Companion:

```text
E78_22_theta_dominance_probe.py
E78_22_theta_dominance_results.json
```

### Zeta

On the audited zeta rows:

```text
dominance count      = 12
nondominance count   = 0
same-sign count      = 12
opposite-sign count  = 0.
```

The audited dominance ratios are large:

```text
5.324 <= |Q_theta|/|Q_t0| <= 9.252.                       (TD-8)
```

And the signs are completely rigid:

```text
Q_t0   < 0,
Q_theta > 0,
Q_logT > 0                                               (TD-9)
```

throughout the current `sigma in {1,3}` ladder.

### Planted build

On the planted rows:

```text
dominance count      = 6
nondominance count   = 6
same-sign count      = 8
opposite-sign count  = 4.                                 (TD-10)
```

The failures line up exactly with loss of dominance. Representative bad rows:

```text
sigma=1.0, N=12:
  Q_t0    = -7.7247
  Q_theta = +5.0642
  Q_logT  = -2.6605
  |Q_theta|/|Q_t0| = 0.656

sigma=3.0, N=14:
  Q_t0    = +6.9774
  Q_theta = -0.5686
  Q_logT  = +6.4088
  |Q_theta|/|Q_t0| = 0.0815.                              (TD-11)
```

So the plant loses sign coherence exactly by failing theta dominance.

## 4. Consequence

E78.21's sign clause now has a concrete Schur-side source:

```text
THETA-DOMINANCE
=> sign coherence of (Q_ext,Q_logT),                      (TD-12)
```

because `Q_ext` stays positive on the audited ladder and `Q_logT` is then
forced to stay positive as well.

Hence the live denominator target sharpens to

```text
THETA-DOMINANCE
+ ratio-to-one control for |Q_logT|/|Q_ext|
=> SIGN-COHERENT-BALANCE
=> LOGT-CANCEL-COFINAL.                                   (TD-13)
```

## 5. Honest reading

This is not yet a proof of sign coherence on the cofinal path.  But it is a
real reduction: the open sign question no longer sits at the level of the full
defect `Q_ext-Q_logT`; it sits inside the exact Schur split and asks for one
thing:

```text
does the theta block keep dominating the transfer block?
```

That is the right scale for the current program. It stays entirely inside the
finite cell/Schur algebra and it explains both audited behaviors:

```text
zeta:  theta dominates and sign coherence holds;
plant: theta dominance fails exactly where sign coherence fails.
```

## 6. Status

```text
proved:
  sign coherence of Q_logT is forced by the exact Schur-side condition
  |Q_theta| > |Q_t0| with fixed sign(Q_theta);

observed:
  all audited zeta rows satisfy strong theta dominance
  (ratio 5.3 to 9.25) and hence coherent positive Q_logT;

observed:
  the planted build loses sign coherence exactly where theta dominance fails;

reduced:
  the sign part of SIGN-COHERENT-BALANCE to THETA-DOMINANCE;

next:
  derive theta dominance from the exact u-sector/Schur identities, not from
  the audited tables alone.
```
