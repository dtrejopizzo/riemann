# Round 008 D — The Schur coupling of the comb-response family E_T: rank profile, Neumann expansion in the comb, and the degree at which a truncation carries the sign

Target (★): λ_A(T) ≥ 0 for every T (STATEMENT_001). Object: E_T = N′ ⊕ V_T of ROUND_005_C Definition 1 (with
REVIEW_004 §1 corrections), its complement E_T^c = P_T ∩ E_T^⊥, and the exact Schur complement
S_E = a_EE − a_EC a_CC^{−1} a_CE of ROUND_005_C Theorem 2. Predecessors: ROUND_007_E (E_T in multiprecision at
N = 120), ROUND_008_A (the same Neumann mechanism on the archimedean spectral band). Labels: PROVED / CITED /
CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL. No equivalence of (★) with any other statement is used; nothing
is reduced to zeros.

Notation. On one parity sector of P_T: A := a_T = Arch − Π; for subspaces X, Y, A_XY := P_X A|_Y, likewise Arch_XY,
Π_XY. E := E_T, C := E_T^c. 𝒞_T := a_EC a_CC^{−1} a_CE (the coupling), so S_E = a_EE − 𝒞_T.

## 0. Corpus check

- ROUTES-TRIED-INDEX: P211-7E (E_T in mp, capture NO-GO, "sign lives in the Schur coupling"; next step = this
  memo), P211-8A (Neumann expansion in the comb on the archimedean spectral band B_t, Prop. 3.1 tail bounds,
  Cor. 3.2 degree count), C3/C18 floor-only Schur class (NO-GO: scalar replacement of A_𝒞𝒞^{−1} loses alignment),
  POLAR_CAP_001 (bordered Schur inverting a_T on P_T: consumes λ_A > 0), W-det/W-mom (finite Schur matrix S_{T,k}
  attacked by norms/determinants/moments).
- What differs. (a) The split is E_T ⊕ E_T^c with E_T comb-generated (block + Π-responses), not an archimedean
  spectral band: Arch is NOT block-diagonal in this split, so a_EC carries an archimedean part on N′ and a comb part
  on V_T, and the Neumann series runs in the compressed archimedean operator Arch_CC, which is not diagonal.
  (b) The question asked is not coercivity of a fixed block (C3, floor class) but the full coupling, kept
  exactly to degree K; nothing is replaced by a scalar. (c) The point tested is whether the comb-generated
  E_T lowers the degree K* needed to carry the sign relative to the spectral band of ROUND_008_A; the recorded
  failure (precision ≈ λ_A demanded of every finite-degree truncation) is exactly what is measured.

## 1. Structure of the coupling and the Neumann expansion (PROVED / CONDITIONAL)

**Proposition 1 (what a_CE is). [PROVED]** a_CE = Arch_CE − Π_CE P_V, where P_V is the orthogonal projector of E
onto V_T. In words: on N′ the coupling is purely archimedean, on V_T it carries the comb.
Proof. ROUND_005_C Theorem 2(iii): for x ∈ N′, P_C A x = P_C Arch x; for y ∈ V_T, P_C A y = P_C(Arch − Π)y. ∎

Correction recorded. The statement "a_EC = Arch_EC exactly" holds on N′ only. On V_T, Π_CV ≠ 0: NUMERICAL
‖Π_{C,N′}‖_F ≤ 10⁻⁴⁹ (the identity, at working precision) against ‖Π_{C,V}‖_F ≈ 1.9–2.4 at T = 1.0, 1.2 (§2).
The responses V_T = P_𝒞Π(𝒩_η + 𝒯) absorb Π of the block, but Π of the responses (second responses Π P_𝒞 Π φ_q)
leaks to C at O(1). This is the mechanism by which the coupling contains every power of Π below.

**Theorem 2 (Neumann expansion on E_T^c). [PROVED under (H₋); (H₋) NUMERICAL]** Assume
  (H₊) a_CC = Arch_CC − Π_CC ≻ 0 on C, and
  (H₋) Arch_CC + Π_CC ≻ 0 on C,
