# POWER_FOUR_TURAN_084 — A sufficient local criterion for the Pfaffians of order four

**Update085:** the remaining compact set was certified and audited in `POWER_FOUR_GENERATORS_085.md`, `POWER_FOUR_GENERATORS_AUDIT_085.md` and `POWER_STATE_085.md`: ALL four exponents ai>1 have complete W positive. The mentions of a pending compact set below keep the historical status of084; higher orders remain open.

Status: **PROVED as criterion, inheritance falsifier and exterior application, independent audit approved.** See `POWER_FOUR_TURAN_AUDIT_084.md`. For the real Phi the new conditions are proved here only on an explicit exterior region. The remaining compact set and four global generators are not declared. Papers untouched; no numerical matrices or campaigns.

## 1. Antecedents and difference

Consulted the project rules, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; cross-checked SCHUR003,074,079–083.083 factorizes determinants into products of Pfaffians, without controlling their signs.080 and082 control exactly three nodes via concavity of the two reciprocal data. That concavity is not extrapolated to four.

The algebra of Pfaffians, generalized determinants, Rolle and quotients of Wronskians are classical tools, they are not claimed as new. Here the specialization to four nodes and an additional quantitative inequality that does imply the sign on ALL such nodes are proved directly. It is also shown, keeping the exact reciprocity RS=x, that the previous scalar properties do not suffice by themselves. It is not a refutation of the real theta datum nor of the whole potential hypothesis073.

## 2. Four-node identity

Let0<u1<u2<u3<u4, xi=ui², and f a real function. Put

    A_f,ij=[f(xj)−f(xi)]/(ui+uj),
    P=product_(i<j)(ui+uj)>0,
    D_f=det[1,xi,f(xi),xi f(xi)]_(i=1,...,4).

Then exactly

    Pf(A_f)=−D_f/P.                                  (PF-DET)

It can be verified without an inverse: expand Pf=A12A34−A13A24+A14A23, multiply by P and expand the determinant along the two columns containing f. The coefficients of each product f(xi)f(xj) coincide with the indicated negative sign. It is a polynomial identity in the ui and the four values of f; the auxiliary symbolic check gave identically zero, not a sampling.

In particular, for R(x)=sqrt(x)/M(sqrt(x)) and S(x)=sqrt(x)M(sqrt(x)),083 gives

    det K=Pf(A_R)Pf(A_S)/product_i R(xi),
    K_ij=[M(ui)+M(uj)]/(ui+uj).

Thus a positive sign of each Pfaffian would suffice; the identity alone does not supply it.

## 3. Global quantitative criterion by Rolle

Suppose f∈C³ on an interval of squares, f'>0,f''<0, and

    T_f=2f'f'''−3(f'')²>0 on the WHOLE interval.        (TURAN)

We prove Pf(A_f)>0 for ALL four distinct nodes of the interval.

Define

    H(x)=(x f(x))''/f''(x)=x+2f'(x)/f''(x).

Since f'' does not vanish,

    H'(x)=−T_f/(f'')²<0.

If D_f vanished for four distinct points, there would exist a non-zero combination

    h(x)=a+bx+cf(x)+dx f(x)

with four distinct zeros. Rolle applied twice would require at least two distinct zeros of

    h''(x)=f''(x)[c+dH(x)].

Strict monotonicity of H allows at most one, unless c=d=0. In that edge case h is affine and four zeros force a=b=0, contradiction. Hence D_f never vanishes on the connected domain of ordered quadruples and its sign is constant.

The Wronskian of the four columns is exactly

    W(1,x,f,xf)=3(f'')²−2f'f'''=−T_f<0.

On letting the nodes merge at any interior point,

    D_f/product_(i<j)(xj−xi) -> −T_f/(0!1!2!3!)<0.

This fixes D_f<0 for every ordered quadruple. PF-DET proves the positive sign of the Pfaffian. The argument is not limited to a confluent jet: Rolle transports that sign to ALL sets of nodes.

