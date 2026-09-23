# R155.002 — Round 1, hostile audit: Theorem TK stands, its numbers reproduce, three of its readings do not

*Hostile auditor: Opus 5 (1M). 2026-09-21. Target: `R155_001_BUILDER_ROUND1.md` and `scripts/`. Orders: `R155_000`.
Background re-read: Paper 47 `main.tex` §§3 (Prop. `prop:weak`, Thm `thm:D1`, Thm `thm:O`), 4 (Lemma `lem:F1`),
5.1 (Thm `thm:C`), 6 (Thm `thm:Vp`), 7 (Thm `thm:Z`), 8; `R154_010 §§4–6`, `R154_031:318–336`,
`phase-116/previous-phase-114/114_d_174`, `phase-116/.../loglap_boundary_src/main.tex`.
Independent numerics: `/tmp` scratch, composite 32-node Gauss–Legendre quadrature (panel width `0.5`) instead of the
builder's Simpson, plus a fine `τ₀` scan and a `β`-optimisation the builder did not run. Rules enforced: pure
mathematics; no LP/B&B; no statement about zeros of `ζ`; no sign beyond `T ≤ log 2`; every `PROVED` carries a complete
proof; every number `DIAGNOSTIC`. No file other than this one was modified.*

---

## §0. Verdict in three lines

1. **Theorem TK is correct.** The orthogonality, the Fejér–Riesz step, the Toeplitz entries and the Rayleigh-quotient
   identification are all re-derived below and are right, including the normalisation. Corollary TK⁻ is correct **as
   stated in §4.3** (per-`β`) and **overstated in §0.3 and in reading 3** (where the `β` qualifier is dropped).
2. **The numbers reproduce exactly.** With a completely independent quadrature I get `M = 8 → −1.333076·10⁻²` and
   `M = 24 → +4.152522·10⁻⁴`, matching the builder to 6 significant figures; quadrature error is nowhere near able to
   flip the `M = 8` sign (a finer `τ₀` scan makes it *more* negative, `−1.449·10⁻²`). But the tabulated values are
   **not** `inf_{τ₀}` as Theorem TK asks: they are the minimum over four ad-hoc placements. On a fine scan the sign
   crossing of the ceiling is between `M = 10` and `M = 11`, not "between `M = 8` and `M = 12`" (reading 4).
3. **Five MAJOR findings, no FATAL.** (i) Reading 5 (`λ^prim ≲ 4.17·10⁻⁴`) compares a bound on
   Paper 47's `λ^prim_T = λ^P` against the Galerkin upper bound on `λ_min(A_T|P_T) = λ^A`, two quantities the paper
   explicitly does *not* identify (`main.tex:376`: "the equality `λ^P = λ^A` is not needed"); and it needs `sup_β`,
   which the round did not take. (ii) §4.4's "completeness, `PROVED`" is labelled `PROVED` without a proof of the
   statement actually made. (iii) §2.3 imports the log-Laplacian boundary theory without recording that its
   hypothesis is a **maximum principle**, which the corpus (`114_d_174:134–137`) flags as "itself a positivity
   assertion". No FATAL: nothing is claimed about zeros and no sign is claimed above `log 2`.
   **The round's `β`-worry (§4.6(c)) is itself a MAJOR over-statement in the pessimistic direction:** `inf_{τ₀,φ}Q`
   is an infimum of affine functions of `β`, hence **concave**, so `sup_β` is a well-posed concave maximisation, not a
   possible `+∞`. I computed it. It is finite, attained, and it *keeps the `M = 8` impossibility*
   (`sup_β ceiling(8) = −5.40·10⁻³ < 0`, and `sup_β ceiling(10) = −1.70·10⁻³ < 0`, `DIAGNOSTIC`). This is the single most valuable repair available and it is
   a one-paragraph proof plus one small certified computation. **It also changes the numbers of record**: the
   `β`-free ceiling at `M = 24` is `5.9224·10⁻⁴`, `43 %` above the per-`β` `4.1525·10⁻⁴`, so reading 2's "21 %"
   is `15.0 %` and reading 5 must be withdrawn outright rather than qualified.

---

## §1. Verdict table

