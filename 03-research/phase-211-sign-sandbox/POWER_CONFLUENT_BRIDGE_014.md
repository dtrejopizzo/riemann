# POWER_CONFLUENT_BRIDGE_014 — A single confluent rate suffices, in strong norm

Status: PROVED. New precision of the bridge: not only L² density is used. Papers untouched.

## 1. Antecedents and difference

Consulted the project rules, index/grid/crossword according to the previous audits; POWER_BRIDGE_002, POWER_PACKET_SCOPE_AUDIT_009, POWER_COMMON_TRANSFER_010 and confluent certificates004–013. Bridge002 proved sufficiency of a fixed ladder of distinct rates32+k via a weighted fractional norm. The difference here is to prove strong density of ALL degrees with ONE SAME fixed rate u. No sign is attributed to that density: positivity of all blocks remains a separate obligation.

## 2. Elementary lemma: exponentials times polynomials dense in H¹ of the half-line

For any a>0,

    span{y^k exp(-ay): k=0,1,...}

is dense in H¹(0,infinito), with no condition on the value at0.

Proof. It suffices to show that its orthogonal complement for the H¹ product is zero. Let h be in that orthogonal complement; complexify if needed. Define for Re z>0 the bilinear analytic function

    J(z)=integral_0^infinito [h(y)e^(-zy)-z h'(y)e^(-zy)]dy.

All derivatives with respect to z converge locally by Cauchy--Schwarz and the exponential decay. Orthogonality to y^k e^(-ay) is exactly J^(k)(a)=0 for all k, since differentiating the second term too reproduces the temporal derivative of the test. By analyticity, J is identically zero on the connected half-plane Re z>0.

Write H(z)=integral h(y)e^(-zy)dy. Integrating h' by parts gives

    integral h'(y)e^(-zy)dy=-h(0)+zH(z),
    J(z)=(1-z²)H(z)+z h(0).

The integration is legitimate for H¹: it has a trace at0, and the endpoint at infinity vanishes against e^(-zy). Evaluating at z1, where H is analytic, gives h(0)=0. Thus (1-z²)H(z)=0 and H is zero on all of Re z>0. Uniqueness can be checked by taking any vertical Re z=c>0: it is the Fourier transform of the integrable function e^(-cy)h(y) extended by zero. Hence h=0. The Hilbert projection theorem proves the announced density. No Robin condition is imposed on the closure: the term h(0) was precisely necessary to rule it out.

## 3. Weighted norm controlling the whole form

Fix u>1/2 and choose eta with1/2<eta<u. Set

    H_eta={f: exp(eta y)f(y) belongs to H¹(0,infinito)},
    ||f||_eta=||exp(eta y)f||H¹.

Multiplying by exp(eta y) identifies polynomials times exp(-uy) with polynomials times exp(-(u-eta)y). Lemma§2 applies because u-eta>0. Thus

    union_N span{y^k exp(-uy):0<=k<N}

is dense in H_eta.

The complete form W of the zero extension is continuous on H_eta, by the estimates already audited, which are listed to fix its topology:

* The zero extension H¹(0,infinito)->H^s(R) is continuous for0<s<1/2, without requiring f(0)=0. The multiplier m has logarithmic growth and its form is controlled by that norm.
* With the weight e^(eta y), the shifted bilinear correlations are bounded by e^(-eta t) times the two weightedL² norms. The sum2sum Lambda(q)q^(-eta-1/2) converges because eta>1/2, and controls the WHOLE comb and its differences.
* Both polar moments are continuous by Cauchy--Schwarz, since e^((1/2-eta)y) is square integrable.

These bounds are bilinear and prove real or Hermitian continuity of W, not merely finiteness on each member of a sequence. The density obtained is therefore strong enough to pass a sign inequality to the limit.

## 4. Exact sufficient consequence

If for a SINGLE rate u>1/2 all finite Laguerre blocks

    V_N(u)=span{exp(-uy)L_j(2uy):0<=j<N}

are nonnegative for W, then W>=0 on all of H_eta by density and continuity. For an arbitrary smooth compactly supported test on R, translate it to support inside(0,infinito). The translate belongs to H_eta and W is translation invariant, even in its polar because the two moments are multiplied by reciprocal factors. One obtains the sign for all smooth compact tests. Density of the form core in each window extends the sign to the corresponding domain; on the primitive subspaces the polar vanishes and the required sign of a_T remains.

No margin uniform in N is needed: semidefiniteness of each block and continuity of the limit suffice. Nor is it necessary to prove all sets of rates or to transport monotonicity when varying poles. For u63/2, this is a sufficient target of ONE single sequence of complete Toeplitz matrices.

## 5. Relation with the exterior data and limits

In the Z image, the derivatives with respect to the exponent at a=u+1/2 of X^-a have the form

    partial_a^k[ zeta(a)exp(-(a-1/2)y)]
      =exp(-uy)sum_(j=0)^k binom(k,j)zeta^(k-j)(a)(-y)^j.

The diagonal of this triangular transformation is(-1)^k zeta(a), nonzero for a>1. Hence every confluence of powers generates exactly V_N(u) in its image. The bridge can be formulated in either of the two coordinates without assuming an entrywise positive transformation: the form is preserved by invertible identification.

The union of blocks with all their cross terms is dense; a single chain of vectors f_n, or a union of spaces of uniformly bounded dimension, does not inherit that sufficiency. The current certificates up toN12 and their rate extensions do not prove the rest of the blocks. The known negative AP block forces keeping arithmetic when attempting this direction at all orders.


## 6. Moving rates: exact threshold for strong approximation (2026-11-06)

**PROVED as an approximation criterion; no new positivity.** Independent audits PASS. Consulted the project rules, the three indices, this bridge, THREE002§§7–8 and094/096. The difference is to allow rates u_N tending to infinity, without highpass filter, and to prove the threshold in the norm H_eta that controls W. It is not the r²/N criterion of094 nor the density of a linear envelope. No bibliographic novelty is claimed.

Fix eta>1/2 and u_N>eta with u_N->infinito. Set

    V_N(u_N)={exp(-u_N y)P(y):deg P<N},
    L²_eta={f:exp(eta y)f belongs to L²(0,infinito)},
    ||f||_Heta=||exp(eta y)f||_H1.

Then:

1. dist_Heta(f,V_N(u_N))->0 for EVERY f in H_eta, along all N, if and only if N/u_N->infinito.
2. The UNION of these blocks is dense in H_eta if and only if limsup_(N->infinito) N/u_N=infinito.

The closure of its linear envelope is not characterized here.

**Exact distance in L²_eta.** It is the unfiltered case r=0 of the projection representation of096§2, applied to the shifted rates; no novelty is attributed to that formula. For v>eta, normalize e_v(y)=sqrt(2(v-eta))exp(-vy). The Laguerre basis at rate a_N=u_N-eta, after multiplying by exp(eta y), has coefficients against e_v proportional to ((u_N-v)/(u_N+v-2eta))^j. Summing the geometric tail gives EXACTLY

    dist_L²eta(e_v,V_N(u_N))²
            =abs((u_N-v)/(u_N+v-2eta))^(2N).            (MOV-DIST)

Indeed the degree-j coefficient is 2sqrt(a_N(v-eta))/(a_N+v-eta) times ((v-eta-a_N)/(v-eta+a_N))^j; the square of the prefactor is one minus the square of the ratio. For u_N->infinito, the logarithm of(MOV-DIST) is

    -4(v-eta)(N/u_N)(1+o(1)).

The exponentials with v>eta are total in L²_eta by Laplace uniqueness. Orthogonal projections have norm1, so N/u_N->infinito implies approximation of all of L²_eta along N.

**Strong step without loss of degrees.** The anticausal operator

    (Jh)(y)=integral_y^infinito h(t)dt

satisfies ||Jh||_L²eta<=eta^(-1)||h||_L²eta: after weighting, it is an integral of translations against exp(-eta t), of L1 norm equal to1/eta. If f belongs to H_eta, then f' belongs to L²_eta, f' is integrable and f tends to0 at infinity, so f=-Jf'. Approximate f' by h_N in V_N(u_N) and define g_N=-Jh_N. Integrating a polynomial times an exponential does NOT increase its degree; hence g_N belongs to the SAME V_N(u_N) and g_N'=h_N. Thus

    ||f-g_N||_Heta
       <=sqrt(eta^(-2)+4) ||f'-h_N||_L²eta ->0.          (MOV-STRONG)

No additional condition N/u_N much larger than log N is needed: that loss appears if one differentiates an L² projection instead of first approximating the derivative.

**Necessity and union.** Strong approximation implies L²_eta approximation. (MOV-DIST), with a fixed v>eta, forces N/u_N->infinito. For the union, if limsup N/u_N=infinito sufficiency is applied to a subsequence. If the limsup is finite, choose eta<v<min_N u_N; that minimum exists and is greater than eta because u_N->infinito. Each distance of(MOV-DIST) is positive, and its tail is uniformly separated from0. Hence the union does not approximate even that exponential in L²_eta, nor in H_eta.

**Sign consequence, still conditional.** If W>=0 were proved on each COMPLETE block V_N(u_N) of a subsequence with N/u_N->infinito, continuity of W on H_eta and translation, as in§4, would give the global target. All internal crossings of each block are required, but not crossings between distinct blocks: each approximant belongs to a single positive block. That hypothesis has not been proved here. More generally W[f]>=-epsilon_N||f||² for ALL f in the block, with epsilon_N->0 along the dense subsequence, suffices: the approximants converge in H_eta, their L² norms remain bounded and the error disappears. Sufficiency of a vanishing lower bound has an antecedent in036; it is not a new positive inequality.

The positive theorem THREE002§7 requires u_N>=2^(40N), a regime that does not satisfy the criterion. Moreover, its fixed margin W>=9||f||² cannot be kept when passing to a dense regime: that would carry the same margin to all physical compacts, contradicting the smooth cutoffs of Phi, whose energy tends to0 by the physical identity H_full Phi=0 ofGRAM19.12, while their L² norm tends to a positive value. This observation only prevents preserving fixed coercivity; it does not prevent semidefiniteness nor margins tending to0. No new windowT, computations or paper changes.


**Scope control: N/u_N² does not suppress the complete comb (2026-11-06).** Independent verification of the application of008. Take u_N=N^(3/4) for N sufficiently large and eta=1. The exactly primitive test h of PRIME_PATTERN_FALSIFIER008 belongs to H_eta and satisfies Arch[h]<-3.83||h||², c_h(log2)>||h||²/2. By this bridge, there exist approximants in V_N(u_N) converging to h in H_eta. They can be made exactly primitive: also approximate two fixed correctors e^(-2y),e^(-3y) in those same blocks. Their Tate moment matrix converges to an invertible matrix; solving the2x2 system eliminates the small moment errors with coefficients tending to0. The corrected combinations f_N remain in V_N(u_N) and converge to h in H_eta.

By continuity of Arch, of the moments and of the autocorrelation, eventually

    (Arch[f_N]+Polar[f_N])/||f_N||² < -3,
    c_(f_N)(log2)/||f_N||² > 1/3,
    Polar[f_N]=0 exactly,

while N/u_N²=N^(-1/2)->0. Thus uniform suppression of contact2 as an O(N/u_N²) error over ALL numerators fails, and the main part Arch+Polar that eliminates the arithmetic cannot be declared positive. It is transport of falsifier008 to the dense regime, not a new principle on arithmetic necessity. It does not refute an expansion whose main part keeps the contacts and whose positivity is proved independently; it does not claim W[f_N]<0. No new T nor computations.


## 7. Growing arithmetic cutoff with explicit uniform error (2026-11-06)

**PROVED as tail control; sign of the retained block OPEN.** Independent audits PASS. Consulted the project rules, the three indices, THREE002§7,008 and106_32. It is a quantitative application of the already proved tail bound, not a new concentration estimate nor positivity. Compared with the attempt to suppress low contacts, a cutoff growing with N/u is kept.

For N>=1, u>=2, let V_N(u)=exp(-uy) times polynomials of degree<N and define

    Q_cut=ceil(exp(40N/u)),
    W_(<=Q_cut)[f]=Arch[f]+Polar[f]
          -2sum_(2<=q<=Q_cut) Lambda(q)/sqrt(q) Re c_f(log q).

The normalization of W and all crossings of each block are kept exactly. Then

    |W[f]-W_(<=Q_cut)[f]| < exp(-N)||f||²,
    for EVERY f in V_N(u).                              (MOV-TAIL)

**Proof.** The estimate of THREE002§7

    ||f 1_(y>=t)|| <=sqrt6 13^N exp(-ut/2)||f||

uses only the orthonormal basis and the rates in[u,3u], not the later positivity threshold u>=2^(40N). Its confluent limit keeps the bound for V_N(u). Cauchy–Schwarz for the correlation, followed by Lambda(q)<=log q, gives

    |W-W_(<=Q_cut)|/||f||²
       <=2sqrt6 13^N sum_(q>Q_cut)log(q)q^(-(u+1)/2).

The function log(x)x^(-(u+1)/2) decreases for x>=Q_cut>=2, since (3/2)log2>1. Comparing each term with its preceding interval and integrating exactly gives

    sum_(q>Q_cut)log(q)q^(-(u+1)/2)
       <=Q_cut^(-(u-1)/2)
                  [2log(Q_cut)/(u-1)+4/(u-1)²].

Since u>=2,

    Q_cut^(-(u-1)/2)<=exp(-10N),
    log Q_cut<=40N/u+1,
    2log(Q_cut)/(u-1)+4/(u-1)²<=40N+6<=46N.

Using 2sqrt6<5 and13<exp3, the tail is less than230N exp(-7N). Finally N<=exp(N-1) and exp6>400>230 prove230N exp(-7N)<exp(-N), as required.

**Finite obligation that remains.** For u_N=N^(3/4), from N sufficiently large on u_N>=2 and Q_cut,N=ceil(exp(40N^(1/4))). If one proved for ALL vectors of each retained block

    W_(<=Q_cut,N)[f]>=-epsilon_N||f||²,
    epsilon_N->0,

then(MOV-TAIL) and§6 would give the global target. Neither that lower bound nor PSD of the retained block has been proved. The sign of its diagonals, of some vectors or of a fixed number of degrees does not suffice. This growing cutoff does not contradict the indispensability of atoms for a FIXED cutoff of106_32. The result only removes the infinite tail from this quantitative obligation; it does not decide the arithmetic compensation within the cutoff. No computations, new windowT or paper changes.


## 8. Necessary size of the cutoff at a dense scale (2026-11-06)

**PROVED for the truncated main part; complete sign OPEN.** Independent audit and re-check; independent deduplication. Consulted the three indices,007§2 and106_32. The explicit difference is quantitative: the cutoff grows with the dimension, and a necessary threshold is obtained at the scale u_N=N^(3/4). The bands of007 are antecedents, not a new identity.106_32 treats elimination of atoms in the transformed energy of differences; that truncation is not identified with W_(<=Q) here.

For N>=2,u>=1,Q integer>=1, define the orthonormal basis

    phi_j(y)=sqrt(2u)exp(-uy)L_j(2uy), y>=0,
    d=N-1, f=(phi_0-(-1)^d phi_d)/sqrt2.

Then ||f||=1 and, with the full definition of W_(<=Q) from§7,

    W_(<=Q)[f] <= 2log u+32+4sqrt(Q)log Q+6/u
                         -(2/u)exp((N-1)/u).             (MOV-NEC)

**Proof of the polar.** The integrals of phi_j against exp(±y/2) are sqrt(2u)(-1)^j r^(±j)/(u∓1/2), where r=(u+1/2)/(u-1/2). Their symmetrized product gives the bands of007 generalized to u: p_d=C_u(-1)^d(r^d+r^(-d)), C_u=2u/(u²-1/4). Hence the polar of the chosen vector is EXACTLY C_u(2-r^d-r^(-d)). Since 2/u<=C_u<=3/u and log r>=1/u, it is <=6/u-(2/u)exp(d/u).

**Archimedean and arithmetic proof.** The multiplier m(tau)=Re psi(1/4+i tau/2)-log pi has minimum m(0)>-8. Its mean against the Fourier density of phi_0 is a_0=psi((u+1/2)/2)-log pi<=log u. The last inequality uses psi(x)<log x; this follows from Jensen applied to log for a Gamma(x,1) variable. The bound m(0)>-8 follows from psi(1/4)=-gamma-pi/2-3log2 and the bounds gamma<1,pi/2<2,3log2<3,log pi<2. In the Cayley coordinate, the archimedean bands are Fourier coefficients of that multiplier; each has modulus <=integral |m|<=a_0+16. Thus the contribution of the two coordinates is <=2log u+32. Finally |c_f(t)|<=||f||²=1, Lambda(q)<=log q and sum_(q=2)^Q q^(-1/2)<=2sqrt Q give the majorant 4sqrt Q log Q for all retained contacts. Summing yields(MOV-NEC).

**Moving consequence.** Fix 0<delta<2, u_N=N^(3/4). If log Q_N<=(2-delta)N/u_N, the ratio of the arithmetic majorant to (2/u_N)exp((N-1)/u_N) is <=2(2-delta)N exp(-delta N^(1/4)/2+1/u_N), which tends to0. The logarithmic terms and 6/u_N are also negligible. Eventually

    W_(<=Q_N)[f_N] <= -exp((N-1)/u_N)/u_N -> -infinito.

In particular, no fixed polynomial cutoff Q_N<=N^k permits a lower bound -epsilon_N||f||², epsilon_N->0, on ALL of V_N(u_N). If such a bound existed along all N, necessarily liminf u_N log Q_N/N>=2: any subsequence with ratio <=2-delta contradicts the preceding bound. It is not claimed that the threshold2 is sufficient or optimal. The sufficient cutoff for the ERROR of§7 has constant40, so both bounds fix the same exponential order for this concrete scale.

**Scope.** The vectors are not claimed primitive. Complete W has not been proved negative: the omitted tail may compensate the polar. The threshold does not extend without proof to all dense scales, especially if N/u_N grows slowly. The main part with cutoff40 is not signed, no new windowT and no paper changes.


## 9. Insufficient cutoff even with both moments zero (2026-11-06)

**PROVED: primitive falsifier of the truncated main part, not of complete W.** Construction with mutual check of constants; independent mathematical review PASS. Prior consultation of the three indices,008 and§§6–8; targeted search for Dirichlet/Jackson filters with Laguerre and Tate moments, with this statement not located. The new difference is an explicit test in the SAME moving block with growing cutoff. The gamma vector of008 does not give this scale: its width is sqrt(N)/u, while the following filter reaches N/u. No novelty is attributed to the Dirichlet kernel nor to the inequalities of008.

Let u=N^(3/4), N>=2^60, and Q>=1 an integer with

    log Q <= 2^(-12)N/u.

There exists f in V_N(u), real, ||f||=1, with both Tate moments exactly zero and f(0)=0, such that

    W_(<=Q)[f]<-3.                                      (PRIM-CUT)

**Exact construction.** Set M=floor(N/4), r=(u+1/2)/(u-1/2) and define the coefficients c_j of the polynomial

    C(z)=(1-z)(z+r)(z+r^(-1)) [sum_(j=0)^(M-1)(-z)^j]^4.

Its degree is4M-1<N. Take f proportional to sum_j c_j phi_j, normalized in L². The Laplace formulas of§8 evaluate the moments at z=-r and z=-1/r; hence both vanish EXACTLY. Moreover phi_j(0)=sqrt(2u), so C(1)=0 implies f(0)=0.

**Second spectral moment.** In the Cayley coordinate z=-exp(2ix), -pi/2<x<pi/2, one has |tau|=u|tan x|. The spectral measure of phi_0 transforms into uniform measure, which cancels in the normalized ratio. Write a=1/(u²-1/4), S=sin(Mx)/sin x. Then |(z+r)(z+1/r)|=a+4sin²x and |1-z|²=4cos²x, so

    E_f tau² = u² integral sin²x(a+4sin²x)²|S|^8 dx
                      / integral cos²x(a+4sin²x)²|S|^8 dx.

All the following integrals have limits [-pi/2,pi/2]. For |x|<=1/(2M), M>=2, cos²x>=1/2 and |S|>=M/2. The denominator is >=a²M^7/512. Use |S|<=min(M,1/|sin x|), |sin x|<=|x| and |sin x|>=|x|/2. Splitting into |x|<=1/M and its complement gives

    I_2=integral sin²x |S|^8 dx
         <=(2/3+128/5)M^5 <27M^5,
    I_6=integral sin^6x |S|^8 dx
         <=(2/7+8)M <9M.

Since (a+4sin²x)²<=2a²+32sin^4x, the numerator is <=u²(2a²I_2+32I_6). Hence, for1<=u<=M,

    E_f tau² <=512u²[54/M²+288/(a²M^6)]
              <=175104(u/M)² <2^18(u/M)².                (PRIM-MOM)

One used a>=1/u² and u/M<=1. The factor1-z ensures integrability of the second moment also at the endpoints x=±pi/2.

**Sign of each retained piece.** By008, Arch[f]<-4+17 E_f tau² and c_f(t)>=1-(t²/2)E_f tau². For N>=2^60, M>=N/8 and u<=M, so E_f tau²<=2^24/sqrt(N)<=1/64. Hence Arch[f]<-3. If log q<=2^(-12)N/u, then log q<=M/(512u), and(PRIM-MOM) implies c_f(log q)>=1/2. All retained contacts are nonpositive and the polar is zero, which proves(PRIM-CUT).

**Scope.** The cutoff can grow exponentially in N/u with the small constant2^(-12); every fixed polynomial cutoff is eventually included. The threshold2 of§8 is not transferred to primitives, nor is the constant here proved optimal. The omitted tail could compensate the deficit: complete W and the main part with cutoff40 of§7 remain OPEN. Mere elimination of the polar does not allow replacing that cutoff by a polynomial one. No computations, new windowT or paper changes.
