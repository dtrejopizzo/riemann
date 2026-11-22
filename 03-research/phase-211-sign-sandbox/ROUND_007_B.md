# Round 007 B — The sign budget taken apart: the three pieces on P_T, the crossing window, the response cubic, and what the budget can and cannot carry

Object: the budget of ROUND_005_C Prop. 3 on P_T,

    a_T(F) = σ_T‖F‖² + κ(F) − ℛ(F),   σ_T = C_0 + 4 − 4e^{−T} + ε_T,   κ(F) = ∫_0^{2T}(‖F‖² − Re c_F(u))K_1(u)du,
    ℛ(F) = ∫_{[0,2T)} Re c_F(u) dR(u),   dR = Σ_{n∈N_T} v_n δ_{log n} − 2e^{u/2}du,   K_1(u) = 2Σ_{j≥1}e^{−(2j+½)u},

and the sign lemma (SL′_T): ℛ(F) ≤ κ(F) + σ_T‖F‖² on E_T (the comb-response family of ROUND_005_C Definition 1).
Notation of STATEMENT_001 §1 and ROUND_005_C (mesh ω_q = πq/2T, φ_q, G, H, C_q, m_q, s_q, Π, Arch = a_T + Π,
𝒩, N′, V_T, E_T). Labels PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL. Nothing outside
STATEMENT_001 is used; nothing is reduced to zeros.

Corrections from REVIEW_004 applied throughout: σ_T is positive for T < T_0 = 0.0520 (§1.1), so the budget is written
with −σ_T and never with |σ_T|; the Tate responses P_𝒞Π𝒯 are part of E_T (so that ROUND_005_C Theorem 2(iii) is exact);
the C_q² identity of ROUND_005_C §5.3(i) is a truncated convolution for N ≥ e^{2T}; the halo kernel −½K is not used here.

---------------------------------------------------------------------------------------------------
## 0. Corpus check

Routes-tried index. README rows P211-5C (predecessor: the budget, (SL′_T), the crossing of the carrying role),
P211-C ((L2′), block-only criteria NO-GO), P211-2A (floor Schur NO-GO), P211-4A (Prop. B: fixed Λ-free finite
subspaces with margin cannot carry the sign), P211-5A (Prop. 3.4: near-coincidence classes W_3(r) at degree 3, sign
against the inequality; Prop. 3.5 scaling), P211-6A (Theorem 4: the density part of the comb is −∫(u′² + u²/4) on P_T).
06_OPEN_RESIDUES R1 ((N)/(N_loc), polar-free form 𝓕_T(F) ≤ 𝔞^♯(F) with λ^♯(T) ↓ C_0 + 4, OPEN; dead sub-routes:
absolute/mean-square bounds, bounded functionals of v, pointwise symbol positivity, per-prime Euler bounds, Selberg,
SOS, exterior certificates, determinants/moments, Poisson comparison), R5 ((E_γ) at one frequency, m^♯(γ)).
Phase 192 EI_001 (outer field split: boundary polar moment − Chebyshev fluctuation − archimedean tail; sign content
= Lemma S, excluded by the review). grep "EI_001", "sign budget", "fluctuation functional", "(N)", "twisted Chebyshev":
only the rows above and R186-E_γ (04_PHASES line 145).

Paper 46 (CITED below, checked against the tex): lem:polarelim (2∫_0^{2T}Re c_F e^{u/2} = −𝔢(F), 𝔢(F) =
(1/2π)∫|F̂|²/(¼+τ²) = ‖G′‖² + ¼‖G‖² for F = (¼ − ∂²)G, 0 ≤ 𝔢 ≤ 4‖F‖²); prop:sharp (m^♯ = m + 1/(¼+τ²) =
Re ψ(5/4 + iτ/2) − log π, increasing in |τ|, m^♯(0) = C_0 + 4; 𝔞_T = 𝔞^♯ − 𝓕_T on P_T; λ^♯(T) nonincreasing,
≥ C_0 + 4, → C_0 + 4); thm:nyq-cone (P_T = (¼ − ∂²)H²_0(I_T)); prop:arch (λ_inf,P(T) ↓ C_0); cor:margin1
(λ_A(T) ≤ 4·10⁹ T e^{−15.449T}).

What this memo establishes about the predecessor and why it is not a retry. The budget σ_T‖F‖² + κ(F) is
exactly the polar-free form 𝔞^♯ of prop:sharp written at the window (§1.2, PROVED in three lines), and ℛ is exactly
𝓕_T = Π + 𝔢 (§1.3, CITED). So (SL′_T) is residue R1 in its polar-free form restricted to E_T; the "fluctuation
functional" contains the Λ-free energy 𝔢 ≥ 0, and the crossing of the carrying role reported in ROUND_005_C §4.5 is
a property of this bookkeeping (§2.4, PROVED). None of the dead sub-routes of R1 is retried: no absolute or
mean-square bound, no bounded functional, no pointwise positivity, no per-prime bound, no Selberg identity as a
sign mechanism. The new pieces are the nodal/Tate-pin lemma (§1.2), the T-independence and continuity of the pieces
on the minimiser (§2.1–2.2), the bookkeeping theorem (§2.4), the explicit time-domain cubic of the response with
its window cutoffs (§3.1–3.2), and the degree hierarchy on the minimiser against λ_A (§3.3), which is the
quantitative content of the NO-GO of §3.4.

---------------------------------------------------------------------------------------------------
## 1. The three pieces on P_T

### 1.1 The constant σ_T [PROVED]

**Lemma 1.1.** (i) σ_T = C_0 + 4 + ∫_{2T}^∞ K_1(u)du = C_0 + 4 + Σ_{j≥1} 4e^{−(4j+1)T}/(4j+1) = C_0 + 4 + 4∫_T^∞ e^{−5t}(1 − e^{−4t})^{−1}dt.
(ii) C_0 + 4 = 4 − γ − π/2 − log(8π) = −1.3721834…, since ψ(¼) = −γ − π/2 − 3log 2 (CITED, Gauss digamma theorem).
(iii) T ↦ σ_T is strictly decreasing and convex on (0, ∞), σ_T → +∞ as T → 0 (σ_T = −log(4T) + O(1)), σ_T ↓ C_0 + 4
as T → ∞, and σ_T < 0 exactly for T > T_0 = 0.05199… (NUMERICAL root; the sign change is PROVED by (iii) and the
limits). At the windows of the record: σ_{½log5} = −1.35755, σ_1 = −1.36674, σ_{1.25} = −1.37024.
Proof. (i) ε_T = ∫_{2T}^∞ K = Σ_{j≥0}2e^{−(4j+1)T}/(2j+½); the j = 0 term is 4e^{−T}, which cancels −4e^{−T}; what is
left is ∫_{2T}^∞K_1. The integral form is the geometric sum. (ii) is the digamma value. (iii) The tail of a positive
decreasing integrable kernel is decreasing and convex in the lower limit; K_1(u) ~ 1/u at 0 gives the logarithm. ∎

