# 107.216 -- The relative R-genus has no ordinary prime sum

## 1. Exact inversion formula

Let

\[
D(z)=\left.\partial_\nu\operatorname{Li}_\nu(z)\right|_{\nu=0}
\]

and retain the corrected scalar boundary value of 107_215.  Put
\(x=q^{-1}>1\), \(L=\log x\), and take the upper lateral value at the
polylogarithm cut.  Differentiating Jonquiere's inversion formula at
order zero gives

\[
 \operatorname{Re}\{D(x+i0)+D(x^{-1})\}
 =-\operatorname{Re}\psi\left(-{iL\over2\pi}\right)
  -\gamma-\log(2\pi).
 \tag{1.1}
\]

Since

\[
 \operatorname{Re}{\log(1-x-i0)\over\log(x+i0)}
 ={\log(x-1)\over\log x},
\]

the real relative anomaly has the exact expression

\[
 R^{\mathrm{rel}}(x^{-1})
 =2D(x^{-1})
 +\operatorname{Re}\psi\left(-{i\log x\over2\pi}\right)
 +\gamma+\log(2\pi)-{\log(x-1)\over\log x}.
 \tag{1.2}
\]

This identity also provides a stable evaluation that does not approach
the polylogarithm cut numerically.

## 2. Asymptotic theorem

For \(q\to0^+\), the convergent defining series gives

\[
 D(q)=-\sum_{n\ge2}q^n\log n=O(q^2).
 \tag{2.1}
\]

The standard digamma asymptotic in every closed sector avoiding the
negative real axis gives

\[
 \operatorname{Re}\psi(-iy)=\log y+O(y^{-2}).
 \tag{2.2}
\]

Finally, \(\log(x-1)/\log x=1+o(1)\).  Substitution in (1.2) proves

\[
 \boxed{
 R^{\mathrm{rel}}(x^{-1})
 =\log\log x+\gamma-1+o(1).}
 \tag{2.3}
\]

For fixed real \(s>0\) and \(x=p^s\), the arithmetically weighted local
term therefore satisfies

\[
 A_p(s)=\log p\,R^{\mathrm{rel}}(p^{-s})
 =\log p\,[\log(s\log p)+\gamma-1+o(1)].
 \tag{2.4}
\]

In particular, \(A_p(s)\to+\infty\) along the primes.

### Theorem 2.1 (ordinary-sum no-go)

For every fixed real \(s>0\), the series

\[
 \sum_p A_p(s)
\]

does not converge in the ordinary sense.  Its terms do not even tend to
zero.  The same obstruction rules out any scalar summation method that
requires termwise decay before a prime-independent finite correction is
applied.

## 3. Consequence for the Gamma bridge

The correction of 107_215 solves the local branch problem but worsens,
rather than solves, ordinary global summability.  It cannot be summed
over prime divisors and then compared with Gamma.

Meyer's construction has a different order of operations.  The finite
places and the archimedean principal-value term arise together from a
virtual nuclear character, before placewise scalar evaluation.  Theorem
2.1 makes that order mandatory for the present route:

\[
 \boxed{\text{form the global operator quotient first; take its trace second.}}
\]

This does not yet identify the relative \(R\)-genus with Meyer's third
operator term, nor construct an arithmetic direct image.  It closes only
the ordinary prime-sum globalization of the scalar anomaly.

There is also a domain distinction: Mellin characters are spectral
probes, not elements of Meyer's rapidly decreasing multiplicative test
algebra.  Therefore (2.4) cannot be inserted termwise into Meyer's
published character formula; a comparison would first need a continuous
operator-valued transform on that test algebra.

## 4. Falsifier

`107_216_relative_r_genus_prime_sum_no_go.py` checks (1.2) against the
two lateral polylogarithm evaluations on actual primes, tests (2.3) at
large actual primes fixed in advance, and verifies that the weighted
terms grow rather than decay.  The proof of divergence is (2.1)--(2.4),
not the finite computation.
