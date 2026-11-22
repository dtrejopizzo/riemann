# R155.023 — round 3a: the archimedean threshold and the necessity of the primes

*Phase 155, round 3a. Executes the the round-3a order. Inherits Paper 46 §2
(`lem:K`, `thm:S`, `thm:A`, `cor:mono`), §4 (`lem:mbounds`), §8 (`thm:SC`, table `T₀(A)`), and
`R155_022` (the decomposition `W = pole + gamma + prime`). Paper 46 is **not** touched.*

**No sign for `ζ` is claimed at any `T`. Endpoint of record unchanged:
`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵` (Paper 46 Thm C). All numbers are `DIAGNOSTIC`
(double precision, Galerkin, no interval arithmetic). Scripts: `scripts/r3a/`.**

*[amended per R155_025] Eight repairs (E1–E8) applied throughout per the audit
`R155_025_AUDIT_R3A.md`: the prime quadratic form is renamed `Π_T` to stop colliding with the
subspace `P_T` (E6); the Lévy cross-check numbers, the stability claim, the `T = ½log2` table row, the
"eight windows" count, and several labels are corrected below at each marked point.*

---

## §0 Verdict in five lines

1. **There are two archimedean thresholds, not one, and the order's guess is inverted at one of them.**
 On all of `L²(−T,T)` (pole term present) `T*_∞ = 0.3716` (bisected, `[0.371602, 0.371641]`).
 On the primitive subspace `P_T` (pole term killed — the space on which Paper 46's `λ^P` and
 Theorem C live) `T*_{∞,P} = 0.5958` (`[0.595781, 0.595859]`). *[amended per R155_025,
 E3] Both are Galerkin values, hence upper bounds: `T*_∞,true ≤ 0.3716`, `T*_{∞,P},true ≤ 0.5958`.*
2. `T*_∞ = 0.3716` sits **just above** `½log 2 = 0.34657` — the archimedean form survives the end of the
 prime-free window by `0.025` and no more — and **below** `½log 3 = 0.54931`. So for the *complete*
 Weil form at `½log3` the primes are necessary: the deficit is `η(½log3) = 0.43027` and the prime
 term on the archimedean ground state supplies `Π_T(F*_∞) = +0.46252`, covering it with `7 %` to spare.
3. `T*_{∞,P} = 0.5958 > ½log 3`. **Therefore Theorem C's certificate at `½log3` does *not* rely on the
 primes to supply positivity.** The archimedean form alone is positive there on `P_T`
 (`λ^{∞,P}_min(½log3) = +0.08255`), and switching the primes on *lowers* the bottom by two orders,
 `+8.26·10⁻² → +9.77·10⁻⁴`. On the primitive subspace the primes are a **cost**, not a resource,
 and they remain one until `T*_{∞,P}`; past `0.5958` they become indispensable (at `log 2`:
 `λ^{∞,P}_min = −0.15428`, prime term on that ground state `+0.18849`).
4. The order's inequality `λ^{∞,P}_min ≤ λ^∞_min` is **false as stated and holds in the opposite
 direction**: `P_T ⊂ L²(−T,T)`, so the restricted infimum is the larger one. Verified at every `T`
 of §3 (e.g. `−0.43027` vs `+0.08255` at `½log3`).
5. The trivial bound `λ_min ≥ λ^∞_min − ‖Π_T‖` is useless by three orders of magnitude at every window
 (`−0.920` at `½log3` against the true `+9.8·10⁻⁴`): pole, gamma and prime cancel, as `R155_022 §4`
 measured, and no triangle inequality between the three blocks can see it.

---

## §1 Corpus check (grep-verified, `03-research` + `04-papers`)

| query | hits | what is already there | what is new here |
|---|---|---|---|
| `archimedean` | 1189 files | the multiplier `m(τ)`, its Lévy form (Paper 46 §2), the high-`τ` envelope regime (`lem:mbounds`, `prop:env`) | nobody has ever computed the **bottom of the archimedean block alone** as a function of `T` |
| `prime-free window` / `Connes–Consani` | 156 files (`phase-115/115_10`, `phase-115/scripts/115_08`, `phase-118/PHASE_118_CLOSURE`, `THE_BACKWARD_MAP`) | the regime `2T < log 2`: `N_T = ∅`, the prime term vanishes identically, positivity is unconditional | that regime ends at `½log2` but the **archimedean positivity** survives to `0.3716`; the `0.025` gap is measured here for the first time |
| `Yoshida` | Paper 46 `:137,241,244,276`; `phase-154/R154_013`; `phase-155/R155_001`; `phase-114/114_d_58` | Yoshida 1992: strict positivity at autocorrelation support `log 2`; Lemma 2 a small-window constant. `R154_013`: the 1992 volume is **not** in `00-references`, statements are from secondary reports | the citation is used here only for `≥ 0`; the strictness is recorded as `CONDITIONAL` |
| `lambda_min` / `λ_min` | 124 files | `λ^P`, `λ^W`, `λ_min(A_T\|P_T)`, Galerkin values | the archimedean analogues `λ^∞_min`, `λ^{∞,P}_min` are new names for new objects |
| `pole term` | 72 files | `2Re(A B̄)`, the polar multiplier `β₀ = 2` (Paper 46 `prop:P`), `R155_022 §4` (pole ≈ −gamma to a few %) | the pole term is here shown to be **the whole difference between the two thresholds**: `0.3716` vs `0.5958` |
| `rank two` / codim 2 | 56 files | `P_T` is codimension 2; `cor:mono` uses `λ₃` for that reason | reused verbatim |
| `local positivity` | 24 files | rows A–C vocabulary | not relevant |
| `primitive`, `P_T` | 1388 / 313 files | `K^prim`, `λ^P ≤ λ_min(A_T\|P_T)` | the archimedean restriction of the same subspace |

