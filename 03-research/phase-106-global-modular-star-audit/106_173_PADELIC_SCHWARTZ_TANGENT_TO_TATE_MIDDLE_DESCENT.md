# 106.173 — (p)-adic Schwartz tangent descent to the Tate middle complex

## 1. Purpose

Documents 106.169--106.172 construct the polarized Tate middle spaces,
their odd orientation, and the scalar primitive--Gamma boundary
normalization.  One comparison map was still only denoted by
\(\mathrm{Loc}_{\rm Tate}\): the passage from the actual local
Schwartz functions in the adelic source to the two harmonic coordinates
of each complex Tate fibre.

This note constructs that map on the finite-support tangent of the
restricted adelic product.  The construction uses only local additive
Fourier transform, the distinguished spherical vector
\(1_{\mathbb Z_p}\), and averaging on \(\mathbb Z_p^\times\).  It is
surjective, complex-linear, and admits an explicit complex-linear right
inverse.  After applying the middle projector of 106.169, it is a split
surjection onto every finite-prime Tate middle space.

This closes the finite-place coefficient descent.  It does not identify
the resulting local kernel with the complete CCM cyclic restriction
kernel; that is a derived global assertion.

## 2. The spherical tangent at one prime

Fix a prime \(p\).  Normalize additive Haar measure on \(\mathbb Q_p\)
by \(\mathrm{vol}(\mathbb Z_p)=1\), and choose the standard
self-dual additive character.  Let

\[
 \mathscr S_p=\mathcal S(\mathbb Q_p)^{\mathbb Z_p^\times}
\]

be the real radial Bruhat--Schwartz space.  Its distinguished spherical
vector is

\[
 \phi_p^0=1_{\mathbb Z_p},
 \qquad \mathcal F_p\phi_p^0=\phi_p^0.                       \tag{1}
\]

The tangent to the restricted product at \(\phi_p^0\) is

\[
 \mathscr T_p=\mathscr S_p/\mathbb R\phi_p^0.                \tag{2}
\]

Since \(\mathcal F_p\phi_p^0=\phi_p^0\), Fourier transform descends to
an involution of \(\mathscr T_p\).  Radial functions are even, so

\[
 \mathcal F_p^2=I\quad\hbox{on }\mathscr T_p.                \tag{3}
\]

Normalize multiplicative Haar measure on \(\mathbb Z_p^\times\) to
have mass one.  Define

\[
 \ell_p^\circ(f)
 =\int_{\mathbb Z_p^\times}f(u)\,d^\times u-f(0).            \tag{4}
\]

Because \(\ell_p^\circ(\phi_p^0)=1-1=0\), (4) is a well-defined
continuous functional on \(\mathscr T_p\).

Let

\[
 \chi_p=1_{\mathbb Z_p^\times}.                              \tag{5}
\]

Then \(\ell_p^\circ(\chi_p)=1\), so \(\ell_p^\circ\) is onto.

## 3. Fourier double and the Tate Hodge plane

Let \(\mathscr K_{\rm alg}\) be the algebraic common coefficient core
of the Cauchy-dilation module of 106.154.  Set

\[
 \mathscr D_p=(\mathscr T_p\oplus\mathscr T_p)
                    \otimes\mathscr K_{\rm alg}.             \tag{6}
\]

The local Fourier complex structure is

\[
 J_p^{\rm src}(f,g)=(-\mathcal F_pg,\mathcal F_pf).           \tag{7}
\]

Let \(V_p=(\mathbb Ra_p\oplus\mathbb Rb_p)otimes
\mathscr K_{\rm alg}\) be the harmonic Tate plane of 106.169, and put

\[
 c_p={2\pi\over\log p},
 \qquad
 J_p^{\rm Tate}(x,y)=(-c_p^{-1}y,c_px).                      \tag{8}
\]

Define the local coefficient map

\[
 \boxed{
 L_p(f,g)=
 \left(\ell_p^\circ(f),\;c_p\ell_p^\circ(\mathcal F_pg)\right).}
                                                                    \tag{9}
\]

The functionals act on the Schwartz factor and leave
\(\mathscr K_{\rm alg}\) unchanged.

### Theorem 3.1 — Exact local Hodge descent

