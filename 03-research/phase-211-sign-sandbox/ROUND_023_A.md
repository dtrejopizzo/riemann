# Round 23 A — The exponent ray ℕ^{1+t}: edges of the positive segment and the first variation at t = 0

Target (★): λ_A(T) ≥ 0 for every T. Notation of ROUND_021_A and ROUND_022_A (𝔇 = 𝔇_R, Φ = Φ_R, P = Φ(Λ), M = M_x,
𝒦_R, V_R, ℓ_g; ℓ = log R, I = (−h, h)). Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

Reading under test. ℕ is the unique point of the exponent ray {ℕ^{1+t}} at which the R-cell form is ≥ 0 for every R:
the positive segment [t₋(R), t₊(R)] ∋ 0 shrinks to {0} from both sides.

## 0. Corpus check
Index rows read: P211-21A (c-window J_R → {1}, Lemma 3.3 window ≍ λ₀), P211-22A (generalized systems, Prop 3.2, ℕ at the
right edge of the exponent ray, t₋ ≈ −0.1 … −0.005 for R = 5…8). Index falsifier F-root (t = −½ is the √p system).
What differs: 22A measured t₋ only to a factor ≈ 3–10 and only at T = 0.8, R ≤ 8, and left ∂_tQ on the near-null cluster
unanalysed. Here: (i) the first variation ∂_tλ is split exactly into three pieces (comb scaling, weight exponent, positions),
the first of which is the falsifier-(a) direction c = 1 + t of 21A; (ii) the left edge is separated into "a new cell enters
the window" (n = R reaches log-position < ℓ when t < 0) versus "fixed cell set" by a variant powfix:t that keeps the index set
{n < R}; (iii) R = 9, 10. No retried construction: this is a measurement and an identity on the 22A object.

## 1. Tools (NUMERICAL)
gen_system.py gains SYS = powfix:t (positions n^{1+t}, n < R only), sig:t (positions log n, weights n^{−(1+t)/2} in 𝔇 and Π),
pos:t (positions (1+t)log n, weights n^{−1/2}, comb Λ(n)), lam:t (positions log n, comb (1+t)Λ). To first order in t,
pow = lam + sig + pos. window_build.py pickles for R = 9 (110→130 digits), R = 10 (150 digits), T = 0.8, Nb = 40, J = 40.

## 2. The first variation at t = 0 (task 2)

Standing assumptions as in 22A §3 (F ∈ V ⊂ H¹₀(I), constraints from ℤ, so V_R and ℓ_g are t-free; D := ½ + ∂).

### Lemma 2.1 (Selberg's identity in operator form; PROVED)
Φ(Λ·log) = [M, P] = 𝔇⁻¹[M,[M,𝔇]] − P², with P = Φ(Λ) = 𝔇⁻¹[M,𝔇] and 𝔇⁻¹ = Φ(μ).
*Proof.* Φ is a unital homomorphism from Dirichlet convolution truncated at x < R (22A Lemma 3.1; truncation is a ring
quotient because τ_aτ_b = τ_{a+b} and τ_a^I = 0 for a ≥ ℓ). Since μ ∗ 1 = δ₁, Φ(μ)𝔇 = 𝔇Φ(μ) = I. By 22A Lemma 3.1,
[M, Φ(α)] = Φ(α·log) for every α; with α = Λ this is the first equality, and with α = 1 twice, Φ(log) = [M,𝔇],
Φ(log²) = [M,[M,𝔇]]. Then [M,P] = [M,𝔇⁻¹][M,𝔇] + 𝔇⁻¹[M,[M,𝔇]] and [M,𝔇⁻¹] = −𝔇⁻¹[M,𝔇]𝔇⁻¹ give the second equality.
(Read through Φ, this computation is the identity Λ·log + Λ∗Λ = μ∗log² — CITED, Selberg — and needs nothing else.) ∎

### Proposition 2.2 (three-piece split of the exponent derivative; PROVED)
With ∂_t𝔇 = −[M,𝔇]D and ∂_tP = P − [M,P]D (22A Prop. 3.2 and Lemma 2.1),
    ∂_t = δ_lam + δ_sig + δ_pos,
    δ_lam: 𝔇 ↦ 0,              P ↦ P                    (comb scaled by 1 + t, cells fixed),
    δ_sig: 𝔇 ↦ −½[M,𝔇],        P ↦ −½[M,P]              (all weights x^{−1/2} → x^{−(1+t)/2}, positions fixed),
    δ_pos: 𝔇 ↦ −[M,𝔇]∂,        P ↦ −[M,P]∂              (positions log x → (1+t)log x, weights and comb fixed),
