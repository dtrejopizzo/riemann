# PROOF_L_SHARP_S_001 — Strategy S: Q(G,G) in the Poisson-dual harmonics (negativity half of (C_G))

Phase 199, prover memo (pen and paper; NUMÉRICO only as a check, scripts `PROOF_L_SHARP_S_001_endpoint.py`,
`PROOF_L_SHARP_S_001_localized.py`). Target: (C_G)(b) of AUDIT_L_SHARP_3 §6: −Q(G,G) ≥ κμ^{−A}dist²(ρ,𝒢̄₁) on the constrained
PW_μ class, first its sign Q(G,G) ≤ 0. "E1"
is not a criterion; no zero of ζ, no analyticity of 1/ζ is used anywhere (only the FE, Γ, Poisson summation).
Notation of memos F, P, Q, R.

**Outcome.** (C_G)(b) NOT proved. (S.0) The exponent in the brief is corrected: G_k(s) = −∫ρX^{−s}∫_X^∞e^{2πikt}t^{s−1}dt dX.
(S.1, PROVED) Exact dual structure: G_k(s) = −k^{−s}∫_k^∞ξ^{s−1}ρ̂(ξ sgn k)dξ, harmonics are dilates of one function, and
**G(s) = ρ₀/s − \overline{F_c(s)}**: the defect is the conjugated exterior partial-sum transform of the *dual data*
c(ξ) = 2∫_1^∞ρ(X)cos(2πξX)dX on (1,∞). Incomplete-Γ form; its complete-Γ part sums over k to −F₀ (the FE).
(S.2, PROVED) Q(G_k,G_l) as an explicit time-domain bilinear form; G^{log} = ∂_sG + G_L. (S.3) **Diagonal negativity FAILS**:
local weight log(k/t) (t = dilate length), endpoint law Q(G_k,G_k) = ρ(1)²(log k − 1)/(2π²k²)(1+o(1)) (ARGUED, NUMÉRICO
confirmed to 2% at k = 8): positive for every k ≥ 3. (S.4) Cross terms are not decoupled with polynomial loss in general, and
the harmonic amplitudes are not free coordinates: on span{G_k : k ≥ 3} the matrix is positive definite (NUMÉRICO) ⇒ NO-GO for
"harmonic-wise sign + decoupling". (S.5) The sign lives in arithmetic sums over ℕ: endpoint total ∝ −ζ′(2) − ζ(2) < 0;
localized-dual total ∝ −[(γ + log X)log N + γ log X − 2γ₁] < 0 (ARGUED). (S.6, PROVED) Polar mode: Q(G_pol,G_pol) =
c₀ρ₀² − 2ρ₀ρ₁, c₀ = ψ(3/2) − log π = −1.1082, rank 2, indefinite; it couples to the harmonics only through Θ_∞ (rank one).
(S.7) Λ-ingredient localised. Residual (★_S) stated in §8. No sign claimed. Row D OPEN.

## 0. Corpus / index check and the new reason
Index (README §phase 199; 04_PHASES_100-189) searched for Poisson dual / dual data / cosine transform / harmonic / AFE /
incomplete Gamma. Relevant: K.3 (Poisson in the dilate index on PW tails is circular, technique NO-GO), Q §2 consistency
remark (Hankel image = Σ_{k≠0}(ρ1)^(ke^{−y})), R.4 (stationary-phase weight 2log k − log(τ/2π), ARGUED), INV_K_001 (AFE as
reformulation), L2_012 (|ζ|²-positivity via AFE, NO-GO). **Why not a retry.** K.3 used Poisson to *evaluate* 𝔔 on PW tails;
R.4 gave a heuristic per-harmonic weight with no amplitude and no cross terms. Here the object is the *exact* bilinear matrix
Q(G_k,G_l) of the Euler–Maclaurin defect, its dual-data form, and the test of whether a per-harmonic sign exists. The answer
is negative (S.3–S.4), recorded as a NO-GO, and the surviving sign is located in explicit ℕ-sums (S.5).

