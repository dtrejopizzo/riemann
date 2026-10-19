# R185_005B — Relative barrier theorem BR, rewritten with no equivalence (editor)

**Preliminary note.** This file replaces, for all subsequent use, R185_005 §2–§3 (which is **not edited**; it remains as
historical record). Reason: the R186_114 audit (item 3, MAJOR outside the goal) detected that the "Conclusion" of
R185_005 §2.1 invokes an equivalence between row D and another statement. It is rewritten so that every step is
proved only from D (W_T ≥ 0 on 𝒫_T for every T of the declared carrier), its internal reformulations (CITED) and its
falsifiers, with no equivalence between D and another statement invoked. Where a step cannot be rewritten this way, it
is marked **RETIRED** and the conclusion that depended on it drops to **OPEN**. No new mathematics except the
incorporation of R186_037 (ρ1′ → ρ1‴). Paper 47, the grid and the crossword are not touched. Row D: OPEN.

Sources read in full: R185_001, R185_003, R185_004, R185_005, R185_091, R185_092, R185_093, R186_037, R186_114 §3.2 and §5;
R166_802 §0–§1 (framework).

Labels: PROVED, CITED, CONDITIONAL[on X], OPEN, ARGUED, RETIRED.

---

## 0. Inventory: where the equivalence or the E1 label appears in R185_005 and its lemmas

### 0.1 As a LOGICAL STEP (affecting the conclusion)

| location | text | use |
|---|---|---|
| R185_005 §2.1 Conclusion | "the conjunction over all π … is D, and D is equivalent to RH on the declared carrier (cluster E1, I1)" | the only step that turns "not weaker than D" into "not weaker than RH". **RETIRED** |
| R185_005 §2.1 (b) + R185_004 U3(ii) | "the exclusion is RH unchanged"; "Ex(K_j ∧ window) ⟺ ζ has no zeros at σ > ½" | translates the exclusion over {ζ} into a zero statement and names it; rewritten in terms of D (§2(b)) |
| R185_005 §2.1 (c) final sentence | "it is false, or it is RH, or it is stronger than RH" | classifies by comparison with RH; rewritten with D (§2(c)) |
| R185_005 §2.4 item 3 | "the family ∀π is equivalent to the absence of every witness, i.e. D, and D ⟺ RH (I1)" | same step as the Conclusion. **RETIRED** |
| R185_005 N-I tree (ii) | "I1 gives D ⟺ RH, used in the 'Conclusion'" | same step. **RETIRED** |
| R185_005 N-U2 tree | "R184_016 … (A1 E1 with the selector)"; "RH ⟹ A1 in Reg⁺"; "⟺ CONDITIONAL" | the whole node classifies the selector by E1; it only served the phrase "weaker than RH". Not needed in §2: **RETIRED** as a tree node; the selector problem remains recorded with no label (ρ3) |
| R185_004 Cor 6 / §5, U3(iii-c), (iii-b) | "the exclusion is equivalent to RH"; "implies RH and is a priori stronger"; "subsystems … give RH" | comparison with RH in the class remark; rewritten as comparison with the zero statement **of ζ** without naming it (§2(c)); does not affect the D tree |
| R185_002 Thm F "⟹ E1"; R185_004 U3(i) "⟹ E1" | already ARGUED (R185_091 M4, R185_092 F1) and **not used** in R185_005 (replaced by N-a3) | omitted; the PROVED core is preserved |

### 0.2 MENTION ONLY (not steps; removed or reformulated in terms of D)

- R185_005 header and R185_001/003 §"State": "RH is not asserted." Removed: the goal statement is D.
- R185_005 §1.3 (O3): "EF is the external datum that turns anything into literal RH (I4, I5)" → "into a question about
  the zeros of ζ alone" (Obs 4 of R185_004, PROVED).
- R185_005 §3(ii): "(TC) on the witness is RH (R164 README)", "zero-free strip = RH (I6 Thm 4)", "W11 says the coupling …
  is RH." Map mentions; in §3 of this file they are cited only as OPEN / outside 𝔐, without the comparison.
