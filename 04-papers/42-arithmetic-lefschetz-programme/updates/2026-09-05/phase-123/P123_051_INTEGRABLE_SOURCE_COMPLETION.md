# P123.051 — An integrable completion for the source transgression

Date: 2026-09-05. Status: CONSTRUCTED with continuous algebra operations
and traces for the two-prime extension. This is an additional source
domain, not a claim of trace continuity on all rapid C_0 coefficients.

## 1. Graph seminorms on ideal and quotient tests

Use A_c, I_c, B_c, the section s and the two boundary measures mu_p,mu_q
of P123.050. For integers k,d>=0 and a label gamma define

    N_d(i_gamma)=sum_(v=p,q) integral_(Z_v)
                     (1+|t|)^d |i_gamma| dmu_v,
    M_d(b_gamma)=integral_R (1+|t|)^d |b_gamma(t)|dt.

Add these to the original rapid seminorms:

    I_kd(i)=p_k(i)+sum_gamma H(gamma)^k N_d(i_gamma),
    B_kd(b)=p_k(b)+sum_gamma H(gamma)^k M_d(b_gamma).

Define I_int and B_int as the completions of the test spaces in all
these seminorms. They embed injectively in their original rapid algebras:
supremum convergence determines the coefficient limit, and the weighted
L¹ limits on each stratum agree with its restriction by almost-everywhere
subsequences. In particular a zero rapid limit has zero graph-norm limit.
The completions impose no differentiability not present in these norms.

## 2. Product and involution estimates

Boundary measures are invariant under Gamma. Only the real moment weight
changes under dilation. For ell=log gamma,

    1+|t+ell| <= (1+|t|)(1+|ell|),
    |ell| <= log H(gamma).

Consequently weighted boundary L¹ norms of alpha_gamma(i) are bounded
by (1+log H(gamma))^d N_d(i). The same estimate holds for M_d on the
quotient. Multiplying coefficients uses the supremum norm of one factor
and the weighted L¹ norm of the other. Combining with
H(gamma eta)<=H(gamma)H(eta) proves continuity of products and involutions
on I_int and B_int. Polynomial factors in log H are absorbed by increasing
the rapid index, for example from k to k+d+2. No uniform estimate at one
fixed k is required for continuity in this Fréchet topology.

The valuation derivations delta_p and delta_q also act continuously on
B_int, because |v_p(gamma)|+|v_q(gamma)| is bounded by a constant times
log H(gamma). Multiplication by t maps the d+1 moment seminorm to the d
moment seminorm, so it is a continuous multiplier on this domain.

## 3. The attaching defect is continuous in these stronger norms

For b_gamma=g U_gamma and c_eta=h U_eta, P123.049 gives

    omega(b_gamma,c_eta)
      =(chi alpha_gamma(chi)-chi)g(t)h(t-log gamma)
                                                   U_(gamma eta).

On the two boundary strata, the total absolute shell measure is
max(v_p(gamma),0)+max(v_q(gamma),0), bounded by C log H(gamma).
Therefore

    N_d(omega(b_gamma,c_eta))
      <= C log H(gamma) ||h||_infinity M_d(g).

The original supremum bound is at most ||g||_infinity ||h||_infinity.
Summing label pairs and absorbing log H in a higher rapid seminorm
proves that omega:B_int times B_int -> I_int is continuous bilinear.

Likewise the involution defect s(b)*-s(b*) has coefficient supported in
the symmetric difference between chi and its dilate. Its total boundary
shell measure is |v_p(gamma)|+|v_q(gamma)|. The same estimates, including
the real translation moment factor, prove continuity into I_int.

Finally multiplication of an ideal element by s(b) on either side is
continuous: on each boundary use ||b_gamma||_infinity, the weighted L¹
norm of the ideal coefficient and the translation estimate of section 2.

## 4. A complete extension on which the traces make sense

On the vector space I_int direct_sum B_int define the product by

    (i,b)(j,c)=(ij+i s(c)+s(b)j+omega(b,c),bc).

Here s and the mixed products are understood through their coefficient
formulas in the original rapid algebra; sections 2–3 prove they extend
continuously to this space. The involution is

    (i,b)*=(i*+s(b)*-s(b*),b*).

These operations give a Fréchet star algebra A_int. Associativity and
the star identities hold on the dense test algebra and extend by
continuity. The injective map (i,b) -> i+s(b) identifies it with a
subalgebra of A(X^+). It yields the strict linearly split extension

    0 -> I_int -> A_int -> B_int -> 0.            (4.1)

Thus the choice of a stronger domain retains the actual source product
and its nonzero attaching term. It does not replace that product by a
direct-product algebra or assume the section multiplicative.

## 5. Continuous traces and transgression on the completion

The defining estimates immediately give

    |tau_p(i)|, |tau_q(i)| <= I_00(i),
    |tau_B(b)| <= B_00(b),
    |eta(b)| <= B_01(b).

Hence the source traces and first-moment functional of P123.050 extend
continuously. Trace cyclicity and mixed centrality extend from the dense
tests by continuity of multiplication. The formulas

    c_q(x,y)=-tau_B(delta_p(x)y),
    c_p(x,y)=-tau_B(delta_q(x)y),
    (log p)c_q(x,y)+(log q)c_p(x,y)=-eta(xy-yx)

are now continuous identities on B_int, and equal the traces of the
attaching defects in (4.1). All cyclic identities therefore also extend.

This resolves the integrability-domain requirement left by P123.050 for
this two-prime source calculation. It does not prove that the external
normal cutoff realization factors through A_int, that its relative trace
equals these source operations, or that this domain has the required
semilocal and integral-contact functoriality. Those comparisons remain
necessary before claiming the common shadow or a completed row.
