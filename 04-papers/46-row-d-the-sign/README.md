# Paper 46 — Row D: the sign

**David Alejandro Trejo Pizzo, with Claude (Opus 5).**  2026-09-12.

**Status: `SKELETON AND FIRST THEOREMS`, round 3 — final state of the opening
campaign (`R134_002` M1–M7 and minors, `R134_003` LF1–LF3, and `R134_005`'s
bounded erratum E1–E5, all carried out).  `ROW D: NO LABEL CLAIMED, NONE
EXPECTED FROM THIS CAMPAIGN.`  No sign is claimed, asserted or suggested.**

**Route status:** D.1 is graded `RESTATEMENT`; **D.3 is retired as a programme
item**, with Theorem 5.8 kept as its result; D.2, D.4 and D.5 stand as
described below.  One round-2 repair was withdrawn in round 3 (§9.2b): it was
not proved, it is false under RH, and it would have put a statement about the
zeros inside the paper.

---

## What this paper is

The opening campaign of row D, the last of the four rows of the Weil-strength
programme.  Rows A, B and C are closed on the declared carrier (Papers 43, 44,
45).  They hand row D a target that is not a metaphor:

> `I_∂ ≤ 0` on every primitive radial class `Γ_g`, `g ∈ C_c^∞(R)`, on the
> colimit `D_A^∞` with `T_∞` and `c = 0`; this implies RH by Paper 45
> Theorem 9.6 (9.10) and Theorem 10.4.

and three standing negatives that say which shapes a proof cannot have
(Paper 43 Theorem 14.1; Paper 44 Theorems 8bis.4a and 8bis.7; P124.014).

This paper does **not** prove the target and does not claim to be closer to
it.  It establishes the first theorems of the row, with honest labels, and it
records what it refuted.

## The five results

* **D.1 (§3) — the state reformulation.  Graded `RESTATEMENT`.**  Row D's
  target is equivalent to: *the explicit distribution
  `𝔏 = −Π²(W_{fin}+ω_∞) ∈ D'(R)` on the modulus group of the carrier is
  positive-definite* — equivalently, by Bochner–Schwartz **in its `D'` form**
  and SNAG, *there is a unitary representation of that group in which the
  target functional is a squared norm*.  This names and types the "nonnegative
  invariant" the phase-133 panel identified as missing: it is a **norm**, not
  a dimension.  Two small new theorems live inside it and are the only new
  content: `Π = −∂_t²+¼` is a **bijection** onto the primitive class
  (Lemma 3.1) — the two Tate conditions are exactly what makes
  `e^{−|t|/2} ∗ F` compactly supported — and Theorem 3.6, which identifies
  `𝔏` and observes `Πϖ = 0`, so the polar packet is annihilated
  *identically*.  Proposition 3.6a proves that `ϖ` and `W_{fin}` are **not
  tempered**, which is why the `D'` form of Bochner–Schwartz is the one that
  applies; and Remark 3.6b records that nothing may be concluded about `𝔏`
  itself, since `Π²` annihilates exactly the growth involved and RH *implies*
  temperedness — a round-2 claim to the contrary is withdrawn in §9.2b.  **No proof in the paper uses the identification of the group
  with the carrier's modulus group beyond naming** — which is why §3 is a
  restatement and is graded as one.  Constructing the Hilbert space **is** row
  D and is not done here.
* **D.2 (§4) — the dichotomy, and a swap law.**  P124.013's shielding
  dichotomy is restated on the true carrier with its hypothesis carried
  (`T_q < ∞`, which for `ζ` is the negation of the target — so the dichotomy
  has no content for `ζ` unless the target fails).  New: the reflection
  `t ↦ −t` forces `Σ(T)` to be a symmetric **Toeplitz** `2×2`, so the
  surviving constraint-free target `Σ(T) ≥ 0` splits into the two scalar
  inequalities `α ± β ≥ 0` along the even/odd decomposition.  Monotonicity in
  `T` is proved **not** to be available.
* **D.3 (§5) — finite inertia.**  The Gram entries are defined, at every
  `ε`, by Paper 45 **Lemma 5.1a** (no support hypothesis); Paper 44
  Theorem 8bis.1e is cited only for their *interpretation* as a Frobenius Gram
  form, in the regime `ε = O(1/N)`, which **no** reported computation
  satisfies.  The primitive constraint on the smeared Frobenius family is
  exactly `Σc_n n^{±1/2} = 0`, independent of the smearing.  The `ε → 0` asymptotics are computed: the archimedean diagonal
  diverges like `−(c_φ/ε)\log(1/ε)` — Paper 44 Theorem 8bis.2, the infinite
  genus — **one logarithm faster** than every prime atom, so below an explicit
  `ε_1(N)` the whole Gram matrix is **negative definite unconditionally**, for
  `ζ` and for the falsifier alike.  Finite inertia is therefore evidence of
  nothing at small `ε`; the separation observed numerically lives in a window
  of `ε` of order one, which is exactly where the concentrated Frobenius
  reading of the kernel is invalid.
