# POWER_REAL_SECOND_PAIR_AND_TP2_112 — Second positive pair and TP2 of the real family

## Verified update: reproduction finished and WM activated

The logs of the original run and the independent reproduction of110 are byte-for-byte identical, SHA256 `90a2ec137e806c8a7f8cce975f7af1cee375d9e48bdaf1c5bc302f7c06428539`. Driver: `c629d4ed4b5eeb625a69ee92f6000892b9493c50e825e9ade73bf3a5a9362108`; the four imported modules keep the audited hashes. It was checked by exact fractions that the full origin (16 leaves in lambda[0,1/4]) and 4198 contiguous REST leaves from1/2 to845/32 appear in BOTH logs. Both programs ended INCONCLUSIVE at8192 evaluations; that label is not changed nor is FULLPASS up to64 claimed.

The analytic tail104, independently audited, proves Wmixed/Phi^4>6t^2/y^2 for every t>=16. Hence the reproduced coverage and that tail overlap and prove WM for EVERY t>0. The three prefixes103 complete MIXED4. The real application of the audited implications112 is thereby activated: second positive density Xi for all p,q>0, E/Psi decreasing, strict TP2 and confluence. The code of§8 and the two independently verified forcings were also reviewed: the comparisons of the limiting star pair are activated. Xi_(p,q)/E_(p,q) decreasing for finite parameters, five arbitrary powers, all orders or a new window are not claimed.

The later mentions of a pending replica or conditional application describe the state prior to this update and are superseded exclusively by this evidence. The global sign remains OPEN. See `POWER_REASSESSMENT.md` for the change of strategy.


Status: **ANALYTIC IMPLICATION PROVED; global REAL application CONDITIONAL until the independent reproduction of the mixed compact is confirmed.** This source does NOT yet declare the global mixed sign proved. The tail t>=16 of104 is proved analytically; the compact closure and its reproduction must be confirmed separately before activating the following results. No new computations in this source. Papers untouched.

## 1. Consultation and substantive difference

Consulted the project rules, ROUTES-TRIED-INDEX/README.md, R162_2300_MASTER_GRID.md and CROSSWORD-TO-D.md; cross-checked083,099,102,103,104,106–110 and111. The three indexes record the mixed criterion103 and the auxiliary NO-GO111, but not an activated global proof of the second pair nor of TP2 of the REAL family.

103 already identified the mixed forcings and the exact bridge between the finite pivots and the pair(J,K). Here the full consequence of closing that sign is proved: a new positive time numerator for ALL two finite pivots, monotonicity of the second pair and strict TP2 between different real resolvents. TP2 is not inferred from the individual monotonicities or from full parametric monotonicity:111 falsifies that implication for another class. The input used here is specific and stronger, the real mixed system with its four Wronskians.

It is neither the abstract Hankel hierarchy083 nor a new writing of the global target: a concrete step of time positivity and comparison between TWO parameters is proved. That step is not promoted to arbitrary orders.

## 2. Activation hypothesis, data and root count

Phi,J,K,a are exactly those of102/103, with K EVEN. All functions used are even, real analytic and have supertails with the necessary derivatives. Define Lp=D_t^2-p^2. The only hypothesis additional to the already proved sources is

    W_t(K,J,Phi,J'')(t)>0 for EVERY t>0.          (WM)

103 section11.4 already proves that the three initial Wronskians of the order[K,J,Phi,J''] are strictly positive. Under WM, weighted Rolle gives an extended Chebyshev system of dimension4: every nontrivial combination has at most three positive roots counting multiplicities. This is the property called MIXED4 below.

