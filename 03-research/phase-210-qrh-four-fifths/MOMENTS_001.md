# The two moment estimates of the 7/8 manuscript: ranges, recursion, terminal bounds, and the lower bound on κ

**Result.** Both moments of the 7/8 manuscript (Lemma 17.1, the marked inverse moment, and Lemma 18.1, the plain fourth moment with short prime factors) are bounds of large-sieve quality: the squared exponent equals the row count, which is sharp up to Z^ε, so no iteration of their recursions can improve the exponent; what the recursions decide is the admissible *range* of lengths, and that range is fixed by the terminal estimate at the root node, not by the depth. For Lemma 17.1 the range is the dual-length condition r + 2z ≤ m (columns shorter than rows) together with a second condition coming from the column branch of the reflected energy; for Lemma 18.1 the range is the affine region A + (6κ − 1)z ≤ M, in which the only external input is the zero-free hypothesis β∗ ≤ (1 + κ)/2 behind the prime estimate (18.12). The restriction κ ≥ 3/4 in Lemma 18.1 is a convenience: in the text it is used in exactly one displayed inequality (the comparison step before (18.16), "6κ − 1 ≥ 7/2, hence z < M/21") and in three uniformity sentences that need only a compact range; the same proof goes through verbatim for every κ > 1/2 with the explicit margin (M/6)(6κ − 3)/(6κ − 1) in place of M/15. For the target 4/5 the dynamic value is κ = 2β∗ − 1 ∈ (3/5, 3/4], so Lemma 18.1 must be extended to κ ∈ [3/5, 1]; the extension is routine (PROVED as an algebraic recomputation of the affected lines, CONDITIONAL on the unaudited remainder of the published proof). It restores the dynamic plain capacity (1 − 2m)/(6κ) and changes the constants of Proposition 19.2 explicitly (D_x = 3 − 19x/9, P_x = (2 − 10x/9)(1 − x)), but it does not touch the row-floor certificate deficit found before, because that certificate counts rows trivially (R = 1) and uses no moment at all. Labels: statements of the manuscript are CITED; the exponent identities checked here are PROVED; the extension of Lemma 18.1 is CONDITIONAL; the consequences for the 4/5 certificate are OPEN.

## 1. Index and prior notes

Index entry L74 records the 7/8 manuscript as an external, unaudited claim and its mechanisms (completed mean squares, quadratic large sieve, Möbius transfer) as a toolbox. The phase 209 notes QRH_EXPONENT_MAP, QRH_FOUR_FIFTHS_ATTEMPT and QRH_HIGH_CANDIDATE_AUDIT read Sections 15, 16, 19 and 20 and raised the restriction κ ≥ 3/4 (QRH_HIGH_CANDIDATE_AUDIT, Section 2) without opening the proof of Lemma 18.1; they proposed the conservative choice κ = max{3/4, 2β∗ − 1}, which loses capacity, and left open whether the lemma itself extends. Nothing below repeats those computations; Sections 17 and 18 of the manuscript are read here for the first time. All line references are to the text extraction `00-references/qrh-preprints/openai-qrh-seven-eighths.txt`.

## 2. Lemma 17.1: the marked inverse moment (CITED)

**Objects.** Rows are elements u ∈ O with 0 < q_u ≪ Z^m. The row character is ψ_u(n) = ν(n)χ_n(u)^{ε_χ} with ν a fixed finite-order ray character of conductor in S and ε_χ ∈ {±1}. The inverse polynomial is

    M_u(Z^r; W) = Z^{−r/2} Σ_n μ(n) ψ_u(n) W(q_n / Z^r),

and the slots are Q_u = Π_{i∈I} Z^{−z_i/2} Σ_{p∈P_i} a_i(p) ψ_u(p) W_i(q_p / Z^{z_i}), with disjoint prime sets P_i outside S, |a_i(p)| ≤ 1 independent of u, z = Σ z_i.

**Statement (lines 6957–6973).** For bounded ranges of m, r, z_i, a bound on |I|, and constants c_1, c_2 > 0, if

    (H1)  r + 2z ≤ m − c_1,        (H2)  2r + 8z ≤ 3m − c_2,

then Σ_{u} |M_u(Z^r; W) Q_u|² ≪ Z^{m+ε}, uniformly in the prime supports and coefficients, for either sign ε_χ and every subcollection of slots, with no mesh condition on the z_i and no lower bound on them.