- R185_003 §0 ("trivial E1" as motivation for reading exclusion about proofs) and §4 ("selector … labeled E1");
  R185_003 Thm 1 and R185_001 Thm 6 use none of it. R185_003 §3 (ρ1″): "(TC) on the witness is RH", a mention, not an
  implication (R185_092 m3).
- R185_001 §5: "Can a zero statement … be 'weaker than RH'?" — a discussion; it enters no theorem.
- R185_091 M4, R185_092 F1: downgrade "⟹ E1" to ARGUED; their positive content (core of Thm F, N-a3) uses no E1.
- R185_093: reviews R185_006–008 (W11-∞ "⟹ RH" as a remark after cor:RH); does not bear on BR.
- R166_802 C1/C2 ("von Koch ⟺ RH", "O-bound ⟺ zero-free"): framework comments; the Thm 0–3 cited here concern Tail_K,
  Z_K(Σ_ζ) and the exponent Θ − ½ (a zero-side quantity, not an equivalence).

### 0.3 Falsifiers (R186_114)

BR does not depend on M_m or on f_t at any step: they appear only in the class remark of (c) (M_m is not discrete,
R185_092 M4(2)) and in citation I11 of §3. Where I11/(★_cell) with f_t is cited: CONDITIONAL[on f_t's primitive
witness, (Z-strip)/Cor F].

---

## 1. Framework and class 𝔐 (no content change relative to R185_005 §1; vocabulary only)

- **Goal statement D:** W_T ≥ 0 on 𝒫_T for every T of the declared carrier (ROW-D-REDUCED-STATEMENT). Internal
  reformulation CITED: D ⟺ "there is no first-contact witness" (R166_802 §1; Paper 47 lem:contA, prop:witness). A
  witness has type T_c, G = F̂ real-rooted, G ≢ 0, and parameters π = (t_q, G) with t_q = γ_q − iδ_q, 0 < δ_q < ½
  (hypothetical quadruple; Paper 47 prop:witness, CITED). Nothing further is assumed about the zeros.
- Admissible tests 𝒦 (K continuous, K ≥ 0 on ℝ, type ≤ Δ_max, Ψ = G²K admissible for Weil); exact identity (1.1)
  Z_K(Σ) = 𝔄_K − Tail_K(λ), linear in K (checked against eq:nuw, R185_091 m5); Z_K = Q_K + R_K + O_K, O_K ≥ 0.
- Models of the remainder: (M1) R_K ≥ −S_K test by test, witness set O_U, U_K := 𝔄_K − Q^{hyp}_K + S_K; (M2) R ∈ 𝓡
  closed convex, relaxed set W₂ = 𝔄 − Q^{hyp} − 𝓡 − C̄ (R185_001 Lemma 4; scope R185_091 M2).
- Atoms L, D, C, Q_θ and the class 𝔐_Λ (R185_004 Def 5 with R185_092 M3, m7, m8). Proof scheme in 𝔐 = (1) P ∈ 𝔐_Λ,
  (2) 𝔉 ⊂ 𝒦 and its (1.1)'s, (3) O_K ≥ 0 + remainder information in (M1)/(M2), (4) inputs I1–I18 only through their
  shadow in (1)–(3). Transfer logic (R185_003 §0): the scheme holds for every λ′ ⊨ P, hence excludes π only if
  Sh_𝔉(P) ∩ W = ∅.
- Outside 𝔐: (O1) unbounded type; (O2) zero-side inputs; (O3) class properties with EF (in 𝒟, EF₁ alone identifies ζ:
  R185_004 Obs 4, PROVED, and then the question is about the zeros of ζ alone); (O4) joint sentences (Λ,Γ) or
  operator statements; (O5) atoms outside L∪D∪C∪Q (exhaustiveness ARGUED).

---

## 2. Theorem BR (rewritten)

**Definition (weaker).** For statements A, B, "A is strictly weaker than B" means B ⟹ A and A ⇏ B. Here B = D.
A scheme in 𝔐 "excludes every witness with the statement P" if, for every π, Sh_𝔉(P) ∩ W_π = ∅.

