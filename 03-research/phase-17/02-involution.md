# SURF-A Step 2 — The real-locus involution

**Phase 17, step 2.** Supports: `00-SURF-2.0-design.md` §A.2; follows `01-SURF-A-triage.md`.
**Experiment:** `experiments/surfA_involution_orbits.py` (runs clean, verifies I1–I3).
**Date:** 2026-06-06.

> **Goal (per the triage):** turn the numerical observation `b ↔ distance to a fixed locus`
> into a precise, geometry-ready statement, by naming the involution whose fixed locus is the
> critical line. Start from the **symmetries**, not from cycles. No Arakelov metric is assumed.

---

## 0. Setup: two involutions and the group they generate

On the `s`-plane define
```
  σ(s) = s̄        (complex conjugation)
  ι(s) = 1 − s     (functional-equation symmetry, ξ(s)=ξ(1−s))
```
Both are involutions and they commute (`σι = ισ`), so they generate the **Klein four-group**
```
  V = ⟨σ, ι⟩ = { id, σ, ι, j },   with   j := σι : s ↦ 1 − s̄.
```
The zero set of `ξ` is invariant under `V` (functional equation + real coefficients).

---

## 1. I1 — Which involution fixes the critical line? (an honest correction)

A natural first guess is that the functional equation `ι` fixes the critical line. **It does
not.** Algebraically `ι(s)=s ⟺ 1−s=s ⟺ s=½`: a single point. Likewise `σ` fixes the real
axis `{Im s = 0}`. The involution whose fixed locus is the **whole** critical line is the
composite `j`:

> **Proposition I1.** Let `j(s)=1−s̄`. Then `j` is an **anti-holomorphic involution**
> (`j²=id`, `j` reverses orientation), and
> `Fix(j) = { s : 1−s̄ = s } = { s : Re s = ½ }` = the critical line. Moreover
> `Fix(ι) = {½}` (a point) and `Fix(σ) = {Im s = 0}` (the real axis), so among the three
> nontrivial elements of `V`, **only `j` fixes the critical line**.

*Proof.* `j²(s) = 1 − \overline{1−s̄} = 1 − (1−s) = s`. `j` is anti-holomorphic since it
involves `s̄`. `1−s̄=s ⟺ s+s̄=1 ⟺ 2 Re s = 1`. The statements for `ι, σ` are immediate. ∎
(Verified: `surfA_involution_orbits.py`, block I1.)

**Why this is the right object, not a technicality.** An *anti-holomorphic* involution is
exactly a **real structure** on a complex variety; its fixed locus is the set of *real points*.
So the critical line is naturally the **real locus of the real structure `j`** — precisely the
kind of "diagonal / real subvariety" SURF-A needs, and a *better* fit than the holomorphic
`ι` (which has no fixed curve). The triage's intuition ("critical line = fixed locus of an
involution") is correct; the involution is the anti-holomorphic reflection `j = σι`, not the
functional equation alone.

---

## 2. I2 — Off-line zeros are free `V`-orbits; on-line zeros sit on `Fix(j)`

> **Proposition I2.** Write `ρ = ½ + b + iγ`, `b = β − ½`. The `V`-orbit of `ρ` is
> ```
>   { ½ ± b ± iγ } = { ρ, σρ=ρ̄, ιρ=1−ρ, jρ=1−ρ̄ }.
> ```
> If `b ≠ 0` and `γ ≠ 0` the orbit is **free** (size 4, stabilizer `{id}`): this is the
> **off-line quartet**. If `b = 0` (on the critical line) the stabilizer is `{id, j}` and the
> orbit **degenerates to the pair** `{½ ± iγ}` (size 2). [And on the real axis `γ=0` the
> stabilizer is `{id, σ}`.]

*Proof.* Direct computation of `σρ, ιρ, jρ`; the four points coincide in pairs iff `b=0` or
`γ=0`. For `b=0`: `jρ = 1−\overline{½+iγ} = ½+iγ = ρ`, so `j` stabilizes, and `σρ=ιρ=½−iγ`. ∎
(Verified: block I2 — off-line `|orbit|=4`, stabilizer `{id}`; on-line `|orbit|=2`, stabilizer
`{id, j}`.)

**The structural payoff (links I2 to the signature law A.2).** The quartet degenerates to a
pair **exactly on `Fix(j)`** — which is exactly where the experiment's bilinear block
degenerated from `(1,1)` to `(1,0)`. The orbit degeneration *is* the signature degeneration:
on-line zeros are the `j`-fixed (real) points, and their block loses its negative direction
because the real structure collapses the two transverse directions into one.

---

## 3. I3 — `b = β − ½` is the coordinate transverse to the fixed locus

Center the plane: `ζ := s − ½`, so the critical line is `{Re ζ = 0}` (the imaginary `ζ`-axis).

> **Proposition I3.** In the centered coordinate, the generators act by
> ```
>   σ : ζ ↦ ζ̄        (b,γ) ↦ ( b, −γ)
>   ι : ζ ↦ −ζ        (b,γ) ↦ (−b, −γ)
>   j : ζ ↦ −ζ̄        (b,γ) ↦ (−b,  γ)
> ```
> where `ζ = b + iγ`, `b = Re ζ = β − ½`, `γ = Im ζ`. Thus **`j` acts as `b ↦ −b`, fixing `γ`**:
> it is the reflection in the transverse coordinate. `Fix(j) = {b = 0}` is the critical line,
> and `b = Re(s − ½)` is the natural coordinate **transverse** to it, exchanged by `j`.

