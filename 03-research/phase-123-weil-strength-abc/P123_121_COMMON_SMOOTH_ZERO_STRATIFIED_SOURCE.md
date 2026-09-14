# P123.121 — One smooth semilocal source containing the zero-stratum boundaries

Date: 2026-09-07. Status: PROVED-IN-REPOSITORY for the explicitly
defined coefficient and crossed-product algebras below. This provides
one source with all finite-zero layers and coherent semilocal embeddings.
It does not by itself construct the full mixed RR metric or prove A.

## 1. A coefficient algebra across one finite zero

For each prime p write a nonzero p-adic number uniquely as p^j u,
j in Z, u in U_p=Z_p^*. Define F_p by Fourier sequences f_(j,kappa),
where kappa ranges over the continuous finite-order characters of U_p,
with seminorms

    v_(l,N)(f)=sum_(j,kappa) p^(l|j|) c_p(kappa)^N
                                      |f_(j,kappa)|,      (1)

finite for all integers l,N>=0. Reconstruct
f(p^j u)=sum_kappa f_(j,kappa) kappa(u), and set f(0)=0.
The series converges uniformly. The bounds for every l show decay to
zero at both ends j->+infinity and j->-infinity, and continuity at 0.
Thus F_p is an injectively realized Frechet algebra of actual functions
in C_0(Q_p). It is an algebra ideal under its own pointwise product:
unit Fourier multiplication is convolution at the same j, and the
conductor product inequality gives v_(l,N)(fg)<=v_(l,N)(f)v_(l,N)(g).
Completeness follows from weighted ell1 completeness at every seminorm.

Put chi_p=1_(Z_p) and

    E_p=C chi_p direct_sum F_p,                            (2)
    ev_0(lambda chi_p+f)=lambda.

The sum is direct since every F_p function vanishes at 0. It is an
algebra: chi_p^2=chi_p and multiplication by chi_p on F_p is exactly
the projection onto j>=0. Evaluation at 0 is an algebra homomorphism,
and lambda->lambda chi_p is a continuous algebra section. The inclusion
E_p -> C_0(Q_p) is continuous and injective.

The space F_p is nuclear. The inclusion from (l+1,N+3) to (l,N)
has a rank-one coordinate expansion with summable coefficients
p^(-|j|) c_p(kappa)^(-3): the j sum is geometric and the character
sum is finite by the conductor count in P123.101. The same is true
of E_p, with its additional one-dimensional summand.

## 2. Dilation includes its actual nonzero attaching correction

For a=p^h v with v a unit, define alpha_a f(x)=f(a^-1 x).
On F_p it shifts j to j-h and multiplies each unit Fourier coefficient
by a unit-modulus phase. Hence

    v_(l,N)(alpha_a f)<=p^(l|h|) v_(l,N)(f).               (3)

On the other summand,

    alpha_a chi_p-chi_p=1_(p^h Z_p)-1_(Z_p) in F_p.        (4)

It is supported on |h| valuation shells, has only the trivial unit
character, and its (l,N) seminorm is at most
|h| p^(l|h|), with zero value when h=0. In particular dilation acts
continuously on E_p with polynomial growth in max(p^h,p^-h), allowing
one extra power to absorb |h|. The splitting (2) is not asserted to
be equivariant. The explicit correction (4) is retained in every
crossed multiplication; it is the shell term used in P123.049.

Every compactly supported locally constant function on Q_p belongs
to E_p: subtract its value at 0 times chi_p; the remainder has finite
valuation support and finite unit level. Thus E_p is dense in C_0(Q_p).
This density is not used to transfer trace or tensor identities.

## 3. Real coefficients and the common finite-prime source

Let E_R consist of smooth functions on the real t line such that

    r_(l,m)(f)=sup_t exp(l|t|)|D^m f(t)|<infinity           (5)

for every l,m>=0. It is a complete algebra, contains C_c^infinity(R),
and embeds continuously and densely in C_0(R). Real translation by s
costs at most exp(l|s|) in (5); products obey Leibniz estimates.
This Frechet space is nuclear: use a smooth partition subordinate to
integer translates of a fixed compact interval, and expand each
localized function in a Fourier series on a fixed larger interval.
Analysis and synthesis are continuous in the seminorms with weights
exp(l|j|)(1+|n|)^m. The analysis map has a continuous left inverse by
summing the localized series, with only finitely many overlapping
intervals at each point. The weighted sequence space is nuclear since
increasing l by one and m by two gives a summable rank-one expansion.
Thus E_R is a complemented subspace of a nuclear sequence space.

For a finite set P of primes put

    E_P=E_R tensorhat_pi tensor_(p in P) E_p.              (6)

It is a complete nuclear Frechet algebra and an algebra of functions
on R times product_p Q_p. An explicit faithful realization follows
from the finite direct-sum splitting (2): each summand is a function
with real coefficient in E_R and weighted absolutely summable shell/
unit-character indices for its F_p factors, multiplied by chi_p in
its other factors. Repeated evaluation at 0 separates these summands;
Fourier uniqueness then gives injectivity. Products and the inclusion
into C_0 are continuous. The tensors of compact smooth/locally constant
functions lie in (6) and are dense in the original C_0 coefficient
space.

