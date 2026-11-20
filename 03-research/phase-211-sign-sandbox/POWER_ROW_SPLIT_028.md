# POWER_ROW_SPLIT_028 — Separating the polar edge k=0 from the orbit k>=1

Status: PROVED the whole row N5 with uniform margin in k and u, rational certificate executed. Independent review APPROVED in POWER_ROWS_AUDIT_028.md; the verifier was reproduced PASS. No campaign. Papers untouched.

## Corpus and new reason before building

Read the project rules, INTERIOR017 (WRN), the full rows N1–3 of018, LOW_TABLE018, ARCH_CELL026 and the current statuses; searches in index/grid/crossword (covariance/first differences/polar/edge). The archimedean monotonicity and the WRN bound are already proved and are not presented as novelties.

The difference here is a NEW separation of obligations: ARCH positive at k=0 is not required. There the positive polar is kept, dividing u into two intervals via monotonicities of components; from k=1 the covariance gain is used and only the small odd polar is controlled. The aim is to close the WHOLE row N5 with these few analytic endpoints, not to certify a list of k.

## 1. Infinite result

For N=5, ALL integers k>=0 and ALL rates u>=63/2, let f_(5,k,u) have transform

    F(s)=s^k/(s+u)^(5+k).

Then

    W[f]>(1/25)||f||².                                  (ROW5)

For all k>=1 the stronger bound W[f]>(4/5)||f||² holds. The case k=0 is covered by keeping its positive polar; in fact ARCH_50(63/2)<−1/10, so the previous argument «ARCH positive from k0» does not work for this row.

## 2. Two monotonicities covering infinite parameters

Write A_(N,k)(u)=Arch[f]/||f||². The spectral probability is proportional to tau^(2k)/(u²+tau²)^(N+k). For fixed u, passing from k to k+1 multiplies that probability by Z=tau²/(u²+tau²), normalizing. Since m(tau) and Z increase in |tau|,

    A_(N,k+1)(u)−A_(N,k)(u)=Cov(m,Z)/E Z>0.

On the other hand, tau/u has a law independent of u. Since m increases in |tau|, A_(N,k)(u) increases with u. Thus for k>=1,u>=u0=63/2,

    A_(5,k)(u)>=A_(5,1)(u0).

No monotonicity of the FULL form nor of AP is claimed; the polar will be treated separately.

## 3. Exact archimedean constants, only at the necessary endpoints

The rational orthonormal Laguerre basis of rate u has archimedean Toeplitz bands

    r_0=psi((u+1/2)/2)−logpi,
    r_l=(1/2)Σ(j=1..l)binom(l−1,j−1)u^j
                             psi^(j)((u+1/2)/2)/j!.

If z=(s−u)/(s+u), the transform of f_(N,k,u) has in that basis the coefficients of the polynomial (1−z)^(N−1)(1+z)^k, up to a common factor that cancels in Rayleigh. For N5,

    k0: v0=(1,−4,6,−4,1), ||v0||²=70,
    k1: v1=(1,−3,2,2,−3,1), ||v1||²=28.

The attached rational verifier encloses the derivatives of psi via positive sums of256 terms plus integral tails; the values psi16 and psi(127/4) are obtained by recurrence from the quarter values and rationally enclosed constants. It evaluates ONLY the endpoints used by the monotonicities and proves

    −13/100 <A_(5,0)(63/2)<−1/10,
    A_(5,1)(63/2)>9/10,
    A_(5,0)(63)>1/2.                                    (ARCH)

There is no list of k nor an interpolation from points. The two u are the endpoints of the intervals of the next section.

## 4. Exact polar and separation of k0

Let a=u²−1/4. The normalized polar has sign (−1)^k and magnitude

    p_(N,k)(u)= (4pi/u)(u²/a)^N
                      (4u²−1)^(-k)/B(k+1/2,N−1/2).

In particular

    p_(N,0)(u)=4^N/[u binom(2N−2,N−1)]·(u²/a)^N,
    p_(N,1)=p_(N,0)N/(2a),
    p_(N,k+1)/p_(N,k)=(k+N)/[(k+1/2)(4u²−1)].

For N5, p_(5,0)(u) decreases with u, and the rational certificate gives p_(5,0)(63)>23/100. On u∈[63/2,63], ARCH and polar are then bounded by OPPOSITE endpoints:

    AP_(5,0)(u)>−13/100+23/100=1/10.

For u>=63, ARCH>1/2 and the polar remains positive. This division does not use an unproved AP monotonicity.

For k>=1, the successive quotient of the polar magnitudes is <=4/(4u0²−1)<1. Moreover p_(5,1)(u) decreases with u and p_(5,1)(u0)<1/500. Hence the odd polar of any k>=1 is >−1/500; for even k its favourable sign is kept.

## 5. The whole comb, uniformly in k and u

The WRN theorem audited in INTERIOR017 gives, with eta12,

    ||e^(12y)f_(5,k,u)||²/||f_(5,k,u)||²<=R5(u,12),
    R5(u,12)=[u/(u−12)]^9 S5([12/(u−12)]²),
    S5(r)=[1+4r−2r²+(4/5)r³−(1/7)r⁴]/(1−r)^5.

The function S5 is increasing in r because its original series has coefficients B_l^(5)>0; that monotonicity is not inferred from the mixed signs of the closed numerator. All the factors of R5 decrease with u. For u0=63/2, r=64/169 and the certificate proves

    R5(u,12)<=R5(u0,12)<2500.

Shifted Cauchy–Schwarz and Lambda(q)<=q give for ALL contacts

    |Comb[f]|/||f||²
      <100Σ(q>=2)q^-11
      <=100·2^-11(1+2/10)<3/50.                         (PRIME)

q^-11.5 was replaced by q^-11 for simplicity. The full infinite sum converges and is controlled without assuming a favourable sign for any contact.

## 6. Closing the WHOLE row

At k0,u∈[63/2,63], §§4–5 prove W/norm²>1/10−3/50=1/25. At k0,u>=63 they prove W/norm²>1/2−3/50>1/25. For ALL k>=1,u>=63/2, §§2–5 give

    W/norm²>9/10−3/50−1/500>4/5.

ROW5 is proved with margin independent of the two parameters. The script `tools/power_row_split_028_verify.py` when run gives PASS on all the necessary rational comparisons.

## 7. Reusable analytic pattern, without extrapolating rows

For a given N, the same argument works if one has U>=u0, a uniform WRN cost L_N, bounds b0<=A_(N,0)(u0), bU<=A_(N,0)(U), b1<=A_(N,1)(u0), and an odd control p1 with successive polar quotients<1, such that

    min(b0+p_(N,0)(U),bU)>L_N,
    b1>L_N+p1.

This is a sufficient criterion for the INFINITE row, not a claim that the premises hold for all N. The exact identity

    A_(N,1)=A_(N,0)+u ∂_u A_(N,0)

explains why starting at k1 can be substantially better than requiring ARCH0>0. It is derived from the beta integrals and the resolvent recurrence, not from a numerical fit; for fixed N and large u the gain tends to1. That limit is not used as a bound uniform in N.

The closure of rowN5 enlarges the sufficient sign table. It does not by itself cover all rows nor new windows T; the interior regions of growing N keep their obligation of an additional arithmetic inequality.
