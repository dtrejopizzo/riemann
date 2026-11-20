# Round 25 B — The prime-free statement as a kernel on one function: coprime-ratio decomposition, local factors, and the Schur-product test

Target (★): λ_A(T) ≥ 0 for every T. Notation of ROUND_015_A, ROUND_016_B, ROUND_020_A: λ = e^T, 𝒜_∞ the archimedean (Lévy) form
with symbol m(τ) = Re ψ(¼ + iτ/2) − log π, i.e. 𝒜_∞[G] = (1/2π)∫m|Ĝ|², written ∫∫G(x)G(x′)k(x − x′) with k the (distributional)
kernel of m; A(G) = ∫Ge^{x/2}, B(G) = ∫Ge^{−x/2}; 𝒜𝒫 = 𝒜_∞ + 2AB; 𝒞[Ψ] = 2⟨𝒯_log u, 𝒯u⟩; P := 1_{(−∞,−T)}.
Variables: F := F₁ ∈ L²(−∞, −T], y its variable, ξ := e^{−y} (> λ on the support). H(M) := Σ_{k≤M}1/k, L(M) := Σ_{k≤M}(log k)/k.
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 0. Corpus check
Read: ROUND_020_A (Cor 1.4, Thm 1.5), ROUND_015_A (Thm 3.1, Cor 3.2), ROUND_016_B (Lemma 2.1), REVIEW_010 §0 (polar term) and
§2 (absolute-convergence hypothesis added to 15A Cor 3.2); index rows P211-15A … P211-24A; phase 199 proof-L-sharp
PROOF_L_SHARP_E_001 (Thm E.1/E.1′: grouping by coprime ratio with the harmonic cutoff H(min(ξ/αλ, η/βλ)); Thm E.2 comb collapse;
Thm E.5: ratio classes indefinite one by one, NO-GO "sum of squares over ratios" and "Schur/Bochner on the coprime comb (Möbius
signs)"), PROOF_L_SHARP_F_001 (Thm F.1: symbol Θ_∞ = −2Re(ζ′/ζ)(½ + iτ); Thm F.2 sawtooth), PROOF_L_SHARP_J_001 (Prop J.1 exact
dilation Gram, Thm J.2), PROOF_L_SHARP_NN_001 (local factors E_p), SPEC_SIGN_OBJECT_002 (null symbol of the discrete archimedean part).
What is prior and is NOT reclaimed. The coprime-ratio grouping with the harmonic cutoff (§2) is Thm E.1′ of phase 199 written in the
tail variable F₁ of this phase, together with the polar term; the class-by-class indefiniteness is Thm E.5; the identity
m = −2Re ζ′/ζ on the line used in §3 is the content of Thm F.1.
What differs. The one question not settled on record: whether the coprime-pair weight factorises over primes into local
positive-definite kernels so that a Schur-product argument (local PD × archimedean PD) gives the sign. E.5 closed "Schur/Bochner on
the coprime comb" by the Möbius signs of the comb coefficients; here the comb has been collapsed (no Möbius signs), the weight is
(ab)^{−1/2}·(H, L, log(ab)), and the factorisation question is asked of that object. §3 answers it: the weight (ab)^{−1/2} DOES
factorise into local Poisson kernels (PROVED), but the cofactor is not archimedean and its symbol vanishes identically. No indexed
route is retried; the Schur test is new as stated and is closed here.

## 1. The prime-free form as a kernel on F₁ (PROVED, given the hypotheses of 15A Thm 3.1 and REVIEW_010 §2)

Hypotheses (H): u even on |ξ| > λ with Σ_N log N‖F_N‖ < ∞ and Σ_{N,N′}|𝒜_∞(F_N, F_{N′})| < ∞ (REVIEW_010 §2), F_N = N^{−1/2}Pτ_{log N}F
(16B Lemma 2.1), Ψ = 𝒯u = Σ_N F_N.

**Theorem 1.1 (exact kernel).** Under (H),
 𝒬[F] := 𝒜𝒫[Ψ] − 𝒞[Ψ] = ∫∫F(y)F(y′)K_ℕ(y, y′)dy dy′ with
 K_ℕ(y, y′) = Σ_{N,N′≥1}(NN′)^{−1/2}{ k(y − y′ + log(N/N′))·1[N < ξ/λ]1[N′ < ξ′/λ] − log(NN′)·δ(y − y′ + log(N/N′))·1[N < ξ/λ] }
        + α(y)β(y′) + β(y)α(y′),
 α(y) := e^{y/2}⌊ξ/λ⌋,  β(y) := e^{−y/2}H(⌊ξ/λ⌋)   (a.e. in y),