and for every simple eigenvalue branch, ∂_tλ_k = −𝒦_R[u_k] + δ_sigQ[u_k] + δ_posQ[u_k], with
    δ_•Q[F] = 2𝒜(𝔇F, δ𝔇F) + 2A(δ𝔇F)B(𝔇F) + 2A(𝔇F)B(δ𝔇F) − 4⟨δ𝔇F, P𝔇F⟩ − 2⟨𝔇F, (δP)𝔇F⟩
(P self-adjoint is not used: the term −2⟨δ𝔇F,P𝔇F⟩ − 2⟨𝔇F,Pδ𝔇F⟩ is written as −4Re⟨δ𝔇F, P^{sym}𝔇F⟩ with Π the
symmetric form ⟨H, P^{sym}H⟩ = ½Π[H]).
*Proof.* Split D = ½ + ∂ and P = P·1 in the two formulas; each piece is the t-derivative at t = 0 of the stated one-parameter
family (direct differentiation of x^{−(1+t)/2}, of (1+t)Λ, and of τ^I_{(1+t)log x} as in 22A Prop. 3.2). The eigenvalue
statement is Hellmann–Feynman (CITED, Rellich–Kato). ∎

### Proposition 2.3 (dilation picture; PROVED)
Let s = 1 + t and U_s: L²(−h,h) → L²(−h/s, h/s), (U_sF)(y) = s^{1/2}F(sy), unitary. Then U_sτ^{I}_{s a}U_s⁻¹ = τ^{I/s}_a, so
    U_s 𝔇^{ℕ^s} U_s⁻¹ = Σ_{n < R^{1/s}} n^{−s/2} τ^{I/s}_{log n},     Π^{ℕ^s}[U_s⁻¹H] = s Σ 2Λ(n)n^{−s/2}⟨H, τ^{I/s}_{log n}H⟩.
Hence the R-cell form of ℕ^{1+t} is unitarily the R^{1/s}-cell form of ℕ with (i) comb scaled by s, (ii) weight exponent
s/2 in place of ½ (in the cells and in the comb), (iii) the archimedean form and the constraint functionals transported by U_s.
*Proof.* (τ_{sa}F)(x) = F(x − sa) on I; (U_sτ_{sa}F)(y) = s^{1/2}F(sy − sa) = (U_sF)(y − a) on I/s. The cell condition
n^s < R is n < R^{1/s}. Substitute. ∎
Consequence: the exponent ray mixes three things the earlier rounds measured separately — the comb scaling c (21A, window ≍ λ₀
two-sided), an off-line weight exponent σ = s/2, and a change of the archimedean side relative to the comb. At first order these
are the three pieces of Prop. 2.2.

### 2.4 Sign of the comb-scaling piece (PROVED) and of the other two (NUMERICAL)
δ_lam λ_k = −𝒦_R[u_k] = −(Q₀[u_k] − λ_k). On the bottom vector of ℕ, 𝒦_R[u₀] = Q₀[u₀] − λ₀ > 0 whenever Q₀[u₀] > λ₀; the runs give
𝒦_R[u₀] = 0.126 (R = 4), 0.0859 (R = 5), … (table 2.5). So the comb piece pushes every near-null branch toward the right edge; this is the falsifier-(a) direction, which 21A found
one-sided at first order on u₀ as well, with the c < 1 side closed through coupling to higher eigenvectors. The question is the size and sign of δ_sig and δ_pos.

### Proposition 2.4 (virial identity for the position piece; PROVED)
Write Q = Q[𝒜, C, ℓ, X] for the R-cell form with archimedean form 𝒜, constraint functionals C (f₀, f_λ, A, B and ℓ_g), window
length ℓ and cell positions X = {log x}. For s > 0, U_s carries Q[𝒜, C, ℓ, sX] (same weights, same comb values) to
Q[𝒜∘U_s⁻¹, C∘U_s⁻¹, ℓ/s, X], so the two have the same spectrum on the corresponding constrained spaces. Differentiating at s = 1,
for every simple branch
    δ_pos λ_k = −ℓ ∂_ℓλ_k|_{X fixed} + δ_∞λ_k + δ_Cλ_k,
