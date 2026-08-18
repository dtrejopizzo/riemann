# Archimedean boundary obstruction to the Loewner margin

## Result

The full Loewner/Carathéodory margin proposed in `103_24` is false even if
RH is assumed.  The obstruction is purely archimedean and occurs on the
critical-line boundary of the disk.

Let
\[
 s={1\over1-z},\qquad
 \mathfrak C_{\rm arch}(z)={2(1-z)^2\over z}\mathcal A(z).
\]
From the exact generator in `140`, cancellation of the pullback factors
gives
\[
 \mathfrak C_{\rm arch}(z)
 ={2\over s}-\log\pi+\psi\!\left({s\over2}\right).             \tag{1}
\]
The strong-margin symbol of `103_24` is
\[
 \mathfrak C_{\rm SM}=\mathfrak C_1-\tfrac12\mathfrak C_{\rm arch}.
\tag{2}

Under RH, away from zero ordinates, the functional equation and reality give
\[
 \Re\mathfrak C_1(z)=2\Re{\xi'\over\xi}(1/2+it)=0
 \quad\text{when}\quad s=1/2+it.                                 \tag{3}
\]
We prove below that
\[
 \Re\mathfrak C_{\rm arch}(1/2+it)>0\qquad(|t|\ge30).             \tag{4}
\]
Consequently
\[
 \Re\mathfrak C_{\rm SM}(z)
 =-\tfrac12\Re\mathfrak C_{\rm arch}(z)<0                        \tag{5}
\]
at those boundary points.  By radial continuity at a point which is not a
zero image, the same strict negativity holds at nearby interior points.
Therefore the kernel
\[
 {\mathfrak C_{\rm SM}(z)+\overline{\mathfrak C_{\rm SM}(w)}
  \over1-z\bar w}
\tag{6}
\]
cannot be positive semidefinite.  In particular, it cannot be the missing
Euler--Gamma proof of A1.

## Explicit digamma estimate

For \(\Re q>0\), the differentiated Binet identity is
\[
 \psi(q)=\log q-{1\over2q}
 -2\int_0^\infty {u\over u^2+q^2}{du\over e^{2\pi u}-1}.          \tag{7}
\]
It follows directly by differentiating the convergent Binet integral for
\(\log\Gamma(q)\); equivalently, differentiation under the integral is
justified on every closed right half-plane.  We include a bound sufficient
for (4), so no asymptotic sign is being used without a remainder.

Put \(q=1/4+iy\), \(y\ge1\), and call the integral term in (7) \(R(q)\).
Since
\[
 |u^2+q^2|=|u-y+i/4|\,|u+y-i/4|,
\]
split the integral at \(y/2\).  On \(0\le u\le y/2\),
\[
 |u^2+q^2|\ge(y-u)(y+u)\ge{3\over4}y^2.
\]
On \(u\ge y/2\),
\[
 |u^2+q^2|\ge {1\over4}(u+y).
\]
Using
\[
 \int_0^\infty {u\,du\over e^{2\pi u}-1}={1\over24},
 \qquad {1\over e^{2\pi u}-1}\le2e^{-2\pi u}\quad(u\ge1/2),
\]
gives
\[
 |R(q)|\le {1\over9y^2}+{8\over\pi}e^{-\pi y}<1.                \tag{8}
\]
Also \(|1/(2q)|\le1/2\).  Taking real parts in (7),
\[
 \Re\psi(1/4+iy)\ge\log|1/4+iy|-{3\over2}.                      \tag{9}
\]

Now put \(s=1/2+it\), so \(q=s/2=1/4+i t/2\).  For \(|t|\ge30\),
(9) and (1) imply
\[
\begin{aligned}
 \Re\mathfrak C_{\rm arch}(s)
 &\ge \log{|t|\over2}-\log\pi-{3\over2}\\
 &=\log{|t|\over2\pi}-{3\over2}>0,
\end{aligned}                                                     \tag{10}
\]
which proves (4).  Notice that this is a Gamma asymptotic with an explicit
remainder, not a numerical plot.

## Surviving target

The identities in `103_24` remain useful, but only after discarding full
Loewner positivity.  The surviving scalar target is the integrated
Dirichlet/Fejer energy
\[
 2\lambda_n-\lambda_n^{\rm arch}
 =\mathbf1_n^*[g_{j-k}-\tfrac12g^{\rm arch}_{j-k}]\mathbf1_n
 \ge0.                                                            \tag{11}
\]
It would imply the strong margin and A1 after A0.  Unlike (6), (11) does
not impose a boundary sign on the whole Carathéodory symbol, so the Gamma
obstruction above does not disprove it.  Proving (11) for all \(n\) remains
RH-strength (it implies Li positivity), but it is the only Toeplitz/Fejer
target left by this audit.
