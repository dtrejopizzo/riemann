# R168_001 — Semantic survey: open residues and input classes never used (phase 168)

Method: grep over all of 03-research and 04-papers (*.md, *.tex), with context reads of the hits. Grid read: R162_2300_MASTER_GRID §3, §6, §7.
Labels: (a) RH-neutral, (b) RH-strength (equivalent to RH or stronger), (c) possibly weaker than RH and relevant to D. "Attacked" means a later phase worked on it.
No new mathematics here. Every verdict is a record verdict (from grep) unless it is marked SURVEYOR.

## 1. Open residues

| # | Residue (one line) | Class | Attacked? |
|---|---|---|---|
| 1 | O-151.4: true axis summand vs numerator in the T6/dlVP family (8C) | c (weak) | No. R166_404 row 8: "never developed" |
| 2 | GAP-157.A / Q26: discrepancy or irrationality-measure bound for the Kronecker flow τ↦(p^{iτ}), non-local Tauberian with LI input (3E/3F/4F) | c | Partly. Phase 49 killed 2 of 3 routes; F40 local form = E1; the non-local form is still OPEN (R166_400 Q26) |
| 3 | Q27 / P122 E_(∞,T): relative correspondence Bohr ↔ quarter-Γ Calderón (1H) | a, until a sign is added | No. Never built (R166_404 row 16) |
| 4 | P13: laminated carrier (Deninger D1–D3; Torelli-failing lamination, R160 D1/C1 OS-1) (8H) | b if built with positivity (W10) | Partly. R160_C1 Thm Z: at most 1 pair; Torelli-failing case not attacked |
| 5 | P14: Meyer H¹ density / H¹_alg (R158_006) | a. Density is PROVED (R160_C3 Thm B); positivity is E1 | Done as a density result; nothing open with content |
| 6 | C1 (R166_701): every θ=0 Beurling system is ζ·(finite Euler modification) | c, and needed for C2 | No. Hilberdink 2012 not yet read (O166.701.1) |
| 7 | C2: some θ=0 discrete system has a zero with Re s>½ | b. If C1 holds, C2 ⟺ ¬RH | No |
| 8 | O166.501.1 (meta): must a separating H without Z^off be non-linear in Λ beyond the window? (7B) | a (meta) | No |
| 9 | O166.802.1: circularity of (N′) for arbitrary non-linear B (3A) | a (meta). Settles whether (N′) is a wall | No. Only ARGUED |
| 10 | Exact stop of R167_102: large-values bound for Type II products of length X at a single height | c. This is the only sub-RH form of (WS*) | No. No literature (ARGUED) |
| 11 | O167.101.1 (Dom_θ): other quartets near γ_q carry ≤θ|Q_K| (7D) | b at the witness (same as R165_102 (Dom), O701.1) | Partly. R163_701 B.2: Turán power-sum loss swamps the gain |
| 12 | O167.101.2: small-y regime needs an on-line count sharper than S(t)=O(log t) (7D) | c. A Lindelöf-type or S(t) improvement, not RH | No |
| 13 | O202.1: T_e = T_o for ζ carries no sign (6C) | a | No. Closed as a statement, with no route left |
| 14 | O164.201a: discrete Beurling system off the Witt lattice, error O(x^{θ′}), θ′≤1/3, with a zero at β>½ (5G) | c (a construction problem; a counterexample-type object) | No |
| 15 | O164.503a: prime-side rounding stops at x^{1/2} (stationary phase) | a (ARGUED tool) | No |
| 16 | O164.503b: check Huxley's exponent 131/416 in Goal B ⇒ quadratic GRH | a (bookkeeping) | No |
| 17 | O164.503c–d: quadratic-mean §3.3 and system variants (Goal A OPEN) | Goal A: c. Goal B: b+ (RH + quadratic GRH) | No |
| 18 | O164.601.1: lower bound for Σ_{q′}Re[G(t_{q′})²K(t_{q′})] with K localized at γ_q (7F) | b. This is (★_cell) weighted by K | Indirectly. Phases 165–167 |
| 19 | (★_cell)/(TC)/(WS*) | b at the witness. The single-scale form is the explicit formula (Thm E) | Yes. 163–167, all DEAD |
| 20 | §6 items 1, 2, 5, 9–11, 13, 14, 16–19, 22, 26, 27, 31–33, 37, 38, 41–44, 48–50, 52–59 and part 7 (O2201.1, O2302.1–2, O2202.1, O2401.1) | mostly a (carriers, Kreĭn and KK indices) or b (item 19 is RH-strength, item 43 is W10). Exceptions in class c: item 8 GAP-197.1, item 11 GAP-179.B, item 39 C_B, item 41 Problem B, O2302.2 | No later attack is recorded for these. See grid §6 |

