# FAMILIES_B_001 — Inventory B of phase 201: analysis, probability, logic, mathematical physics, computation, information, dynamics, geometry

Mandate: README of phase 201. Inputs read: MAP_200_001 §1, §2, §4 (v12 and SPEC-𝔇 S1–S6), §6;
HORN_B_BIGSHARP_001 §3; SPEC_SIGN_OBJECT_006 §B (Φ200, branches 1–5); survey/SYNTHESIS.md; index
`05-meta-and-planning/ROUTES-TRIED-INDEX/` (grep by family, including 05/05b of literature and SURVEY_MODERN_UNTRIED).
ARGUED. This document is an inventory. It proves nothing new and launches no constructions.

## Summary (≤300 words)

32 method families with a genuine positivity theorem (sign from structure) were reviewed. Each one was grepped
against the index (≈1,700 routes), grepped against the corpus (03-research, 04-papers, 00-references) and, when the
grep gave 0, searched in the literature. Result: **23 NON-VIRGIN**, **6 VIRGIN-DEAD** and **3 VIRGIN-VIABLE**.

Almost everything "physical" has already been used:
- Osterwalder–Schrader: per place (NG-E1), at the boundary (K1) and on the lattice (CA_J_001).
- FKG, GKS, Lee–Yang, strong Rayleigh and Brascamp–Lieb: J front, frustration Thm 1.3.
- Log-Sobolev, Γ₂, relative entropy, Wasserstein and Talagrand.
- Random matrices, determinantal processes and RKHS.
- o-minimality, Ax–Schanuel, Loeb, Szegő, Helson and rearrangements.
- Beurling–Malliavin (GAP-157.A), Gelfand–Levitan–Kreĭn (R186) and Perron–Frobenius/Kreĭn–Rutman.

The virgin-dead ones are the Shannon–Stam EPI and Fisher monotonicity (ABBN), information geometry, frame-operator
positivity, large deviations, Fuglede spectral sets and the Gaussian correlation inequality (which is also only
half-virgin). All are continuous functionals on the comb or linear in the data, and fall into branches 1–2 of Φ200
via C-τ and restriction 1.

The three viable virgins share a new feature: they are **semialgebraic integer invariants that are not
Vandermonde-generic**. That is how they evade Thm 3′ / O7, which killed the analytic rank counts.
- **V1. Non-negative rank and extension complexity (Yannakakis).** It is a discontinuous integer (S2, S5) with a
  factorization ↔ extension duality that is not Poisson (S3).
- **V2. Additive-multiplicative recurrence (Moreira, Bergelson–Moreira).** It is a measure positivity for patterns
  {x+y, xy}. It reads (ℕ,+,·) literally, which is the semiring principle, and does not exist for Beurling.
- **V3. Forster sign rank.** It is a positivity bound via radial isotropic position on additive sign matrices of λ
  or μ.

None has a declared Λ_cosh channel (S6) beyond ARGUED-weak. That is the first point to attack. Ranking: V1 > V2 > V3,
with a first exact lemma for each in §4.

---

## 0. Filter conventions

For each family the following are given:
- (a) the key positivity theorem, CITED;
- (b) the index grep (hits and entry);
- (c) the corpus grep or the web search;
- (d) the instantiation on the window in one sentence;
- (e) the S1–S6 filter and the Φ200 branch (1 comb-generic, 2 REF-D/certificate, 3 h* functional, 4 blind to ζ, 5
  equality between data);
- (f) the Λ channel (O11) and the battery falsifier (Epstein 11, DH 12, a_P, cΛ, Beurling);
- (g) the verdict.

**Virginity rule.** NON-VIRGIN if there is an index entry covering the mechanism. VIRGIN-DEAD if there is no entry
but the S1–S6/Φ200 filter kills it with a restriction already PROVED or ARGUED from MAP_200 §2. This is **not** a
new NO-GO: it is the application of an existing one, and it is added to the index as such. VIRGIN-VIABLE if there
is no entry and no listed restriction kills it.

**Cross-cutting criterion used (from MAP_200).** A family whose functional is continuous in the topology in which
the comb Σv_nδ_{log n} varies falls into branch 1 via C-τ and restriction 1 (TV), and that holds regardless of its
internal positivity. A family whose sign is read on the form 𝔞_T or its kernel falls into branch 2 (S1, REF-D). A
family that sees only (ℚ, ℚ^×) dies by C-MvN. A "rank" family with analytic dependence on the test dies by Thm 3′
(O7).

