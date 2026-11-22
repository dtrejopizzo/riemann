# R162_1701 — Target R-C made precise: Type I ⟺ complete-form contact, nodal exclusion of Type I, residue window

Pure mathematics, no numerics run. The float data cited are R162_1601 (UNCERTIFIED).
Inputs: R162_1501 §5 (R-C), R162_1601, R162_504 Thms 1–3, R162_703 Thm 4.2 with the R162_990 fixes, R162_902,
Paper 46 thm:parityschur (o),(a3),(b),(c), lem:contA, lem:contT, lem:monoT, cor:convfail.

**Status.**
- §1 Theorem 1 (what "Type I" means across windows): **PROVED**, by assembling results from the corpus. The literal
  "Type I ⟺ T_W = T_*" is **false** as stated. The correct form is T_W = T_* ⟺ [every contact vector is Type I] ∧
  [𝔊_{T_*} ⪰ 0].
- §2 Lemma C (Chebyshev orthogonality) and Theorem 3 (conditional nodal exclusion of Type I): **PROVED**, conditional
  on two hypotheses (C2) and (N2). Proposition 4 (for the archimedean operator, (C2) holds in the even sector and the odd
  sector is positivity improving on (0,T)): **PROVED**. Proposition 5 (ζ's near-Type-I behaviour comes from Perron–Tate
  alignment): **PROVED**. The same argument gives an exact formula for the Type I margin (Proposition 6).
- (N2), a Courant bound for the second even eigenfunction, is **OPEN**, and there is no general tool for it (NO-GO for the
  standard routes, §2.4). (C2) is **OPEN** once the comb is present, because the Riesz rearrangement fails for the
  comb.
- §3 Residue window (Theorem 7): **PROVED**. It restates R162_902 with the residue as a free parameter. R-C.a is
  equivalent to "1 ∈ [κ₋(T), κ₊(T)] for all T < T_*". This makes precise the idea "PNT main term = rank-one term".
  **NO-GO** as a weakening: once R-C.b is proved, R-C.a is equivalent to RH (E1).

No sign is claimed. No label moves. Gate 1 stays OPEN.

Conventions:
- T_* := inf{T : λ_A(T) ≤ 0}. This is fix (b) of R162_990 for 703 Thm 4.2(3), so λ_A > 0 on (0, T_*).
- T_W := inf{λ_W < 0}.
- 𝔞_par(T) := min{a_T(F) : F ∈ D_T^par, ℓ_par(F) = 1}, the primitive polar energy (thm:parityschur(a3)). It is defined
  whenever λ_par(T) > 0. g_par = 𝔞_par + 2ε_par.

## 1. Type I versus T_W = T_* — PROVED

**Theorem 1.** Assume ¬RH, so that T_* < ∞. Then:
1. T_W ≤ T_*.
2. T_W = T_* ⟺ λ_W(T_*) ≥ 0 ⟺ g_ev(T) ≥ 0 and g_odd(T) ≥ 0 for all T < T_*.
3. T_W = T_* ⟺ (range condition α ≡ 0 on 𝒩 in each sector with λ_par(T_*) = 0) ∧ 𝔊_{T_*} ⪰ 0.
   By the definition in thm:parityschur(b), α ≡ 0 on 𝒩 says exactly that every contact vector is Type I (r = 0).
4. The equivalence "Type I ⟺ T_W = T_*" holds only in the direction ⟸. A Type I contact at T_* can coexist with an
   earlier polar contact T_W < T_*. In that case λ_W(T_*) < 0 comes entirely from g_par(T_*) < 0 on 𝒩^⊥.

*Proof.*
- (1) λ_W ≤ λ_A.
- (2) λ_W is continuous (lem:contT) and nonincreasing (lem:monoT). So T_W ≥ T_* ⟺ λ_W ≥ 0 on (0, T_*] ⟺ λ_W(T_*) ≥ 0.
  On (0, T_*) we have λ_A > 0. There thm:parityschur(c) gives λ_W(T) ≥ 0 ⟺ g_ev(T), g_odd(T) ≥ 0. The functions g_par
  are nonincreasing (703 Lemma 2.1), and λ_W is continuous at T_*.
- (3) At T_*, λ_A(T_*) = 0 (lem:contA), so WP_{T_*} holds. Apply the second equivalence of thm:parityschur(c).
  If the range condition holds, the residue r = α(F)φ vanishes for every F ∈ 𝒩 (R162_504 Thm 3).
