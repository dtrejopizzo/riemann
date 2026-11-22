# CA_K_002 — Guerra-type interpolation for a deterministic frustrated form; disorder and the Ĝ-gauge; heat flow on the solenoid; site independence (prime-sited tests suffice) (seeds K1, K2, K3, K10)

Phase 193. Pen and paper; **no numerics run**. Setting: CA_K_000 §1; CA_K_001 notation.
**No sign contact. No certified negative value for ζ.**

Guerra's mechanism (SK model; CITED: Guerra, CMP 233 (2003); Talagrand, Ann. Math. 163 (2006); Aizenman–Sims–Starr, PRB 68 (2003)):
interpolate H_t = √t H_N + √(1−t) H_decoupled with *Gaussian* couplings; Gaussian integration by parts writes φ′(t) as
−(β²/4)E⟨(R₁₂ − q)²⟩ + (explicit), and the sign of the variance term gives a one-sided bound. Three ingredients: (G-a) a solvable endpoint,
(G-b) Gaussian disorder with matched covariance, (G-c) a remainder that is a square. We test each for 𝔸_M.

## 1. Deterministic interpolation (K1)
**Lemma 1.1 (CITED/standard).** For A(θ) = A₀ + θB (Hermitian), λ(θ) := λ_min(A(θ)) is concave; λ′(θ+) = min_{s∈E(θ)}s*Bs and
λ′(θ−) = max_{s∈E(θ)}s*Bs, E(θ) = unit bottom eigenspace (Danskin / analytic perturbation; Kato, *Perturbation theory*, II.§6). The same holds for
the Gibbs version f_β(θ) = −β^{−1}log tr e^{−βA(θ)} (A ↦ log tr e^{A} convex; CITED), with ⟨B⟩_{β,θ} as derivative.

**Theorem 1.2 (interpolation principle; PROVED).** Let A(1) = 𝔸_M and θ₀ ∈ [0,1). The Guerra-type hypothesis "λ′ ≥ 0 on [θ₀,1]" holds iff
there is a bottom eigenvector s₁ of 𝔸_M with s₁*A(θ₀)s₁ ≤ λ_min(𝔸_M). Without this hypothesis, concavity yields only upper bounds
λ(1) ≤ λ(θ) + (1 − θ)λ′(θ+). The same with f_β and Gibbs states in place of s₁.
*Proof.* Concavity: λ′ ≥ 0 on [θ₀,1] ⟺ λ′(1−) ≥ 0 ⟺ ∃s₁ ∈ E(1) with s₁*Bs₁ ≥ 0; and s₁*A(θ₀)s₁ = λ(1) − (1 − θ₀)s₁*Bs₁. ∎
So every deterministic interpolation reduces its sign to a property of the minimizer of the target (REF-D; SPEC_A Lemma S class), and
the free direction of concavity is the wrong one. For the archimedean → full path (A₀ = Arch_M, B = −Comb_M) the hypothesis is
Comb_M(s₁) ≤ 0; CA_K_001 Prop 1.3(c) shows the opposite end (θ = 0) has Comb_M(s₀) < 0 under the premise. Whether Comb_M(s₁) ≤ 0 is OPEN
and is a minimizer statement (no route).
(G-a) fails twice: the archimedean endpoint is indefinite (CA_K_001 Prop 1.3(a)); the Euler-decoupled endpoint is indefinite (§3, Cor 3.3).

## 2. Disorder: the only symmetry is a gauge (K1 (G-b), K2)
**Proposition 2.1 (twist average = Schur multiplier; quenched ≤ annealed; PROVED).** For a probability μ on Ĝ let K_μ(m,k) := ∫y(m)ȳ(k)dμ(y) = μ̂(m/k).
Then E_{y∼μ}[(y∘s)*𝔸_M(y∘s)] = s*(𝔸_M∘K_μ)s, and λ_min(𝔸_M∘K_μ) ≥ λ_min(𝔸_M). Haar: 𝔸_M∘I = 𝖡(0)I; Kronecker line ν₀: 𝔸_M∘[c₀(log(m/k))].
*Proof.* (y∘s)_m = y(m)s_m; expand. Each U_y𝔸_MU_y* has the spectrum of 𝔸_M, and λ_min of an average of Hermitian matrices is ≥ the average of
their λ_min (concavity of λ_min). ∎
Consequence: averaging over the only symmetry group of the problem produces *upper* bounds on λ_min(𝔸_M) (annealed ≥ quenched); the overlap
R₁₂ = ⟨y∘s, y′∘s⟩ structure is trivial (gauge orbit). (G-b) proper — a Gaussian vector X with E X_mX_k = 𝔸_{mk} — exists iff 𝔸_M ⪰ 0 (G0, REF-D);
the couplings φ(q) are deterministic, so there is no Gaussian disorder to integrate by parts. K2 (Ghirlanda–Guerra, ultrametricity,
positivity of overlaps) has no input. **NO-GO (PROVED for twist averaging; REF-D for Gaussian representations).**

