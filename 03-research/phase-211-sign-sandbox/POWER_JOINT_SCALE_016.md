# POWER_JOINT_SCALE_016 — Joint scale of dimension and highpass order

Status: PROVED beta formulas, linear packet limit, time moments and obstructions to uniformizing the weights. OPEN a positivity cone for the complete form. No numerical campaigns. Papers untouched.

## Antecedents and new reason, recorded before building

Read: the project rules, HIGHPASS015 and its audit, GEOMETRIC_TRANSFER015, CONFLUENT_BRIDGE014; joint search in the ROUTES-TRIED-INDEX index, grid part3 and CROSSWORD-TO-D (Jacobi/resolvent/joint scale/highpass). High-frequency coercivity and the limits of prolate blocks are already recorded. The difference here is to quantify the N-dependence of the exact rational orbit Q^kV_N, especially for P=1 and P=s^(N−1), not to infer a prolate tail or general positivity from a high index.

Investigated separately: (i) real spectral scale, (ii) uniformity of the time weights used to sum the comb, (iii) complete sign. A falsifier of (ii) will not be presented as a falsifier of (iii).

## 1. Endpoint P=1: EXACT beta law for all N,k

Let u=63/2 and f_(N,k) with transform F(s)=s^k/(s+u)^(N+k), N>=1,k>=0. Its normalized spectral density is proportional to tau^(2k)/(u²+tau²)^(N+k). Changing to

    Z=tau²/(u²+tau²),

one obtains EXACTLY

    Z~Beta(k+1/2,N−1/2),
    ||f_(N,k)||²=u^(1−2N)B(k+1/2,N−1/2)/(2pi).          (BETA)

The sign of tau is symmetric and independent of Z. For N>3/2,

    E tau²=u²(k+1/2)/(N−3/2).

Thus the typical scale is u sqrt(k/N), not sqrt(k) with a constant independent of N. The hidden constant in the theorem of015 really matters as the dimension varies.

## 2. Packet in the LINEAR cone: the contacts do not disappear

Suppose N->infinity and k/N->c, 0<c<infinity. The beta mean and variance are

    E Z=(k+1/2)/(k+N),
    Var Z=(k+1/2)(N−1/2)/[(k+N)²(k+N+1)].

By Chebyshev, Z converges in probability to c/(1+c). Consequently |tau| converges in probability to u sqrt(c). For every fixed real t,

    c_f(N,k)(t)/||f_(N,k)||² ->cos(u sqrt(c)t).           (PACKET)

No central limit theorem is used: the function cos is bounded and beta concentration suffices. The normalized archimedean energy converges to m(u sqrt(c)); the required integrable uniformity follows from the uniform bound on E tau², since m has logarithmic growth.

This result falsifies the extrapolation "uniform disappearance of each contact in every cone k>=C N". For any C, choose a sufficiently large integer m and c=[2pi m/(u log2)]²>=C; take k=ceil(cN). Then

    c_f(N,k)(log2)/||f_(N,k)||² ->1.

Contact 2 remains and does not tend to zero. It is not claimed that the complete form is negative along this sequence: its infinite sum cannot be interchanged with PACKET using the bounds of015, precisely because their uniformity fails. The linear cone remains without a sign proof, not refuted as a sign statement.

## 3. Another endpoint: P=s^(N−1) removes the dimensional difficulty

For that numerator,

    Q(s)^k P(s)/(s+u)^N
      =s^(k+N−1)/(s+u)^(k+N)
      =Q(s)^(k+N−1)/(s+u).

It is EXACTLY the orbit of initial dimension one and order k+N−1. By HIGHPASS015 its normalized form grows like

    (1/2)log(k+N−1)+log[u/(2pi)]−(1/2)psi(1/2)+o(1),

and the normalized comb and polar parts disappear as k+N grows. Its beta law is Beta(k+N−1/2,1/2). This behaviour differs from that of P=1, although both numerators belong to the same initial space. An analysis of a single endpoint does not uniformize the whole block.

## 4. The complete beta Gram matrix explains the N-dependence

For a real numerator P(s)=Σa_j s^j, the norm is a Gram form whose entries are computed by beta. Entries with i+j odd vanish by symmetry; if i+j=2r,

    (1/2pi)∫tau^(2k)(i tau)^j conjugate[(i tau)^i]
                         /(u²+tau²)^(N+k)d tau
      =(−1)^(r+i) u^(1−2N+2r)
           B(k+r+1/2,N−r−1/2)/(2pi).                   (GRAM)