- (4) (3) has two independent clauses, and a Type I contact supplies only the first. ∎

**Reading.** R-C splits RH as follows. Under ¬RH, one of two things happens:
- **(R-C.a fails)**: a polar contact at T_W < T_*. At T_W, λ_A > 0, some g_par(T_W) = 0, and the radical is ℝh_par ⊄ P.
- **(R-C.b fails)**: T_W = T_*, and every first-contact vector is Type I:
  - A F = 0 and F ⊥ φ_par;
  - even sector: F ⊥ ψ_T, and 0 = μ₂^ev(T_*) (from μ₁ < λ_ev = 0 ≤ μ₂^ev, R162_504 Thm 2(b), together with 0 being an
    eigenvalue ≠ μ₁);
  - odd sector: 0 = μ_k^odd.
  By min-max, μ₂^ev(T) is nonincreasing in T, so μ₂^ev > 0 on (0, T_*) and reaches 0 exactly at T_*.

So **RH ⟸ R-C.a ∧ R-C.b**, where
- R-C.a: λ_W(T_*) ≥ 0, i.e. no polar contact strictly before T_*;
- R-C.b: no Type I first contact.

Under RH both hold vacuously. The float data fit this dichotomy. ζ's near-null branch is asymptotically Type I (r/λ ≈ 0.93),
the regime of an (I₀)-type contact. Deletion is Type II with T_W ≤ 0.4608 < T_c = 0.5958, which is regime (P).
(C1) is the approach version of "Type I at T_*". If r_T → 0 along the branch, the limit contact is Type I. The rate O(λ)
is not needed for Theorem 1, and it is not proved here.

## 2. R-C.b: Type I contacts and sign changes

### 2.1 Lemma C (Chebyshev orthogonality) — PROVED

Let u₁ > 0 and u₂ > 0 be continuous on (0,T), with u₁/u₂ strictly monotone. Let 0 ≠ F ∈ L²(0,T) satisfy
⟨F,u₁⟩ = ⟨F,u₂⟩ = 0. Then F has at least 2 sign changes on (0,T).

*Proof.*
- F cannot have 0 sign changes, because it is orthogonal to u₁ > 0.
- Suppose F has exactly one sign change, at t₀. Put c = u₁(t₀)/u₂(t₀).
- Then u₁ − c u₂ = u₂(u₁/u₂ − c) has exactly one strict sign change, also at t₀. Replacing c by −c if necessary, it has
  the same sign pattern as F.
- So ∫F(u₁ − c u₂) = ∫|F||u₁ − c u₂| > 0. This contradicts orthogonality. ∎

### 2.2 Theorem 3 (conditional exclusion of Type I) — PROVED given (C2), (N2)

Hypotheses at a window T:
- (C2) ψ_T/cosh(t/2) is strictly monotone on (0,T).
- (N2) every nonzero even vector in E₂ := ker(A^ev − μ₂^ev) has at most one sign change on (0,T). Equivalently, S ≤ 2
  on I_T. This is the Courant bound for the second even eigenvalue.

Then E₂ ∩ ker ℓ_ev = {0}. In particular:
- there is no even Type I first contact at T;
- μ₂^ev is simple.

If T = T_* and T_W = T_*, the first contact is therefore odd.

*Proof.*
- Let F ∈ E₂ ∩ ker ℓ_ev. Then F ⊥ ψ_T by the spectral theorem, and F ⊥ cosh(t/2).
- Restrict to (0,T); both functions are even. Lemma C with u₁ = ψ_T > 0 (R162_504 Thm 1) and u₂ = cosh gives at least 2
  sign changes on (0,T). This contradicts (N2).
- Simplicity: if dim E₂ ≥ 2, some nonzero combination lies in ker ℓ_ev.
- The last claim follows from Theorem 1(3): an even contact at T_* would have to be Type I. ∎

**Odd version (same proof).** Hypotheses:
- (P-odd) the odd sector is positivity improving on (0,T), so the odd ground state ψ₁^odd > 0 on (0,T) is simple;
- (C2-odd) ψ₁^odd/sinh(t/2) is strictly monotone;
- (N2-odd) the second odd eigenvector has one sign change on (0,T).

