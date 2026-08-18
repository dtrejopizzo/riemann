# 107.01 — Paper 0 function-field calibration specification

## 1. Purpose

Paper 0 is a positive control for the categorical interface proposed in
107.00.  It must reconstruct Weil's correspondence--Lefschetz--Hodge
chain by explicit operations on one fixed curve.  It may use the
classical Hodge-index theorem only after the correspondence, intersection
numbers and primitive projection have been independently constructed.

Paper 0 does not validate the finite-support mechanism over
\(\mathrm{Spec}\,\mathbb Z\).  The function-field proof takes place
on the complete proper surface \(E\times E\); no truncation by closed-point
degree is introduced.

## 2. Fixed control curve

Use

\[
 E/\mathbb F_5:\qquad y^2=x^3+x+1.
 \tag{1}
\]

The discriminant is nonzero modulo \(5\), so \(E\) is an elliptic curve.
Direct counting gives

\[
 \#E(\mathbb F_5)=9,
 \qquad
 a_1=5+1-\#E(\mathbb F_5)=-3.
 \tag{2}
\]

Let \(\alpha,\beta\) be the formal roots of

\[
 P_E(T)=T^2+3T+5.
 \tag{3}
\]

Define

\[
 a_n=\alpha^n+\beta^n,
 \qquad
 N_n=\#E(\mathbb F_{5^n})=5^n+1-a_n.
 \tag{4}
\]

The recurrence used for exact preflight calculations is

\[
 a_0=2,qquad a_1=-3,qquad
 a_n=-3a_{n-1}-5a_{n-2}.
 \tag{5}
\]

The first values are

\[
 (a_1,N_1)=(-3,9),\qquad
 (a_2,N_2)=(-1,27),\qquad
 (a_3,N_3)=(18,108).
 \tag{6}
\]

These values are anchors, not inputs from the desired inequality.

## 3. Geometric correspondence package

Fix a rational base point \(O\in E(\mathbb F_5)\).  In
\(S=E\times E\), define

\[
 F_{\mathrm v}=\{O\}\times E,
 \qquad
 F_{\mathrm h}=E\times\{O\},
 \qquad
 \Delta=\{(P,P):P\in E\}.
 \tag{7}
\]

For the geometric Frobenius \(F\), let

\[
 \Gamma_n=\Gamma_{F^n}
 =\{(P,F^nP):P\in E\}.
 \tag{8}
\]

Paper 0 must prove from graphs and fiber products that

\[
 \Gamma_m\circ\Gamma_n=\Gamma_{m+n},
 \tag{9}
\]

that transpose exchanges Frobenius with the corresponding Verschiebung
correspondence, and that

\[
 \Gamma_n\cdot F_{\mathrm v}=1,
 \qquad
 \Gamma_n\cdot F_{\mathrm h}=5^n.
 \tag{10}
\]

No zeta function is used to define these operations.

## 4. Lefschetz fixed-point calculation

The diagonal intersection must be derived scheme-theoretically:

\[
 \Gamma_n\cdot\Delta
 =\deg\mathrm{Fix}(F^n)
 =N_n.
 \tag{11}
\]

For \(m>n\), the cross-check

\[
 \Gamma_m\cdot\Gamma_n
 =5^nN_{m-n}
 \tag{12}
\]

must follow from factoring the inseparable part of
\(F^m-F^n\).  Equation (12) is a consistency test for composition and
intersection multiplicity; it is not needed to insert the point counts.

## 5. Connected Euler extraction

Let \(B_d\) be the number of closed points of degree \(d\).  The fixed
point counts and primitive orbit counts satisfy

\[
 N_n=\sum_{d\mid n}dB_d,
 \qquad
 B_n=\frac1n\left(N_n-
 \sum_{\substack{d\mid n\\d<n}}dB_d\right).
 \tag{13}
\]

The connected/cycle operation used in the arithmetic source package must
derive

\[
 Z_E(u)
 =\exp\left(\sum_{n\ge1}\frac{N_n}{n}u^n\right)
 =\prod_{d\ge1}(1-u^d)^{-B_d}.
 \tag{14}
\]

For the fixed curve,

\[
 B_1=9,qquad B_2=9,qquad B_3=33.
 \tag{15}
\]

