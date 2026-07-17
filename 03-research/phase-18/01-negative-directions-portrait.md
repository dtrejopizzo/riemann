# Camino 2, Step 1 — A portrait of the negative directions of the Weil form

**Phase 18** (the direct study of `κ`; leaves SURF behind per the strategic review).
**Experiment:** `experiments/camino2_negative_directions.py` (runs clean).
**Date:** 2026-06-06.

> **Why this line.** Phase 17 showed symmetry, real structure, resolvent and geometry are all
> *abundant* and survive even if RH is false; the only scarce ingredient is the positivity
> `κ=0`. P25 did something rare: it isolated, explicitly, the object whose existence is
> equivalent to `¬RH` — a **negative direction** of the localized Weil form, supported on the
> off-axis evaluation of an off-line quartet. So instead of building yet another realization, we
> **dissect that object**: what must a negative direction look like, inevitably, if it exists?

---

## 0. The object

For an off-line quartet `ρ = ½ + b + iγ` (`b = β−½ ≠ 0`), the localized Weil form restricted to
the quartet, on even real test functions `f`, is (P25/P26)
```
   Q_quartet(f) = 4 ( u² − v² ),
   u = ⟨f, K_u⟩,  K_u(t) = cosh(b t) cos(γ t),     (the "real / on-line" mode)
   v = ⟨f, K_v⟩,  K_v(t) = sinh(b t) sin(γ t).     (the "imaginary / off-line" mode)
```
The form is **rank 2** — it sees `f` only through `(u,v)` — with signature `(1,1)`: one negative
direction, the combination that suppresses `u` and lives on `v`. We compute that direction in an
orthonormal even Hermite basis (so the metric is `I`) and read off its properties.

---

## 1. The four inevitable properties (all verified)

### P1 — Shallowness (the `δ²` law), per direction
Along a **fixed** test function `f₀` (frozen, orthogonal to the on-line mode `cos γt`),
`Q(f₀; b)/b² → const` and `Q < 0`:

| `b` | `Q(f₀;b)` | `Q/b²` |
|---|---|---|
| 0.020 | −1.49e1 | −3.73e4 |
| 0.010 | −3.51e0 | −3.51e4 |
| 0.005 | −8.64e−1 | −3.46e4 |
| 0.0025 | −2.15e−1 | −3.44e4 |

So **each negative direction is shallow, `O(b²)`**, vanishing as the zero approaches the line
(recovers the `δ²` law of P7 from the direction viewpoint).
**Honest caveat (important):** the *supremum* of `−Q` over `L²` is `+∞` — the off-axis
evaluation is unbounded in `L²` (the Phase-4 fact). Shallowness is a **per-direction**,
bandwidth-relative statement, *not* a bound on the negative eigenvalue. This is exactly why the
realization needs a weighted (de Branges) space, and it is the first structural tension in the
portrait: the negativity is individually shallow but collectively unbounded.

### P2 — It is the "imaginary" (sinh-sine) mode
The negative eigenvector suppresses `u` and lives on `v`: `|u(f)/v(f)| ≈ 4×10⁻³` (`b=0.20`),
`≈ 9×10⁻⁴` (`b=0.05`). A negative direction is precisely a test function nearly **orthogonal to
the on-line evaluation** `cos γt`, aligned with the off-line **`sinh(bt) sin(γt)`** mode. The
negativity is the imaginary part of the off-axis value, `Re(w²)=u²−v²<0 ⟺ |Im w|>|Re w|`.

### P3 — Frequency localization at the ordinate `γ`
The transform `|f̂(ξ)|` of the negative direction **peaks at `ξ = γ`**, to high precision:

| `γ` | `argmax_ξ |f̂(ξ)|` | `|peak − γ|` |
|---|---|---|
| 10.000 | 9.945 | 0.06 |
| 14.134 | 14.063 | 0.07 |
| 21.022 | 21.091 | 0.07 |
| 25.011 | 24.914 | 0.10 |

A negative direction is a **wave packet at frequency `γ`** — the ordinate of the zero is its
carrier frequency. This is the geometric meaning of "the off-axis functional at `γ−ib`."

### P4 — Near-orthogonality across quartets
Negative directions for well-separated `γ` are nearly orthogonal (max off-diagonal overlap
`0.054` for gaps `~3–4` in `γ`); the Gram of directions is near-diagonal. So distinct off-line
zeros give **near-independent** negative directions — the geometric content behind the
finite-case independence lemma of P26.

---

## 2. The portrait, and the structural tension it exposes

