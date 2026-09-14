# P123.084 — The continuous degree-zero shadow of localized twists

Date: 2026-09-06. Status: PROVED-IN-REPOSITORY for the original rapid
C_0 topology of P123.019, with S_f nonempty. This is a restriction on
that topology and on the underived Hausdorff shadow, not on every
derived, integrable or renormalized diagonal.

For a Gamma-invariant open U in X_S, take E_(U,a) from P123.083 and
the continuous shadow of P123.065. Write D for the scalar rapid algebra
on the abelian group Gamma. Then

    Q_A(E_(U,a)) = 0                 if 0 is not in U,
    Q_A(E_(U,a)) isomorphic to D     if 0 is in U.              (1)

The second isomorphism is induced by coefficientwise evaluation at the
common coordinate origin. It is independent of the external twist a.

## 1. Continuous twisted traces have finite coefficient measures

Let tau:I_U->C be continuous and satisfy

    tau(c x)=tau(x beta_a(c))  for c in A, x in I_U.

There are k and C with |tau(x)|<=C p_k(x). Consequently
tau_gamma(f)=tau(f U_gamma) is a bounded functional on C_0(U), of norm
at most C H(gamma)^k. Represent it by a finite complex Radon measure
mu_gamma on U. This use of a finite measure is specific to the sup-norm
coefficient topology; it is not justified in the stronger integrable
topologies of P123.051–057.

Choose c=U_delta and x=f U_(delta^-1 gamma). Since beta_a fixes U_delta
and Gamma is abelian, the trace identity gives

    tau_gamma(alpha_delta(f))=tau_gamma(f).

Thus each mu_gamma is Gamma-invariant. Extend it by zero to X_S;
invariance is preserved since U is invariant. Its finite total-variation
measure is invariant as well, since pushforward by a homeomorphism
commutes with total variation.

## 2. Finite invariant measures are supported at the origin

For the real coordinate fix p in S_f. The shells

    {x: p^j <= |x_infinity| < p^(j+1)}, j in Z,

are disjoint translates of one another by powers of p, and cover the
set with nonzero real coordinate. Invariance gives them equal mass;
finiteness forces this mass to be zero. For each finite coordinate q
in S_f use instead the disjoint shells {x: |x_q|_q=q^j}, j in Z,
which are permuted transitively by powers of q. Their masses likewise
vanish. There are finitely many coordinates, so the measure is supported
where every coordinate is zero. This argument applies to the extended
total-variation measure and hence to the original complex measure.

If 0 is not in U, all mu_gamma vanish. Otherwise
mu_gamma=c_gamma delta_0, with |c_gamma|<=C H(gamma)^k. Finite-label
sums are dense in I_U, so

    tau(x)=sum_gamma c_gamma x_gamma(0).

The sum converges absolutely by the rapid seminorm bound. Conversely,
every continuous functional on D composed with evaluation at zero is
a twisted trace: evaluation intertwines beta_a with identity, and D
is commutative.

## 3. Identification of the closed commutator subspace

Let R be the closed span of c x-x beta_a(c). If 0 is absent, all
continuous functionals annihilating R vanish, so Hahn--Banach separation
in the Hausdorff locally convex quotient implies R=I_U.

If 0 is present, evaluation ev_0:I_U->D is continuous and onto. Indeed,
choose h in C_c(U) with h(0)=1; the map (d_gamma)->(d_gamma h) is a
continuous linear section in all rapid seminorms. The preceding trace
classification and Hahn--Banach give R=ker(ev_0). The induced quotient
isomorphism to D is topological, either by this section or by the
Frechet open mapping theorem. This proves (1).

## 4. Consequence for the construction of A

The localized composition theorem P123.083 remains valid. However,
every such localized twist supported away from the origin has zero
continuous underived shadow. Composing it with another localized twist
or an original twist leaves its support away from the origin, because
external dilations fix zero. Thus all scalar continuous degree-zero
trace tests obtained from those compositions vanish too. Taking finite
sums or bounded cones and the degreewise shadow does not repair this.

This does not prove that the required numerical quotient in A.6 is
zero: its determinant/derived trace target has not yet been constructed,
and higher homology or a different admissible topology is not computed
here. It does rule out using the present degree-zero continuous shadow
to distinguish these localized geometric classes.

The next construction must explicitly carry the integrable boundary
trace domains already developed in P123.051–058, or construct the
required derived/renormalized target with its domain and comparison.
In particular the bounded approximate-identity estimates used for
P123.083 cannot simply be assumed for stronger integrable seminorms.
The composition theorem and nonvanishing trace domain must be made
compatible before this localized sector can contribute to closing A.
