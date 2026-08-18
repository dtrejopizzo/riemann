# D.109 — Periodic-depth Green resolvent and the archimedean support gate

## Status

The Frobenius-depth extremal frames of row A contain an intrinsic source for
the missing same-prime **difference** kernel.  If

\[
 d_{p,r}(a)=ap^r-p+1,
\]

the normalized cumulative extremal vectors have, after a cofinal shift of
the depth, Gram matrix

\[
 \lim_{t\to\infty}
 \left\langle u_{t+r},u_{t+s}\right\rangle
 =p^{-|r-s|/2}.
\]

This is exactly the Szegő/Poisson kernel used in the row-C realization of
all powers \(p^k\).  It is the Green kernel of an explicit positive Jacobi
operator and is compatible with Künneth products.  Thus the passage from
sum-depth contact to difference-depth correlation need not be inserted by
hand: it is forced by normalized overlap in the Frobenius filtration.

There are two precise qualifications.

1. The ordered-frame inclusion used below is canonical from the intrinsic
   slope labels, but it is not the differential of the literal inclusion
   \(\mathcal E_{N,p}\subset\mathcal E_{M,p}\).  The extremal functions
   themselves depend on \(N\), and the smaller regular moduli lands on the
   boundary of the larger one.  Row A does not yet contain this depth
   transition as a morphism of regular section moduli.
2. Prime-periodic fibres cannot produce the Gamma oscillator.  Their edge
   lengths are supported on \(k\log p\geq\log2\), whereas the Gamma heat
   module has nonzero continuous density on every interval next to zero.
   The independently constructed quarter-shift oscillator supplies the
   archimedean term, but it is an additional real boundary object.

After adjoining that oscillator, the source construction pulls back
exactly to \(B_{\rm nuc}\), including every \(p^k\) and Gamma.  It is a
Krein difference of positive forms, not a positive Hilbert form.  Its
nonpositivity on the two-moment primitive subspace is still exactly the
row-D inequality; it does not follow merely from positivity of the local
Green resolvents.

No zeta zero or sign of \(B_{\rm nuc}\) is used.  The paper is not modified.

## 1. Ordered extremal-depth Hilbert system

For an integral effective divisor of degree \(a>0\) on \(C_p\), row A and
the exact special-module theorem give

\[
 \mathrm{Ext}_{p,r}(a)
 =\{0,1,\ldots,d_{p,r}(a)-1\},\qquad
 d_{p,r}(a)=ap^r-p+1.                                  \tag{1.1}
\]

The label is intrinsic: it is the negative integral slope at the left end
of the fundamental interval.  Residuation recovers the coefficient of
each labelled extremal.  Hilbertize the row-A ordered cotangent frame by

\[
 H_{p,r}(a)=\ell^2(\mathrm{Ext}_{p,r}(a)).         \tag{1.2}
\]

Since \(d_{p,r}\) increases with \(r\), slope labels define the based
isometry

\[
 j_r:H_{p,r}(a)\longrightarrow H_{p,r+1}(a),\qquad
 e_i\longmapsto e_i.                                   \tag{1.3}
\]

This is a canonical morphism of the **free ordered frames**.  It is
important not to overstate (1.3).  In Connes--Consani's explicit formula

\[
 \phi_a^{(N)}(x)=
 \max\{-a(x-1),\lfloor(N-a)/p\rfloor(x-p)\},            \tag{1.4}
\]

the extremal function changes when \(N\) changes.  Although the inequality
defining the modules gives \(\mathcal E_{N,p}\subset\mathcal E_{M,p}\) for
\(N<M\), that inclusion does not send a regular point using all
\(N-p+1\) extremals to a regular point using all \(M-p+1\) extremals.
Consequently (1.3) is not presently the cotangent of a map between the
regular loci in row A.  It is the candidate depth morphism singled out by
the ordered residuation labels.

Let \(H_{p,\infty}(a)\) be the Hilbert direct limit and define the normalized
cumulative vector

\[
 u_r={1\over\sqrt{d_{p,r}(a)}}
      \sum_{i=0}^{d_{p,r}(a)-1}e_i.                    \tag{1.5}
\]

For \(r\leq s\), direct counting gives

\[
 \langle u_r,u_s\rangle
 ={d_{p,r}(a)\over\sqrt{d_{p,r}(a)d_{p,s}(a)}}
 =\sqrt{{d_{p,r}(a)\over d_{p,s}(a)}}.                 \tag{1.6}
\]

