# R162_2101 — Why the exact weight at 2 is (nearly) a Type I degeneracy

Pure mathematics (§1–§3) plus labelled float checks (§4, **UNCERTIFIED**).
Inputs: R162_2001, R162_1601/1803, R162_1701 Prop 5, R162_902, R162_1401 Thm 3, Paper 47 eq:form/eq:W/eq:symbol,
R160_M4_R1 Thm B (Pólya-kernel truncation, 106.09).
Scripts (new, `scripts/c3/`): `t2101_single_atom.py`, `t2101_sc.py`, `t2101_W.py`, `t2101_W2.py`, `t2101_polya.py`.

## Status

- **The hypothesis in the brief is FALSE (NO-GO).** No local identity links the atom at log 2 with the archimedean or
  polar term. The factors 2^{±1/2}·Λ(2)/√2 give no eigen-relation for cosh(t/2) (§1). The degeneracy is not tied to the
  functional form 2 log x/√x either. A single atom at log x with weight s·2log x/√x can also produce a Type I sign change for other x (x = 1.6 at s ≈ 1.41). Only at x = 2 does it sit at the arithmetic weight s = 1, and only there is W positive semidefinite with a near-kernel (§4.2–4.3). So Type I curves exist generically in (x, s); x = 2 is where one passes within 10⁻⁴ of s = 1, for the ζ reason of §2.
- **The mechanism (PROVED as structure, §2).** When s₂ = 1 and T < ½log 3, the window form is **exactly ζ's** complete
  Weil form W^ζ_T. The extended ζ-form has an infinite-dimensional even radical: every F with Φ_F = P(z²)·Ξ(z). Its
  truncations to I_T are W-null up to a doubly-exponentially small error (R160_M4_R1 Thm B). This radical contains
  **primitive** vectors, for example Φ_F = (¼+z²)Ξ, which vanish at s = 0, 1. So W^ev_T has a near-kernel of dimension ≥ 2,
  and one direction in it is primitive.
- **Lemma 3 (PROVED).** At a primitive contact the minimiser x satisfies Wx = κφ̂. Type I ⟺ κ = 0, and |κ| = ‖Wx‖. So a
  primitive near-kernel forces κ ≈ 0. That makes the contact near-Type-I (⟨u₂,φ̂⟩ ≈ 0, μ₂ ≈ 0). This is the precise form of
  "Perron–Tate alignment" (1701 Prop 5) in this setting.
- **Why s₃ barely matters (PROVED, §2.3).** The atom at log 3 pairs F(t) with F(t − log 3) only on |t| ≥ log 3 − T. There
  the radical vectors carry only their doubly-exponential tails.
- **Why the curve sits at 0.9998 and not at 1 (PARTIAL).** s₂ = 1 is **not** an exact Type I point. It is the point where
  κ is as small as the ζ near-kernel allows. The defect is κ(T_*) ~ 10⁻⁵, the truncation error at T_* ≈ 0.55–0.61.
  Detuning moves κ linearly (slope ≈ 0.06), so 1 − s₂^c ≈ κ/slope ~ 10⁻⁴. Asymptotically: 1 − s₂^c → 0 as T_c → ∞, at
  the doubly-exponential rate of the radical truncation. This is an upper-bound mechanism and is not proved for the curve.
  In the two-atom model T_c stays bounded (< ½log 4), so 1 is **not** reached exactly.
- **Λ-specificity.** The structure is specific to ζ, not to the value Λ(2). It holds exactly when the comb agrees with ζ's
  on the window. A single atom qualifies only for x = 2, weight Λ(2), T < ½log 3. The single atom at 3 (s₂ = 0) never
  does, because the atom at 2 is missing for T > ½log 2. There, ⟨u₂,φ̂⟩(T_*) ≈ −0.13 for every s₃ (§4.1). The same holds
  for a general single prime p ≥ 3.

