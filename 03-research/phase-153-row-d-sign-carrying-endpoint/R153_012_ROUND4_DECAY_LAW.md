# R153.012 — Round 4 (construction): the decay law of `λ(T) = λ_min(A_T|P_T)` on `[0.30, log 2]`

Scripts: `scripts/round4/` (`core.py`, `scan.py`, `dense.py`, `mu.py`, `second.py`, `rate.py`, `table.py`, `zeroprofile.py`, `boundary.py`),
reusing `scripts/audit/aud_spectral.py` (`basis_hat`, `moments`) verbatim as the discretisation of record.*

## 0. Corpus check (run before building)

`grep -rIl "Slepian"` → `phase-7-weil-carleson-sine-kernel/connes/prolate_bridge.py`, `phase-73/E73_277` (a declared bridge, no
computation), `phase-5/M5`, `phase-137` (a CC preprint), `R153_011`. `"decay rate of λ"`, `"c(T)"` as an exponent
→ **no hits**; `"boundary exponent"` only `P122_019` and a phase-114 Carleson script. Phase 118 `SPEC.md:70`
records `lam_min_norm` decreasing under refinement in a *different* normalisation, limit left open
(`PHASE_118_CLOSURE.md:99`). **No prior file computes `λ(T)` as a function of `T`, its logarithmic derivative, or
the boundary behaviour of the minimiser.**

Pipeline validated against the record before producing any new number: `core.lam_min` reproduces R153_008 at
`T = log 2` exactly (`K = 160 → 1.06754·10⁻⁷`, `K = 240 → 1.04378·10⁻⁷`, `λ_e = 1.044·10⁻⁷`, `λ_o = 1.178·10⁻⁵`).

## 1. Object, normalisation, precision

`A_T` is Paper 42 `eq:localizedprimitiveoperator`, symbol
`g_T(τ) = Re ψ(¼+iτ/2) − log π − 2Σ_{n<e^{2T}} Λ(n)n^{−1/2} cos(τ log n)`;
`P_T = ker M_− ∩ ker M_+`; `λ(T) = min{⟨A_TF,F⟩/‖F‖²_{L²} : F ∈ P_T}` (L² Rayleigh), `c(T) = −d log λ/dT`.

*Parity.* `A_T` commutes with `t ↦ −t` and `R P_T = P_T` (R153_008 §2.1, `PROVED`). In the sine basis
`φ_k(t) = sin(kπ(t+T)/2T)`, odd `k` spans the even block and even `k` the odd block; in each block the two Tate
moments collapse to one. All computations below are block-diagonal, which is also what makes the `K = 320`
runs affordable.

*Contacts.* On `[0.30, log 2]` the contact set is `∅` for `T < ½log2 = 0.3466`, `{2}` for `T < ½log3 = 0.5493`,
`{2,3}` for `T ≤ log 2`; `n = 4` is born **at** `T = log 2` (`n < e^{2T}`) and is absent throughout. The window is
therefore threshold-free in its interior except at the two marked points, and the `n = 4` omission that caveats
R153_008 §3 does not touch anything here.