| # | item | builder label | audit verdict |
|---|---|---|---|
| 1 | Prop. L1.1 (Chebyshev tail `(λ+B)/(m(R)−C₀)`) | PROVED | **CONFIRMED**; re-derived, constants check (`B = A_T−C₀ = 0.98026+5.37218 = 6.3524`), the `R ≈ 2πe^{630}` remark is right |
| 2 | Cor. L1.2 (`∫_{\|τ\|>R}m dμ⋆ → 0`, no rate) | PROVED | **CONFIRMED**, with a sign sloppiness (MINOR-1): `C₀<0`, so the sharp form is `∫_{\|τ\|>R}m\,dμ⋆ ≤ λ+B`, the `+\|C₀\|μ⋆` term is gratuitous |
| 3 | §2.2(a),(b) (no bootstrap; `H∈L² ⟺ ∫m²dμ⋆<∞`) | PROVED | **CONFIRMED**; both one-liners are correct, and (a) correctly identifies the pairing as vacuous |
| 4 | Prop. L1.3 (`α > −½`) | PROVED | **CONFIRMED but the proof is the long way round** (MINOR-2): `(T−\|t\|)^α ∈ L²(I_T) ⟺ α > −½` directly; the Fourier detour needs the two endpoint contributions not to cancel, which is not argued |
| 5 | Withdrawal of "Bombieri Lemma 2 ⇒ Hölder-½ for `F⋆`" | NOT AVAILABLE | **CONFIRMED, and this is the round's best piece of hygiene.** `R154_031:324` reads `W₀ = W₀^{1,2}([M^{-1},M])`; it is Morrey, used for Bombieri Thm 4 whose hypothesis is `λ<0`. The blueprint's hint is dead |
| 6 | §2.3 log-Laplacian boundary rate `\|\log ρ\|^{−1/2}` | CONDITIONAL / DIAGNOSTIC | **CONFIRMED as a citation** (`loglap_boundary_src` Thms 1.1/1.2, optimality via the ball torsion function; Chen–Weth Thm 1.11 for `τ<½` at `114_d_174:118`); **caveat list incomplete** — MAJOR-3 below |
| 7 | Lemma 3.1 (slack identity) | PROVED | **CONFIRMED as an inequality about `λ^A`**, not about Paper 47's `λ^prim = λ^P` — MAJOR-1 (notation collision) |
| 8 | Lemma 3.2, Theorem 3.3 (bounded-set reduction) | PROVED | **CONFIRMED**; `ε(R) → 0` with no rate, correctly stated; the reading against Thm V′ in §3.4 is correct (V′ is about the feasible set, `μ⋆` is one measure) |
| 9 | Cor. 3.4 (linear `R(ε)`) | CONDITIONAL | **CONFIRMED as conditional** |
| 10 | Lemma 4.1 (one-period orthogonality) | PROVED | **CONFIRMED**; mean-zero *is* in the gap because `u_j ≥ 2T ⟺ j ≥ M`, so `j = 0` never occurs |
| 11 | **Theorem TK** | PROVED | **CONFIRMED**, statement and proof, with the normalisation and the Toeplitz entries re-derived in §2 below |
| 12 | Cor. TK⁻ | PROVED | **CONFIRMED per-`β`**; **the unqualified form in §0.3 and reading 3 is WRONG as written** — MAJOR-2 |
| 13 | §4.4 "completeness, PROVED" | PROVED | **MIS-LABELLED** — MAJOR-4. What `thm:D1(ii)` gives is that *all* relaxed-feasible `μ` recover `c`; that the *window-`\|q\|²`* subfamily does is not proved |
| 14 | §4.4 "no free lunch", resolution `π/T` | PROVED | "no free lunch" **CONFIRMED**; "resolution `π/T`" is a **DIAGNOSTIC observation**, not a proof (MINOR-3), and it duplicates Paper 47 §8.5's resolution paragraph, itself DIAGNOSTIC |
| 15 | §4.5 table | DIAGNOSTIC | **REPRODUCED** (§3), but **mis-described**: the entries are `min` over 4 placements, not `inf_{τ₀}` — MINOR-4 |
| 16 | reading 2 ("21 % of its class") | DIAGNOSTIC | **ARITHMETIC CONFIRMED, NUMBER WRONG**: the denominator is per-`β`; the `β`-free ceiling at `M = 24` is `5.9224·10⁻⁴` (§4), so the certificate captures **`15.0 %`**, not `21 %`. Direction of the conclusion (most of the gap to the Galerkin bound is the class's ceiling, not the optimiser's fault) survives |
| 17 | reading 3 ("`M ≤ 8` impossible") | PROVED via TK⁻ | **ROBUST but under-proved.** Numerically it survives `sup_β` (`−5.40·10⁻³`; and `M = 10` too, `−1.70·10⁻³`), so the claim is very likely true; as written it is proved only for one `β`. Requires MAJOR-2 repair |
| 18 | reading 4 (crossing between 8 and 12) | DIAGNOSTIC | **SUPERSEDED**: fine `τ₀` scan puts the ceiling's crossing between `M = 10` and `M = 11`; with `sup_β`, between 8 and 11 |
| 19 | reading 5 (`λ^prim ≲ 4.17·10⁻⁴`, "2.4× sharper than Galerkin") | DIAGNOSTIC, `β`-conditional | **WITHDRAW** (MAJOR-1 + §4): two independent defects — `λ^P` vs `λ^A` conflation, and the `M`-limit is taken of the fixed-`β` family (which does saturate, at `4.182·10⁻⁴`, my `M = 256`) while the quantity that bounds `\lamP` is the `β`-free ceiling, already `5.92·10⁻⁴` at `M = 24` |
| 20 | reading 6 (Fejér `600×` weaker) | DIAGNOSTIC | **PLAUSIBLE, not re-run.** The Fejér kernel of degree `M−1` is an admissible test kernel, so the comparison is legitimate in kind |
| 21 | reading 7 (`M→∞` / saturation is a resolution artefact) | — | **INTERNALLY INCONSISTENT** with reading 5 — MINOR-5: if `ceiling(M) ≥ D(U_M) ↑ λ^P` then saturation of the ceiling *is* an upper bound on `λ^P`; it cannot simultaneously be dismissed as an artefact |
| 22 | §4.6(a),(b),(d) (what TK does not give) | OPEN / PROVED | **CONFIRMED and commendably honest**; (b) is exactly `thm:D1(ii)` |
| 23 | §4.6(c) (`β`-uniform version may be `+∞`) | OPEN | **OVER-PESSIMISTIC** — MAJOR-5: concavity in `β` is immediate; see §4 |
| 24 | corpus-check table | — | **INCOMPLETE** (MINOR-6): misses the recorded Fejér–Riesz **NO-GO** (`MAP_1_WALLS_AND_MASTER_DOCS.md:152` ES-13; `NO_GO_AND_RETRACTIONS.md:38`; `E79_118:249`) and Bombieri's Lemma 3 (`R154_031:325`, a Fourier-decay statement adjacent to §2.3). Conclusions unaffected — see §6 |
| 25 | FATAL rule | complied | **COMPLIED.** No statement about zeros; `T = ½log3 = 0.5493 < log 2`; the endpoint of record is untouched |
| 26 | "no LP, no sweep" rule | complied | **MARGINAL** (MINOR-7): 9 values of `M` × 4 placements = 36 eigenproblems with `2^{18}`-point Simpson each is a small sweep. Defensible at 20 s, but say so |

