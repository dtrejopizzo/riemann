# POWER_RECURRENCE_BOUNDARY_036 — Energy of the cone on an infinite boundary

Status: **PROVED; independent review APPROVED in POWER_FRONTIER_AUDIT_036.md**. At FIXED u63/2, for any initial entry N>=18,k>=0, the FULL energy of the positive cone017 on the diagonal boundary of depth L tends to0 with explicit bound O(logL/sqrtL). The energy of the complement tends EXACTLY to the initial entry, without assuming that the remainder vanishes. A boundary stopped at the first contact with that cone moreover leaves explicit positive normative mass. No new sign of W is proved, nor an obstruction for other boundaries.

## 1. Corpus and new reason

First read ROUTES-TRIED-INDEX/README.md, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; consulted the descent/recurrence/cone entries, DESCENT016 and its audit§7, JOINT_SCALE016, TABLE_DESCENT018 and its falsifier, QUADRATIC_EXPLICIT017, DIVISOR_COMPARISON034 and BOUNDARY_BALANCE035.

The spectral beta law and the binomial expansion are not new: they already appear in016. The identification as an urn is only a way of organizing that same law. The difference HERE is controlling the ENERGY OF THE FULL REAL FORM on the WHOLE growing parabolic subset k'>=10000N'^2 of each diagonal boundary, not only an edge with fixed N', nor only its probability. The infinite comb and the polar are kept using their bounds017. The full remainder has an identified exact limit; it is not erased by a mass consideration.

The result035 was finite and used a positive real column and a terminal datum. Here we study what sending a boundary to infinity actually produces with the available explicit data, without restating as novelty the abstract counterexample018.

## 2. Exact weights, without an implicit martingale limit

Let a_(N,k)=W[f_(N,k)] and n_(N,k)=||f_(N,k)||². Use the full recurrence

    a_(N,k)=a_(N,k+1)+u²a_(N+1,k),
    n_(N,k)=u^(1−2N)B(k+1/2,N−1/2)/(2pi).

Set A_(N,k)=a_(N,k)/n_(N,k), alpha=k+1/2,beta=N−1/2,S=N+k. Then

    A_(N,k)=[alpha/S]A_(N,k+1)+[beta/S]A_(N+1,k).

Iterating L times gives a FINITE identity for the FULL form:

    A_(N,k)=sum_(j=0)^L pi_(L,j) A_(N+j,k+L−j),          (FRONT)
    pi_(L,j)=binom(L,j)(beta)_j(alpha)_(L−j)/(S)_L.

Here j counts increments of N. All the pi are positive and their sum is1, by Vandermonde or by integrating the binomial against Beta(alpha,beta). The unnormalized expansion has weights binom(L,j)u^(2j); the formula above includes EXACTLY the change of norm. No infinite series has been interchanged with W.

## 3. An exact inverse moment controls the WHOLE growing cone

If J has weights pi_(L,j), the elementary beta-binomial mixture gives

    E[1/(N+J−3/2)]
      =(S−1)/[(N−3/2)(S+L−1)], N>=2.                    (INV)

Proof: take Q~Beta(alpha,beta), J|Q~Binomial(L,1−Q). The posterior Q|J is Beta(alpha+L−J,beta+J). By the beta integral,

    E[(1−Q)^(-1)|J]=(S+L−1)/(beta+J−1),
    E[(1−Q)^(-1)]=(S−1)/(beta−1).

Averaging proves INV; beta>1 is equivalent to N>3/2. One can also verify it by multiplying each term of FRONT by1/(beta+j−1) and applying Vandermonde. No asymptotic beta approximation is used.

Let C=10000 and

    E_L={j: k+L−j>=C(N+j)²},
    s_L=sqrt((k+L)/C),
    M_L=min(1, (s_L−3/2)_+ (S−1)/[(N−3/2)(S+L−1)]).

On E_L one has N+j<=s_L, and hence 1/(N+j−3/2)>=1/(s_L−3/2), if the set is nonempty. INV proves

    sum_(j in E_L)pi_(L,j)<=M_L=O_(N,k)(L^(-1/2)).       (MASS)

If s_L<N, E_L is empty. The bound written with positive part remains valid even before there is contact with the cone.

## 4. REAL archimedean upper bound uniform on the boundary

The full symbol is m(tau)=Re psi(1/4+i tau/2)−logpi. The psi recurrence subtracts a reciprocal with positive real part, so

    m(tau)<=Re psi(5/4+i tau/2)−logpi.

Periodic Euler B1 on Re z=5/4 gives

    psi(z)=logz−1/(2z)+R(z), |R(z)|<=2/5.

Since Re(1/z)>0 and logpi>0,

    m(tau)<= (1/2)log(25/16+tau²/4)+2/5.                (SYMBOL)

For the spectral probability of the boundary atom N'=N+j,k'=k+L−j,

    E tau²=u²(k'+1/2)/(N'−3/2)
                <=u²(k+L+1/2)/(N−3/2).

Jensen for log proves on the WHOLE boundary

    ARCH_(N',k')/n_(N',k')<=H_L,
    H_L=(1/2)log[25/16+u²(k+L+1/2)/(4(N−3/2))]+2/5.      (ARCH-UP)

