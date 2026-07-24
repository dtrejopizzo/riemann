# E78.2 - PROJECTIVE-MU-TRANSFER is mu_L-location driven, not build-neutral
# (autopsy of item 2, and unification with item 4)

**Run:** 2026-07-18.
**Target:** interface subclause (c) / Fable-5 item 2 -- `PROJECTIVE-MU-TRANSFER`:
for each safe compact `K`, `sup_{z in K}|Pi_N(z;mu_L) - Pi_N(z;0)| -> 0`, where
`Pi_N(z;mu)=T_N(z;mu)/T_N(z0;mu)` and `T_N(z;mu)=r_z A_N(mu)^{-1} b_N` (E77.7n).
**Verdict:** the statement is **false for the plant** (defect plateaus at `~0.84`)
and only **slowly / ambiguously** approached for zeta. Its size is governed by
`|mu_L - 0|`, the same build-discriminating quantity that governs the item-4
ground gap (E78.1). So item 2 is a detector, not a build-neutral forcing step.

## 1. What the earlier audit left open

E77.7n reduced the pencil mismatch to `PROJECTIVE-MU-TRANSFER` and, using a
*frozen surrogate* `mu` at the largest section, observed that projective
normalization made the moving/frozen defect small (`~1e-4` zeta). But that probe
compared two approximations of `mu_L` against each other; it never tested the
actual target -- the `mu_L` family against the Phase-76 `mu = 0` family. The
exact identity (E77.7m M-6):

```text
Pi_N(z;mu_L) - Pi_N(z;0)  is driven by  (mu_L - 0) * r_z A_N(mu_L)^{-1} A_N(0)^{-1} b_N.
```

The size of the defect therefore carries an explicit factor `mu_L`.

## 2. Probe of the genuine target

`E78_2_projective_transfer_probe.py` (P76.002 `build_mp` + P76.018 `transfer`,
`lambda=6`, `dps=55`) sets `mu` to the section inner-block bottom eigenvalue (an
honest `mu_L` proxy) and reports
`maxProjDefect = sup_sigma|Pi_N(i sigma;mu_L) - Pi_N(i sigma;0)|`,
`sigma in {0.6,1,2,3}`, anchor `sigma_0=1`:

```text
ZETA                                   PLANT
 N   mu_bottom     defect               N   mu_bottom    defect
 6   7.43e-21    0.0337178              6  -0.0381883   0.703644
 8   1.14e-25    0.0269685              8  -0.411329    0.960552
10   1.85e-30    0.0212735             10  -1.49705     0.873715
12   4.30e-35    0.0178288             12  -1.69984     0.846783
14   2.26e-39    0.0149035             14  -1.72344     0.843461
16   1.57e-43    0.0129144             16  -1.73553     0.841695
```

```text
- PLANT: mu_bottom -> ~ -1.74 (order one), and the defect PLATEAUS at ~0.84.
         PROJECTIVE-MU-TRANSFER is FALSE for the plant: the mu_L family and the
         mu=0 family stay O(1) apart projectively.
- ZETA:  mu_bottom -> 0, and the defect decreases 0.0337 -> 0.0129, but the
         per-step ratio creeps 0.80 -> 0.87 toward 1 (decelerating). This is
         consistent with -> 0 but does NOT establish it; a small nonzero limit
         is not excluded by the data.
```

## 3. Reading: the defect is mu_L-location driven

By the M-6 factor `(mu_L - 0)`:

```text
zeta:  mu_L ~ 0        => A_N(mu_L) ~ A_N(0), the two families nearly coincide,
                          the defect is small and slowly shrinking -- a shadow of
                          mu_L ~ 0, not a genuine projective compatibility.
plant: mu_L ~ -1.74    => A_N(mu_L) and A_N(0) are genuinely different operators;
                          the (mu_L-0) prefactor is order one and the defect
                          stays O(1).
```