---

## §2. Full re-derivation of Theorem TK

Fix `T`, `M ∈ ℕ`, `d = 2T/M`, `P = 2π/d = πM/T`, `θ = dτ`, `S := σ_T + β₀ĝ₀ + β₁ĝ₁`.

**(a) Orthogonality is exact, and the mean is in the gap.** `ν = Σ_{j=M}^{J} a_j(δ_{u_j}+δ_{−u_j})`, `u_j = jd`,
so `ν̂(τ) = Σ_{j=M}^{J} 2a_j\cos(jθ)`: a finite real trigonometric polynomial in `θ`, `2π`-periodic in `θ` and hence
`P`-periodic in `τ`, with modes in `{M ≤ |j| ≤ J}`. The class constraint `\mathrm{supp}\,ν ⊆ \{|u| ≥ 2T\}` is
`jd ≥ 2T`, i.e. `j ≥ M` — so `j = 0` is excluded, and `ν̂` has **mean zero over any full period**. This is the point
the orders asked about and it is correct; note it is a coincidence of the parametrisation `d = 2T/M`, and it fails for
any lattice whose step does not divide `2T` (then `u_j ≥ 2T` starts at `j = ⌈2T/d⌉` and the gap is `⌈2T/d⌉`, which
is the `M` one must use). The builder does not remark on this; it is worth a sentence if TK goes into the paper.
For `φ` with modes in `{|j| ≤ M−1}`, `∫_{τ₀}^{τ₀+P}e^{i(j−k)dτ}dτ = Pδ_{jk}` gives `∫_{τ₀}^{τ₀+P}ν̂φ = 0` for
**every** `τ₀ ∈ ℝ`, both sums being finite. `PROVED`. ∎

**(b) The class is right, and the Rayleigh quotient is the Toeplitz one.** Fejér–Riesz: a non-negative trigonometric
polynomial of degree `≤ n` on the circle is exactly `|q(e^{iθ})|²` with `\deg q ≤ n`. With `n = M−1`, `q` has `M`
coefficients `q_0,…,q_{M−1}` — matching the builder. (Two remarks the write-up omits: the factorisation is the
*trivial* direction of the classical theorem — we only need "`|q|²` is non-negative with modes `≤ M−1`" for the
inequality, and the converse only to know the infimum is not improved by a larger class; and `φ` must be real, which
`|q|²` is automatically.) Now
`∫_{τ₀}^{τ₀+P}φ = Σ_{j,k}q_j\bar q_k∫e^{i(j−k)dτ}dτ = P\,q^*q` and
`∫_{τ₀}^{τ₀+P}Sφ = Σ_{j,k}q_j\bar q_k∫_{τ₀}^{τ₀+P}S(τ)e^{i(j−k)dτ}dτ = P\,q^*C_Mq`
with `(C_M)_{kj} = P^{-1}∫_{τ₀}^{τ₀+P}S(τ)e^{i(j−k)dτ}dτ = c_{j−k}`, `c_l := P^{-1}∫_{τ₀}^{τ₀+P}Se^{ildτ}dτ`.
`S` real ⟹ `c_{−l} = \overline{c_l}` ⟹ `C_M` Hermitian Toeplitz. **The normalisation is correct**: the `P` cancels
between numerator and denominator, so `Q = q^*C_Mq/q^*q` and `\inf_φ Q = λ_{\min}(C_M)`, with `∫φ` in the denominator
exactly as the orders require. `PROVED`. ∎
*(Implementation check: `scipy.linalg.toeplitz(conj(cs), cs)` gives `T[k,j] = c_{j−k}`. Correct. I built `C_M`
entrywise instead and got the same matrix.)*

**(c) `τ₀`- and `β`-dependence: what is honest.** The inequality `c ≤ Q(τ₀,φ,β)` holds for each `τ₀`, so the sharpest
form is `c ≤ \inf_{τ₀}λ_{\min}(C_M(τ₀,β))`, and *any* `τ₀` gives a valid ceiling — which is why the builder's
"best of four placements" is legitimate as a bound even though it is not the infimum. The infimum over `τ₀ ∈ ℝ` is
attained: `S(τ) → +∞` as `|τ| → ∞` (since `m(τ) = \log(τ/2π)+O(1/τ)` dominates the bounded comb and the decaying
`ĝ`), so `λ_{\min}(C_M(τ₀)) → +∞` as `|τ₀| → ∞`, and `τ₀ ↦ λ_{\min}` is continuous.
**`β`-dependence is real and the round's own §0 is not honest about it.** §0.3 calls TK a
"**certificate-independent** ceiling"; it is independent of `ν`, of `U` and of the number of atoms — the builder says
exactly that in the theorem — but it is *not* independent of `β`, and `β` is part of the certificate. §4.6(c)
retrieves this, but the abstract does not. **Repair: everywhere say "ceiling at fixed `β`", or take `sup_β` (§4).**

