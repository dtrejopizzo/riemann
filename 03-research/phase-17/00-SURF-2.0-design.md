# SURF 2.0 — Internal Design Document

**Status:** internal design / roadmap. NOT for publication.
**Author:** David Alejandro Trejo Pizzo
**Date:** 2026-06-06
**Supersedes (as the working spec):** `phase-16/00-SURF-SPEC-SHEET.md` (still valid; this
document refines it in light of the obstruction chain P22–P28).

> **Purpose.** The arc P22–P28 changed the question. We no longer ask *"which Hilbert/Kreĭn
> space could carry the Weil form?"* — that has been explored and answered (the indefinite de
> Branges space, with two explicit residual gaps). We now ask the much more specific question
> that the chain isolated:
>
> **What geometry produces exactly (i) the off-axis evaluation functionals of P25 and (ii) a
> resolvent obeying the de Branges difference-quotient identity (dB2) of P28?**
>
> This document fixes what SURF 2.0 must produce, the minimal properties it needs, and how the
> two residual objects should emerge. When it is complete and stable, it gates the writing of
> P29. Not before.

---

## 0. Honesty guardrails (carried over, non-negotiable)

These are the standing rules of the program; they bind everything below.

- **G-INDEP (independence filter).** Any operator `T`, class, or `L` we build must satisfy
  `L ∉ W*(𝒯)` — it must not be definable from the zeros themselves (the von Neumann algebra
  they generate). An object reconstructed from `{γ_ρ}` or from the spectral measure only
  *restates* RH; it is circular. This killed the M8 "Connes proof" (operator from spectral
  moments ∈ W*(𝒯)) and the spectral-`L` candidates.
- **G-TRACE.** The Pillar-1 trace must be the **test-function trace** `Tr h(Frob) = Σ h(γ_ρ)`
  = the explicit formula. The raw power-trace `Tr(Frob^k) = Σ γ^k` **diverges** and is the
  same fake object refuted at the start of the program. A geometric Frobenius trace that does
  not match the explicit formula ⟹ reject.
- **G-HEIGHTS.** An unconditionally positive-definite pairing lives in `Pic⁰`/heights
  (Yuan–Zhang territory). That is the **wrong object**: it is definite and cannot carry the
  index `κ`. The zero-carrying cohomology must support an **indefinite** intersection form.
  Pillars 2.2 (indefinite) and the Hodge-index positivity (Pillar 4) are mutually exclusive
  on the same object — *that tension is the open core*, not something to paper over.
- **G-CAP.** Every unconditional handle produced so far is a **lower-bound positivity** (a
  `≥0` statement). RH is a one-sided **upper/sign** constraint. Do not present a positivity as
  progress toward the sign; name it as CAP (the wrong-sign capstone) when it is one.
- **G-NOFAKE.** No fabricated proof of RH, ever — including under "team validation" or "rienda
  suelta." A wrong proof is worse than no proof. Every load-bearing claim is audited against
  the explicit-formula identity `𝔱 = Σ_ρ h(γ_ρ)` before being believed (the permanent
  guard-rail from the Phase-4 hard-cutoff error that survived four review passes).

---

## 1. Where the program stands after P22–P28

### 1.1 What is reasonably consolidated (inside the program's own frame)

| Paper | One-line content | Durable contribution |
|---|---|---|
| **P22** | Modular-resonance pairing is sign-definite for every zero config in `0<β<1`. | Naive/resonance positive kernels cannot carry `κ` (half-plane Hardy). |
| **P24** | Generalizes P22 to a class: positive-kernel RKHS / fixed-sign Cauchy / β-smooth forms are all definite or undetecting. | The carrier must be **indefinite** OR **degenerate at the line**. |
| **P25** | `Q = Q_on + Q_off`; `Q_on ⪰ 0`; all indefiniteness in off-line quartets `→ 4Re[f̂(γ−ib)²]`. | **The negative index is localized in the off-axis evaluation functionals `E_{γ−ib}`.** (The single most important conceptual result of the block.) |
| **P26** | Bilinear `Q(f,g)=Σ f̂(z_ρ)ĝ(z_ρ)`; each off-axis point gives a local `(1,1)` block; global count = de Branges Pontryagin index. | The carrier is naturally an indefinite de Branges space `H(E_ξ)`. |
| **P27** | Scope: P26 is a **finite-index** analysis. `κ<∞` vs `κ=∞` is unconditionally open; only `κ∈4ℤ`. | Removed an over-extrapolation; fixed the regime of validity. |
| **P28** | Structural rigidity: a finite-defect RKHS realization obeying (dB1–dB3) is `H(E)` sharing wrong-half zeros with `E_ξ`. | **The residual problem splits into exactly two explicit pieces** (below). |