*Precision (of record).* Galerkin ⇒ every `λ` is an **upper bound**, decreasing in `K`. Errors: linear algebra
`~10⁻¹³` absolute (`‖M‖ ~ 10³`, double precision) = 6 digits at `λ ~ 10⁻⁷`; quadrature (400 graded Legendre
panels, `τ_max = 4000`, `ng = 24`) `≈ 10⁻¹¹` (R153_008's sensitivity study) = 4 digits; basis truncation `O(1/K)`
— dominant, `1.3 %` from `K = 240` to `320` at `log 2`, and *explained* in §5.2. **Verdict: 4 trustworthy digits
of the Galerkin eigenvalue; 2 digits as an approximation of the true `λ(T)` (`1/K` Richardson gives
`λ(log 2) ≈ 9.91·10⁻⁸`).** `c(T)` is better conditioned — the `K`-dependence cancels in the log-derivative
(`0.14 %` from `K = 240` to `320`) — so `c(T)` carries 3 digits. Double precision suffices; the one function
missing from scipy (`ψ''` at complex argument) is `core.psi2`, recurrence + asymptotics, agreeing with
`mpmath.polygamma(2,·)` to `10⁻¹⁵`.

## 2. The table

`DIAGNOSTIC-NUMERIC`. `c_HF` is the Hellmann–Feynman rate of §5 at `K = 320` (it agrees with centred finite
differences to 4–5 digits at every `T` tested, see §5).

| `T` | `λ` (K=160) | `λ` (K=240) | `λ` (K=320) | `1/K` Richardson | parity | `c(T) = −dlogλ/dT` |
|---|---|---|---|---|---|---|
| 0.3000 | 6.94105e−01 | 6.93414e−01 | 6.93059e−01 | 6.91994e−01 | even | 4.83 |
| 0.3400 | 5.68412e−01 | 5.67721e−01 | 5.67367e−01 | 5.66305e−01 | even | 5.21 |
| **0.3466** = ½log2 | 5.49092e−01 | 5.48401e−01 | 5.48048e−01 | 5.46987e−01 | even | 5.30 (kink) |
| 0.3800 | 3.47104e−01 | 3.45411e−01 | 3.44488e−01 | 3.41719e−01 | even | 19.29 |
| 0.4200 | 1.45567e−01 | 1.44582e−01 | 1.44079e−01 | 1.42569e−01 | even | 23.72 |
| 0.4600 | 5.09979e−02 | 5.05290e−02 | 5.02882e−02 | 4.95658e−02 | even | 29.67 |
| 0.5000 | 1.24092e−02 | 1.22298e−02 | 1.21395e−02 | 1.18688e−02 | even | 43.21 |
| 0.5400 | 1.50526e−03 | 1.47784e−03 | 1.46399e−03 | 1.42242e−03 | even | 53.80 |
| **0.5493** = ½log3 | 9.79358e−04 | 9.68423e−04 | 9.62755e−04 | 9.45751e−04 | even | 33.60 (kink) |
| 0.5800 | 2.21800e−04 | 2.17740e−04 | 2.15564e−04 | 2.09036e−04 | even | 53.88 |
| 0.6200 | 1.97504e−05 | 1.93062e−05 | 1.90673e−05 | 1.83508e−05 | even | 66.98 |
| 0.6500 | 2.49055e−06 | 2.43485e−06 | 2.40428e−06 | 2.31257e−06 | even | 67.92 |
| 0.6800 | 3.36757e−07 | 3.28222e−07 | 3.23645e−07 | 3.09915e−07 | even | 78.32 |
| **0.6931** = log2 | 1.06754e−07 | 1.04378e−07 | 1.03071e−07 | 9.91476e−08 | even | 75.77 |

**The minimiser is in the even block at every `T` of `[0.30, log 2]`** (odd ground value `1.18·10⁻⁵` at `log 2`,
two orders above). Complement to R153_010's amendment: below `log 2` the binding direction is even everywhere;
the odd block becomes the smaller one only above `T ≈ 0.7038` (R153_008 §3).

Local structure of `c` (centred differences, `K = 240`, step `0.0033`, script `dense.py`; and `rate.py` near the
right end): `c` is `≈ 5` on `[0.30, 0.3466]` (no primes: pure Gamma), rises to `≈ 56` at `T = 0.526`, **dips to
`≈ 45` across the `½log3` threshold**, then rises monotonically to a maximum `c ≈ 92.8` at `T ≈ 0.6888`, and
falls back to `75.8` at `T = log 2`. Neither the two kinks nor the terminal fall is a discretisation artefact:
both are reproduced by the independent Hellmann–Feynman formula of §5 and are `K`-stable to `0.2 %`.

**`c(T)` has no plateau.** Over the certified window it sweeps `5 → 93`; a single exponential law is wrong by a
factor `19`. Fitting `λ ≍ exp(−κT^p)` on the clean two-prime stretch `[0.56, 0.689]` gives `p ≈ 4.4` — i.e. no
simple law; `c` is an increasing function of `T` with threshold kinks, and any statement "`λ(T) ≍ e^{−cT}`" is a
mis-description of the data on this window.

## 3. Confrontation 1 — the Slepian / origin-gap prediction (`c → 2γ_1 ≈ 28.3`): **REFUTED as a rate**

*The prediction, stated properly.* Under RH, on `P_T`, `⟨A_TF,F⟩ = Σ_ρ F̂(ρ)F̂(1−ρ) = Σ_γ |F̂(γ)|²`
(R153_007 T1.1, `RESTATEMENT` of Paper 42 `main.tex:1965`; the left side is computed unconditionally from Gamma
and primes — RH enters only in reading it). The zero measure has no mass in `(−γ_1,γ_1)`, `γ_1 = 14.1347`. A
trial `F` supported in `(−T,T)` whose transform concentrates in that band leaks a fraction `1 − λ_0(c_S)` of its
energy outside, `c_S = γ_1T`, and Landau–Widom/Slepian gives `1 − λ_0(c) ∼ 4√π √c e^{−2c}`. With the zero
density `≈ 1/(γ_2−γ_1)` converting an integral into a sum one predicts
`λ(T) ≈ (2π/(γ_2−γ_1))·4√π√(γ_1T)e^{−2γ_1T}` and `c(T) = 2γ_1 − 1/(2T) → 28.27`. Label: `DIAGNOSTIC/heuristic`.

*Value.* At `T = log 2`: `c_S = 9.798`, `1−λ_0 ≈ 6.84·10⁻⁸`, predicted `λ ≈ 6.3·10⁻⁸` against a measured
`9.91·10⁻⁸` — a factor `1.6`. That near-miss is what made the prediction attractive; it does not survive at the
other end (`T = 0.30`: predicted `3·10⁻³`, measured `0.693`, wrong by `230×`).

*Rate.* The prediction is `c(log 2) = 27.55`. Measured: `75.8` (and `92.8` at `T = 0.689`). **Factor `2.8` off,
and with the wrong sign of variation** — Slepian's `c(T)` decreases in `T`, the data increase.

*Why it fails.* Expand the minimiser against the first 600 zeros (`scripts/round3/zeros600.npy`). First an
independent validation: `Σ_{γ<600}|F̂(γ)|²/⟨A_TF,F⟩ = 0.997–0.998` at every `T` — **the explicit formula verified
to `0.3 %` by two separate computations (Gamma+primes vs zeros)**. The Weil mass at the minimiser:

| `T` | `λ` | share at `γ_1` | at `γ_2` | at `γ_3` | median `γ` | 90 % below |
|---|---|---|---|---|---|---|
| 0.45 | 6.73e−2 | 12.4 % | 31.9 % | 25.5 % | 25.0 | 88.8 |
| 0.55 | 9.46e−4 | 0.30 % | 2.3 % | 6.9 % | 32.9 | 118.8 |
| 0.60 | 6.94e−5 | 0.03 % | 0.33 % | 1.5 % | 48.0 | 182.2 |
| 0.65 | 2.43e−6 | <0.01 % | 0.02 % | 0.13 % | 43.3 | 202.5 |
| log 2 | 1.04e−7 | <0.01 % | <0.01 % | 0.01 % | 65.1 | 229.3 |

**The minimiser does not live in the origin gap.** By `T = log 2` it has driven the first two dozen zeros to
essentially zero and leaks at `γ ≈ 40–230`. Concentration in `(−γ_1,γ_1)` is only one trial function; the true
minimiser *also puts zeros of `F̂` at the low `γ_n`*, buys a much smaller value, and pays with bandwidth. The
band edge that governs the exponent is therefore not `γ_1` but an effective `Ω_eff(T) ≈ c(T)/2 ≈ 38–46` — of the
order of the observed median of the Weil mass. The increase of `c(T)` with `T` is exactly this: as the window
lengthens the minimiser can afford to annihilate more zeros and the effective edge moves out.

**Verdict.** `c → 2γ_1` is `REFUTED` on `[0.30, log 2]`. The origin-gap picture is the wrong extremal problem;
the right one is *multi-null* concentration (nulls at `γ_1,…,γ_m` **plus** concentration), with exponent
`2Ω_eff(T)`, `Ω_eff` increasing. Doc 143's reading applies, sharpened: `λ(T)` is the Riesz/Ingham lower frame
bound of `{e^{iγt}}` on `(−T,T)`; the system has **infinite Beurling density**, so Ingham's `a·δ_* > π` threshold
is never met at fixed `T` and no single ordinate gap controls the bound.

## 4. Confrontation 2 — the `Ξ_a` second-order prediction (`c ≈ 75`): **CONFIRMED, on a different space**

### Theorem 4.1 (second-order expansion of `A_T^{(a)}`) — `PROVED`

> Let `E_a` be multiplication by `e^{at}` and `A_T^{(a)} = E_{−a}A_TE_a + E_aA_TE_{−a}` (Theorem A, R153_005,
> `PROVED`). Then, as operators on `C_c^∞(I_T)`,
> `A_T^{(a)} = 2A_T + a²D_T + O(a⁴)`, `D_T = [t,[t,A_T]] = ad_t²(A_T)`,
> and `D_T` is **exactly the Fourier multiplier with symbol `−g_T''(τ)`**, i.e.
> `D_T = −(1/4)Re ψ''(¼+iτ/2) + 2Σ_{n<e^{2T}} Λ(n)n^{−1/2}(log n)² cos(τ log n)` as a multiplier.
> Equivalently `D_T = −g_Γ''(D) + Σ_n w_n(log n)²(S_{log n}+S_{−log n})`: the prime weights acquire `(log n)²`
> **with the sign reversed** relative to `A_T`, and the archimedean multiplier is `−g_Γ''`.
> The constant `m_0` contributes nothing (`ad_t²` kills multiples of the identity), so there is **no polar term
> in the operator**; the entire polar/moment content of the expansion sits in the *domain*: `P_T^{(a)}` is cut by
> the four moments at `β ∈ {±(½±a)}`, which degenerate as `a→0⁺` to the **codimension-4** space
> `P_T^{(2)} := {F : ∫Fe^{±t/2} = ∫ tFe^{±t/2} = 0} ⊊ P_T`, not to `P_T`.

*Proof.* (i) `e^{−aX}Ae^{aX} = A + a[A,X] + (a²/2)[[A,X],X] + O(a³)`
with `X` = multiplication by `t`; adding the same with `a ↦ −a` cancels every odd power, giving
`A^{(a)} = 2A + a²[[A,X],X] + O(a⁴)`, and `[[A,X],X] = AX²−2XAX+X²A = [X,[X,A]] = ad_t²(A)`.
(ii) Under `F ↦ F̂(τ)=∫Fe^{−iτt}dt`, multiplication by `t` becomes `i∂_τ`, so for a multiplier `m(D)`,
`ad_t(m) = [i∂_τ, m] = im'` and `ad_t²(m) = [i∂_τ, im'] = −m''`. Both `G_{Γ,T}` and `S_{±log n}` are multipliers
(`cos(τ log n)`), and `m_0` is the multiplier `m ≡ m_0` with `m'' = 0`. Hence `D_T` is the multiplier `−g_T''`,
which is the displayed formula (`d²/dτ² Re ψ(¼+iτ/2) = −¼ Re ψ''(¼+iτ/2)`, and
`d²/dτ²(−2w_n cos(τ log n)) = 2w_n(log n)²cos(τ log n)`).
(iii) Consistency check with the symbol: `A^{(a)}` has symbol `g(τ+ia)+g(τ−ia) = 2g(τ) − a²g''(τ) + O(a⁴)`,
where for the prime part `−2w_n[cos((τ+ia)ℓ)+cos((τ−ia)ℓ)] = −2w_n(n^a+n^{−a})cos(τℓ)` — exactly Prop. 12.6's
weights, and for the Gamma part `Σ_± Re ψ(¼∓a/2+iτ/2) − 2log π`, exactly Lemma C1's ladder. So the conjugation
identity and the symbol shift are the same statement, and the `a²` coefficient is `−g''`, matching (ii). ∎

*Corpus check for 4.1.* `grep -rIn "ad_t\|\[t,\[t,"` → no hits; `D_T` is new. Theorem A itself is R153_005's.

### The prediction and its numerical confirmation

With `μ(T) := λ_min(A_T | P_T^{(2)})` (codim 4) and `F` its minimiser, `q_D(T) := ⟨D_TF,F⟩/‖F‖²`, the threshold
`T*(a)` of R153_003 §4 satisfies, to second order, `2μ(T*) + a²q_D(T*) = 0`. Measured (`K = 240`):

| `T` | `μ(T)` | `q_D(T)` |
|---|---|---|
| 0.66 | 5.022e−3 | −0.2295 |
| 0.69 | 7.327e−4 | −0.1954 |
| 0.72 | 1.126e−4 | −0.1715 |
| 0.75 | 9.923e−6 | −0.1532 |
| 0.78 | 8.013e−7 | −0.1408 |
| 0.81 | 5.416e−8 | −0.1286 |

`q_D < 0` throughout (the `(log n)²`-reweighted primes dominate `−g_Γ''`), which is *why* a threshold exists at
all. Solving `2μ(T)+a²q_D(T)=0` against the exact `λ_min(A_T^{(a)}|P_T^{(a)})` computed from Prop. 12.6's symbol
with the four exact moments (script `second.py`, full contact set including `n = 4,5,7,8,9`):

| `a` | `T*` exact | `T*` from Thm 4.1 | `2μ+a²q_D` at `T*` exact | `λ_min(A^{(a)})` at `T*` 2nd-order |
|---|---|---|---|---|
| 0.001 | 0.80827 | 0.80827 | `+3.29e−11` | `−3.29e−11` |
| 0.005 | 0.76943 | 0.76943 | `+1.17e−09` | `−1.17e−09` |
| 0.01 | 0.75304 | 0.75304 | `+7.61e−09` | `−7.61e−09` |
| 0.03 | 0.72546 | 0.72548 | `+1.86e−07` | `−1.86e−07` |

**The second-order expansion reproduces `T*(a)` to five decimals for `a ≤ 0.01` and to `2·10⁻⁵` at `a = 0.03`**
(`DIAGNOSTIC-NUMERIC`; the `O(a⁴)` term is visible only at `a = 0.03`). The R153_003 table is thereby explained:
`T*(a)` is, to second order, the level set of `μ`.

Differentiating `log(2μ(T*)) = 2log a + log|q_D(T*)|`:
`dT*/d log(1/a) = 2/(c_μ(T*) + d log|q_D|/dT)`, `c_μ = −d log μ/dT`.
Measured `c_μ` (script `mu.py`, `K = 240`): mean `79.3` on `[0.69,0.81]`, `86.0` on `[0.69,0.86]`, pointwise
`60 → 99`; and `d log|q_D|/dT ≈ −2.9`. The predicted slope is `2/(79.3−2.9) = 0.0262` against the fitted
`0.0268` of R153_003 — **agreement to `2 %`**, i.e. the fit `c = 2/0.0268 = 74.6` is right.

**Verdict.** `c ≈ 75` is `CONFIRMED`, but it is **not** the decay rate of `λ` on `[0.30, log 2]`. It is the decay
rate `c_μ` of the *codimension-4* minimum `μ(T)` over the range `T ∈ [0.685, 0.81]` where the `T*(a)` data live —
a different space and a different window. This is the answer to the blueprint's question "is the minimiser of
`A_T` not the minimiser of the `Ξ_a` form?": **correct, and the reason is the moment constraint, exactly as the
blueprint's third option suggested.** `P_T^{(a)}` imposes four moments, not two; `μ ≥ λ` (e.g. at `T = 0.69`,
`μ = 7.33·10⁻⁴` against `λ = 1.37·10⁻⁷`, a factor `5·10³`), and the two decay at comparable but distinct rates.

