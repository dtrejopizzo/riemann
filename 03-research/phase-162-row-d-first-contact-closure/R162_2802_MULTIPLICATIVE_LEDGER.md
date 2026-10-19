# R162_2802 — The multiplicative ledger 1 = exp_*(Λ/log): Piltz family d_k (all k) + ψ against H(m) — **NO-GO (PROVED); PARTIAL: three PROVED tools (Piltz blindness under H(m), terminating ledger identity with amplification law, Λ̃/deletion ledger computation)**

Angle B ("exponential structure"). Pure math, no numerics. Cell 4F/5F (Euler product × global in x),
residual O2601.1 (grid §7). Gate 1 OPEN. No label moves. No sign claimed.

Corpus check. grep "Piltz", "d_k(n)", "Selberg–Delange" over phases 150–162 and the R160 survey: phase-13-omega-class-multiplicative-chaos (d_k = k^ω on
squarefree n, freezing, RH-independent), phase-19-omega-rate-freezing (ω-flow via Selberg–Delange, RH-independent), G2_B1_R4 Prop K
(Selberg–Delange obstruction for absolute budgets). None compares the integer-k family with ψ under H(m), none uses the
terminating ledger (R162_903 Thm 3.2) at the level of partial sums, none computes exp_* of Λ̃. Walls named in advance:
W1 (E1), W3 (class), W12 (exact identity without sign). Inputs: R162_2501 (H(m), E, M_m), R162_2601 (Thm T, Thm Λ̃,
Thm H), R162_2602, R162_903 Thm 3.2, R162_2301 Lemma S.

Notation. a ↦ exp_*(a) is the Dirichlet-convolution exponential on arithmetic functions with a(1)=0; ℓ := Λ/log
(ℓ(p^k)=1/k). d_z := exp_*(zℓ), so d_z(n) = Π_{p^a‖n} C(z+a−1,a), a polynomial in z of degree Ω(n); d_k (k∈ℕ) are the
Piltz functions, d_0=δ, d_1=1. D_z(x) := Σ_{n≤x} d_z(n); Δ_k(x) := D_k(x) − Res_{s=1} ζ(s)^k x^s/s.
H(m): exactly m off-line quartets ρ_j = ½+β_j+iγ_j (and reflections), β* = max β_j.

## 1. Failing lines first

| model | ledger exp_*(a/log) | ≥0 | integer | ≡1 | off-line | status for a ledger argument |
|---|---|---|---|---|---|---|
| ζ under H(m) | 1 | yes | yes | yes | m | the ledger holds identically whatever m is (§3) |
| Λ̃ (2601) | b̃ := exp_*(Λ̃/log), §5 | yes (after the finite modification) | **no** | no | exactly m zeros of F̃ | kills every ledger argument not using b≡1 exactly |
| deletion Λ1_{n≥N} | ζ·exp(−Σ_{p^k<N}p^{−ks}/k), §5 | yes | **no** (rational) | no | = ζ | kills "≥0 + prime-power support" |
| M_m | undefined (not a Dirichlet series) | — | — | — | κ+4m | outside; but any ledger statement plus FE conductor 1 pins ζ (Hamburger, 2601 Thm H), so M_m is excluded only tautologically |
| Epstein ζ_Q (h>1) | r_Q ≥0 integer; log_*(r_Q)·log not ≥0, not on prime powers | coeffs yes | yes | no | ∞ | kills "integer ≥0 coefficients + FE" without Euler |
| Beurling DMV | ≡1 on 𝒩_B | yes | yes on 𝒩_B | yes on 𝒩_B | ∞ | kills "≡1" read without ℤ-support |

## 2. Theorem PB (Piltz blindness under H(m), PROVED)

(a) For every k∈ℕ, Perron's formula for D_k(x) sees no zero of ζ: ζ^k is holomorphic on ℂ∖{1}, so shifting the contour
to Re s = σ₀ < 1 picks up only the residue at s=1 (x P_{k−1}(log x)); off-line zeros are zeros of ζ^k, contribute no
residue, and enter Δ_k only through the growth of |ζ(σ+it)|^k.
(b) H(m) ⟹ LH ⟹ α_k ≤ ½ for all k (α_k := inf{a : Δ_k(x) ≪ x^a}).
*Proof of (b).* Backlund's criterion (Titchmarsh §13.5): LH ⟺ for every σ>½, N(σ,T+1) − N(σ,T) = o(log T). Under H(m)
the left side is 0 for T > max γ_j + 1. Then Titchmarsh Thm 13.4 (LH ⟺ α_k ≤ ½ ∀k). □
*Consequence.* The whole integer family {Σ_{n≤x} d_k(n)}_{k∈ℕ}, with exact integer coefficients ≥ 0, generated
non-linearly from Λ, satisfies under H(m) exactly the bounds it satisfies under RH (known: α_k ≤ ½ for all k under LH;
nothing better is known under RH for general k). **No finite-k Piltz statement separates H(m) from RH.** This is the
corpus line of P33 (m<∞ ⟹ A ⟹ LH) read on the Piltz side: the Piltz exponents are Lindelöf-type, and H(m) implies
Lindelöf.

