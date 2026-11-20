# Forced cancellation between two already signed prime sums

In the sample C_k of 217 separate ALL primes p≤exp(k/3) from the larger ones, keeping within each group their signs and the whole oscillatory integral in u. Call the first group P_k. One has

    P_k ∼ 3^(−√k+ik) exp(k/6−ik) k^(−3/2) · H/(1/2−3i),
    H = 3 exp(−1/4)/(2√π) · ∫₀^∞ exp(−r−ir²/2)dr ≠ 0.

The equivalence is complex. Hence C_k−P_k∼−P_k, unconditionally. Indeed 217 and |γ|>14, |δ|≤1/2 give limsup log(1+|C_k|)/k≤arctan(1/28)<1/6. The margin is larger using the verified height. 211 gave cancellation of a short prime sum at fixed rate, along a subsequence. 216 gave the cost of taking moduli per prime after the integral. Here the signal survives BOTH signed sums (over primes and over rates) for EVERY sufficiently large integer. The cut k/3 is chosen so that the two phases have equal derivatives at u=3.

**Boundary coefficient.** For L=k/3+d, define I_k(L) as in 216 but with the weight u^(−√k+ik−1) of 217. Let F_k=3^(−√k+ik) exp(−ik) k^(−3/2). One has, for d in compacts,

    I_k(k/3+d)/F_k = H exp(−3id)+o(1).

Indeed, in u=3exp(r/√k), du/u=dr/√k, the remaining weight gives 3^(−√k+ik)exp(−r+i√k r). For each bounded r the cut indicator is eventually one, since log X_(k²)(u) is of order k² there. By the scaling and the profile of 211,

    k c_(k²)(L;u) = u exp(−(uL/k)²/4) cos(uL)/√π + o(1)

uniformly in compact r,d. The previous envelope k|c|≤Cu gives domination for all r≥0 by C exp(−r/2) after the change, for k≥4, even with the indicator. On the negative branch of the cosine use uL=k+√k r+r²/2+3d+o(1). After removing exp(−ik) the indicated integral remains. On the positive branch the additional oscillation exp(2i√k r) remains, multiplied by a prefactor of modulus one and a profile that converges in L¹ after extracting that phase (and the constant phase). Riemann–Lebesgue gives o(1). The errors are uniform in compact d by uniform Taylor in bounded r and the common domination. The integral factor of H differs from 1 in modulus of the difference by strictly less than ∫ exp(−r)r²/2 dr=1, since |exp(−ix)−1|<x for x>0. This proves H≠0.

**Prime sum up to the cut.** For d=log p−k/3 with fixed −D≤d≤0, PNT gives weak convergence of the measure exp(−k/3)Σ(log p)δ_d to exp(d)dd, on that compact. Multiplying by p^(−1/2) exp(k/6)=exp(−d/2) and using the uniform profile gives, after normalising P_k by F_k exp(k/6), the contribution H∫_(−D)^0 exp((1/2−3i)d)dd. For d<−D one uses |I_k(L)|≤C|F_k|, uniform in L by the envelope k|c|≤Cu and the change in r. Chebyshev and partial summation give Σ_(p≤X)(log p)/√p≤C√X. The normalised tail therefore costs O(exp(−D/2)). Letting D→∞ proves the formula without requiring an error rate in PNT.

**Consequence for the route.** Estimating these two blocks of primes separately in modulus already costs exp(k/6+o(k)); the target of 217 is exp(o(k)) along a subsequence. The main term of P_k is obtained from the continuous density, with its explicit complex phase. Subtracting it can remove that term, but the relative o(1) of PNT only gives error o(|P_k|), insufficient by itself at the required scale. Subexponential control of the joint residue has not been proved.
