# Round 3, option 5 — the virial pair: selection

Selection memo, not a construction memo. Notation of `../phase-211-sign-sandbox/STATEMENT_001.md`;
N = e^{2T}. Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.
Question: is there an exact commutator or virial identity on all of P_T,
a_T(F) = (commutator form with the dilation generator) + ρ_T(F), or a quantity monotone in T,
in which m′ and the weights Λ(n) log n enter with signed orientation and whose exactness uses
Σ_{d|k}Λ(d) = log k?

## Cross-check

### What was searched and where

Case-insensitive grep for «virial», «pohozaev», «morawetz», «mourre», «positive commutator»,
«conmutador», «hellmann», «dilat», «monoton», «Grönwall», «Hadamard» in all of `03-research/`, in
`04-papers/47*` and `48*`, in the routes index (README and catalogues 01–06), in the grid and in the
crossword, and reading of `RULES_AVOID.md` §§B4, C1, D9, I3–I5, I8. There were more than forty files with
hits. Read in primary: R170_840 (§0 and §§8–9 in full); R162_501 (in full);
106_124 §§1–2; P121_COMMUTATOR_MOMENT_TOMOGRAPHY_NO_GO (in full); P124_007 (verdict and §1);
R165_202 (table 1.4–1.9); 211/ROUND_008_C (§§0–2 and statements of Props. 3–6); IDX README, phase 193,
front I. Not read line by line: 106_105, 106_119, 106_41, R162_407, R162_408 nor the G2_* of
phase 159. That they were not read does not prove they do not contain the idea.

### (1) Closest antecedents, read in primary

- **R162_501, Theorem 2.2 (Selberg–virial), PROVED under (REG) on the radical.** It is precisely the
  question of this zone. The weight Λ(n) log n of the derived comb is rewritten with
  Λ·log + Λ∗Λ = W := μ∗log². That identity comes from multiplying Λ∗1 = log by the derivation log, so
  it uses Σ_{d|k}Λ(d) = log k. The kernel equation absorbs the square Λ∗Λ. Prop. 3.1: no
  term has a determined sign, and the reformulation (S-W) is equivalent to 𝒱|_N ≤ 0, that is to
  VIR–LB. Falsifiers: the argument falls for Davenport–Heilbronn only at the line W ≥ 0, and **does not
  fall** for finite modifications Λ + η with η ≥ 0.
- **106_124 §1.** With the complete generator, the dilation commutator has even parity. Each
  prime power contributes the isolated distribution log n·{δ′_{log n} − δ′_{−log n}}, and the commutator
  is unbounded in both signs on the even smooth core. Projecting the dilation gives a non-local
  conjugate. Below the threshold, a strict Mourre estimate for it is equivalent to the absence of the
  states one wanted to exclude.
- **R170_840 §8, Prop. 8.1 (PROVED).** VIR–LB and VIR–DET together force R_LG = 0 at a supposed first
  window. Both remain OPEN, as do (REG) and uniformity in T. The memo itself says that
  the pair «has exactly the strength needed» for the closure (§8, after (8.6)).
- **Monotonicity and derivative in T.** R165_202 1.4 gives the Hellmann–Feynman formula
  D⁺λ ≤ −𝒱_T(F_T)/T ≤ D₋λ (PROVED under (REG)), and its 1.5 gives the Hadamard principle (ARGUED).
  In 211/ROUND_008_C, Theorem 1 is the version with Tate multipliers and Prop. 5 proves that
  Grönwall in T and (EB_C) are reformulations of (★) plus a rate (PROVED). R186_038 α.3 is
  recorded as NO-GO (vacuous). PROOF_L_SHARP_H_001 defines the class 𝒦_H, NO-GO ARGUED.
- **Commutators with the position.** In P121 one has ad_Q(S_a) = −aS_a. On the radical, simple
  commutators give no information; the double commutator gives ⟨QF, HQF⟩ ≥ 0 and the route is
  withdrawn. P124_007: the commutator with the Tate multiplier cancels with the projection
  defect.
- **IDX README, phase 193, front I:** «Virial/Pohozaev (holds for every comb, DH included) … dead».

### (2) Genuinely new object

