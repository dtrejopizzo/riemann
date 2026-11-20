# Round 23, memo C — Interior block I^λ with sieve weights and lemma 𝒩_k(ν): selection gate

Assignment: decide whether (a) the interior block I^λ of ROUND_004_A (4.3), (b) the OPEN lemma 𝒩_k(ν) of phase 211
ROUND_006_C §7, or their combination, give a one-sided inequality that sees Near_M together with Arch_M in the same step, that
is neither an absolute-value bound nor a standard large sieve. Selection gate: no derivations or computations.

Primary reading: ROUND_004_A in full (Lemmas 1, 3, Prop. 2, (4.3)–(4.4), answer (iv), «NOT excluded» 1–4);
phase 211 ROUND_006_C §§1–7 and result; phase 188 N_BUILD_021 in full (Prop. 1, Thm. 2, Prop. 3); ROUND_015_A in full
(class 𝒮_Λ², §1); RULES_AVOID l.37, 57, 84, 440, 650, 668; NEAR_DOSSIER l.128–133, 162, 187, 304, 320, 356–385.
Grep in the master index («criba», «sieve», «Selberg», «large sieve», «Montgomery–Vaughan», «Hilbert»; 469 lines):
relevant entries W-sieve (R167_102 Thm B/B′, R167_103 Thm S; l.3861, 4370), table 1.5 row «Sieves (Selberg, large
sieve, Ramanujan)» (round 15, repetition; l.1914), l.1320–1323, l.20430–20431 (phase 116: large sieve worse, orthogonality
from scale e^{2T}), l.23403–23409 (phase 104_35–38: Cholesky/large sieve, «every Selberg inversion loses the signed
cancellation»), l.23435–23436 (104_93: class NO-GO Selberg/Vaughan), l.5402 (Bessel/large sieve up to Y^{1/2−ε}), l.5998
(strategy J, weighted Hilbert: «do not retry Hilbert bounds…»), l.6135, l.6446 (MV+Sobolev NO-GO), l.866 (MV class, large
sieve, Sobolev, Hölder). No entry examines I^λ or 𝒩_k by name: both appear only as residues in NEAR_DOSSIER.

## (1) Closest antecedent

- (a) ROUND_004_A, answer (iv) and «NOT excluded» 4: with λ fixed without the weight, I^λ is affine in c and Corollary 2 of
  ROUND_003_6 (R3-e) applies literally: a sign of I^λ on its own holds for all c > 0 or for none. For the
  quadratic version (4.4), ROUND_015_A §1 (class 𝒮_Λ², PROVED): no certificate with sieve squares of
  Λ-free coefficients fails under the three controls. For every bound of I^λ obtained from sieve or
  progression statistics: N_BUILD_021 Thm. 2 (class closed under finite modification) and W-sieve (R167_102 Thm B).
- (b) ROUND_006_C §§3, 5, 7 themselves: 𝒩_k(ν) is a multiplicative energy count with b_m ≥ 0; the memo declares in §5
  that it is a size statement that survives cΛ, deletion and finite modification, and that failing for Beurling (because of
  integer spacing) «is not a diagnosis». Class: MV/large sieve (index l.866, l.20430–20431, l.23403–23409).

## (2) New object or operation

None. The only writable thing is the composition
    |I^λ(F)| ≤ Σ_{1<k≤N} |θ^λ(k)| k^{−1/2} |⟨A_M τ_{−log k}F, F⟩|,
bounding each term by a 𝒩_k-type count of near-coincidences m ≈ k·m′. That is exactly an absolute-value
bound with weights |θ^λ| and a large sieve over products: the form excluded by the assignment. I do not know how to write a
one-sided inequality (without |·|) combining both pieces: 𝒩_k(ν) does not contain Arch (it is Σ b_m b_{m′} over pairs of
products of N_T, without archimedean kernel), and in I^λ the Arch term enters with coefficients θ^λ that do not see the weight.

## (3) Why the change would avoid the failure of the antecedent

Not applicable: there is no change. Concretely:
- (a) The exact reason for failure is degree 0 in the weight of θ^λ (R3-e). Giving a sign to I^λ does not alter it; only
  a λ depending on the exact values of Λ would alter it (extremal problem; RULES_AVOID l.668, ROUND_015_A «next
  operation»), which is another operation, not I^λ with sieve weights, and falls first under ROUND_014_A Lemma P(b) if the dependence
  is by affine quotient.
- (b) The reason for failure of 𝒩_k is that it is a size statement: it holds for any non-negative weight of given support, and the
  loss C^k is fixed per order, incompatible with (F4) (margin ≈ M⁻³). Improving θ < 1 improves the cap exp(2e^T) of the
  sublevel set of ROUND_006_C, which is not a sign statement about 𝔸_M.
- Combination: composing a piece affine in c with a size bound is still affine/absolute-value; no
  term appears whose orientation depends on the weight being exactly 2Λ.

## (4) Connection with 𝔸_M ⪰ 0 and controls

Possible connection: 𝔸_M ⪰ 0 ⟸ Arch_M − Div_M − Near_M ≥ (bound of I^λ + remainder R^λ), with a_T = Re⟨M^λS_NA_MF,F⟩ − I^λ − R^λ.
Named step at which it would have to fail and does not fail:
- weight cΛ: «bound of I^λ» — affine in c (R3-e); a bound in |·| holds for all c ≤ c₀ with the same λ: it does not fail.
- deletion of a prime power: «count 𝒩_k» and «bound of I^λ» — they change by O(1) per term; class closed under
  finite modification (N_BUILD_021 Thm. 2; thm:finmod): it does not fail.
- Beurling: 𝒩_k uses the integer spacing 1/(m+1) and unique factorization (ROUND_006_C §5(c)), so its proof
  does not transfer; but this is the failure of a size bound, not of a sign step, and I^λ with sieve transfers
  (R167_103 Thm. S). (F2) is not met either: Arch and the weight do not enter through the same object in the same step.

## Verdict

DOES NOT PASS (no mechanism; in part (a), repetition of ROUND_004_A (iv) + ROUND_015_A §1; in part (b), MV/large sieve
class already recorded). Neither I^λ, nor 𝒩_k(ν), nor their composition give a one-sided inequality that sees Near_M and
Arch_M in the same step: the only writable composition is an absolute-value bound with weights |θ^λ| and a multiplicative
energy count, which holds for every weight in the class and does not fail in the controls.

Labels: the two residues remain OPEN as statements (sign of I^λ not examined in itself; lemma 𝒩_k(ν) OPEN as
a size statement), but they are discarded as a route to the global sign at this gate: that of I^λ by R3-e, that of
𝒩_k for being a size statement (F1, F4). What is not excluded remains ROUND_004_A «NOT excluded» 1–3 (λ depending on the
values of Λ or of F; Möbius of the system μ_a), which is not the operation examined here.

For independent checking: verify that (4.3) of ROUND_004_A has θ^λ independent of the weight for every sieve λ (Selberg,
Barban–Vehov, GPY, Λ_R), and that 𝒩_k(ν) in ROUND_006_C §7 contains no archimedean kernel.