N>=2 is needed, which is amply satisfied in the pending regime N>=18. It is not assumed that the symbol is bounded nor that ARCH converges uniformly across all cells.

## 5. FULL ENERGY of the cone and exact limit of the remainder

In EACH cell of E_L, QUADRATIC_EXPLICIT017 proves for the real form

    A_(N',k')>49/50,
    |PRIME|/n_(N',k')<1/1000,
    |POLAR|/n_(N',k')<1/1000.

Its hypotheses are N'>=2,u63/2 and k'>=10000N'^2: exactly the present ones, with no additional N threshold. The second bound includes ALL contacts and the third the exact polar.

Define the known energy of the cone and the real remainder

    C_L=sum_(j in E_L)pi_(L,j)A_(N+j,k+L−j),
    R_L=sum_(j notin E_L)pi_(L,j)A_(N+j,k+L−j).

From MASS, ARCH-UP and the full bounds017,

    0<=C_L<=M_L(H_L+1/500)
               =O_(N,k)(log(L+2)/sqrt(L+1))->0.          (ENERGY)

FRONT then implies EXACTLY

    R_L=A_(N,k)−C_L,
    |R_L−A_(N,k)|<=M_L(H_L+1/500)->0.                   (REMAINDER)

This is a limit of the ENERGY OF REAL W, not only a probability law. Uniform integrability of all A values on the boundary has not been assumed, nor has an infinite compensation of polar and comb been separated. Only the positive subset is dominated through full bounds valid there; the complement is kept as the exact FINITE difference of FRONT.

The region034 at fixed u covers N'<=17 for k'>=1. From a pending entry N>=18 it is never reached because N' only increases. The data035 are not reachable from above either. Hence, on this diagonal boundary, the WHOLE accessible explicit positive set017 contributes energy that VANISHES, while the complement carries the full original value. No reduction of the interior obligation to the cone is obtained.

As an example of a rigorously NONZERO REAL remainder, CONTACT_DECISION032 proves A_(211,1)>3.4e−15. For that already decided entry, REMAINDER gives R_L->A_(211,1)>3.4e−15, although the positive energy of the cone tends to0. It is not a sign counterexample nor a new computation for another N.

## 6. Stopped boundary: exact weight and surviving mass

The conclusion above concerns DIAGONAL boundaries. In order not to turn it into a prohibition on all schemes, also record stopping at the FIRST contact with the cone. Suppose the initial datum is below: k<CN².

Each path with r increments of k and j increments of N has probability

    (alpha)_r(beta)_j/(S)_(r+j),

independently of the order of its steps. If g_(L,j) counts the paths of length L that did NOT touch the cone and end with j increments of N, the EXACT weight of the stopped remainder is

    sigma_(L,j)=g_(L,j)(alpha)_(L−j)(beta)_j/(S)_L.        (STOP-WEIGHT)

The integers g are obtained from Pascal discarding cells after their first contact. Analogously, each first cell reached has the same weight per path multiplied by its number of admissible paths. Iterating REC only on non-stopped cells gives a finite identity: energy of first arrivals up to L + sum_j sigma_(L,j)A_(N+j,k+L−j)=A_(N,k). It is an exact weight of the remainder, not a claim that this remainder converges to0.

There is mass that NEVER touches the cone. Condition the beta representation on Q<=1/3. The steps are then independent with probability Q of incrementing k. The process 2^(r−j) is a nonnegative supermartingale, since its mean factor is2Q+(1−Q)/2<=1. On touching the cone,

    r−j=(k'−N')−(k−N)>=CN²−k,

because CN'^2−N' increases for N'>=N. The elementary maximal inequality (finite stopping and then monotone limit) gives

    P(hit|Q<=1/3)<=2^(-(CN²−k)).

Hence

    P(never hit)>=P_Beta(alpha,beta)(Q<=1/3)
                         ·[1−2^(-(CN²−k))]>0.          (SURVIVAL)

It is not inferred from this persistent mass that the stopped ENERGY remainder cannot vanish: signed control/integrability of A on those trajectories would be missing. The exact result ENERGY/REMAINDER is stronger for the concrete diagonal boundary; it does not resolve that other stopped boundary.

## 7. Scope and remaining quantitative obligation

The positive recurrence only increments k and N. From k>=1 it never reaches the edge k0; from N>=18 it does not reach the already covered finite rows either. Algebraic inversion towards k0 gives differences with alternating signs, not a positive representation authorized by REC.

The remaining sufficient boundary condition would be a REAL ARITHMETIC estimate proving R_L>=−epsilon_L with epsilon_L->0; ENERGY would turn it into A_(N,k)>=0. The sign data of the cone alone do not provide that estimate: its energy on the diagonal boundary tends to0 and R_L converges precisely to the value whose decision was pending. This condition is not declared a new closure route.

Recorded as a new bounded result: the explicit bound ENERGY for the WHOLE existing parabolic cone and the limit REMAINDER of the full form, plus STOP-WEIGHT/SURVIVAL with separate scope. The beta law016 is not repeated as novelty, no global NO-GO is proved, and the possibility of a new signed estimate of the interior or of another boundary with energy control is not eliminated.
