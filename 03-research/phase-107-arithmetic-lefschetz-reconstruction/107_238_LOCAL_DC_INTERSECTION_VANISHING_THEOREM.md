# 107.238 -- Local DC intersection vanishes; the Weil term is a corner term

## 1. Hessian of a homogeneous correspondence potential

Let

\[
 U(x,y)=x\,u(r),\qquad r=\frac yx,\qquad x,y>0,
 \tag{1.1}
\]

where \(u\) is twice differentiable in the distributional sense.  Direct
differentiation gives

\[
 \nabla^2U=\frac{u''(r)}x
 \begin{pmatrix}
 r^2&-r\\
 -r&1
 \end{pmatrix}
 =\frac{u''(r)}x\,v_rv_r^T,
 \qquad v_r=(r,-1)^T.
 \tag{1.2}
\]

The matrix has rank one and determinant zero.  More importantly, for any two
homogeneous potentials \(U=xu(r)\) and \(V=xv(r)\), their Hessians at the same
point are scalar multiples of the same rank-one matrix \(v_rv_r^T\).

## 2. Local mixed-intersection no-go

For symmetric \(2\times2\) matrices define the mixed determinant by

\[
 \mathrm{MD}(A,B)
 =\frac12\bigl(\det(A+B)-\det A-\det B\bigr).
 \tag{2.1}
\]

### Theorem 2.1

For every pair of correspondence potentials \(U_f,U_g\) constructed in
107_237,

\[
 \boxed{
 \mathrm{MD}(\nabla^2U_f,\nabla^2U_g)=0
 }
 \tag{2.2}
\]

on the punctured positive quadrant.  Consequently the ordinary local mixed
Monge--Ampere/tropical intersection of the two diffuse DC divisor currents
vanishes there.

### Proof

By (1.2), \(A=a\,v_rv_r^T\) and \(B=b\,v_rv_r^T\).  The matrices \(A\),
\(B\), and \(A+B\) all have rank at most one, hence all three determinants
in (2.1) vanish. \(\square\)

The same conclusion is visible before passing to diffuse currents.  Two
distinct Frobenius rays

\[
 L_\lambda:\ y=\lambda x,\qquad
 L_\mu:\ y=\mu x
 \tag{2.3}
\]

with \(\lambda\ne\mu\) have no intersection for \(x>0\).  Their only common
point in the closed quadrant is the corner \((0,0)\).  Parallel self-products
on one ray likewise have no ordinary transverse local intersection.

## 3. Consequence for the required Weil pairing

Connes--Consani's RR strategy requires

\[
 D_f\bullet D_g
 =\langle D_f\star\widetilde D_g,\Delta\rangle
 =N(f\star\widetilde g),
 \tag{3.1}
\]

where \(N\) is the nonzero counting distribution of the explicit formula.
The 2018 paper also records that the naive diagonal self-intersection has a
divergent \(\log\Lambda\) term and explicitly requires a renormalized
intersection theory.

Theorem 2.1 proves that (3.1) cannot come from integrating a local Hessian or
ordinary mixed Monge--Ampere density over the smooth interior of the Scaling
square.  Every nonzero contribution must be supported by global data lost on
the punctured chart:

1. the common corner of all Frobenius rays;
2. the periodic/adelic quotient and its isotropy;
3. the diagonal renormalization producing the distribution \(N\).

Thus the next intersection cannot be chosen by local analogy with convex
geometry.  It must be a **corner functional** fixed by the global trace
formula.

## 4. Exact design restriction

Let \(I_{\mathrm{loc}}\) be any bilinear pairing on the DC currents which is
obtained solely by integrating a pointwise mixed determinant of their local
Hessians on \((0,\infty)^2\).  Then

\[
 I_{\mathrm{loc}}(D_f,D_g)=0
 \qquad\text{for all }f,g.
 \tag{4.1}
\]

Since the required pairing (3.1) is not identically zero,

\[
 \boxed{I_{\mathrm{loc}}\ne I_{\mathrm{Weil}}.}
 \tag{4.2}
\]

This closes the naive local intersection extension.  It does not close the
DC completion itself: 107_237's divisor map remains valid.

The only surviving gate is now sharply stated:

\[
 \boxed{
 \text{construct the corner/diagonal functional intrinsically and prove}
 \ I_{\partial}(D_f,D_g)=N(f\star\widetilde g).}
 \tag{4.3}
\]

Defining \(I_\partial\) by the right-hand side would be circular and is not
allowed.  It must arise from the quotient geometry, a trace/residue, or a
renormalized diagonal construction.

## 5. Status

\[
 \boxed{\texttt{LOCAL\_DC\_INTERSECTION: CLOSED\_ZERO}.}
\]

Row (a) remains `partial`; the global corner functional, RR existence, and
\(H^1\) remain open.  Row (c) is not reopened by this theorem.

## 6. Machine certificate

Run

```bash
/home/trabajo/miniforge3/bin/python \
  107_238_local_dc_intersection_vanishing.py
```

The certificate derives the two Hessians symbolically, checks their mixed
determinant, tests distinct real Frobenius rays on a fixed five-pair atlas,
and reads the required nonlocal pairing and diagonal divergence from the
2018 source.