## 1. S.0–S.1 — exact harmonic and dual structure (PROVED)
**S.0.** F Lemma 3.1 at w = 1−s: e_{1−s}(X) = −Σ_{k≠0}∫_X^∞e^{2πikt}t^{−w}dt with t^{−w} = t^{s−1}. Since T_X(w) = ζ − ζ_X =
−X^{1−w}/(1−w) − e_w(X), Φ_G = −∫ρX^{−s}T_X dX gives G = G_pol + Σ_{k≠0}G_k with G_pol = ρ₀/s and
  G_k(s) = −∫_1^∞ρ(X)X^{−s}∫_X^∞e^{2πikt}t^{s−1}dt dX   (exponent t^{s−1}, not t^{−s}).
**Theorem S.1.** Put ρ̂(ξ) := ∫_1^∞ρ(X)e^{−2πiξX}dX and c(ξ) := ρ̂(ξ)+ρ̂(−ξ) = 2∫_1^∞ρ cos(2πξX)dX. Then for s = ½+iτ:
(a) G_k(s) = −k^{−s}∫_k^∞ξ^{s−1}ρ̂(−ξ)dξ (k ≥ 1; k ≤ −1 with ρ̂(ξ)), and in the time variable v = log(t/X) > 0,
  G_k(s) = ∫_0^∞u_k(v)e^{iτv}dv,  u_k(v) = −e^{v/2}ρ̂(−ke^v);  paired: u_{±k} = −e^{v/2}c(ke^v) =: u_k (k ≥ 1),
  so u_k(v) = k^{−1/2}u_1(v + log k)|_{v>0}: **the harmonics are the dilates of one function**, truncated at v = 0.