## 5. Confrontation 3 — the Hellmann–Feynman rate and the boundary exponent

### 5.1 The rate formula (`PROVED`, elementary) and its numerical verification

Rescale to `(−1,1)` as in D.133 §1. Between thresholds the contact set is locally constant, and the only
`T`-dependence of the symbol is through `α_n = log n/T` and `σ/T`. Hellmann–Feynman at a simple block ground
eigenvalue gives, with `F = F_T` normalised,

> `dλ/dT = −(1/T)·(1/2π)∫_ℝ τ g_T'(τ)|F̂(τ)|²dτ − (1/T)Σ_± (±)c_±∫ tF(t)e^{±t/2}dt`,

where `c_±` are the Lagrange multipliers of `(A_T−λ)F = c_+e^{t/2}+c_−e^{−t/2}`. The first integral splits
exactly into D.133's items (1) and (2): the **Gamma shape derivative** `−(1/T)(1/2π)∫τ g_Γ'(τ)|F̂|²` and one
**transport derivative per contact**, which in `t`-space is `+(2w_n log n/T)·c_F'(log n)`, `c_F(b)=∫F(t)F(t+b)dt`
— the same autocorrelation derivative that R153_008 (2.2) identified in the `b`-variable. The last term is
D.133's item (4), the derivative of the two-Tate projection. D.133's item (3), the **rank-two endpoint form
`−(2w_N/T_N)(F̄(−1)F(1)+F̄(1)F(−1))`, is absent away from a threshold** and appears only in the right derivative
at `T = ½log N`. Measured (`K = 240`; `c_FD` from centred differences, `h = 10⁻⁴`):

