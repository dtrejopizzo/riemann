# 106.153 — A polarized degree-one coefficient module on the prime orbits

## 1. Purpose and scope

Document 106.152 realizes the literal factor \(p^{-k/2}\) as the
\(k\)-th Fourier moment of the Poisson measure and then as a relative heat
trace on a circle of length \(\log p\).  It also proves that deleting the
zero-winding sector is incompatible with heat-kernel composition.

The present document changes parity instead of repairing that deletion.  It
constructs, for every ordinary prime \(p\), a measurable family of
weight-one, polarized, real rank-two local systems over the periodic orbit

\[
 C_p\simeq \mathbb R/(\log p)\mathbb Z
\]

of the Connes--Consani arithmetic Jacobian.  The family is parametrized by
the character variety
\(\mathrm{Hom}(\pi_1(C_p),U(1))\simeq\mathbb T\), and its holonomy is
averaged with the same Poisson measure as in 106.152.  The resulting finite
von Neumann module has a positive polarization before any zero of \(\zeta\)
is used, and its normalized trace gives exactly

\[
 \frac{\log p}{p^{k/2}}.
\]

Putting this coefficient module formally in cohomological degree one
supplies the minus sign of the prime channel by graded trace.  This grading
does **not** by itself construct a cochain complex or an actual \(H^1\); those
belong to the global descent problem below.  No zero-winding projection is
made, and no heat semigroup with prescribed trace is postulated.

This is a local construction, not a proof of RH.  The remaining construction
is a global descent problem: glue these polarized coefficient systems over
all finite periodic orbits to the generic and archimedean fibers of the
Riemann sector, and prove a Lefschetz formula on the resulting global
cohomology.  That gluing is not performed here.

## 2. The polarized real plane

Let \(V=\mathbb R^2\), and put

\[
 \mathbf E=
 \begin{pmatrix}0&1\\-1&0\end{pmatrix},
 \qquad
 \mathbf J=
 \begin{pmatrix}0&-1\\1&0\end{pmatrix}=-\mathbf E.
\]

Define

\[
 \Omega(u,v)=u^{\mathsf T}\mathbf E v,
 \qquad
 g(u,v)=\Omega(u,\mathbf Jv).
\]

Then \(\Omega\) is alternating, \(\mathbf J^2=-I\), and

\[
 g(u,v)=u^{\mathsf T}v.
\]

Thus \((V,\Omega,\mathbf J,g)\) is a polarized real Hodge structure of
weight one at the linear-algebra level.

For \(\theta\in\mathbb T\), let

\[
 R_\theta=
 \begin{pmatrix}
 \cos\theta&-\sin\theta\\
 \sin\theta& \cos\theta
 \end{pmatrix}.
\]

The rotation \(R_\theta\) commutes with \(\mathbf J\), preserves \(\Omega\),
and is unitary for \(g\).

## 3. Weight-one prime monodromy

For an ordinary prime \(p\), define

\[
 F_{p,\theta}=p^{1/2}R_\theta,
 \qquad
 U_{p,\theta}=p^{-1/2}F_{p,\theta}=R_\theta.       \tag{1}
\]

### Theorem 3.1 — Exact local weight-one polarization

For every \(u,v\in V\),

\[
 \boxed{
 \begin{aligned}
 \Omega(F_{p,\theta}u,F_{p,\theta}v)&=p\,\Omega(u,v),\\
 F_{p,\theta}\mathbf J&=\mathbf JF_{p,\theta},\\
 g(F_{p,\theta}u,F_{p,\theta}v)&=p\,g(u,v).
 \end{aligned}}                                                   \tag{2}
\]

Consequently \(U_{p,\theta}\) is symplectic and unitary.

#### Proof

Since \(R_\theta^{\mathsf T}\mathbf E R_\theta=\mathbf E\),

