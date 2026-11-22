# R162_101 — B1: minimality of T_* through a first variation in the window

Round 1 of phase 162, front B1.
Status: **NO-GO** (for the mechanism as posed), with three exact lemmas that explain why. No claim of
R_L F = 0.

Corpus checked before building: P124_001 (joint variation at fixed window: tautological, returns the
radical equation), **P124_004 (window variation via dilation U_T + Tate correction: one-sided crossing
quotient (1.1), no sign; Euler shift quotients not differentiable on the log-Sobolev form domain;
birth terms o(1) with no rate)**, R161_081 (2.1) = Paper 46 eq:Qspectral, R161_099 §2 (square of (PC)
is A_M → −A_M invariant). The present note does not repeat P124_004's differentiation; it replaces it
by exact (derivative-free) identities, which make the negative verdict sharper and regularity-independent.

Notation (Paper 46): a_T form (eq:form / eq:Aform), P_T primitive subspace, H_T ≥ 0 its operator on
P_T at the first-contact window T_*, N_T = ker H_T, F ∈ N_{T_*}, JF = εF, r the Tate vector of
eq:localweak. By R162_001, λ_A is continuous and T_* := inf{T : λ_A(T) < 0} has λ_A(T_*) = 0.

---

## 1. What "minimality" contains

