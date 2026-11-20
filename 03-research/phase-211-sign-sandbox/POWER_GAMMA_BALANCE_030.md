# POWER_GAMMA_BALANCE_030 — Sign of the integrated gap for a REAL gamma law

Status: PROVED uniform constructive bound of the ARCH_sharp gap for the real gamma law; PROVED a strictly negative complete gap for N2,u63/2. Independent review APPROVED and verifier reproduced with PASS. No campaign. Papers untouched.

## Corpus and new reason before building

Read the project rules, INTERIOR_CONSTRAINT027, rows018/028 and the current statuses; search in index/grid/crossword (gamma mixture/Jensen/Gaussian of equal variance/integrated gap). The heat mixture and the lack of global Gaussian convexity are already recorded027 and are NOT presented as novelties.

The difference is to evaluate the SIGN of the gap against the law L_N of a REAL test, at the fixed rate u=63/2. Negative curvature in a generic range did not decide that pairing. A single concrete premise is to be decided: «the full form of the gamma test is at least that of the Gaussian with the same second spectral moment». Negative W will not be inferred from that comparison failing.

The following constructive part holds for ALL N>=2 at the fixed rate. The directed full comparison is fixed only at N=2, where the gamma formulas and the favorable bound of the Gaussian polar allow an elementary proof with all the arithmetic. No sweeps of N nor another wedge of variable u are made.

## 1. CONSTRUCTIVE bound for ALL N: cost of the sharp gap

Keep u=63/2, beta=u²/4, b=N−1/2>1, V=beta/G with G~Gamma(b,1), m=EV=beta/(b−1). As in027,

    rho_N(t)=E e^(-Vt²),
    L_N(a)=E(V−a)_+−(m−a)_+>=0,
    ARCH_sharp[g_N]/||g_N||²=E A_sharp(V).

The uniform bound is proved:

    0<A_sharp(m)−ARCH_sharp[g_N]/||g_N||²
       <=(1/2)[psi(b)−log(b−1)]<1/[2(b−1)].             (SHARP-GAP)

This quantitatively repairs the unfavorable direction of Jensen: the Gaussian of equal second moment does produce a LOWER bound after paying an explicit cost O(1/N), without requiring false convexity.

Proof. The positive sharp kernel satisfies

    K_sharp(t)=2e^(-5t/2)/(1−e^-2t)
               =2e^(-t/2)/(e^2t−1)<=1/t.

Hence

    0<−A_sharp''(a)=∫K_sharp(t)t^4e^(-at²)dt<=1/(2a²).

The hinge formula for the convex function−log gives EXACTLY

    ∫_0^infinito L_N(a)a^-2da
       =log(EV)−ElogV=psi(b)−log(b−1).

It is finite for all b>1, EVEN N2 where ∫L_N is infinite. Integrating the curvature bound against L_N proves the first bound. Finally psi(b)<=logb and log[b/(b−1)]<1/(b−1). The strict left sign was already proved027 via the nondegeneracy of V. No absolute budget of the comb is added and the gamma carrier is not changed.

In particular a valid lower inequality remains for the sharp part:

    ARCH_sharp[g_N]/||g_N||²
       >=A_sharp(m)−(1/2)[psi(N−1/2)−log(N−3/2)].

The signed arithmetic fluctuation ERR still needs its own comparison. SHARP-GAP does not replace it nor declare a sign of W.

## 2. Full premise decided on a real law

Let G_W(v) be the full form of the Gaussian test of norm one and autocorrelation e^(-vt²). The identity027 keeps all pieces and says

    W[g_N]/||g_N||²−G_W(m)=∫L_N(a)G_W''(a)da.           (FULL-GAP)

For the REAL law N=2,u=63/2, m=u²/2, it is proved that

    W[g_2]/||g_2||²<17/20,
    G_W(u²/2)>7/8,
    ∫L_2(a)G_W''(a)da<−1/40.                           (NEG-GAP)

