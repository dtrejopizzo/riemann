# Round 002 D — Three sign-carrying candidates reverse-engineered from the failure pattern; the comb-null archimedean bottom

Notation of STATEMENT_001. Throughout T > 0 is fixed, D_T := {F ∈ P_T : ∫ log(2+|τ|)|F̂|² dτ < ∞} (a linear subspace on which
a_T is finite), S_T := {F ∈ D_T : ‖F‖ = 1}, and the window form is split as a_T = Arch − Π with

    Arch(F) = (1/2π) ∫ m(τ)|F̂(τ)|² dτ,     Π(F) = Σ_{log n < 2T} v_n Re c_F(log n).

Both are Hermitian forms on D_T; Π is bounded (|c_F(u)| ≤ ‖F‖²), Arch ≥ λ_arch(T)‖F‖² with λ_arch(T) the bottom of the
pure archimedean form on P_T (negative for T ≥ 0.60, Paper 46). For a real parameter c put

    Φ_T(c) := inf_{F ∈ S_T} [Arch(F) − cΠ(F)],   so Φ_T(1) = λ_A(T) and Φ_T(c) = λ_A(T; cΛ).

Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 0. The failure pattern read as a specification

Every recorded failure falls into one of four shapes: (i) an identity valid for every comb (strip identities, Selberg-type
identities, Poisson on ℤ) — returns a dual certificate or the continuous window form; (ii) an estimate with slack — killed by
the margin λ_A/κ_T; (iii) smooth test vectors — reduce to a continuous window form (ROUND_001_A); (iv) a functional in which
the comb enters monotonically — killed by cΛ on one side of c = 1 (ROUND_001_B, BB_001, G11 of the tractability review).
The data point the task singles out is the opposite of (iv): c ↦ Φ_T(c) is concave (CITED, lem:degen), negative at c = 0 for
T ≥ 0.60 and negative again for large c, so the target is a statement about the *location of the top* of a concave curve.
A sign step that escapes (iv) must therefore contain a piece that is homogeneous of degree 0 in the comb (does not see c) and a
piece that pins the scale (sees c, but not monotonically). The three candidates are built to that template.

## 1. Corpus check

Searched: ROUTES-TRIED-INDEX (README, 04_, 05_, 05b_, 06_, SURVEY_MODERN_UNTRIED, AUDIT_PHASE193), phase-211 files, the
tractability review of phase 204 (G11), phase-200 ledger (S2), Paper 46, the corpus for "gcd", "numerical range",
"Toeplitz–Hausdorff", "S-lemma", "joint range", "Schoenberg", "ℓ¹ metric", "Bohr", "log-gamma".

