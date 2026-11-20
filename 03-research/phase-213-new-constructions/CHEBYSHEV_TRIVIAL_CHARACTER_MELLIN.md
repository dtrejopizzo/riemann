# Fractional weight of the trivial character

For \(x\ge1\), let \(G(x)=\sum_{n\le x}\Lambda(n)(x/n-1)-x\log x+(1+\gamma)x\).
The one-sided reduction requires \(G(x)\le C_\epsilon x^{1/2+\epsilon}\)
for each \(\epsilon>0\). The sign depends on the distribution of the primes
at arbitrary scales. What follows checks which spectral information
survives the substitution by large primes.

For \(\Re s>1\), termwise (absolute) integration gives
\[
 \int_1^\infty G(x)x^{-s-1}\,dx
 =-\frac{\zeta'(s)}{s(s-1)\zeta(s)}
   -\frac{1}{(s-1)^2}+\frac{1+\gamma}{s-1}.
\]
Indeed the integral of \(x/n-1\) from \(n\) is \(n^{-s}/[s(s-1)]\).
The Laurent expansion of \(\zeta\) checks the cancellation at 1.
At each nontrivial zero \(\rho\) of multiplicity \(m\), the residue
of the continuation is \(-m/[\rho(\rho-1)]\ne0\).

At the integers, \(\sum_{n\le N}\Lambda(n)\lfloor N/n\rfloor=\log N!\).
By Stirling, with \(w_N(t)=1-\{N/t\}\),
\[
 G(N)=\gamma N-\sum_{\sqrt N<p\le N}\log p\,w_N(p)+O(\sqrt N\log^2(2N)).
\]
The error includes the small primes, the powers with exponent at least two
and the logarithmic Stirling remainder; \(0\le w_N\le1\) suffices.
On the interval \([N,N+1]\) the von Mangoldt sum in the definition of
\(G\) is affine, and the linear interpolation error of \(G\) is at most \(1/(8N)\).

Consequently the step extension to \(x\) of the large-prime deficit,
taking \(N=\lfloor x\rfloor\), differs from \(G(x)\) by
\(O(\sqrt x\log^2(2x))\): on a unit interval the slope of \(G\)
is \(O(\log^2(2x))\) since \(\Lambda(n)\le\log n\).
The Mellin transform of this difference is holomorphic in
\(\Re s>1/2\) by locally uniform convergence. The large-prime deficit
therefore has the same residue at each possible zero to the right of the
line. The cutoff at \(\sqrt N\) does not attenuate that residue. The one-sided bound
for the deficit remains pending.
