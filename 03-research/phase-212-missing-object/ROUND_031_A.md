# Round 031 A — Cross-check of antecedents: inequality for entire functions with zeros at ±i/2 for (PBP_T)

Type: reading cross-check. Nothing is constructed. Labels as they appear in the source.

## 0. Operation cross-checked

Bound from above `μ(|τ| < 6.29)` (or `∫m dμ` from below) for `μ = Σ|F̂_i|²dτ/2π`, `F_i ∈ P_T`, using at once
(i) exponential type `T` (density of type `2T`), (ii) double zeros of the density at `±i/2`, and possibly
(iii) `Φ(log n) = 0`, `n ≥ 2`.

## 1. What was opened

- Paper 46 (`04-papers/46-row-d-dual-certificates/main.tex`): thm:A and its proof (l.444–477), rem:Kprim (l.479),
  prop:arch (l.2323–2350), thm:index and its proof (l.2518–2560), prop:NC, cor:P3, rem:P4, thm:J and the observation
  that follows (l.2638–2780), thm:nyq-cone with proof and rem:nyq-dual (l.6320–6360). By grep: lem:polarelim,
  prop:sharp (l.7330–7361), prop:haynsworth (l.10992), lem:KyFan (l.10802).
- Phase 155: R155_033 (§§ "τ = 0 cap", §3 index, l.110, 272–363), R155_047 (Thm P, Cor P3, Remark PA/P4).
  R155_052 header only. R155_023/024/027/048–051: NOT opened (covered by P46 thm:index/cor:P3, which integrates them).
- Phase 160: R160_M2_R1 (table of results, §§ definitions, Thm 4.1, Thm 4.2); R160_PC_R1 by grep (l.129, 271).
  R160_D4_R2 and R160_M4_R1: grep only ("primitiv/P_T" appear, no Paley–Wiener); not read in full.
- Phase 186: R186_052 §3 (Thm 3.1 primal cone, Cor 3.2, Thm 3.3, Thm 3.4). Phase 195: VERIFY_CLAMPED_AND_EDGE_LAW (statement).
- Phase 211: ROUND_007_B §§0–1.3 (piece 𝔢, form in the potential `G ∈ H²_0`); ROUND_008_E, 009_A, 009_B only by grep
  (prolate concentrations of `[−λ,λ]` in the extension construction; another object).
- Phase 212: ROUND_026_B §§1–3, ROUND_030_B §§2–3 and closing; entries 212-26-B (l.31333) and 212-30-B (l.31398) of the index.
- Master index: grep of the requested list; read the families "prolate / Thm P" (l.250–253, 3688, 3717, 4645, 5150),
  "polar capacity" (l.256, 4731, 5194), "Paley–Wiener" (l.2035, 2172, 2212, 5330), "Slepian" (l.3298, 3625, 4713),
  "Blaschke" (l.4551, 4685), "de Branges" (l.2151, 4521–4530), "Sonin/prolate" (l.2133–2141, 5141–5163, 5994, 6028).
- NOT opened: phases 153, 154, 156, 159, 183–185 (except grep), 197, 199 (only list of files with "prolat": KK_001,
  C_001, BB_001, U_001; not read), 201, 204. Grep in 183: "entire/prescribed" only gives prescribed support and Tate
  conditions on `h_1` (R183_002 l.77), not a concentration inequality.

## 2. Real antecedents

**A1. P46 thm:nyq-cone (l.6320; PROVED, Akhiezer CITED) = R186_052 Thm 3.1 + Cor 3.2.** The cone of densities
`{|F̂|²: F ∈ P_T}` is exactly `{f ≥ 0 on ℝ, entire of type ≤ 2T, L¹, zeros of order ≥ 2 at ±i/2}`, and
`P_T = (¼ − ∂²)H²_0(I_T)`, `F̂ = (τ² + ¼)Ĝ`. Tool: Akhiezer + Paley–Wiener + Blaschke factor
`(z − i/2)/(z + i/2)`. It is the exact characterization of (i)+(ii); it gives no mass bounds. Class (β): same tool,
used as a reformulation of the cone, not as an inequality.
*Immediate consequence (PROVED, one line from A1):* every mixed density `Σ|F̂_i|²` with `F_i ∈ P_T` is in
the cone, hence is `|F̂|²` of a single `F ∈ P_T`; since `Φ(log n)` is linear in the density, **(PBP_T) over mixed
states of P_T coincides with the pure problem `Z^A_T`** of R160_M2_R1 (l.111). By contrast ROUND_026_B/030_B work
with `Z^prim_T` (relaxation `K^prim` of eq:Kprim: two linear conditions on `Φ`), which is strictly weaker
than "double zeros". The claim of ROUND_030_B §3 ("primitivity is not a bounded functional on μ") is correct
for `K^prim`, but in the double-zero version primitivity is a **weight**: `μ = (τ²+¼)² ν`, `ν` the density of
`G ∈ H²_0(I_T)` (R186_052 Cor 3.2: "Tate = weight").

