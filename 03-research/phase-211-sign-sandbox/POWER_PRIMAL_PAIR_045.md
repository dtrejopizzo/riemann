# POWER_PRIMAL_PAIR_045 — Compact spectral repair of a representing pair

Status: PROVED; independent review APPROVED in POWER_PRIMAL_AUDIT_045.md§4. Bounded result: in the first window with contacts2,3, a low-frequency repair that leaves the tail of the symbol EXACTLY fixed cannot produce a positive pair with small slack. This does not close L55-B, does not refute pairs with non-compact corrections and gives no new sign coverage.

## 1. Antecedents and precise change of hypothesis

Consulted ROUTES-TRIED-INDEX/README.md§L55, AUDIT_B.md§1 (especially lines32–41 and L55-B), grid R162_2300_MASTER_GRID, CROSSWORD-TO-D and the primal/dual definitions of Paper47§3. L55-B remains recorded as an open candidate: no later construction was found. Review044 already distinguished a feasible test that gives an upper from a REPRESENTING pair that can give a lower.

No finite total mass is imposed on the spectral measure: that restriction does not belong to L55-B and is inadequate for a symbol of logarithmic growth. Here the measure is locally finite and has a tail of that scale. The new and specific hypothesis tested is that its whole CORRECTION be compact in frequency, keeping exactly the real tail of the symbol. The obstruction uses uniqueness of moments of a compact measure and the identity for ALL tests, not W4 nor a modification of the comb.

Uniqueness of compact transforms is a classical tool. It is not presented as a new sign principle. The result identifies why this particular repair does not build the missing pair and where the known dual freedom returns.

## 2. Window, normalisations and orientation of the lower

Fix T=3/5, I=(-T,T), Fourier Fhat(tau)=int F(t)exp(i tau t)dt and

    Phi_F(tau)=|Fhat(tau)|²/(2pi),
    c_F(u)=int F(t)conj(F(t−u))dt.

Take real tests F in C_c^infty(I) with A(F)=int F exp(t/2)=0 and B(F)=int F exp(−t/2)=0. The FULL form coincides there with the primitive one because its polar2Re(A conjB) vanishes. In this window log3<2T<log4, so the only contacts are2,3. Define

    m(tau)=Re psi(1/4+i tau/2)−logpi,
    a_n=logn, v_n=2Lambda(n)/sqrt(n),
    q_T(tau)=m(tau)−v_2 cos(a_2 tau)−v_3 cos(a_3 tau),
    nu_Lambda=(v_2/2)(delta_(a_2)+delta_(−a_2))
                    +(v_3/2)(delta_(a_3)+delta_(−a_3)).

Thus a_T(F)=int q_T Phi_F d tau. No arithmetic contact of the window has been deleted.

A proposed representing pair consists of EVEN positive measures mu,nu, locally finite, satisfying, for ALL those tests,

    ARCH_complete(F)+epsilon||F||²
          =int Phi_F dmu+int c_F dnu,                  (PAIR)
    nu|_(-2T,2T)=nu_Lambda.

Possible masses of nu in|u|>=2T do not contribute, since c_F is0 there. All integrals must exist. Then, with correct orientation,

    a_T(F)+epsilon||F||²=int Phi_F dmu>=0,
    lambda_A(T)>=−epsilon.                             (LOWER)

mu here is NOT the feasible probability of programme(P) of Paper47: that one produces an upper of lambda_P. PAIR is a representing identity for ALL tests and is therefore a potential lower datum.

## 3. Fixed-tail ansatz and compact rigidity lemma

Suppose that, for some finite R,

    eta:=mu−(q_T+epsilon)d tau

is an EVEN signed measure supported in[-R,R]. By local finiteness, eta has finite total variation. The measure mu may have infinite total mass; outside the compact it coincides exactly with the shifted real symbol. Since q_T grows logarithmically, this tail is positive for R large enough. No artificial restriction of global finite mass is adopted.

**Lemma.** If PAIR holds for all the indicated primitive tests, then eta=0.

Proof entirely in real variables. Subtracting the two representations gives

    int |Fhat(tau)|² d eta(tau)=0.

For ANY real phi in C_c^infty(I), take F=(D²−1/4)phi. Two integrations by parts prove A(F)=B(F)=0, and

    Fhat(tau)=−(tau²+1/4)phihat(tau).

The compact EVEN measure d eta_tilde=(tau²+1/4)²d eta satisfies

    int |phihat|²d eta_tilde=0 for every phi.            (ALL-SQUARES)

Polarising over real phi,psi and using parity gives that the continuous real kernel

    k(u)=int cos(tau u)d eta_tilde(tau)

