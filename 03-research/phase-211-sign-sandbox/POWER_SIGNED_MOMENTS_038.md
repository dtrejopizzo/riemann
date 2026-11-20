# POWER_SIGNED_MOMENTS_038 — Signed product kept via gamma Fourier

Status: **PROVED**, independent adversarial review approved in POWER_SIGNED_AUDIT_038.md and exact verifier PASS reproduced. Fixed rate u=63/2. Papers untouched.

Result: the central error of Möbius grouping is controlled by B_Q/N WITHOUT the factor V_Q/U_Q; that factor remains only in an exponentially small tail. No sign of W nor of the infinite residue is claimed.

## 1. Corpus and precise difference

Consulted ROUTES-TRIED-INDEX/README.md, master grid and CROSSWORD-TO-D; read ENERGY_GROUP037, UNIFORM_CUTOFF026 and MOVING_BALANCE036. The entries542/543 of the index treat cumulants of a class-group calibrator and different full forms. Here the object is a FINITE Möbius product over divisors of Q applied to the same REAL gamma profile037. No Jensen inequality is used for a signed measure.

The difference from037 is to keep exactly the signed multiplier in Fourier and to estimate the logarithm of its centred part in the frequency band relevant for gamma. The divisor modulus sum V_Q/U_Q is only used outside that band, where the gamma transform is already exponentially small. The moment identity alone is not called a sign bound.

## 2. Extended real profile and finite operator

Set d=N−1,a=u²−1/4=992,c_N=d/a and rho=rho_N, extended EVENLY to all of R. Define g(y)=rho(y)/2−rho'(y) and

    f_N(ell)=e^(ell/2)g(c_N+ell)/g(c_N).

For ell>=0, it is precisely the real profile r_N of037:

    f_N(ell)=e^ell D_N(e^ell).

For ell<−c_N the factor g can be negative. f_N is NOT considered a positive density on all of R. The positive density used to normalize the transform is introduced separately in§4.

For finite squarefree Q, define

    U_Q=prod_(p|Q)(1−1/p), V_Q=prod_(p|Q)(1+1/p),
    A_Q=sum_(p|Q)logp/(p−1),
    B_Q=sum_(p|Q)p(logp)²/(p−1)²,
    M_Q f(ell)=U_Q^(-1)sum_(b|Q)mu(b)b^(-1)f(ell+logb).

The grouped kernel037 satisfies K_(N,Q)(m)=(U_Q/m)M_Q f_N(logm). The parameters A_Q,B_Q are not interpreted as mean/variance of a probability: the first two signed cumulants are−A_Q and−B_Q.

## 3. Exact Fourier product and centred remainder

With Z_Q(z)=prod_(p|Q)(1−p^(z−1)), the multiplier of M_Q at real frequency xi is Z_Q(i xi)/U_Q. The ABSOLUTE expansion

    log[Z_Q(i xi)/U_Q]
      =−sum_(p|Q)sum_(k>=1)[exp(ik xi logp)−1]/(k p^k)

chooses the continuous branch equal to0 at xi0. Subtracting the linear term and using |exp(it)−1−it|<=t²/2 proves for ALL real xi

    |log[Z_Q(i xi)/U_Q]+iA_Q xi|<=B_Q xi²/2.

In particular

    |Z_Q(i xi)/U_Q−exp(−iA_Q xi)|
       <=(B_Q xi²/2)exp(B_Q xi²/2).                      (CENTRAL-MULT)

No sign is assigned to a cumulant nor is signed convexity applied. For the tail the general bound suffices

    |Z_Q(i xi)/U_Q−exp(−iA_Q xi)|<=V_Q/U_Q+1.             (TAIL-MULT)

## 4. Exact gamma transform and normalization at the centre

Use Fourier with exp(−i xi y). In this section norm²=Gamma(N−1/2)/[2sqrt(pi)Gamma(N)u^(2N−1)] is the normalization of the original gamma atom. The normalized autocorrelation has

    rhohat(xi)=1/[norm²(u²+xi²)^N].

