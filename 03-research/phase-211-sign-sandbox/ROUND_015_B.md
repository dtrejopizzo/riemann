# Round 15 B — The low block: what the half-line identity leaves, the nested cancellations, and where the falsifiers die

Target (★): λ_A(T) ≥ 0 for every T. Notation of ROUND_008_E, ROUND_012_B, ROUND_015_A: λ = e^T, N = λ² = e^{2T}, c = 2πN,
ψ_k the k-th prolate of [−λ, λ] (unit norm), φ_k its whole-line extension, χ_k its concentration, d_k = 1 − χ_k, ε_k = i^k,
u_k := √χ_k φ_k 1_{|ξ|>λ} (out-of-band datum, ⟨u_j, u_k⟩ = δ_{jk}d_k), E the summation map, 𝒯 the tail map
𝒯h(x) = 1_{(−∞,−T)}(x)e^{−x/2}Σ_{n≥1}h(ne^{−x}), F_n := n-th summand of 𝒯h (the n-th dilate), ω = ξ/λ.
𝒲 is the complete form on the line:
    𝒲(F, G) = (1/2π)∫m F̂ Ĝ̄ − Σ_{n≥2}Λ(n)n^{−½}[⟨F, G(·−log n)⟩ + ⟨F, G(·+log n)⟩] + A(F)B(G) + B(F)A(G),
with the FULL comb (all n ≥ 2, no truncation at 2T). Low block: V_low = span{ψ_0, ψ_2, ψ_4, ψ_6, ψ_8} cut by the four
functionals f(0), ℱf(0), A(Ef), B(Ef) (ROUND_008_E Prop 3.3: one survivor f_*, the minimiser direction of λ_A to angle 1e-4).
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 0. Corpus check
Read: STATEMENT_001, OBJECT_SPEC_001, ROUND_001_B (Thm 1.1 radical lemma, Cor 1.2 half-line identity, Prop 1.3 defect),
ROUND_007_D, ROUND_008_E (§2 Ritz table, Prop 3.3 index count, (5.1), Prop 5.1 and its c-table), ROUND_009_A, ROUND_009_B,
ROUND_012_B (Thm 1.1 M = S𝒢S), ROUND_014_A, ROUND_015_A (Thm 3.1 comb collapse on Poisson tails, Cor 3.2 exact ledger,
§4 falsifiers of the tail form), ROUND_015_C, REVIEW_008, REVIEW_009. Index: every P211 row and the REVIEW blocks at the end
of 05-meta-and-planning/ROUTES-TRIED-INDEX/README.md. Phase 199 (proof-L-sharp): SYNTHESIS_MECHANISM_001 §3.3 (M3: Langer
chirps, weight 𝔴_μ, resonant pairs (1,n) at ω = √(1+n⁻²)), PROOF_L_SHARP_X_001 (Lemma X.4: log² cancellation),
PROOF_L_SHARP_Z_001 (Theorem C: caustic layer, resonances, κΛ-insensitivity of the layer), PROOF_L_SHARP_S_001 §5
(endpoint constant ζ(2) + ζ′(2)), PROOF_L_SHARP_FF_001 (edge channel FF.2; edge–edge sign OPEN; Constraint 25).

What is on record and is used, not reclaimed: the radical lemma and the half-line identity (ROUND_001_B); the comb collapse
on tails (15A Thm 3.1 = 199 E.2); the dilate ledger with weight 𝔴 (199 M3 / 15A Cor 3.2); Lemma X.4; Theorem C (layer value
and resonance size for a single prolate tail, there for λ_W at μ with index 4); the cΛ-insensitivity of the layer.
What differs (and why no recorded failure is repeated).
(i) Object: the λ_A low block (index 8, four constraints, window variable T) — not the λ_W/L′♯ object of phase 199, not
the high block of 12B/14A/15A. The task here is not a new sign mechanism but the exact bookkeeping of the low block:
which comb is left, which part of Λ acts, which identity makes the leading orders cancel, and where each falsifier dies.
(ii) The falsifier analysis is quantitative on recorded data (ROUND_008_E §5 table): a two-term law with two different
thresholds for c > 1 and c < 1, with the mechanism of each (§4). Not on record.
(iii) Nothing in this memo uses a per-harmonic sign plus decoupling (S_001 NO-GO), stationary phase between chirp and
kink line as the size of the datum (FF Constraint 25), or the class/selection rule as a sign (9B, 12B).
No equivalence of (★) with another statement is used; no zero data, no explicit formula over zeros.