| `T` | `λ` | Gamma shape | transport `n=2` | transport `n=3` | Tate drift | sum | finite diff | `c_HF` | `c_FD` |
|---|---|---|---|---|---|---|---|---|---|
| 0.60 | 6.938e−5 | −1.671266 | +1.879318 | −0.212229 | −2.92e−6 | −4.17958e−3 | −4.17861e−3 | 60.243 | 60.229 |
| 0.65 | 2.435e−6 | −1.542929 | +1.890938 | −0.348174 | −9.88e−8 | −1.65204e−4 | −1.65227e−4 | 67.850 | 67.859 |
| 0.69 | 1.368e−7 | −1.453636 | +1.877827 | −0.424204 | −5.40e−9 | −1.25608e−5 | −1.25600e−5 | 91.796 | 91.791 |
| log2 | 1.044e−7 | −1.447046 | +1.875819 | −0.428780 | −4.11e−9 | −8.08309e−6 | −8.08374e−6 | 77.440 | 77.447 |

**Verified to 4–5 digits — and it says what §2 cannot.** The three terms are `O(1)` (`−1.45`, `+1.88`, `−0.43`
at `log 2`); their sum is `8·10⁻⁶`. The rate is an exact cancellation over **five to six orders of magnitude**
between the archimedean shape derivative and the prime transport terms. Consequences:

