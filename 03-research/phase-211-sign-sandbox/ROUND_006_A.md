# Round 6, memo A: the size of the comb form, λ_max(Π_T) against A_T

Object. Notation of STATEMENT_001 §1. For F ∈ L²(I_T) (extended by zero), c_F(u) = ∫ F(t)F(t−u) dt,
u_n = log n, N_T = {n ≥ 2 : u_n < 2T}, v_n = 2Λ(n)n^{−1/2}, X = e^{2T},

  Π_T(F) := Σ_{n∈N_T} v_n c_F(u_n) = (1/2π) ∫ M_T(τ)|F̂(τ)|² dτ,   M_T(τ) = Σ_{n∈N_T} v_n cos(τ u_n),
  A_T := Σ_{n∈N_T} v_n = M_T(0),   V(s) := Σ_{u_n ≤ s, n∈N_T} v_n  (0 ≤ s ≤ 2T),
  π_+(H) := sup{Π_T(F) : F ∈ H, ‖F‖ = 1},  π_−(H) := −inf{…},  for H = L²(I_T) or P_T.

a_T = Arch_T − Π_T on P_T, and Arch_T(F) = (1/2π)∫ m |F̂|² on P_T (Paper 46 prop:nodes, CITED).
Everything below is a statement about the size of Π_T. It is comb-generic and carries no sign (§5).

## 0. Corpus check

- ROUTES-TRIED-INDEX: grep "‖Π_T‖", "λ_max(Π_T)", "A_T", "arena", "truncated shift", "Toeplitz bound", "Gram"
  returns: P211-5E (ROUND_005_E, which asked for the present quantity), the Gram-inertia and Gram/BRS entries of
  phase 199 (GRAM_INERTIA_001, PROOF_L_SHARP_W_001: sign by Gram inertia; not a size bound), INV_M_001 (stability of
  Gram symbols). No entry bounds λ_max(Π_T) beyond A_T for large T. The modulation + Riemann–Lebesgue device used in
  Theorem 1 is recorded (COSH_DEFECT_001 "modulation PROVED", LEMMA_13_1_CUMULANT_001): it is used here as a tool,
  not as a route; no index item is retried.
- Paper 46 prop:coer-prime (CITED): (i) ‖Π_T‖ ≤ A_T; (ii) the truncated-shift (path-graph) bound
  ‖Π_T‖ ≤ Σ v_n cos(π/(⌈2T/u_n⌉+1)), stated for T ≤ ½log5. Theorem 2 below is a different inequality (one
  Cauchy–Schwarz on the common window instead of one path graph per shift); it is never weaker than the large-T
  reading of (ii) in its second form and is smaller than (ii) at every tested T > ½log 3 (Table 2).
- Paper 46 thm:arena / cor:arena (CITED): lower count N*(T) ≥ ⌊Tτ_*/π − ½⌋, τ_* = m^{−1}(A_T), any threshold
  admissible in the proof. STATEMENT_001 §3: ∫_ℝ e^{u/2}c_F(u)du = A(F)B(F) = 0 on P_T (the cosh half of
  Theorem 4 below); the sinh half (Theorem 4) is not in the corpus (grep "sinh(|", "e^{|x−y|/2}": no hit).
- The "Gram/Toeplitz bound on the shifted copies" proposed by ROUND_005_E: ‖F − tΣ_n w_n S_{u_n}F‖² ≥ 0 gives
  (Σ w_n c_F(u_n))² ≤ Σ w_m w_n c_F(u_m − u_n), i.e. Π_T bounded by the comb Gram form of the differences —
  circular (it bounds Π_T by a form of the same size). Recorded in §6, not used.

## 1. On P_T the comb reaches its full L² top (PROVED)

Lemma 1.0 (PROVED). |Π_T(F)| ≤ Π_T(|F|). Hence π_−(L²) ≤ π_+(L²) and π_+(L²) = sup over F ≥ 0.
Proof. Π_T(F) = Σ v_n ∫F(t)F(t−u_n)dt with v_n > 0; take absolute values inside. ∎

Theorem 1 (PROVED). π_+(P_T) = π_+(L²(I_T)) and π_−(P_T) = π_−(L²(I_T)).
Proof. "≤" is inclusion. Let F_0 real, ‖F_0‖ = 1, and F_τ(t) = √2 F_0(t) cos(τt). Then
‖F_τ‖² = 1 + ∫F_0² cos 2τt → 1, and
  c_{F_τ}(u) = c_{F_0}(u) cos(τu) + ∫ F_0(t)F_0(t−u) cos(τ(2t−u)) dt,