**Shape of the bound.** Z^m is the number of rows; each normalized factor has mean square of order one, so the bound is the diagonal. It is sharp up to Z^ε whenever the row characters are asymptotically orthogonal on the column support (ARGUED; this is the usual lower bound for a mean square and is not needed below).

**Relation between (H1) and (H2).** From (H1), 2r + 8z ≤ 2m − 2c_1 + 4z, so (H2) follows from (H1) whenever 4z ≤ m − 2c_1 + c_2. Thus (H2) is binding only for slot length above about m/4. At m = 1 (the application in Section 19), the inverse capacity z_M(r) = (1 − r)/2 is below 1/4 exactly for r ≥ 1/2, and the manuscript indeed uses the capacity only where (H2) keeps a margin (line 11134, and the margin 9/37 at line 11266 since r ≥ 23/37 there). PROVED (one-line algebra).

## 3. Lemma 17.2: the canonical family and its two invariants (CITED, structure PROVED)

**Objects (lines 6991–7028).** Rows k ∈ O, 0 < q_k ≪ Z^M; averaged squarefree labels f with q_f ≍ Z^V and weight w(f) ≤ C d_O(f)^C; columns n squarefree of length N with coefficient ᾱ(n)γ_2(n)ν(n)ρ(n)χ_n(k)χ_n(f)^4 d(n), where ρ is a fixed puncture of radical norm Z^Q and d is a product mark of total slot cap z_0. Put F_0 = N + V. The energy is

    E = Z^{−V} Σ_f w(f) Σ_k | Z^{−N/2} Σ_n (coefficient) W(q_n/Z^N) |².

**Hypotheses (17.2).** Q ≤ F_0 − M − z_0 − c_∗ and 3M + 6z_0 + c_∗ ≤ 4F_0. **Conclusion.** E ≪ Z^{F_0+ε}.

**Shape.** The bound is Z^{N+V}, the column-plus-label length, not the row count Z^M. By the first hypothesis F_0 ≥ M + z_0 + c_∗, so Z^{F_0} is the larger of the two trivial sizes; the lemma is the large sieve in the regime "columns at least as long as rows". The inverse moment of Section 2 lives in the opposite regime (rows longer than columns, bound = rows); the initialization Poisson summation of Section 17.6 exchanges the two, see Section 5 below.

**The two node invariants (17.9).** At every node, with F = N + V and Q the actual puncture length,

    (I1)  F − M − Q − z_0 ≥ c_node,        (I2)  4F − 3M − 6z_0 ≥ c_node,

with c_node = c_∗ − 7hη at depth h. The recursion preserves them with a loss of at most 7η per passage (17.51), lowers M by at least 2d − 8η ≥ d (17.52), and raises the energy exponent by at most 40η + τ + π (17.17), (17.65). Depth is bounded by D = ⌈(M_max + 2)/d⌉ + 1 (line 7417), so the total loss is D(40η + τ + π) < ε_c by the choices (17.66).

## 4. The recursive mechanism of Lemma 17.2 (CITED; exponent identities PROVED)

**Terminal case: the short completion (lines 7444–7530).** When the label length V and the cube-dyad centre ℓ_1 are both below d, Möbius inversion of the cube factor (17.10) completes the column and Lemma 14.3 (reflected energy) bounds the block. Its exponent E_ref must be below F. Three branches:

- row branch: E_ref ≤ M + z_a + (5/3)η ≤ F − c_node + (5/3)η, by (I1) (line 7497);
- column branch, u = z_a: E_ref ≤ F − 2c_node + 5d + (17/3)η + τ_ref, by (17.12) and (I1) (17.13);
- column branch, u ≠ z_a: E_ref ≤ F − M/4 − 3c_node/4 + (5/2)d + (19/6)η + τ_ref/2, by (17.12), z_a ≤ z_0 and (I2) (17.14).

