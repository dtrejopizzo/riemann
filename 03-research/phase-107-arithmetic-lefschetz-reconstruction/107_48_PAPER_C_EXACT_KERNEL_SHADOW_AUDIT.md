# 107.48 -- Paper C exact-kernel shadow audit

## 1. Purpose

`107_11` demands the sharpest equality-case gate of Phase 107:

\[
 \ker(f\mapsto \overline M_f)=\mathfrak R_W.
 \tag{1.1}
\]

The present note does not prove the full Picard/Jacobian realization.
It exact-audits the finite algebraic shadow that any such realization
must satisfy once realified.

## 2. What is audited

The verifier `107_48_paper_c_exact_kernel_shadow_audit.py` checks four
exact finite statements.

1. Designated radical generators map to torsion classes.
2. After tensoring with \(\mathbf R\), those radical generators vanish.
3. Non-radical witnesses survive in the free part and therefore cannot
   lie in the real kernel.
4. The real kernel is exactly the span of the designated radical
   generators, not a larger subspace.

## 3. Finite shadow being tested

The script uses a finite realization shadow with:

1. a finite-rank source module carrying two explicit radical directions
   and several non-radical witnesses;
2. a torsion part modeling the “maps to torsion” clause of `107_11`;
3. a free part modeling the realified Picard/Jacobian target.

The exact-kernel audit is then performed on the free part, while the
torsion part records the finite-level radical-jet behavior.

This is the finite algebraic version of the logic stated in `107_11`
and reinforced by the projection-kernel identities cited there through
Phase 106.

## 4. Result

The verifier passes exactly.

It confirms that:

1. radical modes can die after realification while remaining visible as
   torsion before realification;
2. non-radical witnesses do not die after realification;
3. the real kernel can be checked sharply as an equality, not merely as
   an inclusion.

So `107_11` now has an exact audit for the kernel logic itself, even
though the actual geometric realization map is still open.

## 5. Scope boundary

This audit does **not** prove the full content of `107_11`.  It does not
construct:

1. the actual Picard/Jacobian realization on \(\mathcal X_T\);
2. the true Gamma--polar metric on the target line bundles;
3. the genuine pairing transport identity;
4. the real arithmetic proof that the geometric kernel equals
   \(\mathfrak R_W\).

Its force is exact but finite: it pressure-tests the equality-case logic
that the eventual realization must obey.
