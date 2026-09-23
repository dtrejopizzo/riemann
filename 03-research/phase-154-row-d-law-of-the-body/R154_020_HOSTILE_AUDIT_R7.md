# R154.020 — Hostile audit, round 7 of phase 154

*Hostile auditor: Opus 5 (1M). 2026-09-21. Target: `R154_019_BUILDER_ROUND7.md` (orders `R154_018`).
Inputs re-read: `R154_007 §2.2`, `R154_010 §2`, `R154_012`, `R154_015 §5–6`, `R154_016`, `R154_017 §3–5`,
`R153_016 §2.4`, `scripts/round4/certificate/CERT_log3_M24.json`. Computation used: `mpmath` digamma at four
points, arithmetic, and two `numpy` least-squares slopes over the 437 archived decimals. No LP, no B&B.*

---

## 0. Verdict table

| item (builder's label) | audit verdict |
|---|---|
| **Theorem K**, constant `πN/(e·u_max)` — `PROVED` | **CONFIRMED, constant correct.** Full derivation in §1; the `π` is not an error (it is `π/2` from the mean of `\|\sinθ\|` times `2` from evenness). |
| Theorem K is a *rate theorem for `c(h,u_max)`* (implicit in §3.3, §7 "the rate theorem the round was asked for") | **REJECTED.** K bounds the **support radius of the relaxed minimiser**, and nothing else. It gives neither an upper nor a lower bound on `c`. See §2. |
| "`supp μ ⊆ [−τ_c,τ_c]` is a restrictive hypothesis; (P154.6) is the single technical gap" (§3.4) | **BOTH HALVES WRONG.** The hypothesis is **free at the minimiser** (Bauer + extreme points: §2.1 — a repair, offered). And (P154.6) is *not* the missing lemma; the missing lemma is a **mass ⟹ value** balance, whose gain is only logarithmic (§2.3). |
| **Corollary K1** — `PROVED` | **CONFIRMED as stated**, but its direction is the opposite of the one used downstream (§2.2). |
| calibration `M_crit(½log3) = 15.9` vs "measured LP sign crossing between `M=16` and `M=19`" | **FATAL CITATION ERROR.** Those three LP values are the ones `R154_010 §2` itself declares **fictitious** two lines later (true B&B minima `−7·10⁻³…−8·10⁻³`). No measured crossing of `c(M)` exists. §3. |
| "four independent data points, no fitted parameter" | **REJECTED.** One (dead) data point plus two one-sided consistency checks; and the two 0.58 points are `DIAGNOSTIC-NUMERIC` upper bounds with a 30 % solver disagreement on record (`R154_017 §4`). |
| deficit law `D ≳ λ_min(eτ₁/π)h`, `α = 1` | **NOT PROVED, and internally inconsistent** with §4.1, which prefers the *squared* law on the same single data point. Downgrade to `HEURISTIC`. §4. |
| `M_crit ∝ 2eTτ₁(T)/π`; `τ₁` the same for all `T ∈ (½log3, log2]`; arithmetic `15.92 / 59.76 / 71.42` | **CONFIRMED.** Re-derived independently (§3.1). `τ₁` depends on `T` only through the contact set: correct. |
| `M_crit` doubly exponential in `T` | **CONFIRMED** as a statement about `τ₁` (`R153_016 §2.4`), with the caveat of §3.2 (`τ₁` is the convex hull of the negative set, not its measure). |
| (R2) the off-lattice-`log 3` hypothesis **refuted** by the window identity (§2.2) | **CONFIRMED, and this is the round's cleanest result.** The atoms at `±log n` lie inside the window where `ν ≡ 0`; they cannot be a commensurability problem. |
| (R2) the `(3.75)² ≈ 15` squared scaling | **REJECTED as evidence**; it is a two-parameter reading of one ratio, and it contradicts §3.3's `α = 1`. |
| remedy: clustered atoms on `[2T,V]`, `175` columns at `log 2` | **DIRECTIONALLY RIGHT, arithmetic right, clause (c) rightly unproved.** But it is motivated by the converse of what K proves (§2.2), so it must be sold as a *heuristic* with a decisive falsifier. Falsifier specification accepted with amendments (§5). |
| **Proposition E** (identity) | **CONFIRMED** (trivially: `[T,∞)+[−T,T] = [0,∞)`). |
| Proposition E's "consequence": *no* analytic near-certificate of E-L type exists | **OVERREACH.** It refutes one algebraic route. The sub-claim "`F̂_★` has real zeros" is **asserted, not proved**. Downgrade to `DIAGNOSTIC`. §6. |
| **Proposition P** (`β₀ = 2` ⟺ polar terms restored) | **CONFIRMED, PROVED** (identity re-derived, §7). |
| (R4) `β₀^{opt} → 2` is `OPEN`, and `R154_012 §1` should be amended | **AGREED, and the amendment is required.** The recorded drift `2.00256 → 2.03996` is at *different `T`*, so it is not even evidence against the limit — the honest statement is "untested". §7. |
| §4.3 "`\|a_j\| ∼ u_j^{-1}`, same exponent as `½K(u) ∼ 1/(2u)`" | **REJECTED — numerology.** Recomputed: global slope `−1.066`, but first-half slope `−0.243`, second-half slope `−3.688`. There is no power law. The *qualitative* fact (mass at the window edge: 23.8 % of `‖a‖₁` in the first 10 % of the `u`-range) survives and is enough for §4.2. |
| literature placement | **Mostly sound; three arXiv IDs unverified.** §8. |
| FATAL rule / no sign | **CLEAN.** Nothing above `log 2`, nothing certified, Theorem R5a remains the endpoint of record. |

---

## 1. The settled constant (full derivation) — **the builder is right**

> **Theorem K.** `μ` even Borel probability on `R`, `supp μ ⊆ [−τ_c,τ_c]`, `μ̌(u) = ∫\cos(uτ)dμ(τ)` vanishing at
> `N` distinct points `0 < u_1 < … < u_N ≤ u_max`. Then `τ_c ≥ πN/(e·u_max)`.

*Derivation, step by step, with the constant tracked.* Let `Λ(z) = ∫\cos(zτ)dμ(τ)`.

1. `Λ` is entire, even, `Λ(0) = μ(R) = 1 ≠ 0` (Jensen is applicable).
2. **Type.** `|\cos(zτ)| ≤ e^{|τ||\Im z|} ≤ e^{τ_c|\Im z|}` for `|τ| ≤ τ_c`, so
   **`|Λ(z)| ≤ e^{τ_c|\Im z|}`** — the bound is in `|\Im z|`, *not* in `|z|`. This is where the audit's own
   suspicion ("`|f(z)| ≤ e^{σ|z|}` gives `n(r) ≤ eσr`, without the `π`") breaks down: that cruder hypothesis
   ignores that `Λ` is bounded by `1` on the real axis.
3. **Jensen.** `∫_0^R n(t)t^{-1}dt = (2π)^{-1}∫_0^{2π}\log|Λ(Re^{iθ})|dθ − \log|Λ(0)|`.
4. **Right side.** `\log|Λ(Re^{iθ})| ≤ τ_cR|\sinθ|` and `(2π)^{-1}∫_0^{2π}|\sinθ|dθ = 2/π`, so the right side is
   `≤ (2/π)τ_cR`. **This is the factor `π/2` the crude estimate loses.**
5. **Left side.** `Λ(±u_i) = 0` by evenness ⟹ `n(u_max) ≥ 2N`. **This is the factor `2`.** With `n` nondecreasing,
   `∫_0^R n/t\,dt ≥ n(u_max)\log(R/u_max) ≥ 2N\log(R/u_max)` for `R > u_max`.
6. `2N\log(R/u_max) ≤ (2/π)τ_cR` for all `R > u_max`; the right side over the left is minimised at `R = e·u_max`
   (`\log(R/u_max) = 1`), giving `2N ≤ (2/π)τ_c·e·u_max`, i.e. **`τ_c ≥ πN/(e·u_max)`**. ∎

**Settled: the constant is `π/e`, and `π = (π/2)·2` is accounted for exactly.** `M_crit` is *not* off by `π`.

**On the slack (builder's open item 4 — sharper than he thinks).** `|Λ| ≤ 1` on `R`, so `Λ` is automatically in the
**Cartwright class**, and Levinson's theorem gives `n(r)/r → 2τ_c/π`. Hence *asymptotically in `u_max`*
`τ_c ≥ πN/u_max + o(1)`: the factor `e` is pure Jensen slack and the **sharp density constant is `1`, not `1/e`**.
Consequence for the round's headline: `M_crit(\log 2)` is somewhere in `[26, 71]`, not `71`. Any budget claim is
an order-of-magnitude claim; it must be written as such.

---

## 2. What Theorem K does and does not prove

### 2.1 Repair (offered, `PROVED`): the compact-support hypothesis is free at the minimiser

The feasible set of (REL) is convex, weak-\* closed, and **tight** (`σ_T(τ) ≥ m(τ) − Σv_n → ∞`, so a minimising
sequence cannot leak mass to infinity), hence weak-\* compact; `μ ↦ ∫σ_Tdμ` is affine and lower semicontinuous.
By **Bauer's minimum principle** the infimum is attained at an **extreme point**, and the extreme points of
`{μ ≥ 0 : μ(R)=1,` `N+2` further linear equalities`}` are atomic with at most `N+3` atoms. So:

> **Corollary K0 (`PROVED`).** `c(h,u_max;T)` is attained by an atomic `μ_★` with `≤ N+3` atoms; in particular
> `supp μ_★` is compact and Theorem K applies to it **unconditionally**:
> **the relaxed minimiser must place an atom beyond `πN/(e·u_max)`.**

This is a clean, correct, new statement — and it is the *whole* of Theorem K's force.

### 2.2 The direction problem (binding)

`c < 0` requires a feasible `μ` with `∫σ_Tdμ < 0`, i.e. **mass** in `{σ_T < 0} ⊆ (−τ₁,τ₁)`. Corollary K1 forbids
`supp μ ⊆ [−τ₁,τ₁]` once `N > N_crit`. **Support is not mass.** A feasible `μ` may satisfy K by putting `10⁻⁹`
of its mass at `τ = 10³` and everything else inside the negative set; its value is unchanged to nine digits.
Therefore:

* K1 **does not** imply `c ≥ 0` for `N > N_crit`;
* K1 **does not** imply `c < 0` for `N < N_crit` (it asserts no existence of anything);
* so `M_crit` is a threshold for **no** quantity that has been defined. The builder's own label
  (`DIAGNOSTIC` for "the wall as a threshold for the sign") is correct, but §3.3's prose
  ("that is the rate theorem the round was asked for"), §3.3's budget table and §7's summary all use it as if it
  were a *necessary budget for positivity* — which is the converse of the converse of what is proved.

**Explicit witness that support alone is empty.** Take `μ̌(u) = (1−|u|/2T)_+`, i.e.
`dμ = (T/π)(\sin(Tτ)/(Tτ))²dτ`: a probability measure, `μ̌(u) = 0` for **every** `|u| ≥ 2T`, hence feasible for
every lattice, every `N`, every `u_max`, with essentially all mass in `|τ| ≲ 1/T`. It has `τ_c = ∞` and so evades
K — and it shows that the constraint set never collapses with `N`: what changes with `N` is the geometry of the
extreme points, not the reachable mass profile.

### 2.3 The missing lemma is not (P154.6)

(P154.6) as stated (Turán/Remez stability of the count under near-zeros) would upgrade K to: *if `μ` keeps
`1−ε` of its mass inside `[−τ₁,τ₁]` and nearly satisfies the constraints, then `N ≲ e·τ₁u_max/π + C(ε)`.*
Even granting it, the next step is a **mass-to-value** balance, and it is weak: with
`σ_T ≥ −B`, `B = Σv_n − m(0) = 6.352442` at `½log3` (`R153_016 §2`, re-derived: `m(0) = −5.37218`), a measure with
mass `ε` beyond `R` satisfies `∫σ_Tdμ ≥ −B + ε(m(R) − Σv_n) ≈ −B + ε\log(R/τ₁)`. To convert an escaped mass `ε`
into a positive value one needs `\log(R/τ₁) ≳ B/ε`, i.e. **`R ≳ τ₁e^{B/ε}`**. The gain is logarithmic in the very
quantity K controls; a factor-2 improvement in the wall buys essentially nothing in the value. **Required repair:
replace (P154.6) by a quantitative statement about the mass distribution of relaxed-feasible measures
(a Turán-type lower bound on `μ([−τ₁,τ₁])^c`), and state honestly that the logarithmic exchange rate above may
make any such route quantitatively inert.**

---

## 3. Calibration

### 3.1 Arithmetic — all confirmed

Re-derived independently (mpmath, `dps = 25`): `m(16.748) = 0.9802531` vs `v_2 = 0.9802581`;
`m(59.544) = 2.2488267` vs `v_2+v_3 = 2.2488263`. `v_n = 2Λ(n)/\sqrt n` are `T`-independent, so `τ₁` depends on
`T` **only** through `{n < e^{2T}}` — the builder's use of the same `τ₁ = 59.544` at `0.58` and at `\log 2`
is correct, and `M_crit ∝ T` on that plateau. `2eTτ₁/π = 15.9204 / 59.7641 / 71.4230`: confirmed.
Floors at `u_max = 21.0567`: `M=16 → 15.972`, `M=19 → 18.991`, `M=24 → 23.930` (builder: `23.99`; he used
`N = 437` where the count from `(u_max−2T)/h` is 436 — immaterial).

### 3.2 A caveat the round should record

`τ₁` is defined by the **conservative** bound `σ_T ≥ m − Σv_n`, i.e. it is (an upper bound for) the *convex hull*
of the negative set. `R153_016 §2.4` shows the actual negative set at `\log 2` is eleven intervals inside
`[0,59.544]`, of far smaller total measure. Theorem K/K1 are correctly stated with the hull (weakest hypothesis,
strongest conclusion), but any *sign* heuristic built on `τ₁` overestimates the room the relaxation has, in a way
that is `T`-dependent and grows with the number of contacts. This weakens the §4.1 diagnosis further.

### 3.3 The fatal citation error

> `R154_010 §2`, two lines after the quoted table: *"But every one of those LP values was **fictitious**: the
> branch-and-bound minimum of the same certificate was `−7·10⁻³` to `−8·10⁻³`, and cut rounds did not close the
> gap (`M = 16`: `it0 −6.70·10⁻³ → it1 −8.20·10⁻³`)."*

The triple `M=16 → −4.75·10⁻⁵`, `M=19 → +5.72·10⁻⁵`, `M=24 → +1.742·10⁻⁴` is exactly that withdrawn series
(flat programme, `ρ` free, `τ_max = 160`, grid-LP values, no verifier). **There is no measured sign crossing of
`c(M)` at `½log3` anywhere in the corpus.** What is on record is: `c(24) ≥ 4.4279·10⁻⁵` (certified,
`CERT_log3_M24.json`, `bb_lower_bound`, `2.372·10⁸` evaluations, 0 unresolved — re-read here) and, in a *different*
programme, `R154_015`'s `8.8577·10⁻⁵`. `c(16)` and `c(19)` are **unknown**; the only evidence about `M = 16` is a
*negative* B&B minimum of `−6.7·10⁻³` from the withdrawn programme.

**Required repair (binding).** Delete the "the measured crossing is exactly there" claim and the "four independent
data points" claim from §0, §3.3 and §7. The honest statement is: *`M_crit(½log3) = 15.9` is not contradicted by
anything measured, and no measurement of the crossing exists.* Note also that even the `M = 24` deficit input is
ambiguous by a factor 2 (`4.43·10⁻⁵` certified vs `8.86·10⁻⁵` used), which alone moves the "captured fraction"
from `0.090` to `0.045`.

At `T = 0.58` the two recorded numbers (`c(24) ≤ −3.93·10⁻³`, `c(32) ≤ −7.45·10⁻⁴`, `R154_017 §4`) are genuine
row-relaxation **upper** bounds, hence genuinely negative — but `R154_017` attaches a 30 % primal/dual solver
disagreement to them, and they test only the vacuous half of the implication (below the wall, negative: K predicts
nothing either way).

---

## 4. The deficit law

§3.3 derives `D ≳ λ_min·M_crit/M` (captured fraction `1 − M_crit/M`, `α = 1`) and calibrates it against one
number. §4.1 then explains the second-contact cost with `(1 − M_crit/M)²` and states that the squared form is
"the better of the two fits at `½log3`". **The two sections use incompatible laws on the same data point.** Neither
is derived from Theorem K — K bounds no value (§2.2) — so both are curve-reading on one measurement whose input
is itself ambiguous by a factor 2 (§3.3). **Required: relabel the deficit law `HEURISTIC` (not `DIAGNOSTIC`), pick
one exponent, and state explicitly that no proof connects K to `D`.**

---

## 5. The remedy, and the falsifier

Clause (a) is Theorem K, clause (b) is immediate (the lattice `2T + jh'` with `h' | 2T` keeps `ν̂`
`P'`-periodic), clause (c) is the content and is correctly flagged unproved. The budget arithmetic is right
(`e·3.386·59.544/π = 175`; `e·21.1·59.544/π = 1087`), and the qualitative corroboration in §4.3 survives even
though its power law does not (23.8 % of `‖a‖₁` sits in the first 10 % of the `u`-range; the outer atoms are
numerically idle). Two costs the builder understates:

* the verification period `P' = 2π/h' ≈ 550` is `4×` round 5's, and Lemma F1's conservatism term
  `|β₀|k₀ + |β₁|k₁` is evaluated per period — `R154_016 E2` measured `1.81·10⁻²` at `M = 24`, which at `\log 2`
  must be compared against a target of `1.09·10⁻⁷`. **The tail lemma's own slack, not the LP, may be the binding
  object in the clustered class.** This must be checked before any run.
* clustering shrinks `u_max`, hence *lengthens* the shortest oscillation `2π/u_max` — good for the separation
  oracle — but it also makes the `\cos(u_jτ)` columns **more** collinear (all frequencies within `[2T,V]`), which
  is precisely the conditioning failure `R154_017 §3` diagnosed as the true LP wall. The `(n_cols/52)^{2.4}`
  extrapolation is not transferable to a differently-conditioned column block.

**Falsifier, as specified, accepted with amendments.** One LP, `T = 0.58`, `N' = 175` atoms on `[1.16, 3.16]`,
`h' = 2/175` adjusted so that `h' | 2T`, full column set, row generation only (no column pricing — 175 columns is
inside the affordable regime measured in `R154_017 §3`), value compared against `−3.196·10⁻³`. Amendments:
(i) report the row-relaxation value as an **upper** bound and the refined true minimum as a **lower** bound, and
do not quote a single number; (ii) report `|β₀|k₀+|β₁|k₁` at `P' = 2π/h'` in the same table; (iii) run the
matched control (`N' = 175` atoms *spread* over `[1.16, 21.1]`), otherwise the comparison confounds the budget
with the clustering.

---

## 6. Proposition E

The identity is correct and trivial: `\mathrm{supp}(H⋆\tilde F_★) ⊆ [T,∞)+[−T,T] = [0,∞)`, and with evenness the
gap is gone. Accepted as `PROVED`.

The *consequence* is overreach on two counts. (i) It shows that **this** algebraic route (multiply the E-L
identity by `\overline{F̂_★}`) destroys the gap; it does not show that no analytic construction produces a gapped
minorant — a claim of that strength would have to quantify over all constructions, and Theorem O (non-attainment)
does not supply it, since near-certificates are exactly what is wanted. (ii) The assertion "`F̂_★` … has a discrete
real zero set unless it has none, which a real even `L²(−T,T)` datum does not avoid" is **not an argument**;
compactly supported `L²` data with real-zero-free transforms are not excluded by anything stated. The comb ↔
`\{F̂_★ = 0\}` identification is at best `DIAGNOSTIC` and rests on exact complementary slackness at `c = λ_min`,
which Theorem O says is never attained. **Required: keep Proposition E as `PROVED`; relabel the consequence
`DIAGNOSTIC` and restate it as "the E-L route via `\overline{F̂_★}` is closed", not "no analytic near-certificate
exists".**

---

## 7. Proposition P and the `β₀` row

Identity re-derived: with `\hatΦ(z) = ∫Φ(u)e^{izu}du` and `Φ` even, `\hatΦ(i/2)+\hatΦ(−i/2) = 2∫Φ(u)\cosh(u/2)du`,
so a multiplier `β₀ = 2` on the constraint `∫Φ\cosh(u/2) = 0` reproduces the two polar terms with coefficient `1`
each. **`PROVED`, agreed.**

On the limit: I go further than the builder. The two recorded values (`2.0025617` at `½log3`, `2.0399645` at
`0.58`) are at **different `T` and different contact sets**, so they are not a drift of anything — they are two
unrelated numbers. They are neither evidence for nor evidence against `β₀^{opt} → 2`. The builder's proposed
amendment is therefore **too generous to the data**; the correct amendment to `R154_012 §1` is:

> **The polar term.** `β₀ = 2` is the unique multiplier value that restores exactly the two polar terms
> `\hatΦ(i/2)+\hatΦ(−i/2)` of the explicit formula (`PROVED`, identity). Optimal duals are observed near `2`
> (`2.0026` at `½log3`, `2.0400` at `0.58`); **no limit is claimed or tested**, and boundedness of the multipliers
> along a maximising sequence is itself `OPEN` (Theorem O's degeneracy `‖a‖₁ → ∞` threatens it).

The word "drift", in either direction, must not appear.

---

## 8. Literature and corpus

**Verified as real and apt:** Vaaler, *Some extremal functions in Fourier analysis*, Bull. AMS **12** (1985)
183–216; Holt–Vaaler, Duke **83** (1996); Carneiro–Vaaler, Trans. AMS **362** (2010); Carneiro–Littmann–Vaaler,
Gaussian subordination, Trans. AMS **365** (2013); Poltoratski, *Spectral gaps for sets and measures*, Acta Math.
**208** (2012); Beurling–Malliavin. B. F. Logan's thesis (1965) is the right origin for the sign-change density
`a/π` of high-pass signals, and Eremenko–Novikov, *Oscillation of Fourier integrals with a spectral gap*
(PNAS **101** (2004) announcement) is the right proof reference; the density check is right
(`2T/π = 0.3497` at `½log3`).

**Unverified — do not print until checked against the actual records:** the arXiv IDs `math/0301060`
(Eremenko–Novikov), `1406.0025` with the title *Determinacy for measures* (Mitkovski–Poltoratski — the paper I can
place with confidence is *Pólya sequences, Toeplitz kernels and gap theorems*), and `1311.1157` with the title
*Extremal functions with vanishing condition* (Carneiro–Littmann, Constr. Approx. **42** (2015)). The
Carneiro–Littmann "prescribed zeros" line is apt *if* the paper is what the title says; I could not confirm the
pairing here. Mark all three `CITATION UNVERIFIED`.

**Corpus greps rerun (2026-09-21, `03-research`, `04-papers`, `05-meta-and-planning`, `.md`/`.tex`):**
`"one-sided approximation"` — **0 hits outside phase 154**, confirming the builder's row. `"Jensen"` — many hits
(phase-24, phase-58, phase-136 `NG-A5`/`CIR-6`), **all unrelated** (Jensen's formula for `ζ` growth, and the
Li/Jensen-coefficient no-go). The builder's claim that the *application of Jensen to the lattice constraint set*
is new stands. Note for the record: phase-136 `NG-A5`/`CIR-6` are the standing no-go against Jensen-coefficient
routes and are not touched by anything here (Theorem K is about `μ̌`, not about `ζ`).

**FATAL rule:** clean. Every `T` discussed is `≤ \log 2`; no sign for `ζ`; nothing certified this round; the
endpoint of record remains Theorem R5a / Theorem C(`½log3`).

---

## 9. Required repairs, ranked (binding for the round-7 record)

1. **§3.3, §0, §7:** delete the "measured sign crossing" calibration and the "four independent data points"
   claim; the numbers cited are the ones `R154_010 §2` withdrew as fictitious. Replace by "not contradicted;
   the crossing has never been measured".
2. **§3.3, §7:** stop calling Theorem K "the rate theorem the round was asked for". Add Corollary K0 (§2.1, free
   repair) and state K's content as: *the relaxed minimiser is atomic with `≤ N+3` atoms and must place an atom
   beyond `πN/(e·u_max)`* — a support statement, not a value statement.
3. **§3.4:** replace (P154.6) by the mass-balance problem of §2.3, with the logarithmic exchange rate
   `R ≳ τ₁e^{B/ε}` stated as the obstacle.
4. **§3.1 remark (iii) / §8 item 4:** record that the sharp density constant is `1`, not `1/e`
   (Cartwright/Levinson, applicable because `|Λ| ≤ 1` on `R`), hence every `M_crit` is uncertain by a factor up to
   `e`: `M_crit(\log 2) ∈ [26, 71]`.
5. **§4.1, §3.3:** one deficit exponent, labelled `HEURISTIC`; delete the `(3.75)²` inference.
6. **§4.3:** delete the `|a_j| ∼ u_j^{-1}` power law and its identification with `½K(u) ∼ 1/(2u)`
   (local slopes `−0.24` / `−3.69`); keep the edge-concentration statement.
7. **§5:** relabel the consequence of Proposition E `DIAGNOSTIC` and narrow it to the `\overline{F̂_★}` route.
8. **§6:** adopt the stronger `R154_012` amendment of §7 above (no "drift").
9. **§4.2:** add the two understated costs of §5 and the matched control to the falsifier.
10. **§2.3:** mark the three arXiv IDs `CITATION UNVERIFIED`.

## 10. Honest reading (one paragraph)

Theorem K is true, the constant `π/e` is correct and correctly derived, and with the extreme-point repair it is
unconditional at the relaxed minimiser — but it is **not a rate theorem**: it constrains the *support radius* of
the minimising measure and says nothing about `c(h,u_max;T)`, because value is governed by mass and K controls no
mass (the Fejér witness of §2.2 is feasible for every `N` with all its mass in the negative set). Everything the
round hangs on `M_crit` — the calibration, the deficit law, the budget table, the staircase — is therefore
heuristic, and its single empirical anchor is a set of LP values the corpus had already declared fictitious.
What survives, and is worth keeping, is real: the refutation of the off-lattice-`log 3` diagnosis by the window
identity; the observation that the wall depends on atoms only through the density `N/u_max`, which explains why
round 6's `u_max`-lever was neutral; and the resulting clustering proposal, which is the first concrete,
affordable, falsifiable thing anyone has proposed for `T = 0.58`. On the round's final question: the clustered
class makes the staircase **arithmetically** plausible (`≈ 26–175` columns at `\log 2` instead of `≈ 1087`), and
that is a real change in the compute picture; but "`M ≈ 70–80` suffices" is the converse of a heuristic, the true
negative set is far sparser than `[−τ₁,τ₁]`, the `M_crit ∝ Tτ₁(T)` growth is doubly exponential in `T` so no
`T`-uniform family can come from here, and the binding object in the clustered class may turn out to be Lemma F1's
own slack (`1.8·10⁻²` at `M = 24`) against a `\log 2` target of `1.09·10⁻⁷`. **Feasible in principle at one more
step, closed as a uniform route.** Run the amended falsifier before anything else.