and 𝒬[F] = W_T(Ef) on data from admissible f (16B Lemma 2.3 / DOSSIER §7.1, with the polar term).
*Proof.* x = y + log N maps the support condition x < −T of Pτ_{log N}F to y < −T − log N, i.e. N < ξ/λ. Then
𝒜_∞(F_N, F_{N′}) = (NN′)^{−1/2}∫∫F(y)F(y′)k((y + log N) − (y′ + log N′))1[N < ξ/λ]1[N′ < ξ′/λ], and ⟨F_N, F_{N′}⟩ is the same with
k replaced by δ; on the δ-support ξ/N = ξ′/N′, so one indicator suffices. 𝒞 = Σ_{N,N′}(log N + log N′)⟨F_N, F_{N′}⟩ is 15A Thm 3.1
symmetrised. A(Ψ) = Σ_N N^{−1/2}∫_{x<−T}F(x − log N)e^{x/2}dx = Σ_N∫_{N<ξ/λ}F(y)e^{y/2}dy = ∫Fα; likewise B(Ψ) = Σ_N N^{−1}∫_{N<ξ/λ}Fe^{−y/2}
= ∫Fβ. Summation exchanges are justified by (H). ∎
Reading. No prime appears: the arithmetic data are the set {log N}, the weights N^{−1/2}, log N, and the counting functions
⌊ξ/λ⌋, H(⌊ξ/λ⌋) in the polar vectors. The kernel is Toeplitz in log(N/N′) except for the cutoffs N < ξ/λ — those are the only
non-translation-invariant pieces, and they carry the T-dependence (16B Lemma 2.1).

## 2. Decomposition by the coprime ratio (PROVED; = phase 199 Thm E.1′ in the tail variable)

**Theorem 2.1.** Write N = ka, N′ = kb with gcd(a, b) = 1 (bijection ℕ² ↔ {(a, b) coprime} × ℕ). Put z_{ab} := y − y′ + log(a/b),
M_a(y) := ⌊ξ/(λa)⌋. Then
 K_ℕ(y, y′) = Σ_{gcd(a,b)=1}(ab)^{−1/2}{ k(z_{ab})·H(min(M_a(y), M_b(y′))) − δ(z_{ab})·[2L(M_a(y)) + log(ab)·H(M_a(y))] } + α⊗β + β⊗α.
*Proof.* (NN′)^{−1/2} = k^{−1}(ab)^{−1/2}; log(N/N′) = log(a/b); 1[ka < ξ/λ]1[kb < ξ′/λ] = 1[k ≤ min(M_a(y), M_b(y′))] a.e.;
log(NN′) = 2log k + log(ab); sum over k. On the δ-support ξ/a = ξ′/b, so M_a(y) = M_b(y′). ∎
Arithmetic of the inner sums (CITED, Euler–Maclaurin; ζ(1 + s) = 1/s + γ − γ₁s + …): H(M) = log M + γ + O(1/M),
L(M) = ½log²M + γ₁ + O(log M/M). These are the truncated forms of ζ(1 + s) and −ζ′(1 + s) at s = 0: ζ itself (not Λ) enters
through Σ_k k^{−1−s}, Σ_k k^{−1−s}log k, regularised by the edge cutoff M = ⌊ξ/(λa)⌋, which ties the arithmetic index a to the
archimedean variable ξ. The class (a, b) = (1, 1) carries k(y − y′)H(min(M₁(y), M₁(y′))) − δ(y − y′)2L(M₁(y)); every class is
indefinite (phase 199 Thm E.5; measured below).

## 3. Local factorisation of the coprime weight and the Schur-product test

**Proposition 3.1 (the coprime weight is a product of local positive-definite kernels; PROVED).** For q ∈ ℚ_{>0}, q = a/b in
lowest terms, w(q) := (ab)^{−1/2} = Π_p p^{−|v_p(q)|/2}. Each n ↦ r^{|n|} (0 < r < 1) is positive definite on ℤ (its Fourier
series is the Poisson kernel P_r(θ) = (1 − r²)/|1 − re^{iθ}|² > 0, total mass 1). Hence w is positive definite on the discrete
group ℚ^×_{>0} ≅ ⊕_pℤ: it is the Fourier transform of the product probability measure ⊗_pP_{p^{−1/2}}(θ_p)dθ_p/2π on the dual
torus Π_pℝ/2πℤ (Kolmogorov extension). With a regulariser σ > ½ and the character q ↦ q^{−iτ}:
 Σ_{gcd(a,b)=1}(ab)^{−1/2−σ}(a/b)^{−iτ} = |ζ(½ + σ + iτ)|²/ζ(1 + 2σ) = Π_p(1 − p^{−1−2σ})/|1 − p^{−1/2−σ−iτ}|² =: D_σ(τ) > 0.
*Proof.* Multiplicativity of w in each v_p; the identity is Σ_{N,N′} = Σ_kΣ_{(a,b)=1} and the Euler product, both absolutely
convergent for σ > ½. ∎ (This uses unique factorisation: ℚ^×_{>0} free abelian on the primes.)

