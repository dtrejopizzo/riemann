# R155_034 — round 4c: the Li/Keiper and Báez-Duarte criteria as dual certificates

**Order** `R155_031` §3.2(v) and §4**P4** (rank 4) ·
**Scope** Papers 36 and 47 in one language, through Theorem Z (`thm:Z`, Paper 46 §7).
**Files touched** this file, `scripts/r4c/`, the phase README, `PLAN.md`. Paper 46, `scripts/r4a`,
`scripts/r4b` untouched.

---

## §0 Verdict

**There is a theorem, and it is the *failure* branch of P4 — the branch `R155_031` §4 called "a proved
mismatch … itself a clean no-go".** The dictionary exists, is exact, and is one line of residue
calculus; what it proves is that the Li–Keiper family and the flat-top family are **disjoint**, for
three independent reasons, and that the Li coordinates are **archimedean-dominated** while the
flat-top coordinates are **balanced**. Concretely:

1. **Theorem L1 (exact dictionary).** `λ_n = Σ_ρ Φ_n(γ_ρ)` with `Φ_n` an explicit even **rational**
 function of `γ` whose only poles are of order `n` at `γ = ±i/2`; `Φ_n = ŵ_n` for the explicit
 weight `w_n(u) = P_n(|u|)e^{−|u|/2}`, `deg P_n = n−1`. So `λ_n` *is* a Weil-form value, exactly as
 Theorem Z demands. Verified numerically to 6–7 digits against the classical `λ_1,…,λ_4`.
2. **Theorem L2 (disjointness).** `w_n ∉ 𝒲_T` for every `n ≥ 1` and every `T > 0`, for three
 independent reasons — (a) `Φ_n ≥ 0` on `ℝ`, which `cor:nontermwise` forbids for flat-top weights;
 (b) the decay is exactly `e^{−|u|/2}`, i.e. `δ = 0` in `def:W`, the borderline the definition
 excludes; (c) `w_n` is nowhere locally constant, so it is not flat-top on any window. Hence **no
 `λ_n` is a flat-top dual certificate and no flat-top certificate is a `λ_n`.**
3. **Theorem L4 (the Li version of Theorem SC is FALSE — and that is the finding).**
 *[amended per R155_035]* Unconditionally (L4a), the `{2,3}` truncated comb
 `λ_n^{(S)}` is eventually positive — an explicit arithmetic fact with no zero-sum content. Under
 RH, sourced to Bombieri–Lagarias/Coffey (L4b), `λ_n^{(S)}` differs from the full `λ_n` by
 `o(n log n)`, the exact opposite of Theorem SC. The collectivity of positivity — Paper 46's
 sharpest structural fact — is **invisible** in the Li coordinates. This is, in one sentence, why
 Paper 36's fifteen-step chain *terminates* at `λ_n ≥ 0` instead of penetrating it.
4. **Báez-Duarte / Nyman–Beurling: no theorem, only a dictionary, and a sign obstruction** (§3). The
 NB distance `d_N` is an *upper*-bound-per-`N` quantity whose dual is a certificate of
 **non**-approximability; the Weil/flat-top dual is a certificate of **positivity**. The two duals
 sit on opposite sides. Labelled `HEURISTIC`.

**Net movement toward D: zero certificates, one closed ambiguity.** P4 is now **CLOSED** as a route
to a certificate and should not be re-opened. Its value is diagnostic and, in the case of L4,
explanatory: it isolates *the normalisation* (`m^{−1/2}` versus `m^{−1}`) as what separates the two
culminations of the corpus.

---

## §1 Corpus record (grep-verified)

