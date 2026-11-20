# The row D crossword — complete dependency graph

> **Registro cerrado.** Este documento conserva su estructura para consulta y no recibe más registros. Todo lo intentado, incluido el contenido de este documento, está consolidado en `05-meta-and-planning/ROUTES-MASTER-INDEX.md`, que es el único lugar donde se anotan intentos nuevos.

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


### Fase209 — VIRTUAL_SOURCE_017: ensayo explícito de métrica virtual (2026-10-19)

Por nueva orden del usuario se ensaya una fuente virtual calculable.
Diferencia frente008: se cambia la métrica gaussiana a y^(α−1)τ²dy;
no se afirma reparar el adjunto en el Hilbert original. S=τ conjuga G_n
a dilataciones unitarias y J_virtual a inversión exacta. El mapa unitario
C F=2^(−1/2)y^(−α/2)τ^−1F(log y/2) realiza traslaciones/reflexión.
La suma positiva de energías de saltos, más Lévy gamma, satisface en
el portador par polar libre Q_T=E_pos−(A_T−C0)||F||²,
A_T=Σ_{log n<2T}2Λ(n)/√n y C0<0. Contratermino negativo sin controlar.
La construcción funciona para cualquier perfil positivo, también borrado;
el signo virtual no selecciona los primos completos ni la FE del paper.
Diagnóstico: fuente no funcional para D; retorna a P1_BBSTAR/INV_N,
NO se presenta esa descomposición conocida como nueva ruta o avanceD.
Dominio de perfiles verificado para0<α<1. Sin numéricas ni modificaciónP47.
No NO-GO contra otras virtualizaciones; D sigue OPEN. Memo:
03-research/phase-209-nonlocal-kernel/VIRTUAL_SOURCE_017_METRIC_TEST.md.
Auditoría independiente favorable en AUDIT_017.md; identidades y alcance verificados.


### Fase209 — QRH: lectura focal y mapa condicional de exponentes (2026-10-19)

QRH_SOURCE_RELEVANCE.md y QRH_EXPONENT_MAP.md revisan las fuentes
solicitadas: Kintali47/48; OpenAI5Oct11/12; lectura estructural de
OpenAI30Sept7/8. CorregidaL74; no confundir versiones o formalizaciones.
Quanta reporta revisión humana y Lean para30Sept, no verificados aquí.
PROVED: si hay H^κ réplicas con errorO(DH^-δ) y energía total
O(D^(a+ε)H^b), H=D^h, la extracción da
θ=(1/2)max{a+(b−κ)h,2−2δh}. Sexticκ=δ=1/6,a=b=1,h=1+ϑ
recupera11/12+5ϑ/12. Esa cota no alcanza1/2 ni ampliando sóloelrango.
No se prueba imposibilidad de mejoras ni se interpolan tres fracciones.
OPEN: mejor familia/estimación selectiva y enlace exacto con déficit017.
La estimación crítica de réplicas escrita es un objetivo condicional,
NO un resultado del paper o nuestro. No signoD ni integraciónP47.


### Fase209 — QRH_REPLICA_COHERENCE: estimación selectiva examinada (2026-10-19)

Nuevo cálculo sobre las réplicas p^6 de la fuente QRH, tras consulta
del índice/grid/crucigrama. No se reabre una criba cerrada como pruebaD.
PROVED: Ap6=A1−Bp, Bp=−ν(p)Σ_(p∤m)μ(m)ν(m)W(Np Nm/D).
ParaNp≈Y=√D, conteoideal da |Bp|≪√D y varianza media≪D.
Identidad exacta Esel=|A1−barB|²+VarB. El control sin centrar
Esel≪D^(1+ε), para todoε, equivale a |A1|≪D^(.5+ε), para todoε,
con renombreε. No se probó control nuevo del componente coherente.
Revisión independiente favorable tras precisar estos cuantificadores.
ActualizadoQRH_EXPONENT_MAP: la condición suficiente propuesta era
también necesaria enesta familia; no se cuenta como mejora de cancelación.
No NO-GO general, no equivalenciaexternaD, no integraciónP47; D OPEN.
Memo:03-research/phase-209-nonlocal-kernel/QRH_REPLICA_COHERENCE.md.


### Fase209 — continuación de la media coherente QRH (2026-10-19)

Añadido ataque directo enQRH_REPLICA_COHERENCE.md, con revisión
independiente. Exactamente C_D=ΣμνW w_D, w_D=1−r_D/J∈[0,1].
ParaD>(8v)²,r_D≤2 sobreelsoporte; máscara cercana1 sinoscilaciónnueva.
Bp=−ν(p)A1(D/Np)+O_W(1), conWfijo y resto uniforme: mejorar
la escala corta reduceelerror pero no controlala señal larga.
Al expandir|C_D|², diagonal≪D porconteo; offdiagonal real aún sin
cota superior≪D1+ε. No se obtuvo estimación crítica deC_D, no se
relanzanVaughan/cribasgenéricas ni se declaraNO-GOgeneral.
Este diagnóstico no es un avancepositivoD ni prueba de cancelación.


### Fase209 — QRH7/8 y proyección hiperbólica (2026-10-19)

QRH_HYPERBOLIC_PROJECTION.md, revisión independiente favorable.
Diferencia frenteGreen/modeloshiperbólicosyaindexados: normaproyectada
exacta, frecuenciayposicióninflexión; no nueva fuente ni reapertura.
PROVED enL²par polarfreeb=.5: para0<a<bfijos yγfijo,
||P_bcosh((a+iγ)x)||²/||cosh((a+iγ)x)||²→
[(b−a)²+γ²]/[(b+a)²+γ²]. En a3/8,γ0: razón1/49,
normaresidual²~(2/147)e^(3T/4). La atenuación desaparece aaltas
frecuencias, tambiénparaT fijo. CotaexactaCauchysobremomentos.
Perfilrealcorregido tieneinflexión positivaenT−8log(128/63)+o1
para a3/8b.5, yotra simétrica. Coshmismaesconvexa globalmente.
SeptLemma20.2 certifica49/440640 enexponentecompensado, no margenD.
Franja7/8noidentificafluctuaciónconcosh3x/8 ni daamplitud/signo.
Sincontroldelcontratermino017, sinestimacióncríticanuevaniintegraciónP47.
Es cota geométrica/modelodiagnóstico, no avancepositivo de signoD.


### Fase209 — ensayo aritmético QRH4/5 (2026-10-19)

QRH_FOUR_FIFTHS_ATTEMPT.md, revisión independiente favorable con
alcancecondicionalexplícito. Usuario pideadaptar pruebaSept30, no sólo
modelo hiperbólico. Localmente, mismas identidadesEuler danH−1=O(Q^-87/50)
en caja x≥4/5,z≥33/200,w≥19/20; multiplicadorprincipal−1+O(Q^-4/5).
Noesextensióndetodaprueba. Cota baja publicada3/16 deja déficit3/40.
Alensayargeometría libre conservando majoraciones, aparece pérdida
(5ell−1+d)_+/4 en norma cuadrada completada; trasCS/sumatuplas,
σlow=11/12−ell/4+(5ell−1)_+/8, mínFORMAL13/15 enell1/5.
Así elcertificadoactual no llega4/5 variandosólo longitudes; necesita
almenos1/15 adicionalenexponentebajo (no suficienteparaalta).
No teorema13/15, no barrerauniversal, no cierreD. Candidatoescalar
ell1/5,b1/10,lx7/20,ly9/20,h17/20 pendientevalidaciónglobal.
No se usaX'≥1 comohipótesispublicada ni se confunde CII=s−11/16
con CI=s−2/3. Geometría/hightestsfueraoriginalsiguenOPEN.


### Fase209 — goalQRH4/5 y validación baja/alta (2026-10-19)

Usuariofija nuevoobjetivoexplícito: pruebaRe(s)>4/5; create_goalactive,
no conseguido porresultadosformales/intermedios, no equivaleacierreD.
QRH_LOW_CANDIDATE_VALIDATION: cota11/60paraell1/5,b1/10 bajo
lemmasexternosdeclaradosCITED; soportes,máscaras,perfilesuniformes revisados.
QRH_HIGH_CANDIDATE_AUDIT: mismosupplyslots pasa;certificadodelpiso
no cierra (49/1500 enextremo13/15). Jointformalinf167/192, no teorema
niNO-GOuniversal. Kappa dinámicofuera18.1requiereatención, pero
puedeensayarsekappa3/4coninputbeta*≤7/8; no declararbarrerainevitable.
GOAL_QRH_FOUR_FIFTHS_STATUS.md recogeobjetivo,estadoytrabajopendiente.
Revisiónindependiente de cálculos;ningunanueva regiónlibreprobada.


### 2026-11-04 — Casos elementales de potencias

PROVED, con revisión independiente: `03-research/phase-211-sign-sandbox/POWER_CONE_001.md`, signo exterior en cada plano de dos potencias con exponentes >=32 (no envolvente, no PW_N). FALSIFIED: cosh positivo/logconvexidad implica signo de mezclas; H=3+cosh y vector (42,-41) dan -129/(34 log2). No es contraejemplo al dato aritmético. OPEN: P3, todos los órdenes y puente en norma de forma, en `PROPOSAL_POWER_CASES_2026_11_04.md`. Antecedentes Pick conocidos; novedad acotada al lema explícito. `NEAR_CASES_RESULTS_2026_11_04.md`: mejora auxiliar nearfree y contraejemplos a monotonía por contacto/ciclo automáticamente favorable; ningún NO-GO global.


### 2026-11-04 — Goal activo: potencias, ronda 002

`POWER_AUDIT_002.md` confirma normalización y polarización. `POWER_THREE_002.md`: PROVED/revisado caso de tres tasas en [u,3u], u>=2^30; extensión constructiva a n tasas con u>=2^{40n} y obstrucción cuantitativa a densidad (§§7–8 aprobados por revisión independiente). `POWER_BRIDGE_002.md`: puente en norma fraccionaria ponderada a PW_N; revisión independiente favorable §§1–5. La familia fija a=32+k es densa para transportar el signo si TODOS sus órdenes son positivos. Por ello el obstáculo del puente deja de ser el objetivo principal: resta signo a todos los órdenes de una misma familia densa. Umbrales crecientes con n no bastan por concentración. Objetivo siguiente: matrices K_ij=(L(32+i)+L(32+j))/(63+i+j), sin confundir casos finitos con cierre. No se modifica ningún paper.


### 2026-11-04 — Potencias, ronda 003 (revisada)

`POWER_STATE_003.md` resume registro vigente. PROVED/revisado: puente para PW_N y test compacto mediante Möbius finito, familia fija32+k suficiente; seis órdenes de `POWER_FIXED_GRID_003.md` certificados en Fraction con restos y reejecución independiente. `POWER_POLYNOMIAL_003.md`: identidades exactas Jacobi, sin signo uniforme. `POWER_SCHUR_003.md`: F=(z²−z+10)/10 tiene F creciente y F/z decreciente en[1,3], pero detK(1,2,3)=−13/270000; falsifica inducción desde pares/monotonías, no dato aritmético. La concavidad tampoco basta (falsificador por tramos§7). Próximo: caso confluente y auditoría de movimiento de tasas; monotonía sólo hipótesis a probar/refutar. P3 general y todos órdenes siguen OPEN. No hay cierre global ni edición de papers.


### 2026-11-04 — Potencias ronda 004: P3 completo PROVED

`POWER_STATE_004.md` es estado vigente. `POWER_POLE_MOVEMENT_004.md`+`POWER_CONFLUENT_004.md`, revisados en `POWER_AUDIT_004.md`: Q[Σ_{i=1}^3 c_iX^{-a_i}] >= ||Σc_iζ(a_i)e^{-(a_i−1/2)y}||²/20 para TODOS a_i>=32, sin separación/cota superior. Incluye P3 A>=32,h>0 y triples desiguales. Insight probado: cambio de polos repondera densidad por R(|τ|) creciente; covarianza positiva con m da monotonía de todas eigenenergías ARQUIMEDIANAS. Certificado confluente >.1 y pérdidas peine<.003, polar negativo<.042. Próximo: orden4 conservando polar positivo; no se traslada automáticamente movimiento a forma completa. Todos órdenes siguen OPEN; papers intactos.


### 2026-11-04 — Potencias rondas005–006, verificadas

Estado vigente `POWER_STATE_006.md`. PROVED/revisado: confluencia4 a32, W>norm²/5 aunque ARCH admite vector<−norm²/10 (`POWER_CONFLUENT_FOUR_005`). Derivada individual ARCH+POLAR>1/420 para todo numerador grado<4 en confluencia31.5, SOS racional (`POWER_POLAR_MOVEMENT_005`, auditoría005); sólo LOCAL. Test12 explícito: AP<−norm²/100; todos contactos positivos, n2solo repara; W>norm²/50. Borrar SOLO contacto2 conservando potencias4,8,... produce W<−norm²/125 (`POWER_ARITHMETIC_WITNESS_006`, auditoría006, cola restante<norm²/500). Son casos concretos nuevos, no novedad de necesidad aritmética general ni cierre. Todos órdenes y cuádruples arbitrarios siguen OPEN.


### 2026-11-04 — Potencias007: límite exacto del transporte arch+polar

`POWER_HIGH_ORDER_PM_NOGO_007.md`, revisado en `POWER_AUDIT_007.md`: para numerador1 con n=2^17 polos confluentesu=63/2, el Rayleigh AP disminuye al aumentar cualquiera de los polos (u∂_jE<−140/(31n)). Prueba escalar con0<=τm'(τ)<4 y polar exacto; ningún espectro enorme calculado. FALSIFIED sólo la monotonía numeratorfixed AP para todo orden en tasasaltas. NO es falsificador de λmin, ni del signo, ni del movimiento ARCH, ni del teorema local4. Por ello no extender ese mecanismo a todos órdenes; falta tratar cancelación conjunta con peine o una propiedad más débil que preserve signo.


### 2026-11-04 — Potencias007–008: bloque aritmético y patrón contrario

`POWER_STATE_008.md` es estado vigente. PROVED/revisado en `POWER_BLOCK_AUDIT_007`: W>norm²/10000 para TODO bloque Laguerre de dimensión 12 en tasa31.5, todos contactos/cruces (`POWER_ARITHMETIC_BLOCK_007`, verifier Fraction PASS independiente). ARCH+POLAR indefinida allí; contacto 2 repara matriz y cola norma<.0006. PROVED/revisado en `POWER_AUDIT_008`: f=(D²−.25)[y^(n−1)e^-31.5y], n=2^17, polar nulo, ARCH<−3.83norm², TODOS contactos primos <=1024 perjudican. No se afirma signo negativo de W: la cola está abierta. Refuta patrón universal de contactos bajos reparadores, no nuevo NO-GO global sobre peines finitos. Cuádruples arbitrarios, todos los órdenes y signo del Paper 47 OPEN; puente sí PROVED. Papers intactos.


### 2026-11-04 — Potencias009–012: hasta siete polos arbitrarios

`POWER_STATE_012.md` es estado vigente. PROVED/revisado: todos los espacios de4,5,6,7 polos reales>=31.5, incluidas multiplicidades, tienen W>c||f||² con c=2/25,1/100,1/25,1/500 respectivamente (`POWER_FOUR_GLOBAL_009`, `POWER_FIVE_GLOBAL_010`, `POWER_SIX_GLOBAL_011`, `POWER_SEVEN_GLOBAL_012` y auditorías). Verificadores Fraction PASS independientes. Nuevo paso: transporte exacto de margen por filtro, déficit espectral localizado y traza ponderada máxima en confluencia (`POWER_COMMON_TRANSFER_010`). NO se afirma monotonía AP ni del mayor eigenvalor ponderado. Puente a todo dominio sí probado, pero exige todos los órdenes, aún OPEN. `POWER_TATE_CHAIN_009` da segunda diferencia exacta de la suma completa; convexidad abierta, límite E0 ya conocido, familia individual no densa. Papers intactos.


### 2026-11-04 — Potencias013: límite de la cota puntual en orden ocho

`POWER_DEFICIT_LIMIT_013`, `POWER_DEFICIT_AUDIT_013`, verifier Fraction PASS: un vector racional da margen baseAP8<1/25, pero la pérdida uniforme puntual directa obligatoria supera1/20 (evaluaciónτ4, m4<−2/5), para cualquier c>=0. Incluye la mejor cota del producto completo, no sólo máximos separados. FALSIFIED la posibilidad de cerrar8 mediante ese criterio que descarta la ganancia positiva, aunque se optimicen constantes. NO se afirma AP/Wnegativa ni imposibilidad de otro transporte. Pivot autorizado: conservar integral firmada/estructura espectral, no repetir optimización puntual. Global7 sigue PROVED; todos los órdenes OPEN.


### 2026-11-04 — Potencias014: ocho polos arbitrarios y puente confluente

`POWER_STATE_014.md` vigente. PROVED/revisado: W>||f||²/1000 para TODOS los espacios de ocho polos reales>=31.5, multiplicidades permitidas (`POWER_SIGNED_TRANSFER_014`, `POWER_SIGNED_AUDIT_014`, verifier Fraction PASS reproducido). TEL descompone la corrección firmada en energías de nueve polos con numerador cero en0; su ARCH restringida confluente>1/4 permite superar013 sin cota puntual. `POWER_CONFLUENT_BRIDGE_014`, revisado independientemente: todos los bloques de una sola tasa bastan por densidad fuerte H1 ponderada; NO requiere margen uniforme en tamaño. `POWER_PRIME_TRANSFER_014`+auditoría: Wfv−R0Wfu=(1−R0)WG exacta con TODOS contactos/polar; falta probar signo de correcciones en todo orden. No extrapolar ocho/bloque12 a todos. Papers intactos.


### 2026-11-04 — Potencias015: mezcla completa y cola uniformemente positiva

`POWER_STATE_015.md` vigente. PROVED: `POWER_GEOMETRIC_TRANSFER_015` expresa transporte por mezcla positiva absolutamente convergente de W[Q^k f], incluidos polar y TODOS contactos; pesos de Rayleigh incorporan normas. PROVED: `POWER_HIGHPASS_015`, auditado en `POWER_HIGHPASS_AUDIT_015`, para cada u>1,N fijos, W>0 en TODO Q^k V_N para k suficientemente grande, uniformemente en numeradores. ARCH/norma² >=.5logk-C_N; peine completo y polar/norma² tienden a0. Diferencia nueva: se conserva energía firmada completa y se controla su cola mediante matrices Gram, evitando el déficit puntual013 y los patrones falsificados007–008. Queda segmento inicial sin signo ni extremo efectivo; no hay uniformidad en N ni cierre global. Ocho polos arbitrarios sigue PROVED. Papers intactos.


### 2026-11-04 — Potencias016: defecto exacto, interior binomial y límites del descenso

`POWER_STATE_016.md` vigente. `POWER_DESCENT_016`: PROVED Wf=WQf+WLf completo y diferencias finitas eventualmente positivas a orden fijo. Pesos binomiales exactos siguen p=tau²/(u²+tau²); borde cubierto015 pierde masa Y energía, interior conjunto permanece OPEN. `POWER_JOINT_SCALE_016`: PROVED Beta(k+.5,N−.5) para P1, contactos->cos(u sqrt(c)t) si k/N->c; media temporal (N−.5)/u independiente k y varianza explícita. FALSIFIED uniformizar desaparición de contactos en cono lineal y pesos exponenciales fijos en N en cualquier cono; NO falsifica conos de signo. `POWER_DESCENT_AUDIT_016`: momentos nulos impiden densidad fuerte de colas incluso hacia datos primitivos; k creciente sólo admite límite fuerte0 en peso común. W−4norm² conserva estructura+eventual pero inicial negativo (verificador Fraction PASS): NO-GO sólo inferencia estructural. Diferencia nueva respecto015: localizar masa y energía pendientes, no repetir cota de alta frecuencia. Global OPEN; ocho polos sigue PROVED; papers intactos.


### 2026-11-04 — Potencias017: puente escalar por coeficientes positivos

`POWER_SCALAR_BRIDGE_017.md`: prueba escrita, revisión conceptual independiente por mapa y signo; auditoría formal de ronda en curso. PROVED algebraicamente: signo de TODOS los átomos s^k/(s+u)^(N+k), N>=1,k>=0, basta para todos los bloques confluentes. Densidad racional = peso base por R(q)>=0 en[0,1]; R+epsilon admite expansión Bernstein EXACTA de grado elevado con coeficientes positivos. Identidad racional conserva polar al evaluar x=-1/4 y todo peine; epsilon->0 controla cruces sin inferir positividad de una envolvente desde una unión. Diferencia explícita: uso cónico de densidades, no densidad de colas refutada016. Lema clásico de elevación de grado no se presenta como nuevo. Tabla escalar completa OPEN; NO certifica ninguna ventana nueva T>log(5)/2. Construcciones adicionales017 en revisión; papers intactos.


### 2026-11-04 — Potencias017: fila infinita y cono cuadrático con peine completo

`POWER_STATE_017.md` vigente. PROVED/revisado: `POWER_INTERIOR_017` cubre N1, TODOS k>=0,u>=31.5 con W>4norma²/3 (verificador Fraction PASS); WRN ofrece cota efectiva de norma ponderada por cada N para todos k, no signo general. `POWER_QUADRATIC_017`: para cada c>0, P1 tiene W>0 para TODOS k>=cN²,N>=N0(c) explícitamente acotable. Nuevo método: desplazar DENSIDAD racional conjunta, no separar normas temporales; envolvente Ce^-t suma TODO peine y permite perfil gaussiano aritmético completo. Difiere del paquete E0 y evita obstáculo016; no se omite polar. `POWER_SCALAR_BRIDGE_017` revisado íntegramente por dos revisores: TODOS N,k escalares bastan para todas las matrices por identidad cónica Bernstein de densidades y polar racional. Tabla completa OPEN; no nueva ventana T certificada. Extensión numérica del cono en revisión aparte. Papers intactos.


### 2026-11-04 — Potencias017: cono numérico explícito desde dimensión dos

`POWER_QUADRATIC_EXPLICIT_017`: PROVED, prueba completa revisada independientemente por root y verificador Fraction PASS. A u31.5, P1, TODOS N>=2 y k>=10000N² satisfacen W>49norma²/50. Desplazar densidad a Imz15 da autocorrelación<5e^-15|t|; peine completo y polar <norma²/1000 cada uno, ARCH>99norma²/100. Diferencia respectoQUADRATIC017: elimina N0 desconocido/conservador mediante banda más ancha y normalización exacta. No afirma cono para todo numerador ni signo debajo de la parábola. Con la filaN1, resta en el blanco escalar suficiente N>=2,0<=k<10000N². No ventanaT nueva certificada. Revisión adicional APROBADA por mapa y signo (POWER_INTERIOR_AUDIT_017 §9 y POWER_QUADRATIC_EXPLICIT_AUDIT_017); papers intactos.


### 2026-11-04 — Potencias018: primeras dos diferencias y presupuesto del error

`POWER_STATE_018.md` vigente. `POWER_TABLE_DESCENT_018`: PROVED/revisado por root y mapa, verificador Fraction PASS, W>norma²/8 en filas N2,N3 para TODOS k>=0,u>=31.5. Recurrencia completa da primera y segunda diferencias estrictamente positivas de fila1, no completa monotonía. Conserva paridad polar y TODO peine mediante WRN. `POWER_LOW_TABLE_018`: presupuesto exacto D_N(theta)=2+2theta J_N(theta−.5), D_N(0)=2, crecimiento sqrtN en.5 y exponencial para theta>.5; endpoints y regímenes revisados. Sólo cuantifica pérdida conocida de cotas absolutas, no signo nuevo ni NO-GO global. Región suficiente restante N>=4,k<10000N²; no ventanaT nueva certificada. Papers intactos.


### 2026-11-05 — Auditoría018 y falsificador del descenso estructural

`POWER_TABLE_AUDIT_018` guardado y revisado por root. Aprueba filas23 y LOWbudget. Modelo explícito V=2norma²−u|F(iu)|²/100 conserva recurrencias/mezclas, márgenes de todos los espacios de hasta12 polos>=u, filas1/2/3 completas y cono k>=10000N², pero V tiene entrada negativa N40402,k40401. Prueba elemental mediante medida arcoseno menos átomo en1/2 y coeficientes binomiales. Diferencia respectoW4 de016: preserva también las regiones y márgenes positivos conocidos. NO es W ni conserva su dato aritmético ni perfil logarítmico exacto. NO-GO sólo inferencia estructural basada en esas propiedades; signo real OPEN. Próximo paso exige desigualdad aritmética firmada. Papers intactos.


### 2026-11-05 — Potencias019: transición firmada del peine y media de dilataciones

`POWER_STATE_019.md` vigente. `POWER_ARITHMETIC_DIFFERENCES_019` PROVED/revisado: autocorrelación k1 con raíz positiva única para TODO N y frontera O(sqrtN); TODOS los contactos ayudan para1<=N<=211,u>=31.5, peine completo>0. En k0 peine<0 paraTODON; no implica signo W. Verificador Fraction PASS reproducido por root y mapa. `POWER_SIGNED_MEAN_019`: B(x)=log(n!)−xHn+n<=−(1−log2)(x−1) da media firmada negativa de dilataciones; identidadEuler conocida, aplicaciónkernel específica. Inversoadjunto mu(m)mH(mx) exacto; prefijo3 negativo paraN>=2^17, SIN conclusión sobre inversocompleto. `POWER_SIGNED_AUDIT_019` aprueba ambos. CoberturaW no ampliada: filas1/2/3+cono017; global y nuevasventanasT OPEN. Papers intactos.


### 2026-11-05 — Potencias020: inverso completo exterior y déficit del primer contacto

`POWER_STATE_020.md` vigente. `POWER_INVERSE_KERNEL_020`: PROVED H_N/4<=h_N<=7H_N/4 para TODOS N>=2,logx>=(N−1)/30, con cola Möbius COMPLETA dominada mediante coeficientes positivos. N2 inverso positivo paraTODOx>=1. Parte negativa potencial localizada en intervalo explícito; emparejamiento interior OPEN. Diferencia respecto019: no prefijo sino suma completa. `POWER_SIGNED_BALANCE_020`: PROVED ARCH+POLAR+P2<−.66norma² en N211,k1,u31.5; contactos restantes positivos no omitidos y W no decidida. Refuta reparaciónporprimercontacto, no todopeinefinito. Ambos verificadores Fraction PASS root/mapa; POWER_BALANCE_AUDIT_020 aprueba. No nueva coberturaW ni ventanaT; papers intactos.


### 2026-11-05 — Potencias021: balance de un átomo y cola aritmética completa

`POWER_STATE_021.md` vigente. `POWER_CONTACT_BALANCE_021`: PROVED en N211,k1,u31.5, ARCH+POLAR+P2+P3+P4<−.21norma²; y0<sum_(q>300)Pq<5e−13norma². Verificador Fraction PASS root; cola analítica por unimodalidad/derivada logarítmica/recurrencia de integrales, sin enumeración extra. NUMÉRICO45/65dps: parcial hasta300≈−6.0812e−14, errorcuadratura no certificado; NO intervalo deW ni signo deducido de esa cifra. Nueva razón respecto020: magnitud de varios contactos y bound de cola completa en el mismo punto; no campañaN. CoberturaW y ventanasT sin cambios; global OPEN; papers intactos.

Auditoría independiente021 completada: `POWER_CONTACT_BALANCE_AUDIT_021` aprueba FAIL234/TAIL y conserva NUMÉRICO el diagnóstico parcial; sin signo de W deducido.


### 2026-11-05 — Potencias022: inverso Möbius completo negativo en un punto

`POWER_STATE_022.md` vigente. `POWER_INVERSE_INTERIOR_022` + `POWER_INVERSE_INTERIOR_AUDIT_022`: PROVED −2/3<h128(1)<−33/50; verificador Fraction reforzado PASS root/mapa. Segmento m<=64 y COLA COMPLETA<1e−10; diferencia respecto019prefix y020outer: falsificador del inverso completo en región interior. Por continuidad hB adverso cerca1; exterior positivo020 permanece. FALSIFIED sólo h_N>=0 global, NO W ni ERR. Pivot: primitiva exterior y condiciónmásdébil K=J+xh, aún en investigación. CoberturaW y ventanasT sin cambios; papers intactos.


### 2026-11-05 — Potencias023: criterio compensado y peso celular firmado

`POWER_STATE_023.md` vigente. `POWER_CUMULATIVE_INVERSE_022`: PROVED masa sumJ(n)=1, criterioCONDICIONAL K=J+xh>=0⇒ERR<=−2(.75−log2)(1−J1), y representación ERR=−2intK C_B con C_B>0, cota exterior(.75−log2)/2 y daño de borde<=delta²supK^-. No compensaciónW inferida. `POWER_CUMULATIVE_TEST_023`+auditoría: PROVED −1/250<K129(1)<−1/251, suma COMPLETA ycola<1e−10, FractionPASSroot/mapa. FALSIFIED K>=0universal, aunque K128(1)>0; no ERR/Wnegativeclaim. Razón nueva: condición compensada tolera hnegativo y se prueba separadamente del criterio022 ya refutado. CoberturaW/T sin cambios; papers intactos.


### 2026-11-05 — Potencias024–025: media aritmética completa favorable pese al kernel negativo

`POWER_STATE_025.md` vigente. `POWER_CELL_BALANCE_024`: presupuesto celular uniforme tolera K^-; no dominio favorable universal afirmado. `POWER_CELL_TEST_024`: PROVED S129(2)>.33 y primera celdaKC_B>.31, integrales polinómicas exactas y suma Möbius completa. `POWER_INVERSE_LOGCONCAVITY_025`: cocientes coeficientes D_N decrecientes⇒logD cóncava TODOS N. Chequeo racional D129'(2/3)<30D129(2/3)⇒K129>0 paraTODOx>=2⇒todas celdasrestantes positivas. Combinado: ERR129<−.66 COMPLETO, no prefijo. Verificadores Fraction PASS root/mapa, auditorías024/025 aprobadas. Diferencia nueva vs023: integración compensa K129(1)<0 y corte mejorado usa logconcavidad específica, no positividad puntual falsa. ARCH_sharp pendiente; NO nuevo W/T. Papers intactos.


### 2026-11-05 — Potencias026: corte uniforme y kernel conjunto firmado

`POWER_STATE_026.md` vigente. `POWER_UNIFORM_CUTOFF_026`: PROVED dos cortes analíticos t_J y t_R para TODOS N, de orden (N−1)/330 frente al anterior (N−1)/30; suma Möbius COMPLETA K positiva fuera del corte y celdas exteriores favorables. Rango uniforme TODOS2<=N<=129,x>=exp(2/3), por monotonía y extremos, no certificados por fila. Diferencia nueva vs025: Jensen de coeficientes y barreras Riccati eliminan chequeos por dimensión. `POWER_ARCH_CELL_026`: ARCH_sharp129<−.81; beneficio garantizado .66 insuficiente, SIN conclusión W<0. Identidad conjunta W/norma²=intK Omega conserva todas las cancelaciones, pero Omega(3/2)<−.1: FALSIFIED sólo positividad puntual del peso conjunto. Restricciones gamma reales aún disponibles. `POWER_ARCH_CELL_AUDIT_026` aprueba ambos; dos verificadores Fraction PASS root/mapa. CoberturaW/T sin cambios; interior y signo global OPEN; papers intactos.


### 2026-11-05 — Potencias027: contribución conjunta exterior y su magnitud

`POWER_DISCRETE_BALANCE_027`: prueba leída por root y verificador Fraction reproducido PASS; revisión independiente APROBADA en POWER_JOINT_AUDIT_027. Fórmula completa de Omega por pisos y bound Omega(t)>=ell−(4logt+9)/t, ell=1+gamma/2−log(4pi)/2>1/50; por tanto Omega>9/1000 para t>=4096 fuera de singularidades integrables. Con corte gamma026, TODA cola conjunta int_T^infinito K_N Omega es positiva para T>=max(4096,exp(tau_N)), con mayorante explícito. En el único N129: 0<cola4096<10^-36. Diferencia vs026: desigualdad para contribución real de W, no sólo ERR ni identidad; la cota de magnitud impide atribuirle compensación grande. Masas sumK(n)=3/2 y sumK(nx)=x^-32D(logx) registradas como identidades conocidas de inversión, no prueba de signo. Interior y W global OPEN; coberturaW/T sin cambios; papers intactos.


### 2026-11-05 — Potencias027: restricción gamma y dirección de Jensen

`POWER_STATE_027.md` vigente. `POWER_INTERIOR_CONSTRAINT_027`: mezcla de calor REAL ya conocida018, ahora peso positivo específico L_N(a)=E(V_N−a)_+−(EV_N−a)_+ para el resto respecto a gaussiana de igual segundo momento. Identidad completa Wgamma−G_W(EV)=int L_N G_W'' conserva todas las piezas. Masa L=VarV/2 sólo N>=3; N2 tratado sin varianza. ARCH_sharp estrictamente cóncava da cota SUPERIOR, refutando el sentido inferior propuesto. G_W''(a)<0 para TODOS a>=65536 refuta convexidad global del funcional real, NO W ni signo del resto específico. Diferencia explícita: ley inversa gamma fijada y peso de brecha, no mezcla arbitraria ni rebranding heat. `POWER_JOINT_AUDIT_027` aprueba ambos memos027, verificadores PASS root/mapa. Interior, coberturaW/T y signo global sin cierre; papers intactos.


### 2026-11-05 — Potencias028: cuarta fila completa de W positiva

`POWER_STATE_028.md` vigente, N5 aún pendiente. `POWER_ROW_FOUR_028`: PROVED W[f_(4,k)]>norma²/50 para TODOS k>=0, TODOS u>=63/2, con TODO el peine y polar. ARCH exacto y monotonías u/k dan>11/400; WR eta12 da peine<3/500; polar impar<1/1000, par favorable. Diferencia vs018: preservar margen de fórmula ARCH4 y cambiar peso de autocorrelación, no inferencia de recurrencias ni barrido. Tercera diferencia de fila1 estrictamente positiva como corolario, no completa monotonía. `POWER_ROWS_AUDIT_028` aprueba ROW4; verificador Fraction PASS root/mapa. Nueva coberturaW REAL: filas1..4; resto tabla N>=5,k<10000N² a u31.5. No nueva ventanaT certificada ni cierre global; papers intactos.


### 2026-11-05 — Potencias028: quinta fila completa y separación del borde polar

`POWER_STATE_028.md` actualizado. `POWER_ROW_SPLIT_028`: PROVED W[f_(5,k,u)]>norma²/25 para TODOS k>=0,u>=63/2; para k>=1 margen4/5. ARCH50(u0)<−.1 muestra por qué la condición ARCH0 positiva no basta. Nuevo argumento vs018/ROW4: k0 aprovecha polar positivo con extremos opuestos en u∈[u0,2u0], y ARCH positivo para u>=2u0; k>=1 usa covarianza desde1. Peine COMPLETO<.06, polar impar<.002, certificados racionales de extremos y monotonías analíticas. Identidad A_N1=A_N0+uA_N0' y criterio suficiente general registrados, sin extrapolar premisas. `POWER_ROWS_AUDIT_028` aprueba ambas filas, verificadores PASS root/mapa. Nueva coberturaW filas1..5; cuarta diferencia de fila1 positiva. Resto suficiente N>=6,k<10000N² a u31.5; no nueva ventanaT ni cierre global. Papers intactos.


### 2026-11-05 — Potencias029: límite del puente positivo con tasas crecientes

`POWER_SCALE_BRIDGE_LIMIT_029`: PROVED/revisión independiente mapa APROBADA. Toda densidad espectral normalizada del átomo N,k,u tiene altura<sqrtN/(u sqrtpi); el máximo decrece con k por comparación elemental de trigamma con integral midpoint, y el extremo k0 se acota por Cauchy–Schwarz gamma. Por tanto el cono de mezclas positivas con u>=C sqrtN tiene altura uniforme1/(C sqrtpi). En I=[−C/8,C/8] su masa<1/4, mientras un átomo p_(M,0,31.5) tiene masa>3/4 para M grande explícito; distanciaL1>1/2. Diferencia vs016: obstrucción del CONO de densidades con tasa variable, no pesos exponenciales a tasa fija. Impide sustituir automáticamente el puente017 por esa región; NO refuta W ni otros mecanismos. Papers intactos, signo global OPEN. Teoremas positivos de región029 aún en construcción/revisión.


### 2026-11-05 — Potencias029: positividad uniforme con escala cuadrática

`POWER_STATE_029.md` vigente. `POWER_ROW_PATTERN_029`: PROVED W>.7norma² para TODOS N>=2,k>=1,u²>=256N. `POWER_BOUNDARY_WEDGE_029`: PROVED W>.4norma² para TODOS N>=1,k>=0,u²>=4096N. Ambos con peine y polar COMPLETOS. Diferencia vs016/018: CS con pesos opuestos y comparación de coeficientes S_N cancelan el coste Neta/u; queda control por Neta²/u². ARCH por Euler+momentos beta en k>=1; cota de altura espectral y resolvente integrable cubren k0. `POWER_SCALE_AUDIT_029` aprueba tresmemos incluido límite del puente; dosverificadoresPASS root/mapa. No campañaN. NUEVA región real en tasas variables, SIN ampliación de tabla u31.5 ni ventanaT: filas1..5+cono017 siguen cobertura fija. Obstrucción del cono de densidades registrada arriba impide inferir puenteautomático. Papers intactos; global OPEN.


### 2026-11-05 — Potencias030: coste gamma–gaussiano contra la ley real

`POWER_GAMMA_BALANCE_030`: PROVED/AUDITADO, verificador Fraction PASS root/mapa. Para TODOS N>=2 a u31.5, 0<A_sharp(EV)−ARCH_sharp_gamma<=.5[psi(N−.5)−log(N−1.5)]<1/[2(N−1.5)]. Usa K_sharp<=1/t y momento EXACTO int L_N/a²=logEV−ElogV, finito tambiénN2; control constructivo O(1/N) de la pérdida real. Además en el único N2, Wgamma/norma²<.85 y G_W(EV)>.875 ⇒gapCOMPLETO contraL2<−1/40. Refuta comparar Wgamma>=Wgaussiana sin corrección, NO W negativo (filaN2positiva). Diferencia vs027: emparejamiento específico con ley real y presupuesto uniforme, no curvatura genérica ni mezcla arbitraria. `POWER_INTERIOR_AUDIT_030` aprueba; paralelo de bloque interior pendiente. No nueva coberturaW/T, compensación aritmética firmada aún OPEN; papers intactos.


### 2026-11-05 — Potencias030: compensación de un bloque real a tasa fija

`POWER_STATE_030.md` vigente. `POWER_INTERIOR_SCALE_030`: PROVED int_1^(9/4)G_N H>1/100 para TODOS N>=2^20 a u31.5 FIJO, incluyendo contacto2 adverso. Inversión adjunta de Omega cancela singularidades en enteros>1 y da H explícito con sumqLambda(q), conservando W completa. Diferencia vs026/027: bloque INTERIOR integrado real y errorgamma uniforme O(1/N), no otra cola ni signo supuesto del peso. Integralprincipal exacta>1/50, error<1/200. Primitivas H yx²H hasta5/2 negativas refutan sólo criterio de primitivas positivas; el bloque se rescata por comparación real. `POWER_INTERIOR_AUDIT_030` aprueba ambosmemos030; verificadoresPASS root/mapa. Resto desde9/4 aún OPEN; NO Wtotalpositivo ni nuevacobertura/T. Papers intactos.