Reading. σ_T is the value of the polar-free symbol at τ = 0, m^♯(0) = C_0 + 4, plus the part of the j ≥ 1 Lévy
kernel that lies beyond the window. The record's "universal constant −1.36" is m^♯(0) up to the window tail.

### 1.2 The Λ-free form σ_T‖F‖² + κ(F) = 𝔞^♯(F), its bottom and its negative directions

**Proposition 1.2 (identification). [PROVED]** For every F ∈ P_T, σ_T‖F‖² + κ(F) = 𝔞^♯(F) := (1/2π)∫ m^♯(τ)|F̂(τ)|²dτ,
with m^♯(τ) = C_0 + 4 + ∫_0^∞(1 − cos τu)K_1(u)du = m(τ) + 1/(¼+τ²) = Re ψ(5/4 + iτ/2) − log π. Consequently the form
σ_T‖·‖² + κ does not depend on T on ∪_T P_T (extension by zero), it is bounded below by (C_0 + 4)‖F‖², and
σ_T‖F‖² + κ(F) ≥ Arch(F) with equality iff F = 0.
Proof. m = C_0 + ∫_0^∞(1 − cos τu)K du and ∫_0^∞(1 − cos τu)2e^{−u/2}du = 4 − 1/(¼+τ²), so m^♯ = C_0 + 4 +
∫_0^∞(1 − cos τu)K_1 du. By Plancherel and Fubini (K_1 ≥ 0, ‖F‖² − Re c_F(u) ≥ 0), (1/2π)∫[∫_0^∞(1 − cos τu)K_1du]|F̂|²dτ =
∫_0^∞(‖F‖² − Re c_F(u))K_1(u)du = κ(F) + ‖F‖²∫_{2T}^∞K_1, since c_F vanishes beyond 2T; add (C_0 + 4)‖F‖² and use
Lemma 1.1(i). The lower bound is m^♯ ≥ m^♯(0) (prop:sharp(i)); the comparison with Arch is lem:polarelim:
𝔞^♯ = Arch + 𝔢 with 𝔢 ≥ 0 and 𝔢(F) = 0 only for F = 0. ∎

So κ(F) ≥ 0 is the Lévy energy of the completely monotone density K_1 and its bottom on P_T is governed by that of
𝔞^♯: λ^♯(T) := inf{𝔞^♯(F) : F ∈ P_T, ‖F‖ = 1} is nonincreasing, ≥ C_0 + 4, and tends to C_0 + 4 (CITED, prop:sharp(iii)).
The negative set of m^♯ is |τ| < τ^♯ with τ^♯ = 6.12587… (NUMERICAL root of m(τ) = −1/(¼+τ²); m itself vanishes at
6.2898), and m^♯(0) = C_0 + 4 is its minimum.

**Lemma 1.3 (nodal structure and the Tate pin). [PROVED]**
(i) Every real F ∈ P_T \ {0} changes sign at least twice in I_T.
(ii) For every F ∈ P_T and every τ ∈ ℝ, |F̂(τ)|² ≤ d_T(τ)‖F‖², where d_T(τ) := dist²_{L²(I_T)}(e^{iτt}, 𝒯) =
    2T − (Re Z(τ))²/(T + sinh T) − (Im Z(τ))²/(sinh T − T),  Z(τ) := 2 sinh((½ + iτ)T)/(½ + iτ).
    In particular d_T(0) = 2T − 16 sinh²(T/2)/(T + sinh T) = T⁵/360 + O(T⁷), and d_T(τ) → 2T as |τ|T → ∞.
(iii) Hence 𝔞^♯(F) ≥ −‖F‖²(1/2π)∫_{|τ|<τ^♯}|m^♯(τ)| d_T(τ)dτ on P_T, and the number of negative eigenvalues satisfies
    n_−(𝔞^♯|_{P_T}) ≤ n_−(Arch|_{P_T}) ≤ N_Arch(0; T), the archimedean upper Weyl count of ROUND_006_A Lemma 5.1.
Proof. (i) 𝒯 = span{cosh(t/2), sinh(t/2)} is a Haar space of dimension two on I_T: a nonzero element has at most one
zero. If F had no sign change, ∫F cosh(t/2) ≠ 0; if exactly one, at t_0, then g(t) = sinh((t − t_0)/2) ∈ 𝒯 changes
sign exactly at t_0, so Fg has constant sign and is not a.e. zero, and ∫Fg ≠ 0. Both contradict F ⊥ 𝒯.
(ii) F̂(τ) = ⟨F, e^{−iτt}⟩ = ⟨F, e^{−iτt} − P_𝒯e^{−iτt}⟩ since F ⊥ 𝒯; Cauchy–Schwarz. The projection: cosh(t/2) ⊥
sinh(t/2) on the symmetric interval, ‖cosh(t/2)‖² = T + sinh T, ‖sinh(t/2)‖² = sinh T − T, and ∫_{I_T}e^{t/2}e^{iτt}dt = Z(τ)
has real part ∫cosh(t/2)cos τt and imaginary part ∫sinh(t/2) sin τt (the odd products integrate to zero). The
expansion at τ = 0 is a Taylor computation. (iii) Split m^♯ into its negative and positive parts and apply (ii) on
the negative part; the counts: 𝔞^♯ ≥ Arch as forms (Prop. 1.2) and min–max; the last bound is the cited lemma. ∎