---

## 1. Mathematical physics and statistical mechanics

**F1. Osterwalder–Schrader reflection positivity (continuum, lattice and transfer matrix).**
- (a) OS/Glimm–Jaffe theorem (CITED): RP ⟹ Hamiltonian ≥ 0 via reconstruction. On the lattice, RP ⟺ the transfer
  matrix T is ≥ 0 (Fröhlich–Israel–Lieb–Simon 1978, CITED).
- (b) Index: NG-E1 "OS reflection positivity per place," FALSIFIED (G_p(π/log p) < 0, phase 6). NG-E5
  "Hilbert–Pólya via OS reconstruction," FALSIFIED. K1 OS-Γ (K1_OSG_001), NO-GO PROVED: reflection at the boundary
  x = T of the exterior datum with CM kernel of poles of Γ_ℝ has NN′ structure (R-K1). CA_J_001: "lattice RP ⟺
  lattice support," PROVED.
- What remains outside: the "arithmetic transfer matrix" with T indexed by ℕ and coupling m→kn. CA_J_001 covers it
  because any lattice RP is lattice support. CA_J_002 (frustration) covers it if the coupling mixes + and ·: the
  cycle m → m+1 → … → 2m closed by the edge (m, 2m) is frustrated.
- (e) Branch 2 (boundary RP = Hankel = R-K1) or branch 1.
- (g) **NON-VIRGIN.** New reason needed: an RP without lattice support and without a frustrated cycle. I do not
  have one.

**F2. Correlation inequalities (FKG, GKS/Griffiths, Ginibre, GHS, Lebowitz, Fortuin–Kasteleyn), Ising model on the
primes.**
- (a) GKS: ⟨σ_Aσ_B⟩ ≥ ⟨σ_A⟩⟨σ_B⟩ with ferromagnetic interactions (CITED).
- (b) Index: "Lee–Yang, strong Rayleigh, GKS/FKG, Brascamp–Lieb | L32; J front | dead (frustration Thm 1.3)."
  J3/J7/J9/K9 "presuppose ferromagnetic/RP ⇒ die with J1/J6." Knauf/Contucci–Knauf (spin chain with
  Z(β) = ζ(β−1)/ζ(β), ferromagnetic coefficients): OPEN-unpromising, only β > 2 real.
- (d) An Ising model "on the primes" whose correlations are the comb requires couplings J ≥ 0 on a graph that
  contains both additive and multiplicative edges: frustrated by Thm 1.3.
- (g) **NON-VIRGIN.**

**F3. Lee–Yang theory, Pólya–Lee–Yang, Newman.**
- (a) Lee–Yang circle theorem (1952). Newman (1976): Lee–Yang measures give transforms with real zeros. It is zero
  localization by positivity (CITED).
- (b) Index: "HEAT = heat flow / de Bruijn–Newman / Lee–Yang," NG-B5 (de Bruijn–Newman, only gives an upper bound).
  J front. Lee–Yang appears in 76 corpus files, including BARRIER_EST_001 (phase 197).
- (c) Literature: Newman and Rodgers–Tao (Λ_dBN ≥ 0).
- The "inverse direction" the mandate proposes (positivity of an operator ⟹ zeros on the circle) is exactly
  Newman's program. It requires a Lee–Yang-type spin measure whose transform is Ξ. The existence of that measure is
  REF-D (branch 2).
- (g) **NON-VIRGIN.**

**F4. Strong Rayleigh, stable polynomials, Gurvits capacity and van der Waerden.**
- (a) Borcea–Brändén–Liggett 2009; Gurvits: perm ≥ cap·n!/nⁿ (CITED).
- (b) Index: "strong Rayleigh" (J front); Lorentzian polynomials G6 (retry, no sign).
- (g) **NON-VIRGIN.**

**F5. Random matrices (GUE, Tracy–Widom, ensembles) and determinantal point processes (DPP).**
- (a) Macchi–Soshnikov: a Hermitian kernel 0 ≤ K ≤ I defines a DPP (CITED).
- (b) Index: GUE in 196 lines; "Determinantal / random combs, GMC | G8D-R160_S5; L77 | DEAD." "Tracy" has 0 hits in
  the index and 2 in the corpus (phase 60).
- (d) A DPP over log ℕ with the Weil kernel requires 0 ≤ K ≤ I, and that is the sought positivity (branch 2). A
  DPP with a given kernel (sinc) is blind to ζ (branch 4).
