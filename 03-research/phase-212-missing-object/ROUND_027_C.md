# Round 27, memo C — Structure of the damped form `a^{(ω)}_T`

Notation of P47 (eq:symbol, eq:form, eq:W, eq:Aform, lem:K, lem:polar): `c_F(u) = ∫F(t)F̄(t−u)dt`, `m`, `s_T`,
`v_n = 2Λ(n)/√n`, `N_T = {n ≥ 2 : log n < 2T}`, `A(F) = ∫Fe^{t/2}`, `B(F) = ∫Fe^{−t/2}`, `W_T = a_T + 2Re(AB̄)`,
`K(u) = 2e^{3u/2}/(e^{2u}−1)`. Damped form: `a^{(ω)}_T(F) = Arch(F) − Σ_{N_T} v_n cos(ω log n) c_F(log n)` on `P_T ∩ D_T`.
General test weight: `a^w_T`. Antecedents cross-checked: 212-26-A (the optimum with `w ≥ 0` looks like damped `v`),
212-25 (`K_T`, Tychonoff), ROUND_019_A (3.1), ROUND_021_A §4, ROUND_024_A, P211-9A (prolate "taper": another object),
212-24-C(c) (Fejér means on the torus: another object). Nothing in this memo retries those entries: the new object
is the modulated weight `v_n cos(ω log n)` as a family of relaxations with margin.

## §1 Facts (i) and (ii)

**Lemma 1.1 (domains and complex tests).** PROVED. (a) `D_T` is invariant under modulation: `Ĝ(τ) = F̂(τ+ω)` and
`log(2+|τ−ω|) ≤ log(2+|τ|) + log(1+|ω|)`. (b) For a real even symbol, `a(U+iV) = a(U) + a(V)` (U, V real): the
cross term is `∫ s·Im(ÛV̄̂)`, an odd integrand. Since `e^{±t/2}` are real, `P_T` splits the same way; the real and
complex infima coincide. (c) For real `F`, `c_{Fe^{iωt}}(u) = e^{iωu}c_F(u)`, hence `cos(ωu)c_F(u) = Re c_G(u)`.
**Lemma 1.2 (extension by zero and closedness).** PROVED. `K_T = {w ∈ ℝ^{N_T} : a^w_T ≥ 0 on P_T ∩ D_T}` is an intersection
of closed half-spaces `{w : Arch(F) ≥ Σ w_n c_F(log n)}`, hence closed and convex in finite dimension (`a^w` is
affine in `w`). If `T < T′` and `F ∈ P_T`, its extension by zero is in `P_{T′} ∩ D_{T′}` with the same `F̂`, and `c_F`
(continuous, support `[−2T,2T]`) vanishes at `log n ≥ 2T`; thus `a^w_{T′}(F) = a^{w|N_T}_T(F)` and `w ∈ K_{T′} ⟹ w|N_T ∈ K_T`.
**Lemma 1.3 (passage to the limit).** PROVED. Let `T_j → ∞` and `ω_j` with `ω_j log n → 0` for each fixed `n` (it suffices that
`ω_j → 0`). If `a^{(ω_j)}_{T_j} ≥ 0` on `P_{T_j}` for every `j`, then `λ_A(T) ≥ 0` for every `T`.
*Proof.* Fixing `T`, for `T_j ≥ T` the vector `(v_n cos(ω_j log n))_{n∈N_T}` is in `K_T` (Lemma 1.2) and converges
to `v|N_T` in `ℝ^{N_T}`; `K_T` is closed. ∎ Neither uniformity in `T` nor a sign of `cos` is needed.
**Corollary 1.4 (convex class).** PROVED. If `g(u) = ∫cos(ωu)dμ(ω)`, `μ ≥ 0` a probability, then
`a^{v·g}_T = ∫ a^{(ω)}_T dμ(ω)`. By convexity of `K_T`: if `a^{(ω)}_T ≥ 0` for `ω ∈ supp μ`, then also `a^{v·g}_T ≥ 0`.

