# CA_F_003 — Is there a polarized object over ℤ whose pairing is not the signature of 𝔞_T? (front F)

Pen and paper. **No sign contact. No negative value for ζ.** This develops F9, F13 and F15, and the coordinator's question (3). It also
treats the structural reading of CA_F_SYNTHESIS (question (2)).

## 1. Corpus and literature check (done first)
| source | object | pairing on a primitive class? | corpus record |
|---|---|---|---|
| Connes–Consani 2205.01391 | Riemann–Roch on Spec ℤ̄ (curve), integer dim_spm H⁰/H¹ | none; logarithmic growth ⌈log(2n+1)/log3⌉ | MAP_5 §1; MW-5 |
| CC 2602.15941 | Picard/Jacobian *monoid* of the adèle class space; framed/rooted Pontryagin duality | none; "no h⁰/χ construction"; infinite genus discussed conceptually | MAP_5 §1; R186_027 "ninguna" |
| CC 2606.06604 | absolute geometry, real locus × Fargues–Fontaine-type phase space | none (grep "square", "self-intersection", "Hodge index" empty) | MAP_5 §1 |
| CC 2609.00299 (twistor line / F_{1²}) | archimedean component | none recorded | R186_027 "ninguna"; index L42 "Hodge index analogue still missing" |
| CC scaling-site square | square with diagonal reading | authors: "still in development" | MAP_5 §2 |
| Cartwright; Jell–Shaw–Smacka 1506.02023 | tropical surfaces, Hodge index (≤1 positive eigenvalue) | yes, but on combinatorial complexes, not over ℤ | MAP_5 §1; P41-1 |
| Yuan–Zhang adelic Hodge index; 2503.14099 local version | arithmetic surfaces over Spec ℤ (finite-dimensional) | yes, for arithmetic varieties, not for Spec ℤ × Spec ℤ | L26, L83, phase 135 |
| 2403.09266 quadratic RR; 2510.08033 arithmetic Riemann–Hurwitz | — | no square of Spec ℤ | R184_009 (W10) |
**Answer to (3), CITED from the corpus audits:** in the 2024–2026 literature recorded in the corpus, no object over ℤ carries an
intersection pairing on a primitive class of a square of Spec ℤ̄, let alone one not equal to the window form. The gap is the absence
of the object (MW-5 / OT-5′ OPEN; W10 NO-GO for declared carriers, P47 Thm 19.25).
Caveat: the CC listing in R186_027 stops at 2609.00299. Papers after were not checked.

## 2. What such an object would have to give (PROVED, under explicit axioms)
Axioms for a "Weil carrier" 𝒳:
- (L) a real vector space N with symmetric pairing ⟨,⟩, and for each test F ∈ P_T a class Γ_F ∈ N with the Lefschetz trace property
  ⟨Γ_F, Γ_G⟩ = 𝔞_T-bilinear(F,G) + (terms killed on P_T);
- (H) a Hodge index statement: ⟨x,x⟩ ≥ 0 for x in a primitive subspace N⁰ ⊇ {Γ_F : F ∈ P_T}.
**Lemma 1.** Under (L), the restriction of ⟨,⟩ to span{Γ_F} is the window form. Under (L)+(H) the target holds. The pairing on
primitive test classes *is* the window form, with no freedom.
*Proof.* Polarization of (L). ∎
So "a pairing on a primitive class that is not the signature of 𝔞_T" is impossible on test classes. The only room is in **how (H) is
proved**. In function fields, (H) comes from geometry that does not use the trace:
- an ample class H, with N⁰ = H^⊥;
- Riemann–Roch on the surface with quadratic growth h⁰(nD) ≈ n²D²/2;
- hence D² > 0 ⇒ ±D effective ⇒ D·H ≠ 0.
**Labelled gap G-F (OPEN).** It is the conjunction of three things:
(a) a surface-type object 𝒳 over ℤ with an ample class;
(b) an h⁰ with quadratic growth and a vanishing/duality theorem;
(c) the trace property (L) for the Frobenius/scaling correspondences.
The known objects have (c) on the curve (CC trace formula) but not (a), and (b) only with logarithmic growth (2205.01391). This is
exactly MW-5. It is a missing construction, not a proof of impossibility. P47 Thm 19.25 (W10) proves only that every *declared*
carrier class postulates the positivity.

## 3. Structural reading, question (2)
Class 𝒢_u: invariants I(q) of a closed semibounded form q (on a separable Hilbert space) that are **invariant under unitary
equivalence**.
**Proposition 2 (PROVED).** Every I ∈ 𝒢_u is a function of the unitary-equivalence class of the self-adjoint operator of q. By the
spectral theorem with multiplicity (Hahn–Hellinger, CITED) that class is its spectral measure class plus multiplicity function. In
particular, I detects λ(q) ≥ 0 only through spectral data: (R)(3)/(R)(5), REF-D.
This covers Floer homology, capacities, signatures, A¹-/GW-degrees of real forms, and heat/Weyl invariants (F1, F2, F4, F6, F12), since
each is defined from q up to unitary equivalence.
Invariants outside 𝒢_u depend on extra structure E (a lattice, a cone, a basis, a Frobenius, an ample class):
- E is a cone and positivity is membership: dual certificate, class (D) (F8, F15);
- E is local data: (B′), (R)(5), O6 (F3; CA_F_001);
- E is a polarized global geometry: §2, gap G-F.
**Label.** Proposition 2 is PROVED. The trichotomy for invariants outside 𝒢_u is ARGUED, with this counterexample shape:
- an invariant of (𝔞_T, E) where E is natural and independent of zeros, with E-positivity proved from E by an ampleness / Riemann–Roch
  mechanism, as in §2;
- or a non-spectral E whose positivity does not reduce to certificates.
No such E is known in this area.

## 4. Verdicts for F9 / F13 / F15
- F9 (DAG/∞-traces): supplies (c)-type trace formalisms, not (a)/(b). OPEN at G-F; NO-GO only for declared carriers (W10).
- F13 (perfectoid tilting): local at one p, so it supplies neither (a) nor (b). The local part is CA_F_001 Proposition 3.
- F15 (nef/ample cones): (a) presupposes the object. Nakai–Kleiman *criteria* are dual-cone statements, class (D).
None of these is a proof of impossibility. The honest label of the polarized-object route is **OPEN (object unbuilt)**, matching MW-5.

## 5. Self-review
- *Lemma 1 is tautological.* It is meant to be. It shows the coordinator's question has a forced answer on test classes, and moves all
  content to how (H) is proved. That is the useful output.
- *Is "quadratic growth needed" proved?* No. It is the function-field mechanism (CITED: Weil/Grothendieck, Hodge index via RR). Other
  proofs of (H) are not excluded. Label: ARGUED as necessity, PROVED as sufficiency in the function-field model.
- *Corpus coverage risk.* The literature check relies on MAP_5/R186_027. The 2609.00299 entry there is one word ("ninguna"), so a
  direct read of that paper is a residual task (low).
