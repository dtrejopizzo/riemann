# CA_J_001 — Lattice reflection positivity in prime coordinates and chessboard estimates (seeds J6, J7)

Phase 193. Pen and paper; no numerics (hand arithmetic on CITED digits shown).
Setting and Lemmas J0, J0′ as in CA_J_000 §1. **No sign contact. No negative value for ζ.**

## 1. Why this is not CA_A_007
CA_A_007 §3 treats Θf(t) = f(−t) on the log line: in group language this is q ↦ q^{−1}, the inversion of *all* prime coordinates at
once, which is the restriction to G of the map τ-reflection of ℝ. Chessboard estimates (Fröhlich–Israel–Lieb–Simon, CITED: Comm. Math.
Phys. 62 (1978); Biskup's Prague lectures, CITED) need reflection positivity for reflections in **each coordinate hyperplane of a
lattice**. On G ≅ ⊕_p ℤ the coordinate reflections are
  θ_p (site): v_p(q) ↦ −v_p(q), other valuations fixed;   θ′_p (bond): v_p(q) ↦ 1 − v_p(q).
θ_p is a monoid-level automorphism of G (·), and it is not induced by any map of ℝ: log θ_p(q) = log q − 2v_p(q)log p depends on v_p(q),
not on log q (+). This is the +/· content of the seed: chessboard estimates are an inequality machine on a lattice whose
reflections are multiplicative symmetries; the kernel's strength is additive.

**Definition (RP_p).** Write x ∈ ℤ^S for exponent vectors (S finite, p ∈ S), φ(x) := 𝖡(Σ_q x_q log q). φ is *site-RP in p* if
  R_p(s) := Σ_{x,y: x_p ≥ 0, y_p ≥ 0} s_x s_y φ(θ_p x − y) ≥ 0  for every finitely supported real s,
and *bond-RP in p* if R′_p(s) := Σ_{x_p, y_p ≥ 1} s_x s_y φ(θ′_p x − y) ≥ 0 for all such s. Translation invariance makes the choice of
hyperplane position irrelevant. Chessboard estimates on (a box of) ℤ^S require RP in every coordinate direction used.

## 2. Theorem 1 (RP fails on short windows; PROVED, unconditional)
For every prime p there is τ_p > 0 such that for every profile with T₀ ≤ τ_p: φ is neither site-RP nor bond-RP in p.
For p = 2 one may take τ_2 = 0.05.
*Proof.* Site: take s = δ_{e_p} (x = y = e_p, the point q = p). θ_p e_p − e_p = −2e_p, so R_p(s) = φ(−2e_p) = 𝖡(−2 log p) = 𝖡(2 log p),
negative for T₀ small by Lemma J0′(b). Bond: s = δ_{e_p}; θ′_p e_p − e_p = −e_p, R′_p(s) = 𝖡(log p) < 0 by Lemma J0′(a).
p = 2, 2T₀ ≤ 0.1: 𝖡(log 4) < −0.23 and 𝖡(log 2) < −0.27 (Lemma J0′). ∎
Reading: the diagonal of the reflected (Hankel) form is the kernel at the shift p² (site) or p (bond), where the Euler factor puts the
negative atom −½v_{p^k}. Toeplitz positivity tolerates negative off-diagonal values; Hankel positivity puts them on the diagonal.

## 3. Theorem 2 (characterization of RP_p under the target; PROVED)
Assume φ is PD on G, with Bochner measure ν of 𝖡 on ℝ (CA_E_001 Lemma 1). Then:
(i) site-RP in p ⟺ supp ν ⊂ (π/log p)ℤ ⟺ 𝖡 is 2 log p-periodic;
(ii) bond-RP in p ⟺ supp ν ⊂ (2π/log p)ℤ ⟺ 𝖡 is log p-periodic.
*Proof.* Write χ ∈ Ĝ as (z, χ′), z = χ(p) ∈ S¹, χ′ the restriction to G′ := ⟨primes ≠ p⟩. μ_φ = ι_*ν, so on the support z = p^{iτ},
χ′ = ι′(τ) := (q^{iτ})_{q ≠ p}. For s supported on {x_p ≥ 0} put P(w, χ′) := Σ s_x w^{x_p}χ′(x′). Since φ(θ_p x − y) = ∫ χ(θ_p x)χ̄(y)dμ_φ and
χ(θ_p x) = z^{−x_p}χ′(x′):
  R_p(s) = ∫ P(z̄, χ′)·\overline{P(z, χ′)} dμ_φ = ∫_ℝ P(p^{−iτ}, ι′τ)·\overline{P(p^{iτ}, ι′τ)} dν(τ).
(⇒) Take product vectors s_x = a_{x_p}b_{x′}, a real finitely supported on ℕ₀, b complex on ℤ^{S′} (use s and is, i.e. R_p is a
Hermitian form; real s suffices after polarization, since R_p is real-symmetric). With A(w) = Σ a_k w^k (real coefficients, so
\overline{A(p^{iτ})} = A(p^{−iτ})) and B(χ′) = Σ b_{x′}χ′(x′):
  R_p(s) = ∫ A(p^{−iτ})² |B(ι′τ)|² dν(τ) ≥ 0  for all A, B.
*Step 1 (the B-family is positivity-determining).* Let σ be a finite complex measure on ℝ with ∫|B∘ι′|²dσ ≥ 0 for every trigonometric
polynomial B on Ĝ′. Then ι′_*σ is a finite complex measure on the compact group Ĝ′ which is ≥ 0 on {|B|²}; every nonnegative
g ∈ C(Ĝ′) is a uniform limit of |B_j|² (approximate √g by B_j, Stone–Weierstrass), so ι′_*σ ≥ 0. ι′ is continuous and injective
(two primes q₁, q₂ ≠ p in G′, log q₁/log q₂ ∉ ℚ), so by Lusin–Souslin ι′(E) is Borel for Borel E ⊂ ℝ and σ(E) = ι′_*σ(ι′E) ≥ 0. Hence σ ≥ 0.
*Step 2.* Apply Step 1 to σ = A(p^{−iτ})²ν: the function A(p^{−iτ})² must be real and ≥ 0 ν-a.e., for every real polynomial A. With
A(w) = 1 + w and w = e^{−iθ}: Im(1 + w)² = −2 sin θ(1 + cos θ), which vanishes iff θ ∈ πℤ. So ν-a.e. τ log p ∈ πℤ.
(⇐) If supp ν ⊂ (π/log p)ℤ then z = p^{iτ} ∈ {±1} ν-a.e., z̄ = z, and R_p(s) = ∫|P(z, ι′τ)|²dν ≥ 0 for every s.
(ii) For bond reflection χ(θ′_p x) = z^{1−x_p}χ′(x′), so R′_p(s) = ∫ z·A(z̄)²|B|²dν with A supported on exponents ≥ 1. A(w) = w gives
z·z̄² = z̄, which must be ≥ 0 ν-a.e.: z = 1, i.e. τ log p ∈ 2πℤ. Conversely z = 1 ν-a.e. gives R′_p(s) = ∫|P(1, ι′τ)|²dν ≥ 0.
Periodicity: 𝖡 = ν̂, and ν on the lattice (π/log p)ℤ is equivalent to 𝖡(d + 2log p) = 𝖡(d) (uniqueness of Fourier–Stieltjes transforms). ∎

**Corollary 3 (two primes; PROVED modulo CITED explicit formula).** Under the premise, φ is site-RP in two distinct primes p ≠ p′ only
if supp ν ⊂ (π/log p)ℤ ∩ (π/log p′)ℤ = {0}, i.e. 𝖡 ≡ 𝖡(0). This is false: by the explicit formula in the form of P47 thm:Z (CITED),
ν = Σ_γ m_γ ĉ₀(γ)δ_γ over the zero ordinates, ĉ₀ = F̂₀² > 0 on ℝ for every profile in 𝒫_{T₀} (F̂₀ = (τ² + ¼)|ĝ|⁴ and |ĝ(τ)| ≥
|e^{ba} − 1|/|b + iτ| > 0), and ζ has a zero on the line (Hardy, CITED). Hence **chessboard estimates in ≥ 2 prime directions have no input.**

**Corollary 4 (one prime, every window; PROVED for p ≤ 7 from CITED digits, ARGUED in general).** Under the premise, site-RP in p
forces γ₁ ∈ (π/log p)ℤ, γ₁ = 14.134725… (CITED). γ₁log p/π = 3.1186 (p = 2), 4.9429 (p = 3), 7.2413 (p = 5), 8.7550 (p = 7): none is an
integer, so site-RP (and a fortiori bond-RP) fails for p ≤ 7 at **every** T₀ < ½log 2. For general p the statement γ₁log p/π ∉ ℤ is
checkable p by p; no uniform proof is claimed (ARGUED).
(These corollaries use zero ordinates only to *refute* a structural hypothesis; nothing is deduced about the sign of the window form,
and no equivalence of the target with any other statement is used.)

## 4. Proposition 5 (the +/· mechanism behind Theorem 2; PROVED for transpositions, ARGUED in general)
Let σ be an automorphism of the group G induced by a permutation/sign change of the prime coordinates, σ ≠ id, σ ≠ inversion. If
φ∘σ = φ (or more generally if a positivity of the reflected form in σ holds, as in Theorem 2), then μ_φ is carried by
ι(ℝ) ∩ σ̂^{−1}ι(ℝ), which is the image of a discrete subset of ℝ.
*Proof for σ = transposition of p, p′ and invariance.* μ_φ is σ̂-invariant and carried by ι(ℝ) (CA_E_001 Lemma 1), so it is carried by
ι(ℝ) ∩ σ̂^{−1}ι(ℝ). A point ι(τ) of this set satisfies, for some τ′, q^{iτ′} = q^{iτ} for two further primes q (hence τ′ = τ, by
irrationality of the log ratio) and p^{iτ} = p′^{iτ}, i.e. τ ∈ (2π/log(p′/p))ℤ. ∎
**Reading.** A symmetry or reflection of the *monoid* (·) is compatible with the *line* (+) only on a discrete set of frequencies; the
Bochner measure of the window kernel lives on the line and is not discrete-lattice-supported. Every statistical-mechanics method whose
input is a lattice symmetry in prime coordinates (chessboard, Gaussian domination/infrared bounds, symmetric-group averaging over
primes) is therefore excluded at the input. This is the exact place where + and · fail to meet for this class of tools.

## 5. Screens
| item | REF-D | (B″) | O7 | O11/O12 | FE-gen | [crit] | sign content |
|---|---|---|---|---|---|---|---|
| Thm 1 | no | no (uses the atom at p, p²) | — | — | — | — | NO-GO (a false hypothesis, not a value of the form) |
| Thm 2 | no | yes (holds for every comb with PD kernel) | survives | survives | yes | no | NO-GO for the RP input |
| Cor 3/4 | no | uses zeros only to refute | — | — | — | — | NO-GO |
| Prop 5 | no | yes | — | — | — | — | NO-GO for lattice-symmetry inputs |

## 6. Self-review
1. *Is Theorem 1 just CA_A_007 Thm 2?* Same phenomenon (a negative atom lands on the Hankel diagonal), different reflection; CA_A_007 needs
   concentration on the continuum, here a single lattice site suffices and the reflection is per prime. It is recorded as a
   lattice analogue, not as new mechanism. Theorem 2 (exact characterization by lattice support of ν) is new.
2. *Could a weaker RP (only on Euler-product vectors, or only after a gauge z ↦ −z) suffice for chessboard?* Chessboard needs the full
   Hankel positivity in each direction (the proof iterates Cauchy–Schwarz for the RP inner product). Gauging by a character
   (s_x ↦ ε^{x_p}s_x) replaces z by εz and only rotates the allowed lattice; Theorem 2's proof covers it.
3. *Short windows only?* Theorem 1 is for T₀ ≤ τ_p; Theorem 2 + Cor 3/4 cover every T₀ under the premise (two primes: all p; one prime:
   p ≤ 7 PROVED from digits).
4. *Uses zeros.* Only in Cor 3/4, only to refute RP, labelled. The target is never deduced.
5. *Measure theory.* Step 1 needs σ finite: A² is bounded and ν finite. Lusin–Souslin (CITED, Kechris 15.1).
**Verdict.** J6 (chessboard / lattice RP) and J7 (Gaussian domination, which needs RP): **NO-GO (PROVED)**. The RP input is false
for every profile (two prime directions) and the failure is structural: Theorem 2 identifies RP_p with lattice support of the line
measure.
