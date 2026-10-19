# CA_F_000 — Seeds, front F (topology and geometry), phase 193

 Pen and paper; **no numerics run**. **No sign contact. No negative value for ζ.**
Notation of Paper 47: window form 𝔞_T on P_T (tests on I_T with the two Tate conditions A(F)=B(F)=0), bottom λ_A(T),
archimedean part m_T (C₀ + Lev), comb weights v_n = 2Λ(n)/√n, autocorrelation c_F. O-labels are Paper 47's (l. 8331–8345).
Screen columns: Idx = ROUTES-TRIED-INDEX retry?; (R) = Problem (R) clause failed; (P) = CA_B (P1)–(P6) failed; O = surviving
falsifier; B′/B″ = shape theorem; FE = FE-class generic; REF-D; [crit] = can it reach relative precision M^{−3} at the central cell.

## Batch 1 (the subareas named in the brief)

### F1. Floer homology beyond Maslov (Lagrangian/Hamiltonian spectral invariants)
Seed: read 𝔞_T as the Hessian of an action on the unit sphere of P_T; use Floer/Morse homology of the quadratic Hamiltonian and its
spectral invariants c(α) (Viterbo–Oh) beyond the Maslov grading.
**Lemma F1 (PROVED).** For a closed semibounded quadratic form q on a Hilbert space H with discrete spectrum below the essential
spectrum, the Morse–Floer complex of f(x)=q(x) on the unit sphere S(H) has critical set = unit eigenvectors, critical values =
eigenvalues, and the spectral invariant of the fundamental-type class of degree 0 is c = inf q|_S = λ(q).
*Proof.* df_x = 2(Qx − q(x)x) on T_xS, zero iff Qx = q(x)x; the minimax over the degree-0 class is the infimum (Courant–Fischer). ∎
So every Floer invariant here is spectral data of the target form: (R)(3)/(R)(5); continuation invariance under a homotopy holds
exactly when no eigenvalue crosses 0 = CA_A_008 Lemma 1 (REF-D). Floer *beyond* Maslov adds products/A∞ structure on the same
critical data — a ring of eigenvectors with no order. **DISCARD** (REF-D, (R)(3),(5); Idx: P49-2, CA_A_008).

### F2. Bridgeland stability conditions / mirror symmetry
Seed: a heart 𝒜 and central charge Z with Z(𝒜∖0) ⊂ ℍ∪ℝ_{<0}; the support property gives a quadratic form Q with Q|_{ker Z} < 0.
**Lemma F2 (PROVED, formal).** If a lattice Λ_T with Z: Λ_T → ℂ and quadratic form Q is built so that ker Z ⊗ ℝ = P_T and
Q|_{ker Z} = −𝔞_T, then the support property for (Z,𝒜) is the statement 𝔞_T ≻ 0 on P_T, quantitatively λ_A ≥ c > 0.
*Proof.* Support property ⟺ ∃ Q negative definite on ker Z_ℝ with Q(E) ≥ 0 for semistable E (Bayer–Macrì–Stellari form). ∎
Hence building the stability condition contains the target (REF-D). There is no triangulated category whose K-group realizes
P_T with two Tate classes (ES-20: object unbuilt). Mirror/Gamma-conjecture variant: Γ̂-class ↔ Γ(s/2) is archimedean only
((P3) addendum: archimedean reading insufficient, O7/O8 keep the archimedean part) and Gamma conjecture I is an asymptotic
((B′)). **DISCARD** (REF-D; ES-20; (B′)).

### F3. Condensed / liquid MW-3 (local positivity at every place ⇒ global)
Seed: pass to condensed ℝ- and ℚ_p-vector spaces and liquid tensor products to obtain a Hasse–Minkowski for the window form.
Screen: condensed mathematics changes topology/completion, never order; a cone in a condensed ℚ_p-space has no positivity meaning
(ℚ_p unordered, CA_C_004 D3). The finite-place part of 𝔞_T is not a sum of local forms (Wall A; CA_C_002 Prop 1, class 𝓗 NO-GO).
Any condensed HM statement whose local hypotheses are archimedean-plus-valuation is closed under O6 (a_P keeps every local factor
at p ≥ P and drops the others consistently) ⇒ falsifier a_P fails WP_T on [0.60, ½log P]. **DISCARD** (O6; CA_C_002; (R)(2)).
The index cell "MW-3 condensed variant untried" is now closed: NO-GO (ARGUED) by O6 + ℚ_p unordered.

