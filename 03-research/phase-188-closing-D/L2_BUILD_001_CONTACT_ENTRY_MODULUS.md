# L2_BUILD_001 — Explicit modulus at contact entry

Scope: tool toward (L2) of Paper 46 §open. Pen and paper only; no numerics.
Conventions of Paper 46: a_T(F) = (1/2π)∫σ_T|F̂|², σ_T = m − Σ_{n∈N_T} v_n cos(τ log n),
v_n = 2Λ(n)/√n, ‖F‖² = (1/2π)∫|F̂|², 𝓕(u) = ∫F(t)F̄(t−u)dt, A_T = Σ_{N_T} v_n,
C_0 = m(0), m increasing (lem:mbounds(i)), lower bound lem:mbounds(ii).
Corpus check: lem:contA gives continuity of λ_A with a non-explicit modulus η(r);
R186_100/105 give ‖K‖ ≤ ‖G_{VE}‖/c (so no new ‖K‖ lemma is written here). No prior
explicit modulus at contact entry found (grep "edge mass", "contact entry", "log(1/δ)").

## 1. Edge-mass lemma (PROVED)

Put N(F) := (1/2π)∫ log(2+|τ|)|F̂(τ)|² dτ.

**Lemma 1.** Let F ∈ L²(ℝ) with N(F) < ∞, J an interval of length δ ∈ (0, 1/e), L := log(1/δ). Then
  ∫_J |F|² ≤ (2/(πL))‖F‖² + (4/L) N(F) ≤ (5/L) N(F).

*Proof.* Fix Ω > 0, split F̂ = F̂1_{|τ|≤Ω} + F̂1_{|τ|>Ω}, F = F_lo + F_hi. For every t,
|F_lo(t)| ≤ (1/2π)∫_{|τ|≤Ω}|F̂| ≤ (1/2π)(2Ω)^{1/2}(2π‖F‖²)^{1/2}, so |F_lo(t)|² ≤ (Ω/π)‖F‖² and
∫_J|F_lo|² ≤ (δΩ/π)‖F‖². By Plancherel ‖F_hi‖² ≤ N(F)/log(2+Ω). Hence
∫_J|F|² ≤ 2(δΩ/π)‖F‖² + 2N(F)/log(2+Ω). Take Ω = 1/(δL). Then δΩ = 1/L and
log(2+Ω) ≥ log(1/δ) − log L = L − log L ≥ L/2 because y ≥ 2 log y for all y > 0
(the minimum of y − 2log y is 2 − 2log 2 > 0). This gives the first inequality; the second uses
N(F) ≥ log 2·‖F‖² and 2/(π log 2) < 1. ∎

## 2. Relative bound of the archimedean weight (PROVED)

**Lemma 2.** With κ := max{log(6π) + 3/2, log 3 − C_0}, m(τ) ≥ log(2+|τ|) − κ for all τ; hence for
F in the form domain of a_T, N(F) ≤ a_T(F) + (κ + A_T)‖F‖².

*Proof.* m is even. For |τ| ≥ 1, lem:mbounds(ii) gives m ≥ log|τ| − log 2π − 3/2, and
log(2+|τ|) ≤ log(3|τ|). For |τ| < 1, m ≥ m(0) = C_0 (monotone) and log(2+|τ|) < log 3.
Then σ_T ≥ m − A_T ≥ log(2+|τ|) − κ − A_T; integrate against |F̂|²/2π. ∎

## 3. Contact-entry theorem (PROVED)

Let n be a contact, T' > ½log n, δ := 2T' − log n ∈ (0, 1/e), and suppose n is the only element of
N_{T'} with log n ≥ 2T' − δ (i.e. n is the most recent contact). Let a⁰_{T'} be the form on
L²(I_{T'}) with the term of n deleted (contact set N_{T'}∖{n}), A⁰ := A_{T'} − v_n, and
λ⁰ := inf{a⁰_{T'}(F): F ∈ P_{T'} ∩ D_{T'}, ‖F‖ = 1}.

**Theorem 3.** With ε := 5v_n / log(1/δ) < 1,
  λ_A(T') ≥ (1 − ε)·λ⁰ − ε(κ + A⁰).

*Proof.* For F ∈ L²(I_{T'}), 𝓕(log n) = ∫_R F(t)F̄(t − log n)dt, with R = [−T' + log n, T'] of
length δ and t − log n ranging over L = [−T', T' − log n], also of length δ. Cauchy–Schwarz and
Lemma 1: |𝓕(log n)| ≤ ‖F1_R‖‖F1_L‖ ≤ (5/log(1/δ))N(F). Since a_{T'}(F) = a⁰_{T'}(F) − v_n Re𝓕(log n)
and, by Lemma 2 applied to a⁰ (the proof only uses σ ≥ m − Σv), N(F) ≤ a⁰(F) + (κ + A⁰)‖F‖²,
  a_{T'}(F) ≥ a⁰(F) − ε(a⁰(F) + (κ + A⁰)‖F‖²) = (1−ε)a⁰(F) − ε(κ+A⁰)‖F‖².
Take the infimum over unit F ∈ P_{T'} ∩ D_{T'}. ∎

**Corollary 4 (transfer to S).** If (1−ε)λ⁰ > ε(κ+A⁰), then λ_A(T') > 0, hence S_{T',k} ≻ 0 for every
k with c(T',k) > 0 (thm:coer-schur(iii)). Quantitatively, a new contact cannot produce a first
contact of λ_A within distance δ of its entry unless log(1/δ) ≤ 5v_n(1 + (κ+A⁰)/λ⁰).

Label: Lemmas 1–2, Theorem 3, Corollary 4 PROVED. No sign is certified at any window; no
negative value is produced.

## 4. Self-review

1. *Correctness.* Lemma 1: the constant chase is right; the sup bound for F_lo uses the 2π
   convention ‖F‖² = (1/2π)∫|F̂|² consistently. Lemma 2: lem:mbounds(ii) has −1/τ − 1/(2τ²) ≥ −3/2
   only for τ ≥ 1 — that is where it is used. OK. Theorem 3: λ⁰ may be negative a priori; the
   inequality is still valid (it is linear in a⁰), it is only useless then. OK.
2. *Is it new?* lem:contA proves continuity with η(r) non-explicit, through dilation. Theorem 3 is
   an explicit modulus, but only at contact entries and only relative to the deleted-contact form
   a⁰ on the same window. Minor novelty; a tool, not a step of sign.
3. *Barriers.* Theorem 3 is a relative form-norm bound: it lies INSIDE the class of thm:posext /
   lem:half (bounds by norms in a fixed frame), and a⁰ is a finite modification of Λ (finmod,
   cor:void): λ⁰ is the bottom of a modified weight sequence, which can be negative
   (thm:finmod). Therefore Theorem 3 cannot by itself decide any window, and it does not claim to.
   Its only role is a gluing tool: it moves the difficulty at each window to the deleted-contact
   form a⁰ on the same window and costs a factor log(1/δ), which is far too weak against
   thm:margin (λ ≤ 4·10⁹Te^{−15.449T}): the admissible δ is doubly exponentially small in T.
   It is not in W-det, W-fam, W-pat, W-loc, W-mom, W-coh (no determinant, no family functional,
   no observables list, uses the full symbol, no moments, no coherence sum).
4. *Verdict.* PROVED, correct, weak. Does not advance the sign of (L2). Kept because Lemma 1
   (log-weight edge control, constant 5/log(1/δ)) is reused in L2_BUILD_002.