**Theorem BR.** Let a proof scheme in 𝔐 have sentence P ∈ 𝔐_Λ, true at ζ, in normal form ∨_j K_j, J₀ ≠ ∅ the disjuncts
true at ζ. Then:

**(0) Factorization through a test. PROVED.** If the scheme excludes the witness with parameter π, there exists
K*_π ∈ 𝒦 (in (M1) K*_π ∈ 𝔉; in (M2) K*_π = Σ a_iK_i ≥ 0 on ℝ, a finite combination) with
  Tail_{K*_π}(Λ_ζ) > U_{K*_π}  ⟺ (by true (1.1))  Z_{K*_π}(Σ_ζ) < Q^{hyp}_{K*_π} − S(K*_π),   (★_π)
and (★_π) is **false if the quadruple π is present** and the model's information about R is true (R166_802 Thm 2;
R185_003 Thm 1 (M1); Thm 2 / R186_037 Thm E (M2)). Scope: (M1) exclusion of O_U; (M2) exclusion of W₂ (relaxed).
Hypothesis in (M2): 𝓡 with coordinate-wise lower bounds (R186_037 Lemma D, Thm E; covers 𝓡 compact and convex
couplings), or ba(𝔉) functionals over 𝔉 bounded in sup (R186_037 Thm C). Residual: ρ1‴ (R186_037 §4) OPEN.

**(a) Deletion. PROVED.** If some K_j, j ∈ J₀, has only L and D atoms, there exists X with {ζ∖S}_{S ⊂ ℙ∩(X,∞)} ⊂ 𝒞_P
(R185_004 U3(i) core, Lemmas 1–2), and in (M1) exclusion of O_U is equivalent to ∃K ∈ 𝔉: E_K > U_K, with E_K the
power-contribution, invariant under deletion (R185_002 Thm F core, R185_091 M4). The zero-side reading is (★_π) by
(0) applied to Λ_ζ (N-a3 of R185_005), **not** via Λ_∅ (which does not satisfy (1.1)). In (M2), exclusion of W₂,
subject to ρ1‴.

**(b) Identification. PROVED.** If some K_j, j ∈ J₀, contains a C atom (with X_P ≤ X_W, R185_092 M3), then
𝒞_{K_j} ∩ {d ≡_{X_W} ζ} = {ζ} (R185_004 Lemma 3(e) + Lemma 1). Hence the arithmetic hypothesis K_j ∧ window leaves no
λ′ ≠ Λ_ζ to transfer over: the scheme has only (1.1) for Λ_ζ, O_K ≥ 0 and the remainder model, and its exclusion of
π is exactly (★_π) **for ζ and with no additional arithmetic hypothesis**. The remaining disjuncts only enlarge
𝒞_P and do not help exclude (R185_004 note 5). (This replaces "the exclusion is RH unchanged".)

**(c) Counting. PROVED (scope of (0)).** If every K_j, j ∈ J₀, is of type Q (with L/D), within ζ's (1.1) frame the
exclusion is covered by (0) with no falsifier (R185_092 M4(3)): there exists K*_π with (★_π), and R166_802 Thm 1/3
requires at that scale a tail bound of exponent strength δ_q = Θ − ½, where Θ := sup Re ρ (a zero-side quantity,
CITED Landau).
*Class remark, outside the D tree (not used in (★) or in the Conclusion):* for class Ex, θ_P > ⅓ is falsified with
BFdisc glued to ℕ ≤ X (R185_092 M4(1), sketch, to be checked atom by atom: (iii-a) OPEN-verification); for ℙ∖S with
p_k ≥ 2^{2^k}, the zeros of ζ_{𝒫′} at σ > ½ are those of ζ, so class exclusion adds nothing to that of ζ ((iii-b),
PROVED after R185_092 M5); θ_P ≤ ⅓ is OPEN ((iii-c), Paper 48 Problem 6): a positive answer contains the case ζ and
is a priori stronger than ζ's zero statement (R184_001 §3.1). M_m is not discrete and does not enter (R185_092 M4(2)).