## 1. What the half-line identity leaves (task (1))

### 1.1 The answer: full comb, not comb-free (PROVED, assembled from recorded pieces)
For f admissible (f even, supp f ⊂ [−λ, λ], f(0) = ℱf(0) = f(λ) = 0), ROUND_001_B Cor 1.2 gives W_T(Ef) = 𝒲[Ψ_f] with
Ψ_f = 𝒯(ℱf) supported in (−∞, −T]. The form 𝒲 is the COMPLETE form: archimedean symbol m on all of ℝ, comb over ALL
n ≥ 2, and the rank-two Tate term. Nothing is removed. On a half-line function the comb does not truncate: for x < −T and
every m ≥ 2, x − log m < −T, so every shift log m overlaps the tail with itself. So arithmetic remains, twice:
(a) inside Ψ_f, through the coefficients 1 of the summation over ℕ (𝒯 samples ℱf at ne^{−x}, n ≥ 1);
(b) in the comb of 𝒲, with weights Λ(m), all m.
The two meet exactly (15A Thm 3.1, = phase 199 E.2, PROVED): τ_{log m}F_n = m^{1/2}F_{nm} on the tail, hence
    comb part of 𝒲[𝒯u] = 2Σ_N (Λ ∗ 1)(N)⟨F_N, 𝒯u⟩ = 2⟨𝒯_log u, 𝒯u⟩,                                   (1.1)
whenever Σ_N log N‖F_N‖ < ∞. So after the identity the comb is the resonant weight log N on the dilate index N — the
Dirichlet convolution Λ ∗ 1 = log, not the window comb (log n, Λ(n)), n < N, of the definition of a_T.

### 1.2 The low-block matrix (PROVED given ROUND_012_B (S), (T); entries defined as in 15A Prop 1.1)
For f = Σ_{k∈{0,2,4,6,8}} a_kψ_k in the admissible part of V_low,
    W_T(Ef) = Σ_{j,k} a_ja_k ε_jε_k 𝒢_{jk},   𝒢_{jk} = 𝒲(𝒯u_j, 𝒯u_k)
           = 𝒜_∞(𝒯u_j, 𝒯u_k) − ⟨𝒯_log u_j, 𝒯u_k⟩ − ⟨𝒯u_j, 𝒯_log u_k⟩ + A(𝒯u_j)B(𝒯u_k) + B(𝒯u_j)A(𝒯u_k),       (1.2)
𝒜_∞ the archimedean (Lévy) part: 𝒜_∞(F, G) = C_0⟨F, G⟩ + ½∫_0^∞(2⟨F, G⟩ − ⟨F, τ_uG⟩ − ⟨τ_uF, G⟩)K(u)du, K the Lévy kernel
of STATEMENT_001 §1. In dilate coordinates (15A Cor 3.2):
    𝒢_{jk} = Σ_{N,N′}[𝒜_∞(F_N^{(j)}, F_{N′}^{(k)}) − (log N + log N′)⟨F_N^{(j)}, F_{N′}^{(k)}⟩] + (Tate),
    F_N^{(k)}(x) = 1_{x<−T}e^{−x/2}u_k(Ne^{−x}),  ‖F_N^{(k)}‖² = N^{−1}∫_{Nλ}^∞u_k².
