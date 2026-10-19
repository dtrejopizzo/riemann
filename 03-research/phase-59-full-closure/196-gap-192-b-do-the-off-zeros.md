# Document 196 — GAP-192.B: do the off zeros of Davenport–Heilbronn reach polylog scale?

**Program:** Riemann Hypothesis — Phase 59 (full closure)
**Mandate:** decide [GAP-192.B] (D192 §5): does there exist a sequence of off zeros of the Davenport–Heilbronn function with b_j·log γ_j → 0 (or b_j ≤ (log γ_j)^{−1−η})? If YES, polylog repulsion is an Euler property and [CONJ 179.6-strong] is correctly aimed; if NO, the Euler mechanism is mis-aimed. Two routes: (1) CLT/level-crossing on the line (main); (2) effective universality (backup). Full candor; no numerics; backward-only citations.
**Prerequisites:** D192 (GAP-192.B, test 192.2, E-192.1); D179 (Conj 179.6-strong/∞); **D150 (Prop 150.2 — DISCLOSURE: D150 is NOT third-party audited, debt E-194.6 of D194 §5.3; risk rated LOW, textbook input; every use here is flagged)**.

---

## 0. Conventions and the exact object

**The D–H function** ([DH36]; standard form, Def. 146.2 / D150 §4.3):
$$f(s)\;=\;\frac{\sec\theta}{2}\Bigl(e^{-i\theta}L(s,\chi)+e^{i\theta}L(s,\bar\chi)\Bigr),\qquad \tan\theta=\kappa:=\frac{\sqrt{10-2\sqrt5}\,-2}{\sqrt5-1},$$
with χ the primitive complex character mod 5 with χ(2)=i. I write L₁:=L(s,χ), L₂:=L(s,χ̄).

**[CHECK 196.0 — correction to the assignment].** χ(−1)=χ(4)=χ(2)²=i²=−1: the character is **ODD** (a=1), the completion is Λ_j(s)=(5/π)^{(s+1)/2}Γ((s+1)/2)L_j(s), not Γ(s/2). The assignment said "χ even, Γ(s/2)" with an instruction to verify: verified and corrected. The choice of θ ([DH36]; exposition in [Tit86 §10.25], [BG11]) makes the coefficients of f real (a_n = secθ·Re(e^{−iθ}χ(n))) and makes Λ_f(s):=(5/π)^{(s+1)/2}Γ((s+1)/2)f(s) satisfy **Λ_f(s)=Λ_f(1−s)** — a Riemann-type functional equation, WITHOUT an Euler product (f is not multiplicative: a₆=a₂a₃ fails). Inherited facts: infinitely many zeros with β>1 [DH36] ("fat zeros"); liminf b=0 over the off zeros [Prop 150.2, **not audited**, E-194.6]. b:=β−½. **Polylog scale**: b ≤ (log γ)^{−1−η}, η>0.

---

## 1. Route 1 (main): structure on the line and the inverted Lehmer mechanism

### 1.1. [LEMMA 196.1] (anchored phases: the Z-functions exist for complex χ)

*For j=1,2 and real t: Λ_j(½+it) = ε_j·conj(Λ_j(½+it)), with ε_j=ε(χ_j) the root number (|ε_j|=1). Consequently Z_j(t):=ε_j^{−1/2}Λ_j(½+it) is REAL for all t, and Λ_f(½+it) is real.*

*Proof.* The series and the gamma factor give Λ(s,χ̄)=conj(Λ(s̄,χ)) (conjugated coefficients, gamma real on ℝ). The functional equation Λ(s,χ)=ε(χ)Λ(1−s,χ̄) at s=½+it: Λ(1−s,χ̄)=Λ(½−it,χ̄)=conj(Λ(½+it,χ)). Substituting, Λ₁(½+it)=ε₁·conj(Λ₁(½+it)); writing Λ₁=Re^{iφ}: e^{2iφ}=ε₁, i.e. φ=½arg ε₁ mod π. The same for j=2. The reality of Λ_f(½+it) follows from Λ_f(s)=Λ_f(1−s) plus real coefficients (Λ_f(½−it)=conj Λ_f(½+it)). ∎

