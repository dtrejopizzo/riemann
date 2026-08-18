# High-order Euler--Maclaurin scaling boundary

The requested fixed-point extension through \(\gamma_{148}\) cannot be
claimed with the present remainder and \(N=64\).  For
\(q=2R\), the implemented rigorous remainder is

\[
 \frac4{6^q}\int_N^\infty x^{-q-1}
 \sum_l|[t^l]P_{148,q}|\log^l x\,dx. \tag{1}
\]

It is an exact rational expression once the rational logarithm interval is
chosen.  Forming it for \(q=180\), \(N=64\) with Python `Fraction` exceeded
the interactive resource limit; thus no false numerical bound is reported.

Its scale already rules out the proposed parameter expectation under this
coarse periodic-Bernoulli bound.  The leading derivative size has the
Stirling scale \(q!\), so (1) contains the characteristic factor

\[
 \frac{q!}{(6N)^q}(\log N)^{148}
 \asymp\left(\frac q{6eN}\right)^q(\log N)^{148}. \tag{2}
\]

For \(q=180,N=64\), the factorial factor is about \(10^{-138}\), while
\((\log64)^{148}\) is about \(10^{89}\), before the other positive terms.
This is far short of a \(10^{-120}\) target.  Increasing \(R\) only helps
until the usual asymptotic optimum near the Euler--Maclaurin scale; it does
not make \(N=64,R=90\ldots120\) an established 120-digit scheme for
\(j=148\).

Therefore a 149 certificate requires either a substantially larger \(N\),
a sharper high-order remainder method, or a different analytic generator.
The currently executed fixed-point certificate remains exactly
\(9\le n\le20\).  No higher range is asserted.
