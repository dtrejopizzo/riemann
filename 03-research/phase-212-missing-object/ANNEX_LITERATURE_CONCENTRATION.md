# Annex — literature: concentration-type positivity mechanisms

Phase notation: a_T(F) = Arch(F) − Σ_n v_n c_F(log n), v_n = 2Λ(n)/√n, F real, supp F ⊂ [−T,T],
∫F e^{±t/2} = 0; Arch(F) = ∫W F² + ¼∬K(|t−s|)(F(t)−F(s))², K(u) = 1/(2sinh(u/2)) + 1/(2cosh(u/2)).

Tool-search note. Nothing is derived and it is not claimed that the solution is in the literature.
What is sought: a positive expression that is at the same time (a) of concentration type (transform followed
by restriction), (b) isometric only for the true integers (uses Σ_{d|n}Λ(d) = log n and the equal
spacing), (c) non-local per prime, (d) exact, (e) of dimension growing with the window.

Labels: CITED = what the article states; ARGUED = own reading. Theorem numbers are those of the
arXiv version consulted; those given «without number» could not be read in the primary source and must be verified
before citing them elsewhere. The same applies to journal data (volume, year) for items whose
arXiv record does not carry them: the arXiv identifier is the checked datum. For each item the following are indicated: sign mechanism; whether it sees additive and
multiplicative structure; behaviour under (i) weight ×2, (ii) deletion of a prime power, (iii) Beurling system;
class of the taxonomy of `ROUND_009_G3.md` §1 (1–25).

**Conclusion in advance.** No item gathers the five features. In particular, none has a
sign depending on the exact values of the weight: all the mechanisms found are either
weight-free (they depend on the nodes, not on v_n), or inequalities with slack, or identities valid for
every comb. There are five mechanisms without substantive mark in the corpus (§6); none passes the gate as it stands.

---

## 0. Prior cross-check with the corpus

Almost the whole requested perimeter is already recorded. The index entry is given (IDX =
`05-meta-and-planning/ROUTES-TRIED-INDEX/`) so as not to repeat it; of these items only what the
corpus did not use is reported.

| Topic | Where it is | Status there |
|---|---|---|
| Radchenko–Viazovska, Bondarenko–Radchenko–Seip, Kulikov–Nazarov–Sodin | `phase-35-five-fronts/101-…`; IDX P35-4, L30, L102 | NO-GO (refutation independent of the weight) |
| Crystalline measures, Kurasov–Sarnak, Olevskii–Ulanovskii, Wei | IDX L30, L60, L101; R162_1002 | low / not applicable |
| Magic functions, CKMRV | IDX fronts L, N | NO-GO (thm:O) |
| Sign uncertainty | 8 files; IDX 1 | no route |
| Prolates, Sonin, semilocal form, spectral triples, truncated form | IDX L06–L09, L39–L41, L68, L106; phase 183 | Sonin chain PROVED without sign |
| de Branges, Kreĭn, Hermite–Biehler, Lagarias, Burnol (co-Poisson, conductor operator), Suzuki, Bombieri, Yoshida | IDX L02, L03, L11, L12, L16, L17, L20, L36, L38 | used / reformulation |
| H² of Dirichlet series, Hedenmalm–Lindqvist–Seip, Helson, Perfekt, multiplicative Hilbert matrix | IDX L87; `AUDIT_PHASE193`; phase 159 (G1_P2_R3) | only upper bounds; generic in the comb |
| Nyman–Beurling, Báez-Duarte, Vasyunin, Bettin–Conrey | IDX L18, L61, L79, L95; phase 150 (T3); G2_B10_R1 | reformulation; Vasyunin «not used in row D» |
| Toeplitz algebra of ℕ ⋊ ℕ^× (Laca–Raeburn), Bost–Connes | phase 159 (G1_B5_R3, G1_P4_R5) | cited |
| Differential commutant of the window (bispectrality) | `phase-200-sign-object/SPEC_SIGN_OBJECT_011.md`; IDX README CS0_COMMUTE_001 | order ≤ 2 PROVED trivial; order > 2 OPEN |
| Reflection positivity | class 17; R-K1 | per place / boundary, excluded |
| Determinantal processes | IDX G8D-R160_S5; `ROUND_009_G3.md` §3 | «not virgin» |
| SOS / Positivstellensatz | IDX front E, G2C-159 | REF-D |
| Borodin–Okounkov | only phase 67 (another object) | not applied to the window |

No match in `03-research/` nor in `05-meta-and-planning/` (grep; does not prove conceptual novelty):
«hyperbolic Fourier series», «quasimodular», «Serre derivative», «Dritschel», «Geronimo», «Neeb»,
«Katsnelson», «Olofsson», «reflect… differential operator». With a single match: «Heisenberg
uniqueness» (note on a bibliographic gap in `phase-47-live-fronts/148-…`), «Frank–Lieb / inversion
positivity», «Ramos», «Stoller».

