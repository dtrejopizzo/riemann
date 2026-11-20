# Round 006 B — The mixed word family of (M, Π_P): homogeneity, the halo/leak commutator, and the NO-GO for word families from Λ-free seeds

Target (★): λ_A(T) ≥ 0 for every T (STATEMENT_001). Object specification: OBJECT_SPEC_001 (R1–R5). Predecessors:
ROUND_005_A (comb-first Krylov family K_j, word algebra, Widom square, commutator formula, sign lemmas (SL_1),
(SL_2)), ROUND_005_B (numerical NO-GO of K_j), ROUND_005_E (sharp arena band E_{n_P}, Theorem 3.1, cluster ≈
0.15e^{4T}). This memo builds the family proposed at the end of ROUND_005_A — the Krylov space of the pair (M, Π_P)
from the same Λ-free seed — tests it, and proves why it cannot carry the sign. Labels: PROVED / CITED /
CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL. No equivalence of (★) with any other statement is used.

## 0. Notation

As in ROUND_005_A §0: I = (−T, T), Q = 1_I, R = 1 − Q, V_a the shift, c_x = ½(V_x + V_{−x}), S_x = Qc_xQ the
truncated shift, contacts N_T = {n ≥ 2 : log n < 2T}, x_n = log n, v_n = 2Λ(n)/√n, Π = Σ v_n S_{x_n} on L²(I),
𝔪 the multiplier by m(τ), M_0 = Q𝔪Q, P the orthogonal projection of L²(I) onto P_T (two Tate conditions),
M = PM_0P|_{P_T} (the operator of Arch on P_T; compact resolvent, CITED Paper 47 prop:nodes), Π_P = PΠP|_{P_T},
A = M − Π_P. K(u) = 2Σ_{j≥0} e^{−(2j+½)u} the Lévy kernel; (𝔪F)(t) = C_0F(t) + ½∫_ℝ (F(t) − F(s))K(|t − s|) ds
(the Lévy form of Paper 47 lem:K, CITED; the factor ½ is checked in §4.3). 𝒩_T = negative spectral subspace of M
on P_T, n_T = dim 𝒩_T; Band = E_{n_P} = span of the eigenvectors of M with eigenvalue ≤ λ_max(Π_P) (the sharp
band of ROUND_005_E); U_δ = spectral subspace of A for eigenvalues < δ (the cluster), m_δ = dim U_δ.

For a finite set of operators 𝒢 = {G_1, …, G_r} on P_T and a seed subspace S, the **word family** is

    𝒲_j(𝒢; S) := span{ G_{i_1} ⋯ G_{i_ℓ} s : s ∈ S, 0 ≤ ℓ < j, i_1, …, i_ℓ ∈ {1..r} },   dim ≤ (r^j − 1)/(r − 1)·dim S.

K̃_j := 𝒲_j({M, Π_P}; 𝒩_T) is the family of the task. Four variants are tested: 𝒲_j({M, Π_P}; S) (all words),
𝒲_j({A}; S) (the Lanczos family of A, the only *inhomogeneous* one, see §4.1), 𝒲_j({Π_P}; S) = K_j of ROUND_005_A,
and 𝒲_j({Π_P, [M, Π_P]}; S) (comb and commutator), with S = 𝒩_T and S = Band.

## 1. Corpus check

- Routes-tried index (README phase-211 block and files 02–05), grid R162_2300 and crossword searched for
  "commutator", "halo", "leak", "Krylov", "Lanczos", "mixed generator", "word family". Hits: P211-5A/5B/5E (the
  immediate predecessors; 5A's Next step is exactly the present object), G8D-R164_502c tool L5 ("Stieltjes on
  moments = positivity on Krylov space; only m₁ carries sign": the Krylov space of the *symbol* operator — a
  restatement), phase-83/97/98 commutator items (Gamma–Euler intertwiner, trace commutators: different objects,
  zero-side). Nothing builds the Krylov family of the pair (M, Π_P), nor the halo/leak operators H_x, L_x as
  generators, nor a word family of several generators from the archimedean cone.
- What differs from the recorded failures: 5B/5A failed because the Π-Krylov space is scale-invariant as a set and
  misses the near-null pair; the present family adds the archimedean steps M (and the commutators) that 5A §6.1
  identified as "what reaches the bottom". The hypothesis tested is 5A's: that the M-steps break the set-invariance
  and generate the pair. §4.1 proves this hypothesis false for every word family; the memo is therefore not a retry
  but the closure of the proposal, with the mechanism.
- Nothing of the index is retried. Paper 47's coercivity reduction (thm:coer-B, cor:coer-L1, k_0(T)) is the exact
  band/Schur reduction that §5 points to; it is CITED, not rebuilt.

## 2. The object and its regularity

K̃_j(T) = 𝒲_j({M, Π_P}; 𝒩_T). Generating vectors: W e with W a word in {M, Π_P}; since M𝒩_T = 𝒩_T, every word
beginning (on the right) with M collapses, so K̃_1 = 𝒩_T, K̃_2 = 𝒩_T + Π_P𝒩_T = K_2 (5A Prop. 4.2(i)), K̃_3 = K_2 +
Π_P²𝒩_T + MΠ_P𝒩_T, and span{e, Π_Pe, [M, Π_P]e} = span{e, Π_Pe, MΠ_Pe} ⊂ K̃_3 for e ∈ 𝒩_T an eigenvector
([M, Π_P]e = MΠ_Pe − αΠ_Pe). dim K̃_j ≤ (2^{j−1} + 2^{j−2} + … ) n_T; NUMERICALLY the dimension is exactly
2^{j−1}·n_T up to saturation (no rank loss).