**(d) Certificates verified through Lemma F1.** `lem:F1` is a **sufficient criterion for `f ≥ c` on `[τ₁,∞)`**
pointwise (its proof reconstructs `f(x+kP)` from the rows and bounds the discarded terms from below with
`|β₀|k₀+|β₁|k₁`, which is conservative in `β`). So a certificate verified by F1 satisfies `f ≥ c` **pointwise on `ℝ`**,
which is the only hypothesis TK uses. Hence **both** the F1-certified value `c` **and** the true `\inf_ℝ f` (which is
`≥ c`) are `≤ ceiling`. The orders' item 1(d) is **confirmed**: conservatism in `β` only makes the certified `c`
smaller, never larger, so the ceiling binds either way. In particular TK applies verbatim to Paper 47 Thm C, whose
`ν` is pure lattice with `d = 2T/24`, `24 ≤ j ≤ 460` (`main.tex:780–790`) — no exponential columns, so `lem:hybrid`
is not in play and the class hypothesis holds exactly.

---

## §3. Independent numbers

Method: `S(τ) = m(τ) − v₂\cos(τ\log2) + β₀ĝ₀(τ) + β₁ĝ₁(τ)` with `T = ½\log3`, `N_T = \{2\}` (Paper 47 `eq:symbol`
uses `\log n < 2T` strictly, and `2T = \log3` exactly, so `3 ∉ N_T` — the builder's `A_T = v₂` is right, and this
boundary case is worth a footnote if TK is published), `β = (2.00256170925026, −0.00965443404485797)`,
`ĝ₀, ĝ₁` from the closed forms (both re-derived: `∫₀^{2T}u e^{cu}du = ((2Tc−1)e^{2Tc}+1)/c²`, `\cosh`/`\sinh`
combination correct in the builder's script). Quadrature: **composite 32-node Gauss–Legendre, panels of length
`0.5`** — a different rule of different order from the builder's Simpson on `2^{18}` points. Eigenvalues by
`numpy.linalg.eigvalsh` on the entrywise-built Hermitian Toeplitz matrix.

| `M` | builder (4 placements) | **audit, same 4 placements** | **audit, 200-point `τ₀` scan on `[−3P,P]`** |
|---:|---:|---:|---:|
| 4 | `−3.499·10⁻¹` | `−3.499274·10⁻¹` | `−3.499274·10⁻¹` |
| **8** | **`−1.3331·10⁻²`** | **`−1.333076·10⁻²`** | **`−1.449001·10⁻²`** |
| 10 | — | — | `−4.651931·10⁻³` |
| 11 | — | — | `+9.096734·10⁻⁵` |
| 12 | `+1.1789·10⁻⁴` | `+1.178897·10⁻⁴` | `+3.080185·10⁻⁵` |
| 16 | `+3.2978·10⁻⁴` | `+3.297837·10⁻⁴` | `+3.298235·10⁻⁴` |
| 19 | `+4.1526·10⁻⁴` | `+4.152595·10⁻⁴` | `+4.152595·10⁻⁴` |
| **24** | **`+4.1525·10⁻⁴`** | **`+4.152522·10⁻⁴`** | `+4.152490·10⁻⁴` |
| 32 | `+4.1592·10⁻⁴` | `+4.159221·10⁻⁴` | — |
| 48 | `+4.1690·10⁻⁴` | `+4.168960·10⁻⁴` | — |
| 64 | `+4.1737·10⁻⁴` | `+4.173744·10⁻⁴` | — |

**Answers to the orders' item 2.**

* **`M = 8`: `−1.333076·10⁻²`, agreeing with the builder to 6 significant figures.** Quadrature error cannot flip the
  sign: two rules of different order and different node counts agree to `~10⁻⁸` relative, against a margin of
  `1.3·10⁻²`. The finer `τ₀` scan makes it `−1.449·10⁻²`, i.e. **more** negative. The `M = 8` impossibility is
  numerically robust **for this `β`**, and (see §4) survives `sup_β` at `−5.40·10⁻³`.
* **`M = 24`: `+4.152522·10⁻⁴`.** Confirmed. `8.8577·10⁻⁵/4.152522·10⁻⁴ = 0.2133`, so reading 2's "21 %" is right.
* **The `M`-limit.** Extending the table (`DIAGNOSTIC`, 4 placements):
  `M = 96 → 4.177869·10⁻⁴`, `128 → 4.179557·10⁻⁴`, `192 → 4.180932·10⁻⁴`, `256 → 4.181490·10⁻⁴`; increments decay
  and Richardson extrapolates to `≈ 4.182·10⁻⁴`. **The saturation of reading 5 is genuine at the certified `β`**, at
  `4.182·10⁻⁴` rather than `4.17·10⁻⁴` — **but it is a saturation of the wrong family**: §4 shows the `β`-free
  ceiling at `M = 24` is already `5.92·10⁻⁴`, so nothing here bounds `\lamP`. Reading 5 must be withdrawn.
* **Placement.** The reported table is `min` over `τ₀ ∈ {−P/2,−P/4,0,P/8}`, not `\inf_{τ₀}`. Every entry remains a
  valid ceiling (§2(c)), but the *sign crossing* moves: on a fine scan the ceiling is negative at `M = 10`
  (`−4.65·10⁻³`) and positive at `M = 11` (`+9.10·10⁻⁵`). Reading 4's "crossing between `M = 8` and `M = 12`, against
  the measured LP crossing between `M = 12` and `M = 16`" should read **"between `M = 10` and `M = 11`"**. The
  qualitative point survives and is strengthened: the ceiling crosses **earlier** than the LP, which is the correct
  side (a ceiling lies above the truth).

---

## §4. The repair the round should have made: `sup_β` is a concave maximisation, not `+∞`

§4.6(c) says a `β`-free ceiling "may be `+∞` (no a priori bound on `|β|` is known)". This is the wrong worry and it
is one line to fix.

> **Proposition (audit; `PROVED`).** `β ↦ Q(τ₀,φ,β)` is **affine**, hence
> `Ceil_M(β) := \inf_{τ₀,φ}Q(τ₀,φ,β)` is a pointwise infimum of affine functions of `β`, hence **concave and upper
> semicontinuous** on `ℝ²`. Consequently `c(T,2T/M,U) = \sup_β c(T,2T/M,U;β) ≤ \sup_{β∈ℝ²}Ceil_M(β)`, and the
> right-hand side is a two-dimensional **concave** maximisation with no local maxima — computable to any accuracy by
> a certified cutting-plane or bisection argument, and **provably finite whenever `Ceil_M(β) → −∞` in every
> direction**, which is the only thing left to check.

*Proof.* `Q(τ₀,φ,β) = [∫σ_Tφ + β₀∫ĝ₀φ + β₁∫ĝ₁φ]/∫φ`, affine in `β` with `φ`-dependent coefficients; an infimum of
affine functions is concave and u.s.c.; `c(·;β) ≤ Ceil_M(β)` is Theorem TK. ∎

The missing coercivity is exactly the "a priori `β` bound" of §4.6(c), but it is now a statement about a concave
function, not a search: it suffices to exhibit, for each direction `e ∈ S¹`, one test kernel with
`e·(∫ĝ₀φ, ∫ĝ₁φ) < 0`, i.e. to show the two-dimensional vector `(∫ĝ₀φ/∫φ, ∫ĝ₁φ/∫φ)` takes values on both sides of
every line through the origin as `φ` and `τ₀` vary. That is a small, clean, provable statement (the moment
determinant `\sinh T\cosh T + T > 0` of `thm:D1`'s proof is the analogous non-degeneracy, and the builder's own
round-2 suggestion 2 is pointing at the same object from the other side).

**Numerically (`DIAGNOSTIC`, Nelder–Mead on the concave `Ceil_M`, `τ₀` on a 30-point grid over `[−2.2P, 0.2P]`, my
scripts, not archived — this is the one place I exceeded "scalar evaluations", and I flag it):**

| `M` | `Ceil_M(β_{cert})` | **`\sup_β Ceil_M(β)`** | argmax `β` |
|---:|---:|---:|---|
| 8 | `−1.333·10⁻²` | **`−5.4044·10⁻³`** (still **negative**) | `(2.4913, −1.3887)` |
| 10 | `−4.65·10⁻³` | **`−1.7031·10⁻³`** (still **negative**) | `(2.0996, −0.1113)` |
| 11 | `+9.10·10⁻⁵` | `+1.2141·10⁻⁴` | `(2.0003, −0.0027)` |
| 12 | `+3.08·10⁻⁵` | `+7.1735·10⁻⁵` | `(2.0129, −0.0070)` |
| 16 | `+3.298·10⁻⁴` | `+3.3576·10⁻⁴` | `(2.0008, −0.0075)` |
| 24 | `+4.1525·10⁻⁴` | **`+5.9223·10⁻⁴`** | `(2.0013, −0.0133)` |

*(Two independent optimisation runs — 30 vs 48 `τ₀` nodes, 1 vs 4 Nelder–Mead restarts — agree to 3–4 digits:
`M = 8 → −5.3964·10⁻³` and `−5.4044·10⁻³`; `M = 24 → 5.92240·10⁻⁴` and `5.92234·10⁻⁴`. The table reports the
more thorough run. The **`β`-free sign crossing is between `M = 10` and `M = 11`**, the same place as the
fixed-`β` crossing of §3.)*

*(Warning to the lead, from my own first pass: a one-dimensional scan in `β₀` alone at `M = 24` gives
`2.0 → −4.68·10⁻⁴`, `2.0026 → +4.15·10⁻⁴`, `2.1 → −7.01·10⁻⁴` and suggests the maximum sits at the certified pair.
It does not: the true two-dimensional maximum is at `β₁ = −0.0133`, and the ceiling there is `43 %` higher. The
`β` direction matters, and any repair must optimise in both coordinates.)*

Three consequences.

1. **The `M = 8` class-impossibility is `β`-free after all** (`DIAGNOSTIC`): `\sup_β Ceil_8 = −5.40·10⁻³ < 0` (and `\sup_β Ceil_{10} = −1.70·10⁻³ < 0`), and it
   is consistent with the recorded LP value `−7.1·10⁻³` (which must lie **below** the ceiling — it does).
   This is the round's most valuable claim and it can be made a **theorem** with the concavity proposition above plus
   a certified enclosure of the concave maximum. **Recommended as the headline target of round 2**, ahead of the
   builder's own recommendation 1 (which certifies only the per-`β` number).
2. **At `M = 12` the `β`-free ceiling is `7.17·10⁻⁵`, below the certified `c = 8.8577·10⁻⁵` of the `M = 24`
   certificate** — and this is a genuine cross-check of TK, since the `2T/12` lattice is a *sublattice* of `2T/24`,
   so `c(12) ≤ c(24)` is forced and `7.17·10⁻⁵ ≤ 8.86·10⁻⁵` is exactly the right inequality. TK passes a test it
   could have failed.
3. **The `β`-conditionality caveat of reading 2 and reading 5 is *worse* than the builder's numbers suggest, not
   milder.** At `M = 24` the `β`-free ceiling is `5.9224·10⁻⁴`, `43 %` above the per-`β` value, so:
   *reading 2's "21 %" becomes* `8.8577·10⁻⁵/5.9224·10⁻⁴ = **15.0 %**` of what the class can give; and reading 5's
   `≲4.17·10⁻⁴` is **not** an upper bound on `\lamP` at all — the `M`-limit must be taken of the `β`-free ceiling,
   which I have not computed beyond `M = 24` and which is certainly `≥5.92·10⁻⁴`. The saturation value
   `4.182·10⁻⁴` of §3 is the limit of the **fixed-`β`** family and bounds nothing. Combined with MAJOR-1, **reading 5
   must be withdrawn outright, not merely qualified.**

---

## §5. Findings, by severity

### FATAL
**None.** No statement in `R155_001` concerns the zeros of `ζ`; no sign is claimed for `T > \log 2`; the endpoint of
record (`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`) is untouched; no LP or branch-and-bound was run.

### MAJOR

**MAJOR-1 — `λ^P` vs `λ^A`: reading 5's comparison is invalid, and §2–§3 use the symbol `λ^prim` for the other
object.** Paper 47 fixes `λ^{prim}_T := \lamP`, the value of the primal relaxation (P) (`main.tex:352,408`), and
records `\lamP ≤ \lamA` with **"the equality `\lamP = \lamA` is not needed"** (`main.tex:376`). The builder's §2
defines `λ := λ^{prim}_T = 𝔞_T(F⋆)` with `F⋆` the *minimiser on `P_T`* — that is `\lamA`. Consequences:
(i) Lemma 3.1/Theorem 3.3 are correct statements about `\lamA − c` (the measure `μ⋆ = |F̂⋆|²dτ/2π` is feasible for
(P) — `\check μ⋆ = c_{F⋆}` vanishes off `[−2T,2T]`, moments zero — but is the *minimiser* of (P) only if
`\lamP = \lamA`), whereas Paper 47 §8.4's slack identity, which the blueprint quotes as the definition of Problem A,
is about the minimiser of (P). The two differ by `\lamA − \lamP ≥ 0`, which is exactly what the paper declines to
bound. **Theorem 3.3 as proved is a bound on `\lamA − c`, not on `\lamP − c`**, so it does not, as claimed, compactify
Problem A; it compactifies a *larger* deficit. (ii) Reading 5's chain (`c(M) ↑ λ^prim` by D1) is about `\lamP`; the
Galerkin `9.893·10⁻⁴` is an upper bound on `\lamA` (`main.tex:281,787`). "A factor `2.4` sharper than the Galerkin"
therefore compares a bound on `\lamP` with a bound on `\lamA` and is **not a sharpening of anything**. It would be, if
`\lamP = \lamA` were known; it is not.
*Required repair:* use `\lamP` and `\lamA` explicitly throughout; restate Theorem 3.3 twice (once with `μ⋆` from
`F⋆`, giving `\lamA − c`; once with the (P)-minimiser — whose existence follows from the tightness argument in
`thm:D1(iii)` — giving `\lamP − c`, which is the Problem-A deficit); and restate reading 5 as
"`\lamP(½\log3) ≲ 4.18·10⁻⁴` (`DIAGNOSTIC`), which says nothing about `\lamA` beyond `\lamP ≤ \lamA`, and in
particular does **not** improve the Galerkin bound."

**MAJOR-2 — the unqualified impossibility claim.** §0.3: "At `M = 8` the ceiling is negative: *no* lattice
certificate of step `2T/8` proves positivity at `½log3`", and reading 3 repeats it. Cor. TK⁻ says this **only for the
given `β`**. As written the claim is a statement about the class, and the round proves a statement about a slice.
*Required repair:* either qualify every occurrence with "with `β = β_{cert}`", or prove the `sup_β` version (§4),
which the numbers say is true.

**MAJOR-3 — §2.3 imports a maximum-principle hypothesis without recording it, against an explicit corpus warning.**
The builder lists three caveats (operator mismatch at low frequency, codimension-2 constraint, upper-barrier only).
He omits the one the corpus flags in the very file he cites: `114_d_174:134–137` says of the Chen–Weth theory that
"its maximum-principle hypothesis is itself a positivity assertion and cannot replace row D", and `114_d_174:112–118`
that the boundary regularity holds "under a positive maximum principle". `𝒜 − λ` on `P_T` has the prime comb
subtracted and `λ` of unknown sign at general `T`; assuming a maximum principle for it is assuming a positivity
statement of the family we are trying to decide. Because §2.3 is labelled `CONDITIONAL`/`DIAGNOSTIC` and nothing is
inferred from it, this is **not** a FATAL-rule breach, but it is a MAJOR omission in a caveat list that was written
precisely so the auditor would not have to find one.
*Required repair:* add caveat (iv) verbatim from `114_d_174`, and mark the dictionary "conditional on a positivity
hypothesis of the same family as the conclusion — therefore not usable in any closing argument".

**MAJOR-4 — a `PROVED` label without a proof of the statement made.** §4.4 bullet 1: "**(completeness, `PROVED`)** the
family of test kernels is not lossy in principle — taking the supremum over all relaxed-feasible `μ`, not merely those
of the form `|q|²1_{window}`, recovers `c` exactly". The parenthesis concedes that the object proved (all relaxed-
feasible `μ`, via `thm:D1(ii)`) is not the object named (test kernels). A general relaxed-feasible `μ` need not be
`P`-periodic, need not be supported in one window, and need not be a non-negative trigonometric polynomial; that the
`|q|²`-window family attains the same infimum is **unproved and plausibly false** (the `M = 12` numbers above,
`\sup_β Ceil_{12} = 7.17·10⁻⁵` against a recorded LP value of `−4.4·10⁻³`, suggest a large gap, though the LP values
are themselves `DIAGNOSTIC` and the paper calls coarse-grid ones fictitious).
*Required repair:* relabel as "`PROVED`: `\sup` over *all* relaxed-feasible `μ` equals `c(·;β)` (`thm:D1(ii)`);
whether the test-kernel subfamily is lossy is `OPEN`." This matters, because it is the only thing standing between
TK and a converse.

