# SURF-A Triage — Geometry of the off-axis functionals

**Phase 17, step 1.** Supports: `00-SURF-2.0-design.md` §3 (SURF-A), acceptance test A.4.
**Experiment:** `experiments/surfA_gram_signature.py` (runs clean).
**Date:** 2026-06-06.

> **SURF-A question (only this — no Lefschetz, no RH):** what geometric object's cohomology
> produces the off-axis evaluation functionals `E_{γ−ib}` of P25, with the on-line/off-line
> `(1,0)/(1,1)` signature of P26, **F-independently** (cycles not built from `{γ_ρ}`)?

---

## 1. The TARGET template (what any candidate must reproduce) — established

The finite Gram experiment fixes, on a concrete config and a 6-function even test basis, exactly
what the geometry must match. All four checks pass:

| Check | Result | Meaning |
|---|---|---|
| **(A)** on-line block (`b=0`) | signature **(1,0)** | a real evaluation → one positive direction |
| **(A)** off-line block (`b=0.20`) | signature **(1,1)**, eigs `≈ ±10.7` | complex evaluation → one `+`, one `−` |
| **(B)** `b`-scaling | `λ_min: 0 → −0.41 → −2.9 → −8.3 → −10.5` as `b: 0→0.02→0.05→0.10→0.20` | the negative direction **switches on continuously with `b`** = distance to the real locus (confirms A.2) |
| **(C)** `K` distinct off-line quartets | signature `(K,K,·)`, **neg index = K** for `K=0,1,2,3` | the negative index **counts off-line quartets** (`= κ/4`) |

So the geometric object must carry a bilinear intersection form whose **per-zero block signature
is `(1,0)` on the critical line and `(1,1)` off it**, with the off-axis coordinate `b = β−½`
controlling the negative direction. This is now a precise, falsifiable acceptance template, not a
slogan.

## 2. The arithmetic Hodge-index mechanism: compatible, with one constraint and one catch

**Compatible (mechanism exists).** An arithmetic surface carries an intrinsic **indefinite**
intersection pairing: by the **arithmetic Hodge index theorem (Faltings–Hriljac)** the pairing on
the arithmetic Picard group has Lorentzian signature `(1, n−1)` — one positive direction, the rest
negative. Experiment block **(D)**: such a `(1, N−1)` form, restricted to a 2-plane that contains
the one positive direction, gives exactly `(1,1)`; restricted to the positive direction alone, it
gives `(1,0)`. **So the signature mechanism the Weil form needs is the standard signature of an
arithmetic-surface intersection form.** This is the first time in the program that the off-line
`(1,1)` blocks have a named geometric source.

**Constraint (not automatic).** Block **(D)** also shows a *generic* 2-plane in `(1, N−1)` is
`(0,2)` ~88% of the time and `(1,1)` only ~12% — the positive cone is "thin" (1 timelike vs `N−1`
spacelike directions). Therefore **every off-line cycle-plane `Z_ρ` must contain the single
positive (polarization) direction** to match the Weil `(1,1)`. A candidate geometry must *explain*
why all off-line cycles meet the positive cone; this is a genuine demand, not a freebie.

**Catch (G-HEIGHTS).** In the **existing** arithmetic surface, the negative-definite part of the
Faltings–Hriljac form is the **Néron–Tate height pairing**, and the single positive direction is
the fiber/polarization. That negative part is the **wrong object** (G-HEIGHTS): the off-line zeros
are *not* heights (a Hilbert–Pólya spectrum is not a height pairing). So a candidate that places
the `Z_ρ` inside the usual `Pic⁰` fails F-heights. The off-line zeros must live in a **different**
indefinite structure on the surface — one whose negative directions are the zeros, not heights.
That different structure is precisely what SURF must supply; the existing surface is not it.

## 3. Triage of the three candidate homes (against the target + filters)

### Route 1 — `Spec ℤ ×_{𝔽₁} Spec ℤ` (Connes–Consani). **SURVIVES (primary).**
- **S1 spectrum:** in the Connes–Consani program the zeros are the spectrum of Frobenius/flow on a
  cohomology, with the *test-function* trace = explicit formula (G-TRACE compatible, by design).
- **S2/S3 target:** the diagonal `Δ` is the candidate **real locus** (on-line); off-diagonal
  position is the candidate `b`. The self-intersection of the off-diagonal correspondence classes
  would carry the indefinite form. **Signature-compatible** with §2.
- **F-heights:** *passes in principle* — the relevant cycles are the **zero-carrying** classes
  (diagonal minus Frobenius correspondences), explicitly **not** `Pic⁰`/heights. This is the whole
  point of the missing surface.