The map \(L_p:\mathscr D_p\to V_p\) is continuous and surjective, and

\[
 \boxed{L_pJ_p^{\rm src}=J_p^{\rm Tate}L_p.}                 \tag{10}
\]

It has the explicit complex-linear right inverse

\[
 \boxed{
 s_p(x,y)=left(\chi_p\otimes x,
       \mathcal F_p\chi_p\otimes c_p^{-1}y\right),}
                                                                    \tag{11}
\]

where tensor notation is suppressed in (9).

#### Proof

Write \(L_p(f,g)=(x,y)\).  Equations (3), (7), and (9) give

\[
 \begin{aligned}
 L_pJ_p^{\rm src}(f,g)
 &=L_p(-\mathcal F_pg,\mathcal F_pf)\\
 &=\left(-\ell_p^\circ(\mathcal F_pg),
          c_p\ell_p^\circ(f)\right)\\
 &=(-c_p^{-1}y,c_px)
 =J_p^{\rm Tate}L_p(f,g).
 \end{aligned}                                               \tag{12}
\]

Using \(\ell_p^\circ(\chi_p)=1\) and \(\mathcal F_p^2=I\),

\[
 L_ps_p(x,y)=(x,y),                                          \tag{13}
\]

so \(L_p\) is onto.  Finally,

\[
 \begin{aligned}
 J_p^{\rm src}s_p(x,y)
 &=\left(-\chi_p\otimes c_p^{-1}y,
          \mathcal F_p\chi_p\otimes x\right)\\
 &=s_p(-c_p^{-1}y,c_px)
 =s_pJ_p^{\rm Tate}(x,y),
 \end{aligned}                                               \tag{14}
\]

which proves complex linearity of the section. \(\square\)

The factors \(c_p\) in (9) and (11) are forced: without them the local
Fourier double would descend to the standard quarter turn rather than to
the actual Hodge star of the Tate curve of modulus \(p^{-1}\).

## 4. The finite-support adelic tangent

The tangent at the spherical vector of a restricted tensor product is the
algebraic direct sum of its local tangents.  Define

\[
 \mathscr D_{\rm fin}=\bigoplus_p\mathscr D_p,
 \qquad
 \mathscr V_{\rm fin}=\bigoplus_pV_p,                         \tag{15}
\]

and

\[
 L_{\rm fin}=\bigoplus_pL_p,
 \qquad s_{\rm fin}=\bigoplus_ps_p.                          \tag{16}
\]

All sums in (15)--(16) are finite on every vector.  Hence there is no
summability or completion issue.

### Corollary 4.1 — Split global coefficient localization

On the LF finite-support cores,

\[
 \boxed{
 L_{\rm fin}s_{\rm fin}=I,
 \qquad
 L_{\rm fin}J^{\rm src}=J^{\rm Tate}L_{\rm fin},
 \qquad
 s_{\rm fin}J^{\rm Tate}=J^{\rm src}s_{\rm fin}.}            \tag{17}
\]

Thus the complete collection of ordinary-prime Tate Hodge planes is a
complex-linear retract of the actual radial Bruhat--Schwartz tangent of
the finite adeles.

#### Proof

Apply Theorem 3.1 prime by prime.  Algebraic direct sums preserve split
surjections and the three identities. \(\square\)

## 5. Descent to the middle relative space

For a finite prime set \(S\), let \(P_S^{\rm mid}\) be the orthogonal
projector of 106.169 onto

\[
 IH_S^1=\ker R_S\cap\ker(R_SJ_S).                            \tag{18}
\]

It commutes with \(J_S^{\rm Tate}\).  Put

\[
 \mathrm{Loc}_S^{\rm mid}
 =P_S^{\rm mid}L_S:\bigoplus_{p\in S}\mathscr D_p
                 \longrightarrow IH_S^1.                    \tag{19}
\]

### Theorem 5.1 — Finite middle localization is split

For every finite \(S\), (19) is a continuous complex-linear
surjection.  Its right inverse is the restriction

\[
 \boxed{
 \sigma_S=s_S|_{IH_S^1},
 \qquad
 \mathrm{Loc}_S^{\rm mid}\sigma_S=I.}                \tag{20}
\]

#### Proof