\[
 F_{p,\theta}^{\mathsf T}\mathbf E F_{p,\theta}
 =pR_\theta^{\mathsf T}\mathbf E R_\theta=p\mathbf E.
\]

Rotations commute in dimension two, hence
\(R_\theta\mathbf J=\mathbf JR_\theta\).  The last identity follows either
directly from \(F_{p,\theta}^{\mathsf T}F_{p,\theta}=pI\) or from the first
two identities and \(g=\Omega(\cdot,\mathbf J\cdot)\).  Dividing
\(F_{p,\theta}\) by \(p^{1/2}\) proves the final assertion. \(\square\)

Equation (2) is the continuous-weight analogue of the similitude relation
for a polarized Frobenius.  It has been obtained here from \(p\) and a
unitary angle only; no zeta zero occurs in the definition.

## 4. The finite prime coefficient module

Set

\[
 r_p=p^{-1/2},
 \qquad
 d\mu_{r_p}(\theta)
 =\frac{1-r_p^2}{1-2r_p\cos\theta+r_p^2}\frac{d\theta}{2\pi}.
\]

Let

\[
 \mathcal M_p
 =L^\infty(\mathbb T,\mu_{r_p})\,\bar\otimes\,M_2(\mathbb C)
\]

and give it the normalized finite trace

\[
 \tau_p(A)=\frac12\int_{\mathbb T}
                 \mathrm{Tr}_2(A(\theta))\,d\mu_{r_p}(\theta).
                                                                    \tag{3}
\]

In particular \(\tau_p(I)=1\).  The measurable fields
\(F_p(\theta)=F_{p,\theta}\), \(U_p(\theta)=U_{p,\theta}\), and
\(\mathbf J_p(\theta)=\mathbf J\) belong to its real subalgebra.  The
complexification is used so that the analytic logarithm in Theorem 5.1 is
an element of the ambient von Neumann algebra.  Fiberwise integration of
\(\Omega\) and \(g\) gives a
nondegenerate alternating form and a positive metric on

\[
 \mathcal V^1_p=L^2(\mathbb T,\mu_{r_p};\mathbb R^2).
\]

Theorem 3.1 therefore holds on the entire module.

### Theorem 4.1 — The literal von Mangoldt tower is a polarized trace

For every integer \(k\),

\[
 \boxed{
 \tau_p(U_p^k)=p^{-|k|/2}.}                         \tag{4}
\]

Hence, for every \(k\geq1\),

\[
 \boxed{
 \frac{\log p}{p^{k/2}}
 = (\log p)\,\tau_p(U_p^k).}                       \tag{5}
\]

#### Proof

Since \(U_p(\theta)=R_\theta\),

\[
 \frac12\mathrm{Tr}_2(U_p(\theta)^k)=\cos(k\theta).
\]

The Fourier coefficients of the Poisson measure are
\(\int e^{ik\theta}d\mu_{r_p}=r_p^{|k|}\).  Taking real parts gives

\[
 \tau_p(U_p^k)=\int\cos(k\theta)d\mu_{r_p}(\theta)
 =r_p^{|k|}=p^{-|k|/2}.
\]

Multiplication by \(\log p\) gives (5). \(\square\)

This is a trace in a finite von Neumann algebra, not the ordinary operator
trace on the direct-integral Hilbert space.  More precisely,
\(L^\infty(\mu_{r_p})\bar\otimes M_2\) is a finite type-I algebra with diffuse
center, not a type-II factor.  Its normal trace nevertheless has the exact
continuous averaging required by (4).

## 5. The prime channel as an odd graded trace

Place \(\mathcal V^1_p\) formally in degree one and define its contribution
to the graded local trace with the sign \((-1)^1=-1\).  For any admissible test
function \(\widehat h\) on positive lengths, Theorem 4.1 gives

\[
 \boxed{
 -\sum_p\sum_{k\geq1}(\log p)\,
   \tau_p(U_p^k)\,\widehat h(k\log p)
 =-\sum_p\sum_{k\geq1}
   \frac{\log p}{p^{k/2}}\widehat h(k\log p).}     \tag{6}
\]

