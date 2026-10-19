# R164_401 — O164.101, construction side: the positive witness class is {ζ} (Beurling–Hamburger rigidity)

*Phase 164, round 2, construction side of O164.101 ≡ O164.102.1. Pure mathematics, no numerics, no commits. Only this file was written. No label of record changes.*
*Read first: R164_190 (round-1 synthesis), R164_102 (Thm L, Cor L.1, Thm A, Prop W, Thm H, Prop I), R164_101 (Prop D, Prop θ), R163_901 (Lemma 2.1, Thm F).*
*Corpus check.* I grepped for "self-dual / autodual / Poisson / sinc / positive-definite" in phases 160–164. The self-dual measure appears only in R163_901 (Lemma 2.1, Thm F.1), where it is used to **build** FE solutions (signed). Nobody has used the **sign** of the self-dual measure. The sinc-annihilation step below is the Cohn–Elkies / linear-programming device for lattices, applied here to the theta measure. Novelty: not found in this form. The ingredients are classical (Bochner 1951, Chandrasekharan–Narasimhan 1961, Hamburger, Cohn–Elkies). The result is close to Córdoba 1989 and Kahane–Mandelbrojt 1958 and is plausibly folklore. It is labelled PROVED, not PROVED-CITED.

## 0. Status table

| # | statement | label |
|---|---|---|
| Lem 1 | (Hecke–Bochner dictionary) ξ_f has ζ's FE, Γ_ℝ, polar data and finite order ⟺ the even theta measure m_f = δ_0 + N + Ň is tempered and satisfies m̂_f = m_f | PROVED (Riemann's proof run in reverse; Bochner 1951, Chandrasekharan–Narasimhan 1961 for general frequencies: CITED as the standard reference) |
| Lem 2 | (sinc annihilation) if m ≥ 0 off ℤ, m̂ = m, and m = Σ_{n∈ℤ}δ_n on (−X,X) for some X>1, then m is supported on ℤ | PROVED |
| Lem 3 | a self-dual tempered measure supported on ℤ with mass 1 at 0 equals the Dirac comb | PROVED |
| **Thm R** | (rigidity) Let f(s)=∫_{[1,∞)}λ^{-s}dN(λ) be absolutely convergent for σ>1, with N({1})=1. Suppose (a) N = N_ζ on [1,X) for some X>1, (b) **N ≥ 0 on [1,∞)∖ℕ**, (c) Λ_f(s)=π^{-s/2}Γ(s/2)f(s) has ζ's FE, has **the same polar data as ζ** (simple poles at 0 and 1 only, with Res_{s=1}Λ_f = 1 and Res_{s=0}Λ_f = −1), and s(s−1)Λ_f is of finite order. The residue is essential: a residue r ≠ 1 makes m̂_f = m_f + (r−1)δ₀-type, which puts (r−1)δ₀ inside the window and breaks the hole of Lemma 2. Then f = ζ. | PROVED |
| Cor R.1 | every Beurling zeta ζ_B=exp(∫e^{-su}dμ_B), μ_B ≥ 0, with ζ's window μ_B=μ_ζ on (0,L], L>0, and ζ's Γ_ℝ, FE, polar data and finite order **is ζ**. The witness class of O164.101 is the singleton {ζ} | PROVED |
| Cor R.2 | O164.101 ("is there a member with an off-line zero?") ⟺ ¬RH. The construction side is **CLOSED NEGATIVE** (no member other than ζ exists). The obstruction side does **not** follow: "no member has an off-line zero" is RH itself. This is the identification wall W-identification, not a class lemma for RH | PROVED |
| Cor R.3 | strategies (1)–(3) of the brief are all impossible. (1) For every t≠0, f_t=ζ+tg (R163_901) has a negative Dirichlet coefficient off ℕ. (2) Q=ζ_B/ζ ≡ 1. (3) No continuous Beurling density can satisfy the FE. | PROVED |
| Falsifiers | f_t, ζ_θ, Thm A, Dedekind ζ_K, Prop D deletion, Λχ₂: none contradicts Thm R (§4) | PROVED (by inspection of hypotheses) |
| (★_cell), (TC), row D | | **OPEN** |

