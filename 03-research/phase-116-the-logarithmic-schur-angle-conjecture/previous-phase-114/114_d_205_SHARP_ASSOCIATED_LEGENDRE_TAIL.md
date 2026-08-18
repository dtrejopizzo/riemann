# D.205 — Sharp associated-Legendre tail for the endpoint-flat action

## Statement

The coefficient in D.204 can be sharpened without any asymptotic
estimate.  Let

\[
 p_n(u)=\sqrt{(2n+1)/2}\,P_n(u)
\]

and let \(g\in H^m(-1,1)\).  Then

\[
 \boxed{
 \sum_{n\ge N}|\langle g,p_n\rangle|^2
 \le { (N-m)!\over(N+m)!}
 \int_{-1}^1(1-u^2)^m|g^{(m)}(u)|^2\,du .
 }                                                     \tag{0.1}
\]

This improves the coefficient of D.204 by the exact factor

\[
 {N+m\over2m-1}.                                      \tag{0.2}
\]

It uses only associated-Legendre orthogonality and does not use a sign of
\(B_{\rm nuc}\).

## Proof

For \(n,k\ge m\), associated Legendre orthogonality gives

\[
 \int_{-1}^1(1-u^2)^m
 P_n^{(m)}(u)P_k^{(m)}(u)\,du
 =
 {2(n+m)!\over(2n+1)(n-m)!}\,\delta_{nk}.             \tag{1.1}
\]

After normalizing,

\[
 \int_{-1}^1(1-u^2)^m
 p_n^{(m)}(u)p_k^{(m)}(u)\,du
 =
 {(n+m)!\over(n-m)!}\,\delta_{nk}.                    \tag{1.2}
\]

For a polynomial \(g=\sum a_np_n\), (1.2) proves the exact identity

\[
 \int_{-1}^1(1-u^2)^m|g^{(m)}(u)|^2\,du
 =
 \sum_{n\ge m}{(n+m)!\over(n-m)!}|a_n|^2.             \tag{1.3}
\]

The multiplier on the right is increasing in \(n\).  Hence

\[
 \sum_{n\ge N}|a_n|^2
 \le {(N-m)!\over(N+m)!}
 \sum_{n\ge N}{(n+m)!\over(n-m)!}|a_n|^2,
\]

which proves (0.1) for polynomials.  Density in the graph norm of the
closed weighted derivative extends (1.3), and hence (0.1), to \(H^m\).

## Physical chart and operator form

On \((-T,T)\), write

\[
 \phi_n(t)=T^{-1/2}p_n(t/T).
\]

The unitary change \(\widetilde G(u)=\sqrt T\,G(Tu)\) transforms (0.1)
into

\[
 \sum_{n\ge N}|\langle G,\phi_n\rangle|^2
 \le c^\sharp_{N,m,T}
 \int_{-T}^T
 \left(1-{t^2\over T^2}\right)^m|G^{(m)}(t)|^2\,dt,
                                                               \tag{2.1}
\]

where

\[
 c^\sharp_{N,m,T}
 ={(N-m)!\over(N+m)!}T^{2m}.                         \tag{2.2}
\]

Thus for a safe synthesis \(S\), its finite positive block
\(B=S^*A_TS\), and

\[
 H_m(S)_{ij}
 =
 \int_{-T}^T
 \left(1-{t^2\over T^2}\right)^m
 (A_TS e_i)^{(m)}
 \overline{(A_TS e_j)^{(m)}}\,dt,                    \tag{2.3}
\]

one has

\[
 \boxed{
 \|R_NA_TSB^{-1/2}\|^2
 \le c^\sharp_{N,m,T}
 \lambda_{\max}(B^{-1/2}H_m(S)B^{-1/2}).
 }                                                     \tag{2.4}
\]

## Applicability to the complete endpoint action

For the endpoint-flat source

\[
 F(t)=(T^2-t^2)^{20}P(t),
\]

D.171 gives

\[
 A_TF(t)
 =-\frac12F(t)\log(T^2-t^2)+U_F(t).                  \tag{3.1}
\]

The singular part is locally \(x^{20}\log x\) times an analytic
function.  Its twentieth weak derivative is a sum of an \(L^2\)
logarithm and bounded functions.  Every translated contact is the
zero-extension of an endpoint-flat polynomial: its derivatives through
order nineteen match at the translated boundary and its twentieth weak
derivative is piecewise bounded.  The remaining term \(U_F\) is analytic
on each contact cell.  Therefore

\[
 A_TF\in H^{20}(-T,T),                                \tag{3.2}
\]

so (2.4) applies to the complete Gamma term and all active contacts, not
only to a formal smooth approximation.

## Numerical budget at \(N=260,m=20\)

Before the physical factor \(T^{40}\),

\[
 {240!\over280!}
 =2.4253625013\ldots\times10^{-97}.                  \tag{4.1}
\]

Consequently a tail allowance \(0.05\) permits the normalized derivative
budget

\[
 {0.05\over240!/280!}
 =2.0615474995\ldots\times10^{95},                   \tag{4.2}
\]

with the physical \(T^{40}\) kept explicitly in (2.2).  This is
\(7.17948\ldots\) times the budget from the coefficient-summed estimate
of D.204.

## Remaining finite computation

The analytic tail is now reduced to the directed finite Gram (2.3).
It must be evaluated using (3.1), exact beta/log moments for the
\(x^{20}\log x\) terms, cellwise contact polynomials, and directed
Bernstein enclosures for the analytic remainder.  The inequality above
does not substitute a sampled derivative or a numerical SVD for that
Gram.
