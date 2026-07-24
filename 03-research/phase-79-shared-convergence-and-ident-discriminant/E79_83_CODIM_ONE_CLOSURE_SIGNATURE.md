# E79.83 - Small `c` is a robust codimension-one signature, but not a monotone convergence law

**Scope:** `DISCRIMINANT`, first direct progress on E79.5 with two off-line
falsifiers instead of one.  
**Class:** REDUCCION GENUINA + falsifier audit.  
**What we know after this document that we did not know before:** the closure
defect

```text
c_N := 1 - sum_j x_j                                                    (83-1)
```

is a robust zeta-only smallness regime on the audited ladder, and that regime
travels together with spectral-cloud coherence across two different planted
off-line controls. But `c_N` does **not** behave like a monotone or geometric
convergence law, so the honest E79.5 object is "codimension-one near-closure"
rather than "nice convergence of c_N".

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 / IDENT side only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform gap assumption.
K1-K5: respected. Uses only the finite CCM transfer data and the E78.154
       counting-function profile.
E72.16/E77.7az: respected. This is an IDENT-side discriminant audit, where
  build separation is admissible, and it does not smuggle zero location into
  a convergence claim.
Circularity: respected. `c_N` and `M_N` come from `(D,x,q)` / `K_N`, not from
  the target arithmetic derivative.
```

## 1. Why this is the right next audit

Phase 78 already isolated three point-6 fingerprints:

```text
small |c_N| for zeta vs O(1) for the plant,
single-signed M_N * x for zeta vs sign-mixed for the plant,
BOUND=TRUE tight vs loose.                                               (83-2)
```

But only one planted control had actually been checked in a phase-79-shaped
ledger, and the language "c_N -> 0" was drifting toward a stronger claim than
the evidence supports. E78.155 already warned that

```text
c_N is small and sign-oscillating, not monotone and not geometric.       (83-3)
```

So the honest next step is:

```text
test whether small |c_N| is still a robust zeta-only regime when a second
off-line planted height is added, and compare it directly with cloud
coherence on the same audited ladder.                                    (83-4)
```

## 2. Probe

Companion files:

```text
E79_83_codim_one_closure_probe.py
E79_83_codim_one_closure_results.json
```

The probe runs the `lambda=6`, `N=8..18`, `dps=60` ladder for three builds:

```text
1. zeta,
2. planted off-line at gamma1 = 14.134725..., beta=0.30,
3. planted off-line at gamma2 = 21.022039..., beta=0.30.                (83-5)
```

For each section it records:

```text
sum_x = sum_j x_j,
c_N   = 1 - sum_x,
|c_N|,
-log10 |c_N|.                                                            (83-6)
```

For each step `N -> N+2` it also records the E78.154 coherence fraction

```text
coh_N := Pxpos / total,                                                  (83-7)
```

where `coh_N = 1` means `M_N * x` is single-signed on the whole audited line.

## 3. Result

The separation is robust.

### Zeta

On every audited zeta section,

```text
|c_N| < 1e-5,                                                            (83-8)
```

in fact on the certified ladder it stays on the tiny scale already seen in
phase 78 (about `1e-7` down to around `1e-10` / `1e-11`, depending on the row).

And on every audited zeta step,

```text
coh_N > 0.99,                                                            (83-9)
```

indeed the phase-78 profile already gave exact audited coherence
`coh_N = 1.0` on the tested ladder, and the present extended run preserves the
same regime.

### Planted off-line controls

For **both** off-line planted heights, the small-`c` regime disappears:

```text
|c_N| = O(1) or larger on the audited ladder,                           (83-10)
```

and the cloud coherence also fails as a stable regime:

```text
the planted ladders do not sustain coh_N ~ 1 across the audited path.    (83-11)
```

with the same qualitative sign-mixing pattern already seen in E78.154.

Numerically, the audited summaries are already stark:

```text
zeta:
  max |c_N| ~ 3.93e-7,
  min |c_N| ~ 2.04e-10,
  all 6 sections satisfy |c_N| < 1e-5,
  all 5 steps satisfy coh_N > 0.99;                                   (83-11a)

plant at gamma1 = 14.1347...:
  min |c_N| ~ 2.32,
  max |c_N| ~ 34.69,
  no section satisfies |c_N| < 1e-5,
  coherence stays in the band 0.56..0.74;                             (83-11b)

plant at gamma2 = 21.0220...:
  min |c_N| ~ 1.78,
  max |c_N| ~ 145.99,
  no section satisfies |c_N| < 1e-5,
  coherence is usually far from 1 and bottoms near 0.055,
  with one isolated near-coherent step around 12->14.                  (83-11c)
```

So the zeta-vs-plant split is not an artifact of one planted height.

## 4. What this does and does not prove

This supports a sharpened version of E79.5:

```text
zeta sits on a codimension-one near-closure surface
  1^T A_N^{-1} b_N = sum_x ~ 1,                                          (83-12)
```

while the off-line planted builds do not.

But it does **not** support the stronger claim

```text
c_N -> 0 monotonically,
or c_N -> 0 geometrically,
or c_N alone is already the theorem-grade discriminant.                  (83-13)
```

The sign oscillation of `c_N` survives, and the magnitude is the stable object,
not the raw signed trajectory.

So the honest upgraded reading is:

```text
small |c_N| is a robust necessary signature of the on-line build,
best read as codimension-one near-closure, not as a neat scalar limit law. (83-14)
```

## 5. Reading

This is meaningful progress because it removes a hidden ambiguity in the phase.

Before this note, the language

```text
"c_N -> 0 for zeta"                                                      (83-15)
```

could be misread as a simple scalar convergence claim. After this note, the
correct picture is:

```text
- the discriminant content is in the near-closure regime |c_N| << 1,
- that regime is robust under a second planted falsifier,
- and it travels with cloud coherence at the regime level rather than as a
  pointwise "every step is perfectly incoherent" statement.             (83-16)
```

So `c_N` is now better placed in the chain:

```text
small |c_N|  = codimension-one closure signature,
coh_N ~ 1    = cloud coherence signature,
and the live burden is to connect these two structurally.               (83-17)
```

That is much closer to E79.6 than the old loose "c tends to zero" phrasing.

## 6. Consequence

After E79.83, the honest E79.5 target sharpens to:

```text
prove that the on-line arithmetic build enforces
  |1 - 1^T A_N^{-1} b_N| << 1
in a way off-line planted data cannot,                                  (83-18)
```

and then explain why that near-closure is the operator-side shadow of cloud
coherence / SAFE-GAMMA-IDENT.

So the next admissible move is not another scalar fit for `c_N`, but:

```text
either
  derive small |c_N| from the secular equation / residue package,
or
  build a combined coherence functional using both |c_N| and the sign pattern
  of M_N * x.                                                           (83-19)
```

## 7. Status

```text
proved by probe:
  the small-|c_N| regime is robust for zeta and fails for two distinct
  planted off-line controls;

proved by probe:
  that regime travels with cloud coherence at the ladder level
  (coh_N ~ 1 throughout zeta, while the planted controls do not sustain that
  regime and one of them shows only an isolated near-coherent resonant step);

clarified:
  E79.5 should be read as codimension-one near-closure, not as a monotone or
  geometric convergence law for signed c_N;

reduced:
  the discriminant burden from a vague "c -> 0" slogan to the sharper pair
  (small |c_N|, cloud coherence);

open:
  derive the structural relation between small |c_N| and the coherence of
  the spectral-shift cloud;

next:
  attack that relation directly instead of mining more packet-side variants.
```