**Remark 2.2 (where twists are not gauges).** Twisting only the comb, a ↦ Λy, is not a gauge: it is the family of CA_K_001 Thm 2.1, whose
unconstrained bottoms lie above ζ's (diamagnetic), and the Fejér points of CA_E_001 Cor 1.1. Neither gives a lower bound for ζ.

**K3 (cavity).** Additive cavity M → M + 1: 𝔸_{M+1} ⪰ 0 ⟺ 𝔸_M ⪰ 0 and the Schur complement 𝖡(0) − b^T𝔸_M^+b ≥ 0 (b in range), b = (𝖡(log((M+1)/k)))_k:
P46 thm:coer-schur/thm:wh-schur class, REF-D. Multiplicative cavity S → S ∪ {p}: the induction of CA_E_001 Thm 1 (PD of the fibre functions g_b):
retry. DISCARD.

## 3. Heat flow on the solenoid; site independence (K10)
Fix weights w_p > 0; ℓ(q) := Σ_p w_pv_p(q)² (finite for q ∈ G); h_t the Gaussian semigroup on Ĝ = ∏_pS¹ with ĥ_t(q) = e^{−tℓ(q)}; μ_t := ν₀ ∗ h_t.
By CA_H_002 Thm 3.1 (Fourier coefficients of ν₀ − m_Ĝ are c₀(log q)1[q ≠ 1]):
 Q_t(s) := Arch(s) − ∫_Ĝ g_s dμ_t = Arch(s) − Div(s) − Σ_{q≠1}e^{−tℓ(q)}c₀(log q)M^Λ_s(q),   Q₀ = s^T𝔸_Ms,   Q_∞ = Arch(s) − Div(s).
**Proposition 3.1 (PROVED).** (a) ∂_tQ_t(s) = Σ_{q≠1}ℓ(q)e^{−tℓ(q)}c₀(log q)M^Λ_s(q): additive-only weight × monoid-only coefficient, linear in Λ
(H-anat, CA_H_002 Thm 3.2). (b) Q_t = Arch − Div − Near∘E_t with E_t the Schur multiplier by the PD Gaussian kernel e^{−tℓ(m/k)} on G.
The weight e^{−tℓ(q)} damps an additive near-identity q = (b+h)/b by its multiplicative height — the one +/·-genuine weight met on this front.
(a) has no sign (c₀ and M^Λ_s both signed); the path is K1 with an extra parameter, Theorem 1.2 applies.

