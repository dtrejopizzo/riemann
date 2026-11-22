# R162_302 — C2: a coefficient-direction law at `a = Lambda`?

Round 3, mechanism C2.

Status: **PARTIAL.** Four rigorous facts (§1–§4) and one exact reduction (§5). Candidates (i) and
(iii) are **NO-GO** as stated. (ii) survives only in a reduced form: Gate 1 follows from
two statements, (A) and (B). (A) is a coefficient-direction feasibility law and is the only place
where `Lambda` can enter. (B) is a purely archimedean "Gamma-moment dual certificate". Neither is
proved. The next sub-lemma is stated in §7.

Notation (Paper 46): `v_n = v_n(a) = 2a(n)/sqrt n` on `N_T = {2 <= n < e^{2T}}`. The form is
`a^{(v)}_T(F) = C_0 + Lev(c_F) - sum_n v_n c_F(log n)` for real unit `F` in `P_T` (eq:Aform).
`V_T(v)` is the primitive bottom (lem:degen), `v^0 = v_{T_*}(Lambda)`, `K_* = ker H_{T_*}`
(finite-dimensional, J-invariant), and `c_F(s) = int F(t)F(t-s) dt`.

## 1. The superdifferential at first contact (PROVED)

**Lemma 1.1.** For every `w` in `R^{N_T}`, as `t -> 0+`,

    V_{T_*}(v^0 + t w) = t * min_{F in K_*, ||F||=1, real} ( - sum_n w_n c_F(log n) ) + o(t).

Consequently the superdifferential of `V_{T_*}` at `v^0` is the convex hull of the vectors
`-c_F|_{log N_T}` over unit `F` in `K_*`. The tangent cone of the positivity set `𝒱_{T_*}` at `v^0` is

    Tan(v^0) = { w : sum_n w_n c_F(log n) <= 0 for every F in K_* }.

*Proof.* On `P_T` the perturbation `w ↦ -sum w_n Re<V_{log n}F, F>` is a bounded self-adjoint
operator `B_w` with `||B_w|| <= sum|w_n|`. `H_{T_*}` has compact resolvent and `0` is its bottom
eigenvalue, which is isolated and has finite multiplicity. Kato–Rellich perturbation theory for
`H + tB_w` gives the first-order bottom `t * min spec(P_{K_*} B_w P_{K_*})`. The kernel is J-invariant
and the form is real, so the minimum is attained at a real vector. The superdifferential and
tangent-cone statements are the standard duals of this directional derivative for the concave
function of lem:degen. ∎

This is the exact content of "coefficient-direction stationarity". The quantity
`∂_u <F, H_{T,a_u} F>` of R162_207 (3.3) equals `-sum_n w_n c_F(log n)` with `w_n = 2η(n)/sqrt n`.
First contact gives `V(v^0) = 0`. It gives no sign on the directional derivative in any interior
direction `w`.

## 2. Candidate (i): the joint surface and regime boundaries (NO-GO)

**Lemma 2.1 (the entering atom is first-order invisible).** Suppose `T_* = ½ log n_k` is a regime
boundary. Then `c_F(log n_k) = 0` for every `F` in `L^2(I_{T_*})`. So the new coordinate `v_{n_k}` has
zero directional derivative at `v^0`, and the jump of `v_T(Lambda)` across the boundary carries no
first-order inequality.

*Proof.* `c_F` is supported in `[-2T, 2T]`, and it vanishes at `±2T` because the overlap of the
supports is null. ∎

Inside a regime, `v_T(Lambda)` is constant. The only variation in `T` is the change of window. Under
the dilation `U_r` (lem:contT), a change of window is equivalent to moving the atoms from `log n` to
`(log n)/r` at fixed weights. Minimality of `T_*` (`V_T(v_T(Lambda)) >= 0` for `T < T_*`) is
therefore a law in the **position** direction, not in the weight direction. It is a virial-type
inequality involving `c_F'(log n)`, the Gamma symbol `τ m'(τ)` and a Tate correction. That law holds
verbatim for every coefficient system at its own first contact, including the modifications of
thm:finmod. So it fails falsifier F3. Concavity in `v` together with monotonicity in `T` yields no
one-sided inequality on `c_F(log n)` beyond Lemma 1.1.

