# D.204 — Exact weighted-Sobolev control of the Legendre tail

## Verdict

Endpoint flatness can be converted into the precise Legendre-tail estimate
needed by the corrected three-block Feshbach argument.  No Fourier-to-
Legendre heuristic is required.  If \(p_n(u)=\sqrt{(2n+1)/2}\,P_n(u)\) and
\(g\in H^m(-1,1)\), then, for \(N\ge m\),

\[
 \boxed{\quad
 \sum_{n\ge N}|\langle g,p_n\rangle|^2
 \le { (N-m)!\over(N+m)!}
       \int_{-1}^1(1-u^2)^m|g^{(m)}(u)|^2\,du .\quad}       \tag{0.1}
\]

On \((-T,T)\), with the normalized physical Legendre basis, the right hand
side becomes

\[
 { (N-m)!\over(N+m)!}\,T^{2m}
 \int_{-T}^T\left(1-{t^2\over T^2}\right)^m
 |G^{(m)}(t)|^2\,dt .                                  \tag{0.2}
\]

Consequently the finite-band computations in D.203 can be completed by a
directed enclosure of one finite derivative Gram matrix.  Formula (0.1) is
only the analytic bridge: it does not by itself assert the final row-D
sign, and no paper file is modified.

## 1. Exact coefficient estimate

For \(n\ge m\), the Jacobi differentiation identity is

\[
 P_n(u)={ (n-m)!\over 2^m n!}{d^m\over du^m}
 \left((u^2-1)^mP_{n-m}^{(m,m)}(u)\right).             \tag{1.1}
\]

The factor \((u^2-1)^m\) kills all boundary terms of orders below \(m\).
Integrating (1.1) by parts \(m\) times therefore gives

\[
 \int_{-1}^1gP_n
 ={(n-m)!\over2^mn!}
 \int_{-1}^1g^{(m)}(1-u^2)^mP_{n-m}^{(m,m)}.           \tag{1.2}
\]

The exact Jacobi norm is

\[
 \int_{-1}^1(1-u^2)^m\left(P_{n-m}^{(m,m)}(u)\right)^2du
 ={2^{2m+1}\over2n+1}{(n!)^2\over(n-m)!(n+m)!}.       \tag{1.3}
\]

Cauchy--Schwarz in (1.2), using weight \((1-u^2)^m\), gives the
coefficientwise estimate

\[
 |\langle g,p_n\rangle|^2
 \le {(n-m)!\over(n+m)!}
 \int_{-1}^1(1-u^2)^m|g^{(m)}(u)|^2du.                \tag{1.4}
\]

That estimate alone would give the weaker summed constant

\[
 \sum_{n=N}^{\infty}{(n-m)!\over(n+m)!}
 ={(N-m)!\over(2m-1)(N+m-1)!},                        \tag{1.5}
\]

because the summand is the difference of consecutive factorial ratios
divided by \(2m-1\).  There is, however, an exact orthogonality which is
stronger by the factor \((N+m)/(2m-1)\):

\[
 \int_{-1}^1(1-u^2)^m p_n^{(m)}(u)p_k^{(m)}(u)\,du
 ={(n+m)!\over(n-m)!}\,\delta_{nk}.                   \tag{1.6}
\]

Thus Parseval in the weighted derivative space gives

\[
 \int_{-1}^1(1-u^2)^m|g^{(m)}|^2
 =\sum_{n\ge m}{(n+m)!\over(n-m)!}
   |\langle g,p_n\rangle|^2.                          \tag{1.7}
\]

The weight in (1.7) increases with \(n\), so keeping only \(n\ge N\)
and dividing by its value at \(N\) proves the sharp estimate (0.1).
Density extends the calculation from polynomials to the corresponding
weighted Sobolev domain.

## 2. Finite-dimensional operator form

Let \(S:\mathbb C^s\to L^2(-T,T)\) synthesize the proposed safe frame, let
\(A\) be the completed row-D operator, and let

\[
 B=S^*AS>0,\qquad
 H_m=\left(\left\langle
 (AS e_i)^{(m)},
 \left(1-{t^2\over T^2}\right)^m(AS e_j)^{(m)}
 \right\rangle\right)_{i,j}.                          \tag{2.1}
\]

Denote by \(R_N\) the orthogonal projection onto Legendre modes
\(n\ge N\).  Applying (0.2) to every linear combination gives the Loewner
inequality

\[
 S^*A R_N A S
 \le c_{N,m,T} H_m,
 \qquad
 c_{N,m,T}={ (N-m)!T^{2m}\over(N+m)!}.                \tag{2.2}
\]

Thus the normalized tail capacity satisfies

\[
 \|R_NASB^{-1/2}\|^2
 \le c_{N,m,T}\,
 \lambda_{\max}(B^{-1/2}H_mB^{-1/2}).                 \tag{2.3}
\]

Everything on the right of (2.3) is finite-dimensional and can be enclosed
with Arb interval arithmetic.  This is the correct replacement for treating
a finite rectangular band as though it were the entire complement.

## 3. Primitive graph correction

The complement used in D.185 is the primitive complement, not literally
the raw Legendre tail.  Write it as the graph

\[
 Q=\{h+Lh:h\in R_NL^2\},\qquad \|L\|\le\eta,          \tag{3.1}
\]

where D.185 gives a directed value \(\eta<10^{-500}\) at
\(T=\tfrac12\log6\), \(N=200\).  For every \(v\), projection onto this
graph obeys the elementary bound

\[
 \|P_Qv\|\le \sqrt{1+\eta^2}
 \bigl(\|R_Nv\|+\eta\|(I-R_N)v\|\bigr).              \tag{3.2}
\]

Indeed, writing \(P_Qv=h+Lh\), the graph normal equation gives
\(h=(I+L^*L)^{-1}(R_Nv+L^*(I-R_N)v)\); (3.2) follows from
\(\|(I+L^*L)^{-1}\|\le1\) and
\(\|h+Lh\|\le\sqrt{1+\eta^2}\|h\|\).

Hence (2.3), together with a directed full-action Gram for \(AS\), controls
the actual primitive residual.  The graph term is numerically negligible
at this endpoint, but it must remain in the interval certificate.

## 4. What remains at the endpoint

For the \(M=20\) endpoint-flat safe space one must now:

1. enclose \(H_{20}\) for the **complete** Gamma and all active contacts;
2. combine (2.3) with the already directed rectangular rows and (3.2);
3. prove \(\kappa<\delta\) and the corrected low-block Schur inequality of
   D.200.

The factorial in (2.3) supplies the missing rigorous decay.  The numerical
sign of the resulting finite interval matrices is a separate obligation.
