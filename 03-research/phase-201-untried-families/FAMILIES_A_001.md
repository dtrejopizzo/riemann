# FAMILIES_A_001 — Inventory A (phase 201): algebra, combinatorics, algebraic/arithmetic geometry, topology, category theory, homological, representations

Row D (window form 𝔞_T on 𝒫_T, L′♯). Nothing is built here: this is only an
inventory with a filter.

## Summary (≤300 words)

I inventoried 30 families in domain A with a structural positivity theorem (sign proved by structure, not by a
bound). For each one I grepped the index `05-meta-and-planning/ROUTES-TRIED-INDEX/` and did a web search for "Weil
positivity / explicit formula + family." I then filtered them by SPEC-𝔇 S1–S6 (HORN_B_BIGSHARP_001 §3) and by the
5 branches of Φ200 (SPEC_SIGN_OBJECT_006 §B).

The dominant filter is an index result not in the mandate: **G1 (PROVED)**, "the free monoid ℕ^× does not
distinguish ζ from Beurling or from fields." It kills, on branch 1 (comb-generic), every combinatorial positivity
that reads only the multiplicative structure: symmetric functions/Schur/Kostka/LR, Macdonald, Koszul over ℕ^×,
Dirichlet species, pure Cohen–Lenstra/Hall and local quivers. These are virgin, but dead.

Result: **12 NON-VIRGIN**, among them Lorentzian/AHK, Soergel/KL, cluster, total positivity, hyperbolic,
Borcea–Brändén, tropical, ampleness, purity, Cohn–Elkies, Morse/index, Jones/categorification, persistent
homology, Ihara, theta/Howe and Weil-étale/Artin–Verdier. **15 VIRGIN-DEAD**, each with its branch. **3
VIRGIN-VIABLE**:

1. **Björner complex of squarefree integers with additive coupling faces**, plus the Stanley–Reisner /
   Lefschetz package via Adiprasito anisotropy. Its χ is an integer count giving M(x) (CITED: Björner
   2011). It is discontinuous on the comb (S5) and has Poincaré/Alexander duality, which is not Poisson (S3).
2. **Hall algebra of Arakelov ℤ-lattices** (Kapranov: the Eisenstein functional equation comes out of the Hall
   algebra). The structure constants are integer counts (S2) and there is a categorical Serre duality (S3). Main
   risk: Epstein (branch 1) and vdG–S (S3).
3. **Koszul duality of a bigraded algebra encoding (ℕ,+,·)**: H_A(t)·H_{A^!}(−t)=1 and Hilbert positivity via the
   Koszul condition (S3 non-Poisson). No candidate algebra exists and it is the lowest-ranked.

None of the three satisfies S6 (Λ_cosh) natively. This is the hardest restriction of domain A: every
algebraic/combinatorial positivity is non-archimedean. For each one, the first exact lemma is given (§4). No new
PROVED result. The branch verdicts are ARGUED except where a NO-GO from the index is cited.

## 0. Method and sources

- Read: README of phase 201; HORN_B_BIGSHARP_001 §3 (S1–S6); SPEC_SIGN_OBJECT_006 §B (Φ200, branches 1–5);
  survey /SYNTHESIS.md; ROUTES-TRIED index (README and tables, keyword grep).
- Index grep, with the word and the number of files with a hit. Kazhdan 0, Kostka 0, Fukaya 0,
  Khovanov 0, Tannaka 0, Ramsey 0, Hall alg 0, Stanley/h-vector 0, Ehrhart 0, quiver 0, Koszul 0, Macdonald 0,
  symmetric func 0, Hilbert series 0, Gorenstein/Macaulay/shellab 0, Coxeter 0, Specht 0, Schubert 0, species 0,
  chromatic/Tutte 0, Björner 0, Kapranov 0, Cohen–Lenstra 0, Artin–Verdier 0, anisotrop 0, simplicial 0. Non-zero
  hits: matroid 2, Lorentzian 4, Huh 3, total positiv 4, cluster 8, hyperbolic 5, Gårding 2, Borcea 2, persistent 2,
  Morse 1, ample/nef 9, tropical 6, Jones 2, purity/weight 10, Möbius/poset 6, Szemerédi 1, Cohn/Elkies 3, Soergel 3,
  Hecke 10, unitar 7, Witt 4, graded dimension 1, Ihara 1, Plücker 1, Minkowski 5, Lefschetz 4, SOS 5.
