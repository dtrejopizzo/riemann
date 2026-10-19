# R159_099 — Synthesis of phase 159 (two fronts, 5 rounds)

*Synthesis. Sources: R159_000 (blueprint and premises), the 50 panel reports `G{1,2}_P{1..5}_R{1..5}.md`
(the §0 verdict tables and first-defect columns were read in full), the §0 verdict of every memo, and the
run digest. [prim] means the primitive form `𝔞_T|P_T`, [compl] the
complete form `W_T` on `L²(I_T)`. No sign is claimed anywhere in this file.*

## 0. Verdict

**Neither objective was achieved.**
* **G1 (the object, OT-5′):** no candidate reached the success threshold (≥ 4 of 5). The best score of the run was
  **1/5**, three times (G1_B2_R1, G1_B2_R2, G1_B6_R2). Each of those votes was cast by P5 for "survives *as a negative
  structural result only, not an object*". No carrier with a positive form defined before the spectrum, compatible
  with the flow and with ζ's explicit formula as Lefschetz formula, was built.
* **G2 (the mechanism, ∀T):** no candidate scored above 0/5 as a mechanism. No argument gives `λ^A_T ≥ 0` or
  `λ^W_T ≥ 0` for any `T > 0.8`, in either form.

Both premises of record stand unchanged:
* nothing is proved for `T > 0.8` (Zhu, CITED; Paper 42 `T ≤ log 2` [prim]);
* `thm:finZ` holds.

What the phase produced is a set of **walls**: unconditional exclusion theorems that narrow the classes where an
object or a mechanism could live. It also produced one family of results that is correct but EQUIVALENT (the graded
Weil converse, proved five times at once).

---

## 1. G1: the object

### 1.1 What was built, by angle