whose second term → 0 as τ → ∞ (Riemann–Lebesgue; the integrand is in L¹). Also A(F_τ), B(F_τ) → 0
(Riemann–Lebesgue), so with P the orthogonal projection onto P_T (codimension 2, spanned complement
{e^{t/2}, e^{−t/2}}), ‖F_τ − PF_τ‖ → 0, and since Π_T is bounded, Π_T(PF_τ) − Π_T(F_τ) → 0.
Choose τ_k → ∞ with max_{n∈N_T} ‖τ_k u_n/2π‖_{ℝ/ℤ} → 0 (Dirichlet's simultaneous approximation, CITED, applied
to θ_n = u_n/2π; if the integers q it produces stay bounded, some q gives qθ_n ∈ ℤ for all n and τ = jq, j → ∞,
works). Then Π_T(PF_{τ_k})/‖PF_{τ_k}‖² → Σ v_n c_{F_0}(u_n) = Π_T(F_0). Supremum over F_0 gives π_+; for π_−
the same sequence carries the infimum. ∎

Consequence (correction to ROUND_005_E Table 1.1). The values λ_max(Π_T) = 0.901, 1.516, 1.730, 2.057 reported on
P_T there are Galerkin values (78 smooth modes). The true π_+(P_T) = π_+(L²) is reached only through modulated
packets of arbitrarily high frequency. NUMERICAL (Legendre–Galerkin on L²(I_T), N = 60/100):

| T | A_T | π_+(L²) | π_+(P_T), Galerkin N = 100 | π_+(L²)/A_T |
|---|---|---|---|---|
| log 2 | 2.249 | 0.9009 | 0.9009 | 0.401 |
| 0.9 | 4.381 | 1.554 | 1.523 | 0.355 |
| 1.2 | 8.521 | 2.695 | 2.057 (1.954 at N = 60: not converged, as Theorem 1 predicts) | 0.316 |

For the Weyl count of ROUND_005_E Theorem 3.1 on the full operator the relevant number is π_+(P_T) = π_+(L²).

## 2. Upper bound: θ → ½ (PROVED)

Theorem 2 (overlap bound; PROVED). For every T > 0,

  π_+(L²(I_T)) ≤ ½ max_{0≤s≤2T} [V(s) + V(2T − s)] ≤ ½ (A_T + V(T)),

and V(T) = Σ_{n ≤ e^T} v_n. The same bounds hold for π_− and for ‖Π_T‖, on L²(I_T) and on P_T.
Proof. For F ≥ 0 (Lemma 1.0), c_F(u) = ∫_{−T+u}^{T} F(t)F(t−u)dt ≤ ‖F1_{[u−T,T]}‖·‖F1_{[−T,T−u]}‖
≤ ½(∫_{u−T}^{T}F² + ∫_{−T}^{T−u}F²). Summing with weights v_n,
  Π_T(F) ≤ ½ ∫_{−T}^{T} F(t)² [Σ_n v_n 1{u_n ≤ T + t} + Σ_n v_n 1{u_n ≤ T − t}] dt = ½∫F(t)²[V(T+t) + V(T−t)]dt,
and the bracket is at most max_s [V(s)+V(2T−s)]. For s ≤ T: V(2T−s) ≤ A_T and V(s) ≤ V(T); symmetric for s ≥ T. ∎

