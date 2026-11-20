# Round 001 C — The exact Nyquist reduction with η ↓ 0: dimension, gauge, shift, and the block at ½ log 5

Object: the two-sector Nyquist reduction of Paper 47 (§sec:nyq, P47:6049–6439: thm:nyq, prop:nyq-LK,
thm:nyq-sectors, thm:nyq-schur, rem:nyq-schur-num, prop:nyq-nopoint) and the band of the symbol
(prop:band, P47:2864–2982). Target (★): λ_A(T) ≥ 0 for every T. Notation as in DOSSIER_001 §1 and P47 §sec:nyq:
ω_k = πk/2T, s_T = m + r_T − Σ_{n∈N_T} v_n cos(· log n) (truncated symbol), r_T(τ) = ∫_{2T}^∞ cos(τu)K(u)du,
c_T = s_T(0), ε_T := ∫_{2T}^∞ K, so |r_T| ≤ ε_T.

---------------------------------------------------------------------------------------------------
## 0. Corpus check

- Routes-tried index, 04_PHASES_100-189.md lines 70–72: prop:nyq-nopoint (NO-GO: no common eigenbasis),
  thm:nyq-schur via the inversion-free bound S^low_η (PARTIAL at ½log3, log2, ½log5 with d = 7/29/45–59; NO-GO for all T
  because d_η ≳ λ_A^{−1/p}), circulant cone on the mesh (FALSIFIED). Line 146: algebra of D_T, two self-adjoint
  extensions (PARTIAL/PROVED). README line 148: pointwise Nyquist positivity false; correlated version = (N), REF.
  06_OPEN_RESIDUES line 29, 58: coherence on the mesh, signed cancellation at ≈ e^{2T} Nyquist frequencies.
- Paper 48 table (P48:779): "Nyquist sampling, two sectors — the form reads the symbol on πk/2T — coherence inequality
  equals the target — REF".
- Grid R162_2300 item 41 (R186_052–053): exact Nyquist identity, two sectors, S^low numerics.
- DOSSIER_001 §6(h), §7: the observation that thm:nyq-schur(ii) holds for every η > 0.

What differs from the recorded attempts, and why it avoids the recorded failure.
(a) The recorded NO-GO concerns S^low_η, whose loss S_η − S^low_η forces large η, hence large d_η. This memo works with
    the exact Schur complement S_η at η ↓ 0, which has no such loss; the dimension count of S_η is a different quantity
    and was never computed. (b) New tools proved here: the reduction is valid on every shifted mesh ω_k + α and modulo the
    alternating gauge c(−1)^k; the gauge- and shift-optimized dimension is bounded by (2T/π)·|{s_T < 0}|. (c) The block
    at T = ½log5 + ε is written explicitly and the role of the entering contact is identified (it is a gauge to first
    order). Nothing here reattempts the S^low certificate, a pointwise criterion, or the circulant cone.
The recorded reason for the REF label (the reduction is an exact restatement) still applies to everything below:
no sign step is produced. This is stated in the Result.

---------------------------------------------------------------------------------------------------
## 1. Shifted and gauged sampling

**Lemma 1 (shifted Nyquist identity). [PROVED]** For every α ∈ ℝ and F ∈ 𝒟_T,
a_T(F) = (1/4T) Σ_{k∈ℤ} |F̂(ω_k+α)|² s_T(ω_k+α), absolutely convergent, and Σ_k (−1)^k |F̂(ω_k+α)|² = 0.

Proof. The functions ε^α_k(t) = (4T)^{−1/2} e^{−i(ω_k+α)t} form an orthonormal basis of L²(−2T,2T) (the standard basis times
the unimodular e^{−iαt}). Let τ_u be the unitary "twisted translation" on L²(−2T,2T) for which every ε^α_k is an
eigenvector, τ_u ε^α_k = e^{i(ω_k+α)u} ε^α_k; concretely (τ_u f)(t) = f(t−u+4Tj) e^{−iα4Tj} with j chosen so that
t−u+4Tj ∈ (−2T,2T). For F supported in I_T and 0 ≤ u ≤ 2T, the part of F(·−u) that is wrapped lands in
(−2T, −3T+u) ⊂ (−2T,−T], disjoint from I_T, so ⟨F, τ_u F⟩ = c_F(u). Parseval in {ε^α_k} gives
(1/4T)Σ_k |F̂(ω_k+α)|² e^{−i(ω_k+α)u} = c_F(u) for 0 ≤ u ≤ 2T, and by conjugation for |u| ≤ 2T. At u = 2T the twisted
translate does not meet I_T, which gives the alternating identity after multiplying by the unimodular e^{i(ω_0+α)2T}.
From here the proof of thm:nyq (P47:6097–6122) applies verbatim (atoms at ±log n, then ν_ε = ½K(|u|)1_{ε<|u|<2T}du and
monotone convergence; the identity uses only the cosine sampling formula on |u| ≤ 2T). ∎

