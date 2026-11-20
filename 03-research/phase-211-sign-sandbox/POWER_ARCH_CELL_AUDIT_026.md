# POWER ARCH CELL AUDIT 026

Status: ARCH_CELL026 and UNIFORM_CUTOFF026 APPROVED. Papers untouched.

Antecedents reviewed: CELL_BALANCE024 and its audit, CELL_TEST024, INVERSE_LOGCONCAVITY025 and its audit. The specific log-concavity already allows a full cutoff and ERR129<−.66; it is not by itself a sign of W. The new quantitative obligation is to keep ARCH_sharp in the real balance, or to extend the cutoff with a uniform theorem in the parameters. An insufficient lower bound is not W negative. A grouping identity without an additional inequality does not complete that balance.

## ARCH_CELL026 — APPROVED

Reviewed `POWER_ARCH_CELL_026.md` and `tools/power_arch_cell_026_verify.py`; independent run PASS. The recurrence ψ(5/4+iτ/2)=ψ(1/4+iτ/2)+1/(1/4+iτ/2) incorporates exactly the sharp polar symbol. For g129, the variance V=u²/[4(2N−3)] and the three shifts up to 17/4 are correct; Euler/Jensen give ARCH_sharp<−.81. Therefore the comparator ARCH_sharp+.66 is negative by more than .15. This shows the insufficiency of that ERR guarantee, not W<0.

The identity w(x)=ΣJ(nx) follows from μ*1 with absolute summation. Substituting J=x∫K/t² gives the weights D=T(t)/t² and E_x=T(t/x)/t² and the factor x^(3/2) in rho. The representation of ψ produces k(x)=x^−7/2/(1−x^−2), with the declared factor 2. Thus JOINT preserves all normalisations and jumps.

The grouped interchange is valid: near x1, the smooth part of T(t)−x^(3/2)T(t/x) is O(x−1) in norm integrated against |K|/t²; the step crossings n≤t<nx also add up to O(x−1) by the decay and smooth boundedness of K. This cancels the singularity of k. At infinity the majorant is integrable. The logarithmic singularities at integer t have measure zero and are locally integrable; the two divergent terms of the bracket are not separated.

On 1<t<2, I′=−1/(t²−1) and the difference of ψ values give the formula FIRST. The rational evaluator certifies Omega(3/2)<−.1. Universal pointwise positivity of this joint weight is refuted. Choosing an arbitrary K as if it came from a gamma autocorrelation is not allowed: the compact-support example would violate rho≤1. No sign of W and no impossibility of other groupings is inferred.


## UNIFORM_CUTOFF026 — APPROVED

Reviewed `POWER_UNIFORM_CUTOFF_026.md` and `tools/power_uniform_cutoff_026_verify.py`; independent run PASS. The Jensen cutoff is valid for d≥2: f(j)=(d−j)/(2d−j−1) is decreasing and concave, r_j≤63(1+10/d)f(j), and the mean of the index is tL<d. The comparison with L30 gives exactly t_J=d(d+220)/(330d+6300). The case 30t≥d is also treated, without leaving the domain of f.

The differential equation for rho and the Riccati equation for q are correct. q>0 comes from the heat kernel; the polynomial expansion at infinity gives q′=d/t²+O(t^−3)>0. At the level q′0, q″<0 prevents returning to positive values; at the level q′M_d, q″=2qM_d+q²/t>0 prevents returning from above to the limit 0. These barriers also exclude contacts and give 0<q′<M_d for all t>0. The inequality to be proved is not presupposed.

From Riccati one obtains the lower bound for q. The identity D′/D=u−q+q′/(3/2+q), the threshold Q²=9/4+M_d and the resolution t_R=2dQ/(u²−Q²) are correct. For d≥2 the denominator is positive. The case d1 is correctly separated with the affine polynomial and its threshold 1/30−1/693. Thus both cutoffs are uniform theorems, not extrapolations between pointwise certificates.

The expression of t_R in x=2d−1 and the polynomial for the sign of its derivative have positive denominators. The expansion in x=5+y is positive; the two rational comparisons d2, d128 and the affine case prove the range 2≤N≤129. The script only verifies these constants; the analytic argument provides the uniformity.

Integrating the log-derivative bound controls the FULL Möbius sum by Σm^−2≤3/4, and hence K>0 on the whole declared tail. The representation of J gives the positive lower gamma integral; LOCAL gives CELLTAIL. The reduction of the number of interior cells is correct and does not supply their sign. Order 129 reproduces ERR025, without counting it as new coverage.

## Scope closure

The round adds two uniform cutoffs and an exact joint kernel that remains signed. The insufficient comparator ARCH+.66 and Omega(3/2)<0 are not W<0. The positive tails do not prove the remaining interior averages nor the sign of all orders. There is no newly certified window T and no modification of papers.
