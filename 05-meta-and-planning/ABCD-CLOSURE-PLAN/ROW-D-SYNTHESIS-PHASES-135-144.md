# Row D — lead synthesis after phases 135–144 (2026-09-13) and the decision point

## 1. What was built (all hostile-audited; labels as recorded)
* The frame: Weil class `D^W`, canonical class `K` (Pólya kernel, `Φ_K = ξ`, `K > 0`), degree, affine
  duality `σ_K`, spectral bound Thm 11.14 with its exact constant (support function of the effective cone);
  splitting `D^W = Λ ⊥ P^W` with explicit `K_odd`; field-uniform version (`K_K` by contour shift; base
  change additive over conjugate packets); `Frob_𝔫` and `Sh_{O_K}` for every number field.
* Detection: triangles detect every off-line zero (Landau criterion `RH ⟺ W(h_T) ≥ 0 ∀T`); effective cone
  and `C_c^∞` are detecting; Frobenius traces determine classes mod the radical (`ker T = 𝓝_∞`).
* Method theorems: T1 (no local structure separates `ξ` from `ζ_K` ⟹ any proof is field-uniform); T2
  (Epstein `Ξ_Q`: equimodular polar block + positivity + functional equation are insufficient ⟹ any proof
  uses the Euler product); the `ζ_K` gap for rank-one polar arguments; the phase-65 chain's fork.
* Riemann–Roch-defined `h⁰_RR⁺` with (a),(c) unconditional and the exact growth `¼m²`; `χ ≤ 0` forced.
* **Frame defect theorem** (given `ρ₁` simple, on the line): no `h⁰` satisfies (a),(b′),(c) of Thm 12.3
  for `ξ` — the effective cone is a thin moment cone (`s₁ = 0.99846 < 1`); the frame keeps the
  intersection theory of `C×C` and discards its linear systems.
* **Trace-cone transfer theorem 12.3-B4**, unconditional; `(b′)_{B4}` true under RH; hence
  **RH ⟺ `I_∞(E, g_λ) ≥ 0` on `S_0 = {deg E > 0, ½I_∞(E,E) > ¼deg E}`** — the shortest form row D has.

## 2. What was proved impossible on this page
One family, `tF + dK` (`F` primitive with `I_∞(F,F) > 0` if RH fails; `d = 1` in phases 143–144, `d = 400`
and the cousin `E_0 + tF` in phases 140–142), has frozen frame invariants `(a,b,deg,R) = (d/2,d/2,d,·)` with
`R > 0`, and refutes: every bidegree-function `h⁰`; every 2-homogeneous trace
functional; the effective clause `(b′)⁺`; every fixed-index trace inequality; the sparse cone; the
head/tail stratification; bounded density on `S_0`; any large-constant hope; O-30. The frame cannot see
that `W` is a norm (`|n^{½−ρ}| = 1`, `W ≥ 0`) — those are zero-location facts. `Ξ_a` satisfies every frame
statement tested; the only parting point is "a primitive `F` with `I_∞(F,F) > 0`", a theorem for `Ξ_a`
and literally `¬RH` for `ξ`.

**Conclusion of record.** The Riemann–Roch / Hodge-index frame of rows A–D produces restatements of RH,
not reductions. The sign must come from a structure outside it.

## 3. What "outside" can mean, checked against the corpus map (phase 136) and T1/T2
Any candidate must: use the Euler product essentially (T2), be uniform in the number field (T1), fail for
`Ξ_a` at a named line, and not be a magnitude method (cluster D) nor a finite window (cluster B) nor a
Hilbert–Pólya/KMS realization (MW-4, Thm 161.9).
* **(α) Change the coefficient of the form, not the cone.** All of 135–144 kept `I_∞` fixed and varied
  `h⁰`/the cone. The alternative is a *different pairing* `J` on the same carrier with **`J ≥ I_∞` on `P^W` and
  `J ≤ 0` provable there** (since RH is `I_∞(F,F) ≤ 0` on primitives, a form that is *positive* and
  dominates `I_∞` proves nothing — sign fixed after R144_004). T2 says it must be built from the Frobenius
  family's multiplicativity; the corpus's only unconditional positivities are prime-only (Docs 131/135)
  and archimedean-only (CC). The meta-theorem of phase 136 says the sign is their *coupling*. Nothing in
  the corpus has attempted a pairing `I_∞^{(coupled)} := I_∞^{prime} + I_∞^{arch}` with a *cross term*
  built from `Frob_n ⋆ Frob_n^† = Δ^{(n)}` — this is the one untried square adjacent to what is proved.
* **(β) Function-field model of `D^W`** (O-23): build the analogue of the whole frame for a curve over
  `F_q` and check whether *there* the frame defect theorem holds too. If it does, the defect is in the
  frame, and its geometric repair (linear systems) can be transcribed; if it does not, the arithmetic
  frame is missing a specific geometric ingredient, identifiable by comparison. Predicted answer (R144_004): on a curve Riemann–Roch is a theorem, so the frame defect theorem will
  **fail** there; the value of β is therefore not the yes/no but that the comparison **names** the missing
  ingredient (a sections functor; a cone that is not a thin moment cone — `s₁ < 1` is the numerical
  signature of its absence). β is to be judged only on whether it names that ingredient, and α cannot be
  scoped before it does.
* **(γ) Horn A / (T2)-type cones** (O-19′, O-18′, O-26): inside the frame; the auditor keeps them as the
  only defensible frame-internal continuations, but §2 argues they will meet the same ray.

## 4. Recommendation
Close the trace-cone route with Restatement D.38.3a as its final form. Open phase 145 on **(β)**: the
function-field model of the frame, with the frame defect theorem as the test. Reason: it is the only
proposal whose outcome is decidable in one phase and informative either way, and it would tell us
*which* geometric ingredient the arithmetic frame lacks before we try to build (α). Then (α) in phase 146
with that ingredient named. Owner decides.