- Web search (WebSearch), two combined queries:
  - «"Weil positivity" OR "explicit formula" + Kazhdan–Lusztig / Koszul / Hilbert series / Ehrhart»;
  - «Weil explicit formula positivity + Tannakian / Deligne category / Hall algebra».

  No result links these families to Weil positivity. Only certificate literature appears (Zenodo
  23238720, alphaxiv 2609.weil-positivity…, nic410/zeta-positive-solutions), Connes–Consani arXiv 2006.13771 and
  Deligne–Milne *Tannakian categories* (Weil forms = polarizations; see A13). The arXiv API was not searched
  exhaustively, as in the survey. "0 hits" means 0 in those searches, not 0 in the world.
- **Master index filter (G1, PROVED, phases 194–198):** "the free monoid ℕ^× does not distinguish ζ from Beurling
  or from fields." The same block declares dead "Supersymmetry, Clifford, Soergel/KL, VOA/moonshine, Lorentzian,
  cluster, Jordan, Connes–Kreimer, involutions, Elias–Williamson." Anything that reads only (ℕ^×, ·) falls on branch
  1 by G1.

Table notation: **S** = S1…S6 satisfied (✓), failed (✗) or open (?). **Branch** = Φ200 branch that kills it.
**Falsif.** = falsifier from the battery (Epstein 11, DH 12, a_P, cΛ, Beurling).

## 1. NON-VIRGIN families (already used: not retried)

**A1. Lorentzian polynomials / AHK / combinatorial Hodge–Riemann / log-concavity (Huh, Brändén–Huh 2020,
Adiprasito–Huh–Katz 2018).**
- Theorem (CITED): the Hodge–Riemann form of the Chow ring of a matroid has the correct signature, and Lorentzian
  polynomials are closed under linear operators that preserve stability.
- Index: table "Lorentzian polys, Hodge–Riemann, AHK Kähler package, matroids | P41-2; G8H-R160_S2; CA vs F/G | NO-GO
  / = parity Schur"; also "Kähler packages for non-algebraic objects … Babaee–Huh" and row 35 "F5 Hodge–Riemann /
  Lorentzian (non-AHK): signature hypothesis fails."
- **NON-VIRGIN.** The same holds for Kazhdan–Lusztig–Stanley of matroids (Braden–Huh–Matherne–Proudfoot–Wang) and
  for log-concavity of Tutte/chromatic (Huh): they are the same Kähler package and inherit P41-2. Applying
  log-concavity to (Λ(n)/√n) or to (c_N) would be a cone condition on a sequence, which is branch 2/1, and is
  already covered by "= parity Schur."

**A2. Kazhdan–Lusztig / Soergel / Elias–Williamson (coefficient positivity via Hodge theory of Soergel bimodules).**
- CITED: Elias–Williamson, Ann. Math. 2014.
- Index: "Soergel/KL … Elias–Williamson on the window ladder: dead" (block G). **NON-VIRGIN.**

**A3. Total positivity, Lusztig, canonical bases, cluster algebras, positroids, amplituhedron.**
- CITED: Lusztig 1994, canonical basis positivity; Lee–Schiffler 2015, Laurent positivity in clusters.
- Index: L23 "Pólya frequency / total positivity … COVERED"; G7/J5 "total positivity of order ≤ 4 (PF₄ OPEN)";
  "cluster dead"; "Amplituhedron / positive geometry … ≈ TP (closed family)." **NON-VIRGIN.** The "canonical
  basis" does not give 0 hits as an independent class: its positivity is TP in another coordinate.

**A4. Hyperbolic polynomials (Gårding), stable (Borcea–Brändén), interlacing (MSS).**
- Index: "B1. Hyperbolic polynomials, Gårding cones, real stability (Borcea–Brändén), MSS interlacing families —
  score 4"; "Jensen hyperbolicity … closed." **NON-VIRGIN.**