Lemma 2.1 (the ladder lies in the form domain and in every operator domain; PROVED for seeds in the log-Sobolev
scale, CONDITIONAL for the spectral cone). Let 𝓗 := {F ∈ L²(I) : ∫ (1 + log(2 + |τ|))^s |F̂(τ)|² dτ < ∞ for all s ∈ ℝ}.
Then 𝓗 is invariant under V_x, Q, P, 𝔪-compressions (M_0, M), S_x, Π, Π_P, and hence under every word in
{M, Π_P, [M, Π_P], H_x, L_x}. If 𝒩_T ⊂ 𝓗 (true for the explicit sine cone (N2) of 5A Lemma 2.1, since each sine
vanishes at ±T and has F̂ = O(τ^{−2}); for the spectral cone it is the regularity hypothesis (H_𝓗)), then K̃_j ⊂ 𝓗
⊂ 𝒟_T ∩ Dom(M^k) for all j, k, and all form values below are finite.
Proof. V_x is the unitary multiplier e^{ixτ} on every weighted space. 𝔪 is the multiplier m(τ) with C_0 ≤ m ≤
C + log(2 + |τ|) (Paper 47 lem:mbounds, CITED), so it maps weight s to weight s − 2. Q is multiplication by
1_I = ½(sgn(t + T) − sgn(t − T)); multiplication by sgn(t − a) is, in Fourier variables, the Hilbert transform
conjugated by the modulation e^{iaτ}, and the Hilbert transform is bounded on L²(w dτ) for every weight w in the
Muckenhoupt class A_2 (CITED: Hunt–Muckenhoupt–Wheeden), which contains w_s(τ) = (1 + log(2 + |τ|))^s for every real
s (w_s is slowly varying: sup_{|τ|≤2ρ} w_s / inf_{|τ|≤2ρ} w_s = O(1) uniformly in ρ ≥ 1, and w_s ≍ 1 on |τ| ≤ 1, so
the A_2 constant is finite). P = 1 − Γ with Γ the projection on span{e^{±t/2}1_I} ⊂ 𝓗 (jumps at ±T only: F̂ =
O(1/τ), and ∫ w_s τ^{−2} < ∞ for all s). Compositions preserve 𝓗. ∎
Remark. The Lévy double integral of a word vector is finite although the vectors are not continuous: a truncated
shift of a function with a jump produces log-singularities after one application of 𝔪 (the halo of a jump), and
these remain in 𝓗. This is why the pair (M, Π_P) can be iterated at all; no such lemma was needed for the Π-Krylov
family (5A Lemma 2.2 used L^∞).

## 3. Validation numerics (NUMERICAL; validates points, proves nothing)

Set-up of ROUND_005_B/E: N = 80 Dirichlet sines, saved Arch matrices (double-precision quadrature on |τ| ≤ 6000),
Π exact in t-space, P_T imposed by the two constraints (78-dimensional Galerkin P_T; 39-dimensional even sector).
Capture of a subspace U by V: smallest principal cosine ≥ 0.99. Windows: log 2, ½log5 + 10⁻³, 0.9, 1.0 (λ_A
resolved at the first three: 1.1·10⁻⁷, 3.1·10⁻¹², 4.5·10⁻¹⁵; T = 1.0, 1.2 unresolved, |λ_A| ≤ 10⁻¹⁴, cluster
counts resolved). Scripts r6b.py, r6b_ev.py, r6b_ov.py, r6b_halo2.py (scratch).

### 3.1 Capture on P_T (both parities), seed 𝒩_T versus seed Band

Columns: dim, μ = bottom of a_T on V, cos = smallest principal cosine with U_{10⁻³}, c = bottom of a_T on V^⊥.

| T | family, seed 𝒩_T | j = 3 | j = 4 | j = 5 | j = 6 | E_k at equal dim (k = dim K̃_3) |
|---|---|---|---|---|---|---|
| log 2 (n_T = 1, m = 2) | 𝒲({M,Π}) | 4: μ 2.7e−3, cos 0 | 8: 1.2e−3, 0 | 16: 5.5e−4, 0 | 32: 1.5e−7, 0 | E_4: 2.3e−3, cos 0.98; E_6: 3.7e−4, 1.000 |
| ½log5 (1, 4) | 𝒲({M,Π}) | 4: 1.3e−3, 0 | 8: 5.3e−4, 0 | 16: 2.9e−4, 0 | 32: 6.4e−8, 0 | E_4: 1.1e−3, 0.77; E_10: 5.2e−6, 0.997 |
| 0.9 (2, 6) | 𝒲({M,Π}) | 8: 1.9e−3, 0 | 16: 6.6e−4, 0.05 | 32: 1.1e−4, 0.37 | 64: 1.0e−8, 0.999 | E_8: 2.8e−6, 0.59; E_14: 2.3e−8, 0.998 |
| 1.0 (2, 9) | 𝒲({M,Π}) | 8: 1.3e−3, 0 | 16: 8.2e−4, 0.0001 | 32: 7.6e−5, 0.014 | 64: 1.9e−8, 0.976 | E_8: —; E_21: 3.0e−12, 0.991 |

The seed 𝒩_T has only even vectors for T ≤ ½log5 (the cluster has an odd member there), so cos = 0 identically;
the even-sector test is §3.2. At T = 0.9, 1.0 (𝒩_T has one vector per parity) the words capture U_{10⁻³} only at
j = 6, dim 64 of 78 (0.9) and not at all below saturation (1.0: cos 0.976 at dim 64). The families 𝒲({Π,[M,Π]})
(dims 2, 6, 14, 30, 62) and the Lanczos family 𝒲({A}) behave in the same way or worse: at T = 0.9 the Lanczos
family of dimension 12 has cos 0 and μ = 3.5e−4. Complement coercivity c(K̃_j^⊥) stays at λ_2 ≈ 10⁻¹⁰–10⁻¹⁵
until the capture dimension, as for K_j in 5B.

Seed Band: 𝒲_1 = Band captures by itself (cos 0.98, 0.988, 0.998, 0.991 at dim 5, 9, 14, 21; 5E Table 1.2);
M·Band = Band, so 𝒲_2({M,Π}; Band) = K′_2 of 5E (dim 10, 18, 28, 42; cos ≥ 0.998) and the M-steps add nothing
before j = 3. The mixed family from the band is the band's Π-Krylov family with the halo directions added one
level later; its μ improves by one decade per level, with dimension doubling, i.e. exactly the behaviour of K′_j.

