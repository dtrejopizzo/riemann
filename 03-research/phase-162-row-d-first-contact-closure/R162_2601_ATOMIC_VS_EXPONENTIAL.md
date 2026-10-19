# R162_2601 — O2501.1: atomic Λ-comb vs finite exponential density — **NO-GO (PROVED) for atomicity as the separating property; PARTIAL: two PROVED reductions (tempered form = E1; Hamburger rigidity pins the class to ζ alone)**

Pure math, no numerics. Cell 8F / 4E (residual O2501.1 of R162_2501 §6). Gate 1 OPEN; no sign claimed.
Corpus check: R162_2501 (Prop 1–3, Thm 3, M_m); R162_1203 and R162_407 (Hamburger only as dictionary at conductor 1);
grid §3 W1, W3, W8; grid §4 DH, Beurling DMV. No earlier file compares the *tempered part* of the arithmetic
distribution with H(m), and none tests "atomic on {log n}" by itself.

## 0. Setting

H(m): ζ has exactly m quartets off the line, ρ_j=½+β_j+iγ_j, 0<β_j<½. The explicit formula, read as an identity of
distributions in u (well defined on C_c^∞, and on Gelfand–Shilov S^{1}_{1}-type tests of decay e^{−(½+ε)|u|}), is
  D := Σ_n Λ(n)n^{−½}(δ_{log n}+δ_{−log n}) − P_arch − 2cosh(u/2)  =  −Z_R − E,
with Z_R := Σ_{real t} m_t cos(tu) (real zeros, positive integer multiplicities) and
E(u) := Σ_j 4 e^{β_j|u|}cos(γ_j u) (up to the harmless normalisation of 2501). E ≠ 0 ⟺ m>0.

## 1. Falsifier lines first

| model | atomic on {log n}? | log-derivative (integer residues)? | FE of ζ? | off-line | what it kills |
|---|---|---|---|---|---|
| M_m (2501) | no (a.c. E_m) | yes | yes | κ(ζ)+4m | every class-level argument (2501 Thm 3) |
| Λ̃-model (§3, new) | **yes, positive weights** | **no** | no | "m" poles of residue −1 | any argument using atomicity + positivity + growth only |
| DH | yes (complex weights) | yes | conductor 5 | ∞ | atomicity + log-derivative + FE *without conductor 1 / Euler* |
| Beurling DMV | atoms at log of g-integers | yes | no | ∞ | Λ≥0 + Euler + Λ*1=log without ℤ |
| ζ | yes | yes | yes, conductor 1 | m (unknown) | — |

Proving-too-much test: an argument must fail on Λ̃ (atomic, positive, same non-tempered part as H(m)) and must use
something that DH lacks, else it would make an assertion about DH-type functions that nobody can check (not a
contradiction, since DH has m=∞, but a warning that the argument does not see finiteness).

## 2. Theorem T (tempered form, PROVED) — idea (1) is E1

(a) Z_R ∈ S′(ℝ) (since N(T)=O(T log T), Σ m_t cos(tu) converges in S′). (b) E ∉ S′+ (anything of exponential type
< β*) when m>0: pairing with φ(u−a)e^{iγ_j u}, φ∈C_c^∞, grows like e^{β* a}, which a tempered distribution cannot do
against translates of a fixed test (polynomial bound). Hence
  **m = 0 ⟺ D ∈ S′(ℝ).**
(c) D ∈ S′ is a statement about the atomic side alone: with x=e^a it says Σ_n Λ(n)n^{−½}φ(log n−a) − ∫(x-density)
= O(a^A), i.e. ψ-fluctuations O(x^{½}(log x)^{A}) in smoothed form — an RH-type bound. Under H(m) the same
computation gives "exponential type of D modulo S′" = β*, i.e. exactly Prop 1 of 2501 in distribution language.
*Verdict:* "tempered distributions cannot grow" is true but the tempered object is Z_R, not D; whether D is tempered
is C_B itself (W1/E1). Enlarging the space (Gelfand–Shilov, analytic functionals) changes nothing: it only makes D
well defined; it never forces its non-tempered part to vanish. □

## 3. Theorem Λ̃ (atomicity does not exclude E, PROVED)

Let ρ_j as in H(m) (any finite configuration, 0<β_j<½). Put, for n≥1,
  Λ̃(n) := 1 − Σ_j 2Re( n^{ρ_j−1} ).
Then (i) Λ̃(n)>0 for n≥n_0 (since |n^{ρ_j−1}| = n^{β_j−½} → 0); modify finitely many n (a compactly supported, hence
tempered, change) to get Λ̃≥0 everywhere. (ii) Its Dirichlet series is
  G(s) = Σ Λ̃(n)n^{−s} = ζ(s) − Σ_j [ζ(s+1−ρ_j) + ζ(s+1−ρ̄_j)],
meromorphic on ℂ with poles only at s=1 (residue 1) and s=ρ_j, ρ̄_j (residue −1): the *exact* polar pattern of −ζ′/ζ
at a pole and at off-line zeros. (iii) With μ̃ := Σ Λ̃(n)n^{−½}(δ_{log n}+δ_{−log n}) (a positive measure on ±{log n}):
  μ̃ − 2cosh(u/2) + E  ∈ S′(ℝ).
