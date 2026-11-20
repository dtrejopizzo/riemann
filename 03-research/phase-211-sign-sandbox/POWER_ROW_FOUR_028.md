# POWER_ROW_FOUR_028 — Full fourth row of the scalar table

Status: **PROVED**, independent review approved and verifier PASS reproduced. For ALL k>=0 and ALL u>=63/2,

    W[f_(4,k)]>(1/50)||f_(4,k)||²,
    F_(4,k)(s)=s^k/(s+u)^(4+k).                           (ROW4)

The WHOLE comb and the polar are kept. Papers untouched. No extrapolation to other rows or to the global sign.

## 1. Corpus and new reason

Read the project rules, INTERIOR017 (WRN), TABLE_DESCENT018 (rows2/3), their audits and STATE027; consulted the routes index, master grid and CROSSWORD-TO-D.md on rows, gamma derivatives and weights. The prohibition018 on replacing a universal proof by a campaign of rows is kept: this row is the concrete authorized target028 and is not presented as closure. Recurrences alone give no sign, as the falsifier018 proves.

The mathematical difference from018 is to keep the EXACT formula of ARCH4, whose margin turns out small but positive, and to use the rational weight eta12 in WR4 instead of fixing eta15. It is not a sweep nor a search for another N: a gamma formula and an analytic choice of the weight produce a uniform bound of the REAL form for all k and u. The alternating sign of the polar is kept; the positive polar of even k is not subtracted.

## 2. Legitimate archimedean monotonicities and exact formula

Let m(tau)=Re psi(1/4+i tau/2)−logpi. By the series of psi, m increases with |tau|. For fixed N, normalizing the density tau^(2k)/(u²+tau²)^(N+k) and rescaling tau=u xi gives a probability in xi independent of u. Hence ARCH_(N,k)/norm² increases with u by pointwise comparison of m(u xi).

When k increases, the probability is reweighted by xi²/(1+xi²), increasing in |xi|. The covariance with m(u xi) is nonnegative. Thus for all u>=u0=63/2 and k>=0,

    ARCH_(4,k)(u)/norm²>=ARCH_(4,0)(u0)/norm².             (MON)

This only uses ARCH, not pole motion of the full form nor the global lemma refuted in007.

Set d(u)=psi((u+1/2)/2)−logpi. The Poisson integral gives I1=d(u)/(2u), and the exact recurrence I_(r+1)=−I_r'/[2ur] for the denominator (u²+tau²)^r allows computing

    ARCH_(4,0)/norm²=d−u d'+(2u²/5)d''−(u³/15)d'''.       (A4)

The base norm is5/(32u^7). At u0, the argument of psi is16. Using psi^(r)(16) through its ABSOLUTE series,

    A4(u0)=H15−gamma−logpi−(u0/2)S2−(u0²/5)S3−(u0³/20)S4,
    Sp=sum_(j=16)^infty j^(−p).

All the Sp are subtracted. By elementary monotonicity,

    Sp<=sum_(j=16)^115 j^(−p)+115^(1−p)/(p−1).

The Fraction verifier and the explicit intervals003 of gamma/logpi prove

    A4(u0)>11/400.                                       (ARCH)

The endpoint115 is a cut of the three special-function series with integral remainder, not a sample of parameters k or u. MON extends ARCH to ALL declared parameters without computing another matrix or another atom.

## 3. Weight eta12 and FULL comb

The lemma WRN017, valid for eta<u/2, proves for all k the bound

    ||e^(eta y)f_(4,k)||²/||f_(4,k)||²<=R4(u,eta),
    R4=(u/(u−eta))^7 S4(rho), rho=(eta/(u−eta))²,
    S4(rho)=(1+3rho−rho²+rho³/5)/(1−rho)^4.

The expression is obtained from the differential product017; equivalently,

    S4(rho)=sum_(l>=0)[(2l+1)(2l+3)(2l+5)/15]rho^l.

This last series has positive coefficients, so S4 increases with rho. For fixed eta12, u/(u−eta) and rho decrease with u. Thus R4(u,12)<=R4(u0,12)<400, an exact rational comparison with rho=64/169 and u0/(u0−12)=21/13.

By weighted Cauchy–Schwarz,

    |c_f(t)|<=sqrt(R4)e^(−12t)||f||².

The WHOLE comb contribution is controlled by

    |PRIME|/norm²<40sum_(q>=2)Lambda(q)q^(−25/2).

Using Lambda(q)<=logq and q^(−1/2)<=2^(−1/2)<5/7 allows comparison with a single decreasing integral:

    |PRIME|/norm²
      <(200/7)2^(−12)[log2+2log2/11+2/121]
      <3/500.                                           (PRIME)

The last comparison uses log2<7/10 and Fraction. Λ is not truncated nor are adverse contacts discarded. The inequality f'(q)<0 for f(q)=q^(−12)logq,q>=2 already follows from log2>2/3.

## 4. Alternating polar, uniform in ALL k

Write c_k=binom(2k,k)/4^k. The beta integral gives

    norm_(4,k)²=[5/(32u^7)] c_k/binom(k+3,3),
    POLAR_(4,k)=2(−1/4)^k/(u²−1/4)^(4+k).

Set q_u=1/(4u²−1) and p_40(u)=64u^7/[5(u²−1/4)^4]. Then

    |POLAR|/norm²=p_40(u) q_u^k binom(k+3,3)/c_k
                 <=p_40(u)(8q_u)^k.                      (P)

Indeed c_k>=2^(−k) by Vandermonde and binom(k+3,3)<=4^k by counting the histograms of words of length k in four letters. Both p_40(u) and q_u decrease with u>1/2: the logarithmic derivative of p_40 has numerator−u²−7/4<0.

For EVEN k, the polar is positive and causes no loss. For ODD k>=1,8q_(u0)<1 and the verifier proves

    |POLAR|/norm²<=p_40(u0)8q_(u0)<1/1000.                (POLAR)

This bound does not subtract the polar of k0 nor replace it by its maximum over all k, which would be too large.

## 5. Full form and new region

For all declared k and u, combining ARCH, PRIME and POLAR,

    W[f_(4,k)]/norm²
      >11/400−3/500−1/1000
      =41/2000>1/50.

Thus ROW4 is proved with uniform margin and with ALL the terms of the explicit form. The result covers an additional full row; it is not a formal consequence of the other rows nor of the filter identities. Nor does it close the table of ALL N,k required by SCALAR_BRIDGE017. No new windowT is claimed from this isolated result.

By the full recurrence018, in particular the THIRD difference of row1 is strictly positive for all k, with the corresponding factor u^6. More precisely, if a_(N,k)=W[f_(N,k)],

    (−Delta)^3 a_(1,k)=u^6 a_(4,k)
      >3c_k/[160u(k+1)(k+2)(k+3)].

Complete monotonicity of arbitrary order is not claimed.

Reproduction:

    python3 03-research/phase-211-sign-sandbox/tools/power_row_four_028_verify.py

The script runs only Fraction comparisons and intervals of elementary constants; PASS. Uniformity in k and u belongs to the proofs MON/WRN/P, not to a numerical sweep.
