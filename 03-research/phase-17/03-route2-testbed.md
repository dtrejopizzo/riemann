# SURF-A Step 3 — Route-2 finite testbed: the γ-blindness verdict

**Phase 17, step 3.** Supports: `00-SURF-2.0-design.md` (SURF-A acceptance / A-pass-vs-A-fail);
follows `02-involution.md`. **Experiment:** `experiments/surfA_route2_testbed.py` (runs clean).
**Date:** 2026-06-06.

> **The strict F-indep test (step-2 handoff):** build `(X, j)` — a space with the real
> structure — *without any reference to zeros*, then ask whether the ordinates `{γ}` can be
> **derived**. Never define `Z_ρ` via `γ_ρ`. This is exactly where A-pass vs A-fail lives.

---

## 1. What the testbed shows

### Part 1 — the `(X, j)` scaffolding is F-indep and trivial
Build the real-structure scaffolding with **no `γ` whatsoever**: each on-line zero is a 1-dim
block with the real structure fixing it (form `+1`); each off-line quartet is a 2-dim block
`(u,v)` with real structure `c(u,v)=(u,−v)` and form `diag(1,−1)`. This reproduces the step-1
template exactly:

| config | signature | neg index |
|---|---|---|
| 5 on-line + 0 quartets | (5,0) | 0 |
| 5 on-line + 1 quartet | (6,1) | 1 |
| 5 on-line + 2 quartets | (7,2) | 2 |
| 5 on-line + 3 quartets | (8,3) | 3 |

The real structure `j` **alone** forces the `(1,0)/(1,1)` blocks and the index. No zeros used.
So the geometric scaffolding — transverse coordinate `b`, the signature law, the orbit sizes —
is **F-independently realizable, and trivially so.**

### Part 2 — but the scaffolding is **γ-blind**
Take the *same* on/off-line pattern (5 on-line + 2 off-line quartets) with three completely
different ordinate sets and compute the actual bilinear Weil-Gram signature:

| ordinate set | signature |
|---|---|
| real `ζ` ordinates `14.13, 21.02, …` | **(3, 2)** |
| random ordinates (uniform 5–60) | **(3, 2)** |
| arithmetic progression `10,20,30,…` | **(3, 2)** |

**Identical.** The negative index is `2 = #quartets` in every case; the scaffolding does not
distinguish the genuine `ζ` ordinates from random numbers. It constrains `b` and the signature
but is **blind to which `γ` appear.**

---

## 2. The verdict: SURF-A collapses into SURF-B

Putting the two halves together:

> The geometric real-structure scaffolding `(X, j)` — the part SURF-A was meant to construct — is
> **free and γ-blind.** All the nontrivial content is the **spectrum `{γ}`**, i.e. the operator
> `T`. **SURF-A reduces to SURF-B.**

This is the honest outcome, and it is exactly the bottleneck anticipated in the step-2 review:
`b` was the easy half (a transverse coordinate to `Fix(j)`); `γ` is the hard half, and it is
**irreducible arithmetic data** that no F-indep geometric scaffolding supplies. The off-axis
functional factorizes conceptually as
```
   E_{γ−ib}   =   (real-structure transverse 2-plane in b)   ×   (spectral point γ),
                   \___________ free, geometric __________/      \__ the whole problem __/
```
and only the second factor carries content.

### 2.1 What this is, and is not
- **It is** a roadmap sharpening: the two stages SURF-A and SURF-B are really **one** object —
  build the operator `T`. We do not have two problems; we have one (plus a constraint, §2.2).
- **It is not** progress toward RH (G-CAP honesty). Producing `T` with spectrum `{γ_ρ}` from
  natural F-indep data **is** the Hilbert–Pólya problem; we have not made it easier, we have shown
  the geometric dressing around it is weightless. A green box on the scaffolding is a hollow
  green box; we mark it as such.