---

## 1. Fourier interpolation, uniqueness pairs, crystalline measures

**1.1 Bondarenko–Radchenko–Seip.** A. Bondarenko, D. Radchenko, K. Seip, *Fourier interpolation with zeros
of zeta and L-functions*, Constr. Approx. 57 (2023); arXiv:2005.02996. Theorem 1.1 (CITED): for f even,
analytic in a strip |Im z| < ½+ε with weighted integrability, f is reconstructed from the values of f̂ at
the nodes log n/(4π), n ≥ 1, and from the values (with derivatives up to the multiplicity) of f on a second
discrete set, the one in the title; the basis functions U_n, V are entire, even, rapidly decaying, and
the formula ceases to hold if a single node is removed. Theorems 2.1–2.2: Dirichlet series kernels
associated with the sequence and its dual. Section 5 covers other series, including a subsection «Dirichlet
series without Euler products».
- Mechanism: linear duality identity (weakly holomorphic modular forms for the theta group);
  there is no sign statement.
- Additive/multiplicative: uses the nodes log n (additive in n via the theta group) and the functional equation;
  does not use the Euler product.
- Falsifiers: (i) does not depend on the weight, does not break; (ii) the node log n is still there even if
  v_n is deleted, does not break; (iii) breaks (needs the integers as nodes), but because of the nodes, not the weight.
- Class 20 (identity valid for every comb with those nodes). What the corpus did not use: the
  minimality statement («no node is superfluous»). ARGUED: it is a property of the pair of sets, not of v_n; it does not
  distinguish cΛ from Λ. It enables nothing.

**1.2 Kulikov–Nazarov–Sodin.** A. Kulikov, F. Nazarov, M. Sodin, *Fourier uniqueness and non-uniqueness
pairs*, J. Math. Phys. Anal. Geom. 21 (2025); arXiv:2306.14013. Definition 2 (CITED): (Λ,M) is
supercritical if limsup |λ_j|^{p−1}(λ_{j+1}−λ_j) < ½ and limsup |μ_j|^{q−1}(μ_{j+1}−μ_j) < ½, 1/p+1/q = 1;
subcritical with liminf > ½. Theorem 1: supercritical ⟹ uniqueness pair; subcritical ⟹ non-uniqueness.
Theorem 2: for separated supercritical pairs, c‖f‖² ≤ Σ weights·|f(λ)|² + Σ weights·|f̂(μ)|² ≤ C‖f‖² on a
symmetric Sobolev space ℋ_{s,p,q}. Corollary 2: interpolation formula. Corollary 3: for every
supercritical pair there are nontrivial crystalline measures, in infinite dimension.
- Mechanism: Poincaré–Wirtinger inequalities in the gaps between nodes, then Phragmén–Lindelöf. It is a
  coercive frame-type lower bound, with non-explicit constants.
- Falsifiers: no weight; insensitive to (i) and (ii); depends only on the node density, so a
  Beurling system with the same density preserves it.
- Class 21 (estimate with remainder). ARGUED: at the critical point (constant exactly ½) Theorem 2 gives
  no bound; the target form lives in that regime (exponentially small margin). What is unused in the
  corpus is Theorem 2; it does not serve, by P5.

**1.3 Ramos–Sousa.** J. P. G. Ramos, M. Sousa, *Fourier uniqueness pairs of powers of integers*, J. Eur.
Math. Soc. 24 (2022); arXiv:1910.04276. Uniqueness for nodes ±n^α, ±n^β in a range of exponents, by
perturbation of the Radchenko–Viazovska formula (CITED from the abstract; without number). Same diagnosis
as 1.2; superseded by 1.2.

**1.4 Crystalline rigidity.** N. Lev, A. Olevskii, *Quasicrystals and Poisson's summation formula*, Invent.
Math. 200 (2015): a measure on ℝ with uniformly discrete support and spectrum is a finite combination of
Dirac combs of lattices (CITED; without number). P. Kurasov, P. Sarnak, *Stable polynomials and
crystalline measures*, J. Math. Phys. 61 (2020); A. Olevskii, A. Ulanovskii, *Fourier quasicrystals with
unit masses*, C. R. Math. 358 (2020): positive integer masses ⟺ zero set of an exponential polynomial
with real roots.
- It is the only statement in the perimeter that *deduces* the equal spacing from a two-sided
  discreteness hypothesis (feature (b)). Mechanism: rigidity (Helson–Cohen/idempotents), not sign.
- Already cross-checked (IDX L30, L60, L101): the pair of the form has an absolutely continuous density on the
  archimedean side and a signed comb; the hypothesis does not hold. Class 25/20. Nothing new.

