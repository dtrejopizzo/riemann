# 107.207 -- The absolute archimedean germ geometrizes the relative Fock determinant

## 1. New published geometric input

Connes--Consani, *On the Absolute Geometry of* \(\mathrm{Spec}\,\mathbb Z\)
[arXiv:2606.06604v1, Proposition 4.1], identify the space of
archimedean-local complex points over the stalk at \(p\) with \(\mathbb C\):

\[
 z\longmapsto \rho_z(t)=\exp(zt).
 \tag{1.1}
\]

The trivial point is \(z=0\).  Its complement is a torsor under
\(W_\infty=\mathbb C^\times\), acting by scalar multiplication.  The
Frobenius generator acts by \(z\mapsto pz\), and quotienting the
nontrivial locus by \(p^{\mathbb Z}\) gives the complex Tate curve
\(E_p=\mathbb C^\times/p^{\mathbb Z}\).

The important feature for Phase 107 is the fixed holomorphic germ at
the trivial point, not yet the quotient curve.

## 2. The local ideal filtration

Let \(\mathcal O_0\) be the holomorphic local ring at \(0\), with
maximal ideal \(\mathfrak m\).  For

\[
 q=p^{-s},\qquad \Re s>0,
 \tag{2.1}
\]

the Weil-group action \(z\mapsto qz\) fixes \(0\) and induces

\[
 T_qf(z)=f(qz)
 \tag{2.2}
\]

on germs.  Every \(\mathfrak m^r\) is invariant and the exact sequence

\[
 0\longrightarrow\mathfrak m^2
 \longrightarrow\mathfrak m
 \longrightarrow\mathfrak m/\mathfrak m^2
 \longrightarrow0
 \tag{2.3}
\]

is \(T_q\)-equivariant.  The quotient is the cotangent line at the
trivial point, and \(T_q\) acts on it by \(q\).

## 3. Identification with the Fock filtration

Complete the germs in the Hardy norm on a small invariant disk.  Then

\[
 \overline{\mathfrak m^r}=z^rH^2(\mathbb D)
 =\bigoplus_{n\ge r}\mathbb Cz^n.
 \tag{3.1}
\]

Under \(z^n\leftrightarrow e_n\), this is exactly
\(\mathcal F_{\ge r}\) of `107_196`, and \(T_qz^n=q^nz^n\).  Since
\(|q|<1\), the operator is trace class and

\[
 \det(1-T_q\mid\overline{\mathfrak m^r})
 =\prod_{n\ge r}(1-q^n).
 \tag{3.2}
\]

Fredholm multiplicativity in (2.3) therefore gives

\[
 \boxed{
 {\det(1-T_q\mid\overline{\mathfrak m})
  \over
  \det(1-T_q\mid\overline{\mathfrak m^2})}
 =\det(1-T_q\mid\mathfrak m/\mathfrak m^2)
 =1-q=1-p^{-s}.}
 \tag{3.3}
\]

### Theorem 3.1 (geometric germ realization)

The relative Fock determinant of `107_196` is the holomorphic Lefschetz
normal determinant of the fixed trivial point in the archimedean-local
Connes--Consani moduli space.  It is therefore derived from an actual
geometric ideal filtration and is not an ad hoc cancellation of the eta
tower.

## 4. Coordinate independence

Let \(w=uz+O(z^2)\), \(u\ne0\), be another local coordinate.  The
conjugated action has derivative

\[
 {d\over dw}\bigl(w(qz(w))\bigr)\big|_{w=0}=q.
 \tag{4.1}
\]

Thus its action on the intrinsic cotangent line
\(\mathfrak m/\mathfrak m^2\) is still multiplication by \(q\).
Equivalently, every finite jet matrix is conjugate to the triangular
matrix with diagonal \(q,q^2,\ldots\), and the determinant quotient in
(3.3) is coordinate independent.

## 5. What this closes and what it does not

This supplies the geometric realization missing from `107_196` at the
level of a local complex germ.  It also explains why the full flat-torus
determinant of `107_195` was too large: the Euler factor is the normal
determinant at the fixed point, not the scalar Laplacian determinant of
the entire Tate curve.

There is a sharp remaining boundary.  The proper quotient

\[
 E_p=\mathbb C^\times/p^{\mathbb Z}
 \]

removes the fixed point \(0\).  Hence (2.3) does not yet descend to a
coherent ideal sequence on \(E_p\), and this note does not construct:

1. a proper global arithmetic square containing the fixed germ;
2. a pushforward in arithmetic \(K\)-theory;
3. a Green current or diagonal intersection;
4. the archimedean distribution \(W_\infty\);
5. a Hodge form.

The next geometric problem is consequently precise: compactify the
trivial section without losing the local ideal filtration, and prove an
index/pushforward formula that sends its cotangent determinant to the
finite-prime character transported in `107_206`.

## 6. Falsifier

`107_207_archimedean_germ_geometrizes_fock_determinant.py` checks actual
prime twists at real and complex \(s\), exact finite-jet determinant
ratios, and conjugation by nonlinear local coordinates.  It must return
`NO` if the ideal filtration is not invariant, if the quotient weight
changes under a coordinate transformation, or if moving the action off
the fixed point is incorrectly accepted.