**Theorem 3.2 (the would-be archimedean cofactor is not archimedean and has null symbol; PROVED for σ > ½, CITED limit).** In the
untruncated dilation model Ψ_σ := Σ_N N^{−1/2−σ}τ_{log N}F (F ∈ C_c^∞(ℝ), σ > ½, no cutoff),
 𝒜_∞[Ψ_σ] − Σ_{N,N′}log(NN′)(NN′)^{−1/2−σ}⟨τ_{log N}F, τ_{log N′}F⟩
   = ζ(1 + 2σ)·(1/2π)∫|F̂(τ)|²·D_σ(τ)·[m(τ) + 2Re(ζ′/ζ)(½ + σ + iτ)] dτ.
At σ = 0 the bracket is m(τ) + 2Re(ζ′/ζ)(½ + iτ) = 2Re(ξ′/ξ)(½ + iτ) − 2Re(1/s + 1/(s − 1))|_{s=½+iτ} = 0 identically (off the
ordinates) (CITED: functional equation; ξ real on the line ⇒ Re ξ′/ξ = 0; m = 2Re Γ_ℝ′/Γ_ℝ; this is the symbol identity of phase
199 Thm F.1).
*Proof.* Ψ̂_σ = F̂·ζ(½ + σ + iτ), Σ log N·N^{−s} = −ζ′(s); the cross term is 2Re(−ζ′ζ̄) = −2|ζ|²Re ζ′/ζ; |ζ|² = ζ(1 + 2σ)D_σ by
Prop 3.1. ∎
Consequences (PROVED from 3.1–3.2 and Thm 2.1).
 (a) The coprime kernel is "local PD × cofactor", but the cofactor m + 2Re ζ′/ζ = m − 2Σ_pΣ_j log p·p^{−j/2}cos(jτ log p) (σ = 0,
   formal) is a SUM of local terms plus m, not an archimedean function: log(ab) = Σ_p|v_p(q)|log p is additive in the local
   coordinates, so the comb side of the class weight is a derivation of the local product (Σ_p ∂ of the p-factor), not a product.
   A Schur product (pointwise product of PD kernels) has no slot for it.
 (b) The only archimedean cofactor available is m alone, which is not PD (m(0) = ψ(¼) − log π = −5.37 < 0; m < 0 on |τ| < 6.29,
   SPEC_SIGN_OBJECT_002); D_σ·m is not ⪰ 0, so the archimedean-times-local product carries the wrong sign on low frequencies, and the
   comb is exactly what must repair it.
 (c) In the regularised limit the full bracket vanishes: the "main term" of every class sum is null. By Thm 2.1, what survives in
   𝒬 is (i) the cutoff remainders H(M) − (log M + γ), L(M) − (½log²M + γ₁) (sawtooth, phase 199 F.2) with M = ⌊ξ/(λa)⌋ coupling a to
   ξ, and (ii) the polar vectors α, β. Neither factorises: M_a(y) depends on (a, y) jointly through ξ/a, so the class coefficient is
   not of the form w(q)·κ(y, y′) with w multiplicative.
**NO-GO (PROVED, class: Schur/Hadamard products of a multiplicative local PD weight on ℚ^×_{>0} with a q-independent archimedean
kernel).** Any such product with the archimedean factor m is not ⪰ 0 (b); with the factor m + 2Re ζ′/ζ it is identically null (c);
the sign of 𝒬 sits entirely in the cutoff/polar part, which is not of product type. The task's proposed falsifier (non-unique
factorisation) is moot: the factorisation exists (Prop 3.1) and does not carry the sign.

## 4. Numerical test of the truncated coprime-pair kernel (NUMERICAL)

