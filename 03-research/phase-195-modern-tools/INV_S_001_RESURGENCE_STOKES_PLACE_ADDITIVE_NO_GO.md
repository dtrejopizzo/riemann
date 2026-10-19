# INV_S_001 — Resurgence / exact WKB / Stokes constants for the window form (track S, survey B5)

Phase 195.
Objects as in Paper 47: s_T = m − Σ_{n∈N_T} v_n cos(τ log n), m(τ)=Re ψ(¼+iτ/2) − log π, v_n=2Λ(n)/√n,
𝔞_T(F)=(1/2π)∫ s_T|F̂|² on P_T (A=B=0), λ_A = inf over P_T, thm:margin (λ_A ≤ 4·10⁹ T e^{−15.449T}, 15.449 < 42/e).

## 0. Corpus check / routes-tried index
- ROUTES-TRIED-INDEX: no WKB / resurgence / Stokes entry (grep "wkb|resurg|stokes|instanton|tunnel": only survey B5). Grid and crossword: no hit.
  The nearest indexed items are L41 (spheroidal asymptotics, prolate piece only), thm:margin and prop:env (Paper 47), and INV_Q/INV_R (phase 195:
  exact identities go through ρ_S=∏γ_v and are place-additive).
- New reason (why this is not a rerun): the object is the singularity/Stokes data of the transseries of λ_A in ħ=1/T, and the possibility that a Stokes
  constant is sign-definite by Stokes-graph topology or median-resummation reality. This is a different method class (non-perturbative, nonlinear in the
  form) from the linear identities in Q/R. The memo finds that it reduces to them anyway (§2, §4).

## 1. The two-atom window has no semiclassical parameter (PROVED, elementary)
On T∈(½log3, ½log5)=(0.5493, 0.8047), N_T={2,3,4}. Note that 4 is a contact (v_4=log 2), so the "two-atom" model has two primes and three contacts.
Here ħ=1/T∈(1.24, 1.82), so there is no asymptotic regime and no transseries in 1/T is defined on the window. λ_A>0 there (CITED, Paper 47:
½log5 certificates and the nonincreasing property). The only regime where exact WKB could apply is T→∞. By lem:spec-collapse the contact set then grows
at every T=½log n, so λ_A is defined piece by piece on infinitely many windows and has no global transseries in T.
The semiclassical question therefore splits into two well-posed models, treated in §3 and §4.

## 2. Borel plane of the symbol = the u-line of the explicit formula; Stokes data are place-additive (PROVED)
**Lemma S1.** Write s_T(τ)=C_0+∫_0^∞(1−cos τu)K(u)du − Σ_{n∈N_T} v_n cos(τ log n) (thm:Z with w≡0 outside, eq:fw), where
K(u)=e^{−u/2}/(1−e^{−2u}) (Gauss integral for ψ, t=2u). The "Borel transform" of s_T (the measure whose Fourier/Laplace transform is s_T) is
K(u)du + atoms −(v_n/2)δ_{±log n}. Its singular set is
  Σ_∞ = iπℤ∖{0} (poles of K continued in u; residues independent of Λ)  ∪  {u=0} (log-growth of m, Stirling)
  Σ_fin = {±log n : n∈N_T} (real axis; jump data v_n/2, independent of Γ).
The Stirling Stokes constants of ψ (alien derivatives at u=iπk) are fixed numbers independent of the comb. The data at u=log n are exactly v_n and do not
depend on the archimedean factor. Σ_∞∩Σ_fin=∅ (imaginary vs real rays), so every alien derivative of s_T is purely archimedean or purely prime.
*Proof.* Linearity of the Borel/Fourier transform. Distinct rays (arg u=±π/2 vs arg u∈{0,π}) carry distinct Stokes automorphisms, which commute and factor.
∎
**Consequence (NO-GO, class 𝒦_St-symbol).** Stokes constants of the symbol cannot satisfy clause (5): they are place-additive, the same phenomenon
INV_Q/INV_R found for exact identities (log of ∏γ_v becomes a sum). O_6 (finite modification of the weights) changes only real-ray data. O_4-type
rescalings of the comb do the same. The archimedean Stokes data are invariant under every comb falsifier, so they cannot carry the sign.

