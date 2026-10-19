# AUDIT_200_SPEC_002: audit of SPEC_SIGN_OBJECT_002 (phase 200, round 2)

Checked against Paper 47
(thm:ext-half l.9647, rem:ext-killing l.9669, prop:ext-gauge l.9680, prop:ext-grouped l.10325) and the index (INV_H_001, INV_J_001,
V2, phase 193 (S⁺)). Control script: python/sympy with exact fractions (NUMERICAL, reproducible in 20 lines).

**Central finding.** The spec's own Lemma SQ.0 (full Ramanujan combs are radical), applied consistently,
implies that **every mollified outer object is −g modulo the radical, at any level Y**. This makes Q1
tautological (y^T𝔅y = 𝒲[g]) and degenerates Q2 (the matrix 𝔊 is constant; the difference of mollifiers is radical, 𝒲 = 0). The
spec identified the risk in Q2 in the wrong direction: radicality at level μ/2 does not "fail"; it holds and kills the ladder.

---

## 1. Lemma T.1

**Verified steps.**
- Step 2: 𝓛g entire (compact support); D_μ(½+s)𝓛g(s) has at most the pole at s = ½ with residue M_μ(1)𝓛g(½) = M_μ(1)B(g),
  B = A by parity. Correct. The continuation by uniqueness is correct *if* 𝓛Ψ̌_c is holomorphic on Re s > −3/2, which requires the
  bound e^{−3x/2} for Ψ̌_c; that bound is given by thm:ext-half for Ψ_f (CITED Guo L4.2–4.4) and Φ̌_{φ₀} has support on (−∞, −T] reflected,
  so the subtraction preserves the bound for x > T. OK.
- Step 3: A(Ψ̌_c) = 𝓛Ψ̌_c(−½) = D_μ(0)A(g) = 0. Correct. B(Ψ̌_c) = 𝓛Ψ̌_c(½) is finite (value of the continuation), so the
  polar product vanishes. OK.
- Step 4 (absolute convergence of ∫|ĝ|²|D_μ|²m): requires enough decay of ĝ to dominate |ζ(½+it)|²log|t| ≪ |t|^{1/3+ε}.
  For g in the core (C², vanishing to second order at ±a), |ĝ(t)| ≪ |t|^{−2}... actually ≪ |t|^{−3}, which suffices. **Implicit
  regularity hypothesis: must be stated** (g ∈ H^1 already suffices). The sum over n, |c_Ψ̌(log n)| ≤ Cn^{−3/2}, is not proved in the spec;
  it follows from thm:ext-half (the prime series of 𝒲[Ψ̌] converges absolutely there). Acceptable as CITED.

**Hypothesis A(g) = 0.** This is the right one to kill the pole and the 2AB term. For A ≠ 0 the spec delegates to GG.0 (κψ̌); not audited here.

**Gauge (radical).** Step 1 uses W_T(g) = 𝒲[Ψ̌] = 𝒲[Ψ̌_c] because Φ̌_{φ₀} is radical (prop:ext-gauge). Correct, but note: the
same logic, carried over to SQ.0, gives Ψ̌_c ≡ −g modulo radical (§3, §5). T.1 is then the Fourier formula for 𝒲[g] written with the
factor |D_μ|²; it adds no new information about the sign.

**Novelty.** thm:ext-half already gives 𝒲[Ψ̌] = (1/2π)∫m|𝓕Ψ̌|² − (comb) + 2AB. The only new thing is the factorization 𝓕Ψ̌_c = ĝ·D_μ(½+it).
Verdict: **PROVED (given Guo, CITED), with the regularity hypothesis made explicit; corollary of thm:ext-half + analytic
continuation, not an independent theorem.** Record as a lemma in P47 §22, not as a round result.

**T.2:** I agree: only formal (Σc_N²/N = ∞ verified: S_1(1) > 0 is exactly the coefficient of the pole of ζ in T.3 at n = 1).

**𝒯_∞ not positive:** m(0) = ψ(¼) − log π = −5.372, correct. The correction to the target is valid.

## 2. NO-GO of idea (ii)

- D_μ(ρ) = ζ(ρ)M_μ(ρ) − 1 = −1: **PROVED**, and it is literally rem:ext-killing(iii) (Φ_{Ef}(ρ) = −Φ_{Ψ_f}(ρ)). Not new.
- F4: m + 2Re ζ′/ζ(½+it) = 0 away from ordinates. Correct **unconditionally**: ξ(½+it) is real, hence ξ′/ξ(½+it) is purely
  imaginary, and Re[1/s + 1/(s−1)] = 0 on the line.
