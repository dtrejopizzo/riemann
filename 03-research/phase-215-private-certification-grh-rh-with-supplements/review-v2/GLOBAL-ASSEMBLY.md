# Global assembly: obligations and deduction V2

Sources: main.tex of 46 in sources-v2.json; direct rereading of an:lem-R, an:lem-landau, an:prop-density, an:thm-criterion, au:twistprime, au:Zj, srcC and an:thm-main up to an:cor-GRH. This note certifies the implication indicated; it does not anticipate the discharge of its premises.

## Sufficient logical kernel

The conclusion requires SF, Sp and Cv for the data produced by an:thm-data. It does not require the window computations, the finite comparisons declared without proof, the rows of 43–45 or any assertion of novelty. Nor is it enough to check only the copies of statements in appendices.

SF receives seesaw, divisibility and kernel from 49/50. Sp receives the second moment of 51/52 and the reductions of 46. Cv receives inj, aux, factor, regular, onelift, hecke and mult from 53–56/51. The shared dependencies must be closed once only, with their full hypotheses. The phase of Paper 49, the exchange of 53 and the level/Higman of 55 are reviewed in the V2 ledgers, without assuming their conclusions from this assembly.

## Product and heights

In au:twistprime the same twist theta_iota serves the changes of basis at iota and at conjugate(iota): the definition of the index demands a matrix that serves for all the twists permitted at that prime. The mixed determinant is integral and costs 2 delta. It is not assumed that a complex automorphism commutes with conjugation: sigma'=c sigma c supplies the two Gram matrices needed; an exterior Cauchy–Schwarz followed by Fischer gives the archimedean bound. The multiplier in the height principle is algebraic, since its images under all the isomorphisms to Qbar_2 have bounded valuation; a transcendental could be sent to elements of arbitrary valuation. The product of rational norms gives the height inequality. This part is a proof, not a postulate of positivity of the lifts.

## Cv from its inputs

au:onelift and mult give Z_j(1)/Z_j(theta^j)=(Delta_j(theta^j)/Delta_j(1))(H_j(1)/H_j(theta^j))^d. The budgets add up to d(3A+r bud+10mx1+6k bud-k hdir). With r<=2k and k bud log b=fa(log b)^4/m it suffices that 3fm²b(log b)²+10m²x1<=fa(log b)³(log b-8), by m²<=4x and a=xb and the admissible sizes.

Completing n vectors with n'<=4d/b² auxiliaries allows au:twistprime to be applied. The ramified ratios cost at most b and the auxiliary archimedean cost is 2x1²b². Then

0 <= c+2delta+n'(2x1²b²+b)+d(b+fa(log b)^4-hmain).

The term in n' is <=db by the sizes, and 2b<=2fa(log b)^4. This yields Cv exactly. Each of its inputs must still have a valid proof in its instance; this arithmetic does not replace them.

## SF + Sp + Cv

Put L=fa(log b)^4, E=fa(log b)^3 and d=dim T>0. Sp supplies a family of translations with cost <=5d log(1+2b²). SF allows one to choose a basis of its image, of dimension n between (1-4/b²)d and d, with covolume<=n(hmain-m rem+L) and index<=10d log(1+2b²)E. Cv implies

n m rem <= d[4L+20log(1+2b²)E],

using hmain>=0 for n hmain<=d hmain. If rem<=0 the conclusion is immediate; otherwise d<=2n and log(1+2b²)<=3log b. By log b>=128 one obtains m rem<=fa(log b)^5. The sign of rem is preserved; there is no division by a quantity whose sign is unknown.

## From the remainder to GRH

The exact identity an:lem-rem and #Pa/#Pb<=log b give

R_d,q0(x)<=phi(q0)(log b)^6/m+|R_d,q0(x1)|+log b |R_d,1(x1)|.

For fixed q0,d, PNT is applied only at x1; its constants may depend on them. With m>=sqrt(x), log b<=2x^delta and log x1>=x^(delta/6)-1, the two remainders are O(x^-2). One obtains R(y)<=y^(-1/2+epsilon), passing from integers to reals at cost O(1/x).

The quadratic large sieve allows one to choose d in the required class whose twists have no zeros in a fixed box containing the candidate zero rho and the relevant real segment. The proof of density keeps the saving theta²/8: the truncation error saves theta(2-theta)/4; the sum over square products saves theta²/4 before the epsilons. GRH is not required for this selection.

The transform of R has residue (n_q(rho)-n_q^K(rho))/(phi(q)rho(1-rho)). The one-sided bound and Landau imply holomorphy in Re(s)>beta except for a possible real pole of negative residue. The selection of d removes the zeros of twists on the segment, so the real residues are non-negative and that alternative is impossible. At rho there is no cancellation by twists either: n_q(rho)=0. With q0=18480q every character is covered; the added Euler factors have zeros only on Re(s)=0. The functional equation of the primitive character gives the other half-plane.

**Verdict for this segment: (a), implication checked from SF/Sp/Cv for the constructed data to Dirichlet GRH and RH.** The pending conditions of SF/Sp/Cv are resolved in the specialist notes; they are not removed by calling the conclusion a certification.
