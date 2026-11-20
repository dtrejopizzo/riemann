# POWER_DESCENT_016 — Complementary defect, binomial localization and precise obstruction to purely structural descent

Status: PROVED (complete identities, eventual monotonicity of differences, mass localization and falsifier of the structural inference). Global arithmetic descent OPEN. Papers untouched.

## 1. Previous state, corpus and new reason

Read POWER_STATE_015, POWER_HIGHPASS_015, POWER_GEOMETRIC_TRANSFER_015 and the index/grid/crossword, searching for complementary filters, binomial mixtures/partitions, descent and constant shifts. The global sign of eight poles and eventual positivity for every fixed order are kept. That tail is not interpreted as positivity of the initial steps.

The new difference with respect to 015 is to compute the exact DEFECT between high-pass steps, including the polar, and to localize quantitatively the mass of its binomial refinement. This allows proving which part of a descent attempt is really controlled and which is not. The filter identities are not presented as an exclusive arithmetic property.

## 2. Complementary identity with the complete polar

Fix u>1, Q(s)=s/(s+u), L(s)=u/(s+u). On the Fourier axis,

    |Q(i tau)|²+|L(i tau)|²=1.

Moreover, setting a=1/2,

    Q(-a)Q(a)+L(-a)L(a)
       =[-a²+u²]/[u²-a²]=1.

Hence the same partition holds EXACTLY for the complete form:

    W[f]=W[Qf]+W[Lf].                                    (DEF)

The archimedean part and each contact are verified by multiplying their spectral integrands; the polar uses the second identity. The contact sums converge absolutely in the rational class considered. The identity also holds for the L2 norm. It has not been assumed that W[Lf] is non-negative.

The filters commute. Iterating (DEF) m times gives

    W[f]=Σ_{j=0}^m binom(m,j)W[Q^j L^{m-j}f],             (BIN)

and the same formula for ||f||². All crossings are included via the filter identity; it is not an argument of positivity of summands.

## 3. Additional positive result: eventually positive finite differences

For f in V_N, let a_k=W[Q^k f] and Δa_k=a_{k+1}-a_k. (DEF) implies, for each integer r>=0,

    (-1)^r Δ^r a_k=W[L^r Q^k f].                          (FD)

Since L^r f=u^r P(s)/(s+u)^{N+r} belongs to V_{N+r}, the eventual positivity theorem of 015 proves that, for fixed N and r, the right-hand side is positive for k sufficiently large, uniformly over all numerators of V_N. In particular a_k is eventually positive and decreasing, and converges to zero by the already proved strong convergence.

This statement is a monotonicity of the UNNORMALIZED QUADRATIC VALUES in the tail, not a global monotonicity of the Rayleigh quotients. Each order r has its own threshold; a common threshold for all r,N, or descent down to k=0, has not been proved.

Telescoping r=1 also gives

    W[f]=Σ_{k>=0}W[LQ^k f],
    ||f||²=Σ_{k>=0}||LQ^k f||².

The series of energies converges absolutely: its tail is positive by 015 and the partial sums converge to W[f] by (DEF) and Q^k f->0 in strong norm. The finite prefix may still contain values whose sign is not proved.

## 4. Exact binomial localization: the known tail occupies a null-mass edge

For f non-zero, define the spectral probability dmu=|F(i tau)|²d tau/(2pi||f||²) and

    p(tau)=tau²/(u²+tau²),
    nu_m(j)=binom(m,j)||Q^j L^{m-j}f||²/||f||².

Then nu_m is a probability on j=0,...,m and has the EXACT representation

    nu_m(j)=∫binom(m,j)p(tau)^j[1-p(tau)]^{m-j}dmu.       (LAW)

Conditioned on tau, j is a binomial variable of m trials and parameter p(tau). Consequently, for every Lipschitz function phi on [0,1],

    |Σ_j nu_m(j)phi(j/m)-∫phi(p(tau))dmu|
       <=Lip(phi)/(2sqrt m).                              (LOC)

Proof: the conditional variance of j/m is p(1-p)/m<=1/(4m), and Cauchy--Schwarz is applied. Thus the law of j/m converges to the image of the REAL SPECTRAL MEASURE of f under p; it does not automatically accumulate at j/m=1.

