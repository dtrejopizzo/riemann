# POWER_THETA_DENSITY_ORIGIN_087 — Exact sign of the next Wronskian at the origin

Status: **PROVED for ONE point and an unquantified neighbourhood, independent audit approved and independent reproduction exit0/NEGATIVE with matching hash.** See `POWER_THETA_DENSITY_ORIGIN_AUDIT_087.md`. A necessary condition of the pointwise transport of four densities of the REAL Phi is decided. Neither the global sign of that Wronskian, a new sign of W, nor the closure of all orders is claimed. Papers untouched; no campaigns.

## 1. Object and difference relative to 086

Consulted the project rules, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; read 073–086, in particular the linear density identities and the Rolle/Hankel criterion of 083/084. 086 controls three densities using exactly N>0 of 077. The next step requires a higher-order inequality; it is not inherited from positivity of the previous minors.

For t>0, fix V=−logPhi, p=V', q=V'', r=V''' and the four odd densities

    rho1=tPhi, rho2=(tPhi)'', rho3=−Phi', rho4=−Phi'''.

Dividing by tPhi>0 one obtains

    (1,A,B,C),
    A=p²−q−2p/t,
    B=p/t,
    C=(p³−3pq+r)/t.

All the ratios have an even analytic extension to the origin. This source certifies the sign of the Wronskian with variable lambda=t² AT lambda=0, retaining the whole theta sum. That point was chosen because it is a necessary condition before proposing any global certificate; no pivots or ranges with a desired sign were sought.

## 2. Exact Darboux form and new obligation

With k=B'>0, J=(A'/B')'>0 and E=(C'/B')', 086 gives exactly

    J=tN077/[p(tq−p)²]>0.

The change of coordinate B and the Wronskian rule give

    W_t(1,A,B,C)=−k³J²(E/J)'.                       (RAISE)

Therefore the condition (E/J)'>0 would be sufficient for the negative sign of the pointwise determinant of four densities, by Rolle, using the already controlled three-function base. It is a NEW condition, not an automatic consequence of the sign of J.

In fact the four-row Wronskian is affine in V^(6)(t), with exact coefficient

    [V^(6)]W_t=−N077/[p t⁴].

077 controls N through derivatives up to V''''; by itself it does not fix the new jet. This observation does not allow the jets of the real Phi to be varied freely nor does it give a NO-GO: it only locates the additional quantitative datum that must be proved.

## 3. Symbolic limit without singular cancellations

Write the normalized even series

    Phi(t)/Phi(0)=sum_(j>=0)a_j lambda^j,
    lambda=t², a_j=Phi^(2j)(0)/[(2j)!Phi(0)], a0=1.

Multiplying the four functions (1,A,B,C) by Phi/Phi(0) eliminates all quotients before computing the limit. The resulting columns are

    phi,
    (tphi)''/t,
    −phi'/t,
    −phi'''/t,

with phi=Phi/Phi(0). The Wronskian of the ratios at lambda=0 is exactly detH, where

    H=[[a0, 6a1, −2a1, −24a2],
       [a1, 20a2, −4a2, −120a3],
       [2a2, 84a3, −12a3, −672a4],
       [6a3, 432a4, −48a4, −4320a5]].                (ORIGIN-MATRIX)

In general the matrix with unnormalized coefficients is divided by Phi(0)^4. Only even derivatives up to order 10 are required, not 12. The rows include the factors k! of the derivatives in lambda: they are not unnormalized Taylor coefficients.

Moreover W_t=(2t)^6 W_lambda for t>0, by the change-of-variable rule for Wronskians. Since the previous factors of RAISE are positive in the coordinate lambda near 0, a W_lambda(0)>0 would refute that sufficient transport condition near the origin, NOT the sign of W. The following certificate obtains the opposite sign and therefore gives no such obstruction.

## 4. Single rational enclosure of the complete theta sum

The verifier tools/power_theta_density_origin_087_verify.py reuses the outward 70-digit interval operations of 077, copied WITHOUT importing or running its mesh. pi is computed by Machin128 and exp by Taylor128 after dividing the argument by 2048 and eleven outward squarings.