## 3. Candidate (iii): Möbius / Ward-preserving directions (NO-GO, vacuous)

**Lemma 3.1.** Let `N >= 1`. Then `{η : (η*1)(k) = 0 for 1 <= k <= N} = {η : η = 0 on [1, N]}`.

*Proof.* The map `η ↦ (η*1)|_{[1,N]}` is unitriangular in the divisor order, with inverse
convolution by `μ`. ∎

Take `N = e^{2T_*}`. By prop:finite(i),(iv), every interior direction that preserves `Λ*1 = log`
up to order `N` is zero. So "restricted stationarity" is stationarity over a single point, and it is
empty. Inside the window, `Λ*1 = log` is equivalent to "the vector equals `v^0`" and has no
directional content.

**Lemma 3.2 (exterior directions are exactly stationary and exactly silent).** Let `η` be supported
on `n >= e^{2T_*}`. Then:

- `H_{T,a_u} = H_T` for every `u`, so R162_207 (3.3) holds trivially;
- the Ward defect `b_{a_u} = u(η*1)` is nonzero on every multiple of `supp η`;
- `D_N` and `𝓔_N` change by the same amount `δD·R`, so `RB_N = D_N R - 𝓔_N` is unchanged;
- `c_{N,L}` changes by `<R_L F, δD R_L F>` and `Q_{N,L}` by `-2<R_L F, δD R_L F>`, so
  `2c + Q` (eq:Qbalance) is invariant.

*Proof.* `B_N` involves only `n < e^{2T}`. For `n >= e^{2T}` the collar integral runs over the
whole window, so `(𝓔_N)_m` gains `b_m Λ'(n) n^{-(a_m+½)} K_F(a_m)`. Insert this into (eq:Qfull). ∎

The situation is therefore split in two:

- interior coefficient directions are Λ-specific but not stationary;
- exterior coefficient directions are stationary but silent in every compressed identity proved so
  far.

## 4. The Gamma energy is linear in the autocorrelation (PROVED)

**Lemma 4.1.** Let `F` be real with `JF = εF`. Then

    ||R_L F||^2 = ε ∫_{-2T}^{2T} c_F(s) κ_L(s) ds,
    κ_L(s) = sum_{m <= L} a_m e^{-2a_m(T+δ)} cosh(a_m s).

*Proof.* We have `∫ c_F(s) cosh(as) ds = K_F(a) K_F(-a)`. Parity gives
`K_F(-a) = ε K_F(a)`. Sum the terms with weights `b_m^2`. ∎

By faithfulness of `R`, Gate 1 is thus **equivalent** to one linear inequality on the
autocorrelation of the first-contact vector:

    ε <c_F, κ_L> <= 0    for F in K_*.                                         (4.1)

Like (eq:equivgate), (4.1) is not a weaker lemma. It moves the problem from the Hankel side (Gamma
moments) to the Toeplitz side, where the prime atoms live. The identity itself is archimedean and
holds for every system.

## 5. Exact reduction: which inequality on {c_F(log n)} suffices (PROVED)

**Proposition 5.1.** Suppose there exist `α` in `R^{N_{T_*}}`, `β` in `R` and an even distribution `p`
on `[-2T_*, 2T_*]` such that:

**(B) — Gamma-moment certificate, archimedean.**

    ε κ_L = sum_n α_n (δ_{log n} + δ_{-log n}) - β σ̌_{T_*} - p,

with `<c_G, p> >= 0` for every `G` in `P_{T_*}` of parity `ε`. Here `σ̌_T` is the kernel of the
symbol, so that `a_T(G) = <c_G, σ̌_T>`.

**(A) — coefficient-direction feasibility, arithmetic.**

    V_{T_*}(v^0 + t α) >= 0    for all small t > 0.

Then `R_L F = 0` for every first-contact vector of parity `ε`. If `L` is injective on the radical,
`F = 0`.