No sign is claimed. No label moves. Gate 1 stays OPEN. The "first Λ-value-specific structure" is really the explicit
formula (ζ's radical) seen through a window where only the atom at 2 is present. It is already on record in
R160_M4_R1 Thm B / 106.09. What is new is the identification with the R162_2001 falsifier curve.

## 1. The local hypothesis fails

- Write w = Λ(2)/√2 and a = log 2. For t ∈ [a − T, T] (nonempty since a < 2T):
  (S_a φ)(t) = cosh((t − a)/2). Otherwise it is 0.
- So w(S_a + S_{−a})φ = w[cosh((t−a)/2)1_{t≥a−T} + cosh((t+a)/2)1_{t≤T−a}].
- On the overlap |t| ≤ T − a this equals 2w cosh(a/2)cosh(t/2) = (3/2)log 2 · cosh(t/2). At T_* ≈ 0.59 < a, however,
  that overlap is **empty**. The image then consists of two one-sided pieces cosh((t∓a)/2), each supported on
  [a − T, T] or its mirror. These are not proportional to φ.
- The archimedean multiplier m(τ) (eq:symbol) is transcendental (digamma). The polar term 2Re(A B̄) is rank 2 and
  independent of the comb.
- So no identity of the form "comb·φ = (arch + polar)·φ" holds at s₂ = 1 for any T. A detuning experiment confirms this
  (§4.2): replacing (log 2, Λ(2)) by (log x, log x) with x = 1.8, 2.2, 2.5, 2.8 removes the effect at s ≈ 1 (a Type I point can still occur elsewhere, e.g. x = 1.6 at s ≈ 1.41, with O(10⁻¹) negative ν₀).

## 2. The mechanism

### 2.1 Window coincidence (PROVED, trivial)

- A_T depends only on the atoms with log n < 2T (eq:symbol).
- Hence for T ∈ (½log 2, ½log 3) and s₂ = 1, the form a_T is ζ's, whatever s₃ is.
- For s₂ = s₃ = 1 the same holds up to ½log 4.
- Consequently W_T(F) = Σ_ρ Φ_F(ρ)Φ_F(1−ρ) on L²(I_T) (eq:W, explicit formula).

### 2.2 The primitive radical (PROVED given 106.09 / R160_M4_R1 Thm B)

- Let K_Pó be the Pólya kernel, Φ_{K_Pó} = Ξ. It is even and decays like e^{−πe^{2|t|}}·e^{9|t|/2}.
- For an even polynomial P, set F_P := P(i∂_t)K_Pó, so that Φ_{F_P} = P(z)Ξ(z). Then Φ_{F_P}(ρ) = 0 for every zero ρ, so
  F_P lies in the radical of the extended form.
- Take P(z) = ¼ + z². Then Φ_{F_P}(0) = Φ_{F_P}(1) = 0, so ℓ(F_P) = A(F_P) = B(F_P) = 0: F_P is **primitive**.
- Truncate to I_T: F_P^T := F_P·1_{I_T}. Continuity of W in the norm of 106.09 gives
  W_T(F_P^T) ≤ C_P e^{c_P T} e^{−2πe^{2T}}, and |ℓ(F_P^T)| ≤ C_P e^{c_P T} e^{−πe^{2T}}.
  This is R160_M4_R1 Thm B(i), with the polynomial factor absorbed.
- Hence, for s₂ = 1 and T < ½log 3:
  (i) ν₀(W^ev_T) is doubly-exponentially small (from K_Pó);
  (ii) the bottom λ_A(T) of a_T on the primitive space is doubly-exponentially small (from F_P, after projecting off the
  tiny φ-component);
  (iii) W^ev_T has at least two small eigenvalues ν₀, ν₁. This follows by min–max on span{K_Pó^T, F_P^T}: the two
  vectors are independent, since their φ-overlaps differ by O(1).

### 2.3 Lemma 3 (contact multiplier, PROVED)

- Let λ_A(T) = 0 be attained at a unit primitive x. Then P_{φ^⊥}Wx = 0, so Wx = κφ̂ with κ = ⟨Wx, φ̂⟩ = ±‖Wx‖.
- Since x ⊥ φ, A x = Wx − 2φ⟨φ,x⟩ = κφ̂.
- Therefore:
  (a) κ = 0 ⟺ x ∈ ker A ∩ φ^⊥ ⟺ Type I (μ₂ = 0 and ⟨u₂,φ̂⟩ = 0; 1901 Thm 1);
  (b) if κ ≠ 0, then x = κA⁻¹φ̂, which gives ⟨u_k, x⟩ = κ⟨u_k,φ̂⟩/μ_k and 1 = κ² Σ_k ⟨u_k,φ̂⟩²/μ_k².
  With the Type II law μ₂ ≈ −⟨u₂,φ̂⟩²/g(0), the k = 2 term gives |⟨u₂,φ̂⟩| ≈ |κ|/|g(0)| to leading order.
- So near-Type-I ⟺ |κ| small ⟺ the primitive minimiser is an approximate W-null vector.
- **Consequence:** at s₂ = 1 the only error in κ comes from the truncation defect of §2.2 and from the non-ζ atoms
  (log 3 with s₃ ≠ 1).
- **The s₃-perturbation (PROVED as a bound).**
  - |(s₃−1)w₃⟨(S_{log3}+S_{−log3})F, F⟩| ≤ 2|s₃−1|w₃ ∫_{log3−T}^{T}|F(t)||F(t−log3)| dt.
  - On that range |t| ≥ log 3 − T ≥ 0.49 for T ≤ 0.61. There the radical vectors are at their tails:
    |t − log 3| ≥ log 3 − T. So the perturbation is bounded by the tail product, which is small. The perturbation from
    detuning 2, by contrast, pairs F on |t| ≥ log 2 − T ≈ 0.1, where F is O(1). That explains the sensitivity to s₂ and
    the insensitivity to s₃.

### 2.4 Why 0.9998, not 1 (PARTIAL)

- On s₂ = 1 exact, κ(T_*) ≠ 0. It is set by the truncation defect at T_* ≈ 0.55–0.61, where e^{−πe^{2T}} ~ 10⁻⁵, and by
  the s₃ tail term.
- Detuning gives dκ/ds₂ = O(1), because the log-2 overlap is not in the tail. So s₂^c = 1 − κ(T_*)/(dκ/ds₂) + …, i.e.
  1 − s₂^c ~ 10⁻⁴, matching R162_2001 §3.
- s₂^c depends on s₃ through T_c and the tail term. The observed values are 2.3·10⁻⁴ at s₃ = 0 and 5.7–7.8·10⁻⁵ for
  s₃ ∈ [1.5, 4]. The drift is not monotone in T_c, so the tail term is not negligible against the truncation term.
  **No closed formula is claimed.**
- As T_c → ∞ along any family whose comb agrees with ζ's on the window, 1 − s^c → 0 at the doubly-exponential rate (upper
  bound, §2.2). 1 is an asymptote in that sense, **not an exact root**.
