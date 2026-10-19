# CA_D_002 — Can Hardy-amplitude transfer reach row D by approximation? NO-GO (phase 193)

Pen and paper; no numerics.
**No negative value of 𝔞_T for ζ is produced or claimed.** Notation is that of CA_D_001.

## 0. Question (seed D9 of CA_D_000)
CA_D_001 proves positivity of ∫Θ′W for every W in the cone
  𝒲_{T,K} := { Σ_i c_i|F̂_i|²Z_T^{2k_i} : c_i ≥ 0 (finite sums), 1 ≤ k_i ≤ K, F_i ∈ P_T^{(k_i)} },
where P_T^{(k)} denotes the real F ∈ C_c^∞(−T,T) with F̂^{(l)}(±i/2) = 0 for l < k. Row D asks for ∫Θ′Φ ≥ 0 for Φ = |F̂|², F ∈ P_T.
If every such Φ were a limit of elements of 𝒲_{T,K}, in any topology in which ∫Θ′· is continuous, row D would follow from CA_D_001.
Corpus check: this is a question about CA_D_001, which is new, so there is no prior entry. The general shape (a cone of proved weights
approximating the constant weight) is close to the certificate/closure theme of P47 §3–6. It differs in that the cone here is a cone of
amplitude-weighted tests, not of dual certificates.

## 1. Theorem 2 (closure obstruction; PROVED, with CITED inputs)
Let T ≥ 1 and K ≥ 1. Let W_j ∈ 𝒲_{T,K} satisfy
  (H1) sup_j ∫W_j dτ < ∞,  (H2) sup_j ∫Θ′W_j dτ < ∞,  (H3) W_j dτ → Φ dτ vaguely, with Φ = |F̂|² for some F ∈ L²(−T,T).
Then F̂(γ) = 0 at the ordinate γ of every zero of ζ on the critical line. Consequently F = 0.
**In words:** no nonzero spectral density of P_T is a vague limit, with bounded mass and bounded window energy, of amplitude-transferred
densities of bounded power. The vague limit is the weakest natural topology for passing the inequality to the limit.

*Proof.*
Step 1 (each term is close to its untransferred density). Write W_j = Σ_i c_iΦ_iZ_T^{2k_i} with Φ_i = |F̂_i|², and set Ψ_j := Σ_i c_iΦ_i.
By Theorem 1′ of CA_D_001 (the even/odd split is understood), the transferred function is ǧ_i = F_i + R_i with R_i supported in [T,∞) and
orthogonal to F_i. So
  (1/2π)∫Φ_iZ_T^{2k_i} = ‖F_i‖² + ρ_i,  ρ_i := ‖R_i‖²,  and  ∫Θ′Φ_iZ_T^{2k_i} = (2π/k_i)∫_T^∞u|R_i|² ≥ (2πT/K)ρ_i.
Moreover |ǧ_i|² − |F̌_i|² = 2Re(F̌_i·conj Ř_i) + |Ř_i|². Hence ∫Φ_i|Z_T^{2k_i} − 1| ≤ 2π(2‖F_i‖√ρ_i + ρ_i).
Summing with weights c_i and applying Cauchy–Schwarz,
  ∫|W_j − Ψ_j| ≤ 2π(2√(A_j B_j) + B_j),  A_j := Σc_i‖F_i‖² ≤ (1/2π)∫W_j,  B_j := Σc_iρ_i ≤ (K/2πT)∫Θ′W_j.
By (H1) and (H2), ε := sup_j ∫|W_j − Ψ_j| < ∞.
Step 2 (domination where the amplitude is small). On U := {τ : Z_T(τ)² < 1}, every k_i ≥ 1 gives Z_T^{2k_i} ≤ Z_T². So W_j ≤ Z_T²Ψ_j
there, and
  Ψ_j − W_j ≥ (1 − Z_T²)Ψ_j ≥ ((1 − Z_T²)/Z_T²)·W_j ≥ 0 on U.