Nothing in the corpus computes `λ^∞_min`. `R155_018` has no §5 (its headings are §1–§4); the round-3
orders are those of the message and of `R155_018 §4`, which are executed here.

---

## §2 Theorem and proofs

Notation as in Paper 46 §2: `K(u) = 1/(2 sinh(u/2)) + 1/(2 cosh(u/2))`, `C₀ = ψ(¼) − log π = −5.3721834`,
`Lev(Φ) = ∫₀^∞ (Φ(0) − Re Φ(u)) K(u) du`, `φ` the complete Bernstein function of `thm:S`,
`c_F` the autocorrelation, `A(F) = ∫F e^{t/2}`, `B(F) = ∫F e^{−t/2}`, `P_T = {A = B = 0}`.

**Definition.** `A_∞(F) = 2 A(F)B(F) + (1/2π)∫ m(τ)|F̂(τ)|²dτ = 2A(F)B(F) + C₀‖F‖² + Lev(c_F)`
(the second equality is Paper 46 `thm:A` with `N_T = ∅`). Put

 `λ^∞_min(T) = inf{ A_∞(F) : ‖F‖ = 1, supp F ⊂ (−T,T) }`,
 `λ^{∞,P}_min(T) = inf{ A_∞(F) : ‖F‖ = 1, F ∈ P_T } = inf{ C₀ + Lev(c_F) : ‖F‖=1, F ∈ P_T }`.

### Theorem 1 (archimedean indefiniteness). `PROVED` except where marked.

**(a) Monotonicity.** Both `λ^∞_min` and `λ^{∞,P}_min` are non-increasing in `T`. `PROVED`.
*Proof.* `A_∞` does not depend on `T`: the Lévy density `K`, the constant `C₀` and the two Tate
moments are `T`-free. The feasible sets `{‖F‖=1, supp F ⊂ (−T,T)}` and its primitive subset increase
with `T` (extension by zero), and the constraint `A(F)=B(F)=0` is `T`-free. An infimum over a growing
set is non-increasing. ∎ (This is Paper 46 `cor:mono` with the comb removed; the comb is what makes
the cited statement say "with the contact set held fixed".)

**(b) Positivity below the prime-free threshold.** For `2T < log 2`, `λ^∞_min(T) ≥ 0`. `PROVED` (by
citation). Strict positivity: `CONDITIONAL`.
*Proof.* For `2T < log 2` the contact set `N_T = {n ≥ 2 : log n < 2T}` is empty, so the prime term of
`W_T` is identically zero and `W_T = A_∞` as quadratic forms on `L²(−T,T)`. Positivity of `W_T` for
`T ≤ log 2` is known (Paper 46 `:137,276`, citing `Paper42`, `Yoshida1992`, `Bombieri2000`; the [amended per R156_004 A14: `T ≤ log 2` holds for the primitive form only; complete form `T ≤ ½log2` classical, `≤ 0.8` Zhu, cited]
prime-free case is also verified end to end in `phase-115/scripts/115_08_prime_free_window_crosscheck.py`
and `phase-118/PHASE_118_CLOSURE`). Hence `λ^∞_min(T) = λ^W_min(T) ≥ 0`. ∎
*On strictness.* The corpus's own record (`R154_013`) is that Yoshida 1992 is not held in
`00-references` and its Lemma 2 is known only from secondary reports, so the strict inequality is
labelled `CONDITIONAL` on that citation. A self-contained bound is available but far too weak to
reach `½log2`: since `|c_F| ≤ 1` and `c_F = 0` off `[−2T,2T]`, and `|A|,|B| ≤ (2 sinh T)^{1/2}`,
 `λ^∞_min(T) ≥ C₀ + ∫_{2T}^∞ K − 4 sinh T = C₀ + log coth(T/2) + π − 2 arctan e^{T} − 4 sinh T`,
positive only for `T ≲ 0.031`. Numerically (§3) `λ^∞_min(½log2) = +1.33·10⁻³ > 0`, `DIAGNOSTIC`.

**(c) Negativity for large `T`, and the limit.** For every `T`,
 `λ^∞_min(T) ≤ λ^{∞,P}_min(T) ≤ C₀ + φ((3π/2T)²)`,