### 3.2 Even sector, scalar seed e (the lowest even archimedean mode), the near-null even pair

Columns: dim, μ, cos(pair) = smallest principal cosine with span{v_1, v_2} (two lowest even eigenvectors of A),
cos(v_1).

| T | 𝒲_3({M,Π}) (dim 4) | 𝒲_4 (8) | 𝒲_5 (16) | 𝒲_6 (32 of 39) | Lanczos 𝒲_7({A}) (7) | Π-Krylov 𝒲_7 (7) | E_4^ev | E_6^ev |
|---|---|---|---|---|---|---|---|---|
| log 2 | 2.7e−3, 0.48, 0.85 | 1.2e−3, 0.90, 0.96 | 5.5e−4, 0.999, 0.9997 | 1.5e−7, 1.000 | 8.0e−4, 0.19, 0.82 | 4.6e−3, 0.95, 0.98 | 8.3e−5, 0.988, 1.000 | 3.2e−5, 0.998 |
| ½log5 | 1.3e−3, 0.18, 0.72 | 5.3e−4, 0.55, 0.85 | 2.9e−4, 0.976, 0.993 | 6.4e−8, 1.000 | 2.8e−4, 0.0001, 0.67 | 3.1e−3, 0.68, 0.82 | 1.8e−5, 0.999, 1.000 | 1.3e−6, 0.9999 |
| 0.9 | 1.9e−3, 0.05, 0.60 | 6.6e−4, 0.22, 0.70 | 1.1e−4, 0.53, 0.86 | 1.0e−8, 0.9999 | 3.3e−4, 0.0000, 0.57 | 2.3e−3, 0.30, 0.61 | 2.8e−6, 0.975, 0.9997 | 1.9e−7, 0.9999 |
| 1.0 | 2.1e−3, 0.03, 0.77 | 1.2e−3, 0.10, 0.87 | 7.6e−5, 0.33, 0.97 | 1.9e−8, 0.996 | 9.1e−5, 0.0000, 0.75 | 2.3e−3, 0.13, 0.78 | 2.0e−6, 0.962, 0.987 | 1.6e−8, 0.9997 |
| 1.2 | 2.9e−4, 0.03, 0.89 | 1.4e−4, 0.12, 0.95 | 2.2e−5, 0.51, 0.99 | 2.1e−12, 0.989 | 7.2e−5, 0.0000, 0.87 | 4.3e−4, 0.09, 0.91 | 7.3e−8, 0.991, 0.993 | 5.5e−11, 0.998 |

Answer to task (1): **no**. K̃_3 does not capture the near-null even pair at any window (cos(pair) = 0.48, 0.18,
0.05, 0.03, 0.03); capture needs j = 5 at log 2 (dim 16 of 39) and j = 6 at T ≥ ½log5 (dim 32 of 39, i.e. 82 % of
the sector), against E_4^ev–E_6^ev (dim 4–6) for the archimedean ordering. The family 𝒲({Π, [M,Π]}) captures at
dim 15 (log 2) and 31 (T ≥ ½log5); the Lanczos family of A never captures the pair (cos ≤ 0.19 at log 2 and
0.0000 at T ≥ ½log5 for j ≤ 7; mechanism in §4.2). Comparison of capture dimension: E_k^ev 4–6; sharp band
(both parities) 5–21; K̃_j 16–32 per sector; cluster size m = 2–9.

Overlaps (r6b_ov.py). The seed is not orthogonal to the pair: |⟨e, v_1⟩|, |⟨e, v_2⟩| = (0.79, 0.58), (0.65, 0.64),
(0.56, 0.62), (0.74, 0.08) at log 2, ½log5, 0.9, 1.0. The near-null vectors are two-mode archimedean cancellation
states: v_1 ≈ 0.6·u_1 + 0.4·u_2 (weights |⟨u_i, v_k⟩|²), v_2 ≈ u_1 + u_3 (0.39 + 0.51 at 0.9; 0.24 + 0.68 at 1.0),
v_3 ≈ u_5 (0.57, 0.54), with < 0.1 % outside the lowest ten archimedean modes at T ≤ 1.0. This is why E_k^ev
captures at k ≈ 2m: the cluster is a low-lying archimedean object, and each word step from u_1 reaches the next
archimedean mode only through the off-diagonal entries of Π_P in the archimedean basis, which are O(10⁻¹).

### 3.3 Falsifiers: first dimension at which a_T^w becomes negative on the family (families built with w's own
operators, Λ-free seed; P_T both parities)

| T | w | λ_A^w | E_k | 𝒲({M,Π}; 𝒩) | 𝒲({A}; 𝒩) | 𝒲({Π}; 𝒩) | 𝒲({Π,[M,Π]}; 𝒩) | Band (j = 1) |
|---|---|---|---|---|---|---|---|---|
| log 2 | 1.1Λ | −5.4e−2 | 3 | 16 | 9 | 10 | 15 | 6 |
| log 2 | Λ + 0.1·1₂ | −6.5e−2 | 3 | 16 | 8 | 11 | 15 | 5 |
| log 2 | 1.01Λ | −4.0e−3 | 5 | 16 | none ≤ 39 | none | 15 | 5 |
| log 2 | 0.9Λ / a_3 / Beurling 3→3.2 | | 3 / 1 / 3 | 2 / 1 / 16 | 2 / 1 / 6 | 2 / 1 / none | 3 / 1 / 15 | 4 / 3 / 5 |
| ½log5 | 1.1Λ | −9.4e−2 | 4 | 16 | 9 | none | 7 | 10 |
| ½log5 | Λ + 0.1·1₂ | −8.4e−2 | 3 | 16 | 8 | none | 7 | 10 |
| ½log5 | 1.01Λ | −8.0e−3 | 4 | 32 | none | none | 15 | 9 |
| 0.9 | 1.1Λ | −1.12e−1 | 4 | 32 | 14 | none | 30 | 17 |
| 0.9 | Λ + 0.1·1₂ | −9.2e−2 | 3 | 32 | 12 | none | 30 | 16 |
| 0.9 | 1.01Λ | −1.0e−2 | 5 | 32 | none | none | 30 | 15 |
| 0.9 | 0.9Λ / a_3 / Beurling | | 1 / 1 / 1 | 2 / 2 / 2 | 2 / 2 / 2 | 2 / 2 / 2 | 2 / 2 / 2 | 12 / 9 / 15 |

