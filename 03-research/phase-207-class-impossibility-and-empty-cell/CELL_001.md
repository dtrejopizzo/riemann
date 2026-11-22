# CELL_001 — Lead 2 of phase 207: the empty-cell object

Index: `05-meta-and-planning/ROUTES-TRIED-INDEX/`.
No numerical computation was done because it was not needed:
all statements are structural or come from cited lemmas.

## Summary (≤250 words)

The question is what structure has positivity at weight n^{−1/2} and native symmetry s ↔ 1−s in the same step. I fix the
frame where the question is precise: L²(½+iℝ, w dt) with the unitary involution of the FE, J f(t) = χ(½+it) f(−t), and forms
q(a) = B(D_a, D_a) over Dirichlet polynomials D_a(t) = Σ a_n n^{−1/2−it}. There are four results.
(1) **Lemma F (PROVED).** Helson is the integral of |Σa_n n^{−σ}|² over σ ∈ [½,∞), which is a fundamental domain of σ ↦ 1−σ.
Its weight ½ is the boundary of that domain, and that is why it has no FE: extending it to all σ diverges.
(2) **Lemma V₊ (PROVED).** No nonzero Dirichlet polynomial lies in the ±1 eigenspace of J. The "projection to the +1
eigenspace" positivity only sees infinite objects.
(3) **Lemma G (PROVED given Gonek's lemma, CITED).** The FE part of every form in the algebra ⟨M_f, J⟩ is
⟨D_a, J D_a⟩_w = 2π Σ_N w(2πN)(a∗ā)(N) + error. It is a functional of the Dirichlet square: the FE turns weight ½·½ into
weight 0 over N = mn, because e(−mn) = 1. With full Euler, a∗a = a·d is linear in a.
(4) **Theorem C (ARGUED on the declared class 𝒞).** Every weight-½ positivity of the class is either a generic norm (Lemma N) or
the J part. The J part is linear in the coefficients under Euler, or depends on a∗a ≥ 0 (non-negative coefficients). None
distinguishes Λ from a_P or cΛ.
The candidates (α Helson with involution, β split Hardy, γ prime theta/RS) end up NO-GO or RETRY. New object
recorded: the split Hardy form R_w(D) = ‖Re e^{iθ}D‖²_w − ‖Im e^{iθ}D‖²_w. The cell remains empty, and now has a
precise reason why.

## 0. Corpus check

I did the mandatory grep in `ROUTES-TRIED-INDEX/` and in phases 204–207:
- **Helson / H² / multiplicative Hilbert / Bohr.** L87 (Perfekt, 05b l.39): "the only positivity at weight 1/√(mn); Λ enters
  only through ∂log ⇒ INV_F_001 predicts comb-genericity". AUDIT_2026-10-15_PHASE193 l.76: C_006 E4 Helson H²(𝔻^∞) =
  **RD + CIRC** (RD: it is the target reformulated via torus/line, CA_C_002 Prop 2; CIRC: the clause that kills it is ARGUED in P46).
  Bohr has 18 files (Bohr lift, infinite torus) and all point to the same family. RIGID_001 §2.12 and §4 (Helson⊗Estermann
  gluing) gives NO-GO ARGUED: "F only rewrites".
- **Fejér–Riesz / Perfekt.** L87. It is a boundary positivity (critical line bounded by the imaginary axis) and has no P2 (FE).
- **Estermann.** RIGID_001 §2.10, Lemma HV (generic norm), Z_CARRIER_001 and MULT_GAUGE Thm R-MOM.
- **Hardy / Riemann–Siegel / Z(t).** 04_PHASES l.878 G3C-R163_603: "Riemann–Siegel/AFE are FE-only data, shared by
  f_χ: DEAD as a separator". README l.164 (EI_003): **symbol rigidity theorem**: no exact identity on σ_T
  built with FE, Euler, Mellin, Poisson or Riemann–Siegel is nonlinear in Λ.
- **theta / Poisson / Mellin.** README l.465 (PROOF_L_SHARP_T_001): Poisson mirror 𝔉 as an exact symmetry, sectors
  𝒮_±, with "do not retry the 𝔉-sector form as a sign source without controlling 𝒫". SYNTHESIS §4: Ш/Poisson = Euler at σ = 1.
- **involution.** NG-D4 (03_PHASES l.55: "FE involution commutes, not anticommutes"). G1H-R160_S1 (real-structure
  involution j(s) = 1−s̄, REF-D). PROOF_L_SHARP_T_001 (𝔉 involution, sectors).
- **weight ½ / n^{−1/2}.** There are 7 files with "weight ½" and all point to SYNTHESIS §4 (the weight gap). "eigenspace" and
  "prime theta" do not appear in the index.
- **BARRIER_D1 Thm 4** (phase 197): every defect Δ ≥ 0, real-analytic in a family of deformations and vanishing only at
  Λ, admits both signs at the same scale. It is blind to w_T.
- **Lemma N** (RIGID_001 §5): a quadratic rigidity ‖A_F‖² − B with ‖A_F‖² generic is an empty reduction.

What is new here, with the written reason for each piece:
(a) Formulating the cell as spectral theory of the involution J on L²(critical line). The index has the involution as a
symmetry (NG-D4, 𝔉-sectors in the test space 𝒮). Never as an operator on the space of weight-½ *coefficients*, where
the question is "when is ⟨D_a, J D_a⟩ ≥ 0?"
(b) Lemma G: the J part of every weight-½ form is the Dirichlet square (a∗ā) evaluated at integers. This does not appear.
(c) Reading Helson as an integral over a fundamental domain of the FE does not appear.
What is not new, and I mark as RETRY: the Hamburger defect ‖P_X − J P_X‖² (BARRIER_D1 Thm 4), the Riemann–Siegel
structure as a separator (G3C-R163_603), and the Helson gluing with additive twists (RIGID_001 §4).

## 1. The frame: the critical line as the line of unitarity, and J

Let H_w = L²(ℝ, w(t)dt) with w ≥ 0, even, integrable and smooth. I identify t with s = ½+it. Let
  χ(s) = 2^s π^{s−1} sin(πs/2) Γ(1−s),  ζ(s) = χ(s)ζ(1−s).
On the line, |χ(½+it)| = 1 and χ(½+it) = e^{−2iθ(t)}, with θ the Riemann–Siegel phase (CITED, Titchmarsh §4.17). Also
χ(½+it)χ(½−it) = 1.

**Definition 1.1 (FE involution).** (J f)(t) := χ(½+it) f(−t).

**Lemma 1.2 (PROVED).** J is unitary on H_w because w is even and |χ| = 1, and moreover J² = I. Hence
H_w = V₊ ⊕ V₋ (±1 eigenspaces, orthogonal), with P_± = ½(I ± J).
*Proof.* J²f(t) = χ(½+it)χ(½−it)f(t) = f(t), and ‖Jf‖² = ∫w(t)|f(−t)|²dt = ‖f‖². ∎

There is a second, antilinear object: K f(t) := χ(½+it)·\overline{f(t)}. Also K² = I. The Hardy function
Z(t) = e^{iθ(t)}ζ(½+it) is real, and that is equivalent to Kζ = ζ on the line. For real coefficients,
\overline{D_a(t)} = D_a(−t), so on the real subspace J and K coincide. Below I use J.

**Weight-½ Dirichlet polynomials.** For a = (a_n)_{n≤X}, D_a(t) := Σ_n a_n n^{−1/2−it}. The weight n^{−1/2} is
exactly the one that places n^{−s} on the Mellin line of unitarity: the critical line is the only vertical axis
where J is unitary. This is the identification "weight ½ = critical line = line of unitarity", and it requires no hypothesis.

**Lemma 1.3 (PROVED).** (J D_a)(t) = χ(½+it) Σ_n a_n n^{−1/2+it}. In particular, for a real,
  ⟨D_a, J D_a⟩_w = ∫ w(t) \overline{χ(½+it)} D_a(t)² dt = ∫ w(t) e^{2iθ(t)} D_a(t)² dt.
The value is real because w is even and a is real. For complex a, D_a·D_{ā} appears, and the form is sesquilinear in a.
*Proof.* Direct substitution. Reality comes from the change t ↦ −t, using θ(−t) = −θ(t). ∎

**Corollary 1.4 (PROVED).** For a real,
  ⟨D_a, J D_a⟩_w = ‖Re(e^{iθ}D_a)‖²_w − ‖Im(e^{iθ}D_a)‖²_w =: R_w(D_a).
*Proof.* e^{2iθ}D² = (e^{iθ}D)², and Re(u²) = (Re u)² − (Im u)². ∎

I call R_w the **split Hardy form**: the energy of the "Hardy part" of D minus that of its transverse part. For ζ
the transverse part is zero. R_w is the most natural form with weight ½ and FE in the same step: weight ½ lives in D_a,
the FE acts as an operator (J), and the required positivity is R_w ≥ 0. I answer the central question of the order.

**Proposition 1.5 (PROVED).** For f ∈ H_w, ⟨f, Jf⟩ = ‖P₊f‖² − ‖P₋f‖². It is ≥ 0 if and only if the +1 component dominates
the −1 one. The form has signature (∞, ∞): it is indefinite on any subspace that meets V₋. Bounded Hermitian forms that are
≥ 0 and J-invariant (B(Jf, Jg) = B(f, g)) are exactly the averages ½(B′ + J*B′J) of forms B′ ≥ 0.
*Proof.* The first part is projector algebra. For the second: if B is J-invariant, B = ½(B + J*BJ). If B′ ≥ 0,
its average is ≥ 0 and invariant. ∎

**Reading.** An FE used only as a *symmetry* of a positive form contributes no positivity (1.5, second part). This
reproduces, in this frame, the "FE only as symmetry" clause from lead 1. For the FE to *produce* a sign, the form must
be indefinite on H_w and semidefinite only on a subspace defined by the FE. The canonical example is ⟨f, Jf⟩ restricted to
V₊, where it equals ‖f‖² and is trivial. The nontrivial question is which subspaces 𝒰 ⊂ H_w, defined by Euler, satisfy
⟨·, J·⟩|_𝒰 ≥ 0. That is what §§3–4 examine.

## 2. The extreme (α): Helson, verified and reinterpreted

**Lemma 2.1 (PROVED; verifies the integral representation).** Let a = (a_n)_{2≤n≤X}, and let f_a(σ) = Σ_n a_n n^{−σ} for real σ.
Then
  ∫_{½}^{∞} |f_a(σ)|² dσ = Σ_{m,n≥2} a_m ā_n / ( √(mn) · log(mn) ).
*Proof.* |f_a|² = Σ a_m ā_n (mn)^{−σ} and ∫_{½}^{∞} x^{−σ}dσ = x^{−1/2}/log x for x > 1. The sum is finite, so it can be
interchanged. ∎
n = 1 must be excluded, because the term m = n = 1 diverges. There is also a minor correction to RIGID_001 §2.12: there
the identity is written with a factor 2 in front of the integral, and the correct identity does not carry it. The sign and
conclusion of RIGID_001 do not change.

**Lemma 2.2 (Helson lives in a fundamental domain of the FE; PROVED).** On the real axis, the FE reflection is σ ↦ 1−σ and
has fixed point ½. The half-axis [½, ∞) is a fundamental domain of that reflection, and the Helson form is the integral of |f_a|²
over that domain. Its "invariant extension" ∫_{−∞}^{∞} |f_a|² dσ diverges for every a ≠ 0, because n^{−σ} → ∞ as
σ → −∞. If instead one uses the FE version, ∫_{−∞}^{½} |χ(σ)f_a(1−σ)|²dσ, one gets Σ a_m ā_n ∫ χ(σ)²(mn)^{σ−1}dσ.
That integral also diverges, because Γ(1−σ)² grows as σ → −∞.
*Proof.* Immediate from 2.1 and from Γ(1−σ) → ∞ superexponentially. ∎

**Reading (ARGUED, but structural).** Helson's weight ½ appears because the integral starts at the boundary of the FE's
fundamental domain. Helson's positivity is a norm (integral of a squared modulus) over the "unpaired" half
of the FE. The FE cannot act on the form because the form does not see the other half. This explains why extreme (α)
has weight ½ and no FE: **weight ½ = boundary of the reflection's fundamental domain, and a positivity at the boundary
is a one-sided positivity.**

For the same reason, the automorphic norms of extreme (β) integrate over a fundamental domain of a group that contains the
FE (Γ\ℍ). Unfolding against the Eisenstein series puts the reading abscissa at Re s = 1 (Petersson unitarity ⇒
|a_n|²/n^{k}). That is SYNTHESIS §4 (ii): Rankin–Selberg at σ > 1, Maass–Selberg at abscissa 1, CA_A_006 (transport 1 → ½
NO-GO PROVED).

## 3. Candidate (1): Helson with involution, and the quadratic Hamburger defect

**Definition 3.1.** For a Dirichlet polynomial D_a, the "Hamburger dual" is J D_a (Lemma 1.3). The quadratic defect
at weight ½ is
  𝔇_w(a) := ‖D_a − J D_a‖²_w = 2‖D_a‖²_w − 2 Re⟨D_a, J D_a⟩_w = 4‖P₋ D_a‖²_w.

**Lemma 3.2 (V₊ and V₋ contain no Dirichlet polynomials; PROVED).** If D_a = ±J D_a on the line (for all t, with w > 0 on
an open set and analytic continuation), then a = 0.
*Proof.* The equality D_a(s) = ±χ(s)D_a^♯(1−s), with D_a^♯(s) = Σ a_n n^{−s}, holds on the line and by analyticity throughout ℂ
except at the poles of χ. The left side is entire and bounded on each vertical strip. I use the bound on χ in vertical strips:
|χ(σ+it)| ≍ (|t|/2π)^{½−σ} (CITED, Titchmarsh (4.12.3)), and
D_a^♯(−2+it) is bounded. Then D_a(3+it) = O(|t|^{−5/2}) → 0. But a nonzero Dirichlet polynomial is almost periodic
in t and does not tend to 0 unless it is identically 0 (its mean square is Σ|a_n|²n^{−6} > 0). ∎

**Consequence.** 𝔇_w(a) > 0 for every nonzero finite a. The "positive by FE" form ⟨D, JD⟩|_{V₊} is empty on finite objects.
This is the spectral version of Thm finZ of P46 §7 (row D is intrinsically infinite): **the FE only has infinite
eigenvectors.** Euler enters only through the entire series (ζ ∈ V₊ in a regularized sense), not through
truncations.

**Does BARRIER_D1 Thm 4 cover this? Yes.** Take the natural family Λ ↦ P_X[Λ] = exp(Σ_{n≤X} Λ(n)n^{−s}/log n), i.e. the
truncated Euler product of log P_X. Then Δ(Λ) := 𝔇_w(coefficients of P_X[Λ]) is ≥ 0 and real-analytic in Λ (exponential of a
linear form, then quadratic). In the regularized limit X → ∞ it vanishes only at the FE's location: by Hamburger, in the
class with a simple pole, the zero is ζ (CITED, BARRIER_D1 Prop 1). Those are exactly the hypotheses of Thm 4: Δ ≥ 0, analytic
along a deformation and zero only at Λ. Conclusion: it is blind to w_T, because both signs of the
deformation are admitted at the same scale ε^{1/2m}. The defect being *quadratic* does not take it out of Thm 4. Thm 4 only uses
that s ↦ Δ(u(st*)) is analytic, nonnegative and not identically zero, and a quadratic form composed with an analytic
deformation is such a thing.
**Candidate (1): RETRY of BARRIER_D1 (NO-GO by Thm 4).** I have no new reason. Using the Helson norm instead of the
L²_w norm changes nothing either, because it is also analytic in a.

## 4. Candidate (2): the split Hardy form R_w and Lemma G

The positivity R_w(D_a) ≥ 0 (Cor. 1.4) is a serious candidate for the cell: native weight ½, FE as an operator, and sign as a
concrete inequality. I compute it.

**Lemma 4.1 (Lemma G: J part = Dirichlet square; PROVED given Gonek's lemma, CITED).** Let w be smooth, even, with support
on ±[T₁, T₂], T₁ ≫ 1, and with w^{(j)} ≪ T₁^{−j}. For real a, supported on n ≤ X and X² ≤ T₂/2π,
  ⟨D_a, J D_a⟩_w = 2π Σ_{N≥1} w(2πN)·(a∗a)(N) + E_w(a),  (a∗a)(N) = Σ_{mn=N} a_m a_n,
with |E_w(a)| ≪ Σ_{m,n} |a_m a_n| (mn)^{−1/2}·(1 + T₁^{−1/2}√(mn))·(tail of w), i.e. of lower order on the scale of w.
*Proof (full sketch).* Expanding, ⟨D_a, J D_a⟩_w = Σ_{m,n} a_m a_n (mn)^{−1/2} I(mn), with
I(r) = ∫ w(t) e^{2iθ(t) − it log r} dt. The phase φ(t) = 2θ(t) − t log r has φ′(t) = log(t/2π) + O(t^{−2}) − log r. The stationary
point is t₀ = 2πr, where φ″ = 1/t₀ and φ(t₀) = −2πr − π/4 + O(1/r). Stationary phase (Gonek 1984, Lemma 5, CITED)
gives I(r) = w(2πr)·√(2π t₀)·e^{iπ/4}·e^{−2πir − iπ/4} + error = 2π√r·w(2πr)·e(−r) + error. For r = mn an integer, e(−mn) = 1.
The t < 0 part conjugates, and the value is real because a is real. ∎

**Reading of Lemma G.**
(i) The weight. The factor (mn)^{−1/2} of the weight ½ cancels with the √(mn) from stationary phase. **The FE turns weight ½ ⊗
weight ½ into weight 0 over N = mn, with conductor t/2π.** This is the weight gap from SYNTHESIS §4 in its exact form: the FE part of
a weight-½ form reads the coefficients of the *Dirichlet convolution* without weight, at height t ≈ 2πN.
(ii) The semiring. The identity e(−mn) = 1 (additive character evaluated at an integer product) is exactly the (ℕ,+,·)
interaction that the semiring principle calls for. It appears natively. But the result is positive with *any* sign of
phase, because e(−N) = 1 for every integer N. Integrality contributes a trivial phase sign, and the form's sign is left
in the hands of (a∗a)(N).
(iii) Euler as structure. If a is completely multiplicative, (a∗a)(N) = a_N·d(N), and the J part is
2π Σ_N w(2πN) d(N) a_N: **linear in a**. Full Euler collapses the quadratic form into a linear functional weighted by d.
This does distinguish quartets (FE without Euler, which do not collapse). It does not distinguish a_P, which is also
completely multiplicative and collapses the same way. For the node, Λ must go into the coefficients. If D = −ζ′/ζ truncated,
a = Λ and (Λ∗Λ)(N) ≥ 0: the positivity is one of non-negative coefficients.

**Corollary 4.2 (PROVED given 4.1).** Let Q(a) = ‖D_a‖²_w for real a. Then
  R_w(D_a) = 2π Σ_N w(2πN)(a∗a)(N) + E_w(a),  ‖D_a‖²_w = ŵ(0)Σ a_n²/n + (off-diagonal, ŵ(log(m/n))).
For a ≥ 0, R_w ≥ 0 at main order. For a ∈ {Λ, a_P, cΛ, the coefficients of Epstein's Λ_Q, Λ_DH in its absolute-value
version} the same holds. The falsifier passes all of them.

**Verdict for candidate (2).** NO-GO ARGUED: the positivity reduces to "non-negative coefficients", which is generic (RIGID_001
l.137: NO-GO PROVED for positivity of non-negative coefficients plus F). The part that is not of main order, E_w, is the
Riemann–Siegel transition zone (mn ≈ t/2π at the edge of w's support). That is exactly the structure
G3C-R163_603 declared DEAD as a separator ("FE-only data, shared by f_χ"). New reason versus G3C: here the question is about
the sign of a quadratic form, not about a coupling with witnesses. Reason it dies the same way: Lemma G shows
that the only non-generic term is linear in a∗a, so Theorem X (bilinear in Λ ⇒ functional of h*) and the symbol rigidity
theorem (EI_003) reach it. **New object recorded: R_w and Lemma G.**

**On Z(t)² ≥ 0 and Z(t)·(something) ≥ 0.** Z(t)² ≥ 0 is trivial: Z is the component of ζ in V₊, and ‖P₊ζ‖² ≥ 0 is a norm. If
the Riemann–Siegel formula Z = 2Σ_{n≤√(t/2π)} n^{−1/2}cos(θ − t log n) + R is used, any positivity of the form
∫ w Z·G ≥ 0, with G built from the main sum, is linear in the coefficients 1. Sign changes of Z
(Hardy–Littlewood) belong to the zero side (CITED). There is no sign step. RETRY of G3C-R163_603.

## 5. Candidate (3): theta with Euler and Rankin–Selberg with a non-modular factor

**Definition 5.1.** θ_Λ(z) := Σ_n Λ(n) n^{−1/2} e(nz), with z = x+iy ∈ ℍ.

**Lemma 5.2 (PROVED).** θ_Λ is not modular for any congruence subgroup. If it were, its L-series, Σ Λ(n)n^{−s−1/2},
would have an entire continuation apart from finitely many poles and a gamma FE. But −ζ′/ζ(s+½) has poles at every shifted
zero of ζ. The "modularity defect" θ_Λ(−1/z) − (factor)θ_Λ(z), integrated against a Gaussian test, is the explicit formula
with a Gaussian test, linear in Λ (README, Theorem X). ∎

**Rankin–Selberg with |θ_Λ|².** Unfolding ∫_{Γ\ℍ} |θ_Λ|² E(z,s) dμ requires |θ_Λ|²y^{1/2} to be Γ-invariant, and it is not (5.2).
The only thing that remains well-defined is the integral over the strip Γ_∞\ℍ:
  ∫_0^∞∫_0^1 |θ_Λ(z)|² y^{s} dx dy/y² = Γ(s−1)(4π)^{1−s} Σ_n Λ(n)² n^{−1}·n^{1−s}.
It is **diagonal** (orthogonality in x kills m ≠ n) and at weight n^{−1}·Λ². m+n does not appear. This is SYNTHESIS §4 (ii): RS reads
at weight n^{−1}.
**The m+n.** It only appears in the *non-conjugated bilinear* form θ_Λ(z)², whose coefficients are Σ_{m+n=k}Λ(m)Λ(n)(mn)^{−1/2}.
These are non-negative coefficient by coefficient, without the FE. A form Σ_{m,n}Λ(m)Λ(n)(mn)^{−1/2}K(m,n), with K positive-
definite and induced by an FE, requires an FE acting on K. The only available FEs (Jacobi on θ, J on the line) give, by
Lemma G, K(m,n) = k(mn) (multiplicative Hankel), which is a function of mn and not of m+n.
**Product θ_Λ·θ_Jacobi (weight ½ + ½).** The Jacobi factor is modular of weight ½ in Γ₀(4). θ_Λ is not, so the product
is not either. Unfolding against E(z,s) is again illegitimate, and the strip integral gives the series Σ_{n} Λ(n)n^{−1/2}·r(n)·n^{−s}
(with r the squares): linear in Λ.
**Verdict for candidate (3).** NO-GO ARGUED, for three reasons: (a) without automorphy there is no unfolding; (b) what survives
is diagonal (RS, weight n^{−1}) or linear in Λ (explicit formula); (c) m+n appears only with coefficients ≥ 0, which is generic.
It did not appear in the index as "prime theta", but it falls into the Ш/Poisson (V1.3) and Theorem X families.

## 6. Candidate (4): Weil form with a weight-½ test plus Euler

This is already row D (K2 of the grid). It is not a candidate.

## 7. Candidate (5): compressions of J to Euler-defined subspaces (own invention)

By Prop. 1.5, for the FE to produce a sign, the form must be ⟨·, J·⟩ (or B = M_f + M_g J) restricted to a subspace
𝒰 that is not V₊ and on which it is ≥ 0. I examine the natural "Eulerian" 𝒰's.

**7.1 𝒰_mult = {D_a : a completely multiplicative}.** It is not a linear subspace (it is a variety). On it, by Lemma G,
⟨D_a, J D_a⟩ = 2π Σ_N w(2πN)d(N)a_N + E. Positivity over the variety: for a_p ∈ [−1, 1], a_N = λ(N) (Liouville, a_p = −1)
gives Σ_N w(2πN)d(N)λ(N). Its sign depends on w. There is no uniform positivity over the variety: NO-GO by counterexample
within the variety (ARGUED; the sign of Σ d(N)λ(N)w(2πN) oscillates with the support of w).

**7.2 𝒰_X = span{n^{−1/2−it} : n X-friable}.** It is a linear subspace stable under the product (semigroup of friables), and
Euler enters as structure: it is the "Mellin image" of the Euler product over p ≤ X. The compression P_{𝒰_X} J P_{𝒰_X} has,
by Lemma G, matrix (a,b) ↦ 2π Σ_N w(2πN)(a∗b)(N), with N friable. It is a multiplicative Hankel form on the semigroup of
X-friables, with symbol w(2πN). By Helson's theory of multiplicative Hankel forms (CITED, Helson 2006;
Brevig–Perfekt, family L87), its signature is given by the symbol as a function on the infinite torus 𝕋^{π(X)}:
ψ(z) = Σ_N w(2πN)z^{α(N)}. The form is ≥ 0 on 𝒰_X if and only if ψ is positive as a measure. But ψ is a trigonometric
polynomial with mean w(2π) (the N = 1 term) and is not positive for generic w. **Indefinite: NO-GO PROVED (given Lemma G)**
for the friable compression. Moreover, the torus 𝕋^{π(X)} is exactly the Bohr lift. That is C_006 E4 Helson H²(𝔻^∞) (RD +
CIRC, AUDIT l.76), so in its full form it is a RETRY.

**7.3 𝒰_{a_P} versus 𝒰_Λ.** The question is whether the object distinguishes "Euler over all primes" from "almost all".
In the J frame, everything that is not generic is linear in a∗a (Lemma G). If a prime P is erased, the multiplicative variety
changes at a_{P^k}. The linear functional changes by Σ_k w(2πP^k…)·(…), with no sign structure whatsoever. **There is no
structural distinction, only one of values.** This is property (i) of the node, and here it fails explicitly.

**7.4 The two-operator version (J and antilinear K).** For complex coefficients, J ≠ K. The form ⟨f, JKf⟩ is the one that
detects "real coefficients", which is a Galois symmetry and not the FE. ⟨f, Jf⟩ − ⟨f, Kf⟩ vanishes on the reals. It
contributes no sign: it is the Kronecker parity of SYNTHESIS §4 (i) in different clothing (conjugation ↔ (−1)^j in p^j). ARGUED.

## 8. The cell obstruction theorem

**Class 𝒞 (declared).** Real quadratic forms q(a) = B(D_a, D_a) over finitely supported real coefficients, with
D_a(t) = Σ a_n n^{−1/2−it} (weight ½), and B in the algebra generated by the multipliers M_f (f ∈ C_b(ℝ)) and the FE
involution J. Every B of that type is M_f + M_g J (Lemma 8.1). With w = |g| satisfying the hypotheses of Lemma G, q = q_f + q_g.

**Lemma 8.1 (PROVED).** J M_f J = M_{f(−·)}. Therefore the generated algebra is {M_f + M_g J}, and every B in 𝒞 has that form.

**Theorem C (cell obstruction; PROVED in the algebraic part, ARGUED in the stationary-phase error).**
For every q ∈ 𝒞:
(C1) q_f(a) = ∫ f|D_a|² is either (i) a generic norm if f ≥ 0 (Lemma N reduces it to empty), or (ii) indefinite in coefficients if f
changes sign, without the FE.
(C2) q_g(a) = 2π Σ_N ĝ-cutoff(2πN)(a∗a)(N) + E_g(a) (Lemma G). It is a functional of the Dirichlet square: linear in a for
completely multiplicative a, and ≥ 0 at main order when a ≥ 0.
(C3) The pure FE part, positive on V₊, is empty on finite objects (Lemma 3.2). Every defect ‖P₋D‖² falls under BARRIER_D1 Thm 4.
(C4) Consequently, every sign step in 𝒞 is of one of three types: a generic norm, a linear functional of Λ (reached by
Theorem X and symbol rigidity), or non-negative-coefficient positivity. All three pass a_P and cΛ (c > 0). Only the
collapse of C2 separates quartets, and it is linear and therefore has no sign of its own.

**Answer to the central question of the order.** "When is ⟨f, Jf⟩ ≥ 0 on a subspace?" is answered as follows: exactly when the
compression P_𝒰 J P_𝒰 ⪰ 0. For 𝒰 = V₊ this is trivial and empty on finite objects (3.2). For a linear Eulerian 𝒰, it is the
positivity of the Helson symbol of a multiplicative Hankel form (7.2), which fails. The cell "weight ½ + native FE +
positivity" is empty *in the class 𝒞* for a representational reason. On the line of unitarity, the FE is a unitary
involution J, and its action on weight-½ coefficients is, by stationary phase, the Dirichlet convolution evaluated at
integers (e(mn) = 1). A quadratic positivity in coefficients that involves J is, then, a positivity of the Dirichlet
square, and under Euler that is linear.

**What Theorem C does NOT cover (OPEN, direction for a future object).**
(O1) Forms B outside the algebra ⟨M_f, J⟩: for example, operators that mix heights t non-locally (integrals with
kernel K(t, t′)). Lemma G does not apply, and the object would have to be non-diagonal in height. Example: the pole kernel
1/(¼+(t−t′)²) of the node is of this type. The node lives outside 𝒞, in the compression to compactly supported functions, which
is not J-stable. That is why the empty cell and the node are not the same object.
(O2) Non-quadratic positivities in a (degree ≥ 3, or determinants). A multiplicative Hankel determinant on the
friable semigroup (7.2) does not reduce to a∗a. I did not examine it.
(O3) Weight ½ off the line: integrals over σ ∈ (½−δ, ½+δ) with the FE pairing σ ↔ 1−σ, i.e. the truncated symmetric
version of Helson (2.2) with cutoff δ. It is finite. It is symmetric under J *only if* f_a(1−σ) is replaced by χ·f_a^♯, and then it
is indefinite (by 1.5). Its positivity for small δ is a perturbation of the line (C1–C2). ARGUED: contributes nothing.

## 9. Falsifiers

| object | a_P | quartets (FE without Euler) | cΛ | Epstein h>1 | DH | label |
|---|---|---|---|---|---|---|
| (α) Helson | passes (norm) | passes | passes | passes | passes | generic norm (Lemma N) |
| (1) Hamburger defect ‖P₋D‖² | — | — | — | — | — | RETRY BARRIER_D1 Thm 4 |
| (2) R_w = ⟨D, JD⟩ | passes (coef ≥ 0) | different collapse, no sign | passes | passes | passes in |a| | NO-GO ARGUED (Lemma G) |
| Z², Z·G | trivial / linear | — | — | — | — | RETRY G3C-R163_603 |
| (3) θ_Λ, RS, θ_Λ·θ | diagonal/linear | — | passes | — | — | NO-GO ARGUED |
| (5) friable compression | indefinite | — | — | — | — | NO-GO PROVED given Lemma G; Bohr = RETRY C_006 E4 |
| (5) multiplicative variety | oscillates (λ) | — | — | — | — | NO-GO ARGUED |

"Passes" means the positivity holds for the falsifier too, so the object does not distinguish it and is useless.

## 10. Honest verdict

- **None of the examined candidates** gives a precisely defined object that passes the falsifiers on paper.
- **New PROVED results:** Lemma 2.1 (Helson verified, without the factor 2), Lemma 2.2 (Helson = integral over a fundamental
  domain of σ ↦ 1−σ), Lemma 1.2/Prop 1.5 (J unitary, J-invariant forms ≥ 0 = averages), Lemma 3.2 (V_± contain no Dirichlet
  polynomials), Lemma 8.1.
- **PROVED given CITED (Gonek):** Lemma G (4.1): the FE part of a weight-½ form is 2πΣ_N w(2πN)(a∗a)(N), from e(−mn) = 1.
- **ARGUED:** Theorem C on the class 𝒞 (the stationary-phase error is controlled only at main order), and the verdicts
  for candidates (2), (3) and 7.1.
- **OPEN:** forms outside the algebra ⟨M_f, J⟩ (O1); degree-≥3 positivities / multiplicative Hankel determinants (O2).
- **Necessary condition for a future object (from C + O1):** it must be non-local in height t (non-diagonal in Mellin) and
  at the same time use J. Equivalently, it must couple the FE with a support compression, which is what the node does. The
  empty cell, formulated only with "weight ½ + FE", has no object in 𝒞. The missing ingredient is non-locality in t, not a new
  (weight, FE) pair.

## 11. Index entry (for ROUTES-TRIED-INDEX)

- **CELL_001 (phase 207, lead 2, inventor; new reason: the cell "weight ½ + FE + positivity" as spectral theory of the FE's
  involution J on L²(critical line) over weight-½ coefficients):** Lemma G (PROVED given Gonek): ⟨D_a, JD_a⟩_w =
  2πΣ_N w(2πN)(a∗a)(N) + error (e(−mn) = 1; the FE turns weight ½⊗½ into weight 0 at N = mn; Euler collapses it to linear). Helson =
  integral over a fundamental domain of σ ↦ 1−σ (no factor 2; corrects RIGID_001 §2.12). V_± ∩ {Dirichlet} = {0}. Theorem C
  (ARGUED in the algebra ⟨M_f, J⟩): every positivity is a generic norm, linear in Λ, or one of non-negative coefficients.
  Split Hardy form R_w NO-GO ARGUED; Helson+involution = RETRY BARRIER_D1 Thm 4; prime theta/RS NO-GO ARGUED; indefinite
  friable compression (= C_006 E4). OPEN: forms non-local in t (O1) and of degree ≥ 3 (O2). Empty cell in 𝒞. (`03-research/phase-207-class-impossibility-and-empty-cell/CELL_001.md`) Row D OPEN.