**Lemma 2 (two shifted sectors and the gauge). [PROVED]** Put e^α_j = (2T)^{−1/2}e^{−i(ω_{2j}+α)t},
e'^α_l = (2T)^{−1/2}e^{−i(ω_{2l+1}+α)t} on I_T; both are orthonormal bases of L²(I_T), related by the same real unitary
Laurent matrix H = (h_{l−j}), h_m = 2(−1)^m/(π(2m+1)). For every c ∈ ℝ, with s^{α,c}_k := s_T(ω_k+α) + c(−1)^k,
a_T(F) = ½ Σ_j s^{α,c}_{2j} |⟨F,e^α_j⟩|² + ½ Σ_l s^{α,c}_{2l+1} |⟨F,e'^α_l⟩|².
Proof. ⟨e^α_j, e'^α_l⟩ = ⟨e_j, e'_l⟩ = h_{l−j} (the phase e^{−iαt} cancels), so the computation of thm:nyq-sectors(iii)
is unchanged. Parseval in each basis gives (1/2T)Σ_{k even}|F̂(ω_k+α)|² = (1/2T)Σ_{k odd}|F̂(ω_k+α)|² = ‖F‖², so the gauge
adds +c‖F‖² to one sector and −c‖F‖² to the other; average with Lemma 1. ∎

Remark. On the unshifted mesh r_T(ω_k) = (−1)^k ρ(ω_k) with ρ > 0 decreasing (eq:nyq-r): the aliasing correction is a
gauge modulated by a slowly varying amplitude. Its constant part is removed by a gauge.

---------------------------------------------------------------------------------------------------
## 2. The reduction (L2′)

**Theorem 1 (exact reduction at η ↓ 0). [PROVED]** Fix T > 0, α ∈ ℝ, c ∈ ℝ, write s_k = s^{α,c}_k and
𝒩 := {k ∈ ℤ : s_k ≤ 0}, 𝒩_e = {j : 2j ∈ 𝒩}, 𝒩_o = {l : 2l+1 ∈ 𝒩}, η_0 := min{s_k : s_k > 0} > 0.
For η ∈ (0, η_0] put 𝒩_η := span{e^α_j : j∈𝒩_e} + span{e'^α_l : l∈𝒩_o}, 𝒞 := P_T ∩ 𝒩_η^⊥, N′ := pr_T 𝒩_η, and
c_* := ½( min_{j∉𝒩_e} s_{2j} + min_{l∉𝒩_o} s_{2l+1} ) ≥ η_0.
(i) a_T(F) ≥ c_* ‖F‖² for F ∈ 𝒟_T ∩ 𝒩_η^⊥.
(ii) S(x) := inf{ a_T(x+y) : y ∈ 𝒞 ∩ 𝒟_T } is attained at a unique y_*(x), linear in x; S is a Hermitian form on N′,
dim N′ ≤ |𝒩|, and λ_A(T) ≥ 0 ⟺ S ⪰ 0, λ_A(T) > 0 ⟺ S ≻ 0. The space and the form do not depend on η ∈ (0,η_0], and for
η > η_0 (larger blocks) the equivalence also holds (thm:nyq-schur); so "for some η > 0" ⟺ "for every η > 0".
(iii) (Dimension lower bound.) |𝒩| ≥ n_−(a_T on L²(I_T)), the number of negative directions of a_T on all of L²(I_T).
Proof. s_k → +∞ along the shifted mesh by prop:nyq-LK(iii) (the lower bound there holds for every real τ), so 𝒩 is
finite and η_0 > 0. For η ≤ η_0 the set {k : s_k < η} equals 𝒩. (i) and (ii) are the proof of thm:nyq-schur(i)–(ii)
(P47:6385–6405) with e_j, e'_l replaced by e^α_j, e'^α_l and s_T(ω_k) by s_k; that proof uses only Lemma 2, Parseval, the
growth of s_k, Lemma lem:compact, and that e^α_j, e'^α_l, e^{±t/2}1_{I_T} lie in 𝒟_T (their transforms are O(1/|τ|)
on the mesh). (iii) A negative subspace of a_T meets 𝒩_η^⊥ only in 0 by (i), so its dimension is at most codim 𝒩_η^⊥
= dim 𝒩_η ≤ |𝒩|. ∎