Reading. The most negative direction of the symbol, τ = 0 where m^♯ = C_0 + 4, is unavailable on P_T to relative
precision d_T(0)/2T = T⁴/720 (4·10⁻⁴ at T = 0.75): the two Tate conditions remove the two lowest modes (cosh(t/2) ≈ 1, sinh(t/2) ≈ t/2) and force two
sign changes. The negative directions of 𝔞^♯ on P_T therefore sit at 1/T ≲ |τ| < τ^♯, a band of fixed width, and
their number grows like (2T/π)τ^♯ − O(1) (ARGUED from the Landau–Widom count; the exact counts at the windows of
the record are in §2.3, NUMERICAL). The bound (iii) is not sharp (§2.3 compares it with the computed bottom); its
content is that the pin, not the Lévy energy κ, is what keeps λ^♯(T) above C_0 + 4 at finite T.

### 1.3 The functional ℛ: exact identity and the Sobolev term [CITED + PROVED]

**Proposition 1.4.** For F ∈ P_T,
    ℛ(F) = Σ_{n∈N_T} v_n Re c_F(log n) − 2∫_0^{2T}e^{u/2}Re c_F(u)du = Π(F) + 𝔢(F),
    𝔢(F) = (1/2π)∫_ℝ |F̂(τ)|²/(¼ + τ²) dτ = ∫_{I_T}(|G′|² + ¼|G|²)dt  for F = (¼ − ∂²)G, G ∈ H²_0(I_T),
so that 0 ≤ 𝔢(F) ≤ 4‖F‖² and ℛ = 𝓕_T of Paper 46 (lem:polarelim, thm:nyq-cone; the time-domain form is
ROUND_006_A Theorem 4). On the mesh, R̂_q = C_q + 𝒮_q with
    𝒮_q = −2∫_0^{2T}e^{u/2}cos(ω_q u)du = (1 − (−1)^q e^T)/(¼ + ω_q²)   [PROVED, direct integration with e^{2iTω_q} = (−1)^q],
negative on every even mode and positive on every odd mode, while the form ½Σ_q 𝒮_q|x_q(F)|² = 𝔢(F) ≥ 0 on P_T:
the two Tate conditions are exactly what makes an alternating mesh symbol a nonnegative form.
Consistency: Arch = 𝔞^♯ − 𝔢 on P_T (lem:polarelim), hence a_T = Arch − Π = 𝔞^♯ − 𝔢 − Π = 𝔞^♯ − ℛ, which is Prop. 3 of
ROUND_005_C. [PROVED]

**Corollary 1.5 (the sign lemma rewritten). [PROVED]** On E_T (or on P_T), each of the following is the same statement:
    (SL′_T)  ℛ(F) ≤ κ(F) + σ_T‖F‖²;   Π(F) ≤ 𝔞^♯(F) − 𝔢(F);   Π(F) ≤ Arch(F);   a_T(F) ≥ 0.
The "Sobolev term" 𝔢 moves between the two sides and nothing else happens. Equivalently, in the potential G ∈ H²_0:
    Σ_n v_n Re [(∂² − ¼)²c_G](log n) ≤ (1/2π)∫ m(τ)(τ² + ¼)²|Ĝ(τ)|²dτ,
with no constraint on G other than G = G′ = 0 at ±T.

---------------------------------------------------------------------------------------------------
## 2. The crossing window: what is T-independent, what is continuous, what is bookkeeping

### 2.1 One form, nested subspaces [PROVED]

**Lemma 2.1.** Let 𝔞(F) := 𝔞^♯(F) − ℛ(F) for F ∈ ∪_T P_T (extension by zero; P_T ⊂ P_{T′} for T < T′ since A, B are
integrals over the support). Then 𝔞^♯, ℛ, Π, 𝔢 and 𝔞 do not depend on T, 𝔞|_{P_T} = a_T, and
    λ_A(T) = inf{𝔞(F) : F ∈ P_T, ‖F‖ = 1}.
Proof. 𝔞^♯ is T-free by Prop. 1.2; Π(F) = Σ_{log n<2T}v_nRe c_F(log n) is T-free because c_F vanishes beyond 2T, so
the primes with log n ≥ 2T contribute zero whatever the window; 𝔢 is T-free by its Fourier form; ℛ = Π + 𝔢. ∎

So the three pieces are three fixed functionals on one nested family; the window enters only through the test space.
On a minimiser F*_T (which exists: the form 𝔞 on P_T is bounded below, closed, with compact resolvent, since
m^♯ → ∞ logarithmically and the supports are compact):
    𝔞^♯(F*_T) − ℛ(F*_T) = λ_A(T),   Arch(F*_T) − Π(F*_T) = λ_A(T),   ℛ(F*_T) = Π(F*_T) + 𝔢(F*_T).   [PROVED]

### 2.2 Continuity of the pieces along the minimiser [PROVED under simplicity; the hypothesis is NUMERICALLY false at the precision of any model, §2.3]

**Lemma 2.2.** Suppose λ_A(T) is a simple eigenvalue of the operator of 𝔞 on P_T for T in an interval I. Then the
minimiser F*_T (unit, up to phase) depends continuously on T ∈ I in the form norm, and T ↦ 𝔞^♯(F*_T), ℛ(F*_T),
Π(F*_T), 𝔢(F*_T) are continuous on I. If moreover 𝔞^♯(F*_{T_1}) > 0 > 𝔞^♯(F*_{T_2}) for T_1 < T_2 in I, there is
T_× ∈ (T_1, T_2) with 𝔞^♯(F*_{T_×}) = 0, i.e. ℛ(F*_{T_×}) = −λ_A(T_×) and Π(F*_{T_×}) = −𝔢(F*_{T_×}) − λ_A(T_×).
Proof. Let T_n → T in I. The unit minimisers F_n := F*_{T_n} satisfy 𝔞(F_n) = λ_A(T_n) → λ_A(T) (continuity of λ_A,
STATEMENT_001). All F_n are supported in a fixed I_{T′}; the sublevel sets of 𝔞 + C‖·‖² on L²(I_{T′}) are compact
(Kolmogorov–Riesz: the symbol m^♯ − Λ-part is ≥ c log(2 + |τ|) − C), so a subsequence converges in L², and by lower
semicontinuity of 𝔞 and the nesting (every L²-limit of P_{T_n}-vectors with T_n → T lies in P_T: the Tate
functionals are continuous and the supports shrink to I_T up to a set of measure → 0, where the L² mass → 0 by the
form bound on the boundary slabs) the limit is a unit minimiser at T, hence ±F*_T by simplicity. Then 𝔞(F_n) → 𝔞(F)
and F_n → F in L² give convergence in the form norm, and 𝔞^♯, 𝔢, Π are form-continuous. The last claim is the
intermediate value theorem. ∎

