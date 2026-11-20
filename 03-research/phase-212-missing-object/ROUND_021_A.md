# Round 21, memo A — The near-radical family `{Π_T(M∗φ)}`: count and structural statement

Note of computation and structure. It is not a sign attempt. Notation of round 7:
`a_T(F) = Arch(F) − Σ_n v_n c_F(log n)` on `P_T = {∫F e^{±t/2} = 0}`; `W_*` the global form (P46 §11);
`K_Pó` the Pólya kernel, `M = −K_Pó″ + ¼K_Pó`, `Φ_M(s) = s(1−s)ξ(s)`; `X_T` as in `R160_M4_R1.md` and `ROUND_019_A.md`.

## Four-point filter (cross-check first)

1. **Antecedents, read in primary sources.**
   - `phase-106-global-modular-star-audit/106_09_NEAR_RADICAL_CLUSTER_AND_GAP_COLLAPSE.md`: Lemma 1 (weighted
     continuity of the full form on `𝒳_b`), §3 (smooth truncations `χ_aK^{(j)}`, matrix `O(λ^Me^{−cλ²})`),
     end of §4: «any fixed finite collection of derivatives puts each fixed number of eigenvalues in a
     near-null cluster»; §5: selection within the cluster is the problem.
   - `phase-160-row-d-infinite-T/R160_M4_R1.md`: Theorem B(i) (`λ_A ≤ Ce^{cT}e^{−2πe^{2T}}`), Observation C1
     (`Q(∂)τ_bK_Pó` in the radical, exact rate `π`), Theorem D and its reading (the constraint bites up to
     height `≈ 4e^{2T}`).
   - `phase-204-refd-tractability/P2_SCHUR_001.md`: `𝒜 = span{(ζP)(∂)g} ⊂ rad 𝒲`, `𝒲_AA ≡ 0`, `𝒲_AB ≡ 0`,
     Haynsworth `In(𝒲) = (0,0,dim 𝒜) + In(𝒲_BB)`, Lemma P2-S.3 (a useful Schur needs a block outside the radical).
   - `phase-211-sign-sandbox/ROUND_006_A.md` Theorem 5 and `ROUND_006_C.md` (P211-6C): UPPER bound
     `m_δ(T) ≤ exp(2e^T(1+o(1)))`; `ROUND_005_B.md` (P211-5B): numerical cluster sizes `2,4,6,9,16,26`;
     `ROUND_005_E.md` l.242: no archimedean lower bound of the cluster; P211-8E, P211-9B, P211-17A.
   - P47 `cor:nasym` (`n_−(Arch|P_T) ≈ 4.004·T`), `thm:coer-schur`, `rem:coer-size` (dimension `2k−2` doubly
     exponential); phase 212: `ROUND_019_A`, `ROUND_020_A`, `ROUND_020_B`, `ANNEX_MARGIN_CONFLICT`.
2. **What is new.** Only (a) the family written with general convolution `φ` (the corpus uses polynomials in `∂`
   and translations, which are the case `φ` = finite combination of `δ^{(j)}_b`); (b) a Weyl LOWER bound for
   the cluster, `N_T(ε) ≳ (4/(πe))e^{2T}` (ARGUED), which is not recorded (the corpus has only upper
   bounds and fixed counts); (c) the reading of the sign of the leading defect term.
3. **Why it does not repeat.** It proposes neither construction nor sign; it is a count. Part (3) of the assignment
   (quotient + defect) IS the decomposition of P2_SCHUR_001 at `T = ∞` and that of P211-17A at finite `T`:
   it is cited and not rederived.
4. **Global connection.** None directly; see §4.

## §1 The family (PROVED except where indicated; it is 106_09 §3 with general `φ`)

Let `0 < η < δ < T`, `χ` smooth even, `χ = 1` on `[−(T−η), T−η]`, support in `[−T,T]`. Domain:
`φ ∈ L¹ ∩ L²`, support in `[−(T−δ), T−δ]`. Set `F_φ = M∗φ`, `R_φ = (1−χ)F_φ` and

    Π_T(φ) := χF_φ − A(χF_φ)u_+ − B(χF_φ)u_−,

with `u_±` fixed in `C_c^∞(I)` dual to the moments `A, B` (`A(u_+)=1, B(u_+)=0`, etc.). Since
`Φ_{F_φ}(0) = Φ_{F_φ}(1) = 0`, `A(F_φ) = B(F_φ) = 0`, hence `A(χF_φ) = −A(R_φ)`, and `Π_T(φ) ∈ P_T`.

**Exact identity.** Since `F_φ` is in the radical of `W_*` (its transform is `Φ_M·φ̂`, divisible by `ξ`;
P46 Thm 11.11, R160 Lemma 2(a)) and `a_T = W_*` on functions supported in `I` (P47):

    a_T(Π_T φ) = W_*(R_φ + A(R_φ)u_+ + B(R_φ)u_−) =: 𝔡_T(φ).                  (1.1)