- With only two atoms, T_c < ½log 4, so the limit is never attained. As s₃ → 1, T_c rises toward ½log 4 (R162_2001 §2,
  0.66 → 0.73) and the curve approaches 1. This is consistent with the mechanism but was not measured to an asymptote.

## 3. Relation to the corpus

- **R162_1701 Prop 5 (Perron–Tate).** In the present setting, Lemma 3 refines the Cauchy–Schwarz bound. Alignment is
  good precisely because W has a near-kernel: the rank-one term 2φφ* absorbs the non-primitive radical direction
  (K_Pó, ⟨v₀,φ̂⟩ ≈ 0.8). The Perron vector μ₁ lives there. The primitive radical direction F_P becomes u₂.
- **R162_902.** The rank-one term is the PNT main term, and the asymptote f(0) → −1/(2‖φ‖²) is reached. At T_c ≈ 0.593,
  −1/(2‖φ‖²) = −0.41 = g(0) (R162_2001 §3). This is consistent: W's near-kernel overlapping φ drives f to its asymptote.
- **R162_1401 Thm 3.** Only on the Tate ray does Λ∗1 = log cancel the secular term. Here the analogous statement is that
  only the ζ comb has the ξ-radical. Any comb that differs inside the window loses it at first order.
- **R160_M4_R1 Thm B / 106.09.** The truncation bound is on record. What is new is the identification with the
  R162_2001 curve and Lemma 3.

## 4. Float checks (UNCERTIFIED, K = 34)