### 2.3 The pieces on the minimiser across the windows (NUMERICAL)

Model and scripts: ROUND_002_A's two-sector truncation, J = 500 even modes, L = 4000 odd modes (truncation error
≈ 1/L in the odd sums); scratchpad/p211/r7b.py (scan), r7b_cluster.py (ranges over the near-null cluster),
r7b_deg.py (block/response split). All identities of §1 are verified to 10⁻¹³ at every T (columns "checks").

Table 2.3 (unit minimiser F* = bottom eigenvector of a_T on P_T in the model; all pieces on F*; last columns: bottom and
negative count of the Λ-free form 𝔞^♯ on P_T, the count on L²(I_T), the Tate-pin bound of Lemma 1.3(iii) and the
trivial bound −(T/π)∫|m^♯|_−):

| T | N_T | σ_T | λ_A (model) | gap to 2nd | 𝔞^♯(F*) | ℛ(F*) | Π(F*) | 𝔢(F*) | Arch(F*) | inf 𝔞^♯\|P_T | n_−(𝔞^♯\|P_T) / L² | pin / trivial |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.75 | 2,3,4 | −1.35283 | 7.4·10⁻¹⁰ | 9.3·10⁻⁸ | +0.1026 | +0.1026 | +0.0743 | +0.0284 | +0.0743 | −0.1804 | 1 / 3 | −0.36 / −1.95 |
| ½log5+10⁻⁴ | 2,3,4,5 | −1.35755 | 3.1·10⁻¹² | 6.4·10⁻¹⁰ | +0.0913 | +0.0913 | +0.0623 | +0.0291 | +0.0623 | −0.2448 | 1 / 3 | −0.44 / −2.09 |
| 0.85 | 2,3,4,5 | −1.36056 | 1.7·10⁻¹⁴ | 5.4·10⁻¹² | +0.0837 | +0.0837 | +0.0541 | +0.0296 | +0.0541 | −0.2940 | 2 / 3 | −0.52 / −2.21 |
| 0.875 | 2,3,4,5 | −1.36194 | 5.9·10⁻¹⁵ | 2.8·10⁻¹³ | +0.0799 | +0.0799 | +0.0501 | +0.0298 | +0.0501 | −0.3199 | 2 / 3 | −0.56 / −2.27 |
| 0.9 | 2,3,4,5 | −1.36316 | −4·10⁻¹⁶ | 2.0·10⁻¹⁴ | +0.0762 | +0.0762 | +0.0461 | +0.0301 | +0.0461 | −0.3450 | 2 / 3 | −0.60 / −2.34 |
| 0.925 | 2,3,4,5 | −1.36423 | 1·10⁻¹⁵ | 3·10⁻¹⁵ | +0.0735 | +0.0735 | +0.0433 | +0.0302 | +0.0433 | — | — | — |
| 0.95 | 2,3,4,5 | −1.36517 | 7·10⁻¹⁸ | 1.0·10⁻¹⁴ | +0.1263 | +0.1263 | +0.0996 | +0.0267 | +0.0996 | −0.3925 | 2 / 4 | −0.69 / −2.47 |
| 1.0 | 2,3,4,5,7 | −1.36674 | −9·10⁻¹⁵ | 1.5·10⁻¹⁵ | +0.2898 | +0.2898 | +0.2726 | +0.0172 | +0.2726 | −0.4370 | 2 / 4 | −0.78 / −2.60 |

Readings. (i) ROUND_005_C reported 𝔞^♯(F*) = +0.0815 at ½log5 + ε and −0.0041 at T = 1 on the bottom vector of
a_T|_{E_T}; the present bottom vector of a_T on P_T gives +0.0913 and +0.2898. The two computations are both correct
to their precision: at T = 1 four eigenvalues sit at machine zero (gap 10⁻¹⁵) and at ½log5 + ε the bottom of E_T
differs from the bottom of P_T by 5·10⁻¹⁰ in a_T, enough to rotate inside the ladder (next paragraph). The values
of the pieces on "the minimiser" are not reproducible across models at any T ≥ 0.85, and the crossing cannot be
located (§4.3). (ii) On the P_T-bottom, Π(F*) = Arch(F*) − λ_A is positive at every scanned T: with the density
booked on the archimedean side (ν = 0, §2.4) there is no crossing in [0.75, 1]. (iii) The Λ-free bottom inf 𝔞^♯|_{P_T}
is −0.18, −0.24, −0.29, −0.32, −0.35, −0.39, −0.44 (monotone, as prop:sharp(iii) says, heading to −1.372), with one
negative direction up to 0.805 and two from 0.85 on, against three to four on L²(I_T): the Tate pin removes one to
two negative directions. (iv) The pin bound of Lemma 1.3(iii) improves the trivial bound by a factor ≈ 4 and is
still a factor 1.8–2 below the computed bottom. (v) The mass of F* sits on the mesh modes |q| ≤ 6 (q = ±4: 0.33,
±3: 0.32–0.36, ±2: 0.11–0.17, ±5: 0.12–0.20, ±1, ±6: ≤ 0.06): the minimiser is a low-frequency packet in the band
1/T ≲ |τ| < τ^♯, as Lemma 1.3 predicts.

Ranges over the near-null cluster (r7b_cluster.py, J = 300, L = 2500): the lowest eigenvalues of a_T on P_T and the
range [min, max] of each piece over the span of the lowest k eigenvectors.

