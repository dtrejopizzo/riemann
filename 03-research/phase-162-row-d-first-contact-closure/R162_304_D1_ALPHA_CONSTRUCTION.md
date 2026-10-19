# R162_304 — D1: constructing the direction α of Proposition 5.1 (R162_302)

Mechanism D1.

Status: **NO-GO for the α-route (PROVED).** Five results are proved below:

- (B) is **not** archimedean. With β = 0 it has no solution (Thm 2). With β > 0 it has no solution
  either. With β < 0 it is equivalent, up to its boundary case, to a finite quadratic condition on
  the radical K_*^ε (Thm 3), so it depends on Λ through K_*.
- (A) and (B) evaluated on K_*^ε are opposite inequalities. For L large, their conjunction is
  **equivalent** to K_*^ε = {0} (Thm 4).
- Every test α (θv⁰ with either sign of θ, a single contact, a certificate direction) reproduces
  this collision (§4).
- No nonzero α admits a global directional certificate (Thm 5). So (A) cannot be proved by adding
  certificates.

Proposition 5.1 is therefore a reformulation of "no first-contact vector of parity ε", not a
reduction. The next sub-lemma returns to C2.1 (§7).

Notation as in R162_302 and Paper 47:

- P_T^ε is the set of vectors of P_T with JG = εG.
- K = K_* = ker H_{T_*}, and K^ε = K ∩ P^ε, which is finite-dimensional.
- A_∞(G) = C_0‖G‖² + Lev(c_G) is the archimedean form, and a_T(G) = A_∞(G) − Σ_n v⁰_n c_G(log n) (eq:Aform).
- σ_T(τ) = m(τ) − Σ_n v⁰_n cos(τ log n), so that a_T(G) = (1/2π)∫σ_T|Ĝ|².
- c_G(u) = (1/2π)∫cos(τu)|Ĝ(τ)|² dτ.
- q_n(G) := c_G(log n) is a bounded quadratic form with |q_n(G)| ≤ ‖G‖².

## 1. (B) in the Fourier variable (PROVED)

**Lemma 1.** For real G of parity ε, Lemma 4.1 of R162_302 gives ⟨c_G, εκ_L⟩ = ‖R_L G‖². Hence (B)
with some (α, β, p) holds **iff**

    (B*)  Q_{α,β}(G) := 2 Σ_n α_n c_G(log n) − β a_T(G) − ‖R_L G‖² ≥ 0   for all G ∈ P_T^ε,

and then p is *defined* by the displayed identity in (B). In the Fourier variable, (B*) reads

    (1/2π) ∫ p̂(τ) |Ĝ(τ)|² dτ ≥ 0   for G ∈ P_T^ε, where
    p̂(τ) = 2 Σ_n α_n cos(τ log n) − β σ_T(τ) − ε κ̂_L(τ) + ν̂(τ) + β_0 ĝ_0(τ) + β_1 ĝ_1(τ).

Here:

- ν is any even finite measure supported in |u| ≥ 2T_*. This is the freedom to extend κ_L outside
  the window: c_G vanishes there, as in the weak-duality step of prop:weak.
- β_0ĝ_0 + β_1ĝ_1 are the primitivity multipliers; they integrate to 0 against |Ĝ|² on P_T.
- κ̂_L(τ) = Σ_{m≤L} a_m e^{−2a_m(T+δ)} · 2[a_m sinh(2a_mT) cos 2Tτ + τ cosh(2a_mT) sin 2Tτ]/(a_m²+τ²)
  is the transform of κ_L·1_{[−2T,2T]}.

A sufficient, certificate-type version is p̂ ≥ 0 pointwise on ℝ. This is problem (D) of Paper 47
with target εκ_L and an extra comb Σα_n cos(τ log n) *inside* the window.

*Proof.* Pair (B) with c_G: ⟨c_G, δ_{log n}+δ_{−log n}⟩ = 2c_G(log n) and ⟨c_G, σ̌_T⟩ = a_T(G).
Conversely, given (B*), put p := Σα_n(δ_{±log n}) − βσ̌_T − εκ_L. The Fourier form is Parseval
together with the support and multiplier remarks. ∎

## 2. Which β are possible (PROVED)