Reading. The comb-strengthening falsifiers (c > 1, η = +0.1) are rejected by the archimedean ordering at dimension
3–5 and by the mixed word family only at dimension 16–32 (half the section), i.e. only once the family has captured
the pair; the comb-weakening ones (c < 1, deletions) at dimension 1–2 by every family (they act on 𝒩_T itself,
5A §5.1). The Lanczos family, the only one not invariant under cΛ as a set (§4.1), rejects 1.1Λ at dimension
8–14 but never 1.01Λ below saturation.

### 3.4 The 3×3 sign lemma on {e, p := Π_Pe, g := [M, Π_P]e} (even sector, n_T = 1)

Moments: α = ⟨e, Me⟩, μ_k = ⟨e, Π_P^k e⟩, m_2 = Arch(p), n_2 = ‖Mp‖², n_3 = ⟨p, M³p⟩, q_1 = ⟨Π_Pp, Mp⟩,
q_2 = ⟨Mp, Π_P Mp⟩. The matrix of a_T in the (non-orthogonal) system (e, p, g) is (PROVED, §4.4; checked to 10⁻¹⁶)

    𝔄_3 = [ α − μ_1        αμ_1 − μ_2                      αμ_2 − m_2                                        ]
          [ αμ_1 − μ_2     m_2 − μ_3                       n_2 − αm_2 − q_1 + αμ_3                           ]
          [ αμ_2 − m_2     n_2 − αm_2 − q_1 + αμ_3         n_3 − 2αn_2 + α²m_2 − (q_2 − 2αq_1 + α²μ_3)       ].

| T | α | μ_1 | μ_2 | μ_3 | m_2 | n_2 | n_3 | q_1 | q_2 | eigenvalues of a_T on span (generalised) | det 𝔄_3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| log 2 | −0.1501 | −0.1836 | 0.0626 | −0.0173 | +0.0326 | 0.0579 | 0.1013 | −0.0062 | +0.0004 | 9.0e−3, 1.07, 2.38 | 5.2e−6 |
| ½log5 | −0.3049 | −0.3524 | 0.1859 | −0.1167 | +0.0210 | 0.0847 | 0.1147 | −0.0236 | −0.0121 | 2.2e−3, 1.31, 2.28 | 6.9e−6 |
| 0.9 | −0.4200 | −0.4370 | 0.2055 | −0.0951 | −0.0585 | 0.0719 | 0.0612 | +0.0305 | −0.0032 | 5.3e−3, 1.04, 2.23 | 1.0e−6 |
| 1.0 | −0.5309 | −0.5611 | 0.3674 | −0.2893 | −0.1166 | 0.1501 | 0.0482 | +0.0403 | −0.0442 | 3.5e−3, 1.51, 2.02 | 7.3e−6 |
| 1.2 | −0.7277 | −0.7467 | 0.5997 | −0.5303 | −0.3553 | 0.3692 | −0.0882 | +0.2405 | −0.2118 | 1.5e−3, 2.00, 2.42 | 4.0e−6 |

(SL̃_3): 𝔄_3 ⪰ 0 holds at every window with bottom 1.5–9·10⁻³ (a necessary condition under (★), min–max). Falsifier
verdicts of (SL̃_3) (sign of the bottom of a_T^w on span{e, Π^w e, [M, Π^w]e}):

| T | 1.1Λ | 1.01Λ | 0.99Λ | 0.9Λ | η = +0.1 | η = +0.5 | no 3 | Beurling 3→3.2 | swap 2↔3 |
|---|---|---|---|---|---|---|---|---|---|
| log 2 | + (0.022) | + (0.010) | + (0.008) | − | + | + | − | + | + |
| ½log5 | + (0.029) | + (0.005) | − (−5e−4) | − | + | + | − | − | + |
| 0.9 | + (0.046) | + (0.009) | + (0.001) | − | + | + | − | − | − |
| 1.0 | + (0.055) | + (0.009) | − | − | + | + | − | − | + |
| 1.2 | + (0.073) | + (0.009) | − | − | + | + | − | − | − |

("+" = not rejected, with the bottom in brackets.) (SL̃_3) never rejects c > 1 nor η > 0: the bottom of 𝔄_3
*increases* with c (0.009 → 0.022 at log 2, 0.005 → 0.073 at 1.2), i.e. the minimiser u of a_T on K̃_3 has
⟨Π_Pu, u⟩ < 0 (≈ −0.13 at log 2, −0.72 at 1.2): on the three-dimensional family the comb is negative at the
bottom, whereas on the true near-null pair it is indefinite (ROUND_003_A). By rule 4 (SL̃_3) cannot be a sign step,
and no argument of this memo is built on it.

### 3.5 Set-invariance under cΛ (validation of Prop. 4.1)

𝒲_4({M, 1.1Π_P}; 𝒩_T) = 𝒲_4({M, Π_P}; 𝒩_T) to 4·10⁻⁸ (largest principal angle) at all four windows; the Lanczos
family 𝒲_4({M − 1.1Π_P}) differs from 𝒲_4({M − Π_P}) by principal angles with sine 0.085–0.154.

### 3.6 The halo formula (validation of §4.3)