Consequently, for real M, if TURAN were proved for both R and S on an interval, all blocks of four distinct nodes would be positive definite: the minors of sizes1,2,3 are already positive by073/080 and that of size4 is by083. Coincident nodes are grouped as usual. TURAN of both factors is a SUFFICIENT condition; it is not claimed here that each is necessary for the Pfaffian product or for W.

## 4. Falsifier of inheritance from the previous concavities

Fix epsilon=1/16 and, on0<=x<=1,

    R(x)=1+x−epsilon x²,
    S(x)=x/R(x),
    M(u)=u/R(u²), 0<=u<=1.

R>0,R'>0,R''=−1/8<0. Moreover

    S'=(1+epsilon x²)/R²>0,
    S''R³=−2+6epsilon x+2epsilon²x³
          =(x−4)(x²+4x+64)/128<0.

RS=x is kept EXACTLY. For x=u²,

    M'=[1−x+3x²/16]/R²>0,
    M''R³/(2u)=[3x³−24x²+208x−384]/128<0

for0<u<=1: it suffices to bound the last numerator by3+208−384<0. Also M(0)=0,M'(0)=1, M/u=1/R decreases, and

    g(x)=u/M(u)−1=x−x²/16,
    b(x)=g(x)/x=1−x/16>0

are, respectively, strictly increasing/concave and strictly decreasing. The example therefore satisfies the scalar properties used in073/077/080, and079 gives all its triples positive definite at distinct nodes of the interval. It is not claimed that this M is the tilt of a Phi with the complete hypothesis of073.

However, for ANY four distinct nodes in(1/2,1), put V=product_(i<j)(uj−ui)>0. The rank decomposition gives exactly

    Pf(A_R)=−epsilon² V,
    Pf(A_S)=epsilon V/product_i R(xi).

For the first identity, A_R is the sum of the simple forms 1∧u and −epsilon(1∧u³+u²∧u). In the basis(1,u,u²,u³), its Pfaffian of coefficients is−epsilon²; the congruence contributes V. For the second, multiplying rows and columns of A_S by Ri gives the matrix with entries(uj−ui)(1+epsilon ui²uj²), that is1∧u+epsilon u²∧u³. Its Pfaffian is epsilon V. Thus

    det K=−epsilon³ V²/[product_i R(xi)]²<0.         (FAIL-HEREDITY)

It is a symbolic falsifier of ALL the indicated quadruples, not a selected numerical matrix. It refutes only inferring four from those local scalar properties; it does not refute the real datum Phi,073,080 nor a specific additional condition.

## 5. Explicit conditions for the real datum

The following derivatives are with respect to x=u². Put c=M(u),d=M'(u),e=M''(u),f=M'''(u). Direct differentiation gives

    T_R=N_R/(16c⁴u⁶),
    T_S=N_S/(16u⁶),

with

    N_R=3c²−6ucd−6u²ce−2u³cf
           +3u²d²+6u³de+2u⁴df−3u⁴e²,
    N_S=3c²+6ucd+6u²ce+2u³cf
           −9u²d²−6u³de+2u⁴df−3u⁴e².                 (REAL-TURAN)

The denominators are positive.073/080 already prove R',S'>0 and R'',S''<0 for u>1/2. Hence N_R>0 and N_S>0 are TWO specific quantitative obligations sufficient for the next step; they are not obtained only from the sign of the second-order derivatives.

At confluence of four nodes, the identity also gives

    Pf(A_f)/product_(i<j)(uj−ui) -> T_f/12.

This checks the factors and signs of REAL-TURAN, but the global sufficiency comes from§3, not from that local check.

## 6. Analytic exterior verification with all the arithmetic

N_R,N_S>0 is proved for ALL A=u+1/2>=128. It is an exterior region chosen analytically for loose margins, without sweep or optimization of a threshold. Write

    P_j(A)=Σ_(n>=2)Lambda(n)(log n)^j n^(−A),
    D=ud,E=u²e,F=u³f.

