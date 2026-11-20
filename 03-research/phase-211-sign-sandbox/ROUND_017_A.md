# Round 017 A — The survivor's coupling vector split into archimedean, comb and Tate parts; the Schur correction and the falsifiers on it

Target (★): λ_A(T) ≥ 0 for every T. Notation of ROUND_008_E, ROUND_012_B, ROUND_015_B: λ = e^T, N = λ², c = 2πN, ψ_k the k-th
prolate of [−λ, λ] (unit norm, even k ↔ even function), d_k = 1 − χ_k, E the summation map, Ψ_f = 𝒯(ℱf) the Poisson tail of
Ef on (−∞, −T), Φ_f(x) = e^{x/2}Σ_{n≥1} f(ne^x) on ℝ (so Ef = Φ_f − Ψ_f on ℝ, Φ_f radical for 𝒲 when f(0) = ℱf(0) = 0).
Conventions of tools/galerkin_mp.py: v_n = 2Λ(n)/√n, c^sym(u) = ½(⟨F, G(·−u)⟩ + ⟨F, G(·+u)⟩),
Arch(F, G) = C_0⟨F, G⟩ + ∫_0^∞(c(0) − c^sym(u))K(u)du, Π(F, G) = Σ_n v_n c^sym(log n), K(u) = 1/(2 sinh(u/2)) + 1/(2 cosh(u/2)).
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 0. Corpus check
Read: ROUND_015_B (§1.2 low-block matrix, §3.5 Schur restatement, §4.2 two-threshold model, next step), ROUND_008_E (§2.2 Ritz
table, §5 (5.1) and c-table, Prop 5.1), ROUND_012_B (Thm 1.1, M = S𝒢S), ROUND_015_A (Thm 3.1 comb collapse on tails), ROUND_001_B
(Thm 1.1 radical lemma, Cor 1.2), ROUND_016_B (dilation form, complete tail form with the polar term 2A(Ψ)B(Ψ)), tools/README.md. Index rows P211-15A, P211-15B (do-not-retry lists: the sign in the low-block
ledger, in the prolate-asymptotic expansion of the entries, in the window atoms on the tail; "comb averages out along chirps";
"long-range band = radical correction"). Phase 199 memos cited there (SYNTHESIS_MECHANISM_001 §3.3, PROOF_L_SHARP_X_001 Lemma X.4,
PROOF_L_SHARP_Z_001 Thm C, PROOF_L_SHARP_S_001 §5, PROOF_L_SHARP_FF_001 Constraint 25).
What differs. (i) Object: not the low block (15B) nor the high block (14A/15A) but the off-diagonal vector b(G) = a_T(Ef_*, G)
of the survivor against the complement of Ef_* in P_T, and its Schur functional bᵀC⁻¹b; no memo of record computes it or splits
it by the three terms of the form. (ii) The split is done exactly, through the radical identity applied bilinearly (§1), not by
asymptotics. (iii) The falsifiers are run on the vector, not on the block bottom. No equivalence of (★) with another statement
is used; no zero data.

## 1. Exact form of the coupling vector (PROVED, given the radical lemma; domain caveat as in ROUND_015_B §1.2)

Setting. f_* = Σ_{k∈{0,2,4,6,8}} a_kψ_k spans the kernel of f(0), ℱf(0), A(Ef), B(Ef) (computed in multiprecision: the
constraint matrix has singular values 2.8, 1.9, 0.49, 0.090, 4·10⁻⁸⁸ at T = 1; the survivor is
f_* = 0.1037ψ_0 − 0.7340ψ_4 + 0.6712ψ_8 with |a_2|, |a_6| ≤ 10⁻¹³ — only the ℱ-even prolates enter, as ROUND_008_E §2.2(ii)).
F := Ef_*/‖Ef_*‖ ∈ P_T, H := P_T ⊖ F, b(G) := a_T(F, G) for G ∈ H, ρ := a_T(F), C := a_T|_H.

**Proposition 1.1 (Schur form of λ_A; PROVED, standard).** For λ < inf spec C,
    λ_A(T) ≥ λ  ⟺  ρ − λ − sup_{G∈H, G≠0} b(G)² / (a_T(G) − λ‖G‖²) ≥ 0,
