# E94 — Quaternionic Hodge–Riemann polarization: ζ carries it, DH and random do not

**Date:** 2026-06-26 · dps=40 · λ = 7,9,11,13,15,17,19,21 · ζ vs DH falsador vs random-symmetric.
Builds on E92 (wrong involutive structure) → E93 (found AJ ≈ antisymmetric for ζ) → E94 (correct test).

## Setup

Quaternionic complex structure `J e_n = sgn(n) e_{−n}` (real, `J² = −1` on H¹, n≠0) — the
Deninger object (2204.02714; cf. E48/E50), *not* the involution E92 used. Two measurements:

1. **J-compatibility** `r(λ) = ‖[A,J]‖ / ‖A‖` (= 0 iff A respects the Hodge structure).
2. **Hodge–Riemann positivity:** complexify, take the +i-eigenspace `V₊` of J, and report the
   signature of the Hermitian form `A|V₊`. A polarization ⟺ `A|V₊` is (semi)definite.

Control: a random symmetric matrix with the **same** parity symmetry `A_{−m,−n}=A_{mn}` as A
(tests whether the positivity is merely algebraic-from-symmetry).

## Result (all λ)

| λ | ζ: r, V₊ sig | DH: r, V₊ sig | random: r, V₊ sig |
|---|---|---|---|
| 7 | 0.144, **(8,6,0)** | 0.510, (4,0,10) | 1.496, (7,0,7) |
| 11 | 0.105, **(8,10,0)** | 0.685, (6,0,12) | 1.371, (9,0,9) |
| 15 | 0.153, **(8,12,0)** | 0.741, (7,0,13) | 1.373, (9,0,11) |
| 19 | 0.160, **(8,14,0)** | 0.817, (8,0,14) | 1.386, (12,0,10) |
| 21 | 0.159, **(8,14,0)** | 0.900, (8,0,14) | 1.386, (12,0,10) |

(signature = (positive, zero, negative) eigenvalues of `A|V₊`.)

- **ζ:** `A|V₊` is **positive semidefinite at every λ** — **0 negative eigenvalues** above
  machine noise (the only sub-zero values are ~1e-16). This is the Hodge–Riemann polarization
  signature, computed *exactly* on `V₊` (J is exactly `J²=−1`). **Correction to the "rank 8"
  count below:** the V₊ spectrum is not 8 clean positives + a kernel; it is an **exponential
  cascade** with no spectral gap, e.g. at λ=21:
  `[~1e-16 noise …, 3.8e-14, 3.8e-12, 3.8e-10, 3.3e-8, 1.8e-6, 7.5e-5, 1.9e-3, 4.3e-2, 0.41, 5.5, 6.3]`
  — each positive eigenvalue ≈100× the previous, decaying to machine zero. The "8 positive" in the
  table is an artifact of the 1e-9 threshold cutting this cascade. The positivity is genuine but
  **razor-thin**: the margin → 0 like `e^{−cL}`.
- **DH falsador (off-line zeros):** `A|V₊` is **indefinite** (always has negative eigenvalues),
  and `r` grows with λ (0.51→0.90) — increasingly J-*incompatible*. Correctly fails.
- **Random-symmetric (same parity symmetry):** `r≈1.4` (strongly J-incompatible), `A|V₊`
  **indefinite**. So the positivity is **not** a trivial consequence of the symmetry.

## Honest reading — strong structural evidence, but NOT a proof (and why)

**What is genuinely new and strong:** the finite-window Weil matrix of ζ behaves *exactly* like a
**polarized weight-1 quaternionic Hodge structure** — positive semidefinite on the J-positive
subspace, with a stable primitive rank — while both the off-line falsador (DH) and a
symmetry-matched random control fail. This is the clearest intrinsic appearance of Weil/Hodge–Riemann
positivity the program has produced, and it is **not** trivially algebraic (random fails).

**Why it does not cross the wall (the honest boundary):**

1. **r_ζ saturates at ≈ 0.13–0.16, it does not → 0.** ζ is only *approximately* J-compatible;
   the residual does not vanish with λ. A genuine Hodge structure needs `[A,J]=0` exactly; the
   non-vanishing residual is plausibly the same `e^{−cL}` wall residue seen elsewhere.
2. **DH fails the V₊ positivity.** That means V₊-positivity tracks zeros-on-the-line — i.e. it
   is (so far) a **detector**, equivalent in strength to RH, not an independent input. The same
   structural trap as the Cesàro route (C1): a property that holds ⟺ RH cannot *prove* RH unless
   established by an independent argument.
3. **The independent argument is exactly MW-5.** In the function-field case HR positivity is a
   *theorem* (Hodge index theorem on the Jacobian) proven from geometry, and RH follows. Here we
   *observe* the same positivity but have no geometric realization over Spec ℤ that would make it
   a theorem rather than an observation. E94 is strong evidence that **if** the Connes–Consani
   arithmetic-site realization exists (MW-5), it would carry the right polarization — but it does
   not supply that realization.

**Verdict:** E94 advances the MW-5 lever from "no intrinsic positivity seen" to "the intrinsic
quaternionic Hodge–Riemann positivity is present for ζ, absent for DH/random." This is a real,
reproducible structural finding — the most natural form the program has found for Weil positivity.
**But the margin test settles its status: it lands on the master wall.** The V₊ spectrum is an
exponential cascade with *no spectral gap* (margin → 0 like `e^{−cL}`); the polarization is
"razor-thin", exactly the residue that has blocked every route (cf. the Phase-61 LGV "collective
razor-thin positivity", `[[riemann-phase61-phaseF-LGV]]`). So E94 does **not** cross the wall — it
re-expresses it as Hodge–Riemann polarization. It remains a detector (PSD ⟺ RH, DH fails), now
known to be a *gapless* one. No false victory: `r≠0`, DH-correlation, and the gapless cascade are
all stated.

## Net: what E94 contributes

The MW-5 / positivity lever is the right object — the finite-window Weil matrix genuinely behaves
like a polarized quaternionic Hodge structure for ζ and not for DH/random. The obstacle is now
**located precisely**: it is not "find the positivity" (it is there) but "**give the V₊ positivity
a uniform spectral gap** `e^{−cL}`-residue control without using zero locations." That is identical
to the master wall (Step 12 / `ε₀(λ)≥0`), now in its most geometric form. The crossing still
requires the geometric realization over Spec ℤ (Connes–Consani arithmetic site) that would make
HR positivity a *theorem* with a gap, rather than a gapless observation.

## Next probes (open, but wall-bound)

- The margin cascade `e^{−cL}` is the wall residue; controlling it = crossing the master wall.
- Can `A|V₊ ⪰ 0` *with a gap* be derived from the Euler-product structure without zero locations?
  This is the MW-5 crossing; E94 says it is the right target but confirms it is wall-hard.

## Reproduce

```
venv/bin/python E94_Jcompat.py "[(7.0,14),(9.0,16),(11.0,18),(13.0,18),(15.0,20),(17.0,20),(19.0,22),(21.0,22)]"
```
Predecessors: `E92_hodge_riemann.py` (phase-61, involutive — superseded), `E93_quaternionic_HR.py`.
