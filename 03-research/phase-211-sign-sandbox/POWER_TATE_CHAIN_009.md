# POWER_TATE_CHAIN_009 — Exact identity of the whole sum for the Tate chain

Status: PROVED identities and scalar reduction of the family; OPEN its sign for all orders. No new convexity proof is claimed. Papers untouched.

## 1. Antecedents and explicit reason

Read the project rules, POWER_PRIME_PATTERN_FALSIFIER_008/STATE008 and the index entries: Euler/Möbius/N_018; PROOF_L_SHARP_E/J (collapse Λ*1=log and moments); A_MU_FACTORIZATION/AUDIT200 (transversal convexity not automatic); LEMMA_F_HALFLINE (counterexample to uniform convexity). Consulted grid part 3 (Laguerre/fluctuation integrals) and the crossword according to POWER_BRIDGE_002. R5 of the open inventory records E_gamma, with criticality and failure of generic uniform bounds.

The difference delimited here is to evaluate a VERY specific one-parameter family, with fixed numerator s²−1/4 and denominators (s+31.5)^n. Convexity of all tails is not relaunched, nor is a sign attributed to an Euler identity. The question asked also allows an exact reduction that identifies the remaining signed statistic; that is what is obtained.

## 2. Three gamma kernels, without expanding a huge polynomial

Fix u=63/2, a=u²−1/4=992. For n>=1 define

    g_n(y)=y^(n−1)e^-uy/(n−1)! ·1_(y>0),
    C_n(t)=c_gn(t),
    ghat_n(tau)=(u−i tau)^-n.

For n>=3 write f_n=(∂²−1/4)g_n; to avoid any boundary regularity issue in the forms one may take n>=4, which includes case 008. Its two polar moments vanish and its Laplace transform is (s²−1/4)/(s+u)^n.

The Fourier identity

    (tau²+1/4)²/(tau²+u²)^n
       =a²/(tau²+u²)^n−2a/(tau²+u²)^(n−1)
                       +1/(tau²+u²)^(n−2)

gives exactly, for all real t,

    c_fn(t)=a² C_n(t)−2a C_(n−1)(t)+C_(n−2)(t).          (G)

Each C_j is positive. The relevant signed autocorrelation is, however, a second difference of THREE positive kernels; it has no sign imposed by individual positivity. This identity keeps all cancellations without printing the n Laguerre coefficients.

By gamma integration, for t>=0,

    C_n(t)=e^-ut/Γ(n)² Σ(j=0..n−1) β_nj t^j,
    β_nj=binom(n−1,j)Γ(2n−1−j)/(2u)^(2n−1−j)>0.         (CG)

All the following arithmetic series converge absolutely: u+1/2=32 and the polynomials are finite for each n.

## 3. The sum over ALL contacts as an explicit scalar statistic

Define

    I_n(u)=(1/2pi)∫_R m(tau)(tau²+u²)^-n d tau,
    J_n(u)=2Σ(m>=2)Lambda(m)m^-1/2 C_n(log m)>0.

The archimedean part is computed without additional spectral reference by

    I_1(u)=[psi((u+1/2)/2)−log pi]/(2u),
    I_n(u)=−[2u(n−1)]^-1 ∂_u I_(n−1)(u).

If D(s)=Σ(m>=2)Lambda(m)m^-s=−zeta'(s)/zeta(s), s>1, then CG gives

    J_n(u)=2/Γ(n)² Σ(j=0..n−1)β_nj (−1)^j D^(j)(u+1/2). (J)

It is the complete sum, not a truncation nor an asymptotic expansion. The terms of J separately are positive, but the combination of three orders imposed by G has coefficients a²,−2a,1.

The moments of g_n are (u−1/2)^-n and (u+1/2)^-n. Therefore

    W[g_n]=I_n−J_n+2a^-n.

Set q_n=a^n W[g_n]=a^n(I_n−J_n)+2. Applying linearity of the Weil distribution in the autocorrelation to G,

    W[f_n]=a^(2−n)[q_n−2q_(n−1)+q_(n−2)].              (CHAIN)

The polar contributions cancel exactly: 2−4+2=0 after normalization. This is a result for the whole family, independent of any computation of large coefficients.

**Remaining precise scalar objective:** prove discrete convexity of the explicit sequence q_n for all n>=4. CHAIN does not prove that convexity. The sequence mixes the gamma contribution I_n with the complete arithmetic statistic J_n.

## 4. What Λ*1=log does exactly and what it does not

The Euler identity for s>1 is

    D(s) zeta(s)=Σ(m>=1)(log m)m^-s=−zeta'(s).

Differentiating j times expresses the numbers of J as a triangular recurrence among positive sums. Explicitly, with H_j(s)=ΣLambda(m)(log m)^j m^-s and Z_j(s)=Σ(log m)^j m^-s,

    Σ(r=0..j)binom(j,r) H_r(s) Z_(j−r)(s)=Z_(j+1)(s).