Check of the last line. The retained dual bound gives E_ref ≤ O/2 + (T_d − S_0 − B_0)/2 + z_a + (7/6)η + τ_ref/2, and (17.12) gives T_d − S_0 − B_0 ≤ M − O + 2z_a − z_0 − c_node + 5d + 4η, so E_ref ≤ M/2 + (3/2)z_0 − c_node/2 + (5/2)d + O(η) + τ_ref/2. This is at most F − M/4 − 3c_node/4 + ... if and only if F ≥ (3M + 6z_0 + c_node)/4, which is (I2). PROVED. So (I2) exists only for the column branch with u = min{v, z_a, (v + z_a)/3} ≠ z_a of the reflected energy (14.13), where the dual length T_d = 2H + 2A_0 + 2z_a − N_∗ − N_0 − 3B_0 of (14.11) has the shape "twice the rows minus the columns".

**Nonterminal case: two masked Poisson summations (Lemma 17.5, (17.8)).** The block (A) is squared, the two columns are factored as n_i = A_i C u_i, and the first Poisson summation in the row k (scale Z^M, conductor u_1 u_2 R_1) produces an inverse-type polynomial (C) in the frequency y = h f² E; its principal term is O(Z^{M+ε}) (line 7693). After the first weighted Cauchy inequality (D) the old labels f, h are removed by the fibre bound (17.32) and the new row is y with scale Z^{H_use}, H_c = 2r − 2B − M + 4ℓ + 2V + δ − j (17.26). The second Poisson summation in y (conductor z_1 z_2, mask g′) returns canonical polynomials (17.55) in the new row k_new = d_k d_2 k″ and label f_new = J C d_2 v′, with centres

    N_c = r − A_i − B − t − g − v,  V_c = B + θ + v + j,  M_c = M − 4ℓ − 2A_i − 2t − 2g + 2θ − 2V + j   (17.37), (17.45).

**The contraction (17.48), PROVED by substitution.** With D_c = ℓ + A_i + t + g − θ + V ≥ ℓ + V − 2η,

    F_c − M_c = F − M + D_c,     4F_c − 3M_c = 4F − 3M + 2(A_i + t + g − θ + V) + j,     M − M_c = 2D_c + 2ℓ − j.

Hence both invariants are nondecreasing along the recursion up to the η-errors, and the row length drops by at least 2(ℓ + V) − 8η ≥ 2d − 8η because every nonterminal block has V + ℓ ≥ d (line 7572). The energy bookkeeping is the exact identity κ_i + λ_c + C_c + 2F_c = F (17.64): the two prefactors, the count of frozen triples (17.61) and twice the child energy reproduce F.

**Consequence for question (1).** The depth is already maximal (the recursion runs until the row cap M_max − hd is negative); no further iteration is possible or useful. The exponent is F at every node and m after the initialization, both the trivial sizes of their regimes. The admissible range cannot be enlarged by the recursion because (I1), (I2) are monotone along it: the binding instance is the root, where the short completion (V < d) may already be terminal, and there (I1) is exactly the row branch E_ref ≤ M + z_a < F of the reflected energy. ARGUED from the displayed inequalities; no inequality in the proof becomes slack with depth.

## 5. Initialization (Section 17.6) and where (H1), (H2) enter (PROVED identities)

The overlap j = (n, P) of the column with the slot primes is frozen (cost Z^G cancelled by Z^{−G}, line 8695), leaving a residual column of length D′ = r + z − 2G with cap z_0 = z − G. One masked Poisson summation at row scale Z^m gives the canonical centres (17.69), (17.74):

    M_c^init = 2D′ − m − 2P_1,   F_c^init = D′ − P_1,   Q_init ≤ P_1 + G + 3η,   P_1 = B − θ ≥ −2η.

Then (lines 9146–9147)

    F_c^init − M_c^init − (P_1 + G) − z_0 = m − r − 2z + 2G ≥ c_1,
    4F_c^init − 3M_c^init − 6z_0 = 3m − 2r − 8z + 10G + 2P_1 ≥ c_2 − 4η.

So (H1) is the root instance of (I1) and (H2) is the root instance of (I2); the margins (17.85) are c_1 − 9η − τ_init and c_2 − 22η − 3τ_init, and with c_∗ = min(c_1, c_2)/2 Lemma 17.2 applies. The energy identity κ_c^init + P_1 + 2F_c^init = m returns the exponent m with loss 11η + π_init + ε_c (17.86).