For F = cos²(πt/2T)1_I, T = 1, at t_0 = 1.3, 1.8, 2.5: (𝔪F)(t_0) computed in τ-space (m(τ)F̂(τ), |τ| ≤ 2000)
equals −½∫_I K(|t_0 − s|)F(s) ds to 4·10⁻⁹, 8·10⁻¹⁰, 1·10⁻⁹. The factor ½ is confirmed (correction to 5A Prop.
4.2(v), which omits it).

## 4. Structure (PROVED)

### 4.1 Homogeneity: every word family from a Λ-free seed is scale-invariant as a set

Proposition 4.1. Let 𝒢 = {G_1, …, G_r} be operators on P_T each homogeneous in the weight vector v: G_i(cv) =
c^{d_i} G_i(v) for all c > 0, with d_i ∈ ℤ_{≥0} (M: d = 0; Π_P: d = 1; [M, Π_P]: d = 1; H_x, L_x: d = 0; Σ v_n H_{x_n},
Σ v_n L_{x_n}: d = 1; every word in these: d = number of degree-one letters). Let S be independent of v. Then for
every j and every c > 0,
    𝒲_j(𝒢(cv); S) = 𝒲_j(𝒢(v); S)   as subspaces.
Consequently the condition "a_T^{cΛ} ⪰ 0 on 𝒲_j(cΛ)" is the pencil condition M − cΠ_P ⪰ 0 on the fixed subspace
𝒲_j(Λ); c ↦ λ_min(M − cΠ_P|_{𝒲_j}) is concave, and its one-sided derivatives at c = 1 are −max resp. −min of
⟨Π_Pu, u⟩ over the unit minimisers u of a_T on 𝒲_j (Danskin). In particular, if the minimiser is unique and
⟨Π_Pu, u⟩ ≤ 0, then no c ∈ (1, 1 + ε) is rejected for some ε > 0; and in every case rejection of c = 1 + ε requires
a minimiser u with ⟨Π_Pu, u⟩ ≥ λ_min(a_T|_{𝒲_j})/ε.
Proof. A word W = G_{i_1}⋯G_{i_ℓ} satisfies W(cv) = c^{d_{i_1}+⋯+d_{i_ℓ}} W(v); hence each generating vector W(cv)s is a
positive multiple of W(v)s and the spans coincide. The pencil statement is the definition; concavity is the
minimum of affine functions; the derivative formula is Danskin's theorem for the minimum of ⟨(M − cΠ_P)u, u⟩ over
the unit sphere of a finite-dimensional space. ∎

Reading. This extends 5A Prop. 3.5(ii) from the single generator Π_P to every finite set of homogeneous generators,
including the archimedean operator M and the halo/leak commutators. The expectation stated at the end of 5A
("not scale-invariant as a set: M-steps break Prop. 3.5(ii)") and the premise of the present task ("cΛ changes the
subspace since M and cΠ do not commute the same way") are **false**: [M, cΠ_P] = c[M, Π_P], and the subspace is the
same. §3.5 validates this to 4·10⁻⁸. The cΛ-falsifier therefore acts on every word family through the pencil only,
exactly as on K_j; and §3.4 shows that on K̃_3 the pencil moves the wrong way (⟨Π_Pu, u⟩ < 0 at the bottom).

### 4.2 The only inhomogeneous family is the Lanczos family of A, and it is blind to the cluster

Proposition 4.2. (i) If a generator is an inhomogeneous polynomial in homogeneous operators, G = Σ_d G_d, then the
word family of G from S is contained in the word family of {G_d} from S; the only way to obtain a subspace that
depends on c is to use G with at least two homogeneous components of different degree — e.g. A = M − Π_P itself, or
the resolvent (A − z)^{−1}. For a single such generator the family is the Krylov space K_j(G; S) = {p(G)s}.
(ii) (Blindness to a near-degenerate cluster.) Let G be self-adjoint on a finite-dimensional space, U its spectral
subspace for an interval [λ_1, λ_1 + δ] with dim U = m ≥ 2, e a seed vector with Krylov dimension ≥ j (so that
p ↦ p(G)e is injective on polynomials of degree < j). Then for every unit vector u ∈ U with u ⊥ P_U e,
    cos ∠(u, K_j(G; e)) ≤ C_j(G, e) · δ,   C_j(G, e) := sup_{deg p < j} sup_{[λ_1, λ_1+δ]}|p′| · ‖P_Ue‖ / ‖p(G)e‖ < ∞,
and for δ = 0 the cosine is exactly 0 for all j: P_U K_j(G; e) = span{P_U e}.
Proof. P_U p(G)e = p(G|_U)P_U e, and G|_U = λ_1 + E with 0 ≤ E ≤ δ, so ‖p(G|_U) − p(λ_1)‖ ≤ δ sup|p′| on the interval.
Hence ⟨u, p(G)e⟩ = ⟨u, (p(G|_U) − p(λ_1))P_Ue⟩ has modulus ≤ δ sup|p′| ‖P_Ue‖, while ‖p(G)e‖ is a norm on the
finite-dimensional space of polynomials of degree < j; the ratio is bounded by compactness of the unit sphere. For
δ = 0, p(G|_U) = p(λ_1) and P_U p(G)e ∈ span{P_Ue}. ∎

Reading. The near-null cluster of A has internal spread δ = λ_2 − λ_1 = 2.3·10⁻³ (log 2, even sector), 3·10⁻⁷
(½log5), 10⁻¹¹ (0.9), ≤ 10⁻¹⁴ (1.0, 1.2). A single-generator Krylov family from a Λ-free seed sees the cluster only
through the one vector P_Ue, and resolves its other m − 1 directions at a rate O(δ) — in practice never (§3.2:
cos(pair) = 0.0000 for j ≤ 7 at T ≥ ½log5). The cluster's internal structure (which directions of U the comb is
positive or negative on, ROUND_003_A) is exactly what decides the sign of the pencil at c near 1; the inhomogeneous
family cannot see it, and the homogeneous families (Prop. 4.1) see it only after capturing U, i.e. at dimension
≥ capture dimension (≈ 2.3m by 5E for the best ordering; 16–32 per sector for the words, §3.2).

