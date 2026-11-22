# R185_007 — Residual (ρ1″): statements about the full tail (unbounded-type tests)

Phase 185 (crossword). Pure mathematics, no numerics. RH is never asserted.
Inputs: R185_003 (Lemma 2∞, Thm 1–2, Prop 3, §3), R185_092 (m3), R185_004 (§2, Def 5), R185_005 (BR), R166_802 (Thm 1–3),
R164_000 (TC, Rem 4.8a), R164_601 (Thm 3.1–3.3, W2/M), R164_190, Paper 46 (Theorem Z, thm:finZ), R163_101.

## State

| Item | Statement | Label |
|---|---|---|
| Def 1 | Weil class 𝒦^∞_ε: K ≥ 0 continuous on ℝ, Ǩ even, e^{(½+ε)|x|}Ǩ ∈ L¹ ∩ BV(ℝ), ε > 0 | definition |
| Lemma 1 | K ∈ 𝒦^∞_ε ⟹ Ψ = G²K is in the Weil–Barner class (exact explicit formula, Σ_ρ absolutely convergent) | PROVED (over CITED Weil/Barner/Bombieri) |
| Lemma 2 | For K ∈ 𝒦^∞_ε the tail Tail^∞_K(Λ) converges absolutely; U_K < ∞ | PROVED |
| Obs 2.1 | Without ε (weight e^{−ax}, a ≤ ½): convergence of the pole-corrected tail ⟺ a > Θ − ½ (Landau): already a zero statement | PROVED-CITED |
| Thm 1∞ | M1 circularity for arbitrary families 𝔉 ⊂ ⋃_ε 𝒦^∞_ε: a single K* with Z_{K*}(Σ_ζ) < Q^{hyp} − S | PROVED |
| Thm 2∞ | Same M2 with 𝓡 compact (product topology); K* = finite, ≥ 0 combination, in the Weil class | PROVED |
| Prop 3 | Power-type families K_Y: "Tail_{K_Y} = O(Y^{δ′})" ⟺ Θ ≤ ½ + δ′; excludes exactly the quadruples with δ_q > δ′ | PROVED-CITED (R166_802 Thm 3) |
| Cor 3.1 | Excluding all witnesses via power-type families ⟺ ∀δ′>0 ⟺ Θ = ½ ⟺ RH | PROVED |
| Classif. (ρ1″) | {circular in M1/M2 (PROVED)} ∪ {partial Θ: not E1, quasi-RH strength, OPEN, outside the corpus's methods (W2/M)} | PROVED (classification) |
| (TC) | type **Q** in R185_004's table; invariant under finite modifications of the tail; non-L PROVED; non-D ARGUED | DECIDED |

Verdict: **(ρ1″) is closed** as a circularity residual. The only thing not E1 in unbounded type is exponent
statements Θ ≤ ½+δ′ (quasi-RH), which are not circular in the sense of "false if the quadruple is present" only for
δ_q ≤ δ′, and whose proof without zeros is a classical open problem (not even Θ < 1 is known). No row D label
changes.

## 0. Framework

Same as R185_003 §0, except that 𝔉 may contain K with no finite type. For such K, Ψ = G²K, Ψ̌ = (G²)^∨ ∗ Ǩ no longer
has compact support, and the split at X = e^{2T_c} is defined by convention:
  (1.1∞) Z_K(Σ) = 𝔄_K − Tail^∞_K(λ), Tail^∞_K(λ) := Σ_{n ≥ X} λ(n) n^{−1/2} Ψ̌(log n) (plus the symmetric n^{+} term per
  Paper 45/47's normalization), with 𝔄_K = archimedean + polar terms + primes n < X.
This is the same identity; the only change is that the "window" no longer isolates the tail in a finite interval. In
particular the tail weight w := Ψ̌|_{[2T_c,∞)} is the w of the task, and every w satisfying Def 1's conditions
(transported by convolution with (G²)^∨, support in [−2T_c,2T_c]) arises this way.

## 1. Admissibility (new point (i))

**Weil–Barner class. CITED** (Weil 1952; Barner 1981; Bombieri, *Remarks on Weil's quadratic functional*; the form
used in Paper 45 §explicit formula). If g: ℝ → ℂ is even, e^{(½+ε)|x|}g ∈ L¹ ∩ BV, normalized at jumps, and h = ĝ,
then h is holomorphic in |Im t| < ½+ε, h(t) ≪ (1+|t|)^{−1} uniformly in |Im t| ≤ ½ + ε/2 (by BV), and the explicit
formula holds: Σ_ρ h(t_ρ) = polar + archimedean − Σ_n Λ(n)n^{−1/2}(g(log n)+g(−log n)), with Σ_ρ convergent (in the
symmetric sense; absolutely if h ≪ (1+|t|)^{−1−η}).

**Lemma 1. PROVED.** Let K ∈ 𝒦^∞_ε (Def 1) and G = F̂, F ∈ C_c^∞ even with support in [−T_c, T_c] (witness). Then
g := Ψ̌ = (G²)^∨ ∗ Ǩ satisfies the Weil–Barner hypotheses with the same ε, and Σ_ρ |Ψ(t_ρ)| < ∞.
*Proof.* (G²)^∨ = F∗F ∈ C_c^∞ with support in [−2T_c, 2T_c]; e^{(½+ε)|x|} ≤ e^{(½+ε)2T_c} e^{(½+ε)|x−y|} for |y| ≤ 2T_c,
hence e^{(½+ε)|x|}g ∈ L¹ and BV (convolution with C_c^∞ preserves both). Moreover Ψ = G²K with |K(t)| ≤ ‖e^{(½+ε)|x|}Ǩ‖_{L¹} in
the band and G² ≪_N (1+|t|)^{−N} in the band (F ∈ C_c^∞, Paley–Wiener); with N(T) ≪ T log T, Σ_ρ |Ψ(t_ρ)| < ∞. ∎

Exact condition on the family: **exponential decay of Ǩ (and of w) strictly greater than e^{−x/2}** plus BV. The
smoothness of w is not needed for absolute convergence in ρ: that is provided by G² (the C_c^∞ witness). This
corrects the task: what decides it is the decay exponent of w, not its smoothness.

## 2. Tail convergence and finiteness of U (points (ii), (iii))

**Lemma 2. PROVED.** For K ∈ 𝒦^∞_ε: (a) Σ_{n≥X} Λ(n)n^{−1/2}|Ψ̌(log n)| < ∞; (b) 𝔄_K is finite; (c) U_K := 𝔄_K − Q^{hyp}_K + S_K < ∞
whenever S_K < ∞.
*Proof.* (a) e^{(½+ε)x}g ∈ L¹ ∩ BV ⟹ e^{(½+ε)x}g(x) bounded (BV) ⟹ |g(log n)| ≪ n^{−½−ε}, and Σ Λ(n)n^{−1−ε} = −ζ′/ζ(1+ε) < ∞.
(b) polar term = h(±i/2) finite (holomorphy in |Im t| < ½+ε); archimedean: ∫ h(t)Re Γ′/Γ(¼+it/2)dt, convergent by
h ≪ (1+|t|)^{−N}; primes n < X: finite sum. (c) Q^{hyp}_K = 4Re Ψ(t_q) finite by holomorphy (|δ_q| < ½). ∎

**Obs 2.1 (boundary ε = 0). PROVED-CITED (Landau).** Taking w(x) = e^{−ax}·(smooth cutoff at 2T_c), 0 < a ≤ ½:
- absolute convergence of the tail ⟺ ∫ e^{x/2}w < ∞ ⟺ a > ½ (by Chebyshev ψ(x) ≍ x, Λ ≥ 0);
- the pole-corrected tail, Σ_{n≥X}Λ(n)n^{−½−a} − ∫_X^∞ t^{−½−a}dt, converges ⟺ ½ + a > σ_c(−ζ′/ζ − 1/(s−1)) = Θ
  (Landau: Λ ≥ 0 ⟹ σ_c = σ_h; the pole at s = 1 is the only one on ℝ).
Hence, below the Weil class, **mere convergence of the statement is already a statement about Θ**. A statement B
that uses weights with a ≤ ½ already presupposes (or asserts) Θ < ½ + a: it is not zero-neutral. This is recorded in Prop 3.

## 3. Circularity for the full tail

**Thm 1∞ (M1). PROVED.** Let 𝔉 ⊂ ⋃_{ε>0}𝒦^∞_ε be arbitrary (unbounded types, scales Δ → ∞, families e^{−sx} with s > ½,
smooth cutoffs at all scales). If a proof using only B, the identities (1.1∞) for K ∈ 𝔉, O_K ≥ 0 and bounds
R_K ≥ −S_K excludes the witness, there exists K* ∈ 𝔉 with
  Tail^∞_{K*}(Λ_ζ) > U_{K*}, equivalently Z_{K*}(Σ_ζ) < Q^{hyp}_{K*} − S_{K*},
a zero-side inequality that is false if the quadruple is present and R_{K*} ≥ −S_{K*} is true.
*Proof.* That of R185_003 Thm 1 uses: (1) Lemma 2∞ (purely set-theoretic); (2) that t_ζ ∈ ℝ^𝔉 (Lemma 2(a)); (3) that
U ∈ (−∞,∞]^𝔉 (Lemma 2(c), with the Obs 1.2 convention for S_K = ∞); (4) the true identity (1.1∞) (Lemma 1 + CITED);
(5) O_K ≥ 0 (K ≥ 0 on ℝ, G real on ℝ, absolutely convergent series by Lemma 1). None uses finite type. ∎

**Thm 2∞ (M2). PROVED.** With 𝓡 convex compact in the product topology, there exists K* = Σ_{i≤m}a_iK_i, K_i ∈ 𝔉, K* ≥ 0 on ℝ, with
the inequality of R185_003 Thm 2. K* ∈ 𝒦^∞_{min ε_i}: the class is a convex cone stable under finite combinations with
K* ≥ 0. *Proof.* R185_003 Lemmas 5–7 and Thm 2 do not use the type; Lemma 7 uses the convergence of Σ_γ G²K, given by
Lemma 1. ∎

**R185_003 Prop 3 (mixtures) in unbounded type. PROVED** with the substitute hypothesis sup_{K∈supp μ}‖e^{(½+ε)|x|}Ǩ‖_{L¹∩BV} < ∞
(uniform ε): then K_μ ∈ 𝒦^∞_ε and the three linearities (Tail, Z, 𝔄) transfer by Fubini with the Lemma 2(a) majorant.
If ε_K → 0 on supp μ, the mixture may leave the Weil class: back to Obs 2.1 (a statement about Θ).

**Consequence.** For individually admissible tests, (ρ1″) is **not** a new residual: the full tail is handled
exactly like the finite-window tail. Finiteness of type was never used; Weil admissibility was.

## 4. The genuinely different part: power-type families and partial Θ

Let K_Y be a power-type family (smooth cutoff at log Y, Y → ∞; each K_Y is even of finite type). The statement
  B_{δ′}: ∃C ∀Y ≥ X: |Tail_{K_Y}(λ)| ≤ C Y^{δ′}
is not a conjunction of test-by-test bounds with U fixed: C is existential. For each fixed C, B_{δ′,C} is of the
form of R166_802 Thm 1(b) (two-sided) and Thm 1∞ applies. The new content is in the quantifier ∃C.

**Prop 3. PROVED-CITED (R166_802 Thm 3(b),(c)).** For δ′ ∈ (0,½): B_{δ′}(Λ_ζ) ⟺ Θ ≤ ½ + δ′ (up to ε, with smooth
cutoffs). A quadruple with δ_q > δ′ forces Tail_{K_Y} = Ω(Y^{δ_q}) via (1.1∞) (Landau), so B_{δ′} excludes it; a
quadruple with δ_q ≤ δ′ is compatible with B_{δ′}.

**Cor 3.1. PROVED.** (a) Excluding every witness (every δ_q ∈ (0,½)) with power-type families requires B_{δ′} for
every δ′ > 0, i.e. Θ = ½, i.e. RH. (b) Excluding witnesses with δ_q > δ′ is equivalent to Θ ≤ ½ + δ′: a partial statement.

**Status of (b).**
- It is not E1 in the strict sense: for δ_q ≤ δ′ the statement B_{δ′} is true even if the quadruple exists, so it is
  not "false if the quadruple is present". It is a zero statement of a different class: a uniform vertical zero-free
  region Re s > ½ + δ′.
- Strength: quasi-RH. Today no Θ < 1 is known by any method (the de la Vallée Poussin region and the
  Vinogradov–Korobov one tend toward Re s = 1 with height; zero-density estimates and the Lindelöf hypothesis
  **do not** imply Θ < 1). CITED (standard; Titchmarsh ch. 6, 9, 14; Montgomery–Vaughan §15). It is not claimed to be
  "as hard as RH": only that it is OPEN and has no known method.
- Corpus (grep "Θ <|quasi-RH|Lindelöf" in 03-research): **no phase proves or attacks a partial bound on Θ for ζ.**
  Occurrences: R163_101 (θ < ⅓ is a **Beurling** exponent — error in N(x) —, not Θ of ζ; O163.101b), R164_601 Thm 3.3
  (Λ ≥ 0 excludes only the dlVP region, ½ − δ_q < c/log γ_q: **W2/M**, computed loss), R167_101 and R164_190 (Phragmén–
  Lindelöf as a tool, not Lindelöf). R166_802 Thm 4: sieves give only the trivial exponent (Θ ≤ 1).
- Relation to row D: row D is the complete statement (every δ_q). A bound Θ ≤ ½ + δ′ with δ′ < ½ would **not** close
  D, but it **would be** a genuine intermediate result (and new in the literature). By W2/M (R164_601) and R166_802
  Thm 4, the corpus's methods (Λ positivity, sieves, window certificates) reach no δ′ < ½. Recorded as OPEN outside
  scope, not as a proven NO-GO (W2/M is a method wall, not an impossibility theorem).

**Final classification of (ρ1″). PROVED (as a classification).**
(ρ1″) = {full-tail statements with admissible tests (individual, unions, combinations, uniform-ε mixtures):
circular, Thm 1∞/2∞} ∪ {asymptotic statements with quantifier ∃C (power-type families) or weights below the Weil
boundary (Obs 2.1): equivalent to Θ ≤ ½ + δ′, not E1, quasi-RH, OPEN, outside the corpus's methods (W2/M; R166_802 Thm 4)}.
The case δ′ → 0 of the second class is RH.

## 5. (TC) in R185_004's table

(TC): C_{T_c} − iG²𝒯_X with no poles for Im x ∈ (−½, 0), with 𝒯_X the transform of the full tail Λ|_{[X,∞)}.
- At the witness (λ = Λ_ζ): (TC) is RH (Rem 4.8a; R163_801 Cor 3.1). CITED (corpus).
- As a statement about λ:
  - **not L. PROVED.** A finite modification of λ beyond Y adds to 𝒯_X a finite sum Σ c_n n^{−½−ix}… entire:
    it does not change poles. So (TC) is **invariant under finite modifications of the tail** and does not depend on
    λ|[1,Y] for any Y: its truth is fixed by behavior at infinity.
  - **not C.** It is not claimed to identify ζ; it is not used.
  - **not D: ARGUED.** Deleting an infinite set S of primes ≥ X changes 𝒯_X's poles by those of −Σ_{S}Λ(n)n^{−s},
    whose poles/abscissa are not controlled in general (in R185_004 (iii-b) the subsystems of ℕ already reproduce
    RH). No explicit written counterexample exists; it remains ARGUED.
  - **Q. DECIDED.** By Landau/Hardy–Riesz (Λ ≥ 0), "no poles in the strip" for the tail's transform is equivalent to
    a growth bound on the tail's exponent: it is a quantitative statement at infinity, the same class as "PNT with
    error" in the table, and it is precisely the second class of §4 with δ′ → 0.
- Relation to (ρ1″): (TC) **is** the δ′ → 0 member of the second class. It is neither new circularity nor a new
  escape route: it is RH in Q form. This replaces R185_003 §3's "no implication asserted" with a precise location,
  without changing any label of (TC) (it remains OPEN).

## For the audit

1. **Lemma 1, Paley–Wiener constant.** The decay of G² in the band |Im t| ≤ ½+ε uses F ∈ C_c^∞ (Paper 46's witness).
   If the witness is only finite-type with G ∈ L², replace with Barner's h ≪ (1+|t|)^{−1} and symmetric convergence.
2. **Normalization.** (1.1∞) must be checked against def:W/eq:nuw of Paper 46 (editor's rule), especially the factor
   2Re and the n^{+} term for Ψ̌ not supported in [−2T_c−Δ, 2T_c+Δ].
3. **Uniform ε in mixtures.** Without it, R185_003's Prop 3 may leave the Weil class; that does not break the
   classification (it falls into the second class) but it does break factorization through a single test.
4. **"Not E1".** Used in the strict sense: B_{δ′} is not false in the presence of the quadruple when δ_q ≤ δ′. It is
   not claimed to be "easier": it is OPEN.
5. **(TC) type Q.** "not D" is ARGUED, not PROVED. If required, downgrade to "Q or D, not L, not C".
6. Neither RH nor Θ < 1 is asserted.

## For Paper 46/48

- Add to the residual remark after the circularity theorem: "Finiteness of type is not used; the conclusion holds
  for every K ≥ 0 with e^{(½+ε)|x|}Ǩ ∈ L¹ ∩ BV (Weil–Barner class). Below the boundary ε = 0, convergence of the
  tail itself is already a statement about Θ."
- New proposition (short): power-type families ⟺ Θ ≤ ½+δ′ (R166_802 Thm 3), excluding exactly δ_q > δ′; δ′ → 0 is RH
  and coincides with phase 164's (TC) (type Q).
- Do not introduce "Θ < 1" or "quasi-RH" as program goals; mention them only as a method limit (W2/M).

## Note (R185_093)

* Obs 2.1: Landau does not apply to Σ(Λ(n)−1)n^{−s} (variable sign); σ_c = Θ is true by the explicit formula + holomorphy; no "⟺" at the boundary.
* (TC): "DECIDED type Q" → "not L, not C; Q or D (OPEN)".
