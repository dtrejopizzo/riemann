# 107.49 -- Paper C pairing-transport shadow audit

## 1. Purpose

`107_11` and `107_13` meet at one load-bearing comparison:

\[
 \langle D_f,D_g\rangle_{\rm src}
 =
 -\,\widehat{\deg}(\overline M_f\cdot \overline M_g).
 \tag{1.1}
\]

The present note exact-audits the finite algebraic shadow of that
comparison before the full geometric realization exists.

## 2. What is audited

The verifier `107_49_paper_c_pairing_transport_shadow_audit.py` checks
four exact finite statements.

1. Generator comparison on a visible finite basis.
2. Bilinear extension from generators to arbitrary finite-support
   divisors in the test window.
3. Primitive self-pairing compatibility after polarization correction.
4. Compatibility with one explicit radical direction.

## 3. Finite shadow being tested

The script uses:

1. a finite source pairing matrix representing the Paper A side;
2. a finite target height matrix representing the candidate realized
   side;
3. the exact relation that the target matrix is the negative of the
   source matrix;
4. one explicit radical direction that lies in the kernel of both
   bilinear forms.

This is the finite bilinear shadow of the pairing-transport requirement,
not the final arithmetic-surface theorem.

## 4. Result

The verifier passes exactly.

It confirms that:

1. checking the comparison on generators is enough to force it on all
   finite-support linear combinations;
2. the primitive degree-zero projection remains compatible with the
   transported self-pairing;
3. the radical/equality-case logic can be incorporated at the bilinear
   comparison stage, not only after the terminal identity is stated.

So the comparison target of `107_11` now has an exact finite witness,
not just a prose requirement.

## 5. Scope boundary

This audit does **not** prove:

1. the actual geometric height pairing on \(\mathcal X_T\);
2. the true generator comparison on the realized target classes;
3. the analytic Gamma--polar metric comparison;
4. the full terminal identity of `107_13`.

Its force is exact but finite: it pressure-tests the bilinear transport
logic that the eventual realization must satisfy.
