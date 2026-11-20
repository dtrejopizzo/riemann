# Round 19, memo A — Scale control: is the margin `e^{−2πe^{2T}}` the lattice tail beyond `N = e^{2T}`?

Control note, deliberately modest. It is not a sign proof and is not presented as one. Notation of
P47 and of round 7: `a_T(F) = Arch(F) − Σ_n v_n c_F(log n)`, `v_n = 2Λ(n)/√n`, `c_F(u) = ∫F(t)F(t−u)dt`,
`P_T = {∫F e^{±t/2} = 0}`, `N := e^{2T}`. `W_*` = form of the explicit formula in the Weil class
`D^W` (prime sum over all `n`), as in `phase-160-row-d-infinite-T/R160_M4_R1.md`.

## Four-point filter

1. **Closest antecedent.** `R160_M4_R1.md` §4 (Theorem B(i), l.334–351), Remark C1 (l.427–431:
   «`2π` is the natural exponent of the truncation of a single radical») and O-5 (l.555–557: sharp constant
   open); rechecked in `ANNEX_MARGIN_CONFLICT.md` §3. For the tail of (PC):
   `phase-161-row-d-sum-product-square/R161_001_MUNTZ_CHEBYSHEV_ANOMALY.md` Thm. 2.1 and 3.1, §5;
   `ROUND_002_A.md` (Lemma and §(4)). «Poisson tails» side: `phase-211-sign-sandbox/ROUND_015_A.md`
   (comb on Poisson tails = `2⟨𝒯_log u, 𝒯u⟩`) and `ROUND_019_B.md` (reduction to admissible
   tails; master index P211-15A, P211-19B).
2. **What is new.** Only a control statement: the decomposition of the value `a_T(X_T)` by sources
   (archimedean diagonal, correction `a·u_ev`, primes `n ≥ N−2`), with the sign of the lattice tail
   `n > N`, and the behaviour of `a_T(X_T)` under the three controls. No object is proposed.
3. **Why it does not repeat.** No located source evaluates `a_T(X_T)` by sources or compares its
   exponent with a lattice tail; B(i) only bounds `|W_*(E)|` as a block. There is no new sign
   mechanism: the note does not claim to pass the filter as a construction.
4. **Connection with global positivity.** None directly. The only thing it could give is a constraint
   on the remainder `ρ_T` of an identity `a_T = ‖V_TF‖² + ρ_T` evaluated at `X_T`.

## §1 Cross-check of antecedents

- `grep` in `05-meta-and-planning/ROUTES-MASTER-INDEX.md` for `2πe^{2T}`, `near-radical`, `X_T`,
  `Poisson tail`, `first omitted`: the only occurrences of `X_T` as an almost-null vector are l.31144–31146
  (record of R160_M4_R1: «the object must bring `X_T` almost to zero at that scale»); the `X_T` of
  G1C-R161_020-021 (l.5235, l.12338) and of 16_03 (l.21265, l.30658) are **other** objects (a dispersion
  scalar and an operator). Q-P2.2 (l.9305) asks for a near-radical block with quantitative Guo, without
  evaluation. No entry states «margin = first omitted lattice term at `N = e^{2T}`».
- In the corpus, «first omitted / primer término omitido» does not appear in this sense. R160_M4_R1
  Remark C1 says the closest thing: `2π` = twice the decay rate `π` of `K_Pó`, which by
  Theorem C is the maximum possible in the ξ-divisible radical. 106_09 (bound `Cλ^Me^{−cλ²}`, `λ = e^T`, `c`
  unspecified) has the same origin (cutoffs of `K, K′, K″`), without evaluating the tail of (PC).
- **The tail of (PC) was never evaluated at `X_T`.** Moreover it cannot be evaluated as such: (PC) is an
  operator identity `S_N A_{M_0} 𝓕 = …`, and to read `a_T(F)` in it one needs a test
  `z = S_N𝓕g = F` with `g` in the window, which has no solution (`ROUND_002_A` §(4), `REVIEW_001_ABD`
  §4.1). What does appear in `a_T(X_T)` is the prime sum of `W_*` over `n > N` (§2).
- **What `ROUND_002_A` closed.** Class NO-GO (Lemma, PROVED): forms `C^w − ⟨α, Bα⟩` with moment test
  `Σ_L`, `L` finite, any weight `w ≥ 0` at `k > N`: none is semidefinite on `P_T`; the tail is not
  `±(Σ_k h(k)|ℓ_k|² + ρ)` with `ℓ_k` in moments of order `≤ L`. An evaluation on **one** explicit
  vector is not a form on `P_T` and lies outside that class; but it cannot give a sign either: only
  constraints. That is how it is treated here.

## §2 The computation