This refutes the full inequality «the gamma test dominates the Gaussian of equal second moment» for a concrete member of the original family. It is more specific than the lack of global convexity027: there the pairing against no particular law L_N was decided.

## 3. Gamma upper bound with all the arithmetic

The normalized archimedean energy of g_2 is

    d−b0=psi(16)−logpi−(63/4)psi'(16)<59/100.

The verifier encloses gamma and logpi with the audited rational module and uses the positive sum of psi'16 up to255 plus its lower integral tail. The normalized polar is

    p20=8/u·[u²/(u²−1/4)]²<13/50.

The autocorrelation C_2(t) is positive for all t, so ALL prime contacts contribute negatively to W[g_2]. They are kept with the correct sign in an upper bound:

    W[g_2]/||g_2||²<59/100+13/50=17/20.

The comb is not taken as zero in an identity nor is the full value inferred from a truncated sum.

## 4. Gaussian lower bound that keeps the gain of the polar

Let v=u²/2. Its spectral probability is centered normal with deviation u, with maximal density pmax=1/[u sqrt(2pi)] and

    Elog|tau|=logu−(gamma+log2)/2.

A digamma bound tighter than the constant error4 of the global lower bound is needed. Euler–Maclaurin and integrating the periodic Bernoulli function once give, for z=a+it,a>0,

    psi(z)=logz−1/(2z)−1/(12z²)
                    +∫_0^infinito B2({x})(z+x)^-3dx.

Since |B2|<=1/6, the remainder has modulus <=1/(12a²). Hence

    Re psi(a+it)>=log|a+it|−Re[1/(2(a+it))]−1/(6a²).

Applying a=5/4 and the recurrence from1/4 proves

    m(tau)>=log(|tau|/(2pi))−8/75
        −(5/4)/[2((5/4)²+tau²/4)]−1/(tau²+1/4).

The two reciprocal kernels have integrals pi and2pi, respectively, so their average cost is <=3pi pmax=3sqrt(pi/2)/u. The exact Gaussian polar is

    2sqrt(pi/v)exp(1/(16v))
       >4sqrt(pi/2)/u.

Keeping it BEFORE rounding cancels three quarters of that loss and leaves

    ARCH_gauss+Polar_gauss
      >log(u/(2pi))−(gamma+log2)/2−8/75+1/u,            (GP)

using sqrt(pi/2)>1. This joint step is a real lower bound; convexity of G_W is not presumed.

For the Gaussian comb, logq>=log2>2/3 and u²/3>20 imply v(logq)²>20logq. Thus

    |Comb_gauss|<=2Σ(q>=2)q^-19<1/1000,

using Lambda(q)<=q and relaxing a power1/2. It is the complete infinite sum, not a segment.

Finally pi<22/7 gives u/(2pi)>441/88=4(441/352). With log2>693/1000 and the first atanh term,

    log(u/(2pi))>2(693/1000)+178/793.

Together with gamma<3/5,log2<7/10 and u63/2, the side of GP minus1/1000 is strictly greater than7/8 by a rational comparison. This proves NEG-GAP.

## 5. Verification, missing balance and scope

The verifier `tools/power_gamma_balance_030_verify.py` checks the real N2 bounds, the Euler/Bernoulli constants and the complete Gaussian lower bound via Fraction. It contains neither a sweep over N nor a quadrature.

SHARP-GAP is indeed a uniform integrated estimate over the REAL weight L_N and gives a controlled cost for a negative component. NEG-GAP shows that the full comparison without cost cannot replace it. For a lower bound of W one would still need to control the SIGNED change of ERR together with that loss, or the full pairing L_NG_W'' with its term G_W(m), without discarding the polar nor turning the comb into an absolute value that reproduces018.

W[g_2]<0 is not proved: row N2 already has a proved positive sign. The coverage of W is not extended here, N>=6 is not decided and no sign of FULL-GAP is claimed for other N. The constructive contribution is SHARP-GAP; the precise counterexample delimits the full premise that cannot be used without that new arithmetic compensation.