and λ_A = ρ − bᵀ(C − λ_A)⁻¹b when λ_A < inf spec C (secular equation). At λ = 0: (★) at T ⟺ C ⪰ 0 and
    ρ ≥ sup_{G∈H} b(G)²/a_T(G).                                                                           (1.1)
*Proof.* Write G′ = αF + G, minimise a_T(G′) − λ‖G′‖² over α for fixed G (a quadratic in α with leading coefficient
ρ − λ, positive if the claim is to hold), then over G. ∎ ("low-block value − Schur correction ≥ 0" is (1.1).)

**Proposition 1.2 (the three parts of b; PROVED for admissible f with f(λ) = 0, ARGUED for the survivor).**
For f admissible (f(0) = ℱf(0) = 0) put Ψ = Ψ_f on (−∞, −T) and Φ = Φ_f, so Ef = Φ − Ψ on ℝ. For every G ∈ P_T:
  (a) Tate part: A(Ψ)B(G) + B(Ψ)A(G) = 0 (A(G) = B(G) = 0; the line functionals restricted to window functions are those of P_T).
  (b) W_T(Ef, G) = a_T(Ef, G) = −𝒲(Ψ, G) (Φ is in the radical of 𝒲, ROUND_001_B Thm 1.1; A(Ef) = B(Ef) = 0).
  (c) Since Ψ and G have disjoint supports, c_{ΨG}(0) = 0 and only the leftward shifts of G meet Ψ:
    b(G) = ∫_0^∞ h_G(u) dν(u),   h_G(u) := ⟨Ψ, G(· + u)⟩ = ∫_{−T}^{min(T, u−T)} Ψ(y − u)G(y)dy,
    ν := ½K(u)du + Σ_{n≥2} Λ(n)n^{−1/2} δ_{log n}                                                         (1.2)
  with archimedean part b_arch(G) = ½∫K h_G du = −𝒜_∞(Ψ, G), comb part b_comb(G) = Σ_n Λ(n)n^{−1/2}h_G(log n) = 𝒞(Ψ, G),
  and b_Tate ≡ 0. The comb part runs over ALL prime powers (h_G(log n) ≠ 0 for every n), with the overlap truncated at
  u − T for n < N and full for n > N; it is not collapsed (the collapse Λ ∗ 1 = log of ROUND_015_A needs both arguments
  to be tails).
  (d) If moreover G = Eg with g admissible, then b(Eg) = 𝒲(Ψ_f, Ψ_g) (tail–tail; apply (b) twice), and in this form the
  comb collapses to the weight (Λ ∗ 1)(N) = log N on dilate pairs and the Tate term A(Ψ_f)B(Ψ_g) + B(Ψ_f)A(Ψ_g) is present
  and nonzero. Hence on E-images
    ∫_0^∞ h_{Eg} dν = 𝒲(Ψ_f, Ψ_g),                                                                          (1.3)
  a second-level radical identity: the left side is a difference of two terms of size ‖Ψ_f‖‖Eg‖ (window–tail), the right
  side is of size ‖Ψ_f‖‖Ψ_g‖ = O(√(d_f d_g)).
*Proof.* (a)–(c): definitions of the galerkin_mp conventions (c^sym, K, v_n = 2Λ(n)/√n) and (b). (d): (b) with the roles
exchanged, Eg = Φ_g − Ψ_g, Φ_g radical, then ROUND_015_A Thm 3.1 bilinearly. ∎
The window split of the same vector is b = b_Arch − b_Π with b_Arch(G) = Arch(F, G), b_Π(G) = Π_T(F, G); by (b),
b_Π = b_Arch + 𝒲(Ψ, ·), i.e. both are O(1) and equal up to O(√d_8) (bilinear form of the identity (3.1) of ROUND_015_B).
Survivor caveat: f_*(λ) ≠ 0, Ψ has jumps (a sawtooth tail); (b) is used in the mollified limit (ROUND_015_B §1.2, ARGUED).

**Proposition 1.3 (parity defect of the survivor; PROVED).** For f admissible, Ef(−t) = E(ℱf)(t) (Poisson summation with
f(0) = ℱf(0) = 0). For f = Σ_{k∈{0,4,8}} a_kψ_k (ℱ(ψ_k1) = i^k√χ_kψ_k = √χ_kψ_k on the band) the odd part of Ef is
    F_odd = ½(Ef − E(ℱf)) = ½E(Σ_k a_k(1 − √χ_k)ψ_k) − ½E(u·1_{(λ,∞)}),   u := ℱ(f1_{[−λ,λ]}),