**What stops the inverse moment below r = m.** Condition (H1) with z = 0 says r < m: the polynomial must be shorter than the row range. This is the regime in which the diagonal Z^m is the large-sieve bound; for r > m the large sieve gives Z^r, and a bound Z^m there would be a power saving beyond the large sieve for Möbius sums twisted by sextic characters, which is the kind of statement the whole argument is trying to prove. In the language of the short preprint this is H ≥ D^{1+c} (17.87), and the recursion cannot relax it because (I1) never decreases. This is the obstacle the phase README calls "below the diagonal" for the alternative architecture (step 3 of the plan); the present reading confirms that it is the root condition of the reflected energy, not a depth or loss issue. ARGUED.

**Lemma 17.6 (lines 9249–9268), CITED.** With no slots, Z = H, m = 1, r = log_H D, (17.87) gives Σ_{q_u ≤ H} |M_u(D)|² ≪ H (HD)^ε for H ≥ D^{1+c}. The sixth-power transfer u ↦ u a^6 (17.90), injective on sixth-power-free u, with P = (H/U)^{1/6} choices of a, gives Σ_{q_u ≍ U} |M_u(D)|² ≪ (H/P)(UD)^ε = U^{1/6} H^{5/6}, hence e(r) = max{1, (1 + 5r)/6} for D = U^r. This is the exponent map of QRH_EXPONENT_MAP (θ = ½ max{1 + 5h/6, 2 − h/3} at h = 1 + ϑ) seen from the row side; the slope 5/6 is the only place where the sixth power enters the inverse side, and it is κ-free.

## 6. Lemma 18.1: the plain fourth moment with short prime factors (CITED)

**Objects (lines 9343–9366).** Rows k ∈ O, 0 < q_k ≪ Z^m; ψ_k(n) = τ(n)χ_n(k), where the moving residue-symbol support of τ has length ≤ q; effective width M = m + q. Two plain polynomials S_{ψ_k}(n_1; W_1), S_{ψ_k}(n_2; W_2) of lengths n_1, n_2 ≥ 0 and a product Q of prime polynomials of lengths z_i, z = Σ z_i, whose coefficients are fixed finite combinations of characters in a fixed finite group Θ. Put A = n_1 + n_2 + z. R_z is the set of rows whose inducing character is not in Θ (for z > 0) or is nonprincipal (z = 0).

**Statement (lines 9368–9404).** Let 3/4 ≤ κ ≤ 1. For every ε > 0 there is a slot mesh η > 0 such that, if all z_i ≤ η,

    Σ_{k∈R_z} |S_{ψ_k}(n_1) S_{ψ_k}(n_2) Q|² ≪ Z^{M+ε}

in either case: (1) z = 0, no restriction on n_1, n_2; (2) z > 0 and

    (18.3)  n_1 + n_2 + 6κz = A + (6κ − 1)z ≤ M,   with β∗ ≤ (1 + κ)/2 if κ < 1.

The mesh depends only on the bounded ranges and ε, "uniformly for κ ∈ [3/4, 1]". The application sets κ = 2β∗ − 1 (line 9405), so the zero-free hypothesis holds with equality.

**Shape.** Z^M = Z^{m+q} is the row count enlarged by the moving conductor length; again the diagonal. The absence of a length restriction at z = 0 is due to the functional equation: a plain factor longer than M/2 is reflected once (18.9), (18.10), so the padded core n_1^∗, n_2^∗ ≤ M/2 + ξ suffices. The inverse polynomial has no functional equation, which is why Lemma 17.1 has the restriction r < m and Lemma 18.1 does not.

## 7. The mechanism of Lemma 18.1 and the role of κ (CITED; the κ-ledger PROVED)

**Induction (lines 9620–9646).** On the width M in bands of length σ/4, zero-slot bands first; within a band the uncentered range A ≤ 5M/6 first, then the remainder by centering (subtraction of a comparison product with equal product of scales X_1X_2 = Y_1Y_2, (18.17)). Terminal at width M ≤ ρ by absolute counting: exponent at most A − q ≤ ρ + δ, plus κz ≤ M/6 ≤ ρ/6 for positive slots via (18.12). Depth D = 2 + ⌈2M_max/σ⌉; each nonterminal call lowers the width by at least σ (18.32) (declared width by at least σ/2 after the C_∗ξ corrections).