Thus the complete ordinary prime-power channel of the Weil explicit formula
is the distributional graded trace of an unconditionally polarized family
of local degree-one coefficient systems.  Calling it a cohomological
supertrace requires the still-unbuilt global complex and Lefschetz theorem.

Equation (6) is not obtained by assigning a negative metric to the prime
blocks.  Every fiber metric is positive.  The minus sign is solely the
cohomological parity.

### Theorem 5.1 — Polarized analytic determinant of the Euler factor

For \(\Re s>1\), put \(z_p(s)=p^{1/2-s}\).  The power-series branch of the
operator logarithm is well defined because \(|z_p(s)|<1\), and

\[
 \boxed{
 \exp\!\left[-\tau_p\log(I-z_p(s)U_p)\right]
 =(1-p^{-s})^{-1}.}                                \tag{6a}
\]

Consequently

\[
 \boxed{
 \zeta(s)=
 \exp\!\left[-\sum_p\tau_p
       \log(I-p^{1/2-s}U_p)\right],
 \qquad \Re s>1.}                                 \tag{6b}
\]

#### Proof

The normalized matrix trace and the two eigenvalues \(e^{\pm i\theta}\)
of \(U_p(\theta)\) give

\[
 \begin{aligned}
 \tau_p\log(I-zU_p)
 &=\frac12\int\left[
     \log(1-ze^{i\theta})+\log(1-ze^{-i\theta})
   \right]d\mu_{r_p}(\theta)\\
 &=-\sum_{k\geq1}\frac{z^k}{k}
       \int\cos(k\theta)d\mu_{r_p}(\theta)\\
 &=-\sum_{k\geq1}\frac{(zr_p)^k}{k}
 =\log(1-zr_p).
 \end{aligned}
\]

With \(z=p^{1/2-s}\) and \(r_p=p^{-1/2}\), this is
\(\log(1-p^{-s})\), proving (6a).  Absolute convergence for \(\Re s>1\)
permits summation over primes and proves (6b). \(\square\)

Unlike the circle-generator regularized determinant of 106.01, (6a) uses a
bounded normalized monodromy inside a finite von Neumann algebra carrying a
positive polarization.  Both constructions remain safe-half-plane local
realizations; neither supplies the global analytic continuation or the
zero-carrying cohomology.

## 6. Why the winding obstruction disappears locally

The heat construction of 106.152 required subtracting the \(k=0\) winding
from a heat semigroup.  Since winding numbers add, the nonzero sectors are
not an ideal and the subtraction destroys composition.

No such operation occurs in (6).  A Lefschetz orbit distribution is indexed
from the beginning by nontrivial iterates \(k\geq1\) of a closed orbit.  It
is not the trace of a heat semigroup after deleting its identity path.
Therefore (6) neither assumes nor violates a semigroup law on the complement
of winding zero.

This gives a precise meaning to the parity diagnosis:

\[
 \text{relative nonzero-winding heat trace}
 \quad\rightsquigarrow\quad
 \text{degree-one Lefschetz graded trace}.          \tag{7}
\]

The right side retains the literal prime coefficients without asking a
non-ideal sector to compose.

## 7. Monoidal compatibility of the Poisson weights

The construction is compatible with multiplication of root characters.
For \(0<r,s<1\), convolution on the circle satisfies

\[
 \boxed{\mu_r*\mu_s=\mu_{rs}.}                     \tag{8}
\]

Indeed the \(k\)-th Fourier coefficient of the left side is
\(r^{|k|}s^{|k|}=(rs)^{|k|}\), which characterizes the right side.

Writing \(r=e^{-\ell/2}\), equation (8) becomes