*Proof.* Substitute `s = ½ + ζ` into `σ, ι, j` and read off the real/imaginary parts. ∎
(Verified: block I3 — `j: (b,γ) ↦ (−b, γ)`.)

**Conservative working hypothesis (what we are entitled to claim).**
```
  (WH)  b = Re(s − ½) is the algebraic coordinate transverse to Fix(j),
        on which the real structure j acts by sign reversal b ↦ −b.
```
We do **not** yet claim `b` is an Arakelov/metric *distance* to the real locus: no surface, no
metric, no intersection theory exists yet. (WH) is exactly what the symmetries support, and it
is the precise replacement for the heuristic "`b` = distance to `Δ`."

---

## 4. The signature, read through the real structure

The off-axis evaluation produces `w = f̂(γ−ib) = u + iv`, and the off-line block is the split
form `4 Re(w²) = 4(u² − v²)` (P25/P26). This is exactly the shape a **real structure** forces:
an anti-holomorphic involution acting on the value `w` by `w ↦ w̄` has `±1` eigenspaces
`{w real}` and `{w imaginary}`, and the `j`-invariant quadratic form `Re(w²) = u² − v²` is the
**split (1,1) form diagonalized by those eigenspaces**. On `Fix(j)` (`b=0`) the imaginary part
`v → 0`, the `−1` eigenspace disappears, and the form degenerates to `u²` of signature `(1,0)`.

So the experimental signature law of step 1 is the **shadow of the real structure `j`**:
- `(1,1)` off-line = the split form of an anti-holomorphic involution in transverse position;
- `(1,0)` on-line = its degeneration on the fixed (real) locus;
- the negative direction's growth with `b` = moving off the real locus along the transverse
  coordinate `j` reverses.

This is the clean geometric formalization of A.2 the triage asked for — and it is **forced by
the symmetries alone**, before any surface is built.

---

## 5. What this sets up for Route 2 and SURF-B

### 5.1 The sharpened F-indep exam (Route 2 testbed)
We now have the data a candidate must use *and* the data it must **not** use:

> **A-pass requires:** construct cycles `Z_ρ` from the pair `(X, j)` — a variety with an
> anti-holomorphic involution (real structure) whose real locus models the critical line —
> such that
> 1. the `Z_ρ` are a single `V`-orbit (quartet off the real locus, pair on it: I2),
> 2. their bilinear self-pairing is the split `(1,1)`/`(1,0)` block (step 1, §4),
> 3. **`b` enters only as the transverse coordinate to `Fix(j)` (WH)** — *not* as an externally
>    supplied label `γ_ρ`.
>
> **A-fail (named danger):** if the only way to define `Z_ρ` is `Z_ρ := (cycle tagged by γ_ρ)`,
> then the construction imports the spectrum and is circular (G-INDEP). The whole point of I1–I3
> is that `Z_ρ` should be *located by its position relative to `Fix(j)`*, with `(b, γ)` read off
> the geometry, never fed in.

### 5.2 The handoff to SURF-B (resolvent)
SURF-B will seek a geometric operator `T` whose resolvent realizes the de Branges (dB2)
difference quotient. I1–I3 constrain it: `T` should be **compatible with the same real
structure `j`** — concretely, the divided-difference / shift along the transverse coordinate
`b`, intertwined with `j` by `b ↦ −b`. The functional equation (`ι`) and conjugation (`σ`) then
appear as the `±` symmetries of the resolvent. This is the thread step 3 will pull.

---

## 6. Findings (durable)

1. **The real-locus involution is named and is `j(s) = 1 − s̄`** — the anti-holomorphic
   reflection across `Re = ½`, i.e. a **real structure**; the critical line is its real locus
   (I1). *Correction:* it is **not** `ι(s)=1−s` (which fixes only the point `½`).
2. **Off-line zeros = free Klein-four orbits (quartets); on-line zeros lie on `Fix(j)`**, where
   the orbit degenerates to a pair (I2) — the same place the `(1,1)` block degenerates to
   `(1,0)`.
3. **`b = Re(s−½)` is the transverse coordinate to `Fix(j)`, reversed by `j`** (I3); the split
   signature `u²−v²` is the real structure's invariant form (§4). This formalizes A.2 from the
   symmetries alone.
4. **Conservative stance:** `b` is the algebraic transverse coordinate (WH); identifying it with
   an Arakelov *distance* is deferred to when a metric/surface exists.
5. **The F-indep exam is now sharp:** locate `Z_ρ` by position relative to `Fix(j)`, with
   `(b,γ)` read off `(X, j)`, never importing `γ_ρ`.

## 7. Next

- **Step 3 (Route-2 finite testbed / SURF-B probe).** Build the smallest model `(X, j)` — a real
  structure with the right orbit combinatorics — and test §5.1: define `Z_ρ` F-independently and
  check it reproduces the step-1 template; then probe whether a `j`-compatible shift along `b`
  gives a (dB2)-type resolvent identity. → `03-route2-testbed.md`.
- **Literature pin:** Connes–Consani real structure / the scaling site; the role of the
  archimedean place as the real place (for `Fix(j) ↔` critical line). Read before building.

---

*Cross-refs:* `01-SURF-A-triage.md` (target template, routes), `00-SURF-2.0-design.md` (§A.2),
`experiments/surfA_involution_orbits.py`, `../06-papers/P25,P26` (the split form `u²−v²`).
*Memory:* `[[project-rh-current-direction]]`.
