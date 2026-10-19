# The row D crossword — complete dependency graph

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
Architect's document. Pure mathematics, no new numerics and no web. Each node cites its record file, and each
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

**(D) Row D on the declared carrier** (Paper 47 §1; Paper 48 Def; R163_401_v9 Def 1.1):

> ∀T > 0: W_T(F) ≥ 0 for every F ∈ 𝒟_T (equivalently F ∈ C_c^∞(I_T)), and, in primitive form, ∀T > 0: 𝔞_T ≥ 0 on 𝒫_T.

D is the target statement and is not compared with any external statement. The only zero statements that enter are
those of the **witness**: a quartet off the line produces a negative direction in some window (Paper 47
`lem:roughEF`, `prop:witness`, `lem:contA`), so that D ⟺ "there is no first-contact witness" (internal
reformulation, CITED). Nothing else is assumed about the zeros.

### 1.2 The members of the cluster

All are ⟺ D (REF-D). The table gives the form, the source, and the nature of the equivalence **with D**.

| # | form | source | nature |
|---|---|---|---|
| D-1 | ∀T λ^W_T ≥ 0 | Weil; P47 §1 | definition of D |
| D-2 | ∀T λ^A_T ≥ 0 | P45 Thm 10.4; Bombieri 2000 (CITED) | global only: the per-window converse fails (`cor:convfail`) |
| D-3 | ∀T there exists a flat-top certificate, i.e. Σ_ρ ŵ(τ−γ_ρ) admits a one-sided smoothing ≥ 0 | P47 `thm:Z` | PROVED |
| D-4 | ∀T v_T = (2Λ(n)/√n)_{n<e^{2T}} ∈ 𝒱_T (closed convex set defined only by Γ) | P47 `prop:finite`, `prop:uniform` | PROVED; at fixed T it is a finite, decidable condition |
| D-5 | lim_T λ^A_T ≥ 0 | P47 `cor:margin2` | PROVED |
| D-6 | Hodge index on the adelic square | P46 §5 | PROVED |
| D-7 | ∀T the Kreĭn extension problem is indeterminate | P47 Thm 8.5 | PROVED; unconditional for T ≤ 0.8 via Zhu (CITED) |
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

**I3 — W3/F3, class blindness** (Paper 48 W3; P47 Thm 12.5). Every proof whose sign step uses only a ≥ 0, supp a ⊂
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

## Editor's addendum (after R184_016)

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

## Editor's addendum: Phase 186

Sources: `03-research/phase-186-toolbox/README.md` (rounds 1–13) and entry 25 of the master grid
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

### 4. What goes into Paper 47

| item | label | destination |
|---|---|---|
| F_S unitary/involutive, A_S compact non-HS, Thm C, Thm C′, Π_S + gap, TC_S, L2_S, (84)_S, chain ∀S finite | PROVED (CC 2008.10974 and CCM 2403.01247 CITED) | section 2 "semilocal chain", DRAFT already written (round 10; CHECK_TABLE) |
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
-  AUDIT_197_2 (D1/D2): exact Bohr defect formula PROVED (+NUMERICAL); Thm 4 of D1: continuity of the defect in Λ suffices ⇒ REF-D⁺ (not impossibility). D2: defect/continuation = WP_T(Λ) ∧ sign-free rigidity (PROVED). Residues: R1 closed (continuous ⇒ REF-D⁺, discontinuous ⇒ cone/certificate); R2 = non-crossing #101. Normalization P47 v_n=2a(n)/√n to be corrected in BARRIER_001/D1/D2. No symbol changes. Row D: OPEN.

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
| half-line identity (A Thm 1.1 / C Prop 1.2 / E Thm E.1) | a single identity in three forms; W_T(Ef) = 𝒲_ext[Zr] with a killing term ∫\|Ψ\|²κ_a (correction E, P47 "Dirichlet form with killing") | PROVED |
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
| shallow data (F Prop F.5) | depth X₀ ≤ e^{1.6} ⇒ window form T₀ = ½log X₀ ≤ 0.8 ≥ 0 (Zhu Thm 1.2 CITED via P47); log-depth = full window 2T₀ | PROVED / CITED |
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

### Fase209 — FEΠ y contracciones auditadas (2026-10-19)

006/007 y audits correspondientes: FEΠ exacta conα↔1/2−α y defecto
no nulo tras borrado; móduloV_n contractivo con defectoGaussian positivo.
No implicanQ. Pendiente inversiónencompletación/forma de enlace y dominio;
no dar adjuntosambientales poradjuntosdel subespacio. ObjetivoD active.

### Fase209 — inversión008 (2026-10-19)

008/audit008: inversión ambientalU con defectoUGnU=M_bGn*;
b cambiaorientación en y=n. No igualdadadjunto ni invarianciaH implícitas.
Sucesiónprimorial de evaluación puntual tiene normaGaussian divergente,
pruebaelemental: no stronglimvertical. Clausurabilidad/invariancia/mapaQ
siguenOPEN. Resultados auxiliares no cambianestadoD ni objetivoactive.

