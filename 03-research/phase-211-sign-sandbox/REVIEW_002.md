# Review 002: the four round-1 memos (A, B, C, D), line by line

Scope. Every claim labelled PROVED in ROUND_001_A.md, ROUND_001_B.md, ROUND_001_C.md and ROUND_001_D.md has been
checked against the definitions of STATEMENT_001.md and against Paper 46 (04-papers/46-row-d-sign-radial-intersection-form/main.tex:
thm:oneprofile 7773, prop:AM 7811, def:ext 9867, thm:ext-half 9913, lem:ext-cell 10270, thm:ext-cell, cor:ext-cellpos
10357, cor:ext-cfals 10365, thm:ext-lattice 10568, prop:nyq-LK 6182, thm:nyq-schur 6367). Verdicts: CONFIRMED (proof
checked, the key step named), REFUTED (counter-argument given), DOWNGRADE (to ARGUED or CONDITIONAL, with what is
missing). Line numbers refer to the memos. No equivalence of (★) with any statement outside STATEMENT_001 is used.

Summary of verdicts.

| Memo | Claim | Verdict |
|---|---|---|
| A | (0.1), (0.2) | CONFIRMED |
| A | Lemma 1 | CONFIRMED |
| A | Theorem 1(a): 𝒜(w) = a_{T'}(F_0∗W), B(F_0∗W) ≠ 0 | CONFIRMED, and sharper: B ≠ 0 for every w |
| A | Theorem 1(b): 𝒳_M = O(M^{−K}) | CONFIRMED (contour proof, not only numerics); two steps to be written out |
| A | Theorem 1(c): 𝒵_N = O(N^{−5/2+ε}) | CONFIRMED |
| A | Theorem 1 as an asymptotic statement Q_M = M𝒜 + O(M^{−3+ε}) | DOWNGRADE to ARGUED (ℛ_M); crude bound gives only O(M^{−7/3+ε}) |
| A | §3 "Theorem 1 holds verbatim for any comb" | DOWNGRADE to ARGUED (the vanishing of 𝒳 is Λ-specific) |
| B | Theorem 1.1, Corollary 1.2 | CONFIRMED, with one correction (σ₂ ∈ (−½,0) for non-smooth G) |
| B | Proposition 1.3 | CONFIRMED; the remark on a_P with P > N is REFUTED; "again admissible" is false as stated |
| B | Proposition 1.4 | CONFIRMED |
| B | Proposition 1.5 reduction | CONFIRMED (last step ARGUED, as labelled) |
| B | §1.6(i) "indefinite, PROVED by these two examples" | DOWNGRADE to ARGUED |
| B | §0 item 3 formula for the defect | REFUTED as written |
| B | Lemma 1.6 | CONFIRMED (it is cor:ext-cfals(i) extended to all w ≤ Λ) |
| B | Lemma 2.1 | CONFIRMED |
| B | Proposition 2.2 | CONFIRMED for the archimedean edge terms |
| B | Proposition 2.3 | DOWNGRADE to ARGUED (jet matching of φ_* at ±1/λ) |
| B | Proposition 2.4 | CONDITIONAL, as labelled; proof checked |
| C | Lemma 1 | CONFIRMED (sign typo in the twist, line 40) |
| C | Lemma 2 | CONFIRMED |
| C | Theorem 1 (L2′) (i)–(iii) | CONFIRMED |
| C | Explicit data of S; Proposition 1 | CONFIRMED |
| C | Proposition 2 | CONFIRMED |
| C | Proposition 3 | CONFIRMED (immediate) |
| C | Lemma 3 | CONFIRMED (wording of line 161 inverted) |
| C | The 11-dimensional block "PROVED as an equivalence" | DOWNGRADE: structure PROVED, membership of 𝒩 NUMERICAL |
| C | Proposition 4 on L²(I_T) | CONFIRMED for (a), (b) as stated; the stated consequence needs a strengthening of (a) (supplied below) |
| D | Proposition 1 | CONFIRMED in content; the proof as written is wrong for k ≥ 1 with the standard profile |
| D | Proposition 2 "never determinate" | REFUTED as a proof; what survives is weaker (below) |

---------------------------------------------------------------------------------------------------------------------
## 1. ROUND_001_A

**(0.1), lines 99–101. CONFIRMED.** χ′/χ(s) = log π − ½ψ((1−s)/2) − ½ψ(s/2); at s = ½+iτ the two digammas are conjugate,
so χ′/χ = −m(τ). With χ = e^{−2iθ}, d/dτ log χ(½+iτ) = i(χ′/χ) = −2iθ′, hence m = 2θ′.

**(0.2), lines 103–107. CONFIRMED.** v_n cos(τ log n) = 2Re(Λ(n)n^{−s}), so the subtracted comb is the truncation of
+2Re ζ′/ζ; on the line 1−s = s̄ and m|ζ|² = −2|ζ|²Re(ζ′/ζ) = −2Re(ζ′(s)ζ(1−s)). The sign correction is right.

**Lemma 1, lines 114–125. CONFIRMED.** Key step: w ≡ 1 on [0,e^{−L}] gives w̃(u) = −u^{−1}∫w′(x)x^u dx with w′ ∈ C_c^∞
supported in [e^{−L},1], so w̃ is meromorphic with the single pole u = 0 (residue 1) and decays faster than any power on
vertical lines (repeated integration by parts; the constants grow like e^{LK} on Re u = −K, harmless for fixed K).
Residues at u = 1−z and u = 0 are as stated; |ζ(½−K+it)| ≪ |t|^K by the functional equation.

**Theorem 1(a), lines 134–140. CONFIRMED, and sharper than stated.** Key step: W(t) = e^{t/2}w(e^t) has Ŵ(τ) = w̃(½+iτ);
F_0 is supported in [−T_0,T_0]; for t < −L−T_0, (F_0∗W)(t) = e^{t/2}B(F_0) = 0, and for t > T_0 it is 0; so F_0∗W is
supported in an interval of length L+2T_0 = 2T′ and the atoms log n ≥ 2T′ of s_N contribute nothing. Hence 𝒜(w) is the
window form at T′ of a translate of F_0∗W, independent of M once M > e^L.
On B: A(F_0∗W) = A(F_0)·∫w = 0. For B, use transforms: B(F) = F̂(i/2), F̂_0 has a simple zero at τ = i/2 (factor τ²+¼; the
factor |ĝ|⁴ = ĝ(z)²ĝ(−z)² does not vanish there since |b| > ½), and w̃(½+iz) has a simple pole at z = i/2 with
w̃(½+iz) ~ 1/(i(z−i/2)). Hence B(F_0∗W) = −i F̂_0′(i/2) ≠ 0, **for every w** in the family, not only "in general"
(line 139). So F_0∗W ∉ P_{T′} always.
Remark the memo missed. Combined with prop:AM(i) and any bound ℛ_M + 𝒵_N + 𝒳_M = o(M) (the crude bound of §1(d) below
suffices), (★) implies 𝒜(w) ≥ 0 for every w in the family: a necessary condition of (★) on vectors with A = 0, B ≠ 0,
outside P_{T′}. This is CONDITIONAL only on writing the o(M) bound; it is the one non-tautological output of the memo
and should be recorded. (Q3), lines 192–194, calls the transfer a restatement; it is a restatement on the family, but the
leading coefficient lives outside P_{T′}, which is not the same form.

**Theorem 1(b), lines 142–149: is 𝒳_M = O(M^{−K}) proved or only observed? It is proved by the contour argument;
CONFIRMED, with two steps that must be written out.**
Key step: the split of s_N ζ(z) at line 143 is an exact meromorphic identity (check: the two ζ′/ζ terms sum to
−ζ(χ′/χ)(z) = mζ on the line, and the two truncated sums give −ζΣ_{n<N}v_n cos). First bracket: on Re z = σ > 1 it equals
ζ(z)Σ_{n≥N}Λ(n)n^{−z}; the integrand is a sum of terms Φ(z)w̃(z)M^z(kn)^{−z}, |Φ| ≪ e^{2T_0(σ−½)}(1+|τ|)^{−4}, |w̃(σ+it)| ≤ 1/σ,
and kn ≥ N ≥ Me^{2T_0}, so dominated convergence as σ → ∞ gives 0; the integral is independent of σ (the double pole of ζ′
at z = 1 is cancelled by the double zero of Φ). Second bracket: moved to Re z = −c it is O_c(M^{−2c}e^{O(c)}).
Missing steps (not errors): (1) the integrand of the second bracket contains ζ(z)(ζ′/ζ)(1−z), which must be rewritten as
χ(z)ζ′(1−z) before the shift; otherwise the contour crosses the poles of (ζ′/ζ)(1−z) at 1−z = ρ. The memo does not say
this (line 147–148 mentions only z = 0). With the rewriting the only singular point is z = 0, where Φ's double zero
cancels the simple poles of ζ′(1−z)χ(z) and of w̃ — correct as stated. (2) The boundary case kn = N (when Me^{2T_0} is an
integer) is rescued by |w̃| ≤ 1/σ, not by "(Me^{2T_0}/n)^σ ≤ 1 with strict decay" (line 145–146). Neither affects the
result. The numerics of line 149 are only corroboration.

**Theorem 1(c), lines 151–157. CONFIRMED.** Key step: by (0.2) and evenness of Φ, 𝒵_N = −(1/π)∫Φζ(1−s)[ζ′(s)+ζ(s)Σ_{n<N}…];
the shift to 1 < σ < 7/2 crosses only s = 1, where Φ's double zero cancels; there ζ′ + ζΣ_{n<N} = −ζΣ_{n≥N}. Growth:
|Φ| ≪ e^{2T_0(σ−½)}|τ|^{−4}, |ζ(1−s)| ≪ |τ|^{σ−½}, so σ < 7/2; Σ_{n≥N}Λ(n)n^{−σ} ≍ N^{1−σ}.

**Theorem 1(d), lines 159–160, and the headline "Q_M = M𝒜 + O(M^{−K}) + 𝒵_N + ℛ_M" (lines 130–132). DOWNGRADE of the
asymptotic statement to ARGUED.** The identity is exact and (a)–(c) are proved; the size of ℛ_M is ARGUED (as the memo
says at line 160 and 248), so every sentence using "O(M^{−3+ε})" (lines 178–180, 192, 227) is ARGUED. Additional
objection: s_N is not O(log|τ|) uniformly in M; its comb part is bounded only by Σ_{n<N}v_n ≍ 4√N. With
|R_M| ≪ M^{−K}|τ|^K (K < 17/6 for integrability against |τ|^{−4}|ζ|) the crude bound for 2Re(ζR̄)Φs_N is O(M^{−7/3+ε}),
not O(M^{−3+ε}). The exponent −3 needs the oscillation of the comb against R, which is not written. The O(M^{−7/3}) bound
does suffice for the necessary condition noted under (a).

**(Q2), lines 188–190.** Correctly labelled ARGUED; the proposed regularity test is the right control.

**Falsifier test, lines 196–205. DOWNGRADE to ARGUED; the test was asserted, not carried out.** "Theorem 1 holds
verbatim for any comb b" (line 198) is false for part (b): the vanishing of 𝒳 uses ζ′ + ζΣ_{n<N}Λ(n)n^{−z} =
−ζΣ_{n≥N}Λ(n)n^{−z} on Re z > 1, i.e. ΣΛ(n)n^{−z} = −ζ′/ζ exactly. For a comb b the first bracket acquires
ζ(z)Σ_{n<N}(Λ−b)(n)n^{−z}, which contains small n and does not vanish as σ → ∞; 𝒳^b is a new term not estimated. Its
likely size is O(1) (for cΛ it is (1−c) times the comb part of 𝒳, which line 149 reports as ≈ 3·10^{−8} at M = 25 but
does not follow in M), so the conclusion "Q^b_M = M𝒜^b + O(1)" is plausible, but it is ARGUED. No numerical computation
of Q^b_M for any falsifier was made.

**NO-GO, lines 233–235.** The class "lattice-to-continuum transfer by Poisson summation / approximate functional
equation for smooth-cutoff Dirichlet polynomials" is too broad for what was shown. What was shown concerns the family
s_w = m^{−1/2}w(m/M) with w ≡ 1 near 0 and fixed L. The memo itself (line 255) says the sign must then be sought on
non-smooth vectors, which the same class (Poisson/AFE) could treat. Correct name: "the smooth-cutoff family
m^{−1/2}w(m/M), leading order in M". The falsifier part of the NO-GO is ARGUED (above).

---------------------------------------------------------------------------------------------------------------------
## 2. ROUND_001_B

**Theorem 1.1, lines 103–130: is the proof complete (poles at s = 0, 1; absolute convergence; interchange)? CONFIRMED,
with one correction.**
Checked in order. (1) Φ̃_f = ζ·Mf on Re s > −1 (line 96): Φ_f = O(e^{3x/2}) at −∞ by Poisson and 𝓕f = O(ξ^{−2}); Mf
holomorphic on Re s > −2 because f even, C², f(0) = 0 gives f = O(u²); Mf(1) = ½𝓕f(0) = 0 cancels the pole. (2) Parseval in
Mellin form (line 106) matches the conventions F̃(½+iτ) = F̂(τ), G̃(½−iτ) = conj Ĝ(τ). (3) Comb sums: Σ_nΛ(n)n^{−σ₁} and
Σ_nΛ(n)n^{σ₂−1} converge, and ∫|F̃||G̃| < ∞ on the lines (F̃ = ζMf = O(|t|^{max(0,½−σ)−1+ε}), G̃ rapidly decreasing), so
Fubini applies; line 113 says this tersely but correctly. (4) Singularities: −(ζ′/ζ)·ζ = −ζ′ (zeros of ζ cancel);
(ζ′/ζ)(1−s)ζ(s) = χ(s)ζ′(1−s), holomorphic on [σ₂,½] except s = 0 (χ's first pole is at s = 1, outside the region swept).
(5) Residue at s = 1: −ζ′ = (s−1)^{−2} + O(1), Mf(1) = 0, so residue Mf′(1)G̃(0) = A(F)B(G); moving left adds it. Residue at
s = 0: χ(s) = s/2 + O(s²) (from ζ(0) = −½ and ζ(1−s) = −1/s + O(1)), ζ′(1−s) = −s^{−2} + O(1), so −χζ′(1−s) = 1/(2s) + O(1),
residue ½Mf(0)A(G) = −B(F)A(G); moving right subtracts it. (6) On the line, ζ′(s) + χ(s)ζ′(1−s) = (χ′/χ)ζ = −mζ. The
bookkeeping at line 126 then gives 0. Key step: (6) together with the two residues, which reproduce exactly the pole
term A(F)B(G) + B(F)A(G) of 𝒲.
Correction (line 112 and 128–130). For G = Φ_{f′} or Ψ_{f′} (G̃ only O(1/|t|)), the second integrand on Re s = σ₂ is
≍ |t|^{½−σ₂}·|t|^{−1}·|t|^{−1}, integrable only for σ₂ > −½. The memo writes σ₂ ∈ (−1,0) and then "A < 1" without saying
this forces σ₂ ∈ (−½,0). With that choice the argument is complete. The memo's proof removes the dependence of
thm:ext-half on the citation of Lemmas 4.2–4.4 of the cited preprint; this is worth recording.

**Corollary 1.2, lines 132–135. CONFIRMED.** Key step: Theorem 1.1 with G = Φ_f and G = Ψ_f; W_T(Ef) = 𝒲[Ef] since Ef is
supported in Ī_T (this matches def:ext, line 9890 of the paper: "for Ψ supported in I_T this is W_T(Ψ)").

**Proposition 1.3, lines 141–151. CONFIRMED (identity); two side remarks are wrong.** Key step: 𝒲^w = 𝒜𝒫 − 𝒫_w =
𝒲 + 𝒫_{Λ−w}, with 𝒫_u entering 𝒲 with a minus sign (consistent with Prop 1.4's 𝒜𝒫 = 𝒲 + 𝒫_Λ).
(i) Line 149: "f_P … again an admissible function" is false as stated. f(d·) has jumps of f′ (and f″) at ±λ/d, which lie
inside [−λ,λ], so f_P is not C² on [−λ,λ]. Theorem 1.1 still applies (it uses only continuity, f = O(u²) at 0,
Mf = O(1/|t|), 𝓕f = O(ξ^{−2}), all true for continuous piecewise-C² f), so the instance survives once the hypothesis is
weakened. (ii) Line 150, "(When P > N, Ef_P = Ef since f(d·) for d ≥ P > N is a gauge element.)": REFUTED. For P > N the
divisors d include every prime p < N, and f(p·) is not in the gauge. On I_T, Φ_{f_P}(x) = e^{x/2}Σ_{(n,∏_{p<P}p)=1}f(ne^x)
keeps only n < N < P coprime to all p < P, i.e. n = 1, so Ef_P = e^{x/2}f(e^x)|_{I_T} ≠ Ef in general.

**Proposition 1.4, lines 153–159. CONFIRMED.** Key step: radicality of 𝒜𝒫 against C_c^∞ is the distributional equation
m(D)F = −A(F)e^{−x/2} − B(F)e^{x/2}. The left side is tempered (F ∈ L², m of logarithmic growth), and e^{±x/2} grow on
opposite sides, so A = B = 0; then mF̂ = 0 and m vanishes only at ±t₀, so F̂ = 0 a.e. The comb pairings against C_c^∞
converge because F = O(e^{3x/2}) at −∞. Lines 160–166 are correctly labelled ARGUED.

**Proposition 1.5, lines 168–177.** Reduction CONFIRMED (Ψ_{f+tφ} = Ψ_f + tΦ_φ; 𝒲(·,Φ_φ) = 0; 𝒫_Λ(Φ_φ,·) = 𝒜𝒫(Φ_φ,·)).
Last step ARGUED, as labelled.

**§1.6(i), lines 180–182, "Indefinite. PROVED (by these two examples)." DOWNGRADE to ARGUED.** Showing that 𝒫_Λ[Ef] and
𝒫_Λ[Ψ_f] each take both signs does not show that their difference does: one needs admissible f with
𝒫_Λ[Ef] − 𝒫_Λ[Ψ_f] > 0 and another with < 0. Neither is exhibited.
Related error, §0 item 3, line 22: the defect is written as "−(c−1)(arch+pole)[Ef] + (c−1)(same)[Ψ_f]". REFUTED as
written. Theorem 1.1 gives 𝒫_Λ(Φ_f,·) = 𝒜𝒫(Φ_f,·) only on the radical vector Φ_f, not on Ef or Ψ_f separately; 𝒫_Λ[Ef] ≠
𝒜𝒫[Ef] in general. The correct defect is that of Proposition 1.3(a), (1−c)(𝒫_Λ[Ef] − 𝒫_Λ[Ψ_f]).

**Lemma 1.6, lines 184–189: does the monotonicity cover the key cancellation of cor:ext-cfals? CONFIRMED for what it
claims; it is not new.** Key step: lem:ext-cell(ii) (paper line 10276ff.) gives the comb contribution as
−2‖ϱ‖²Σ_{n≤J}(w∗1)(n)/n for any comb w ≥ 0. All other terms of 𝔔 in lem:ext-cell(iii) are comb-free, so 𝔔^w ≥ 𝔔 whenever
w∗1 ≤ Λ∗1 = log; (a_P∗1)(n) = log n − Σ_{p<P}v_p(n)log p ✓. Hence the lower bound of cor:ext-cellpos holds for every w ≤ Λ.
This is cor:ext-cfals(i) of the paper, which already states it for c′ ≤ 1 and adds "it says nothing about 𝔔^{c′} on other
data". What the lemma does not cover: the key cancellation in the proof of thm:ext-cell (H_J log(tφ′/2π) − 2H_1(J)) is an
equality that makes the frequency threshold logarithmic, and cor:ext-cfals(iii) shows that Λ is exactly the upper
boundary of the cone of combs for which positivity holds at that threshold. Monotonicity explains why the cancellation
is blind below Λ. It does not explain why the boundary sits at Λ, which comes from Λ∗1 = log. The NO-GO at lines
190–194 is correct as a statement that cell positivity cannot be the whole sign step: since c < 1 and a_P falsify (★)
(STATEMENT §4(i)), the step must fail for them. It does not exclude using cell positivity as one ingredient. Class
correctly named; falsifier test carried out analytically (by the lemma itself).

**Lemma 2.1, lines 218–232. CONFIRMED.** Key step (b): with h(t) = f(t/λ), 𝓕h(ξ) = λ𝓕f(λξ), and Poisson summation
(h continuous, piecewise C², compact, so Σ|𝓕h(n)| < ∞) gives Σ_{n≥1}ϱ(n) = Σ_{k≥1}h(k) = Σ_{k<N}h(k) = λ^{½}Ef(−T)
(h(0) = 𝓕h(0) = h(N) = 0). The convention must count n = 1 (ϱ(1) = λ𝓕f(λ), the endpoint of the open interval (λ,∞)
defining r_f); state it.

**Proposition 2.2, lines 234–243. CONFIRMED for the archimedean edge terms.** Key step: ½∫_0^∞‖Ψ − Ψ(·−u)‖²K du split
over (0,∞)² and the two cross regions gives the killing term ∫|Ψ|²κ, κ(y) = ½∫_y^∞K (cf. rem:ext-killing (i) of the
paper). The residue of phase 202 (BUILD_R2_001 line 80; Lemma M "up to layer edges") arises in archimedean pairings of
dilated tails, so the proposition covers the residue as it was defined, and the NO-GO "void" stands for that residue.
Caveat for the index: in a per-layer decomposition the comb pairings ∫_0^∞u_n(y)u_{n′}(y+log q)dy also depend on the cut
at y = 0 and carry v_q. They are not "edge terms" of the residue but are not comb-free; line 237 ("in any
decomposition … all of them involve K and C₀ only") should be limited to the archimedean part.

**Proposition 2.3, lines 245–260. DOWNGRADE to ARGUED.** By thm:ext-lattice the jets that φ₀ must match at ±1/λ are the jets
of Σ_{m<N}μ(m)𝗉(m·) there, and these depend on g through g(log(m/λ)) and its derivatives. Line 247 fixes φ_* "once and
for all … with the C²-matching data of 𝗉". Then φ₀ + I(g)φ_* lies in 𝒢_T only if the required jet of φ₀ equals −I(g)
times the jet of φ_*, i.e. only if the jet data are proportional to the scalar I(g). This is not shown and is false in
general. The repair is φ₀ = −I(g)φ_1 + φ_{J,g} + φ_𝒢, with φ_{J,g} carrying the g-dependent jets, ∫φ_{J,g} = 0 and
φ_{J,g}(0) = 0. φ_{J,g} is not a gauge element (its jets at ±1/λ are nonzero), so it is a second coupling. "The coupling
is a forced scalar" is therefore not proved.

**Proposition 2.4, lines 262–288. CONDITIONAL, proof checked.** Key step: double orthogonality gives
leak(f) = Σ|a_k|²(1−χ_k) for f = Σa_kψ_k on [−λ,λ] with c = 2πN; ‖E‖ ≤ 2√N (lem:ext-mob). The exponent arithmetic in (i)
is right: 2N^{½}(8·10⁹T N^{A₀−7.72}/(κε′))^{½} ∝ N^{(A₀−6.72)/2}. (ii) is CONDITIONAL also on a NUMERICAL law, as labelled.

**NO-GO, lines 302–307.** (1) "Objects whose Λ-dependence is the radical of 𝒲" is a class name that goes beyond what was
shown. What was shown: the defect for the falsifiers is an explicit bilinear expression (Prop 1.3), its sign is not
determined (ARGUED, §1.6(i)), and the one sign-definite piece (cells) is monotone (Lemma 1.6). That is a NO-GO for these
two readings, not for the class. (2) Layer edges: correct for the residue as defined (above). (3) φ₀ coupling: ARGUED
(Prop 2.3). Falsifier test: analytic for Lemma 1.6 and Prop 2.2; no computation was carried out, and none was needed for
those two.

---------------------------------------------------------------------------------------------------------------------
## 3. ROUND_001_C

**Lemma 1, lines 35–46. CONFIRMED.** Key step: for F ⊂ I_T and 0 ≤ u ≤ 2T, the wrapped part of F(·−u) lands in
(−2T,−3T+u) ⊂ (−2T,−T], so ⟨F,τ_uF⟩ = c_F(u). Parseval in {ε^α_k} gives the sampling formula on |u| ≤ 2T. At u = 2T this
gives the alternating identity. The Lévy form then gives the symbol m + r_T − comb exactly as in thm:nyq (the term
ε_T c_F(0) from u > 2T produces r_T). Typo, line 40: for ε^α_k to be an eigenvector the twist must be e^{+iα4Tj}, not
e^{−iα4Tj} (with the stated sign one gets e^{−2iα4Tj}).

**Lemma 2, lines 48–54. CONFIRMED.** Key step: ⟨e^α_j,e′^α_l⟩ = ⟨e_j,e′_l⟩ (the phase cancels), and
(1/2T)Σ_{even}|F̂(ω_k+α)|² = (1/2T)Σ_{odd}|F̂(ω_k+α)|² = ‖F‖² by Parseval, so the gauge adds ±½c‖F‖² to the two halves.
The two-sector formula is Lemma 1 with the sum split; H is not needed for it. As an operator statement: A = ½(D_e +
HᵀD_oH) is invariant under D_e ↦ D_e + c, D_o ↦ D_o − c because HᵀH = I (H real orthogonal, being a change of orthonormal
basis). Only the block 𝒩 depends on (α,c), not the form.

**Theorem 1 (L2′), lines 62–76: correct for η ↓ 0? CONFIRMED.**
- Coercivity constant: c_* = ½(min_{j∉𝒩_e}s_{2j} + min_{l∉𝒩_o}s_{2l+1}). Both minima exist and are ≥ η_0 > 0 because
  s_k → +∞ on every shifted mesh (prop:nyq-LK(iii) bounds L_T(τ) for every real τ). c_* does not tend to 0 as η ↓ 0: for
  η ≤ η_0 the block {s_k < η} is the fixed set 𝒩 = {s_k ≤ 0}.
- Zero samples. The definition 𝒩 = {s_k ≤ 0} puts samples equal to 0 in the block. This is what makes the limit η ↓ 0
  harmless. With the literal η = 0 block {s_k < 0}, a zero sample would sit in the complement and coercivity would be
  lost (c_* = 0 if that sector has no other small sample). The memo's convention is the correct one. The counts in the
  table (line 131, "samples with s_T < 0") use strict inequality; at the gauge-optimised points the optimiser could sit
  at an exact zero. This does not matter for Proposition 2(c), which selects α with no vanishing sample, but the table
  entries d should be read as counts of s ≤ 0.
- (ii) The proof of thm:nyq-schur(ii) (paper lines 6385–6405) uses only Lemma 2, Parseval, lem:compact, the growth of
  the samples, and that e^α_j, e′^α_l, e^{±t/2}1_{I_T} ∈ 𝒟_T (transforms O(1/|τ|) on the mesh). All of these hold for the
  shifted and gauged data. The decomposition P_T ∩ 𝒟_T = N′ ⊕ (𝒞 ∩ 𝒟_T) uses N′ = orthogonal projection of 𝒩_η into
  P_T, which is in 𝒟_T. The "some η ⟺ every η" statement is immediate, since each is equivalent to λ_A(T) ≥ 0.
- (iii) A negative subspace V ⊂ 𝒟_T meets 𝒩_η^⊥ only in 0 by (i), so dim V ≤ dim 𝒩_η ≤ |𝒩|. Correct.
- Shift and gauge invariance: confirmed under Lemma 2.

**Explicit data of S, lines 78–85. CONFIRMED.** Key step: ⟨e^{±t/2},e^α_j⟩ = (2T)^{−½}·2sinh((±½+iπj/T+iα)T)/(±½+iπj/T+iα).
At α = 0, sinh(±T/2 + iπj) = ±(−1)^j sinh(T/2), which gives the stated formula. Σ_l s_{2l+1}|(Hc)_l|² converges
(Σ log l/l²).

**Correction about the entries of S and Proposition 1, lines 87–98. CONFIRMED.** (a) is thm:nyq-schur(iii) transported
by Lemma 2. (b): infima over increasing sets decrease; density in the form norm with continuity of a_T gives
convergence; the error identity a_T(x+y) = S(x) + a_T(y−y_*) is the one in the proof of thm:nyq-schur(ii). Line 101's bound
a_T(y_*) ≤ ‖P_𝒞g_x‖²/c_* follows from a_T(y_*) = −⟨y_*,P_𝒞g_x⟩ and a_T(y_*) ≥ c_*‖y_*‖².

**Proposition 2, lines 112–120. CONFIRMED.** Key step for (c): the shifted meshes ω_k + α, α ∈ [0,π/2T), tile ℝ, so by
Tonelli the average count is (2T/π)|{s_T < 0}|. A count is ≤ its average on a set of positive measure. s_T is
real-analytic in |Im τ| < ½ (K = O(e^{−u/2})) and nonconstant, so its zeros are countable and a.e. α has no vanishing
sample. (a), (b) are as stated; m_lo is increasing on τ > 0.

**Proposition 3, lines 126–129. CONFIRMED** (prop:nyq-LK(iv) and Theorem 1(iii)); immediate.

**Lemma 3, lines 158–164. CONFIRMED.** Trigonometry: ω_k log n = πk(1−δ). Wording at line 161 is inverted: the
perturbation exceeds θ only for |k| ≥ (2θ/v_n)^{½}/(πδ) (the memo says "by at most θ only at").

**The block at ½log5 + ε, lines 170–188, and "the exact finite inequality … PROVED as an equivalence", lines 177–182.
DOWNGRADE.** The structure (λ_A ≥ 0 ⟺ Schur complement on N′ ⪰ 0) is Theorem 1 and is PROVED for any (α,c). The
particular statements "𝒩 = {0,±3,±5,±9,±14,±23}", "|𝒩| = 11", "c_* ≥ 8.8·10^{−5}" rest on double-precision evaluation of
r_T and of the samples, with the gauge quoted as "c ≈ 1.21" and ε unspecified between 10^{−6} and 10^{−4}. They are
NUMERICAL. The displayed equivalence with the specific 11-dimensional space is CONDITIONAL on that numerical
identification. Using it as a finite target requires a certified (interval) evaluation of the samples near the
threshold, in particular of the smallest positive gauged sample 8.8·10^{−5} and of k = 23 (−0.053). The arithmetic
reading (k = 158 ↔ 3^{34} ≈ 2^{54}) was checked: 158·log2/(2log5) = 34.02, 158·log3/(2log5) = 53.93.

**Proposition 4, lines 190–201: proved on L²(I_T)? CONFIRMED for (a), (b) as stated; the stated consequence needs more,
which is easily supplied.**
(a) Key step: off-block mass ≤ C/M for near-minimisers, then compactness of the unit sphere of the finite-dimensional
E and E ∩ E′ = {0}. Even and odd powers of z = e^{−iπt/2T} cannot agree on an arc; the shift multiplies both by
e^{−iαt}. (b) is Lemma 2 at F = e_j with Σ_l h²_{l−j} = 1.
Gap: (a) as stated gives "bottom > −δ for M large", not "bottom ≥ 0". To conclude "the sign is not a function of the block
samples" (line 195), one needs one completion with nonnegative form and one with a negative form. The same compactness
gives dist²(F,E) + dist²(F,E′) ≥ κ‖F‖² for some κ > 0, hence a ≥ (½Mκ − C)‖F‖² > 0 for M large. With this strengthening the
consequence holds.
On P_T: (a) is trivial there (the infimum over a subspace is not smaller), so only (b) needs the two Tate constraints. The
label "on P_T ARGUED" (line 190) is honest, but the missing part is only (b).
Scope: the result is about abstract sequences. The actual samples come from one symbol s_T and are not free off the
block. The memo states this correctly ("as a statement about sequences", line 201).

**Falsifier test, lines 204–215. Carried out (NUMERICAL) for the block dimension.** One wording error. Line 213 says "the
dimension is not monotone in any sign-relevant direction (deleting primes lowers it, as does shrinking Λ)". The data
(1.5Λ: 49; Λ: 11; 0.7Λ: 9; a_3: 7) show the opposite: the dimension is monotone in the comb, increasing upward and
decreasing downward. That is why it cannot separate Λ from the downward falsifiers, which also violate (★). The
conclusion (no sign information in the dimension) is right; the stated reason should be "monotone in the comb,
hence blind below Λ".

**Result, lines 232–238.** PIVOT, not NO-GO, is the appropriate label: Theorem 1 is an exact reformulation (an internal
move, STATEMENT §5), and no sign step was claimed.

---------------------------------------------------------------------------------------------------------------------
## 4. ROUND_001_D

**Proposition 1, lines 268–272: does it need F_0 smoother than the standard profile? Yes, for the proof as written;
the statement survives. CONFIRMED in content, proof to be replaced.**
For the profile of STATEMENT §2, G_0 = c_g∗c_g is C² with jumps in the third derivative, so F_0 = (¼−∂²)G_0 is continuous
with jumps of F_0′. Then ∂²F_0 contains Dirac masses and is not in L²(I_{T_0}), let alone in P_{T_0} ∩ 𝒟_{T_0}. The step
"∂^{2k}F_0 lies in P_{T_0}" (line 270) is false for k ≥ 1 with this profile. Consistently, ∫mF̂_0²τ^{2k} < ∞ only for k ≤ 1
(F̂_0² ≍ τ^{−4}, as line 282 itself says). Correct proof, valid for any profile: the comb part of B(d) is
−½Σ_nv_n[c_0(log n − d) + c_0(log n + d)], which vanishes identically for |d| < log 2 − 2T_0. Hence B coincides near 0 with
d ↦ (1/2π)∫mF̂_0²cos(τd)dτ, all its existing derivatives at 0 are the archimedean ones, and for a positive μ with μ̂ = B
the existence of B^{(2k)}(0) gives ∫τ^{2k}dμ = (−1)^kB^{(2k)}(0). Two remarks. (1) μ exists as a positive measure only
under (★) (Bochner), so Proposition 1 is an implication from (★), or else a statement about the distribution μ.
(2) For the standard profile the proposition concerns two numbers (orders 0 and 2).

**Proposition 2, lines 274–284, "never determinate, for any admissible profile". REFUTED as a proof.**
(1) The first argument (lines 275–281) assumes determinacy and derives: if B^c is positive definite then B^c = B,
contradiction. The memo then concedes, "if B^c is not positive definite, nothing follows about μ". So no contradiction
with determinacy is reached. Since the competitors cΛ (c ≠ 1) and a_P are exactly the combs for which positive
definiteness is expected to fail (STATEMENT §4(i)), the argument proves nothing about μ for Λ.
(2) Standard profile: only moments of order ≤ 2 exist, so the Hamburger problem is not posed. "Indeterminate" holds
trivially (infinitely many positive measures share three moments), and this part is correct.
(3) C_c^∞ profiles: the claim "m_{2k} grows faster than (2k)!^{1/α} for every α < 1" (line 283) is not justified in that
generality. A correct route to the conclusion: c_0 is compactly supported and smooth, and its derivatives are bounded
by the moments of F̂_0² (times log factors from m). If Σm_{2k}^{−1/2k} = ∞, the Denjoy–Carleman theorem would make c_0
quasi-analytic, contradicting compact support. So Carleman's series converges. This shows only that Carleman's
sufficient condition never applies. Convergence of the Carleman series does not imply indeterminacy.
(4) Such profiles are not the profile of thm:oneprofile. Its (⟸) direction (paper Step 2–3) uses analyticity of 1/ĝ in
the strip |Im z| < |b|, with |b| > ½. For another profile the equivalence "(★) ⟺ B positive definite" is not available
from the paper, so "for any admissible profile" needs the class of admissible profiles to be defined.
What survives, and is the real content: **NO-GO (PROVED, given the falsifiers of STATEMENT §4(i), which are CITED from
Paper 46).** The germ of B at 0, hence every moment of μ, is the same for Λ, cΛ and a_P (Proposition 1, corrected
proof). The proof of thm:oneprofile is comb-generic (Step 3 needs only Σw(n)n^{−½−β} < ∞), so B^c is positive definite
iff (★) holds for cΛ, which fails for c ≠ 1. Therefore no criterion that uses only the moments of μ (equivalently, the
germ of B at d = 0) can decide positive definiteness of B. This one-line argument replaces Proposition 2 and gives the
NO-GO directly.

**Consequence, lines 287–288.** "Positivity of μ is equivalent (thm:KEP1–KEP3) to the indeterminacy of the Kreĭn
extension problem" is an internal reformulation (STATEMENT §5); admissible. "REF-D" is not one of the phase labels; use
NO-GO.

**NO-GO, line 291.** The class should be "criteria using only the moments of the representing measure (the germ of B at
0)", not "moment determinacy (Hamburger/Stieltjes/Carleman)". Determinacy was not shown to fail in general, and the
reason the route dies is comb-blindness of the moments, not indeterminacy. Falsifier test: carried out analytically
via the comb-independence of the germ; correct once Proposition 1's proof is replaced.

---------------------------------------------------------------------------------------------------------------------
## 5. All NO-GO labels in round 1

| Memo, lines | NO-GO | Class correctly named? | Falsifier test carried out? |
|---|---|---|---|
| A 233–235 (also 227–229) | lattice-to-continuum transfer, Poisson/AFE | Too broad; should be "smooth-cutoff family m^{−1/2}w(m/M), leading order in M" | Asserted, not carried out; the step "Theorem 1 holds verbatim for any comb" fails for 𝒳; ARGUED |
| B 190–194 | key cancellation of cor:ext-cfals as sign source | Yes ("statements on cones with sign-definite comb pairing"); excludes it as the whole sign step, not as an ingredient | Yes, analytically (Lemma 1.6) |
| B 207–213 | fused reading as a clause-(5) object | Classification by reading; ARGUED, as labelled | Not applicable |
| B 243 | layer-edge residue void | Yes, for the residue as defined in phase 202 (archimedean pairings); line 237 overstates "any decomposition" | Yes, trivially (comb-free) |
| B 302–307 | "objects whose Λ-dependence is the radical of 𝒲" | Too broad; what was shown is a NO-GO for two specific readings | Partly: §1.6(i) indefiniteness ARGUED |
| C (none; PIVOT) | Proposition 4 acts as "no criterion on block samples alone" | Correct on L²(I_T) after the strengthening of (a); on P_T only (b) is missing | Yes, NUMERICAL table, with the monotonicity wording corrected |
| D 288, 291 | moment determinacy | Misnamed; should be "criteria using only the moments of μ / germ of B at 0" | Yes, analytically, once Proposition 1's proof is corrected; Proposition 2's own argument does not carry it |

## 6. Items to carry into the index and the ledger

1. A: Theorem 1(a)–(c) PROVED; ℛ_M = O(M^{−3+ε}) ARGUED (crude O(M^{−7/3+ε})); falsifier robustness ARGUED. New necessary
   condition: (★) ⟹ 𝒜(w) = a_{T′}(F_0∗W) ≥ 0 for every w of the family, with B(F_0∗W) = −iF̂_0′(i/2) ≠ 0 always.
2. B: Theorem 1.1 PROVED without the citation (σ₂ ∈ (−½,0) for non-smooth G). Proposition 1.3's remark on P > N is
   wrong. §1.6(i) is ARGUED. §0 item 3's defect formula is wrong. Proposition 2.3 is ARGUED (jet matching).
3. C: Theorem 1 (L2′), Lemmas 1–3 and Propositions 1–3 PROVED. The 11-dimensional block is NUMERICAL until certified.
   Proposition 4 on L² holds with the strengthened (a). The dimension is monotone in the comb.
4. D: Proposition 1 holds with the germ argument. Proposition 2 as written is withdrawn. The NO-GO is "moments of μ are
   comb-blind", PROVED given the CITED falsifiers.
