# 106.199 — Global Hilbert completion and the Gamma-compliance kernel

## 1. Purpose

Documents 106.196--106.198 construct positive finite-level
Gamma--Euler--polar pushouts and a topologically faithful derived jet
localization.  Two logically different assertions must now be separated.

First, the positive pushouts possess a canonical Hilbert direct limit.
Second, the product of all translated jets in 106.197 does not, merely by
being a topological embedding, define a vector in that Hilbert limit.  Its
image topology was the rapid-jet topology transported from the Schwartz
space.  A Hilbert aggregation of the orbit coordinates remains necessary.

This note constructs the first intrinsic nonlocal aggregation supplied by
the operator-valued Gamma boundary.  It is positive, faithful on the scalar
Schwartz core, and exactly equivariant for real scaling.  It therefore
passes the dense-orbit obstruction of 106.185.  The note then isolates the
remaining relative descent: the CCM restriction range must remain proper
after completion in the *coupled* prime--Gamma--polar graph norm.  This is
the point not supplied by the scalar kernel alone.

## 2. The Hilbert direct limit of the pushouts

Let

\[
 (\mathbb P_S,g_{\mathbb P,S},J_S,V_t)
\tag{1}
\]

be the operator-valued finite pushout of 106.198, where \(S\) ranges over
finite sets of primes.  For \(S\subset T\), extension by zero gives the
polarized isometry

\[
 \iota_{S,T}:\mathbb P_S\longrightarrow\mathbb P_T.
\tag{2}
\]

The compatibility in 106.198 means

\[
 \begin{aligned}
 g_{\mathbb P,T}(\iota_{S,T}v,\iota_{S,T}w)
   &=g_{\mathbb P,S}(v,w),\\
 J_T\iota_{S,T}&=\iota_{S,T}J_S,\\
 V_t\iota_{S,T}&=\iota_{S,T}V_t .
 \end{aligned}
\tag{3}
\]

Define the algebraic direct limit and its completion by

\[
 \mathbb P_{\rm alg}=\varinjlim_S\mathbb P_S,
 \qquad
 \boxed{\mathbb P_\infty=
   \overline{\mathbb P_{\rm alg}}^{\,g_{\mathbb P}}.}
\tag{4}
\]

### Theorem 2.1 — Canonical global source polarization

The form \(g_{\mathbb P}\) is positive definite on
\(\mathbb P_{\rm alg}\).  The operators \(J_S\) and \(V_t\) induce on
\(\mathbb P_\infty\) an orthogonal complex structure \(J_{\mathbb P}\)
and a strongly continuous orthogonal group \(V_t\).  Consequently

\[
 \boxed{
 \Omega_{\mathbb P}(v,w)
   :=g_{\mathbb P}(J_{\mathbb P}v,w)}
\tag{5}
\]

is a bounded nondegenerate alternating form, and
\(e^{t/2}V_t\) is a polarized weight-one similitude.

#### Proof

Every vector in the algebraic limit is represented at some finite level.
Equation (3) makes its squared norm independent of the representing level,
and finite-level definiteness makes it positive unless the vector is zero.
The compatible isometries \(J_S\) define an isometry on the dense algebraic
limit; it extends to the completion and still satisfies
\(J_{\mathbb P}^2=-I\).  The same argument defines each \(V_t\).
Strong continuity holds first on a finite-level representative, where it
was proved in 106.198, and then on the completion by the common unitary
bound.  Formula (5) has all the standard polarization properties. \(\square\)

This theorem completes the source Hilbert object.  It does not yet put a
norm on the CCM cokernel.

## 3. What the jet embedding does and does not prove

For a logarithmic Schwartz profile \(F\), 106.197 constructs

\[
 \mathfrak L_\infty F
 =\bigl(\mathfrak L(D^nT_gF)\bigr)_{g\in G,\ n\geq0},
 \qquad G=\log\mathbb Q_+^\times,
\tag{6}
\]

