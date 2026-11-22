# L2_BUILD_023 — Review (pen and paper)

Checked against Paper 46: A(F)=∫F e^{t/2}, B(F)=∫F e^{−t/2} (l.117), P_T, lem:K (K(u)=2Σ_{k≥0}e^{−(2k+½)u}), eq:Aform / l.4454
(𝔈 = ∫_0^{2T}(c(0)−c(u))K + c(0)∫_{2T}^∞K, comb over log n ≤ 2T), l.4089 (∫c_F e^{u/2} = A·B), and N_BUILD_014 §1–§3.
Premise respected: no use of any equivalence involving row D.

## (1) Lemma L — CONFIRMED (one wording FIX)
- τ_aF(t)=F(t−a): A(τ_aF)=∫F(t−a)e^{t/2}dt = e^{a/2}A(F), B(τ_aF)=e^{−a/2}B(F). Sign/convention correct; primitivity preserved, no Tate correction.
- c_F bilinear, translation-covariant: (ii) correct; supp c₀ ⊂ [−2T₀,2T₀] since supp F₀ ⊂ I_{T₀}.
- (iv) ∫c₀(u−D)e^{±u/2}du = e^{±D/2}∫c₀e^{±v/2} = e^{±D/2}A(F₀)B(F₀) = 0 (evenness of c₀ gives the − sign case). Correct.
- (iii) correct (atoms at log n ≥ log 2 > 2T₀).
- FIX (wording): "F ∈ P_T for every T with I_T ⊃ ∪(a_k + I_{T₀})" — fine; but since 𝔞 depends only on (‖F‖, c_F), one should state
  explicitly that the form is translation invariant, so "F₀" in Theorem T may be the copy centred at −d/2 (as in N_014 review item 1).

## (2) Lemma C — CONFIRMED with constant FIX
- Exponents of K are (2k+½): ½, 5/2, 9/2, … . There is NO e^{−3u/2} term. The k=0 term 2e^{−d/2}∫c₀e^{−v/2} = 0 by L(iv). Correct.
- Only u>0 lags enter (c₀(u+d)=0 for u>0, d>2T₀). Correct.
- Constant: |∫c₀e^{−(2k+½)v}| ≤ ‖c₀‖₁e^{(2k+½)2T₀}, ‖c₀‖₁ ≤ ‖F₀‖₁² ≤ 2T₀. Sum over k≥1:
  ≤ 4T₀ e^{−5(d−2T₀)/2}/(1 − e^{−2(d−2T₀)}). The memo's denominator 1 − e^{−4(d−2T₀)} is WRONG (ratio step is 2, not 4); harmless,
  O(e^{−5d/2+5T₀}) stands. Hypothesis d > 4T₀ more than needed (d > 2T₀ suffices).
- Polar kernel: ∫e^{−|u|/2}e^{iτu}du = 1/(¼+τ²) ✓; cross term κe^{−d/2}∫c₀e^{−v/2} = 0 EXACTLY (for v+d>0). The G_κ claim "up to
  O(e^{−5d/2})" holds only insofar as G_κ = archimedean + polar parts; state which m is used.

## (3) Theorem T — CONFIRMED (novelty DOWNGRADE)
- c_{F₀+sτ_dF₀} = (1+s²)c₀ + s(c₀(·−d)+c₀(·+d)) ✓. Diagonal gives (1+s²)𝔞_{T₀}(F₀) via the freeze identity (∫_0^{2T}+c(0)∫_{2T}^∞ = ∫_0^∞
  when c vanishes beyond 2T₀) ✓. Comb terms at log n ∈ [d−2T₀,d+2T₀] lie inside log n ≤ 2T iff T ≥ T₀ + d/2 ✓ (the window requirement
  is exactly the placement requirement; consistent).
- 2×2 Gram [[a₀, −X/2],[−X/2, a₀]] ⪰ 0 ⟺ |X| ≤ 2a₀ ✓. Two-sided (Ξ) with O(e^{−5d/2}) ✓.
- a₀ = 𝔞_∞(F₀) when 2T₀ < log 2: no comb atoms in (0,2T₀], and the tail term c(0)∫_{2T}^∞K is absorbed as above ✓.
- DOWNGRADE of novelty claim: N_BUILD_014 §3 already writes 𝔞_T(Σx_jτ_{a_j}F₀) = ‖x‖²𝔞(F₀) − Σ_{i≠j}x_ix̄_jX(a_i−a_j); k=2, x=(1,−1)
  gives the lower side. "Strictly stronger than Cor A′" is true of Cor A′ as stated, but the content was implicit in N_014 §3.
  Genuinely new: explicit two-sided statement + O(e^{−5d/2}) error.

## (4) Theorem P — CONFIRMED (constant statement FIX)
- Mean: E X_ν(D) = ∫2ue^{−u/2}c₀(u−D)·κe^u/u du − (det.) = 2κe^{D/2}A B = 0, plus archimedean O(e^{−5D/2}) ✓.
- Variance: ∫(2ue^{−u/2})²c₀²·κe^u/u = 4κ∫u c₀(u−D)² ≥ 4κ(D−2T₀)‖c₀‖₂² ✓.
- Independence: windows [D_k−2T₀, D_k+2T₀] of width 4T₀ with spacing 4T₀ — adjacent windows share endpoints only (null set for a
  Poisson process) ✓. Event {λ_A(T)≥0} ⊂ ∩_k{|X(D_k)| ≤ 2a₀} by Theorem T ✓.
- Esseen: 1−cos x = 2sin²(x/2) ≥ (2/π²)x² on |x|≤π ✓; Gaussian integral √π·π/(√2σ) ✓; sup f needs ‖c₀‖_∞ ≤ ‖F₀‖² = 1 (state it).
  Q is shift-invariant, so the deterministic archimedean part is irrelevant ✓.
- Counting: D_K ≤ 2T−4T₀ ⇒ K ≈ T/(2T₀); Σ_k log D_k = Σ log(4T₀k)+O(K) = K log T(1+o(1)) because 4T₀K ≈ 2T; −½K log T =
  −T log T/(4T₀); K·log C' = O(T) = o(T log T) ✓. Rate exp(−T log T/(4T₀)(1+o(1))) PROVED.
- FIX: "constant → 1/(2 log 2)" as T₀ ↑ ½log 2 is the WORST admissible constant, not a limit to report: 1/(4T₀) grows as T₀ ↓ 0, and the
  T₀-dependence of a₀, ‖c₀‖₂ only enters the O(T/T₀·log(1/T₀)) term. Hence for every c > 0, P(λ_A(T;ν) ≥ 0) ≤ exp(−c T log T) for
  T ≥ T(c) (need a₀(T₀)>0, which holds for small T₀). State it this way (strictly stronger).

## (5) Novelty vs corpus
- L(i), L(iv) at one translate, and the multi-copy kernel: already N_014 §1, §3. New: difference-set support (ii), exact k=0 archimedean
  cancellation (improves N_014's O(e^{−d/2}) to O(e^{−5d/2})), explicit two-sided band, and Theorem P (rigorous superexponential rate
  for Poisson combs). Removal of 022 §3's Tate-correction obstacle: CONFIRMED.
- §5 ζ remarks: correctly labelled identity check / heuristic; no sign contact.

## Verdicts
Lemma L CONFIRMED (+wording FIX); Lemma C CONFIRMED (+constant FIX); Theorem T CONFIRMED, novelty DOWNGRADE (implicit in N_014 §3);
Theorem P CONFIRMED with FIX (rate holds for every c > 0, 1/(2log2) is not the limiting constant). No sign for ζ; no label change.