Only the remainder `R_φ` and the Tate correction enter. **Bound** (106_09 Lemma 1 and (15)):
`|M(s)| ≤ C e^{M_0|s|}e^{−πe^{2|s|}}`, hence on `|t| ≥ T−η`, `|F_φ(t)| ≤ ‖φ‖_{L¹}·C e^{c}e^{−πe^{2(δ−η)}}`, and

    0 ≤ |𝔡_T(φ)| ≤ C e^{cT} e^{−2πe^{2(δ−η)}} ‖φ‖²_{L¹} ≤ C′ T e^{cT} e^{−2πe^{2(δ−η)}} ‖φ‖²_{L²}.   (1.2)

The relevant norm is `‖φ‖_{L¹}` (or `L²` with factor `√(2T)`), not `‖F_φ‖`.

**Denominator.** `‖Π_Tφ‖² = ‖F_φ‖² + O(tail) = (1/2π)∫|Φ_M(½+iτ)|²|φ̂(τ)|²dτ + O(tail)`, with
`|Φ_M(½+iτ)| ≍ τ^{2}|Ξ(τ)| ≈ τ^{15/4}e^{−πτ/4}|ζ(½+iτ)|`. The Rayleigh quotient is therefore

    a_T(Π_Tφ)/‖Π_Tφ‖² ≲ T e^{cT} e^{−2πe^{2(δ−η)}} · ‖φ‖²/∫|Φ_M|²|φ̂|².                (1.3)

## §2 The count

**Proposition 2.1 (ARGUED; the unproved step is the lower bound (2.1)).** Let `V_{L,Ω}` be the space
of the first `⌊LΩ/π⌋(1−o(1))` prolate functions with support of length `L = 2(T−δ)` and band `[−Ω,Ω]`.
Assuming

    ∫|Φ_M|²|φ̂|² ≥ e^{−(π/2)Ω − o(Ω)}‖φ‖²  on V_{L,Ω}                                   (2.1)

(average of `|ζ|²` on the band against zeros of `ζ`: an element of `V_{L,Ω}` has `φ̂` of type `T−δ`
and cannot concentrate on the zeros; it is a Remez/Logvinenko–Sereda-type inequality, not verified here),
min–max gives `μ_j(a_T|P_T) ≤ ε` for `j < dim V_{L,Ω}` whenever

    Ω ≤ Ω_max(δ, ε) := 4e^{2(δ−η)} − (2/π)log(1/ε) − O(T).

Optimizing `(T−δ)e^{2δ}` at `δ = T − ½`:

    N_T(ε) ≥ (2(T−δ)/π)Ω_max ≈ (4/(πe)) e^{−2η} e^{2T} − (2/π²)log(1/ε)   (ε fixed, T large).     (2.2)

For `ε = e^{−πe^{2T}}` (half the exponent of the margin) the same count still gives `≍ e^{2T}` eigenvalues.
The height `4e^{2T}` coincides with that of R160 Theorem D (reading). Order of magnitude `0.47e^{2T}`: `3.5, 5.1, 7.7`
at `T = 1, 1.2, 1.4`, comparable with the sizes of `P211-5B` (NUMERICAL there, not rederived).

**Comparisons.**
(a) `n_−(Arch|P_T) ≈ 4.004 T` (P47 `cor:nasym`, CITED): the near-radical cluster, `≍ e^{2T}`, is much
larger; it is not the archimedean negative space (consistent with P211-7B: «block = resonances of the comb»).
(b) `S_{T,k}`: size `2k−2 ≥ exp(c e^T)` (`rem:coer-size`, CITED), and `c(T,k) > 0` on the complement
`𝒱_k ∩ 𝒟_T` forces the whole cluster `≍ e^{2T}` (eigenvalues `≤ ε < c`) to lie, up to an angle
controlled by `‖𝖪‖`, inside `E_k` (PROVED as a consequence of min–max + `thm:coer-schur`). The upper
bound `exp(2e^T)` (P211-6C) and the lower one (2.2) leave the true size of the cluster between `e^{2T}` and `exp(2e^T)` (OPEN).
(c) Law P211-8E (`λ_A ≈ κ₈(1−χ_8)`, test of fixed index 8 in the exterior image `E`): it describes the BOTTOM of the
cluster (one vector), not the cluster. The identification «cluster = high prolate block» (P211-9B: the gauge vectors
live in the high block, `k > 4N`) remains ARGUED/OPEN; the count (2.2) shows that the cluster produced by
`{M∗φ}` grows like `e^{2T}`, it is not of fixed size.

## §3 Structure and sign of the defect term

