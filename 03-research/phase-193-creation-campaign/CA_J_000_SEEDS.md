# CA_J_000 — Front J seeds: correlation inequalities and rigorous statistical mechanics (phase 193)

Pen and paper; no numerics run (elementary hand arithmetic only, shown). no equivalence of the
target with any statement about another object is used.
**No sign contact. No negative value for ζ.**

## 0. Corpus check (done first)
`grep -rliE "FKG|Griffiths ineq|chessboard|Brascamp|Pr[eé]kopa"` over all `*.md` of the repository: **0 hits** (verified ).
Neighbouring records that ARE in the corpus and that this front must not retry:
- CA_A_007 §3, Thm 2: OS reflection positivity of the window kernel for Θf(t)=f(−t) on the log line (all of q inverted) fails for
  every atomic comb (concentration at ½log n₀). That is the *continuous, full-inversion* RP. The *lattice, one-prime* reflection θ_p
  on G = ℚ_{>0}^× ≅ ⊕_p ℤ (seed J6) is a different map: it is a monoid automorphism of G that is not induced by any map of ℝ.
- phase 159 G2_B8_R2 §1: the ferromagnetic (Dirichlet-form, jump-process) reading of 𝔞_T on the *t-line*, with couplings ½K and ½v_n ≥ 0,
  and Theorem R (coupling ray β ↦ βΛ non-monotone). That covers GKS/Lee–Yang in the t-picture. Seed J1 uses the *dual lattice picture*
  (sites = integers m ≤ M, couplings 𝖡(log m/k)); not in the corpus.
- phase 78 E78_1: numerical frustration (no ±1 gauge) of a different matrix B_L. Not a proof; not 𝔸_M.
- Lee–Yang (L32), Bost–Connes/KMS, prime gas as product state (CA_E_001 Thm 2), multiplicative chaos (L77): dead, not reopened.

## 1. Setting (as CA_E_001 §0, CA_H_002 §1; checked against P46 eq:symbol, eq:m, lem K, prop:AM)
F₀ ∈ 𝒫_{T₀}, ‖F₀‖ = 1, 2T₀ < log 2, c₀ = c_{F₀} (even, |c₀| ≤ c₀(0) = 1, supp ⊂ [−2T₀, 2T₀]), ĉ₀ = F̂₀² > 0.
𝖡(d) = α(d) − ½Σ_{n≥2} v_n[c₀(log n − d) + c₀(log n + d)], α(d) = (1/2π)∫ m ĉ₀ cos(τd)dτ, v_n = 2Λ(n)n^{−½}.
φ(q) = 𝖡(log q) on G; 𝔸_M = [𝖡(log m − log k)]_{m,k≤M}; (eq:target) ⟺ 𝔸_M ⪰ 0 ∀M ⟺ φ PD on G (CA_E_001 Lemma 0).
ν := Bochner measure of 𝖡 on ℝ when 𝖡 is PD; μ_φ = ι_*ν (CA_E_001 Lemma 1).

**Lemma J0 (off-centre archimedean term; PROVED from P46 eq:m).** For |d| ≥ 2T₀,
  α(d) = −½∫_0^∞ K(u)[c₀(d − u) + c₀(d + u)]du,  hence  |α(d)| ≤ 2T₀·K(|d| − 2T₀)   (|d| > 2T₀),
with K(u) = 2e^{3u/2}/(e^{2u} − 1) (positive, decreasing).
*Proof.* m = C₀ + ∫_0^∞(1 − cos τu)K(u)du. (1/2π)∫ĉ₀ cos τd = c₀(d) = 0 for |d| ≥ 2T₀, and (1/2π)∫ĉ₀ cos τu cos τd dτ =
½[c₀(d−u) + c₀(d+u)]. Fubini is legitimate because for |d| > 2T₀ the integrand vanishes for u < |d| − 2T₀. For d > 2T₀, c₀(d+u) = 0, the
support of c₀(d − ·) has length 4T₀, |c₀| ≤ 1, K decreasing. ∎

