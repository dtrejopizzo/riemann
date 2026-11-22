# CA_C_003 — Settling (Fam_η) = T*₃(η) at η > 2/3: what it is, what it implies, and where the hand proof stops

Phase 193, round 7. Pen and paper. One table read from EXP_005 §5 (NUMÉRICO, not recomputed). **No sign contact. No negative
value for ζ.**

## 1. Identification (corpus check)
(Fam_η) of CA_C_001 §4 is T*₃(η) of SPEC_B §1.3: for all M and all w ∈ 𝒲_η, Q_M(w) = s_w^⊤A_M s_w ≥ 0. The collapse, its Farey form and the
dichotomy (§1.4) are there. The phase-192 identities (EI_002, Thms 1–5) are exact for Q_M(w). What CA_C_001 added is the reading of the
collapse as the product formula (Lemma 1) and the singleton/falsifier table of relaxations (Theorem 1), which is not in SPEC_B.

## 2. What T*₃(η) implies for η > 2/3
**Proposition 1 (PROVED, from CA_C_001 Obs. 2).** span{s_w : w ∈ 𝒲_η} = {s : m^{½}s_m constant on m ≤ ηM}. So T*₃(η) is the statement
"A_M ⪰ 0 on the subspace of vectors that are c·m^{−½} on [1, ηM] and free on (ηM, M]". This subspace has codimension ⌊ηM⌋ − 1.
**Proposition 2 (NUMÉRICO input, PROVED deduction).** By EXP_005 §5, the bottom eigenvector of A_M is v_M = m^{−½}w_M(m/M)(1 + noise ≤ 0.4%),
with w_M(0.5) ∈ [0.89, 0.95] and w_M(0.8) ∈ [0.84, 0.85] for M = 400…1200. Since w_M is not constant on [0, 0.5], v_M lies outside the span of
Proposition 1 for every η ≥ 0.5, and in particular for η > 2/3. Hence we are in case (ii) of SPEC_B §1.4: **T*₃(η) for η > 2/3 is a necessary
condition, strictly weaker than (S) along these M (NUMÉRICO), and not a restatement of it.**
**Remark (distance in the natural norm; ARGUED).** The relative distance of v_M to the span is small: the defect sits on (0.4M, ηM], where the
weight Σ m^{−1} carries mass log(η/0.4) ≈ 0.5, against ‖v_M‖² ≍ log M. So dist² / ‖v‖² ≈ ∫_{0.4}^{η}(w_M − 1)²dx/x / log M ≈ 5·10⁻³/log M → 0.
This does **not** make T*₃(η) strong. The margin of (S) is λ_min ≍ M^{−3} (NUMÉRICO), and a vector at relative distance (log M)^{−1/2} from
the minimizer can have a Rayleigh quotient larger by up to dist²·(spectral spread), which is ≫ M^{−3}. "In the family for some η" holds
(SPEC_B: η ≈ 0.3–0.4, where T*₃ is REF-D). It fails for η > 2/3.

**Answer to the coordinator's question.** The A_M-minimizer is in the family for η ≈ 0.3–0.4, where T*₃(η) is REF-D (SPEC_B §1.4(i)).
It is not in the family for η > 2/3 (Prop. 2, NUMÉRICO). So (Fam_η > 2/3) is **not** strong: it is a necessary condition only. The two
properties that would have made it interesting, "prime-free (log 2 only)" and "contains the minimizer", hold on disjoint ranges of η.
This is SPEC_B's sentence "no choice of η is simultaneously strictly weaker than D and sufficient", made explicit by the product formula:
**primes are absorbed exactly where the minimizer is flat, and the minimizer is flat only on [0, 0.4M], so d < e^{2T₀}/0.4 < 5 always
survive (Λ(2), Λ(3), Λ(4)).** These are the "defects at 2, 3, 4" of EXP_003 §3, now explained.

