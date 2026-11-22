# Round 011 A — (HR)(a) on the high block: large values of P_T against |ĝ|², what the uncertainty principle can and cannot add, and the exact range left open

Target (★): λ_A(T) ≥ 0 for every T (STATEMENT_001). Notation of ROUND_010_A: λ = e^T, N = λ², I_T = [−T, T], g = Ef ∈ P_T,
W_T(g) = (1/2π)∫(m − P_T)|ĝ|² + 2A(g)B(g) (ROUND_010_A (3.1)), P_T(τ) = Σ_{2≤n<N} v_n cos(τ log n) = Re 𝒫(τ),
𝒫(τ) = Σ v_n n^{iτ}. Two masses are kept apart (the earlier rounds use S_T for both):
Σ₀ := Σ_{n<N} v_n = P_T(0) (= 4λ(1+o(1)) for Λ), and S₂ := Σ_{p<N} a_p², a_p = Σ_k v_{p^k} (= 8T²(1+o(1)), ROUND_006_C §3).
"High data": admissible g whose spectrum sits at |τ| ≥ Ω_lo := (1+δ)2πN up to a tail; the passage between this
frequency statement and prolate indices k > 4N(1+δ) is the one of ROUND_010_A §3.3 (local frequency τ/u of
f = E^{−1}g on [1/λ, λ] against the prolate band 2πλ), ARGUED there and used here only in that form.
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 0. Corpus check

Searched: ROUTES-TRIED-INDEX README rows P211-6A, P211-6C, P211-9B, P211-10A and the barrier list (W-loc, W-mom);
ledger rows C21–C24; ROUND_006_C §§3–4 (Theorem B, Corollaries C–D, class limit); ROUND_010_A §§3.3–3.4 and its
"Next concrete step"; grep in the corpus for Logvinenko, Kovrijkine, Panejah: hits only in phases 114/116 (weighted
prolate depth, multiplier phase coverage) and 154/186, all used there as sign tools on wells, not as a coercivity
bound on a frequency block with a Dirichlet-polynomial weight.
What differs and why the recorded barriers do not apply.
(i) W-mom (mean-square/moment bounds cannot give the sign) concerns the sign of the form. The statement attacked here
is coercivity on the high block with an O(1) constant: W_T ≥ κ·(positive quadratic quantity) for data whose spectrum
sits where m(τ) ≥ 2T + log(1+δ) + O(1). The margin λ_A is not involved; nothing here is required to reject (a)–(d) of
BRIEF rule 4 (ROUND_010_A §5(c): the Λ-specific sign lives in the low block). So a moment/large-values bound is a
legitimate tool for this piece; W-mom forbids only reading the sign off it.
(ii) P211-6C used Theorem B to count the near-null cluster (measure of a sublevel set). Here Theorem B is used for the
opposite purpose: to show a superlevel set is EMPTY at a given height (via a Bernstein lower bound on the measure of a
nonempty superlevel cell), and the uncertainty principle is tested as the bridge between measure and energy.
(iii) P211-10A closed the comb-mass class 𝒦_S; everything below uses S₂ (the spread over prime blocks) and integer
spacing, not Σ₀ alone, as that NO-GO requires.
Nothing in the index is retried.

## 1. Packets: (HR)(a) is a pointwise statement about a smoothed Dirichlet polynomial (PROVED)

Fix an even β ∈ C_c^∞(−1, 1), β ≥ 0, β ≢ 0, and put ρ(u) := ∫β(y)β(y + u)dy / ∫β², so ρ is even, 0 ≤ ρ ≤ 1, ρ(0) = 1,
supp ρ ⊂ [−2, 2], ρ > 0 on (−2, 2). For τ₀ > 0 put g₀(x) := β(x/T)cos(τ₀x) and
    P^ρ_T(τ) := Σ_{n<N} v_n ρ(log n / T) cos(τ log n).                                                    (1.1)

