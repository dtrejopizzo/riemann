# A — a contravariant kernel duality and its classical control

Research work; do not insert into paper42 automatically.
The construction below is on a smooth projective curve. Its transfer to
the arithmetic source still requires the dualizing comparison stated last.

## Imported inputs and scope

For a smooth projective curve C over a finite field k, use perfect
kernels on C times C, derived pull-tensor-push composition, and proper
Grothendieck duality. Properness, smoothness, finite presentation and
finite Tor dimension hold here. The needed kernel composition and
adjoint statements are in the Stacks Project, Section 57.8, particularly
Lemmas 57.8.3 and 57.8.9:
https://stacks.math.columbia.edu/tag/0FYP
These inputs are not being asserted for the arithmetic Frechet category.

Choose a line h and an isomorphism h^2=omega_C. In odd characteristic
such an h exists over a finite field by Atiyah, section 5, Remark 2,
page 61 (finite fields satisfy the stated cyclic-Galois and Brauer
conditions):
https://www.numdam.org/item/10.24033/asens.1205.pdf
This is an existence result, not a canonical choice. In characteristic
two one can use a separating rational function f: the nonzero rational
differential df has even valuation at every point, since the surviving
terms in its local derivative have even exponents. Thus div(df)=2D
and O(D)^2=omega_C. The choice and its square isomorphism are retained.

## Actual contravariant involution

Let sigma interchange the two factors, H=h external_tensor h, and
K^vee=RHom(K,O_(C times C)). Define

    D_h(K)=sigma^*(K^vee) tensor H[1].                    (1)

On a morphism K->L, derived duality gives D_h(L)->D_h(K), so this
operation is genuinely contravariant. Perfect biduality and symmetry
of H give

    D_h^2(K) ~= K.                                       (2)

Explicitly the second application contributes H^-1[-1] and H[1],
which cancel. The bidual maps use the ordinary signed evaluation of
cochain complexes; no ungraded reversal of differential signs is used.

Write K star L=Rp_13*(p_12^*K tensor^L p_23^*L). Proper duality for
p_13 has relative dualizing object p_2^*omega_C[1]. Applying it to
(1), and then reversing the outer coordinates, gives the factors

    (dual reversed kernels) tensor p_2^*omega_C
                            tensor p_1^*h tensor p_3^*h[2].

On the other hand the tensor defining D_h(L) star D_h(K) has the
middle factor p_2^*(h^2), the same outer h factors, and shift [2].
The chosen h^2=omega_C therefore yields a natural isomorphism

    D_h(K star L) ~= D_h(L) star D_h(K).                  (3)

For a triple product, both associations identify each internal h^2
with the corresponding internal omega_C. This gives the associativity
coherence of (3); the tensor and proper-duality structural maps are
used with their derived signs throughout.

The unit is also preserved, not just the order of composition. The
regular diagonal has normal line T_C=omega_C^-1, so its two-term
Koszul resolution gives

    (Delta_*O_C)^vee ~= Delta_*(omega_C^-1)[-1].

Its product with H[1] restricts H to h^2=omega_C on the diagonal.
Therefore

    D_h(Delta_*O_C) ~= Delta_*O_C.                        (4)

This constructs the required shape of an involutive contravariant
composition reversal on the classical perfect-kernel category. Changing
h by a two-torsion line changes the construction; no canonical descent
of that choice is inferred.

## Why ordinary adjoints were not enough

With the convention above, the right-adjoint kernel is
R(K)=sigma^*(K^vee) tensor p_2^*omega_C[1]. Applying this twice gives

    R^2(K)=K tensor p_1^*omega_C^-1 tensor p_2^*omega_C.

It is generally not an involution. For C=P^1 and K=O_(C times C),
the result is O(2,-2), not O. Formula (1), using h=O(-1), instead
has square the identity. This is a concrete correction of the duality
operation, not an assumption that every adjoint automatically satisfies
A.4. Likewise simply swapping or conjugating the source factors is
covariant on morphisms and does not establish the contravariant claim.

## Graphs, effective cycles, and the diagonal trace

For the graph i_f:C->C times C of a finite morphism f, the normal
line is f^*T_C. The same codimension-one dual calculation gives

    D_h(O_(Gamma_f))
        =sigma_* i_f*(h tensor f^*h^-1),                  (5)

concentrated in degree zero. In particular it has the ordinary transposed
graph as its leading effective cycle, with multiplicity one. For a
Frobenius morphism (5) does not claim an integral inverse correspondence.
The line factor in (5) is necessary at the kernel level, although it
does not change the leading cycle.

More generally, a finite flat effective correspondence Z gives the
perfect kernel O_Z. Composing two such kernels computes their ordinary
fiber product over the middle curve: flatness removes higher Tor, and
the resulting map to the outer product is finite. Generic lengths of
its pushforward recover the usual effective composition cycle. This
uses actual cycle effectivity, with no positive-semidefinite cone imposed.

The diagonal shadow is R Gamma(C,L Delta^*K). If an effective Cartier
correspondence Z meets Delta properly, restricting its defining local
equation to the smooth curve Delta is a nonzerodivisor. Its Koszul
resolution therefore gives the finite intersection sheaf, and the Euler
characteristic is the sum of local intersection lengths times residue
field degrees. For the diagonal itself the derived pullback has terms
O_C and Omega_C[1]; its Euler characteristic is

    (1-g)-(g-1)=2-2g=deg T_C=Delta dot Delta.

Thus the excess term is retained in the self-intersection. Twisting a
proper zero-dimensional intersection by the line in (5) does not change
its lengths. These are explicit classical checks of composition,
transpose at the cycle level, and derived diagonal intersection.
They do not identify all perfect kernels with effective cycles.

## What is needed on the actual arithmetic source

The formula (1) suggests precise data instead of an unspecified dagger:
a relative dualizing object for the relevant projection, compatible
biduality on the admissible kernels, and a half-density/half-dualizing
factor whose square supplies that relative object in the composition
calculation. Proper duality and the unit's Koszul normalization must
then be proved for the same arithmetic coefficient/trace domain.

P123.122 constructs continuous relative bars but does not prove this
Grothendieck-type duality for their pushforwards. The analytic half-density
operators alone do not supply it either. Accordingly this construction
provides a fully typed classical model and the necessary normalization
for A.4, not a proof that A.4 or A.9 is already satisfied by the arithmetic
category. The transfer, including the determinant/metric comparison,
remains load-bearing work.

## The actual boundary: an explicit continuous dual pair

The following calculation is on S=S(Y) of P123.101, not on a replacement
finite-dimensional model. It provides a genuine involutive dual pair,
while showing why the Haar pairing is not an identification S=S'.

For a continuous complex linear functional T on S put t_chi=T(chi).
The seminorms rho_m give exactly the following description:

    T(f)=sum_chi f_hat(chi) t_chi,
    |t_chi|<=C W(chi)^m for some C,m.                     (8)

Necessity follows by applying a continuity bound to a character; sufficiency
follows from absolute summation against rho_m. Give this space S' its
strong dual topology, defined by p_B(T)=sup_(f in B)|T(f)| for bounded
subsets B of S. This explicitly specifies the topology rather than
identifying it with an unproved inductive-limit topology.

For R>0 let T_R retain only characters W(chi)<=R. These are finite sets,
by the frequency/conductor definition. If (8) has exponent m, then

    p_B(T-T_R)<=C R^-1 sup_(f in B) rho_(m+1)(f).           (9)

Thus finite Fourier functionals are strongly dense in S'.

The original bilinear Haar pairing embeds S continuously in S':

    J(f)(g)=integral_Y f g,
    J(f)(chi)=a f_hat(chi^-1),     a=log q.                (10)

It is injective by Fourier uniqueness and continuous since
p_B(J(f))<=a rho_0(f) sup_(g in B)rho_0(g). Its image is proper:
point evaluation delta_y is continuous, bounded by rho_0, but its
coefficients delta_y(chi)=chi(y) have constant modulus one. They cannot
be the rapidly decreasing coefficients in (10). In particular the
nondegeneracy of (10) does not make it a perfect topological pairing
with both factors equal to S.

