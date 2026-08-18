# 107.145 -- Classical Abel-Jacobi target control for Work Package III-B

## 1. Result

This note adds one genuine geometric control for Work Package III-B of
`107_00`.  It does not construct the Phase 107 realization map

\[
 \mathcal A_T:\operatorname{Div}_{\mathrm{EF}}(T)\to
 \widehat{\operatorname{Pic}}^0(\mathcal X_T),
\]

and it does not build the required arithmetic surface \(\mathcal X_T\).
What it does prove is that the target-side kernel logic demanded in
`107_11` is classically realizable on actual Jacobian objects already
available in Sage.

The verifier uses:

1. five actual elliptic curves over \(\mathbf Q\):
   `20a1`, `36a4`, `11a1`, `37a1`, `389a1`;
2. the fixed Paper 0 control
   \(E/\mathbf F_5: y^2=x^3+x+1\);
3. the genus-\(2\) control
   \(C/\mathbf F_5: y^2=x^5+x+1\).

It returns `YES` exactly when all of the following hold on those genuine
objects:

1. torsion divisor classes are the only visible real-kernel classes on
   the chosen elliptic controls;
2. the canonical-height Gram matrix is positive definite on the sampled
   free part;
3. the Paper 0 elliptic Jacobian control is nontrivial on explicit
   points;
4. the genus-\(2\) Jacobian separates explicit point-minus-infinity
   classes and realizes the hyperelliptic involution as inversion.

## 2. Why this matters

`107_11` asks for an exact kernel statement

\[
 \ker(f\mapsto \overline M_f)=\mathfrak R_W.
 \tag{2.1}
\]

At the current Phase 107 state this is still open because neither the
surface \(\mathcal X_T\) nor the realization map \(f\mapsto \overline
M_f\) has been built.  Still, the program needs a reality check on the
target side: the desired kernel behavior should occur on genuine Picard
and Jacobian targets, not only in symbolic finite shadows.

This note provides that control.  On actual elliptic curves over
\(\mathbf Q\), the divisor
\((P)-(O)\) maps to the classical Jacobian point \(P\in E(\mathbf Q)\),
torsion has height \(0\), and the free quotient has positive-definite
height pairing.  On an actual genus-\(2\) Jacobian over \(\mathbf F_5\),
explicit divisor classes \(P-\infty\) are nontrivial and are inverted by
the hyperelliptic involution.

So the target-side exact-kernel logic of III-B is not internally empty:
it occurs on real Jacobian objects.  What remains missing is the Phase
107 realization map into such objects.

## 3. Elliptic control over Q

The verifier splits the elliptic atlas into two kinds.

### 3.1. Pure torsion controls

For `20a1`, `36a4`, and `11a1`, Sage computes rank \(0\) and torsion
orders \(6\), \(2\), and \(5\), respectively.  Every torsion point
checked by the verifier has height \(0\).

This is the exact target-side behavior required by III-B after
realification: torsion classes are allowed to die, but no free class may
do so.

### 3.2. Free controls

For `37a1`, Sage returns rank \(1\) with generator \((0,-1)\).  For
`389a1`, Sage returns rank \(2\) with generators \((-1,1)\) and
\((0,-1)\).  The verifier checks:

1. every nonzero sampled integer combination of those generators has
   strictly positive canonical height;
2. the height Gram determinant is positive in ranks \(1\) and \(2\).

This gives an actual nondegeneracy check on the free quotient of
\(\operatorname{Pic}^0\) for real elliptic curves over \(\mathbf Q\).

## 4. Paper 0 and genus-2 Jacobian controls

The fixed Paper 0 control
\[
 E/\mathbf F_5:\ y^2=x^3+x+1
 \tag{4.1}
\]
has \(9\) rational points.  The verifier checks that explicit nonzero
points have nontrivial orders \(3\) or \(9\) in the Jacobian
\(E(\mathbf F_5)\cong\operatorname{Pic}^0(E)\).

For the genus-\(2\) curve
\[
 C/\mathbf F_5:\ y^2=x^5+x+1,
 \tag{4.2}
\]
Sage computes \(J(C)(\mathbf F_5)\) of order \(36\).  The verifier then
checks explicit divisor classes:

1. \(P-\infty\) is nontrivial for visible rational points \(P\);
2. the Weierstrass point \((2,0)\) gives an order-\(2\) class;
3. paired points with opposite \(y\)-coordinates map to inverse
   Jacobian classes.

This is the first III-B control in Phase 107 that touches a genuine
non-elliptic Jacobian object rather than only a symbolic finite shadow.

## 5. Scope boundary

This note does **not** prove any of the following:

1. existence of the Phase 107 regular proper models \(\mathcal X_T\);
2. existence of the realization map \(\mathcal A_T\) of `107_11`;
3. exact identification of the Weil radical inside the Phase 107 source
   space;
4. the terminal identity of `107_13`.

So Paper C remains `partial`.  The contribution here is narrower and
candid: the kernel/equality-case target logic demanded by III-B is now
anchored to genuine geometric Jacobians over \(\mathbf Q\) and
\(\mathbf F_5\), not only to abstract finite models.