**Conclusion (rewritten). PROVED relative to 𝔐, modulo the leaves of §2.3.** Let a scheme in 𝔐 exclude every witness
with P. By (0), for every π: P ∧ (1.1) ∧ [true remainder model] ⟹ (★_π) ⟹ "π is not present". The conjunction over π
is "no first-contact witness", which is D (internal reformulation, CITED §1). Hence
  P ∧ 𝔐-frame ⟹ D,
and P (with its frame) **is not strictly weaker than D**. By branch: in (a) and (c), the statement doing the work is
the family {(★_π)}_π, each member refuted by its own π; in (b), P adds nothing beyond ζ and the scheme reduces to the
(1.1) frame alone. In no case is a statement implied by D obtained that does not itself imply D.
**What is NOT asserted:** nothing about the strength of D relative to any other statement; nothing about the truth of
(★_π); no comparison with external conjectures. (The original phrase "strictly weaker than RH" is **RETIRED**; its
only support was I1, and it is not reconstructed.)

### 2.1 Statement (English, for Paper 48)

**Theorem (relative barrier, D-only form).** Let a proof scheme in the class 𝔐 exclude every first-contact witness on the
declared carrier through an arithmetic sentence P ∈ 𝔐_Λ, admissible tests 𝔉 ⊂ 𝒦 of type ≤ Δ_max, and remainder information
in model (M1), or in model (M2) with 𝓡 bounded below coordinatewise (or ba(𝔉)-functionals on sup-bounded 𝔉). Then for every
witness parameter π there is a single admissible test K*_π with
  Tail_{K*_π}(Λ_ζ) > 𝔄_{K*_π} − Q^{hyp}_{K*_π} + S(K*_π)  ⟺  Z_{K*_π}(Σ_ζ) < Q^{hyp}_{K*_π} − S(K*_π),
an inequality that fails whenever π is present. Moreover (a) if some disjunct true at ζ is deletion-closed beyond the window,
the exclusion is equivalent (M1) to ∃K: E_K > U_K; (b) if some disjunct true at ζ contains a completeness atom, the arithmetic
hypothesis leaves only ζ and the exclusion is the frame inequality for ζ alone; (c) if every disjunct true at ζ is of counting
type, the exclusion is covered by the factorisation and needs exponent strength Θ − ½ at the witness's scale.
Consequently P together with the frame of 𝔐 implies the absence of every witness, i.e. row D itself: **no scheme in 𝔐 excludes
all witnesses through a statement strictly weaker than D**, except possibly through the residues ρ1‴, ρ2, the unverified
gluing in (iii-a), the frontier θ ≤ 1/3 (class problem, outside the tree) and the exhaustiveness of 𝔐 (ARGUED).
In (M1) "exclusion" means of O_U; in (M2) of the relaxed set W₂.

### 2.2 Proof tree (only the nodes that change; the rest as in R185_005 §2.3)

