# R162_1901 — R-C.b from minimality + the rank-one pole correction: NO-GO with exact obstruction

Note. One 3×3 sanity evaluation (float, only to display a PROVED closed-form model).
Inputs: R162_1801 Thm A, R162_1803 §3 (UNCERTIFIED), R162_1890 fix (T_* := inf{T : λ_A(T) < 0}), R162_802 §§2–3
(monotone data, Kreĭn law df/dT ≥ 0, Haynsworth charge ι = N₋ − 𝟙[f<0]), R162_902 (A^ev = W^ev − 2φφ*).

**Status: NO-GO (PROVED) for the route; PARTIAL (PROVED) sharpening of Theorem A.**
- §1 Theorem 1: exact three-condition characterisation of an even Type I first contact. **PROVED.**
- §2 Theorem 2: every structural law available weight-blindly (min–max monotonicity of μ_k, monotonicity of λ,
  Kreĭn law for f, conserved charge ι, rank-one pole correction, interlacing, T_W ≤ T_*) is satisfied by an explicit
  family that has a Type I first contact. **PROVED.** So R-C.b does not follow from minimality plus these laws.
- §3 The exact obstruction: a codimension-two stratum, cut out by two equations and one *open* inequality that is
  automatically satisfied near every Type II contact. **PROVED.**
- §4 Whether that stratum meets the positive-comb cone: **OPEN**, with a sharp falsifier test.

No sign is claimed. No label moves. Gate 1 stays OPEN.

Notation (even sector throughout; the odd sector is identical with φ_odd). A = A^ev_T, eigenvalues
μ₁ < μ₂ ≤ μ₃ ≤ …, eigenvectors u_k, residues r_k = ⟨u_k,φ⟩², f(z) = ⟨(A − z)^{−1}φ,φ⟩ = Σ r_k/(μ_k − z),
f(T) := f(0). λ(T) = inf spec A|_{φ^⊥}. Before contact N₋ = 1 (R162_1890: μ₂ ≥ λ > 0 on (0,T_*)).
g(z) := Σ_{k≠2} r_k/(μ_k − z) (the regular part of f at μ₂).

## 1. Theorem 1 (Type I = two equations + one inequality) — PROVED

**Theorem 1.** Assume μ₂(T_*) is simple (the multiple case is §3(iv)). Then the first contact at T_* is Type I iff
  (E1) μ₂(T_*) = 0,  (E2) ⟨u₂(T_*), φ⟩ = 0,  (I) g(0) ≤ 0 at T = T_*.
Moreover (I) holds strictly at, and is implied by the limit of, every Type II contact: at a Type II contact
g(0) = −r₂/μ₂ < 0.

*Proof.* (⟹) Theorem A of 1801 gives (E1) and (E2). With r₂ = 0, f = g is analytic and strictly increasing on
(μ₁, μ₃). The constrained spectrum on φ^⊥ is {μ₂} ∪ {zeros of g in (μ₁,μ₃)} ∪ … (Weinstein–Aronszajn with a removed
pole). λ = 0 = μ₂ is the bottom iff g has no zero in (μ₁, 0), i.e. iff g(0) ≤ 0 (g increasing, g → −∞ at μ₁⁺ because
r₁ > 0: φ is not orthogonal to the Perron ground state, 1701). (⟸) Same computation read backwards: (E1)+(E2)+(I) give
λ(T_*) = 0 attained by u₂ ∈ φ^⊥ with Au₂ = 0, which is Type I. For the last claim: at a Type II contact 0 < μ₂ and
f(0) = 0, so g(0) = −r₂/μ₂ < 0. ∎