and recovers every jet from the literal \((2,1)\) coordinate.  This proves
a topological embedding when the image is equipped with the transported
rapid-jet seminorms.  It does not specify a Hilbert norm on the product in
(6), nor a map from (6) to the single space \(\mathbb P_\infty\).

This distinction is forced by 106.185: a diagonal sum of the orbit samples
cannot be simultaneously finite, faithful, and invariant under the dense
group \(G\).  Therefore the missing aggregation must correlate different
times.  The full Gamma compliance in 106.198 provides a canonical such
correlation.

## 4. The nonlocal Gamma-compliance kernel

Let \((\mathscr K,V_t)\) be the common Cauchy coefficient space of
106.154.  Choose the real cyclic unit vector \(b\) for which

\[
 \langle b,V_tb\rangle=e^{-|t|/2}.
\tag{7}
\]

Its spectral measure for the self-adjoint generator
\(V_t=e^{itA}\) is the Cauchy probability measure

\[
 d\nu_C(\gamma)
 ={1\over2\pi}{d\gamma\over\gamma^2+1/4},
\tag{8}
\]

which has strictly positive density on the whole real line.  Retain the
strictly positive Gamma boundary operator

\[
 K_\Gamma=\kappa_\infty I+m_\Gamma(A)
\tag{9}
\]

from 106.198 and put

\[
 \psi_\Gamma=K_\Gamma^{-1/2}b,
 \qquad
 \boxed{\kappa_\Gamma(t)=
   \langle\psi_\Gamma,V_t\psi_\Gamma\rangle.}
\tag{10}
\]

The spectral formula is

\[
 \boxed{
 \kappa_\Gamma(t)
 =\int_{\mathbb R}e^{it\gamma}
   {d\nu_C(\gamma)\over
    \kappa_\infty+m_\Gamma(\gamma)}.}
\tag{11}
\]

### Theorem 4.1 — Positive, nonlocal, faithful real-orbit aggregation

For \(F\in\mathcal S(\mathbb R)\), the Bochner integral

\[
 \boxed{
 \mathcal W_\Gamma F
 =\int_{\mathbb R}F(t)V_t\psi_\Gamma\,dt}
\tag{12}
\]

exists in \(\mathscr K\).  It satisfies

\[
 \begin{aligned}
 q_\Gamma(F,G)
 &:=\langle\mathcal W_\Gamma F,
            \mathcal W_\Gamma G\rangle\\
 &=\iint_{\mathbb R^2}F(t)\overline{G(u)}
       \kappa_\Gamma(u-t)\,dt\,du\\
 &=\int_{\mathbb R}
   \widehat F(\gamma)\overline{\widehat G(\gamma)}
   {d\nu_C(\gamma)\over
    \kappa_\infty+m_\Gamma(\gamma)}.
 \end{aligned}
\tag{13}
\]

In particular, \(q_\Gamma\) is positive definite, nonlocal, and faithful
on \(\mathcal S(\mathbb R)\).  If
\((T_sF)(t)=F(t-s)\), then

\[
 \boxed{
 \mathcal W_\Gamma T_s=V_s\mathcal W_\Gamma,
 \qquad
 q_\Gamma(T_sF,T_sG)=q_\Gamma(F,G).}
\tag{14}
\]

#### Proof

Since \(K_\Gamma\succeq\kappa_\infty I\), the vector
\(\psi_\Gamma\) exists and
\(\|\psi_\Gamma\|\leq\kappa_\infty^{-1/2}\).  Schwartz functions are
integrable, so (12) is a norm-convergent Bochner integral.  Expanding its
inner product gives the second line of (13).  Applying the spectral theorem
to \(A\), followed by Fubini, gives the third line.