**1.5 Hedenmalm–Montes-Rodríguez; hyperbolic Fourier series.** H. Hedenmalm, A. Montes-Rodríguez,
*Heisenberg uniqueness pairs and the Klein–Gordon equation*, Ann. of Math. 173 (2011) 1507–1527;
arXiv:0910.1246. Main statement (CITED; without number): for the hyperbola x₁x₂ = 1 and the lattice
cross (αℤ×{0}) ∪ ({0}×βℤ), there is uniqueness if and only if αβ ≤ 1; equivalently, the system
{e^{iπαnt}, e^{iπβn/t}}_{n∈ℤ} is weak-∗ dense in L^∞(ℝ) exactly when αβ ≤ 1. F. Canto-Martín,
H. Hedenmalm, A. Montes-Rodríguez, *Perron–Frobenius operators and the Klein–Gordon equation*, J. Eur.
Math. Soc. 16 (2014). A. Bakan, H. Hedenmalm, A. Montes-Rodríguez, D. Radchenko, M. Viazovska,
*Hyperbolic Fourier series*, arXiv:2110.00148 (CITED from the abstract): explicit biorthogonal system in L¹(ℝ)
for {1, e^{iπnx}, e^{iπn/x}}, complete, and expansion convergent in tempered distributions; the
uniqueness part is equivalent to that of Radchenko–Viazovska at critical density.
- Mechanism: transfer (Perron–Frobenius) operator of a Gauss-type map x ↦ −1/x mod 2
  on [−1,1], with infinite invariant measure; uniqueness in the critical case αβ = 1 comes from the fact that the
  iterates of the (positive) transfer operator tend to zero. It is cone positivity under an operator
  that **is not a convolution** (composition with an expanding map).
- Additive/multiplicative: integer translations and inversion t ↦ −1/t (theta group); the inversion is the
  «Fourier transform + scale inversion» in another presentation. No primes, no weight.
- Exact threshold in one parameter: changing the spacing (α or β) breaks the statement at the critical value.
  It is the only exact dichotomy of the perimeter whose critical point is the integer lattice. But the parameter
  is the node spacing, not the weight: (i) and (ii) do not apply; (iii) breaks (ℤ is needed).
- Class: close to 14 (Markov/positive operator), but the operation is a transfer operator of an
  expanding map, not a folded convolution semigroup; ARGUED: it is not covered by the reason for
  failure of 14 (reflected branch |t−u|) nor by P12. The corpus has transfer operators only in the
  Mayer/Dolgopyat form (IDX G3H-152, estimates) — another use.

---

## 2. Magic functions, linear programming bounds, sign uncertainty

**2.1 How an exact sign is certified there.** M. Viazovska, *The sphere packing problem in dimension 8*,
Ann. of Math. 185 (2017); H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, M. Viazovska, *Universal
optimality of the E₈ and Leech lattices and interpolation formulas*, Ann. of Math. 196 (2022), Theorem 1.7
(interpolation with f, f′, f̂, f̂′ at √(2n); CITED, number according to the published introduction). The sign of the
magic function is obtained by writing it as sin²(πr²/2) times a Laplace transform of a modular
kernel of definite sign on the imaginary axis; the sign of the kernel was originally proved with interval
arithmetic on Fourier coefficients.
- Mechanism: (forced double zeros at the lattice lengths) × (Laplace transform of a
  function of constant sign). It is a dual certificate: a linear functional on the autocorrelation.
- Corpus: thm:O (fronts L, N), NO-GO. Class 1/20. Not repeated.

**2.2 Algebraic proof of the modular inequalities.** S. Lee, *Algebraic proof of modular form
inequalities for optimal sphere packings*, arXiv:2406.14659. Definitions (§3): a quasimodular form F
is *positive* if F(it) ≥ 0 for t > 0, and *completely positive* if all its Fourier coefficients are
≥ 0. Proposition 3.4: completely positive ⟺ all derivatives are positive (Bernstein).
Proposition 3.5 (CITED): if (∂_kF)(it) ≥ 0 on 0 < t < t₀ and F(it₀) > 0, then F(it) > 0 on (0,t₀]; the
proof is that F/Δ^{k/12} is monotone on the imaginary axis. Corollary 3.6: if the Serre derivative ∂_kF is
positive and F(it) > 0 for large t, F is positive. Proposition 3.8: conditions under which ∂_k preserves
complete positivity. With this the inequalities of dimensions 8 and
24 are proved without numerical computation. Same author, *Positive quasimodular forms and the sign uncertainty principle*, arXiv:2608.15415:
A₊(d) ≤ √(2⌊d/16⌋+2) for 4 | d (CITED from the abstract).
- Mechanism: comparison of a first-order ODE along the imaginary axis (the Serre derivative is
  the covariant logarithmic derivative with respect to Δ^{k/12}), with base case given by *signed integrality*
  of the q-coefficients. Functional equation (modularity) and integrality enter in the same step: the
  differential ring of quasimodular forms is closed under differentiation (Ramanujan identities).