**Lemma 1.1 (PROVED).** For every M there is C_M(β) with, for τ₀T ≥ 1,
  (a) (1/2π)∫P_T|ĝ₀|² = ‖g₀‖²(P^ρ_T(τ₀) + ε₁), |ε₁| ≤ C_MΣ₀(τ₀T)^{−M};
  (b) (1/2π)∫m|ĝ₀|² = ‖g₀‖²(m(τ₀) + ε₂), |ε₂| ≤ C(β)/(τ₀T) + C_M(τ₀T)^{−M}log(2+τ₀);
  (c) |A(g₀)| + |B(g₀)| ≤ C_M(τ₀T)^{−M}‖g₀‖, and the P_T-projection g of g₀ satisfies ‖g − g₀‖ ≤ C_M(τ₀T)^{−M}‖g₀‖.
*Proof.* (a) By (3.1) of ROUND_010_A, (1/2π)∫P_T|ĝ₀|² = Σv_nc_{g₀}(log n), and
c_{g₀}(u) = ½cos(τ₀u)∫β(x/T)β((x+u)/T)dx + ½∫β(x/T)β((x+u)/T)cos(τ₀(2x+u))dx. The first term is
‖g₀‖²(1 + O((τ₀T)^{−M}))ρ(u/T)cos(τ₀u), since ‖g₀‖² = ½T∫β² + O((τ₀T)^{−M}) (same oscillatory integral); the second is
O_M((τ₀T)^{−M})T by M integrations by parts in x. Sum over n with weights v_n. (b) ĝ₀ = ½(β̂_T(τ − τ₀) + β̂_T(τ + τ₀)),
β̂_T(ξ) = Tβ̂(Tξ) is Schwartz at scale 1/T; m is even, |m(τ)| ≤ log(2+|τ|) + C_∞ and |m′(τ)| ≤ C/|τ| for |τ| ≥ 1
(lem:mbounds, CITED from Paper 46); split at |τ − τ₀| = τ₀/2. (c) A, B are pairings with e^{±x/2}-type profiles
(Paper 46 eq:W); integrate by parts M times against cos(τ₀x). ∎

**Proposition 1.2 (necessity; PROVED).** Suppose that for some Ω_lo, κ ≥ 0 and every g ∈ P_T with
∫_{|τ|<Ω_lo}|ĝ|² ≤ η∫|ĝ|² one has W_T(g) ≥ κ‖g‖² (any coercive form of (HR)(a), with the leakage replaced by ‖g‖²
or by anything ≥ 0). Then for every τ₀ ≥ 2Ω_lo with τ₀T large enough (depending on β, η),
    P^ρ_T(τ₀) ≤ m(τ₀) − κ + O_β(1/(τ₀T)).                                                                   (1.2)
*Proof.* The packet g of Lemma 1.1(c) has spectral mass below Ω_lo ≤ τ₀/2 of size O_M((τ₀T)^{−M}), and
W_T(g) = ‖g₀‖²(m(τ₀) − P^ρ_T(τ₀) + O(1/(τ₀T))) by Lemma 1.1. ∎
So the requested inequality, in any form strong enough to give W_T ≥ 0 on high data, is equivalent at leading order
to the family of pointwise bounds (1.2) over all centres τ₀ ≳ Ω_lo and all profiles ρ. In particular the target
form of ROUND_010_A, (1/2π)∫(P_T − m)_+|ĝ|² ≤ θ(1/2π)∫(m − P_T)_+|ĝ|² with θ < 1 (which gives
W_T ≥ (1 − θ)(1/2π)∫(m − P_T)_+|ĝ|² + 2AB), forces (1.2) with κ = 0, and the measure of {P_T > m} plays no role
except through whether it meets the packet's cell of width O(1/T).

## 2. What the uncertainty principle contributes (CITED + PROVED); why it cannot replace (1.2)