**Explicit data of S. [PROVED]** In the coordinates c_j = ⟨F, e^α_j⟩ (so ⟨F,e'^α_l⟩ = (Hc)_l):
- a_T(F) = ½⟨c, (D_e + HᵀD_oH)c⟩, D_e = diag(s_{2j}), D_o = diag(s_{2l+1}); for finitely supported c the series
  Σ_l s_{2l+1}|(Hc)_l|² converges absolutely ((Hc)_l = O(1/l), s_k = O(log|k|)).
- P_T = {c : Σ_j c_j κ^±_j = 0}, κ^±_j = conj⟨e^{±t/2}1_{I_T}, e^α_j⟩ with
  ⟨e^{±t/2}, e^α_j⟩ = (2T)^{−1/2}·2 sinh((±½ + iπj/T + iα)T)/(±½ + iπj/T + iα); at α = 0 this is
  (2T)^{−1/2}·2(−1)^j sinh(T/2)/(½ ± iπj/T).
- 𝒩_η^⊥ = {c : c_j = 0 (j∈𝒩_e), (Hc)_l = 0 (l∈𝒩_o)}.
- S = A_{N′N′} − A_{N′𝒞} A_{𝒞𝒞}^{−1} A_{𝒞N′} with A = ½(D_e + HᵀD_oH), A_{𝒞𝒞} ≥ c_* on 𝒞.

**Correction (to DOSSIER_001 §6(h)/§7 wording). [PROVED as a statement about what is available]** The entries of the
exact S are not absolutely convergent series in the samples: they contain A_{𝒞𝒞}^{−1}, the inverse of an unbounded
operator on an infinite-dimensional space. thm:nyq-schur(iii) gives series only for the inversion-free lower bound
S^low. What is available for S itself:
**Proposition 1 (two-sided computable bounds). [PROVED]** (a) S ≥ S^low (thm:nyq-schur(iii), applied to the shifted,
gauged data). (b) If X_1 ⊂ X_2 ⊂ … are finite-dimensional subspaces of 𝒞 ∩ 𝒟_T whose union is dense in the form norm
of a_T + M‖·‖², then S^{(J)}(x) := inf_{y∈X_J} a_T(x+y) decreases to S(x), and S^{(J)} − S = a_T(y_J − y_*) where y_J is
the X_J-minimizer. Proof of (b): with x fixed, y ↦ a_T(x+y) is a continuous strictly convex quadratic on 𝒞∩𝒟_T in the
form norm (coercive by (i)); infima over increasing sets decrease; for y_k ∈ ∪X_J with y_k → y_* in form norm,
a_T(x+y_k) → S(x); the error identity is the Pythagoras relation of the a_T-inner product on 𝒞. ∎
So (L2′) is sandwiched by explicit finite matrices: S^{(J)} (upper, exact entries are finite sums of absolutely convergent
series in s_k and h_m) and S^low (lower, same).

**Cost of shrinking the block. [PROVED + NUMERICAL]** The complement constant is c_* = ½(s^e_+ + s^o_+), the mean of the
smallest positive even and odd samples. The norm of y_* satisfies a_T(y_*) ≤ ‖P_𝒞 g_x‖²/c_* (Cauchy–Schwarz in the
a_T-inner product, as in thm:nyq-schur(iii)); a small c_* means a large, poorly conditioned correction. At
T = ½log5 + 10^{−4} with the optimal gauge (§4) the smallest positive gauged sample is 8.8·10^{−5} (NUMERICAL). Dimension
and coercivity trade against each other: the block {s_k < η} for larger η is larger and c_* ≥ η is better.

---------------------------------------------------------------------------------------------------
## 3. Growth of the negative Nyquist set

Put n_raw(T) := #{k : s_T(ω_k) ≤ 0} (α = c = 0), d_min(T) := min_{α,c} #{k : s^{α,c}_k ≤ 0}, and let τ^*_T be the root of
m_lo(τ) = A_T + ε_T, m_lo(τ) = log(τ/2π) − 1/τ − 1/(2τ²) (lem:mbounds).

**Proposition 2 (upper bounds). [PROVED]**
(a) {s_T < 0} ⊂ (−τ^*_T, τ^*_T), and τ^*_T = 2π e^{A_T+ε_T} exp(1/τ^*_T + 1/(2τ^{*2}_T)).
(b) n_raw(T) ≤ 2⌊2Tτ^*_T/π⌋ + 1.
(c) d_min(T) ≤ min_α #{k : s_T(ω_k+α) ≤ 0} ≤ (2T/π)·|{τ ∈ ℝ : s_T(τ) < 0}| ≤ (4T/π) τ^*_T ≈ 8T e^{A_T+ε_T}.
Proof. (a) s_T(τ) ≥ m(τ) − ε_T − A_T ≥ m_lo(τ) − ε_T − A_T for τ > 0, and m_lo is increasing; s_T is even; the identity is
the definition. (b) counts mesh points in the interval. (c) s_T is real-analytic (K decays like e^{−u/2}, so r_T extends
to |Im τ| < ½) and nonconstant, so its zero set is discrete; hence for almost every α no sample vanishes. By Tonelli,
∫_0^{π/2T} #{k : s_T(ω_k+α) < 0} dα = Σ_k ∫_0^{π/2T} 1_{s_T<0}(ω_k+α) dα = |{s_T < 0}|, so some α (with no vanishing
sample) has count ≤ (2T/π)|{s_T<0}|; take c = 0. The last inequality is (a). ∎