**Vector** (R160_M4_R1 l.346–351; ANNEX §3). `K_Pó(t) = Σ_{n≥1}(4π²n⁴e^{9t/2} − 6πn²e^{5t/2})e^{−πn²e^{2t}}`,
even, `Φ_{K_Pó} = ξ`; `M = −K_Pó″ + ¼K_Pó`, `Φ_M(s) = s(1−s)ξ(s)`, `M ∈ P_T`-type (`A(M) = B(M) = 0`).
`χ_T` smooth cutoff, `= 1` on `[−T+θ, T−θ]`, `θ = e^{−2T}`; `E = M(1−χ_T)`; `a = −ℓ_ev(E)`;
`X_T = Mχ_T − a u_ev ∈ P_T`. With `Y = E + a u_ev`:

    a_T(X_T) = W_*(Y) = W_*(E) + 2a W_*(u_ev, E) + a² W_*(u_ev).                          (2.1)

(PROVED in the memo; here CITED, rechecked in ANNEX §3.)

**Where `e^{−2πe^{2T}}` comes from in the proof.** There is no contour and no Bessel: it is the Gaussian tail of the
term `n = 1` of the theta series, `|K_Pó^{(j)}(t)| ≤ c_j e^{(9/2+2j)|t|} e^{−πe^{2|t|}}` (Lemma 3), evaluated at
the edge of the support of `E`, `e^{2(T−θ)} = N − 2 + O(e^{−2T})`. Each factor (`‖E‖`, `a`, `𝔪_T(E)`) is
`e^{cT}e^{−πN}`; `2π` comes from (2.1) being **quadratic** in the tail. That is,
`e^{−2πN} = (e^{−π·1²·x})²|_{x=N}`: lattice point `n = 1` of `ℤ` in the theta Gaussian, squared;
not a term `e^{−2πky}` at `k = N`. (PROVED as a reading of the proof.)

**Decomposition by sources** (ARGUED: Laplace estimates on `e^{−π(e^{2t}+e^{2s})}`, without
written constants). Let `ε_N := e^{−2πN}`.

(a) *Archimedean diagonal.* `Arch_*(E) ≈ ∫ m(τ)|Ê(τ)|²dτ`; `E` lives at frequencies `|τ| ≳ e^{2T}`
(collapse of the cutoff in width `θ` and oscillation of the Gaussian), where `m(τ) ~ log|τ| > 0`. Size
`e^{cT}ε_N`, **positive**.

(b) *Primes `n < N − 2`.* For `E(t)E(t−log n) ≠ 0` with both points in `|·| ≥ T−θ` one needs
`log n ≥ 2T−2θ` (opposite sides) or both on the same side, with exponent `−π(N−2)(1+n²) ≤ −5π(N−2)`.
Negligible.

(c) *Primes `n ≥ N − 2` (the «lattice tail beyond `N`»).* Opposite sides: `c_E(log n) ≈
∫E(t)E(log n − t)dt` (parity of `E`), exponent `−π(e^{2t} + n²e^{−2t})`, minimum `−2πn` at `e^{2t} = n`,
admissible exactly when `n ≥ N − 2`. Thus `c_E(log n) = e^{cT}e^{−2πn}`·(shape factor), and
`−Σ_{n≥N−2} v_n c_E(log n)` has the **same exponent** `2πN`, dominated by the two or three integers
`n ∈ [N−2, N+2]` and decreasing like `e^{−2πn}` afterwards. Scale coincidence: **yes**, but by the
same Gaussian (inequality `e^{2t} + n²e^{−2t} ≥ 2n`), not by a Poisson lattice.

(d) *Correction `a·u_ev`.* `2aW_*(u_ev,E)`: `a = e^{cT}e^{−πN}`, and `W_*(u_ev, E)` contains primes with
`log n ≈ T`, i.e. `n ≈ √N = e^T` (contacts of `u_ev ⊂ (−½,½)` with the tail at `±T`), of size
`e^{cT}e^{−πN}`. Product: again `e^{cT}ε_N`, with arithmetic at `n ≈ e^T`, not at `n ≈ e^{2T}`.

**Conclusion of the computation.** The exponent `2πe^{2T}` is common to (a), (c) and (d); the natural cutoff for
(c) is `N = e^{2T}` (not `e^T`), but (d) introduces `e^T`. The constant in front of `ε_N` depends on
`χ_T`, `θ`, `u_ev` and on `Λ` at a few integers near `N` and near `√N`: it is not canonical (it is
O-5, sharp constant, open). The term `H_{M,N}` of (PC) does not appear: what appears is the prime sum
of `W_*` restricted to `n ≥ N − 2`.

## §3 Sign and controls

