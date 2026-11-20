# Recursive transfer through the sixth-power rows

**Result.** Let MS(α) denote the mean-square hypothesis of the short preprint with the row
range H = D^α in place of D^{1+ϑ} (precise form in §2). Theorem R below is PROVED: for
0 < α ≤ 1, MS(α) implies A_1(D) ≪ D^{θ+ε} with θ = 1/2 + 5α/12, with a constant independent
of the prime p and of the induction step, with the same test function W and the same excluded
set S at every scale. Together with the Mellin argument of §3 of the short preprint (CITED,
checked to use only this bound) it gives: no zeros of L_K(s, ν) in Re s > 1/2 + 5α/12. The
values are α = 1 → 11/12 and α = 18/25 → 4/5. The mechanism is an exact identity (Lemma 1):
A_{p⁶}(D) is a finite geometric series of untwisted sums A_1(D/N(p)^j), so the trivial transfer
error O(D/Y) of (2.4) is never needed; the second branch 2 − h/3 of the exponent map of the
phase 209 notes disappears. Part (2) is PROVED: the proof of Proposition 3.1 uses H > D first
at (5.13), to satisfy the hypothesis 𝓗 ≤ Σ D^{−κ} of Proposition 5.1; for H = D^α with α < 1
the dual row range exceeds the column scale by D^{1−α}/B, Lemma 5.3 becomes circular, the
iteration does not contract, the best conceivable output of the chain is Σ|A_u|² ≪ D^{2+ε}
(loss D^{1−α}, giving θ = 1 − α/12 ≥ 11/12 through Theorem R), and the dual target (4.12) is
in fact false in part of the range (4.11) (Proposition 2, PROVED). Part (3): MS(α) with α < 1
is a mean square below the diagonal; no estimate uniform in the coefficients can give it, and
by Theorem R itself any unconditional proof of MS(α) with α < 9/10 would be a new zero-free
half-plane beyond 7/8, so none exists in the literature. The result of Gao and Zhao cited as
[12] by the short preprint is GRH-conditional, concerns quadratic twists, and holds only when
the family is larger than the length. 4/5 remains OPEN; it is now equivalent, within this
architecture, to MS(18/25).

## 1. Setting (CITED: short preprint, §3 and (2.2))

K = Q(√−3), O = Z[ω]. ν a finite-order Hecke character of K, S a finite set of prime ideals
containing those above 2 and 3 and those dividing the conductor of ν. W ∈ C_c^∞((0,∞); C)
with supp W ⊂ [a, b], 0 < a < b. For u ∈ O,

    A_u(D) = Σ_{(n,S)=1} μ(n)ν(n)χ_n(u) W(N(n)/D),      χ_n(u) = (u/n)_6,

n running over ideals prime to S represented by primary generators, and (u/n)_6 extended by
zero when (u, n) ≠ 1. For a primary prime p ∉ S and n prime to S, χ_n(p⁶) = 1_{p∤n}
(short preprint, proof of Theorem 1.1 from Proposition 3.1).

Two facts about the field, used with unspecified absolute constants:

(F1) #{n ⊂ O ideal : N(n) ≤ x} ≤ c_1 x for x ≥ 1 (ideal counting; CITED, standard).
(F2) #{p ∉ S prime ideal : Y/2 < N(p) ≤ Y} ≥ c_2 Y/log Y for Y ≥ Y_0(S) (Landau's prime
ideal theorem, as used in §3 of the short preprint; CITED).

**Hypothesis MS(α).** Fix 0 < α ≤ 1. For every ε > 0 there is C_ε = C(ε; ν, S, W) such that
for all D ≥ 1

    Σ_{u ∈ O, 0 < N(u) ≤ D^α} |A_u(D)|² ≤ C_ε D^{1+α+ε}.                                (MS)

In the preprint's form (Proposition 3.1 with α = 1 + ϑ) the constant is
≪_{ν,S,I,ϑ,ε} max_{0≤j≤k} ‖W^{(j)}‖_∞² with k = k(ϑ, ε) and I ⊃ supp W; for Theorem R the
only thing used is that C_ε is finite for the fixed W, because W never changes along the
induction. Nothing below needs MS(α) for any W other than the one in the conclusion.