### F4. Motivic / A¹-homotopy and RO(G)-graded equivariant degrees
Seed: A¹-Brouwer degree / A¹-Euler characteristic in GW(k) (over ℝ its signature is n₊−n₋); C₂-equivariant RO(C₂)-graded degree
for the reflection τ↦−τ (parity of P_T). An integer with sign!
Screen: the signature of 𝔞_T|_{P_T∩V} on finite-dimensional V is n₊−n₋ of the target form; constancy along a path = no eigenvalue
crossing = CA_A_008 Lemma 1 (REF-D). GW(ℚ) classes need a rational form; entries of 𝔞_T are transcendental (log n, ψ-values), and
the rational sub-forms are those of thm:sos (arithmetic squares, class (D)). RO(C₂) grading splits even/odd modes = parity Schur
(thm:parityschur), covered. **DISCARD** (REF-D; Idx P37-2, P49-2, inertia-nogo; thm:sos).

### F5. Hodge–Riemann bilinear relations / Lorentzian polynomials (not AHK)
Seed: P_T is a codimension-2 "primitive" subspace (orthogonal to the two polar directions g₀,g₁); Hodge–Riemann says a form of
known signature on the full space is definite on primitives. Lorentzian polynomials give reverse Cauchy–Schwarz from signature (1,n).
**Lemma F5 (PROVED).** Let q be closed semibounded on H = L²(I_T) ∩ 𝒟, with exactly k negative directions, and P = {g₀,g₁}^⊥.
Then q|_P ≻ 0 ⟺ k ≤ 2 and the 2×2 Schur complement S of q on span{g₀,g₁} relative to P is negative definite on the q-negative part,
i.e. the Hodge–Riemann conclusion is equivalent to a 2×2 condition that already contains λ_A's sign.
*Proof.* Block decomposition H = P ⊕ span(g₀,g₁) (Haynsworth inertia additivity). ∎
This is thm:parityschur / thm:coer-schur and Theorem P (n₋ ≤ 5/7/8): the full-space signature of 𝔞_T is not (2, ∞) at large T,
so a Hodge-index *input* is false and Lorentzian (one negative direction) fails a fortiori. Idx P40-3 (CIRCULAR), NG-62b.
**DISCARD** (retry; Theorem P kills the signature hypothesis).

