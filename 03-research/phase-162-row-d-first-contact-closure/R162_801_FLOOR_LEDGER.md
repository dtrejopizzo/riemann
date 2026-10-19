# R162_801 — Round 8: the floor ledger

Round 8, mechanism L.

**Status: NO-GO (PROVED), with four PROVED statements (L1–L4) and one sensitivity theorem (L5).**
The Chebyshev ledger Σ_{n≤x}Λ(n)⌊x/n⌋ = log⌊x⌋!, read uniformly in T, does separate Λ from every
F3 model (L1). But it enters the Weil family in only three ways. Each is already on the dead-end map:
(i) per-window Möbius rewriting (R162_406 §6, R162_502 B2), (ii) Poisson/Stirling on the log comb, which
is the (PC) sawtooth (R162_701, R161_001–002), (iii) dilation of tests, which is a window shift
(R160_D4 Thm 5.1). A non-exact (asymptotic, Stirling-type) use is ruled out by Theorem M (L5): the ledger
defect that has to be detected is ≤ exp(−exp((2−ε)T)) in relative size. Gate 1 stays OPEN.

Notation (R162_404–406): I_T=(−T,T); ℓ_n=Λ(n)n^{−1/2}; c_F = F⋆F̃ is supported in (−2T,2T);
Φ_F(j) = j^{−1/2}(c_F(log j)+c_F(−log j)); W_T(F) = Arch_T(F) − Σ_n Λ(n)Φ_F(n) (polar/Tate terms are in
Arch_T; the argument below does not touch them). For a weight a we write W_T^a with comb Σ a(n)Φ_F(n).
X_T = e^{2T}. Ledger defect: D_a(x) = Σ_{n≤x} a(n)⌊x/n⌋ − log⌊x⌋!.

## 0. Corpus check

- R160_D4 Thm 5.1 / Cor 5.2: convolution identities on tests are window shifts, and finitely many exact
  values of Λ are not enough. So any ledger use that dilates tests is (iii).