**A2. P46 prop:arch(ii) (l.2323; PROVED).** `λ_inf,P(T) ≤ C_0 + φ((3π/2T)²)` and `λ_inf,P(T) ↓ C_0` as `T → ∞`.
That is: **(i)+(ii) without (iii) do not bound the low mass uniformly in T**; there are primitive states with
`∫m dμ → C_0 = −5.372`. Class (α) for the part (i)+(ii): negative result PROVED. Proof: Dirichlet modes +
concavity of φ (cor:mono); the restriction to `P_T` costs at most two modes (`λ_3`).

**A3. P46 thm:index (l.2518; PROVED with certified intervals).** Exact value of the problem (i)+(ii) on small
windows: `n_-(A_∞|P_T) = 0` for `T < T*_ev`, `0.58 ≤ T*_ev ≤ 0.60`, `T*_odd ∈ [log 2, 0.81]`, index ≤ 2 on `(0, 0.90]`.
Tool: multiband minorant of `m` (28 bands), finite Legendre section by parity, tail via the trace
(lem:KyFan), Haynsworth certificates (prop:haynsworth) and explicit negative planes (prop:negplane). The two
constraints `e^{±t/2}` are imposed in the finite section; an inequality for entire functions with prescribed zeros is
**not** used. Class (α) as regards the result (i)+(ii); (β)/(γ) in the tool.

**A4. P46 prop:NC, cor:P3, rem:P4; R155_047 Thm P (PROVED).** Prolate concentration `S_{T,τ_1}` + two-valued
minorant: `n_- ≤ 5/7/8` at `½log3, log2, 0.80`. R155_047 l.155: "the two Tate constraints only remove
directions … and are not used". rem:P4: the floor 5 is due to the two-valued minorant and to `codim P_T = 2`, not to prolate
theory. Class (β): (i) without (ii). Route "two-valued prolate" CLOSED (index l.3688, 3717, 5150).

**A5. P46 observation after thm:J (l.2770–2776).** States that a lower bound of the archimedean form requires "an
explicit non-asymptotic estimate of prolate concentration" and that concavity (Jensen) only gives upper bounds.
It is the same question (i), without (ii) or (iii); declared, not resolved. Class (β).

**A6. R155_033 "τ = 0 cap" (l.110, 350; PROVED).** Bound on dual certificates `f_w(0)`; another object (weights `w`), (β/γ).
R155_033 l.332: "the two primitivity constraints subtract at most 2" from the index (PROVED): (ii) is codimension 2.

**A7. ROUND_007_B (211) §1.3 / P46 lem:polarelim, prop:sharp (PROVED/CITED).** In the potential `G ∈ H²_0`:
`Arch = 𝔞^♯ − 𝔢`, `m^♯ = m + 1/(¼+τ²)`, `m^♯(0) = C_0 + 4`, `𝔢 = ∫|F̂|²/(¼+τ²) ≤ 4‖F‖²`. Uses (ii) as a weight
`(τ²+¼)`, with the true weight of the complete form; the residue (N) remained OPEN. Class (β): same tool
(Tate weight), another object (with fixed `v_n`, without `Φ(log n) = 0`).

**A8. R160_M2_R1 Thm 4.1–4.2 (PROVED).** Defines `Z^A_T` (pure, primitive, prime-blind) and `Z^prim_T` (relaxed),
strong duality and sandwich `Z^prim ≤ V* ≤ Z^A`. No lower bound for either; H1 (l.26) is HEURISTIC.
R160_PC_R1 (l.129, 271): the target `Z^prim_T ≥ e^{−(2π−η)e^{2T}}` remained as a statement to prove, OPEN.