so both are `< 0` for `T ≥ T₀(0) = 0.74921`, and `λ^{∞,P}_min(T) → C₀ = −5.3721834` as `T → ∞`. `PROVED`.
*Proof.* The first inequality is inclusion of feasible sets (`P_T ⊂ L²(−T,T)`): an infimum over a
smaller set is larger. **This corrects the direction stated in the order.** For the second, read the
proof of Paper 46 `cor:mono`. It has exactly two steps: (i) the bottom of the Lévy energy `Lev(c_F)`
on `P_T` is at most `φ((3π/2T)²)`, because `Lev` is the Dirichlet form of the subordinate Brownian
motion of `thm:S` killed on leaving `I_T`, whose eigenvalues obey `λ_n ≤ φ((nπ/2T)²)` (Song–Vondraček),
and `P_T` has codimension 2, so the bottom on `P_T` is at most `λ₃`; (ii) the comb contributes at most
`A_T‖F‖²`. Step (i) never mentions the primes, and step (ii) is vacuous when there are none. Moreover
the pole term is *identically zero on* `P_T`, which is precisely why `cor:mono` is a statement about
`P_T` and applies here with `A = 0`. This is Paper 46 `thm:SC` with `N = ∅`, `A = 0`, whose table gives
`T₀(0) = 0.74921` (verified: `φ(x_0) = −C₀ = 5.3721834` at `x_0 = (3π/2T₀)²`, `T₀ = 3π/(2√x_0)`; our
independent evaluation of `φ` gives `φ((3π/2·0.74921)²) = 5.37218`). For the limit: `Lev ≥ 0` and the
pole term vanishes on `P_T`, so `λ^{∞,P}_min ≥ C₀`; and `φ((3π/2T)²) ↓ 0` since `φ(0⁺) = 0`. ∎
(`λ^∞_min` itself decreases without bound: the pole term is an indefinite rank-2 perturbation and
`λ^∞_min(T) ≈ −1.16 T + 0.00` on `0.45 ≤ T ≤ 0.80` in §3 — no limit is claimed for it.)

**(d) The thresholds exist.** `PROVED`. By (a) each of `λ^∞_min`, `λ^{∞,P}_min` is non-increasing, by
(b) positive for `2T < log 2`, by (c) negative for `T ≥ 0.74921`. A non-increasing function changes
sign once; define
 `T*_∞ = sup{T : λ^∞_min(T) > 0}`, `T*_{∞,P} = sup{T : λ^{∞,P}_min(T) > 0}`.
Then `½log2 ≤ T*_∞ ≤ T*_{∞,P} ≤ 0.74921`. (No continuity is asserted, so "threshold" is a supremum,
not a root; in the numerics the crossing is smooth and transversal.)

### Corollary 2 (the deficit). `PROVED` (as a definition + inequality), values `DIAGNOSTIC`.
Put `η(T) = max(0, −λ^∞_min(T))` and `η_P(T) = max(0, −λ^{∞,P}_min(T))`. For `T > T*_∞` every proof
of `λ^W_min(T) ≥ 0` must exhibit, on the negative cone of `A_∞`, a prime term
`Π_T(F) = −Σ_{n<e^{2T}} v_n c_F(log n)` with `Π_T(F) ≥ −A_∞(F)`; in particular
`sup_{‖F‖=1} Π_T(F) ≥ η(T)`, and likewise with `η_P` on `P_T` for `T > T*_{∞,P}`.
*Proof.* `W_T = A_∞ + P_T` pointwise on test functions; evaluate at a minimising `F`. ∎

---

## §3 Numerics

Galerkin in an orthonormal Legendre basis of `L²(−T,T)`, `N = 18` (values stable to an **absolute**
`2.5·10⁻⁵` against `N = 36`; *[amended per R155_025, E2] this is an absolute figure, not a
relative one — the `1.3 %` spread between this round's `λ_min(a_T|P_T)(½log3) = 9.7692·10⁻⁴` and
`R155_004`'s independent Galerkin value `9.893·10⁻⁴` is consistent with it: both are upper bounds on
the true infimum, the new one tighter, no contradiction*); the Gamma block is assembled from the
**Lévy** representation
`C₀I + ∫₀^{2T}(I − C(u))K(u)du + (∫_{2T}^∞ K)I` (three-panel Gauss–Legendre, the `1/u` singularity of
`K` cancelled by `I − C(u) = O(u)`), the pole block as the rank-2 `ab^T + ba^T`, the prime block as
`−Σ v_n C(log n)`. *[amended per R155_025, E1]* The Lévy assembly is cross-checked against
the direct `(1/2π)∫m|F̂|²` on a random unit vector at working accuracy `N = 18`:
`direct(|τ|<500) = 1.86645`, `direct(|τ|<2000) = 2.05753`, against the Lévy value `2.14514723` — errors
`13 %` and `4 %` (the `log τ` tail of `m` makes the convergence slow but monotone). This is a weak,
genuine corroboration of the assembly, not a tight numerical agreement.
**End-to-end validation** (`r3a_01`): `λ_min(W_T) > 0` at every
`T ≤ log 2` — *[amended per R155_025, E8: the list previously gave six of the eight
computed windows, omitting `T = 0.45` and `T = 0.60`; both are restored here]*
`+7.5748·10⁻³, +1.3322·10⁻³, +1.8232·10⁻⁴, +1.6434·10⁻⁵, +9.5835·10⁻⁷, +5.6461·10⁻⁸, +3.1344·10⁻⁹,
+1.4007·10⁻¹⁰` at `T = 0.30, 0.3465, 0.40, 0.45, 0.50, 0.55, 0.60, log2` (eight windows) —
reproducing the known theorem, and
`λ_min(A_T|P_T)(log2) = +9.9416·10⁻⁷` (`r3a_02`'s restriction path; `r3a_04` gives `9.96·10⁻⁷` by a
different restriction path — *[amended per R155_025, E8]* the two agree only to `1.5·10⁻³`
relative, which is the real accuracy of the restricted eigenvalue), of the order Paper 46 §2 quotes
("the truth is `λ ≈ 10⁻⁷`"). *[amended per R155_036] This is an unstabilised
Rayleigh–Ritz upper bound: round 4a found `9.94e−7` at `N = 18` vs `3.38e−5` at `N = 36` (a factor
`34` at fixed subspace dimension), with the bottom itself falling `9.94e−7 → 1.05e−7` from `N = 18`
to `N = 36`. No numerical value of `inf A_T|P_T` (or `inf W_T|P_T`) at `log 2` is supported by this
computation.*