Comparison: (L2) uses dimension 2k−2 with k > T e^{A_T + C_B}, C_B ≈ 1.64, i.e. ≈ 10.3 T e^{A_T}; the bound (c) is
≈ 8 T e^{A_T}. The proved upper bounds are therefore of the same order; the possible gain of (L2′) is entirely the ratio
|{s_T < 0}| / (2τ^*_T), on which nothing is proved.

**Proposition 3 (lower bound). [PROVED]** For T ≥ ½log2, n_raw(T) ≥ 1 (s_T(0) = c_T < −2.37, prop:nyq-LK(iv)), and for
all α, c: #{k : s^{α,c}_k ≤ 0} ≥ n_−(a_T on L²(I_T)) (Theorem 1(iii)).
No superlinear lower bound is proved; a lower bound for n_−(a_T on L²(I_T)) is OPEN (the comb part has no sign on the
Dirichlet-sine spaces used in thm:J).

**Is the negative set O(T)? [NUMERICAL: no; proof OPEN]** Counts on the mesh (double precision; counts of samples with
s_T < 0; all k with |ω_k| ≤ τ^*_T examined, so the raw counts are complete up to rounding at near-zero samples):

| T | N_T | A_T | n_raw | largest negative |k| | d (gauge c, α = 0) | min over 40 shifts α | (2T/π)·|{s_T<0}| (shift average) |
|---|---|---|---|---|---|---|---|
| ½log3+10^{−6} | {2,3} | 2.249 | 11 | 16 | 5 | 5 | 8.1 |
| log 2 | {2,3} | 2.249 | 11 | 20 | 9 | 9 | 10.3 |
| ½log5 − 10^{−7} | {2,3,4} | 2.942 | 13 | 23 | 11 | 12 | 14.2 |
| ½log5 + 10^{−4} | {2,3,4,5} | 4.382 | 33 | 158 | 11 | 16 | 24.9 |
| 1 | {2,3,4,5,7} | 5.853 | 49 | 594 | 41 | 44 | 48.3 |
| 1.25 | up to 11 | 8.521 | 131 | 8916 | 125 | 128 (16 shifts) | 139 |
| 1.5 | up to 19 | 13.016 | 693 | 685361 | 685 (c ∈ [−1,1]) | — | — |

