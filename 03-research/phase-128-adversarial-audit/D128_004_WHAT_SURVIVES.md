# D128.004 — what survives, and what would earn the strong labels

Date: 2026-09-12.

## Honest labels, replacing the three withdrawn ones

```text
ROW A:  CONSTRUCTED on the automorphism-graph sector G, with its dagger,
        its excision and its classical control.  A.5 is NOT addressed.
        A.6 depends on a ruling plane whose descent P123.013 refutes.
        A.8 asserts what P123.108/109 disclaim.  The analytic invariant T
        is CANDIDATE: Definition 8.1 evaluates a small-test germ outside
        its domain and is never proved equal to the lattice sum it is
        computed with.  The non-invertible sector, where Weil's argument
        lives, is absent.

ROW B:  CONSTRUCTED.  The arithmetic family Γ_n lives in G with its
        composition, dagger and half-density (PROVED).  The two contact
        operations of P123.060 have COPRIME SUPPORT on Spec Z (PROVED,
        and this is row B's real contribution).  Prim is NOT monoidal for
        ⊗^L (PROVED here).  deg_det Prim_n = Λ(n) on the Z-linear models
        (PROVED).  B.4 is REFUTED AS STATED: the derived diagonal contact
        is the fixed complex, differential n−1, not the cyclotomic one.
        The realization of the integral contact as a shadow of G is OPEN.

ROW C:  ASSEMBLED AND NORMALIZATION-COMPATIBLE, NOT LOCALIZED.  The finite
        local terms W_p (P123.042/046) and the archimedean distribution
        W_∞ (P123.035) sum, term by term, to the arithmetic side of the
        Weil explicit formula in the corpus's own normalizations, with
        Meyer's theorem removed (PROVED).  The polar packet IS the
        hyperbolic ruling form (PROVED).  Sufficiency of the primitive
        class for Weil's criterion (PROVED — this closes a real gap).
        OPEN: that the sum is the relative character of the carrier; that
        the multiple-zero strata vanish (Thm 5.4 WITHDRAWN); the
        canonicity of the f(1) counterterm.
```

## What genuinely survives, across the three rows

These are the results the audits confirmed, or could not damage, and they are
worth keeping regardless of the labels.

1. **Coprime support** (row B, Thm. 3.3(i)–(iii)).  `V(n) ∩ V(n−1) = ∅`, so the
   ramified and unit local factors of the arithmetic class never occupy the
   same place; `μ_n` is the deck group and `μ_{n−1}` the fixed group of the
   same morphism (Lemma 3.1).  Elementary, correct, and it is the right way to
   read P123.060 — provided one does not claim it *realizes* either contact.

2. **`Prim` is not monoidal** (row B, corrected).  `Z/2 ⊗^L Z/2 = Z/2 ⊕ Z/2[1]
   ≇ Z/2`.  This closes P123.037 §5's open item properly.

3. **The polar packet is the hyperbolic ruling form** (row C, Thm. 8.1).
   `M_+conj(M_−) + M_−conj(M_+)` is literally `β_T`.  Hence primitivity is the
   vanishing of the ruling component.  Verified against P123.036 and P123.008.

4. **Sufficiency for Weil's criterion** (row C, Thm. 10.4).  `Π = −∂_t² + ¼`
   multiplies the entire function by `s(1−s)`, kills both Tate moments,
   preserves support, reality, parity and exponential type, and is invertible
   at every nontrivial zero; so `106_11`'s construction runs on primitive
   targets.  This closes the gap `113_07` had flagged and nobody had covered.
   Checked line by line by the audit and confirmed.

5. **Meyer is removable** (row C, §7).  `W_∞` is proved outright in P123.035,
   constant computed, and P123.035 §1's Gaussian test shows the literal Meyer
   archimedean coefficient is `−1/2`, not `−1`.  Row C no longer needs the
   citation — and the two computations `K(t) = Tr e^{−tN_Γ}` and
   `det_ζ(N_Γ+s−½) = √(2π)2^{1/2−s/2}/Γ(s/2)` are correct, if less than the
   slogan claimed.

## What would earn the strong labels

**Row A.**  (a) Write clause A.5: declare the trace-class domain and `T_A`,
prove cyclicity and restriction-compatibility.  (b) Give Definition 8.1 a
well-posed meaning: either prove `log(germ) = reg-Σ(8.2)`, or define `T` by a
specified regularization of (8.2) and prove existence and independence.
(c) Construct the external Tate characters directly on `N_A`, or withdraw A.6.
(d) Prove or withdraw A.8.  (e) Prove Prop. 3.2, Thms. 6.1, 9.1, 10.2, 10.5.
(f) Decide the non-invertible sector.

**Row B.**  (a) Realize the integral contact as a shadow of a declared
category — which requires an integral carrier, since a `C`-linear shadow cannot
carry `Z/p` (P123.022).  (b) Supply the cyclic extension to mixed
correspondences and the comparison with the analytic trace that P123.038 §5 and
P123.039 §5 actually demand.

**Row C.**  (a) Prove an excisive localization of the character along the
filtration (1.4) — this is P123.048 §5's missing result, and it is the real
content of "no corner terms".  (b) Compute the deep strata's `f(1)`
coefficient and show the total is cutoff-independent.  (c) Then, and only then,
`Σ_p W_p + W_∞` becomes an intersection number rather than an assembly.

## Method note

All three audits were adversarial and all three found real errors.  One finding
was verified **wrong** and rejected (D128.001 R1: the local factor does exist
pointwise at a fixed unit twist).  The pattern the row-A audit named — "each
correction preserved the conclusion by construction" — is the failure mode to
avoid; that is why the labels are withdrawn here rather than qualified.