- Concavity of Φ_T in c, monotonicity of Π, D_∃c: in the index (BB_001, CA_R1_001 line "D_∃c", G11: "concavity ⇒ upper
  bounds only", phase-200 S2). What is used there is the concave curve itself; the supergradient gives upper bounds.
- Joint numerical range of (Π, Arch), its convexity, and the comb-null cone {Π = 0}: no entry (grep: "numerical range" occurs
  once, in LITERATURE_001, about a different operator; "S-lemma", "Toeplitz–Hausdorff", "joint range", "comb-null": none).
- gcd kernels: phase 116 (gcd boundary state ⟨V_n e_t, V_m e_t⟩ = (mn/g²)^{−t/2}, used to build a Hilbert completion; an
  identification object, never used as a Schur multiplier on 𝔸_M). Bohr torus / Helson: many entries (NT_003, NT_005, P122,
  AUDIT_193 #26, thm:geo-parity), all through the symbol on the torus; none through the factorization metric as a
  conditionally negative definite kernel.
- Infinitely divisible cones across ∂log: INV_F_001 (only ID cones cross), prop:spec(6) ARGUED.

## 2. Candidate I — the comb-null archimedean bottom and the calibration interval

Definition. W_T := {(Π(F), Arch(F)) : F ∈ S_T} ⊂ ℝ²,  Θ_T := inf{Arch(F) : F ∈ S_T, Π(F) = 0},
J_T := {c ∈ ℝ : Φ_T(c) ≥ 0}.

Statement to prove (★ split). (I.a) Θ_T ≥ 0 for every T; (I.b) 1 ∈ J_T. Theorem 1 below (PROVED) shows that (I.a) is the
statement "some real multiple of the comb is positive at T", that (I.a) ∧ (I.b) is exactly (★) at T, and that J_T is a closed
interval [c_−(T), c_+(T)] (empty iff Θ_T < 0).

Why it implies (★): (I.b) is (★); the point of the split is that (I.a) is a statement in which the comb enters *only through the
quadric cone {Π = 0}* and the sign is carried entirely by the archimedean form m (Γ(s/2) at conductor 1). It is non-linear in Λ
(degree 0: the cone depends on the direction of (v_n), not on its size). (I.b) is the calibration: it is the only place where
the size of the comb (the exact coefficient 1 of ζ, i.e. the exponent 1 in ζ^1, matched with the exponent 1 of Γ(s/2)) enters.

Why it is not in the index (written reason). G11/BB_001 used the concave curve c ↦ Φ_T(c) and its supergradient; the only
outputs are upper bounds on Φ_T. The object here is the dual one: by convexity of the joint range (Toeplitz–Hausdorff) the
*maximum* of the curve is an *infimum of the archimedean form* over a cone. An infimum is a lower-bound statement, which the
concave-curve analysis cannot produce. The difference (joint range instead of the curve) is exactly what reverses the direction
of the inequality that killed G11.

Falsifier mechanism.
(a) cΛ: Θ_T(cΛ) = Θ_T(Λ) for c ≠ 0 (the cone is unchanged), J_T(cΛ) = c^{−1}J_T(Λ). So (I.a) does NOT fail for cΛ (by
    design: it is the degree-0 half) and (I.b) fails for cΛ exactly when c ∉ J_T. Hence the split satisfies the falsifier test
    only as a conjunction; (I.a) alone is not a sign step (it is D_∃c, CITED weaker than (★)). PROVED (Theorem 1(v)).
(b) a_P, P > e^{2T}: Π ≡ 0 on the window, the cone is all of S_T, Θ_T = λ_arch(T) < 0 for T ≥ 0.60. So (I.a) itself fails for
    the empty comb. PROVED. For a_P with P ≤ e^{2T}: OPEN (no explicit window computed).
(c) Beurling systems, (d) finite modifications: the cone {Π = 0} moves (positions log n or weights change); whether (I.a) fails
    is OPEN. ARGUED: (I.a) is a property of the direction of (v_n) only; a finite modification that preserves the direction on
    the window (e.g. a scaling of all weights below e^{2T}) is invisible to (I.a), so (I.a) is at best half of the argument.
Risk: high. (I.a) is weaker than (★) and is c-blind; (I.b) is (★) restated. The gain is structural: the sign of (I.a) is
archimedean, its comb input is a cone. Estimated probability that (I.a) admits a proof that does not prove (★): low but not
nil, because (I.a) fails for the empty comb and for every comb whose cone contains an archimedean-negative vector, a class
that can be attacked with the comb as a *constraint* rather than as a *weight*.

First lemma. Theorem 1 below (attempted and PROVED).

## 3. Candidate II — Schur coupling of the two metrics of ℕ

Definition. On ℕ there are two distances: the archimedean one ρ(m,k) = |log m − log k| (order of ℕ ⊂ ℝ_{>0}, the additive
structure), and the factorization one δ(m,k) = log(lcm(m,k)/gcd(m,k)) = Σ_p |v_p(m) − v_p(k)| log p (the multiplicative
structure; unique factorization = the Euler product). Always ρ ≤ δ, with equality iff one divides the other; near-coincidences
m ≈ kn, m ≠ kn are the pairs with ρ small and δ large. δ is an ℓ¹ metric on the exponent lattice, hence conditionally negative
definite, hence (Schoenberg) 𝕂_t := [e^{−tδ(m,k)}] = [(gcd(m,k)²/(mk))^t] ⪰ 0 for all t > 0 (PROVED: standard; ℓ¹ embeds
in L¹, |x−y| on ℝ is CND, sums of CND kernels are CND). The integer-lattice matrix 𝔸_M = [B(ρ(m,k))] (STATEMENT_001 §2) depends
on ρ only; the comb enters through Div (pairs with ρ = δ = log p^j) and Near (pairs with ρ < δ).

Statement to prove. For some t > 0 and every M, 𝔸_M = 𝕏_M ∘ 𝕂_t + ℝ_M with 𝕏_M ⪰ 0 and ℝ_M ⪰ 0 (Schur product theorem ⇒
𝔸_M ⪰ 0 ⇒ (★) by prop:AM). The natural choice is 𝕏 = 𝔸 ∘ [e^{tδ}] on the Div ∪ diagonal part and the archimedean part of the
near entries, with ℝ collecting the rest.

Why not in the index. Phase 116 used the gcd kernel as a Gram of dilation states (an identification); Bohr-torus routes use
the symbol on Π_p S¹. Here the object is the *comparison* of the CND metric δ with the archimedean metric ρ inside a Schur
factorization. The difference avoids the torus failure (the symbol of the full form vanishes off the zeros, thm:ext-line)
because a Schur factorization is a matrix inequality on ℕ ∩ [1,M], not a statement about a symbol.

Falsifier mechanism (ARGUED). (a) cΛ: Div scales by c while 𝕂_t is fixed; the factorization is tuned to the identity
Σ_{d | m} Λ(d) = log m, which holds only for c = 1, and an exact factorization (no slack) cannot survive a change of c on
the Div entries. (b) a_P: the Div entries for p < P vanish but δ still counts p; the factorization uses e^{tδ} weights at
pairs (m, mp), p < P, whose entries are then purely archimedean and of the wrong size. (c) Beurling: δ exists on the Beurling
integers but there is no inequality ρ ≤ δ with equality on divisor pairs *and* small ρ on non-divisor pairs coming from the
additive structure of ℤ (Beurling integers have no +). (d) Finite modification: changes Div at finitely many ratios, breaking
exactness. Every one of these is an argument that the factorization must be exact; none is a proof that it exists.
Risk: very high. The obvious weights (Schur test with p_m = m^{−1/2}) reduce to row sums Σ_{n | m} Λ(n) = log m, which grow;
that is an absolute-value bound (clause (iv) of prop:spec) and fails. A factorization has to keep signs.
First lemma. Compute, for M ≤ 12 and the profile of STATEMENT_001, whether 𝔸_M ∘ [e^{tδ}] ⪰ 0 for some t > 0 (a
necessary test for the simplest 𝕏), and prove the 2×2 and 3×3 cases {1, p, q} symbolically.

## 4. Candidate III — signed Lévy measure of the completed Euler–Gamma law

Definition. K(u)du on (0,∞) is the Lévy density of log of a Gamma(¼)-type variable (the factor Γ(s/2) at conductor 1):
m(τ) = C_0 + ∫(1 − cos τu)K(u)du is a Lévy–Khintchine exponent (PROVED, lem:K). The comb is a discrete Lévy measure
ν_Λ = Σ v_n δ_{log n}. The window form is the Lévy–Khintchine form of the *signed* measure K du − ν_Λ (cut at 2T) tested on P_T.

Statement to prove. On P_T, the signed measure K du − ν_Λ restricted to (0,2T) is dominated, after Bochner subordination by
the Euler product (ζ(σ+iτ)/ζ(σ) is an ID characteristic function for σ > 1), by a positive-definite part; i.e. an inequality
between the two ID laws at σ ↓ ½, used on the line.

Why not in the index: only partly new. INV_F classified cones crossing ∂log (only ID cones cross); prop:spec(6) is ARGUED.
The difference is that here the two ID laws are compared (subordination), not one cone transported. Risk: very high; ζ^c is ID
for every c > 0, so the law-level statement is c-blind exactly like (I.a), and it carries no mechanism for (I.b). This
candidate is dominated by Candidate I (it is a probabilistic reading of the same degree-0 half) and is recorded only so that it
is not retried as new.

## 5. Choice

Candidate I: it is the only one whose first lemma is a clean theorem, it isolates the c-blind half (where the comb is a
constraint) from the calibration half (where the coefficient 1 enters), and it explains the sweet spot: c*_T is the multiplier
of the constrained archimedean problem.

## 6. Theorem 1 (PROVED). Joint range, comb-null bottom, calibration interval

Assume T > ½ log 2 (for T ≤ ½ log 2 the comb is empty on the window and everything below is trivial).

(i) W_T is convex.
(ii) Π takes both signs on S_T.
(iii) Φ_T is finite, concave, Φ_T(c) → −∞ as |c| → ∞, and max_{c∈ℝ} Φ_T(c) = Θ_T (finite, attained at some c*_T).
(iv) J_T is a closed bounded interval, empty iff Θ_T < 0. In particular (★) at T ⟺ Θ_T ≥ 0 and 1 ∈ J_T, and
     "∃c ∈ ℝ: λ_A(T; cΛ) ≥ 0" ⟺ Θ_T ≥ 0.
(v) For c ≠ 0: Θ_T(cΛ) = Θ_T(Λ), Φ_T^{cΛ}(c') = Φ_T^{Λ}(cc'), J_T(cΛ) = c^{−1}J_T(Λ). For the empty comb (a_P, P > e^{2T}),
    Θ_T = λ_arch(T).

Proof.
(i) Let F_1, F_2 ∈ S_T and V = span(F_1, F_2) ⊂ D_T. If dim V = 1 then F_2 = e^{iθ}F_1 and the two points coincide. If
dim V = 2, choose an orthonormal basis of V; Π and Arch restrict to Hermitian 2×2 matrices P, A, and
{(Π(F), Arch(F)) : F ∈ V, ‖F‖ = 1} = {(⟨Px,x⟩, ⟨Ax,x⟩) : x ∈ ℂ², |x| = 1}, which is the numerical range of P + iA read in
coordinates (Re, Im). By the Toeplitz–Hausdorff theorem (CITED) it is convex; it contains both points, so the segment between
them lies in W_T. (Both forms are finite on D_T, which is all the argument uses; no boundedness of Arch is needed.)

(ii) Since 2T > log 2 pick ε with 0 < ε < min(2T − log 2, log(3/2)) and an interval J ⊂ I_T of length ε with
J + log 2 ⊂ I_T. Pick G ∈ C_c^∞(J), G ≠ 0, with ∫G e^{t/2} = ∫G e^{−t/2} = 0 (two linear conditions on an infinite-dimensional
space). Put F_θ = G + e^{iθ}G(· − log 2). Then A(G(·−log 2)) = √2 A(G) = 0 and B(G(·−log2)) = B(G)/√2 = 0, so F_θ ∈ P_T, and
F_θ is smooth with compact support, so F_θ ∈ D_T. Its autocorrelation is supported in (−ε, ε) ∪ ±(log 2 − ε, log 2 + ε).
The lags log n with log n < 2T in that set: none in (−ε, ε) (log n ≥ log 2 > ε), and in (log 2 − ε, log 2 + ε) only n = 2
(log 3 − log 2 > ε). On (log 2 − ε, log 2 + ε) only the cross term contributes: c_{F_θ}(log 2) = e^{−iθ}·∫G(t)conj G(t) dt
up to the conjugation convention, i.e. c_{F_θ}(log 2) = e^{∓iθ}‖G‖². Hence Π(F_θ) = v_2 ‖G‖² cos θ, and
‖F_θ‖² = 2‖G‖² (the supports of G and its translate are disjoint as ε < log 2). Normalising, Π takes the values ±v_2/2.

(iii) Π is bounded: |Π(F)| ≤ (Σ_{log n<2T} v_n)‖F‖² =: π_T. So Φ_T(c) ≥ λ_arch(T) − |c|π_T > −∞, and Φ_T, an infimum of
affine functions of c, is concave and finite, hence continuous. With F_± ∈ S_T, ±Π(F_±) > 0 from (ii):
Φ_T(c) ≤ Arch(F_±) − cΠ(F_±) → −∞ as c → ±∞. A continuous concave function tending to −∞ at both ends attains its maximum.
Upper bound: if Π(F) = 0, F ∈ S_T, then Φ_T(c) ≤ Arch(F) for every c; so max Φ_T ≤ Θ_T. Note Θ_T < ∞: the segment in W_T
(by (i)) between (Π(F_+), Arch(F_+)) and (Π(F_−), Arch(F_−)) meets {p = 0}; and Θ_T ≥ λ_arch(T) > −∞.
Lower bound: fix θ < Θ_T and let E = {(0, a) : a ≤ θ}. E is convex, and E ∩ W_T = ∅ by definition of Θ_T. Two disjoint
non-empty convex subsets of ℝ² are separated by a line (CITED, finite-dimensional separation theorem): there are (α, β) ≠ 0
and γ with αp + βa ≥ γ on W_T and βa ≤ γ for every a ≤ θ. The second condition forces β ≥ 0 and βθ ≤ γ. If β = 0 then
α ≠ 0 and αp ≥ γ ≥ 0 on W_T, impossible because W_T contains points with p of both signs (ii). Hence β > 0, and with
c := −α/β: a − cp ≥ γ/β ≥ θ on W_T, i.e. Φ_T(c) ≥ θ. As θ < Θ_T is arbitrary, max Φ_T ≥ Θ_T.

(iv) J_T is a superlevel set of a continuous concave function tending to −∞ at both ends: a closed bounded interval,
non-empty iff max Φ_T ≥ 0 iff Θ_T ≥ 0 by (iii). (★) at T is Φ_T(1) ≥ 0, i.e. 1 ∈ J_T, which forces J_T ≠ ∅.

(v) Π^{cΛ} = cΠ, so {Π^{cΛ} = 0} = {Π = 0} (c ≠ 0) and Arch is unchanged: Θ_T(cΛ) = Θ_T. The other two identities are
immediate from Φ^{cΛ}(c') = inf[Arch − c'cΠ]. For the empty comb Π ≡ 0 and Θ_T = inf_{S_T} Arch = λ_arch(T). ∎

Corollary 2 (PROVED). For T ≥ 0.60 and the empty comb, Θ_T < 0: the degree-0 half (I.a) fails for a_P with P > e^{2T}.
For T ≤ ½ log 5, Θ_T ≥ λ_A(T) ≥ 0 (certified positivity, Paper 46). For every T, Θ_T ≥ λ_A(T), with equality iff c*_T = 1
can be chosen.

Corollary 3 (PROVED, the sweet spot made exact). Let c*_T be a maximiser. Then
  (a) Θ_T = Φ_T(c*_T) = inf_{S_T}[Arch − c*_TΠ]: the comb-null problem and the scaled problem at c*_T have the same bottom;
  (b) λ_A(T) = Φ_T(1) ≥ Θ_T − |1 − c*_T|·sup{|Π(F)| : F ∈ S_T} ≥ Θ_T − |1 − c*_T| π_T, since Arch − Π = (Arch − c*Π)
      − (1 − c*)Π.
So (★) at T follows from the two inequalities Θ_T ≥ 0 and |1 − c*_T| ≤ Θ_T/π_T. The second is the calibration; it is a lower
bound statement with an explicit right side. It is far from sharp (π_T grows like e^{T}), so in practice the calibration must
be taken in the form 1 ∈ J_T; but (b) shows that any quantitative control of c*_T near 1 together with a positive Θ_T gives
(★) with an explicit loss, which is the first time the scale of the comb enters a lower bound non-monotonically.

What Corollary 3 says about Π(F*) ≈ 0. If F* ∈ S_T is a minimiser at c = 1 (when it exists) and c*_T ≠ 1, then by concavity
the supergradient −Π(F*) has the sign of c*_T − 1 (CITED lem:degen for the supergradient): Π(F*) > 0 ⟹ c*_T < 1, and
Π(F*) < 0 ⟹ c*_T > 1. Π(F*) = 0 iff (up to the choice of minimiser) c*_T = 1 and then λ_A(T) = Θ_T. So the question "is the
true comb at the top of its scaling curve" is the question "does the minimiser of the window form see zero comb mass". PROVED
under existence of a minimiser; existence is CITED for the form domain used in Paper 46 (compact resolvent part).

## 7. Falsifier test for the sign step of Candidate I

The sign step is the conjunction (I.a) ∧ (I.b).
(a) cΛ: (I.b) fails for c ∉ J_T (Theorem 1(v)), both sides of 1 since J_T is bounded: passes the test as a conjunction. (I.a)
alone survives cΛ and is therefore not a sign step; recorded as such.
(b) a_P, P > e^{2T}: (I.a) fails (Corollary 2). P ≤ e^{2T}: OPEN.
(c) Beurling, (d) finite modifications: OPEN; (I.b) as a statement is (★) for that comb, so the test reduces to the known
falsifiers (finite deletion fails positivity at T > 0.75, thm:finmod). Neither half has been shown to *use* integrality; that
is the missing mechanism and the main risk.

## Result

PROVED piece (Theorem 1, Corollaries 2–3), with the candidate left OPEN.

## What was proved

- Theorem 1 (PROVED): the joint range W_T of (Π, Arch) on P_T is convex; max_c λ_A(T; cΛ) = Θ_T, the infimum of the pure
  archimedean form on the comb-null cone {Π = 0}; J_T = {c : λ_A(T;cΛ) ≥ 0} is a closed bounded interval, non-empty iff
  Θ_T ≥ 0; (★) ⟺ Θ_T ≥ 0 ∧ 1 ∈ J_T; the residue D_∃c is exactly Θ_T ≥ 0; Θ_T is invariant under c ↦ cΛ and equals
  λ_arch(T) < 0 for the empty comb at T ≥ 0.60.
- Corollary 3 (PROVED): λ_A(T) ≥ Θ_T − |1 − c*_T| π_T; Π(F*) = 0 on a minimiser iff the true comb sits at the top of its
  scaling curve, in which case λ_A(T) = Θ_T.
- Candidates II (Schur coupling of the CND factorization metric δ with the archimedean metric ρ) and III (signed Lévy measure)
  defined, with falsifier mechanisms ARGUED; III recorded as dominated by I.

## What failed and why

- (I.a) alone is c-blind (Theorem 1(v)) and therefore cannot be the sign step; it is the degree-0 half of the target, equal to
  D_∃c. Its value is that its sign is archimedean and its comb input is a cone, not a weight.
- Corollary 3(b) loses π_T ≍ Σ v_n (absolute-value size of the comb): as a route it is an estimate with slack and fails for
  T beyond the certified range unless |1 − c*_T| is controlled at the margin scale λ_A/κ_T. No such control is known.
- Candidate II: the natural weighted diagonal dominance reduces to the row sums Σ_{n|m} Λ(n) = log m, which are unbounded;
  any factorization must keep signs. Not attempted beyond that observation.

## Next concrete step

Attack (I.a) as a constrained archimedean problem: compute Θ_T at T = ½ log 5 + ε and at T = 1 by the generalized eigenproblem
Arch F − μΠF = ΘF on S_T (μ = c*_T is its multiplier), record c*_T − 1 against the margin, and test (I.a) on a_P (P ≤ e^{2T})
and on a single finite modification Λ + η1_{n=2}: if Θ_T stays ≥ 0 for those combs, (I.a) is comb-generic beyond scaling and
the candidate closes NO-GO; if it fails, (I.a) is a genuine separator in which the comb enters only as a cone, and the
first lemma to prove is Θ_T ≥ 0 at T = 1 from the archimedean form restricted to the quadric {Σ v_n Re c_F(log n) = 0}.