| T | lowest a_T eigenvalues | k | 𝔞^♯ range | Arch range | Π range | 𝔢 range |
|---|---|---|---|---|---|---|
| ½log5+10⁻⁴ | 3·10⁻¹², 6.5·10⁻¹⁰, 3.1·10⁻⁷, 3.2·10⁻⁵, 2.1·10⁻³, 6.1·10⁻² | 1 | +0.091 | +0.062 | +0.062 | +0.029 |
| | | 3 | [−0.109, +0.485] | [−0.156, +0.473] | [−0.156, +0.473] | [+0.012, +0.048] |
| | | 6 | [−0.205, +1.129] | [−0.262, +1.126] | [−0.262, +1.086] | [+0.003, +0.059] |
| 0.9 | 7·10⁻¹⁵, 3·10⁻¹⁴, 1.1·10⁻¹¹, 2.0·10⁻⁹, 3.5·10⁻⁷, 2.7·10⁻⁵ | 1 | +0.076 | +0.046 | +0.046 | +0.030 |
| | | 3 | [−0.134, +0.457] | [−0.183, +0.444] | [−0.183, +0.444] | [+0.012, +0.050] |
| | | 6 | [−0.232, +1.019] | [−0.293, +1.015] | [−0.293, +1.015] | [+0.004, +0.063] |
| 1.0 | −2·10⁻¹⁵, 1·10⁻¹⁵, 2·10⁻¹⁵, 1.5·10⁻¹⁴, 1.2·10⁻¹², 1.8·10⁻¹⁰ | 1 | +0.256 | +0.237 | +0.237 | +0.019 |
| | | 2 | [+0.009, +0.262] | [−0.037, +0.244] | [−0.037, +0.244] | [+0.018, +0.046] |
| | | 3 | [−0.152, +0.439] | [−0.203, +0.425] | [−0.203, +0.425] | [+0.013, +0.052] |
| | | 6 | [−0.250, +0.984] | [−0.314, +0.980] | [−0.314, +0.980] | [+0.004, +0.065] |

Reading. Inside the span of the three lowest eigenvectors (a_T ≤ 3·10⁻⁷ at ½log5 + ε, ≤ 10⁻¹¹ at 0.9, ≤ 2·10⁻¹⁵ at 1)
each Λ-free piece ranges over an interval of length ≈ 0.6 containing 0, and Π = Arch − a_T ranges with it. The sign
of 𝔞^♯ on "the minimiser" is decided by which vector inside this ladder one calls the minimiser, i.e. by
perturbations of the form of size 10⁻⁷ (½log5 + ε) down to 10⁻¹⁵ (T = 1). 𝔢 is the only piece that keeps its sign on
the cluster (it is ≥ 0 everywhere) and it is small there, 0.003–0.06.

### 2.4 The bookkeeping theorem: the carrying role is a choice of density [PROVED]

**Proposition 2.4.** Let ν be any Λ-free locally finite measure on [0, 2T) and write the comb measure as
Σ v_nδ_{log n} = dR_ν + ν (so dR_ν is "Λ minus the density ν"; ROUND_005_C takes ν = 2e^{u/2}du). Put
𝒜_ν(F) := Arch(F) + ∫Re c_F dν (Λ-free) and ℒ_ν(F) := ∫Re c_F dR_ν = Π(F) − ∫Re c_F dν. Then a_T = 𝒜_ν − ℒ_ν for
every ν, and on a minimiser
    𝒜_ν(F*) = Arch(F*) + ∫Re c_{F*}dν,   ℒ_ν(F*) = 𝒜_ν(F*) − λ_A(T).
In particular: (i) the sign of the "Λ-free part on the minimiser" and hence the existence and position of a
crossing window depend on ν; (ii) for ν = 0 the Λ-free part is Arch(F*) and the Λ-part is Π(F*) = Arch(F*) − λ_A(T);
(iii) for ν = 2e^{u/2}du the Λ-free part is 𝔞^♯(F*) = Arch(F*) + 𝔢(F*) ≥ Arch(F*), and the "fluctuation" ℒ_ν = ℛ
exceeds Π by the Λ-free, nonnegative 𝔢(F*); (iv) a crossing for ν exists at T iff ∫Re c_{F*}dν = −Arch(F*).
Proof. Linearity of F ↦ ∫Re c_F dμ in μ and the identities of §2.1. ∎

Consequence for ROUND_005_C §4.5. The statement "at T = 1 the fluctuation carries the sign" means ℛ(F*) < 0 <
𝔞^♯(F*) is false there and ℛ(F*) = 𝔞^♯(F*) − λ_A < 0; by (iii) this is Π(F*) + 𝔢(F*) < 0, a statement in which
the Λ-free energy 𝔢(F*) ∈ [0, 4] is booked on the arithmetic side. With ν = 0 the same numbers read Arch(F*) =
λ_A + Π(F*): the archimedean form on the minimiser equals the comb form on the minimiser up to λ_A, at every T,
and there is nothing to cross unless Π(F*_T) itself changes sign. Whether it does is the first row of the table of
§2.3 (Π(F*) column). The crossing window of the Next step of ROUND_005_C is therefore not a window where "the
archimedean side is neutral and the sign is purely arithmetic": it is the window where Arch(F*) = −𝔢(F*), a
Λ-free quantity on both sides, and the inequality to prove there, Π(F*) ≤ −𝔢(F*) − λ_A, has a Λ-free right side
of size ≈ 0.03 (§2.3) booked against the comb. Falsifier test of the reading: for cΛ, Prop. 2.4 holds verbatim
with Π ↦ cΠ (and F* the minimiser of Arch − cΠ); the decomposition is comb-generic and carries no sign, as it must.

---------------------------------------------------------------------------------------------------
## 3. The response cubic

### 3.1 The explicit cubic for one comb response [PROVED]

**Proposition 3.1.** Let φ = φ_q, ω = ω_q, u_n = log n, and F = Πφ_q = φ_q ψ_q with ψ_q(t) = ½Σ_{m∈N_T}v_m[m^{iω}1_{t>−T+u_m} +
m^{−iω}1_{t<T−u_m}] (ROUND_005_C Prop. 2). Then

    Π(Πφ_q) = (1/8T) Σ_{k,m,n∈N_T} v_k v_m v_n [ 2cos(ω log(m/nk)) (2T − max(u_m, u_n + u_k))_+
                                              + cos(ω log(mn/k)) (2T − max(u_m, u_k) + min(0, u_k − u_n))_+
                                              + cos(ω log(mnk)) (2T − u_m − u_n − u_k)_+ ],

