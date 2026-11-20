# Prime dilations: negative sign of the cyclotomic finite part

Status: **PROVED**, with independent review of the proof and of its scope. It does not decide the sign of the complete form.

## Cross-check

1. Antecedent: Part V of the master index, "Index-dependent cyclotomic cutoff", after 212-94. There the homogeneous finite part J_sc is obtained, its positivity at b_6 is certified and its general sign is left open. "Selection of aggregation by dilations" had remained without a rule for the crossings.
2. New object: an explicit integer test that sums prime dilations of b_6 and has negative J_sc. No table of matrices is enlarged and no other representation of the target form is sought.
3. Difference: for distinct primes larger than the support of b_6, the gcd of the dilated indices is computed exactly. This provides the dominant cross term with sign, which was missing in the previous selection. The independent gate approved investigating only this auxiliary obstruction.
4. Link with the target: it decides whether J_sc can be a PSD piece in the splitting a=J_sc+(a−J_sc). A negative value rules out that splitting into two PSD pieces, but does not rule out a≥0 nor a different joint compensation. No novelty is claimed for the elementary tools on primes or gcd.

## Definitions and statement

For finitely supported real sequences, use the symmetric bilinear form

    B(b,c)=−Σ_(i,j≥1) gcd(i,j)b_i c_j log((i+j)/gcd(i,j)),
    J_sc(b)=B(b,b).

The integer carrier K consists of the finitely supported integer sequences satisfying

    Σ_j b_j=0,    Σ_j j b_j=0,    Σ_j b_j v_r(j)=0 for each prime r.

Let b=b_6=(−1,3,−1,−2,0,1), with indices 1,...,6. For a positive integer p, D_p b places b_i at index pi and zero elsewhere. For any integer k≥4096, define

    X=2^k,    P_X={p prime: sqrt(X)<p≤X},    N=|P_X|,
    β_X=Σ_(p∈P_X) D_p b.

**Statement.** β_X is a nonzero element of K and J_sc(β_X)<0. Therefore J_sc is not PSD on the integer carrier.

## 1. Data of the test and preservation of the constraints

For b, the sum and the moment are zero. The only nonempty prime rows are

    Σ_i b_i v_2(i)=3−4+1=0,
    Σ_i b_i v_3(i)=−1+1=0.

The identity v_r(pi)=v_r(p)+v_r(i) shows that each D_p b and their sum belong to K. If p,q>6 are distinct primes and 1≤i,j≤6, pi=qj is impossible: it would force p|j. Their supports are disjoint; in particular β_X is nonzero when N>0.

By exact finite computation, already recorded for this same b,

    A=Σ_(i,j=1)^6 gcd(i,j)b_i b_j=14,
    J_sc(b)=−72log2+36log3+10log5−2log7<3.

For the last bound the integer inequality suffices

    3^36·5^10 < 2^75·7²,

which gives J_sc(b)<log8<3. The earlier interval certificate is not used. Moreover Σ_i|b_i|=8, so that

    H=Σ_(i,j=1)^6 gcd(i,j)|b_i b_j|≤6·8²=384.

Exact homogeneity gives B(D_p b,D_p b)=pJ_sc(b)<3p.

## 2. Complete crossings between distinct primes

Let p≥q>6 be distinct primes. Since neither divides the indices i,j≤6,

    gcd(pi,qj)=gcd(i,j)=g.

Hence, without omitting any crossing,

    B(D_p b,D_q b)
      =−A log p−Σ_(i,j=1)^6 g b_i b_j log((i+(q/p)j)/g).

One has 1≤(i+(q/p)j)/g≤12. Therefore

    |B(D_p b,D_q b)+14log p|≤H log12<1152.

Here log12<3, since the sum of the first four terms of exp(3) is 13. For p,q∈P_X, log p>(log X)/2. If k≥4096, log X=klog2>(2/3)k>2304, and thus

    B(D_p b,D_q b)<−(13/2)log X.                 (CROSS)

The bound is uniform over all pairs used. It does not require p/q to be bounded away from zero.

## 3. Sufficient number of primes, without an asymptotic theorem

For X=2^k, the central coefficient satisfies

    binom(X,X/2)≥2^X/(X+1).

For each prime p≤X, the factorial valuation formula expresses its valuation in that binomial as the sum of floor(X/p^a)−2floor(X/(2p^a)). Each summand is 0 or 1 and vanishes for p^a>X. Consequently,

    v_p(binom(X,X/2))log p≤log X,
    π(X)log X≥Xlog2−log(X+1).

Since π(sqrt X)≤sqrt X,

    Nlog X≥Xlog2−log(X+1)−sqrt X log X.

For k≥16, k+1≤2^k/16 and k≤2^(k/2)/16. Both are checked at k=16 and are preserved when k is incremented. Using log2<1, one obtains

    log(X+1)≤k+1≤X/16,
    sqrt X log X≤2^(k/2)k≤X/16.

The elementary bound log2>2/3 (for example, integrating the expansion of 1/(1−t²) between 0 and 1/3) implies

    Nlog X>(2/3−1/8)X>X/2,
    N>X/(2log X).                                (COUNT)

In particular N>0. The whole count is elementary and effective.

## 4. Negative sign

Expand the quadratic form, with each unordered pair twice. The diagonals and (CROSS) give

    J_sc(β_X)<3XN−(13/2)log X·N(N−1).

By (COUNT), the right-hand side is less than

    N[−X/4+(13/2)log X].

This number is negative, because 2^k>26k>26log X for k≥4096. This proves the statement on explicitly defined finite tests. There is no need to enumerate their primes or compute a matrix of growing size.

## Result

**What was proved:** the finite part J_sc of the homogeneous cyclotomic regularizer takes negative values on the integer carrier, despite the known positive value at b_6. The family β_X exactly preserves all the valuation constraints and the two moments.

**What failed and why:** subtracting the positive self-energy of the regularizer does not preserve PSD. The individual dilations scale their energy by p, while the crossings among many prime scales accumulate a negative term of order N² log X. The result excludes taking J_sc as a universal nonnegative piece in a=J_sc+(a−J_sc).

**Concrete next step:** any cyclotomic reopening must specify a joint compensation with the remainder that responds to this family of tests; the homogeneous cutoff and its positivity on one test do not suffice. No such compensation is proposed here. No negativity of a, nor sign of the remainder, nor impossibility of other regularizers, nor closure of global positivity is claimed. The falsifier battery for a positive proof of a does not apply to this refutation of an auxiliary form: that sign step has not been taken.
