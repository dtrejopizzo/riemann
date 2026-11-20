# Round 17 C — First-cell coercivity of the archimedean form on a window of length log 2

Target (★): λ_A(T) ≥ 0 for every T. Notation of ROUND_016_B (F₁, 𝔇, first Poisson cell, transported functionals) and of
Paper 47 §sec:levy (K, m, C_0, lem:K, thm:S, thm:A) and §subsec:arch (𝒜_∞, prop:arch).
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 0. Corpus check
Index row read: P211-16B (first-cell lemma, idealised cell values 0.549 / 0.075, "next: prove 𝒜_∞ ≥ μ on length-log 2
windows under the transported constraints"); ledger C34. Paper 47: lem:K and eq:m (m(τ) = Re ψ(¼ + iτ/2) − log π =
C_0 + ∫(1 − cos τu)K(u)du), thm:S (m − C_0 = φ(τ²), φ complete Bernstein), thm:A (Lévy-energy form), prop:arch(iii)
(the complete form 𝒜_∞ = 2AB + (1/2π)∫m|F̂|² is ≥ 0 for 2T < log 2, cited from the literature; strictness at the boundary not
re-proved there).
What differs. Nothing indexed is retried. prop:arch(iii) concerns the complete form (with the polar term 2AB) on windows
strictly shorter than log 2 and gives ≥ 0 without a constant. Here the window has length exactly log 2, the form is the
comb-free, polar-free Lévy form (1/2π)∫m|F̂|² (which has bottom −1.27 there), and the claim is a strict, explicit,
computer-certified constant on an explicit hyperplane (and on an explicit codimension-4 subspace). The tool (symbol
truncation + polynomial compression + Taylor tail bound, §2) is a lower-bound method; Galerkin values in 16B were upper
bounds and are not used as inputs.

## 1. The problem, written out (PROVED bookkeeping)

### 1.1 The form
By lem:K and Tonelli, for F ∈ L²(I), I an interval of length L = log 2 (F extended by 0),
    𝒬[F] := (1/2π)∫_ℝ m(τ)|F̂(τ)|²dτ = (C_0 + ∫_L^∞K)‖F‖² + ½∫_0^L K(u)∫|F(x+u) − F(x)|²dx du,
with C_0 + ∫_L^∞K = ψ(¼) − log π + log coth(L/4) + π − 2 arctan e^{L/2} = −2.3784… (thm:S(iii) with 2T = L). 𝒬 is
translation invariant, so the position of I is irrelevant. This is 𝒜_∞[F₁] of ROUND_016_B Lemma 2.2 (first cell, no comb,
no polar term).

### 1.2 The transported constraints on F₁
With F₁(x) = e^{−x/2}u(e^{−x}) on x ∈ (−T − log 2, −T), ξ = e^{−x} ∈ (λ, 2λ), dξ = ξdx, and the transport f ≈ ℱ^{−1}u of
16B §3.1 (u even, 2 = two half-lines):
- f(0) = 2∫_λ^{2λ}u dξ = 2∫F₁(x)e^{−x/2}dx. In the centred variable y = x + T + L/2 ∈ I this is λ^{1/2}e^{L/4}·2∫F e^{−y/2}dy:
  **T-free up to a scalar.** The hyperplane is H₀ := {F : ∫_I F(y)e^{−y/2}dy = 0}.
- f(λ) = 2∫F₁(x)e^{−x/2}cos(2πλe^{−x})dx.
- A(Ef) = ∫F₁(x)e^{−x/2}·Σ_{n: ne^{−T}<λ} n^{−1}·2[sin(2πξλ) − sin(2πξne^{−T})]/(2πξ) dx, ξ = e^{−x}.
- B(Ef) = ∫F₁(x)e^{−x/2}·Σ_{n: ne^{−T}<λ} 2[Ci(2πξλ) − Ci(2πξne^{−T})] dx.
(Exactly the functionals of tools/tail_direct/cellRp.py; the transport itself is the idealisation of 16B §3.1, ARGUED
there.) The weight of f(0) is e^{−x/2}, which is the second Tate moment of the window: on H₀ one of the two polar factors
vanishes, so on H₀ the complete form of prop:arch and 𝒬 coincide. This is why f(0) alone moves the bottom from −1.27 to
≈ +0.07: it removes exactly the direction that the polar term 2AB compensates in the complete form (whose bottom on
length log 2 is ≈ 0, 16B §3.1 row R = 2, "with polar", 0.001).

## 2. The lower-bound tool (PROVED)

### Lemma 2.1 (monotone symbol)
m is even and nondecreasing on [0, ∞). *Proof.* thm:S(i): m(τ) − C_0 = φ(τ²) = Σ_k τ²/(a_k(τ² + 4a_k²)), each summand
nondecreasing in τ² ≥ 0. ∎