i.e., up to O(d_8), minus one half of the summation-map image of the survivor's own out-of-band datum. Its norm is O(√d_8),
the same order as the bottom; the even minimiser of the sector has no such component, so its energy is part of
"ρ − λ_A". (No sign content: Λ-free.)

## 2. Numerics (NUMERICAL; T = 0.8, Nb = 90 and T = 1.0, Nb = 160, 40 digits, cached Galerkin matrices)

Method. Survivor and edge data: tools/schur_coupling_survivor.py (prolates as in prolate_eproj.py; the four constraints
exactly, (3.0) of ROUND_008_E for A, B; Frobenius series of the prolate ODE at t = 1; the scale u_k = (−1)^{k/2}√(2π/c)λ^{1/2}
φ_k(ξ/λ) checked against the Bessel series to 10⁻³²). Galerkin Schur: tools/schur_coupling_galerkin.py (F = P·trunc Ef_*,
Householder complement in P_T, both sectors). Tail: tools/schur_coupling_tail.py (u from the prolate ODE to ξ = 8πλ³, edge
asymptotic series of 14 orders and Bernoulli closed forms beyond; Ψ checked against the finite Poisson sum
e^{x/2}Σ_n f_*(ne^x) in 70 digits to 7 digits at three depths; comb over all 465 prime powers n ≤ 2971; archimedean part
by the series K(u) = 2Σ_j e^{−(2j+½)u} against closed-form sine transforms). Split and falsifiers:
tools/schur_coupling_split.py. Note: the vectors of prolate_eproj.py carry a factor λ^{1/2} (prolates unnormalised on
[−λ, λ]); harmless for directions, corrected for the tail normalisation.

### 2.1 Reproduction of the recorded numbers
| T | ρ/λ_A (Galerkin, survivor in all of P_T) | b^TC⁻¹b / ρ (Galerkin) | X of the 5-block (15B §4.2) |
|---|---|---|---|
| 0.8 | 1.578 | 0.366 | 34.0 |
| 1.0 | 1.489 | 0.329 | 211.8 |
Secular check ρ − bᵀ(C − λ_A)⁻¹b − λ_A = 10⁻⁵⁷. The 33–37 % of ROUND_015_B is reproduced, and so is X ≈ 210.

### 2.2 The three-term split (task (1))
| T | |b| | window: |b_Arch|, |b_Π| | tail: |b_arch|, |b_comb| | Tate |
|---|---|---|---|---|
| 0.8 | 1.93·10⁻⁶ | 0.3217, 0.3217 | 4.8·10⁻⁸, 1.9·10⁻⁶ | 0 |
| 1.0 | 3.49·10⁻¹² | 0.3331, 0.3331 | 3.7·10⁻¹⁴, 3.46·10⁻¹² | 0 |
Shares of bᵀC⁻¹b (units of ρ): window split Arch–Arch = Π–Π = +1.6·10¹⁶ (T = 0.8), +3.2·10³⁸ (T = 1), cross −2× that;
tail split arch–arch ≈ comb–comb = +126 (T = 0.8), +8.4·10¹¹ (T = 1), cross −2× that. Tate share 0.
Agreement of the tail vector (exact survivor) with the Galerkin vector (truncated survivor): 26 % (T = 0.8), 12 % (T = 1)
in norm; enlarging the sine space 160 → 220 for the survivor moves the Galerkin components on the near-null rungs toward
the tail values (rung 1: 3.9 → 3.0 against 1.0, ×10⁻²¹), i.e. the residual is the slow (∼1/k) sine convergence of the
jumpy Ef_*, not the tail evaluation.
Reading. No single part gives the 33–40 %: in either split the two nonzero parts are individually 10²–10³⁸ times the
Schur correction and cancel. In norm the comb part dominates the tail split (|b_comb|/|b_arch| ≈ 40–90); on the stiff
directions (μ ≳ 0.1) comb is the whole vector; on the near-null directions arch and comb cancel.