**Lemma 2.1 (local energy at scale 1/T; PROVED, elementary).** Let χ₀ ∈ C_c^∞(−2, 2), χ₀ = 1 on [−1, 1],
C₀ := ‖χ̂₀‖_{L¹}, k_T(ξ) := T|χ̂₀(Tξ)|/C₀ (a probability density at scale 1/T). For every g ∈ L²(I_T),
    |ĝ(τ)|² ≤ (C₀²/4π²)(k_T ∗ |ĝ|²)(τ),   hence ∫w|ĝ|² ≤ (C₀²/4π²)∫(w ∗ k_T)|ĝ|² for every w ≥ 0.
*Proof.* g = gχ₀(·/T) gives ĝ = (2π)^{−1}ĝ ∗ (Tχ̂₀(T·)); Cauchy–Schwarz with the measure |Tχ̂₀(T(τ − σ))|dσ; Fubini. ∎

**Logvinenko–Sereda / Kovrijkine (CITED).** O. Kovrijkine, "Some results related to the Logvinenko–Sereda theorem",
Proc. Amer. Math. Soc. 129 (2001), 3037–3047, Theorem 1: if h ∈ L²(ℝ) has Fourier transform supported in an interval
of length b and E ⊂ ℝ is (γ, a)-thick (|E ∩ J| ≥ γ|J| for every interval J of length a), then
‖h‖_{L²(ℝ)} ≤ (C/γ)^{C(ab+1)}‖h‖_{L²(E)}, C absolute. (Logvinenko–Sereda 1974 for the qualitative form; Panejah
1961–62 for the necessity of thickness.) Applied to h = ĝ (whose Fourier transform is supported in I_T, b = 2T) with
a = A/T: ∫_E|ĝ|² ≥ c_A(γ)∫|ĝ|², c_A(γ) := (γ/C)^{2C(2A+1)}.

**Proposition 2.2 (what (i)+(ii) give; PROVED).** Let 0 < ϑ < 1, E_ϑ := {τ : P_T(τ) ≤ ϑm(τ)} and
E := E_ϑ ∪ (−Ω_lo, Ω_lo). If E is (γ, A/T)-thick and g ∈ L²(I_T) has ∫_{|τ|<Ω_lo}|ĝ|² ≤ η∫|ĝ|², then
    (1/2π)∫(m − P_T)|ĝ|² ≥ [(1 − ϑ)m_lo(c_A(γ) − η) − (1 − c_A(γ))·sup_{|τ|≥Ω_lo}(P_T − m)_+ − η(Σ₀ + C_m)]·‖g‖²,
m_lo := inf_{|τ|≥Ω_lo} m, C_m := sup(−m)_+ < ∞. So coercivity follows only if
    sup_{|τ|≥Ω_lo}(P_T − m)_+ < (1 − ϑ)m_lo(c_A(γ) − η)/(1 − c_A(γ)).                                       (2.1)
*Proof.* Split ∫ = ∫_{E_ϑ} + ∫_{E_ϑ^c}; on E_ϑ, m − P_T ≥ (1 − ϑ)m; on the complement, m − P_T ≥ −(P_T − m)_+;
Kovrijkine for the mass on E_ϑ; the low region costs at most Σ₀ times its mass. ∎
Reading (PROVED by comparing (2.1) with (1.2)). (2.1) is a pointwise bound on P_T − m on the whole high range, with an
allowance c_A(γ)/(1 − c_A(γ)) that is small; it is strictly stronger than the necessary condition (1.2). Theorem B of
ROUND_006_C enters only through the thickness of E_ϑ, but thickness of E_ϑ at scale A/T cannot be derived from a
measure bound for its complement unless that complement has no cell of length ≳ γA/T, i.e. again a pointwise
statement. Conclusion: the combination (i) (measure of large values) + (ii) (uncertainty at scale 1/T) collapses to
the pointwise bound (1.2) / (2.1); the uncertainty principle only converts a pointwise bound into an energy bound, it
cannot convert a measure bound into one, because P_T has frequencies up to 2T = log N and its superlevel cells have
the same scale 1/T as the packets of P_T (Lemma 1.1). This is the structural fact behind the task's step (ii).

