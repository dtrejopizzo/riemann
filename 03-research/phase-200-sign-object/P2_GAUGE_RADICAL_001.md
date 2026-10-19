# P2_GAUGE_RADICAL_001 — Angle between the gauge and the radical of 𝒲_a (phase 200, round 7, question P2)

**Data and scripts:** `P2_GAUGE_RADICAL_001_data/` (`gauge_defect.py`, `analyse.py`, `window_bottoms.py`, `analysis.json`,
`gauge_mu{5,10,15}.npz`, `window_bottoms_mu{5,10,15}_M16.json`, logs).
**Labels:** PROVED / ARGUED / OPEN / NUMERICAL, per item.

## Summary (≤250 words)

**Answer to P2: yes it separates, but not at the scale of the leak. Therefore it does not work as quantitative E1.**
Given Guo L4.4, the complete exterior form 𝒲_a restricted to the gauge is exactly
D_a = Σ_n 2(Λ(n)−a(n)) n^{−1/2} c_{Φ_φ}(log n), i.e. the comb difference evaluated on correlation atoms.
(1) Check (c), NUMERICAL: ‖𝒲_Λ|_{𝒢_M}‖ ≤ 2.4·10⁻⁵, versus ‖arch|_𝒢‖ = 2.247. It is zero within quadrature error
(Parseval 7·10⁻⁷). The gauge discretization is validated.
(2) PROVED, by scaling: D_a on unit vectors of the gauge **does not depend on T**. The numbers at μ = 5, 10 and 15
agree to 5 digits.
(3) NUMERICAL: for every falsifier, D_a|_𝒢 is **indefinite**, with n₋ ≥ 2 and n₊ ≥ 2. None has a definite sign.
Moreover, d_a = 9 = dim 𝒢_M in the block restricted to ε ≤ 10⁻² for 7 of the 9 combs. The exceptions are the
single-atom deletions Λ−δ_3 and Λ−δ_7, which have a near-kernel.
(4) Defect 𝔡_a = −min D_a: 0.0128 for 0.9Λ, 0.2246 for 1.1Λ, 2.246 for 2Λ, 0.122 for a_{2}, 0.128 for a_{2,3},
0.128 for the zero comb and 0.185 for Λ−δ_3. All are O(1), while the leak scale of G_Λ in the block is
10⁻¹¹–10⁻¹⁴ (and the true value at μ = 15 is 10⁻⁷⁰).
In the sample λ_A^{(a)} ≥ −C·𝔡_a holds with C ≈ 10, but trivially: both sides are O(1).
𝔡_a is a **T-independent comb distance**: at a = Λ the stability inequality reduces to the original statement.
For this reason (β)-quantitative offers no leverage on L′♯. This is a NUMERICAL + PROVED NO-GO (scale invariance)
for the "gauge–radical angle" version of E1.

## 1. Object and discretization

**Definitions (Paper 47 def:ext, thm:ext-half, prop:ext-gauge, eq:symbol, eq:W).** T = ½log μ, λ = √μ.
- Gauge 𝒢_T: φ even, C², supported on [−1/λ,1/λ], with φ(0) = ∫φ = 0.
- Tail Φ_φ(x) = e^{x/2}Σ_{n≥1}φ(ne^x), supported on x ≤ −T.
- Complete form on the line: 𝒲_a[Ψ] = (1/2π)∫m|Ψ̂|² − Σ_{n≥2} 2a(n)n^{−1/2}c_Ψ(log n) + 2A(Ψ)B(Ψ), where
  m(τ) = Re ψ(¼+iτ/2) − log π, c_Ψ(u) = ∫Ψ(t)Ψ(t−u)dt, A = ∫Ψe^{t/2} and B = ∫Ψe^{−t/2}.

**Structural identity (PROVED given Guo L4.4, CITED).** By prop:ext-gauge, 𝒲_Λ(Φ_φ,·) = 0. Then, for any
comb a and any pair φ, φ′ ∈ 𝒢_T,
  𝒲_a(Φ_φ, Φ_φ′) = Σ_{n≥2} 2(Λ(n)−a(n)) n^{−1/2} c_{Φ_φ,Φ_φ′}(log n) =: D_a(φ,φ′).