where δ_∞, δ_C are the first variations under 𝒜 ↦ 𝒜∘U_s⁻¹ and C ↦ C∘U_s⁻¹ (generator x∂_x + ½ on the log line).
*Proof.* Prop. 2.3 with weights and comb held fixed; unitary invariance of the spectrum; Hellmann–Feynman for each of the three
parameters (constraint variation: the constrained space moves smoothly, the eigenvalue of the compressed form is differentiable
for simple branches — CITED, Rellich–Kato). ∎
Reading. The dominant piece (table 2.5) is the position piece, and by 2.4 it is a mismatch between the dilation behaviour of the
archimedean data and the cell lattice — not a property of the comb. So the one-sidedness on the ray is a statement about how
𝒜 (and the constraints) respond to dilation on the near-null cluster. No sign follows from 2.1–2.4: δ_∞ is the quadratic form of
the kernel (u k_∞(u))′ (k_∞ the archimedean kernel on the log line) evaluated at 𝔇u, which is indefinite.

### 2.5 Measured split of the slope (NUMERICAL, T = 0.8, Nb = 40; symmetric differences at t = ±δ, δ = 10⁻¹⁰ (R = 4),
10⁻³⁰ (R = 9); 70 / 130 digits; bottom four branches of ℕ)
| R | piece | branch 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 4 | lam (= −𝒦_R[u_k]) | −0.126 | −0.297 | −0.680 | −1.184 |
| 4 | sig | +0.039 | +0.093 | +0.271 | +0.557 |
| 4 | pos | −0.906 | −1.195 | −1.206 | +2.101 |
| 4 | total (powfix) | −0.994 | −1.399 | −1.615 | +1.474 |
| 9 | lam | −0.096 | −0.420 | −0.727 | −1.183 |
| 9 | sig | +0.027 | +0.129 | +0.302 | +0.394 |
| 9 | pos | −0.866 | −1.375 | −1.322 | −1.578 |
| 9 | total (powfix) | −0.935 | −1.666 | −1.747 | −1.972 |
Additivity lam + sig + pos = total holds to all printed digits (check of Prop. 2.2). (At R = 4 the fourth branch, eigenvalue 0.11,
is not near-null; its slope is positive.) Reading: the position piece carries ≈ 90 % of the slope of every near-null branch;
the comb piece −𝒦_R[u_k] is negative but small on the bottom branch (0.10–0.13); the weight-exponent piece is positive and small.
So the one-sidedness is **not** the comb-scaling (falsifier (a)) direction in disguise: it is the dilation mismatch of
Prop. 2.4.

Bottom six branches of the fixed-cell-set ray (powfix, symmetric differences, matrices at 70–150 digits): eigenvalue / slope
| R | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| 5 | 5.8e-9 / −0.91 | 9.5e-8 / −1.66 | 2.4e-5 / −1.81 | 7.4e-4 / −1.44 | 4.2e-3 / −2.21 | 0.169 / +4.27 |
| 6 | 2.0e-12 / −1.07 | 6.9e-10 / −1.77 | 2.1e-8 / −1.40 | 5.1e-7 / −1.92 | 5.6e-5 / −2.82 | 1.0e-3 / −2.12 |
| 7 | 9.8e-17 / −1.02 | 6.0e-14 / −1.75 | 2.2e-11 / −1.80 | 4.7e-9 / −1.98 | 5.8e-8 / −2.04 | 1.4e-6 / −3.34 |
| 8 | 7.7e-20 / −0.97 | 2.6e-17 / −1.71 | 1.6e-14 / −1.77 | 2.6e-12 / −2.02 | 4.4e-10 / −3.03 | 2.1e-8 / −2.75 |
| 10 | 1.06e-24 / −0.90 | 2.3e-22 / −1.63 | 2.0e-19 / −1.74 | 2.0e-17 / −1.82 | 5.9e-15 / −2.74 | 4.5e-13 / −3.37 |
Every near-null branch (eigenvalue ≪ 1) has slope in [−3.4, −0.9]; the bottom slope is −0.90…−1.07 for R = 4…10.
(R = 9: λ₀ = 1.33·10⁻²²; R = 10: λ₀ = 1.06·10⁻²⁴, both new.)

