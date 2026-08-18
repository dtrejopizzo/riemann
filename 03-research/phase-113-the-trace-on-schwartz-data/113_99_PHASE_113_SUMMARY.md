# 113.99 — Phase 113 summary

## Verdict

> **Row (d) of Weil's programme is complete over `Spec Z` except for one
> statement, and that statement is the Riemann Hypothesis itself.**
>
> Phase 113 moved the Weil pairing onto Schwartz data, computed its radical,
> and showed the resulting object is a commutative Frobenius `*`-algebra
> `(D/rad, ⋆, *, τ)` with a **zero-free** trace, two rulings realised by candid
> functions, a `Z`-valued divisor map, a degree map, an effective cone,
> Serre duality and `K = 0`. Of the backward map's six requirements
> d0–d5, **four that had never been attempted are now built** (d0, d2, d4, d5,
> plus `K = 0`), **d1's analytic half is closed** (`rad I_∂` = the `χ`-ideal,
> `χ(s) = s(s−1)ξ(s)`), and **d3 is proved impossible inside `D`**.
>
> The residue is not a gap that further work might close from this side:
> 113_10 Thm 4.2/4.3 and 113_12 Thm 4.1 prove that the missing effectivity
> statement `(E°)` and the Hodge index inequality on `H^⊥` are each
> **equivalent to RH**. Therefore **row (d) is not a route to RH. Row (d) is
> RH.** **RH is not proved.**

---

## 1. What the phase was launched to do, and what happened instead

The phase was opened to answer one question inherited from phase 108: does the
identity-value obstruction (`χ(1) = 1` forcing divergence for the graded
family) resurface for Schwartz data?

**113_01–113_04 answered it, and the answer was sharper than the question.**
113_01 Thm 4.1: `h(1) = 0` is not what one regularization scheme needs, it is
what *every* scheme needs in order to agree with every other — two explicit
schemes (raw shell truncation; Laurent finite part of the local zeta integral)
differ by exactly `h(1)/2` at every prime. Unlike phase 108, where `h(1) = 1`
was forced because every element of the graded family is a quasi-character,
here `h = f ⋆ g̃` is built from two free functions and `h(1) = 0` is one linear
condition on the pair.

**113_05–113_07 then dissolved the condition entirely.** Once the pairing is
written in the canonical Weil decomposition (113_06 Def 2.1) on the balanced
profile class `D` (113_07 Def 1.3), no admissibility side condition and no
renormalisation survive: `h(1) = 0` turned out to be both *impossible* to
impose on the ξ-divisible class and *unnecessary* (113_07 §3). What was
supposed to be the phase's central risk became a non-issue, and the phase's
real content turned out to be row (d).

## 2. The objects

- **`D`** = `∪_{θ>3/2} D_θ`, defined by decay of the balanced profile
  `F(x) = e^{x/2} f(e^x) ∈ S_θ`; `f̂(s) = F̂(s − ½)`; `D°` = the balanced
  subspace `{f̂(0) = f̂(1) = 0}` (113_07 Def 1.3).
- **The pairing**
  `𝔰(x,y) = x̂(0)·conj ŷ(1) + x̂(1)·conj ŷ(0) − Σ_ρ m_ρ x̂(ρ)·conj ŷ(ρ')`,
  `ρ' = 1 − conj ρ`. Its *definition* contains no zero of ξ (113_06 Def 2.1);
  the zero sum is the value of a contour integral of `ξ'/ξ`.
- **The trace** `τ(z) = Σ_{n≥2} Λ(n)[z(n) + z(1/n)/n] − A(z)`, **zero-free**,
  with `𝔰(x,y) = τ(x ⋆ y*)` (113_12 Thm 1.3). This is what makes the object a
  Frobenius algebra rather than merely a space with a form.
- **The involution** `g*(s) = conj g(1 − conj s)` — the functional equation,
  promoted to an algebra involution. `χ* = χ`, `(f_v)* = f_h`.