### 2.3 Where the Schur correction sits: by complement direction
Eigen-resolution of C (T = 1; μ = eigenvalue, share = (v·b)²/(μρ); cancellation = |v·b|/|v·b_comb| in the tail split):
| μ | sector | share (Galerkin) | share (tail) | v·b_arch | v·b_comb | cancellation |
|---|---|---|---|---|---|---|
| 9.1·10⁻²¹ | odd | 9·10⁻²⁵ | 6·10⁻⁴ | −4.27·10⁻¹⁶ | +4.27·10⁻¹⁶ | 2.7·10⁻⁸ |
| 1.2·10⁻¹⁷ | ev | 0.053 | 0.0037 | −1.785·10⁻¹⁵ | +1.785·10⁻¹⁵ | 5.7·10⁻⁷ |
| 1.3·10⁻¹² | ev | 0.049 | 0.0058 | +3.07·10⁻¹⁵ | −3.07·10⁻¹⁵ | 1.4·10⁻⁴ |
| 3.8·10⁻⁸ | ev | 0.025 | 0.0037 | +6.5·10⁻¹⁵ | −6.6·10⁻¹⁵ | 8.9·10⁻³ |
| 2.2·10⁻⁴ | ev | 0.0046 | 7·10⁻⁶ | −1.04·10⁻¹⁴ | +1.02·10⁻¹⁴ | 0.019 |
| 0.17 | ev | 4·10⁻⁴ | 6·10⁻⁴ | −1.8·10⁻¹⁴ | −3.1·10⁻¹⁴ | 1.6 |
Sector totals:
| T | Galerkin: even, odd | tail (exact survivor): even, odd |
|---|---|---|
| 0.8 | 0.241, 0.126 | 0.061, 0.125 |
| 1.0 | 0.169, 0.159 | 0.048, 0.163 |
(i) Parity defect (odd sector): 0.126 (T = 0.8), 0.16 (T = 1) of ρ, the same in both representations (to 0.2 % and 2 %).
It is not carried by an odd near-null eigenvector (their shares are ≤ 6·10⁻⁴) but spread over the stiff odd directions:
it is the energy of the survivor's odd component F_odd of Proposition 1.3, removed when the bottom is projected to the even
sector. (ii) Even sector: the coupling to the next even near-null rungs (μ ≈ 1.2·10⁻¹⁷, 1.3·10⁻¹², 3.8·10⁻⁸ at T = 1 — the
Eψ_12-, Eψ_16-, … type directions of the ladder κ(1 − χ_{4j+8}) of ROUND_009_B — identification by eigenvalue scale only, ARGUED; 6·10⁻⁷, 3.3·10⁻³ at T = 0.8): Galerkin
0.17–0.24, tail 0.05–0.06 of ρ — representation-dependent (the Galerkin vector is the truncated survivor). Stiff directions:
< 1 %. On every rung the archimedean and comb parts cancel with ratio 5.7·10⁻⁷, 1.4·10⁻⁴, 8.9·10⁻³ (T = 1), 0.07, 0.68
(T = 0.8): the rung coupling is the second-level identity (1.3), of order √(d_8d_g) (as γ_k = O(√(d_kd_8)) of ROUND_009_B).
Dominant part, answer to (1): none of arch / comb / Tate. By direction: about half (0.13–0.16 ρ) is the parity defect of the
survivor (Λ-free, Proposition 1.3), the rest is the tail–tail coupling 𝒲(Ψ_{f*}, Ψ_g) to the even rungs, whose comb is
the collapsed log N weight. The 33–40 % is therefore not a comb-versus-archimedean competition at all.

## 3. Falsifiers on the vector (task (2))

**Proposition 3.1 (where a weight change enters; PROVED).** For the weight cΛ (window form a^c_T = a_T + (1 − c)Π_T on P_T):
    ρ^c = ρ + (1 − c)Π_T(F),   C^c = C + (1 − c)Π_T|_H,   b^c = b_arch + c·b_comb + (1 − c)X,
    X(G) := Π_T(F, G) + b_comb(G) = 𝒞(Φ, G) = 𝒜_∞(Φ, G)   (G ∈ P_T),