### 2.2 The one genuinely new thing: a real-structure constraint on `T`
The collapse is not entirely vacuous. Steps 1–2 add a constraint the bare Hilbert–Pólya program
did not state: **`T` must be compatible with the anti-holomorphic real structure `j`** — it must
intertwine with `j` by `b ↦ −b`, with the functional equation `ι` and conjugation `σ` as its `±`
symmetries. Whether this real-structure compatibility *usefully* constrains `T` (e.g. forces its
spectrum to the line, or obstructs it) is precisely the SURF-B question. So the deliverable of
SURF-A is not a geometry; it is **the constraint catalogue for `T`**:
```
  (T1)  spectrum of T = {γ_ρ}            [the Hilbert–Polya / arithmetic content]
  (T2)  T intertwines the real structure j:   T compatible with b ↦ −b
  (T3)  the resolvent (T−z)^{-1} obeys the de Branges (dB2) difference-quotient identity
  (T4)  F-indep: T is built from arithmetic (primes / explicit formula), never from {γ_ρ}
```

---

## 3. A-pass / A-fail call

Against the pre-registered criteria of `00-SURF-2.0-design.md` §8:

- **Scaffolding (b, j, signature):** A-pass, but **hollow** — γ-blind, hence not a realization of
  the functionals, only of their transverse factor.
- **Functionals `E_{γ−ib}` with the actual `γ_ρ`:** **not achieved**, and shown to be
  unachievable from `(X, j)` alone. The `γ`-half is the irreducible arithmetic content.

This is **not** A-fail in the terminal sense (no claim that the functionals have *no* F-indep
origin — they may, via an arithmetic `T`). It is the sharper statement: **the origin, if any,
is entirely in the operator `T`, not in the geometry `(X, j)`.** The wall did not move; it was
**relocated precisely onto `T`** and stripped of the geometric ambiguity that surrounded it.

---

## 4. Findings (durable)

1. **The `(X, j)` real-structure scaffolding is F-indep and trivial** (Part 1): the `(1,0)/(1,1)`
   signature, transverse `b`, and orbit sizes follow from the real structure alone, no zeros.
2. **It is γ-blind** (Part 2): identical signature for `ζ`, random, and arithmetic ordinates. The
   ordinates `{γ}` are irreducible arithmetic data, not derivable from the geometry.
3. **SURF-A collapses into SURF-B.** The single hard object is the operator `T` with spectrum
   `{γ_ρ}`; the geometric dressing is weightless. This confirms `γ`, not `b`, is the bottleneck.
4. **The net deliverable of SURF-A is the constraint catalogue (T1)–(T4) for `T`**, including the
   genuinely new **real-structure compatibility (T2)**.
5. **Honesty:** the scaffolding green box is hollow (G-CAP); we have clarified the problem, not
   advanced on RH. The Hilbert–Pólya content is untouched and is now the sole target.

---

## 5. Next — straight to SURF-B

SURF-A has done its job: it has *located* the difficulty entirely in `T` and handed over the
constraint catalogue (T1)–(T4). The next document opens SURF-B with the sharpened question:

> **Is there a natural, F-indep operator `T` (built from the primes / explicit formula, the
> arithmetic side) that (T2) intertwines the real structure `j` and (T3) has a resolvent obeying
> the de Branges (dB2) identity — with (T1) spectrum `{γ_ρ}` emerging, not imposed?**

We already know the bare prime→zero transport is the explicit formula whose positivity is the
wrong-sign capstone (the program's standing wall). The *new* leverage to test in SURF-B is
whether the **real-structure constraint (T2)** changes that picture at all — i.e. whether
requiring `T` to be `j`-compatible adds a usable handle on the sign, or whether it too is
satisfied vacuously by the explicit-formula operator (in which case SURF-B re-confirms CAP from
the real-structure side, an honest negative). → `04-SURF-B-resolvent.md`.

**Pre-registered:** if the `j`-compatible arithmetic `T` reproduces only the explicit-formula
positivity with no new sign handle, that is **CAP again**, reported as such — not a failure to
hide but the expected structural outcome (§8 S5-fail of the design doc), reached one level deeper.

---

*Cross-refs:* `01-SURF-A-triage.md`, `02-involution.md`, `experiments/surfA_route2_testbed.py`,
`00-SURF-2.0-design.md` (§4 SURF-B, §8 falsifiers). *Memory:* `[[project-rh-current-direction]]`,
`[[riemann-key-contradiction]]`.