*[amended per R155_025, E4] The `T = 0.3466` (`½log2`) row previously listed `‖Π_T‖ = 0`,
`A_T = 0`, which misstates the contact set: at `T = 0.3466`, `2T = 0.6932 > log2`, so `N_T = {2}` is
already nonempty. Corrected below from the rerun.*

*[amended per R155_036] The `λ_min(a_T|P_T)` / `λ_min(W_T)` columns at the two-prime windows (`N_T ⊇ {2,3}`, i.e. `T ≥ log 2`) are unstabilised Rayleigh–Ritz upper bounds; no numerical value of `inf W_T|P_T` at `log 2` is supported (see `R155_036`: `N`-inconsistency at `k = 8`, `9.94e−7` at `N = 18` vs `3.38e−5` at `N = 36`; bottom falls `9.94e−7 → 1.05e−7`).*

| `T` | `λ^∞_min` | `λ^{∞,P}_min` | `n₋(A_∞)` | `n₋(A_∞\|P_T)` | `‖Π_T‖` | `A_T` | `λ_min(a_T\|P_T)` | `λ_min(W_T)` |
|---|---|---|---|---|---|---|---|---|
| 0.300 | `+7.5748e−03` | `+0.69203` | 0 | 0 | 0 | 0 | `+6.9203e−01` | `+7.5748e−03` |
| 0.320 | `+3.4871e−03` | `+0.62723` | 0 | 0 | 0 | 0 | `+6.2723e−01` | `+3.4871e−03` |
| 0.340 | `+1.6098e−03` | `+0.56633` | 0 | 0 | 0 | 0 | `+5.6633e−01` | `+1.6098e−03` |
| **0.3466** (`½log2`) | `+1.3322e−03` | `+0.54730` | 0 | 0 | `0.01261` | `0.9803` | `+5.4730e−01` | `+1.3287e−03` |
| 0.360 | `+1.0835e−03` | `+0.50888` | 0 | 0 | 0.46089 | 0.9803 | `+4.7821e−01` | `+8.5072e−04` |
| **0.3716** | **`≈ 0` (T\*_∞)** | `+0.48` | 0→1 | 0 | 0.478 | 0.9803 | — | — |
| 0.380 | `−2.3548e−02` | `+0.45450` | 1 | 0 | 0.48474 | 0.9803 | `+3.4285e−01` | `+4.0888e−04` |
| 0.400 | `−7.8010e−02` | `+0.40287` | 1 | 0 | 0.48862 | 0.9803 | `+2.2590e−01` | `+1.8232e−04` |
| 0.420 | `−1.3029e−01` | `+0.35373` | 2 | 0 | 0.48946 | 0.9803 | `+1.4329e−01` | `+7.4998e−05` |
| 0.440 | `−1.8065e−01` | `+0.30684` | 2 | 0 | 0.48993 | 0.9803 | `+8.7253e−02` | `+2.7936e−05` |
| 0.460 | `−2.2929e−01` | `+0.26200` | 2 | 0 | 0.49006 | 0.9803 | `+5.0061e−02` | `+9.4516e−06` |
| 0.480 | `−2.7642e−01` | `+0.21902` | 2 | 0 | 0.49007 | 0.9803 | `+2.6203e−02` | `+2.9709e−06` |
| 0.520 | `−3.6679e−01` | `+0.13809` | 2 | 0 | 0.49013 | 0.9803 | `+4.5884e−03` | `+3.5383e−07` |
| **0.5493** (`½log3`) | `−4.3027e−01` | `+0.08255` | 2 | 0 | 0.49013 | 0.9803 | `+9.7692e−04` | `+5.8700e−08` |
| 0.560 | `−4.5294e−01` | `+0.06300` | 2 | 0 | 0.68637 | 2.2488 | `+6.0167e−04` | `+3.0236e−08` |
| **0.580** | `−4.9474e−01` | `+0.02739` | 2 | 0 | 0.79004 | 2.2488 | `+2.1552e−04` | `+8.3342e−09` |
| **0.5958** | `−0.52` | **`≈ 0` (T\*_{∞,P})** | 2 | 0→1 | 0.85 | 2.2488 | — | — |
| 0.600 | `−5.3584e−01` | `−0.00707` | 2 | 1 | 0.85902 | 2.2488 | `+7.1221e−05` | `+3.1344e−09` |
| 0.640 | `−6.1629e−01` | `−0.07278` | 2 | 1 | 0.89575 | 2.2488 | `+9.3347e−06` | `+7.8599e−10` |
| 0.680 | `−6.9500e−01` | `−0.13469` | 2 | 1 | 0.89886 | 2.2488 | `+1.7042e−06` | `+2.0226e−10` |
| **0.6931** (`log2`) | `−7.2060e−01` | `−0.15428` | 2 | 1 | 0.89997 | 2.2488 | `+9.9416e−07` | `+1.3997e−10` |
| 0.720 | `−7.7257e−01` | `−0.19324` | 2 | 1 | 0.95595 | 2.9420 | `+4.3933e−07` | `+9.4082e−11` |
| 0.760 | `−8.4955e−01` | `−0.24882` | 2 | 1 | 1.12143 | 2.9420 | `+2.0711e−07` | `+5.4790e−11` |
| 0.800 | `−9.2643e−01` | `−0.30175` | 2 | 1 | 1.19515 | 2.9420 | `+2.2906e−07` | `+4.4338e−12` |

