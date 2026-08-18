# Central-xi stability and the strong-margin gate

## Purpose and verdict

This note tests a route algebraically different from the prime--Laguerre
integral.  The theta expansion at the symmetry centre produces a genuine
moment sequence and a natural Jensen-stability target.  That target is an
RH criterion, but it does not by itself prove the stronger inequalities
\[
 D_n:=2\lambda_n-\lambda_n^{\rm arch}\ge0.                         \tag{1}
\]
For (1), the exact coefficient object is a different analytic function,
defined in Section 3 below.  A concrete coefficient-ratio property of that
function would prove every inequality (1), but the exact rational-interval
certificate below disproves it.  It also disproves the weaker reciprocal-
coefficient positivity suggested by the same argument.  Ordinary theta
positivity does not control either property, because the archimedean
division destroys the positive-measure structure.  Positive
Stieltjes/continued-fraction and Jensen-stability strengthenings of the
strong-margin function are incompatible with its complex divisor.

No external theorem is used below.

## 1. The central theta moments and the correct Jensen target

Use the positive even theta density of `103_15` and absorb its harmless
positive normalization into \(d\mu(u)\):
\[
 \xi(s)=\int_{\mathbb R}e^{(s-1/2)u}\,d\mu(u),\qquad d\mu(-u)=d\mu(u)>0.
                                                                    \tag{2}
\]
Put \(\Xi(t)=\xi(1/2+it)\) and
\(m_k=\int_{\mathbb R}u^k\,d\mu(u)\).  Superexponential decay of the
theta density permits termwise integration and gives
\[
 \Xi(t)=\sum_{k\ge0}{(-1)^km_{2k}\over(2k)!}t^{2k}.                \tag{3}
\]
Equivalently,
\[
 G(x):=\Xi(i\sqrt{x})=\sum_{k\ge0}c_kx^k,
 \qquad c_k={m_{2k}\over(2k)!}>0.                                 \tag{4}
\]
The notation is unambiguous because the right side defines an entire
function of \(x\).  A real zero \(t=\gamma\) of \(\Xi\) becomes the
negative real zero \(x=-\gamma^2\) of \(G\).  Conversely, every zero of
\(G\) has this form for one of the two square roots.  Therefore
\[
 \boxed{\quad RH\quad\Longleftrightarrow\quad
        \hbox{all zeros of }G\hbox{ are real and nonpositive}.\quad} \tag{5}
\]

For \(d,N\ge0\), define directly from (4)
\[
 J^{d,N}(X)=\sum_{j=0}^d{d\choose j}c_{N+j}X^j.                    \tag{6}
\]
A valid stability route is consequently:

> **Central Jensen target.** Prove that every polynomial (6) is
> hyperbolic with nonpositive zeros and prove that its standard cofinal
> rescalings converge locally uniformly to \(G\).

