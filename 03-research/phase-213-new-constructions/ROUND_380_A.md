# Balance of the sector with exactly two large primes

**Status: PROVED, with independent review of both PNT substitutions and of the signed Taylor sum.**

With the definitions of 379 and a fixed in (0,1), let S_d be the balance with exactly d primes greater than y=exp(b), b=L^a. Then

    S_2 ∼ J x P(0) log(L/b)/L,     S_2/|S_1| ∼ log(L/b),
    P(t)=∏_{z<p≤y}(1−p^(−1+t)),   z=L².

Hence the sector d=2 exceeds that of d=1 by a divergent factor. The set d≥3 compensates d=2 to first order, by 377 and 379. The sum of d=1,2 still has a positive balance of exponent one.

**Semiprime density.** Write n=mpq and count p,q>y in order with factor 1/2. The diagonals cost O(Y/y) at Y=x/m since g(log(Y/p²))≪Y/p². As in 379, discarding m>exp(L/4) costs O(x exp(−L/(4b)+O(log L))) using that distinct semiprimes have a unique unordered representation. For m≤exp(L/4), restrict p,q to [y,exp(2L)]: every omitted product exceeds exp(2L), with Gaussian cost O(Y exp(−cL²)) when counting over integers. Replacing both prime measures by dt/log t gives error O(Y L² exp(−c√b)). Indeed, with one factor r fixed, integrate by parts using |π(t)−li(t)|≪t exp(−c√b) on that interval. Boundaries and the derivative integral cost O((Y/r)exp(−c√b)), since exp(−u)g(u) is bounded and ∫exp(−u)|g'(u)|du is finite. The reciprocal mass of the other factor costs O(L) both for primes and for the continuous density. The sum over m amplifies these errors by a power of L.

In the variables log p,log q, with D their sum, the continuous density stripped of exp(D) is

    H(D)=(1/2)∫_b^(D−b) dv/[v(D−v)]=log((D−b)/b)/D,     D>2b.

The upper endpoints exp(2L) are inactive on |u|=|log Y−D|≤√L. The tails of the continuous integral are O(Y exp(−cL)) using the majorant H(D)≪1 for D>2b. What remains is x times the sum with weight μ(m)/m of the integral of exp(−u)g(u) H(L−log m−u).

**Signed summation of an analytic density.** On the complex disc |D−L|≤L/2 the real branch of H extends and |H|≪H(L) by its formula. On log m≤L/4, |u|≤√L, Taylor up to degree N−1 has remainder O_N(H(L)(|log m+u|/L)^N). In absolute value Σ_m (1/m) exp((log m)/b)≤exp(O(log log y))≤L^C with C absolute, by the finite product and p^(1/b)≤e. Hence a remainder cost O_N(H(L)L^C(b/L)^N) after integrating the Gaussian. Choose N fixed according to a so that it is o(H(L)P(0)), since P(0)≫L^(−1). In each polynomial term extending to all m and u costs an error smaller than any negative power of L by Rankin with margin 1/(2b) and by the Gaussian.

The signed moments of log m are the derivatives of P at zero. On |t|≤1/b one has |P(t)|≪P(0) by integrating the logarithmic derivative O(b) as in 379, valid also on the complex disc. Cauchy gives |P^(i)(0)|≪_i P(0)b^i. Hence the Taylor terms of order i≥1 give O_i(H(L)P(0)(b/L)^i), while the constant one is J H(L)P(0). This proves the equivalent. The computation preserves the cofactor cancellations before comparing the two sectors.

**Review record.** Each prime replacement has error O((Y/r)exp(−c sqrt b)); the other factor only introduces its reciprocal mass, so the two substitutions can be performed sequentially, one against the prime measure and the other against the continuous one. Their boundaries satisfy the same bound by sup exp(−u)g(u)<∞. The diagonal and repeated products have ordered coefficient at most1, and their cost O(Y/y) is negligible after summing cofactors. On the disc |D−L|≤L/2, D and D−b stay away from0, which fixes a holomorphic branch of the formula for H and justifies Cauchy. For the moments of (log m+u)^i the binomial is expanded and both the derivatives of P and the fixed Gaussian moments are used; the signed derivatives are not replaced by absolute moments. N is fixed once a<1 is fixed and absorbs the factor L^C because (b/L)^N=L^(−N(1−a)). The extension of each moment outside log m≤L/4 has error exp(−cL/b+O_N(log L)), even with the factors (log m)^i, by Rankin with margin1/(2b). All these bounds are uniform in the cofactors, without claiming uniformity for a→1.