| angle | what was built | panel outcome and fatal step |
|---|---|---|
| Scaling-site square (B1, R1–R5) | effective cones on the square of the scaling site; R3 two-horn theorem; R5 orbit-closure law O1–O4 | R3: excluded. Horn (i) is killed by P46 Cor 19.25b; horn (ii) fails the degree gate (`−K` effective, `2K` not ample). **P3 refuted Thm T(iii)/Cor T.1**: an intermediate salient cone with gate, ample `2K` and all witness classes exists unconditionally (G1_P3_R3 §1.3), so the "third horn = RH" clause is false as stated. R5: O1–O4 correct under (C), (Def), (Sm)/(Orb) and ergodicity. They exclude ergodic DK_α carriers; the non-ergodic residual is OPEN with no candidate |
| Deninger laminations (B2, R1–R5) | suspension of `A_K/K`; Hecke/Shimura suspension; Kronecker-line theorem; DK_α orbit–measure and homothety laws; III₁ law | R1/R2: excluded **by the memo's own Cor D1/D2** (suspended `H¹ = 0`: the polar pair only, zero-blind, C16). R2 Thm E(i) **false as stated** (G1_P3_R2 §1), repaired with a tail-defined `Γ`. R3: Cor H is an unconditional exclusion of prime-local operator carriers, via Hardy. R4: Cor M1 excludes codimension-one manifolds. R5: Prop NH says the natural suspension is not T₁, so OT-1 fails |
| FF / condensed (B3) | R1 Theorem C (slope-½ Serre lemma); R4 gap wall G | R1: **restatement**. "OT-5′ automatic" holds only after OT-5′ is redefined as a growth bound, and OT-2 then carries RH (Connes 1999 Thm 5; Lemma T(⇒)). R4: correct, but a weaker duplicate of B4 W♯. R5: flat wall F and Euler wall E, correct, excluding finite-trace DK_α |
| Arakelov / Faltings–Hriljac (B4) | R3 tail wall W; R4 sharp tail wall W♯; R5 rationality wall R/R′ | all **excluded**, all checked by 5/5. W♯ is the canonical form of the tail wall. R/R′ excludes every `Q̄`-structure at ≥ 3 primes (six exponentials, CITED). The residual Q-R5 is OT-5′ itself |
| Borger / Witt / Bost–Connes (B5) | R3 Witt–Kronecker theorem; R4 covariant orbit law K; R5 eigen-sector theorem | excluded. Suspension lives only on the Rosati part `H_u`, where zeros are installed (Lemma T(⇐)). **Cor K5(a) is false as a characterisation on `Π_κ` when `κ > #pairs`** (G1_P3_R4). The Kreĭn exit is EQUIV (Pontryagin κ family) |
| Operator algebras (B6) | R1 Sz.-Nagy bridge; R2 resolution law, Thm A; R3 visibility; R4 relative-trace law Δ; R5 stratification S | R1: restatement ("⟹ simple zeros" overclaimed; cyclicity is needed). R2: excluded by its own Thm A (see §1.2). R3: **P3 marks Thm C(iv)/D(b) unproved** for strip width `a < ½`, and P5 E-P5.8 says the "unconditional" clause of Cor D1 needs a CITED on-line density input (Selberg). R4: "finite split ⟺ RH" is EQUIV (Weil + von Koch–Landau). R5: Thm S is Mackey imprimitivity. Its atoms are installation |
| Motivic (B7) | R1 numerical motive `𝔐_Z`; R3 contraction wall | R1: restatement (M1 = Weil / CCM Cor 6.3). R3: excluded; Thm C is a third independent proof of the tail wall. Prop BL (`Z[Q/Z]`) is new to P4's knowledge. R2, R4, R5 were self-declared dead ends |
| Canonical systems (B8) | R1/R2 Nehari norms of Suzuki's kernel; R4 echo law | R1/R2: restatement (Herglotz/Lagarias; Landau-type growth law Thm G, correct). R4: excluded; Frobenius-local concatenated chains are excluded unconditionally at `r ∈ (½log3, log 2)`. For ζ alone the link is HEURISTIC |
| Function-field transport (B9) | R1 q→1 closure = Bochner cone; R2 Bombieri–Stepanov transport; R4 F–V rebalancing on E×E; R5 theta pull-backs | all restatements on the Spec Z side. The admissibility of the transported cone is ⟺ RH (Thm 5(iv)); `𝔗_ζ ≥ 0` is Weil's criterion, and on primitives it is row D verbatim. Function-field theorems are correct (RH is known there) |
| Probabilistic ladders (B10) | R1 Cauchy damping; R2 Gaussian heat ladder, `ε_G ≤ 1` | restatement. `RH ⟺ ε_G = 0` is Weil's criterion through a PD semigroup. The proved rungs are RH-silent (OT-4 fails), and Thm 6 reads verified zeros. R3–R5 (Koopman power law, phase–power law) were self-declared dead ends |

### 1.2 The one structural picture G1 converged on (the wall, as a synthesis)

Four memos (B2, B4, B5, B7) proved the same theorem independently. B3 proved a weaker variant. **Tail-factorizable
Frobenius carries at most one critical zero per summand.** Its sharp form is B4's W♯: at most one joint eigenvalue
per summand whenever `Σ_p ‖S_p‖^{-2} = ∞`. This covers the degree bound `‖F_p‖ ≤ Cp`, and the threshold is sharp by
Prop Σ.

The following results add to this wall:
* B4 R/R′: no algebraic (`Q̄`) structure;
* B5 Thm K: covariant flows have `log N`-stable spectrum;
* B6 Δ/S: canonical operator-algebra functionals have absolutely continuous flow spectrum, so atoms are installed;
* B3/B1/B2 DK_α results: flat leaves at finite trace, ergodic carriers carry at most one pair, closed orbits μ-null.

Together they exclude, **unconditionally**, every carrier class in which the zeros would come out of prime-local data:
- prime-local;
- tail-factorizable;
- algebraic;
- covariant;
- finite-trace conformal;
- ergodic conformal;
- canonical crossed product.

In each class the zeros enter only by installation, which is Lemma T(⇐) and fails OT-3/OT-4.