and Arch_CC ≻ 0. Put X := Arch_CC^{−1/2} Π_CC Arch_CC^{−1/2} (self-adjoint, compact when Arch has compact resolvent),
r_± := max(0, ±sup/inf spec X), r := ρ(X) = max(r_+, r_−). Then:
  (i) spec X ⊂ (−1, 1), r < 1, and a_CC^{−1} = Arch_CC^{−1/2}(1 − X)^{−1}Arch_CC^{−1/2} = Σ_{k≥0} Arch_CC^{−1}(Π_CC Arch_CC^{−1})^k,
      norm-convergent; ‖Π_CC Arch_CC^{−1}‖ measured in the norm ‖Arch_CC^{−1/2}·‖ equals r (the Euclidean norm is not
      the relevant quantity: Π_CC Arch_CC^{−1} = Arch_CC^{1/2} X Arch_CC^{−1/2} is only similar to X).
  (ii) With W := Arch_CC^{−1/2} a_CE (a map E → C),
          S_E = a_EE − Σ_{k≥0} a_EC Arch_CC^{−1}(Π_CC Arch_CC^{−1})^k a_CE = a_EE − Σ_k W* X^k W,
       and S_E^{(K)} := a_EE − Σ_{k=0}^{K} W* X^k W satisfies S_E − S_E^{(K)} = −W* f_K(X) W, f_K(x) = x^{K+1}/(1 − x).
  (iii) (Tails.) With ε_K := max{r_+^{K+1}/(1 − r_+), r_−^{K+1}/(1 + r_−)}:
          S_E^{(K)} − ε_K W*W ⪯ S_E ⪯ S_E^{(K)} + ε_K W*W;   for odd K, S_E ⪯ S_E^{(K)};
       and W*W = a_EC Arch_CC^{−1} a_CE ⪯ ‖a_CE‖²/λ_min(Arch_CC).
  (iv) (Degree.) Freeze the subspaces E, C (they depend on v through the block {q : s_q ≤ 0} and through V_T).
       Then Arch_CC, Arch_EC are v-free and Π is linear in v, so the k-th term W*X^kW, in the blocks
       (N′, N′), (N′, V), (V, V) of E, is a homogeneous polynomial in v of degree k, k + 1, k + 2 respectively, plus
       lower-degree terms from the Arch_CV part of a_CV; S_E^{(K)} is a matrix polynomial in v of degree K + 2.
Proof. (H₊) and (H₋) are ±Π_CC ≺ Arch_CC, i.e. ⟨Xu, u⟩ ∈ (−‖u‖², ‖u‖²) for u ≠ 0 after the substitution
u = Arch_CC^{1/2}w; compactness of X upgrades the strict form inequalities to spec X ⊂ [−r, r] with r < 1. Then
a_CC = Arch_CC^{1/2}(1 − X)Arch_CC^{1/2}, invert, expand (1 − X)^{−1} = Σ X^k (norm-convergent since ‖X‖ = r < 1) and
note Arch_CC^{−1/2}X^kArch_CC^{−1/2} = Arch_CC^{−1}(Π_CC Arch_CC^{−1})^k. (ii) substitute. (iii) is the scalar
estimate of ROUND_008_A Prop. 3.1(iv) applied to f_K on spec X ⊂ [−r_−, r_+], conjugated by W; for odd K, K + 1 is
even and f_K ≥ 0 on (−1, 1). (iv) Proposition 1 and multilinearity of the product a_EC·Arch^{−1}·(Π Arch^{−1})^k·a_CE. ∎

Status of the hypotheses. (H₊) is the floor of ROUND_002_A Theorem F on C ⊂ 𝒞 (ROUND_005_C Theorem 2(i)): PROVED.
(H₋) is NOT proved: it is the coercivity of the archimedean form with the comb added (the form of the sign-flipped
comb −v) on C; the available PROVED bound π_− ≤ ½(A_T + V(T)) (ROUND_006_A) exceeds λ_min(Arch_CC) already at
T = 1 (A_1 ≈ 5.9 against λ_min(Arch_CC) ≈ 2.5), so (H₋) is OPEN; NUMERICAL r_− ≈ 0.48–0.61 (§2).
Without (H₋) the identity (ii) still holds with the series replaced by any polynomial approximation of 1/(1 − x)
on spec X, but the geometric series itself may diverge.