The complete arithmetic formula and the polygamma series give

    c=1/A+1/(A−1)−logpi/2+psi(A/2)/2−P0,
    d=−1/A²−1/(A−1)²+psi1(A/2)/4+P1,
    e=2/A³+2/(A−1)³+psi2(A/2)/8−P2,
    f=−6/A⁴−6/(A−1)⁴+psi3(A/2)/16+P3.

The integral comparisons of the positive series prove

    1/t<=psi1(t)<=1/t+1/t²,
    −1/t²−2/t³<=psi2(t)<=−1/t²,
    2/t³<=psi3(t)<=2/t³+6/t⁴.

With Lambda(n)(log n)^j<=(log n)^(j+1)<=n^(j+1),

    P_j(A)<=2^(j+1−A)[1+2/(A−j−2)], j=0,1,2,3.

The relevant majorants decrease from A=32 on by logarithmic derivative<=3/A−log2<0. The rational comparisons at32 give

    AP1<1/100, A³P2<1/4, A³P3<1/100,
    (A−1)P0<1,                                      (PRIME-BOUNDS)

valid for all A>=32. For example A³P3 at32 is29/(27·8192)<1/100; the others are the bounds already documented078. The prime sum is not cut without a tail.

For A>=128 one obtains, WITHOUT substituting an asymptotic,

    9/20<D<51/100,
    −51/100<E<−2/5,
    4/5<F<101/100.                                  (BOX)

Details of the less immediate lower/upper sides: with(A/(A−1))^k<2 for k<=4,

    D>=1/2−13/(4A)>9/20,
    E>=−1/2−A²P2>−51/100,
    E<=−1/2+13/(2A)<−2/5,
    F>=1−39/(2A)>4/5,
    F<=1+A³P3<101/100.

The upper bound on D is that of078. For the lower bound on F, (u/A)³>1−3/(2A) and the two negative rational contributions, bounded by6/A and12/A, were used; for the upper bound the term6/A⁴ of psi3 cancels with the rational−6/A⁴.

Moreover c>3/2. Indeed psi(t)>=logt−1/t and PRIME-BOUNDS give

    c>(1/2)log[A/(2pi)].

For A>=128, pi<22/7 gives A/(2pi)>224/11. The comparison e<87/32 (series up to degree3 plus tail5/96) implies e³<(87/32)³<224/11. Thus the logarithm exceeds3.

Finally REAL-TURAN is written

    N_R=3c²+c(−6D−6E−2F)+3D²+6DE+2DF−3E²,
    N_S=3c²+c(6D+6E+2F)−9D²−6DE+2DF−3E².

The box BOX implies, by direct rational comparisons,

    −6D−6E−2F>−3,
    3D²+6DE+2DF−3E²>−2,
    6D+6E+2F>0,
    −9D²−6DE+2DF−3E²>−2.

Hence, for ALL A>=128,

    N_R>3c²−3c−2>1/4,
    N_S>3c²−2>19/4.                                (OUTER-TURAN)

This proves TURAN of both real data on the exterior region with explicit arithmetic remainders. It is not a claim of sufficiency of their limiting behaviour.

## 7. Pending obligation and scope

To apply this criterion to four generators on ALL A_i>1 one would still need to prove N_R,N_S>0 on1/2<u<127+1/2, or find another comparison that directly pays the product of Pfaffians without requiring individual signs. No compact certificate was executed nor were parameters chosen from floating values.

The exterior result does NOT extend coverage of four:053 already proved thirteen arbitrary poles at rates>=63/2. The new contribution is the GLOBAL quantitative criterion for Pfaffian4, the exact falsifier of inheritance from concavity and a first analytic verification, with all the arithmetic, of the local obligations. Four global generators, all orders or a new time window are not proved.
