# P123.083 — Noninvertible localized correspondences and exact composition

Status: PROVED-IN-REPOSITORY for the original rapid
C_0 coefficient ideals inside the unital algebra A of P123.019.
This supplies localized objects beyond P123.082. It does not close row A.

## 1. Objects and approximate identities

For a Gamma-invariant open U in X_S, let I_U consist of rapid sequences
whose coefficients belong to C_0(U), extended by zero to X_S. It is a
closed two-sided Frechet ideal of A with the inherited seminorms p_k.
In particular I_U intersect I_V=I_(U intersect V), topologically.

Compactly supported functions e_alpha in C_c(U), with 0<=e_alpha<=1
and tending to one uniformly on compact subsets of U, placed at label
1, form a two-sided approximate identity of I_U. Every p_k(e_alpha)<=1.
Left convergence follows first coefficientwise and then by domination
of the weighted summable tail. For right convergence use
(x e_alpha)_gamma=x_gamma alpha_gamma(e_alpha); invariance of U gives
the same coefficientwise convergence and the same tail bound.
These assertions require neither an invariant cutoff nor compact U.

## 2. The completed intersection theorem

There is a canonical topological bimodule isomorphism

    I_U tensorhat_A I_V  --multiplication--> I_(U intersect V).       (1)

Here tensorhat_A is the completed projective tensor modulo the closed
linear span of the balancing relations. This quotient is Frechet.

First prove surjectivity already before balancing. For z in the
intersection set r_0=z. Choose e_j from the approximate identity of I_U
so that p_k(r_j-e_j r_j)<=2^(-j-1) for k<=j, and set
r_(j+1)=r_j-e_j r_j. All residuals remain in the intersection.
For each fixed k, p_k(r_j)<=2^-j eventually. Thus

    sum_j e_j tensor r_j in I_U tensorhat_pi I_V

converges in every projective seminorm and its product is z.

For injectivity let T be the balanced quotient and let m:T->I_(U cap V)
be multiplication. Left multiplication L_e on the first tensor factor
has norm at most one in every projective seminorm; L_e tends strongly
to identity on T, by density of elementary tensors and equicontinuity.
Balancing gives, first on elementary tensors and hence on all T,

    L_e(t)=e tensor m(t),

since e x tensor y=e tensor x y for x in I_U, which is also in A.
If m(t)=0, every L_e(t)=0 and consequently t=0. The continuous bijection
(1) is a homeomorphism by the Frechet open mapping theorem.

## 3. No higher homology in the explicit completed composition bar

Use the augmented two-sided bar

    B_n=I_U tensorhat_pi A^(tensorhat_pi n) tensorhat_pi I_V (n>=0),
    B_(-1)=I_(U cap V),

with the alternating adjacent-product differential and augmentation m.
For e in the approximate identity define

    h_e(x tensor a_1 tensor ... tensor a_n tensor y)
       =e tensor x tensor a_1 tensor ... tensor a_n tensor y,
    h_e(z)=e tensor z  (degree -1).

The middle x is an A factor. Direct cancellation gives

    d h_e+h_e d=L_e,

where L_e multiplies the first factor, including in degree -1.
Insertion is uniformly bounded by one in each projective seminorm,
and L_e converges strongly to identity in every degree.

For a cycle z choose successive e_j so that the residuals
r_(j+1)=r_j-d h_(e_j)r_j=(1-L_(e_j))r_j are at most 2^(-j-1)
in the first j seminorms. The convergent series sum_j h_(e_j)r_j
is an exact filling. Thus the augmented bar is strictly exact:
boundary images are the closed kernels, and the surjections onto them
are open. The same proof works after tensoring with any Frechet space,
using its projective seminorms. No continuous linear section is asserted.
Consequently this explicit completed bar computes only the intersection
in degree zero. Identifying it with a different derived tensor formalism
still requires that formalism's admissibility hypotheses; in particular
this does not supply a splitting in the exact structure of P123.066.

## 4. External twists, associativity and genuine localization

Define E_(U,a)=I_U with ordinary left action and right action
x.c=x beta_a(c). Since beta_a(I_V)=I_(aV), (1) gives

    E_(U,a) tensorhat_A E_(V,b) = E_(U cap aV,ab),
    x tensor y |-> x beta_a(y).                                  (2)

The bar argument transfers by applying beta_a to the middle algebra
factors and to the second module. For three factors both compositions
send x tensor y tensor z to x beta_a(y) beta_(ab)(z), with support
U cap aV cap abW. These continuous maps agree on a dense subspace,
so associativity and its coherence follow. Adjoin the original twists
E_a of P123.064 as well; E_1=A is the unit, and their products with
localized objects obey the same support-transport rule.

Inclusions of invariant opens give continuous bimodule maps I_U->I_V.
For any nonempty U, I_U is nonzero and idempotent under (1), but is not
isomorphic to A as an A-bimodule: an isomorphism would map 1 to a
central element of I_U. P123.082 gives Z(A)=C1, whereas I_U cap C1=0.
Moreover an invertible idempotent object in a monoidal category would
be isomorphic to the unit, so these objects are noninvertible.
Proper invariant opens exist, for example {x_p!=0} for p in S_f.
This therefore enlarges the twist sector by actual localized objects.

The star formula x |-> beta_(a^-1)(x*) sends E_(U,a) to
E_(a^-1 U,a^-1), reverses products (2), and is a continuous conjugate
linear involution. This is an object/product-level transpose, not yet
a contravariant duality on every stable morphism or a dualizability result.

## 5. Exact scope for A

This constructs noninvertible geometric localization, continuous
composition, and a strictly exact bar comparison for the localized
ideal sector. It does not establish a nonzero numerical mixed quotient:
that requires the diagonal trace tests and radical in A.6. Nor does
it construct the determinant-valued diagonal, mixed Riemann--Roch,
effectivity descent, or finite-field comparison. Those remain necessary
for full A, and are not consequences of the intersection theorem.