Corollary 3 (degree needed). [PROVED under (H₋)] A truncation S_E^{(K)} certifies the sign of λ_A(T) only if
ε_K‖W*W‖ < λ_min(S_E) = λ_A(T) (the Schur complement carries λ_A exactly), i.e.
     K + 1 ≥ log(‖W*W‖/((1 − r)λ_A(T))) / log(1/r).
Since λ_A(T) decays doubly exponentially (ROUND_007_D, NUMERICAL rate-2 law) and r does not tend to 0
(NUMERICAL r ≈ 0.53 at T = 1.0, 0.61–0.67 at T = 1.2, increasing), the worst-case degree grows at least like
log(1/λ_A(T)), i.e. exponentially in T. This is the same quantitative wall as ROUND_008_A Cor. 3.2(c).


## 2. Numerics at T = 1.0, 1.2, N = 160, 200, block q ≤ N/2 (NUMERICAL)

Setup. tools/galerkin_mp.py at 40 digits; E_T rebuilt per (T, N) from the gauged negative Nyquist block
(gauge c = 0.613 at T = 1.0, −0.140 at T = 1.2) truncated to q ≤ N/2 (a fixed fraction of N, which separates
growth of the block from saturation of the Galerkin space); 𝒞_T and S_E computed exactly in each parity sector;
S_E^{(K)} as in Theorem 2(ii). Every number in this section is NUMERICAL.

### 2.1 Dimensions, coupling spectrum, Schur bottom

| T | N | sector | q kept / full block | dim N′+V = E | dim C | λ_min(a_EE) | λ_min(S_E) = λ_A (sector) | 2nd eig S_E | λ_min(a_CC) | λ_min(Arch_CC) | spec X | ‖Π_{C,V}‖ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.0 | 160 | ev | 14/41 | 14+15 = 29 | 50 | 5.7e-17 | 1.61e-23 | 1.2e-17 | 1.30 | 2.53 | [−0.491, 0.537] | 1.99 |
| 1.0 | 160 | odd | | 13+14 = 27 | 52 | 1.6e-14 | 9.11e-21 | 3.5e-15 | 1.23 | 2.47 | [−0.502, 0.562] | 2.00 |
| 1.0 | 200 | ev | 15/41 | 15+16 = 31 | 68 | 6.2e-17 | 1.50e-23 | 1.1e-17 | 1.32 | 2.53 | [−0.493, 0.541] | 2.20 |
| 1.0 | 200 | odd | | 14+15 = 29 | 70 | 2.0e-14 | 8.67e-21 | 3.4e-15 | 1.26 | 2.47 | [−0.504, 0.555] | 2.12 |
| 1.2 | 160 | ev | 20/127 | 20+21 = 41 | 38 | 4.0e-27 | 1.08e-41 | 5.9e-35 | 1.17 | 2.48 | [−0.530, 0.649] | 2.44 |
| 1.2 | 160 | odd | | 19+20 = 39 | 40 | 5.1e-24 | 1.52e-38 | 6.0e-32 | 1.14 | 2.43 | [−0.539, 0.652] | 2.52 |
| 1.2 | 200 | ev | 23/127 | 23+24 = 47 | 52 | 4.1e-27 | 1.00e-41 | 5.5e-35 | 1.09 | 2.49 | [−0.548, 0.670] | 2.43 |
| 1.2 | 200 | odd | | 22+23 = 45 | 54 | 4.9e-24 | 1.39e-38 | 5.5e-32 | 1.11 | 2.43 | [−0.558, 0.669] | 2.34 |