Corollary 2.1 (PROVED, with Chebyshev's bounds CITED). V(T)/A_T ≤ C e^{−T/2} for T ≥ 1, hence
limsup_{T→∞} π_+(P_T)/A_T ≤ ½. (Partial summation with c_1x ≤ ψ(x) ≤ c_2x gives c′e^{s/2} ≤ V(s) ≤ c″e^{s/2}.)

Table 2 (exact finite sums; the bounds are PROVED inequalities, the numbers are evaluations):

| T | A_T | ½max_s[V(s)+V(2T−s)] | path bound prop:coer-prime(ii) | ½(A_T+V(T)) | overlap/A_T |
|---|---|---|---|---|---|
| log 2 | 2.249 | 1.124 | 1.124 | 1.615 | 0.500 |
| 0.9 | 4.381 | 2.191 | 2.394 | 2.681 | 0.500 |
| 1.2 | 8.521 | 4.260 | 4.826 | 5.385 | 0.500 |
| 2.0 | 24.38 | 12.19 | 13.72 | 15.12 | 0.500 |
| 4.0 | 213.5 | 106.8 | 113.4 | 119.0 | 0.500 |
| 6.0 | 1608.6 | 804.3 | 823.7 | 841.9 | 0.500 |

At every tested T the maximum is attained at s ∈ {0, 2T}, i.e. the overlap bound equals A_T/2 (NUMERICAL). It equals
A_T/2 exactly whenever the head–tail inequality (HT_T): Σ_{n ≤ a} v_n ≤ Σ_{X/a < n < X} v_n for all 1 ≤ a ≤ √X holds.
(HT_T) for all T is OPEN as stated (it is a Chebyshev-type inequality on short-ish intervals; true for large X by
the prime number theorem, and checked at the tabulated T only).

## 3. Lower bound: θ ≥ ¼ (PROVED; asymptotics given PNT, CITED)

Theorem 3 (PROVED). For every T > 0, with X = e^{2T},

  π_+(P_T) = π_+(L²) ≥ R_T := N_T / (sinh T + T),
  N_T = e^{T} Σ_{n<X} Λ(n)/n − e^{−T} ψ(X⁻) + ½ Σ_{n<X} Λ(n)(1 + 1/n) log(X/n).

Proof. F = cosh(t/2) on I_T: c_F(u) = sinh(T − u/2) + (T − u/2)cosh(u/2) for 0 ≤ u ≤ 2T, c_F(0) = sinh T + T.
With v_n = 2Λ(n)n^{−1/2}: v_n sinh(T − u_n/2) = Λ(n)(e^T/n − e^{−T}) and v_n (T − u_n/2)cosh(u_n/2) =
½Λ(n)log(X/n)(1 + 1/n). Sum, divide, and apply Theorem 1 (F itself is not in P_T; Theorem 1 transports the value). ∎

Corollary 3.1 (PROVED given PNT, CITED). ½Σ_{n<X}Λ(n)log(X/n) = ½∫_1^X ψ(t)dt/t = (X/2)(1+o(1)), the other terms of
N_T are O(Te^T), sinh T + T = (e^T/2)(1+o(1)) and A_T = 4e^T(1+o(1)). Hence π_+(P_T) ≥ e^T(1+o(1)) and

  ¼ ≤ liminf π_+(P_T)/A_T ≤ limsup π_+(P_T)/A_T ≤ ½.

Evaluations of R_T (exact sums): 0.763, 1.432, 2.609, 7.90, 59.1, 412.1 at T = log 2, 0.9, 1.2, 2, 4, 6;
R_T/A_T = 0.34, 0.33, 0.31, 0.32, 0.28, 0.26; R_T e^{−T} = 0.38, 0.58, 0.79, 1.07, 1.08, 1.02.
NUMERICAL: the continuum model (comb replaced by its density 2e^{u/2}du, kernel e^{|x−y|/2}) has L² top
e^T(1.0008) at T = 10, so ¼ is the continuum value; whether arithmetic raises the constant is OPEN.

Answer to the question of ROUND_005_E. λ_max(Π_T)/A_T does NOT tend to 0. The decrease 0.40 → 0.24 in ROUND_005_E
was the Galerkin value; the true ratio is 0.40, 0.36, 0.32 at log 2, 0.9, 1.2 and stays in [¼ − o(1), ½] forever.

## 4. Where the top lives: the smooth part of the comb is ≤ 0 on P_T (PROVED)

Theorem 4 (PROVED). For F ∈ P_T, with u_F(x) := ∫ sinh(|x−y|/2)F(y)dy,

  ∫_0^{2T} 2e^{u/2} c_F(u) du = ∫∫ e^{|x−y|/2}F(x)F(y) dx dy = −∫_{−T}^{T} (u_F′² + ¼u_F²) dx ≤ 0.

Proof. e^{|s|/2} = cosh(s/2) + sinh(|s|/2), and cosh((x−y)/2) = ½(e^{x/2}e^{−y/2} + e^{−x/2}e^{y/2}) contributes
A(F)B(F) = 0. G(s) = sinh(|s|/2) satisfies G″ − G/4 = δ (G′ jumps by 1), so u_F″ − u_F/4 = F. For x ≥ T,
u_F(x) = ½e^{x/2}B(F) − ½e^{−x/2}A(F) = 0; likewise for x ≤ −T; u_F ∈ C¹, so u_F(±T) = u_F′(±T) = 0 and
∫F u_F = ∫(u_F″ − u_F/4)u_F = −∫(u_F′² + u_F²/4). ∎

Reading. Write the comb measure as 2e^{u/2}du + ρ_T on (0, 2T). On P_T the density part — the part that makes
A_T ≈ 4e^T and π_+(L²) ≈ e^T — is a nonpositive form. So the top π_+(P_T) ≈ e^T is reached on P_T only by the
modulated packets of Theorem 1: the comb's size on P_T is carried by Diophantine coincidences τ u_n ≈ 0 mod 2π at
high frequency τ, where the archimedean form m(τ) ≈ log τ is large. This is the structural fact that the
counting question must use (§7).

## 5. Sharpened arena count (PROVED, explicit constants)

Lemma 5.1 (archimedean upper Weyl count; PROVED). Let α_1 ≤ α_2 ≤ … be the eigenvalues of Arch_T on P_T and
N_Arch(s) = #{k : α_k < s}. For s ≥ −1,

  N_Arch(s) ≤ 4e^{1.172} · T · e^{s} · (s + 1 − C_0) ≤ 12.92 · T · e^{s} · (s + 6.373),   C_0 = m(0) = −5.37218…

Proof. Let E be the span of the eigenvectors with α_k < s, F ∈ E, ‖F‖ = 1, so (1/2π)∫m|F̂|² < s. m is even,
increasing on [0, ∞) (lem:mbounds(i), CITED) with minimum m(0) = C_0, so Ω := {m < s+1} = (−τ′, τ′). With
q = (1/2π)∫_Ω|F̂|²: s > (s+1)(1−q) + C_0 q, so q > 1/(s+1−C_0). Hence the time–frequency limiting operator
B = 1_{I_T}𝓕^{−1}1_Ω𝓕1_{I_T} satisfies ⟨BF,F⟩ ≥ ‖F‖²/(s+1−C_0) on E, so by min–max B has at least dim E
eigenvalues ≥ 1/(s+1−C_0), and dim E ≤ (s+1−C_0)·tr B = (s+1−C_0)·2T·2τ′/2π. By lem:mbounds(ii) (CITED), for
τ ≥ 2π, m(τ) ≥ log(τ/2π) − 1/τ − 1/(2τ²) ≥ log(τ/2π) − 0.172, so τ′ ≤ 2πe^{s+1.172} (also when τ′ < 2π, since
s + 1.172 ≥ 0). ∎

Theorem 5 (sharpened arena count; PROVED). For every T > 0 and δ ≥ −1 − π_+, with π_+ = π_+(P_T) and
m_δ(T) = #{eigenvalues of a_T on P_T below δ},

  m_δ(T) ≤ N_Arch(δ + π_+) ≤ 12.92 · T · exp(δ + ½(A_T + V(T))) · (δ + ½(A_T + V(T)) + 6.373),

so m_δ(T) ≤ exp(2e^T(1 + o(1))) (Chebyshev, CITED), against the arena lower count N*(T) ≥ exp(4e^T(1+o(1))) of
modes below A_T (cor:arena). Proof: ROUND_005_E Theorem 3.1, Theorem 2, Lemma 5.1, monotonicity. ∎

Theorem 6 (limit of the pointwise-comparison class; PROVED given PNT). Any bound m_δ ≤ N_Arch(δ + θ) obtained
from a form inequality a_T ≥ Arch_T − θ on P_T needs θ ≥ π_+(P_T) ≥ e^T(1+o(1)), and then
N_Arch(δ + θ) ≥ ⌊T m^{−1}(δ + θ)/π − ½⌋ ≥ 2T exp(e^T(1 + o(1))) (the proof of thm:arena with threshold δ + θ in
place of A_T, and m^{−1}(s) = 2πe^{s}(1+o(1)) by lem:mbounds(ii)).
Proof. a_T ≥ Arch_T − θ evaluated on the packets PF_{τ_k} of Theorem 1 gives Π_T(PF_{τ_k}) ≤ θ‖PF_{τ_k}‖², so θ ≥ π_+.
The lower count is the cited argument verbatim. ∎

Answer. The sharp band is doubly exponential: n_P(T) = N_Arch(π_+) lies between exp(e^T(1+o(1))) and
exp(2e^T(1+o(1))). The single exponential ≈ e^{4T} seen in ROUND_005_E on T ≤ 1.2 is a small-T, Galerkin-truncated
effect, not the asymptotic size. Improving the constant θ ∈ [¼, ½] cannot make the Weyl cap single exponential:
NO-GO for the class "cap the cluster by an archimedean count via a pointwise comparison a_T ≥ Arch_T − θ".

## 6. Falsifier test and what failed

Rule 4 applies to sign steps; nothing here is a sign step. All of Theorems 1–6 hold verbatim for (a) cΛ (scale
A_T, V, π_+, N_T by c), (b) a_P (deleting n < P changes V(T) and the o(1) terms only), (c) a Beurling system with
a prime number theorem (replace ψ by its counting function in Corollaries 2.1, 3.1, 5), (d) a finite modification
of the v_n (o(1) change). This is the expected behaviour of a size statement: it bounds the object, it carries no
sign. Theorem 4 is likewise comb-generic (it concerns the density part only).

Failed or not obtained:
- The Gram/Toeplitz bound on shifted copies (ROUND_005_E next step) is circular: it bounds Π_T by the comb form of
  the difference set {u_m − u_n}, of the same size. Not used.
- A ratio λ_max/A_T → 0 is FALSE (Corollary 3.1). The hoped-for single-exponential cap through Theorem 3.1 is
  impossible (Theorem 6).
- The sharp constant in [¼, ½] and (HT_T) for all T: OPEN.

## 7. Next lemma (OPEN)

The comb on P_T is large only at high frequency on Diophantine-rare sets (Theorems 1, 4), where Arch is also
large. The count of the cluster must therefore use the joint symbol s_T(τ) = m(τ) − M_T(τ), not two separate
norms. Lemma (phase-space count; OPEN): for η > 0,

  m_δ(T) ≤ C(η) · T · |{τ ∈ ℝ : m(τ) − M̃_T(τ) < δ + η}| + C′(η, T),

where M̃_T is M_T averaged at scale 1/(2T) (the resolution of type-2T functions |F̂|²). Ingredients: Landau–Widom
counting for time–frequency limiting to unions of intervals of length ≳ 1/T; distribution of the almost periodic
M_T (frequencies u_n generated by log p, linearly independent over ℚ — Kronecker–Weyl equidistribution CITED) with
a Hoeffding-type tail |{τ ≤ R : M_T(τ) > s}| ≲ R exp(−s²/(2Σ_p a_p²)), a_p = Σ_k v_{p^k}, Σ_p a_p² ≈ 8T², made
uniform in R. If both hold, the measure of {m − M̃_T < δ+η} is ≲ ∫ exp(−(log τ)²/(16T²)) dτ ≈ e^{4T²+O(T)}, a cap
exp(O(T²)) instead of exp(2e^T) (ARGUED heuristic; the uniformity in R is the hard point).

## Result

PROVED piece (size of the comb; comb-generic, no sign), plus one NO-GO with class.

## What was proved

- Theorem 1: π_±(P_T) = π_±(L²(I_T)) (modulation, Dirichlet, Riemann–Lebesgue); ROUND_005_E's P_T values of
  λ_max(Π_T) at T ≥ 0.9 are Galerkin values (true 1.554, 2.695 at 0.9, 1.2, not 1.516, 2.057).
- Theorem 2: λ_max(Π_T), ‖Π_T‖ ≤ ½max_s[V(s)+V(2T−s)] ≤ ½(A_T + V(T)); = A_T/2 at all tested T; limsup ratio ≤ ½.
- Theorem 3 / Cor 3.1: λ_max(Π_T) ≥ N_T/(sinh T + T) (exact arithmetic expression) = e^T(1+o(1)); liminf ratio ≥ ¼.
- Theorem 4: on P_T the density part of the comb is a nonpositive form, −∫(u′² + u²/4).
- Lemma 5.1, Theorem 5: m_δ(T) ≤ 12.92·T·exp(δ + ½(A_T+V(T)))·(δ + ½(A_T+V(T)) + 6.373) = exp(2e^T(1+o(1))),
  versus Paper 46's arena count exp(4e^T(1+o(1))).
- Theorem 6 (NO-GO, class: Weyl caps from pointwise comparisons a_T ≥ Arch_T − θ): no such cap is below
  2T·exp(e^T(1+o(1))).

## What failed and why

λ_max(Π_T)/A_T does not tend to 0 (it lies in [¼, ½] asymptotically), so the single-exponential cluster cap hoped for
in ROUND_005_E cannot come from Theorem 3.1; the Gram/Toeplitz bound on shifted copies is circular. The numerical
ratio decrease of ROUND_005_E was a truncation artifact.

## Next concrete step

The phase-space count of §7: bound m_δ(T) by T times the measure of {τ : m(τ) − M̃_T(τ) < δ + η}, with a
uniform-in-R tail bound for the almost periodic sum M_T; first test numerically the Landau–Widom step at T = 0.9, 1.2
(count eigenvalues of a_T below δ against T·|{m − M̃_T < δ + η}| with a high-frequency basis, not the 78-mode one).