The same connected extraction must distinguish primitive closed points
from their iterates.  It may not be fitted to (14) after the fact.

## 6. Critical balancing

A primitive orbit of degree \(d\), iterated \(k\) times, has logarithmic
length \(kd\log5\).  The source half-density normalization must give

\[
 5^{-kd/2}
 \tag{16}
\]

from the balanced bidegree of the correspondence, rather than by
inserting the critical exponent manually.  Paper 0 must state the exact
normalization functor that produces (16) and show that it is the same
operation proposed for \(p^{-k/2}\) over \(\mathbb Z\).

## 7. Primitive projection and Hodge sign

The elementary intersections are

\[
 F_{\mathrm v}^2=F_{\mathrm h}^2=0,
 \qquad F_{\mathrm v}\cdot F_{\mathrm h}=1,
 \qquad \Delta^2=\Gamma_n^2=0.
 \tag{17}
\]

Define the primitive classes

\[
 \Delta^0=\Delta-F_{\mathrm v}-F_{\mathrm h},
 \qquad
 \Gamma_n^0=\Gamma_n-5^nF_{\mathrm v}-F_{\mathrm h}.
 \tag{18}
\]

Direct expansion, before invoking Hodge, must give

\[
 (\Delta^0)^2=-2,
 \qquad
 (\Gamma_n^0)^2=-2\cdot5^n,
 \qquad
 \Gamma_n^0\cdot\Delta^0=-a_n.
 \tag{19}
\]

The primitive Gram matrix is therefore

\[
 G_n^0=
 \begin{pmatrix}
 -2&-a_n\\
 -a_n&-2\cdot5^n
 \end{pmatrix}.
 \tag{20}
\]

Only now may the Hodge-index theorem be applied.  Negative
semidefiniteness gives

\[
 \det G_n^0=4\cdot5^n-a_n^2\ge0,
 \qquad
 |a_n|\le2\cdot5^{n/2}.
 \tag{21}
\]

This is the required recovery of the Weil estimate from the source
geometry.

### Genus-sensitivity gate

The fixed elliptic control certifies the case \(g=1\) only.  It does
**not** by itself prove that the same source route tracks the genus
factor in the primitive diagonal entries.

For a smooth proper curve \(C/\mathbf F_q\) of genus \(g\), the expected
primitive package is

\[
 (\Delta^0)^2=-2g,
 \qquad
 (\Gamma_n^0)^2=-2g\,q^n,
 \qquad
 \Gamma_n^0\cdot\Delta^0=-a_n,
 \tag{21a}
\]

with

\[
 \det G_n^0 = 4g^2q^n-a_n^2.
 \tag{21b}
\]

Therefore a valid Paper 0 source route must be genus-sensitive at the
two diagonal entries.  The elliptic values
\(-2,-2q^n\) may not be treated as if they automatically transported to
general genus.

Auxiliary exact audit:

1. `107_28_PAPER_0_GENUS_2_DIAGONAL_SENSITIVITY_AUDIT.md`
2. `107_28_genus2_diagonal_sensitivity.py`

These do not replace the fixed positive control, but they do separate
the genus-portability question from the elliptic proof.

## 8. Equality and radical calibration

Paper 0 must record the equality condition in (21).  It must identify
which primitive numerical classes become isotropic and compare that
mechanism with the proposed equality-case audit over \(\mathbb Z\).
This comparison is structural only: it does not certify the explicit
Weil radical required in 107.00.

## 9. Anti-retrofit rules

The calibration fails if any of the following occurs:

1. \(N_n\) is installed as the definition of \(\Gamma_n\cdot\Delta\).
2. The Euler product is assumed instead of derived from (13).
3. The factor \(5^{-kd/2}\) is inserted independently of bidegree.
4. The primitive correction is chosen after inspecting \(a_n\).
5. The Hodge sign is used to define an earlier operation.
6. A truncation by closed-point degree is presented as a proper surface.

## 10. Completion criterion

Paper 0 passes only when Sections 3--7 are proved by operations that have
a literal proposed counterpart in the arithmetic source package.  Passing
the exact arithmetic preflight script is necessary but not sufficient.
The output is a calibrated interface, not a new proof of the
function-field theorem and not evidence that the arithmetic surface over
\(\mathbb Z\) already exists.