### 2026-11-05 — Potencias031: prefijo adverso real, recuperación y costo global inicial

`POWER_STATE_031.md` vigente. `POWER_WEIGHTED_BLOCK_031`: PROVED a u31.5, prefijo hasta225/64<−.003 para TODOS N>=2^24; bloque hasta4>.015 para TODOS N>=2^22; recuperación entreextremos>.018 paraN>=2^24. Contactos2/3 íntegros, q4extremo cancela. I_*>=0 universal FALSIFIED, no Wnegativo; errorgammauniforme sin campañaN. `POWER_GAMMA_WEIGHT_031`: PROVED único máximoR antes2/3, q''<0, sobrepaso<=2M2/9 y TV<=1+4M2/9; W/norma²>=int_(T)^infinito I_*(e^t)(−R')dt−M2. Diferencia vs030: variaciónTOTAL real y costo adverso inicialO(1/N), no sólo bloquefinito/identidad. Promedioaritméticofirmadopendiente. `POWER_WEIGHTED_AUDIT_031` aprueba ambos; verificadorbloquesPASS root/mapa. No nueva coberturaW/T ni signo global; papers intactos.


### 2026-11-05 — Potencias032: decisión exacta del candidato211,1

`POWER_STATE_032.md` vigente. `POWER_ARCH_EXACT_032` + `POWER_CONTACT_DECISION_032`: PROVED 3.4e−15<W/norma²<4.5e−15 para ÚNICO N211,k1,u31.5 pendiente021. FórmulaARCH estable de sumandoscontrolados, EM8/corte32 conrestointegral absoluto y ancho<1e−18; todos primepowers<=512 exactos conHornerdivided yfactorq^-32, polarfracciónexacta; colacompleta positiva019 ymayorante<1.1e−15. Diferencia vs021: certificar error sincuadratura ydecidir MISMO candidato, no campañaN/cortes. Parcialnegativo300 se repara porcontactosomitidos, no por atribuirerrquad. `POWER_CONTACT_AUDIT_032` aprueba; certificadoprincipalPASS root/mapa. Nueva cobertura sóloeseátomo, no fila/vecindario/T ni cierre global. Papers intactos.


### 2026-11-05 — Potencias033: resto aritmético relativo y mezcla finita gamma

`POWER_STATE_033.md` vigente. `POWER_PRIME_BALANCE_033`: PROVED kernelreal k1 cumple w(mq)<=m^-2w(q) paraq>=5 enu>=31.5,3<=N<=2u²/9−u/3+1.5. Dcontraeρ2389/3600; identidaddivisores conb(n)corregidopor2,3,4 da paraKimpar0<S_K<=A_tail<=S_K/(1−ρ^(K+1)), yA_tail>=3600L/5989. Errorrelativoalpeine, noalresiduoW; comparaciónconARCHpolarOPEN. `POWER_COEFFICIENT_BALANCE_033`: mezclaErlangFINITA exacta conpesospositivos; −.01<E22<−.006 completo, perfilNOpositivo definido, NOcontraejemploW. Dañoindividual<.22/(N−1). Abel producepesospositivos paraT_m=ΣjE_j; TODOS T_m>=0 sería suficiente sólocolumnak0 yestáOPEN. Diferencias vs027/019: mezclafinita específica ycontracciónprobada paraaritméticareal, noidentidadescomosigno. `POWER_BALANCE_AUDIT_033` apruebaambos; verificadoresPASS root/mapa. Sin nuevacoberturaW/T; papers intactos.


### 2026-11-05 — Potencias034: nuevas filas completas y oscilación del criterioT

`POWER_STATE_034.md` vigente. `POWER_DIVISOR_COMPARISON_034`: PROVED W>norma²/40 para TODOS N>=3,k>=1,u>=31.5,u²>=225N/4; k>=2 margen3/20. k1 conserva peinepositivo019 yARCH−polar>0; higherk pagan peineCOMPLETO conCENTERED029, sin extrapolarsignoaritmético. A u31.5 cubreN<=17,k>=1; combinadoV12fijo007 completafilas1..12 TODOk. Combinado8polos014 completatambiénfilas1..8 TODOk/TODOu>=31.5. No arbitrarycrosses nuevosniTwindow. `POWER_WEIGHTED_COEFFICIENT_034`: PROVED T_m reales cambiansigno infinitasveces, porcoshREALpositivo/paridad/generador ylemadecontinuaciónde coefpositivos demostrado. FALSIFIED criterio033 T_m>=0todos e incluso eventual, NO Wnegativo ni no-go global. No reintentarpositividadporcomponentesTsincompensaciónnueva. `POWER_COMPARISON_AUDIT_034` aprueba ambos, verificadorregiónPASS root/mapa. Tabla fija pendiente k0N>=13 ycolumnasN>=18debajocono salvo211k1; papersintactos, globalOPEN.


### 2026-11-05 — Potencias035: filas1–17 completas y ley del promedio firmado

`POWER_STATE_035.md` vigente. `POWER_BOUNDARY_BALANCE_035`: PROVED W>norma²/40 para TODOS N1..17,k>=0 a u31.5 fijo. Un único terminal17,k0 tiene ARCH>−.868, polar>.911 y peine COMPLETO de módulo<.002; margen>.041. La recurrencia normalizada convexa y la columna k1 real034 completan por descenso los bordes13..16. Diferencia vs018: terminal y columna efectivamente certificados, no recurrencia aislada. `POWER_SIGNED_TRANSFORM_035`: ley positiva exacta P_d del promedio FIRMADO T_m/[m(m+1)/2], cola explícita, ventana m~sqrt(N), límite Gamma2 y costo de cualquier prefijo adverso fijo O(N^-2). No controla magnitudes ni signos en la ventana móvil; oscilación034 permanece. `POWER_BOUNDARY_AUDIT_035` aprueba ambos; verificadores PASS root/mapa. No nuevas combinaciones arbitrarias ni ventana T. Pendiente fijo desdeN18 debajo del cono salvo211,k1; signo global OPEN, papers intactos.


### 2026-11-05 — Potencias036: resto de frontera y localización de energías reales

`POWER_STATE_036.md` vigente. `POWER_RECURRENCE_BOUNDARY_036`: PROVED desde N>=18,k>=0,u31.5, energía COMPLETA del cono017 en frontera diagonal <=O(logL/sqrtL)->0; resto exacto R_L->A inicial. Momento inverso beta-binomial + upper ARCH y bounds017; novedad vs016: TODO cono parabólico creciente y energía real. Pesos de frontera detenida y masa superviviente positivos, sin inferencia de energía detenida. `POWER_MOVING_BALANCE_036`: PROVED energías polar y peine REAL COMPLETO bajo ley035 concentran m/(N−1)->1/32, mientras masa normativa tiene escala sqrtN. Inclinación beta-binomial exacta y cotas exponenciales; fase común(3969/3968)^N. CHEB elemental demostrado, sin truncar aritmética. FALSIFIED descartar colas de componentes separados usando sólo masa035; no localiza ventana del funcional firmado ni estima diferencia prime/polar. `POWER_FRONTIER_AUDIT_036` aprueba ambos; verifier constantes PASS root/mapa. Sin nuevo signo W/cobertura/T; filas1..17 de035 permanecen, globalOPEN, papers intactos. Continuación debe preservar cancelación conjunta y explicitar diferencia frente018/030/031.


### 2026-11-05 — Potencias037: dilatación crítica y agrupación finita firmada

`POWER_STATE_037.md` vigente. `POWER_ENERGY_GROUP_037`: PROVED perfil real D_N(m)=mH_N(mx_N)/H_N(x_N) tiene principal1/m y error explícito M_N(logm+log²m)/m, x_N=exp((N−1)/992). ABS-FAIL para TODOS N>=2^16 por conteo squarefree/Abel discreto, no tabla ni modelo artificial. Agrupación Möbius por Q finito conserva principal U_Q/m y error explícito con momentos divisor; condición WINDOW prueba signo de núcleo AUXILIAR, no W. Q creciente primorial hasta floor(N^(1/8)) da error<.01 para m<=exp(3N^(1/4)), N>=2^80, pero resto agrupado ABSOLUTO>1.48 frente grupo principal<.505. Refutada dominación absoluta para ESA elección, no agrupación firmada ulterior. Diferencia vs018/030/031: cotas uniformes sobre mismo perfil real, no nueva identidad sola; diferencia vs033: banda crítica1/m. `POWER_GROUP_AUDIT_037` aprueba todo, verifier ampliado PASS root/mapa. Error no sumable en infinito; complemento firmado e integración OPEN. Sin nueva coberturaW/T, papers intactos, globalOPEN.


### 2026-11-05 — Potencias038: producto firmado por Fourier y ventana ampliada

`POWER_STATE_038.md` vigente. `POWER_SIGNED_MOMENTS_038`: PROVED para N>=16,B_Q<=N/1000, TODOell real, |M_Q f_N(ell)−f_N(ell−A_Q)|<=12000B_Q/N+65sqrtN(V_Q/U_Q+1)e^-N/2000. Conserva multiplicador Möbius EXACTO, normaliza gamma con densidad positiva separada del perfil extendido firmado. Diferencia vs037: eliminaV/U del errorCENTRAL, no mero cálculo de cumulantes ni Jensen firmado. MismaQprimorial037,N>=2^80: (4/5)U/m<K_NQ(m)<(6/5)U/m en A_Q<=logm<=A_Q+sqrtN/100, longitud ampliada de ordenN^.25 a√N. Es núcleo auxiliar, noW ni ventanaT. `POWER_SIGNED_AUDIT_038` aprueba teorema/corolario, verifierconstantesPASS root/mapa, revisiónnormalizador adicionalcasos. Resto aritmético firmado infinito e integralOPEN; errorpolinómico no precisión suficiente por sísolo frenteenergíasexponenciales. Sin nueva coberturaW/T, papers intactos, globalOPEN.


### 2026-11-05 — Potencias039: inversos completos positivos desde un corte cercano a la energía

`POWER_STATE_039.md` vigente. `POWER_INFINITE_SHOULDER_039`: PROVED para TODOS N>=4e6,u31.5, h_N(x)>0 yK_N(x)>0 paraTODOx>=exp(T_N), T_N=2(N−1)v/(u²−v²),v=.5+1000/√N; T_N=(N−1)/992+O√N<(N−1)/330. Comparación con026 es del MISMO K; h se prueba también. Inclinación móvil, productoEuler INFINITO σ>1 firmado conservado enFourier, ψ<=2xelemental, normalizadoruniformec/v yperfiltrasladadopositivo. Cocientesfullh/H,K/G∈(.9Uσ,1.1Uσ) enintervalov; cola siguiente por m^-2. Diferencia vs038: noQfinito ni restocoprimoomitido, controla complemento completo enregióndeclarada. `POWER_SHOULDER_AUDIT_039` aprueba; root+dosrevisores, verifierPASS. T_N coordenadanúcleoNOventanaPaper47; interior/balanceWOPEN, sin nueva coberturaW/T, papers intactos.


### 2026-11-05 — Potencias040: patrón central real y corte a distancia constante

`POWER_STATE_040.md` vigente. `POWER_CRITICAL_BALANCE_040`: PROVED para TODOS N>=2^80,δ=N^-2,v=.5+δ,t_v=2(N−1)v/(u²−v²), fullh/H<−1/N yfullK/G>1/N enMISMOcentro. Además fullh,K positivos paraTODOlogx>=(N−1)/992+5. Diferencia vs039: factor elemental reciprocalEuler z−γz² conrest9|z|³ antesdeFourier, erroro1/N efectivo; no momentoscéntricosdivergentes ni seriesformales. NuevaCURV −2q′/t<q″<0 desdepesospolinomiales/Riccati da derivadas y margenreal. Colaδ2000/N..1000/√N enlaza039: distanciaO1 envezO√N, rangodeNexplícito. `POWER_CRITICAL_AUDIT_040` aprueba todo, verifierampliadoPASS root/mapa, curvaturaadversarialcasos. SignosnúcleosNOsignoW; interiorintegrado/ARCHbalanceOPEN. Sin nueva coberturaW/T, papers intactos, globalOPEN.


### 2026-11-05 — Potencias041: beneficio integrado en banda móvil con aritmética completa

`POWER_STATE_041.md` vigente. `POWER_ENERGY_BAND_041`: PROVED para TODOS N>=2^80, T=2(N−1)(.5+N^-2)/(u²−(.5+N^-2)^2), L=√N/100, 2∫_(e^T)^(e^(T+L))h_N B<−C_N/25600, C_N=e^(T/2)(rho/2−rho′)(T)>0. FULLMöbius+Brealsaltos, favoreceW=ARCHsharp−F pero complementoOPEN. Diferencia vs030031/040: bandaenergéticaMOVIL e integraciónfinita del factorδ−D antesabs, conbordes yerrorrelativoa MISMAescalaC controlados; noFubiniglobalcrítico. §7 prueba B=−γx−B1({x})logx+κ+E, −1/x<E<1/(2x), yboundintegrado periódico conQ2norm1/16,bordes/variación/∫|h|/x; auxiliarelementalnoWsign. `POWER_ENERGY_AUDIT_041` aprueba núcleo+append, verifierBANDPASS root/mapa. Sin nueva coberturaW/T; balancecomplemento/globalOPEN, papers intactos.


### 2026-11-05 — Potencias042: cola renormalizada absolutamente pequeña

`POWER_STATE_042.md` vigente. `POWER_RENORMALIZED_TAIL_042`: PROVED global F/2=−γ+(κ−γ/2)J1+R porMASS022 ySAWTOOTH041, con TODOSbordes/saltos. ParaN>=2^80,X=exp((N−1)/992+5), |Rtail|<=N(T+2)e^-3T/2<e^-N/1000; W=ARCHsharp+2γ−(2κ−γ)J1−2Rinside+epsilon, |epsilon|<2e^-N/1000. Diferencia vs041: errorABSOLUTO trascancelaciónGLOBALafín, no escalarelativaC_N ni suma de beneficios incompatibles. REALDECAYfullh/h′ porqT ydivisores, Q2borderXconservado. `POWER_RENORMALIZED_AUDIT_042` aprueba todo, verifierPASS root/mapa. Interiorrenormalizado yWsignOPEN; sin nuevacoberturaW/T, papers intactos.


### 2026-11-05 — Exploración043: interior renormalizado, sin nueva desigualdad

Revisión constructor/auditor de la continuación042: reunir (κ−γ/2)J(1)+R da exactamente ∫h(x)[B(x)+γ floor(x)]dx. Las medias celulares positivas de ese peso no controlan su emparejamiento con h firmado; invertir otra vez por divisores reconstruye H de INTERIOR_SCALE030. No se obtuvo un lower firmado nuevo ni se controla la variación interior mediante Q2. Etiqueta: exploración SIN AVANCE DE SIGNO, no NO-GO global ni teorema nuevo. No se creó un memo de identidades. Evitar repetir esta misma normalización como método nuevo sin una hipótesis o desigualdad adicional. STATE042 conserva el último resultado integrado. Se pasa a revisar mecanismos para la forma completa, con consulta previa del corpus.


### 2026-11-05 — Exploración043: dos pivotes descartados por antecedentes concretos

Sin nuevo resultado matemático. La lectura de BB5 como residuo abierto era histórica: CC_001_CROSS_LAG_LOG6_AND_KAPPA_HESSIAN.md (phase198, §§2,5,7; alcance enlíneas74/83) trata después Hessianκ, separación porlog6 yBochnercuatropuntos. La condición de simplicidad y la auditoría de CC4 se conservan; NO se deduce una prohibición de toda vía de dos primos. Se aclaró la remisión en la entrada BB001 para evitar repetir el intento.

El pivote theta tampoco produjo una desigualdad nueva: 103_34 ya prueba logconcavidad de la suma específica y menores cuadráticos; 103_39–42 delimitan argumentos genéricos de curvatura/hazard; 103_47 contiene las traslaciones aritméticas exactas, la cola relativa decreciente y un criterio cúbico condicional. No se promovieron esos antecedentes como novedad ni se concluyó imposibilidad global. STATE042 conserva el último resultado integrado. Nuevas exploraciones requieren otra hipótesis cuantitativa y un puente explícito a la forma completa.


### 2026-11-05 — Potencias044: chequeo de reflexión y candidato de representación

`POWER_STATE_044.md`: `POWER_REFLECTION_TEST_044` PROVED gapreal W[g_Q]−W[g_L]>3/2, u31.5, normas1; ARCH>2, polar>−.5, peineCOMPLETOgap>0. Refuta SÓLO eliminarsectorantisymétricoporreflexiónq↔1−q enpuente017; no toda subfamilia niW. Reutiliza004/018 explícitamente, sinnuevacobertura. `POWER_REDUCTION_AUDIT_044` aprueba/scriptPASS root/mapa. L55-B revisado: parpositivo explícito+slack/erroraritmético puede darlower; no se construyóparni nueva cota. No se afirma converso/equivalenciageneralniNO-GO deesa herramienta. STATE042 conservaúltimoavancedebalance; globalOPEN, papers intactos.


### 2026-11-05 — Potencias045: reparación compacta y corrección de frontera documental

`POWER_STATE_045.md`: `POWER_PRIMAL_PAIR_045` PROVED, revisión independiente en `POWER_PRIMAL_AUDIT_045`: si un par representante conserva exactamente la cola real del símbolo y sólo cambia una medida espectral PAR compacta, la identidad en TODOS los tests primitivos fuerza que la corrección sea cero. Prueba por F=(D²-1/4)phi, polarización/localización y momentos compactos; paridad esencial. En T=3/5, q_T(0)<-15/2, así ese ansatz no admite slack<=15/2. No es negatividad de W ni NO-GO de L55-B general. El subcaso no compacto con resto temporal exterior medida finita firmada retorna al dual(D) existente; no se generaliza a medidas/distribuciones arbitrarias. Diferencia respecto044: hipótesis concreta de reparación compacta, no mero cambio de orientación ni imposición artificial de masa total finita. `POWER_CONTACT_FLOOR_045` comprueba que el piso CRUDO m(240)-A2345<-1/2 falla al entrar5; ROUND026A ya evita esa limitación, por lo que no es nueva vía ni imposibilidad de otros certificados. Ambos verificadores racionales PASS constructor/root/auditor.

CORRECCIÓN DE ESTADO: Paper47 prueba hasta log5/2, pero el sandbox anterior `ROUND_026_A`, Theorem26A.2, registra PROVED/computer-assisted lambda_A(T)>=2e-26 para TODOS 0<T<=207/200=1.035. Root y auditor leyeron logs archivados de ambas paridades certified:true a mu2e-26; NO se reprodujo ahora la certificación larga. T1.098 sólo tiene builds/matriz localizados, sin certificado final hallado: no se promueve. La frontera local archivada, las cotas CITED y los resultados recientes de potencias son distintos. Ronda045 no añade cobertura W ni ventanaT; signo global OPEN y papers intactos.


### 2026-11-05 — Potencias046: exploración del interior deduplicada, sin nuevo signo

Constructor y revisor volvieron a `POWER_RENORMALIZED_TAIL_042` y al puente suficiente017. No se obtuvo una desigualdad nueva: Turán de los valores completos vuelve a la ruta de momentos/determinantes; recombinar J(1) con el residuo y efectuar la inversión completa reconstruye el peso043 o Hjoint030. Los emparejamientos con primo o Q fijo reproducen037/038. Elegir Q según la escala añade bordes de entrada y un resto firmado que siguen sin estimación. No se promovió un falsificador auxiliar del inverso de divisores de C(n), porque su positividad no era una hipótesis necesaria del intento. No hay NO-GO general ni nuevo artefacto teoremático.

Precisión de la obligación suficiente, ya consecuencia de016/036: para A_Nk=W[f_Nk]/norma² a u fijo, bastaría A_Nk>=-epsilon_N, epsilon_N->0, UNIFORMEMENTE en 0<=k<10000N² para N grande; el cono017 cubre el resto. Para cualquier epsilon, elija M con epsilon_N<=epsilon en N>=M y refine hasta profundidad L>=10000(M-1)²+M. Cada hijo con N'<M cae en el cono por su k' grande, y los demás tienen lower -epsilon. La recurrencia normalizada convexa fuerza A_parent>=-epsilon; epsilon->0 da signo. No requiere certificar excepciones finitas ni margen positivo puntual. Es una condición suficiente conocida, no una estimación aritmética ya obtenida. El resultado042 sólo aborda k0: un lower asintótico ahí no cubre toda la banda. La cota D_N>=2exp(-N/1000) es suficiente para decidir cada k0 puntual, pero no es un requisito necesario del cierre por lower uniforme evanescente.

Estado de cobertura sin cambios respecto045; signo global OPEN, papers intactos. La siguiente construcción necesita una entrada firmada adicional concreta, no otra inversión de los mismos pesos.


### 2026-11-05 — Potencias047: familia primitiva revisada, sin nuevo bound

Se comprobó el candidato H_Nk(s)=(s²-1/4)s^k/(s+u)^(N+k+2), N>=1,k>=0,u=63/2. Dos revisores y root contrastaron TATE_CHAIN009, PRIME_TRANSFER014, CONFLUENT_BRIDGE014 y SCALAR_BRIDGE017 con índice/grid/crucigrama. La adaptación Bernstein con base(s²-1/4)/(s+u)^3, más densidad014 y reparación de los dos momentos por dos racionales fijos, hace suficiente el signo de toda esta tabla para el portador PRIMITIVO. Es una adaptación del puente existente, no una desigualdad aritmética nueva; no se afirma una separación lógica estricta entre los objetivos globales primitivo/completo.

La densidad primitiva es exactamente la suma de las densidades originales (N,k+2), (N+1,k+1), (N+2,k) con coeficientes1,1/2,1/16. La identidad conserva toda W: los tres polares se cancelan por evaluación racional en x=-1/4. Hereda el cono017 para k>=10000(N+2)² y las filas N<=15 a partir de035. La recurrencia conserva pesos normalizados POSITIVOS, pero éstos son cocientes de las normas primitivas, no los coeficientes beta simples originales; su ley es una mezcla positiva de tres leyes beta. El criterio uniforme -o(1) de046 se adapta, sin aportar su hipótesis de signo.

En la otra expansión, con a=u²-1/4=992 y a_Nk=W[f_Nk] original sin normalizar, W[H_Nk]=a_Nk-2a a_(N+1,k)+a² a_(N+2,k). Es la segunda diferencia009 extendida a k variable. La anulación polar no controla el resto ARCH+peine y la mezcla positiva no fuerza un lower evanescente. No se obtuvo un bound nuevo, no se creó otro memo teoremático ni se presentó esta reducción como prueba del signo. La cobertura y la frontera documental permanecen como en045; global OPEN, papers intactos.


### 2026-11-05 — Potencias048: corolario subcuadrático y extremo restringido R12

`POWER_SUBQUADRATIC_COROLLARY_048` PROVED; auditoría independiente `POWER_SUBQUADRATIC_AUDIT_048` y revisión root. A u=63/2, para TODOS N>=exp(10^6) y TODOS k>=2N²/log log N, W[f_Nk]>(2/5)log N·norma². Extracción explícita de STRIP/PRIME/ARCH/POL017 con c_N=2/log log N: C(c_N)<=1+4sqrt(log N), ARCH crece como log N y domina TODO el peine y el polar. No se invoca uniformidad implícita de N0(c), ni límite gaussiano, ni truncamiento aritmético. Es cobertura no acotada adicional explicitada desde bounds existentes, no una nueva desigualdad aritmética. La banda inferior y el resto036 siguen abiertos; no hay nueva ventanaT.

`POWER_R12_ENDPOINT_048` PROVED y auditado en `POWER_R12_AUDIT_048`: para G en V13 confluyente con G(0)=0, E2[G]>norma²/50, donde E2=ARCH+POLAR+contacto2. Extiende una banda del certificado racional007 y verifica por congruencia/LDL12 el extremo v=u de la hipótesisR12 abierta014. Diferencia frente al falsificador universal014: aquí F0 pertenece EXACTAMENTE a V12; aquél no. Verificador PASS constructor/auditor/root. Se sigue un entorno común por continuidad, sin radio efectivo ni transporte para todosv. La cola de los demás primos no está incluida en E2; no se importa automáticamente el bound007 aV13. Para Q=s/(s+u), compresión tridiagonal de q enV12 da minEq>=1/576 y logconvexidad de normas: polar normalizado de Q^jF decae <=(9/62)^j PB12. El corte arquimediano efectivo y los bloques intermedios aún faltan; no se realizó un barrido.

Ambos resultados tienen alcance explícito. Signo global OPEN, papers intactos; frontera documental de ventanas conservada según045.


### 2026-11-05 — Potencias049: R12 uniforme resuelto en la base restringida

`POWER_STATE_049.md`: `POWER_R12_TRANSPORT_049` PROVED y auditado en `POWER_R12_AUDIT_049`. Para TODO F!=0 enV12 confluyente y TODO v>=u=63/2, E2[sF/(s+v)]>norma²/2500. AquíE2=ARCH+POLAR+contacto2. Por T2 de014 transporta coercividadE2 al mover UN polo desdeV12. Diferencia frente al falsificador universal014: se conserva exactamente la base positivaV12; no se declara una ordenación universal. R12, antesOPEN en014/048, queda resuelto en esa clase.

`POWER_CENTERED_CUTOFF_049`: centrar el polinomio del círculo y separar sectores de grados11/10 permite IBP+energía polinómica ponderada con prueba autónoma. Para TODOSj>=14 y TODOSnumeradoresV12, E[tau^-2]<1/405 y ARCH/norma²>859/800. Contacto2<norma² y polar048 decreciente pagan la cola. El corte32 inicial de HIGHPASS_CUTOFF049 queda dominado por14. Se certificó el segmento exhaustivo j1..13 mediante trece congruencias/LDL racionales12dim, error relativo aGram; el segmento fue fijado analíticamente, no por búsqueda de casos favorables. Script PASS constructor/auditor/root. Mezcla geométrica015 preserva norma y polar; |Q|<=1 y dominación de |m||F|² justifican la convergencia para cada v finito.

No se ha transportado la cola de contactos n>=3 desde007, por lo que no se afirmaWcompleto sobrelosnuevosespacios. Tampoco se autoriza iterar sobre bases intermedias distintasdeV12. Signo globalOPEN; no nueva ventanaT; papers intactos. Regiones completas048 y frontera documental045 permanecen.


### 2026-11-05 — Potencias050: W completo en todos los doce polos reales

`POWER_STATE_050.md`: `POWER_FULL_TWELVE_050` PROVED, auditoría independiente `POWER_FULL_TWELVE_AUDIT_050`, verificador completo PASS constructor/auditor/root. Para cualesquiera DOCE polos reales v_i>=63/2, repetidos permitidos, y TODO numerador real propio P, W[P/prod(s+v_i)]>norma²/10000. Incluye todos los cruces, todos los contactos aritméticos y el polar; amplía ocho polos arbitrarios014 y el bloque fijoV12 de007. Por cancelación de factores incluye los espacios de menor dimensión.

Ganancia nueva: W>norma²/250 en TODOS los TRECE polos reales>=u con numerador cero en0. Se reforzó el MISMO segmento exhaustivo j1..13 de049 a E2>norma²/50; la cola analíticaJ14 ya venceese margen. MULTI015 sobreG0=QF0 lleva todaesaórbita a13polosnum0. Trace010 conalpha1/2 da B_T13=109543953194<330975²; conservando n^(-1/4)<=10/13 desde3, la cola aritmética COMPLETA n>=3 tiene norma<2/125. ZERO13 resultante alimenta FULLTEL014, que conserva exactamente norma/polar y transmite sin pérdida la coercividad1/10000 del bloque base. La nueva entrada de signo es aritmética2 junto con ARCH+POLAR y cola infinita, no sólo ARCH.

La consecuenciaMULTI de049 también daE2positivo en todos12polos sin iterarR12; la exploración inicialFULL_TRANSFER_PLAN050(E23) quedó superada y no se ejecutó. No hay barrido de tasas/índices: segmento fijado por corteanalítico y13LDLs racionales12dim. No se afirma signo de13polos generales ni ordenarbitrario, ni nueva ventanaT. GlobalOPEN; papers intactos.


### 2026-11-05 — Potencias051: corte arquimediano lineal para todas las dimensiones

`POWER_DIMENSIONAL_CUTOFF_051` PROVED, versión corregida auditada en `POWER_DIMENSIONAL_AUDIT_051` y revisada por root. Para TODOS n>=1, TODOS F!=0 enV_n y TODOS j>=ceil(7n/6), E_(Q^jF)[tau^-2]<1/405 y ARCH[Q^jF]>(859/800)norma². Diferencia frente015/049: corte explícito LINEAL en dimensión, simultáneo en todos los numeradores, no eventualidad con constante desconocida. Con d=n-1 y r=u²E[tau^-2], (2j-1)r<=1+2sqrt[d(d+2j)r]. Se da J(n,b) explícito para r<b y cualquier margen arquimediano h>=0. Paridad y bordes se justifican por centrado y energía polinómica. Root corrigió el factor del segundo sector a(d-1)(d+2j+1), aún dominado por d(d+2j) con diferencia2j+1; los resultados finales no cambian y la auditoría reconoce la corrección.

No es nuevo signo deW. La extrapolación literal de050 con E2positiva en TODAS las órbitas y TODOS los órdenes ya la refuta PRIME_TRANSFER014: F_Tate de orden2^17 satisface E2[QF]<0. Esto exige cambiar el control aritmético de los segmentos iniciales, no descarta W completo. ZERO13positivo050 sólo deja un pivote deSchur para13polos generales; casos no halló nueva desigualdad del cruce. La reducción Toeplitz/persimétrica y el Schur son antecedentes, no se promueven como nuevo resultado. CoberturaW permanece en050; globalOPEN, papers intactos.


### 2026-11-05 — Potencias052: bloque confluyente13 completo y pivote real cuantificado

`POWER_STATE_052.md`: `POWER_CONFLUENT_THIRTEEN_052` PROVED y aprobado en `POWER_CONFLUENT_THIRTEEN_AUDIT_052`. Para TODO f∈V13 confluyente a u=63/2, W[f]>norma²/4000. Se conserva toda la aritmética: E2>.0003norma² ya positiva pero el majorante de cola desde3 es excesivo; E23>.00028norma² y TODAcola n>=4 tiene norma<.00001. LDL racional, constantes con restos y cotas por bandas; script PASS constructor/auditor/root. ÚNICO bloque siguiente motivado por ZERO13 de050, sin barrido de dimensiones/tasas.

Diferencia frente al Schur abstracto deduplicado051: se controló el acoplamiento REAL y el error de TODOS los cruces. Pivote respecto a h=ell/sqrt13,ell_j=(-1)^j: sigma(E2)∈(.0004054,.0004055), sigma(E23)∈(.0003834,.0003836), sigma(W)∈(.0003,.0005). Se encierran por orden de formas Tc±epsilonI y mínimo sobre el mismo espacio afín, no por errores independientes de una inversa. En el minimizador RACIONAL del centroE2, energías divididas por13: AP∈(.01839,.01841), contacto2∈(-.018,-.01798), contacto3<0. Son energías de una dirección de complemento fijo, NO cocientesRayleighunitarios ni afirmaciones de optimalidad exacta del vector central. Conservar3 mejora el certificado al evitar una pérdida de la cota absoluta;3 NO mejora el pivote real.

La investigación paralela de norma ponderada uniformeQ^jV_n no obtuvo boundnuevo: WRN017monomial no controlaGrammixta ytrace010 no se importa automáticamente aórbita. No se promueve un no-go general. Cobertura050 de12polosarbitrarios se mantiene; trecepolosarbitrarios yorden general siguenOPEN. No nueva ventanaT; papers intactos.


### 2026-11-05 — Potencias053: forma completa en trece polos arbitrarios

`POWER_STATE_053.md`, `POWER_FULL_THIRTEEN_053.md`: PROVED, verificador racional reproducido por constructor, mapa y root, exit0. Para TODO numerador real propio y trece polos reales >=63/2 (repeticiones permitidas), W>norma²/4000. Auxiliar ZERO14: catorce polos con numerador cero en s=0 tienen W>norma²/1000.

Diferencia respecto050/052: se retienen exactamente contactos2,3; momento matricial centrado y monotonía cubren TODOS j>=96, y los95 bloques iniciales se certifican exhaustivamente con error epsilonGram. MULTI14 transporta E23; traza14 acota TODA cola desde4 por<1/1000; FULLTEL13 conserva el margen de052. La optimización intervalar del logaritmo no cambió precisión ni umbrales. No nuevo T, no dimensión arbitraria, no cierre global. No reintentar como si positividad eventual resolviera el segmento inicial para toda dimensión.


### 2026-11-05 — Potencias054: control efectivo de coeficientes en frecuencia inversa

`POWER_INVERSE_COEFFICIENT_054.md`: COEFF/EVAL PROVED, revisados independientemente por root y mapa. Con a=u sqrt(j), R(y)=y^(n−1)P(ia/y), D=integral |R(y)|²(1+y²/j)^−(n+j)dy, se tiene norma²=a^(1−2n)D/(2pi). Para TODO n>=1, j>=n y TODO numerador, (suma|coef R|)²<=9n²9^n D; por tanto el mismo factor controla evaluación compleja y producto R(z)R(-z), con max(1,|z|^(2n−2)). Prueba elemental: peso>=exp(-2) en[-1,1], expansión Legendre, recurrencia de coeficientes y Cauchy.

Diferencia frente015/016: constante efectiva dependiente sólo de n para TODOS j>=n, evitando el menor eigenvalor no cuantificado de una Gram límite; no supone norma temporal ponderada uniforme en n. Las coordenadas por sí solas no son el resultado. Contorno completo, corte efectivo para W y segmento inicial siguen pendientes; no nueva cobertura de signo ni T. No se promueven como nuevas las reformulaciones de energía negativa036 ni la extrapolación de momentos que reproduce016.


**Actualización054 — corte completo aprobado.** `POWER_EFFECTIVE_HIGHPASS_054.md` y `POWER_EFFECTIVE_HIGHPASS_AUDIT_054.md`, PROVED/revisado por root y mapa: con C_n=9n²9^n, D_n=10C_n n!, A_n=6C_n n n! y K(n)=max(10000n²,A_n·3^(4D_n+20)), W[Q^j P/(s+u)^n]>norma² para TODO n>=1, TODO numerador real de grado<n y TODO j>=K(n), u=63/2. Contorno completo<=D_n, momentos beta explícitos incluidas ramas r=0 y r=n, extremo escalarN=1 justificado aparte; autocorrelación<=D_n exp(-15|t|)norma², peine infinito<D_n, ARCH>2D_n+9 y polar<1. No campaña ni evaluación de enteros gigantes. Resuelve el contorno/corte que la entrada054 anterior dejaba pendiente. Diferencia frente015: fórmula efectiva en dimensión variable, sin Gram límite no cuantificada. Segmentos iniciales j<K(n), signo global y nueva ventanaT siguen sin resolver; no eliminar el resto usando recurrencia036.


### 2026-11-05 — Potencias059: escala necesaria para contorno uniforme

`POWER_STRIP_NECESSITY_059.md`, PROVED por prueba analítica root/mapa: para u>0 y0<eta<u fijos, no existe D independiente de n,j que acote integral|rho_(n,j)(x+i eta)| porD integralrho sobre una sucesión n<=j=o(n²), ya conP=1. Var|tau|<=u²[j/(2(n−3/2)(n−1))+1/(2(n−3/2))]→0; elegir t_n en[T,T+2pi/u] con fase media múltiplo2pi hace la correlación→1, incompatible conD exp(-eta t_n) paraTgrande. Excluye estrategiasSTRIPuniforme enconos j>=C n^p,p<2.

Diferencia frente016: toda escala subcuadrática, incluida frecuencia central divergente, con control exacto de varianza. No Wnegativa, no prohibición de signo subcuadrático, no cota necesaria p>=3.017escalarcuadrático y054conD_npermanecenválidos. Constructor investiga producto de amplitudes sin fase causal para p>=2; comparación gaussiana global no justificada. GlobalOPEN; sin nuevoT ni campaña; papers intactos.


### 2026-11-05 — Potencias060: contorno uniforme y signo en cono n³ log³n

`POWER_STATE_060.md`, `POWER_UNIFORM_STRIP_060.md` y `POWER_UNIFORM_STRIP_AUDIT_060.md`: PROVED/APROBADO por constructor, root y mapa. Para TODO n>=1, TODO numerador real P de grado<n y TODO j>=10^12(n ceil(log_2(n+1)))^3, u=63/2, W[Q^jP/(s+u)^n]>norma². STRIP a altura3 tiene constante<2 INDEPENDIENTE de n/P; autocorrelación<=2exp(-3|t|)norma², peine completo<2, ARCH>4, polar<1 en la misma normalización.

Diferencia frente015/054: polinomios ortogonales del peso Student exacto dan FIRST200 para amplitud sin fase; los grados crecen como(n+3r,j−r). Cauchy enL² a altura15 paga sólo colaTaylor desde20nq_n conD_n054, mientras las primeras derivadas cuestan<.01porpaso. No se exponentia un generador de dimensión fija, ni se usa gaussiana global ni norma causal ponderada uniforme refutada016. SINGLE-EVAL controla amplitudes complejas; rho=H H# conserva el producto correcto fuera de la recta. CorteO(n³log³n), también válido el más débil10^12n^6; sin campaña numérica.

Índices iniciales j<J(n) y signo global OPEN. No se infiere descenso desde el cono ni una nueva ventanaT.059 no refuta este rango: sólo exige al menos escala cuadrática paraSTRIPuniforme. Papers intactos.


### 2026-11-05 — Potencias061: decisión completa del caso interior129,0

`POWER_GAMMA_129_DECISION_061.md`, `POWER_GAMMA_129_AUDIT_061.md`, `POWER_STATE_061.md`: PROVED/APROBADO, verificador racional reproducido por constructor/root/mapa, exit0/PASS. ParaG(s)=(s+63/2)^−129, W/norma²∈[13456684165,13456684168]/10^20, enparticularentre1.34e−10y1.35e−10. Caso histórico pendiente025/026/027, no búsqueda de otroN. ARCHestable032,polar racional, TODOScontactoshasta512 ycola completaADVERSA<1e−24 porROOT026q(log512)>16; sin cuadratura ni floatcomo prueba.

ARCHsharp/norma²≈−1.04219397018062543, ERR≈−1.04219397031519227, ambos encerrados racionalmente. El beneficio−ERR supera el déficit sólo1.3456684e−10; la garantía−.66 de025no era suficiente. ConCELL024, restodeceldasn>=3aportaentre.3755y.3822 a−ERR, sin dobleconteo. Se decideWdelmismotest dondeK129(1)<0, no se rehabilitaKpuntual>=0. No se infiere fila, siguienteN, ventanaT ni signo global. Papers intactos.


### 2026-11-05 — Potencias062: déficit afín y residuo completo en el mismo129

`POWER_GAMMA_AFFINE_BALANCE_062.md`, `POWER_GAMMA_AFFINE_AUDIT_062.md`: diagnóstico PROVED/APROBADO, verificadorreproducido constructor/root/mapaexit0PASS. Reusa024J129(1)completo y061ERR/ARCHsharp sinotroN/precisión/corte. AFF=ARCHsharp+2γ−(log(2π)−1−γ)J1∈[−60446492280,−60446492279]/10^12; Rcompleto∈[−30223246208,−30223246207]/10^12; W/norma²=AFF−2R. La parteafínesnegativa y la reparaciónR esesencialenESTEbalance.

RincluyeB1periódico+errorEuler, no B1solo; no usaABS-TAIL042(N>=2^80). ElenclosureRusaERR061conocido, NOesboundindependienteparadescenso;Wmantienecert061sinredondeosindependientescompartidos. No nuevoW/TniNO-GOgeneral. ComparacióndediferenciasNdeJ/K/ARCHsiguesinbound; globalOPEN,papersintactos.


### 2026-11-05 — Potencias064: escala cúbica necesaria para STRIP en todos los numeradores

**PROVED/APROBADO.** `POWER_STATE_064.md`, `POWER_STRIP_CUBIC_NECESSITY_064.md` y `POWER_STRIP_CUBIC_AUDIT_064.md`: prueba analítica revisada por constructor, root y mapa, incluida la mejora al umbral lineal j≥10^6n. Para u=63/2 y0<η<u, TODOS n≥4,j≥10^6n admiten un numerador REAL P de grado<n con ∫|ρ(x+iη)|/∫ρ≥1+η²n³/(1152u²j). En consecuencia se refuta STRIP con D independiente de n,j,P sobre TODOS los tests j≥C n^p para cualquier p<3. Elegir j=max(ceil(Cn^p),ceil(10^6n)) conserva j=o(n³) y hace divergir el lower.

Diferencia frente059: numerador variable, tomado del polinomio ortonormal Student de grado n−1; no P=1 ni extrapolación de un paquete lineal. Recurrencia β exacta con k/8≤β_k≤4k, proyección del generador060 al grado n+2 y resto racional controlado dan ||H′||²/||H||²≥n³/(2304u²j). La paridad construye P real par y ρ=H²; convexidad par de la norma desplazada produce el lower. No necesita transferencia gaussiana ni campaña numérica.

Alcance sólo estrategia de contorno ABSOLUTO: no W negativa ni obstáculo a otros mecanismos de signo.060 sigue válido en n³log³n; potencia3 necesaria para STRIP, factores logarítmicos no decididos. Interior/signo global y nueva ventanaT siguen abiertos; papers intactos.


### 2026-11-05 — Potencias065: exactamente k raíces simples y signo de la cola completa

**PROVED/APROBADO.** `POWER_STATE_065.md`, `POWER_CONTACT_OSCILLATION_065.md` y `POWER_CONTACT_OSCILLATION_AUDIT_065.md`: prueba analítica revisada por root y mapa. Para TODOS u>0,N>=1,k>=1, la autocorrelación de s^k/(s+u)^(N+k) tiene exactamente k ceros positivos simples, signos alternados desde positivo y última raíz en x=ut estrictamente menor que4k(N+k−1). Para u>1/2, TODA la cola de contactos u logq>=4k(N+k−1) tiene contribución de signo(−1)^(k+1): favorable para k impar, adversa para k par; convergencia absoluta y signo estricto de su suma.

Diferencia frente019: conteo exacto para TODO k, no otra evaluación k=1. Momentos nulos hasta2k−1 más grado resuelven N=1; filtros exponenciales unilaterales y Rolle con borde en infinito preservan ceros simples y propagan en N. La cota019 más fina para k=1 no se reemplaza. No se asume positividad total genérica ni se borra ningún primo. No se controla la magnitud frente al prefijo/ARCH/polar: sin nueva fila W, ventanaT ni signo global. Papers intactos.


### 2026-11-05 — Potencias067: el descarte positivo Selberg falla en el caso129 ya certificado

**PROVED/APROBADO.** `POWER_SELBERG_DROP_OBSTRUCTION_067.md`, `POWER_SELBERG_DROP_AUDIT_067.md` y `POWER_STATE_067.md`: revisión independiente mapa y root, sin nuevos cálculos ni otroN. Para el MISMO gamma129,u=63/2 de061, Selberg da S=U−V y W/norma²=ARCH/norma²+polar/norma²−2U+2V. El par2·2 y la mezcla real030/Jensen prueban2V>1/243. Como061 certificó0<W/norma²<1.35·10^(−10), el criterio que descarta2V tiene valor<−1/250. Incluso retener sólo1−theta de2V exige theta<6561/(2·10^11); theta=10^(−7) ya deja ese candidato negativo.

Diferencia explícita frente055/023: no se vuelve a ofrecer la identidad Selberg ni V>=0 como avance.055 dejó abierta la falsedad del criterio fuerte W/norma²>=2V; el certificado completo posterior061 ahora lo refuta en un test ya existente. Es una obstrucción a esa pérdida positiva aislada, no a Selberg completo, métodos compensados ni signo de W. No nueva fila, ventanaT o conclusión global. Nota retrospectiva incorporada a STATE055; papers intactos.


### 2026-11-05 — Potencias073: convexidad global del hazard theta y positividad de TODOS los pares

**PROVED/APROBADO.** `POWER_STATE_073.md`, `POWER_THETA_HAZARD_COMPACT_073.md`, `POWER_THETA_TWO_COPY_073.md` y `POWER_THETA_AUDIT_073.md`. Cerrado el compacto que phase103/103_43 dejaba abierto: un certificado racional de4096paneles prefijados verifica la cuarta derivada de logPhi negativa en[0,1/4], con TODOS los sumandos theta mediante cola explícita. Paridad y el outer10343 dan V'''(t)>0 para TODOt>0, V=−logPhi. Constructor, root y mapa reprodujeron exit0/PASS; no campaña ni edición histórica.

Nueva consecuencia positiva: dos copias independientes del tilt exp(ux)Phi(x) prueban M''(u)<0 y M(u)−uM'(u)>0 para TODOu>0, M(u)=L(u+1/2). La varianza condicional del semidiferencial decrece con el módulo del semipromedio; una covarianza de monotonías opuestas da el signo estricto. Así1<L(a)/L(b)<(a−1/2)/(b−1/2) para a>b>1. El criterio exacto CONE001 prueba positividad de la forma COMPLETA en TODO plano de dos potencias con a,b>1, incluyendo todos los contactos. Para a≠b la matriz es definida positiva; para a=b es semidefinida por redundancia y la función representada no nula tiene energía positiva.

Diferencia explícita: se resuelve el residuo compacto10343 y se demuestra una aplicación de dos copias que no dependía de las cinco comparaciones de tilt polinómico allí pendientes. Supera el antiguo umbral a,b>=32 de CONE001§5 en el caso de PARES; éste queda como antecedente válido, no como frontera actual. No se infiere positividad de tres generadores, todos los órdenes, su envolvente lineal ni una nueva ventanaT. Signo global OPEN; papers intactos.


### 2026-11-05 — Potencias074: la hipótesis fuerte073 no basta para tres generadores

**PROVED/APROBADO.** `POWER_STATE_074.md`, `POWER_TWO_COPY_SCOPE_074.md` y `POWER_TWO_COPY_SCOPE_AUDIT_074.md`; verificador racional exit0/PASS reproducido por constructor, root y auditor. Un potencial par POLINÓMICO V=A[x²/2+x^(2p)/(2p·2^(2p−2))], p=10^6,A=4·10^8, conserva TODAS las hipótesis073, incluso convexidad fuerte. Todos los pares positivos son definidos positivos y M''<0, pero en nodos A,2A,3A el vector(40,−40,3) da c^T Kc<−53111/(10000A). Modos controlados analíticamente y error modo-media<=1/sqrtA por integración por partes; sin cuadratura ni barrido. El jet en0 de V=x^6 se comprobó positivo mediante momentos gamma, sin ofrecerlo como falsificador.

Diferencia frente003: el contraejemplo pertenece exactamente a la clase fuerte probabilística073, no sólo a funciones cóncavas o medidas pares genéricas. Refuta ÚNICAMENTE su promoción automática a orden3; NO Phi real ni W. Los TODOS PARES reales073 permanecen probados, sin nueva cobertura W/T. STATE074 registra como obligación OPEN, no como bound obtenido: con r=uM'/M,t=−u²M''/M, el jet3 exige t<=(1−r)(1+2r); falta magnitud de la covarianza y comparación global. Signo global OPEN; papers intactos.


### 2026-11-05 — Potencias075: densidad positiva del denominador Schur regularizado

**PROVED/APROBADO.** `POWER_THETA_SCHUR_DENSITY_075.md`, `POWER_THETA_SCHUR_DENSITY_AUDIT_075.md` y `POWER_STATE_075.md`. Para la Phi REAL de073, Z(z)=∫Phi(x)e^(zx)dx, u>0,c=M(u),a=M'(0), el denominador D_u=zcZ−uZ' admite la representación positiva explícita H_u(z)=D_u(z)/[z(z²−u²)]=∫Phi_u(x)e^(zx)dx. Aquí h_u=−cPhi'−uxPhi, k_u(x)=∫_x∞h_u(y)dy y Phi_u(x)=u^−1∫_|x|∞sinh(u(y−|x|))k_u(y)dy>0. h_u y k_u tienen cada uno UN cruce negativo/positivo en la semirrecta; la cancelación exacta∫cosh(uy)k_u(y)dy=0 y un cociente creciente prueban el signo antes de tomar valores absolutos. La ecuación Phi_u''−u²Phi_u=k_u, sin delta en0, da la transformada entera y sus valores removibles.

Diferencia frente003/074: se construye una medida positiva para el denominador regularizado que quedaba pendiente, no sólo valores positivos reales del cociente Schur. H_u>0 y(logH_u)''>0 en la recta. Se conserva exactamente F1=−cz/u+c²Z/(uzH_u), con residuo R=uc²/(ua−c)>0 en0. No se identifica F1 con una derivada logarítmica ni se obtiene G=F1−R/z positivo: falta comparar Phi con Phi_u. Sin positividad de tres generadores, todos los órdenes o nueva ventanaT. Sin cómputos ni campañas; papers intactos y signo global OPEN.


### 2026-11-05 — Potencias077: signo real uniforme del resto Schur regularizado

**PROVED/APROBADO.** `POWER_STATE_077.md`, `POWER_THETA_REMAINDER_077.md`, `POWER_THETA_RATIO_COMPACT_077.md`, `POWER_THETA_RATIO_OUTER_077.md` y `POWER_THETA_REMAINDER_AUDIT_077.md`. Para la MISMA Phi real de073/075, TODOu>0, c=M(u),a=M'(0),beta=u²a/(ua−c), la diferencia F_u=J−betaPhi_u tiene exactamente UN cero positivo SIMPLE, con signo negativo/positivo y masa cero. Se obtiene T_u(z)>0 y G_u(z)>0 para TODOSu,z>0, con T=Z−[Z0/H0+z²/c]H y G=c²T/(uzH). Es signo REAL puntual del resto, no positividad de su kernel.

Diferencia frente075/076: se verifican desigualdades locales ESPECÍFICAS C>0 y N=(xq−p)C'−xrC>0, donde p=V',q=V'',r=V''' y C=p³+xp²q−pq−xpr+xq². Así L=(xq−p)/C decrece hacia0; con el borde wPhi->0, un promedio de cola prueba R creciente hacia infinito. El forzante tiene patrón+−+ y dos momentos nulos; interpolación convexa da F(0)<0, la representación anticausal da cola positiva y Rolle con multiplicidades fuerza el único cruce. No se supone que una transformada positiva sea una derivada logarítmica.

Evidencia: exterior x>=1 analítico, numeradores racionales con TODOS los coeficientes positivos en un cuadrante y cola theta completa hasta orden4; root leyó y reprodujo el verificadorFraction, tresPASS. Compacto origen1024/resto8192 paneles FIJOS, jets completos hasta8 y modelosTaylor2 con restos, código auditado línea por línea; constructor1589 terminóexit0/PASS. SHA256 `896902cf8ac1f504eb1357b6edc3048a9316094afd9b8ac5597aaff4a81a70ee`. Reproducción independiente root36038 **terminada exit0/FULL PASS**, origen y8192 paneles restantes; hash coincidente con el constructor. Los anterioresFAIL de evaluación intervalar directa fueron dependencia insuficiente; se conservaron mallas/dominios y se justificó el nuevo encierroTaylor, sin cambiar la hipótesis.

El auxiliar074 no refuta estas nuevas condiciones específicas. G>0 no prueba [G(z_i)+G(z_j)]/(z_i+z_j) PSD, ni tres generadores, todos los órdenes, una ventana temporal nueva o signo globalW. Los términos cruzados del kernel del resto siguen OPEN. Papers intactos.


Corolario auxiliar auditado077: N=M/u, B=(a/N−1)/u² cumpleB>0,B′<0,2B+uB′>0; el valor removible G_u(u)=−aB′/[B(2B+uB′)]>0 da el signo deB′. ParaF=uB, |uF′/F|<1 prueba todos sus pares. El complemento deSchur del nodo0 satisface K_M(u,v)−N(u)N(v)/a=[uN(u)vN(v)/a]K_F(u,v), así la matriz anclada{0,u,v} esPD para u,v>0 distintos. Nodo0 corresponde al exponente original1/2, FUERA de los datosW admisiblesa>1; no es positividad de tres generadores admisibles ni del kernelG.


### 2026-11-05 — Potencias078: colas analíticas de dos curvaturas auxiliares

**PROVED/APROBADO en sus rangos declarados.** Apéndice078 de `POWER_STATE_077.md`, auditado en `POWER_THETA_CURVATURE_AUDIT_078.md`. Para x=u², b(x)=B(sqrt x), g(x)=xb(x)=a0u/M(u)−1 y h(x)=1/b(x), se prueba g″<0 para TODOu>=63/2 y h″<0 para TODOu>=128. Series reales completas y cotas elementales poligamma/Dirichlet, sin nuevas matrices, puntosW o mallas. Para g se obtiene el margenDelta>423/10000; para h, el ancla realL8>3/10 da a0>1/25 y luego a0u/M>3 en toda la cola desde128. Identidades de derivadas y constantes racionales verificadas independientemente.

Una condición SUFICIENTE adicional para todos los pares del kernelG_p es la doble concavidad GLOBAL de g,h: las fórmulas exactas de C_P′ y(xC_P)′ son errores de tangentes de h y g. Su descarga global sigueCONDITIONAL: quedan los compactos iniciales de g/h y no se presume preservación al iterar. g″<=0 es el jet ya registrado074, no una condición sin antecedente. La coordenada positiva K del apéndice da b=Z_K/Z_J, pero073 para cada ley por separado no ordena ese cociente.

Diferencia nueva: descarga analítica de las COLAS de estas obligaciones específicas, no una nueva regiónW. Los trece polos de tasas>=31.5 ya están cubiertos053; no se presenta un caso de tres exponentes grandes como avance de cobertura. Sin nuevoT ni signo global; continuación compacta activa, papers intactos.


### Ronda079 — Comparación exacta de secantes para tres generadores (PROVED condicional)

Fuentes phase211: `POWER_THREE_SECANTS_079.md` y `POWER_THREE_SECANTS_AUDIT_079.md`. Bajo BASE073, los bloques de tres nodos del kernel completo son PSD **si y sólo si** g(x)=a sqrt(x)/M(sqrt(x))−1 es cóncava en su intervalo de cuadrados. DET/CONC/GAP comparan exactamente dos cotas de la diferencia de secantes; delta<0 da determinante negativo. No necesita077 ni concavidad de h=1/b, ni concavidad hasta0. La nueva obligación para ai>1 queda reducida a UNA curvatura real en 1/2<u<63/2; la cola g''<0 de078 ya está probada. La región de triples ui>=63/2 ya estaba cubierta por053: ninguna nueva cobertura W o T, ningún resultado de todos los órdenes.003/074 siguen vigentes fuera de la hipótesis nueva. Auditoría root/mapa/insight aprobada; compacto activo.


### Ronda081 — BASE073 no se hereda literalmente por el resto REAL (PROVED, clase acotada)

Fuentes phase211: `POWER_SCHUR_BASE_OBSTRUCTION_081.md`, `POWER_SCHUR_BASE_AUDIT_081.md`. Para el resto exacto G_p de la Phi REAL, G_p'(1024)<0 para todo pivote p>=p0=[25(2g*+24a²·1024²/M(1024)²+2)]². Se prueban mediante cotas reales completas a>1/25, M(1024)<3 y M'(1024)>1/[3(1024+1/2)]. Por positividad global077, tampoco puede conservar concavidad global para esos pivotes. Es un fallo de la clase recursiva que exige BASE073 en cada resto, distinto del falsificador genérico074. NO refuta G_p>0, su kernel, W ni una recursión con hipótesis más amplias; no nueva cobertura ni obstrucción global. Auditoría mapa aprobada; continuación082 separada.


### Ronda082 — Criterio recíproco exacto de tres nodos (PROVED algebraico)

Fuentes phase211: `POWER_RECIPROCAL_SECANTS_082.md`, `POWER_RECIPROCAL_SECANTS_AUDIT_082.md`. Para F>0 con todos los pares del kernel K_F estrictamente PD, todos sus triples son PSD si y sólo si R(x)=sqrt(x)/F(sqrt x) y S(x)=sqrt(x)F(sqrt x) son cóncavas. DET3=Vandermonde²·R[x1,x2,x3]S[x1,x2,x3]/(R1R2R3); RECIPROCAL y pares estrictos excluyen ambos defectos negativos. Permite F decreciente y no exige BASE073, a diferencia de la herencia refutada081. Recupera079 para M real. Aplicación a G_p, pares y ambas curvaturas/preservación siguen OPEN; no nuevo W/T ni orden superior. Auditoría root/insight/mapa aprobada.


### Ronda080 — W completa para TRES potencias arbitrarias ai>1 (PROVED)

Fuentes phase211: `POWER_STATE_080.md`, `POWER_THETA_G_COMPACT_080.md`, `POWER_THETA_G_COMPACT_AUDIT_080.md`, `tools/power_theta_g_compact_080_verify.py`. BASE073+criterio079+cola078+certificado080 dan g''<0 para todo u>=1/2, y por tanto kernel completo PD para tres nodos distintos ui=ai−1/2>1/2. Repetidos se agrupan; positividad de la función representada no nula. ARCH/polar/TODOScontactos conservados por congruenciaCONE001. Certificado continuo4096panelesdyádicos fijos, arb256bits/cap20, Taylorgrado16 con resto Cauchy racional<1e−12; constructor43260 exit0/FULL PASS, hash640d8eb8ecf2bce7e782e08333a722171744af8fc0c9831582fcfcb796fb09bc. Auditoría matemática/código mapa aprobada; reproducción independiente root92790 exit0/FULL PASS4096 y hash coincidente. Novedad: triples pequeños/mixtos fuera de la región053 tasas>=31.5. NO cuatro/todos los órdenes ni nueva ventanaT; signo global OPEN. Historia de encierros de resto fallidos preservada en audit, sin cambio de malla/precisión/margen.


### Ronda083 — Factorización recíproca pfaffiana ALLorders (IDENTIDAD PROVED)

Fuentes phase211: `POWER_RECIPROCAL_PFAFFIANS_083.md`, `POWER_RECIPROCAL_PFAFFIANS_AUDIT_083.md`. Para Kij=(Fi+Fj)/(ui+uj), Ri=ui/Fi,Si=uiFi y (A_R)ij=(Rj−Ri)/(ui+uj), se prueba detK=P_n(A_R)P_n(A_S)/productoRi. P_n es Pf sin borde para n par y Pf con borde FINAL de unos para n impar. Prueba por desplazamiento, actualización rango2, cofactores impares y congruencias; incluye singulares/nodos coincidentes. Álgebra clásica atribuida (Okada/Knuth/Ishikawa–Okada–Tagawa–Zeng; anti-Löwner como antecedente), sin reclamo de prioridad mundial. Nuevo respecto del corpus: especialización exacta de todos los órdenes, no signo. Productos Pfaffianos para la Phi real siguen OPEN; PSD exige todos los subconjuntos principales. NO nueva W/T ni orden4; global OPEN. Auditoría root/mapa aprobada.


### Ronda084 — Turán local suficiente para Pfaffiano4, falsificador y cola real (PROVED acotado)

Fuentes phase211: `POWER_FOUR_TURAN_084.md`, `POWER_FOUR_TURAN_AUDIT_084.md`. PF(A_f)=−det[1,x,f,xf]/producto(ui+uj); f'>0,f''<0 y T_f=2f'f'''−3f''²>0 en TODO un intervalo implican Pf>0 para TODOS sus cuatro nodos por Rolle y Wronskiano. Para R=u/M,S=uM las obligaciones NR,NS son explícitas; se prueban NR>1/4,NS>19/4 en A=u+.5>=128 con aritmética completa. Compacto .5<u<127.5 OPEN; no cuatroglobal. Falsificador recíproco R=1+x−x²/16,S=x/R conserva propiedades escalares073/077/080 pero detK4<0 para todas las cuádruplas distintas en(.5,1): sólo NO-GO de herencia escalar local, no Phi/W negativo. La cola ya estaba cubierta por053; NO nuevaW/T. Auditoría root/mapa aprobada. Apéndice clásico083 Rolle/Hankel también auditado: criterio suficiente abstracto, signos de los cocientes reales OPEN.


### Ronda085 — W completa para CUATRO potencias arbitrarias ai>1 (PROVED)

Fuentes phase211: `POWER_STATE_085.md`, `POWER_FOUR_GENERATORS_085.md`, `POWER_FOUR_GENERATORS_AUDIT_085.md`, `tools/power_four_turan_compact_085_verify.py`. CertificaNR,NS>0 enTODOu∈[.5,127.5] con16384panelesdyádicos fijos/512bits/cap45/Taylor40 y restoCauchy racional<1e−16. Constructor61911 exit0/FULL PASS ambasfunciones, hash4916689a48baf3164b8e99ff8ff7973dbd505367cf9ee46b17b7efc9845abf46; auditoría matemática/código mapa aprobada; reproducción independiente root29132 exit0/FULL PASS16384 y hash coincidente. Exterior084+Rolle084+factorización083+menores080⇒kernel completo PD paraTODOSlos cuatro exponentes distintos ai>1, repetidosPSD/función no nula positiva. ARCH/polar/TODOScontactos conservados. Nueva cobertura exponentespequeños/mixtos, no nuevas tasasgrandes ya053. NOcinco/todoslosórdenes ni ventanaT; objetivo globalOPEN.


### Ronda086 — Curvatura REAL global por tres densidades y TP (PROVED estructural)

Fuentes phase211: `POWER_THETA_DENSITY_CONCAVITY_086.md`, `POWER_THETA_DENSITY_CONCAVITY_AUDIT_086.md`. Para R(lambda)=sqrt(lambda)/M(sqrt(lambda)), se prueba R''<0 enTODOlambda>0 SIN usar080: densidades tPhi,(tPhi)'',−Phi' normalizadas por tPhi dan[1,A,B], B'=D/t²>0 y (A'/B')'=tN077/(pD²)>0. Su determinante es negativo; sinh(ut) TP3 y su versión confluente, probadas por serie/Cauchy–Binet, más Andreief absolutamente convergente trasladan ese signo a W(Z'/u,uZ',Z)=f1³R''<0. Se conservan bordes/paridad/factores2; no se supone positividad de cada densidad. Descarga una curvatura real mediante estructura específica077, distinta de meraidentidad; depende073/077 ya probados, no elimina el certificado fijo de077. Recupera triples079/080 y fortalece la curvatura a todaλ>0; NO nuevaW frente080/085, no admisibilidad ai<=1, no jerarquía superior/allorders/T/global. Auditoría mapa aprobada.


### Ronda087 — Siguiente Wronskiano REAL en el origen (PROVED puntual)

Fuentes phase211: `POWER_THETA_DENSITY_ORIGIN_087.md`, `POWER_THETA_DENSITY_ORIGIN_AUDIT_087.md`, `tools/power_theta_density_origin_087_verify.py`. Para densidadesR4 tPhi,(tPhi)'',−Phi',−Phi''' se decide W_lambda(1,A,B,C)(0)<0 mediante UN encierro fijo racional70dig,Q0..10,modos1..8 y colacompleta m>=9, prefactorpi exp5t/2/binomialconvolutionincluido. Constructor/root/mapa exit0NEGATIVE mismos extremos/hashf8f28e5f33659ec7245e23906ab11addc5a04243f1d502a8a070dbf12d13d7b7. Por continuidad el signo deseado pasa en una vecindad existente SIN radio; no Chebyshevglobal. Darbouxexacto Wt=−k³J²(E/J)' ycoefV10=W_R3/840 localizan obligación adicional, NOpreservaciónautomática. RamaS4/globalraising OPEN; ningunaWextra respecto085, no5/allorders/T. Auditoría aprobada.


### Ronda088 — Wronskiano REAL R4 exterior, toda cola theta (PROVED)

Fuentes phase211: `POWER_THETA_DENSITY_OUTER_088.md`, `POWER_THETA_DENSITY_OUTER_AUDIT_088.md`, `tools/power_theta_density_outer_088_verify.py`. Prueba TODOt>=1: Wt(1,A,B,C)<−4000y6/t²,y=pi exp2t. Primer modo exacto con27coefpositivos tras desplazar t1,y21 y margen4096; cola theta COMPLETA hastaV6 mediante cancelaciónlog, Euler/Bell6, E62523502209/6553600000000000000000, caja128y y polinomio55monomios conK30936927338496; error<96t²y6. Constructor/root/mapa Fraction4PASSexit0, hashd2b1e479295cbf9eda602a2786b657cab5c83db1c74dee9a7d00b751723fc8f4. Da signo de determinantes de densidad para cuatro nodos TODOS>=1, no integral completa. Compacto0<t<1OPEN (087sóloentornoorigen no cuantificado); noWextrarespecto085, no5/allorders/T. Auditoría aprobada.


### Ronda090 — Secante recíproca y una curvatura del resto (PROVED real tras089)

Fuentes phase211: `POWER_RECIPROCAL_SECANT_CONCAVITY_090.md`, `POWER_RECIPROCAL_SECANT_CONCAVITY_AUDIT_090.md`. LemaTf>0⇒secante recíproca estrictamente cóncava, también para anclaINTERIORP conambasorientaciones. InputTRglobal descargado089(constructor/rootFULLPASS): h=1/bstrictconcava; con086/078 todosparesGpstrictPD. REST-SECANTS yTg=a²TR descarganademás S_G(x)=sqrt(x)Gp(sqrt(x)) estrictamente cóncava TODOSp,x>0. Laotra R_Gcurvatura exigeTh>0globalOPEN, equivalenteenconfluenciaanclada al siguientejet: W(x,x²,G,xG)=−a²G⁴Th. ANCHORED-FIVE tiene nodo0auxiliarNOadmisibleW. NoherenciaBASE/TuranGp/allorders/Wnueva/T. Auditoríamapaaprobada.


**Actualización090§9, NO-GO de herencia genérica (PROVED):** w=(5−e^−x)/4 y f0=1,f'=1/w² definen f positiva, creciente, cóncava y T_f=e^−x/w5>0 global. Sin embargo H=x/(f−f0)=1+x/4−x²/12+5x³/192+O(x4) tiene T_H(0)=−1/192 y T_H<0 en una vecindad positiva. Antiderivada y jets exactos auditados root/mapa; sin campaña. Refuta sólo herencia automática T_f⇒T_H, NO T_h de Phi ni W; S_G real sigue PROVED y T_h real OPEN. Consolidado en090, sin registro091 duplicado.

### Ronda089 — Transporte REAL R4 global y T_R>0todoeje (PROVED estructural)

Fuentes phase211:`POWER_STATE_089.md`,`POWER_THETA_DENSITY_COMPACT_089.md`,`POWER_THETA_DENSITY_COMPACT_AUDIT_089.md`,`POWER_THETA_DENSITY_TRANSPORT_089.md`. Constructor40406FULLPASS1024origenλ+8192restot,hash995ef292abf5a80a3d195b4e68a815e1b56f9b343531bc1c0786af682413d1aa; auditoríamath/literalaprobada,reproducciónindependienteroot87911exit0/FULLPASS1024+8192ymismohash. Boundsthetacomplejos+16modos/colascoefantesderivar+Cauchydeterminante,parámetrosfijos,sinajustes. Empalme088⇒WronskianR4negativoTODOt>0. OrdenECT[1,B,A,C]usaWronskianosprevios086sinpresuponerA'>0; Rolle⇒detdensidadesnegativoTODOSnodos. SinhTP4/Andreiefconfluente⇒W(Z'/u,uZ',Z,u²Z)=−F0⁴T_R<0⇒T_R>0TODOx>0.090aplicableglobal⇒h=1/bstrictconcava yparesdelrestoGpPD via078/086. NoS4global/noherenciaTuranGp/allorders; ningunaWextrarespecto085niT,globalOPEN.


### Ronda091 — Pi/s no monótono para cofactores REALES (NO-GO de criterio, PROVED)

Fuentes phase211:`POWER_PEANO_MONOTONICITY_OBSTRUCTION_091.md`,`POWER_PEANO_MONOTONICITY_AUDIT_091.md`. Para cofactoresellúltimacolde[w,v,w'',*], w=tPhi,v=−Phi', Pi(s)=Σell_i(s−ti)+, W3=w³(B')²J>0real086. Cerca de CUALQUIERt0>0 con ti=t0+(i−1)eps, ell=eps³W3[−1,3,−3,1]+O(eps4). (Pi/s)'=Σactiveell_i ti/s² tiene primerprefijo<0 ysegundo>0; refutaambasmonotoníasglobalesparaTODOSnodos. Peanoexacto det[w,v,w'',K]=∫s zeta[Pi/s−Pi(b)/b] conserva momento/cruceyFubini. Sólo falla esecriteriosuficiente: integral/menoranclado/T_hREALsiguenOPEN, compensaciónposible, ECTR4real089 no refutado. NoWnegativo/nuevaW/T/global. Auditoríaroot/mapaaprobada.


