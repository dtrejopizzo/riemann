# D128.002 — row B audit: findings and dispositions

Date: 2026-09-12.  Target: Paper 44.

## Accepted (verified)

**B1. Theorem 8.1(iii) contains a backwards inference, and its conclusion is
false.**  The paper argues: "if `Λ(n)` were a function of the ruling data it
would be a function of `n`, hence determined by `log n`, but `Λ(4)=Λ(8)` with
`log 4 ≠ log 8` shows the level sets differ."  This is invalid: `n ↦ log n` is
**injective**, so anything that is a function of `n` **is** determined by
`log n`; a function need not be injective.  The truth is the opposite — the
ruling pairing depends on `|a_S(n)|_S = 1/n`, which determines `n`, which
determines `Λ(n)`.  **So `Γ_n` IS separated by the ruling plane and the appeal
to the mixed sector is unsupported.**  `ACCEPTED — a genuine mathematical
error of mine.`  §7 check 5 repeats it and is likewise false.

**B2. Theorem 6.1(iii) is a definitional identity, not the missing arrow.**
`w_ram = |a_S(n)|_S^{1/2}` and `[L_S:nL_S] = |a_S(n)|_S^{−1}` is the definition
of the module of the automorphism, which P123.038 §4 already states.  Worse,
the quotation of P123.038 §5 was truncated: the full demand is that the
lattice-index operation be realized as the diagonal shadow "**extended
cyclically to mixed correspondences and compared with the analytic nuclear
trace**", and P123.039 §5 warns "A collection of equal trace values is
insufficient for those functorial claims".  Neither is supplied.  `ACCEPTED`;
both open items are restored.

**B3. Clause B.4 is not discharged, and its literal form is false.**  None of
the four constructions of Thm. 6.3 is an operation on `Γ_n ∈ G`; they are a
cotangent complex on `G_m/Z`, a complex of abelian groups on `L_S`, an operator
on `Z[L_S/nL_S]`, and a Koszul complex in `Z[t,z]`.  The actual derived
self-contact of `Γ_n` in `G` is Paper 43 Thm. 7.1(c) and is `C[0]` at `p|n`,
independent of the twist.  Moreover the plan's B.4 read literally — the
**derived diagonal** contact identified with `[Z→Φ_n(1)→Z]` — is *false*: the
derived diagonal contact is the fixed complex, differential `n−1` (P123.060
(2.1)).  `ACCEPTED`.  B.4 is marked `REFUTED AS STATED` and replaced by the
ramification contact, which is what rows C/D actually use.

**B4. Theorem 3.3 renames rather than realizes.**  P123.060 §2 says of the very
factor `p^{−k/2}`: "the half-density numerator comes from the dilation action.
**Neither supplies a `Z/p` ramification contact as the cohomology of (2.1)**",
and §4 forbids obtaining the relation "by **renaming**".  Theorem 3.3 produces
no complex at `p|n`; it observes that a number `|n|_p^{1/2}` appears there.
`ACCEPTED`.  Corollary 3.4's claim that row A's invariant "realizes" both
complexes is withdrawn; what survives is the **coprime support** statement,
which is correct and is the paper's real contribution.

**B5. `w_unit(Γ_n) = n−1` is chart-dependent as defined.**  On the minimal
chart `S = {∞} ∪ P(n)` the product `∏_{p∈S_f, p∤n}τ_p` is empty, hence `1`, not
`n−1`; the value `n−1` needs the product over **all** rational primes.
`ACCEPTED`.  Fix: take the product over all finite places (legitimate, since
`τ_p = 1` off the finite set `V(n) ∪ V(n−1)`), and note that the quantity
depends only on the gauge-invariant anchor `b_S = n` of P123.038 §2.

**B6. The archimedean place is dropped without accounting.**  `a_S(n)` has
`σ_∞ = 1`, where (1.1) is undefined; Paper 43 Def. 8.1 handles that case by the
renormalized identity determinant (P123.012, P123.105), a nonzero
contribution.  `ACCEPTED`; `w` must be declared a finite-part quantity.

**B7. `w(Γ_n)` is not a value of row A's invariant.**  Paper 43 Lemma 8.2 says
two admissible regularizations of (8.2) differ by `c·log|w|`; for
`w = a_S(n)`, `log|w| = −log n`, i.e. exactly the magnitude row B extracts.
Paper 43 (9.1) escapes this only because it is a **difference** of two classes
of modulus one.  `ACCEPTED`.  Fix: `w` is defined as a product of the **proved
local factors** of P123.042, not as a value of `T`; every reference to the
"`γ=1` term of (8.2)" is removed.  This also decouples row B from A2 of
[D128.001](D128_001_AUDIT_A.md).

**B8. Theorem 5.4 refutes a strawman.**  The open item (P123.037 §5) is
object-level: "transitivity (1.2) is an exact triangle, not such an
isomorphism".  Refuting {monoidal + **additive degree** + `deg = Λ`} attacks a
conjunct nobody asserted.  `ACCEPTED`.  **But the correct statement is
provable and is now proved**: `Prim_2 ⊗^L Prim_2 = Z/2 ⊗^L Z/2 = Z/2 ⊕ Z/2[1]
≇ Z/2 = Prim_4`, so `Prim` is not monoidal for `⊗^L`.  The open item is closed
properly rather than by reclassification.

**B9. Minor, all verified:** Def. 5.2's `m=0` clause is incoherent (`n=1` gives
`m=1`, and `[Z→0→Z]` has infinite `H⁰`) — deleted; Remark 4.7's claim that
`[Z→1−u→Z] ≅ [Z→1−u^{−1}→Z]` fails over `Z` for `u = n ≥ 2` (`1−n^{−1} ∉ Z`) —
restricted to the analytic factor; "four independent constructions" is an
overclaim, (b) is derived from (a) — restated as two routes plus two
transports; the adversarial table has `n−1` prime in every row — rows `n=9,10,16`
added; there is no functor `W → G` (the divisor morphisms have no image, by
P123.082) — B.2 restated as monoidal on the label monoid only.

## Verified in the paper's favour

The audit independently re-checked and confirmed: all `Φ_n(1)` values, all cube
alternating sums, the `V(n)`/`V(n−1)` columns, `#H⁰(C_fix) = n−1`, and the
product-formula computations `(∏_{p<∞}|n|_p)^{1/2} = n^{−1/2}` and
`∏_{p<∞}|n−1|_p^{−1} = n−1`.  It also confirmed that P123.019 §4 does prove the
associativity coherence used in Thm. 4.3 (the paper cited the wrong place).

## Disposition

The label `WEIL-STRENGTH-COMPLETE` for row B is **withdrawn**.  See
[D128.004](D128_004_WHAT_SURVIVES.md).
