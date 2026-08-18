# 106.33 — Endpoint-corrected prolate source and the even Rayleigh residual

## Purpose

The three-mode source of 106.12 has the two co-Poisson radical moments, but
its endpoint value is nonzero.  Consequently its Fourier leakage has a
literal (t^{-1}) carrier and the dilation estimate proposed after 106.32
does not apply to that vector.

This note makes the minimal correction: the moving source is selected in a
fixed low-mode space subject to the two radical moments and the two endpoint
jets.  The correction preserves the first two angle scales (d_4,d_8).  A
uniform exterior PSWF estimate then gives a Fuchs--Mellin carrier with
exponent (a=7/2), and hence

\[
 \boxed{
 |\mathscr R_L^+|\ll \lambda^7d_4 .}
 \tag{1}
\]

Thus the required residual exponent is (p_R=7<8).

No assertion about the beta floor or the cross residual is made here.

## 1. The endpoint-corrected constrained ladder

Let

\[
 J_6=\{0,4,8,12,16,20\}
 \tag{2}
\]

and let \(\psi_{j,\lambda}\) be the real, normalized, even PSWFs in the
Fourier (+1) sector, in the normalization of 106.12 and 106.24.  Put

\[
 a_j=\psi_{j,\lambda}(0),\qquad
 e_j=\psi_{j,\lambda}(\lambda),\qquad
 q_j=1-\chi_j,\qquad d_j=1-\chi_j^2 .
 \tag{3}
\]

Define the two-dimensional space

\[
 \mathcal K_\lambda^{\rm ep}
 =\left\{
 f=\sum_{j\in J_6}c_j\psi_{j,\lambda}:
 f(0)=0,\ \int_{\mathbb R}f=0,\
 f(\lambda)=0,\ f'(\lambda)=0
 \right\}.
 \tag{4}
\]

The four rows in (4) may be written as

\[
 (a_j),\qquad(q_ja_j),\qquad(e_j),\qquad(\mu_je_j).
 \tag{5}
\]

Indeed, the first two original rows are ((a_j)) and
\((\chi_ja_j)), while Theorem 2 of 106.24 gives

\[
 2\lambda f'(\lambda)
 =\sum_jc_j(\mu_j-4\pi^2\lambda^4)e_j.
 \tag{6}
\]

After the endpoint-value row vanishes, the last condition in (4) is exactly
the last row of (5).

### Lemma 1 — The endpoint constraints preserve the angle ladder

For all sufficiently large \(\lambda\), the four rows in (5) have rank four.
If \(\delta_{0,\lambda}^{\rm ep}\leq
\delta_{1,\lambda}^{\rm ep}\) are the two generalized eigenvalues of

\[
 \sum_{j\in J_6}d_j|c_j|^2
 \tag{7}
\]

relative to \(\sum|c_j|^2\) on \(\mathcal K_\lambda^{\rm ep}\), then

\[
 \boxed{
 \delta_{0,\lambda}^{\rm ep}\asymp d_4,
 \qquad
 \delta_{1,\lambda}^{\rm ep}\asymp d_8 .}
 \tag{8}
\]

In particular, a normalized first vector (f_\lambda^{\rm ep}\) satisfies

\[
 \sum_jd_j|c_j|^2\asymp d_4.
 \tag{9}
\]

#### Proof

Fixed-order prolate-to-Hermite asymptotics and the endpoint theorem of
106.24 give, for (j=4r), (0\leq r\leq5),

\[
 |a_{4r}|\asymp1,
 \qquad
 |e_{4r}|\asymp \lambda^{1/2}q_{4r}^{1/2},
 \qquad
 \mu_{4r}=\lambda^2(M_0+M_1r+O(\lambda^{-2})),
 \tag{10}
\]

where (M_1\neq0), and

\[
 \frac{q_{4(r+1)}}{q_{4r}}\asymp\lambda^8.
 \tag{11}
\]

Multiplication of rows and columns by uniformly invertible diagonal
matrices does not change rank or the orders of the generalized
eigenvalues.  With (y=\lambda^4), the resulting constraint matrix is a
uniform perturbation of

