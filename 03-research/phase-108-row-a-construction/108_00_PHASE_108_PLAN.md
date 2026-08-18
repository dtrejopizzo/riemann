# Phase 108 — Row (a): the space over ℤ

## 1. Mission

Row (a) is the only remaining unknown of the program.  Rows (b), (c) and (d)
are each blocked on it and contribute no independent unknowns.

Phase 108 has one objective:

> **Make the global rational-function question well posed on the DC quotient,
> and determine the category the descent forces.**

Phase 108 does **not** aim to prove RH, to close row (a), or to promote any
paper.  Its deliverable is verified structure plus candid verdicts.

## 2. Source rule (inherited, non-negotiable)

No definition may use a zero of ξ, a Li coefficient, the sign of the Weil
form, or a positive part extracted from that form.  Zeros may appear only in
the *description* of an obstruction, never as an input to a construction.

## 3. Inherited state — do not re-derive

| ref | result |
|---|---|
| 107_146 | `dim_{S±}‖H(ℤ^r)‖_n`: two-sided bounds, base 3 is rank-one; exact `s·⌈log₂(n+1)⌉` for `s ≥ 2` |
| 107_224 | every hom `(ℝ,+) → ` f.g. abelian group is 0 |
| 107_237 | `U_f(x,y) = x·u_f(y/x)`, `u_f''(r) = f(r)/r`; unique **mod affine**; `D_f` is **not** finite-PL |
| 107_238 | the interior mixed Hessian density vanishes **identically** |
| 107_239 | corner trace `𝔗(f⋆g̃) = N(f⋆g̃)` |
| 107_240 | Thm C: local principal subspace is `{0}`; Thm D: `rad I_∂` is zero-determined; §5: the **numerical** quotient is free |
| 107_242 | no `W_rat`-based map carries the transverse `p`-direction |

**The blocker, stated exactly:** by 107_237 §2 the potential `U_f` is a local
equation on the universal positive chart, *not* a global rational function on
the quotient topos.  By 107_240 Thm C the local principal subspace is `{0}`,
so the question cannot even be posed locally.  It is global or nothing.

## 4. The Frobenius action, fixed once

`Ψ_λ` is the correspondence of slope `λ > 0` and `D_f = ∫f(λ)Ψ_λ d^*λ`.
Frobenius `φ_n` sends `Ψ_λ ↦ Ψ_{nλ}`, hence acts on test functions by

```
(n·f)(λ) = f(λ/n),        n ∈ ℕ^×,   extended to ℚ_+^× .
```

Since `u_f''(r) = f(r)/r` and affine functions have vanishing second
derivative, **`U_f` is determined by `f`, and `f` by `U_f` mod affine.**
Every descent condition below is therefore a condition on `f` alone.

## 5. Part I — well-posedness (the critical path)

### 108.01 — Strict-invariance falsifier  *(run first)*

> Does there exist `f ≠ 0`, `f ∈ C_c((0,∞))`, with `U_{n·f} − U_f` affine for
> every `n ∈ ℕ^×`?

Reduces to `f(r/n) = f(r)`.  With `r = e^t` this is invariance under
translation by `log n`, and `{log n}` generates a **dense** subgroup of ℝ.

Expected verdict: **NO**.  Deliverable is not the no-go but the identification
of *which hypothesis* is incompatible: compact angular support.
Cross-reference 106.185 (the same dense-orbit mechanism).

### 108.02 — The character relaxation  *(the constructive step)*

A global rational **section of a line bundle** is not invariant; it satisfies
a cocycle condition.  Relax to a character twist:

> Classify all `f ≠ 0` and characters `χ : ℚ_+^× → ℝ^×` with
> ```
> f(r/n) = χ(n) f(r)      for all n .
> ```

`f(r) = r^s` gives `χ(n) = n^{-s}`.  The general solution is `r^s` times a
`log`-periodic factor.  **These are exactly the Mellin characters**, and `s`
is the graded degree.

Deliverables: the classification with proof; the statement that descent forces
**exit from compact support into a character-graded family**; explicit
compatibility of `χ` on `ℕ^×` with its extension to `ℚ_+^×`.

### 108.03 — The graded sheaf and `div`

Build the character-graded sheaf of DC sections from 108.02, define `div` on
it, and thereby define **principal** globally.

### 108.04 — Is 107_240 Thm C resolved?

With 108.03 in hand: is the **global** principal subspace nonzero?  If yes,
the question that 107_240 declared not-well-posed becomes well posed, and
principal invariance becomes testable for the first time.  Do **not** test it
here; only establish well-posedness.

## 6. Part II — the numerical route  *(independent of Part I)*

### 108.10

107_240 §5 gives `Ī_∂` on `{DC divisors}/rad I_∂` unconditionally.  Determine
what is constructible there **without** principal invariance, and state
precisely what fails for lack of linear equivalence.

## 7. Part III — `H¹`  *(only after Part I)*

### 108.20

CC declare `H¹` open (1805.10501) for the idempotent-monoid formulation.
Mikhalkin–Zharkov/Cartwright define `H¹(Δ, 𝒜_ℤ) ≅ Pic_ridge` for the
**abelian** sheaf of PL functions on **finite** Δ-complexes.

Two facts must be confronted candidly before any use:
1. 107_237 Thm 2.1: the DC object is **not** finite-PL, by construction;
2. `Pic_ridge` is a Picard group; CC need `H¹` of the structure sheaf.  These
   may not be the same `H¹`.

Deliverable: a decision document on whether the abelian-sheaf route is
available for DC objects.  A negative answer is a full deliverable.

## 8. Part IV — the one untried lemma  *(row c, cheap, parallel)*

### 108.30 — Component-triviality

> Every realized `D_f` is component-trivial at every finite place.

If true, `c_p` leaves the target and `107_126` (`TARGET_KODAIRA_ONLY: YES`)
already passes.  Test first on the fixed atlas `20a1@2`, `36a4@2`, `14a1@5`,
`11a1@5`, genus-2 control.  Named as the escape in 107_144 §5; never attempted.

## 9. Execution rules

1. One `.md` + one `.py` verifier per document, numbered `108_NN_*`.
2. Every verifier must run to `exit 0` and print an explicit `VERDICT:`.
3. A failed gate **is** the deliverable.  Write the no-go with its exact
   scope.  Never work around a falsifier.
4. Never promote `ROW_*_STATUS`.  Never modify Paper 40, phase 106 or
   phase 107.  Write only inside `phase-108-row-a-construction/`.
5. State scope boundaries explicitly in every document, in the style of
   107_233 §5 and 107_240 §6.
6. Claims that were read but not verified must be labelled as such.

## 10. Order

```
108.01  falsifier            → cheap, decisive, run first
108.02  character relaxation → the constructive core
108.03  graded sheaf + div
108.04  well-posedness verdict
108.30  component-triviality → independent, may run in parallel
108.10  numerical route      → independent
108.20  H¹ decision          → last
```
