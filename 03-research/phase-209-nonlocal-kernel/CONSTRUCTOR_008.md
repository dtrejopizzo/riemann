# CONSTRUCTOR_008 — Inversion of scale, adjoint defect, and a domain check

2026-10-19. **PROVED, independent review approved in AUDIT_008.** D remains OPEN. No identity with Q_T is claimed.

## 0. Corpus check and the precise change of object

Read project rules, index entries CELL_001, P1, the sector/reflection calculations
of phase199, and the new 005–007. Consulted grid and crossword before the
calculation. The earlier sector identities concern the Weil carrier or its
Sonin realization. This note computes the actual inversion of the NEW
Gaussian factor of 007 with its nonhomogeneous weight. It does not retry
those sector arguments as a source of sign. Nor does it introduce a generic
unitary reflection as an additional positivity theorem.

The closed image used in007 is NOT known to be the graph of a closable map.
In particular, a formula on the ambient Gaussian space cannot automatically
be restricted to the completed arithmetic module. The point of the following
calculation is to keep that distinction explicit and test the proposed
adjoint intertwining before using it.

## 1. The ambient inversion is explicit

Fix 0<alpha<1/2. Put

    tau(y)=theta(y)-1,  rho_alpha(y)=y^(alpha-1)tau(y),
    L_alpha=L²((0,infinity),rho_alpha(y)dy).

Define

    (U_alpha f)(y)=a_alpha(y)f(1/y),
    a_alpha(y)=y^(-alpha)sqrt(tau(1/y)/tau(y)).

**Lemma 1.** U_alpha is a unitary self-adjoint involution on L_alpha.

Proof: a(y)a(1/y)=1 and change variables u=1/y in the squared norm.
Indeed the resulting density is u^(alpha-1)tau(u). This argument is a
weighted-L² identity; its unitarity alone supplies no arithmetic sign. At
alpha=1/4, Poisson gives the exact simplification

    a_(1/4)(y)=sqrt((1-m(y))/tau(y)),
    m(y)=y^(-1/2)-tau(y).

For the feature functions f_d(y)=q_d(y)-1/d of007, U_alpha f_d is well-defined
in this ambient space. No assertion is made that the vector, together with
some arithmetic component, belongs to the closed image defining H_alpha.

## 2. Inversion does NOT simply turn a dilation into its adjoint

The Gaussian contractions and their ambient adjoints were computed in007:

    (G_n f)(y)=n^alpha tau(n²y)/tau(y) f(n²y),
    (G_n* f)(y)=n^(-alpha)f(y/n²).

Let

    r(y)=tau(y)tau(1/y)>0,
    b_n(y)=sqrt(r(y/n²)/r(y)).

**Lemma 2.** The exact bounded-operator identity is

    U_alpha G_n U_alpha = M_(b_n) G_n*,             (1)

where the product on the right is interpreted on its natural domain and
then extended by the bounded left-hand side. The multiplier b_n need not
be bounded by itself. In particular one must not separately assert that
both factors are bounded operators.

Proof: insert the formulas. The coefficient multiplying f(y/n²) becomes

    n^(-alpha)sqrt[tau(n²/y)tau(y/n²)/(tau(1/y)tau(y))].

This is exactly (1). The bounded extension follows from unitarity of U and
boundedness of G_n. Conversely, if f is in L_alpha then this explicit
product is in L_alpha, since it equals that bounded extension almost
everywhere. No graph invariance is being assumed.

**Lemma 3.** For each integer n>1,

    b_n(y)<1 if y<n;  b_n(n)=1;  b_n(y)>1 if y>n.

Proof: from ANTICORRELATION_003 let h(x)=log tau(exp x), h''<0. Then
log r(exp x)=h(x)+h(-x) is even, with derivative
h'(x)-h'(-x)<0 for x>0. Hence it decreases strictly with |x|.
Compare |log y-2log n| with |log y| to obtain the three cases. Thus the
multiplicative defect of adjoint intertwining changes direction across
scale n. One cannot delete it by a global inequality b_n<=1.

This is an exact defect, not a NO-GO against other possible involutions or
an extension of H_alpha. It shows that this PARTICULAR ambient inversion
and the known adjoint do not obey U G_n U=G_n*.

## 3. The graph-domain question remains a real question

