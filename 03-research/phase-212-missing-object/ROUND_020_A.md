# Round 20, note A — negative index of the archimedean form on P_T for all T

## 0. Four-point filter

1. **Closest antecedent (read in primary sources).** Paper 46 (`04-papers/46-row-d-sign-radial-intersection-form/main.tex`):
   thm:index (l. 2518, exact index on (0, 0.90]), subsec:negindex (l. 2630): prop:NC (l. 2638), cor:P3,
   rem:P4, thm:J (l. 2694), **cor:nasym (l. 2722)**, cor:H1; Paper 48 thm:archcount (l. 182);
   master index, Part VII §1.2 («archimedean negative count n_−(m_T) ≥ N(T) ≈ 4T», PROVED) and entry
   «Archimedean negative index, P46 thm:index/P/J/arena» (PARTIAL, tool PROVED).
2. **New object.** None. The assigned question is **solved in the corpus**; see §1.
3. **Why it avoids the difficulty of the antecedent.** Not applicable: it is a repetition. It stops here, without new derivations.
4. **Connection with global positivity.** This was step P1 of a decomposition (necessary localization),
   not a sign result; no weight enters and the three controls do not apply. The known result
   **refutes P1 as it was drawn** («the sign lives in ≤ 2 directions»).

## 1. What is already proved (CITED, Paper 46)

Notation: m(τ) = Re ψ(¼ + iτ/2) − log π, m(0) = C_0 < 0, m even, increasing on [0,∞), m − C_0 = φ(τ²) with φ
complete Bernstein; τ_0 = 6.28983599… is the only positive zero of m (the negative band of the symbol is |τ| < τ_0).

- **Lower bound (thm:J, PROVED):** n_−(m_T) ≥ ⌈2Tτ_0/π⌉ − 1 on L²(I), and n_−(Arch|P_T) ≥ ⌈2Tτ_0/π⌉ − 3.
  Proof: Dirichlet sines up to frequency < τ_0 plus Jensen on concave φ; P_T removes at most 2.
- **Upper bound (prop:NC, PROVED):** for every τ_1 > τ_0, with θ(τ_1) = m(τ_1)/(m(τ_1) − C_0),
  n_−(Arch|P_T) ≤ n_−(m_T) ≤ #{n : λ_n(S_{T,τ_1}) > θ(τ_1)} ≤ ⌊2Tτ_1/(πθ(τ_1))⌋ (time–band
  limiting operator S_{T,τ_1}).
- **Asymptotics (cor:nasym, PROVED via Landau–Widom, CITED):**
  n_−(Arch|P_T) = (2τ_0/π) T (1 + o(1)) = 4.0042 T (1 + o(1)), likewise for n_−(m_T).
- **Exact values (thm:index, PROVED with verification in interval arithmetic):** n_− = 0 on (0, T*_ev),
  1 on (T*_ev, T*_odd), 2 on (T*_odd, 0.90]; T*_ev ∈ [0.58, 0.60], T*_odd ∈ [log 2, 0.81]; case T = 0.80 open
  in the odd sector (rem:odd080).
- **Explicit bounds (cor:P3):** n_− ≤ 5, 7, 8 at T = ½log3, log2, 0.80. rem:P4: the excess over the true
  value comes from the two-valued minorant and from codim P_T = 2, not from prolate theory (NUMERICAL, not certified).
- By thm:J, n_−(Arch|P_T) ≥ 2 already for T > π/τ_0 ≈ 0.4995… on L²(I) and ≥ 2 on P_T from 2Tτ_0/π > 4,
  i.e. T > 2π/τ_0 = 0.99894; and ≥ 3 from T > 5π/(2τ_0) ≈ 1.2487.

Requested comparison: 2Tτ_0/π − 2 equals 0.20, 0.78, 1.20, 1.60 at T = ½log3, log2, 0.80, 0.90; the
proved values 0, 1, {1,2}, 2 are compatible (the prediction is asymptotic; the ⌈·⌉ of thm:J is the rigorous version).

## 2. Answer

- **n_−(Arch|P_T) is NOT bounded by 2 for all T** (PROVED, thm:J): it grows linearly, with exact
  density 2τ_0/π ≈ 4.004 per unit of T (cor:nasym), half even and half odd (P48 thm:archcount).
- **Correction of P1.** The correct localization is not to ≤ 2 directions but to a negative space of
  dimension (2τ_0/π)T(1+o(1)), described (ARGUED as to the fine description; the dimension is PROVED)
  by the prolate functions of the band |τ| < τ_0 on I, minus the two Tate conditions; the comb must
  cancel all of them, leaving none, on P_T (P48 §2: «exact cancellation counted in directions»). The exact even
  reduction is P48 thm:eveninertia: W^ev ⪰ 0 ∀T ⟺ n_−(A_ev) = 1 ∀T (A_ev = even a_T, without Tate or pole).
- **(L2) in these terms.** The matrix S_{T,k} of size 2k−2 (sec:coer, l. 4876; (L2), l. 10683) is the
  Schur complement of a_T (not of Arch) on the piecewise Tate exponentials, with k ≥ k_0(T) chosen
  so that Arch is coercive on the complement 𝒱_k; by rem:coer-size, 2k−2 grows doubly exponentially in T,
  far above ≈ 4T: it comfortably contains the archimedean negative space, but it is not a prolate basis
  of it. No more precise identification is proved (OPEN).

## 3. What an independent check must rederive

Only the reading: that thm:J, prop:NC and cor:nasym of Paper 46 say what is cited, with the same form Arch = 𝔞_∞ on
P_T (without pole) and the same τ_0. This note proves nothing new. Entry for the index (to be made when
the index is maintained): «P1 ≤ 2 directions: false for T > 2π/τ_0 by P46 thm:J/cor:nasym — repetition, no object».
