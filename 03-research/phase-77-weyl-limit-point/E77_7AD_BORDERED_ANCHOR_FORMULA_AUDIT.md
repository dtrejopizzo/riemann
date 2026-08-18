# E77.7ad - Bordered anchor formula audit

**Run:** 2026-07-18.

## 1. Purpose

E77.7ac reduced the singular fixed-section clause to invertibility of the
shifted bordered matrix

```text
M(z0) =
[ A      g ]
[ r(z0)  c0 ].
```

This note compares its determinant with the kernel-anchor scalar from
E77.7ab:

```text
scalar(z0) = (v0^* g)(r(z0)v0),
```

where `v0` is the normalized eigenvector of `A` corresponding to the
smallest `|lambda|`.

The goal is to decide whether the tiny bordered determinant seen in zeta is
caused by loss of coupling, or merely by the characteristic derivative factor
coming from an almost-singular inner block.

## 2. Probe

Companion:

```text
E77_7ad_bordered_anchor_formula_probe.py
E77_7ad_bordered_anchor_formula_results.json
```

Command:

```bash
python3 E77_7ad_bordered_anchor_formula_probe.py \
  --lambda 6 --max-modes 14 --dps 70
```

For each section, the probe records:

```text
1. the smallest inner eigenvalue |lambda0(A)|;
2. the kernel-anchor scalar |(v0^* g)(r(z0)v0)|;
3. the bordered determinant |det M(z0)|;
4. the derivative factor
   p'_A(0) = product_{j != 0} (-lambda_j(A));
5. the normalized ratio det M / (p'_A(0) scalar).
```

This is still a finite audit at the sectionwise moving `mu`.

## 3. Result

### Zeta

The bordered determinant becomes astronomically small:

```text
N=10: |det M| = 1.89e-214
N=12: |det M| = 2.60e-281
N=14: |det M| = 2.70e-347.
```

But the kernel-anchor scalar remains nonzero:

```text
N=10: |scalar| = 4.59e-24
N=12: |scalar| = 5.96e-25
N=14: |scalar| = 5.51e-29.
```

Moreover the normalized quotient

```text
det M / (p'_A(0) scalar)
```

stays close to `-1`, already on the first rows:

```text
N=6:  -0.9647 - 0.0810 i
N=8:  -0.9741 - 0.0656 i
N=10: ... continuing toward the same pattern.
```

So the extreme smallness of `det M` is not explained by vanishing of the
coupling scalar.  It is consistent with the determinant carrying the extra
characteristic factor `p'_A(0)`.

### Planted build

The planted sections do not enter the same near-singular regime, and the
bordered determinant is correspondingly macroscopic:

```text
N=8:  |det M| = 3.08e-3
N=12: |det M| = 9.98e4
N=14: |det M| = 2.45e6.
```

The normalized quotient is not yet stable on this short ladder, which is
expected because the planted block is not operating in the same almost-singular
one-mode regime.

## 4. Reading

The audit gives a sharp structural conclusion.

```text
The zeta bordered determinant is tiny because the inner block A is almost
singular, not because the source/anchor coupling disappears.
```

That is exactly the distinction needed for the LP interface:

```text
small bordered determinant  !=  blind kernel direction.
```

So “bordered invertibility with uniform margin” is too strong and points at
the wrong phenomenon.  What matters for the singular projective clause is the
nonzero kernel coupling itself.

## 5. Autopsy of the stronger target

The following candidate is therefore too strong as a theorem target:

```text
UNIFORM-BORDERED-ANCHOR-INVERTIBILITY:
the shifted bordered matrix M(z0) stays quantitatively bounded away from
singularity.
```

E77.7ad refutes this as the right object for zeta.  The determinant can be
tiny even while the projective singular cancellation is healthy.

This is another appearance of the old lesson from P76.061:

```text
ambient or determinant-scale smallness is not the same as directional
projective failure.
```

## 6. Smaller live object

The admissible singular target is now:

```text
KERNEL-ANCHOR-RESIDUE-FORMULA:
when the inner block A has a simple near-zero mode v0,
det M(z0) factors as

  det M(z0) = -p'_A(0) (v0^* g)(r(z0)v0)

up to the exact phase convention.
```

Then:

```text
KERNEL-ANCHOR-RESIDUE-FORMULA
+ FIXED-SECTION-KERNEL-ANCHOR-THEOREM
=> singular-section clause for PROJECTIVE-MU-TRANSFER.
```

This is strictly smaller than demanding a quantitative invertibility margin on
the whole bordered determinant.

## 7. Status

```text
observed:  zeta bordered determinants collapse super-exponentially while the
           kernel-anchor scalar stays nonzero;
observed:  det M / (p'_A(0) scalar) is already close to a fixed phase, near
           -1, in the zeta regime;
refuted:   uniform bordered-margin invertibility as the right singular target;
refined:   the live object is the residue-level factorization of det M by the
           kernel-anchor scalar;
next:      derive the bordered determinant expansion exactly from the simple
           zero mode of A, or autopsy that formula if multiplicity/phase
           issues obstruct it.
```