and the mesh form of 𝔢 on the response is ½Σ_p 𝒮_p|x_p(Πφ_q)|² = ⅛(G𝒞G 𝒮 G𝒞G)_{qq} (quadratic in v; it equals 𝔢(Πφ_q)
only after projection to P_T, since the identity of Prop. 1.4 uses the Tate conditions). Hence ℛ(P_𝒞Πφ_q) is a cubic
plus a quadratic polynomial in (v_n)_{n∈N_T} whose cubic part is the display above corrected by the finite projection.
Proof. c_F(u) = (1/2T)e^{−iωu}∫ψ_q(t) conj ψ_q(t − u) 1_{I_T}(t)1_{I_T}(t − u)dt; expand the product of the two step
functions into its four terms, with phases (m/n)^{iω}, (mn)^{iω}, (mn)^{−iω}, (n/m)^{iω}, and compute the lengths of the
four intervals {t ∈ I_T : t − u_k ∈ I_T, t ∈ S^±_m, t − u_k ∈ S^±_n} with S^+_m = (−T + u_m, T), S^−_m = (−T, T − u_m):
they are (2T − max(u_m, u_n + u_k))_+, (2T − max(u_m, u_k) + min(0, u_k − u_n))_+, (2T − u_m − u_n − u_k)_+ and
(2T − max(u_m + u_k, u_n))_+; multiply by e^{−iωu_k} = k^{−iω}, take real parts and symmetrise the first and fourth in
m ↔ n. ∎
NUMERICAL validation (scratchpad/p211/r7b_cubic.py, J = 300, L = 2000): at T = ½log5 + 10⁻⁴ and T = 1, for q = 0, 3, 5,
9, 10, 14 the display agrees with the sector formula ⅛(G𝒞G𝒞G𝒞G)_{qq} to the truncation 10⁻³–10⁻⁴.

### 3.2 Where the near-coincidences sit, and when they enter [PROVED]

**Corollary 3.2.** (i) The three classes are the three triple phases of ROUND_005_C Prop. 5(ii) / ROUND_005_A Prop. 3.4:
m ≈ nk (first term, weight 2), mn ≈ k (second), mnk ≈ 1 (third). (ii) The third class is empty for T ≤ ½ log 8 = 1.0397
(every u_m + u_n + u_k ≥ 3log 2). (iii) A triple (m; n, k) with m ≠ nk enters the first class only when both m and nk
are below e^{2T}, with weight (2T − log max(m, nk))_+: at T = ½log 5 (+ε) the near triples (5; 2, 2), (5; 2, 3), (5; 3, 2)
have weight 0 (resp. 10⁻⁴), at T = 1 the triples (5; 2, 2), (5; 2, 3), (5; 3, 2), (7; 2, 3), (7; 3, 2) have weights
2 − log 5 = 0.391, 2 − log 6 = 0.208, 2 − log 7 = 0.054; (7; 2, 4) and (7; 4, 2) have weight (2 − log 8)_+ = 0. (iv) The only
exact coincidence with all three entries in N_T for T ≤ 1 is 4 = 2·2, the prime-power tie v_4 = v_2/√2, with weight
2T − log 4 in both classes and phase 0 at every mesh frequency; the next ones, 8 = 2·4 and 9 = 3·3, enter at T > ½log 8,
½log 9.
Proof. Read off the cutoffs of Prop. 3.1. ∎