Bisection (`r3a_03`, 9 steps each):
**`T*_∞ ∈ [0.371602, 0.371641]`**, **`T*_{∞,P} ∈ [0.595781, 0.595859]`**.
*[amended per R155_025, E3] The Legendre basis is orthonormal and supported in `(−T,T)`,
so every Galerkin eigenvalue is an **upper bound** on the true infimum, and hence every Galerkin
threshold is an upper bound on the true threshold: `T*_∞,true ≤ 0.3716` and `T*_{∞,P},true ≤ 0.5958`.
Nothing computed here certifies that the true thresholds equal these values, only that they do not
exceed them.*
Both lie in the interval `[½log2, T₀(0)] = [0.34657, 0.74921]` predicted by Theorem 1(d), and
`T*_∞` uses only `13 %` of that interval while `T*_{∞,P}` uses `62 %`.

**Position relative to the landmarks.** `T*_∞ = 0.3716 < ½log3 = 0.54931 < log 2 = 0.69315`, and
`T*_∞ > ½log2 = 0.34657`. But `½log3 < T*_{∞,P} = 0.5958 < log 2`.

**The prime term on the archimedean ground states** (`r3a_04`; `F*_∞` = bottom eigenvector of `A_∞`
on `L²(−T,T)`, `F*_P` = bottom eigenvector of `A_∞|P_T`):

*[amended per R155_036] The `λ_min(a_T|P_T)` / `λ_min(W_T)` columns at the two-prime windows (`N_T ⊇ {2,3}`, i.e. `T ≥ log 2`) are unstabilised Rayleigh–Ritz upper bounds; no numerical value of `inf W_T|P_T` at `log 2` is supported (see `R155_036`: `N`-inconsistency at `k = 8`, `9.94e−7` at `N = 18` vs `3.38e−5` at `N = 36`; bottom falls `9.94e−7 → 1.05e−7`).*

| `T` | `η = −λ^∞_min` | `Π_T(F*_∞)` | `W_T(F*_∞)` | `η_P` | `Π_T(F*_P)` | `a_T(F*_P)` | `‖Π_T‖` | `λ^∞_min − ‖Π_T‖` | true `λ_min(a_T\|P_T)` |
|---|---|---|---|---|---|---|---|---|---|
| `½log3` | 0.43027 | **+0.46252** | +0.03225 | — (`+0.08255`) | **+0.00805** | +0.09060 | 0.49013 | `−0.92039` | `+9.7692e−04` |
| 0.58 | 0.49474 | **+0.52126** | +0.02651 | — (`+0.02739`) | **+0.06496** | +0.09235 | 0.79004 | `−1.28479` | `+2.1552e−04` |
| `log 2` | 0.72060 | **+0.76281** | +0.04221 | 0.15428 | **+0.18849** | +0.03421 | 0.89997 | `−1.62057` | `+9.9416e−07` |

Readings.
1. At every window the primes cover the deficit of the *complete* form on the archimedean ground
 state, and only just: `Π_T(F*_∞)/η = 1.075, 1.054, 1.059`. The residue `W_T(F*_∞) ≈ 0.03`, i.e.
 `6 %` of the two terms — the same few-percent cancellation `R155_022 §4` measured on random `F`,
 now on the worst archimedean direction.