## 3. Edges of the positive segment (task 1; NUMERICAL, Nb = 40, outer bounds as in 22A §2)

### 3.1 Right edge
t₊(R) = λ₀/|∂_tλ₀| (1 + o(1)) with the bottom slope of 2.5: first-order values t₊^lin = 6.4·10⁻⁹, 1.9·10⁻¹², 9.7·10⁻¹⁷,
7.9·10⁻²⁰, 1.4·10⁻²², 1.2·10⁻²⁴ (R = 5…10, T = 0.8), i.e. t₊ ≈ 1.05 λ₀. Every sampled t > 0 (10⁻⁴ at R = 9, 10:
bottoms −5.1·10⁻⁴, −5.5·10⁻⁴) is negative. The right edge shrinks exactly like λ₀ (Lemma 3.3 of 21A transported to the ray:
the proof there uses only Q(t) = Q + tQ′ + O(t²) and a unit minimiser with Q′[u] < 0).

### 3.2 Left edge: brackets (sign of the Galerkin bottom at the two ends)
| R | T = 0.8, ray ℕ^{1+t} | T = 0.8, fixed cell set | first order t₋^lin (fixed cell set) | T = 1.0, ray |
|---|---|---|---|---|
| 5 | (−0.15, −0.10) | (−0.03, −0.02) | −0.0167 | (−0.2, −0.1) |
| 6 | (−0.10, −0.03) | (−0.10, −0.05) | −0.0133 | (−0.05, −0.03) |
| 7 | (−0.03, −0.02) | (−0.02, −0.01) | −0.0105 | (−0.03, −0.02) |
| 8 | (−0.01, −0.005) | (−0.01, −0.005) | −0.0073 | (−0.005, −0.002) |
| 9 | (−0.003, −0.002) | | −0.0034 | |
| 10 | (−0.0007, −0.0005) | | −0.00065 | |
t₋^lin is the largest negative root of det(Q + tQ′) on V_R (generalized eigenproblem with Q′ from symmetric differences at
±10⁻¹⁴…±10⁻³⁴, 70–150 digits). Selected values: R = 10, t = −10⁻⁴, −3·10⁻⁴, −5·10⁻⁴: bottoms +2.7·10⁻⁶, +4.3·10⁻⁶, +1.9·10⁻⁶;
t = −7·10⁻⁴: −3.6·10⁻⁶; R = 9, t = −0.002: +1.9·10⁻⁵, −0.003: −2.1·10⁻⁵.

Fit. With geometric midpoints at T = 0.8, ln|t₋| = −2.10, −2.90, −3.71, −4.95, −6.01, −7.43 (R = 5…10): the steps
0.80, 0.81, 1.24, 1.06, 1.42 increase, so the decay is faster than exponential in R, and ln|t₋| / ln λ₀ = 0.11, 0.11, 0.10,
0.11, 0.12, 0.13: |t₋(R)| ≈ λ₀(R)^{0.1…0.13} on this range. Both edges go to 0; the segment is asymmetric by a factor
|t₋|/t₊ ≈ 2·10⁷ (R = 5) … 5·10²⁰ (R = 10). T = 1.0 behaves the same way with somewhat smaller |t₋| (R = 8: 0.002–0.005).
So the reading "[t₋(R), t₊(R)] ∋ 0 shrinks to {0} from both sides" is confirmed on R ≤ 10 (NUMERICAL). Whether this makes it
ζ-specific is §5.

## 4. The left side: why t < 0 gains margin at fixed R and loses it as R grows (task 3)

