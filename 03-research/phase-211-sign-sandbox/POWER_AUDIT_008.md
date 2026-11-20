# POWER_AUDIT_008 — Audit of the opposite pattern of low contacts

Status: PROVED, independent review of POWER_PRIME_PATTERN_FALSIFIER_008.md. Papers untouched.

## 1. Vector and exact moments

For n131072 and u63/2, g=y^(n-1)e^(-uy) has g(0)=g'(0)=0 and the decay required to integrate by parts twice. Thus f=(D²-1/4)g has Laplace transform (n-1)!(s²-1/4)/(s+u)^n, with no boundary terms or additional distributions. The two moments are exactly zero. The degree 2 of the numerator is less than n and the vector belongs to the declared confluent space.

The spectral density is the base rational Student density multiplied by (tau²+1/4)^2, not by a factor of uncertain sign. The beta formula gives M2=u²/(2n-3), M4=3u^4/[(2n-3)(2n-5)], M6=15u^6/[(2n-3)(2n-5)(2n-7)]. Since u²<1024 and each denominator is larger than n, their bounds via 128 are correct. The denominator of the reweighting is >=1/16, so

    E_f tau²<=16M6+8M4+M2
               <15/131072+192/131072+1024/131072
               =1231/131072<1/100.

No asymptotic approximation or factorisation of gigantic factorials is used.

## 2. Deficit of the form without comb

The series for m and the bound on denominators produce m(tau)-m(0)<17tau², because sum a_k^-3<=64+104/125 and a quarter of this bound is less than 17. The identity for psi1/4 gives m(0)=-gamma-pi/2-3log2-logpi<-4; the proposed elementary inequalities even give <-9/2. Therefore ARCH/||f||²<-383/100, and the zero polar term keeps that negativity for ARCH+POLAR.

## 3. Contacts and tail obligation

For a real vector, Parseval and the parity of its spectral density identify c_f(t)/||f||² with the average of cos(tau t). The inequality cos x>=1-x²/2 gives c_f(t)/||f||²>1-t²/200. Since logq<=10log2<10 for q<=1024, all those autocorrelations are larger than 1/2. Each nonzero prime-power contact of that segment therefore contributes strictly negative sign; integers with Lambda0 do not contribute.

The TAIL inequality of the memo follows exactly from W>=0, AP<-383/100 and the strict bound of the low contacts: the tail would have to exceed 383/100+sum_(2<=q<=1024)Lambda(q)q^-1/2. It is asserted only as a necessary obligation, not as an estimate already proved. The absolute convergence of the comb is justified by the autocorrelation being exponential times polynomial and the rate 31.5.

## 4. Approved scope

The test shows within the same family that the repair pattern by low contacts of WITNESS006 is not universal. It does not prove negativity of W, does not contradict the complete certificate V12 and is not a new general theorem of negativity of subcombs. The tail above 1024 remains without evaluated sign. The label PROVED is appropriate exactly for the vector, zero polar term, AP deficit and effect of each declared contact.