## 3. Theorem B gives (1.2) — with room to spare — above a double-exponential height (PROVED)

**Theorem 3.1 (emptiness of the superlevel set at large height; PROVED given Mertens/PNT, CITED).** Let ρ be as in §1
or ρ ≡ 1 on [0, 2) (then P^ρ_T = P_T). Let 0 < ϑ ≤ 1, Ω ≥ 2πe^{1.172}, m_Ω := log(Ω/2π) − 0.172, s := ϑm_Ω/2,
k := ⌊log Ω/(2T)⌋ ≥ 1. If
    (3 + 6π)Ω · e√(2k) · (4kS₂/(e s²))^k < s/(TΣ₀),                                                         (3.1)
then P^ρ_T(τ) < ϑm(τ) for every τ ∈ [Ω, 2Ω]. Asymptotically, (3.1) holds for all Ω ≥ Ω_B(ϑ, T) with
    log Ω_B(ϑ, T) = (64/(eϑ²))·T·e^{2T}·(1 + o(1))   (T → ∞).                                                (3.2)
*Proof.* M := P^ρ_T is a real exponential sum with frequencies log n ∈ [0, 2T), bounded on ℝ by Σ₀; Bernstein's
inequality for bounded entire functions of exponential type σ (‖F′‖_∞ ≤ σ‖F‖_∞, CITED) gives |M′| ≤ 2TΣ₀. If
M(τ₀) ≥ ϑm(τ₀) ≥ 2s for some τ₀ ∈ [Ω, 2Ω] (lem:mbounds(ii), CITED: m(τ) ≥ log(τ/2π) − 0.172 for τ ≥ 2π), then M > s on
an interval of length s/(TΣ₀) around τ₀, contained in [0, 3Ω]. Theorem B of ROUND_006_C applies to M verbatim: its
proof uses only nonnegative coefficients supported on n < N, grouped in p-blocks with h_p(0) = Σ_kv_{p^k}ρ(k log p/T)
≤ a_p (so the Hoeffding range and S₂ do not increase), unique factorisation and the spacing of log m for m < N^k. With
window [0, 3Ω] and N^k ≤ Ω it bounds |{M > s} ∩ [0, 3Ω]| by the left side of (3.1); contradiction.
Asymptotics: with L := log Ω, S₂ = 8T²(1+o(1)), Σ₀ = 4λ(1+o(1)) (ROUND_006_C §3, CITED Mertens/PNT), s = ϑL/2·(1+o(1)),
k = (L/2T)(1 + O(T/L)): log(left side) = L + (L/2T)log(64T/(eϑ²L)) + O(log L) and log(right side) = −T + O(log L).
The difference is negative as soon as (1/2T)log(eϑ²L/(64T)) ≥ 1 + C(T + log L)/L, i.e. for L ≥ (64T/(eϑ²))e^{2T}(1+o(1)). ∎

**Corollary 3.2 ((HR)(a) above Ω_B; PROVED, same citations).** Let Ω_B = Ω_B(ϑ, T) and g ∈ L²(I_T) with
∫_{|τ|<Ω_B}|ĝ|² ≤ η∫|ĝ|², η < 1. Then
    (1/2π)∫(P_T − m)_+|ĝ|² ≤ θ·(1/2π)∫(m − P_T)_+|ĝ|²,   θ := η(Σ₀ + C_m) / ((1 − η)(1 − ϑ)m(Ω_B)),
and θ = (eϑ²/(16(1 − ϑ)))·η/((1 − η)Tλ)·(1 + o(1)) → 0. Consequently W_T(g) ≥ (1 − θ)(1 − ϑ)(1 − η)m(Ω_B)‖g‖² + 2A(g)B(g).
*Proof.* Theorem 3.1 with ρ ≡ 1 on dyadic blocks: (P_T − m)_+ = 0 on |τ| ≥ Ω_B, and (P_T − m)_+ ≤ Σ₀ + C_m everywhere;
on |τ| ≥ Ω_B, m − P_T ≥ (1 − ϑ)m ≥ (1 − ϑ)m(Ω_B) (m increasing there). ∎
So on data living above Ω_B the coercivity is not merely O(1): it is of size m(Ω_B) ≍ TN, and the uncertainty
principle is not needed. The theorem is an ℕ-specific size statement (§5), not a sign step.