X the radical defect: the comb (equivalently archimedean) pairing of the WHOLE-LINE function Φ_{f*} with G.
*Proof.* 𝒲^c = 𝒲 + (1 − c)𝒞. b^c(G) = 𝒲^c(Φ, G) − 𝒲^c(Ψ, G) = (1 − c)𝒞(Φ, G) + b_arch(G) + c𝒞(Ψ, G), using 𝒲(Φ, ·) = 0
and Tate(Φ, G) = 0. 𝒞(Φ, G) = 𝒞(Ef, G) + 𝒞(Ψ, G) = Π_T(Ef, G) + b_comb(G) (shifts of G to the right miss Ψ; on the window
the comb is Π_T). 𝒜_∞(Φ, G) = 𝒞(Φ, G) by the radical identity. ∎
For a_P the same holds with (1 − c)𝒞 replaced by 𝒞_{Λ1_{p<P}}; for a finite modification e by −𝒞_e. In every case the tail
parts change by O(√d_8)·(size of the change) while X is O(1): |X| = 0.3217 / 0.3331 (T = 0.8 / 1), |b_comb| ≤ 2·10⁻⁶ / 3.5·10⁻¹²,
so X = Π_T(F, ·) to 6 / 12 digits. The part whose change kills positivity is X, not any part of b.

NUMERICAL (full even Galerkin bottom, complement-block bottom, survivor diagonal):
| T | c | bottom | bottom of C^c | ρ^c |
|---|---|---|---|---|
| 1.0 | 1 − 10⁻⁴ | −4.5·10⁻⁵ | −2.6·10⁻⁵ | +3.3·10⁻⁶ |
| 1.0 | 1 + 10⁻⁴ | −1.08·10⁻⁴ | −1.08·10⁻⁴ | −3.3·10⁻⁶ |
| 1.0 | 1 − 10⁻¹⁶ / 1 − 10⁻¹⁸ | −1.6·10⁻¹⁷ / +2.6·10⁻²⁰ | +3.1·10⁻¹⁷ / +1.2·10⁻¹⁷ | |
| 1.0 | 1 + 10⁻²⁰ / 1 + 10⁻²² | −3.2·10⁻²² / +1.3·10⁻²³ | | |
| 0.8 | 1 − 10⁻⁴ | −1.5·10⁻⁵ | +2.6·10⁻⁵ | +6.3·10⁻⁶ |
| 0.8 | 1 + 10⁻⁴ | −4.7·10⁻⁵ | −2.6·10⁻⁵ | −6.3·10⁻⁶ |
| 0.8 | 1 − 10⁻⁶ / 1 − 10⁻⁸ | −3.6·10⁻⁸ / +6.3·10⁻¹⁰ | +8.6·10⁻⁷ / +6.0·10⁻⁷ | |
| 0.8 | 1 + 10⁻¹⁰ / 1 + 10⁻¹² | −3.8·10⁻¹³ / +5.9·10⁻¹² | | |
Readings. (i) c > 1 dies at first order at |1 − c| ≈ λ_A/Π_T(F) (5·10⁻²² at T = 1, 10⁻¹⁰ at T = 0.8), on the diagonal
ρ^c and on every near-null rung at once (C^c goes negative with the same value): Π_T = 𝒜_∞ > 0 on each of them.
(ii) c < 1 survives first order and dies at second order through the survivor–rung coupling (1 − c)X(v_g) against the
next rung μ_g: threshold ≈ Π_T(F)μ_g/X(v_g)², observed between 10⁻¹⁸ and 10⁻¹⁶ at T = 1 (rung μ = 1.2·10⁻¹⁷) and between
10⁻⁸ and 10⁻⁶ at T = 0.8 (rung μ = 6·10⁻⁷), with C^c still positive there. CORRECTION to ROUND_015_B §4.2: the c < 1
threshold 1.5·10⁻⁴ and X ≈ 210 belong to the five-prolate block, which lacks the next rung; X = 211.8 is reproduced and
comes entirely from one block eigenvector (μ = 5.2·10⁻⁴, term 211.8; T = 0.8: μ = 3.0·10⁻³, term 34.0), with
Π_T(F_b, g)² = 0.11, i.e. X is pure radical defect. On the full space the c < 1 threshold is of the size of the next rung.
At c = 1 ± 10⁻⁴ (the values asked) everything is already dead, including the complement block alone.
(iii) a_3 (atoms 2, 4 removed): ρ^{(a_3)} = ρ + Π^{(2)}_T(F) = −0.0122 at T = 1 (diagonal kill at first order) and +0.0352 at
T = 0.8 (survivor positive, the complement kills: full even bottom −0.506); |Π^{(2)}_T(F, ·)| = 0.58–0.63 against the
p = 2 part of b_comb of size 10⁻¹²–10⁻⁶. Again the radical defect, not the coupling vector.

