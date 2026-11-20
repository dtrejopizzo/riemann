# POWER_THETA_DENSITY_COMPACT_089 — Global sign of the real Wronskian R4 via densities

**Independent audit:** `POWER_THETA_DENSITY_COMPACT_AUDIT_089.md` approved; run 40406 FULL PASS, independent reproduction 87911 exit0/FULL PASS 1024+8192 and matching hash. Independent transport development: `POWER_THETA_DENSITY_TRANSPORT_089.md`.

Status: **PROVED, certificate and independent reproduction 87911 exit0/FULL PASS; mathematical and code audit approved.** The objects, domains, tails and parameters were fixed and audited before implementing and running. The transport of the R_SIDE via densities is proved; not S4 nor new W coverage relative to 085. Papers untouched.

## 1. Object and antecedents

Consulted the project rules, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; reread 077, 083–088. 087 decides the Wronskian R4 at the origin and 088 its exterior t>=1. The compact range 0<t<1 of the SAME Phi was missing. The pointwise density condition is stronger than the transformed curvature already proved in 085: it is not inherited from it.

Keep the four densities

    rho=(tPhi,(tPhi)'',−Phi',−Phi'''),
    K(t)=W_t(rho1,rho2,rho3,rho4).

Since rho=tPhi·(1,A,B,C),

    K(t)=(tPhi)^4 W_t(1,A,B,C).