## 4. The open range [Ω_lo, Ω_B): what (1.2) is there, and the limit of the moment class

**Proposition 4.1 (the condition (1.2) is a genuine large-values statement at order T; PROVED, Mertens CITED).**
Let ρ be as in §1, V := Σ_{n<N}v_n²ρ(log n/T)², and Ω ≥ max(N², C·Σ₀²/V). Then
    sup_{τ∈[Ω,2Ω]} P^ρ_T(τ) ≥ V^{3/2}/(488 S₂) − 3Σ₀/Ω ≥ c₁T,   c₁ := ρ(1)³/1381·(1 + o(1)).
*Proof.* Write P^ρ_T = Re𝒫^ρ, 𝒫^ρ = Σb_nn^{iτ}, b_n = v_nρ(log n/T). Montgomery–Vaughan (CITED) gives
∫_Ω^{2Ω}|𝒫^ρ|² ≥ V(Ω − 3π(N + 1)); |∫_Ω^{2Ω}(𝒫^ρ)²| ≤ Σb_mb_n·2/log(mn) ≤ 2Σ₀²/log 4; hence ∫_Ω^{2Ω}(P^ρ_T)² ≥ VΩ/4
for Ω ≥ CΣ₀²/V and Ω ≥ 12π(N + 1). Theorem B's mean-value step with k = 2 and Lemma B.0 (ROUND_006_C) give
∫_Ω^{2Ω}(P^ρ_T)⁴ ≤ (2Ω + 3π(N² + 1))·24(eS₂/2)² ≤ 931ΩS₂² for Ω ≥ N². Hölder: ∫|P^ρ_T| ≥ (∫(P^ρ_T)²)^{3/2}(∫(P^ρ_T)⁴)^{−1/2}
≥ ΩV^{3/2}/(244S₂). The mean is small: |∫_Ω^{2Ω}P^ρ_T| ≤ Σb_n·2/log n ≤ 3Σ₀. So ∫(P^ρ_T)_+ = ½(∫|P^ρ_T| + ∫P^ρ_T)
≥ ΩV^{3/2}/(488S₂) − 3Σ₀/2, and the sup is at least the mean of the positive part. Finally V ≥ ρ(1)²Σ_{n≤λ}4Λ(n)²/n =
2ρ(1)²T²(1 + o(1)) and S₂ = 8T²(1 + o(1)), so V^{3/2}/(488S₂) ≥ ρ(1)³T/(488·2√2)(1 + o(1)). ∎
At Ω = N² the right side of (1.2) is m ≈ 4T + O(1); the left side is ≥ c₁T. So (1.2) at the bottom of the high range
is a comparison of two quantities of order T with no slack in the exponent: it is the same O(1)-competition that
ROUND_010_A §3.4(i) found in the mean square (RMS P_T ≈ 2T vs m ≈ 2T + O(1)), now at the level of the supremum over
cells of width 1/T.