- (g) **NON-VIRGIN.**

**F6. Integrable systems (Toda, KdV, Painlevé) and Fredholm determinants.**
- (a) τ-function positivity: τ > 0 for reflectionless potentials (Kay–Moses), CITED.
- (b) Index: "Toda" only gives false positives of "todas" (Spanish "all"). KdV/Painlevé: 0 hits. W-det
  (Fredholm/Szegő–Widom) is NO-GO: every determinant that decides the sign factors as λ_A·R (R186_034 Thm 3.1).
- (c) Literature: Burnol, "Paley–Wiener spaces with vanishing conditions and Painlevé VI transcendents" (arXiv
  1008.0617), already in survey S2. The Painlevé ↔ Sonin/Paley–Wiener space link exists.
- (g) **NON-VIRGIN** (τ = determinant ⟹ W-det; Burnol literature).

**F7. Inverse spectral theory: Gelfand–Levitan, Marchenko, Kreĭn, inverse scattering.**
- (a) Gelfand–Levitan: the spectral measure determines the potential. The GL equation has a positive solution ⟺ the
  measure is positive (CITED). It is a potential ↔ spectral-data duality that is not Fourier, so it was a candidate
  for S3.
- (b) Index: "Inverse spectral / Hilbert–Pólya / Jacobi / Mercer (RH5, L44–L47): closed." R6-01, inverse Jacobi,
  DEAD. L89 Faddeev–Pavlov / Lax–Phillips, NO-GO ARGUED.
- (c) Corpus: R186_000/R186_045 (toolbox), "{W_T}_T resolved (Gelfand–Levitan–Kreĭn: H is obtained from the
  resolvents at the vertex)… Missing: TB-1, global existence for the non-linear Gelfand–Levitan equation with
  arithmetic data" (HEURISTIC, open). Web: N. N. Khuri (not Wu–Sprung; BIBLIO_CHECK_001), "Inverse scattering, the
  coupling constant spectrum and the Riemann hypothesis," Math. Phys. Anal. Geom. 5 (2002) (hep-th/0111067).
- (e) The input spectral datum is the form itself (branch 2). The comb as a Sturm–Liouville "potential" requires
  the spectral measure to be positive, which is the conclusion.
- (g) **NON-VIRGIN** (open residue TB-1 in R186; cited to avoid duplicating it).

**F8. Supersymmetry / Witten–Riccati factorization.**
- Index #96 "G1 SUSY (Witten/Riccati), factorization ⟺ positivity."
- (g) **NON-VIRGIN.**

**F9. Thermodynamic formalism (Ruelle, transfer operators, Kreĭn–Rutman).**
- (a) Ruelle–Perron–Frobenius and Kreĭn–Rutman: positive dominant eigenvalue with positive eigenvector (CITED).
- (b) Index: P60-1 (PF gives simplicity, not sign); CA_I_001 ("Krein–Rutman lives…"); Knauf; prime gas (survey
  §2.5: "Ruelle… are not pieces of the object"). Corpus: Doc 51, "Operator Φ… Krein–Rutman Theorem."
- (g) **NON-VIRGIN.**

## 2. Harmonic and functional analysis, PDE and variational methods

**F10. Hypercontractivity and log-Sobolev (Nelson, Gross, Bonami–Beckner).**
- (a) Bonami–Beckner: ‖T_ρf‖_q ≤ ‖f‖_p for ρ ≤ √((p−1)/(q−1)). Gross: LSI ⟺ hypercontractivity (CITED).
- (b) Index: "Do not retry Γ₂/CD/log-Sobolev/Poincaré of the jump part without an input coupling E_T and W_T" (I
  front, B2 Bakry–Émery). In the corpus, Bonami only appears as Bonami–Karoui (prolate bounds, K3), not as
  hypercontractivity.
- (d) The natural semigroup on the window is the Markov one of the I front, and there the sign is decided by W_T.
- (g) **NON-VIRGIN** by the explicit index rule.

**F11. Optimal transport, Talagrand, displacement convexity.**
- Index: P33-11 "Relative entropy / KL / Wasserstein / max-entropy," CIRCULAR. "Optimal transport (displacement
  convexity, LSV)… fold into B2." K2 Talagrand/Parisi.
- (g) **NON-VIRGIN.**