The density in the last integral is strictly positive for every real
\(\gamma\): \(\nu_C\) has full support and
\(0<(\kappa_\infty+m_\Gamma(\gamma))^{-1}leq
\kappa_\infty^{-1}\).  If \(q_\Gamma(F,F)=0\), then
\(\widehat F=0\) almost everywhere.  Continuity of the Schwartz Fourier
transform gives \(\widehat F=0\) everywhere, hence \(F=0\).  Finally,
the substitution \(t=u+s\) in (12) gives
\(\mathcal W_\Gamma T_sF=V_s\mathcal W_\Gamma F\), proving (14).
\(\square\)

The kernel (11) is the first explicit source-defined kernel in this branch
which passes the four-way obstruction of 106.185: it is finite, faithful,
translation invariant, and genuinely off diagonal.  The Gamma phase is
retained before taking a norm.

## 5. Why this does not yet descend to CCM degree one

The map \(\mathcal W_\Gamma\) acts on the scalar logarithmic profile.  It
does not by itself impose the adelic restriction differential.  If one
simply quotients its Hilbert target by the closure of the CCM restriction
range, the dense-range phenomenon of 106.164 and 106.189 can still make
the quotient zero.

### Theorem 5.1 — Scalar Gamma compliance still has zero reduced cokernel

Let \(M(\gamma)\) be the Mellin multiplier of the scalar CCM restriction
map on the critical real spectral line.  Assume only that \(M\) is not
identically zero and is the boundary value of the corresponding
meromorphic completed Euler function.  Then multiplication by \(M\) has
dense range in

\[
 L^2\!\left(\mathbb R,
 {d\nu_C(\gamma)\over
  \kappa_\infty+m_\Gamma(\gamma)}\right).
\tag{15a}
\]

Consequently the scalar nonlocal kernel (11), despite being positive and
faithful before descent, has zero reduced Hilbert cokernel for the CCM
restriction map.

#### Proof

The measure in (15a) is mutually absolutely continuous with Lebesgue
measure: its density is strictly positive and finite at every real
\(\gamma\).  A nonzero meromorphic function has a discrete real zero set
away from its isolated poles, hence \(M(\gamma)\ne0\) almost everywhere.
If \(h\) is orthogonal to the range of multiplication by \(M\), then

\[
 \overline{M(\gamma)}h(\gamma)=0
\quad\text{almost everywhere}.
\tag{15b}
\]

Thus \(h=0\) almost everywhere.  The orthogonal complement of the range is
zero, so the range is dense. \(\square\)

The theorem is unconditional; discrete zeros, on or off the critical
line, have measure zero and do not alter the conclusion.  It proves that
\(\mathcal W_\Gamma\) is a necessary orbit-aggregation block but cannot
be the final descent.  The charge fibers must remain distinct through the
relative quotient.  This is exactly the role of the operator law
\(K_\Gamma(E)_{q,q}=\kappa_\infty+m_\Gamma(E-\log q)\) in
106.198.

Let \(\mathscr D_c\) be the compact logarithmic CCM core and
\(\mathcal V_c\) its intersection with the restriction range.  A genuine
Hilbert descent of the coupled localization requires a map

\[
 \mathfrak D_0:\mathscr D_c\longrightarrow\mathbb P_\infty
\tag{15}
\]

defined from the prime/root/Gamma/polar relative differential, not merely
from scalar sampling, for which

\[
 \boxed{
 \mathfrak D_0^{-1}
 \left(\overline{\mathfrak D_0(\mathcal V_c)}^{\,\mathbb P_\infty}
 \right)
 =\overline{\mathcal V_c}^{\,\mathrm{CCM}}
 \cap\mathscr D_c.}
\tag{16}
\]

Equation (16) is the Hilbert-closure version of the nuclear identity in
106.197.  The latter proves (16) only for the transported rapid-jet
topology, not for the positive Hilbert topology of (4).

## 6. The positive pullback contains the complete sign