**A9. ROUND_026_B / ROUND_030_B (212).** Kreĭn (ceiling 3.0–3.4) and one generator (`𝔈 ≥ −1.4979 − 5.0434/(J+1)`, optimal
for one generator). Neither uses (i)+(ii). 026_B l.59–62: primitivity via `cosh(u/2)` has asymptotically null
contribution (ARGUED).

**Vocabulary-only matches (γ):** Paley–Wiener in index l.2035 (fixed PW basis as detector, FALSIFIED),
l.2172 (ξ-divisibility, NO-GO), l.2212 (pivot LP-141), l.5330 (PW nodal tests read `Φ_Λ` only at `log k`, DEAD);
Slepian l.3298/3625/4713 (decay law, refuted prediction; another object); Blaschke l.4551/4685 (Fejér
blocks, first-contact witness; DEAD); de Branges l.2151/4521 (reformulations, Conrey–Li); prolate–Sonin
(phase 183, CC_001, boundary triples: concentration of `[−λ,λ]` in the extension construction, without `Φ(log n)=0`).
There are no matches for Logvinenko–Sereda, Kovrijkine, Remez, Nazarov, Turán, Beurling–Malliavin applied to
low mass (l.2796 and 5163 are BM density in `p^{iτ}`, another object).

## 3. Does the failure reason apply to the operation?

- (i)+(ii) alone: **yes, closed**. A2 proves there is no bound uniform in `T` (infimum → `C_0`); A3 gives the exact value
  on small windows. Any PW inequality with zeros at `±i/2` without (iii) is bounded by A2 and must reproduce
  `T*_ev ∈ [0.58, 0.60]` (a stronger bound ⇒ contradiction with prop:negplane).
- Structural reason: (ii) is codimension 2 (R155_033 l.332; prop:arch proof with `λ_3`); its weight `(τ²+¼)²` only
  penalizes `|τ| ≲ ½`, while the mass to be controlled (ROUND_030_B §2.3) is in `π/log 2 < |τ| < 6.29`, where
  `(τ²+¼)²` is relatively almost constant. Therefore (ii) cannot contribute something of the order of the deficit `1.498`; ARGUED
  (this round), consistent with 026_B l.59–62.
- (i)+(ii)+(iii) together: **not done**. Nobody bounded `Z^A_T` or `Z^prim_T` from below with exponential type.

## 4. Verdict

**PARTIALLY DONE.** (i)+(ii): repetition (α) — resolved negatively for large `T` (prop:arch(ii)) and
exactly for `T ≤ 0.90` (thm:index). (iii) with one generator and Kreĭn: 212-26-B, 212-30-B. The combination
(i)+(iii) [exponential type with vanishing at `log n`] and (i)+(ii)+(iii) is not done.

What would really be new: an inequality using the **type `2T` together with `Φ(log n) = 0` for several
generators** (free non-integer quotients, ROUND_030_B §2.3) to control `μ(π/log 2 < |τ| < 6.29)`; with
primitivity only as a codimension-2 correction / weight `(τ²+¼)²` near 0, not as a mechanism.

Results that any construction MUST respect:
1. thm:nyq-cone: (PBP_T) over mixed states of `P_T` = pure problem `Z^A_T`; do not confuse with `Z^prim_T` (eq:Kprim).
2. prop:arch(ii): without (iii), infimum → `C_0 = −5.3722`; every bound must degrade to this if (iii) is removed.
3. thm:index: with (i)+(ii) and no effective contacts, positivity exactly up to `T*_ev ∈ [0.58, 0.60]`;
   index 1 at `log 2`, 2 at `0.81–0.90`.
4. cor:P3/rem:P4: the two-valued minorant does not go below 5 at `log 2`; use multiband minorants.
5. ROUND_030_B §2.3: one generator is optimal at `−1.4979`; the improvement must come from interacting generators.
6. R160_PC_R1: the useful threshold for `Z^prim_T` is `exp(−(2π−η)e^{2T})`; R160_M2_R1 T6: `Z^prim_T ≤ λ^A_T`.
7. P46 (observation after thm:J): Jensen/concavity only gives upper bounds; non-asymptotic concentration is needed.
