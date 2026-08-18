# 113.15 — The four-row ledger: what Weil's programme over Spec ℤ has, and what it does not

> **What this file is.** An audit, not a theorem. Weil's proof of RH for curves
> over finite fields rests on four rows — (a) a space, (b) correspondences as
> cycles, (c) `Gamma_n . Delta = N_n` as an intersection number, (d) the Hodge
> index theorem. This file states, row by row and requirement by requirement,
> what this programme has built over `Spec Z`, what it has closed negatively,
> and what has never been attempted. Every "HAVE" cites a file and a theorem;
> every citation is checked mechanically by the verifier.
>
> **What this file is not.** It is not a claim about RH. The phase's own
> Theorem — 113_10 Thm 4.2/4.3, 113_12 Thm 4.1 — says that row (d), completed,
> *is* RH. **RH is not proved here or anywhere in this corpus.**

```
ROW (a)  the space ................. UNCHANGED by phase 113; product structure MISSING
ROW (b)  correspondences as cycles . UNCHANGED by phase 113; O2 is a new constraint
ROW (c)  the intersection identity . ADVANCED: now a Frobenius *-algebra with a
                                     zero-free trace tau, radical computed
ROW (d)  the Hodge index ........... d0 d1 d2 d4 d5 BUILT; d3 IMPOSSIBLE inside D;
                                     the residue is exactly RH
```

---

## 1. Row (a) — the space

| # | item | status | source |
|---|---|---|---|
| a1 | a divisor group `Div` and a principal subgroup `Prin'` | HAVE | 108_03, 108_31, 108_33 |
| a2 | `Prin'`-invariance of the pairing | **CLOSED (false)** | 108_38 Thm 3.1, "principal invariance fails" |
| a3 | a curve-like absolute dimension, `Theta(deg D)`, every rank | HAVE | 107_146 Cor C |
| a4 | a **product** structure on which the dimension grows quadratically | MISSING | never attempted |
| a5 | a working pairing on the graded side | CLOSED both sides | 108_50, 108_52, 108_53 |

**Phase 113 changed nothing in row (a),** and this must be said plainly rather
than implied away: the phase works inside `D`, an analytic function class, and
never touches the graded family. But it does add one **design constraint** that
row (a) did not have before, and it is severe:

> **The space of phase 113 cannot be an (a).** `D / rad` is a complex vector
> space (113_10 Prop 5.1), so it has no lattice; O1, O2 and O3 below prove
> three times over that no lattice is hiding in it. Any future (a) must carry a
> `Z`-structure on which the row-(c) pairing is **finite** — and 113_13 Thm 4.1
> shows the obvious candidate lattice fails that test.

---

## 2. Row (b) — correspondences as cycles

| # | item | status | source |
|---|---|---|---|
| b1 | the Weil coefficient `Lambda(p^k)/sqrt(p^k)`, exactly, at the central weight | HAVE | 108_34, 108_35 |
| b2 | the `Gamma_{p,k}` as **cycles**, not functionals | MISSING | never built |
| b3 | import from foliated dynamics (Deninger–Morishita) | **CLOSED** | 107_242 Thm 4.1 |
| b4 | a lattice of correspondences with finite mutual intersection | **CLOSED (O2)** | 113_13 Thm 4.1 (new) |

**Phase 113 changed nothing in row (b) either,** but b4 is new and is a genuine
constraint. The natural embedding `n |-> delta_n` of the correspondence monoid
into the pairing gives

```
s(delta_n, delta_m) = m + n - m * sum_rho m_rho (n/m)^rho ,
```

which **diverges**: `|(n/m)^rho| = (n/m)^{Re rho} = 1.2247...` never tends to
zero. The symmetric partial sums of the zero sum `sum_rho (3/2)^rho` wander —
`K=5: 2.8305, K=10: 2.3678, K=20: 2.0270, K=40: 1.0671, K=59: 1.2144` — with no
Cauchy behaviour. Arakelov-style discretisation
cannot be transplanted along this map. R19 states what a replacement would have
to do.

---

## 3. Row (c) — `Gamma_n . Delta = N_n`

This is the row phase 113 actually advanced.