**Prime estimate (18.11)–(18.12): the only place where κ has analytic content.** For κ < 1, s_κ = (1 + κ)/2 and, under s_κ ≥ β∗, Lemma 4.9 gives L′/L(s_κ + e + it, ψ) ≪ log(2Q_ψ(3 + |t|)²) for every primitive nonprincipal ψ. Moving the Mellin contour of a smooth prime sum of scale P to ℜs = s_κ + e bounds it by P^{s_κ+e}; after central normalization by P^{1/2} the squared exponent is 2(s_κ − 1/2) = κ. Hence |Q_ω|² ≤ C Z^{κz+ε_1} p_j(W)^b (1 + |ω|)^h on R_z. For κ = 1 absolute counting gives the same with no hypothesis. Nothing here uses κ ≥ 3/4; it uses s_κ ≥ β∗ and s_κ > 1/2.

**The 6 in 6κ.** Rows whose child inducing character lies in Θ ("exceptional rows") have the sixth-power form (h′) = h_0 v^6 and number O(Z^{(m′−f)/6+ε}) (18.41). Bounding their plain products by volume leaves an excess A − 5M/6 before the common-support savings (18.42)–(18.44), which is why the uncentered range is A ≤ 5M/6. When the affine expression F_act = (A_act − M′_act + (6κ − 1)z_act)_+ is positive in a child, whole slots are removed by (18.12): removing length d lowers A + (6κ − 1)z by 6κd and costs κd (line 10529), so the removed length is d_z ≤ F_act/(6κ) + η and the cost κd_z ≤ F_act/6 + κη ≤ Δ_child + δ_fr,1/6 + θ_N/3 + η (18.39). The ratio cost/reduction = 1/6 is κ-independent; the region (18.3) is exactly the statement "the trivial cost κz of the slots is at most the one-sixth of the length budget M − A + z that the exceptional-row count supplies". Lowering κ enlarges the capacity linearly, z ≤ (M − A + z)/(6κ), and the only price is the zero-free hypothesis β∗ ≤ (1 + κ)/2. With κ = 2β∗ − 1 the hypothesis is self-consistent at every β∗ ∈ (1/2, 1]. ARGUED from the displayed ledgers.

**Complete list of the places where κ occurs in the proof** (every line of 9330–10987 of the extraction containing κ, "3/4" or "7/2" was listed):

| line | use | needs |
|---|---|---|
| 9368, 9401 | statement, mesh uniform on [3/4, 1] | compact range only |
| 9572–9617 | prime estimate (18.12), losses uniform in κ ∈ [3/4, 1] | s_κ ≥ β∗, bounded lengths |
| 9643 (18.13) | z ≤ M/(6κ) ≤ 2M/9, κz ≤ M/6 | second bound κ-free (from (18.3) and A ≥ z) |
| **9652** | **(6κ − 1)z ≤ M − A < M/6 and 6κ − 1 ≥ 7/2, hence z < M/21 < M/20; A − z > 2L** | **κ ≥ 3/4 (numerical)** |
| 9664–9672 (18.15)–(18.16) | A_comp ≤ 23M/30 + ξ, A_comp + (6κ − 1)z ≤ 14M/15 + ξ, margin M/15, ξ ≤ ρ/30 | consequence of 9652 |
| 10499–10541 (18.38)–(18.39) | affine region preserved, greedy slot removal | κ > 0 only |
| 10877 (18.51) | Lipschitz constant 5 from 0 ≤ 6κ − 1 ≤ 5 | 1/6 ≤ κ ≤ 1 |
| 10923, 10933 | choices uniform for κ ∈ [3/4, 1]; cost κz, contour 2ez | compact range only |

## 8. Question (2): is κ ≥ 3/4 structural? Answer: no; the structural threshold of this proof is κ > 1/2 (PROVED for the affected lines)

The comparison step (lines 9647–9675) treats inputs with A > 5M/6 by reflecting one factor or by subtracting a comparison with lengths L = M/4 and A − z − L. The reflected total length is A_comp ≤ 3M/2 − A + 2z + ξ (18.15), and the step calls the already proved uncentered assertion, which needs A_comp ≤ 5M/6 − (margin) and A_comp + (6κ − 1)z ≤ M − (margin).