Tool: tools/coprime_pair/coprime_kernel.py R Nb T. F on the R-cell window y ∈ (−T − log R, −T) (u on λ < ξ < Rλ; then only
N, N′ < R occur, so the class set {(a, b) coprime, a, b < R} is finite and exact), sine basis Nb, Arch and Λ-comb Gram of
tools/galerkin_mp.py (as in tail_direct/cellRp.py), shift-and-cut matrices for Pτ_{log N}, polar vectors α, β. Class matrices
Q_{a,b} := Σ_k(k²ab)^{−1/2}[Arch(τ_{log ka}F, τ_{log kb}F) − log(k²ab)⟨·,·⟩], symmetrised over (a, b) ↔ (b, a). No admissibility
constraints imposed (the unconstrained R-cell form; 16B §3.1 shows its bottom is ≈ 0 with the polar term).
Validation. Σ_{classes}Q_{a,b} + polar vs direct G^T(Arch − Π_Λ)G + polar: relative max-entry difference 1.1·10⁻² (R = 3),
1.3–3.5·10⁻² (R = 5, Nb = 32…96), 5.1·10⁻² (R = 8); the difference is the Galerkin projection of the cut shifts (Π_Λ evaluated on
the projected G, the prime-free comb on the exact shift identity); it does not decrease with Nb at this grid, so the numbers below
are good to ≈ 5% of the matrix scale, not more. Bottom of the full form: −0.0000 (R = 3, 5, 8; T = 0.8 and 1.0).
| R | classes | min eig of single classes (range) | height ≤ H partial sums + polar, H = 1, 2, …, R−1 | S-unit partial sums (primes ≤ P) + polar |
|---|---|---|---|---|
| 3 | 2 | (1,1): −2.31; (1,2): −1.60 | −0.84, −0.00 | P=1: −0.84; P=2: −0.00 |
| 5 | 6 | −4.17 … −0.88 (each indefinite) | −1.96, −1.55, −0.93, −0.0004 | −1.96, −1.29, −0.0004 |
| 8 | 18 | −6.39 … −0.54 (each indefinite) | −3.53, −3.55, −2.55, −2.38, −1.64, −1.30, −0.0013 | −3.53, −3.40, −2.08, −1.30, −0.0013 |
(T = 0.8, Nb = 48; T = 1.0, R = 5, Nb = 64 reproduces the R = 5 row to 2 digits.)
Readings. (a) Every coprime class is indefinite with many negative directions (phase 199 E.5 reproduced in the tail variable).
(b) Positivity appears only when the LAST class enters: every truncation by height or by prime support is negative by O(1)
(−0.84 … −3.5 against matrix scale ≈ 5), and the full sum reaches 0 to tool accuracy. No monotone or local-in-p build-up of the
sign: the sign is global in the class set. (c) This is consistent with §3: there is no product structure for a Schur argument
to use; even within the finite window the positivity is a cancellation across all ratio classes, with the polar term essential
(no-polar partial sums are −2.3 … −23.5).

## Falsifier test (rule 4)
No sign step is taken; the memo proves identities and a NO-GO. (a) cΛ, (b) a_P, (d) finite modifications: Theorem 1.1 uses
Λ ∗ 1 = log (15A Thm 3.1); for these combs the collapse fails and the form is not prime-free (extra terms (c − 1)log N, or
Σ_{p<P}-corrections) — the identities break, as they must. (c) Beurling: there is no Poisson tail map, so Thm 1.1 has no
analogue; Prop 3.1 needs the ratio group to be free on the generators (for a Beurling system with unique factorisation it holds
formally, with non-unique factorisation the coprime parametrisation fails). Since the factorisation carries no sign (§3), none of
this distinguishes ζ; the NO-GO is method-level.

## Result
NO-GO (PROVED, class: local-PD × archimedean Schur products on the coprime-ratio kernel), with PROVED pieces.
### What was proved
- Thm 1.1: (★) on tails is ∫∫F₁F₁K_ℕ with an explicit prime-free kernel, polar vectors α = e^{y/2}⌊ξ/λ⌋, β = e^{−y/2}H(⌊ξ/λ⌋).
- Thm 2.1: coprime-ratio form with weights (ab)^{−1/2}·H(min M), (ab)^{−1/2}[2L(M) + log(ab)H(M)], M = ⌊ξ/(λa)⌋ (= phase 199 E.1′).
- Prop 3.1: (ab)^{−1/2} is a product over p of Poisson kernels p^{−|v_p|/2}, positive definite on ℚ^×_{>0}; D_σ = |ζ|²/ζ(1 + 2σ).
- Thm 3.2 + Cor: the cofactor of the local product is m + 2Re ζ′/ζ — additive in p, not archimedean, null on the line; with m
  alone it is not PD. Hence no Schur-product proof of the sign.
### What failed and why
The Schur/local–global route: the comb weight log(ab) is additive over primes (a derivation of the local product), and the
cutoff M = ⌊ξ/(λa)⌋ couples the arithmetic index to the archimedean variable; the regularised main term is identically zero, so the
sign is entirely in the cutoff remainders and the polar term. NUMERICAL: every class and every height/prime-support truncation is
negative by O(1); positivity appears only with the full class set.
### Next concrete step
The surviving object is the cutoff part of Thm 2.1: K_cut := Σ_{(a,b)=1}(ab)^{−1/2}{k(z)[H(min M) − ζ-regularised value] − δ(z)[2(L(M) −
½log²M − γ₁) + log(ab)(H(M) − log M − γ)]} + polar, i.e. the sawtooth form of phase 199 F.2 in the tail variable. Any further
attempt must be on K_cut + polar directly (F.2 and J.3 on record: do not retry "sawtooth decides the sign in the transition region").

## Index row and ledger line
Index (05-meta-and-planning/ROUTES-TRIED-INDEX/README.md): row P211-25B. Ledger (LEDGER.md): line C49.