**Verdict.** O164.101 is decided as a **class question**: the class contains exactly one member, ζ. Inside it, the off-line-zero question is RH verbatim. The whole of L1 (positivity of the tail, read in the witness class) therefore collapses into identification (pattern of Thm O / W3′, R163_1001). L1 is **DEAD (identification)**: positivity plus window plus FE carries no information beyond "this is ζ". No label moves. RH is neither proved nor contradicted.

---

## 1. The dictionary (Lemma 1)

Let N ≥ 0 or signed with |N|(λ ≤ x) ≪ x^{1+ε}, N({1}) = 1, supp N ⊂ [1,∞), and f(s)=∫λ^{-s}dN. Put Θ_N(x)=∫e^{-πλ²x}dN(λ), and let m := δ_0 + N + Ň (Ň = reflection) be the even tempered measure on ℝ, so that Θ_m(x) := ∫e^{-πy²x}dm(y) = 1 + 2Θ_N(x).

**Lemma 1. PROVED (standard).** Under (c) of Thm R, Θ_m(1/x) = √x Θ_m(x) for all x>0, and therefore m̂ = m as tempered distributions. Conversely, m̂ = m implies (c).

*Proof.* For σ>1 we have ξ_f(s) = π^{-s/2}Γ(s/2)f(s) = ∫_0^∞ Θ_N(x) x^{s/2} dx/x (Fubini; for signed N use |N|). Mellin inversion gives Θ_N(x) = (1/2πi)∫_{(c)} ξ_f(s)x^{-s/2}ds, c>1. ξ_f decays exponentially on σ=c (Stirling) and, by the FE, on σ=1−c. Finite order of s(s−1)ξ_f plus Phragmén–Lindelöf gives decay uniformly in the strip, so the contour can be moved to σ=1−c. The residues at s=1 and s=0 are those of ξ, namely 1/(s−1) and −1/s. With the factor ds/2 of the inversion in s/2, they contribute ½x^{-1/2} and −½. Using the FE on the new line gives Θ_N(x) = x^{-1/2}Θ_N(1/x) + ½x^{-1/2} − ½, which is Θ_m(x) = x^{-1/2}Θ_m(1/x).

For the distributional statement, let γ_x(y) = e^{-πxy²}. Then γ̂_x = x^{-1/2}γ_{1/x}, so ⟨m̂,γ_x⟩ = ⟨m,γ̂_x⟩ = x^{-1/2}Θ_m(1/x) = Θ_m(x) = ⟨m,γ_x⟩. Hence D := m − m̂, an even tempered distribution, annihilates every γ_x. Difference quotients in x converge in 𝒮, so D also annihilates ∂_x^kγ_x|_{x=1} = (−πy²)^k e^{-πy²}. Their span is the span of the even Hermite functions, which is dense in 𝒮_even. D is even, so it kills odd functions as well. Hence D = 0. The converse is Riemann's proof. ∎