```
BR (D-only form)  — PROVED relative to 𝔐, modulo ▲
├─ N0  (0): R166_802 Thm 0–2; R185_001 Lemmas 2–4, Thm 5(a), Thm 6; R185_003 Lemma 2∞, Thm 1   PROVED
│   ├─ N0.5 (M2): R185_003 Thm 2 (𝓡 compact) ⊂ R186_037 Thm E (coord.-wise lower bounds)      PROVED (W₂)
│   │        R185_003 Prop 3 (Radon) ⊂ R186_037 Thm C (ba(𝔉), 𝔉 sup-bounded)                  PROVED
│   │        R186_037 Prop G (finite dim., t_ζ ∈ cl W₂: non-strict factorization)              PROVED
│   ├─ ▲ ρ1‴  𝔉 infinite, 𝓡 with no lower bound at some test, 𝓡 + C̄ not closed; or ba with 𝔉
│   │         not sup-bounded (R186_037 §4, Example F)                                         OPEN (narrow)
│   ├─ ▲ ρ2   discrete witness set vs W₂ (zero-side input, outside 𝔐, O2)                     OPEN
│   └─ ρ3     uniformity of K*_π in π: not needed for (★_π); producing π ↦ K*_π from Λ
│             is a recorded OPEN problem, with no classification label                         recorded
├─ N-U2  [RETIRED as a node: classified the selector by E1 (R184_016/094). Not used.]
├─ N-U3  (a)(b)(c): R185_004 Lemmas 1–3, Obs 4, Prop 0; U3 core (corrected Def 5)              PROVED
│   ├─ N-a3 zero-side reading via N0 at Λ_ζ (not Λ_∅)                                          PROVED (M2: ρ1‴)
│   ├─ N-b  Lemma 3(e)+Lemma 1 ⟹ 𝒞 ∩ {≡_X ζ} = {ζ}; "frame only" reading (§2(b))               PROVED
│   └─ N-c  circularity = N0 + R166_802 Thm 1/3                                                PROVED (scope N0)
│        class remark: (iii-a) sketch to verify; (iii-b) PROVED; (iii-c) OPEN                  outside the tree
├─ N-D   "no witness ∀π" = D (Paper 47 lem:contA, prop:witness; R166_802 §1)                   CITED
├─ N-I   I1–I18 cited only through their shadow in (1)–(3); I1 is NOT used; I11 with f_t:      CONDITIONAL[(Z-strip)/Cor F]
└─ ▲ N-EX  exhaustiveness of L, D, C, Q and I1–I18                                             ARGUED
```

### 2.3 Open leaves (state after R186_037 and this rewrite)

| leaf | statement | state |
|---|---|---|
| ρ1‴ | (M2) with 𝔉 infinite, 𝓡 with no lower bound at some test and 𝓡 + C̄ not closed, t_ζ ∈ cl W₂ ∖ W₂ unsupported; or ba(𝔉) with 𝔉 not sup-bounded | OPEN, narrow; still a zero-side statement (R185_003 Thm 6∞) |
| ρ2 | exclusion of the discrete witness set, not of W₂ | OPEN; outside 𝔐 (O2) |
| (iii-a) | BFdisc ∥ ℕ ≤ X gluing satisfies the remaining L/D atoms | OPEN-verification (sketch R185_092 M4(1)); not a D leaf, only a class one |
| (iii-c) | discrete systems with θ ≤ ⅓ and a zero with β > ½ | OPEN; class problem, outside the tree |
| N-EX | exhaustiveness of 𝔐 | ARGUED; refuted by exhibiting an atom outside L∪D∪C∪Q |
| ρ3 | selector π ↦ K*_π from Λ | OPEN recorded; unclassified |

### 2.4 Dependency check

1. (0) uses only t_ζ ∈ Sh(P), true (1.1) for ζ, and the remainder model; nothing about other statements.
2. "(★_π) false if π is present" is R166_802 Thm 2: substitution in the true identity with Q_K = Q^{hyp}_K and
   R_K ≥ −S_K. It uses no property of ζ's zeros beyond Weil admissibility (Σ_ρ|G(t_ρ)|² < ∞, R185_091 m4).
3. "Conjunction ∀π = D" uses only the definition of first-contact witness and lem:contA/prop:witness (CITED,
   internal to D).
4. No step uses R184_016/094, I1, I4–I6 or W11 as premises. I11 appears only in §3 (CONDITIONAL by f_t).
5. The branches of R185_005 whose content depended on the retired sentence: only the "Conclusion" (and its echoes in
   §2.4.3 and N-I(ii)). No lemma loses its PROVED label; only what the conclusion asserts changes (D instead of RH).

---

## 3. Consequences (mandatory vocabulary: "relative to 𝔐 (Def §1)", never "absolute barrier")

- **BR is a barrier relative to 𝔐.** It says: every exclusion obtainable with 𝔐's inputs factors through (★_π) and,
  over all π, is D itself. It does not say D is unreachable, nor does it compare D with anything external.