1. **No term-by-term bound on `c(T)` can exist.** Any estimate that bounds the Gamma term and the transport terms
   separately loses `10⁵`. This is D.133's verdict ("no uniform signed Hadamard induction") re-derived at the
   minimiser, and it now has a number attached to it.
2. The Tate-drift term is `10⁻⁹`–`10⁻⁶` of the total: the moment constraints contribute nothing to the rate on
   `P_T`. (They contribute everything to the *value*, cf. §4: `μ/λ ≈ 5·10³`.)
3. `dλ/dT < 0` at every `T` sampled, consistent with the `RESTATEMENT` Q3(i) monotonicity.

### 5.2 The boundary exponent — `F_T(±T) = 0`, `α ≈ 1.2` at `T = 0.60`, `≈ 2.2` at `T = log 2`

*Analytic input.* `g_Γ(τ) ~ log(|τ|/2)`, so the form domain is `{F : ∫log(2+|τ|)|F̂|²dτ < ∞}`, strictly weaker
than `H^{1/2}`: **point evaluation is unbounded on it** — D.133's obstruction. Nothing in the domain forces
`F(±T) = 0`, and the Euler–Lagrange equation `A_TF = λF + c_+e^{t/2}+c_−e^{−t/2}` gains only a logarithm of
regularity. It must be measured.