**Quotient (CITED, P2_SCHUR_001).** At `T = ∞`, `In(𝒲) = (0,0,dim 𝒜) + In(𝒲_BB)`; at finite `T`, the family
is near-radical and the form is `𝔡_T` on the family plus the quotient plus the coupling (P211-17A: the Schur
correction is not attributable to any part; they cancel). The quotient `P_T/{Π_Tφ}` has infinite codimension
(106_09: the near-radical directions are not dense). The matrix `S_{T,k}` lives in `E_k`, which contains the
cluster: the sign problem lies in the **cluster–complement coupling** and in `𝔡_T`, not in the quotient alone
(the complement is coercive with `c(T,k)`).

**Leading term of `𝔡_T(φ)` (ARGUED).** `R_φ` is concentrated in two pieces at `|t| ≈ T−η + O(e^{−2(T−η)})`
(product of `1−χ`, which vanishes to finite order, by a profile `e^{−πe^{2t}}`), of width `w ≍ e^{−2T}`, hence
with frequency `≍ e^{2T}`. In `W_*(R_φ)`:
- archimedean diagonal `(1/2π)∫m|R̂_φ|² ≈ (2T + O(1))‖R_φ‖² > 0` (`m(τ) ≈ log τ`);
- comb: self-shifts `log n ≤ w` impossible; crossing between the two pieces only for `log n ∈ 2T ± w`,
  `O(1)` integers with `v_n ≈ 4Te^{−T}`: `|·| ≤ 4Te^{−T}‖R_φ‖²`, with sign `−` (coincides with ROUND_019_A (iii));
- Tate: `|A(R_φ)| ≤ e^{T/2}√w‖R_φ‖ ≍ e^{−T/2}‖R_φ‖`; contribution `O(e^{−T/2})‖R_φ‖²`.

Therefore, at first order, `𝔡_T(φ) = (2T + O(1))‖(1−χ)(M∗φ)‖²·(1 + O(e^{−T/2}))`: **positive**, dominated by
the archimedean diagonal by a factor `≳ e^{T/2}`; the prime tail with sign `−` loses. This corrects the reading
of ROUND_019_A (ii) in the sense that, with a smooth cutoff, the three sources do NOT have the same constant: the
archimedean one dominates (ARGUED; the computation of ROUND_019_A used the cutoff of `X_T` and was not rederived).
For the family the term is the diagonal form `φ ↦ ∫ 2T|(1−χ)(M∗φ)|²`, manifestly `≥ 0`.

**But it is not a useful positivity.** (i) It is positivity of the leading term of `a_T` on `{Π_Tφ}`, which is already
`≥ 0` up to `e^{−2πe^{2T}}`; the bottom `λ_A` is fixed by the coupling with the complement (P211-17A), not by `𝔡_T`.
(ii) The leading term is blind to the weight: the archimedean diagonal of the remainder does not see `Λ`; `Λ` enters only in the
radicality of `M∗φ`.

## §4 Controls and OBJECT_SPEC reading

Under `cΛ`: `a^{(c)}_T(Π_Tφ) = 𝔡_T(φ) + (1−c)·Arch_*(M∗φ)`, and `Arch_*(M∗φ) = Σ v_n c_{M∗φ}(log n)` is indefinite in
`φ` (`Arch_*(M) = −1.71`, positive at high frequency): the remainder loses its sign at the named step «`M∗φ` in the
radical» (F1 is satisfied at the step, ROUND_020_B §3). Deleting 2 or moving a generator: defect
`Σ(w_n−v_n)c_{M∗φ}(log n)`, of order `‖M∗φ‖²`, without sign. A sign statement on the family would use O3
(Euler product + functional equation + Γ in one line: radicality), O11/O12 (it breaks in the three controls
at the radicality step); but what it would give (`𝔡_T ≥ 0` at first order) does not touch the coupling that fixes the global sign.

## Verdict

- Family and identity (1.1)–(1.2): PROVED (106_09 §3 with general `φ`; R160 Obs. C1). CITED in its core.
- Lower count (2.2) `N_T(ε) ≳ (4/(πe))e^{2T}`: ARGUED ((2.1) missing); new in the corpus.
- Cluster inside `E_k` of (L2): PROVED as a consequence of `thm:coer-schur`.
- Quotient + defect decomposition: CITED (P2_SCHUR_001, P211-17A); not new.
- Sign of the leading defect term: positive, archimedean, blind to the weight: ARGUED; not a sign step.
- Identification with the high prolate block of P211-8E/9B: OPEN.

**Single next operation:** prove (2.1) (lower bound of `∫|Ξ|²|φ̂|²` over prolates of band `Ω`), which
turns (2.2) into PROVED and gives the minimal size `≍ e^{2T}` of the block that any object of the phase must resolve.
No sign construction is proposed.