## §2 The damped form in terms of the complete form
**Proposition 2.1 (exact identity).** PROVED. For real `F ∈ P_T` and `G = Fe^{iωt}`:
```
a^{(ω)}_T(F) = a_T(G) − ∫_0^∞ (1−cos ωu) K(u) c_F(u) du                                   (2.1)
             = W_T(G) + ∫_0^∞ (1−cos ωu) [4cosh(u/2) − K(u)] c_F(u) du.                   (2.2)
```
*Proof.* (2.1): `Arch(G) = C_0‖F‖² + ∫(c_F(0) − cos(ωu)c_F(u))K`, and `Arch(F) − Arch(G) = −∫(1−cos ωu)Kc_F`; the
prime part of `a_T(G)` is `Σv_n Re c_G(log n)` (Lemma 1.1c). In symbol form: `m(τ) − ½m(τ−ω) − ½m(τ+ω) =
−∫_0^∞ cos(τu)(1−cos ωu)K(u)du`. (2.2): `2Re(A(G)B̄(G)) = ∫_ℝ c_G(u)·2cosh(u/2)du = ∫ cos(ωu)c_F 2cosh(u/2)`, and
`∫c_F 2cosh(u/2) = 2Re(AB̄)(F) = 0` on `P_T`; subtracting gives `−2∫_0^∞(1−cos ωu)c_F·2cosh(u/2)`. ∎
**Polar term.** `G` does not annihilate the poles: `A(G) = ∫F e^{t/2}(e^{iωt}−1)`, `B(G) = ∫Fe^{−t/2}(e^{iωt}−1)`.
The polar term appearing in (2.2) is `−2Re(A(G)B̄(G)) = −2ω²A′(F)B′(F) + O(ω³)`, with `A′ = ∫tFe^{t/2}`,
`B′ = ∫tFe^{−t/2}` (checked both ways: `∫u²c_F 2cosh(u/2) = −4A′B′` on `P_T`). Sign: indefinite; it is the
rank-2 form of signature (1,1) of lem:polar evaluated on the first-moment directions. Size:
`|A′B′| ≤ ‖F‖²·∫_{−T}^{T}t²e^{t}dt ≲ T²e^{T}‖F‖²`, i.e. `≲ ω²T²e^{T}` — large compared with the measured margin.
The archimedean correction is `−(ω²/2)∫_0^∞u²Kc_F + O(ω⁴)`, bounded by `(ω²/2)‖F‖²∫u²K` (`∫u²K < ∞`): `O(ω²)`.
Reading: damping is the complete form at the modulated test plus a correction whose kernel `(1−cos ωu)
(4cosh(u/2) − K)` is negative near 0 and grows like `ω²u²e^{u/2}`: the pole dominates. Equivalent direct
expansion: `a^{(ω)}_T(F) = a^v_T(F) + (ω²/2)Q(F) + O(ω⁴Σv_n(log n)⁴|c_F|)`, `Q(F) = Σv_n(log n)²c_F(log n)`.