*Measurement (`DIAGNOSTIC-NUMERIC`).* Two independent readings of the same minimiser.
(i) *Endpoint values.* `|F_T(−T+h)|` fitted over `h ∈ [0.04,0.20]` (the range resolved by the basis;
`2T/K = 0.004` at `K = 320`): global exponent `α = 1.250` at `T = 0.60` and `2.163` at `T = log 2`, **stable to
three digits across `K = 160/240/320`**. The local exponent drifts within the range (`0.84 → 1.18` at `T = 0.60`;
`2.14 → 1.81` at `log 2`), so this is an *effective* exponent, not a clean power law; the drift sets in at
`h ≈ 0.02 ≈ 1/Ω_eff`, i.e. at the scale of the boundary layer that the basis cannot resolve.
(ii) *Coefficient asymptotics.* A jump `F(±T) = A ≠ 0` would give even-block coefficients `c_k ≈ 4A/(kπ)`.
Measured `c_k kπ/4` for odd `k ∈ [101,301]` at `T = log 2`, `K = 320`: `−0.0006, −0.0010, −0.0006, −0.0007,
−0.0004` against `F(0) = 1.694` — i.e. `A/‖F‖_∞ < 5·10⁻⁴`. **No jump.**

**Verdict: `α ≥ 1`, and `F_T(±T) = 0`.** Therefore, at a threshold `T = ½log N`, D.133's rank-two endpoint form
(0.1) **vanishes at the minimiser**, and the right derivative of `λ` is carried by the Gamma shape derivative,
the transport terms and the Tate drift alone. This does **not** bypass D.133's obstruction: the vanishing is a
property of *one* vector, established numerically, not a bound on the functional `F ↦ F(±T)` over the form
domain, which remains unbounded. D.133's conclusion — no signed induction — stands untouched; what §5.2 adds is
that the failure is not located in the endpoint term.

