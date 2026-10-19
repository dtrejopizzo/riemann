# R148.005 — Closing decision, phase 148: mixed effectivity on the full square

(round 1 + Corrections of record), `R148_002` (audit: ACCEPT WITH REPAIRS), `R148_003` (round 2,
document of record), `R148_004` (confirmation: ACCEPT; three cosmetic residues applied in a note appended to
`R148_003`). This decision is unconditional.*

## 1. The idea and its fate
**Idea (after R147_005).** The missing `+` of row D must not commute with the radial projection.
Enlarge the frame from radial classes (translation kernels `Φ(y/x)` on `C_Q × C_Q`) to kernels on the
full square, add rank-one kernels `φ⊗ψ` as generators of the effective cone, and use **mixed effectivity**
`Φ(y/x) − φ(x)ψ(y) ≥ 0` — a new *constraint*, not new data — to obtain inequalities on the zero data of
`Φ` that the radial sector alone cannot give. Corpus check: rank-one generators and the mixed condition
were NEW; the extension to the square had been named (phases 113, 136, 146) and never built.

**Fate: REFUTED, by a two-line theorem.** Mixed effectivity is the tropical condition
`Φ ≥ φ ⊛ ψ`, `(φ ⊛ ψ)(w) = sup_u φ(u)ψ(u+w)` (max-plus correlation) — correctly predicted. But for
nonnegative factors the right side is a supremum of nonnegative numbers, so **`Φ ≥ φ ⊛ ψ ⟹ Φ ≥ 0`**, with
no decay hypothesis whatsoever (D.56.3′). For signed factors a single `w` with `(φ ⊛ ψ)(w) < 0` forces
`|φ(u)ψ(u+w)| ≥ ε` for every `u`, so the cross pairing `χ_{φ,ψ}(w) = ∫φ(u)ψ(u+w)du` is infinite and the
(T)×(R) block does not exist (D.56.3′, 3‴). The same holds for the opposite quadrant `k_Φ + φ⊗ψ ≥ 0`
(D.56.4′) and at every finite rank (D.56.4″). Hence the translation shadow of the mixed cone is exactly the
frame's effective cone `𝓔` (Theorem D.56.4), the support-function constant at `ρ₁` is `s₁ = 0.99846016…`
unchanged, and the relaxed clause `(b′)⁺_X` is equivalent to `(b′)⁺` and dies at the same witness
`tF₀ + dK`. `PROVED`. No FATAL flag. `Ξ_a`-uniform (no step uses equimodularity).

## 2. What the phase established beyond the refutation
* **The form `B` on `(T) ⊕ (R)` exists** (directness `(T) ∩ (R) = 0`; three blocks by two inequivalent
  prescriptions, regularized on (T)×(T), honest traces elsewhere — D.55.5′), but **has no common radial
  representation** (D.55.6′: `B(·,k_Φ)` is represented by the Weil density `w_Φ` on (T) and by `Φ` on
  (R); at `Φ = 2K`, `w_{2K} = 2cosh(w/2)` grows while `2K` decays), **no radial projection and no
  degree** on the square (D.55.7′), and the passage from (R) to (T) by diagonal averaging is not a
  limit of `B` (D.55.8′). `PROVED`.
* **The (T)×(R) block is zero-blind**: `⟨Frob_n, φ⊗ψ⟩ = χ_{φ,ψ}(log n)` is the first finite, nonnegative
  Frobenius pairing in row D — and contains no zero, pole or Euler factor. It is a count that sees the
  radial variable and nothing arithmetic. `PROVED`.
* **Corpus repair**: phase-41 Doc 125 (`phase-41-build-G2/125-construction-of-the-intersection-form.md`),
  reported missing in `CORPUS_CHECK_R145`, is located and is the same object one level up: its flow
  correspondences are (T) unsmeared, and its `f₁·f₂ = 1` is a finite nonzero **integer** intersection
  number on classes `B` cannot pair. Consequence of record: **phase 148 proved its form trivial on its
  domain, not that the square admits no intersection theory.** Doc 125's own obstructions (real rather
  than integer numbers on the continuous flow; Babaee–Huh non-persistence of the signature at infinite
  rank; NC3 circularity) bound the prize from the other side.

## 3. Reading of record
The phase tested the stated goal at its sharpest: create a `+` that the mathematics seems to forbid.
The `+` of kernels on the square exists trivially; what does not exist is an effectivity constraint
coupling the rank-one sector to the zero data. The mechanism is the same as in phases 146–147, one level
up: **everything the new sector contributes is either nonnegative by construction (hence a restatement of
`Φ ≥ 0`) or infinite (hence outside the form).** The tropical structure enters row D for the first time,
and enters vacuously. P122.028's bar ("no new arithmetic data beyond `log p, p^{−½}, N, Γ`") now has a
companion: **a new constraint of positivity type on the square constrains nothing new.**

## 4. Open (principal residue) and closed
* **O-148.2 (principal)** — a kernel class `𝒦′ ⊇ (T)` with a form `B′` restricting to `I_∞` on (T),
  pairing Doc 125's `f₁, f₂` finitely and nonzero, `T_a`-invariant, with an unambiguous degree. Doc 125
  answers it on compact `C_p × C_p`; on `C_Q × C_Q` `f₁` has infinite measure and the answer does not
  transfer. This is the exact shape of "intersection theory on the square with a degree", and it is
  where CC's "delicate principal values" live (ANALOGY, not imported).
* O-148.1, O-148.4, O-148.5 minor; O-148.3 CLOSED (D.56.4′). Carried: O-47.7, O-47.8, O-47.1′, O-47.3′.

## 5. Decision
Phase 148 **closed, negative, by theorem** (D.56.4′ plus Doc 125's obstructions). Row D: no label, no
sign. The original idea is refuted; the refutation is elementary and should have been seen at blueprint time
— recorded as an error (`φ ⊛ ψ ≥ 0` for nonnegative factors is immediate).

**Where the search now stands.** Four independent mechanisms close four independent enlargements:
no ring on `Spec Z` (146); Galois ring invisible on the radial carrier (147.1); graded carrier acts away
from `ζ`'s zeros (147.3); positivity-type constraints on the full square are vacuous or infinite (148).
The common statement: **the zero data of `ζ` enters the frame only through the regularized trace on the
radial sector, and every object whose degree is a genuine count is either supported there (and then it is
`Φ ≥ 0`) or pairs with it infinitely.** A new idea for D must break *that* statement: it needs an object
with a finite count-degree that pairs finitely with translations **and** carries zero data — i.e. a
regularization of the trace on the square that is not the radial one (O-148.2). That is the single
question left by phases 145–148, and it is the question Connes–Consani left open on the scaling site.