So the "smallness" of `PROJECTIVE-MU-TRANSFER` for zeta is not a build-neutral
analytic fact about the pencil; it is the **same** build-discriminating datum as
item 4 -- the location of `mu_L` (`~0` for zeta, order-one negative for the
plant). Item 4 saw it as a vanishing spectral gap; item 2 sees it as a vanishing
`(mu_L - 0)` prefactor. They are one quantity.

## 4. Gate verdict and unification

```text
1. PROJECTIVE-MU-TRANSFER is NOT build-neutral. Its defect is order-one
   build-discriminating (0.84 plant vs ->small zeta). By the E77.7az / E72.16
   gate it is a DETECTOR carrying surplus zero-location content, not an
   admissible forcing mechanism. Item 2 does not close as a build-neutral step.

2. UNIFICATION. Interface subclauses (c)=item 2 and (e)=item 4 both reduce to
   the location/gap of mu_L:  ~0 for zeta, O(1) negative for the plant. The
   Phase-78 README's classification of front A2 ("SAFE-DISK-IDENT ... build-
   neutral by nature") is INCORRECT: any interface quantity evaluated AT mu_L
   inherits the mu_L-location discriminant and is therefore a detector. Only
   interface quantities that avoid pinning to mu_L (e.g. the mu-free separation
   of Cauchy rows, E77.7aj subclause a) are genuinely build-neutral.
```

This is the same lesson as the Phase-77 shell-mismatch cascade (E77.7az), now at
the pencil/interface level: a quantity that separates the builds by order one is
a detector, and here the separation is inherited from `mu_L` itself.

## 5. Consequence for the interface program

```text
- Subclauses (c) and (e) cannot be the build-neutral LP-forcing steps the
  SAFE-DISK-IDENT decomposition assumed. They are detectors.
- The only build-neutral LP-interface content is the mu-free part: separation of
  safe Cauchy rows (E77.7aj, PROVED) and the gauge-free NEUTRAL-GROUND-CAUCHY
  named in E78.1 section 7.
- The mu_L-location discriminant (gap ~0 for zeta vs O(1) for plant; equivalently
  defect ->small vs 0.84) belongs, by the Falsifier Location Rule, to IDENT --
  where E77.6 already measures the plant break. It must NOT be re-imported into
  LP through an interface subclause evaluated at mu_L.
```

## 6. Flag for Fable-5 (consistent with E78.1 section 6)

The plant defect plateau at `0.84` and the plant order-one ground gap (E78.1)
are the same phenomenon: at the plant's own `mu_L ~ -1.74` the finite resolvent
`A_N(mu_L)^{-1}` stays bounded, so no projective collapse and no canonical-energy
divergence occur there. This is Outcome-B-flavored and is recorded as data for
review; the settled E77.7az gate is not reopened here.

## 7. Probes

```text
E78_2_projective_transfer_probe.py
E78_2_projective_transfer_results.json
```

All cited numbers were read from executed probe output; none is projected.

## 8. Status

```text
observed:  genuine item-2 defect |Pi_N(mu_L)-Pi_N(0)| plateaus at ~0.84 for the
           plant (statement FALSE for plant) and only slowly/ambiguously
           decreases for zeta (ratio creeping to 1);
proved:    the defect carries the exact M-6 prefactor (mu_L - 0), so its size is
           mu_L-location driven;
refuted:   PROJECTIVE-MU-TRANSFER as a BUILD-NEUTRAL forcing step -- it is
           order-one build-discriminating, hence a detector under E77.7az/E72.16;
unified:   items 2 and 4 both reduce to the mu_L-location/gap discriminant
           (~0 zeta, O(1) plant); the 'front A2 build-neutral' label is wrong for
           any subclause evaluated at mu_L;
flagged:   plant bounded resolvent at its own mu_L (Outcome-B-flavored); data for
           Fable-5, gate not reopened;
open:      whether the mu-free remnant (E77.7aj + NEUTRAL-GROUND-CAUCHY) suffices
           for the LP interface without any mu_L-pinned subclause.
```