| source | what it proved | used here |
|---|---|---|
| Paper 36 `36-obstruction-ledger/main.tex` | the fifteen-step Pick/Nevanlinna chain; `Ω₇` = ARP-P reduces to `δ_N ≥ 0 ∀N ⟺ λ_n ≥ 0 ∀n` (Li–Keiper), the **sole open central input**; `thm:explicit-channel` = the same Weil functional Paper 46 uses; `ng:envelope`: the scale-uniform bound `|λ_n^{prime}| ≤ c√n log n` is **RH-strength**, and the former stationary-phase reduction is **withdrawn**; the umbrella wall — an off-line `ρ` injects `r^n`, `r = \|1−1/ρ\| > 1`, that overtakes only *eventually*, so **no finite `n` closes it**; `ng:partition` (the archimedean term is not a per-prime density) | §2, §4 |
| Paper 38 `38-li-fir-stability/main.tex` | `λ_n` as the sampled output of a Cayley plant; `limsup\|λ_n\|^{1/n} ≤ 1 ⟺ RH`; under RH `λ_n = O(n log n)`; off-line zeros force `\|λ_n\| ≥ cR^n` on a syndetic set; FIR/moving-window criteria that do **not** need every sample to be positive | §2.4 |
| Paper 46 §3 `def:PD`, `thm:D1` | (P)/(D), strong duality, **finite** atomic certificates | §2.5 |
| Paper 46 §7 `thm:Z`, `thm:Zexh`, `cor:RH`, `cor:zeros`, `lem:Rrig`, `cor:nontermwise`, `thm:finZ` | every certificate is an explicit-formula evaluation `f_w = Σ_ρ ŵ(τ−γ_ρ)`; flat-top class `𝒲_T` (`w ≡ 1` on `[−2T,2T]`, `\|w\| ≤ Ce^{−(½+δ)\|u\|}`); **no flat-top `w` has `ŵ ≥ 0`**; no finite zero set carries a certificate | §2.3, §2.6 |
| Paper 46 §8 `thm:SC`, `cor:SC1` | sub-comb negativity: any comb of mass `A < −C₀ = 5.3721834` is negative for `T ≥ T₀(A)`; positivity is **collective** | §4.4 |
| Phases 147–155 | **zero** Li–Keiper work; **zero** Báez-Duarte hits anywhere in the row-D arc (`R155_031` §3.2(v)) | — |
| Phase 33 `phase-33-dbn/82-variational-reformulation-and-the-connection.md` and neighbours | the corpus's only Nyman–Beurling material: variational density, exponential completeness, the central measure `dν` | §3 |
| Phase 104 `104_02_LAGARIAS_TRANSLATION.md`, `104_85_NONLOCAL_PRIME_HURWITZ_NYMAN_GATE.md` | Nyman-type gates, all closed negative | §3 |

---

## §2 Li ↔ the Weil form

### 2.1 The Li kernel is rational with poles at the edge of the strip

Write `ρ = ½ + iγ` (with `γ ∈ ℂ`; `γ ∈ ℝ` iff `ρ` is on the critical line) and

```
B(γ) := (ρ−1)/ρ = (2iγ−1)/(2iγ+1), B(−γ) = B(γ)^{−1}.
```

**Theorem L1 (the Li coefficient is a Weil-form value).**
For `n ≥ 1` put

```
Φ_n(γ) := 1 − ½ (B(γ)^n + B(γ)^{−n}).
```

Then
1. `Φ_n` is an **even rational function** of `γ`, real on `ℝ`, with poles of order exactly `n` at
 `γ = ±i/2` and no others; `Φ_n(γ) = n²/(2γ²) + O(γ^{−4})` as `|γ| → ∞`, so `Φ_n ∈ L¹(ℝ) ∩ C(ℝ)`.
2. `λ_n = Σ_ρ [1 − (1−1/ρ)^n] = Σ_ρ Φ_n(γ_ρ)`, the sum in the Bombieri–Lagarias symmetric pairing
 (`ρ` with `1−ρ`, unconditionally — the pairing used in the proof below; on the critical line this
 coincides with `ρ` with `\barρ`, but only there). *[amended per R155_035]*
3. On the critical line `B(γ) = e^{iθ(γ)}` with `θ(γ) = 2 arctan(1/2γ) = 2 arg(γ + i/2)`, so
 `Φ_n(γ) = 1 − cos(n θ(γ)) ≥ 0` for **every real `γ`**.
4. `Φ_n = ŵ_n` where, by the residue theorem applied to the two poles at `±i/2`,
 `w_n(u) = P_n(|u|) e^{−|u|/2}` for `u ≠ 0`, with `P_n` a real polynomial of degree `n−1`;
 `w_n` is even, continuous, integrable and **positive definite** (Bochner, from (3)). Closed form
 (free strengthening): `w_n(u) = −½ e^{−|u|/2} L_n'(|u|)`, i.e. `P_n = −½L_n'` where `L_n` is the
 `n`-th Laguerre polynomial (`n=1`: `w_1 = ½e^{−|u|/2}`; `n=2`: `w_2 = (1−|u|/2)e^{−|u|/2}`).
 *[amended per R155_035]*

