# 107.51 -- Paper D A6 functoriality shadow audit

## 1. Purpose

Route A item A6 of `107_12` asks for target-side functorial
compatibility of the realization map.  The present note exact-audits the
finite algebraic shadow of that requirement.

## 2. What is audited

The verifier `107_51_paper_d_a6_functoriality_shadow_audit.py` checks
four exact finite statements.

1. Additivity of the realization map.
2. Compatibility with transpose.
3. Discrete scaling covariance on a finite visible sub-semigroup.
4. Pullback/pushforward compatibility with the transported pairing.

## 3. Finite shadow being tested

The script uses a finite visible basis of source generators together
with:

1. a finite realization map;
2. a source pairing and its negative target counterpart;
3. a transpose involution;
4. one finite pullback operator modeling a visible correspondence
   shadow;
5. two exact discrete scaling factors corresponding to visible critical
   weights.

This is the finite functoriality logic behind A6, not the final target
theorem.

## 4. Result

The verifier passes exactly.

It confirms that:

1. the finite realization shadow is additive;
2. transpose compatibility can be checked exactly at the generator
   level;
3. a discrete version of the critical scaling covariance is compatible
   with realization;
4. one visible pullback shadow preserves the bilinear comparison pattern.

So A6 now has a genuine finite witness, not only a prose checklist.

## 5. Scope boundary

This audit does **not** prove:

1. the actual pullback/pushforward theorem on a realized arithmetic
   target;
2. the full continuous scaling covariance of `107_11`;
3. the real geometric functoriality needed by Faltings--Hriljac or
   Yuan--Zhang.

Its force is exact but finite: it pressure-tests the functorial logic
that the eventual realization must satisfy.