The lemmas with boundary conditions102 are used. An even function h with supertails and m positive roots produces at least m+1 of Lp h: divide by cosh(pt), differentiate and use the even boundary condition at0 and the boundary conditions at infinity; the identity is

    [cosh(pt)^2(h/cosh(pt))']'=cosh(pt)Lp h.

Multiplicities are kept. Applying two operators Lp,Lq gives at least m+2 positive roots. The arguments apply to any finite list; they do not presuppose finiteness of roots before proving it. Null combinations are discarded by means of the explicit nonzero coefficient of the corresponding forcing and the independence of MIXED4.

## 3. Second pair: U has one crossing and Xi is positive

For p>0 write c=M(p), beta=ap^2/(ap-c), lambda=p^2c/(ap-c).102/103 prove

    D_p>0, Psi_p>0,
    beta D_p+p^2Psi_p=lambda K,
    LpPsi_p=J-lambda K,
    (Psi_p/D_p)'<0.

For q>0 define, with two-sided transforms,

    F(z)=z ZPsi_p(z)/ZD_p(z)=G_p(z)/c,
    d=F(q)>0,
    E=G_q(dD_p-qPsi_p)>0,
    gamma=massPsi_p/massE>0,
    alpha=gamma q-q^2>0,
    C=d lambda/beta>0, D=dp^2/beta+q>0.

Here G_q is the anticausal Green function102, not the remainder G_p. One has LqE=CK-DPsi_p and Cp^2-Dlambda=-qlambda. The symbols C,D in this source are coefficients; D_p remains the density of the first denominator.

The new weight U=Psi_p-gamma E is even and of zero mass. The exact computation103 gives

    LpLqU=J''-a(lambda+gamma C)Phi
       +[lambda-q^2+gamma(C+D)]J-lambda alpha K. (U-FORCE)

The MIXED4 combination is not trivial: its coefficient of J'' is1. If U had two positive roots counting multiplicities, the two Rolle lemmas would produce at least four of U-FORCE, a contradiction. U has at most one simple positive root. It is not zero and has zero mass, so it must have exactly one sign change.

The orientation is fixed using only an ALREADY PROVED nonnegative scalar sign, without inferring time signs from a transform.099,102 and103 section11.3 give R_next(z)>=0 for all p,q,z>0: the triples of the kernel of F at positive nodes pass to an auxiliary PSD block when a node is taken to0, and its two pivots d/q and aF-d/q are positive. The double Schur congruence leaves R_next(z)/z nonnegative. There is no need to transfer strictness through that limit. For Xi=G_0U, zero mass ensures smooth parity and the boundary conditions;102 gives exactly

    Xi''=U, Xi'(0)=0,
    R_next(z)=d z ZXi(z)/ZE(z).

If the unique crossing of U were positive/negative, all its tail integrals would be negative; Xi'>0 and Xi(infinito)=0 would imply Xi<0. This would make ZXi(z)<0 and R_next(z)<0, a contradiction. Hence

    U(t)<0 for 0<t<b, U(t)>0 for t>b,
    b is its unique positive crossing, simple,
    Xi(t)>0 for EVERY real t.                    (SECOND-POSITIVE)

Strict positivity of Xi follows from the tail integral of U, strictly positive for every t>0, and from Xi' negative with limit0 at infinity. Now Xi>0 also implies R_next(z)>0, without requiring it in the orientation argument. Thus E,Xi form a NEW positive pair for ALL finite pivots p,q>0.

## 4. The second time comparison E/Psi_p also decreases

For r>0 let H_r=E-rPsi_p. The same equations give

    LpLqH_r=-rJ''+a(C+r lambda)Phi
       -[C+D+r(lambda-q^2)]J
       +lambda(q-rq^2)K.                         (RATIO-FORCE)

The coefficient of J'' is-r, strictly negative. MIXED4 and two Rolle lemmas imply that H_r has at most one simple positive root. A stationary point of E/Psi_p, with r=E(t)/Psi_p(t)>0, would produce a double root of H_r. Hence (E/Psi_p)' never vanishes for p,q,t>0.

The orientation is fixed directly at finite parameters, without a tail estimate or a new limit. The continuous never-zero derivative has constant sign in t. By SECOND-POSITIVE,

    U=Psi_p[1-gamma E/Psi_p]

is negative before its crossing and positive after; hence E/Psi_p passes from values greater than1/gamma to smaller values. Its derivative cannot be positive. Consequently

    (E_(p,q)/Psi_p)'(t)<0
       for ALL p,q,t>0.                      (SECOND-RATIO)

This argument requires neither uniform convergence on the whole time half-line nor transport from p infinite: it uses the already proved finite real crossing and the global non-vanishing of the derivative.

## 5. Exact divided difference and strict TP2

Put V(x,t)=Psi_(sqrt(x))(t), x>0. For q!=p,

    lambda_p=ZJ(p)/ZK(p),
    v_pq=(lambda_q-lambda_p)/(q^2-p^2).

The first identity comes from transforming LpPsi_p=J-lambda_pK and evaluating at z=p. Evaluating at z=q and using the bridge beta D_p=lambda_pK-p^2Psi_p gives

    ZPsi_p(q)=v_pq ZK(q),
    d=q beta v_pq/(lambda_p-p^2v_pq),
    eta=q+dp^2/beta=q lambda_p/(lambda_p-p^2v_pq)>0,
    C=eta v_pq.

The denominator is positive because it is beta ZD_p(q)/ZK(q); its sign is not assumed from an abstract divided difference. Applying Lq and using the two boundary conditions proves the exact identity

    E_(p,q)(t)=eta[Psi_p(t)-Psi_q(t)]/(q^2-p^2). (DIVIDED-GREEN)

Indeed Lq of its right side is eta v_pq K-eta Psi_p=CK-DPsi_p, since eta=D. It is the forcing of E. The homogeneous difference with supertails at both ends is zero.

Dividing by Psi_p and differentiating in t, SECOND-RATIO implies

    derivative_t[Psi_q/Psi_p]
       =-(q^2-p^2)/eta * derivative_t[E_(p,q)/Psi_p]
       >0 for q>p.                             (CROSS-RATIO)

Thus, for 0<x1<x2 and0<t1<t2,

    det[[V(x1,t1),V(x2,t1)],
         [V(x1,t2),V(x2,t2)]]>0.                 (STRICT-TP2)

The specific time sign obtained through MIXED4 has been used. STRICT-TP2 is not deduced from mere positivity of E nor from individual monotonicities;111 shows why that shortcut would be incorrect.

## 6. Strict confluence

The anticausal integrals and the coefficients lambda are smooth in the positive parameters, with continuous derivatives in t on compacts. The confluent case can be proved directly, without transferring strictness through a limit. Write lambda(x)=ZJ(sqrt(x))/ZK(sqrt(x)) and Lx=D_t^2-x. The identity LxV=J-lambda(x)K gives

    Lx(-partial_xV)=lambda'(x)K-V.

Differentiating the transformed identity and evaluating at z=p, x=p^2, proves lambda'(p^2)=ZPsi_p(p)/ZK(p)>0. In the forcing LpE_(p,p)=CK-DPsi_p, the transformed balance at z=p gives C/D=lambda'(p^2). By uniqueness with the boundary conditions,

    E_(p,p)(t)=-eta_(p,p) partial_x V(p^2,t),
    eta_(p,p)=D=p+F_p(p)p^2/beta>0.

The inequality SECOND-RATIO was also proved directly for q=p, by means of the same coefficient-r of RATIO-FORCE. Dividing this identity by V(p^2,t) and differentiating in t gives

    partial_t partial_x log V(x,t)>0
       for EVERY x,t>0.                         (STRICT-CONFLUENT)

Since E_(p,p)>0, also partial_xV(x,t)<0, but complete monotonicity in x of all orders is not claimed. STRICT-CONFLUENT and STRICT-TP2 are comparisons of order2; they do not constitute TP of arbitrary orders.

## 7. Precise scope and next undischarged preservation

Once WM is activated by independent reproduction, the substantive results are SECOND-POSITIVE, SECOND-RATIO, STRICT-TP2 and STRICT-CONFLUENT for the REAL family. Nonnegativity of the scalar transformed remainder, sufficient for the orientation, was proved099/102/103; what is new is the positivity of its selected inverse density and the time comparisons, which had not been inferred from that scalar sign.

For the pair of FINITE parameters(p,q) it is not proved that Xi/E decreases. For H=Xi-rE, the computation of the next obligation shows why the same argument is not repeated automatically:

    LpLq(H'')=[1+r(C+D)]J''-raC Phi''
       -a[lambda+gamma C+rq lambda]Phi
       +[lambda-q^2+gamma(C+D)+rq lambda]J
       -lambda alpha K.

The fifth function Phi'' appears, in addition to MIXED4. A new comparison for that family or for its restricted coefficients would be needed. That preservation is not claimed, nor TP3/TPinf, nor a closed positive cone of all orders.

Nor is a new window T or five arbitrary powers of the full form W obtained. The coverage of four arbitrary exponents085 and that of thirteen exponents>=32 of053 remain as they were. The nodes0 of the congruences used are auxiliary, not new admissible tests. The proof of the global sign remains OPEN.

Until the compact reproduction that activates WM is confirmed and recorded, ALL new global results of this source remain CONDITIONAL. No paper is modified nor is computation run for this deduction.

## 8. Additional comparison of the limiting pair (J,K), for ALL q>0

This extension also remains **CONDITIONAL on WM**. The identities were verified independently; no other test is run. To avoid confusing it with the finite pair E_(p,q),Xi_(p,q), stars are written here for the objects of103:

    d*_q=q ZK(q)/ZJ(q)=q/lambda_q,
    E*_q=G_q(d*_q J-qK)>0,
    gamma*_q=massK/massE*_q,
    U*_q=K-gamma*_q E*_q,
    Xi*_q=G_0U*_q>0.

Positivity and unique crossing of this STAR pair are already proved103 for all q>0; what is new under WM will be its next monotonicity. Put lambda0=massJ/massK=1/b0 and V0=lambda0H, with H of103. The convergence V(x,t)->V0(t) in local C1 as x->0 comes from FINITE-GREEN and E*_q/q->H. Integrating LqPsi_q=J-lambda_qK gives

    lambda_q-lambda0
       =q^2 massPsi_q/massK>0.

The exact bridge103 and the masses give

    E*_q=(q/lambda_q)V(q^2,.),
    gamma*_q=q lambda_q/(lambda_q-lambda0).

Moreover, differentiating twice and using the boundary conditions verifies

    Xi*_q=[V0-V(q^2,.)]/(lambda_q-lambda0).        (STAR-IDENTITY)

Indeed, the numerator has second derivative (lambda_q-lambda0)K-q^2Psi_q, exactly (lambda_q-lambda0)U*_q.

STRICT-TP2 extended to the parameter0 by continuity gives that V(q^2,t)/V0(t) is NONDECREASING in t. Strictness is not attributed to this limit. Thus

    Xi*_q/E*_q
      =[lambda_q/(q(lambda_q-lambda0))]
                    [V0/V(q^2,.)-1]

is nonincreasing. To exclude stationary points, fix r>0 and F=Xi*_q-rE*_q. Its exact equations give

    Lq(F'')=a(1+rq)Phi
       -(1+gamma*_q d*_q+rq)J
       +(gamma*_q q-q^2)K-rd*_q J''.             (STAR-FORCE)

The coefficient-rd*_q is nonzero. MIXED4 and the two Rolle lemmas, D2 followed by Lq, exclude a positive double root of F. Hence the derivative of the quotient never vanishes. Together with the nonpositive sign already proved,

    (Xi*_q/E*_q)'(t)<0
       for ALL q,t>0.                        (STAR-RATIO)

### Additional confluence q->0

103 proves Xi*_q->Xi_lim and E*_q/q->H in local C1. Thus q Xi*_q/E*_q->Xi_lim/H in local C1. STAR-RATIO only allows concluding from that limit a NONPOSITIVE derivative. To obtain strictness independently, fix r>0 and F=Xi_lim-rH. With gamma_bar=massK/massH and H''=b0J-K,

    F''''=a(1+r)Phi
       -(1+r+gamma_bar b0)J
       +gamma_bar K-rb0 J''.                     (ZERO-STAR-FORCE)

It is a nontrivial MIXED4 combination, with coefficient-rb0. Two applications of lemma D2 exclude a positive double root of F; hence the derivative of Xi_lim/H does not vanish. We conclude

    (Xi_lim/H)'(t)<0 for EVERY t>0.               (ZERO-STAR-RATIO)

This extension proves the next time quotient for the limiting STAR pair, using the same mixed comparison under WM. It does not replace the five-function obligation for Xi_(p,q)/E_(p,q) of FINITE parameters p,q, exhibited in section7. Indefinite propagation, TP of higher orders, five W powers nor a new window T are claimed. The reproduction that activates WM remains a prerequisite for declaring these global consequences proved.
