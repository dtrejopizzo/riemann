# 107.203 -- Canonical finite order-change renormalization has no critical cofinal limit

## 1. Exact finite-support counterterm

Let \(S\) be a finite set of primes and let

\[
 D_{S,s}=\bigoplus_{p\in S}D_{p,s}
\]

be the balanced operator of 107_199.  The order-change identity is

\[
 \boxed{
 \det{}_2(1-D_{S,s})
 =
 \det{}_5(1-D_{S,s})
 \exp\left(
 -\frac12\mathrm{Tr}\,D_{S,s}^2
 -\frac14\mathrm{Tr}\,D_{S,s}^4
 \right).
 }
 \tag{1.1}
\]

Indeed each prime block contributes

\[
 \frac12\mathrm{Tr}\,D_{p,s}^2=p^{-s},
 \qquad
 \frac14\mathrm{Tr}\,D_{p,s}^4=\frac12p^{-2s},
\]

which cancels exactly the order-five counterterm of 107_201.  Therefore

\[
 \det{}_2(1-D_{S,s})=\prod_{p\in S}(1-p^{-s}).
 \tag{1.2}
\]

This derives the prime-side renormalization required by 107_202.  It is
fixed by the universal order-change formula, not by fitting zeta.

## 2. Critical cofinal failure

Take \(s=1/2\) and let \(S_X=\{p:p\le X\}\).  Then

\[
 0<\prod_{p\le X}(1-p^{-1/2})
 \le
 \exp\left(-\sum_{p\le X}p^{-1/2}\right).
 \tag{2.1}
\]

The prime sum on the right diverges, so

\[
 \lim_{X\to\infty}\det{}_2(1-D_{S_X,1/2})=0.
 \tag{2.2}
\]

On the other hand, \(\zeta(1/2)\) is finite and nonzero, hence

\[
 \zeta(1/2)^{-1}\ne0.
 \tag{2.3}
\]

## 3. No-go theorem

**Theorem.**  Although (1.1) gives the unique canonical prime-side
order-change counterterm at every finite support, its ordinary cofinal
limit does not realize the analytic continuation of \(\zeta^{-1}\) on
the critical line.

**Proof.**  Equations (2.2) and (2.3) give distinct limits at
\(s=1/2\). \(\square\)

Thus analytic continuation cannot be interpreted as norm convergence,
strong determinant convergence, or an ordinary infinite Euler product
of the renormalized finite blocks.

## 4. Required structure

A surviving continuation must add a genuinely nonlocal summation
functional or topology, for example:

1. a distributional/Mellin continuation as in 107_184;
2. a relative determinant against a global reference operator;
3. a branched determinant line with specified monodromy;
4. a nuclear-space trace rather than a Hilbert-space determinant limit.

The continuation functional must be fixed independently and must reject
Davenport--Heilbronn at the Euler input.

## 5. Exact scope

This does not invalidate the operator theorem of 107_200 on
\(\Re s>1\), nor the finite-support identity (1.1).  It closes only
the ordinary cofinal-limit route to the critical strip.

## 6. Falsifier

The verifier checks (1.1) on real and complex parameters and finite real
prime sets.  It then uses every prime through \(10^6\) to measure the
decay in (2.2), while independently evaluating \(1/\zeta(1/2)\).
Any stabilization toward the analytic value returns NO.