Consequently:
- for cΛ, D = (1−c)·Σv_n c(log n) = (1−c)·(arch + 2AB)|_𝒢;
- for the zero comb, D = (arch + 2AB)|_𝒢;
- for a_P, D = Σ_{p∈P,k} 2 log p · p^{−k/2} · c(k log p);
- for the deletion Λ−δ_q, D is a single atom, v_q c(log q).

Thus, "G_a|_{𝒢_M}" is a linear combination of **correlation atoms** c_Φ(log n) on the gauge.

**Gauge discretization.** We use x = λ|v| ∈ [0,1] and the raw basis p_k = x²(1−x²)³x^{2k}, with k = 0…9. Each p_k is
even and C² at ±1/λ, and satisfies φ(0) = 0. We impose ∫φ = 0, which leaves **dim 𝒢_M = 9**, and orthonormalize in
L²(−1/λ,1/λ).
Declared deviation: I **did not** reuse the GRAM_INERTIA_001/MORI15 pipeline. That pipeline depends on scratchpad
files (ed1/, gi/) and its environment is the Möbius/ω-grid basis, not an explicit gauge. Here the gauge is
discretized directly according to def:ext. This suffices for P2 because the restriction to the gauge only needs
gauge tails.

**Computation (NUMERICAL).**
- Comb. With S(u) = Σ_kφ(ku) on a uniform grid u_i = i/(λN), N = 2·10⁵, we compute
  c(log n) = √n ∫_0^{1/(λn)} S(u)S(nu) du by exact trapezoid rule on the grid (nu_i = u_{ni}). Prime powers
  n < 6000 are summed.
- Archimedean. On the Mellin side, Φ̂_φ(τ) = ζ(½+iτ)·φ̃(½+iτ), with φ̃(s) = λ^{−s}Σ_j c_j/(j+s), and |τ| ≤ 600
  (ζ with mpmath).
- A = φ̃′(1), because the pole of ζ cancels with ∫φ = 0. B = ζ(0)φ̃(0) = −½φ̃(0).
- Precision: float64 on the tail side and dps 20 for ζ. dps ≥ 50 was not used here because no gauge quantity has
  relative cancellation below 10⁻⁵. The reported defects are ≥ 1.5·10⁻³, and the control error (Parseval and the
  Λ check) is ≤ 2.4·10⁻⁵.
- Windows (λ_A^{(a)} and λ_W^{(a)}): Legendre Galerkin of degree < 16 on the window interval, with mpmath at
  dps 60 (μ = 5, 10) and dps 100 (μ = 15). The kernel K formula from CERT_FALSIFIERS_001 is used.

## 2. (c) Mandatory consistency check: Λ (NUMERICAL)

| μ | ‖𝒲_Λ\|_{𝒢_M}‖ (eigenvalue range) | ‖arch\|_𝒢‖ | ‖comb_Λ\|_𝒢‖ | rel. Parseval error |
|---|---|---|---|---|
| 5 | [−1.29e−5, 1.65e−5] | 2.2472 | 2.2465 | 7.4e−7 |
| 10 | [−6.2e−6, 4.3e−6] | 2.2472 | 2.2465 | 7.4e−7 |
| 15 | [−1.8e−5, 2.4e−5] | 2.2472 | 2.2465 | 7.4e−7 |

The archimedean term and the comb cancel to within 10⁻⁵ relative. The residual is compatible with the truncation
at τ ≤ 600 and at n < 6000, and with the grid. **Guo L4.4 / prop:ext-gauge is confirmed in the block** as exact
isotropy of 𝒢_M for 𝒲_Λ. What is verified is isotropy (null restriction), not the complete radical. The cross
terms 𝒲_Λ(Φ_φ, Ψ_f) with non-gauge f were not computed (OPEN numerically; the complete radical is CITED, Guo).