*Byproduct.* The observed `O(1/K)` Galerkin convergence (R153_008 §1, the `1/K` Richardson) is now explained: the
even-block coefficients decay like `k^{−1}`·(oscillation) because of the boundary layer at scale `1/Ω_eff`, which
gives a Rayleigh-quotient error `≍ log K/K`. `DIAGNOSTIC`.

## 6. What a bound `c(T) ≤ c_0` would mean — and what is prime-computable

`c(T) ≤ c_0` for all `T` is `λ(T) ≥ λ(T_0)e^{−c_0(T−T_0)} > 0` for `T ≥ T_0`, i.e. **`A_T ≥ 0` for every `T`
with an explicit rate** — a restatement of RH (via Paper 42's row-D chain) *with a modulus*. Doc 143 §4.4 already
liquidated that target: the modulus of the localized Weil form is computable **from the zeros, not the primes**
(Thm 143.B, a Vandermonde in the ordinate gaps), and a uniform modulus is equivalent to LP-143 (Prop. 143.E),
which GUE predicts **false**. §3's zero profile is the window version of the same statement: `λ(T)` is set by
`|F̂(γ_n)|²` over `γ ∈ [40,230]`.

Prime-computable? **One thing only:** the rate formula of §5.1. Every term (`g_Γ'`, `w_n log n`, `c_F'(log n)`,
the multipliers) comes from Gamma and the primes `n < e^{2T}`, with no zero data, and reproduces `dλ/dT` to five
digits. No *bound* on it is: the `10⁵` cancellation means the prime-side expression is a difference of `O(1)`
quantities whose smallness is the arithmetic content. **The sign is prime-computable pointwise and not
prime-boundable.**

## 7. Verdict table

| # | Statement | Label |
|---|---|---|
| 1 | Pipeline reproduces R153_008's `λ` at `log 2` (`K = 160/240`) to all printed digits; explicit formula `Σ_γ|F̂(γ)|²/⟨A_TF,F⟩ = 0.997` independently | `DIAGNOSTIC-NUMERIC` (validation) |
| 2 | `λ(T)` table, `[0.30, log 2]`, 14 values, `K = 160/240/320`, 4 Galerkin digits / 2 true digits; minimiser **even** at every `T` | `DIAGNOSTIC-NUMERIC` (new) |
| 3 | `c(T)` sweeps `5 → 93` with kinks at `½log2, ½log3` and a terminal fall to `75.8`; **no plateau, no single-exponential law** | `DIAGNOSTIC-NUMERIC` (new) |
| 4 | (P-Slepian) `c → 2γ_1 ≈ 28.3` | **`REFUTED`** (factor 2.8, wrong monotonicity) |
| 5 | Mechanism of 4: the minimiser annihilates the first ~20 zeros; Weil mass median at `γ ≈ 65`, 90 % below `γ ≈ 229`; effective edge `Ω_eff ≈ c/2 ≈ 38–46`, increasing in `T` | `DIAGNOSTIC-NUMERIC` (new) |
| 6 | **Theorem 4.1**: `A_T^{(a)} = 2A_T + a²D_T + O(a⁴)`, `D_T = ad_t²(A_T) = −g_T''(D)`; primes `×(log n)²` sign-reversed, archimedean `−g_Γ''`, **no polar term in the operator** — the polar/moment content is the degeneration `P_T^{(a)} → P_T^{(2)}` (codim 4) | `PROVED` (new) |
| 7 | `2μ(T*)+a²q_D(T*)=0` reproduces `T*(a)` to 5 decimals for `a ≤ 0.01` | `DIAGNOSTIC-NUMERIC` (new) |
| 8 | (P-Xi) `c ≈ 75` | **`CONFIRMED`**, but as `c_μ` on `[0.69,0.81]` (codim-4 space), `= 79.3` measured, predicted slope `0.0262` vs fitted `0.0268` |
| 9 | Resolution of 28 vs 75: **different extremal problems**. 75 is right for `μ` on `[0.69,0.81]`; 28 is wrong everywhere; `λ` on `[0.30,log 2]` has no constant rate at all | `DIAGNOSTIC-NUMERIC` + `PROVED` (via 6) |
| 10 | Rate formula `dλ/dT = −(1/T)(1/2π)∫τg'|F̂|² + `Tate drift, verified to 4–5 digits; no rank-two term between thresholds | `PROVED` (elementary) + `DIAGNOSTIC-NUMERIC` (verification) |
| 11 | The rate is a `10⁵`–`10⁶` cancellation between `O(1)` Gamma and transport terms ⇒ **no term-by-term bound on `c`** | `DIAGNOSTIC-NUMERIC` (new; confirms D.133) |
| 12 | `F_T(±T)=0`, effective `α ≈ 1.25` (`T=0.60`) / `2.16` (`log 2`), `K`-stable to 3 digits; no jump (`|A| < 5·10⁻⁴`) ⇒ D.133's rank-two endpoint form vanishes at the minimiser | `DIAGNOSTIC-NUMERIC` (new) |
| 13 | D.133's obstruction is **not** bypassed: unboundedness of `F↦F(±T)` on the log-Sobolev form domain is untouched by a property of one vector | `RESTATEMENT` of D.133 |
| 14 | `c(T) ≤ c_0` uniformly = RH with a modulus; zero-computable (Doc 143 §4.4), and by §3 our window agrees; only the *rate formula* is prime-computable, and it is not prime-boundable | `RESTATEMENT` + `DIAGNOSTIC` |
| 15 | Blueprint's `O(1/K)` Galerkin drift explained by the `1/Ω_eff` boundary layer | `DIAGNOSTIC` |

**FATAL rule.** No zero-free region, no moment bound, no cancellation imported from any known theorem. Zero
ordinates appear in one place (§3) and only *diagnostically*; no result depends on them. Two of the three
blueprint predictions were expected to agree and do not; the survivor (75) survives *relabelled*. **No sign is
claimed for `ζ` at any `T > log 2`**: everything in §4 about `T ∈ (log 2, 0.86]` concerns `Ξ_a` and `μ`.

## 8. Open

| id | statement | label |
|---|---|---|
| (P153.11) | Prove `c_μ` and `c` are finite and increasing; is `Ω_eff(T)` asymptotically `≍ ` the ordinate of the `N(T)`-th zero, `N(T) ≍ T·`(something)? A derivation would give the true law replacing "`e^{−2γ_1T}`" | `OPEN` |
| (P153.12) | The multi-null Slepian problem: `min{Σ_γ|F̂(γ)|² : supp F ⊂ (−T,T), F ∈ P_T}` — asymptotics as `T→∞` with the zero density `log(τ/2π)/2π`. This is the correct extremal problem and the corpus has never posed it | `OPEN` (new) |
| (P153.13) | The boundary exponent `α(T)`: is it really `T`-dependent, or is `α = 1` with a `1/Ω_eff`-layer that our `K` cannot resolve? Needs `K ≳ 10³` or an endpoint-adapted basis | `OPEN` |
| (P153.14) | Certify `q_D(T) < 0` on `[0.69,0.86]` (interval arithmetic on `−g_Γ''` against the `(log n)²`-primes): this would make "`T*(a)` exists and is finite for every `a ∈ (0,½)`" a theorem via Theorem 4.1 | `OPEN` (tractable) |
| (P153.15) | Is the terminal fall of `c(T)` (`92.8` at `0.689` → `75.8` at `log 2`) a precursor of the `n = 4` threshold? If thresholds *decelerate* the decay, that is a structural reason to expect positivity past `log 2` | `OPEN` (speculative) |