The master-grid ranking reaches the same conclusion: every class-c item reduces either to the Beurling frontier (C1, O164.201a, Goal A) or to a single-height large-values bound (#10, #12). No class-c residue reaches the witness directly.

## 2. Input classes: FOUND / NOT FOUND

| Input | Verdict | Where, how it was used, record verdict |
|---|---|---|
| Baker / linear forms in logs | FOUND | phase-12-meta-obstruction-moment-problem M12.6–M12.7: Baker used on near-coincidences of log(pq/rs); "too weak". MAP_1 NG-B7: wrong category for γ. Paper 36 ng:baker. Never used on p^{iγ_q} at the witness. |
| Diophantine approximation of p^{iγ} | FOUND | phase-12-meta-obstruction-moment-problem M12.6; phase-47/148 (GAP-135.A, frames); GAP-157.A; R167_291 Lemma K (alignment needs log γ ≳ Y/log Y, so it is only an observation). |
| Ergodicity / equidistribution of γ log p | FOUND | P122_016 (Kronecker flow, uniquely ergodic); R154_001 (hyperfinite II₁, no transversal); R160_M12 (×p×q rigidity, Rudolph–Johnson, sign-blind); phase-51/160 Erdős–Turán discrepancy, Prop 160.12 (universal, so it falls to W2). |
| o-minimality / Pila–Wilkie | FOUND | R162_2402: NO-GO (W10+W8). |
| p-adic ζ (Kubota–Leopoldt, Iwasawa) | FOUND, shallow | G1_B3_R2 Thm I: Iwasawa positivity is compactness (a ℤ_p-lattice). It was never tested as a constraint on ζ at the archimedean place. |
| Random matrix statistics as a constraint | FOUND only as heuristic | phase-7-weil-carleson-sine-kernel P7b (sine kernel = same wall, "describe, do not force"); phase-21-negative-directions-geometry/02 W3; phase-8-heat-flow-monotonicity. The unconditional pieces (Montgomery F(α), |α|<1, under RH; Goldston–Gonek; Rudnick–Sarnak n-level) were never used as an input. Counted as NOT FOUND in that sense. |
| Selberg class beyond degree 1 | NOT FOUND | Only degree 1 appears: Kaczorowski–Perelli in R162_2801/2890 and R160 briefs; Suzuki's Hamiltonians in G1_B8_R1 as a framework. No use of degree-2 structure (ζ², Rankin–Selberg ζ⊗ζ, Conrey–Ghosh, primitivity/factorization). |
| Erdős–Turán-type quantitative unique factorization | PARTIAL | The discrepancy inequality is used (phase-51/160). Beurling rigidity is used (DMV, Zhang, Theorem S in R167_103; Hilberdink pending). The multiplicative-semigroup quantitative UF theorems (Erdős–Turán/Szemerédi-type sumset or Sidon structure of log ℕ) were never used. |
| Deuring–Heilbronn / Landau–Siegel repulsion | FOUND, generic only | MAP_1 NG-B3 (phase-25-lower-bounds-bj-audit): "no anti-Siegel repulsion". phase-37/111 §3: the Siegel mechanism has no analogue for ζ quadruples, and two quadruples look worse (anti-Siegel). R163_603 Rem 5.1a: (H-sep) is exactly an on/off-line repulsion at scale δ_q, and "nothing known gives it". Never attacked as a witness-scale input against M_m. |
| Turán power-sum method | FOUND | phase-37/111 §4 (no finiteness); NG-B1/B6; R163_701 Rem B.2 (Knapowski–Turán loss (cn)^{-n} swamps the gain); G2_B5_R5 (pointer). |
| Montgomery–Vaughan Hilbert inequality at the witness | FOUND | R167_102 Thm A (η=½ for every witness weight); R167_103 (holds for Beurling); R163_601; R162_404/408. |
| Zero-density N(σ,T) as input | FOUND | phase-12-meta-obstruction-moment-problem M12.10 (b) ("few", never "none"); R163_111; R167_102 Thm D (after Perron = zero density). |
| Bohr–Jessen | FOUND | G2_B7_R1/R2 (dead end: ∀T positivity is Haar-null); R163_802. |
| Universality (Voronin, Bagchi) | FOUND | phase-35/102; R139 D.19.5 (DH vs Voronin); R163_602/603/901. |

## 3. Ranking of the not-found and under-used classes against (★_cell)/(WS*)

1. **Deuring–Heilbronn repulsion at the witness (zero side, non-linear).** This is the first class that could fail on M_m rather than be refuted by it. Theorem 5.2 of R163_603 shows that inputs (a)–(d) — positions, averages, identities — cannot exclude a witness, because M_m inserts quartets by hand. D–H is different in kind. It is an *implication* between zeros that comes from the Euler product and an explicit-formula positivity: one exceptional zero forces the others away, with the trade-off depending on the distance. If a version holds at height γ_q, with an off-line zero at δ_q repelling on-line zeros to distance ≫ δ_q·f(δ_q log γ_q), it supplies (H-sep), and R163_603 T5.1 then closes. The walls to evade: (i) identification, since the repulsion must use a property that M_m lacks; it is the Euler product through the positive kernel in the D–H proof, which is the "both sides coupled" form R166_190 demands. (ii) W2/M, since classical D–H costs exp(−c/δ) and the witness may sit at Theorem-M depth. (iii) NG-B3/anti-Siegel (phase-37/111 §3): the archimedean budget ≍ log γ swamps any positivity budget away from s=1. Verdict (SURVEYOR): the only genuinely new mechanism type. Phase-37 §3 already argues it is quantitatively hopeless near ½. A test that reads it from the record: compute the D–H trade-off for a single quartet in the (★_cell) normalization and compare it with δ_q at the witness.
2. **Selberg class degree 2 (ζ², ζ⊗ζ̄, Rankin–Selberg).** A Weil/explicit-formula positivity for the Rankin–Selberg square has a non-negative coefficient sequence (|a_n|² structure). Its zeros are the zeros of ζ doubled, so an off-line quartet of ζ appears with multiplicity, and the square-structure positivity is the usual source of Siegel-type repulsion (#1). It would evade identification because it is a different L-function with the same zeros. It must evade E1: positivity of the doubled Weil form is again RH, so only a *strictly weaker* non-negativity, such as Landau's lemma on the |a_n|² series, helps. It must also evade W4 (wrong sign: square positivity gives lower bounds, while (WS*) is an upper bound). This is the cousin of the sum×product square that R161 refuted (F2). Risk: high.
3. **Unconditional pair-correlation / n-level statistics as constraints.** These are averaged, so they fall under Theorem 5.2(b) and W2: averages over H→∞ never exclude a witness. The only escape is the short-range, unconditional forms (Goldston–Gonek–Montgomery with weights, Rudnick–Sarnak for supp f̂ < 2/n), which are still averages. Expected to die at M_m and W2. Low.
4. **Erdős–Turán / Szemerédi-type quantitative unique factorization.** This is integrality on the prime side. It must evade W3′ and W-identification: "integer multiset = ℕ" already forces ζ (R167_103 row 11), and Theorem S shows that sieve-type tools hold equally for Beurling. Additive-combinatorial structure of log ℕ is still integrality, so it dies at identification unless it gives a large-values bound at one height (residue #10). Low-to-medium. It would be relevant only if aimed at #10.
5. **p-adic ζ at the archimedean place.** Kubota–Leopoldt interpolates values at negative integers, which is functional-equation data shared by f_χ (W3′). Iwasawa positivity is compactness (G1_B3_R2 Thm I) and blind at the archimedean place (W11). Lowest.
6. **Baker on p^{iγ_q} (under-used, not new).** Lower bounds for |Σ b_p log p − 2πk/γ| only control alignment, which is what Lemma K needs, and alignment already does not refute (WS*) (R167_291). Dies at W-sieve/(N′). Low.

Summary: the only class not used that differs in kind is witness-scale **Deuring–Heilbronn repulsion**: a non-linear statement on the zero side forced by the Euler product, which M_m cannot satisfy, and exactly the (H-sep) hypothesis that R163_603 says "nothing known gives". Degree-2 Selberg-class positivity is the natural carrier for it. Everything else in the requested list is FOUND and closed by a named wall, or reduces to an open residue (#10, #12) that is the sub-RH form of (WS*).