**A5. Tropical / Allermann–Rau / Berkovich.**
- Index: P41-1 PARTIAL (toy (1,2), real and non-integral); "Tropical, Berkovich | L10, L29; phase-152 | DEAD."
  **NON-VIRGIN.** What remains (S2) is exactly what is already registered as failed.

**A6. Ampleness / nefness / Kleiman / Nakai–Moishezon ("arithmetic ampleness of the window divisor").**
- Index: row 52 "F15 nef/ample, Nakai–Moishezon on arithmetic square | class (D)." **NON-VIRGIN.** The "window
  divisor" version is that same row: ampleness on the arithmetic square presupposes the square, which does not
  exist (S3).

**A7. Weight purity (Deligne Weil II), "window motive."**
- Index: R9-04, R9-13 ("weight", "Adams grading … LITERATURE-ONLY (negative)"); the Deligne route (phases 149–150);
  Weil-étale in HORN_B §table. **NON-VIRGIN.** A pure "window motive" of weight w is a Tannakian polarization
  (see A13).

**A8. Morse / spectral flow / index / Floer.**
- Index: BARRIER_W_001 (phase 197), "NO-GO class 𝒦_W (Morse index / spectral flow / signature)." **NON-VIRGIN.**

**A9. Jones / Temperley–Lieb / categorification (Khovanov).**
- Index: row 43 "E3 Jones index / TL Gram | no object"; row 55 "G4 categorification / graded dimension." Khovanov
  gives 0 hits by name, but its positivity is that of a categorified "graded dimension," already covered by row 55.
  **NON-VIRGIN.**

**A10. Persistent homology.**
- Index: NG-A7 / ES-5 "TDA persistent homology H0/H1 as detector … NUMERICAL-ONLY." **NON-VIRGIN** as a detector.
  The structural use (Betti numbers of an arithmetic complex) is a different matter: treated in V1.

**A11. Cohn–Elkies / packings / linear programming with Poisson.**
- Index: row 76 "L3 Cohn–Elkies | gives upper (Odlyzko) direction | THM"; also the "magic functions" V1–V3.
  **NON-VIRGIN.** By construction it is S3 ✗ (Poisson).

**A12. Ihara / Ramanujan graphs / expanders.**
- Index: L91. **NON-VIRGIN.**

**A13. Tannaka / Weil forms in Tannakian categories (Deligne–Milne: Tr(u∘u†) > 0, polarizations).**
- CITED: Deligne–Milne, *Tannakian categories*, §5 (jmilne.org/math/xnotes/tc2018.pdf).
- Index: "Tannaka" gives 0 hits by name. But Tannakian Weil positivity is that of a polarization, i.e. a standard
  Hodge-type conjecture. That line is closed: "Hodge-transfer line closed in all its corners" (HORN_B §5;
  R9-01/R9-13; phases 134–148).
- **NON-VIRGIN** in content, though virgin in name. Tannakian duality (group reconstruction) is not Fourier, but
  gives no sign without a polarization.

**A14. Weil-étale / Artin–Verdier (Grothendieck duality, non-Fourier, on Spec ℤ).**
- Index: "Weil-étale (Lichtenbaum, Flach–Morin) | S6, S4." Artin–Verdier gives 0 hits by name, but it is the base
  duality of the Weil-étale complex. **NON-VIRGIN.**

**A15. Unitarity / Weil representation / Howe duality / theta.**
- Index: "unitar" 7 hits (bootstrap mechanism: "unitarity + crossing ⇒ linear functionals"); theta is closed in
  Φ200 (piece "Bochner on θ," Theorem S (C-θ), branch 1). **NON-VIRGIN.**

**A16. Sum-product / Szemerédi–Trotter / Erdős–Szemerédi.**
- Index: row 22 "H4 sum-product … set statements ignore weights." **NON-VIRGIN.**

## 2. VIRGIN-DEAD families (0 hits; die in the filter)

