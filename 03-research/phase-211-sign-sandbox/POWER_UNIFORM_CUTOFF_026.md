# POWER_UNIFORM_CUTOFF_026 — Analytic cutoff in N for the tail of the compensated kernel

Status: PROVED two analytic cutoffs uniform in N and full control of the tail of K and of its cells. Independent review approved in POWER_ARCH_CELL_AUDIT_026.md; verifier reproduced: PASS. No row-by-row certificates. Papers untouched.

## Corpus and new reason before building

Read the project rules, INVERSE_KERNEL020, CUMULATIVE_INVERSE022, CELL_TEST024 and the log-concave lemma 025; searches in index/grid/crossword (Riccati/Bessel/coefficients/log-concavity/cutoff). The signs of h and K already have interior falsifiers. The difference here is to replace the cutoff certified for a single N by a FORMULA in N, using coefficient ratios and the differential equation of the same gamma kernel. No points are collected and positivity is not extrapolated from one row to others.

## 1. Uniform result

Fix u=63/2 and d=N−1. For N>=3 define

    t_J(d)=d(d+220)/(330d+6300),
    M_d=u²/(2d−1), Q_d=sqrt(9/4+M_d),
    t_R(d)=2d Q_d/(u²−Q_d²),
    t_*(N)=min(t_J(d),t_R(d)).

The denominators are positive. For N=2 set t_*(2)=1/30−1/693. Then

    D_N'(t)/D_N(t)<=30 for ALL t>=t_*(N),             (LOG)
    K_N(x)>=x^-32D_N(logx)/4>0
                       for ALL x>=exp(t_*(N)).       (TAIL)

Here D_N=33P_N−P_N' and K_N is the COMPLETE Möbius sum, not an approximate polynomial or a prefix. In particular t_J(d)<d/30 for all d>1 and both cutoffs are d/330+O(1): the exponent of the exterior cutoff improves from scale d/30 to d/330.

One also obtains without a sweep over N the uniform range

    K_N(x)>0 for ALL 2<=N<=129, x>=exp(2/3).           (RANGE)

No sign of K in the interior region is proved, nor positivity of W for all those N.

## 2. Rational cutoff via Jensen on the coefficients

Use the positive coefficients of P_N=Σp_jt^j. Those of D_N are

    D_j=p_j(3d+30j)/(2d−j)>0.

For d>1, their differentiation ratios satisfy, j=0..d−1,

    r_j=(j+1)D_(j+1)/D_j
       =63(d−j)/(2d−j−1)·(1+10/(d+10j)); r_d=0.

The function f(z)=(d−z)/(2d−z−1) is decreasing and concave on [0,d]. If L=D_N'(t)/D_N(t), the probability with weights D_jt^j/D_N(t) has index mean tL. Thus

    L=E r_j<=63(1+10/d)E f(j)
              <=63(1+10/d)f(tL).                       (JEN)

One has tL<d because all coefficients are positive. At t=t_J one checks exactly

    30=63(1+10/d)f(30t_J),
    30t_J<d,

since the difference after multiplying by the positive denominator is −3d−660+990t+18900t/d. If L>30, f(tL)<f(30t_J), contradicting JEN. For t>=t_J, if 30t>=d it is immediate that L<d/t<=30; if 30t<d the same comparison applies by monotonicity of f. This proves LOG with t_J for ALL N>=3 without checking each row.

The inequality t_J<d/30 is equivalent to d>1. Its asymptotic expansion has leading term d/330. The log-concavity of D from 025 is compatible with this proof, but there is no need to invoke it to interpolate rows.

## 3. Riccati cutoff via the gamma autocorrelation

Write rho_N(t)=e^-ut P_N(t)>0 and q(t)=−rho_N'(t)/rho_N(t)>0 for t>0. Positivity follows from the gamma heat representation of 018. The recurrence of p_j proves the differential equation

    rho_N''−(2d/t)rho_N'−u²rho_N=0,
    q'=q²+(2d/t)q−u².                                 (RIC)

Since P_N has degree d and positive leading coefficient,

    q(t)=u−d/t+O(t^-2),
    q'(t)=d/t²+O(t^-3)>0 for large t.

A global curvature bound can be proved WITHOUT citing a special Bessel inequality:

    0<q'(t)<M_d=u²/(2d−1), t>0.                       (CURV)

