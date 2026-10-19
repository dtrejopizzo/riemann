# R170_826 — Audit of the coupled multiscale collar

R170_825 was built on a first attempt and then audited. It does not contain a sign inequality.

## Verdict

The central analytic piece is accepted: the scale average of the real
coupled collar

\[
 C_{a,w}=\int w(\rho)\tau_{a/\rho}U_\rho\,d\rho,
 \qquad U_\rho=D_\rho^*\mathscr F D_\rho,
\]

is a multiplier--reflection that gains one derivative for each fixed
\(a>0\). Its compression to a finite window is Hilbert--Schmidt. By a
finite sum, this holds for the averaged block
\(\int w(\rho)H_\rho U_\rho d\rho\) that actually appears in PC.

This result repairs the gap left open in R170_823. It does not imply
positivity, uniform smallness across scales, nor control of the other
blocks of the multiscale interface.

## Phase and sign check

With the conventions of Paper 47,

\[
 U_\rho=u_\infty(D/\rho)J,
\]

and the multiplier preceding \(J\) is

\[
 q_{a,w}(\xi)=\int\eta(s)
   e^{i[\theta(s\xi)-as\xi]}ds,
 \qquad \theta'=m.
\]

So the phase derivative is

\[
 \xi[m(s\xi)-a].
\]

The Bernstein series of Paper 47 shows that \(m\) is even and strictly
increasing on the positive half-axis. The stationary point \(m(s\xi)=a\)
is confined to a finite band. For sufficiently large frequencies,
\(|m(s\xi)-a|\ge1\), and integration by parts gives decay
\(O(|\xi|^{-1})\).

It was also checked that the other orientations must not be mixed:
\(JH_\rho\) does not contain \(u_\infty\), while
\(\tau_{-a/\rho}U_\rho\) carries the phase with \(m+a\). Its possible
stationary points are likewise in a finite band for fixed \(a\).

## Bound check

Integration by parts produces

\[
 |q_{a,w}(\xi)|\le A_w/|\xi|
\]

outside an explicit band. The estimate for \(A_w\) is consistent: when
differentiating the denominator, \(m'(s\xi)\) appears, and
\(|s\xi m'(s\xi)|\le C_m\) provides the second term of the constant.
Together with the trivial bound inside the band, this proves \(q\in L^2\)
and \(L^2\to H^1\).

For \(q(D)J\), the kernel has the form \(\kappa(t+s)\). The measure of
each slice of the square \((-T,T)^2\) is at most \(2T\), so that

\[
 \|P_Tq(D)JP_T\|_{HS}^2\le \frac{T}{\pi}\|q\|_2^2
\]

with the normalization used. The triangle inequality gives the claim for
the finite arithmetic sum without modifying \(h_{M,N}(k)\).

## Exact limits

The explicit constant chosen in R170_825 grows with \(a=\log k\); the
resulting triangular bound is not uniform as the cutoffs grow. This does
not disprove better cancellations between different values of \(k\), but
it does not prove them either.

Hilbert--Schmidt means compactness, not a sign. A compact self-adjoint
operator can have eigenvalues of both signs, and the collar here does not
even appear isolated from all the other terms of PC. The next useful
piece would have to exploit the matrix of this operator over the
first-contact radical together with the Tate, Gamma, and alignment
blocks, or produce a joint cancellation before using norms.

The certified range of Paper 47 is not extended, nor is D proved.