* **D.4 (§6) — what the invariant cannot be.**  Five theorems with
  counterexamples, plus an explicit requirement list (R1)–(R5) any candidate
  must meet — and a sixth, structural negative added in round 3: the list is
  **vacuous** for any duality preserving primitivity, since (R3)+(R4) would
  force `I_∞` constant on the primitive sector; and `†`, the only duality rows
  A–C construct, does preserve it.  **The obstruction is not the choice of `h`
  but the absence of a `K`-twist**, which is now a named `NOT CONSTRUCTED`
  requirement.
* **D.5 (§7) — the falsifier suite.**  `Ξ_a = ξ(s+a)ξ(s−a)` fails a
  **pre-comparison** axiom of row B, identified by theorem number: its local
  contacts are not shell volumes, so its would-be Frobenius satisfies
  `F_n ⋆ F_n^† = (n^a+n^{−a})Δ^{(n)}` and is **not a partial isometry**
  (against Paper 44 Theorem 3ter.6).  Davenport–Heilbronn has no Frobenius
  family and no Tate block at all.

## What was refuted

Nine blueprint claims were refuted or repaired; full table in §9.2, and the
round-2 repair ledger is §9.2a.  The two that matter most:

* `Λ(g) = Σ_ρ |ρ(1−ρ)|² Φ_g(ρ)Φ_g(1−ρ)` is **false**: the correct factor is
  `[ρ(1−ρ)]²` (Paper 45 Lemma 10.3a), and the two agree exactly on the
  critical line — **writing `|·|²` assumes RH**.
* "the inertia is indefinite for large `N`, by Theorem 14.1 transported" is
  **false**: under `(C1)` the conclusion would contradict row D's target
  (Theorem 5.5), and under the chart reading the kernel formula leaves its own
  window.  *(Round 1 offered a second refutation via the unavailability of
  14.1's mechanism; its key step was unproved and is downgraded to
  Remark 5.4, with the colimit question marked `OPEN`.)*

Three findings against the corpus are recorded in §9.3 and, after round 2,
in phase 124 and phase 118 themselves.  The sharpest — **confirmed by
independent re-run** — is that the phase-118/124 Galerkin eigenvalues are
**variational upper bounds**, so a negative computed eigenvalue certifies a
real negative direction while a positive one certifies nothing; this makes the
`ζ` "control" of P124.014 incapable of supporting a conclusion about `ζ`, and
makes its printed first-contact brackets for `Ξ_a` resolution-unstable.  It
also governs **this paper's own §4 numerics**, which now carry Warning 4.5a.
The third finding of round 1 — that P124.013 Corollary 3.3 is
"basis-dependent" — was **partially refuted on audit and is withdrawn**: at a
finite `T_*` the criterion is invariant; only the *value* `λ_{\min}Σ` is not.

## Files

| file | content |
|---|---|
| `main.md` | the paper: §0 target and negatives, §1 conventions by number, §2 the D-H/D-E contract and the P122 acceptance test, §3 D.1, §4 D.2, §5 D.3, §6 D.4, §7 D.5, §8 external inputs with the clause each serves, §9 what is open, §10 no label, §11 reproduction |
| `../../03-research/phase-134-row-d-opening/scripts/d134_gram.py` | Gram inertia of the smeared unit-averaged Frobenius family on the primitive subspace, for `ζ` and for `Ξ_a`, at several `N` and `ε` |
| `../../03-research/phase-134-row-d-opening/scripts/d134_sigma.py` | the Schur complement `Σ(T)` in the named border basis, reusing phase-124's `p124_lab.py`: swap law, the Tate **block** `𝔅_T` (not the ruling plane `B_T`), monotonicity |
| `../../03-research/phase-134-row-d-opening/R134_001_BUILDER_ROUND1.md` | builder's round-1 report: what was built, every refutation with its counterexample, four places to press |
| `../../03-research/phase-134-row-d-opening/R134_002_AUDIT_ROUND1.md` | hostile audit of round 1: M1–M7 and minors; no no-sign violation found |
| `../../03-research/phase-134-row-d-opening/R134_003_LEAD_AUDIT_ROUND1.md` | lead audit of round 1: LF1–LF3 |
| `../../03-research/phase-134-row-d-opening/R134_004_BUILDER_ROUND2.md` | builder's round-2 report: every audit item, with grep/script evidence |
| `../../03-research/phase-134-row-d-opening/R134_005_AUDIT_ROUND2.md` | hostile audit of round 2: `(F1)` `FATAL`, `(R2-1)` `MAJOR`, minors `(r1)`–`(r6)` |
| `../../03-research/phase-134-row-d-opening/R134_006_BUILDER_ROUND3.md` | builder's round-3 report: the bounded erratum, with evidence and the running count of refuted claims |

## Rules this paper is written under

Labels as in Papers 43–45; the hypothesis-carrying rule; convention `(C1)`
wherever all primes occur; `c = 0` as a theorem of row C, not a convention;
every classical import named in §8 with the clause it serves; **no statement
about the location of zeros outside the comparison theorem and D.1's
classical equivalence**; no relabelling; **numerics illustrate and falsify,
they prove nothing**; and **no sign is claimed.**
