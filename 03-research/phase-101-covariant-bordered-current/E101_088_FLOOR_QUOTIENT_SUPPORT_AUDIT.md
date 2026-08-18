# E101.088 - Floor-quotient support audit of a claimed PNT mean square

## 1. Decision

The preprint

```text
H.-C. Wu,
Proof of the Riemann Hypothesis via the Chebyshev Function and the
Integral Convergence, version 2:
  https://www.preprints.org/manuscript/202605.1525             (1.1)
```

does not prove its asserted estimate

```text
integral_2^X [Psi_Cheb(t)-t]^2dt=O(X^2 log^2 X).               (1.2)
```

The first fatal error is the lower bound in its Lemma 9.  A positive average
indexed by the attained quotients `floor(N/k)` is replaced by a sum over
every integer `m<=N`, including quotient classes which are empty.  The missing
support is exactly where an RH-strength second moment enters the argument.

The valid consequence of the preceding estimates controls only
`O(sqrt N)` distinct floor quotients.  Forcing a dense initial interval by a
larger choice of `N` returns a trivial-scale estimate.  Therefore the paper
does not close `LOG-GAUSSIAN-L2-CANCELLATION`, E101.087 or Omega7.

This audit is included because (1.2), if true unconditionally, would imply
the live target immediately.  It may not be cited as recent progress toward
that target.

## 2. Exact notation in the claimed proof

Let

```text
a_n=Lambda(n)-1,                                             (2.1)

A(x)=sum_(n<=x)a_n
    =Psi_Cheb(x)-floor(x)
    =Psi_Cheb(x)-x+{x}.                                      (2.2)
```

Thus, for an integer `n`,

```text
A(n)=Psi_Cheb(n)-n.                                          (2.3)
```

The hyperbolic average used in the preprint is

```text
U(N)=sum_(k=1)^N k A(N/k)^2.                                 (2.4)
```

Its established elementary estimate is

```text
U(N)=O(N^2 log N),

U(N)/N=O(N log N).                                           (2.5)
```

For `m>=1`, define the quotient class

```text
J_m
 ={k in {1,...,N}: floor(N/k)=m}

 ={k in N: N/(m+1)<k<=N/m},                                 (2.6)
```

and its normalized weight

```text
W_(m,N)=sum_(k in J_m) k/N.                                  (2.7)
```

These definitions determine exactly which `m` can occur.

## 3. The expansion has no approximation error

If `k in J_m`, then the integers counted by `A(N/k)` are precisely
`1,...,m`.  Hence

```text
A(N/k)=A(floor(N/k))=A(m)                                   (3.1)
```

exactly.  The auxiliary error introduced in the preprint's expansion is
identically zero.  Grouping (2.4) by quotient classes gives the exact identity

```text
U(N)/N
 =sum_(m=1)^N A(m)^2W_(m,N).                                 (3.2)
```

An empty `J_m` contributes zero.  That qualification cannot be removed.

## 4. Fatal failure of the weight lower bound

The preprint asserts

```text
W_(m,N)>=1/(2m)                                              (4.1)
```

for every `m>=1` and `N>=2`.  The proof chooses the least member of `J_m`
without establishing that `J_m` is nonempty.

Take

```text
N=10,
m=4.                                                         (4.2)
```

Then

```text
J_4=(10/5,10/4] intersect N
   =(2,2.5] intersect N
   =emptyset.                                                 (4.3)
```

Consequently,

```text
W_(4,10)=0<1/8.                                              (4.4)
```

This is not an endpoint convention or an asymptotic loss.  It invalidates
(4.1) on the majority of the proposed support.

## 5. The actual floor-quotient support

Define

```text
Q_N={floor(N/k):1<=k<=N}
   ={m<=N:J_m is nonempty}.                                  (5.1)
```

Only for `m in Q_N` does the least element used in the argument exist.  In
that case, if `k_min=min J_m`, then

```text
W_(m,N)>=k_min/N>N/[N(m+1)]=1/(m+1)>=1/(2m).                 (5.2)
```

Thus the valid lower bound is

```text
1/2 sum_(m in Q_N) A(m)^2/m
 <=sum_(m in Q_N)A(m)^2W_(m,N)
 =U(N)/N.                                                     (5.3)
```

Using (2.5), one obtains only

```text
sum_(m in Q_N)A(m)^2/m=O(N log N).                           (5.4)
```

### Proposition 5.1 - The attained support is sparse

```text
|Q_N|<=2floor(sqrt N).                                       (5.5)
```

### Proof

For `k<=sqrt N` there are at most `floor(sqrt N)` values of
`floor(N/k)`.  For `k>sqrt N`, every value satisfies
`floor(N/k)<sqrt N`, so there are at most another `floor(sqrt N)` values.
Their union is `Q_N`. `QED`

The average (2.4) therefore controls a sparse hyperbola, not all integers up
to `N`.

## 6. Dense recovery loses the entire claimed gain

One can force an initial interval into the quotient support, but only by
making `N` quadratic.  Let

```text
N=M(M+1).                                                     (6.1)
```

For every `m<=M`, the interval

```text
(N/(m+1),N/m]                                                (6.2)
```

has length

```text
N/[m(m+1)]>=1.                                               (6.3)
```

It therefore contains an integer, and

```text
{1,...,M} subset Q_N.                                        (6.4)
```

Applying (5.4) with (6.1) gives

```text
sum_(m<=M)A(m)^2/m=O(M^2 log M).                             (6.5)
```