If \(v\in IH_S^1\), then \(P_S^{\rm mid}v=v\).  Equations (13) and
(19) therefore give

\[
 \mathrm{Loc}_S^{\rm mid}s_Sv
 =P_S^{\rm mid}L_Ss_Sv=P_S^{\rm mid}v=v.                    \tag{21}
\]

Every map in (19)--(20) commutes with the relevant complex structure by
(17) and the commutation of \(P_S^{\rm mid}\) with \(J_S^{\rm Tate}\).
\(\square\)

Pulling the positive Tate metric back along \(\sigma_S\) gives the exact
source coefficient metric

\[
 \|\sigma_Sv\|_{\rm coeff}^2:=\|v\|_{\rm Tate}^2>0
 \qquad(v\ne0).                                              \tag{22}
\]

This is a quotient metric on the explicit coefficient retract, not a
claim that the ambient Bruhat--Schwartz \(L^2\) metric equals the Hodge
metric.

## 6. Compatibility under adjoining primes

The raw maps \(L_{\rm fin}\) and \(s_{\rm fin}\) are strictly compatible
with extension by zero.  Although the formula for the ambient middle
projector changes when a prime is added, a vector already satisfying the
two balance equations remains balanced after extension by zero.

Let \(S\subset S'\).  Extend \(v\in IH_S^1\) by zero and apply
\(P_{S'}^{\rm mid}\).  Then

\[
 \iota_{S,S'}^{\rm mid}v:=P_{S'}^{\rm mid}(v,0)              \tag{23}
\]

equals \((v,0)\), is complex-linear, and (19) gives the commutative
identity

\[
 \mathrm{Loc}_{S'}^{\rm mid}
 \bigl(s_{S'}\iota_{S,S'}^{\rm mid}v\bigr)
 =\iota_{S,S'}^{\rm mid}v.                                  \tag{24}
\]

Consequently the finite middle localizations define a split cofinal
system on the algebraic source core.  The nonclosability theorem of
106.169 still applies to its Hilbert completion; (24) is an LF/nuclear
statement.

## 7. Relation to the CCM restriction morphism

The construction above is not an arbitrary local model.  The source
spaces \(\mathscr S_p\) are the radial factors of the same
Bruhat--Schwartz restricted product used in the CCM groupoid algebra, and
\(\phi_p^0=1_{\mathbb Z_p}\) is its distinguished unramified vector.
Thus (15) is the literal first-order finite-place tangent of that adelic
source.  Equations (9)--(10) show that additive Fourier duality descends
to the actual Tate Hodge star rather than to a formally chosen copy.

What has not yet been proved is the following derived kernel identity:

\[
 \ker H^1(\mathrm{Loc}^{\rm mid})
 =\overline{\mathrm{Ran}\,\rho^\natural}                \tag{25}
\]

inside the CCM nuclear cyclic target.  Theorem 5.1 proves local
surjectivity onto the finite middle coefficients.  Equation (25) is the
remaining global faithfulness statement and cannot be inferred from
surjectivity.

## 8. Falsification controls

1. The map uses the Euler restricted product through the individual
   spherical vectors \(1_{\mathbb Z_p}\).  A Dirichlet series without an
   Euler product has no collection of local tangent factors on which
   (15) can be formed.
2. No zero of \(\zeta\) is used in (1)--(24).
3. No Paley--Wiener sampling estimate is used.  Surjectivity follows from
   the explicit shell function \(1_{\mathbb Z_p^\times}\).
4. No Hilbert closure is taken.  The construction therefore does not
   erase the nonclosed relative information before comparison with CCM.

## 9. Status

Proved without RH or spectral input:

* an explicit local map from radial \(p\)-adic Schwartz tangents to the
  two Tate harmonic coordinates;
* exact compatibility with local Fourier transform and the Tate Hodge
  star;
* an explicit complex-linear right inverse at every prime;
* split surjectivity on the finite adelic tangent;
* split surjectivity onto every finite-prime middle relative space;
* cofinal compatibility in the LF category.

Still required:

* extension through the complete CCM cyclic restriction morphism;
* proof of the derived kernel identity (25);
* assembly with the full Gamma/polar differential and proof of the
  Rosati metric identity.