| # | Family | Positivity theorem (CITED) | Instantiation on the window (one sentence) | S that fails | Φ200 branch / falsifier |
|---|---|---|---|---|---|
| M1 | Symmetric functions: Schur, Kostka, Littlewood–Richardson | K_{λμ} ≥ 0 and c^ν_{λμ} ≥ 0 (Macdonald, *Symmetric functions*, 1995) | with x_p = p^{−s}: log ζ = Σ_k p_k(x)/k, so Λ is the power-sum coefficient, and Schur-positivity of the form would be requested | S2 (only ·), S6 | **branch 1 by G1**; Beurling has the same x_p |
| M2 | Macdonald / Haiman (n!) positivity | q,t-Kostka coefficients ∈ ℕ[q,t] (Haiman 2001) | (q,t)-deformation of M1 | S2, S6 | branch 1 (G1) |
| M3 | Koszul over ℕ^× (the polynomial of ℚ[x_p] and its exterior dual) | H_A(t)H_{A^!}(−t)=1; Hilbert positivity of A^! (Backelin–Fröberg) | 1/ζ = Hilbert series of the exterior dual (μ of the squarefree numbers) | S2 (only ·) | branch 1 (G1); μ is unimodular only on the free ℕ^×, and Beurling gives the same |
| M4 | Dirichlet species (Baez–Dolan), exponential formula | positivity of the exponential formula | ζ = species of finite sets with Dirichlet weight | S2 | branch 1 (G1) |
| M5 | Cohen–Lenstra / Hall algebra of p-groups | Σ_G 1/\|Aut G\| = Π(1−p^{−i})^{−1}; Hall numbers ≥ 0 | count of abelian groups of order n (reads ·) | S6, S2 | branch 1 (local, place by place; survey P2 ✗). Lives only in the Arakelov variant (V2) |
| M6 | Quivers / Kac polynomials (Hausel–Letellier–Rodriguez-Villegas 2013: coefficients ≥ 0) | Kac positivity | count over 𝔽_p | S6, S4 | branch 1 (local datum at fixed p) |
| M7 | Ehrhart / h*-non-negativity (Stanley 1980) | h*_i ≥ 0 on lattice polytopes | counting points of {mn ≤ x} | non-polytopal region (hyperbola), no polynomiality; S3: Ehrhart reciprocity is proved via Poisson (Beck–Robins ch. 5) | branch 1 (counts over quadratic regions are those of Epstein 11) |
| M8 | Brunn–Minkowski / Alexandrov–Fenchel | log-concave mixed volumes | mixed area of window bodies | already touched in phase 200 ("mixed area," MAP_200/AUDIT_200_DCONS) | branch 2/1 (phase 200). More than virgin-dead it is NON-VIRGIN via phase 200 |
| M9 | Symplectic capacities, Gromov non-squeezing (Fukaya 0 hits) | c(B) ≤ c(Z) monotone | capacity of the time–frequency box [−T,T]×[−Ω,Ω] | S2, S6 (it is prolate geometry) | branch 2: CCM prolates (L106, REF-D) |
| M10 | Ramsey / Sidorenko densities / flag algebras (Razborov) | t(H,W) ≥ t(K₂,W)^{e(H)}; flag SOS | graph n∼m if m≈kn (weighted) | S1 | branch 2: flag algebras are SOS (index: "Positivstellensatz / SOS … REF-D"); Sidorenko is branch 1 (insensitive to weights, O2/O6) |
| M11 | Schubert calculus, Graham positivity | c^w_{uv}(t) ∈ ℕ[α_i] | torus weights = log p | no object; S2 | branch 1 if forced (free weights = Beurling) |
| M12 | Symmetric group representation theory (Specht), characters ≥ 0 in dimension | dim S^λ ∈ ℕ | no natural one | no Λ channel | branch 4 (blind to ζ) |
| M13 | Rota's Möbius function on non-divisor posets (geometric lattices, alternating μ, Rota 1964) | (−1)^r μ ≥ 0 on geometric lattices | poset of divisors truncated to ≤ x | partial S2 | the sign alternation is exactly Björner's: absorbed into **V1** |
| M14 | Modular / Borcherds (0 hits "modular form") | positivity of Eisenstein coefficients | window via a weight-k form | S3 (theta = Poisson) | branch 1 (Theorem S, C-θ) |
| M15 | Operads / Connes–Kreimer | — | — | — | dead in block G (Connes–Kreimer); NON-VIRGIN de facto |