There is no numerical division by Phi or by t. For the origin set lambda=t² and phi(lambda)=Phi(sqrt(lambda)), WITHOUT normalizing by Phi(0). The four densities divided by t are

    Psi=[phi,6phi'+4lambda phi'',−2phi',−12phi''−8lambda phi'''].

Here the primes of phi are with respect to lambda. The exact Wronskian identities give

    K(t)=64t^10 W_lambda(Psi)(t²).                  (BRIDGE)

Therefore two complementary obligations are fixed: W_lambda(Psi)<0 on 0<=lambda<=1/256, and K<0 on 1/16<=t<=1. Their union covers 0<t<=1 and avoids the order-10 cancellation at the origin.

## 2. Complex theta bound for the origin branch

If |t|<=1/4, then

    Re exp(2t)>=exp(−1/2)cos(1/2)>1/2.

It suffices that exp(1/2)<5/3, cos(1/2)>7/8 and (3/5)(7/8)>1/2. The first bound follows from e<87/32<25/9 and the second from the alternating series of cos. Moreover |exp(2t)|<2 and |exp(5t/2)|<2: for the second use exp(1/2)<5/3 and exp(1/8)<8/7.

Thus each mode satisfies on that disc

    |Phi_m(t)|<152m⁴4^(−m²),

using pi<4, pi Re exp(2t)>3/2 and exp(3/2)>4. The sum is bounded by 1000: the consecutive ratio of m⁴4^(−m²) is <=16/4³<1/2 and hence 152Σ<=76<1000.

The analytic parity of Phi gives a function phi holomorphic in a neighbourhood of the disc |lambda|<=1/16, with

    |phi(lambda)|<1000.

For |lambda|<=1/32, Cauchy with radius 1/32 gives

    |phi^(k)(lambda)|<=1000k!32^k.

In the Wronskian of Psi, the rows are derivatives of orders 0,...,3. With P_k=1000k!32^k, the four exact maximal column bounds are

    [P3,18P4+P5/8,2P4,36P5+P6/4]
      =[196608000,956301312000,50331648000,338228674560000].

The bound over the 24 permutations is less than 10^48. The same B_origin=10^48 can be used on ALL |lambda|<=1/32.

## 3. Partition and complete approximation at the origin

1024 equal panels of [0,1/256] are fixed, with exact positive centres and radius h_lambda=1/524288. At each centre the Taylor expansion of W_lambda(Psi) up to degree 16 is used, with disc r_lambda=1/64. All those discs lie in |lambda|<=5/256<1/32. The complete Taylor error is

    R_origin=10^48(1/8192)^17/(1−1/8192)<10^(−18).

Precision 1024 bits and phi cap 23 are fixed: the determinant needs coefficients up to degree 16 and derivatives of phi up to order 22, because the fourth column of Psi contains phi''' and is differentiated three times when forming the Wronskian.

To evaluate jets use EXACTLY

    phi16(lambda)=[Phi16(sqrt(lambda))+Phi16(−sqrt(lambda))]/2,

where Phi16 retains modes 1,...,16. The average is essential: an individual theta partial sum is not even, and its composition with sqrt would not be analytic at lambda=0. The function phi16 is; the centres are positive, so the formal series of sqrt have a defined real branch.

The COMPLETE tail on |lambda|<=1/16 is bounded by

    epsilon_origin=304·17⁴/4^289,

since from m=17 the ratio is <=(18/17)^4/4^35<1/2. The average of the two tails does not add a factor 2. At each centre, Cauchy with radius 1/32 gives a coefficient error of phi of order k at most epsilon_origin32^k. That ball is added to ALL coefficients 0,...,22 BEFORE forming Psi, its derivatives and the determinant. This tail is not replaced by a parity check or by floating-point precision.

## 4. Complex theta bound for the remaining branch

Let c0∈[1/16,1] and |z−c0|<=1/32. Then

    Re z∈[1/32,33/32], |Im z|<=1/32,
    |y|=|pi exp(2z)|<32, Re y>5/2,
    |exp(5z/2)|<16.

For the upper bounds exp(33/16)<8 and exp(165/64)<16 suffice, both comparisons with log2>56/81. For Re y, use pi>3, exp(2Re z)>1 and cos(1/16)>511/512. Hence

    |Phi_m(z)|<4288m⁴8^(−m²),
    |Phi(z)|<10000.

The coefficient 4288 is 4·16·(64+3); exp(5/2)>8 pays for the decay. The sum is bounded by a geometric series, with initial ratio 16/8³<1/2.

On the inner disc |z−c0|<=1/64, Cauchy with radius 1/64 stays in the outer disc and gives

    |Phi^(k)(z)|<=p_k=10000k!64^k.

Since |z|<2, the maximal column bounds of the raw Wronskian rho are

    [2p3+3p2,2p5+5p4,p4,p6].

Their 24 products lie below 10^60. Therefore B_rest=10^60 is a uniform bound of |K| on each inner disc.

## 5. Partition and tail of the remaining branch

8192 equal panels of [1/16,1] are fixed, with radius h_t=15/262144. The Cauchy radius for K is r_t=1/64, so h_t/r_t=15/4096. Taylor of degree 40 is used with complete error

    R_rest=10^60(15/4096)^41/(1−15/4096)<10^(−39).

The precision is 512 bits, Phi cap 47: the fourth density is −Phi''' and its third derived row uses Phi^(6), so the coefficient 40 needs Phi up to degree 46.

Phi16 is evaluated DIRECTLY as a function of t. No symmetrization is needed in this branch without sqrt. The complete tail on all outer discs is

    epsilon_rest=8576·17⁴/8^289,

with consecutive ratio from 17 less than 1/2. The Cauchy error epsilon_rest32^k is added to each coefficient k=0,...,46 BEFORE differentiating the densities and forming the Wronskian.

## 6. Sign asserts and parameters fixed before running

For EITHER of the two branches, the coefficients C_k of the determinant are normalized by k!. The negative sign on each panel is certified by

    C0.upper+Σ_(k=1)^degree |Ck|.upper h^k+Remainder<0.

All coefficients are required to be finite and the necessary formal precision (at least 17 for origin and 41 for rest). One does not pass from negative central values to an interval without the remainder. The theta tail balls are incorporated into the jets of phi/Phi, separately from the Taylor remainder of the determinant.

The two domains, their 1024/8192 panels, the precisions 1024/512, the degrees 16/40, caps 23/47, 16 modes and the tails are fixed by these derivations before implementing or running. There was no FAIL nor change of a parameter after running. No sign was obtained by a search over meshes or ranges.

## 7. Reproducible result

Stable code: tools/power_theta_density_compact_089_verify.py. It uses real Arb series with the two declared precisions and caps, adding the tail balls to ALL coefficients before differentiating. The determinant is computed by Laplace expansion along the first two rows: six products of 2x2 minors, without divisions. Formal precision at least 17/41 and finiteness of all necessary coefficients are verified.

Run 40406 finished exit0 and FULL PASS:

    ORIGIN:1024/1024 panels,W_lambda(Psi)<0 on [0,1/256];
    REST:8192/8192 panels,W_t(rho4)<0 on [1/16,1].

Run

    python3 03-research/phase-211-sign-sandbox/tools/power_theta_density_compact_089_verify.py

SHA256 of the exact version that finished, not modified during its execution:

    995ef292abf5a80a3d195b4e68a815e1b56f9b343531bc1c0786af682413d1aa.

The .sha256 file fixes the same version for reproduction. The theta tails and the two Cauchy remainders are printed as exact fractions. There was no evaluation of diagnostic signs nor adjustments after results: the two continuous obligations were those predeclared in this same file.

## 8. Splice, Rolle and global transport of the R side

BRIDGE and both certificates prove W_t(1,A,B,C)<0 on 0<t<=1. 088 supplies the same sign for ALL t>=1. Therefore

    W_t(1,A,B,C)<0 for ALL t>0.                    (GLOBAL-R4)

086 already gives B'>0 and J=(A'/B')'>0. With E=(C'/B')', the Darboux identity of 087 implies (E/J)'>0 for ALL t>0. In the order (1,B,A,C), the initial Wronskians have signs 1, B'>0, (B')²J>0 and −W original>0. No sign of A' is presupposed.

To prove the sign of the evaluation determinant, use the coordinate z=B(t). If a nonzero combination a+bB+cA+dC had four zeros, Rolle would give at least two zeros of cA_zz+dC_zz. Dividing by A_zz=J/B'>0 leaves c+d(E/J), which has at most one zero by its strict monotonicity, unless c=d=0. In that boundary case an affine function of B does not admit four zeros without vanishing identically. Thus the determinant does not vanish on the chamber of four ordered positive nodes; its confluent sign GLOBAL-R4 fixes it strictly negative in the original order (1,A,B,C). Multiplying the rows by t_iPhi(t_i)>0 preserves the sign of the four densities rho.

The kernel

    L(lambda,t)=sinh(sqrt(lambda)t)/sqrt(lambda)
                =Σ_(m>=0)lambda^m t^(2m+1)/(2m+1)!

has positive minors of size 4 for ordered positive nodes. The proof is that of 086, now with four rows: Cauchy–Binet on truncations produces products of determinants of monomials with strictly increasing exponents, positive by Rolle and their Wronskians. The terms m=0,1,2,3 guarantee strict positivity. The same holds for the confluent rows of derivatives 0,...,3 in lambda, by the Wronskians of lambda^m. Convergence of the series and their derivatives is locally uniform.

Two-sided integration by parts, with vanishing superexponential boundary terms, gives

    LT(rho)=(Z',u²Z',uZ,u³Z).

Dividing by u>0 and setting lambda=u² produces functions

    F=(Z'/u,uZ',Z,u²Z)
      =2∫_0^infinity L(lambda,t)rho(t)dt.

Andreief —expansion of determinants and Fubini— transports the negative sign of the density determinant to detF for four positive nodes lambda. Its confluent version also gives W_lambda(F)<0. Each term is absolutely integrable by the superexponential tails of Phi and its derivatives, even after the kernel derivatives on compact subsets of lambda>0.

Since F0=Z'/u>0 and

    F=F0·(1,lambda,R(lambda),lambda R(lambda)),

one obtains in particular

    W_lambda(1,lambda,R,lambda R)<0,
    2R'R'''−3(R'')²>0 for ALL lambda>0.            (REAL-R-TURAN)

The identity of the last Wronskian is exactly that of 084. Thus the R side now has a global proof via the densities of the SAME Phi, independent of the certificate in the parameter u of 085. No contribution of the complete form has been removed nor positivity of an unrelated kernel used.

## 9. Exact scope

The result is GLOBAL-R4 and the transport REAL-R-TURAN of the R_SIDE for all positive parameters. It does not treat the four densities of the S side nor prove an inheritance rule to higher levels. The three-density base 086 and the new four-density Wronskian were verified separately; that datum was not replaced by the generic concavity refuted in 084.

The W positivity of four generators 085 remains valid, but this result does not extend its admissible coverage, does not prove five generators, all orders or a time window. Its contribution is the density comparison that structurally explains and transports one of the two reciprocal signs. The global objective of the paper remains OPEN; papers untouched.