### Ronda092 — Cero REAL de la carta de eliminación Delta (PROVED acotado)

Fuentes phase211:`POWER_SHIFTED_WRONSKIAN_092.md`,`POWER_SHIFTED_WRONSKIAN_AUDIT_092.md`,`tools/power_shifted_wronskian_092_verify.py`. IdentidadDelta=−W(w'',v'',w4)/(w³k²J). Cerca0 Wshift=8Phi0³t6[D0+Ot²], con−56488961026<D0<−56488961025 usandoEXACTAMENTEintervalos087; constructor/root/mapaPASS,sinotratheta. Exterior088jetsVj=2^jy+O1hasta6 paganpolinomiofinito: Wshift/Phi³=4096(2t²−1)y9+O(t²y8)>0eventual. PorcontinuidadDelta tieneceroREAL, carta2×2noinvertibleglobal. Abel: ambasimágenesD3(1/w),D3(t/w) tienenWronskian noidénticocero concero; ningunaODEhomog2mónica concoefcontinuosGLOBALpuedecontenerAMBAS. Sóloexcluyeesaregularizaciónuniversal, nocancelaciónparticularK/otraODE/gauge/carta/orden. NoWnegativo/menorancladodecidido/nuevaW/T/global. Auditoríamapaaprobada.


### Ronda093 — Jet particular REAL seleccionado por bordes (PROVED local)

Fuentes phase211:`POWER_PARTICULAR_ORIGIN_DESIGN_093.md`,`POWER_PARTICULAR_ORIGIN_AUDIT_093.md`,`tools/power_particular_origin_093_verify.py`. Dpart=Pκ+Qc+R,κ=τ0/a−1; NUM=QPhi0I0+PI1I0+(R−P)Phi0I2=Phi0I2Dpart. ÚNICotestmomentosI0..2:128paneles[0,2],Taylor64/cap65/512bits,16modostheta+colascoefcompletas+restotemporal2^-140; parámetrosauditadosantesrun. Constructor37905exit0PASS128/NEGATIVE,hash57c0656deb1767e00a4de674a0f5f6556886eca06edbc93ae1ef8488b032c67e; reproducciónindependienteroot94506exit0/FULLPASS128ymismohash. Dpart<0 (aprox−21658.19847758sololectura)⇒W(w,v,w'',K)<0envecindadexistentedel origen,sinradio. Verifica(nofalsifica)premisalocalparticular; noglobalQF/conoselector/Deltauniversal/nuevaW/T. Auditoríamath/literalmapaaprobada.


### Ronda094 — Distancia exacta y densidad de UNIÓN diagonal en L² (PROVED)

Fuentes phase211:`POWER_HIGHPASS_DIAGONAL_DENSITY_094.md`,`POWER_HIGHPASS_DIAGONAL_DENSITY_AUDIT_094.md`. CayleyUNITARIOsinpeso llevaQ^rVn aS_n,r=(1+z)^rPdeg<n. dist²(1,S)=1−A,A=[(n+r−1)!]²/[(n−1)!(n+2r−1)!],porGram/Dodgsonconbordesa0/b0. exp(−r²/n)<=A<=exp(−r²/(n+2r−1))upperr>=1; r0A1. UNIÓN_nQ^r(n)Vn esL²densaiff liminf r(n)²/n=0; pruebaMISMOespacioparaaproxpolinomios yexcepcionesfinitascon1+εzM. Todosbloquesr>=n tienen distancia>1/2alvectorbase; finitobloquesconfluentestasaFijano reparanUNIÓN. Diferencia016:normaponderadaallí,distanciaEXACTAL²sinpesoaquí. NOafirmaenvolventelineal/continuidadW/crosses/mezclasninuevaW/T/global. Auditoríasroot/mapaaprobadas.


### Ronda095 — Cola PARTICULAR K con tres derivadas completas (PROVED analítico)

