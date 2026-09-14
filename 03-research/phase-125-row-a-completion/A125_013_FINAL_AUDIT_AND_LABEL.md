# A125.013 — final audit of row A, including P123.082, and the label

Status: `AUDIT`.  Supersedes A125.010 §§4–5.

## 1. The adversarial audit the specification requires

The closure rule (P123_A_ACCEPTANCE_SPECIFICATION §4) grants
`WEIL-STRENGTH-COMPLETE` only if A.1–A.10 are proved **and** an adversarial
audit confirms none of A.2–A.8 is a renaming of the scalar explicit formula.
The audit must also be consistent with every `PROVED-IN-REPOSITORY`
statement.  Two such statements bear directly on this campaign and were not
confronted in A125.010:

* **P123.082**: the twist-only stable sector "did not produce the
  geometrically mixed sector required by A.2, A.6 and A.8"; the source must
  contain further bimodules or kernels.
* **P123.038 §1**: the arithmetic family is the invertible twist
  `E_{a_S(n)}`, already in the twist sector.

A125.012 reconciles them.  The mixed sector of A125.006 is genuinely nonzero
in the numerical quotient, so A.6's letter holds; but the boundary shadow that
computes it vanishes on the whole arithmetic family (A125.012 Theorem 1.2),
so a theory built on it can hand nothing to B/C.  P123.082 was right that the
theory is deficient and wrong about where: the deficiency is the shadow, not
the absence of non-invertible objects.

## 2. Status table, two theories

`A^\partial` = graph sector with the boundary shadow (A125.006–011).
`A^{\rm full}` = graph sector with the full shadow (2.1) of A125.012.

| clause | `A^\partial` | `A^{\rm full}` |
|---|---|---|
| A.1 carrier, coefficients, restriction, descent | `PROVED` | `PROVED` (same data) |
| A.2 correspondences, geometric localization, declared completion | `PROVED` (A125.011 Def. 5.1) | `PROVED` (same) |
| A.3 composition, unit, two-sided excision | `PROVED` (A125.002, A125.006 Thm 3.1) | `PROVED` (same) |
| A.4 dagger | `PROVED` unconditionally (A125.011 Thm 2.2) | `PROVED` (same) |
| A.5 trace/shadow on a trace-class domain | `PROVED` — but the shadow is **zero on `Γ_n`** (A125.012 Thm 1.2) | `CONDITIONAL` on `(F)` |
| A.6 numerical equivalence, ruling plane, mixed sector | `PROVED` | `CONDITIONAL` on `(F)` |
| A.7 effectivity, proper cone | `PROVED` | `CONDITIONAL` on `(F)` |
| A.8 mixed RR | `PROVED` | `CONDITIONAL` on `(F)` |
| A.9 classical control | `PASSED` on invertible correspondences | `PASSED`; with `(F)` the Lefschetz count is reproduced on `Γ_n`, not only its vanishing |
| A.10 independence | `PROVED` | `PROVED`; `(F)` uses no `Λ(n)` |
| adversarial: not a renaming of the explicit formula | passes vacuously — the theory cannot even see it | passes: the shadow is defined before any value is asserted |
| adversarial: consistent with P123.082 | **fails in spirit** (A125.012 §1) | consistent |

## 3. The label

```text
ROW A (boundary theory A^∂):  A.1–A.10 PROVED ON G, UNCONDITIONALLY.
                              NOT WEIL-STRENGTH: its shadow vanishes on Γ_n
                              (A125.012 Thm 1.2), so B/C cannot be built on it.

ROW A (full theory A^full):   A.1–A.4, A.9, A.10 PROVED ON G.
                              A.5–A.8 PROVED CONDITIONALLY ON (F).
                              WEIL-STRENGTH-COMPLETE  <=>  (F).
```

`(F)`: the full relative cyclic shadow of every graph class is perfect and
decomposes along the fixed-point stratification into interior contributions,
with their transverse complexes and half-density weights, plus the boundary
corner bar (A125.012 §3).

The label `WEIL-STRENGTH-COMPLETE` is **not** granted.  Granting it to
`A^\partial` would be literally correct under the ten clauses and would make
the specification's own adversarial audit fail, since it would contradict the
proved judgment of P123.082 in the only sense that matters for rows B and C.
Granting it to `A^{\rm full}` requires `(F)`, which is open.

## 4. What changed in this campaign, in one paragraph

Before: ten clauses, six `OPEN`, three `PARTIAL`, one `NOT PASSED`, with the
dagger blocked by `Hom(U,N)=0`, no trace-class domain or target defined, no
numerical radical on correspondence objects, effectivity blocked by `C1`, and
classical control blocked by `C1`,`C2`.  After: every clause has a theorem on
a declared category; the four recorded obstructions are each shown to be
either misread (`Hom(U,N)=0`, `C1`, `C2`) or an obstruction to the wrong
invariant (P123.082 read as "add non-invertible objects"); two phase-123 open
items are closed (two-sided excision, properness); one conditional input was
introduced and then eliminated; one determinant target was proposed, proved
degenerate, and retracted; and the distance to `WEIL-STRENGTH-COMPLETE` is
reduced to a single named localization theorem `(F)` whose every ingredient
is constructed in phase 123 and whose natural proof route is the integral
deformation of P123.061.