Comment: M1–M6 are the main contribution of the inventory as **NO-GO by G1**. Every "counting" positivity that
reads only the free ℕ^× fails S2 and the semiring principle. This turns the phase-201 question, for domain A, into
this other one: **what positive algebraic structure reads the sum?** The three viable ones are the only ones I
found where the + enters the structure itself and not the test.

## 3. VIRGIN-VIABLE families

### V1. Björner complex of squarefree integers with additive coupling + Stanley–Reisner / Lefschetz package

- **Key positivity theorem (CITED).**
  - Björner, "A cell complex in number theory," *Adv. Appl. Math.* 46 (2011): the simplicial complex Δ_n, whose
    faces are sets of primes with product ≤ n, has reduced Euler characteristic −M(n) (Mertens). Its homotopy type
    is a wedge of spheres, with Betti numbers ≥ 0 and |M(n)| = number of spheres (via discrete Morse theory).
  - Stanley–Reisner (Stanley 1975), Cohen–Macaulay ⇒ h-vector ≥ 0.
  - Adiprasito, "Combinatorial Lefschetz theorems beyond positivity" (2018): hard Lefschetz and Hall–Laman via
    **anisotropy**. There, positivity of a quadratic form (Hodge–Riemann) is **not** used: what is used is that the
    form is anisotropic in generic characteristic.
- **Index.** Björner, simplicial, anisotrop, Stanley: 0 hits. The index has "Net index/Fredholm/Euler
  characteristic | Euler/Möbius algebra … DEAD [OTHER:net-…]" (G8D-R160_S3), which is a Fredholm χ, not a
  combinatorial complex. It also has NG-A7, which is persistent homology as a numerical detector. Neither covers
  the complex Δ_x nor its Stanley–Reisner ring. Grep in the corpus (03-research, 04-papers): 0 hits of Björner.
- **Web.** There is no union "Weil positivity + Björner / Stanley–Reisner." The Mertens ↔ χ(Δ_n) relation is CITED
  (Björner; there are follow-up works on the homology of Δ_n), but only for μ and M(x), never for the Weil
  quadratic form.
- **Instantiation.** Define Δ_{F,T} with vertices = primes p ≤ e^T and faces = sets with log Π p in the support of
  the window. Add **additive coupling faces**: a pair {n, m} with |m − kn| small is joined by a cell (the
  semiring). The window form is read as a Lefschetz/intersection pairing on the Stanley–Reisner ring with weights
  c_F(log n).
- **Filter.**
  - S1 ? : χ is a *computation* (Euler characteristic of a complex), not χ := R(E). Good as a start.
  - S2 ✓ : the Betti numbers are integers and the complex reads ·. The additive faces are the only way for it to
    read +. Without them, Δ_x for a Beurling generalized-integer system still exists: branch 1 via G1.
  - S3 ✓ (in principle): the duality is combinatorial Alexander/Poincaré duality (Δ ↔ Δ^∨, the Alexander dual
    complex), which is not Poisson. With Adiprasito anisotropy it gives a **quadratic** object (middle-degree
    pairing) without needing an arithmetic surface.
  - S4 ? : compatibility with P_T (support [−T,T] is literally the face threshold). Good.
  - S5 ✓ : Δ_x jumps at every integer; the complex is discontinuous on the comb, and for Epstein there is no prime
    complex. The falsifier fails **at the construction**, which is what S5 requires.
  - S6 ✗ : there is no archimedean term. One would have to add a "vertex at ∞" with weight Γ_ℝ; nothing in the
    theory suggests it.
- **Λ channel.** Λ = −μ * log. The complex gives μ via χ; log enters through the threshold filtration (∂_x of the
  faces). It is an I5 channel (comb), so there is a risk of branch 1 if the dependence is only through pointwise
  values.
- **Falsifiers.** Beurling (kills the version without additive faces), cΛ (changes the weights, not the complex:
  the complex is blind to c and that is why it needs the weights in the pairing), DH 12 (has no Euler product, so
  there is no complex: it fails at the construction, good).
- **Risk.** The weighted pairing could simply be the Weil form written in the face basis (branch 2, REF-D).
  Anisotropy is the only ingredient that could avoid this.
