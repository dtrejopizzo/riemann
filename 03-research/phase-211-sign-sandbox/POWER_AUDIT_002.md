# POWER_AUDIT_002 — Polarisation from scratch and approximation bridge

Status: PROVED (polarisation and bridge for smooth data with decay); OPEN (sign for three or more powers). Independent audit. Does not modify papers.

Consulted: the project rules, POWER_CONE_001.md, index README (current entry on powers and Pick antecedents), grid R162_2300_part3/part5 and CROSSWORD-TO-D.md. The isolated sign problem is respected. The new reason is to check the cross terms of an explicit family and build its approximation in a topology that controls each term; the construction is not discarded on the basis of reformulation labels.

## 1. Cross terms: there is no polar defect

Write h_u(y)=exp(-uy) for y>0, zero outside, u=a-1/2. For v=b-1/2, the symmetric bilinear autocorrelation is

    C_uv(t)=[exp(-ut)+exp(-vt)]/[2(u+v)], t>=0.

This follows from integrating each of the two shifted products over the half-line. Define

    g(a)=psi(a/2)/2-log(pi)/2+zeta'(a)/zeta(a),
    r(a)=1/a+1/(a-1), L(a)=g(a)+r(a).

The archimedean and comb terms of the polarisation are [g(a)+g(b)]/(a+b-1). The moments are A_a=1/(a-1), B_a=1/a; therefore the bilinear polar term is

    P_ab=A_a B_b+A_b B_a
        =1/[(a-1)b]+1/[(b-1)a]
        =[r(a)+r(b)]/(a+b-1).

The last identity is checked by multiplying by a(a-1)b(b-1)(a+b-1); it also results from factoring its numerator (a+b-1)(2ab-a-b). Hence

    W(h_u,h_v)=[L(a)+L(b)]/(a+b-1).

For rho_a(X)=X^-a, Z rho_a= zeta(a) h_u. Hence the correct coefficients are d_i=c_i zeta(a_i), and Q[rho]=sum d_i d_j K_ij as POWER_CONE declares. The factor 2 of the polar term, the autocorrelation and the comb were reviewed from scratch: no correction is required. On the diagonal Q[rho_a]=zeta(a)^2 L(a)/(a-1/2).

## 2. Results kept and scope

The two-point criterion, the estimate L-uL'>0 for a>=32 and its consequence on each plane of two powers survive. In the gamma estimate one can first obtain the more precise bound .5log(a/(2pi))-.5-7/(4a)+1/(2a^2), which implies the one used. The bound for S follows from Lambda(n)<=log n<=n. No order-three sign is inferred.

The falsifier H=3+cosh has, for u=log2, v=2log2,

    (log2)K=[[3/17,126/697],[126/697,15/82]],
    det((log2)K)=-387/971618,
    (42,-41)K(42,-41)^t=-129/(34log2).

It refutes exclusively the step from a positive cosh representation to the sign of all mixtures. It does not refute the arithmetic datum.

## 3. Bridge proved in a norm that controls the form

Fix 1/2<eta<31.5 and the space H_eta of functions h on [0,infinity) such that exp(eta y)h belongs to H^1(0,infinity), with its usual norm. The universal form W of the extension by zero is continuous on H_eta:

* The archimedean term is controlled because the extension by zero H^1(0,infinity) -> H^s(R) is continuous for 0<s<1/2, and |m(tau)|<=C_s(1+tau^2)^s. It is not presupposed that the extension by zero is H^1: it may have a jump at zero.
* For t>=0, Cauchy--Schwarz gives |c_h(t)|<=exp(-eta t)||exp(eta y)h||_2^2. By polarisation the difference of two forms is also controlled. The comb sum converges, since sum v_n n^-eta=2 sum Lambda(n)n^-(eta+1/2)<infinity.
* A and B are continuous functionals by Cauchy--Schwarz, since eta>1/2.

The linear span of {exp(-(31.5+k)y): k=0,1,...} is dense in H_eta. Constructive proof: smooth functions with compact support in [0,infinity) are dense in H_eta (without imposing value zero at the endpoint). For one of them set z=exp(-y), h(y)=z^31.5 f(z). The function f is smooth on [0,1], identically zero near zero. Approximate f and f' uniformly by a polynomial P and its derivative: approximate f' by a polynomial and then integrate adjusting f(0). Then

    |z^31.5(f-P)| <= epsilon z^31.5,
    |d/dy[z^31.5(f-P)]| <= (31.5+1)epsilon z^31.5.