The prolate data enter only through u_k = √χ_kφ_k on |ξ| > λ, i.e. through the whole-line extension of the prolate.
Domain caveat (PROVED, 15A remark): a raw prolate has f(λ) = ψ_k(λ) ≠ 0, u_k = ε_kψ_k(λ)sin(2πλξ)/(πξ) + O(ξ^{−2}),
‖F_N‖ ≍ N^{−1}, and the absolute series in (1.1) diverges. The admissible part of V_low keeps f(λ) free (four constraints,
five prolates, one survivor), so the survivor f_* has f_*(λ) ≠ 0 generically, and for it (1.2) holds only as the limit of
mollified data (15A Prop 1.1 with ε → 0) — ARGUED: W_T(Ef_ε) → W_T(Ef_*) since Ef_ε − Ef_* is a sum of ramps of width ε
at the N breakpoints (form-norm O(ε log(1/ε)), m of logarithmic growth); the convergence of 𝒲[𝒯ũ_ε] needs a uniform bound
on the collapsed comb tail Σ_{N>X} log N⟨F_N, 𝒯u⟩ (conditionally convergent: ‖F_N‖² ≍ N^{−2}, the squared terms sum),
not proved here. Index-count consequence (ARGUED, matches ROUND_008_E §2.2): imposing f(λ) = 0 as a fifth constraint on V_low
leaves no survivor, so the index-8 law λ_A ≈ κ₈d_8 is carried by data with f(λ) ≠ 0: the edge channel is part of the
bottom at leading order, not a correction.

### 1.3 Leading order in c (ARGUED; Langer/WKB form CITED as in phase 199 Theorem C)
Each u_k is, on ω > 1, a Langer wave with the common leading phase c√(ω²−1), index-dependent phase φ_k(ω) (from the
(k + ½) term of the prolate ODE), amplitude ∝ |ψ_k(λ)|(ω√(ω²−1))^{−1/2}c^{−1/2}, and Bessel form ψ_k(λ)J_0(c√(ω²−1))
in the zone ω − 1 ≲ c^{−2} (regular singular point, not Airy). With Slepian's identity ∂_c log χ_k = 2φ_k(1)²/c (CITED,
used in ROUND_008_E), ψ_k(λ)² = φ_k(1)²/λ ≍ c d_k/λ, so all amplitudes are ∝ √d_k: the entries of the low block are
    𝒢_{jk} = √(d_jd_k)·[ ∫_1^∞ 𝔴_N(ω) cos(φ_j(ω) − φ_k(ω)) dm(ω) + R_{jk}(N) ]·(1 + O(log c/c)),
    𝔴_N(ω) = H(ω)·log(Nω²/√(ω²−1)) − 2H₁(ω),   H(ω) = Σ_{n≤ω}1/n,  H₁(ω) = Σ_{n≤ω}(log n)/n,
    dm = (2/π)dω/(ω√(ω²−1)) (Langer mass, = (2/π)dθ with ω = sec θ),                                        (1.3)
R_{jk} the resonant pairs (1, n) (stationary points ω₁ = √(1+n^{−2}) on dilate 1, ω_n = √(n²+1) on dilate n, phase
c(n²−1)/n, size O(c^{−1/2}) each, summable in n — phase 199 Theorem C, there for k = 4). The diagonal (j = k) is exactly the
ledger of 15A Cor 3.2 with m replaced by its value at the local frequency τ = cω²/√(ω²−1) (log(τ/2π) = log(Nω²/√(ω²−1));
the 2π of Γ_ℝ against c = 2πN). Because d_0 : d_4 : d_8 ≍ 1 : c⁴ : c⁸ (and d_2, d_6 interleaved), and the survivor's
coefficients a_k are fixed by four O(1) functionals, W_T(Ef_*) = a_8²𝒢_88(1 + O(1/c)): the bottom is the (8, 8) entry
times the square of the survivor's ψ_8-coordinate. The constant κ₈ of ROUND_008_E is therefore predicted as
    κ₈ ≈ ½[D(N) + R_{88}(N)]·a_8²/‖Ef_*‖²,   D(N) := ∫𝔴_N dm ≥ log 2N                                     (1.4)