Under these, an odd Type I vector F must satisfy F ⊥ ψ₁^odd:
- 0 = μ₁^odd with F ∈ ker ℓ_odd would contradict ψ₁^odd > 0 and sinh > 0;
- so 0 = μ_k^odd with k ≥ 2.

Lemma C then gives S_{(0,T)}(F) ≥ 2, so S(F) ≥ 5 on I_T (the zero at 0 counts). This contradicts (N2-odd).
This is the "S ≥ 5" of the task.

### 2.3 What is actually proved about (C2), (P-odd) — PROVED for the archimedean operator

Recall k(u) = e^{−|u|/2}/(1−e^{−2|u|}) = Σ_{j≥0} e^{−(2j+½)|u|}. It is completely monotone, and strictly decreasing
in |u|.

**Proposition 4.** Let Γ_T be the archimedean part of a_T, i.e. v ≡ 0. This is the deletion model Λ1_{n≥N} for
T < ½log N.
- (a) The ground state ψ_T of Γ_T is symmetric decreasing. Hence (C2) holds: ψ/cosh is strictly decreasing, because
  ψ > 0 is nonincreasing and cosh(t/2) is strictly increasing on (0,T).
- (b) For odd F, write F on (0,T). Then Γ_T(F) = m(0)‖F‖² + ∬_{(0,T)²}(F(t)−F(s))²J(t,s) + ∫V F², where
  J(t,s) = k(t−s) − k(t+s) > 0 and V(t) = 4∫_t^∞ k ≥ 0. So (P-odd) holds and ψ₁^odd > 0 on (0,T).

*Proof.*
- (a) Almgren–Lieb (J. AMS 2 (1989), Thm 9.2; CITED, statement to be checked against the source) says:
  ∬(F*(t)−F*(s))²k(t−s) ≤ ∬(F(t)−F(s))²k(t−s) for symmetric decreasing k and F ≥ 0 vanishing at infinity.
  The rearrangement preserves ‖F‖ and support ⊂ I_T. So |ψ|* is a ground state. By simplicity (504 Thm 1),
  ψ = |ψ|*.
- (b) For odd F, split R² into quadrants and use
  (F(t)+F(s))² = 2F(t)² + 2F(s)² − (F(t)−F(s))².
  The kernel J is positive because k is strictly decreasing on (0,∞). Replacing F by |F| on (0,T) lowers the J-term
  and leaves the V-term unchanged. The rest is the argument of 504 Thm 1 (iii)–(iv). ∎

**The comb breaks both parts.**
- Even sector: the comb term −v_n c_F(log n) has a point kernel δ(t−s∓log n). This kernel is not symmetric decreasing,
  so Riesz / Almgren–Lieb does not apply. With the comb present, ψ_T is not known to be monotone, and (C2) is OPEN. The
  R162_1501 float test was inconclusive.
- Odd sector: the reflected comb term contains +v_n F(t)F(s)δ(t+s−log n), which has the wrong sign for positivity. It is
  active as soon as log n < 2T. So (P-odd) is OPEN at every T_* > ½log5.

### 2.4 (N2) — OPEN, and the standard routes are NO-GO

- **Courant's theorem** is a statement about local operators. For symmetric matrices with nonpositive off-diagonal entries,
  the discrete nodal theorems (Davies–Gladwell–Leydold–Stadler 2001) count nodal domains in the **graph** sense. Here
  k > 0 everywhere, so the graph is complete. Then every function has at most 2 graph-nodal domains, and the bound says
  nothing about sign changes on the line.
- **Total positivity / Karlin** would give Sturm counts. This route is CLOSED (R155_046 N3).
- For subordinate Brownian motion on an interval, which is the class of Γ_T since k is completely monotone, sign-change
  counts are known only in special cases. The results we know are about symmetry of the second eigenfunction (e.g.
  Bañuelos–Kulczycki for the Cauchy process; CITED from memory, to be checked). We know of no result on the nodal count of
  the second **even** eigenfunction.
- Conclusion: (N2) is a genuine new analytic statement even for Γ_T. It is weight-blind within a ≥ 0 (see §4).

### 2.5 Why ζ looks almost Type I — PROVED

