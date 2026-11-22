# CA_G_001 — Monoid invariance, SUSY factorization, and the Elias–Williamson template on the window ladder

Phase 193. Pen and paper. **No sign contact. No negative value for ζ.**

## §1 Monoid invariance (Lemma G1, PROVED)
**Lemma.** Let 𝒢 be any construction (algebra, category, Hopf algebra, involution, Hodge-type structure) depending only on the abstract
commutative monoid (ℕ^×, ·). Then 𝒢(ℕ^×) ≅ 𝒢(𝔐) for 𝔐 = the g-integers of a Beurling system with free generators, and for 𝔐 = the ideal
monoid of a number field K.
*Proof.* All three are free commutative monoids on countably infinitely many generators (fundamental theorem of arithmetic; Beurling
freeness by definition; Dedekind unique factorization). Free commutative monoids on sets of equal cardinality are isomorphic. ∎
**Consequence.** Such a positivity survives O11 and O12, so it fails (R)(10) and is comb-generic (B″). The data separating ζ is the norm
map N(n) = n: (i) the image is exactly ℕ, each value with multiplicity one (fails for ζ_K: multiplicities a_K(n); fails for Beurling: the
image is not ℕ); (ii) N is additive-compatible (ℕ is a semiring). A template "Hodge theory without a variety for ℕ" must therefore be
built on the semiring (ℕ,+,·) or on log: ℕ → ℝ, not on the monoid. Then its output is a property of the comb (Λ(n))_{n<e^{2T}}, and O7
keeps the comb (lem:shape-quartet), so (P3) fails unless the construction also reads the form. **YES→NO move proposed:** "an algebra
built from the multiplicative monoid ℕ carries the sign" → NO (PROVED, by the Lemma together with O11/O12).

## §2 SUSY / Riccati factorization (PROVED, standard)
For H = −d² + V on an interval with self-adjoint boundary conditions: H ≥ 0 ⟺ the ground state ψ₀ > 0 exists with eigenvalue ≥ 0, and
then H = A*A + E₀, with A = d/du − (log ψ₀)′ (Sturm oscillation, CITED). So "positivity from a supercharge" is equivalent to positivity:
the supercharge is built from the ground state, i.e. from the minimizer. For the window form (a Toeplitz form, not Schrödinger) G0(a)
gives the same thing: Q = 𝔞^{1/2}. The Witten-index identity H = {Q,Q*} holds for every W, hence for every comb (B″). REF-D.

## §3 The Elias–Williamson template on the window ladder
EW structure: graded object B = ⊕B^i, symmetric form ⟨,⟩, Lefschetz operator L of degree 2. Hard Lefschetz (L^i: B^{−i} ≅ B^i) plus
Hodge–Riemann (sign (−1)^i on primitive parts) are proved by induction: HR for smaller objects ⇒ HL for the next (via restriction to the
"hyperplane" B_s·B), and HL along a deformation ρ_t ⇒ HR is constant in t; it is known at one limit.
**Translation.** Ladder T_0 < T_1 < …, P_{T_k} ⊂ P_{T_{k+1}}. Natural Lefschetz: L_g F = F * g, g ≥ 0 even, supp g ⊂ [−t,t], maps P_T
into P_{T+t}, and 𝔞_{T+t}(F*g) = (1/2π)∫ σ_{T+t}|F̂|²|ĝ|².
(a) Our target is HR with only degree-0 primitives (no negative directions). The EW output is a signature, and it gives positivity
only when every non-zero degree is empty. The "signature constancy along a deformation" step needs nondegeneracy (HL) for all t: that is
CA_A_008 (integer invariant from a positive endpoint) ⇒ REF-D.
(b) Decomposition P_{T+t} = L_g(P_T) ⊕ Prim, Prim = 𝔞-orthogonal complement. Positivity on P_{T+t} ⟺ positivity on L_g(P_T), on Prim,
and the Schur complement of the cross term. On L_g(P_T) the form is the window form of the symbol σ_{T+t}|ĝ|², not 𝔞_T: new primes in
(e^{2T}, e^{2T+2t}) enter through σ_{T+t} (Theorem X: they must cancel σ on U at resolution π/T). So HR at T does not transport; the
induction step is the Schur tower L2_002 / W-lin (n₋ independent of k). Prim carries the target.
(c) What EW have that we lack: the Lefschetz operator comes from an ample class with a *positivity that is proved independently* (the
action is by multiplication by ρ with ρ(α_s^∨) > 0), and the local intersection forms are computed from the Soergel calculus, a
categorification in which every local form is a Gram matrix of light leaves with explicitly known leading signs. The analogue of the
light-leaves basis would be a basis of P_T in which 𝔞_T is block-triangular with known diagonal signs — that is an LDLᵀ (Cholesky)
certificate, class (D) as final object (G0). The genuinely non-tautological ingredient of EW is the deformation to a limit where HR is
known (ρ → ∞ along the ample cone, where the form becomes a direct sum of rank-one pieces). Window analogue: T ↓ ½log2 (no primes,
P46 positive endpoint) — CA_A_008 again.
**Verdict.** G3 = REF-D/retry (CA_A_008, L2_002, Theorem X). PROVED pieces: the identity in (b) and the reduction (a). No sign.