(normalisation per side as in Theorem C; the factor a_8²/‖Ef_*‖² is a fixed-T quantity of the five-prolate block, not
computed here). Check against the data (NUMERICAL, recorded): κ₈ grows roughly linearly in T on T ∈ [0.8, 1.3]
(κ₈/2T = 0.76, 0.75, 0.62, 0.72, 0.92), as D(N) = 2T·(const) + O(1) predicts; the ratio a_8²/‖Ef_*‖² is the untested factor.

## 2. Which part of Λ acts on the low block (task (2))

### 2.1 Not the atoms at log n > T, and not the near-coincidences (PROVED structure + ARGUED sizes)
The task's guess "the tail lives at log-scales > T, where the comb has atoms at log n > T" is not what happens. By (1.1)
the comb on a Poisson tail is never evaluated atom by atom: every shift log m sends dilate n onto dilate nm, and the sum
over m collapses to (Λ ∗ 1)(N) = log N on dilate N. What the low block sees of Λ is therefore:
(a) the values (Λ ∗ 1)(N) = log N, weighted by the dilate mass ‖F_N‖² ≍ d·N^{−2}; dilate N samples only ω ≥ N. In the
    Langer mass dm = (2/π)dθ (ω = sec θ) the caustic layer ω ∈ (1, 2) carries 2/3 of the mass and has H₁ = 0: it is
    comb-free (phase 199 Theorem C item 6, PROVED algebra). The comb acts only on the cells ω ≥ 2 (mass 1/3), through
    2H₁(ω) = 2Σ_{n≤ω}(Λ∗1)(n)/n, dominated by n = 2, 3, … (cell n carries Langer mass ≍ n^{−2});
(b) the resonant pairs (1, n), whose phases e^{ic(n²−1)/n} = e^{2πiN(n − 1/n)} carry N (not Λ) and whose size is
    O(c^{−1/2}) per pair with the comb weight log n inside (1.3);
(c) the Tate term, A(𝒯u)B(𝒯u) = O(d·N^{−2}) relative (ARGUED: ∫u over a chirp of frequency 2πλ is O(amplitude/λ)).
The near-coincidences m ≈ kn, m ≠ kn, of the window (STATEMENT_001 §4(vi)) do not appear on the low block at all: the
exact identity (ROUND_001_B Thm 1.1) has converted the whole window comb Σ_{n<N}v_n c_{Ef}(log n) into the O(1) cancellation
of §3.1 plus the tail, and on the tail only EXACT divisibility N = nm survives at leading order (non-resonant dilate
pairs decouple at relative order 1/c, resonant ones at c^{−1/2}).
So the active arithmetic is strictly smaller than the near-coincidence structure: it is the divisor-sum structure
Σ_{n≤ω}(Λ ∗ 1)(n)/n of the first few cells, i.e. constants of the type γ, γ₁, ζ(2), ζ′(2).

### 2.2 The constant in the dual (harmonic) bookkeeping (ARGUED; consistency check with phase 199 S_001 §5)
For the far part of the tail (ω ≫ c, where the Langer phase is c ω and u = f(λ)sin(2πλξ)/(πξ)), the Poisson sum is a
sawtooth: Σ_n u(nw) = f(λ)(½ − {λw})/w. Computing 𝒲 on S(y) := e^{y/2}·f(λ)(½ − {λe^y})e^{−y}, y > T (tail written on
the right half-line; 𝒲 is reflection invariant) harmonic by harmonic: harmonic j has local frequency 2πjx, x = λe^y > N,
mean energy density f(λ)²dw/(2π²j²w²) in w = e^y, and m(2πjx) = log(jx) + O(x^{−2}); with ∫_λ^∞log(jλw)w^{−2}dw =
(log j + 2T + 1)/λ this gives
    archimedean = (f(λ)²/(2π²λ))·Σ_j (log j + 2T + 1)/j² = (f(λ)²/(2π²λ))[ζ(2)(2T + 1) − ζ′(2)],
    comb (Franel: ∫_0^1(½−{mt})(½−{t})dt = 1/(12m)) = (f(λ)²/(2π²λ))·2ζ(2)Σ_mΛ(m)/m² = (f(λ)²/(2π²λ))·(−2ζ′(2)),
    total = (f(λ)²/(2π²λ))·[2Tζ(2) + ζ(2) + ζ′(2)] = (f(λ)²/(12λ))·[2T + 1 − (−ζ′/ζ)(2)] = (f(λ)²/(12λ))(2T + 0.43),
