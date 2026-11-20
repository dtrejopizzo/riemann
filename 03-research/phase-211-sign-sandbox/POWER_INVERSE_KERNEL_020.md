# POWER_INVERSE_KERNEL_020 — Positivity of the COMPLETE inverse outside an explicit interval

Status: PROVED positivity of the complete inverse in an explicit region for ALL N; PROVED global positivity of the inverse for N=2. Independent review approved in POWER_BALANCE_AUDIT_020.md; the proof and the certificate were also checked separately. The sign of ERR for all N is not proved. No numerical tables. Papers untouched.

## Antecedents and new reason, before the construction

Read: the project rules, SIGNED_MEAN019 and its audit, LOW_TABLE018, TATE_CHAIN009; targeted searches in the ROUTES-TRIED-INDEX index, grid part3 and CROSSWORD-TO-D (Möbius/kernel/inversion/positivity/polynomials). The inversion identities and their Euler/Möbius limitations are already recorded and are not relaunched as a sign proof.

The new difference is to exploit POSITIVE coefficients of a specific polynomial of the gamma kernel to dominate the COMPLETE Möbius TAIL in a range of x that depends explicitly on N. The sign of the inverse is not inferred from a prefix. A case in which the complete inverse is positive for all x is also sought.

## 1. Theorems on the COMPLETE inverse

Keep u=63/2 and the kernels of019,

    H_N(x)=−[x^-1/2 C_N(logx)]'/C_N(0)>0,
    h_N(x)=Σ(m>=1)mu(m)m H_N(mx), x>=1.

For all N>=2 we prove

    H_N(x)/4 <=h_N(x)<=7H_N(x)/4
       if logx>=(N−1)/30.                              (OUTER)

The series of h_N is the COMPLETE one. As a consequence, its whole negative part is contained in1<=x<exp((N−1)/30).

Moreover, for N=2, positivity is proved on the WHOLE half-line:

    h_2(x)>=H_2(x)/[2zeta(32)]>H_2(x)/4>0, x>=1.       (ROW2)

OUTER does not declare the sign of h_N on the complement. ROW2 is not extrapolated to other N.

## 2. Gamma polynomial with all coefficients positive

Write rho_N(t)=C_N(t)/C_N(0)=e^-ut P_N(t), t>=0. The gamma integral of the autocorrelation gives

    P_N(t)=Σ(j=0..N−1)p_j t^j,
    p_j=binom(N−1,j)(2u)^j Gamma(2N−1−j)/Gamma(2N−1)>0.

Set d=N−1, s=u+1/2=32. Then

    H_N(x)=x^-33 A_N(logx),
    A_N(t)=sP_N(t)−P_N'(t).

For0<=j<d,

    (j+1)p_(j+1)/p_j=2u(N−1−j)/(2N−2−j)<=u.

Thus each coefficient of A_N is >=(s−u)p_j=p_j/2>0; the last one is sp_d>0. Its degree is exactly d. For N>=2, p_0=1,p_1=u, so A_N(0)=1/2. The derivation does not rely on numerical signs of a large polynomial.

## 3. Domination of the WHOLE Möbius sum

If A is a polynomial of degree d with nonnegative coefficients and t>0,l>=0,

    A(t+l)/A(t)<=(1+l/t)^d<=exp(dl/t).

It is applied term by term to the monomials; no monotonicity of the derivatives of an inverse is assumed. The complete series is written

    h_N(x)/H_N(x)
       =1+Σ(m>=2)mu(m)m^-32
                     A_N(logx+logm)/A_N(logx).

For logx>=d/30, the polynomial quotient is <=m^30. Since |mu(m)|<=1,

    |h_N(x)/H_N(x)−1|
       <=Σ(m>=2)m^-2
       <=1/4+∫_2^infinito t^-2dt=3/4.

This proves OUTER and controls the COMPLETE tail before extracting the sign. The sign of no Möbius prefix is used. More generally, if q=32−d/logx>1, the same proof gives

    |h_N/H_N−1|<=2^-q[1+2/(q−1)].                      (RANGE)

The choice q>=2 produces the simple threshold of OUTER.

## 4. Global structure and the case N=2

Expanding the finite polynomial A_N inside the absolutely convergent series, h_N(x)=x^-33 tildeA_N(logx), where tildeA_N is a polynomial of degree d. Its leading coefficient is that of A_N divided by zeta(32), strictly positive, since Σmu(m)m^-32=1/zeta(32). In particular h_N has at most d positive roots in the coordinate logx; OUTER moreover gives an explicit uniform location of all possible negative regions.

For N=2, P_2(t)=1+ut and

    A_2(t)=1/2+1008t.

With M(s)=1/zeta(s), D(s)=Σ(q>=2)Lambda(q)q^-s, one has M'=DM. Thus the COMPLETE sum is evaluated exactly:

    h_2(x)=x^-33/zeta(32)
                 [1/2+1008logx−1008D(32)].             (H2)

The elementary bound Lambda(q)<=q and integral comparison give

    0<D(32)<=Σ(q>=2)q^-31
         <=2^-31(1+2/30),
    1008·2^-31(1+2/30)<1/4.

By H2, h_2(x)>x^-33[1/4+1008logx]/zeta(32)>=H_2(x)/[2zeta(32)]. Finally zeta(32)<2, by the same bound for positive series. ROW2 is proved without discarding terms of the sum.

The existence of negative prefixes for large N in019 is compatible with ROW2 and OUTER: they are statements about different N and regions. It has not been proved here that the complete h_N is negative at any point.

## 5. Localized negative part and favorable tail of the pairing

Let X_N=exp((N−1)/30), and B(x) the negative grouping of019. There it was proved that B(x)<=−a0(x−1), a0=1−log2>0, and F_N=2∫h_N B. By OUTER,

    F_N <=2∫_1^X_N h_N(x)B(x)dx
                −(a0/2)∫_X_N^infinito H_N(x)(x−1)dx.   (LOCAL)

The tail of LOCAL is favorable and explicit. Writing w_N(x)=x^-1/2 C_N(logx), integration by parts gives

    ∫_X^infinito H_N(x)(x−1)dx
       =[(X−1)w_N(X)+∫_X^infinito w_N(x)dx]/C_N(0).

The remaining integrals are incomplete gammas of a known polynomial times exponential, with no arithmetic sum. The adverse term h_N^- paired with −B is rigorously restricted to the finite interval[1,X_N]. This is NOT yet a bound that compensates it: the one-sided estimate of that interior pairing remains.

## 6. Result and scope

The sign of the COMPLETE inverse kernel was established on an explicit infinite region for all N, and on the whole half-line for N=2. Positivity of h_N for all x and all N is not deduced, nor the sign of ERR for the complete row. ROW2 contributes a property of the kernel; even F_N<=0 would not automatically compensate the deficit of Arch_sharp. The missing contribution is localized by LOCAL and must preserve its arithmetic sign.