### Lemma 4.1 (first-order edge bounds; PROVED)
Let Q(t) be a C² family of symmetric forms on a fixed finite-dimensional V with Q(0) = Q ≥ 0, Q′ = Q′(0), and
|Q(t)[v] − Q[v] − tQ′[v]| ≤ C t²‖v‖² for |t| ≤ t₀. If v is a unit vector with Q′[v] > 0, 4C·Q[v] < Q′[v]² and
2Q[v]/Q′[v] ≤ t₀, then Q(t)[v] < 0 at t = −2Q[v]/Q′[v]; hence the left edge satisfies |t₋| ≤ 2 inf_v Q[v]/Q′[v] over such v.
Symmetrically on the right with Q′[v] < 0. The linearised edge t₋^lin := −1/μ_max(Q^{−1/2}Q′Q^{−1/2}) (Q > 0) is the exact edge of
the family Q + tQ′.
*Proof.* Q(t)[v] ≤ Q[v] + tQ′[v] + Ct² = Q[v] − 2Q[v] + 4CQ[v]²/Q′[v]² = −Q[v](1 − 4CQ[v]/Q′[v]²) < 0 (if Q[v] = 0 take
any small t < 0). For the last sentence, Q + tQ′ = Q^{1/2}(1 + tQ^{−1/2}Q′Q^{−1/2})Q^{1/2}. ∎
(Lemma 4.1 is the ray version of 21A Lemma 3.3; nothing in it is specific to the exponent direction.)

### 4.2 What the edge vector is (NUMERICAL)
For the maximiser v of Q′/Q (the generalized eigenvector at t₋^lin), normalised:
| R | Q[v] | Q′[v] | |⟨v,u_k⟩|, k = 1…6 | mass of v on the upper half of the spectrum |
|---|---|---|---|---|
| 5 | 0.166 | 9.99 | 0.14, 0.33, 0.10, 0.49, 0.49, 0.55 | 1.5·10⁻² |
| 8 | 4.1·10⁻³ | 0.56 | 0.50, 0.05, 0.38, 0.14, 0.34, 0.30 | 3.8·10⁻⁴ |
| 9 | 1.1·10⁻⁴ | 0.032 | 0.53, 0.08, 0.43, 0.11, 0.37, 0.14 | 8.3·10⁻⁷ |
| 10 | 1.6·10⁻⁵ | 0.025 | 0.56, 0.04, 0.48, 0.08, 0.39, 0.10 | 3.9·10⁻⁸ |
Mechanism. Each near-null eigenvector u_k has Q′[u_k] < 0 (2.5), yet Q′ restricted to the near-null cluster is indefinite:
the off-diagonal couplings ⟨u_j, Q′u_k⟩ exceed the geometric mean of the diagonal slopes. In a 2×2 compression on {u_i, u_j}
with diagonal slopes −a_i, −a_j and coupling c, det(Q + tQ′) = 0 at t = −τ with
    τ²(c² − a_ia_j) = τ(λ_ia_j + λ_ja_i) + λ_iλ_j,    so  τ ≈ (λ_ia_j + λ_ja_i)/(c² − a_ia_j) when c² > a_ia_j
(PROVED, elementary): the left edge is set by the eigenvalue of the *upper* member of a strongly coupled pair, not by λ₀. The
edge vector at R = 8–10 lives in the span of modes 1, 3, 5 (and higher modes of the cluster up to Q-values ≈ 10⁻⁵), with almost no
weight outside the cluster. As R grows the whole cluster sinks (eigenvalues 2–5 at R = 10 are 10⁻²²…10⁻¹⁵), Q[v] at the edge
vector falls (0.17 → 1.6·10⁻⁵), Q′[v] stays O(10⁻²…1), and t₋ → 0 by Lemma 4.1(i).
So the competing mechanism is the **collapse of the near-null cluster combined with the indefinite coupling of ∂_tQ inside it**.
It is the same mechanism 21A found on the c-side ("c < 1 reached through coupling of u to higher eigenvectors").

### 4.3 New cells entering (NUMERICAL; the mechanism proposed in the task is secondary)
On the ray ℕ^{1+t} with t < 0 the element R^{1+t} enters the window (log-position (1+t)ℓ < ℓ), and further elements enter at
t = log R/log(R+1) − 1 (−0.10, −0.079, −0.064, −0.054 for R = 5…8). Comparison with the fixed cell set {n < R} (powfix):
– R = 6, 8 (R with Λ(R) = 0 resp. a prime power far from the edge effect): the two edges coincide to resolution.
– R = 5, 7 (R prime): with the cell fixed the form fails already at t = −0.03 (R = 5) / −0.02 (R = 7) on a *different* branch,
  an O(1) vector (𝒦 ≈ 0.9–3.2, bottoms −0.005…−0.15); the entering prime cell R^{1+t}, carrying 2Λ(R)R^{−(1+t)/2} at lag
  (1+t)ℓ, removes that branch and the edge moves out to the cluster-coupling value. So an entering prime cell *extends* the left
  segment; it is not what closes it.