*Proof.* By (A) and lem:degen, `0 <= V(v^0 + tα) <= -t sum α_n c_F(log n)`, hence
`sum α_n c_F(log n) <= 0`. Equivalently, `α` lies in `Tan(v^0)` of Lemma 1.1. On the radical,
`<c_F, σ̌> = a_T(F) = 0`. Lemma 4.1 then gives

    ||R_L F||^2 = 2 sum α_n c_F(log n) - <c_F, p> <= 0. ∎

The exact sufficient inequality is therefore

    sum_{n < e^{2T_*}} α_n c_F(log n) <= 0    for F in K_*,                   (5.1)

where `α` is an atom vector that certifies (B). In words, `α` must be a tangent direction of the
positivity cone at `v^0` along which raising the weights keeps positivity. Then (5.1) is equivalent
to (A) (Lemma 1.1).

**Why (B) needs atoms.** With `α = 0`, (B) says `a_T >= (ε/|β|) ||R_L||^2` on the parity class of
`P_T`. That spectral gap is false at a contact. So every certificate must use the prime positions
`log n`, `n < e^{2T_*}`. Structurally, (B) is a dual-certificate problem of Paper 46 type, with
target `κ_L` and flat-top replaced by cosh-moments.

## 6. Filter (F1–F4)

- **Not trivially F = 0.** (A) and (B) are separately non-equivalent to the conclusion:
  - (B) contains no `Λ` and is a statement about all of `P_T`.
  - (A) is a statement about the vector `v^0` in a direction, not about the kernel.

  Only their conjunction is closing. By itself, (5.1) is weaker than (4.1) whenever (B) holds with
  `p ≠ 0`.
- **F1.** (A) uses `V(v^0) = 0` and the bottom of `H_{T_*}` in an essential way. For an eigenvector
  with `λ > 0`, the step "(A) implies (5.1)" is unavailable. For `λ > 0` one would get
  `sum α c_F <= λ`-terms, and (4.1) would fail.
- **F3, finite modifications.**
  - (B) is identical for every system with the same atom positions.
  - (A) is a property of the specific point. For `a = Λ + cδ_{n_0}` with `c` beyond `c_*` of
    thm:finmod(ii), the point leaves `𝒱_T`, and its own first contact sits at a different point with
    its own tangent cone. Nothing transfers (A) from `v^0` to it.
  - Conversely, Lemma 3.1 shows that no interior Ward identity can prove (A). An arithmetic proof
    of (A) must use `n >= e^{2T_*}`, where Lemma 3.2 shows that the currently proved identities are
    silent.
- **F3, Davenport–Heilbronn.** A DH first-contact vector exists, since RH fails for DH. So for its
  weights (A) and (B) cannot both hold. (B) is archimedean and common to both, so the failure must
  sit in (A). That is consistent: (A) must come from the Euler product.
- **F2 and F4.** (A) is one-sided, since it is a superlevel condition. It is not a square or a
  linear limit.

## 7. Exact next sub-lemma

**Sub-lemma C2.1 (exterior Ward feasibility).** Let `supp η ⊂ [e^{2T_*}, M]` and `a_u = Λ + uη`. In
the finite (PC-ren) identity (thm:PCfinite with `M >= N >= e^{2T_*}`), paired against
`F ⊗ Π S_L F` with both orientations, the polar layer and the Tate endpoints retained, compute the
`u`-derivative. The derivative is exactly stationary by Lemma 3.2. Show that the Ward slot
`(η*1)(k)` at `k = dm`, `d ∈ supp η`, `m <= N`, contributes a quadratic form in `(K_F(a_m))` that is
**not** the collar shift `-2<R_L F, δD R_L F>`.

If the difference is a nonzero multiple of `||R_L F||^2`, then stationarity forces `R_L F = 0`
directly, bypassing (A) and (B). If the Ward contribution equals the collar shift identically, the
exterior direction is tautological. In that case (A) must be proved by a non-perturbative argument:
an explicit `α` in `Tan(v^0)`, for instance from the dual certificates of Theorem Z restricted to the
radical. Then (B) becomes the remaining archimedean problem.

Prediction: the tautological case is likely, because compression `P` kills `k >= e^{2T}`. It should
be checked before any construction of `α`.

Files edited: this file only.