Consequence (HEURISTIC, but supported by all the walls): **an OT-5′ object must be "infinitely entangled across
primes" (N-e) *and* non-algebraic *and* non-covariant.** This is exactly the region where no candidate is known. The
only object on record in that region, the adèle class space, has an RH-equivalent trace formula (A17).

### 1.3 G1 results proposed for the record (to be re-audited before any paper)

These are **no-go theorems**. None carries a sign. Each was checked by at least three panelists, with the stated
caveats.

| item | statement (short) | label | caveat |
|---|---|---|---|
| G1_B4_R4 Thm W♯ | sharp tail wall, exact threshold `Σ‖S_p‖^{-2} = ∞`; Prop Σ sharpness | PROVED (PNT CITED) | §0 overstates the Rosati clause (E-P5.13); supersedes B3 Thm G, B2 Thm I, B7 Thm C |
| G1_B4_R5 Thm R/R′ | no zero is a joint Frobenius exponent on a `Q̄`-structure at ≥ 3 primes | PROVED mod CITED six exponentials | Cor FH is a list, not a theorem (E-P5.22) |
| G1_B6_R2 Thm A | on Construction 9′, `sup_{|s|≤T}‖U_s|H¹_w‖ ≥ (2n_w/πK_w)T − 1`, so OT-5′ (P-HS) is false there | PROVED, unconditional (5/5 checked) | a Kadec/Seip-type separation mechanism (P4) |
| G1_B6_R3 Cor D1 | modulation-invariant carriers have `sup_s‖U_s|H¹‖ = ∞` | PROVED **only** with the repair of P3 §5.2 plus the CITED Selberg density (E-P5.8) | P3: Thm C(iv)/D(b) unproved for `a < ½` |
| G1_B5_R3 Thm 1, R4 Thm K, R5 Thm E | Witt–Kronecker; covariant `log N`-stability; eigen-sector | PROVED | K5(a) false as stated; Thm G constant repaired (`1 − 2^{−β}`) |
| G1_B2_R3 Cor H; R4 Cor M1; R5 Thm R, Prop NH | prime-local operator carriers empty (Hardy); codim-one DK_α excluded; III₁ law | PROVED (Connes–Takesaki / Connes–Haagerup CITED) | R2 Thm E(i) in repaired form only |
| G1_B3_R5 Thm F, Thm E | flat wall at finite trace, `dim Ĥ¹ ≤ d`; `χ_Co = 0` | PROVED under (FT), (IBP), (R), (D) | hypotheses must be carried in the statement (E-P5.21) |
| G1_B1_R5 O1–O4 | Weil-number law at closed orbits; ergodic exclusion | PROVED under (C), (Def), (Sm)/(Orb) | Lemma 2.3 needs a co-closedness repair |
| G1_B8_R4 Echo Lemma E, Thm K | Frobenius-local chains excluded on `(½log3, log 2)` | PROVED mod CITED Romanov (F4) | the reduction for systems violating (L) is not written; the ζ-only link is HEURISTIC |
| G1_B9_R5 Thm G | O-37 closed on curves over `F_q` (theta pull-backs) | PROVED (function field) | says nothing new over Spec Z (Thm H = Weil) |
| G1_B9_R2 | correction of R157_002 row 29: the Bombieri–Stepanov closing is Landau, not rationality | PROVED/CITED | accepted 5/5; update the table |

**Withdrawn or false in this phase:**
- G1_B1_R3 Thm T(iii) / Cor T.1 (refuted);
- G1_B2_R2 Thm E(i) as stated;
- G1_B5_R4 Cor K5(a);
- G1_B6_R1 Cor 8.1(iii) "simple zeros" (needs cyclicity);
- G1_B6_R3 Thm C(iv) for `a < ½` (unproved).

---

## 2. G2: the mechanism

### 2.1 What was built, by angle