- It does not see the Euler product nor primes. Falsifiers: there is no weight; they do not apply.
- Class 16 (monotonicity under a flow), with one difference: the flow is in the modular variable and the base case
  is arithmetic. No mark in the corpus («quasimodular», «Serre derivative»: 0 files).
- ARGUED: it gives a pointwise sign of a function on the axis, not positive semidefiniteness of a kernel; the corpus already
  records that the pointwise sign of the screw function is at most a necessary condition (IDX L72) and that
  Bochner in θ is excluded (rule C-hom, `RULES_AVOID.md` §G2).

**2.3 Sign uncertainty.** J. Bourgain, L. Clozel, J.-P. Kahane, *Principe d'Heisenberg et fonctions
positives*, Ann. Inst. Fourier 60 (2010); H. Cohn, F. Gonçalves, *An optimal uncertainty principle in
twelve dimensions via modular forms*, Invent. Math. 217 (2019) (optimal constant √2 in dimension 12, with
a −1 eigenfunction of the Fourier transform built by the Viazovska transform); F. Gonçalves,
D. Oliveira e Silva, J. P. G. Ramos, *On regularity and mass concentration phenomena for the sign
uncertainty principle*, J. Geom. Anal. 31 (2021), arXiv:2003.10765 (minimizers can be taken in the
Schwartz class in d = 1; infinitely many zeros after the last sign change); by the same authors,
*New sign uncertainty principles*, arXiv:2003.10771.
- Mechanism: Poisson summation applied to a ±1 eigenfunction; the sign is certified by a signed linear
  functional (linear programming duality). For the +1 side in d = 1 the constant is not known.
- Scale covariant, no weight, no primes. Class 1/20 (dual class = the target itself, C3). Nothing to
  transfer.

---

## 3. Prolate operators, Sonin spaces, semilocal formulas (after 2020)

Everything located is in IDX (L06–L09, L39–L41, L68, L106, L109). No work by these
authors later than those listed there was found. It is specified what is proved about the small eigenvalues and by what
mechanism, because that is the point where feature (a) appears in the literature.

**3.1** A. Connes, C. Consani, *Weil positivity and trace formula, the archimedean place*, Selecta Math. 27
(2021); arXiv:2006.13771. The archimedean part of the form on a window is identified with a trace
of the scaling action compressed to the Sonin space, and from there positivity is obtained in small
windows, reducing the rest to a finite-codimension constraint (CITED from the abstract and introduction).
Mechanism: compression of a unitary (transform + restriction). Only the archimedean place.

**3.2** A. Connes, C. Consani, *Spectral triples and ζ-cycles*, Enseign. Math. 69 (2023);
arXiv:2106.01715. Proved (CITED from the abstract): the form restricted to support in a fixed interval has
very small eigenvalues, and the corresponding vectors are obtained by applying the arithmetic sum
E(f)(x) = x^{1/2}Σ_n f(nx) to prolate functions at the scale of the window; the radical of the form is the
image of E. It is an **upper bound** on the bottom of the spectrum (existence of near-null directions).
- Reading (ARGUED): E is exactly a «transform that uses the equal spacing» and the restriction is the
  window; the mechanism produces the superexponential smallness, not the sign. No lower bound comes out of
  it. It coincides with the Sonin chain of the corpus (phase 183: PROVED, without sign; wall W-Sonin).

**3.3** A. Connes, C. Consani, H. Moscovici, *Zeta zeros and prolate wave operators*, arXiv:2310.18423; and
*Zeta spectral triples*, arXiv:2511.22755. From the second (CITED): Theorem 3.6, the operator of the form in
the window has discrete spectrum bounded below; Corollary 3.7, there exists an eigenvector of the bottom
μ_λ; the text declares that μ_λ ≥ 0 cannot be asserted. Theorems 1.1 and 5.10: under the hypothesis that the
minimal eigenvalue of the finite-dimensional truncation is simple and its eigenvector even (hypothesis, not
theorem), a perturbed operator is self-adjoint for the inner product T = Q − ε_N ≥ 0 and a
determinant identity holds. The approximation of the minimal eigenvector by prolate functions is observed and
supported by cited estimates (Lemma 7.2); the step that would justify it is declared open.
- Mechanism of the only sign that appears: T ≥ 0 by construction (the minimal eigenvalue is subtracted). It is not a
  sign of the form.

