# E79.87 - The exceptional planted row is a cloud-only resonance, not a codimension-one closure event

**Scope:** `DISCRIMINANT`, autopsy of the exceptional planted row left open by
E79.86.  
**Class:** AUTOPSIA FRANCA + structural correction.  
**What we know after this document that we did not know before:** the unique
near-coherent planted step from E79.83/E79.86 does not contradict the zeta-side
chain. It realizes a different mechanism:

```text
internal cloud near-symmetry without codimension-one closure,
without residual balance,
and without a sharply separated zeta-style outlier.                      (87-1)
```

So the normalized cloud-defect quotient

```text
D_N = (mean pair defect)/(outlier_fraction)                             (87-2)
```

is a strong one-sided zeta signature, but not the full theorem-grade
discriminant by itself.

## 0. Why this autopsy is required

E79.86 compressed the geometric bridge to one finite proxy:

```text
D_N ~ 10^-3  =>  coherence defect collapses on the audited ladder.      (87-3)
```

But one planted row stayed uncomfortable:

```text
plant gamma2, section N=12 / step 12->14,
delta_coh ~ 2.28e-4 while D_N ~ 1.36e-2.                               (87-4)
```

If that row shared the zeta mechanism, then `D_N` would be too weakly stated.
If it came from a different finite mechanism, then the chain needed one candid
branch correction instead of a false equivalence claim.

## 1. The exceptional row in one table

The relevant audited values are:

```text
zeta, N=12:
  |c| ~ 1.29e-7,
  R_net ~ 1.46e-16,
  R_pm  ~ 1.0,
  outlier_fraction ~ 11.83,
  mean_pair_defect ~ 1.41e-2,
  D_N ~ 1.19e-3.                                                       (87-5)

plant gamma1, N=12:
  |c| ~ 1.18e1,
  R_net ~ 2.11e-1,
  R_pm  ~ 6.51e-1,
  outlier_fraction ~ 1.16,
  mean_pair_defect ~ 1.19e-2,
  D_N ~ 1.02e-2.                                                       (87-6)

plant gamma2, N=12:
  |c| ~ 1.46e2,
  R_net ~ 1.0,
  R_pm  ~ 0.0,
  outlier_fraction ~ 1.16,
  mean_pair_defect ~ 1.58e-2,
  D_N ~ 1.36e-2.                                                       (87-7)
```

The exceptional planted row is therefore not "almost zeta with slightly worse
constants". It differs from zeta in **all** non-geometric discriminant
coordinates:

```text
- no small c,
- no positive/negative residue balance,
- no sharply isolated outlier.                                          (87-8)
```

## 2. What is actually happening in the exceptional planted row

A direct sectionwise inspection of `plant gamma2, N=12` gives:

```text
c = -145.99...                                                          (87-9)
sum_{r_j>0} |r_j| = 0,
sum_{r_j<0} |r_j| ~ 2969.81,                                            (87-10)
```

so the secular residue package is literally one-signed there:

```text
R_net = 1,   R_pm = 0.                                                  (87-11)
```

This is the opposite of the zeta-side balanced package from E79.84.

At the same time, the **outlier-removed cloud** is genuinely close to symmetric
in its deeper pairs:

```text
first pair defect  ~ 1.10e-1,
middle/late defects drop to 1e-3 and below,
last three defects ~ 1.5e-4, 2.5e-4, 1.4e-4.                           (87-12)
```

And the outlier itself is not really detached:

```text
outlier_fraction ~ 1.157,                                               (87-13)
```

so this row has:

```text
very good internal pair symmetry,
but only after abandoning both zeta hallmarks
  (small |c| and strongly isolated outlier).                            (87-14)
```

That is why the coherence defect can become tiny while `D_N` stays on the
planted scale `10^-2`: the row is a **cloud-only resonance**.

## 3. Structural correction to the E79.83-E79.86 chain

The candid chain is now:

```text
zeta route:
  small |c_N|
    -> residual balance
    -> sharply separated outlier + low-defect symmetric remainder
    -> coherence.                                                       (87-15)

exceptional planted resonance:
  no small |c_N|,
  no residual balance,
  no sharp outlier separation,
  but temporary internal cloud near-symmetry
    -> near-coherence only.                                             (87-16)
```

So `D_N` is measuring the **zeta route**, not the entire set of ways a finite
row can look coherent.

This resolves the apparent tension in E79.86:

```text
tiny D_N is a strong sufficient signal for the zeta-side coherence regime,
but near-coherence can also appear through a cloud-only resonance.       (87-17)
```

## 4. Consequence for the live discriminant burden

After this autopsy, the next candid target is not

```text
"upgrade D_N into an iff criterion".                                    (87-18)
```

That would be chasing the wrong object.

The right target is instead:

```text
prove that the theorem-grade discriminant needs the conjunction

  small |c_N|
  + residual balance
  + cloud symmetry regime,

while cloud symmetry alone can only create isolated resonant near-coherence.    (87-19)
```

In other words, the planted exception should be archived as a **falsifier of the
too-strong claim**

```text
coherence <=> tiny D_N                                                  (87-20)
```

and not as a falsifier of the zeta-side bridge.

## 5. Status

```text
proved by direct audit:
  the exceptional planted row is not a hidden zeta-like event;
  it is a cloud-only resonance with one-signed residues, huge |c|,
  weak outlier separation, and very good internal pair symmetry;

clarified:
  D_N tracks the zeta mechanism but not every possible source of finite-row
  near-coherence;

corrected:
  the live discriminant object is the conjunction
    (small |c_N|, residual balance, cloud symmetry regime),
  not cloud symmetry alone and not D_N alone;

next:
  sharpen the bridge so that cloud-only resonances are explicitly excluded,
  rather than trying to force an iff statement from E79.86.
```
