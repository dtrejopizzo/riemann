# The pending criterion as a finite alternating sum

Antecedents: 047 leaves an improper integral and a short sum. The parity weight already appears among the residue combinations in phase 188, L2_BUILD_030 §3, and in phase 211, CORRECTION_RESIDUE_BALANCE_031. Here the physical cutoff is made to coincide at two scales to cancel the integral, and the one-sided bound is recovered by iteration towards larger scales.

With V,g,χ from 047 define A(x)=x∫V−Σ_n Λ(n)V(n/x) and β(y)=[1−χ(log y)]log y. For x=j⁴ choose K as in 047, for example K=C₀(log x)² with the first construction. Global positivity is equivalent to the existence of C such that eventually

    Σ_{k<2eK} (−1)^(k+1) β(k/(2K)) g(k/(2x)) ≤ C√x.

The refined cutoff of 047 with its corresponding weight also works. Each g(t)=Σ_{m≤16e/t}μ(m)V(mt) is a finite sum.

**Cancellation.** Apply 047 with cutoff K at x and cutoff 2K at 2x. The second cutoff also gives error O(√x) by the order-q estimate of 047, increasing the initial constant of K if necessary. For the lower function F(u)=g(u/x)β(u/K), that of the second scale is F(u/2). Its integral is exactly twice the first. Thus 2A(x)−A(2x) is, up to a two-sided O(√x), the sum over all k of F(k/2) minus twice the sum over the even indices of F(k/2). The alternating expression of the statement results.

**Recovery.** Under the sign |A(x)|≤C√x by 047. In the converse direction write D(r)=exp(−r/2)A(exp r); the normalised difference is 2D(r)−√2 D(r+log 2). By 047 its second derivative is O(exp(r/2)), so an upper bound at the samples j⁴ extends to all large x by interpolation with error O(1). Then A(x)≤A(2x)/2+C√x/2. By the prime number theorem A(y)=o(y), using partial summation with the fixed weight V. Iterating, 2^(−N)A(2^N x) tends to zero and the sum of errors is bounded by C√x/[2(1−1/√2)]. Apply 047.

**Where cancellation is needed.** Expanding g, the coefficient of V(n/(2x)) is Σ_{k|n, k<2eK}(−1)^(k+1)β(k/(2K))μ(n/k). For each prime n inside the band and sufficiently large x, only k=1 contributes and the coefficient equals log(2K). On a fixed subinterval of the interior where V≥η>0, these terms alone sum to ≫ x log(2K)/log x by PNT, larger than √x. This rules out estimating the sum by its positive part term by term after grouping by n. The compensation with the composites remains open. It is not a counterexample to the criterion.