satisfies int int phi(t)psi(s)k(t−s)dt ds=0. Localising phi and psi with smooth approximations of point masses at two points of I, one obtains k(u)=0 for EVERY|u|<2T. Here all cross terms are used, not only diagonal entries of a finite matrix.

By compactness one can differentiate under the integral to any order in u0. All even moments of eta_tilde are0; the odd ones are0 by parity. Polynomials are dense in the continuous functions on the compact[-R,R], so eta_tilde=0. The factor(tau²+1/4)² is strictly positive on R, hence eta=0. No argument about spectral objects external to these forms and measures is needed.

The EVEN condition is essential. Without it, an arbitrary odd measure would be invisible to these real autocorrelations; one would only conclude eta_even=0.

## 4. Verifiable falsifier of the ansatz with small slack

At tau0,

    m(0)=−gamma−pi/2−3log2−logpi<−53/10,
    v_2>19/20, v_3>5/4,
    q_T(0)<−15/2.                                     (NEGATIVE-DENSITY)

These are rational comparisons with the elementary intervals already audited003. For example sqrt2<10/7 gives v2>(7/5)log2>19/20; sqrt3<26/15 gives v3>(15/13)log3>5/4. No quadrature or approximate spectrum is used.

If epsilon<=15/2, the lemma forces mu=(q_T+epsilon)d tau, whose density is NEGATIVE in a neighbourhood of0 by continuity. This contradicts mu>=0. Hence there is no PAIR with exactly fixed tail with compact correction and slack epsilon<=15/2. In particular that ansatz does not build a pair of slack0, although positivity of the form in this window is already proved within the range log5/2.

No vector with a_T(F)<0 has been exhibited. Pointwise negativity of the symbol is not that of its compression to the window; precisely that difference makes a different representation necessary.

## 5. The non-compact correction and its exact relation with(D)

The obstacle allows NON-compact corrections. To recognise when that exit already belongs to the corpus, consider the subcase mu=(q_T+epsilon+r)d tau, with r a continuous tempered even function. The representing identity requires

    int |Fhat|²r d tau=0 for every primitive F.

Let k be the inverse transform of r as a distribution. The same test F=(D²−1/4)phi and polarisation imply

    (D²−1/4)²k=0 in(-2T,2T).

The EVEN solutions of this differential equation are

    k(u)=alpha cosh(u/2)+beta u sinh(u/2), |u|<2T.

Define g0=cosh(u/2)1_(|u|<2T), g1=u sinh(u/2)1_(|u|<2T). If the exterior remainder k−alpha g0−beta g1 is a finite signed EVEN measure nu_ext supported in|u|>=2T, then

    r=alpha g0hat+beta g1hat+nu_exthat,
    mu>=0 ⇒ q_T+nu_exthat+alpha g0hat+beta g1hat>=−epsilon.

This is EXACTLY a certificate of value−epsilon of programme(D) of Paper47, with its exterior measure and its two Tate multipliers. Thus the non-compact repair of THIS subcase is not a new primal tool: its verification brings back the known dual margin.

That identification is not extended to all singular positive spectral measures nor to all exterior distributions. L55-B keeps a more general constructive possibility, but this attempt provides no independent pair of that class.

## 6. Entry of the next contact and scope

When T passes log4/2 and stays below log5/2, the updated primitive symbol is

    q_(2,3,4)(tau)=q_(2,3)(tau)−log2·cos(tau log4).

The identity includes the REAL value Lambda(4)=log2. That update is global in frequency: it cannot be carried out as a compact repair of the old tail. The previous lemma applies again to the updated symbol; there is no automatic continuation of the previous pair.

If a representing pair were extended to the new window but kept only contacts2,3, the discrepancy of contact4 would have total variation log2 and formula044 would only guarantee a floor−epsilon−log2. That is a conservative cost of the WHOLE form, not a control of its margin nor of the cross terms of a Schur. The identity of the previous window by itself does not even guarantee that extension: its exterior correction may cease to be invisible when the interval is enlarged.

Hence no new coverage is announced nor a mechanism to pass4 or5. The advance of this exploration is a verifiable obstacle to the concrete fixed-tail ansatz with compact repair, plus the precise identification of the non-compact subcase that returns to the existing dual. It is not a general no-go for positive pairs, it uses no hypothesis of global finite mass and does not turn auxiliary positivity into closure.

Reproduction of constants:

    python3 03-research/phase-211-sign-sandbox/tools/power_primal_pair_045_verify.py

The rigidity proof and its cross terms are analytic and uniform in R. The script only verifies the explicit point and the set of contacts, without campaigns.
