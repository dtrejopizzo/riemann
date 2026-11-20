# What prime size would suffice and what size is unavoidable

**Status: PROVED, with independent review of the constant4, the unconditional consequence and the exponent barrier.**

Let p_*(x) be the smallest terminal prime admitting the exact representation of 392, including the terminal weights 0 and 1. It is eventually finite by 392. There are two bounds of different nature:

* If p_*(x)≤(log x)^(2+o(1)) eventually, then RH.
* Under RH, liminf p_*(x)/(log x)²≥4.

In particular, claiming a uniform localization p_*≤(4−δ)(log x)² with fixed δ>0 would be contradictory: it would imply RH by the first statement and then violate the second. The result does not ensure existence when reaching the constant 4.

**Majorant that does not need to know the weight.** For a terminal cut Y, any terminal weight between zero and one, and real σ in a fixed compact set, the mass in absolute value is ≤ C x^σ ∏_{z<q≤Y}(1+q^(−σ)), since g(u)≤C exp(σu). It is a majorant over the integers, different from taking absolute values on the contour of 388. If Y≤L^(A+o(1)), A≥2 fixed and L=log x, choose 1−1/A<σ<1. The logarithm of the product is O(Y^(1−σ))=o(L), by summing even over integers. At the minimal cut the complete pulse then has upper exponent ≤1−1/A by letting σ decrease. For A=2, 372 excludes any exterior zero. More generally, if Θ>1/2, 372 implies limsup log(p_*)/log L≥1/(1−Θ), interpreted as infinity for Θ=1: every A strictly less than that barrier gives a contradiction with the exponent Θ (for A<2, p_*≥z suffices).

**Constant at the square-root end.** Fix 1<K<4 and Y=Kz, z=L², b=log z. Allow all primes of (z,Y] in the majorant. For σ=1/2+c/b with c constant,

    Σ_{z<q≤Kz} q^(−σ)=(2(√K−1)e^(−c)+o(1)) L/b.

This follows by partial summation of the PNT on [z,Kz], using q^(−c/b)=e^(−c)(1+o(1)) uniformly. Hence the logarithm of the bound for any terminal product in that interval is at most

    L/2 + [c+2(√K−1)e^(−c)+o(1)]L/b.

Minimizing in c gives c=log(2(√K−1)) and coefficient 1+log(2(√K−1)). By 368 and the calibration of the saddle under RH, the logarithm of |S| is L/2+[1+log 2+o(1)]L/b. The Gaussian term and the saddle prefactor cost o(L/b) in logarithm. For K<4 the first coefficient is strictly smaller, so no weight in [0,1] nor cut ≤Kz can reproduce S eventually under RH. Take K↑4.

**Review record.** The bound by absolute values also holds for the terminal weights0 and1, since all coefficients of the product have modulus≤1 and it is dominated by allowing all primes up toY. For each fixed A and each σ>1−1/A, the exponent A(1−σ)<1 absorbs the o(1) in Y≤L^(A+o(1)); letting σ decrease afterwards justifies the exponent ceiling1−1/A. If the limsup of the exponent of p_* were less than1/(1−Θ), one would choose a fixed A strictly in between and contradict372. For Θ=1 every finite A is ruled out in this way.

In the computation of the constant, the optimal parameter c=log(2(sqrt K−1)) may be negative: this is allowed, since σ=1/2+c/b stays in a fixed compact set and the Gaussian bound g(u)≤C exp(σu) does not require σ≥1/2. The PNT error on[z,Kz] is uniform for that fixed c and the logarithm of the Gaussian constant is O(1)=o(L/b). The exact contrast of coefficients is log(sqrt K−1)<0 for K<4. This proves the liminf≥4 only underRH. The impossibility of an eventual ceiling(4−δ)L² is unconditional by combining the two implications; it is not converted without hypothesis into a pointwise floor nor into a liminf≥4. The equality withS and the restriction of the weight to[0,1] are essential for this argument.

The remaining opportunity is to find a terminal cut of exponent 2+o(1). The scale x^o(1) obtained in 392 is much larger in general. The necessary threshold 4 refers to exact equality with S under RH, not to the sign of an isolated summand.