Thus this correlation is obtained from actual extremal multiplicity and
the ordered-frame metric, not from the coefficients of the explicit
formula.

## 2. Stationary Frobenius limit

Translate both depths by \(t\).  For fixed \(r,s\), (1.1) and (1.6) give

\[
\begin{aligned}
 \lim_{t\to\infty}
 \langle u_{t+r},u_{t+s}\rangle
 &=\lim_{t\to\infty}
 \sqrt{
 {ap^{t+\min(r,s)}-p+1\over
  ap^{t+\max(r,s)}-p+1}}\\
 &=p^{-|r-s|/2}.                                       \tag{2.1}
\end{aligned}
\]

The limit is independent of \(a\).  Multiplication by the canonical Haar
length \(\mu_p(C_p)=\log p\) yields

\[
 \boxed{K_p^{\rm per}(r,s)=\log p\,p^{-|r-s|/2}.}      \tag{2.2}
\]

This is exactly the kernel \(K_{\rm diff}\) missing in D.108.

There is also a finite-depth Markov decomposition.  Put

\[
 \rho_r=\sqrt{d_{p,r}(a)/d_{p,r+1}(a)}.
\]

Then

\[
 w_{r+1}={u_{r+1}-\rho_ru_r\over\sqrt{1-\rho_r^2}}
\]

is a unit vector orthogonal to all \(u_j\), \(j\leq r\), and

\[
 u_{r+1}=\rho_ru_r+\sqrt{1-\rho_r^2}\,w_{r+1},
 \qquad \rho_r\longrightarrow p^{-1/2}.                \tag{2.3}
\]

Hence (2.2) is the stationary covariance forced by independent new
extremal increments under Frobenius growth.

For two periodic factors the ordered Künneth frame gives the product

\[
 K_{p,q}^{\rm per}((r,s),(r',s'))
 =p^{-|r-r'|/2}q^{-|s-s'|/2},                          \tag{2.4}
\]

so the construction is strongly compatible with the row-A external
product.

## 3. Positive Jacobi operator and Szegő identification

Put \(\rho=p^{-1/2}\), and let \(S\) be the unilateral shift on
\(\ell^2(\mathbb Z_{\geq0})\).  The Toeplitz matrix

\[
 K_\rho(r,s)=\rho^{|r-s|}                               \tag{3.1}
\]

is the inverse of the positive Jacobi operator

\[
 Q_\rho={1\over1-\rho^2}(I-\rho S)(I-\rho S^*).        \tag{3.2}
\]

Indeed

\[
 K_\rho=(1-\rho^2)
 (I-\rho S^*)^{-1}(I-\rho S)^{-1}.                    \tag{3.3}
\]

Thus the prime kernel is a genuine Green/resolvent kernel of an intrinsic
positive nearest-neighbour depth operator.

Equivalently, in \(H^2(\mathbb D)\) define

\[
 h_p(z)={\sqrt{1-p^{-1}}\over1-p^{-1/2}z}.              \tag{3.4}
\]

Then

\[
 \langle S^rh_p,S^sh_p\rangle=p^{-|r-s|/2}.            \tag{3.5}
\]

Equations (2.1) and (3.5) give a unique isometry between the cyclic
stationary completion of the periodic-depth vectors and the Szegő cyclic
space.  Therefore the vector used in row C to generate every coefficient

\[
 \log p\,p^{-k/2}={\Lambda(p^k)\over\sqrt{p^k}}         \tag{3.6}
\]

is recovered from the periodic section filtration itself, once the
ordered depth morphism (1.3) is admitted.

## 4. Why the Gamma oscillator is not a periodic-depth limit

The prime-periodic construction has translation lengths

\[
 \{k\log p:p\text{ prime},\ k\geq1\}\subset[\log2,\infty). \tag{4.1}
\]

Any positive direct sum of its edge energies has jump measure supported on
that set.  In contrast, the archimedean boundary derivation has measure

\[
 d\nu_\infty(r)
 ={e^{-r/2}\over1-e^{-2r}}\,dr,\qquad r>0,             \tag{4.2}
\]

and

\[
 \|\partial_\infty F\|^2
 =\int_0^\infty\|F-S_rF\|_2^2\,d\nu_\infty(r).         \tag{4.3}
\]