### Lemma 2.2 (symbol truncation)
For τ* > 0 put M = m(τ*), h = (M − m)1_{|τ|<τ*} and G = P_I Op(h) P_I on L²(I). Then for F ∈ L²(I):
    𝒬[F] ≥ M‖F‖² − ⟨GF, F⟩,   0 ≤ G,   ‖G‖ ≤ M − C_0.
*Proof.* By Lemma 2.1, min(m, M) = M − h with h ≥ 0, h ≤ M − m(0) = M − C_0. 𝒬[F] ≥ (1/2π)∫min(m,M)|F̂|² = M‖F‖² −
(1/2π)∫h|F̂|², and (1/2π)∫h|F̂|² = ⟨GF,F⟩ ≤ sup h·‖F‖². ∎
G has the entire kernel g(x − y), g(s) = (1/π)∫_0^{τ*}h(τ)cos(τs)dτ.

### Lemma 2.3 (polynomial compression with a tail bound)
Let P be the orthogonal projection of L²(I) onto polynomials of degree < n, I = [−L/2, L/2], φ_l = ((2l+1)/L)^{1/2}P_l(2y/L).
(i) ⟨Gφ_k, φ_l⟩ = (1/π)∫_0^{τ*}h(τ)·((2l+1)(2k+1))^{1/2}L·j_l(τL/2)j_k(τL/2)·(−1)^{(l−k)/2}dτ for l ≡ k (mod 2), 0 otherwise
(φ̂_l(τ) = ((2l+1)L)^{1/2}(−i)^l j_l(τL/2)).
(ii) ε := ‖(1 − P)G‖ ≤ ‖(1 − P)G‖_HS ≤ L·(τ*/π)(M − C_0)(τ*L/2)^n/n!.
(iii) For w ∈ L²(I) analytic, ‖(1 − P)w‖² = ‖w‖² − Σ_{l<n}⟨w, φ_l⟩².
*Proof.* (i) ∫_{−1}^1P_l(t)e^{−izt}dt = 2(−i)^l j_l(z), and the integrand is even in τ. (ii) For fixed y,
‖(1−P)g(·−y)‖ ≤ (1/2π)∫_{−τ*}^{τ*}h(τ)dist(e^{iτ·}, 𝒫_{n−1})dτ and dist(e^{iτ·}, 𝒫_{n−1}) ≤ L^{1/2}·sup_I|Taylor remainder at
0| ≤ L^{1/2}(|τ|L/2)^n/n!; integrate the square over y ∈ I. (iii) Parseval. ∎

### Lemma 2.4 (constrained lower bound)
Let w_1, …, w_k ∈ L²(I), V = {F : ⟨F, w_i⟩ = 0 ∀i}, W = [Pw_1 … Pw_k] (n × k in the basis φ_l) of full rank, δ_i ≥ ‖(1−P)w_i‖,
η := (Σδ_i²)^{1/2}‖(WᵀW)^{−1}‖^{1/2}, g_∞ := M − C_0, and γ ≥ λ_max(PGP restricted to W^⊥ ∩ ran P). Then for F ∈ V,
    𝒬[F] ≥ (M − λ_max[[γ, ε + g_∞η], [ε + g_∞η, ε + g_∞η²]])·‖F‖².
*Proof.* p = PF, r = (1−P)F, a = ‖p‖, b = ‖r‖, a² + b² = ‖F‖². ⟨GF,F⟩ = ⟨Gp,p⟩ + 2Re⟨(1−P)Gp, r⟩ + ⟨(1−P)Gr, r⟩ ≤
⟨Gp,p⟩ + 2εab + εb². From ⟨F, w_i⟩ = 0: Wᵀp = −(⟨r, (1−P)w_i⟩)_i, so the component p_W of p in ran W has
‖p_W‖ ≤ ‖(WᵀW)^{−1/2}‖·‖Wᵀp‖ ≤ ηb. With p = p₁ + p_W, p₁ ⊥ ran W: ⟨Gp,p⟩ ≤ γa² + 2g_∞ηab + g_∞η²b². Sum and use
Lemma 2.2; the quadratic form in (a, b) is bounded by its top eigenvalue. ∎