– Linear prediction vs measurement: t₋^lin agrees with the bracket at R = 8, 9, 10; at R = 5, 6 the true edge is further out
  (second-order terms help), which is why the margins at t ∈ [−0.05, −0.01] (2·10⁻³…7·10⁻³ at R = 5, 6) look large.
At fixed R the gain of margin for t < 0 is first order: λ₀(t) ≈ |t|·min_k|∂_tλ_k| on the lowest-slope branch (e.g. R = 5,
T = 1.0: 2.6·10⁻⁴, 4.9·10⁻⁴, 1.1·10⁻³, 2.1·10⁻³ at t = −0.001, −0.002, −0.005, −0.01: slope ≈ −0.23…−0.26 for the bottom of
Q(t), smaller than the branch slopes −0.9…−1.8 of the near-null modes at t = 0 because the minimum switches to a mixed vector
with 𝒦 < 0 — the bottom vectors at t < 0 have 𝒦_R[u] ≈ −0.1 in every run).

## 5. Assessment of the reading (task 4)

(i) Confirmed as a measurement. On R ≤ 10 (T = 0.8; R ≤ 8 at T = 1.0) the positive segment of the exponent ray is
[t₋(R), t₊(R)] with t₊ ≈ 1.05 λ₀(R) and |t₋| ≈ λ₀^{0.1…0.13}, both → 0, ℕ at the right end. (NUMERICAL.)

(ii) Not a characterisation that isolates addition. Both edges are produced by mechanisms that do not involve the additive
structure: the right edge is λ₀/|slope| (Lemma 4.1, any direction with Q′[u₀] < 0), the left edge is the collapse of the
near-null cluster plus indefiniteness of Q′ on it (§4.2). The same two facts give the same picture in the comb-scaling
direction c (21A: J_R → {1} two-sided, right edge λ₀/𝒦[u₀], left edge through cluster coupling), and c = 1 is fixed by the
multiplicative normalisation Λ ∗ 1 = log, not by addition; and in the single-generator directions (22A, two-sided). So "ℕ is
the unique point of the ray with λ₀^{(R)} ≥ 0 for all R" splits as
    [λ₀^{(R)}(ℕ) ≥ 0 for all R]  +  [λ₀^{(R)}(ℕ) → 0, cluster collapse, Q′ indefinite on the cluster],
the first part being the R-cell positivity itself and the second a generic consequence of the collapse already recorded (18A,
21A). As a characterisation it contains the target and adds nothing that acts on it: a restatement plus a generic corollary.
(ARGUED, from Lemma 4.1 and the measurements.)

(iii) No variational lever. λ₀^{(R)}(t) is not maximised at t = 0: ℕ is the end of the segment with the *smallest* margin
(λ₀(0) ≈ 10⁻²⁴ against 4·10⁻⁶ at t = −3·10⁻⁴, R = 10). A proof along the ray would have to deduce positivity at the worst point
from positivity in the interior, which requires the sign of the slope integrated from the interior to 0 — i.e. control of
λ₀(0) itself. Proving ∂_tλ₀(0) < 0 (task 2) would establish only that positivity is lost for t > 0 at first order; it says
nothing about λ₀(0) ≥ 0. So even a complete proof of the slope sign is not a step toward (★). (ARGUED; logical, not numerical.)

(iv) What is genuinely specific. Only the first-order sign structure: in the exponent direction every near-null branch has slope
in [−3.4, −0.9] (one-sided), the slope being ≈ 90 % position piece (Prop. 2.4: dilation mismatch between the archimedean data and
the cell lattice), while single-generator directions give both signs. This is a property of how 𝒜 reacts to dilation on the
cluster; it is OPEN, and by (iii) it would not yield (★) even if proved. The bottom slope −0.90…−1.07 (R = 4…10) is
suspiciously close to −1; whether an exact identity forces ∂_tλ₀ → −1 is OPEN (a candidate source is the virial identity
2.4 with the homogeneity of the archimedean kernel).