(c) (Where the zeros hide: Selberg–Delange in z.) For complex z, ζ^z has branch points at every zero, and the Hankel
contour at ρ gives a term c_ρ(z) x^ρ (log x)^{−z−1}/Γ(−z) (standard Selberg–Delange local computation; c_ρ holomorphic
in z). The factor 1/Γ(−z) vanishes exactly on z∈ℕ. So all zeros — on-line and off-line alike — lie in the kernel of
"restriction to z∈ℕ". Carlson's theorem cannot remove this kernel: 1/Γ(−z) has infinite exponential type. The
on/off distinction is |x^ρ| = x^{½+β}, visible only for z∉ℕ, where d_z is not integer-valued and not ≥0 for z<0.
∂_z|_{z=0} D_z(x) = Σ_{n≤x} ℓ(n) = Σ_{n≤x}Λ(n)/log n recovers the prime side and the x^ρ/ρ log x terms. Hence
"integer family + ψ" = "the z-family at z∈ℕ and its z-jet at 0" = Selberg–Delange for complex z = zero side (W1).

## 3. Theorem L (terminating ledger identity and the amplification law, PROVED)

(a) For x ≥ 1, K := ⌊log₂ x⌋, with the exact integer identity (R162_903 Thm 3.2 at the level of partial sums)
  Σ_{n≤x} Λ(n)/log n = Σ_{j=1}^{K} ((−1)^{j+1}/j) Σ_{i=0}^{j} (−1)^{j−i} C(j,i) D_i(x).
