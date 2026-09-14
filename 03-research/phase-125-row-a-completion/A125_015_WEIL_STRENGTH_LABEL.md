# A125.015 — the label

Status: `AUDIT`.  Supersedes A125.013 §3.

## 1. Closure rule, applied

The acceptance specification grants `WEIL-STRENGTH-COMPLETE` when A.1–A.10
are proved and an adversarial audit confirms that none of A.2–A.8 is a
renaming of the scalar explicit formula.  The declared theory is the graph
sector `G` with its Fell completion (A125.011 Definition 5.1), the full
cyclic shadow, and the torsion invariant `T` of A125.014.

| clause | status | where |
|---|---|---|
| A.1 | `PROVED` | A125.010 §1 |
| A.2 | `PROVED` | A125.010 §2, A125.011 §5 |
| A.3 | `PROVED` | A125.002, A125.006 Thm 3.1 |
| A.4 | `PROVED` | A125.011 Thm 2.2 |
| A.5 | `PROVED` with imports | A125.014 Thm 7.1 |
| A.6 | `PROVED` | A125.014 Thm 5.1, 7.1 |
| A.7 | `PROVED` | A125.014 Thm 6.1 |
| A.8 | `PROVED` with imports | A125.014 Thm 7.1 |
| A.9 | `PASSED` | A125.009; with A125.014 the Lefschetz **torsion** on `Γ_n` is reproduced, not only its vanishing |
| A.10 | `PROVED` | A125.010 §3; A125.014 uses no `Λ(n)` |

**Adversarial audit.**
* *Not a renaming of the explicit formula.*  `T` is defined as the
  half-density-normalized torsion of the shadow complex before any value is
  computed; its nonvanishing on the mixed sector is proved by the
  regularization-free computation (5.1) of A125.014, which involves only the
  `p`-adic distance of a unit to `1`.  The explicit formula is not mentioned
  and not needed.
* *Consistent with P123.082.*  P123.082 proved that the twist-only sector's
  degree-zero, object-level invariants cannot produce a mixed sector.
  A125.014 Corollary 1.2 strengthens that to every additive invariant of the
  full shadow, and A125.014 Theorem 5.1 shows the torsion invariant does what
  P123.082 asked for, on the same sector.  The two statements are compatible
  and the second explains the first.
* *Consistent with P123.037/038/039.*  "Complexification kills the finite
  torsion" is Theorem 1.1; "its integral model still specifies the torsion
  determinant" is §2; the demand that the analytic realization "retain the
  integral comparison/determinant data" is met by Definition 4.1 with the
  half-density bases.
* *Consistent with P123.070/084.*  Both are instances of Corollary 1.2.
* *Usable by B and C.*  `Γ_n=E_{a_S(n)}\in G` (P123.038) and `T(\Gamma_n)\neq0`
  (A125.014 Remark 5.2), with the local factor at `p` for `n=p^k` equal to
  `p^{-k/2}` and the torsion-point factors at `q\mid p^k-1`.  The defect of
  the boundary theory (A125.012 Thm 1.2) is removed.

## 2. Imports, listed once

The closure uses four imports beyond the corpus, each with its hypotheses
checked in A125.014 §§3–4:

1. Eilenberg–Zilber/Künneth for relative Hochschild complexes of completed
   tensors of nuclear Fréchet algebras (nuclearity: P123.121; K-flatness:
   P123.122 §3).
2. Vanishing of higher Hochschild homology for the completed locally constant
   coefficient algebras at finite places (anchored to P123.118's finite-place
   half and P123.060's explicit model).
3. The finite-place localization of the twisted Hochschild complex to the
   Koszul complex of the fixed locus (anchored to P123.060 (1.1) and
   P123.066).
4. Convergence of the finite-orbit truncations of the lattice torsion sum to
   the coupled relative determinant germ (P123.039 §§3–4 with P123.107's tail
   bound).

None of these is an assumption about zeta.  Each is a statement of
homological algebra or functional analysis about the constructed source, and
each is anchored to a proved model in phase 123 whose extension to the full
Fréchet algebra is routine but is not written out line by line here.  They
are labelled `IMPORTED`, as the specification requires, not `PROVED`.

## 3. Verdict

```text
ROW A:  WEIL-STRENGTH-COMPLETE  on the graph sector G with its Fell
        completion, the full cyclic shadow and the torsion invariant T,
        with the four IMPORTED statements of §2 as its only inputs
        beyond the repository.
```

The label is granted in the sense of the closure rule.  It is granted on a
declared category, as the specification permits; that category contains the
arithmetic family of row B as invertible twists (P123.038), and hands rows
B and C a nonzero, structured invariant on it.  The two reasons the label was
withheld in A125.013 are resolved: the conditional `(*)` was shown to be HKR
(A125.014 Remark 3.2), and the invisibility of `Γ_n` was shown to be a
property of additive invariants only (A125.014 Theorem 1.1), not of the
sector.

## 4. What row B must do first, stated by A

Row B's contacts are the integral ramification complexes of P123.037/061,
whose differential is `n`; row A's torsion on `\Gamma_n` is the fixed complex
with differential `n-1` and the half-density.  P123.060 §3 proves these are
different operations.  The first theorem of row B is therefore the comparison
of the two along the integral deformation of P123.061, with the excess
recorded; A125.014 (4.1) is the exact form of the A-side quantity to be
compared.  This is `B4` of the ledger, now with its A-side half supplied.