\[
 \mu_{e^{-\ell_1/2}}*\mu_{e^{-\ell_2/2}}
 =\mu_{e^{-(\ell_1+\ell_2)/2}}.                   \tag{9}
\]

Angle addition also gives

\[
 R_{\theta_1}R_{\theta_2}=R_{\theta_1+\theta_2}. \tag{10}
\]

Consequently the pair consisting of normalized monodromy and normal weight
is functorial under addition of lengths and multiplication of characters.
This matches the character multiplication used for rooted arithmetic
divisors in the arithmetic Picard monoid.  It is stronger than a
coefficient-by-coefficient coincidence: the entire family of prime weights
forms a convolution semigroup.

### Theorem 7.1 — One generic Poisson correspondence contains all primes

For \(t>0\), write

\[
 \nu_t:=\mu_{e^{-t/2}}.
\]

Then

\[
 \boxed{\nu_t*\nu_u=\nu_{t+u}}                    \tag{10a}
\]

and the convolution operators

\[
 P_tf=f*\nu_t
\]

form a strongly continuous, self-adjoint Markov semigroup on
\(L^2(\mathbb T,d\theta/(2\pi))\), with

\[
 \boxed{
 P_te^{ik\theta}=e^{-|k|t/2}e^{ik\theta},
 \qquad P_t=e^{-t|D|/2}.}                         \tag{10b}
\]

At the arithmetic times \(t=\log p\),

\[
 \nu_{\log p}=\mu_{p^{-1/2}},
 \qquad
 \bigl(P_{\log p}e^{ik\theta}\bigr)(0)
 =p^{-|k|/2}.                                    \tag{10c}
\]

#### Proof

The \(k\)-th Fourier coefficient of \(\nu_t\) is
\(e^{-|k|t/2}\).  Products of Fourier coefficients prove (10a), and
(10b) follows by diagonalization in the Fourier basis.  Positivity and
preservation of constants follow because each \(\nu_t\) is a probability
measure; self-adjointness follows from its even density.  Equation (10c) is
the specialization \(t=\log p\), evaluated at the identity of the circle.
Equivalently,
\(\int_{\mathbb T}e^{ik\theta}\,d\nu_{\log p}(\theta)=p^{-|k|/2}\).
\(\square\)

Thus the finite-prime normal weights do not have to be glued pairwise.  They
are restrictions of one generic length evolution.  The algebra and the
fiberwise polarization remain fixed while the normal state evolves by
\(P_t\).

This is a global interpolation only in the category of Markov
correspondences.  It is not yet a flat local system for the scaling flow:
the state changes with \(t\), whereas a flat deterministic holonomy acts in
one fixed fiber.  A Markov dilation can turn \(P_t\) into a cocycle on path
space, but descending that dilation to the arithmetic Jacobian is part of
the open global construction.

## 8. Relation with the arithmetic Jacobian

Connes and Consani identify the finite fiber over \(p\) with the circle

\[
 C_p\cong\mathbb R_+^\times/p^{\mathbb Z}
     \cong\mathbb R/(\log p)\mathbb Z.
\]

Thus the base circle required by the construction is already present in
the arithmetic Jacobian.  The rooted-divisor enhancement fixes characters
on the torsion dual, and its tensor product multiplies those characters.
Equations (8)--(10) define a measurable polarized local system over this
existing orbit, rather than inventing a new prime circle.

The 2026 arithmetic Jacobian does not itself provide a polarization,
intersection form, Hodge index theorem, or a cohomology of its square.  Its
semi-norms live on rank-one arithmetic divisors and may vanish at the
archimedean boundary.  The present construction adds a polarized local
coefficient system on each finite orbit; it does not promote the Jacobian
monoid to a globally polarized abelian variety.

## 9. The exact global gluing problem

Let \(\mathcal X_{\mathbb Q}\) denote the visible Riemann sector, with finite
fibers \(C_p\), generic fiber \(C_\eta\simeq\mathbb R_+^\times\), and the
absorbing archimedean fixed point \(C_\infty\).  The next construction must
produce a global graded object \(\mathscr H^\bullet\) with the following
properties.