**3.4** A. Connes, W. van Suijlekom, *Quadratic forms, real zeros and echoes of the spectral action*,
arXiv:2511.23257 (IDX L09). Mechanism: real-rootedness property of the ground state of the truncated
form, of Hermite–Biehler type on a vector, not a sign of the form (classes 7 and 9 of the corpus, B9).

Summary of §3 (ARGUED): the prolate literature proves (1) discreteness and lower boundedness, (2) superexponential upper
bounds on the bottom via E∘prolates, (3) structure conditional on simplicity and
parity. Positivity in the window is obtained from none of the three. Classes 10 and 20.

---

## 4. de Branges spaces, Hermite–Biehler, canonical systems with arithmetic input

All covered in IDX. Unconditional positivity statements in windows and their mechanism:

| Source | Unconditional statement | Mechanism |
|---|---|---|
| H. Yoshida, *On Hermitian forms attached to zeta functions*, Adv. Stud. Pure Math. 21 (1992) (IDX L03) | positivity for small support (number not verified) | for support below log 2 the comb does not enter; the archimedean part remains, treated by comparison and computation |
| E. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers, I*, Rend. Mat. Acc. Lincei (9) 11 (2000) (IDX L01–L02; the corpus uses Thm 3, 5, 12) | minimum attained, continuity, cost of the primes | compactness and calculus of variations; the sign does not come out of the method |
| J.-F. Burnol, *The explicit formula and the conductor operator*, arXiv:math/9902080; *Sur les formules explicites I*, C. R. Acad. Sci. 331 (2000) | each local term is −(log|x|_v + log|y|_v) conjugated by Fourier; lower boundedness per place | local positivity per place (class 2; P8) |
| J.-F. Burnol, *Two complete and minimal systems associated with the zeros of the Riemann zeta function*, J. Théor. Nombres Bordeaux 16 (2004), arXiv:math/0203120; *Entrelacement de co-Poisson*, Ann. Inst. Fourier 57 (2007) | completeness and minimality of systems in Sonin spaces; co-Poisson formula | unitarity of «Fourier + inversion» and support conditions (class 10/20); no sign of the form |
| M. Suzuki, series on canonical systems and the screw function (IDX L12, L36, L38) | existence of the Hamiltonian and localized positivity for small windows; continuity of the minimal eigenvalue in the window size | invertibility of I ± K in a small window (perturbation of the identity; class 3/21) |
| J. C. Lagarias, spaces of entire functions (IDX L17) | reformulation | — |

ARGUED: the unconditional results in windows come from one of three mechanisms: (a) the comb does not enter
in the support range; (b) the comb is a perturbation dominated by the archimedean coercivity
(P2 excludes it for T ≳ 0.60); (c) numerical certificate per window (W-fam). None is of
concentration type with arithmetic input. Nothing unused.

---

## 5. Mechanisms from other fields

**5.1 Inversion positivity for non-local kernels.** R. L. Frank, E. H. Lieb, *Inversion positivity
and the sharp Hardy–Littlewood–Sobolev inequality*, Calc. Var. PDE 39 (2010): for the kernel |x−y|^{−λ}
there is reflection positivity with respect to inversions in spheres, ∬ f(x) f(Θy)… ≥ 0 for f supported on one
side (CITED; without number). K.-H. Neeb, G. Ólafsson, *Reflection positive one-parameter groups and
dilations*, Complex Anal. Oper. Theory 9 (2015), arXiv:1312.6161; *Reflection Positivity*, Springer
Briefs (2018), ch. 4: classification of reflection-positive one-parameter unitary groups and their
relation with outgoing Lax–Phillips spaces.
- Elementary observation (ARGUED): with x = e^t, y = e^s one has √(xy)/|x−y| = 1/(2sinh(|t−s|/2)) and
  √(xy)/(x+y) = 1/(2cosh((t−s)/2)); that is, K is the kernel |x−y|^{−1} + |x+y|^{−1} on the half-line in
  Haar measure, and the inversion x ↦ 1/x is t ↦ −t. The sinh part is completely monotone in u; the
  cosh part is an alternating series of exponentials and is not.
- Mechanism: ⟨ΘF,F⟩ ≥ 0 for F supported in t > 0. For F supported in [−T,T] it only controls the cross
  term between the two halves, and only of the sinh part. No weight, no primes; the three falsifiers do not
  apply. Class 17; the cross-check of `ROUND_009_G3.md` §3 (reflection at 0 = ⟨JF,F⟩, falls into R3-a) and rule
  R-K1 already cover it. Frank–Lieb appears in a single file of the corpus; the mechanism is not new.