‖Π_{C,N′}‖ ≤ 6.6e-50 in every row (Proposition 1, to working precision). (H₊) and (H₋) hold in every row
(spec X strictly inside (−1, 1)), so Theorem 2 applies to the Galerkin matrices.

Rank profile of 𝒞_T (eigenvalues of a_EC a_CC^{−1} a_CE on E): top eight at T = 1.0, N = 200 (ev)
0.487, 0.467, 0.363, 0.23, 0.171, 0.073, 0.051, 0.019; counts above 10⁻⁶ / 10⁻¹² / 10⁻²⁰: 12/16/21 of 31
(ev), 11/15/21 of 29 (odd); at N = 160: 10/14/20 of 29 and 10/14/20 of 27. At T = 1.2, N = 200: top 0.59, 0.46,
0.39, 0.27, …; counts 15/20/25 of 47 (ev), 15/20/24 of 45 (odd); at N = 160: 13/18/22 of 41, 13/17/22 of 39.
The coupling is O(1) and full rank to 10⁻²⁰ on ≈ 2/3 of E (T = 1.0) and ≈ 1/2 of E (T = 1.2); its spectrum
decays roughly geometrically, i.e. there is no low-rank coupling.

N-comparison. λ_A per sector moves by ≤ 7% between N = 160 and 200 (1.61→1.50e-23, 1.08→1.00e-41): the
Galerkin bottom is converged to the leading digit only (upper bounds; the N = 120 values of ROUND_007_E
are 1.74e-23, 1.26e-41, consistent with monotone decrease). spec X, λ_min(a_CC), λ_min(Arch_CC) are stable to
≤ 3% between N = 160 and 200; one more block frequency enters at each step (q = 87 at T = 1.0; q = 84, 92, 96
at T = 1.2), i.e. R1 growth is still truncation-limited. The gap λ_min(a_EE) / λ_A is 4e6 (T = 1.0) and 4e14
(T = 1.2): the coupling 𝒞_T removes all but a 10⁻⁶ / 10⁻¹⁴ relative fraction of a_EE in the bottom direction.

## 3. Truncation degree K needed (NUMERICAL; worst case from Corollary 3)

λ_min(S_E^{(K)}) for the true comb (ev sector; odd sector qualitatively identical):

| K | T=1.0 N=160 | T=1.0 N=200 | T=1.2 N=160 | T=1.2 N=200 |
|---|---|---|---|---|
| 0 | −1.5e-15 | −2.3e-15 | −3.5e-10 | −8.8e-10 |
| 1 | +6.6e-18 | +6.3e-18 | +4.9e-28 | +3.8e-28 |
| 2 | −1.8e-16 | −3.0e-16 | −2.2e-12 | −9.7e-12 |
| 4 | −2.7e-17 | −5.6e-17 | −2.4e-13 | −1.4e-12 |
| 6 | +6.4e-20 | −4.6e-18 | −3.4e-15 | −2.2e-13 |
| 10 | +2.8e-20 | +1.2e-20 | −6.4e-20 | −4.3e-16 |
| 20 | +6.2e-23 | +2.6e-23 | −3.8e-24 | −7.7e-23 |
| resolves λ_A to 10% | K* = 30 | 25 | 105 | 125 |

(odd sector: K* = 25, 25, 115, 120.) Readings.
(a) Even K < K₀ gives a NEGATIVE minimum (K₀ = 6 at T = 1.0, ≈ 20–40 at T = 1.2): low truncations do not
merely miss λ_A, they have the wrong sign. Odd K gives a positive minimum, but by Theorem 2(iii) odd K only
yields S_E ⪯ S_E^{(K)}, an upper bound: its positivity is necessary, not sufficient, and carries no sign.
(b) The term-by-term expansion on the bottom vector u of S_E (T = 1.0, N = 160, ev; ‖u_N′‖ = 1,
‖u_V‖ = 6.7e-3): ⟨u, a_EE u⟩ = 5.96e-16, the k = 0 term cancels it to 3.1e-18, and the partial sums then
oscillate (k odd terms of alternating sign) and reach λ_A = 1.611e-23 to 4 digits at k = 40. The NN, NV, VV
block contributions of each term are ±1e-8 … 1e-13 and cancel against each other to 1e-17 … 1e-22 (relative
cancellation 1e-9 per term): the sign is a cancellation of degree-k, k+1, k+2 polynomials in v at every order.
(c) Worst-case degree certifying the sign from the tail bound (Cor. 3 with ‖W*W‖ ≈ 0.5–1): K ≥ 84 / 80
(T = 1.0, ev/odd), K ≥ 220 / 205 (T = 1.2). Polynomial degree in v: K + 2 ≈ 86 at T = 1.0, ≈ 222 at T = 1.2.
The ratio between T = 1.2 and T = 1.0 (≈ 2.6 in K, measured and worst-case) follows log(1/λ_A).