On the algebraic Haar-centered domain, let

    T A(y)=E_y A,
    A -> (sqrt(kappa) A, T A)

be the embedding of007 into L²(P_s) direct-sum L_alpha, s=2alpha.
Let H_alpha be its closed image. Closure in a product always exists, but
it does not prove that its projection onto L²(P_s) is injective. A vertical
component {0} direct-sum V could be present. Neither its presence nor its
absence has been proved here.

A tempting argument for a vertical component uses primorial exclusions.
Let L>=3, P_L the product of primes <=L, delta_L=prod_(p<=L)(1-1/p), and

    A_L(N)=1_((|N|,P_L)=1)-delta_L.

Each A_L is a finite divisor polynomial and E_1 A_L=0. Under P_s,

    E_s|A_L|²=delta_(s,L)-2delta_L delta_(s,L)+delta_L² ->0,
    delta_(s,L)=prod_(p<=L)(1-p^(-s)).

The convergence follows from delta_L->0 and delta_(s,L)<=delta_L for s<1.
For each fixed y>0, dominated convergence of the Gaussian sum gives

    T A_L(y) -> 2exp(-pi y)/tau(y).

That is ONLY pointwise convergence, not convergence in L_alpha.

**Lemma 4 (elementary arithmetic bounds included).** For fixed
0<alpha<1/2, the Gaussian norms of this particular sequence diverge:

    ||T A_L||²_(L_alpha) >= c_alpha delta_L² L^(1/2-alpha)
                         -> infinity.

No Mertens estimate or zero-location input is needed. The elementary bounds

    exp(-2)/(1+log²L) <= delta_L <= 1/H_floor(L)

suffice. For the upper bound, the finite Euler product for reciprocal
primes <=L contains the harmonic sum over n<=floor(L). For the lower bound,
put epsilon=1/log²L. The logarithm of the ratio of finite products at
1 and1+epsilon is at most

    epsilon sum_(p<=L) log p/(p-1)
      <=epsilon log L (1+log L)<2,

using 1-exp(-u)<=u termwise in the logarithmic power series. The product
at1+epsilon is at most zeta(1+epsilon)<=1+1/epsilon, by integral comparison.
This proves the stated lower bound and the divergence in Lemma4.

Proof of the lower bound: for y in [1/L,2/L], all permitted positive integers
other than1 exceed L. Therefore

    tau_(P_L)(y)=2exp(-pi y)+O(L exp(-cL)),
    tau(y) is comparable to sqrt(L),
    q_(P_L)(y)=tau_(P_L)(y)/tau(y)=O(L^(-1/2)).

The elementary lower bound above gives delta_L much larger than L^(-1/2). Thus |T A_L(y)|>=delta_L/2
throughout this interval for L large. Integrating against
rho_alpha(y)dy yields the claimed lower bound because

    int_[1/L,2/L] y^(alpha-1)tau(y)dy is comparable to L^(1/2-alpha).

This rules out the proposed STRONG-limit argument using A_L. It does NOT
prove closability or nonclosability of T, and it does not exclude other
vertical sequences. The norms may concentrate toward y=0 while the
pointwise limit is perfectly integrable.

## 4. What this changes in the next step

The available inversion has an explicit nontrivial adjoint defect (1).
Its invariance on H_alpha and the relation to the arithmetic component are
still unproved. A construction may now either calculate a compensating
arithmetic operation, or choose another explicitly defined enlargement and
prove all its restrictions. Neither can be inferred from generic unitary
inversion of the ambient measure.

No trace, carrier map U_T, or equality with Q_T has been constructed. The
next requirement remains a concrete map and a termwise identity with the
archimedean, comb, and pole of Paper46. The completion of D is still the
active objective, not the completion of this auxiliary note.

Final review AUDIT_008: all stated lemmas approved with elementary proofs.
No Mertens estimate is needed. Domain invariance and Q_T remain OPEN.


## Domain update — continuation015

CONSTRUCTOR_015_DOMAIN_AND_CONE resolves with another sequence the question
left open here: H=L²(P_s)⊕V and the operator T of 007 is not closable.
The strong vertical vector comes from likelihood tilts over large primes,
not from the divergent primorial sequence of 008. V=all Gaussian is not claimed,
nor invariance under the ambient FE; the Q link remains OPEN. AUDIT_015 favourable.
