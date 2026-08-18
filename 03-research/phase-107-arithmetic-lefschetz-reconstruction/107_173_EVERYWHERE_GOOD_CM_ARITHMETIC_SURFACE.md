# 107.173 -- An everywhere-good arithmetic surface for the fixed CM control

## 1. The explicit field and curve

Retain

\[
 K=\mathbb Q(\alpha),\qquad \alpha^2+3\alpha+5=0,
\]

and put

\[
 w^2=2\alpha+3,\qquad L=K(w).
\]

Since \((2\alpha+3)^2=-11\), the field \(L\) has degree four over
\(\mathbb Q\).  Over \(L\), consider

\[
 E_L:\qquad
 y^2+w y=x^3+\alpha x^2-(\alpha+1)x.
 \tag{1.1}
\]

All coefficients in (1.1) are algebraic integers.  Direct evaluation of
the Weierstrass invariants gives

\[
 \Delta(E_L)=1,qquad j(E_L)=-32768.
 \tag{1.2}
\]

Thus (1.1) defines an elliptic scheme

\[
 \mathcal E_L\longrightarrow\operatorname{Spec}\mathcal O_L
\]

with good reduction at every finite prime.

## 2. Identification with the Paper-0 CM lift

The curve of `107_171`, base-changed to \(L\), is transformed to (1.1)
by the admissible Weierstrass change

\[
 (u,r,s,t)=(w,-\alpha-3,0,-6).
 \tag{2.1}
\]

Indeed

\[
 w^{12}=(-11)^3=-1331,
\]

so (2.1) changes the old discriminant \(-1331\) into the unit
discriminant in (1.2).  This also explains geometrically why the
quadratic extension \(L/K\) resolves the type \(I_0^*\) fibre found at
the ramified prime above 11 in `107_172`.

The CM action by \(\mathcal O_K\) is defined on the generic fibre over
\(L\).  Every such endomorphism extends uniquely over
\(\operatorname{Spec}\mathcal O_L\), because \(\mathcal E_L\) is an
abelian scheme over a normal base.

## 3. A proper smooth arithmetic product

Define

\[
 \mathcal X_L=
 \mathcal E_L\times_{\operatorname{Spec}\mathcal O_L}\mathcal E_L.
 \tag{3.1}
\]

Then \(\mathcal X_L\) is proper and smooth of relative dimension two
over the complete arithmetic base \(\operatorname{Spec}\mathcal O_L\).
It carries globally:

1. the two rulings \(F_1,F_2\);
2. the diagonal \(\Delta\);
3. every CM graph \(\Gamma_{\alpha^n}\);
4. the finite flat intersections
   \(\Gamma_{\alpha^n}\cap\Delta=\ker(\alpha^n-1)\).

Their degree over the base is

\[
 \deg\ker(\alpha^n-1)
 =N_{K/\mathbb Q}(\alpha^n-1)
 =\#E(\mathbb F_{5^n}).
 \tag{3.2}
\]

Consequently the two Paper-0 rulings, all graph correspondences, the
point-count intersections, and the centered Hodge matrices coexist on
one regular proper arithmetic surface with no finite places removed.

At primes over 5 the residue field of \(L\) is \(\mathbb F_{25}\).
The endomorphism \(\alpha\) still reduces to the geometric
\(\mathbb F_5\)-Frobenius on the base-changed Paper-0 curve; it is not
the relative \(\mathbb F_{25}\)-Frobenius.  This distinction is part of
the construction, not a defect.

## 4. Exact scope

This is the first Phase-107 construction of an actual proper smooth
relative surface over an entire arithmetic base that carries the full
Paper-0 correspondence package.  It proves existence for one fixed CM
control after a degree-four number-field extension.

It is **not** the requested universal surface over
\(\operatorname{Spec}\mathbb Z\).  The field \(L\), the curve, and the
endomorphism \(\alpha\) are tailored to the fixed elliptic Frobenius
polynomial.  Formula (3.2) realizes the zeta function of that elliptic
curve, not the prime/Gamma explicit formula for Riemann zeta.  Rows (a),
(c), and (d) for \(\operatorname{Spec}\mathbb Z\) remain open, and no
paper is promoted by this calibration.

## 5. Falsifier

The Sage verifier constructs \(L\), checks the degree and defining
relations, constructs both Weierstrass models, verifies the explicit
isomorphism, unit discriminant, trivial conductor and absence of bad
local data, and checks the graph-kernel degrees through \(n=16\).  It
returns `VERDICT: NO` if any prerequisite of (3.1) fails.