### Fase209 — enlace continuo009 (2026-10-19)

LINK009/AUDIT009: ningún semigrupoC0 interpola n^betaV_n enlogn,
incluidoD_n. VectorX₂−1/2 prueba separación persistente a escalaslog
arbitrariamentecercanas. Se descarta ese enlace DIRECTO, noO1 niD.
CompresiónunitariaV_n tambiénexcluida; compresiónD_n no resuelta.
P44rem:nointerp amplio no se usa: SCOPE_P44009 da interpolaciónconvexa
arbitraria. Falta un mapaQ_T distinto con todas sus hipótesis; goalactive.


### Fase209 — LINK010: regularidad de una compresión de D_n (2026-10-19)

LINK_010_SPECTRAL_REGULARITY calcula, para cada observable finito centrado
no nulo A, incrementos con liminf ||D_mA−D_nA||²/log(m/n)^s>0,
s=2alpha, mediante n=1+kL,m=n+L fuera del soporte primo de A.
Toda realización D_n=P U(log n)J con mapas fijos acotados y U unitario C0
requiere momento espectral s INFINITO para JA: no Dom(|B|^(s/2)).
En alpha1/4, momento1/2 y potencia de dominio1/4. PROVED, revisión
independiente favorable en AUDIT_010. Sólo excluye compresiones con esa
regularidad; la compresión general permanece OPEN, igual que el enlace Q_T.
No se reabre la compresión normalizada009 ni se modifica el estado de D.


### Fase209 — LINK011: primer mapa continuo calculado y cotejado (2026-10-19)

LINK_011_MELLIN_GAUSS_MAP construye UF=Σ a_d(F)(X_d−1/d), con
 a_d=2∫ e^(x/2)F(x)W_d(e^(2x))dx en alpha1/4.
Convergencia enH por a_d=O_T(||F||/d), Sdd=O(d^-s); operador compacto,
featureC∞ y kernel efectivo suave. FEcoef paraFpar recupera exactamente
C(F)=∫Fcosh(x/2). No sumar el vector polar separado: diverge; cancelar
coeficientes primero. La igualdad Q_T=||UF||² en el portador continuo es
FALSA para ESTE mapa: tests polarcorregidos de alta frecuencia tienen
Q_T~logλ y||UF||→0. La dominación Q_T≥||UF||² sigue OPEN, igual que otros
mapas no suavizantes. No NO-GO generalO1, ni prueba deD. Revisión favorable en AUDIT_011.
Precisión006: no se exigen correspondenciasG/Π/v pieza a pieza; basta
identidad o dominación TOTAL sobre un core denso para norma de forma.


### Fase209 — LINK012: dominación011 refutada por test certificado (2026-10-19)

LINK_012_DOMINATION_FALSIFIER conserva exactamente el mapaU de011 y
prueba la desigualdad que había quedadoOPEN, sin reintentar la igualdad.
Test explícitoT=4/5, ω=5π/8, r=3(ω²+1/4)/(9ω²+1/4),
F=(cos3ωx+r cosωx)/sqrt(T(1+r²)), par, H0¹ y polar libre EXACTO.
CertificaciónArb128 y colasanalíticas: Q(F)<.002351, mientras el rango uno
positivo de005 da ||UF||²≥κ|Σa_dv_d|²>.26134304. Resto<−.25899.
Laplaceexacta de autocorrelación y expansiónK=2Σexp(−(2j+.5)u)
proporcionan comprobaciónindependiente sincuadraturagamma/peine:
Qupper<.001647953. Datos/códigoenLINK012_data. AproximaciónH1polarcorregida
extiende el falsificador a coreC_c∞. AUDIT_012 favorable, ambos scripts reproducidos.
Sólo escala EXACTA deU011: ninguna exclusión de reescalares pequeñas,
otros mapas/O1 niD. Esta dominación concreta ya no es un residuoOPEN.
No integraciónP47 ni cambio de celdas/conteos. ObjetivoD íntegro active.


### Fase209 — LINK013: toda escala fija deU011 falla para ventanas grandes (2026-10-19)

Diferencia nueva escrita respecto012: no cambiaU ni reintenta escala1;
calcula la respuesta del mismo mapa sobre la familia EXPLÍCITA de P47
lem:testfam aT→∞, y prueba la clase antesabierta de constantes arbitrarias.
El perfilM(F)=∫Fh cumple h(−∞)=−κ,h(+∞)=0, por sumaRiemann y Mellin
positiva de m=y^−1/2−τ. Para G_T=ω_k(x/T),k=ceil21T/e,F_T=P(D)G_T,
masaG_T/Tescapa compactos, derivadasL1 son o(T), y
M(F_T)/T→γ1²κ/8. AsíE_T≥κM²≥c0T². La prueba deP47thm:margin/cor:margin1
(CITED, inputsZ1/Z2 y fórmulaexplícita sólo para este falsificador) da
|Q_T(F_T)|/||F_T||²≤4e9Texp(−15.449T) paraESTAFAMILIA, no porinferir
un test de un ínfimo. NormF²O(T^1.5) => |Q|/E=O(√Texp(−15.449T))→0.
No existec>0 fijo conQ_T≥cE_Ten todasventanas. Cualquierc(T) eventual
requiere c(T)≤C√Texp(−15.449T); su existencia no se demuestra.
Pruebaanalítica sin nuevo cálculo numérico; AUDIT_013 favorable, inputCITED explícito.
No exclusión de otrosmapas, ni signoD nuevo. No integraciónP47/celdas/conteos.