- **Verdict: VIRGIN-VIABLE** (priority 1, ARGUED).

### V2. Hall algebra of Arakelov ℤ-lattices (Kapranov)

- **Key positivity theorem (CITED).**
  - Kapranov, "Eisenstein series and quantum affine algebras," *J. Math. Sci.* 84 (1997): in the Hall algebra of
    bundles over a curve over 𝔽_q, Eisenstein series satisfy quadratic relations whose functional equation is that
    of ζ_X.
  - The Hall structure constants are counts ≥ 0 (Hall polynomials, Ringel 1990).
  - The number-field case (Arakelov bundles = ℤ-lattices with a metric) is sketched in Kapranov–Smirnov and in the
    q → 1 heuristic; the index records it only as a dictionary (phase 159, G1_B9: "The q→1 dictionary is
    heuristic").
- **Index.** Kapranov gives 0 hits in the index; in the corpus it appears only as a citation in the q→1 dictionary
  (phase 159 G1_B9_R1/R3). Hall algebra gives 0. Cohen–Lenstra gives 0. There is no registered route using the
  *Hall structure constants* as a source of sign. **New written reason** (relative to the function-field transfer
  of phase 159): there, Weil/Bombieri was transported on C×C; here, a quadratic identity of the Hall algebra would
  be used (the commutator of the Eisenstein currents), which is a different object and does not presuppose the
  square.
- **Web.** There is no union "Weil positivity + Hall algebra."
- **Instantiation.** The Eisenstein currents E(z) of the Hall algebra of ℤ-lattices, paired with the window test.
  The relation E(z)E(w) = (ζ(w/z)/ζ(z/w)) E(w)E(z) transports the window form into a Hall norm (a Green's
  product with a positive metric).
- **Filter.**
  - S1 ? : Kapranov's identity is proved in the Hall algebra, not from I_∞.
  - S2 ✓ : counts of sublattices of index n are entire σ-functions and read (ℕ,+,·) via extensions
    0→A→B→C→0. The + enters through the direct sum.
  - S3 ? : the duality is Serre duality in a hereditary category (Ext¹ ↔ Hom^∨). But in the Arakelov case the
    archimedean part is theta/Poisson (vdG–S, Prop 20.1): **direct risk of S3 ✗**.
  - S4 ? .
  - S5 ? : lattice counts are the same for general quadratic forms, which is **Epstein 11**.
  - S6 ✓ in principle: the archimedean metric of the lattices gives Γ_ℝ.
- **Λ channel.** Λ enters through log of ζ in the commutation relation; it is the I1/functional-equation channel.
- **Falsifiers.** Epstein 11 (high risk, branch 1), vdG–S (branch 2 via Prop 20.1).
- **Verdict: VIRGIN-VIABLE** (priority 2, ARGUED). It is the only family in domain A that has S6 together with S2.

### V3. Koszul duality for a bigraded algebra encoding (ℕ,+,·)

- **Theorem (CITED).** For A Koszul: H_A(t)·H_{A^!}(−t) = 1, and A^! has a series with coefficients ≥ 0, which is a
  sign restriction on 1/H_A(−t) (Polishchuk–Positselski, *Quadratic algebras*, 2005; Backelin–Fröberg).
- **Index.** Koszul gives 0 hits. The version over ℕ^× (M3) is branch 1 via G1.
- **Instantiation.** A quadratic algebra A_T generated by the integers ≤ e^T with two gradings (log n and an
  additive degree), whose quadratic relations encode m ≈ kn. Koszul positivity ⇒ sign on a series that is the
  restricted window form.
- **Filter.** S2 ✓ (by design), S3 ✓ (Koszul is neither Poisson nor flat Möbius), S5 ✓ (the relations are
  discrete), S1 ?, S4 ?, S6 ✗.
- **Verdict: VIRGIN-VIABLE** (priority 3; no candidate algebra exists, OPEN).

## 4. Ranking and first proof lemma

1. **V1 (Björner–Stanley–Reisner with additive faces).**
   - **Lemma V1.1 (to prove or disprove).** Let Δ⁺_x be the Björner complex Δ_x augmented with edges {n, m} of
     squarefree integers such that m = kn ± 1, k ≤ K. One must decide whether there exists a symmetric ℤ-valued
     pairing on H_*(Δ⁺_x), defined without I_∞ (via intersection/Alexander), such that:
     - (a) its χ weighted by c_F(log n) matches 𝔞_T restricted to tests in 𝒫_T supported on [log 2, T];
     - (b) for a Beurling system with the same counting function, Δ⁺ is not defined or has a different homotopy
       type.

     If (a) holds only by a term-by-term identity, the family dies on branch 2 (the audit points out that such an
     identity is REF-D). If (b) fails, it dies on branch 1. Minimal test: x = 30, K = 2, homology of Δ⁺_30 by hand
     and comparison with that of a Beurling system of primes {2, 3, 5.1, 7, …}.
2. **V2 (Hall algebra of Arakelov).**
   - **Lemma V2.1.** In the Hall algebra of ℤ-lattices of rank ≤ 2 with Haar measure, decide whether the
     commutation relation of the Eisenstein currents E₁(z)E₁(w), restricted to the window test F, gives an
     expression ⟨E₁(F), E₁(F)⟩_Hall = 𝔞_T(F) + (term ≥ 0 by counting). One must also check whether the same
     identity holds for the currents of an Epstein-11 lattice (binary forms of discriminant −11 with h = 1 vs.
     ζ_K).
   - If it holds for Epstein, branch 1 and the family dies. If the archimedean term reduces to theta, S3 ✗ by
     Prop 20.1.
3. **V3 (bigraded Koszul).**
   - **Lemma V3.1.** Decide whether there exists a quadratic algebra A with generators in degree (log p, 1) and
     relations that are Koszul, whose specialized bigraded Hilbert series is ζ_T, the truncated window of ζ, so
     that H_{A^!}(−t) gives 1/ζ_T with a non-trivial second additive grading.
   - Candidate obstruction to disprove first: for Koszul, the quadratic relations on the free ℕ^× (commutativity)
     already give the polynomial/exterior pair (M3). Any extra relation m≈kn breaks freeness and may break Koszul.
     One must prove or disprove that "ℕ-Koszul + additive relation" is compatible.

There is no fourth or fifth viable family in domain A: the remaining virgins die by G1 (branch 1) or by
theta/Poisson (S3). Remark for the SPEC_201_001 synthesis: **S6 is the restriction that domain A does not know how
to satisfy.** Only V2 has it natively, and it is precisely the one that risks S3 and Epstein the most. This suggests
that the choice of a single family in stage 2 should come from inventory B (the analytic domain) for S6, or from V1
with an explicit archimedean graft.

## 5. Sources

- Index: `05-meta-and-planning/ROUTES-TRIED-INDEX/README.md` (block G, G1 PROVED; rows 22, 35, 43, 52, 55, 76; L23,
  L91, NG-A7, P41-1/2, BARRIER_W_001).
- Phase 200: `03-research/phase-200-sign-object/HORN_B_BIGSHARP_001.md` §3; `SPEC_SIGN_OBJECT_006.md` §B.
- Web:
  - [Zenodo 23238720](https://zenodo.org/records/23238720)
  - [alphaxiv 2609 Certified Weil Positivity](https://www.alphaxiv.org/abs/2609.weil-positivity-riemann-zeta-bounds)
  - [Connes–Consani arXiv 2006.13771](https://arxiv.org/pdf/2006.13771)
  - [Deligne–Milne, Tannakian categories](https://www.jmilne.org/math/xnotes/tc2018.pdf)
  - [KLS polynomials arXiv 1712.01250](https://arxiv.org/pdf/1712.01250)
  - [nic410/zeta-positive-solutions](https://github.com/nic410/zeta-positive-solutions)
- Literature cited from memory (not verified online in this session): Björner 2011 (Adv. Appl. Math. 46);
  Adiprasito 2018 (arXiv 1812.10454); Kapranov 1997; Ringel 1990; Haiman 2001; Hausel–Letellier–Rodriguez-Villegas
  2013; Polishchuk–Positselski 2005; Stanley 1975/1980; Lusztig 1994; Lee–Schiffler 2015; Elias–Williamson 2014.