## §3 Evaluation on the near-null family `X_φ = Π_T(M∗φ)`
By ROUND_019_A (3.1) with `w = v cos(ω log ·)` (exact up to `O(e^{cT}e^{−πN})` and the layer of ROUND_024_A):
```
a^{(ω)}_T(X_φ) = Σ_{N_T} v_n (1 − cos(ω log n)) c_{X_φ}(log n) = (1/2π)∫ |M̂(τ)|²|φ̂(τ)|² q_ω(τ) dτ,   (3.1)
q_ω(τ) = Σ_{N_T} v_n (1 − cos(ω log n)) cos(τ log n) = p(τ) − ½p(τ−ω) − ½p(τ+ω),  p = Σ_{N_T} v_n cos(τ log n).
```
(The rewriting is PROVED: `c_{M∗φ} = c_M ∗ c_φ`, Plancherel.) **φ = δ:** only `n ≤ 6` count (`c_M(log 7) ≈ 3·10⁻⁷`):
`(ω²/2)[0.9803·0.4805·(−9.753) + 1.2685·1.2069·6.066 + 0.6931·1.9218·0.235] = (ω²/2)(−4.594 + 9.287 + 0.313)
≈ +2.50·ω²` (NUMERICAL with the cited values): **positive**, the `3` beats the `2` by the factor `(log 3/log 2)²`.
Ratio `≈ 2.50ω²/97.47 = 0.026ω²`; at `T = 2`, `k = 1` gives `0.004` versus `λ_min ≈ 10⁻⁴`: `X_δ` is not the
minimizer. The law `∝ ω²` does match the measurement.
**General φ:** the sign is that of the mean of `q_ω` under `|M̂φ̂|²`. `q_ω` has no constant term and is not
identically zero, hence it takes negative values; by PNT its smooth part is `≈ Re[2e^{(½+iτ)2T}h(τ)/(½+iτ)]`,
it oscillates in `τ` with period `≈ π/T` and amplitude `≍ e^{T}`. To make (3.1) negative one must concentrate `φ̂` on a
negative zone of width `≍ π/(2T)` with `φ` of support `≤ 2T`: time–band product `O(1)`, marginal, and
`|M̂|²` (decay `e^{−πτ/2}`) rewards leakage towards `τ ≈ 0` where `q_ω > 0`. Conclusion: positive for `φ = δ`
(NUMERICAL); for every `φ`: OPEN, without proof and without counterexample; the risk is real (ARGUED). Cheap computation that
decides: minimize (3.1) in `φ` over a prolate basis of the support, `T = 1.6, 2.0, 2.4`.

## §4 Why Fejér fails and cosine does not
The triangle `g(u) = (1 − |u|/2T)_+` **is** positive definite: `μ_F(dω) ∝ sinc²(ωT)dω`. By Cor. 1.4,
`a^{Fejér} = ∫a^{(ω)}dμ_F`, and `μ_F` has tail `∝ ω⁻²` without bounded support. That the mean gives `−0.04…−0.15` forces
(PROVED, logic) `a^{(ω)}_T < 0` for some `ω` in the support, necessarily large (for `k ≤ 1` it is `> 0`
numerically). Mechanism (ARGUED): with `ω log 2`, `ω log 3` far from 0 the weights of `2` and `3` drop or change
sign and the negative directions of `Arch` on `P_T` reappear (thm:index: `n_− ≥ 1` from `T = 0.60`), which only
the low primes at almost full weight compensate. On `X_δ` Fejér gives `(1/2T)(−6.63 + 8.45 + 0.23) > 0`: the failure is
in another direction. What decides is **not** `g″(0) < 0` nor being positive definite by themselves, but
`1 − g(log p) = O(ω²)` for the low primes, i.e. **bounded and small spectral support** of `μ`.
**Proposed class (CONDITIONAL on `a^{(ω)}_T ≥ 0` on `[0, ω_*(T)]`):** `g = ∫cos(ωu)dμ`, `μ ≥ 0`,
`supp μ ⊂ [0, ω_*(T)]`, `ω_*(T) ≈ π/(4T)` according to the table. The whole class reduces to cosines (Cor. 1.4): there is
no gain in seeking other dampings; the core of the matter is `ω ↦ a^{(ω)}_T` on that interval.