**F12. Brascamp–Lieb, Prékopa–Leindler, Hardy–Littlewood–Sobolev, Riesz and rearrangements.**
- Index: J4/J4′ (Brascamp–Lieb and BCCT: RD/CIRC); J5 Prékopa–Leindler (PF₅ fails); "concentration-compactness,
  rearrangements: dead. Every F ∈ P_T has ≥ 2 sign changes (PROVED)." HLS: 0 hits in the index, 1 in the corpus
  (R162_1701). Symmetrization requires a fixed-sign test, which P_T excludes.
- (g) **NON-VIRGIN** (HLS falls under "rearrangements" for the same reason: ≥ 2 sign changes).

**F13. Hardy spaces: inner-outer factorization, Szegő, Helson–Szegő, H²(𝔻^∞).**
- Index: W-det (Szegő/Widom, NO-GO); C_006 E4 Helson H²(𝔻^∞), RD + CIRC; G8D-R164_502c (Szegő–Widom, DEAD). Corpus:
  R161 (sum-product square phase) uses inner/outer.
- (g) **NON-VIRGIN.**

**F14. Beurling–Malliavin, densities and completeness of exponentials.**
- Index: GAP-157.A "non-local Tauberian with LI input (Beurling–Malliavin on p^{iτ})," OPEN-RESIDUE (condition C1
  neither known nor excluded). C-emb kills "completeness."
- (g) **NON-VIRGIN** (open residue already registered).

**F15. Riesz bases and frames.**
- (a) Positivity of the frame operator A ≤ S ≤ B (Duffin–Schaeffer, CITED).
- (b) Index: "Riesz bas" 0 hits. "frame" has 27 lines, mostly with a different meaning.
- (d) Frame {e^{iτ log n}} or {v_n c(·−log n)} on P_T: the frame lower bound A > 0 **is** a lower bound of a
  quadratic form linear in the data. If the form is the Weil form, REF-D (branch 2). If not, it is continuous on
  the comb (branch 1, C-τ).
- (f) Falsifier: a_P (same support, different weights).
- (g) **VIRGIN-DEAD (branches 1/2).**

**F16. Spectral sets / Fuglede / tilings.**
- (a) Ω is spectral if it admits an orthogonal basis of exponentials. It is a positivity of the Delsarte function
  (CITED, Kolountzakis–Matolcsi).
- (b) Index: 0 hits for "Fuglede" as a conjecture; the corpus uses the Fuglede commutation theorem. Delsarte (L8)
  is there: "K4 Grothendieck/SDP… L8 Delsarte… Schur reductions / dual certificate."
- (e) It is a Delsarte LP: branch 2 (certificate).
- (g) **VIRGIN-DEAD (branch 2).**

**F17. Gaussian correlation inequality (Royen 2014).**
- (a) μ(K∩L) ≥ μ(K)μ(L) for symmetric convex sets (CITED).
- (b) Index: 0 hits. Corpus: the "Gaussian correlation" of R160_M5 is a different object (a named prime measure).
- (c) Literature: Henderson, "Kernel-positivity of Laplace registers, Blagouchine–Royen measures, and the Weil/de
  Branges explicit-formula criterion" (Zenodo 19636675, listed in survey S3), so it is not virgin in the literature.
- (e) It is continuous on the comb (branch 1).
- (g) **VIRGIN-DEAD** (and only half-virgin because of Henderson).

**F18. Choquet theory / capacities / Riesz energies.**
- (a) Energy positivity ∬|x−y|^{−α}dμdμ ≥ 0 (CITED). It is Bochner for a positive-definite kernel.
- (b) Index: Choquet, 0 hits. Bochner appears in 21 lines (C-hom, RKHS DEAD).
- (g) **NON-VIRGIN** by mechanism (Bochner/RKHS).

## 3. Probability, information, dynamics, logic, computation, geometry

**F19. Entropy power inequality (Shannon–Stam) and entropy/Fisher monotonicity (Artstein–Ball–Barthe–Naor 2004).**
- (a) N(X+Y) ≥ N(X)+N(Y). ABBN: H(S_n/√n) is increasing (CITED). The positivity comes from the additive structure
  of independent sums, with the Fisher projection as a duality.
- (b) Index: Shannon, Stam and Fisher, 0 hits. "entrop" falls under P33-11 (relative entropy, CIRCULAR), which does
  not cover the EPI.