- **Proof defect:** the statement "the total symbol is the boundary value from Re s > ½ of 2Re ξ′/ξ, vanishing as a function, with
  mass only at the ordinates" presupposes there are no zeros with β > ½: if there were, −ζ′/ζ has poles in Re s > ½ and there is no
  boundary value of a function holomorphic in the half-plane; the mass is not "at ordinates" but spread as Poisson kernels of symmetric
  pairs (which cancel in Re, but not as a δ). That reading is **CONDITIONAL**. The conclusion is indeed unconditional, via the
  correct route: rem:ext-killing(iii), W_T = Σ_ρ Φ_Ψ̌(ρ)Φ_Ψ̌(1−ρ) (PROVED in P47).
- There is no residual continuous archimedean part: correct, m is absorbed by F4.
- Verdict: **NO-GO of (ii) valid (PROVED via rem:ext-killing(iii)); the formulation "mass only at zeros" must be rewritten without
  boundary value.** Additional correction: since D_μ(ρ) = D_μ(1−ρ) = −1, the zero-side form of the outer object is *identical* to that of g; the
  mollifier disappears entirely. This is another sign that the whole outer apparatus is g modulo radical.

## 3. T.3, the c_{pN} rule, and the numbers (NUMERICAL, exact fractions)

**Proof of T.3.** e | nN ⟺ e/(e,n) | N: correct. Sum over multiples of [d, e/(e,n)]: correct. N = 1 gives c_n; 2 ≤ N < μ gives 0.
**PROVED.**

**Rule c_{pN}.** Divisors of pN (p ∤ N) = {d, pd : d | N}; Σ_{pd<μ}μ(pd) = −Σ_{d<μ/p}μ(d). **PROVED.** Warning: the rule holds
for c_N as a full sum Σ_{d|N}λ_d (not for the sequence "c_N = 0 on [2, μ)" read as a datum); in the spec's usage it is correct.

**Pairs (μ = 15):** recomputed:
| N | c_N | c^{(7.5)}_N | direct c_{2N} |
|---|---|---|---|
| 33 | −1 | 0 | −1 |
| 39 | −1 | 0 | −1 |
| 15 | −1 | −1 | 0 |
All three agree.

**Selberg.** 1/[d,e] = (de)^{−1}Σ_{k|(d,e)}φ(k): correct, S_1(1) = Σφ(k)y_k². This is Selberg applied correctly, but the
"positivity" is trivial (S_1(1) is the density of c_N², ≥ 0 by definition).

**y_k and 𝖼_{b/a}.** y_k = Σ_{k|d, d<μ}μ(d)/d = (μ(k)/k)M̃_k(μ/k), which matches 𝖼_{b/a} = (μ(a)/a)M̃_a(N/a) with a = k
**except for the cutoff convention** (prop:ext-grouped uses k < N/a with its N; the spec uses d < μ strictly). Exact if N ≡ μ under the
convention of AUDIT_200 §1; check the N vs λ² label before citing "exactly."

**Recomputation:** y_1 = −89/15015, y_2 = −17/105, y_3 = −1/6, y_5 = −1/10, y_6 = 1/6, y_7 = −1/14, y_10 = 1/10, y_11 = −1/11,
y_13 = −1/13, y_14 = 1/14: **match**. S_1(1) = 0.432234 (same by the double sum and by Selberg), S_2(1) = S_4(1) = 0.154645,
S_3(1) = 0.269131, S_5(1) = 0.289843: **match**. Missing datum in Q3: 𝔖_1(1) = Σy_k²μ(k) = **−0.040360**.

## 4. P1–P9 v2

- **P1:** correct and verifiable.
- **P2:** correct, and it is the strongest property in the spec. Its consequence ("𝒫 must vanish on the extended radical") is
  exactly what kills Q1 and Q2 (§5).
- **P3(a):** well posed as a filter. **P3(b): ill posed for DH.** It does not say which identity fails. If it is "Q_μ(ιr) = W_T(Ef)",
  the object does not yet exist and P3(b) is a requirement, not a test. If it is "the radical identity of FF.1", the claim "it does not exist
  for DH" is **doubtful**: DH has coefficients periodic mod 5 and a functional equation, so a Poisson-over-N with period 5 and
  an analogous radical exist (the index, V2, records that the lattice Poisson structure is shared with Epstein). What fails for DH
  is the Euler product (and hence the multiplicative rule c_{pN} of the inverse), not the radical. Rewrite P3(b)-DH as "the
  multiplicativity of the truncated inverse fails" and prove it for the concrete object. cΛ with c < 1: remains ARGUED (GG §4).