- R162_406 §3: at the threshold n_0 = e^{2T_*}, the edge coefficient log n_0 − Σ_{d|n_0,d<n_0}a(d) is the
  ledger increment D_a(n_0) − D_a(n_0−1) (a single threshold). There, Chebyshev is an automorphism of
  𝒟_{T'}. This note sums those increments over all thresholds with floor weights; that sum is new.
- R162_502 B2, R162_701: M_T(Λ) = ZXZ^{−1} − X, and integrality enters only linearly through the sawtooth.
- R162_702: the support class 𝒞 = {a ≥ 0, supp a ⊂ prime powers} contains κ-models with first contacts.
- R161_001–002: joint Poisson–Chebyshev anomaly; canonical square is sign-blind (F2).
- None of these files contains L1, L4 or L5.

## 1. The ledger identifies Λ (PROVED)

**L1.** (a) D_a ≡ 0 on [1,∞) ⟺ a = Λ. More precisely, D_a(N) − D_a(N−1) = (a∗1)(N) − log N.
(b) Let a = Λ + η with η ≠ 0 supported on n ≤ N_0. Then D_a(x) = Σ_{n≤N_0} η(n)⌊x/n⌋ = c_η x − P_η(x),
with c_η = Σ η(n)/n and P_η(x) = Σ η(n){x/n} bounded and periodic mod lcm(n ≤ N_0). If c_η = 0,
D_a is a nonzero bounded periodic function.
(c) κ-model a = κΛ on n ≤ N_0, and a = Λ otherwise: D_a(x) = (κ−1)Σ_{n≤N_0}Λ(n)⌊x/n⌋ ~ (κ−1)x log N_0.
(d) Davenport–Heilbronn: with a_DH the coefficients and Λ_DH := coefficients of −L'/L, the twisted
ledger Σ_{n≤x}Λ_DH(n)A_DH(x/n) = Σ_{m≤x}a_DH(m)log m holds identically, with A_DH(y) = Σ_{m≤y}a_DH(m).
This is the definition of the log-derivative. The ζ-ledger (coefficient 1, floor function) is false for
DH data.

*Proof.* (a) Take differences in x at integers: ⌊N/n⌋ − ⌊(N−1)/n⌋ = 1_{n|N}. Induction on N gives
a∗1 = log, so a = μ∗log = Λ. (b), (c): substitute. (d): −L'·L^{−1}·L = −L', coefficientwise. ∎

So the ledger passes F3 against all three models, at different lines. Finite modification and κ-models
fail at "a∗1 = log", and they fail for all large x, not only near T_*. DH passes its own ledger. It fails
only at "the coefficient sequence of the L-function is 1", i.e. at the Euler product with a ≡ 1
(Λ_DH is not supported on prime powers). This is the uniform-in-T structure the task asked for. The
rest of this note shows that it cannot be moved into the first-contact problem.

## 2. The ledger inside one window (PROVED; = map item (i))

**L2 (Möbius ledger of the comb).** For F ∈ L²(I_T),
  Σ_n Λ(n)Φ_F(n) = Σ_{m<X_T} log m · φ_F(m),   φ_F(m) := Σ_{k<X_T/m} μ(k)Φ_F(mk).
For any weight a: Σ a(n)Φ_F(n) = Σ_m (a∗1)(m)φ_F(m), hence
  W_T^a(F) = W_T(F) − Σ_{m<X_T} [D_a(m) − D_a(m−1)] φ_F(m).

*Proof.* The sums are finite because supp Φ_F ⊂ [1,X_T). Then Φ_F = 1∗φ_F on [1,X_T) (Möbius inversion
restricted to a divisor-closed range), and Σ a(n)(1∗φ)(n) = Σ_m φ(m)(a∗1)(m). ∎

φ_F(m) = ⟨F, M_m F⟩ with M_m = Σ_k μ(k)(mk)^{−1/2}(V_{log mk}+V_{log mk}^*). This is the quadratic form of
Z^{−1} applied to the comb, i.e. B2 of R162_502. **Failing line:** L2 is an identity in the weights. It
holds for every a with a∗1 replacing log, so it contributes no inequality. At a first contact it gives
Arch_{T_*}(F) = Σ log m·φ_F(m), which is H_{T_*}F = 0 restated (F1: the same identity holds on every
eigenvector).

## 3. Floor weights and Stirling = the (PC) sawtooth (PROVED; = map item (ii))

The ledger Σ Λ(n)⌊x/n⌋ = log⌊x⌋! is L2 with φ = 1_{[1,x]}, i.e. Φ(j) = ⌊x/j⌋. Summing the threshold
ledgers against a measure ν(dx) gives L2 with φ(m) = ν([m,∞)). Therefore every floor-weighted threshold
sum is L2 with a nonincreasing φ ≥ 0.

**L3 (Stirling side).** For φ of bounded variation supported in [1,X],
  Σ_{m≤X} log m φ(m) = ∫_1^X φ(u)log u du + ½φ(1)·0 + Σ_{ν≠0} ∫_1^X φ(u) log u · e(νu) du
(Poisson, with the usual half-weight convention at jumps). For φ = 1_{[1,x]} this is Stirling:
x log x − x + 1 + ½log x + (sawtooth series) = log⌊x⌋! up to the fractional-part correction.

Put the L2 profile φ_F into L3 (extend φ_F to real u by the same formula). The result is
W_T(F) = [Arch_T(F) − ∫ φ_F log] − Σ_{ν≠0} ∫ φ_F(u)log u e(νu) du. The first bracket is the
archimedean/pole part the task wanted to match. The second term is the additive Poisson dual. This is
the Poisson–Chebyshev anomaly of R161_001, and R162_701 already showed that integrality enters it only
linearly, through the sawtooth. **Failing line:** the decomposition is linear in c_F, and the sawtooth
series has no sign. Its square is (PC)², which is invariant under A_M → −A_M (F2). No ordering of φ_F
is available either: φ_F is a Möbius transform of an autocorrelation and is indefinite. The only case
with a sign is the floor case φ ↓, ≥ 0, and it is not of the form φ_F for the first-contact vector.
Imposing it is a positivity/support constraint, which κ-models pass (R162_103, R162_702).

## 4. Summing over thresholds in T (PROVED; = map item (iii), plus a concavity lemma)

The two candidate T-families are λ_A(T) (continuous, lem:contA; so it has no jumps) and the
Hellmann–Feynman derivatives ∂λ/∂v_n = −Φ_{ψ_T}(n), where ψ_T is the ground state. Summed over n with
weights Λ(n), these reproduce λ_A(T) − Arch_T(ψ_T) (degree-1 homogeneity in v). With floor/Möbius
weights they reproduce L2 at the single window T. Summing over T to use all thresholds needs a vector
at windows T ≠ T_*. The only arithmetic maps between windows are dilations F ↦ τ_{log k}F. These
send I_{T_*} into I_{T_*+½log k}, and the translation invariance of W makes this a window shift
(D4 Thm 5.1). With Möbius signs μ(k), the transported family is indefinite.

**L4 (concavity in the weights).** a ↦ λ_A(T;a) = inf_{‖F‖=1} W_T^a(F) is concave and nonincreasing in
each a(n) on the cone where Φ_F ≥ 0 matters only through affine pieces. Hence, for a = Σθ_i a_i with
θ_i ≥ 0 and Σθ_i = 1, λ(T;a) ≥ Σθ_iλ(T;a_i).
*Proof.* An infimum of affine functions of a is concave. ∎
**Failing line:** the ledger writes Λ = μ∗log. This is a signed combination, not a convex one, so L4 gives
no lower bound from it. The only convex decompositions available are κΛ = κ·Λ + (1−κ)·0. They reduce to
Arch_T, which is indefinite from T ≈ 0.58 (prop:archneg). L4 holds for every weight (F1/F3-blind).

## 5. Sensitivity: an asymptotic use of the ledger is impossible (PROVED modulo Theorem M)

**L5.** Fix T large and a prime p with ½log p < T − 1. Suppose there is F ∈ L²(I_T) with ‖F‖ = 1,
W_T(F) ≤ 2m(T), where m(T) ≤ exp(−exp((2−ε)T)) (Theorem M), and Φ_F(p) ≠ 0. This holds after an
arbitrarily small perturbation within near-minimisers, because {Φ_F(p) = 0} is a real quadric.
Then there is ε_p with |ε_p| ≤ 3m(T)/|Φ_F(p)| such that a = Λ + ε_pδ_p has λ_A(T;a) < 0. So a first
contact T_*(a) ≤ T exists. Its ledger defect is D_a(x) = ε_p⌊x/p⌋, so sup_x |D_a(x)|/x ≤ |ε_p|/p.
*Proof.* W_T^a(F) = W_T(F) − ε_pΦ_F(p). Choose sgn ε_p = sgn Φ_F(p). Then use L1(b). ∎

Consequence: to exclude this model, a ledger mechanism must detect a relative defect of size
≲ exp(−exp((2−ε)T)) in the identity Σ Λ(n)⌊x/n⌋ = log⌊x⌋!. Stirling expansions have power-type errors
in x, so they cannot see it. The ledger can therefore enter only exactly, i.e. as an identity, and
§§2–4 show the exact entries are (i)–(iii). This is the ledger form of the Theorem-M kill ("estimates
die by Theorem M").

## 6. Verdict and the declared failing lines

| model | ledger line | result |
|---|---|---|
| DH | "coefficients ≡ 1, Λ_a supported on prime powers" (L1(d)) | ζ-ledger false; own ledger true |
| κ-model a = κΛ, n ≤ N_0 | "a∗1 = log" (L1(c)); defect (κ−1)x log N_0 for all x | fails for all large x |
| finite modification η | "a∗1 = log" (L1(b)); defect c_ηx − P_η(x) | fails; can be ≤ e^{−e^{2T}}·x (L5) |

The ledger detects every falsifier, but only as a property of the weights, not of a vector. The route
from the weights to the first-contact vector runs through L2 (identity, F1), L3 (linear sawtooth, F2)
or dilation (window shift, D4). Uniqueness in L1(a) shows "ledger ⇒ no first contact" is
equivalent to RH for ζ (E1). No first-contact mechanism violating the ledger exists at the level of
identities or estimates.

**Residual (not claimed):** a mechanism would need to use the ledger *nonlinearly and exactly*. One
example is the integer-valuedness of D_a jointly with the Möbius profile of ψ_{T_*} at infinitely many
thresholds. Such a step must not factor through L2 or L3. No candidate is known. Add to R162_590 §1c:
"floor ledger / Stirling matching — R162_801 — Möbius automorphism + (PC) sawtooth + window shift;
asymptotic use killed by L5 (Theorem M) — F1, F2, M".