1. **Finite-orbit restriction.**  Its degree-one restriction to every
   \(C_p\) is the finite von Neumann coefficient module
   \(\mathcal V^1_p\) above.
2. **Polarized descent.**  The forms \(\Omega_p\), complex structures
   \(\mathbf J_p\), and normal traces \(\tau_p\) descend from one global
   line-valued alternating form and one positive polarization.
3. **Generic gluing.**  Upgrade the Markov correspondence of Theorem 7.1 to
   a coefficient object on the dense generic fiber; the prime systems must
   not remain a disjoint sum.
4. **Archimedean completion.**  A stalk or fixed-point complex at
   \(C_\infty\) produces the Gamma and polar terms and cancels the divergent
   identity channel.
5. **Lefschetz theorem.**  The distributional supertrace of the scaling flow
   is the completed Weil explicit formula.
6. **Spectral comparison.**  The global degree-one cohomology is identified
   with the zero-carrying cokernel of the adelic trace formula.

Items 1 and the scalar finite-prime distribution required by item 5 are
proved by Theorems 3.1 and 4.1.  The global Lefschetz theorem itself is not
proved.  Equations (8)--(10) provide the local monoidal datum needed by item
2, and Theorem 7.1 solves the generic interpolation at the level of Markov
correspondences.  Items 2--6 remain open at the cohomological level.

The first unresolved identity is therefore no longer the existence of a
positive polarization on a prime tower.  It is the **global polarized
descent map**

\[
 \boxed{
 \mathrm{Desc}:
 \{(\mathcal V^1_p,\Omega_p,\mathbf J_p,\tau_p)\}_p
 \longrightarrow
 (\mathscr H^1,\Omega,\mathbf J,\tau)
 }                                                     \tag{11}
\]

through the generic and archimedean fibers.

## 10. Semantic distinction from earlier polarization attempts

Earlier constructions in Phases 15, 39, 42, and 62 started from the Weil
pairing, the zero spectrum, or a finite matrix equivalent to Weil
positivity.  Their candidate polarization was genuine precisely when RH
held.

The local systems in this document have a different logical status:

* they are defined solely from the literal prime \(p\), the circle
  \(C_p\), and the positive Poisson measure \(\mu_{p^{-1/2}}\);
* their polarization is positive by the two-dimensional identity (2),
  independently of every zeta zero;
* their normalized finite trace gives the literal arithmetic coefficient
  by (4);
* their construction requires the ordinary positive Euler weights and is
  absent for a Dirichlet series without an Euler product of this form.

What has not been constructed is the global descent which would turn these
local polarized systems into the zero-carrying adelic cohomology.  Claiming
that descent from the explicit formula alone would return to Weil
positivity; it must instead be defined geometrically on the arithmetic
Picard/Jacobian data.

## 11. Status

Proved:

* an unconditional weight-one similitude \(F_{p,\theta}\) on every prime
  orbit;
* a positive fiberwise polarization and compatible complex structure;
* a finite normal trace reproducing every \(p^{-k/2}\);
* the exact prime channel as an odd graded trace;
* convolution-semigroup and character-multiplication compatibility;
* one generic Poisson--Markov semigroup whose arithmetic times are all
  ordinary prime fibers;
* avoidance of the nonzero-winding semigroup obstruction.

Not proved:

* polarized descent across different prime fibers;
* the generic and archimedean stalks;
* a global differential and cohomology carrying the new coefficient system;
* a global Lefschetz theorem for that complex;
* identification of its global \(H^1\) with the zero-carrying adelic
  cokernel;
* RH.

The construction supplies a local, unconditionally polarized degree-one
coefficient object in this branch.  It does not yet supply a cohomology.
Its next test is global descent and construction of the differential, not a
new positivity estimate.