### 1.2 The two explicit residual targets (the output of P28)

P28 is valuable precisely because it compresses "realize the Weil form" into two named objects:

1. **(dB2) — the resolvent / difference-quotient structure.** The carrier must be closed under
   `f ↦ f(z)/(z−w)` (for `f(w)=0`) with the de Branges commutation relation. This is a
   *shift/resolvent* structure — exactly what the resolvent `(T−z)^{-1}` of a Hilbert–Pólya
   operator would supply. P28 isolates it as the single substantive (operator-theoretic)
   hypothesis; it is **not** read off from the symmetries of `Q`.

2. **(ID) — the identification `E = E_ξ`.** Kreĭn–Langer pins the carrier to the class `H(E)`
   and fixes its *wrong-half-plane* zeros (= the off-line zeros). It does **not** fix the
   on-line spectrum, the modulus, or the boundary phase. Matching the full structure function
   (equivalently the reproducing kernel) of `ξ` is left open and is genuinely deeper.

### 1.3 What is NOT resolved

- **The geometric origin of `E_{γ−ib}`.** P25 *locates* the functionals; nothing says where
  they *come from*. They are analytic objects with no realized geometry.
- **The resolvent itself.** P28 says "if a (dB2)-resolvent exists, we enter de Branges." It
  does not construct one.
- **(ID).** Open by P28's own statement.
- **RH.** Nothing in P22–P28 implies it. The gain is a sharp localization of *where the
  difficulty lives*, not a reduction in its depth.

### 1.4 The map of the path to RH (today's honest version)

```
RH
│
├─ (ID)   Identify completely  E = E_ξ              ⟵ SURF-C
│
├─ (dB2)  Construct a resolvent obeying (dB2)       ⟵ SURF-B   ★ the critical step
│
├─ (GEO)  Construct the SURF geometry               ⟵ SURF-A
│
├─ Understand the off-axis functionals E_{γ−ib}     ⟵ P25–P28 (done)
│
└─ Localize the negative index κ                    ⟵ P25 (done)
```

The bottom two rungs are P25–P28. SURF 2.0 is the program for the next three rungs, **in this
order** (geometry → operator/resolvent → identification), never starting from RH.

---

## 2. What SURF must produce — the refined spec

The Phase-16 spec sheet had four Pillars (Spectrum / Pairing / Lefschetz / Positivity). P22–P28
**refine Pillar 2 and add a new requirement** that did not exist before the chain: the
realization must carry a **resolvent**, not merely a pairing. Updated spec:

### S1 — Spectrum (unchanged in spirit, sharpened by G-TRACE)
A geometric object `X` (over `Spec ℤ`, or its `𝔽₁`-analogue) with an endomorphism `Frob` (or a
flow generator) whose **test-function trace** reproduces the explicit formula:
`Tr h(Frob) = Σ_ρ h(γ_ρ)` for `h` in the admissible class. **Not** `Σ γ^k` (G-TRACE).

### S2 — Off-axis functionals (NEW, from P25)
The cohomology / cycle theory of `X` must produce, for each zero `ρ = ½ + b + iγ`, an
evaluation functional that *is* `E_{γ−ib}: f ↦ f̂(γ−ib)`. Concretely: a family of cycles or
cohomology classes `{Z_ρ}` such that pairing a test class against `Z_ρ` equals `f̂` evaluated at
the off-axis point. The **off-axis-ness** (`b ≠ 0` ⟺ off-line zero) must be a *geometric*
feature of `Z_ρ` — e.g. its position relative to a diagonal / a real locus — not an analytic
accident. (This is SURF-A.)

### S3 — Indefinite intersection form (P26, constrained by G-HEIGHTS)
The pairing of the `{Z_ρ}` must be the **bilinear** Weil form `Q(f,g)=Σ f̂(z_ρ)ĝ(z_ρ)`, which
is *indefinite* with negative index `κ`. It must **not** be the definite height pairing
(G-HEIGHTS). The local `(1,1)` signature of each off-axis block (P26 Thm F) should be the
*geometric* self-intersection signature of `Z_ρ`.