**Theorem 3.2 (site independence; PROVED).** Let X ⊂ ℕ be infinite with x′/x → 1 along consecutive elements (e.g. the primes, CITED: PNT).
Then (eq:target) ⟺ [𝖡(log x − log x′)]_{x,x′∈X, x,x′≤M} ⪰ 0 for every M.
*Proof.* (⇒) principal submatrices of 𝔸_M. (⇐) Given d₁, …, d_K and real s, choose x_j ∈ X ∩ (e^{C+d_j−ε}, e^{C+d_j+ε}) (nonempty for C large,
since consecutive ratios → 1; distinct for C large and ε small). Continuity of 𝖡 gives Σs_js_k𝖡(d_j − d_k) = lim Σs_js_k𝖡(log x_j − log x_k) ≥ 0;
𝖡 is real and even, so complex s splits; thm:oneprofile. (This is the proof of prop:AM(i) with X in place of ℕ.) ∎
**Corollary 3.3 (Div is a site artifact; the Haar endpoint is negative; PROVED).** (i) On prime-sited vectors (X = primes) Div ≡ 0: m = kn
with m, k prime and n ≥ 2 is impossible. So (eq:target) ⟺ Arch(s) ≥ Near(s) for every prime-sited s, every M: on this decisive class there
are no exact multiplicative relations, and the whole comb contribution is the Kronecker defect (CA_H_002 Thm 3.1), i.e. the
near-coincidences p ≈ np′ weighted by Λ(n).
(ii) Arch is indefinite on prime-sited vectors for M large (CA_K_001 Prop 1.3(a), with the approximating points chosen prime as in Thm 3.2).
Hence Q_∞ = Arch − Div is indefinite (Div = 0 there): the Euler-decoupled endpoint of every Haar ↔ line interpolation is negative.
(iii) Under the premise, every prime-sited s with Arch(s) < 0 has Near(s) ≤ Arch(s) < 0: on prime sites the positivity is paid
entirely by near-coincidences of primes with prime-power multiples of primes.
*Proof.* (i) Div(s) = Σ_{kn=m}s_ms_kv_n (prop:AM(iii)); Theorem 3.2. (ii) as stated. (iii) s^T𝔸s = Arch(s) − Near(s) ≥ 0. ∎
**Reading (PRINCIPIO RECTOR).** CA_E_001 Thm 1: Euler-product tests (maximal multiplicative structure) suffice. Theorem 3.2: prime-sited tests
(no multiplicative relations at all) also suffice. So the exact/near split (Div/Near, Haar/line − Haar), and with it the closing edge (m,2m)
of the frustrated cycle, depends on the site set and is not intrinsic: on prime sites the cycle C_m does not exist, frustration persists
through ratios p′/p ≈ 2 (CA_J_002 Lemma 1.2(b) is site-free), and its holonomy is again sgn 𝖡 (CA_K_001 Prop 3.1). The intrinsic object is 𝖡
on ℝ; the +/· interaction enters only through the values of 𝖡 at log q for q near integers, i.e. the R9/(S) locus. Theorem 3.2 and Cor 3.3(i)
are exact restatements (lem:shape-restate class): REF-D, not sign steps. Cor 3.3(iii) is a necessary property and a falsifier test (not computed).

## 4. Screens
| item | REF-D | (B″) | O7/O10/O11/O12 | [crit] | (R) | (P1)–(P6) | PR | sign content |
|---|---|---|---|---|---|---|---|---|
| Thm 1.2 | sign of path = minimizer statement | identity valid for every comb | survive | — | (R)(3),(R)(5) | P2 fails (derivative linear in Λ) | side by side | NO-GO for deterministic interpolation |
| Prop 2.1 | Gaussian form = G0 | every 𝖡 | survive | — | (R)(3) | — | none | NO-GO (wrong direction) |
| Prop 3.1 | — | yes | survive | — | (R)(3) | P2 fails | genuine weight, linear | none |
| Thm 3.2 / Cor 3.3 | exact restatement | yes (any 𝖡; Beurling: same with Beurling primes) | survive | — | — | — | removes the monoid coefficient from the decisive class | REF-D; Cor 3.3(ii) PROVED NO-GO for the Haar endpoint |

## 5. Self-review
1. *Is Theorem 3.2 new?* As stated (arbitrary asymptotically dense site sets, prime sites) it has 0 corpus hits (grep "prime-sited / prime sites /
   primes suffice"); its proof is P46 prop:AM(i) verbatim. Value: it shows Div can be removed from the decisive class, and it
   kills the Haar endpoint (Cor 3.3(ii)). It does not move any clause of (R).
2. *Does Cor 3.3(iii) contradict P46 prop:nearfree (tests on which Near is invisible are positive)?* No: prop:nearfree concerns tests with no
   near-coincidences; prime-sited tests reaching Arch < 0 need widely spread points, which create near-coincidences p ≈ np′ for large C.
   Under the premise Near is then negative enough; nothing is claimed beyond the premise.
3. *Concavity of the Gibbs free energy.* log tr e^{A} is convex on Hermitian matrices (standard; CITED); only the direction is used.
4. *Guerra with the zeros as disorder?* Using the explicit formula to write 𝖡 as a zero sum is (R)(4); excluded by the declared frame and P46.
5. *Numerics.* None run. Cor 3.3(iii) and Prop 1.3(c) of CA_K_001 are falsifier tests that could be computed; under the premise they hold,
   and they are not strictly necessary.
6. *Equivalences.* Theorem 3.2 is an internal restatement of (eq:target);
**Verdict.** K1: NO-GO (PROVED: sign of any deterministic path = minimizer statement; both solvable endpoints indefinite). K2: no input
(PROVED: twists are gauges; Gaussian representation = G0). K3: retry, DISCARD. K10: +/·-genuine weight but linear in Λ; endpoint negative
(PROVED). New exact tool: Theorem 3.2 (site independence) and Cor 3.3 (Div is a site artifact).