Falsifiers (T = 1.0 and 1.2, N = 160; exact S_E and S_E^{(K)}, K = 0…7):

| comb | T = 1.0 ev / odd: λ_min S_E | S^{(K)}, K = 0..7 | T = 1.2 ev / odd | S^{(K)} |
|---|---|---|---|---|
| 1.01Λ | −0.01381 / −0.01274 | constant to 4 digits | −0.01850 / −0.01866 | constant to 3–4 digits |
| 1.1Λ | −0.1413 / −0.1458 | constant | −0.1961 / −0.1901 | constant to 3 digits |
| a_3 | −0.5346 / −0.5230 | constant | −0.5387 / −0.5483 | constant |

Every falsifier is rejected at K = 0 (S^{(0)} already O(1) negative with tail ε_0‖W*W‖ ≲ 0.5 · 0.6 well
below |λ_min| only for a_3; for 1.01Λ the honest certificate K is the one with ε_K‖W*W‖ < 0.0138, i.e.
K ≈ 7, matching ROUND_008_A). The falsifiers are therefore cheap; the true comb is expensive: the degree
gap is K ≈ 7 (reject 1.01Λ) against K ≈ 84 (accept Λ) at T = 1.0, and the gap grows with T. The falsifier test
of the BRIEF is passed by the expansion as a whole (the exact S_E is comb-specific), but any finite truncation
that rejects 1.01Λ cheaply is not by that fact sign-carrying for Λ.

## 4. The explicit finite polynomial inequality at T = 1.0 (PROVED as a sufficient condition; NUMERICAL status)

**Proposition 4. [PROVED, conditional on (H₋) on the frozen C]** Fix T = 1, the Galerkin space P_T^{(N)}, the
gauged block 𝒩 (fixed set of q) and hence N′; freeze V and C at their Λ-values. Let v = (v_2, v_3, v_4, v_5, v_7)
(n < e² ≈ 7.39) enter only through Π = Σ_n v_n Π_n (each Π_n an explicit matrix). Define, per parity sector,
   𝒫_K(v) := a_EE(v) − Σ_{k=0}^{K} a_EC(v) Arch_CC^{−1}(Π_CC(v) Arch_CC^{−1})^k a_CE(v) − ε_K(v) a_EC(v) Arch_CC^{−1} a_CE(v),
with ε_K = max{r_+^{K+1}/(1−r_+), r_−^{K+1}/(1+r_−)}, r_± from spec X(v). If 𝒫_K(v) ⪰ 0 then S_E(v) ⪰ 0, hence
a_T(v) ⪰ 0 on P_T^{(N)} (Theorem 2 of ROUND_005_C: S_E ⪰ 0 and a_CC ≻ 0 give a ⪰ 0).
Proof. Theorem 2(iii) gives S_E ⪰ S_E^{(K)} − ε_K W*W = 𝒫_K. ∎
𝒫_K is a 29 × 29 (ev) / 27 × 27 (odd) matrix whose entries are polynomials in v of degree K + 2, apart from the
scalar ε_K(v), which is not polynomial (it needs an a-priori bound r_±(v) ≤ r̄_± on a box of v; a box with
r̄ = 0.55 at T = 1.0 is consistent with the NUMERICAL values 0.537–0.562).

