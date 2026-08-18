# 106.146 — Global chord reconstruction and the null-IQC normal form

## 1. Purpose and result

Documents 106.143--106.144 show that neither a source-independent dynamic
IQC nor a decomposable arithmetic rotation can improve the physical signed
form.  This note identifies a genuinely global linear constraint on the
complete chord field.  It is not a triangle, local Hodge, divisor, or
Möbius relation.

Let

\[
 h(x)=\cosh(x/2),\qquad
 c_K=\int_{\mathbb R}K(u)h(u)\,du=\frac12,
 \tag{1}
\]

and, for an oriented displacement \(u\in\mathbb R\), define

\[
 (Cq)(u,x)
 =\{K(x)K(x-u)\}^{1/2}\{q(x)-q(x-u)\}.
 \tag{2}
\]

There is an explicit global reconstructor \(\mathscr R\) satisfying

\[
 \boxed{
 \mathscr RCq
 =q-\frac{((hq)*K)}{c_Kh}.}
 \tag{3}
\]

Consequently Riemann mean periodicity is equivalent to the exact chord
reconstruction equation

\[
 \boxed{(hq)*K=0\quad\Longleftrightarrow\quad\mathscr RCq=q.}
 \tag{4}
\]

After adjoining the literal copy constraints for every ordinary
\(\Lambda(n)\), the full Gamma density, and the polar continuum, one obtains
one stacked constraint \(\mathcal LZq=0\) whose kernel is exactly the
physical mean-periodic port range.

The resulting full-block S-procedure is lossless on every finite
heat/hybrid row.  More precisely, all off-kernel blocks can be eliminated
explicitly and the completed IQC becomes

\[
 \boxed{
 J+\mathcal L^*Y+Y^*\mathcal L
 =\operatorname {diag}(PJP,I),}
 \tag{5}
\]

where \(P\) is the orthogonal projection onto \(\ker\mathcal L\).  Thus a
global null IQC exists, but it has exactly zero sign slack: its only
uneliminated block is the original compressed physical form \(PJP\).

The direct Gamma-weighted Cauchy estimate for \(\mathscr R\) is not merely
too large; its ambient operator norm is infinite.  Therefore the surviving
construction must modify the reconstructor by a literal-prime,
source-specific null term before estimating its norm.  It cannot estimate
\(\mathscr R\) on the uncompressed chord space.

No zero-location statement is used below.

## 2. Exact global reconstruction

For an analytic chord field \(z=z(u,x)\), put

\[
 (\mathscr Rz)(x)
 =\frac1{c_Kh(x)}\int_{\mathbb R}
 \frac{h(x-u)K(u)}{\{K(x)K(x-u)\}^{1/2}}
 z(u,x)\,du.
 \tag{6}
\]

The initial domain consists of fields for which the integral is ordinary;
the identities then extend to the corresponding graph closure.

### Theorem 1 — Chord reconstruction identity

On the analytic multiplier core, (3) holds.  Hence (4) holds exactly.

#### Proof

Substitution of (2) in (6) gives

\[
\begin{aligned}
 (\mathscr RCq)(x)
 ={}&\frac{q(x)}{c_Kh(x)}
       \int_{\mathbb R}h(x-u)K(u)\,du\\
 &-\frac1{c_Kh(x)}
       \int_{\mathbb R}h(x-u)q(x-u)K(u)\,du.
\end{aligned}
 \tag{7}
\]

Since \(K\) is even and

\[
 h(x-u)=\cosh(x/2)\cosh(u/2)
        -\sinh(x/2)\sinh(u/2),
\]

the odd term integrates to zero and

\[
 (K*h)(x)=c_Kh(x).                                \tag{8}
\]

The second integral in (7) is \(((hq)*K)(x)\).  Equations (7)--(8) prove
(3), and (4) follows because \(c_Kh>0\). \(\square\)

Define

\[
 \mathcal L_0=I-C\mathscr R.                      \tag{9}
\]

On the analytic chord graph one has the exact range statement

\[
 \boxed{
 \ker\mathcal L_0
 =C\{q:(hq)*K=0\}.}                               \tag{10}
\]

Indeed, (4) proves inclusion from right to left.  Conversely, if
\(\mathcal L_0z=0\), then \(z=Cq\) with \(q=\mathscr Rz\).  Applying
\(\mathscr R\) gives \(\mathscr RCq=q\), and Theorem 1 gives
\((hq)*K=0\).

Unlike a local cycle equation, (9) integrates every chord displacement
before reconstructing its endpoint value.  It therefore remains meaningful
after the local Hodge and finite-incidence mechanisms of 106.111--106.113
have been exhausted.