| # | item | status | source |
|---|---|---|---|
| c1 | the analytic identity, `sum_p sum_k Gamma_{p,k}(f_s) = -zeta'/zeta(s)` | HAVE | 108_36 Thm 1.1 |
| c2 | a pairing whose **definition** contains no zero of `xi` | HAVE | 107_240 §1; 113_06 Def 2.1 |
| c3 | the pairing on **Schwartz** data, with a stated domain `D` | HAVE (new) | 113_07 Def 1.3, 113_09 Lemma 1.1 |
| c4 | no admissibility side condition, no renormalisation | HAVE (new) | 113_07 §3 (`h(1)=0` was impossible *and* unnecessary) |
| c5 | the radical, computed exactly | HAVE (new) | 113_09 Thm 2.2: `rad I_d` = the `s(s-1)xi(s)`-ideal |
| c6 | the two rulings realised by **candid elements** of `D` | HAVE (new) | 113_09 Thm 3.1: `f_v, f_h` = Riemann's `Phi +- 2Phi'` |
| c7 | the intersection numbers as facts about **primes** | HAVE (new) | 113_09 §4: `H^2 = 2` etc. verified from `Lambda(n)` + digamma, no zeros |
| c8 | the form is a **trace**: `s(x,y) = tau(x * y^*)`, `tau` zero-free | HAVE (new) | 113_12 Thm 1.3, Def 1.1 |
| c9 | nondegeneracy of the trace form on `D` (both blocks) | HAVE (new) | 113_12 Thm 3.2 + 113_14 Thm 2.1 |
| c10 | promotion of c1 to an intersection number **of cycles** | **CLOSED** | 108_50, 108_53; 109_04 Thm 1.1 (blindness, every kernel) |

The net effect: row (c) is no longer "an identity plus a pairing with a computed
signature". It is a **Frobenius `*`-algebra** `(D/rad, *, ^*, tau)` — commutative,
with a nondegenerate symmetric trace, a canonical involution given by the
functional equation, two minimal idempotents `[f_v], [f_h]`, a `Z`-valued
divisor map `div_S`, a degree map, and an effective cone. That is a complete
row-(c) vocabulary. What it still is not is a statement about cycles: c10 stays
closed, and nothing in phase 113 reopens it.

---

## 4. Row (d) — the Hodge index

The requirement list is the backward map's d1–d5, plus d0 (the degree map),
which the backward map had not isolated.

| # | requirement | status after phase 113 | source |
|---|---|---|---|
| d0 | a degree map, `Z`-valued on the effective classes, killing the radical | **BUILT** | 113_10 Thm 1.2, Thm 1.3 |
| d1 | the form descends to a "linear equivalence" | **BUILT, analytic half only** | 113_09 Thm 2.2, Thm 2.4 |
| d2 | a polarization `H` with `H^2 > 0` | **HAVE** (`H^2 = 2`, and `H = 2Phi` is *effective*) | 107_241 Thm 3.1; 113_10 Thm 3.2 |
| d3 | Riemann–Roch with a quadratic `D^2` term | **IMPOSSIBLE inside `D`** | 113_11 Thm 3.1, Thm 3.3 |
| d4 | Serre duality / `h^2` vanishing | **BUILT, unconditional** | 113_12 §3 + 113_14 Thm 2.1, Cor 2.2 |
| d5 | an effective cone with `D` effective `=> D.H > 0` | **BUILT** (requirement (R) proved) | 113_10 Thm 2.2, Thm 2.5 |
| — | `K = 0` (the canonical class) | **BUILT** | 113_12 Thm 3.4; corroborated by CC genus 0 |

Four of the six were "MISSING, never attempted" when THE_BACKWARD_MAP was
written. They are now built. And that is exactly why the ledger has to be read
carefully, because the engine assembled from them does not turn:

> ### The two theorems that decide the row
>
> **113_10 Thm 4.2 / 4.3.** `(E^o) <=> RH`, where `(E^o)` is the effectivity
> statement d3 was supposed to supply. Both directions proved. Since 113_14
> Thm 3.3, both directions are statements about `D`, with no interpolation
> hypothesis.
>
> **113_12 Thm 4.1.** The Hodge index inequality on `H^perp` holds **iff** RH.
> Measured, from identical code: signature `(1,7)` with the zeros on the line,
> `(3,5)` off it.
>
> Therefore **row (d) is not a route to RH. Row (d) is RH.** Anything that
> closed it would be a proof of the Riemann Hypothesis, and this programme has
> not closed it.

### 4.1 Why d3 is impossible inside `D`, precisely

113_11 gives the mechanism, and it is sharper than "we could not find an `h^0`".

- `div_S(f) = sum_{s0 in S} ord_{s0}(f^) [s0]` is the phase's only `Z`-valued,
  `*`-additive, `C^x`-invariant structure — exactly the integrality O1 asked for.
- **Double dissociation** (113_11 Thm 3.1): `2f_v` has the same divisor as `f_v`
  but different values; `f_v * f_v` has the same values as `f_v` (they are
  idempotent classes) but a different divisor. Divisor and values are mutually
  independent.
- Hence escaping O1 costs the pairing, and keeping the pairing costs the
  lattice. `h^0` in the sense d3 needs — a finite dimension growing like
  `n^2 D^2 / 2` — cannot be a function of either.

### 4.2 The three obstructions, and the one fact behind them

The obstacle is the absence of a lattice, and it has been proved three
independent times, each killing a different escape route.

- **O1** (113_10 §5) — the divisor group is a complex vector space, so the
  effective cone is scaling-stable: `h^0(nD) = h^0(D)`. Measured exactly at
  `n = 2, 5, 100`. This kills every growth argument, which is the engine of the
  classical Hodge index proof.
- **O2** (113_13 Thm 4.1) — the correspondences `delta_n` have infinite self-
  and mutual intersection. This kills discretisation.
- **O3** (113_13 Thm 3.1) — the negative part has **no spectral gap**:
  `sup s(f,f)/||f||^2 = 0` on `D^o \ rad`, not attained. Measured, in a zero
  gap at `b = 17.5`: the ratio falls from `-5.7e-5` at `sigma = 1` to
  `-1.7e-176` at `sigma = 6`, while the on-zero control *grows* from `-3.54` to
  `-22.05`. This kills every coercive, spectral-gap or compactness proof.

Ansatz A (113_12 §5: `h^0 - h^1 + h^2 = D^2/2`, `h^2(D) = h^0(-D)`, `K = 0`)
survives O3 only because it is non-quantitative — it asserts effectivity, not a
bound. It implies `(E^o)` and hence RH (113_12 Thm 5.1), and it passes R7, R8
and R9, the last with margin 3 on a test registered before Ansatz A existed.
It is not proved, and by Thm 5.1 it is RH-hard.

### 4.3 The arithmetic measurement

For the first time, `s(f,f)` on `D^o` was computed **from the primes**:
`sum_n Lambda(n)[...] - A(f)` against the zero side, at four probes
(113_13 §2). Agreement to `2.7e-15`, `3.8e-15`, `4.0e-16`, and a floor-limited
`1.4e-15`; all four values `<= 0`. This is Weil positivity measured from
`Lambda(n)` and a digamma integral alone. It is evidence, not proof, and R17
records exactly what would overturn it.

---

## 5. What phase 113 changed, in five lines

1. The pairing moved from compactly supported to **Schwartz** data, where the
   `xi`-divisibility route that 110 closed is alive (113_07, 113_09).
2. The radical was **computed**: `rad I_d` = the `s(s-1)xi(s)`-ideal. d1's
   analytic half is done; the geometric half (rows a/b) is untouched.
3. The row-(c) object became a **Frobenius algebra with a zero-free trace**,
   and its intersection numbers became facts about primes.
4. d0, d2, d4, d5 and `K = 0` were built; d3 was proved **impossible** inside
   `D`; `(E^o)` and the Hodge index were proved **equivalent to RH**.
5. The last two analytic gaps, (SEP) and (INT), were **discharged** (113_14),
   so none of the above carries an undischarged hypothesis.

## 6. What would have to happen next

Not "prove `(E^o)`" — that is RH. The only non-circular openings the ledger
leaves are on the other side of the map:

- **a4** — a product structure with quadratic growth. The CC absolute dimension
  is `Theta(deg D)`, curve-like; a surface needs `D^2`. Untested.
- **a-new / b4** — exhibit a space whose principal divisors are the `xi`-ideal
  (113_09 §5 makes this the candid statement of d1) **and** whose divisor group
  is a lattice on which the row-(c) pairing is finite. O1 and O2 are the two
  tests any candidate must pass.
- **R16** — decide whether a *quadratic* `chi` can exist over `Spec Z` at all.
  Every Riemann–Roch actually available there is one-dimensional with a linear
  `chi`. If none can, Ansatz A is dead and this route with it.

## 7. The pre-registered conditions, consolidated

Every refutation condition the phase registered, with its status. "OPEN" means
no candidate has been offered to test.

| # | file | condition | status |
|---|---|---|---|
| R1 | 113_08 | an `h^0` quantifying over the zeros or over `sign Q` is circular | OPEN (standing rule) |
| R2 | 113_08 | deformation-blind `h^0` cannot deliver (E) | OPEN |
| R3 | 113_08 | must fail the Davenport–Heilbronn test | OPEN |
| R4 | 113_08 | (R) must hold for every nonzero effective `D` | **PASSED** (113_10 Thm 2.5) |
| R5 | 113_10 | an `h^0` on a scaling-stable cone cannot grow | **FIRED** — this is O1, and 113_11 reported it as required |
| R6 | 113_10 | circularity, restated for `(E^o)` | OPEN (standing rule) |
| R7 | 113_10 | any `h^0` must give `h^0(H) >= 1` | **PASSED** by Ansatz A (tight, `= 1`) |
| R8 | 113_10 | no nonzero element of `rad` may be effective | **PASSED** by Ansatz A |
| R9 | 113_11 | `h^1([3f_v - f_h]) > h^1([H])` at equal degree | **PASSED** by Ansatz A, margin 3 |
| R10 | 113_11 | an `h^0` not determined by the section sets escapes Thm 3.3 | OPEN |
| R11 | 113_11 | CC duality must reproduce `(F_v - F_h)^2 = -2` | OPEN |
| R12 | 113_11 | the `m_rho > 1` truncation caveat | OPEN (does not affect `f_v, f_h, H`) |
| R13 | 113_12 | a `D^2 > 0` class with neither `D` nor `-D` effective kills Ansatz A | OPEN (would also refute RH) |
| R14 | 113_12 | `chi(O) != 0` would shift every number in §5 | OPEN |
| R15 | 113_12 | an `h^1` with `h^1(H) != 0` breaks R7 or `K = 0` | OPEN |
| R16 | 113_12 | no quadratic `chi` over `Spec Z` ⟹ Ansatz A dead | OPEN — **the sharpest open test** |
| R17 | 113_13 | any `f` in `D^o` with `s(f,f) > 0` disproves RH | **NOT FIRED** at four probes, `<= 4e-15` |
| R18 | 113_13 | a coercive bound `s(f,f) <= -eps ||f||^2` is refuted by Thm 3.1 | **STANDING** (O3) |
| R19 | 113_13 | a finite lattice pairing cannot embed as `n |-> delta_n` | **STANDING** (O2) |
| R20 | 113_13 | the prime and zero columns must not disagree beyond the floor | **NOT FIRED** |
| R21 | 113_14 | a real `f` in `D^o` with `s(f,f) > 0` *not* assuming an off-line zero disproves RH | **NOT FIRED** |
| R22 | 113_14 | a file claiming a gap already proved elsewhere must fail its citation audit | **FIRED ONCE** — 113_12's (SEP); corrected in 113_14 §5 |
| R23 | 113_14 | if the witness of 113_14 Thm 3.3 leaves `D`, Cor 3.4 reverts | OPEN |

## 8. The bottom line

- **Rows (a) and (b) are where the programme is stuck**, and phase 113 left both
  untouched. The binding constraint moved: it is no longer d1 (solved
  analytically) but the absence of any integral structure at all — a4, b4, and
  the O1/O2/O3 triple that says one will not be found inside `D`.
- **Row (c) is in good shape**, better than at any previous point: a genuine
  `*`-algebra, a zero-free trace, a computed radical, intersection numbers
  measured from primes.
- **Row (d) is complete except for one statement, and that statement is RH.**
  This is the phase's most important negative result and it is a theorem, not
  an impression: 113_10 Thm 4.2/4.3 and 113_12 Thm 4.1.
- **RH is not proved.** No status in this ledger is promoted beyond what its
  cited file proves, and the verifier checks the citations mechanically.

---

## 9. Scope

**Proved here.** Nothing. This file is an audit; every entry is a citation.

**Read from source.** All files named in the tables of §1–§4. The three CC facts
used in §4 are second-hand, via `phase-39-G1G2-interface/120-inventario-CC-fuente.md`
(`[VERIFICADO]`-tagged there, not re-read from the papers here).

**Verified numerically here.** `xi(0) = xi(1) = 1/2` and the five intersection
numbers that follow from it; `deg H = 2`; the signature flip `(1,7)` vs `(3,5)`;
O1's exact scaling ratio `100`; O2's non-settling partial sums; plus 20 source
citations and 3 candor audits, checked mechanically.

**Not established.** Everything the tables mark MISSING, CLOSED, IMPOSSIBLE or
OPEN. In particular: a4, b2, b4, c10, d3 inside `D`, `(E^o)`, Ansatz A, row (d),
and RH.

## 10. Verifier

`113_15_the_four_row_ledger.py` — 34 checks, all passing, exit 0.