### S4 — Resolvent / (dB2) (NEW, from P28 — the critical requirement)
There must be a **natural operator `T` on `X`** (a geometric correspondence: Frobenius, a
Hecke/scaling generator, a vector field of a flow) whose resolvent `(T−z)^{-1}` induces the
difference-quotient operation `f ↦ f(z)/(z−w)` on the realized space, satisfying the de Branges
commutation relation (dB2). **This is the heart of SURF 2.0.** Without it, P28 says we are not
even in the de Branges universe.

### S5 — Positivity / Lefschetz (the open core, unchanged)
A Hodge-index / Lefschetz positivity on the zero-carrying `H¹` that would force `κ=0`. By
G-HEIGHTS and the Lefschetz dichotomy (P21), this is **not** suppliable by Yuan–Zhang and is
the genuinely new theorem. SURF 2.0 does **not** attempt S5 until S1–S4 are in hand; attempting
it first is how spectral programs die (and is forbidden by the staged order of §1.4).

### Rejection filters (carried from the spec sheet, all still active)
- **F-spectrum:** geometric Frob trace ≠ explicit formula ⟹ reject (kills `J₀(N)` etc.).
- **F-heights:** unconditionally pos-def pairing ⟹ in `Pic⁰` ⟹ reject (G-HEIGHTS).
- **F-indep:** `{γ_ρ}` or the anatomy used as input ⟹ circular ⟹ reject (G-INDEP, P21).
- **F-cite:** S5 closed by citing Yuan–Zhang ⟹ reject (wrong object).
- **F-resolvent (NEW):** a candidate that supplies S3 (pairing) but has *no* natural `T` for S4
  ⟹ it is a Phase-16-style dead end (definite or pairing-only). The modular surface failed here:
  it gave the zeros (S1) and a pairing, but the pairing was definite (CAP) and carried no
  indefinite resolvent.

---

## 3. SURF-A — Geometry of the off-axis functionals

**Goal:** construct a geometric object whose cohomology produces exactly the `E_{γ−ib}`. **Do
not** attempt Lefschetz or RH here. Only: *what represents these functionals?*

### A.1 The concrete question
The Weil form is `Q(f,g) = Σ_ρ φ_f(ρ) φ_g(ρ)`, a sum over zeros. In a geometry where zeros are
**Frobenius eigenvalues / intersection points**, this is a sum over intersection points of two
cycles. So:

> If `E_{γ−ib}` is "evaluation at the zero `ρ`," what cycle, divisor, or cohomology class `Z_ρ`
> represents it, and why is its *off-axis* coordinate `b = β−½` a geometric quantity?

### A.2 The decisive structural clue (must be respected)
On-line (`b=0`) the functional is **real** and the block is positive `(1,0)`; off-line (`b≠0`)
it is **complex** and the block is indefinite `(1,1)` (P26). So the geometry must have a **real
locus / involution** (the functional equation `ρ ↔ 1−ρ`, conjugation `ρ ↔ ρ̄`) such that:
- a zero **on** the real locus (the critical line) ⟹ a class with **definite** self-pairing;
- a zero **off** it ⟹ a class with **indefinite** self-pairing, the deviation governed by the
  distance `b` to the real locus.

This is exactly the behaviour of an **intersection form near a real/anti-holomorphic
involution** — a `(1,1)`-type signature appearing for cycles in "general position" relative to a
real structure. SURF-A's target is to name the involution and the cycles.

### A.3 Candidate geometric homes (to be triaged, like Phase-16 Pillar 1)
1. **The arithmetic surface `Spec ℤ ×_{𝔽₁} Spec ℤ`** (Connes–Consani). The diagonal is the
   real locus; off-diagonal intersection = off-line. Most aligned, least constructed.
2. **A `δ`-/`𝔽₁`-cohomology** with an intersection theory and a diagonal `Δ` (Phase-16 Route B,
   "untestable" then for lack of a constructed object — SURF-A is where it would be built).
