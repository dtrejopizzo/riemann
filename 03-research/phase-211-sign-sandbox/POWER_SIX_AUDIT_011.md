# POWER_SIX_AUDIT_011 — Independent review of the global six-pole sign

Status: PROVED. Reviewed POWER_SIX_GLOBAL_011.md and tools/power_six_global_011_verify.py; independent run with PASS. Papers untouched.

## 1. Confluent basis and scalar constants

The diagonal and the five arch+polar Toeplitz bands use the same formulas derived and verified earlier, with psi^(j)(16) up to j5. The sums16..2000 and tails between the integrals from2001 and2000 have the correct orientation for each alternating sign; the interval arithmetic C.I keeps all endpoints. The symmetric interval elimination of AP-(3/25)I has six pivots with positive lower endpoint. The column/rowpivot factors remain intact at each update. The certificate proves the sign of the whole matrix, including cross terms.

The exact moment sums AA,BB and the comparison4AA BB<1 justify |Polar|<I. The value m0 is computed with the previously audited intervals gamma,pi,log2,logpi and its lower endpoint exceeds-5373/1000.

The sixteen-term digamma lower(x) is correct and increasing. The program's26 sites delimit exactly25 panels covering[0,49] without gaps; the jump10→12 is included as one panel. On each panel the bound b*(c-lower(a))_+<9 is valid by monotonicity and produces the GLOBAL inequality x(c-m)_+<9. Site49 verifies m>c and monotonicity extends that sign to the exterior. It is not a numerical interpolation of rates.

## 2. Deficit transport

With n6,u63/2,b3/25,C1,c1/20,X49,D9, the exact comparison of the script is

    b-c-D[(1+X/u²)^6-1]/X-6/(4u²)>3/500.

The already audited general rule implies AP[f]>(1/20)||f||² for all rates>=u. The use of the Bernoulli polar loss6/(4u²) is conservative relative to exact eta_n. The TARGET norm of f is kept in the identity, so the result remains uniform even when R0 tends to zero for large rates.

## 3. All-pass improvement and ALL contacts

The weighted Plancherel argument is valid because causal rational functions have exponential decay and sigma3u/4<min v_j. On the shifted line, the norm of each multiplier is(v+sigma)/(v-sigma)<=7. The first mode has weighted norm²<=4. Hence B6=4sum_(j0..5)49^j=(49^6-1)/12=1153440600 is correct without assuming weighted orthogonality.

The comparisons2sqrt(B6)<68000 and sigma+1/2=193/8>24 are verified. Using Lambda(q)<=logq, the log factor and the decreasing integral of(logx)x^-24 from2 are kept. Its exact formula is2^-24[log2+2log2/23+2/23²], and log2<7/10 provides the rational majorant of the script<1/250. This estimate includes the full infinite sum and does not presuppose a favourable sign of the comb.

It concludes W[f]>(1/20-1/250)||f||²=23/500||f||²>(1/25)||f||² for EVERY space of six real poles>=31.5, with multiplicities allowed and with no upper bound or minimal separation. The argument covers arbitrary real numerators of degree<6; mixtures of up to six exterior powers are subcases. The passage to seven or arbitrary dimension requires new verified hypotheses and is not included in this approval.