In the first test (μ = 5, K = 8, N = 10⁵) we obtained ‖𝒲_Λ|_𝒢‖ = 1.1e−6 versus arch = 1.72. It is the same verdict.

## 3. Invariance in T (PROVED)

**Lemma P2.1.** Let ψ ∈ 𝒢_0, the version with λ = 1, and φ(v) = ψ(λv). Then Φ_φ(x) = λ^{−1/2}Φ_ψ(x+T) and
‖φ‖² = λ^{−1}‖ψ‖². Since 𝒲_a is translation invariant (def:ext), 𝒲_a[Φ_φ]/‖φ‖² = 𝒲_a[Φ_ψ]/‖ψ‖². In particular,
the spectrum of D_a on the normalized gauge does not depend on T.
*Proof.* S_φ(u) = S_ψ(λu), hence e^{x/2}S_ψ(λe^x) = λ^{−1/2}e^{(x+T)/2}S_ψ(e^{x+T}). The remaining claims are a
change of variable. □ (This is the gauge part of prop:ext-univ.)

**NUMERICAL confirmation.** The spectra of arch, comb_Λ and D_a for μ = 5, 10 and 15 agree to the 5 printed digits
(table §4 and `analysis.json`).

## 4. (a), (b), (d): spectrum of D_a = G_a|_{𝒢_M} (NUMERICAL; identical for μ = 5, 10, 15)

Auxiliary spectra on 𝒢_M:
- arch|_𝒢: {−0.505, −0.112, −0.034, 0.098, 0.255, 0.535, 0.947, 1.650, 2.247};
- comb_Λ|_𝒢 = (arch + 2AB)|_𝒢: {−0.128, −0.058, 0.088, 0.204, 0.255, 0.575, 0.946, 1.666, 2.246}.

The form Σ_n v_n c(log n) is indefinite on the gauge.

In the table, the "sen θ ≳" column is σ_min(D_a)/‖D_a‖ (see note (a) below).

| comb a | min D_a | max D_a | n₋/n₊ | σ_min | 𝔡_a = −min | sen θ ≳ | λ_A^{(a)} μ=5 / 10 / 15 (block) | λ_A/𝔡_a (μ=15) |
|---|---|---|---|---|---|---|---|---|
| Λ | ≈0 (≤2.4e−5) | ≈0 | — | — | **0** | — | 2.0e−7 / 4.7e−10 / 7.7e−11 | — |
| 0.9Λ | −1.277e−2 | 2.247e−1 | 2/7 | 5.8e−3 | 0.0128 | 0.026 | −0.026 / −0.064 / −0.083 | −6.5 |
| 1.1Λ | −2.247e−1 | 1.277e−2 | 7/2 | 5.8e−3 | 0.225 | 0.026 | −0.072 / −0.054 / −0.034 | −0.15 |
| 2Λ | −2.247 | 1.277e−1 | 7/2 | 5.8e−2 | 2.247 | 0.026 | −0.925 / −0.658 / −0.555 | −0.25 |
| a_{2} | −1.223e−1 | 9.723e−1 | 2/7 | 4.5e−2 | 0.122 | 0.046 | −0.507 / −0.545 / −0.552 | −4.5 |
| a_{2,3} | −1.279e−1 | 1.566 | 2/7 | 5.9e−2 | 0.128 | 0.037 | −0.308 / −1.116 / −1.163 | −9.1 |
| zero comb | −1.277e−1 | 2.247 | 2/7 | 5.8e−2 | 0.128 | 0.026 | −0.308 / −0.687 / −0.868 | −6.8 |
| Λ−δ_3 | −1.854e−1 | 6.004e−1 | 4/5 | 4.8e−5 | 0.185 | 8e−5 | −0.368 / −0.687 / −0.840 | −4.5 |
| Λ−δ_7 | −1.56e−3 | 2.044e−1 | 3/4 (+2 ≈0) | ~1e−11 | 0.0016 | 0 | (no contact at 7 for μ ≤ 7) | — |
| Λ−δ_2 | −1.212e−1 | 6.958e−1 | 2/7 | 5.1e−2 | 0.121 | 0.073 | — | — |