**5.2 Toeplitz / Wiener–Hopf on the multiplicative semigroup.**
- H. Hedenmalm, P. Lindqvist, K. Seip, *A Hilbert space of Dirichlet series and systems of dilated
  functions in L²(0,1)*, Duke Math. J. 86 (1997): {φ(nx)} is a Riesz basis of L²(0,1) if and only if the
  Dirichlet series of the coefficients of φ and its inverse are multipliers of ℋ² (CITED; without number).
  The dilations D_n are isometries representing (ℕ,·) on odd 2-periodic functions: it is the
  only classical object where the equal spacing (orthonormality of sin πnx) and multiplication act at
  the same time. Cited in phase 159.
- H. Helson, *Hankel forms and sums of random variables*, Studia Math. 176 (2006): (Σ|a_n|²/d(n))^{1/2} ≤
  ‖f‖_{ℋ¹}. Mechanism: prime-by-prime iteration of a one-variable inequality. Free monoid only:
  it holds in any Beurling system (B7).
- O. F. Brevig, K.-M. Perfekt, K. Seip, A. Siskakis, D. Vukotić, *The multiplicative Hilbert matrix*, Adv.
  Math. 302 (2016), arXiv:1411.7294: norm π; multiplicative Hankel form. Upper bound (B10).
- J.-F. Olsen, *Local properties of Hilbert spaces of Dirichlet series*, J. Funct. Anal. 261 (2011),
  arXiv:1011.3370. Theorem 1 (CITED): Σ_{n≤x} w_n ≲ x/(log x)^α ⟺ the weighted space ℋ_w embeds
  locally (on each bounded interval of the line Re s = ½) into D_α of the half-plane. Theorems 2 and 4: under
  the corresponding lower bound, every f in D_α coincides in the window with an F ∈ ℋ_w up to a term
  that continues analytically. Theorem 3: same compactly supported Carleson measures and same bounded
  interpolating sequences. Example 3: w_n = Λ(n)/log n. Antecedents: J.-F. Olsen, K. Seip, *Local
  interpolation in Hilbert spaces of Dirichlet series*, Proc. AMS 136 (2008); J.-F. Olsen, E. Saksman,
  J. reine angew. Math. 663 (2012).
  - It is a **window** statement at the critical weight with prime input. Mechanism: sampling density
    of the measure Σ w_n δ_{log n}/n (Beurling–Jaffard–Seip, Ortega-Cerdà–Seip). Equivalences
    up to constants: class 21. It depends only on Chebyshev bounds of the weight: preserved with weight ×2, with
    a deletion and in Beurling systems with the same density. It carries no sign.
- Nyman–Beurling–Báez-Duarte: the Gram matrix of the dilated fractional parts has a closed form
  (Vasyunin) and the cotangent sum c₀(h/k) satisfies a reciprocity formula (S. Bettin, J. B. Conrey,
  *Period functions and cotangent sums*, Algebra Number Theory 7 (2013)). It is an exact identity that sees
  h/k additively and multiplicatively, on a manifestly positive semidefinite matrix free of Λ.
  ARGUED: it is not a form on a support window, and Λ enters only through the coefficients of the approximant;
  it factors through a fixed Λ-free object (P9). The corpus records it as unused (G2_B10_R1) and closes the
  family as a reformulation (T3).
- M. Laca, I. Raeburn, *Phase transition on the Toeplitz algebra of the affine semigroup over the natural
  numbers*, Adv. Math. 225 (2010), arXiv:0907.3760. Theorem 4.1 (CITED): 𝒯(ℕ ⋊ ℕ^×) is universal for an
  isometry s and isometries v_p with (T1) v_p s = s^p v_p, (T2) v_p v_q = v_q v_p, (T3) v_p^* v_q = v_q v_p^*,
  (T4) s^* v_p = s^{p−1} v_p s^*, (T5) v_p^* s^k v_p = 0 for 1 ≤ k < p. Proposition 6.1: in the boundary
  quotient (Cuntz algebra 𝒬_ℕ) Σ_{k<p} (s^k v_p)(s^k v_p)^* = 1 holds.
  - (T5) and the inequality 1 − Σ_{k<p} s^k v_p v_p^* s^{*k} ≥ 0 are the operator form of «the residue
    classes mod p are orthogonal and fill ℤ»: an exact positivity that only holds for the true
    integers and uses sum and product in one same relation. It breaks in Beurling (there is no s). It has no
    weight: insensitive to (i) and (ii).
  - Cited in phase 159 (presentation). ARGUED: what I did not find used is (T5) as a complementary
    projection within the compression to the window. It is a fixed Λ-free object (P9) and the window is
    not invariant under v_p; class 9/10 without a new operation. I do not propose it.

