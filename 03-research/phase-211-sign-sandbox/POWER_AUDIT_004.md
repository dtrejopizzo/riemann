# POWER_AUDIT_004 — Pole movement and closure of dimension three

Status: PROVED pole movement, exterior losses, confluent certificate and sign of every triple of powers with exponents >=32; complete independent review. Papers untouched. Review of a fixed-dimension construction; no extrapolation to arbitrary order.

## 1. Pole movement: proof from scratch

Let fhat(tau)=P(i tau)/prod_j(u_j+i tau), where P is a polynomial of degree less than n and u_j>0. This representation describes the span of n exponentials if the poles are distinct and the corresponding confluent space if they repeat. If v_j>=u_j for each j, keeping P and replacing u_j by v_j multiplies |fhat|² by

    R(tau)=prod_j (u_j²+tau²)/(v_j²+tau²).

Each factor is nondecreasing in |tau|, by direct differentiation. For the probability measure p=|fhat|²/(2pi||f||²), the new archimedean quotient is E_p[mR]/E_p[R]. Since m and R are nondecreasing functions of |tau|,

    Cov_p(m,R)=1/2 integral integral (m(t)-m(s))(R(t)-R(s)) dp(t)dp(s)>=0.

The integrals converge: the rational functions have tail O(1/tau), m=O(log(2+|tau|)) and R is bounded. Therefore the archimedean quotient does not decrease when any of the poles increases, for each fixed P. Taking the infimum over ALL polynomials P of the same allowed degree preserves this comparison. In particular, for n<=3 and all rates >=u, it suffices to control the confluent space of rates u,u,u. No pointwise comparison of matrices is used, nor is it assumed that the exponential coefficients remain fixed.

## 2. Uniform weighted norm: constant 1302

In the rational orthonormal Malmquist basis order the three rates v_j>=u. Each vector is obtained by applying j all-pass factors to sqrt(2v_j)e^(-v_j y). For the weighted norm ||e^(uy/2)f||_2, the first vector has norm <=sqrt(2), since 2v_j/(2v_j-u)<=2. The kernel of each all-pass factor is delta_0-2v e^(-vy), and after weighting its total variation norm is

    1+2v/(v-u/2)<=5.

Young for convolution and Cauchy--Schwarz on the orthonormal coefficients give

    ||e^(uy/2)f||² <=2(1+25+625)||f||²=1302||f||².

The same bound covers dimension one or two. It requires neither an upper bound nor a separation of the rates, and directly admits repeated factors. By restriction to the interval [t,infinity),

    ||f 1_[t,infinito)|| <=sqrt(1302)e^(-ut/2)||f||.

## 3. Comb and polar losses at u>=63/2

By Cauchy--Schwarz for the autocorrelation and the tail norm,

    |comb|/||f||² <=2sqrt(1302) sum_{n>=2}Lambda(n)n^(-(u+1)/2).

Since u>=31.5, the exponent is >=16 and Lambda(n)<=log n. Integral comparison of log x/x^16, decreasing for x>=2, gives

    sum log(n)n^-16 <=2^-16 log2+2^-15[(log2)/15+1/225]
                     <2^-16[1+2/15+2/225].

Using 2sqrt(1302)<74, the comb is <.002||f||², using rationals only.

For the moments A=integral f e^(y/2), B=integral f e^(-y/2),

    2AB >=-(A-B)²/2,
    integral_0^infinito 4sinh²(y/2)e^(-uy)dy=2/[u(u²-1)].

Weighted Cauchy--Schwarz implies

    polar >=-1302/[u(u²-1)]||f||²>-.042||f||²

for u>=63/2. The last comparison is rational: 1302/[u(u²-1)] at u=63/2 equals 10416/249795<21/500.

## 4. Archimedean obligation and conditional consequence

If the archimedean form on span{e^(-63y/2), y e^(-63y/2), y² e^(-63y/2)} is >=.1||f||², §1 transports it to every span of up to three exponentials with rates >=63/2. The independent bounds §§2–3 would then give

    W(f)>(.1-.042-.002)||f||²=.056||f||².

This would close the sign of all triples of powers a_i>=32, including rates arbitrarily close or widely separated. The concrete confluent bound is reviewed and approved in §5; therefore this conclusion is PROVED. The dimension-three result implies neither the sign in arbitrary dimension nor the closure of the paper.

## 5. Confluent certificate received and verified: PROVED

POWER_CONFLUENT_004.md was reviewed from the archimedean kernel and its Fraction Python block was run independently: all rational asserts pass. The coefficients are checked without inferring them from diagonals: for p(u)=[psi((u+1/2)/2)-log pi]/2, the entry between the exponential and its first Laguerre function is 2up'(u), and the entry with the second is 2u[p'(u)+up''(u)]. The equal diagonals and the repetition of the first band also result from the product of the rational all-pass bases. Thus d=psi(16)-log pi, b=(63/4)psi'(16), c=b+(3969/16)psi''(16) are correct.

The bounds gamma<H256-log256, pi<22/7, the atanh series with r=1/3 for log2 and r=15/29 for log(22/7), and the integral tails of S2/S3 are valid with the declared directions. They produce d>159/100, 0<b<51/50, |c|<1/50. The final matrix bound is strictly larger than

    159/100-(10/7)(51/50)-1/50=79/700>1/10.

By §§1–4, Q[f]>(7/125)||f||² is proved for the three exponentials with arbitrary rates >=63/2, using our losses <.002 and <.042. The conservative claim Q>=||f||²/20 of the main memo is therefore approved. Confluence and absence of minimal separation do not introduce an unjustified limit: the rational spaces and bases allow repeated poles directly.

## 6. Review of the main movement memo

POWER_POLE_MOVEMENT_004.md §§2–5: APPROVED. Its formulation for all eigenenergies, besides the minimum, follows from min–max on the same vector space of numerators P, since the Rayleigh comparison is pointwise for every P. The Rayleigh derivative keeps the normalisation term and has the correct sign. Its somewhat coarser comb bound <3/1000 is valid (74/28672<3/1000) and leads to the margin 11/200>1/20. Using it instead of the .002 bound of this audit does not affect the approval.

The construction achieves the dimension-three sign for the WHOLE range a_i>=32; it does not extrapolate to all orders. In particular it is not claimed that the weighted bound B_n=(25^n-1)/12 stays uniform nor that the confluent archimedean part keeps its margin as n grows.