**Haynsworth reading (R162_802 ι).** For T < T_*: N₋ = 1, f < 0, ι = 0. For T > T_*: ι = 1.
- Type II: N₋ stays 1, f crosses 0 upward (𝟙[f<0]: 1 → 0). This is the event 802 §3.2 describes.
- Type I: f does **not** cross 0 or ∞ (it stays ≈ g(0) < 0, analytically continued through T_*, since r₂ vanishes to
  second order while μ₂ vanishes to first order); instead N₋ jumps 1 → 2 through a crossing with zero residue.
  ι is conserved at crossings *only when the residue is nonzero*; a zero-residue crossing is the other way ι can jump.
So the conserved-charge bookkeeping sees both contact types and prefers neither: R-C.b ⟺ "the first jump of ι is
by f, not by N₋".

## 2. Theorem 2 (the minimality route cannot close) — PROVED

**Theorem 2.** On ℝ³ let φ = (2,0,1)/√5, R(t) the rotation by angle t in the (e₂,e₃)-plane, and
  A(t) = R(t) diag(−1 − t, −t, 1) R(t)ᵀ,  W(t) = A(t) + 2φφᵀ,  t ∈ [−t₀, t₀] (t = T − T_*, t₀ small).
Then:
1. μ₁ = −1 − t, μ₂ = −t, μ₃ = 1 are all nonincreasing (min–max monotonicity).
2. N₋ = 1 for t < 0; λ(t) > 0 for t < 0, λ(0) = 0, λ(t) < 0 for t > 0, λ strictly decreasing: t = 0 is the first
   contact in the R162_1890 sense.
3. f(t) = ⟨A^{−1}φ,φ⟩ is strictly increasing (Kreĭn law) and extends analytically through t = 0 with f(0) = −3/5.
4. A = W − 2φφᵀ (rank-one pole correction, sign as in 902), interlacing holds, and λ_W = λ_A on φ^⊥ so T_W ≤ T_*.
5. u₂(t) = (0, cos t, sin t), ⟨u₂(0), φ⟩ = 0: the first contact is **Type I** (μ₂(T_*) = 0).

*Proof.* (1),(4),(5) are read off. (3): r₁ = 4/5, r₂ = sin²t/5, r₃ = cos²t/5, so
f(t) = −(4/5)/(1+t) − sin²t/(5t) + cos²t/5 = −3/5 + (4/5 − 1/5)t + O(t²), increasing near 0; t = 0 is removable.
(2): for t < 0, N₋ = 1 and f(t) < 0, hence ι = 0 and λ > 0 (802 §3.2); for t > 0, N₋ = 2 so λ < 0; λ(0) = 0 by
Theorem 1 (g(0) = −3/5 < 0). Float evaluation of λ(t), f(t) on [−0.3, 0.02] confirms all signs (e.g. λ(−0.01) =
9.97e-3, λ(0.01) = −1.00e-2, f monotone from −0.902 to −0.588). ∎

Every law used by 1801, 802, 902 and 1890 is a property of this triple (A(t), φ, W(t)); none of them is violated. The
model is weight-blind (no comb, no primes, no archimedean symbol), so it tests exactly the proposed route. Local
embedding into the true setting is not claimed; the theorem shows only that the proposed implication has no content
beyond the listed laws.

Why the requested argument fails, point by point:
- "λ_A ≥ 0 up to T_* ⇒ at most one negative direction off P_T": true (interlacing), but it bounds N₋ only on
  (0, T_*); at T_* it allows μ₂ = 0 — equality is precisely the Type I case.
- "μ₂ = 0 and the constrained bottom reaching 0 simultaneously with u₂ ⊥ φ": this simultaneity is **automatic** once
  (E1)+(E2)+(I) hold — the constrained spectrum *contains* μ₂ when r₂ = 0. It is not a third coincidence; the count
  is two equations, not three.
- Monotonicity of f_ev: f passes smoothly through T_* in the Type I case (Theorem 2(3)); the Kreĭn law is not engaged.
- T_W ≤ T_*: W and A agree on φ^⊥; the order carries no information about μ₂.

## 3. The exact obstruction — PROVED