The counts are far from linear in T: from T = 1.25 to 1.5 the raw count grows by a factor 5.3, and the largest negative
sample sits at ω ≈ 7.2·10^5, with log ω ≈ 13.5 ≈ A_T, i.e. near the edge τ^*_T of Proposition 2(a). This is the
mesh trace of deep simultaneous near-coincidences of the log p. Heuristic [ARGUED, not proved]: the comb at a generic
mesh point behaves like a sum of weakly dependent oscillations of variance ½Σv_n² ≈ 4T² while m ≈ log(τ/2π), so the
negative set has length of order ∫ exp(x − x²/8T²) dx, superexponential in T and only cut off by τ^*_T. Proving a
superlinear lower bound needs quantitative Kronecker–Weyl equidistribution at finite height (OPEN).

Answer to task (2): the sharpest proved bound is Proposition 2(c), d_min ≤ (2T/π)|{s_T<0}| ≤ (4T/π)τ^*_T; O(T) is not
proved and is contradicted by the data (NUMERICAL). The raw count n_raw is not even continuous in T (33 vs 13 across
½log5); the gauge-optimized count is the meaningful one (11 vs 11), see §4.

---------------------------------------------------------------------------------------------------
## 4. The block at T = ½log5 + ε

**Lemma 3 (an entering contact is a gauge to first order). [PROVED]** Let n ∈ N_T with δ := 1 − log n/2T ∈ (0,1). On the
unshifted mesh v_n cos(ω_k log n) = v_n(−1)^k cos(πkδ), so
v_n cos(ω_k log n) − v_n(−1)^k = v_n(−1)^k (cos πkδ − 1), with |·| ≤ v_n min(2, π²k²δ²/2).
Hence after the gauge c ↦ c + v_n the contact n perturbs the samples by at most θ only at |k| ≥ (2θ/v_n)^{1/2}/(πδ),
Proof: trigonometry.
In the form this is the identity v_n Re c_F(log n) = (1/4T)Σ_k |F̂(ω_k)|² v_n cos(ω_k log n), with the gauge part
contributing 0 (Lemma 1); and c_F(2T − h) → 0 as h ↓ 0, consistent with continuity of λ_A (lem:contA). ∎

So at T = ½log5 + ε (δ ≈ 2ε/log5) the contact 5 adds ≈ v_5 = 1.4395 to every odd sample and subtracts it from every
even sample, up to v_5 π²k²δ²/2 (numerically ≤ 2.8·10^{−3} for |k| ≤ 160 at ε = 10^{−4}). This explains the raw jump
13 → 33 (31 of the 33 raw negative samples are even) and why the gauge removes it.

**The block. [NUMERICAL data; the structure PROVED by Theorem 1]** At ε ∈ {10^{−6}, 10^{−4}}, α = 0, the optimal gauge is
c ≈ 1.21 (close to v_5 − 0.23) and
𝒩 = {0, ±3, ±5, ±9, ±14, ±23}, |𝒩| = 11: even sector 𝒩_e = {0, ±7} (k = 0, ±14), odd sector 𝒩_o ↔ k = ±3, ±5, ±9, ±23.
Gauged samples (ε = 10^{−4}): k=0: −6.739; 3: −0.337; 5: −0.259; 9: −1.287; 14: −0.635; 23: −0.053.
Raw samples there: −7.950, 0.875, 0.952, −0.076, −1.846, 1.158. Smallest positive gauged sample 8.8·10^{−5}.
The raw negative set (α = c = 0, k ≥ 0) is {0,2,4,6,9,12,14,18,24,32,38,56,70,88,102,144,158}.

