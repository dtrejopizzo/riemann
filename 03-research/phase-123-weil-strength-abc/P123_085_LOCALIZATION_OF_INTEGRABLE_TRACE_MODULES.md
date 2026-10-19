# P123.085 — Localization acts exactly on integrable trace modules

Status: PROVED-IN-REPOSITORY for a two-prime carrier.
The construction is a module action of localized correspondences on
trace domains. It does not assert that two integrable modules compose
to an integrable module by an invertible multiplication map.

## 1. A common ambient algebra and the stronger module topology

Use X^+=R_(>0) times Q_p times Q_q, t=log(x_infinity), Gamma=<p,q>,
and let A be the coefficient-unitized rapid C_0(X^+) crossed product,
with seminorms p_k. This is the P123.019 construction on the open
positive-real carrier. Put W=X^+ minus {x_p=x_q=0}.

On Z_q={x_q=0,x_p!=0} use dmu_q=dt d^*x_p; define mu_p symmetrically.
Both measures are Gamma-invariant and locally finite on W. For an
invariant open V contained in W, define J_V to consist of rapid C_0(V)
coefficients, extended by zero, satisfying all seminorm bounds

    j_kd(x)=p_k(x)+sum_gamma H(gamma)^k
                sum_(v=p,q) integral_(Z_v) (1+|t|)^d |x_gamma| dmu_v
             < infinity.                                      (1)

This is a complete Frechet space: a Cauchy sequence has a coefficient
sup-norm limit in C_0(V) and weighted L1 limits on the strata, and these
agree by almost-everywhere subsequences. The resulting rapid and graph
limits agree coefficientwise and converge in every displayed seminorm.

Let I_U be the ordinary sup-norm rapid ideal of an invariant open U in
X^+. The multiplication formulas define continuous left and right A
actions on J_V. For example, for some constant depending on d,

    j_kd(a x) <= C_d p_(k+d+1)(a) j_kd(x),
    j_kd(x a) <= C_d j_kd(x) p_k(a),                           (2)

with harmless index enlargement also allowed in the second inequality.
Indeed, use the sup norm on the a coefficient and the weighted L1 norm
on the x coefficient; a Gamma translation costs at most
(1+|log gamma|)^d <= C_d H(gamma)^(d+1). Summability then proves (2).
Products remain supported in V by invariance. In particular J_V is an
A-bimodule, even though it carries a stronger topology than I_V.

## 2. Mixed completed tensor localization

Multiplication induces topological bimodule isomorphisms

    I_U tensorhat_A J_V  = J_(U intersect V),
    J_V tensorhat_A I_U  = J_(U intersect V).                    (3)

Use coefficient cutoffs e_alpha in C_c(U), 0<=e_alpha<=1, at label 1.
They have p_k(e_alpha)<=1; their integrable norms are not assumed
bounded. Left multiplication by e_alpha converges to identity on
J_(U cap V), in every (1), by dominated convergence on each stratum
and domination of the rapid label tails. Right multiplication does as
well: its coefficient multiplier is alpha_gamma(e_alpha), again bounded
by one and converging pointwise to one on U for every fixed gamma.

For left surjectivity, set r_0=z in J_(U cap V). Choose successive e_j
so that r_(j+1)=r_j-e_j r_j is <=2^(-j-1) in the first j graph seminorms.
Then sum_j e_j tensor r_j converges in I_U tensorhat_pi J_V and its
product is z. Only the sup seminorms of the first factor are used.

For injectivity, in the completed balanced quotient T, left cutoffs
converge strongly to identity because they do so on I_U with uniformly
bounded operators. Balancing and continuity give

    L_e(t)=e tensor m(t).

If m(t)=0 then t=lim_e L_e(t)=0. The open mapping theorem gives the
topological isomorphism. The right version uses right cutoffs on I_U,
the identity R_e(t)=m(t) tensor e, and the right-hand residual series.

The augmented completed bar with terms
I_U tensorhat_pi A^(tensorhat_pi n) tensorhat_pi J_V and augmentation
onto J_(U cap V) is strictly exact. Insertion of e as its first factor
gives d h_e+h_e d=L_e, uniformly bounded insertion in the mixed
projective seminorms, and strong convergence of L_e in every degree.
The same diagonal residual series fills every cycle exactly, as in
P123.083. This is strict exactness, not a continuous linear contraction.

## 3. Nonzero continuous cyclic tests on this same module domain

The actual boundary traces

    tau_v(x)=integral_(Z_v) x_1 dmu_v

are continuous on J_V with |tau_v(x)|<=j_00(x), and satisfy
tau_v(a x)=tau_v(x a) for every a in A. To check this, expand inverse
label pairs and change variables by Gamma on Z_v. Each pair is
integrable by the supremum bound on a and the L1 bound on x; the
weighted rapid estimates justify summing the absolute integrals.
Thus they descend to the Hausdorff continuous quotient Q_A(J_V).

They are independent on J_W. Choose nonnegative g in C_c(R) with
integral g=1 and set, at identity label only,

    f_q(t,x_p,x_q)=g(t) 1_(Z_p^*)(x_p) 1_(Z_q)(x_q).

This is a compactly supported coefficient on W, belongs to J_W, and
(tau_p(f_q),tau_q(f_q))=(0,1), since unit Haar masses are one.
Swapping p and q gives f_p with trace vector (1,0). Consequently the
map Q_A(J_W)->C^2 given by these two traces is continuously split
surjective, with section represented by f_p,f_q. In particular the
trace module has nonzero Hausdorff cyclic classes away from the origin.

There is no contradiction with P123.084: continuity of these integrals
uses (1), not the C_0 sup topology. The inclusion J_W->I_W can send
nonzero shadow classes to zero; a continuous inclusion need not induce
an injection after quotienting by closed commutators.

## 4. Scope and next requirement

Equations (3) show that geometric localization and the nonzero boundary
trace domain coexist over one declared algebra, without an unjustified
bounded approximate identity in integrable norms. Iterated localization
is coherent: all parenthesizations multiply elementary tensors to the
same product and identify the final support with the intersection.

This is a nontrivial trace-module sector, not yet the numerical mixed
correspondence quotient of A.6. In particular no identification
J_U tensorhat_A J_V = J_(U cap V) has been proved, and neither a
determinant-valued shadow nor the required mixed RR follows from the
two scalar traces. Those structures and their prescribed analytic
comparison remain obligations for full A.