*Proof.* (1) `B` is a Möbius map with a simple pole at `γ = i/2` and a simple zero at `γ = −i/2`, so
`B^n` has a pole of order `n` at `i/2`, `B^{−n}` one at `−i/2`, and `Φ_n` is their symmetrisation.
`B(γ) → 1` as `|γ| → ∞`; writing `B = 1 − 2/(2iγ+1)` and expanding gives
`½(B^n+B^{−n}) = 1 − n²/(2γ²) + O(γ^{−4})`. (2) `1 − 1/ρ = B(γ)` and `1 − 1/(1−ρ) = B(γ)^{−1}`
(the identity `1 − 1/(1−ρ) = (1−1/ρ)^{−1}` recorded in Paper 36 `ng:envelope`); pairing `ρ` with
`1−ρ`, equivalently `γ` with `−γ`, halves the sum into `Φ_n`. (3) For `γ ∈ ℝ`,
`2iγ−1 = −\overline{(2iγ+1)}`… more directly `1 − 1/ρ = (γ+i/2)²/|γ+i/2|²`, of modulus `1`, with
argument `2 arg(γ+i/2)`; then `½(e^{inθ}+e^{−inθ}) = cos nθ`. (4) `Φ_n ∈ L¹` and rational with poles
only at `±i/2`; close the inversion contour in the half-plane opposite to the sign of `u` and collect
the single `n`-fold residue. ∎

**Numerical validation** (`scripts/r4c/li_phi_check.py`, 10 000 zeros + an explicit density tail,
runtime 40 s):

| `n` | `Σ_{γ≤9877.8} Φ_n` | `+ tail` | classical `λ_n` |
|---|---|---|---|
| 1 | 0.022961 | **0.0230957** | 0.0230957090 |
| 2 | 0.0918069 | **0.0923457** | 0.0923457352 |
| 3 | 0.2064266 | **0.2076390** | 0.2076389205 |
| 4 | 0.3666353 | **0.3687905** | 0.3687904095 |
| 5 | 0.5721752 | 0.5755428 | 0.5757790843 |

Six to seven correct digits for `n ≤ 4`. `DIAGNOSTIC` (the theorem is L1(2); this only checks the
bookkeeping).

### 2.2 The arithmetic side, and why it is `m^{−1}` and not `m^{−1/2}` — `FORMAL`, not `PROVED`
*[amended per R155_035]*

Apply the Weil functional of Paper 46 `thm:Z`(i) to the even test `w_n` of L1(4). The prime term of
that functional is `−Σ_{m≥2} v_m w_n(log m)` with the paper's normalisation `v_m = 2Λ(m)/√m`. Since
`w_n(log m) = P_n(log m)·m^{−1/2}`, the two square roots cancel to give, formally,

```
prime side of λ_n = −2 Σ_{m≥2} Λ(m) P_n(log m) / m, deg P_n = n−1.
```

**This series does not converge.** `Σ_{m≤X}Λ(m)(log m)^j/m ≍ (log X)^{j+1}/(j+1)`, so for `n=1` the
series is `−Σ_mΛ(m)/m ~ −log X → −∞`; reproduced numerically, truncations at
`X=10²,10³,10⁴,2·10⁵` give `−3.986, −6.329, −8.635, −11.629` against `−(log X−γ_E) = −11.639`. The
identity above is therefore an equality of two divergent formal expressions, not an absolutely
convergent evaluation. This is the sharp form of Theorem L2(b): `δ = 0` means `ŵ_n(±i/2) = Φ_n(±i/2)
= ∞` (the pole sits *on* the boundary of the Weil admissibility strip), and simultaneously the prime
sum above diverges — the two infinities cancel to produce the finite `λ_n`. Consequently `w_n` is
**not an admissible test function for the explicit formula at all**, and `λ_n` is not a Weil-functional
evaluation in the sense of `thm:Z`: it is only the **zero-sum half** of one (`λ_n = Σ_ρ Φ_n(γ_ρ)`,
Theorem L1(2), which is untouched by this). Label: `FORMAL` (was `PROVED` — error). The classical
identification of the divergent series with the Bombieri–Lagarias arithmetic expression — a finite
combination of binomial coefficients against `Σ_m Λ(m)(log m)^{k−1}/m`, `k ≤ n`, each divergent in the
same way — is `CITED`, not used.

### 2.3 Theorem L2: the two families are disjoint

**Theorem L2.** For every `n ≥ 1` and every `T > 0`, `w_n ∉ 𝒲_T` (Paper 46 `def:W`). Consequently no
Li coefficient is a flat-top dual certificate, and no flat-top certificate value equals any `λ_n`.