**Lemma 2 (modulated tests).** Let φ ∈ C_c^∞(I_T) be even, real, φ > 0 on I_T. Put
G_τ = φ(t) cos τt if ε = +1, and G_τ = φ(t) sin τt if ε = −1. Then G_τ has parity ε. Let G'_τ be its
projection to P_T^ε. As τ → ∞:

- ‖G_τ − G'_τ‖ → 0 and ‖G'_τ‖² → ½‖φ‖²;
- c_{G'_τ}(u) = ½ cos(τu) c_φ(u) + o(1), uniformly in u;
- R_L G'_τ → 0;
- a_T(G'_τ) → +∞.

*Proof.* The complement of P_T in parity ε is spanned by cosh(t/2) or sinh(t/2). The inner products
with G_τ tend to 0 by Riemann–Lebesgue. Next, c_{G_τ}(u) = ½cos(τu)c_φ(u) ± ½∫φ(t)φ(t−u)cos(τ(2t−u))dt,
and the last integral is o(1) uniformly by Riemann–Lebesgue in t. R_L has finite rank, and each
K_{G_τ}(a_m) → 0 by Riemann–Lebesgue. Finally, a_T(G'_τ) = (1/2π)∫σ_T|Ĝ'_τ|², where
σ_T ≥ m − Σ|v⁰_n|, m(τ) ≍ log|τ| → ∞ (thm:S), and |Ĝ_τ|² concentrates at ±τ. The difference
G − G' lies in a fixed two-dimensional smooth space with vanishing coefficient, so its form
contribution also vanishes. ∎

**Theorem 2.** (i) If β > 0, (B*) has no solution. (ii) If β = 0, (B*) has no solution α.

*Proof.* (i) In Q(G'_τ) the comb and R_L terms stay bounded, while −βa_T(G'_τ) → −∞.

(ii) Put f(τ) := Σ_n α_n c_φ(log n) cos(τ log n). Then Q(G'_τ) = f(τ) + o(1). Here c_φ > 0 on
(−2T, 2T) because φ > 0 on I_T, and log n < 2T for n ∈ N_T.

- **Case f ≢ 0.** f is a trigonometric polynomial with distinct positive frequencies, so its Bohr
  mean is 0. A nonnegative almost-periodic function with mean 0 vanishes identically. So f is not
  ≥ 0 on any half-line [τ_1, ∞), which gives liminf_{τ→∞} f = −2η < 0. Then Q(G'_τ) < −η for
  arbitrarily large τ.
- **Case f ≡ 0.** The cos(τ log n) are linearly independent, so α_n c_φ(log n) = 0, hence α = 0.
  Then Q = −‖R_L G‖². This is negative at any G ∈ P^ε with K_G(a_1) ≠ 0. Such G exists because the
  parity-ε part of e^{−a_1t} is not in span{e^{±t/2}}. ∎

This refutes the claim in R162_302 that (B) is purely archimedean (§5 and §6 there). A certificate
needs β < 0, and βσ̌_T carries the full comb v⁰(Λ).

**Theorem 3 (Schur reduction of (B)).** Let β = −M with M > 0, and put
b_α(F) := 2Σα_n c_F(log n) − ‖R_L F‖² on K^ε.

- (a) If (B*) holds, then b_α ≥ 0 on K^ε.
- (b) If b_α > 0 (positive definite) on K^ε, then (B*) holds for all large M.

*Proof.* (a) For F ∈ K^ε we have a_T(F) = 0, so Q(F) = b_α(F).

(b) Write G = F + H with F ∈ K^ε and H ⊥ K^ε in P^ε. Then a_T(G) = a_T(H), because
a_T(F, ·) = ⟨H_{T_*}F, ·⟩ = 0. Compact resolvent gives a_T(H) ≥ λ_2‖H‖² with λ_2 > 0, the next
eigenvalue.

The form b(G) = 2Σα c_G(log n) − ‖R_LG‖² is bounded, with constant C = 2Σ|α_n| + ‖R_L‖². If
b ≥ c_0‖F‖² on K^ε, then

    Q(G) ≥ c_0‖F‖² − 2C‖F‖‖H‖ + (Mλ_2 − C)‖H‖²,

which is ≥ 0 once (Mλ_2 − C)c_0 ≥ C². ∎

So (B) is solvable exactly when some combination Σα_n q_n dominates ½‖R_L‖² on the
finite-dimensional radical K^ε, up to the degenerate boundary case. This depends on Λ, through
K_* = ker H_{T_*}(Λ).

## 3. (A) on the radical, and the collision (PROVED)

By lem:degen (supergradient), (A) ⇒ Σ_n α_n c_F(log n) ≤ 0 for every unit F ∈ K (both parities).
Lemma 1.1 of R162_302 gives the converse to first order.

**Lemma 3.** For L ≥ L_0(T_*, δ), R_L is injective on K^ε.

*Proof.* The subspaces ker R_L ∩ K^ε are decreasing in L, and K^ε is finite-dimensional, so the
chain stabilizes. Its intersection is ker R ∩ K^ε, which is {0} by faithfulness of R (eq:Gammaenergy). ∎

**Theorem 4 (the conjunction is the conclusion).** Let L ≥ L_0.

- (i) If some α satisfies (A) and (B) with this L, then K^ε = {0}.
- (ii) Conversely, if K^ε = {0}, then (B) holds for α = 0 and M large, by Thm 3(b) applied
  vacuously (see the proof below). (A) holds for α = 0 trivially.
- So "∃α: (A) ∧ (B)" ⟺ K_*^ε = {0}.
- (iii) For every α with b_α > 0 on K^ε, that is, for every α given by Thm 3(b), (A) restricted
  to K^ε is equivalent to K^ε = {0}.

*Proof.*

(i) For F ∈ K^ε, (B) gives 2Σα c_F ≥ ‖R_LF‖² and (A) gives Σα c_F ≤ 0. Hence R_LF = 0, and
F = 0 by Lemma 3.

(ii) When K^ε = 0, P^ε = K^⊥ and a_T ≥ λ_2‖·‖², so Q = −‖R_L·‖² + M a_T ≥ 0 for M ≥ ‖R_L‖²/λ_2.

(iii) Such an α has Σα c_F > 0 for every nonzero F ∈ K^ε. So "Σα c_F ≤ 0 on K^ε" holds iff K^ε = 0. ∎

**Answer to the circularity check.** For every α that solves (B), (A) is again equivalent to F = 0.
(A) and (B) are not both "non-contradictory" in any world that has a parity-ε first-contact vector.
Their joint content is exactly the negation of that vector's existence. They are not a weight-only
positivity statement: both are inequalities for the same quadratic forms q_n restricted to K^ε, with
opposite signs.

## 4. The test directions (PROVED, all collide)

Use a_T(F) = 0 on K, so that Σ_n v⁰_n c_F(log n) = A_∞(F) for unit F ∈ K.

- **α = θv⁰.**
  - (A) ⟺ θ·A_∞(F) ≤ 0 on K.
  - (B) needs 2θA_∞(F) > ‖R_LF‖² on K^ε. Taking β = −2θ − M, Q equals
    2θA_∞ − ‖R_L‖² − M a_T.
  - θ > 0: (B) needs A_∞ > 0 on K^ε, while (A) needs A_∞ ≤ 0.
  - θ < 0: (B) needs A_∞ < 0 on K^ε, while (A) needs A_∞ ≥ 0.
  - Concavity does not decide the sign. θ ↦ V(θv⁰) is concave, with V(0) = λ^P_∞(T_*) < 0
    (T_* ≥ log 2 > 0.60, cor:Tarch) and V(1) = 0. The one-sided derivatives at θ = 1 are
    D_+ = min_K(−A_∞) and D_− = min_K A_∞.
  - The concavity bound V(0) ≤ V(1) + D_− gives min_K A_∞ ≥ λ^P_∞. This already follows from F ∈ P,
    so it carries no information. The chord slope −λ^P_∞ > 0 bounds D_+ from above only.
  - So the sign of A_∞ on K (equivalently, of the prime sum Σv⁰c_F on the radical) is undetermined
    by concavity. Whatever it is, one of the two signs of θ is killed by (A) and the other by (B).
- **α = c e_{n_0}** (a single contact).
  - (A) ⟺ c·c_F(log n_0) ≤ 0 on K.
  - (B) needs c·c_F(log n_0) > ½‖R_LF‖² on K^ε.
  - These are the same collision. Moreover, if n_0 is a regime-boundary atom, c_F(log n_0) = 0
    (302, Lemma 2.1), and (B) fails outright.
- **α from a dual certificate.** See Thm 5.

## 5. Certificates cannot supply (A) (PROVED, NO-GO)

(D)-certificates at T_* for the comb v are lower bounds on V(v) (prop:weak; thm:D1 holds for any
nonnegative weights). The linear way to prove (A) from certificates:

1. Take a certificate f_0 = σ^{(v⁰)} + ν̂_0 + β^0·ĝ ≥ 0 for v⁰, attained.
2. Take a *directional certificate* h = −Σα_n cos(τ log n) + ν̂_1 + β^1·ĝ ≥ 0 on ℝ, with ν_1
   supported in |u| ≥ 2T.
3. Then σ^{(v⁰+tα)} + (ν̂_0 + tν̂_1) + (β^0 + tβ^1)·ĝ = f_0 + t h ≥ 0, so V(v⁰ + tα) ≥ 0 for all
   t ≥ 0.

**Theorem 5.** A directional certificate h ≥ 0 exists only for α = 0.

*Proof.* By weak duality, h ≥ 0 implies Σα_n c_G(log n) ≤ 0 for every G ∈ P_T. Apply this to G'_τ
of Lemma 2 (either parity): f(τ) + o(1) ≤ 0 for all large τ, with f as in Thm 2. By the Bohr-mean
argument f ≡ 0, and then α = 0. ∎

In addition, weak duality applied to *any* certificate proof of (A) at v⁰ + tα gives
0 ≤ ∫f_t dμ_F = −tΣα c_F for F ∈ K. So every certificate proof of (A) proves the radical inequality
of §3. By Thm 4 it then cannot coexist with (B) unless K^ε = 0. Finally, thm:D1 gives certificates of
value λ^P − ε, and attainment at a first contact is not known, so step 1 is also unsupported.

## 6. Falsifier F3 (PROVED)

Nothing in §§1–5 uses the Euler product or Λ*1 = log. Everything uses only: the weights v, the
first contact (V(v) = 0 attained on a nonzero finite-dimensional K), compact resolvent, and
faithfulness of R. Hence for **every** system with a first-contact vector of parity ε, "∃α: (A) ∧ (B)"
fails. This covers:

- the deletions Λ1_{n≥N} (N ≥ 5): the contact is at T^*_{∞,P} ∈ [0.58, 0.60], with empty comb on
  N_T by thm:finmod(i), and the kernel is nonzero by lem:strict and compact resolvent;
- the amplifications of thm:finmod(ii) at their own first contact;
- Davenport–Heilbronn, at a first contact of its own form.

Which of the two individually fails depends on the unknown sign structure of the q_n on that
system's K, exactly as for ζ. Therefore:

- R162_302 §6 is wrong in two places. (B) is not "identical for every system with the same atom
  positions", since βσ̌_T contains the weights, and Thm 2 forces β ≠ 0. And the DH failure cannot be
  located in (A) alone.
- The pair passes F3 only in the vacuous sense that it is logically equivalent to the absence of a
  contact.

## 7. Exact next sub-lemma

The α-route adds nothing beyond K^ε = {0}. The only unconstrained object left from R162_302 is
**Sub-lemma C2.1 (exterior Ward feasibility)**. It concerns directions η supported on
[e^{2T_*}, M], where the q_n with n < e^{2T_*} do not enter. Theorems 2–5 therefore do not apply
to it.

Precisely: in thm:PCfinite with M ≥ N ≥ e^{2T_*}, compute the u-derivative of the pairing against
F ⊗ Π S_L F for a_u = Λ + uη, and decide whether the Ward slot (η*1)(dm) contributes a quadratic
form in (K_F(a_m))_{m≤L} that differs from the collar shift −2⟨R_LF, δD R_LF⟩ by c·‖R_LF‖², c ≠ 0.
If it does, R_LF = 0 follows, and hence F = 0 by Lemma 3. If it does not, R162_302's route (ii) is
closed completely.

Files edited: this file only.