## 3. Frozen-comb model: the large-T limit is perturbative and negative (PROVED except the T^{-2} coefficient)
Freeze N={2,3,4} and let T→∞ with symbol s^{(3)}=m − Σ_{n=2,3,4} v_n cos(τ log n).
**Theorem S2.** λ_A^{frozen}(T) → min_τ s^{(3)} = s^{(3)}(0) = ψ(¼) − log π − (√2 log2 + (2/√3) log3 + log2)
= −γ − π/2 − 3log2 − logπ − 2.94197… = −8.3142… (closed form; decimals NUMÉRICO).
*Proof.* Re ψ(x+iy) = ψ(x) + Σ_{j≥0} y²/((j+x)((j+x)²+y²)) is increasing in |y|, so m(τ)≥m(0). Also Σ v_n cos ≤ Σ v_n with equality at 0, so
s^{(3)} ≥ s^{(3)}(0), and the lower bound 𝔞 ≥ s(0)‖F‖² follows. Upper bound: the compression of the Fourier multiplier s^{(3)} to L²(−T,T) has, for
every j, λ_j(T) → inf s (wave packets concentrated at τ=0, of width ≪1 in τ, exist in L²(−T,T) in dimension ≍T). The constraint subspace P_T has
codimension 2, so by min-max λ_A^{frozen} ≤ λ_3(T) → s(0). ∎
ARGUED (Parter–Widom-type expansion for an analytic symbol with a nondegenerate minimum): λ^{frozen}(T) = s(0) + c_2T^{−2} + c_3T^{−3} + …, a
power series with no exponentially small sector at leading orders. The minimum is unique (τ=0) and even, so there are no symmetric wells and no tunnelling
pair.
**Reading.** With a fixed comb the bottom stays O(1) negative. The exponentially small, nonnegative λ_A of the true system therefore does not come from
tunnelling between the Tate ends. It comes from the growth of the contact set, i.e. from the explicit-formula identity 𝔞_T(F)=Σ_ρΦ_F(ρ)Φ_F(1−ρ)
(lem:roughEF).

## 4. 15.449 is not an action; the effective exponent is unbounded (ARGUED, from the thm:margin proof)
In thm:margin, 42/e = 2·21/e comes from optimizing k in (k/(21T))^{2k}. Here 21 is a chosen cutoff above γ_1 and k is the Paley–Wiener order of the test
family (Lemma testfam). **Proposition S3 (ARGUED).** Replace 21 by any Γ<H_PT and the factor ϖ by a polynomial vanishing at all ordinates ≤Γ
(finitely many; on the line by CITED verification up to H_PT). The same proof then gives λ_A ≤ C_Γ T^{a_Γ} e^{−(2Γ/e)T}. Hence
λ_A = O(e^{−ST}) for every S < 2H_PT/e, and the leading "instanton exponent" is not intrinsic: it is a property of the test family.
Its real scale is the doubly exponential zero-density threshold 2π e^{𝒜_T} (prop:env), consistent with sampling-density heuristics
(F̂ can vanish on all ordinates where the zero density is below T/π).
**Sign of the exponentially small sectors.** Any expansion of λ_A into exponentially small pieces is indexed by zero contributions
Φ_F(ρ)Φ_F(1−ρ). Each piece is |F̂(γ)|²≥0 for an ordinate on the line, and it has no definite sign otherwise. In the comb falsifiers
(O_2/O_4/O_6 of thm:shape) the archimedean Stokes data (§2) and the frozen limit (§3, with the falsifier's contacts) keep their structure,
while the zero-side pieces lose their definiteness. So the sign is not fixed by Stokes-graph topology or by median-resummation reality: reality holds
for every real comb, positive or not. **Proved partial statement:** below height H_PT every exponentially small sector of the test-family
expansion is ≥0 (CITED verification). This is exactly thm:margin's step (4) and is not new.

## 5. Self-check: six clauses (sec:spec)
(1) comb-generic? Yes: §2 data are linear in Λ, §3 holds for any comb → fails. (2) cone on log ζ: no. (3) integrality: no. (4) sparse-stable: yes
(§3 holds for any finite comb) → fails. (5) coupling Λ with FE outside ζ(½+iτ): **fails, proved** (Lemma S1, disjoint Borel rays).
(6) crossing ∂log: not reached. Everything that survives positivity is the zero-side sum = REF-D.

## 6. Verdict
NO-GO for the class 𝒦_St (Stokes/alien data of the symbol; exact-WKB sectors of λ_A in 1/T): place-additive (S1), the frozen model is perturbative and
negative (S2), and the exponential exponent is test-dependent (S3). No sign. Residual seed: a Stokes phenomenon in the **joint** variable (T, contact
count), i.e. resurgence of the windowed family as n crosses e^{2T}. That is not analytic in T (jumps at ½log n), so it needs a new object; not pursued.
