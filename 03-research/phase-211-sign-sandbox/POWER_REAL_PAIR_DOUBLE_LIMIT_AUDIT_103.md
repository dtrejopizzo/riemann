# Independent audit103 — real limits and pointwise test

Status: **PROVED / audit approved. Original run and independent reproduction FULLPASS.** The test certifies a negative sign at the limiting origin. Papers untouched.

Sources reviewed: `POWER_REAL_PAIR_DOUBLE_LIMIT_103.md`, `POWER_REAL_PAIR_LIMIT_ORIGIN_DESIGN_103.md` and `tools/power_real_pair_limit_origin_103_verify.py`. The project rules and the three current indexes were consulted, in particular102 and its complement099. The difference is to decide a pointwise condition of the next REAL pair by means of justified limits; not another representation nor a generic test of potentials.

## Limits and normalisations

The two-sided resolvent formula `A_p=pD_p=R_pJ−(c/p)R_pPhi` is exact. The formula B-EXACT is also exact, using `R_pJ−J=R_pJ''/p²`. The probabilistic kernel has weighted norm at most `p/(p−sigma)`; the identities with derivatives pay the approximation to the identity without requiring a uniform superexponential bound in p. The double primitive G0 is continuous for the declared weights and its even boundary conditions come from zero mass. Hence `A_p→J`, `B_p=(ap/c)Psi_p→K`, with values, derivatives and moments.

For fixed positive q, the anticausal Green function is continuous with weight sigma>q; the cosh balances preserve Neumann and parity. When afterwards q→0 one must normalise **E/q**, not E: it converges to `H=G0(b0J−K)`. Strict positivity of H and Hmass follows from the unique crossing of its forcing. The product gamma E converges to `(Kmass/Hmass)H`; it is not assumed that gamma has a finite limit. Scaling A and B positively preserves the sign of U. The iterated order p→infinito, then q→0, suffices to transfer an eventual positive value to FINITE parameters p,q; joint uniformity is not used.

## Formulas and code

The moment formulas are Fubini with absolute integrability. Independent exact symbolic expansion verified

`720 I0²(K0 Hmass−Kmass H0)−P=0`.

The code fixes128 panels on[0,2], Taylor64/cap65,512 bits and16 modes before data. The centres and half-widths are exact dyadics. It includes the theta prefactor; it adds to all coefficients the full tail of modes **before** multiplying by t^r. It adds the exact symmetric Cauchy remainder and the full positive time tail to each of I0,...,I6. It checks precision and finiteness. The main sign is decided by P without divisions, accepts either sign and fails honestly if the enclosure contains zero. Kmass/Hmass are checked positive before auxiliary quotients. It imports no certificates and runs no other mesh.

## Scope

P>0 would refute exclusively the proposed negative/positive crossing of U for some FINITE parameters of the REAL pair. P<0 would only confirm the pointwise sign of the origin in the limit. Neither case proves a negative sign of W, global crossing, positivity of Xi nor closure of all orders. The transformed positivity of the remainder already proved099+102 remains intact.

Run authorised after this code review. Reproduction and result will be incorporated only after their real outputs.

## Certified result and reproduction

Run68812 and independent reproduction91737 ended exit0/PASS on all128 panels. Identical script hash: `5090a71fd7dd4ae786a3f785ca8a4c32d6691cf92af912d4e5fffff9e583d080`. No parameters were changed after data. The printed Arb enclosures are

- P: `[-3.1683047444094325e−13 ± 2.16e−30]`;
- U_lim(0): `[-1.35855717857699839e−6 ± 8.09e−24]`.

The proof is the outward interval asserts, including the full tails, not a floating reading. The sign is strictly NEGATIVE. By the iterated limits there also exist sufficiently small positive q and, for each sufficiently small chosen q, sufficiently large finite p with U_original(0)<0; the thresholds are not made explicit. This only confirms the orientation of the origin in that regime. It does not prove global crossing, positivity of Xi, propagation, a new W sign nor a falsifier. No additional tests are run.

## Later analytic extension — full limiting pair

**APPROVED, without new computations.** With b=Kmass/Jmass, H''=bJ−K and K''=aPhi−J. For r>0, F=H−rK satisfies

`D⁴F=(b+r)D²J−raD²Phi−aPhi+J`.

It is a nontrivial combination of the even Chebyshev4 family of102: the coefficient of J is1. If H/K had a positive stationary point, F would have a root of multiplicity at least2. Two applications of the even Rolle lemma with superexponential boundary conditions would give at least4 positive roots of D⁴F, counting multiplicities, against the maximum3 of Chebyshev4. It is not assumed that strict concavity implies a strict derivative: the stationary point is excluded directly.

Put I(t)=int_t^infinito(s−t)Phi(s)ds. Since tau=J/Phi decreases to0, for tau(t)<=a/2 one has K(t)>=aI(t)/2; moreover H(t)<=b int_t^infinito(s−t)J(s)ds<=b tau(t)I(t). Thus H/K→0. Positivity of H,K and absence of stationary points fix (H/K)'<0 at EVERY t>0.

