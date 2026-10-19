# R165_000 — Phase 165 proposal: critical interlacing and the detection theorem

**Status:** proposal. Nothing proved here. Corpus check done before writing: "interlacing" appears
only as *eigenvalue* interlacing (Cauchy; R162_504, R160_C7: E1); interlacing of *zero sets* (witness nodes
against on-line zeros, Hermite–Biehler pair) is not in the corpus; the "detection theorem" (T_c pinned to the
Landau window of the lowest off-line zero) exists only as a heuristic (R163_402 §2–3, "density-limited branch
HEURISTIC"; R163_401 (I1-b)), never as a theorem. Cells: 7A (D.16-γ "cone cut by the zero datum," never attacked,
grid §6 item 25), 7D, 2A.

## 0. Starting point (phase 164, proved)

Every class property identifies ζ. So the proof of (★_cell) uses ζ individually: its on-line zeros (verified
up to H = 3·10¹²; Levinson/Conrey; Σ_j δ_j² = o(T), R163_115), its count N(t), and the witness's geometry. What
phase 164 did not touch is **where** T_c is and **what geometry the nodes have relative to the on-line zeros at
that T_c**. This phase builds exactly that.

## 1. Detection theorem (two-sided), to be proved

Let γ* be the ordinate of the lowest off-line zero, δ* its distance from the line, T_L(γ) := ½ log(γ/2π) the
Landau window (node density T/π = on-line zero density).

> **(Det+)** There is C such that for T ≥ T_L(γ*) + C + c·log(1/δ*)/... , λ^W_T < 0. *(Construction: F̂ = P·S
> with P the polynomial with roots at the on-line zeros of [γ*−Δ, γ*+Δ] (and its reflection), S of type
> T − deg P/Δ with decay; in the supra-Landau regime the number of zeros to be cancelled fits within the type
> budget. The far sum must be bounded with N(t) and the other quartets with Σδ² = o(T). Slack is allowed: this is
> not a statement at the witness's margin.)*
>
> **(Det−)** There is C′ such that for T ≤ T_L(γ*) − C′, λ^W_T > 0 — *or* the precise way this fails.
> *(This is the hard side; R163_701 Thm B says that sub-Landau local positivity for every γ implies near-RH, so
> uniform (Det−) has RH strength. What is requested is the "first-quartet-only" version: before the window can
> resolve the on-line zeros near γ*, the quartet at γ* cannot tip the balance. If (Det−) is false, the mechanism
> must be exhibited.)*

Consequence if both hold: **T_c = T_L(γ*) + O(1)**, i.e. the witness lives exactly at the density crossing. It is
a new theorem about ζ, not equivalent to RH, with allowed slack, and fixes §2's geometry.

## 2. The new object: critical interlacing

At T_c = T_L(γ*) + O(1), near height γ*, the witness's nodes X (density T_c/π) and the on-line zeros (density
(1/2π) log(γ/2π)) have **the same density**. Two real sets of equal density can interlace. Definition:

> **(EC)** The witness is *critically interlaced* on [γ*−Δ, γ*+Δ] if between two consecutive nodes there is
> exactly one on-line zero of ζ, and vice versa.

Facts to establish:
1. **Algebra.** If F̂ (real-rooted) and Z_loc (local Hardy function, real-rooted on the line where ζ has no
   off-line zeros) interlace on an interval, F̂ + iZ_loc is Hermite–Biehler there (every zero in one half-plane).
   The quartet at γ* breaks the interlacing exactly in its cell: Z there has two fewer on-line zeros (the ones
   that "went" to the quartet). The quartet's cell is the **only** cell where the pair loses the
   Hermite–Biehler property.
2. **Geometry.** The light cone (R163_401 Lemma 3.1): Re F̂(γ*−iδ*)² < 0 ⟺ phase of F̂(γ*−iδ*) ∈ (π/4, 3π/4) mod
   π. For real-rooted F̂, phase(F̂(γ−iδ)) = −Σ_x arctan(δ/(γ−x)) + (exponential term). Under critical interlacing
   that sum is the "harmonic measure" of the point γ−iδ relative to X, and it compares term by term with the
   same sum over the on-line zeros (which is Z's phase at γ−iδ, i.e. ξ's): **the witness's phase at the quartet
   minus ξ's phase at the same point is an alternating sum of arctan over interlaced pairs**, bounded by a
   cell's width. This gives an *exact* (not asymptotic) bound on the witness's phase at the quartet in terms of
   ξ's phase, and ξ's phase at γ*−iδ* is known: ξ(½+δ*+iγ*) = 0 ⇒ there the phase is undefined and turns by π in
   a neighbourhood. Precise question: does critical interlacing force the witness's phase at the quartet
   **outside** the cone (i.e. Re F̂(t_q)² ≥ 0), so that the quartet contributes positive mass and (★_cell) becomes
   trivial in that cell?
3. **Dynamics in T.** Between prime powers the form evolves only by growth of the domain; the nodes move
   continuously; interlacing is gained or lost only when a node crosses an on-line zero, and at that instant
   F̂(γ) = 0 for a zero γ: the term |F̂(γ)|² vanishes. One must write the node flow (Hellmann–Feynman on the
   kernel equation, R163_401 §4.6) and see whether first contact can occur **without** critical interlacing in
   the quartet's cell.

## 3. Why this repeats nothing, and which wall it names

- It is not class-level: it uses ζ's on-line zeros **individually** (their exact position near γ*, not their
  average count) and the verified height γ* > H. f_t and f_χ do not have ζ's on-line zeros nor its local Z
  (their on-line zeros are different); construction (Det+) and interlacing (EC) are formulated for ζ, not for a
  class.
- Wall E1: (Det±) are not restatements of RH; they are bounds on T_c with slack. (EC) is a geometric property of
  the witness, not a zero-side identity. If §2.2's answer were "yes, interlacing pulls the quartet out of the
  cone," then (★_cell) in that cell would be trivial and Rem 4.8a's circularity would break **by geometry**, not
  by identity.
- Wall W2/M: slack only enters (Det±), which are not at the margin; §2.2 is exact.
- Main risk, stated now: that the witness at T_c is **not** critically interlaced near γ* (nodes can cluster;
  Cor SA.1 only forbids high-order vanishing at ±T_c). Then §2.3 must prove first contact forces interlacing, or
  the route dies and is recorded with the node countermodel.

## 4. Plan

- A1: complete (Det+) with constants; falsifier: it must hold equally for f_t (yes, it is pure analysis given the
  zeros) — that is correct here because (Det+) does not aim to exclude anything.
- A2: (Det−) for the first quartet, or its failure mechanism.
- A3: §2.1–2.2, the exact phase computation under critical interlacing; yes/no answer to the cone question.
- A4: §2.3, node flow in T and whether first contact forces interlacing.
- Audit at the end of the round.

Success criterion: a PROVED theorem of the form "at first contact, the lowest quartet is outside the light cone"
(closes (★_cell) in that cell and, with Lemma 3.1, in every cell), or a PROVED theorem refuting it with a node
configuration.