**There is none I can write with a sign mechanism.** The question asks for an exact form
on all of P_T and not only on the radical. In that form the only thing new, relative to the antecedents,
is what the two lemmas of §1 delimit: a commutator form with translation-invariant
multipliers is a tautology (Lemma 1), and the identity a_T = κ·𝒱 + ρ with ρ bounded below is
false (Lemma 2). The Selberg–virial identity on all of P_T is that of R162_501 without step 5, that is
without the kernel equation. In its place a cross pairing −⟨τ Im z_c F, S_T F⟩ without
sign appears, of the same type as the residue of I4 (§2). ℋ_T, V_T and ρ_T are not written.

### (3) Why the change does not avoid the difficulty of the antecedent

On the radical, the kernel equation is what turns Λ∗Λ into archimedean data (R162_501,
step 5). Outside the radical that step does not exist, and the square of the comb returns as an unsigned cross term
with S_T. Passing from the radical to all of P_T worsens the difficulty: the comb term of the virial is not
relatively bounded by a_T (Lemma 2). No identity of the requested form can have a remainder
bounded below.

### (4) Identity or inequality that would connect with global positivity

The only exact identities connecting the virial with λ_A are the variation formula in T
(R165_202 1.4; 211/ROUND_008_C Thm. 1) and the sufficiency VIR–EP ⟹ R_LG = 0 (R170_840 Prop. 8.1).
Both live on minimizers or vectors of the radical. On all of P_T, the inequality
«a_T ≥ κ𝒱 − C‖·‖²» is false for every κ ≠ 0 and every C when T > ½ log 2 (Lemma 2). The
Grönwall version is proved to be a reformulation of (★) plus a rate (211/ROUND_008_C Prop. 5).

Weaker or equivalent? VIR–EP is quantified over supposed first-contact windows.
When there is no contact it is vacuous, so it does not give an intermediate statement that can be proved
separately. Its content, together with (REG), is that of the closure (R170_840 §8; CITED). The global form
a_T = κ𝒱 + ρ, ρ ≥ 0, is neither weaker nor equivalent: it is **false** (Lemma 2).

### (5) Lines that break for cΛ and a_P

In the Selberg–virial identity, the only line that distinguishes the weights is W_a := a·log + a∗a = μ∗log².

- **cΛ, c ≠ 1:** W_{cΛ}(p) = c log²p ≠ log²p, and W_{cΛ}(pq) = 2c² log p log q. The identity
  W_a = μ∗log² fails at n = p for every c ≠ 1 (PROVED, by direct computation).
- **a_P:** W_{a_P}(n) = W(n)·1[all prime factors of n are ≥ P] (Lemma 3). The identity fails
  exactly at n = p < P and at the n with some small prime. The structural properties
  (W1)–(W3) of R162_501 are preserved on the support. The separation is «knowing Λ on [2,N)», that is
  linear identification, already recorded (RULES_AVOID I2, K4).

What does not break: the sign. No signed orientation of the virial comes from these lines
(R162_501 Prop. 3.1), and the falsifier Λ + η, η ≥ 0, already makes any sign based on W ≥ 0 fail.

**Cross-check verdict: repetition.** By rule 3 of the brief, the memo would end here. Only
the three short and complete lemmas that delimit the class are added, because they answer the question «on all of P_T».

## 1. Two format lemmas

Let D be the unitary generator of dilations, (U_rF)(t) = r^{−1/2}F(t/r). In Fourier,
(U_rF)^(τ) = r^{1/2}F̂(rτ). For real F with c_F ∈ C¹ (for example F ∈ C_c^∞(I_T)) define

    𝒱_T(F) := (1/2π)∫ τ s_T′(τ)|F̂(τ)|² dτ
            = (1/2π)∫ τ m′(τ)|F̂|² dτ − Σ_{log n<2T} v_n log n · c_F′(log n).

The equality holds because 2π c_F(u) = ∫ cos(τu)|F̂|², whence ∫ τ sin(τu)|F̂|² = −2π c_F′(u). It is the
virial of R170_840 (8.1) without the Tate term of the radical. Moreover
𝒱_T(F) = −(d/dr)|_{r=1} (1/2π)∫ s_T(τ)|(U_rF)^(τ)|² dτ: it is the form ⟨F, i[D, S_T]F⟩ with the
sign convention of R162_407.