Why the PROVED region stops at Ω_B (PROVED for Theorem B; class statement ARGUED).
(a) Theorem B's off-diagonal error 3πN^k forces k ≤ log Ω/(2T); the saving (4kS₂/(es²))^k then beats the cell
length s/(TΣ₀) ≈ e^{−T} only for log Ω ≳ (64/e)TN/ϑ² (proof of (3.2)). This is the same mechanism as the class limit
of ROUND_006_C §4, now at the level "superlevel set empty" instead of "superlevel set small".
(b) Even with no off-diagonal error the moment class cannot reach (1.2) on most of [Ω_lo, Ω_B). Lemma B.0 identifies
Σ_mb_m² with E|𝒫(θ)|^{2k} for the torus model 𝒫(θ) = Σ_ph_p(θ_p) (independent p-blocks). A bound that uses only these
moments cannot separate P_T from the torus model; the torus model is a sum of independent bounded blocks with variance
of Re𝒫 equal to S₂/2·(1 + o(1)) ≈ 4T², so (central limit, ARGUED with explicit Berry–Esseen not written out) its
superlevel probability at level L is ≥ exp(−L²/(8T²)(1 + o(1))) for L ≤ o(T³)-range, and a band of e^L cells of width
1/T contains such a level unless L²/(8T²) ≥ L, i.e. unless L ≥ 8T². So in the pure moment class the earliest height
at which (1.2) can be certified is log Ω ≈ 8T² (with the spacing error, ≈ (64/e)TN). The heuristic extreme value of a
Gaussian model, 2T√(2L), exceeds m ≈ L exactly for L < 8T²; for P_T itself the inequality (1.2) must therefore come
from arithmetic correlations between cells (near-coincidences m ≈ m′ of k-fold products, the semiring interplay of
ROUND_006_C §4), not from the size of the moments.
(c) The plunge. Nothing in this memo depends on k ∈ (4N(1 − δ), 4N(1 + δ)): the frequency picture places the plunge at
τ ≈ 2πN, a single scale; the open range is the whole interval of heights log τ ∈ [2T + log 2π(1 + δ), (64/e)TN(1 + o(1))),
which contains ROUND_010_A Proposition 3.3's range e^{S−C} (S = Σ₀ ≈ 4λ) as a subrange. So "what fails at the plunge"
has the answer: nothing specific; what fails is the pointwise control (1.2) on 2T ≲ log τ ≲ min(8T², (64/e)TN), with
the moment class certifying nothing there and Theorem B certifying everything above Ω_B.

## 5. Falsifier test (BRIEF rule 4; not a sign step, checked as required by the task)

(a) cΛ. Theorem 3.1/Corollary 3.2 survive for every c with S₂ → c²S₂, Σ₀ → cΣ₀: log Ω_B(c) = c²(64/(eϑ²))TN(1+o(1)),
so the PROVED region recedes like c² in the exponent. The necessary condition (1.2) FAILS for large c (PROVED): by
Proposition 4.1, sup_{[N²,2N²]}cP^ρ_T ≥ cc₁T > 4T + C ≥ m once c > 4/c₁ + o(1) (an explicit absolute constant,
≈ 5.6·10³/ρ(1)³ with the constants above, far from sharp). Hence (HR)(a) is NOT cΛ-invariant: it holds for no c ≥ c*,
and its status for c ∈ (1, c*) is the same O(1) competition as for Λ. Consistent with ROUND_010_A §5 (α_HI moves < 1%
under 1.01Λ): weakening, not rejection, near c = 1.
(b) a_P (primes below P deleted): S₂ and Σ₀ decrease, P^ρ_T changes by a fixed trigonometric polynomial with
frequencies log p^k, p < P; Theorem 3.1 survives with a smaller Ω_B. Not rejected (size statement).
(c) Beurling systems. Theorem 3.1 uses unique factorisation (distinct products ↦ distinct characters, Lemma B.0) and
integer spacing (Montgomery–Vaughan with δ_m ≥ 1/(m+1)); both can fail for generalized integers, so the PROVED region
is ℕ-specific and has no proof for (c). Proposition 1.2 and §2 hold verbatim with the Beurling P_T.
(d) Finite modification of v_n: O(1) changes of S₂, Σ₀; Theorem 3.1 survives with an O(1) change in (3.1).
Comb-genericity. Theorem 3.1 depends on the comb only through (S₂, Σ₀), nonnegativity, support in n < N and integer
structure: it holds for every nonnegative comb on prime powers with the same block masses a_p. This is acceptable for
(HR)(a) (coercivity on the high block, ROUND_010_A §5(c)); it is not a sign step and is not used as one. The single-atom
comb Sδ₂ of ROUND_010_A Proposition 3.3 has S₂ = S², and Theorem 3.1 then gives log Ω_B ≍ S²TN, consistent with the
negative values below e^{S−C} found there.