Indeed, differentiating RIC, if q'=0 one gets q''=−2dq/t²<0. Any passage from nonpositive values to the final positive values would require an upward crossing, impossible with that derivative. If q'=M_d, RIC gives 2dq/t=2dM_d−q², and hence q''=2qM_d+q²/t>0. Any value above M_d would have to come back down because q'->0, but every crossing of the level M_d has positive derivative. Exact contacts are also excluded by the same argument. Thus CURV holds for all t>0, not only near the origin.

The lower part of CURV and RIC give

    q(t)>sqrt[(d/t)²+u²]−d/t.                           (ROOT)

On the other hand D_N=e^ut rho_N(3/2+q), hence

    D_N'/D_N=u−q+q'/(3/2+q)
             <u−q+M_d/(3/2+q).

The last side is <=u−3/2=30 if q>=Q_d=sqrt(9/4+M_d). For d>=2, Q_d<u. The right side of ROOT reaches Q_d exactly at t_R=2dQ_d/(u²−Q_d²). Therefore LOG holds with t_R for all N>=3. Its leading term is 3d/(u²−9/4)=d/330.

For N=2, D_N(t)=3/2+(2079/2)t; its log-derivative is <=30 when t>=1/30−1/693, giving the separate case without using a nonpositive denominator of t_R.

## 4. A whole range of N without individual certificates

The Riccati cutoff allows recovering and analytically extending the site 2/3 that 025 certified only for N=129. With x=2d−1,

    t_R=(2/3)(x+1)sqrt[x(x+441)]/(440x−441).

Twice its logarithmic derivative has the sign of the polynomial

    T(x)=880x³+192276x²−778365x−194481.

The expansion T(5+y)=830594+1210395y+205476y²+880y³ has all coefficients positive. Therefore t_R increases for d>=3. The comparison t_R(128)<2/3 reduces to the rational inequality

    9·128² Q_128² <(u²−Q_128²)².

For d=2 the same rational comparison is checked; for d=1 the previous linear cutoff is used. These are TWO comparisons at the endpoints of a monotone formula, not a campaign of certificates for 129 rows. This proves LOG for all 2<=N<=129, t>=2/3 and by §5 proves RANGE.

## 5. The complete Möbius tail and the remaining cells

The exact formula is

    K_N(x)=x^-32Σ(m>=1)mu(m)m^-32D_N(logx+logm).

If logx>=t_*(N), integrating LOG gives D_N(logx+logm)<=m^30D_N(logx). By |mu|<=1 and Σ(m>=2)m^-2<=3/4,

    |K_N(x)/(x^-32D_N(logx))−1|<=3/4,

which proves TAIL with the WHOLE sum. No tail of unknown sign is subtracted without controlling it.

Set X_N=exp(t_*(N)). The identity (J_N/x)'=−K_N/x² and J_N/x->0 give, for x>=X_N,

    J_N(x)=x∫_x^infinity K_N(t)t^-2dt
      >=(x/4)∫_x^infinity t^-34D_N(logt)dt>0.           (JTAIL)

For any cell [n−1,n] with n−1>=X_N, monotonicity of J_N/x implies

    S_N(n)=H_(n−1)∫_(n−1)^nJ_N−logn J_N(n)
      >=[H_(n−1)(1−1/(2n))−logn]J_N(n)
      >=(3/4−log2)J_N(n)>0.                           (CELLTAIL)

The two harmonic bounds used, already proved in the cellular criterion, are H_(n−1)−logn>=1−log2 and H_(n−1)/(2n)<=1/4. JTAIL even allows replacing J_N(n) by an explicit positive gamma integral. Thus the part of ERR=−2ΣS_N(n) formed by those cells is favorable, with a complete quantitative bound.

The number of interior cells still needing control is bounded by ceil(X_N). In terms of the exponent, it goes from the previous cutoff of order exp(d/30) to exp(d/330+O(1)). It still grows with N; the interior problem has not been eliminated.

## 6. Scope

An ANALYTIC cutoff was obtained for all N, and a range 2..129 with positive tail from a single site. No new matrix or polynomial certificate per N is required. For N=129, combined with the already audited S129(2)>33/100, CELLTAIL again gives complete ERR129<−33/50; that case was already proved by 025 and is not counted as new W coverage.

For other N the interior averages are still missing. No isolated tail bound proves the sign of W or all the blocks. The new formulas serve to locate and quantitatively reduce the remaining obligation, keeping the signed arithmetic and all contacts.
