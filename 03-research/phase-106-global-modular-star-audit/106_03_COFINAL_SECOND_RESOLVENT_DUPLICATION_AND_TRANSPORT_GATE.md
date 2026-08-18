# 106.03 — Cofinal second-resolvent duplication and transport gate

## Result

The second-resolvent proposal is not a new spectral route.  At the finite
level it is exactly the curvature defect already isolated in Phase 101.
More precisely, if \(D_{L,N}\) denotes the finite source-built self-adjoint
quotient operator of E101.093 and

\[
\Theta_{L,N}=\frac12+iD_{L,N},
\tag{1}
\]

then

\[
\Theta_{L,N}^{*}=1-\Theta_{L,N}
\tag{2}
\]

and the Phase-101 defect satisfies

\[
\boxed{
K_{L,N}(s)
=
-\left(\frac{\xi'}{\xi}\right)'(s)
-\mathrm{Tr}(s-\Theta_{L,N})^{-2}.
}
\tag{3}
\]

Consequently, the Phase-106 trace target is literally

\[
K_{L,N}\longrightarrow0,
\tag{4}
\]

which is Route C of E101.095, Section 14.  It must not be advertised as an
untried replacement for that route.

There was nevertheless one genuinely unexecuted operation: construct
connecting maps between the finite positive quotients.  This document carries
out that operation and proves a sharp dichotomy.

1. Positive Gram transport can always be made cofinal, but then the limit
   generator is unitarily equivalent to the free generator and loses all
   Euler--Gamma spectral information.
2. The actual shifted-Weil quotients admit canonical Hilbert-space connecting
   maps, but their arithmetic generators have an explicit intertwining defect
   \(\mathcal R_N\).  Exact intertwining would force nesting of the finite
   spectra.  Approximate intertwining is governed by an exact resolvent
   identity and returns to (4).

Thus canonical Hilbert connectivity is now closed.  The force-bearing
arithmetic operator compatibility is not.

## 1. Exact crosswalk with Phase 101

Assume the finite even-simple hypothesis of E101.093, so that \(D_{L,N}\) is
self-adjoint on the positive radical quotient.  Equation (2) follows at once
from (1):

\[
\Theta_{L,N}^{*}
=\frac12-iD_{L,N}
=1-\Theta_{L,N}.
\tag{5}
\]

Let

\[
\alpha=\frac12+i\theta,
\qquad \theta\in\mathrm{Spec}\,D_{L,N},
\tag{6}
\]

with algebraic multiplicity \(m_\alpha\).  Functional calculus gives

\[
\mathrm{Tr}(s-\Theta_{L,N})^{-2}
=\sum_\alpha\frac{m_\alpha}{(s-\alpha)^2}.
\tag{7}
\]

For the finite characteristic \(\mathcal F_{L,N}\), affine regularization
terms disappear after two derivatives, and hence

\[
(\log\mathcal F_{L,N})''(s)
=-\mathrm{Tr}(s-\Theta_{L,N})^{-2}.
\tag{8}
\]

E101.095(5.3)--(5.5) defines

\[
K_{L,N}(s)
:=\left(\log\frac{\mathcal F_{L,N}(s)}{\xi(s)}\right)''
=\sum_\rho\frac{m_\rho}{(s-\rho)^2}
 -\sum_\alpha\frac{m_\alpha}{(s-\alpha)^2}.
\tag{9}
\]

Since

\[
-\left(\frac{\xi'}{\xi}\right)'(s)
=\sum_\rho\frac{m_\rho}{(s-\rho)^2},
\tag{10}
\]

equations (7)--(10) prove (3).  This is an identity, not an analogy.

The notation here must not be confused with the generally nonnormal secular
matrix called \(K_{L,N}\) in Phase 81.  The positive-star operator is
\(D_{L,N}^{\mathrm{phys}}\) on the E101.093 radical quotient; \(K_{L,N}(s)\)
in (9) is a scalar curvature defect.

## 2. A compactness gate already implies RH

The topology in (4) cannot be weakened to an unspecified pointwise limit.
The natural trace-compactness hypothesis already carries the entire divisor.

### Theorem 1 — Second-resolvent compactness criterion

Let \(\Theta_j\) be finite-dimensional operators satisfying

\[
\Theta_j^*=1-\Theta_j.
\tag{11}
\]

Assume that, for one real \(s_0>1\),

\[
\sup_j\left\|(s_0-\Theta_j)^{-2}\right\|_{\mathcal S_1}<\infty,
\tag{12}
\]

and that locally uniformly on \(\Re s>1\),

\[
\mathrm{Tr}(s-\Theta_j)^{-2}
\longrightarrow
-\left(\frac{\xi'}{\xi}\right)'(s).
\tag{13}
\]

Then RH holds.  Conversely, under RH a family satisfying (11)--(13) is
obtained by truncating the zero spectrum.

### Proof

Put

\[
A_j=-i(\Theta_j-\tfrac12).
\tag{14}
\]

Equation (11) makes \(A_j\) self-adjoint.  Let \(\mu_j\) be its eigenvalue
counting measure.  For \(s=\frac12+iz\),

\[
\mathrm{Tr}(s-\Theta_j)^{-2}
=-\int_{\mathbb R}\frac{d\mu_j(t)}{(t-z)^2}.
\tag{15}
\]

Writing \(a=s_0-\frac12>0\), condition (12) is

\[
\sup_j\int_{\mathbb R}\frac{d\mu_j(t)}{a^2+t^2}<\infty.
\tag{16}
\]

The weighted positive measures

\[
d\nu_j(t)=\frac{d\mu_j(t)}{a^2+t^2}
\tag{17}
\]

therefore have uniformly bounded mass.  A weak-star subsequence on the
compactified real line yields an analytic limit of (15) throughout
\(\Im z<0\), because

\[
-\frac{a^2+t^2}{(t-z)^2}
\tag{18}
\]

and all its (z)-derivatives are locally uniformly bounded and have finite
limits as \(t\to\pm\infty\).

The half-plane \(\Re s>1\) corresponds to \(\Im z<-1/2\).  By (13), the
analytic limit there is

\[
\((\log\Xi)''(z)\),
\qquad
\Xi(z)=\xi(\tfrac12+iz).
\tag{19}
\]

Uniqueness of analytic continuation extends (19) through the lower
half-plane.  A zero \(z_\rho\) of multiplicity \(m\) in that half-plane would
give the nonremovable principal part

\[
-\frac{m}{(z-z_\rho)^2}
\tag{20}
\]

in (19), contradicting analyticity of the limit.  Hence \(\Xi\) has no zero
in the lower half-plane.  Its real symmetry excludes upper-half-plane zeros,
so all its zeros are real.

Conversely, under RH take \(A_j\) diagonal on the first \(j\) real zeros of
\(\Xi\), with multiplicity, and put \(\Theta_j=\frac12+iA_j\).  The
Riemann--von Mangoldt estimate gives (12) and locally uniform convergence in
(13).  \(\square\)

Theorem 1 shows that the proposed finite-star limit plus its natural
\(\mathcal S_1\) compactness is equivalent to RH.  Compact resolvent is
stronger than the single weighted bound (12).

## 3. Universal positive Gram transport is spectrally free

The next construction answers whether positivity and canonical connecting
maps alone can create the missing global object.

Let

\[
V_N\subset V_{N+1}
\tag{21}
\]

be finite-dimensional source spaces with standard isometric inclusions
\(I_N\), and let \(W_N=W_N^*\) be arbitrary source Hermitian matrices.  Define

\[
G_N=(1+\|W_N\|)I+W_N>0,
\qquad
\langle x,y\rangle_N=\langle G_Nx,y\rangle.
\tag{22}
\]

### Theorem 2 — Canonical Gram transport

The maps

\[
J_N=G_{N+1}^{-1/2}I_NG_N^{1/2}
\tag{23}
\]

are isometries.  If a free self-adjoint generator \(D_N^0\) satisfies

\[
D_{N+1}^0I_N=I_ND_N^0,
\tag{24}
\]

then

\[
A_N=G_N^{-1/2}D_N^0G_N^{1/2}
\tag{25}
\]

is self-adjoint for (22), and

\[
A_{N+1}J_N=J_NA_N.
\tag{26}
\]

The inductive-limit operator is nevertheless unitarily equivalent to the
free generator \(D^0\).

### Proof

Direct multiplication gives

\[
J_N^*G_{N+1}J_N=G_N,
\tag{27}
\]

which proves isometry.  The \(G_N\)-adjoint of (25) is

\[
G_N^{-1}A_N^*G_N=A_N,
\tag{28}
\]

and (24) gives (26).  Finally,

\[
U_N=G_N^{1/2}:H_N\longrightarrow V_N
\tag{29}
\]

is unitary and obeys

\[
U_{N+1}J_N=I_NU_N,
\qquad
U_NA_NU_N^{-1}=D_N^0.
\tag{30}
\]

Thus the complete inductive system is unitarily the free system.  \(\square\)

For the bilateral Fourier generator

\[
D^0e_n=\frac{2\pi n}{L}e_n,
\qquad
\Theta=\frac12+iA,
\tag{31}
\]

one obtains the desired adjoint relation, but the trace is

\[
\mathrm{Tr}(s-\Theta)^{-2}
=\frac{L^2}{4}
\mathrm{csch}^2\!\left(\frac L2(s-\tfrac12)\right),
\tag{32}
\]

not (10).  Moreover \(L\to\infty\) sends the first nonzero frequency
\(2\pi/L\) to zero and destroys compact resolvent in the naive limit.

Theorem 2 is the precise reason that inserting the Euler--Gamma matrix only
through a positive metric cannot solve the problem: the metric changes
coordinates but not spectral content.

## 4. Exact compatibility of the shifted-Weil quotients

There remains the actual E101.093 construction, where the operator is not a
metric conjugate of a fixed free generator.

Fix \(L\), let \(V_N\subset V_{N+1}\) be the nested Fourier spaces, and assume

\[
W_N=I_N^*W_{N+1}I_N.
\tag{33}
\]

Put

\[
\varepsilon_N=\min\mathrm{Spec}\,W_N,
\qquad
T_N=W_N-\varepsilon_NI,
\qquad
\Delta_N=\varepsilon_N-\varepsilon_{N+1}\ge0.
\tag{34}
\]

The min--max principle gives the last inequality.

### Theorem 3 — Natural quotient-inclusion obstruction

For every \(x,y\in V_N\),

\[
\boxed{
\langle T_{N+1}I_Nx,I_Ny\rangle
=\langle T_Nx,y\rangle
 +\Delta_N\langle x,y\rangle.
}
\tag{35}
\]

Assume the two ground spaces are simple.  The natural inclusion induces an
isometric map

\[
V_N/\ker T_N\longrightarrow V_{N+1}/\ker T_{N+1}
\tag{36}
\]

if and only if \(\Delta_N=0\).

### Proof

Equation (35) follows by substituting (33)--(34).  If
\(\Delta_N>0\) and \(\xi_N\in\ker T_N\setminus\{0\}\), then

\[
\|I_N\xi_N\|_{T_{N+1}}^2
=\Delta_N\|\xi_N\|^2>0.
\tag{37}
\]

Thus the zero class would be sent to a nonzero class, so (36) is not even
well-defined.  If \(\Delta_N=0\), equality in Rayleigh--Ritz sends the old
ground line into the new one, and (35) proves that the induced map is an
isometry.  \(\square\)

The obstruction is not the end of Hilbert connectivity.  It can be corrected
without reading spectral zeros of \(\xi\).

Let

\[
K_N=(\ker T_N)^\perp,
\qquad
S_N=T_N|_{K_N},
\tag{38}
\]

and define

\[
C_N=P_{K_{N+1}}I_N|_{K_N},
\qquad
B_N=(S_N+\Delta_NI)^{-1/2}S_N^{1/2},
\qquad
j_N=C_NB_N.
\tag{39}
\]

### Theorem 4 — Corrected canonical Hilbert connection

The map \(j_N\) is injective and satisfies

\[
\langle T_{N+1}j_Nx,j_Ny\rangle
=\langle T_Nx,y\rangle
\qquad(x,y\in K_N).
\tag{40}
\]

### Proof

Projection from \(I_Nx\) to \(C_Nx\) changes it only by a vector in
\(\ker T_{N+1}\), so (35) gives

\[
\langle T_{N+1}C_Nx,C_Ny\rangle
=\langle(S_N+\Delta_NI)x,y\rangle.
\tag{41}
\]

The right side is positive for nonzero \(x\), proving injectivity of \(C_N\).
Because \(B_N\) is a commuting functional-calculus expression in \(S_N\),
substitution of (39) into (41) gives (40).  \(\square\)

This closes the previously missing construction of positive connecting maps.

## 5. The surviving arithmetic operator defect

Realize each quotient operator \(D_N\) on \(K_N\), and put

\[
\mathcal R_N=D_{N+1}j_N-j_ND_N.
\tag{42}
\]

If \(\mathcal R_N=0\), the range of \(j_N\) is invariant under the
self-adjoint \(D_{N+1}\), hence reducing.  Therefore every eigenvalue of
\(D_N\), with multiplicity, must occur in \(D_{N+1}\).  In finite dimension,
this is equivalent to

\[
\chi_{D_N}\mid\chi_{D_{N+1}}.
\tag{43}
\]

Conversely, spectral containment with multiplicity permits an isometric
intertwiner after choosing compatible eigenbases, although it does not by
itself make that choice source-canonical.

The moving finite characteristics of Phase 101 were not constructed as a
nested divisor.  Hence exact intertwining is not supplied by their finite
self-adjointness.

For approximate compatibility one has the exact identity

\[
\boxed{
(D_{N+1}-z)^{-1}j_N-j_N(D_N-z)^{-1}
=-(D_{N+1}-z)^{-1}\mathcal R_N(D_N-z)^{-1}.
}
\tag{44}
\]

It follows by multiplying (42) on the left and right by the two resolvents.
Equation (44) identifies the only genuinely new quantitative target created
by the cofinal construction: a source estimate on \(\mathcal R_N\) strong
enough to yield trace-norm convergence of second resolvents.  Taking traces
then returns exactly to \(K_{L,N}\to0\) through (3).

## 6. Binding decision

The proposed work has the following audited classification.

```text
finite positive star and centered adjoint       already Phase 101;
second-resolvent curvature identity             already E101.095;
cofinal determinant/divisor identification      already the open Route C;
canonical positive connecting maps              proved here;
canonical free-generator transport              refuted as spectrally trivial;
arithmetic generator compatibility              open as the defect R_N;
trace-class cofinal convergence                  equivalent to the old K-defect;
global compact-resolvent H1 with Xi divisor      not constructed.
```

Therefore Phase 106 must not launch another copy of the Phase-101 curvature
route.  Any successor on this front must estimate the explicit operator
defect (42) from the complete coupled Euler--Gamma matrix and must pass the
off-line planted-system falsifier.  Merely constructing a positive metric,
an inductive Hilbert space or a formal determinant does not address (42).

## Status

Proved: the exact Phase-101/Phase-106 crosswalk, Theorems 1--4, the free
transport no-go, the natural quotient-inclusion obstruction, the corrected
positive connecting maps, and the resolvent-defect identity.

Open: a source estimate on \(\mathcal R_N\) implying the trace-class limit,
equivalently the force-bearing \(K_{L,N}\to0\) identification.  No RH
conclusion is claimed.