> **A negative direction, if it exists, is a shallow (`O(b²)`), frequency-`γ`-localized wave
> packet living on the `sinh`-`sin` (imaginary) mode, nearly orthogonal to the directions of
> other zeros. The negative cone is a sum of such lines, one per off-line quartet.**

Two facts in this portrait pull against each other, and the tension is the real content:

- **(individually shallow)** each negative direction has `Q ~ −b²` — arbitrarily weak as `β→½`;
- **(collectively unbounded)** the supremum of `−Q` over `L²` is `+∞`, and the directions at
  different `γ` are independent and frequency-localized, so they **tile frequency space** and do
  not interfere.

A *single* off-line zero is a shallow, harmless dent. The danger, if any, is **collective**: an
infinite family of independent shallow dents, one per frequency `γ`. Whether such a family can
coexist is **not** decided by the single-quartet analysis — and that is exactly where the next
question lives.

---

## 3. The real handle (next step): are the directions mutually compatible with `ξ`?

The single-quartet portrait treats each off-line zero as **free**: any `(b, γ)` gives a valid
`(1,1)` block. But the off-line zeros are **not** free — they are zeros of **one entire function
`ξ`**, constrained by:
- the **Hadamard product** `ξ(s) = ξ(0)∏_ρ(1−s/ρ)e^{s/ρ}` (the zeros determine `ξ` and each
  other through one analytic object);
- equivalently the **explicit formula** (the zeros are dual to the primes).

So the operative question for `κ` is **not** "can one negative direction exist?" (yes, trivially,
for any synthetic `(b,γ)`), but:

> **Is a collection of these shallow, `γ`-localized, independent negative directions compatible
> with all the `γ` being ordinates of zeros of a single function `ξ` with the known
> prime/explicit-formula coupling — or does that coupling forbid a free family of them?**

This is the first question in the whole program that attacks `κ` **directly** and is *not*
obviously CAP: it does not ask for a positivity of a realization; it asks whether the **arithmetic
rigidity of `ξ`** (Hadamard/explicit formula) is consistent with the negative-direction portrait.
Two honest outcomes:
- **(a) compatible** — a free family of negative directions is consistent with `ξ`'s rigidity:
  then the portrait gives no obstruction, and `κ>0` is not excluded this way (an honest null, but
  a sharp one — it would say the arithmetic does not see the dents).
- **(b) incompatible** — the explicit-formula coupling forbids the simultaneous existence of the
  `γ`-localized negative directions: that would be a genuine handle on `κ`, the first non-CAP one.

We do not prejudge which. The point of Camino 2 is that this is a **well-posed, falsifiable**
question about the object Phase 17 identified as irreducible.

---

## 4. Next

- **Step 2 (the compatibility probe).** Couple the negative directions to the explicit formula:
  build the bilinear form `Q(f,f) = Σ_ρ φ_f(ρ)²` for a **test family adapted to a putative
  off-line zero** and ask whether the on-line zeros' (positive) contributions at the *same
  frequency `γ`* must cancel the off-line dent — i.e. whether the prime side fixes the sign at
  frequency `γ`. This is the explicit-formula coupling of §3, made into a finite experiment.
  → `02-explicit-formula-coupling.md`.
- **In parallel (P29 consolidation):** the Phase-17 symmetry-vs-positivity dichotomy is
  independent of this and can be written up while Camino 2 runs.

---

## 5. Findings (durable)

1. **Negative directions are explicitly characterized** (first time): shallow `O(b²)` (P1),
   the `sinh`-`sin`/imaginary mode (P2), frequency-localized at `γ` (P3), near-orthogonal across
   zeros (P4).
2. **The tension is shallow-but-unbounded:** individually harmless `O(b²)` dents, but collectively
   unbounded and frequency-tiling — the danger, if any, is collective, not per-zero.
3. **The direct handle on `κ` is the arithmetic-compatibility question** (§3): can the family of
   `γ`-localized negative directions coexist with `ξ` being one entire function (Hadamard /
   explicit formula)? This is well-posed, falsifiable, and *not* obviously CAP — the first such
   question aimed straight at `κ`.

---

*Cross-refs:* `../06-papers/P25` (the localization and the off-axis functional), `../06-papers/P7`
(the `δ²` law), `../06-papers/P26` (independence of off-axis evaluations),
`../phase-4-handoff/proofs/00-PROOF-LOG.md` (off-axis evaluation unbounded in `L²`),
`../phase-17/04-SURF-B-resolvent.md` (symmetry vs positivity — why this is the remaining target).
*Memory:* `[[project-rh-current-direction]]`, `[[riemann-key-contradiction]]`.