**5.3 Fejér–Riesz in several variables and sums of squares.** M. A. Dritschel, *On factorization of
trigonometric polynomials*, Integral Equations Operator Theory 49 (2004): a strictly positive operator-valued
trigonometric polynomial in several variables is a finite sum of hermitian squares of
analytic polynomials (CITED; without number; without degree bound). M. A. Dritschel, *Factoring non-negative
operator valued trigonometric polynomials in two variables*, arXiv:1811.06005: in two variables
non-negativity suffices, with control of number and degrees, via Schur complements. J. Geronimo, H. Woerdeman,
*Positive extensions, Fejér–Riesz factorization and autoregressive filters in two variables*, Ann. of
Math. 160 (2004): necessary and sufficient condition, in terms of the Fourier coefficients, for
stable spectral factorization in two variables.
- By the Bohr lift, a Dirichlet polynomial in the primes ≤ P is a trigonometric polynomial
  in π(P) variables. Mechanism: existence of SOS given positivity; the certificate exists if and only if
  the target holds, and without a degree bound with margin e^{−cT}. Classes 1 and 4 (B3, J3). Moreover the form in the
  window is a compression, not a Toeplitz operator on the torus. New names, mechanism already closed
  (front E).

**5.4 Borodin–Okounkov identity on a finite interval.** E. Basor, Y. Chen, *A note on Wiener–Hopf
determinants and the Borodin–Okounkov identity*, Integral Equations Operator Theory 45 (2003),
arXiv:math/0202062 (CITED): det(I − K_{[0,α]}) = Z e^{cα} det(I − L_{[α,∞)}), with Z and c given by the
Wiener–Hopf factorization of the symbol and L an operator on the complementary half-line with small
kernel. Wiener–Hopf + Hankel variants: Basor–Ehrhardt, arXiv:math/0304002.
- It is exactly of concentration type and exact: the determinant on the window is a constant times a
  Fredholm determinant of the complementary restriction of a product of Hankel operators, which is
  superexponentially close to 1. Dimension growing with α.
- Mechanism: Jacobi identity for complementary minors of A and A^{−1}. It holds for every symbol with a
  factorization (generic identity: B1, class 20); it requires a symbol without zeros and index zero, and the symbol of
  the form changes sign; and it controls a determinant, not the minimal eigenvalue (wall W-det). In the corpus
  it only appears in phase 67, on another object.
- ARGUED: the inertia version (Haynsworth Schur complement between PAP and QA^{−1}Q) is class 4/6.

**5.5 Integral operators reflecting a differential operator.** W. R. Casper, F. A. Grünbaum,
M. Yakimov, I. Zurrián, *Reflective prolate-spheroidal operators and the KP/KdV equations*, Proc. Natl.
Acad. Sci. 116 (2019), arXiv:1909.01448; *Reflective prolate-spheroidal operators and the adelic
Grassmannian*, Comm. Pure Appl. Math. 76 (2023), arXiv:2003.11616. Definition (CITED): T reflects R if
T∘R(−z,−∂_z) = R(z,∂_z)∘T on a dense subspace. Theorem 1: every point of Wilson's adelic Grassmannian
gives an integral operator reflecting a nonconstant differential operator of order ≤ 2min(d₁,d₂).
Theorem 3: under a symmetry, the time- and band-limited Fourier-type operator commutes with a
differential operator with rational coefficients of the same order. Theorem 4: operator common to a finite
family. The examples have order 1, 3 and 6.
- Mechanism: Fourier algebra of a bispectral function; algebraic source of the prolate commutation.
  It is not a sign mechanism: it gives eigenvectors and Sturm structure for concentration operators.
- Cross-check: CS0_COMMUTE_001 proved that there is no differential commutant of order ≤ 2 for the operator of the
  window with comb, and left order > 2 OPEN. The notion of *reflection* (weaker than commutation) and the
  high orders are precisely that residue. ARGUED: the per-atom periodicity argument of CS-0
  (each δ_{log n} forces periodic coefficients) does not depend on the order and probably also excludes
  reflection; it is not written.
- No weight: the CS-0 obstruction holds for cΛ, a_P, Beurling (IDX), so even if it existed it would be
  generic in the comb. Class 13 (Sturm) / 10.

**5.6 Determinantal processes; optimal transport and entropy with integer structure.** No
statement was found with kernel «restriction of an arithmetic unitary» other than the already recorded concentration one
(0 ≤ PQP ≤ 1, class 10), nor transport or entropy identities using the spacing of the integers
beyond what was cross-checked in IDX P33-11 and `ROUND_009_G3.md` §3. Shallow search at this point; it does not
count as an exclusion.

---

## 6. Short list

Mechanisms without substantive mark in the corpus, ordered by number of features they gather. **None
gathers all five and none passes the four-point gate**: all lack the same thing, a sign that
depends on the exact values of v_n (none breaks with weight ×2 for a sign reason).