Chebyshev's elementary estimate `A(m)=O(m)` already gives

```text
sum_(m<=M)A(m)^2/m=O(sum_(m<=M)m)=O(M^2).                    (6.6)
```

Thus the dense consequence of the hyperbolic average is weaker than the
trivial bound.  No mean-square improvement survives.

## 7. Where the downstream proof collapses

The false lower bound (4.1) is used to claim

```text
U(N)/N
 >=1/2 sum_(m=1)^N A(m)^2/m+O(N log^2 N),                    (7.1)
```

and then

```text
sum_(m=1)^N A(m)^2/m=O(N log^2 N).                           (7.2)
```

The exact integral on a unit interval is

```text
integral_n^(n+1)[Psi_Cheb(t)-t]^2dt
 =A(n)^2-A(n)+1/3.                                           (7.3)
```

Indeed, away from the right endpoint `Psi_Cheb(t)=Psi_Cheb(n)`, so
`Psi_Cheb(t)-t=A(n)-(t-n)` and direct integration gives (7.3).

Summing (7.3) yields, up to the terminal interval,

```text
integral_2^X[Psi_Cheb(t)-t]^2dt
 =sum_(n<=X)A(n)^2-sum_(n<=X)A(n)+O(X).                      (7.4)
```

The proposed estimate then uses

```text
sum_(n<=N)A(n)^2
 <=N sum_(n<=N)A(n)^2/n
 =O(N^2 log^2 N).                                            (7.5)
```

But (7.2), the only input to (7.5), depends on the false completion
`Q_N -> {1,...,N}`.  The valid estimate (5.4) cannot be inserted in (7.5),
because it omits all `n` outside `Q_N`.  Equations (7.1), (7.2), (7.5) and the
claimed second moment (1.2) therefore fail together.

## 8. Exact relation to the live Omega7 target

Suppose, contrary to the audit, that (1.2) had been proved.  Dyadic
decomposition would give, for every `epsilon>0`,

```text
integral_1^infinity
 |Psi_Cheb(x)-x|^2x^(-2-epsilon)dx<infinity.                  (8.1)
```

To see this, on `[2^j,2^(j+1)]` use (1.2) and
`x^(-2-epsilon)<=2^(-j(2+epsilon))`.  The resulting series is bounded by

```text
sum_(j>=1)j^2 2^(-epsilon j)<infinity.                        (8.2)
```

In logarithmic coordinates, (8.1) is

```text
integral_0^infinity exp(-epsilon u)
 |exp(-u/2)[Psi_Cheb(exp u)-exp u]|^2du<infinity.             (8.3)
```

E101.087 proves that Gaussian convolution of the differentiated centered
error in (8.3) gives `LOG-GAUSSIAN-L2-CANCELLATION`.  Hence (1.2) would close
Omega7 precisely because it already has RH strength.

The conservation-of-difficulty location is now explicit:

```text
actual positive support Q_N
        --false completion--> all m<=N
        --second moment-----> RH-sized logarithmic L2.        (8.4)
```

The false completion, not a subtle limiting theorem, inserts the missing
force.

## 9. Independent defects

The support error is already fatal.  Three further issues prevent the
auxiliary arguments from repairing it.

### 9.1 Dyadic endpoint

With `L=floor(log_2 N)`, the manuscript uses

```text
min(N,2^L)=N.                                                 (9.1)
```

In fact `2^L<=N<2^(L+1)`, so the minimum is `2^L`.  For `N=10`, the stated
decomposition stops at `8` and omits `9,10`.  This can be repaired with a
correct terminal interval, but it does not restore Lemma 9.

### 9.2 Impossible subsequence thinning

The appendix states that an arbitrary sequence `x_n->infinity` may be
thinned, after relabelling, so that

```text
x_n<=n^2.                                                     (9.2)
```

This is false.  For example, every subsequence of `x_n=exp(n)` has its
relabeled `n`-th member at least `exp(n)`, which exceeds `n^2` eventually.

### 9.3 Continuation versus convergence

Analytic continuation of the meromorphic expression corresponding to a
Dirichlet integral does not imply convergence of the original integral in
the continued region.  The Hardy boundary-limit distinction in E101.087
Section 9.2 applies verbatim.  Treating continuation as convergence deletes
the poles or growing modes which the integral is meant to detect.

## 10. General support-completeness no-go

The reusable conclusion is:

```text
Let Q be the support attained by a positive grouped average.
A lower weight proved only on Q controls only coefficients on Q.
Replacing Q by a larger index set requires an independent completion
theorem.  Positivity cannot fill the missing indices.                    (10.1)
```

For floor quotients, `|Q_N|=O(sqrt N)`, so the completion cost is quadratic.
Any future hyperbola, divisor-switching or finite-section proposal must state
its attained support before applying a positive lower bound.

## 11. Status

```text
verified:
  exact floor-class expansion of U(N);
  explicit counterexample to the claimed weight bound;
  sparse-support estimate |Q_N|=O(sqrt N);
  strongest dense consequence is trivial-scale;
  the asserted mean square would imply the live Omega7 target;

rejected:
  unconditional estimate (1.2) from the cited preprint;
  completion of Q_N to every m<=N;
  use of analytic continuation as integral convergence;

retained as a stop rule:
  positive averages control only their attained support;

not claimed:
  any defect in the classical RH equivalences cited by the preprint;
  any progress from that preprint toward RH or Omega7.
```