NUMERICAL (same script). At T = ½log5 + 10⁻⁴ the near-coincidence triples contribute < 10⁻⁴ to Π(Πφ_q) for every q,
and the exact triple (4; 2, 2) contributes +0.046 (class 1) and +0.023 (class 2); the bulk of the cubic is the
m = k part of class 2 (phases log n, i.e. the response's self-correlation against the comb). At T = 1 the near triples
are no longer small: on the block mode q = 10 (ω = 15.71) they contribute −0.343 (class 1) and −0.257 (class 2) against
+0.102 and +0.051 from the exact triple, and the whole Π(Πφ_10) is −0.191. So the near-coincidences m ≈ nk, m ≠ nk,
enter the response cubic at T > ½log 5 with the window weight (2T − log max(m, nk))_+, and at T = 1 they dominate the
exact ones on the block modes.

### 3.3 The degree hierarchy on the minimiser, against λ_A (NUMERICAL; this is the quantitative content of §3.4)

Split F* = x + y with x = P_{N′}F* (block part, a_T-entries affine in v given 𝒩) and y = F* − x (response part, in V_T to
10⁻¹⁰; a_T-entries of degree ≤ 3). At T = ½log5 + 10⁻⁴ (r7b_deg.py, J = 500, L = 4000, gauge c = 1.224):

    ‖x‖² = 0.999254,  ‖y‖² = 7.46·10⁻⁴ (7.46·10⁻⁴ in V_T, 3.5·10⁻¹⁰ outside E_T);
    a_T(F*) = +1.409·10⁻³ (block–block) − 2.817·10⁻³ (cross, degree 2) + 1.409·10⁻³ (response–response, degree 3) = 3·10⁻¹²;
    Π(F*)   = +0.060484 + 0.002398 − 0.000598 = +0.062284;   Arch(F*) = +0.061892 − 0.000418 + 0.000810 = +0.062284;
    𝔢(F*)   = +0.029049 + 0.000007 + 0.000003 = +0.029059;   λ_min(a_T|_{N′}) = 7.05·10⁻⁶,  a_T(x)/‖x‖² = 1.41·10⁻³.

Reading. The three degree contributions to a_T(F*) are of the same size, 1.4·10⁻³, and cancel to 3·10⁻¹² (a square:
a_T(x) = a_T(y) = −Re⟨x, a_T y⟩, i.e. x + y is null and x − y carries 4·1.4·10⁻³). No degree dominates; the block part of
the minimiser is not the block minimiser (1.4·10⁻³ against 7·10⁻⁶); the response part, 0.07 % of the norm, moves the
value by 10⁹ times λ_A. Relative to λ_A every term is enormous; relative to each other none is small.

### 3.4 What the cubic can and cannot be made to prove [NO-GO, class named]

NO-GO (class: arguments that sign a proper sub-part of ℛ(F) or of a_T(F) on E_T — a degree, a coincidence class, the
exact-coincidence part, the local Euler factors at 2, 3, 5, 7 — with an error term that is not itself ≤ λ_A(T)).
PROVED logic: by §3.3 the sub-parts are of size ≥ 10⁻³ and cancel to λ_A ≤ 4·10⁹Te^{−15.449T} (cor:margin1, CITED);
an argument that controls a sub-part to precision ε and ignores the rest proves a_T(F*) ≥ −(size of the rest) only,
which is ≥ 0 iff the rest is signed, i.e. iff the full inequality is proved. The same holds for the falsifiers: for
cΛ with |c − 1| < 10⁻⁵ the block part a_T(x)/‖x‖² and the per-class cubic parts move by less than their size and keep
their signs while λ_A(cΛ) < 0 (ROUND_005_C §4.6: −2.4·10⁻³ at c = 0.99); for a_3 and the Beurling shift 3 → 3.2 every
identity of §3.1–3.2 holds verbatim with the positions u_n moved (Lemma 6(e) of ROUND_005_C) and (SL_T) fails by
0.51 and 0.24. So no sub-part argument distinguishes Λ from its falsifiers; the distinction lies in the exact
cancellation of the whole, which is the statement itself.

What remains as the exact requirement (OPEN, restated with the pieces explicit): for every unit F ∈ E_T,
    Π(F) ≤ Arch(F),
with Π(F) a cubic in (v_n)_{n∈N_T} whose near-coincidence classes are listed in Cor. 3.2 and whose T-dependence is
through the window cutoffs, and Arch(F) = 𝔞^♯(F) − 𝔢(F) a Λ-free form evaluated on Λ-shaped vectors. The local
structure at the small primes enters only through (a) the prime-power ties v_{p^k} = v_p p^{−(k−1)/2}, i.e. the exact
triples (4; 2, 2) and, beyond T = 1.04, (8; 2, 4), (9; 3, 3); and (b) the near triples (5; 2, 2), (5; 2, 3), (7; 2, 3),
(7; 2, 4) with the window weights of Cor. 3.2(iii). Nothing in (a)–(b) is a sign: the same ties and weights are
present for cΛ (scaled by c³) and for a Beurling system with the positions 2, 3, 4, 5, 7 kept and 3 → 3.2 moved.

---------------------------------------------------------------------------------------------------
## 4. Assessment

### 4.1 Against R1–R5 of OBJECT_SPEC_001

R1 (dimension grows): unchanged from ROUND_005_C (E_T, dim ≤ 2|𝒩| + 2). R2 (exact Λ, non-linear at the sign step): the
cubic of Prop. 3.1 is the explicit non-linear object; §3.3 shows that it is not separable from the affine part at any
precision above λ_A. R3 (exact reduction): Theorem 2 of ROUND_005_C stands (with the Tate responses in E_T,
REVIEW_004 (4)); the margin-carrying version is not obtained. R4 (joint archimedean/Euler): the budget does not
realise it — Prop. 2.4 shows the archimedean data enter (SL′_T) only as the Λ-free form Arch = 𝔞^♯ − 𝔢 evaluated on
Λ-shaped vectors, the same as in a_T = Arch − Π; no new coupling. R5 (falsifier test): the identities of §1–3 are
comb-generic (they hold for cΛ, a_P, Beurling, finite modifications) and are labelled as tools; the only sign-bearing
statement, Π ≤ Arch on E_T, is (★)_T itself on E_T and fails for every falsifier with the value of λ_A(T; w)
(ROUND_005_C §4.6).

### 4.2 What the budget is

PROVED: σ_T‖F‖² + κ(F) = 𝔞^♯(F), the polar-free form of Paper 46 prop:sharp; ℛ = 𝓕_T = Π + 𝔢 with 𝔢 the H^{−1}-type
energy of lem:polarelim; the window constant σ_T is m^♯(0) plus the window tail of K_1 (Lemma 1.1). So the "sign
budget" is the polar-free form of residue R1 at the window, and (SL′_T) is R1 restricted to E_T. Its reading in
ROUND_005_C §4.5 ("the kernel carries the sign at ½log5 + ε, the fluctuation at T = 1") is a bookkeeping statement
(Prop. 2.4): the quantity that moves between the two readings is the Λ-free energy 𝔢(F*) ≈ 0.03, and with the
density booked on the archimedean side (ν = 0) the pieces on the minimiser are Arch(F*) and Π(F*) = Arch(F*) − λ_A,
both positive at every scanned window and of the same size (§2.3, NUMERICAL, with the cluster caveat below).

### 4.3 The crossing window: NO-GO as a target

NO-GO (class: statements about the values of the budget pieces on "the minimiser" F*_T, and in particular the
location of a window T_× where one piece vanishes). Reasons, in order of strength. (a) PROVED (Prop. 2.4): the
crossing depends on the Λ-free density ν chosen in the bookkeeping; for ν = 0 there is no crossing in the scanned
range (Arch(F*) > 0 throughout, NUMERICAL). (b) NUMERICAL, and decisive at any model precision: the bottom of a_T on
P_T is a geometric ladder (3·10⁻¹², 6·10⁻¹⁰, 3·10⁻⁷, 3·10⁻⁵, 2·10⁻³ at ½log5 + ε; four eigenvalues at machine zero at
T = 1), and over the span of the lowest three the Λ-free piece 𝔞^♯ ranges over [−0.11, +0.49] at ½log5 + ε, [−0.13, +0.46]
at 0.9, [−0.15, +0.44] at 1 (§2.3). Any perturbation of the form by more than the gap — the model's truncation
(10⁻⁴), a weight change of 10⁻⁷ in one v_n, the scaling c = 1 ± 10⁻⁷ — rotates the minimiser inside the ladder and
moves 𝔞^♯(F*) across zero. The value 𝔞^♯(F*_T) is therefore not a computable function of T below the cluster
spread, and Lemma 2.2 (continuity under simplicity) is true and empty: the hypothesis holds in exact arithmetic
and is invisible at every reachable precision. (c) By (a)–(b) the "window where the archimedean side is neutral and
the sign is purely arithmetic" does not exist as a well-defined object; the Next step of ROUND_005_C is withdrawn.

Falsifier test of this NO-GO: it is a statement about the geometry of the bottom of a_T, which is comb-generic
(the ladder exists for cΛ, a_P and the Beurling shift as well, with negative bottoms); it does not claim a sign and
does not have to fail for the falsifiers.

### 4.4 What is left standing, and what was learnt

Standing (PROVED tools): Lemma 1.1 (σ_T closed form, monotone, T_0 = 0.052), Prop. 1.2 (identification with 𝔞^♯,
T-independence), Lemma 1.3 (nodal structure, Tate pin d_T(τ), count bounds), Prop. 1.4 and Cor. 1.5 (ℛ = Π + 𝔢, the
alternating mesh symbol 𝒮_q, the four equivalent forms of the sign lemma, the H²_0 form), Lemma 2.1 (one form,
nested spaces), Lemma 2.2 (continuity under simplicity), Prop. 2.4 (bookkeeping), Prop. 3.1 (response cubic),
Cor. 3.2 (classes, entry thresholds ½log5, ½log7, ½log8, ½log9, window weights).

Learnt: (1) the budget of ROUND_005_C is the polar-free form of the record and (SL′_T) is residue R1 on E_T;
(2) the pieces on the minimiser are not well-defined below the near-null ladder, which is why no per-minimiser
statement (crossing, carrying role, "the comb form is negative on F*") can be a target; (3) the near-coincidence
triples enter the response cubic with the explicit window weights (2T − log max(m, nk))_+ and are zero at ½log 5,
comparable to the exact triple at T = 1; (4) the negative cone of 𝔞^♯ on P_T is one- or two-dimensional at the
windows of the record (n_− = 1 at 0.75–0.805, 2 at 0.85–1), while the a_T-block has 11–41 modes: the block is made
of comb resonances, not of archimedean deficit, and on the Λ-free negative cone the requirement is 𝓕 < 0 strictly,
a necessary condition with margin (0.04 at ½log5 + ε), hence not a sign step (ROUND_004_A Prop. B).

### 4.5 Next lemma

The structure that survives this memo is the exact reduction of ROUND_005_C with the inequality Π ≤ Arch on E_T, and
the fact (§3.3) that its value is a cancellation between the affine block part and the cubic response part at
every scale above λ_A. The only statement in the memo that is both Λ-specific and finite is the entry structure of
Cor. 3.2: the thresholds ½log 5, ½log 7, ½log 8, ½log 9 at which new triples enter the cubic with weight growing
linearly in T from zero. A lemma that could be attacked, and is not in the index: the one-sided derivative of
λ_A(T) at an entry threshold T_e (where a new triple (m; n, k) or a new prime enters with zero weight) in terms of
the minimiser cluster — a Hadamard-type variation formula for the nested family (Lemma 2.1), with the new term
entering linearly in (T − T_e). Its value would be a PROVED statement about how λ_A decreases through each entry,
with the cluster spread as the only unknown; whether it carries a sign is not claimed. The index has no variation
formula for λ_A in T (grep "Hadamard", "d/dT": zero-geometry rows only).

---------------------------------------------------------------------------------------------------
## Result

PROVED piece (structure) and NO-GO (two classes). PROVED: the budget σ_T‖F‖² + κ(F) is the polar-free form 𝔞^♯ of
Paper 46 (prop:sharp) and ℛ = 𝓕_T = Π + 𝔢 (lem:polarelim), with σ_T = C_0 + 4 + ∫_{2T}^∞K_1 = 4 − γ − π/2 − log(8π) +
window tail, decreasing, positive for T < 0.052; the nodal lemma and the Tate pin |F̂(τ)|² ≤ d_T(τ)‖F‖² with
d_T(0) = T⁵/360 + O(T⁷); the sign lemma in four equivalent forms, the last being Π ≤ Arch on E_T; the T-independence
of all pieces on the nested family and the continuity of their values on the minimiser under simplicity; the
bookkeeping theorem (the carrying role and the crossing are functions of the density ν chosen); the explicit
time-domain cubic of the response with its three coincidence classes and their entry thresholds. NO-GO (i) the
crossing window and every per-minimiser budget statement (class: values of forms on F*_T; reasons: bookkeeping
dependence PROVED, near-null ladder NUMERICAL with spreads of order 0.5 above λ_A ≈ 10⁻¹²); (ii) sub-part
arguments on the cubic (class: signing a degree, a coincidence class, the exact-coincidence or local-factor part of
ℛ or a_T on E_T with error above λ_A): the three degree parts of a_T(F*) are +1.4·10⁻³, −2.8·10⁻³, +1.4·10⁻³ and
cancel to 3·10⁻¹².

## What was proved

Lemma 1.1, Prop. 1.2, Lemma 1.3, Prop. 1.4, Cor. 1.5, Lemma 2.1, Lemma 2.2 (conditional on simplicity), Prop. 2.4,
Prop. 3.1, Cor. 3.2, the NO-GO logic of §3.4 and §4.3; all identities validated in the model to 10⁻¹³ (§2.3) and the
cubic to the truncation (§3.1).

## What failed and why

- The crossing T_× cannot be located: the pieces on the minimiser are undefined below the near-null ladder (spread
  of 𝔞^♯ over the lowest three eigenvectors ≈ 0.6 against gaps 10⁻¹⁰–10⁻⁷), and the crossing itself is a property
  of the density booked into ℛ (Prop. 2.4); with ν = 0 there is none.
- The cubic has no dominant part: the degree contributions cancel exactly (§3.3); the near-coincidence triples are
  invisible at ½log 5 (window weight zero) and comparable to the exact triple at T = 1, but every identity is
  comb-generic and holds for the falsifiers where (SL_T) fails by 0.24–0.51.
- The monotonicity in T of the pieces on the minimiser is not provable because the pieces are not continuous at
  any precision where they could be compared; only the T-independence of the functionals (Lemma 2.1) and the
  monotonicity of σ_T and λ^♯(T) (Lemma 1.1, prop:sharp) are PROVED.

## Next concrete step

Derive the one-sided variation formula for λ_A(T) on the nested family at an entry threshold T_e ∈ {½log 7, ½log 8,
½log 9} (Lemma 2.1 setting: one form, P_T ⊂ P_{T′}), expressing dλ_A/dT⁺ through the minimiser cluster and the
newly entering term of Prop. 3.1 with weight (T − T_e); check it in the model across T_e = ½log 7 = 0.9730 with the
cluster of §2.3; record whether the decrease of λ_A through an entry is governed by the near-coincidence weight or
by the archimedean boundary flux. Index entry for this memo: P211-7B (§4.3 NO-GO classes, §3.4 NO-GO class).