the Tate term being O(f(λ)²λ^{−5}). With T = 0 this is the endpoint constant ζ(2) + ζ′(2) = 0.707 of phase 199 S_001 §5
(there with the opposite sign, because S_001 evaluates the mirror form Q = −𝔔 + …); the window adds 2Tζ(2) = log N·ζ(2).
Two remarks. (i) This is a bookkeeping check, not a size: on prolate data the region ω < c is a Langer chirp, not a
sawtooth (FF Constraint 25 forbids using the kink line as the size of the datum), and (1.3) is the leading form. (ii) The
comb enters through Σ_mΛ(m)m^{−2} = −ζ′(2)/ζ(2) = 0.570 — the Euler product at s = 2, i.e. the smallest primes.

## 3. The cancellations and the first non-cancelling term (task (3))

### 3.1 First cancellation, O(1) → O(d_8): the radical identity (PROVED, ROUND_001_B Thm 1.1; reading new)
Raw entries are O(1): W_T(Eψ_0)/‖Eψ_0‖² = 0.14–0.17 (ROUND_008_E §2.1), because ψ_k(0) ≠ 0 and ℱψ_k(0) ≠ 0 leave the Poisson
boundary terms ±½ψ(0)e^{x/2}, ½ℱψ(0)e^{−x/2} in Eψ_k. On the admissible part the identity W_T(Ef) = 𝒲[Ψ_f] holds, and
Ψ_f is built from the out-of-band datum alone, whose squared norm is EXACTLY Σa_k²d_k (double orthogonality, 12B (S)).
So the e^{−2c}·poly size of the bottom is not a cancellation among the prolate asymptotics: it is d_8 = 1 − χ_8 itself,
the squared out-of-band norm of ψ_8. The cancellation that produces it is the identity, read on the window:
    Π_T(Ef) = 𝒜_∞(Ef) + 2A(Ef)B(Ef) − 𝒲[Ψ_f]         (Π_T(F) := Σ_{n<N}v_n Re c_F(log n), the window comb energy),   (3.1)
i.e. on admissible data the window comb energy equals the archimedean energy up to O(d). Recorded instance (ROUND_008_E §5,
NUMERICAL): on the five-prolate Ritz vector Π_T(F_b) = 𝒜_∞(F_b) = 0.0331 (T = 1), 0.0152 (T = 1.2), equal to 10⁻²² and
10⁻⁴⁰ relative. Inputs of (3.1): coefficients 1 on ℕ (Poisson over ℤ), Λ ∗ 1 = log (−ζ′ has only the pole at 1), the
functional equation with χ′/χ = −m on the line; all used at once (ROUND_001_B §1). This is the mechanism asked for in (3).
It carries no sign: (3.1) is an identity.

### 3.2 Second cancellation, inside the tail: log² against log² (PROVED inequality; leading form ARGUED)
On the tail, at depth ω the archimedean symbol is log(Nω²/√(ω²−1)) ≈ 2T + log ω on each of the H(ω) ≈ log ω active
dilates, and the collapsed comb removes 2H₁(ω) ≈ log²ω: the log² terms cancel (phase 199 Lemma X.4). What is left is
non-negative term by term:
**Lemma 3.1 (PROVED).** For T > 0 and ω > 1, 𝔴_N(ω) ≥ 2T·H(ω) ≥ 2T; on 1 < ω < 2, 𝔴_N(ω) ≥ 2T + log 2.
*Proof.* 𝔴_N = 2T·H + H·log(ω²/√(ω²−1)) − 2H₁. Since ω²/√(ω²−1) ≥ ω, the last two terms are ≥ H_n log ω − 2H₁(n) ≥
H_n log n − 2H₁(n) =: F(n) with n = ⌊ω⌋. F(1) = 0 and F(n+1) − F(n) = H_n log(1 + 1/n) − log(n+1)/(n+1) ≥ (H_n − log(n+1))/(n+1)
≥ 0 (log(1+1/n) ≥ 1/(n+1), H_n ≥ log(n+1)). On (1, 2), H = 1, H₁ = 0 and min ω²/√(ω²−1) = 2 at ω = √2. ∎
(F(n) ≥ 0 is Lemma X.4 of phase 199; the increment proof is given for completeness.)