## 3. The literal completed port constraint

Put

\[
 u_n=\log n,\qquad
 a_n=\frac{\Lambda(n)}{\sqrt n},\qquad
 r_\Gamma(u)=\frac{e^{-5u/2}}{1-e^{-2u}}quad(u>0).
 \tag{11}
\]

Use the three physical ports

\[
\begin{aligned}
 Z_pq&=(\sqrt{a_n}\,C_{u_n}q)_{n\ge2},\\
 Z_\Gamma q&=(\sqrt{r_\Gamma(u)}\,C_uq)_{u>0},\\
 Z_0q&=(e^{u/4}C_uq)_{u>0},
\end{aligned}                                      \tag{12}
\]

and

\[
 Zq=(Z_pq,Z_\Gamma q,Z_0q),\qquad
 J=\operatorname {diag}(I,I,-I).                 \tag{13}
\]

With the conventions fixed in 106.139--106.143,

\[
 \boxed{
 \langle Zq,JZq\rangle=\mathfrak Q_{\rm phys}(q).}
 \tag{14}
\]

Extract the master chord field from the polar port by

\[
 z(u)=e^{-u/4}Z_0(u).                              \tag{15}
\]

In addition to \(\mathcal L_0z=0\), impose the exact copy equations

\[
\begin{aligned}
 Z_\Gamma(u)-\sqrt{r_\Gamma(u)}\,z(u)&=0,\\
 Z_{p,n}-\sqrt{a_n}\,z(u_n)&=0,
\end{aligned}                                      \tag{16}
\]

together with the oriented-even compatibility equation.  Point evaluation
at \(u_n\) is continuous in the analytic form-core topology.  Let
\(\mathcal L\) denote the stack of (9) and (15)--(16).

### Theorem 2 — Exact physical range

On the analytic form core,

\[
 \boxed{
 \ker\mathcal L
 =Z\{q:(hq)*K=0\}.}                               \tag{17}
\]

#### Proof

Every physical port vector satisfies (15)--(16), and (10) proves the
global equation.  Conversely, (10) recovers a mean-periodic \(q\) from the
master chord field.  Equations (15)--(16) then force every other component
to equal the corresponding component of \(Zq\).  The orientation equation
identifies the two bilateral copies. \(\square\)

Thus (17) retains every real prime-power location, every ordinary
von Mangoldt coefficient, the complete Gamma density, and the polar
continuum.  None is replaced by an asymptotic density.

## 4. Lossless full-block null-IQC elimination

The next theorem is abstract but its constraint is the literal operator
of Theorem 2.

### Theorem 3 — Canonical finite-row null-IQC normal form

Let \(E\) be a finite heat/hybrid row and restrict \(\mathcal L\) and
\(J\) to the resulting finite port space \(H_E\).  Put

\[
 P=P_{\ker\mathcal L},\qquad Q=I-P,
 \qquad \mathcal L_1=\mathcal L|_{QH_E}.
 \tag{18}
\]

After replacing the constraint codomain by \(\operatorname {ran}\mathcal
L\), \(\mathcal L_1\) is bijective.  Write

\[
 J=\begin{pmatrix}A&B\\B^*&C\end{pmatrix}
 \quad\text{on }PH_E\oplus QH_E,
 \qquad A=PJP.                                    \tag{19}
\]

Define \(Y=[Y_P,Y_Q]:PH_E\oplus QH_E\to
\operatorname {ran}\mathcal L\) by

\[
 Y_P=-(\mathcal L_1^*)^{-1}B^*,\qquad
 Y_Q=\frac12(\mathcal L_1^*)^{-1}(I-C).           \tag{20}
\]

Then (5) holds.  Consequently

\[
 \boxed{
 \exists Y:\ J+\mathcal L^*Y+Y^*\mathcal L\succeq0
 \quad\Longleftrightarrow\quad PJP\succeq0.}     \tag{21}
\]

#### Proof

Relative to (18), \(\mathcal L=[0,\mathcal L_1]\).  Therefore

\[
 \mathcal L^*Y+Y^*\mathcal L
 =\begin{pmatrix}
 0&Y_P^*\mathcal L_1\\
 \mathcal L_1^*Y_P&
 \mathcal L_1^*Y_Q+Y_Q^*\mathcal L_1
 \end{pmatrix}.                                  \tag{22}
\]