Let ψ := 1_U·(1 − Z_T²)/Z_T², with value +∞ at the zeros of Z_T. Then ∫ψW_j ≤ ∫_U(Ψ_j − W_j) ≤ ε.
Step 3 (lower semicontinuity). ψ ≥ 0 is lower semicontinuous: it is continuous on the open set U with values in [0,∞], and it tends to 0 at
∂U ⊂ {Z_T² = 1}. By (H3) and the portmanteau inequality for vague limits of nonnegative measures against nonnegative lsc functions,
∫ψΦ ≤ liminf ∫ψW_j ≤ ε < ∞.
Step 4 (vanishing at ordinates). Z_T = Z(τ)·e^{−C_X(τ)} has the zeros of Z, with the same multiplicities. Near an ordinate γ of
multiplicity m, ψ ≍ |τ−γ|^{−2m}. Since Φ is continuous (indeed entire), ∫ψΦ < ∞ forces Φ(γ) = 0, so F̂(γ) = 0.
Step 5 (too many zeros). The ordinates of zeros on the line satisfy N₀(R) ≫ R log R (Selberg 1942, CITED). F̂ is entire of exponential
type ≤ T. If F̂ ≢ 0, Jensen's formula gives at most O_F(R) zeros in |z| ≤ R (CITED, e.g. Boas, Entire Functions, §1.2; recentre if
F̂(0) = 0). Hence F̂ ≡ 0. ∎

**Theorem 2′ (quantitative, zero-free version; PROVED).** Under (H1)–(H3), with ε as in Step 1 and η_T := 6.6·e^{−√2B_X},
B_X = Σ_{n<X}Λ(n)n^{−½}/log n:
  ∫_{I_T}Φ dτ ≤ ε·η_T/(1−η_T),  I_T = {|τ| ≤ π/(8T)}.
*Proof.* Z_T² ≤ η_T < 1 on I_T (CA_D_001 §4), so I_T ⊂ U and ψ ≥ (1−η_T)/η_T on I_T. Apply Step 3. ∎
This version uses no zero information. It shows that elements of the closure are doubly-exponentially small on the central Nyquist cell,
which is the cell where the window symbol is negative (σ_T(0) = C₀ − A < 0).

**Corollary 2.1 (single sequence, sharp form; PROVED).** If K = 1 and W_j = |F̂_j|²Z_T² with F_j ∈ P_T, and W_j → |F̂|² in
L¹((1+|Θ′|)dτ) with ‖F‖ = 1 and 𝔞_T(F) = λ, then
  δ_F := (1/2π)∫|F̂|²·|1 − Z_T^{−2}|dτ ≤ √(2λ/T) + λ/(2T).
Equivalently, λ ≥ T·(2δ_F/(√2+√(2+2δ_F)))², which is ≥ 0.34·Tδ_F² for δ_F ≤ 1. Since δ_F = +∞ for every F ≠ 0 (Steps 4–5), the hypothesis
is never met, and the inequality is vacuous for ζ.
*Proof.* Step 1 with A_j → 1 and limsup B_j ≤ λ/(2T). Then use Fatou along an a.e.-convergent subsequence, on which
|F̂_j|² = W_j/Z_T² → Φ/Z_T². ∎

## 2. What the NO-GO says about the sign (structure)
1. **The class excluded.** Any deduction of row D that proves positivity for amplitude-weighted tests F̂·Z_X^k, with k ≥ 1 and the
   amplitude belonging to the test, and then passes to amplitude one by approximation. By Theorem 2, the passage is impossible for every
   nonzero test: not only for minimizers, and not only at small λ. The obstruction is not quantitative. Every transferred density vanishes
   at every on-line ordinate, at a rate that no bounded-energy limit can undo.
2. **Where the sign must be produced.** Theorem 2′ locates the deficiency on the central cell I_T and, through Step 4, at the ordinates.
   These are the two places where |ζ/Z_{<X}| < 1. CA_D_001 proves the sign where the Hardy amplitude is large, at no cost. Row D asks for
   it with amplitude one. The difference is supported on {Z_T² < 1}. **In the phase picture, row D is a statement about the unimodular
   factor e^{−iΘ} = Z_X/Z_T alone.** Its spectral measure is two-sided, so no support argument applies to it.
3. **Consistency with the falsifiers.** Theorem 1″ holds for DH, Epstein and ζ_K. Theorem 2 also holds for them, provided they have
   infinitely many on-line zeros with superlinear counting (Theorem 2′ needs nothing). So the dichotomy "positive with Hardy amplitude, open
   with amplitude one" is common to the whole FE class. The ζ-specific information must enter in the amplitude-one regime, on {Z_T² < 1}.
   This matches thm:shape(C) and (R)(7) (exactness at the centre).
4. **Possible use.** A proof might still use CA_D_001 for the part of a test whose spectral mass lies in {Z_T² ≥ 1}. It would then need a
   separate argument on {Z_T² < 1}, which is the region of the central cell and of the ordinates. That residual is not weaker than row D
   on tests concentrated there. No reduction is claimed: the split is by a non-polynomial multiplier, which does not preserve P_T.

