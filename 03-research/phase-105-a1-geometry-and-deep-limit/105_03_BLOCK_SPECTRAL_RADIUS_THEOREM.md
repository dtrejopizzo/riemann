# 105_03 — Exact block spectral radius and the ordinary-prime selector

## Result

Let

\[
 I_L=\{L^2,L^2+1,\ldots,L^2+L-1\},
 \qquad
 S_L=\sum_{n\in I_L}|\lambda_n|.
\]

For a nontrivial zero \(\rho\), put

\[
 w_\rho=1-\frac1\rho,
\]

and define

\[
 \mathcal R_\zeta
 =\max\left\{1,\max_\rho |w_\rho|\right\}.
\]

The maximum is understood as \(1\) when every \(|w_\rho|=1\). If an
off-line zero exists, the maximum is attained because
\(|w_\rho|\to1\) as \(|\Im\rho|\to\infty\).

The exact block law is

\[
 \boxed{
 \lim_{L\to\infty}(1+S_L)^{1/L^2}=\mathcal R_\zeta.}
 \tag{1}
\]

Consequently,

\[
 \boxed{
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 \log(1+S_L)=o(L^2).}
 \tag{2}
\]

Thus a subexponential block estimate does not merely provide a convenient
sufficient condition. It excludes exactly the innermost Cayley pole and is
equivalent to RH.

## 1. Dominant Cayley poles

Use the Li generating function

\[
 G(z)
 =z\frac d{dz}\log\xi\!\left(\frac1{1-z}\right)
 =\sum_{n\ge1}\lambda_n z^n.                             \tag{3}
\]

A zero \(\rho\) of multiplicity \(m_\rho\) maps to
\(w_\rho=1-1/\rho\). Near that point,

\[
 \operatorname*{Res}_{z=w_\rho}G(z)=m_\rho w_\rho.      \tag{4}
\]

Assume RH is false and put

\[
 r_0=\min_{\Re\rho>1/2}|w_\rho|<1,
 \qquad R=r_0^{-1}>1.                                    \tag{5}
\]

There are finitely many poles on \(|z|=r_0\). Subtract their principal
parts and choose \(q\), with \(r_0<q<1\), before the next pole modulus.
Coefficient extraction then gives

\[
 \lambda_n
 =-\sum_{|w|=r_0}m_w w^{-n}+O(q^{-n})
 =-R^nP_n+O(R_1^n),                                      \tag{6}
\]

where \(R_1=q^{-1}<R\) and, after equal phases are grouped,

\[
 P_n=\sum_{j=1}^d M_j u_j^n,
 \qquad |u_j|=1,
 \qquad u_j\ne u_k\quad(j\ne k),
 \qquad M_j>0.                                           \tag{7}
\]

The functional equation pairs \(w\) with \(1/\overline w\). Hence

\[
 R=\max_\rho|w_\rho|=\mathcal R_\zeta.                 \tag{8}
\]

## 2. A dominant mode survives every long block

The finite trigonometric polynomial in (7) has a uniform block
mean-square lower bound. For every starting point \(N\),

\[
\begin{aligned}
 \sum_{n=N}^{N+L-1}|P_n|^2
 &=L\sum_{j=1}^dM_j^2+E_{N,L},\\
 |E_{N,L}|
 &\le
 \sum_{j\ne k}\frac{2M_jM_k}{|1-u_j\overline{u_k}|}
 =:C_P.
\end{aligned}                                            \tag{9}
\]

Indeed, every off-diagonal term is a finite geometric sum. Set

\[
 A_P=\sum_jM_j^2>0.
\]

For \(L\ge2C_P/A_P\), equation (9) implies that some
\(n\in[N,N+L-1]\) satisfies

\[
 |P_n|\ge\sqrt{A_P/2}=:c_P>0.                           \tag{10}
\]

This conclusion is uniform in \(N\). In particular, take \(N=L^2\).
Since \((R_1/R)^{L^2}\to0\), equations (6) and (10) give, for all large
\(L\),

\[
 S_L\ge cR^{L^2}                                        \tag{11}
\]

with a fixed \(c>0\). The upper bound from (6) is

\[
 S_L\le CL R^{L^2+L}.                                   \tag{12}
\]

Taking logarithms in (11)--(12) proves

\[
 \lim_{L\to\infty}\frac{\log S_L}{L^2}=\log R         \tag{13}
\]

when RH is false.

## 3. Critical-line estimate

Assume RH. For \(\rho=1/2+i\gamma\), write

\[
 w_\rho=e^{i\theta_\gamma},
 \qquad
 |\theta_\gamma|
 =2\arctan\frac1{2\gamma}
 \le\frac1\gamma.
\]

Pairing conjugate zeros gives

\[
 \lambda_n
 =2\sum_{\gamma>0}m_\gamma
       \{1-\cos(n\theta_\gamma)\}.                     \tag{14}
\]

The zeros with \(\gamma\le n\) contribute at most \(4N(n)\). For the
remaining zeros,

\[
 2\{1-\cos(n\theta_\gamma)\}
 \le n^2\theta_\gamma^2
 \le\frac{n^2}{\gamma^2}.                              \tag{15}
\]