The weighted integral converges because eta<31.5. This proves the approximation in H_eta. Each approximant is the Z image of a finite combination of X^-(32+k), dividing its exponential coefficient by zeta(32+k)>0.

**Exact consequence:** if positivity of ALL finite matrices of powers with exponents 32+k is proved, one obtains the sign of W for every h in H_eta by continuity. In particular it transfers to any exterior datum whose Zrho belongs to H_eta. For rho smooth with rapid decay and derivatives with rapid decay, this is verified by summing the series of Z and its derivative: for every M>1, they are O(exp(-(M-1/2)y)).

This bridge is a positive approximation result, not a proof of the sign of the matrices. The approximants may require arbitrarily many generators and coefficients of both signs. The existing result on a union of planes does not authorise its passage to the limit. Nor is it claimed here that every C^2 representative of PW_N lies in H_eta: their concrete regularity and decay must be treated, or one works on a smooth core and justifies the relevant closure afterwards.

## 4. Next mathematical obligation

The constructive bottleneck of this route is located: prove the sign of matrices of order three and then a structure for all orders. The approximation bridge is already available for smooth data; it need not be invented again nor confused with an inference from order-two minors. Keep separate universal sign, PW_N constraints and coercivity relative to the gauge.

## 5. Reviewed extension: the fractional bridge covers PW_N C²

POWER_BRIDGE_002.md resolves the regularity limitation of §3. Independent review: APPROVED. Its norm is ||e^(5y/4)rho(e^y)||H^(1/4)(0,infinity). Two integrations by parts, both for h and for xh, give rho,rho'=O(X^-2) for the PW_N C² datum. Hence G=e^(5y/4)rho(e^y) satisfies |G|<=Ce^(-3y/4), |G'|<=Ce^(y/4). For 0<delta<1, splitting at R=log(1/delta) gives

    integral_0^R |Delta_delta G|² <= C delta² exp(R/2)=C delta^(3/2),
    integral_R^infinito |Delta_delta G|² <= C exp(-3R/2)=C delta^(3/2).

The H^t seminorm is finite for t<3/4; the extension by zero is continuous for t<1/2. The crucial point is NOT to differentiate the Z series term by term: rho'=O(X^-2) would not give absolute convergence of that derivative. Instead,

    e^(3y/4)Zrho(y)=sum n^(-5/4) G(y+log n)

converges in H^(1/4) by the contraction property of each forward translation. This controls the form, comb and poles as B1/B2 of the memo show. The polynomial approximation of §3 of the same memo produces exponents 33.25+k, all >=32, and converges in that norm. Therefore the bridge to ALL of PW_N C² is proved. It does not yet claim the sign of matrices of arbitrary size.

## 6. Direct bridge by translation for the sign of windows

There is also a more direct consequence of the H_eta bridge of §3. If the kernel is positive at ALL sizes for exponents 32+k, W is nonnegative on all of H_eta by density. For any smooth F with compact support on the line, translate it far enough to the right that its support lies in (0,infinity). The translate belongs to H_eta. The full form is translation invariant: the archimedean and comb terms are, by autocorrelation, while A multiplies by e^(d/2) and B by e^(-d/2), preserving their product. Thus one obtains W(F)>=0 for any such F. In each fixed window, continuity in the form norm and density of the smooth core extend that inequality to the domain of the form; on P_T the moments vanish and the required sign of a_T remains.

This is a conditional constructive implication from ALL sizes of the power kernel. It requires neither a coercive bound relative to the gauge nor a positive margin. The existing proof for size two or three does not yet satisfy the hypothesis.

## 7. Audit of the three-generator advance