(b) G(s) = ρ₀/s − Σ_{k≥1}k^{−s}∫_k^∞ξ^{s−1}c(ξ)dξ = ρ₀/s − \overline{F_c(s)}, where F_c(s′) := ∫_1^∞c(ξ)ξ^{−s′}ζ_ξ(1−s′)dξ is
the partial-sum transform of Thm F.1 applied to the dual data c|_{(1,∞)}, and 1−s = s̄ on the line.
(c) G_pol(s) is the transform of ρ₀e^{v/2}1_{v<0} (the k = 0 Poisson term, ρ̂(0) = ρ₀ = c(0)/2).
(d) Incomplete-Γ form: ∫_X^∞e^{2πikt}t^{s−1}dt = (−2πik)^{−s}Γ(s,−2πikX) (principal branches). Splitting Γ(s,z) = Γ(s) − γ(s,z),
the complete part summed over ±k is 2(2π)^{−s}cos(πs/2)Γ(s)ζ(s)·R(s) = ζ(1−s)R(s) = F₀ (FE, CITED Titchmarsh 2.1), so
Σ_k G_k = −F₀ + (lower-incomplete parts) is F − F₀ − G_pol again: the AFE structure is exactly Γ(s,·)'s transition
|2πkX| ≈ |s|, i.e. harmonic k is non-negligible at frequency τ only if k < τ/(2πX).
*Proof.* (a) Substitute t = Xe^v: X^{−s}t^{s−1}dt = e^{sv}dv, Fubini on the X-integral for each fixed v (ρ = O(X^{−2})), then
v′ = v + log k. The v-integral converges absolutely: for ρ C¹ with a jump at 1, ρ̂(ξ) = O(1/ξ), so |e^{v/2}ρ̂(ke^v)| = O(e^{−v/2}/k).
(b) Sum over k: Σ_k k^{−1/2}O(k^{−3/2}) after one integration by parts in ξ (boundary term at ξ = k); the conditionally
convergent Σ_{k≠0} of Lemma 3.1 is legitimised by Poisson summation for the BV function n ↦ ρ(ne^{−y})1_{ne^{−y}>1} (equality a.e.
in y, hence in L²(dτ)), which is Q's §2 identity. Rewriting Σ_k k^{−s}∫_k^∞ = ∫_1^∞ξ^{s−1}c(ξ)Σ_{k≤ξ}k^{−s}dξ = F_c(1−s). (c) direct.
(d) the incomplete-Γ formula is the standard rotation of contour (CITED DLMF 8.6); the sum is Riemann's FE. □
**Reading.** Poisson self-duality of the lattice ℤ turns the exterior defect of ρ into the exterior transform of the dual data c,
with the *same* coefficients a_k ≡ 1. For PW data, c(ξ) = g(ξ) − 2∫_0^1ĝ cos(2πξX)dX; for ξ > μ only the in-band piece and the
endpoint X = 1 survive (K.3's circularity, now as an identity of transforms).

## 2. S.2 — the exact bilinear form (PROVED)
For pairs (U,U^{log}) with time functions (u,u^{log}) (U = ∫u e^{iτv}dv), Plancherel gives
  Q(U,V) = (1/2π)∫Θ_∞(τ)Re(U\overline{V})dτ − ∫(u v^{log} + v u^{log})dv.
By R.0 and linearity, G^{log} = ∂_sG + G_L with G_L the defect of ρ log X; in time, u_k^{log}(v) = −e^{v/2}[c_L(ke^v) + v·c(ke^v)],
c_L(ξ) := 2∫ρ log X cos(2πξX)dX (the log-weight is log t = log X + v). Hence, exactly,
  **Q(G_k,G_l) = ⟨Θ_∞u_k,u_l⟩ − ∫_0^∞e^v[2v c(ke^v)c(le^v) + c(ke^v)c_L(le^v) + c(le^v)c_L(ke^v)]dv,**
with ⟨Θ_∞u,w⟩ := (1/2π)∫Θ_∞Re(Û\overline{Ŵ})dτ. In dual form (Thm S.1(b), R.0 for the data c):
  Q(G−G_pol, G−G_pol) = (1/2π)∫[Θ_∞|F_c|² + 2Re(\overline{F_c}F_{c,log})]dτ − (1/π)∫Re(\overline{F_c}F_c[c♮])dτ,
  c♮(ξ) := 2∫_1^∞ρ(X)log(ξX)cos(2πξX)dX.
(Derivation: Ḡ = −F_c, G^{log} = \overline{∂_sF_c} − \overline{F_{c_L}}, using ∂_s\overline{F(s)} = −\overline{∂_sF(s)} on the line,
and ∂_sF_c = F_{c,log} − F_c[c log ξ].) The first bracket is the symbol part of 𝔔 for the dual data *with the sign of the prime
part reversed*. **OPEN (S-dual):** whether the c♮ term, whose Mellin multiplier is the log-derivative of the cosine kernel
(2π)^{−z}Γ(z)cos(πz/2) — a Γ_ℝ-ratio — recombines with the first bracket into −𝔔[c] + (truncation terms at ξ = 1, X = 1).
If so, (C_G)(b) would be exterior positivity of the dual data: a self-dual restatement, not a reduction.

## 3. S.3 — the diagonal: where it fails (ARGUED + NUMÉRICO; NO-GO for per-harmonic sign)
**Local weight (ARGUED, sharpens R.4).** u_k oscillates with phase 2πkXe^v = 2πkt, local frequency τ = 2πkt, Θ_∞ =
log(τ/2π) + O(τ^{−2}) = log(kt); the log-pairing carries −2log t. Net local weight **log(k/t)**: harmonic k is negative exactly on
dilate lengths t > k (⟺ k < √(τ/2π), R.4's AFE point), positive on 1 < t < k.
**Endpoint law (ARGUED).** If ρ(1) ≠ 0 (generic: the constraints g(0) = ĝ(0) = g(μ) = 0 do not impose ĝ(1) = 0), then
c(ξ) = −ρ(1)sin(2πξ)/(πξ) + O(ξ^{−2}) and c_L(ξ) = O(ξ^{−2}) (log 1 = 0), so |u_k|² averages to ρ(1)²e^{−v}/(2π²k²) and
  **Q(G_k,G_k) = (ρ(1)²/2π²k²)∫_0^∞(log k − v)e^{−v}dv·(1+o(1)) = ρ(1)²(log k − 1)/(2π²k²)·(1+o(1)),  k → ∞.**
For PW data and k > μ this is the full harmonic (c is endpoint-driven beyond μ). **Sign change at k = e: positive for all k ≥ 3.**
NUMÉRICO (ρ = e^{−(X−1)}, v ≤ 5, dv = 2·10^{−5}, exact Θ_∞ via complex ψ): diag = −0.0556, −0.0044, +0.00045, +0.00120, +0.00123,
+0.00112, +0.00098, +0.00086 for k = 1…8; predicted (same truncation) −0.0486, −0.0034, +0.00074, +0.00132, +0.00129, +0.00115,
+0.00101, +0.00088 (ratio → 1). Localized dual data (ρ = bump on (1,L)·cos(2πξ₀X), c concentrated at ξ₀): diagonal changes
sign between k = ⌊√(X̄ξ₀)⌋ and +1 (ξ₀ = 6: k = 3/4; ξ₀ = 10: k = 4/5), as the AFE reading predicts. **Diagonal negativity
Q(G_k,G_k) ≤ 0 ∀k is FALSE** (falsifier: any ρ with ρ(1) ≠ 0, k large; NUMÉRICO at k = 3…8, ARGUED for all k ≥ 3).

## 4. S.4 — cross terms; harmonics are not free (NUMÉRICO; NO-GO, ARGUED)
k ≠ l: phases 2πkt vs 2πlt are non-stationary relative to each other except at the truncation v = 0, so Q(G_k,G_l) is a boundary
term, not a decaying-in-μ quantity; it is of the same order as the diagonal (endpoint data: Q(G_1,G_l) = −1.8e−3, −1.2e−3,
−7.5e−4, −5.2e−4 for l = 2…5; adjacent k ≥ 3 entries ≈ +1e−4). PW type does not decouple them: the decoupling scale is the
dilate scale log(l/k), independent of μ. In the localized family cross terms are negligible (total − trace < 1% at ξ₀ = 6).
The harmonic matrix M = (Q(G_k,G_l))_{k,l≤8} (endpoint data) has eigenvalues −0.0557, −0.0044, then six positive (4.5e−4…1.4e−3):
**restricted to span{G_k: k ≥ 3} it is positive definite.** So (C_G)(b) "on the span of harmonics with free coefficients" is
FALSE; it can only hold because all harmonics come from one ρ with coefficients ≡ 1 (Thm S.1(a): dilates of one function).
**NO-GO (ARGUED; NUMÉRICO falsifier) for the class 𝒦_S^{harm}:** proofs of Q(G,G) ≤ 0 by a per-harmonic sign plus
decoupling/almost-orthogonality of k ≠ l (with any polynomial loss in μ).

## 5. S.5 — where the sign actually comes from (ARGUED)
Summing the diagonal laws with the forced coefficients 1:
- endpoint: Σ_{k≥1}(log k − 1)/k² = −ζ′(2) − ζ(2) = 0.93755 − 1.64493 = −0.70739 < 0, total ρ(1)²(−0.70739)/(2π²) (+ cross terms,
  which are negative numerically: total −0.0660 vs trace −0.0542 at K = 8);
- localized dual at ξ₀ ≈ N, dilate X̄: G ≈ −C(s)Σ_{k≤N}k^{−s} (a partial zeta sum), weights (2log k − log(X̄N))/k:
  Σ_{k≤N}(2log k − log X̄N)/k = −(γ + log X̄)log N − γlog X̄ + 2γ₁ + o(1) < 0 (γ₁ = −0.0728 Stieltjes; CITED Euler–Maclaurin).
The leading terms (log²N, resp. Σlog k/k² vs Σ1/k²) cancel exactly; the sign is carried by **Euler's constant γ > 0** (and
−ζ′(2)/ζ(2) = 0.570 < 1). NUMÉRICO totals: Q(G,G) = −0.184 (ξ₀ = 6, L = 3, both phases), −0.227 (ξ₀ = 10), −8.6e−5 (ξ₀ = 4, L = 2);
every test negative, polar part ≤ 1e−6 there.

## 6. S.6 — the polar mode (PROVED)
u_pol = ρ₀e^{v/2}1_{v<0}, u_pol^{log} = (ρ₁ + ρ₀v)e^{v/2}1_{v<0} (G_pol^{log} = ρ₁/s − ρ₀/s²). Supports are disjoint from the harmonics,
so the log-pairing vanishes between them:
  Q(G_pol,G_pol) = ρ₀²[(1/2π)∫Θ_∞/(¼+τ²)dτ + 2] − 2ρ₀ρ₁ = **c₀ρ₀² − 2ρ₀ρ₁, c₀ = ψ(3/2) − log π = −1.10824**
((1/2π)∫Θ_∞/(¼+τ²) = c₀ − 2 = −3.10824: J Cor J.4, CITED; NUMÉRICO re-check to 1e−15);
  Q(G_pol, G_k) = ρ₀·ℓ(u_k), ℓ(u) := ⟨Θ_∞e^{v/2}1_{v<0}, u⟩ (only the off-diagonal Γ_ℝ kernel; rank one).
The 2×2 form in (ρ₀,ρ₁) has determinant −1: **indefinite**, so the polar mode is not absorbed by its own sign. Absorption
condition (exact Schur complement): Q(G,G) ≤ 0 ⟺ Q(G_h,G_h) + 2ρ₀ℓ(G_h) + c₀ρ₀² − 2ρ₀ρ₁ ≤ 0 (G_h = harmonic part). It holds in all
tests (endpoint data: −0.301 + 2(−0.105) + (−0.066) < 0). OPEN in general; note ρ₀, ρ₁ are also two of the pole functionals of P.2,
so the polar mode is naturally part of the comparison (C_G)(a), not of (b).

## 7. S.7 — the Λ-ingredient (a_n ≡ 1) made precise
(i) **Poisson duality:** Thm S.1 uses that ℤ is self-dual: the Euler–Maclaurin tail of Σ_{n≤X}1·n^{−w} is again a Dirichlet series
with coefficients 1 in the dual index k (and the k = 0 term is the residue 1, the polar mode). For a_n ≡ 1 replaced by a Beurling
system {n_j} there is no dual lattice: Σ_jδ_{n_j} has no Poisson formula, the defect is not a sum of dilates of one function,
and S.1–S.5 have no object. (ii) **Sign constants:** the totals in S.5 are γ, γ₁, ζ(2), ζ′(2) — Euler–Maclaurin constants of
a_n ≡ 1 in the *dual* index; a dual weight b_k ≢ 1 replaces them by Σb_k²(log k − 1)/k² resp. the Euler constant of (b_k),
whose sign is not forced. (iii) **cΛ (ARGUED):** with the prime part ×c the local weight is log k + (1−2c)log t; endpoint
total Σ(log k + 1 − 2c)/k² = −ζ′(2) + (1−2c)ζ(2) < 0 ⟺ c > ½(1 − ζ′(2)/ζ(2)) = 0.785. So the *negativity* of Q_c(G,G) persists for
c > 1: it does not detect c = 1 (consistent with Q.4: c > 1 is killed by the Toeplitz symbol a_c, not by G). The c = 1
selection lives in (C_G)(a)/the coupling, not in (b).

## 8. Residual (OPEN)
**(★_S)** For ρ ∈ PW_μ constrained: Σ_{k,l≥1}Q(G_k,G_l) + 2ρ₀ℓ(Σ_kG_k) + c₀ρ₀² − 2ρ₀ρ₁ ≤ −κμ^{−A}dist²(ρ,𝒢̄₁), with G_k the
dilates of Thm S.1(a). Equivalently a statement about F_c of the dual data (§2). The per-harmonic route is closed (S.3–S.4);
what remains is a *global* inequality whose leading terms cancel and whose sign is carried by γ-type constants of ℕ (S.5).
Next object worth testing: (S-dual) of §2 (is Q(G,G) = −𝔔[c] + boundary terms?), which would make (C_G)(b) self-dual.

## 9. Labels
PROVED: S.0, Thm S.1 (a)–(d), the bilinear formula of §2 and its dual form, S.6 (polar form, rank-one coupling).
CITED: Titchmarsh (FE, Euler–Maclaurin), DLMF 8 (incomplete Γ), J Cor J.4 (c₀). ARGUED: local weight log(k/t), endpoint law
(log k − 1)/(2π²k²), S.5 sums, cΛ threshold 0.785, NO-GO 𝒦_S^{harm}. NUMÉRICO: §3–§6 checks (not proofs). OPEN: (★_S),
(S-dual), (C_G). **Do not retry:** per-harmonic negativity of Q(G_k,G_k); decoupling of harmonics k ≠ l by the PW type;
treating harmonic amplitudes as free coordinates. No sign claimed. Row D OPEN.