**Structural consequence (correction to the assignment's design).** The assignment proposed analyzing arg g(½+it), g:=L₁/L₂, as a Gaussian process via "arg g = 2 Im log L + deterministic phase." Lemma 196.1 shows that the **value** of arg Λ_j on the line is anchored mod π (what fluctuates à la Selberg is the continuous branch, i.e. the winding/zero count, not the direction of the value): g(½+it) = (ε₁/ε₂)^{1/2}·Z₁(t)/Z₂(t) lives on a **fixed line** through the origin. The zero equation for f on/near the line is therefore not a 2D phase crossing but **ONE real equation**: with w₀:=−e^{2iθ}, f=ce^{−iθ}(L₁−w₀L₂) and, on the line,
$$\Lambda_f(\tfrac12+it)\;=\;c'\,\bigl(Z_1(t)-r_0\,Z_2(t)\bigr)\;=:\;c'\,H(t),\qquad r_0\in\mathbb R,\ H\ \text{real},$$
where r₀∈ℝ is forced by the reality of Λ_f (the choice of θ in [DH36] is exactly the rotation that aligns the two anchored lines). Zeros of f ON the line = sign changes of H; **near-zeros** = positive local minima of |H|.

### 1.2. [LEMMA 196.2] (Rouché conversion: positive minimum ⟹ off pair, with b<r — PROVED)

*Let t₀ be real, 0<r≤1/10. Suppose: (i) Λ_f has exactly 2 zeros (with multiplicity) in the disk D:=D(½+it₀,r); (ii) Λ_f(½+it)≠0 for |t−t₀|≤r. Then the two zeros form a symmetric off pair ρ=½+b+iγ, 1−ρ̄=½−b+iγ with 0<b<r and |γ−t₀|<r.*

*Proof.* The involution σ(s):=1−s̄ fixes D (center on the line, σ is an isometry) and permutes the zeros of Λ_f (Λ_f(1−s̄)=conj Λ_f(s) by FE + real coefficients). No zero lies on the critical segment of D by (ii); a zero fixed by σ would lie on the line — excluded. So σ pairs them up: with exactly 2 zeros, either they form a σ-symmetric pair {ρ, 1−ρ̄} (same ordinate γ, abscissas ½±b, 0<b<r ✓), or each would generate a distinct partner, giving ≥4 zeros in D — contradicting (i). ∎

**Quantitative reading (inverted Lehmer).** A Lehmer pair is a near-double of H that DOES cross (two glued zeros on the line); the enemy here is the same near-double when it does NOT cross: local minimum |H(t₀)|=δ>0 with curvature A≍|H''| ⟹ the local model H≈A((t−t₀)²+δ/A) analytically continues to an off pair with **b≈√(δ/A)**. With A ≍ (log t)²·(local amplitude) — the typical logarithmic derivative is ≍ log t, twice — reaching b ≤ (log γ)^{−1−η} only requires **relative depth δ/amplitude ≲ (log γ)^{−2η}**: a *polynomially weak* requirement in 1/log. Lemma 196.2 makes rigorous the near-crossing→genuine-off-zero step the assignment asked to be formalized: hypothesis (ii) guarantees off-ness; (i) gives b<r with no derivative computation.

### 1.3. The CLT count — what is a theorem and what is not

**Available unconditional inputs:** (a) Selberg's CLT for Dirichlet L-functions: log L(½+it,χ_j)/√(½loglog t) → standard complex Gaussian, UNCONDITIONAL ([S46] for ζ; the method extended to Dirichlet L-functions — quantitative versions in [Tsa84], [RS17]); **joint** version for inequivalent characters (χ≁χ̄): asymptotically independent, engine of [BH95] — hence log|Z₁/Z₂|(½+it) ≈ real Gaussian of variance ~loglog t, and the level condition |Z₁/Z₂|≈|r₀| is realized with density ≍(loglog T)^{−1/2} — a near-positive proportion of t. (b) Second moments of L and L' on the line (unconditional, classical). (c) Total count N_f(T) ~ (T/2π)log(T·√5/2πe)·2 — Riemann–von Mangoldt for f (FE + Dirichlet series, no Euler product, standard); zeros ON the line: ≫ T·(log T)^{1/2}e^{−c√{loglog T}} ([Kar90-91]; low-height computations in [BS07]) — a lower bound, no on-line upper bound.

**The heuristic count (labeled as such, NOT a theorem).** Near-crossings: H has ≍ log T critical points per unit of t; conditional on being in the level window (density (loglog)^{−1/2}), a local minimum of |H| has relative depth ≤ ε with probability ≍ ε (bounded density of values — this is where the CLT with rate [Tsa84/RS17] enters); half (the non-crossing half) produces, via Lemma 196.2, off pairs with b ≍ √ε/log. With ε=(log T)^{−2η}: **≍ T·log T·(log T)^{−2η}(loglog T)^{−1/2} off pairs with b ≤ (log γ)^{−1−η} in [T,2T] — the count CLOSES with abundance**, consistent with [BH95] (almost all zeros of linear combinations of Euler products glued to the line, under RH-for-the-L_j + a spacing hypothesis; statement cited at the level of its abstract — page-level verification pending, [minor literature gap]) and with the fine distribution of [BG11].

**Where unconditional rigor dies — exact identification.** Everything above is rigorous EXCEPT one single point: guaranteeing, for infinitely many t₀→∞, hypotheses (i)+(ii) of Lemma 196.2 with r=r(t₀)≤(log t₀)^{−1−η}. That requires a **near-double below mean spacing** (two zeros of Λ_f in a disk of radius (log)^{−1−η} ≪ 1/log) avoiding the critical segment. The CLT/moments give VALUE distributions; converting them into a guaranteed point-geometric configuration is exactly the small-gaps problem — whose known machinery (Montgomery, Conrey–Ghosh–Gonek) is conditional on RH and designed for ζ. **I do not fabricate the statement: it remains a named GAP.**

**[GAP-196.A — the exact minimal input].** *For some η>0 and infinitely many t₀: Λ_f has exactly 2 zeros in D(½+it₀,(log t₀)^{−1−η}) and none on the disk's critical segment.* Status: open; statistically "almost sure" by the CLT count; **strictly weaker than effective universality** (which would give control of values over the whole disk, overdetermining the configuration) and of second-moment, not universality, nature.

**[REDUCTION 196.3 — what is proved from route 1].** *GAP-196.A ⟹ there exists a sequence of off zeros of f with b_j ≤ (log γ_j)^{−1−η}, in particular b_j·log γ_j → 0.* *Proof: Lemma 196.2 applied to each t₀; the pairs obtained in disjoint disks are distinct and b_j<r(t₀_j)→0 with b_j log γ_j ≤ (log γ_j)^{−η}.* ∎

## 2. Route 2 (backup): effective universality — does NOT penetrate the scale

Prop 150.2 [**D150, not audited, E-194.6**] gives, for each FIXED ε>0, ≫_ε T zeros with b≍ε; penetrating polylog requires the regime ε=ε(T)→0. The known effectivizations of Voronin's theorem ([Gar03]; discrepancy rates of [LLR17-19] for the value distribution of ζ/L) have the quality: for approximation ε, the first admissible τ and the lower density depend on ε in an **at least exponential** way (density bounds of type ≥ exp(−c/ε^{B}) or worse; [literature gap: the exact exponents of [Gar03] and the scope of [LLR] to joint Dirichlet L-functions not page-level verified this session — the conclusion only uses that NO published rate is polynomial in ε]). Inverting: at height T the best achievable ε(T) is at most ≍(loglog T)^{−c}, hence b·log γ ≍ log T·(loglog T)^{−c} → ∞. **Route 2 dies at distance (loglog)^{−c} from the line: two whole scales above the target.** This confirms D192's diagnosis: GAP-192.B *as originally formulated* (via effective universality) is not decidable with that area's technology; route 1 **reformulates** it in terms of value theory on the line, where the deficit is a single configuration statement (GAP-196.A), not an exponentially distant rate.

## 3. Anti-circularity test

| Object | RH-free? | ζ-free? | Where arithmetic enters |
|---|---|---|---|
| Check 196.0 (odd χ) | yes | yes (character mod 5) | character table |
| Lemma 196.1 (anchored phases) | yes | yes | only FE + Schwarz reflection |
| Lemma 196.2 (symmetric Rouché) | yes | yes | none: pure complex analysis |
| Reduction 196.3 | yes | yes | conditional on GAP-196.A |
| CLT count §1.3 | yes (unconditional CLT) | yes | heuristic in the values→configuration step |
| Route 2 §2 | yes | yes | uses D150 **not audited** (disclosed) |

Nothing uses RH or GRH; [BH95] is cited only as conditional corroboration, not as an input of any labeled statement. No numerics.

## 4. Verdict

**GAP-192.B: NOT UNCONDITIONALLY DECIDED, but REDUCED with a proved conversion theorem and an unambiguous conditional/heuristic answer: YES, D–H penetrates the polylog scale.**

1. **[What is proved]:** [LEMMA 196.1] (phase anchoring — corrects the assignment's design: the relevant process is not arg g but the real pair (Z₁,Z₂)); [LEMMA 196.2] (positive local minimum + near-double ⟹ genuine off pair with b<r, via σ-symmetry + Rouché/count); [REDUCTION 196.3]: GAP-196.A ⟹ b_j log γ_j → 0 in D–H.
2. **[The exact deficit]:** GAP-196.A — near-doubles of Λ_f below mean spacing with line avoidance. Statistically abundant (CLT count §1.3: ≍T(log T)^{1−2η} expected configurations); rigorously open — it is a small-gaps problem without RH, not a universality problem. **Net improvement over D192**: the test no longer hangs on effective universality (route 2, dead at (loglog)^{−c}: §2) but on a second-moment statement with active literature.
3. **[Impact on 179.6]:** the conditional answer is favorable to the Euler mechanism: D–H (without Euler) violates polylog repulsion as soon as GAP-196.A is confirmed — the 179.6-strong form would be **correctly aimed** (polylog repulsion would genuinely be an Euler property, not one of the functional equation). While GAP-196.A remains open, the verdict of test 192.2 moves up from "open at polylog scale" to "open but with a complete mechanism and a single missing input, with an unambiguous prediction." No evidence appeared in direction (c) (demolition): on the contrary, no term in the count protects the polylog scale in the absence of Euler-ness.
4. **[Potential publishable note]:** "Off-line zeros of the Davenport–Heilbronn function at polylogarithmic distance" is viable as a conditional result (on GAP-196.A or on the hypotheses of [BH95]) with Lemma 196.2 as a new piece; NOT as an unconditional theorem today.
5. **[Debts]:** D150/Prop 150.2 used and disclosed as not audited (E-194.6, low risk); exact pages of [BH95], [Kar90-91], [Gar03], [LLR] pending page-level verification ([minor literature gap, non-load-bearing: no labeled statement depends on them]).

**Numbered GAPs:** **[GAP-196.A]** (load-bearing): sub-spacing near-doubles of Λ_f with line avoidance — decides GAP-192.B via 196.3. **[GAP-196.B]** (minor): density of zeros of f, N_f(σ>½+(log T)^{−1−η},T)=o(T log T) unconditional — would give "almost all zeros at polylog distance" but not the existence of off zeros (no on-line upper bound, §1.3(c)); recorded as a partially dead route.

**Successor:** attack GAP-196.A with second moments of H and H' on short intervals (Heath-Brown/CGG discrete-moments method adapted to H=Z₁−r₀Z₂, where the CLT-independence of Z₁,Z₂ is an advantage, not an obstacle); if it falls, audit D150 before scaling to publication (mandate E-194.6).

---

### References

**Internal (backward-only):** D146 (Def. 146.2); D150 (§4.3 Prop 150.2 — **not audited**, debt E-194.6); D179 (Conj 179.6, Def. 179.1); D192 (test 192.2, GAP-192.B, E-192.1); D194 (§5.3, E-194.6).

**Literature:** H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series* I, II, J. London Math. Soc. 11 (1936), 181–185, 307–312. — A. Selberg, *Contributions to the theory of the Riemann zeta-function* (1946), Coll. Works I. — K.-M. Tsang, *The distribution of values of the Riemann zeta-function*, thesis, Princeton, 1984. — M. Radziwiłł, K. Soundararajan, *Selberg's central limit theorem for log|ζ(1/2+it)|*, Enseign. Math. 63 (2017). — E. Bombieri, D. Hejhal, *On the distribution of zeros of linear combinations of Euler products*, Duke Math. J. 80 (1995), 821–862. — E. Bombieri, A. Ghosh, *Around the Davenport–Heilbronn function*, Russian Math. Surveys 66 (2011). — A. A. Karatsuba, on zeros of the D–H function on the critical line, Izv. Akad. Nauk SSSR (1990–91). — R. Garunkštis, *The effective universality theorem for the Riemann zeta function*, Proc. "Probability in Number Theory" (2003). — Y. Lamzouri, S. Lester, M. Radziwiłł, *Discrepancy bounds for the distribution of the Riemann zeta-function* (and works on effective universality, ~2017–2019). — E. P. Balanzario, J. Sánchez-Ortiz, *Zeros of the Davenport–Heilbronn counterexample*, Math. Comp. 76 (2007), 2045–2049. — E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford 1986, §10.25. — S. M. Voronin (1975), universality (via D150).