Riemann--von Mangoldt and partial summation yield

\[
 N(T)\ll T\log(T+2),
 \qquad
 \sum_{\gamma>n}\frac{m_\gamma}{\gamma^2}
 \ll\frac{\log(n+2)}n.                                 \tag{16}
\]

Therefore

\[
 0\le\lambda_n\ll n\log(n+2),                          \tag{17}
\]

and

\[
 S_L\ll L^3\log(L+2)=\exp\{o(L^2)\}.                  \tag{18}
\]

Equations (13) and (18) prove (1)--(2).

## 4. Exact ordinary-prime lift

For \(\varepsilon>0\), retain the complete prime--pole expression

\[
 \lambda_{n,\varepsilon}
 =A_n+p_n(\varepsilon)
 -\sum_{m\ge2}\frac{\Lambda(m)}{m^{1+\varepsilon}}
       L_{n-1}^{(1)}(\log m),
 \qquad
 \lambda_{n,\varepsilon}\longrightarrow\lambda_n.     \tag{19}
\]

The polar term has the integral form

\[
 p_n(\varepsilon)
 =\int_0^\infty e^{-\varepsilon u}
       L_{n-1}^{(1)}(u)\,du.                             \tag{20}
\]

Define the signed prime--continuum discrepancy

\[
 d\nu_\varepsilon(u)
 =e^{-\varepsilon u}\,du
 -\sum_{m\ge2}\frac{\Lambda(m)}{m^{1+\varepsilon}}
       \delta_{\log m}(du),                              \tag{21}
\]

and, for \(\sigma=(\sigma_0,\ldots,\sigma_{L-1})\),

\[
 P_{\sigma,L}(u)
 =\sum_{j=0}^{L-1}\sigma_j
       L_{L^2+j-1}^{(1)}(u).                             \tag{22}
\]

Finite-dimensional \(\ell^1\)--\(\ell^\infty\) duality and (19)--(21)
give the exact identity

\[
\boxed{
 S_L
 =\lim_{\varepsilon\downarrow0}
 \sup_{\sigma\in[-1,1]^L}
 \left\{
 \sum_{j=0}^{L-1}\sigma_jA_{L^2+j}
 +\int_0^\infty P_{\sigma,L}(u)\,d\nu_\varepsilon(u)
 \right\}.}                                             \tag{23}
\]

The limit and supremum commute here because the block is finite:

\[
 \left|
 \sup_\sigma\sum_j\sigma_j\lambda_{L^2+j,\varepsilon}
 -\sup_\sigma\sum_j\sigma_j\lambda_{L^2+j}
 \right|
 \le\sum_j
 |\lambda_{L^2+j,\varepsilon}-\lambda_{L^2+j}|\to0.    \tag{24}
\]

No modulus has been placed on the prime and polar channels separately.

For arbitrary selectors, summation over the Laguerre degree gives

\[
\begin{aligned}
 P_{\sigma,L}(u)
 ={}&\sigma_{L-1}L_{L^2+L-2}^{(2)}(u)
    -\sigma_0L_{L^2-2}^{(2)}(u)\\
 &+\sum_{j=0}^{L-2}(\sigma_j-\sigma_{j+1})
       L_{L^2+j-1}^{(2)}(u).                             \tag{25}
\end{aligned}
\]

Thus the two-boundary collapse occurs only for a constant selector.
Controlling the absolute block norm requires all selectors in (23).

Combining (2) and (23), RH is equivalent to the single literal-prime
estimate

\[
\boxed{
 \log\!\left[
 1+\lim_{\varepsilon\downarrow0}
 \sup_{\sigma\in[-1,1]^L}
 \left\{
 \sum_{j<L}\sigma_jA_{L^2+j}
 +\int P_{\sigma,L}\,d\nu_\varepsilon
 \right\}
 \right]
 =o(L^2).}                                               \tag{26}
\]

## 5. Contour audit

For a circle which crosses Cayley poles, the residue theorem gives

\[
 \frac1{2\pi i}\int_{|z|=r}\frac{G(z)}{z^{n+1}}\,dz
 =\lambda_n+
   \sum_{|w_\rho|<r}m_\rho w_\rho^{-n}.                 \tag{27}
\]

The second term is exactly the unstable mode in (6). Therefore none of
the following is a valid unconditional shortcut:

1. dropping the residue sum in (27);
2. bounding it by \(\exp\{o(n)\}\);
3. choosing cofinal circles \(r\uparrow1\) on which the generating
   function is holomorphic.

Each assertion excludes every Cayley pole in the unit disk and is already
equivalent to RH.

## 6. Status

Proved here:

- the exact block spectral-radius law (1);
- the block equivalence (2);
- uniform survival of a dominant trigonometric mode on every long block;
- the exact ordinary-prime selector identity (23);
- the contour residue audit (27).

Not proved here:

- the uniform arithmetic estimate (26) for the literal von Mangoldt
  weights;
- RH.

The remaining inequality is now a single quantified statement: it must
control the coupled prime--pole--archimedean expression uniformly over all
block selectors, after the Abel cancellation and before taking its
\(L^2\)-scale logarithm.