## 4. The Schur correction exactly, and its structure (task (3))

### 4.1 The inequality in its most explicit form (PROVED reduction; ARGUED for the survivor's domain)
With Ψ_* := Ψ_{f*}/‖Ef_*‖, ρ = 𝒲[Ψ_*] (ROUND_015_B Cor 1.2 reading), Proposition 1.1 and 1.2 give: (★) at T holds iff
C ⪰ 0 and, for every G ∈ P_T with ⟨G, Ef_*⟩ = 0,
    ( ½∫_0^∞K(u)⟨Ψ_*, G(·+u)⟩du + Σ_{n≥2}Λ(n)n^{−1/2}⟨Ψ_*, G(·+log n)⟩ )²  ≤  𝒲[Ψ_*] · a_T(G).            (4.1)
Three pieces of the left side, by the numerics of §2:
  (P) parity: G = F_odd/‖F_odd‖ direction: the left side is the odd component's energy (Proposition 1.3), share
      0.13–0.16 of ρ — Λ-free (prolates, E, u only).
  (R) rungs: G = Eg, g admissible (next ladder directions): by (1.3) the left side is 𝒲(Ψ_*, Ψ_g)², and (4.1) restricted to
      span{Ef_*, Eg} reads 𝒲(Ψ_*, Ψ_g)² ≤ 𝒲[Ψ_*]·𝒲[Ψ_g]: Cauchy–Schwarz for the tail form on the pair of tails, i.e. 2×2
      positivity of the tail Gram 𝒢 of ROUND_012_B/014_A on {Ψ_*, Ψ_g}. Entrywise (ROUND_015_A Cor 3.2, bilinear):
      𝒲(Ψ_*, Ψ_g) = Σ_{N,N′}[𝒜_∞(F_N^{*}, F_{N′}^{g}) − (log N + log N′)⟨F_N^{*}, F_{N′}^{g}⟩] + A(Ψ_*)B(Ψ_g) + B(Ψ_*)A(Ψ_g),
      F_N the N-th dilates u(Ne^{−x})e^{−x/2}1_{x<−T}; the comb atoms enter only through (Λ ∗ 1)(N) = log N on exact dilate
      coincidences, the Lévy kernel through 𝒜_∞ of dilate pairs, the prolate overlaps through ⟨F_N^{*}, F_{N′}^{g}⟩
      (out-of-band overlaps of the Langer chirps of ψ_8 and ψ_{12}, …). Share 0.05–0.24 of ρ (representation-dependent).
  (S) stiff and high directions (not E-images of low prolates): the left side is the window–tail pairing (1.2) with the
      full uncollapsed comb over all prime powers; share < 1 %.
So the sign competition at order d_8 is: ledger 𝒲[Ψ_*] against (P) + (R) + (S), and (R) is a statement about the tail Gram
alone.

### 4.2 Comb-genericity (falsifier test, rule 4)
- (P) is comb-free: it survives every falsifier unchanged. Not a sign step.
- (R) in tail form depends on the weight only through the collapsed weight (w ∗ 1)(N). For cΛ it becomes c·log N, for a_P
  log N minus the P-smooth divisor sums, for finite e a finite change — and the diagonal ledger 𝒲^w[Ψ_*] is robust for c < 1
  and small modifications (ROUND_015_B §3.4). Whether the off-diagonal tail Gram inequality survives c log N is not computed
  here (OPEN); if it does, (R) in tail form is not a sign step either. What certainly fails for w ≠ Λ is the passage from
  (4.1) to its tail form: identities (1.2)(b) and (1.3) require Φ_f to be radical, and for w ≠ Λ they acquire the radical
  defect X_w = 𝒞_{Λ−w}(Φ_{f*}, ·) of §3, of size O(1).
