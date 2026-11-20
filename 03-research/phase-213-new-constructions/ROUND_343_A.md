# The residue of large quotients in an isolated rectangle still detects RH

Use Y=√X and I_Y=(21Y/20,22Y/20] as in 340. In the first rectangle I_Y² and in the second I_(Y/2)² remove all pairs (d,e) with height max(d,e)/(d,e)≤R, using the **same R**. Let V(Y,R) be the sum of μ(d)μ(e) over the remaining pairs of the first rectangle. For each δ=1/j, j≥16, take R=X^(1/6+δ/3). Then RH is equivalent to

    |V(Y,R)−2V(Y/2,R)| ≪_(δ,ε) Y^(1+δ+ε)     for each ε>0 and all large Y.

This is only the zero-frequency measurement of the two-scale block (divided by h∫η). For each product the integral of the pulse is complete in the window of the corresponding rectangle.

**Computation.** Put u(Y)=(Σ_{d∈I_Y}μ(d))². At fixed quotient r/s, d=gr,e=gs, the admissible interval J of g in the first rectangle is divided exactly by two in the second. By 341, the difference of their counts weighted by μ(r)μ(s) costs O(τ(rs)√(Y/max(r,s))) because the density cancels. Without k or local weight, summing over v=max(r,s) as in 342 gives

    V(Y,R)−2V(Y/2,R) = u(Y)−2u(Y/2) + O(Y^(1/2) R^(3/2) X^o(1)).

With the chosen R the error is Y^(1+δ+o(1)). Under RH, 340 gives u(Y)≪_ε Y^(1+ε), which proves the announced ceiling. Conversely one obtains |u(Y)−2u(Y/2)|≪Y^(1+δ+ε). Iterate down to bounded Y/2^l: the errors sum a progression of ratio 2^(−δ−ε) and the initial term costs O(Y). Thus u(Y)≪Y^(1+δ+ε). The telescoping in ratio 21/22 of 340, followed by j→∞, gives RH. When iterating the inequality **for u** is used, which no longer depends on R; residues computed with different cuts are never identified.

**Second-moment version.** If only heights up to R=X^(1/8) are removed, the second-moment criterion for the isolated residue of the two scales is also equivalent to RH. Indeed, by the proof of 342 applied to the two rectangles, with k=1, the difference of the removed pulses costs pointwise O(X^(1/4+3/16+o(1)))=o(√(Xh)) for δ≤1/16. Under RH, both complete rectangles satisfy the bound of 340 (the width at Y/2 only changes by a constant factor relative to its natural width; the Plancherel proof admits that factor). Conversely, reinserting the error and testing against the constant function gives the same inequality for u as above. The larger cut of the scalar version is not claimed for this second moment.

**Implication for the plan.** The pointwise result of 342 removes components of the total observable. Applying that pruning and then trying to estimate autonomously the remaining rectangle of 340 still imposes the Mertens criterion, even if only control of its integral is demanded. Joint control of rectangles preserves a possibility of cancellation that this separate estimate loses.