\[
 \begin{pmatrix}
 1&1&1&1&1&1\\
 1&y^2&y^4&y^6&y^8&y^{10}\\
 1&y&y^2&y^3&y^4&y^5\\
 0&y&2y^2&3y^3&4y^4&5y^5
 \end{pmatrix}.
 \tag{12}
\]

Its four consecutive-column minors are nonzero.  Hence the exact matrix
has rank four for large \(\lambda\).

Gaussian elimination in (12) gives two kernel vectors whose coefficient
profiles, up to uniformly bounded nonzero factors, are

\[
 v^{(0)}=
 (1,-1,2y^{-1},-y^{-2},y^{-4},0)+O(y^{-2})
 \tag{13}
\]

and

\[
 v^{(1)}=
 (0,1,-1,2y^{-1},-y^{-2},y^{-4})+O(y^{-2}).
 \tag{14}
\]

Since (d_{4r}\asymp d_4y^{2(r-1)}), (13) has Rayleigh quotient
\(\asymp d_4\).  After removing its component from (14), the latter has
quotient \(\asymp d_8\).  Conversely, the first two pivot equations in
(12), followed by Cauchy--Schwarz, give lower bounds (cd_4) on the whole
kernel and (cd_8) on the orthogonal complement of its first minimizing
direction.  The (O(y^{-2})) perturbation is smaller than both pivots and
is absorbed by the min--max principle.  This proves (8)--(9). \(\square\)

The coefficients in (13) also show that the first vector converges to the
same nonzero (0/4) Hermite combination as the vector of 106.12.  Hence the
norm lower bound for its positive-parity co-Poisson projection remains

\[
 \|V_\lambda^+\|\geq c_V>0.
 \tag{15}
\]

## 2. A uniform two-jet exterior theorem

Put

\[
 \ell_\lambda=(1-P_\lambda)\widehat f_\lambda^{\rm ep}.
 \tag{16}
\]

### Lemma 2 — Uniform exterior two-jet estimate

For \(t\geq\lambda\),

\[
 \boxed{
 |\ell_\lambda(t)|+
 \lambda^{-1}|\ell_\lambda'(t)|
 \leq
 C\lambda^{7/2}\sqrt{d_4}\,t^{-3}.}
 \tag{17}
\]

#### Proof

Write (c=2\pi\lambda^2) and (x=t/\lambda\).  The Fourier continuation of
each fixed prolate mode is the corresponding radial PSWF.  We use the
uniform radial expansions with error bounds in Dunster, *Asymptotics of
Prolate Spheroidal Wave Functions*, Sections 2--3.  The Bessel expansion is
uniform for (1<x<\infty); away from the pole the Liouville--Green
expansion has an arbitrary fixed number of terms and remainder
\(O(c^{-p})\), uniformly up to (x=\infty).  The same estimates hold after
one (x)-derivative by the differentiated Olver equations.

There are three overlapping regions.

**Boundary region, (1\leq x\leq2).**  The Bessel approximation and its
derivative bound, together with (9), give

\[
 |\ell_\lambda(\lambda x)|+
 \lambda^{-1}|\ell_\lambda'(\lambda x)|
 \ll \lambda^{1/2}\sqrt{d_4}.
 \tag{18}
\]

Since (x^{-3}\geq1/8), this is (17) in this region.

**Uniform oscillatory region, (2\leq x\leq c).**  Because all indices are
congruent modulo four, their outgoing phases have the same Fourier
orientation.  Expand the Liouville--Green solution through order (c^{-1})
and retain the error at order (c^{-2}).  The two boundary symbols of this
expansion are exactly

\[
 \sum_jc_je_j=f_\lambda^{\rm ep}(\lambda),
 \qquad
 \sum_jc_j\mu_je_j=2\lambda f_\lambda^{\rm ep}{}'(\lambda)
 \tag{19}
\]

after the common (4\pi^2\lambda^4) term has been removed.  They vanish by
(4).  The uniform remainder therefore gives

\[
 |\ell_\lambda(\lambda x)|+
 \lambda^{-1}|\ell_\lambda'(\lambda x)|
 \ll \lambda^{1/2}\sqrt{d_4}
       \bigl(x^{-3}+c^{-2}x^{-1}\bigr).
 \tag{20}
\]

For (x\leq c), (c^{-2}x^{-1}\leq x^{-3}), proving (17).