Fuentes phase211:`POWER_PARTICULAR_TAIL_095.md`,`POWER_PARTICULAR_TAIL_AUDIT_095.md`. ParaKreal seleccionadoportail, W(tPhi,−Phi',(tPhi)'',K)<−3071Phi⁴t²y² enTODOt>=64. StripthetaCOMPLETO|Rtheta|<2^-460⇒pboundholomorfo; IBPexactaK/Phi=1/p+resto(6+25|z|)/Y², Cauchycontrola3derivadas(ningúnOrealderivado). ModeloW[t,q,tq²,1/q]=−128q²(6t²+4t−1);7erroresmultilinealespagadosporC=1e6(1+39321600)³<2^98,umbral64analíticosinmuestras. Objeto distinto088densidadoriginal/092cartauniversal; evitainvertirDelta.093sóloorigensinradio,intervalointermedioOPEN; no globalparticular/condeselecciónni nuevaW/T/generadores. Auditoríamapaaprobada.


### Ronda096 — Proyección uniforme con TODAS las tasas, objetivo fijo (PROVED)

Fuentes phase211: `POWER_VARIABLE_RATE_HIGHPASS_096.md`, `POWER_VARIABLE_RATE_HIGHPASS_AUDIT_096.md`. Para f0(t)=sqrt(2u0)exp(−u0t) FIJO y TODOS u>0,n>=1,r>=1e12n³, ||Proj_(Q_u^rVn(u))f0||²<=200n/sqrt(r)<=1/5000. Por tanto distancia a la UNIÓN con TODAS las tasas >=sqrt(4999/5000). Prueba autónoma Gegenbauer/Rodrigues/Gamma, centrado con ambas paridades y factor4^r/pi, NEAR por evaluaciones imaginarias, FAR por Gram exacta094 y logs explícitos; sin campañas. Diferencia094: allí tasa fija, aquí objetivo fijo y tasa variable; diferencia016: aquí L² sin peso. Cono060 incluido. NO envolvente lineal/cruces/mezclas ni otras familias continuas iniciales; no W negativo ni cierre/imposibilidad global ni nuevaT. Auditorías root/mapa aprobadas.


### Ronda097 — T_h REAL directa, cola u>=512 y jet regular (PROVED acotado)

Fuentes phase211:`POWER_DIRECT_RECIPROCAL_TURAN_097.md`,`POWER_DIRECT_RECIPROCAL_TURAN_AUDIT_097.md`. Identidadexacta T_h=a[auN_S−4C_h]/[16u³(au−M)^4]. BOX084con aritméticaCOMPLETA daN_S>2M²,C_h<4M³; ancla078a>1/25 yMupper/gapmonótono pruebanau>8M TODOu>=512⇒T_h>0allí. Sinmuestras/certnuevo. OrigenregularN=M/u=a+b1x+...+b4x4,b1<0por086; T_h0=12a/b1⁴detHankel3(a..b4),signoNOevaluado. ObjetivoexactomásdébilqueWronskianparticular093/095; uinclinación≠tiempot. Compacto0<u<512OPEN,noT_hglobal/R_GtodoslosP/triplesGp/cinco/allorders/nuevaW/T. Auditoríaroot/mapaaprobada.


### Ronda098 — T_h REAL exacta en el origen (PROVED local)

Fuentes phase211:`POWER_EXACT_H_ORIGIN_DESIGN_098.md`,`POWER_EXACT_H_ORIGIN_AUDIT_098.md`,`tools/power_exact_h_origin_098_verify.py`. ÚNICOtestseismomentosparesI0..I10con128paneles[0,2],Taylor64/cap65/512bits,16modos+EPScoefcompleta,REM1e12adaptado ytailtemporal2^-138paraorden10. Zprec11→log11/Mprec10daNcoefcumulantesa..e; H3=ace−ad²−b²e+2bcd−c³ yTh0=12aH3/b⁴. Constructor19778exit0FULLPASS/H3POSITIVO,hashbebcca70c5dd54ba53841e77542aa3e3e2ea059306061dc676e24f88ee5117c9; reproducciónindependienteroot57072exit0/FULLPASS128ymismohash. AsíThREAL0>0(aprox3.15513e−5sólolectura)yentornoexistentepositivosinradio. ObjetivoEXACTOmásdébilquedensidadparticular093;0auxiliarnoexponenteW. Compactointermediohasta097u512OPEN,noThglobal/triplesGp/cinco/nuevaW/T. Auditoríamath/literalmapaaprobada.


### Ronda099 — T_h REAL global, triplesGp y cinco nodos AUX anclados (PROVED)

Fuentes phase211:`POWER_STATE_099.md`,`POWER_EXACT_H_GLOBAL_DESIGN_099.md`,`POWER_EXACT_H_GLOBAL_AUDIT_099.md`,`POWER_SCHUR_TRIPLES_APPLICATION_099.md`. Constructor98529FULLPASS2048/hash6712eb8542b4d8b7e0836260fba831cd44ccaffb7f1ea321df0a0a32668d51d7; root8310exit0/FULLPASS2048ymismohash. S=Ntilde/u15=(16/a)NUMλENTERApar; Schwarzlocal/polysPSPC y gaugeexp−4Mc(u−c)antesdatos paganCauchyB2^169/Taylor104/cap109/1024bits,2048paneles[0,512],sinajustesencorrida. Más097⇒Th>0TODOx>0,098incl0.090ancla+082⇒RG/SGstrictconcavas yTODOStriplesKGpPD paraTODOp. DobleSchurcongruenciaREAL(noforzosamentepositivad_i)⇒bloqueK_M{0,p,z1,z2,z3}PD.0auxiliar correspondea_orig1/2NOadmisible: NOcincoWgeneradoresarbitrarios,nuevaW/T/allorders; siguienteTuránrestoOPEN. Auditoríamapaaprobada.


### Ronda100 — Observable REAL de la pareja J/K no creciente (PROVED, clase acotada)

Fuentes phase211:`POWER_PAIR_OBSERVABLE_SCOPE_100.md`,`POWER_PAIR_OBSERVABLE_SCOPE_AUDIT_100.md`. ParaKPAR078/Jpositivos, eta=−K'/J es imparsuave, eta0=0 y0<eta(t)<a/tparaTODOt>0⇒eta∞0, no monótona enningúnsentidoglobal. Balance∫(aPhi−J)=0+uncruce paga−K'>0. IBPbilateralexacta E_(J,u)eta=uZK/ZJ=ub=a/M−1/u, h=u/Eeta. F(u)ya081explícitamenteatribuida, no otroNO-GOdeF/Gp; nuevoobjetoobservabletemporal deLApareja. Sóloinvalida clasequeexigeetacreciente, no otrascomparaciones/datos/parejas/invariantes. NoTh/Wnegativo,nuevacobertura/allorders/T/global;099permanecePROVED. Auditoríamapaaprobada.


### Ronda101 — Curvatura logconvexa del potencial insuficiente (PROVED, auditoría aprobada)

Fuente phase211: `POWER_LOGCONVEX_CURVATURE_OBSTRUCTION_101.md`. Potencial AUX explícito V=A[cosh(t)+10^-4 cosh(10t)], A=10^46: V''>1, V'''/V'' estrictamente creciente por logconvexidad estricta de V'', TODAS derivadas pares positivas y TODAS impares positivas en t>0. Tres nodos U_i=A*i*10^-4 y vector (1,-2,1) dan c^tK_Mc<−3delta^4/(2A): inversa de v' con jet quinto d=−51675000000000/107213535210701<−2/5, resto elemental <=100u^7; concentración IBP exacta <=A^-1/2. Diferencia074: allí potencial polinómico, curvatura no logconvexa en cola y derivadas altas nulas. Sólo refuta esa candidata genérica reforzada de073; NO incorpora todos los inputs077/089/099, que el triple negativo no puede satisfacer conjuntamente. No Phi/W negativo, nueva cobertura, herencia general ni signo global;099 vigente. Consulta DEDUP y chequeo racional PASS; fuente y auditoría independiente `POWER_LOGCONVEX_CURVATURE_AUDIT_101.md` aprobadas; coeficientes y costes reproducidos por Fraction exacta.


### Ronda102 — Cocientes temporales REALES estrictamente decrecientes (PROVED)

Fuentes phase211:`POWER_REAL_PAIR_MONOTONICITY_102.md`,`POWER_REAL_PAIR_MONOTONICITY_AUDIT_102.md`. (K_even/J)'<0TODOt>0 porvalle077+Rolleparconbordes; (Psi_p/D_p)'<0TODOSp,t>0 porECT4impar089⇒Chebyshev4PAR[J,Phi,J'',Phi'']. ParaF=Psi−rD,LpF''=(1+rp)J''+(pbeta−p²)J−rcPhi''−betacPhi tiene<=3raíces; RolleD²yLpganan2,descartanraíz dobleF/estaciónratio. Colaspositivas0<Psi/D<=2tau/c→0fijansigno;normalizaciónexactaGp=c z ZPsi/ZD. Se conservanmultiplicidades/bordes/supertails,sinnuevoscertificados. ObjetoDISTINTOeta100(no contradicción); usa075077089reales,nohipótesisgenéricafalsa101. Sólo parejasactuales/primerpivote: preservaciónECT4/positividadtrasnueva reducción/allordersOPEN,noWextra/T/cincoadmisibles. Auditoríasroot/mapaaprobadas.

**Corolario102§8 aprobado (mismo resultado ampliado):** A=D_p,B=Psi_p yF=zZB/ZA=Gp/c. Cov(rho,t tanhzt)<0⇒q aF>d y h=dA−qB tiene cruce−/+ con balancecosh. Green075 construyeE>0,par/supertail/Neumann, ZE=(dZA−qZB)/(z²−q²). F1=d/z(ZB/ZE−q), residuo r_q=q d²/(q aF−d)>0. U=B−gammaE de masa0 es el NUEVO numerador: cruce/positivadensidadXi todavíaOPEN; no se infiere deB/A. EscalaoriginalGp=cF conserva cE,cF1,cr. Denominador siguientePROVED, pareja completa/monotonía/herenciaallorders no. Auditoríasroot/mapaaprobadas; sin nuevaW/T.

**Complemento099+102 (PROVED, mismo bloque):** con inputADICIONAL099, R_F,S_F paraF=Gp/c sonstrictconcavos yanalíticosen0 (aF>0). DET3con0 ydivididasstrictnegativas,incl[0,q²,q²],danK_F{0,q,z}PD. DobleSchur⇒R_next(z)>0 z!=q; coeficientescuadráticospositivosDET3/ell² y ell'(q)>0pruebanR_next(q)>0. Así el resto REALtransformadoyapositivoTODOSp,q,z>0, no sólo denominador/residuo. Ucross/Xipositive/monotoníanuevapareja/kernelcruces siguenOPEN: positividadtransformada≠densidadpositiva.0auxiliarNOadmisibleW,no nuevaW/T/allorders.


### Ronda103 — Límite REAL de la pareja y signo puntual del origen (PROVED)

Fuentes phase211: `POWER_REAL_PAIR_DOUBLE_LIMIT_103.md`, `POWER_REAL_PAIR_LIMIT_ORIGIN_DESIGN_103.md`, `POWER_REAL_PAIR_DOUBLE_LIMIT_AUDIT_103.md`. Escalas positivas A_p=pD_p y B_p=(ap/M(p))Psi_p convergen a(J,K_even) en normas con peso exponencial fijo y derivadas, por resolvente bilateral y primitiva doble. Para q fijo el Green es continuo; luego E_*(q)/q→H, H''=b0J−K, b0=massK/massJ, Hmass>0. Así U_lim=K−(massK/massH)H. El test puntual único P=720I0²(K0Hmass−KmassH0), polinomio de ocho términos en I0,...,I6, dio NEGATIVO: P=[−3.1683047444094325e−13±2.16e−30], U_lim(0)=[−1.35855717857699839e−6±8.09e−24]. Certificado fijo128 paneles[0,2]/Taylor64/cap65/512bits/16modos, colas theta y temporal completas. Constructor68812 y root91737 exit0/FULLPASS; hash5090a71fd7dd4ae786a3f785ca8a4c32d6691cf92af912d4e5fffff9e583d080. Auditoría matemática/literal mapa y root aprobadas. También U_original(0)<0 para q pequeño fijo y p suficientemente grande, sin umbrales explícitos. Sólo signo puntual de origen: NO falsificador, cruce global, positividad Xi, nueva W/T ni cierre de órdenes;099+102 siguen vigentes. Papers intactos.


**Extensión analítica103 posterior (PROVED, sin nuevo test):** H/K_even es estrictamente decreciente en TODOt>0. Para F=H−rK, D⁴F=(b0+r)D²J−raD²Phi−aPhi+J es combinación no trivial de EVEN4(102). Doble Rolle par con bordes excluye raíces dobles de F y estaciones del cociente. Cola K>=aI/2,H<=b0tauI⇒H/K→0 fija signo estricto. Promedio de masas⇒U_lim=K−(Kmass/Hmass)H tiene exactamente UN cruce simple−/+ y Xi_lim=G0U_lim>0. El caso LÍMITE completo queda probado; el certificado negativo previo de origen se conserva como comprobación independiente cronológicamente anterior. NO se propaga por límites el cruce global a parámetros FINITOS p,q, ni hay nueva W/T/allorders. Auditorías root/mapa aprobadas.


**Ampliación103 a TODOq>0 (PROVED):** para la pareja REAL(J,K), E_q=Gq(dJ−qK),d=qZK(q)/ZJ(q)>0. Lq(E_q−rK)''=(d+r)J''−raPhi''+a(rq²−q)Phi+(q−rq²)J es EVEN4 no trivial; Rolle D²+Lq excluye estaciones de E_q/K. Continuidad en q para cada t y límite C1 E_q/q→H fijan (E_q/K)'<0 para TODOSq,t>0. Promedio estricto de masas⇒U_q tiene un único cruce simple−/+ y Xi_q>0 para TODOq. Resultado final ya no requiere q pequeño; sigue siendo pareja p→infinito, SIN conclusión global para p FINITO ni nueva W/T/allorders. Auditorías root/mapa aprobadas, sin nuevo cómputo.


**Puente exacto103 a pivotes FINITOS (PROVED):** Con lambda=p²M(p)/(ap−M(p)), se tienen beta D_p+p²Psi_p=lambda K, LpPsi_p=J−lambda K y Psi_p=(lambda/p)E_*(p). Por tanto Psi_p/K decrece estrictamente y D_p/K crece estrictamente para TODOS p,t>0 finitos, mediante103 para todo q, sin suponer estabilidad del cruce bajo límites. Para U=Psi−gammaE, LpLqU es una combinación de[K,J,Phi,J''] con coeficiente de K igual a−lambda alpha≠0, alpha=gammaq−q²>0. La propiedad Chebyshev4 de esta familia MIXTA bastaría, pero sigue OPEN: EVEN4 no la prueba; se conservan los antecedentes093/095. Bajo ese input suficiente, la orientación−/+ usa además Rnext>=0, ya deducida de099+102 mediante Schur para z distinto de q y continuidad en el valor removible z=q. La orientación inversa forzaría Xi<0 y contradicción. No se afirma nuevo cruce global de U finito, positividad Xi, signo W/T ni todos los órdenes; no se ejecutó otro certificado. Auditoría root/mapa aprobada.

**Prefijos mixtos103 (PROVED):** [K,Phi,J] es Chebyshev extendido global de dimensión3: f=AK+BPhi+CJ con tres raíces daría D²f no trivial en EVEN4 con al menos cuatro. Para tau=J/Phi,kappa=K/Phi=tau(K/J), S=kappa'/tau'>0 y W(Phi,J,K)=Phi³(tau')²S' nunca se anula. S'>0 contradiría(K/J)'<0 mediante el promedio de cola de S; así S'<0 y kappa es estrictamente convexa como función de tau. Los primeros tres Wronskianos en orden[K,J,Phi] son positivos. El CUARTO mixto sigue OPEN; sin nuevo certificado ni signo W/T/allorders. Auditoría root/mapa aprobada.


### Ronda104 — Gate mixto de origen positivo y cola analítica (PROVED, alcance local)

Fuentes phase211:`POWER_MIXED_FOUR_ORIGIN_DESIGN_104.md`,`POWER_MIXED_FOUR_ORIGIN_AUDIT_104.md`. Familia[K_even,J,Phi,J'']; matriz regularizada enlambda=t², factoresk! ypuenteW_t=64Phi0⁴t⁶[Dmix+Ot²]. Recuperación087 INTACTA porhash y cajas103 racionales completas, sin cuadratura nueva. Constructor y root exit0/PASS: Dmix>0 (extremos exactos en fuente/log), hash063ce9ba28dc9b0e3cca245018a968794b5b28c7a57df5da7a5c70d008b95105. Log104 persistePhi0,z1,z2,z3 outward antesnoarchivados. Prueba holomorfa independiente con toda cola theta y7errores multilineales daWmixed/Phi⁴>6t²/y² paraTODOt>=64. Por tanto origenpositivo envecindadexistente SINradio ycola positiva; compacto intermedioOPEN. Prefijos1–3globales103vigentes, pero NOCheb4global, falsificador, cruceUfinito/Xipositiva, nuevaW/T/allorders. Auditoríasroot/mapaaprobadas; no más tests. Papers intactos.


### Ronda105 — Kernel Volterra mixto bruto de signo variable (PROVED, clase acotada)

Fuentes phase211:`POWER_MIXED_VOLTERRA_OBSTRUCTION_105.md`,`POWER_MIXED_VOLTERRA_AUDIT_105.md`. Sobre la pareja REAL, tau=J/Phi,kappa=K/Phi,E=−tau'>0,S=kappa'/tau'>0,w=−S'>0,D=tauS−kappa>0. Identidad exacta w'+Bw+RS−TD=1, B=(2−2V''tau)/E,R=(tV'−1)'/E,T=(V'^2−V'')'/E. CT3 yK/J→0 danS=integralcola w yD=integralcola tauw; kernelH(t,s)=R(t)−T(t)tau(s). Jets theta completos y cambio de variable con dominación(1+u)e^-u prueban tauV'/t→1, luego[(tV'−1)'−tau(V'^2−V'')']/(tV')→−2. AsíH<0 cerca de s=t para t grande, peroH→R(t)>0 al s→infinito. Refuta SÓLO positividad punto a punto del kernel BRUTO, distinto del Peano091. No signo de integral, exclusión de gauges/reordenaciones, W4mixto/Ufinito/W ni obstrucción global. Auditorías root/mapa aprobadas, sin cómputos nuevos ni papers modificados.


### Ronda106 — Control holomorfo de integrales mixtas normalizadas (PROVED, sin signo)

Fuentes phase211:`POWER_MIXED_NORMALIZED_INTEGRAL_106.md`,`POWER_MIXED_NORMALIZED_INTEGRAL_AUDIT_106.md`. StripRe z>=−1/16,|Im z|<=1/16: Theta=(2y−3)(1+Rtheta),|Rtheta|<1/4, Y=|pi e2z|>21/8. Variablevreal y r=.5Log(1+v/y) dan representaciones normalizadas EXACTAS de tau=J/Phi ykappa=K/Phi; igualdadreal extendida holomórficamente por dominación, sin cambio de contorno supuesto. FactorTheta/jacobiano acoplado pagaA<=7/(2Y)e^-v(1+v)^2. CotasY|tau|<100(1+|z|),Y²|kappa|<1000(1+|z|); colav>=512<2^-450, modosm>=17<2^-675 parafunciones escaladas, incluidosnumerador/denominador ycolumnaX porlogderiv. Cauchy pagaerrorescoef32^j. BoundWronskianescalado2^120 ydivisibilidadpart6+Schwarz danboundregularizado2^168. Resuelve control de evaluación/errores, NOpositividad. Diseño de ejecución, cuadratura finita/tolerancias/partición/orden siguenPENDIENTES; nocorrida/nuevojet/muestra. Cheb4mixto/Ufinito/W/T/allordersOPEN. Auditorías independientes root/mapa aprobadas; papers intactos.


**Ampliación106§8 (PROVED, herramienta sin ejecución):** Gauss–Legendre64 en diez intervalosv[0,1],[1,2],...,[256,512], discosradio2h,dominiocomplejoRe(y+v)>2 yRe(1+sv/y)>4/5. Mayoranteuniforme2^34 también para parámetrotemporalballsemiancho<=1/64, condominioextendido|z−c|<=3/64 y escalasconstantes. Cauchycoefj yexactitud127/pesospositivos paganerroranalíticototal2^(−83+5j)<=2^-68 paraj<=3. Bolasnodos/pesos,aritmética,colasmodos/v yfactorialesdebenpagarseadicionalmente ANTESWronskiano. Auditorías matemática/literal root/mapa aprobadas; diseño107/ejecución/signos siguen pendientes.


### Ronda107 — Certificado compacto mixto INCONCLUSO (reproducido)

Fuentes phase211:`POWER_MIXED_FOUR_COMPACT_DESIGN_107.md`,`POWER_MIXED_FOUR_COMPACT_AUDIT_107.md`. Diseño/literales auditados ANTESdatos: origenlambda[0,.25],Phi128/cap1025/1024bits/Taylor512,recurrenciasJ/K ymoment103; RESTGauss64*10/512bits/cap4/5; subdivisionleftfirstdepth10/eval8192fijos. Root5594 yreproindependientemapa46719 terminaronexit2/INCONCLUSIVEorigen:11eval,0accepted,depth10lambda[0,1/65536],det[+/−2.94e−3]. RESTNOejecutado. Logsroot/auditpersistidos; hashmain2a7d147caf8181adb5aa29eb6fcbe356f625e2743ad6765e6ac543aacad23054,origin15d6f12c197ef52c062a12c59ee4a7c5db94c74e0073e8463a7ce03dd613e553 idénticos/sinmodificaciones. SóloinsuficienciaencierroconESTEpresupuesto: NOfalsificador/obstrucciónmatemática/signonegativo/Cheb4global/Ufinito/W/T/allorders. Nuevarepresentaciónrequiereotro diseñoauditado antescorrida; noajustesparaforzarPASS. Papersintactos.


### Ronda108 — Determinante polinómico correlacionado INCONCLUSO (reproducido)

Fuentes phase211:`POWER_MIXED_FOUR_POLYNOMIAL_DESIGN_108.md`,`POWER_MIXED_FOUR_POLYNOMIAL_AUDIT_108.md`. Cambioalgebraicoauditado ANTESdatos: formar24permscompletasenpolinomios,grado2042real(<=2048),trasladoTaylorallcoef+error2^-200; builders/presupuestos107intactos. Root82660 ymapa28564exit2/INCONCLUSIVE:15eval4accepted,coberturaλ[0,141/8192],depth10en[141/8192,1129/65536],det±2.04e−4;RESTNO. Hash108eb200a9061a3761d2b1a5dc5ca38def6c5c16e1e0901524c39969555eb791f6a;107hashesintactos. Logsroot/auditpersistidos. PerfilSÓLOlocalsYAcalculados,noextraprobe:finalcoef0±1.79e−4 yradioadicional≈2.456e−5,asíincertidumbrecentral noseconfundeconvariacióncelda. No decideceroreal/causaúnicadeancho. INCONCLUSO,nofalsificador/obstrucciónmatemática/Cheb4global/Ufinito/W/T/allorders. Otra representación requiere diseño previo, no ajustesparaPASS. Papersintactos.


### Ronda109 — Cauchyclip: origen PASS; certificado total INCONCLUSO por presupuesto

Fuentes phase211:`POWER_MIXED_FOUR_CAUCHY_CLIP_DESIGN_109.md`,`POWER_MIXED_FOUR_CAUCHY_CLIP_AUDIT_109.md`. IntersecciónBASEcoeficientes107conCauchy|phi_k|<=2^(40+k),|J_k|,|K_k|<=2^(42+k),antesrederivar/Q/det108;verdaderoscoeficientespreservados,resto2^-200ymismosparámetros. Root52183terminóexit2/INCONCLUSIVE:origenPASS16/16lambda[0,.25],REST8192eval4113hojasaceptadas. AuditoríalogFractionconfirmacoberturacontiguaREST[1/2,2645/512],longitud2389/512. Siguientecelda[2645/512,1323/256],depth6,NOevaluadaporcap; nofallopordepth/signonegativo. Driverhashc3fe2df06692622dcaddbb4f2eb21047a7f4be46affdbe151af27f25bbef48ba y107/108intactos. NOreproducciónindependiente109niFULLPASS. NoCheb4global/Ufinito/W/T/allorders/obstrucciónmatemática. Logpersistido;papersintactos;auditoríamath/literal/logroot/mapa, sin nuevaevaluaciónporauditor.


### Ronda110 — Cociente theta factorizado: AUDITADO, ejecución root en curso

Fuentes phase211:`POWER_MIXED_FOUR_FACTORED_RATIO_DESIGN_110.md`,`POWER_MIXED_FOUR_FACTORED_RATIO_AUDIT_110.md`. Condición109sinFULLPASSsatisfecha porexit2. IdentidadexactaTheta16=(2y−3)(1+R16),Bm=m4+3m²(m²−1)/(2y−3);ratio=(1+2v/d)(1+Rshift)/(1+R),p16=2y−9/2−6/d−Rt/(1+R). No modosomitidosnifuncióncambiada; mismosorigen109,Gauss107,errores/parámetros/DFS/budgets. Root/mapaaprobarondiseñoyliteralANTESdatos(cachem−1correcto,hashguardscuatroarchivos,nopatch). Primeracorridarootautorizada/encurso, SINresultadofinal,reproducciónniPASSadelantado. No sepromete mejorarencierroocoste. Identidad/controlrepresentación,noW/T/allordersnuevos;papersintactos.


### Ronda111 — Monotonías individuales allp insuficientes para TP2 (PROVED, clase auxiliar)

Fuentes phase211:`POWER_GREEN_PAIR_TP2_SCOPE_111.md`,`POWER_GREEN_PAIR_TP2_AUDIT_111.md`. ParejaabstractaK=1_(|t|<2),J=(1+1_(1<|t|<2))K. Lambda_p=2−1/(2coshp) yGreenVpC1compactoexacto danVp>0,(Vp/K)'<0paraTODOp>0en(0,2). Mismosparams1,2:ratioV2/V1creceen(0,.5],decreceen(1,2),pordesigualdadesanalíticas; menoresnodos(.25,.5)y(1.5,1.75)tienensignosopuestos. InclusoJ/Kstrict↑:añadirdelta t²paradelta>0suficientementepequeñopreservaambosmenoresporcontinuidad;W=Vp' resuelveLpW=2delta t+Dirac1conDirichlet0,Greennegativopruebamonotoníasallp. SuavizarescalóninteriorconKindicadortambiénadmisible; NOseafirmabordescompactossuavesconallp. SóloNO-GOdeimplicacióngenéricamonotoníasindividuales⇒TP2, NOparejaREAL/compatibilidaddiferencial103/MIXED4/W/allorders. Dedup074/101/091/105objetosdistintos. Auditoríasmath/literalroot/mapaaprobadas,sincómputos/campañas,papersintactos.


**Ampliación111§5.3 (PROVED, misma contraclase):** V(x,t),x=p², es además completamente monótona estricta en x para TODO orden y t interior. q_x=−partial_tV satisface(−D²+x)q_x=mu positiva fija(Dirac1, oDirac1+2delta tdt), Dirichlet0,2. Greenpositivo/suaveenxcompactos permite derivar conmedidafinita: A_x partial_x^n q_x=−n partial_x^(n−1)q_x, porinducción signosalternadosestrictos. V=integral_t²q_x heredaCMtodosórdenes. LosMISMOSminoresTP2opuestos persisten: añadirCMparamétrica alasmonotoníasindividualesallp NOimplicaTP2. Sóloauxiliar, noCMdeparejaREALdecidida niW/allordersrefutados. Auditoríasmath/literalroot/mapaaprobadas; sin datos ni campañas.


**Mejora analítica posterior104 (PROVED, sin datos):** conservar las potencias de y en los7errores da61440Ht³/y³+6144H²t³/y⁴+192H³t³/y⁵. Para y>=H suma<2^17Ht³/y³. e²>7 ycomparaciónentera3*7^16=99698791708803>82463372083200=16·2^17H, conH39321600; y/t↑pagaerror<t²/y²paraTODOt>=16. Modelo>7t²/y²⇒Wmixed/Phi⁴>6t²/y² enTODOt>=16, mejorando64. Auditoría root/mapa, sinsampling/certtheta nuevo. NOretoca110 ni declara compacto/global/W antescobertura yrepro.


**Resultado constructor110:** root52878terminóexit2/INCONCLUSIVEporbudget8192,4198hojasRESTaceptadasyorigenPASS16/16. ParserFractionauditorconfirmacoberturacontiguaREST[1/2,845/32],longitud829/32. Siguiente[845/32,3381/128],depth4pendientealcap. Driverhashc629d4ed4b5eeb625a69ee92f6000892b9493c50e825e9ade73bf3a5a9362108. NOFULLPASSdelprogramahasta64. Réplicaindependiente12244sigueMISMOprograma/presupuestosinpararen16; WMglobal112todavíaCONDICIONALhasta coberturaindependiente16+TAIL104. Nofalsificador/obstrucciónmatemática,ningunaactivaciónadelantada.


### POWER — Revisión estratégica y cierre auxiliar WM (sin cierre del signo)

Fuente phase211: `POWER_REASSESSMENT.md`; actualización de110/112. Antecedente explícito: función generadora de R162_803, Theorem H, y D-16; POWER usa su núcleo real de tipo Pick. La diferencia declarada en001 justifica casos finitos y falsificadores, no un mecanismo uniforme nuevo. REF-D no se usa como imposibilidad. Por instrucción del usuario se abandona la continuación automática de la torre: una nueva candidata debe identificar una propiedad que controle todos los tamaños y una diferencia verificable respecto de las obstrucciones previas.

WM PROVED: logs110 constructor/audit idénticos (SHA25690a2ec137e806c8a7f8cce975f7af1cee375d9e48bdaf1c5bc302f7c06428539), origen completo y4198 hojas REST contiguas[1/2,845/32], ambos INCONCLUSIVE por8192evaluaciones, sin FULLPASS hasta64. Cola104 analítica desde16 se solapa y completa Wmixed>0 para todo t>0; prefijos103 dan MIXED4. Quedan activadas las consecuencias auditadas112 (Xi positiva, comparación E/Psi, TP2 real/confluencia y cocientes de la pareja límite). No cinco potencias arbitrarias, conservación indefinida, todos los órdenes ni nueva ventana T. Papers intactos; objetivo global OPEN.


**Auditoría transversal posterior a la revisión de POWER:** phase211 `POWER_CORPUS_OPPORTUNITY_AUDIT.md` y `POWER_GLOBAL_ROUTE_REVIEW.md`. Root y tres revisores contrastaron índices, LEDGER y fuentes primarias selectivas; no se afirma relectura exhaustiva del corpus. No se identificó aún una candidata global nueva justificada entre las familias examinadas. Se distinguen falsificadores de clase, reducciones y obligaciones abiertas; no se usa REF-D como imposibilidad. Se corrigieron etiquetas obsoletas de O-151.4 y06R4, y se incorpora la corrección lógica de TB3-neg desdeR186_092. No nueva torre/certificado ni signo global.


### Completitud en potencias perfectas — alcance algebraico y falsificadores auditados

Fuentes phase211:`SQUARE_COMPLETENESS_OBSTRUCTION.md`,`SQUARE_COMPLETENESS_AUDIT.md` (PROVED,sin nuevaejecución). LocalFp=(1+cpz)/(1−z²),0<=cp<=1, daNmultiplicativa0<=N<=1,N(n²)=1,ell>=0. Endpointc20otros1=ζ/(1+2^-s),antecedenteR163102CorF/R163191,residuo2/3sinFEasumida. ReusaMISMOtestigoprimitivopar007_CThm1conx>1; bordesanalíticosdanC_F(log4)>0,asíWnuevo=Wa3−2log2C4<0. CadamFIJO>=2tambiéninsuficienteconNentero0/1:reemplazo2→2^m,N(n^m)=1;param>=3noátomo2antes8⇒Wm=Wa3<0,residuo1/[2(1−2^-m)]<1.

**TODOSlosórdenessimultáneos, sinintegralidad:** local2=(1−z/2+z²/2)/(1−z),otrosprimosordinarios,N2=1/2,N2k=1k>=2⇒N(n^m)=1TODOn,m>=2. Raícesformalesr±=(1±i√7)/4 demuestranell(2^k)/log2=1−r+^k−r-^k>=0. Pesosv2=√2log2/2<1/2,v4=7log2/4 yMISMO007CdanW<−.00528norm². Residuo7/8,noFEasumida;nofalsificaintegralidad/residuo1/compatibilidadadicional.

**Selección/identificación, NOsigno:** enansatzcp∈[0,1],residuoEXACTO1fuerzacp1inclusoinfinitos(producto≤unfactor). Másgeneralmente,Nmultiplicativa+ALLperfectpowers+N(p)entero>=0+ell>=0fuerzaN≡1:ell(p²)/logp=2−c²⇒c0/1,yc0local(1+z³)/(1−z²)daell(p6)/logp=−1. EstoidentificaLambda,nopruebasusigno. Sóloexclusióndesuficienciadelasclasesdeclaradas,NOimposibilidadglobaldetodousodecuadrados/completitud,NOΛnegativa,nuevacoberturaW/Tnicampaña. Auditoríasroot/mapa completadas;papersintactos.


**Ampliación de residuo normalizado (§11, PROVED, misma clase acotada):** se conserva el factorlocal2simultáneo yseañadenfinitosp>=7conPdelta=1+delta z−delta z²,0<=delta<=2/5. Np=1+delta,Npk=1k>=2; factoresr,sdanellodd>0,elleven>=logp/25. DivergenciaΣ1/ppermiteelegirfinitamenteúltimodeltaracionalconproductoderesiduosEXACTO8/7. AsíF=ζR,RDirichletpolynomialfinito,R1=1:residuo1,sumN=x+O1,Nmultiplicativa0<=N<=Cfinito,ALL-POWERSyell>=0. Compensadoresp>=7invisibles007C⇒MISMOvalorW<−.00528norm². NO N<=1 (Np>1altos),NOintegralidad(N2=.5),NOFE/defectoBohrpequeño. AntecedentesLemaSR163102/resnormalR163802;noideaEulerpresentadacomonueva. No contradicecolapsode§7ni197(controlDelta≠residuo). Auditoríasliteralroot/mapa,sin nuevosdatos ni campañas.


### Gram por traslación theta — identidad y obstrucción de capas PSD

**PROVED, alcance limitado.** Fuentes phase211: `POWER_GRAM_SLICES_OBSTRUCTION.md`, `POWER_GRAM_SLICES_AUDIT.md`; auditorías root/casos/mapa, sin certificados nuevos. A(t,s)=integral_0^infinito(t+s+2r)Phi(t+r)Phi(s+r)dr tiene doble transformada [Z′(u)Z(v)+Z(u)Z′(v)]/(u+v), sin factor2. Su desintegración exacta en v da capas Gram para el modelo cuártico. Para Phi REAL no todas pueden ser PSD: la derivada normalizada exige CND de [V′(t)+V′(s)]/(t+s), refutada con tres nodos positivos y V′(R)/R³→infinito. **PSD de A permanece OPEN**; no W negativo, nueva cobertura ni imposibilidad de otro Gram. Dedup dirigido103_47/48,073/074,N_BUILD014/016/018,C9 sin duplicado literal hallado; marco Gram/Pólya clásico, no afirmación de nunca intentado. Compensación conjunta entre capas aún sin cota nueva.


**Addendum Gram — operaciones (PROVED, misma entrada):**074 ya refuta suficiencia de V=g(t²) convexa y con todas sus derivadas no negativas. Mezcla de dos gaussianas distintas falla: (M/u)'=u Var(v)>0 contradice pares001. Convolución conserva el kernel transformado por suma de M; pero mezcla positiva de cuárticas o convolución con un factor cuártico impone cola inferior exp(-Ct⁴), incompatible con Phi real. La corrección hazard DdiagB tiene diagonal (f-tf')/f²<0 por073, no puede descartarse como PSD. Incluso un operador positivo Bop(-Phi')=tPhi existe para la mezcla gaussiana y no basta: la forma A conserva un término de semirrecta no controlado. Sólo suficiencias declaradas refutadas; A real OPEN. NotaGram§7 y auditoría, sin datos nuevos.


### Corrección de cancelación residual L2_BUILD_031 (PROVED)

Fuentes phase211: `CORRECTION_RESIDUE_BALANCE_031.md`, `CORRECTION_RESIDUE_BALANCE_AUDIT_031.md`. La identidad031§3 omite indebidamente módulos p^b<=Q usando B_Q. Contraejemplo exacto M=Q=2,s=(1,1), perfil2T0<log(3/2), interpolante suave S soporte(2/3,5/2),S1=S2=1: W1 tiene filasdelta y la componenteq2 completa es v2/2>0; n>=3 no contribuye. Balance de c2(k) no se transporta a c2(2k). El componente está definido mediante el interpolante explícito030; no se afirma que sea independiente de cualquier interpolación. **TeoremaE de aproximación intacto**, sin W negativo ni cambio del objetivo(S). Aviso añadido a031 preservando texto histórico. Auditoría independiente, sin cómputos/papers.


**Aclaración de reparación031 (misma corrección, PROVED):** en R_Q,Q>=2, exigir anulaciónq2 para TODOS los perfiles e interpolantes deja sólo s0: perfilwidth<log((M+1)/M) daW1delta, soporteimpar hace único el coeficiente deS(j/2), igual a−s_jv2/2. No colapso demostrado en soporte mixto por colisiones diádicas; un ejemplo narrow no decide todos los perfiles. TeoremaE original permanece intacto. Fuente correctiva§5 y auditoría, sin datos nuevos.


**Complemento016§9 — filtro desplazado y límite de las diagonales (PROVED):** en `POWER_DESCENT_AUDIT_016.md`, delta1,u63/2,eta3/4, Qdelta=(s+delta)/(s+u) es un isomorfismo del H_eta fuerte014; su cero externo evita el hiperplano de momento0. Por triangularidad confluente, el SPAN de CUALQUIER cola fr=Qdelta^r/(s+u) es denso. La identidad binomial completa, con d=delta²/u² y producto polar incluido, más015N1, prueba diagonales W[fr] y W4[fr] eventualmente positivas. Sin embargo W4=W−4norm² tiene f0negativo016 y es continua: alguna combinación FINITA de generadores de CADA cola positiva da W4<0. Sólo refuta inferir signo delspan desde densidad+diagonales, aun reparado el momento. NO Wrealnegativa, NOparesPSD ni uniformtodosnumeradores; no nueva familia general cerrada, certificado o ventana. Auditorías root/casos/mapa.


### Ensamblaje PSD de tamaño fijo en la escalera002 — obstrucción limitada (PROVED)

Fuentes phase211: `POWER_FIXED_BLOCK_ASSEMBLY_OBSTRUCTION.md`, `POWER_FIXED_BLOCK_ASSEMBLY_AUDIT.md`. Un certificado C=sum B_alpha, cada B_alpha PSD soportada en<=k coordenadas originales, exige ones^T C ones<=k trC. Para TODO k fijo, n=k+1 y nodos de la MISMA escalera a_j=32+2N+2j dan L(a_j)=.5logN+O_k1, con psi entero y cola Lambda completa; el bloque normalizado tiene Cij→1. Entonces ones^TC ones→n²>kn=k trC y ningún certificado así existe para algún N finito. Submatrices principales heredan esos certificados: tampoco los bloques iniciales002 que contienen el subbloque los admiten. Caso2 incluye ensamblajes PSD2/Gershgorin escalado. Se excluye sumar certificados2/4/13 o tamaño FIJO para todos los órdenes ENBASEoriginal; NO implica K negativa/PSD arbitraria, NOotrasbases/bloquescrecientes/Schur/partePSDglobaldensa. Dedup186043044/N018019: instrumentos clásicos, clases distintas, sin prioridad absoluta. Auditorías root/casos/mapa, sin cómputos/papers; W global OPEN.


### Desplazamiento simultáneo de exponentes: falla el orden Loewner (PROVED)

Fuentes phase211: `POWER_SIMULTANEOUS_SHIFT_OBSTRUCTION.md`, `POWER_SIMULTANEOUS_SHIFT_AUDIT.md`. La diferencia completa D(f,g)=W(f,g)−W(e^(-2t)f,e^(-2t)g) tiene un plano indefinido. Dos paquetes norma1 separados log2, el primero a distanciaO(epsilon) del borde causal0, dan Dff=O(epsilon^(1−2s)),Dgg=O(epsilon^−2s),s1/8, y Dfg→−3log2/(4sqrt2) por el único contacto2; ARCHsuave/polarO(epsilon). Determinante→−9log²2/32<0. Densidad fuerte014 y continuidad transportan esto a un bloque inicial FINITO [K(32+i,32+j)−K(34+i,34+j)] noPSD. Coeficientes de exponentiales DIRECTAS, sin confundir factoreszeta de rho. AntecedenteN007atom/bump: aquí el borde suprime una diagonal del DEFECTOfullW y paga la reservaARCH antes ausente. Orden contrario ya falla diagonalmente073. Sólo se refuta esta ordenación universalshift2; NO Wnegativa/Knegativa/otros transportes ni todosshifts. Auditorías root/casos/mapa/invariante, sin datos/certificados/papers.


**Addendum IMS al desplazamiento simultáneo (misma entrada, PROVED):** fuenteSHIFT§7 y auditoría. T=e^(-2t),S=sqrt(1−T²),d=1−TtTs−StSs>=0. R=D−W[Sf] conserva ARCH, peine y polar2cosh. Los MISMOS paquetes causales dan Rff=O(epsilon),Rgg=O(epsilon²),Rfg→−3v2/8 y R[f±g]→∓3v2/4; restoIMSindefinido, noWnegativa. Para compactos separados de0, suma_r R[T^r f] tiene coeficiente exacto d/(1−TtTs)∈[0,1], cuyo límite al(0,log2) es1, no0. Convergencia justificada; S no se supone Lipschitz en0. AntecedenteIMS004 explícito; no signo/cancelación global inferidos ni exclusión de otro compensador con prueba propia. Root/mapa literal aprobado, sin nuevos datos/papers.


**Aclaración al objetivo anti-Löwner/Stieltjes (PROVED, no nueva nota):** `POWER_GLOBAL_ROUTE_REVIEW.md`, sección L-DER. L'(a)=Laplace[b(t)dt+ΣLambda(n)logn delta_logn], b=t[(exp2t−1)^−1−exp t]. Tras cualquier tiltA>1 la medida es finita; en(log2,log3) no hay átomos y b<0. No puede existir una medida Laplace POSITIVA que represente L' en NINGUNA raya a>=a0>1. Unicidad autocontenida: tilt, pushx=e^(-t), igualdad de todos los momentos, aproximación polinomial de continuas. AntecedenteformalPaper37cor:bernstein para OTROcociclo;019/020/023 tratan inversoMöbiusgamma, noL'. NO excluye N(x)=M(sqrtx)/sqrtx Stieltjes, NO K/Wnegativas. Es una prevención de ‘Gamma positivo⇒L' positivo como medida’, no cierre del objetivo083. Sin datos/papers.


**Addendum027§8 — inversos gaussianos uniformes refutados (PROVED, misma mezcla real):** `POWER_INTERIOR_CONSTRAINT_027.md` y `POWER_JOINT_AUDIT_027.md`. Para w_a=x^(-1/2)e^(-a log²x), H_a=−w_a'>0, definir FULLh_a=Σmu(m)mH_a(mx),J_a=Σmu(m)w_a(mx),K_a=J_a+xh_a. LeyFIJAV_N inversagamma027 y Tonelli positivo+FubiniABSOLUTO (ΣmH_N(m),Σw_N(m) finitas) dan h_N(1)=E h_VN(1),K_N(1)=E K_VN(1). NEGCOMPLETO022 h128(1)<−33/50 y023 K129(1)<−1/251 fuerzan EXISTENCIAS a_h>0 con h_a_h(1)<0 y a_K>0 conK_a_K(1)<0; parámetros posiblementeDISTINTOS, ninguno calculado. No son prefijos ni Jensen/convexidadW. Refuta ambas premisas gaussianasUNIVERSALES de inverso positivo; NO ERR/Wnegativas, NOheatH_A−Pnegativo, NONStieltjesexcluido. Sin nuevosdatos/certificados/papers; auditoríasroot/mapa/invariante.


### Modelo hiperbólico: Green positivo todos los órdenes; transferencia real abierta

**PROVED para el modelo / OPEN para Phi real.** Fuente phase211: `POWER_HYPERBOLIC_MODEL_GRAM.md`. Para phi_a(t)=exp(−a cosh(2t)), a>0, Z_a(u)=K_(u/2)(a), H_a=−D_r²+a²exp(2r) en la semirrecta con borde Dirichlet y R_i=(H_a+u_i²/4)^−1. La identidad positiva M_a(u)/u=(1/2)Tr R_u produce
K_M(u_i,u_j)=(1/2)Tr(H_a R_i R_j)+(u_i u_j/8)Tr(R_i R_j),
una suma de Gram positiva para TODOS los órdenes. Prueba mediante Green/ODE y trazas, sin nuevos datos. Las capas de la desintegración GramSlices NO son todas PSD incluso en este modelo, pues V'(R)/R³→infinito; el Green prueba el kernel completo de M, sin requerir positividad de cada capa. Cotejo dirigido de antecedentes no halló esta aplicación literal; no se afirma prioridad mundial. Auditorías root/casos/invariante, cotejo mapa. La supercola compatible con theta no transfiere la representación: falta una identidad ODE/Green positiva para la Phi REAL; mezclar densidades positivas tampoco preserva automáticamente el kernel logarítmico. NO nueva cobertura W/T ni cierre global real; papers intactos.


**Modelo hiperbólico, §7 — dos transferencias directas excluidas (PROVED, alcance restringido).** `POWER_HYPERBOLIC_MODEL_GRAM.md` conserva el Gram positivo del modelo y prueba que Phi real no es ni una mezcla positiva pura de exp(-a cosh(2t)) (se permite masa infinita, con integral exp(-a)dmu finita), ni phi_a convolucionada con una medida positiva finita no nula (sin suponer soporte compacto). La cola real es 2pi² exp(9t/2)exp(-pi exp(2t)): su tasa obliga el soporte extremo y la representación impondría un prefactor acotado, contradicción. Diferencia frente a la exclusión cuártica de GRAM_SLICES§7: mismo orden doble exponencial, pero prefactor incompatible. Revisión root/casos/invariante. No excluye prefactores temporales, diferenciaciones, combinaciones firmadas ni otros Green; no W negativa, nueva T ni cierre global. Sin datos nuevos ni cambios en papers.


**Modelo hiperbólico, §8 — prefactor afín mediante Robin (PROVED sólo para el modelo).** `POWER_HYPERBOLIC_MODEL_GRAM.md`: para a>0,beta>=0, phi=(beta+a cosh(2t))exp(-a cosh(2t)) tiene transformada beta*y_x(0)-y_x'(0), x=u²/4. Con m=-y'/y y k=y/y(0), m'=integral k² y R_beta=R_D+k tensor k/(m+beta); el borde es f'(0)=beta f(0), con término positivo beta|f(0)|² en la forma. La identidad M/u=(1/2)Tr R_beta y el Gram completo prueban todos los órdenes. Neumann beta=0 corresponde a la derivación de escala; no se afirma preservación por derivaciones generales. El prefactor exp(2t) no es el exp(9t/2) de theta: transferencia real OPEN, sin W/T nueva. Revisión root/casos/invariante, cotejo dirigido mapa, sin prioridad mundial ni nuevos cómputos; papers intactos.


**Modelo hiperbólico, §9 — orden matricial del flujo de escala refutado (PROVED sólo para el modelo).** `POWER_HYPERBOLIC_MODEL_GRAM.md`: aunque cada K_a es PSD, D_a=-a partial_a K_a no lo es en todos los tamaños sobre u>0. La representación P_a(x)=Tr[(H+x/4)^(-1)V_a(H+x/4)^(-1)] tiene coeficientes alternados A_n=(n+1)sum w_j t_j^n, w_j>0. El mayor t_j aislado da A_n A_(n+2)-A_(n+1)^2<0 eventualmente, con error O(n²rho^n). PSD de D_a exigiría los menores opuestos por diferencias finitas desde nodos positivos y los jets pares. No teorema externo Stieltjes ni argumento sobre ceros; sin tamaño evaluado ni campaña. Diferencia SHIFT: escala de densidad auxiliar, no exponentes de tests reales. Revisión root/casos/invariante. NO derivada theta refutada, NO W negativa, NO nueva T; permanece válido el Gram del modelo. No transferir monotonía matricial desde sus diagonales.


**Modelo hiperbólico, §10 — rigidez del prefactor fijo (PROVED, clase restringida).** Fuente phase211: `POWER_HYPERBOLIC_MODEL_GRAM.md`. Para Y_nu(b)=integral exp(-b cosh v)q(v)cosh(nu v)dv, q par C² positiva y q,q',q'' de crecimiento a lo sumo exponencial, la fuente de la ecuación en r=log(b/a) es F_nu=integral exp(-b cosh v)[-q''+2b sinh(v)q']cosh(nu v)dv. Si F_nu(b)=E(b)Y_nu(b) con E independiente de nu en sólo dos escalas distintas y un intervalo abierto de nu, unicidad de la transformada y evaluación en v=0 fuerzan q constante. La q real=Phi(v/2)exp(2pi cosh v) crece como exp(9v/4), por lo que esa transferencia escalar directa falla. Diferencia§7: admite prefactor temporal fijo, exige potencial independiente del parámetro. No excluye otros Green, gauges, sistemas ni prefactores dependientes de escala; Robin§8 no pertenece a esta clase. Revisión root/casos/invariante, dedup dirigido mapa; no W negativa, cierre global ni nueva T. Sin cómputos ni cambios en papers.


**Ampliación de la misma clase, modelo§10.1 (PROVED):** admitir Y_rr=A(b)Y_r+[b²+nu²+E(b)]Y, con A,E independientes de nu y el mismo prefactor fijo q, sólo permite q=C o q=C cosh(v/2). Restar dos escalas en la identidad inversa fuerza q=C cosh(v/2)^alpha; la independencia de1,cosh(v),sech²(v/2) fuerza alpha=0 o1. La q theta, de crecimiento exp(9v/4), no pertenece a esta clase. Incluye la imposibilidad de reparar esta familia mediante multiplicación escalar g(r) independiente de nu para obtener z_rr=[nu²+V(r)]z. No excluye otros cambios de variable, transformaciones integrales, prefactores dependientes de escala o sistemas. Diferencia explícita frente§10: ahora se permite primera derivada. Revisión root/casos y dedup mapa; sin signo nuevo ni modificaciones de papers.


**Precisión adicional de§10.1, sólo para q theta:** permitir Y_rr=A Y_r+[w(b)nu²+B]Y tampoco repara esta familia. Invertir la transformada cosh y usar q'/q=9/4+O(exp(-v)), q''/q=81/16+O(exp(-v)) fuerza w=1 por el término dominante (1-w)b²cosh²(v). Así queda excluida también una reparametrización C² de escala con derivada no nula acompañada de multiplicación escalar, ambas independientes de nu, que pretendan dar z_tt=[nu²+V(t)]z. Prueba en la misma§10.1, revisión root/casos y cotejo mapa. No clasificación para q arbitraria ni exclusión de otras familias/sistemas; sin nuevo signo.


**Precisión del puente temporal GramSlices§2.1 (PROVED, sin signo real nuevo):** bajo DOM gaussiana, A es PSD en toda R si y sólo si K_M es PSD para todos los tamaños con nodos en cualquier intervalo abierto positivo fijado. La recíproca usa continuidad de la forma en L²(exp(-Nt²)dt), densidad de exponenciales con exponentes CONTINUOS por unicidad de transformada entera, y aproximación de deltas. No afirma densidad de una escalera discreta bajo cota gaussiana ni suficiencia de un tamaño fijo. La nota existente POWER_GRAM_SLICES_OBSTRUCTION incorpora la prueba; revisión literal root/casos y dedup mapa. El Gram hiperbólico sí firma por ello su A temporal completo; no el real. Es precisión de representación, no atajo ni ampliación T.


**Corrección de alcance temporal, GramSlices§2.2 (PROVED, sin signo nuevo):** A_theta es conjuntamente holomorfo en |Im t|,|Im s|<pi/4 por dominación uniforme de su integral theta. PSD de TODOS los tamaños en cualquier intervalo temporal abierto implica PSD en toda R: diferencias finitas dan matrices mixtas de jets y puntos viejos; Taylor doble y simple conserva también los cruces al ampliar el intervalo, y se itera con radio fijo. Por ello A++ PSD no dejaría una obligación independiente de cruces; queda corregida esa cautela anterior. No se ha probado A++ ni basta orden finito. Fuente existente POWER_GRAM_SLICES_OBSTRUCTION§2.2, revisión root/casos y cotejo mapa; sin prioridad mundial ni nueva T.


**GramSlices§8 — modos theta individuales no PSD ni localmente (PROVED, clase restringida).** Phi_n(t)=n^(-1/2)h(t+log n), y el kernel modal A_n tiene límite diagonal al−infinito (2H/n)(m-log n)<0 para TODOS n>=1. El momento m<0 se prueba por dos recurrencias de integrales gamma y Jensen: m<(1/2)log(5/(4pi))<0. Holomorfía en strips y propagación§2.2 implican que A_n no es PSD de todos los tamaños en ningún intervalo abierto, incluso en la cola donde Phi_n es positiva. Diferencia frente a la traslación modal ya registrada103_47/48: falsificador global y alcance local, no sólo identidad. No refuta A_theta completo, que conserva pares cruzados n,m; no estima comparación relativa ni amplía T. Fuente POWER_GRAM_SLICES_OBSTRUCTION§8, revisión root/casos y cotejo mapa, sin datos nuevos ni cambios en papers.


**GramSlices§8.1 — prefijos theta completos no PSD eventualmente (PROVED, cruces conservados).** Para Phi_M=sum_(n<=M)Phi_n, M^(-1/2)Phi_M(x-log M) converge en L²((1+|x|)dx) a F(x)=-pi exp(5x/2)exp(-pi exp(2x)). Suma Riemann y mayorantes uniformes Ce^(5x/2) a izquierda, Ce^(-x/2) a derecha. Luego integral tPhi_M²/(Mlog M)→-||F||²<0: todos los prefijos suficientemente grandes tienen diagonal negativa en su kernel A cerca de−infinito y, por continuación analítica, noPSD en ningún intervalo abierto. Diferencia§8: se incluyen TODOS los pares n,m<=M. No umbral numérico, no fallo de Atheta infinito ni exclusión de compensar la cola; sólo impide usar prefijos eventualmentePSD. Fuente POWER_GRAM_SLICES_OBSTRUCTION§8.1; revisión root/casos y dedup mapa, papers intactos.


**GramSlices§8.2 — primera corrección continua tampoco da aproximantes PSD (PROVED).** Q_M=Phi_M+pi M³exp(5t/2)exp(-pi M²exp(2t)) añade la cola modal integrada. Ahora Q_M→Phi en L²(1+|t|), pero integral tQ_M²=−||h||² logM/(4M)+O(1/M+logM/M^(3/2))<0 eventualmente. Trapecios de la cola aíslan h(t+logM)/(2sqrtM) con resto global controlado; se estiman también todos los cruces conPhi. La diagonal negativa y continuación analítica excluyen PSD local de todos los órdenes. Diferencia§8.1: aproximante corregido con convergencia global, no prefijo bruto. No refuta la positividad del límite ni otras correcciones. Fuente POWER_GRAM_SLICES_OBSTRUCTION§8.2; revisión root/casos y cotejo mapa, sin campaña ni cambios en papers.


**GramSlices§8.3 — simetrización corregida refutada para TODO M>=1 (PROVED).** S_M=(Q_M+Q_M reflejado)/2 elimina el momento impar, pero tiene masa>=C>0 y cola −[pi M(3M+1)/4]exp(-5|t|/2). Su transformada Z_M(u) tiende a−infinito al aproximarse u=5/2 desde abajo; valor medio antes del nivel positivo Z_M(0)/2 da Z_M>0,Z_M'<0. LT absolutamente justificada por cota exponencial bilateral produce un test cuadrático negativo ZZ'/u. Continuación analítica excluye PSD en cualquier intervalo. Cambio§8.2: paridad restaurada, falsificador distinto que conserva toda la forma; no se usan ceros. No refuta Phi real ni otras reparaciones. Fuente POWER_GRAM_SLICES_OBSTRUCTION§8.3; revisión root/casos y cotejo mapa, sin datos ni cambios en papers.


**Alcance de GramSlices§§8–8.3:** cualquier reparación que coincida con uno de los aproximantes excluidos en una semirrecta derecha conserva su matriz negativa local: A_psi=A_f allí por r>=0. Incluye reflexiones y suavizados sólo a izquierda, aun sin analiticidad depsi. Mantiene los alcances de índices de cada resultado; no excluye modificar la cola derecha ni firmaPhi. Consecuencia revisada root/casos, añadida a la misma fuente, sin nueva ruta.


**Fortalecimiento de GramSlices§8.1: TODO prefijo bruto, M>=1, fallaPSD.** Z_[Phi_M](u)=(u-1/2)H_M(u), H_M(u)=½pi^(-u/2-1/4)Gamma(u/2+5/4)sum_(n<=M)n^(-u-1/2)>0. Para u positivo cercano a1/2 por debajo, Z<0,Z'>0; LT da test negativo ZZ'/u. Convergencia absoluta sin paridad por |A|<=B(t)B(s), B(t)²=integral_t∞(1+x²)Phi_M². Continuación analítica da fallo local en todo intervalo. Sustituye el alcance eventual del descarte de prefijos brutos y sus reparaciones sólo a izquierda; mantiene intactos la asintótica de masa y el alcance eventual deQ_M. Revisión root/casos, sin datos ni signo real nuevo.


**GramSlices, extensión modal a cortes suaves infinitos (PROVED):** w_n>=0 nozero, sum w_n n²<infinito implica que A de phi_w=sum w_n Phi_n no es PSD en ningún intervalo abierto. Fubini y diferenciación dan Z=(u-1/2)C(u)sum w_n n^(-u-1/2), con factor restante positivo C¹; el test ZZ'/u es negativo inmediatamente a izquierda de1/2. Cotas en substrips y B justifican todo sin momentos adicionales. Incluye exp(-epsilon n²), no heat temporal ni w_n=1. Cambio frente al prefijo: soporte infinito suavizado, todos los cruces conservados. Fuente POWER_GRAM_SLICES_OBSTRUCTION, revisión root/casos y cotejo mapa; sin signo real nuevo ni papers modificados.


**Modelo hiperbólico, §11 — productos temporales de cosh excluidos (PROVED, clase exacta).** Fuente phase211: `POWER_HYPERBOLIC_MODEL_GRAM.md`. No existe Phi(t)=C exp(-a cosh(2t)) prod_j cosh(alpha_j t) con C,a>0, alpha_j>0 y sum alpha_j² finita, producto finito o numerable. La tasa fuerza a=2pi; log Q/t fuerza sum alpha_j=9/2. Infinitos factores anulan el coeficiente principal normalizado, incompatible con2pi². Para finitos, la primera corrección theta exige alpha_min=1 y multiplicidad entera k=pi-3/(2pi), entre2 y3: imposible. Diferencia§7/§10: multiplicación temporal exacta, sin hipótesis de ODE ni de preservación del signo. No excluye potencias reales de cosh, cocientes, sumas, otras aproximaciones ni comparación relativa; tampoco decide preservación abstracta por cosh. Revisión matemática root/casos y dedup dirigido mapa; sin cómputos, signo real nuevo, ampliaciónT ni cambios en papers.


**Núcleo temporal, §8.4 — momento exponencial cancelado y producto de Jacobi (PROVED, clase explícita).** Fuente phase211: `POWER_GRAM_SLICES_OBSTRUCTION.md`. Para phi real no nula, continua, con caída exponencial a izquierda y superexponencial a derecha, integral exp(ct)phi=0 con c>0 excluye PSD de A_phi: la identidad LT absoluta daría (Z_phi²)' >=0 hasta Z_phi(c)²=0, contradiciendo unicidad Laplace. Con holomorfía conjunta de A,§2.2 excluye PSD en cualquier intervalo abierto. Aplicación: phi_P=(D²-1/4)[exp(t/2)P(exp(-pi exp(2t)))]/4 para TODO polinomio real no constante P; el momento c=1/2 se anula conservando los bordes. Incluye cortes J>=1 del producto Jacobi, con todos sus coeficientes firmados y cruces. Diferencia frente cortes positivos previos: no exige signo de phi ni de los pesos; usa cancelación exacta de un momento. No pasa al producto infinito/Phi completa, cuyo momento es positivo. Revisión matemática root/casos y cotejo dirigido mapa; identidad clásica citada DLMF20.5.3, no prioridad mundial, sin cómputos ni nuevaW/T.


**Núcleo temporal, §8.5 — Jacobi simetrizado, corolario de pares001 (PROVED).** Fuente phase211: `POWER_GRAM_SLICES_OBSTRUCTION.md`. Para todo J>=1, S_J=(phi_PJ+phi_PJ reflejada)/2 tiene cola POSITIVA D_J exp(-beta|t|), beta=2J+1/2, D_J=(8^J J!pi^J)(beta²-1/4)/8. En nodos beta-epsilon,beta-2epsilon, epsilon K converge a [[2,3/2],[3/2,1]]/(2beta), de determinante negativo. LT absoluta y continuación§2.2 excluyen PSD de A_SJ en cualquier intervalo. Se atribuye el criterio de pares aCONE001, no novedad general; aplicación diferente de§8.4(momento cancelado) y§8.3(cola negativa/diagonal negativa). No afirma S_J positivo en toda la recta ni refutaPhi; otras reparaciones y globalOPEN. Revisión root/casos y dedup dirigido mapa; sin cómputos ni nuevaT.


**Núcleo temporal, §2.3 — alcance de la factorización Hankel traslacional (PROVED; antecedente clásico).** `POWER_GRAM_SLICES_OBSTRUCTION.md`: A no admite integral_0^infinito<h(t+r),h(s+r)>dr, incluso con h medible de valores en un Hilbert e integrales diagonales finitas. La diferencia bajo traslación común sería PSD; su derivada fuerza(t+s)Phi(t)Phi(s) PSD, pero su menor2 es negativo. Antecedente: Blower, https://eprints.lancs.ac.uk/id/eprint/615/1/integrablepaper.pdf, Thm1.2 y§2.5(2.14); no novedad atribuida al mecanismo. Sólo esas variables y esa representación: no refuta PSD deA, otrosGram, otrascoordenadas ni la suma de productos Hankel. Revisión root/fresh_global, sin datos nuevos ni signo/T.


**Núcleo temporal, §8.6 — deformación modal n^(-delta), todo delta distinto de0 (PROVED).** Fuente phase211: `POWER_GRAM_SLICES_OBSTRUCTION.md`. Para phi_delta=sum n^(-delta)Phi_n, la suma infinita y todos sus cruces se conservan. Z_delta=C(u)(u-1/2)sum n^(-u-1/2-delta), absolutamente para u>max(-5/2,1/2-delta). Delta>0: Z<0,Z'>0 justo a izquierda de1/2. Delta<0: al bajar u a c=1/2-delta desde arriba, Z~D/(u-c),Z'~-D/(u-c)²,D>0, por comparación elemental suma-integral. LT absoluta produce test negativo; holomorfía conjunta y§2.2 excluyen PSD de A_delta en cualquier intervalo. Diferencia frente cortes suaves: cubre amortiguaciones arbitrariamente débiles, antes sólo delta>3; no paridad ni cota gaussiana izquierda supuestas. Delta0 NOcubierto: Z_Phi(1/2)=1/4, mientras Z_delta(1/2)=0 para todo delta>0; distancia L1 con pesoexp(t/2)>=1/4 pese a convergencia compacta. Revisión root/casos y dedup dirigido mapa. No signo negativo dePhi/W, nuevaT, cómputos ni cambios en papers.


**Núcleo temporal, §7.1 — convolución gaussiana, equivalencia global por nodo remoto (PROVED).** Fuente phase211: `POWER_GRAM_SLICES_OBSTRUCTION.md`. Si K(u,R),K(R,R)->0, entonces K+b PSD en todos los bloques finitos equivale a K PSD para b>=0: añadir nodoR y coeficiente menos la suma de los originales elimina el rango uno y recupera cualquier valor negativo al hacerR->infinito. ParaPhi, cotas gaussianas para todoN y convexidad de logZ prueban M(R)/R->0. Convolucionar con gaussiana de varianza sigma² añade exactamente sigma² aK; así basta una prueba independiente para UN sigma fijo. Normalizar la densidad por exp(-sigma²/8) conserva Z(1/2)=1/4 sin cambiarK. Diferencia frente§7: recíproca, no nueva preservación; distinto de multiplicar la densidad por exp(lambda t²). NOsigno suavizado demostrado, NOequivalencia de tamaño fijo/rangoacotado, NOprohibición de usar esta reformulación constructivamente. Revisión root/casos y cotejo mapa; sin nuevos datos ni W/T.

### 2026-11-05 — Criterio logarítmico: falsificador cuártico de una inferencia general

`POWER_GRAM_SLICES_OBSTRUCTION.md`§4.1: PROVED, root/theta_joint, dedup mapa. Para phi=exp(-a t^4), a>0, A y todas sus capas son PSD (§4), pero log A no es condicionalmente positivo: el coeficiente t^5s^5 es (51/120)(4a)^5 kappa_5(V)<0 para V de densidad proporcional a exp(-2av²); quinta diferencia en seis nodos da falsificador. Alcance: PSD/capas positivas NO implican infinita divisibilidad del kernel normalizado. No refuta la Phi real. Un único bloque real de cinco nodos no dio falsificador numérico, sin certificado ni extrapolación. La condición logarítmica real sigue OPEN; no nueva positividad W/T. Diferencia frente CND de capas: se estudia logaritmo del integral completo. Papers intactos.

**Actualización CPD, 2026-11-06 (misma entrada).** GRAM§4.1, PROVED global_restart_checked/root; auditoría independiente arithmetic_fresh_candidate PASS y root PASS para ambos mecanismos. Para z=x+iy,x>=0, la identidad F²H=4D+L²+2xbL-Fb usa F=A(z,bar z)>0,b=|Phi(z)|²,L=integral_x^infinito|Phi|² y D=(F/2)min_(a complejo)integral_x^infinito v|Phi'-aPhi|²>=0. En x0, LARGE da L>=c epsilon^-4, la cota global F<=C epsilon^-5 y SMALL b<=C epsilon^-N exp(-a/epsilon): H>0 eventualmente. En x=h=log2/2, Poisson completo hasta3deriv da perfil C1 f=(1+2iu)^(-5/2),u∈[0,1], con min_beta integral|f'-beta f|²>=1/9375; la restricción local del mínimo paga Fb y prueba H>0 eventualmente sin aproximar Ftotal. Cotejo dirigido sin antecedente literal localizado. Pasan sólo esos dos tests diagonales complejos; CPD y signo global OPEN. Sin umbral numérico, asintótica local7/16 del H completo, nueva ruta, cobertura W/T, cómputos ni papers editados.

**Alcance de la extensión conjunta CPD (misma entrada).** GRAM§4.1, PROVED global_restart_checked/root, auditoría independiente arithmetic_fresh_candidate PASS y root PASS; cotejo dirigido sin antecedente literal localizado. Fijados z0,I,peso positivo, para f_eta(u)=Phi(z0+eta+u) y P_eta proyección al span{f0,f_eta}, R_ij=<(I-P_eta)f_i',(I-P_eta)f_j'> no domina c bb* con c>0 uniforme en eta, b_i=f_i(0): R_00<=||f0'-(f_eta-f0)/eta||²=O(|eta|²), pero |b0|²>0 fijo. eta=i tau mantiene las partes reales; resto C2 uniforme, sin exigir independencia. Sólo ese residual/borde y uniformidad: no excluye c(eta), renormalizaciones por separación, otros términos/bordes/proyecciones ni Gram general. S=A^(odot2)odot H PSD no implica H PSD. CPD/global OPEN; sin nueva ruta, W/T, cómputos ni papers.

**Promedio horizontal, alcance CPD (misma entrada).** GRAM§4.1, PROVED root/global_restart_checked/joint_sign_fresh_review, auditoría independiente arithmetic_fresh_candidate PASS y root PASS; cotejo dirigido sin antecedente literal localizado. Para B_y=integral_2^4[logt/(2t)]|Phi(.5logt+iy)|²dt y epsilon=cos2y, epsilon^(9/2)B_y->315(log2)²/(512sqrt2). Diagonal modal por Riemann gaussiana uniforme; cruces COMPLETOS por IBP <=Cepsilon^-4(1+log1/epsilon), término inferior y cross o(epsilon^-9/2). Luego A(iy,-iy)>=c epsilon^-9/2. El segmento[h,h+c0epsilon],h=.5log2,c0 fijo, aporta O(epsilon^-4), proporción O(sqrt epsilon)->0. Equivalente SÓLO de B_y; no de A total ni H, ni bandas arbitrarias. No nueva positividad matricial, CPD, W/T ni ruta; signo global OPEN, sin cómputos/papers.

### 2026-11-05 — Theta completa: fallo de log-supermodularidad temporal

`POWER_GRAM_SLICES_OBSTRUCTION.md`§4.2, PROVED root/theta_joint/casos, cotejo mapa. Para A temporal COMPLETO y s en cualquier compacto positivo, H=partial_t partial_s log A=-1/(t+s)²+O(exp(-2t))<0 cuando t crece. Prueba por v=pi exp(2t)(exp(2r)-1), expansión con restos diferenciados hasta orden2 y cola theta completa. Así A no es TP2 global; no puede cerrarse la vía por positividad puntual de H ni por features todas no negativas de H. Diferencia frente§5: integral completo, no capas; TP2 de073/112 pertenece a otros objetos. Alcance restringido: NO refuta PSD de H, CPD de log A ni PSD de A; menores rectangulares negativos no son menores principales. Sin signo W/T nuevo, papers intactos.

### 2026-11-05 — Modelos principales de cola indefinidos en todo intervalo

`POWER_GRAM_SLICES_OBSTRUCTION.md`§4.3, PROVED root/casos/theta_joint, dedup mapa. G0=(t+s)/(exp(2t)+exp(2s)) y H0=sech²(t−s)−1/(t+s)² no son PSD en TODOS los tamaños sobre ningún intervalo positivo, incluidas colas arbitrariamente lejanas. Corolario de continuación analítica§2.2: G0 llega a diagonal negativa t<0; H0 a H0(1/4,1/4)=-3. La expansión theta completa en t=L+x,s=L+y aproxima ambos modelos con error de entradas O(exp(-2L)), incluido control C² para log A, pero no transfiere su indefinición al kernel real. Se descarta usarlos como referencia PSD o mediante un sándwich multiplicativo simétrico. No se refuta A/H reales ni otras compensaciones; sin nueva W/T, papers intactos.

### 2026-11-05 — Cercanía relativa de densidades no conserva positividad

`POWER_GRAM_SLICES_OBSTRUCTION.md`§8.7, PROVED root/casos/theta_joint, cotejo mapa. Para cada epsilon>0 se construye psi positiva, par, holomorfa en el mismo strip que Phi, con sup|psi/Phi-1|<epsilon y psi/Phi→1 en ambas colas, cuyo A no es PSD en ningún intervalo. Reparación suave que coincide con Phi_M en cola hereda su bloque negativo; mollificar el ERROR RELATIVO por gaussiana produce analiticidad y conserva ese bloque por continuidad. La razón modal da epsilon_M<=4(M+1)^4 exp[-pi((M+1)²-1)]. Se conservan expansiones relativas exponenciales de todo orden fijo, no momentos exactos ni transseries aritméticas. Diferencia frente8.2/8.3: positividad/paridad/analyticidad y error relativo uniforme simultáneos. No es un contraejemplo a A_Phi; no garantiza ni excluye control en norma de formas o normas analíticas fuertes. Sin nueva W/T, datos numéricos ni cambios en papers.

### 2026-11-05 — Aproximantes analíticos negativos con momentos finitos exactos

`POWER_GRAM_SLICES_OBSTRUCTION.md`§8.8, PROVED root/casos, cotejo mapa. La construcción8.7 admite cualquier familia FINITA de pesos pares continuos independientes en(-1,1), integrables contraPhi: corregir momentos con bumps relativos compactos antes de mollificar y resolver el pequeño residual con los mismos bumps mollificados. Positividad/paridad/analyticidad, error relativo arbitrariamente pequeño y colas persisten, así como el bloque negativo fijado. Para pesos cosh(u_i t),t sinh(u_i t), conserva EXACTAMENTE cualquier colección finita de bloques K reales. La conclusión8.8 por sí sola no garantiza las familias infinitas de2/3/4generadores; ver8.9 para hasta4. No conserva estructura aritmética completa ni refutaPhi. Diferencia frente018/8.7: densidad real regular cercana y datos finitos exactos simultáneos. Sin nueva W/T ni papers editados.

### 2026-11-05 — Todos los cuatro generadores pueden coexistir con fallo global en aproximantes

`POWER_GRAM_SLICES_OBSTRUCTION.md`§8.9, PROVED preservador/root, revisión casos, dedup mapa. Existe delta_*>0 para el que ||psi/Phi-1||_20<delta_* conserva K_psi PD en TODOS los bloques de<=4 nodos distintos u>1/2. El bound Delta M^(k)=O(delta u^-8(1+logu)^4),k<=3, conserva los numeradores estrictos084/085; T>0 y las colas recuperan crecimiento/concavidad y los signos083 sin asumirBASE073 para psi. Los aproximantes8.8 entran en esa norma sin perder su bloque negativo, analiticidad, paridad, colas y momentos finitos exactos. Diferencia frente8.8: familia CONTINUA completa de orden4, no bloques concretos; controla confluencias y escape mediante criterios escalares. No preserva identidad aritmética theta; la extensión a todoslos13de053 se trata en8.10. NOrefutaPhi ni da nuevaW/T. Sin cómputos ni papers editados.

### 2026-11-05 — Control relativo por Cayley/Newton y estabilidad de trece tasas arbitrarias

`POWER_GRAM_SLICES_OBSTRUCTION.md`§8.10, PROVED root/preservador, revisión casos, dedup dirigido mapa. En el espacio de exponenciales por polinomios de dimensión<=13, A=-D es accretivo y Q=(A-a)/(A+a) contractivo. Interpolación Newton/Hermite de F(z)=Delta M(a(1+z)/(1-z)) da un bound de Delta K RELATIVO a la Gram de Cauchy, uniforme en colisiones/escape, sin asumir Delta M globalmente holomorfa. Error relativo de densidad en norma100 controla C12 de F. El margen053 de1/4000 conserva1/8000 para psi suficientemente cercana, todos13polos>=63/2, incluidos polos múltiples. Los aproximantes8.8 pueden conservar esto, TODOS4admisibles y datos finitos exactos, manteniendo fallo global en un bloque de másde13nodos altos. No preserva aritmética theta ni todaslasdimensiones; NOrefutaPhi ni amplíaW/T. Sin datos numéricos/papers.

### 2026-11-06 — Imposibilidad de un margen Cauchy uniforme en dimensión

`POWER_GRAM_SLICES_OBSTRUCTION.md`§8.11, PROVED root/casos/preservador, cotejo mapa. Para M real analítica positiva-variable con M(u)=O(u) en0, ningún K_M-c/(u+v), c>0, es PSD en todos los órdenes sobre ningún intervalo abierto positivo. Continuación analítica por jets hasta un punto pequeño contradice la diagonal M(u)/u-c/(2u). Aplica a Phi REAL y al modelo hiperbólico, sin suponer ni refutar K_M PSD. Impide extender el margen053 o8.10 a todos los órdenes mediante una constante positiva fija, incluso en tasas altas. No excluye no negatividad sin margen, comparaciones relativas distintas ni prueba global. Sin nuevos cálculos ni papers editados.


### Phase211 — covarianza divisorial agrupada (2026-11-06)

PROVED/revisado root-casos, cotejo dirigido mapa: `POWER_GLOBAL_ROUTE_REVIEW.md`, sección «Covarianza divisorial agrupada». Para C_s(n)=sum_(dm=n)mu(d)log(m)(gcd(d,m)^s-1), s>0, C_s(p²)=-(p^s-1)logp<0, mientras C_s(p²q²)=(q^s-1)(p^s-2)logp+(p^s-1)(q^s-2)logq>0 si p^s,q^s>2 (s=1/2: p5,q7). Se conserva toda la cancelación por producto n. Antecedente del factor:209 CONSTRUCTOR005; desintegración distinta:106114. FALSIFIED sólo signo uniforme de coeficientes del resto mixto, NO signo de la forma ni compensación conjunta con ARCH. No nueva W/T ni cambios en papers.


### Phase211 — resto divisorial indefinido en el portador primitivo (2026-11-06)

PROVED/revisado root-casos, dedup mapa; `POWER_GLOBAL_ROUTE_REVIEW.md`, «El resto divisorial es indefinido». Se fortalece el resultado de coeficientes: R(F)=sum n^(-1/2)C_(1/2)(n)Re c_F(logn) toma ambos signos en tests reales pares C_c^infinito con ambos momentos polares cero, en una misma ventana T=3log4+1/100000. Trenes de bumps espaciados log4, coeficientes (1,-5/2,1) y (1,-3/2,-1/2,-1/2,-1/2,-3/2,1), dan respectivamente R/(kappa||g||²)=7/4 y -1/4, kappa=(sqrt2-1)log2. Todos los contactos quedan tratados por aislamiento exacto; no barrido. FALSIFIED sólo R>=0 o R<=0 universal como pieza aislada; compensación conjunta con ARCH/medias y signo de W siguen OPEN. No nueva W/T ni cambios en papers.


### Phase211 — comparador Robin ajustado, falsificador de dos nodos (2026-11-06)

PROVED/revisado root/casos/preservador, cotejo mapa; `POWER_GLOBAL_ROUTE_REVIEW.md`, «Comparador Robin ajustado». Modelo positivo M_*=wb M_R(bu), w7/2,b2/7,a4pi/7,beta4pi²/49-33/392, coincide con M_Phi hasta u^-2 pero D=M_Phi-M_*=d/u³+O(u^-7/2), d>0. El resto K_D en nodos u,2u tiene det=-5d²/(64u⁸)+O(u^-17/2)<0 para u grande. FALSIFIED sólo esa comparación aditiva PSD; ambos kernels individuales no quedan refutados. Corolario de pares: D=o(1/u) y K_D PSD en una raya fuerzan D=0; no buscar comparador positivo noidéntico cancelando también1/u. Diagnóstico de origen NUMÉRICO no usado en prueba. No nuevaW/T ni cambios en papers.


### Phase211 — comparador asinh, menor negativo certificado (2026-11-06)

PROVED/asistido, root/preservador, auditoría colas-jets casos, dedup mapa. `POWER_GLOBAL_ROUTE_REVIEW.md`, «Comparador asinh» y `tools/power_asinh_comparison_jet_verify.py`: M_0=.5asinh(u/(4pi)) tiene kernel PSD por integral positiva de resolventes, pero el residual N_D=(M_Phi-M_0)/u tiene menor de jets{5,6}, [[n10,n11],[n11,n12]], con det entre -1.684e-57 y -1.683e-57. Arb256,14momentos hasta26,16modos[0,3], colas totales<2^-645 cubiertas por2^-500; root reprodujo exit0. Sólo un menor prescrito, sin barrido. FALSIFIED comparación aditiva PSD, NO K_Phi ni comparación firmada general; jets no equivalen a sólo dos exponentes. Diagonales positivas no bastaban. No nuevaW/T ni cambios en papers.


### Phase211 — comparación hiperbólica original refutada (2026-11-06)

PROVED/asistido, root/preservador, revisión casos, dedup mapa. `POWER_GLOBAL_ROUTE_REVIEW.md`, «Comparación hiperbólica original»; `tools/power_hyperbolic_comparison_jet_verify.py`. Se cierra como FALSIFIED la comparación exacta antes OPEN K_Phi-K_(2pi) PSD. El menor residual de jets{5,6} tiene det entre -3.307e-59 y -3.306e-59, con28 half-moments completos hasta26, Arb256 y colas2^-500 por momento; root reprodujo exit0. No se transfiere el certificado asinh ni se exploran otros bloques. El modelo hiperbólico sigue PSD; K_Phi no queda refutado. Otras escalas, reponderaciones y compensaciones firmadas no decididas. No nuevaW/T ni cambios en papers.


### Phase211 — HCM recíproca no implica el signo del kernel (2026-11-06)

PROVED/root-theta_exacta-casos, dedup mapa; `POWER_GLOBAL_ROUTE_REVIEW.md`, «HCM, reciprocidad y supercolas». f_epsilon(x)=C(1+x)^(-2)exp[-epsilon(x+x^-1)], epsilon=2^-100, es HCM por producto explícito, recíproca y tiene todos los momentos Mellin. La ley de logX es par/real-analítica con supercolas; su cuarto cumulante>0 por cotas racionales con corte32. Entonces detK(h,2h)=−kappa2·kappa4·h²/6+O(h⁴)<0. FALSIFIED sólo inferencia desde esas hipótesis; no Phi, no BPY general, no propiedad V''' >0 ni etiquetaGGC. El criterio de pares es conocido; nueva clase del falsificador cotejada contra003/074/101 yL93. No nuevaW/T ni cambios en papers.


### Phase211 — HCM de la densidad theta real refutada (2026-11-06)

PROVED/theta_exacta-root-casos, cotejo mapa; `POWER_GLOBAL_ROUTE_REVIEW.md`, «La densidad theta en S=exp(2t) no es HCM». Para f(x)=Phi(.5logx)/(2xZ0), la paridad da f(1/x)=x²f(x). El producto HCM con a=1 tiene H(w)~(pi⁴/Z0²)w^(9/2)e^-2piw, w=v+1/v. CM exigiría logconvexidad; g=logH+2piw sería convexa, sublineal y tendente a+infinito, imposible. No se derivan restos. FALSIFIED HCM de esta densidad real y sus tilts/escalas positivos; no GGC ni K_Phi ni otros cambios de potencia. Se aplica el mecanismo ya conocido de tasa/prefactor a un objeto distinto de las mezclas§7.1; no reclamar principio nuevo. No nuevaW/T ni cambios en papers.


### Phase211 — los dos comparadores tampoco funcionan en el subespacio primitivo (2026-11-06)

PROVED/casos-root, auditoría matemática preservador y literal casos; `POWER_GLOBAL_ROUTE_REVIEW.md`, «Comparaciones primitivas: transferencia analítica del descarte». Restricciones exactas sum d/(u-.5)=sum d/(u+.5)=0. Para D impar real-analítica global, L=(u²-.25)(v²-.25)K_D convierte esas restricciones en momentos0,1 nulos. Proyección contra dos anclas + continuación de GRAM_SLICES§2.2 propagan positividad condicional desde cualquier intervalo abierto; las filas nulas en±.5 permiten completar los momentos sin energía y fuerzan PSD completa. Los certificados asinh/hiperbólico previos excluyen así también ambas comparaciones PRIMITIVAS uniformes. Diferencia: dominio codim2 antes no decidido por los vectores completos; no nuevo principio de continuación. Test primitivo negativo existencial, sin coeficientes ni ventana; no son automáticamente los jets originales. No negatividad de K_Phi, no equivalencia de mínimos a T fijo, no nuevaW/T ni papers editados.


### Phase211 — clausura de productos cosh a escala hiperbólica fija (2026-11-06)

PROVED/root-casos, auditoría independiente preservador, cotejo dirigido mapa; `POWER_HYPERBOLIC_MODEL_GRAM.md`§11.4. No puede aproximarse Phi localuniformemente por C_n exp(-2pi cosh(2t)) productos finitos de cosh(alpha_nj t), alpha_nj>0, incluso variando cantidad y parámetros. Lema: todo límite positivo normalizado de esos productos es exp(gamma t²)prod cosh(alpha_jt), gamma>=0, sum alpha_j² finita; logQ_n(1) acota la masa cuadrática y Taylor controla uniformemente el residuo. Para el cociente theta, logQ(t)/t→9/2 fuerza gamma0 y contradice§11 exacto. Diferencia: se cierra una clase de aproximaciones antes no cubierta, no se repite mera exclusión de representación exacta. Sólo escala2pi fija, factores unitarios positivos y convergencia uniforme en compactos; no escalas variables, potencias reales, otras topologías ni comparación relativa. Sin cómputos, signo real nuevo, ampliaciónT ni cambios en papers.


### Phase211 — cierre matricial finito sin derivada primera excluido (2026-11-06)

PROVED/root-casos, auditoría independiente preservador; `POWER_HYPERBOLIC_MODEL_GRAM.md`§12. Para vector finito de prefactores fijos Q, pares C² de crecimiento exponencial, con Q1=q_theta, no puede cumplirse Y_rr=(b²+nu²)Y+E(b)Y en dos escalas distintas con E independiente de nu. FORCE y unicidad fuerzan sinh(v)Q'=BQ constante; w=logtanh(v/2) da Q_w=BQ y límite finito de todas las componentes en infinito, incompatible con q_theta~2pi²e^(9v/4). Diferencia§10: dimensión finita arbitraria y potencial matricial, no sólo escalar. Sólo esta clase SIN A(b)Y_r ni prefactores dependientes de b; no exclusión de sistemas generales, infinitos u otros Green. Sin cómputos, nuevaW/T ni cambios en papers.


### Phase211 — cierre matricial finito con primera derivada excluido (2026-11-06)

PROVED/root-casos-preservador, auditoría literal casos y cotejo dirigido mapa; `POWER_HYPERBOLIC_MODEL_GRAM.md`§12.1. No se localizó antecedente literal anterior; E101_070§5 sólo excluía cierre automático de banda finita, no este sistema con matrices arbitrarias. En la familia de prefactores fijos Q que contiene q_theta, tampoco puede cumplirse Y_rr=(b²+nu²)Y+A(b)Y_r+E(b)Y en dos escalas distintas, con matrices independientes de nu y dimensión finita. FORCE y unicidad obligan a Qtilde_x=R(x)Qtilde racional, x=exp(v). Dependencia de filas fuerza un anulador racional escalar de q_theta(logx); conjugación por pi*x^(5/4)*exp(pi/x) lo transporta a g=sum n²(2pi n²x-3)exp[-pi(n²-1)x]. Separar sucesivamente las tasas exponenciales prueba que cada polinomio modal del anulador es nulo; su coeficiente principal exige un polinomio no nulo anulado en infinitas tasas distintas, contradicción. Diferencia§12: ahora permite A(b)Y_r. Sólo prefactores fijos, dimensión finita y coeficiente de nu² identidad; no sistemas generales, prefactores dependientes de b, dimensión infinita ni otras representaciones. Sin cómputos, nueva positividad W/T ni cambios en papers.


### Phase211 — la normalización por Phi no da generador traslacional positivo (2026-11-06)

PROVED/root-casos, cotejo dirigido mapa; `POWER_GLOBAL_ROUTE_REVIEW.md`, «Normalizar por Phi». Para B=A/(Phi(t)Phi(s)), p=-Phi'/Phi, C=−(partial_t+partial_s)B=t+s−(p(t)+p(s))B. C00=0, pero partial_s C00=1−aB00>0, a=p'(0): si a<=0 es inmediato; si a>0,073 da Phi(r)²/Phi0²<exp(-ar²) y B00<1/a. Menor{0,s} negativo y continuidad dan nodos positivos; continuación analítica excluye PSD en cualquier intervalo abierto. Distinto del hazard§7 y del generador sin gauge§2.3. Sólo falla esta condición suficiente; no B/A/KPhi, otras normalizaciones ni signo global. Sin cómputos, nuevaW/T ni papers editados.


**Ampliación por paridad del generador normalizado (2026-11-06).** En «Normalizar por Phi» de GLOBAL_ROUTE_REVIEW, corolario root/casos con cotejo mapa: ningún g par positivo real-analítico hace PSD local a C_g=−Dcommon[A/(gg)]. Paridad conjunta hace C_g impar; continuación PSD obliga diagonales cero y C_g=0, es decir estacionariedad A/(gg)=F(t-s). La diagonal H(L,L)=1−1/(4L²)+O(e^-2L) de GRAM§4.3 no es constante y excluye esa excepción. Incluye la reparación que anula la fila0 eligiendo g'/g=−sPhi0Phi(s)/A(0,s). Sólo corolario de paridad, continuación y asíntota escalar previas; no nuevos cómputos ni extrapolación matricial. No cubre gauges no pares ni otros mecanismos; sin nuevaW/T ni papers editados.


### Phase211 — generador inclinado C1, diagnóstico inicial (2026-11-06)

**Actualización:** FALSIFIED para todo c finito por el argumento de cúspides modulares registrado abajo. El párrafo siguiente conserva el estado histórico del diagnóstico.

`POWER_GLOBAL_ROUTE_REVIEW.md`, «Generador con inclinación exponencial». Cotejo dirigido mapa sin antecedente literal localizado. g_c=Phi exp(ct) evita paridad; C_c=C0+2cB, B=A/(PhiPhi), y B=integral exp(-2cr)C_c trasladado para c>=1: PSD de C_c sería suficiente. Root/casos: cola negativa exige c>=1. En c1 su principal es el Gram Cauchy1/[pi(e2t+e2s)], sin control relativo de resto. Único jet{0,1} evaluado por preservador a50/80dps, theta16/[0,3]: determinante≈+0.00788625227439, sólo NUMÉRICO sin enclosure. No otros bloques/barrido. Estado histórico inicial: C1PSD todosórdenes OPEN. Estado vigente: **FALSIFIED para todo c finito**, incluido c=1, por «Cúspides modulares» en la misma fuente y la entrada de descarte posterior; no reintentar desde este diagnóstico positivo. No positividad W/T nueva. Diferencia real: normalización no par, fuera del descarte anterior; no suficiencia inferida del diagnóstico.


### Phase211 — cúspides modulares refutan todo C_c con c finito (2026-11-06)

PROVED/root-casos-preservador, cotejo dirigido mapa; `POWER_GLOBAL_ROUTE_REVIEW.md`, «Cúspides modulares». C_cPSD y reflexión exigirían B<=exp(2ch)B trasladado. La congruencia elimina denominadores y produce H_h PSD real, holomorfo en strip²; sus jets exigirían H_h(iy,-iy)>=0. Para h=.5log2, y→pi/4, epsilon=cos2y, Poisson alternado en w→i da |Phi(iy)|<=Cepsilon^-9/2 exp[-pi/(8epsilon)], mientras la cúspide par w→2i da |Phi(h+iy)|>=kappa epsilon^-5/2, uniformemente también en un segmento de longitudepsilon. Integrales horizontales positivas dan A0>=kappa epsilon^-4 y Ah<=Cepsilon^-5. Así H<=C_c epsilon^-14 exp[-pi/(4epsilon)]−kappa epsilon^-9<0 para cada c finito. C1 antes OPEN pasa a FALSIFIED; su jet numérico positivo no implicaba signo global. Serie theta completa, sin cómputos ni argumentos por ceros. Sólo excluye esta familia de generadores y su comparación traslacional, no A/B/KPhi ni otros Gram. No nueva positividad W/T ni papers editados.


### Phase211 — generador con normalización diagonal completa refutado (2026-11-06)

PROVED/root-relative_comparison_audit, auditoría matemática independiente arithmetic_fresh_candidate PASS y cotejo dirigido diagonal_gauge_dedup. Fuente `03-research/phase-211-sign-sandbox/POWER_GLOBAL_ROUTE_REVIEW.md`, «Normalización por la diagonal completa». Para d(t)=A(t,t), R=A/sqrt(d(t)d(s)), ningún C_c=2cR-DcommonR es PSD de todos los tamaños en un intervalo real abierto, para ningún c real finito. Cambia el gauge a sqrt(d)exp(ct), no cubierto automáticamente por el descarte Phi exp(ct). Para c>0, reflexión y suma dan R PSD y comparación traslacional; producto de Schur de la diferencia y la suma, seguido de congruencia, da H=exp(4ch)A_h²d(t)d(s)-A²d_h(t)d_h(s) PSD hipotético, holomorfo sin raíces. La identidad d'(z)=-2zPhi(z)² y Poisson prueban d(iy) acotada y d(h+iy)~-(9/16)(h+i*pi/4)(2i)^(3/2)zeta^(-4), zeta=exp(2z)-2i, h=log2/2. Con las cotas completas previas A0>=kappa*epsilon^(-4), Ah<=C*epsilon^(-5), resulta H(iy,-iy)<=C_c*epsilon^(-10)-kappa*epsilon^(-16)<0, contradicción con jets PSD. c<0 falla diagonal; c=0 obligaría R estacionario y H=0, misma contradicción. Antecedentes: descarte modular de gaugePhi, paridad sin tilt y CPD normalizada; diferencia nueva: comparación cuadrada y primitiva de la diagonal. No se refuta A/R/K_Phi ni otros gauges; test real negativo existencial, sin nodos explícitos. Sin numerica, nueva ventana T ni cambios en papers.


**Corolario del descarte de normalización diagonal (2026-11-06).** GLOBAL_ROUTE_REVIEW, corolario final: PROVED root/relative_comparison_audit, auditoría arithmetic_fresh_candidate PASS. También se excluye g_c=sqrt(A(t,t))*exp(ct)/F(t), F(t)=exp(t/2)theta(exp(2t)), para todo c real finito. La comparación traslacional INVERSA y su producto de Schur exigen PSD de J=exp(4ch)A²F(t)²F(s)²d_h(t)d_h(s)-A_h²F_h(t)²F_h(s)²d(t)d(s). Poisson alternante/par y las mismas cotas completas dan J(iy,-iy)<=C_c*epsilon^(-20)*exp(-b/epsilon)-kappa*epsilon^(-10)<0. c<=0 se trata por diagonales reflejadas/paridad. Dividir por F invierte qué comparación falla; es corolario del mecanismo, no nueva clase general de imposibilidad. Sólo ese gauge, no A/K_Phi, otros gauges ni signo global. Cotejo dirigido sin antecedente literal; sin cómputos ni cambios en papers.


### Phase211 — gauge asimétrico de escala theta: menor real negativo (2026-11-06)

PROVED/root-relative_comparison_audit, revisión arithmetic_fresh_candidate PASS, cotejo dirigido diagonal_gauge_dedup. Fuente GLOBAL_ROUTE_REVIEW, «Gauge asimétrico de escala theta». g(t)=exp(2pi sinh(2t)), q=4pi cosh(2t), cambia la clase frente a even-gauge por inclinación constante. El generador congruente C=(q(t)+q(s))A+(t+s)Phi(t)Phi(s) falla en nodos temporales (-L,L) para L grande. Y=pi exp(2L),P=Phi(L): expansión diagonal completa da C--/P²=O(L/Y), C++/P²=4L+O(L/Y), mientras restringir A(-L,L) a0<=r<=Y^-1/2 da Aop>=kappa P²/Y y C-+>=4kappa P². Así det/P4<=O(L²/Y)-16kappa²<0. No precisa cola del integral, cúspides ni cómputos. Antecedentes: GRAM§4.3 y fórmulas de nodos opuestos, no este gauge; no duplicado literal hallado. Sólo esta candidata, no todos gauges asimétricos, A ni W. Los dos nodos no son dos potencias. Sin ampliaciónT ni papers modificados.


**Extensión del gauge asimétrico a todos los parámetros (2026-11-06).** PROVED/root-relative_comparison_audit, auditoría arithmetic_fresh_candidate PASS y cotejo dirigido diagonal_gauge_dedup; fuente GLOBAL_ROUTE_REVIEW, extensión final. Ningún g_a(t)=exp(a sinh(2t)), a real finito, hace PSD al generador. Para z=-h+iy,h=log2/2,epsilon=cos2y, el generador congruente satisface C_a(z,barz)=4a cosh(2h)epsilon Ah-2h|Phi(h+iy)|². Si a>0, cotas completas previas dan <=C_a'*epsilon^(-4)-kappa*epsilon^(-5)<0, contra jets PSD; a<=0 falla ya por diagonales reales. Amplía el caso2pi sin barrer parámetros, mediante test complejo DIRECTO del generador. Sólo existencia de un test real finito para a general, no dos nodos explícitos. Aplicación de herramientas previas de cúspides, no método nuevo de positividad ni no-go de todos los gauges. No refuta A/K_Phi; sin cómputos, ampliaciónT ni cambios en papers.


### Phase211 — todos los pares temporales y de capas v son positivos (2026-11-06)

PROVED/root, auditoría arithmetic_fresh_candidate PASS, cotejo dirigido diagonal_gauge_dedup sin antecedente literal localizado. Fuente POWER_GRAM_SLICES_OBSTRUCTION§9. De073 V'''(x)>0 y paridad se obtiene xV''-V'=integral_0^x rV'''(r)dr>0, luego G(u)=V(sqrt u) es estrictamente convexa. En SLICE, a=sqrt(m²+v)+delta,b=sqrt(m²+v)-delta tienen a²+b²=t²+s²+2v y dispersión estrictamente mayor que (t²+v,s²+v) si v>0,t!=s. Convexidad da S_v(t,s)²<S_v(t,t)S_v(s,s): todos los bloques de dos nodos reales distintos son SPD para v>0, y también los de A al integrar. v0 es rango uno. Con§5, tres es el tamaño mínimo de un falsificador de una capa v real; NO implica fallo de A en tres. Diferencia: pares TEMPORALES por convexidad en cuadrados, no pares de potencias073 ni TP2 de112. Principio convexo clásico; consecuencia nueva en corpus cotejado, no prioridad mundial. Sin nueva cobertura W/T, cómputos ni papers modificados; global OPEN.


### Phase211 — compensación entre capas probada en triples simétricos (2026-11-06)

PROVED/root, auditoría matemática arithmetic_fresh_candidate, cotejo dirigido diagonal_gauge_dedup. Fuente POWER_GRAM_SLICES_OBSTRUCTION§10. Refinamiento del mismo resultado: A sobre(-R,0,R) es SPD para TODO R>=8. El sector antisimétrico tiene d-b>0 por§9; el simétrico tiene determinante d0(d+b)-2c²>0 por cotas explícitas. Con Y=pi exp(2R),P=Phi(R), B=supPhi=Phi0<450/499<1 (todos los modos), p(x)>=pi exp(2x) en x>=1 da c<=BP(R/Y+2/Y²); integrar hasta r=1/(4Y), usando p(R+r)<3Y, da d>RP²/(4Y). Además d0>81/2^24 por Phi>9/256 en[0,1/16]. Para R>=8, 2c²/d<9B²R/Y<=9R/Y<24/7^8<81/2^24<d0. En LOS MISMOS nodos, para TODO R>=8, las capas pequeñas son negativas sobre w=(1/P,-2/Phi0,1/P): para B_v=S_v/(PhiPhi), eta=(1,-2,1), eta^T B_v eta=-v Q_R+o(v)<0, pues Q_R=2p'(R)-6p(R)/R+4p'(0)>(8-12/R)Y-2-6/R+4p'(0)>0. El intervalo 0<v<v_R depende de R. La integral completa sobre ese vector es positiva, así la contribución posterior compensa estrictamente la pérdida inicial. Diferencia: realización probada de compensación para theta REAL, frente a mera posibilidad abstracta o falsificador de capas§5; R>=8 explicita ambos signos, sin uniformidad de v_R ni ruta nueva. Sin intervalo v uniforme; no triples de potencias080, R intermedios, todos los tamaños, inducción, signo global ni ampliaciónW/T. Sin cómputos ni papers modificados.


### Phase211 — Andréief emparejado: integrando negativo de orden tres (2026-11-06)

PROVED/positive_identity_attempt-root, auditoría arithmetic_fresh_candidate PASS y cotejo dirigido diagonal_gauge_dedup. Fuente POWER_GRAM_SLICES_OBSTRUCTION§11. Para f_i(r)=Phi(t_i+r),g_i(r)=(t_i+r)Phi(t_i+r), detA3=(1/6)integral S, S suma de ocho productos det[u_ej(rj)]det[u_(1-ej)(rj)]. En(r,r,r+h), la suma COMPLETA es -4det[g,f,f_h]det[g,f,g_h]. Taylor da principales hC p[x1,x2,x3] y hC(xp)[x1,x2,x3], C>0; p'' y(xp)'' son positivos en la cola theta completa. Así S<0 para h pequeño y, por continuidad conr>0, en una región abierta de r1<r2<r3. Diferencia frente capas crudas: ya se emparejaron todas las elecciones del determinante; fuentes086/089/099–112 usan otros objetos. Sólo se descarta signo puntual de este integrando estándar; NO detA<0, no otros emparejamientos ni compensación integrada. Sin nuevaW/T, cómputos ni papers modificados.


### Phase211 — cierre del criterio recíproco y triples temporales pequeños (2026-11-06)

PROVED con certificado intervalar, constructor positive_identity_attempt/root; auditoría matemática arithmetic_fresh_candidate PASS y cotejo dirigido diagonal_gauge_dedup sin prueba anterior localizada del cierre. Fuente POWER_GRAM_SLICES_OBSTRUCTION§12 y tools/power_temporal_reciprocal_compact_verify.py. Origen u=r² en[0,1/64]: a>0,a''<0 en256paneles; resto r en[1/8,1]: T=N Phi³>0 en8192paneles, Taylor24/cap28, Arb512,16modos más cola completa. Cauchy da resto<1e-30; mínimo certificado T>1.04e-17. Constructor y root FULL PASS, SHA256 498e199ae7bb52f7fedeef02847a1b8642a635b76bb036212259bc2f875e93fa. Junto a cola r>=1 y073, q(u)=r/V'(r) es estrictamente convexa globalmente y a>0. Identidad (HK-J²)/H²=Var(a+ua')+E[u²(2a'²-aa'')] prueba HK>J². Expansión auditada D/d0=R^4(K-J²/H)+O(R6) y pares§9 dan A sobre(-R,0,R) SPD para todo R>0 suficientemente pequeño. Diferencia: se cierra el compacto pendiente de§12; no nuevo criterio. No confundir con M=Z'/Z de086, triplespotencias080 ni triplesRgrande§10. Sin umbral pequeño explícito; R intermedio y todosórdenes OPEN, no ampliaciónW/T ni papers modificados.

Aclaración de alcance (§12.3): el falsificador074 tiene q''<0 en0<u<=1, por lo que no refuta suficiencia de la nueva hipótesis. La familia V=r²/2+r⁴/4+epsilon*r⁶/6,0<epsilon<=1, sí cumple qconvexa pero tiene capas negativas por§5; no se decide su integral A. No se obtuvo extensión a R arbitrario.


### Phase211 — límite global de la nueva convexidad recíproca (2026-11-06)

PROVED, fuente POWER_GRAM_SLICES_OBSTRUCTION§13; construcción arithmetic_fresh_candidate/root, revisión de estabilidad positive_identity_attempt. Se fortalece§8.7: h_M del corte relativo tiende0 en C6 ponderada porque los jets modales tienen bounds polinomiales por exp[-(n²-1)pi e/2]; mollificación conserva la pequeñez. La nueva condición§12 a>0,q''>0 es abierta bajo perturbaciones pares C6 pequeñas: en origen |delta a|<=delta,|delta a'|<=delta/6,|delta a''|<=delta/60; cola N>2r²Y² y error<=1290delta r²Y. También se conserva V'''>0. Elegir M primero y sigma después conserva el bloque negativo de§8.7. Existen así densidades pares positivas analíticas cercanas aPhi con nueva convexidad GLOBAL y HK>J², pero A noPSD en algún tamaño noespecificado. FALSIFIED sólo suficiencia de esas hipótesis genéricas; NOsignonegativoPhi, NOherenciaSchur refutada enTheta, NOcierre global ni nuevaW/T. Sin cómputos ni papers modificados.


### Phase211 — primitiva theta regularizada: menor temporal explícito negativo (2026-11-06)

PROVED/root, auditoría arithmetic_fresh_candidate PASS; cotejo dirigido sin antecedente temporal literal localizado. Fuente POWER_GLOBAL_ROUTE_REVIEW, «La primitiva regularizada tampoco es un núcleo temporal PSD». Para U=2cosh(t/2)-exp(t/2)theta(exp2t)=2g, monotonía modal y exp3>16 dan (4/5)exp(-t/2)<U(t)<exp(-t/2) para t>=0. Entonces A_U(8,8)<18exp(-8), A_U(0,0)<2 y A_U(8,0)>(32/5)exp(-4); menor(0,8)<-(124/25)exp(-8)<0. Diferencia: decide falta dePSD de la fuente auxiliar misma, no sólo indefinitud de la corrección K_g-K_Phi ya registrada. No refuta A_Phi ni excluye compensación adicional; sin nuevaW/T, cómputos ni cambios en papers.


### Phase211 — recíproco temporal: no representación Laplace positiva (2026-11-06)

PROVED/root-arithmetic_fresh_candidate; cotejo dirigido diagonal_gauge_dedup sin antecedente literal localizado. Fuente POWER_GRAM_SLICES_OBSTRUCTION§14. q(u)=sqrtu/V'(sqrtu) no se extiende holomórficamente a todoReu>0, por tanto no es integral exp(-us)dmu(s) conmu>=0. Si Qextendiera, Q(z²)Phi'+zPhi=0 en x>|y|,|y|<pi/4. En w=i(16+2/m)+delta,mimpar, Poisson y |Gauss_m|²=m dan Phi~Cdelta^(-5/2),Phi'/Phi~−5w0/delta. Así Q(z_m²)=0 en puntos distintos acumulados en (log4+i pi/4)², interiorReu>0: unicidadanalítica contradiceq>0. No uniformidad enm ni divisióninteriorporPhi'. Los39primerosórdenesderivados disponibles yorden0 tienen signosalternadosfavorables, pero no pruebanrepresentación. No confundir q conrecíprocoM086 niCMparamétrica111; no refuta convexidad§12 ni signoA_Phi. Sin nuevaW/T ni cambiosenpapers.


### Phase211 — falsificador elemental de triples simétricos bajo G convexa (2026-11-06)

PROVED, fuente POWER_GRAM_SLICES_OBSTRUCTION§15; constructor positive_identity_attempt, revisión root/arithmetic_fresh_candidate PASS, cotejo dirigido sin antecedente temporal literal. phi=exp(-r²/2-epsilon*r⁶/6),epsilon=1/1000 tiene G'>0,G''>0 para u>0 y V'''>0 para r>0. Con w=exp(-u-epsilon*u³/3),Z=intw, a=1+epsilon*u², identidad§12 da Delta=(HK-J²)/H²=-2epsilonEu²+epsilon²(15Eu⁴-9(Eu²)²). Exp(-x)>=1-x prueba I2>=49/25,I4<=24 y Delta<=-89/(25000Z)<0. Por expansión D(R)=2(HK-J²)R⁴+O(R⁶), bloque(-R,0,R) indefinido paraRpequeño, aunque todosparesSPD. q''(0)=-2epsilon: no cumplepropiedadtheta§12. No confundir conKpotencias074/080/101; no refutaPhi ni signoobjetivo. Sin datos numéricos, nuevaW/T ni papers modificados.


### Phase211 — principal aritmético del A completo en escalas enteras fijas (2026-11-06)

**Alcance adicional§16.5, misma entrada (PROVED).** Root/global_restart_checked, auditoría independiente arithmetic_fresh_candidate PASS y root PASS; cotejo dirigido sin antecedente literal localizado. Fijar PRIMERO y∈(0,pi/4) y DESPUÉS k->infinito,l=k+1. Cola theta completa uniforme en r>=0 y Laplace en el extremo dan Akl/(Phi_k conjugado(Phi_l))=(x_k+x_l)/[2pi(epsilon(k+l)+i sigma(k-l))](1+O_y(1/k)); de ahí |C_y(k,k+1)|->1 para C_y normalizado por la diagonal. Como rho(k,k+1)=0, el bloque rho es I2 y eigenmin C_y=1-|corr|->0. No existe c_y>0 con C_y>=c_y rho uniformemente en bloques enteros, aun dependiendo c_y de y; tampoco aproximación uniforme o(1) a rho (sup error>=1 para cada y). Sólo este comparador/normalización; no A negativo ni otros pesos/modelos. Sin régimen conjunto epsilon,k, nueva ruta, W/T, cómputos o papers; signo global OPEN.

Fuentes: [GRAM§16 y banda§4.1](../../03-research/phase-211-sign-sandbox/POWER_GRAM_SLICES_OBSTRUCTION.md), [phase209 CONSTRUCTOR_005](../../03-research/phase-209-nonlocal-kernel/CONSTRUCTOR_005.md) y [AUDIT_005](../../03-research/phase-209-nonlocal-kernel/AUDIT_005.md).

PROVED, fuente POWER_GRAM_SLICES_OBSTRUCTION§16; construcción root/joint_sign_fresh_review, verificación independiente global_restart_checked, auditoría arithmetic_fresh_candidate PASS y root PASS. Cotejo dirigido sin antecedente literal localizado para este enlace con A; phase209 CONSTRUCTOR_005/AUDIT_005 son antecedentes del Gram aritmético, y GRAM§4.1 del promedio de banda. Para k,l enteros positivos FIJOS, z_k=.5logk+iy, epsilon=cos2y y L=log(1/epsilon), A(z_k,bar z_l)=[105/(512sqrt2)]rho(k,l)epsilon^(-9/2)L²+O_(k,l)(epsilon^(-9/2)L). Si k=d a²,l=d b² con igual parte libre de cuadrados, rho=gcd(a,b)/sqrt(ab); si no, rho=0. Resonancias exactas por Riemann gaussiana; casi resonancias, incluidas aproximaciones cuadráticas, por separación elemental de residuos y suma gaussiana S_delta<=C_(k,l)delta^-4log(2+1/delta), TODO delta>0. IBP diádica sobre TODO t>=1 da resto no resonante O_(k,l)(epsilon^-4L); términos inferiores pagan por cotas absolutas y Cauchy–Schwarz. La identidad gcd clásica con totientes prueba rho SPD para cada lista fija de enteros DISTINTOS; entonces su bloque COMPLEJO A es SPD eventualmente, con umbral dependiente de la lista. No nuevo Gram clásico ni identificación con norma209; no uniformidad en dimensión/enteros, ventana real, CPD/H, comparación relativa de todos los órdenes ni signo global. Sin cómputos, campañas, nuevaW/T ni papers modificados.


### Phase211 — SOS de todos los órdenes para la parte resonante exacta (2026-11-06)

**Alcance§17.8, misma entrada (PROVED).** Root/joint_sign_fresh_review, verificación global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS. Para T=pi t^(5/4)(-2tD-3), A0=-D, R_s=(A0+s)^(-1) terminal, T^-1F=(1/(2pi))t^-3/2 integral_t^infinito u^-3/4 F(u)du. La forma física q=Re<TA0f,Tf>=(pi²/2)[7 integral t5/2|f'|²−(9/2)integral t1/2|f|²] es negativa para f=t^-3/4u(logt) con bump ancho. Elegir s>0 pequeño y v=T(A0+s)f da Re<T R_s T^-1v,v>=q+s||Tf||²<0. La fórmula integral de Rtilde_s es acotada en H_gamma EXPONENCIAL, norma<=2/gamma+4(s+3/2)/gamma²; densidad§17.7 transfiere la negatividad a un agregado theta finito real. Antecedentes phase199 E§3Rem3.1 y phase188 N_BUILD_007/018 tienen otros núcleos/órdenes/métricas; sin literal localizado. Sólo falla acretividad de todos estos resolventes físicos. El logaritmo contiene MENOS R_s: NO refuta positividad del log conjugado ni todo método de resolventes, balance conjunto con C o signo A. Sin nueva ruta, cómputos, W/T o papers.

**Alcance§17.6, misma entrada (PROVED).** Root/global_restart_checked, auditoría arithmetic_fresh_candidate PASS y root PASS, incluido y0 por extensión directa del cálculo de extremo. Fijado y∈[0,pi/4), los pares k,k+1 tienen E_y y R_res diagonales. e_k=√k sum_n I_(kn²), r_k=√k sum_n[J_(kn²)+logk I_(kn²)]; r_k/e_k=logk+O_y(1/k) y Off_y(k,k)/e_k->0 exponencialmente. La correlación da |A_y(k,k+1)|/√e_ke_(k+1)=logk+o1. Coeficientes E-normalizados con cruce negativo producen Off_y[c]=-logk+o1, R_res[c]=logk+o1 y A_y[c]=o1. No existe C_y finito con Off_y>=-C_y E_y ni delta_y>0 con A_y>=delta_y R_res uniformemente. En y0, coeficientes reales(+,-) y A_y[c]>0 por§9; no A negativo ni decisión del bound crítico Off_y>=-R_res. Sin nueva ruta, W/T o papers.

**Atajo escalar§17.7, misma entrada (PROVED).** Root/joint_sign_fresh_review/global_restart_checked, auditoría arithmetic_fresh_candidate PASS y root PASS. Para y0 y F en span FINITO de Theta_k(t)=Phi(.5logkt), C=sum_(m>=2)Lambda(m)/√m T_m², T_m²F(t)=F(m²t), no existe M con |integral(CF)barF dt/(2t)|<=M integral(1+logt)|F|²dt/(2t). El operador C es continuo en H_gamma=L²(e^(gamma t)dt/t),0<gamma<2pi, y el span theta es denso allí por inversión Möbius de h(kt), inversa de L=-2tD-3 y aproximación C1 de polinomios en e^-pi t. Las mesetas1_[1,R] dan numerador>=cR^(1/8)logR y denominador=.5logR+.25log²R. Se extiende primero por densidad para R fijo y después R->infinito. Antecedentes explícitos phase199 PROOF_L_SHARP_C_001§4Prop4.2/E_001§3Rem3.1, BRIDGE002§3, AUDIT_L_SHARP_1§2.4 y019§§3–5; no nuevo principio de no acotación, sólo comprobación en este portador exacto y peso. No A negativo, bound no resonante por R_res ni transferencia/cierre global. Sin cómputos o papers.

**Refinamiento uniforme§17.5, misma entrada (PROVED).** Root/joint_sign_fresh_review, verificación global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS. D_q>=c_*I_q para todos d,q>=1 y 0<epsilon<=1, c_*=(log2/3)(4pi-3)²e^-6pi/[(4pi+3)²+(4pi-3)²e^-6pi]. Para dq>=2 sirve log(dq)Iq; para d=q=1, N!<=N^N2^-floor(N/2) da gap log2/3 cuando X>=2. Con X=sqrtu, el corchete de DIAG es>=log2/3 en u>=2 (en2<=u<4 la suma está vacía). Core[1,2]<=pi²sqrt2(4pi+3)² y tail[2,3]>=pi²sqrt2(4pi-3)²e^-6pi pagan una fracción uniforme de I1. Así R_res>=c_*E_y, E_y=sum_d sqrt(d)sum_q I_(dq²)|f_(d,q)|². Uniformidad sólo en esa energía divisorial exacta, con I dependientes de epsilon/índices; NO margen euclídeo uniforme, NO A completo ni off-frequency, W/T o cierre global. La eventual positividad del A COMPLETO entero sí se transfiere al real por§18; esta cota resonante sola no la prueba. Sin nueva ruta, cómputos ni papers.

Fuente: [GRAM§17](../../03-research/phase-211-sign-sandbox/POWER_GRAM_SLICES_OBSTRUCTION.md). Antecedentes: [SIGNED_MEAN_019](../../03-research/phase-211-sign-sandbox/POWER_SIGNED_MEAN_019.md), [CONSTRUCTOR_005](../../03-research/phase-209-nonlocal-kernel/CONSTRUCTOR_005.md) y [AUDIT_005](../../03-research/phase-209-nonlocal-kernel/AUDIT_005.md).

PROVED, construcción root/joint_sign_fresh_review, verificación independiente global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS, incluida SOS y positividad estricta. Cotejo all3/019/209 sin identidad literal localizada. R_res conserva TODOS los pares kn²=lm² del A exacto y su integral t>=1. Cada frecuencia puede ser indefinida: nodos1,4 y lambda4 dan det=-2(log2)²I_4²<0. Pero para cada grupo k=d a² y c_a finito, f_q=sum_(a|q)sqrt(a)c_a, I_q=I_(dq²), J_q=J_(dq²), la identidad exacta es R_res[c]/sqrt(d)=sum_q D_q|f_q|²+sum_q sum_(m|q,m>=2)Lambda(m)I_q|f_q-f_(q/m)|², D_q=J_q+(logd+logq)I_q-sum_(m>=2)Lambda(m)I_(qm)>0. El cambio u=lambda t convierte D_q en integral positiva: sum_(m<=X)Lambda(m)/m<2logX por la identidad factorial y floor(X/m)>=X/(2m). Sumabilidad absoluta gaussiana y f acotado justifican todo; el menor a con c_a!=0 prueba definitud estricta. Así R_res es PD en TODOS los órdenes sobre enteros positivos distintos k para CADA |y|<pi/4, incluido y0. Herramienta factorial clásica, sin inversión Möbius; se acoplan frecuencias distintas, no capas PSD ni Gram sustituto209. NO A completo, NO todos nodos reales, NO control no resonante, nueva W/T o cierre global. Actualización§18: para A COMPLETO, todos los bloques enteros y todos los nodos reales son equivalentes; no se transfiere R_res por separado. Sin campañas, datos numéricos ni papers.


### Phase211 — El A completo entero equivale al A sobre todos los nodos reales (2026-11-06)

Fuente: [GRAM§18](../../03-research/phase-211-sign-sandbox/POWER_GRAM_SLICES_OBSTRUCTION.md). **PROVED**, construcción independiente root/joint_sign_fresh_review, verificación global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS. Consultados all3 y corpus, sin literal localizado. Definir P_kappa=kappa^(5/4)sum_n n²e^(-pi kappa n²t), T=pi t^(5/4)(-2tD-3), LgP=integral_0^infinito[e^-pi r P(t)-P(t+r)]dr/r y G=.5T LgP-C TP. Frullani y sum_(m|n)Lambda(m)=logn dan TP_kappa=Theta_kappa y G(P_kappa)=.5logkappa Theta_kappa. La forma A completa es integral[logt|F|²+2Re(GbarF)]dt/(2t). Para cada lista finita de escalas positivas se eligen a<pi min(1,kappa_min), gamma<2a; la norma B_a² controla simultáneamente(F,G) en H_gamma exponencial. Los targets tienen jets ponderados tendiendo a0: corte, aproximación C2 en e^-pi t e inversión Möbius absoluta e^-pi kt=k^-5/4 sum_n mu(n)/sqrt(n)P_kn² aproximan por escalas enteras en esa norma. NO se afirma densidad de compactos para todo B_a² ni se usa sólo densidad de F. Continuidad de la forma transfiere PSD de TODOS los bloques enteros a TODOS los nodos reales; la recíproca es restricción. Antecedentes BRIDGE002§3, CONFLUENT_BRIDGE014, SCALAR_BRIDGE017 y GRAM§17.7: herramientas de densidad previas, otras familias o norma sin este grafo completo. No nueva herramienta abstracta ni signo probado: R_res positivo solo no basta; el balance conjunto completo sigue OPEN. Se elimina únicamente la puerta adicional de transferencia del A COMPLETO, la equivalencia con el objetivo lambda_A(T)>=0 para TODOS T se verifica después en§18.9, sin identificar mínimos a T fijo. Sin cómputos, nueva W/T o cambios en papers.


**Alcance§18.5, misma entrada (PROVED).** Root/joint_sign_fresh_review, verificación global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS. B=Lg-2sum_(m>=2)Lambda(m)m²D_(m²), p=P1, Bp=0, tiene tasas positivas antes de T sobre P=pf. Pero la cola integral de TU_rT^-1 induce en T Lg T^-1 el núcleo fuera de la diagonal K(t,v)=t^-1/4v^-3/4-t5/4v^-5/4/(v-t), respecto de dv. K>0 para2<v/t<3. TBT^-1=T LgT^-1-2C; elegir t0=2 y F>=0 no nula, soporte compacto en(9/2,11/2), da CF(2)=F(2)=0 y TBT^-1F(2)>0. Refuta únicamente la representación JF=integral[F(t)-F(v)]nu_t(dv)+V(t)F(t), nu_t>=0, incluso con killing local o posterior conjugación por Theta1 positiva. Soportes separados justifican intercambios absolutos sin renormalización diagonal ni pérdida de borde1. Antecedentes106_31, ROUND005D y L2_BUILD008 son otras formas/métricas, sin este T/K; cotejo dirigido sin literal. NO Q/A negativo, NO descarte general de Doob ni del método conjunto; signo completo OPEN. Sin nueva ruta, archivos, cómputos, W/T o papers.


**Alcance§18.6, misma entrada (PROVED).** Root/global_restart_checked, auditoría arithmetic_fresh_candidate PASS y root PASS. Para A_ij(x,y)=integral_x^infinito(x_i+x_j+2s)Phi(x_i+s+iy)barPhi(x_j+s+iy)ds, Delta A_ij=4integral w_ij Phi_i'barPhi_j'-4P_ij(x,y), con borde inferior conservado. En diagonal x_i=0,y0,x>=1,088 da p=-Phi'/Phi>2Y-6>Y, Y=pi e2s. Así I=integral_x^infinito2s p²Phi²>Y(x)[xPhi(x)²+integralPhi²]>Phi(x)² y Delta A_ii>0. Falla superarmonicidad/armonía requerida por el principio mínimo directo desde el borde complejo§16. No se afirma fuente matricial indefinida: su signo conjunto no está probado. El umbral por bloque de§16 tampoco proporciona PSD conjunta en intervalo real abierto para§2.2. NO A/Q negativo ni descarte de toda PDE/transporte; signo global OPEN. Cotejo all3/16/2.2/088 sin literal resuelto; sin nueva ruta, archivos, cómputos, W/T o papers.


**Extensión§18.7, misma entrada (PROVED).** Root/joint_sign_fresh_review/global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS. Cada cola fija k>=K de los P_k aproxima los targets de§18 en B_a² y en el grafo(F,G): tras corte, P_c=x^KQ(x), x=e^-pi t; aproximación C² produce sólo exponenciales con k>=K y error C_K eta e^-pi Kt, y Möbius sólo introduce kn²>=K. Así PSD de TODOS los bloques de cualquier cola equivale al A real global. Para cualquier prefijo fijo c_1..c_J existen completaciones finitas con k>J que aproximan menosP_prefijo y hacen A_0[c]->0, sin suponer PSD. Si PSD, el ínfimo de esas completaciones es0. No puede existir A_0[c]>=delta|ell(c)|² con delta>0 y ell no nulo FINITAMENTE soportado. Tampoco minorantes diagonales no triviales con pesos TODOS NO NEGATIVOS, sobre c_k o los observables divisoriales finitodependientes f_(d,q) de§17; fijar el prefijo conserva un término positivo. Antecedentes DESCENT_AUDIT016§§8–9 (otra cola racional/W4), BRIDGE002§3 y18.3: instrumento previo, no este portador/grafo/conclusión. También excluye una identidad ÚNICA compatible A_0=sum_alpha w_alpha|ell_alpha|² con w_alpha>=0 y todos ell_alpha finitemente soportados, aunque sus tamaños crezcan: cada sumando sería un minorante prohibido. No excluye factorizar por separado cada bloque finito; FIXED_BLOCK_ASSEMBLY trata otra clase/kernel y tamaños uniformemente acotados. Scope y0; no A negativo, no descarte de energías sobre observables globales continuos/SOS no diagonales ni signo global. Sin nueva ruta, archivos, cómputos, W/T o papers.


**Corolario§18.8, misma entrada (PROVED).** Root/joint_sign_fresh_review/global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS. Para CADA sigma real fijo, ell_sigma(c)=integral_0^infinito e^(sigma u)sum_k c_kPhi(.5logk+u)du no admite A_0[c]>=delta|ell_sigma(c)|² con delta>0 sobre todos los soportes finitos. El momento es continuo H_gamma, por CS con integral_1^infinito t^(sigma-1)e^-gamma t finita;§18 transfiere el supuesto minorante a nodos reales. En x=-R, Axx=2integral_R^infinito sPhi² y ell_sigma(F_x)~Z_sigma e^(sigma R), F_x(t)=Phi(x+.5logt), Z_sigma=integral sobre TODA R de e^(sigma s)Phi(s)>0. La supercola hace el cociente tender a0 para todo sigma real. Antecedentes BRIDGE002/106_31/ROUND005D/106_36 y GRAM8.4 tienen continuidad, otras formas o densidad alterada/momento cancelado; cotejo all3/corpus sin literal. Sólo momentos exponenciales reales individuales: no complejos/test espectral, no momentos firmados generales ni A negativo; global OPEN. Sin nueva ruta, archivos, cómputos, W/T o papers.


**Alcance§18.9, misma entrada (PROVED, no signo).** Root/joint_sign_fresh_review/global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS; reglas del repositorio/all3 y definiciones primarias Paper47 cotejados. El objetivo lambda_A(T)>=0 para TODO T equivale a PSD completo K_(M_Phi), A real y todos los bloques enteros A, incluso cualquier cola fija. Recíproca nueva de alcance: cortar en infinito f(r)=sum d_i e^-u_i r, u_i>.5, con sum d/(u_i±.5)=0; dos bumps físicos fijos corrigen momentos con coeficientes→0 en H_eta014. No se exige f(0)=0: salto causal permitido en H^s,s<.5 y dominio log. Trasladar cada compacto a una ventana conserva Tate/W; hipótesis∀T firma K primitivo. El lema YA probado en GLOBAL Comparaciones primitivas con D=M_Phi impar real-analítica da K completo; suficiencia inversa BRIDGE002. En el grafo, ell_sigma(TP)=pi P(1)+pi(sigma/2-.25)integral t^(sigma/2+.25)P: Tate equivale a P(1)=0 e integralP=0, SIN P'(1)=0. No importar preimagen L2_BUILD008. Cada cola tiene rango2 de momentos: un bump P toca1, otro interior; dos vectores tail FIJOS con matriz invertible corrigen errores→0. Así18.7 conserva cualquier prefijo y A0→0 incluso para completaciones exactamente primitivas; sus no minorantes/SOSlocales sobreviven.18.8σ±.5 vacuo allí, otrosσsin inferir. NO equivalencia de mínimos a T fijo ni nuevo signo; global OPEN. Sin enunciados externos, archivos, cómputos, W/T o papers.


### Phase211 — Signo completo del primer polinomio primitivo en t=exp(2r) (2026-11-06)

Fuente: [GRAM§19](../../03-research/phase-211-sign-sandbox/POWER_GRAM_SLICES_OBSTRUCTION.md). **PROVED para el primer vector; ampliación bidimensional posterior en§19.9**, construcción fresh_global/root; auditoría arithmetic_fresh_candidate FULLPASS, root PASS y lectura literal independiente global_restart_checked PASS. Con p=P1=sum_n n²exp(-pi n²t), S_j=sum_n n^-j exp(-pi n²), a=1+(2/pi)S4/S2 y P=p(t)(t-1)(t-a), se tienen EXACTAMENTE P(1)=integral_1^infinitoP=0, por tanto ambos momentos Tate de F=TP nulos. Q(P)=Q_log+Q_B, Q_log>=0 y Q_B>1/1200-1/40000-1/4500-1/30000=199/360000>1/2000. La prueba retiene p exacto; principal(1,1) sólo como referencia con bound, corrección de a exacto, cruces(1,2)/(2,1) y TODO resto de la doble serie theta/prima con colas gaussianas explícitas y partición exhaustiva. No cuadratura/campaña ni truncación sin error. Cotejo all3/corpus101/195/199/209/211 sin familia literal localizada; antecedente E101_061 interpola nodos, las familias gamma/Laguerre previas son en otra variable. Instrumentos elementales, sin prioridad mundial. Esta prueba elemental firma ESTE primer vector primitivo; no hereda otros grados/cruces o recurrencia. La ampliación independiente§19.9 firma el plano E1,E2; grados posteriores, todos los órdenes, nueva ventana W/T y signo global permanecen abiertos. La propiedad de core suficiente se prueba por separado en§19.8 y no aporta esos signos. Papers intactos; sin archivos nuevos.


**Core suficiente§19.8, misma entrada (PROVED como alcance).** Construcciones independientes root/fresh_global, auditoría global_restart_checked PASS; cotejo all3/BRIDGE002§3/CONFLUENT_BRIDGE014/DESCENT_AUDIT016§§8–9/18 sin familia/core literal. En B_a²,a<pi, V=clausura span{pt^j}; H(z)=p e^zt tiene Taylor en norma con ||p e^(z0t)t^j/j!||<=C_(z0)(1+b)²b^-j, b=pi-a-Re z0>0. Diferencias finitas y discos solapados negativos dan p e^-nu t en V para todo nu>0 sin Hahn–Banach. C² en x=e^-t para Q=P_c/(px) aproxima compactos; corte sólo de targets con jets ponderados→0, NO todoB_a². Convergencia B_a² controla grafo(F,G)/Q. Corregir errores(P(1),integralP) mediante p,tp tiene determinante p(1)integral(t-1)p>0 y coeficientes→0. Primitivos son E_j=p(t)(t-1)q_j(t), j>=1, q_j ortogonales mónicos para w=(t-1)p; E1 es el vector firmado, grado2 de R. PSD de TODOS los Gram Gamma_ij=Q(E_i,E_j) equivale al objetivo lambda_A(T)>=0 para TODO T: físico fcompactprimitivo->F(t)=f(.5logt)->P=T^-1F compacto y primitivo, core+repair firmaW y dominio de cada ventana; recíproca TPpoly superdecay se corta∞ y corrige Tate en H_eta014 antes de pasar al límite. Se conserva borde causal/salto0 permitido, sin imponer P'(1)=0. No mínimos a T fijo ni nuevaW/T. El plano E1,E2 tiene signo PROVED por el certificado posterior§19.9; grados/cruces fuera de él y global siguen OPEN. El core no usa resultados numéricos; papers intactos.


**Bloque completo§19.9, misma entrada (PROVED asistido).** Diseño arithmetic_fresh_candidate/root, revisión matemática fresh_global/root, auditoría literal corregida fresh_global/root/global_restart_checked PASS; ejecuciones constructor y reproducción independiente root exit0/FULLPASS con SHA256 e589fb2b9d98d76f021418427a903794f17aa629832f400f2154c21add52f170. Para los dos primeros E1,E2 de§19.8, Gram COMPLETO real simétrico Q11>179/100000, Q22>17/10000, |Q12|<79/50000 y detQ>2733/5000000000: TODA combinación real no nula del plano es positiva. A la vez Q_B(E1+E2)<-1/20000; falla promover el signo separado Q_B(E1) a la familia, NO el signo completo Q. Parámetros exactos mediante momentos de w, encierro theta4modos+cola positiva; referencia de integral2modos pagada con TODAS las colas theta/primas, temporal y resto Cauchy deterministas. Verificador corregido usa192bits,960paneles[1,16],gradoTaylor40 y derivadas R/L algebraicas exactas, assertsorden41; inflación de errores ANTES gates. No cuadratura adaptativa/búsqueda ni corte sin error. Fuentes y proof en GRAM§19.9, tools/power_thermal_primitive_two_verify.py/.log. Sólo este bloque bidimensional: NO herencia siguiente grado, todos los órdenes, margen uniforme, nuevaW/T o signo global; core suficiente§19.8 permanece independiente. Papers intactos.


**Colas de grados§19.10, misma entrada (PROVED como alcance).** Root/joint_sign_fresh_review; auditorías joint_sign_fresh_review/arithmetic_fresh_candidate y root PASS. Para CADA J>=1 fijo, PSD de TODOS los bloques Gamma_(J..N), N>=J, equivale al objetivo lambda_A(T)>=0 para TODO T. Es aplicación del lema de GLOBAL Comparaciones primitivas a un número finito de restricciones: V=prod(u-sigma), d=Vb convierte sum d/(u-sigma)=0 en momentos polinomiales de grados0..m-1; anclas+continuación y filas nulas en sigma reparan mediante Vandermonde y entregan K completo. La cola térmica equivale exactamente a P(1)=0 e integral t^kP=0,0<=k<J, o momentos físicos Sigma_J={.5} union {2k-.5:0<=k<J}; sin P'(1)=0. El core19.8 repara J+1 errores mediante p y t^j(t-1)p: rango por borde p(1)>0 y Hankel positivo de w. Para exponentes físicos se corta PRIMERO en infinito y se reparan todos los momentos con bumps fijos en H_eta014; sólo después T^-1 produce un compacto al que aplicar el core. No se introduce la preimagen con cola de potencia en B_a². Antecedentes014/083/GLOBAL/18.9/19.8, no desigualdad positiva nueva ni no-go general. Ni el plano certificado E1,E2 firma una cola, ni se excluye firmar alguna; todos sus tamaños/cruces siguen OPEN. Sin uniformidad en J, mínimos a T fijo, nuevaW/T, cómputos o cambios en papers.


**Referencia primer modo§19.11, misma entrada (PROVED, aplicación de008).** Root/joint_sign_fresh_review; versión corta auditada por joint_sign_fresh_review/fresh_global/arithmetic_fresh_candidate y root. Para p0=exp(-pi t), la referencia Q0(R)=integral[logt|T(p0R)|²+Re(TLg(p0R)conjT(p0R))]dt/(2t) NO es PSD sobre polinomios reales con R(1)=0 e integral pR=0 EXACTOS. No se afirma que p0R sea primitivo en ambos momentos: las restricciones corresponden a pR. Prueba:008 da Arch[f]<=-4norm²+17normderiv²; tres bumps disjuntos igualmente ensanchados forman un espacio real negativo dimensión3. En sus preimágenes P=T^-1[f(.5logt)], dos restricciones P(1)=0 e integral rhoP=0,rho=p/p0, dejan vector no cero; la primera anula ell_+=piP1 y por sí sola el polar. A_P(P)=Arch+Polar<0. Corep0 en B_a² y reparación mediante p0,tp0, con det=e^-pi integral(t-1)p>0, producen un polinomio admisible yQ0<0 por continuidad. No grado ni coeficientes calculados. Aplicación del falsificador008 al dominio exacto, no nueva necesidad aritmética ni falsificador del Q completo/A/kernel theta truncado. Tampoco refuta toda perturbación o compensación entre modos; certificados19.7/19.9 intactos y global OPEN. Sin cómputos, archivos nuevos, nuevaW/T ni papers.


### Phase211 — Potencial del adjunto causal: signo interior negativo (2026-11-06)

**PROVED, prueba elemental con colas completas.** Fuente: POWER_GRAM_SLICES_OBSTRUCTION.md§19.12. Construcción joint_sign_fresh_review/root; auditoría arithmetic_fresh_candidate FULLPASS y root PASS de gates racionales. Consultados reglas del repositorio/all3/106_31/ROUND005D/18.5/GLOBAL: Picone/Doob y killing logarítmico tienen antecedentes; cambia el potencial del adjunto causal exacto en dt/(2t), no se afirma prioridad mundial ni lectura exhaustiva. Con Theta(t)=Phi(.5logt), J=TBT^-1 y r=.5logt, Bp=0 para todo t>0 y paridad de Phi dan forward Phi=2rPhi, backward Phi=-2rPhi. Su promedio completo anula Phi por esa álgebra física, SIN usar el argumento externo de106_31. Al restringir r>=0 queda g(r)=-integral_0^infinito k(r+s)Phi(s)ds, k(h)=2cosh(h/2)-exp(-h/2)/(1-exp(-2h))-sum Lambda(n)/sqrt(n)delta_logn. Adjunto débil causal J*Theta=2g-4rPhi, incluido borde1; el potencial de la identidad firmada de diferencias es V(f)=integral Phi(r)g(r)|f(exp(2r))|²dr. En log2 por DERECHA, la cola prima empieza n>=3. Aplus=pi p(1)>3/25; Gamma<=Aplus/(3sqrt2). Principal(n,m)=(3,1)<3645/56000; TODO resto, agrupado q=mn, <1024/249000 por cociente<1/250 y exp(25/2)>250000. Así P3<7/100 y g(log2+)<-19/300<-1/20. Gates Taylor racionales y colas detallados en§19.12; sin cuadratura ni truncación sin error. Continuidad derecha da un intervalo con Phi g<0. Tres bumps físicos disjuntos en ese intervalo y dos restricciones Tate dejan una combinación no nula EXACTAMENTE primitiva con V<0; su preimagen P es compacta, P(1)=integralP=0. Falla sólo exigir V>=0, incluso sobre esos perfiles primitivos. No Q/A negativo ni NO-GO universal de caminos/tres puntos; el término de diferencias puede compensarlo. Signo global OPEN; certificados19.7/19.9 intactos. Sin archivos nuevos, campañas, nuevaW/T ni papers.


**Dos fases exactas, GLOBAL (PROVED, alcance restringido).** Root/new_structural_sign; auditoría arithmetic_fresh_candidate PASS. Con perfiles COMPLETOS Psi_(k,theta)=sum_n n^-1/2 h_(kn²)exp(i kn²theta), la media en theta del A_theta ponderado exactamente por logt+.5log(kl) es R_res de GRAM§17. Para D=A0−Api, los nodos{1,2} dan D22=0 yD12>0 por positividad de h y del subagregado impar; detD_{1,2}=−D12²<0. Así fallan AMBOS órdenes PSD entre A0 yApi. No A0/Api negativos, otra mayoración, asintótico uniforme en fase ni signo global. Series y colas completas, sin numerica, archivos nuevos, W/T o papers.


### Phase211 — comparación hiperbólica pequeña: anulación necesaria (2026-11-06)

**PROVED como implicación / comparación OPEN.** GLOBAL, «Comparación hiperbólica pequeña: condición necesaria de anulación». Construcción fresh_global, auditoría new_structural_sign/root. Para H=-D²+(2pi)²exp(2r) Dirichlet, U_f=integral f(t)exp(2it sqrtH)dt, el Gram REAL 2||U_f||HS² reproduce K_h. ContinuidadH_eta, puente014 y traslación transfieren K_Phi>=epsilon K_h a compactos bilaterales reales. Cortes dePhi convergen en H1 con peso exp(eta|t|); la identidad física H_fullPhi=0 deGRAM19.12 fuerza U_Phi=0. Diferencia disponible: identidad física nueva, no principio nuevo de inclusión de radicales. Falta demostrar U_Phi!=0: NO contradicción, NO descarte de epsilon pequeño, NO signo global ni nuevaT. Para complejos se requieren ambas ramas; no aplicar014 directamenteaPhi bilateral. Sin cómputos ni cambios en papers.


### Phase211 — RES-SOS no identifica los canales de 106_38 (2026-11-06)

**PROVED, cotejo de objetos; no nuevo signo.** GLOBAL, «Alcance de RES-SOS frente a los restos de 106_38». Root/new_structural_sign, auditoría arithmetic_fresh_candidate PASS. En X_frac, x=y+log n y v=e2y dan productos h_(n²i²)(v)h_(j²)(v) con n no divide j: TODOS son no resonantes, y llevan un multiplicador de diferencias distinto del peso deGRAM17. X_ctr usa h_(i²)(v)h_(j²)(n²/v), escalas recíprocas. Bajo síntesis BILATERAL f_c=sum c_kPhi(x+.5log k), c=delta1 da g=f_c/Phi=1 y X_frac+X_ctr=0, pero R_res[c]>0; excluye sólo su identificación literal y un minorante positivo por R_res con esa síntesis. NO trasladar al A causal ni descartar comparaciones corregidas. Puente18 transporta A completo, no estos canales. La identidad física19.12 no resuelve la Poincaré antigua ni repone los términos omitidos en106_32. Sin cómputos, nuevaT o cambios en papers.


### Phase211 — cierre infinito simétrico sin deriva: rigidez de norma (2026-11-06)

**PROVED, clase fuerte explícita.** HYPERBOLIC§12.2; root, auditorías new_structural_sign/arithmetic_fresh_candidate PASS. Q C² en norma de un Hilbert, Q(v) en dominio común de B,C simétricos, sinh(v)Q'=BQ y Q''=CQ fuerzan ||Q(v)||²=A+c logcosh(v), A,c>=0. Prueba: w=logtanh(v/2), simetríaB=>K(w,z)=F(w+z), simetríaC=>sinh(s)F''+cosh(s)F'=0. Ninguna observación lineal continua puede ser q_theta~2pi²exp(9v/4). Dos FORCE fuertes -Q''+2b_i sinh(v)Q'=E_iQ con E_i simétricos en dominio común implican ese sistema. Diferencia§12: dimensión infinita y operadores no acotados, añadiendo simetría; no basta anterior argumento matricial finito. No requiere DomB² ni autoadjunción. Para deducir FORCE de una ODE integral se deben justificar dominios/intercambios, no son automáticos. NO exclusión de drift, métricas variables, observaciones no continuas, prefactores dependientes de escala u otros Green. Sin signo real nuevo, cómputos, ventanaT o cambios en papers.


### Phase211 — dimensión infinita con deriva escalar constante (2026-11-06)

**PROVED para la clase fuerte declarada.** HYPERBOLIC§12.3, root; auditorías new_structural_sign/arithmetic_fresh_candidate PASS y literal PASS. Q par C² en norma hasta0, dominio común de B,C simétricos, sinh(v)Q'+alpha cosh(v)Q=BQ y Q''=CQ fuerzan K(v,z)=A/2[cosh((v+z)/2)^(-2alpha)+cosh((v-z)/2)^(-2alpha)], A=||Q0||². SimetríaC da ecuación de ondas; simetríaB fija sus datos. Gram analítico prolonga Q a |ImZ|<pi/2 con norma²=A/2[cosh(ReZ)^(-2alpha)+cos(ImZ)^(-2alpha)]. Alpha>=0: norma real acotada contradice q_theta; alpha<0: norma acotada en ReZ=log2, ImZ->pi/2 contradice cúspide PAR e^Z->2i de theta completa. No usar cúspide alternante i. Diferencia12.2: primera derivada ESCALAR CONSTANTE 2alpha, cualquier signo, dimensión infinita, añadiendo paridad/Neumann0. Dos FORCE fuertes con E_i simétricos y esa deriva implican el sistema; no inferir FORCE desde integrales sin justificar dominios. No excluye deriva variable/operatorial, métricas variables u otros Green. Sin signo global, nuevaT, cómputos o papers editados.


### Phase211 — deriva escalar variable forzada a constante (2026-11-06)

**PROVED, clase fuerte explícita.** HYPERBOLIC§12.4; root, auditorías arithmetic_fresh_candidate y new_structural_sign PASS; literal PASS. Dos FORCE con b1!=b2>0, coeficientes escalares reales a1,a2 y E_i simétricos en dominio común fuerzan a1=a2 para Q C² no nulo, incluso en dimensión infinita. Gauge q=(sinh v)^alpha Q, w=logtanh(v/2), da GramF(w+z); simetríaC impone lado izquierdo sólo de s=w+z igual a beta F(s)/(sinhw sinhz). Variar w-z a s fijo fuerza beta=0; beta=b1b2(a1-a2)/(b2-b1). Con paridad C² hasta0 y observación continua theta, reduce a12.3 y falla. Extiende constante a variable escalar; no deriva operatorial. También excluye gauge multiplicativo escalar real C² no nulo en la misma coordenada y coeficiente espectral1, siempre que FORCE esté justificada. No inferir intercambios de operadores no acotados automáticamente. Sin signo global, nuevaT, cómputos o cambios en papers.


**Control de alcance de HYPER12.4, misma fecha.** Ejemplo algebraico new_structural_sign/root: Q=(1,2coshv), C=diag(0,1), D=diag(-4,-1), B=[[0,-2],[-2,0]] satisface sinhvQ'+coshvDQ=BQ yQ''=CQ con B,C,Dsimétricos y[B,D]!=0. No se extiende automáticamente el descarte escalar a drift operatorial. No contiene theta ni da Green positivo: gauge exp(-rD) produce offdiagonales -4bexp(±3r), perdiendo simetría usual. Otras métricas y sistemas generales no refutados. Sin nuevo signo o ventanaT.


**Reparación por métrica del ejemplo operatorial12.4 (2026-11-06, PROVED).** Root/new_structural_sign PASS. Formal symmetry local de L=-D_r²+2D D_r+b²I+E exige M'=-DM-MD y[E+D²,M]=0, luegoM=e^-rDM0e^-rD. Para el ejemplo2x2 ya registrado, M0V=V*M0 implica -4abexp3r+4dbexp(-3r)-16c=0; b=a0exp r y la independencia de exp4r,exp(-2r),1 fuerzan M0=0. No métrica matricial LOCAL positiva para ESEejemplo en ningún intervalo abierto. No otros sistemas, métricas no locales ni signo theta refutados. FuenteHYPER12.4, párrafo final; sin nuevaT o cómputos.


### Phase211 — tasas móviles: umbral fuerte exacto (2026-11-06)

**PROVED como aproximación, no signo.** CONFLUENT_BRIDGE014§6; root, auditorías new_structural_sign/arithmetic_fresh_candidate PASS. Para eta>1/2, u_N>eta,u_N->infinito y V_N=e^-uNy polynomialsgrado<N, aproximación de todoH_eta A LO LARGO deN iffN/u_N->infinito; densidad de la UNION iff limsupN/u_N=infinito. Distancia exponencialL²_eta=|(u_N-v)/(u_N+v-2eta)|^(2N), caso r0 de096. Paso fuerte nuevo: aproximar f' enL²_eta y antiderivar terminalmente, operador de norma<=1/eta que conserva MISMOgrado/bloque; sin pérdida logarítmica. No envolvente lineal. PSD de esos bloques completos, o lower -epsilon_N||f||² conepsilon_N->0 (criterio036), sería suficiente por continuidad014 ytraslación; hipótesis OPEN. THREE002u>=2^(40N) noentra; preservar margenfijo9 enregimendenso contradicecortesradicalfísico19.12, no contradice semidefinitud. Sin nuevaW/T, cómputos o papers editados.


**Alcance de la doble escala, aplicación de008 (2026-11-06).** BRIDGE014§6 final, root/arithmetic_fresh_candidate. Para u_N=N^(3/4), aproximar enH_1 el test primitivo008 y reparar ambos momentos con dos correctores del MISMO V_N. Se obtiene Polar0, AP[f_N]/||f_N||²<-3 y c_fN(log2)/||f_N||²>1/3 eventualmente, aunqueN/u_N²->0. No vale suprimir uniformemente ese contacto comoO(N/u²), ni declararPSD el principalAP. NoWnegativo ni descarte de un principal que conserve aritmética; aplicación del falsificador previo, no nueva positividad. SinT/cómputos/papers.


### Phase211 — corte primo creciente: error uniforme exp(-N) (2026-11-06)

**PROVED cola / signo retenido OPEN.** BRIDGE014§7, root/arithmetic_fresh_candidate/new_structural_sign PASS. ParaTODOSN>=1,u>=2 y f∈V_N(u), Q=ceil exp(40N/u) da |W−W_(<=Q)|<exp(-N)||f||². Aplicación deTHREE002tailnorm sqrt6·13^Nexp(-ut/2), válida antesdelumbralpositivo yporconfluencia: Lambda<=log, comparaciónintegralexacta dafactor Q^(-(u-1)/2)[2logQ/(u-1)+4/(u-1)²], menorfinal230Nexp(-7N)<exp(-N). SeconservanARCH/polar/contactosq<=Q ytodoscruces; no supresión deátomosbajos. Conu_N=N^.75,corteexp(40N^.25), faltaría loweruniforme -epsilon_N||f||²,epsilon_N->0, paraesebloqueretenido;014§6cerraríaentoncesglobal. NiPSDretendida ni nuevaT demostradas. Cortecreciente no contradice10632fixedcutoff. Sin cómputos/papers.


### Phase211 — corte móvil subcrítico: umbral necesario (2026-11-06)

**PROVED, principal truncado solamente.** CONFLUENT_BRIDGE014§8; fresh_sign_mechanism, auditoría new_structural_sign y root. Para u_N=N^(3/4), cualquier corte log Q_N<=(2-delta)N/u_N, delta>0 fijo, tiene un vector unitario explícito de dos coordenadas Laguerre con W_(<=Q_N)->-infinito. Cota: 2log u+32+4sqrt Q log Q+6/u-(2/u)exp((N-1)/u). Excluye cortes polinómicos para lower evanescente de TODO el bloque; tal lower exigiría liminf u_N log Q_N/N>=2. Diferencia respecto de antecedentes: corte creciente cuantificado;007 aporta bandas exactas,106_32 trata otro objeto (energía transformada con átomos eliminados). Frente al corte suficiente40 de014§7, fija orden exponencial necesario, no constante óptima. No primitividad, no negatividad de W completa, no signo del corte40 ni nuevaT; no extender a toda escala densa sin prueba.


### Phase211 — corte móvil insuficiente aun en primitivas (2026-11-06)

**PROVED para W truncada, no para W completa.** BRIDGE014§9; construcción fresh_sign_mechanism/root, auditoría matemática new_structural_sign PASS. Para u=N^(3/4),N>=2^60 y log Q<=2^(-12)N/u, un vector unitario explícito del MISMO V_N tiene ambos momentosTate0, f(0)=0 y W_(<=Q)[f]<-3. Coeficientes C(z)=(1-z)(z+r)(z+1/r)[sum_(j<M)(-z)^j]^4, M=floor(N/4),r=(u+.5)/(u-.5). Concentración elemental E tau²<=2^18(u/M)²; Arch<-3 y todos los contactos retenidos tienen correlación>=1/2, por lo que empeoran el déficit. Diferencia frente a008: ancho u/M en vez de u/sqrt(N), permite esta escala móvil y corte creciente explícito. No es simple aplicación del polar negativo de§8: aquí se anula exactamente. Descarta también cortes polinómicos en subespacios primitivos; NO transfiere umbral2, no negatividad fullW, no signo del corte40 ni nuevaT. Sin cómputos o cambios en papers.


### Phase211 — comparación hiperbólica pequeña refutada (2026-11-06)

**PROVED asistido, sustituye OPEN de esta comparación específica.** GLOBAL «Cierre de la comparación hiperbólica pequeña»: no existe epsilon>0 con K_Phi>=epsilon K_(2pi). La condición necesaria anterior exigía U_Phi=0, usando el radical físicoGRAM19.12 y el puente de forma. Nuevo input: Picone con r exp(-3r) y Rayleigh con r exp(-5r) sitúan omega_1=2sqrt(lambda_1(H)) en[17,41/2], H=-D²+(2pi)²exp(2r), Dirichlet0. La integral física G(omega)=integral_R Phi(t)cos(omega t)dt es <-10^-8 en TODA esa banda por certificado de bolas, colas completas y Bernstein; luego U_Phi v_1!=0. Constructor arithmetic_fresh_candidate, cotas/auditoría new_structural_sign, root y revisor reproducen FULL PASS/exit0. Script tools/power_hyperbolic_phi_cosine_band_verify.py enphase211, SHA cddcc0bf1c902be2fce90a12969dec3a43209c85a037d5156a916c9a74410ab6. Sólo theta explícita y espectro del MODELO, sin tablas de ceros. No signo negativo del objetivo, no exclusión de otros modelos, no nuevaT ni papers editados.


**Precisión primitiva del mismo cierre (2026-11-06).** GLOBAL aplica su lema anterior de continuación primitiva a D=M_Phi-epsilon M_(2pi). Para CADA epsilon>0 y CADA intervalo abierto no vacío I⊂(1/2,infinito), algún bloque finito de tasas en I con ambos momentosTate0 tiene energía residual negativa. Root/new_structural_sign PASS. Aplicación del lema existente, no nuevo mecanismo ni cómputo; no tamaño, coeficientes o ventana explícitos, no negatividad del núcleo objetivo.


**Familia física del mismo descarte, no nuevo mecanismo.** GLOBAL: g_R=(D²-1/4)(chi_R Phi) es compacto, par y exactamente primitivo; converge en H1 bilateral ponderada a f_*=(D²-1/4)Phi, radical físico. U_f*=-(4H+1/4)U_Phi tiene primer modo no nulo por el certificado ya registrado. Convergencia HS implica W[g_R]-2epsilon||U_gR||HS²<0 para cada epsilon>0 y R suficientemente grande. Root/new_structural_sign PASS; sin R numérico, sin W negativo demostrado, sin nuevos cálculos o papers.


### Phase211 — antecedente bibliográfico directo del kernel temporal (2026-11-06)

GRAM_SLICES§1 incorpora el manuscrito público de Dylan Suvlu (24Sep2026), «Theta correlations and a causal range criterion for the Weil form», §3eq18–23, https://dsuvlu.github.io/weil-form-operators/paper/theta-correlations-causal-range.pdf . Cotejo root/new_structural_sign: j=A/(integral Phi)² y misma respuesta logarítmica. Antecedente de representación, no signo global demostrado; no atribuir novedad a A por ausencia en búsquedas anteriores. No determina prioridad de RES-SOS17 ni del bloque19.9. Borrador, sin afirmación de revisión por pares o auditoría completa; no nueva construcción ni cómputos.


**Compañero causal del mismo antecedente:** GLOBAL registra lectura de SuvluIII§2. La contracción con peso no da L² ordinario; su majorante separado diverge al bajar r a1/2 ya por c_Gamma. No se afirma divergencia del feedback real ni fracaso de toda vía causal. RES-SOS y bloques finitos no aportan aquí una cota de la inversa. Cotejo root/arithmetic_fresh_candidate; no nuevo teorema de signo ni cómputos.


### Phase211 — ramificación BPY examinada, preservación OPEN

GLOBAL registra la candidata T'=W_1^-2 T_1+W_2^-2 T_2 y simetrización recíproca. No es truncación theta. Semilla S delta_(pi/3) tiene Gram explícito; un solo bloque de jets del primer paso fue positivo NUMÉRICAMENTE, sin certificado ni extrapolación. Simetrizar después conserva el límite bajo las hipótesis de convergencia/media fija; simetrizar dentro cambia la dinámica y su convergencia no está probada. El paso conserva una entropía con factor firmado y un borde firmado de integración por partes; no se obtuvo preservación PSD ni contraejemplo. No nueva vía validada ni campaña de grados. Cotejo root/independent_sign_reset; fuente y fórmulas en GLOBAL, sin papers editados.


**Precisión del alcance de la ramificación (2026-11-06).** GLOBAL prueba que S B no factoriza universalmente a través de S: S delta_4=S delta_(1/4), pero las salidas tienen distinta regularidad en t=5. Densidad y salto de derivada exactos; auditoría independiente new_structural_sign PASS. No refuta preservación PSD ni la órbita de media pi/3; las dos entradas tienen medias distintas. Concreción de pérdida de información, no nuevo avance del signo. Extensión auditada independent_sign_reset/root/new_structural_sign: GLOBAL proporciona dos leyes finitas positivas de media pi/3, misma S y salidas S B distintas, mediante una perturbación recíproca antisimétrica de seis átomos y cocientes de saltos de densidad. Tampoco basta añadir la media como dato. No se prueba PSD de esas entradas ni se refuta preservación PSD o la órbita específica; extensión rutinaria del alcance.


**Diagnóstico escalar de ramificación (2026-11-06).** GLOBAL contiene prueba asistida y código inline reproducido de kappa4 del tilt logarítmico de S B delta_c<-1/5000 para todo c>0. Se reduce a k+4ds-2d^4 y a dos cotas de momentos de V=A1+A2. Construcción independent_sign_reset, auditoría algebraica new_structural_sign y reproducción integral root FULL PASS. Este falsificador necesario no funciona; NO se prueba PSD ni preservación. Sin campaña de órdenes ni nueva ventanaT.


**Ramificación: alcance del condicionamiento (2026-11-06).** GLOBAL conserva identidad exacta K=media de congruencias condicionales+C, con C igual al negativo de dos covarianzas normalizadas. Para la entrada real mu=B delta_(pi/3), C(u,u)=−Var(h)u²/2+O(u⁴), Var(h)>0 por continuidad y soporte pleno. Así C noPSD ya en el segundo paso real. Constructor independent_sign_reset, root y auditoría new_structural_sign PASS. Sólo falla pagar ESTA corrección como positiva; no K negativo ni exclusión de compensación conjunta. Sin cómputos ni avance de ventanaT.


**Fuente externa de ventana log11 (CITED/UNVERIFIED, 2026-11-06).** GLOBAL registra rStation45v1 y cotejo de normalización root/new_structural_sign. La afirmación externa cubriría la restricción primitiva deP47 hasta log(11)/2 si se valida; construcción intervalar no reproducida, suplemento ya localizado por API pública; pasan comprobaciones cortas de hashes, matrices pequeñas y Green, sin regeneración400. No nueva frontera local certificada ni cierre global. Papers intactos.


**2026-11-06 — rStation45/log11, actualización parcial auditada.** Sector PAR hasta T=log(11)/2: **PROVED con asistencia computacional, reproducción local de resultado externo**. Cadena completa regenerada (safe/graph/contract/family/checker); checker exit0, complemento393 con Hmin>0 y siete pivotes del núcleo>0. Root y new_structural_sign reprodujeron la eliminación intervalar del núcleo; auditor independiente confirmó seis fuentes idénticas al suplemento, metadatos, enlaces entre archivos y logs. Archivo final SHA25618a3a25b3bacb3e265bee09232bdd09b17ea88074c9619bf6d9be069c4654cb3; último pivote [5.173121145006658e-50 +/-3.29e-66], NO cota de gap espectral. Diferencia con pivotes históricos compatible con distinta congruencia/orden de eliminación; no se requiere identidad bit a bit. **Sector IMPAR todavía pendiente de reproducción; ventana de la forma COMPLETA local permanece1.035; signo global OPEN.** Resultado externo, no novedad propia. Evidencia y procedencia en POWER_GLOBAL_ROUTE_REVIEW.md, sección fuente externa log11, y /tmp/riemann-rstation45-audit/work. No se modifican papers.


**2026-11-06 — log11 COMPLETO: reproducción local auditada.** Sustituye el estado parcial anterior: **PROVED con asistencia computacional, resultado EXTERNO reproducido** para la forma completa W_T en ambas paridades, 0<T<=log(11)/2 (aprox.1.1989476364). Fuente: https://rstation.ai/problems/riemann_hypothesis/papers/45 . Todas las etapas de regeneración terminaron exit0; root y new_structural_sign comprobaron logs, fuentes idénticas al suplemento, metadatos, vínculos de los archivos y reeliminación intervalar de ambos núcleos. Impar: complemento394 con Hmin=[0.0072415100579310717783150120757660513853081885959734786213576 +/-4.96e-62]>0, seis pivotes positivos, último revalidado [2.92609807122468755690e-45 +/-8.74e-66]. SHA final impar7211d28ec770386db511be3942e20ecd4056d2b5cc95501e7fd5a4802ae548ce. Archivo final par y su auditoría constan arriba. La auditoría analítica previa conserva el complemento infinito y coincide con la normalización P47; la restricción primitiva hereda positividad. La frontera local verificada de la forma completa se actualiza de1.035 a log(11)/2. NO se deduce un margen espectral de los pivotes. NO es resultado original nuestro ni prueba para todoT: signo global OPEN. Evidencia persistida en phase-211-sign-sandbox/tools/rstation45_reproduction/ (logs, fuentes, dos resultados finales, auditor pequeño y hashes); las matrices intermedias permanecen en /tmp/riemann-rstation45-audit/work. Papers intactos. No se lanza otra campaña de ventanas: falta una estimación estructural uniforme del bloque Schur completo, no sólo positividad de sus sumandos favorables.


**2026-11-06 — Resta de cortes, auditoría sin signo nuevo.** GLOBAL, «Resta de dos cortes suaves»: w1−w2 elimina el sumando común y da continuo primitivo, pero abarca todo W compacto tras traslación; el principal conserva oneprofile y el resto cruzado carece de cota firmada nueva. Consecuencia de ROUND_001_A/REVIEW_002 y P211-A; revisión root/arithmetic_fresh_candidate/corpus_global_gap. No NO-GO general, nueva ventana ni cambios en papers. Global OPEN.


**2026-11-06 — Candidata PF infinito aditivo + reciprocidad (puente OPEN).** GLOBAL, «Densidad BPY»: q(v)=sum n²(2pi n²v−3)e^(−pi n²v), 2pi q tiene Laplace prod(1+s/(pi n²))^(−2). Convolución de exponenciales dobles y límite uniforme prueban TP aditiva de todos los órdenes; q(1/v)=v^(5/2)q(v). Son propiedades clásicas del dato, no signo nuevo de A. El contramodelo HCM ajustado a esa reciprocidad tiene (log q_e)''(1)=3/4−2epsilon>0 y falla PF2: diferencia de clase comprobada. Falta firmar el kernel integral con q(av)q(bv) y log(abv²); TP aditiva no autoriza esa composición multiplicativa. No se afirma suficiencia, prioridad o cierre. Root/new_structural_sign y auditoría arithmetic_fresh_candidate PASS de identidades y alcance; cotejo selectivo L23/L93/corpus. Sin cómputos ni papers; global OPEN.


**PF aditivo + reciprocidad: alcance adicional, sin signo global.** GLOBAL desarrolla la consecuencia h''<=0 y h(1/x)=beta logx+h(x) ⇒ −(log Phi)''>=2beta=5, ya compatible con la convexidad theta conocida. Una Gamma(2,rate4), PF infinito pero NO recíproca, tiene integral t Phi²<0 por Jensen (media9/16), y su A tiene diagonal negativa. Excluye sólo transferir automáticamente signo desde convoluciones exponenciales; no refuta el paquete conjunto ni sus aproximaciones particulares. Cálculo root/new_structural_sign, sin cómputos. Puente multiplicativo OPEN; papers intactos.


**PF/reciprocidad — aproximantes finitos simetrizados, alcance específico.** GLOBAL: densidad f_N de2Nexponenciales tiene f_N(v)~C_Nv^(2N−1) en0. Su perfil simetrizado tiene cola positiva exp[−(4N+1/2)|t|], por lo que GRAM§8.5 ya implica A noPSD. Además la densidad recíproca ftilde_N tiene cola v^−(2N+3/2) y (log ftilde_N)''>0 eventual: falla PF2. No contraejemplo al paquete completo; f_N→2pi q y perfil normalizado usa factor1/2, no pi. Resultado específico sin cómputos/papers; puente global OPEN.


**2026-11-06 — Rigidez de modificaciones FINITAS de tasas BPY (PROVED en clase).** GLOBAL: mantener exactamente dos tasas pi y modificar finitas otras tasas, todas>pi, da L_f=R racional·L_0. Si además f(1/t)=t^(5/2)f(t), la cola (At+B)e^−pi t y su recíproca fuerzan R=r0+r1/sqrt(s)+r1/(2sqrt(pi)s)+error exponencial; racionalidad implica r1=0,Rconstante=1. Construcción root, auditoría arithmetic_fresh_candidate PASS; sin antecedente literal en cotejo selectivo. No unicidad PF infinito general ni signo de A; modificaciones infinitas/cambio del mínimo fuera de alcance. Sin cómputos/papers; global OPEN.


**2026-11-06 — Renovación aditiva BPY, alcance acotado.** GLOBAL: vf(v)=∫_0^v k(v−u)f(u)du, k=2sumexp(−pi n²x), produce transición descendente; reciprocidad produce ascendente. Su mezcla equiprobable no admite densidad reversible: el cociclo R(L,2L)R(2L,3L)/R(L,3L)~1/sqrt(2L), no1. Construcción global_sign_independent_reset, revisión root; diferencia respecto renovación divisorialE101.089, cotejo dirigido all3/corpus. No se identificó su energía con A: NO signo negativo de A ni cierre del paquete, no exclusión de otros pesos/no reversibilidad. Sin cómputos/papers; global OPEN.


**2026-11-06 — Renovación plegada: identidad exacta y capas indefinidas.** GLOBAL construye xf(x)=∫_1∞f(u)h_u(x)du y A=∫∫f(u)f(w)S_ab^(u,w)dudw, con h_u=k(x−u)+sqrt(u)k(x−1/u) en sus soportes exactos. Fubini absoluto conserva todo el peso logarítmico. Para u>w>1,a=u+delta, Sdiag→S0>0, S1=−C/sqrt(delta)+O1, S12=O(delta^−1/2), luego jetdet=−C²/delta+O(delta^−1/2)<0. Hay capas con menor negativo en cada intervalo real abierto de escalas>1. No signo negativo de A, ni conclusión para nodos enteros, ni exclusión de compensación/agrupamiento. Construcción global_sign_independent_reset/root, doble revisión PASS. Sin cómputos/papers; global OPEN.


**Renovación BPY, una fuente integrada (corolario específico).** GLOBAL: integrar completamente w deja C_ab(u) con g(x)=xf(x). Diagonales positivas para a>=1, pero cerca a=u+delta el jetdet es −u f(u)²(logu)²/(256delta)+O(delta^−1/2)<0. Por tanto tampoco son PSD estas capas individuales; falla en nodos reales próximos>1, no se decide enteros ni A completo. Construcción global_sign_independent_reset, revisión root; aplicación del mecanismo anterior, no nuevo criterio general. Sin cómputos/papers; global OPEN.


**2026-11-06 — Autodescomposición BPY y límite de la órbita de escalas (alcance PROVED; signo OPEN).** POWER_GLOBAL_ROUTE_REVIEW, «Autodescomposición BPY»: L(s)/L(cs)=prod[c+(1−c)lambda/(lambda+s)]² construye el semigrupo de saltos con densidad invariante f y energía positiva auxiliar, rho=−k'. Su estacionariedad reproduce la renovación, sin identificar la energía con A. El semigrupo común NO preserva las dilataciones: si cdX+Y_c fuese bX, la media fija b=1+c(d−1), pero la diferencia de varianzas es −2sigma²c(1−c)(d−1), no nula para d distinto de1. Inversión cambia f dx a x^(1/2)f dx. No descarta otros transportes ni decide A. Objeto distinto de la falsa identificación arquimediana/difusión de phase64/154; herramienta clásica sin prioridad. Construcción root/new_structural_sign y revisión arithmetic_fresh_candidate PASS; cotejo dirigido corpus/all3. Sin web, cómputos numéricos o papers.


**2026-11-06 — RES-SOS: no hay cota SUPERIOR uniforme del resto (corolario, y=0).** GLOBAL, «presupuesto resonante»: para N fijo y k>N², k,...,k+N−1 tienen distintas partes libres de cuadrados; R_res es diagonal. El extremo theta completo de GRAM16.5/17.6 da R^(-1/2) A R^(-1/2)->J_N y Off normalizado->J_N−I_N. Coeficientes r_i^(-1/2) dan Off/R->N−1. Hacer crecer N después de ese límite excluye Off<=C R y |Off|<=C R para todo C finito, y por tanto una norma uniforme de H=−R^(-1/2)Off R^(-1/2). NO excluye H<=I ni decide Off>=−R o A. Mismo mecanismo de bloques cercanos, con presupuesto RES-SOS exacto; no nuevo principio ni signo. Root y auditoría arithmetic_fresh_candidate PASS; cotejo all3/corpus global_arithmetic_restart. Sin web, cómputos numéricos o papers.


**2026-11-06 — Extensión factorial antes de resonancia, restos firmados (identidad PROVED; signo global OPEN).** GLOBAL, «Extensión factorial»: con b_lambda=sum_(n²|lambda)n^-1/2 c_(lambda/n²), Gram completo K, proyección P_m sobre m²|lambda y traslado R_m, Q=sum Lambda||P_mb−R_mb||_K²+b*Db+E. D integra h_lambda h_mu contra log(t sqrt(lambda mu))−loggcd(q_lambda,q_mu)−S(sqrt t); E=−2Re sum Lambda(R_mb)*K(I−P_m)b. El factorial firma TODAS entradasD, pero D noPSD porque H−D>=0 y la referenciaH sinpeine tiene test negativo por GRAM19.11/18.3. E(delta1)<0. Inversión Möbius truncada y colas gaussianas transfieren ambos fallos separados a c finito. No Q/A negativo ni descarte de compensación conjunta. Diferencia con RES-SOS: se conservan cruces de frecuencias distintas; no nueva herramienta factorial/Gram. Constructor global_concrete_reset, root y auditoría new_structural_sign PASS; cotejo dirigido all3. Sin web, cómputos numéricos o papers.


**Corolario de la extensión factorial, 2026-11-06:** c=delta1 da b_(n²)=n^-1/2 y P_m b=R_m b para todos m. Por tanto S_sq=0, mientras E=−2sum Lambda(P_mb)*K(I−P_m)b<0 (ya m2, índices4/1). Ningún C finito permite E>=−C S_sq. Q[delta1]=A(0,0)>0: D paga ese E, sin signo global inferido. Corolario directo de la identidad anterior, no nuevo mecanismo; root y auditoría new_structural_sign PASS. GLOBAL conserva prueba y alcance. Sin web, cómputos o papers.


**Núcleo de S_sq, corolario algebraico (2026-11-06).** En la extensión factorialGLOBAL, para c finito, S_sq=0 iff c está soportado en enteros libres de cuadrados. b_(dq²)=c_d/sqrt q prueba un sentido; inyectividad del GramK por T y unicidad exponencial, recurrencias en cada primo e inversión Möbius prueban el otro. En esa familia Q=D+E; no PSD ni densidad inferidas. Root y auditoría new_structural_sign PASS, cotejo dirigido all3. Sin web, cómputos o papers.


**2026-11-06 — Balance factorial SF: B+M noPSD (test exacto).** GLOBAL: en el núcleo libre de cuadrados, suma de loggcd ponderada por K coincide con B=Gram_S(sqrt t), y D+E=Q=L+M; factorial firma0<=B<=L. La cota suficiente B+M>=0 falla en{1,2},c=(1,−1/100): cotas completas theta dan T11<1e−6,T22<1e−2,T12>1e−4, luego c*Tc<0. L−B>=0 no se elimina de Q y el bloque completo sigue positivo; no signo global. Constructor global_concrete_reset, root y auditoría new_structural_sign PASS; cotejo all3, sin nueva herramienta factorial ni campaña. Sin web, cómputos numéricos o papers.


**2026-11-06 — Densidad SF en grafo y ausencia de margen fijo L−B.** GLOBAL: P_z holomorfaB_a², ||P_z||<=C(1+|z|)^13/4 enRe z>=delta>a/pi. Funcional anulador dividido por(z+1)^4 esacotado; Schwarz con factores finitos yΣSF1/d=infinito fuerzaanulaciónidentica. Hahn–Banach+GRAM18.3/18.7 prueban aproximación de compactos por cualquier colaSF conservando grafo. Con g_R=(D²−1/4)(chi_RPhi), Wg_R->0,normaL²->positiva; trasladar a r>=1 y usar w=logt−S√t>=log2/3 implica que Q>=epsilon(L−B) esfalso∀epsilon>0, tambiénSF. Equivale a excluir B+M+alpha(L−B)PSD∀alpha<1 fijo. No Qneg, nosemidefinitudprobada, nomárgenesvariablesdescartados. Construcción root/global_concrete_reset y auditoría new_structural_sign PASS; cotejo dirigido all3, herramientasclásicas, sinweb/cómputos/papers.


**2026-11-06 — Resto conjunto factorial noPSD; no margen por S_sq.** GLOBAL: aproximarP4 enB_a² porP(cn) con cnSFfinito, y tomar e_n=delta4−cn. Q[e_n]->0, pero J anulaSF y por tanto S_sq[e_n]=S_sq[delta4]=s0>0. Luego(D+E)[e_n]->−s0: restoCONJUNTOnoPSD y ningúnε>0 permiteQ>=εS_sq. S_sq no continua enB_a², aunqueQ sí. Diferencia respecto18.7: observableinfinito deidentidadfactorial, usandodensidadSF. Root y auditoría new_structural_sign PASS. NoQneg ni descarteglobal decompensaciones; sinweb/cómputos/papers.


**2026-11-06 — Resolventes escalares del producto: capas noPSD.** GLOBAL: J_u=integral Phi(r+x)Phi(r+y)[(1+u)^−1−(exp(2r+x+y)+u)^−1]dr, A=integral J_u du conFubiniabsoluto. Paridad da diagonal límite negativa∀0<=u<1; GRAM2.2 excluye PSD deJ_u sobre cualquierintervalorealabierto. DensidadSF aplicada alPAR(P_z,z^-1/2P_z), noPsola, transfiereJ0neg a cSFfinito; continuidadconservamismotest para0<=u<eta. NoAneg ni falloSF∀u<1 afirmado. Objeto distinto deTR_sT^-1 de17.8; falta compensaciónintegrada. Constructor global_signed_balance, root y auditoría new_structural_sign PASS; cotejoall3, sinweb/cómputos/papers.


**Parejas recíprocas de resolventes, candidata OPEN (2026-11-06).** GLOBAL: C_u=J_u+u^-2J1/u, A=integral_0¹C_u du; peso h_u(z)=(z²−1)/[(z+u)(uz+1)] imparbajoinversión. h0=z−1/z,h1=(z−1)/(z+1), integral0¹|h_u(z)|du=|logz|. ParidadPhi da diagonalesC_u(x,x)>0∀xreal,u∈[0,1], eliminando falsificadorindividual. NO PSDallorders ni signoA; faltacotadecruces. Diferencia: emparejarantesdeestimar, no capasindividuales. Root/global_signed_balance y auditoría new_structural_sign PASS deidentidades, cotejoall3; sinweb/cómputos/papers.


**2026-11-06 — Pareja extrema C_0 PSD en TODOS los órdenes reales (PROVED auxiliar).** GLOBAL: C0=integral2sinh(2r+x+y)Phi(r+x)Phi(r+y)dr tiene DOMgaussiano. Transformada=(Z(a+1)Z(b+1)−Z(a−1)Z(b−1))/(a+b). Z(a)=xi(a+.5)/2; S=2pi(s−1)zeta(s)/[(s+1)(s+2)zeta(s+2)],s=a−.5. InversaEulerabsoluta yEuler–Maclaurin construyenS holomorfa, crecimiento polinomial; paridad da|S(it)|1, boundEuler paraRea>=32 y máximoenstrip dan|S|<=1. KernelSchurPSD porHardy/Parseval, congruencia y recíprocaDOM deGRAM2.1 firmanC0 temporal todosnodos. Constructor global_signed_balance, root y auditoría new_structural_sign PASS, cotejodirigidoall3/phase16sinliteral, sinprioridadmundialafirmada. NO C_u interior niAglobal: extremo u0demedidacero. Sinweb,cómputos,papers.


**2026-11-06 — Dos transportes de C_0 descartados en clases precisas (PROVED).** GLOBAL, «Dos transportes desde C_0»: q_u(w)=1/(1+u²+2u cosh w) tiene log estrictamente cóncavo, por lo que q_u(x+y+2r) falla PSD ya en menores2; no es multiplicador Schur positivo. Además NO existe minorante C_u>=integral C_0(x+t,y+t)dmu(t) con mu positiva fija no nula, 0<u<=1: diagonales pares D_u/D_0<=u^(-1)e^(-2|x|)->0, mientras cualquier masa compacta de mu impone cociente positivo en uno de los extremos por monotonía D_0. Incluye imposibilidad de igualdad. Nueva hipótesis de trabajo: C_0 completo ya firmado todos órdenes; distinto del Hankel puntual GRAM2.3. Constructor global_signed_balance, new_structural_sign y root PASS; cotejo dirigido all3. No refuta C_u/A ni transportes con otros perfiles/gauges. Sin web, cómputos o papers; signo global OPEN.


**2026-11-06 — B_1 PSD todos órdenes NO implica B_0 PSD: contramodelo suave (PROVED).** GLOBAL, «El extremo hiperbólico positivo»: B_b tiene peso sinh(b(2r+x+y))/b, B_0 lineal. Perfil phi=3g+(g(·−2)+g(·+2))/2, g normal estándar, Z=exp(a²/2)(3+cosh2a). Inversa geométrica explícita y diferencia de módulos prueban S_1=Z(a−1)/Z(a+1) contractivo; Schur/DOM firma B_1 todos órdenes. Pero K_M, M=Z'/Z, en nodos Laplace(log2/2,log2), vector(42,−41), da1−516/(34log2)<0: B_0 temporal noPSD (no se identifican esos nodos con test temporal2). Antecedente CONE001§4; diferencia gaussianizar y verificar también B_1PSD. Constructor global_concrete_reset, auditoría new_structural_sign y root PASS. Excluye transporte universal bajo paridad/positividad/suavidad/DOMgauss; NO dato theta ni sus hipótesis adicionales/supercolas. Descenso theta OPEN, sin web/cómputos/papers.


**2026-11-07 — Reciprocidad unitaria no hace contractivos los factores BPY (PROVED, clase precisa).** GLOBAL, «PF aditivo e inversión»: R_beta h=x^(−beta)h(1/x), beta=5/2, fija q y es unitario en L²(x^(beta−1)dx). Pero V_lambda=lambda(D+lambda)^(-1) causal NO es contractivo para NINGUNA lambda>0: h_R=h(x/R), v_R=h_R'+lambda h_R, da diferencia de normas R^(alpha−1)[lambda alpha R B−A]>0, alpha=3/2, A,B positivos explícitos. Antecedente VIRTUAL_SOURCE_017§§1–4 cambia métrica; nuevo cálculo sobre factores exponenciales BPY completos en métrica recíproca. new_structural_sign/root y auditoría PASS. Sólo impide esa composición de contracciones; no descarta producto completo/otras compensaciones ni PF+reciprocidad. Cotejo adicional: derivadas del producto devuelven renovación registrada; inversión del kernel aditivo devuelve cambio Möbius ya examinado. Sin nueva cota conjunta ni signo A, sin web/cómputos/papers.


**2026-11-07 — Convolución BPY COMPLETA no acotada en métrica recíproca (PROVED).** GLOBAL, «El producto BPY completo»: H=L²(x^(3/2)dx), T_f causal, f=2pi q. h_epsilon=epsilon^(−5/4)h(x/epsilon), h>=0 compacto(1,2) normalizado, tiene norma1 y ||T_fh_epsilon||>=c epsilon^(−1/4), usando min_[1/2,2]f>0. Cada salida está en H; no existe extensión acotada. Control separado lejos0: h_R=h(x/R) da defecto de contractividad alpha m R^alpha B+O(R^(alpha−1))>0 por Taylor y momento exponencial BPY. Diferencia: evalúa producto completo, no infiere desde sus factores. Root/new_structural_sign PASS; cotejo all3. T_fq!=q (LaplaceL²!=L); normalización por filas cambia operador, kernel k devuelve renovación anterior. Sólo descarta este mecanismo normativo, NO A/PF+reciprocidad. Sin web/cómputos/papers.


**2026-11-07 — Diagnóstico único de C_1, sin falsificador (NUMÉRICO, no certificado).** GLOBAL: bloque de pareja recíproca C_1 en nodos(−1,−1/2,0,1/2,1), fórmula par integrada con tanh(v); primer autovalor normalizado aproximado0.01323704, todos positivos en cálculo double truncado. Fórmula auditada new_structural_sign, cotejo all3: no confundir con antiguo generador gauge C_1. NO certificado ni avance de signo global; sin barrido adicional. Parejas C_u y A siguen OPEN; papers intactos.


**2026-11-07 — Restricción explícita de deriva operatorial (PROVED en clase regular).** HYPERBOLIC§12.5. Q par C4, Q''=CQ, sinh(v)Q'+cosh(v)DQ=BQ, B,C,D simétricos en dominio común y DQ continuo: K=.5[F(v+z)+F(v−z)] fuerza L=<DQv,Qz>=.5[G(v+z)+G(v−z)], G=−coth(t/2)F'(t), G0=−2F''0. Luego Lvv=Lzz; L no se presupone PSD. Con dominios DC/CD y diferenciación en grafoD adicionales sólo se deduce conmutador débil nulo contra spanQ; NO conmutación fuerte. Diferencia§12.4: resuelve kernel operatorial, no reducción escalar. Root/paired_kernel_fresh y auditoría new_structural_sign PASS, cotejoall3. No realización theta, Green ni signoA; escapeoperatorial OPEN. Sin web/cómputos/papers.


**2026-11-07 — Proceso físico SIN PLEGAR tampoco monótono en orden usual (PROVED).** GLOBAL, «Conservar ambas ramas»: para A_markov=−L de106.41, tasa superior Q_x(z), z<log2 próximo, Q'_0/c=−integral_z∞g'K+sum a_nK'(logn)<=g(z)Kz+a2K'(log2)<0. Cada modo theta enlog2 da derivadalog<−19; límiteupper<K(log2)/sqrt2[4/3−19log2]<0. Umbral sin cruces y colas completas justifican derivación/suavización; dos estados ordenados violan condición necesaria de monotonía. Diferencia106.115: recta completa y defecto continuo de tasas, NO salto plegado de reflexión. Root/new_structural_sign PASS, cotejoall3 y10641/42/115. Sólo orden usualR, no otrosconos ni signoA. Sinweb/cómputos/papers.


**2026-11-07 — Semigrupo físico no preserva convexidad PAR (PROVED).** GLOBAL, «El semigrupo físico tampoco conserva las funciones pares convexas». Test suave de bisagra(|x|−R)+, R↑log2, plano cerca0: (A_markov f)''0/(2c) tiene Gamma<K0, cola entera n>=3<K0, contacto2<−38K0/3. Cotas modales p_j''<=y²p_j y series geométricas controlan todos modos/contactos, sin cómputos. Mollificación par positiva deja contactos en región lineal. Testdual psi=rho''/(dmu/dx) delcore, fL²mu, muestra derivada negativa de integralP_tf rho'' inicialmente0: no preservaciónconvexa sin asumir fDomA ni P_tC². Diferencia106115/últimoGLOBAL: reflexión preservaconvexidad, pero tasas completas destruyenestecono;106112Bochner y10364otroobjeto. Root/paired_kernel_fresh, auditoría new_structural_sign PASS, cotejoall3. No signoA ni descarte deotrosconos; papers intactos.


**2026-11-07 — T*T/Hardy ponderado: identidad sin cota nueva (control de duplicación).** GLOBAL: B_j=Lg−2sumΛ(m)m^jD_m², E_j(U)=integral t^(j−1/2)[logt|U|²+ReB_jUbarU]. Para P(1)=0, (B2P)'=B4P' e IBP da Q=(pi²/2)(4E4(P')−6E2(P)−6||P||²_t3/2). Borde−6P1·bar(B2P1) desaparece sin exigirP'1=0. Hardy de normas solas no firmaB_j; no estimación conjunta obtenida. GaugeR=e5x/4P(e^x) devuelve dato físico F=−2pi(R'+R/4). Constructor global_signed_balance/root verificación directa, cotejoall3/GRAM. NO nuevo signo ni NO-GO general; no repetir identidad como cierre. Papers intactos.


**2026-11-07 — Traslaciones imaginarias conjugadas de C_0 no minoran A (PROVED, clase precisa).** GLOBAL, «Traslaciones imaginarias conjugadas»: K_eta=C0(x+i eta,y-i eta), |eta|<pi/4. Theta completa da K_eta(x,x)~pi³/c_eta exp(9x-2pi c_eta exp(2x)), c_eta=cos2eta, uniforme en compactos interiores. Así K_eta/D0>=1/2 uniformemente, mientras A(x,x)/D0<=x/sinh2x->0 y Cu/D0<=u^-1exp(-2x)->0. Ninguna mezcla positiva fija no nula sin gauges puede minorar ni representar A o Cu, 0<u<=1. Diferencia frente a traslaciones reales: argumentos imaginarios conjugados interiores, no cubiertos por aquel descarte. Constructor global_sign_independent_attempt/root, auditor new_structural_sign PASS, cotejo all3 sin antecedente literal; sin prioridad mundial. Sólo esta clase, no negatividad de A ni descarte de gauges/congruencias generales. Sin web/cómputos/papers.


**2026-11-07 — Cociente integrado A/C0 no PSD, incluso con gauges (PROVED).** GLOBAL, «El cociente integrado A/C_0»: diagonales H(x,x)<=x/sinh2x->0, pares; antidiagonal H(x,-x)->1/2. Prueba completa: nu_x proporcional a2sinh2r Phi(x+r)Phi(x-r) concentra en0; lower c exp(7x-2pi exp2x), colas delta..x y x..infinito controladas con theta completa. Menor{−x,x}->−1/4. Para Cu/C0, u>0 fijo, mismo argumento da antidiagonal(1+u)^−2, diagonal0, menor negativo. Factores diagonales no nulos sólo congruencia del cociente: no reparan transporte Schur. Diferencia frente a q_u puntual: aquí kernels ya integrados; no deducible de aquel no-go. Root/global_sign_independent_attempt, auditor new_structural_sign PASS, cotejoall3. Sólo cocientes, NO A/Cu negativos ni descarte de otros transportes; sin web/cómputos/papers.


**2026-11-07 — Proyección ortogonal de divisibilidad: aplicación de densidad (PROVED).** GLOBAL, «Control de la sustitución ortogonal»: en H=L²dt/(2t), clausura span h_(m²k)=H por GRAM17.7 escalado x=exp(-pi m²t); Pi_m=I. Sustituir selección coordenada P_m por Pi_m en factorial pierde divisibilidad. R_mF=m^-1/2F(m²t), norma<=m^-1/2||F||; suma Lambda(m)||F-R_mF||² diverge siF!=0, ya sobre potencias2. No elimina resto firmado ni prueba Q negativo; sólo invalida ese reemplazo. Root/global_sign_independent_attempt, auditor new_structural_sign PASS, cotejoall3. Aplicación del antecedente, no herramienta nueva ni signo; sin web/cómputos/papers.


**2026-11-07 — Realización operatorial theta explícita (PROVED, no signo).** HYPERBOLIC§12.6: H=L²(sech(pi omega/2)domega) directaR³, Q=(cos omega v,cosh(v/4),cosh(5v/4),cosh(9v/4)); C multiplicador(-omega²,lambda_j²). Dcontinuo=1+omega coth(pi omega/2)+(15/2)cosh(pi omega/2)/cosh(2pi omega), Ddiscreto=(-29/4,-23/4,-9/4). BQ=sinhvQ'+coshvDQ define operador simétrico densamente definido sobre spanQ, clausurable; C,D autoadjuntos y dominios de grafo verificados. qtheta=Phi(v/2)exp(2pi coshv) es observación continua exacta: restar trescosh deja residual analítico strip pi/2, O(exp(-|Re v|/4)); densidadcoseno decaeexp(-pi omega/3), cuadrado/rho integrable. Diferencia12.5: se construyen objetos y observación, no sólo condiciones necesarias. Root/global_constructive_rethink, auditor new_structural_sign PASS con corrección tasa residual3/4→1/4. NO métrica compatible, Greenpositivo ni signoA; no prioridad mundial. Sinweb/cómputos/papers.


**Extensión integral de la misma realización12.6 (PROVED, no signo).** Y_nu(b)=integral_0∞exp(-bcoshv)cosh(nu v)Qv dv pertenece a grafosC,D,Bbar por superamortiguación. IBPdoble con bordes nulos da Yrr=(b²+nu²)Y+2DYr+(-C+2bBbar)Y, r=logb. Observaciónexacta <Y_nu(2pi),h>=Z(2nu), normalización completa. Root/new_structural_sign PASS de dominios y signos. No autoadjunción de la suma, métrica ni Greenpositivo/signoA.


**2026-11-07 — Métrica local acotada imposible para realización theta12.6 (PROVED, clase).** HYPER12.7: e2,e1 en grafoBbar,C,D² con Be2=−9e1/4, Be1=−7e0/2−9e2/4. Para M(r)>0 acotada localC², sin diagonalidad, compatibilidad M'=-DM−MD y simetría deE=−C+D²+2bBbar fuerzan Mij=mijexp(−(di+dj)r). Par(e2,e1) da b[−9M11+14M20+9M22]−63M21=0, exponentes25/2,21/2,11/2,8 distintos: m11=m22=0, contradicción. No Be0; límitesdegrafo yformas justificados. Diferencia12.4: realizacióntheta exacta infinita, no modelo2x2. Root/global_constructive_rethink independientes, new_structural_sign PASS. Realización12.6 permanece válida; sólo falla esa reparación local acotada con principal−I. NO métricasnoacotadas/nolocales, otrasconexiones/realizaciones ni signoA decididos. Sinweb/cómputos/papers.


**2026-11-07 — Laplace de parejas recíprocas (identidad PROVED, candidata OPEN).** GLOBAL: D_v=integralPhiPhi[exp(-v/z)-exp(-vz)]dr,z=exp(2r+x+y). Cu=integralexp(-uv)D_vdv yA=integral(1-exp(-v))/v D_vdv, Fubiniabsoluto por |h_u|/|logz|. D_v/v→C0 conmayorante|z−1/z|. PSDdeD_v∀v,tamaños bastaríaA; premisa NOprobada, sinfalsificador. Diferencia: combinarrecíprocosantesfirmar, no fuentesaditivasBPY; Poisson2Dpropuesto no introduce nm, noGram obtenido. Root/global_constructive_rethink, auditor new_structural_sign PASS; cotejoall3/E101070/renovaciónsinliteral. No nueva estimación de signo ni prioridadmundial, sinweb/cómputos/papers.


**2026-11-07 — Capa Laplace D_(2pi) indefinida (PROVED certificado; actualiza candidata anterior).** GLOBAL: bloque−1,0,1 tiene entradasd1,c,e ycentrald0; (d1+e)d0−2c² in[−6e−21 ±8.08e−22]<0. Test racional(1,−1/1300000,1) upper<−2.6e−17. Cuatrointegralesplegadas positivas,32768rectángulosArb192bits porintegral,8modos+omisiónuniforme2^-224,cola s>=4<2^-1000;inflación2^-210. Verificador tools/power_paired_laplace_counterexample_verify.py ylogsroot/audit FULLPASSexit0; SHA256 e6fee17a626174c60ecbd46a4d206deca911a3e156ec25fd4af5b0b695e7a07c. Diseño root/global_constructive_rethink, auditoría previa/literal yreproducción new_structural_sign PASS. Un diagnóstico, sinbarrido. D_vPSD∀v FALSIFIED; identidadLaplace permanece, compensaciónintegradaOPEN. NO Cu/A negativos ni ventanaT/papers modificados.


**Corolario de D_(2pi), misma entrada.** GLOBAL: testcertificadog(v)=c^TD_vc continuoacotado, g(2pi)<0; (-1)^nf^(n)(u)=integralv^nexp(-uv)g(v)dv paraf=c^TC_uc. PesosGamma enu=n/(2pi) concentranen2pi (errorcuadráticov0²(n+2)/n²), porloquederivadasalternadasnegativaseventualmente. RefutaCMmatricialenTODAu>0/cualquiercola; NOen(0,1], niPSDdeCu/monotoníaorden1/signoA. Root/global_constructive_rethink ynew_structural_sign PASS; consecuencia sincómputosnuevos.


**Control puntual posterior, NUMÉRICO no certificado.** GLOBAL: al integrar paraCu conu=1/(2pi), test fijo(1,−1/1300000,1), nodos−1,0,1, forma≈4.0700e−15 positiva en double; no falsificadorintegrado encontrado. Ocho modos/cortes sinenclosure, no PSD ni signonuevo. No barrido ni máscertificados; D_(2pi)negativo sigue sinimplicarCu/Anegativos.


**2026-11-07 — Primitivas de D_v: revisión sin avance de signo.** GLOBAL, «Primitivas de las capas»: G_V=int_0^V D_v, F_R=int_0^R D_v/v; F_R=G_R/R+int_0^R G_v/v² y A=int(-w')G_V, w=(1-exp(-V))/V. Identidades verificadas root/fresh_gap_screen/new_structural_sign; G_V PSD todos V sigue OPEN. Cambio de peso sin operación theta nueva rechazado como ruta nueva. El argumento por radicales aproximados no cierra: nodos normalizados en C0 tienen A/C0->0 y G_V/C0<=V/(2sinh(2x))->0 para cada V, aunque G_V/C0->1 al tomar V->infinito primero. Falta radical fijo en dominio común; no refutación de G_V ni A. Sin cómputos ni papers.


**2026-11-07 — Productos cosh desplazados: clausura entera incompatible con theta (PROVED).** `03-research/phase-211-sign-sandbox/POWER_HYPERBOLIC_MODEL_GRAM.md`§13. Para Q_n=prod_j(cosh(b_nj t)-c_nj)/(1-c_nj), b_nj>0, -1<c_nj<1, Q_n(1)<=M implica suma d_nj<=M-1, d=(cosh b-1)/(1-c), y b<=B=arcosh(2M-1). En |z|<=R, |Q_n(z)|<=exp[(M-1)R²cosh(BR)]. Todo límite localuniforme real se extiende a función entera. El cociente theta Phi(t)exp[2pi(cosh2t-1)]/Phi(0) diverge en la cúspide t=(log2)/2+i pi/4 ya probada; no es tal límite. Excluye aproximar Phi por C_n exp(-2pi cosh2t) Q_n a escala fija, e infinitos productos definidos por sus parciales. Diferencia frente§11/11.4: c variable evita la multiplicidad entera anterior, pero normalidad excluye la clase ampliada sin clasificar productos límite. Constructor root; filtro y auditoría independiente shifted_cosh_gate PASS, root PASS. No decide conservación de PSD por cada factor; no cubre escalas variables, otros factores, sumas, cocientes o potencias reales. Sin signo A nuevo, ampliaciónT, cómputos numéricos, web ni papers.


**2026-11-07 — Escala positiva variable en productos cosh desplazados: escape cerrado (PROVED).** `03-research/phase-211-sign-sandbox/POWER_HYPERBOLIC_MODEL_GRAM.md`§13.1 amplía§13 a phi_n=C_n exp(-a_n cosh2t)Q_n con a_n>0 variables. Nueva pieza: log[(cosh(b sqrt(s))-c)/(1-c)] es cóncava en s>=0 para b>0,-1<c<1; el numerador de x f''-f' se acota por(1+coshx)(x-sinhx)<0. Con H(s)=cosh(2sqrt(s)), delta=H0+H2-2H1>0, a_n<=[2logphi_n(1)-logphi_n(0)-logphi_n(sqrt2)]/delta. Convergencia positiva en esos tres puntos acota las escalas SIN convergencia de derivadas; normalidad§13 vuelve a aplicar y la cúspide theta excluye aproximación localuniforme real. Diferencia: a_n->infinito evadía el control complejo anterior, ahora se descarta por una cota discreta. Constructor root; filtro y auditoría independiente shifted_cosh_gate PASS, root PASS. Se retira sólo la reserva de escalas positivas variables de la misma base cosh2t; no cambios de frecuencia, otros factores, c fuera(-1,1), sumas/cocientes/potencias reales ni conservación abstracta de PSD. Sin signo global nuevo, ampliaciónT, cómputos, web o papers.


**2026-11-07 — BPY geométrico G2: OPEN, diagnóstico inconcluso.** Fuente: phase211 `POWER_GLOBAL_ROUTE_REVIEW.md`, «Aproximantes BPY geométricamente simetrizados». G_N=sqrt(Phi_N(t)Phi_N(-t)), con f_N convolución de dos exponenciales por tasa pi n², evita la cola exponencial de la media aritmética previamente descartada. Filtro independiente PASS acotado; fórmula elemental de G2 y supercola revisadas. Dos bloques de jets exploratorios dieron mínimos numéricos positivos, sin certificado; se detuvo enumeración. No Gram allorders ni falsificador, no nueva positividad o T. No repetir diagnóstico sin mecanismo nuevo. NO NO-GO de esta familia; PSD todosN y paso dominado al límite siguen pendientes. Papers intactos.


**Actualización BPY geométrico — límite PROVED, signo OPEN (2026-11-07).** GLOBAL, «Paso al límite de los aproximantes geométricos»: reservar Gamma(2,pi), evaluar E exp(pi Y_N)=[2N/(N+1)]²<=4 y convolucionar da f_N(v)<=4pi²v exp(-pi v). Así G_N(t)<=2pi²exp(-pi cosh2t) uniformemente enN. Con la convergencia previa f_N→2pi q, dominación absoluta prueba A[G_N]→A[Phi] localuniformemente, incluidos todos los cruces de cada bloque fijo. Cierra la obligación de límite de la entrada precedente; no PSD de G2 ni todosN, no comparación matricial desde la cota escalar. Root y filtro/revisión geometric_domination_gate PASS; aplicación de herramientas previas a esta familia, sin prioridad ni nuevaT. Papers intactos.

**2026-11-07 — BPY geométrico: comparación consecutiva con sech REFUTADA para todo c>0.** Fuente phase211 GLOBAL, «Comparación consecutiva BPY con congruencia sech». No existe c>0 con A[G2]>=c D A[G1]D, D(x)=sech(2x), en todos los bloques reales. Diferencia explícita frente al acoplamiento consecutivo: congruencia externa destinada a corregir la caída adicional del perfil. Filtro previo geometric_sech_congruence_gate PASS limitado a falsificación; construcción root y auditoría matemática independiente PASS. Prueba analítica completa: H(z)=z−2+(z+2)e^−z no se anula en Re z>0 por identidad energética elemental, lo que define G2 holomorfa en |Im z|<pi/4. A[G2](iy,−iy) queda uniformemente acotado; A[G1](iy,−iy) tiene cota inferior positiva y D(iy)D(−iy)=sec²(2y) diverge. PSD real implicaría diagonales complejas no negativas por jets y Taylor, contradicción para cada c. Existe por tanto un bloque real finito negativo del RESTO para cada c, sin orden/coefs explícitos ni cómputos. No negatividad de A[G2] ni de A[Phi]; otras congruencias no decididas. Límite geométrico sigue probado, signo global OPEN, sin nuevaT ni cambios en papers.


**2026-11-07 — BPY G1→G2: exclusión de TODA congruencia holomorfa en la franja (PROVED).** Fuente GLOBAL, «Ampliación: ninguna congruencia holomorfa no nula transfiere G1 a G2». Si D es holomorfa en |Im z|<pi/4, real sobre R, y c>0, PSD de A[G2]−c D A[G1]D implica D idénticamente0. No se supone crecimiento, extensión al borde ni ausencia de ceros. Diferencia frente al factor sech: A[G1](x+iy,x−iy) diverge uniformemente para x en compactos positivos al subir y a pi/4, mientras A[G2] permanece acotado. Jets/Taylor fuerzan D→0 uniformemente en esos segmentos; continuidad, reflexión y unicidad concluyen. Construcción root; filtro previo y revisión matemática independiente geometric_sech_congruence_gate PASS. No afirma PSD para D=0 ni negatividad de G2, no cubre factores con franja menor u operaciones no diagonales. Sin cómputos ni nuevaT; papers intactos, signo global OPEN.

**2026-11-07 — Cierre BPY G1→G2 para CUALQUIER factor diagonal real (PROVED).** GLOBAL, «Cierre de la transferencia diagonal: regularidad automática del factor». Para cualquier D:R→R y c>0, PSD de A[G2]−cD A[G1]D implica D≡0, sin hipótesis iniciales de regularidad. L=cD A[G1]D es PSD y dominado por K=A[G2]; el Hilbert de K y un operador 0<=T<=I prolongan L holomórficamente mediante jets/Taylor. Una sección real estrictamente positiva da analiticidad real de D. Ausencia de ceros comunes de las secciones de A[G1] en Re z>0 permite pegar cocientes y extender D allí. La desigualdad compleja y el contraste uniforme de borde anterior fuerzan D=0. Constructor root, filtro y auditoría independiente geometric_sech_congruence_gate PASS. Se cierra buscar otros factores diagonales, incluidos los de franja menor. No afirma que D=0 sea suficiente, ni refuta PSD de G2; transferencias no diagonales fuera de alcance. Sin cómputos, nuevaT o papers; signo global OPEN.


**2026-11-07 — G2: energía derivada de borde y presupuesto de ramas finitas (PROVED, sin signo nuevo).** Fuente phase211 `POWER_GLOBAL_ROUTE_REVIEW.md`, «G2: la energía derivada de borde supera cualquier colección fija de ramas». Para x>0 fijo, E_x(epsilon)=integral_x^infinito 2t|G2'(t+i(pi/4−epsilon))|²dt satisface E_x/log(1/epsilon)->infinito. Las raíces auxiliares H(iu_j)=0 tienen u_j~2pi j; el coeficiente local w_j=|(G2²)'(z_j)|/4~C²d^6/(48u_j) da contribución 4t_jw_j log(1/epsilon)+O_j(1). La suma de t_jw_j diverge: colección finita primero, límite después, colección creciente al final, sin uniformidad en j. Cada colección fija de vecindades aporta fracción->0 de la diagonal completa. B_x=partial_z partial_w A2(x+iy,x−iy)=E_x−|G2(x+iy)|² conserva el borde y tiene el mismo límite normalizado. Resuelve el presupuesto diagonal pendiente del filtro de dos singularidades; NO controla el cruce completo, no descarta ese menor ni prueba/refuta PSD de G2 o Phi. Constructor root; filtro previo y auditoría independiente g2_tail_residue_novelty_gate PASS. Cotejo dirigido Paper48/all3/primarias, sin prioridad mundial. Sin cómputos, nuevaT o cambios en papers; global OPEN.


Fase 212, mapa consolidado de las rondas 1–17: tabla por familia, restricciones sobre el objeto (cláusulas O11–O17 de `OBJECT_SPEC.md` §5) y terreno sin objeto ni cierre, en `03-research/phase-212-missing-object/MAP_ROUNDS.md`. Sin mecanismo de signo; global OPEN.
