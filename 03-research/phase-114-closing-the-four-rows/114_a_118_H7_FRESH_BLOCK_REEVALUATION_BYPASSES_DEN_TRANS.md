# 114.a.118 — H7: fresh-block reevaluation bypasses DEN-TRANS degreewise

```
+------------------------------------------------------------------------+
| OLD NO-GO   A retained F_p block cannot evaluate a later denominator p.|
| FRESH       Choose a new canonical controlled prime for every divisor. |
| PRODUCT     Reevaluate both factors in the fresh block for D+E.         |
| RESULT      Degreewise image size and source multiplication are defined.|
| LIMIT       No transition maps, restriction exactness or cohomology yet.|
+------------------------------------------------------------------------+
```

## 1. Canonical degreewise blocks

Let `D` be an effective class in the ordered external presentation
`Pic(X) x Pic(X)` for the repaired square.  Use the standard representative
construction of `a53` independently on both curve factors.  It produces
intrinsic finite denominator heights and residual real metrics depending only
on that ordered pair.  Invariance under a possible anti-diagonal identification
inside `Pic(Y^reg)` is not assumed here; `a121` identifies it exactly with
anti-diagonal faithfulness.

Choose the rank `m(D)`, the calibrated coordinate number `k(D)` and then the
**least** prime `p(D)` satisfying the finite conditions of `a51`:

1. `p(D)` exceeds every denominator and coefficient bound used at degree
   `D`;
2. every retained odd exponent is invertible modulo `p(D)-1`;
3. the interpolation nodes required by the chosen block remain distinct.

Existence follows from the controlled-prime theorem in `a51`.  Taking the
least admissible prime makes the block a function of the standard
representative rather than an auxiliary choice.  Let

\[
 \mathcal E_D:H^0_{\rm bd}(D)\longrightarrow
 T_D:=\mathbb F_{p(D)}^{k(D)}                                           \tag{1.1}
\]

be the selected full-bio evaluation and define

\[
 h_{\rm fresh}(D)=\log\#\operatorname{im}\mathcal E_D.                 \tag{1.2}
\]

Every denominator of `D` is invertible in `T_D`, so (1.1) is typed.  On the
saturated rays of `a117`, it agrees with `h_cal` and has the sharp quadratic
coefficient.

## 2. Why the old denominator obstruction does not apply

The no-go `a57` considers a nested target retaining an old characteristic
`p` after the divisor cone later admits `1/p`.  Construction (1.1) retains
no old residue block.  If `p(D)` divides a denominator of a later divisor
`E`, then `p(E)` is, by definition, another admissible prime.

There is deliberately no claimed unital map

\[
 T_D\longrightarrow T_E.                                               \tag{2.1}
\]

Thus the impossible operation “evaluate `1/p(D)` in characteristic `p(D)`”
is never requested.  This is a bypass of H7-DEN-TRANS for degreewise image
cardinalities, not a construction of DEN-TRANS.

## 3. Multiplication by reevaluation at the sum degree

For effective `D,E`, Haran's external section multiplication gives

\[
 H^0_{\rm bd}(D)\times H^0_{\rm bd}(E)
 \longrightarrow H^0_{\rm bd}(D+E),\qquad(s,t)\longmapsto st.           \tag{3.1}
\]

Evaluate the entire diagram using the fresh bio of `D+E`.  Since
`mathcal E_(D+E)` is a bio homomorphism,

\[
 \mathcal E_{D+E}(st)
 =\mathcal E_{D+E}(s)\mathcal E_{D+E}(t),                               \tag{3.2}
\]

where the two factors on the right mean direct reevaluation of the source
sections in `T_(D+E)`, not transport of their old values from `T_D,T_E`.

### Theorem 3.1 (degreewise multiplicative typing)

The fresh-block invariant is defined for every standard effective class and
is compatible with multiplication in the source in the exact sense (3.2).
No residue-characteristic transition is required.

This satisfies the multiplication clause needed to test products at a fixed
output degree.  It does not supply a graded ring formed by the finite targets
themselves.

## 4. Principal and sign invariance

Adding a principal arithmetic divisor separately on either curve factor does
not change the ordered standard representative and therefore does not change
`m(D),k(D),p(D)` or `T_D`.
Two transports to the standard representative differ by the global curve
unit `+/-1`.  All retained exponents are odd, so the two image sets in
(1.2) differ by coordinatewise sign, a bijection.  Hence

\[
 h_{\rm fresh}(D+\operatorname{div}f)=h_{\rm fresh}(D).                 \tag{4.1}
\]

This is the same valid per-block argument retained in `a53`, now without the
retracted accumulated target.

## 5. Remaining exactness gate

Fresh reevaluation removes the denominator collision from **definition,
factorwise principal invariance and output-degree multiplication**.  It does
not give:

1. transition maps between `T_D` and `T_E`;
2. functorial maps for restrictions to Cartier subschemes;
3. kernels/cokernels or a long exact cohomology sequence;
4. a proof that the calibrated rule exists with the sharp coefficient on
   every positive ray, rather than the saturated rays of `a117`;
5. the geometric H7-REG-EXCESS-RR realization.
6. descent through a nontrivial anti-diagonal relation in the square Picard
   group.

Thus H7-DEN-TRANS is no longer necessary for a degreewise scalar dimension,
but a sheaf/cohomological RR theory still needs the new gate
**H7-FRESH-EXACT**.  Row A and RH remain open.

## 6. Verification scope

`114_a_118_h7_fresh_block_reevaluation_verify.py` checks canonical fresh
prime selection in finite models, denominator invertibility, failure of old
transition maps, direct product reevaluation and sign invariance.  The
existence and typing of the full bio evaluations are the theorems of `a49`
and `a51`.