**Lemma 1 (tautology in the multiplier class; PROVED).** Let s be a real, even and
continuous function. Let x(τ) := ∫_1^{|τ|} s(σ)σ^{−1} dσ for τ ≠ 0. Then τ x′(τ) = s(τ) for every τ ≠ 0 and
⟨F, i[D, X]F⟩ = (1/2π)∫ s|F̂|² for every F with ∫ |s||F̂|² < ∞, where X is the multiplier of symbol
x and the commutator is understood in the sense of forms. In particular, for any sequence of weights
a one has a_T^{(a)}(F) = ⟨F, i[D, X_a]F⟩ with ρ = 0.

*Proof.* For a multiplier X of symbol x, U_r X U_r^{−1} is the multiplier of symbol
x(τ/r). Differentiating at r = 1 gives the symbol −τx′(τ) for i[D,X], up to the sign convention
fixed above. By construction τx′ = s, and the form is (1/2π)∫ s|F̂|². ∎

Consequence. In the class of commutators of D with translation-invariant multipliers, every
identity «a_T = commutator + ρ» is a splitting of the symbol s_T = σ₁ + σ₂. It holds for every comb, so
that it does not break for cΛ nor for a_P (pattern B1), and the sign of the commutator is literally (★).

**Lemma 2 (the virial is not relatively bounded by a_T on P_T; PROVED).** Let T > ½ log 2. For
every κ ∈ ℝ∖{0} and every C ≥ 0 there exists G ∈ P_T ∩ C_c^∞(I_T) with a_T(G) − κ𝒱_T(G) < −C‖G‖². Therefore
there is no exact identity a_T = κ𝒱_T + ρ_T on P_T ∩ C_c^∞ with ρ_T ≥ −C‖·‖².

*Proof.* Let ℓ = log 2. Let φ ∈ C_c^∞(−1, 1) be real with ‖φ‖ = 1. Then c_φ is even, of class
C¹ and non-constant, so there exists θ with c_φ′(−θ) ≠ 0. Since c_φ′ is odd, the sign of c_φ′(−θ)
is chosen by replacing θ with −θ. Let φ_ε := ε^{−1/2}φ(·/ε). For small ε take

    F_ε(t) = φ_ε(t − t₀) + φ_ε(t − t₀ − ℓ − εθ),

with t₀ such that the support lies in I_T; this is possible because ℓ < 2T. One has
c_{F_ε}(u) = 2c_φ(u/ε) + c_φ((u − ℓ − εθ)/ε) + c_φ((u + ℓ + εθ)/ε). The log n with n ≥ 2 are
separated from each other and from 0. For small ε, the only one that falls in a support is log 2, through the second
summand. Thus c_{F_ε}′(log n) = 0 for n ≠ 2, c_{F_ε}′(ℓ) = ε^{−1}c_φ′(−θ) and c_{F_ε}(ℓ) = c_φ(−θ).

Primitive correction. Fix ψ₁, ψ₂ ∈ C_c^∞(I_T) with det[(A,B)(ψ_i)] ≠ 0; they exist because A and B are
linearly independent on C_c^∞(I_T). One has |A(F_ε)|, |B(F_ε)| ≤ 2e^{T/2}‖φ‖₁ε^{1/2}.
Then G_ε = F_ε − α_εψ₁ − β_εψ₂ ∈ P_T with α_ε, β_ε = O(ε^{1/2}).

Estimates:
- s_T′ = m′ + Σ v_n log n sin(τ log n) is bounded (m′(τ) = O(1/(1+|τ|)), CITED from
  211/ROUND_008_C Lemma 1.2). Hence |𝒱_T(F,ψ)| ≤ C‖F‖‖τψ̂‖ = O(1), and
  𝒱_T(G_ε) = −v_2 ℓ c_φ′(−θ)/ε + O(1).
- m(τ) ≤ C₁ + log(1 + |τ|) and (1/2π)∫ log(1+|τ|)|F̂_ε|² = O(log(1/ε)), while the comb
  terms are bounded. Hence a_T(G_ε) = O(log(1/ε)), and ‖G_ε‖² → 2.

Choose the sign of c_φ′(−θ) so that κ𝒱_T(G_ε) → +∞ like 1/ε. Then
a_T(G_ε) − κ𝒱_T(G_ε) → −∞, faster than any −C‖G_ε‖². ∎

