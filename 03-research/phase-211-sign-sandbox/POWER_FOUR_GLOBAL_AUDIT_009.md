# POWER_FOUR_GLOBAL_AUDIT_009 — Review of the deficit transport and closure for four arbitrary poles

Status: PROVED. Verifier tools/power_four_global_009_verify.py executed with PASS. The four-pole theorem is reviewed, not the sign at all orders. Papers untouched.

## 1. Exact identification of functions and terms

Fix u=63/2, D0(s)=(s+u)^4. For real poles v_j>=u and any real polynomial P of degree<4, compare fhat0=P(i tau)/D0(i tau) with fhatv=P(i tau)/prod(v_j+i tau). They are identical numerator spaces; repeated ones are admitted from the start. Define

    R=prod_j(u²+tau²)/(v_j²+tau²),
    R0=prod_j u²/v_j²,
    r0=prod_j(u²-1/4)/(v_j²-1/4).

If N0=||f0||² and Pv0=2A(f0)B(f0), then Nv=integral R|fhat0|²/(2pi) and the new polar is r0 Pv0. For any real c,

    APv-cNv =R0(AP0-cN0)
       +integral (R-R0)(m-c)|fhat0|²/(2pi)
       +(r0-R0)Pv0.                                   (ID)

The identity keeps all normalizations. It does not claim that APv/Nv is greater than AP0/N0; it is transport of a deficit inequality and does not contradict the monotonicity falsifiers.

## 2. Spectral filters and polar

Each factor satisfies R>=R0 and

    R/R0<= (1+tau²/u²)^4,
    r0/R0=prod_j (1-1/(4u²))/(1-1/(4v_j²))
            >=(1-1/(4u²))^4>=1-1/u².

Also r0<=R0. The signs of each comparison are verified directly from v_j>=u>1/2. The norm of the polar in the confluent basis is controlled via the two moment vectors: if AA=||A||²,BB=||B||², |2A(f)B(f)|<=2sqrt(AA BB)||f||². The script certifies 4AA BB<1 exactly, with its two rational progressions, so |Pv0|<N0. Thus the last term of ID is greater than -R0 N0/u² independently of the sign of the polar.

## 3. Audit of the five scalar comparisons

The code was executed and the constants verified from their series:

* Three terms of the atanh series for log2 give log2>693/1000. Then gamma<H32-log32<H32-5(693/1000)<3/5.
* The first term2/3 and the geometric remainder bounded by1/36 give log2<25/36<7/10.
* The positive sum up to degree6 of exp(23/20) exceeds22/7; together with pi<22/7 it gives logpi<23/20. Hence gamma+pi/2+3log2+logpi<11/2, and m(0)>-11/2.

With x=tau², the first sixteen positive digamma summands produce the lower(x) of the script. Its formula x/[a(4a²+x)] has the correct factor4. The five lower bounds at4,16,32,64,81 are rational and their asserts pass. Since m increases in x, the panels [0,4],[4,16],[16,32],[32,64],[64,81] certify

    x(1/10-m(sqrt(x)))_+ <23.

The last site81 has m>.1, so the negative part vanishes for x>=81. No numerical sweep is used nor interpolation without monotonicity.

For 0<=x<=81, the quotient [(1+x/u²)^4-1]/x is increasing by its positive polynomial expansion. Thus

    0<=R-R0<=R0 Kx,
    K=[(1+81/u²)^4-1]/81.

The integral loss of ID is greater than -23KR0 N0.

## 4. Complete final margin, including all contacts

The previously audited confluent certificate gives AP0>(49/200)N0. Inserting c1/10 in ID and using §§2–3 leaves

    APv-(1/10)Nv
       >R0[49/200-1/10-23K-1/u²]N0.

The bracket is exactly3669270349/93389776200>3/100. Hence APv>(1/10)Nv for EVERY numerator and EVERY quadruple of rates>=u, without separation or upper bound. This comparison uses an absolute deficit bound limited to low frequencies, not monotonicity of the AP quotient.

The already audited uniform Young/all-pass bound B4=32552 holds for those arbitrary poles and gives |Comb|<(13/1000)Nv. The sum of all contacts converges absolutely for these rational functions. Consequently

    W[fv]>(1/10-13/1000)Nv>(2/25)Nv.

This proves positivity with uniform margin on ALL spaces of four real poles>=63/2, including repeated poles and the corresponding polynomials times exponentials. Mixtures of up to four powers with exponents>=32 are subcases via the diagonal identification with zeta(a). The result is not inferred for five poles nor for any dimension.

The complete final memo POWER_FOUR_GLOBAL_009.md was received and read afterwards: APPROVED in full. The explicit sum759/140 and the five bounds112/5,344/15,112/5,112/5,81/50 coincide with the comparisons of the verifier. The small factor R0 is correctly treated because the target norm Nv already figures in ID. No hidden restriction of separation, upper bounding of rates or individual positivity of the comb was found.