Here is the coefficient calculation behind this implication.  In Dunster's
notation, specialized to \(m=0\) and fixed \(n=j\), equations (2.27)--(2.28)
and (3.10) give

\[
 \sigma_j^2=\frac{2j+1}{c}+O(c^{-2}).
 \tag{20a}
\]

Insert this in the \(p=2\) version of the Liouville--Green expansion
(2.44)--(2.47), and use the quantization expansion (3.12).  Since
\(j\equiv0\pmod4\), the term \(-j\pi/2\) is an integral multiple of
\(2\pi\).  Taylor expansion of the amplitude and phase in \(\sigma_j^2\)
therefore gives, after restoring the physical normalization,

\[
 \widehat\psi_{j,\lambda}(\lambda x)
 =
 e_j\bigl(U_{0,\lambda}(x)+\mu_jU_{1,\lambda}(x)\bigr)
 +E_{j,\lambda}(x),
 \qquad 2\le x\le c,
 \tag{20b}
\]

where \(U_{0,\lambda},U_{1,\lambda}\) are independent of \(j\), and the
Olver remainder bounds, together with their differentiated versions, give

\[
\begin{aligned}
 |E_{j,\lambda}(x)|
 +\lambda^{-1}|\partial_tE_{j,\lambda}(x)|
 \le C_J |e_j|
 \bigl(x^{-3}+c^{-2}x^{-1}\bigr).
\end{aligned}
 \tag{20c}
\]

The spatial powers in (20c) can be read off without suppressing the phase
calculation.  Directly from Dunster's Liouville variable,

\[
\begin{aligned}
 \xi(\sigma,x)+J(\sigma)
 ={}&\sqrt{x^2-1}\\
 &+\sigma^2\left(
       \frac{\pi}{4}-\frac12\mathrm{arcsec}\,x
     \right)
 +O\!\left(\sigma^4(1+x^{-1})\right).
\end{aligned}
 \tag{20d}
\]

Here

\[
 J(\sigma)=\frac{\pi}{4}\sigma^2
            +\frac{\pi}{32}\sigma^4+O(\sigma^6),
\qquad
 \int_1^x\frac{dt}{t\sqrt{t^2-1}}
 =\mathrm{arcsec}\,x .
 \tag{20e}
\]

Using (20a), the quantization term \(cJ-j\pi/2\), and
\(j\equiv0\pmod4\), the mode-dependent phase relative to the common
outgoing phase is

\[
 \frac{2j+1}{2x}+O_j(x^{-3}+c^{-1}x^{-1}).
 \tag{20f}
\]

The radial amplitude is \(x^{-1}(1+O_j(x^{-2}+c^{-1}))\).  Consequently
the constant and the term linear in \(2j+1\) are precisely the two symbols
in (19); after their exact cancellation the spatial remainder is
\(O(x^{-3})\).  Expanding the \(c^{-1}\) coefficient once more shows that
its constant and affine parts are cancelled by the same two rows, leaving
\(O(c^{-2}x^{-1})\).  This proves (20c), including its powers of \(x\) and
\(c\), directly from the displayed uniform expansion.

The normalization by \(e_j\) in (20b) follows from Dunster's matching
constant (3.7); it is not an additional asymptotic assumption.  Summing
(20b), the two displayed terms vanish by (19), while
\(\sum|c_je_j|\ll\lambda^{1/2}\sqrt{d_4}\).  This proves (20).

For clarity, the occurrence of (x^{-3}) in (20) is not a formal
integration-by-parts assertion.  It is the second boundary-symbol remainder
in the uniform radial expansion.  Its coefficient can also be checked from
the exact outgoing recurrence.  If

\[
 y_j(t)=e^{2\pi i\lambda t}
        \sum_{m\geq0}a_{m,j}t^{-m-1}+\text{conjugate},
 \tag{21}
\]

then, with (A_j=4\pi^2\lambda^4-\mu_j),

\[
 2i(2\pi\lambda)m a_{m,j}
 =[m(m-1)+A_j]a_{m-1,j}
 +2i(2\pi\lambda)\lambda^2(m-1)a_{m-2,j}
 -\lambda^2(m-2)(m-1)a_{m-3,j}.
 \tag{22}
\]

The first two combined coefficients vanish by (19), while