## 3. Review (own)
1. *Vague versus weak convergence.* Steps 3–4 need only vague convergence and ψ ≥ 0 lsc. (H1) prevents mass escaping in a way that
   matters, but it is not even needed for Step 3. (H1) and (H2) are used only to make ε finite. ✓
2. *Is (H2) natural?* Passing ∫Θ′W_j → ∫Θ′Φ to the limit requires at least boundedness. ✓ Without (H2), ε could be infinite and the
   theorem says nothing. That case would mean the transferred energies diverge, which cannot give a finite limit inequality anyway.
3. *Lower semicontinuity at ∂U.* At points where Z_T² = 1, ψ → 0 from inside U and ψ = 0 outside, so ψ is continuous there. ✓ At
   zeros, ψ = +∞ is the limit, so ψ is continuous as an extended-valued function. ✓
4. *Step 1 for k ≥ 2.* It uses the k-th order Tate condition of Theorem 1′. The orthogonality F ⊥ R^{(k)} uses supp R^{(k)} ⊂ [T,∞). ✓
5. *Step 5 citations.* Selberg's positive proportion gives N₀(R) ≍ R log R. Even "N₀(R)/R → ∞" suffices against exponential type. Jensen:
   n(r) ≤ log(M(er)/|f(0)|) ≤ eTr + O(log r) for type T. ✓ Zero information is used **only in a NO-GO about a route**, never toward row D.
   (R)(4) concerns proofs of D. Theorem 2′ avoids zeros completely.
6. *Could a different amplitude escape?* The class is "amplitude = |Z_X|^k" (CA_D_001). Other amplitudes with the same phase and a
   one-sided spectrum: |Z_X·V| with V/Z_X... Any G = e^{−iΘ}·A with spectrum split as in CA_D_001 is the boundary value of a function
   holomorphic on Re s > ½. Dividing by Z_X gives V := G/(F̂Z_X), real-positive on the line. Removing the zeros of Z_X from V would need
   poles of even order at simple on-line zeros, which is impossible for a real-positive ratio. This is ARGUED (CA_D_000 analysis), not
   PROVED in full generality. Recorded as OPEN: "classify all amplitudes A ≥ 0 such that A·e^{−iΘ}F̂ has the CA_D_001 support split".
7. *Overclaim check.* Theorem 2 is a NO-GO for a route. It is not a statement about λ_A, and it moves no clause of (R).

## 4. Synthesis of the round (seeds D1–D9; memos CA_D_001–002)
| item | label |
|---|---|
| Theorem 1 (𝔞^{Z}_T(F) = 2∫_T^∞u\|R_F\|² ≥ 2Tρ_F ≥ 0 on P_T), Cor 1.1, Thm 1′ (powers k) | PROVED |
| Theorem 1″ (same for every FE Dirichlet series with at most a simple pole at 1: DH, Epstein, ζ_K) | PROVED |
| Lead (a): positivity of z_X is never used; the gap {1<n<X} is the operative fact, and it holds for every comb | PROVED (observation) |
| Theorem 2 (vague closure of the transferred cone ∩ P_T-densities = {0}) | PROVED (Selberg, Jensen CITED) |
| Theorem 2′ (zero-free: closure elements ≤ ε·η_T on the central cell, η_T ≈ e^{−√2B_X}) | PROVED |
| Route "row D by approximation from Hardy-amplitude positivity" | **NO-GO (PROVED)** |
| Route "Landau/positive-coefficient phase inequality on Z_X" | DEAD (retry of R164_102 W-Landau) |
| D1, D4–D8 | DISCARDED at pre-screen (coordinate / zero information / retry) |
| OPEN | classification of admissible amplitudes (§3.6); a ζ-specific statement on {Z_T² < 1} with amplitude one |
**Insight recorded (for the ledger and the index).** In the phase picture 𝔞_T(F) = (1/π)∫Θ′|F̂|², the sign is free when the test carries the
Hardy amplitude |ζ/Z_{<X}|. The Euler gap and the Tate condition then push all non-window spectrum to u ≥ T, where the phase velocity is at
least T. Row D is the amplitude-one statement. It differs from the free one exactly on {|ζ/Z_{<X}| < 1}: the central Nyquist cell, where
the comb is coherent, and the on-line ordinates. No limit of amplitude-weighted tests can reach it (Theorem 2). A proof must handle the
unimodular phase factor e^{−iΘ} directly on that set, with a property that separates ζ from the FE class.
No sign contact. No certified negative value for ζ. No YES→NO move proposed for the clauses of (R).