General κ. From (18.3) and A > 5M/6, (6κ − 1)z ≤ M − A < M/6, so z < M/(6(6κ − 1)). Then

    A_comp < 3M/2 − 5M/6 + M/(3(6κ − 1)) + ξ = 2M/3 + M/(3(6κ − 1)) + ξ,
    5M/6 − A_comp > M/6 − M/(3(6κ − 1)) − ξ = (M/6)·(6κ − 3)/(6κ − 1) − ξ;

    A_comp + (6κ − 1)z < 5M/2 − 2A + 2z + ξ < 5M/6 + M/(3(6κ − 1)) + ξ,
    M − [A_comp + (6κ − 1)z] > (M/6)·(6κ − 3)/(6κ − 1) − ξ.

Both margins equal (M/6)(6κ − 3)/(6κ − 1), positive if and only if κ > 1/2. At κ = 3/4 this is M/14 (the text states M/15 after the looser z < M/20). The auxiliary claim A − z > 2L = M/2 needs z < M/3, true for κ > 1/4. The length L = M/4 cannot be lowered to buy margin: the centered saving (18.50) is maximal at v = L and equals A − M only for L ≥ M/4. So the architecture as written has the sharp threshold κ > 1/2, and the value 3/4 in the statement is simply the lower end of the range κ = 2β∗ − 1 ∈ (3/4, 5/6] forced by the Part II contradiction hypothesis β∗ > 7/8 of (12.1). The three uniformity sentences (9401, 9617, 10923) require only that κ range over a compact set with bounded lengths, since the contour cost 2ez and the Lipschitz constant 6κ − 1 ≤ 5 are uniform there. Classification: a parameter range chosen for the application, lowerable with a bounded loss of margin; not an inequality that fails below 3/4. PROVED for the lines listed; CONDITIONAL in that the remainder of the proof (pages 152–179) is not audited here and the text extraction may have dropped symbols in displayed formulas (the search covered all lines containing κ, 3/4, 7/2, M/20, M/21, 2M/9 and β∗).

## 9. Question (3): the extension needed for σ_0 = 4/5 (CONDITIONAL), and what it changes downstream (PROVED algebra, OPEN consequences)

**Needed statement.** With the Part II hypothesis replaced by β∗ > 4/5, set Δ = β∗ − 4/5 and κ = 2β∗ − 1 = 3/5 + 2Δ. Taking the published 7/8 bound as input (CITED, unaudited) gives β∗ ≤ 7/8 and κ ∈ (3/5, 3/4]; taking only the short preprint's 11/12 gives κ ∈ (3/5, 5/6]. Lemma 18.1 must therefore be restated for κ ∈ [3/5, 1], with the mesh uniform on the compact closure [3/5, 3/4] (or [3/5, 5/6]). This is "extension of Lemma 18.1" in the sense of rule 3 of the brief.

**Proof of the extension (routine).** Replace line 9652 by: 6κ − 1 ≥ 13/5, hence z < 5M/78 < M/15; then A − z > 5M/6 − M/15 = 23M/30 > M/2 = 2L. Replace (18.16) by

    A_comp ≤ 2M/3 + 10M/78 + ξ = 31M/39 + ξ,   5M/6 − 31M/39 = M/26,
    A_comp + (6κ − 1)z ≤ 5M/6 + 10M/78 + ξ = 25M/26 + ξ,   margin M/26,

and "choose ξ ≤ ρ/30" by "choose ξ ≤ ρ/52". Replace 2M/9 in (18.13) by 5M/18 (unused). Replace "[3/4, 1]" by "[3/5, 1]" in lines 9401, 9617, 10923. Everything else is κ-independent or needs only 1/6 ≤ κ ≤ 1. The zero-free hypothesis β∗ ≤ (1 + κ)/2 = 4/5 + Δ holds by equality. CONDITIONAL on the published proof being correct as written; the modification itself is PROVED.

Is the extension possibly false? Only if the unmodified parts of the proof silently used κ ≥ 3/4 through a symbol lost in the extraction. The two candidates are (18.13) and (18.16), both displayed above with their derivations; none of the other ledgers (18.23)–(18.25), (18.31)–(18.33), (18.38)–(18.44), (18.48)–(18.52) contains κ. The judgement "routine" is therefore well founded but is not an audit of Section 18.