The quotient Hmass/Kmass is a strict average of H/K under K. Hence U_lim=K−(Kmass/Hmass)H has exactly one simple positive crossing, negative/positive. Zero mass and that crossing imply Xi_lim=G0 U_lim>0, even and with correct boundary conditions. This decides the global limiting pair, and in particular the sign at the origin that the previous certificate verified independently. The GLOBAL crossing for finite parameters p,q is not obtained by continuity; it remains pending. The chronology of the single test103 is kept and no more tests are run.

## Analytic extension — all positive q in the pair (J,K)

**APPROVED.** Fix q>0, d=q ZK(q)/ZJ(q)>0, E_q=Gq(dJ−qK)>0. For r>0 and F=E_q−rK, direct computation gives

`(D²−q²)F''=(d+r)J''−raPhi''+a(rq²−q)Phi+(q−rq²)J`.

The EVEN4 combination is not zero because d+r>0. If (E_q/K)' vanished at a positive t, choosing r=E_q(t)/K(t)>0 would produce a double root of F. Even Rolle D² adds a positive root, and weighted Rolle Lq adds another, including multiplicities and boundary conditions: at least4 against the maximum3. Hence the derivative of the quotient never vanishes. For EACH fixed t it depends continuously on q>0 (Green with supertails and positive denominators). Since E_q/q→H in C1 and (H/K)'<0, it is negative for small q; the connectedness of(0,infinito) and the absence of zeros fix its sign negative for EVERYq>0. No uniformity in t is required for this argument.

Strict average under K: ZE_q(0)/ZK(0) lies inside the range of E_q/K. Thus U_q=K−[ZK(0)/ZE_q(0)]E_q has exactly one simple negative/positive crossing and Xi_q=G0U_q>0 for EVERYq>0. The restriction q→0 is removed from the final result for the pair(J,K), but it is still p→infinito: NO global crossing is inferred for any finite p nor a new W coverage.

## Exact bridge to finite p and a different obligation

**Identities and monotonicities APPROVED.** With lambda=p²c/(ap−c), beta c=a lambda and beta p−p²=lambda. The equations and boundary conditions give exactly `beta D_p+p²Psi_p=lambda K`, and `LpPsi_p=J−lambda K`. The transform at z=p gives d_*(p)=p/lambda, hence `Psi_p=(lambda/p)E_*(p)`. The monotonicity103 for all q implies (Psi_p/K)'<0 and (D_p/K)'>0 for EVERY FINITE p,t>0. This exact bridge does not assume stability of the crossing under limits.

For E=E_(p,q), put A=d lambda/beta, B=dp²/beta+q, gamma=massPsi/massE and alpha=gamma q−q²>0 (positive residue102). Then LqE=AK−BPsi and, for U=Psi−gamma E,

`LpLqU=J''−a(lambda+gamma A)Phi+[lambda−q²+gamma(A+B)]J−lambda alpha K`.

The coefficient of K uses Ap²−Blambda=−qlambda. Chebyshev4 for the MIXED family[K,J,Phi,J''] would suffice to exclude a double root of U by two weighted Rolle lemmas, but it does NOT follow from EVEN4 of102. The hypothesis remains open, keeping antecedents093/095. Under it, zero mass and U nonzero would impose a unique crossing. Its orientation does not come from the limit: a positive/negative crossing would make Xi=G0U strictly negative, contradicting even the non-strict bound R_next=d z ZXi/ZE>=0 obtained from099+102 by the auxiliary PSD block. For z different from q the Schur congruence applies directly; at z=q continuity suffices. The additional strictness already recorded is not needed for this orientation. The orientation would be negative/positive. Without the mixed input no finite Xi positivity nor new W is claimed. No additional certificate was launched.

Final literal reading of103§11 approved: exact bridge, mixed forcing and criterion only SUFFICIENT. The antecedents093/095 and the open intermediate obligation are expressly kept; no audit of that appendix remains pending.

## Three global prefixes of the mixed family

**APPROVED, without computations.** For f=A K+B Phi+C J, `D²f=AaPhi−AJ+B D²Phi+C D²J` belongs to EVEN4 and is not trivial unless A=B=C=0. Three positive roots of f, counting multiplicities, would produce at least four of D²f by even Rolle and boundary conditions, a contradiction. This proves extended Chebyshev of dimension3 for[K,Phi,J].

Let tau=J/Phi and kappa=K/Phi=tau(K/J). Both are positive and strictly decreasing to0. S=kappa'/tau'>0 satisfies `W(Phi,J,K)=Phi³(tau')²S'`, which never vanishes by the confluent property. S' has fixed sign. If it were positive, kappa/tau would be the average of S on the tail with measure−tau'(s)ds, strictly greater than S(t); then (kappa/tau)'=tau'(S−kappa/tau)/tau>0, contradicting(K/J)'<0. Hence S'<0 and d²kappa/dtau²=S'/tau'>0. In the order[K,J,Phi], the first three Wronskians are positive: K>0, W(K,J)=−J²(K/J)'>0 and W(K,J,Phi)=−W(Phi,J,K)>0. Only the fourth Wronskian of the mixed family remains open; it is not inferred from these prefixes.
