# CA_C_006 — Seed batch 3 (new areas): o-minimality / Pila–Wilkie, free probability, and four others

Phase 193, round 8. Pen and paper. **No sign contact. No negative value for ζ.**
Fixed input from CA_C_005 (NUMÉRICO): the sign of (S) is critical, at margin ≍ M^{−3}, already on the prime-free family η > 2/3. Any
mechanism must therefore decide an exact cancellation of size M^{−3} in O(log M) terms. Screens as in CA_C_000, plus:
**[crit]** does the seed resolve a single eigenvalue at relative precision M^{−3}, or does it only control bulk/averaged quantities?

## E1. o-minimality / Pila–Wilkie counting of near-coincidences
**Seed.** Near_M counts integer triples (m, k, n), m, k ≤ M, with |log(kn/m)| < 2T₀, weighted by Λ(n)c₀. That is, it counts lattice points
near the definable surface {xy/z ∈ (e^{−2T₀}, e^{2T₀})}. Pila–Wilkie bounds the rational points of height ≤ H on the transcendental part of a
definable set by H^ε. Idea: show that the "dangerous" near-coincidences lie on a set with small transcendental part and bound them.
| screen | result |
|---|---|
| Idx | never constructed (G5H-157, R160_M12_R1: "Pila–Wilkie never analysed") ✓ |
| geometry | ✗ the set {xy/z ∈ (a, b)} is **semialgebraic**, so its transcendental part is empty and Pila–Wilkie says nothing. The count of lattice points is volume ≍ M²·T₀ plus a boundary term: a classical count, not a sparsity statement |
| B′ | ✗ Pila–Wilkie gives upper bounds O(H^ε). Any use is an estimate with a remainder, against [crit] precision M^{−3} (lem:shape-est(i)) |
| B″ / O11, O15 | ✗ counts of near-coincidences weighted by a positive comb are comb-generic in sign. With Λ the weights enter only through sums |
| ζ-definability | ζ restricted to a compact set is definable in ℝ_an. Pila–Wilkie on its graph counts algebraic points (Bombieri–Pila type); its content about the line is zero location (R)(4) ✗ |
**DISCARD** (semialgebraic, so the method is vacuous; B′). Index: o-minimal / Pila–Wilkie changes from "never constructed" to "pre-screened
NO-GO as a mechanism: the near-coincidence set is semialgebraic (ARGUED); counting upper bounds are B′".

## E2. Free probability in integer coordinates (Arch against Div)
**Seed.** In the integer basis m ≤ M, with the state τ_M(X) = Σ_m m^{−1}X_{mm}/H(M) (the weight of m^{−½}), ask whether Arch_M and
Div_M + Near_M are asymptotically free. If they were, the spectrum of 𝔸_M would be the free additive convolution of the two limits, which
could be computed.
| screen | result |
|---|---|
| Idx | not in the index ✓ |
| structure | ✗ both are compressions to ℕ ∩ [1, M] of **convolution operators on the same abelian group ℚ_{>0}^×**: Arch by the function d ↦ Arch(d) of the real lag, Div + Near by d ↦ ½Ξ_{F₀}(d) (prop:AM(iii)). On the full group they commute. Free independence of commuting non-scalar elements fails (freeness forces τ((a−τa)(b−τb)(a−τa)(b−τb)) = 0, whereas commuting elements give τ((a−τa)²(b−τb)²) > 0 unless one of them is scalar). Truncation adds a boundary error: [1, M] is not Følner in ℚ^×_+ (the boundary fraction for multiplication by p is 1 − 1/p). It is therefore not small, but it is a one-sided (Toeplitz-type) correction, not a free rotation. ARGUED: asymptotic freeness fails. It is replaced by "commuting modulo Toeplitz boundary terms", the integer analogue of Szegő in window coordinates |
| [crit] | ✗ **decisive even if freeness held**: free probability determines the limiting *spectral distribution* in the state τ_M. The bottom eigenvalue λ_min ≍ M^{−3} is an extreme value with weight O(1/H(M)) in τ_M. A rank-one change of one weight (O5) leaves every limiting moment unchanged and can move the bottom below zero (P46 lem:shape-weight, conditional). So no distributional statement decides the sign (PROVED: rank-one perturbations do not change limiting moments; the falsifier is O5 with its label) |
| (R)(5) | ✗ moments of the empirical spectral distribution are bounded functionals of the symbol |
**DISCARD** (commuting structure; [crit]; O5).