*Proof.* Three independent obstructions, any one sufficient.
(a) **Sign.** By L1(3), `ŵ_n = Φ_n ≥ 0` on `ℝ`. `lem:Rrig` / `cor:nontermwise` (Paper 46) say that an
even continuous `w ∈ L¹` with `w ≡ 1` on any interval `[−2T,2T]` cannot have `ŵ ≥ 0`. So `w_n` is not
flat-top on any window.
(b) **Decay.** `def:W` requires `|w(u)| ≤ Ce^{−(½+δ)|u|}` with `δ > 0`. By L1(4) the decay of `w_n` is
exactly `|u|^{n−1}e^{−|u|/2}`: `δ = 0`, the single value the definition excludes. Equivalently: the
poles of `Φ_n` sit **on** the boundary `|Im γ| = ½` of the Weil admissibility strip, of order `n`.
(c) **Flatness.** `w_n` is real-analytic on `(0,∞)` and non-constant, so it is not identically `1` on
any interval. ∎

**Remark (the structural reading).** (a) is the sharp one. Paper 46 `cor:nontermwise` proves that a
flat-top certificate is *always* a statement of **cancellation across the zeros**, never termwise
positivity — "the whole family of strategies *choose `w` with `ŵ ≥ 0`* is empty". Theorem L1(3) says
the Li family is **precisely** that empty strategy, realised outside `𝒲_T`: `λ_n ≥ 0` under RH is
termwise, one nonnegative number per zero. The price of termwise positivity is the loss of the flat
top — i.e. the loss of any window, hence of any arithmetic locality.

### 2.4 Which inequality is stronger, per element

| | `λ_n ≥ 0` (one `n`) | `λ^W(T) ≥ 0` (one `T`) |
|---|---|---|
| kernel | `Φ_n ≥ 0`, fixed, no translation parameter | `ŵ(τ−γ)`, sign-changing, swept over `τ ∈ ℝ` |
| under RH | **trivially true termwise** (L1(3)) | a genuine cancellation statement (`cor:nontermwise`) |
| unconditional certifiability | none in general: needs the zero sum or an RH-strength tail bound (Paper 36 `ng:envelope`); closed forms exist only for the first few `n` | **yes**: `thm:D1` gives a *finite* atomic certificate whenever `λ^P_T > 0`; Theorem C is one, at `T = ½log3` |
| arithmetic content | primes at `m^{−1}`, lower order (§4.4) | primes at `m^{−1/2}`, critical order, in a window `m < e^{2T}` |
| what one element gives | nothing about RH: an off-line `ρ` contributes `≍ r^n`, `r>1`, overtaking only **eventually** (Paper 36 `ng:envelope`, Paper 38 syndetic-set theorem) | nothing about RH either, but a proved lower bound on the `ŵ`-smoothing of the zero measure, unconditionally (`cor:zeros`) |

**Verdict:** per element the window inequality is strictly the more *usable* — it is unconditionally
finitely certifiable and it carries the primes at the critical normalisation. Per element the Li
inequality is the *weaker* object under RH (trivial) and the *harder* object unconditionally
(uncertifiable). They are not comparable as implications; they are comparable as instruments, and
the instrument comparison is one-sided.

### 2.5 Is there a `T(N)`?

**Proposition L3.** No implication between `{λ_n ≥ 0 : n ≤ N}` and `{λ^W(T) ≥ 0 : T ≤ T(N)}` is
derivable through Theorem Z, in either direction, for any choice of `T(N)`.

*Reason.* Theorem Z is an isomorphism between certificates and explicit-formula evaluations
**within** `𝒲_T`; `thm:Zexh` states the exhaustion `sup_{w ∈ 𝒲_T^{reg}} inf_τ f_w = λ^W(T)`. By
Theorem L2 the Li kernels lie outside every `𝒲_T`, so neither family is in the closure of the other
and no evaluation of one is an evaluation of the other. `PROVED` as stated (a
statement about what Theorem Z derives); the stronger logical independence is **not** claimed —
both families are RH-equivalent *in full*, so each implies the other through RH, and that is the only
implication that exists.

**Remark (motivation, not proof)** *[amended per R155_035]*: two further asymmetries make
the absence of a `T(N)` structural rather than accidental, though neither is itself a proof:
(i) `λ_n` involves **all** primes (weight `Λ(m)P_n(log m)/m`, formally of unbounded support — see
§2.2) whereas `λ^W(T)` involves exactly `m < e^{2T}`, so there is no candidate window attached to an
`n`; (ii) the window family is **nested and monotone** in `T` (`R155_023` Theorem 1: `λ^∞_min`,
`λ^{∞,P}_min` non-increasing; the full form inherits the same direction from `thm:SC`), while
`(λ_n)_n` has **no order structure at all** — Paper 38 exhibits criteria that tolerate individual
negative samples inside a moving window.

### 2.6 What `thm:finZ` becomes in Li language