The convergence clause is essential: hyperbolicity of a finite collection,
or of every fixed degree only after an uncontrolled shift, says nothing
about the missing diagonal family.  If the target is proved, local uniform
convergence and the elementary preservation of zero-free compact sets
(Rouche's theorem) imply that \(G\) has no nonreal zero, and (5) proves RH.

## 2. What theta positivity proves, and the missing sign

The raw even moments are automatically Hankel-positive.  For arbitrary
real \(a_0,\ldots,a_r\),
\[
 \sum_{i,j=0}^ra_ia_jm_{2(i+j)}
 =\int_{\mathbb R}\left(\sum_{i=0}^ra_iu^{2i}\right)^2d\mu(u)\ge0. \tag{7}
\]
Thus all Hankel matrices \((m_{2(i+j)})\) are positive semidefinite.  This
is the exact Stieltjes-moment information delivered term by term by theta.

Jensen hyperbolicity asks for a different direction of minors.  Already
the discriminant of (6) for \(d=2\) is nonnegative exactly when
\[
 c_{N+1}^2\ge c_Nc_{N+2},                                         \tag{8}
\]
whereas (7), by Cauchy--Schwarz, gives
\[
 m_{2N+2}^2\le m_{2N}m_{2N+4}.                                   \tag{9}
\]
In moment form, (8) requires the quantitative *upper* bound
\[
 {m_{2N}m_{2N+4}\over m_{2N+2}^2}
 \le{(2N+4)(2N+3)\over(2N+2)(2N+1)},                              \tag{10}
\]
while (9) supplies only the lower bound that the left side is at least one.
There is no contradiction: the factorials leave a narrow interval.  But
there is also no implication.  Higher Jensen determinants require the
corresponding higher Toeplitz-type signs, while (7) remains a Hankel square.

This pinpoints the new theta theorem that would have to be proved: not
positivity of each theta summand, but the complete family of normalized
moment inequalities beginning with (10), strong enough to give all (6).
The finite positive even measure in `103_15` has the same proof of (7) and
has off-line zeros.  Hence no argument that uses only evenness, positivity,
termwise integration, and Gram/Hankel squares can establish that family.
One must use a special variation-diminishing or total-positivity property of
the actual theta density.  Establishing it for all orders would itself prove
RH by (5).

## 3. The analytic function whose logarithmic coefficients are \(D_n\)

Let
\[
 H_\xi(z)={\xi(1/(1-z))\over\xi(1)},\qquad
 \log H_\xi(z)=\sum_{n\ge1}{\lambda_n\over n}z^n,                 \tag{11}
\]
and let
\[
 X_{\rm arch}(s)=s\pi^{-s/2}\Gamma(s/2),\qquad
 H_{\rm arch}(z)={X_{\rm arch}(1/(1-z))\over X_{\rm arch}(1)}
 =\exp\left(\sum_{n\ge1}{\lambda_n^{\rm arch}\over n}z^n\right). \tag{12}
\]
The last equality follows by applying the same Li generating identity to
the archimedean factor; its first coefficient is
\(1-(\gamma+\log4\pi)/2\), and expansion of the logarithmic derivative of
\(\Gamma(s/2)\) gives the odd-\(r\) formula for
\(\lambda_n^{\rm arch}\) used in the phase.  In particular, these are
identities of germs at zero, and \(H_{\rm arch}\) is nonzero whenever
\(s=1/(1-z)\) is a nontrivial zeta zero: \(s\ne0\), the exponential factor
is nonzero, and the Gamma function has no zeros.
Define the **strong-margin exponential**
\[
 \boxed{\quad B_D(z)={H_\xi(z)^2\over H_{\rm arch}(z)}
 =\exp\left(\sum_{n\ge1}{D_n\over n}z^n\right).\quad}            \tag{13}
\]
Thus (1) is exactly coefficient positivity of \(\log B_D\), not zero
stability of \(G\).

There is a non-tautological sufficient coefficient property.  Write
\(B_D(z)=1+\sum_{n\ge1}b_nz^n\).  Assume
\[
 b_n>0,\qquad {b_n\over b_{n-1}}
 \text{ is nondecreasing in }n.                                  \tag{14}
\]
Then every \(D_n\ge0\).

Here is a self-contained proof.  Write
\[
 {1\over B_D(z)}=1-\sum_{n\ge1}q_nz^n.                            \tag{15}
\]
Coefficient comparison gives
\[
 b_n=q_n+\sum_{j=1}^{n-1}q_jb_{n-j}.                              \tag{16}
\]
Assume inductively that \(q_1,\ldots,q_{n-1}\ge0\).  Multiply the
identity (16) at index \(n-1\) by \(b_n/b_{n-1}\).  Monotonicity in
(14) gives
\[
 {b_n\over b_{n-1}}b_{n-1-j}\ge b_{n-j}\qquad(1\le j<n),
\]
with \(b_0=1\), and hence
\(b_n\ge\sum_{j<n}q_jb_{n-j}\).  Equation (16) gives \(q_n\ge0\).
Finally,
\[
 \log B_D(z)=-\log\left(1-\sum_{n\ge1}q_nz^n\right)
 =\sum_{r\ge1}{1\over r}\left(\sum_{n\ge1}q_nz^n\right)^r       \tag{17}
\]
has nonnegative coefficients.  Equation (13) now gives \(D_n\ge0\).

Property (14) is therefore an exact sufficient condition for the strong
margin.  It is, however, false for \(B_D\).  From (13),
\[
 b_1=D_1,\qquad b_2={D_2+D_1^2\over2},\qquad
 b_3={D_3\over3}+{D_1D_2\over2}+{D_1^3\over6}.                  \tag{18}
\]
The fraction-only propagation of the certified phase-102 intervals gives
\[
\begin{aligned}
 b_1&\in[0.600311373867653894420822,
          0.600311373867653894420823],\\
 b_2&\in[0.709802288892808649025747,
          0.709802288892808649025748],\\
 b_3&\in[0.830102184035357907376825,
          0.830102184035357907376826],
\end{aligned}                                                     \tag{19}
\]
and
\[
 \boxed{b_1b_3-b_2^2\in
 [-0.005499506768664409777139,
  -0.005499506768664409777138]<0.}                               \tag{20}
\]
Thus \(b_3/b_2<b_2/b_1\), contrary to (14).  The reproducible verifier is
`tools/bd_ratio_interval_verify.py`; it imports the rational input
enclosures and interval operations of the phase-102 certificate, and uses
no binary floating-point arithmetic in the sign decision.

Nor can one merely reverse the monotonicity.  The polynomial
\(B(z)=1+z+(2/5)z^2\) has positive coefficients and decreasing ratios, but
\[
 [z^2]\log B={2\over5}-{1\over2}=-{1\over10}<0.                  \tag{21}
\]
Hence neither direction of elementary ratio monotonicity proves the desired
logarithmic coefficient sign.

Theta positivity would not prove (14) term by term even if it survived:
\(H_\xi\) has a positive-measure representation, but (13) squares it and
then divides by the independent exponential (12).  Neither the coefficients
\(b_n\) nor their two-by-two minors are Gram determinants of the theta
measure.  Expanding (13) simply restores the completed prime--pole--Gamma
cancellation already isolated in `103_26`.

## 4. Why Stieltjes fractions and Jensen stability of \(B_D\) are too strong

Differentiate (13):
\[
 M_D(z):={B_D'(z)\over B_D(z)}=\sum_{n\ge1}D_nz^{n-1}.             \tag{22}
\]
A tempting sufficient condition is a positive Stieltjes representation
\[
 M_D(z)=\int_0^R{d\nu(t)\over1-tz},\qquad d\nu\ge0.               \tag{23}
\]
It would immediately give \(D_n=\int_0^Rt^{n-1}d\nu(t)\ge0\), and its
coefficient algorithm would yield a positive Stieltjes continued fraction.
But (23) is impossible for the actual function.

Indeed, if \(\rho\) is a nontrivial zero of multiplicity \(m\), then
\(H_\xi\) vanishes at
\[
 w_\rho=1-{1\over\rho},
\]
and (12) has no zero.  Therefore (22) has a pole at \(w_\rho\) with
residue \(2m\).  The theta representation (2) is strictly positive for real
\(0<s<1\), so no nontrivial zero is real; hence \(w_\rho\) is nonreal.
On the other hand, (23), wherever meromorphically continued from a compactly
supported measure, can have isolated poles only at real points \(z=1/t\).
Thus its divisor cannot equal that of (22).  The same obstruction rules out
a Hamburger/Stieltjes moment fraction with real support.

Likewise, demanding that \(B_D\), or all its Jensen approximants with a
cofinal limit, have only real nonpositive zeros is incompatible with the
same nonreal points \(w_\rho\).  Jensen stability belongs naturally to the
central function \(G\), where it is an RH criterion; it does not belong to
the conformal strong-margin exponential.

## 5. Exact remaining property

The algebraic alternatives are now separated:

1. Proving cofinal Jensen hyperbolicity for the normalized theta moments
   \(c_k=m_{2k}/(2k)!\) proves RH, but ordinary termwise theta positivity
   supplies only the wrong (Hankel) minors.
2. The positive, log-convex coefficient property (14) would prove the
   stronger inequalities \(D_n\ge0\), but (20) disproves it.  Reversed
   ratio monotonicity does not suffice, by (21).
3. A positive Stieltjes/continued-fraction representation for (22), or a
   real-zero Jensen theorem for \(B_D\), is excluded by its nonreal poles or
   zeros and should not be pursued.

The proof of the ratio lemma passed through a seemingly weaker sufficient
condition, namely \(q_n\ge0\) in (15).  That condition is also false.  The
same exact verifier computes \(b_n\) recursively from
\[
 nb_n=\sum_{k=1}^nD_kb_{n-k}
\]
and then computes the reciprocal coefficients from (16).  It certifies
\[
 \boxed{\quad q_7\in
 [-0.004643030401682042718870,
  -0.004643030401682042718869]<0.\quad}                           \tag{24}
\]
Thus even reciprocal-coefficient positivity cannot be the missing
strong-margin mechanism.

The central expansion leaves one valid stability program: prove the full
Jensen property of Section 1 from a special, all-order property of the
actual normalized theta moments.  That would prove RH directly, but not the
stronger sequence (1).  For \(D_n\), all three tested upgrades---elementary
ratio monotonicity, reciprocal positivity, and a Stieltjes fraction---are
now eliminated.  Termwise theta positivity cannot repair them: it supplies
only the Hankel squares (7), whereas the required normalized Jensen minors
and the completed archimedean quotient contain essential subtractions.