In the parameter space 𝒫 = {(T, a)} (a ranging over any family of combs), the Type I first contacts form
  𝒮_I = {μ₂ = 0} ∩ {⟨u₂, φ⟩ = 0} ∩ {g(0) < 0} (plus the boundary g(0) = 0),
i.e. (i) a codimension-two set cut out by two real equations, (ii) intersected with an **open** condition,
(iii) with **no further global condition**: if (E1),(E2) hold at (T_c, a), g(0) < 0, μ₂ simple and strictly decreasing
in T and ⟨u₂,φ⟩ vanishing to first order in T, then λ(T) > 0 for T < T_c near T_c (f = r₂/μ₂ + g < 0, since
r₂/μ₂ = O(T_c − T)), hence on all of (0, T_c) by monotonicity of λ; so T_c = T_*(a). Minimality is exhausted by
local data.
(iv) If μ₂ = μ₃ = 0 (double), Type I holds as soon as the eigenspace meets φ^⊥, which is automatic (dim 2): a
codimension-three event (double eigenvalue at 0) that forces Type I with no sign condition.
(v) The open condition (I) is automatic in a neighbourhood of Type II contacts with small r₂/μ₂, so it gives no
protection: any one-parameter path of Type II contacts along which r₂ → 0 faster than μ₂ ends in 𝒮_I.

Consequently: a generic **one**-parameter family (T only, fixed a) avoids 𝒮_I, but a generic **two**-parameter comb
family (T, s) meets the codim-two set {E1, E2} in isolated points — so R-C.b for *all* combs a ≥ 0 can only be proved
by an input that is neither local-spectral nor monotone: it must show the sign of ⟨u₂,φ⟩ on the crossing surface
{μ₂ = 0, g(0) < 0} is constant over the positive cone. By 1801 Thm B that sign is not forced by Perron structure.

## 4. Relation to R162_1803 and the falsifier — OPEN

- 1803 (float) reports ⟨u₂,φ̂⟩ at the μ₂ = 0 crossing: −0.062 (s = 0.5), −0.137 (deletion), +0.016 (s = 1.5),
  +0.022 (s = 2). At the contacts, −ĝ(0) = r̂₂/μ₂ ≈ 0.43 (s = 0.5), 0.49 (deletion), 0.56 (1.5), 0.61 (2), 0.65 (3):
  g stays O(1) negative, so (I) is comfortably satisfied near the crossing surface.
- Along the single family sΛ, the sign change does not produce a Type I point by continuity, because T_*(s) is not
  continuous in s (ζ, s = 1, has no contact below ½log5). So 1803 is **not** a counterexample.
- **Falsifier (weight-blind, decisive).** Take the two-parameter positive family a = s₂·δ_{log 2} + s₃·δ_{log 3}
  (plus fixed Λ-tail, or none). Trace the curve {μ₂^ev(T; s₂,s₃) = 0} and the sign of ⟨u₂,φ⟩ on it, restricted to
  its part with g(0) < 0 and N₋ = 1 just before. If the sign changes along a connected arc of that part, Theorem 1 +
  §3 give a Type I first contact for a positive comb ⇒ R-C.b is false weight-blind and must use the arithmetic of Λ.
  If the sign is constant on the whole positive cone, that constancy is the statement to prove.

## 5. For README

- R-C.b (even) ⟺ NOT[(E1) ∧ (E2) ∧ (I)] at T_*; Type I = two equations + open inequality (Thm 1).
- Minimality + rank-one pole + interlacing + Kreĭn monotonicity + charge ι cannot exclude Type I: explicit 3×3
  monotone model with a Type I first contact (Thm 2). NO-GO for the route.
- Obstruction: codimension-two stratum {μ₂ = 0, ⟨u₂,φ⟩ = 0}; minimality imposes no further condition (§3).
- Next: the two-parameter (s₂, s₃) crossing-surface sign test (§4) — O1901.1.
