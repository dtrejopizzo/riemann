# N_BUILD_011 — Existence: combs whose window form is positive for ALL T. Continuous Beurling systems: YES (PROVED). Atomic: OPEN (sharp sub-question). A positive-start segment to Λ

Pen and paper. For a positive measure λ on (0,∞) (the "comb", window weight measure; for Λ it is Σ v_nδ_{log n}) put
𝔞_T^{(λ)}(F) := 𝔞_∞(F) − ∫_{(0,2T)} Re c_F dλ on P_T ∩ D_T, b_T(λ) := its bottom, Pos := {λ : b_T(λ) ≥ 0 ∀T > 0}.

## Corpus check
L2_BUILD_011 rows 1–23 and row 6 (cΛ fails for c large and small), L2_BUILD_014/015 (Euler–Poisson cube; λ concave in the weight
vector w; no prime–prime terms; (Q) ill-posed), cor:void/thm:finmod, R167_103 Theorem S (Beurling/DMV falsifiers of SIEVE proofs),
R164_201 (Beurling below a third), Paper 47 thm:posext. grep "positive for all T|existence of a positive comb|Beurling.*positive|
continuous Beurling|ψ_B = κx|uniformly positive": nobody constructs a comb with b_T ≥ 0 for every T; Beurling systems appear
only as falsifiers. New: Theorem 1, Corollary 2, Proposition 3, the segment of §4.

## 1. Structure of Pos (PROVED)
(i) b_T is concave in λ (inf of affine functionals), so Pos is convex, and so is each Pos_T := {b_T ≥ 0}.
(ii) Pos + ν ⊂ Pos for every positive measure ν with ∫Re c_F dν ≤ 0 ∀F ∈ P_T, ∀T; in particular for ν = 2κ′e^{u/2}du|_{(0,∞)},
κ′ ≥ 0, because ∫₀^{2T}Re c_F·2e^{u/2}du = −𝔭(F) ≤ 0 on P_T (N_BUILD_001 (A)).
(iii) (mass growth) If λ ≥ 0 and its partial mass A^λ(T) := λ((0,2T)) satisfies A^λ(T_j) ≤ c₀T_j² along T_j → ∞ with c₀ small
(absolute), then λ ∉ Pos. *Proof.* Dilated test F = (¼−∂²)G_T, G_T = T^{−½}g(·/T), g ≥ 0 even in C_c^∞(−1,1): c_G ≥ 0, c_F =
(1/16)c_G − ½c_G″ + c_G⁗ with |c_G″| ≤ T^{−2}‖c_g″‖_∞, so ∫Re c_F dλ ≥ −C A^λ(T)T^{−2}·‖F‖²; and 𝔞_∞(F)/‖F‖² → C₀ (N_BUILD_003 Thm 1
proof). Hence 𝔞^{(λ)}(F)/‖F‖² ≤ C₀ + o(1) + C c₀ < 0. ∎

## 2. Theorem 1 (continuous main-term combs; exact characterization, PROVED)
For κ ≥ 0 let ρ_κ := 2κe^{u/2}du on (0,∞) and g_κ(τ) := m(τ) + κ/(¼+τ²). Then for every T and F ∈ P_T ∩ D_T
 𝔞_T^{(ρ_κ)}(F) = (1/2π)∫ g_κ(τ)|F̂(τ)|² dτ,
and **ρ_κ ∈ Pos ⟺ g_κ ≥ 0 on ℝ ⟺ κ ≥ κ* := sup_{τ: m(τ)<0} (−m(τ))(¼+τ²)**. κ* is finite (m continuous, increasing in |τ|,
m(0) = C₀ < 0, m → ∞: {m < 0} = (−τ₀, τ₀) bounded, lem:mbounds) and κ* ≥ |C₀|/4 = 1.343… (value at τ = 0) and
κ* ≤ |C₀|(¼ + τ₀²).
*Proof.* Identity: N_BUILD_001 (A) with the factor κ. (⇐) the integrand is ≥ 0. (⇒) if g_κ(γ) < 0 for some γ > 0, the spectral-
derivative family F_T^γ ∈ P_T (Paper 47 §17) and lem:wit-conc with p = g_κ (continuous, |g_κ| ≤ C(1+log(1+|τ|))) give
𝔞_T(F_T^γ)/‖F_T^γ‖² → g_κ(γ) < 0; for γ = 0 use the dilated family of §1(iii) (concentration at 0). ∎
For κ > κ*, η_κ := inf g_κ > 0 (g_κ ≥ (κ−κ*)/(¼+τ₀²) on {m<0}, ≥ κ/(¼+τ²) + m on {m ≥ 0}, and → ∞): **b_T(ρ_κ) ≥ η_κ > 0 uniformly
in T.** Note Λ's main term is ρ_1 and 1 < 1.343 ≤ κ*: the main term of Λ alone is NOT in Pos; its fluctuation must supply the
rest (consistent with N_BUILD_001 (E): λ^♯ → C₀+4 < 0, and L2_BUILD_010 centre criticality).