*Proof.* ℓ = log_*(1) = Σ_{j≥1}(−1)^{j+1}(1−δ)^{*j}/j, and (1−δ)^{*j}(n)=0 for j>Ω(n) (it counts ordered factorizations
into j factors >1); (1−δ)^{*j} = Σ_i (−1)^{j−i}C(j,i) d_i. Sum over n≤x, where Ω(n) ≤ K. □
(b) The identity holds for ζ unconditionally, hence under H(m) for every m; it is a formal identity of Dirichlet series
with the coefficient 1, i.e. the *definition* of Λ from 1 (Lemma S analogue: exp_* is injective, so "exp_*(a/log) ≡ 1"
⟺ a = Λ). It cannot be violated by any hypothesis on the zeros of ζ.
(c) Amplification. Insert D_i = main_i + Δ_i. The main terms recombine to li-type main term (ψ's pole part). The error
part is Σ_i w_i(x) Δ_i(x) with w_i(x) = Σ_{j=max(i,1)}^{K} (−1)^{j+1}(−1)^{j−i}C(j,i)/j, and max_i |w_i(x)| ≫ 2^K/K³ ≫
x/(log x)³. Known Ω-results (Δ_k(x) = Ω(x^{(k−1)/(2k)}), Hardy/Szegő–Walfisz) show individual Δ_i are not small.
Therefore: from per-k bounds |Δ_i(x)| ≤ C_i x^{θ}, the ledger yields for ψ only an error ≪ x^{1+θ}·max_{i≤K}C_i — worse
than trivial. The x^{ρ_j} terms of ψ under H(m) (size x^{½+β*}) are produced entirely by cancellation among
Δ_0,…,Δ_K with weights of size x, in the range k ~ log x where no Piltz bound is uniform.
(d) Converse direction (what would be needed). A contradiction with H(m) via the ledger needs a uniform bound
Σ_i |w_i(x)||Δ_i(x)| ≪ x^{½+β*−ε}, i.e. control of the signed Piltz errors for k up to log₂ x at relative precision
x^{−½−ε}. By (a) that bound *implies* ψ(x) − x ≪ x^{½+β*−ε}; it is a ψ-bound written in Piltz coordinates (E1).
Uniform Piltz asymptotics for k ≍ log x (Sathe–Selberg/Norton type) are of Selberg–Delange quality and carry the zero
terms of (2c). □

## 4. Why "ψ sees ρ, Σd_k does not" gives no exact separating identity (PROVED)

Suppose I is an identity among {D_k}_{k∈ℕ}, ψ and main terms, derived from 1 = exp_*(Λ/log). By 3(b) I holds for ζ for
every m. An identity cannot be "violated by off-line zeros": it is either a formal consequence of the ledger (then it
holds under H(m)) or it contains an analytic inequality (then that inequality is the content, and by 2(b) and 3(d) it is
a ψ-/zero-side inequality of RH or C_B strength). The ledger's nonlinear content (products of Λ-values) is exactly
Selberg-type (Lemma S), already shown sign-free (R162_2301 Thm Q, W12). **NO-GO.**

## 5. Falsifier computations (PROVED)

(a) Λ̃. With Λ̃(n) = 1 − Σ_j 2Re n^{ρ_j−1} (modified at finitely many n to be ≥0), a := Λ̃/log, b̃ := exp_*(a)
= δ + a + a*a/2 + …. Then b̃ ≥ 0 (exponential of a nonnegative function), b̃(1)=1, and e.g. b̃(p) = Λ̃(p)/log p,
b̃(6) = Λ̃(6)/log 6 + Λ̃(2)Λ̃(3)/(log2 log3): generically transcendental (n^{iγ_j}), not integer, not ≡1 (b̃(p) ≈ 1/log p).
F̃(s) := Σ b̃(n)n^{−s} = exp(Σ a(n)n^{−s}) satisfies −F̃′/F̃ = G = ζ(s) − Σ_j[ζ(s+1−ρ_j)+ζ(s+1−ρ̄_j)]; G has simple
poles with integer residues (+1 at 1, −1 at ρ_j, ρ̄_j), so F̃ = exp(−∫G) is meromorphic on ℂ: a pole at 1, **simple
zeros exactly at the m off-line points ρ_j, ρ̄_j, and no other zeros**. (Correction/precision to 2601 §3: G *is* the
log-derivative of a meromorphic function; what F̃ lacks is the functional equation, integrality and b̃≡1, not
meromorphy.) Its Piltz sums Σ b̃^{*k} see only the pole (as in 2(a)); its ψ_Λ̃ sees x^{ρ_j}. So F̃ realizes the whole
"Piltz blind / ψ sees" dichotomy with exactly m off-line zeros and nonnegative ledger coefficients. Any argument using
{exp structure, ≥0 coefficients, atomic support, Chebyshev growth, the Piltz/ψ contrast} would exclude F̃: impossible.
The only separator left is **b ≡ 1 (integer values) together with the FE**, which by Hamburger is the statement "F=ζ".
(b) Deletion N=3 (Λ(2) removed): F = ζ(s)exp(−2^{−s}); coefficient at 2^a·odd equals Σ_{j≤a}(−1)^j/j! ∈ [0,1] ∩ ℚ
(a=1: 0; a=2: ½; a=3: ⅓); ≥0, not integer, zeros = those of ζ. General N: rational, ≥0, not ≡1.
(c) M_m: no ledger. Adding FE conductor 1 to any ledger statement pins ζ (2601 Thm H) — the tautological exclusion.

## 6. Verdict and residual

**NO-GO (PROVED).** The Piltz family is blind to all zeros at integer k (Thm PB(a),(c)); H(m) implies Lindelöf, so all
Piltz exponents are the RH ones (PB(b), E1 check: Piltz exponents are Lindelöf-type, and H(m) ⟹ LH); the combination
with ψ is the terminating ledger (Thm L), a formal identity valid for every m, whose error recombination amplifies by x
(Thm L(c)); the separating content lies only at z∉ℕ (Selberg–Delange = zero side, W1). Λ̃ gives an ordinary Dirichlet
series F̃ with ≥0 ledger coefficients and exactly m off-line zeros; deletion gives ≥0 rational ledgers. Walls: W1, W12,
W3 (for the ≥0 part); the integer part collapses to Hamburger (ζ itself).
Sharpened residual **O2802.1** (folds into O2601.1 / row 5): a property of the *integer-valued* ledger b ≡ 1 (not ≥0,
not exp-structure) that is non-formal and uniform in k ≍ log x. Only integrality separates ζ from F̃; its exact use
(integer lattice ⌊x/n⌋) was previously shown invisible to continuous invariants (R162_903 Thms 4.1–4.2).
