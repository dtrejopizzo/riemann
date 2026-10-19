# P123.092 — An explicit orbit-decay ideal with the original trace

Status: PROVED-IN-REPOSITORY on the single-zero
two-prime boundary. This constructs and compares a stronger domain;
surjectivity of its corner tensor map is not assumed.

## 1. Weight and topology

On Z_q=R times Q_p^* set

    w(t,x)=exp(|t|) p^|v_p(x)|.

This continuous proper weight is at least one. For gamma in Gamma,
both w(gamma z)/w(z) and its reciprocal are at most H(gamma)^2:
the real factor costs exp(|log gamma|)<=H(gamma), and the valuation
factor costs p^|v_p(gamma)|<=H(gamma).

Define J_orb inside the original rapid boundary algebra A_Z by requiring
all seminorms

    s_kl(a)=sum_gamma H(gamma)^k
                  ||w^l a_gamma||_infinity < infinity,
    k,l nonnegative integers.                               (1)

Completeness follows coefficientwise in the weighted sup norms and
then in the weighted label sums. Moreover w^l a_gamma vanishes at
infinity: the bound at l+1 and properness of w imply this outside large
weight balls. Compact coefficient truncations therefore converge in
each (1), using one higher weight and then the summable label tails.
Finite-label compact coefficients are dense in J_orb and in A_Z.
Thus the inclusion J_orb->A_Z is continuous, injective and dense.

It is strict: the coefficient exp(-(1+t^2)^(1/4))1_(Z_p^*)(x) from
P123.091 lies in A_Z and in every polynomial-moment trace domain, but
fails (1) for l=1. No equality of these domains is asserted.

## 2. Ideal operations in the original algebra

For a in A_Z and b in J_orb, the crossed-product formula and the weight
inequality give

    s_kl(a b) <= p_(k+2l)(a) s_kl(b),
    s_kl(b a) <= s_kl(b) p_k(a),
    s_kl(b*) <= s_(k+2l,l)(b).                               (2)

For the first bound, move w(z)^l to the b coefficient evaluated at
gamma^-1 z, paying H(gamma)^(2l) on the a label. For the second, retain
the weight on the first b coefficient. The last inequality follows
by reversing the label and transporting the weight through its dilation.
The same estimates allow the coefficient-unitized ambient rapid algebra
to act: its coefficients remain bounded and its label weights unchanged.

Hence J_orb is a complete two-sided star ideal, with continuous ambient
module actions and its own continuous multiplication. In particular,
if 1+b is invertible in the ambient unital rapid algebra, then

    (1+b)^-1-1=-(1+b)^-1 b belongs to J_orb.                  (3)

Thus its unitization is inverse-closed relative to that algebra. This
is not a statement about invertibility in an unspecified C*-completion.

## 3. External action and cutoff data stay inside the domain

For an external tangent dilation a_T,

    w(a_T z) <= C(a) w(z),
    C(a)=exp(|log a_infinity|) p^|v_p(a_p)|,

and the analogous inverse bound holds. Therefore
s_kl(beta_a b)<=C(a)^l s_kl(b). These maps are continuous automorphisms.
They act strongly continuously: this holds on compact coefficients by
uniform continuity, and the displayed bound is locally uniform in a,
so density extends it to all J_orb. The normal coordinate a_q acts
trivially on the boundary coefficients, as it should.

Every finite-label compact cutoff projection and cutoff transfer from
P123.090 belongs to J_orb. External translates do too. Consequently
the exact projection, partial-isometry and group-law identities of that
note hold within this new ideal's boundary coefficient domain.

## 4. Comparison with the integrable trace domains

For every integer d>=0 and l>0,

    C_dl=integral_(Z_q) (1+|t|)^d w(t,x)^(-l) dt d^*x
        =[integral_R (1+|t|)^d exp(-l|t|)dt]
                       [sum_(m in Z) p^(-l|m|)] < infinity.

The p-adic unit Haar mass is one, so each valuation shell contributes
exactly one before the weight. Hence

    sum_gamma H(gamma)^k integral (1+|t|)^d |b_gamma|
        <= C_dl s_kl(b).                                    (4)

This proves a continuous inclusion into the boundary polynomial-moment
integrable domain used in P123.085–088. The original boundary trace,
full-label trace-class fields, logarithmic trace germ, and their already
proved product identities therefore restrict continuously to J_orb.
No new trace functional or normalization is introduced.

This inclusion also has dense image in that moment domain: truncate
labels, then coefficients by compact cutoffs. Dominated convergence
in every moment norm and uniform convergence in C_0 prove convergence;
all resulting compact coefficients belong to J_orb. Density is not an
inverse to the inclusion and does not transfer arbitrary tensor theorems.

## 5. What is now available for the missing comparison

The orbit-decay condition required by the tensor-image estimate in
P123.091 now has an explicit complete source domain, dense in both the
old rapid algebra and the moment trace domain. It is stable under the
original ambient left/right actions, star, external action and the
cutoff descent, and its traces are the restrictions of the original
ones. This is a compared domain, not a relabeling of the full source.

The next missing statement is an actual completed tensor comparison
for its corner modules, followed by the comparison needed to transport
the designated source correspondences. Neither follows merely from
density or inverse-closedness. Semilocal gluing, the determinant-valued
diagonal and mixed RR remain necessary for full A.