For each fixed R,

    Σ_{m-j<=R}nu_m(j)->0.                                 (EDGE)

Indeed p(tau)<1 for every finite tau; the binomial probability of having at most R failures tends to zero for each p<1, and dominated convergence is applied. The statement is uniform over the unit sphere of any fixed V_N: the multiplier operator of the event lies between 0 and 1, converges pointwise to zero, and its compression of dimension N has trace tending to zero; its norm is bounded by that trace.

The relation with 015 is precise. The term of (BIN) with m-j=r fixed is Q^{m-r}(L^r f), whose base order is N+r. For fixed R, 015 makes all the edge terms r<=R positive for m sufficiently large. But (EDGE) proves that this edge has TOTAL NORMALIZED WEIGHT tending to zero. In the interior j/m≈theta<1, the base order N+m-j also grows: 015 provides no uniform threshold there.

This does not prove that the interior terms are negative; it proves that knowing only the eventually positive edges does not control by mass the rest of (BIN). The pending information remains in the macroscopic region described by the measure p_#mu, which depends on the numerator.

### The energy contribution of a fixed edge also vanishes

For f=P/(s+u)^N fixed non-zero, put d=degree P and r0=N-d>=1. The norm and complete-quotient asymptotics of POWER_HIGHPASS_015 give, for each fixed r,

    ||Q^{m-r}L^r f||²=O(m^{-(r0+r-1/2)}),
    W[Q^{m-r}L^r f]/||Q^{m-r}L^r f||²=O(logm).

Since binom(m,r)=O(m^r), we get

    Σ_{r=0}^R binom(m,r)W[Q^{m-r}L^r f]
       =O(m^{1/2-r0}logm)->0.

Hence the positive terms that 015 directly controls over a fixed number of upper diagonals not only have zero normalized weight: their TOTAL energy contribution also vanishes. The interior of (BIN) keeps the initial energy. Its sign is not inferred from this localization.

## 5. Exact falsifier of descent that uses only identities and tail

Observation. Modify only the constant of the archimedean part:

    W_4[f]=W[f]-4||f||².

The integer comb and the polar remain identical. Since the norm satisfies all the partitions, W_4 keeps EXACTLY (DEF), (BIN), the geometric mixtures and their normalizations. It also keeps the eventual positivity theorem of 015: the high-pass quotient grows at least (logk)/2-C_N, and subtracting 4 does not alter its positive divergence. Hence it also keeps all the eventual conclusions of (FD).

However, for f(y)=exp(-63y/2)1_{y>0}, the exact complete formula gives

    W[f]/||f||²=2L(32)<3,
    W_4[f]/||f||²<-1.

The bound is elementary: psi(16)=H15-gamma<H15, logpi>1 and zeta'(32)/zeta(32)<0. Hence 2L(32)<H15-1+1/16+2/31<3, and this last rational comparison is verified in tools/power_descent_016_verify.py. ALL contacts are included through the exact sign of the convergent series of zeta'/zeta; no approximations of special constants are used.

The inference «complete exact partitions + positive mixture + uniform eventual positivity at each fixed order imply initial positivity» is FALSIFIED. All those statements are true for W_4, but its explicit initial datum is negative. This class of descent must use some additional quantitative estimate that distinguishes the real multiplier from the shifted one. Even keeping Lambda exactly does not suffice if its interaction with the archimedean constant does not appear in that estimate.

It is NOT a counterexample to the form W of the paper: W_4 is an explicitly modified form. Nor is a descent excluded that controls W[Lf] with the complete arithmetic datum or uses the spectral distribution of the numerator. The result excludes only the inference based on the structural properties and the tail already available.

## 6. Obligation remaining after the exact defect

The defect W[f]-W[Qf] is the COMPLETE form of Lf. Neither the stable filter L, nor Lambda>=0, nor the sign of the high-pass tail prove its positivity in the first steps. A new descent inequality would have to control this low-frequency block with the real multiplier and the arithmetic autocorrelations, or couple it explicitly with the high-pass block; assuming that sign reintroduces the pending obligation.

The localization (LOC) offers a concrete restriction for that inequality: it must act on the interior j/m, not only on a fixed number of diagonals of the eventually positive tail. This note does not yet provide that arithmetic control and does not declare global closure.
