# The row D crossword — complete dependency graph

> **Closed record.** This document keeps its structure for reference and receives no further entries. Everything attempted, including the content of this document, is consolidated in `05-meta-and-planning/ROUTES-MASTER-INDEX.md`, the only place where new attempts are recorded.

**Status: row D OPEN. The closure of D is not claimed. No label in the record changes.**

> **Note (author's premise).** §0–§1 were rewritten in D-only form following the
> model of `03-research/phase-185-crossword/R185_005B_BR_WITHOUT_EQUIVALENCE.md`, and in §2–§5 and in the addenda the
> same line-by-line substitution was applied: row D (W_T ≥ 0 ∀T on the declared carrier) is the only
> target statement; no equivalence of D with any external statement is invoked, reasoned from, or mentioned, and the
> label "E1" does not exist as a criterion. The old label "E1" is replaced by **REF-D** (internal
> reformulation of D: equivalent to D by a theorem of the programme, CITED or PROVED); the old "cluster E1" is the cluster of
> reformulations of D; "⟺ RH" becomes "⟺ D", "under RH" becomes "under D (no witness)", "¬RH" becomes "¬D (witness exists)". All
> the mathematics about D (statements, sources, labels, arrows, falsifiers, walls) is preserved. Nothing here
> labeled REF-D is closed by that label. The only
> consequence for the record: the phrase in §4.2/§5 "barrier theorem … weaker than RH" has already been replaced by the
> D-only form of R185_005B §2.1. Original text: git history.
Working document. Pure mathematics, no new numerics and no web. Each node cites its record file, and each
label is copied from the record without promoting it. When this document adds its own reading, it is marked **[reading]**.

Sources read: Paper 48 (`04-papers/48-row-d-route-map/main.tex`: §sec:walls, §sec:spec complete, Concluding remark,
tab:tools); `ROW-D-REDUCED-STATEMENT.md`, `SIGN-REAUDIT.md`, `SUPPORT-DESCENT-TEST.md`;
R163_401_v9 (gap box, 4.8), R163_801 Thm 5, R163_901 Thm F; R164_000 (TC); R165 (in Paper 48); R166_190, R166_501,
R166_802; R167_101 (in Paper 48 and R169); R168_102, R168_103, R168_190; R169_000 v2 (+ R169_091); R183_024 §2.5, R183_031,
R183_033; R184_001, 003, 004, 005, 008, 011, 014, 015, 099; grid R162_2300 §3, §4, §7; NO-GO-LIST §V, §VII.

Labels: **PROVED**, **PROVED-CITED**, **CONDITIONAL[on X]**, **ARGUED**, **OPEN**, **REF-D** (internal reformulation
of D, equivalent to D by theorem; not a closure criterion), **NO-GO** (excluded by theorem), **FALSE**.

Notation: W_T is the complete Weil form on L²(I_T), I_T = [−T,T]. 𝒫_T are the primitive tests (Φ_F(0) = Φ_F(1) = 0),
𝔞_T the primitive form, λ^W_T and λ^A_T their respective minima. T_c is the hypothetical first contact, F the real-rooted witness,
G = F̂, X the set of nodes, X_c = e^{2T_c}, and t_q = γ_q − iδ_q the lowest quartet. m is the number of quartets off
the line, Θ = sup Re ρ. The falsifiers are those from the Paper 48 table and from grid §4.

---

## 0. One-screen summary

```
                         ┌──────── REF-D CLUSTER (reformulations of D, all ⟺ D) ────────┐
                         │  D: ∀T W_T ≥ 0 ⟺ ∀T λ^A_T ≥ 0 ⟺ thm:Z ∀T ⟺ D-4/D-5           │
                         │  ⟺ Kreĭn ∀T ⟺ Hodge (D-6) ⟺ CL ⟺ (★_cell)@witness             │
                         │  ⟺ (TC) ⟺ N(T)≡0 ⟺ Q (R184_015) ⟺ {P_loc} ⟺ q_E=0             │
                         └───────────────────────▲────────────────────────────────────────┘
          (not ⟺ D; S11)                         │
   O2601.1 ──► C_B ──┐                           │
                     ├──(∧ L8)──────────────────►│  D ⟺ C_B ∧ L8
   L8 (sup N<∞) ─────┘                           │
   [D] decorrelator 𝓘_X ∀X ─┐                     │
   (Dom_θ) ─────────────────┼─(∧, on the PROVED chain of R169 §1)─►│
   (P_gap) (regime y≪1) ───┘                     │
   P_src ─────────────────── Prop 1 (PROVED) ────►│   but Thm 2: blind to M_m or REF-D
   ∀T C_T ─────────────────── Prop 2.5 (PROVED) ─►│   but C_T ⟹ D and is probably false
   BF^disc_{θ₀}, θ₀∈(0,⅓] ── (logical) ──────────►│   and moreover ⟹ quadratic GRH (stronger than D)

   Pure Beurling layer (does not touch ζ):  C1 ⟹ [C2 ⟺ ¬D];  (ZF_R) ⟹ L*_comp;  BFdisc(⅓,½) PROVED
   Sonin/operator layer (no sign):  (M) ⟹ (M_w) ⟺ (E′_loc) ⟹ R'_S Hilbert–Schmidt;  (Q*) ⟺ (L-184.011) under D
```

**Verdict [reading].** No known theorem simultaneously satisfies conditions (α)–(θ) of §3.3. The condition that always fails
is (γ), the strength of (N′), and also (δ), the coupling with the archimedean place. The set (α)–(θ) is
logically consistent: if D is true (no witness), the bound in (γ) holds for ζ. But its two *proved* forms
as necessary, the single-test one and the power-size-family one (R166_802), are reformulations of D (REF-D):
that label does not rule them out, but they do not by themselves take a constructive step. The only blank cell that no
PROVED meta-theorem covers is that of the inequalities on Λ that are **non-linear and not of power-family type**: O166.802.1, which
coincides with O166.501.1 and O184.015b.

---

## 1. The root node and the cluster of reformulations of D (REF-D)

### 1.1 The root statement

**(D) Row D on the declared carrier** (Paper 46 §1; Paper 48 Def; R163_401_v9 Def 1.1):

> ∀T > 0: W_T(F) ≥ 0 for every F ∈ 𝒟_T (equivalently F ∈ C_c^∞(I_T)), and, in primitive form, ∀T > 0: 𝔞_T ≥ 0 on 𝒫_T.

D is the target statement and is not compared with any external statement. The only zero statements that enter are
those of the **witness**: a quartet off the line produces a negative direction in some window (Paper 46
`lem:roughEF`, `prop:witness`, `lem:contA`), so that D ⟺ "there is no first-contact witness" (internal
reformulation, CITED). Nothing else is assumed about the zeros.

### 1.2 The members of the cluster

All are ⟺ D (REF-D). The table gives the form, the source, and the nature of the equivalence **with D**.

| # | form | source | nature |
|---|---|---|---|
| D-1 | ∀T λ^W_T ≥ 0 | Weil; P46 §1 | definition of D |
| D-2 | ∀T λ^A_T ≥ 0 | P45 Thm 10.4; Bombieri 2000 (CITED) | global only: the per-window converse fails (`cor:convfail`) |
| D-3 | ∀T there exists a flat-top certificate, i.e. Σ_ρ ŵ(τ−γ_ρ) admits a one-sided smoothing ≥ 0 | P46 `thm:Z` | PROVED |
| D-4 | ∀T v_T = (2Λ(n)/√n)_{n<e^{2T}} ∈ 𝒱_T (closed convex set defined only by Γ) | P46 `prop:finite`, `prop:uniform` | PROVED; at fixed T it is a finite, decidable condition |
| D-5 | lim_T λ^A_T ≥ 0 | P46 `cor:margin2` | PROVED |
| D-6 | Hodge index on the adelic square | P47 §5 | PROVED |
| D-7 | ∀T the Kreĭn extension problem is indeterminate | P46 Thm 8.5 | PROVED; unconditional for T ≤ 0.8 via Zhu (CITED) |
| D-8 | CL (closure lemma) | R163_401 Prop 4.0 | PROVED ⟺ D |
| D-9 | (★_cell): on the witness, P_j > N_j in every cell C_j containing an off-line ordinate | R163_401 §4.8, Rem 4.8a | ⟺ D on the witness, circularly (Σ_j(P_j − N_j) = 0); §5: (★_cell) ⟹ D is PROVED conditional on 4.8 |
| D-10 | (TC), the tail theorem: C_{T_c}(x) − iG(x)²𝒯_X(x) has no poles with Im x ∈ (−½, 0) | R164_000; R163_801 Cor 3.1 | ⟺ no witness (Rem 4.8a) |
| D-11 | N(T) := n₋(W_T \| C_c^∞ ∩ 𝒫_T) ≡ 0 | R184_004 Prop 2; R162_2602 Thm 6 | PROVED |
| D-12 | Q: W_T ≥ −e^{o(T)} on 𝒫_T for all T ≫ 1 | R184_015 Thm 2(ii) | PROVED by the detection law |
| D-13 | the family of local positivities {P_loc(kL, T)} | R163_601 Thm 1, Cor 2 | PROVED (exact decomposition into cells) |
| D-14 | q_E = 0 (canonical exchange) | R163_001; Paper 48 §subsec:beurling | REF-D |
| D-15 | (L-C) ∀T; P_{C_T} with C_T free | R183_031 §3 | reformulation of D |
| D-16 | Lagarias/Herglotz: Φ(s) = Poisson factor × 2Re ξ′/ξ | Paper 48 W1 | classical |
| D-17 | "(2) holds at every first-contact vector" (support descent) | SUPPORT-DESCENT §2 | PROVED ⟺ D |
| D-18 | (WS*) in scale-uniform form | R167_101 Thm C (Landau) | equivalent to the absence of a witness (statement with no zeros off the line) |
| D-19 | P_form (‖W^X_T − Son_S‖ ≤ e^{o(T)}) | R184_015 Thm 2(ii) | P_form = Q ∧ U, Q ⟺ D |

(Correspondence with the earlier numbering: D-k = old E_k.)

### 1.3 Diagram of the cluster

```
   ∀T λ^W≥0 ══ ∀T λ^A≥0 ══ thm:Z ══ D-4 (v_T∈𝒱_T) ══ D-5 (lim λ^A≥0)
       ║            ║                     ║
   Kreĭn ∀T     N(T)≡0 ══ Q (W≥−e^{o(T)})      {P_loc(kL,T)}
       ║            ║
     Hodge     P_form ⊇ Q          (L-C)∀T ══ P_{C_T} free
       ║
   [witness]  CL ══ (★_cell)@T_c ══ (TC) ══ "no poles in −½<Im x<0"
       (everything in the "witness" row is vacuously true if there is no witness, and false if there is)
```

**Quantifier warning [reading].** The "on the witness" statements (D-8–D-10, (WS*) on the witness, (★_loc)) have
the form "for every hypothetical first contact, …". If there is no witness they are vacuously true, and if there is one they are equivalent to
the negation of the witness. That is why, as they stand, they are ⟺ D (REF-D). They cease to be so only when they are **strengthened** to a
statement without a witness, defined without zeros and perhaps false, such as 𝓘_X on all of Γ_S(F) (§2.4). That strengthening is what
S11 demands and what nobody has written. (This does not close D-8–D-10 as targets: they are reformulations of D and are attacked by their
constructive tractability.)

---

## 2. Intermediate nodes: those that are not ⟺ D

Each entry gives: (i) the statement; (ii) the status; (iii) the walls that apply to it; (iv) the falsifiers that satisfy it,
which explain why it does not imply D by itself; (v) what it additionally needs; (vi) the record file.

### 2.1 C_B — finite-multiplicity dichotomy
- (i) If m < ∞, then m = 0.
- (ii) **OPEN.** D ⟹ C_B is trivial (no witness, m = 0). The non-equivalence C_B ≢ D is NOT-REFUTED, but not proved (R184_004 §1.1(5)).
  By inertia, C_B ⟺ [sup_T N(T) < ∞ ⟹ N ≡ 0]; the ⟸ direction is CONDITIONAL on Weil/Yoshida (R183_031 Lemma 1.1(b), not
  verified in the source).
- (iii) W3, on the prime variable (R184_004 Cor 5). Thm H (R162_2601): atom + log-derivative + EF ⟹ cζ, so C_B has
  no class content. Also W-identification and the 2β* law (Problem 5 of Paper 48).
- (iv) M_m (0 < m < ∞) satisfies every class property, inertia property, and B_p block property; Λ̃ satisfies the "atomic
  comb ⟹ E = 0" version.
- (v) Needs O2601.1 to be proved and L8 to give D: **D ⟺ C_B ∧ L8** (R184_004 §1.1(1)).
- (vi) R162_2501, R162_2601, R184_004.

### 2.2 O2601.1 — individual Euler property
- (i) A property of the exact values of Λ, used non-linearly (Euler product), that forbids the a.c. part E
  among functions with atomic log-derivative.
- (ii) **OPEN, no candidate.**
- (iii) W3, Thm H, R184_004 Cor 5 (cannot enter via the B_p) and R184_015 Thm 2 (cannot be a norm bound on the remainder).
- (iv) Must fail for deletion, M_m, Λ̃ and for the conductor-q combinations, if any has 0 < m < ∞ (unknown).
- (v) Implies C_B. For D it additionally needs L8.
- (vi) R162_2601 §6; grid §7, ranking of part 8.

### 2.3 L8 — finiteness
- (i) sup_T N(T) < ∞, equivalently m < ∞ (κ < ∞).
- (ii) **OPEN.** It has Lindelöf strength or more: κ < ∞ ⟹ Θ < 1, and under A ⟹ LH (P33; R162_2501 §5).
- (iii) W2/M: the exponential law lim T⁻¹ log(−λ^A) = 2β* < 1 does not clash with the unconditional floor.
- (iv) M_m satisfies L8 (N → 2m).
- (v) Together with C_B it gives D.
- (vi) R162_2501, R184_004 Prop 2.

### 2.4 (WS*) and its witness-free version 𝓘_X
- (i) With w = (e^{−iγ_q·}g) ∗ ǩ, with transform G(s+γ_q)²k(s) ≥ 0, and Y = X e^{Δ}:
  Re Σ_{n≤Y} Λ(n) n^{−½+iγ_q} w(log n) < (1−θ) c_Θ |G(t_q)|² |k(−iδ_q)| − ¼E_K.
  The witness-free version (R169 v2) is: **𝓘_X: for every F in the image of the selector [S] at scale X and every (γ,δ) ∈ Γ_S(F),
  the same bound holds.**
- (ii) The chain of R169 §1, steps 1–4, is **PROVED**; step 4 holds given (Dom_θ). (WS*) is **OPEN**. At a single scale
  it is an evaluation of the explicit formula (R167_102 Thm E). In scale-uniform form it is the absence of a witness (REF-D).
- (iii) W-sieve (b_θ, Theorem S), (N′), A1–A12 of R169, and Theorem M (A12).
- (iv) At a fixed scale, 𝓘_X is a finite computation: the tail [X, Y] is the Eratosthenes sieve of the window because Y < X²
  (R169_091 corr. (2), PROVED). Hence no falsifier satisfies it "by class"; the infinite content lies only in
  ∀X, the master quantifier.
- (v) Additionally needs (Dom_θ) and, in the regime δ_q log γ_q < y₀, also (P_gap).
- (vi) R167_101–103, R167_291, R169_000/091.

### 2.5 (Dom_θ) (O167.101.1)
- (i) Domination hypothesis on the neighboring quartets in Thm B of R167_101.
- (ii) **OPEN.** It is technical.
- (iii) Theorem M if requested with slack.
- (iv) It is on the zero side, so M_m can satisfy it.
- (v) Only useful within the chain of §2.4.
- (vi) R167_101, R167_291.

### 2.6 (★_loc) and (P_gap) — the small-y regime
- (i) (★_loc): Σ(γ − x₀)² ≥ (32/9)(δ + Mε/|G′|)², with local counting. By R168_103 (PROVED, sufficiency), (★_loc) ⟹ the
  local form of (★_cell). (P_gap): for every off-line zero with δΛ < y₀ and γ* > H, the interval |x − γ*| ≤ c₁/Λ contains
  an on-line zero γ with |γ − γ*| ≥ c₂δ.
- (ii) **OPEN.** D implies (P_gap) vacuously (no witness). It is not proved to be equivalent to D.
- (iii) The wall dichotomy: it is an input on the zero side, so M_m violates it at will. W-jet. R168_203 Prop L4:
  the first Laguerre inequality does not detect quartets.
- (iv) There are M_m models with neighbors placed on purpose that satisfy (P_gap): **[reading]** that is why it alone does not imply D.
- (v) Needs (WS*) outside the small-y regime.
- (vi) R168_103, R168_190, R168_203.

### 2.7 BF^disc_θ below ⅓ (Problem 6, cell 5G)
- (i) Does there exist θ₀ ∈ (0, ⅓] such that every discrete Beurling system with N = ρx + O(x^θ), θ < θ₀, has all its zeros with
  Re s > θ₀ on the line Re s = ½?
- (ii) **OPEN** in both directions. For θ₀ > ⅓ it is **FALSE**: Thm BFdisc (R163_803, PROVED). A positive answer for
  any θ₀ > 0 ⟹ D (R184_001 item 10, logical PROVED) and ⟹ D ∧ quadratic GRH (R164_503). **It is stronger than D, not
  weaker.**
- (iii) ζ_θ (prop:analyticnogo): every analytic obstruction fails, so a proof must use integrality.
  Cor finitepert: the ℕ-comparable part is equivalent to D. Requirement (N): the count N is blind to the zeros.
  R184_008 Thm F: the factor route is NO-GO for every θ < 1.
- (iv) Its negation is realized by systems outside the Witt lattice, if they exist (O164.201a, O184.001a/b).
- (v) As a route to D it reduces nothing.
- (vi) Paper 48 Prob. 6; R163_803; R164_201/503; R184_001/008.

### 2.8 C1 and C2 (rigidity at θ = 0)
- (i) C1: every discrete system with N = ρx + O(1) is ζ·E, with E a finite Euler modification. C2: there exists a system
  with θ = 0 and a zero off the line.
- (ii) C1 in O(1) is **OPEN**. C1 in O(log x) and in O(x^ε) is **FALSE** (R184_005 Prop 4.1), but the counterexample is
  equivalent to D. **C1 ⟹ [C2 ⟺ ¬D]** (R166_701 T6, PROVED). If C1 fails, ¬C2 is stronger than ¬D.
- (iii) Requirement (N) and REF-D at the boundary θ = 0.
- (iv) ℕ ∪ √2ℕ refutes the set-theoretic version (N1), and root substitution is a rigidity falsifier.
- (v) It is pure Beurling theory and does not close D.
- (vi) R166_701, R184_005.

### 2.9 Theorem L*_comp
- (i) Every discrete system of the Witt lattice with θ < ⅓ has error ≫ x^{(1−θ)/2 − ε}.
- (ii) **OPEN** (B7). **(ZF_R) ⟹ L*_comp** is CONDITIONAL[on (ZF_R)], with the proof written out (Thm B.4). That L*_comp is equivalent
  to the class of R₀ being nontrivial in {tame R}/{bounded integer Euler products} is ARGUED (B6).
- (iii) B3 gives a counterexample in the relaxed class (R = L(u,χ)). By B4, the proof must use ε_p ≡ −p^a (mod 1): **
  integrality is indispensable**.
- (iv) L(u,χ) satisfies everything except integrality.
- (v) It is pure Beurling theory. It would promote to PROVED the "outside the lattice" statement of rem:onlynonident, which today is ARGUED.
- (vi) R184_014.

### 2.10 (M) and (M_w) — compactness of the Sonin remainder
- (i) (M) is a microlocal hypothesis on r_p. (M_w) is ∫|(μ_D − ρ_E) ∗ K|² ds < ∞.
- (ii) **OPEN.** (M) ⟹ (M_w), and (M_w) ⟺ (E′_loc) for T′ < T₀ (R184_003, PROVED). (E′_loc) ⟺ R'_S is Hilbert–Schmidt
  (R183_029 Thm C).
- (iii) W12 (sign-free identity) and R184_015 Thm 2: compactness does not give a sign.
- (iv) (M) "hides no zeros": it holds equally for any zero configuration with the same source.
- (v) To have a sign it would need P_src, which by Thm 2 is blind to M_m or REF-D.
- (vi) R183_029/033, R184_003.

### 2.11 (Q*) and (L-184.011)
- (i) There is no nonzero real tempered Dirichlet series B with Re B ≤ Re ξ′/ξ for Re s > ½.
- (ii) Under D (no witness), (Q*) ⟺ (L-184.011) (PROVED). Without D it is empty.
- (iii) W3 via the Type I curve.
- (v) It is NO-GO as a route to D.
- (vi) R184_011.

### 2.12 The gap requirement (R183_031 Thm 1)
- (i) If W = P_T + R_T with P_T ≥ 0 a multiplier of density ρ_T and n₋(R_T) ≤ N₀ for all T, then ρ_T → 0 in Landau
  measure away from the ordinates of the zeros.
- (ii) **PROVED** given 1.1(b) (CITED), and clean under D.
- (iii) It is a **consequence, not a mechanism**: under D it is satisfied by P_T = 0. By R183_031, "the gap property is
  not separable from D" (thm:Z).
- (v) A P_T that knows the zeros at all heights without using them. It does not exist.
- (vi) R183_031/033.

### 2.13 The C_T conjecture (R183_024 §2.5)
- (i) C_T := I_S ∧ N_T. I_S is the semilocal identity E_S = Son_S − ∫c_h ε_S; N_T is the inertia R'_{S,T} ≥ −b|v⟩⟨v| +
  c(I − |v⟩⟨v|) with δ_T > 0.
- (ii) **PROVED:** C_T ⟹ D_T on ker ℓ, and ∀T C_T ⟹ D. D ⟹ C_T is **OPEN, with evidence against**. I_S was later proved
  (R183_029 + 025). By the Szegő falsifier (CONDITIONAL[on ε_S ∈ L¹, Landau–Widom]): if r_S < 0 on a set of positive measure,
  then n₋ ~ cT and C_T is false.
- (iii) It is **strictly stronger than D**: class (b) of R183_024.
- (v) It would have to be true, and probably is not.
- (vi) R183_024, 027, 031.

### 2.14 P_src — norm of the Sonin remainder from the source
- (i) ‖Δ_T‖ ≤ e^{o(T)}, with Δ_T = R'_{S(T)}|_{𝒫_T} computed from ε and δε_p.
- (ii) **PROVED: P_src(ζ) ⟹ D** (Prop 1). That P_src ⟺ Θ = ½ is ARGUED (4.3).
- (iii) Thm 2 / Cor 3 (W11′).
- (iv) M_m has the same source, so P_src(M_m) ⟺ P_src(ζ).
- (v) A proof that does not use identity (3.1) also proves P_src(M_m). A proof that uses it is a bound on ψ(x) − x
  with exponent 2Θ − 1: REF-D.
- (vi) R184_015.

### 2.15 Arrows between nodes (summary)

```
O2601.1 ⟹ C_B                         C_B ∧ L8 ⟺ D                   L8 ⟹ Θ<1 ; (A ∧ L8) ⟹ LH
C1 ⟹ [C2 ⟺ ¬D]                        ¬C1 ⟹ [¬C2 stronger than ¬D]
(ZF_R) ⟹ L*_comp                       L*_comp ⟺(ARGUED) [R₀] ≠ 0
BF^disc_{θ₀} (0<θ₀≤⅓) ⟹ D ∧ GRH₂      BF^disc_{θ₀} (θ₀>⅓) FALSE
(M) ⟹ (M_w) ⟺ (E′_loc) ⟺ R'_S HS      R'_S HS ⇏ sign
P_src ⟹ D                              P_src(ζ) ⟺ P_src(M_m)            [Thm 2(i)]
inertia + quantitative bound ‖Δ_T‖ ≤ e^{o(T)} ⟹ {blind to M_m} ∨ {REF-D}   [W11′, Cor 3]
∀T C_T ⟹ D ;  C_T ⟹ D_T|ker ℓ          D ⟹ C_T : OPEN, evidence against
(WS*)@witness ∧ (Dom_θ) ∧ (P_gap)@y≪1 ⟹ no witness ⟹ D   [PROVED chain of R169 §1]
𝓘_X ∀X ⟹ (WS*) at every witness          𝓘_X at fixed X: finite computation (Eratosthenes)
(★_loc) ⟹ local (★_cell) ;  (★_cell) ⟹ D (PROVED cond. on 4.8)
```

---

## 3. The impossibility layer

### 3.1 The meta-theorems

Each entry is stated as "every proof of D that uses only … is a reformulation of D (REF-D) or fails on falsifier X". [Note: "is REF-D" describes the content of the sign step; it is not a closure criterion.]

**I1 — W1, the catalogue of reformulations (REF-D)** (Paper 48 W1; grid §3). Let there be a proof whose sign step is the positivity of one of these
structures: window Kreĭn or de Branges, Herglotz of ξ′/ξ, Li or Keiper, Nyman–Beurling, the global Sonin range in
a contact, a window-wise law quantified ∀T, the flat-top certificate, the Hodge index, ε₀ ≥ 0, Ω₇/RDI, P_form, Q,
N ≡ 0, or (L-C) ∀T. Then that proof is a reformulation (REF-D): its sign step is D itself. [Note: being a reformulation is not grounds for closure; the historical figure "≈ 40% of the routes" refers to routes that did not contribute a constructive step, not to routes dismissed by label.]

**I2 — Theorem M** (Paper 48 thm:M(b), PROVED in the record; not yet in a refereed paper).
λ^W ≤ λ^P ≤ λ^A ≤ exp(−e^{(2−ε)T}) for T ≥ T₀(ε). Every proof that needs, in window T, a margin, a compactness
gap, a bootstrap, or a perturbation larger than exp(−e^{2T}) fails. Complements: O3 from phase 157 (a single weight
change of size ≤ 2·10⁹T e^{−14.449T} reverses the sign, so no estimate-type input acts in any window);
the per-window ceiling T/log T; the master-quantifier lemma (averages over T imply nothing per window).

**I3 — W3/F3, class blindness** (Paper 48 W3; P46 Thm 12.5). Every proof whose sign step uses only a ≥ 0, supp a ⊂
{p^k}, the EF, or monotone laws on the weights also holds for deletion Λ1_{n≥5}, the κ-models/finmod, Davenport–Heilbronn,
Epstein, and the two-atom Type I curve (s₂^c = 0.9997678; uncertified), and therefore proves something false. Exact list of
falsifiers by property used (grid §4):

| property used | falsifier |
|---|---|
| zeros only | M_m |
| window data | f_t |
| Fr ⊂ ℕ + EF at q > 1 | f_χ |
| Λ ≥ 0 + Euler + Λ*1 = log without ℤ | Beurling DMV/Zhang |
| character sums | Λχ₂ |
| positivity and atomic counting | Λ̃ |
| extended class | ζ_θ |
| moments of θ − 1 | P_{a,c} |
| sieves | b_θ |
| geometry (A1–A6) | Epstein |
| EF without Euler | DH |
| Hodge, h⁰, two gates | Ξ_a |
| uniformity across fields | ζ_K, S₃ |

**I4 — W3′ / Thm O** (R163_1001, PROVED given the zeros of f_χ). Global integrality of the frequencies together with the EF
with Γ(s/2) is blind to the sign when q > 1 (f_χ), and is the identification f = cζ when q = 1.

**I5 — W-identification** (Hamburger; Thm O; Thm R of R164_401; thm:ident of R164_190). Every global property that separates
ζ from all falsifiers defines the class {ζ} or {cζ}. A proof using only such a class property reduces the
question, without change, to D for ζ. Corollary: (★_cell) must be proved for ζ individually.

**I6 — W-sieve** (R167_102 Thm B′; R167_103 Theorem S; R168_102 Thms 2 and 4). Every proof of (WS*) using only
0 ≤ b ≤ Λ, support on prime powers, upper sieve bounds, and the large sieve fails on b_θ, whose one-sided twisted sum
reaches X^{½}. Every proof with Selberg, Brun–Titchmarsh, Vaughan, or the Montgomery–Vaughan large sieve, uniform in X with
η < ½, holds in Beurling DMV/Zhang, where there are zeros off the line. Measure statements in γ never exclude a given
height (Thm 2). Inputs uniform in γ ≤ Y^A prove too much: they give a zero-free strip, i.e. absence of a witness, D (Thm 4).

**I7 — Inertia** (R184_004 Cor 5, PROVED). Every proof of C_B from the decomposition W_T = A_∞ − C_ε − ΣB_p, from the
inertia arithmetic (Sylvester, Haynsworth, monotonicity), and from any property of the B_p, including Λ(p^k) = log p, applies
to M_m. There N ≡ 2m ≠ 0 even though ζ has no witness, so that proof shows ¬D for ζ, or is incorrect.

**I8 — Source/form disjunction, W11′** (R184_015 Thm 2 and Cor 3, PROVED). Let W_T = Pos_S + Δ_T with Pos_S ≥ 0 built
from the local source, and let the property be "‖Δ_T‖ ≤ e^{o(T)}". If Δ_T is defined from the source, the property is invariant
under X ↦ M_m (blind). If it is defined as W^X − Pos_S, its lower half is Q ⟺ D (REF-D). There is no third definition.

**I9 — (iii) ⟹ (ii)** (R166_501 Thm A, PROVED). Let H be a class of hypotheses with ζ ∈ H, proved without assuming D, that excludes f_t and
M_m. Then H uses Λ beyond the window. The set {(i), (iii)} without (ii) is empty by theorem, and every functional of
(X, Γ_on), including the phase ω(E), is satisfied by M_m with its own witness.

**I10 — Interlacing** (R165_201 Thm 3(a), PROVED). With G = sin πρz and Z = cos πρz there is perfect interlacing at
critical density, and yet Re G(x₀ − iδ)² = −sinh²πρδ < 0. Every proof of the type "critical interlacing ⟹ the quartet leaves the cone"
is false. Moreover, contact does not force interlacing (R165_202).

**I11 — The M_m / f_t dichotomy** (R163_801 Thm 5; R163_901 Thm F). Every proof that uses only the zero side (Thm 1,
Prop 2, Thm 3 and Prop 4 of R163_801) holds for M_m, whose prime side differs only by the non-atomic density β_m. Every
proof that uses the full EF with Γ_ℝ and the pole, real coefficients, integer multiplicities, the zero identity, and the
prime side for |u| < 2T₀ holds for f_t = ζ + tg, which has zeros off the line. The clause for (★_cell) depends on
the existence of a witness for f_t (ARGUED).

**I12 — Jet hierarchy** (R166_201 Thm 1.3, PROVED). No quantity built from nodal weights (k = 1), from the kernel
equation (k = 0), or from any nodal jet reads the sign of Re G(t_q)², which is the k = −1 jet.

**I13 — Circularity of inequalities on Λ, (N′)** (R166_802). Let B be an inequality on Λ, true for ζ, that
excludes the witness with a single test or with a power-size family. Then B is the O-bound on the sum of Λ beyond
the window, at the frequency γ_q, with exponent δ′ < δ_q, and that is equivalent to Θ ≤ ½ + δ′. It is PROVED for one test and for
power-size families, and **ARGUED** in general. Sieves (S1)–(S3) reach at most Θ ≤ 1; Λ ≥ 0 only reaches the
dlVP region.

**I14 — Discarded-term principle** (R164_601 Thm 3.1, PROVED). Every inequality obtained by discarding a signed tail
holds for the true zeros, whatever they may be. It excludes only a quartet together with an independent lower bound,
which is weighted (★_cell).

**I15 — No descent** (SUPPORT-DESCENT §2, PROVED). Every implication "R_L F ≠ 0 ⟹ there exists T′ < T_* with 𝔞_{T′} < 0" at a
first contact is equivalent to D: the consequent is impossible by lem:monoT. The interference acts on the outer collar, not
on the interior.

**I16 — No propagation by dilation** (SIGN-REAUDIT §3, PROVED). For ½log2 < T < ½log3 there is no finite C with
q′₁(F) ≥ −C q₁(F) on all of C_c^∞(−T,T). Every Grönwall-type proof over the whole domain fails. Inequality (1) of
β(n) holds for s ≥ 2, but breaks down under modulation (3).

**I17 — The remaining walls** (Paper 48):
- W4 (orientation): a square of (PC) or of truncated Weil does not orient.
- W5 (jets at λ = 0).
- W6 (linear limit): the two identities are PROVED; the general exclusion is **not** claimed.
- W7 (Λ*1 = log used linearly).
- W8 (finZ and rationality).
- W9 (T1/T2/T5).
- W10 (no MW-5 carrier nor h⁰).
- W11 (one-sided positivity).
- W12 (sign-free identity; trilemma).
- Thm 7C (second moment = Parseval).
- R164_502 L1 (spectral invariants are window data).
- R164_501 Thm SA (sinc from the zero side: REF-D, no free type remains).

**I18 — Beurling layer.**
- prop:analyticnogo: every analytic class obstruction fails on ζ_θ.
- Thm BFdisc: integrality alone does not suffice for θ₀ > ⅓.
- Cor finitepert: every ℕ-comparable system is equivalent to D.
- R184_008 Thm F: multiplying by a factor never adds zeros to the right of θ.
- R184_014 B3/B4: L*_comp without integrality mod 1 is false in the relaxed class.
- R184_005 N2: the diophantine route is NO-GO.

### 3.2 What a proof must use: the blank cells

Read in the negative, the meta-theorems of §3.1 say what a proof of D must use. They are joint requirements.

| | requirement | forced by |
|---|---|---|
| (α) | A property of **Λ over ℕ**, individual (not of a class): it must distinguish ζ from f_t (prime side beyond the window) and from M_m (atomicity) | I5, I9, I11 |
| (β) | Used **non-linearly** in Λ and non-polynomially in the test (S2). Linear, or it is Poisson, or it collapses to Sonin, or it is identification (cone Λ ≥ 0 + EF = {ζ}) | S2; Thm R; W7 |
| (γ) | Controlling Σ_{n≥X} Λ(n) n^{−½−iγ_q} w(log n), with γ_q the witness frequency, beyond the window, as an **upper bound**, with the strength of exponent Θ − ½ | I13 (N′); R169 A2, A3 |
| (δ) | Coupling the primes with the archimedean place without already being D | W11, W11′ |
| (ε) | **Not** being a norm bound on the Sonin remainder, nor on any Δ with Pos ≥ 0 | I8 |
| (ζ) | **Not** being a sieve upper bound, nor a measure bound in γ, nor uniform in γ ≤ Y^A | I6 |
| (η) | **Not** being only inertia | I7 |
| (θ) | Using the **integrality of the multiplicities** (and of ℤ) | I18; B4; S4 |

There are implicit requirements that also apply:
- (ι) No margin (I2, S12).
- (κ) Not using the zeros (R169 A4).
- (λ) Holding on the whole set Γ_S(F) that defines the window, because the window does not determine γ_q (R169_091 corr. 1).
- (μ) Being global in X, not local in jets (I12, requirement (G)).

### 3.3 Is (α)–(θ) consistent? What the known theorems say

**Logical consistency.** If D is true (no witness), the bound in (γ) is true for ζ: the sum is O(log² Y). The remaining requirements
constrain the *proof*, not the statement, so there is no formal contradiction. The real question is whether there is an
**unconditional** theorem with (α)–(θ). The answer is that **none known** has it:

| result | (α) | (β) | (γ) | (δ) | (ε) | (ζ) | (η) | (θ) | why it fails |
|---|---|---|---|---|---|---|---|---|---|
| Matomäki–Radziwiłł (multiplicative functions in short intervals) | yes | yes (multiplicativity, bilinear) | **no**: gives o(·), not a power saving; holds for bounded multiplicative functions, not for Λ twisted at height γ_q | **no** | yes | yes (b_θ is not multiplicative) | yes | yes | (γ), (δ); R184_015 §6(O184.015b) |
| Sarnak / Möbius disjointness (proved cases) | yes | yes | **no**: o(N); for n^{iγ} it is TNP strength | no | yes | yes | yes | yes | (γ), (δ) |
| Bombieri–Vinogradov | yes | yes (Vaughan + large sieve) | **no**: it is an average over moduli, of the "D on average" type (A9); it does not speak about an isolated frequency | no | yes | yes: b_θ does not satisfy two-sided BV | yes | yes | (γ), (δ); R169 §7 proposes a "BV for a window-selected frequency", which does not exist |
| Vinogradov–Korobov (bound on ζ, Vinogradov mean value) | partial: it is about ℤ, via n^{it}, not about individual Λ | yes | **no**: region 1 − c(log t)^{−2/3}…; bounded by dlVP (R164_601 Thm 3.3: ½ − δ ≤ c/log γ) | no | yes | yes | yes | **yes**: counts integer solutions | (γ), (δ); it is the closest case in (θ) |
| Montgomery–Vaughan (mean value and large values) | **no**: holds for any coefficient | no: it is quadratic (W4) | no | no | yes | **no**: it is large sieve (Theorem S, Thm 2) | yes | no | almost everything |
| Deuring–Heilbronn | **no**: zero-side and family-based | yes | **no**: conditional on an exceptional zero near σ = 1 | partial (explicit formula) | yes | yes | yes | no | it is the opposite of (P_gap): repulsion by a zero, not localization |
| Linnik (log-free density + DH) | **no**: families (T5) | yes | **no**: near σ = 1 | no | yes | yes | yes | partial | (α), (γ) |
| Selberg central limit theorem | **no**: values of log ζ, in measure | yes | **no**: measure statement in t (I6, Thm 2) | no | yes | **no** | yes | no | (γ), (ζ) |
| Li–Radziwiłł (R184_011) | **no**: zero side | — | no | no | — | — | — | — | (α), (κ) |
| Hilberdink / Révész Rem. 7 | no: of class | yes | **no, opposite direction**: pushes zeros to β > θ, not towards the line | no | yes | yes | yes | **yes** | (α), (γ) |
| Levinson–Conrey | no | — | no | no | — | — | — | — | Bombieri–Hejhal: DH has 100% of zeros on the line and still infinitely many off it |
| Ingham–Landau (Ω) | — | — | **wrong direction**: lower bounds (A2) | — | — | — | — | — | (γ) |
| Weil over 𝔽_q | yes | yes | yes | yes | yes | yes | yes | yes | **does not exist over ℤ** (W10: no h⁰, not even the framework) |
| Maynard–Pandey–Radziwiłł 2026 (R184_009) | yes | yes | no: additive phase | no | yes | **no**: b_θ satisfies the bound | yes | yes | (γ), (ζ) |

**Reading.** (γ) always fails: it is the only requirement of quantitative strength, and that of "localization of D". When
(α) ∧ (β) ∧ (θ) is satisfied, as in Vinogradov–Korobov or Matomäki–Radziwiłł, the saving is o(·) or stays in the dlVP region.
When a power is gained, as in Bombieri–Vinogradov or the large sieve, it is on average and violates (ζ)/(λ). Nor is
any unconditional theorem known that satisfies (δ). **Verdict: (α)–(θ) is consistent as a specification, but is empty in the
known literature.** The part of (γ) that no PROVED meta-theorem excludes is the following: **non-linear, multi-scale**
inequalities linking the window (selector) with the tail (Eratosthenes) without being an O-bound on a single twisted sum.
This is O166.802.1.

---

## 4. The minimal crossword

### 4.1 The minimal set of OPEN statements whose conjunction, together with the PROVED tools, would close D

**Route A (witness and decorrelator).** It is the only route with the intermediate chain fully written out (R169 §1).

```
 [PROVED] ¬D ⟹ ∃ T_c ∈ (0.8047, min τ(ρ)], real-rooted witness F, nodes X, Γ_S(F)    (Prop witness; R165_101)
 [PROVED] identity 4Re𝒮 = (L/π)I − Q_K − R_K − O_K + polar                           (R167_101 Thm A)
 [PROVED given A2] negative quartet ⟹ Re𝒮 ≥ B                                        (R167_101 Thm B)
 A1 = 𝓘_X for every X: Re𝒮 < B at every (γ,δ) ∈ Γ_S(F), F in the image of [S]          OPEN — THE blank cell
 A2 = (Dom_θ)                                                                        OPEN (technical)
 A3 = (P_gap) in δ_q log γ_q < y₀                                                     OPEN (zero side)
 A1 ∧ A2 ∧ A3  ⟹  no witness  ⟹  D
```

The conditions of A1 are (α)–(θ) and (ι)–(μ). The prior question is whether A1 is strictly weaker than D: that is the check in
R169 §8 about the size of the image of [S]. If the heights Γ_S(F) that the window selects, as X varies, cover
[0, Y^A] with sufficient density, R168_102 Thm 4 turns A1 into D (REF-D) and route A reduces to the cluster. Today it is
**undecided**.

**Route B (finite multiplicity).**

```
 B1 = O2601.1        OPEN, no candidate   ⟹  C_B
 B2 = L8 (m < ∞)     OPEN, Lindelöf strength or more
 C_B ∧ L8 ⟺ D
```

It needs **two** unknowns, and B2 alone is stronger than any known theorem. B1 is blocked for proofs
by inertia (I7) and by norms (I8).

**Routes excluded as minimal:**
- P_src (I8).
- ∀T C_T: probably false.
- BF^disc ≤ ⅓: stronger than D.
- (★_cell)/(TC): REF-D as they stand (valid targets; not closed by the label).

**[reading] The minimal crossword is {A1, A2, A3}, with A1 as the only cell with content.** A2 and A3 are technical or on the
zero side. A1 is a single inequality on Λ, with no zeros, on a set of frequencies defined by the window, uniform
in X.

### 4.2 The minimal set whose conjunction would prove that D is unreachable with the corpus's methods

There is no absolute mathematical statement "D is unreachable": D might be provable. What can be formulated is a
**barrier theorem relative** to a declared class of methods 𝔐. 𝔐 is the ∧-closure of the primitive inputs of the
corpus:
- class properties (positivity, support, EF, integrality of frequencies and of multiplicities without EF);
- window data;
- sieve upper bounds and measure bounds;
- inertia;
- remainder norm bounds;
- linear or quadratic functionals of Λ;
- finite identities (Selberg, Möbius, Vaughan, window→tail Eratosthenes).

Three pieces are missing for that theorem:

```
 U1 = O166.802.1 in the negative: every inequality B on Λ, true for ζ, of bounded
      degree in Λ and with finitely many scales, that excludes the witness, is equivalent
      to Θ ≤ ½ + δ′ (extends I13 from "single test / power family" to "multiscale polynomial").
 U2 = closure of 𝓘_X: either (a) the image of [S] is dense in the sense of R168_102 Thm 4
      (then A1 is REF-D), or (b) every proof of A1 in 𝔐 holds for a Cramér model
      conditioned on the window with a quartet (a new falsifier that would need to be built).
 U3 = O2601.1 in the negative within 𝔐: every property of Λ in 𝔐 that forbids the a.c. part E
      is either satisfied by Λ̃ / M_m or identifies ζ (extension of thm:ident to individual properties).
 U1 ∧ U2 ∧ U3 ∧ {I1–I18}  ⟹  "no proof of D in 𝔐"   (relative barrier)
```

This set **exists as a programme**. U1 is the most tractable: it is the extension of a theorem already PROVED in two cases.
U2(a) is a computation about the selector. U3 is the hardest to formalize. The result would be a barrier paper, in the
style of relativization or of natural proofs, and not the closure of D.

---

## 5. Priorities for the author

Decidability indicates whether a theorem can be expected in either direction.

| # | item | cost | decidability | can close D | pure Beurling |
|---|---|---|---|---|---|
| 1 | **U2(a)/R169 §8**: size of the image of the selector [S] as X varies. Does R168_102 Thm 4 force A1 to be REF-D? | low-medium | high | indirectly: decides whether cell A1 is real | no |
| 2 | **U1 = O166.802.1** restricted to degree 2 and two scales (window × tail, Eratosthenes): does the circularity extend? | medium | medium-high | no; if it comes out negative, it is the central barrier | no |
| 3 | **(Dom_θ)** (O167.101.1) | medium | high (technical) | only as a piece of route A | no |
| 4 | **A1** directly: a "Bombieri–Vinogradov for a window-selected frequency" | very high | low | **yes, it is the cell** | no |
| 5 | (P_gap) / O168.103.1: non-linear coupling in ξ′/ξ | high | low; probably REF-D | only as a piece | no |
| 6 | O2601.1 + L8 (route B) | very high, two unknowns | very low | yes, in theory | no |
| 7 | U3 and writing the barrier theorem (possible Paper 49) | medium | medium | no; honestly closes the programme | no |
| 8 | **L*_comp** via (ZF_R) or uniform anticoncentration | medium | medium | **no** | **yes**, publishable |
| 9 | **BF^disc_θ, θ ≤ ⅓** (outside the lattice, O184.001a/b) | high | low | no (it is stronger than D) | **yes** |
| 10 | **C1 in O(1)**; check Hilberdink 2012 (O166.701.1) and the priority of BFdisc (R163_892) | low-medium | medium | no | **yes**, publishable |
| 11 | (M)/(M_w): compactness of the Sonin remainder | medium | medium | no (no sign) | no; it is CC-type operator analysis, publishable |
| 12 | Refute ∀T C_T with the Szegő falsifier (remove the conditional ε_S ∈ L¹) | low-medium | high | no | no; negative note on the later Connes route |
| 13 | Theorem M(b) to a refereed paper | low | high | no; consolidates I2 | no |

**Pure Beurling mathematics**, publishable but unable to close D: items 8, 9, and 10, together with Thm BFdisc,
lattice rigidity, T3/T4, and Theorem F of R184_008.

**Recommendation [reading].** Do 1 and 2 first, which are cheap and decide whether the only blank cell with content (A1)
is real or is REF-D. If both come out negative, the honest exit is 7: a barrier theorem relative to 𝔐. Package 8–10 can
run in parallel as publishable production independent of D.

---

*No record file has been modified. Row D: OPEN.*

---

## Addendum (after R184_016)

**A1 is REF-D** (R184_016 Thm 1, Thm 2, Prop 3; PROVED given (Dom_θ)). With the first-contact
selector, A1 is vacuous without a witness and is equivalent to "there is no witness in the regime".
For every family of tests defined without zeros, A1^𝔉 is equivalent to the selected heights
forming a zero-free region; sine-type translations sweep through every γ, so A1 strengthened is D in the regime.
U2 is closed in sense (a). (Dom_θ) and (P_gap) are on the zero side.

**Corrected minimal crossword (after R184_094):** route A reduces to the REF-D cluster plus
ONE blank cell within that architecture: **O166.802.1**. Outside route A,
route B (B1 = O2601.1, B2 = L8), C_B, C_T, (M)/(E′_loc), and C1 in O(1) remain OPEN.
The R184_094 sandwich: A1^𝔉 ⟹ absence of zeros in Z(𝔉) (PROVED), ⟸ CONDITIONAL.
O166.802.1 is (non-linear, multiscale inequalities on Λ, outside the
power-family case of the circularity theorem (N′) of R166_802). Resolving it
in the negative closes U1 and, with U3 (O2601.1 in the negative within 𝔐), gives the
relative barrier theorem; resolving it in the positive is the only arithmetic input that
no meta-theorem of the corpus excludes today.

---

## Addendum: Phase 186

Sources: `03-research/phase-186-toolbox/README.md` (steps 1–13) and entry 25 of the master grid
log (`03-research/phase-162-row-d-first-contact-closure/grid/R162_2300_MASTER_GRID.md`, §8).
Cells are closed only by proved impossibility within a declared class or by an explicit falsifier.
Documentary task: nothing new is proved here.

### 1. New cells built (PROVED)

| cell | statement | file |
|---|---|---|
| F_S | F_S = E F_∞ E⁻¹ unitary; F_S² = 1, self-adjoint; F_S ϑ(ρ) F_S = ϑ(ρ⁻¹) | R186_006, R186_007, R186_009 (L0) |
| A_S | A_S = P F_S P compact, not Hilbert–Schmidt, ∈ S_p ∀p>2; new spectrum (not similar to A_∞) | R186_007, R186_011, R186_015 |
| Thm C / C′ | dispersion phase φ′(t) = −Σ_k v_{2^k} cos(kt log 2) exact, additive in S; exact linear trace Tr ϑ(h)(P̂^S − P̂_∞) with no remainder | R186_008 (adversarial 094) |
| Π_S | Riesz projection (1−P)∧(1−P̂^S); unconditional operator gap cos²θ_n = λ_n², rate λ₁^{2n}; Π_S = Q₁Q₂Q₁ − Σλ_n²\|ζ_n⟩⟨ζ_n\| | R186_009, R186_095 |
| semilocal chain ∀S finite | TC_S (010), L2_S with log^r singularities at the S-units (012, 015), (84)_S (014, 015): E_S = Son_S − ∫c_h ε_S, Son_S ≥ 0 trace-class, remainder −C_{ε_S} Hilbert–Schmidt ∀T | R186_010, 012, 014, 015 (adversarials 096–098) |
| dictionary D0–D3 | λ does not depend on the window; model u at λ=1 = CC's S(1,1); no 2π error; Tr ϑ(f)Π_{S(λ,λ)} = W_∞(f) + 2log(1/λ) f(1) + ∫f ε_λ; CONSISTENT chain | R186_017, R186_099 |
| invariant ρ*(T) | ρ*(T) = sup_{𝒫_T} C/Son_S; positivity on 𝒫_T ⟺ ρ* < 1 (definition PROVED; values NUMERICAL: 0 at ½log2 → 0.944 at ½log3) | R186_101, R186_021 |
| 𝒱_k ⊕ E_k | decomposition of 𝒫_T into k equal blocks, dim E_k = 2k−2 (piecewise Tate); sector with Tate = archimedean background of window τ = T/k | R186_024, R186_104 |
| K₁ | residual kernel after the per-block Tate terms: K₁ = 2e^{−5u/2}/(1−e^{−2u}) ≤ 1/u | R186_024, R186_104 |
| Thm A | c_∞(τ) ≥ log(1/τ) − C_A(τ), C_A ≤ 1.29 for τ ≤ 0.1 | R186_025 (adversarial 105) |
| Thm B | 𝔞_∞(F) ≥ (log(1/τ) − C_B(τ))‖F‖² on 𝒱_k, C_B → 1.64 (Lemma 2.1: low-pass leakage) | R186_025 (adversarial 105) |
| Cor. (L1) | c(T,k) ≥ log(k/T) − C_B − ‖P\|𝒱_k‖, with ‖P\|𝒱_k‖ ≤ 1.674; positive with k ≥ 25 at ½log5 | R186_025, R186_105 |
| ‖𝒦₁‖ = π | norm of the residual coupling in the adjacent pair (explicit Weyl sequence); (P2) false | R186_025, R186_104 |
| per-window reduction | (L1) + Thm 3.1 (domain form, R186_100) ⟹ λ_A(T) > 0 ⟺ S_{T,k(T)} ≻ 0 in dim 2k−2 | R186_019, R186_100, R186_105 |

### 2. Cells closed in the negative (NO-GO)

| cell | reason | file |
|---|---|---|
| CCM candidates −𝔰² + λ²N_S and metaplectic | do not commute with P^S_λ (exact computation F1); defect on disjoint support | R186_003, R186_006, R186_092 |
| TB-3 (two-scale bilinear, degree 2) | Thm TB3-neg for every degree; b_θ satisfies the generalized Selberg inequality | R186_005, R186_092 |
| zero of the Sonin density | ρ_T = m + ε̂_T is not ≥ 0 pointwise (ρ_T(0) = −2.36); positivity is of the compressed operator | R186_022, R186_103 |
| single-mode alignment law | W[h_a] follows λ_min only up to T ≈ 0.45; increasing-rank near-cancellation (Landau–Widom) | R186_023, R186_103 |
| AL-k as a route | rewriting of W ≥ 0 in the eigenbasis of A_∞; AL-k(a) ill-posed | R186_103 |
| uniform 4×4 Schur | c = min 𝔞_T\|𝒱 drops 0.906 → 0.013 between T = 0.48 and 0.69; dim E jumps to 8 at log 2 | R186_024 |
| k ≍ T stability as a structure | approximation artifact (E_k = piecewise linears approximate any smooth h* to O((T/k)²)) | R186_104 |
| (L1) via operator norms | ‖𝒦₁‖ → π in the continuum; ‖P\|𝒱_k‖ ≤ 𝒜_T/2 false for T > log 2 (superseded by Thm B, which does not separate diagonal/coupling) | R186_104, R186_025 |
| inertia of the semilocal remainder | n₋(−C_{ε_S}\|𝒫_T) = ∞ at λ=½ (ARGUED, antidiagonal block of the log peak); "n₋ < ∞ by compactness" FALSE; equivalent to the density requirement of R183_031 | R186_013 |

### 3. New blank cell of the front: **(L2)**

**Statement.** S_{T,k} = G_EE − G_E𝒱 G_𝒱𝒱⁻¹ G_𝒱E ≻ 0 in dim 2k−2 (≈ 48–58 at ½log5, for k = 25–30).
By the reduction of §1, this is, for each T, exactly λ_A(T) > 0.

**What is known.** G_EE admits a closed form (in progress, R186_026, `r026_gram.py`); the Schur
correction is variational over 𝒱_k, and with c PROVED (Cor. L1) a rigorous upper bound on the
subtracted term is obtained (near-maximizer + residual²/c), certifiable today only for T ≤ 0.6 by precision (R186_105).
NUMERICAL: λ_S/λ_W ∈ [1.00, 1.09] over the whole grid, λ_A(½log5) ≈ 3–4e-12 (mpmath 30–40 digits).

**What is missing.** A structure for S_{T,k} that **does not inherit thm:margin**: today the positivity of S is the
full superexponential near-cancellation, merely shifted to a finite matrix. No norm bound decides it (§2); an
argument internal to E_k (piecewise Tate) is needed, or a relative bound
𝒦₁ ≤ θ·A_∞\|𝒱_k in forms (θ ≈ 0.21–0.23 NUMERICAL, R186_025) that enters the Schur complement itself.

**Relation to O166.802.1.** (L2) is a distinct cell: O166.802.1 asks for a multiscale, non-linear
arithmetic inequality on Λ (class 𝔐, prime side), while (L2) is a finite matrix
positivity on the window-form side, with the primes already inside G via K; neither
implies the other by a theorem of the corpus. It remains OPEN whether a T-uniform resolution of (L2)
would in fact need an input of the O166.802.1 type (R186_104: "(L2) inherits thm:margin" is evidence,
not proof). This question is not closed here.

### 4. What goes into Paper 46

| item | label | destination |
|---|---|---|
| F_S unitary/involutive, A_S compact non-HS, Thm C, Thm C′, Π_S + gap, TC_S, L2_S, (84)_S, chain ∀S finite | PROVED (CC 2008.10974 and CCM 2403.01247 CITED) | section 2 "semilocal chain", DRAFT already written (step 10; CHECK_TABLE) |
| dictionary D0–D3, term 2log(1/λ)‖h‖² | PROVED | section 2, normalization note |
| n₋ = ∞ of the semilocal remainder; CV_S NO-GO in L^∞ | PROVED / ARGUED | section 2, negative observation |
| Lemma 1.1, Thm A, Lemma 2.1, Thm B, Cor. (L1), reduction λ_A(T) > 0 ⟺ S_{T,k(T)} ≻ 0, ‖𝒦₁‖ = π | PROVED | `DRAFT_SECTION_COERCIVITY_REDUCTION.tex` (in preparation) |
| ρ*(T), archimedean s₀, single-mode alignment, λ_A up to ½log5, precision floor at 0.85 | NUMERICAL | observation after prop:negtrace, only T ≤ 0.72 (R186_103) |
| relative barrier BR, Lemma 1.1(b), corrected W11 | PROVED / CITED / CONDITIONAL | `DRAFT_SECTION_INERTIA_BARRIERS.tex` (not integrated) |
| (L2), closed form of G_EE | OPEN | open problem at the end of the coercivity section |

Integration rule: each item is checked against def:W / def:PD / eq:nuw / thm:margin / lem:contA
of the paper before entering (feedback-check-against-paper-definitions).

*No symbol in the grid changes; no contact with the sign. Row D: OPEN.*

## Addendum phase 188 (D-only)

Source: `03-research/phase-188-closing-D/SYNTHESIS_188.md` (tracks (L2) and (N); 34 memos, 2 adversarial reviews). Pen and paper.

| cell | phase-188 result | label |
|---|---|---|
| does there exist a comb with window positivity ∀T? | YES: ρ_κ (κ ≥ κ*), continuous Beurling, multiscale atomic comb (N_011, L2_018) | PROVED |
| density threshold | κ* = sup(−m)(¼+τ²) ≥ 1.343 > 1 = density of Λ: explicit deficit (κ*−1)/(¼+τ²) that the arithmetic fluctuation must cover | PROVED |
| requirement (δ) coupling primes and the archimedean place | every surviving entry needs a non-linear Euler product over ℕ × FE(q=1) (L2_011); Poisson–Euler Φ and the cube realize it as objects, without an inequality | PROVED / OPEN |
| weakenings of (N) | (Ω_{t₀}) strictly weaker; it collapses on wave packets (exact criticality at every γ) and on translation/modulation families | PROVED / CONDITIONAL / ARGUED |
| closed method classes | W-tail, Euler structure, cone-monotone resolvent, relative order, scalar transfer, Euler cone, Möbius–log certificate, Frobenius, perturbative Φ, constant-weight packets | NO-GO |
| frontier | correlation inequality (anti-alignment of U_μF and U_logF on 𝒩_T) quantified against (κ*−1)/(¼+τ²); (Ω_{t₀}) on non-convergent spectral-measure families | OPEN |

*No symbol in the grid changes; no contact with the sign for ζ. Row D: OPEN.*

### Addendum phase 188 — update 2 (D-only)
| cell | result | label |
|---|---|---|
| single-function reformulation | target ⟺ B_{F₀}(d) = 𝔞(F₀, τ_dF₀) positive definite on ℝ (L2_024 Thm S) | PROVED (⇒); (⇐) mod. Lemma I ARGUED |
| necessary local proof | two-sided band |X(d)| ≤ 2a₀ at every scale (L2_023 Thm T); unconditional oscillation around 0 (N_015 Thm L) | PROVED |
| dual side | operator splits = linear identities + C–S (N_018); SOS = class (D), pure arithmetic side empty (N_019); known exteriors exhausted (N_020) | PROVED / NO-GO |
| ℤ-additive center | +4T‖F‖²: the leading term survives in quadratic norms even though Tate cancels it in the comb (N_017) | PROVED |
| density | no comb ≥ 0 over log ℕ with residue r > 1 in Pos; κ* ≥ 1.343 (L2_021 Prop 4, CONDITIONAL on Q′; N_011) | PROVED/CONDITIONAL |
| balance | primal and dual reduced to D in every known form (SYNTHESIS_188 §5) | ARGUED (summary) |

*No symbol in the grid changes; no contact with the sign for ζ. Row D: OPEN.*

### Addendum phase 189 (D-only; NT_011–014 + adversarial)
| cell | result | label |
|---|---|---|
| pointwise (𝒱) at σ = 1 | NO-GO for FE + line identity + averages (model ζ̃ = ζ·R, Δℓ″ = 3/(2δ²)); 𝓜 excludes holomorphy + order 1 | NO-GO (CONFIRMED) |
| weak (𝒱) | width √(T₀log(1/T₀)) from archimedean dominance; method limit | PROVED / ARGUED |
| part (b), 1 < σ ≤ 3/2 | zero-free zone Re s > ½+ϑ ⇒ (b) on (1+ϑ, 3/2]; converse with σ-analyticity | PROVED / ARGUED |
| absolute methods for (b) | excluded with sub-power PNT errors | NO-GO (ARGUED) |
| Target E via σ-transport through odd FE factor | excluded: L2_026 antisymmetry/empty transport, L2_027, NT_014, cor:void | NO-GO |
| remaining door | inequality at σ = 1 with on-line multiplicativity, not a zero-free zone | OPEN |

*No symbol in the grid changes; no contact with the sign. Row D: OPEN.*

### Addendum phase 193 front K (D-only; CA_K_000–002, CA_K_SYNTHESIS)
| cell | result | label |
|---|---|---|
| diamagnetic (Kato/Simon) | entire image: empty (→ −∞); t-image: ζ is the diamagnetic extreme and on 𝒫_T the order reverses (λ_A(0.7;0)<0<λ_A(0.7;Λ)) | NO-GO PROVED |
| +/· frustration flow | holonomy = sgn 𝖡; commutation data do not decide | NO-GO PROVED |
| Guerra/ASS interpolation | concavity ⇒ minimizer (REF-D); archimedean and Haar extremes undefined | NO-GO PROVED |
| site independence | D ⟺ tests on primes; Div ≡ 0 there; D ⟺ Arch ≥ Near on primes | PROVED (reformulation) |

*No symbol in the grid changes; no contact with the sign. Row D: OPEN.*
-  front N (phase 193): Viazovska V1–V3 — constructible only in generic form (Epstein) or REF-D; Thm N2 (unimodular transfer impossible T ≥ ½log3). See CA_N_SYNTHESIS.
-  phase 194 D–J leads (AUDIT_194_2): no sign. NO-GO PROVED: cones over log ζ (F2, O_4), integrality 𝒞_ℤ/𝒞_{01} (I2), sparse-stable properties of pairs incl. HL and zero correlation (J3, O_6). E2 only ARGUED for Eichler–Selberg. New datum: the integer comb (component q=1) is negative, g_ℤ(0)=m(0)+2−2ζ(½)=−0.4515 (H3 PROVED). Residue "q≥2 exceeds 0.45" = REF-D. Live hypotheses to break: H_cone, H_mono, H_sparse.
-  AUDIT_195 (phase 194 L + phase 195 M/N/O/P): L3 (Green identity of d_S) verified, no sign; P2 boundary band holds only in ½<σ<1, not in L3's Ω; N BE ceiling reproduced; M, O NO-GO/REF-D confirmed (O §3 downgraded to ARGUED). No symbol in the grid changes. Row D: OPEN.
-  AUDIT_195_2 (Q, R): Green identity without log R1 verified (NUMERICAL 1e−13), Q2 and R4 correct; "only if" normalization lemma false (free gauge I); Q1(a) corrected; "every exact identity factors through ∏γ_v" only ARGUED. Residue: unimodular gauge I with ℤ data. No sign. Row D: OPEN.
-  AUDIT_195_3 (S, T): additive Stokes/resurgence by places, frozen comb {2,3,4} → s(0)=−8.31416 (verified); 42/e = test-family constant (footnote recommended in cor:margin1). Gauge: T1/T1′ verified; contractive gauges impossible ∀T≤½log5 (thm:log5A, not thm:A); expansive gauges = certificates, sup = λ_P PROVED in the source-free unimodular class (T4(⇐) finite-atomic); outside the class ARGUED. No symbol in the grid changes. Row D: OPEN.
-  INV_U_001 (contact crossing): 1/log modulus at the crossing PROVED; boundary law (log 1/δ)^{−1/2} and λ_A C¹ at crossings ARGUED; NO-GO 𝒦_cross (generic-comb local law). No sign.
-  AUDIT_196 (V, phase 196): identities V1.1/V2.1 verified (NUMERICAL 1e−12); Ш-positivity = multiplicativity of 1/j (trivial), V1.4 subsumed; V2.2(c) false (every lattice αℤ); Chebyshev rigidity V2.4 PROVED in a narrow class; (G2) tautological, (G1) inside N_018 ∪ I4. No sign.
-  AUDIT_197_HOSTILE (BARRIER_001): a uniform method decides T ⟺ π_N S ⊆ K_T={μ_T≥0}, convex (lem:degen); Thm 5 = its supporting half-space (PROVED). Lemma 2(a) false (prefix atoms), primitive Ξ_Q ARGUED, 0≡a_P in the window, D1.a false, D2 OPEN ill-posed (near-repeat of INV_P/INV_Q). No symbol in the grid changes. No sign. Row D: OPEN.
-  AUDIT_197_2 (D1/D2): exact Bohr defect formula PROVED (+NUMERICAL); Thm 4 of D1: continuity of the defect in Λ suffices ⇒ REF-D⁺ (not impossibility). D2: defect/continuation = WP_T(Λ) ∧ sign-free rigidity (PROVED). Residues: R1 closed (continuous ⇒ REF-D⁺, discontinuous ⇒ cone/certificate); R2 = non-crossing #101. Normalization P46 v_n=2a(n)/√n to be corrected in BARRIER_001/D1/D2. No symbol changes. Row D: OPEN.

### Addendum— AUDIT_197_HOSTILE_3 (track X)
Kronecker parity (X2) holds for every functional of the stationary ratio process, but only on σ-closed classes (𝓘 is not:
1+2x ↦ 1−2x). Integrality without order = antipodal; with the {0,1} order = finite but not orthant-one-sided (X3(a) corrected),
deciding = REF-D⁺. Open cell: sign of c_{F⋆}(log q) for q in the top layer √N ≤ q < N (Farkas condition of X3(b)). Row D OPEN.

### Addendum— AUDIT_198 (phases 197–198: Y, Z, AA, CERT, BB, CC)
The parity split is exact, and D_odd is not easier in kind. The CERT interval certificates are rigorous. New Lemma M:
λ_A(T;a) is non-increasing in T, so a certified falsifier holds at every larger window. Falsifiers now PROVED: zero comb
(odd) and a_3 for T ≥ ½log5; a_2, 2Λ, 1.15Λ, Λ−δ_7 for T ≥ 1; Λ−δ_3 for T ≥ 0.75; Λ−δ_8 for T ≥ log3. BB Identity 2 had a
coefficient error and should read 2(a⋆a)/√N. CC4 is CONDITIONAL on a simple bottom at Λ. CC's numerics at Λ (M = 12–16)
are under-resolved by ≥ 15 orders and have been withdrawn. Open cell unchanged: sign at Λ in the window (½log5, ∞). Row D OPEN.

## Addendum phase 199 (AUDIT_199, D-only)
- **Horizontal "certificate cost":** the Liu–Mori class (constant absorption γI + tail Prop 3.1) has superpolynomial cost
  Ω ≥ 2π·exp((8+o(1))√μ/log μ). PROVED relative to that class. PATTERN_001's "~μ⁴" is retracted for certificates.
- **Vertical "uniform target":** L′ is NO-GO as stated (gauge falsifier). The correct cell is L′♯:
  W_T(g) ≥ κμ^{−A}·ℓ(g), with ℓ = leakage minimized over the summation-map gauge. L′♯ ⇒ λ^W_T ≥ κμ^{−A−1}(1−λ₀(2πμ))/4
  for every T (PROVED given L′♯). L′♯ is OPEN and REF-D. Before building, state how the proof avoids N_018
  (Möbius identities + Cauchy–Schwarz).
- **Crossing with the barrier:** L′♯ is consistent with the λ^W ceiling. The transfer of BARRIER_EST to λ^W is
  CONDITIONAL.
- **F-DH:** it passes only a conductor-rescaled, pole-free analogue of the residual identity. What must act in the
  coercivity is a feature absent from F-DH; that this feature is specifically the Euler product is not established.

### Addendum— AUDIT_L_SHARP_1 (phase 199, proof attempts A–E of L′♯)
| cell | result | label |
|---|---|---|
| half-line identity (A Thm 1.1 / C Prop 1.2 / E Thm E.1) | a single identity in three forms; W_T(Ef) = 𝒲_ext[Zr] with a killing term ∫\|Ψ\|²κ_a (correction E, P46 "Dirichlet form with killing") | PROVED |
| comb collapse (E Thm E.2) | only on the exterior carrier (full comb); Λ-free form; "Λ ≥ 0 consumed" withdrawn: it is c_N ≥ 0 in Z_logZ^{−1} = Σc_N S_{log N} | PROVED / RETRACTED |
| inverted weights (D Prop 2.3) | ε′(1⁺) = −cΣ(d/dc)log(1−λ_n(c)) by Slepian; reproduces CC's 22.9965; ε_λ′ = O(μ^{3/2}), not e^{4πμ}; gap (G4) withdrawn | FALSE (size) / PROVED (identity) |
| window barrier (B Thm 4.2, D Prop 3.1) | r ≤ λ^W − Cδ PROVED; scale e^{−4πμ} only with rem:moriceiling (μ ≥ 50); "every μ ≥ 5" withdrawn | PROVED / CONDITIONAL |
| exterior-carrier barrier (C Thm 6.1) | does not transfer: identity fails for ν′ ≠ Λ and the margin relative to ‖ℓ‖² is polynomial; multiplier NO-GO only by N_018 | RETRACTED / ARGUED |
| ratio classes (E Thm E.5) | H ~ log X vs G ~ log² X verified; indefinite one by one in C_c^∞; ARGUED in Paley–Wiener | PROVED / ARGUED |
| remaining inequality | (★) = (L_ext) = (R_C) = (★E) = L′♯ ⇒ (★★): 𝒜[Zr] + 2AB − 2⟨Zr, Z_log r⟩ ≥ κμ^{−A}dist²(r,𝒢̄), r Paley–Wiener of type λ modulo the radical; 7 restrictions listed (AUDIT_L_SHARP_1 §6.3) | OPEN (REF-D) |

*No symbol in the grid changes; no contact with the sign. Row D: OPEN.*

### Addendum (bis) — AUDIT_L_SHARP_2 (phase 199, proof attempts F, H, J of L′♯)
| cell | result | label |
|---|---|---|
| universal form (F Prop F.0) | (★★) = a fixed form 𝔔 on L²(1,∞) with fixed radical 𝒢̄₁; all the μ-dependence is in class PW_μ; rescaling verified | PROVED |
| critical line (F Thm F.1) | 𝔔 = quadratic form in ζ_X(1−s), Θ_∞ = −2Re(ζ′/ζ)(½+iτ) (verified to 30 digits); "no zero data" holds for (F.1), not for the partition (the zeros are in F₀ = ζ(1−s)R) | PROVED / ARGUED |
| Euler–Maclaurin partition (F Thm F.2, Cor 3.2) | F₀ pointwise null vector of the line form Q, not of 𝔔: 2AB does not split and contains an F₀–F₀ term; the 2×2 block argument does not apply to 𝔔 (false premises); "sign in the coupling" = A §3.2 | PROVED (identity) / ARGUED (Cor 3.2) |
| Hilbert-type kernel (F Thm F.3) | computation of the kernel max(nξ,mη)/\|n²ξ²−m²η²\| correct; the identity "regular part = −∫∫ρρ𝒦" diverges on every rational line: only a polarized reading (same as literal E.1′, J Rem 2.1) | PROVED / RETRACTED |
| deep data (F Prop F.4, J Thm J.3) | both PROVED and consistent; J gives the exact value (2+γ−log4π)B_φ²e^D = 2(ξ′/ξ)(1)B_φ²e^D = 0.0462 (anatomy −5.372+2.264+2+1.154, NUMERICAL); F.4(b) "the O(1) is the sawtooth in the transition region" FALSE: F₂ negligible, bulk value = explicit formula at the pole | PROVED / FALSE |
| shallow data (F Prop F.5) | depth X₀ ≤ e^{1.6} ⇒ window form T₀ = ½log X₀ ≤ 0.8 ≥ 0 (Zhu Thm 1.2 CITED via P46); log-depth = full window 2T₀ | PROVED / CITED |
| Hilbert kernel in the integer index (J Thm J.2) | there is no antisymmetric kernel 1/(log m − log n): the prime part is log(mn) on the dilation Gram matrix, the archimedean part is (mn)^{−1/2}c_r̃(log n/m) with c_r̃ bounded, continuous, and positive definite, concentrated at 1/μ on PW data; class NO-GO only ARGUED (the Toeplitz-in-log object exists; it is excluded by A §5/N_018) | PROVED / ARGUED |
| base case (H Prop H.1) | L′♯ for 5 ≤ μ ≤ 15 with A = 2, κ = 2^{−2905}/C₀ (Mori Thm O CITED, B1 reproduced) | PROVED (given CITED) |
| flow in c (H Thm H.4, H.5) | dN/dT = −2G_φ(−2T)(W^−G_φ)(−2T): the flow only sees the band-edge alias; Grönwall closure ⟺ (H) ρ_N ≤ ρ_L + A/c at the minimizer (virial, relative precision 1/c, functional of h*); (H) ⇒ L′♯ mod 4.1; Cor H.4′ corrected sign −4c_qG_φ(−log q)φ′(1); 𝒦_H NO-GO | PROVED / CONDITIONAL / NO-GO (ARGUED) |
| same mechanism? (F/J/E) | no: three separate accounts of one global number (Weil distribution at the pole), none localized (neither the transition region, nor the class, nor a "Chebyshev remainder" except by label); outside the PW regime of (★★) | ARGUED |
| remaining inequality | (★★) = (★★_u) = (★★_EM) = (★★_St) = L′♯; restrictions 8–11 added (no antisymmetric Hilbert kernel in (m,n); the deep-mode value as a proof object; the pole couples the Q-null vector; no flow closes without a virial bound) | OPEN (REF-D) |

*No symbol in the grid changes; no contact with the sign. Row D: OPEN.*

## Addendum phase 199b (AUDIT_L_SHARP_3, D-only)

| cell | result | label |
|---|---|---|
| admissible prolate repair (K.1) | f̂(0)=0 forces the use of ψ₀−√2ψ₂; the minimal admissible leakage is (2/3)(1−λ₂) ≍ c²(1−λ₀); f(0)=0 is free at the form level; f(λ)=0 costs on the order of the defect itself; the leakage is not invariant under the radical | PROVED (given Fuchs/Slepian CITED) / ARGUED |
| Poisson J.3 on PW tails (K.3) | the dual terms k<λu are the window: it is circular | PROVED (technique NO-GO) |
| κ-band law | 1.89 = certified Schur margin / unrepaired Fuchs(ψ₄): not comparable; Mori Galerkin V gives 4.1–5.3; the data only fix c^{4.64}e^{−2c}; the constraint count gives index 2, so index 4 requires two unexplained null directions | NUMERICAL / ARGUED |
| reflection and pole (P.1, P.2) | 𝔔 = −Q(G,G)+2Q(F,G)+2AB; the pole's F₀ piece is a rank-one residue, via −χ(s)ζ′(1−s), with no zeros; J_{c′} and I_c are complete forms | PROVED |
| Euler–Maclaurin defect (P.4) | μ=5: 𝔔 ≈ −Q(G,G) eigenvalue by eigenvalue and Q(F,G) low rank; μ=15 not converged; conjecture (C_G) stated | NUMERICAL / OPEN |
| remaining inequality | (★★) = (★★_P) = L′♯; restrictions 12–13 added | OPEN |

*No symbol in the grid changes; no contact with the sign. Row D: OPEN.*

## Addendum phase 199c (AUDIT_L_SHARP_4, D-only)

| cell | result | label |
|---|---|---|
| identity in σ (R.0–R.2) | F_log = ∂_sF + F[ρ log X]; identity in the exponent w of the partial sums; it is the moment form | PROVED (REF-D) |
| pointwise monotonicity (R.3) | impossible on shallow data | NO-GO (narrow class) |
| dual harmonics (S.1–S.4) | the harmonics are dilations of one function; there is no sign per harmonic (k ≥ 3 positive, PD on span{k≥3}) | PROVED / NO-GO (NUMERICAL) |
| ℕ constants (S.5) | −ζ′(2)−ζ(2), γ: diagonal reading; they are the constants of 𝔔[c] | ARGUED |
| mirror (S-dual) | Q(G,G) = −𝔔_line[c] + 2𝔅 − R(1)G_h(0) + c₀ρ₀² − 2ρ₀ρ₁; (C_G)(b) is self-dual, not a reduction; exact only with c=1 | PROVED (C_c^∞) / CONDITIONAL (PW) |
| remaining inequality | (★★) = L′♯; restrictions 14–15 added | OPEN |

*No symbol in the grid changes; no contact with the sign. Row D: OPEN.*

## Addendum phase 199d (AUDIT_L_SHARP_5, D-only)

| cell | result | label |
|---|---|---|
| interlacing E∘𝔉 = R∘E + rank-2 polar | constants verified by Poisson | PROVED (classical) |
| sectors 𝒮_± | 𝔔 = ε(Σ_{j≥1}L_j² + 𝒫 − A²), archimedean SOS, B² absorbed | PROVED given the radical lemma on 𝒮 (CONDITIONAL) |
| transfer 𝒮 → window data | 𝒮∩C_c={0}; no window datum lies in 𝒮 | OPEN (restriction 16) |
| prediction 𝒮_− ∩ {A=0} | 𝒫 < 0 forced; it is not a falsifier of D | OPEN |
| gauge of (C_G) | −Q(G,G) not bounded below on radical classes | PROVED mod NUMERICAL (restriction 17) |

*No symbol in the grid changes; no contact with the sign. Row D: OPEN.*

## Addendum phase 199e (AUDIT_L_SHARP_6, D-only)

| cell | result | label |
|---|---|---|
| boundary mirror 𝔉_μ ↔ R_a, radical sectors f_± | W_T = ¼𝒲_refl[u_+] − ¼𝒲_refl[u_−] = Guo polarization 4.5 | PROVED (no sign content) |
| gauge complement | 𝒮(1,1)⁺; data = Sonin ring 𝒱_μ; ℓ = λ‖Πρ‖² | PROVED (L²) |
| U.3 transfer | identity with polar block e₀ | CONDITIONAL |
| Mori extremal μ=15 | pieces and 1−λ₄ reproduced; κ_emp ≥ 0.56 | NUMERICAL |
| self-duality of f* | = parity of g* (Φ_{f_−} = ½(Ψ − Ψ∘R)); not sector 𝔉_μ | PROVED (identity) |
| reduction of (★★) to one sector | parity (empty) or impossible (𝔉_μ) | NO-GO (restriction 18) |

*No symbol in the grid changes; no contact with the sign. Row D: OPEN.*

## Addendum phase 199f (AUDIT_L_SHARP_7, D-only)

| cell | result | label |
|---|---|---|
| Carleson sampling at the zeros (W.1–W.3) | Σ_{|γ|≤t*}|Φ_g(ρ)|² ≤ 48M·inf_gauge‖ℓ‖²_*, M over |t| ≤ t*+¼ | PROVED (unconditional, no sign) |
| inverse sampling (W.4) | false by the gauge | PROVED |
| t* = caustic of the prolate continuation | t_c = 183.94 (χ₄ real); peak n = 71–72 | ARGUED + NUMERICAL |
| Mori background = Pólya kernel (N1) | forced by f(0)=0 on span{h₀,h₄} | NUMERICAL, no new structure |
| M1 "Hessian at the radical point" | = I1 (A_001 Thm 1.1) | PROVED, no new content |
| M3 weight 𝔴_μ ≥ log 2μ in chirps | minimum at the caustic tautological; only after Π; leading-order boundary | ARGUED / OPEN (restriction 19) |

*No symbol in the grid changes; no contact with the sign. Row D: OPEN.*

## Addendum phase 199g (AUDIT_L_SHARP_8, D-only)

| cell | result | label |
|---|---|---|
| Theorem B (single-cell chirps, N ≥ 2) | 𝔔 = ∫w\|a\|² + O(H_N log N/ν₀); K₂ corrected (6/2/12), gap 2δ/N | PROVED |
| log² cancellation F(N) = H_N log N − 2H₁(N) | F ≥ 0 ∀N; F ≤ γ log N + 1 | PROVED |
| weight cΛ, c > 1 | explicit negative direction (ν₀ = 2πN^{(c−1)/2}, N → ∞) | PROVED |
| weight cΛ, c < 1 | positive only in the high-frequency cone; 𝔔^{c<1} indefinite on shallow data (0.85Λ) | PROVED (cone) / CONDITIONAL (indefiniteness) |
| PRECHECK_T1 (M3 on prolate tails) | 0.97–0.98·½D₄, offset O(1); partial zero-test | NUMERICAL |
| restriction 20 | single-cell data do not prove cross-class interference | PROVED (X.1, X.3) |

*No symbol in the grid changes; no contact with the sign. Row D: OPEN.*

## Addendum phase 199h (AUDIT_L_SHARP_9, D-only)
| cell | result | label |
|---|---|---|
| Theorem B′ (Y_001, P2 multi-cell, Z₁, no boundary) | 𝔔 = ∫𝔴_μ|a|² + O(c^{−½}) asymptotic; not uniform in X; empty at μ = 15 (≈13×) | PROVED (asymptotic) |
| (1,n) resonances | s_n = √(1+n^{−2}), Hessian −c(n⁴−1)(n²+1)/n³, weight log(μ(1+n^{−2})); m ≥ 2 with no stationary point | PROVED |
| leading resonant size, μ = 15 | 0.17 relative (Langer profile) | ARGUED |
| cΛ, κ > 1 in the Langer class | negative for μ ≥ μ₀(κ); repeats X.7(ii) | PROVED |
| real tails at μ = 15 | jumps ≈0.2% (ARGUED); layer t→1, tail > X, boundary −51% | OPEN |
| restriction 21 | P2 at μ = 15 requires uniformity in X, stationary phase with explicit remainder, t→1 layer, and boundary | — |

*No symbol in the grid changes; no contact with the sign. Row D: OPEN.*

### Addendum AUDIT_L_SHARP_10: TEST_BRIDGE_001
| cell | result | label |
|---|---|---|
| P2 cross-dilate μ = 15 | |Σ_{m≠n}|/S ∈ [0.51, 0.59] after closure error ≤ 0.02 S; (1,2), (1,3) resonant | NUMERICAL |
| P3a μ = 15 | C*/S* = 0.19 ± 0.01 | NUMERICAL |
| P3b boundary | ALIVE withdrawn: global Schur degenerate (p ∥ g*); hybrid V_J cuts, boundary 13–91% W* | OPEN |
| −51% vs +0.04% | distinct objects (I1 failure outside the core vs degenerate cut); neither is the canonical boundary | PROVED (reading) |
| rough complement P1 | physical vs Galerkin undecided; possible jump datum | OPEN |
| restriction 22 | test P3b requires p_λ Schur against a block containing v and excluding the lowest eigenvector | — |

*No symbol in the grid changes; no contact with the sign. Row D: OPEN.*

### Addendum AUDIT_L_SHARP_11 + ROUGH_COMPLEMENT_001: caustic layer and rough complement
| cell | result | label |
|---|---|---|
| layer diagonal (single tail) | (2/3)log 4μ − Cl₂(2π/3)/(2π) from one-sided mass; (1−λ)[⅓log 4μ − 0.053844] is the one-sided value | PROVED (given the envelope) |
| ω = 1 | regular singular point (0,0), Bessel J₀, zone c⁻² | PROVED local + CITED |
| (1,n) resonances, single tail | exact product C²; R̂_n with w₂ = 0.2309, w₃ = 0.1061 | ARGUED |
| layer and κΛ | κ-free (diagonal), O(μ^{−½}) (resonances); does not transfer to the extremal | ARGUED / bounded |
| split g* = p + δ (J = 50) | W(p) = 1.2325, 2W(p,δ) = −0.4650, W(δ) = 0.2325 W*; forced crossing = −W(δ) | NUMERICAL + PROVED |
| δ | rough bulk degree ≈ 250, exterior ω ≥ 2, not prolate; neither jump nor layer | NUMERICAL |
| (1,2) of the extremal | 62% p, 32% crossing, 6% δ; p alone −0.35·X₁₁ | NUMERICAL |
| conjecture (RC) | |W(p,δ)| ≤ θ′√(S(p)S(δ)), θ′ = 0.156 < 0.36 | OPEN |

*No symbol in the grid changes; no contact with the sign. Row D: OPEN.*

### Addendum AUDIT_L_SHARP_12: Möbius network of the exterior datum
EXTERIOR_DATUM_001 audited: ACCEPTED WITH CORRECTIONS. E⁻¹g = Σ_{m≤14} μ(m)h(mu)1_{mu<λ} (PROVED; the pieces are dilates of
h·1_{[m/λ,λ)}, only the upper cutoff is shared). Line m@1 ≡ line nm@n ⇒ resonance (1,n) with sign μ(n), O(1), directional
(PROVED as an identity; dominance NUMERICAL). Corrections: (1,4)=+0.108; bands 8/9; model C′ sensitive to the cutoff; M̃(15)=+0.061.
**Restriction 24:** the exterior datum of admissible data is a Möbius network of truncation lines; every bound on (1,n) must
include the lines m ≥ 2 — single-line models are invalid. Open cell: form grouped by q (C_q, D_q) coupled to the boundary
line, without a "near-cancellation" reading (heuristic). Row D OPEN.

### Addendum AUDIT_L_SHARP_13 + GRAM_INERTIA_001: Theorem D and the inertia of the lattice Gram matrix
AA_001 audited: ACCEPTED WITH CORRECTIONS. f = Σ_{m<μ}μ(m)H(mu) + φ₀ and the form grouped by classes (C_{b/a} = μ(a)M̃_a(μ/a)/a)
are exact identities (PROVED, Abel/L² reading). Corrected table: C_{b/3} = −1/6, C_{b/5} = −1/10. GRAM_INERTIA_001 (NUMERICAL):
the lines Zσ^{(m)} are 10³²–10³⁴ times ρ_p (33-digit cancellation); the lattice Gram matrix is PD and its only null vector is
μ⊕1; falsifier vectors carried over on fixed G give ≫ 0. **Restriction 25:** the sign is not in the inertia of the lattice Gram
matrix nor in the coefficients C_q/M̃; it lies within the cancellation direction imposed by admissibility (band, Tate).
Open cell: form of 𝒲_ext in a basis adapted to the cancellation (Schur complement along v). Row D OPEN.

### Addendum AUDIT_L_SHARP_14: uniform prolate envelope (CC_001)
CC_001 audited: ACCEPTED WITH ERRATA. Adiabatic invariant G = √Pψ² + (pψ′)²/√P (P with ϑ_k, not χ_k), decreasing energy E,
|ψ| ≤ |ψ(1)|, G = G_∞e^x with |x| ≤ σ, envelope 1.57 and J₀ form (10.3): PROVED; κ = 1.159 (35 survives). Numerical (c = 94–804,
k ≤ 24): constants 3–20× slack, real η ≈ −0.02 at c = 201. **Restriction 26:** thm:ext-layer(iii) is PROVED as an
asymptotic theorem; the explicit bound on η is non-empty only for N ≳ 130 — every quantitative use of the layer at N ≤ 130 (e.g. N = 15)
remains NUMERICAL. A tool, not a sign. Row D OPEN.

### Addendum AUDIT_L_SHARP_15: Schur board (DD), exterior variational (EE), 2×2 test
- Verdict: all three ACCEPTED WITH CORRECTIONS; no new PROVED beyond identities, elementary bounds, and NO-GOs.
- The raw board ⟨v,S_V v⟩ ≥ W − ‖QGv‖²/c_Q holds on p (θ=0.466 ≡ 0.644) but FAILS on V_50 (θ_50 = 1.0075): only the exact resolvent (θ′_50 = 0.388) closes it.
- b_J ≤ λ_{J+1}(G) (interlacing): non-coercivity for J<20 is spectral, basis-independent.
- Exterior vector bracket (0.15) and ratio 0.189 = reformulation of W(g*)>0; EE 0.324 is another partition (inside p).
- Restriction 27: remaining cell = board with exact resolvent and uniform margin at leakage scale; operator-level coupling in exterior variables OPEN. Measured margin 0.612 (μ=15, J=50). Row D OPEN.

### Addendum AUDIT_L_SHARP_16: translate comb (FF), renormalization (GG), Möbius kinks (HH), KINKS/SAWTOOTH tests
- FF.1 (Ψ̌ = Σ_{N≥μ}c_N N^{−1/2}τ_{log N}g + gauge mirror) PROVED, but does NOT escape Restriction 25: the comb is O(0.1) at depth ≥1 and cancels ~33 digits against Φ_{φ₀}(−x); GG.1 is an identity with ~70 digits.
- FF.2 corrected: Ψ̌^{(k)}(a+) = [1+(−1)^k c_μ μ^{−1/2}]g^{(k)}(a) (k ≤ 2); the gauge jet is O(1). The gap 2 ≤ N < μ is shared with a_P (two-term mirror): it is not Λ-specific.
- HH/TEST_KINKS: divergent jets at ω ≤ 48 (ratio 54m/ω); kinks ≤ 20% and incoherent; the residual Δr_out is post-cancellation and gauge-dependent (canonical only mod 𝒢̄).
- SAWTOOTH: NOT SUPPORTED + no mechanism (W_T changes at μ = m only via Λ(m)); Λ reading 7/9, normalization-dependent.
- Restriction 28: the boundary jet is not a coordinate for ω ≲ 54m; remaining cell = 𝒲_ext over the prolate tail + non-local content of Möbius cells at leakage scale (coset mod 𝒢̄). Row D OPEN.
- AUDIT_L_SHARP_17 (MM/NN): local PR and threshold c ≤ 1 PROVED; σ₀ = 1.1923474 (van de Lune, verified). MM.2 "lossless loop" = reformulation of II_001 (CONDITIONAL). Passivity/small-gain class closed (NO-GO). "Boundary triples" residue is not a free cell: DEAD (R162_2702b). Row D OPEN.

### Addendum phase 208: quantifier audit

See `03-research/phase-208-node-scope-audit/README.md`. No new route:
pointwise ZCERT ≠ interval; node in N(T) ≠ full domain without P1.c′;
even sector ≠ full row without further reduction. Λ*1=log arithmetically separates
Λ from the removal of a single prime, but does not provide the pending
sign (do not reopen E.2/Möbius). No cell changes; row D OPEN.

### Addendum phase 209: first O1 attempt

`03-research/phase-209-nonlocal-kernel/`: precise SOS/PD/BR task and
effective non-locality controls. Compact J+C has no sign on H_A, no finite
codimension, no dense ideal P_b𝒟 (free coefficients). NO-GO only for that
repair on those domains; it does not apply to the Euler+FE domain nor to PW_T. No
positive kernel has been built, nor a link to Q_T. O1 and row D OPEN; no cell changes.

### Phase 209, continuation: partial critical anticorrelation

ANTICORRELATION_003 and CONSTRUCTOR_004: strict proof of geometric concavity
θ−1 and Cov_gaussian(v_p,v_q)<0 at every scale, p≠q. For coprime pairs
the counterterm G₀ is zero; the Mellin transform of B=τCov converges with sign in α1/4,
even across all powers of two fixed primes. Auxiliary positive, not global PSD
nor a link to Q_T. Diagonal/same-prime, global tail, height realization, and
erased specificity remain OPEN. See AUDIT_003/004. No cell changes.

### Phase 209, completion of Rα and explicit goal D

CONSTRUCTOR005/AUDIT005: canonical SPD −Rα on finite divisors via
κE_s|A−μ₁|²+∫τ|E_yA−μ₁|². Includes the diagonal/same-prime term from R, not Q.
The same identity survives finite deletion: the auxiliary sign is not specific.
The goal is to complete all of D; status active in GOAL_D_STATUS.md. Link 006
Poisson+map pending; no cell changes, and closure of D is not claimed.

### Phase 209 — FEΠ and checked contractions (2026-10-19)

006/007 and the corresponding checks: exact FEΠ with α↔1/2−α and nonzero
defect after deletion; module V_n contractive with positive Gaussian defect.
They do not imply Q. Pending: inversion in the completion/link form and domain;
do not take ambient adjoints for adjoints of the subspace. Goal D active.

### Phase 209 — inversion 008 (2026-10-19)

008/check 008: ambient inversion U with defect U G_n U = M_b G_n*;
b changes orientation at y=n. No adjoint equality and no H-invariance implied.
The primorial point-evaluation sequence has divergent Gaussian norm,
elementary proof: no vertical strong limit. Closability/invariance/map Q
remain OPEN. Auxiliary results change neither the status of D nor the active goal.

### Phase 209 — continuous link 009 (2026-10-19)

LINK009/AUDIT009: no C0 semigroup interpolates n^beta V_n in log n,
including D_n. The vector X₂−1/2 proves persistent separation at log scales
arbitrarily close. That DIRECT link is discarded, not O1 nor D.
Unitary compression of V_n also excluded; compression of D_n unresolved.
The broad P44 rem:nointerp is not used: SCOPE_P44009 gives arbitrary convex
interpolation. A distinct map Q_T with all its hypotheses is missing; goal active.


### Phase 209 — LINK010: regularity of a compression of D_n (2026-10-19)

LINK_010_SPECTRAL_REGULARITY computes, for every finite centered nonzero
observable A, increments with liminf ||D_mA−D_nA||²/log(m/n)^s>0,
s=2alpha, via n=1+kL, m=n+L outside the prime support of A.
Every realization D_n=P U(log n)J with fixed bounded maps and U unitary C0
requires INFINITE spectral moment s for JA: not Dom(|B|^(s/2)).
At alpha 1/4, moment 1/2 and domain power 1/4. PROVED, independent
re-check favorable in AUDIT_010. It only excludes compressions with that
regularity; the general compression remains OPEN, as does the link Q_T.
The normalized compression 009 is not reopened and the status of D is not changed.


### Phase 209 — LINK011: first continuous map computed and cross-checked (2026-10-19)

LINK_011_MELLIN_GAUSS_MAP constructs UF=Σ a_d(F)(X_d−1/d), with
 a_d=2∫ e^(x/2)F(x)W_d(e^(2x))dx at alpha 1/4.
Convergence in H by a_d=O_T(||F||/d), Sdd=O(d^-s); compact operator,
C∞ feature and smooth effective kernel. FEcoef for even F recovers exactly
C(F)=∫F cosh(x/2). Do not add the separate polar vector: it diverges; cancel
coefficients first. The equality Q_T=||UF||² on the continuous carrier is
FALSE for THIS map: high-frequency polar-corrected tests have
Q_T~log λ and ||UF||→0. The domination Q_T≥||UF||² remains OPEN, as for other
non-smoothing maps. No general NO-GO for O1, nor proof of D. Favorable re-check in AUDIT_011.
Precision 006: piece-by-piece G/Π/v correspondences are not required; a
TOTAL identity or domination on a dense core suffices for the form norm.


### Phase 209 — LINK012: domination 011 refuted by a certified test (2026-10-19)

LINK_012_DOMINATION_FALSIFIER keeps exactly the map U of 011 and
tests the inequality that had remained OPEN, without retrying the equality.
Explicit test T=4/5, ω=5π/8, r=3(ω²+1/4)/(9ω²+1/4),
F=(cos3ωx+r cosωx)/sqrt(T(1+r²)), even, H0¹ and EXACTLY polar-free.
Arb128 certification and analytic tails: Q(F)<.002351, while the positive
rank one of 005 gives ||UF||²≥κ|Σa_dv_d|²>.26134304. Remainder<−.25899.
Exact Laplace transform of the autocorrelation and the expansion K=2Σexp(−(2j+.5)u)
provide an independent check without gamma/comb quadrature:
Qupper<.001647953. Data/code in LINK012_data. Polar-corrected H1 approximation
extends the falsifier to the C_c∞ core. AUDIT_012 favorable, both scripts reproduced.
Only the EXACT scale of U011: no exclusion of small rescalings,
other maps/O1 nor D. This concrete domination is no longer an OPEN residue.
No P46 integration nor change of cells/counts. Full goal D active.


### Phase 209 — LINK013: every fixed scale of U011 fails for large windows (2026-10-19)

New difference written with respect to 012: U is not changed and scale 1 is not retried;
it computes the response of the same map on the EXPLICIT family of P46
lem:testfam as T→∞, and proves the previously open class of arbitrary constants.
The profile M(F)=∫Fh satisfies h(−∞)=−κ, h(+∞)=0, by a Riemann sum and positive
Mellin transform of m=y^−1/2−τ. For G_T=ω_k(x/T), k=ceil 21T/e, F_T=P(D)G_T,
the mass of G_T/T escapes compacts, the L1 derivatives are o(T), and
M(F_T)/T→γ1²κ/8. Thus E_T≥κM²≥c0T². The proof of P46 thm:margin/cor:margin1
(CITED, inputs Z1/Z2 and explicit formula only for this falsifier) gives
|Q_T(F_T)|/||F_T||²≤4e9T exp(−15.449T) for THIS FAMILY, not by inferring
a test from an infimum. Norm F² O(T^1.5) => |Q|/E=O(√T exp(−15.449T))→0.
There is no fixed c>0 with Q_T≥cE_T in all windows. Any eventual c(T)
requires c(T)≤C√T exp(−15.449T); its existence is not proved.
Analytic proof without new numerical computation; AUDIT_013 favorable, CITED input explicit.
No exclusion of other maps, nor new sign for D. No P46/cells/counts integration.


### Phase 209 — LINK014: removing positive pieces does not repair U011 either (2026-10-19)

Written difference: 013 discarded a LARGER form via κvv*; it did not imply
failure of subforms. Here each piece is proved directly with the SAME a_d of 011.
For Π, the profile K_y(x)=2e^.5x ΣWd(e2x)(qd(y)−1/d) is positive, L1 and
∫K_y=C(y)=κΣvd(1/d−qd)>0. Local CLT via Fourier for G_T and sup bounds on derivatives
=>B_FT(y)/√T→−γ1²g0 C(y)/4. Fatou on [1,2] gives EΠ(F_T)≳T.
For G_s, G(d,2)=(1−1/√2)d^−.5 1_even; profile h2 bounded with limits
−κ(1−1/√2)/2 and 0. Even Riemann sums + mass escape give L2(F_T)≍T; Cauchy covariance
=>E_G(F_T)≳T². κvv* already gave ≳T² in 013. With Q(F_T) CITED from the paper decaying
exponentially, EVERY fixed nonnegative nonzero combination AκG+Bκvv*+CΠ
with the SAME a_d of 011 has |Q|/E→0. No uniform positive domination constant.
No inferences from larger to smaller; new proof for both subforms.
No new numerics. AUDIT_014 and addendum favorable for the whole class.
Other maps, signed cancellations and T-dependent factors are not excluded.
Full goal D active/OPEN; no P46/cells/counts integration.


### Phase 209 — CONSTRUCTION 015: separate domain and exact PSD cone (2026-10-19)

New difference with respect to 008: small positive tilts over many high primes,
not the primorial whose Gaussian norm diverged. For H=Σp^-s→∞, t=H^-2/3,
Z_u=∏(1+tp^-u), A=∏(1+tXp)/Z_s−Z_1/Z_s is Haar-centered and satisfies
Es|A−1|²→0, ||TA||≤C(Z_r−1)/Z_s→0, r=(s+1)/2>s, via Πdd of 011.
This produces (√κ1,0)∈H. The bounded actions Dn of 007 generate pure Xd and give
H=L²(P_s)⊕V, V=closure TA0. T densely defined, NOT closable, with
explicit sequence f2−(D2A_j−A_j/2)→0 arith, image→q2−1/2≠0.
The 3 forms κG, κvv*, Π are energies of 3 genuine orthogonal projections.
The PSD cone in their REAL span over ALL of A0 is exactly a,b,c≥0.
With 014 this also closes global PSD signed combinations of that span with
the SAME map 011. It does not classify forms positive only on its image, nor other maps.
Ps is a product of valuations, NOT the zeta law on N. Not V=all Gaussian nor FE invariance.
No new numerics nor new zero input. AUDIT_015 favorable to the three theorems.
No sign of Q/D; full goal active, without P46/cells/counts integration.


### Phase 209 — LINK016: dense even polar-free image (2026-10-19)

New difference with respect to 015: global PSD is no longer assumed; the
annihilator of U_T 011 over ALL even polar-free tests is computed. At α 1/4,
for every T>0, closure U_T(P_Tev)=H, also for the polar-corrected C_c∞ core.
Proof: ηd=<fd,h>=O(d^-1/4), c=Σηd/d converges; the analytic annihilator profile b_h
satisfies b_even=λcosh. Integer atomic comb μ, a_n=Σ_{d|n}ηd−c, a0=0;
μ'=μ−λδ0/2 is anti-Fourier by Gaussian injectivity on even S' (integer lemma
included). The Fourier transform of an integer comb is periodic => μ' periodic => constant coeff;
Theta μ'(1)=0 forces 0; divisor induction ηd 0 => h 0. No new zero input.
Thus any continuous Hermitian form on H that is PSD on U_T(core) is globally PSD.
With 015+014 this also closes continuous signed combinations of the span of the 3 pieces
positive only on that image, with the SAME map 011. Not finite block E_N, not
discontinuous H forms, not other maps/T-dependent coefficients nor sign of Q. Favorable
independent re-check in AUDIT_016.md. Full D active/OPEN.


### Phase 209 — VIRTUAL_SOURCE_017: explicit trial of a virtual metric (2026-10-19)

On a new instruction from the user, a computable virtual source is tried.
Difference with respect to 008: the Gaussian metric is changed to y^(α−1)τ²dy;
no claim is made to repair the adjoint in the original Hilbert space. S=τ conjugates G_n
to unitary dilations and J_virtual to exact inversion. The unitary map
C F=2^(−1/2)y^(−α/2)τ^−1F(log y/2) realizes translations/reflection.
The positive sum of jump energies, plus Lévy gamma, satisfies on
the even polar-free carrier Q_T=E_pos−(A_T−C0)||F||²,
A_T=Σ_{log n<2T}2Λ(n)/√n and C0<0. Negative counterterm uncontrolled.
The construction works for any positive profile, also deleted;
the virtual sign selects neither the complete primes nor the FE of the paper.
Diagnosis: source not functional for D; returns to P1_BBSTAR/INV_N,
that known decomposition is NOT presented as a new route or progress on D.
Profile domain verified for 0<α<1. No numerics nor P46 modification.
No NO-GO against other virtualizations; D remains OPEN. Memo:
03-research/phase-209-nonlocal-kernel/VIRTUAL_SOURCE_017_METRIC_TEST.md.
Favorable independent re-check in AUDIT_017.md; identities and scope verified.


### Phase 209 — QRH: focused reading and conditional exponent map (2026-10-19)

QRH_SOURCE_RELEVANCE.md and QRH_EXPONENT_MAP.md review the requested
sources: Kintali 47/48; OpenAI 5 Oct 11/12; structural reading of
OpenAI 30 Sept 7/8. L74 corrected; do not confuse versions or formalizations.
Quanta reports human review and Lean for 30 Sept, not verified here.
PROVED: if there are H^κ replicas with error O(DH^-δ) and total energy
O(D^(a+ε)H^b), H=D^h, the extraction gives
θ=(1/2)max{a+(b−κ)h,2−2δh}. Sextic κ=δ=1/6, a=b=1, h=1+ϑ
recovers 11/12+5ϑ/12. That bound does not reach 1/2, even by enlarging only the range.
Impossibility of improvements is not proved, nor are the three fractions interpolated.
OPEN: better family/selective estimate and exact link with deficit 017.
The written critical replica estimate is a conditional target,
NOT a result of the paper or ours. No sign of D nor P46 integration.


### Phase 209 — QRH_REPLICA_COHERENCE: selective estimate examined (2026-10-19)

New computation on the p^6 replicas of the QRH source, after consulting
the index/grid/crossword. A closed sieve is not reopened as a proof of D.
PROVED: Ap6=A1−Bp, Bp=−ν(p)Σ_(p∤m)μ(m)ν(m)W(Np Nm/D).
For Np≈Y=√D, ideal counting gives |Bp|≪√D and mean variance≪D.
Exact identity Esel=|A1−barB|²+VarB. The uncentered control
Esel≪D^(1+ε), for all ε, is equivalent to |A1|≪D^(.5+ε), for all ε,
with renaming of ε. No new control of the coherent component was proved.
Independent re-check favorable after making these quantifiers precise.
QRH_EXPONENT_MAP updated: the proposed sufficient condition was
also necessary in this family; it does not count as an improvement in cancellation.
No general NO-GO, no external equivalence with D, no P46 integration; D OPEN.
Memo: 03-research/phase-209-nonlocal-kernel/QRH_REPLICA_COHERENCE.md.


### Phase 209 — continuation of the QRH coherent mean (2026-10-19)

Direct attack added in QRH_REPLICA_COHERENCE.md, with independent
re-check. Exactly C_D=ΣμνW w_D, w_D=1−r_D/J∈[0,1].
For D>(8v)², r_D≤2 on the support; mask close to 1 without new oscillation.
Bp=−ν(p)A1(D/Np)+O_W(1), with W fixed and uniform remainder: improving
the short scale reduces the error but does not control the long signal.
On expanding |C_D|², diagonal≪D by counting; real off-diagonal still without
an upper bound≪D^(1+ε). No critical estimate of C_D was obtained,
Vaughan/generic sieves are not relaunched and no general NO-GO is declared.
This diagnosis is not positive progress on D nor a proof of cancellation.


### Phase 209 — QRH 7/8 and hyperbolic projection (2026-10-19)

QRH_HYPERBOLIC_PROJECTION.md, independent re-check favorable.
Difference with respect to Green/hyperbolic models already indexed: exact projected norm,
frequency and inflection position; no new source nor reopening.
PROVED in even polar-free L², b=.5: for fixed 0<a<b and fixed γ,
||P_b cosh((a+iγ)x)||²/||cosh((a+iγ)x)||²→
[(b−a)²+γ²]/[(b+a)²+γ²]. At a 3/8, γ 0: ratio 1/49,
residual norm²~(2/147)e^(3T/4). The attenuation disappears at high
frequencies, also for fixed T. Exact Cauchy bound on moments.
The corrected real profile has a positive inflection at T−8log(128/63)+o(1)
for a 3/8, b .5, and another symmetric one. Cosh itself is globally convex.
Sept Lemma 20.2 certifies 49/440640 in the compensated exponent, not a margin for D.
The 7/8 strip does not identify the fluctuation with cosh 3x/8 nor give amplitude/sign.
Without control of the counterterm 017, without a new critical estimate nor P46 integration.
It is a geometric bound/diagnostic model, not positive progress on the sign of D.


### Phase 209 — arithmetic trial QRH 4/5 (2026-10-19)

QRH_FOUR_FIFTHS_ATTEMPT.md, independent re-check favorable with
explicit conditional scope. The user asks to adapt the Sept 30 proof, not just
the hyperbolic model. Locally, the same Euler identities give H−1=O(Q^-87/50)
in the box x≥4/5, z≥33/200, w≥19/20; main multiplier −1+O(Q^-4/5).
It is not an extension of the whole proof. The published low bound 3/16 leaves a deficit of 3/40.
On trying free geometry while keeping the majorizations, a loss appears
(5ell−1+d)_+/4 in the completed square norm; after CS/tuple summation,
σlow=11/12−ell/4+(5ell−1)_+/8, FORMAL minimum 13/15 at ell 1/5.
Thus the current certificate does not reach 4/5 by varying only lengths; it needs
at least an additional 1/15 in the low exponent (not sufficient for the high one).
No 13/15 theorem, no universal barrier, no closure of D. Scalar candidate
ell 1/5, b 1/10, lx 7/20, ly 9/20, h 17/20 pending global validation.
X'≥1 is not used as a published hypothesis and CII=s−11/16 is not confused
with CI=s−2/3. Geometry/high tests outside the original remain OPEN.


### Phase 209 — goal QRH 4/5 and low/high validation (2026-10-19)

The user sets a new explicit goal: prove Re(s)>4/5; goal created and active,
not achieved by formal/intermediate results, not equivalent to closing D.
QRH_LOW_CANDIDATE_VALIDATION: bound 11/60 for ell 1/5, b 1/10 under
declared external lemmas CITED; supports, masks, uniform profiles reviewed.
QRH_HIGH_CANDIDATE_AUDIT: the same supply slots pass; the floor certificate
does not close (49/1500 at the endpoint 13/15). Joint formal inf 167/192, not a theorem
nor universal NO-GO. Dynamic kappa outside 18.1 requires attention, but
kappa 3/4 can be tried with input beta*≤7/8; do not declare an unavoidable barrier.
GOAL_QRH_FOUR_FIFTHS_STATUS.md records the goal, status and pending work.
Independent re-check of computations; no new free region proved.


### 2026-11-04 — Elementary cases of powers

PROVED, with independent re-check: `03-research/phase-211-sign-sandbox/POWER_CONE_001.md`, exterior sign in each plane of two powers with exponents >=32 (not envelope, not PW_N). FALSIFIED: positive cosh/log-convexity implies the sign of mixtures; H=3+cosh and vector (42,-41) give -129/(34 log2). It is not a counterexample to the arithmetic datum. OPEN: P3, all orders and the bridge in form norm, in `PROPOSAL_POWER_CASES_2026_11_04.md`. Pick antecedents known; novelty limited to the explicit lemma. `NEAR_CASES_RESULTS_2026_11_04.md`: auxiliary nearfree improvement and counterexamples to monotonicity by contact/automatically favorable cycle; no global NO-GO.


### 2026-11-04 — Active goal: powers, step 002

`POWER_AUDIT_002.md` confirms normalization and polarization. `POWER_THREE_002.md`: PROVED/checked case of three rates in [u,3u], u>=2^30; constructive extension to n rates with u>=2^{40n} and quantitative obstruction to density (§§7–8 approved by independent re-check). `POWER_BRIDGE_002.md`: bridge in weighted fractional norm to PW_N; independent re-check favorable §§1–5. The fixed family a=32+k is dense for transporting the sign if ALL its orders are positive. Hence the bridge obstacle is no longer the main target: what remains is the sign at all orders of a single dense family. Thresholds growing with n do not suffice because of concentration. Next target: matrices K_ij=(L(32+i)+L(32+j))/(63+i+j), without confusing finite cases with closure. No paper is modified.


### 2026-11-04 — Powers, step 003 (checked)

`POWER_STATE_003.md` summarizes the current record. PROVED/checked: bridge for PW_N and compact test via finite Möbius, fixed family 32+k sufficient; six orders of `POWER_FIXED_GRID_003.md` certified in Fraction with remainders and independent rerun. `POWER_POLYNOMIAL_003.md`: exact Jacobi identities, no uniform sign. `POWER_SCHUR_003.md`: F=(z²−z+10)/10 has F increasing and F/z decreasing on [1,3], but detK(1,2,3)=−13/270000; falsifies induction from pairs/monotonicities, not the arithmetic datum. Concavity does not suffice either (piecewise falsifier §7). Next: confluent case and check of rate movement; monotonicity only a hypothesis to prove/refute. General P3 and all orders remain OPEN. No global closure nor paper edits.


### 2026-11-04 — Powers step 004: complete P3 PROVED

`POWER_STATE_004.md` is the current state. `POWER_POLE_MOVEMENT_004.md`+`POWER_CONFLUENT_004.md`, checked in `POWER_AUDIT_004.md`: Q[Σ_{i=1}^3 c_iX^{-a_i}] >= ||Σc_iζ(a_i)e^{-(a_i−1/2)y}||²/20 for ALL a_i>=32, without separation/upper bound. Includes P3 A>=32, h>0 and unequal triples. Proved insight: moving the poles reweights the density by an increasing R(|τ|); positive covariance with m gives monotonicity of all ARCHIMEDEAN eigenenergies. Confluent certificate >.1 and comb losses<.003, negative polar<.042. Next: order 4 keeping positive polar; movement does not transfer automatically to the full form. All orders remain OPEN; papers untouched.


### 2026-11-04 — Powers steps 005–006, verified

Current state `POWER_STATE_006.md`. PROVED/checked: confluence 4 a32, W>norm²/5 although ARCH admits a vector<−norm²/10 (`POWER_CONFLUENT_FOUR_005`). Individual derivative ARCH+POLAR>1/420 for every numerator of degree<4 at confluence 31.5, rational SOS (`POWER_POLAR_MOVEMENT_005`, check 005); LOCAL only. Explicit test 12: AP<−norm²/100; all contacts positive, n2 alone repairs; W>norm²/50. Deleting ONLY contact 2 while keeping powers 4,8,... produces W<−norm²/125 (`POWER_ARITHMETIC_WITNESS_006`, check 006, remaining tail<norm²/500). These are new concrete cases, not novelty of general arithmetic necessity nor closure. All orders and arbitrary quadruples remain OPEN.


### 2026-11-04 — Powers 007: exact limit of arch+polar transport

`POWER_HIGH_ORDER_PM_NOGO_007.md`, checked in `POWER_AUDIT_007.md`: for numerator 1 with n=2^17 confluent poles u=63/2, the AP Rayleigh quotient decreases when any of the poles increases (u∂_jE<−140/(31n)). Scalar proof with 0<=τm'(τ)<4 and exact polar; no huge spectrum computed. FALSIFIED only the numerator-fixed AP monotonicity for all orders at high rates. It is NOT a falsifier of λmin, nor of the sign, nor of the ARCH movement, nor of the local theorem 4. Therefore do not extend that mechanism to all orders; joint cancellation with the comb, or a weaker property that preserves sign, still has to be treated.


### 2026-11-04 — Powers 007–008: arithmetic block and contrary pattern

`POWER_STATE_008.md` is the current state. PROVED/checked in `POWER_BLOCK_AUDIT_007`: W>norm²/10000 for EVERY Laguerre block of dimension 12 at rate 31.5, all contacts/crossings (`POWER_ARITHMETIC_BLOCK_007`, independent Fraction verifier PASS). ARCH+POLAR indefinite there; contact 2 repairs the matrix and tail norm<.0006. PROVED/checked in `POWER_AUDIT_008`: f=(D²−.25)[y^(n−1)e^-31.5y], n=2^17, zero polar, ARCH<−3.83norm², ALL prime contacts <=1024 hurt. No negative sign of W is claimed: the tail is open. Refutes a universal pattern of repairing low contacts, not a new global NO-GO on finite combs. Arbitrary quadruples, all orders and the sign of Paper 46 OPEN; bridge is PROVED. Papers untouched.


### 2026-11-04 — Powers 009–012: up to seven arbitrary poles

`POWER_STATE_012.md` is the current state. PROVED/checked: all spaces of 4,5,6,7 real poles>=31.5, multiplicities included, have W>c||f||² with c=2/25,1/100,1/25,1/500 respectively (`POWER_FOUR_GLOBAL_009`, `POWER_FIVE_GLOBAL_010`, `POWER_SIX_GLOBAL_011`, `POWER_SEVEN_GLOBAL_012` and checks). Independent Fraction verifiers PASS. New step: exact transport of margin by filter, localized spectral deficit and maximal weighted trace at confluence (`POWER_COMMON_TRANSFER_010`). No AP monotonicity is claimed, nor of the largest weighted eigenvalue. Bridge to the whole domain is proved, but it requires all orders, still OPEN. `POWER_TATE_CHAIN_009` gives the exact second difference of the complete sum; convexity open, limit E0 already known, individual family not dense. Papers untouched.


### 2026-11-04 — Powers 013: limit of the pointwise bound at order eight

`POWER_DEFICIT_LIMIT_013`, `POWER_DEFICIT_AUDIT_013`, Fraction verifier PASS: a rational vector gives base margin AP8<1/25, but the mandatory direct pointwise uniform loss exceeds 1/20 (evaluation τ4, m4<−2/5), for any c>=0. Includes the best bound of the full product, not only separate maxima. FALSIFIED the possibility of closing 8 by that criterion that discards the positive gain, even with optimized constants. No claim of negative AP/W nor impossibility of another transport. Authorized pivot: keep the signed integral/spectral structure, do not repeat pointwise optimization. Global 7 remains PROVED; all orders OPEN.


### 2026-11-04 — Powers 014: eight arbitrary poles and confluent bridge

`POWER_STATE_014.md` current. PROVED/checked: W>||f||²/1000 for ALL spaces of eight real poles>=31.5, multiplicities allowed (`POWER_SIGNED_TRANSFER_014`, `POWER_SIGNED_AUDIT_014`, Fraction verifier PASS reproduced). TEL decomposes the signed correction into energies of nine poles with numerator zero at 0; its confluent restricted ARCH>1/4 allows going beyond 013 without a pointwise bound. `POWER_CONFLUENT_BRIDGE_014`, independently checked: all single-rate blocks suffice by strong weighted H1 density; does NOT require a margin uniform in size. `POWER_PRIME_TRANSFER_014`+check: Wfv−R0Wfu=(1−R0)WG exact with ALL contacts/polar; the sign of the corrections at every order remains to be proved. Do not extrapolate eight/block 12 to all. Papers untouched.


### 2026-11-04 — Powers 015: complete mixture and uniformly positive tail

`POWER_STATE_015.md` current. PROVED: `POWER_GEOMETRIC_TRANSFER_015` expresses transport as an absolutely convergent positive mixture of W[Q^k f], including polar and ALL contacts; Rayleigh weights incorporate norms. PROVED: `POWER_HIGHPASS_015`, checked in `POWER_HIGHPASS_AUDIT_015`, for each fixed u>1, N, W>0 on ALL of Q^k V_N for k large enough, uniformly in numerators. ARCH/norm² >=.5 log k−C_N; complete comb and polar/norm² tend to 0. New difference: the complete signed energy is kept and its tail controlled through Gram matrices, avoiding the pointwise deficit 013 and the falsified patterns 007–008. An initial segment remains without sign or effective endpoint; no uniformity in N nor global closure. Eight arbitrary poles remains PROVED. Papers untouched.


### 2026-11-04 — Powers 016: exact defect, binomial interior and limits of descent

`POWER_STATE_016.md` current. `POWER_DESCENT_016`: PROVED Wf=WQf+WLf complete and finite differences eventually positive at fixed order. Exact binomial weights follow p=tau²/(u²+tau²); the border covered in 015 loses mass AND energy, the joint interior remains OPEN. `POWER_JOINT_SCALE_016`: PROVED Beta(k+.5,N−.5) for P1, contacts->cos(u sqrt(c)t) if k/N->c; temporal mean (N−.5)/u independent of k and explicit variance. FALSIFIED making the disappearance of contacts uniform in a linear cone and weights exponential fixed in N in any cone; does NOT falsify sign cones. `POWER_DESCENT_AUDIT_016`: zero moments prevent strong density of tails even toward primitive data; increasing k only admits a strong limit 0 in common weight. W−4norm² keeps structure+eventual but negative initially (Fraction verifier PASS): NO-GO only for structural inference. New difference with respect to 015: localize pending mass and energy, do not repeat the high-frequency bound. Global OPEN; eight poles remains PROVED; papers untouched.


### 2026-11-04 — Powers 017: scalar bridge via positive coefficients

`POWER_SCALAR_BRIDGE_017.md`: written proof, independent conceptual check of map and sign; formal check of the step in progress. PROVED algebraically: the sign of ALL atoms s^k/(s+u)^(N+k), N>=1, k>=0, suffices for all confluent blocks. Rational density = base weight times R(q)>=0 on [0,1]; R+epsilon admits an EXACT Bernstein expansion of high degree with positive coefficients. The rational identity preserves polar on evaluating x=-1/4 and the whole comb; epsilon->0 controls crossings without inferring positivity of an envelope from a union. Explicit difference: conic use of densities, not the density of tails refuted in 016. The classical degree-elevation lemma is not presented as new. Complete scalar table OPEN; does NOT certify any new window T>log(5)/2. Additional constructions 017 under check; papers untouched.


### 2026-11-04 — Powers 017: infinite row and quadratic cone with complete comb

`POWER_STATE_017.md` current. PROVED/checked: `POWER_INTERIOR_017` covers N1, ALL k>=0, u>=31.5 with W>4norm²/3 (Fraction verifier PASS); WRN offers an effective bound of weighted norm for each N for all k, not a general sign. `POWER_QUADRATIC_017`: for each c>0, P1 has W>0 for ALL k>=cN², N>=N0(c) explicitly boundable. New method: shift the joint rational DENSITY, do not separate temporal norms; the envelope Ce^-t sums the WHOLE comb and allows a complete arithmetic Gaussian profile. Differs from the E0 package and avoids obstacle 016; polar is not omitted. `POWER_SCALAR_BRIDGE_017` fully checked twice independently: ALL scalar N,k suffice for all matrices by the conic Bernstein identity of densities and rational polar. Complete table OPEN; no new window T certified. Numerical extension of the cone under separate check. Papers untouched.


### 2026-11-04 — Powers 017: explicit numerical cone from dimension two

`POWER_QUADRATIC_EXPLICIT_017`: PROVED, complete proof independently re-checked and Fraction verifier PASS. At u31.5, P1, ALL N>=2 and k>=10000N² satisfy W>49norm²/50. Shifting the density to Im z 15 gives autocorrelation<5e^-15|t|; complete comb and polar <norm²/1000 each, ARCH>99norm²/100. Difference with respect to QUADRATIC017: eliminates the unknown/conservative N0 via a wider band and exact normalization. Does not claim a cone for every numerator nor a sign below the parabola. With row N1, what remains in the sufficient scalar target is N>=2, 0<=k<10000N². No new window T certified. Additional check against the map and the sign APPROVED (POWER_INTERIOR_AUDIT_017 §9 and POWER_QUADRATIC_EXPLICIT_AUDIT_017); papers untouched.


### 2026-11-04 — Powers 018: first two differences and error budget

`POWER_STATE_018.md` current. `POWER_TABLE_DESCENT_018`: PROVED/checked against the map, Fraction verifier PASS, W>norm²/8 in rows N2, N3 for ALL k>=0, u>=31.5. The complete recurrence gives strictly positive first and second differences of row 1, not complete monotonicity. Preserves polar parity and the WHOLE comb via WRN. `POWER_LOW_TABLE_018`: exact budget D_N(theta)=2+2theta J_N(theta−.5), D_N(0)=2, growth sqrtN at .5 and exponential for theta>.5; endpoints and regimes checked. Only quantifies the known loss of absolute bounds, not a new sign nor global NO-GO. Remaining sufficient region N>=4, k<10000N²; no new window T certified. Papers untouched.


### 2026-11-05 — Check 018 and falsifier of structural descent

`POWER_TABLE_AUDIT_018` saved and re-checked. Approves rows 2,3 and LOW budget. The explicit model V=2norm²−u|F(iu)|²/100 preserves recurrences/mixtures, margins of all spaces of up to 12 poles>=u, complete rows 1/2/3 and the cone k>=10000N², but V has a negative entry N40402, k40401. Elementary proof via the arcsine measure minus an atom at 1/2 and binomial coefficients. Difference with respect to W4 of 016: it also preserves the known positive regions and margins. It is NOT W and keeps neither its arithmetic datum nor the exact logarithmic profile. NO-GO only for structural inference based on those properties; real sign OPEN. The next step requires a signed arithmetic inequality. Papers untouched.


### 2026-11-05 — Powers 019: signed transition of the comb and mean of dilations

`POWER_STATE_019.md` current. `POWER_ARITHMETIC_DIFFERENCES_019` PROVED/checked: autocorrelation k1 with a unique positive root for ALL N and frontier O(sqrtN); ALL contacts help for 1<=N<=211, u>=31.5, complete comb>0. At k0 comb<0 for ALL N; does not imply the sign of W. Fraction verifier PASS reproduced on independent reruns. `POWER_SIGNED_MEAN_019`: B(x)=log(n!)−xHn+n<=−(1−log2)(x−1) gives a negative signed mean of dilations; Euler identity known, specific kernel application. Adjoint inverse mu(m)mH(mx) exact; prefix 3 negative for N>=2^17, WITHOUT conclusion about the complete inverse. `POWER_SIGNED_AUDIT_019` approves both. W coverage not enlarged: rows 1/2/3+cone 017; global and new windows T OPEN. Papers untouched.


### 2026-11-05 — Powers 020: complete exterior inverse and deficit of the first contact

`POWER_STATE_020.md` current. `POWER_INVERSE_KERNEL_020`: PROVED H_N/4<=h_N<=7H_N/4 for ALL N>=2, log x>=(N−1)/30, with COMPLETE Möbius tail dominated via positive coefficients. N2 inverse positive for ALL x>=1. Potential negative part localized in an explicit interval; interior pairing OPEN. Difference with respect to 019: not a prefix but the complete sum. `POWER_SIGNED_BALANCE_020`: PROVED ARCH+POLAR+P2<−.66norm² at N211, k1, u31.5; remaining positive contacts not omitted and W undecided. Refutes repair by the first contact, not every finite comb. Both Fraction verifiers PASS on independent reruns; POWER_BALANCE_AUDIT_020 approves. No new W coverage nor window T; papers untouched.


### 2026-11-05 — Powers 021: balance of one atom and complete arithmetic tail

`POWER_STATE_021.md` current. `POWER_CONTACT_BALANCE_021`: PROVED at N211, k1, u31.5, ARCH+POLAR+P2+P3+P4<−.21norm²; and 0<sum_(q>300)Pq<5e−13norm². Fraction verifier PASS; analytic tail by unimodality/logarithmic derivative/recurrence of integrals, without extra enumeration. NUMERICAL 45/65 dps: partial up to 300≈−6.0812e−14, quadrature error not certified; NOT an interval for W nor a sign deduced from that figure. New reason with respect to 020: magnitude of several contacts and bound of the complete tail at the same point; not an N campaign. W coverage and windows T unchanged; global OPEN; papers untouched.

Independent check 021 completed: `POWER_CONTACT_BALANCE_AUDIT_021` approves FAIL234/TAIL and keeps the partial diagnosis NUMERICAL; no sign of W deduced.


### 2026-11-05 — Powers 022: complete Möbius inverse negative at one point

`POWER_STATE_022.md` current. `POWER_INVERSE_INTERIOR_022` + `POWER_INVERSE_INTERIOR_AUDIT_022`: PROVED −2/3<h128(1)<−33/50; reinforced Fraction verifier PASS on independent reruns. Segment m<=64 and COMPLETE TAIL<1e−10; difference with respect to 019 prefix and 020 outer: falsifier of the complete inverse in an interior region. By continuity hB adverse near 1; exterior positivity 020 remains. FALSIFIED only global h_N>=0, NOT W nor ERR. Pivot: exterior primitive and weaker condition K=J+xh, still under investigation. W coverage and windows T unchanged; papers untouched.


### 2026-11-05 — Powers 023: compensated criterion and signed cell weight

`POWER_STATE_023.md` current. `POWER_CUMULATIVE_INVERSE_022`: PROVED mass sumJ(n)=1, CONDITIONAL criterion K=J+xh>=0⇒ERR<=−2(.75−log2)(1−J1), and representation ERR=−2∫K C_B with C_B>0, exterior bound (.75−log2)/2 and border damage<=delta² supK^-. No W compensation inferred. `POWER_CUMULATIVE_TEST_023`+check: PROVED −1/250<K129(1)<−1/251, COMPLETE sum and tail<1e−10, Fraction PASS on independent reruns. FALSIFIED universal K>=0, although K128(1)>0; no ERR/W negative claim. New reason: the compensated condition tolerates negative h and is proved separately from the already refuted criterion 022. W/T coverage unchanged; papers untouched.


### 2026-11-05 — Powers 024–025: complete arithmetic mean favorable despite the negative kernel

`POWER_STATE_025.md` current. `POWER_CELL_BALANCE_024`: uniform cell budget tolerates K^-; no universal favorable domain claimed. `POWER_CELL_TEST_024`: PROVED S129(2)>.33 and first cell KC_B>.31, exact polynomial integrals and complete Möbius sum. `POWER_INVERSE_LOGCONCAVITY_025`: decreasing coefficient ratios of D_N⇒log D concave for ALL N. Rational check D129'(2/3)<30D129(2/3)⇒K129>0 for ALL x>=2⇒all remaining cells positive. Combined: ERR129<−.66 COMPLETE, not a prefix. Fraction verifiers PASS on independent reruns, checks 024/025 approved. New difference vs 023: integration compensates K129(1)<0 and the improved cutoff uses specific log-concavity, not false pointwise positivity. ARCH_sharp pending; NO new W/T. Papers untouched.


### 2026-11-05 — Powers 026: uniform cutoff and signed joint kernel

`POWER_STATE_026.md` current. `POWER_UNIFORM_CUTOFF_026`: PROVED two analytic cutoffs t_J and t_R for ALL N, of order (N−1)/330 versus the previous (N−1)/30; COMPLETE Möbius sum K positive outside the cutoff and exterior cells favorable. Uniform range ALL 2<=N<=129, x>=exp(2/3), by monotonicity and endpoints, not certified row by row. New difference vs 025: Jensen on coefficients and Riccati barriers eliminate per-dimension checks. `POWER_ARCH_CELL_026`: ARCH_sharp129<−.81; guaranteed benefit .66 insufficient, WITHOUT conclusion W<0. The joint identity W/norm²=∫K Omega keeps all cancellations, but Omega(3/2)<−.1: FALSIFIED only pointwise positivity of the joint weight. Real gamma constraints still available. `POWER_ARCH_CELL_AUDIT_026` approves both; two Fraction verifiers PASS on independent reruns. W/T coverage unchanged; interior and global sign OPEN; papers untouched.


### 2026-11-05 — Powers 027: exterior joint contribution and its magnitude

`POWER_DISCRETE_BALANCE_027`: proof re-read and Fraction verifier reproduced PASS; independent re-check APPROVED in POWER_JOINT_AUDIT_027. Complete formula for Omega by floors and bound Omega(t)>=ell−(4log t+9)/t, ell=1+gamma/2−log(4pi)/2>1/50; hence Omega>9/1000 for t>=4096 outside integrable singularities. With the gamma cutoff 026, EVERY joint tail int_T^infinity K_N Omega is positive for T>=max(4096,exp(tau_N)), with explicit majorant. In the single N129: 0<tail 4096<10^-36. Difference vs 026: inequality for the real contribution of W, not just ERR nor an identity; the magnitude bound prevents attributing a large compensation to it. Masses sumK(n)=3/2 and sumK(nx)=x^-32 D(log x) recorded as known inversion identities, not a proof of sign. Interior and global W OPEN; W/T coverage unchanged; papers untouched.


### 2026-11-05 — Powers 027: gamma constraint and direction of Jensen

`POWER_STATE_027.md` current. `POWER_INTERIOR_CONSTRAINT_027`: REAL heat mixture already known in 018, now a specific positive weight L_N(a)=E(V_N−a)_+−(EV_N−a)_+ for the remainder with respect to the Gaussian with equal second moment. Complete identity Wgamma−G_W(EV)=∫L_N G_W'' keeps all pieces. Mass L=VarV/2 only N>=3; N2 treated without variance. Strictly concave ARCH_sharp gives an UPPER bound, refuting the proposed lower direction. G_W''(a)<0 for ALL a>=65536 refutes global convexity of the real functional, NOT W nor the sign of the specific remainder. Explicit difference: inverse gamma law fixed and gap weight, not an arbitrary mixture nor heat rebranding. `POWER_JOINT_AUDIT_027` approves both memos 027, verifiers PASS on independent reruns. Interior, W/T coverage and global sign without closure; papers untouched.


### 2026-11-05 — Powers 028: complete fourth row of positive W

`POWER_STATE_028.md` current, N5 still pending. `POWER_ROW_FOUR_028`: PROVED W[f_(4,k)]>norm²/50 for ALL k>=0, ALL u>=63/2, with the WHOLE comb and polar. Exact ARCH and u/k monotonicities give>11/400; WR eta12 gives comb<3/500; odd polar<1/1000, even favorable. Difference vs 018: preserve the margin of the ARCH4 formula and change the autocorrelation weight, not inference from recurrences nor a sweep. Third difference of row 1 strictly positive as a corollary, not complete monotonicity. `POWER_ROWS_AUDIT_028` approves ROW4; Fraction verifier PASS on independent reruns. New REAL W coverage: rows 1..4; rest of the table N>=5, k<10000N² at u31.5. No new window T certified nor global closure; papers untouched.


### 2026-11-05 — Powers 028: complete fifth row and separation of the polar border

`POWER_STATE_028.md` updated. `POWER_ROW_SPLIT_028`: PROVED W[f_(5,k,u)]>norm²/25 for ALL k>=0, u>=63/2; for k>=1 margin 4/5. ARCH50(u0)<−.1 shows why the positive ARCH0 condition does not suffice. New argument vs 018/ROW4: k0 exploits positive polar with opposite extremes on u∈[u0,2u0], and positive ARCH for u>=2u0; k>=1 uses covariance from 1. COMPLETE comb<.06, odd polar<.002, rational certificates of extremes and analytic monotonicities. Identity A_N1=A_N0+uA_N0' and general sufficient criterion recorded, without extrapolating premises. `POWER_ROWS_AUDIT_028` approves both rows, verifiers PASS on independent reruns. New W coverage rows 1..5; fourth difference of row 1 positive. Remaining sufficient region N>=6, k<10000N² at u31.5; no new window T nor global closure. Papers untouched.


### 2026-11-05 — Powers 029: limit of the positive bridge with growing rates

`POWER_SCALE_BRIDGE_LIMIT_029`: PROVED/independent check against the map APPROVED. Every normalized spectral density of the atom N,k,u has height<sqrtN/(u sqrtpi); the maximum decreases with k by elementary comparison of trigamma with a midpoint integral, and the endpoint k0 is bounded by gamma Cauchy–Schwarz. Hence the cone of positive mixtures with u>=C sqrtN has uniform height 1/(C sqrtpi). On I=[−C/8,C/8] its mass<1/4, while an atom p_(M,0,31.5) has mass>3/4 for explicit large M; L1 distance>1/2. Difference vs 016: obstruction of the CONE of densities with variable rate, not exponential weights at fixed rate. Prevents automatically replacing the bridge 017 by that region; does NOT refute W nor other mechanisms. Papers untouched, global sign OPEN. Positive region theorems 029 still under construction/check.


### 2026-11-05 — Powers 029: uniform positivity with quadratic scale

`POWER_STATE_029.md` current. `POWER_ROW_PATTERN_029`: PROVED W>.7norm² for ALL N>=2, k>=1, u²>=256N. `POWER_BOUNDARY_WEDGE_029`: PROVED W>.4norm² for ALL N>=1, k>=0, u²>=4096N. Both with COMPLETE comb and polar. Difference vs 016/018: CS with opposite weights and comparison of coefficients S_N cancel the cost N eta/u; control by N eta²/u² remains. ARCH via Euler+beta moments for k>=1; the spectral height bound and integrable resolvent cover k0. `POWER_SCALE_AUDIT_029` approves the three memos including the bridge limit; two verifiers PASS on independent reruns. Not an N campaign. NEW real region at variable rates, WITHOUT enlarging the u31.5 table nor window T: rows 1..5+cone 017 remain the fixed coverage. The obstruction of the cone of densities recorded above prevents inferring an automatic bridge. Papers untouched; global OPEN.


### 2026-11-05 — Powers 030: gamma–Gaussian cost against the real law

`POWER_GAMMA_BALANCE_030`: PROVED/CHECKED, Fraction verifier PASS on independent reruns. For ALL N>=2 at u31.5, 0<A_sharp(EV)−ARCH_sharp_gamma<=.5[psi(N−.5)−log(N−1.5)]<1/[2(N−1.5)]. Uses K_sharp<=1/t and the EXACT moment ∫L_N/a²=log EV−E log V, finite also for N2; constructive O(1/N) control of the real loss. Moreover in the single N2, Wgamma/norm²<.85 and G_W(EV)>.875 ⇒ COMPLETE gap against L2<−1/40. Refutes comparing Wgamma>=W Gaussian without correction, NOT W negative (row N2 positive). Difference vs 027: specific pairing with the real law and uniform budget, not generic curvature nor arbitrary mixture. `POWER_INTERIOR_AUDIT_030` approves; parallel interior block pending. No new W/T coverage, signed arithmetic compensation still OPEN; papers untouched.


### 2026-11-05 — Powers 030: compensation of a real block at fixed rate

`POWER_STATE_030.md` current. `POWER_INTERIOR_SCALE_030`: PROVED int_1^(9/4)G_N H>1/100 for ALL N>=2^20 at FIXED u31.5, including the adverse contact 2. Adjoint inversion of Omega cancels singularities at integers>1 and gives an explicit H with sum_q Lambda(q), keeping the complete W. Difference vs 026/027: real integrated INTERIOR block and uniform gamma error O(1/N), not another tail nor an assumed sign of the weight. Exact main integral>1/50, error<1/200. Primitives H and x²H up to 5/2 negative refute only the criterion of positive primitives; the block is rescued by real comparison. `POWER_INTERIOR_AUDIT_030` approves both memos 030; verifiers PASS on independent reruns. Remainder from 9/4 still OPEN; NOT total W positive nor new coverage/T. Papers untouched.


### 2026-11-05 — Powers 031: real adverse prefix, recovery and initial global cost

`POWER_STATE_031.md` current. `POWER_WEIGHTED_BLOCK_031`: PROVED at u31.5, prefix up to 225/64<−.003 for ALL N>=2^24; block up to 4>.015 for ALL N>=2^22; recovery between endpoints>.018 for N>=2^24. Contacts 2/3 intact, endpoint q4 cancels. Universal I_*>=0 FALSIFIED, not W negative; uniform gamma error without an N campaign. `POWER_GAMMA_WEIGHT_031`: PROVED unique maximum of R before 2/3, q''<0, overshoot<=2M2/9 and TV<=1+4M2/9; W/norm²>=int_(T)^infinity I_*(e^t)(−R')dt−M2. Difference vs 030: real TOTAL variation and initial adverse cost O(1/N), not only a finite block/identity. Signed arithmetic average pending. `POWER_WEIGHTED_AUDIT_031` approves both; block verifier PASS on independent reruns. No new W/T coverage nor global sign; papers untouched.


### 2026-11-05 — Powers 032: exact decision of the candidate 211,1

`POWER_STATE_032.md` current. `POWER_ARCH_EXACT_032` + `POWER_CONTACT_DECISION_032`: PROVED 3.4e−15<W/norm²<4.5e−15 for the SINGLE N211, k1, u31.5 pending from 021. Stable ARCH formula with controlled summands, EM8/cutoff 32 with absolute integral remainder and width<1e−18; all prime powers<=512 exact with Horner divided differences and factor q^-32, polar as exact fraction; complete positive tail 019 and majorant<1.1e−15. Difference vs 021: certify the error without quadrature and decide the SAME candidate, not an N campaign/cutoffs. The negative partial 300 is repaired by the omitted contacts, not by attributing quadrature error. `POWER_CONTACT_AUDIT_032` approves; main certificate PASS on independent reruns. New coverage only that atom, not a row/neighborhood/T nor global closure. Papers untouched.


### 2026-11-05 — Powers 033: relative arithmetic remainder and finite gamma mixture

`POWER_STATE_033.md` current. `POWER_PRIME_BALANCE_033`: PROVED real kernel k1 satisfies w(mq)<=m^-2w(q) for q>=5 at u>=31.5, 3<=N<=2u²/9−u/3+1.5. D contracts ρ 2389/3600; divisor identity with b(n) corrected by 2,3,4 gives for odd K 0<S_K<=A_tail<=S_K/(1−ρ^(K+1)), and A_tail>=3600L/5989. Error relative to the comb, not to the W residue; comparison with ARCH polar OPEN. `POWER_COEFFICIENT_BALANCE_033`: exact FINITE Erlang mixture with positive weights; −.01<E22<−.006 complete, profile NOT positive definite, NOT a counterexample to W. Individual damage<.22/(N−1). Abel produces positive weights for T_m=ΣjE_j; ALL T_m>=0 would be sufficient only for column k0 and is OPEN. Differences vs 027/019: specific finite mixture and proved contraction for the real arithmetic, not identities as sign. `POWER_BALANCE_AUDIT_033` approves both; verifiers PASS on independent reruns. No new W/T coverage; papers untouched.


### 2026-11-05 — Powers 034: new complete rows and oscillation of the T criterion

`POWER_STATE_034.md` current. `POWER_DIVISOR_COMPARISON_034`: PROVED W>norm²/40 for ALL N>=3, k>=1, u>=31.5, u²>=225N/4; k>=2 margin 3/20. k1 keeps positive comb 019 and ARCH−polar>0; higher k pay the COMPLETE comb with CENTERED029, without extrapolating arithmetic sign. At u31.5 covers N<=17, k>=1; combined with fixed V12 007 completes rows 1..12 for ALL k. Combined with 8 poles 014 also completes rows 1..8 for ALL k/ALL u>=31.5. No new arbitrary crosses nor T window. `POWER_WEIGHTED_COEFFICIENT_034`: PROVED the real T_m change sign infinitely often, via REAL positive cosh/parity/generator and a proved lemma on continuation of positive coefficients. FALSIFIED criterion 033 T_m>=0 for all and even eventually, NOT W negative nor global no-go. Do not retry componentwise positivity of T without new compensation. `POWER_COMPARISON_AUDIT_034` approves both, region verifier PASS on independent reruns. Fixed table pending k0 N>=13 and columns N>=18 below the cone except 211 k1; papers untouched, global OPEN.


### 2026-11-05 — Powers 035: rows 1–17 complete and law of the signed average

`POWER_STATE_035.md` current. `POWER_BOUNDARY_BALANCE_035`: PROVED W>norm²/40 for ALL N1..17, k>=0 at fixed u31.5. A single terminal 17,k0 has ARCH>−.868, polar>.911 and COMPLETE comb of modulus<.002; margin>.041. The convex normalized recurrence and the real column k1 of 034 complete the borders 13..16 by descent. Difference vs 018: terminal and column effectively certified, not an isolated recurrence. `POWER_SIGNED_TRANSFORM_035`: exact positive law P_d of the SIGNED average T_m/[m(m+1)/2], explicit tail, window m~sqrt(N), Gamma2 limit and cost of any fixed adverse prefix O(N^-2). Does not control magnitudes nor signs in the moving window; oscillation 034 remains. `POWER_BOUNDARY_AUDIT_035` approves both; verifiers PASS on independent reruns. No new arbitrary combinations nor window T. Fixed pending from N18 below the cone except 211,k1; global sign OPEN, papers untouched.


### 2026-11-05 — Powers 036: boundary remainder and localization of real energies

`POWER_STATE_036.md` current. `POWER_RECURRENCE_BOUNDARY_036`: PROVED from N>=18, k>=0, u31.5, COMPLETE energy of the cone 017 on the diagonal boundary <=O(log L/sqrtL)->0; exact remainder R_L->initial A. Inverse beta-binomial moment + upper ARCH and bounds 017; novelty vs 016: the WHOLE growing parabolic cone and real energy. Weights of the stopped boundary and surviving mass positive, without inference about the stopped energy. `POWER_MOVING_BALANCE_036`: PROVED polar and COMPLETE REAL comb energies under the law 035 concentrate at m/(N−1)->1/32, while the normative mass has scale sqrtN. Exact beta-binomial tilt and exponential bounds; common phase (3969/3968)^N. Elementary CHEB proved, without truncating arithmetic. FALSIFIED discarding tails of separate components using only mass 035; does not localize the window of the signed functional nor estimate the prime/polar difference. `POWER_FRONTIER_AUDIT_036` approves both; constants verifier PASS on independent reruns. No new W sign/coverage/T; rows 1..17 of 035 remain, global OPEN, papers untouched. Continuation must preserve joint cancellation and make explicit the difference from 018/030/031.


### 2026-11-05 — Powers 037: critical dilation and finite signed grouping

`POWER_STATE_037.md` current. `POWER_ENERGY_GROUP_037`: PROVED the real profile D_N(m)=mH_N(mx_N)/H_N(x_N) has main term 1/m and explicit error M_N(log m+log²m)/m, x_N=exp((N−1)/992). ABS-FAIL for ALL N>=2^16 by squarefree counting/discrete Abel, not a table nor an artificial model. Möbius grouping by finite Q keeps main term U_Q/m and explicit error with divisor moments; the WINDOW condition proves the sign of an AUXILIARY kernel, not W. Q growing primorial up to floor(N^(1/8)) gives error<.01 for m<=exp(3N^(1/4)), N>=2^80, but the ABSOLUTE grouped remainder>1.48 against main group<.505. Absolute domination refuted for THAT choice, not further signed grouping. Difference vs 018/030/031: uniform bounds on the same real profile, not a new identity alone; difference vs 033: critical band 1/m. `POWER_GROUP_AUDIT_037` approves everything, extended verifier PASS on independent reruns. Error not summable at infinity; signed complement and integration OPEN. No new W/T coverage, papers untouched, global OPEN.


### 2026-11-05 — Powers 038: signed product via Fourier and enlarged window

`POWER_STATE_038.md` current. `POWER_SIGNED_MOMENTS_038`: PROVED for N>=16, B_Q<=N/1000, ALL real ell, |M_Q f_N(ell)−f_N(ell−A_Q)|<=12000B_Q/N+65sqrtN(V_Q/U_Q+1)e^-N/2000. Keeps the EXACT Möbius multiplier, normalizes gamma with positive density separated from the extended signed profile. Difference vs 037: eliminates V/U from the CENTRAL error, not mere cumulant computation nor signed Jensen. Same primorial Q of 037, N>=2^80: (4/5)U/m<K_NQ(m)<(6/5)U/m on A_Q<=log m<=A_Q+sqrtN/100, length enlarged from order N^.25 to √N. It is an auxiliary kernel, not W nor window T. `POWER_SIGNED_AUDIT_038` approves theorem/corollary, constants verifier PASS on independent reruns, additional check of the normalizer on cases. Infinite signed arithmetic remainder and integral OPEN; polynomial error is not sufficient precision by itself against exponential energies. No new W/T coverage, papers untouched, global OPEN.


### 2026-11-05 — Powers 039: complete inverses positive from a cutoff close to the energy

`POWER_STATE_039.md` current. `POWER_INFINITE_SHOULDER_039`: PROVED for ALL N>=4e6, u31.5, h_N(x)>0 and K_N(x)>0 for ALL x>=exp(T_N), T_N=2(N−1)v/(u²−v²), v=.5+1000/√N; T_N=(N−1)/992+O(√N)<(N−1)/330. Comparison with 026 is of the SAME K; h is proved as well. Moving tilt, INFINITE Euler product σ>1 kept signed in Fourier, ψ<=2x elementary, uniform normalizer c/v and positive translated profile. Ratios full h/H, K/G∈(.9Uσ,1.1Uσ) on the interval v; next tail by m^-2. Difference vs 038: no finite Q nor omitted coprime remainder, controls the complete complement in the declared region. `POWER_SHOULDER_AUDIT_039` approves; three independent checks, verifier PASS. T_N is a kernel coordinate, NOT a Paper 46 window; interior/W balance OPEN, no new W/T coverage, papers untouched.


### 2026-11-05 — Powers 040: real central pattern and cutoff at constant distance

`POWER_STATE_040.md` current. `POWER_CRITICAL_BALANCE_040`: PROVED for ALL N>=2^80, δ=N^-2, v=.5+δ, t_v=2(N−1)v/(u²−v²), full h/H<−1/N and full K/G>1/N at the SAME center. Moreover full h, K positive for ALL log x>=(N−1)/992+5. Difference vs 039: elementary reciprocal Euler factor z−γz² with remainder 9|z|³ before Fourier, effective error o(1/N); no divergent central moments nor formal series. New CURV −2q′/t<q″<0 from polynomial/Riccati weights gives derivatives and a real margin. Tail δ 2000/N..1000/√N links to 039: distance O(1) instead of O(√N), explicit range of N. `POWER_CRITICAL_AUDIT_040` approves everything, extended verifier PASS on independent reruns, adversarial curvature check on cases. Kernel signs are NOT the sign of W; integrated interior/ARCH balance OPEN. No new W/T coverage, papers untouched, global OPEN.


### 2026-11-05 — Powers 041: integrated benefit in a moving band with complete arithmetic

`POWER_STATE_041.md` current. `POWER_ENERGY_BAND_041`: PROVED for ALL N>=2^80, T=2(N−1)(.5+N^-2)/(u²−(.5+N^-2)^2), L=√N/100, 2∫_(e^T)^(e^(T+L))h_N B<−C_N/25600, C_N=e^(T/2)(rho/2−rho′)(T)>0. FULL Möbius+B real jumps, favors W=ARCHsharp−F but complement OPEN. Difference vs 030/031/040: MOVING energy band and finite integration of the factor δ−D before abs, with borders and error relative to the SAME scale C controlled; not a global critical Fubini. §7 proves B=−γx−B1({x})log x+κ+E, −1/x<E<1/(2x), and periodic integrated bound with Q2 norm 1/16, borders/variation/∫|h|/x; elementary auxiliary, not the sign of W. `POWER_ENERGY_AUDIT_041` approves core+appendix, BAND verifier PASS on independent reruns. No new W/T coverage; complement balance/global OPEN, papers untouched.


### 2026-11-05 — Powers 042: absolutely small renormalized tail

`POWER_STATE_042.md` current. `POWER_RENORMALIZED_TAIL_042`: PROVED global F/2=−γ+(κ−γ/2)J1+R via MASS022 and SAWTOOTH041, with ALL borders/jumps. For N>=2^80, X=exp((N−1)/992+5), |Rtail|<=N(T+2)e^-3T/2<e^-N/1000; W=ARCHsharp+2γ−(2κ−γ)J1−2Rinside+epsilon, |epsilon|<2e^-N/1000. Difference vs 041: ABSOLUTE error after GLOBAL affine cancellation, not relative scale C_N nor a sum of incompatible benefits. REALDECAY full h/h′ via qT and divisors, Q2 border X kept. `POWER_RENORMALIZED_AUDIT_042` approves everything, verifier PASS on independent reruns. Renormalized interior and sign of W OPEN; no new W/T coverage, papers untouched.


### 2026-11-05 — Exploration 043: renormalized interior, no new inequality

Re-examination of the continuation of 042: gathering (κ−γ/2)J(1)+R gives exactly ∫h(x)[B(x)+γ floor(x)]dx. The positive cell means of that weight do not control its pairing with signed h; inverting again by divisors reconstructs H of INTERIOR_SCALE030. No new signed lower bound was obtained nor is the interior variation controlled via Q2. Label: exploration WITHOUT SIGN PROGRESS, not a global NO-GO nor a new theorem. No memo of identities was created. Avoid repeating this same normalization as a new method without an additional hypothesis or inequality. STATE042 keeps the last integrated result. Moving on to review mechanisms for the complete form, with prior consultation of the corpus.


### 2026-11-05 — Exploration 043: two pivots discarded because of concrete antecedents

No new mathematical result. The reading of BB5 as an open residue was historical: CC_001_CROSS_LAG_LOG6_AND_KAPPA_HESSIAN.md (phase 198, §§2,5,7; scope at lines 74/83) later treats the κ Hessian, separation by log 6 and four-point Bochner. The simplicity condition and the check of CC4 are kept; a prohibition of every two-prime route is NOT deduced. The cross-reference in entry BB001 was clarified to avoid repeating the attempt.

The theta pivot did not produce a new inequality either: 103_34 already proves log-concavity of the specific sum and quadratic minors; 103_39–42 delimit generic curvature/hazard arguments; 103_47 contains the exact arithmetic translations, the decreasing relative tail and a conditional cubic criterion. Those antecedents were not promoted as novelty nor was global impossibility concluded. STATE042 keeps the last integrated result. New explorations require another quantitative hypothesis and an explicit bridge to the complete form.


### 2026-11-05 — Powers 044: reflection check and representation candidate

`POWER_STATE_044.md`: `POWER_REFLECTION_TEST_044` PROVED real gap W[g_Q]−W[g_L]>3/2, u31.5, norms 1; ARCH>2, polar>−.5, COMPLETE comb gap>0. Refutes ONLY eliminating the antisymmetric sector by the reflection q↔1−q in the bridge 017; not every subfamily nor W. Reuses 004/018 explicitly, without new coverage. `POWER_REDUCTION_AUDIT_044` approves/script PASS on independent reruns. L55-B reviewed: an explicit positive pair+slack/arithmetic error can give a lower bound; neither the pair nor a new bound was constructed. No converse/general equivalence nor NO-GO of that tool is claimed. STATE042 keeps the last balance progress; global OPEN, papers untouched.


### 2026-11-05 — Powers 045: compact repair and correction of the documented frontier

`POWER_STATE_045.md`: `POWER_PRIMAL_PAIR_045` PROVED, independent check in `POWER_PRIMAL_AUDIT_045`: if a representative pair keeps exactly the real tail of the symbol and only changes a compact EVEN spectral measure, the identity on ALL primitive tests forces the correction to be zero. Proof via F=(D²-1/4)phi, polarization/localization and compact moments; parity is essential. At T=3/5, q_T(0)<-15/2, so this ansatz does not admit slack<=15/2. This is neither negativity of W nor a NO-GO for general L55-B. The non-compact subcase with an exterior temporal remainder given by a finite signed measure returns to the existing dual(D); it is not generalized to arbitrary measures/distributions. Difference with respect to 044: a concrete compact-repair hypothesis, not a mere change of orientation nor an artificial imposition of finite total mass. `POWER_CONTACT_FLOOR_045` checks that the RAW floor m(240)-A2345<-1/2 fails when 5 enters; ROUND026A already avoids that limitation, so this is neither a new route nor an impossibility for other certificates. Both rational verifiers PASS on independent reruns.

STATUS CORRECTION: Paper 46 proves up to log5/2, but the earlier sandbox `ROUND_026_A`, Theorem 26A.2, records PROVED/computer-assisted lambda_A(T)>=2e-26 for ALL 0<T<=207/200=1.035. The archived logs of both parities, certified:true at mu 2e-26, were read and re-checked; the long certification was NOT reproduced now. T1.098 only has localized builds/matrix, with no final certificate found: it is not promoted. The archived local frontier, the CITED bounds and the recent power results are distinct. Step 045 adds no W coverage nor T-window; global sign OPEN and papers untouched.


### 2026-11-05 — Powers 046: deduplicated exploration of the interior, no new sign

I returned to `POWER_RENORMALIZED_TAIL_042` and to the sufficient bridge 017. No new inequality was obtained: Turán for the complete values returns to the moments/determinants route; recombining J(1) with the residue and performing the full inversion reconstructs the weight 043 or Hjoint030. Pairings with a fixed prime or fixed Q reproduce 037/038. Choosing Q according to the scale adds entry edges and a signed remainder that still have no estimate. An auxiliary falsifier for the divisor inverse of C(n) was not promoted, because its positivity was not a necessary hypothesis of the attempt. There is no general NO-GO and no new theorem-level artifact.

Precision on the sufficient obligation, already a consequence of 016/036: for A_Nk=W[f_Nk]/norm² at fixed u, it would suffice to have A_Nk>=-epsilon_N, epsilon_N->0, UNIFORMLY in 0<=k<10000N² for large N; cone 017 covers the rest. For any epsilon, choose M with epsilon_N<=epsilon for N>=M and refine to depth L>=10000(M-1)²+M. Each child with N'<M falls into the cone by its large k', and the others have lower -epsilon. The convex normalized recurrence forces A_parent>=-epsilon; epsilon->0 gives the sign. It does not require certifying finite exceptions nor a pointwise positive margin. It is a known sufficient condition, not an arithmetic estimate already obtained. Result 042 only addresses k0: an asymptotic lower bound there does not cover the whole band. The bound D_N>=2exp(-N/1000) suffices to decide each pointwise k0, but it is not a necessary requirement of closure by a vanishing uniform lower bound.

Coverage status unchanged with respect to 045; global sign OPEN, papers untouched. The next construction needs a concrete additional signed input, not another inversion of the same weights.


### 2026-11-05 — Powers 047: primitive family checked, no new bound

The candidate H_Nk(s)=(s²-1/4)s^k/(s+u)^(N+k+2), N>=1,k>=0,u=63/2 was checked. TATE_CHAIN009, PRIME_TRANSFER014, CONFLUENT_BRIDGE014 and SCALAR_BRIDGE017 were checked against the index/grid/crossword. The Bernstein adaptation with base (s²-1/4)/(s+u)^3, plus density 014 and repair of the two moments by two fixed rationals, makes the sign of this entire table sufficient for the PRIMITIVE carrier. It is an adaptation of the existing bridge, not a new arithmetic inequality; no strict logical separation between the primitive/complete global targets is claimed.

The primitive density is exactly the sum of the original densities (N,k+2), (N+1,k+1), (N+2,k) with coefficients 1, 1/2, 1/16. The identity preserves all of W: the three polar terms cancel by rational evaluation at x=-1/4. It inherits cone 017 for k>=10000(N+2)² and the rows N<=15 from 035. The recurrence keeps POSITIVE normalized weights, but these are quotients of the primitive norms, not the original simple beta coefficients; their law is a positive mixture of three beta laws. The uniform -o(1) criterion of 046 adapts, without supplying its sign hypothesis.

In the other expansion, with a=u²-1/4=992 and a_Nk=W[f_Nk] original, unnormalized, W[H_Nk]=a_Nk-2a a_(N+1,k)+a² a_(N+2,k). This is the second difference 009 extended to variable k. The polar cancellation does not control the ARCH+comb remainder and the positive mixture does not force a vanishing lower bound. No new bound was obtained, no other theorem memo was created, and this reduction was not presented as a proof of the sign. Coverage and the documented frontier remain as in 045; global OPEN, papers untouched.


### 2026-11-05 — Powers 048: subquadratic corollary and restricted endpoint R12

`POWER_SUBQUADRATIC_COROLLARY_048` PROVED; independent check `POWER_SUBQUADRATIC_AUDIT_048` and a further re-check. At u=63/2, for ALL N>=exp(10^6) and ALL k>=2N²/log log N, W[f_Nk]>(2/5)log N·norm². Explicit extraction of STRIP/PRIME/ARCH/POL017 with c_N=2/log log N: C(c_N)<=1+4sqrt(log N), ARCH grows like log N and dominates ALL of the comb and the polar term. No implicit uniformity of N0(c), no Gaussian limit, and no arithmetic truncation is invoked. It is additional unbounded coverage made explicit from existing bounds, not a new arithmetic inequality. The lower band and the remainder 036 remain open; there is no new T-window.

`POWER_R12_ENDPOINT_048` PROVED and checked in `POWER_R12_AUDIT_048`: for G in confluent V13 with G(0)=0, E2[G]>norm²/50, where E2=ARCH+POLAR+contact2. It extends one band of the rational certificate 007 and verifies by congruence/LDL12 the endpoint v=u of the open hypothesis R12 of 014. Difference from the universal falsifier 014: here F0 belongs EXACTLY to V12; there it did not. Verifier PASS on independent reruns. A common neighborhood follows by continuity, with no effective radius nor transport for all v. The tail of the other primes is not included in E2; bound 007 is not automatically imported to V13. For Q=s/(s+u), tridiagonal compression of q on V12 gives minEq>=1/576 and log-convexity of norms: the normalized polar term of Q^jF decays <=(9/62)^j PB12. The effective archimedean cutoff and the intermediate blocks are still missing; no sweep was performed.

Both results have explicit scope. Global sign OPEN, papers untouched; documented window frontier kept as in 045.


### 2026-11-05 — Powers 049: uniform R12 resolved in the restricted basis

`POWER_STATE_049.md`: `POWER_R12_TRANSPORT_049` PROVED and checked in `POWER_R12_AUDIT_049`. For ALL F!=0 in confluent V12 and ALL v>=u=63/2, E2[sF/(s+v)]>norm²/2500. Here E2=ARCH+POLAR+contact2. By T2 of 014 it transports E2 coercivity when moving ONE pole from V12. Difference from the universal falsifier 014: the positive basis V12 is kept exactly; no universal ordering is declared. R12, previously OPEN in 014/048, is resolved in that class.

`POWER_CENTERED_CUTOFF_049`: centering the circle polynomial and separating the sectors of degrees 11/10 allows IBP + weighted polynomial energy with a self-contained proof. For ALL j>=14 and ALL numerators in V12, E[tau^-2]<1/405 and ARCH/norm²>859/800. Contact2<norm² and the decreasing polar term of 048 pay for the tail. The initial cutoff 32 of HIGHPASS_CUTOFF049 is dominated by 14. The exhaustive segment j1..13 was certified by thirteen rational 12-dimensional congruences/LDL, with relative error to the Gram matrix; the segment was fixed analytically, not by searching for favorable cases. Script PASS on independent reruns. Geometric mixture 015 preserves norm and polar term; |Q|<=1 and domination of |m||F|² justify convergence for each finite v.

The tail of contacts n>=3 has not been transported from 007, so complete W is not claimed on the new spaces. Nor is iteration over intermediate bases other than V12 authorized. Global sign OPEN; no new T-window; papers untouched. Complete regions 048 and documented frontier 045 remain.


### 2026-11-05 — Powers 050: complete W on all twelve real poles

`POWER_STATE_050.md`: `POWER_FULL_TWELVE_050` PROVED, independent check `POWER_FULL_TWELVE_AUDIT_050`, full verifier PASS on independent reruns. For any TWELVE real poles v_i>=63/2, repetitions allowed, and ALL proper real numerators P, W[P/prod(s+v_i)]>norm²/10000. It includes all cross terms, all arithmetic contacts and the polar term; it extends the eight arbitrary poles of 014 and the fixed block V12 of 007. By cancellation of factors it includes the lower-dimensional spaces.

New gain: W>norm²/250 on ALL THIRTEEN real poles >=u with numerator vanishing at 0. The SAME exhaustive segment j1..13 of 049 was strengthened to E2>norm²/50; the analytic tail J14 already beats that margin. MULTI015 on G0=QF0 carries that whole orbit to 13 poles with num0. Trace010 with alpha 1/2 gives B_T13=109543953194<330975²; keeping n^(-1/4)<=10/13 from 3 on, the COMPLETE arithmetic tail n>=3 has norm <2/125. The resulting ZERO13 feeds FULLTEL014, which preserves norm/polar exactly and transmits without loss the coercivity 1/10000 of the base block. The new sign input is arithmetic 2 together with ARCH+POLAR and the infinite tail, not ARCH alone.

The MULTI consequence of 049 also gives positive E2 on all 12 poles without iterating R12; the initial exploration FULL_TRANSFER_PLAN050 (E23) was superseded and not executed. There is no sweep of rates/indices: the segment was fixed by an analytic cutoff and 13 rational 12-dimensional LDLs. No sign for 13 general poles nor arbitrary order is claimed, nor a new T-window. Global OPEN; papers untouched.


### 2026-11-05 — Powers 051: linear archimedean cutoff for all dimensions

`POWER_DIMENSIONAL_CUTOFF_051` PROVED, corrected version checked in `POWER_DIMENSIONAL_AUDIT_051` and re-checked. For ALL n>=1, ALL F!=0 in V_n and ALL j>=ceil(7n/6), E_(Q^jF)[tau^-2]<1/405 and ARCH[Q^jF]>(859/800)norm². Difference from 015/049: an explicit cutoff LINEAR in the dimension, simultaneous over all numerators, not an eventuality with an unknown constant. With d=n-1 and r=u²E[tau^-2], (2j-1)r<=1+2sqrt[d(d+2j)r]. An explicit J(n,b) is given for r<b and any archimedean margin h>=0. Parity and edges are justified by centering and polynomial energy. The factor of the second sector was corrected to (d-1)(d+2j+1), still dominated by d(d+2j) with difference 2j+1; the final results do not change and the check acknowledges the correction.

This is not a new sign of W. The literal extrapolation of 050 with positive E2 on ALL orbits and ALL orders is already refuted by PRIME_TRANSFER014: F_Tate of order 2^17 satisfies E2[QF]<0. This requires changing the arithmetic control of the initial segments; it does not rule out complete W. Positive ZERO13 of 050 only leaves a Schur pivot for 13 general poles; no new cross-term inequality was found. The Toeplitz/persymmetric reduction and the Schur step are antecedents, not promoted as a new result. W coverage remains at 050; global OPEN, papers untouched.


### 2026-11-05 — Powers 052: complete confluent block 13 and quantified real pivot

`POWER_STATE_052.md`: `POWER_CONFLUENT_THIRTEEN_052` PROVED and approved in `POWER_CONFLUENT_THIRTEEN_AUDIT_052`. For ALL f∈V13 confluent at u=63/2, W[f]>norm²/4000. All arithmetic is kept: E2>.0003norm² is already positive but the tail majorant from 3 on is excessive; E23>.00028norm² and the WHOLE tail n>=4 has norm <.00001. Rational LDL, constants with remainders and band bounds; script PASS on independent reruns. The ONLY next block motivated by ZERO13 of 050, with no sweep of dimensions/rates.

Difference from the deduplicated abstract Schur of 051: the REAL coupling and the error of ALL cross terms were controlled. Pivot with respect to h=ell/sqrt13, ell_j=(-1)^j: sigma(E2)∈(.0004054,.0004055), sigma(E23)∈(.0003834,.0003836), sigma(W)∈(.0003,.0005). They are enclosed by the order of forms Tc±epsilonI and a minimum over the same affine space, not by independent errors of an inverse. At the RATIONAL minimizer of the center E2, energies divided by 13: AP∈(.01839,.01841), contact2∈(-.018,-.01798), contact3<0. These are energies of a fixed complement direction, NOT unit Rayleigh quotients nor claims of exact optimality of the central vector. Keeping 3 improves the certificate by avoiding a loss from the absolute bound; 3 does NOT improve the real pivot.

The parallel investigation of a uniform weighted norm Q^jV_n obtained no new bound: monomial WRN017 does not control the mixed Gram matrix and trace010 is not automatically imported to the orbit. No general no-go is promoted. Coverage 050 of 12 arbitrary poles is kept; thirteen arbitrary poles and general order remain OPEN. No new T-window; papers untouched.


### 2026-11-05 — Powers 053: complete form on thirteen arbitrary poles

`POWER_STATE_053.md`, `POWER_FULL_THIRTEEN_053.md`: PROVED, rational verifier reproduced on independent reruns, exit0. For ALL proper real numerators and thirteen real poles >=63/2 (repetitions allowed), W>norm²/4000. Auxiliary ZERO14: fourteen poles with numerator vanishing at s=0 have W>norm²/1000.

Difference with respect to 050/052: contacts 2,3 are retained exactly; the centered matrix moment and monotonicity cover ALL j>=96, and the 95 initial blocks are certified exhaustively with error epsilonGram. MULTI14 transports E23; trace14 bounds the WHOLE tail from 4 on by <1/1000; FULLTEL13 keeps the margin of 052. The interval optimization of the logarithm did not change precision or thresholds. No new T, no arbitrary dimension, no global closure. Do not retry as if eventual positivity resolved the initial segment for every dimension.


### 2026-11-05 — Powers 054: effective control of coefficients in inverse frequency

`POWER_INVERSE_COEFFICIENT_054.md`: COEFF/EVAL PROVED, independently re-checked twice. With a=u sqrt(j), R(y)=y^(n−1)P(ia/y), D=integral |R(y)|²(1+y²/j)^−(n+j)dy, one has norm²=a^(1−2n)D/(2pi). For ALL n>=1, j>=n and ALL numerators, (sum|coef R|)²<=9n²9^n D; hence the same factor controls complex evaluation and the product R(z)R(-z), with max(1,|z|^(2n−2)). Elementary proof: weight >=exp(-2) on [-1,1], Legendre expansion, coefficient recurrence and Cauchy.

Difference from 015/016: an effective constant depending only on n for ALL j>=n, avoiding the unquantified smallest eigenvalue of a limiting Gram matrix; it does not assume a temporal weighted norm uniform in n. The coordinates by themselves are not the result. The full contour, effective cutoff for W and initial segment remain pending; no new sign coverage nor T. The negative-energy reformulations of 036 and the moment extrapolation reproducing 016 are not promoted as new.


**Update 054 — full cutoff approved.** `POWER_EFFECTIVE_HIGHPASS_054.md` and `POWER_EFFECTIVE_HIGHPASS_AUDIT_054.md`, PROVED/independently re-checked: with C_n=9n²9^n, D_n=10C_n n!, A_n=6C_n n n! and K(n)=max(10000n²,A_n·3^(4D_n+20)), W[Q^j P/(s+u)^n]>norm² for ALL n>=1, ALL real numerators of degree <n and ALL j>=K(n), u=63/2. Full contour <=D_n, explicit beta moments including branches r=0 and r=n, scalar endpoint N=1 justified separately; autocorrelation <=D_n exp(-15|t|)norm², infinite comb <D_n, ARCH>2D_n+9 and polar <1. No campaign and no evaluation of gigantic integers. It resolves the contour/cutoff that the earlier 054 entry left pending. Difference from 015: an effective formula in variable dimension, with no unquantified limiting Gram matrix. Initial segments j<K(n), global sign and a new T-window remain unresolved; do not eliminate the remainder using recurrence 036.


### 2026-11-05 — Powers 059: scale necessary for a uniform contour

`POWER_STRIP_NECESSITY_059.md`, PROVED by analytic proof, independently re-checked: for fixed u>0 and 0<eta<u, there is no D independent of n,j bounding integral|rho_(n,j)(x+i eta)| by D integral rho over a sequence n<=j=o(n²), already with P=1. Var|tau|<=u²[j/(2(n−3/2)(n−1))+1/(2(n−3/2))]→0; choosing t_n in [T,T+2pi/u] with mean phase a multiple of 2pi makes the correlation →1, incompatible with D exp(-eta t_n) for large T. It excludes uniform STRIP strategies on cones j>=C n^p, p<2.

Difference from 016: every subquadratic scale, including a divergent central frequency, with exact variance control. Not negative W, not a prohibition of subquadratic sign, not a necessary bound p>=3. Scalar quadratic 017 and 054 with D_n remain valid. Under investigation: product of amplitudes without causal phase for p>=2; a global Gaussian comparison is not justified. Global OPEN; no new T nor campaign; papers untouched.


### 2026-11-05 — Powers 060: uniform contour and sign on the cone n³ log³n

`POWER_STATE_060.md`, `POWER_UNIFORM_STRIP_060.md` and `POWER_UNIFORM_STRIP_AUDIT_060.md`: PROVED/APPROVED on independent re-checks. For ALL n>=1, ALL real numerators P of degree <n and ALL j>=10^12(n ceil(log_2(n+1)))^3, u=63/2, W[Q^jP/(s+u)^n]>norm². STRIP at height 3 has constant <2 INDEPENDENT of n/P; autocorrelation <=2exp(-3|t|)norm², complete comb <2, ARCH>4, polar <1 in the same normalization.

Difference from 015/054: orthogonal polynomials of the exact Student weight give FIRST200 for the amplitude without phase; the degrees grow like (n+3r,j−r). Cauchy in L² at height 15 pays only the Taylor tail from 20nq_n on with D_n of 054, while the first derivatives cost <.01 per step. No fixed-dimension generator is exponentiated, and neither a global Gaussian nor the uniform weighted causal norm refuted in 016 is used. SINGLE-EVAL controls complex amplitudes; rho=H H# preserves the correct product off the line. Cutoff O(n³log³n), the weaker 10^12n^6 also valid; no numerical campaign.

Initial indices j<J(n) and global sign OPEN. No descent from the cone is inferred, nor a new T-window. 059 does not refute this range: it only requires at least quadratic scale for uniform STRIP. Papers untouched.


### 2026-11-05 — Powers 061: complete decision of the interior case 129,0

`POWER_GAMMA_129_DECISION_061.md`, `POWER_GAMMA_129_AUDIT_061.md`, `POWER_STATE_061.md`: PROVED/APPROVED, rational verifier reproduced on independent reruns, exit0/PASS. For G(s)=(s+63/2)^−129, W/norm²∈[13456684165,13456684168]/10^20, in particular between 1.34e−10 and 1.35e−10. Historical pending case 025/026/027, not a search for another N. Stable ARCH 032, rational polar term, ALL contacts up to 512 and complete ADVERSE tail <1e−24 by ROOT026 q(log512)>16; no quadrature nor float as proof.

ARCHsharp/norm²≈−1.04219397018062543, ERR≈−1.04219397031519227, both enclosed rationally. The benefit −ERR exceeds the deficit by only 1.3456684e−10; the guarantee −.66 of 025 was not sufficient. With CELL024, the remainder of cells n>=3 contributes between .3755 and .3822 to −ERR, with no double counting. W is decided for the same test where K129(1)<0; pointwise K>=0 is not rehabilitated. No row, next N, T-window or global sign is inferred. Papers untouched.


### 2026-11-05 — Powers 062: affine deficit and complete residue in the same 129

`POWER_GAMMA_AFFINE_BALANCE_062.md`, `POWER_GAMMA_AFFINE_AUDIT_062.md`: diagnosis PROVED/APPROVED, verifier reproduced on independent reruns, exit0 PASS. Reuses the complete J129(1) of 024 and ERR/ARCHsharp of 061 with no other N/precision/cutoff. AFF=ARCHsharp+2γ−(log(2π)−1−γ)J1∈[−60446492280,−60446492279]/10^12; complete R∈[−30223246208,−30223246207]/10^12; W/norm²=AFF−2R. The affine part is negative and the repair R is essential in THIS balance.

R includes periodic B1 + Euler error, not B1 alone; it does not use ABS-TAIL042 (N>=2^80). The enclosure of R uses the known ERR of 061; it is NOT an independent bound for descent; W keeps cert 061 with no shared independent roundings. No new W/T nor general NO-GO. Comparison of N-differences of J/K/ARCH still has no bound; global OPEN, papers untouched.


### 2026-11-05 — Powers 064: cubic scale necessary for STRIP over all numerators

**PROVED/APPROVED.** `POWER_STATE_064.md`, `POWER_STRIP_CUBIC_NECESSITY_064.md` and `POWER_STRIP_CUBIC_AUDIT_064.md`: analytic proof independently re-checked, including the improvement to the linear threshold j≥10^6n. For u=63/2 and 0<η<u, ALL n≥4, j≥10^6n admit a REAL numerator P of degree <n with ∫|ρ(x+iη)|/∫ρ≥1+η²n³/(1152u²j). Consequently STRIP with D independent of n,j,P is refuted over ALL tests j≥C n^p for any p<3. Choosing j=max(ceil(Cn^p),ceil(10^6n)) keeps j=o(n³) and makes the lower bound diverge.

Difference from 059: variable numerator, taken from the Student orthonormal polynomial of degree n−1; not P=1 nor extrapolation of a linear packet. Exact β recurrence with k/8≤β_k≤4k, projection of the generator of 060 to degree n+2 and a controlled rational remainder give ||H′||²/||H||²≥n³/(2304u²j). Parity constructs a real even P and ρ=H²; even convexity of the shifted norm produces the lower bound. It needs no Gaussian transfer nor numerical campaign.

Scope is only the ABSOLUTE contour strategy: not negative W nor an obstacle to other sign mechanisms. 060 remains valid at n³log³n; power 3 is necessary for STRIP, logarithmic factors undecided. Interior/global sign and a new T-window remain open; papers untouched.


### 2026-11-05 — Powers 065: exactly k simple roots and sign of the complete tail

**PROVED/APPROVED.** `POWER_STATE_065.md`, `POWER_CONTACT_OSCILLATION_065.md` and `POWER_CONTACT_OSCILLATION_AUDIT_065.md`: analytic proof independently re-checked. For ALL u>0, N>=1, k>=1, the autocorrelation of s^k/(s+u)^(N+k) has exactly k simple positive zeros, alternating signs starting from positive, and last root at x=ut strictly less than 4k(N+k−1). For u>1/2, the WHOLE tail of contacts u logq>=4k(N+k−1) has contribution of sign (−1)^(k+1): favorable for odd k, adverse for even k; absolute convergence and strict sign of its sum.

Difference from 019: exact count for ALL k, not another k=1 evaluation. Vanishing moments up to 2k−1 plus degree settle N=1; one-sided exponential filters and Rolle with an edge at infinity preserve simple zeros and propagate in N. The finer bound of 019 for k=1 is not replaced. No generic total positivity is assumed and no prime is dropped. The magnitude is not controlled against the prefix/ARCH/polar: no new W row, T-window or global sign. Papers untouched.


### 2026-11-05 — Powers 067: the positive Selberg drop fails in the already certified case 129

**PROVED/APPROVED.** `POWER_SELBERG_DROP_OBSTRUCTION_067.md`, `POWER_SELBERG_DROP_AUDIT_067.md` and `POWER_STATE_067.md`: independent re-check, with no new computations nor another N. For the SAME gamma129, u=63/2 of 061, Selberg gives S=U−V and W/norm²=ARCH/norm²+polar/norm²−2U+2V. The pair 2·2 and the real mixture 030/Jensen prove 2V>1/243. Since 061 certified 0<W/norm²<1.35·10^(−10), the criterion that drops 2V has value <−1/250. Even retaining only 1−theta of 2V requires theta<6561/(2·10^11); theta=10^(−7) already leaves that candidate negative.

Explicit difference from 055/023: the Selberg identity and V>=0 are not offered again as progress. 055 left open the falsity of the strong criterion W/norm²>=2V; the later complete certificate 061 now refutes it on an already existing test. It is an obstruction to that isolated positive loss, not to complete Selberg, compensated methods or the sign of W. No new row, T-window or global conclusion. Retrospective note added to STATE055; papers untouched.


### 2026-11-05 — Powers 073: global convexity of the theta hazard and positivity of ALL pairs

**PROVED/APPROVED.** `POWER_STATE_073.md`, `POWER_THETA_HAZARD_COMPACT_073.md`, `POWER_THETA_TWO_COPY_073.md` and `POWER_THETA_AUDIT_073.md`. The compact piece left open by phase103/103_43 is closed: a rational certificate on 4096 preset cells verifies that the fourth derivative of logPhi is negative on [0,1/4], with ALL theta summands via an explicit tail. Parity and the outer 10343 give V'''(t)>0 for ALL t>0, V=−logPhi. Independent reruns gave exit0/PASS; no campaign nor historical edit.

New positive consequence: two independent copies of the tilt exp(ux)Phi(x) prove M''(u)<0 and M(u)−uM'(u)>0 for ALL u>0, M(u)=L(u+1/2). The conditional variance of the half-difference decreases with the modulus of the half-average; a covariance of opposite monotonicities gives the strict sign. Thus 1<L(a)/L(b)<(a−1/2)/(b−1/2) for a>b>1. The exact criterion CONE001 proves positivity of the COMPLETE form on EVERY plane of two powers with a,b>1, including all contacts. For a≠b the matrix is positive definite; for a=b it is semidefinite by redundancy and the nonzero represented function has positive energy.

Explicit difference: the compact residue 10343 is resolved and an application of two copies is proved that did not depend on the five polynomial-tilt comparisons pending there. It surpasses the old threshold a,b>=32 of CONE001§5 in the case of PAIRS; that remains a valid antecedent, not the current frontier. No positivity for three generators, all orders, their linear envelope nor a new T-window is inferred. Global sign OPEN; papers untouched.


### 2026-11-05 — Powers 074: the strong hypothesis of 073 does not suffice for three generators

**PROVED/APPROVED.** `POWER_STATE_074.md`, `POWER_TWO_COPY_SCOPE_074.md` and `POWER_TWO_COPY_SCOPE_AUDIT_074.md`; rational verifier exit0/PASS reproduced on independent reruns. An even POLYNOMIAL potential V=A[x²/2+x^(2p)/(2p·2^(2p−2))], p=10^6, A=4·10^8, keeps ALL hypotheses of 073, even strong convexity. All positive pairs are positive definite and M''<0, but at nodes A,2A,3A the vector (40,−40,3) gives c^T Kc<−53111/(10000A). Modes controlled analytically and mode-mean error <=1/sqrtA by integration by parts; no quadrature nor sweep. The jet at 0 of V=x^6 was checked positive via gamma moments, without offering it as a falsifier.

Difference from 003: the counterexample belongs exactly to the strong probabilistic class of 073, not just to concave functions or generic even measures. It refutes ONLY its automatic promotion to order 3; NOT the real Phi nor W. ALL real pairs of 073 remain proved, with no new W/T coverage. STATE074 records as an OPEN obligation, not as an obtained bound: with r=uM'/M, t=−u²M''/M, jet 3 requires t<=(1−r)(1+2r); the magnitude of the covariance and a global comparison are missing. Global sign OPEN; papers untouched.


### 2026-11-05 — Powers 075: positive density of the regularized Schur denominator

**PROVED/APPROVED.** `POWER_THETA_SCHUR_DENSITY_075.md`, `POWER_THETA_SCHUR_DENSITY_AUDIT_075.md` and `POWER_STATE_075.md`. For the REAL Phi of 073, Z(z)=∫Phi(x)e^(zx)dx, u>0, c=M(u), a=M'(0), the denominator D_u=zcZ−uZ' admits the explicit positive representation H_u(z)=D_u(z)/[z(z²−u²)]=∫Phi_u(x)e^(zx)dx. Here h_u=−cPhi'−uxPhi, k_u(x)=∫_x∞h_u(y)dy and Phi_u(x)=u^−1∫_|x|∞sinh(u(y−|x|))k_u(y)dy>0. h_u and k_u each have ONE negative/positive crossing on the half-line; the exact cancellation ∫cosh(uy)k_u(y)dy=0 and an increasing quotient prove the sign before taking absolute values. The equation Phi_u''−u²Phi_u=k_u, with no delta at 0, gives the entire transform and its removable values.

Difference from 003/074: a positive measure is constructed for the regularized denominator that was pending, not just positive real values of the Schur quotient. H_u>0 and (logH_u)''>0 on the line. F1=−cz/u+c²Z/(uzH_u) is kept exactly, with residue R=uc²/(ua−c)>0 at 0. F1 is not identified with a logarithmic derivative, and G=F1−R/z positive is not obtained: comparing Phi with Phi_u is missing. No positivity for three generators, all orders or a new T-window. No computations nor campaigns; papers untouched and global sign OPEN.


### 2026-11-05 — Powers 077: uniform real sign of the regularized Schur remainder

**PROVED/APPROVED.** `POWER_STATE_077.md`, `POWER_THETA_REMAINDER_077.md`, `POWER_THETA_RATIO_COMPACT_077.md`, `POWER_THETA_RATIO_OUTER_077.md` and `POWER_THETA_REMAINDER_AUDIT_077.md`. For the SAME real Phi of 073/075, ALL u>0, c=M(u), a=M'(0), beta=u²a/(ua−c), the difference F_u=J−betaPhi_u has exactly ONE SIMPLE positive zero, with sign negative/positive and zero mass. One obtains T_u(z)>0 and G_u(z)>0 for ALL u,z>0, with T=Z−[Z0/H0+z²/c]H and G=c²T/(uzH). This is a pointwise REAL sign of the remainder, not positivity of its kernel.

Difference from 075/076: SPECIFIC local inequalities C>0 and N=(xq−p)C'−xrC>0 are verified, where p=V', q=V'', r=V''' and C=p³+xp²q−pq−xpr+xq². Thus L=(xq−p)/C decreases to 0; with the edge wPhi->0, a tail average proves R increasing to infinity. The forcing term has pattern +−+ and two vanishing moments; convex interpolation gives F(0)<0, the anticausal representation gives a positive tail, and Rolle with multiplicities forces the unique crossing. It is not assumed that a positive transform is a logarithmic derivative.

Evidence: exterior x>=1 analytic, rational numerators with ALL coefficients positive in a quadrant and complete theta tail up to order 4; the Fraction verifier was read and reproduced, three PASS. Compact part: origin 1024 / remainder 8192 FIXED cells, complete jets up to 8 and Taylor-2 models with remainders, code checked line by line; run 1589 ended exit0/PASS. SHA256 `896902cf8ac1f504eb1357b6edc3048a9316094afd9b8ac5597aaff4a81a70ee`. Independent reproduction 36038 **ended exit0/FULL PASS**, origin and the remaining 8192 cells; hash matching the first run. The earlier FAILs of direct interval evaluation were due to insufficient dependency tracking; meshes/domains were kept and the new Taylor enclosure was justified, without changing the hypothesis.

The auxiliary 074 does not refute these new specific conditions. G>0 does not prove [G(z_i)+G(z_j)]/(z_i+z_j) PSD, nor three generators, all orders, a new temporal window or the global sign of W. The cross terms of the remainder kernel remain OPEN. Papers untouched.


Checked auxiliary corollary 077: N=M/u, B=(a/N−1)/u² satisfies B>0, B′<0, 2B+uB′>0; the removable value G_u(u)=−aB′/[B(2B+uB′)]>0 gives the sign of B′. For F=uB, |uF′/F|<1 proves all its pairs. The Schur complement of node 0 satisfies K_M(u,v)−N(u)N(v)/a=[uN(u)vN(v)/a]K_F(u,v), so the anchored matrix {0,u,v} is PD for distinct u,v>0. Node 0 corresponds to the original exponent 1/2, OUTSIDE the admissible W data a>1; this is not positivity of three admissible generators nor of the kernel G.


### 2026-11-05 — Powers 078: analytic tails of two auxiliary curvatures

**PROVED/APPROVED in their declared ranges.** Appendix 078 of `POWER_STATE_077.md`, checked in `POWER_THETA_CURVATURE_AUDIT_078.md`. For x=u², b(x)=B(sqrt x), g(x)=xb(x)=a0u/M(u)−1 and h(x)=1/b(x), g″<0 is proved for ALL u>=63/2 and h″<0 for ALL u>=128. Complete real series and elementary polygamma/Dirichlet bounds, with no new matrices, W points or meshes. For g the margin Delta>423/10000 is obtained; for h, the real anchor L8>3/10 gives a0>1/25 and then a0u/M>3 on the whole tail from 128. Derivative identities and rational constants verified independently.

An additional SUFFICIENT condition for all pairs of the kernel G_p is GLOBAL double concavity of g,h: the exact formulas for C_P′ and (xC_P)′ are tangent errors of h and g. Its global discharge remains CONDITIONAL: the initial compact pieces of g/h remain and preservation under iteration is not presumed. g″<=0 is the jet already recorded in 074, not a condition without antecedent. The positive coordinate K of the appendix gives b=Z_K/Z_J, but 073 for each law separately does not order that quotient.

New difference: analytic discharge of the TAILS of these specific obligations, not a new W region. The thirteen poles with rates >=31.5 are already covered by 053; a case of three large exponents is not presented as coverage progress. No new T nor global sign; compact continuation active, papers untouched.


### Step 079 — Exact comparison of secants for three generators (PROVED conditional)

Sources phase211: `POWER_THREE_SECANTS_079.md` and `POWER_THREE_SECANTS_AUDIT_079.md`. Under BASE073, the three-node blocks of the complete kernel are PSD **if and only if** g(x)=a sqrt(x)/M(sqrt(x))−1 is concave on its interval of squares. DET/CONC/GAP compare exactly two bounds on the difference of secants; delta<0 gives a negative determinant. It needs neither 077 nor concavity of h=1/b, nor concavity down to 0. The new obligation for ai>1 is reduced to ONE real curvature on 1/2<u<63/2; the tail g''<0 of 078 is already proved. The region of triples ui>=63/2 was already covered by 053: no new W or T coverage, no all-orders result. 003/074 remain in force outside the new hypothesis. Independent re-check passed; compact piece active.


### Step 081 — BASE073 is not inherited literally by the REAL remainder (PROVED, bounded class)

Sources phase211: `POWER_SCHUR_BASE_OBSTRUCTION_081.md`, `POWER_SCHUR_BASE_AUDIT_081.md`. For the exact remainder G_p of the REAL Phi, G_p'(1024)<0 for every pivot p>=p0=[25(2g*+24a²·1024²/M(1024)²+2)]². Proved via complete real bounds a>1/25, M(1024)<3 and M'(1024)>1/[3(1024+1/2)]. By global positivity 077, it also cannot keep global concavity for those pivots. It is a failure of the recursive class that requires BASE073 at each remainder, distinct from the generic falsifier 074. It does NOT refute G_p>0, its kernel, W, or a recursion with broader hypotheses; no new coverage nor global obstruction. Checked against the map; check passed; continuation 082 separate.


### Step 082 — Exact reciprocal three-node criterion (PROVED algebraic)

Sources phase211: `POWER_RECIPROCAL_SECANTS_082.md`, `POWER_RECIPROCAL_SECANTS_AUDIT_082.md`. For F>0 with all pairs of the kernel K_F strictly PD, all its triples are PSD if and only if R(x)=sqrt(x)/F(sqrt x) and S(x)=sqrt(x)F(sqrt x) are concave. DET3=Vandermonde²·R[x1,x2,x3]S[x1,x2,x3]/(R1R2R3); RECIPROCAL and strict pairs exclude both negative defects. It allows decreasing F and does not require BASE073, unlike the inheritance refuted in 081. It recovers 079 for real M. Application to G_p, pairs and both curvatures/preservation remain OPEN; no new W/T nor higher order. Independent re-check passed.


### Step 080 — Complete W for THREE arbitrary powers ai>1 (PROVED)

Sources phase211: `POWER_STATE_080.md`, `POWER_THETA_G_COMPACT_080.md`, `POWER_THETA_G_COMPACT_AUDIT_080.md`, `tools/power_theta_g_compact_080_verify.py`. BASE073 + criterion 079 + tail 078 + certificate 080 give g''<0 for all u>=1/2, and hence complete kernel PD for three distinct nodes ui=ai−1/2>1/2. Repeated nodes are grouped; positivity of the nonzero represented function. ARCH/polar/ALL contacts preserved by congruence CONE001. Continuous certificate on 4096 fixed dyadic cells, arb 256 bits/cap 20, Taylor degree 16 with rational Cauchy remainder <1e−12; run 43260 exit0/FULL PASS, hash 640d8eb8ecf2bce7e782e08333a722171744af8fc0c9831582fcfcb796fb09bc. Mathematical/code check against the map passed; independent reproduction 92790 exit0/FULL PASS 4096 with matching hash. Novelty: small/mixed triples outside region 053 of rates >=31.5. NOT four/all orders nor a new T-window; global sign OPEN. History of failed remainder enclosures preserved in the audit file, with no change of mesh/precision/margin.


### Step 083 — Reciprocal Pfaffian factorization ALL orders (IDENTITY PROVED)

Sources phase211: `POWER_RECIPROCAL_PFAFFIANS_083.md`, `POWER_RECIPROCAL_PFAFFIANS_AUDIT_083.md`. For Kij=(Fi+Fj)/(ui+uj), Ri=ui/Fi, Si=uiFi and (A_R)ij=(Rj−Ri)/(ui+uj), it is proved that detK=P_n(A_R)P_n(A_S)/productRi. P_n is the Pf without border for even n and the Pf with a FINAL border of ones for odd n. Proof by displacement, rank-2 update, odd cofactors and congruences; includes singular/coincident nodes. Classical algebra attributed (Okada/Knuth/Ishikawa–Okada–Tagawa–Zeng; anti-Löwner as antecedent), with no claim of world priority. New with respect to the corpus: exact all-orders specialization, not a sign. Pfaffian products for the real Phi remain OPEN; PSD requires all principal subsets. NO new W/T nor order 4; global OPEN. Independent re-check passed.


### Step 084 — Local Turán sufficient for Pfaffian 4, falsifier and real tail (PROVED bounded)

Sources phase211: `POWER_FOUR_TURAN_084.md`, `POWER_FOUR_TURAN_AUDIT_084.md`. PF(A_f)=−det[1,x,f,xf]/product(ui+uj); f'>0, f''<0 and T_f=2f'f'''−3f''²>0 on an ENTIRE interval imply Pf>0 for ALL four of its nodes by Rolle and the Wronskian. For R=u/M, S=uM the obligations NR, NS are explicit; NR>1/4, NS>19/4 are proved on A=u+.5>=128 with complete arithmetic. Compact .5<u<127.5 OPEN; no global four. Reciprocal falsifier R=1+x−x²/16, S=x/R keeps the scalar properties 073/077/080 but detK4<0 for all distinct quadruples in (.5,1): only a NO-GO for local scalar inheritance, not negative Phi/W. The tail was already covered by 053; NO new W/T. Independent re-check passed. Classical appendix 083 Rolle/Hankel also checked: abstract sufficient criterion, signs of the real quotients OPEN.


### Step 085 — Complete W for FOUR arbitrary powers ai>1 (PROVED)

Sources phase211: `POWER_STATE_085.md`, `POWER_FOUR_GENERATORS_085.md`, `POWER_FOUR_GENERATORS_AUDIT_085.md`, `tools/power_four_turan_compact_085_verify.py`. Certifies NR,NS>0 on ALL u∈[.5,127.5] with 16384 fixed dyadic cells/512 bits/cap 45/Taylor 40 and rational Cauchy remainder <1e−16. Run 61911 exit0/FULL PASS for both functions, hash 4916689a48baf3164b8e99ff8ff7973dbd505367cf9ee46b17b7efc9845abf46; mathematical/code check against the map passed; independent reproduction 29132 exit0/FULL PASS 16384 with matching hash. Exterior 084 + Rolle 084 + factorization 083 + minors 080 ⇒ complete kernel PD for ALL four distinct exponents ai>1, repeated ones PSD/nonzero function positive. ARCH/polar/ALL contacts preserved. New coverage of small/mixed exponents, not new large rates already in 053. NOT five/all orders nor T-window; global target OPEN.


### Step 086 — Global REAL curvature via three densities and TP (PROVED structural)

Sources phase211: `POWER_THETA_DENSITY_CONCAVITY_086.md`, `POWER_THETA_DENSITY_CONCAVITY_AUDIT_086.md`. For R(lambda)=sqrt(lambda)/M(sqrt(lambda)), R''<0 is proved on ALL lambda>0 WITHOUT using 080: densities tPhi, (tPhi)'', −Phi' normalized by tPhi give [1,A,B], B'=D/t²>0 and (A'/B')'=tN077/(pD²)>0. Its determinant is negative; sinh(ut) TP3 and its confluent version, proved by series/Cauchy–Binet, plus absolutely convergent Andreief transfer that sign to W(Z'/u,uZ',Z)=f1³R''<0. Edges/parity/factors 2 are kept; positivity of each density is not assumed. It discharges a real curvature via the specific structure of 077, distinct from a mere identity; it depends on 073/077 already proved and does not eliminate the fixed certificate of 077. It recovers triples 079/080 and strengthens the curvature to all λ>0; NO new W versus 080/085, no admissibility ai<=1, no higher hierarchy/all orders/T/global. Checked against the map; check passed.


### Step 087 — Next REAL Wronskian at the origin (PROVED pointwise)

Sources phase211: `POWER_THETA_DENSITY_ORIGIN_087.md`, `POWER_THETA_DENSITY_ORIGIN_AUDIT_087.md`, `tools/power_theta_density_origin_087_verify.py`. For the R4 densities tPhi, (tPhi)'', −Phi', −Phi''' one decides W_lambda(1,A,B,C)(0)<0 via ONE fixed rational enclosure at 70 digits, Q0..10, modes 1..8 and complete tail m>=9, prefactor pi exp 5t/2 / binomial convolution included. Independent reruns exit0 NEGATIVE with the same endpoints/hash f8f28e5f33659ec7245e23906ab11addc5a04243f1d502a8a070dbf12d13d7b7. By continuity the desired sign holds on an existing neighborhood WITHOUT a radius; not global Chebyshev. Exact Darboux Wt=−k³J²(E/J)' and coefficient V10=W_R3/840 locate an additional obligation, NOT automatic preservation. S4 branch/global raising OPEN; no extra W with respect to 085, not 5/all orders/T. Check passed.


### Step 088 — Exterior REAL Wronskian R4, whole theta tail (PROVED)

Sources phase211: `POWER_THETA_DENSITY_OUTER_088.md`, `POWER_THETA_DENSITY_OUTER_AUDIT_088.md`, `tools/power_theta_density_outer_088_verify.py`. Proves for ALL t>=1: Wt(1,A,B,C)<−4000y⁶/t², y=pi exp 2t. Exact first mode with 27 positive coefficients after shifting t1, y21 and margin 4096; COMPLETE theta tail up to V6 via log cancellation, Euler/Bell 6, E 62523502209/6553600000000000000000, box 128y and a polynomial with 55 monomials with K 30936927338496; error <96t²y⁶. Independent reruns: Fraction 4 PASS exit0, hash d2b1e479295cbf9eda602a2786b657cab5c83db1c74dee9a7d00b751723fc8f4. Gives the sign of density determinants for four nodes ALL >=1, not the complete integral. Compact 0<t<1 OPEN (087 only a non-quantified neighborhood of the origin); no extra W with respect to 085, not 5/all orders/T. Check passed.


### Step 090 — Reciprocal secant and one curvature of the remainder (PROVED real after 089)

Sources phase211: `POWER_RECIPROCAL_SECANT_CONCAVITY_090.md`, `POWER_RECIPROCAL_SECANT_CONCAVITY_AUDIT_090.md`. Lemma T_f>0 ⇒ the reciprocal secant is strictly concave, also for an INTERIOR anchor P with both orientations. The global input T_R discharged in 089 (FULL PASS on independent reruns): h=1/b strictly concave; with 086/078 all pairs G_p strictly PD. REST-SECANTS and T_g=a²T_R additionally discharge that S_G(x)=sqrt(x)G_p(sqrt(x)) is strictly concave for ALL p, x>0. The other curvature R_G requires T_h>0 globally, OPEN, equivalent under anchored confluence to the next jet: W(x,x²,G,xG)=−a²G⁴T_h. ANCHORED-FIVE has an auxiliary node 0 that is NOT admissible for W. No BASE inheritance / Turán G_p / all orders / new W / T. Checked against the map; check passed.


**Update 090 §9, NO-GO for generic inheritance (PROVED):** w=(5−e^−x)/4 and f0=1, f'=1/w² define f positive, increasing, concave, with T_f=e^−x/w⁵>0 globally. However H=x/(f−f0)=1+x/4−x²/12+5x³/192+O(x⁴) has T_H(0)=−1/192 and T_H<0 on a positive neighbourhood. Antiderivative and exact jets independently re-checked and checked against the map; no campaign. Refutes only the automatic inheritance T_f⇒T_H, NOT T_h of Phi nor W; real S_G remains PROVED and real T_h OPEN. Consolidated in 090, without a duplicate record 091.

### Step 089 — REAL global R4 transport and T_R>0 on the whole axis (PROVED structural)

Sources phase211: `POWER_STATE_089.md`, `POWER_THETA_DENSITY_COMPACT_089.md`, `POWER_THETA_DENSITY_COMPACT_AUDIT_089.md`, `POWER_THETA_DENSITY_TRANSPORT_089.md`. Run 40406 FULL PASS 1024 origin λ + 8192 rest total, hash 995ef292abf5a80a3d195b4e68a815e1b56f9b343531bc1c0786af682413d1aa; mathematical/literal check passed, independent reproduction 87911 exit 0 / FULL PASS 1024+8192 and same hash. Complex theta bounds + 16 modes / coefficient tails before differentiating + Cauchy determinant, fixed parameters, no tuning. Splicing with 088 ⇒ R4 Wronskian negative for ALL t>0. ECT order [1,B,A,C] uses the previous Wronskians of 086 without presupposing A'>0; Rolle ⇒ determinant of densities negative for ALL nodes. Sinh TP4 / confluent Andréief ⇒ W(Z'/u,uZ',Z,u²Z)=−F0⁴T_R<0 ⇒ T_R>0 for ALL x>0. 090 applies globally ⇒ h=1/b strictly concave and the remainder pairs G_p PD via 078/086. No global S4 / no Turán inheritance for G_p / all orders; no extra W relative to 085 nor T, global OPEN.


### Step 091 — Pi/s not monotone for REAL cofactors (criterion NO-GO, PROVED)

Sources phase211: `POWER_PEANO_MONOTONICITY_OBSTRUCTION_091.md`, `POWER_PEANO_MONOTONICITY_AUDIT_091.md`. For the cofactors ell of the last column of [w,v,w'',*], w=tPhi, v=−Phi', Pi(s)=Σell_i(s−t_i)_+, W3=w³(B')²J>0 real 086. Near ANY t0>0 with t_i=t0+(i−1)eps, ell=eps³W3[−1,3,−3,1]+O(eps⁴). (Pi/s)'=Σ_active ell_i t_i/s² has a first prefix <0 and a second >0; this refutes both global monotonicities for ALL nodes. Exact Peano det[w,v,w'',K]=∫s zeta[Pi/s−Pi(b)/b] preserves moment/crossing and Fubini. Only that sufficient criterion fails: the integral / anchored minor / REAL T_h remain OPEN, compensation possible, real ECT R4 089 not refuted. No negative W / new W / T / global. Independent re-check passed, checked against the map.


### Step 092 — REAL zero of the elimination chart Delta (PROVED bounded)

Sources phase211: `POWER_SHIFTED_WRONSKIAN_092.md`, `POWER_SHIFTED_WRONSKIAN_AUDIT_092.md`, `tools/power_shifted_wronskian_092_verify.py`. Identity Delta=−W(w'',v'',w⁴)/(w³k²J). Near 0, W_shift=8Phi0³t⁶[D0+O(t²)], with −56488961026<D0<−56488961025 using EXACTLY the intervals of 087; verifier PASS on independent reruns, checked against the map, no other theta. Exterior 088 jets V_j=2^j y+O(1) up to 6 pay a finite polynomial: W_shift/Phi³=4096(2t²−1)y⁹+O(t²y⁸)>0 eventually. By continuity Delta has a REAL zero, the 2×2 chart is not globally invertible. Abel: both images D3(1/w), D3(t/w) have a Wronskian not identically zero but with a zero; no monic homogeneous 2nd-order ODE with GLOBAL continuous coefficients can contain BOTH. This excludes only that universal regularization, not a particular cancellation K / another ODE / gauge / chart / order. No negative W / anchored minor decided / new W / T / global. Checked against the map; check passed.


### Step 093 — Particular REAL jet selected by the boundaries (PROVED local)

Sources phase211: `POWER_PARTICULAR_ORIGIN_DESIGN_093.md`, `POWER_PARTICULAR_ORIGIN_AUDIT_093.md`, `tools/power_particular_origin_093_verify.py`. D_part=Pκ+Qc+R, κ=τ0/a−1; NUM=QPhi0I0+PI1I0+(R−P)Phi0I2=Phi0I2D_part. SINGLE test of moments I0..2: 128 cells [0,2], Taylor 64 / cap 65 / 512 bits, 16 theta modes + complete coefficient tails + temporal remainder 2^-140; parameters checked before the run. Run 37905 exit 0 PASS 128 / NEGATIVE, hash 57c0656deb1767e00a4de674a0f5f6556886eca06edbc93ae1ef8488b032c67e; independent reproduction 94506 exit 0 / FULL PASS 128 and same hash. D_part<0 (approx −21658.19847758, read-only) ⇒ W(w,v,w'',K)<0 on an existing neighbourhood of the origin, without radius. Verifies (does not falsify) the particular local premise; not global QF / selector cone / universal Delta / new W / T. Mathematical/literal check against the map passed.


### Step 094 — Exact distance and density of the diagonal UNION in L² (PROVED)

Sources phase211: `POWER_HIGHPASS_DIAGONAL_DENSITY_094.md`, `POWER_HIGHPASS_DIAGONAL_DENSITY_AUDIT_094.md`. The unweighted UNITARY Cayley map takes Q^rV_n to S_{n,r}=(1+z)^r P_{deg<n}. dist²(1,S)=1−A, A=[(n+r−1)!]²/[(n−1)!(n+2r−1)!], by Gram/Dodgson with boundaries a0/b0. exp(−r²/n)<=A<=exp(−r²/(n+2r−1)) upper r>=1; r=0: A=1. UNION_n Q^{r(n)}V_n is L²-dense iff liminf r(n)²/n=0; the proof is in the SAME space for approximating polynomials, and finite exceptions with 1+εz^M. All blocks r>=n have distance >1/2 to the base vector; finitely many confluent blocks at a fixed rate do not repair the UNION. Difference from 016: weighted norm there, EXACT unweighted L² distance here. Does NOT claim linear envelope / continuity of W / crossings / mixtures nor new W / T / global. Independent re-checks passed, checked against the map.


### Step 095 — PARTICULAR tail K with three full derivatives (PROVED analytic)

Sources phase211: `POWER_PARTICULAR_TAIL_095.md`, `POWER_PARTICULAR_TAIL_AUDIT_095.md`. For the real K selected by the tail, W(tPhi,−Phi',(tPhi)'',K)<−3071Phi⁴t²y² for ALL t>=64. COMPLETE theta strip |R_theta|<2^-460 ⇒ holomorphic p bound; exact IBP K/Phi=1/p+remainder (6+25|z|)/Y², Cauchy controls 3 derivatives (no real O differentiated). Model W[t,q,tq²,1/q]=−128q²(6t²+4t−1); 7 multilinear errors paid by C=1e6(1+39321600)³<2^98, analytic threshold 64 without samples. Object distinct from the original density of 088 / universal chart of 092; avoids inverting Delta. 093 only gives the origin without radius, the intermediate interval is OPEN; no global particular / selection cone nor new W / T / generators. Checked against the map; check passed.


### Step 096 — Uniform projection with ALL rates, fixed target (PROVED)

Sources phase211: `POWER_VARIABLE_RATE_HIGHPASS_096.md`, `POWER_VARIABLE_RATE_HIGHPASS_AUDIT_096.md`. For FIXED f0(t)=sqrt(2u0)exp(−u0t) and ALL u>0, n>=1, r>=1e12n³, ||Proj_(Q_u^rV_n(u))f0||²<=200n/sqrt(r)<=1/5000. Hence the distance to the UNION with ALL rates is >=sqrt(4999/5000). Self-contained Gegenbauer/Rodrigues/Gamma proof, centring with both parities and factor 4^r/pi, NEAR by imaginary evaluations, FAR by the exact Gram of 094 and explicit logs; no campaigns. Difference from 094: there fixed rate, here fixed target and variable rate; difference from 016: here unweighted L². Cone 060 included. NOT linear envelope / crossings / mixtures nor other initial continuous families; no negative W nor global closure/impossibility nor new T. Independent re-checks passed, checked against the map.


### Step 097 — Direct REAL T_h, tail u>=512 and regular jet (PROVED bounded)

Sources phase211: `POWER_DIRECT_RECIPROCAL_TURAN_097.md`, `POWER_DIRECT_RECIPROCAL_TURAN_AUDIT_097.md`. Exact identity T_h=a[auN_S−4C_h]/[16u³(au−M)⁴]. BOX 084 with COMPLETE arithmetic gives N_S>2M², C_h<4M³; anchor 078 a>1/25 and monotone M upper / gap prove au>8M for ALL u>=512 ⇒ T_h>0 there. No samples / new certificate. Regular origin N=M/u=a+b1x+...+b4x⁴, b1<0 by 086; T_h0=12a/b1⁴ det Hankel3(a..b4), sign NOT evaluated. Exact target weaker than the particular Wronskian of 093/095; slope u ≠ time t. Compact range 0<u<512 OPEN, no global T_h / R_G for all P / triples G_p / five / all orders / new W / T. Independent re-check passed, checked against the map.


### Step 098 — Exact REAL T_h at the origin (PROVED local)

Sources phase211: `POWER_EXACT_H_ORIGIN_DESIGN_098.md`, `POWER_EXACT_H_ORIGIN_AUDIT_098.md`, `tools/power_exact_h_origin_098_verify.py`. SINGLE test of six even moments I0..I10 with 128 cells [0,2], Taylor 64 / cap 65 / 512 bits, 16 modes + complete EPS coefficient, REM 1e12 adapted and temporal tail 2^-138 for order 10. Z prec 11 → log 11 / M prec 10 gives the N coefficients, cumulants a..e; H3=ace−ad²−b²e+2bcd−c³ and T_h0=12aH3/b⁴. Run 19778 exit 0 FULL PASS / H3 POSITIVE, hash bebcca70c5dd54ba53841e77542aa3e3e2ea059306061dc676e24f88ee5117c9; independent reproduction 57072 exit 0 / FULL PASS 128 and same hash. Thus REAL T_h(0)>0 (approx 3.15513e−5, read-only) and an existing positive neighbourhood without radius. EXACT target weaker than the particular density of 093; auxiliary 0 is not a W exponent. Intermediate compact range up to 097 u=512 OPEN, no global T_h / triples G_p / five / new W / T. Mathematical/literal check against the map passed.


### Step 099 — Global REAL T_h, triples G_p and five anchored AUX nodes (PROVED)

Sources phase211: `POWER_STATE_099.md`, `POWER_EXACT_H_GLOBAL_DESIGN_099.md`, `POWER_EXACT_H_GLOBAL_AUDIT_099.md`, `POWER_SCHUR_TRIPLES_APPLICATION_099.md`. Run 98529 FULL PASS 2048 / hash 6712eb8542b4d8b7e0836260fba831cd44ccaffb7f1ea321df0a0a32668d51d7; independent rerun 8310 exit 0 / FULL PASS 2048 and same hash. S=Ntilde/u¹⁵=(16/a)NUM, λ ENTIRE even; local Schwarz / PSPC polys and gauge exp(−4Mc(u−c)) fixed before the data pay Cauchy B 2^169 / Taylor 104 / cap 109 / 1024 bits, 2048 cells [0,512], no tuning during the run. Together with 097 ⇒ T_h>0 for ALL x>0, 098 incl. 0. 090 anchor + 082 ⇒ R_G/S_G strictly concave and ALL triples K_Gp PD for ALL p. Double REAL Schur congruence (d_i not necessarily positive) ⇒ block K_M{0,p,z1,z2,z3} PD. The auxiliary 0 corresponds to a_orig 1/2, NOT admissible: NOT five arbitrary W generators, new W / T / all orders; the next Turán remainder OPEN. Checked against the map; check passed.


### Step 100 — REAL observable of the J/K pair is not increasing (PROVED, bounded class)

Sources phase211: `POWER_PAIR_OBSERVABLE_SCOPE_100.md`, `POWER_PAIR_OBSERVABLE_SCOPE_AUDIT_100.md`. For positive EVEN K (078) / J, eta=−K'/J is odd and smooth, eta0=0 and 0<eta(t)<a/t for ALL t>0 ⇒ eta→0 at ∞, not monotone in any global sense. Balance ∫(aPhi−J)=0 + one crossing pays −K'>0. Exact two-sided IBP E_(J,u)eta=uZ_K/Z_J=ub=a/M−1/u, h=u/E eta. F(u) already in 081, explicitly attributed, not another NO-GO for F/G_p; new temporal observable object of THE pair. Only invalidates the class that requires increasing eta, not other comparisons / data / pairs / invariants. No T_h / negative W, new coverage / all orders / T / global; 099 remains PROVED. Checked against the map; check passed.


### Step 101 — Log-convex curvature of the potential insufficient (PROVED, check passed)

Source phase211: `POWER_LOGCONVEX_CURVATURE_OBSTRUCTION_101.md`. Explicit AUX potential V=A[cosh(t)+10^-4 cosh(10t)], A=10^46: V''>1, V'''/V'' strictly increasing by strict log-convexity of V'', ALL even derivatives positive and ALL odd ones positive for t>0. Three nodes U_i=A*i*10^-4 and vector (1,-2,1) give c^tK_Mc<−3delta^4/(2A): inverse of v' with fifth jet d=−51675000000000/107213535210701<−2/5, elementary remainder <=100u^7; exact IBP concentration <=A^-1/2. Difference from 074: there a polynomial potential, curvature not log-convex in the tail and vanishing high derivatives. Only refutes that reinforced generic candidate of 073; does NOT incorporate all the inputs 077/089/099, which the negative triple cannot satisfy jointly. No negative Phi/W, new coverage, general inheritance or global sign; 099 still in force. DEDUP lookup and rational check PASS; source and independent check `POWER_LOGCONVEX_CURVATURE_AUDIT_101.md` passed; coefficients and costs reproduced with exact Fraction.


### Step 102 — Strictly decreasing REAL temporal quotients (PROVED)

Sources phase211: `POWER_REAL_PAIR_MONOTONICITY_102.md`, `POWER_REAL_PAIR_MONOTONICITY_AUDIT_102.md`. (K_even/J)'<0 for ALL t>0 by valley 077 + even Rolle with boundaries; (Psi_p/D_p)'<0 for ALL p, t>0 by odd ECT4 089 ⇒ EVEN Chebyshev4 [J,Phi,J'',Phi'']. For F=Psi−rD, L_pF''=(1+rp)J''+(pbeta−p²)J−rcPhi''−betacPhi has <=3 roots; Rolle D² and L_p gain 2, rule out a double root of F / stationary point of the ratio. Positive tails 0<Psi/D<=2tau/c→0 fix the sign; exact normalization G_p=c z Z_Psi/Z_D. Multiplicities / boundaries / supertails preserved, no new certificates. Object DISTINCT from eta of 100 (no contradiction); uses the real 075, 077, 089, not the false generic hypothesis of 101. Only the current pairs / first pivot: preservation of ECT4 / positivity after a new reduction / all orders OPEN, no extra W / T / five admissible. Independent re-checks passed, checked against the map.

**Corollary 102 §8 accepted (same result, extended):** A=D_p, B=Psi_p and F=zZ_B/Z_A=G_p/c. Cov(rho,t tanh zt)<0 ⇒ q a_F>d and h=dA−qB has a −/+ crossing with cosh balance. Green 075 constructs E>0, even / supertail / Neumann, Z_E=(dZ_A−qZ_B)/(z²−q²). F1=d/z(Z_B/Z_E−q), residue r_q=q d²/(q a_F−d)>0. U=B−gammaE of mass 0 is the NEW numerator: crossing / positive density Xi still OPEN; not inferred from B/A. The original scale G_p=cF preserves cE, cF1, cr. Next denominator PROVED, full pair / monotonicity / inheritance to all orders not. Independent re-checks passed, checked against the map; no new W / T.

**Complement 099+102 (PROVED, same block):** with the ADDITIONAL input 099, R_F, S_F for F=G_p/c are strictly concave and analytic at 0 (a_F>0). DET3 with 0 and strictly negative divided differences, incl. [0,q²,q²], give K_F{0,q,z} PD. Double Schur ⇒ R_next(z)>0 for z!=q; positive quadratic coefficients DET3/ell² and ell'(q)>0 prove R_next(q)>0. Thus the transformed REAL remainder is already positive for ALL p,q,z>0, not only denominator/residue. U crossing / Xi positive / monotonicity of the new pair / crossing kernel remain OPEN: transformed positivity ≠ positive density. Auxiliary 0 NOT admissible for W, no new W / T / all orders.


### Step 103 — REAL limit of the pair and pointwise sign at the origin (PROVED)

Sources phase211: `POWER_REAL_PAIR_DOUBLE_LIMIT_103.md`, `POWER_REAL_PAIR_LIMIT_ORIGIN_DESIGN_103.md`, `POWER_REAL_PAIR_DOUBLE_LIMIT_AUDIT_103.md`. Positive scalings A_p=pD_p and B_p=(ap/M(p))Psi_p converge to (J,K_even) in norms with a fixed exponential weight and derivatives, by the two-sided resolvent and the double primitive. For fixed q the Green function is continuous; then E_*(q)/q→H, H''=b0J−K, b0=massK/massJ, Hmass>0. Thus U_lim=K−(massK/massH)H. The single pointwise test P=720I0²(K0Hmass−KmassH0), an eight-term polynomial in I0,...,I6, came out NEGATIVE: P=[−3.1683047444094325e−13±2.16e−30], U_lim(0)=[−1.35855717857699839e−6±8.09e−24]. Fixed certificate 128 cells [0,2] / Taylor 64 / cap 65 / 512 bits / 16 modes, complete theta and temporal tails. Runs 68812 and 91737 exit 0 / FULL PASS; hash 5090a71fd7dd4ae786a3f785ca8a4c32d6691cf92af912d4e5fffff9e583d080. Mathematical/literal check against the map and independent rerun passed. Also U_original(0)<0 for fixed small q and sufficiently large p, without explicit thresholds. Only a pointwise sign at the origin: NOT a falsifier, global crossing, Xi positivity, new W/T or closure of orders; 099+102 remain in force. Papers untouched.


**Later analytic extension of 103 (PROVED, no new test):** H/K_even is strictly decreasing for ALL t>0. For F=H−rK, D⁴F=(b0+r)D²J−raD²Phi−aPhi+J is a nontrivial combination of EVEN4 (102). Double even Rolle with boundaries excludes double roots of F and stationary points of the quotient. Tail K>=aI/2, H<=b0tauI ⇒ H/K→0 fixes the strict sign. Mass averaging ⇒ U_lim=K−(Kmass/Hmass)H has exactly ONE simple −/+ crossing and Xi_lim=G0U_lim>0. The complete LIMIT case is proved; the earlier negative origin certificate is kept as a chronologically earlier independent check. The global crossing does NOT propagate through limits to FINITE parameters p,q, and there is no new W/T/all orders. Independent re-check passed, checked against the map.


**Extension of 103 to ALL q>0 (PROVED):** for the REAL pair (J,K), E_q=G_q(dJ−qK), d=qZ_K(q)/Z_J(q)>0. L_q(E_q−rK)''=(d+r)J''−raPhi''+a(rq²−q)Phi+(q−rq²)J is a nontrivial EVEN4; Rolle D²+L_q excludes stationary points of E_q/K. Continuity in q for each t and the C1 limit E_q/q→H fix (E_q/K)'<0 for ALL q,t>0. Strict mass averaging ⇒ U_q has a unique simple −/+ crossing and Xi_q>0 for ALL q. The final result no longer requires small q; it is still the pair p→infinity, WITHOUT a global conclusion for FINITE p nor new W/T/all orders. Independent re-check passed, checked against the map, no new computation.


**Exact bridge from 103 to FINITE pivots (PROVED):** With lambda=p²M(p)/(ap−M(p)), one has beta D_p+p²Psi_p=lambda K, L_pPsi_p=J−lambda K and Psi_p=(lambda/p)E_*(p). Hence Psi_p/K is strictly decreasing and D_p/K strictly increasing for ALL finite p,t>0, via 103 for all q, without assuming stability of the crossing under limits. For U=Psi−gammaE, L_pL_qU is a combination of [K,J,Phi,J''] with K coefficient equal to −lambda alpha≠0, alpha=gammaq−q²>0. The Chebyshev4 property of this MIXED family would suffice, but it remains OPEN: EVEN4 does not prove it; the antecedents 093/095 are kept. Under that sufficient input, the −/+ orientation also uses R_next>=0, already deduced from 099+102 via Schur for z distinct from q and continuity at the removable value z=q. The reverse orientation would force Xi<0 and a contradiction. No new global crossing of finite U, Xi positivity, W/T sign or all orders is claimed; no other certificate was run. Independent re-check passed, checked against the map.

**Mixed prefixes 103 (PROVED):** [K,Phi,J] is a global extended Chebyshev system of dimension 3: f=AK+BPhi+CJ with three roots would give a nontrivial D²f in EVEN4 with at least four. For tau=J/Phi, kappa=K/Phi=tau(K/J), S=kappa'/tau'>0 and W(Phi,J,K)=Phi³(tau')²S' never vanishes. S'>0 would contradict (K/J)'<0 via the tail average of S; thus S'<0 and kappa is strictly convex as a function of tau. The first three Wronskians in the order [K,J,Phi] are positive. The FOURTH mixed one remains OPEN; no new certificate nor W/T/all-orders sign. Independent re-check passed, checked against the map.


### Step 104 — Positive mixed origin test and analytic tail (PROVED, local scope)

Sources phase211: `POWER_MIXED_FOUR_ORIGIN_DESIGN_104.md`, `POWER_MIXED_FOUR_ORIGIN_AUDIT_104.md`. Family [K_even,J,Phi,J'']; matrix regularized in lambda=t², factors k! and bridge W_t=64Phi0⁴t⁶[D_mix+O(t²)]. Recovery of 087 INTACT by hash and complete rational boxes of 103, no new quadrature. Run and independent rerun exit 0 / PASS: D_mix>0 (exact endpoints in source/log), hash 063ce9ba28dc9b0e3cca245018a968794b5b28c7a57df5da7a5c70d008b95105. Log 104 persists Phi0, z1, z2, z3 outward, previously not archived. An independent holomorphic proof with the whole theta tail and 7 multilinear errors gives W_mixed/Phi⁴>6t²/y² for ALL t>=64. Hence positive origin on an existing neighbourhood WITHOUT radius and positive tail; intermediate compact range OPEN. Global prefixes 1–3 of 103 in force, but NOT global Cheb4, falsifier, finite U crossing / positive Xi, new W/T/all orders. Independent re-checks passed, checked against the map; no more tests. Papers untouched.


### Step 105 — Raw mixed Volterra kernel of variable sign (PROVED, bounded class)

Sources phase211: `POWER_MIXED_VOLTERRA_OBSTRUCTION_105.md`, `POWER_MIXED_VOLTERRA_AUDIT_105.md`. On the REAL pair, tau=J/Phi, kappa=K/Phi, E=−tau'>0, S=kappa'/tau'>0, w=−S'>0, D=tauS−kappa>0. Exact identity w'+Bw+RS−TD=1, B=(2−2V''tau)/E, R=(tV'−1)'/E, T=(V'^2−V'')'/E. CT3 and K/J→0 give S=tail integral of w and D=tail integral of tau w; kernel H(t,s)=R(t)−T(t)tau(s). Complete theta jets and a change of variable with domination (1+u)e^-u prove tauV'/t→1, then [(tV'−1)'−tau(V'^2−V'')']/(tV')→−2. Thus H<0 near s=t for large t, but H→R(t)>0 as s→infinity. Refutes ONLY pointwise positivity of the RAW kernel, distinct from Peano 091. No sign of the integral, exclusion of gauges/reorderings, mixed W4 / finite U / W nor global obstruction. Independent re-checks passed, checked against the map, no new computations nor papers modified.


### Step 106 — Holomorphic control of normalized mixed integrals (PROVED, no sign)

Sources phase211: `POWER_MIXED_NORMALIZED_INTEGRAL_106.md`, `POWER_MIXED_NORMALIZED_INTEGRAL_AUDIT_106.md`. Strip Re z>=−1/16, |Im z|<=1/16: Theta=(2y−3)(1+R_theta), |R_theta|<1/4, Y=|pi e^{2z}|>21/8. The real variable v and r=.5Log(1+v/y) give EXACT normalized representations of tau=J/Phi and kappa=K/Phi; the real equality is extended holomorphically by domination, no change of contour assumed. The coupled Theta/Jacobian factor pays A<=7/(2Y)e^-v(1+v)^2. Bounds Y|tau|<100(1+|z|), Y²|kappa|<1000(1+|z|); tail v>=512 <2^-450, modes m>=17 <2^-675 for the scaled functions, including numerator/denominator and column X via the log-derivative. Cauchy pays coefficient errors 32^j. The scaled Wronskian bound 2^120 and part-6 divisibility + Schwarz give the regularized bound 2^168. Resolves control of evaluation/errors, NOT positivity. Execution design, finite quadrature / tolerances / partition / order remain PENDING; no run / new jet / sample. Mixed Cheb4 / finite U / W / T / all orders OPEN. Independent re-checks passed, checked against the map; papers untouched.


**Extension 106 §8 (PROVED, tool without execution):** Gauss–Legendre 64 on ten intervals v [0,1],[1,2],...,[256,512], discs of radius 2h, complex domain Re(y+v)>2 and Re(1+sv/y)>4/5. Uniform majorant 2^34 also for a temporal ball parameter of half-width <=1/64, with extended domain |z−c|<=3/64 and constant scales. Cauchy coefficient j and exactness 127 / positive weights pay a total analytic error 2^(−83+5j)<=2^-68 for j<=3. Balls for nodes/weights, arithmetic, mode/v tails and factorials must be paid additionally BEFORE the Wronskian. Mathematical/literal check passed, checked against the map; design 107 / execution / signs remain pending.


### Step 107 — Mixed compact certificate INCONCLUSIVE (reproduced)

Sources phase211: `POWER_MIXED_FOUR_COMPACT_DESIGN_107.md`, `POWER_MIXED_FOUR_COMPACT_AUDIT_107.md`. Design/literals checked BEFORE the data: origin lambda [0,.25], Phi 128 / cap 1025 / 1024 bits / Taylor 512, J/K recurrences and moment 103; REST Gauss 64*10 / 512 bits / cap 4/5; left-first subdivision depth 10 / eval 8192 fixed. Run 5594 and the independent reproduction 46719 ended exit 2 / INCONCLUSIVE at the origin: 11 eval, 0 accepted, depth 10 lambda [0,1/65536], det [+/−2.94e−3]. REST NOT executed. Logs of both runs persisted; hash main 2a7d147caf8181adb5aa29eb6fcbe356f625e2743ad6765e6ac543aacad23054, origin 15d6f12c197ef52c062a12c59ee4a7c5db94c74e0073e8463a7ce03dd613e553 identical / unmodified. Only insufficient enclosure with THIS budget: NOT a falsifier / mathematical obstruction / negative sign / global Cheb4 / finite U / W / T / all orders. A new representation requires another design checked before the run; no tuning to force a PASS. Papers untouched.


### Step 108 — Correlated polynomial determinant INCONCLUSIVE (reproduced)

Sources phase211: `POWER_MIXED_FOUR_POLYNOMIAL_DESIGN_108.md`, `POWER_MIXED_FOUR_POLYNOMIAL_AUDIT_108.md`. Algebraic change checked BEFORE the data: form 24 complete permutations in polynomials, real degree 2042 (<=2048), Taylor shift of all coefficients + error 2^-200; construction routines and budgets of 107 intact. Runs 82660 and 28564 exit 2 / INCONCLUSIVE: 15 eval 4 accepted, coverage λ [0,141/8192], depth 10 on [141/8192,1129/65536], det ±2.04e−4; REST NO. Hash 108 eb200a9061a3761d2b1a5dc5ca38def6c5c16e1e0901524c39969555eb791f6a; 107 hashes intact. Logs of both runs persisted. Profile ONLY from locals ALREADY computed, no extra probe: final coefficient 0±1.79e−4 and additional radius ≈2.456e−5, so the central uncertainty is not confused with cell variation. Does not decide a real zero / single cause of the width. INCONCLUSIVE, not a falsifier / mathematical obstruction / global Cheb4 / finite U / W / T / all orders. Another representation requires a prior design, no tuning for PASS. Papers untouched.


### Step 109 — Cauchy clip: origin PASS; full certificate INCONCLUSIVE due to budget

Sources phase211: `POWER_MIXED_FOUR_CAUCHY_CLIP_DESIGN_109.md`, `POWER_MIXED_FOUR_CAUCHY_CLIP_AUDIT_109.md`. Intersection of the BASE coefficients of 107 with Cauchy |phi_k|<=2^(40+k), |J_k|,|K_k|<=2^(42+k), before re-deriving / Q / det 108; true coefficients preserved, remainder 2^-200 and same parameters. Run 52183 ended exit 2 / INCONCLUSIVE: origin PASS 16/16 lambda [0,.25], REST 8192 eval, 4113 leaves accepted. A Fraction check of the log confirms contiguous REST coverage [1/2,2645/512], length 2389/512. Next cell [2645/512,1323/256], depth 6, NOT evaluated because of the cap; no failure by depth / negative sign. Driver hash c3fe2df06692622dcaddbb4f2eb21047a7f4be46affdbe151af27f25bbef48ba and 107/108 intact. NO independent reproduction of 109 nor FULL PASS. No global Cheb4 / finite U / W / T / all orders / mathematical obstruction. Log persisted; papers untouched; mathematical/literal/log check against the map, with no new evaluation in the check.


### Step 110 — Factored theta quotient: CHECKED, run in progress

Sources phase211: `POWER_MIXED_FOUR_FACTORED_RATIO_DESIGN_110.md`, `POWER_MIXED_FOUR_FACTORED_RATIO_AUDIT_110.md`. Condition of 109 without FULL PASS satisfied by exit 2. Exact identity Theta16=(2y−3)(1+R16), B_m=m⁴+3m²(m²−1)/(2y−3); ratio=(1+2v/d)(1+R_shift)/(1+R), p16=2y−9/2−6/d−R_t/(1+R). No modes omitted nor function changed; same origin 109, Gauss 107, errors / parameters / DFS / budgets. Design and literals checked against the map and independently BEFORE the data (cache m−1 correct, hash guards on four files, no patch). First authorized run in progress, WITHOUT final result; no reproduction nor PASS anticipated. No improvement of enclosure or cost is promised. Identity / representation control, no new W/T/all orders; papers untouched.


### Step 111 — Individual monotonicities for all p insufficient for TP2 (PROVED, auxiliary class)

Sources phase211: `POWER_GREEN_PAIR_TP2_SCOPE_111.md`, `POWER_GREEN_PAIR_TP2_AUDIT_111.md`. Abstract pair K=1_(|t|<2), J=(1+1_(1<|t|<2))K. Lambda_p=2−1/(2cosh p) and the exact compact C1 Green V_p give V_p>0, (V_p/K)'<0 for ALL p>0 on (0,2). Same params 1,2: the ratio V2/V1 increases on (0,.5], decreases on (1,2), by analytic inequalities; minors at nodes (.25,.5) and (1.5,1.75) have opposite signs. Even with J/K strictly ↑: adding delta t² for delta>0 sufficiently small preserves both minors by continuity; W=V_p' solves L_pW=2delta t+Dirac1 with Dirichlet 0, negative Green proves the monotonicities for all p. Smoothing the interior step with indicator K is also admissible; smooth compact boundaries with all p are NOT claimed. Only a NO-GO for the generic implication individual monotonicities ⇒ TP2, NOT the REAL pair / differential compatibility 103 / MIXED4 / W / all orders. Dedup 074/101/091/105 distinct objects. Mathematical/literal check passed, checked against the map, no computations/campaigns, papers untouched.


**Extension 111 §5.3 (PROVED, same counter-class):** V(x,t), x=p², is moreover strictly completely monotone in x for EVERY order and interior t. q_x=−partial_tV satisfies (−D²+x)q_x=mu, a fixed positive measure (Dirac1, or Dirac1+2delta t dt), Dirichlet 0,2. Positive / smooth Green on compact x-sets allows differentiation with a finite measure: A_x partial_x^n q_x=−n partial_x^(n−1)q_x, by induction strictly alternating signs. V=integral_t² q_x inherits CM of all orders. The SAME opposite TP2 minors persist: adding parametric CM to the individual monotonicities for all p does NOT imply TP2. Auxiliary only, no CM of the REAL pair decided nor W / all orders refuted. Mathematical/literal check passed, checked against the map; no data nor campaigns.


**Later analytic improvement of 104 (PROVED, no data):** keeping the powers of y in the 7 errors gives 61440Ht³/y³+6144H²t³/y⁴+192H³t³/y⁵. For y>=H the sum is <2^17Ht³/y³. e²>7 and the integer comparison 3*7^16=99698791708803>82463372083200=16·2^17H, with H=39321600; y/t ↑ pays an error <t²/y² for ALL t>=16. Model >7t²/y² ⇒ W_mixed/Phi⁴>6t²/y² for ALL t>=16, improving 64. Independent re-check against the map, no sampling / new theta certificate. Does NOT touch 110 nor declare compact/global/W before coverage and reproduction.


**Result of run 110:** run 52878 ended exit 2 / INCONCLUSIVE due to budget 8192, 4198 REST leaves accepted and origin PASS 16/16. An independent Fraction parser confirms contiguous REST coverage [1/2,845/32], length 829/32. Next [845/32,3381/128], depth 4, pending at the cap. Driver hash c629d4ed4b5eeb625a69ee92f6000892b9493c50e825e9ade73bf3a5a9362108. NO FULL PASS of the program up to 64. Independent replica 12244 follows the SAME program/budget without stopping at 16; global WM 112 still CONDITIONAL until independent coverage to 16 + TAIL 104. No falsifier / mathematical obstruction, no anticipated activation.


### POWER — Strategic review and auxiliary WM closure (no closure of the sign)

Source phase211: `POWER_REASSESSMENT.md`; update of 110/112. Explicit antecedent: generating function of R162_803, Theorem H, and D-16; POWER uses its real Pick-type kernel. The difference declared in 001 justifies finite cases and falsifiers, not a new uniform mechanism. REF-D is not used as an impossibility. On the user's instruction, the automatic continuation of the tower is abandoned: a new candidate must identify a property that controls all sizes and a verifiable difference from the previous obstructions.

WM PROVED: the logs of 110 from the run and the independent rerun are identical (SHA256 90a2ec137e806c8a7f8cce975f7af1cee375d9e48bdaf1c5bc302f7c06428539), complete origin and 4198 contiguous REST leaves [1/2,845/32], both INCONCLUSIVE due to 8192 evaluations, no FULL PASS up to 64. The analytic tail 104 from 16 overlaps and completes W_mixed>0 for all t>0; prefixes 103 give MIXED4. The checked consequences of 112 are activated (positive Xi, E/Psi comparison, real TP2 / confluence and quotients of the limit pair). Not five arbitrary powers, indefinite preservation, all orders nor a new window T. Papers untouched; global goal OPEN.


**Cross-cutting check after the POWER review:** phase211 `POWER_CORPUS_OPPORTUNITY_AUDIT.md` and `POWER_GLOBAL_ROUTE_REVIEW.md`. Indices, LEDGER and selected primary sources were cross-checked; no exhaustive rereading of the corpus is claimed. No justified new global candidate has yet been identified among the families examined. Class falsifiers, reductions and open obligations are distinguished; REF-D is not used as an impossibility. Obsolete labels of O-151.4 and 06R4 were corrected, and the logical correction of TB3-neg from R186_092 is incorporated. No new tower/certificate nor global sign.


### Completeness on perfect powers — algebraic scope and checked falsifiers

Sources phase211: `SQUARE_COMPLETENESS_OBSTRUCTION.md`, `SQUARE_COMPLETENESS_AUDIT.md` (PROVED, no new execution). Local F_p=(1+c_pz)/(1−z²), 0<=c_p<=1, gives multiplicative N with 0<=N<=1, N(n²)=1, ell>=0. Endpoint c2=0, others 1: ζ/(1+2^-s), antecedent R163102 Cor F / R163191, residue 2/3 without assumed FE. Reuses the SAME primitive even witness 007_C Thm 1 with x>1; analytic boundaries give C_F(log4)>0, so W_new=W_a3−2log2 C4<0. Each FIXED m>=2 is also insufficient with integer N in 0/1: replacing 2→2^m, N(n^m)=1; for m>=3 no atom 2 before 8 ⇒ W_m=W_a3<0, residue 1/[2(1−2^-m)]<1.

**ALL orders simultaneously, without integrality:** local 2=(1−z/2+z²/2)/(1−z), other primes ordinary, N2=1/2, N2^k=1 for k>=2 ⇒ N(n^m)=1 for ALL n, m>=2. The formal roots r±=(1±i√7)/4 show ell(2^k)/log2=1−r+^k−r-^k>=0. Weights v2=√2log2/2<1/2, v4=7log2/4 and the SAME 007C give W<−.00528norm². Residue 7/8, FE not assumed; does not falsify integrality / residue 1 / additional compatibility.

**Selection/identification, NOT sign:** in the ansatz c_p∈[0,1], EXACT residue 1 forces c_p=1 even for infinitely many (product ≤ one factor). More generally, multiplicative N + ALL perfect powers + integer N(p)>=0 + ell>=0 forces N≡1: ell(p²)/logp=2−c² ⇒ c=0/1, and c=0 local (1+z³)/(1−z²) gives ell(p⁶)/logp=−1. This identifies Lambda, it does not prove its sign. Only an exclusion of sufficiency of the declared classes, NOT a global impossibility of every use of squares/completeness, NOT negative Λ, new coverage W/T nor campaign. Independent re-checks completed, checked against the map; papers untouched.


**Extension to normalized residue (§11, PROVED, same bounded class):** the simultaneous local factor at 2 is kept and finitely many p>=7 are added with P_delta=1+delta z−delta z², 0<=delta<=2/5. N_p=1+delta, N_p^k=1 for k>=2; factors r,s give ell_odd>0, ell_even>=logp/25. Divergence of Σ1/p allows choosing finitely, with a last rational delta, an EXACT product of residues 8/7. Thus F=ζR, R a finite Dirichlet polynomial, R1=1: residue 1, sum N=x+O(1), multiplicative N with 0<=N<=C finite, ALL-POWERS and ell>=0. Compensators p>=7 invisible to 007C ⇒ SAME value W<−.00528norm². NOT N<=1 (N_p>1 high), NOT integrality (N2=.5), NOT FE / small Bohr defect. Antecedents Lemma S R163102 / resnormal R163802; no Euler idea presented as new. Does not contradict the collapse of §7 nor 197 (control of Delta ≠ residue). Literal re-check passed, checked against the map, no new data nor campaigns.


### Gram by theta translation — identity and obstruction of PSD layers

**PROVED, limited scope.** Sources phase211: `POWER_GRAM_SLICES_OBSTRUCTION.md`, `POWER_GRAM_SLICES_AUDIT.md`; independent re-checks and a check against the map, no new certificates. A(t,s)=integral_0^infinity(t+s+2r)Phi(t+r)Phi(s+r)dr has double transform [Z′(u)Z(v)+Z(u)Z′(v)]/(u+v), without factor 2. Its exact disintegration in v gives Gram layers for the quartic model. For REAL Phi not all of them can be PSD: the normalized derivative requires CND of [V′(t)+V′(s)]/(t+s), refuted with three positive nodes and V′(R)/R³→infinity. **PSD of A remains OPEN**; no negative W, new coverage nor impossibility of another Gram. Targeted dedup 103_47/48, 073/074, N_BUILD014/016/018, C9 with no literal duplicate found; classical Gram/Pólya framework, no claim of never-attempted. Joint compensation between layers still without a new bound.


**Gram addendum — operations (PROVED, same entry):** 074 already refutes the sufficiency of V=g(t²) convex with all its derivatives nonnegative. A mixture of two distinct Gaussians fails: (M/u)'=u Var(v)>0 contradicts pairs 001. Convolution preserves the transformed kernel by adding M; but a positive mixture of quartics or convolution with a quartic factor imposes a lower tail exp(-Ct⁴), incompatible with real Phi. The hazard correction D diag B has diagonal (f-tf')/f²<0 by 073, it cannot be discarded as PSD. Even a positive operator Bop(-Phi')=tPhi exists for the Gaussian mixture and does not suffice: the form A keeps an uncontrolled half-line term. Only the declared sufficiencies are refuted; real A OPEN. Gram note §7 and its check, no new data.


### Correction of the residual cancellation in L2_BUILD_031 (PROVED)

Sources phase211: `CORRECTION_RESIDUE_BALANCE_031.md`, `CORRECTION_RESIDUE_BALANCE_AUDIT_031.md`. The identity 031 §3 improperly omits moduli p^b<=Q by using B_Q. Exact counterexample M=Q=2, s=(1,1), profile 2T0<log(3/2), smooth interpolant S with support (2/3,5/2), S1=S2=1: W1 has delta rows and the full q2 component is v2/2>0; n>=3 does not contribute. The balance of c2(k) does not transfer to c2(2k). The component is defined through the explicit interpolant 030; it is not claimed to be independent of every interpolation. **Approximation Theorem E intact**, no negative W nor change of the target (S). Warning added to 031 preserving the historical text. Independent re-check, no computations/papers.


**Clarification of the 031 repair (same correction, PROVED):** in R_Q, Q>=2, requiring vanishing of q2 for ALL profiles and interpolants leaves only s=0: profile width <log((M+1)/M) gives W1 delta, odd support makes the coefficient of S(j/2) unique, equal to −s_jv2/2. No collapse proved on mixed support due to dyadic collisions; one narrow example does not decide all profiles. Original Theorem E remains intact. Corrective source §5 and its check, no new data.


**Complement 016 §9 — shifted filter and the limit of diagonals (PROVED):** in `POWER_DESCENT_AUDIT_016.md`, delta=1, u=63/2, eta=3/4, Q_delta=(s+delta)/(s+u) is an isomorphism of the strong H_eta of 014; its external zero avoids the moment-0 hyperplane. By confluent triangularity, the SPAN of ANY tail f_r=Q_delta^r/(s+u) is dense. The complete binomial identity, with d=delta²/u² and polar product included, plus 015 N1, proves the diagonals W[f_r] and W4[f_r] eventually positive. However W4=W−4norm² has f0 negative (016) and is continuous: some FINITE combination of generators of EACH positive tail gives W4<0. Only refutes inferring the sign of the span from density + diagonals, even with the moment repaired. NOT negative real W, NOT PSD pairs nor uniform over all numerators; no new closed general family, certificate or window. Independent re-checks passed, checked against the map.


### Fixed-size PSD assembly on ladder 002 — limited obstruction (PROVED)

Sources phase211: `POWER_FIXED_BLOCK_ASSEMBLY_OBSTRUCTION.md`, `POWER_FIXED_BLOCK_ASSEMBLY_AUDIT.md`. A certificate C=sum B_alpha, each B_alpha PSD supported on <=k original coordinates, requires ones^T C ones<=k trC. For EVERY fixed k, n=k+1 and nodes of the SAME ladder a_j=32+2N+2j give L(a_j)=.5logN+O_k(1), with integer psi and complete Lambda tail; the normalized block has C_ij→1. Then ones^TC ones→n²>kn=k trC and no such certificate exists for some finite N. Principal submatrices inherit those certificates: neither do the initial blocks of 002 containing the subblock admit them. Case 2 includes PSD2 / scaled Gershgorin assemblies. This excludes summing certificates of size 2/4/13 or of FIXED size for all orders IN THE original BASIS; does NOT imply negative K / arbitrary PSD, NOT other bases / growing blocks / Schur / dense global PSD part. Dedup 186043044 / N018019: classical instruments, distinct classes, no absolute priority. Independent re-checks passed, checked against the map, no computations/papers; global W OPEN.


### Simultaneous shift of exponents: the Loewner order fails (PROVED)

Sources phase211: `POWER_SIMULTANEOUS_SHIFT_OBSTRUCTION.md`, `POWER_SIMULTANEOUS_SHIFT_AUDIT.md`. The full difference D(f,g)=W(f,g)−W(e^(-2t)f,e^(-2t)g) has an indefinite plane. Two norm-1 packets separated by log2, the first at distance O(epsilon) from the causal boundary 0, give D_ff=O(epsilon^(1−2s)), D_gg=O(epsilon^−2s), s=1/8, and D_fg→−3log2/(4sqrt2) through the single contact at 2; smooth ARCH / polar O(epsilon). Determinant →−9log²2/32<0. Strong density 014 and continuity transport this to a FINITE initial block [K(32+i,32+j)−K(34+i,34+j)] that is not PSD. Coefficients of DIRECT exponentials, without confusing the zeta factors of rho. Antecedent N007 atom/bump: here the boundary suppresses one diagonal of the full-W DEFECT and pays the ARCH reserve previously absent. The opposite order already fails diagonally (073). Only this universal shift-2 ordering is refuted; NOT negative W / negative K / other transports nor all shifts. Independent re-checks passed, checked against the map, no data/certificates/papers.


**IMS addendum to the simultaneous shift (same entry, PROVED):** source SHIFT §7 and its check. T=e^(-2t), S=sqrt(1−T²), d=1−T_tT_s−S_tS_s>=0. R=D−W[Sf] preserves ARCH, comb and polar 2cosh. The SAME causal packets give R_ff=O(epsilon), R_gg=O(epsilon²), R_fg→−3v2/8 and R[f±g]→∓3v2/4; IMS remainder indefinite, not negative W. For compact sets separated from 0, sum_r R[T^r f] has exact coefficient d/(1−T_tT_s)∈[0,1], whose limit at (0,log2) is 1, not 0. Convergence justified; S is not assumed Lipschitz at 0. Explicit antecedent IMS 004; no global sign/cancellation inferred nor exclusion of another compensator with its own proof. Literal check against the map passed, no new data/papers.


**Clarification on the anti-Löwner/Stieltjes target (PROVED, no new note):** `POWER_GLOBAL_ROUTE_REVIEW.md`, section L-DER. L'(a)=Laplace[b(t)dt+ΣLambda(n)logn delta_logn], b=t[(exp2t−1)^−1−exp t]. After any tilt A>1 the measure is finite; on (log2,log3) there are no atoms and b<0. There cannot exist a POSITIVE Laplace measure representing L' on ANY ray a>=a0>1. Self-contained uniqueness: tilt, push x=e^(-t), equality of all moments, polynomial approximation of continuous functions. Formal antecedent Paper 37 cor:bernstein for ANOTHER cocycle; 019/020/023 treat the Möbius-gamma inverse, not L'. Does NOT exclude N(x)=M(sqrtx)/sqrtx Stieltjes, NOT negative K/W. It is a guard against 'positive Gamma ⇒ L' positive as a measure', not a closure of target 083. No data/papers.


**Addendum 027 §8 — uniform Gaussian inverses refuted (PROVED, same real mixture):** `POWER_INTERIOR_CONSTRAINT_027.md` and `POWER_JOINT_AUDIT_027.md`. For w_a=x^(-1/2)e^(-a log²x), H_a=−w_a'>0, define FULL h_a=Σmu(m)mH_a(mx), J_a=Σmu(m)w_a(mx), K_a=J_a+xh_a. The FIXED law V_N, inverse gamma of 027, and positive Tonelli + ABSOLUTE Fubini (ΣmH_N(m), Σw_N(m) finite) give h_N(1)=E h_VN(1), K_N(1)=E K_VN(1). The COMPLETE NEG 022 h128(1)<−33/50 and 023 K129(1)<−1/251 force the EXISTENCE of a_h>0 with h_a_h(1)<0 and a_K>0 with K_a_K(1)<0; parameters possibly DIFFERENT, none computed. These are not prefixes nor Jensen/convexity of W. Refutes both UNIVERSAL Gaussian premises of a positive inverse; NOT negative ERR/W, NOT negative heat H_A−P, NOT N Stieltjes excluded. No new data/certificates/papers; independent re-checks passed, checked against the map.


### Hyperbolic model: positive Green for all orders; real transfer open

**PROVED for the model / OPEN for real Phi.** Source phase211: `POWER_HYPERBOLIC_MODEL_GRAM.md`. For phi_a(t)=exp(−a cosh(2t)), a>0, Z_a(u)=K_(u/2)(a), H_a=−D_r²+a²exp(2r) on the half-line with Dirichlet boundary and R_i=(H_a+u_i²/4)^−1. The positive identity M_a(u)/u=(1/2)Tr R_u produces
K_M(u_i,u_j)=(1/2)Tr(H_a R_i R_j)+(u_i u_j/8)Tr(R_i R_j),
a positive Gram sum for ALL orders. Proof via Green/ODE and traces, no new data. The layers of the GramSlices disintegration are NOT all PSD even in this model, since V'(R)/R³→infinity; the Green proves the full kernel of M, without requiring positivity of each layer. A targeted corpus/literature cross-check of antecedents did not find this literal application; no world priority claimed. Independent re-checks passed, checked against the map. The supertail compatible with theta does not transfer the representation: a positive ODE/Green identity for the REAL Phi is missing; mixing positive densities does not automatically preserve the logarithmic kernel either. NO new W/T coverage nor real global closure; papers untouched.


**Hyperbolic model, §7 — two direct transfers excluded (PROVED, restricted scope).** `POWER_HYPERBOLIC_MODEL_GRAM.md` keeps the positive Gram of the model and proves that real Phi is neither a pure positive mixture of exp(-a cosh(2t)) (infinite mass allowed, with integral exp(-a)dmu finite), nor phi_a convolved with a nonzero finite positive measure (without assuming compact support). The real tail is 2pi² exp(9t/2)exp(-pi exp(2t)): its rate forces the extreme support and the representation would impose a bounded prefactor, a contradiction. Difference from the quartic exclusion of GRAM_SLICES §7: same double-exponential order, but incompatible prefactor. Independently re-checked. Does not exclude temporal prefactors, differentiations, signed combinations nor other Green functions; no negative W, new T nor global closure. No new data nor changes in papers.


**Hyperbolic model, §8 — affine prefactor via Robin (PROVED only for the model).** `POWER_HYPERBOLIC_MODEL_GRAM.md`: for a>0, beta>=0, phi=(beta+a cosh(2t))exp(-a cosh(2t)) has transform beta*y_x(0)-y_x'(0), x=u²/4. With m=-y'/y and k=y/y(0), m'=integral k² and R_beta=R_D+k tensor k/(m+beta); the boundary condition is f'(0)=beta f(0), with a positive term beta|f(0)|² in the form. The identity M/u=(1/2)Tr R_beta and the full Gram prove all orders. Neumann beta=0 corresponds to the scale derivation; preservation under general derivations is not claimed. The prefactor exp(2t) is not the exp(9t/2) of theta: real transfer OPEN, no new W/T. Independently re-checked, targeted cross-check against the map, no world priority nor new computations; papers untouched.


**Hyperbolic model, §9 — matrix order of the scale flow refuted (PROVED only for the model).** `POWER_HYPERBOLIC_MODEL_GRAM.md`: although each K_a is PSD, D_a=-a partial_a K_a is not, in all sizes on u>0. The representation P_a(x)=Tr[(H+x/4)^(-1)V_a(H+x/4)^(-1)] has alternating coefficients A_n=(n+1)sum w_j t_j^n, w_j>0. The isolated largest t_j gives A_n A_(n+2)-A_(n+1)^2<0 eventually, with error O(n²rho^n). PSD of D_a would require the opposite minors via finite differences from positive nodes and the even jets. No external Stieltjes theorem nor argument about zeros; no size evaluated nor campaign. Difference from SHIFT: scale of an auxiliary density, not exponents of real tests. Independently re-checked. NOT the theta derivative refuted, NOT negative W, NOT new T; the Gram of the model remains valid. Do not transfer matrix monotonicity from its diagonals.


**Hyperbolic model, §10 — rigidity of the fixed prefactor (PROVED, restricted class).** Source phase211: `POWER_HYPERBOLIC_MODEL_GRAM.md`. For Y_nu(b)=integral exp(-b cosh v)q(v)cosh(nu v)dv, q even, C², positive, and q,q',q'' of at most exponential growth, the source of the equation in r=log(b/a) is F_nu=integral exp(-b cosh v)[-q''+2b sinh(v)q']cosh(nu v)dv. If F_nu(b)=E(b)Y_nu(b) with E independent of nu at only two distinct scales and on an open interval of nu, uniqueness of the transform and evaluation at v=0 force q constant. The real q=Phi(v/2)exp(2pi cosh v) grows like exp(9v/4), so that direct scalar transfer fails. Difference from §7: admits a fixed temporal prefactor, requires a parameter-independent potential. Does not exclude other Green functions, gauges, systems nor scale-dependent prefactors; Robin §8 does not belong to this class. Independently re-checked, targeted dedup against the map; no negative W, global closure nor new T. No computations nor changes in papers.


**Extension of the same class, model §10.1 (PROVED):** admitting Y_rr=A(b)Y_r+[b²+nu²+E(b)]Y, with A,E independent of nu and the same fixed prefactor q, only allows q=C or q=C cosh(v/2). Subtracting two scales in the inverse identity forces q=C cosh(v/2)^alpha; independence of 1, cosh(v), sech²(v/2) forces alpha=0 or 1. The theta q, of growth exp(9v/4), does not belong to this class. Includes the impossibility of repairing this family through a scalar multiplication g(r) independent of nu to obtain z_rr=[nu²+V(r)]z. Does not exclude other changes of variable, integral transforms, scale-dependent prefactors or systems. Explicit difference from §10: now a first derivative is allowed. Independently re-checked, dedup against the map; no new sign nor modifications of papers.


**Additional precision for §10.1, only for the theta q:** allowing Y_rr=A Y_r+[w(b)nu²+B]Y does not repair this family either. Inverting the cosh transform and using q'/q=9/4+O(exp(-v)), q''/q=81/16+O(exp(-v)) forces w=1 through the dominant term (1-w)b²cosh²(v). Thus a C² reparametrization of scale with nonzero derivative accompanied by scalar multiplication, both independent of nu, aiming to give z_tt=[nu²+V(t)]z, is also excluded. Proof in the same §10.1, independently re-checked and cross-checked against the map. No classification for arbitrary q nor exclusion of other families/systems; no new sign.


**Precision of the temporal bridge GramSlices §2.1 (PROVED, no new real sign):** under Gaussian DOM, A is PSD on all of R if and only if K_M is PSD for all sizes with nodes in any fixed open positive interval. The converse uses continuity of the form in L²(exp(-Nt²)dt), density of exponentials with CONTINUOUS exponents by uniqueness of the entire transform, and approximation of deltas. Does not claim density of a discrete ladder under a Gaussian bound nor sufficiency of a fixed size. The existing note POWER_GRAM_SLICES_OBSTRUCTION incorporates the proof; literal re-check passed, dedup against the map. The hyperbolic Gram therefore does sign its full temporal A; not the real one. It is a precision of representation, not a shortcut nor an extension of T.


**Correction of temporal scope, GramSlices §2.2 (PROVED, no new sign):** A_theta is jointly holomorphic in |Im t|,|Im s|<pi/4 by uniform domination of its theta integral. PSD of ALL sizes on any open temporal interval implies PSD on all of R: finite differences give mixed matrices of jets and old points; double and single Taylor also preserve the crossings when enlarging the interval, and it is iterated with fixed radius. Hence A++ PSD would not leave an independent obligation for crossings; that earlier caution is corrected. A++ has not been proved nor does a finite order suffice. Existing source POWER_GRAM_SLICES_OBSTRUCTION §2.2, independently re-checked and cross-checked against the map; no world priority nor new T.


**GramSlices §8 — individual theta modes not PSD, not even locally (PROVED, restricted class).** Phi_n(t)=n^(-1/2)h(t+log n), and the modal kernel A_n has diagonal limit at −infinity (2H/n)(m-log n)<0 for ALL n>=1. The moment m<0 is proved by two recurrences of gamma integrals and Jensen: m<(1/2)log(5/(4pi))<0. Holomorphy in strips and the propagation of §2.2 imply that A_n is not PSD of all sizes on any open interval, even in the tail where Phi_n is positive. Difference from the already recorded modal translation 103_47/48: global falsifier and local scope, not only an identity. Does not refute the full A_theta, which keeps the cross pairs n,m; does not estimate a relative comparison nor extend T. Source POWER_GRAM_SLICES_OBSTRUCTION §8, independently re-checked and cross-checked against the map, no new data nor changes in papers.


**GramSlices §8.1 — complete theta prefixes eventually not PSD (PROVED, crossings kept).** For Phi_M=sum_(n<=M)Phi_n, M^(-1/2)Phi_M(x-log M) converges in L²((1+|x|)dx) to F(x)=-pi exp(5x/2)exp(-pi exp(2x)). Riemann sum and uniform majorants Ce^(5x/2) on the left, Ce^(-x/2) on the right. Then integral tPhi_M²/(Mlog M)→-||F||²<0: all sufficiently large prefixes have a negative diagonal in their kernel A near −infinity and, by analytic continuation, are not PSD on any open interval. Difference from §8: ALL pairs n,m<=M are included. No numerical threshold, no failure of infinite A_theta nor exclusion of compensating the tail; only prevents using eventually PSD prefixes. Source POWER_GRAM_SLICES_OBSTRUCTION §8.1; independently re-checked, dedup against the map, papers untouched.


**GramSlices §8.2 — the first continuous correction does not give PSD approximants either (PROVED).** Q_M=Phi_M+pi M³exp(5t/2)exp(-pi M²exp(2t)) adds the integrated modal tail. Now Q_M→Phi in L²(1+|t|), but integral tQ_M²=−||h||² logM/(4M)+O(1/M+logM/M^(3/2))<0 eventually. Trapezoids of the tail isolate h(t+logM)/(2sqrtM) with a controlled global remainder; all crossings with Phi are also estimated. The negative diagonal and analytic continuation exclude local PSD of all orders. Difference from §8.1: corrected approximant with global convergence, not a raw prefix. Does not refute positivity of the limit nor other corrections. Source POWER_GRAM_SLICES_OBSTRUCTION §8.2; independently re-checked and cross-checked against the map, no campaign nor changes in papers.


**GramSlices §8.3 — corrected symmetrization refuted for ALL M>=1 (PROVED).** S_M=(Q_M+Q_M reflected)/2 removes the odd moment, but has mass >=C>0 and tail −[pi M(3M+1)/4]exp(-5|t|/2). Its transform Z_M(u) tends to −infinity as u approaches 5/2 from below; the mean value before the positive level Z_M(0)/2 gives Z_M>0, Z_M'<0. LT absolutely justified by a two-sided exponential bound produces a negative quadratic test ZZ'/u. Analytic continuation excludes PSD on any interval. Change from §8.2: parity restored, a distinct falsifier keeping the whole form; zeros are not used. Does not refute real Phi nor other repairs. Source POWER_GRAM_SLICES_OBSTRUCTION §8.3; independently re-checked and cross-checked against the map, no data nor changes in papers.


**Scope of GramSlices §§8–8.3:** any repair that coincides with one of the excluded approximants on a right half-line keeps its local negative matrix: A_psi=A_f there because r>=0. Includes reflections and smoothings only on the left, even without analyticity of psi. Keeps the index scopes of each result; does not exclude modifying the right tail nor sign Phi. Consequence independently re-checked, added to the same source, no new route.


**Strengthening of GramSlices §8.1: EVERY raw prefix, M>=1, fails PSD.** Z_[Phi_M](u)=(u-1/2)H_M(u), H_M(u)=½pi^(-u/2-1/4)Gamma(u/2+5/4)sum_(n<=M)n^(-u-1/2)>0. For positive u near 1/2 from below, Z<0, Z'>0; LT gives a negative test ZZ'/u. Absolute convergence without parity via |A|<=B(t)B(s), B(t)²=integral_t^∞(1+x²)Phi_M². Analytic continuation gives local failure on every interval. Replaces the eventual scope of the discarding of raw prefixes and their left-only repairs; keeps intact the mass asymptotics and the eventual scope of Q_M. Independently re-checked, no data nor new real sign.


**GramSlices, modal extension to infinite smooth cutoffs (PROVED):** w_n>=0 nonzero, sum w_n n²<infinity implies that A of phi_w=sum w_n Phi_n is not PSD on any open interval. Fubini and differentiation give Z=(u-1/2)C(u)sum w_n n^(-u-1/2), with a positive C¹ remaining factor; the test ZZ'/u is negative immediately to the left of 1/2. Bounds on substrips and B justify everything without additional moments. Includes exp(-epsilon n²), not temporal heat nor w_n=1. Change from the prefix: smoothed infinite support, all crossings kept. Source POWER_GRAM_SLICES_OBSTRUCTION, independently re-checked and cross-checked against the map; no new real sign nor papers modified.


**Hyperbolic model, §11 — temporal products of cosh excluded (PROVED, exact class).** Source phase211: `POWER_HYPERBOLIC_MODEL_GRAM.md`. There is no Phi(t)=C exp(-a cosh(2t)) prod_j cosh(alpha_j t) with C,a>0, alpha_j>0 and sum alpha_j² finite, finite or countable product. The rate forces a=2pi; log Q/t forces sum alpha_j=9/2. Infinitely many factors annihilate the normalized leading coefficient, incompatible with 2pi². For finitely many, the first theta correction requires alpha_min=1 and integer multiplicity k=pi-3/(2pi), between 2 and 3: impossible. Difference from §7/§10: exact temporal multiplication, without an ODE hypothesis nor sign preservation. Does not exclude real powers of cosh, quotients, sums, other approximations nor relative comparison; nor does it decide abstract preservation by cosh. Mathematical re-check passed, targeted dedup against the map; no computations, new real sign, extension of T nor changes in papers.


**Temporal kernel, §8.4 — cancelled exponential moment and Jacobi product (PROVED, explicit class).** Source phase211: `POWER_GRAM_SLICES_OBSTRUCTION.md`. For real nonzero continuous phi, with exponential decay on the left and superexponential on the right, integral exp(ct)phi=0 with c>0 excludes PSD of A_phi: the absolute LT identity would give (Z_phi²)' >=0 up to Z_phi(c)²=0, contradicting Laplace uniqueness. With joint holomorphy of A, §2.2 excludes PSD on any open interval. Application: phi_P=(D²-1/4)[exp(t/2)P(exp(-pi exp(2t)))]/4 for EVERY nonconstant real polynomial P; the moment c=1/2 vanishes while preserving the boundaries. Includes cutoffs J>=1 of the Jacobi product, with all their signed coefficients and crossings. Difference from previous positive cutoffs: does not require a sign of phi nor of the weights; uses exact cancellation of one moment. Does not pass to the infinite product / full Phi, whose moment is positive. Mathematical re-check passed, targeted cross-check against the map; classical identity cited DLMF 20.5.3, no world priority, no computations nor new W/T.


**Temporal kernel, §8.5 — symmetrized Jacobi, corollary of pairs 001 (PROVED).** Source phase211: `POWER_GRAM_SLICES_OBSTRUCTION.md`. For every J>=1, S_J=(phi_PJ+phi_PJ reflected)/2 has POSITIVE tail D_J exp(-beta|t|), beta=2J+1/2, D_J=(8^J J!pi^J)(beta²-1/4)/8. At nodes beta-epsilon, beta-2epsilon, epsilon K converges to [[2,3/2],[3/2,1]]/(2beta), with negative determinant. Absolute LT and the continuation of §2.2 exclude PSD of A_SJ on any interval. The pairs criterion is attributed to CONE 001, no general novelty; an application different from §8.4 (cancelled moment) and §8.3 (negative tail / negative diagonal). Does not claim S_J positive on the whole line nor refute Phi; other repairs and global OPEN. Independently re-checked, targeted dedup against the map; no computations nor new T.


**Temporal kernel, §2.3 — scope of the translational Hankel factorization (PROVED; classical antecedent).** `POWER_GRAM_SLICES_OBSTRUCTION.md`: A does not admit integral_0^infinity<h(t+r),h(s+r)>dr, even with h measurable with values in a Hilbert space and finite diagonal integrals. The difference under common translation would be PSD; its derivative forces (t+s)Phi(t)Phi(s) PSD, but its 2×2 minor is negative. Antecedent: Blower, https://eprints.lancs.ac.uk/id/eprint/615/1/integrablepaper.pdf, Thm 1.2 and §2.5 (2.14); no novelty attributed to the mechanism. Only those variables and that representation: does not refute PSD of A, other Grams, other coordinates nor the sum of Hankel products. Independent re-check passed, no new data nor sign/T.


**Temporal kernel, §8.6 — modal deformation n^(-delta), every delta different from 0 (PROVED).** Source phase211: `POWER_GRAM_SLICES_OBSTRUCTION.md`. For phi_delta=sum n^(-delta)Phi_n, the infinite sum and all its crossings are kept. Z_delta=C(u)(u-1/2)sum n^(-u-1/2-delta), absolutely for u>max(-5/2,1/2-delta). Delta>0: Z<0, Z'>0 just to the left of 1/2. Delta<0: as u decreases to c=1/2-delta from above, Z~D/(u-c), Z'~-D/(u-c)², D>0, by elementary sum–integral comparison. Absolute LT produces a negative test; joint holomorphy and §2.2 exclude PSD of A_delta on any interval. Difference from smooth cutoffs: covers arbitrarily weak dampings, previously only delta>3; neither parity nor a left Gaussian bound assumed. Delta=0 NOT covered: Z_Phi(1/2)=1/4, while Z_delta(1/2)=0 for all delta>0; L1 distance with weight exp(t/2) >=1/4 despite compact convergence. Independently re-checked, targeted dedup against the map. No negative sign of Phi/W, new T, computations nor changes in papers.


**Temporal kernel, §7.1 — Gaussian convolution, global equivalence via a remote node (PROVED).** Source phase211: `POWER_GRAM_SLICES_OBSTRUCTION.md`. If K(u,R),K(R,R)->0, then K+b PSD on all finite blocks is equivalent to K PSD for b>=0: adding the node R with coefficient minus the sum of the original ones removes the rank one and recovers any negative value as R->infinity. For Phi, Gaussian bounds for all N and convexity of log Z prove M(R)/R->0. Convolving with a Gaussian of variance sigma² adds exactly sigma² to K; thus an independent proof for ONE fixed sigma suffices. Normalizing the density by exp(-sigma²/8) keeps Z(1/2)=1/4 without changing K. Difference from §7: converse, not a new preservation; distinct from multiplying the density by exp(lambda t²). NO smoothed sign proved, NO fixed-size / bounded-rank equivalence, NO prohibition on using this reformulation constructively. Independently re-checked and cross-checked against the map; no new data nor W/T.

### 2026-11-05 — Logarithmic criterion: quartic falsifier of a general inference

`POWER_GRAM_SLICES_OBSTRUCTION.md` §4.1: PROVED, independently re-checked, dedup against the map. For phi=exp(-a t^4), a>0, A and all its layers are PSD (§4), but log A is not conditionally positive: the coefficient of t^5s^5 is (51/120)(4a)^5 kappa_5(V)<0 for V with density proportional to exp(-2av²); a fifth difference at six nodes gives a falsifier. Scope: PSD / positive layers do NOT imply infinite divisibility of the normalized kernel. Does not refute the real Phi. A single real block of five nodes did not give a numerical falsifier, without certificate nor extrapolation. The real logarithmic condition remains OPEN; no new W/T positivity. Difference from CND of layers: the logarithm of the full integral is studied. Papers untouched.

**CPD update, 2026-11-06 (same entry).** GRAM §4.1, PROVED; independent re-checks passed for both mechanisms. For z=x+iy, x>=0, the identity F²H=4D+L²+2xbL-Fb uses F=A(z,bar z)>0, b=|Phi(z)|², L=integral_x^infinity|Phi|² and D=(F/2)min_(a complex)integral_x^infinity v|Phi'-aPhi|²>=0. At x=0, LARGE gives L>=c epsilon^-4, the global bound F<=C epsilon^-5 and SMALL b<=C epsilon^-N exp(-a/epsilon): H>0 eventually. At x=h=log2/2, full Poisson up to 3 derivatives gives the C1 profile f=(1+2iu)^(-5/2), u∈[0,1], with min_beta integral|f'-beta f|²>=1/9375; the local restriction of the minimum pays Fb and proves H>0 eventually without approximating F total. Targeted corpus/literature cross-check located no literal antecedent. Only those two complex diagonal tests pass; CPD and global sign OPEN. No numerical threshold, local asymptotics 7/16 of the full H, new route, W/T coverage, computations nor papers edited.

**Scope of the joint CPD extension (same entry).** GRAM §4.1, PROVED, independent re-checks passed; targeted corpus/literature cross-check located no literal antecedent. Fixing z0, I, a positive weight, for f_eta(u)=Phi(z0+eta+u) and P_eta the projection onto span{f0,f_eta}, R_ij=<(I-P_eta)f_i',(I-P_eta)f_j'> does not dominate c bb* with c>0 uniform in eta, b_i=f_i(0): R_00<=||f0'-(f_eta-f0)/eta||²=O(|eta|²), but |b0|²>0 fixed. eta=i tau keeps the real parts; uniform C2 remainder, without requiring independence. Only that residual/boundary and uniformity: does not exclude c(eta), renormalizations by separation, other terms/boundaries/projections nor general Gram. S=A^(odot2) odot H PSD does not imply H PSD. CPD/global OPEN; no new route, W/T, computations nor papers.

**Horizontal average, CPD scope (same entry).** GRAM §4.1, PROVED, independent re-checks passed; targeted corpus/literature cross-check located no literal antecedent. For B_y=integral_2^4[logt/(2t)]|Phi(.5logt+iy)|²dt and epsilon=cos2y, epsilon^(9/2)B_y->315(log2)²/(512sqrt2). Modal diagonal by uniform Gaussian Riemann sums; COMPLETE crossings by IBP <=Cepsilon^-4(1+log1/epsilon), lower term and cross o(epsilon^-9/2). Then A(iy,-iy)>=c epsilon^-9/2. The segment [h,h+c0epsilon], h=.5log2, c0 fixed, contributes O(epsilon^-4), proportion O(sqrt epsilon)->0. Equivalent ONLY for B_y; not for the total A nor H, nor arbitrary bands. No new matrix positivity, CPD, W/T nor route; global sign OPEN, no computations/papers.

### 2026-11-05 — Complete theta: failure of temporal log-supermodularity

`POWER_GRAM_SLICES_OBSTRUCTION.md` §4.2, PROVED, independently re-checked, cross-checked against the map. For the COMPLETE temporal A and s in any positive compact set, H=partial_t partial_s log A=-1/(t+s)²+O(exp(-2t))<0 as t grows. Proof via v=pi exp(2t)(exp(2r)-1), expansion with differentiated remainders up to order 2 and complete theta tail. Thus A is not globally TP2; the route cannot be closed by pointwise positivity of H nor by all-nonnegative features of H. Difference from §5: full integral, not layers; the TP2 of 073/112 belongs to other objects. Restricted scope: does NOT refute PSD of H, CPD of log A nor PSD of A; negative rectangular minors are not principal minors. No new W/T sign, papers untouched.

### 2026-11-05 — Main tail models indefinite on every interval

`POWER_GRAM_SLICES_OBSTRUCTION.md` §4.3, PROVED; independent re-checks passed; deduplicated against the map. G0=(t+s)/(exp(2t)+exp(2s)) and H0=sech²(t−s)−1/(t+s)² are not PSD at ALL sizes on any positive interval, including arbitrarily distant tails. Corollary of analytic continuation §2.2: G0 reaches a negative diagonal at t<0; H0 reaches H0(1/4,1/4)=-3. The full theta expansion at t=L+x, s=L+y approximates both models with entrywise error O(exp(-2L)), including C² control for log A, but does not transfer their indefiniteness to the real kernel. Using them as a PSD reference or through a symmetric multiplicative sandwich is ruled out. The real A/H and other compensations are not refuted; no new W/T, papers untouched.

### 2026-11-05 — Relative closeness of densities does not preserve positivity

`POWER_GRAM_SLICES_OBSTRUCTION.md` §8.7, PROVED; independent re-checks passed; checked against the map. For every epsilon>0 one constructs a positive, even psi, holomorphic in the same strip as Phi, with sup|psi/Phi-1|<epsilon and psi/Phi→1 in both tails, whose A is not PSD on any interval. A smooth repair that agrees with Phi_M in the tail inherits its negative block; mollifying the RELATIVE ERROR by a Gaussian yields analyticity and preserves that block by continuity. The modal ratio gives epsilon_M<=4(M+1)^4 exp[-pi((M+1)²-1)]. Relative exponential expansions of every fixed order are preserved, not exact moments nor arithmetic transseries. Difference from 8.2/8.3: positivity/parity/analyticity and uniform relative error simultaneously. It is not a counterexample to A_Phi; it neither guarantees nor excludes control in form norm or strong analytic norms. No new W/T, numerical data or changes to papers.

### 2026-11-05 — Negative analytic approximants with exact finite moments

`POWER_GRAM_SLICES_OBSTRUCTION.md` §8.8, PROVED; independent re-checks passed; checked against the map. The construction 8.7 admits any FINITE family of independent continuous even weights on (-1,1), integrable against Phi: correct the moments with compact relative bumps before mollifying and solve the small residual with the same mollified bumps. Positivity/parity/analyticity, arbitrarily small relative error and tails persist, as does the fixed negative block. For weights cosh(u_i t), t sinh(u_i t), it preserves EXACTLY any finite collection of real K blocks. Conclusion 8.8 by itself does not guarantee the infinite families of 2/3/4 generators; see 8.9 for up to 4. It does not preserve the full arithmetic structure nor refute Phi. Difference from 018/8.7: a nearby regular real density and exact finite data simultaneously. No new W/T and no papers edited.

### 2026-11-05 — All four generators can coexist with global failure in approximants

`POWER_GRAM_SLICES_OBSTRUCTION.md` §8.9, PROVED; independent re-checks passed; deduplicated against the map. There exists delta_*>0 for which ||psi/Phi-1||_20<delta_* keeps K_psi PD on ALL blocks of <=4 distinct nodes u>1/2. The bound Delta M^(k)=O(delta u^-8(1+log u)^4), k<=3, preserves the strict numerators 084/085; T>0 and the tails recover growth/concavity and the signs 083 without assuming BASE073 for psi. The approximants 8.8 enter that norm without losing their negative block, analyticity, parity, tails and exact finite moments. Difference from 8.8: the complete CONTINUOUS family of order 4, not concrete blocks; it controls confluences and escape through scalar criteria. It does not preserve the theta arithmetic identity; the extension to all 13 of 053 is treated in 8.10. It does NOT refute Phi nor give a new W/T. No computations, no papers edited.

### 2026-11-05 — Relative control via Cayley/Newton and stability of thirteen arbitrary rates

`POWER_GRAM_SLICES_OBSTRUCTION.md` §8.10, PROVED; independent re-checks passed; targeted deduplication against the map. In the space of exponentials times polynomials of dimension <=13, A=-D is accretive and Q=(A-a)/(A+a) contractive. Newton/Hermite interpolation of F(z)=Delta M(a(1+z)/(1-z)) gives a bound on Delta K RELATIVE to the Cauchy Gram, uniform under collisions/escape, without assuming Delta M globally holomorphic. Relative density error in norm 100 controls C12 of F. The margin 053 of 1/4000 keeps 1/8000 for psi sufficiently close, all 13 poles >=63/2, including multiple poles. The approximants 8.8 can preserve this, ALL 4 admissible ones and exact finite data, while keeping global failure on a block of more than 13 high nodes. It does not preserve the theta arithmetic nor all dimensions; it does NOT refute Phi nor extend W/T. No numerical data/papers.

### 2026-11-06 — Impossibility of a Cauchy margin uniform in dimension

`POWER_GRAM_SLICES_OBSTRUCTION.md` §8.11, PROVED; independent re-checks passed; checked against the map. For M real analytic, positive-variable, with M(u)=O(u) at 0, no K_M-c/(u+v), c>0, is PSD at all orders on any open positive interval. Analytic continuation by jets down to a small point contradicts the diagonal M(u)/u-c/(2u). It applies to the REAL Phi and to the hyperbolic model, without assuming or refuting K_M PSD. It prevents extending the margin 053 or 8.10 to all orders through a fixed positive constant, even at high rates. It does not exclude nonnegativity without margin, different relative comparisons, or a global proof. No new calculations, no papers edited.


### Phase 211 — grouped divisorial covariance (2026-11-06)

PROVED/re-checked independently; targeted cross-check against the map: `POWER_GLOBAL_ROUTE_REVIEW.md`, section «Covarianza divisorial agrupada». For C_s(n)=sum_(dm=n)mu(d)log(m)(gcd(d,m)^s-1), s>0, C_s(p²)=-(p^s-1)log p<0, while C_s(p²q²)=(q^s-1)(p^s-2)log p+(p^s-1)(q^s-2)log q>0 if p^s,q^s>2 (s=1/2: p=5, q=7). All cancellation per product n is retained. Antecedent of the factor: 209 CONSTRUCTOR005; distinct disintegration: 106/114. FALSIFIED only the uniform sign of the coefficients of the mixed remainder, NOT the sign of the form nor joint compensation with ARCH. No new W/T or changes to papers.


### Phase 211 — indefinite divisorial remainder on the primitive carrier (2026-11-06)

PROVED/re-checked independently, deduplicated against the map; `POWER_GLOBAL_ROUTE_REVIEW.md`, «El resto divisorial es indefinido». The coefficient result is strengthened: R(F)=sum n^(-1/2)C_(1/2)(n)Re c_F(log n) takes both signs on real even C_c^infinity tests with both polar moments zero, in one and the same window T=3log4+1/100000. Bump trains spaced log4, coefficients (1,-5/2,1) and (1,-3/2,-1/2,-1/2,-1/2,-3/2,1), give respectively R/(kappa||g||²)=7/4 and -1/4, kappa=(sqrt2-1)log2. All contacts are handled by exact isolation; no sweep. FALSIFIED only universal R>=0 or R<=0 as an isolated piece; joint compensation with ARCH/means and the sign of W remain OPEN. No new W/T or changes to papers.


### Phase 211 — fitted Robin comparator, two-node falsifier (2026-11-06)

PROVED/re-checked independently, checked against the map; `POWER_GLOBAL_ROUTE_REVIEW.md`, «Comparador Robin ajustado». Positive model M_*=wb M_R(bu), w=7/2, b=2/7, a=4pi/7, beta=4pi²/49-33/392, agrees with M_Phi up to u^-2 but D=M_Phi-M_*=d/u³+O(u^-7/2), d>0. The remainder K_D at nodes u,2u has det=-5d²/(64u⁸)+O(u^-17/2)<0 for large u. FALSIFIED only that additive PSD comparison; neither individual kernel is refuted. Pair corollary: D=o(1/u) and K_D PSD on a ray force D=0; do not search for a non-identical positive comparator that also cancels 1/u. Diagnostic of NUMERICAL origin not used in the proof. No new W/T or changes to papers.


### Phase 211 — asinh comparator, certified negative minor (2026-11-06)

PROVED/computer-assisted; independent re-checks passed, including a separate check of tails and jets; deduplicated against the map. `POWER_GLOBAL_ROUTE_REVIEW.md`, «Comparador asinh» and `tools/power_asinh_comparison_jet_verify.py`: M_0=.5asinh(u/(4pi)) has a PSD kernel by a positive integral of resolvents, but the residual N_D=(M_Phi-M_0)/u has a jet minor {5,6}, [[n10,n11],[n11,n12]], with det between -1.684e-57 and -1.683e-57. Arb256, 14 moments up to 26, 16 modes [0,3], total tails <2^-645 covered by 2^-500; an independent rerun reproduced exit 0. Only one prescribed minor, no sweep. FALSIFIED additive PSD comparison, NOT K_Phi nor general signed comparison; jets are not equivalent to just two exponents. Positive diagonals were not enough. No new W/T or changes to papers.


### Phase 211 — original hyperbolic comparison refuted (2026-11-06)

PROVED/computer-assisted; independent re-checks passed; deduplicated against the map. `POWER_GLOBAL_ROUTE_REVIEW.md`, «Comparación hiperbólica original»; `tools/power_hyperbolic_comparison_jet_verify.py`. The exact comparison K_Phi-K_(2pi) PSD, previously OPEN, is closed as FALSIFIED. The residual jet minor {5,6} has det between -3.307e-59 and -3.306e-59, with 28 complete half-moments up to 26, Arb256 and tails 2^-500 per moment; an independent rerun reproduced exit 0. The asinh certificate is not transferred and other blocks are not explored. The hyperbolic model remains PSD; K_Phi is not refuted. Other scales, reweightings and signed compensations undecided. No new W/T or changes to papers.


### Phase 211 — reciprocal HCM does not imply the sign of the kernel (2026-11-06)

PROVED; independent re-checks passed (including exact theta); deduplicated against the map; `POWER_GLOBAL_ROUTE_REVIEW.md`, «HCM, reciprocidad y supercolas». f_epsilon(x)=C(1+x)^(-2)exp[-epsilon(x+x^-1)], epsilon=2^-100, is HCM by explicit product, reciprocal, and has all Mellin moments. The law of log X is even/real-analytic with supertails; its fourth cumulant is >0 by rational bounds with cutoff 32. Then det K(h,2h)=−kappa2·kappa4·h²/6+O(h⁴)<0. FALSIFIED only the inference from those hypotheses; not Phi, not general BPY, not the property V'''>0 nor the GGC label. The pair criterion is known; the new class of the falsifier was cross-checked against 003/074/101 and L93. No new W/T or changes to papers.


### Phase 211 — HCM of the real theta density refuted (2026-11-06)

PROVED; independent re-checks passed; checked against the map; `POWER_GLOBAL_ROUTE_REVIEW.md`, «La densidad theta en S=exp(2t) no es HCM». For f(x)=Phi(.5log x)/(2xZ0), parity gives f(1/x)=x²f(x). The HCM product with a=1 has H(w)~(pi⁴/Z0²)w^(9/2)e^-2piw, w=v+1/v. CM would require log-convexity; g=log H+2piw would be convex, sublinear and tending to +infinity, impossible. No remainders are derived. FALSIFIED HCM of this real density and its positive tilts/scalings; not GGC nor K_Phi nor other power changes. The already known rate/prefactor mechanism is applied to an object different from the mixtures §7.1; do not claim a new principle. No new W/T or changes to papers.


### Phase 211 — the two comparators also fail on the primitive subspace (2026-11-06)

PROVED; independent re-checks passed, including a separate mathematical check and a literal check; `POWER_GLOBAL_ROUTE_REVIEW.md`, «Comparaciones primitivas: transferencia analítica del descarte». Exact constraints sum d/(u-.5)=sum d/(u+.5)=0. For D odd and globally real-analytic, L=(u²-.25)(v²-.25)K_D turns those constraints into vanishing moments 0,1. Projection against two anchors + continuation from GRAM_SLICES §2.2 propagate conditional positivity from any open interval; the null rows at ±.5 allow completing the moments at no energy cost and force full PSD. The previous asinh/hyperbolic certificates thus also exclude both uniform PRIMITIVE comparisons. Difference: a codim-2 domain previously not decided by the full vectors; not a new continuation principle. Existential negative primitive test, without coefficients or window; these are not automatically the original jets. No negativity of K_Phi, no equivalence of minima at fixed T, no new W/T, no papers edited.


### Phase 211 — closure of cosh products at fixed hyperbolic scale (2026-11-06)

PROVED; independent re-checks passed, including a separate independent check; targeted cross-check against the map; `POWER_HYPERBOLIC_MODEL_GRAM.md` §11.4. Phi cannot be approximated locally uniformly by C_n exp(-2pi cosh(2t)) times finite products of cosh(alpha_nj t), alpha_nj>0, even varying number and parameters. Lemma: every normalized positive limit of such products is exp(gamma t²)prod cosh(alpha_j t), gamma>=0, sum alpha_j² finite; log Q_n(1) bounds the quadratic mass and Taylor controls the remainder uniformly. For the theta quotient, log Q(t)/t→9/2 forces gamma=0 and contradicts exact §11. Difference: a class of approximations not previously covered is closed, not a mere repetition of the exclusion of an exact representation. Only fixed scale 2pi, positive unit factors and uniform convergence on compacts; not variable scales, real powers, other topologies nor relative comparison. No computations, new real sign, extension of T or changes to papers.


### Phase 211 — finite matrix closure without first derivative excluded (2026-11-06)

PROVED; independent re-checks passed, including a separate independent check; `POWER_HYPERBOLIC_MODEL_GRAM.md` §12. For a finite vector of fixed prefactors Q, even, C², of exponential growth, with Q1=q_theta, one cannot have Y_rr=(b²+nu²)Y+E(b)Y at two distinct scales with E independent of nu. FORCE and uniqueness force sinh(v)Q'=BQ constant; w=log tanh(v/2) gives Q_w=BQ and a finite limit of all components at infinity, incompatible with q_theta~2pi²e^(9v/4). Difference from §10: arbitrary finite dimension and matrix potential, not only scalar. Only this class WITHOUT A(b)Y_r nor b-dependent prefactors; no exclusion of general, infinite or other Green systems. No computations, new W/T or changes to papers.


### Phase 211 — finite matrix closure with first derivative excluded (2026-11-06)

PROVED; independent re-checks passed, including a literal check; targeted cross-check against the map; `POWER_HYPERBOLIC_MODEL_GRAM.md` §12.1. No earlier literal antecedent was located; E101_070 §5 only excluded automatic finite-band closure, not this system with arbitrary matrices. In the family of fixed prefactors Q containing q_theta, one also cannot have Y_rr=(b²+nu²)Y+A(b)Y_r+E(b)Y at two distinct scales, with matrices independent of nu and finite dimension. FORCE and uniqueness force Qtilde_x=R(x)Qtilde rational, x=exp(v). Row dependence forces a scalar rational annihilator of q_theta(log x); conjugation by pi*x^(5/4)*exp(pi/x) carries it to g=sum n²(2pi n²x-3)exp[-pi(n²-1)x]. Separating the exponential rates successively proves that each modal polynomial of the annihilator vanishes; its leading coefficient requires a nonzero polynomial annihilated at infinitely many distinct rates, contradiction. Difference from §12: it now allows A(b)Y_r. Only fixed prefactors, finite dimension and identity coefficient of nu²; not general systems, b-dependent prefactors, infinite dimension nor other representations. No computations, new W/T positivity or changes to papers.


### Phase 211 — normalization by Phi does not give a positive translational generator (2026-11-06)

PROVED; independent re-checks passed; targeted cross-check against the map; `POWER_GLOBAL_ROUTE_REVIEW.md`, «Normalizar por Phi». For B=A/(Phi(t)Phi(s)), p=-Phi'/Phi, C=−(partial_t+partial_s)B=t+s−(p(t)+p(s))B. C00=0, but partial_s C00=1−aB00>0, a=p'(0): if a<=0 it is immediate; if a>0, 073 gives Phi(r)²/Phi0²<exp(-ar²) and B00<1/a. A negative minor {0,s} and continuity give positive nodes; analytic continuation excludes PSD on any open interval. Distinct from the hazard §7 and from the gauge-free generator §2.3. Only this sufficient condition fails; not B/A/KPhi, other normalizations nor global sign. No computations, new W/T, no papers edited.


**Parity extension of the normalized generator (2026-11-06).** In «Normalizar por Phi» of GLOBAL_ROUTE_REVIEW, corollary independently re-checked and checked against the map: no positive, even, real-analytic g makes C_g=−Dcommon[A/(gg)] locally PSD. Joint parity makes C_g odd; PSD continuation forces zero diagonals and C_g=0, i.e. stationarity A/(gg)=F(t-s). The diagonal H(L,L)=1−1/(4L²)+O(e^-2L) of GRAM §4.3 is not constant and excludes that exception. Includes the repair that kills row 0 by choosing g'/g=−sPhi0Phi(s)/A(0,s). Only a corollary of parity, continuation and the earlier scalar asymptotics; no new computations nor matrix extrapolation. Does not cover non-even gauges nor other mechanisms; no new W/T, no papers edited.


### Phase 211 — tilted generator C1, initial diagnostic (2026-11-06)

**Update:** FALSIFIED for every finite c by the modular cusp argument recorded below. The following paragraph preserves the historical state of the diagnostic.

`POWER_GLOBAL_ROUTE_REVIEW.md`, «Generador con inclinación exponencial». Targeted cross-check against the map with no literal antecedent located. g_c=Phi exp(ct) avoids parity; C_c=C0+2cB, B=A/(PhiPhi), and B=integral exp(-2cr)C_c translated for c>=1: PSD of C_c would be sufficient. Independent re-check: the negative tail requires c>=1. At c=1 its principal part is the Cauchy Gram 1/[pi(e2t+e2s)], with no relative control of the remainder. Single jet {0,1} evaluated at 50/80 dps, theta 16/[0,3]: determinant ≈+0.00788625227439, NUMERICAL only, without enclosure. No other blocks/sweep. Initial historical state: C1 PSD at all orders OPEN. Current state: **FALSIFIED for every finite c**, including c=1, by «Cúspides modulares» in the same source and the later ruling-out entry; do not retry from this positive diagnostic. No new W/T positivity. Real difference: non-even normalization, outside the earlier ruling-out; no sufficiency inferred from the diagnostic.


### Phase 211 — modular cusps refute every C_c with finite c (2026-11-06)

PROVED; independent re-checks passed; targeted cross-check against the map; `POWER_GLOBAL_ROUTE_REVIEW.md`, «Cúspides modulares». C_c PSD and reflection would require B<=exp(2ch)B translated. Congruence removes denominators and produces H_h real PSD, holomorphic on strip²; its jets would require H_h(iy,-iy)>=0. For h=.5log2, y→pi/4, epsilon=cos2y, alternating Poisson at w→i gives |Phi(iy)|<=C epsilon^-9/2 exp[-pi/(8epsilon)], while the even cusp w→2i gives |Phi(h+iy)|>=kappa epsilon^-5/2, uniformly also on a segment of length epsilon. Positive horizontal integrals give A0>=kappa epsilon^-4 and Ah<=C epsilon^-5. Thus H<=C_c epsilon^-14 exp[-pi/(4epsilon)]−kappa epsilon^-9<0 for every finite c. C1, previously OPEN, becomes FALSIFIED; its positive numerical jet did not imply a global sign. Full theta series, no computations nor arguments via zeros. Only excludes this family of generators and its translational comparison, not A/B/KPhi nor other Grams. No new W/T positivity, no papers edited.


### Phase 211 — generator with full diagonal normalization refuted (2026-11-06)

PROVED; independent mathematical re-check PASS; targeted deduplication cross-check. Source `03-research/phase-211-sign-sandbox/POWER_GLOBAL_ROUTE_REVIEW.md`, «Normalización por la diagonal completa». For d(t)=A(t,t), R=A/sqrt(d(t)d(s)), no C_c=2cR-DcommonR is PSD of all sizes on an open real interval, for any finite real c. It changes the gauge to sqrt(d)exp(ct), not automatically covered by the ruling-out of Phi exp(ct). For c>0, reflection and sum give R PSD and translational comparison; the Schur product of the difference and the sum, followed by congruence, gives a hypothetical PSD H=exp(4ch)A_h²d(t)d(s)-A²d_h(t)d_h(s), holomorphic without roots. The identity d'(z)=-2zPhi(z)² and Poisson prove d(iy) bounded and d(h+iy)~-(9/16)(h+i*pi/4)(2i)^(3/2)zeta^(-4), zeta=exp(2z)-2i, h=log2/2. With the earlier complete bounds A0>=kappa*epsilon^(-4), Ah<=C*epsilon^(-5), one gets H(iy,-iy)<=C_c*epsilon^(-10)-kappa*epsilon^(-16)<0, contradicting PSD jets. c<0 fails on the diagonal; c=0 would force R stationary and H=0, same contradiction. Antecedents: modular ruling-out of the Phi gauge, parity without tilt, and normalized CPD; new difference: squared and primitive comparison of the diagonal. A/R/K_Phi and other gauges are not refuted; existential negative real test, without explicit nodes. No numerics, new window T or changes to papers.


**Corollary of the diagonal-normalization ruling-out (2026-11-06).** GLOBAL_ROUTE_REVIEW, final corollary: PROVED; independent re-check PASS. Also excluded is g_c=sqrt(A(t,t))*exp(ct)/F(t), F(t)=exp(t/2)theta(exp(2t)), for every finite real c. The INVERSE translational comparison and its Schur product require PSD of J=exp(4ch)A²F(t)²F(s)²d_h(t)d_h(s)-A_h²F_h(t)²F_h(s)²d(t)d(s). Alternating/even Poisson and the same complete bounds give J(iy,-iy)<=C_c*epsilon^(-20)*exp(-b/epsilon)-kappa*epsilon^(-10)<0. c<=0 is handled by reflected diagonals/parity. Dividing by F inverts which comparison fails; it is a corollary of the mechanism, not a new general impossibility class. Only that gauge, not A/K_Phi, other gauges nor global sign. Targeted cross-check without literal antecedent; no computations or changes to papers.


### Phase 211 — asymmetric theta-scale gauge: negative real minor (2026-11-06)

PROVED; independent re-check PASS; targeted deduplication cross-check. Source GLOBAL_ROUTE_REVIEW, «Gauge asimétrico de escala theta». g(t)=exp(2pi sinh(2t)), q=4pi cosh(2t), changes the class relative to the even gauge with constant tilt. The congruent generator C=(q(t)+q(s))A+(t+s)Phi(t)Phi(s) fails at temporal nodes (-L,L) for large L. Y=pi exp(2L), P=Phi(L): the full diagonal expansion gives C--/P²=O(L/Y), C++/P²=4L+O(L/Y), while restricting A(-L,L) to 0<=r<=Y^-1/2 gives Aop>=kappa P²/Y and C-+>=4kappa P². Thus det/P⁴<=O(L²/Y)-16kappa²<0. Needs neither the tail of the integral, cusps nor computations. Antecedents: GRAM §4.3 and opposite-node formulas, not this gauge; no literal duplicate found. Only this candidate, not all asymmetric gauges, A or W. The two nodes are not two powers. No extension of T, no papers modified.


**Extension of the asymmetric gauge to all parameters (2026-11-06).** PROVED; independent re-check PASS; targeted deduplication cross-check; source GLOBAL_ROUTE_REVIEW, final extension. No g_a(t)=exp(a sinh(2t)), a finite real, makes the generator PSD. For z=-h+iy, h=log2/2, epsilon=cos2y, the congruent generator satisfies C_a(z,barz)=4a cosh(2h)epsilon Ah-2h|Phi(h+iy)|². If a>0, the earlier complete bounds give <=C_a'*epsilon^(-4)-kappa*epsilon^(-5)<0, against PSD jets; a<=0 already fails on real diagonals. Extends the 2pi case without sweeping parameters, through a DIRECT complex test of the generator. Only existence of a finite real test for general a, not two explicit nodes. Application of earlier cusp tools, not a new positivity method nor a no-go for all gauges. Does not refute A/K_Phi; no computations, extension of T or changes to papers.


### Phase 211 — all temporal pairs and v-layer pairs are positive (2026-11-06)

PROVED; independent re-check PASS; targeted deduplication cross-check with no literal antecedent located. Source POWER_GRAM_SLICES_OBSTRUCTION §9. From 073 V'''(x)>0 and parity one gets xV''-V'=integral_0^x rV'''(r)dr>0, hence G(u)=V(sqrt u) is strictly convex. In SLICE, a=sqrt(m²+v)+delta, b=sqrt(m²+v)-delta have a²+b²=t²+s²+2v and strictly larger dispersion than (t²+v,s²+v) if v>0, t!=s. Convexity gives S_v(t,s)²<S_v(t,t)S_v(s,s): all blocks of two distinct real nodes are SPD for v>0, and so are those of A after integrating. v=0 is rank one. With §5, three is the minimal size of a falsifier of a real v-layer; it does NOT imply failure of A at three. Difference: TEMPORAL pairs via convexity in squares, not power pairs 073 nor TP2 of 112. Classical convex principle; new consequence within the cross-checked corpus, not a world priority claim. No new W/T coverage, computations or papers modified; global OPEN.


### Phase 211 — compensation between layers proved on symmetric triples (2026-11-06)

PROVED; independent mathematical re-check; targeted deduplication cross-check. Source POWER_GRAM_SLICES_OBSTRUCTION §10. Refinement of the same result: A on (-R,0,R) is SPD for EVERY R>=8. The antisymmetric sector has d-b>0 by §9; the symmetric one has determinant d0(d+b)-2c²>0 by explicit bounds. With Y=pi exp(2R), P=Phi(R), B=sup Phi=Phi0<450/499<1 (all modes), p(x)>=pi exp(2x) for x>=1 gives c<=BP(R/Y+2/Y²); integrating up to r=1/(4Y), using p(R+r)<3Y, gives d>RP²/(4Y). Moreover d0>81/2^24 since Phi>9/256 on [0,1/16]. For R>=8, 2c²/d<9B²R/Y<=9R/Y<24/7^8<81/2^24<d0. At THE SAME nodes, for EVERY R>=8, the small layers are negative on w=(1/P,-2/Phi0,1/P): for B_v=S_v/(PhiPhi), eta=(1,-2,1), eta^T B_v eta=-v Q_R+o(v)<0, since Q_R=2p'(R)-6p(R)/R+4p'(0)>(8-12/R)Y-2-6/R+4p'(0)>0. The interval 0<v<v_R depends on R. The full integral over that vector is positive, so the later contribution strictly compensates the initial loss. Difference: a proved realization of compensation for the REAL theta, as opposed to a mere abstract possibility or the layer falsifier §5; R>=8 makes both signs explicit, without uniformity of v_R nor a new route. No uniform v-interval; not power triples 080, intermediate R, all sizes, induction, global sign nor extension of W/T. No computations, no papers modified.


### Phase 211 — paired Andréief: negative integrand of order three (2026-11-06)

PROVED; independent re-check PASS; targeted deduplication cross-check. Source POWER_GRAM_SLICES_OBSTRUCTION §11. For f_i(r)=Phi(t_i+r), g_i(r)=(t_i+r)Phi(t_i+r), det A3=(1/6)integral S, S a sum of eight products det[u_ej(rj)]det[u_(1-ej)(rj)]. At (r,r,r+h), the FULL sum is -4det[g,f,f_h]det[g,f,g_h]. Taylor gives principal parts hC p[x1,x2,x3] and hC(xp)[x1,x2,x3], C>0; p'' and (xp)'' are positive on the full theta tail. Thus S<0 for small h and, by continuity with r>0, on an open region of r1<r2<r3. Difference from raw layers: all choices of the determinant have already been paired; sources 086/089/099–112 use other objects. Only the pointwise sign of this standard integrand is ruled out; NOT det A<0, not other pairings nor integrated compensation. No new W/T, computations or papers modified.


### Phase 211 — closure of the reciprocal criterion and small temporal triples (2026-11-06)

PROVED with interval certificate; independent mathematical re-check PASS and targeted deduplication cross-check with no earlier proof of the closure located. Source POWER_GRAM_SLICES_OBSTRUCTION §12 and tools/power_temporal_reciprocal_compact_verify.py. Origin u=r² in [0,1/64]: a>0, a''<0 on 256 cells; remainder r in [1/8,1]: T=N Phi³>0 on 8192 cells, Taylor 24/cap 28, Arb512, 16 modes plus full tail. Cauchy gives remainder <1e-30; certified minimum T>1.04e-17. Two independent full runs PASS, SHA256 498e199ae7bb52f7fedeef02847a1b8642a635b76bb036212259bc2f875e93fa. Together with the tail r>=1 and 073, q(u)=r/V'(r) is strictly convex globally and a>0. The identity (HK-J²)/H²=Var(a+ua')+E[u²(2a'²-aa'')] proves HK>J². The checked expansion D/d0=R^4(K-J²/H)+O(R⁶) and the pairs §9 give A on (-R,0,R) SPD for every sufficiently small R>0. Difference: the pending compact piece of §12 is closed; not a new criterion. Not to be confused with M=Z'/Z of 086, power triples 080 nor large-R triples §10. No explicit small threshold; intermediate R and all orders OPEN, no extension of W/T, no papers modified.

Scope clarification (§12.3): the falsifier 074 has q''<0 on 0<u<=1, so it does not refute sufficiency of the new hypothesis. The family V=r²/2+r⁴/4+epsilon*r⁶/6, 0<epsilon<=1, does satisfy q convex but has negative layers by §5; its integral A is not decided. No extension to arbitrary R was obtained.


### Phase 211 — global limit of the new reciprocal convexity (2026-11-06)

PROVED, source POWER_GRAM_SLICES_OBSTRUCTION §13; independently re-checked, including a separate stability check. §8.7 is strengthened: h_M of the relative cutoff tends to 0 in weighted C6 because the modal jets have polynomial bounds times exp[-(n²-1)pi e/2]; mollification preserves the smallness. The new condition §12 a>0, q''>0 is open under small even C6 perturbations: at the origin |delta a|<=delta, |delta a'|<=delta/6, |delta a''|<=delta/60; tail N>2r²Y² and error <=1290 delta r²Y. V'''>0 is also preserved. Choosing M first and sigma afterwards preserves the negative block of §8.7. There thus exist positive even analytic densities close to Phi with the new GLOBAL convexity and HK>J², but A not PSD at some unspecified size. FALSIFIED only sufficiency of those generic hypotheses; NOT a negative sign for Phi, NOT refuted Schur inheritance in Theta, NOT global closure nor new W/T. No computations, no papers modified.


### Phase 211 — regularized theta primitive: explicit negative temporal minor (2026-11-06)

PROVED; independent re-check PASS; targeted cross-check with no literal temporal antecedent located. Source POWER_GLOBAL_ROUTE_REVIEW, «La primitiva regularizada tampoco es un núcleo temporal PSD». For U=2cosh(t/2)-exp(t/2)theta(exp2t)=2g, modal monotonicity and exp3>16 give (4/5)exp(-t/2)<U(t)<exp(-t/2) for t>=0. Then A_U(8,8)<18exp(-8), A_U(0,0)<2 and A_U(8,0)>(32/5)exp(-4); minor (0,8)<-(124/25)exp(-8)<0. Difference: decides the lack of PSD of the auxiliary source itself, not only the indefiniteness of the correction K_g-K_Phi already recorded. Does not refute A_Phi nor exclude further compensation; no new W/T, computations or changes to papers.


### Phase 211 — temporal reciprocal: no positive Laplace representation (2026-11-06)

PROVED; independent re-check passed; targeted deduplication cross-check with no literal antecedent located. Source POWER_GRAM_SLICES_OBSTRUCTION §14. q(u)=sqrt u/V'(sqrt u) does not extend holomorphically to all of Re u>0, hence is not integral exp(-us)dmu(s) with mu>=0. If Q extended, Q(z²)Phi'+zPhi=0 on x>|y|, |y|<pi/4. At w=i(16+2/m)+delta, m odd, Poisson and |Gauss_m|²=m give Phi~C delta^(-5/2), Phi'/Phi~−5w0/delta. Thus Q(z_m²)=0 at distinct points accumulating at (log4+i pi/4)², interior to Re u>0: analytic uniqueness contradicts q>0. No uniformity in m nor interior division by Phi'. The first 39 available derivative orders and order 0 have favorable alternating signs, but do not prove a representation. Not to be confused q with the reciprocal M 086 nor parametric CM 111; does not refute convexity §12 nor the sign of A_Phi. No new W/T nor changes to papers.


### Phase 211 — elementary falsifier of symmetric triples under convex G (2026-11-06)

PROVED, source POWER_GRAM_SLICES_OBSTRUCTION §15; independent re-checks PASS; targeted cross-check with no literal temporal antecedent. phi=exp(-r²/2-epsilon*r⁶/6), epsilon=1/1000 has G'>0, G''>0 for u>0 and V'''>0 for r>0. With w=exp(-u-epsilon*u³/3), Z=int w, a=1+epsilon*u², identity §12 gives Delta=(HK-J²)/H²=-2epsilon Eu²+epsilon²(15Eu⁴-9(Eu²)²). Exp(-x)>=1-x proves I2>=49/25, I4<=24 and Delta<=-89/(25000Z)<0. By the expansion D(R)=2(HK-J²)R⁴+O(R⁶), the block (-R,0,R) is indefinite for small R, even though all pairs are SPD. q''(0)=-2epsilon: it does not satisfy the theta property §12. Not to be confused with power K 074/080/101; does not refute Phi nor the target sign. No numerical data, new W/T or papers modified.


### Phase 211 — arithmetic principal part of the full A at fixed integer scales (2026-11-06)

**Additional scope §16.5, same entry (PROVED).** Independent re-checks PASS; targeted cross-check with no literal antecedent located. Fix FIRST y∈(0,pi/4) and AFTERWARDS k->infinity, l=k+1. Full theta tail uniform in r>=0 and Laplace at the endpoint give Akl/(Phi_k conjugate(Phi_l))=(x_k+x_l)/[2pi(epsilon(k+l)+i sigma(k-l))](1+O_y(1/k)); hence |C_y(k,k+1)|->1 for C_y normalized by the diagonal. Since rho(k,k+1)=0, the rho block is I2 and eigenmin C_y=1-|corr|->0. There is no c_y>0 with C_y>=c_y rho uniformly on integer blocks, even with c_y depending on y; nor a uniform o(1) approximation to rho (sup error >=1 for each y). Only this comparator/normalization; not A negative nor other weights/models. No joint epsilon,k regime, new route, W/T, computations or papers; global sign OPEN.

Sources: [GRAM §16 and band §4.1](../../03-research/phase-211-sign-sandbox/POWER_GRAM_SLICES_OBSTRUCTION.md), [phase209 CONSTRUCTOR_005](../../03-research/phase-209-nonlocal-kernel/CONSTRUCTOR_005.md) and [AUDIT_005](../../03-research/phase-209-nonlocal-kernel/AUDIT_005.md).

PROVED, source POWER_GRAM_SLICES_OBSTRUCTION §16; independent verification and re-checks PASS. Targeted cross-check with no literal antecedent located for this link with A; phase209 CONSTRUCTOR_005/AUDIT_005 are antecedents of the arithmetic Gram, and GRAM §4.1 of the band average. For FIXED positive integers k,l, z_k=.5log k+iy, epsilon=cos2y and L=log(1/epsilon), A(z_k,bar z_l)=[105/(512sqrt2)]rho(k,l)epsilon^(-9/2)L²+O_(k,l)(epsilon^(-9/2)L). If k=d a², l=d b² with the same squarefree part, rho=gcd(a,b)/sqrt(ab); otherwise rho=0. Exact resonances via Gaussian Riemann sums; near-resonances, including quadratic approximations, via elementary separation of residues and the Gaussian sum S_delta<=C_(k,l)delta^-4 log(2+1/delta), ALL delta>0. Dyadic IBP over ALL t>=1 gives a non-resonant remainder O_(k,l)(epsilon^-4L); lower terms are paid by absolute bounds and Cauchy–Schwarz. The classical gcd identity with totients proves rho SPD for every fixed list of DISTINCT integers; then its COMPLEX A block is eventually SPD, with a threshold depending on the list. Not a new classical Gram nor identification with norm 209; no uniformity in dimension/integers, real window, CPD/H, relative comparison at all orders nor global sign. No computations, campaigns, new W/T or papers modified.


### Phase 211 — SOS at all orders for the exact resonant part (2026-11-06)

**Scope §17.8, same entry (PROVED).** Independent verification and re-checks PASS. For T=pi t^(5/4)(-2tD-3), A0=-D, R_s=(A0+s)^(-1) terminal, T^-1F=(1/(2pi))t^-3/2 integral_t^infinity u^-3/4 F(u)du. The physical form q=Re<TA0f,Tf>=(pi²/2)[7 integral t^5/2|f'|²−(9/2)integral t^1/2|f|²] is negative for f=t^-3/4u(log t) with a wide bump. Choosing s>0 small and v=T(A0+s)f gives Re<T R_s T^-1v,v>=q+s||Tf||²<0. The integral formula of Rtilde_s is bounded on EXPONENTIAL H_gamma, norm<=2/gamma+4(s+3/2)/gamma²; density §17.7 transfers the negativity to a finite real theta aggregate. Antecedents phase199 E §3 Rem 3.1 and phase188 N_BUILD_007/018 have other kernels/orders/metrics; no literal located. Only accretivity of all these physical resolvents fails. The logarithm contains MINUS R_s: it does NOT refute positivity of the conjugate log nor every resolvent method, joint balance with C or the sign of A. No new route, computations, W/T or papers.

**Scope §17.6, same entry (PROVED).** Independent re-checks PASS, including y=0 by direct extension of the endpoint calculation. Fixing y∈[0,pi/4), the pairs k,k+1 have E_y and R_res diagonal. e_k=√k sum_n I_(kn²), r_k=√k sum_n[J_(kn²)+log k I_(kn²)]; r_k/e_k=log k+O_y(1/k) and Off_y(k,k)/e_k->0 exponentially. The correlation gives |A_y(k,k+1)|/√(e_k e_(k+1))=log k+o(1). E-normalized coefficients with negative cross term produce Off_y[c]=-log k+o(1), R_res[c]=log k+o(1) and A_y[c]=o(1). There is no finite C_y with Off_y>=-C_y E_y nor delta_y>0 with A_y>=delta_y R_res uniformly. At y=0, real coefficients (+,-) and A_y[c]>0 by §9; not A negative nor a decision of the critical bound Off_y>=-R_res. No new route, W/T or papers.

**Scalar shortcut §17.7, same entry (PROVED).** Independent re-checks PASS. For y=0 and F in the FINITE span of Theta_k(t)=Phi(.5log kt), C=sum_(m>=2)Lambda(m)/√m T_m², T_m²F(t)=F(m²t), there is no M with |integral(CF)barF dt/(2t)|<=M integral(1+log t)|F|²dt/(2t). The operator C is continuous on H_gamma=L²(e^(gamma t)dt/t), 0<gamma<2pi, and the theta span is dense there by Möbius inversion of h(kt), the inverse of L=-2tD-3 and C1 approximation by polynomials in e^-pi t. The plateaus 1_[1,R] give numerator>=cR^(1/8)log R and denominator=.5log R+.25log²R. One extends first by density for fixed R and then R->infinity. Explicit antecedents phase199 PROOF_L_SHARP_C_001 §4 Prop 4.2/E_001 §3 Rem 3.1, BRIDGE002 §3, AUDIT_L_SHARP_1 §2.4 and 019 §§3–5; not a new unboundedness principle, only a check on this exact carrier and weight. Not A negative, a non-resonant bound by R_res nor transfer/global closure. No computations or papers.

**Uniform refinement §17.5, same entry (PROVED).** Independent verification and re-checks PASS. D_q>=c_*I_q for all d,q>=1 and 0<epsilon<=1, c_*=(log2/3)(4pi-3)²e^-6pi/[(4pi+3)²+(4pi-3)²e^-6pi]. For dq>=2, log(dq)I_q suffices; for d=q=1, N!<=N^N 2^-floor(N/2) gives gap log2/3 when X>=2. With X=sqrt u, the bracket of DIAG is >=log2/3 on u>=2 (on 2<=u<4 the sum is empty). Core[1,2]<=pi²sqrt2(4pi+3)² and tail[2,3]>=pi²sqrt2(4pi-3)²e^-6pi pay a uniform fraction of I1. Thus R_res>=c_*E_y, E_y=sum_d sqrt(d)sum_q I_(dq²)|f_(d,q)|². Uniformity only in that exact divisorial energy, with I depending on epsilon/indices; NOT a uniform Euclidean margin, NOT the full A nor off-frequency, W/T or global closure. Eventual positivity of the FULL integer A does transfer to the real one by §18; this resonant bound alone does not prove it. No new route, computations or papers.

Source: [GRAM §17](../../03-research/phase-211-sign-sandbox/POWER_GRAM_SLICES_OBSTRUCTION.md). Antecedents: [SIGNED_MEAN_019](../../03-research/phase-211-sign-sandbox/POWER_SIGNED_MEAN_019.md), [CONSTRUCTOR_005](../../03-research/phase-209-nonlocal-kernel/CONSTRUCTOR_005.md) and [AUDIT_005](../../03-research/phase-209-nonlocal-kernel/AUDIT_005.md).

PROVED; independent verification and re-checks PASS, including the SOS and strict positivity. Cross-check all3/019/209 with no literal identity located. R_res retains ALL pairs kn²=lm² of the exact A and its integral t>=1. Each frequency may be indefinite: nodes 1,4 and lambda 4 give det=-2(log2)²I_4²<0. But for each group k=d a² and finite c_a, f_q=sum_(a|q)sqrt(a)c_a, I_q=I_(dq²), J_q=J_(dq²), the exact identity is R_res[c]/sqrt(d)=sum_q D_q|f_q|²+sum_q sum_(m|q,m>=2)Lambda(m)I_q|f_q-f_(q/m)|², D_q=J_q+(log d+log q)I_q-sum_(m>=2)Lambda(m)I_(qm)>0. The change u=lambda t turns D_q into a positive integral: sum_(m<=X)Lambda(m)/m<2log X by the factorial identity and floor(X/m)>=X/(2m). Gaussian absolute summability and bounded f justify everything; the least a with c_a!=0 proves strict definiteness. Thus R_res is PD at ALL orders on distinct positive integers k for EACH |y|<pi/4, including y=0. Classical factorial tool, without Möbius inversion; distinct frequencies are coupled, not PSD layers nor substitute Gram 209. NOT the full A, NOT all real nodes, NOT non-resonant control, new W/T or global closure. Update §18: for the FULL A, all integer blocks and all real nodes are equivalent; R_res is not transferred separately. No campaigns, numerical data or papers.


### Phase 211 — The full integer A is equivalent to A over all real nodes (2026-11-06)

Source: [GRAM§18](../../03-research/phase-211-sign-sandbox/POWER_GRAM_SLICES_OBSTRUCTION.md). **PROVED**, independent construction and verification; independent re-checks passed. Consulted all3 and the corpus; no literal statement located. Define P_kappa=kappa^(5/4)sum_n n²e^(-pi kappa n²t), T=pi t^(5/4)(-2tD-3), LgP=integral_0^infinity[e^-pi r P(t)-P(t+r)]dr/r and G=.5T LgP-C TP. Frullani and sum_(m|n)Lambda(m)=log n give TP_kappa=Theta_kappa and G(P_kappa)=.5log kappa Theta_kappa. The full A form is integral[log t|F|²+2Re(G bar F)]dt/(2t). For every finite list of positive scales one chooses a<pi min(1,kappa_min), gamma<2a; the norm B_a² simultaneously controls (F,G) in exponential H_gamma. The targets have weighted jets tending to 0: cutoff, C2 approximation in e^-pi t and absolute Möbius inversion e^-pi kt=k^-5/4 sum_n mu(n)/sqrt(n)P_kn² approximate by integer scales in that norm. Density of compacts for all of B_a² is NOT claimed, nor is density of F alone used. Continuity of the form transfers PSD of ALL integer blocks to ALL real nodes; the converse is restriction. Antecedents BRIDGE002§3, CONFLUENT_BRIDGE014, SCALAR_BRIDGE017 and GRAM§17.7: earlier density tools, other families or a norm without this full graph. No new abstract tool and no proved sign: R_res positive alone does not suffice; the full joint balance remains OPEN. Only the additional transfer gate for the FULL A is removed; the equivalence with the target lambda_A(T)>=0 for ALL T is verified later in §18.9, without identifying minima at fixed T. No computations, new W/T or changes to papers.


**Scope §18.5, same entry (PROVED).** Independent construction and verification; independent re-checks passed. B=Lg-2sum_(m>=2)Lambda(m)m²D_(m²), p=P1, Bp=0, has positive rates before T on P=pf. But the integral tail of TU_rT^-1 induces in T Lg T^-1 the off-diagonal kernel K(t,v)=t^-1/4v^-3/4-t5/4v^-5/4/(v-t), with respect to dv. K>0 for 2<v/t<3. TBT^-1=T LgT^-1-2C; choosing t0=2 and F>=0 nonzero, compactly supported in (9/2,11/2), gives CF(2)=F(2)=0 and TBT^-1F(2)>0. Refutes only the representation JF=integral[F(t)-F(v)]nu_t(dv)+V(t)F(t), nu_t>=0, even with local killing or subsequent conjugation by positive Theta1. Separated supports justify absolute interchanges without diagonal renormalization or loss at boundary 1. Antecedents 106_31, ROUND005D and L2_BUILD008 are other forms/metrics, without this T/K; targeted corpus/literature cross-check found no literal statement. NOT negative Q/A, NOT a general dismissal of Doob or of the joint method; full sign OPEN. No new route, files, computations, W/T or papers.


**Scope §18.6, same entry (PROVED).** Independent verification; independent re-checks passed. For A_ij(x,y)=integral_x^infinity(x_i+x_j+2s)Phi(x_i+s+iy)barPhi(x_j+s+iy)ds, Delta A_ij=4integral w_ij Phi_i'barPhi_j'-4P_ij(x,y), with the lower boundary preserved. On the diagonal x_i=0,y0,x>=1.088 gives p=-Phi'/Phi>2Y-6>Y, Y=pi e2s. Thus I=integral_x^infinity 2s p²Phi²>Y(x)[xPhi(x)²+integralPhi²]>Phi(x)² and Delta A_ii>0. The superharmonicity/harmonicity required by the direct minimum principle from the complex boundary §16 fails. No indefinite matrix source is claimed: its joint sign is not proved. The per-block threshold of §16 does not provide joint PSD on an open real interval for §2.2 either. NOT negative A/Q nor dismissal of all PDE/transport; global sign OPEN. Cross-check all3/16/2.2/088 with no literal statement resolved; no new route, files, computations, W/T or papers.


**Extension §18.7, same entry (PROVED).** Independent construction and verification; independent re-checks passed. Every fixed tail k>=K of the P_k approximates the targets of §18 in B_a² and in the graph (F,G): after cutoff, P_c=x^KQ(x), x=e^-pi t; C² approximation produces only exponentials with k>=K and error C_K eta e^-pi Kt, and Möbius introduces only kn²>=K. Thus PSD of ALL blocks of any tail is equivalent to the global real A. For any fixed prefix c_1..c_J there exist finite completions with k>J that approximate minus P_prefix and make A_0[c]->0, without assuming PSD. If PSD, the infimum over those completions is 0. There cannot exist A_0[c]>=delta|ell(c)|² with delta>0 and ell nonzero and FINITELY supported. Nor nontrivial diagonal minorants with ALL weights NONNEGATIVE, on c_k or on the finitely dependent divisorial observables f_(d,q) of §17; fixing the prefix preserves a positive term. Antecedents DESCENT_AUDIT016§§8–9 (another rational tail/W4), BRIDGE002§3 and 18.3: earlier instrument, not this carrier/graph/conclusion. It also excludes a SINGLE compatible identity A_0=sum_alpha w_alpha|ell_alpha|² with w_alpha>=0 and all ell_alpha finitely supported, even if their sizes grow: each summand would be a forbidden minorant. It does not exclude factoring each finite block separately; FIXED_BLOCK_ASSEMBLY treats another class/kernel and uniformly bounded sizes. Scope y0; no negative A, no dismissal of energies on continuous global observables/non-diagonal SOS, nor a global sign. No new route, files, computations, W/T or papers.


**Corollary §18.8, same entry (PROVED).** Independent construction and verification; independent re-checks passed. For EACH fixed real sigma, ell_sigma(c)=integral_0^infinity e^(sigma u)sum_k c_kPhi(.5log k+u)du admits no A_0[c]>=delta|ell_sigma(c)|² with delta>0 over all finite supports. The moment is continuous on H_gamma, by CS with integral_1^infinity t^(sigma-1)e^-gamma t finite; §18 transfers the assumed minorant to real nodes. At x=-R, Axx=2integral_R^infinity sPhi² and ell_sigma(F_x)~Z_sigma e^(sigma R), F_x(t)=Phi(x+.5log t), Z_sigma=integral over ALL of R of e^(sigma s)Phi(s)>0. The supertail makes the quotient tend to 0 for every real sigma. Antecedents BRIDGE002/106_31/ROUND005D/106_36 and GRAM8.4 have continuity, other forms, or altered density/cancelled moment; cross-check all3/corpus with no literal statement. Only individual real exponential moments: not complex ones/spectral test, not general signed moments nor negative A; global OPEN. No new route, files, computations, W/T or papers.


**Scope §18.9, same entry (PROVED, no sign).** Independent construction and verification; independent re-checks passed; repository rules/all3 and the primary definitions of Paper 46 cross-checked. The target lambda_A(T)>=0 for ALL T is equivalent to full PSD of K_(M_Phi), real A and all integer blocks A, even any fixed tail. New scope converse: cut at infinity f(r)=sum d_i e^-u_i r, u_i>.5, with sum d/(u_i±.5)=0; two fixed physical bumps correct moments with coefficients→0 in H_eta 014. f(0)=0 is not required: a causal jump is allowed in H^s, s<.5, and the log domain. Translating each compact to a window preserves Tate/W; the ∀T hypothesis signs the primitive K. The ALREADY proved lemma in GLOBAL Primitive comparisons with D=M_Phi odd real-analytic gives the full K; inverse sufficiency BRIDGE002. In the graph, ell_sigma(TP)=pi P(1)+pi(sigma/2-.25)integral t^(sigma/2+.25)P: Tate is equivalent to P(1)=0 and integral P=0, WITHOUT P'(1)=0. Do not import the preimage of L2_BUILD008. Each tail has moment rank 2: one bump P touches 1, another is interior; two FIXED tail vectors with invertible matrix correct errors→0. Thus 18.7 preserves any prefix and A0→0 even for exactly primitive completions; its non-minorants/local SOS survive. 18.8 σ±.5 vacuous there, other σ not inferred. NOT equivalence of minima at fixed T nor a new sign; global OPEN. No external statements, files, computations, W/T or papers.


### Phase 211 — Full sign of the first primitive polynomial in t=exp(2r) (2026-11-06)

Source: [GRAM§19](../../03-research/phase-211-sign-sandbox/POWER_GRAM_SLICES_OBSTRUCTION.md). **PROVED for the first vector; later two-dimensional extension in §19.9**; independent re-checks FULL PASS and PASS, and an independent literal reading PASS. With p=P1=sum_n n²exp(-pi n²t), S_j=sum_n n^-j exp(-pi n²), a=1+(2/pi)S4/S2 and P=p(t)(t-1)(t-a), one has EXACTLY P(1)=integral_1^infinity P=0, hence both Tate moments of F=TP vanish. Q(P)=Q_log+Q_B, Q_log>=0 and Q_B>1/1200-1/40000-1/4500-1/30000=199/360000>1/2000. The proof retains p exactly; principal (1,1) only as a reference with bound, correction of exact a, crosses (1,2)/(2,1) and ALL the remainder of the theta/prime double series with explicit Gaussian tails and exhaustive partition. No quadrature/campaign nor truncation without error. Cross-check all3/corpus 101/195/199/209/211 with no literal family located; antecedent E101_061 interpolates nodes, the earlier gamma/Laguerre families are in another variable. Elementary instruments, no world priority. This elementary proof signs THIS first primitive vector; it does not inherit other degrees/crosses or recurrence. The independent extension §19.9 signs the plane E1,E2; later degrees, all orders, a new W/T window and the global sign remain open. The sufficient-core property is proved separately in §19.8 and does not supply those signs. Papers untouched; no new files.


**Sufficient core §19.8, same entry (PROVED as scope).** Independent constructions; independent re-check PASS; cross-check all3/BRIDGE002§3/CONFLUENT_BRIDGE014/DESCENT_AUDIT016§§8–9/18 with no literal family/core. In B_a², a<pi, V=closure span{pt^j}; H(z)=p e^zt has Taylor in norm with ||p e^(z0t)t^j/j!||<=C_(z0)(1+b)²b^-j, b=pi-a-Re z0>0. Finite differences and overlapping negative disks give p e^-nu t in V for all nu>0 without Hahn–Banach. C² in x=e^-t for Q=P_c/(px) approximates compacts; cutoff only of targets with weighted jets→0, NOT all of B_a². B_a² convergence controls graph (F,G)/Q. Correcting errors (P(1), integral P) via p, tp has determinant p(1)integral(t-1)p>0 and coefficients→0. The primitives are E_j=p(t)(t-1)q_j(t), j>=1, q_j monic orthogonal for w=(t-1)p; E1 is the signed vector, degree 2 in R. PSD of ALL Gram Gamma_ij=Q(E_i,E_j) is equivalent to the target lambda_A(T)>=0 for ALL T: physical f compact primitive->F(t)=f(.5log t)->P=T^-1F compact and primitive, core+repair signs W and the domain of each window; converse TP poly superdecay is cut at ∞ and Tate is corrected in H_eta 014 before passing to the limit. The causal boundary/jump 0 allowed is preserved, without imposing P'(1)=0. No minima at fixed T nor new W/T. The plane E1,E2 has sign PROVED by the later certificate §19.9; degrees/crosses outside it and global remain OPEN. The core uses no numerical results; papers untouched.


**Full block §19.9, same entry (PROVED, computer-assisted).** Design, mathematical check and corrected literal check PASS; runs and independent reproduction exit0/FULLPASS with SHA256 e589fb2b9d98d76f021418427a903794f17aa629832f400f2154c21add52f170. For the first two E1,E2 of §19.8, FULL real symmetric Gram Q11>179/100000, Q22>17/10000, |Q12|<79/50000 and detQ>2733/5000000000: EVERY nonzero real combination in the plane is positive. At the same time Q_B(E1+E2)<-1/20000; promoting the separate sign Q_B(E1) to the family fails, NOT the full sign Q. Exact parameters via moments of w, enclosure theta 4 modes + positive tail; reference integral 2 modes paid with ALL theta/prime tails, temporal and Cauchy remainder deterministic. Corrected verifier uses 192 bits, 960 cells [1,16], Taylor degree 40 and exact algebraic R/L derivatives, asserts order 41; error inflation BEFORE gates. No adaptive quadrature/search nor cutoff without error. Sources and proof in GRAM§19.9, tools/power_thermal_primitive_two_verify.py/.log. Only this two-dimensional block: NO inheritance to the next degree, all orders, uniform margin, new W/T or global sign; sufficient core §19.8 remains independent. Papers untouched.


**Degree tails §19.10, same entry (PROVED as scope).** Independent re-checks passed. For EACH fixed J>=1, PSD of ALL blocks Gamma_(J..N), N>=J, is equivalent to the target lambda_A(T)>=0 for ALL T. It is an application of the GLOBAL Primitive comparisons lemma to a finite number of constraints: V=prod(u-sigma), d=Vb turns sum d/(u-sigma)=0 into polynomial moments of degrees 0..m-1; anchors+continuation and null rows at sigma repair via Vandermonde and deliver the full K. The thermal tail is equivalent exactly to P(1)=0 and integral t^kP=0, 0<=k<J, or physical moments Sigma_J={.5} union {2k-.5:0<=k<J}; without P'(1)=0. Core 19.8 repairs J+1 errors via p and t^j(t-1)p: rank by boundary p(1)>0 and positive Hankel of w. For physical exponents one cuts FIRST at infinity and repairs all moments with fixed bumps in H_eta 014; only afterwards T^-1 produces a compact to which the core applies. The preimage with power tail in B_a² is not introduced. Antecedents 014/083/GLOBAL/18.9/19.8, no new positive inequality nor general no-go. Neither does the certified plane E1,E2 sign a tail, nor is signing one excluded; all its sizes/crosses remain OPEN. No uniformity in J, minima at fixed T, new W/T, computations or changes to papers.


**First-mode reference §19.11, same entry (PROVED, application of 008).** Short version independently checked. For p0=exp(-pi t), the reference Q0(R)=integral[log t|T(p0R)|²+Re(TLg(p0R)conjT(p0R))]dt/(2t) is NOT PSD on real polynomials with R(1)=0 and integral pR=0 EXACT. It is not claimed that p0R is primitive in both moments: the constraints correspond to pR. Proof: 008 gives Arch[f]<=-4norm²+17normderiv²; three disjoint bumps equally widened form a negative real space of dimension 3. In their preimages P=T^-1[f(.5log t)], two constraints P(1)=0 and integral rhoP=0, rho=p/p0, leave a nonzero vector; the first kills ell_+=piP1 and by itself the polar term. A_P(P)=Arch+Polar<0. Core p0 in B_a² and repair via p0, tp0, with det=e^-pi integral(t-1)p>0, produce an admissible polynomial and Q0<0 by continuity. No degree or coefficients computed. Application of falsifier 008 to the exact domain, not a new arithmetic necessity nor a falsifier of the full Q/A/truncated theta kernel. Nor does it refute every perturbation or compensation between modes; certificates 19.7/19.9 untouched and global OPEN. No computations, new files, new W/T or papers.


### Phase 211 — Potential of the causal adjoint: negative interior sign (2026-11-06)

**PROVED, elementary proof with complete tails.** Source: POWER_GRAM_SLICES_OBSTRUCTION.md§19.12. Independent re-checks FULLPASS and PASS of the rational gates. Consulted repository rules/all3/106_31/ROUND005D/18.5/GLOBAL: Picone/Doob and logarithmic killing have antecedents; what changes is the potential of the exact causal adjoint in dt/(2t); no world priority nor exhaustive reading is claimed. With Theta(t)=Phi(.5log t), J=TBT^-1 and r=.5log t, Bp=0 for all t>0 and parity of Phi give forward Phi=2rPhi, backward Phi=-2rPhi. Their full average annihilates Phi by that physical algebra, WITHOUT using the external argument of 106_31. Restricting to r>=0 leaves g(r)=-integral_0^infinity k(r+s)Phi(s)ds, k(h)=2cosh(h/2)-exp(-h/2)/(1-exp(-2h))-sum Lambda(n)/sqrt(n)delta_log n. Weak causal adjoint J*Theta=2g-4rPhi, boundary 1 included; the potential of the signed difference identity is V(f)=integral Phi(r)g(r)|f(exp(2r))|²dr. At log 2 from the RIGHT, the prime tail starts at n>=3. Aplus=pi p(1)>3/25; Gamma<=Aplus/(3sqrt2). Principal (n,m)=(3,1)<3645/56000; ALL the remainder, grouped by q=mn, <1024/249000 by ratio<1/250 and exp(25/2)>250000. Thus P3<7/100 and g(log2+)<-19/300<-1/20. Rational Taylor gates and tails detailed in §19.12; no quadrature nor truncation without error. Right continuity gives an interval with Phi g<0. Three disjoint physical bumps in that interval and two Tate constraints leave a nonzero EXACTLY primitive combination with V<0; its preimage P is compact, P(1)=integral P=0. Only requiring V>=0 fails, even on those primitive profiles. Not negative Q/A nor a universal NO-GO of paths/three points; the difference term can compensate it. Global sign OPEN; certificates 19.7/19.9 untouched. No new files, campaigns, new W/T or papers.


**Two exact phases, GLOBAL (PROVED, restricted scope).** Independent re-check PASS. With COMPLETE profiles Psi_(k,theta)=sum_n n^-1/2 h_(kn²)exp(i kn²theta), the theta-average of A_theta weighted exactly by log t+.5log(kl) is R_res of GRAM§17. For D=A0−Api, nodes {1,2} give D22=0 and D12>0 by positivity of h and of the odd subaggregate; detD_{1,2}=−D12²<0. Thus BOTH PSD orders between A0 and Api fail. Not A0/Api negative, another majorization, a phase-uniform asymptotic nor a global sign. Complete series and tails, no numerics, new files, W/T or papers.


### Phase 211 — small hyperbolic comparison: necessary vanishing (2026-11-06)

**PROVED as implication / comparison OPEN.** GLOBAL, «Small hyperbolic comparison: necessary vanishing condition». Independently checked. For H=-D²+(2pi)²exp(2r) Dirichlet, U_f=integral f(t)exp(2it sqrtH)dt, the REAL Gram 2||U_f||HS² reproduces K_h. Continuity in H_eta, bridge 014 and translation transfer K_Phi>=epsilon K_h to real two-sided compacts. Cutoffs of Phi converge in H1 with weight exp(eta|t|); the physical identity H_full Phi=0 of GRAM19.12 forces U_Phi=0. Available difference: new physical identity, not a new principle of radical inclusion. It remains to show U_Phi!=0: NO contradiction, NO dismissal of small epsilon, NO global sign nor new T. For complex ones both branches are required; do not apply 014 directly to two-sided Phi. No computations nor changes to papers.


### Phase 211 — RES-SOS does not identify the channels of 106_38 (2026-11-06)

**PROVED, comparison of objects; no new sign.** GLOBAL, «Scope of RES-SOS against the remainders of 106_38». Independent re-check PASS. In X_frac, x=y+log n and v=e2y give products h_(n²i²)(v)h_(j²)(v) with n not dividing j: ALL are non-resonant, and carry a difference multiplier distinct from the weight of GRAM17. X_ctr uses h_(i²)(v)h_(j²)(n²/v), reciprocal scales. Under TWO-SIDED synthesis f_c=sum c_kPhi(x+.5log k), c=delta1 gives g=f_c/Phi=1 and X_frac+X_ctr=0, but R_res[c]>0; it excludes only their literal identification and a positive minorant by R_res with that synthesis. Do NOT transfer to the causal A nor dismiss corrected comparisons. Bridge 18 transports the full A, not these channels. The physical identity 19.12 does not resolve the old Poincaré nor restore the terms omitted in 106_32. No computations, new T or changes to papers.


### Phase 211 — symmetric infinite closure without drift: norm rigidity (2026-11-06)

**PROVED, explicit strong class.** HYPERBOLIC§12.2; independent re-checks PASS. Q C² in the norm of a Hilbert space, Q(v) in a common domain of symmetric B,C, sinh(v)Q'=BQ and Q''=CQ force ||Q(v)||²=A+c log cosh(v), A,c>=0. Proof: w=log tanh(v/2), symmetry of B=>K(w,z)=F(w+z), symmetry of C=>sinh(s)F''+cosh(s)F'=0. No continuous linear observation can be q_theta~2pi²exp(9v/4). Two strong FORCE -Q''+2b_i sinh(v)Q'=E_iQ with E_i symmetric in a common domain imply that system. Difference from §12: infinite dimension and unbounded operators, adding symmetry; the earlier finite matrix argument does not suffice. Does not require Dom B² nor self-adjointness. To deduce FORCE from an integral ODE, domains/interchanges must be justified; they are not automatic. NOT an exclusion of drift, variable metrics, non-continuous observations, scale-dependent prefactors or other Green functions. No new real sign, computations, T window or changes to papers.


### Phase 211 — infinite dimension with constant scalar drift (2026-11-06)

**PROVED for the declared strong class.** HYPERBOLIC§12.3; independent re-checks PASS and literal check PASS. Q even, C² in norm up to 0, common domain of symmetric B,C, sinh(v)Q'+alpha cosh(v)Q=BQ and Q''=CQ force K(v,z)=A/2[cosh((v+z)/2)^(-2alpha)+cosh((v-z)/2)^(-2alpha)], A=||Q0||². Symmetry of C gives a wave equation; symmetry of B fixes its data. The analytic Gram extends Q to |Im Z|<pi/2 with norm²=A/2[cosh(Re Z)^(-2alpha)+cos(Im Z)^(-2alpha)]. Alpha>=0: bounded real norm contradicts q_theta; alpha<0: bounded norm at Re Z=log2, Im Z->pi/2 contradicts the EVEN cusp e^Z->2i of complete theta. Do not use the alternating cusp i. Difference from 12.2: CONSTANT SCALAR first derivative 2alpha, any sign, infinite dimension, adding parity/Neumann 0. Two strong FORCE with symmetric E_i and that drift imply the system; do not infer FORCE from integrals without justifying domains. Does not exclude variable/operator drift, variable metrics or other Green functions. No global sign, new T, computations or edited papers.


### Phase 211 — variable scalar drift forced to be constant (2026-11-06)

**PROVED, explicit strong class.** HYPERBOLIC§12.4; independent re-checks PASS; literal check PASS. Two FORCE with b1!=b2>0, real scalar coefficients a1,a2 and E_i symmetric in a common domain force a1=a2 for nonzero C² Q, even in infinite dimension. Gauge q=(sinh v)^alpha Q, w=log tanh(v/2), gives Gram F(w+z); symmetry of C imposes a left-hand side depending only on s=w+z equal to beta F(s)/(sinh w sinh z). Varying w-z at fixed s forces beta=0; beta=b1b2(a1-a2)/(b2-b1). With parity, C² up to 0 and continuous theta observation, it reduces to 12.3 and fails. Extends constant to variable scalar; not operator drift. It also excludes a nonzero real scalar C² multiplicative gauge in the same coordinate and spectral coefficient 1, provided FORCE is justified. Do not infer interchanges of unbounded operators automatically. No global sign, new T, computations or changes to papers.


**Scope check of HYPER12.4, same date.** Algebraic example, independently checked: Q=(1,2cosh v), C=diag(0,1), D=diag(-4,-1), B=[[0,-2],[-2,0]] satisfies sinh v Q'+cosh v DQ=BQ and Q''=CQ with B,C,D symmetric and [B,D]!=0. The scalar dismissal does not extend automatically to operator drift. Contains no theta and gives no positive Green function: gauge exp(-rD) produces off-diagonals -4b exp(±3r), losing the usual symmetry. Other metrics and general systems not refuted. No new sign or T window.


**Metric repair of the operator example 12.4 (2026-11-06, PROVED).** Independent re-check PASS. Local formal symmetry of L=-D_r²+2D D_r+b²I+E requires M'=-DM-MD and [E+D²,M]=0, hence M=e^-rD M0 e^-rD. For the 2x2 example already recorded, M0V=V*M0 implies -4ab exp3r+4db exp(-3r)-16c=0; b=a0 exp r and the independence of exp4r, exp(-2r), 1 force M0=0. No positive LOCAL matrix metric for THAT example on any open interval. Other systems, non-local metrics and the theta sign not refuted. Source HYPER12.4, final paragraph; no new T or computations.


### Phase 211 — moving rates: exact strong threshold (2026-11-06)

**PROVED as approximation, not sign.** CONFLUENT_BRIDGE014§6; independent re-checks PASS. For eta>1/2, u_N>eta, u_N->infinity and V_N=e^-uNy polynomials of degree<N, approximation of all of H_eta ALONG N iff N/u_N->infinity; density of the UNION iff limsup N/u_N=infinity. Exponential distance in L²_eta=|(u_N-v)/(u_N+v-2eta)|^(2N), case r0 of 096. New strong step: approximate f' in L²_eta and antidifferentiate terminally, an operator of norm<=1/eta that preserves the SAME degree/block; no logarithmic loss. Not a linear envelope. PSD of those full blocks, or lower bound -epsilon_N||f||² with epsilon_N->0 (criterion 036), would suffice by continuity 014 and translation; hypothesis OPEN. THREE002 u>=2^(40N) does not enter; preserving the fixed margin 9 in the dense regime contradicts the physical radical cutoffs 19.12, it does not contradict semidefiniteness. No new W/T, computations or edited papers.


**Scope of the double scale, application of 008 (2026-11-06).** BRIDGE014§6 final, independently checked. For u_N=N^(3/4), approximate in H_1 the primitive test 008 and repair both moments with two correctors from the SAME V_N. One obtains Polar 0, AP[f_N]/||f_N||²<-3 and c_fN(log2)/||f_N||²>1/3 eventually, even though N/u_N²->0. It is not valid to suppress that contact uniformly as O(N/u²), nor to declare the principal AP PSD. Not negative W nor dismissal of a principal that preserves arithmetic; application of the earlier falsifier, not new positivity. No T/computations/papers.


### Phase 211 — growing prime cutoff: uniform error exp(-N) (2026-11-06)

**PROVED tail / retained sign OPEN.** BRIDGE014§7, independent re-checks PASS. For ALL N>=1, u>=2 and f∈V_N(u), Q=ceil exp(40N/u) gives |W−W_(<=Q)|<exp(-N)||f||². Application of THREE002 tail norm sqrt6·13^N exp(-ut/2), valid before the positive threshold and by confluence: Lambda<=log, exact integral comparison gives factor Q^(-(u-1)/2)[2log Q/(u-1)+4/(u-1)²], final bound 230N exp(-7N)<exp(-N). ARCH/polar/contacts q<=Q and all crosses are preserved; no suppression of low atoms. With u_N=N^.75, cutoff exp(40N^.25), a uniform lower bound -epsilon_N||f||², epsilon_N->0, would still be needed for that retained block; 014§6 would then close global. Neither retained PSD nor new T proved. A growing cutoff does not contradict the 106_32 fixed cutoff. No computations/papers.


### Phase 211 — subcritical moving cutoff: necessary threshold (2026-11-06)

**PROVED, truncated principal only.** CONFLUENT_BRIDGE014§8; independently checked. For u_N=N^(3/4), any cutoff log Q_N<=(2-delta)N/u_N, delta>0 fixed, has an explicit unit vector with two Laguerre coordinates with W_(<=Q_N)->-infinity. Bound: 2log u+32+4sqrt Q log Q+6/u-(2/u)exp((N-1)/u). Excludes polynomial cutoffs for a vanishing lower bound on the WHOLE block; such a lower bound would require liminf u_N log Q_N/N>=2. Difference from antecedents: quantified growing cutoff; 007 provides exact bands, 106_32 treats another object (transformed energy with atoms removed). Compared with the sufficient cutoff 40 of 014§7, it fixes the necessary exponential order, not the optimal constant. Not primitivity, not negativity of the full W, not the sign of cutoff 40 nor new T; do not extend to every dense scale without proof.


### Phase 211 — moving cutoff insufficient even on primitives (2026-11-06)

**PROVED for truncated W, not for full W.** BRIDGE014§9; independent mathematical check PASS. For u=N^(3/4), N>=2^60 and log Q<=2^(-12)N/u, an explicit unit vector from the SAME V_N has both Tate moments 0, f(0)=0 and W_(<=Q)[f]<-3. Coefficients C(z)=(1-z)(z+r)(z+1/r)[sum_(j<M)(-z)^j]^4, M=floor(N/4), r=(u+.5)/(u-.5). Elementary concentration E tau²<=2^18(u/M)²; Arch<-3 and all retained contacts have correlation>=1/2, so they worsen the deficit. Difference from 008: width u/M instead of u/sqrt(N), allowing this moving scale and an explicit growing cutoff. It is not a simple application of the negative polar of §8: here it vanishes exactly. Also dismisses polynomial cutoffs on primitive subspaces; does NOT transfer threshold 2, not negativity of full W, not the sign of cutoff 40 nor new T. No computations or changes to papers.


### Phase 211 — small hyperbolic comparison refuted (2026-11-06)

**PROVED, computer-assisted; replaces the OPEN status of this specific comparison.** GLOBAL «Closure of the small hyperbolic comparison»: there is no epsilon>0 with K_Phi>=epsilon K_(2pi). The earlier necessary condition required U_Phi=0, using the physical radical GRAM19.12 and the form bridge. New input: Picone with r exp(-3r) and Rayleigh with r exp(-5r) place omega_1=2sqrt(lambda_1(H)) in [17,41/2], H=-D²+(2pi)²exp(2r), Dirichlet 0. The physical integral G(omega)=integral_R Phi(t)cos(omega t)dt is <-10^-8 on ALL of that band by a ball certificate, complete tails and Bernstein; hence U_Phi v_1!=0. Independent reruns reproduce FULL PASS/exit0. Script tools/power_hyperbolic_phi_cosine_band_verify.py in phase211, SHA cddcc0bf1c902be2fce90a12969dec3a43209c85a037d5156a916c9a74410ab6. Only explicit theta and the spectrum of the MODEL, no zero tables. Not a negative sign of the target, not an exclusion of other models, no new T nor edited papers.


**Primitive refinement of the same closure (2026-11-06).** GLOBAL applies its earlier primitive continuation lemma to D=M_Phi-epsilon M_(2pi). For EACH epsilon>0 and EACH nonempty open interval I⊂(1/2,infinity), some finite block of rates in I with both Tate moments 0 has negative residual energy. Independent re-check PASS. Application of the existing lemma, not a new mechanism nor computation; no explicit size, coefficients or window, not negativity of the target kernel.


**Physical family of the same dismissal, not a new mechanism.** GLOBAL: g_R=(D²-1/4)(chi_R Phi) is compact, even and exactly primitive; it converges in weighted two-sided H1 to f_*=(D²-1/4)Phi, the physical radical. U_f*=-(4H+1/4)U_Phi has nonzero first mode by the certificate already recorded. HS convergence implies W[g_R]-2epsilon||U_gR||HS²<0 for every epsilon>0 and R large enough. Independent re-check PASS; no numerical R, no negative W proved, no new calculations or papers.


### Phase 211 — direct bibliographic antecedent of the temporal kernel (2026-11-06)

GRAM_SLICES§1 incorporates the public manuscript by Dylan Suvlu (24 Sep 2026), «Theta correlations and a causal range criterion for the Weil form», §3 eq18–23, https://dsuvlu.github.io/weil-form-operators/paper/theta-correlations-causal-range.pdf . Cross-check: j=A/(integral Phi)² and the same logarithmic response. Antecedent of representation, not a proved global sign; do not attribute novelty to A because of its absence in earlier searches. Does not determine priority of RES-SOS 17 nor of block 19.9. Draft, with no claim of peer review or complete verification; no new construction nor computations.


**Causal companion of the same antecedent:** GLOBAL records a reading of Suvlu III§2. The weighted contraction does not give ordinary L²; its separate majorant diverges when r is lowered to 1/2 already through c_Gamma. Divergence of the actual feedback or failure of every causal route is not claimed. RES-SOS and finite blocks do not supply a bound for the inverse here. Cross-checked; no new sign theorem nor computations.


### Phase 211 — BPY branching examined, preservation OPEN

GLOBAL records the candidate T'=W_1^-2 T_1+W_2^-2 T_2 and reciprocal symmetrization. It is not a theta truncation. Seed S delta_(pi/3) has explicit Gram; a single jet block of the first step was NUMERICALLY positive, without certificate or extrapolation. Symmetrizing afterwards preserves the limit under the convergence/fixed-mean hypotheses; symmetrizing inside changes the dynamics and its convergence is not proved. The step preserves an entropy with a signed factor and a signed integration-by-parts boundary; neither PSD preservation nor a counterexample was obtained. No new validated route nor degree campaign. Cross-checked; source and formulas in GLOBAL, no papers edited.


**Scope refinement of the branching (2026-11-06).** GLOBAL proves that S B does not factor universally through S: S delta_4=S delta_(1/4), but the outputs have different regularity at t=5. Exact density and derivative jump; independent re-check PASS. Does not refute PSD preservation nor the orbit of mean pi/3; the two inputs have different means. A concrete instance of information loss, not new progress on the sign. Independently checked extension: GLOBAL provides two finite positive laws of mean pi/3, same S and different S B outputs, via a six-atom antisymmetric reciprocal perturbation and ratios of density jumps. Adding the mean as data does not suffice either. PSD of those inputs is not proved, nor are PSD preservation or the specific orbit refuted; routine extension of the scope.


**Scalar diagnosis of the branching (2026-11-06).** GLOBAL contains a computer-assisted proof and reproduced inline code for kappa4 of the logarithmic tilt of S B delta_c<-1/5000 for all c>0. It reduces to k+4ds-2d^4 and to two moment bounds of V=A1+A2. Independent construction, algebraic check and full integral reproduction FULL PASS. This necessary falsifier does not work; PSD and preservation are NOT proved. No order campaign nor new T window.


**Branching: scope of the conditioning (2026-11-06).** GLOBAL keeps the exact identity K=mean of conditional congruences+C, with C equal to the negative of two normalized covariances. For the real input mu=B delta_(pi/3), C(u,u)=−Var(h)u²/2+O(u⁴), Var(h)>0 by continuity and full support. Thus C is not PSD already at the second real step. Independent re-checks PASS. Only paying THIS correction as positive fails; not negative K nor exclusion of joint compensation. No computations nor progress on the T window.


**External source for the log 11 window (CITED/UNVERIFIED, 2026-11-06).** GLOBAL records rStation45v1 and a normalization cross-check. The external claim would cover the primitive restriction of P46 up to log(11)/2 if validated; interval construction not reproduced, supplement already located through the public API; short checks of hashes, small matrices and Green pass, without regeneration 400. No new certified local frontier nor global closure. Papers untouched.


**2026-11-06 — rStation45/log11, partial verified update.** EVEN sector up to T=log(11)/2: **PROVED with computer assistance, local reproduction of an external result**. Full chain regenerated (safe/graph/contract/family/checker); checker exit0, complement 393 with Hmin>0 and seven core pivots>0. The interval elimination of the core was reproduced independently; an independent check confirmed six sources identical to the supplement, metadata, links between files and logs. Final file SHA256 18a3a25b3bacb3e265bee09232bdd09b17ea88074c9619bf6d9be069c4654cb3; last pivot [5.173121145006658e-50 +/-3.29e-66], NOT a spectral gap bound. Difference from historical pivots compatible with a different congruence/elimination order; bit-for-bit identity not required. **ODD sector still pending reproduction; local window of the FULL form remains 1.035; global sign OPEN.** External result, not our own novelty. Evidence and provenance in POWER_GLOBAL_ROUTE_REVIEW.md, external source log11 section, and /tmp/riemann-rstation45-audit/work. Papers not modified.


**2026-11-06 — FULL log11: verified local reproduction.** Replaces the earlier partial status: **PROVED with computer assistance, EXTERNAL result reproduced** for the full form W_T in both parities, 0<T<=log(11)/2 (approx. 1.1989476364). Source: https://rstation.ai/problems/riemann_hypothesis/papers/45 . All regeneration stages finished exit0; logs, sources identical to the supplement, metadata, file links and interval re-elimination of both cores were checked independently. Odd: complement 394 with Hmin=[0.0072415100579310717783150120757660513853081885959734786213576 +/-4.96e-62]>0, six positive pivots, last one revalidated [2.92609807122468755690e-45 +/-8.74e-66]. Final odd SHA 7211d28ec770386db511be3942e20ecd4056d2b5cc95501e7fd5a4802ae548ce. The final even file and its check are recorded above. The earlier analytic check preserves the infinite complement and agrees with the P46 normalization; the primitive restriction inherits positivity. The verified local frontier of the full form is updated from 1.035 to log(11)/2. NO spectral margin is deduced from the pivots. It is NOT our original result nor a proof for all T: global sign OPEN. Evidence stored in phase-211-sign-sandbox/tools/rstation45_reproduction/ (logs, sources, two final results, small checker and hashes); intermediate matrices remain in /tmp/riemann-rstation45-audit/work. Papers untouched. No further window campaign is launched: what is missing is a uniform structural estimate of the full Schur block, not just positivity of its favorable summands.


**2026-11-06 — Subtraction of cutoffs, checked, no new sign.** GLOBAL, «Subtraction of two smooth cutoffs»: w1−w2 removes the common summand and gives a primitive continuum, but covers all compact W after translation; the principal keeps one profile and the cross remainder lacks a new signed bound. Consequence of ROUND_001_A/REVIEW_002 and P211-A; independently checked. No general NO-GO, new window nor changes to papers. Global OPEN.


**2026-11-06 — Candidate: additive infinite PF + reciprocity (bridge OPEN).** GLOBAL, «BPY density»: q(v)=sum n²(2pi n²v−3)e^(−pi n²v), 2pi q has Laplace transform prod(1+s/(pi n²))^(−2). Convolution of double exponentials and uniform limit prove additive TP of all orders; q(1/v)=v^(5/2)q(v). These are classical properties of the data, not a new sign of A. The HCM countermodel fitted to that reciprocity has (log q_e)''(1)=3/4−2epsilon>0 and fails PF2: class difference verified. It remains to sign the integral kernel with q(av)q(bv) and log(abv²); additive TP does not authorize that multiplicative composition. No sufficiency, priority or closure claimed. Identities and scope independently checked, PASS; selective cross-check L23/L93/corpus. No computations nor papers; global OPEN.


**Additive PF + reciprocity: additional scope, no global sign.** GLOBAL develops the consequence h''<=0 and h(1/x)=beta log x+h(x) ⇒ −(log Phi)''>=2beta=5, already compatible with the known theta convexity. A Gamma(2, rate 4), PF infinite but NOT reciprocal, has integral t Phi²<0 by Jensen (mean 9/16), and its A has a negative diagonal. Excludes only automatic transfer of sign from exponential convolutions; does not refute the joint package nor its particular approximations. Hand calculation, no computations. Multiplicative bridge OPEN; papers untouched.


**PF/reciprocity — symmetrized finite approximants, specific scope.** GLOBAL: the density f_N of 2N exponentials has f_N(v)~C_Nv^(2N−1) at 0. Its symmetrized profile has positive tail exp[−(4N+1/2)|t|], so GRAM§8.5 already implies A not PSD. Moreover the reciprocal density ftilde_N has tail v^−(2N+3/2) and (log ftilde_N)''>0 eventually: PF2 fails. Not a counterexample to the full package; f_N→2pi q and the normalized profile uses factor 1/2, not pi. Specific result without computations/papers; global bridge OPEN.


**2026-11-06 — Rigidity of FINITE modifications of BPY rates (PROVED in class).** GLOBAL: keeping exactly two rates pi and modifying finitely many other rates, all>pi, gives L_f=R rational·L_0. If moreover f(1/t)=t^(5/2)f(t), the tail (At+B)e^−pi t and its reciprocal force R=r0+r1/sqrt(s)+r1/(2sqrt(pi)s)+exponential error; rationality implies r1=0, R constant=1. Independent re-check PASS; no literal antecedent in selective cross-check. Not uniqueness of general infinite PF nor the sign of A; infinite modifications/change of the minimum out of scope. No computations/papers; global OPEN.


**2026-11-06 — Additive BPY renewal, bounded scope.** GLOBAL: vf(v)=∫_0^v k(v−u)f(u)du, k=2sum exp(−pi n²x), produces a descending transition; reciprocity produces an ascending one. Their equiprobable mixture admits no reversible density: the cocycle R(L,2L)R(2L,3L)/R(L,3L)~1/sqrt(2L), not 1. Independently checked; difference from divisorial renewal E101.089, targeted corpus/literature cross-check. Its energy was not identified with A: NO negative sign of A nor closure of the package, no exclusion of other weights/non-reversibility. No computations/papers; global OPEN.


**2026-11-06 — Folded renewal: exact identity and indefinite layers.** GLOBAL constructs xf(x)=∫_1∞f(u)h_u(x)du and A=∫∫f(u)f(w)S_ab^(u,w)dudw, with h_u=k(x−u)+sqrt(u)k(x−1/u) on their exact supports. Absolute Fubini preserves the entire logarithmic weight. For u>w>1, a=u+delta, Sdiag→S0>0, S1=−C/sqrt(delta)+O1, S12=O(delta^−1/2), hence jetdet=−C²/delta+O(delta^−1/2)<0. There are layers with a negative minor in every open real interval of scales>1. Not a negative sign of A, nor a conclusion for integer nodes, nor exclusion of compensation/grouping. Double independent check PASS. No computations/papers; global OPEN.


**BPY renewal, one integrated source (specific corollary).** GLOBAL: integrating w completely leaves C_ab(u) with g(x)=xf(x). Positive diagonals for a>=1, but near a=u+delta the jetdet is −u f(u)²(log u)²/(256delta)+O(delta^−1/2)<0. Hence these individual layers are not PSD either; fails at nearby real nodes>1, neither integers nor the full A are decided. Independently checked; application of the earlier mechanism, not a new general criterion. No computations/papers; global OPEN.


**2026-11-06 — BPY self-decomposition and limit of the scale orbit (scope PROVED; sign OPEN).** POWER_GLOBAL_ROUTE_REVIEW, «BPY self-decomposition»: L(s)/L(cs)=prod[c+(1−c)lambda/(lambda+s)]² constructs the jump semigroup with invariant density f and auxiliary positive energy, rho=−k'. Its stationarity reproduces the renewal, without identifying the energy with A. The common semigroup does NOT preserve dilations: if cdX+Y_c were bX, the mean fixes b=1+c(d−1), but the difference of variances is −2sigma²c(1−c)(d−1), nonzero for d different from 1. Inversion changes f dx to x^(1/2)f dx. Does not dismiss other transports nor decide A. Object distinct from the false archimedean/diffusion identification of phase 64/154; classical tool, no priority. Independent re-checks PASS; targeted corpus/all3 cross-check. No web, numerical computations or papers.


**2026-11-06 — RES-SOS: no uniform UPPER bound of the remainder (corollary, y=0).** GLOBAL, «resonant budget»: for fixed N and k>N², k,...,k+N−1 have distinct squarefree parts; R_res is diagonal. The complete theta endpoint of GRAM16.5/17.6 gives R^(-1/2) A R^(-1/2)->J_N and normalized Off->J_N−I_N. Coefficients r_i^(-1/2) give Off/R->N−1. Letting N grow after that limit excludes Off<=C R and |Off|<=C R for every finite C, and hence a uniform norm of H=−R^(-1/2)Off R^(-1/2). Does NOT exclude H<=I nor decide Off>=−R or A. Same mechanism of nearby blocks, with exact RES-SOS budget; no new principle nor sign. Independent re-checks PASS; all3/corpus cross-check. No web, numerical computations or papers.


**2026-11-06 — Factorial extension before resonance, signed remainders (identity PROVED; global sign OPEN).** GLOBAL, «Factorial extension»: with b_lambda=sum_(n²|lambda)n^-1/2 c_(lambda/n²), full Gram K, projection P_m onto m²|lambda and shift R_m, Q=sum Lambda||P_mb−R_mb||_K²+b*Db+E. D integrates h_lambda h_mu against log(t sqrt(lambda mu))−log gcd(q_lambda,q_mu)−S(sqrt t); E=−2Re sum Lambda(R_mb)*K(I−P_m)b. The factorial signs ALL entries of D, but D is not PSD because H−D>=0 and the reference H without comb has a negative test by GRAM19.11/18.3. E(delta1)<0. Truncated Möbius inversion and Gaussian tails transfer both separate failures to finite c. Not negative Q/A nor dismissal of joint compensation. Difference from RES-SOS: crosses of distinct frequencies are preserved; no new factorial/Gram tool. Independent re-checks PASS; targeted cross-check all3. No web, numerical computations or papers.


**Corollary of the factorial extension, 2026-11-06:** c=delta1 gives b_(n²)=n^-1/2 and P_m b=R_m b for all m. Hence S_sq=0, while E=−2sum Lambda(P_mb)*K(I−P_m)b<0 (already m2, indices 4/1). No finite C allows E>=−C S_sq. Q[delta1]=A(0,0)>0: D pays for that E, no global sign inferred. Direct corollary of the earlier identity, not a new mechanism; independent re-checks PASS. GLOBAL keeps proof and scope. No web, computations or papers.


**Kernel of S_sq, algebraic corollary (2026-11-06).** In the factorial extension in GLOBAL, for finite c, S_sq=0 iff c is supported on squarefree integers. b_(dq²)=c_d/sqrt q proves one direction; injectivity of the Gram K through T and exponential uniqueness, recurrences at each prime and Möbius inversion prove the other. In that family Q=D+E; neither PSD nor density inferred. Independent re-checks PASS, targeted cross-check all3. No web, computations or papers.


**2026-11-06 — SF factorial balance: B+M not PSD (exact test).** GLOBAL: on the squarefree kernel, the K-weighted sum of log gcd coincides with B=Gram_S(sqrt t), and D+E=Q=L+M; the factorial signs 0<=B<=L. The sufficient bound B+M>=0 fails on {1,2}, c=(1,−1/100): complete theta bounds give T11<1e−6, T22<1e−2, T12>1e−4, hence c*Tc<0. L−B>=0 is not removed from Q and the full block remains positive; no global sign. Independent re-checks PASS; cross-check all3, no new factorial tool nor campaign. No web, numerical computations or papers.


**2026-11-06 — SF density in the graph and absence of a fixed L−B margin.** GLOBAL: P_z holomorphic in B_a², ||P_z||<=C(1+|z|)^13/4 on Re z>=delta>a/pi. An annihilating functional divided by (z+1)^4 is bounded; Schwarz with finite factors and ΣSF 1/d=infinity forces identical vanishing. Hahn–Banach+GRAM18.3/18.7 prove approximation of compacts by any SF tail preserving the graph. With g_R=(D²−1/4)(chi_R Phi), W g_R->0, L² norm->positive; translating to r>=1 and using w=log t−S√t>=log2/3 implies that Q>=epsilon(L−B) is false ∀epsilon>0, also SF. Equivalent to excluding B+M+alpha(L−B) PSD ∀ fixed alpha<1. Not negative Q, no semidefiniteness proved, variable margins not dismissed. Independent construction and re-check PASS; targeted cross-check all3, classical tools, no web/computations/papers.


**2026-11-06 — Joint factorial remainder not PSD; no margin from S_sq.** GLOBAL: approximate P4 in B_a² by P(c_n) with c_n SF finite, and take e_n=delta4−c_n. Q[e_n]->0, but J annihilates SF and hence S_sq[e_n]=S_sq[delta4]=s0>0. Therefore (D+E)[e_n]->−s0: the JOINT remainder is not PSD and no ε>0 allows Q>=εS_sq. S_sq is not continuous in B_a², though Q is. Difference from 18.7: infinite observable of the factorial identity, using SF density. Independent re-checks PASS. Not negative Q nor global dismissal of compensations; no web/computations/papers.


**2026-11-06 — Scalar resolvents of the product: non-PSD layers.** GLOBAL: J_u=integral Phi(r+x)Phi(r+y)[(1+u)^−1−(exp(2r+x+y)+u)^−1]dr, A=integral J_u du with absolute Fubini. Parity gives a negative limiting diagonal ∀0<=u<1; GRAM2.2 excludes PSD of J_u on any open real interval. SF density applied to the PAIR (P_z, z^-1/2P_z), not P alone, transfers J0 negative to finite SF c; continuity preserves the same test for 0<=u<eta. Not negative A nor SF failure ∀u<1 claimed. Object distinct from TR_sT^-1 of 17.8; integrated compensation still missing. Independent re-checks PASS; cross-check all3, no web/computations/papers.


**Reciprocal pairs of resolvents, candidate OPEN (2026-11-06).** GLOBAL: C_u=J_u+u^-2J_1/u, A=integral_0¹C_u du; weight h_u(z)=(z²−1)/[(z+u)(uz+1)] odd under inversion. h0=z−1/z, h1=(z−1)/(z+1), integral_0¹|h_u(z)|du=|log z|. Parity of Phi gives diagonals C_u(x,x)>0 ∀x real, u∈[0,1], removing the individual falsifier. NOT PSD all orders nor sign of A; a bound on the crosses is missing. Difference: pairing before estimating, not individual layers. Identities independently checked PASS, cross-check all3; no web/computations/papers.


**2026-11-06 — Extreme pair C_0 PSD in ALL real orders (PROVED, auxiliary).** GLOBAL: C0=integral 2sinh(2r+x+y)Phi(r+x)Phi(r+y)dr has Gaussian DOM. Transform=(Z(a+1)Z(b+1)−Z(a−1)Z(b−1))/(a+b). Z(a)=xi(a+.5)/2; S=2pi(s−1)zeta(s)/[(s+1)(s+2)zeta(s+2)], s=a−.5. Absolute Euler inverse and Euler–Maclaurin construct S holomorphic, polynomial growth; parity gives |S(it)|1, Euler bound for Re a>=32 and maximum in the strip give |S|<=1. Schur kernel PSD by Hardy/Parseval, congruence and the DOM converse of GRAM2.1 sign the temporal C0 at all nodes. Independent re-checks PASS, targeted cross-check all3/phase16 without literal statement, no world priority claimed. NOT interior C_u nor global A: endpoint u0 of measure zero. No web, computations, papers.


**2026-11-06 — Two transports from C_0 dismissed in precise classes (PROVED).** GLOBAL, «Two transports from C_0»: q_u(w)=1/(1+u²+2u cosh w) has strictly concave log, so q_u(x+y+2r) fails PSD already in 2-minors; it is not a positive Schur multiplier. Moreover there is NO minorant C_u>=integral C_0(x+t,y+t)dmu(t) with fixed nonzero positive mu, 0<u<=1: even diagonals D_u/D_0<=u^(-1)e^(-2|x|)->0, while any compact mass of mu imposes a positive ratio at one of the ends by monotonicity of D_0. Includes impossibility of equality. New working hypothesis: full C_0 already signed in all orders; distinct from the pointwise Hankel GRAM2.3. Independent re-checks PASS; targeted cross-check all3. Does not refute C_u/A nor transports with other profiles/gauges. No web, computations or papers; global sign OPEN.


**2026-11-06 — B_1 PSD in all orders does NOT imply B_0 PSD: smooth countermodel (PROVED).** GLOBAL, «The positive hyperbolic endpoint»: B_b has weight sinh(b(2r+x+y))/b, B_0 linear. Profile phi=3g+(g(·−2)+g(·+2))/2, g standard normal, Z=exp(a²/2)(3+cosh2a). Explicit geometric inverse and difference of moduli prove S_1=Z(a−1)/Z(a+1) contractive; Schur/DOM signs B_1 in all orders. But K_M, M=Z'/Z, at Laplace nodes (log2/2, log2), vector (42,−41), gives 1−516/(34log2)<0: temporal B_0 not PSD (these nodes are not identified with temporal test 2). Antecedent CONE001§4; difference: Gaussianizing and also verifying B_1 PSD. Independent re-checks PASS. Excludes universal transport under parity/positivity/smoothness/Gaussian DOM; NOT theta data nor its additional hypotheses/supertails. Theta descent OPEN, no web/computations/papers.


**2026-11-07 — Unitary reciprocity does not make the BPY factors contractive (PROVED, precise class).** GLOBAL, «Additive PF and inversion»: R_beta h=x^(−beta)h(1/x), beta=5/2, fixes q and is unitary on L²(x^(beta−1)dx). But causal V_lambda=lambda(D+lambda)^(-1) is NOT contractive for ANY lambda>0: h_R=h(x/R), v_R=h_R'+lambda h_R, gives norm difference R^(alpha−1)[lambda alpha R B−A]>0, alpha=3/2, A,B explicit positive. Antecedent VIRTUAL_SOURCE_017§§1–4 changes the metric; new calculation on complete BPY exponential factors in the reciprocal metric. Independent re-checks PASS. Only blocks that composition of contractions; does not dismiss the full product/other compensations nor PF+reciprocity. Additional cross-check: derivatives of the product return the recorded renewal; inversion of the additive kernel returns the Möbius change already examined. No new joint bound nor sign of A, no web/computations/papers.


**2026-11-07 — COMPLETE BPY convolution unbounded in the reciprocal metric (PROVED).** GLOBAL, «The complete BPY product»: H=L²(x^(3/2)dx), causal T_f, f=2pi q. h_epsilon=epsilon^(−5/4)h(x/epsilon), h>=0 compactly supported in (1,2), normalized, has norm 1 and ||T_fh_epsilon||>=c epsilon^(−1/4), using min_[1/2,2]f>0. Every output lies in H; there is no bounded extension. Separate control away from 0: h_R=h(x/R) gives a contractivity defect alpha m R^alpha B+O(R^(alpha−1))>0 by Taylor and the BPY exponential moment. Difference: evaluates the complete product, does not infer from its factors. Independent re-check PASS; cross-check all3. T_f q!=q (Laplace L²!=L); row normalization changes the operator, kernel k returns the earlier renewal. Only dismisses this normative mechanism, NOT A/PF+reciprocity. No web/computations/papers.


**2026-11-07 — Single diagnosis of C_1, no falsifier (NUMERICAL, not certified).** GLOBAL: reciprocal-pair block C_1 at nodes (−1,−1/2,0,1/2,1), even integrated formula with tanh(v); first normalized eigenvalue approximately 0.01323704, all positive in a truncated double computation. Formula independently checked, cross-check all3: not to be confused with the old gauge generator C_1. NOT certified nor progress on the global sign; no further sweep. Pairs C_u and A remain OPEN; papers untouched.


**2026-11-07 — Explicit restriction on operator drift (PROVED in regular class).** HYPERBOLIC§12.5. Q even C4, Q''=CQ, sinh(v)Q'+cosh(v)DQ=BQ, B,C,D symmetric in a common domain and DQ continuous: K=.5[F(v+z)+F(v−z)] forces L=<DQv,Qz>=.5[G(v+z)+G(v−z)], G=−coth(t/2)F'(t), G0=−2F''0. Hence Lvv=Lzz; L is not presupposed PSD. With additional DC/CD domains and differentiation in the graph of D one deduces only a vanishing weak commutator against span Q; NOT strong commutation. Difference from §12.4: solves the operator kernel, not a scalar reduction. Independent re-checks PASS, cross-check all3. No theta realization, Green function nor sign of A; operator escape OPEN. No web/computations/papers.


**2026-11-07 — UNFOLDED physical process not monotone in the usual order either (PROVED).** GLOBAL, «Keeping both branches»: for A_markov=−L of 106.41, upper rate Q_x(z), z<log2 nearby, Q'_0/c=−integral_z∞g'K+sum a_nK'(log n)<=g(z)Kz+a2K'(log2)<0. Each theta mode at log2 has log-derivative<−19; upper limit<K(log2)/sqrt2[4/3−19log2]<0. Threshold without crosses and complete tails justify differentiation/smoothing; two ordered states violate a necessary condition for monotonicity. Difference from 106.115: full line and continuous rate defect, NOT the folded reflection jump. Independent re-check PASS, cross-check all3 and 106_41/42/115. Only the usual order on R, not other cones nor sign of A. No web/computations/papers.


**2026-11-07 — Physical semigroup does not preserve EVEN convexity (PROVED).** GLOBAL, «The physical semigroup does not preserve even convex functions either». Smooth hinge test (|x|−R)+, R↑log2, flat near 0: (A_markov f)''0/(2c) has Gamma<K0, integer tail n>=3<K0, contact 2<−38K0/3. Modal bounds p_j''<=y²p_j and geometric series control all modes/contacts, without computations. Positive even mollification leaves contacts in the linear region. Dual test psi=rho''/(dmu/dx) of the core, f in L²mu, shows a negative derivative of integral P_tf rho'' initially 0: no convex preservation without assuming f in Dom A nor P_t C². Difference from 106115/last GLOBAL: reflection preserves convexity, but complete rates destroy this cone; 106112 Bochner and 10364 another object. Independent re-check PASS, cross-check all3. No sign of A nor dismissal of other cones; papers untouched.


**2026-11-07 — T*T/weighted Hardy: identity without a new bound (duplication check).** GLOBAL: B_j=Lg−2sumΛ(m)m^jD_m², E_j(U)=integral t^(j−1/2)[log t|U|²+Re B_jU bar U]. For P(1)=0, (B2P)'=B4P' and IBP give Q=(pi²/2)(4E4(P')−6E2(P)−6||P||²_t3/2). The boundary −6P1·bar(B2P1) disappears without requiring P'1=0. Hardy for norms alone does not sign B_j; no joint estimate obtained. Gauge R=e5x/4P(e^x) returns the physical datum F=−2pi(R'+R/4). Direct verification, cross-check all3/GRAM. NO new sign nor general NO-GO; do not repeat the identity as a closure. Papers untouched.


**2026-11-07 — Conjugate imaginary translations of C_0 do not minorize A (PROVED, precise class).** GLOBAL, «Conjugate imaginary translations»: K_eta=C0(x+i eta,y-i eta), |eta|<pi/4. Complete theta gives K_eta(x,x)~pi³/c_eta exp(9x-2pi c_eta exp(2x)), c_eta=cos2eta, uniform on interior compacts. Thus K_eta/D0>=1/2 uniformly, while A(x,x)/D0<=x/sinh2x->0 and Cu/D0<=u^-1exp(-2x)->0. No fixed nonzero positive mixture without gauges can minorize or represent A or Cu, 0<u<=1. Difference from real translations: interior conjugate imaginary arguments, not covered by that dismissal. Independent re-check PASS, cross-check all3 with no literal antecedent; no world priority. Only this class, not negativity of A nor dismissal of general gauges/congruences. No web/computations/papers.


**2026-11-07 — Integrated quotient A/C0 not PSD, even with gauges (PROVED).** GLOBAL, «The integrated quotient A/C_0»: diagonals H(x,x)<=x/sinh2x->0, even; antidiagonal H(x,-x)->1/2. Complete proof: nu_x proportional to 2sinh2r Phi(x+r)Phi(x-r) concentrates at 0; lower bound c exp(7x-2pi exp2x), tails delta..x and x..infinity controlled with complete theta. Minor {−x,x}->−1/4. For Cu/C0, u>0 fixed, the same argument gives antidiagonal (1+u)^−2, diagonal 0, negative minor. Nonzero diagonal factors are only a congruence of the quotient: they do not repair Schur transport. Difference from pointwise q_u: here the kernels are already integrated; not deducible from that no-go. Independent re-check PASS, cross-check all3. Only quotients, NOT A/Cu negative nor dismissal of other transports; no web/computations/papers.


**2026-11-07 — Orthogonal projection of divisibility: application of density (PROVED).** GLOBAL, «Control of the orthogonal substitution»: in H=L²dt/(2t), closure of span h_(m²k)=H by GRAM17.7 rescaled x=exp(-pi m²t); Pi_m=I. Replacing the coordinate selection P_m by Pi_m in the factorial loses divisibility. R_mF=m^-1/2F(m²t), norm<=m^-1/2||F||; sum Lambda(m)||F-R_mF||² diverges if F!=0, already over powers of 2. Does not remove the signed remainder nor prove negative Q; only invalidates that replacement. Independent re-check PASS, cross-check all3. Application of the antecedent, not a new tool nor sign; no web/computations/papers.


**2026-11-07 — Explicit theta operator realization (PROVED, no sign).** HYPERBOLIC§12.6: H=L²(sech(pi omega/2)domega) direct sum R³, Q=(cos omega v, cosh(v/4), cosh(5v/4), cosh(9v/4)); C multiplier (-omega², lambda_j²). D continuous=1+omega coth(pi omega/2)+(15/2)cosh(pi omega/2)/cosh(2pi omega), D discrete=(-29/4,-23/4,-9/4). BQ=sinh v Q'+cosh v DQ defines a densely defined symmetric operator on span Q, closable; C,D self-adjoint and graph domains verified. q_theta=Phi(v/2)exp(2pi cosh v) is an exact continuous observation: subtracting three cosh leaves an analytic residual in the strip pi/2, O(exp(-|Re v|/4)); cosine density decays like exp(-pi omega/3), square/rho integrable. Difference from 12.5: objects and observation are constructed, not only necessary conditions. Independent re-check PASS with correction of residual rate 3/4→1/4. NOT a compatible metric, positive Green function nor sign of A; no world priority. No web/computations/papers.


**Integral extension of the same realization 12.6 (PROVED, no sign).** Y_nu(b)=integral_0∞exp(-b cosh v)cosh(nu v)Qv dv belongs to the graphs of C, D, Bbar by superdamping. Double IBP with vanishing boundaries gives Yrr=(b²+nu²)Y+2DYr+(-C+2bBbar)Y, r=log b. Exact observation <Y_nu(2pi),h>=Z(2nu), full normalization. Domains and signs independently checked PASS. Not self-adjointness of the sum, metric nor positive Green function/sign of A.


**2026-11-07 — Bounded local metric impossible for theta realization 12.6 (PROVED, class).** HYPER12.7: e2,e1 in the graphs of Bbar, C, D² with Be2=−9e1/4, Be1=−7e0/2−9e2/4. For M(r)>0 bounded local C², without diagonality, compatibility M'=-DM−MD and symmetry of E=−C+D²+2bBbar force Mij=mij exp(−(di+dj)r). The pair (e2,e1) gives b[−9M11+14M20+9M22]−63M21=0, exponents 25/2, 21/2, 11/2, 8 distinct: m11=m22=0, contradiction. No Be0; graph limits and forms justified. Difference from 12.4: exact infinite theta realization, not a 2x2 model. Independent re-checks PASS. Realization 12.6 remains valid; only that bounded local repair with principal −I fails. Unbounded/non-local metrics, other connections/realizations and the sign of A NOT decided. No web/computations/papers.


**2026-11-07 — Laplace of reciprocal pairs (identity PROVED, candidate OPEN).** GLOBAL: D_v=integral PhiPhi[exp(-v/z)-exp(-vz)]dr, z=exp(2r+x+y). Cu=integral exp(-uv)D_v dv and A=integral(1-exp(-v))/v D_v dv, absolute Fubini by |h_u|/|log z|. D_v/v→C0 with majorant |z−1/z|. PSD of D_v ∀v, all sizes, would suffice for A; premise NOT proved, no falsifier. Difference: combining reciprocals before signing, not additive BPY sources; proposed 2D Poisson does not introduce nm, no Gram obtained. Independent re-check PASS; cross-check all3/E101070/renewal without literal statement. No new sign estimate nor world priority, no web/computations/papers.


**2026-11-07 — Laplace layer D_(2pi) indefinite (PROVED, certified; updates the earlier candidate).** GLOBAL: block −1,0,1 has entries d1,c,e and central d0; (d1+e)d0−2c² in [−6e−21 ±8.08e−22]<0. Rational test (1,−1/1300000,1) upper<−2.6e−17. Four positive folded integrals, 32768 Arb rectangles at 192 bits per integral, 8 modes+uniform omission 2^-224, tail s>=4<2^-1000; inflation 2^-210. Verifier tools/power_paired_laplace_counterexample_verify.py and logs FULLPASS exit0 on independent reruns; SHA256 e6fee17a626174c60ecbd46a4d206deca911a3e156ec25fd4af5b0b695e7a07c. Design, prior and literal checks and reproduction PASS. One diagnosis, no sweep. D_v PSD ∀v FALSIFIED; Laplace identity remains, integrated compensation OPEN. NOT Cu/A negative nor T window/papers modified.


**Corollary of D_(2pi), same entry.** GLOBAL: certified test g(v)=c^TD_vc continuous bounded, g(2pi)<0; (-1)^nf^(n)(u)=integral v^n exp(-uv)g(v)dv for f=c^TC_uc. Gamma weights at u=n/(2pi) concentrate at 2pi (quadratic error v0²(n+2)/n²), so the alternating derivatives are eventually negative. Refutes matrix CM on ALL u>0/any tail; NOT on (0,1], nor PSD of Cu/first-order monotonicity/sign of A. Independent re-checks PASS; consequence without new computations.


**Later pointwise check, NUMERICAL not certified.** GLOBAL: integrating for Cu with u=1/(2pi), fixed test (1,−1/1300000,1), nodes −1,0,1, form ≈4.0700e−15 positive in double; no integrated falsifier found. Eight modes/cutoffs without enclosure, not PSD nor a new sign. No sweep nor further certificates; negative D_(2pi) still does not imply negative Cu/A.


**2026-11-07 — Primitives of D_v: review without progress on the sign.** GLOBAL, «Primitives of the layers»: G_V=int_0^V D_v, F_R=int_0^R D_v/v; F_R=G_R/R+int_0^R G_v/v² and A=int(-w')G_V, w=(1-exp(-V))/V. Identities independently verified; G_V PSD for all V remains OPEN. A change of weight without a new theta operation is rejected as a new route. The argument by approximate radicals does not close: normalized nodes in C0 have A/C0->0 and G_V/C0<=V/(2sinh(2x))->0 for each V, although G_V/C0->1 when V->infinity is taken first. A fixed radical in a common domain is missing; no refutation of G_V or A. No computations nor papers.


**2026-11-07 — Shifted cosh products: entire closure incompatible with theta (PROVED).** `03-research/phase-211-sign-sandbox/POWER_HYPERBOLIC_MODEL_GRAM.md`§13. For Q_n=prod_j(cosh(b_nj t)-c_nj)/(1-c_nj), b_nj>0, -1<c_nj<1, Q_n(1)<=M implies sum d_nj<=M-1, d=(cosh b-1)/(1-c), and b<=B=arcosh(2M-1). On |z|<=R, |Q_n(z)|<=exp[(M-1)R²cosh(BR)]. Every real locally uniform limit extends to an entire function. The theta quotient Phi(t)exp[2pi(cosh2t-1)]/Phi(0) diverges at the already proved cusp t=(log2)/2+i pi/4; it is not such a limit. Excludes approximating Phi by C_n exp(-2pi cosh2t) Q_n at fixed scale, and infinite products defined by their partials. Difference from §11/11.4: variable c avoids the earlier integer multiplicity, but normality excludes the enlarged class without classifying limit products. Independent screening and re-check PASS. Does not decide preservation of PSD by each factor; does not cover variable scales, other factors, sums, quotients or real powers. No new sign of A, extension of T, numerical computations, web or papers.


**2026-11-07 — Variable positive scale in shifted cosh products: escape closed (PROVED).** `03-research/phase-211-sign-sandbox/POWER_HYPERBOLIC_MODEL_GRAM.md`§13.1 extends §13 to phi_n=C_n exp(-a_n cosh2t)Q_n with variable a_n>0. New piece: log[(cosh(b sqrt(s))-c)/(1-c)] is concave in s>=0 for b>0, -1<c<1; the numerator of x f''-f' is bounded by (1+cosh x)(x-sinh x)<0. With H(s)=cosh(2sqrt(s)), delta=H0+H2-2H1>0, a_n<=[2log phi_n(1)-log phi_n(0)-log phi_n(sqrt2)]/delta. Positive convergence at those three points bounds the scales WITHOUT convergence of derivatives; normality §13 applies again and the theta cusp excludes real locally uniform approximation. Difference: a_n->infinity evaded the earlier complex control, now it is dismissed by a discrete bound. Independent screening and re-check PASS. Only the reservation about variable positive scales of the same cosh2t base is withdrawn; not frequency changes, other factors, c outside (-1,1), sums/quotients/real powers nor abstract preservation of PSD. No new global sign, extension of T, computations, web or papers.


**2026-11-07 — Geometric BPY G2: OPEN, inconclusive diagnosis.** Source: phase211 `POWER_GLOBAL_ROUTE_REVIEW.md`, «Geometrically symmetrized BPY approximants». G_N=sqrt(Phi_N(t)Phi_N(-t)), with f_N the convolution of two exponentials per rate pi n², avoids the exponential tail of the arithmetic mean previously dismissed. Independent screening PASS, bounded; elementary formula for G2 and supertail checked. Two exploratory jet blocks gave positive numerical minima, without certificate; enumeration stopped. No all-orders Gram nor falsifier, no new positivity or T. Do not repeat the diagnosis without a new mechanism. NOT a NO-GO for this family; PSD for all N and the dominated passage to the limit remain pending. Papers untouched.


**Geometric BPY update — limit PROVED, sign OPEN (2026-11-07).** GLOBAL, «Passage to the limit of the geometric approximants»: reserving Gamma(2,pi), evaluating E exp(pi Y_N)=[2N/(N+1)]²<=4 and convolving gives f_N(v)<=4pi²v exp(-pi v). Thus G_N(t)<=2pi²exp(-pi cosh2t) uniformly in N. With the earlier convergence f_N→2pi q, absolute domination proves A[G_N]→A[Phi] locally uniformly, including all crosses of each fixed block. Closes the limit obligation of the preceding entry; not PSD of G2 nor all N, no matrix comparison from the scalar bound. Screening and check PASS; application of earlier tools to this family, no priority nor new T. Papers untouched.

**2026-11-07 — Geometric BPY: consecutive comparison with sech REFUTED for all c>0.** Source phase211 GLOBAL, «Consecutive BPY comparison with sech congruence». There is no c>0 with A[G2]>=c D A[G1]D, D(x)=sech(2x), on all real blocks. Explicit difference from consecutive coupling: an external congruence meant to correct the additional decay of the profile. Prior screening PASS limited to falsification; independent mathematical check PASS. Complete analytic proof: H(z)=z−2+(z+2)e^−z does not vanish on Re z>0 by an elementary energy identity, which defines G2 holomorphic on |Im z|<pi/4. A[G2](iy,−iy) stays uniformly bounded; A[G1](iy,−iy) has a positive lower bound and D(iy)D(−iy)=sec²(2y) diverges. Real PSD would imply nonnegative complex diagonals via jets and Taylor, a contradiction for each c. There is therefore a negative finite real block of the REMAINDER for each c, without explicit order/coefficients or computations. Not negativity of A[G2] nor of A[Phi]; other congruences undecided. The geometric limit remains proved, global sign OPEN, no new T nor changes to papers.


**2026-11-07 — BPY G1→G2: exclusion of EVERY holomorphic congruence in the strip (PROVED).** Source GLOBAL, «Extension: no nonzero holomorphic congruence transfers G1 to G2». If D is holomorphic on |Im z|<pi/4, real on R, and c>0, PSD of A[G2]−c D A[G1]D implies D identically 0. No growth, extension to the boundary nor absence of zeros is assumed. Difference from the sech factor: A[G1](x+iy,x−iy) diverges uniformly for x in positive compacts as y rises to pi/4, while A[G2] stays bounded. Jets/Taylor force D→0 uniformly on those segments; continuity, reflection and uniqueness conclude. Prior screening and independent mathematical check PASS. Does not claim PSD for D=0 nor negativity of G2, does not cover factors with a smaller strip nor non-diagonal operations. No computations nor new T; papers untouched, global sign OPEN.

**2026-11-07 — Closure of BPY G1→G2 for ANY real diagonal factor (PROVED).** GLOBAL, «Closure of the diagonal transfer: automatic regularity of the factor». For any D:R→R and c>0, PSD of A[G2]−cD A[G1]D implies D≡0, with no initial regularity hypotheses. L=cD A[G1]D is PSD and dominated by K=A[G2]; the Hilbert space of K and an operator 0<=T<=I extend L holomorphically via jets/Taylor. A strictly positive real section gives real analyticity of D. Absence of common zeros of the sections of A[G1] on Re z>0 allows gluing quotients and extending D there. The complex inequality and the earlier uniform boundary contrast force D=0. Screening and independent re-check PASS. The search for other diagonal factors, including those with a smaller strip, is closed. Does not claim that D=0 suffices, nor refutes PSD of G2; non-diagonal transfers out of scope. No computations, new T or papers; global sign OPEN.


**2026-11-07 — G2: boundary derivative energy and budget of finite branches (PROVED, no new sign).** Source phase211 `POWER_GLOBAL_ROUTE_REVIEW.md`, «G2: the boundary derivative energy exceeds any fixed collection of branches». For fixed x>0, E_x(epsilon)=integral_x^infinity 2t|G2'(t+i(pi/4−epsilon))|²dt satisfies E_x/log(1/epsilon)->infinity. The auxiliary roots H(iu_j)=0 have u_j~2pi j; the local coefficient w_j=|(G2²)'(z_j)|/4~C²d^6/(48u_j) gives contribution 4t_jw_j log(1/epsilon)+O_j(1). The sum of t_jw_j diverges: finite collection first, limit afterwards, growing collection at the end, without uniformity in j. Each fixed collection of neighborhoods contributes a fraction->0 of the full diagonal. B_x=partial_z partial_w A2(x+iy,x−iy)=E_x−|G2(x+iy)|² keeps the boundary and has the same normalized limit. Resolves the pending diagonal budget of the two-singularity screen; does NOT control the full cross, does not dismiss that minor nor prove/refute PSD of G2 or Phi. Prior screening and independent re-check PASS. Targeted cross-check Paper48/all3/primary sources, no world priority. No computations, new T or changes to papers; global OPEN.


Phase 212, consolidated map of steps 1–17: table by family, constraints on the object (clauses O11–O17 of `OBJECT_SPEC.md` §5) and ground without object or closure, in `03-research/phase-212-missing-object/MAP_ROUNDS.md`. No sign mechanism; global OPEN.