\[
 \sum_jc_ja_{2,j}
 =-\frac1{8(2\pi\lambda)^2}
   \sum_jc_j\mu_j^2a_{0,j},
 \tag{23}
\]

so (10) and (9) put the surviving coefficient within the polynomial budget
in (17).

**Far region, (x\geq c).**  In this range (22) is a convergent Volterra/Jost
majorant after the first two coefficients have been deleted.  Since
\(|\mu_j|\ll\lambda^2\) and

\[
 \sum_j|c_je_j|\ll\lambda^{1/2}\sqrt{d_4},
 \tag{24}
\]

(23) and the recurrence tail give

\[
 |\ell_\lambda(t)|+\lambda^{-1}|\ell_\lambda'(t)|
 \ll\lambda^{5/2}\sqrt{d_4}\,t^{-3},
 \tag{25}
\]

which is stronger than (17).  The three regions cover
\([\lambda,\infty)). \(\square\)

## 3. Co-Poisson and Mellin transfer

Let

\[
 H_\lambda(v)=v^{1/2}\sum_{n\geq1}\ell_\lambda(nv),
 \qquad v\geq\lambda,
 \tag{26}
\]

and (D=v\partial_v).  Lemma 2 and absolute summation give

\[
 |H_\lambda(v)|\ll
 \lambda^{7/2}\sqrt{d_4}\,v^{-5/2},
 \tag{27}
\]

and

\[
 |DH_\lambda(v)|\ll
 \lambda^{9/2}\sqrt{d_4}\,v^{-3/2}.
 \tag{28}
\]

Define

\[
 A_\lambda(w)=\int_\lambda^\infty
 H_\lambda(v)v^{-w}\,d^*v,
 \qquad |\Re w|<\frac12.
 \tag{29}
\]

The direct bound from (27), followed for large ordinate by one integration
by parts using (28), yields uniformly on this strip

\[
 \boxed{
 |A_\lambda(w)|
 \ll
 \frac{\lambda^{7/2}\sqrt{d_4}}
      {1+|\Im w|}.}
 \tag{30}
\]

Indeed,

\[
 wA_\lambda(w)
 =H_\lambda(\lambda)\lambda^{-w}
  +\int_\lambda^\infty
       DH_\lambda(v)v^{-w}\,d^*v,
 \tag{31}
\]

and the last integral is

\[
 O\!\left(
  \lambda^{9/2}\sqrt{d_4}\,
  \lambda^{-3/2+|\Re w|}
 \right)
 =O(\lambda^{7/2}\sqrt{d_4}).
 \tag{32}
\]

The same estimate holds at (-w).  Therefore the seminorm of 106.26 obeys

\[
 \|\ell_\lambda\|_{\mathrm{FM},0,1}
 \ll\lambda^{7/2}\sqrt{d_4}.
 \tag{33}
\]

This is (FM) with (a=7/2<4).

## 4. Residual closure

The exact parity coordinate of 106.26 is

\[
 QW(R^+,R^+)=\sum_\rho b_\lambda(x_\rho)^2,
 \qquad
 b_\lambda(w)=\frac{A_\lambda(w)+A_\lambda(-w)}{\sqrt2}.
 \tag{34}
\]

The local zero-count estimate and (30) imply absolute convergence and

\[
 |QW(R^+,R^+)|\ll\lambda^7d_4.
 \tag{35}
\]

Finally (15) gives

\[
 \boxed{
 |\mathscr R_L^+|
 =\frac{|QW(R^+,R^+)|}{\|V_\lambda^+\|^2}
 \ll\lambda^7d_4.}
 \tag{36}
\]

Thus the first residual obligation in Paper 40 holds with

\[
 \boxed{p_R=7<8.}
 \tag{37}
\]

## 5. Scope of the correction

The endpoint correction is not an estimate applied to the old three-mode
vector.  It is a choice of the moving radical vector inside a fixed
low-mode prolate space.  It preserves:

1. the two exact co-Poisson radical moments;
2. the nonzero Hermite limit and hence the norm lower bound;
3. the first two constrained leakage levels (d_4,d_8);
4. positive multiplicative parity.

Accordingly, Lemmas A and B and the cross-residual obligation must be read
with this endpoint-corrected (q_L^+).  Their stated abstract forms are
unchanged.