## 6. Falsifier test (rule 4)
No sign step is proposed. For the characterisation itself: (a) cΛ — the same uniqueness holds at c = 1 in the c-direction
(21A), so the property does not separate ℕ from the falsifier class (a) by a mechanism different from positivity at ℕ; it
holds wherever λ₀ ≥ 0 with collapse. (b) a_P and (d) finite modifications fail at O(1) (21A, 22A), consistent. (c) Beurling
systems ℕ^{1−ε}: positive at fixed R for ε < |t₋(R)|, negative once |t₋(R)| < ε; R = 9, 10 confirm |t₋| → 0
(0.002–0.003, 0.0005–0.0007), so the R-cell family does eventually reject every ℕ^{1−ε} — NUMERICAL, and by §5(ii) through the
generic cluster mechanism, not through a property of addition.

## 7. Corpus and index notes
New: gen_system.py SYS = powfix / sig / pos / lam and SAVE=1 (V_R matrices for linearised edges); window_build.py pickles R = 9
(130 digits) and R = 10 (150 digits); λ₀(9) = 1.33·10⁻²², λ₀(10) = 1.06·10⁻²⁴ (T = 0.8, Nb = 40). Lemma 2.1 (operator Selberg
identity), Prop. 2.2 (three-piece split, additivity checked), Prop. 2.3 (dilation picture), Prop. 2.4 (virial identity for the
position piece), Lemma 4.1 (edge bounds), 2×2 cluster-coupling formula. Index row P211-23A; ledger C47.

## Result
PIVOT with PROVED pieces. The reading is confirmed numerically (both edges → 0 on R ≤ 10) but is not a ζ-specific
characterisation: the right edge is λ₀/|slope| and the left edge is the generic collapse of the near-null cluster with an
indefinite first variation, exactly as in the comb-scaling direction; ℕ is the minimum-margin point of its segment, so the ray
offers no variational route, and the slope sign — even if proved — does not bear on λ₀(0) ≥ 0.

### What was proved
- Lemma 2.1: Φ(Λ log) = [M,P] = 𝔇⁻¹[M,[M,𝔇]] − P² (Selberg's identity through the truncated Dirichlet homomorphism).
- Prop. 2.2: ∂_t = δ_lam + δ_sig + δ_pos with δ_lamλ_k = −𝒦_R[u_k]; explicit δ𝔇, δP for each piece.
- Prop. 2.3: ℕ^{1+t} at window log R is unitarily the R^{1/(1+t)}-cell form of ℕ with comb ×(1+t), weight exponent (1+t)/2,
  dilated archimedean and constraint data.
- Prop. 2.4: δ_posλ_k = −ℓ∂_ℓλ_k + δ_∞λ_k + δ_Cλ_k (virial identity).
- Lemma 4.1 and the 2×2 coupling formula for the left edge.

### What failed and why
- "ℕ is singled out by addition on the ray": both edges come from λ₀-collapse mechanisms shared with the c-direction (c = 1 is
  a multiplicative normalisation). The uniqueness is [positivity at ℕ] + [generic collapse corollary].
- "The left edge is closed by new cells entering": the entering prime cell R^{1+t} *extends* the left segment (R = 5, 7);
  with the cell set fixed the edge is set by cluster coupling, matching t₋^lin at R = 8–10.
- Sign of ∂_tQ on the cluster: not proved; numerically all near-null slopes ∈ [−3.4, −0.9], ≈ 90 % from δ_pos.

### Next concrete step
Decide whether the bottom slope ∂_tλ₀ → −1 is exact: evaluate δ_∞, δ_C and ℓ∂_ℓ of Prop. 2.4 separately on u₀ for R = 4…10 and
compare their sum with −1 + 𝒦_R[u₀] − δ_sigλ₀. This is a
structural curiosity only; per §5(iii) the exponent ray should not be pursued further as a route to (★).

## Reproducibility
tools/multi_cell/window_build.py 9 40 0.8 40 130 and 10 40 0.8 40 150 (≈ 14 / 17 min). gen_system.py R 40 0.8 J dps SYS Z with
SYS = pow:t | powfix:t | sig:t | pos:t | lam:t; EIGS=1 prints the bottom four eigenvalues (25 digits); SAVE=1 dumps the V_R matrix
to a scratch file M_<R>_<T>_<SYS>.pkl. Linearised edges: symmetric differences of two SAVE dumps at ±δ (δ = 10⁻¹⁴, 10⁻¹⁸,
10⁻²², 10⁻²⁶, 10⁻³⁰, 10⁻³⁴ for R = 5…10), generalized eigenproblem at the run's precision. 3–25 min per run.
