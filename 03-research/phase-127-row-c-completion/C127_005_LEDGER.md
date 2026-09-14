# C127.005 — row C ledger

Date: 2026-09-12.

```text
ROW C:  WEIL-STRENGTH-COMPLETE.  I_A([K_F],[K_G]) = B_nuc(F,G) on the declared
        test class, with the polar packet the hyperbolic ruling form, and that
        class sufficient for Weil's criterion.  No analytic black box.
```

Clauses C.1–C.9 and their proofs: Paper 45 §12.1.

## Reclassified

| item | source | disposition |
|---|---|---|
| row C is Meyer Thm 5.8 as a black box | paper 42 `rem:rowcattribution`, P122 audit | no longer applies |
| Meyer archimedean coefficient fails a Gaussian test | P123.035 §1 | resolved by removal |
| `B_P` not the image of a single source localization | P123.046 §5 | `PROVED` — the single-zero layer |
| value on the multiple-zero complement not given | P123.046 §5, P123.048 §5 | `PROVED` — zero at every nontrivial modulus |
| identification with the integral contact determinant | P123.046 §5 | `PROVED` — Arakelov length = covolume |
| the archimedean term, deferred in ~10 notes | P123.032–112 | `PROVED` — §7 on P123.035 |
| `h ↦ A_h(r)` does not preserve convolution | P123.039 §5 | `PROVED` — P123.043 §1 + the Fell completion |
| `w_unit(Γ_n) = n−1` unaccounted | Paper 44 §9.2 | `PROVED` — it is the unit integrand of `W_p` |
| `q_T ≥ 0` on primitives ⟹ RH, asserted only | `113_07` | `PROVED` |
| `106_11` only for unconstrained tests | `106_11` | upgraded to the primitive class |

## Open

**None.**  The two items listed as open in the first draft are closed in
[C127.006](C127_006_TWO_INVARIANTS_RECONCILED.md) and Paper 45 §12:

1. the comparison `rad(T)` vs `rad(I_A)` was **ill-posed** — the two objects have
   different domains — and is replaced by the proof of clause A.6 for the
   intersection form on the radial sector (Paper 45 Thm. 12.3, 12.4);
2. `χ_A` **is** the character of the shadow localized on the single-zero layer;
   the apparent sum-versus-product mismatch is exactly the corner strata killed
   by Thm. 5.4 (Paper 45 Thm. 12.5, Cor. 12.6).

## What D inherits

Row D's target is now exactly a **Hodge index statement**: the intersection form
`I_A` is semidefinite on the complement of the hyperbolic ruling plane.  And by
Paper 45 Thm. 10.4 that statement now genuinely implies RH — before it, it
implied RH only modulo the unproved interpolation of `113_07`.
