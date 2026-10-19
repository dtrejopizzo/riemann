# CA_A_003 — Candidate (c): Hecke multiplicativity as the Euler mechanism on the window form; metaplectic escape

Phase 193. Pen and paper.

## 0. Corpus / index check
159 G1_B2_R3 §5.3: Hecke-shape Frobenius carriers 2cos(γ log p) excluded (Theorem E*, PROVED there) — that is a
*carrier of zeros*; here Hecke enters on the *prime/test side*. Phase 158: adèle class space = restatement.
Phase 192 EI_002/EI_003: tests built from the coefficients of ζ lead to the twisted second moment (REF-D residue T*₃(η)).
Phase 190: minimizer ≈ m^{−½}w(m/M).

## 1. The Hecke structure that ζ actually carries (CITED/PROVED)
a_τ(n):=Σ_{d|n}(d²/n)^{iτ} (normalized coefficient of E(·,½+iτ)), Σ a_τ(n)n^{−w}=ζ(w+iτ)ζ(w−iτ);
Hecke: a_τ(m)a_τ(n)=Σ_{d|(m,n)}a_τ(mn/d²) (unitary normalization), a_τ(p)=2cos(τ log p).

## 2. Theorem (Hecke relations at tempered parameters are comb-generic; PROVED)
Let H be the operator of multiplication by 2cos(τ log p) on L²(ℝ_τ) (equivalently μ_p+μ_p^* on ℓ²(ℚ^×_{>0}), μ the
regular representation). Then the Hecke relations H_pH_{p^k}=H_{p^{k+1}}+H_{p^{k−1}} and H_pH_q=H_{pq} (p≠q) are the
Chebyshev/product identities of cos(τ x) at x=log p, log q, and hold verbatim with log p replaced by any real numbers x,y
(H_xH_y=H_{x+y}+H_{x−y}). Hence, inside the window form 𝔞_T(F)=(1/2π)∫σ_T|F̂|², any manipulation that uses only Hecke
relations between the cosines cos(τ log n) is an identity valid for every weight vector on ℕ and, further, for every
finite measure on (0,2T) (lem:shape-ident). By thm:shape(B″) it carries no sign.
*Proof.* 2cos a·2cos b=2cos(a+b)+2cos(a−b); log(mn)=log m+log n is shared by every comb supported on ℕ. ∎

**Consequence for the seed.** The multiplicativity T_mT_n=Σ_{d|(m,n)}dT_{mn/d²} "encodes near-coincidences m≈kn" only
through log(m/k), the same Toeplitz-in-log(m/k) coordinate of Near_M that every comb shares (phase 190: all Near
statistics identical under 10⁻⁵ perturbations). The Euler product enters the window form through Λ=log-derivative of
the *degree-1* Euler product; Hecke relations are degree-2 relations among the *divisor* coefficients a_τ, which do not
appear in σ_T at all. So: property "Hecke multiplicativity is a mechanism on σ_T" moves YES→NO (PROVED).

## 3. Where Hecke structure can be load-bearing: the test side (pre-screen)
Choose tests whose Dirichlet polynomial is Hecke-built, D(τ)=Σ_{m≤M}b_m m^{−½−iτ} with b multiplicative (e.g. b=1,
giving ζ_M; or b=a_{τ0}). Then 𝔞_T(F)=(1/2π)∫σ_T|F̂_0|²|D|² is a twisted second moment.
| clause | verdict |
|---|---|
| (1) exact Λ | YES (σ_T exact) |
| (2) Euler × FE jointly | YES only if |D|² is evaluated by the approximate FE of ζ (needs Γ(s/2), conductor 1) |
| (3) non-linear | YES through D (test built from ζ's coefficients), as in EI_003 residue |
| (11) | NO as it stands: it is exactly EI_002 / T*₃(η) = (S), REF-D (phase 192 review); the sign step is (S) itself |
Key test: replacing Λ by a_P keeps the test family (b=1) and changes σ_T; the deduction "∫σ_T|F̂₀|²|ζ_M|² ≥ 0" has no
ζ-specific content until the twisted moment is evaluated — and its evaluation (Conrey-type main term + remainder) is an
estimate with remainder ⇒ (B′). NO at the sign step.

## 4. Metaplectic escape of line doubling (OPEN, recorded as next candidate)
CA_A_001 Lemma 2 forbids invariant positivity at Re s=¼ for weight 0. For weight ½ on Γ₀(4) the nonholomorphic Eisenstein
series E_{1/2}(z,s) has n-th coefficients ∝ L(2s−½,χ_n)/ζ(4s−1) (Goldfeld–Hoffstein; CITED, normalization to verify);
on the unitary axis s=½+it and n a square this gives ζ(½+2it) times finitely many Euler factors — the critical line of ζ
at a unitary parameter, with Γ(s/2) and conductor 1 visible through θ(z)=Σ_n e(n²z) (Riemann's FE).
Positivity available there: Parseval on a horocycle ∫₀¹|E_{1/2}(x+iy,½+it)|²dx = Σ_n|c_n(y,t)|² ≥ 0 and Maass–Selberg for
the metaplectic constant term (ζ(4s−1)/ζ(4s), back at abscissa 1). Parseval gives |ζ(½+2it)|²·|W_t(y)|², i.e. second-moment
data, not Re ζ′/ζ — this is again the |ζ|² family of §3. **Open question that would make it new:** a positive form on the
weight-½ Eisenstein packet ∫h(t)E_{1/2}(·,½+it)dt whose *off-diagonal* Parseval terms Σ_n c_n(t)c̄_n(t′) reproduce the
correlation of σ_T inside P_T (clause 8) — the Shimura correspondence ties these to weight-0 objects (line doubling again),
so a candidate must avoid passing through Shimura. Status: OPEN, not built.

## 5. Self-review
- §2 is airtight as an identity statement; it does not exclude Hecke operators acting on a space where they are not
  multiplication operators (e.g. on L²(Γ\ℍ) cusp part) — but those do not contain ζ (cusp L-functions), and the Eisenstein
  part is the multiplication picture. Fine.
- §4 citation must be verified before any use; nothing proved there.
- No negative value for ζ.