### Certification protocol (computer-assisted step, ball arithmetic, python-flint arb, 120 bits)
tools/first_cell/cert_f0.py (k = 1, w = e^{−y/2}, closed form ⟨w, φ_l⟩ = ((2l+1)/L)^{1/2}L·i^l j_l(iL/4)) and
tools/first_cell/cert_multi.py (k ≤ 4, ⟨w_i, φ_l⟩ and ‖w_i‖² by rigorous acb.integral).
(a) M = m(τ*) by acb digamma. (b) PGP: Gauss–Legendre (40 nodes, arb nodes/weights) on unit panels of [0, τ*], j_l by
j_l(z) = z^l/(2l+1)!!·₀F₁(; l + 3/2; −z²/4); the quadrature remainder is enclosed by the Bernstein-ellipse bound
(64/15)Bρ^{−2N}/(ρ² − 1) (ρ = 2, half-length ½, ellipse inside |Im τ| ≤ 3/8), with B from |j_l(z)| ≤ e^{|Im z|} and
|h| ≤ (M − C_0) + (256/7 + 0.278)(τ* + 1)² (from φ(τ²) = Σ τ²/(a_k(τ² + 4a_k²)): |τ² + 4a_0²| ≥ 7/64,
|τ² + 4a_k²| ≥ 3a_k² for k ≥ 1, Σ_{k≥1}a_k^{−3} ≤ 0.832, on |Im τ| ≤ 3/8); this radius is added to every entry.
(c) γ: floating-point guess + 10⁻¹², certified by an arb LDLᵀ showing Π(γI − PGP)Π + WWᵀ ≻ 0, Π = I − W(WᵀW)^{−1}Wᵀ (for
v ⊥ ran W one has Πv = v, so positivity on W^⊥ follows). (d) ε, δ_i, η as in Lemmas 2.3–2.4, enclosed in arb.

## 3. Results

### Theorem 3.1 (first-cell coercivity on the Tate hyperplane; PROVED, computer-assisted, T-free)
For every interval I of length log 2 and every F ∈ L²(I) with ∫_I F(y)e^{−y/2}dy = 0 (equivalently f(0) = 0 for first-cell
data, any T),
    (1/2π)∫m|F̂|² = C_0‖F‖² + ∫_0^∞(c_F(0) − Re c_F(u))K(u)du ≥ μ₀‖F‖²,   μ₀ = 0.069611732… (lower end of the ball).
Certificate: τ* = 100, n = 112; M = 2.7672890, quadrature radius 1.4·10⁻¹⁵, ε ≤ 2.6·10⁻⁸, η ≤ 3.3·10⁻²⁶⁸, LDLᵀ pivots
≥ 1.7·10⁻³, γ = 2.6976772206; μ₀ ∈ [0.06961173221 ± 4.4·10⁻¹²]. Coarser certificates (same proof): τ* = 20, n = 48:
μ₀ ≥ 0.046056; τ* = 50, n = 72: μ₀ ≥ 0.065479. The Ritz upper bound (n = 40 Legendre, full symbol) is 0.07196, and 16B's
sine-basis value 0.0751 (Nb = 128, still decreasing); so the true constant lies in [0.0696, 0.0720].
*Proof.* Lemmas 2.1–2.4 with k = 1, w = e^{−y/2}; the inequalities (a)–(d) are verified in ball arithmetic; the window
position only rescales w. ∎
Corollary 3.2 (PROVED). On length log 2 the complete form of prop:arch is ≥ μ₀‖F‖² on {B(F) = 0} (the polar term
vanishes there). This is a strict, quantitative, boundary-length statement that prop:arch(iii) does not contain.

### Theorem 3.3 (all four transported constraints; PROVED, computer-assisted, for the stated T)
For F on the first cell satisfying the four transported constraints of §1.2 (f(0), f(λ), A, B),
    𝒬[F] ≥ μ₄(T)‖F‖²,  μ₄(0.8) ≥ 0.527631,  μ₄(1.0) ≥ 0.549417.
Certificates: τ* = 50, n = 72; ‖(1−P)w_i‖² ≤ 2.4·10⁻³² (all i); η ≤ 2.5·10⁻¹⁵; ε ≤ 2.1·10⁻¹³; LDLᵀ pivots ≥ 0.043;
balls [0.5276311697 ± 4.4·10⁻¹¹], [0.5494172344 ± 3.7·10⁻¹¹]. (16B's Galerkin value 0.549 at T = 0.8 is an upper bound;
the gap 0.02 to the certificate is the symbol truncation at τ* = 50, cf. the τ*-sequence of Theorem 3.1.)
Target μ ≥ 0.5: **met** at T = 0.8 and T = 1.0. What is T-free is only Theorem 3.1; μ₄ is certified pointwise in T.
In D-units (×λ/2, 16B §1.2): (λ/2)μ₄ ≥ 0.587 (T = 0.8), ≥ 0.747 (T = 1.0); (λ/2)μ₀ ≥ 0.0775 (T = 0.8).

### NUMERICAL (non-rigorous, for orientation; tools: scratch exploration with the same formulas)
Unconstrained 𝒬 on length log 2, Legendre n = 40: Ritz values −1.2873, 0.0846, 0.5819. So one negative direction; H₀
almost reaches the second eigenvalue (0.0720 vs 0.0846), and the four constraints land just under the third (0.548 vs
0.582). Truncation loss of μ₀ vs τ*: 0.0457/0.0652/0.0693/0.0709/0.0715/0.0719 at τ* = 20/50/100/200/400/1000 (≈ C/τ*).