Define S by Phi(t)=pi exp(5t/2)S(t), and

    Q0(y)=2y−3,
    Q_(j+1)(y)=2y(Q_j'−Q_j),
    S^(j)(0)=Σ_(m>=1)m²Q_j(pi m²)exp(−pi m²).

Q0,...,Q10 are generated exactly. Their maximal sum of absolute coefficients is B=1745986560; all degrees are <=11. Modes m 1,...,8 are retained. For ALL m>=9, pi m²>3m²>=243>11, and y^11exp(−y) decreases. With exp3>16,

    m²|Q_j(y)|exp(−y)<=B·3^11 m^24 2^(−4m²).

The consecutive ratio is <=(10/9)^24·2^(−76)<1/2. The COMPLETE tail of each S^(j), j<=10, is enclosed in [−epsilon,epsilon], with

    epsilon=2B·3^11·9^24·2^(−324)
      =24093226761510505348366812581954355/
       16687398718132110018711107079449625895333629080911349765211262561111091607661254297054391304192.

Before forming the a_j the WHOLE prefactor is kept:

    Phi^(n)(0)=pi Σ_(r=0)^n binom(n,r)(5/2)^(n−r) S^(r)(0).

The tails are added to all Sder and then propagated through the interval operations. The derivative of S is not used as if it were that of Phi. It is checked that the enclosures of Phi^(1), Phi^(3),...,Phi^(9) contain 0, in agreement with the known parity; those checks are validations of the implementation, not the proof of parity.

The determinant H is evaluated over its 24 permutations with outward rounding. The assert only requires that the resulting interval separate 0, without imposing in advance which sign must appear. There is no choice of precision, number of modes or tail based on the sign obtained.

## 5. Certified result and reproduction

The final pointwise run, after correcting the inherited header and renaming the script to 087, finished exit0:

    CERTIFIED origin Wronskian sign: NEGATIVE.

The exact interval was

    lower=−35600018069828449972375574599599903124108706418423624372844374475370483826219849/10^70,

    upper=−2225001129364278123273473412474993945256794144848122636536351986556379522095569/
           625000000000000000000000000000000000000000000000000000000000000000000.

In particular both endpoints are negative; the approximate figure −3.56000180698·10^9 only serves for reading, not as proof.

Run

    python3 03-research/phase-211-sign-sandbox/tools/power_theta_density_origin_087_verify.py

SHA256 of the final version:

    f8f28e5f33659ec7245e23906ab11addc5a04243f1d502a8a070dbf12d13d7b7.

The first enclosure of the same point had already given the same interval under the provisional name 086. The only change before the final run was the name and the docstring; the object, precision, tail or parameter were not altered to obtain the sign. It is not a campaign of cases.

## 6. Coefficient pattern that preserves the previous level

Let v_j=V^(j)(0) for even j. The exact symbolic expansion gives for the first three densities

    W_R3,lambda(0)=[(3v2²+v4)v6−20v2v4²]/180.

The four-density Wronskian is affine in v10 and its coefficient is

    [v10]W_R4,lambda(0)
       =[(3v2²+v4)v6−20v2v4²]/151200
       =W_R3,lambda(0)/840.                        (JET-RAISE)

The rest depends only on v2, v4, v6, v8 and is given explicitly by ORIGIN-MATRIX substituting the series of exp[−v2lambda/2−v4lambda²/24−...]. JET-RAISE is a triangular link between levels, not a proof that the rest preserves the sign. The new term v10 requires additional real information even though the coefficient of the previous level already has a sign.

## 7. Exact scope

The sign required for the pointwise sufficient condition R4 PASSES at the origin. By analytic continuity it also passes in some positive neighbourhood, with radius not quantified here. (E/J)'>0 has not been proved for all t>0, nor the pointwise sign of the four density determinants at all their nodes. The S4 density block has not been treated here either.

The global positivity of four generators 085 remains an independent result. 087 does not prove another W region, five generators, all orders or a time window. Its specific result is to decide, without a campaign, a possible real falsifier of the new transport strategy and to show the jet term that must be controlled at the next level.