### 3.3 The first non-cancelling term and its sign (ARGUED, leading order in c)
By (1.3) and Lemma 3.1,
    W_T(Ef_*) = a_8²d_8·½[D(N) + R_{88}(N)]·(1 + O(log c/c)),   D(N) ≥ ∫(2T·H)dm ≥ 2T,
and phase 199 Theorem C (stationary phase on the CITED uniform expansion, there for index 4; the bound on |ΣR̂_n| uses only
the n-free amplitude product and |cos| ≤ 1, so it holds for every fixed index) gives |R| ≤ 0.59 for N ≥ 4 against
D_layer ≥ 1.74. So the first non-cancelling term of the low-block Rayleigh value is POSITIVE for T ≥ log 2, with margin
growing like (2/3)·2T. The data are consistent (λ_A > 0 on all resolved windows; κ₈ ∝ T roughly).

### 3.4 Why this is not the sign step (falsifier test of §3.2–3.3; PROVED algebra)
Replace Λ by cΛ in the tail form only: 𝔴_N^c = 𝔴_N − 2(c − 1)H₁. On the caustic layer (2/3 of the mass) H₁ = 0: no change.
On cell n ≥ 2 the change is −2(c − 1)H₁(n), against ∫H₁dm < ∞ (the Langer mass of cell n is ≍ n^{−2}). So the leading
low-block term stays positive for every c < 1 and for 1 < c < 1 + κ_T with κ_T ≍ T > 0; it survives a_P (H₁ replaced by a
smaller divisor sum) and every finite modification of weight below ≍ T. By rule 4 the positivity of §3.3 is NOT a sign
step. All Λ-specificity of the low block sits in the identity (3.1), which has no sign. Conclusion for (3): the low block,
at its first non-cancelling order, is positive for comb-robust reasons, and its Λ-exactness is an identity. There is no
third object between them that could carry an arithmetic sign on the low block alone.

### 3.5 Where the sign competition really is: the Schur term of the survivor (NUMERICAL from recorded data + ARGUED)
The low-block value is a Ritz value: λ_A ≤ W_T(Ef_*)/‖Ef_*‖². The true bottom is the Schur complement of the survivor
against the rest of P_T (the other near-null rungs: odd sector κ₁₀d_10, even ladder κ(1 − χ_{4j+8}) of 9B, the high block,
and the stiff O(1) directions):
    λ_A = W_T(Ef_*)/‖Ef_*‖² − sup_G |W_T(Ef_*, G)|²/(‖Ef_*‖²·a_T(G)) + (higher Schur terms)   (restatement, REF).
By the bilinear identity, W_T(Ef_*, Eg) = 𝒲(Ψ_{f*}, Ψ_g) for g admissible (O(√(d_8d_g))) and W_T(Ef_*, G) = −𝒲(Ψ_{f*}, G)
for G supported in the window (O(√d_8)); so every Schur term is of order d_8, the same order as the ledger. Recorded data
measure it: Ritz on five prolates = 1.49–1.69 λ_A, on seven = 1.33–1.47 λ_A (ROUND_008_E §2.2). So the Schur correction
removes 33–40 % of the ledger value: the sign of λ_A at order d_8 is decided by "ledger (comb-robust, +) minus coupling
(window–tail cross terms 𝒲(Ψ_{f*}, ·), comb-dependent, −)", with observed margin ≈ 0.6 of the ledger. This competition, not
the low block itself, is where a sign step must act.