- **F-indep:** **the open test.** Does the construction of `Z_ρ` reference `{γ_ρ}`? In the
  Connes–Consani framing the zeros *emerge* as Frobenius eigenvalues, so F-indep holds *if the
  surface is built first*. **Unconstructed** — this is exactly where SURF-A's burden lies.
- **Verdict:** the only route that is signature-compatible *and* passes F-heights *and* could pass
  F-indep. Most aligned, least built. **Carry forward as the primary SURF-A target.**

### Route 2 — `δ`/`𝔽₁`-cohomology with intersection theory + diagonal `Δ`. **SECONDARY.**
- Has a diagonal (real locus) and could carry an intersection form, but the **Lorentzian
  signature must be proven, not assumed** — there is no Hodge-index theorem in hand for it.
- Effectively a hand-built model of Route 1's intersection theory; useful as a **finite testbed**
  for the F-indep and cone-membership questions before the full surface exists.
- **Verdict:** keep as the place to *build the finite Gram model* of A.4 and test F-indep, since
  Route 1 is unconstructed.

### Route 3 — direct Lorentzian / split real form. **REJECT as standalone (mechanism only).**
- The modular-surface incarnation already **failed** (Phase 16: every Eisenstein pairing was
  definite or `β`-blind). A bare split form has the signature mechanism but **no Frobenius/zero
  spectrum** (fails S1) and no F-indep link to `ζ`.
- **Verdict:** its *signature mechanism* (the indefinite metric) is what Routes 1–2 must realize,
  but it is not itself a home. Do not pursue as a standalone geometry.

## 4. Findings (durable)

1. **Target fixed and falsifiable.** Any SURF-A geometry must reproduce: per-zero block `(1,0)`
   on-line / `(1,1)` off-line; negative index = number of off-line quartets; negative direction
   continuous in `b`. (Experiment A–C.)
2. **Named geometric mechanism.** The off-line `(1,1)` blocks are signature-compatible with the
   **Lorentzian `(1, n−1)` arithmetic Hodge-index form** — the first geometric source for them in
   the program. (Experiment D.)
3. **New constraint (cone membership).** Each off-line cycle-plane must contain the single positive
   (polarization) direction; this is *not* generic (~12% of random planes) and a candidate must
   explain it.
4. **The catch is sharp.** In the existing surface the negative part is Néron–Tate heights
   (G-HEIGHTS, wrong object). SURF must carry the zeros in a *different* indefinite structure —
   confirming the missing-surface picture rather than dissolving it.
5. **F-indep is the decisive open test**, and it lives in Route 1 (Connes–Consani), with Route 2 as
   the finite testbed.

## 5. Immediate next steps

- **Step 2 (name the involution).** Formalize the real-locus involution whose off-locus distance is
  `b = β−½`: the candidates are the functional-equation involution `s ↦ 1−s` and conjugation
  `s ↦ s̄`, realized on the diagonal of `Spec ℤ ×_{𝔽₁} Spec ℤ`. Decide which is "the real locus"
  and whether `b` is the Arakelov/archimedean distance to `Δ`. → `02-involution.md` (next).
- **Build the Route-2 finite testbed** for A.4: a `δ`-intersection model where the `Z_ρ` are
  defined **without** reference to `{γ_ρ}`, then check (i) it reproduces the target template of §1
  and (ii) each off-line cycle meets the positive cone (§2 constraint). This is the F-indep trial
  that decides **A-pass vs A-fail**.
- **Literature pin before building:** Connes–Consani (`Spec ℤ ×_{𝔽₁} Spec ℤ`, the scaling site),
  Faltings–Hriljac (arithmetic Hodge index, to confirm the `(1, n−1)` signature and that its
  negative part is heights). Read before constructing Route 2.

## 6. Pre-registered honesty checkpoint

If the Route-2 testbed can only reproduce the target by **feeding in `{γ_ρ}`** (F-indep fails), or
can only get the `(1,1)` by placing the `Z_ρ` in the **height** part (F-heights fails), then
**A-fail**: the off-axis functionals have no F-independent geometric origin, and we report that as
the structural negative it is — consistent with the standing CAP/SURF map. We do not "try harder";
we state the limit. Conversely, an F-indep finite model reproducing §1's template would be the
first genuine geometric realization of the off-axis functionals and the green light for SURF-B.

---

*Cross-refs:* `00-SURF-2.0-design.md` (§3 SURF-A, filters), `experiments/surfA_gram_signature.py`,
`../06-papers/P25,P26` (the functionals and their signature), `../phase-16/` (why the modular
surface failed Route 3). *Memory:* `[[project-rh-current-direction]]`.