**Lemma J0′ (one-prime values are negative on short windows; PROVED).** Let p be prime.
(a) If 2T₀ < log(1 + 1/p), then 𝖡(log p) ≤ −(log p)/√p + 2T₀K(log p − 2T₀).
(b) If 2T₀ < log(1 + 1/p²), then 𝖡(2log p) ≤ −(log p)/p + 2T₀K(2log p − 2T₀).
In both cases the right side is < 0 for T₀ small enough (depending on p). Explicitly, for p = 2 and 2T₀ ≤ 0.1:
  𝖡(log 2) ≤ −0.490 + 0.1·K(0.593) ≤ −0.490 + 0.215 < −0.27,   𝖡(log 4) ≤ −0.346 + 0.1·K(1.286) ≤ −0.346 + 0.114 < −0.23.
*Proof.* (a) The only n ≥ 2 with |log n − log p| < 2T₀ is n = p (the nearest integers p ± 1 are at log-distance ≥ log(1+1/p)); c₀(log n + d)
vanishes for d > 0. So the comb part is −½v_p c₀(0) = −(log p)/√p. Lemma J0 bounds α. (b) Same with n = p², v_{p²}/2 = (log p)/p, and
the neighbours p² ± 1 at log-distance ≥ log(1 + 1/p²). As T₀ → 0 the error 2T₀K(·) → 0 while the comb term is fixed.
p = 2: e^{0.8895} = 2.434, e^{1.186} = 3.274, K(0.593) = 4.868/2.274 = 2.141; e^{1.929} = 6.883, e^{2.572} = 13.09,
K(1.286) = 13.77/12.09 = 1.139; for n = 3, 5 the log-distances to log 2, log 4 are 0.405, 0.288, 0.223 > 0.1. ∎
(These are values of the *kernel* 𝖡 at nonzero shifts, not values of any quadratic form: no negative value for ζ is implied.)

## 2. PRINCIPIO RECTOR for this front
The interacting system has sites in the monoid (ℕ, ·) or its group G and interaction kernel φ(q) = 𝖡(log q): the *graph* is
multiplicative (q = m/k, divisibility, gcd/lcm), the *strength* is additive (it depends on |log q|, the + side of log). Each
correlation inequality below needs a structural property of the pair (graph, strength): ferromagnetic sign, log-supermodularity on
the lattice, reflection symmetry, log-concavity. For each seed we state which of + and · it uses and test whether that property
holds for φ. The +/· clash of the front is this: **monoid symmetries of G (reflections θ_p, lattice operations gcd/lcm per prime) do
not preserve the archimedean line ι(ℝ) ⊂ Ĝ, while the Bochner measure of φ lives on that line**.

## 3. Seeds and pre-screens
Columns: FE-gen = holds for Epstein/ζ_K as well (then not ζ-specific); G0 = positivity is a Gram/covariance factorization;
O7 = comb-only (survives quartets); [crit] = can it see λ_min(𝔸_M) = M^{−3+o(1)} (EXP_005, NUMÉRICO quoted); Idx = corpus.

