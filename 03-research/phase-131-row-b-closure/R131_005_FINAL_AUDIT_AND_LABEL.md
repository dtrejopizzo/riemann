# R131.005 — Final audit of Paper 44 (round 2) and the closure decision


## 1. Round-2 re-check

| item | result |
|---|---|
| Lemma 3bis.3b, Thm 3bis.7′ | correct: on `Q` every ideal is principal, the norm class is the level set; `ω_fin` is purely atomic with support exactly `{±k log p}` and masses `(log p)p^{−k/2}`; local finiteness argument ✓ |
| amended B.4 wording (§6.2a′, §2, PLAN §6) | now formulated through the unique representing measure; `T` undefined on point masses stated; ✓ |
| Thm 8.1(iii),(iv) proofs | rewritten; the fallacy is deleted with the explicit counterexample `Λ = f∘log`; ✓ |
| P123.038 §5 / P123.039 §5 | quoted in full; one ledger row; ✓ |
| B.3 dagger extension to `Q_{>0}^×`, `|S_f| = 1` remark, `ω_∞(log n)` rename, citations | ✓ |
| numerics | `scripts/verify_131_contacts.py` ALL CHECKS PASS (re-run) |

No new findings.

## 2. Rulings on the two items the construction left `PARTIAL`

**B.7 (mechanism).**  The stopping rule of PLAN §6 asks to compute both
contacts for `p`, `p²` and, if they differ, to *locate the geometric mechanism
producing the cyclotomic factor*, without substituting one determinant for
another.  Both contacts are computed (Thm 6.4) and differ.  The factor that
actually enters row A's trace is `Λ(p^k) = log p`, and its mechanism on the
carrier is located: the multiplicative Haar volume of the valuation shell,
`k`-independent by translation invariance, with the fixed-point weight
identically `1` on the shell (Thm 6.5).  The cyclotomic *polynomial* lives on
the `Z`-model `G_m/Z`, where its mechanism is also located (deck group `μ_n`,
Lemma 3.1, Thm 6.4(iv)).  No determinant was substituted for another: the two
agree in degree (Thm 3bis.10) and the paper says a map between the two
locations is not supplied.  A functor from the `C`-linear carrier to the
`Z`-model carrying `Z/p` is **impossible** (P123.022), so the missing map is
not an open item of this theory but a refuted one.  **Ruling: B.7 `PROVED`**
(test and mechanism on the carrier), with Rem 6.5a′'s sentence retained.

**The P123.038 §5 / P123.039 §5 arrow.**  Its three demands are: (a) the
lattice-index operation realized as the admissible diagonal shadow; (b)
extended cyclically to mixed correspondences; (c) compared with the analytic
nuclear trace.  After phase 130, (b) and (c) exist on the carrier: Paper 43's
`T` is a cyclic trace on all mixed smeared correspondences (Thms 8A.3–8A.4),
nuclear-continuous on `𝓐_tr` (Thm 8A.7b), and Thm 3bis.7/3bis.10 compare it
with the lattice index in degree.  What is not — and cannot be — supplied is
(a) at object level: the lattice-index *operation* acts on `Z`-lattices and
produces `Z/n`, which no additive functor from the `C`-linear carrier carries
(P123.022).  **Ruling: CLOSED in degree, REFUTED at object level on the
declared carrier; "OPEN for an integral carrier" means a different theory,
outside the declared one.**  The row stays as the construction wrote it, with this
ruling attached.

## 3. Renaming test

Row B's content — the norm classes as objects with composition, dagger (on
`Q_{>0}^×`), bidegree; the contact-locus theorem (arithmetic recovered from an
arithmetic-free family by its contact with the diagonal); the element/norm
dichotomy and the withdrawal of the `n−1` obligation; the degree matching with
the integral cube; membership in `N_A^{dist}` with canonical components; the
non-primitivity of the classes — is not stated or implied by the explicit
formula.  `T(Γ_h)` is the geometric side of that formula because row A's trace
is (Paper 43 Rem 9.7a), and row B inherits that; it adds no identity with a
sum over zeros.  **Pass.**

## 4. Decision

Contract (Paper 44 §2, mirroring the row-A closure rule): every clause proved,
and the audit of record finds no renaming.  B.1–B.3, B.5–B.9 are `PROVED` on
Paper 43's declared carrier (with the honest notes in the ledger).  B.4 is
`REFUTED AS STATED` and `PROVED AS AMENDED`; the amendment is a decision of the
repository record, exactly as A.6 was.

    ROW B: WEIL-STRENGTH-COMPLETE on Paper 43's declared carrier,
           CONDITIONAL ON ACCEPTANCE OF THE B.4 AMENDMENT
           (text: Paper 44 §6.2a′; PLAN §6 item 4 note).
           If the amendment is rejected, B.4 stands REFUTED on this carrier
           and row B is CONSTRUCTED.

Recorded beside the label: the objects are norm classes and forget
factorization (Lemma 3bis.3b); the arithmetic is the contact locus
(Thm 3bis.7′); the source has no dagger and B.3 is proved on `Q_{>0}^×`;
`Λ`-as-shell-volume is inherited from Paper 43; `Z/Φ_n(1)` is not an object of
`G`; no zeros, no sign, the classes are not primitive (Thm 8.3(v)).  The
round-1 audit graded the label NOT EARNED before the round-2 repairs;
its findings are all disposed of in R131.004 and re-checked here.