The global compensated Green identity is already proved in 106.181:
the *indefinite* joined graph/boundary form descends and equals the CCM
Rosati form.  It must not be conflated with a positive pullback from
\(\mathbb P_\infty\).

### Theorem 6.1 — Load-bearing nature of the symplectic pullback

Suppose that a real-linear injective map

\[
 \mathfrak D:H^1_{\rm Ros}\longrightarrow\mathbb P_\infty
\tag{17}
\]

intertwines the complex structures and pulls back the alternating form:

\[
 \mathfrak DJ_0=J_{\mathbb P}\mathfrak D,
 \qquad
 \Omega_{\rm Ros}(u,v)
 =\Omega_{\mathbb P}(\mathfrak Du,\mathfrak Dv).
\tag{18}
\]

Then the CCM Rosati form is positive definite:

\[
 \boxed{
 g_{\rm Ros}(u,u)
 =g_{\mathbb P}(\mathfrak Du,\mathfrak Du)>0
 \quad(u\ne0).}
\tag{19}
\]

Consequently (17)--(18) imply Weil positivity and RH.

#### Proof

Use 106.157(13), (18), and (5):

\[
 \begin{aligned}
 g_{\rm Ros}(u,u)
 &=\Omega_{\rm Ros}(u,J_0u)\\
 &=\Omega_{\mathbb P}(\mathfrak Du,
                    J_{\mathbb P}\mathfrak Du)\\
 &=g_{\mathbb P}(\mathfrak Du,\mathfrak Du).
 \end{aligned}
\tag{20}
\]

The last expression is positive for nonzero \(u\) because
\(\mathfrak D\) is injective.  The Weil criterion gives the final
implication. \(\square\)

Thus the phrase ``remaining global Green identity'' must be used with
care.  The Green identity into the joined indefinite form is closed by
106.181.  Equality with the positive pushout is the complete Hodge-index
sign, not a further formal integration by parts.

## 7. Exact next construction

The source object and its first viable nonlocal real-orbit kernel are now
explicit.  The remaining construction is a relative chain map, before
Hilbert completion,

\[
 \boxed{
 \mathbf D:operatorname {Cone}(\rho^\natural)
 \longrightarrow \mathbb P_{\rm rel},}
\tag{21}
\]

with the following properties:

1. its finite-orbit component is
   \(\mathcal L_{\rm conn}\mathfrak e_1\mathrm{Tr}_{\rm orb}\);
2. its infinite component is the operator-valued Gamma row
   \(\mathbb B_\infty\), not the scalar zero-mode row;
3. its polar component is the determinant boundary of 106.195;
4. it is a chain map and is equivariant for normalized real scaling;
5. its induced map satisfies the Hilbert closure identity (16);
6. either it satisfies the symplectic comparison (18), on the fixed
   Rosati branch, or the descended \(\Omega_{\rm Ros}\) is bounded and
   weakly nondegenerate in its Hilbert norm, on the alternative branch.

Items 1--3 are constructed.  Item 4 is algebraic at every finite level.
The unresolved force-bearing assertion is item 5, together with the form
condition in item 6.  This is now a statement about the closure of one
specific relative differential, not about an unspecified local kernel.

## 8. Status

Proved without RH or zero input:

* the canonical Hilbert direct limit of all finite operator-valued
  pushouts;
* extension of the positive metric, complex structure, and normalized
  real unitary flow;
* the explicit Gamma-compliance kernel (11);
* its positivity, nonlocality, faithfulness, and exact real equivariance;
* the exact distinction between nuclear jet faithfulness and Hilbert
  closure faithfulness;
* the theorem showing that a positive symplectic pullback already contains
  the complete Hodge-index sign.

Still required:

* construction of the complete relative chain map (21) as one coupled
  prime--Gamma--polar differential;
* proof of the Hilbert closure identity (16);
* bounded weak nondegeneracy of the descended alternating form, or the
  stronger fixed-Rosati pullback (18).