1. **Transfer operator of a Gauss-type map at critical density** (§1.5; Hedenmalm–
   Montes-Rodríguez; Canto-Martín–Hedenmalm–Montes-Rodríguez; hyperbolic Fourier series).
   Gathers: exactness (threshold αβ = 1), equal spacing + scale inversion, non-locality, infinite
   dimension; the positive operation is not a convolution (it sidesteps P12 to the letter).
   First statement to transfer: the lemma that the iterates of the Perron–Frobenius operator of
   x ↦ −1/x mod 2 annihilate in the limit every function annihilating the system {e^{iπnt}, e^{iπn/t}};
   its analogue would be a transfer operator on the window intertwining the compression of the
   operator Σ v_n τ_{log n} with an expanding map on the multiplicative side.
   Why it may fail: it is a uniqueness theorem, not a sign theorem for a form, and at critical density it gives no
   frame bound; it has no weight (insensitive to c = 2 and to deletion); the natural expanding map on the
   multiplicative side leads to a jump semigroup, which is class 24 (no reversible density).

2. **Serre derivative criterion with an integrality base case** (§2.2; Lee, Prop. 3.5, Cor. 3.6).
   Gathers: exactness, functional equation and integrality in one same step, without slack.
   First statement to transfer: on the theta realization of the function of a profile, find a weight k
   for which the Serre derivative is completely positive and apply Cor. 3.6.
   Why it may fail: it gives a pointwise sign on an axis, not semidefiniteness of a kernel (Bochner in θ excluded,
   C-hom); it does not see the Euler product (holds for models without it, B6); the object of the phase is not a
   quasimodular form of fixed level.

3. **Reflection, not commutation, of a differential operator of order > 2** (§5.5; Casper–Grünbaum–Yakimov–
   Zurrián, Theorems 1, 3, 4). Gathers: concentration type, exactness, growing dimension.
   First statement to transfer: extend the CS-0 lemma to the identity T∘R(−z,−∂_z) = R(z,∂_z)∘T with R of
   arbitrary order; the expected result is negative and would close with proof the OPEN residue of
   CS0_COMMUTE_001.
   Why it may fail as a sign source: even if R existed, it would give eigenvector structure, not
   sign, and it would be generic in the comb. Its value is one of closure, not construction.

4. **Borodin–Okounkov identity on a finite interval** (§5.4; Basor–Chen). Gathers: concentration type,
   exactness, growing dimension, superexponential smallness of the complementary factor.
   First statement to transfer: the identity for the regularized symbol of the form (adding a
   constant that makes it positive), and follow the complementary factor as the regularization is removed.
   Why it may fail: it is valid for every factorizable symbol (carries no sign, B1); it requires a symbol without
   zeros; it gives a determinant (W-det), not the minimal eigenvalue; removing the regularization is the target.

5. **Olsen's local theory for ℋ_w on a window of the critical line** (§5.2; Theorems 1–4). Gathers: it is a
   window statement, critical weight, prime input, non-local per prime.
   First statement to transfer: Theorem 2 with w_n = Λ(n)/log n as an exact description of the space of
   boundary values on the window, to write the arithmetic term as a norm in a local Hardy
   space.
   Why it may fail: equivalences up to constants (P5); depends only on Chebyshev bounds of the weight
   (generic: survives c = 2, deletion and Beurling with the same density).

Put plainly: **nothing found matches the specification.** Feature (b) —
isometry only for the true integers with Σ_{d|n}Λ(d) = log n inside the sign step — does not appear
in any positivity statement of the literature consulted. Where the equal spacing appears (§1.4,
§1.5, §5.2 Laca–Raeburn, Hedenmalm–Lindqvist–Seip) there is no weight; where the weight appears (§5.2 Olsen, Helson)
there is neither exactness nor additive structure. The two objects that join sum and product in a single exact
relation are the Laca–Raeburn relation (T5) and the Vasyunin–Bettin–Conrey reciprocity; both are free
of Λ and are already cited in the corpus.

## 7. Claims

| # | Claim | Label |
|---|---|---|
| 1 | Statements and theorem numbers of §§1–5 | CITED (arXiv version; those marked «without number» unverified in the primary source) |
| 2 | Cross-check table §0 | NUMERICAL (grep; does not prove novelty) |
| 3 | K(u) = √(xy)(|x−y|^{−1} + (x+y)^{−1}) with x = e^t, y = e^s | PROVED (elementary identity) |
| 4 | Classification of each item in classes 1–25 and behaviour under the three falsifiers | ARGUED |
| 5 | The E∘prolates mechanism gives upper bounds on the bottom and not lower bounds | ARGUED (on CITED statements) |
| 6 | The CS-0 periodicity argument extends to reflection and to every order | OPEN (ARGUED to be likely) |
| 7 | No mechanism found has a sign depending on the exact values of the weight | ARGUED |
| 8 | Global sign | OPEN |