## 2. The exact transfer identity (PROVED)

**Lemma 1.** Let p ∉ S be a primary prime, q = N(p). For every D > 0,

    A_{p⁶}(D) = Σ_{j ≥ 0} ν(p)^j A_1(D/q^j),

the sum being finite: A_1(D') = 0 whenever bD' < 1, so at most 1 + log(bD)/log q terms are
nonzero. Equivalently, A_1(D) − A_{p⁶}(D) = −ν(p) A_{p⁶}(D/q) = −ν(p) Σ_{j≥0} ν(p)^j A_1(D/q^{j+1}).

*Proof.* Since χ_n(p⁶) = 1_{p∤n}, A_{p⁶}(D) is the part of A_1(D) with p ∤ n. In the
complementary part p | n, and μ(n) ≠ 0 forces n = pm with p ∤ m, m squarefree, (m, S) = 1;
then μ(n)ν(n) = −ν(p)μ(m)ν(m) and W(N(n)/D) = W(N(m)/(D/q)). Hence

    A_1(D) = A_{p⁶}(D) − ν(p) Σ_{(m,S)=1, p∤m} μ(m)ν(m)W(N(m)/(D/q)) = A_{p⁶}(D) − ν(p) A_{p⁶}(D/q),

the last sum being exactly A_{p⁶}(D/q) by the same identity χ_m(p⁶) = 1_{p∤m}. Thus
A_{p⁶}(D) = A_1(D) + ν(p)A_{p⁶}(D/q). Apply this at D/q, D/q², …; the recursion stops once
bD/q^j < 1 because no ideal has norm below 1. ∎

Remarks. (i) The identity is the coefficient form of
Σ_{p∤n} μ(n)ν(n)N(n)^{−s} = (1 − ν(p)q^{−s})^{−1} Σ_n μ(n)ν(n)N(n)^{−s}. (ii) Inclusion–exclusion
on the condition p ∤ m, as suggested in the problem statement, gives sums at the scales D/q
and D/q² and then again at D/q³, …: it is the same series. (iii) The phase 209 note
QRH_REPLICA_COHERENCE proves B_p(D) = −ν(p)A_1(D/N(p)) + O_{K,W}(1) for Y = √D; Lemma 1 is the
exact form valid for every Y, which is what the induction needs because here D/q² is large.
(iv) The test function and the excluded set are the same on both sides: the only objects at
the smaller scales are A_1(D/q^j) with the original W and S.

## 3. Theorem R (PROVED, conditional on MS(α))

**Theorem R.** Fix ν, S, W as in §1 and 0 < α ≤ 1, and assume MS(α). Put
θ = 1/2 + 5α/12. Then for every ε ∈ (0, 1) there is K = K(ε; α, ν, S, W) such that

    |A_1(D)| ≤ K D^{θ+ε}      for all D ≥ 1.

*Proof.* Write Y = D^{α/6}, so Y⁶ = D^α, and note 2θ = 1 + 5α/6.

Step 0 (thresholds). Let D_0 = D_0(α, ε, S) ≥ 1 be such that for all D ≥ D_0:
 (i) Y ≥ max(32, Y_0(S)), i.e. D ≥ max(32, Y_0(S))^{6/α};
 (ii) log Y = (α/6) log D ≤ D^ε.
Both hold for D large in terms of α, ε, S only.

Step 1 (base). For 1 ≤ D < D_0, by (F1), |A_1(D)| ≤ ‖W‖_∞ #{n : N(n) ≤ bD} ≤ c_1 b ‖W‖_∞ D
(the sum is empty if bD < 1). Since 1 − θ > 0, |A_1(D)| ≤ K_0 D^{θ+ε} with
K_0 := c_1 b ‖W‖_∞ D_0.

Step 2 (one scale, MS(α) used once). Let D ≥ D_0 and
P = {p ∉ S primary prime : Y/2 < N(p) ≤ Y}, J = #P ≥ c_2 Y/log Y ≥ c_2 Y D^{−ε} by (F2) and (ii).
The elements p⁶, p ∈ P, are distinct, with 0 < N(p⁶) ≤ Y⁶ = D^α, so (MS) at the scale D gives

    Σ_{p∈P} |A_{p⁶}(D)|² ≤ C_ε D^{1+α+ε}.

By Lemma 1, A_1(D) = A_{p⁶}(D) − R_p(D) with R_p(D) := Σ_{j≥1} ν(p)^j A_1(D/q^j), q = N(p).
Hence |A_1(D)|² ≤ 2|A_{p⁶}(D)|² + 2|R_p(D)|²; averaging over p ∈ P,

    |A_1(D)|² ≤ (2/J) Σ_{p∈P} |A_{p⁶}(D)|² + 2 max_{p∈P} |R_p(D)|²
             ≤ (2 C_ε / c_2) D^{1+α+2ε} Y^{−1} + 2 max_p |R_p(D)|²
             = (2 C_ε / c_2) D^{2θ+2ε} + 2 max_p |R_p(D)|².                                   (3.1)

Step 3 (induction). Put K² := max(K_0², 4C_ε/c_2). Claim: |A_1(D)| ≤ K D^{θ+ε} for all
D ∈ [1, D_0 2^k), by induction on k ≥ 0. For k = 0 this is Step 1. Assume it for k and let
D ∈ [D_0 2^k, D_0 2^{k+1}). For p ∈ P, q > Y/2 ≥ 16, so every scale D/q^j (j ≥ 1) in R_p(D)
satisfies D/q^j < D/16 < D_0 2^k and is covered by the induction hypothesis. Since θ ≥ 1/2 and
q ≥ 16, q^{−θ} ≤ 1/4 and Σ_{j≥1} q^{−j(θ+ε)} ≤ q^{−θ}/(1 − q^{−θ}) ≤ (4/3)(2/Y)^θ, so

    |R_p(D)| ≤ K D^{θ+ε} Σ_{j≥1} q^{−j(θ+ε)} ≤ (4/3) 2^θ K D^{θ+ε} Y^{−θ},
    2|R_p(D)|² ≤ (32/9) 4^θ K² Y^{−2θ} D^{2θ+2ε} ≤ (K²/2) D^{2θ+2ε},

the last step because Y ≥ 32 and θ ≤ 1 give (32/9)·4^θ·Y^{−2θ} ≤ (32/9)·4·32^{−1} < 1/2.
Insert into (3.1) and use K² ≥ 4C_ε/c_2:

    |A_1(D)|² ≤ (K²/2) D^{2θ+2ε} + (K²/2) D^{2θ+2ε} = K² D^{2θ+2ε}.

This closes the induction. ∎

Bookkeeping of the constants. K depends on ε, α, ν, S and on W through C_ε(W) (the MS(α)
constant for this W), ‖W‖_∞ and b = sup supp W; it does not depend on p, on k, or on D. The
hypothesis (MS) is invoked exactly once per scale, always at the scale D being treated, with
the fixed W and S; the induction hypothesis is invoked at the scales D/q^j with the same W
and S (Lemma 1, remark (iv)). No ε accumulates: the error term carries the power saving
Y^{−2θ} = D^{−αθ/3}, and the main term is MS(α) at the current scale. The number of nested
scales is at most 6/α + 1 but plays no role.

**Corollary (CITED: short preprint §3, Mellin argument).** Under MS(α), L_K(s, ν) has no
zero in Re s > θ = 1/2 + 5α/12. Check of what the argument uses: for a hypothetical zero ϱ
with Re ϱ > θ it takes W(y) = y^{−ϱ}φ(y), 0 ≠ φ ∈ C_c^∞((1,2)), φ ≥ 0, a complex-valued smooth
compactly supported test, and needs only A_1(D) ≪ D^{θ+ε} for that W (holomorphy of
M_W(s) = ∫ A_1(D) D^{−s} dD/D on Re s > θ) plus Hecke's continuation and the identity
L_K^S(s,ν)M_W(s) = Ŵ(s). The exponent 11/12 enters the argument only through the bound, so
the same text proves the statement with θ. Since MS(α) is assumed for every W, the Corollary
holds. The deduction for Dirichlet L-functions and ζ by quadratic base change is unchanged.

Values (PROVED arithmetic):

    θ(α) = 1/2 + 5α/12:   α = 1 → 11/12;   α = 9/10 → 7/8;   α = 18/25 → 1/2 + 3/10 = 4/5;
    α = 3/5 → 3/4;   α → 0 → 1/2.

Comparison with the phase 209 exponent map θ(h) = ½ max{1 + 5h/6, 2 − h/3}
(QRH_EXPONENT_MAP, QRH_REPLICA_COHERENCE): Theorem R is the first branch alone. The second
branch came from the trivial bound (2.4), |A_{p⁶} − A_1| ≪ D/Y; Lemma 1 replaces it by the
induction, whose contribution is always negligible. At α = 1 nothing changes (5/3 < 11/6), so
the trivial transfer was never the bottleneck of the 11/12 proof; the gain is only that α < 1
becomes meaningful. For α > 1 the same proof gives θ = 1/2 + 5α/12 as well, which is worse.

Remark on the factor 5/6 (ARGUED). The extraction uses only the rows u = p⁶, because they are
the rows on which the twist is trivial. By sextic reciprocity n ↦ χ_n(u) is, up to a fixed
ray class factor, a Hecke character of conductor dividing a fixed multiple of u, trivial
exactly when u is a sixth power times a unit; so the coherent rows among 0 < N(u) ≤ H number
≍ H^{1/6}, and (1/J)·(mean square) ≥ D^{1+α}/H^{1/6} = D^{1+5α/6} is the best this averaging
gives. Reaching θ = 1/2 in this way needs α → 0, i.e. MS over D^{o(1)} rows, which is the
statement A_1(D) ≪ D^{1/2+ε} itself up to the identity of Lemma 1; this is the equivalence
recorded in QRH_REPLICA_COHERENCE (not repeated here).

## 4. Why the proof of Proposition 3.1 does not give MS(α) for α < 1

All displays cited are from the short preprint.

### 4.1 The chain of ranges (CITED)

Proposition 4.5 expands the square, applies Poisson in u, and reduces (3.1) to the dual bound
(4.12), E(𝓗, X, F; ξ, W) ≪ D^ε XF, required for all B, F ≥ 1 in the ranges (4.11):

    X = D/(BF),      0 < 𝓗 ≤ C D²/(H B²),      Σ := XF = D/B.

Here 𝓗 is the dual row range: the Fourier variable k = eh has 0 < N(k) ≤ C_Φ b_0² D²/(H N(b)²)
from the support of Φ̂ in (4.16). The dual bound is then proved by Proposition 5.1, whose
hypothesis (5.1) is

    H_dual ≤ Σ D^{−κ}      (κ > 0 fixed),

and (5.13) verifies it for H = D^{1+ϑ}: 𝓗 ≤ C D^{1−ϑ}/B², Σ = D/B, so 𝓗/Σ ≤ C D^{−ϑ}/B ≤ D^{−ϑ/2}
for large D, κ = ϑ/2.

### 4.2 Where the hypothesis 𝓗 ≤ Σ D^{−κ} is consumed (CITED, located)

(a) Lemma 5.3, display (5.9). The short part of the cube inversion is bounded through
Proposition 5.2 by 𝓗 + 𝓗² F H_c³/X. The cutoff H_c³ = min(X, X²/𝓗²) of (5.6) is chosen so that
the second term is ≤ XF = Σ; the first term 𝓗 is ≤ Σ only by the hypothesis H ≤ Σ of the
lemma. The same hypothesis is used for the case L_b ≤ 1, E ≪ 𝓗/L_b ≪ Σ.

(b) Proof of Proposition 5.1, the contraction. With N(b) > H_c and Σ = XF,

    𝓗' ≤ 𝓗 L_b/(ΣF) = 𝓗/(N(b)³F²) < 𝓗/(H_c³F²) = 𝓗 (𝓗/Σ)² ≤ D^{−2κ} 𝓗,

so the row range drops by a power at each step and the iteration ends after ⌈C_0/κ⌉ steps at
H' ≤ 1, where counting gives the base case. Proposition 5.4 also assumes max{𝓗, LF} ≤ Σ.

So the first inequality of the proof that needs H larger than D by a power is (5.13), i.e.
hypothesis (5.1) of Proposition 5.1; inside the proof, it is the diagonal term 𝓗 of the
quadratic large sieve (Lemma 6.5, the H in (6.13), carried into (5.5) and (5.9)) and the
contraction factor (𝓗/Σ)² that need it. The term 𝓗²N(f)/X of Proposition 5.2 is the
off-diagonal large-sieve term; it is never the obstruction, since H_c absorbs it.

### 4.3 What happens for H = D^α, α < 1 (PROVED arithmetic; ARGUED where marked)

Insert H = D^α in (4.11): 𝓗 = C D^{2−α}/B², Σ = D/B, X = D/(BF), hence

    𝓗/Σ = C D^{1−α}/B,      𝓗/X = C F D^{1−α}/B.

The hypothesis (5.1) fails for every dyadic block with B < C D^{1−α+κ}; in particular for
B ≍ 1, which is present (b is the common factor of the two column indices after extraction
of the exclusion, and b = 1 occurs). On such a block the dual family has more rows than
columns by D^{1−α}/B: the dual problem is above the diagonal, and the target Σ lies below the
diagonal 𝓗 of the dual mean square.

Rigorous output of the chain there: take the model block B = F = 1, X = D, 𝓗 = C D^{2−α},
Σ = D. Then 𝓗² > X and H_c³ = X²/𝓗² = C^{−2} D^{2α−2} < 1, so H_c < 1: in Lemma 5.3 the short
part is empty and the supremum in (5.7) contains b = 1 with L_1 = X, i.e. E(𝓗, X, F) itself.
The lemma is circular. Applying Proposition 5.4 directly at L = X with the free target Σ' = 𝓗
(the smallest allowed by max{𝓗, XF} ≤ Σ') gives 𝓗'' ≤ 𝓗X/(𝓗F) = X/F and Σ'' ≤ X, so
𝓗''/Σ'' ≤ 1 with no power contraction: the iteration never reaches a row range ≤ 1, and the
base case (counting) is never available. The chain proves nothing on these blocks.

Best conceivable output (ARGUED: grant, counterfactually, that every mean square produced by
the recursion were bounded by its own diagonal, E ≼ 𝓗): then on the block B = F = 1,
E/Σ ≈ D^{1−α}, and (4.17) turns this into |S_{ξ;B,F}| ≪ D^ε H·D^{1−α}, so

    Σ_{0<N(u)≤D^α} |A_u(D)|² ≪ D^{2+ε}       (loss D^{1−α} against MS(α), uniformly in α).

Through Step 2 of Theorem R with D^{2+ε} in place of D^{1+α+ε}: |A_1(D)|² ≪ D^{2+ε}/Y, i.e.
θ = 1 − α/12 ≥ 11/12, with equality only at α = 1. Hence no choice of α < 1 improves 11/12
through this chain even in its best case: the loss 1 − α in the mean square exceeds the gain
5(1 − α)/12 of Theorem R, since (1 − α/12) − (1/2 + 5α/12) = (1 − α)/2 ≥ 0.

### 4.4 The dual target (4.12) is false for α < 1 (PROVED)

**Proposition 2.** Let 0 < α < 1, H = D^α, and let W ≢ 0 be smooth with compact support in
(0,∞). For every ε < (1 − α)/4 there are points (B, F, 𝓗) of the range (4.11) at which
E(𝓗, X, F; ξ, W) ≥ D^{1−α−4ε} XF for all large D. Consequently the hypothesis of
Proposition 4.5 cannot hold, and the reduction to the dual mean square — not only the proof
of Proposition 5.1 — is unavailable for α < 1.

*Proof.* Expand (4.9) for fixed f:

    Σ_{0<N(k)≤𝓗} |Σ*_n a_ξ(n)χ_n(k)χ_n(f)⁴W(N(n)/X)|²
      = Σ*_{n,m} a_ξ(n) a_ξ(m)‾ χ_n(f)⁴ χ_m(f)⁴‾ W(N(n)/X) W(N(m)/X)‾ Σ_{0<N(k)≤𝓗} χ_n(k)χ_m(k)‾.

Diagonal n = m: |a_ξ(n)| = 1 for squarefree n prime to S (|α(n)| = 1 and the normalized Gauss
sum of a primitive character has modulus one), |χ_n(f)⁴|² = 1_{(n,f)=1}, and
Σ_{0<N(k)≤𝓗} |χ_n(k)|² = #{k ∈ O : 0 < N(k) ≤ 𝓗, (k, n) = 1}. By inclusion–exclusion over
d | n and the lattice point count #{k : N(k) ≤ x} = (2π/√3)x + O(x^{1/2} + 1),

    #{k : 0 < N(k) ≤ 𝓗, (k,n) = 1} = (2π/√3) 𝓗 Π_{p|n}(1 − 1/N(p)) + O(τ(n) 𝓗^{1/2}) ≥ c 𝓗 X^{−ε}

for N(n) ≤ bX and 𝓗 ≥ X^{2}. The n-sum of |W(N(n)/X)|² over squarefree primary n prime to S
and to f, N(n) ∈ [aX, bX], is ≥ c_W X D^{−ε} for X ≥ X_0(W) (positive density of such ideals,
N(f) ≤ 2D). So the diagonal is ≥ c' 𝓗 X D^{−2ε}.

Off-diagonal n ≠ m: both squarefree and primary, so some prime p divides exactly one of them,
say n = pn' with p ∤ m. The function k ↦ χ_n(k)χ_m(k)‾ is periodic modulo the lattice nmO and
its sum over a complete residue system factors (Chinese remainder theorem) through
Σ_{x mod p} χ_p(x) = 0, as χ_p has exact order 6 on the cyclic group (O/p)^×. The disc
0 < N(k) ≤ 𝓗 is covered by translates of a fundamental parallelogram of nmO, of diameter
≤ 2N(nm)^{1/2}; those lying inside the disc contribute zero; those meeting the boundary circle
number ≪ 1 + 𝓗^{1/2}N(nm)^{−1/2} and contain N(nm) points each. Hence

    |Σ_{0<N(k)≤𝓗} χ_n(k)χ_m(k)‾| ≤ c (N(nm) + (𝓗 N(nm))^{1/2}) ≤ c (b²X² + b 𝓗^{1/2} X),

and the off-diagonal total is ≤ ‖W‖_∞² (c_1 bX)² · c (b²X² + b𝓗^{1/2}X) ≪ X⁴ + 𝓗^{1/2} X³.
If 𝓗 ≥ X^{4+6ε} then X⁴ ≤ 𝓗 X^{−6ε} and 𝓗^{1/2}X³ ≤ 𝓗 X^{1−3ε}, both o(𝓗 X D^{−2ε}) since
X ≥ D^{c} on the points chosen below. So for each f the k-sum is ≥ (c'/2) 𝓗 X D^{−2ε}, and
summing over the ≍ F values of f (squarefree primary, prime to S, F ≤ N(f) < 2F),

    E(𝓗, X, F; ξ, W) = (XF)^{−1} Σ_f Σ_k |…|² ≥ c'' 𝓗 D^{−3ε}.

Now choose the point: B = 1, F = D^{(2+α)/4 + 2ε}, so X = D^{(2−α)/4 − 2ε} → ∞, and
𝓗 = C D^{2−α} (the top of its range in (4.11)). Then
X^{4+6ε} = D^{(2−α) − 8ε + (3/2)(2−α)ε − 12ε²} ≤ D^{2−α−5ε}, so 𝓗/X^{4+6ε} ≥ C D^{5ε} ≥ 1 for
large D and the condition 𝓗 ≥ X^{4+6ε} holds; N(b)N(f) ≤ b_0 D holds since (2+α)/4 + 2ε < 1.
Finally

    E / (XF) ≥ c'' C D^{2−α−3ε} / D = c'' C D^{1−α−3ε} ≥ D^{1−α−4ε}

for large D, while (4.12) demands E/(XF) ≪ D^{ε}. Since ε < (1−α)/4, this is a contradiction
for large D. ∎

Interpretation (ARGUED). The exact dual S_ξ in (4.16) is a bilinear form in (m_1, m_2) with the
weight Φ̂ and the signs μ(f) on the auxiliary index f; it equals M_D − Z, which is small when
MS(α) holds. Proposition 4.5 passes from S_ξ to Σ_{f,k}|S_U|² by Lemma B.2 and the triangle
inequality in b, discarding the signs μ(f) and the sign of Φ̂. For 𝓗 ≤ Σ this costs only D^ε;
for 𝓗 > Σ the discarded cancellation is exactly the factor 𝓗/Σ = D^{1−α}/B. In other words,
the Poisson dual of a below-diagonal Möbius mean square is an above-diagonal mean square
whose rows carry a new Möbius-type sign structure (the f-sum, with coefficient μ(f)), and the
large-sieve step of the short preprint is blind to it. The Möbius structure of the original
coefficients is used by the preprint only once, in the conversion (4.5) to cubic Gauss sums;
after that the dual coefficients a_ξ(n) are treated as arbitrary unimodular coefficients, and
no such treatment can beat the dual diagonal.

## 5. What a proof of MS(α) with α < 1 would need; what exists (one page)

Shape of the statement. MS(α) asks for square-root cancellation on average for
H = D^α < D sums, each of length ≍ D, twisted by the sextic family n ↦ χ_n(u). By sextic
reciprocity each twisted sum is the smoothed Möbius sum of the Hecke L-function L(s, νψ_u),
ψ_u a character of conductor ≪ N(u) ≤ H. So MS(α) is a mean square of Möbius sums over a
family of conductors up to H with length D ≫ H: a mean square below the diagonal.

Three structural facts (PROVED unless marked).

(a) No estimate uniform in the coefficients can give it. For any family of H characters
and any length D > H, taking a_n = W(N(n)/D) and keeping only the row u = 1 (χ_n(1) = 1)
gives Σ_u |Σ_n a_n χ_n(u)|² ≥ |Σ_n a_n|² ≍ D² > H D^{1+ε}. So the large-sieve constant of the
family {χ_·(u) : N(u) ≤ H} on coefficients of length D is ≥ D, and every large sieve for
sextic, cubic or quadratic characters (Heath-Brown 1995; Goldmakher–Louvel 2013;
Blomer–Goldmakher–Louvel 2014; Baier–Young for cubic; all CITED through the short preprint's
bibliography) necessarily contains the column term "+ D". MS(α) must use μ(n)ν(n) itself.

(b) Under GRH for the family, MS(α) holds for every α: Perron's formula with 1/L bounded by
(N(u)(1+|t|))^ε on Re s = 1/2 + ε gives A_u(D) ≪ D^{1/2+ε} N(u)^ε individually (this is the
mechanism of Lemma 2.6 in the paper of Gao and Zhao discussed below). So MS(α) is a
"GRH on average, below the diagonal" statement for the sextic family.

(c) Conversely, by Theorem R and its Corollary, an unconditional MS(α) with α < 1 yields the
zero-free half-plane Re s > 1/2 + 5α/12 for all finite-order Hecke L-functions of K, hence
for all Dirichlet L-functions and ζ; for α < 9/10 this is beyond 7/8, beyond anything in the
literature (where the only unconditional zero-free half-planes are the ones of the two
preprints, neither refereed). Therefore MS(α) with α < 1 cannot be obtained by citation:
any proof of it is a proof of a new zero-free half-plane. The question "which known results
are of this type" has the answer: none, unconditionally, by (c).

What is known of nearby type (CITED, verified).

- Gao and Zhao, Mean squares of quadratic twists of the Möbius function, J. Number Theory 247
  (2023), 1–14 (arXiv 2212.09241). Theorem 1.1: assuming GRH, for smooth Φ, W,
  Σ*_{d} (Σ_n μ(n)χ_{8d}(n)Φ(n/Y))² W(d/X) = (4/π²) XY h̃_1(1,1) Z_2(1) + O(X^{1/2+ε}Y^{3/2+ε} + XY^{1/2+ε}),
  d over odd squarefree positive integers; the authors state that this is an asymptotic
  formula iff Y ≪ X^{1−ε}. Three differences from MS(α): it assumes GRH; it concerns Kronecker
  (quadratic) twists over Z, not the sextic family over O; and it is valid only when the
  family X is larger than the length Y. The error term X^{1/2}Y^{3/2} exceeds the main term XY
  exactly when Y > X: their method (Poisson summation in d after Soundararajan, plus the GRH
  bound for 1/L) loses precisely at the diagonal, the same place as the short preprint. The
  short preprint lists this paper as [12] in its bibliography; the text extraction contains no
  inline citation of it, and the 7/8 manuscript's reference [12] is a different paper of the
  same authors (sextic Hecke L-functions, Lemma 2.9, a large-sieve input).
- Barban–Davenport–Halberstam type bounds for Möbius in progressions,
  Σ_{q≤Q} Σ_a |M(x; q, a)|² ≪ xQ log x + x²(log x)^{−A} (Montgomery's proof via the
  multiplicative large sieve and Siegel–Walfisz applies to μ; ARGUED, no specific reference
  verified here). This is a mean square of ≍ Q² characters of sums of length x, and is below the
  diagonal only up to logarithms, with the deficit x²(log x)^{−A} coming from the individual
  small-conductor L-functions: equivalent in strength to zero-free regions, not to power
  savings.
- Zero-density estimates for the family cannot substitute: a Möbius sum is not controlled by
  zeros alone (1/L has poles at the zeros with residues 1/L'(ϱ)), and even for ψ-type sums the
  exceptional set at σ = 1/2 + ε of a density estimate with exponent c is of size H^{c/2},
  which is o(H) only for c < 2, beyond the density hypothesis (ARGUED).

What a proof would need. Either (i) a sign-sensitive treatment of the exact dual (4.16): the
sum over f with coefficient μ(f) and the kernel Φ̂, kept as a bilinear form rather than a mean
square, on the blocks B < D^{1−α}; this is a Möbius sum in f of length up to D with the dual
column sums as coefficients, i.e. the original difficulty reappears in the dual; or (ii) a
different family embedding A_1(D) with ≫ H^{1/6+δ} coherent rows among N(u) ≤ H, which would
lower the factor 5/6 in Theorem R instead of α (ARGUED; no such family is proposed here); or
(iii) a genuinely new mean-value theorem for 1/L over the sextic family below the diagonal,
which by (c) is a new zero-free half-plane and so cannot be an input.

Routes record. The index entry L74 and the phase 209 section record no recursive transfer;
QRH_REPLICA_COHERENCE records the first-order identity for Y = √D and the equivalence of the
selective estimate with A_1(D) ≪ D^{1/2+ε}, which is consistent with §3 (α → 0). Nothing here
reopens a closed family.

## 6. What this does and does not give

Gives. (1) Theorem R, PROVED: MS(α) ⟹ A_1(D) ≪ D^{1/2+5α/12+ε}, with explicit constants
K² = max((c_1 b‖W‖_∞ D_0)², 4C_ε/c_2) and D_0 = max(32, Y_0(S))^{6/α} ∨ {D : (α/6)log D ≤ D^ε},
the same W and S at every scale, and no dependence on p or on the step. (2) The exact
replacement of the trivial transfer (2.4) by Lemma 1; the second branch of the phase 209
exponent map is an artefact. (3) 4/5 is reduced, within this architecture, to MS(18/25); 7/8
to MS(9/10); the short preprint's own 11/12 is MS(1) with the exact transfer. (4) A precise
location of the failure of Proposition 3.1's proof for α < 1: hypothesis (5.1) via (5.13),
consumed in (5.9) and in the contraction of §5.5, with 𝓗/Σ = CD^{1−α}/B; the chain is circular
there and the dual target (4.12) is false (Proposition 2). (5) A proof that MS(α), α < 1, is
not in the literature in any form: it is equivalent in strength to a new zero-free half-plane.

Does not give. No proof of MS(α) for any α < 1; no new estimate; no new zero-free region.
The status of 4/5 is OPEN. The open problem is exactly MS(18/25): a below-the-diagonal mean
square for the sextic-twisted Möbius family, which needs the sign structure in f of the exact
dual (4.16) or a different embedding family; no construction of either is made here.