**Proposition 5.** Let c_T = ⟨ψ_T, φ̂⟩, where φ̂ = φ_ev/‖φ_ev‖. For every unit even F ⊥ ψ_T, in particular F = u₂:

  |⟨F, φ̂⟩| ≤ (1 − c_T²)^{1/2}.

*Proof.* Write φ̂ = c_Tψ + (1−c_T²)^{1/2}w with w ⊥ ψ a unit vector, and apply Cauchy–Schwarz. ∎

- As c_T → 1, the second eigenvector becomes Tate-orthogonal, so it is asymptotically Type I.
- The alignment c_T → 1 is the Perron form of the PNT main term (R162_504 §5(i), R162_902 §2): the rank-one term
  2φφ* dominates, with |μ₁| ≍ e^T.
- This accounts for the (C1) observation in R162_1601 (the bottom branch = u₂, r/λ ≈ 0.93) without any zero-side
  input.

**Proposition 6 (exact Type I margin).** Assume (C2) and (N2). Let u₂ change sign at t₀ and put c = ψ(t₀)/cosh(t₀/2).
Then

  ⟨u₂, cosh(t/2)⟩_{(0,T)} = −(1/c) ∫_0^T |u₂| · |ψ_T − c·cosh(t/2)| dt ≠ 0

(for the sign choice u₂ > 0 on (0,t₀)).

- The margin that separates ζ from an exact Type I contact is therefore the L¹-distance, weighted by |u₂|, from ψ_T to
  the pole vector line.
- It is small exactly when Perron–Tate alignment is good, which is consistent with Theorem M.
- For the exclusion itself it only has to be nonzero, not large. So Theorem M does **not** kill R-C.b, unlike the
  quantitative alignment route (504 Prop 4.3).

## 3. R-C.a: the polar contact and the residue window

Treat the residue κ of the pole as a free parameter: W^κ := a_T + 2κ AB. Then:
- the even sector reads W^κ = a + 2κℓ_ev²;
- the odd sector reads W^κ = a − 2κℓ_odd²;
- the primitive form a_T, and hence T_*, 𝒩 and Type I/II, do **not** depend on κ.

**Theorem 7 (residue window) — PROVED** (a restatement of R162_902 §§1–2 and 703 Thm 2.2).
For T < T_* define κ₋(T) := −𝔞_ev(T)/2 and κ₊(T) := 𝔞_odd(T)/2. Then:
1. κ₋ is nondecreasing and κ₊ is nonincreasing. The windows [κ₋(T), κ₊(T)] are nested and shrink as T grows.
2. λ_W^κ(T) ≥ 0 ⟺ κ₋(T) ≤ κ ≤ κ₊(T). Hence **R-C.a ⟺ κ₋(T) ≤ 1 ≤ κ₊(T) for all T < T_***, i.e. the true residue
   1 never leaves the window.
3. A polar contact at T_W is the first exit of κ = 1:
   - through κ₊ (odd; the pole is too strong for the primitive odd energy), or
   - through κ₋ (even; the primitive even energy on the Tate slice is below −2).
   In resolvent form, f_odd(0) = 1/(2κ) or f_ev(0) = −1/(2κ) (Sherman–Morrison, 902 §3).
4. If T_* = ∞: lim κ₊ ≤ 1 ≤ lim κ₋, unconditionally (902 Thm 2.1, which uses only ζ ≠ 0 on Re s = 1). So
   ∩_T[κ₋, κ₊] ⊂ {1}, and RH ⟺ ∩_T[κ₋, κ₊] = {1}.

*Proof.*
- (1) 𝔞_par is nonincreasing, by the argument of 703 Lemma 2.1 at κ = 0.
- (2) Apply thm:parityschur(c) with λ_A > 0 and g_par = 𝔞_par + 2ε_par κ.
- (3) Continuity.
- (4) 902 Thm 2.1 with κ = 1, and g̃ = g on {λ_par > 0}. ∎

**The property of ζ that R-C.a encodes.** Unfold 𝔞_par = Γ − Σ v_n c_F(log n) on pole-normalised tests. For odd tests
increasing on (0,T), c_F(log n) < 0 at large shifts, so the comb adds odd energy. Then:
- κ₊ ≥ 1 is a **weighted Chebyshev lower bound**: "the primes up to e^{2T} pay for the residue on every odd
  pole-normalised test";
- κ₋ ≤ 1 is the matching **weighted upper bound** on even tests.