### Fase209 — LINK014: quitar piezas positivas tampoco reparaU011 (2026-10-19)

Diferencia escrita:013 descartó una forma MAYOR porκvv*; no implicaba
falla de subformas. Aquíse prueba directamente cada pieza conMISMOa_d011.
ParaΠ, el perfil K_y(x)=2e^.5xΣWd(e2x)(qd(y)−1/d) es positivo,L1 y
∫K_y=C(y)=κΣvd(1/d−qd)>0. LocalCLTporFourier paraG_T ycotassupderivadas
=>B_FT(y)/√T→−γ1²g0 C(y)/4. Fatouen[1,2] daEΠ(F_T)≳T.
ParaG_s, G(d,2)=(1−1/√2)d^−.5 1_even; perfilh2boundedconlímites
−κ(1−1/√2)/2 y0. Riemannpares+masaescape danL2(F_T)≍T; Cauchycovarianza
=>E_G(F_T)≳T². κvv*ya daba≳T² en013. ConQ(F_T)CITEDdelpaper decreciendo
exponencialmente, TODA combinaciónfija nonegativanonula AκG+Bκvv*+CΠ
con MISMOa_d011 tiene |Q|/E→0. No constantepositivauniforme de dominación.
No inferencias de mayor a menor; nueva prueba para ambas subformas.
Sin numerics nuevos. AUDIT_014 y addendum favorables para toda la clase.
No se excluyen otros mapas, cancelacionesfirmadas ni factoresTdependientes.
ObjetivoD íntegro active/OPEN; no integraciónP47/celdas/conteos.


### Fase209 — CONSTRUCTOR015: dominio separado y cono PSD exacto (2026-10-19)

Diferencia nueva frente008: pequeños tilts positivos sobre muchos primosaltos,
no el primorial cuya normaGaussian divergía. ParaH=Σp^-s→∞,t=H^-2/3,
Z_u=∏(1+tp^-u), A=∏(1+tXp)/Z_s−Z_1/Z_s es Haarcentrado y satisface
Es|A−1|²→0, ||TA||≤C(Z_r−1)/Z_s→0,r=(s+1)/2>s, porΠdd de011.
Esto produce(√κ1,0)∈H. AccionesDnacotadas007 generan purosXd y dan
H=L²(P_s)⊕V,V=closureTA0. Tdensamente definido NOclausurable, con
sucesiónexplícita f2−(D2A_j−A_j/2)→0arith, imagen→q2−1/2≠0.
Las3formasκG,κvv*,Π son energías de3proyeccionesortogonales genuinas.
El conoPSD en su spanREAL sobreTODOA0 es exactamentea,b,c≥0.
Con014cierratambiéncombinacionesfirmadasPSDglobales deese span con
MISMOmapa011. No clasifica formas positivas sóloensuimagen niotrosmapas.
Psproducto devaluaciones, NOleyzetasobreN. NoV=todoGaussian niFEinvariancia.
Sin numerics nuevos ni inputnuevo de ceros. AUDIT_015 favorable a los tres teoremas.
No signoQ/D; objetivo íntegroactive, sin integraciónP47/celdas/conteos.


### Fase209 — LINK016: imagen par polar libre densa (2026-10-19)

Nueva diferencia frente015: ya no se suponePSDglobal; se calcula el
anulador de U_T011 sobre TODOS los tests pares polar libres. Enα1/4,
para cadaT>0, closureU_T(P_Tev)=H, tambiénparaelcoreC_c∞polarcorregido.
Prueba: ηd=<fd,h>=O(d^-1/4), c=Σηd/d converge; el perfilanalítico b_h
anuladorsatisface b_even=λcosh. Combμatómicaentera, a_n=Σd|nηd−c,a0=0;
μ'=μ−λδ0/2 es antiFourier porinyectividadGaussianenS'par (lemaentero
incluido). Fourierdecombenteraesperiódica=>μ'periodic=>constantcoeff;
Thetaμ'(1)=0 obliga0; divisorinductionηd0=>h0. No nuevo input de ceros.
Así cualquierformaHermítica Hcontinua PSDenU_T(core) esPSDglobal.
Con015+014cierratambiéncombinacionesfirmadascontinuas del span3piezas
positivas sóloenesa imagen, conMISMOmapa011. No finiteblockE_N, no formas
Hdiscontinuas, no otrosmapas/coefTdependientes ni signoQ. Auditoría favorable
independiente enAUDIT_016.md. D íntegroactive/OPEN.