| # | seed | +/· use | FE-gen | G0 | O7 | [crit] | Idx | pre-screen verdict |
|---|---|---|---|---|---|---|---|---|
| J1 | Griffiths I/II (GKS) with 𝔸_M as couplings (precision matrix) or as covariance | ·: graph m~k; +: sign of 𝖡(log m/k) | — | covariance reading = G0 | — | — | t-line reading in G2_B8 | **develop (CA_J_002 §1)**: needs a ferromagnetic gauge; test it |
| J2 | FKG / Harris / Holley / Ahlswede–Daykin on the divisor lattice (ℕ, \|, gcd, lcm), distributive | ·: lattice; +: only via φ | lattice ≅ ideal lattice of any free monoid (G1) | yes if the form is a covariance | — | no | 0 hits | **develop (CA_J_002 §2)**: least dead +/· seed; Euler tests = FKG-equality class |
| J3 | Ginibre, GHS, Lebowitz, Newman (Ising/φ⁴ correlation inequalities, Lee–Yang adjacent) | needs J1 sign | — | — | — | — | L32 neighbour | DISCARD: all presuppose ferromagnetic couplings ⇒ die with J1 (CA_J_002 Thm 1.2); GHS/Lebowitz control 3-/4-point truncations, the target is a 2-point form |
| J4 | Brascamp–Lieb variance inequality (Var ≤ ∫∇f·(Hess V)^{−1}∇f) | +: Hessian | yes | **yes**: needs Hess V ⪰ 0, i.e. the form itself convex | — | — | 0 hits | DISCARD: input is the target (REF-D); output is a variance bound |
| J4′ | geometric Brascamp–Lieb datum (log-embedding ℝ^S→ℝ and coordinate projections), Lieb's Gaussian-extremizer theorem, BCCT finiteness | +: B₀ = Σx_p log p; ·: coordinates | **yes**: BCCT finiteness depends only on dim(B_jV); ker B₀ in general position iff all log p ≠ 0 ⇒ Beurling (O11) passes | — | — | no | 0 hits | DISCARD: dimension data cannot separate; Lieb "Gaussians suffice" is the analogue of CA_E_001 Thm 1 (Euler tests suffice), already PROVED there, no sign |
| J5 | Prékopa–Leindler / log-concavity of ν, of 𝖡, or of a Pólya-type kernel | + only | yes | — | — | — | Pólya class K phase 135; PF₅ fails (G7) | DISCARD (retry): log-concavity of Fourier data = Pólya-frequency route, closed |
| J6 | chessboard estimates / lattice reflection positivity in prime coordinates (site and bond reflections θ_p of ℤ^S) | ·: θ_p monoid automorphism; +: φ lives on ι(ℝ) | no (prime-indexed reflections) | no (RP is a Hankel form) | — | — | CA_A_007 is the continuous full-inversion RP only | **develop (CA_J_001)**: chessboard input = RP_p; decide RP_p |
| J7 | Gaussian domination / infrared bounds (Fröhlich–Simon–Spencer) | via RP | — | — | — | — | — | DISCARD: requires RP ⇒ dies with J6 (CA_J_001 Thm 1) |
| J8 | negative dependence: strong Rayleigh / real-stable generating polynomials (Borcea–Brändén–Liggett) | ·: multiaffine in primes | — | — | — | — | Lee–Yang neighbour (L32) | DISCARD: stability = zero location of a multivariate polynomial; Lee–Yang family, dead |
| J9 | Fortuin–Kasteleyn / random-cluster representation of the covariance | needs nonnegative bond weights | — | yes | — | — | — | DISCARD: requires ferromagnetic weights ⇒ J1 |
| J10 | Dobrushin uniqueness / Kotecký–Preiss cluster expansion: positivity of the free-energy Hessian by smallness of couplings | + strength vs · graph | yes | — | — | **fails**: perturbative ⇒ Gershgorin-type margin, cannot see M^{−3} | 0 hits | DISCARD: termwise bound ((R)(3), (B′)), [crit] |
| J11 | Holley comparison: μ₁ ≼ μ₂ stochastically if μ₁(x∧y)μ₂(x∨y) ≥ μ₁(x)μ₂(y); compare ζ's "measure" with a model | · lattice, + weights | — | needs positive measures | comparison of combs = linear in Λ | — | — | folded into J2 (CA_J_002 Prop 2.4) |
| J12 | log-supermodularity of the kernel on the exponent lattice (φ(x∨y)φ(x∧y) ≥ φ(x)φ(y)) as a hypothesis for an FKG proof of the target | ·: lattice; +: φ | — | — | — | — | 0 hits | folded into J2: φ takes negative values (Lemma J0′) ⇒ not an FKG weight |

Survivors developed: **J6** (CA_J_001) and **J1 + J2** (CA_J_002). All others discarded with the killing clause in the table.