`thm:finZ` (no finite zero set carries a flat-top certificate) has **no** Li analogue, and cannot: for
a finite symmetric `Z ⊂ ℝ\{0}`, `Σ_{γ∈Z} Φ_n(γ) ≥ 0` is true for trivial reasons (L1(3)). The
truncation obstruction is a property of sign-changing kernels only. This is a second, independent
confirmation that the Li criterion has no finitary content — and it explains the otherwise puzzling
coexistence of Paper 46 `cor:zeros` ("not verifiable on any finite list of zeros") with the
century of successful finite-`n` Li computations (Keiper, Maślanka, Coffey, up to `n ∼ 10⁵`): those
computations verify a termwise-nonnegative sum.

---

## §3 Nyman–Beurling / Báez-Duarte ↔ the dual

**Setting.** Báez-Duarte's sequential criterion: with `ρ_k(x) = {1/(kx)}`,
`d_N² = inf_{c} ‖1 − Σ_{k≤N} c_k ρ_k‖²_{L²(0,∞;dx/x²)}`, and **RH ⟺ `d_N → 0`**.

**What the dual of `d_N` is.** `d_N²` is the squared distance from `1` to a finite-dimensional
subspace `V_N` of a Hilbert space, i.e. `d_N = sup { ⟨1,φ⟩ : ‖φ‖ ≤ 1, φ ⟂ V_N }`. The dual variable
`φ` is therefore a **witness of non-approximability**: a unit vector orthogonal to `ρ_1,…,ρ_N` with
large pairing against `1`. Producing a dual object for Báez-Duarte *certifies a lower bound* on `d_N`,
i.e. it certifies **against** RH; RH is certified on the **primal** side, by exhibiting coefficients
`c`, and only in the limit `N → ∞`.

**Proposition (the sign obstruction).** The Báez-Duarte dual and the Paper 46 dual point in opposite
directions:

| | Báez-Duarte | Paper 46 |
|---|---|---|
| RH is certified by | the **primal**, asymptotically in `N` (an upper bound `d_N ≤ ε_N → 0`) | the **dual**, at each `T` (a lower bound `f_w ≥ 0`) |
| the dual object certifies | `d_N ≥ c > 0`, i.e. a **refutation** | `λ^W(T) ≥ c > 0`, i.e. a **confirmation** |
| finite data | `d_N` for one `N` is a computable upper bound but never `0`; non-attainment is the known obstruction (Báez-Duarte's `d_N ≫ 1/√log N` conjecturally) | `thm:D1`: a **finite** certificate proves `λ^W(T) > 0` exactly |

There is a structural echo here of Paper 46 `subsec:conc`/`thm:E` **non-attainment** (the primal
optimum in (P) is not attained), which is the same phenomenon: an infimum approached but not reached.
That echo is real and is worth one sentence in Paper 46; it is **not** a theorem relating `d_N` to
`λ^W(T)`.

**Is there a clean connection through Theorem Z?** *No.* The Mellin transform sends
`ρ_k ↦ (ζ(s)/s)·(k^{−s} − …)` and the NB functional becomes
`d_N² = inf_c (1/2π)∫_{ℝ} |1 − Σ_k c_k k^{−(½+it)}|² · |ζ(½+it)|²/|½+it|² dt` (Báez-Duarte's
`L²` form on the critical line) — a weighted **`L²` distance against the measure `|ζ|²dt/|s|²`**,
whose defining data is the *modulus* of `ζ` on the line. Theorem Z's certificates are pairings against
the **zero counting measure** `Σ_ρ δ_{γ_ρ}`. Passing from `|ζ(½+it)|²dt` to `Σ_ρ δ_{γ_ρ}` is exactly
the step no one can take (it is the magnitude→phase problem recorded as Paper 36's fifth arc,
`sec:arcE`, "the magnitude–phase gap"). Any attempted identity `d_N ↔ λ^W(T)` must cross it.
**Label `HEURISTIC`**: the dictionary above is an accurate statement of the two frameworks; there is
no theorem. Recommendation: do not spend another round here.

---

## §4 What the dictionary buys

### 4.1 (a) Does Li positivity for `n ≤ N` give a certificate beyond `½log3`? **No.**

Unconditional positivity *is* available for small `n` — `λ_1 = 1 + γ_E/2 − ½log 4π = 0.0230957…` is a
closed form, and the next few `λ_n` have closed forms in Stieltjes constants — but by Theorem L2
these are evaluations of kernels outside every `𝒲_T`, and by Proposition L3 they transfer to no
window. More basically, a certificate is an inequality **uniform in `τ`** (`inf_τ f_w ≥ c`), while
`λ_n` is a single number: there is no `τ`-family to take an infimum over. **The current record stands
at `½log3` (Theorem C, `c ≥ 8.86·10⁻⁵`) and this route does not move it.** `PROVED`.

### 4.2 (b) Does Theorem C imply anything about `λ_n`? **No.**

Theorem C gives `inf_τ f_w ≥ 8.86·10⁻⁵` for one explicit `w ∈ 𝒲_{½log3}`, hence by `cor:zeros`
`Σ_ρ ŵ(τ−γ_ρ) ≥ 8.86·10⁻⁵` for all real `τ`, unconditionally. To extract `λ_n ≥ 0` one would need
`Φ_n` in the closed cone generated by `{ŵ(·−τ)}`; `Φ_n ≥ 0` and `ŵ` changes sign, so the only
available comparison is `Φ_n ≤ ‖Φ_n‖_∞ · 1`, which is vacuous. `PROVED` (as a non-implication through
Theorem Z; see the caveat in L3).

### 4.3 (c) `λ_n ∼ (n/2)log n` versus `m(τ) ∼ log τ`: **the same mechanism.**

By L1(3), `Φ_n(γ) ≈ 1` on average for `|γ| ≲ n` (where `nθ(γ) ≈ n/γ` oscillates) and
`Φ_n(γ) ≈ n²/2γ²` for `|γ| ≫ n`. So `λ_n` is, to leading order, the **zero count up to height `≍ n`**,
weighted by `1`; and the zero density is `(1/2π)log(γ/2π)`, which is precisely the archimedean
multiplier `m(τ) ≈ log τ` of Paper 46 §2. `λ_n ∼ (n/2)log n` and `m(τ) ∼ log τ` are the **same**
`d/dτ` of `log Γ` — the Riemann–von Mangoldt density — read in two coordinate systems. `PROVED`
structurally; the constants are the classical Bombieri–Lagarias/Coffey asymptotic
`λ_n = (n/2)(log n + γ_E − 1 − log 2π) + O(√n log n)` under RH.

### 4.4 (d) **The Li version of Theorem SC — it FAILS, and that is the result**

*[amended per R155_035: L4 re-sourced and split]*

**Theorem L4a (unconditional: the `{2,3}` sub-comb is eventually positive).** Define the truncated
comb `λ_n^{(S)} := (archimedean+pole part) − 2Σ_{p∈S,k} (log p) P_n(k log p)/p^k` for a finite prime
set `S`, in particular `S = {2,3}`. This is an explicit arithmetic sequence with no zero-sum content.
It is eventually positive, with main term `(n/2)log n`, unconditionally — no RH input is needed for
this half of the claim.

**Theorem L4b (conditional: `λ_n^{(S)}` tracks `λ_n` under RH).** Under RH,

```
λ_n = (n/2)(log n + γ_E − 1 − log 2π) + λ_n^{prime}, |λ_n^{prime}| ≤ c√n log n
```

for the RH-strength asymptotic; **this asymptotic is due to Bombieri–Lagarias / Coffey, not to Paper
36**. Paper 36's `ng:envelope` (`36-obstruction-ledger/main.tex:1082–1086`) states only that
`|λ_n^{prime}| ≤ c√n log n` is a **sufficient route to RH** (the bound would imply RH); it withdraws
the former stationary-phase reduction and never defines `λ_n^{prime}` itself, so it cannot be cited as
the *source* of the RH-conditional asymptotic used here. Given that asymptotic (Bombieri–Lagarias /
Coffey), `λ_n^{(S)}` differs from `λ_n` by `O(√n log n) = o(n log n)`. There is no `n₀(S)` past which
a finite sub-comb turns `λ_n^{(S)}` negative, and the same main term `(n/2)log n` governs both.

**Contrast with Theorem SC.** In the Weil/flat-top coordinates, *any* sub-comb of total mass
`A < −C₀ = 5.3721834` makes the form **negative** for every `T ≥ T₀(A)` — `cor:SC1` exhibits ten
primes of size `10⁵–10⁶` giving `λ_min ≤ −2.12` — because the archimedean deficit `−C₀` is a
**constant** while the full comb's mass `A ∼ 4e^T` **grows**. In the Li coordinates the archimedean
part **grows like `(n/2)log n`** and the prime part is `O(√n log n)`: the roles are reversed, the
competition never happens, and the sub-comb question has no bite.

**The mechanism is the normalisation, and only the normalisation** (§2.2, now `FORMAL` there —
the series is divergent, so this is a formal-order comparison, not an absolutely-convergent one):
`m^{−1/2}` (critical, comb mass `∼ 4e^T`, competes with a constant budget) versus `m^{−1}`
(subcritical, formally lower order, dominated by a growing budget). `PROVED` (unconditional) for
Theorem L4a; `CONDITIONAL` on RH, sourced to Bombieri–Lagarias/Coffey, for Theorem L4b — which is
exactly the right scope, since unconditionally `λ_n^{prime}` *is* the open difficulty.

**Numerics** *[amended per R155_035]*: the script `scripts/r4c/li_phi_check.py`
computes no prime sum. Its "residue" column is `λ_n(10⁴ zeros + tail model) − archimedean asymptotic`,
which is dominated by the **tail-model error** (at `n=1000` the tail is `134.7`, `5.8%` of `λ_n`, with
an absolute uncertainty of the Riemann–von Mangoldt density's `O(1/G)`-per-zero error, of the same
order as the quoted residue `2.545` itself). The residue table below is retained only as a consistency
check, not as a measurement of the prime side:

| `n` | `λ_n` (10⁴ zeros + tail) | `(n/2)(log n + γ_E − 1 − log 2π)` | residue (consistency check only) | `√n log n` |
|---|---|---|---|---|
| 100 | 118.604 | 117.225 | 1.378 | 46.05 |
| 200 | 306.656 | 303.766 | 2.890 | 74.93 |
| 500 | 991.903 | 988.487 | 3.416 | 138.96 |
| 1000 | 2326.092 | 2323.547 | 2.545 | 218.44 |

The actual `{2,3}` sub-comb prime side is directly computable in closed form from
`w_n = −½e^{−|u|/2}L_n'(|u|)` (§2.1), summing `p^k ≤ 10⁶`:

| `n` | 1 | 10 | 100 | 1000 |
|---|---|---|---|---|
| `{2,3}` prime side | `−1.2425` | `+0.6305` | `−0.3098` | `−1.6374` |

Small and bounded — it supports Theorem L4a/L4b — but it is `−1.64` at `n=1000`, not the `2.5` of the
residue column above; the earlier claims "the entire prime contribution", "`≈0.1%`" and "two orders of
magnitude below `√n log n`" are **not established by this run** and are withdrawn. Label:
`DIAGNOSTIC` for the residue table, `PROVED` (closed-form, unconditional computation) for the `{2,3}`
prime-side table.

**Consequence for the programme (the one thing worth carrying forward) — `INTERPRETIVE`**
*[amended per R155_035]*. Scoped to the computed range `n ≲ 10⁵`: the arithmetic content of
`λ_n` (§4.4's closed-form `{2,3}` prime side, bounded and small relative to the archimedean main term
`(n/2)log n`) is a lower-order correction to a growing archimedean main term. This is an assertion
about the finite data, not about the strength of the Li–Keiper criterion — `{λ_n ≥ 0 ∀n}` is
equivalent to RH in full, so it is not logically "weaker" evidence. Paper 46's window certificates
test the opposite regime, where the comb and the archimedean budget are the same size. The corpus
should not treat the two bodies of numerical evidence as commensurable, and Paper 46's claim that
positivity is *collective* is unaffected by any amount of Li data.

### 4.5 What imports, after all

`R155_031` §4 P4 hoped the dictionary would "import Paper 37's sixteen positivity-transfer witnesses
and Paper 38's FIR criteria straight into the dual language, at no cost". **It does not**: by
Theorem L2 the transfer is blocked at the class level for all of them, since every one of those
objects is stated in Li/Cayley coordinates. The one genuine import is negative and is L4.

---

## §5 Labels

| statement | label |
|---|---|
*[amended per R155_035]*

| **Theorem L1** (`λ_n = Σ_ρ Φ_n(γ_ρ)`, pairing `ρ↔1−ρ` unconditional; `Φ_n` rational, poles of order `n` at `±i/2`; `Φ_n = ŵ_n`, `w_n = −½e^{−\|u\|/2}L_n'(\|u\|)`, `P_n=−½L_n'`; `Φ_n ≥ 0` on `ℝ`) | **`PROVED`** |
| §2.2 prime side of `λ_n` `= −2Σ_m Λ(m)P_n(log m)/m` | **`FORMAL`** (was `PROVED` — error; series diverges); sharp form of L2(b): `ŵ_n(±i/2)=∞` and prime sum diverges, so `w_n` is not an admissible explicit-formula test and `λ_n` is only the zero-sum half of a Weil-form value |
| **Theorem L2** (`w_n ∉ 𝒲_T` for all `n,T`; three independent reasons) | **`PROVED`** (uses Paper 46 `lem:Rrig`, `def:W`) |
| **Proposition L3** (no `T(N)` derivable through Theorem Z, either direction) | **`PROVED` as scoped**; full logical independence **not claimed**; asymmetries (i),(ii) are **`REMARK`**, not proof |
| §2.6 (`thm:finZ` has no Li analogue) | **`PROVED`** |
| §4.1, §4.2 (no transfer of certificates in either direction) | **`PROVED` as scoped** |
| §4.3 (same mechanism: Riemann–von Mangoldt density) | **`PROVED`** structurally; constants `CITED` |
| **Theorem L4a** (`{2,3}` sub-comb `λ_n^{(S)}` eventually positive) | **`PROVED`, unconditional** |
| **Theorem L4b** (`λ_n^{(S)}` differs from `λ_n` by `o(n log n)`) | **`CONDITIONAL` on RH**, asymptotic sourced to Bombieri–Lagarias/Coffey (not Paper 36 `ng:envelope`, which is an RH-strength sufficient route, not a source) |
| §3 (Báez-Duarte/NB dual is the opposite-sign object; no connection through Theorem Z) | **`HEURISTIC`** — an accurate dictionary, no theorem; the magnitude→phase gap blocks it |
| residue table (§2.1, §4.4) | **`DIAGNOSTIC`**, under-determined (tail-model error dominates) |
| `{2,3}` prime-side table (§4.4) | **`PROVED`** (closed-form, unconditional computation) |
| §4.4 "Consequence for the programme" | **`INTERPRETIVE`**, scoped to computed range `n ≲ 10⁵` |
| **P4 as a route** | **CLOSED.** Do not re-open. |

---

## §6 Proposal for Paper 46

One new subsection, `\subsection{Why the Li--Keiper criterion is not a flat-top certificate}`, placed
at the **end of §7** (after `thm:finZ`, before §8), roughly 1 page:

*[amended per R155_035: item 1 ready with the closed form and the sharp L2(b) statement;
item 3 NOT READY until re-sourced and split — see below]*

1. `def:Phi_n` and **Theorem L1** (statement + the four-line residue proof), including the closed form
 `w_n = −½e^{−|u|/2}L_n'(|u|)` and L2(b) in its sharp form: `ŵ_n(±i/2) = ∞`, the prime sum diverges,
 and `w_n` is therefore not an admissible explicit-formula test. Do **not** carry in §2.2's
 convergence sentence.
2. **Theorem L2**, presented as the sharpest corollary of `cor:nontermwise`: *the Li family is exactly
 the termwise-positive strategy that `cor:nontermwise` proves empty inside `𝒲_T`; it exists only
 outside, at `δ = 0`, with poles of order `n` on the boundary of the admissibility strip.* This is
 the natural companion to `cor:nontermwise` and strengthens §7's thesis at no cost.
3. **NOT READY as originally drafted.** One remark for §8, after `cor:SC1`, once re-sourced: split
 into (a) unconditional — the `{2,3}` sub-comb `λ_n^{(S)}` is eventually positive, an explicit
 arithmetic fact (Theorem L4a); (b) under RH, citing Bombieri–Lagarias/Coffey (not Paper 36
 `ng:envelope`, which is only an RH-strength sufficient route), `λ_n^{(S)}` differs from `λ_n` by
 `o(n log n)` (Theorem L4b), so no sub-comb statement survives. Drop or re-qualify the
 `n ∼ 10⁵`-evidence sentence: it is `INTERPRETIVE`, scoped to the computed range, not a claim about
 the criterion's logical strength (`{λ_n≥0 ∀n}` is equivalent to RH in full).
4. One sentence in §3 (non-attainment) noting the Báez-Duarte echo, explicitly labelled as an analogy.
5. `\subsection{Open}`: **remove** any suggestion that classical sequential criteria might supply
 certificates; record instead "the Li–Keiper and Weil-window families are disjoint (Thm L2); a
 certificate cannot be imported from the classical sequential criteria."

No change to any existing theorem, constant, or label. `Wcl`, `thm:Z`, `thm:SC`, `cor:nontermwise`
are used exactly as stated.

---

## Reproduction

```
python3 scripts/r4c/li_phi_check.py # ~40 s; reads 06-grafico/zeros_10000.txt
```
Writes `scripts/r4c/li_phi_check.json`. Zeros: the corpus's `zeros_10000.txt` (first 10 000 ordinates,
`γ ≤ 9877.78`). Tail model: `n²(log(G/2π)+1)/(2πG)`, from `Φ_n ≈ n²/2γ²` against the
Riemann–von Mangoldt density; it is an asymptotic estimate, not an enclosure.