- **The rulings** `f̂_v = −2(s−1)ξ`, `f̂_h = 2sξ`, `Ĥ = 2ξ`, `ŵ = χ`. These are
  Riemann's `Φ ± 2Φ'` — candid elements of `D`, not formal symbols
  (113_09 Thm 3.1).

## 3. The theorems, file by file

| file | theorem | content |
|---|---|---|
| 113_01 | Thm 4.1 | the local integral is finite under any fixed scheme, canonical iff `h(1) = 0` |
| 113_02 | Thm 2.1 | given `h(1) = 0`, the prime sum converges absolutely for `θ > 1` |
| 113_03 | Def 4.1 | `𝔗(h) = 𝔗_∞ + 𝔗_fin` well-defined on `A` (modulo Assumption T) |
| 113_04 | §2–3 | verdict on d1's construction gap; the two items then remaining |
| 113_05 | §1–4 | canonical conventions; the closed forms for `f̂`, `ŵ`, `A(z)` |
| 113_06 | Def 2.1, Thm 3.2 | the canonical Weil decomposition; **Assumption T discharged (analytic half)** |
| 113_07 | Def 1.3, Prop 4.1 | the class `D`; the identity functional is a norm; `h(1)=0` unnecessary |
| 113_08 | Thm 2.1 | the polar coordinates **are** the two rulings; Connes' Lemma 2.1 as index engine |
| 113_09 | **Thm 2.2** | **`rad I_∂` = the `χ`-ideal**, `χ = s(s−1)ξ(s)` — d1's analytic half |
| 113_09 | Thm 3.1, §4 | the rulings are candid elements; `H² = 2`, `(F_v − F_h)² = −2`, from `Λ(n)` + digamma alone |
| 113_10 | Thm 1.2/1.3, 2.2/2.5 | **d0** the degree map; **d5** the effective cone, requirement (R) proved |
| 113_10 | **Thm 4.2/4.3** | **`(E°) ⟺ RH`**, both directions |
| 113_11 | Thm 3.1, 3.3 | **d3 is impossible inside `D`**: divisor and values are doubly dissociated |
| 113_12 | Thm 1.3, 3.2, 3.4 | the form is a trace; nondegeneracy; **`K = 0`** |
| 113_12 | **Thm 4.1** | the Hodge index inequality on `H^⊥` holds **iff** RH; signature `(1,7)` on-line, `(3,5)` off |
| 113_12 | §5, Thm 5.1 | **Ansatz A** (`h⁰−h¹+h² = D²/2`, `h²(D) = h⁰(−D)`, `K=0`) ⟹ `(E°)` ⟹ RH |
| 113_13 | §2 | Weil positivity **measured from the primes** at four probes, agreement `≤ 4e−15` |
| 113_13 | Thm 3.1, 4.1 | **O3** no spectral gap; **O2** the `δ_n` have infinite mutual intersection |
| 113_14 | Lemma 1.1′ | ξ·(meromorphic `v`, poles only on zeros of ξ) is `f̂` for some `f ∈ D_θ` |
| 113_14 | **Thm 2.1, Cor 2.2** | **(SEP) discharged** — the separating family `χ/(s−ρ)^{m_ρ}`; **d4 unconditional** |
| 113_14 | **Thm 3.3** | **(INT) discharged** — an off-line zero yields, in closed form, a real Schwartz witness with `𝔰(f,f) = 4m|a₁|² > 0` |
| 113_15 | — | the four-row ledger: every status, every citation, audited mechanically |

## 4. The state of row (d)

| # | requirement | status | source |
|---|---|---|---|
| d0 | degree map, `Z`-valued on effective classes, killing the radical | **BUILT** | 113_10 Thm 1.2/1.3 |
| d1 | descent to linear equivalence | **BUILT, analytic half only** | 113_09 Thm 2.2/2.4 |
| d2 | a polarization `H` with `H² > 0` | **HAVE** (`H² = 2`, `H = 2Φ` effective) | 113_10 Thm 3.2 |
| d3 | Riemann–Roch with a quadratic `D²` term | **IMPOSSIBLE inside `D`** | 113_11 Thm 3.1/3.3 |
| d4 | Serre duality / `h²` vanishing | **BUILT, unconditional** | 113_12 §3 + 113_14 Thm 2.1 |
| d5 | effective cone, `D` effective ⟹ `D·H > 0` | **BUILT** | 113_10 Thm 2.2/2.5 |
| — | `K = 0` | **BUILT** | 113_12 Thm 3.4 |

## 5. The three obstructions

One fact — **there is no lattice inside `D`** — proved three independent times,
each killing a different escape route.

- **O1** (113_10 §5) — the divisor group is a complex vector space, so the
  effective cone is scaling-stable and `h⁰(nD) = h⁰(D)`. Measured exactly at
  `n = 2, 5, 100`. Kills every growth argument, which is the engine of the
  classical Hodge index proof.
- **O2** (113_13 Thm 4.1) — `𝔰(δ_n, δ_m)` diverges: `|(n/m)^ρ| = (n/m)^{1/2}`
  never tends to zero, and the symmetric partial sums wander
  (`K=5: 2.8305 … K=40: 1.0671`). Kills discretisation.
- **O3** (113_13 Thm 3.1) — no spectral gap: `sup 𝔰(f,f)/‖f‖² = 0` on
  `D° \ rad`, not attained; the ratio falls to `−1.7e−176` while the on-zero
  control *grows*. Kills every coercive / compactness proof.

Ansatz A survives O3 only because it is non-quantitative. It passes R7, R8 and
R9 (the last with margin 3, on a test registered before Ansatz A existed), and
by 113_12 Thm 5.1 it is RH-hard.

## 6. The two analytic gaps, and how they closed

- **(SEP)** — nondegeneracy of the zero block *inside `D`*. 113_12 §3 recorded
  it as open on the grounds that "division by `(s−ρ')` is not an operation in
  the convolution algebra." That reasoning was **wrong**: `D` is defined by a
  growth condition, not by closure under an operation, so one only has to
  exhibit a function with the right decay — and 113_09's own proof already had.
  The genuinely new piece is **Lemma 1.1′**, repairing 113_09's citation of its
  own Lemma 1.2 (stated for holomorphic `v`, applied to a `v` with a pole).
  R22 fired on this; the correction is 113_14 §5.
- **(INT)** — the interpolation step in 113_07 Prop 4.1 `(⇐)`. Closed by
  choosing the denominator over the whole quadruple
  `{ρ₀, conj ρ₀, 1−conj ρ₀, 1−ρ₀}`, which makes every other coordinate exactly
  zero and reduces the problem to a two-real-parameter rotation that succeeds
  precisely when `Im(u₀²) = 2(σ−½)t ≠ 0` — i.e. exactly off the critical line.
  Real zeros are covered by a parity switch on `P`. Verified end-to-end against
  a *surrogate* ξ that violates RH: `𝔰(f,f) = +4.000000000000`, predicted `4m`.

**Neither closure moves the programme closer to RH,** and this must be said
plainly: every statement they unblocked is an *equivalence* with RH. Before:
"Hodge index `⟺` RH, modulo an interpolation lemma." After: "Hodge index
`⟺` RH." The one real gain is a closed-form counterexample generator — any
off-line zero yields, by a one-line formula, a real Schwartz datum violating
Weil positivity.

## 7. What phase 113 did **not** touch

**Rows (a) and (b).** The phase works inside an analytic function class and
never touches the graded family. It adds one severe design constraint that row
(a) did not have before: `D/rad` is a complex vector space, so any future (a)
must carry a `Z`-structure on which the row-(c) pairing is **finite** — and O2
shows the obvious candidate lattice fails that test.

The binding constraint has moved. It is no longer d1 (solved analytically) but
the absence of any integral structure at all: **a4** (a product with quadratic
growth), **b4** (a lattice of correspondences with finite mutual intersection),
and **R16** (whether a *quadratic* `χ` can exist over `Spec Z` at all — the
sharpest open test; every Riemann–Roch actually available there is
one-dimensional with a linear `χ`).

## 8. Candor

Twenty-three refutation conditions R1–R23 were pre-registered across the phase
and are tabulated with status in 113_15 §7. R4, R7, R8, R9 passed; **R5 fired**
(it is O1, and 113_11 reported it as required); **R22 fired once**, on 113_12's
mis-recording of (SEP), corrected in 113_14 §5; R17, R20, R21 did not fire;
R18 and R19 stand as O3 and O2.

**RH is not proved.** No status in this summary or in the ledger is promoted
beyond what its cited file proves, and 113_15's verifier checks all 19 source
citations mechanically, plus a textual audit that no file in the phase claims
RH is proved.

## 9. Scope

**Proved here.** Nothing; this is a summary. The theorems are in the files of
§3.

**Read from source.** All files cited in §3–§7.

**Verified numerically.** See the individual verifiers; 113_15 §9 lists the
ledger's own numerical checks.

**Not established.** a4, b2, b4, c10, d3 inside `D`, `(E°)`, Ansatz A, row (d),
and RH.

## 10. Verifiers

`113_99_verify_all.py` runs all fifteen. Individually:

| script | checks |
|---|---|
| 113_01 … 113_06 | see each file's own summary line |
| 113_07 | 46 |
| 113_08 | 60 |
| 113_09 | 79 |
| 113_10 | 51 |
| 113_11 | 53 |
| 113_12 | 40 |
| 113_13 | 33 |
| 113_14 | 38 |
| 113_15 | 34 |

All exit 0 with `VERDICT: ALL CHECKS PASS`.