3. **A Lorentzian / split real form** (Phase-16's indefinite-signature hunt) — *but* the
   modular-surface incarnation failed (β-blind / definite). SURF-A would need a *different*
   carrier of the split signature, tied to the involution of A.2.

### A.4 SURF-A acceptance test
Produce, for at least a **finite** set of zeros, explicit classes `Z_ρ` with:
- pairing matrix `= [φ_{f_i}(ρ_j)]`-type Gram (S2/S3),
- self-pairing signature `(1,0)` on-line, `(1,1)` off-line (A.2),
- and pass **F-indep**: the construction of `Z_ρ` must not take `{γ_ρ}` as input. (This is the
  hard part and where most candidates will die — exactly as in Phase 16.)

A.4 is a finite, checkable, **falsifiable** milestone — in the spirit of the program's best
work (finite Gram-matrix tests). It does **not** require building the full surface.

---

## 4. SURF-B — Emergence of the resolvent (dB2) — the critical step

**Goal:** exhibit a natural operator `T` on the SURF-A geometry whose resolvent realizes the
difference-quotient structure (dB2). This is what P28 named as the single substantive content.

### B.1 Why this is the crux
de Branges' (dB2) identity is, at bottom, a **resolvent identity**. The operation
`f ↦ (f(z)−f(w))/(z−w)` is the divided difference; its closure is multiplication-by-`z`
inverted, i.e. `(T−z)^{-1}` for `T = ` "multiplication by the spectral variable." In the
Hilbert–Pólya picture `T` is *the* self-adjoint operator with spectrum `{γ_ρ}`. So:

> **SURF-B = realize the Hilbert–Pólya operator as a geometric correspondence on `X`, and check
> that its resolvent gives (dB2).**

The novelty vs. naive Hilbert–Pólya: we are **not** asked to prove `T` self-adjoint (that would
be RH). We are asked to **construct a natural `T`** (a geometric endomorphism, F-indep) and show
its resolvent has the de Branges commutation structure. Self-adjointness/`κ=0` is deferred to S5.

### B.2 The concrete question
On the SURF geometry, the natural endomorphism is **Frobenius / the flow generator** (S1). Its
"multiplication by `z`" avatar acts on the realized space of P25/P26. Ask:

> Does `(Frob − z)^{-1}` — equivalently the geometric correspondence
> `Z ↦ (Z − z·Δ)^{-1}·Z` on cycles — induce `f ↦ f(z)/(z−w)` on the realized functions, with
> the (dB2) commutation `[f/(·−w), g] − [f, g/(·−v)] = (v̄−w)[f/(·−w), g/(·−v)]`?

The right-hand side `(v̄−w)` is a **resolvent identity**; geometrically it should be an
**intersection identity** for the graph of `Frob` shifted by `z` and `w` — a Lefschetz-type
fixed-point / correspondence computation.

### B.3 What success looks like
- The (dB2) relation becomes a **correspondence identity** on `X` (graphs intersect with the
  prescribed multiplicities), verifiable on the finite SURF-A model.
- `T = ` geometric `Frob` is **F-indep** (it is part of the geometry, not built from zeros).
- Then P28 applies: the realized space **is** `H(E)` with `E` sharing `E_ξ`'s wrong-half zeros —
  and we have *constructed* it, not assumed it. P28's (dB2) gap is closed **geometrically**.

### B.4 The honest danger (state it up front, per G-NOFAKE)
The risk: any `T` we can write whose resolvent gives (dB2) might secretly be **multiplication by
the spectral variable on `W*(𝒯)`** — i.e. F-indep *fails*, and we have only re-described the
zeros. SURF-B must therefore produce `T` **from the geometry first** and *derive* its spectrum,
never the reverse. Guard-rail: before believing any (dB2) realization, check that `T`'s
definition never references `{γ_ρ}`. If it does, it is circular (the M8 failure mode).

---

## 5. SURF-C — Recovering `E_ξ` (the identification (ID))

**Only after SURF-A and SURF-B.** Order: geometry → operator → resolvent → kernel → `E` → RH.

### C.1 The question
P28 leaves `E` determined only up to its wrong-half zeros + an HB factor on the on-line spectrum
+ normalization. SURF-C asks the geometry to fix the rest:

> Does the reproducing kernel of the SURF-B realization equal the de Branges kernel of
> `E_ξ(z)=ξ(½+iz)` — matching the **on-line spectrum**, the **modulus** `|E_ξ|` (the archimedean
> `Γ`-factor geometry, cf. Phase-4 DB.1–DB.3), and the **boundary phase**?

### C.2 Where the pieces should come from
- **On-line spectrum / modulus:** the **archimedean place** of `X` (the `Γ`-factor; the
  "place at ∞" of the arithmetic surface). Phase-4 already identified `Ω(r)=2Re(γ'/γ)(½+ir)` as
  the archimedean multiplier; SURF-C should see `|E_ξ|` as the archimedean local factor of `X`.
- **Boundary phase:** the functional equation `ξ(s)=ξ(1−s)`, realized as the involution of A.2.

### C.3 Only here does RH (S5) enter
With `E = E_ξ` identified, RH ⟺ `E_ξ` Hermite–Biehler ⟺ `κ=0` ⟺ the Hodge-index positivity S5.
This is the **last** rung, and it is the genuinely new theorem (not Yuan–Zhang). SURF-C makes S5
*well-posed on a constructed object*; it does not pretend to prove it.

---

## 6. The single-sentence summary (for the proof log / MAP)

> P22–P28 do not bring us directly closer to a proof of RH, but they compress the residual
> functional-analytic problem to **two explicit objectives: build a geometry that generates the
> off-axis functionals `E_{γ−ib}` (SURF-A), and obtain from it a resolvent obeying the de Branges
> identity (dB2) (SURF-B).** Identification `E=E_ξ` (SURF-C) and the Hodge-index positivity
> (S5/RH) come strictly after, in that order. SURF 2.0 is the program for SURF-A → SURF-B →
> SURF-C; it never starts from RH.

---

## 7. Immediate next actions (concrete, falsifiable, in order)

1. **SURF-A triage (analogue of Phase-16 Pillar 1).** For each candidate home (§A.3), ask only:
   *can it produce a finite Gram model of `E_{γ−ib}` with the `(1,0)/(1,1)` signature, F-indep?*
   Reject fast on any failed filter. **Deliverable:** `phase-17/01-SURF-A-triage.md` + a finite
   Gram-matrix experiment (like the Phase-16 detectors).
2. **Name the involution (A.2).** Write down the real locus / anti-holomorphic involution whose
   "off-locus distance" is `b=β−½`. This is shared by A and B and should be settled early.
3. **SURF-B resolvent probe.** On whatever finite model survives A.4, test whether a geometric
   `Frob`-resolvent induces the divided-difference (dB2) relation as a **correspondence
   identity**. **Deliverable:** `phase-17/02-SURF-B-resolvent.md` + the correspondence-identity
   check.
4. **Literature pin (do not reinvent).** Connes–Consani `Spec ℤ ×_{𝔽₁} Spec ℤ` and the
   archimedean de Branges/`Γ`-factor (Lagarias, Burnol) for C.2 — read before constructing.
5. **Only then** decide P29, and only on whatever **actually closed** (most likely a SURF-A
   finite-model result or a SURF-B correspondence identity), never on the aspiration.

---

## 8. What would make this fail honestly (pre-registered falsifiers)

Per the program's "break it before you build it" discipline, SURF 2.0 is **falsified / stalled**
if any of these hold, and we say so plainly:

- **A-fail:** every candidate geometry either cannot produce `E_{γ−ib}` without taking `{γ_ρ}`
  as input (F-indep fails) or produces only a **definite** pairing (CAP again). Then SURF-A is
  the same wall as Phase 16, and the off-axis functionals have no F-indep geometric origin.
- **B-fail:** a (dB2)-resolvent exists only as multiplication-by-`z` on `W*(𝒯)` (F-indep fails).
  Then SURF-B is circular and P28's (dB2) is not geometrically closable — Hilbert–Pólya remains
  an aspiration.
- **C-fail:** the SURF kernel matches `E_ξ`'s zeros but not its modulus/phase, so `E ≠ E_ξ` and
  (ID) is genuinely unreachable from this geometry.
- **S5-fail (expected):** even with A–C done, the Hodge-index positivity is the wrong-sign
  capstone in geometric dress (G-CAP) and is no more accessible than before. This is the
  *likely* outcome and must be reported as such, not hidden.

If A or B fails F-indep, the correct conclusion is **not** "try harder" but "the off-axis
functionals / the resolvent have no independent geometric source," which is itself a sharp,
publishable structural negative — consistent with the standing CAP/SURF map.

---

*Cross-refs:* `phase-16/00-SURF-SPEC-SHEET.md` (Pillars/filters), `phase-15/...` (Lefschetz
dichotomy P21), `phase-4-handoff/proofs/00-PROOF-LOG.md` (de Branges / archimedean `Γ`-factor
geometry, the EF-identity guard-rail), `06-papers/P25,P26,P27,P28` (the chain this refines).
*Memory:* `[[project-rh-current-direction]]`, `[[riemann-key-contradiction]]`.