## E3. Ax–Schanuel / transcendence of the log p
**Seed.** Use algebraic independence of log p (Schanuel, or Ax–Schanuel in the functional setting) to show that the Kronecker line is
"generic" in 𝕋^S, so that the line–Haar defect Near_M is controlled.
| screen | result |
|---|---|
| Idx | ✗ F41 (ℚ-linear independence of log p: REF-D); G2_B7 (Haar-null on the twist torus) |
| O11/O15 | ✗ generic positions are shared by Poisson-randomized and Beurling systems, which carry falsifiers |
| [crit] | ✗ genericity is a qualitative or Diophantine-exponent statement, far from M^{−3} |
**DISCARD.**

## E4. Helson / H² of Dirichlet series on the infinite polydisc
**Seed.** Lift Q_M(w) to H²(𝔻^∞) (Bohr lift m ↦ z^{e(m)}). Arch becomes a Toeplitz form with symbol on the Kronecker line, and Div becomes
a multiplier. Use Helson-type inequalities or Carleson measures for H²(𝔻^∞).
| screen | result |
|---|---|
| Idx | ✗ the Bohr torus rows (NT_003/005, G2_B7) and CA_C_002 Prop 2: this is the same line/Haar decomposition |
| B′ | ✗ Helson-type inequalities are norm inequalities with constants: estimates, [crit] fails |
**DISCARD.**

## E5. Real algebraic geometry: a Positivstellensatz on the prime-free family
**Seed.** On η > 2/3, Q_M(w) is an explicit expression in Γ_ℝ, log N and log 2 (CA_C_001 Obs. 1). Seek a sum-of-squares certificate in w.
| screen | result |
|---|---|
| Idx | ✗ G2_B4 SOS / Positivstellensatz (REF-D); (R)(3) squares need a free PD part |
| [crit] | ✗ CA_C_005: the family is critical (M^{−2.9}). An SOS certificate would have to be exact to that precision for every M: class (D) |
**DISCARD.**

## E6. Zero-side identity for the prime-free family (the open sub-question of CA_C_005)
**Seed.** Compute inf_{w∈𝒲_η} Q_M(w) for η > 2/3 through EI_002 Thm 1, Q = (1/π)∫F̂₀²|ζ_w|²Re R_{X′}. Show that the M^{−3} criticality
is produced by ζ_w being small at the low ordinates γ_j, as for the full minimizer (EXP_005 R4).
| screen | result |
|---|---|
| (R)(4) | ✗ as a mechanism it is zero-side by construction (C_zeros) |
| value | as **classification** it is useful: it would show that the critical cancellation on the prime-free family is a zero phenomenon, so no prime-side mechanism on this family exists. This is a NO-GO candidate for the whole s_w direction, not a route |
**DISCARD as a route; KEEP as a classification task** (low cost; next memo if the coordinator wants it).

## Batch-3 result and check
No survivor. E1 is vacuous: the near-coincidence set is semialgebraic, and Pila–Wilkie only acts on transcendental parts. E2 fails
twice: the operators commute up to boundary terms, and spectral distributions are blind to an O(1)-weight-zero extreme eigenvalue. That
second point is the general lesson: **[crit] at M^{−3} excludes every averaged, distributional or counting method**, and CA_C_005 shows
that this holds already on the prime-free family. Check: (a) Is "semialgebraic" right? The defining condition xy/z ∈ (a, b) with
the weight c₀(log(xy/z)) involves exp/log of the ratio only; the set itself is semialgebraic and the weight is a definable function of
one semialgebraic coordinate. Yes, ARGUED. (b) Could free probability with a *different* state (concentrated near the minimizer) help?
A state adapted to the minimizer is the target's own spectral data, (R)(5) / REF-D. (c) No sign contact.