### 4.1 Single atom at 3 or 5 (s₂ = 0)

- x = 5: the contact T_* = 0.5958 precedes ½log 5, so there is no effect. The values are the pure archimedean ones:
  μ₂ = 3.8e-2, ⟨u₂,φ̂⟩ = −0.137.
- x = 3, s ∈ [0, 2]: T_* moves from 0.596 to 0.561. ⟨u₂,φ̂⟩ ∈ [−0.137, −0.130] and μ₂ ≈ 3.3–3.8e-2.
  **No degeneracy at s = 1.**

### 4.2 Single atom at log x with weight s·2log x/√x

| x | s = 0.9 | s = 1.0 | s = 1.05 | sign change in s ∈ [0.3, 1.4]? |
|---|---|---|---|---|
| 1.6 | −0.173 | −0.171 | −0.159 | yes, but far from s = 1: s^c ≈ 1.412 (T_c ≈ 0.733; μ₂ = 1.1e-4 at s = 1.4) |
| 1.8 | (branch jump at s ≈ 0.6, ⟨u₂,φ̂⟩ −0.14 → +0.10, μ₂ = 3e-2: not a near-degeneracy) | | | different phenomenon |
| 2.0 | −3.4e-3 | +1.3e-5 | (s = 1.01: +6.2e-4) | yes, s^c ≈ 0.99977 |
| 2.2 | −0.048 | −0.045 | −0.044 | no, up to s = 3 |
| 2.5 | −0.094 | −0.092 | −0.091 | no |
| 2.8 | −0.122 | — | — | no |

### 4.3 Spectrum of W^ev = A^ev + 2φφ* (s₂ = 1 means ζ in the window; ‖φ‖² = sinh T + T checked)

| T | x = 2: ν₀, ν₁ | ⟨v₀,φ̂⟩ | overlap of v₀ with truncated K_Pó | x = 1.8: ν₀ | x = 2.2: ν₀ |
|---|---|---|---|---|---|
| 0.40 | 1.8e-4, 0.31 | 0.85 | 0.987 | −5.8e-2 | 5.5e-4 (atom barely inside) |
| 0.45 | 1.6e-5, 0.096 | — | 0.989 | −8.6e-2 | −1.5e-2 |
| 0.50 | 9.4e-7, 0.018 | 0.79 | 0.991 | −9.6e-2 | −7.2e-2 |
| 0.54 | 1.1e-7, 2.2e-3 | 0.77 | 0.993 | −9.7e-2 | −1.2e-1 |

- Detuning at T = 0.5: ν₀ goes 6.2e-5 → 9.4e-7 → −2.3e-4 for s₂ = 0.99 → 1 → 1.01. So ν₀ is linear in s₂ with slope
  ≈ −0.03, and W stops being PSD for s₂ > 1.
- For x ≠ 2 the comb is not ζ's and ν₀ < 0 at O(10⁻¹), so Weil positivity fails outright.
- The truncated F_P = (¼ − ∂²)K_Pó at T = 0.5927 (s₂ = 1, s₃ = 0) has |⟨F_P, u₂⟩| = 0.965. Its φ̂-overlap is still
  0.05 there, because truncation at T ≈ 0.6 is coarse. So F_P explains the direction of u₂, but the finite-window optimum
  is much better than the explicit truncation.

## 5. Open

- (O2101.1) A certified two-sided estimate of κ(T_*) at s₂ = 1. This would decide whether the two-atom Type I curve can
  ever touch s₂ = 1, which the mechanism says it cannot for T_c < ½log 4.
- (O2101.2) Rate: the observed ν₀ decay (×1700 from T = 0.40 to 0.54) is faster than the Pólya truncation bound
  (×≈90). The true near-kernel is the prolate-type optimum, not K_Pó^T.
- (O2101.3) Consequence for R-C.b: any proof must use that the comb **is ζ's on the window** (the explicit-formula
  radical), not the numerical value of Λ(2). For ζ itself with all atoms, κ → 0 doubly exponentially. So R-C.b for ζ sits
  on a doubly-exponentially thin margin, which is certifiable only by a zero-side input or an enclosure that tight.
