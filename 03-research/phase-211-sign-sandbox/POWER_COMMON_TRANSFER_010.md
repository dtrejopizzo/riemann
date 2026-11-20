# POWER_COMMON_TRANSFER_010 — Common deficit criterion and two weighted controls

Status: PROVED. Extracts the exact hypotheses of the transport FOUR009 and FIVE010; incorporates a norm improvement proposed in the main line of work. It claims no sign at arbitrary dimension. Papers untouched.

## 1. Explicit sufficient hypotheses

Fix an integer n>=1 and u>1/2. Let V0 be the rational space of transforms P(s)/(s+u)^n, degP<n. Suppose b,C,c,X,D are available, with X>0,D>=0,c>0, such that

    AP[f0]>=b||f0||²,
    |Polar[f0]|<=C||f0||², for all f0 in V0;
    m(tau)>=c when tau²>=X;
    tau²(c-m(tau))_+<=D, for all tau.

The first two are hypotheses on the WHOLE confluent block, not proofs on one vector; the last two are bounds on the symbol over the whole indicated domain. Define

    K_n=[(1+X/u²)^n-1]/X,
    eta=b-c-DK_n-Cn/(4u²).

If eta>0, then AP[f]>c||f||² for ALL poles v_j>=u, allowing multiplicities, and any real numerator of degree<n.

## 2. Single transport proof

The same numerator and the map H(s)=prod(s+u)/(s+v_j) are kept. With R=|H(i tau)|²,R0=prod u²/v_j²,r0=H(-1/2)H(1/2), one has

    R>=R0,
    R/R0<= (1+tau²/u²)^n,
    1-n/(4u²)<=r0/R0<=1.

The last bound uses r0/R0>= (1-1/(4u²))^n and Bernoulli. Even if the lower side of Bernoulli is negative, the loss bound1-r0/R0<=n/(4u²) remains valid. The quotient [(1+x/u²)^n-1]/x has nonnegative coefficients and increases for x>=0; on x<=X it is bounded by K_n.

The exact identity is

    AP[f]-c||f||²=R0(AP[f0]-c||f0||²)
       +integral (R-R0)(m-c)|fhat0|²/(2pi)
       +(r0-R0)Polar[f0].

Outside x<=X, the additional integral is nonnegative. Inside, at most R0 DK_n||f0||² is lost. The polar loss is at most R0 Cn/(4u²)||f0||². Thus the left-hand side is >=R0 eta||f0||²>0. The target norm is that of the NEW f; no uniform comparison between R0||f0||² and ||f||² is needed.

It is not a claim of monotonicity of the AP quotient nor of AP eigenenergies. Each use must verify its own b,C,c,X,D and eta; they are not inherited automatically from another degree.

## 3. Weighted control via Young, already used in the proofs

Fix 0<alpha<1 and sigma=alpha u. The orthonormal rational Malmquist basis is formed from an exponential sqrt(2v_j)e^(-v_j y) and j all-pass factors (s-v_k)/(s+v_k). The initial exponential has squared weighted norm v_j/(v_j-sigma)<=(1-alpha)^-1. The all-pass kernel delta0-2v e^(-vy), weighted by e^(sigma y), has total variation

    1+2v/(v-sigma)<=(3-alpha)/(1-alpha)=r_Y.

Young and Cauchy--Schwarz on the n coefficients give

    ||e^(sigma y)f||²<=B_Y||f||²,
    B_Y=(1-alpha)^-1 sum_(j=0)^(n-1) r_Y^(2j).

This is the valid bound used previously. For alpha2/3, B_Y=(49^n-1)/16; for alpha3/4, B_Y=(81^n-1)/20; for alpha1/2, B_Y=(25^n-1)/12.

## 4. Exact improvement via weighted Fourier multiplier

Young can be replaced by Parseval without any new sign assumption. All causal rational functions decay as polynomial times exponential with rates>=u>sigma; hence their weighting is in L² before estimating it. Weighting a filter amounts to evaluating its Laplace transform at s=-sigma+i tau. For a factor of rate v>=u,

    |(-sigma+i tau-v)/(-sigma+i tau+v)|²
      =[(v+sigma)²+tau²]/[(v-sigma)²+tau²]
      <=[(v+sigma)/(v-sigma)]²
      <=[(1+alpha)/(1-alpha)]²=r_F².