The measure (4.2) is nonzero on every interval \((0,\varepsilon)\), while
(4.1) gives zero there for \(\varepsilon<\log2\).  Hence no positive
combination or cofinal limit of the prime-periodic depth edges can equal
the Gamma energy.

The correct independent source is the quarter-shift oscillator

\[
 A_\infty e_j=(j+\tfrac14)e_j,qquad
 \mathrm{Tr}(e^{-xA_\infty})={e^{-x/4}\over1-e^{-x}},          \tag{4.4}
\]

whose heat module gives (4.2) after \(x=2r\).  The digamma identity then
gives

\[
 G_\infty(F,G)=m_0\langle F,G\rangle
 -\langle\partial_\infty F,\partial_\infty G\rangle,
 \qquad m_0=\log\pi-\psi(1/4).                         \tag{4.5}
\]

This is source-defined and positive before the signed subtraction, but it
is not contained in the periodic moduli alone.

## 5. Exact A--B--C pullback

The cyclic isometry (3.5) yields on the logarithmic translation
representation

\[
 A_p=\sqrt{1-p^{-1}}
       (I-p^{-1/2}U_p)^{-1},qquad U_p=S_{\log p},       \tag{5.1}
\]

and hence

\[
 A_p^*A_p=\sum_{k\in\mathbb Z}p^{-|k|/2}U_p^k.         \tag{5.2}
\]

Combining the periodic Haar length, the reduced A--B contact
\(\deg C_p=\log p\), and (4.5), one obtains without inserting individual
prime-power coefficients

\[
\begin{aligned}
 B_{\rm per+\infty}(F,G)
 ={}&\sum_p\log p
   \bigl(\langle A_pF,A_pG\rangle-\langle F,G\rangle\bigr)\\
 &+m_0\langle F,G\rangle
   -\langle\partial_\infty F,\partial_\infty G\rangle. \tag{5.3}
\end{aligned}
\]

For compactly supported tests the paired expression stabilizes.  Expanding
(5.2) and using \(\Lambda(p^k)=\log p\) proves term by term

\[
 \boxed{B_{\rm per+\infty}(F,G)=B_{\rm nuc}(F,G),}      \tag{5.4}
\]

including both orientations of every \(p^k\) and the complete Gamma
finite part.

The two ruling jets remain

\[
 M_-(F)=\widehat f(0),\qquad M_+(F)=\widehat f(1).       \tag{5.5}
\]

Therefore the pullback on the row-A primitive fibre is exactly
\(B_{\rm nuc}|_{\ker(M_-,M_+)}\).

## 6. Why the positive Green kernel does not yet prove the Hodge sign

Although each \(K_\rho\) is positive, the finite-place term in (5.3) is

\[
 \log p\,(A_p^*A_p-I),                                 \tag{6.1}
\]

whose Fourier symbol \(P_\rho(e^{i\theta})-1\) changes sign.  The Gamma
term is likewise the signed difference \(m_0I-\partial_\infty^*
\partial_\infty\).  Thus (5.3) is a Krein polarization of positive source
objects, not a positive Hilbert Gram.

On the primitive subspace, the desired assertion is

\[
 -B_{\rm per+\infty}(F,F)\geq0.                         \tag{6.2}
\]

By (5.4), this is precisely \(-B_{\rm nuc}(F,F)\geq0\), i.e. the row-D
inequality.  Declaring (5.3) to be a positive metric would assume the
conclusion.  Equivalently, one still needs an intrinsic contraction from
the positive prime-plus-mass preparation space to the
prime-identity-plus-Gamma-energy space, restricted by the two jets.

## 7. Outcome

The decisive comparison has advanced in one genuine way:

\[
 \boxed{
 \text{periodic Frobenius extremal overlap}
 \;\Longrightarrow\;
 p^{-|r-s|/2}
 \;\Longrightarrow\;
 \text{all }p^k\text{ in }B_{\rm nuc}.}
\]

The remaining construction has two sharply separated obligations.

1. Promote the ordered-frame maps (1.3) to a functorial stratified
   cotangent correspondence between the actual regular section moduli.
2. Prove the primitive comparison (6.2) after adjoining the independent
   quarter-shift Gamma boundary module.

The first is a geometric internalization problem.  The second is the
global Hodge inequality; it is not supplied by local Green positivity.

