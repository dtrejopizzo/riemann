# A single isolated subblock with the true signs already demands RH

For each large real Y take X=Y², I=(21Y/20,22Y/20], h=X^(−δ), and form

    B_I(x)=Σ_{d,e∈I} μ(d)μ(e) η(log(x/(de))/h).

In the reduction 338 if both copies are restricted to I only this pulse remains. The following statement **is equivalent to RH**: for δ=1/j, j≥5, and each ε>0,

    ∫_[X,2X] |B_I(x)|² dx/x ≪_(δ,ε) h X^(1+ε)     for all large X.

**Why the isolated block already suffices.** All pulses are entirely in the window, as in 339. For each fixed real t the integral against (x/X)^(−it) is exactly h hatη(ht) [Σ_I μ(n)(n/Y)^(−it)]². Since hatη(0)≠0, Cauchy–Schwarz under the proposed bound implies

    |Σ_I μ(n)n^(−it)| ≪ Y^((1+δ)/2+ε).

In particular t=0 suffices. For each large Z take Y=20Z/22; thus the sum between 21Z/22 and Z is controlled. Telescoping in ratio 21/22, with real endpoints and half-open convention, gives the same bound for Σ_{n≤Z}μ(n). Taking j arbitrarily large and then choosing ε proves the Mertens bound O_ν(Z^(1/2+ν)) for each ν>0. By partial summation 1/ζ extends without poles to Re s>1/2. The same reasoning with a single fixed nonzero t controls the summands μ(n)n^(−it) and extends 1/ζ(s+it) to that half-plane.

**Direction under RH.** Let D_I(t)=Σ_I μ(n)(n/Y)^(−it). For every ν>0, RH gives |D_I(t)|≪_ν Y^(1/2+ν) uniformly for |t|≤Y⁴. In detail, for each endpoint use the half-integer v=⌊endpoint⌋+1/2 and truncated Perron for 1/ζ(s+it), at abscissa 1+1/log Y and height U=Y^10. With coefficients of modulus ≤1 the error is O(Y log Y/U) by separation of v from the integers (on [v/2,2v] sum the inverses of the distances and outside use absolute convergence). Move to Re s=1/2+ν/3. Under RH the bound of 326 gives O((2+U+|t|)^γ) for any γ>0 in that strip; the vertical side costs O(Y^(1/2+ν/3)(2U)^γ log U), and the horizontal ones O(Y(2U)^γ/U). Choose γ small enough. Subtract the two prefixes and multiply by Y^(it).

Plancherel in log x gives exactly h²/(2π) times the integral of |hatη(ht)|²|D_I(t)|⁴ over the whole line. On |t|≤Y⁴ the previous bound and the norm of hatη give O(hY^(2+4ν)). Elsewhere use |D_I|≪Y and the decay of any order of hatη (hY⁴≥Y³ for these δ). Choose ν depending on ε.

**Decision for the method.** Trying to prove the sufficient norm in 338 separately on each rectangle of indices would demand, already on this concrete rectangle, a result equivalent to RH. The argument uses the exact signs and a single frequency in the hard direction, unlike the artificial counterexample 339. It does not establish that the different components of the full block must cancel; it shows the logical cost of discarding that possibility. It is an application of the classical Mertens criterion, not an independent closing mechanism.
