# POWER_INTERIOR_017 — The whole scalar row N=1, with uniform margin and control of the WHOLE comb

Status: PROVED, for all k>=0 and all u>=63/2. It does not resolve the joint interior with N,k growing. Papers untouched.

## 1. Result and new reason with respect to the corpus

Read POWER_STATE_015/016, POWER_TATE_CHAIN_009, POWER_PACKET_SCOPE_AUDIT_009, POWER_HIGHPASS_015, POWER_DESCENT_016 and index/grid/crossword through searches for rational chains, high-pass, resolvent powers and beta packets. The Tate family 009 increases the order with fixed numerator s²-1/4 and concentrates at frequency zero; its scalar identity gave no sign. Here N=1 is fixed and k is increased in

    F_k(s)=s^k/(s+u)^{k+1}, u>=63/2.

The new difference is an EXACT relative weighted-norm bound, UNIFORM IN ALL k, obtained via a convolution of binomial coefficients. It allows controlling the complete comb and the initial steps at the same time, without an unknown asymptotic threshold. The limit value E0 is not used, and it is not claimed that a single row closes all tests.

For the real causal function h_k with transform F_k we prove

    W[h_k]>(4/3)||h_k||², all k>=0,u>=63/2.             (ROW1)

These are confluent spaces of arbitrarily large orders k+1, though with a specific numerator. No sign is inferred for their arbitrary combinations.

## 2. New lemma: uniform weighted quotient for the whole row

More generally, fix u>0 and 0<=eta<u/2. Put a=u-eta, b=eta and c_k=binom(2k,k)/4^k. Then

    ||h_k||²=c_k/(2u),
    ||exp(eta y)h_k||²/||h_k||²
       <=u(u-eta)/[u(u-2eta)]
       =(u-eta)/(u-2eta), all k>=0.                    (WR)

Proof. Plancherel on the line s=-eta+i tau gives

    N_k(eta)=(1/2pi)∫(tau²+b²)^k/(tau²+a²)^{k+1}d tau.

For 0<=z<1, summing the geometric series inside the integral produces exactly

    Σ_{k>=0}N_k(eta)z^k
       =1/[2sqrt((1-z)(a²-b²z))].                        (GEN)

All terms are nonnegative and a>b. Expanding the two binomial factors,

    N_k(eta)=[1/(2a)]Σ_{j=0}^k c_{k-j}c_j(b²/a²)^j.

When eta=0 this gives N_k(0)=c_k/(2u). The combinatorial inequality

    c_{k-j}c_j<=c_k

follows from Vandermonde: the product binom(2j,j)binom(2k-2j,k-j) is ONE of the nonnegative terms summing to binom(2k,k). Hence

    N_k(eta)/N_k(0)
       <=(u/a)Σ_{j>=0}(b²/a²)^j
       =u a/(a²-b²)=(u-eta)/(u-2eta).

No large k has been taken and no leading coefficient estimated: (WR) holds simultaneously at every order, including k=0.

With eta=15 and u>=63/2, the right-hand side is <=11, since (u-15)/(u-30) decreases in u>30. Hence

    ||exp(15y)h_k||<=sqrt11||h_k||.                       (W11)

## 3. Archimedean part: uniform margin from the first step

The spectral density of h_{k+1} reweights that of h_k by q(tau)=tau²/(u²+tau²), increasing in |tau|. Since m increases in |tau|, positive covariance proves that the NORMALIZED archimedean energy does not decrease with k. Thus

    Arch[h_k]/||h_k||² >=psi((u+1/2)/2)-logpi
                         >=psi(16)-logpi>3/2.

The last bound is elementary: psi16=H15-gamma, gamma<3/5, logpi<6/5 and H15-9/5>3/2. The bounds on gamma and logpi were already certified rationally in previous rounds; the verifier of this note checks them again with those intervals.

This comparison only asserts archimedean monotonicity. The polar term alternates and the comb has no sign by covariance.

## 4. Exact polar term, preserved and uniformly bounded

The two moments of h_k are F_k(-1/2) and F_k(1/2), so that

    Polar[h_k]=2(-1/4)^k/(u²-1/4)^{k+1}.

Dividing by c_k/(2u) gives

    |Polar[h_k]|/||h_k||²
      =[4u/(u²-1/4)]*[1/(4u²-1)]^k/c_k.

We have c_k>=2^-k, since binom(2k,k)=Π_{j=1}^k(k+j)/j>=2^k. Hence the second factor is <=[2/(4u²-1)]^k<=1 on the declared range. Moreover 4u/(u²-1/4) decreases for u>1/2. Consequently

    |Polar[h_k]|/||h_k||²<=126/992=63/496.                (POL)