Scope. Lemma 2 uses only v_2 ≠ 0. It is a format obstruction, generic in the comb and without sign,
like the lemma of K1′. It coincides in content with the sentence of 106_124 §1 («unbounded in both signs on
the even smooth core»), but here it is stated for a_T on P_T and with a written proof. **It does not
exclude:** generators other than D (for example dilations with arithmetic weight, or the
multiplicative generator log x · x d/dx in other coordinates); commutators with non-translation-invariant
operators that are not pure dilation (the window, the Tate defect, U_n); remainders ρ_T not bounded
below but with sign on P_T; combinations κ(T)𝒱_T with κ depending on F or non-linear;
identities only on proper subspaces; and the radical version (VIR–LB/VIR–DET), which remains OPEN.

## 2. Selberg–virial on all of P_T (ARGUED, steps 1–4 of R162_501 without step 5)

For real F ∈ P_T with c_F ∈ C¹, and z_c, Y, W as in R162_501, steps 1–4 do not use the kernel
equation. They give

    𝒱_T(F) = (1/2π)∫ τ m′|F̂|² − (1/π)∫ τ Im Y |F̂|² + (1/π)∫ τ Im z_c · m |F̂|²
             − (1/π)∫ τ Im z_c · s_T |F̂|²                     (+ threshold term if 2T = log n₀).

The last term is the cross pairing −(1/π)Re⟨M_{τ Im z_c}F, S_T F⟩. On the radical, S_T F
falls in the Tate space and in the exterior leakage; here it has no sign. It is the same format
«−Re⟨X F, S_T F⟩ without sign and with only a two-sided bound» of RULES_AVOID I4. It holds for every comb a with
W_a in place of W (R162_501 §3, DH line), so it is not new and carries no sign.

**Lemma 3 (W of a_P; PROVED).** For a_P := Λ·1[p ≥ P] (powers of primes p < P erased),
W_{a_P} := a_P·log + a_P∗a_P = W·1[every prime factor of n is ≥ P].

*Proof.* If p ≥ P, then a_P·log(p^k) = k log²p and a_P∗a_P(p^k) = Σ_{i=1}^{k−1}(log p)² =
(k−1)log²p; the sum is (2k−1)log²p = W(p^k). If p, q ≥ P are distinct, a_P∗a_P(p^iq^j) =
2 log p log q = W(p^iq^j), and a_P·log vanishes there. If ω(n) ≥ 3, both summands are 0. If n has a
prime factor less than P, a_P(n) = 0 or n is not a prime power, and every pair d·(n/d) with a_P(d)a_P(n/d)
≠ 0 has both factors without small primes; hence both summands are 0. ∎

Reading. For a_P, the Selberg identity fails only by support, never by structure. The Selberg
virial distinguishes Λ from a_P only by the values at the n with small primes, which is linear
identification. For cΛ it fails in the value and in the degree (c versus c²), but remains without sign.

## Result

No new mechanism; repetition of R162_501, 106_124, R170_840 §8, R165_202, 211/ROUND_008_C and
P121. Two short lemmas are added that delimit the question «on all of P_T»: a class NO-GO (Lemma 2)
and a class tautology (Lemma 1). There is no candidate ready for construction.

## What was proved

- Lemma 1 (PROVED): in the class of commutators of D with multipliers, the identity
  a_T = commutator is tautological and generic in the comb, and its sign is literally (★).
- Lemma 2 (PROVED, NO-GO with class): for T > ½ log 2 there is no a_T = κ𝒱_T + ρ_T with κ ≠ 0 and
  ρ_T ≥ −C‖·‖² on P_T ∩ C_c^∞. The virial of the comb is unbounded in both signs relative to a_T.
- Lemma 3 (PROVED): W_{a_P} = W·1[primes ≥ P]. The a_P line in the Selberg virial is only support.

## What failed and why

Outside the radical, the square Λ∗Λ produced by Σ_{d|k}Λ(d) = log k cannot be absorbed: it returns as
an unsigned cross term with S_T. The virial has growth |τ| in the comb versus log|τ| in a_T, which
prevents any identity with remainder bounded below. On the radical, the pair VIR–LB/VIR–DET has the
strength of the closure and remains OPEN, with no object that orients it.

## Concrete next step

Do not relaunch the pure-dilation virial on P_T. A single reopening remains that Lemma 2 does not
exclude and that has an explicit operation: replace D by a generator whose commutator with the comb
is relatively bounded by a_T. That requires the δ′ term at log n to be compensated within the
generator itself, for example a generator with arithmetic damping at each log n. Before
deriving anything, such a candidate has to write the generator and show the relative bound. The cross-check
of that idea against 106_124 §§3–8 (complete generator, projected conjugate) remains pending and has not
been done here.
