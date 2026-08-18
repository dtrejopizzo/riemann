# D.101 — Maximal neutral Euler--Gamma relation and its Calderon defect

## Status

There is a canonical maximal neutral relation defined by the completed
Euler--Gamma determinant before choosing a zero polarization: on the
central boundary it is the graph of the unitary functional-equation phase.
It is neutral, maximal, translation invariant and Real-reflection
covariant.  Its infinitesimal Green form is the prime--Gamma normal
connection of D.94 and pulls back to the completed Weil form of D.97.

Its Calderon/Hardy quotient does not leave only the two Tate residues.  The
rational polar factor contributes the prescribed two-dimensional Tate
defect, while the nontrivial inner factor contributes its full model space.
At finite Blaschke level the latter dimension is the divisor degree; in the
completed limit it is the spectral quotient.  Removing it requires
cancelling the nontrivial inner factor, which either changes the Green form
or uses the divisor one is trying to localize.

Local prime phases cannot define alternative neutral graphs because they
are not unitary on the boundary.  Abstract unitary graphs exist, but their
choice is unrelated to the A--B--C contact and their infinitesimal Green
form is not `B_nuc`.

Thus the maximal-neutral-relation route constructs the correct boundary
triple but does not prove its reflection positivity.  The exact obstruction
is the Toeplitz/model-space defect of the nontrivial completed factor.

No RH statement or zero localization is assumed.  The paper is not
modified.

## 1. Maximal neutral graphs

Let `H_b` be the boundary Hilbert space in logarithmic spectral
coordinates and put

\[
 \mathcal K_b=H_b\oplus H_b,
 \qquad
 [(x_+,x_-),(y_+,y_-)]
 =\langle x_+,y_+\rangle-\langle x_-,y_-\rangle.           \tag{1.1}
\]

For any unitary `U` on `H_b`, its graph

\[
 \mathcal N_U=\{(x,Ux):x\in H_b\}                         \tag{1.2}
\]

is neutral because

\[
 [(x,Ux),(y,Uy)]=0.                                      \tag{1.3}
\]

It is maximal neutral: if `(a,b)` is Krein-orthogonal to every `(x,Ux)`,
then

\[
 \langle a-U^*b,x\rangle=0\quad\text{for every }x,
 \qquad b=Ua,                                             \tag{1.4}
\]

so `(a,b)` already belongs to the graph.

This construction is prior to any positivity on a source subspace; it is
the natural boundary Cauchy relation for a doubled first-order operator.

## 2. The completed Euler--Gamma unitary

For the displaced determinant family define, as in D.96,

\[
 \Theta_a(\tau)
 ={\Xi(1/2-a-i\tau)\over\Xi(1/2+a-i\tau)}.                \tag{2.1}
\]

The functional equation and reality give

\[
 |\Theta_a(\tau)|=1                                      \tag{2.2}
\]

for real `tau` away from a discrete boundary divisor.  Therefore

\[
 U_a=M_{\Theta_a}:L^2(\mathbb R,d\tau)\to L^2(\mathbb R,d\tau)
                                                                    \tag{2.3}
\]

is unitary and `N_(U_a)` is maximal neutral.

Translations in the logarithmic variable are multipliers
`e^(i tau c)` in this representation, so they commute with `U_a`.  The
Real involution sends `tau` to `-tau` and exchanges the two graph legs;
(2.1) is covariant by the functional equation.  Thus the relation has the
required A--B semigroup and reflection symmetries.

Differentiating the graph in `a` gives the boundary connection

\[
 G_a=-U_a^*\partial_aU_a
 =-\partial_a\log\Theta_a                              \tag{2.4}
\]

in multiplier form.  The divisor-normalized Pick/Green kernel of (2.4) is
the kernel in D.97.  Its pullback is

\[
 \langle M(f),CM(g)\rangle-B_{\rm nuc}(f,g).              \tag{2.5}
\]

Consequently this neutral relation is trace-exact for every prime power,
Gamma and the two Tate residues.

## 3. Calderon polarization and the Toeplitz defect

Let `H^2` be the Hardy Cauchy data of the right-half-plane Dirac operator
and let `P_+` be its Calderon projector.  Relative position of the two
neutral graphs is measured by the Toeplitz operator

\[
 T_{\Theta_a}=P_+M_{\Theta_a}|_{H^2}.                     \tag{3.1}
\]

For an inner finite Blaschke factor `B`, multiplication maps `H^2`
isometrically into itself and

\[
 \mathcal K_B=H^2\ominus BH^2,
 \qquad\dim\mathcal K_B=\deg B.                           \tag{3.2}
\]

This is the Calderon defect/model space.  For a general completed inner or
generalized-inner factor, the same construction gives the corresponding
closed model space, with Pontryagin corrections for poles.

Factor the completed boundary phase schematically as