*Proof of (iii).* For φ∈C_c^∞, a>0, f(x) := x^{−½}Λ̃(x)φ(log x−a) (Λ̃(x) the smooth formula). Euler–Maclaurin:
|Σ_n f(n) − ∫_1^∞ f| ≤ ∫|f′| + |f(1)| = O(e^{−a/2}·C_φ), bounded in a. And ∫f dx = ∫(e^{u/2} − Σ_j 2Re e^{(ρ_j−½)u})
φ(u−a)du, i.e. the pairing of e^{u/2} − ½E. Finitely many modified n are a compactly supported atomic distribution. □
*Consequence.* A positive atomic measure supported exactly on {±log n}, with Chebyshev-size weights (Λ̃ = 1+o(1)),
has *exactly* the non-tempered part of D under H(m). So no argument using only {atomicity on log n, positivity,
growth/Chebyshev, S′ vs non-S′} can prove C_B: it would exclude μ̃, which exists. **O2501.1 as literally posed
("atomic vs exponential") is FALSE.** What μ̃ lacks is the remainder structure: μ̃ − 2cosh + E is tempered but is
*not* of the form −Z_R (Fourier transform of a positive integer-multiplicity measure on real points); equivalently G
is not a logarithmic derivative (ζ(s+1−ρ_j) has no Euler-product/log structure; G has no zeros-as-poles beyond the
m chosen ones, and its "zero side" is not a counting measure). □

## 4. Theorem H (the surviving ingredients pin the class to ζ, PROVED modulo standard hypotheses)

Add the missing structure: F meromorphic of finite order, Γ_ℝ(s)F(s)=Γ_ℝ(1−s)F(1−s), finitely many poles, and
−F′/F = Σ a(n)n^{−s} an ordinary Dirichlet series absolutely convergent in some half-plane (atomic on {log n},
arbitrary complex weights). Then F = exp(Σ a(n)(log n)^{−1}n^{−s}) is an ordinary Dirichlet series (the exponential
of a series supported on log ℕ_{≥2} is supported on the multiplicative semigroup ℕ), so by Hamburger's theorem
(in the Bochner/Chandrasekharan–Narasimhan form allowing any half-plane of absolute convergence and finite order)
F = cζ. Hence: **atomic on {log n} + log-derivative + FE of conductor 1 ⟹ F = cζ.** □
*Consequences.* (i) In this class C_B is not a class statement: it is C_B for the single function ζ; there is no
M_m-type falsifier (M_m = ζ·rational is not a Dirichlet series) and no Λ̃-type one (not a log-derivative). The class
determined by the ingredients O2501.1 is allowed to use contains one element, so "incompatibility of atomicity with
E" in this class is literally the statement m(ζ)=0. No mechanism is produced — only rigidity. (ii) Dropping
conductor 1 (conductor q, degree 1): Hecke/Hamburger give linear combinations of L(s,χ) — DH lives there with m=∞.
Whether some combination has 0<m<∞ is open (Bombieri–Hejhal heuristics say no); none is known, so no falsifier and
no confirmation. An argument that works at conductor q would have to decide that open question too.
(iii) So any C_B proof must use, beyond Theorem H's hypotheses, a property that distinguishes ζ inside its own
rigidity class — i.e. an individual property of ζ (Euler product with Λ's exact values used nonlinearly). That is
2501 §4 again, now with the reason: atomicity is *fully absorbed* by Hamburger rigidity and adds no inequality.

## 5. Where a theorem could have hidden, and why it collapses

The only candidate mechanism in the task, "real-zero part cannot cancel E's analytic growth off {log n}", is
correct pointwise (Z_R is tempered) but D's growth off {log n} is not an obstruction: off the atoms D equals the
smooth density −P_arch−2cosh, and the growth of E is carried *in average* by the atoms (Thm Λ̃). Distributions
cannot see "off the support" growth of a measure whose local averages grow — atoms at spacing 1/n carry any
density up to tempered error. Real-analyticity of E is irrelevant for the same reason.

## 6. Verdict

**NO-GO (PROVED)** for O2501.1 as an atomic-vs-exponential incompatibility: Thm Λ̃ gives a positive atomic measure on
{±log n} whose non-tempered part is exactly E (killer: new falsifier Λ̃, class W3). **PROVED reductions:** Thm T
(m=0 ⟺ D∈S′, E1 in distribution language); Thm H (atomic + log-derivative + FE ⟹ F=cζ, so C_B has no class
content and must use an individual Euler-product property of ζ). Residual narrowed:
- **O2601.1** (live, 4E/6F): a property of Λ's exact values, used nonlinearly (Euler product), that forbids the
  a.c. part E among functions with atomic log-derivative — must fail for conductor-q combinations if any has
  0<m<∞ (unknown). No candidate.
- O2501.1 closed (as posed: false; as corrected: = O2601.1).