- (c) Web: I found no use of the EPI or of Fisher monotonicity for the explicit formula (search "entropy power
  inequality Riemann zeta explicit formula positivity": no relevant results).
- (d) X_p = a random variable with law tied to the local Euler factor (Biane–Pitman–Yor already gives infinitely
  divisible laws for ξ). The EPI would give superadditivity of N under the convolution Σ_p.
- (e) N is continuous in the law, and hence in the comb. S5 fails, branch 1 via C-τ. Also the per-prime Euler laws
  are those of 13.1 (convexity under Euler averages: undefined). An EPI is precisely a "convexity under sums."
- (f) Falsifier: Epstein 11 (it is an average of two Euler products plus Λ_cosh), C-E′.
- (g) **VIRGIN-DEAD (branch 1; C-E′ + Lemma 13.1).** Added to the index.

**F20. Information geometry (Fisher–Rao metric, Bregman divergences).**
- Bregman already appears in the index (nodal flux/Bregman, DEAD). Fisher–Rao is continuous.
- (g) **VIRGIN-DEAD (branch 1)**; by adjacency, nearly NON-VIRGIN.

**F21. Large deviations (Varadhan, Gärtner–Ellis): rate-function positivity.**
- (a) I ≥ 0 as the convex conjugate of Λ_cum (CITED).
- (b) Index: 0 hits.
- (d) I(x) for Σ_{n≤N} v_n c(log n) under a random prime model. That is a Cramér model, blind to ζ (branch 4). With
  the deterministic comb, the convex conjugate is linear-dual (branch 2).
- (g) **VIRGIN-DEAD (branches 4/2).**

**F22. Martingales, Doob, Feynman–Kac.**
- Index: "Feynman–Kac/Doob = CA_I/R160_M10 (not retried)"; K11 Doob, retry.
- (g) **NON-VIRGIN.**

**F23. Dynamics: ×2,×3 rigidity, Furstenberg recurrence, solenoid.**
- Index/corpus: SPEC #15 "×2,×3 rigidity / solenoid… H front: Near = Kronecker − Haar (PROVED)," and G1 states
  Beurling reproduces the solenoid. The purely multiplicative kernel dies by C-MvN.
- (g) **NON-VIRGIN** for ×2,×3 and multiplicative recurrence. For the **additive-multiplicative** version see V2 in
  §4, which is not covered.

**F24. Logic: o-minimality, Pila–Wilkie, Ax–Schanuel, model theory of exp.**
- Index: "o-minimality, Pila–Wilkie | C front | vacuous"; C_006 E3 Ax–Schanuel; Zilber/Wilkie "no ordering/sign."
- (g) **NON-VIRGIN.**

**F25. Ultraproducts, Loeb, Łoś.**
- Index: Ξ2 (Loeb form on Ẑ) NO-GO; Φ.13 Łoś dichotomy.
- (g) **NON-VIRGIN.** Ramsey/partition: see V2.

**F26. Pseudofinite fields and definable counting measures (Chatzidakis–van den Dries–Macintyre).**
- (a) Positive definable measure with Lang–Weil error.
- The source of the sign is Lang–Weil, which is RH over finite fields. That is the function-field model of phase
  145 (T1 allows field-uniform proofs, but the model has already been explored).
- (g) **NON-VIRGIN** (via phase 145 and the Deligne route).

**F27. Clifford / hypercomplex analysis / Weitzenböck.**
- Index: G2 Clifford/Weitzenböck, "both summands indefinite."
- (g) **NON-VIRGIN.**

**F28. p-adic analysis and the Mahler measure.**
- Corpus: 114.a.04 "Mahler scalar gauge on rational Witt vectors," with I7 closed. p-adic Tate moments in d_S
  (index).
- (g) **NON-VIRGIN.**

**F29. Differential geometry: Ricci flow / Perelman entropy, Bakry–Émery, Cheeger.**
- Index: Ricci in 45 lines (bootstrap-in-T closed); B2 Γ₂; K7 Cheeger (reaches ½).
- (g) **NON-VIRGIN.**

**F30. Alexandrov–Fenchel / mixed volumes / BKK / arithmetic isoperimetry.**
- (a) Alexandrov–Fenchel: V(K,L,…)² ≥ V(K,K,…)V(L,L,…). It is a Hodge index theorem for convex bodies (CITED).
- (b) Index: "Monge–Ampère / arithmetic isoperimetry… virgin, no concrete object: not launched" (SPEC_006 #17); F5
  non-AHK Hodge–Riemann and G6 Lorentzian (retry, no sign). AF is the Lorentzian form of Brändén–Huh.
- (g) **NON-VIRGIN** by adjacency (Lorentzian/Hodge–Riemann already registered).

**F31. SOS in group algebras / Kazhdan's property (T) (Ozawa 2016: (T) ⟺ Δ² − εΔ is SOS in ℝ[G]).**
- Index: Kazhdan, 0 hits. "Positivstellensatz / SOS / NC-SOS | REF-D / class (D)" covers the mechanism. For
  G = ℚ⋊ℚ^× (ax+b, amenable) there is no (T) at all (CITED: infinite amenable groups do not have (T)), so the
  theorem is vacuous there.
- (g) **NON-VIRGIN** by mechanism, and vacuous for ax+b.

**F32. Persistent homology / TDA.**
- Index: NG-A7.
- (g) **NON-VIRGIN.**

---

## 4. The three VIRGIN-VIABLE families

They evade Thm 3′/O7 for a shared reason, written here as a new reason. Thm 3′ (ARGUED) kills "rank-type" counts χ
with **analytic** dependence on the test: the generic rank is constant on a dense open set (Vandermonde, δ ≡ 0).
**Non-negative rank**, **sign rank** and **recurrence functions on sets** are not analytic invariants but
**semialgebraic or combinatorial** ones. For instance, for positive 4×4 matrices of rank 3, r_+ = 3 and r_+ = 4 both
occur on open sets (Cohen–Rothblum 1993, CITED; the Lovász/Yannakakis square example), so **there is no generic
value** and Thm 3′'s "constant on a dense open set" conclusion does not apply. This is the only class of integer
counts I know of with that property that does not appear in the index ("nonnegative rank," "sign rank,"
"Yannakakis," "extension complexity," "Forster," "Moreira," "Hindman," "Ramsey": 0 hits in the index; in the corpus
only two mentions of "nonnegative" in phase 15 with a different meaning). Web search ("nonnegative rank OR sign
rank Weil explicit formula positivity zeta"): the results use rank and trace (arXiv 2608.13637, 2607.02828,
2608.24827), not non-negative rank nor sign rank.

### V1. Non-negative rank and extension complexity (Yannakakis 1991) — rank 1

- **Positivity theorem (CITED).** Yannakakis: the extension complexity of a polytope P equals r_+(S_P), the
  non-negative rank of its slack matrix S_P ≥ 0. Fiorini–Massar–Pokutta–Tiwary–de Wolf (2012) give lower bounds via
  rectangles and coverings. Gouveia–Parrilo–Thomas (2013) give the psd-rank version for spectrahedral cones. The
  positivity is in the structure: it is a factorization S = UV with U, V ≥ 0 entrywise.
- **Instantiation.** On the window, take the **pattern polytope** 𝒫_T^{(+,·)} ⊂ ℝ^{N_T} (N_T = ⌊e^{2T}⌋), whose
  vertices are the incidence vectors of triples (k, n, m) with m = kn or |m − kn| ≤ 1 (the m ≈ kn layer of the
  semiring principle), weighted by v_n = 2Λ(n)/√n. Its slack matrix S_T is what is studied.
- **S1.** S_T does not use 𝔞_T or its kernel: only Λ and the (+,·) incidence.
- **S2.** r_+(S_T) is an integer that reads (ℕ,+,·), because the monochromatic rectangles of S_T are sets (k,n)
  with kn in an additive band. For Beurling the additive layer m ≈ kn ± 1 does not exist. For Epstein, the
  "multiplication" of ideal norms is not that of ℕ.
- **S3.** The duality is factorization ↔ extension (Yannakakis), i.e. the LP duality of the projection. It is
  neither Poisson nor Möbius. Caution: if the duality turns out to be the certificate LP (thm:Z), it falls into
  branch 2. That is the main risk and remains **OPEN**.
- **S4.** P_T enters via the restriction to tests with A = B = 0 in the dual cone. OPEN.
- **S5.** r_+ is discontinuous on the comb: lower semicontinuous, and it jumps across semialgebraic strata.
- **S6.** OPEN. The proposed channel is that Λ_cosh(n) = log n·Σκ_j b^{∗2j}(n) enters as a multiplicative
  autoconvolution term in S_T. That changes the support of the rows and hence r_+, something a linear functional
  cannot see.
- **Φ200 branches.** It evades branch 1 (it is not continuous) and branch 3 (it is not a functional of h*, it is an
  invariant of the datum). Branch 5 (equality between data, C-data) is the risk if r_+(S_T) turns out to be a
  function of data without a (P)/(D) variable.
- **Λ channel (O11).** Coordinate and support in the m ≈ kn layer. Falsifiers: Beurling (no additive layer) and
  a_P (same support, different weights). r_+ is sensitive to zero entries, not to positive weights. If a_P > 0 on
  the same support, r_+ coincides and **V1 dies**, unless the weights enter via a threshold. That threshold must be
  named.
- **First exact lemma (Lemma V1.1, OPEN, computable in finite form).** Let
  S_T^{(Λ)}(m; (k,n)) = 1_{m = kn}·v_n − 1_{m = kn+1}·v_n on m ≤ e^{2T}, compensated to ≥ 0 by the slack of the
  pattern polytope's inequalities. One must determine whether there exists T ≤ ½log15 such that
  r_+(S_T^{(Λ)}) ≠ r_+(S_T^{(a_P)}) and ≠ r_+(S_T^{(Beurling)}), with equal ordinary ranks. A **yes** is the first
  non-generic integer separation of Λ from the battery (S2 + S5 at once). A **no** closes V1 with a support NO-GO.
  Exact computation of r_+ is NP-hard (Vavasis 2009, CITED), but for N_T ≤ 15 it is feasible with rectangle bounds
  and the Shitov bound.

### V2. Additive-multiplicative recurrence (Moreira 2017; Bergelson–Moreira 2017) — rank 2

- **Positivity theorem (CITED).** Moreira (Annals 2017): every finite coloring of ℕ has a monochromatic {x, x+y,
  xy}. Bergelson–Moreira (ETDS 2017) prove an ergodic theorem for actions of the affine group of a field: for A
  with positive multiplicative density, the lim inf of the averages of μ(A ∩ A_{+u} ∩ A_{×u}) is > 0. The
  positivity is a measure recurrence, from the structure of the ℚ⋊ℚ^× action.
- **Why it is not NON-VIRGIN.** The index covers ×2,×3/solenoid (only ℚ^×, C-MvN) and the J front (+ and · as a
  frustrated ferromagnetic graph). A measure recurrence for the affine action is not a correlation inequality on a
  graph, so the frustration Thm 1.3 does not apply: there are no couplings J required to be ≥ 0. This is the new
  reason, written down.
- **Instantiation.** A measure μ_Λ on the affine-Bohr compactification of ℚ, built by Furstenberg correspondence
  from the weighted comb, with the functional R_T(A) = average over u ≤ e^{2T} of μ_Λ(A ∩ (A−u) ∩ u^{−1}A).
- **S2.** It reads (ℕ,+,·) literally: it is the semiring principle at m ≈ kn. Beurling has no additive action and
  the object does not exist for it (O4).
- **S3.** The duality would be between the affine Kronecker factor and the weakly mixing complement. It is not
  Poisson. OPEN whether it produces a χ.
- **S5.** Being a set function, R_T is discontinuous on the comb.
- **S6.** No channel declared (weak). Λ_cosh enters only if the Furstenberg correspondence uses the full Λ_Q. OPEN.
- **Φ200 branches.** Risk of branch 4: the recurrence holds for **every** positive-density set, so it may be blind
  to ζ. To avoid this, A must depend on the test (A = {n : F(log n) > 0}), which may reintroduce branch 3.
- **Falsifier.** Epstein 11, because O_K also has + and ·. V2 must name the property of ℤ missing in O_K (C-Guo).
  Candidate: the total order and the additive unit 1, which give the canonical layer m = kn + 1.
- **First exact lemma (Lemma V2.1, OPEN).** For A_F = {n ≤ e^{2T} : F(log n) > 0} with F ∈ P_T, the quantity
  R_T(F) = Σ_{x,y : x+y, xy ≤ e^{2T}} v_x v_y 1_{A_F}(x)1_{A_F}(x+y)1_{A_F}(xy) is **not** a function of the values
  {𝔞_T(F)} ∪ {data of P_T}. That is, it does not fall into C-data / branch 5. This is proved with two tests F₁, F₂
  with equal 𝔞_T and different R_T. If R_T were a function of 𝔞_T, V2 dies in branch 5.

### V3. Forster sign rank (2002) — rank 3

- **Positivity theorem (CITED).** Forster: for M ∈ {±1}^{N×N}, sign-rank(M) ≥ N/‖M‖. The proof uses the existence
  of a radial isotropic position (positivity of the normalized frame operator, Barthe 1998).
  Linial–Mendelson–Schechtman–Shraibman give the margin version.
- **Instantiation.** The additive sign matrix H_N(m,n) = λ(m+n) (or μ²-weighted), m,n ≤ N = ⌊e^{T}⌋. It is an
  additive Hankel matrix of a completely multiplicative function, so it reads + against ·. The multiplicative
  matrix λ(mn) = λ(m)λ(n) has rank 1. The gap between the two is the datum.
- **S2/S5.** Integer and discontinuous.
- **S1.** It does not use the form.
- **S3/S6.** No channel: λ does not see Γ. The connection to the window would be ‖H_N‖ = o(N), a Chowla-type
  cancellation statement (Matomäki–Radziwiłł–Tao, CITED on average). That is a bound, not a sign.
- **Risk.** R-K1 (Hankel ⟹ NN′) and O6 (no Hankel). H_N **is** an additive Hankel matrix, though on λ and not on
  the gap c_N = 0. It must be checked that R-K1, stated for the gap, does not extend.
- **First exact lemma (Lemma V3.1, OPEN).** As N → ∞, sign-rank(H_N^{λ}) versus sign-rank(H_N^{λ_P}), where λ_P is
  the Liouville function of a Beurling system with the same primes ≤ N rounded. If they coincide for all N, V3 is
  comb-generic (branch 1) and dies.

### Ranking

| # | family | S1 | S2 | S3 | S4 | S5 | S6 | main risk | first lemma |
|---|---|---|---|---|---|---|---|---|---|
| 1 | V1 non-negative rank / Yannakakis | yes | yes | OPEN (branch-2 risk) | OPEN | yes | OPEN (proposed channel) | a_P with same support | V1.1 (finite, computable) |
| 2 | V2 recurrence {x+y, xy} | yes | yes | OPEN | OPEN | yes | weak | branch 4 / Epstein | V2.1 |
| 3 | V3 Forster sign rank | yes | yes | no | OPEN | yes | no | R-K1 / Chowla = bound | V3.1 |

V1 comes first because its first lemma is finite, decidable, and names a concrete falsifier (a_P). V2 comes second
because it is the only family found that reads + and · without a ferromagnetic graph, but its S6 is the most
distant. V3 remains an auxiliary tool for V1 (sign rank bounds r_+ from below).

## 5. Entries for the index (to be added by the synthesizer; I do not write them)

**VIRGIN-DEAD, by application of existing restrictions:**
- F15 frames: branches 1/2.
- F16 Fuglede/Delsarte: branch 2.
- F17 Royen: branch 1, plus Henderson Zenodo 19636675.
- F19 EPI/ABBN: branch 1, C-E′ + Lemma 13.1.
- F20 Fisher–Rao: branch 1.
- F21 large deviations: branches 4/2.

**NON-VIRGIN with citation:** F6 Painlevé (Burnol 1008.0617) and F7 Gelfand–Levitan (R186 TB-1, Khuri hep-th/0111067
(corrected attribution)).

**VIRGIN-VIABLE:** V1, V2 and V3, with lemmas V1.1, V2.1 and V3.1, all OPEN.

## Web sources consulted
- [Wu–Sprung, Inverse scattering, the coupling constant spectrum, and the Riemann hypothesis](https://arxiv.org/html/hep-th/0111067)
- [More than two thirds of the zeta zeros… (rank-trace, Weil form)](https://www.alphaxiv.org/abs/2608.13637)
- [A finite Guinand–Weil dictionary… (arXiv 2607.02828)](https://arxiv.org/pdf/2607.02828)
- [Weil positivity in compact windows (arXiv 2608.24827)](https://arxiv.org/pdf/2608.24827)
- [Positive solutions of the explicit formula for ζ(s) (Zenodo 23211712)](https://zenodo.org/records/23211712)
- [Entropy power inequality (general reference)](https://en.wikipedia.org/wiki/Entropy_power_inequality)

The classic CITED references (Yannakakis 1991; Fiorini et al. 2012; Gouveia–Parrilo–Thomas 2013; Cohen–Rothblum
1993; Vavasis 2009; Moreira 2017; Bergelson–Moreira 2017; Forster 2002; Barthe 1998; ABBN 2004; Royen 2014; Ozawa
2016; Fröhlich–Israel–Lieb–Simon 1978; Newman 1976) are from bibliographic memory and were not re-checked in this
session. They must be verified before use in Paper 47.