The shift and the exponential weight give exactly

    fhat_N(xi)=C_N exp(i xi c_N)(1−i xi)
                        (a+xi²+i xi)^(-N),
    C_N=exp(−c_N/2)/[norm² g(c_N)]>0.                   (FOURIER)

The factor1−i xi comes from integrating rho' by parts against exp((1/2−i xi)y). The squared modulus of the denominator is

    |a+xi²+i xi|²=a²+1985xi²+xi^4.

To control C_N without exponential losses, introduce the POSITIVE probability

    p_N(y)=exp(y/2)rho_N(y)/L_N,
    L_N=int_R exp(y/2)rho_N(y)dy=1/(norm² a^N).

Its mean and variance, by differentiating the positive bilateral transform, are

    E Y=N/a,
    sigma_N²=1985N/a².

The function p_N is unimodal: for y<0 its logarithmic derivative is1/2+q_N(|y|)>0 and for y>0 it is1/2−q_N(y), with q_N strictly increasing. Let y_* be its unique mode, q_N(y_*)=1/2. Riccati026 gives

    y_*=d/[a+q_N'(y_*)],
    0<=c_N−y_*<=dM_N/a²<=u²/a²,
    M_N=u²/(2N−3).

Since0<q_N'<M_N,

    p_N(c_N)>=p_N(y_*)exp[−M_N(c_N−y_*)²/2]
             >p_N(y_*)/2.

The last bound follows from M_N<=u² and u^6/(2a^4)<log2, an elementary rational comparison. Chebyshev concentrates at least3/4 of the mass on an interval of length4sigma_N, hence p_N(y_*)>=3/(16sigma_N). One concludes

    p_N(c_N)>=3/(32sigma_N),
    C_N a^(-N)=1/[(1/2+q_N(c_N))p_N(c_N)]
                <=32sigma_N/3<sqrt(N)/2.                (NORMALIZER)

Here q_N(c_N)>1/2 from037 was used. The comparison with the mode and the variation control are essential: Chebyshev and unimodality alone would not give a lower bound at an arbitrary point.

## 5. Central envelope and integrable tail

Let c=1985/a². NORMALIZER and FOURIER give

    |fhat_N(xi)|<sqrt(N)/2 ·sqrt(1+xi²)
                   [1+c xi²+xi^4/a²]^(-N/2).

For |xi|<=1, log(1+c xi²+xi^4/a²)>=(1985/(a²+1986))xi²>=xi²/500. Thus

    |fhat_N(xi)|<=sqrt(N)exp(−Nxi²/1000).                (CENTRAL-GAMMA)

For |xi|>=1, the power of1+c xi² is split into two halves. If N>=16,

    [1+c xi²]^(-N/2)
      <=(1+c)^(-N/4)[1+c xi²]^(-4).

Since c>1/500 and log(1+c)>=c/(1+c)>1/500, and using sqrt(1+xi²)<=1+|xi|,

    int_(|xi|>=1)|fhat_N(xi)|d xi/(2pi)
       <65sqrt(N)exp(−N/2000).                          (TAIL-GAMMA)

An explicit majorant of the auxiliary rational integral on all of R is260: int_0^infty(1+c xi²)^(-4)d xi<46 and int_0^infty xi(1+c xi²)^(-4)d xi<84. 2pi is kept in the normalization and only pi>1 is used for the bound65.

## 6. Main inequality

**Theorem.** If N>=16 and B_Q<=N/1000, then for ALL real ell,

    |M_Q f_N(ell)−f_N(ell−A_Q)|
       <=12000 B_Q/N
          +65sqrt(N)(V_Q/U_Q+1)exp(−N/2000).             (SIGNED-FOURIER)

Proof. Invert Fourier, keep the signed multiplier and subtract the exact shift exp(−iA_Q xi). On |xi|<=1, CENTRAL-MULT and CENTRAL-GAMMA are multiplied; B_Q<=N/1000 leaves exp(−Nxi²/2000). Extending the positive integral to R gives

    (B_Q/2)sqrt(N)int_R xi²exp(−Nxi²/2000)d xi/(2pi)
      =2000^(3/2)B_Q/[8sqrt(pi)N]<12000B_Q/N.

On |xi|>=1 TAIL-MULT and TAIL-GAMMA are combined. All integrals are absolute, and Q is finite. This proves the inequality, without making Z_Q/U_Q a probability.

The leading term is a SHIFT of the real gamma profile by the first signed moment, not simply1. The negative second cumulant is controlled analytically by B_Q in the central error; its sign is not used as if it were a positive variance.

## 7. Corollary: window of order sqrt(N) for the SAME family Q037

For ALL N>=2^80 keep exactly the choice of037:

    K=floor(N^(1/8)), Q=prod_(p<=K)p.

Then for ALL m with

    A_Q<=logm<=A_Q+sqrt(N)/100,

the REAL grouped kernel satisfies

    (4/5)U_Q/m<K_(N,Q)(m)<(6/5)U_Q/m.                    (WIDE-WINDOW)

It is an analytic enlargement of the logarithmic length, from order N^(1/4) in037 to order sqrt(N), without running over new N or Q. It is not a conclusion about the infinite exterior sum.

Proof. The elementary bounds037 give A_Q<=logQ<=KlogK<=K²<=N^(1/4) and V_Q/U_Q<=N^(1/4). Moreover B_Q<=log²Q for this family, which contains2 and3. Indeed p/(p−1)²<=1 for p>=3, the term p2 is2log²2, and the cross product2log2log3 inside log²Q dominates the additional log²2. Hence B_Q<=sqrt(N)<=N/1000.

The central error of SIGNED-FOURIER is <=12000/sqrt(N)<1/100. The tail error is also <1/100: V/U+1<=2N^(1/4) gives a prefactor<=130N, and exp(−N/2000)<=2(2000/N)² produces the majorant1.04·10^9/N.

Write s=logm−A_Q in[0,sqrt(N)/100]. The shifted profile is on its positive physical side. DILATE037 gives directly

    exp{−M_N[s/1985+s²/2]}<=f_N(s)<=1+M_Ns.

Since M_N<=u²/N and N>=2^80, the exponent is <=u²[1/(198500sqrt(N))+1/20000]<1/10, while M_Ns<1/100. Hence9/10<f_N(s)<101/100. Subtracting/adding the two errors smaller than1/100 proves

    4/5<M_Q f_N(logm)<6/5.

Multiplying by U_Q/m proves WIDE-WINDOW. All endpoints and monotone inequalities are verified via the rational constants of the script. The even extension of f is not interpreted as a probability; in this corollary all its physical arguments are nonnegative.

## 8. Scope and pending obligation

SIGNED-FOURIER eliminates V_Q/U_Q from the CENTRAL error that dominated037. That factor remains only multiplied by an exponential tail in N. It allows formulating effective sign conditions for a growing Q if the shifted profile is favourable and the two errors are smaller than it; those conditions must be proved before concluding a sign.

The theorem does not yet control the exterior sum over m coprime to Q nor the full integral of the polar−comb residue. Nor can the error O(B_Q/N) be sold as a sufficient relative error against components of phase lambda^N. W positive, h_N positive or an absolute contraction of the remainder are not declared.

The even extension of rho is used only to obtain FOURIER. Outside the physical side of the shift, f_N can take signs; Jensen is not applied nor is a positive law attributed to it. The only auxiliary probability used is p_N in§4, whose role is to normalize and locate its mode with explicit control.

## 9. Validation

POWER_SIGNED_AUDIT_038.md independently approves FOURIER/NORMALIZER, central and tail constants, branch of the logarithm of the finite product, normalization2pi and absence of probabilistic interpretations for the signed operator. The corollary WIDE-WINDOW was also reviewed twice independently.

Verifier: tools/power_signed_moments_038_verify.py, Fraction/intervals of constants; PASS. It does not evaluate W at new N nor lists of Q: only the constants of the analytic families. Papers untouched.