- (S) carries the uncollapsed comb but is < 1 % of the correction at both windows.
Conclusion (ARGUED from §2–3): no part of the Schur inequality is a comb-specific sign step by itself; the Λ-specificity
sits, again, in the identity (now at second level, (1.3)) that turns the window coupling into a tail–tail coupling. Every
falsifier dies through X (first order for c > 1, a_3 at T = 1; second order through the next rung for c < 1).

## Result
PIVOT with reason, plus PROVED pieces.
Reason: the Schur correction (33–37 % of the low-block value on the Galerkin survivor) is not produced by any one of the
three terms of the form. The Tate part of the coupling vanishes identically on P_T; the archimedean and comb parts are each
10²–10³⁸ times the correction (depending on the split) and cancel. By direction, the correction is (P) the energy of the
survivor's odd component (0.13–0.16 ρ, Λ-free, identical in both representations) plus (R) the tail–tail coupling to the
next even rungs (0.05–0.24 ρ, representation-dependent), where the coupling is a second-level radical identity and the comb
is the collapsed weight log N. The falsifiers kill through the radical defect X = 𝒜_∞(Φ_{f*}, ·) = Π_T(Ef_*, ·) + O(√d_8),
not through any part of b.

### What was proved
- Proposition 1.1: Schur/secular form of λ_A at the survivor; (★) ⟺ C ⪰ 0 and (1.1).
- Proposition 1.2: b(G) = ∫h_G dν with ν = ½K du + Σ_{n≥2}Λ(n)n^{−1/2}δ_{log n} (all prime powers, uncollapsed), b_Tate ≡ 0 on
  P_T; on E-images b(Eg) = 𝒲(Ψ_f, Ψ_g) (collapsed comb, Tate present): second-level radical identity (1.3).
- Proposition 1.3: odd part of Ef for f ∈ span{ψ_0, ψ_4, ψ_8} = −½E(u1_{(λ,∞)}) + O(d).
- Proposition 3.1: under cΛ, a_P, finite e, the vector changes by the radical defect X_w = 𝒞_{Λ−w}(Φ_{f*}, ·), O(1); tail
  parts change by O(√d_8).
NUMERICAL (T = 0.8, 1.0): reproduction of ρ/λ_A = 1.58 / 1.49, Schur share 0.366 / 0.329, X = 34 / 211.8; tables of §2.2–2.3
and §3; c > 1 threshold λ_A/Π_T(F) (first order, 5·10⁻²² at T = 1); c < 1 threshold of the size of the next rung
(10⁻¹⁸–10⁻¹⁶ at T = 1, 10⁻⁸–10⁻⁶ at T = 0.8), correcting the block value 1.5·10⁻⁴ of ROUND_015_B; a_3 kills on the diagonal
(T = 1) or in the complement (T = 0.8).

### What failed and why
- The hypothesis of ROUND_015_B §3.5 that the correction is "comb-dependent window–tail cross terms" competing with a
  comb-robust ledger: the cross terms are arch–comb cancellations; half of the correction is a Λ-free parity defect and the
  other half is a tail–tail (tail Gram) coupling.
- The block model of the c < 1 falsifier (threshold 1.5·10⁻⁴): an artefact of the five-prolate block.
- The even-rung share is not resolved: Galerkin (truncated survivor) 0.17–0.24 ρ versus tail (exact survivor) 0.05–0.06 ρ_Gal;
  the exact ledger ρ = 𝒲[Ψ_*] of the exact survivor was not computed, so the exact survivor's Schur balance is OPEN.

### Next concrete step
Compute the tail Gram on the pair (Ψ_*, Ψ_g) for the first two rungs g (the admissible combinations of ψ_0 … ψ_16 that
carry the complement eigenvectors μ ≈ 1.2·10⁻¹⁷ and 1.3·10⁻¹² at T = 1) entrywise in dilate coordinates, together with the
exact ledger 𝒲[Ψ_*]; check the 2×2 and 3×3 Schur complements against λ_A; then repeat with the collapsed weight c·log N,
c = 1 ± 10⁻⁴ — if the tail-form inequality survives c < 1 it is not a sign step (rule 4) and the rung part is closed as
comb-robust.

## Index row and ledger line
Index (05-meta-and-planning/ROUTES-TRIED-INDEX/README.md): row P211-17A. Ledger (LEDGER.md): line C35.
