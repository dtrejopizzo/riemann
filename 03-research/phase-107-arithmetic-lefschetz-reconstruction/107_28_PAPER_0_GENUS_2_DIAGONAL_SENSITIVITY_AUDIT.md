# 107.28 -- Paper 0 auxiliary audit: genus-2 diagonal sensitivity control

## 1. Purpose

Paper 0 uses the fixed elliptic control

\[
 E/\mathbf F_5:\qquad y^2=x^3+x+1,
 \tag{1.1}
\]

so its primitive diagonal entries are

\[
 (\Delta^0)^2=-2,
 \qquad
 (\Gamma_n^0)^2=-2\cdot 5^n.
 \tag{1.2}
\]

That is correct for genus \(g=1\), but by itself it does **not** test
whether the same route tracks the genus factor or merely hard-codes the
elliptic diagonal values.

This note adds the missing falsifier:

\[
 \text{replace }g=1\text{ by }g=2
 \quad\text{and test whether the diagonal entries become}\quad
 -2g,\ -2gq^n.
 \tag{1.3}
\]

It is an auxiliary audit, not a replacement for `107_02`.  It now does
so in two regimes: one supersingular equality-case control and one
ordinary non-extremal control.

## 2. What the audit measures

For a smooth proper curve \(C/\mathbf F_q\) of genus \(g\), the
primitive two-dimensional Gram package takes the form

\[
 (\Delta^0)^2=-2g,
 \qquad
 (\Gamma_n^0)^2=-2g\,q^n,
 \qquad
 \Gamma_n^0\cdot\Delta^0=-a_n,
 \tag{2.1}
\]

so that

\[
 \det G_n^0=4g^2q^n-a_n^2.
 \tag{2.2}
\]

Thus the genus enters only through the two diagonal entries.

If a purported source route always returns \(-2\) and \(-2q^n\), then
the fixed elliptic control passes while a genus-2 control fails.  This
is exactly the failure mode the present audit is designed to detect.

## 3. Fixed genus-2 controls

### 3.1. Supersingular control

Use the hyperelliptic curve

\[
 C/\mathbf F_2:\qquad y^2+y=x^5+x^2.
 \tag{3.1}
\]

Because the degree is \(5=2g+1\), the curve has genus \(g=2\) and one
point at infinity.  Also

\[
 \frac{\partial}{\partial y}(y^2+y-x^5-x^2)=1,
 \tag{3.2}
\]

so the affine model has no singular points.

This curve is supersingular, and at \(n=8\) the determinant saturates
exactly:

\[
 a_8=64,
 \qquad
 \det G_8^0=16\cdot 2^8-64^2=0.
 \tag{3.3}
\]

So it tests the equality case, not only strict inequality.

### 3.2. Ordinary control

Use also the genus-2 curve

\[
 C_{\rm ord}/\mathbf F_3:\qquad y^2=x^5+x.
 \tag{3.4}
\]

The verifier computes \(N_1\) and \(N_2\) and recovers the degree-two
Weil coefficient

\[
 e_2=\frac{s_1^2-s_2}{2},
 \qquad
 s_n=q^n+1-N_n,
 \tag{3.5}
\]

checking that

\[
 e_2\not\equiv0\pmod 3,
 \tag{3.6}
\]

which is the ordinary witness used here.

## 4. Exact verifier

The new exact verifier is

- `107_28_genus2_diagonal_sensitivity.py`

It now counts points on:

1. \(C(\mathbf F_{2^n})\) for \(1\le n\le 8\) by using the
   characteristic-2 criterion

\[
 y^2+y=a
 \quad\Longleftrightarrow\quad
 \operatorname{Tr}_{\mathbf F_{2^n}/\mathbf F_2}(a)=0,
 \tag{4.1}
\]

   in which case there are exactly two \(y\)-solutions; and
2. \(C_{\rm ord}(\mathbf F_{3^n})\) for \(1\le n\le 6\) by direct
   square testing in \(\mathbf F_{3^n}\).

The script then defines

\[
 a_n=2^n+1-\#C(\mathbf F_{2^n})
 \tag{4.2}
\]

On each row it checks the genus-2 Gram determinant

\[
 16\cdot 2^n-a_n^2 \ge 0,
 \tag{4.3}
\]

equivalently

\[
 |a_n|\le 4\cdot 2^{n/2}.
 \tag{4.4}
\]

## 5. What passed

Running the verifier on Friday, July 31, 2026 gives:

\[
 (N_1,a_1)=(5,-2),\qquad
 (N_2,a_2)=(9,-4),\qquad
 (N_3,a_3)=(5,4),
 \tag{5.1}
\]

\[
 (N_4,a_4)=(17,0),\qquad
 (N_5,a_5)=(25,8),\qquad
 (N_6,a_6)=(81,-16),
 \tag{5.2}
\]

and the determinant check remains nonnegative through \(n=8\), with
equality at \(n=8\).

For the ordinary control, the verifier also finds

\[
 e_2=2,
 \qquad
 e_2\equiv 2 \pmod 3,
 \tag{5.3}
\]

so the control is not in the supersingular extremal configuration.

## 6. What this does and does not prove

What it does prove:

1. the genus factor in the primitive diagonal package is a real audit
   target and is not invisible to exact arithmetic;
2. the supersingular equality case and an ordinary non-extremal case are
   both easy to state and verify independently of the elliptic
   preflight;
3. the old verifier `107_01_function_field_preflight.py` is elliptic and
   does **not** test genus sensitivity by itself.

What it does not prove:

1. it does not rewrite `107_02` into a genus-free source-construction
   theorem;
2. it does not show that the Phase 107 source operations already derive
   the factor \(g\) rather than merely fitting the elliptic case;
3. it does not validate any of Part III or Part IV over
   \(\operatorname{Spec}\mathbf Z\).

## 7. Status consequence

Paper 0 remains proved for the fixed positive elliptic control.
However, genus-sensitive portability of the primitive diagonal package
is now explicitly separated as an auxiliary falsifier audit, rather than
being silently assumed to come for free from the elliptic case.  The
auxiliary gate is now tested in both a supersingular equality-case and
an ordinary non-extremal genus-2 configuration.
