# P123.120 — Smooth source corner with the original completed composition

Date: 2026-09-07. Status: PROVED-IN-REPOSITORY on the single-zero,
two-prime boundary. This compares the smooth boundary algebra of
P123.118 with an explicit subalgebra of the original source. It does
not extend this boundary equivalence over the other arithmetic strata.

## 1. Smoothness imposed on the existing source algebra

Retain J=J_orb, Z=R times Q_p^*, Gamma, w and s_kl from P123.092.
Real translation and multiplication by U=Z_p^* act on coefficients,
commute with the Gamma action, and hence act by automorphisms of J.
Let D be the real derivative and P_kappa the unit-character projection.
Define J_sm to consist of coefficient functions smooth in t for which

    t_(k,l,m,N)(a)
       =sum_kappa c(kappa)^N s_kl(D^m P_kappa a)<infinity   (1)

for every nonnegative k,l,m,N. Derivatives are coefficientwise. This
specifies the topology; no assumption that every element of J is smooth
is made. Weighted absolute Fourier reconstruction in U gives an injective
continuous inclusion J_sm -> J. Completeness follows coefficientwise,
using uniform convergence of all weighted derivatives, and then absolute
summability over Gamma and the unit characters. Truncating labels and
unit Fourier modes, followed by compact real cutoffs and real smoothing,
proves density in J. The cutoffs converge in each (1) when applied to
an element of J_sm, using a higher orbit weight for their tails.

These operations preserve the source product. Real differentiation has
the usual Leibniz rule and unit Fourier characters multiply. Because
c(kappa lambda)<=c(kappa)c(lambda), the estimates in P123.092 give

    t_(k,l,m,N)(ab)
       <=sum_(j=0)^m binom(m,j)
          t_(k+2l,0,j,N)(a) t_(k,l,m-j,N)(b),             (2)
    t_(k,l,m,N)(a^*) <= t_(k+2l,l,m,N)(a).

Here an index l=0 means the corresponding seminorm in (1); replacing
it by a larger one also gives a valid bound. Unit projections commute
with Gamma dilations up to unit-modulus character phases, which do not
alter the estimates. Thus J_sm is a complete Frechet star algebra with
the original crossed-product multiplication. External translations
preserve it: the unit Fourier factors acquire only phases, real
translation commutes with D, and the orbit-weight change is the same
locally bounded factor as in P123.092.

## 2. A smooth cutoff and identification of its corner

The quotient map Z -> Y has evenly covered neighborhoods which can be
chosen as real intervals times finite-level clopen unit sets. Choose a
finite such cover and smooth real, locally constant unit functions g_i
supported in its sheets, with no common zero on the quotient. Dividing
by the square root of the periodized sum of their squared magnitudes
normalizes their translates to satisfy

    sum_(i,gamma) |f_i(gamma^-1 z)|^2=1.                   (3)

The denominator is positive on the compact quotient, smooth in t and
at a fixed finite unit level. All f_i are compactly supported smooth
functions at a common finite unit level. Take c=sum_i |f_i|^2;
then Pc=1. If a square root of c is needed for the cutoff vector, one
may instead use the finite vector (f_i) and the resulting matrix corner,
or choose the original cutoff as a square of normalized smooth bumps.
For the latter choice start with a nonnegative smooth bump sum g,
positive on at least one point of each orbit, and set
sqrt(c)=g/(P(g^2))^(1/2). This has compact support, is smooth and
locally constant in units, and satisfies Pc=1.

The cutoff idempotent e from this scalar c lies in J_sm. The original
corner identification restricts to a topological algebra isomorphism

    e J_sm e = S(Y).                                     (4)

Here is the topology check, which is necessary for (4). On the cover,
a quotient function has unit coefficient f_kappa(t) satisfying
f_kappa(t+a)=kappa(q)^-1 f_kappa(t), a=log q. Its allowed real Fourier
frequencies are a bounded translate of (2pi/a)Z. Integration by parts
on this twisted interval, or after removing that bounded phase, yields
uniformly in kappa

    sum_tau (1+|tau|)^m |f_hat(tau,kappa)|
       <= C_m max_(j<=m+2) ||D^j f_kappa||_infinity.

The reverse derivative bound follows by absolute Fourier summation.
After summing with all conductor weights these are exactly the seminorms
of S(Y) in P123.101. Multiplication by the fixed smooth finite-level
cutoff coefficients is continuous for these seminorms. Thus f->f e
is continuous from S(Y) to e J_sm e.

