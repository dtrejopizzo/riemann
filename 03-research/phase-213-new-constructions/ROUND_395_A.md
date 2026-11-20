# Exact threshold of absolute mass to second order

**Status: PROVED, with independent review of the phase loss, the short intervals and the optimization ofβ.**

Let A(Y)=Σ g(log(x/n)) over squarefree products of primes in (z,Y], z=L², b=log z. For Y=(4+κ/b)z, with fixed real κ, under RH,

    log(A(Y)/|S|)=[κ/4−2(1+log 2)log 4+o(1)] L/b².

Thus, for κ strictly greater than the constant of 394 there is enough mass at each scale, by a factor tending to infinity. The sign of the products remains decisive. The equivalent for A that we use is unconditional.

**Saddle of the positive product.** Set H(s)=Ls+(s−1/2)²/2+Σ_{z<p≤Y}log(1+p^(−s)). The real root β of H'=0 satisfies β=1/2+(log 2+o(1))/b by PNT on the interval and strict convexity. Indeed Σ log p/(1+p^s)∼2(√4−1)e^(−c)L for s=1/2+c/b. In a neighborhood of radius O(1/b) of β one has H''≍Lb and |H'''|≪Lb² (also on the vertical for the third derivative), by the series of the factors and log p∼b. One obtains

    A(Y)∼exp(H(β))/sqrt(2πH''(β)).

To verify it, invert the finite product directly at β. For a_p=p^(−β), the loss log(1+a_p)−log|1+a_p exp(−it log p)| is ≥c a_p(1−cos(t log p)), by the square of the modulus. On |t|≤1/(2b) this gives loss ≫Lb t². On 1/(2b)≤|t|≤2√L apply the estimate by prime subintervals of 367 to [2z,3z], where a_p≍1/L. In the variable log p, a subset of total length ≫1 has 1−cos(t log p)≫min(t²,1); it can be selected in intervals of length ≫1/(1+|t|). In p those pieces have length ≫z^(3/4), sufficient for the short PNT used in 367. One obtains loss ≫L/b³. For |t|>2√L the bound by the positive product itself at β and the Gaussian tail suffice. Finally t=w/√H'' gives the equivalent by Taylor and Gaussian domination, since Lb²/(Lb)^(3/2)→0. The argument uses Fourier phase only to count A at the same scale, without changing the sign of the coefficients of A.

**Cost of optimizing the saddle.** Let α be the exact saddle of 394. One has H'(α)=O(L/b). To see it, compare the sums log p·p^(−α) on (z,Y] and up to z: the higher powers of both products cost O(b²), and for the first powers the PNT gives the integrals of t^(−α)dt with error o(L/b). When scaling by 4, the multiplier is 4^(1−α)=2+O(1/b); moving Y by O(z/b) contributes O(L/b). Using the exact equation of α gives the estimate. Convexity and H''≍Lb between α and β imply |β−α|≪1/b² and H(β)=H(α)+O(L/b³). This error disappears at the scale L/b².

In H(α) replacing the logarithms by the first powers costs O(b²), both for the positive product and for the inverse one up to z of 368: α≥1/2 eventually and Σ_{n≤Y}1/n=O(b). The prefactors of both saddles cost O(log L) in logarithm. Hence the logarithmic difference is precisely I(Y)−2I(z)+o(L/b²) of 394, this time in both directions. At the exact critical value of κ the equivalent does not decide.

**Review record.** The interval[2z,3z] is contained in(z,Y] for every fixedκ and large x. On the frequency range |t|≤2sqrt L, the pieces of favorable phase have length in p at least c z^(3/4); if one is too long for the cited short-PNT statement it is subdivided, keeping the phase floor. Lengths remain between a power greater than17/30 and one less than1, within the range of corollary1.3 of Guth–Maynard used in367. Their total weighted mass is≳L/b and the worst factor min(t²,1) is≳1/b², giving the loss L/b³. Near0 the floor Lb t² allows Gaussian domination without auxiliary zeta constants; outside2sqrt L one uses directly |∏(1+p^(−β−it))|≤∏(1+p^(−β)). Thus the equivalent forA is unconditional.

The saddles α,β both already lie at1/2+(log2+o(1))/b, so H''≍Lb on the whole segment joining them. The error H'(α)=O(L/b) gives by the mean value theorem |β−α|=O(b^(−2)); integrating the derivative again gives |H(β)−H(α)|=O(L/b³), although H(β)≤H(α) by convexity. This cost is of lower order than the term L/b² compared in394. The result above the critical constant asserts that the total massA exceeds |S|; it does not prove that a signed terminal weight realizingS exists nor determine its sign. No uniformity in growingκ is claimed.