The DH comb was not computed because it does not exist in cert_falsifiers. The zero comb and the Y1 deletions,
which are certified (CERT_FALSIFIERS_001), were used as zero falsifiers.

**Notes.**
- **(b) dim 𝒢_M = 9.** The block's λ_W^{(Λ)} values are 3.7e−11 (μ=5), 5.0e−13 (μ=10) and 1.1e−14 (μ=15). These are
  the leak scale of the block; the certified value at μ = 15 is ~4.7e−70.
- **rad_ε of the restriction.** Number of eigenvalues |e| ≤ ε‖D_a‖:
  - ε = 10⁻¹: 4 for cΛ and the zero comb; 1 for a_{2}; 3 for a_{2,3}; 2 for Λ−δ_3; 7 for Λ−δ_7.
  - ε = 10⁻²: 0 in all except Λ−δ_3 (2) and Λ−δ_7 (7).
  - ε = 10⁻⁶ and ε = 10⁻⁹: 0 in all except Λ−δ_7 (4 and 2).

  Therefore, for ε ≤ 10⁻² the defect is **d_a = 9 = dim 𝒢_M** (maximal codimension) for cΛ, a_P, the zero comb and
  Λ−δ_2. For Λ = a, d_Λ = 0.
- **Large-q atoms.** The atom c(log q) only sees the part u < 1/(qλ) of the tail, which decays as u³ (Poisson,
  φ ∈ C²). That is why it has low numerical rank in a polynomial block: for q = 7 there are 2 directions with
  |e| < 10⁻⁹‖D‖. In those directions the intersection 𝒢_M ∩ rad(D_a) is nontrivial at numerical precision. This is
  a block artifact (ARGUED): with dim 𝒢_M → ∞, the atoms are infinite-rank forms.
- **(a) Angle.** For v ∈ 𝒢 unit, ‖G_a v‖ ≥ ‖P_𝒢G_a v‖ = ‖D_a v‖ ≥ σ_min(D_a). Since ‖G_a v‖ ≤ ‖G_a‖(ε + sen θ),
  we get sen θ_min ≥ σ_min(D_a)/‖G_a‖ − ε.
  - The "sen θ ≳" column uses ‖D_a‖ instead of ‖G_a‖. It is an optimistic proxy, because ‖G_a‖ in the full ambient
    space (window ⊕ gauge) was not computed.
  - The full ambient space and the exact Jordan angles remain **OPEN** in this memo.
  - What is solid is that the bound does not depend on μ, neither the proxy nor the numerator σ_min (Lemma P2.1).
- **(d) Sign.** **Indefinite for every falsifier**: none has D_a ≤ 0 on all of 𝒢_M. For cΛ the signature is (2,7)
  if c < 1 and (7,2) if c > 1. This follows exactly from D_{cΛ} = (1−c)·comb_Λ|_𝒢 and from the signature (7,2)
  of comb_Λ|_𝒢 (PROVED given the identity; the signature is NUMERICAL).

## 5. (e) Interpretation and candidate theorem

**Defect functional.** 𝔡_a := −min_{v∈𝒢_M, ‖v‖=1} vᵀG_a v ≥ 0. In the block it is 0 for Λ (NUMERICAL up to 2.4e−5;
PROVED given Guo) and > 0 for every tested falsifier. Moreover:
- 𝔡_a > 0 holds whenever the combination Σ(Λ−a)(n)n^{−1/2}c(log n) has a negative direction in the gauge.
- For cΛ, 𝔡 = |1−c|·0.128 if c < 1 and |1−c|·2.247 if c > 1. It is linear in |1−c|, while |λ_A^{(cΛ)}| is not.