There is nevertheless a canonical topological biduality

    S -> (S'_strong)'_strong,       f -> [T -> T(f)].       (11)

Here is a proof in the declared coordinates. If ell is strongly
continuous on S', there are a bounded set B in S and C such that
|ell(T)|<=C p_B(T) (combine finitely many bounded sets if necessary).
Let epsilon_chi(f)=f_hat(chi), and set f_hat(chi)=ell(epsilon_chi).
For every m, boundedness of B gives

    |f_hat(chi)|<=C sup_(g in B)rho_m(g) W(chi)^-m.

Since sum_chi W(chi)^-3 is finite, these coefficients define f in S.
On finite Fourier functionals ell(T)=T(f); (9) and continuity extend
this to all T in S'. This proves bijectivity in (11).

For the topology, the set of functionals with coefficients satisfying
|t_chi|<=W(chi)^m is strongly bounded, because its supremum on B is at
most sup_B rho_m. Its polar seminorm on the bidual is exactly rho_m(f),
by choosing the coefficient phases. Conversely any strongly bounded
family of functionals is pointwise bounded on S and therefore admits
a common continuity estimate C rho_m by uniform boundedness on the
Frechet space S. Its bidual seminorm is consequently bounded by C rho_m.
This proves both directions of the topological comparison in (11).

Transposition of a continuous linear map S->S is continuous on S'_strong:
a bounded set B maps to a bounded set, and p_B(T composed f)=p_(f(B))(T).
It reverses composition, and biduality recovers the original map. Thus
there is now an explicit continuous contravariant duality between the
smooth boundary space and its specified distributional dual, including
point masses. It is not merely an operator-adjoint notation.

## Consequence for the diagonal unit and the next composition problem

The identity kernel on the compact boundary has Fourier expansion

    (1/a) sum_chi chi(x) chi(y)^-1.

This is a continuous functional on the completed smooth tensor square:
its coefficients are bounded and pairing with the rapidly summable double
Fourier coefficients converges absolutely. Integrating it in y against
the original Haar measure gives the identity on S. It does not belong to
S(Y times Y), because its nonzero coefficients do not decay along the
diagonal sequence (chi,chi^-1). Thus the identity already has a natural
place in the distributional kernel domain just constructed.

This identifies concrete arithmetic dual objects and the distributional
unit that a geometric kernel category must accommodate. It does NOT
justify composing arbitrary distributions, nor prove that transposition
of distribution spaces commutes with every derived pull-tensor-push.
A composition domain stable under this duality, with the required trace
and half-dualizing normalization, still needs construction. This also
does not disprove the possibility of a relative S-module dualizing line:
the obstruction in (10) concerns the scalar Haar pairing specifically.

## Composable boundary kernels and their trace ideal

Continue on the actual Fourier space S(Y), with weights W and Haar mass
a. Write e_i for the characters. Let E consist of matrices A for which
both A and its coordinate transpose define continuous maps S -> S.
Equivalently, for every m there exist n,C with

    sum_i W_i^m |A_ij| <= C W_j^n   (all j),

and the analogous estimate for A^t. Necessity follows by testing e_j;
sufficiency follows by absolute summation against Fourier coefficients.
The existential exponent n is not silently treated as a fixed Frechet
seminorm index.

For A,B in E the sum (AB)_ij=sum_k A_ik B_kj converges absolutely:
rows of A have polynomial growth and columns of B are rapidly summable.
Applying continuous A to the convergent S-valued column expansion of B
identifies this matrix with operator composition. Transposition gives
(AB)^t=B^t A^t. Consequently E is an associative unital algebra closed
under transpose. Every A defines the distributional kernel

    K_A(x,y)=(1/a) sum_ij A_ij e_i(x)e_j(y)^-1,

because the m=0 estimate bounds its coefficients polynomially. Its action
on S is A. This defines composition on a specified distributional domain
without multiplying arbitrary distributions. Haar transposition is
J A^t J, where J inverts character indices, and preserves E because
W_i=W_(i^-1). This operator operation does not yet give the contravariant
functor on kernel objects required by A.4.

Give E uniform convergence on bounded subsets for A and A^t, with

    q_(B,m)(A)=sup_(x in B)rho_m(Ax)+sup_(x in B)rho_m(A^t x).

Multiplication is separately continuous. For a bounded family H in E,
uniform boundedness on the Frechet space S gives common estimates
rho_m(Ax)<=C rho_n(x) for A in H, also for their transposes. Moreover
H(B) and H^t(B) are bounded in S. These facts give uniform continuity
estimates for multiplication on either side by H. Joint continuity on
all of E x E is not asserted; this is not a full proof of A.3.

Let R consist of smooth kernel matrices, with

    r_m(R)=sum_ij |R_ij| W_i^m W_j^m < infinity  (all m).

This is a two-sided ideal of E: the column estimate above gives

    r_m(AR)<=C sum_kj |R_kj| W_k^n W_j^m
             <=C r_max(m,n)(R),

and transposition gives the other side. Multiplication by each fixed A
is continuous on R. The scalar trace tr(R)=sum_i R_ii is absolutely
convergent and satisfies

    tr(AR)=sum_ik A_ik R_ki=tr(RA).

Absolute summability follows from polynomial growth of A and rapid decay
of R. Thus the trace is cyclic on this ideal and agrees with finite-rank
trace. It does not assign a finite scalar trace to the identity.

The all-R-test radical is zero: tr(A E_ji)=A_ij for every matrix unit.
The pairing with each fixed R is continuous in the declared topology.
Indeed B_R={W_i^3 R e_i : i} is bounded in S and

    |tr(AR)| <= (sum_i W_i^-3) sup_(x in B_R)rho_0(Ax).

The sum is finite by P123.101. The radical is therefore closed, and the
boundary operator quotient is Hausdorff and nonzero. This is not yet the
arithmetic numerical quotient with its ruling plane or intersection.

### Obstruction to extending the scalar trace to every boundary kernel

Choose the actual characters e_n(t,u)=exp(2 pi i n t/a), n>=0, with
trivial unit character; their weights are comparable to 1+n. On this
subspace let U e_n=e_(n+1), V e_0=0, V e_(n+1)=e_n. On every remaining
character let U and V be the identity. All four matrices U,V,U^t,V^t
preserve each rho_m up to a constant, so U,V belong to E. Directly,

    VU=1,                 UV=1-E_00.

A cyclic scalar trace tau on E would imply tau(E_00)=tau(VU-UV)=0.
Agreement with the finite-rank trace instead requires tau(E_00)=1.
Thus no such extension exists, even without continuity assumptions.

This does not contradict A.5, which permits a trace-class domain and a
non-scalar shadow. Nor does it prove U,V are geometric correspondences.
It rules out replacing the source category by all boundary kernels while
assigning a finite cyclic scalar degree everywhere. The valid constructed
pair is (E,R): distributional identity and composition in E, cyclic scalar
trace in R. The missing arithmetic bridge must still specify the source
objects and compare their derived shadow, duality and ruling metric on
these domains. None of those comparisons follows from this calculation.

## Source graph actions, smooth averaging, and the shadow comparison

The boundary is a compact abelian group Y. Use additive notation and its
original Haar measure dy of mass a. P123.120 identifies the actual source
corner e J_sm e with S(Y), and its external real/unit translations descend
to translations of Y. The following is consequently an action of those
corner coefficients and translations, not a new coefficient identification.

Put (L_g u)(x)=u(x-g). The source coefficient f acts as M_f. Both belong
to E: translation multiplies Fourier coefficients by phases, whereas
submultiplicativity of W gives rho_m(fu)<=rho_m(f)rho_m(u).
Their Haar transposes satisfy M_f^top=M_f and L_g^top=L_-g. Thus

    (M_f L_g)(M_h L_k)=M_(f h(.-g)) L_(g+k),
    (M_f L_g)^top=M_(f(.+g)) L_-g.

These formulas prove compatibility of this action with the algebraic
translation crossed product. The kernel is f(x) delta_(x-g)(y), with
point mass normalized to act by evaluation under dy. This is genuinely
supported on the translation graph. Finite sums on distinct graphs are
faithfully represented: for fixed x the finitely many points x-g are
distinct, and smooth test functions separate them. In particular no
identification of graph kernels with smooth kernels has been made.

Smoothly average these actual actions. For F in S(Y x Y), define

    A_F u(x)=integral_Y F(x,g) u(x-g) dg.

Its kernel is K_F(x,y)=F(x,x-y). The substitution (x,y)->(x,x-y) and its
inverse induce continuous automorphisms on the completed smooth space:
on characters the index map is (i,j)->(ij,j^-1), and W_ij<=W_i W_j
bounds each output weight by a fixed power of the input weights. Hence
F->K_F is a topological isomorphism onto the smooth kernel ideal R
(the matrix normalization is A_ij=a times the corresponding kernel
Fourier coefficient). Every smooth kernel arises this way. Composition
and Haar transposition are therefore the explicit formulas

    (F diamond G)(x,h)=integral_Y F(x,g) G(x-g,h-g) dg,
    F^top(x,g)=F(x-g,-g).

Their continuity follows equally from the Fourier weight estimates or
from continuous smooth-kernel multiplication. The scalar trace is

    tr(A_F)=integral_Y F(x,0) dx.

Indeed absolute double Fourier summation identifies the matrix trace with
the integral of K_F(x,x). This proves a concrete comparison between the
source graph action, its smooth averages, and diagonal scalar integration.
It does not permit interchanging this scalar trace with an integral of
individual graph traces: individual graph operators need not lie in R.

There is a further essential distinction between this representation and
a Morita comparison of the source coefficient category. The completed
zeroth Hochschild quotient of R is exactly C, with quotient map tr.
Here is an explicit continuous splitting and boundary calculation, so no
Morita theorem for a nonunital algebra is being presumed. Fix the trivial
character index 0. In the completed projective tensor square of R define

    h(T)=sum_ij T_ij E_i0 tensor E_0j.

This converges: each projective seminorm is bounded by a constant times
sum_ij |T_ij| W_i^m W_j^n, finite and continuously bounded by an r_k(T).
For the Hochschild differential b(A tensor B)=AB-BA one has

    b h(T)=T-tr(T) E_00.

Cyclicity shows that every boundary has trace zero; the displayed formula
shows that every trace-zero T is a boundary with a continuous preimage.
Thus the boundary space is closed and R / im(b) = C topologically.
In contrast, the same zeroth quotient of the commutative source corner
S(Y) is S(Y), as also computed by the completed source model P123.118.
The latter is infinite dimensional. Consequently the smooth-averaging
representation cannot be used as a shadow-preserving Morita equivalence
from the source corner to R. It collapses the coefficient-valued shadow
to its scalar integral. Adding the distributional graph operators does
not change this calculation for the ideal R and does not automatically
extend its scalar trace to the added operators.

This gives an explicit local action and diagonal comparison, but also
pinpoints what it cannot supply: the coefficient-valued derived shadow
must be retained on the arithmetic source, with scalar integration only
on its justified trace domain. Replacing that source by its smooth
operator ideal would lose precisely the shadow information which the
arithmetic RR comparison still has to use. No full A clause is closed by
that replacement, and it is not adopted here.

## Relative diagonal shadow retains the missing coefficient information

The preceding loss of information can be avoided at degree zero by using
the correct relative input. Regard R as an S-bimodule via left and right
multiplication operators M_f; do not replace S itself by R. Define

    d:R -> S,              d(K)(x)=K(x,x).

This is continuous and split onto: the smooth kernel K(x,y)=f(x) gives
a continuous section. In the F(x,g)=K(x,x-g) coordinates, d(F)=F(x,0).
The completed degree-one Hochschild boundary for S with coefficients R is

    b:S tensorhat R -> R,  b(f tensor K)=M_f K-K M_f.

It has d b=0. In fact im(b)=ker(d), with a continuous preimage operator.
To prove this explicitly, expand

    F(x,g)=sum_ij F_ij e_i(x)e_j(g)

in the double rapid Fourier topology. Let Q_ij be the smooth kernel with
translation coordinates e_(i j^-1)(x)e_j(g). Then

    b(e_j tensor Q_ij)(x,g)
       =(e_j(x)-e_j(x-g))e_(i j^-1)(x)e_j(g)
       =e_i(x)(e_j(g)-1).

Consequently the series

    h_rel(F)=sum_ij F_ij e_j tensor Q_ij

converges in S tensorhat R and satisfies

    b h_rel(F)=F(x,g)-F(x,0).

For convergence, the seminorm of e_j is a power of W_j, while the smooth
kernel seminorms of Q_ij are bounded by powers of W_i and W_j, using
W_(i j^-1)<=W_i W_j and the coordinate isomorphism already proved.
The rapid double coefficients therefore give an absolute projective
seminorm bound with a finite increase of exponents. This proves continuity
of h_rel, not just a formal Fourier identity. The boundary image is
closed and the resulting completed degree-zero quotient is thus

    HH_0^completed(S,R) = R / im(b) ~= S.

Under this precise identification the ordinary scalar trace factors as

    tr(K)=integral_Y d(K)(x) dx.

This supplies the local coefficient-valued diagonal comparison that the
absolute shadow HH_0(R,R)=C could not retain. It uses the actual corner S
and its smooth kernel bimodule, with all maps continuous and an explicit
splitting. It is only a degree-zero relative computation. In particular
d(KL) need not equal d(LK) as S-valued functions; only their Haar integrals
agree. Thus it does not assert cyclicity of d for arbitrary composition
in R, nor a derived shadow functor for the whole arithmetic category.
Higher relative degrees, compatibility with the source kernel category,
and the determinant/metric comparison still require their own proofs.

## Full relative derived diagonal of a smooth kernel bimodule

The degree-zero comparison above has an explicit extension to all chain
degrees. Retain R as a coefficient bimodule, rather than as a replacement
coefficient algebra. The Fourier identification gives

    R ~= S tensorhat S,

with the outer S-bimodule action: f acts on the first variable on the
left, and on the second variable on the right. Thus R is a free rank-one
module over the completed enveloping algebra S tensorhat S^op. This is
an assertion about the coefficient module, not about the operator product
of two kernels.

Use the unnormalized completed Hochschild chains

    C_n(S,R)=R tensorhat S^tensorhat(n),  n>=0.

For clarity fix the standard sign convention b_1(m tensor f)=mf-fm;
this is the negative of the degree-one map in the preceding section,
with exactly the same image and degree-zero quotient. On elementary
coordinates m=u tensor v, the differential has first term
(u tensor v a_1) tensor a_2 ... a_n, usual alternating internal products,
and last term (-1)^n(a_n u tensor v) tensor a_1 ... a_(n-1).
Augment C_0 by d(u tensor v)=uv in S. The topological rearrangement

    (u tensor v) tensor a_1 ... a_n
          -> v tensor a_1 tensor ... tensor a_n tensor u

identifies this augmented complex with the two-sided multiplication bar
of S. All tensor products here are completed projective tensor products;
there are finitely many factors in each degree.

A continuous contraction is completely explicit:

    h_-1(s)=s tensor 1,
    h_n((u tensor v) tensor a_1 ... a_n)
          =(u tensor 1) tensor v tensor a_1 ... a_n.

The n=0 identity is b_1 h_0(m)=m-h_-1 d(m). In positive degrees,
expansion of b h+h b cancels adjacent internal products and leaves the
original chain. Also d h_-1=id. These identities hold first on elementary
tensors and then on completions by continuity: h only inserts a unit
and permutes factors. In particular

    C_*(S,R) ~= S[0]

by an underlying continuous chain homotopy equivalence. Every higher
cycle has the explicit continuous filler h_n, and every boundary space
is closed (it equals the kernel of the next continuous differential,
with the degree-zero augmentation included). This is the relative
completed Hochschild complex used by the source bar construction; the
contraction is not claimed to be S-bimodule linear.

Hence smooth kernel coefficients have no higher relative diagonal Tor.
This does not remove the degree-one class for the diagonal coefficient
module S itself: P123.118 computes C_*(S,S) ~= S[0] plus S dt[1]. The
modules S tensorhat S and S are different, respectively an outer free
kernel module and the diagonal module. Confusing them would erase the
self-intersection excess needed by the source theory.

## Source composition versus integration of operator kernels

The same identification determines the full source tensor, without a
flatness assumption hidden in an operator formula. Since R is relatively
free on each side, it is K-flat in the split exact structure of P123.122,
and there is a topological bimodule isomorphism

    R tensorhat_S^L R ~= S_x tensorhat S_z tensorhat S_y [0].

On elementary tensors the map is

    (u tensor v) tensor_S (w tensor t) -> u tensor vw tensor t.

Its inverse sends u tensor h tensor t to
(u tensor h) tensor_S (1 tensor t). These maps respect balancing and
are continuous; the free one-sided bar contraction ensures no additional
higher derived terms. Operator convolution is a further map

    mu: S_x tensorhat S_z tensorhat S_y -> S_x tensorhat S_y,
    mu(u tensor h tensor t)=(integral_Y h dz) u tensor t.

It is continuous and split onto, with section
u tensor t -> u tensor (1/a) tensor t. Its kernel is exactly

    S tensorhat ker(integral_Y) tensorhat S,

a closed, nonzero summand. Indeed S=C(1/a) direct-sum ker(integral_Y)
as a topological vector space. Thus convolution is not an isomorphism
from the source tensor product to R. This precisely distinguishes a
representation followed by scalar integration from source composition;
no monoidal equivalence is inferred from the operator action.

More generally the n-fold source tensor of R, n>=1, is S^tensorhat(n+1).
Its outer variables give the bimodule structure and its n-1 middle
variables are retained. Applying the same bar contraction with these
middle factors as passive coefficients yields

    HH_*^completed(S,R tensorhat_S^L ... tensorhat_S^L R)
          ~= S^tensorhat(n)[0].

All these identifications are continuous and associative under the
canonical reassociation of completed tensor products. They exhibit the
information retained before the n middle integrations used by scalar
operator traces.

For smooth kernels K_1,...,K_n the resulting source shadow element is
represented by the function on the cyclic variables

    (x_1,...,x_n) -> product_(i=1)^n K_i(x_i,x_(i+1)),
    x_(n+1)=x_1.

Rotating the tensor factors corresponds to rotating these variables; the
canonical cyclic comparison is an isomorphism between these shadow
coordinates, not pointwise equality after forgetting their labels.
Integrating all n variables gives

    tr(K_1 ... K_n)
       =integral_(Y^n) product_i K_i(x_i,x_(i+1)) product_i dx_i.

Smooth Fourier summability on the compact group justifies every integral
and reordering. Invariance of this integral under cyclic variable
permutation recovers operator trace cyclicity from the source comparison.
For n=1 it is exactly the earlier diagonal formula. This is an all-degree
local relative shadow computation for the tensor powers of the actual
outer free kernel bimodule, with its scalar comparison; it does not yet
supply an arithmetic determinant, a contravariant derived dagger, or the
comparison with the intrinsic ruling metric.

## Closure test for perfect kernels and the bounded continuous dual

The source tensor calculation above decides two concrete candidate
constructions for the still missing dagger. Set B=S tensorhat S, the
outer coefficient algebra. The kernel R is B itself, hence is perfect
as a B-module. Its composite R tensorhat_S^L R is B tensorhat S, with
the last S here denoting the middle-variable vector space. This composite
is not a perfect B-module in the finite-projective sense.

Indeed choose an outer point (x,y) and its continuous character B -> C.
Derived extension of scalars of B tensorhat S gives S in degree zero:
the module is relatively free and its base change is the underlying S.
If it were represented by a bounded complex of finite projective
B-modules, the same base change would be a bounded complex of finite
 dimensional vector spaces. Its cohomology would be finite dimensional,
contrary to the infinitely many independent Fourier characters in S.
This argument takes place in the split exact structure used for the
source derived tensors; it does not assume flatness of point evaluation.
Thus restricting to perfect B-kernels does not produce a composition-
closed category containing this outer free mixed kernel. This is a
specific local obstruction, not a claim that every notion of nuclear
perfectness or geometric proper pushforward fails.

There is also a topology issue in replacing finite-projective duals by
all continuous duals equipped with the strong topology. Although the
bidual identification proved above is valid, the evaluation

    S'_strong x S -> C

is not jointly continuous. A direct Fourier proof is useful. If it were,
there would be a bounded B_0 subset S, an integer m, and positive epsilon,
delta such that |T(f)|<=1 whenever p_(B_0)(T)<epsilon and rho_m(f)<delta.
Finitely many strong seminorm conditions can be combined into one bounded
set, and finitely many rho conditions into one rho_m. Boundedness gives

    sup_(g in B_0)|g_hat(i)| <= C W_i^-(m+1)

with C>0. Put epsilon_i(f)=f_hat(i) and choose

    T_i=(epsilon/(2C)) W_i^(m+1) epsilon_i,
    f_i=(delta/2) W_i^-m e_i.

Both neighborhood conditions hold, while
|T_i(f_i)|=(epsilon delta/(4C)) W_i is unbounded. The weights have an
unbounded sequence already on the trivial-unit real characters. This
contradiction proves the claim without a dual-space topology theorem.

Consequently strong biduality alone does not give a continuous evaluation
map S'_strong tensorhat_pi S -> C. In particular it cannot by itself
supply a duality compatible with the completed projective tensor products
used in the source bars. The earlier continuous transposition of each
fixed map is unaffected; joint evaluation is a different assertion.

The same problem occurs for the natural bounded-convergence B-linear
Hom dual of B tensorhat S. Functionals T on S embed continuously by
b tensor f -> b T(f). Restricting its putative jointly continuous module
evaluation to this embedded strong dual, then evaluating the outer
coefficient at (x,y), would give the forbidden scalar evaluation above.
Hence this particular internal-Hom topology cannot repair the perfect-
kernel closure failure. These statements concern these specified
constructions; they are not an impossibility theorem for A.4.

## A finite derived middle factor with an explicit duality

There is a constructive alternative at the level of the actual tangential
complex, rather than the raw middle coefficient space. This section uses
P123.103 and P123.119 with their original normalization. Use cohomological
degrees and put

    Omega=(S --D--> S dt),     degrees 0,1.

Its multiplication is the usual graded product, with dt squared zero.
The Fourier projection P_0 and Green map G satisfy DG=GD=1-P_0, with
continuous finite-loss estimates. The frequency-zero algebra K_0 has
finite dimension r, as proved in P123.119. Let

    H=K_0 tensor Lambda(dt),   with zero differential.

Inclusion i:H -> Omega is a morphism of differential graded algebras:
frequency-zero functions form a subalgebra, D vanishes on them, and dt
has square zero. Projection p=P_0 in both degrees is a continuous chain
map with p i=1; the homotopy G from degree one to degree zero satisfies

    d G+G d=1-i p.

No multiplicativity of p is claimed or needed. Thus Omega is explicitly
homotopy equivalent, as a complex, to a finite-dimensional complex.

The orientation trace is the continuous chain map

    t:Omega -> C[-1],   t(f dt)=integral_Y f dx,

zero on degree zero. It is a chain map since the integral of Df vanishes,
by the Fourier zero-mode formula. The pairing (alpha,beta)->t(alpha beta)
is jointly continuous and graded symmetric, with total degree one.
To check its derived nondegeneracy, let e_1,...,e_r be the characteristic
idempotents of the r cosets defining K_0. Each coset has Haar mass a/r,
so on H

    t(e_i e_j dt)=(a/r) delta_ij.

This is a perfect pairing between H^0 and H^1. Its matrix inverse is
(r/a) delta_ij, and all other homogeneous pairings vanish for degree
reasons. Thus on finite complexes it identifies H with H^vee[-1].

This extends to a homotopy equivalence Omega -> Omega'_strong[-1]
induced by the same pairing. Here the dual differential has the standard
Hom-complex signs. To justify the topology and equivalence, the pairing
map into the strong dual is continuous by the multiplication seminorm
estimates and boundedness of the second argument. Transposing i,p,G
gives a continuous contraction of the strong dual complex to H^vee,
since transposition of each continuous map is continuous in that topology.
The induced map on these finite retracts is precisely the invertible
matrix above. A chain map between these split finite retracts inducing
this isomorphism is a homotopy equivalence: after the contractions, its
restriction is the finite isomorphism, while all complementary complexes
are contractible. No jointly continuous evaluation on arbitrary
S'_strong x S is used. The jointly continuous pairing here is instead
between the two copies of the specific smooth complex Omega.

The same argument works relatively over the outer algebra B. The complex

    M_dR=B tensorhat Omega

is B-linearly homotopy equivalent to

    B tensor H = B^r[0] direct_sum B^r[-1],

where B^r[-1] denotes the term in cohomological degree one. It is therefore
perfect over B, with an explicit B-linear homotopy, and it has the
relative perfect derived pairing obtained from t by multiplication of
outer coefficients. This is a genuine finite derived duality for the
middle tangential complex on the same boundary.

For multiple independent middle variables, tensor the contractions.
The tensor of homotopy equivalences gives Omega^tensorhat(n) homotopy
equivalent to H^tensor(n); a contraction is obtained successively from
the individual contractions and projections with the usual graded tensor
signs. Only finitely many factors occur, so every map is continuous. The
orientation map is the tensor of the original traces t, and Fubini and
Koszul signs give its compatibility with reassociation and permutation
of the middle variables. Thus these candidate relative integrations are
coherent before any arithmetic comparison is asserted.

This does not identify M_dR with the previous source composite B tensor S
in degree zero: their cohomology is different, and there is no such
quasi-isomorphism. Adding the tangential differential is substantive
geometric input. The remaining task is to prove that a specified source
pushforward is computed by this relative complex and that its dualizing
normalization and determinant agree with the arithmetic category. The
finite derived pairing just constructed cannot be substituted for that
missing identification, but it supplies explicit maps and coherent
normalizations for a candidate that avoids the raw-factor obstruction.

## Geometric realization on the existing compact boundary

The tangential complex has a sheaf-theoretic realization on the same Y,
with an explicitly specified coefficient sheaf. It is not necessary to
postulate its global sections as a pushforward. The distinction between
this sheaf and the arithmetic coefficient sheaf is kept explicit below.

For a clopen subset V of U=Z_p^*, let S_U(V) consist of functions whose
extension by zero to U has Fourier seminorms

    sigma_N(f)=sum_kappa |f_hat(kappa)| c(kappa)^N < infinity

for every N. Multiplication by a clopen characteristic function is
continuous: that function has finitely many Fourier characters, and
conductor weights are submultiplicative. Thus restrictions and extension
by zero between clopen sets are continuous. Translations by units are
continuous and preserve these estimates.

Use flow boxes I x V in Y, with I an interval shorter than the period
and V clopen in U. Define a sheaf A^0 locally by smooth maps
I -> S_U(V), with seminorms on compact subintervals given by all real
derivatives and all sigma_N. On general opens impose this condition
locally. This is a sheaf: on each smaller compact flow box a gluing
problem reduces to finitely many subboxes and a finite partition by
smooth real functions and clopen unit functions. The resulting local
seminorms are controlled by finitely many seminorms of the pieces.
Flow-box transitions are real translations and multiplication by powers
of q on units, so they preserve the condition. Set A^1=A^0 dt.
The derivative D gives a sheaf map of complex vector spaces A^0 -> A^1.

Its global section space is exactly S(Y) from P123.101, with its declared
topology. In one direction, the weighted Fourier series controls every
local derivative/unit seminorm. Conversely choose a finite flow-box
partition of unity and lift its pieces to R x U with compact real
support. Real integration by parts with two extra derivatives controls
the summation over each twisted frequency lattice uniformly in kappa;
unit seminorms control the conductor summation. Summing the finitely many
pieces gives every rho_m bound. This is the local-to-global version of
the estimates in P123.120, not an enlargement to all leafwise smooth
continuous functions.

Let L=ker(D:A^0 -> A^1). Its sections are locally constant in the real
coordinate, with the specified rapid transverse regularity. It is a
sheaf of complex algebras. There is an exact sequence of sheaves

    0 -> L -> A^0 --D--> A^1 -> 0.

For surjectivity on stalks, shrink to a flow box and integrate a given
coefficient from a fixed t_0 in its real interval. Integration is
continuous for every sigma_N; derivative seminorms of positive order
reduce to those of the integrand. This supplies a local primitive and
proves exactness directly, without a global solvability assumption.

Both A^0 and A^1 are fine. Indeed Y is compact metrizable, hence
paracompact Hausdorff. Any open cover has a finite refinement by flow
boxes with smaller boxes still covering Y. Smooth real bump functions
times clopen unit characteristic functions give a subordinate partition
of unity after dividing their sum. The sum is positive and at a common
finite unit level, so its reciprocal is smooth at that same finite
level. Multiplication by the partition functions preserves both sheaves
and has support inside the prescribed opens. This verifies the fine
sheaf hypotheses on this particular transverse completion.

We use the standard fine-sheaf acyclicity theorem on paracompact Hausdorff
spaces; a primary course statement with these hypotheses is Gustavo
Granja, "Flabby, soft and fine sheaves", Instituto Superior Tecnico,
7 November 2012:
https://fenix.tecnico.ulisboa.pt/disciplinas/TH/2012-2013/1-semestre/ver-post/flabby-soft-and-fine-sheaves
The imported assertion is only that fine sheaves are acyclic, so an
exact fine resolution computes derived global sections. All local
regularity, exactness and partition hypotheses were checked above.

For pi:Y -> point, this proves in the derived category of complex sheaves

    R pi_* L ~= [S(Y) --D--> S(Y) dt] ~= H.

The first comparison is supplied by the displayed acyclic resolution;
the second has the explicit continuous contraction already constructed.
The sheaf-derived assertion is about underlying complex vector spaces.
The topology on its displayed global model and the continuity of its
finite retraction are separately specified; no general topological
injective-resolution formalism is presumed. Compactness also identifies
pi_! with pi_* in this instance.

This gives an actual geometric realization of the finite tangential
complex, its orientation trace and its derived pairing on the boundary.
It does not identify L with the original sheaf A^0 or with the integral
arithmetic coefficients: D is a derivation and is not A^0-linear. For
example D(1)=0 while D(e_i)=i tau_i e_i need not vanish. Therefore the
resolution is L-linear, not a resolution by A^0-modules of A^0 itself.
The arithmetic extension must construct a compatible flat/derived
coefficient comparison to L and verify its behavior across other strata;
that comparison is not supplied by the equality of global section spaces
A^0(Y)=S(Y). No full arithmetic pushforward or row A closure is inferred.

## Coefficient comparison by tangential connections

There is a precise local bridge between the preceding sheaf L and smooth
coefficient bundles. Let V be a finite-rank locally free A^0-module with
a tangential connection nabla satisfying

    nabla(f v)=Df v+f nabla(v).

There is only one tangential direction, so its curvature as a tangential
two-form vanishes. In a local frame nabla=D+A(t,u), with a matrix A of
sections of A^0. Solve

    D P=-A P,                 P(t_0,u)=identity.

This equation has a solution with exactly the transverse regularity
specified above. On a compact subinterval use the iterated-integral
Picard series in each matrix Fourier Banach norm sigma_N. If the norm
of A is bounded by M_N there, its k-th term is bounded by
(M_N |t-t_0|)^k/k!. Thus the series converges for every N, consistently
under the inclusions of these spaces. Differentiating the equation
controls every real derivative. Solving D Q=Q A with the same identity
initial value gives QP=PQ=identity by differentiation and uniqueness.
Therefore P is an invertible matrix of A^0 sections, not merely a
pointwise continuous fundamental solution.

In this frame, horizontal sections are exactly P(t,u)c(u), where c is
in S_U(V)^rank and is independent of t. Consequently

    Hor(V,nabla)=ker(nabla)

is a locally free finite-rank L-module, and multiplication gives an
isomorphism

    A^0 tensor_L Hor(V,nabla) -> V.

Conversely a locally free finite-rank L-module extends to A^0 and has
the connection D on the first factor. Its transition matrices are
horizontal, so these local connections agree. These constructions are
inverse equivalences between locally free finite-rank L-modules and
locally free finite-rank A^0-modules equipped with a tangential connection,
using horizontal maps on the latter side. All local solution and change-
of-frame maps preserve the declared regularity.

The comparison has explicit tensor and dual formulas:

    nabla_(V tensor W)=nabla_V tensor 1+1 tensor nabla_W,
    nabla_(V^vee)=D-A^t  in a dual frame,
    nabla_det(V)=D+Tr(A).

The first follows from Leibniz, the second from differentiating the
scalar evaluation, and the third by differentiating a wedge of a frame.
If v=g v' changes frames, the new matrix is

    A'=g^-1 A g+g^-1 Dg.

The fundamental solution then transforms by g(t)^-1 P(t)g(t_0).
This proves the change-of-frame and triple-overlap compatibility, rather
than choosing an unrelated connection in each chart. Horizontal maps,
tensor products, duals and determinant lines are carried to their
corresponding L-module operations.

The local horizontal resolution is also explicit:

    0 -> Hor(V,nabla) -> V --nabla--> V dt -> 0.

Surjectivity follows by writing v=P w and integrating D w=P^-1 f.
The sheaves V and V dt are fine by multiplication with the same scalar
partition of unity used above. Thus their global two-term complex
computes R Gamma(Y,Hor(V,nabla)). This extends the geometric realization
from the trivial connection to specified finite-rank coefficient
connections. It does NOT assert that the resulting global cohomology is
finite dimensional or Hausdorff for every A: the explicit Green estimate
previously used was for D, and does not automatically extend to D+A.

At the global algebra level every displayed finite projective module
P=e S^n admits a connection e D on its sections: e D(fv)=Df v+f e Dv.
This is an existence construction tied to the idempotent presentation;
it is not invariant under all module isomorphisms without transforming
the connection. Two connections on the same module differ by an S-linear
endomorphism. The chosen connection is therefore additional coefficient
data, not an automatic functor on the category with all S-linear maps.

This last distinction is unavoidable even in rank one. For any connection
on S, multiplication by f is horizontal precisely when

    [nabla,M_f]=M_(Df)=0.

There are characters with Df nonzero. Hence there cannot be a lift of the
entire rank-one endomorphism algebra to horizontal maps while preserving
its underlying multiplication action. This does not invalidate the
constructed equivalence of connection-equipped coefficients; it specifies
which morphisms that equivalence contains.

The remaining arithmetic task is now concrete: identify the source
objects with their compatible tangential connections, identify the
horizontal morphisms needed for correspondences, and prove the global
finiteness and metric comparison on that domain. Choosing a connection
independently for each object would not establish those requirements.

## Global finiteness for a tensor- and dual-stable connection domain

A nontrivial class of the connection coefficients above admits a complete
Fourier finiteness proof. This specifies a domain; it does not claim that
all arithmetic coefficients already lie in it. Put tau_0=2 pi/a and let

    Q_adm={alpha+i tau_0 b : alpha real, b rational}.

For a finite-dimensional complex space V and an endomorphism A with
spectrum in Q_adm, consider the global trivial bundle with connection
D+A. Arbitrary Jordan blocks are allowed. The class is closed under
direct sums, tensor connections A tensor 1+1 tensor B, and dual
connections -A^t: the eigenvalues respectively unite, add, and negate.
These are conditions on connection coefficients, without zeta or sign
input.

The complex C_A=[S tensor V --(D+A)--> S tensor V dt] has an explicit
finite deformation retract. For a character chi, its Fourier block is

    T_chi=i tau_chi+A.

Decompose V into generalized eigenspaces V_lambda, writing A=lambda+N
there, with N nilpotent. Call (chi,lambda) resonant when
 i tau_chi+lambda=0. For each fixed lambda there are at most r resonant
characters: if two have the same real frequency, their quotient has
frequency zero, and the zero-frequency character group has cardinality
r=dim K_0. Thus the total resonant space

    E_A=direct_sum_(resonant chi,lambda) C chi tensor V_lambda

is finite dimensional. On E_A the differential is N, not necessarily
zero. Let P_A be its finite Fourier/generalized-eigenspace projection.
It commutes with D+A.

Off resonance the inverse blocks satisfy a uniform polynomial weight
bound. If Re(lambda) is nonzero, |i tau+lambda|>=|Re(lambda)|. Otherwise
write lambda=i tau_0 b with b rational of denominator d. Since
exp(i tau a) kappa(q)=1, tau/tau_0 is rational with denominator dividing
the order of kappa(q), which is at most |U/N_n|<=c(kappa) for a character
of conductor c(kappa)=p^n (the trivial character has order one).
Consequently, whenever tau/tau_0+b is nonzero,

    |i tau+lambda|>=tau_0/(d c(kappa)).

On a Jordan block of size at most s the inverse is the finite sum

    (z+N)^-1=sum_(j=0)^(s-1) (-N)^j z^-(j+1).

For fixed A, these estimates give ||T_chi^-1||<=C_A W(chi)^s off the
resonant generalized eigenspaces. Define G_A by these inverses off
resonance and zero on E_A. Then, for all m,

    rho_m(G_A f)<=C_A rho_(m+s)(f),
    (D+A)G_A=G_A(D+A)=1-P_A.

Here the seminorms include any fixed norm on V. Thus G_A is a continuous
homotopy from degree one to degree zero, and inclusion/projection give

    C_A ~= [E_A --N--> E_A dt].

This is a finite complex with its actual nilpotent differential. It
proves finite-dimensional cohomology, closed boundary image, and a finite
perfect model, including the nonsemisimple case. For a nonresonant A the
complex is continuously contractible. No estimate uniform over an
unbounded family of rational denominators or over changing A is claimed.

Horizontal maps between two such coefficients form finite-dimensional
spaces. Their Fourier coefficients F_chi satisfy

    (i tau_chi+B)F_chi-F_chi A=0.

Apply the same reasoning to the endomorphism F -> BF-FA of Hom(V,W).
Its spectrum consists of differences of admissible eigenvalues, so it
again lies in Q_adm. Its horizontal kernel is therefore finite dimensional
and consists of finitely many Fourier modes, with the nilpotent
intertwining conditions retained. This also proves closure and the
continuity of composition on these horizontal Hom spaces.

The orientation pairing with the dual connection remains perfect in the
derived sense. Fourier orthogonality pairs chi with chi^-1 and V_lambda
with the dual generalized eigenspace for -lambda. On finite retracts,
the two nilpotent differentials are transpose with the dual-complex sign,
and the Haar pairing has nonzero scalar a. The resulting pairing

    C_A tensor C_(-A^t) -> C[-1]

is therefore a perfect pairing of the finite complexes. The continuous
Green homotopies identify this finite comparison with the original
smooth global complexes. This proves global derived duality for this
specified connection domain, not only for the trivial coefficient.

Finite bounded complexes of these coefficients with horizontal
differentials also have finite global models. Apply the individual
contractions columnwise to the two-row de Rham double complex. Transfer
the horizontal differential using the finite perturbation expansion;
each extra factor moves to the next column, so boundedness makes the
expansion finite. All its terms are composites of the continuous maps
just constructed. Hence cones and bounded totalizations have continuous
finite models without an infinite-series convergence assumption.

The resulting determinant lines are determinants of these finite models,
and duality is defined on them by the finite pairings. This establishes
finiteness and duality on an explicit tensor-stable local coefficient
category. It does not determine a Hermitian metric on those lines or
prove their equality with the intrinsic periodic ruling determinant.
Likewise it does not show that every required arithmetic correspondence
has admissible connection spectrum. Those are separate comparison
requirements for the full row A, not consequences of finiteness here.

## Connection-compatible Morita transport back to the source

The connection comparison can be transported to the actual smooth source
algebra, with explicit formulas that account for the nonconstant cutoff.
Retain J=J_sm, its continuous real derivation D, and the smooth full
idempotent e of P123.120. Put S=eJe, P=Je and Q=eJ. The corner derivation
is

    delta_e(b)=e D(b)e,       b in eJe.

It is a derivation: differentiate b=ebe and use eD(e)e=0, obtained by
differentiating e squared=e. Equivalently, inserting e between the terms
of D(bc) proves delta_e(bc)=delta_e(b)c+b delta_e(c).
Under the actual corner map f -> f e from P123.120, it is the original
tangential derivative, since e D(fe)e=(Df)e. Define connections

    nabla_P(p)=D(p)e,         nabla_Q(q)=e D(q).

These are continuous by the source derivative and multiplication
estimates. They satisfy both module Leibniz rules for (J,D) and
(S,delta_e). For example

    nabla_P(ap)=D(a)p+a nabla_P(p),
    nabla_P(pb)=nabla_P(p)b+p delta_e(b).

The other two identities follow in the same way. No assumption D(e)=0
has been made.

Both Morita evaluations from P123.120 are horizontal. For p in P and
q in Q,

    nabla_P(p)q+p nabla_Q(q)=D(pq),
    nabla_Q(q)p+q nabla_P(p)=e D(qp)e.

Thus multiplication identifies the tensor connections on P tensor_S Q
and Q tensor_J P with D on J and delta_e on S, respectively. Since the
underlying maps are continuous isomorphisms, their inverses are horizontal
as well; a new differentiation estimate for the inverse frame sums is
not needed.

A bimodule connection here means a continuous linear map obeying the
Leibniz rules on both sides. On the completed balanced tensor of two
such bimodules use the sum of their connections. Leibniz makes this
well-defined on the balancing relations, and continuity extends it to
the completed quotient. Consequently the actual functors

    L(M)=P tensorhat_S M tensorhat_S Q,
    R(N)=Q tensorhat_J N tensorhat_J P

carry these connections and horizontal morphisms to each other. The
horizontal evaluations just proved show that they are mutually inverse
on the unital S and firm J domains of P123.120. Their monoidal and unit
comparisons are horizontal, and all coherence diagrams follow from the
same multiplication maps as in the unadorned source category. This is
an equivalence of the declared categories with connections; no passage
to an undeclared derived exact structure is being assumed.

The transport is independent of a smooth cutoff in the appropriate
coherent sense. For another smooth full idempotent f, the comparison
bimodule eJf has connection

    nabla_(e,f)(x)=e D(x)f.

The left and right derivations are delta_e and delta_f. For a third
cutoff g, multiplication eJf tensor_(fJf) fJg -> eJg is horizontal:

    (e D(x)f)y+x(f D(y)g)=e D(xy)g.

Its underlying isomorphism follows by composing the full-corner Morita
contexts. These comparisons associate on triple products, have the
correct units on eJe, and their inverse comparisons are horizontal.
Matrix cutoffs obey the identical calculation with entrywise D. Hence
the connection transport includes smooth changes of corner presentation,
rather than selecting incompatible Grassmann connections in each frame.

In particular a right S-module with a specified admissible connection
can be transported to its actual right J-module via tensoring with Q,
and recovered via P. The induced total connection is part of this
transport. One must not compute its cohomology by taking the naive
underlying vector-space complex of the resulting J-module: global
pushforward is the corner/sheaf comparison already constructed, not
forgetting the J action. Under that comparison the finite models and
determinant lines above now apply to actual source modules on this
boundary, coherently under cutoff changes.

This supplies a connection-compatible source bridge on the single-zero
boundary. It neither extends J over all arithmetic strata nor asserts
that arbitrary source maps are horizontal. The full derived dagger,
semilocal arithmetic descent and intrinsic determinant metric comparison
remain outside the result just proved.

## Common semilocal derivation and horizontal localized composition

The connection structure extends to the common source of P123.121, not
just its compact corner. On A_P=A_sm^u(P) define

    D(sum_gamma f_gamma U_gamma)
          =sum_gamma (partial_t f_gamma) U_gamma,
    D(1)=0.

Its continuity follows directly from the real derivative seminorms in
P123.121: each requested derivative order is increased by one, with the
same finite-place and rapid lattice weights. Every lattice action is a
translation in t combined with finite-place dilations, so D commutes
with it. The crossed-product formula consequently gives the Leibniz
rule, and D commutes with the source involution.

Each zero-evaluation and its splitting f -> chi_p ev_(0,p)(f) commutes
with D, because it acts only on a finite-place variable. Thus D preserves
all the zero-stratification ideals, their finite sums and intersections,
and their closed quotients. It preserves every localized ideal I_J of
P123.124 and induces a derivation on each quotient of P123.125. This
retains the nonzero finite-place attaching corrections of P123.121;
none has been set to zero by passing to D.

The actual semilocal maps are horizontal:

    D j_(P,T)=j_(P,T) D.

Indeed j multiplies by new chi_ell factors, all independent of t, and
keeps the old lattice labels. The coefficient-unitization maps are also
horizontal because D kills their scalar unit. The previously proved
triple-transition identity is therefore an identity of differential
algebras as well as of topological algebras.

On a localized twisted bimodule I_J,beta, equip the underlying ideal
with the connection D, where beta is one of the external automorphisms
commuting with real translation. The right Leibniz rule follows from
D beta=beta D. The composition isomorphism of P123.124 is horizontal:

    I_J,beta tensor_A^L I_K,eta -> I_(J union K),beta eta,
    u tensor v -> u beta(v),

since D(u beta(v))=D(u) beta(v)+u beta(Dv). The inverse of the underlying
topological isomorphism is then horizontal automatically. Units,
associativity and the allowed external translations preserve these
connections. This extends the connection structure over the already
constructed localized graph sector on the common source.

For a zero-stratum quotient A/I_O, its finite Cech resolution from
P123.125 consists of these localized ideals and A with alternating
inclusion maps. All its maps are horizontal. Its underlying contraction
uses the finite zero-coordinate projections, which also commute with
D. Consequently the resolution retains its admissibility together with
a compatible connection. The multiplication comparison

    (A/I_O) tensor_A^L (A/I_O) -> A/I_O

is horizontal on this model. This statement concerns the actual closed
quotient maps; it does not replace the noninvertible semilocal induction
map disproved in P123.123.

Finally the equivariant repair of P123.123 also carries connections.
Let C be its coefficient-enlarged old-lattice algebra, G the added
lattice, and M a tempered equivariant C-bimodule with connection nabla
such that nabla rho_g=rho_g nabla. On M crossed_rapid G set

    nabla_cross(sum_g m_g U_g)=sum_g nabla(m_g) U_g.

Continuity follows by increasing the coefficient seminorm in the rapid
sequence definition. Both crossed module Leibniz identities follow from
the commutations with rho_g and alpha_g. The monoidal comparison

    (m U_g) tensor(n U_h) -> (m tensor rho_g(n)) U_(g+h)

is horizontal by direct differentiation of the two factors. Its inverse,
unit and all reassociations are horizontal too. On the actual localized
ideals the required commuting action is rho_g=alpha_g, so this gives
specified examples, not an assertion that every old module has a new
lattice action. The derivative commutes with the equivariant bar faces
and with unit insertion, so the same compatibility holds on the explicit
underlying relative derived models of P123.123.

This constructs common-source connections compatible with semilocal
embeddings, localized composition, closed strata and the equivariant
composition repair. It does not assert a derived equivalence for an
unspecified exact category of horizontal morphisms. Nor does it prove
that every such localized coefficient has the finite tangential
pushforward calculated for the compact admissible corner. Global
arithmetic duality and the determinant metric still require those
comparisons; they cannot be inferred simply from D preserving ideals.

## The full noncompact real pushforward: explicit model on every stratum

The compact-boundary Green calculation must not be applied unchanged to
the common source. Its real coefficient E_R has decay at both ends.
There is a different, explicit continuous contraction for this space.
Choose rho in C_c^infinity(R) with integral one, and put

    I(f)=integral_R f(t) dt,
    H(f)(t)=integral_(-infinity)^t (f(s)-rho(s) I(f)) ds.

The integrand has integral zero, so outside the support of rho one may
use either tail integral. For l>=0 the estimate using r_(l+1,0)(f)
bounds exp(l|t|)|H(f)(t)| on both tails; on the remaining compact interval
it is bounded by the same seminorm times a constant depending on rho,l.
Higher derivatives follow from D H(f)=f-rho I(f). Thus H:E_R -> E_R
is continuous with finite seminorm loss. Also

    D H=1-rho I,             H D=1,             I D=0.

The second identity uses both decay endpoints and I(Df)=0. Therefore,
with cohomological degrees 0,1,

    [E_R --D--> E_R dt] ~= C[-1].

The projection is I in degree one, its section is rho dt, and H is the
homotopy. In particular the degree-zero kernel is zero, not the constant
functions of the compact boundary calculation.

Write F_P=tensorhat_(p in P) E_p and let

    V_P={sum_gamma v_gamma U_gamma:
          sum_gamma H(gamma)^k nu(v_gamma)<infinity
          for every k and every seminorm nu of F_P}.

For the nonunital common source A_sm(P), apply the preceding maps to its
real factor coefficientwise. The estimates extend to completed tensors
and to each rapid lattice seminorm, giving an explicit contraction

    [A_sm(P) --D--> A_sm(P) dt] ~= V_P[-1].

Every boundary is closed, with the continuous primitive just displayed.
This is an equality of explicitly topologized complexes of vector spaces;
integration is not asserted to be a homomorphism of crossed algebras.
The remaining finite-place variables and all lattice labels have been
retained. V_P is generally infinite dimensional, so this is not a finite
perfect scalar pushforward.

The same construction applies to every zero-stratum ideal, sum of ideals
and quotient from P123.124--125: their coefficientwise projections act
only on F_P and commute with I,H and multiplication by rho. Replace F_P
in the displayed formula by its corresponding finite-place subspace or
quotient. Thus these real pushforward models commute with the finite
Cech resolutions of zero-stratum quotients, including their connecting
maps. This proves a compatibility across the declared stratification,
not merely a separate dimension calculation on each stratum.

They also commute with the actual semilocal embeddings: the embedding
multiplies by new chi_ell and retains old labels, so I,H,rho all commute
with it. On the targets V_P the resulting map is precisely finite-place
multiplication by these chi_ell with the same label inclusion. Triple
compatibility is inherited without changing normalization.

Coefficient unitization has an additional term which must be kept.
Let L_P be the rapid scalar lattice space. As vector spaces the unitized
source is A_sm(P) direct_sum L_P, and D vanishes on L_P. Its complex
therefore has model

    L_P[0] direct_sum (V_P direct_sum L_P)[-1].

In particular the scalar lattice sector survives in BOTH cohomological
degrees. It is not removed by the compactly supported real primitive.
The decomposition is used only as a vector-space splitting, not as a
product decomposition of algebras.

Finally I is invariant under real translations, but the chosen section
rho need not be. This dependence is explicitly homotopic. For another
rho' of integral one, the function

    eta(t)=integral_(-infinity)^t (rho'(s)-rho(s)) ds

is smooth and compactly supported, and D eta=rho'-rho. Multiplication by
eta gives the chain homotopy between the two degree-one sections, also
with arbitrary finite-place and rapid-label coefficients. For a fixed
real translation take rho' to be the translate of rho. Thus the
pushforward projection is canonical with this Haar normalization while
its auxiliary splitting has a controlled homotopy dependence. No
translation-invariant compactly supported cutoff is assumed.

This constructs the common-source real integration and its compatibility
with semilocal maps and zero strata. It also identifies precisely why
compact-boundary finiteness cannot simply be transported by forgetting
module structure: before the geometric quotient/pushforward comparison,
the finite-place and lattice coefficients V_P remain. The required
arithmetic descent of this residual target, its duality and its metric
are still separate requirements for row A.

## Completed deck descent of the noncompact tangential complex

The residual transverse space can be descended explicitly for the
remaining q-deck action in the actual boundary presentation
Y=(R x U)/((t,u)~(t+a,q u)). This is a descent theorem on that presentation,
not a claim about the entire semilocal lattice on every stratum.

Put E=E_R tensorhat S_U(U), with rapidly decreasing real coefficients
and all transverse conductor weights, and let

    (T f)(t,u)=f(t-a,q^-1 u),
    P f=sum_(n in Z) T^n f.

The periodized function is T-invariant. Its series and all real-derivative
and transverse seminorm series converge uniformly on compact real
intervals by the real exponential decay; unit translations preserve the
transverse seminorms. The twisted Fourier estimates of P123.120 identify
its target as S(Y), with continuous map P:E -> S(Y).

Choose c in C_c^infinity(R) with sum_n c(t-na)=1. Then
j(F)(t,u)=c(t)F(t,u) defines a continuous section of P, so P is onto.
The kernel has an explicit difference primitive. If P f=0, put

    Q f=sum_(n>=0) T^n f = -sum_(n<0) T^n f.

The first series controls the negative real tail and the second controls
the positive tail. For each exponential real weight and each transverse
seminorm, a one-step increase of the real decay weight bounds the tails
by a geometric series. Derivatives obey the same estimates. Thus Q is
continuous from ker(P) into E and (1-T)Q f=f. Conversely a T-invariant
element of E is zero by decay along its deck orbit. Consequently

    0 -> E --(1-T)--> E --P--> S(Y) -> 0

is exact with closed image and continuous underlying splittings. This
is an actual completed quotient computation; it does not infer exactness
from density of compactly supported functions.

All the maps in this sequence except the auxiliary cutoff section
commute with D. Form the two-term deck Koszul complex with its first E
in cohomological degree -1 and its second E in degree zero, then tensor
it with the two-term tangential de Rham differential. Give the total
complex the usual sign so its differential squares to zero. Periodization
induces a continuous quasi-isomorphism of this total complex onto

    [S(Y) --D--> S(Y) dt].

It is a continuous chain homotopy equivalence: contract the split deck
sequence in each de Rham degree and transfer D. The perturbation
expansion is finite since there are only two de Rham degrees. This
argument handles D(c) explicitly through the transferred homotopy; it
does not assume that the cutoff section is horizontal. The claim is
about this specified completed deck complex, not an unproved derived
coinvariant functor for an arbitrary rapid group algebra.

There is a second computation of the same total complex which directly
connects to the noncompact real integration above. The map

    I:E -> S_U(U),            I(f)(u)=integral_R f(t,u) dt

satisfies I T=T_U I, where T_U h(u)=h(q^-1 u). Apply the real contraction
already proved, columnwise in the deck complex. Its perturbation
expansion is again finite, now by the two deck degrees. The total
complex is therefore homotopy equivalent to

    [S_U(U) --(1-T_U)--> S_U(U)],   degrees 0,1,

up to the harmless overall sign of the differential from totalization.
Thus real integration first and deck descent first give the same
completed cohomology, with explicit continuous comparison models.

This remaining difference complex has finite cohomology. On kappa the
multiplier is 1-kappa(q)^-1. When it is nonzero, its inverse has absolute
value bounded by C c(kappa): a nontrivial root of unity of order m has
distance at least 4/m from 1, and m<=c(kappa). Set the inverse to zero on
the invariant characters. It defines a continuous Green operator with
one conductor-weight loss. The invariant space is exactly K_0, the
finite space of functions on U/closure(q^Z) from P123.119. Hence both
kernel and cokernel are K_0, all boundaries are closed, and the resulting
finite model is K_0 in degrees zero and one.

This proves directly how the infinite transverse residual of real
integration becomes finite after the specified geometric deck descent.
It recovers the compact-boundary result from the noncompact coefficient
complex, without dropping transverse coefficients or lattice action.
It remains local to the displayed boundary quotient: extension to all
semilocal strata, source correspondence duality and the intrinsic metric
comparison are not consequences of this one deck computation.

## Coefficient deck descent for every semilocal zero stratum

Fix a finite prime set P and an exact zero set Z subset P. Write
N=P minus Z, k=|Z|, and U_N=product_(p in N) Z_p^*. The coefficient
space of that stratum in P123.121 is

    C_Z=E_R tensorhat tensor_(p in N) F_p.

Consider its explicit commuting deck Koszul complex for Gamma_P,
with a wedge of j lattice generators in cohomological degree -j,
combined with the real de Rham degrees 0,1. This is a coefficient descent
complex. It is not being identified with the full Hochschild complex
of the crossed algebra, which also retains correspondence labels.

First eliminate the nonzero valuation directions without discarding
unit actions. On points write x_p=p^j_p u_p and set

    s=t-sum_(p in N) j_p log p,
    v_p=u_p product_(r in N, r!=p) r^(-j_r).

The generator p in N then shifts j_p by one and leaves s and every v_r
fixed. A generator q in Z leaves all j_p fixed and sends
(s,(v_p)) to (s+log q,(q v_p)). These assertions follow directly by
substitution in the original simultaneous real and finite scaling.
Using inverse pullbacks changes all shifts consistently and gives the
same complexes up to the corresponding generator convention.

This coordinate change is topological on the specified completions:
|t-s|<=sum |j_p| log p is absorbed by stronger exponential shell weights,
and all the unit changes act on Fourier coefficients by phases. Real
derivatives are unchanged. Thus C_Z becomes a rapidly decreasing
Z^N-sequence space with coefficients E_R tensorhat S(U_N), with the
independent shifts just described. Here S(U_N) uses all product conductor
weights in its absolutely summable Fourier seminorms.

For one shell direction the augmented shift complex has quotient given
by summing its sequence. On a sum-zero sequence, one-sided partial sums
solve the difference equation; use the opposite tail on the other end.
An increase of the exponential shell weight bounds both tails by a
geometric series. The section inserts the sequence at shell zero.
This proves a split continuous contraction, including with the remaining
coefficient seminorms. Applying it in all the N directions reduces the
complex to the deck complex for Z on E_R tensorhat S(U_N). These shell
contractions commute with D and the Z actions in the displayed
coordinates. They do not collapse any exterior degree from a zero
coordinate.

Apply real integration next. It commutes with all Z actions, and the
real contraction transfers through the finite deck complex by a finite
perturbation expansion. The resulting model is

    S(U_N) tensor Lambda^*(C^Z),
    degree of Lambda^j = 1-j,

with differential the Koszul contraction by the commuting operators
1-T_q, q in Z, where T_q f(v)=f(q^-1 v). This includes all derived
lattice directions and the degree-one real orientation shift.

If k>=1 this model has an explicit finite retract. To see finiteness,
choose q_0 in Z. For each p in N choose a positive integer m divisible
by the torsion exponent of Z_p^*, and by 2 at p=2, so q_0^m is in the
domain of the injective p-adic logarithm. Its logarithm is nonzero:
otherwise the positive rational number q_0 would be a root of unity.
Writing b_p=v_p(log_p(q_0^m)), the closure of its powers in that factor
is the open subgroup exp(p^b_p Z_p). The closure simultaneously contains

    product_(p in N) exp(p^b_p Z_p).

Indeed ordinary integers are dense in product_(p in N) Z_p by the
Chinese remainder theorem, so the common exponent can approximate each
p-adic exponent independently. Consequently closure(q_0^Z) is open in
U_N and has finite index. This argument uses distinct residue primes;
it does not incorrectly impose a real-dimensional rank bound on the
product of different p-adic factors.

On a unit character kappa, the q_0 difference multiplier is
1-kappa(q_0)^-1. If nonzero, its inverse is bounded by a constant times
product_p c(kappa_p): the order of kappa(q_0) is at most that product.
Thus the inverse has a finite conductor-weight loss. Its kernel consists
of finitely many characters by the open-subgroup calculation. Among
these finitely many, the other q actions can be diagonalized and every
character not fixed by all q is contracted using one nonzero multiplier.
All these further bounds are finite constants.

More explicitly, on a character not invariant under every q, choose
q_0 when its multiplier is nonzero, otherwise the first nonzero q from
an ordering of Z. Wedge multiplication by that generator divided by its
multiplier contracts the Koszul differential: contraction followed by
wedge plus wedge followed by contraction is the scalar multiplier.
The preceding bound proves continuity of this homotopy. Project onto
jointly invariant characters and set the homotopy to zero there. This
gives the finite model

    K_Z tensor Lambda^*(C^Z),      degrees 1-j,
    K_Z=C(U_N / closure(<q : q in Z>)),

with zero differential. All boundary spaces are closed and

    dim H^(1-j) = dim(K_Z) binomial(k,j),   0<=j<=k.

When N is empty, U_N is a point and K_Z=C, so the same formula retains
all the zero-stratum exterior classes. When Z is empty there is no
unit-difference contraction: the answer is S(U_N)[-1], generally
infinite dimensional. These cases are not silently excluded.

The finite projection to joint invariants is independent of the
ordering used for the homotopy. Reordering deck generators acts by the
usual signed exterior permutation and gives the identical finite
cohomology model. The auxiliary contraction can change, but the
coefficient descent complex and its projection retain these comparison
maps. No compatibility of these stratumwise finite retracts with the
attaching extensions of different strata is claimed here: those
extensions retain the finite-place attaching corrections from P123.121.
Likewise this does not identify the coefficient deck complex with the
arithmetic shadow or give the intrinsic determinant metric. It supplies
the full coefficient-level derived calculation on each exact zero
stratum, with the open stratum and higher exterior degrees preserved.

## Gluing the closed zero locus without deleting attaching maps

The stratumwise finite models can be assembled on each closed locus F_k
of at least k zero coordinates, provided k>=1. This concerns the same
coefficient deck/de Rham complex as above, not the full crossed-algebra
shadow. Let T_k denote that complex on the actual restriction image of
the common coefficients on F_k. The finite linear coefficient splitting
from P123.121 identifies its graded vector space with the sum of the
stratum complexes for |Z|>=k. The splitting is not equivariant.
Accordingly its differential has the form

    d=d_0+delta,

where d_0 is the direct sum of the exact-stratum differentials and delta
strictly decreases the number of zero coordinates. This triangular
assertion follows directly from the finite tensor decomposition
E_p=C chi_p plus F_p: dilation preserves F_p and sends chi_p to chi_p
plus its displayed F_p correction. The real derivative preserves the
splitting. For the prime generators used in the Koszul differential,
the attaching correction at p is specifically

    (1-alpha_p)chi_p=1_(Z_p^*)

and the corrections at the other finite places vanish because p is a
unit there. Real translation of the accompanying real coefficient is
still part of alpha_p; it is not omitted from delta.

For each exact stratum choose a normalized continuous contraction onto
its finite model H_Z=K_Z tensor Lambda(C^Z), in degrees 1-j. Such a
normalization is available from the split contractions above: decompose
the contractible summand into boundaries and chosen continuous
preimages, and take the inverse differential on boundaries and zero
on preimages. With i,p,h denoting the direct sums, this gives

    p i=1,   d_0 h+h d_0=1-i p,   h i=p h=h squared=0.

All these maps preserve the zero-count grading. The operator h delta
strictly lowers that count and is nilpotent: on F_k its power r-k+1
vanishes, where r=|P|. Thus the following formulas are FINITE sums of
known continuous maps:

    I=(1+h delta)^-1 i,
    P=p (1+delta h)^-1,
    H=(1+h delta)^-1 h,
    d_eff=p delta (1+h delta)^-1 i.

The inverse notation means sum_j (-h delta)^j or sum_j (-delta h)^j,
truncated before power r-k+1. Direct substitution using d squared=0
and the displayed contraction identities yields

    d I=I d_eff,       P d=d_eff P,       P I=1,
    d H+H d=1-I P,     d_eff squared=0.

Equivalently these identities are the finite elimination of the
contractible blocks of d_0. They introduce no analytic convergence
hypothesis. Hence T_k has the finite perfect model

    (direct_sum_(|Z|>=k) H_Z, d_eff).

The first term of d_eff is p delta i, but in general the subsequent
terms -p delta h delta i and higher must be retained. The construction
does NOT replace the actual attaching differential by an unproved
incidence formula, nor treat the coefficient splitting as equivariant.
Every term is determined by the original shell corrections and the
explicit stratum primitives and projections.

The transfers preserve the zero-count filtration. Restriction from F_k
to F_(k+1) deletes the |Z|=k summands, and its finite-model map is the
same projection: a strictly lowering path cannot leave those summands
and return to a higher zero count. Thus the models give actual short
exact sequences of finite complexes for successive closed loci, with
the |Z|=k layer as kernel. The extension maps of these complexes contain
the transferred attaching terms. These statements follow from choosing
the stratum contractions once and using their restrictions for every k.
They do not assert naturality under arbitrary added-prime maps that
change the stratum decomposition.

It follows that each closed F_k, k>=1, has finite-dimensional coefficient
deck/de Rham cohomology with closed boundaries. Its determinant line is
now defined by this finite complex, and the successive-layer determinant
isomorphisms are those of the displayed finite short exact sequences.
They obey the usual reassociation identities already on exterior powers
of the finite chain spaces. This is a genuine gluing construction for
these determinant LINES. No Hermitian metric or arithmetic RR equality
has been inferred from the existence of those lines.

The Euler characteristic is zero: on a stratum with |Z|>=1 it is
minus dim(K_Z) times (1-1)^|Z|, and the finite triangular differential
does not change that alternating dimension. This does not make the
complex acyclic or its determinant metric trivial. Finally, including
the open stratum k=0 brings back its infinite S(U_P) term; the finite
perfect assertion above is not extended to that case. The full source
shadow comparison and the intrinsic mixed metric remain required for A.

## Full coefficient descent and its relative determinant

The open stratum can be included in the same transfer without truncating
its infinite coefficient space. Let V=S(U_P), and let F denote the finite
model of the closed locus F_1 just constructed. Use the explicit open
stratum contraction to V[-1] together with the closed-stratum contractions.
The attaching perturbation still strictly lowers the finite zero count,
so its transfer remains a finite sum of continuous maps. Thus the full
nonunitized coefficient deck/de Rham complex has a continuous homotopy
model M with underlying graded space

    M=V[-1] direct_sum F.

The open summand has zero differential and no outgoing attaching term.
Degree considerations therefore force the full differential to be

    d_M(v,f)=(a(f),d_F(f)),
    a:F^0 -> V,          a d_F|_(F^-1)=0.

Here a is the degree-one off-diagonal block of the same finite transfer
formula, including all higher attaching paths. It is not a freely chosen
map. Its domain is finite dimensional, so its image is finite dimensional
and closed in V. This establishes the actual continuous triangle

    V[-1] -> M -> F -> V[0].

It is the transferred triangle of restriction to the closed locus, not
a definition of a new substitute for the source coefficient complex.

Writing a_bar:H^0(F) -> V for the induced map, the cohomology is determined
by the finite exact sequence

    0 -> H^0(M) -> H^0(F) --a_bar--> V
      -> H^1(M) -> H^1(F) -> 0,

and H^n(M)=H^n(F) for n different from 0,1. In particular H^1(M) is an
extension of the finite-dimensional H^1(F) by V/im(a_bar). All ranges
of d_M are closed: apart from the zero open differential, the nonzero
maps have finite-dimensional domain. The continuous homotopy equivalence
then gives closed boundaries also in the original complex. For example,
if a source boundary sequence converges to x, apply the continuous
projection to M, use its closed boundary image there, and use the
homotopy identity to lift a primitive of x.

The quotient V/im(a_bar) is nuclear Frechet. Indeed V has those properties
by its weighted Fourier model, and quotient by a finite-dimensional
closed subspace preserves them. The remaining cohomology spaces are
finite dimensional, and their extensions here split continuously by
choosing lifts of a finite basis. This proves a separated topological
cohomology model for the entire coefficient descent complex, with its
infinite part retained explicitly. It does not equip that cohomology
with the arithmetic numerical intersection form.

There is now a relative determinant line supported by an actual finite
cone. If j denotes the inclusion of the open coefficient complex into
the full one, its cone is quasi-isomorphic to F. Define

    Det_rel(j)=det(F)
       =tensor_n (top exterior power F^n)^((-1)^n).

This definition takes the determinant of the finite cone; it does not
form a ratio of two nonexistent finite determinants of V[-1] and M.
The transferred restriction triangle identifies the line with that of
the original open-to-full map. Changing the continuous contraction
changes the finite model by its induced derived comparison, hence gives
the usual determinant identification through cohomology. The latter is
finite dimensional for this cone, even though H^1(M) is not.

Successive closed layers provide the finite short exact sequences already
constructed, and consequently the corresponding factorization of
Det_rel(j) into their determinant lines. The factorization retains the
attaching differential through the derived determinant comparison; it
does not assert that the layers are a direct sum of complexes.
No metric on Det_rel(j), principal-divisor invariance or comparison to
the intrinsic ruling line is claimed. Nor is j identified with a map of
the eventual arithmetic correspondence shadows. The result supplies
an actual relative finite determinant for the full coefficient descent
triangle, rather than imposing a scalar determinant on its infinite
open-stratum part.

## A continuous cyclic source trace into the descended coefficient target

The coefficient descent now gives a trace on the original nonunital
crossed algebra itself. This is a trace map, not yet a comparison of
entire derived shadow functors. Let E_P be the common coefficient algebra,
A=A_sm(P), and let T be the full coefficient deck/de Rham total complex
just constructed. Its top degree is one, and

    H^1(T)=E_P / (D E_P+sum_(p in P)(1-alpha_p)E_P).

Identify a coefficient with its degree-one dt term. The denominator is
the actual degree-one boundary image and is closed by the full-complex
calculation above. Thus this formula carries the separated quotient
topology, with a nuclear Frechet model; no additional closure that could
change the cohomology is inserted.

Define

    tau_P(sum_gamma f_gamma U_gamma)=[f_identity dt] in H^1(T).

Coefficient extraction and the quotient map are continuous. The trace is
cyclic. To prove this with the completed source product, write
 a=sum f_gamma U_gamma and b=sum g_gamma U_gamma, and set

    k_gamma=f_gamma alpha_gamma(g_(gamma^-1)).

Commutativity of the coefficient algebra gives

    (ab-ba)_identity
        =sum_gamma (1-alpha_(gamma^-1)) k_gamma.

This identity also supplies a convergent boundary preimage, rather than
only a formal expression as an infinite sum of boundaries. Write gamma
in the fixed prime generators. The telescoping identity for 1-product
alpha_p^n_p expresses each (1-alpha_(gamma^-1))k_gamma as a sum of
(1-alpha_p) applied to translated k_gamma, using at most sum_p |n_p|
terms. For n<0 use
1-z^n=-(1-z)sum_(j=n)^(-1) z^j; for n>0 use the usual finite geometric
sum. Prefix products in the multivariable telescoping formula are powers
whose heights are bounded by a fixed power of H(gamma).

The source action estimates of P123.121 bound all translated terms by
an additional power of H(gamma), and the number of terms is absorbed by
one further power. The rapid source seminorms of a,b therefore make the
coefficient sums of these degree-zero Koszul preimages absolutely
convergent. Their differential is exactly (ab-ba)_identity dt. Hence

    tau_P(ab)=tau_P(ba).

Likewise tau_P(Da)=0, since Df_identity dt is an explicit real de Rham
boundary. These are identities in the separated target, not statements
only after applying an unspecified scalar functional.

The same construction applies to the coefficient restriction algebras
on F_k and their layers. Restriction commutes with the group action,
real derivative and extraction of the identity label, so the induced
trace maps commute with those restrictions. On F_k, k>=1, their targets
are the finite H^1 of the glued closed-locus complexes. On the full
source the target retains the infinite open contribution determined
above. No finite scalar degree for the entire algebra is asserted.

Actual semilocal embeddings also commute with this trace. The coefficient
embedding E_P -> E_T multiplies by the new chi factors and is equivariant
for the old generators. It consequently gives a chain map from the old
deck/de Rham complex to the new one by inclusion of the old exterior
generators. It commutes with the real differential. Extraction of the
identity coefficient is preserved by the label inclusion, so

    tau_T(j_(P,T)(a))=H^1(j_(P,T))(tau_P(a)).

The triple compatibility follows from the exact coefficient and exterior
inclusions. This assertion requires no equivariance of chi under the
new generators: the domain differential contains only the old ones.
It therefore does not contradict the semilocal induction obstruction
of P123.123.

There is also a matrix extension: sum the diagonal entries and apply
tau_P. Its cyclicity follows by interchanging the finite matrix indices
and using the scalar source cyclicity above. This supplies the usual
trace of an idempotent matrix with values in the declared target,
invariant under conjugation whenever that conjugation is defined in the
source unitization and the traced entries lie in the nonunital ideal.
Such matrix traces are not automatically determinant metrics.

This is a concrete bridge from the original crossed multiplication to
the descended coefficient target, including continuity and semilocal
compatibility. It does not identify this trace with every derived
correspondence shadow, prove a comparison with the arithmetic contact
values, or establish the required mixed RR metric. Those stronger
identifications cannot be inferred from cyclicity of this degree-zero
source trace alone.

## Separation by all source tests for the descended trace

For a nonempty finite prime set P, the trace tau_P just constructed has
zero radical against all tests in the nonunital source algebra A_sm(P).
This assertion concerns that algebra and that vector-valued trace; it
is not yet the numerical equivalence of geometric correspondence objects.

First the general topology and ideal assertions hold on this domain.
Set

    Rad(tau)={a : tau(ab)=0 for every b in A}.

Every map a -> tau(ab) is continuous into a Hausdorff space, so the
radical is closed. Associativity and cyclicity show it is a two-sided
ideal: tau((ac)b)=tau(a(cb)) and tau((ca)b)=tau(a(bc)). Complex conjugation
preserves the coefficient deck/de Rham relations and induces a continuous
conjugation on the trace target. Since (a^*)_identity is the conjugate
of a_identity, tau(a^*)=conjugate(tau(a)). Cyclicity then shows that the
radical is star-stable. These facts do not invoke a positive Weil form.

To show this radical is actually zero, use the full descent triangle
already proved. Its open cohomology V=S(U_P) maps to the full H^1(T)
with finite-dimensional kernel

    W=im(H^0(F) -> V).

No calculation of W or assumption W=0 is needed. Let a be a nonzero
source element and choose a nonzero coefficient a_gamma. It is an actual
continuous function on R times product Q_p. The locus where every finite
coordinate is nonzero is dense, so a_gamma is nonzero at a point of this
open stratum. In its straightened coordinates (s,j,v), choose a shell j,
a compact real interval and a nonempty clopen unit neighborhood on which
|a_gamma| is bounded below by a positive constant.

Because P is nonempty, U_P has no isolated points. The chosen unit
neighborhood contains arbitrarily many pairwise disjoint nonempty clopen
subsets B_i. Choose nonnegative smooth functions h_i supported in the
selected shell, real interval and B_i, with nonzero real integral.
These belong to the open coefficient ideal: the shell and unit factors
are locally constant with compact support, and the real factor is smooth
and compactly supported. In the original coordinates they still have
this declared coefficient regularity.

Take a test b_i with its only nonzero lattice coefficient at gamma^-1,
namely

    (b_i)_(gamma^-1)=alpha_(gamma^-1)(conjugate(a_gamma) h_i).

Products, conjugation and the fixed lattice action preserve the source
coefficient algebra, so b_i is an allowed test. The identity coefficient
of a b_i is exactly |a_gamma|^2 h_i. Under open deck descent and real
integration its class is represented by the function

    g_i(v)=integral_R |a_gamma(s,j,v)|^2 h_i(s,j,v) ds.

Only the selected shell contributes to the shell sum. Thus g_i belongs
to S(U_P), is nonzero, and has support in B_i. The g_i are linearly
independent because their supports are disjoint. Their images in the
full trace target are tau(a b_i). If a were in Rad(tau), all g_i would
belong to the finite-dimensional W, which is impossible. Taking more
than dim(W) such tests suffices. Therefore Rad(tau)=0.

This proof uses nonnegative local products only to ensure nonvanishing
of the test functions g_i. It does not assign a sign to the vector-valued
trace or define geometric effectivity by operator positivity.

The source quotient by this all-test radical consequently keeps the
entire nonzero completed algebra, including its open localized kernels
and nonidentity lattice labels, with its Hausdorff topology and continuous
product and star. The result relies on the full vector-valued target and
on all source tests; a further scalar specialization can have a different
radical. It also does not identify this algebra quotient with N_A: the
passage to the geometric correspondence category, its contravariant
dagger, ruling plane and RR metric must still be constructed on compatible
domains. The separation theorem supplies one necessary source ingredient
without declaring the full A.6 acceptance clause proved.

## Projective source objects: separating categorical trace and duality

The all-test separation theorem extends to a precise category of source
objects. Let A=A_sm(P), P nonempty, and take objects to be finite matrix
idempotents e in M_n(A), representing the corresponding projective
modules. For e in M_n(A) and f in M_m(A) declare

    Hom(e,f)=f M_(m,n)(A) e.

These are closed complemented subspaces, with their actual Frechet
topologies: X -> fXe is a continuous idempotent projection. Composition
is matrix multiplication and the identity of e is e. The category has
finite direct sums and splits its matrix idempotents. It does not add a
trace of the absent scalar unit to the nonunital source.

Set Tr_e(u)=sum_i tau(u_ii). The finite rectangular matrix identity and
source cyclicity give Tr_e(vu)=Tr_f(uv). This categorical pairing is
nondegenerate against all reverse morphisms. In fact, if u is nonzero,
choose a nonzero entry and use algebraic all-test separation to find a
rectangular matrix h with just one nonzero entry such that Tr(hu)!=0.
The allowed reverse morphism is v=e h f. Since u=fue, cyclicity gives

    Tr_e(vu)=Tr(e h f u)=Tr(h u e)=Tr(h u)!=0.

Thus the categorical all-morphism radical is zero, with closed Hausdorff
Hom spaces and continuous composition. This establishes separation on
actual projective source objects rather than only on coefficients.

There is also an explicit continuous contravariant conjugate-linear
involution on this category:

    e^dagger=e^*,             u^dagger=u^*.

Here star includes transpose of the finite matrix. The type is correct:
u=fue implies u^*=e^*u^*f^*, so the direction of the morphism reverses.
It reverses composition, preserves object identities, squares to the
identity, and conjugates the trace. This is a categorical contravariance
on projective modules, unlike the covariant opposite-bimodule operation
noted in P123.122. It is not yet a dagger on the category of mixed
bimodule correspondences with their balanced tensor composition.

For bounded complexes of these objects there is a corresponding
contravariant operation on chain maps. In cohomological notation set

    (C^dagger)^n=(C^(-n))^dagger,
    d_(C^dagger)^n=(-1)^(n+1)(d_C^(-n-1))^dagger.

For a degree-zero chain map, take its dagger in each reversed degree.
The chain-map identities follow by taking daggers of the original
identities. Squaring this construction changes d to -d, and the maps
(-1)^n in degree n give the canonical chain isomorphism C -> C^daggerdagger.
Thus the degree signs, not an unjustified literal equality of complexes,
provide biduality. Chain homotopies also transpose, so this descends to
the homotopy category. All maps use finite matrices in each degree and
are continuous.

The trace on endomorphisms of a bounded complex is the supertrace

    STr_C(u)=sum_n (-1)^n Tr_(C^n)(u^n)

for degree-zero u. For graded u,v of complementary degrees, finite
reindexing gives STr(vu)=(-1)^(deg(u)deg(v))STr(uv). The supertrace of a
graded commutator vanishes, and in particular STr(dh+hd)=0 for a
homotopy h of degree -1. It therefore gives a trace on degree-zero
endomorphism classes in the homotopy category.

At the graded-chain level the pairing still separates: isolate a
nonzero component of u and choose its reverse component using the
projective-module argument above; its contribution has just the fixed
nonzero sign (-1)^n. But this does NOT prove nondegeneracy after taking
cohomology of Hom complexes. A separating reverse graded morphism need
not be a closed chain map. Nor has closedness of all Hom-boundary images
been proved. Hence no claim of a Hausdorff separated derived numerical
category is made from chain-level nondegeneracy alone.

This gives a concrete projective source category with continuous
contravariance and separating cyclic trace, together with its bounded
complex operations and the exact limit of the separation result. It
still lacks the identification with localized mixed correspondences,
the tensor-duality comparison required by A.4, the ruling plane and the
intrinsic RR metric. Those remain part of the unchanged full A target.

## Correction: the nonunital projective category has no nonzero objects

The preceding projective-category argument must not be used as evidence
of a nonzero category for A. Its formal trace and dagger formulas are
valid, but the particular category defined by idempotents IN M_n(A_sm(P))
is trivial. The following proof resolves the existence issue rather
than presuming a boundary cutoff lifts to the common nonunital source.

On the open stratum use the coordinates (s,j,v) already defined, with
j in Z^P, v in U_P, and t=s+sum_p j_p log p. The lattice acts freely
by shifts of j, fixing s,v. The regular orbit representation at (s,v)
has matrix entries, up to the fixed choice of inverse-label convention,

    pi_(s,v)(a)_(j,j-gamma)=a_gamma(z_j(s,v)).

Its matrix multiplication is exactly the source crossed multiplication.
For each l>0 the coefficient seminorms imply a uniform pointwise bound

    |f(t,(p^j_p u_p)_p)|
      <=C nu_l(f) exp(-l|t|)
                    exp(-2l sum_p log(p) max(-j_p,0)).

Indeed chi_p is bounded for j_p>=0 and zero for j_p<0, while its F_p
remainder obeys every shell-decay bound. The projective tensor seminorm
extends these elementary coefficient estimates to E_P.
Writing L_+=sum log(p)max(j_p,0) and L_-=sum log(p)max(-j_p,0), one has

    |s+L_+-L_-|+2L_- >= s+L_++L_-.

It follows that

    sum_(j,gamma)|a_gamma(z_j(s,v))|
      <=C_l exp(-l s) sum_gamma nu_l(a_gamma)
                       sum_j exp(-l sum_p |j_p|log p).

The final shell sum is finite. The rapid source seminorm controls the
coefficient sum. Thus each orbit operator is trace class (in particular
compact), and its norm tends to zero as s tends to positive infinity,
uniformly in v. The same estimates for real derivatives imply continuity
in s in trace norm on every compact interval. If the opposite real
translation convention is used, replace s by -s and use the other end.

Now let e in M_n(A_sm(P)) satisfy e squared=e. Its orbit representations
are continuous families in s of compact idempotents on the amplified
orbit Hilbert space. A compact idempotent has finite rank, and rank is
locally constant in an operator-norm continuous family of idempotents.
For completeness, sufficiently close idempotents have injective maps
between their ranges by restricting one idempotent to the other's range;
applying this both ways gives equality of their finite ranks. At large
positive s the norm of pi(e) is less than one, forcing pi(e)=0, since a
nonzero idempotent acts as identity on its range. Connectedness of R then
implies pi_(s,v)(e)=0 for every s and each fixed v.

The family of orbit representations is faithful on the source: its
individual matrix entries recover every coefficient on every open-stratum
point. That open stratum is dense, and all source coefficients are
continuous actual functions. Vanishing there therefore implies vanishing
everywhere. Consequently e=0.

Thus the matrix-idempotent category specified above cannot supply the
nonzero mixed sector of A; its separation statement is vacuous on
objects. This does not refute separation of the algebra elements proved
earlier, nor the full-corner projectives on a boundary restriction
algebra. A cutoff projection on that boundary need not lift to an
idempotent of the common nonunital algebra. Those domains must remain
distinct.

The appropriate remaining construction must use the existing coefficient
unitization, projectives with specified behavior in its scalar lattice
quotient, and relative complexes or localization data. No trace of a
unit or nonzero relative K-class is inferred by this correction. In
particular merely replacing 'idempotent in A' by 'idempotent in its
unitization' would require new trace domains and comparison proofs.
The earlier bounded-complex formulas remain formal formulas for that
stated category, not a completed construction of nonzero arithmetic
projective correspondences.

## Repair in the existing unitization: trace and a nonzero relative complex

Let B=A_sm^u(P) be the coefficient unitization already defined in
P123.121, A its nonunital ideal, and L the rapid scalar lattice algebra.
The actual splitting B=A direct_sum L is a vector-space splitting with
L a subalgebra. Define

    tau_tilde(a+lambda)=tau(a),       a in A, lambda in L.

This is continuous and cyclic. The A-A case was proved above. The L-L
case has trace zero because its product stays in L. For a mixed product,
the identity coefficient of [lambda,a] is a convergent sum of scalar
multiples of (alpha_gamma-1)a_(gamma^-1). The same telescoping estimates
used for tau supply convergent deck boundary preimages. Hence its trace
vanishes too. Thus tau_tilde is an actual trace on this unitization,
with tau_tilde(1)=0. It is not an extension of a scalar rank trace taking
1 to 1, and no positivity assertion is made.

The trace pairing on B still separates against tests in A. To see this,
a nonzero coefficient of b in B has the form lambda_gamma+a_gamma(z).
If this function were identically zero, real decay of a_gamma would
force lambda_gamma=0 and then a_gamma=0. Thus a nonzero b has a coefficient
nonzero somewhere on the dense open stratum. The disjoint clopen tests
from the preceding separation proof apply verbatim: multiply its
conjugate by a compactly supported open coefficient to obtain a test in
A, isolate the inverse label, and integrate the resulting nonzero local
squares. More than dim(W) disjoint unit supports cannot all map to the
finite kernel W of the open-to-full trace target. Therefore

    [tau_tilde(bc)=0 for all c in A] implies b=0.

Finite matrix idempotents in B now give a nontrivial projective category:
the unit itself is an object. The earlier sandwich argument proves
separation of its projective morphisms, using tau_tilde and reverse tests
whose entries lie in A. Its matrix-star dagger and bounded-complex
formulas are now applicable on a nonzero category. This repairs the
object-existence defect; it does not turn right modules into mixed
bimodule correspondences.

A genuinely nonzero RELATIVE perfect complex can also be exhibited.
Choose a real-valued coefficient f in A, supported inside the open
stratum at the identity label, equal to 1 on a smaller nonempty product
of a real interval, fixed valuation shells and a clopen unit set. Such
an f is a smooth compact real bump times compact locally constant
finite-place functions and belongs to the declared source. On free
right B-modules form

    C_f=[B --L_(1-f)--> B],      degrees 0,1.

Left multiplication is right B-linear. Reduction along B -> L gives
the contractible complex [L --1--> L]. However C_f is not contractible
in the source: any nonzero coefficient h supported where f=1 satisfies
(1-f)h=0, so H^0(C_f) is nonzero. In particular the identity of C_f is
not null-homotopic. This construction does not require a nonzero
idempotent in A.

There is a closed endomorphism of C_f detected by the source trace.
Take h supported in the plateau of f and set u^0=L_h, u^1=0. It is a
chain map because (1-f)h=0. Choose h from the disjoint unit-support
family in that plateau; at least one has tau(h)!=0 by the finite-kernel
argument. Its supertrace is then

    STr_(C_f)(u)=tau_tilde(h)=tau(h)!=0.

Since the trace of a null-homotopic endomorphism is zero by cyclicity,
this u survives in the homotopy category and detects its identity in
the trace pairing. Thus this example is not a chain-level artifact or
a merely formal assertion that relative objects should exist.

Bounded projective complexes over B whose reduction to L is contractible
form a concrete nonempty class closed under finite sums, shifts and
cones of chain maps: reduction commutes with these operations, and the
cone of a map between contractible complexes is contractible. The class
is also preserved by the bounded-complex dagger, because reduction
commutes with star and the dual of a contracting homotopy contracts the
dual complex with the declared signs. This supplies stable operations
on actual relative source objects and the separating example above.

No claim is made that every morphism in this homotopy category is
separated by supertrace, or that all its Hom-boundary images are closed.
Nor is nonvanishing of C_f a proof of a nonzero relative K-class: its
alternating free ranks cancel. Finally, composition of arithmetic
bimodule kernels and the intrinsic RR metric are still not provided by
this category of right-module complexes. These remain explicit parts
of the full A construction.

## A separated relative contact and failure of the degree-zero supertrace

A finite-order contact tests the derived separation requirement without
using a plateau zero. Choose theta to be the characteristic function of
a nonempty compact clopen finite-place box contained in the open stratum,
for example a product of fixed shells and unit clopen subsets. Choose
a smooth real function r with r(t)=t^2 near zero, r(t)>0 for t!=0, and
r(t)=1 outside a compact interval. Set

    f(t,x)=theta(x)(1-r(t)) in A,
    g=1-f in B,
    C_g=[B --L_g--> B],       degrees 0,1.

Its reduction to the scalar lattice quotient is [L --1--> L]. On the
box theta=1 its differential is multiplication by r(t); outside it the
differential is the identity. Its coefficient zero set is precisely
{t=0,theta=1}, which has empty interior.

Multiplication L_g is injective. Indeed its action is coefficientwise
multiplication by g, and a continuous coefficient function annihilated
by g vanishes on a dense set, hence everywhere. Its image is closed:
it is exactly the simultaneous kernel of the continuous maps extracting
the zeroth and first real jets at t=0 on the box, for every lattice label.
Necessity is immediate. For sufficiency, a smooth function with both jets
zero is divisible by t^2 with continuous estimates using two additional
real derivatives on a fixed small interval (Taylor's integral remainder).
Away from that interval divide by the fixed positive smooth r. These
local divisions and compact cutoffs preserve all transverse seminorms
and real decay estimates. They therefore give a continuous division map
on the joint jet kernel, uniformly in the rapid label seminorms.

For coefficient unitization write a label coefficient as lambda+a.
After division its difference from lambda is (a+lambda f)/g. The
numerator has both jets zero whenever lambda+a does, since it equals
(lambda+a)-lambda g. It has the required decaying coefficient regularity.
Thus division really lands in B, not in a larger multiplier algebra.

The cokernel is the nonzero Hausdorff rapid sequence space of two jets
with values in S of the chosen finite-place box. Surjectivity of the
jet map follows by multiplying prescribed jets by fixed compact real
functions equal to 1 and t near zero, respectively. This constructs a
continuous underlying splitting. Hence C_g is a nonzero relative perfect
complex with separated cohomology; it is not a failure caused by a
nonclosed multiplication range.

Nevertheless the degree-zero supertrace constructed above fails to
detect its identity against EVERY closed endomorphism. Write a chain
endomorphism as left multiplications u_0,u_1 in B. The chain equation is

    g u_0=u_1 g.

At the identity lattice coefficient it reads pointwise

    g(z)(u_0)_identity(z)=(u_1)_identity(z)g(z).

Since g is nonzero on a dense set, the two identity-coefficient functions
are equal everywhere. Their scalar/decaying decompositions are unique
by real decay. Consequently

    STr_(C_g)(u)=tau_tilde(u_0)-tau_tilde(u_1)=0

for every closed u. But id_(C_g) is not null-homotopic, because its
cokernel just computed is nonzero. Thus its identity is in the radical
of this supertrace pairing in the homotopy category. The chain-level
separation theorem cannot be promoted to derived separation, even for
this finite-order contact with closed image.

In fact cyclicity makes the identity invisible against tests factoring
through other objects as well: a cycle C_g -> D -> C_g gives an
endomorphism of C_g and therefore has zero trace. A numerical quotient
formed from this particular degree-zero supertrace would erase C_g.
This does not disprove A.6, which has a richer geometric shadow domain;
it proves that the proposed degree-zero specialization cannot by itself
supply the required contact-sensitive derived numerical theory.

The two-jet cokernel is actual surviving contact data, whereas the
alternating source trace cancels it. A valid next comparison must retain
this supported/derived information in its shadow and determinant before
specializing the trace. No claim that ordinary matrix supertrace has
already supplied that information is retained.

## The actual derived contact endomorphisms and their residual pairing

The contact erased by the supertrace admits a different, explicit
source-level invariant. Retain the compact clopen box theta and replace
t^2 near zero by t^m, with m a positive even integer; choose r positive
away from zero and equal to 1 outside a compact interval as before.
All division and closed-range arguments use m jets and m additional
real derivatives. Put Q=B/gB, the right-module cokernel of L_g, and let
R_theta be the rapid smooth finite-place coefficient algebra on the box.
Then as a topological vector space Q consists of rapid lattice sequences
of elements of

    J_m=R_theta[epsilon]/(epsilon^m).

Taylor coefficients use f^(j)(0)/j!, so epsilon is the original real
coordinate t to order m-1. The quotient topology and its continuous
jet-lifting section were specified by the division construction.

The continuous right B-module endomorphism algebra of Q is EXACTLY J_m,
not the entire lattice sequence space. Indeed an endomorphism is
determined by v, the image of the class of 1, and must satisfy v g=0.
At label gamma this condition multiplies the jet v_gamma by the jet of
alpha_gamma(g). For gamma different from identity, alpha_gamma(g) has
no zero at t=0 on the box: its real zero would be at log gamma, which
is nonzero for a nontrivial element of the prime lattice. Where its
finite-place cutoff is absent the function is 1. Its constant jet is
therefore invertible on the compact box, so v_gamma=0. This reasoning
is coefficientwise; it does not require a uniform inverse bound as
gamma approaches identity in the real embedding.

At the identity label g has zero m-jet, so there is no restriction on
v_identity in J_m. Every such jet lifts to an identity-label coefficient,
whose left multiplication gives a continuous endomorphism of Q because
it commutes with g. Composition is multiplication of jets. Evaluation
at the class of 1 and the fixed continuous lifting section prove the
topological identification of this endomorphism algebra with J_m.

The same algebra is the degree-zero ENDOMORPHISM COHOMOLOGY of the
perfect complex C_g, not merely an algebra of its coefficient jets.
For a chain map (u_0,u_1), its action on Q is represented by u_1 modulo
gB. After subtracting the diagonal chain map of its identity-label jet,
write u_1=g h using the continuous division on the jet kernel. The
chain equation then gives g u_0=g h g; injectivity of L_g yields u_0=h g.
Thus the remaining chain map is the null-homotopy (h g,g h). This proves

    H^0 Hom_B(C_g,C_g) ~= J_m

with closed degree-zero Hom boundaries and a continuous representative
section. No assertion about all higher Hom degrees is needed here.

Define the R_theta-valued residual functional

    res_m(sum_(j=0)^(m-1) a_j epsilon^j)=a_(m-1).

This is the coefficient of t^-1 dt in the finite principal part of
(a(t)/t^m)dt. It is therefore specified from the contact equation and
the existing real coordinate, rather than from a desired sign. The
pairing res_m(ab) on J_m has matrix

    res_m(epsilon^i epsilon^j)=1 if i+j=m-1, and 0 otherwise.

This anti-diagonal matrix is invertible over R_theta. Hence it gives
an explicit perfect relative duality

    J_m -> Hom_(R_theta)(J_m,R_theta),
    a -> [b -> res_m(ab)].

All maps are continuous since J_m is finite free of rank m over R_theta.
In particular the all-test radical is zero. The identity, though erased
by the previous supertrace, is detected by the test epsilon^(m-1).
Nilpotent endomorphisms are retained as well. Finite matrix extension
using the sum of diagonal residues is cyclic and supplies the same
sandwich separation on projective J_m-modules.

For comparison, the ordinary R_theta-linear trace of multiplication by
a on J_m is m a_0. It correctly gives the contact length m on the
identity but kills every nilpotent. These are different maps with
different purposes: residual perfect duality and finite-module trace.
Neither is silently identified with the alternating source supertrace,
which was proved to vanish on every endomorphism of C_g.

The residual duality also has a local derived description. On the
commutative coefficient chart the free resolution

    0 -> A^0 --t^m--> A^0 -> J_m -> 0

is exact, with the same continuous division estimates. Applying the
relative Hom complex gives its degree-one Ext module J_m; tensoring the
dual generator with dt identifies its principal part as dt/t^m. The
residue formula above is precisely the resulting finite-jet pairing.
This description is local on the coefficient chart. It is not a claim
that this commutative Ext computation already identifies every derived
Hom or shadow in the crossed correspondence category.

This constructs contact-sensitive data on an actual relative source
complex, including a separated derived endomorphism algebra and its
perfect residual pairing. It supplies an alternative to the degree-zero
supertrace that erased the contact. Extending it compatibly to different
contacts, their composition, semilocal descent and the intrinsic metric
remains necessary; an isolated Frobenius jet algebra is not full row A.

## Compatibility across contact orders: the trace belongs in Ext degree one

The residual functional on each J_m must not be promoted to a cyclic
trace on degree-zero maps between arbitrary contact orders. There is a
counterexample already among the even orders realized above. Put
J_2=R_theta[t]/t^2 and J_4=R_theta[t]/t^4. Let i:J_2 -> J_4 multiply by
t^2, and let p:J_4 -> J_2 multiply by t and reduce modulo t^2. Both are
well-defined coefficient-module maps. Then

    p i=0,              i p=multiplication by t^3,
    res_2(p i)=0,       res_4(i p)=1.

Thus the preceding perfect Frobenius pairings on the individual jet
algebras do not form a degree-zero categorical trace across these
objects. Their derived normalization must be retained.

Here is the compatible local construction. Work on the same commutative
coefficient chart with coordinate t and coefficient ring R=R_theta.
For positive integers m,n, put d=min(m,n). The two-term free resolutions
by multiplication by t^m and t^n give

    Hom(J_m,J_n)=t^(n-d) R[t]/t^n ~= J_d,
    Ext^1(J_n,J_m)=J_m/t^n J_m ~= J_d.

Higher Ext groups vanish on this chart. The displayed identifications
are topological: all jet spaces are finite free over R, and the smooth
coefficient divisions have the continuous Taylor estimates already
proved. The Hom formula follows by solving t^m u=0 in J_n; the Ext
formula follows by applying Hom to the length-one free resolution.

Orient the degree-one self-extension trace by the original dt:

    tr_m:Ext^1(J_m,J_m) -> R,
    tr_m(c)=coefficient of t^(m-1) in c.

For f:J_m -> J_n represented by t^(n-d)a and an extension class
xi in Ext^1(J_n,J_m) represented by b modulo t^d, their two Yoneda
compositions satisfy

    tr_m(xi composed f)=coefficient_(t^(d-1))(ab),
    tr_n(f composed xi)=coefficient_(t^(d-1))(ab).

To check this without an abstract duality theorem, lift f to the free
resolutions: its map on the quotient-side free term is t^(n-d)a and
its map on the relation-side free term is t^(m-d)a. Pulling back the
extension gives t^(m-d)ab in Ext^1(J_m,J_m); pushing forward gives
t^(n-d)ab in Ext^1(J_n,J_n). Taking the indicated coefficients proves
both identities, and also shows independence of all representatives.

The common coefficient pairing on J_d is anti-diagonal and invertible.
Consequently this constructs the perfect relative pairing

    Hom(J_m,J_n) x Ext^1(J_n,J_m) -> R

with its correct composition compatibility for EVERY pair m,n. It pairs
the identity with a degree-one class, rather than attempting to detect
it by an incompatible family of degree-zero traces. Finite sums use
matrix traces, and composition compatibility follows entrywise. Both
compositions of two degree-one classes land in the vanishing Ext^2;
the remaining cases are the degree-zero/degree-one identities just
proved. Thus these local trace formulas respect the cohomological
grading instead of suppressing the self-extension term.

The contact complexes in the crossed source also carry a well-defined
version of this degree-one trace, on their self Hom cohomology. A
 degree-one cochain of C_g is an element v of B. Boundaries have the
form g u_0-u_1 g. At the identity label these are divisible by t^m on
the box, so taking that label's (m-1)-st Taylor coefficient annihilates
all boundaries. The resulting map

    H^1 Hom_B(C_g,C_g) -> R_theta

is continuous on the quotient topology and agrees with the local
Ext trace on identity-label coefficient classes. It is onto, by taking
v to be a compact lift of a(t,u)=t^(m-1)b(u). These classes cannot be
boundaries because their displayed residue is b. This provides actual
nonzero degree-one source classes detected by the residual map.

No assertion is made here that this map separates the full crossed
H^1 Hom space, or that every nonidentity-label extension is absent.
Those claims require uniform completion estimates beyond the local
free-resolution calculation. Nor has a global shadow with values in
these supported dualizing modules been glued across distinct supports
or compared with the arithmetic metric. What is proved is the compatible
local derived trace across contact orders and its explicit nonzero
realization in the source, correcting the false degree-zero promotion.

## Full crossed Hom comparison for contacts in a single valuation box

For the contacts above, choose the allowed box theta inside ONE fixed
valuation shell at every prime in P, with a clopen unit subset there.
This geometric condition eliminates the nonidentity-label Hom complexes
by a uniform algebraic contraction. It is stronger and simpler than a
small-real-divisor estimate, and its precise scope is important.

For two even contact orders m,n on that same box, write g_m=1-f_m and
g_n=1-f_n as before. Any gamma!=identity has a nonzero valuation at some
prime of P. Hence theta and alpha_gamma(theta) have disjoint support.
In particular

    f_n alpha_gamma(f_m)=0,
    g_n+f_n alpha_gamma(g_m)=1.                 (*)

This identity is exact in the original coefficient unitization.
No limit in gamma and no inverse with potentially growing derivatives
is involved.

The Hom complex Hom_B(C_m,C_n) has degrees -1,0,1, with spaces B,
B direct_sum B, B. Its differentials on label gamma are, writing
b_gamma=alpha_gamma(g_m),

    d_-1(h)=(h b_gamma,g_n h),
    d_0(u_0,u_1)=g_n u_0-u_1 b_gamma.

For gamma!=identity define

    H_1(v)=(v,-f_n v),
    H_0(u_0,u_1)=u_1+f_n u_0.

Commutativity of the coefficient functions and (*) give

    d_0 H_1=1,
    H_0 d_-1=1,
    d_-1 H_0+H_1 d_0=1,
    H_0 H_1=0.

For example the first identity is g_n v+f_n v b_gamma=v; the middle
one in degree zero follows by cancelling the two cross terms. These
formulas give a contraction of the entire nonidentity-label Hom complex,
including scalar lattice coefficients.

All its maps are continuous on the actual rapid completion. Extracting
or deleting the identity label is continuous, and the displayed formulas
only use identity, addition and left multiplication by the fixed
coefficient f_n. The original source seminorm estimates bound these
operations independently of gamma. The differentials use the already
continuous source left/right products. Thus the labelwise identities
extend to the completed Hom complexes without an unproved uniform
small-divisor assertion.

The identity-label subcomplex is exactly the commutative coefficient
Hom complex of the two finite-order contact resolutions. Outside the
box, the differentials are units and its complex is contractible.
Inside the box, Taylor division reduces it to the local calculation
already given. Therefore the FULL source Hom cohomology is

    H^0 Hom_B(C_m,C_n) ~= J_min(m,n),
    H^1 Hom_B(C_m,C_n) ~= J_min(m,n),
    H^j=0 otherwise.

The H^0 identification retains the multiplying factor t^(n-min(m,n))
on the quotient-side map, as in the preceding local calculation. These
are finite free modules over R_theta, not finite-dimensional scalar
spaces unless a further justified transverse pushforward is performed.
All boundary images are closed: the nonidentity part has the explicit
continuous contraction, and the identity part has continuous finite-jet
representatives and division on the jet kernels.

For the family of these contact complexes, keeping only identity-label
Hom cochains is a dg subcategory: differentials and composition preserve
identity labels. Its inclusion into the full crossed Hom category is a
quasi-isomorphism on every Hom complex by the contractions above. Thus
cohomology classes and their compositions really are represented by the
local coefficient calculations; this is not just a vector-space dimension
comparison. No assertion of formality of that dg category is needed.

Consequently the degree-one residue traces and the perfect pairings

    H^0 Hom_B(C_m,C_n) x H^1 Hom_B(C_n,C_m) -> R_theta

proved locally now hold for the full completed source on this contact
family. They satisfy the composition identities already checked by the
two-term resolutions. There are no hidden nonidentity-label extensions
in this specified family, and its derived pairing has zero radical with
closed Hom boundaries. This resolves the completion issue left open in
the preceding section for these actual source contact objects.

The single-box hypothesis is not removed: contacts on different boxes,
more general supports, and bimodule-kernel convolution require additional
comparisons. Nor does this identify R_theta-valued degree-one residues
with the intrinsic periodic determinant metric. This is a complete
crossed-versus-local derived Hom comparison on the stated contact sector,
not a declaration that the full arithmetic row A is closed.

## Finite families of contact supports and their common derived trace

The single-box computation extends to finite families of the following
actual source contacts. An object has even order m, real centre c, and
a compact clopen box in one valuation cell j in Z^P; its defining function
is 1 outside that box and a compact real interval, and equals (t-c)^m
near its zero set. Profiles may be chosen positive away from that zero
set, as above. The assertion below is for fixed finite families, with
constants allowed to depend on their distinct real centres.

First normalize the valuation cells using the actual gauge units in B.
For lambda=product_p p^(-j_p), conjugation alpha_lambda moves the cell
to valuation zero. Left multiplication by U_lambda in both free terms
is a chain isomorphism from C_g to C_(alpha_lambda(g)), because

    alpha_lambda(g) U_lambda=U_lambda g.

Its inverse is left multiplication by U_(lambda^-1). These are continuous
source maps and their compositions obey the exact group law. The new
real centre is s=c-sum_p j_p log p, and the unit box is its corresponding
translated box in U_P. This supplies actual comparison maps, not merely
an identification of orbit labels.

After this normalization all contacts are in valuation cell zero. Thus
for EVERY pair of them the nonidentity-label Hom contraction from the
previous section applies, even when their unit boxes differ. Their
translated finite-place supports are disjoint for nonidentity labels.
It remains to compute the commutative identity-label complex.

If two normalized real centres differ, their zero sets are disjoint.
For the two positive defining functions g,h the functions

    A_0=g/(g^2+h^2),       B_0=h/(g^2+h^2)

are smooth elements of the coefficient unitization, with g A_0+h B_0=1.
The denominator has a positive lower bound for this fixed pair: outside
a compact real interval both functions are 1, and within it the unit
cutoffs take finitely many clopen values and have no common zero.
All transverse and real seminorms are therefore finite. The Hom complex
is contracted by

    H_1(v)=(A_0 v,-B_0 v),
    H_0(u_0,u_1)=B_0 u_0+A_0 u_1.

The same elementary Koszul identities verify the contraction. No uniform
bound is claimed as distinct centres approach one another.

If the centres agree, only the intersection of their unit boxes
contributes. On that intersection the previous Taylor calculation gives
J_min(m,n) over its transverse coefficient algebra. Outside it one of
the contact equations is 1, and the complex is contractible. Local jet
representatives are extended by compact real cutoffs, so the comparison
maps land in B. This does not treat a bare finite-place cutoff, constant
along the entire real axis, as an element of B.

Finite clopen refinements can be handled by actual source decompositions.
If a contact box is the disjoint union of boxes theta_i, write g_i for
the contact with the same real profile on theta_i. Then g=product_i g_i.
For two disjoint boxes, with f_i=1-g_i,

    f_1 f_2=0,       g_1+f_1 g_2=1.

There is a continuous right-module Chinese-remainder isomorphism

    B/(g_1 g_2)B -> B/g_1B direct_sum B/g_2B.

The map is reduction in the two coordinates; its inverse is represented
by f_1 g_2 x+g_1 y for representatives x,y. Independence of representatives
follows because each error is a multiple of g_1g_2. The same Bezout
identity proves that the kernel of the forward map is precisely that
product ideal. Iteration gives the finite refinement comparison. The
closed-range free resolutions then realize this as a derived direct-sum
comparison of the contact complexes; no nonexistent idempotent in A is
being introduced.

Refine the finitely many unit boxes into their Boolean clopen atoms.
For each real centre and each atom, the family consequently has the
jet Hom/Ext description already proved, while different centres or
disjoint atoms have zero Hom cohomology. Extend the residue values by
zero from each atom into R=S(U_P), and sum them over the finite family.
This defines a COMMON R-valued degree-one trace on its contact objects.
For any two objects the pairing between degree-zero Hom and reverse
 degree-one Hom is perfect over the corresponding clopen summands of R:
on each atom it is the invertible anti-diagonal jet pairing. Cyclic
composition follows atomwise from the explicit Yoneda formulas, and
zero morphisms between different centres introduce no additional terms.

All Hom boundary images are closed, by the pairwise contractions and
jet divisions above. Refinement compatibility follows from reduction
and extension by zero on clopen atoms, whose sums reproduce the original
jet functions and residues. Gauge normalization changes real coordinates
only by translation, so it preserves dt and the coefficient-of-t^-1
residue; the finite-place change is the specified unit translation.
Thus the common trace includes the source comparisons between these
finite support presentations.

This establishes the contact-sector derived comparison and trace for
finite families of boxes and centres on the actual open semilocal
source. It does not establish a completion over infinitely many colliding
centres, a tensor-convolution category of bimodule kernels, or the
intrinsic determinant metric. These remain distinct requirements for
the full arithmetic row A.

## Finite collisions without singular jet splittings

Finite collisions can be included without dividing by distances between
roots. Fix one valuation box as above and a bounded collection of real
parameters x_1,...,x_N, with repetitions allowed. For source contact
profiles take each distinct labelled factor with even multiplicity, so

    P_x(t)=product_(j=1)^N (t-x_j)

is nonnegative and positive away from its real zeros. Choose a fixed
compact real cutoff eta equal to 1 on a neighborhood of all allowed
roots, and define r_x=eta P_x+(1-eta). Its transition region contains
no root, so r_x is positive there. Using r_x on the box and 1 outside
it gives a smooth source contact equation g_x=1-f_x as before. All
parameter statements below are local on bounded parameter sets, with
a common root neighborhood and cutoff.

There is a continuous division/remainder construction uniform through
collisions. For a smooth coefficient function F use Newton interpolation
with the divided differences at the labelled nodes:

    R_x(F)(t)=sum_(k=1)^N F[x_1,...,x_k]
                              product_(j<k)(t-x_j).

At repeated nodes, define divided differences by the integral formula

    F[y_0,...,y_l]
       =integral_(Delta_l) F^(l)(sum_i s_i y_i) ds,

where the simplex measure has volume 1/l!. This formula is defined even
when all nodes coincide and gives F^(l)(y_0)/l! in that case. Taylor's
formula or repeated integration yields the exact identity

    F(t)-R_x(F)(t)=P_x(t) F[x_1,...,x_N,t].

Thus neither remainder nor quotient requires inverse root separation.
The integrals preserve all transverse coefficient seminorms. Derivatives
in t and in the labelled root parameters cost only finitely many higher
real derivatives of F on each compact parameter set. For a coefficient
family depending on those parameters, differentiate its integrand as
well. This supplies the stated smooth continuity in parameters, including
the collision locus, rather than inferring it from interpolation at
distinct points.

Multiplying the polynomial remainder by a fixed compact real cutoff
equal to 1 near the roots gives source representatives. Away from that
neighborhood divide by the nonzero profile r_x; its lower bound is
uniform on compact parameter sets with the chosen transition region.
Consequently the source quotient by g_x has the expected polynomial
remainder model, with continuous splittings. Its identity-label algebra is

    J_(P_x)=R_theta[t]/P_x(t),

finite free over R_theta with the same basis 1,t,...,t^(N-1) for all x.
The scalar/decaying coefficient splitting in B is handled as before by
subtracting the unchanged scalar part after division. The nonidentity
Hom contraction continues to hold exactly because all these contacts
remain in the same valuation box. Hence the self Hom cohomology of the
actual crossed contact complex is J_(P_x) in degrees zero and one.

Define the oriented extension trace by

    res_(P_x)(a)=coefficient of t^(N-1) in its remainder.

Equivalently it is the coefficient of t^-1 in the Laurent expansion at
infinity of a(t)/P_x(t); this fixes the sign without using a residue-at-
infinity convention. In the monomial basis the pairing res_(P_x)(ab)
has zeros when i+j<N-1 and ones when i+j=N-1. Its determinant is

    (-1)^(N(N-1)/2),

because reversing the columns makes the matrix triangular with unit
diagonal. The other entries depend polynomially on the coefficients
of P_x. Thus the relative pairing remains perfect at every finite
collision. The determinant line has the same basis wedge
1 wedge t wedge ... wedge t^(N-1), with no vanishing discriminant factor
introduced by a choice of separate-root coordinates.

When the roots separate into disjoint clusters, partial fractions or
polynomial Chinese remainders identify this trace with the sum of local
residues using the full differential dt/P_x. The complementary polynomial
factor must be retained in each local residue. As clusters collide,
those separate-root formulas can diverge, but their common polynomial
model and total pairing above remain regular. For example

    P_s(t)=(t-s)^2(t+s)^2

has two order-two contacts for s!=0 and the order-four algebra at s=0;
its total residue pairing has determinant 1 throughout.

For two contact equations P,Q, derived comparison during collisions
must retain the finite two-term complex obtained by applying the free
resolution of one contact to the other's quotient: its differential is
multiplication by P in R_theta[t]/Q. This finite matrix depends smoothly
on the parameters. Its kernel and cokernel can jump at common roots;
no constant-rank claim for these cohomology spaces is made. Keeping the
matrix complex, instead of replacing it by a family of separated Hom
cohomologies, preserves those derived collision terms.

This proves a source-realized finite collision model and a nonsingular
relative residue/determinant LINE. It neither constructs an infinite
collision completion nor fixes a Hermitian determinant metric. In
particular a regular basis and a perfect residue pairing are not yet the
intrinsic mixed RR metric required by A.8.

## Mixed finite-contact determinant and its multiplicative equality

The finite collision complexes give an explicit equality of determinant
sections, not only the existence of lines. Let R=R_theta (or its smooth
parameter coefficient algebra on a fixed bounded family), and let P,Q
be monic contact polynomials of degrees m,n. Put E_Q=R[t]/Q, a finite
free R-module of rank n. The two-term complex

    E_Q --M_P--> E_Q

is the finite model obtained from the free resolution of one contact
against the other. For tensor it is placed in degrees -1,0; for Ext
in degrees 0,1. These placements differ, but neither discards its kernel
at a common root. Fix the line convention explicitly:

    L(P,Q)=det(E_Q,target) tensor det(E_Q,source)^-1,
    s(P,Q)=det(M_P) in L(P,Q).

The section is defined even when the differential is singular. With the
same monomial bases on its source and target its coefficient is

    det(M_P)=Res(Q,P),

where this fixes the order convention for the resultant. To prove the
formula, for distinct roots beta_1,...,beta_n of Q, multiplication by P
is diagonal in the evaluation basis with eigenvalues P(beta_j). Hence
its determinant is product_j P(beta_j). Both sides are polynomials in
the coefficients of the monic P,Q, so the identity extends to repeated
roots. Equivalently the companion matrix of Q gives M_P=P(T_Q), making
the polynomial dependence explicit. The identity is over the universal
coefficient ring and remains valid after substitution in R.

There are multiplicative section identities in BOTH arguments:

    Res(Q,P_1 P_2)=Res(Q,P_1) Res(Q,P_2),
    Res(Q_1 Q_2,P)=Res(Q_1,P) Res(Q_2,P).

The first follows directly from M_(P_1 P_2)=M_(P_1)M_(P_2) on E_Q.
For the second, the monic polynomials give the finite exact sequence

    0 -> R[t]/Q_1 --multiply Q_2--> R[t]/(Q_1 Q_2)
          -> R[t]/Q_2 -> 0.

Injectivity follows by cancellation of the monic Q_2 in R[t]; division
by a monic polynomial proves the other assertions. This works even when
Q_1 and Q_2 have common roots. Multiplication by P respects this sequence,
so its determinant is the product of its two diagonal-block determinants.
The sequence splits as R-modules by polynomial remainder sections.
Consequently it gives actual determinant-line identifications, not just
an equality at numerical parameter values. Repeated factorizations are
compatible by the exterior-power identifications for the corresponding
finite filtrations, including their usual degree signs.

If P=product_i(t-alpha_i)^m_i and Q=product_j(t-beta_j)^n_j, the explicit
section formula is

    s(P,Q)=product_(i,j)(beta_j-alpha_i)^(m_i n_j)

in the chosen determinant bases. Thus the determinant section records
the multiplicity of every pairwise collision. At a common root it
vanishes; the line and its full two-term complex remain defined. For
example P=(t-s)^2 and Q=(t+s)^2 give s(P,Q)=16 s^4. At s=0 the matrix
is zero on R[t]/t^2, and both its kernel and cokernel have rank two.
The vanishing section does not authorize replacing this derived contact
by the zero object or by its cokernel alone.

These equalities are functorial under coefficient substitutions and the
smooth finite-collision parameter maps already constructed. They are
therefore a concrete mixed determinant calculation in the contact
sector. No Hermitian metric has been fixed by this calculation. Giving
the monomial basis unit norm would be a new metric choice; it is not a
proof that the intrinsic periodic ruling metric is obtained. Likewise
multiplicativity in monic equations is not principal-divisor invariance
on the arithmetic carrier. The requisite geometric comparison and its
metric remain necessary for A.8.

## Independence of a local contact equation, with its metric transition law

The contact residue and determinant have explicit transition maps under
changes of a local equation. This is local presentation independence;
it must not be confused with principal-divisor invariance on the whole
arithmetic carrier.

Let g define one of the coefficient contacts, and let u be an invertible
coefficient multiplier on its chart, with inverse in the same declared
regularity class. To obtain maps on the global source complexes require
u and u^-1 in its coefficient unitization. Replace g by u g. There is
an actual chain isomorphism

    C_(ug) -> C_g,       degree-zero map L_u,
                         degree-one map identity.

The equation g u=u g verifies the chain identity; the inverse uses u^-1.
For successive units the maps compose by their ordinary product, so the
triple comparison is exact. If units exist only locally, this statement
is a chart comparison, not an unproved global extension of those units.

A degree-one endomorphism represented by v for C_(ug) transforms under
this isomorphism to v/u for C_g. Therefore the local trace transforms as

    residue( v dt/(u g))=residue( (v/u) dt/g).

This is why the dualizing principal part dt/g must transform as well as
the coefficient jet. Simply applying the same top-coefficient functional
to v in both presentations would not be invariant.

For a second contact Q, pass to E_Q and write N_Q(u)=det(M_u|E_Q).
It is an invertible coefficient since u is a unit on that finite module.
The determinant sections satisfy

    det(M_(u g))=N_Q(u) det(M_g).

Meanwhile the induced map on the line
L=det(target) tensor det(source)^-1 multiplies its displayed basis by
N_Q(u)^-1, because the chain map is u on the source and identity on
the target. It consequently sends the section for ug to the section
for g. This proves independence of the section AS A SECTION OF ITS
COMPARED LINE, including the necessary nontrivial transition factor.
The formula is valid for smooth units using their finite jets; a global
polynomial expression for u is not required.

The same calculation determines a necessary metric law. If ell_g denotes
the source/target basis ratio in this presentation, an isometric
comparison requires

    ||ell_(ug)||_(ug)=|N_Q(u)|^-1 ||ell_g||_g.

Thus assigning unit norm to every such basis generally violates the
comparison. This equation is a compatibility requirement, not a choice
of the arithmetic metric or a proof that the intrinsic metric satisfies
it.

Coordinate changes have a similarly explicit residue comparison.
Locally write t=phi(s), phi(0)=0 and phi'(0)=c invertible, with a specified
smooth inverse in the coefficient chart. Taylor jets give an isomorphism
R[t]/t^m -> R[s]/s^m; its matrix is triangular in monomial bases and has
 determinant c^(m(m-1)/2). The differential transforms by dt=phi'(s) ds.
For every finite principal part F(t)dt one has

    residue_s(F(phi(s)) phi'(s) ds)=residue_t(F(t)dt).

A formal verification suffices since residues depend on finitely many
Taylor coefficients. For t^k dt with k!=-1 use its formal primitive
 t^(k+1)/(k+1), whose derivative after substitution has zero residue.
For dt/t, write phi(s)=s v(s) with v(0) invertible; then
phi'/phi=1/s+v'/v, and the second term is a power series with no negative
power. This gives residue one. Linearity proves the assertion for all
finite principal parts. No analyticity of the smooth functions is
assumed; their finite jets determine the calculation.

Composition of coordinate substitutions preserves these identities by
the chain rule. Combined with the equation-unit transformation above,
this makes the local supported degree-one residue intrinsic to the
specified dualizing differential, with determinant-line comparisons
under the allowed chart changes. An arbitrary coordinate change is not
claimed to be an automorphism of the crossed lattice action; that global
claim would require equivariance not supplied by this local calculation.

The local transition problem is therefore explicit. What remains for
A.8 is to realize the required global coefficient/line descent and prove
that its Hermitian metric, including these transition factors, equals
the intrinsic periodic ruling metric on the common arithmetic domain.
The local calculation does not supply that missing equality.

## A composition-and-duality prototype on the finite contact algebras

The finite contact algebras support an explicit kernel prototype with
composition and contravariance on the same domain. This construction is
over R=R_theta; it is not an identification of that prototype with the
full arithmetic correspondence category.

For a fixed finite family of monic contact polynomials put A_i=R[t]/P_i.
The residue lambda_i proved above makes A_i a symmetric Frobenius
R-algebra: A_i is finite free over R and a -> lambda_i(a times -) is an
isomorphism A_i -> Hom_R(A_i,R). Symmetry follows from commutativity.
All these maps and their inverses are continuous finite matrices over R.

Declare a kernel from i to j to be an A_i-A_j bimodule M which is finite
projective on both individual sides. In particular it is finite
projective over R. Use the direct-summand topology supplied by its finite
projective presentations; any two presentations give the same topology
because their comparison matrices are continuous. Morphisms are bimodule
maps. Allow bounded complexes of these kernels, finite sums and direct
summands. The diagonal unit at i is A_i itself.

For M from i to j and N from j to k, set

    M star N=M tensor_(A_j) N,

with the completed balanced tensor topology and the usual total complex
on bounded complexes. This tensor is finite projective on the left and
right. For example, a left A_j-projective presentation of N makes the
composite a left A_i-module summand of a finite sum of copies of M;
a right A_j-projective presentation of M proves the right-side assertion.
The same splittings identify the completed tensor with this actual
finite-projective module, so no completion exactness is assumed. They
also show that it computes the derived tensor, since the relevant
one-sided modules are projective. Associativity, unit maps and their
coherence are the canonical balanced-tensor maps. Bounded cones remain
in the declared termwise projective domain.

Define the contravariant dual kernel by

    D(M)=Hom_R(M,R),
    (b phi a)(m)=phi(a m b).

Finite R-projectivity gives continuous biduality. Frobenius duality of
the coefficient algebras identifies D(M) with Hom_(A_j)(M,A_j) for right
modules, and likewise with the left-module dual using A_i. Explicitly,
composition with lambda_j gives the first identification. Its inverse
sends an R-functional phi to the unique A_j-valued functional whose
pairing with each b under lambda_j equals phi(m b); nondegeneracy of
lambda_j proves existence and uniqueness, and also right-linearity.
It follows from the finite one-sided projective presentations that D(M)
is projective on both opposite sides.

The right-module adjunction now gives the actual anti-composition map

    D(M star N) ~= D(N) tensor_(A_j) D(M).

One may verify it by choosing finite right-module dual bases: the right
adjoint to - tensor M is - tensor Hom_(A_j)(M,A_j), its evaluation and
coevaluation satisfy the two triangle identities on those bases, and
the right adjoint of two composed tensor functors is their reversed
composition. Under the Frobenius identifications these are the displayed
D kernels. This verification also proves coherence: both maps for three
factors are the adjoint comparison of the same three tensor functors.
The unit comparison D(A_i)~=A_i is precisely lambda_i. The symmetric
Frobenius identifications agree with R-biduality, so the double dual is
the original kernel, with its canonical bidual map. On bounded complexes
use the dual differential signs already specified above. These are
contravariant maps on kernel morphisms, not an opposite-algebra notation.

There is a nonempty trace-class ideal within this prototype. Require
an i-to-i kernel to be a bounded complex of finite projective modules
over A_i tensor_R A_i^op. Its derived diagonal shadow is then

    A_i tensor^L_(A_i tensor A_i^op) M,

a bounded complex of finite projective R-modules. For a free enveloping
module this is A_i, and finite summands and bounded complexes prove the
assertion generally. Composing an enveloping-projective kernel with a
kernel projective on both sides preserves enveloping projectivity:
reduce the first to an outer free module and use the appropriate
one-sided projective presentation of the second. The analogous argument
works on the other side. R-duality also preserves this ideal because
the enveloping algebra is itself a finite symmetric Frobenius R-algebra.
Thus this gives an actual finite-perfect diagonal domain compatible with
the declared composition. It does not claim that every unit A_i has a
perfect enveloping resolution; nilpotent contact algebras may have higher
Hochschild classes in arbitrarily many degrees.

The prototype proves a joint composition/duality statement for kernels
on these finite contact algebras, with an explicitly limited finite
shadow domain. It does not include all ambient maps between contact
modules of different lengths as projective bimodule kernels, nor supply
an equivalence with the localized source correspondences. In particular
it cannot replace that category merely because these identities hold.
The required source realization, full geometric trace comparison and
intrinsic metric remain unproved parts of A.

## The source realization requires the full dg endomorphism algebra

There is an exact source comparison for the subcategory generated by a
finite contact family, but its coefficient algebra is derived. Let
C=direct_sum_i C_i be the actual bounded finite-free right B complexes
of that family and set

    E=Hom_B^bullet(C,C),
    differential(x)=d_C x-(-1)^degree(x) x d_C.

Composition is the original source matrix composition. In every degree
E is a finite sum of copies of B; its differential and multiplication
are continuous. For the normalized finite family, the identity-label
subalgebra includes into E by a unital dg algebra quasi-isomorphism:
the pairwise nonidentity contractions proved above show acyclicity of
the complementary chain spaces. The complement need not be an ideal,
and no quotient-algebra assertion is used.

For a single order-m contact,

    H^0(E)=J_m,          H^1(E)=J_m,          H^j(E)=0 otherwise.

In particular E cannot be replaced by the ordinary algebra J_m via a
quasi-isomorphism: its degree-one group is nonzero and contains the
residue-detected extension classes. Nor has formality of E been proved.
The finite Frobenius-kernel prototype above therefore cannot be called
a source realization just by identifying its coefficient algebra with
H^0(E). It would omit precisely this supported derived information.

The actual realization is given by the dg Yoneda functor

    F(X)=Hom_B^bullet(C,X),

with right E action by precomposition. On the subcategory generated
from C by finitely many shifts, sums and mapping cones, F takes values
in finite-cell right E-modules: F(C)=E, and Hom from C commutes with
these finite operations. It is fully faithful on Hom cohomology. Here
is a direct proof of the required comparison. For X=C, the map

    Hom_B^bullet(C,Y) -> Hom_E^bullet(E,F(Y))

is the identity under evaluation at 1, for every Y. The class of X for
which the comparison is a quasi-isomorphism for all such Y is closed
under shifts, finite sums and cones, since both mapping complexes turn
these finite operations into the corresponding complexes and the
comparison respects their differentials. Induction proves the assertion.
Every finite-cell E-module is obtained from E by the same operations;
its attaching maps lift, up to chain homotopy, by this full faithfulness.
Thus the functor is essentially onto that finite-cell homotopy category.
Adjoining homotopy direct summands on both sides extends the equivalence
to their explicitly idempotent-completed categories.

This proves a genuine derived comparison with a category generated by
actual source contacts. It is not the introduction of unrelated finite
jet objects. Since every C_i becomes contractible over the scalar lattice
quotient, every finite-cone object in this comparison remains relative
to that quotient. The Hom comparison maps are continuous on the finite
source constructions. No general Hausdorff topology on all homotopy
quotients after arbitrary cones, or on an infinite derived completion,
is inferred from the algebraic quasi-isomorphism assertion.

There is also a precise algebraic kernel-transport formula indicating
what a further correspondence realization would require. Put
C^vee=Hom_B^bullet(C,B). Finite projectivity over B gives the rank-one
operator isomorphism of complexes

    C tensor_B C^vee ~= E.

Consequently the algebraic derived transport of an E-bimodule M is

    Phi(M)=C^vee tensor_E^L M tensor_E^L C.

Reassociation and the preceding isomorphism give
Phi(M) tensor_B^L Phi(N) ~= Phi(M tensor_E^L N). Its unit is the
idempotent kernel Pi=C^vee tensor_E^L C, not automatically B. In fact
Pi cannot be the full source unit: its derived reduction to the scalar
lattice quotient on both sides vanishes because the corresponding
reductions of C and C^vee are contractible. The reduction of B does not
vanish; L tensor_B^L L has degree-zero homology L.

These last tensor statements are explicitly ALGEBRAIC derived statements.
The E-side resolutions and their completed topological tensor estimates
have not been supplied, so they are not a proof of continuous kernel
transport in the completed category. They also exhibit the missing
full unit: a contact-supported kernel projector cannot replace the
arithmetic diagonal. Thus the source dg realization is established on
the finite generated contact sector, while continuous kernel transport,
its extension beyond the relative projector and the metric comparison
remain part of the full A task.

## Continuous full-unit transport with the source and contacts together

The preceding contact-only projector is not needed if the full source
unit is retained in the generator. This yields an explicit completed
Morita context, without replacing the source by its relative subcategory.
Set

    X=B direct_sum C,
    Bhat=Hom_B^bullet(X,X),

where C is the fixed finite direct sum of source contact complexes and
B occupies degree zero. Let e be the projection onto that B summand.
It is a closed degree-zero idempotent, and e Bhat e=B. The complementary
closed corner (1-e) Bhat (1-e) is precisely the full contact dg algebra
E above, including its degree-one extensions. The off-diagonal corners
are the actual complexes C and C^vee, not discarded formal entries.

Identify X=Bhat e and X^vee=e Bhat, with their dg module structures.
All spaces are finite graded sums of copies of B and the differentials
are continuous matrices. The rank-one operator map gives a continuous
isomorphism of dg Bhat-bimodules

    X tensorhat_B X^vee -> Bhat,
    x tensor phi -> [y -> x phi(y)].

On homogeneous coordinates use the standard graded dual convention.
Finite homogeneous bases of X over B give its inverse by a finite sum
of matrix entries and dual basis vectors. This inverse is continuous;
the rank-one map intertwines differentials by the Hom-complex Leibniz
identity, so its inverse is a chain map as well.

The other evaluation is a continuous dg B-bimodule isomorphism

    X^vee tensorhat_Bhat X -> B.

For an explicit inverse choose the closed degree-zero vectors x_0 and
phi_0 furnished by the B summand, with phi_0(x_0)=1. Send b to
b phi_0 tensor x_0. Balancing by the rank-one operator x phi_0 shows
that phi tensor x reduces to phi(x) phi_0 tensor x_0, with the graded
conventions of the evaluation. Thus both inverse identities already
hold on elementary tensors and extend to the completed quotient. The
maps use finite sums and continuous multiplication, not a convergent
infinite frame or an unspecified E-side bar resolution.

Consequently the functors on complete unital dg bimodules

    L(M)=X tensorhat_B M tensorhat_B X^vee,
    R(N)=X^vee tensorhat_Bhat N tensorhat_Bhat X

are mutually inverse, and their tensor comparisons are the actual maps
induced by these evaluations. In particular

    L(M) tensorhat_Bhat L(M') ~= L(M tensorhat_B M'),
    L(B)=Bhat.

Associativity and unit diagrams commute by reassociation and the two
rank-one evaluation identities. This preserves the FULL SOURCE UNIT;
it makes no assertion that the contact corner alone has become full.

The same comparisons apply to the explicit underlying relative derived
models from the source, rather than relying on an arbitrary dg bar
completion. On the B sides, X and X^vee are bounded complexes of finite
projective modules, hence their tensor operations preserve underlying
split acyclic complexes by the finite bounded-complex argument. On the
Bhat sides, Bhat e and e Bhat are summands of the free dg module cut out
by a closed idempotent. Taking such a corner preserves an underlying
contracting homotopy: restrict it as e h e, which contracts because the
differential commutes with e. Thus these transport functors preserve
the declared relative weak equivalences. Applying them to the existing
source tensor models gives the derived comparison with the same units
and continuous evaluation maps. No unrestricted infinite-totalization
claim for all dg algebras is involved.

This is a continuous source enlargement containing the full unit and
all the chosen contact complexes with their extension information, and
it supplies the completed kernel-transport comparison missing from the
contact-only algebraic construction. It is Morita equivalent to the
existing source by construction; it does not by itself add geometric
localization or proper pushforward hypotheses. In particular the
Frobenius duality for the ordinary finite jet algebras cannot simply be
transported as a duality of Bhat-bimodule kernels: its comparison with
the full dg algebra and the source tensor remains unproved. The global
shadow, ruling plane and intrinsic metric requirements of A are also
not consequences of the full-unit Morita context.

## An orbit-saturated contact that is an actual source bimodule complex

The single-box right-module contacts do not carry the standard left
source action. Indeed gB need not be a two-sided ideal: for a nontrivial
gamma moving its valuation box, alpha_gamma(g) is 1 on its zero set,
so U_gamma g does not belong to gB. The earlier identity
 g+f alpha_gamma(g)=1 even shows that the two-sided ideal generated by
g is the whole unitized algebra. Hence imposing this single-box equation
on both standard source actions would erase the object. Orbit saturation
is necessary for a bimodule construction of this kind.

Here is an explicit saturated construction for the one-prime source
P={p}. Put a=log p, x=p^j u on its open finite-place locus, and
s=t-ja. Choose a smooth r(s) equal to s^m near zero, positive elsewhere,
and equal to 1 for |s| large, with m positive even. Define the actual
function

    G(t,p^j u)=r(t-ja),       G(t,0)=1.

It is continuous at x=0: on bounded t-intervals, j tending to positive
infinity puts s outside the support of r-1. It is invariant under the
original simultaneous p-scaling, since that sends (t,j) to (t+a,j+1).
The function need not belong to the coefficient unitization; it is used
as a multiplier on the nonunital source, not falsely as an element of B.

This multiplier is continuous on the declared coefficient algebra E_R
tensorhat E_p. For H=1-G, its support satisfies |t-ja|<=R_0. Multiplying
any coefficient f by H gives an element of E_R tensorhat F_p, since its
value at x=0 is zero and on that support

    p^(N|j|)<=C_N exp(N|t|).

All real derivatives of H in the translated s variable are bounded,
and H has trivial unit character. Thus each requested real derivative,
unit Fourier weight and shell weight of Hf is bounded by stronger real
decay/derivative seminorms of f. To sum over j, take one further real
exponential weight: on the support it supplies a summable factor
exp(-|j|a), up to a fixed constant. These estimates prove continuity in
the completed tensor topology. Since Gf=f-Hf, multiplication by G is
continuous too. Coefficientwise extension preserves rapid lattice
weights, and invariance of G makes the operator central on A=A_sm({p}).
It commutes with both actions of B=A_sm^u({p}) on its ideal A.

The multiplier has a closed image on A. At the coefficient level its
image is precisely the kernel of the m orbit-jet maps

    f -> (partial_t^l f(ja,p^j u))_(j in Z),  0<=l<m.

Their targets are rapidly weighted shell sequences of S(Z_p^*) jets.
The same support/weight estimates give continuity. They are onto that
sequence space: lift a sequence of Taylor coefficients using fixed
compact bumps in s=t-ja and their monomials, with the prescribed shell
index. The rapid shell bounds absorb every real translation weight.
On the joint jet kernel, divide by s^m near zero using Taylor's integral
remainder, and by the fixed nonzero r away from zero. The uniform
translated-chart estimates above prove continuity of division on that
kernel. Extend these maps coefficientwise in the independent crossed
label to obtain a continuous split quotient and closed image on A.
Injectivity follows because the zero set has empty interior.

Consequently

    K_G=[A --multiply G--> A],       degrees -1,0,

is an actual complex of B-bimodules, with nonzero Hausdorff quotient
cohomology in degree zero. The quotient retains the orbit jets with
both their shell and crossed-label coordinates; these are not silently
replaced by scalar multiplicities. Geometrically its support is the
entire invariant orbit hypersurface s=0, not a single noninvariant box.

There is also a concrete derived self-composition. P123.124 proves
A tensorhat_B^L A ~= A on this common source, with one-sided relative
projectivity. Centrality of G makes that multiplication comparison
intertwine the multipliers in both tensor factors. Thus

    K_G tensorhat_B^L K_G

is represented by the two-generator Koszul complex on (G,G), with terms
A, A direct_sum A, A in degrees -2,-1,0. Replacing the two generators
by their first generator and their difference is an invertible constant
change of exterior basis, and turns the sequence into (G,0). Hence

    K_G tensorhat_B^L K_G ~= K_G direct_sum K_G[1].

All basis changes are finite continuous matrices and preserve the two
source actions. This keeps the nonzero derived self-intersection term;
it does not assert idempotence of the contact kernel or discard its Tor.
The comparison uses precisely the previously proved relative tensor
domain, rather than a scalar analogy with jets.

This supplies a nonzero, separated source BIMODULE contact and its
self-composition in one semilocal source. It is not the unit B, does not
provide duality for all kernels, and has not been extended across the
full set of arithmetic strata or compared with the intrinsic metric.
The one-prime scope and the use of a central multiplier on A are part
of the construction and must not be broadened without further proof.

## Saturated contact bimodules for every fixed finite prime set

The saturated multiplier construction extends to any fixed finite set
P. On the open finite-place stratum put

    s=t-sum_(p in P) j_p log p,
    G_P(t,(p^j_p u_p))=r(s),

and set G_P=1 whenever some finite coordinate is zero. The same real
profile r is 1 outside a compact interval and has its only zero at 0
of even finite order m. Simultaneous lattice scaling leaves s invariant,
so G_P is invariant under Gamma_P. It is continuous at every finite
zero stratum: near a point with zero coordinates their valuations tend
to positive infinity, while the remaining nonzero-coordinate valuations
and t stay locally bounded. Hence s tends to negative infinity and r=1.

The required multiplier estimate retains mixed positive and negative
valuations. Set L_+=sum log(p)max(j_p,0) and
L_-=sum log(p)max(-j_p,0). On the support of H_P=1-G_P,

    |t-L_++L_-|<=R_0,
    L_++L_-<=|t|+R_0+2L_-.

Therefore every requested two-sided shell weight for H_P f is absorbed
by a stronger real exponential weight and stronger negative-valuation
weights for f. The latter are available in every E_p, even though its
chi_p summand does not decay at positive valuations. All real derivatives
of H_P are uniformly bounded and its unit Fourier character is trivial.
Increasing these weights further gives a summable factor in every j_p,
so the coefficientwise pointwise estimates extend to the weighted
projective tensor seminorms. In particular H_P f belongs continuously
to E_R tensorhat product_p F_p, the full open-stratum ideal. Thus G_P
acts continuously on the common coefficient algebra and, by invariance,
centrally on A_P=A_sm(P), commuting with both B_P=A_sm^u(P) actions.

The orbit-jet quotient is also explicit. Evaluate real derivatives of
orders below m at t=sum j_p log p in each valuation cell, using the
straightened unit coordinates v from the deck calculation. The above
inequality on s=0 bounds every rapid j weight by stronger real and
negative-valuation seminorms of the source. Hence these maps have as
target rapid Z^P sequences of S(U_P)-valued m-jets. A continuous section
uses fixed compact real bumps in s and the prescribed polynomial jets
cell by cell; arbitrary rapid j decay absorbs the real shifts. Division
on their joint kernel uses the same fixed Taylor remainder in s and
the nonzero profile away from zero. Its estimates are uniform in j
by the displayed weight inequality. Adding the independent rapid
crossed labels preserves all these continuous maps.

It follows that multiplication by G_P is injective with closed image
and nonzero quotient, and

    K_P=[A_P --G_P--> A_P]

in degrees -1,0 is an actual B_P-bimodule complex. On every closed locus
with at least one finite zero coordinate its restriction is the identity
differential, so that restriction is contractible. Its nontrivial
support is the invariant open-stratum hypersurface s=0, with the
specified transverse and orbit jets. It is therefore compatible with
restriction to the existing zero filtration in this precise sense.

Since P123.124 supplies A_P tensorhat_(B_P)^L A_P ~= A_P, centrality and
the same constant Koszul basis change give

    K_P tensorhat_(B_P)^L K_P ~= K_P direct_sum K_P[1].

Thus the continuous bimodule contact and its derived excess are
constructed for every fixed finite P, not only for one prime.

There is, however, an explicit distinction between fixed-P existence
and compatibility with the prescribed added-prime maps. If T=P union
{ell}, the source embedding multiplies by chi_ell, but

    s_T=s_P-j_ell log ell.

On a shell j_ell>0 contained in chi_ell one obtains
G_T j_(P,T)(f)=r(s_P-j_ell log ell) j_(P,T)(f), whereas
j_(P,T)(G_P f)=r(s_P) j_(P,T)(f). These generally differ, already at
s_P=0. The two contact equations therefore do NOT intertwine under the
naive coefficient embedding. On the new unit shell j_ell=0 they do
agree, but replacing chi_ell by that smaller shell would change the
specified semilocal transition and is not adopted here.

This records both the completed multi-prime construction and its actual
transition defect. An equivariant lift or derived comparison incorporating
that defect remains required for global A; the existence of K_P for each
P does not prove a compatible global correspondence. No global duality
or intrinsic metric comparison is inferred.

## An explicit equivariant orbit lift for an added prime

The failed scalar equation comparison has a constructive orbit-family
replacement. It retains the prescribed old coefficient embedding but
enlarges the lifted OBJECT to include all translates, rather than claiming
that the single new saturated contact equals the old one.

Fix T=P union {ell}. Let C be the coefficient-enlarged old-lattice algebra
of P123.123 and C_0 its nonunital ideal with coefficients
E_R tensorhat (tensor_(p in P) E_p) tensorhat E_ell. The added action alpha
of ell preserves C_0. Put b=log ell. For n in Z define the multiplier

    G_n=r(s_P-n b)

on the old open finite-place stratum, extended as 1 on old zero strata.
It ignores the new finite coordinate. Each G_n is a continuous central
multiplier on C_0 relative to its two C actions, since the old lattice
preserves s_P. Its estimates have at most exponential growth in |n|:
in the previous support estimate replace R_0 by R_0+|n|b. Thus each
requested seminorm is bounded by a fixed stronger seminorm times
C exp(M|n|), with constants independent of n.

Define the complete bimodule

    M=Rapid_Z(C_0),
    seminorms sum_n exp(k|n|) nu(m_n) for every k,nu,

and the differential T_G(m)_n=G_n m_n. The preceding bounds prove that
this differential is continuous. Its commutation with both C actions
makes [M --T_G--> M] a C-bimodule complex. Give M the added-lattice
representation

    (rho_h m)_n=alpha^h(m_(n-h)),       h in Z.

It is semilinear for alpha^h on both C sides and tempered: translating
n costs exp(k|h|), and the coefficient action costs the already proved
exponential lattice weight. Since ell is a unit at every old finite
prime, its inverse pullback shifts s_P by -b. Hence

    alpha^h(G_(n-h))=G_n,

including on the old zero strata. This proves rho_h T_G=T_G rho_h.
The orbit-family contact therefore has a specified tempered equivariant
structure, with all topological estimates needed by P123.123.

Crossing this complex with the added Z action produces an actual
B_T-bimodule complex by that note's formulas. Its composition comparison
with other declared equivariant objects is the strong tensor comparison
of P123.123, because all its equivariance hypotheses have now been
constructed explicitly for this object. No naive induction equivalence
B_T tensor_(B_P)^L B_T~=B_T is invoked.

The old contact embeds at n=0 before crossing: on coefficients use the
unchanged map f -> f chi_ell, and put all other orbit indices equal to
zero. This is a continuous map of the old bimodule complexes because
G_0 j(f)=j(G_P f). Its translates are present at the other indices.
The n=0 summand alone is not invariant under rho; the whole rapid family
is the equivariant object. In particular the construction preserves old
contact data instead of claiming equality with the different multiplier
r(s_P-j_ell log ell) on every new valuation shell.

The underlying orbit-family cokernel is nonzero: a coefficient with a
nonzero contact jet in one chosen orbit index cannot be in the image
of the diagonal multiplier. Quotient models and continuous jet lifts
can be made with estimates exponential in |n|, by translating the fixed
Taylor cutoffs. Increasing the orbit seminorm absorbs that cost, so the
underlying complex has closed image and a continuous quotient model in
the same rapid completion. Crossing retains this coefficientwise model
as a complex of topological vector spaces, with nonzero cohomology.

For several added primes use n in Z^d, replace n b by sum n_i log ell_i,
and use (rho_h m)_n=alpha_h(m_(n-h)). The weight estimates use ||n||_1,
and the identity alpha_h(G_(n-h))=G_n still holds. Reordering added
primes permutes the indices and commutes with these maps. Thus there
is a coherent simultaneous orbit lift for any fixed finite added set.
This does not assert that successive coefficient lifts are identical
to every full direct lift without their specified coefficient maps.

The result supplies explicit equivariant contact OBJECTS for the
semilocal composition repair. It does not turn the orbit family into a
single scalar contact, prove a finite determinant for its entire rapid
orbit cokernel, or construct its required contravariant kernel duality.
Those comparisons and the intrinsic metric remain necessary for A.

## The equivariant orbit algebra is a rapid matrix stabilization

The orbit lift has a concrete crossed-algebra description which removes
an apparent independent infinity of translated copies. This is an
additional algebra structure on its underlying coefficient space, not
an identification with the original full B_T algebra. Give
M=Rapid_(Z^d)(C_0) pointwise multiplication in the orbit index. Its action
rho_h(m)_n=alpha_h(m_(n-h)) is an algebra automorphism, tempered in the
previous seminorms. Form its rapid crossed algebra D_orb=M crossed Z^d.
An element has coefficients a_(n,h) in C_0, with all exponential weights
in n,h. Define the matrix

    A_(n,k)=alpha_(-n)(a_(n,n-k)).

The inverse is a_(n,h)=alpha_n(A_(n,n-h)). Both are continuous: the
change of indices has equivalent exponential weights, and alpha_n costs
only another exponential n weight. Thus the map is a topological
isomorphism onto the algebra of rapidly decreasing Z^d by Z^d matrices
with entries in C_0 and its original coefficient seminorms.

It respects multiplication exactly. In the crossed product the term
with first label h multiplies a_(n,h) by alpha_h(b_(n-h,l)). Applying
alpha_(-n) gives A_(n,n-h) B_(n-h,n-h-l), the corresponding matrix
product entry. Absolute rapid summation justifies every regrouping.
The source involution likewise becomes matrix transpose with the C_0
involution. Hence this is an algebra isomorphism with the actual rapid
matrix completion, not just a bijection of indices.

The contact multiplier is also transported exactly. Since
G_n=alpha_n(G_0), applying alpha_(-n) to G_n a_(n,h) gives
G_0 A_(n,k). Thus the orbit contact complex after crossing, viewed with
this coefficient algebra structure, is the rapid matrix stabilization
of

    [C_0 --G_0--> C_0].

Its contact equation is the original one on each matrix entry. This
does not make D_orb equal to B_T: its natural B_T-bimodule actions are
additional structure, and the n=0 old embedding becomes a matrix corner
rather than an algebra isomorphism onto the whole B_T source.

A continuous matrix trace comparison is available without presuming
that C_0 has an idempotent unit. The sum

    tr_mat(A)=sum_n A_(n,n)

converges in C_0 by the rapid estimates. For A,B its difference on
products is

    tr_mat(AB)-tr_mat(BA)=sum_(n,k)[A_(n,k),B_(k,n)].

The corresponding sum A_(n,k) tensor B_(k,n) converges in
C_0 tensorhat C_0, so this difference is an actual continuous Hochschild
boundary. Therefore tr_mat induces a cyclic comparison to the completed
zeroth source shadow of C_0. It commutes with multiplication by G_0,
with the real derivative, and with any already justified cyclic trace
on C_0. No scalar trace of the infinite matrix identity is introduced.

The map putting x in the (0,0) entry is a continuous right inverse of
tr_mat as a linear map. Its corner product is the original C_0 product.
If a full Morita assertion is desired, the nonunital firm tensor domains
and their evaluation maps must still be specified; the existence of
an actual idempotent E_00 tensor 1 in D_orb is not presumed. These
explicit matrix and trace comparisons already show how the translated
family is organized after crossing while retaining its source domain.
They do not prove finite-dimensional cohomology of C_0, a determinant
metric, or a contravariant duality for all B_T-bimodule kernels.

## Nonunital Morita evaluation for the orbit stabilization

The rapid matrix comparison admits actual firm Morita evaluations.
First C_0 has a continuous right-linear splitting h of its multiplication
C_0 tensorhat C_0 -> C_0, by the coefficient partition construction of
P123.124. That construction also applies to the coefficient-enlarged
old-lattice algebra: its coefficient cutoffs are unchanged, its lattice
labels are only a subgroup of the full labels, and the same tempered
weight estimates bound all terms. In particular

    h(ab)=h(a)b,                multiplication(h(a))=a.

After balancing over C_0, these identities give
h(ab)=a tensor b: move the second factor of each term of h(a) across
the balancing relation and sum. Therefore multiplication is an actual
topological isomorphism

    C_0 tensorhat_(C_0) C_0 ~= C_0.

No unit or idempotent in C_0 has been presumed.

Let D be its rapid matrix algebra indexed by Z^d. Let P_col be rapid
columns of C_0, a D-C_0 bimodule, and Q_row rapid rows, a C_0-D bimodule.
Outer multiplication gives

    P_col tensorhat_(C_0) Q_row ~= D.

Indeed the rapid sequence tensor identification is the weighted double
sequence identification, and multiplication on the coefficient factors
is the preceding balanced isomorphism. The inverse applies h to each
matrix coefficient and puts its factors in the corresponding column
and row. The finite seminorm loss of h is absorbed in the coefficient
seminorm; the rapid index weights bound the completed sum.

The dot-product evaluation gives the other topological isomorphism

    Q_row tensorhat_D P_col ~= C_0.

An inverse sends x, with h(x)=sum x_1 tensor x_2, to
sum row_0(x_1) tensor column_0(x_2). To check the inverse on general
positions, factor b by h and balance through the actual matrix entries:

    row_i(a) tensor column_j(b_1 b_2)
      =row_i(a) E_(j,0)(b_1) tensor column_0(b_2)
      =delta_(i,j) row_0(a b_1) tensor column_0(b_2).

Summation and the C_0 balancing identity reduce this to the inverse
image of delta_(i,j)ab. All series converge in the projective quotient
seminorms by rapid decay and the continuity of h. This verifies both
inverse identities without using E_(i,j)(1) as an element of D.

Thus unitality is replaced by the stated firm module condition, and the
usual transport between complete firm C_0-bimodules and complete firm
D-bimodules is defined by these actual row/column tensors. Its inverse,
composition and unit comparisons are the displayed evaluations;
associativity follows on elementary tensors and then by continuity.
Central multiplication by G_0 commutes with both evaluations. Hence the
stabilized contact complex transports back to [C_0 --G_0--> C_0] on this
firm domain. This does not equate D with B_T or remove its additional
B_T actions.

There is also an explicit degree-zero shadow homotopy. Write
h(A_ij)=sum a tensor b and define a continuous map into D tensorhat D by
summing, for every i,j,

    E_(i,0)(a) tensor E_(0,j)(b)
       -delta_(i,j) E_(0,0)(a) tensor E_(0,0)(b).

For the Hochschild boundary b(X tensor Y)=XY-YX its value is

    A-E_(0,0)(tr_mat(A)).

The two reversed coefficient products cancel, so this identity remains
valid for noncommutative C_0. Continuity follows from h and the rapid
double matrix weights. Together with tr_mat E_(0,0)=identity and the
previous trace-of-commutator formula, this proves a topological
isomorphism of degree-zero Hochschild quotients, and also of their
Hausdorff separated versions obtained by closing boundary images.
It does not assert closedness of the C_0 boundary image where that has
not independently been proved.

These are the missing nonunital evaluations and shadow comparisons for
the orbit stabilization. Derived exact structures beyond these firm
completed tensors, the full arithmetic kernel dagger and the metric
comparison are not inferred from this degree-zero Morita calculation.

## The full-unit inclusion constrains the missing kernel duality

There is a necessary compatibility test for any attempt to transport a
firm-local duality into the full source. Let A=A_sm(P) and B=A_sm^u(P),
with P nonempty. As B-bimodules there is a nonzero inclusion A -> B,
but

    Hom_(B-bimod)(B,A)=0.

Here is a proof on the actual source. A bimodule map from B is determined
by its value at 1, which must be central in A relative to B. Write such
a value as sum_gamma a_gamma U_gamma. Commuting it with arbitrary smooth
compact coefficient functions gives, at each label,

    a_gamma(z)(alpha_gamma(f)(z)-f(z))=0.

For gamma!=identity, the lattice action is free on the open stratum.
At every such point there is a compact smooth/locally constant coefficient
f separating that point from its translate. Therefore a_gamma vanishes
on the open stratum, and by continuity and density it vanishes everywhere.
The remaining identity coefficient must be invariant under every prime
lattice generator because the gauge units belong to B.

Its invariance also forces it to vanish. Along positive powers of any
one generator the real coordinate tends to one end of R. Source
coefficients have real exponential decay uniformly in their finite-place
arguments: each E_p has a continuous supremum bound and the completed
coefficient tensor has the corresponding real-weighted supremum bound.
Thus the invariant coefficient tends to zero along that orbit, while
invariance keeps its value constant. The value is zero on every point.
This proves that the required central subspace is zero and establishes
the displayed Hom vanishing.

Consequently a fully faithful contravariant involution on a category
containing these full bimodule Hom spaces cannot simultaneously satisfy

    D(B)~=B,                D(A)~=A.

It would send the nonzero inclusion A -> B to a map B -> A, which must
be zero, contradicting faithfulness. The statement already applies to
objects concentrated in degree zero in the declared relative derived
model: B is relatively free over its enveloping algebra only when that
extra assertion is available, so no derived Hom vanishing is inferred
here merely from the ordinary Hom calculation. The unconditional
obstruction is to the stated bimodule-category extension; a derived
dagger could instead change the dual object or its degrees.

This pinpoints a missing datum rather than ruling out A.4. A duality
local to the firm ideal may take its local unit to itself, but the full
source dual must account for how that ideal sits inside B. One must
construct a different dual extension object, or a justified derived
normalization with its boundary terms, and prove its comparison maps.
Transporting the local self-duality unchanged while retaining all the
full-unit inclusion maps is not valid. No claim that opposite modules
or a formal matrix transpose has solved this extension problem is made.

## The one-sided dual ideal and its explicit boundary extension

The inclusion obstruction can be resolved at the level of computing the
one-sided derived dual, without falsely identifying it with A. Let
L=B/A be the actual scalar lattice quotient and put

    T=Hom_(right B,continuous)(A,B),

with uniform convergence on bounded subsets of A. Every element of T
actually has image in A. Indeed if pi:B -> L is the quotient, then
pi(T(ab))=pi(T(a)b)=0 for a,b in A. The continuous multiplication
splitting h:A -> A tensorhat A expresses every element as a convergent
sum of such products, so pi T=0. Thus T is the space of continuous
right B-linear left multipliers of A with values in A. It is not
assumed that each has a continuous right-multiplier partner.

The bimodule actions on this dual are

    (b T c)(a)=b T(ca).

They are well-defined for fixed b,c; precomposition and postcomposition
are continuous in the bounded-convergence topology. No jointly continuous
evaluation T tensorhat A -> B or internal-Hom theorem is inferred from
that fixed-map continuity. Restriction of endomorphisms of the free
right B-module B gives the actual dual inclusion

    B -> T,              b -> [a -> ba].

It is injective: A has zero right annihilator in B. To check that last
assertion, a nonzero crossed coefficient of b is nonzero at an open
point, and multiplication by a compact identity-label coefficient
supported at the appropriate translated point makes the corresponding
coefficient of ba nonzero. Source continuity extends the pointwise test
to the declared algebra. Thus a nonzero b cannot annihilate every a.

The new dual object is strictly larger than B. The invariant multiplier
G_P constructed above belongs to T, since it acts continuously on A
and commutes with its B actions. It cannot be represented by an element
of B unless its profile r is constant. If it were, comparison on compact
coefficient tests first forces all nonidentity lattice coefficients to
vanish. Its identity coefficient would then be a scalar plus an E_P
function. Along an open lattice orbit the latter decays as the real
coordinate tends to infinity, whereas G_P is the constant r(s) on that
orbit. Different s with different r(s) contradict the same scalar limit.
Therefore the class of G_P in T/B is nonzero.

There is a derived calculation behind this extension. P123.124 supplies
relative projectivity of A as a right B-module, with the continuous
underlying splitting, while B is free and

    0 -> A -> B -> L -> 0

is underlying-linearly split. Thus this is a length-one relative
projective resolution of L. Applying continuous right-module Hom into
B computes its relative derived Hom by the concrete complex

    [B -> T],             degrees 0,1,

with the restriction map just described. Consequently

    Hom_(right B)(L,B)=0,
    Ext^1_rel(L,B)=T/B,
    Ext^j_rel(L,B)=0 for j>=2.

Also RHom_rel(A,B) is T in degree zero, by the same relative projectivity.
These are statements in the specified split exact structure, not in an
unspecified category of all topological modules. The quotient T/B has
its quotient topology, but closedness of B in T, completeness of an
appropriate internal-Hom topology, and Hausdorffness of this Ext quotient
are not asserted here without further proof.

This identifies a nonzero boundary term in the dual of the scalar
quotient, represented explicitly by invariant multiplier classes. The
one-sided dual inclusion is B -> T rather than a nonexistent B -> A,
so it avoids the ordinary bimodule Hom obstruction proved above. It
still does not establish involutive kernel duality: the second dual,
left/right compatibility, completed tensor evaluation and geometric
normalization must be constructed and compared. The calculation supplies
the missing extension candidate and its relative resolution, rather
than declaring that those remaining properties are automatic.

## The bounded-convergence dual quotient loses its boundary topologically

The topology left open above can be decided explicitly. In
T=Hom_(right B,continuous)(A,B) with uniform convergence on bounded
subsets of A, the embedded A is dense. Consequently the nonzero
algebraic quotient T/B is not Hausdorff; its separated quotient is zero.
This rules out using that particular topology as the final boundary
object for A.

Choose smooth real cutoffs eta_R equal to 1 on [-R,R], supported in
[-2R,2R], with derivatives uniformly bounded for R>=1. Let u_R be the
identity-label coefficient

    eta_R(t) product_(p in P) 1_(p^(-R) Z_p),

with integer R. Each u_R belongs to A. Left multiplication by u_R
converges to the identity uniformly on bounded subsets of A. Here are
the needed seminorm facts. The real cutoff error is supported in a
real tail and is bounded by a stronger exponential real seminorm times
exp(-R); its derivatives obey the same estimate after a finite increase
of derivative orders. Each finite cutoff removes only shells j_p<-R;
the error is bounded by a stronger negative-shell weight times p^-R.
It leaves the chi_p zero-value summand unchanged. Finite products of
these estimates cover all coefficient tensor seminorms. Left identity-
label multiplication does not change the crossed labels, so the same
bounds hold in every rapid label seminorm. Taking a supremum on a
bounded subset makes all the stronger source seminorms uniformly finite.
Thus the convergence assertion is in precisely the topology specified.

For any T in that Hom space, its value T(u_R) belongs to A by the
previous image calculation. Right B-linearity gives

    L_(T(u_R))(a)=T(u_R)a=T(u_R a).

Uniform convergence of u_R a to a on bounded subsets, followed by the
fixed continuous map T, therefore proves

    L_(T(u_R)) -> T

in the declared bounded-convergence topology. This proves density of A,
not merely approximation of the one example G_P. In particular B is
dense too, while the multiplier G_P proves B!=T algebraically.

Hence every continuous Hausdorff-valued linear map from T which vanishes
on B vanishes on all T. The quotient T/B carries no nonzero Hausdorff
separated boundary in this topology. The earlier algebraic relative
Ext computation remains valid as a quotient of continuous Hom groups;
it cannot be used as a Hausdorff topological duality object without
changing and justifying the functional-analytic domain.

This is not a proof that arithmetic boundary duality is impossible.
It proves that bounded convergence on the rapid ideal is too weak for
this proposed boundary quotient: it makes cutoffs at infinity converge
to multipliers with nontrivial boundary classes. A successful construction
must specify additional geometric asymptotic control, or a different
supported duality framework, and prove its tensor and bidual properties.
Merely declaring the quotient separated would erase the very boundary
term needed by the inclusion test.

## A separated multiplier extension with declared orbit profiles

There is a concrete stronger topology on a specified subspace of the
multiplier candidate. This does not identify that subspace with the full
continuous Hom dual. Fix P and let Z_0=E_R in the invariant coordinate
s=t-sum j_p log p. Extend h(s), h in Z_0, by zero on every finite zero
stratum. The extension is continuous since s tends to negative infinity
at such a stratum. Let Z=C plus Z_0, with its direct-sum nuclear Frechet
algebra topology. These are actual invariant functions and central
multipliers of A.

The action Z_0 tensorhat E_P -> E_P is jointly continuous, with image
in the open coefficient ideal. To extend the compact-profile estimate,
use everywhere the inequality

    sum_p |j_p|log p <= |t|+|s|+2 sum_p log(p)max(-j_p,0).

A requested shell weight is absorbed by stronger exponential weights
of the real source variable t and of the profile variable s, and by
stronger negative-valuation source weights. Real derivatives use the
finite Leibniz sum. Taking further weights makes the remaining shell
sums geometric. The profile has trivial unit character, so no additional
conductor summation is introduced. This proves the completed tensor
estimate, and not just continuity for each fixed compact profile.

The intersection of E_P and Z as actual functions is zero. An invariant
source coefficient decays along a positive prime orbit by its real
weight, so must vanish; this applies also to a profile with a constant
part. Consequently

    E_ext=E_P direct_sum Z

embeds injectively into the coefficient multipliers. Give it exactly
that direct-sum topology. Its multiplication is the multiplier product:
E_P is an ideal, the mixed product is the continuous action above, and
Z has its usual product. It is therefore a complete nuclear Frechet
algebra. The old lattice action on E_P extends by the identity on Z,
with the same tempered estimates. Define the actual rapid crossed algebra

    B_ext=Rapid_(Gamma_P)(E_ext).

It is again a complete Frechet algebra by those product estimates, and
acts continuously on A on both sides. This action is faithful: testing
with compact coefficients at open points separates every label, and
the coefficient decomposition just proved is injective.

Its vector-space decomposition is

    B_ext=A direct_sum Rapid_(Gamma_P)(Z).

The original B is the closed subalgebra A plus Rapid_(Gamma_P)(C).
Hence the quotient as a B-bimodule is the explicit nonzero Hausdorff
space

    B_ext/B ~= Rapid_(Gamma_P)(Z_0).

The action of the ideal A on this quotient is zero on either side,
because multiplying a profile by A returns to A. The residual scalar
lattice action is the usual rapid label convolution. Thus the extension
keeps an actual boundary profile and its source bimodule actions.

The map B_ext -> T sends a multiplier to its left action on A. It is
continuous for bounded convergence by the joint multiplier estimates,
but its topology is strictly stronger than the topology induced from T.
Indeed the cutoff approximants to a nonconstant invariant profile belong
to A and have zero profile component in B_ext; they cannot converge to
the nonzero profile in its direct-sum topology, although their actions
converge in T as proved above. This explains exactly which information
the stronger topology retains.

The quotient here is NOT asserted to be the previous Ext group T/B
with a repaired topology: it comes from a smaller, explicitly constrained
multiplier algebra with additional asymptotic data. Its admissibility
as an internal dual, its biduality and tensor evaluation, and its
semilocal geometric comparison still require proof. This construction
provides a separated nonzero extension on which those questions can be
posed; it does not establish them by changing the topology alone.

## Geometric recovery and transverse enlargement of the orbit profile

The profile topology can be tied to actual limits of source functions,
and its transverse variables need not be discarded. On the open stratum
use its orbit coordinates (s,v) in R times U_P, already computed by
straightening valuations. Define

    Z_full,0=E_R(s) tensorhat S(U_P),
    Z_full=C direct_sum Z_full,0.

Pull these functions back by the orbit-coordinate map, extending the
nonconstant part by zero on finite zero strata. This extension is
continuous because s tends to negative infinity at each such finite
boundary, uniformly in the unit variables. The pulled-back functions
are invariant under the entire old prime lattice.

They act jointly continuously on E_P, with image in its open ideal
for the nonconstant part. The weight inequality from the scalar-profile
construction is unchanged. In unit Fourier coordinates the straightening
of v introduces only phases depending on valuations; multiplication by
a profile convolves the unit characters. Submultiplicativity of their
conductor weights bounds each requested unit seminorm by the product
of stronger profile and coefficient seminorms. Combining these estimates
with the real/shell inequality and its extra geometric tail weights
proves the completed tensor assertion. Thus the earlier extension also
exists with Z_full in place of its unit-independent subalgebra.

The profile is recovered from functions, not from a chosen decomposition
alone. If F=f+z in E_P direct_sum Z_full, fix an open-stratum point x
and let gamma_N be positive lattice elements with log gamma_N tending
to positive infinity. Real-weighted uniform bounds on f give

    lim_N F(gamma_N x)=z(s(x),v(x)).

The convergence is uniform for x in compact coordinate sets, and it is
independent of the chosen such sequence: f tends to zero by its real
weight, while z is exactly invariant. This proves uniqueness of the
profile as a geometric orbit limit. In particular an invariant element
in the original coefficient algebra is zero, so the displayed sum is
again injective as a space of actual functions.

The orbit limit is multiplicative on this extension. Products of either
remainder with a profile return to E_P, and the product of the profiles
is their ordinary pointwise product. Hence it is precisely the quotient
algebra map to Z_full. It commutes with unit translations and real
translations, using the induced actions on (s,v). It also intertwines
the real derivative: D acts on the profile as partial_s and the
source derivative remainder obeys the same decay estimates.

After rapid crossing, the profile map is coefficientwise with target
Rapid_(Gamma_P)(Z_full). The old lattice acts trivially on these orbit
profiles, so the target multiplication is the corresponding rapid
label convolution with profile products. Its kernel is exactly A, and
the extension of the original B has the separated quotient
Rapid_(Gamma_P)(Z_full,0). No additional quotient of unit characters or
lattice labels is made.

This supplies a geometric interpretation and a larger transverse domain
for the separated multiplier extension. It does not prove that arbitrary
continuous left multipliers admit these orbit limits, or that the
extension represents a categorical internal Hom. Nor is independence
under adding primes established merely by independence of the sequence
inside a fixed prime lattice. Full semilocal profile descent, duality
and the intrinsic metric remain separate requirements.

## Added-prime transitions require separate orbit-face profiles

The prescribed coefficient embedding does not extend to the single-profile
algebras just constructed. This can be decided by two actual orbit
limits, rather than by a choice of topology. Let P be nonempty,
T=P union {ell}, and choose a nonzero compact real profile h(s_P),
independent of unit variables. Its prescribed extension as a function
would be

    F=h(s_P) chi_ell(x_ell).

This is a well-defined continuous coefficient multiplier on E_T: the
old profile acts continuously on E_P, and multiplication by chi_ell
acts continuously on E_ell. It is not, however, an element of
E_T direct_sum Z_full(T).

Choose an open point x with x_ell a unit and h(s_P(x)) nonzero. Along
positive powers of an old p in P, s_P stays fixed and p is a unit at
ell, so

    F(p^n x)=h(s_P(x))  for every n>=0.

Along positive powers of the new ell, the old valuations stay fixed,
s_P increases by n log ell, and chi_ell remains one. Hence

    F(ell^n x)=h(s_P(x)+n log ell) -> 0.

If F=f+z with f in E_T and z a T-invariant profile, real decay would
force f to tend to zero along BOTH sequences, while invariance would
force z to have the same value z(x) along both. The two displayed limits
contradict this. Thus the failure is an actual failure of membership,
not merely a discontinuity of the proposed embedding.

This proves that a compatible profile extension must distinguish
asymptotic directions associated with subsets of the prime lattice.
In particular it cannot assign just one T-invariant limiting function
to every old profile while retaining the prescribed multiplication by
chi_ell. The two limits cannot be reconciled by identifying their classes
without losing the nonzero old profile.

A concrete family of necessary face coefficient algebras is available.
For J subset P, let its nonconstant coefficient space be

    V_(J,P)=(E_R(s_J) tensorhat S(U_J))
                         tensorhat tensor_(p in P minus J) E_p,

where for J empty this is precisely the original E_P. Pull the first
factor back along the J-orbit coordinates and extend it by zero on
zeros in J. These are actual continuous functions and continuous
multipliers of E_P by the estimates already proved. Unitization adds
the same scalar function 1, not an independent scalar at every face.

Each fixed face is preserved by the full prime action: generators in
J fix its profile coordinates, and the others translate s_J and its
unit variables while acting on the remaining E_p factors. Translation
costs only the available exponential profile weights, and the finite
factor actions obey P123.121. Added-prime coefficient maps send an old
face to the face with the SAME J by tensoring its remaining coefficients
with chi_ell. Thus these face-level maps preserve the prescribed old
profile and associate exactly for successive additions.

What has not been constructed is a common completed algebra containing
all these faces with their products, with the original source topology
embedded as required. Products of distinct faces can have overlapping
asymptotics, so simply taking their direct sum would not define that
algebra. Nor would taking an unspecified quotient of a completed tensor
algebra prove preservation of the original coefficient topology. The
face-level construction and the orbit-limit obstruction specify the
next gluing requirement; they do not establish the global duality or
metric comparison of row A.

## Products force joint profiles, already for two primes

For P={p,q}, the sum of the four subset-face coefficient spaces is not
closed under multiplication. This gives a concrete constraint on their
completion. Choose nonnegative compact smooth functions h_p,h_q, with
h_p(0)=1 and h_q=1 on [-log(q)/2,log(q)/2], and consider the permitted
face functions

    F_p=h_p(t-j_p log p) chi_q(x_q),
    F_q=h_q(t-j_q log q) chi_p(x_p).

Their product is nonzero and depends on BOTH indicated real coordinates.
It does not belong to E_P: let j tend to positive infinity, choose k
nearest j log(p)/log(q), and take t=j log p, x_p=p^j, x_q=q^k.
At all these points F_p F_q=1, while t tends to infinity. This violates
the uniform real decay required of every coefficient in E_P.

In fact it cannot be written as a sum of the four allowed face functions.
Suppose it equals F_empty+F_{p}+F_{q}+F_{p,q}, with each term in its
respective V_(J,P). Along simultaneous positive powers of p and q,
both one-face profile coordinates tend to positive infinity, so those
terms and the empty-face source term tend to zero. The full-face term
is exactly invariant under that lattice action. The product also tends
to zero, so this limit forces F_{p,q}=0 on the open stratum, hence as a
continuous function everywhere.

Next take positive powers p^n along a subsequence with p^n tending to
1 in Z_q^*. Such a sequence exists by choosing n divisible by successively
larger finite unit-group orders. The q-face profile and source remainder
tend to zero by real decay; the p-face term tends to its original value,
since its profile is invariant and its remaining q-coordinate returns
to the original point. The product tends to zero, forcing F_{p}=0.
Interchanging p,q forces F_{q}=0. The putative sum would consequently
belong to E_P, contradicting the explicit sequence above.

Thus the joint profile carried by the product is necessary; replacing
it by a single subset-face profile or by a finite sum of such profiles
loses an actual source multiplier. The product itself remains a
continuous multiplier because it is a composition of the two already
bounded multiplier actions. The missing step is its common completion
with the individual faces and original coefficient topology, not its
pointwise existence or continuity of its individual action.

A profile algebra adequate for semilocal descent must therefore retain
simultaneous profile coordinates (here t-j_p log p and t-j_q log q),
including regimes where they stay bounded together while t diverges.
The calculation rules out the subset-direct-sum shortcut. It does not
establish a completed joint-profile algebra or an arithmetic duality by
renaming the product as another face.

## A completed joint-profile algebra and its split semilocal maps

The joint products admit a concrete completion as functions and
multipliers. The construction below does not presume that it induces
the original topology on its embedded source ideal; that last comparison
is explicitly distinguished from the properties proved here.

For each J subset P let U_(J,P)=C plus V_(J,P), with the unitization
and the nuclear Frechet topology of its face coefficient algebra.
There are only finitely many such J. Form

    U_P=tensorhat_(J subset P) U_(J,P).

This is a complete nuclear Frechet algebra with continuous multiplication
and conjugation. Multiplication of the actual face functions defines a
continuous map F_P from U_P to bounded continuous functions on the
coefficient space, with the supremum norm: each face function is bounded
by its defining seminorms. The map extends from elementary tensors by
the projective tensor estimate. Its kernel is a closed algebra ideal.
Define

    JProf_P=U_P/ker(F_P).

It is consequently a complete nuclear Frechet algebra, injectively
realized as actual bounded continuous functions. It contains all face
products, including the two-prime joint product above. Each face acts
jointly continuously on E_P, and iteration over the finite tensor factors
gives a continuous action U_P tensorhat E_P -> E_P. Its kernel contains
ker(F_P), since these functions act pointwise as zero. Therefore the
action descends continuously to JProf_P. In this precise multiplier
sense it preserves the original coefficient algebra and its topology.

The lattice acts on every face with the tempered bounds already proved.
Finite tensoring and quotienting give a tempered action on JProf_P.
Thus its rapid crossed algebra is defined with the same weight method,
and has continuous multiplication and involution. This construction does
not claim an internal duality merely from being a multiplier algebra.

The semilocal embeddings descend through these kernels; this requires
checking their scalar augmentations. On each unitized face use the
existing embedding into the same J-face for T=P union {ell}, tensoring
the nonconstant coefficient with chi_ell and preserving its scalar unit.
Map the other new tensor factors by their units. If z is an elementary
tensor, its represented new function is

    chi_ell F_P(z)+(1-chi_ell) epsilon_P(z),

where epsilon_P is the product of the scalar augmentations. The identity
holds because chi_ell is idempotent. It extends continuously to U_P.
Moreover epsilon_P(z) is the limit of F_P(z) as t tends to positive
infinity with all finite coordinates fixed and nonzero: every nonconstant
face profile then decays. For the completed tensor this follows from
finite-tensor density and the uniform supremum bound. Hence F_P(z)=0
implies epsilon_P(z)=0, and the displayed new function is zero. This
proves descent to a continuous unital map JProf_P -> JProf_T, retaining
the prescribed old source embedding on coefficients of augmentation zero.

These maps have continuous left inverses. Evaluate the new finite
coordinate at zero. A face with ell in J has zero nonconstant limit
there; its factor maps by augmentation. A face with ell notin J maps
by evaluation at zero in its E_ell factor to the corresponding old face.
These continuous factor maps give a map U_T -> U_P, and evaluation of
actual functions shows that it respects the kernels. It descends to
JProf_T -> JProf_P and is a left inverse of the preceding embedding.
Thus the profile-level semilocal embedding is injective with closed
split image. Repeated additions agree because the products of the new
chi factors, scalar augmentations and evaluations commute.

What is NOT proved by this construction is that the injection
E_P -> JProf_P is a topological embedding with closed image. It is
continuous and injective as a map of functions, and the multiplier action
on E_P is continuous, but neither fact supplies the reverse seminorm
bounds. The completed tensor quotient can impose a different subspace
topology on the source. Therefore JProf_P is a completed joint-profile
algebra with coherent split semilocal maps, not yet an admissible
replacement of the coefficient category in A. The source topology
comparison, duality, geometric localization and intrinsic metric remain
requirements rather than consequences of the construction.

## Reverse topology comparisons: one-prime source and a two-prime joint face

For P={p}, the original coefficient topology IS preserved by JProf_P.
There are only the empty face E_P and the full orbit-profile face Z_0.
Expanding their two unitized tensor factors gives

    C plus E_P plus Z_0 plus (E_P tensorhat Z_0).

The last factor multiplies continuously into E_P by the established
profile action. Thus the function map factors through the continuous
linear reduction onto E_P direct_sum (C plus Z_0). This reduction has
a continuous section, given by the two individual factors. The reduced
space is injective as functions, since E_P has no nonzero invariant
coefficient, whereas C plus Z_0 consists of invariant functions.
Consequently the kernel of the original function map is exactly the
kernel of that reduction, and

    JProf_{p} ~= E_{p,common} direct_sum (C plus Z_0)

topologically. In particular the original E_P is a closed subspace
with its unchanged Frechet topology. This proof is specific to the
two-factor situation and does not assume the same reduction for more
primes.

There is a useful joint-face retraction for P={p,q}. Put
H_p=E_R(s_p) tensorhat S(Z_p^*) and H_q analogously, and let

    W=(C plus H_p) tensorhat (C plus H_q).

Define a continuous algebra map on the four tensor factors of U_{p,q}
as follows: use augmentation on the empty and full faces; on the p-face
use evaluation at x_q=0 in its remaining E_q factor; on the q-face use
evaluation at x_p=0. Multiplying these images gives a map U_{p,q}->W.
It descends to JProf_{p,q}; the following geometric argument checks
that it annihilates the function kernel.

Fix s_p,s_q and units u,v. There are positive integers j_N,k_N tending
to infinity with

    j_N log p-k_N log q -> s_q-s_p.

This follows from density of irrational rotation, since log p/log q is
irrational (an integer relation would give equal powers of distinct
primes). Set t_N=j_N log p+s_p and evaluate at
(t_N,p^j_N u,q^k_N v). The two single-face coordinates tend to s_p,s_q.
An empty-face coefficient tends to zero by real decay. A p-face function
tends to its p-profile times evaluation at zero of its E_q coefficient;
the q-face behaves symmetrically. A full-face nonconstant profile tends
to zero, because its real coordinate t_N-j_N log p-k_N log q tends to
negative infinity. Constants remain constants.

These limits give exactly the displayed tensor-factor map, evaluated
as a function on (s_p,u;s_q,v). They extend to completed tensors using
the uniform supremum bounds and density of finite tensors. Therefore a
zero source function has zero image at every such point. The standard
function realization of W is injective (equivalently use the completed
real/unit Fourier tensor realization), so the map respects the kernel.
This proves a continuous algebra map

    beta:JProf_{p,q} -> W.

It has a continuous algebra section: lift the p-profile by multiplying
with chi_q, lift the q-profile by chi_p, and multiply in JProf_{p,q},
preserving their scalar units. Evaluation of the remaining factors at
zero sends both chi functions to 1, so beta composed with this section
is the identity. The joint profile sector W is thus a closed split
subalgebra with its own original tensor topology, rather than a
potentially collapsed image of the function quotient.

The original E_{p,q} lies in ker(beta). This gives one genuine geometric
boundary map but not yet a proof that this kernel is the original source:
other face data remain, including the full invariant profile. Hence
closedness and the reverse source seminorm estimates in the general
multi-prime case remain open. What is established here is the complete
one-prime source comparison and an explicit two-prime joint-face
retraction, both within the previously constructed completion.

## The simultaneous boundary for arbitrarily many primes

The two-prime joint limit has a general version that does not assume
any additional independence of logarithms. For P of size r set

    Sigma_P={ (t-j_p log p)_(p in P) : t real, j in Z^P },
    L_P=closure(Sigma_P) in R^P.

Equivalently rescaling the coordinates by log p identifies L_P with
the inverse image of the closure of the one-parameter subgroup
(t/log p mod 1)_p in the compact torus. This description follows from
the quotient by the lattice product_p log(p) Z, whose quotient map is
open. It is not asserted that this torus closure is always the full
torus.

Every s in L_P can be approximated with t tending to positive infinity
and every j_p tending to positive infinity. Indeed the closure of the
positive tail of a one-parameter subgroup in a compact group equals
its full closure: recurrence to the identity allows any finite-time
approximation to be translated to arbitrarily late times. Lifting the
phase approximations gives t/log p-j_p -> s_p/log p, and t tending to
infinity then forces all j_p to infinity.

Put H_p=E_R(s_p) tensorhat S(Z_p^*) and

    W_P=tensorhat_(p in P)(C plus H_p).

It is a complete nuclear Frechet algebra of bounded continuous functions
on R^P times U_P. Let I_P be the closed ideal of its functions vanishing
on L_P times U_P, and set W_P^acc=W_P/I_P. This is the joint-profile
algebra on the actual accessible limit set, with its quotient topology.
It is well-defined even if L_P is proper.

There is a continuous algebra map JProf_P -> W_P^acc. At the tensor
presentation U_P, retain each singleton-face profile and evaluate all
its remaining finite-place coefficients at zero. Augment the empty
face and every face of size at least two. The resulting map to W_P,
followed by its quotient, respects the function kernel. To see this,
evaluate along an approximating sequence for a point of L_P as above,
with fixed unit coordinates. Singleton profile coordinates tend to their
specified s_p. Every outside finite-place coefficient tends to its
zero value. For a face J of size at least two its real coordinate is

    t-sum_(p in J) j_p log p=(1-|J|)t+sum_(p in J)s_p+o(1),

which tends to negative infinity; its nonconstant profile vanishes.
The empty-face coefficient vanishes by real decay. These limits are
exactly the tensor-factor map. Finite-tensor density and uniform
supremum bounds extend the identity to the completions, proving the
claimed kernel compatibility.

This boundary map has a continuous algebra section. On W_P before
quotient, lift h_p by h_p(s_p,u_p) product_(q!=p)chi_q and preserve units.
One must check that it kills I_P as an actual function, not merely after
applying the boundary map. On open points where all valuations are
nonnegative, its value is w((t-j_p log p)_p,u), which is zero for w in
I_P. If exactly one valuation is negative, only that singleton factor
survives; the value is the corresponding one-factor augmentation
projection of w. That projection is zero: within Sigma_P keep its s_p
fixed while t tends to infinity and the other j_q stay zero, then all
other profile variables tend to infinity and their nonconstant parts
vanish. If at least two valuations are negative, every nonconstant
singleton lift vanishes and the value is the scalar augmentation of w,
also zero by taking t to infinity with every j_p fixed. Continuity and
density of the open stratum give vanishing on finite zero strata too.
Thus the section factors through W_P^acc, and the factorwise zero
evaluations show that its composite with the boundary map is identity.

Therefore the accessible joint boundary is a closed split subalgebra
of JProf_P for every fixed finite P. This gives a general reverse
topology comparison for that boundary sector without a logarithmic
independence hypothesis. It still does not identify the kernel of the
boundary map with E_P: the nonsingleton face sectors remain in that
kernel. The full source topology comparison and arithmetic duality and
metric requirements are not declared solved by this boundary retraction.

## Closed source inclusion for two primes: an explicit remainder projection

For P={p,q}, the source topology comparison can be completed. Write
J=JProf_{p,q} and E=E_{p,q}. There are continuous algebra retractions
R_p,R_q on J: in the tensor presentation retain factors whose face
contains p (respectively q), and augment all other factors. They respect
the function kernel. For R_p, evaluate along p^n with n tending to
infinity through a sequence for which p^n tends to 1 in Z_q^*. The
p-face and full-face functions return to their original values, the
q-face profile vanishes by real decay, and the empty face vanishes.
Continuity in the finite coefficient and uniform supremum bounds give
the same limit on completed tensors. This proves kernel compatibility;
the q case is identical. The factor descriptions imply

    R_p R_q=R_q R_p=R_{p,q}.

Let beta:J -> W=(C plus H_p) tensorhat (C plus H_q) and j:W -> J be
the previously constructed joint-face retraction and section. Define

    H=(1-R_p)(1-R_q),
    Q_E=H-j beta H.

These are initially continuous linear operators on J. The crucial
assertion is that Q_E takes values in E with its ORIGINAL seminorms,
and is continuous into that stronger space.

To prove it, expand the four unitized tensor factors defining U_{p,q}.
There are only finitely many choices of their scalar/nonconstant parts.
Every word containing an empty-face coefficient multiplies continuously
into E by the established multiplier estimates. For such a word H is
identity and beta is zero, so Q_E is that original product.

For words without an empty-face factor, H annihilates those missing
either the p-face or the q-face: such a word is fixed by one of the
retractions. Only a p-face times a q-face, possibly also times a
full-face profile, remains. This classification is at the completed
tensor-factor level, so it includes general joint coefficient tensors,
not only separable test functions.

For a p-face times a q-face, split their remaining finite coefficients
using the original continuous decompositions

    E_p=C chi_p direct_sum F_p,
    E_q=C chi_q direct_sum F_q.

The term with both chi factors is precisely j beta of that product.
Every other term contains a flat F_p or F_q factor and belongs
continuously to E. For example with a flat p factor, put
s_p=t-j_p log p and s_q=t-j_q log q. The inequalities

    |t|<=|s_p|+|j_p|log p,
    |j_q|log q<=|t|+|s_q|

show that every real and shell weight of the output is absorbed by
stronger weights on the two real profiles and the flat p factor.
Additional weights give the summable shell tails. Derivatives use the
finite Leibniz sum and conductor weights use Fourier convolution.
The q-flat case is symmetric. Thus subtracting j beta leaves a
continuous E-valued map, with explicit finite increases of the existing
seminorm orders.

For a word containing all three nonempty faces, let
s_f=t-j_p log p-j_q log q. Then

    t=s_p+s_q-s_f,
    j_p log p=t-s_p,       j_q log q=t-s_q.

The three real profile decay weights therefore control every real and
both shell weights of the output. The same extra-weight summation and
unit Fourier estimates prove that the entire triple product belongs
continuously to E, in fact to its flat open ideal. The full-face factor
has zero image under beta, so Q_E keeps this term. This accounts for
every word in the finite expansion.

We have consequently constructed a continuous map U_{p,q} -> E whose
represented function is Q_E F_P. If the original tensor lies in the
function kernel, this represented function is zero and injectivity of
E as actual functions forces its E-valued image to be zero. It therefore
descends through the quotient to a continuous map J -> E. On an original
coefficient f in E, both R_p,R_q and beta vanish, so Q_E(f)=f.
Thus

    E_{p,q} -> JProf_{p,q}

has a continuous linear left inverse. It is a topological embedding
with CLOSED image and its original nuclear Frechet topology. This
proves the reverse seminorm comparison, not merely injectivity of its
function representation.

The result completes the source inclusion test for one and two primes.
The formula is a linear remainder projection, not an algebra homomorphism
or a duality functor. More-prime configurations have additional joint
profile regimes, so this proof is not asserted to cover them. Nor do
these source topology comparisons establish the global kernel dagger
or the intrinsic RR metric required for full row A.

## A finite linear criterion for source-valued products in any prime set

The weight argument extends beyond two primes in a precise, checkable
form. Take a finite collection F of nonempty face sets, expand their
remaining E_p factors by C chi_p plus F_p, and fix one term of that
finite expansion. Let U be the union of its face sets and let D be the
set of primes for which a flat F_p factor occurs. Put y_p=j_p log p
and l_J=t-sum_(p in J)y_p.

Suppose the linear forms t and y_p for every p in U belong to the span
of

    {l_J : J in F} union {y_p : p in D}.

Primes in D already carry all their own shell weights. The coefficients
of these linear forms are integers after using y_p as variables, so the
condition and any witnessing identities are finite rational linear
algebra; no logarithmic independence assertion enters it. The witnessing
identities give a constant C with

    |t|+sum_(p in U)|y_p|
       <=C(sum_(J in F)|l_J|+sum_(p in D)|y_p|).

It follows that this whole completed product term takes values
CONTINUOUSLY in the original E_P. Indeed every requested real weight
and flat shell weight for primes in U union D is absorbed by stronger
real-profile weights and the existing flat-factor weights. Extra weights
give summable tails in each of these shell indices. Derivatives use
Leibniz, and unit Fourier sums use conductor submultiplicativity. Primes
outside U union D have only the fixed chi_p factors and require no flat
positive-shell decay. The product vanishes at zeros in U union D, so
it has precisely the permissible source coefficient form. These
estimates first apply to elementary tensors and extend continuously to
the completed projective product. Thus the span test proves membership
with reverse seminorm control, not merely pointwise decay.

There is a useful general family of such certificates. Suppose all
singleton face profiles occur and at least one additional face J has
|J|>=2. Then

    t=(sum_(p in J) l_{p}-l_J)/(|J|-1),
    y_p=t-l_{p} for every p in P.

Therefore the product belongs continuously to the full flat open ideal
for ANY number of primes. This generalizes the three-profile identity
used in the two-prime remainder projection.

A different three-prime example shows that singletons are not necessary.
For P={p,q,r}, the profiles on pq,pr,qr,pqr satisfy

    t=l_pq+l_pr+l_qr-2l_pqr,
    y_p=l_qr-l_pqr,
    y_q=l_pr-l_pqr,
    y_r=l_pq-l_pqr.

Their product is consequently a source coefficient with all flat shell
weights. By contrast, the three pair profiles without the full-face
factor have a common unconstrained direction y_p=y_q=y_r=t/2; the span
criterion does not apply to them. This failure is not used as a theorem
that every particular such product lies outside E_P: its coefficients
and the accessible lattice limits must still be examined.

The criterion supplies continuous source-valued maps for certified terms
of the finite tensor presentation of JProf_P. It does not yet produce a
projection of the WHOLE quotient onto E_P. To obtain that projection one
must also construct compatible boundary maps for the uncertified terms
and prove that relations in the function kernel respect the remainder.
The two-prime proof did both; the displayed linear certificates alone
are not a substitute for the latter requirement in higher prime sets.

## A sharper source estimate using the actual valuation support cone

The span criterion can be sharpened using the support conditions of the
fixed chi factors. Retain a term in the finite coefficient expansion,
its face collection F, union U and flat-factor set D. On variables
(t,(y_p)_(p in U union D)) define the linear map

    L(t,y)=((t-sum_(p in J)y_p)_(J in F),(y_p)_(p in D)).

Let C be the closed cone given by y_p>=0 for each p which has a chi_p
factor and has no flat F_p factor. These are actual support restrictions:
outside that cone the term is zero. Coordinates with a flat factor are
already controlled by their two-sided decay and need no sign restriction.
A coordinate occurring in every profile face may have no chi factor,
and no sign condition is imposed on it without evidence.

If C intersect ker(L)={0}, there is a constant c>0 such that

    ||L z||_1 >= c ||z||_1       for every z in C.

Indeed C intersect {||z||_1=1} is compact; ||Lz||_1 is positive on it
under the stated hypothesis, so has a positive minimum. Homogeneity
gives the inequality. It provides precisely the weight bound needed
in the preceding completed tensor argument. Thus this support-cone
condition also proves continuous membership of the entire product term
in E_P, including all required flat shell weights and real derivatives.

The condition is finite rational linear feasibility after rescaling
y_p=j_p log p. To test for a nonzero vector in C intersect ker(L), one
can fix each coordinate in turn to 1 or -1 and solve the resulting finite
linear equalities and inequalities. Any nonzero vector can be scaled
by a positive scalar to satisfy one of these normalizations. This is an
exact finite criterion; it does not test approximate lattice relations
or presume number-theoretic independence.

For a concrete three-prime term, take faces {p},{q},{p,q,r}, with every
remaining finite coefficient chosen to be its chi factor and no flat
factor. Its support has y_p,y_q,y_r>=0. The kernel equations are

    y_p=t,        y_q=t,        y_p+y_q+y_r=t.

Thus y_r=-t; the sign conditions force all variables to zero. The cone
criterion applies, although the three profile forms cannot span the
four-dimensional ambient dual space. More explicitly, for t>=0 use

    t+y_r=l_p+l_q-l_pqr,
    y_p=t-l_p,           y_q=t-l_q;

for t<0, |l_pqr|=|t|+y_p+y_q+y_r already controls every output variable.
This proves a direct seminorm estimate for that actual product. It is
an original source coefficient, not a new joint boundary profile.

The distinction matters for construction: formal kernels of profile
linear forms can overcount asymptotic directions which the chi supports
exclude. Only directions in the actual support cone require further
boundary analysis. The criterion remains sufficient for a whole tensor
term; failure does not imply that every particular profile in that term
is nondecaying. Completing a global source remainder projection still
requires the boundary comparison maps for the surviving cone directions
and their compatibility with the function kernel.