POWER_THREE_002.md reviewed from its formulas: APPROVED for u>=2^30 and three rates in [u,3u]. The written rational orthonormal basis corresponds to the Fourier convention with exp(-i tau y); the multiplier m is even and the computation is independent of that choice. The sum of the envelopes of the three vectors is sqrt(6u)e^(-uy)(3+18uy+18(uy)^2). The constant 327, the tail bound and the comb estimate follow. To verify 654sqrt(6)<1602 it suffices that 267²>6*109²; at p=16 its comb bound is less than .028. The polar term is bounded by 12*366²/u<.1 in the range. The spectral density has maximum 3/(pi u), and the principle of filling the central interval first minimises integral log|tau|, giving the term log(pi u/6)-1 with the correct factor two. The resulting archimedean bound is >10||f||². Therefore the declared margin Q>=9||f||² is justified.

It does not require a minimal separation of rates. The all-pass basis remains valid for repeated rates as a basis of the confluent space of exponentials times polynomials. This order-three result is kept as a bounded positive advance, without inferring all orders.

## 8. Review of all orders with increasing threshold

POWER_THREE_002 §§7–8: APPROVED. The convolution identity produces exactly P_n(z)=sum_{k=0}^{n-1} binom(n,k+1)6^k z^k/k!, and z^k/k!<=2^k e^(z/2) gives P_n<=13^n e^(z/2). Integrating the polynomial before applying the envelope gives the moment 2sqrt(6)13^n/sqrt(u). The bounds for the polar term 48*169^n/u and for the comb <15*16^n*2^(-20n-10) are valid for u>=2^(40n), and each is <.1. The spectral argument gives arch>10; the margin W>=9||f||² is kept for every n with that threshold.

The declared non-density is also exact: every unit direction of the union has norm on [1,infinity) <.01. For a unit test on [1,2], the inner product with each direction is <.01; its distance to each real line generated by such a direction is >=sqrt(1-10^-4). Therefore the union with arbitrary scalars is not dense. This does not rule out the general power strategy: it locates the pending obligation in a common family of rates or in control of cross terms between families already positive.

## 9. Refinement to the exact ladder and finite inversion

The updated POWER_BRIDGE_002 chooses B=123/4 in its polynomial approximation, so the exponents are exactly 32+k (replacing the auxiliary range 33.25+k cited in §5 of this audit). The change preserves all density bounds because B>0.

Its new §6, independently reviewed, also provides a finite realisation for every smooth test h supported in (0,L): u(y)=sum mu(n)n^-1/2 h(y+log n), rho(e^y)=e^-y/2 u(y). When applying Z, only pairs kn<=e^L contribute. Regrouping is finite and the sum of mu over divisors gives Zrho=h. Membership in B is immediate because u is smooth up to zero and compactly supported on the half-line. There is no need to assume surjectivity of an infinite operator.

What remains is an explicit sufficient obligation: prove semidefiniteness of K^(m)_ij=[L(32+i)+L(32+j)]/(63+i+j), 0<=i,j<=m, for all integers m. This step is not yet proved. Both the approximation and its link with every window test are proved, without requiring a positive margin or coercivity on the gauge.

## 10. Rational certificate of the fixed ladder, round 003

Reviewed tools/power_fixed_grid_003.py and POWER_FIXED_GRID_003.md: APPROVED. An independent python3 rerun reproduces the six positive pivots and the six Schur parameters of the memo, including the sixth pivot between 70566563152624/10^30 and 70566563152625/10^30. The sign checks operate only with Fraction and directed rounding to 10^-60; the floats of the __repr__ method play no role in the checks or in the normal certified outputs.

Audited details: atanh series for log with omitted first term of degree 241 and geometric tail; Machin formula and positive alternating remainder after 100 terms; gamma by Euler–Maclaurin of H_1000 with B_2,...,B_24 and next bound B_26=8553103/6; recurrences of psi at integers and half-integers; tails of zeta and of its derivative via integrals from 50, valid by monotonicity in a>=32. In the in-place LDL the update only modifies entries with indices i,j>k, so the column k multiplying each correction remains intact throughout that step. The scalar recurrence likewise does not modify its pivot q[r] during the update of the remaining sites. The declared congruences of the kernel and its complement are correct.

The rational falsifier of POWER_FIXED_GRID_003 §4 was also recomputed: det=-332001/391435520 and the three order-two minors coincide with their declared fractions. The finite scope is kept: neither alternating parameters nor a uniform bound are extrapolated from six cases.