The polar term is neither cancelled nor omitted; its complete formula is kept and its worst sign is counted.

## 5. ALL arithmetic contacts, without truncation

From (W11), for any t>=0,

    |c_hk(t)|<=||h_k||*||h_k 1_{y>=t}||
             <=sqrt11 exp(-15t)||h_k||².

Thus the infinite comb, which converges absolutely, satisfies

    |Comb[h_k]|/||h_k||²
       <=2sqrt11 Σ_{q>=2}Lambda(q)q^{-31/2}
       <7Σ_{q>=2}q^-14
       <=105/[13*2^14]<1/2000.                           (PRIME)

We used 2sqrt11<7, Lambda(q)<=logq<=q, q^-29/2<=q^-14 and the integral comparison Σ_{q>=2}q^-14<=2^-14(1+2/13). This estimate includes all prime powers; it does not presume that the contacts help nor change the coefficients of Lambda.

## 6. Closure of the row and scope

Adding the three complete components,

    W[h_k]/||h_k||²
       >3/2-63/496-1/2000
       =42547/31000>4/3.

This proves (ROW1) for ALL k, with a margin independent of k and u>=63/2. The finite computation of constants is reproduced with `python3 03-research/phase-211-sign-sandbox/tools/power_interior_017_verify.py`; the inequalities for all k come from (GEN) and Vandermonde, not from a list of checks.

The row N=1 does not cover the joint regime with finite k/N when N also grows, which remains pending. The scalar bridge of round 017 requires ALL rows N,k; it does not allow replacing them by this row, by the eventual tail or by a dense union of individual tests. The reusable advance is (WR): a uniform weighted quotient that keeps the whole orbit, and could serve as the basis of a quantitative descent between rows if that additional arithmetic step is built.

## 7. Quantitative extension to ALL rows: weighted norm uniform in k

This additional lemma does not claim a sign for all rows. For integers N>=1,k>=0, define

    F_{N,k}(s)=s^k/(s+u)^{N+k},
    a=u-eta, b=eta, rho=b²/a², 0<=eta<u/2,
    B_l^(N)=Π_{r=0}^{N-2}(2l+2r+1)/(2r+1).

The empty product for N=1 equals one. Then, for ALL k,

    ||exp(eta y)f_{N,k}||²/||f_{N,k}||²
      <=R_N(u,eta):=(u/a)^{2N-1}S_N(rho),
    S_N(rho)=Σ_{l>=0}B_l^(N)rho^l.                       (WRN)

The constant is explicit and computable with a FINITE number of operations: B_l^(N) is a polynomial in l of degree N-1 and

    S_N(rho)=Π_{r=0}^{N-2}
       [(2rho d/drho+2r+1)/(2r+1)] (1/(1-rho)).

Hence S_N is a rational function with denominator dividing (1-rho)^N; it is not an unknown arithmetic statistic nor an asymptotic limit. For example

    S_1=1/(1-rho), S_2=(1+rho)/(1-rho)².

Proof of (WRN). Expanding the positive numerator (tau²+b²)^k inside the Plancherel integral and using the beta integral gives

    N_{N,k}(eta)=a^{1-2N}/(2pi)
       *Σ_{l=0}^k binom(k,l)rho^l
            Beta(k-l+1/2,N+l-1/2),
    N_{N,k}(0)=u^{1-2N}/(2pi)Beta(k+1/2,N-1/2).

The quotient of each beta coefficient factors EXACTLY as

    binom(k,l)Beta(k-l+1/2,N+l-1/2)
         /Beta(k+1/2,N-1/2)
       =[c_{k-l}c_l/c_k]B_l^(N).

Vandermonde bounds the bracket by one. All terms are nonnegative; extending the sum from l<=k to l>=0 proves (WRN). The series converges because rho<1 and B_l^(N) grows only polynomially.

For eta>1/2, this inequality immediately gives control of the COMPLETE comb, uniform in k,

    |Comb[f_{N,k}]|/||f_{N,k}||²
      <=2sqrt(R_N(u,eta))Σ_{q>=2}Lambda(q)q^{-eta-1/2}.

Thus there is an effective constant per row N that also controls its first steps. This differs from 015, where the weighted quotient was controlled asymptotically for large k through limit matrices. Here there is no threshold in k; the dependence on N remains and it has not been proved small enough to close the complete table.
