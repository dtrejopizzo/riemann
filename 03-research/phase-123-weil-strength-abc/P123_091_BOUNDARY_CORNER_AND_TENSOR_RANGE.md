# P123.091 — Exact boundary corner and a limit on its completed tensor range

Date: 2026-09-06. Status: PROVED-IN-REPOSITORY for the rapid boundary
algebra with inherited Frechet topologies. This identifies the corner
precisely, but disproves surjectivity of the proposed full Morita tensor
map in that topology. It does not invalidate P123.090's operator descent.

Let A_Z be the nonunital rapid C_0(Z_q) crossed product by Gamma,
with seminorms p_k=sum_gamma ||a_gamma||_infinity H(gamma)^k.
Let c(t,x)=theta(t)1_(Z_p^*)(x) be the cutoff of P123.087 and e=e_c
the compact finite-label projection in P123.090. Multiplication by e
is continuous, so A_Z e, e A_Z and e A_Z e are closed Frechet spaces.

## 1. The corner is exactly C(B_q)

For h in C(B_q), set

    F(h)_gamma(z)=h([z]) sqrt(c(z)c(gamma^-1 z)).              (1)

Its support and labels are contained in those of e. Hence F is
continuous in every p_k. In the orbit representation of P123.088,
put v_y(delta)=sqrt(c(delta s(y))); its norm is one by Pc=1.
Then pi_y(e)=|v_y><v_y| and pi_y(F(h))=h(y)|v_y><v_y|.
It follows by faithful boundary representation that F preserves products
and star, and F(1)=e.

Conversely, for b=e a e the scalar

    h_a(y)=<v_y,pi_y(a)v_y>

satisfies pi_y(b)=h_a(y)|v_y><v_y|. It is continuous on B_q: expressed
upstairs it is the double sum over delta,kappa of
sqrt(c(delta z)) a_(delta kappa^-1)(delta z) sqrt(c(kappa z)).
Properness makes this sum locally finite, each term is continuous,
and reindexing proves Gamma invariance. Also ||h_a||_infinity<=p_0(a).
Thus b=F(h_a), and F:C(B_q)->e A_Z e is a topological star-algebra
isomorphism, with continuous inverse bounded by p_0 on the corner.

## 2. The expected reverse tensor map is not onto

The continuous multiplication map

    m: A_Z e tensorhat_(e A_Z e) e A_Z -> A_Z                 (2)

does not surject. The tensor is completed projective and balanced
by the closed relation subspace, with the inherited module topologies.

To prove this, let K=supp(c). For u in A_Z e, the identity u=u e
forces

    u_gamma(z)=0 whenever gamma^-1 z is not in K.             (3)

Indeed every summand in (u e)_gamma has the common factor
sqrt(c(gamma^-1 z)), by the explicit formula for e. This argument is
valid for the convergent rapid sums as well as for finite sums.

Choose z_n=(n log q,q^n) in Z_q, n>=1. If gamma^-1 z_n is in K,
the p-adic unit condition forces v_p(gamma)=0, hence gamma=q^j.
Boundedness of supp(theta) then gives |j-n|<=C for a fixed C. Thus,
for each k and all sufficiently large n,

    |(u v)_1(z_n)|
      <= C_k q^(-nk) p_k(u) p_0(v),                         (4)

for u in A_Z e and v in e A_Z. To see this, expand the identity
coefficient sum over gamma, use (3), the bound H(gamma)>=q^(n-C),
and the supremum norm for v_(gamma^-1).

Equation (4) extends to the completed projective tensor by its defining
seminorm estimate. It also descends to the balanced quotient, since
the functional is evaluation of its multiplication image. Consequently
every a in the image of (2) satisfies

    sup_(n>=1) q^(nk) |a_1(z_n)| < infinity for every k.       (5)

For a concrete counterexample, take only identity coefficient

    a_1(t,x)=exp(-(1+t^2)^(1/4)) 1_(Z_p^*)(x).

This is in C_0(Z_q), hence gives an element of A_Z. It even has finite
boundary L1 moments of every order. But its value at z_n decays like
exp(-sqrt(n log q)), which violates (5) already for k=1. Therefore
it is not in the image of (2). It also extends to the integrable
source module J_W by multiplying by 1_(Z_q) in the normal coordinate.
Thus the failure is not removed merely by the moment integrability
used in P123.085.

## 3. Consequence for the A construction

The cutoff corner and the transported external action are exact. What
fails is promoting them to a completed Morita equivalence of the whole
rapid boundary algebra with these inherited module topologies. Rapid
decay in the group labels imposes rapid decay along orbit translates
on the tensor image, while arbitrary C_0 coefficients, even those with
all real moments integrable, need not have that stronger decay.

Accordingly the full-label source cannot be transported through (2)
by asserting an inverse multiplication map. A further construction
must either use a compatible correspondence completion or explicitly
identify an orbit-decay subdomain and establish all necessary trace,
external-action and chart comparisons on it. No such change may be
silently identified with the previously declared full coefficient domain.
This result narrows the missing tensor comparison and keeps the valid
single-boundary operator descent of P123.090 intact. Full A remains open.