## Result

PROVED piece + NO-GO with class. (HR)(a) is reduced exactly (Proposition 1.2) to the pointwise packet bound
P^ρ_T(τ₀) ≤ m(τ₀) − κ + o(1) for all τ₀ ≳ (1 + δ)2πN and all window profiles ρ; it is PROVED (Theorem 3.1, Corollary 3.2,
with θ → 0) for data whose spectrum lies above Ω_B, log Ω_B = (64/(eϑ²))Te^{2T}(1 + o(1)); it is OPEN on
2T ≲ log τ < log Ω_B. NO-GO (class: measure-of-large-values bound + Logvinenko–Sereda/Kovrijkine uncertainty): the
combination collapses to the same pointwise bound with a worse constant (Proposition 2.2), because the superlevel cells
of P_T and the packets of P_T live at the same scale 1/T. NO-GO (class: moment bounds of order k with off-diagonal
error controlled by integer spacing): cannot certify (1.2) below log τ ≈ (64/e)TN; without the spacing error, still
not below log τ ≈ 8T² (ARGUED, torus-model moments).

### What was proved
- Lemma 1.1, Proposition 1.2: packet calculus; any coercive (HR)(a) on high data ⟺ (to leading order) the pointwise
  bound (1.2) for the smoothed Dirichlet polynomial P^ρ_T at every centre.
- Lemma 2.1 (local energy at scale 1/T); Proposition 2.2 (Kovrijkine CITED): what thickness of {P_T ≤ ϑm} buys — a
  pointwise condition (2.1) stronger than (1.2).
- Theorem 3.1: P^ρ_T < ϑm on [Ω, 2Ω] under the explicit inequality (3.1); asymptotic threshold (3.2).
- Corollary 3.2: (HR)(a) with θ = O(η/(Tλ)) for data above Ω_B, coercivity constant ≍ TN.
- Proposition 4.1: sup_{[Ω,2Ω]}P^ρ_T ≥ c₁T for Ω ≥ N² (Montgomery–Vaughan + fourth moment + Hölder); hence (1.2) fails
  for cΛ, c ≥ c* absolute.

### What failed and why
- The uncertainty principle cannot turn the measure bound of Theorem B into an energy bound: P_T has frequencies up to
  log N = 2T, so its superlevel cells have width ≍ 1/T, the same as the minimal spectral width of g ∈ L²(I_T); packets
  at a single cell are admissible high data (Lemma 1.1(c), with the prolate transfer ARGUED as in ROUND_010_A).
- Theorem B certifies emptiness of {P_T ≥ ϑm} only at log τ ≳ (64/(eϑ²))TN (spacing error 3πN^k ties k to log τ/2T).
- The torus-model moments are blind below log τ ≈ 8T² (ARGUED).
- The plunge plays no special role; the open range is all of 2T ≲ log τ < log Ω_B.

### Next concrete step
Two independent pieces. (1) NUMERICAL margin of (1.2): compute min over τ₀ ∈ [2πN(1+δ), N⁴] of m(τ₀) − P^ρ_T(τ₀) for
two profiles ρ at T = 0.8, 1.0, 1.2 (a one-dimensional scan of a Dirichlet polynomial with < N terms at step 1/(20T));
a negative value would falsify (HR)(a) in packet form at that T, a positive margin of order one fixes the constant κ.
(2) Pure math: a large-sieve bound for P^k on [Ω, 2Ω] that counts near-coincidences m ≈ m′ of k-fold products of
n < N through their multiplicative energy (not the spacing 1/(m+1)), aimed at lowering the exponent (64/e)TN of (3.2);
any bound below 8T² must use arithmetic correlation between cells (§4(b)).