So R-C.a is a two-sided, scale-by-scale PNT statement, "residue = prime density", read against the archimedean capacity.
This is the precise sense in which the rank-one φφ* term is the PNT main term (R162_902 §2).

**Why deletion fails.** Take a = Λ1_{n≥5}. It keeps residue 1 but ψ_del(x) = 0 for x < 5.
- For T < ½log5 the odd capacity is purely archimedean.
- By cor:convfail, κ₊(T) < 1 already on [0.4608, 0.58], so 1 exits through κ₊.
- For ζ, the contacts n = 2, 3, 4 enter at T = ½log n = 0.347, 0.549, 0.693. They add odd energy, and this is exactly
  what the certified λ_W(½log5) > 0 (703 Thm 3.1) records.

**NO-GO (as a weakening).**
- Theorem 7(4) shows that the unconditional input (PNT) pins the window's limit from the wrong side.
- If R-C.b holds, then Theorem 1 gives R-C.a ⟺ RH. All the arithmetic of R-C therefore sits in R-C.a, and R-C.a is then
  E1. What R-C.b offers is to remove Type I, leaving "RH ⟺ no polar contact": the global D3 converse, which is the
  statement 703 §4 already identified as the controlling one.

## 4. Falsifier lines

- **R-C.b, weight-blind.** (C2), (N2) and Theorem 3 only use a ≥ 0. They are therefore allowed to hold for deletion and
  for amplification a = sΛ, and they must do so: R-C.b is meant to be structural.
  - Test: in the two-parameter family (T, s) with a = sΛ, a codimension-two event {μ₂^ev = 0, ⟨u₂, φ_ev⟩ = 0} is
    generically isolated, so it is not excluded by counting.
  - Theorem 3 predicts that ⟨u₂, φ_ev⟩ has **constant sign** on {μ₂^ev = 0} for every s.
  - If the sign changes for some s, then an a ≥ 0 model has an even Type I first contact (provided λ_ev > 0 before).
    In that case (N2) or (C2) is false for a ≥ 0, and R-C.b must be arithmetic.
  - Declared, not run (rule: numerics only if necessary).
- **R-C.b and DH.** DH has no pole, so there is no φ-constraint (P_T is everything) and no Perron positivity. Theorem 3 has
  no content there, which is consistent with DH's off-line zeros. The mechanism uses the pole twice: in cosh as the
  second Chebyshev function, and in Perron (v_n ≥ 0).
- **R-C.a.** Any proof must:
  - fail for deletion, i.e. use small primes 2 and 3 at their thresholds;
  - fail for κ-models with κ = 1 ± δ, which exit the window at large T (Theorem 7(4)); so it must know the residue
    exactly;
  - fail for Beurling systems with ψ(x) = x + O(x^θ) and off-line zeros (Diamond–Montgomery–Vorhauer); so a Chebyshev
    bound with a power error cannot suffice, and integrality must enter.
  No mechanism satisfying all three is known (cf. R162_1001: the torsion cocycle is the only object that fails for
  Beurling).

## 5. For R162_590 and the README

- 1701 Theorem 1: T_W = T_* ⟺ (Type I) ∧ (𝔊_{T_*} ⪰ 0). "Type I ⟺ T_W = T_*" is false (only ⟸).
- R-C.b reduces to (C2) + (N2), with Lemma C and Theorem 3 PROVED.
  - (C2) is PROVED for the archimedean operator (Almgren–Lieb) and OPEN with the comb.
  - (N2), a nonlocal Courant bound for the second even eigenfunction, is OPEN. Graph nodal theorems are vacuous here
    and Karlin is closed.
- Proposition 5: ζ's near-Type-I behaviour = Perron–Tate alignment, |⟨u₂, φ̂⟩| ≤ √(1−c_T²).
- Proposition 6: the exact Type I margin is not killed by Theorem M.
- Residue window [κ₋, κ₊] (Theorem 7): R-C.a ⟺ 1 ∈ window for all T < T_*. This is a two-sided weighted PNT at every
  scale. Deletion exits through κ₊ at 0.4608. It is E1 once R-C.b is proved. NO-GO as a weakening.
- Open: (O1701.1) (N2) for Γ_T; (O1701.2) (C2) with the comb; (O1701.3) the sign test of ⟨u₂, φ⟩ in the family (T, s).
