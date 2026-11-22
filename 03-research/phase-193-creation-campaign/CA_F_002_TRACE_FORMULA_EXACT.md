# CA_F_002 — Trace formulas on arithmetic quotients used exactly; exact horocycle and Heegner periods (front F)

Pen and paper. **No sign contact. No negative value for ζ.** Develops F6, F7 and F14 of CA_F_000 in their *exact* forms. Estimates are
not used.

## 0. Setting
Let Γ ⊂ G(ℚ) be an arithmetic lattice and h an admissible spectral test. The (Selberg/Arthur) trace formula is an exact identity:
  Σ_disc m(π)ĥ(π) + Σ_P ∫_{i𝔞_P^*} ĥ(λ) tr(M_P(λ)^{−1}M_P′(λ)) dλ + (residual terms) = (geometric side).
Exact positivity input: if ĥ ≥ 0 on the unitary dual, the discrete side is ≥ 0. This gives the inequality
  (geometric side) − (continuous side) ≥ 0. (TF⁺)
ζ enters (TF⁺) through the normalizing factors of the intertwining operators M_P(λ). By Langlands' constant term computation (CITED),
these are products of ratios ξ(z_j(λ))/ξ(z_j(λ)+1), together with L-functions of cuspidal data. The z_j(λ) are affine in λ.

## 1. The only way ζ on the critical line can enter (PROVED)
**Lemma 1.** Let z(t) = ½ + it + iθ with θ real, a vertical translate of the critical line. Then, distributionally in t:
  (i) Re (ξ′/ξ)(z(t)) = 0;
  (ii) (d/dt) arg ξ(z(t)) = π Σ_{γ real ordinate} δ(t + θ − γ), counting multiplicity.
*Proof.*
(i) This is P46 rem:fe. The FE and reality give (ξ′/ξ)(1−s) = −(ξ′/ξ)(s), and on Re s = ½ we have 1 − s = s̄, so
(ξ′/ξ)(s̄) = conj (ξ′/ξ)(s) = −(ξ′/ξ)(s). So the real part vanishes off zeros. Distributionally, Hadamard gives
Re ξ′/ξ(½+iu) = Σ_ρ Re 1/(½+iu−ρ). Each pair ρ, 1−ρ̄ = 1−β+iγ contributes
  Re[1/(½−β+i(u−γ)) + 1/(β−½+i(u−γ))] = 0,
and zeros on the line give principal values with zero real part.
(ii) Ξ(u) = ξ(½+iu) is real. Its argument is constant except for jumps of π at real zeros of odd multiplicity; with multiplicity, the
distributional derivative of the continuous branch is π Σ δ.
Off-line zeros: Ξ has no real zero there, so they add nothing to the argument on the line. ∎

**Corollary 2.** In (TF⁺), any term in which a factor ξ(z_j(λ)) with Re z_j = ½ on the unitary axis enters through
tr(M^{−1}M′) contributes either 0 (by (i)) or π Σ_γ ĥ(γ − θ) (by (ii)). The latter is a sum over ordinates of zeros: (R)(4),
C_zeros, P46 cor:void.
**Corollary 3.** The remaining ζ-factors on the unitary axis sit at abscissae Re z_j ∉ {½}:
- For rank one (Γ congruence in SL₂(ℤ)), the scattering determinant is a product of Λ(2s−1,χ)/Λ(2s,χ) (Huxley, CITED). On Re s = ½
  these sit at abscissae 0 and 1.
- In higher rank, Re z_j ∈ ½ℤ. For z_j = 0 or 1 we get ζ on the 1-line. For abscissae ≥ 3/2 the series converges absolutely, so the
  input is Euler-product data at σ > 1. Moving it to σ = ½ is MW-2 (CA_A_006: "Y-integration never moves the abscissa").

Whether residual-spectrum normalizations in higher rank actually produce Re z_j = ½ (Mœglin–Waldspurger residual Eisenstein series on
GL_n, CITED-UNVERIFIED) does not matter. Corollary 2 covers that case.

## 2. Exact horocycle and Heegner periods
- **Closed horocycle at height y** (exact): ∫₀¹E(x+iy,s)dx = y^s + φ(s)y^{1−s}, with φ(s) = ξ(2s−1)/ξ(2s). On the unitary axis these
  sit at abscissae 0 and 1, so Corollary 3 applies. Long-horocycle equidistribution *rates* are estimates, (B′).
- **Heegner / CM cycles** (Hecke–Zagier, CITED): Σ_{z ∈ Λ_D} E(z,s) = c_D·ζ_K(s)·(Γ-factors), with K = ℚ(√D). This gives ζ_K(½+it) on the
  unitary axis, an exact critical-line value. The positivity available is a norm: |period|² ≤ ‖·‖² (Cauchy–Schwarz on spectral
  expansions) or Waldspurger-type |period|² ≥ 0. That is the norm class of CA_A_001 Cor 3. It survives O12 (ζ_K), and O10 through
  Epstein forms of other discriminants (CA_A_001 review). The window comb of ζ appears only as the factor of ζ_K = ζ·L(χ_D), with the
  partner L(χ_D) as cofactor. Separating it fails T1 (index l.21: field-uniform or name the separating property).

## 3. Verdict
NO-GO (PROVED) for the class "(TF⁺) on an arithmetic quotient, with ζ entering through Eisenstein normalizing factors":
- the critical-line factors contribute 0 or a zero sum (Lemma 1, Corollary 2);
- all other factors sit at abscissa 0, 1 or ≥ 3/2, which is MW-2.
Exact period identities are either in the norm class (CA_A_001) or abscissa-1 identities. Heat invariants and Weyl laws are the
asymptotic shadow of (TF⁺) and add nothing (R164_502).

## 4. Self-review
- *Could the discrete side carry the sign through a non-trivial identity rather than a positivity?* Then (TF⁺) is not used, and the
  statement is an identity among spectral data of Γ. Any identity in which ζ enters only through Lemma 1 has ζ only through zeros.
  This holds as stated for every trace-formula term built from tr(M^{−1}M′). Terms built from |M| (amplitudes) do not occur on the
  unitary axis, because M is unitary there.
- *Weighted trace formulas (Arthur's (G,M)-families)* bring in derivatives of products of normalizing factors. These are again
  combinations of ξ′/ξ and higher log-derivatives at the same z_j. Higher derivatives of a phase are derivatives of the zero
  measure. Lemma 1 applies termwise (ARGUED for the full (G,M) machinery; PROVED for each log-derivative term).
- *Is Lemma 1(i) circular?* No. It uses only the FE, reality, and Hadamard pairing. Off-line zeros cancel in pairs, which is why the
  real part is blind to them.