Let Gamma_P be the original prime lattice. The action on (6) is the
original real translation and finite dilations, including (4). For
every coefficient seminorm nu there are nu', M and C with

    nu(alpha_gamma f)<=C H(gamma)^M nu'(f).               (7)

This follows factorwise from (3)–(5). Define the common crossed algebra

    A_sm(P)={sum_gamma a_gamma U_gamma:
                sum_gamma H(gamma)^k nu(a_gamma)<infinity
                for all k and nu}.                      (8)

The product is exactly the original crossed product. Submultiplicativity
of H, (7) and the coefficient product estimates prove its continuity;
reversal of labels and (7) prove continuity of its original involution.
Weighted sequence completeness proves completeness, and the same
coefficientwise realization gives an injective continuous map into the
original rapid C_0 crossed algebra. It has dense image there.
If gauge unitaries are required, replace E_P by E_P direct_sum C1
before (8). This is the coefficient unitization, with the original
rapid scalar lattice sector, not an assertion that A_sm(P) is unital.

## 4. All finite-zero strata occur in this single algebra

For a subset J of P, restriction to x_p=0 for p in J is the tensor
of evaluations ev_0 in those coordinates. Its section multiplies by
product_(p in J) chi_p. It is a continuous linearly split coefficient
map; crossing with Gamma preserves the splitting coefficientwise, but
the section is not Gamma-equivariant or multiplicative after crossing.
Its defect is computed by (4), not suppressed.

Let F_k be the locus with at least k zero finite coordinates and L_k
its exactly-k-zero layer as in P123.048. The finite commuting coordinate
projections f->chi_p ev_(0,p) from (2) give the same inclusion-exclusion
splittings as that note. Hence the restrictions of the source (8) form
strict linearly split algebra extensions

    0 -> A_sm(L_k) -> A_sm(F_k) -> A_sm(F_(k+1)) ->0.       (9)

Here these notations mean the actual restriction images of (8), with
the explicitly split quotient topologies; the kernel has the topology
of the corresponding F_p tensor factors from (2). More explicitly,

    A_sm(L_k)=direct_sum_(|J|=k)
       Rapid_(Gamma_P)(E_R tensorhat tensor_(p notin J) F_p). (10)

The zero coordinates in each summand have been evaluated, while all
remaining coordinates have flat decay at the boundaries of that layer.
One can check (9) directly in the finite tensor splitting: each layer
selects exactly the summands with the required zero evaluations, and
its kernel selects an F_p factor whenever another zero is possible.
The maps are restriction and extension by zero on the indicated open
layer. The decompositions are not a multiplicative decomposition of
the whole source into independent strata.

For P={p,q} and the q-zero, p-nonzero layer, (10) is exactly the smooth
orbit-decay algebra J_sm of P123.120, with equivalent seminorms.
Indeed (1), (5) and the rapid Gamma sum give weighted sums over labels,
valuation shells and unit characters of real weighted derivatives.
Changing a supremum over shells to a sum costs only one higher shell
weight; changing the real sup topology to its tensor sequence description
uses the Fourier/partition argument following (5). These are precisely
the seminorms in P123.120 (1). Thus the known smooth corner is the
actual single-zero layer of (8), not an unrelated replacement domain.
The generic and all higher-zero layers in (10) remain present.

## 5. Coherent semilocal embeddings

For P contained in T, embed coefficients by

    j_(P,T)(f)=f product_(ell in T minus P) chi_ell.        (11)

This map is continuous, injective and multiplicative, since every
chi_ell is idempotent. A prime-lattice element gamma in Gamma_P is a
unit at ell notin P, so alpha_gamma chi_ell=chi_ell. Consequently (11)
is equivariant for the old lattice. Extend it to (8) by the inclusion
Gamma_P -> Gamma_T and zero coefficients at new labels. This gives a
continuous injective algebra and star homomorphism, preserving the
old multiplication and involution. Its inverse onto its range is the
new-coordinate evaluation at zero followed by restriction to old labels.
Thus no separation of coefficients is lost.

For coefficient unitizations extend by lambda1+f -> lambda1+j(f);
then the existing gauge unitaries U_gamma map to the actual old-lattice
unitaries. For P contained in T contained in V the maps compose exactly:
products of the new chi factors give j_(T,V)j_(P,T)=j_(P,V).
They commute with the appropriate old-coordinate restrictions and retain
the dilation defects (4) for new lattice elements. This is coherent
semilocal source gluing, not a proof of descent for all future trace
or determinant objects.

## 6. What has been joined and what still requires a theorem

Equations (6)–(11) put the smooth single-zero composition/corner of
P123.120 into one explicit semilocal source with all zero strata,
actual nonzero attaching terms, transpose and coherent embeddings.
The completed boundary diagonal of P123.118 and formal cyclic shadow
of P123.119 now have a specified layer of that same source as their
coefficient domain.

A full A claim still requires a localized correspondence category on
the noncollapsed square, its declared derived composition and shadow
on this whole source (including the other layers), comparison to the
integral coefficient/contact construction, the full numerical quotient
and source effectivity, and identification of the mixed determinant
with the intrinsic ruling determinant and metric. None is inferred
from density or the source algebra alone. In particular (11) is not
an excision or Riemann--Roch theorem, and the boundary metric is not
promoted to the arithmetic intersection by definition.