## 4. What this gives for (HR_g), and what remains
(i) **First-cell data (CONDITIONAL on the transport of 16B §3.1).** If the tail u of a high-block vector lives in
λ < |ξ| < 2λ and its admissibility constraints transport exactly, then 𝒢 = λ·𝒲[𝒯u] = λ𝒬[F₁] ≥ λμ₄‖F₁‖² = (λ/2)μ₄D and,
since ℓ_g ≤ D (ℓ_g is a distance to a subspace, D the full squared norm), 𝒢 ≥ (λ/2)μ₄·ℓ_g: κ_T ≥ 0.587 at T = 0.8 on such
data, and ≥ (λ/2)μ₀ using f(0) alone for every T (0.0775 at T = 0.8). The ℓ_g-bottoms measured in 15A/16B (0.80–0.83 at
K = 88) are above 0.587, consistent with the first stage of the drift stopping at or above this value. ARGUED: since the
measured bottom vectors carry 95–97 % of their tail mass in the first cell (16B §1.3), the first-cell bound controls the
diagonal B₁₁ of the measured drift.
(ii) **Not covered, OPEN:** (a) the transport defect: the in-band part of ℱf and the exact (not transported) constraints;
(b) data spread over R ≥ 3 cells, where the complete form has near-null directions (16B §3.1) — 16B §3.2 shows these are
near-gauge (ℓ_g-quotients 1.28–1.44), so they must be controlled by ℓ_g, not by 𝒬; this needs a multi-cell analogue of
Lemma 2.4 with the gauge closure as the constraint space (the comb enters there: the 𝔇-operator couples cells); (c) the
cross terms between the first cell and the rest (measured ≤ 5 %).
(iii) The method of §2 extends verbatim to any finite family of analytic constraint weights and any window length; for
R cells it needs the comb operator 𝔇 in the compressed matrix (Π-term of tools/galerkin_mp.py is already an exact
polynomial-in-u kernel) and the gauge span as W.

## 5. Falsifier test
Theorems 3.1 and 3.3 concern m, K, C_0 and explicit constraint weights only; no comb weight enters. They hold verbatim
under (a) cΛ, (b) a_P, (c) Beurling systems, (d) finite modifications of v_n. By rule 4 they are therefore not sign steps
for (★) and none is claimed: they are coercivity bounds for the comb-free piece that carries the high-block drift
(16B §1.3(a)). Any sign content must come from step (ii)(b), where the comb and the gauge enter.

## Result
PROVED piece (computer-assisted, ball arithmetic).

### What was proved
- Lemmas 2.1–2.4: monotone symbol, symbol-truncation lower bound with compact remainder, polynomial compression with an
  explicit Hilbert–Schmidt tail, constrained lower bound with constraint-leakage terms (complete proofs).
- Theorem 3.1: on every window of length log 2, (1/2π)∫m|F̂|² ≥ 0.069611‖F‖² on ∫F e^{−y/2} = 0 (T-free); Corollary 3.2
  (complete form ≥ μ₀ on {B = 0} at the boundary length).
- Theorem 3.3: with the four transported constraints, μ₄(0.8) ≥ 0.527631, μ₄(1.0) ≥ 0.549417 (target μ ≥ 0.5 met).

### What failed and why
- Direct rigorous integration of each PGP entry with acb.integral (digamma inside the integrand) was too slow; replaced by
  panel Gauss–Legendre with an analytic Bernstein-ellipse remainder.
- Interval enclosure of digamma on wide complex boxes returns nan/huge balls; replaced by the series bound from thm:S.
- No T-uniform μ ≥ 0.5: the T-free constraint (f(0)) alone gives only 0.0696 (the true value is ≤ 0.0720); the value
  0.53–0.55 needs the T-dependent functionals f(λ), A, B and is certified only at the T computed.

### Next concrete step
Multi-cell version of Lemma 2.4: compress 𝒬∘𝔇 + polar term on R cells (R = 3, 4) with the gauge closure (polynomials
(1 − λ²y²)³(λy)^{2j} transported) as the constraint family W, and certify a positive lower bound of the ratio to ℓ_g;
first, quantify the transport defect (i)/(ii)(a) on the measured bottom vectors.

## Reproducibility
From tools/first_cell/: python3 cert_f0.py 100 112 (≈ 2 min; also 20 48, 50 72); python3 cert_multi.py 50 72 0.8
f0,flam,A,B and python3 cert_multi.py 50 72 1.0 f0,flam,A,B (≈ 2 min each). Outputs: out_100.txt, out_multi_08.txt,
out_multi_10.txt.