### 4.3 The halo/leak operators and the commutator (with the correct constant)

Proposition 4.3. For F ∈ L²(I) and G ∈ L²(ℝ∖I) (bounded, compact support suffices):
    (R𝔪QF)(t) = −½ ∫_I K(|t − s|) F(s) ds   (t ∉ I),       (Q𝔪RG)(t) = −½ ∫_{ℝ∖I} K(|t − s|) G(s) ds   (t ∈ I).
Define, for x > 0, H_x := Q c_x R 𝔪 Q and L_x := Q 𝔪 R c_x Q on L²(I). Then H_x* = L_x, [M_0, S_x] = H_x − L_x =
L_x* − L_x, and explicitly
    (L_xF)(t) = −¼ 1_I(t) [ ∫_T^{T+x} K(|t − s|) F(s − x) ds + ∫_{−T−x}^{−T} K(|t − s|) F(s + x) ds ],
    (H_xF)(t) = −¼ [ 1_{(−T, x−T)}(t) ∫_I K(|t − x − s|) F(s) ds + 1_{(T−x, T)}(t) ∫_I K(|t + x − s|) F(s) ds ].
Hence [M_0, Π] = L* − L with L := Σ_{n∈N_T} v_n L_{x_n}, and [M, Π_P] = P(L* − L)P − PM_0ΓΠP + PΠΓM_0P on P_T
(the last two terms of rank ≤ 2 each).
Proof. The Lévy form (𝔪F)(t) = C_0F(t) + ½∫(F(t) − F(s))K(|t − s|)ds (Paper 47 lem:K, CITED; the ½ is forced by
m(τ) − C_0 = ∫_0^∞(1 − cos τu)K(u)du = ½∫_ℝ(1 − cos τu)K(|u|)du) gives both formulas by F(t) = 0 for t ∉ I, resp.
G(t) = 0 for t ∈ I. H_x* = Q𝔪Rc_xQ = L_x since Q, R, 𝔪, c_x are self-adjoint. [M_0, S_x] = Q𝔪Qc_xQ − Qc_xQ𝔪Q; write
the middle Q as 1 − R and use [𝔪, c_x] = 0 on L²(ℝ): Q𝔪c_xQ − Qc_x𝔪Q = 0, leaving −Q𝔪Rc_xQ + Qc_xR𝔪Q. The explicit
forms: (c_xF)(s) = ½F(s − x) for s ∈ (T, T + x), ½F(s + x) for s ∈ (−T − x, −T), and 0 elsewhere outside I; for H_x,
(R𝔪QF)(t − x) ≠ 0 requires t − x ∉ I, i.e. t < x − T for t ∈ I. The Γ-terms come from M = PM_0P, Π_P = PΠP and
P = 1 − Γ. ∎
Validation: §3.6 (τ-space against the Lévy halo, 10⁻⁹). **Correction to ROUND_005_A Prop. 4.2(v)**: the halo there
is stated as −∫_I K F; the correct value is −½∫_I K F. Nothing else in 5A depends on the constant.

Reading (how K enters the words). L_x reads the **leak slab** (T, T + x) — the part of F that the shift pushes out
of the window, the same slab as in the word algebra of 5A Lemma 3.2 — through the kernel K(|t − s|) and spreads it
over the whole window; H_x reads the **archimedean halo** of F (its K-extension outside the window) on the
**entrance slabs** (−T, x − T) ∪ (T − x, T), i.e. exactly where the shifted function has no comb content. For the
weighted sums, (LF)(t) = −¼ Σ_n v_n ∫_0^{x_n} K(|t − T − σ|) F(T + σ − x_n) dσ + (left): the kernel argument is
t − T − σ with σ ∈ (0, log n), and the function is read at T + σ − log n. In a word with several letters the kernel
is evaluated at differences of positions shifted by signed sums of logarithms of contacts, i.e. at u − log r with
r ∈ ℚ_{>0} a product/quotient of contacts (5A Prop. 3.1(iii)); K is singular only at u = log r, so each word is most
sensitive to the **exact** products and quotients; the near-coincidence classes (mn ≈ k) enter from degree 3 as in
5A Prop. 3.4, now with K-weights. Nothing in this is specific to ℕ beyond the positions log n.

### 4.4 The 3×3 lemma, explicitly, and why it cannot be a sign step

Proposition 4.4. For an eigenvector e ∈ 𝒩_T (Me = αe, ‖e‖ = 1), p = Π_Pe, g = [M, Π_P]e = Mp − αp, the matrix of a_T
in (e, p, g) is 𝔄_3 of §3.4 (PROVED by expanding ⟨x, (M − Π_P)y⟩ with Me = αe and self-adjointness; checked to
10⁻¹⁶). Its entries have degrees in v: (1,1) 1; (1,2) 2; (1,3) 2; (2,2) 3; (2,3) 3; (3,3) 3. The archimedean
coefficients are: in m_2 the Lévy form on one comb response; in n_2 = ‖Mp‖² = Σ v_mv_n⟨S_{x_m}e, M²S_{x_n}e⟩ the
square of the Lévy operator; in n_3 its cube; in q_1, q_2 one Π between archimedean factors (three contacts). The
(1,3) entry is a pure halo/leak pairing:
    αμ_2 − m_2 = −⟨p, g⟩ = ⟨Π e, L e⟩ − ⟨L Π e, e⟩ + (polar terms),
i.e. the archimedean excess of the comb response over the eigenvalue, Arch(Πe) − α‖Πe‖², equals the pairing of the
response with the leak of e read through K minus the pairing of e with the leak of the response (Prop. 4.3).

(SL̃_3): 𝔄_3 ⪰ 0, i.e. (SL_2^{sc}) of 5A together with det 𝔄_3 ≥ 0 and the (1,3)/(3,3) minors. Under (★) it is a
necessary condition (min–max) and holds at the tested windows with bottom 1.5–9·10⁻³ (§3.4).