**Candidate theorem (block level), NUMERICAL.** In the Legendre-16 window block and the gauge-9 block, for the
tested combs and μ ∈ {5, 10, 15}, **λ_A^{(a)} ≥ −10·𝔡_a** holds.
- The constant 10 covers the sample: the worst ratio is a_{2,3}, with 9.1.
- 1.1Λ and 2Λ have much slack (ratio ≤ 0.25).

**Why the candidate theorem is of no use for L′♯ (ARGUED + PROVED in its pieces):**
1. **𝔡_a does not see T** (Lemma P2.1, PROVED). It is a functional of the comb alone, a "distance from a to Λ"
   measured on correlation atoms of universal gauge tails. The leak scale ℓ(T), in contrast, decays like
   e^{−cT²}-type: 10⁻¹¹ → 10⁻¹⁴ in the block and 10⁻⁷⁰ the certified value at μ = 15. There is already a factor
   ≥ 10⁸ in the block, and ≈10⁶⁸ at μ = 15. The gauge–radical angle is **O(1)**, not of scale ℓ nor ℓ^{½}.
2. At a = Λ, the stability inequality 𝒲_a ≥ −C·Δ_T(a)·‖·‖² of META §P2 reduces to 𝒲_Λ ≥ 0, which is the original
   statement. The "yes" branch of P2 holds qualitatively (codimension separation: d_Λ = 0 and d_a = 9), but is
   empty of quantitative content. There is no interpolation a ↦ Λ in which Δ_T(a) controls the leak of Λ.
3. That **D_a is indefinite** for every falsifier rules out even the monotone version "the gauge pushes downward."
   The gauge has no sign transportable to the window.
4. That 𝔡_a is O(1) while λ_A^{(a)} is also O(1) explains the bounded ratio, but the relation is **dimensional,
   not structural**: with 1.1Λ versus 0.9Λ, the ratio changes by a factor of 40.

**Lemma that would need to be proved to salvage something (OPEN, probably false in useful form):** a bound
𝒲_a(Ψ_f) ≥ −C(T)·sup_{𝒢}|D_a|·dist²(r_f, 𝒢̄_T) with C(T) ≤ ℓ-scale. By point 1 this is incompatible with 𝔡_a
being T-independent, unless C(T) absorbs all the content. Not recommended.

## 6. Verdict and labels

- (c) Guo L4.4 in the block, as isotropy: **NUMERICAL** (≤ 2.4e−5 versus 2.25).
- Identity D_a = Σ 2(Λ−a)n^{−1/2}c(log n) on the gauge: **PROVED given Guo L4.4 (CITED)**.
- T-invariance of the gauge defect: **PROVED** (Lemma P2.1), with **NUMERICAL** confirmation.
- Indefiniteness of D_a for cΛ (every c ≠ 1), a_{2}, a_{2,3}, the zero comb and Λ−δ_{2,3,7}: **NUMERICAL**. For cΛ
  it reduces to the (7,2) signature of comb_Λ|_𝒢.
- d_a = dim 𝒢_M for ε ≤ 10⁻² (except for deletions of q ≥ 3): **NUMERICAL**.
- λ_A^{(a)} ≥ −10·𝔡_a in the sample: **NUMERICAL**, without content for L′♯.
- **P2: it separates (yes, qualitative), not at scale ℓ (no, quantitative).** The "gauge–radical angle/codimension"
  version of (β)-quantitative (E1) stays **NO-GO (PROVED in the scale invariance + NUMERICAL in the
  indefiniteness)**. Reason: the gauge defect is a universal comb distance in T.
- OPEN: the full ambient space (gauge ⊕ window sources) with cross terms 𝒲_a(Φ_φ, Ψ_f), the exact Jordan angles
  and DH proper. None of these can change point 1, because the restriction to the gauge is already T-invariant.

**Index:** this NO-GO must be added to `05-meta-and-planning/ROUTES-TRIED-INDEX/` as "E1/(β) quantitative via
gauge–radical angle: T-invariant defect, indefinite." This memo does not write it because the role is read-only
outside phase-200; it is left for the coordinator.