**Lemma 1 (left minimality is redundant).** Let T be any window with H_T ≥ 0. Then H_{T'} ≥ 0 for all
T' ≤ T. Hence, of the two halves of "first contact" — (L) λ_A ≥ 0 on (0,T_*], (R) λ_A < 0 on (T_*,∞) —
(L) is equivalent to the single condition H_{T_*} ≥ 0.

*Proof.* Zero extension P_{T'} ↪ P_T is isometric and preserves a (lem:monoT). ∎

**Lemma 2 (kernel nesting).** If λ_A(T_1) = 0 and T_1 ≤ T ≤ T_*, then the zero extension maps N_{T_1}
injectively into N_T.

*Proof.* For G ∈ N_{T_1}, its extension EG ∈ P_T has a_T(EG) = a_{T_1}(G) = 0 and H_T ≥ 0; for a
nonnegative closed form, a_T(EG) = 0 forces a_T(EG, Φ) = 0 for all Φ in P_T ∩ dom (Cauchy–Schwarz for
the nonnegative form), i.e. EG ∈ N_T. ∎

So the only information in minimality beyond "H_{T_*} ≥ 0, N_{T_*} ≠ 0" is the *right-hand* condition
(R), which concerns vectors that do **not** live in P_{T_*}.

## 2. Inward variation: the first variation vanishes identically (exact, no regularity)

**Proposition 3 (exact displacement identity).** Let F ∈ N_{T_*} and let γ be *any* map
s ↦ γ(s) ∈ P_{T_*} ∩ dom a_{T_*} (no continuity or differentiability assumed). Then

  a_{T_*}(γ(s)) = a_{T_*}(γ(s) − F)   for every s.

In particular, for every inward window transport — dilation U_r (r<1) followed by any Tate correction
into P_{rT_*} ⊂ P_{T_*}, or restriction/cut-off followed by correction, or the transport of P124_004 for
s<0 — the "crossing quotient" equals a_{T_*}(γ(s) − F)/s: its first-order part is **zero**, and its
sign is the sign of the nonnegative form on the displacement. Nothing about F is constrained beyond
H_{T_*} ≥ 0.

*Proof.* a(γ) = a(F) + 2 Re a(F, γ−F) + a(γ−F). Here a(F) = 0 and γ − F ∈ P_{T_*} ∩ dom, so
a(F, γ−F) = ⟨H F, γ−F⟩ = 0 in the form sense (Lemma 2's Cauchy–Schwarz argument). ∎

Remarks. (i) This bypasses the domain wall of P124_004 §4: no Euler derivative is needed, and the
answer is that there is nothing to differentiate — the linear term is exactly 0, for every rough F.
(ii) P124_004 (3.3)–(3.4) found a "Tate-normal term" 2 Re q(f_*, ḟ_0) = c_+ℓ_+(ḟ_0) + c_−ℓ_−(ḟ_0).
Proposition 3 shows that term cancels exactly against the moving-constraint terms once the transported
curve is kept inside P_{T_*} (which is automatic for s<0 after correction into P_{T_*e^s} ⊂ P_{T_*}):
⟨r, γ − F⟩ = 0 because γ − F ∈ P_{T_*} ⊥ Tate space. The Tate multiplier is invisible to inward
variation.
(iii) Second order: a(γ(s) − F) ≥ 0, i.e. at the Hessian level a(γ̇) ≥ 0 when γ̇ exists. This is
H_{T_*} ≥ 0 on one vector.

**Corollary 4 (Hadamard inequality is empty).** Any one-sided inequality of the form
"D(F) := d/ds|_{s=0^-} a_{T_*e^s}(transported F) ≤ 0" derived from (L) is the identity D(F) = 0 (when
D exists) and carries no boundary/endpoint information: no sign on traces F(±T_*) (which in any case
do not exist: P121 gives only H^s, s<1/2), on the Gamma moments K_F(a_m), or on the collars E_{N,L}F.

## 3. Outward variation: minimality (R) gives only upper bounds on λ_A

For s > 0, a transported, Tate-corrected vector F_s ∈ P_{T_*e^s} gives
λ_A(T_*e^s) ≤ a(F_s)/‖F_s‖² (R162_001 Step 5; P124_004 (2.3)). Condition (R) says λ_A(T_*e^s) < 0.
These are **both upper bounds** on λ_A(T_*e^s); they are compatible for every value and every sign of
the outward virial quotient a(F_s)/s. A contradiction would require a *lower* bound on λ_A(T) for
T > T_*, and minimality supplies none (lower bounds come only from certificates, i.e. from the
Theorem C / D1 side of Paper 46, not from T_*).

The only qualitative content of (R) that can be extracted rigorously is:

**Lemma 5 (right limit of negative ground states).** Let T_k ↓ T_*, G_k ∈ P_{T_k}, ‖G_k‖ = 1,
a_{T_k}(G_k) = λ_A(T_k) < 0. Then, after dilation back to I_{T_*} and Tate correction (R162_001 Steps
2–5), a subsequence converges in L² to a unit vector G ∈ N_{T_*}.

*Proof sketch (complete given R162_001).* The corrected pull-backs v_k ∈ P_{T_*} have
a_{T_*}(v_k) ≤ λ_A(T_k) + ω(T_*/T_k) → 0 and ‖v_k‖ → 1; bounded form values give bounded form norm
(Lemma mbounds), compactness of sublevel sets (proof of thm:O) gives an L²-convergent subsequence, and
lower semicontinuity of the closed form gives a_{T_*}(G) ≤ 0, so G ∈ N_{T_*}. ∎

Lemma 5 says some kernel vector is "approachable from the right". It is a selection statement on
N_{T_*}, not an equation on a given F, and it contains no information on R_L G: the approximating
G_k are negative states of *different* windows, and eq:Qspectral applied to them at their own window
gives Q_{N,L}(G_k) = −2 Σ (d_{m,N} + λ_A(T_k)) |(R_L G_k)_m|², which tends to the λ = 0 identity, i.e.
back to eq:Qbalance. No sign is gained in the limit.

## 4. Combination with the collar identities / (PC-ren)

Every identity produced in §§2–3 is either (a) the radical equation a(F, Φ) = 0 on P_{T_*} (inward),
or (b) an upper bound on λ_A to the right (outward). Inserting (a) with the admissible test
Φ = Π S_L F is exactly the derivation of eq:Qbalance (Paper 46 §subsec:collars), whose content is the
gate equivalence eq:equivgate (R_L F = 0 ⟺ Q_{N,L}(F) ≥ 0) and not a proof of it. Inserting (b) gives
nothing, being one-sided in the wrong direction. Hence the combination does not force R_L F = 0.

## 5. Falsifier tests

- **F1 (spectral).** Fails, in the precise sense required. Proposition 3 has an exact analogue for any
  eigenvector H_T F = λF at *any* window: for γ(s) ∈ P_T with ‖γ(s)‖ = 1,
  a(γ) − λ = a(γ − F) − λ‖γ − F‖², again with zero linear term. The window monotonicity of all min–max
  levels λ_k(T) (zero extension) makes every Hadamard-type derivative ≤ 0 for *all* branches,
  including positive eigenvectors at non-critical windows, where Q_{N,L} < 0 (R161_081). So any
  inequality obtainable from the first variation in T holds on vectors that violate the target; it
  cannot use λ = 0 or minimality non-perturbatively. This is the root of the NO-GO.
- **F2 (orientation).** Proposition 3 and Lemmas 1, 2, 5 hold for any nonnegative closed form with
  window monotonicity; they are insensitive to the sign convention of the comb and carry no orientation
  of (PC).
- **F3 (arithmetic).** The same lemmas hold verbatim for arbitrary weights a(n) ≥ 0 in place of Λ
  (thm:finmod) and for Epstein / Davenport–Heilbronn data at their first-contact windows (which exist
  there, since those forms do go negative). Λ*1 = log never enters. Consistent with the NO-GO: the
  mechanism cannot be the step forcing vanishing.
- **F4.** Not reached (no graph limit taken).

## 6. What fails and exactly where

1. Left minimality (L) reduces to H_{T_*} ≥ 0 (Lemma 1); the inward first variation is identically
   zero, exactly and for rough F (Proposition 3). There is no endpoint functional to sign.
2. Right minimality (R) yields only upper bounds on λ_A(T), T > T_*, and the selection Lemma 5; to use
   it one needs an independent **lower** bound on λ_A just right of T_* (e.g. λ_A(T) ≥ −κ(T − T_*)
   with κ expressed through R_L F, or through the birth collar of a prime power at e^{2T_*}). Neither
   is available; P124_004 §5 shows birth terms have no divided rate.
3. Any route of type B1 therefore needs an extra, arithmetic, two-sided input at T_* (a lower
   eigenvalue bound or a signed collar-density law); minimality itself is spent once H_{T_*} ≥ 0 and
   N_{T_*} ≠ 0 are written down.

Status: **NO-GO** for B1 (minimality through window variation cannot force R_L F = 0); PARTIAL
by-products: Lemma 1 (redundancy of left minimality), Lemma 2 (kernel nesting on flat stretches),
Proposition 3 (exact vanishing of the first variation, removing P124_004's regularity issue),
Lemma 5 (right-limit selection).