| angle | what was built | panel outcome and fatal step |
|---|---|---|
| Structure vs randomness (B1) | R1 centre identity `C_0 = −2ζ′/ζ(½)`, failure of the Selberg structured part at fixed `R`; R4 graded converse; R5 arithmetic resonators, Prop P | R1: excluded (modified comb; `cor:void`, F4). R4: restatement. R5: **excluded 5/5**. Prop P (positivity on `ℛ_M ⊂ P_T`) is class-level and holds for the deletion/amplification combs of `thm:finmod` and for `ζ·E`, so `cor:void` applies. Cor T2(iii) is EQUIV |
| Bootstrap in `T` (B2) | R1 exact annulus renormalisation; R2 sieve flow Ψ; R4 Thm U; R5 Lemma L, Thm I | R1/R2: restatement. The flow on the orbit `{Λ}` is the identity. By Prop Ψ4, any exact invariant is a functional of `ζ(½+it)` (E3). R4: `κ = 0 ⟺ RH`, and Thm U is conditional on the OPEN (BD). R5 not audited (§2.4) |
| Hermitian squares (B3) | R1 twist obstruction (Haar average = archimedean form; sign flip at 2 negative for `T ≥ 0.38`); R4 Landau converse | R1: excluded; no square is built, but Thms A/B/C are correct obstructions. R4: restatement (Landau's one-sided ψ). R5 not audited |
| SOS / Positivstellensatz (B4) | R1 covariant SOS = zero-side SOS; Baker no-go; R2 Theorem R (fixed edge profiles) | R1: excluded (S3 depends on its own Def S3.1). R2: excluded by own Thm R; the free branch is `thm:Zexh`/`cor:RH` = EQUIV. R3–R5 not audited |
| de Branges window time (B5) | R1 canonical system with `H ≥ 0` up to `T*(λ)`; R4 Gram converse | restatement: `T*(0) = ∞ ⟺ RH` is `thm:KEP3(b)` (Suzuki's programme) |
| Finite/random zero universes (B6) | R2 Theorem M: `λ^W_T ≤ λ^P_T ≤ λ^A_T ≤ exp(−e^{(2−ε)T})`; R4 BRS uniqueness, Thm P | R2: excluded as a mechanism (premise 2 / `thm:finZ`). **Thm M is PROVED and unconditional**, and P4 finds it **not in Zhu 2608.24827**: a genuine sharpening of `thm:margin`. R4: correct modulo Lemma S; β-blind (F4) |
| Almost periodicity / Kronecker (B7) | R1 Bohr–Jessen twist; R4 one-generator rigidity via Li–Radziwiłł | R1: excluded (∀T positivity is Haar-null on the twist torus; Thm C is Wintner 1944). R4: rigidity on the fibre over Λ, and the decisive input is zero-side (violates premise 3) |
| Lee–Yang / Pólya–Schur (B8) | local certification, Theorems L, L′, L″, D | **never audited by the panel** (§2.4) |
| Jump calculus (B9) | R2 rigidity at `T = ∞` (Thm R, under RH); R3 Thm R′ unconditional, Thm N; R4 doubling inequality | R2/R3: restatement. The only ∀T statement is `RH ⟺ (Λ+ℓ¹_w)∩𝒮^A ≠ ∅` (EQUIV). Thm R′ is correct and unconditional. R3 Remark 3.4 is invalid as written (relabel OPEN) |
| Mollifiers (B10) | Levinson–Conrey; Jensen identity; R5 Thm Γ_f, Thm H | **never audited by the panel** (§2.4) |

### 2.2 The one structural picture G2 converged on

**The graded Weil converse** was proved at round 4 by B1, B2, B3, B5 and B9, with B10 a sixth copy. Its content:
`λ^A_T ≥ −Ce^{κT}` forces `Θ − ½ ≲ κ`, with a sharp exponent. All panels agree that it is PROVED and that its ∀T target
`κ = 0` is **EQUIVALENT to RH** (von Koch–Landau). It is a record lemma, not a mechanism.

Together with the following, it shows that the ∀T arrow cannot be reached by any argument that:
* is class-level (`cor:void`, re-confirmed by B1_R5);
* is twist-covariant (B3_R1);
* is a fixed or resolving SOS rule (B4_R2, and R3–R5 unaudited);
* uses a proportion-of-zeros input (B10_R5 Thm H, unaudited);
* uses a separated arithmetic/archimedean square (B3_R5, unaudited).

Theorem M (B6_R2) also shows that the per-window margin is doubly exponentially small. So "decidable per window"
(`prop:finite`) is, for large `T`, a statement about precision `exp(−e^{2T})`.

### 2.3 G2 results proposed for the record (to be re-audited before any paper)

| item | statement (short) | label | form |
|---|---|---|---|
| G2_B6_R2 Thm M, Cor M1–M2 | `λ^A_T ≤ exp(−e^{(2−ε)T})` unconditionally (Nyquist-lattice annihilation plus Gevrey tail); replaces `thm:margin` for large `T` | PROVED, unconditional (checked by 4 panelists) | both |
| graded converse (B2_R4 Lemma T/Thm G1 as the cleanest proof; B1 Thm Q, B3, B5, B9) | `λ_T ≥ −Ce^{κT}` ⟹ `Θ ≤ ½ + O(κ)`, sharp exponent | PROVED; target EQUIV | both |
| G2_B2_R4 Thm U | two-sided growth law `κ^A = κ^W = Θ − ½` | PROVED **conditional on OPEN (BD)** | both |
| G2_B3_R1 Thms A, B | twist Haar average = archimedean form; sign-flipped ζ has a negative complete form for `T ≥ 0.38` (explicit witness) | PROVED | both |
| G2_B4_R2 Thm R | fixed/convergent edge-profile certificates fail for arbitrarily large `T` | PROVED, unconditional | [compl] |
| G2_B9_R2 Cor R1; R3 Thm R′ | rigidity of jump weights; the two arrows of Weil's criterion are asymmetric under summable perturbation | R′ PROVED unconditional; R2 Thm R PROVED under RH | both |
| G2_B6_R4 Thm P, Cor P2 | uniqueness of the explicit formula among combs on `±log N` (BRS dual) | PROVED mod Lemma S (B6_R5 claims Lemma S closed, **unaudited**) | [compl] |
| G2_B7_R4 Thm P | one-generator rigidity on the fibre over Λ | PROVED (Li–Radziwiłł CITED, checked in the primary text) | [compl] |

### 2.4 Audit gap (must be closed before any of these enters a paper)

The panels did **not** review the following memos:
* G2_B8 in all rounds and G2_B10 in all rounds;
* G2 round 3 except B9;
* G2 round 5 except B1;
* several G1 memos that were self-declared dead ends: B1_R1–R2, B3_R2–R3, B4_R1–R2, B5_R1–R2, B7_R2/R4/R5, B8_R3/R5,
  B9_R3, B10_R3–R5.

Their claims are **self-labels only, not panel-checked**. The most substantive unaudited claims:
* **G2_B8_R5 Thm L″**: the Euler-factor-local certification threshold satisfies `½log3 ≤ T_loc ≤ 0.5925`, with the
  upper bound machine-verified but **not interval-certified**. rule: numerics must be certified before recording.
  Thm D (minimax duality) is PROVED per the memo.
* **G2_B10_R5 Thm Γ_f**: a two-sided growth law for arbitrary zero sets. **Thm H**: Davenport–Heilbronn and Epstein
  `Z_Q` defeat any "proportion ⟹ sign" argument.
* **G2_B2_R5 Lemma L / Thm I**: a Lorentzian zero identity, and the window form of Bombieri's 2000 index theorem
  (CITED; the proof is independent).
* **G2_B3_R5 Thm S / Cor S1**: no separated square at any `T > 0.74921`, although Zhu gives positivity on
  `(0.74921, 0.8]`.
* **G2_B4_R5 Thm RN**: every resolving certificate rule fails at all large `T`.
* **G2_B5_R5 Thm Q♯**: no recovery windows when Θ is attained.
* **G2_B6_R5 Thm X**: Λ is an extreme point of the ∀T-positive fibre.
* **G2_B7_R5 Lemma C / Thm M**: Cesàro progression projection.
* **G2_B9_R5 Thm S / Thm L**: exact resummation, and a conditional log-absorption bound.
* **G1_B7_R4/R5**: genus law.
* **G1_B10_R4**: Koopman power law, citing Li–Radziwiłł.

None of them claims a sign, and none claims the objective.

---

## 3. Honest verdict

1. **G1: not achieved.** Of roughly 30 scored submissions, none was scored as an object by any panelist. Every
  positive-looking "OT-5′ holds" was one of two things: a redefinition (B3_R1), or an equivalence with RH carried by
  OT-2 or by admissibility (B6_R1, B8, B9, B10). Every carrier actually constructed was killed by its own memo's
  theorem: `H¹ = 0` after suspension (B2 R1/R2), Thm A (B6_R2), or installation (B4, B5, B6_R5). The wall of §1.2 is
  the main output.
2. **G2: not achieved.** No mechanism was produced. Every positivity statement found is either class-level (B1_R5
  Prop P, which is killed by `cor:void`) or conditional on RH. Every ∀T statement is EQUIVALENT to RH: `cor:RH`,
  `thm:KEP3(b)`, von Koch–Landau, or `κ = 0`. The one new quantitative fact, Theorem M, points the *wrong* way for a
  mechanism: the margin is `exp(−e^{2T})`.
3. **Premises.** All three premises of record were respected and remain in force. No memo that the panel audited
  contradicts `thm:finZ`. No sign beyond `T = 0.8` was claimed or found.
4. **Process.** A large part of G2 (B8, B10, and most of rounds 3 and 5) was never audited. The results table of §2.3
  and the list of §2.4 must go through a dedicated audit round before any paper integration, under the rule
  "check against the paper's own definitions" (feedback ). No paper or README was edited in this phase.
5. **Recommendation (HEURISTIC).** The two fronts have reached the same boundary from two sides:
  * G1: the object must be entangled, non-algebraic and non-covariant;
  * G2: the argument must not be class-level, twist-covariant or resolving, and it must use the Euler product after
  any counting step.

  Repeating either front with the same angles will reproduce the walls. A further phase is justified only with a
  genuinely new ingredient that lies outside every class excluded above. Such an ingredient must be checked against
  R157_002, R158_004 and this synthesis before it is built.

---

## 4. Summary

Neither of the two goals of phase 159 was achieved. The five panels confirm this unambiguously. In G1 (the
object) no candidate was accepted as an object by any panelist. The best score was 1/5, three times, and
always as a "negative structural result". Every carrier that was built died by its own theorem:
suspension gives `H¹ = 0`, Theorem A of B6 excludes it, or the zeros only enter "installed". What G1 did
leave is a proved, unconditional wall. Four memos proved it independently, and its
strongest form is W♯ of B4, with exact threshold `Σ‖S_p‖^{-2} = ∞`. Added to it are the rationality wall (six
exponentials), the Witt–Kronecker theorem, and the stratification law. Together they exclude every carrier that is local at
primes, factorizable in the tail, algebraic, covariant, or finite-trace conformal. An OT-5′ object, if it exists,
would have to be infinitely entangled across primes and be neither algebraic nor covariant, and there is no
candidate there. In G2 (the mechanism) nothing beat 0/5. Every "for all T" statement turned out equivalent to RH (von
Koch–Landau, `cor:RH`, `thm:KEP3(b)`, `κ = 0`). Every positivity found is class-level, so `cor:void` kills it,
or it is conditional on RH. The strongest new result, Theorem M of B6 (`λ^A_T ≤ exp(−e^{(2−ε)T})`, unconditional,
not in Zhu), says that the per-window margin is doubly exponential: it points against a mechanism, not
for one. Nothing is still proved for `T > 0.8`, and `thm:finZ` still stands. Moreover, an important part of G2
(B8, B10, and almost all of rounds 3 and 5) was never audited. Those results are only self-labels and need an
audit round before entering any paper. My honest recommendation is not to repeat the same angles
and to open another phase only with a genuinely new ingredient, outside all the classes excluded here.