### F6. Riemannian/spectral geometry: Weyl laws, heat invariants
Seed: realize 𝔞_T as a Schrödinger-type form on I_T and use heat invariants a_k / Weyl asymptotics. Screen: heat trace DEAD
(R164_502); Weyl laws are asymptotic counting ((B′)); heat invariants are local in the symbol ((R)(5) "bounded functional of the
symbol") and comb-generic ((B″)). **DISCARD.**

### F7. Hyperbolic geometry, Selberg-type trace formula, horocycle/Ratner equidistribution
Seed: Euler product as prime geodesic lengths; the Selberg Weil form is positive because Δ is self-adjoint. Exact horocycle integral
∫₀¹E(x+iy,s)dx = y^s + φ(s)y^{1−s}. Screen: self-adjoint mechanism = Hilbert–Pólya family (closed, RH5); horocycle integrals of
Eisenstein data unfold to Rankin–Selberg/Maass–Selberg = CA_A_001/005/006 (abscissa never moves, MW-2); equidistribution *rates*
are estimates (B′). Selberg analogue L31 covered. **DISCARD.**

### F8. Geometric measure theory: calibrations
Seed: a calibration certifies area-minimality by a closed form of comass ≤ 1. Screen: a calibration of the minimization
inf 𝔞_T|_S is a dual feasible point — precisely a (flat-top) dual certificate (Definition def:PD, thm:Z), class (D), admissible only as
final object of a computation already carrying the margin. **DISCARD** (class (D), (R)(3)).

### F9. Derived algebraic geometry / ∞-categorical traces
Seed: categorical (Lefschetz) traces, THH/TC of 𝕊 or ℤ, with 𝔞_T a trace pairing. Screen: positivity in Weil-type settings needs a
polarization (Hodge index on a surface); no object built (ES-20, phase 135/149, T1); TC/THH of ℤ is torsion-heavy, produces integer
or p-adic invariants (unordered, F3/F4). **DISCARD** (ES-20; method theorem T1).

### F10. Tropical / foliations / prismatic / AHK — excluded by brief (scaling site L10/L29, Deninger P42-2, prismatic RH9, AHK P41-2).

## Batch 2 (untouched subareas)

### F11. Cluster categories / cluster algebras (positivity of Laurent phenomenon)
Seed: cluster positivity (Lee–Schiffler; GHKK) gives coefficients ≥ 0 in every cluster. Screen: positivity of Laurent *coefficients*
is a comb-type property (signs of expansion coefficients) — exactly what Λ ≥ 0 already gives and what a_P, O2, O3 keep
(lem:shape-amp/-tail, cor:void). No exchange relation reproduces a window autocorrelation. **DISCARD** (O2/O6; (P3)).

### F12. Symplectic capacities / Gromov non-squeezing on the test space
Seed: the Tate conditions as a coisotropic constraint; a capacity lower bound for the sublevel {𝔞_T ≤ 1}∩P_T. Screen: for quadratic
ellipsoids every normalized capacity = π/λ_min-type data (Ekeland–Hofer of ellipsoids are spectral) ⇒ F1 again. **DISCARD** (REF-D).

### F13. Perfectoid tilting (non-prismatic): ℚ_p ↔ 𝔽_p((t)) as a bridge to function-field positivity
Screen: tilting is local at one p; the global Weil positivity of function fields uses the global surface (Hodge index) which tilting
does not produce; local-at-p data is unordered (F3). Idx: function fields L25 (phase 145/149). **DISCARD.**

### F14. Homogeneous dynamics, exact (not rate) statements: invariance of Haar on SL₂(ℝ)/SL₂(ℤ) under the geodesic flow
Seed: write 𝔞_T(F) as a correlation ⟨ g_T·φ_F, φ_F ⟩ of a lifted vector under the geodesic flow; positivity of matrix coefficients of
a positive-definite function. Screen: matrix coefficients of a unitary rep give Bochner-positive kernels — the class "identities +
Bochner/C–S" (N_018 meta-theorem, prop:opcalc) — and the window form is not one (σ_T(0) = C₀−𝖠 < 0, rem:shape-est). Unitary
lifts of Λ-combs are comb-generic (B″). **DISCARD.**

### F15. Positivity in algebraic geometry: nef/ample cones, Kleiman, Nakai–Moishezon on the "arithmetic square"
Seed: a nef-type criterion D·C ≥ 0 for all curves ⇒ D² ≥ 0. Screen: needs the surface (ES-20); on the scaling-site square the toy
intersection form is real-valued and not integral (P41-1); Nakai is a criterion on a cone of curves, i.e. a dual-cone/certificate
statement (class (D)). **DISCARD.**

## Ranking
No survivor. Batch 1 and 2 cover every subarea named in the brief plus five untouched ones. Recurrent killing clauses:
spectral/REF-D (F1, F2, F4, F12), class (D) (F8, F15), unbuilt object ES-20/T1 (F2, F9, F15), O6/unordered ℚ_p (F3, F13),
Theorem P signature (F5), (B′)/(B″) (F6, F7, F14), O2/O6 comb-type (F11).
Lemmas F1, F2, F5 are PROVED but formal (coordinates); none is a sign step.