**The exact finite inequality at this window (L2′ at ½log5 + ε). [PROVED as an equivalence; truth value OPEN at this
form, PROVED true by thm:log5A only at T ≤ ½log5]**
With s_k = s_T(ω_k) + 1.21(−1)^k, A = ½(diag(s_{2j}) + Hᵀ diag(s_{2l+1}) H) on ℓ²(ℤ), the 11-dimensional space
𝒩_η = span{e_0, e_{±7}} + span{e'_l : 2l+1 ∈ {±3, ±5, ±9, ±23}}, its projection N′ to P_T (dim ≤ 11), and 𝒞 as in
Theorem 1:  λ_A(T) ≥ 0 ⟺ A_{N′N′} − A_{N′𝒞}A_{𝒞𝒞}^{−1}A_{𝒞N′} ⪰ 0, with A_{𝒞𝒞} ≥ c_* ≥ 8.8·10^{−5}.
The samples enter as s_k = m(ω_k) + r_T(ω_k) − Σ_{n∈{2,3,4,5}} v_n cos(πk log n / 2T) + 1.21(−1)^k. The arithmetic of the
block: a negative sample at large k requires k log n/4T close to integers for n = 2, 3 simultaneously (4 follows 2,
5 is gauged); e.g. k = 158: k log2/4T = 34.02, k log3/4T = 53.93, the mesh image of 2^54 ≈ 3^34; k = 144: 31.01 and 49.15,
the image of 2^49 ≈ 3^31. These are the mesh analogue of near-coincidences (cf. prop:align). Note that with the optimal
gauge the block contains no such deep coincidence: all of them have been pushed into the complement, where they sit as
small positive samples and make c_* small. The arithmetic does not disappear; it moves from the dimension into the
conditioning of A_{𝒞𝒞}.

**Proposition 4 (no criterion on block samples alone). [PROVED on L²(I_T); on P_T ARGUED]** Fix finite index sets 𝒩_e, 𝒩_o
and the values of s_k on them, with at least one negative. Consider abstract sample sequences equal to these on the block
and ≥ η > 0 off the block. (a) If all off-block samples equal M, then for every δ > 0 the bottom of the form on L²(I_T)
is > −δ once M is large. (b) If the negative block sample is s_{2j}, j ∈ 𝒩_e, and all off-block odd samples equal η, then
a(e_j) = ½s_{2j} + ½Σ_{l∈𝒩_o}s_{2l+1}h²_{l−j} + ½η Σ_{l∉𝒩_o}h²_{l−j} < 0 for η small whenever ½s_{2j} + ½Σ_{l∈𝒩_o}s_{2l+1}h²_{l−j} < 0.
So the sign is not a function of the block samples.
Proof. (a) If bottoms ≤ −δ for M → ∞, unit minimizers F_M have off-block mass ≤ C/M in both bases, so dist(F_M, E) and
dist(F_M, E′) → 0 with E = span{e_j : 𝒩_e}, E′ = span{e'_l : 𝒩_o}; by compactness of the unit sphere of E a subsequence
converges to a unit vector of E ∩ E′, which is {0} by the rational-function argument of prop:nyq-nopoint. (b) is the
formula of Lemma 2 at F = e_j, with Σ_l h²_{l−j} = 1. The P_T case needs the two Tate constraints in (a) and (b); not done. ∎
Consequently any sufficient condition "inequality on the 11 block samples ⇒ S ⪰ 0" is false as a statement about
sequences; it must involve all samples through A_{𝒞𝒞}^{−1}.

---------------------------------------------------------------------------------------------------
## 5. Falsifier test

Theorem 1, Lemmas 1–3 and Propositions 1–4 are identities or bounds valid for every positive window measure
ρ_T = K1_{(0,2T)}du + Σ v_n δ_{log n} with any weights v_n ≥ 0, any constant c_T and any real shift and gauge. They hold
verbatim for (a) cΛ, (b) a_P, (c) a Beurling system, (d) any finite modification of v_n. This is correct for an exact
equivalence and shows that none of them is a sign step; they produce no sign. The finite inequality (L2′) itself is
sensitive because it is exact: its truth value is that of λ_A(T) ≥ 0 for each of the four systems. The block data do
move under the falsifiers at T = ½log5 + 10^{−4} (NUMERICAL; raw count / largest negative |k| / gauge-optimized count):
Λ: 33/158/11; 1.5Λ: 119/1254/49; 0.7Λ: 15/32/9; a_3 (contacts 2, 4 deleted): 25/44/7; v_2 + 0.1: 33/158/13.
The dimension is not monotone in any sign-relevant direction (deleting primes lowers it, as does shrinking Λ), so the
dimension count carries no sign information. Any future sign step on S must fail for (a)–(d); in particular it cannot
depend only on the block samples (Proposition 4) nor only on the size of the block.

---------------------------------------------------------------------------------------------------
## 6. What is new relative to P47 §sec:nyq and P48 "Nyquist, two sectors — REF"

1. Theorem 1 with η ↓ 0: the exact reduction lives on the nonpositive samples only, and the "some/every η" equivalence.
2. Lemmas 1–2: the whole reduction holds on every shifted mesh and modulo the alternating gauge; the dimension is
   min_{α,c} #{s^{α,c} ≤ 0}, and Proposition 2(c) bounds it by (2T/π)|{s_T < 0}|.
3. Theorem 1(iii): the block dimension is at least the negative index of a_T on L²(I_T).
4. Correction: the exact S has no series entries; Proposition 1 gives explicit finite matrices on both sides.
5. Lemma 3: an entering contact is a gauge to first order; the jump of the raw count at ½log n is a gauge artefact.
6. The explicit 11-dimensional block at ½log5 + ε, and the observation that the optimal gauge moves all deep
   near-coincidences into the complement, paying in c_*.
7. Proposition 4: no inequality on block samples alone decides the sign.
8. Numerical counts at seven windows: the negative Nyquist set grows much faster than O(T).

---------------------------------------------------------------------------------------------------
## Result

PIVOT with reason. (L2′) is PROVED as an exact finite-dimensional restatement whose dimension (gauge- and shift-optimized)
is 5, 9, 11, 11, 41, 125, ~685 at T = ½log3, log2, ½log5^±, 1, 1.25, 1.5 (NUMERICAL), much smaller than the (L2)
dimension, but the reduction carries no sign, the complement inverse A_{𝒞𝒞}^{−1} is not explicit, and its coercivity
c_* collapses as the block shrinks (8.8·10^{−5} at ½log5 + ε). Shrinking the dimension moves the arithmetic into
the conditioning rather than removing it.

## What was proved

- Lemma 1 (shifted Nyquist identity and alternating identity on every shifted mesh).
- Lemma 2 (two shifted sectors with the same H; gauge invariance under c(−1)^k).
- Theorem 1 ((L2′): λ_A ≥ 0 ⟺ S ⪰ 0 on N′, dim ≤ #{k : s^{α,c}_k ≤ 0}, for every α, c, every η ∈ (0,η_0]; coercive
  constant c_* = ½(s^e_+ + s^o_+); dimension ≥ n_−(a_T|L²(I_T))).
- Proposition 1 (S^low ≤ S ≤ S^{(J)}, S^{(J)} ↓ S).
- Proposition 2 (n_raw ≤ 2⌊2Tτ^*/π⌋+1; d_min ≤ (2T/π)|{s_T<0}| ≤ (4T/π)τ^*_T, τ^*_T = 2πe^{A_T+ε_T}e^{O(1/τ^*)}).
- Proposition 3 (n_raw ≥ 1 for T ≥ ½log2; every count ≥ n_−(a_T|L²)).
- Lemma 3 (entering contact = gauge + O(k²δ²)).
- Proposition 4 on L²(I_T) (the sign is not a function of block samples).

## What failed and why

- Explicit series for the entries of the exact S: not available; the dossier's wording applies only to S^low.
- O(T) growth of the negative Nyquist set: not proved, and contradicted numerically (superlinear; largest negative
  samples near τ^*_T, i.e. at deep near-coincidences). A superlinear lower bound needs quantitative equidistribution
  of (τ log p) at finite height.
- No sign: the reduction survives all four falsifiers, as an exact identity must; no inequality on the samples of the
  block alone can be sufficient (Proposition 4).

## Next concrete step

Quantify the trade-off of §2: for the block 𝒩_η = {k : s^{α,c}_k < η}, prove an explicit bound for ‖y_*(x)‖ and for the
gap S − S^low in terms of η and the samples in [η, η + 1), and choose (α, c, η) to minimize dimension subject to a
coercivity floor. The concrete object is the operator A_{𝒞𝒞} = ½(D_e + HᵀD_oH) compressed to 𝒞 at T = ½log5 + ε with
the gauge 1.21: its inverse is the only non-explicit ingredient of (L2′) there, and its coercivity floor is set by the
smallest positive gauged samples (to be located; at least one is below 10^{−4}), so a lower bound for A_{𝒞𝒞} on the span
of those modes, using the H-coupling (each e_j spreads over the odd sector with weights h²_{l−j}), is the first finite
piece to prove.