(This is the measure form of Bochner's "modular relation ⟺ functional equation", valid for arbitrary real frequencies and for continuous N. It is the same identity that R163_901 Thm F.1 uses in the other direction.)

## 2. Sinc annihilation and rigidity

Let 𝖢 = Σ_{n∈ℤ}δ_n (the comb, = m_ζ).

**Lemma 2. PROVED.** Let m be an even tempered real measure with m̂ = m. Let X>1. Suppose m = 𝖢 on (−X,X), and m ≥ 0 on ℝ∖ℤ (that is, m(A) ≥ 0 for every Borel A ⊂ ℝ∖ℤ). Then supp m ⊂ ℤ.

*Proof.* Put η = m − 𝖢. Then η̂ = η (both m and 𝖢 are self-dual), and η = 0 on (−X,X). Write η = η₊ − η₋ (Jordan). On ℝ∖ℤ we have η = m ≥ 0, so **η₋ is carried by ℤ∖(−X,X)**.

Fix 0 < a < (X−1)/2 and χ ∈ C_c^∞(−a,a). Put ψ = 1_{[−½,½]} * χ ∈ C_c^∞(−X/2, X/2), ψ̃(y) = conj ψ(−y), and φ = ψ*ψ̃ ∈ C_c^∞(−X,X). Then φ̂ = |ψ̂|², with
  ψ̂(ξ) = (sin πξ / πξ) · χ̂(ξ), which vanishes at every n ∈ ℤ∖{0}.
Self-duality and the hole give
  ∫|ψ̂|² dη = ⟨η, φ̂⟩ = ⟨η̂, φ⟩ = ⟨η, φ⟩ = 0, since supp φ ⊂ (−X,X).
The integral against η₋ vanishes, because η₋ lives on ℤ∖{0} where ψ̂ = 0. So ∫ sinc²(ξ)|χ̂(ξ)|² dη₊(ξ) = 0. Since η₊ ≥ 0, η₊ is carried by (ℤ∖{0}) ∪ Z(χ̂).

Now take χ₁ ∈ C_c^∞(−a,a), χ₁ ≠ 0, and χ₂(y) = e^{2πiby}χ₁(y). Then Z(χ̂₂) = Z(χ̂₁) + b. Z(χ̂₁) is countable, because χ̂₁ is entire and nonzero, so we can choose b ∉ Z(χ̂₁) − Z(χ̂₁) and make the two zero sets disjoint. So η₊ is carried by ℤ∖{0}. Both η₊ and η₋ are then carried by ℤ, and so is m = 𝖢 + η. ∎

**Lemma 3. PROVED.** If m = Σ_{n∈ℤ} a_nδ_n is tempered, m̂ = m and a_0 = 1, then a_n = 1 for all n.

*Proof.* m̂(ξ) = Σa_n e^{-2πinξ} is invariant under ξ ↦ ξ+1 as a distribution. So m = m̂ is 1-periodic, which means a_{n+1} = a_n. ∎

**Theorem R. PROVED.** Under (a), (b) and (c), f = ζ.

*Proof.* By Lemma 1, m_f is tempered (absolute convergence for σ>1 gives |N|[1,x] ≪ x^{1+ε}) and self-dual. By (a), m_f = 𝖢 on (−X,X). By (b), m_f ≥ 0 off ℤ (the atom δ_0 sits at 0 ∈ ℤ). Lemmas 2 and 3 then give m_f = 𝖢, so N = N_ζ and f = ζ. ∎

**Remarks.** (i) Hypothesis (b) needs only positivity **off ℕ**. On the integers above X any signs and sizes are allowed. Theorem R is therefore strictly stronger than the Beurling-positive statement. Hamburger's theorem is the special case where N is supported on ℕ, and it also follows from Lemma 3.
(ii) The window enters only through the gap: (a) is used only to know m_f = 𝖢 on (−X,X) for *some* X>1, so any window length L>0 suffices. The values Λ(n), n<X, are never used.
(iii) The Γ-factor is used only through γ̂_x = x^{-1/2}γ_{1/x}. For Γ_ℝ(s+1), with odd measures and ye^{-πxy²}, the same proof works verbatim with the odd comb. Other Γ-factors (Γ_ℂ, products) break Lemma 1 as stated (§4, Dedekind).

## 3. Consequences for O164.101

**Cor R.1. PROVED.** Let ζ_B = exp(∫_0^∞ e^{-su}dμ_B) with μ_B ≥ 0, ∫e^{−σu}dμ_B < ∞ for every σ>1 (absolute convergence), μ_B = μ_ζ on (0,L] for some L>0, and with ζ's Γ_ℝ, FE, polar data and finite order. Then ζ_B = ζ.
*Proof.* N_B = exp^{*}(μ_B) (multiplicative-convolution exponential) is ≥ 0, so (b) holds everywhere. Its restriction to [1,e^L) is determined by μ_B|_{(0,L)}, which equals μ_ζ there, so (a) holds with X = e^L. Apply Theorem R. ∎

**Cor R.2. PROVED.** The witness class of O164.101 / O164.102.1 is {ζ}. Hence:
- Construction side: **CLOSED NEGATIVE.** No ζ_B ≠ ζ exists, with or without an off-line zero, in any cone.
- Obstruction side: "no member has an off-line zero" is literally RH. Theorem R gives no information on it. This is **not** a class lemma implying RH. It is the wall W-identification (R164_102 §7; Thm O / W3′ of R163_1001): the class is cut down to ζ and the question returns unchanged.
- Witness/cone: vacuous. The only member is ζ, and its witness is ζ's (Prop W is trivial now).

**Cor R.3. PROVED.** The brief's three strategies:
1. **f_t of R163_901.** The coefficient of f_t at the irrational frequency m/√M is t c(m). By Lemma 2.1, Σ_{r mod M}c(r) = 0 with c ≠ 0, so c changes sign on every period. Hence for every t ≠ 0 some coefficient off ℕ is negative. f_t is never a Beurling zeta, and it already fails the weaker hypothesis (b). This upgrades R164_102 §5 "Note on f_t" from ARGUED to **PROVED**, and in a stronger form than "−f_t′/f_t not positive". Lemma 2 says this is forced: any FE solution ζ + h with h supported off ℕ and agreeing near 0 must have h with negative coefficients off ℕ.
2. **Multiplicative modification.** Q = ζ_B/ζ ≡ 1. Bochner's infinite-dimensionality of the FE solution space is real, but the space meets the cone {N ≥ 0 off ℕ} ∩ {window} only at ζ. The solution space is infinite-dimensional; its positive window section is a point.
3. **DMV-type continuous densities.** A continuous part of N is a part of m off ℤ. Lemma 2 kills it, so no continuous Beurling prime density is compatible with ζ's FE, Γ_ℝ, poles and a gap above 1. Thm A of R164_102 escapes only because it breaks the FE and the polar data.

**Sharpening of Thm H / Cor L.1 (recorded).** Thm H ("ζ_B/ζ must have infinitely many zeros/poles") and Cor L.1 ("ν₋ ≠ 0 needed") were necessary conditions. Theorem R says they cannot be met at all in the positive class. The deletion of Euler mass above X that Cor L.1 demands is possible only at integers (where Lemma 2 allows η₋). Even there, Lemma 3 forces the deletion to be zero, because a self-dual measure on ℤ is periodic.

## 4. Mandatory falsifier checks (Theorem R must not contradict any of them)

| System | Hypothesis of Thm R it violates | Consistent? |
|---|---|---|
| f_t (R163_901), t≠0 | (b): t c(m) < 0 for some m (sign change of c) | yes. Exact FE, exact window, off-line zeros, but not positive off ℕ. This is exactly the escape Lemma 2 leaves open |
| ζ_θ (Broucke, R163_101) | (c): no Γ_ℝ FE about ½ (symmetry about (1+θ)/2) | yes |
| Thm A ζ·E (R164_102) | (c): double pole at 1, new arch term, no FE | yes |
| Dedekind ζ_K | (c): Γ_ℝ^{r₁}Γ_ℂ^{r₂}·|d_K|^{s/2}, not Γ_ℝ. Lemma 1 is false for it (its theta lives on ℝ^{n}) | yes. Positive, FE, other Γ: not a counterexample |
| Prop D deletion Λ1_{n≥5} | (c): no FE | yes |
| Λχ₂, L(s,χ) | (b) fails (χ(n)<0), and the conductor/Γ differ | yes |
| ζ₀^K = ζ·S₁^K·P₀/P (R162_2901 Thm B) | (c): pole of order K+1 at 1, double zero of order 2K at ½. It is positive and has ζ's FE, but the polar data are wrong. Note that m_f is then not self-dual with ζ's residues: the Θ relation acquires a polynomial-in-log x term | yes. Thm R also proves, in the infinite and positive-off-ℕ form, the "C_B" statement that R162_2901 §5 asks for (simple pole ⇒ zero continuous part), with no exponential-polynomial restriction |
| ζ = Z₀K, K positive, no FE (R163_002 §2) | (c) | yes |
| ζ itself | satisfies all | yes (the unique member) |
| Signed scaled lattices α^{1/2}𝖢_α + α^{-1/2}𝖢_{1/α} added to 𝖢 | adds positive mass at 0, so it breaks (a)/polar data. Removing that mass needs negative mass at 0, which breaks the hole | yes |

No falsifier contradicts Theorem R. The audit should check the following steps.
- Lemma 1, the contour shift. This needs finite order, which (i) of the brief and Thm H assume.
- The sign bookkeeping in Lemma 2: η₋ is carried by ℤ because m ≥ 0 and 𝖢 is carried by ℤ.
- The choice a < (X−1)/2, which is where X > 1 is used.

## 5. Grid cells

- **4F** (Euler product × global transforms in T). O164.101 / O164.102.1 is **closed by identification** (Thm R). The L1 route "positive tail in the witness class" is **DEAD [W-identification]**. PROVED-TOOL: Thm R (positive-off-ℕ Beurling–Hamburger rigidity). Symbol: no change. The cell keeps its other live residues; per rule §8.3 the editor decides.
- **5G** (integrality of ℤ × L-families/fields). New PROVED-TOOL. **Integrality of the frequency support is forced, not assumed**: positivity off ℕ, the gap and the FE push the support onto ℤ (Lemma 2), and self-duality then fixes the weights (Lemma 3). Consequence for BF_θ^disc: no discrete Beurling system with ζ's FE other than ζ. The BF_θ^disc question is untouched, because it has no FE. Symbol: no change.
- Wall used: **W-identification** (as in Prop I / Thm O). New falsifier statement: f_t is the canonical escape (signed off ℕ).

## 6. Ledger

| Id | Content | Label |
|---|---|---|
| R164_401.L1 | FE + Γ_ℝ + polar + finite order ⟺ self-dual theta measure (general real/continuous frequencies) | PROVED (standard; Bochner, Chandrasekharan–Narasimhan as reference) |
| R164_401.L2 | sinc annihilation: self-dual, ≥ 0 off ℤ, = comb on (−X,X), X>1 ⟹ supported on ℤ | PROVED |
| R164_401.L3 | self-dual measure on ℤ with a_0=1 is the comb | PROVED |
| R164_401.R | Thm R: positive-off-ℕ rigidity ⟹ f = ζ | PROVED |
| R164_401.R1 | witness class of O164.101 = {ζ} | PROVED |
| R164_401.R2 | O164.101 ⟺ ¬RH; construction side closed negative; obstruction side = RH (no gain) | PROVED |
| R164_401.R3 | f_t is non-positive off ℕ for every t ≠ 0 (upgrades R164_102 §5 note) | PROVED |
| O164.101 | as a construction | **CLOSED (negative, identification)** |
| O164.401.1 | (new, optional) the same rigidity *without* the gap: is every positive self-dual m with m({0})=1, supp m∖{0} ⊂ {|y|≥1}, equal to 𝖢? (here Lemma 2 needs X>1, i.e. a hole beyond ±1) | OPEN (irrelevant to row D, since the window gives the gap) |
| O164.401.2 | positive-off-ℕ rigidity for Γ_ℝ(s)^a Γ_ℂ(s)^b (Dedekind-type) with fixed window: does the class reduce to the ζ_K's? | OPEN |
| RH, (★_cell), row D | | OPEN |

**Honest summary.** I did not construct an example. What I proved is that none exists: the positive witness class is {ζ}. This is a rigidity theorem, not an obstruction to off-line zeros, and it does not imply RH. L1 ends in the identification wall.