Substitution of (20) changes the off-diagonal blocks into \(-B\) and
\(-B^*\), and the lower-right block into \(I-C\).  Adding (19) proves
(5).  This proves the reverse implication in (21).  For the forward
implication, test any proposed completion on \(v\in\ker\mathcal L\); its
null terms vanish and leave \(\langle v,Jv\rangle\ge0\). \(\square\)

The same forward implication holds without a closed-range assumption.  In
the infinite problem, (5) is obtained cofinally whenever the inverses in
(20) remain controlled; no such control is needed to identify the
force-bearing block.

### Corollary 4 — Exact counterfactual falsifier

If an off-line orbit exists, the literal vector of 106.37, 106.64, and
106.93 supplies \(q_{\rm off}\) with

\[
 \mathcal LZq_{\rm off}=0,
 \qquad
 \langle Zq_{\rm off},JZq_{\rm off}\rangle<0.    \tag{23}
\]

Hence every multiplier \(Y\), bounded or unbounded on a domain containing
that vector, satisfies

\[
 \langle Zq_{\rm off},
 (J+\mathcal L^*Y+Y^*\mathcal L)Zq_{\rm off}\rangle
 =\mathfrak Q_{\rm phys}(q_{\rm off})<0.          \tag{24}
\]

Thus a null IQC cannot manufacture the sign.  A successful explicit
arithmetic construction must prove positivity of the unchanged block
\(PJP\), and thereby exclude (23).

## 5. Why the raw reconstructor cannot be estimated

One might try to combine (4) with Cauchy--Schwarz using only the positive
Gamma continuum.  This produces an ambient norm obstruction which can be
computed exactly.

Let \(\widetilde r_\Gamma(u)=r_\Gamma(|u|)\) be the bilateral density and
give the oriented chord field the norm

\[
 \|z\|_\Gamma^2
 =\frac12\int_{\mathbb R}\int_{\mathbb R}
 |z(u,x)|^2\,dx\,\widetilde r_\Gamma(u)\,du.      \tag{25}
\]

Since \(\mathscr R\) acts independently at each \(x\), its squared row
norm after weighting the output by
\(d\mu_K=hK\,dx/c_K\) is

\[
 \boxed{
 S_\Gamma(x)
 =\frac{2}{c_K^3h(x)}\int_{\mathbb R}
 \frac{K(u)^2h(x-u)^2}
 {K(x-u)\widetilde r_\Gamma(u)}\,du.}             \tag{26}
\]

### Theorem 5 — Ambient reconstruction is unbounded

\[
 \boxed{\sup_{x\in\mathbb R}S_\Gamma(x)=\infty.} \tag{27}
\]

#### Proof

Fix \(0<u_0<u_1\).  On that interval \(K(u)\) and
\(\widetilde r_\Gamma(u)\) are bounded above and below by positive
constants.  As \(x\to+\infty\), uniformly for \(u\in[u_0,u_1]\),

\[
 h(x-u)^2\asymp e^{x-u},
 \]

while the first theta atom gives

\[
 K(x-u)\asymp
 e^{9(x-u)/2}\exp\{-\pi e^{2(x-u)}\}.             \tag{28}
\]

The contribution of \([u_0,u_1]\) to (26) is therefore bounded below by

\[
 C\,h(x)^{-1}e^{-7x/2}
 \exp\{\pi e^{2(x-u_1)}\},                        \tag{29}
\]

which tends to infinity.  Evenness gives the same conclusion at the
negative end. \(\square\)

The blow-up is caused by estimating arbitrary chord fields whose far-end
amplitude is unrelated to their near-end amplitude.  Physical chord fields
obey (9), all copy constraints (16), and the exact radical anti-short.
Accordingly, (27) does not falsify a compressed source-specific
contraction.  It proves that such a contraction must add a nonzero
\(\mathcal L^*Y\) correction before taking its norm.

## 6. Consequence for the constructive program

The new global information is now completely explicit:

1. mean periodicity is the chord reconstruction constraint (9);
2. literal arithmetic and the completed Archimedean source are the copy
   constraints (16);
3. every null-IQC freedom outside the physical range is eliminated by
   (5);
4. the raw reconstructor is unusable by Theorem 5.

Therefore the next admissible construction is not another ambient
multiplier.  It is an explicit arithmetic factorization of

\[
 \boxed{PJP}
 \tag{30}
\]

on the kernel of (9), obtained by modifying the global reconstructor with
the literal prime-copy equations before estimating.  Such a modification
must mix different chord lengths globally; any decomposable modification
is isometric by 106.144.  It must also retain Gamma and the pole until after
compression.  This is the exact finite-row object to be attacked next.