- **P4, P6, P8:** no new objection; P6 is no longer REF-D after removing P7.
- **P5:** the "separation from a_P on [μ, 2μ)" is a test and is fine.
- **P9: in tension with P2.** P9 requires the object to act on pairs (N, N′) with weights 𝒯_g(log N′/N); P2 (and the spec itself) says
  that every piece indexed by pairs, classes n, or modes k is O(1)‖g‖². P9 + P2 means the object must be a sum of pair-pieces that
  cancel to 70 digits, i.e. P9 describes the **pre-cancellation** structure. The part "never products NN′" is indeed consistent with
  R-K1. It is not REF-D per se, but P9 as stated is incompatible with P2.
- **Any REF-D?** No isolated property; but the "target theorems" of Q1 and Q2 are (§5).

## 5. Candidates

### Q1 (SQ, Selberg variance)
(a) **Tautology + REF-D.** SQ.0 (verified: R_k = Σ_{d|k}μ(k/d)d^{½}τ_{log d}Z_g, PROVED as a comb identity) gives
Ψ̌^{(k)} ≡ −F_k and Σ_k y_kF_k = g; hence y^T𝔅(g)y = 𝒲[g] = W_T(g) by definition. The "target theorem" (dominance
|E| ≤ (1−θ)B_diag for every g in the core) is a positivity claim about the Gram matrix of the translates
{τ_{log N}g}_{N<μ} with Ramanujan coefficients: it is window positivity rewritten. Falsifier: cΛ with c > 1 makes
y^T𝔅y negative at its r_F, without touching SQ.0 (SQ.0 does not see the comb); inequality (b) has no step that excludes this except the
conclusion itself.
(b) Index: E.1/E.5 (ratio classes on dilates of r, pre-cancellation), INV_H ("finite Ramanujan = regrouped Möbius").
New reason (1) is real as a tool (SQ.0), but (2) "Selberg as equality" is empty: the equality is S_1(1) ≥ 0, which does not
touch W. (3) The invariance c_k(nN) = c_k(N) for (n,k)=1 is classical and produces no cancellation between classes in 𝒲.
(c) Lemma SQ.1: the kernel of 𝔅 on span{F_k} contains vectors with y^T𝔅y ≈ ℓ only by numerical coincidence at g*; proving it "by
identity" is exactly proving the sign. False as a decidable lemma.
(d) Output: nominal square (variance), but a bound on the substance.
**Verdict: NO-GO (tautology via SQ.0 + P2).** Keep SQ.0 and T.3 as PROVED tools.

### Q2 (ladder μ → μ/p)
(a) **Degenerate.** For any Y ≥ 2, Σ_{N≥1}c^{(Y)}_N N^{−½}τ_{log N}g = Σ_{d<Y}μ(d)d^{−½}τ_{log d}Z_g is a finite
combination of translates of Z_g: radical by the same SQ.0 argument (it only requires A(g) = 0, **not** depending on the level nor on the
support of g relative to the level-Y window). Since c^{(Y)}_1 = 1 and c^{(Y)}_N = 0 on [2, Y), Ψ̌^{[Y]} ≡ −g modulo radical for
every Y. Hence 𝔊_{YY′} = W_T(g) for all Y, Y′, and 𝒲[Ψ̌^{[μ]} − Ψ̌^{[μ/p]}] = 0. "Ladder positivity" is 0 ≥ 0 and the ladder
identity carries no information. (CONDITIONAL only on SQ.0 holding with Guo L4.4 convergence for translates
of Z_g; if SQ.0 falls, Q1 falls too.) The spec says radicality at level μ/2 "probably fails": it is the opposite.
(b) Index: GG_001 (renormalization to a level), restriction 11; the new reason (discrete sublattice Λ_p) is real as combinatorics
(rule c_{pN}), but the object collapses before it can be used.
(c) Lemma Q2.1(ii): its answer is "yes, radicality holds," and then (iii) gives amplitude 0 in the class modulo radical; the
comparison with −0.481 W* (AUDIT_16 §6) only makes sense on pre-cancellation representatives, violating P2.
(d) Output: none.
**Verdict: NO-GO (degeneration by radicality).** Record in the index as a structural falsification of the spec's ranking.