In the other direction, periodize the identity-label coefficient as in
P123.094. On the compact fundamental interval/unit domain, the estimate
w(gamma z)>=c H(gamma)^(1/2) supplies absolutely summable translated
tails. It remains true after D^m and unit Fourier projection, since
both commute with translations up to phases. Hence periodization is
continuous from (1) to all the displayed quotient seminorms. On the
corner it is inverse to f->f e, because Pc=1. This proves (4), with
its actual completion, not only the equality of finite-level elements.

## 3. Both smooth completed corner tensors

Put P=J_sm e and Q=e J_sm, with their inherited topologies. The local
frames of P123.093 can use the smooth finite-level f_i in (3). Their
coefficients, denoted r_(i,gamma), then lie in P. Translating a fixed
smooth compact function does not increase its real derivative norms
or its unit conductor. Consequently the estimates of that note extend:

    t_alpha(r_(i,gamma)) <= C_alpha H(gamma)^A_alpha,
    t_beta(r_(i,gamma)^* a)
          <= C_(beta,M) H(gamma)^(B_beta-M/2) t_beta'(a),  (5)

where beta' uses orbit weight M and finitely many real derivatives and
unit weights. To verify the additional indices, apply Leibniz to the
fixed frame coefficient and the a coefficient. The former has bounded
derivatives at a fixed unit level; multiplying it convolves with only
finitely many unit characters, of uniformly bounded conductor. Gamma
translation introduces only phases in those Fourier coefficients.
The remaining label and orbit estimates are exactly P123.093 (6)–(7).
Thus A_alpha and B_beta are independent of gamma; M can be arbitrarily
large because (1) contains every orbit weight.

Since sum_gamma H(gamma)^(-epsilon)<infinity for epsilon>0, (5) proves
absolute convergence in every projective tensor seminorm of

    S_sm(a)=sum_(i,gamma) r_(i,gamma) tensor r_(i,gamma)^* a.

The partial frame sums act as identity on J_sm in all seminorms. On
compact coefficient sets only finitely many translated supports occur;
outside them all derivatives of the omitted multipliers are uniformly
bounded and their products with a tend to zero by a higher orbit weight.
The balancing and inverse identities of P123.093 therefore apply without
changing the algebra product. They give topological bimodule isomorphisms

    P tensorhat_(S(Y)) Q = J_sm,
    Q tensorhat_(J_sm) P = S(Y).                           (6)

The second inverse is b->e tensor b. Thus (6) connects the smooth
completion used for the diagonal to the original boundary source
composition, rather than to a newly chosen multiplication.

## 4. Explicit monoidal transport and its unit

For clarity, these identities already give a monoidal comparison at
the level of complete firm bimodules. A J_sm bimodule N is called firm
here when its action maps J_sm tensorhat_Jsm N -> N and
N tensorhat_Jsm J_sm -> N are topological isomorphisms. On unital
complete S(Y) bimodules M define

    L(M)=P tensorhat_S M tensorhat_S Q,
    R(N)=Q tensorhat_Jsm N tensorhat_Jsm P.                (7)

Associating completed projective tensors with their closed balancing
relations and using (6) proves RL=identity and LR=identity on the
stated domains. It also proves

    L(M) tensorhat_Jsm L(M') = L(M tensorhat_S M'),
    L(S)=J_sm.                                           (8)

All comparison maps are the maps induced by multiplication in (6),
so their associativity and unit diagrams follow by evaluating elementary
tensors and then extending by continuity and density. Transpose exchanges
P and Q and reverses tensor order, using the source involution. These
claims specify domains; exact derived equivalences in additional exact
structures do not follow just from writing (7).

In particular the bounded corner-perfect right modules generated by
summands of (e J_sm)^n correspond exactly to the finite projective
S(Y) modules, and their bounded complexes and determinant lines transport
as in P123.095. The boundary Hochschild computation P123.118 and formal
cyclic model P123.119 are now computations on the coefficient corner of
this explicit source Morita context. An assertion identifying every full
source trace complex with that corner still requires the appropriate
cyclic Morita/exact-structure comparison on its declared domain.

## 5. Boundary of this theorem, and the actual A closure burden

This joins smooth coefficients, the original completed composition and
unit, transpose, corner-perfect determinants, and the completed diagonal
model on one compared boundary source. It is not a Morita equivalence
of the whole arithmetic carrier with this single-zero boundary. In
particular it supplies no extension across the generic or multiple-zero
strata, no comparison with integral contacts, and no identification of
the determinant metric with the intrinsic ruling metric. Those are not
consequences of (6)–(8) and remain necessary to close A. The numerical
radical must still be formed against the full geometric trace domain,
not the positive local anomaly kernel already excluded by P123.112.