Thus each factor has weighted operator norm <=r_F. The initial exponential keeps the previous bound. By successive Parseval and Cauchy--Schwarz,

    ||e^(sigma y)f||²<=B_F||f||²,
    B_F=(1-alpha)^-1 sum_(j=0)^(n-1) r_F^(2j).

Since r_F<r_Y, this improves the bound without invalidating the previous certificates. For alpha1/2, B_F=(9^n-1)/4; for alpha2/3, B_F=(25^n-1)/8; for alpha3/4, B_F=(49^n-1)/12. The basis remains orthonormal only in the UNweighted norm; Cauchy--Schwarz is what allows summing their weighted norms, without attributing weighted orthogonality to them.

## 5. From a weighted bound to the complete comb

Either of B_Y,B_F gives

    |c_f(t)|<=sqrt(B)e^(-sigma t)||f||²,
    |Comb[f]|<=L||f||²,
    L=2sqrt(B) sum_(q>=2)Lambda(q)q^(-sigma-1/2).

The sum converges if sigma>1/2; this is an additional hypothesis necessary to use this majorant of ALL contacts. If sigma>3/2 one can use Lambda(q)<=q and p=sigma-1/2>1:

    L<=2sqrt(B)2^-p[1+2/(p-1)].

More tightly, for beta=sigma+1/2>1 and beta log2>=1, the function logx*x^-beta decreases for x>=2, so

    L<=2sqrt(B)2^-beta[log2+2log2/(beta-1)+2/(beta-1)^2].

If beta is replaced by a lower integer still >1, the required monotonicity must be preserved. Any rational upper bound for log2 may be used inside the last bracket. These majorants presume no favorable sign of any individual contact.

If eta>0 in §1 and L<c is certified, the complete result is W[f]>(c-L)||f||² on all those spaces of n poles. The criterion does not require an error margin independent of n; all constants must be verified for each application.

## 6. Additional improvement: maximal weighted trace at confluence

New observation, reviewed independently. Keep sigma=alpha u fixed, 0<alpha<1. For the orthonormal rational basis of rates v_j>=u, set

    R_j(tau)=[(v_j+sigma)²+tau²]/[(v_j-sigma)²+tau²].

The transform of mode j on the shifted line s=-sigma+i tau satisfies exactly

    |phi_jhat(-sigma+i tau)|²
       =(R_j-1)/(2sigma) prod_(k<j)R_k.

Summing telescopically gives

    sum_j |phi_jhat(-sigma+i tau)|²
       =[prod_j R_j-1]/(2sigma).                         (TR)

Integrating via Parseval gives the trace of the Gram matrix of the weighted norm. The inverse transform of R_j-1 is the positive function

    k_v(t)=2v sigma/(v-sigma) exp(-(v-sigma)|t|).

For fixed sigma and v>sigma, d_v log k_v(t)=-sigma/[v(v-sigma)]-|t|<0. Expanding prod_j R_j-1 over nonempty subsets, each spectral integral is the evaluation at zero of a convolution of positive functions k_v. These functions are integrable and bounded; the convolutions are finite, continuous and decrease when any of their rates increases. Hence the weighted trace is nonincreasing in each v_j and attains its maximum when all v_j=u.

At confluence, mode j is sqrt(2u)e^(-uy)L_j(2uy). With s=1-alpha, its squared weighted norm is

    integral_0^infinito e^(-sx)L_j(x)^2 dx
      =s^(-2j-1) sum_(k=0)^j binom(j,k)^2 alpha^(2k).

The identity is proved finitely using the polynomial connection

    L_j(x)=s^-j sum_(k=0)^j binom(j,k)(s-1)^(j-k)L_k(sx)

and orthogonality after the change of variable t=sx; reindexing k↔j-k produces the written formula. One thus obtains the additional uniform bound

    ||e^(sigma y)f||² <=B_T||f||²,
    B_T=sum_(j=0)^(n-1) sum_(k=0)^j
                binom(j,k)^2 alpha^(2k)/(1-alpha)^(2j+1). (BT)

Here one uses that the norm of a positive Gram matrix is bounded by its trace. MONOTONICITY OF THE TRACE under pole motion was proved; monotonicity of the largest eigenvalue of the Gram matrix was not proved. The operator bound comes from operatornorm<=trace and trace(v)<=trace(u), which suffices and avoids that unjustified inference.

B_T can replace B_Y or B_F in §5 without changing the transport criterion nor assuming monotone temporal localization. Its proof holds directly for repeated poles and for arbitrarily large rates, with sigma<min v_j ensured by alpha<1.