## 3. Corollary 2 (genuine Beurling systems in Pos, PROVED)
Let x₀ > 1 and κ > κ*. The continuous Beurling generalized-prime system with Chebyshev function ψ_B(x) = κ(x − x₀)_+ (CITED as a
valid continuous Beurling system: its zeta exp(∫_{x₀}^∞ x^{−s}dψ_B(x)/log x) converges for Re s > 1) has window comb
λ_B = 2κe^{u/2}du on (log x₀, ∞). If 2κ(√x₀ − 1) < η_κ then λ_B ∈ Pos with b_T(λ_B) ≥ η_κ − 2κ(√x₀ − 1) > 0 for all T > ½log x₀,
and for T ≤ ½log x₀ the comb is empty in the window, b_T = λ_{∞,P}(T) > 0 provided ½log x₀ < 0.58 (CITED cor:Tarch), which holds
for x₀ close to 1.
*Proof.* λ_B = ρ_κ − ρ_κ|_{(0,log x₀)}; the removed part changes the form by ∫₀^{log x₀}Re c_F·2κe^{u/2} ≤ 2κ(√x₀−1)‖F‖². ∎
**So Pos is NONEMPTY, and contains Euler-type (continuous Beurling) systems with strictly, uniformly positive window forms.**
They violate ℤ-integrality (atoms) — consistent with the input map: they are not falsifiers (they are positive), and they show that
positivity for all T is not, by itself, an arithmetic miracle; it is forced here by an overdense smooth prime distribution
(κ > κ* > 1: more "primes" than ℤ has).

## 4. Proposition 3 (the positive-start segment to Λ; PROVED reformulation)
For κ > κ* and t ∈ [0,1] put λ_t := (1−t)ρ_κ + tΛ. On P_T,
 𝔞_T^{(λ_t)}(F) = (1/2π)∫ g_{κ_t}|F̂|² − t𝓕_T(F),  κ_t := (1−t)κ + t,
with 𝓕_T the Chebyshev fluctuation of Λ (N_BUILD_001). By concavity (§1(i)), t ↦ b_T(λ_t) is concave, positive at t = 0; so
t*(T) := sup{t ≤ 1: b_T(λ_t) ≥ 0} is a well-defined first-contact parameter and **Λ ∈ Pos_T ⟺ t*(T) = 1**; moreover
b_T(λ_t) ≥ (1−t)η_κ − t(A_T + 4) (|𝓕_T| ≤ (A_T+4)‖F‖², and g_{κ_t} ≥ (1−t)g_κ + t·m^♯ ≥ (1−t)η_κ + t(C₀+4)... used crudely), so
t*(T) ≥ η_κ/(η_κ + A_T + 4 + |C₀+4|) > 0 for every T. (N^♯) is the endpoint t = 1 of a family that starts uniformly positive.

## 5. Atomic combs (the cube) — OPEN, sharpened
Does Pos contain a nonnegative ATOMIC comb (prime-power supported, Euler structure; L2_014 cube or discrete Beurling)?
Necessary (§1(iii)): mass ≥ c₀T². Heuristic route: discretize ρ_κ (κ > κ*) by generalized primes placed so that ψ_B(x) = κx + O(log x)
(greedy placement, including prime powers): the fluctuation E_B(u) = O(ue^{−u/2}) is integrable, giving |fluctuation| ≤ C(1 + ‖F′‖)
— but the archimedean margin grows only like log of frequency, so high-frequency tests are not controlled by this bound
(quadrature error ≍ Ω at frequency Ω, vs η_κ + log Ω). Sub-question (A): can generalized primes be placed so that the atomic
comb's pairing with c_F deviates from ρ_κ's by ≤ η_κ‖F‖² + (1/2π)∫(m(τ) − C)_+|F̂|² for all F? This is a pure discrepancy problem
on the real line (no arithmetic), OPEN. If YES: Pos ∩ (atomic Beurling) ≠ ∅; it would NOT contradict R167_103 Theorem S (which
concerns sieve proofs) nor the input map (positive objects are not falsifiers).

## Barrier position
Theorem 1 is an exact characterization for a class of combs, not a statement about Λ; Corollary 2 is the first proved member of
Pos. Proposition 3 is a one-parameter family in the comb, not in T: W-fam (families of windows) does not apply; Lemma flowdet does
apply to any attempt to follow t ↦ b_T(λ_t) by a flow near t*(T) (coefficient = functional of the minimizer), so §4 is a
reformulation with a positive start, not a proof route by itself.

## Self-review
1. Theorem 1 (⇒) at γ > 0 uses F_T^γ ∈ P_T and lem:wit-conc's polynomial growth (g_κ ≤ |m| + 4κ): correct. The window
truncation of ρ_κ is automatic (c_F = 0 beyond 2T). Correct.
2. η_κ > 0: on {m ≥ 0} g_κ ≥ κ/(¼+τ²) > 0 but tends to 0 as |τ| → τ₀⁺? no — m ≥ 0 there and κ/(¼+τ²) ≥ κ/(¼+τ²) ≥ … the inf over a
compact neighbourhood is positive and g_κ → ∞ at infinity; so inf > 0. Correct.
3. Corollary 2: "valid Beurling system" for a continuous ψ_B is CITED (Beurling generalized primes allow continuous
distributions, e.g. Diamond–Zhang monograph); the window form only uses the measure, so the conclusion b_T > 0 is PROVED regardless.
4. §4 lower bound used crude inequalities; stated as such; t* > 0 holds.
5. Does Corollary 2 conflict with anything? Paper 47 statements are about Λ and its modifications; positivity of an overdense
smooth system is new and harmless. It shows the "sign" is easy with κ > κ*: the content of D is that κ = 1 plus the fluctuation of
ℤ-primes suffices. This is a genuinely new quantitative fact: the arithmetic fluctuation must supply exactly the deficit
between the main-term coefficient 1 and κ*(≥ 1.343) — measured by the symbol κ*/(¼+τ²) − 1/(¼+τ²).
**SIGN CONTACT (positive side, not for Λ):** uniform strict positivity PROVED for the explicit Beurling systems of Corollary 2.
No negative value certified; nothing proved about Λ.