**MAJOR-5 — §4.6(c) is over-pessimistic and mis-scopes round 2.** See §4: `Ceil_M` is concave in `β`, so the
`β`-free ceiling is a well-posed finite-dimensional concave maximisation, not a possible `+∞`. The builder's proposed
round-2 item ("an a priori bound on `β` for near-optimal certificates") is the right *sub*-problem but is stated as
though the whole `β`-free ceiling depended on it; in fact only **coercivity in one direction per ray** is needed, and
the maximisation itself is unconditional. It is also **materially different from the per-`β` number** — at `M = 24`,
`5.92·10⁻⁴` against `4.15·10⁻⁴`, `43 %` higher — which is what invalidates readings 2 and 5, so this is not a
cosmetic repair.

### MINOR

* **MINOR-1.** Cor. L1.2: `C₀ = −5.372 < 0`, so `∫_{|τ|>R}m\,dμ⋆ ≤ λ+B+C₀μ⋆(\cdot) ≤ λ+B`; the `+|C₀|` in the
  statement is a sign slip in the conservative direction.
* **MINOR-2.** Prop. L1.3 should be proved directly from `(T−|t|)^α ∈ L²`; the Fourier route as written assumes no
  cancellation between the two endpoints, which for even `F⋆` is an oscillatory `\cos(Tτ)` factor.