- **The positive program lies outside 𝔐:** (O1) unbounded type — (TC), (★_cell): OPEN, no implication asserted
  (R185_092 m3); (O2) zero-side inputs with Euler — ρ2, (Dom_θ), (P_gap); (O4) joint statements (Λ,Γ) and operator
  objects (W10, MW-5, h⁰); (O5) new atoms. The live arithmetic box remains O166.802.1 ≡ S2 of Ω (R186_032 §4,
  R186_037 §5).
- **Units for Paper 48:** Thm U3 + Def 5 (core), Lemma 3/Obs 4 (W-identification), BR in the D-only form of §2.1. The
  phrase "no scheme … weaker than RH" from R185_005 §2.2 and from DRAFT_SECTION_INERTIA_BARRIERS (CROSSWORD l.646)
  must be replaced by §2.1 of this file before any integration.

---

## 4. Final table: original step → state after the rewrite

| R185_005 step | state after rewrite | grid §3 (BR wall) | crossword |
|---|---|---|---|
| (0) factorization, (M1) | PROVED (unchanged) | unchanged | unchanged |
| (0) factorization, (M2) | PROVED for W₂ with 𝓡 having coordinate-wise lower bounds / sup-bounded ba(𝔉) (R186_037); leaf ρ1′ → ρ1‴ | leaf "ρ1′" → "ρ1‴ (narrow, R186_037)" | ρ1′: "OPEN" → "closed except for ρ1‴" |
| (a) deletion, core and N-a3 reading | PROVED (unchanged); "⟹ E1 via Λ_∅" ARGUED and unused → no longer mentioned | unchanged | U3(i): remove the "E1" label; core PROVED |
| (b) identification | PROVED, reformulated: "the exclusion is RH unchanged" → "P leaves only ζ; the exclusion is (★_π) for ζ with no arithmetic hypothesis" | wall text: replace the sentence | U3(ii): same |
| (c) counting | PROVED (scope of (0)); sentence "false, or RH, or stronger than RH" → "false if π is present, or with strength Θ − ½" | no symbol change; text | (iii-a) OPEN-verification; (iii-b) PROVED; (iii-c) OPEN class |
| Conclusion "not weaker than RH" (via I1) | **RETIRED** the step D ⟺ RH; conclusion rewritten "not weaker than D": PROVED relative to 𝔐 modulo ρ1‴, ρ2, N-EX | entry 21 (log) and §3 BR wall: "strictly weaker than RH" → "strictly weaker than D"; leaves: ρ1‴, ρ2, (iii-a), (iii-c), N-EX | §4.2: same replacement; item 7 (barrier theorem) with the D-only form |
| §2.4 item 3 "D ⟺ RH (I1)" | **RETIRED** | — | — |
| N-I (ii) "I1 gives D ⟺ RH" | **RETIRED**; I1 is not used | — | — |
| N-U2 selector (R184_016/094, "A1 E1") | **RETIRED** as a node; ρ3 recorded as an unclassified OPEN problem | remove "U2: sandwich E1" from the wall; leave "selector: OPEN" | U2: "sandwich E1" → "OPEN (produce K*_π from Λ)" |
| §3 citation I11 with f_t | CONDITIONAL[on f_t's primitive witness, (Z-strip)/Cor F] (R186_114) | already annotated by R186_114 | same |
| §3 mentions "(TC) is RH", "zero-free strip = RH", "W11 … is RH" | removed (mentions; not steps) | text: leave "(TC) OPEN", "outside 𝔐" | same |
| Exhaustiveness of 𝔐 | ARGUED (unchanged) | unchanged | unchanged |

**What does NOT change:** no grid symbol; no lemma label (every PROVED of R185_001/003/004 is preserved);
D OPEN. **What changes:** BR's conclusion goes from "nothing strictly weaker than RH" (resting on a forbidden step)
to "nothing strictly weaker than D" (resting only on (0) + the definition of witness), with leaf ρ1′ replaced by ρ1‴
and node N-U2 retired. No downgrade to OPEN of the main conclusion was necessary: the only unrewritable step was the
comparison with RH, and the goal's target conclusion does not require it. No contact with the sign.