2. On the primitive subspace the picture is the opposite at `½log3` and `0.58`: `η_P = 0`, the primes
 *add* a little on `F*_P` (`+0.008`, `+0.065`) and yet the bottom over all of `P_T` collapses
 (`+0.0826 → +0.0010`, `+0.0274 → +0.00022`): the minimiser moves to a direction the primes punish.
3. The trivial bound `λ_min ≥ λ^∞_min − ‖Π_T‖` is negative by `10³` at `½log3` and by `10⁶` at `log 2`
 (the `log 2` gap statement rests on the unstabilised Galerkin value there — *[amended
 per R155_036]* see the caveat above).
 `‖Π_T‖` is essentially flat in `T` inside a fixed contact regime (`0.489–0.490` for `N_T = {2}`)
 and jumps on prime entry (`{2} → {2,3}`: `0.490 → 0.686`), mirroring the step law in `N_T` recorded
 in `R155_005`.

---

## §4 Proposition: the negative cone of `A_∞`

### Proposition 3 (dimension of the negative cone). (i) `PROVED`; (ii) upper bound `PROVED`, lower
bound `HEURISTIC` — *[amended per R155_025, E5] previously mislabelled `PROVED
(asymptotics standard)` throughout*; counts `DIAGNOSTIC`.
Let `τ₀` be the unique positive root of `m(τ) = 0`. Then **`τ₀ = 6.28983599`** (`r3a_03`, Brent to
`10⁻¹²`; note `τ₀ − 2π = 6.6·10⁻³`, a coincidence, not an identity). Since `m` is increasing on
`[0,∞)` with `m(0) = C₀ < 0` (Paper 46 `lem:mbounds`(i)), `m < 0` exactly on `|τ| < τ₀`.
Let `n₋(T)` be the number of negative eigenvalues of `A_∞|P_T`. Then
 **(i)** `n₋(T) ≥ 1` for every `T > T*_{∞,P}` (definition of the threshold), and
 **(ii)** `n₋(T) = (2τ₀/π)·T + O(log T) = 4.0040·T + O(log T)` as `T → ∞`.
*Proof of (ii).* *[amended per R155_025, E5] The lower-bound half of this argument is a
sketch, not a proof: "`‖F − B_{τ₀}F‖` is small in the `L²`-averaged sense" and "a standard splitting …
makes the form strictly negative" are asserted without quantification, and the `log τ` growth of `m`
off the band is exactly what such a splitting has to beat — no constant is produced. Downgraded to
`HEURISTIC`; only the matching upper bound below is `PROVED`.* On `P_T` the pole term vanishes and
`A_∞(F) = (1/2π)∫ m|F̂|²`. Let `Q_T` be the
orthogonal projection of `L²(ℝ)` onto functions supported in `(−T,T)` and `B_{τ₀}` the band-limiting
projection onto `|τ| < τ₀`. The operator `Q_T B_{τ₀} Q_T` is the time–band-limiting (Slepian) operator
of time–bandwidth product `2T·2τ₀/2π = 2Tτ₀/π`; by Landau–Widom its number of eigenvalues exceeding
`½` is `2Tτ₀/π + O(log T)`. On the corresponding span `V_T`, `‖F − B_{τ₀}F‖` is small in the
`L²`-averaged sense (`HEURISTIC`), and `m ≤ m(τ₀) = 0` on the band while `m(τ) ≤ log(τ/2π) + O(1/τ)`
grows only logarithmically off it; a standard splitting of `(1/2π)∫m|F̂|²` into band and tail on a
subspace of `V_T` of codimension `O(log T)` makes the form strictly negative there (`HEURISTIC`,
unquantified). Removing the two Tate
conditions costs 2 more dimensions. **`PROVED`:** the matching upper bound is the min–max principle
applied to the complement `B_{τ₀}^⊥`, where `m ≥ 0`, giving `n₋(T) ≤ 2Tτ₀/π + O(log T) + 2`. ∎
*Honesty.* The asymptotic is `4.004·T`; at `T = 0.80` it predicts `3.2` against the computed `n₋ = 1`
(and `n₋(A_∞) = 2` on all of `L²`, the extra direction being the indefinite rank-2 pole term). The
`O(log T)` correction dominates in the whole computed range, so the growth statement is asymptotic
only and the table's counts are the honest finite-`T` fact: **one** negative direction on `P_T` from
`0.5958` to `0.80`. The first `n₋ = 2` on `P_T` is therefore expected near `T ≈ 1`, outside this run.

**Consequence.** For `T > T*_{∞,P}` any proof of `λ_min(A_T|P_T) ≥ 0` must show `Π_T(F) ≥ −A_∞(F)` on
a cone of dimension `≥ 1` growing linearly in `T`, i.e. on an increasingly large subspace on which the
archimedean block is *actively* negative. This is the quantitative form of "the primes are necessary".

---

## §5 Corollary for the construction of `D`

