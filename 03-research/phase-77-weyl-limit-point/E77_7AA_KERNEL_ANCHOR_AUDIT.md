# E77.7aa - Kernel-anchor coupling audit

**Run:** 2026-07-18.

## 1. Purpose

E77.7z reduced the fixed finite-section singular problem to the scalar
coupling

```text
A(z0) = - <u0,kappa> tau(z0) u0,
```

where `u0` spans the kernel direction of the rank-one Schur block when
`Sigma` is singular.

If `A(z0) != 0`, the projective intrinsic profile has an automatic finite
`eta -> 0` limit in the singular branch:

```text
Pi_eta(z) -> A(z) / A(z0).
```

This note audits that coupling on the finite sections.

## 2. Probe

Companion:

```text
E77_7aa_kernel_anchor_probe.py
E77_7aa_kernel_anchor_results.json
```

Command:

```bash
python3 E77_7aa_kernel_anchor_probe.py \
  --lambda 6 --max-modes 18 --dps 80
```

For each finite section, the probe computes at the safe anchor `sigma0=1`:

```text
1. the smallest Schur eigenvalue |lambda0(Sigma)|;
2. the kernel/source overlap |<u0,kappa>|;
3. the anchor-row coupling |tau(z0)u0|;
4. the product |A(z0)| = |<u0,kappa> tau(z0)u0|.
```

The same largest-section frozen surrogate `mu_ref` is used as in E77.7y.

## 3. Result

### Zeta

The Schur block is numerically rank one throughout the tested ladder:

```text
min |lambda0(Sigma)| = 1.53e-21.
```

But the kernel-anchor coupling never comes close to vanishing:

```text
min |<u0,kappa>|   = 1.60e-19,
min |tau(z0)u0|    = 2.46e2,
min |A(z0)|        = 9.94e-12.
```

Representative rows:

```text
N=10: |lambda0| = 9.33e-18, |A(z0)| = 1.06e-10
N=14: |lambda0| = 8.44e-20, |A(z0)| = 1.24e-8
N=17: |lambda0| = 1.53e-21, |A(z0)| = 5.19e-8
N=18: |lambda0| = 1.06e-20, |A(z0)| = 2.38e-6.
```

So in the zeta singular regime, the anchor sees the kernel part with a clear
nonzero margin on every tested section.

### Planted build

The planted Schur block does not enter the same near-singular regime on this
ladder:

```text
min |lambda0(Sigma)| = 5.19e-2.
```

Still, the same coupling is comfortably nonzero:

```text
min |<u0,kappa>|   = 3.67e-2,
min |tau(z0)u0|    = 3.49e-2,
min |A(z0)|        = 1.28e-3.
```

This is the expected falsifier-neutral behavior: the interface coupling does
not distinguish the arithmetic build from the planted one.

## 4. Reading

Combined with E77.7z, the audit supports the singular finite-section picture:

```text
1. the only potentially dangerous branch is rank-one Schur singularity;
2. in that branch, the anchor actually couples to the kernel direction;
3. therefore the projective pole cancellation mechanism is active.
```

This explains the strong `eta`-stability observed in E77.7y.  The stability is
not mysterious numerical luck; it is exactly what the rank-one formula
predicts once `A(z0)` stays nonzero.

## 5. What is and is not proved

Supported:

```text
FIXED-SECTION-KERNEL-ANCHOR, numerically:
on all tested finite sections, the anchor sees the singular Schur kernel.
```

Not yet proved theorem-grade:

```text
1. a symbolic/non-numerical proof that A(z0) cannot vanish in the singular
   Schur branch;
2. local-uniform eta-limit on safe compacta for the abstract fixed section;
3. transport from the finite surrogate mu_ref to the true mu_L bridge.
```

So this is still an audit, not the final theorem, but it shrinks the live
object again.

## 6. Smaller live object

After E77.7aa, the singular LP-interface target can be sharpened to:

```text
FIXED-SECTION-KERNEL-ANCHOR-THEOREM:
if the intrinsic Schur block Sigma is singular at a fixed finite section,
then A(z0) = -<u0,kappa> tau(z0)u0 is nonzero.
```

Then E77.7z yields:

```text
FIXED-SECTION-KERNEL-ANCHOR-THEOREM
=> INTRINSIC-SCHUR-ETA-LIMIT at fixed section
=> singular-section clause for PROJECTIVE-MU-TRANSFER.
```

This implication is explicit and admissible under the E77.6 reduction rule.

## 7. Status

```text
observed:  in zeta, Sigma is numerically rank one while A(z0) stays clearly
           nonzero on every tested section;
observed:  plant shows the same neutral coupling behavior;
refined:   the live singular object is now the theorem-grade nonvanishing of
           A(z0), not the whole eta-regularized profile;
next:      prove FIXED-SECTION-KERNEL-ANCHOR-THEOREM from the exact Schur
           formulas, or autopsy that target if a symbolic obstruction appears.
```