\[
 \Theta_{\rm comp}
 =\Theta_{\rm Tate}\,\Theta_{\rm nt}.                    \tag{3.3}
\]

The rational factor `Theta_Tate` represents the two prescribed polar
channels at `s=0,1`.  Its finite model defect has dimension two.  The
nontrivial factor `Theta_nt` contributes an additional model space

\[
 \mathcal K_{\Theta_{\rm nt}}
 =H^2\ominus\Theta_{\rm nt}H^2,                           \tag{3.4}
\]

or its generalized version.  At finite divisor truncation its dimension
and negative index are the zero/pole counts of D.95--D.100.  It does not
vanish merely because the boundary phase is unitary.

Therefore

\[
 \boxed{
 \mathrm{Def}(T_{\Theta_{\rm comp}})
 =\mathrm{Def}(T_{\Theta_{\rm Tate}})
  \mathbin{\widehat\oplus}
  \mathrm{Def}(T_{\Theta_{\rm nt}}),}              \tag{3.5}
\]

with the usual nonorthogonal extension when factors share boundary data.
The first term is the desired two-channel boundary; the second is the
spectral quotient and is not zero a priori.

## 4. Why the nontrivial defect cannot be cancelled for free

Multiplying the graph phase by `Theta_nt^(-1)` would remove (3.4), but it
also changes the logarithmic connection by

\[
 -\partial_a\log\Theta_{\rm nt}^{-1}
 =+\partial_a\log\Theta_{\rm nt}.                        \tag{4.1}
\]

This subtracts exactly the nontrivial divisor/explicit-formula
contribution from (2.5).  The resulting relation no longer has Green form
`B_nuc`.

Alternatively, one may quotient by the model space (3.4).  Defining the
quotient is canonical once the full inner factor is known, but proving
that its Real metric is positive is the free-orbit problem of D.95.  A
quotient chosen as the negative spectral subspace is circular.

The Poisson/Meyer summation relation exhibits the same phenomenon: its
two residue channels are finite, but its cokernel is the spectral
realization rather than zero.  Exactness of the summation triangle is an
Euler/supertrace identity; it does not turn the spectral cokernel into a
positive Hilbert space.

## 5. Local graphs are not neutral

One might try to avoid the global model defect by taking a product of
local neutral graphs.  The prime ratio of D.100 satisfies

\[
 |R_{p,a}(1)|>1,
 \qquad |R_{p,a}(-1)|<1.                                 \tag{5.1}
\]

Hence multiplication by `R_(p,a)` is not unitary and its graph obeys

\[
 [(x,R_{p,a}x),(x,R_{p,a}x)]
 =\|x\|^2-\|R_{p,a}x\|^2,                               \tag{5.2}
\]

which takes both signs.  Only the **completed global** functional-equation
phase is unitary.  Thus local tensoring cannot construct the desired
maximal neutral relation before the global completion.

Abstractly choosing unrelated unitaries between the infinite positive and
negative feature channels would make a neutral graph, but it would not
intertwine the determinant normal connection (2.4); its pullback would not
be (2.5).

## 6. Boundary-triple formulation

The doubled Dirac operator has boundary maps `(Gamma_0,Gamma_1)` with
Green identity

\[
 \langle D^*u,v\rangle-\langle u,D^*v\rangle
 =[\Gamma u,\Gamma v].                                   \tag{6.1}
\]

The graph `N_(U_a)` specifies a self-adjoint boundary relation because it
is maximal neutral.  Its Weyl/Calderon derivative is (2.4), and the
associated infinitesimal boundary Gram is (2.5).  Hence A--B--C does
construct a boundary triple whose Green form is the completed form.

Self-adjointness of a boundary relation is not positivity of its
infinitesimal metric.  Reflection positivity would require the model space
(3.4) to have no free Real hyperbolic block.  By D.95, this is exactly the
nontrivial divisor localization.

## 7. Outcome

The strongest source-defined neutral relation currently available has all
the requested structural properties:

1. maximal neutral and self-adjoint as a boundary relation;
2. invariant under logarithmic translations;
3. compatible with the functional-equation reflection;
4. infinitesimal Green form equal to the full A--B--C contact.

Its quotient is not the two-dimensional Tate space.  It is

\[
 \text{Tate defect}\quad\oplus\quad\text{nontrivial model space}.   \tag{7.1}
\]

The remaining possible improvement must construct, from the **additive
Poisson/summation complex rather than the multiplicative determinant
phase**, a chain contraction which pairs the nontrivial model space in
neutral doublets while preserving the Green form.  Contractibility alone
will not imply positivity; the contraction must be bounded, Real and
isometric.  The next audit tests whether the Fourier--Poisson involution
provides such an isometric contracting homotopy or leaves precisely the
Meyer spectral cokernel.