## 4. Where cΛ breaks the cancellation (task (4))

### 4.1 The break is at O(1), in (3.1), on the window (PROVED, ROUND_008_E (5.1))
For any weight w, W^w_T(Ef) = 𝒲[Ψ_f] + 𝒫_{Λ−w}[Ef]. For w = cΛ the defect is (1 − c)Π_T(Ef): in (3.1) the window comb
energy is multiplied by c and the archimedean energy is not, so the O(1) cancellation leaves (1 − c)·𝒜_∞(Ef) + O(d).
The tail term 𝒲[Ψ_f] (the comb-robust ledger of §3) is untouched at this order. So cΛ does not break the low block where
its sign is computed; it breaks the identity that made the low block small.

### 4.2 Anatomy on the recorded block (NUMERICAL from ROUND_008_E §5 table; mechanism ARGUED)
Second-order perturbation of the bottom b(c) of a^{cΛ}_T on the five-prolate block:
    b(c) = λ_A + (1 − c)P − (1 − c)²X + O(|1 − c|³),  P = Π_T(F_b) (first order), X = Σ_g |Π_T(F_b, g)|²/(μ_g − λ_A),
g the other block eigenvectors. At T = 1, the entries c = 1 ± 10⁻⁴ (−5.3·10⁻⁶, +1.1·10⁻⁶) give P = 0.032 (recorded
Π_T(F_b) = 0.0331: agreement to 3 %) and X ≈ 210. Hence two thresholds of different nature:
- c > 1 dies at FIRST order, |1 − c| ≈ λ_A/P ≈ 7·10⁻²² (T = 1): the uncancelled window comb energy;
- c < 1 survives first order (P > 0) and dies at SECOND order through the coupling of the survivor to the stiff directions,
  at |1 − c| ≈ P/X ≈ 1.5·10⁻⁴: for c = 1 that coupling is O(√d_8) (§3.5); for c ≠ 1 it acquires (1 − c)Π_T(F_b, g) = O(|1 − c|).
At c = 0.99 the quadratic model overshoots (−0.021 vs recorded −0.0039): the stiff eigenvalues move at that size. At T = 1.2 the
two near-1 entries give P_eff = 0.005 against the recorded 0.0152: the second-order model is outside its range there (a block
eigenvalue μ_g − λ_A ≲ 10⁻³ is the likely cause; not checked). The two-threshold picture is therefore validated at one window.
Reading: the low block rejects c > 1 through the identity (3.1) at first order and rejects c < 1 only through the
survivor's coupling to the rest — the same Schur competition as §3.5. The coupling is the place where both falsifier
sides and the true bottom meet.

### 4.3 The other falsifiers (PROVED as statements about where they enter; sizes ARGUED)
(b) a_P: defect 𝒫_{Λ1_{p<P}}[Ef] on the window, O(1), first order with the sign of the P-smooth comb energy of F_b; the
    tail ledger is unaffected at leading order (§3.4). (c) Beurling: (3.1) has no analogue (no Poisson over the generalised
    integers, ROUND_001_B §1, 199 S_001 §7(i)); the O(1) cancellation does not exist (ROUND_007_C certifies λ_A < 0 for
    3 → 3.2 at ½log5 + 10⁻⁴). (d) finite modification e: defect −𝒫_e[Ef], O(|e|), first order on the window.
In every case the argument "identity (3.1) + ledger" fails at the identity, as rule 4 requires; the ledger alone would
survive (a) for c < 1, (b), small (d).

## Result
PIVOT with reason, plus PROVED pieces.
Reason: the sign step requested for the low block does not exist as a separate step. At its first non-cancelling order
the low block is a comb-robust positive ledger (survives c < 1, a_P, small finite modifications; NOT a sign step by rule 4);
its Λ-exactness is the identity (3.1), which has no sign. The sign of λ_A at order d_8 is decided by the Schur competition
between the survivor's ledger and its coupling to the rest of P_T (window–tail cross terms 𝒲(Ψ_{f*}, ·)), which removes
33–40 % of the ledger on the recorded windows and is also exactly where c < 1 is rejected.