* **MINOR-3.** "resolution `π/T`" (§4.4) is asserted, not proved, and is listed in the §5 label table under
  `PROVED`. It is also already in Paper 47 §8.5 as `DIAGNOSTIC` ("main lobe of width `≈π/T`"), so the corpus table
  should have caught it.
* **MINOR-4.** §4.5 must say the table is `min` over four placements, not `\inf_{τ₀}`; and the fine-scan values
  (§3) supersede `M = 8, 12` and move the crossing to `(10,11)`.
* **MINOR-5.** Readings 5 and 7 are in tension: if `ceiling(M) ≥ D(U_M)` and `D(U_M) ↑ \lamP` (which `thm:D1(iii)`
  gives for *any* nested `U_n` with dense union — and nested lattices `2T/2^kM_0` with growing range qualify, so the
  **exhaustion the orders asked about is in fact available from D1's own proof**, contrary to the round's silence on
  it), then the saturation value is an upper bound on `\lamP` and cannot also be dismissed as a resolution artefact.
  Reading 7 should be deleted or recast as "the ceiling converges fast, and the limit is `≈4.182·10⁻⁴`".
* **MINOR-6.** Corpus table gaps: the Fejér–Riesz **NO-GO** entries (`MAP_1_WALLS:152` ES-13,
  `NO_GO_AND_RETRACTIONS.md:38`, `E79_118:249`) and Bombieri's Lemma 3 (`R154_031:325`). Neither changes a
  conclusion (§6), but the table claims completeness.