Why it cannot be attacked as a sign step (PROVED mechanism, NUMERICAL confirmation). By Prop. 4.1 the subspace
span{e, p, g} is the same for cΛ; by §3.4 the bottom of a_T^{cΛ} on it increases with c at all five windows
(⟨Π_Pu, u⟩ < 0 at the minimiser), so (SL̃_3) holds for every c ∈ [1, 1.1] and for η = +0.1, +0.5, where (★) fails.
By rule 4 any proof of (SL̃_3) is a proof of a statement true for 1.1Λ, hence cannot use the inequality on Λ that
(★) needs; the attack requested in task (2) is void, and the inequality that (SL̃_3) needs is an inequality that
1.1Λ also satisfies. The rejection of c < 1, of deletions and of the Beurling shift by (SL̃_3) is the j = 1
mechanism of 5A §5.1 (the comb must be at least as negative as the archimedean form on 𝒩_T), comb-monotone and
not a sign step.

## 5. Assessment, NO-GO class, and what the structure forces

R1 (dim → ∞, Λ-dependent subspace). The words are Λ-dependent from j = 2, but only through homogeneous
polynomials: the subspace is scale-invariant (Prop. 4.1) and its only non-trivial Λ-dependence is through the
off-diagonal entries of Π_P in the archimedean basis, which move the family one archimedean mode per level
(§3.2 overlaps). R2 (non-linear at the deciding step). The entries are polynomials of degree ≤ 3 (K̃_3) with
K-halo coefficients (Prop. 4.3–4.4), but the deciding step is the pencil on a scale-invariant subspace, and it
decides nothing before the family contains the cluster. R3 (exact reduction with controlled complement). As for
K_j: exact Schur reduction (5A Thm 4.1) available, complement coercivity ≈ λ_2 until capture, capture only at
dimension ≈ 0.8 × section in the tested range (§3.1–3.2), far above the 2.3m of the archimedean ordering. R4 (joint
entry, escape from the arena count). The halo/leak words do couple Γ(s/2) (through K) and the Euler product (through
the positions and weights), but the family is less efficient than the archimedean ordering E_k, which is
arena-bound by construction: no escape. R5 (falsifiers). (a) cΛ with c > 1: not rejected by K̃_3 at any window, by
the full word family only at dimension 16–32; c = 1.01 only at 16–32. (b) a_P: rejected at dimension 1–2 (j = 1
mechanism). (c) Beurling 3 → 3.2: rejected from ½log5 on by (SL̃_3) via the j = 1 mechanism, not rejected at log 2.
(d) η = +0.1, +0.5: never rejected by K̃_3; by the words at dimension 16–32. The identities of §4.3–4.4 are
identities and survive every falsifier, as they must.

NO-GO (class, PROVED mechanism + NUMERICAL confirmation). Class: "finite-dimensional families 𝒲_j(𝒢; S) generated
from a Λ-free seed S by any finite set 𝒢 of v-homogeneous operators (Π_P, M, [M, Π_P], H_x, L_x, their words), at
dimension small compared with the capture dimension of the near-null cluster, as carriers of the sign; and
single-generator (Lanczos) families of inhomogeneous generators from a Λ-free seed, at any dimension at which the
cluster is unresolved". Mechanism: Prop. 4.1 (set-invariance ⇒ pencil ⇒ sign decided by the cluster directions
inside the family) and Prop. 4.2 (the inhomogeneous family resolves the cluster at rate O(δ), δ ≤ 10⁻¹¹ at T ≥ 0.9).
NUMERICAL: capture of the pair by the words at dimension 16–32 per sector (E_k^ev: 4–6); rejection of 1.1Λ and
Λ + 0.1·1₂ at dimension 16–32 (E_k: 3–4); (SL̃_3) never rejects c > 1 or η > 0. This closes the proposal at the end of
ROUND_005_A and the candidate "mixed generator with the Lévy halo" of LEDGER C13.

What the structure forces. (i) Any family whose Λ-dependence is to act on the subspace itself (so that cΛ is
rejected by the subspace and not only by the pencil) must be generated inhomogeneously in v, i.e. by A = M − Π_P,
its resolvent, or its spectral projections — the Lanczos/spectral families, for which positivity on the family is
the spectral measure of the seed (index G8D-R164_502c L5, restatement), and which are blind to the cluster at any
finite depth (Prop. 4.2). (ii) Any homogeneous family must first contain U_δ(T) to precision λ_A(T); the cheapest
known ordering is the archimedean one (E_k, k ≈ 2.3m(T) ≈ 0.35e^{4T}, 5E), and the words need, in the tested range,
≈ 0.8 of the section — the depth at which they capture is the depth at which they are the section. (iii) Hence the
sign cannot be carried by the *choice of a family*; it must be carried by an inequality on the captured block, i.e.
by the n_P × n_P (or k × k) Schur complement of a_T on the band E_{n_P} (Paper 47's coercivity reduction thm:coer-B /
cor:coer-L1, CITED; 5E §1), whose entries are the exact resolvent-weighted iterated comb correlations
Π_bc (Arch_c − Π_cc)^{−1} Π_cb, non-linear in v from degree 2, with K entering through the resolvent of Arch on the
complement. The margin of that condition is λ_A(T) itself (it is exact), so no truncation with a margin can
survive rule 4: the deciding inequality must be computed at precision λ_A ≤ 4·10⁹Te^{−15.449T} (OBJECT_SPEC R3(i)).

## Result