### What was proved
- (1) The half-line identity leaves the COMPLETE form with the FULL comb on a half-line tail; on tails the comb collapses
  exactly to the resonant weight (Λ ∗ 1)(N) = log N on the dilate index (assembled from ROUND_001_B, 12B, 15A, 199 E.2).
  Low-block entries (1.2): 𝒢_jk = 𝒲(𝒯u_j, 𝒯u_k) with u_k the whole-line prolate extension off the band; domain caveat for
  f(λ) ≠ 0 (absolute series diverges; mollified limit ARGUED).
- (3) The O(1) → O(d_8) cancellation is the radical identity, read as (3.1): window comb energy = archimedean energy up to
  O(d) on admissible data; d_8 is exactly the out-of-band norm (no hidden cancellation among prolate asymptotics).
- Lemma 3.1: 𝔴_N(ω) ≥ 2T·H(ω) ≥ 2T, and ≥ 2T + log 2 on the caustic layer (elementary; contains Lemma X.4 of phase 199).
- §3.4: the leading low-block term is positive for every c < 1 and for c − 1 ≲ T (PROVED algebra on the ledger).
- §4.1: under cΛ the defect is (1 − c)Π_T(Ef) on the window, i.e. the break is in (3.1) at O(1), not in the tail.
ARGUED: leading form (1.3) (Langer/WKB, stationary phase), κ₈ ≈ ½[D(N) + R]·a_8²/‖Ef_*‖², index-count consequence that the
bottom carries f(λ) ≠ 0, positivity of the first non-cancelling term for T ≥ log 2 (via phase 199 Theorem C), the dual
(harmonic) constant (f(λ)²/(12λ))(2T + 1 − (−ζ′/ζ)(2)) = (f(λ)²/(12λ))(2T + 0.430).
NUMERICAL (from recorded tables only, no new runs): Schur share 33–40 %; two-threshold falsifier law at T = 1
(P = 0.032 vs 0.0331 recorded; X ≈ 210; c > 1 threshold 7·10⁻²², c < 1 threshold 1.5·10⁻⁴); model fails at T = 1.2.

### What failed and why
- The premise of (2) "the tail sees the atoms at log n > T": false; the comb on a tail never acts atom by atom (collapse
  (1.1)); the active arithmetic is divisor sums over the first cells and the resonant pairs (1, n), smaller than the
  near-coincidence structure, which is absorbed by (3.1).
- The premise of (3) "the leading orders cancel among prolate asymptotics, and the first survivor carries the sign": the
  cancellation is the identity (exact, signless), and the first survivor is positive for comb-robust reasons — it cannot be
  the sign step (rule 4). A second cancellation (log² against log², Lemma X.4) is also robust.
- No sign step on the low block alone: the competition is with the coupling term, which the low block does not contain.
- The two-threshold model is validated at T = 1 only.

### Next concrete step
Isolate the coupling term of §3.5 at one window (T = 1): compute the vector 𝒲(Ψ_{f*}, ·) on the stiff directions and the
admissible ladder (prolates up to 4N and the four constraint directions), split each entry into its archimedean, collapsed-
comb and Tate parts, and measure which part produces the 33–40 % reduction and the X ≈ 210 of §4.2. Then test whether the
reduction is bounded by the ledger with a constant < 1 by an identity of the type (3.1) applied to the pair (f_*, g)
(both admissible: 𝒲(Ψ_{f*}, Ψ_g), a tail–tail pairing with the collapsed comb) — the only place on the low block where a
comb-exact, sign-carrying inequality could live. Run the falsifiers there (c = 1 ± 10⁻⁴, a_3) before any proof attempt.

## Index row and ledger line
Index (05-meta-and-planning/ROUTES-TRIED-INDEX/README.md): row P211-15B. Ledger (LEDGER.md): line C33.