Status at the true comb. NUMERICAL: 𝒫_K(Λ) ⪰ 0 requires K ≥ 84 (ev) / 80 (odd); at K = 84 the tail term is
≈ 1e-24 against λ_A = 1.6e-23. So the explicit inequality exists, is finite, and is sufficient, but its tail is
small relative to λ_A only at degree ≈ 86 in v. No reduction of this degree was found: the k-th terms have no
sign and cancel at relative precision 1e-9 per order (§3(b)). Writing the entries in closed form at K = 84 is a
finite but not illuminating computation (it is the Galerkin matrix of ROUND_005_C Theorem 2 expanded in v), and
it remains a statement at one T and one N, not a statement about the form a_T itself (the Galerkin truncation
error and the freezing of V, C in v are not controlled). OPEN: a uniform-in-N version; a degree bound
independent of λ_A.

Falsifier test for Proposition 4. (a) cΛ: at c = 1.01, 1.1, 𝒫_K(cΛ) has a negative eigenvalue for every K ≥ 0
(NUMERICAL, §3) — fails, as required. (b) a_3, (d) finite modifications: same (a_3, v_2 + 0.1 rejected). (c) Beurling:
not run in this memo. The proposition is a pointwise-in-v sufficient criterion; it does not by itself prefer Λ.

## Result

NO-GO (class: finite-degree Neumann truncation of the Schur coupling on the comb-response family E_T, with
tail bounded by the spectral radius of X). The coupling 𝒞_T is O(1) and essentially full rank on E_T
(eigenvalues 0.5 … 1e-20 over 2/3 of dim E); the Neumann series converges (r ≈ 0.54 at T = 1.0, 0.65–0.67 at
T = 1.2), but the sign of S_E is carried only at degree K* ≈ 25–30 (T = 1.0) and ≈ 105–125 (T = 1.2) in
practice and K ≈ 80–84 / 205–220 by the certified tail; the comb-generated E_T does not lower the degree
below the archimedean spectral band of ROUND_008_A (K* ≈ 150 there at T = 1.0 for the certified tail, ≈ 25–40
in practice): same wall, degree ∝ log(1/λ_A)/log(1/r). Low even truncations have the wrong sign.

What was proved. Proposition 1 (a_CE = Arch_CE − Π_CE P_V; a_EC = Arch_EC holds on N′ only — the coupling on V
carries Π at O(1)); Theorem 2 (Neumann expansion of a_CC^{−1} under (H₊) PROVED and (H₋) NUMERICAL; exact tail;
degree structure k, k+1, k+2 on (N′N′), (N′V), (VV)); Corollary 3 (degree lower bound); Proposition 4 (explicit
finite sufficient polynomial inequality at fixed T, N).

What failed and why. (i) The correct operator-norm check is ρ(X) < 1 for X = Arch_CC^{−1/2}Π_CC Arch_CC^{−1/2},
not the Euclidean ‖Π_CC Arch_CC^{−1}‖; (H₋) (the lower half of spec X > −1) has no proof: the available bound on
π_− exceeds λ_min(Arch_CC) by 2.4×. (ii) The terms of the expansion have no sign and cancel at 1e-9 relative
precision per order; the truncation needed to resolve λ_A grows like log(1/λ_A), i.e. like the double
exponential of T in degree. (iii) Falsifiers are rejected at K = 0–7: rejecting them costs nothing; certifying Λ
costs ≈ 84 orders at T = 1.0.

Next concrete step. Replace the geometric series by the Chebyshev (or minimax) polynomial of 1/(1 − x) on
[−r_−, r_+]: its error decays like ((1 − √(1−r²))/r)^K instead of r^K (for r = 0.54: 0.30 vs 0.54 per order),
which would cut the certified degree at T = 1.0 from ≈ 84 to ≈ 45 and at T = 1.2 from ≈ 210 to ≈ 100 — still
∝ log(1/λ_A). Unless a structured (signed) resummation of the k-terms on V is found, this class should be
closed.