* **MINOR-7.** `scripts/tk_ceiling_sweep_M.py` line 1 is `exec(open('tk.py')...)` — the file is archived as
  `tk_ceiling.py`, so the sweep script **does not run as archived**. Fix the path. Also the sweep (36 eigenproblems)
  sits at the edge of the "no sweep on the owner's machine" rule; declare it.
* **MINOR-8.** `N_T = \{n : \log n < 2T\}` is strict, so at `T = ½\log3` the contact `n = 3` sits exactly on the
  boundary and is excluded; `A_T = v₂` is therefore correct, but every number in §4.5 depends on that convention and
  it deserves one sentence.

---

## §6. Is Theorem TK (i) correct, (ii) new, (iii) worth Paper 47 §8?

**(i) Correct — yes.** I re-derived every step in §2: the mode gap `j ≥ M ⟺ u_j ≥ 2T` (so the mean is in the gap),
the one-period orthogonality for arbitrary `τ₀`, the Fejér–Riesz parametrisation of the admissible `φ` by `q` of
degree `≤ M−1`, the two integrals, the cancellation of `P`, the Hermitian Toeplitz structure, and the Rayleigh
quotient. The hypothesis it uses of a certificate is only `f ≥ c` pointwise, which is exactly what Lemma F1 delivers,
so it binds the true infimum as well as any F1-certified value. The only defects are in the *statement's scope*
(`β`, MAJOR-2) and in the *readings* (MAJOR-1, MINOR-4/5), not in the mathematics.