**Downstream constants (PROVED as algebra, CONDITIONAL on the extension and on the proof of Proposition 19.2 carrying over).** Write κ_0 = 3/5 for the baseline (Δ = 0) and c = 1/(3κ_0) = 5/9 (the published case has κ_0 = 3/4, c = 4/9). The plain capacity at m is z_P(m) = (1 − 2m)/(6κ) and its baseline (1 − 2m)/(6κ_0) = c(1 − 2m)/2; the plain count exponent with q = xδ is 1 − 2δm − 2q z_P = 1 − δ[cx + (2 − 2cx)(t − r)] at m = t − r. Repeating the weighted average of (19.7) with the weights (2 − 2cx) and (1 − x):

    D_x = 3 − (1 + 2c)x = 3 − 19x/9   (published: 3 − 17x/9),
    P_x = (2 − 2cx)(1 − x) = (2 − 10x/9)(1 − x)   (published: (2 − 8x/9)(1 − x)),
    R_short(t) = 1 − δ + δP_x(3/2 − t)/D_x,

where the identity D_x − (3/2)P_x = 2x + cx − 3cx² holds for every c (check: 3 − x − 2cx − (3 − 3cx)(1 − x) = 2x + cx − 3cx²). The crossing point is r_∗(t) = ((2 − 2cx)t − (1 − c)x)/D_x, with r_∗(3/2) = 1 and t − r_∗(3/2) = 1/2 for every c; at c = 5/9, r_∗(1) = (2 − 14x/9)/(3 − 19x/9) ≥ 22/35 (x = 1/2) and t − r_∗(1) ≥ 1/3. The inverse capacity on the inverse side is at most (1 − 22/35)/2 = 13/70 (published 7/37), the (H2) margin is 2r − 1 ≥ 9/35, and the plain capacity at m ≥ 1/3 is at most 5/54 (published 2/27). The supply condition ℓ/d > 7/37 becomes ℓ/d > 13/70, slightly weaker. The loss (19.6) from using the dynamic κ instead of κ_0 becomes 2q(1 − 2m)[5/18 − 1/(18/5 + 12Δ)] ≤ (1/3)·12Δ/(18/5)² < Δ/3 (published: ≤ Δ/4), so the row exponent of Proposition 19.2 would read max{R_short(t), L(t)} + Δ/3 + ε with the new D_x, P_x; the constants 37/18 and 35/54 in Proposition 20.3 (line 11849) must be recomputed from D_x ≥ 3 − 19/18 = 35/18 and J = (α − δ)D_x + δP_x. These are inputs for the requirements memo, not results.

**What the extension cannot do.** The deficit found in QRH_HIGH_CANDIDATE_AUDIT, Section 3, is in the row-floor certificate of Section 20.2 (δ_0 = 1/50, R = 1, no witness), where rows are counted trivially and neither moment is invoked; the computed deficits 49/1500 at σ_0 = 13/15 and 149/1500 at 4/5 do not contain κ. Likewise the bound 13/15 for the chain of low estimates (QRH_FOUR_FIFTHS_ATTEMPT) is κ-free. Extending Lemma 18.1 removes the obstruction raised in Section 2 of that audit (the capacity need not be lowered to 2(1 − 2m)/9), and improves the short row count in the regime 1/50 < δ < α by the factor 5/4 in capacity, but leaves the floor and the low chain where they were. OPEN: whether the improved R_short(t), through the coefficient d of R in (20.4), changes the balance of Lemma 20.2 at some geometry; this is a computation for the requirements memo.

## 10. What this does and does not give

Does: a complete reading of the two moments with their exact ranges and the exponent of every step; the identification of (H1), (H2) as the root instances of the two invariants of the canonical recursion, with (I2) traced to the column branch of the reflected energy; the proof that the recursions are already at full depth and cannot enlarge their ranges; the proof that κ ≥ 3/4 is used in one numerical inequality and that the proof of Lemma 18.1 works verbatim for κ > 1/2 with margin (M/6)(6κ − 3)/(6κ − 1); the explicit text of the extension to κ ∈ [3/5, 1] and the recomputed constants D_x, P_x, r_∗, capacities and the Δ/3 loss.

Does not: audit the 7/8 manuscript (all its statements remain CITED); prove the extension beyond the lines it modifies (CONDITIONAL); give any progress on the row-floor deficit, which is where 4/5 fails in the published architecture, nor on the dual-regime wall r < m of the inverse moment, which is the obstacle to the alternative architecture of the phase plan. Status of 4/5: OPEN; at least one new estimate is still required, and it is not the extension of Lemma 18.1.