In the dual language of Paper 46 §3/§7 a certificate is `(ν, β)` with `σ_T + ν̂ + β₀ĝ₀ + β₁ĝ₁ ≥ c`,
`ν` supported outside `[−2T,2T]`. §3–§4 say the following about what such a `(ν, β)` must do.

1. **The two régimes of the certificate are separated by `T*_{∞,P} = 0.5958`, not by a prime entry.**
 For `½log3 ≤ T < 0.5958` the archimedean symbol `m` alone is already `≥ 0` on the primitive class,
 so a certificate has to *repair the damage done by the comb* (§3 reading 2): it is a perturbative
 object, and that is exactly why Theorem C succeeds with `β₀ = 2.0026 ≈ 2` and
 `β₁ = −0.0097 ≈ 0` — the polar multiplier of `prop:P` almost exactly, i.e. the certificate is
 almost purely the restoration of the two polar terms, with only a `1.3·10⁻³` relative correction
 in `β₀`. `PROVED` that `β = (2,0)` is the unique choice bounding `W_T` (`prop:P`); `OBSERVED` that
 the optimum sits `1.3·10⁻³` from it; **new here** (`HEURISTIC` — *[amended per R155_025,
 E7] a narrative reading, not a deduction: nothing in §2–§4 forces the optimiser near `(2,0)`*): the
 reason the optimum is *near* `(2,0)` is that at `½log3` the certificate is not being asked to create
 positivity, only to pay for the comb.
2. **Past `0.5958` the certificate changes job.** It must supply `η_P(T) > 0` of genuinely new
 positivity along at least one direction on which `m` is negative, i.e. it must use the primes
 (`PROVED`, Corollary 2 + Proposition 3). *[amended per R155_025, E7 — withdrawn]* The
 claim that, since `ν` lives outside the window, "the only way it reaches the inside primes is
 through `ν̂`'s oscillation at frequencies `≲ τ₀`" does **not** follow from Paper 46 §7:
 `main.tex:1052,1070` show the inside and outside prime terms combining into a single
 `−Σ_{n≥2} v_n w(log n) cos(τ log n)` valid at *all* `τ`, not only `|τ| < τ₀` — the restriction to
 `|τ| < τ₀` is where positivity is *needed*, not where the outside atoms *act*. So the remainder of
 this paragraph, "a certificate for `T > 0.5958` must carry weight at the prime atoms `log n < 2T`
 with the sign pattern that makes `ν̂` add to `−Σ v_n cos(τ log n)` on `|τ| < τ₀`", is `HEURISTIC`
 — a plausible reading, not a necessary condition. Only the first sentence of this item (the need
 for genuinely new positivity) is `PROVED`.
3. **This explains `R155_016` (comb-vanishing).** Forcing `w(log n) = 0` at the prime powers *outside*
 the window made the LP value strictly worse at all four windows (`−1.17·10⁻²` at `½log3` against
 `−8.59·10⁻³` without the comb equalities at the same `M = 24`, interval `[0,115]`; factor `2.7` at
 `M = 24`). `R155_016` recorded this as `OBSERVED`. §5.2 gives the structural reason: the outside
 prime atoms are the certificate's *only* low-frequency handle on the inside comb, since `ν` is
 confined to `|u| ≥ 2T`; zeroing `w` there removes precisely the mechanism that Proposition 3 says
 is necessary past `T*_{∞,P}` — and `0.58 < T*_{∞,P} < 0.62 < log2` covers three of `R155_016`'s
 four windows. `OBSERVED`: that comb-vanishing costs a factor `2.7`. `HEURISTIC` — *[amended
 per R155_025, E7] downgraded from `PROVED`, since the "only low-frequency handle"
 mechanism it invokes is the withdrawn §5.2 claim*: the structural explanation via §5.2.
 `CONDITIONAL`: that the one is the cause of the other (the `½log3` window, below `T*_{∞,P}`, also
 degrades, so the mechanism is not the whole story there).
4. **What a construction of `D` may not assume.** (`HEURISTIC` — *[amended per R155_025,
 E5/§7] a methodological warning, not a theorem; previously unlabelled.*) Nothing that treats the
 archimedean block as a positive reservoir to be spent survives past `T = 0.5958`. Together with
 Paper 46 `thm:SC` (positivity is collective in the comb) this pins the shape of any closing
 argument: the comb must be complete *and* the archimedean block must be treated as indefinite from
 `0.5958` on.

---

## §6 Labels