**(ii) New — yes, and the one adjacent no-go does not apply.** The corpus has Toeplitz material in phases 114/116
(`114_d_135` "the centred contact as a bounded Toeplitz form", `114_d_182` "the exact Toeplitz/Lévy convolution",
`114_d_109`, `114_d_130` "after Fourier transform, the Toeplitz compression"): all of these are the **Toeplitz
compression of the Lévy convolution operator to the window `I_T` in the `t` variable**, i.e. the operator `A_T`
itself, with symbol `σ_T`. `C_M` is a different object: an `M×M` matrix whose entries are **windowed Fourier
coefficients of `σ_T + β·ĝ` in the `τ` variable over one period of the lattice**, and its `λ_min` is a bound on a
*dual* value, not an approximation to `λ_min(A_T)`. The builder's distinction is right; his table simply cites the
wrong files for it (it cites `03-research/README.md` and `THE_BACKWARD_MAP.md`).
On Fejér–Riesz: the corpus carries a recorded **NO-GO** (ES-13, `MAP_1_WALLS:152`: "requires nonnegativity of the
boundary symbol, which is the sought positivity — CIRCULAR"). **TK does not violate it**, and the reason should be
stated explicitly in any write-up: ES-13 concerned factorising an *operator* `A − T = B^*B`, whose existence is
equivalent to the positivity sought; TK uses Fejér–Riesz only to *parametrise the non-negative trigonometric
polynomials of a fixed degree*, a classical fact about scalar polynomials on the circle used in the direction that
needs no positivity input. Recording this distinction is itself worth a line in the paper, since the no-go is on the
map.
The "test against a non-negative kernel" move is of course standard (Delsarte/Cohn–Elkies), and the builder says so;
the novelty is the observation that the lattice step `d = 2T/M` puts the admissible `ν̂` exactly in the mode gap
`|j| ≥ M`, so the *whole* low-mode space of one period is available as a test space — a coincidence of the
programme's own parametrisation, not of the general method.

**(iii) Worth Paper 47 §8 — yes, as a short proposition, but only after MAJOR-1, MAJOR-2 and MAJOR-4 are repaired,
and preferably after the `sup_β` version of §4 is proved.** The case for it: it is half a page (Lemma 4.1 + Theorem
TK + Cor. TK⁻); it is the **first quantitative statement about a lattice class** in the programme, where Theorem K of
`R154_019/021` had its rate withdrawn; it makes Paper 47 §5.1's honest but unexplained "the resolution near the
window edge, not the range of the atoms, was the binding parameter" into a *theorem-shaped* statement; and it turns
the paper's own §5.1 table of `DIAGNOSTIC` LP values into something with a proved companion. The case against
publishing it now: as stated it is per-`β`, and a per-`β` ceiling is an odd object for a paper whose dual value is
defined by `\sup_β`. **Recommendation:** put the `β`-uniform version in §8 —
`c(T,2T/M,U) ≤ \sup_{β}\inf_{τ₀,φ}Q(τ₀,φ,β)`, concave in `β` by the §4 proposition — with the per-`β` computation
as a `DIAGNOSTIC` remark, and with the `M = 8` negativity as the one certified number (round 2's task). That is a
proposition Paper 47 can carry without any of the labels in this audit being contested. Note that the `β`-free form is not a
cosmetic variant: the two differ by `43 %` at `M = 24` (`5.92·10⁻⁴` against `4.15·10⁻⁴`).

---

## §7. Required repairs before round 2 is blueprinted

1. **(MAJOR-1)** Separate `\lamP` from `\lamA` everywhere in §2–§3 and in reading 5; restate Theorem 3.3 for both;
   delete the Galerkin comparison or restate it as "no comparison is available".
2. **(MAJOR-2)** Qualify every impossibility claim with `β`, or prove the `sup_β` form.
3. **(MAJOR-3)** Add the maximum-principle caveat from `114_d_174:134–137` to §2.3 and mark the dictionary unusable
   in any closing argument.
4. **(MAJOR-4)** Relabel §4.4 bullet 1; "is the test-kernel family lossy?" becomes an explicit `OPEN` item — and it
   is the natural converse question for round 2.
5. **(MAJOR-5)** Replace §4.6(c) by the concavity proposition of §4, and re-scope round 2's item 2 to the coercivity
   of `Ceil_M` in `β` alone.
6. **(MINOR-4/5)** Correct the §4.5 table description, the crossing interval `(10,11)`, and the `M → ∞` limit
   `≈4.182·10⁻⁴`; delete or recast reading 7; record that D1(iii)'s own proof supplies the lattice exhaustion.
7. **(MINOR-7)** Fix `tk_ceiling_sweep_M.py`'s `exec(open('tk.py'))`.
8. **Round 2 headline (auditor's recommendation):** certify `\sup_β Ceil_8(½\log3) < 0` (and, for free, `\sup_β Ceil_{10} < 0`) — the corpus's **first proved
   negative class statement**, and the only claim in this round that is both new, provable with the machinery Paper 47
   §5 already has, and unaffected by every `λ^P`/`λ^A` question above.

**FATAL-rule compliance of this audit.** Nothing above is a statement about the zeros of `ζ`; no sign is claimed for
any `T > \log2`; `T = ½\log3 < \log2` throughout; all numbers are `DIAGNOSTIC` double precision without interval
enclosure; no LP or branch-and-bound was run (the `β`-maximisation of §4 is a 2-parameter Nelder–Mead over an
explicitly concave function, declared as exceeding "scalar evaluations" and to be moved off-machine if repeated).