### Q3 ((S⁺) in shifts)
(a) "𝔖_1 is positive definite in ℤ" is **trivial**: it is the mean autocorrelation of a sequence, PD by Herglotz for any
sequence (including Beurling's or a_P's). It is not an arithmetic square. Positivity does not transfer to W because the weights
∫w_{n,h} come from 𝒯_g = c_g ∗ ν with ν of indefinite sign (m < 0 for |t| < 6.29, atoms −v_n): they are not of positive type in h.
Moreover, by the same SQ.0, the main Poisson term in N (zero frequency ↔ pole of ζ in T.3) is the radical part; all
the content remains in 𝔈_Poisson, at the boundary N ≈ μ, which the spec itself acknowledges as C6 on [μ, μ²] (ARGUED). Falsifier: cΛ with c > 1
leaves 𝔖_n unchanged (it depends only on λ_d) and changes the sign of W.
(b) Index: INV_H (Poisson-on-ℤ as identity), INV_J J2 ("Bochner gives the wrong direction") and J3; phase 193 ((S⁺) as a
separator). New reason (1) "correlations of c_N, not of Λ" is real (they are finite and exact, of Selberg Λ_R type), but
harmless: they do not depend on the comb, so they do not see the falsifier cΛ, c > 1. (3) "(S⁺) as a coupling via h = 1" has no
content: 𝔖_n(1) vs 𝔖_n(0) is a comparison of fixed numbers (−0.040 vs 0.432 for n = 1).
(c) Lemma Q3.1: closed formula for 𝔖_n(h): true and easy; the Poisson error by identity: implausible (per the spec itself).
(d) Output: trivial square + sign-free boundary term = bound.
**Verdict: DOUBTFUL leaning NO-GO.** The asymmetry test 𝔖_2(h) vs 𝔖_2(−h) is cheap and worth running as data, not as a route.

## 6. Verdict and ranking

| Candidate | Verdict | Main reason |
|---|---|---|
| Q3 | DOUBTFUL | trivial PD; indefinite weights; content at the boundary (C6) |
| Q1 | NO-GO | y^T𝔅y = 𝒲[g] by SQ.0: tautology; target = REF-D |
| Q2 | NO-GO | Ψ̌^{[Y]} ≡ −g ∀Y: 𝔊 constant, radical difference |

**Own ranking: Q3 > Q1 > Q2** (reverse of the spec's ordering at the extremes). Do not launch Lemma Q2.1.

**What to change in the spec (effective rejection of all three).**
1. **Replace P9 with P9′:** the object must be defined on the **quotient L²/𝔑**, with 𝔑 = extended radical generated by
   {τ_{log d}Z_g : d ≥ 1} + 𝒢̄ (all translates of summation images). Consequence proved here: every mollified outer
   datum (any level, any base k, or class n) is −g in that quotient. Therefore **the arithmetic of ratios N′/N cannot
   enter through the datum** (it already is g); it can only enter through the **form** 𝒲 restricted to 𝔑^⊥, or through a structure
   on 𝔑 itself (e.g., how 𝔑 depends on a_n ≡ 1). This turns the problem into: describe 𝔑^⊥ ∩ (core) and the symbol of 𝒲 there.
2. **Rewrite P3(b)-DH** in terms of multiplicativity of the truncated inverse (not existence of the radical).
3. **Add P10 (anti-tautology):** every candidate object must first be evaluated modulo 𝔑; if it reduces to 𝒲[g], it is an automatic
   NO-GO.
4. Correct A.1: replace "boundary value with mass only at ordinates" with the reference to rem:ext-killing(iii).

Row D: OPEN. L′♯: OPEN. No sign is asserted.

---

## Summary (≤250 words)

T.1 is PROVED (given Guo, CITED) but is a corollary of thm:ext-half plus analytic continuation; the regularity of g needed
for absolute convergence must be made explicit. The NO-GO of (ii) is valid via rem:ext-killing(iii) (D_μ(ρ) = −1 is already there); the reading "mass
only at ordinates as a boundary value" is CONDITIONAL (it presupposes the absence of zeros with β > ½) and must be rewritten. T.3, Selberg, and
the rule c_{pN} = c_N − c_N^{(μ/p)}: PROVED; the three pairs and all the y_k, S_1 = 0.432234, S_2 = S_4 = 0.154645, S_3, S_5,
recomputed with exact fractions, agree (NUMERICAL); 𝔖_1(1) = −0.04036. y_k = 𝖼_{b/a} except for the cutoff convention.
Central finding: SQ.0 implies that every mollified outer object, at any level, is −g modulo the radical. So Q1 is
tautological (y^T𝔅y = 𝒲[g], target REF-D) and Q2 degenerates (𝔊 constant, mollifier difference radical, 𝒲 = 0): both NO-GO;
the risk flagged for Q2 pointed the wrong way. Q3: the PD property of 𝔖_1 is trivial (autocorrelation), the weights are not of positive type,
the content remains at the boundary: DOUBTFUL. P3(b)-DH ill posed (DH does have periodic Poisson; what fails is multiplicativity). P9
is in tension with P2. Proposal: P9′ = object defined on L²/𝔑 (𝔑 = extended radical), P10 anti-tautology. Ranking:
Q3 > Q1 > Q2; do not launch Q2.1.
