# R134.003 — Lead audit of round 1 (Paper 46, row D opening)

Author: session lead (Fable 5.1). Date: 2026-09-12. Independent of the hostile
audit R134.002 (in progress when written).

## 1. Re-derived and found correct

| statement | check |
|---|---|
| Lemma 3.1 | `u = e^{−\|t\|/2}∗F`; right of `supp F`: `u = e^{−t/2}Φ_F(1)`; left: `e^{t/2}Φ_F(0)`; the two Tate conditions are exactly compact support ✓. A clean converse to Paper 45 Cor 10.2 |
| Thm 3.4 and the refutation of the blueprint's `\|ρ(1−ρ)\|²` | correct; the lead's display presupposed the line. Accepted as `REFUTED`; Rem 3.5 states the trap exactly |
| Thm 3.6 | from Paper 45 (9.6): `Σ_ρΦ_h(ρ) = ⟨h,ϖ⟩ − ⟨h,W_fin+ω_∞⟩` ✓; `(Πg)⋆(Πg)^† = Π²h` by Mellin symbols ✓; self-adjointness ✓. Note (to add): `Πe^{±t/2} = 0`, so `Π²ϖ = 0` as a distribution — the polar summand of `𝔏` is annihilated by `Π²`; this is *why* the polar packet drops on the primitive sector and it should be said in one line |
| Thm 3.7 | (a)⇒(b) uses `Φ_g(1−ρ) = \overline{Φ_g(ρ)}` on the line only ✓; (b)⇒(a) by Lemma 3.1 + Paper 45 Thm 10.4 ✓; Bochner–Schwartz needs temperedness of `𝔏` ✓ (stated); `μ = Σ_γ(¼+γ²)²δ_γ` tempered by `N(T)=O(T\log T)` ✓ |
| Rem 3.9 | `λ_±` are characters of the convolution algebra, so the primitive classes form an ideal, not a unital subalgebra; GNS does not apply directly — correct and the right honesty. The builder's repair of the lead's "partial isometry" attribution is right |
| Thm 4.2 | (4.1): `8T\sinh T`, `4T²+4\sinh²T`, `\det = −16(T²−\sinh²T)² < 0` ✓; the Tate block is polar part + `⟨𝒜_Tφ,φ⟩` (P124.013 (2.3)) ✓; the lead's blueprint conflated three two-dimensional objects — `REFUTED`, accepted |
| Thm 4.3, Cor 4.4 | `R`-invariance term by term; `X_Tσ = UX_T`; `σΣσ = Σ` ✓; even/odd split ✓; Rem 4.5's honesty ("reduction of shape, not progress") ✓ |
| Thm 5.8 | diagonal `(1/ε)[−\log(1/ε)‖φ_1‖² + O(1)]` (Paper 44 8bis.2 with its `‖φ‖²/ε`); off-diagonal atoms `c_φw/ε + O(1)`; Gershgorin ⇒ negative definite for `ε < ε_1(N)`, unconditionally, for both models ✓. This is the important deflation: finite inertia at small `ε` is uninformative, and the naive Dirichlet-delta limit does not exist |
| §9.3 finding 2 | Galerkin on a subspace: computed `λ_min ≥` true infimum ✓; a positive computed value certifies nothing — correct, and correctly scoped away from the interval-arithmetic endpoint certificate |
| §10 | no label, no sign ✓ |

## 2. Findings

**LF1 (MINOR).** State `Π²ϖ = 0` explicitly in Thm 3.6 (one line), and then
write `𝔏 = −Π²(W_fin+ω_∞)` as the equivalent form; keep `ϖ` in (3.2) only if
the paper wants to display where the polar packet went.

**LF2 (MINOR, grading).** Thm 3.7 is an equivalence whose every link is either
classical (Weil, Bochner–Schwartz, SNAG, GNS) or a citation; the new content is
Lemma 3.1 and Thm 3.6. Grade Thm 3.7 `RESTATEMENT (CLASSICAL + PROVED-IN-
REPOSITORY)` and keep Rem 3.8's ledger; the builder's own press point is
right.

**LF3 (NOTE).** §9.3's corpus findings are consequential for phase 124 and
must be recorded there (a one-paragraph `[phase 134]` note in P124.013 after
Cor 3.3 and in P124.014 §3, with the refinement table), without altering the
qualitative conclusions those notes keep.

## 3. Interim ruling

Round 1 does what the blueprint asked and nothing it forbade: a reformulation
with a named missing object, one structural law (the swap law), one honest
deflation (Thm 5.8), five negatives, a falsifier suite tied to Paper 44
Thm 3ter.6, six blueprint refutations (all accepted by the lead), and three
findings against the corpus. No sign, no label. Pending: R134.002, then one
repair round.

## Addendum (after R134.005) — an error of the lead's own

In the lead's round-2 grep pass (not in this file, but on the record of the
session) the lead read Proposition 3.6a(iii) — "`Π²W_fin ∉ S'(R)`" — and
accepted its proof. That acceptance was **wrong**: the proof transposes `Π²`
across a pairing with a Schwartz, non-compactly-supported test, which
presupposes the temperedness it denies, and it discards the cancellation
`Π²ϖ = 0`; under RH the residual `W_fin − ϖ` is the derivative of an `O(t³)`
function and `Π²W_fin` **is** tempered. The hostile auditor (R134.005) caught
it, together with the consequence that 3.6a(iii) + Thm 3.7 would prove `¬RH`
inside the paper. Withdrawn in round 3 (erratum E1). Recorded here so that the
lead's audit trail carries its own mistake.