Here 0<=i,j<N, so the second beta parameter is positive. GRAM is a formula for the WHOLE block, not only its diagonals. The smaller parameter can be1/2 or can grow like N: this contains simultaneously the two previous extreme regimes and does not by itself provide conditioning uniform in N.

The change Z of§1 also separates the two real sectors. Writing P(i tau)=E(tau²)+i tau O(tau²), the cross term is eliminated. If d is the maximal degree allowed by N in the sector (padding with zero coefficients when necessary), setting R(Z)=(1−Z)^d E(u²Z/(1−Z)) (analogously for O) turns the sector into a Gram of polynomials of degree<=d for a Jacobi weight Z^alpha(1−Z)^beta. The parameters are alpha=k−1/2,beta=±1/2 in the even sector, and alpha=k+1/2,beta=±1/2 in the odd one. It is an exact coordinatization for studying the joint scale; no sign of W is attributed to the positivity of this Gram of norms.

## 5. EXACT time mean independent of k

For P=1, the time probability is |f_(N,k)(y)|²dy/||f_(N,k)||², y>=0. Its mean is

    mu_(N,k)=E y=(N−1/2)/u.                              (MEAN)

Proof by Parseval. For tau!=0, the derivative of the phase of F(i tau) is −(N+k)u/(u²+tau²); the phase k arg(i tau) is constant on each half-line. If k>=1, the possible jump at tau=0 is multiplied by F(0)=0; k=0 has no such term. Hence

    E y=(N+k)u E[1/(u²+tau²)]
       =(N+k)/u E(1−Z)=(N−1/2)/u.

The rational functions decay exponentially times polynomial, so Parseval for the derivative and the time moments is legitimate even if the extension jumps at y=0: one differentiates in FREQUENCY to multiply by y, not in time across that edge.

For any eta>0 with eta<u, Jensen then proves

    ||e^(eta y)f_(N,k)||²/||f_(N,k)||²
       >=exp[2eta(N−1/2)/u], for ALL k.                (WEIGHT)

Thus a weighted constant uniform in N is impossible even on k>=C N², k>=exp(N), or any cone allowing N to grow: WEIGHT is independent of k. EVENTUAL015, whose constant does depend on N, is not refuted.

## 6. Centering removes the mean, but not the time dispersion

For k>=1, another Parseval computation gives

    E y²=(N−1/2)/u² [N−k+k²/(k−1/2)],
    Var y=(N−1/2)/u² [1+1/(4(k−1/2))].                 (VAR)

Indeed, |F'|²/|F|²=k²/tau²+(N²−k²)/(u²+tau²). Under BETA,

    E tau^-2=(N−1/2)/[u²(k−1/2)],
    E(u²+tau²)^-1=(N−1/2)/[u²(N+k)],

which produces the two equalities. For k=0 one obtains directly the gamma time distribution and Var y=(N−1/2)/(2u²), consistent with the algebraic extension of VAR.

Let X=y−mu. Since cosh z>=1+z²/2,

    E e^(2eta X)+E e^(-2eta X)>=2+4eta²Var y.

Each expectation is >=1 by Jensen. At least one grows linearly in N for k>=1. Even the product of both grows at least like1+2eta²Var y. Consequently there is no simultaneous uniform bound for the TWO centered exponential weights of fixed amplitude eta, nor for the product of norms used in the corresponding two-sided bound of correlations.

This does not rule out centered weights with N-dependent eta nor an analysis using cancellation instead of absolute values. It distinguishes a shift from a dispersion: centering removes only the former.

## 7. Consequence for the complementary defect and status of the cone

The geometric mixtures of015 preserve complete energies with positive weights and incorporate the norms of Q^k f. EVENTUAL015 controls the tail when N is fixed. PACKET refutes uniform disappearance of the contacts in the linear cone; WEIGHT refutes a weighted exponential bound uniform in N in any cone. The spectral behaviour of the quadratic cone remains open here.

The complementary segment remaining before the effective threshold K_N keeps a sign obligation. Neither the mixture identity nor GRAM nor eventual positivity at fixed N controls it. The appropriate route must quantify that segment or supply an arithmetic inequality for the packet regimes, preserving the complete signed sum.

**OPEN:** existence of C such that W>=0 for all numerators and k>=C N, or k>=C N². No counterexample to those two sign statements was produced. **FALSIFIED:** its justification via uniform disappearance of each contact in the linear cone, or via an exponential weighted constant uniform in N in any cone of k. Concentration/dispersion in the quadratic cone requires additional analysis; here it is presented neither as a theorem nor as a negative of W.