## 3. The hand proof of T*₃(η), η > 2/3: where it stops (exact obstruction)
Write Q_M(w) = 𝒜_M(w) − Σ_N N^{−½}D_w(N)E^w_M(N) with D_w(N) = 2c log N − 2 log 2·[2|N]·(c − w(N/2M))·1{N/(2M) > η}.
(a) **Bulk vanishing (PROVED, from P46 prop:shape-family(iv) and the two Tate conditions).** For N ≤ ηMe^{−2T₀}, w ≡ c on the support of
c₀(log(m/N)), so E^w_M(N) = c Σ_m m^{−½}c₀(log(m/N)). Its Euler–Maclaurin main term N^{½}c∫e^{v/2}c₀(v)dv vanishes, and so does the
first-order term (∫v e^{v/2}c₀ = 0, the double zero of ĉ₀ at −i/2). What is left is the ℤ-Poisson dual sum Σ_{ℓ≠0}, of size
O_A(N^{½}(N·(1−e^{−2T₀}))^{−A}) for the smooth F₀ (rapid decay). So the bulk N-sum of 2c log N·N^{−½}E is O(1) and explicit.
(b) **The arch term.** 𝒜_M(w) = (1/2π)∫mF̂₀²|ζ_w|². With ζ_w = cζ + M^{½−iτ}W(½−iτ) + ρ_M (EI_002), it has an M-order piece
M·(1/2π)∫mF̂₀²|W(½−iτ)|². This piece must cancel against the edge comb terms, because Q_M(1) = 2.58 = O(1) (NUMÉRICO, SPEC_B).
(c) **The edge.** For N ∈ (ηMe^{−2T₀}, Me^{2T₀}), E^w_M(N) sees the variation of w on [η, 1], and the log 2 defect enters. Q_M(w) is then
an O(1) remainder of an O(M) cancellation between (b) and the edge, plus the O(1) bulk of (a). EI_002 Thm 5 applies verbatim: the Mellin
split has no termwise sign, and the edge is a Poisson-dual (lattice) sum.
**Obstruction (precise).** A hand proof of T*₃(η) for η > 2/3 needs the sign of the O(1) remainder
  R_M(w) := [M-order arch piece] − [edge comb at order M] + [bulk O(1)] + [log 2 edge defect],
uniformly in w ∈ 𝒲_η (C_j η^{−j} bounds) and in M. Whether this is a "margin" statement (inf_{w∈𝒲_η} Q_M(w)/‖s_w‖² ≥ c > 0, or ≍ 1/log M)
or a "critical" one (≍ M^{−3}) is **not known**. On that dichotomy everything depends:
- If it is a margin statement, T*₃(η) is a PNT-level / lattice-level theorem, plausibly provable by hand, and a necessary ζ-specific condition.
  It is ζ-specific only if some falsifier fails it, which is open for η > 2/3 (SPEC_B: falsifier directions are in 𝒲_η only for η ≲ 0.2).
  In that case it would probably be a class property, and so no route.
- If it is critical, (B′) applies (lem:shape-est(i)) and no hand estimate can carry it.
The decisive datum is one number per M: μ_M(η) := inf_{w∈𝒲_η} Q_M(w)/‖s_w‖² at η = 0.7. This is a numerical check that is strictly
necessary to settle (Fam_η), and I flag it as such (NUMÉRICO, not run here; it is a constrained eigenvalue problem on the
subspace of Prop. 1, with cost equal to one A_M diagonalization).

**Self-review.** (1) "(a) is new?" No: it is SPEC_B Line 2 / EI_002 Thm 3 (second-order Tate vanishing in the bulk). (2) "Prop 2
rests on numerics." Yes. The deduction is proved and the input is NUMÉRICO (EXP_005). (3) "Could T*₃(0.7) still be strong if the gap of A_M
restricted to the span is comparable to λ_min?" Only if μ_M(0.7) ≍ M^{−3}, which is the critical case above, and then (B′) blocks a hand
proof anyway. Either way (Fam_{η>2/3}) is not a route to D. (4) No sign contact.

## 4. Verdict
- (Fam_η) = T*₃(η) (SPEC_B). Retry acknowledged (CA_C_001 erratum).
- η > 2/3: necessary condition only. The minimizer is outside the family (NUMÉRICO input, PROVED deduction). The only new explanation is
  that the "defects at 2, 3, 4" come from the product formula absorbing exactly the primes below e^{2T₀}/η_flat, with η_flat ≈ 0.4.
- A hand proof is blocked at the O(1) edge remainder R_M(w). The margin-or-critical dichotomy is decided by μ_M(0.7): one strictly necessary
  NUMÉRICO check, flagged and not run.
- No YES→NO move. Index: "T*₃(η), η > 2/3: necessary only (CA_C_003); open datum μ_M(0.7)".