NO-GO with class (PROVED mechanism; NUMERICAL confirmation at N = 80, T = log 2, ½log5, 0.9, 1.0, 1.2). The mixed
word family of (M, Π_P) from the archimedean negative cone does not capture the near-null even pair at j = 3
(principal cosine 0.03–0.48), captures it only at dimension 16–32 per sector (0.4–0.8 of the section; E_k^ev does it
at 4–6), does not reject 1.1Λ, 1.01Λ or Λ + 0.1·1₂ before that dimension, and its 3×3 sign lemma (SL̃_3) on
{e, Π_Pe, [M, Π_P]e} is comb-monotone at the bottom (⟨Π_Pu, u⟩ < 0), holding for every c ∈ [1, 1.1] and η > 0. The
reason is proved: every word family of v-homogeneous generators from a Λ-free seed is invariant under cΛ as a set
(Prop. 4.1; the opposite expectation of ROUND_005_A was wrong), so its only Λ-sensitivity is the pencil, which is
decided by the cluster directions it contains; and the only inhomogeneous family (Lanczos on A) resolves the
cluster at rate O(λ_2 − λ_1) ≤ 10⁻¹¹ (Prop. 4.2). Seed and generator are both "the issue" in the sense that no
Λ-free seed with homogeneous generators can escape; the sharp band seed captures by itself (5E) and the M-steps
add nothing to it (M·Band = Band). LEDGER C13 closes; C14 stands.

## What was proved

- Lemma 2.1: the log-Sobolev scale 𝓗 ⊂ 𝒟_T ∩ ⋂_k Dom(M^k) is invariant under V_x, Q, P, 𝔪, S_x, Π, M, hence under all
  words in {M, Π_P, [M, Π_P], H_x, L_x} (A_2-weighted boundedness of the Hilbert transform, CITED); unconditional
  for sine seeds, hypothesis (H_𝓗) for the spectral cone.
- Prop. 4.1: word families of v-homogeneous generators from a Λ-free seed are scale-invariant as sets; the cΛ
  condition on them is the pencil; Danskin criterion for rejection of c = 1 + ε (needs a minimiser with
  ⟨Π_Pu, u⟩ ≥ λ_min/ε).
- Prop. 4.2: inhomogeneous single-generator families are Lanczos spaces; a Krylov space from one seed captures a
  cluster of spread δ only along P_Ue up to O(δ) (exactly one direction at δ = 0).
- Prop. 4.3: halo and leak formulas with the correct constant ½ (validated 10⁻⁹); H_x = L_x*; [M_0, S_x] = L_x* − L_x;
  explicit kernels on the leak and entrance slabs; [M_0, Π] = L* − L; polar corrections of rank ≤ 4.
  Correction to 5A Prop. 4.2(v) (factor ½).
- Prop. 4.4: the 3×3 matrix 𝔄_3 of a_T on {e, Π_Pe, [M, Π_P]e} in nine moments (degrees 1–3); the identity
  Arch(Πe) − α‖Πe‖² = ⟨Πe, Le⟩ − ⟨LΠe, e⟩ + polar.
- NUMERICAL: capture/falsifier tables §3.1–3.4; overlaps of the cluster with the archimedean modes (two-mode
  cancellation states, < 0.1 % beyond the tenth mode at T ≤ 1); set-invariance to 4·10⁻⁸.

## What failed and why

- Task (1): K̃_3 does not capture the pair nor the cluster; the mixed family is less efficient than E_k at every
  dimension and every window; falsifiers c > 1, η > 0 rejected only at dimension 16–32. Cause: Prop. 4.1 (no
  Λ-dependence of the subspace beyond homogeneous polynomials; scale-invariant) and the slow archimedean ascent of
  the words (one archimedean mode per level, through O(10⁻¹) off-diagonal comb entries, §3.2).
- The premise "cΛ changes the subspace" (task and 5A Next step): false, [M, cΠ_P] = c[M, Π_P].
- The Lanczos family of A (the only non-invariant one): blind to the cluster (cos(pair) = 0.0000 at T ≥ ½log5 for
  all j ≤ 7), by Prop. 4.2 with δ ≤ 3·10⁻⁷.
- (SL̃_3): holds, but survives 1.1Λ and η = +0.1, +0.5 at all windows; the attack of task (2) is void by rule 4.
- The band seed: captures at j = 1 (5E), and M·Band = Band, so the mixed generator adds nothing to the band's
  Π-Krylov family before j = 3; Prop. B of ROUND_004_A applies to the band as before.
- Precision: T = 1.0, 1.2 unresolved for λ_A (round-off); all claims at those windows concern the cluster count,
  capture cosines and the falsifier dimensions, which are resolved.

## Next concrete step

Stop building families from Λ-free seeds with homogeneous generators (closed class). The structure forces the
sign into the exact Schur complement of a_T on the sharp band (or on E_k with k ≥ 2.3m(T)): S_T := D_b − Π_bb −
Π_bc (Arch_c − Π_cc)^{−1} Π_cb, exact, with Arch_c − Π_cc ≥ α_{n_P+1} − λ_max(Π_P) > 0 on the complement (by the
definition of the sharp band and Lemma 3.0 of 5E; coercivity is PROVED once the band threshold is λ_max(Π_P)). The
step is: (a) corpus check of this object against Paper 47's coercivity reduction (thm:coer-B, cor:coer-L1, k_0(T))
and the (L2′) reduction of ROUND_001_C, to state in writing what differs (band threshold λ_max(Π_P) instead of
A_T; exact resolvent instead of a scalar floor); (b) expand (Arch_c − Π_cc)^{−1} in the Neumann series in
Arch_c^{−1/2}Π_ccArch_c^{−1/2} (convergent when the band threshold is max(π_+, π_−); the ratio is ≈ π/α_{n_P+1},
close to 1 at the sharp threshold, ≤ ½ at threshold 2π_+ with band dimension N_Arch(2π_+)), and determine
NUMERICALLY the degree at which the truncated Schur complement first rejects 1.01Λ and Λ + 0.1·1₂ at T = 0.9 — the
degree at which the resolvent-weighted iterated comb correlations (K through the resolvent of Arch on the
complement; near-coincidences from degree 3) carry the sign; (c) if that degree is bounded (≤ 4) across windows,
write the degree-d truncation as an explicit polynomial inequality in v on the band and attack it; if it grows
with T, record the growth as the quantitative form of R3(i) and the NO-GO for truncations.