**Sign of the tail `n > N` at `X_T`** (ARGUED, verifiable by asymptotics of the term `n = 1`). For large `t`,
`K_Pó″ ≈ 16π⁴ e^{17t/2}e^{−πe^{2t}} > 0`, hence `M < 0` at `t ≥ T−1` (`M(1.5) ≈ −1.9·10^{−19}`,
NUMERICAL) and `E ≤ 0` at `t ≥ 0`. Then `E(t)E(log n − t) ≥ 0` and `c_E(log n) > 0` at first order for
`n ≥ N − 2`: the lattice tail enters `a_T(X_T)` as `−Σ_{n≥N−2} v_n c_E(log n) < 0`. It is a sum with
coefficients `v_n ≥ 0` of positive products (not squares), **with a minus sign**. What is positive at that
scale is (a), the high-frequency archimedean energy of the cutoff tail. The reading «`ρ_T` = lattice tail
beyond `N`» has the wrong sign.

**What cancellation makes `X_T` almost null.** `W_*(M, ·) ≡ 0` (Lemma 2(a) of the memo): `Φ_M = s(1−s)ξ`
vanishes at all zeros, by the theta functional equation (Poisson on `ℤ`: `θ(1/x) = √x θ(x)`,
integer spacing) **together with** the Euler product (prime sum with exact `Λ`). It uses the spacing of
the integers twice: in the radical and in the tail rate `π` (first nonzero point `n = 1`).

**Controls.** For a weight `w`, `W^w_* = W_* − Σ_n (w_n − v_n) c(log n)`, and `c_{X_T}(log n) = c_M(log n)
+ O(e^{cT}e^{−πN})`. Hence

    a^w_T(X_T) = −Σ_n (w_n − v_n) c_M(log n) + O(e^{cT}e^{−πN}).                         (3.1)

The step that fails is Lemma 2(a): `M` stops being in the radical of `W^w_*`. Values (NUMERICAL,
quadrature on `[−6,6]`, step `5·10^{−5}`, `n < 2·10⁴`): `c_M(log 2) ≈ −9.753`, `c_M(log 3) ≈ +6.066`,
`c_M(log 4) ≈ +0.235`, `P(M) := Σ v_n c_M(log n) ≈ −1.698`, `‖M‖² ≈ 97.47`.

- `2Λ`: `a^{(2)}_T(X_T) → −P(M) ≈ +1.70 > 0`. The near-null breaks at `O(1)` but towards **positive**:
  `X_T` is not a witness for `c = 2`. (For `c < 1` it gives `(1−c)P(M) < 0`; in particular `Arch(X_T) ≈ P(M) < 0`,
  consistent with F2.)
- Delete `p^k`: `a^{del}_T(X_T) → v_{p^k} c_M(k log p)`. Delete `2`: `√2 log 2·(−9.753) ≈ −9.56 < 0`,
  `X_T` is a negative witness at `O(1)`. Delete `3`: `≈ +7.70 > 0`.
- Beurling: `−Σ(w_n − v_n)c_M(log n)`, `O(1)` and with sign determined by the profile `c_M`, which alternates
  at `n = 2, 3` and is negligible for `n ≥ 7` (`c_M(log 7) ≈ 3·10^{−7}`).

Reading: the near-null of `X_T` is a property of the radical, not of the sign; under control it is lost at
first order, with a sign fixed by `c_M` at `n = 2, 3`. The tail `n > N` plays no role in any of
the three controls at first order.

## §4 Verdict

1. (i) **Refuted as a reading** (ARGUED for orders and sign; PROVED the origin of the exponent): the
   exponent `2πe^{2T}` is `(e^{−π·1²·e^{2T}})²`, Gaussian tail of the term `n = 1` of theta, squared.
   The prime sum over `n ≥ N − 2` reproduces the same exponent (same Gaussian, `e^{2t}+n²e^{−2t} ≥ 2n`),
   but enters with **negative** sign, and shares its order with the archimedean diagonal (positive) and with the
   correction `a·u_ev` (primes `n ≈ e^T`). No canonical constant (O-5 remains OPEN).
2. The tail `H_{M,N}` of (PC) cannot be evaluated at `X_T`: (PC) does not contain `a_T(X_T)` without `z = F`
   (ROUND_002_A §(4)); it was not computed, because it cannot be formulated, not because of cost.
3. (ii) Implication for the object: only a **constraint** (ARGUED): `ρ_T` cannot be a lattice
   tail `Σ_{k>N}(weights ≥ 0)·(products of the tail)`, because at `X_T` that tail is negative and is
   compensated by the high-frequency archimedean energy. There is no candidate `ρ_T` with a formula.
4. Controls (NUMERICAL + identity (3.1) PROVED at first order): `2Λ` gives positive `X_T` (`≈ +1.70`);
   deleting `2` gives `≈ −9.56`; the break is in Lemma 2(a) (radical) and depends on `c_M` at `n = 2, 3`,
   not on the tail.
5. (iii) Next operation: **none** in this direction. Computing the constant of `ε_N` would be LOCAL
   and decides nothing (it depends on `χ_T`, `u_ev`).

Disposable auxiliary computation (not part of the record): quadrature script for `c_M(log n)`.