## §5 Is there a path to prove `a^{(ω)}_T ≥ 0`?
**Circularity, plainly.** (1) `a^{(ω)} ≥ 0` along `T_j → ∞`, `ω_j → 0` **implies** the target
(Lemma 1.3). (2) The target does **not** imply `a^{(ω)} ≥ 0`: by (2.2) even positivity of `W_T` on all
tests leaves the remainder `∫(1−cos ωu)(4cosh(u/2)−K)c_F`, without sign and of size `ω²T²e^{T}` ≫ margin. (3) It is a
**stronger** statement than the target in the directions with `Q(F) < 0` and weaker where `Q(F) > 0`; the measured margin
exists because `Q > 0` on the near-null directions. It is not circular, but it is not weaker either: it is a
strengthening with polynomial slack. The concrete inequality to prove is
`Σ_{N_T} v_n cos(π log n/4T) c_F(log n) ≤ Arch(F)  ∀F ∈ P_T`, with admissible loss constant `≲ c(T)ω²`.
**(a) Small T.** PROVED: for `T ≤ ½log 2` there are no contacts and `a^{(ω)} = Arch ≥ 0` (thm:index, `T ≤ 0.58`).
For `T ≤ ½log 3` (only `n = 2`): `0 ∈ K_T` (thm:index) and `v ∈ K_T` (Theorem A at `½log3` plus Lemma 1.2), hence
`[0, v_2] ⊂ K_T` by convexity and `a^{(ω)}_T ≥ 0` if `cos(ω log 2) ≥ 0`. Beyond: nothing, because `0 ∉ K_T` for
`T > T*_ev` and `w` is not a multiple of `v` with two or more contacts. "Large ω" does not help: it goes against `ω → 0`.
**(b) Induction in T.** With `ω = π/4T` the new integer enters with weight `v_n cos(π log n/4T) ≈ 0` at the boundary:
the cost of the new integers in `[2T, 2T+2dT)` is `O(e^{T}T·dT²)‖F‖²` (PROVED, elementary): free to first order.
What is not free: (b1) the shift of all the old weights, `∂_T w_n = v_n(ω log n/T)sin(ω log n)`, of
generic size `≲ (ω/T)Σ v_n log n|c_F(log n)| ≲ ω e^{T}‖F‖²` versus the budget `ω²c(T)`: deficit by a factor
`≍ e^{(1+β)T}/ω` unless there is cancellation in `Σv_n log n sin(ω log n)c_{F_*}(log n)`, not available; (b2) the growth
of the domain (new tests), whose Hadamard-type derivative is not bounded in the corpus. NO-GO (ARGUED) as
induction with a margin budget; reopening requires a bound on (b1) at the minimizer.
**(c) Known losses.** Measured margin: `0.01269, 0.00229, 0.00040, 0.00010` at `T = 0.8…2.0` (`k = 1`),
i.e. `≈ e^{−4.3T}…e^{−3.5T}` with the `ω²` included: `N^{−2}…N^{−1.7}`. The corpus only has **upper** bounds
with polynomial loss (P211-9A, `N^{16.5}e^{−2πN}`); the lower half (prob:ext-L) is OPEN. No known lower
bound has loss `≤ N^{−2}`: compatible in scale, nonexistent in content.
**What would be needed.** On the family, (3.1) ≥ 0 for every `φ`: a statement about the mean of the second
difference `q_ω` of the prime sum under `|M̂|²` (which contains exact `Λ` via `W_*(M,·) ≡ 0`). Outside the
family, the inequality above. Neither follows from tools of the corpus.

## §6 Controls
There is no proof with a step that could fail; what breaks is the measured positivity, on the family `X_δ` and at the step
named "radicality: `W_*(M,·) ≡ 0`" (Lemma 2(a) of R160_M4_R1), on which (3.1) depends:
- **`cΛ`:** `a(X_δ) = (1−c)P(M) + c·2.50ω² = −1.698(1−c) + 2.50cω²`; with `c < 1` and `ω² < 0.68(1−c)/c` it is negative:
  fails at the term `Arch_*(M∗φ)` of ROUND_021_A §4 (with `c > 1`, by the indefiniteness in `φ` of that term).
- **Delete `2`:** `a(X_δ) ≈ v_2cos(ω log 2)c_M(log 2) ≈ −9.56cos(ω log 2) < 0`: fails at radicality.
- **Beurling:** `−Σ(w_n−v_n)c_M(log n) = O(1)` with the sign of the profile of `c_M`: fails at radicality.
The violations are `O(1)` and the margin `O(ω²e^{−βT})`: the three controls break with room to spare.

## Balance
PROVED: Lemmas 1.1–1.3, Cor. 1.4, Prop. 2.1 (with polar term `−2ω²A′B′`), (3.1), §5(a) for `T ≤ ½log 3`.
NUMERICAL: `X_δ` gives `+2.50ω²`. ARGUED: Fejér fails because of high frequencies of its measure; (b) NO-GO.
OPEN: (3.1) ≥ 0 for every `φ` (cheap computation proposed); `a^{(ω)}_T ≥ 0` for large `T`; lower bound with
polynomial loss. Opened in this memo: the reduction of every positive-definite damping to cosines and the
identity (2.2). Not opened: any proof path of §5.