Solving for H_j requires SUBTRACTING all terms r<j; solving at once introduces the Möbius signs. Thus Euler identifies the arithmetic values exactly and allows computations, but does not automatically transform the second difference of CHAIN into a positive sum. This point coincides with the cited Euler/Möbius antecedents; it is not presented as the discovery of a new barrier.

Neither the positivity H_j>0, nor the ordinary log-convexity of Z_j, nor the positivity of C_n justify the sign of Δ²q_n: the three signed combinations remain. It is not claimed that it is impossible to find a more precise positive identity for this datum; one has not been constructed here.

## 5. Exact relation with test 008 and with E_gamma

Test 008 is a multiple of f_n with n=2^17. Its TAIL obligation is CHAIN written separating the contacts m<=1024 from the rest, keeping the same autocorrelation G. The J/CHAIN formulas sum formally and absolutely that whole tail, but still leave its value and sign in a combination of derivatives of D at 32.

The normalized spectral density of f_n is proportional to (tau²+1/4)²/(tau²+u²)^n and concentrates at tau=0 as n grows; its beta moments prove this directly. This places it in the regime of zero-frequency concentrating packets related to the residue E_gamma of the inventory. It is not uniform control of all packets nor a new Chebyshev inequality: it is only a concrete gamma family, with a formula for all its orders. The problems already recorded do not supply the specific discrete convexity of q_n; nor does their criticality prove that this convexity is false.

## 6. Finite inequality valid for the whole chain: ARCH strictly worsens

Let p_n be the normalized spectral density of f_n and E_n its expectation. Then

    p_(n+1)(tau)=w(tau)p_n(tau)/E_n w,
    w(tau)=1/(u²+tau²).

Therefore, for the normalized archimedean energy alpha_n=E_n m,

    alpha_(n+1)−alpha_n=Cov_n(m,w)/E_n w<0.              (MON)

The symbol m is strictly increasing in |tau| and w strictly decreasing. The strict sign of the covariance is proved by integrating [m(x)−m(y)][w(x)−w(y)]/2 against p_n(x)p_n(y). The density is not a point mass. Thus MON is a finite inequality for ALL orders, not an asymptotic observation. Its limit is m(0), by the beta formulas and concentration.

An additional quantitative estimate keeps n explicit. For n>=7, the beta moments of §008 give

    E_n tau² ≤u²/n+24u^4/n²+240u^6/n³.

If n>=64u², the right-hand side is <2u²/n. Using the bound m(tau)≤m(0)+17tau² already proved in 008,

    alpha_n <m(0)+34u²/n,
    c_fn(t)/||f_n||² >1−u²t²/n.

In particular, if n>=64u² and n>=2u²(log R)², each prime-power contact m<=R harms the sign with autocorrelation at least ||f_n||²/2. It is a uniform and explicit version of the computation 008 for any finite segment. It recovers the already known mechanism of negativity of sub-combs; it is not presented as a new route to the complete sign. The repair must come from contacts that escape with n.

No one-directional inequality is obtained for the COMPLETE energy: changing n also multiplies each cos(tau log m), a non-monotone function. The covariance term of the comb keeps both signs. Hence MON does not imply monotonicity nor complete monotonicity of q_n. Positivity of D and of its alternating derivatives does not by itself give those properties of q_n either, which incorporates the gamma part and a signed combination of orders.

## 7. Why the sign of this family alone would not close all tests

Each individual member has the time expression

    f_n(y)=y^(n−3)e^-uy/Γ(n)
        ·[(n−1)(n−2)−2u(n−1)y+a y²], y>0.

It has at most two sign changes. Scalar multiples of individual members are not dense in the set of real tests: a test that alternates sign with fixed amplitude on four disjoint intervals cannot be approximated in L² by functions with at most two changes. If the intervals have positive length, every approximant leaves a uniform L² error on at least one.

This does not claim that its linear SPAN is small; combinations and their cross terms are another problem. Proving W[f_n]>=0 for each n only proves diagonals of a family; it does not prove W[Σc_n f_n]>=0. The density bridge of POWER_BRIDGE_002 requires positivity of all those combinations, which does not follow from scalar convexity of q_n.

## Result and scope

A closed identity of three gamma kernels and a single explicit scalar sequence were obtained, which keep the WHOLE arithmetic sum and the Tate cancellation. The sign for all n was not obtained. The new residue in its detail is Δ²[a^n(I_n−J_n)]>=0 for this fixed chain, not universal transversal convexity. Any next attempt must supply an inequality for this signed combination; repeating Λ*1=log, positivity of individual derivatives or generic convexity does not complete the proof.