| statement | label |
|---|---|
| Thm 1(a) monotonicity of `λ^∞_min`, `λ^{∞,P}_min` | `PROVED` |
| Thm 1(b) `λ^∞_min ≥ 0` for `2T < log 2` | `PROVED` (by citation: Paper 42 / Yoshida / Bombieri; prime-free verification `phase-115/115_08`) |
| Thm 1(b) strict `> 0` | `CONDITIONAL` (Yoshida Lemma 2, volume not in `00-references`); self-contained bound only for `T ≲ 0.031`; numerically `+1.33·10⁻³` at `½log2` `DIAGNOSTIC` |
| Thm 1(c) `λ^∞_min ≤ λ^{∞,P}_min ≤ C₀ + φ((3π/2T)²)`, `< 0` for `T ≥ 0.74921`, `→ C₀` | `PROVED` (Paper 46 `cor:mono` / `thm:SC` at `A = 0`, proof re-read and shown to apply) |
| the order's `λ^{∞,P}_min ≤ λ^∞_min` | **`REFUTED`** (inclusion goes the other way; verified at 23 windows) |
| Thm 1(d) existence of `T*_∞`, `T*_{∞,P}` in `[½log2, 0.74921]` | `PROVED` |
| `T*_∞ = 0.3716`, `T*_{∞,P} = 0.5958` | `DIAGNOSTIC` (Galerkin `N = 18`, double precision, no enclosure) — *[amended per R155_025, E3]* **upper bounds** on the true thresholds, i.e. `T*_∞,true ≤ 0.3716`, `T*_{∞,P},true ≤ 0.5958` |
| Cor 2 (deficit `η`; the primes must cover it) | `PROVED` |
| `τ₀ = 6.28983599`, `m < 0` iff `|τ| < τ₀` | `PROVED` (monotonicity `lem:mbounds`(i)); the value `DIAGNOSTIC` |
| Prop 3(i) `n₋ ≥ 1` past the threshold | `PROVED` |
| Prop 3(ii) `n₋ ~ (2τ₀/π)T` | *[amended per R155_025, E5]* upper bound `n₋ ≤ 2Tτ₀/π + O(log T) + 2` `PROVED` (min–max); lower bound / asymptotic growth `HEURISTIC` (sketch, unquantified splitting) — previously mislabelled `PROVED (Landau–Widom, standard)`; not visible at `T ≤ 0.8` |
| §5.1 `β ≈ (2,0)` because the certificate only pays for the comb at `½log3` | `PROVED` (necessity, `prop:P`) + `OBSERVED` (the numbers) + *[amended per R155_025, E7]* the causal narrative ("the reason the optimum is near `(2,0)`") is `HEURISTIC`, not `PROVED` |
| §5.2 "`ν` reaches the inside comb only via `\|τ\| ≲ τ₀`" | *[amended per R155_025, E7]* **withdrawn / `HEURISTIC`** — `main.tex:1052,1070` combine inside and outside prime terms at all `τ`; only the need for new positivity past `0.5958` (Cor 2 + Prop 3) remains `PROVED` |
| §5.3 comb-vanishing failure explained by §5.2 | `CONDITIONAL` on `OBSERVED` numbers; the structural explanation itself demoted to `HEURISTIC` since §5.2 is withdrawn (E7) |
| §5.4 (what a construction of `D` may not assume) | `HEURISTIC` — *[amended per R155_025]* methodological warning, previously unlabelled |
| all table entries | `DIAGNOSTIC` |
| notation: prime quadratic form | *[amended per R155_025, E6]* renamed `Π_T` throughout, was colliding with subspace `P_T` |

**Endpoint of record unchanged.** No sign for `ζ` beyond `T ≤ log 2` is claimed. Nothing here is a
certificate; §3 is a Galerkin computation and gives *upper* bounds on `λ_min`, never lower ones.

---

## §7 What this changes in Paper 46 §8

Paper 46 is not edited. For the record, three things §8 could absorb later:

1. **`thm:SC` has a sharper companion at `A = 0`.** `thm:SC` gives `T₀(0) = 0.74921` as the window past
 which the *prime-free* form is negative on `P_T`. The true crossing is `T*_{∞,P} = 0.5958`, so the
 Song–Vondraček step loses `0.15` in `T` (`20 %`); and on all of `L²(−T,T)` the crossing is at
 `0.3716`. §8's reading "positivity is collective in the comb" gains a companion: *the archimedean
 block is indefinite from `0.5958` on, and every window Paper 46 cares about except `½log3` is past
 its own archimedean threshold* (`0.58` is below, `0.62`, `0.68`, `log2`, `0.75`, `0.80` are above).
2. **§8's "where the work is" acquires a number.** The deficit `η_P(T)` — `0` at `½log3`, `0` at `0.58`,
 `0.154` at `log2` — is the amount of positivity a certificate must *create* rather than *preserve*.
 The failure of every `T ≥ 0.62` run in `R155_005`/`R155_016` is on the creating side of that line;
 the success at `½log3` is on the preserving side. This is a cleaner explanation of the `½log3`/`0.58`
 gap than the `τ_env/2πe^{2T}` index of `R155_005` (`0.89` vs `2.4`), and it is `T`-monotone.
3. **`subsec:twoprime` should record that `0.58 < T*_{∞,P}`.** The best certified value at `0.58` is
 `−3.18·10⁻³` against a Galerkin upper bound `2.16·10⁻⁴` (Paper 46) — our independent Galerkin gives
 `+2.1552·10⁻⁴`, agreeing to three digits, and shows that `0.58` is still archimedean-positive
 (`+0.0274`), i.e. the `0.58` window is *not* yet the hard regime. The hard regime starts at `0.5958`.
