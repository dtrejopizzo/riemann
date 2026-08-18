# 106.128 — Covariant cyclic triangles and the holonomy gate

## 1. Purpose and verdict

Documents 106.50 and 106.51 give the exact scalar triangle and Bochner
identities for the complete ordinary-prime--Gamma generator.  Document
106.125 shows that a second variation does not descend through the complete
Riemann radical unless the radical projector is differentiated as well.
This note combines those two facts.

The result is exact and negative for the proposed square factorization.

1.  A unitary edge connection gives a covariant cyclic identity.  Its
    cyclic cross term is

    \[
      -\frac12\{\text{covariant perimeter}\}
      +\frac12\{\text{triangle holonomy square}\}.
      \tag{1}
    \]

2.  With the physical factor \(h=\cosh(x/2)\), (1) acquires an additional
    signed edge-divergence term.  That term is present even for the flat
    physical translation connection.
3.  The polar transport which aligns the threshold-radical evaluation
    lines is flat on those lines.  It therefore supplies no holonomy
    curvature.  Replacing the physical connection by this aligned
    transport changes the generator, and the exact change in the curvature
    is

    \[
       LB+BL+B^2-\frac12B,
       \qquad B=L^{U}-L.                              \tag{2}
    \]

    This is signed.
4.  The infinitesimal version of (2) is exactly the radical-connection term
    in the covariant Hessian of 106.125.  It cancels the raw positive
    second Euler jet on exact threshold-radical vectors and therefore
    cannot be omitted or assigned a favorable sign separately.
5.  A three-state reversible model with an exact constant mode, an exact
    \(1/2\)-threshold radical and a reducing \(1/6\)-mode gives the smallest
    exact countertest.  Its radical correlations are negative on both
    physical edges and reproduce the full negative surplus.

Thus an edge connection does not convert the joint physical surplus into a
free Hilbert square.  A flat connection retains the signed rate variation;
an aligning connection moves the same sign into the connection mismatch.
The literal product, ratio, prime--Gamma, Gamma--Gamma and threshold
channels must still dominate that mismatch jointly.

No assertion about the sign of the literal Riemann surplus is made.

## 2. Complete finite-cutoff setting after radical anti-shorting

Use the common finite source cutoff

\[
 d\nu_{\varepsilon,N}(u)
 =\mathbf 1_{[\varepsilon,\varepsilon^{-1}]}(u)
   \frac{e^{-u/2}}{1-e^{-2u}}\,du
  +\sum_{2\le n\le N}\frac{\Lambda(n)}{\sqrt n}
       \delta_{\log n}(du).                         \tag{3}
\]

An oriented move is \(s=\sigma u\), \(\sigma\in\{\pm1\}\), and its
Doob rate is

\[
 c_s(x)=\frac{c_KK(x+s)}{h(x)}.                     \tag{4}
\]

Let \(P\) be a finite reducing heat or hybrid row after the exact radical
anti-short, and let

\[
 \mathbf Q(x)=(q_1(x),\ldots,q_m(x)),
 \qquad
 q_j\perp\mathbf1\oplus\mathcal R.                 \tag{5}
\]

The anti-short in (5) is global.  There is no additional pointwise radical
projection which may be inserted into an edge or a triangle.  With

\[
\begin{aligned}
 a_s(x)&=\mathbf Q(x+s)-\mathbf Q(x),\\
 b_{s,t}(x)&=\mathbf Q(x+s+t)-\mathbf Q(x+s)
             -\mathbf Q(x+t)+\mathbf Q(x),
\end{aligned}                                       \tag{6}
\]

the exact finite-cutoff curvature is the expression 106.51(16):

\[
\begin{aligned}
 \mathfrak T_{\varepsilon,N}(P)
={}&\frac14\int\sum_{s,t}c_s(x)c_t(x)
       \|b_{s,t}(x)\|^2\,d\mu_K(x)\\
 &+\frac14\int\sum_{s,t}c_s(x)
       \{c_t(x+s)-c_t(x)\}\\
 &\qquad\times
   \{\|a_t(x+s)-a_s(x)\|^2-\|a_s(x)\|^2\}
       \,d\mu_K(x)\\
 &-\frac14\int\sum_s c_s(x)\|a_s(x)\|^2
       \,d\mu_K(x)\\
={}&\operatorname {Tr}P(L_{\varepsilon,N}^2
                      -\tfrac12L_{\varepsilon,N}).
                                                               \tag{7}
\end{aligned}
\]

Every term below is only a reorganization of (7).  In particular, no
component of (7) is declared positive merely from the positivity of its
arithmetic coefficient.

## 3. Exact covariant cyclic identity

Let \(x_0,x_1,x_2\) be the vertices of an oriented triangle.  Let
\(\mathcal H_i\) be Hilbert fibers and let

\[
 U_{ij}:\mathcal H_j\longrightarrow\mathcal H_i,
 \qquad U_{ji}=U_{ij}^*,                            \tag{8}
\]

be unitary edge transports.  For a section \(Q_i\in\mathcal H_i\), put

\[
 d_{ij}^UQ=Q_i-U_{ij}Q_j.                           \tag{9}
\]

At the base vertex \(x_0\), define

\[
\begin{aligned}
 A_0(Q)&=d_{01}^UQ,\\
 A_1(Q)&=U_{01}d_{12}^UQ,\\
 A_2(Q)&=U_{01}U_{12}d_{20}^UQ,
\end{aligned}                                       \tag{10}
\]

and define the triangle holonomy

\[
 H_0=U_{01}U_{12}U_{20}.                            \tag{11}
\]

### Theorem 1 — Covariant perimeter--holonomy identity

For every section \(Q\),

\[
 \boxed{
 \operatorname {Re}\sum_{0\le i<j\le2}
       \langle A_i(Q),A_j(Q)\rangle
 =-\frac12\sum_{i=0}^2\|d_{i,i+1}^UQ\|^2
  +\frac12\|(I-H_0)Q_0\|^2.}                      \tag{12}
\]

Indices are read modulo three.

#### Proof

The three transported differences telescope up to holonomy:

\[
 A_0(Q)+A_1(Q)+A_2(Q)=(I-H_0)Q_0.                  \tag{13}
\]

Expanding the squared norm of the two sides of (13), and using unitarity
to identify \(\|A_i(Q)\|\) with the corresponding edge norm, gives
(12). \(\square\)

For a flat connection, \(H_0=I\), and (12) is exactly the negative
triangle-perimeter identity used in 106.50.  A nonflat connection adds a
positive holonomy square, but it does not yet account for the physical
weight \(h\).

## 4. The weighted identity and its signed divergence

For a positive scalar weight \(h_i\), apply (10) both to \(Q\) and to the
section \((hQ)_i=h_iQ_i\).  Define the symmetrized cyclic cross term

\[
 \mathcal C_{h,U}^{(0)}(Q)
 =\frac12\operatorname {Re}
   \sum_{i\ne j}\langle A_i(hQ),A_j(Q)\rangle.      \tag{14}
\]

The ordered move sum in (7) contains both orders \((s,t)\) and \((t,s)\).
Therefore its cyclic polarization is precisely the symmetrized expression
(14), rather than one arbitrarily chosen orientation.

### Theorem 2 — Weighted covariant cyclic identity

At the base vertex \(x_0\),

\[
\boxed{
\begin{aligned}
 \mathcal C_{h,U}^{(0)}(Q)
={}&\frac{h_0}{2}\|(I-H_0)Q_0\|^2\\
 &-\frac14\sum_{i=0}^2(h_i+h_{i+1})
       \|d_{i,i+1}^UQ\|^2\\
 &-\frac14\sum_{i=0}^2(h_i-h_{i+1})
       \{\|Q_i\|^2-\|Q_{i+1}\|^2\}.
                                                               \tag{15}
\end{aligned}}
\]

After averaging (15) over the three choices of base vertex,

\[
\boxed{
\begin{aligned}
 \overline{\mathcal C}_{h,U}(Q)
={}&\frac16\sum_{i=0}^2h_i\|(I-H_i)Q_i\|^2\\
 &-\frac14\sum_{i=0}^2(h_i+h_{i+1})
       \|d_{i,i+1}^UQ\|^2\\
 &-\frac14\sum_{i=0}^2(h_i-h_{i+1})
       \{\|Q_i\|^2-\|Q_{i+1}\|^2\}.
                                                               \tag{16}
\end{aligned}}
\]

#### Proof

By (13),

\[
 \sum_iA_i(hQ)=h_0(I-H_0)Q_0,
 \qquad
 \sum_iA_i(Q)=(I-H_0)Q_0.                          \tag{17}
\]

Subtracting the diagonal terms from the inner product of the two sums
gives

\[
 \mathcal C_{h,U}^{(0)}(Q)
 =\frac{h_0}{2}\|(I-H_0)Q_0\|^2
  -\frac12\sum_i
    \operatorname {Re}\langle
      d_{i,i+1}^U(hQ),d_{i,i+1}^UQ\rangle.          \tag{18}
\]

For one edge, unitarity gives

\[
\begin{aligned}
 \operatorname {Re}\langle d_{ij}^U(hQ),d_{ij}^UQ\rangle
={}&\frac{h_i+h_j}{2}\|d_{ij}^UQ\|^2\\
 &+\frac{h_i-h_j}{2}
   \{\|Q_i\|^2-\|Q_j\|^2\}.                      \tag{19}
\end{aligned}
\]

Substitute (19) in (18) to obtain (15).  Averaging over the three
basepoints gives (16). \(\square\)

The third line of (15)--(16) is the exact obstruction to a perimeter-only
factorization.  It is a signed divergence of the physical weight and the
pointwise cluster density.  In the Doob calculation this is the same
center variation which appears as

\[
 c_t(x+s)-c_t(x)
 =c_K\left\{\frac{K(x+s+t)}{h(x+s)}
             -\frac{K(x+t)}{h(x)}\right\}.          \tag{20}
\]

It is not a holonomy square.

## 5. Channel audit for ordinary primes, Gamma and the threshold

Use the physical flat transport \(U_{ij}=I\).  Then every \(H_i=I\), so
the first line of (16) vanishes identically.  Integrating the remaining
two lines against the common ordered two-move measure in (7) gives four
distinct classes.

* If both moves are ordinary prime-power moves, opposite orientations
  have neighbor separation

  \[
    \log m+\log n=\log(mn),                         \tag{21}
  \]

  and their ordered coefficient groups as

  \[
    \sum_{mn=r}\Lambda(m)\Lambda(n)
    =(\Lambda*\Lambda)(r).                          \tag{22}
  \]

* Equal orientations have separation

  \[
     \left|\log\frac mn\right|,                    \tag{23}
  \]

  and form the ratio channel.  It does not group by Dirichlet
  convolution.
* A prime-power move and a Gamma move give both

  \[
     |\log n-u|\quad\hbox{and}\quad\log n+u.        \tag{24}
  \]

  These are the prime--Gamma channels.
* Two Gamma moves give \(|u-v|\) and \(u+v\).  The single-move last line
  of (7) is the polar-threshold subtraction.

The logarithmic coefficient \(\delta\Lambda\) occurs through the rate
variation (20), not through (22).  Consequently the positive coefficient

\[
 j_2=\delta\Lambda+\Lambda*\Lambda                 \tag{25}
\]

accounts for only one grouped part of the complete cyclic expression.
The ratio, mixed, continuous and threshold pieces remain in (7), and the
signed divergence in (16) is their common spatial coupling.  Formula
(16) therefore refines the gate in 106.50: even after the radical has been
removed globally, the literal weighted cyclic perimeter is not a sum of
nonnegative squares.

## 6. Smallest pointwise physical-weight countertest

The failure is already visible in one exact even triangle.  Take

\[
 x_0=0,
 \qquad x_1=\log2,
 \qquad x_2=-\log2,
 \tag{26}
\]

so that

\[
 h_0=1,
 \qquad h_1=h_2=b:=\cosh\!\left(\frac{\log2}{2}\right)
 =\frac{3}{2\sqrt2}>1.                              \tag{27}
\]

Use the flat connection and a real-even scalar feature with

\[
 Q_1=Q_2=1,
 \qquad Q_0=\frac{1+b}{2}.                          \tag{28}
\]

Direct substitution in (16) gives

\[
 \boxed{
 \overline{\mathcal C}_{h,I}(Q)
 =(Q_0-Q_1)(bQ_1-Q_0)
 =\frac{(b-1)^2}{4}
 =\frac{17-12\sqrt2}{32}>0.}                       \tag{29}
\]

For constant \(h\), the same cyclic expression is minus one half of the
perimeter.  Equation (29) proves that the actual physical \(h\)-weight
can reverse that sign.  It rules out a pointwise weighted-perimeter square.
It is not a counterexample to the globally integrated Riemann inequality:
the literal rate measure and the global mean-periodic constraint have not
been imposed in this three-point interpolation.

## 7. Why polar edge alignment does not repair the identity

Let \(\mathcal V(x)\) be a finite or regularized infinite threshold-radical
evaluation vector and put

\[
 \Phi(x)=\frac{\mathcal V(x)}{\|\mathcal V(x)\|}
 \tag{30}
\]

where it is nonzero.  The canonical line transport is the rank-one partial
isometry

\[
 T_{xy}=|\Phi(x)\rangle\langle\Phi(y)|.             \tag{31}
\]

It aligns the evaluation lines, but on those lines it is exactly flat:

\[
 \boxed{T_{xy}T_{yz}=T_{xz}.}                       \tag{32}
\]

Thus the attractive polar alignment produces no triangle holonomy at all.
Any unitary extension of (31) to the orthogonal complements is nonunique;
its holonomy depends on that arbitrary extension and cannot be identified
canonically with the fixed arithmetic coefficient (25).

There is a more invariant obstruction.  If \(V_x\) is a pointwise unitary
gauge and

\[
 Q_x'=V_xQ_x,
 \qquad U_{xy}'=V_xV_y^*,                           \tag{33}
\]

then \(U'\) is flat and

\[
 \operatorname {Re}\langle Q_x',U_{xy}'Q_y'\rangle
 =\operatorname {Re}\langle Q_x,Q_y\rangle.        \tag{34}
\]

Therefore a genuine gauge does not change any negative radical
correlation.  This is the edge-transport version of the zero-mean
correlation obstruction proved in detail in 106.129.

To change the sign one must choose a transport which is not the physical
flat connection.  Let \(L^U\) be the generator obtained by replacing
every physical difference \(Q_x-Q_y\) by \(Q_x-U_{xy}Q_y\), and put

\[
 B_U=L^U-L.                                         \tag{35}
\]

Write \(d\mathfrak j(x,y)\) for the symmetric edge measure, normalized so
that

\[
 \mathscr E(Q)=\frac12\iint\|Q_x-Q_y\|^2
                    \,d\mathfrak j(x,y).
\]

At the form level the exact change is

\[
\boxed{
 \mathscr E^U(Q)-\mathscr E(Q)
 =\iint\operatorname {Re}
   \langle Q_x,(I-U_{xy})Q_y\rangle
   \,d\mathfrak j(x,y),}                           \tag{36}
\]

with the usual one-half convention absorbed in the symmetric edge
measure.  At the curvature level,

\[
\boxed{
 (L^U)^2-\frac12L^U-\left(L^2-\frac12L\right)
 =LB_U+B_UL+B_U^2-\frac12B_U.}                      \tag{37}
\]

The right side of (36)--(37) is signed.  It contains the two-step products,
the ratio terms and all mixed channels whenever \(U\) is used on the
complete source.  Polar alignment has therefore moved the missing sign
into \(B_U\); it has not removed it.

## 8. Minimal reducing countertest

The preceding obstruction has a smallest exact reversible realization.
Let

\[
 \mathcal H=\mathbb R^3,
 \qquad
 \langle f,g\rangle_\mu=\frac13\sum_{i=1}^3f_ig_i,
 \tag{38}
\]

and

\[
 L=\frac16
 \begin{pmatrix}
 1&-1&0\\
 -1&2&-1\\
 0&-1&1
 \end{pmatrix}.                                    \tag{39}
\]

The normalized vectors

\[
 \mathbf1=(1,1,1),
 \qquad
 q=\sqrt{\frac32}(1,0,-1),
 \qquad
 r=\frac1{\sqrt2}(1,-2,1)                          \tag{40}
\]

satisfy

\[
 L\mathbf1=0,
 \qquad Lq=\frac16q,
 \qquad Lr=\frac12r.                               \tag{41}
\]

Thus \(r\) is an exact centered threshold radical and \(q\) is an exact
reducing subthreshold row orthogonal to it.  Put

\[
 a_i=\frac{q_i}{r_i}=(\sqrt3,0,-\sqrt3).            \tag{42}
\]

The two unoriented edge conductances are \(1/18\), and

\[
 r_1r_2=r_2r_3=-1.                                  \tag{43}
\]

The exact threshold Picone identity is therefore

\[
\begin{aligned}
 \langle q,(L-\tfrac12)q\rangle_\mu
 &=\frac1{18}\sum_{i=1}^2r_ir_{i+1}
       (a_i-a_{i+1})^2\\
 &=-\frac{3+3}{18}=-\frac13.                       \tag{44}
\end{aligned}
\]

Multiplication by the reducing eigenvalue gives

\[
 \boxed{
 \langle q,L(L-\tfrac12)q\rangle_\mu=-\frac1{18}.} \tag{45}
\]

Replacing the two correlations in (43) by their absolute values changes
the right side of (44) from \(-1/3\) to \(+1/3\).  The exact connection
cost is therefore \(2/3\), and restoring it gives (44), not a positive
square.  Three states are minimal: a model containing distinct eigenvalues
\(0\), \(\alpha\in(0,1/2)\), and \(1/2\) must have dimension at least
three.

This model does not have Riemann's theta placement.  It proves the precise
logical point that reduction, threshold radicality and an edge connection
do not determine the surplus sign.  Any successful argument must use a
literal arithmetic domination of the connection cost.

## 9. Infinitesimal connection and the covariant radical Hessian

Let \(b\mapsto\mathcal R_b\) be the moving complete radical bundle in a
finite common cutoff, and let \(V_b\mathcal R_0=\mathcal R_b\) be a
differentiable unitary trivialization.  Put

\[
 X_b=V_b^*V_b',
 \qquad Q_0=I-P_{\mathcal R_0},
 \qquad
 \mathcal A_b=L_b^2-\frac12L_b.                    \tag{46}
\]

Document 106.125 gives the exact covariant Hessian

\[
\boxed{
 \nabla^2\mathcal A
 =Q_0\{\mathcal A''+2[\mathcal A',X]
       +[[\mathcal A,X],X]+[\mathcal A,X']\}Q_0.}  \tag{47}
\]

The raw part is

\[
 \mathcal A''
 =L''L+2(L')^2+LL''-\frac12L''.                    \tag{48}
\]

For the multiplicative deformation, \(L''\) contains the logarithmic
Euler jet and \((L')^2\) contains the two-step product channel.  Equations
(21)--(24) show that their spatial realization also contains the ratio and
the prime--Gamma/Gamma--Gamma terms.  The remaining part

\[
\boxed{
 \mathcal K_X
 =Q_0\{2[\mathcal A',X]+[[\mathcal A,X],X]
             +[\mathcal A,X']\}Q_0}                \tag{49}
\]

is the infinitesimal connection mismatch.

If \(\mathcal A_b\mathcal R_b=0\) for all \(b\), then

\[
 (\mathcal A''+\text{the connection terms})r=0
 \qquad(r\in\mathcal R_0),                         \tag{50}
\]

whereas the raw positive \(j_2\) translation energy is strictly positive
on nonzero radical vectors by 106.60 and 106.125.  Hence (49) is forced to
cancel that raw positive contribution on the threshold.  It has no
separate nonnegative sign.

Equations (37) and (49) are the finite and infinitesimal forms of the same
missing term.

## 10. Port-Hamiltonian interpretation and the Abel boundary port

Formula (16) has a direct power-balance interpretation.  The edge storage
metric is not spatially constant: it is weighted by (h_i).  The second
line of (16) is the dissipative covariant perimeter, whereas

\[
 \mathfrak P_{\rm bulk}(Q)
 :=-\frac14\sum_i(h_i-h_{i+1})
       \{\|Q_i\|^2-\|Q_{i+1}\|^2\}                 \tag{51}
\]

is the bulk/boundary power created by transport through that nonuniform
storage metric.  It is a discrete port term, not dissipation.  This is why
it has no pointwise sign and why replacing it by a positive square changes
the physical system.

At the positive theta end, document 106.127 performs the corresponding
common-cutoff summation by parts for the literal prime source.  Its
normalized moving-Abel identity gives the incoming port

\[
 \mathcal F_D[q](x)
 =\int_{-\infty}^xD(e^{x-y})e^{-y/2}
   \{(Kq)'(y)+\tfrac12K(y)q(y)\}\,dy,               \tag{52}
\]

where

\[
 D(T)=\frac{\psi(T)-T+1}{T}.                        \tag{53}
\]

The associated Hermitian power is the signed Abel flux

\[
\begin{aligned}
 \mathcal P_D(q)
 =-2\operatorname {Re}\int_{x>y}
 &D(e^{x-y})e^{(x-y)/2}\overline{K(x)q(x)}\\
 &\times\{(Kq)'(y)+\tfrac12K(y)q(y)\}\,dy\,dx.
                                                               \tag{54}
\end{aligned}
\]

Equations (20) and (51) are the finite-cutoff bulk rate-variation port.
Equations (52)--(54) are its literal boundary-flux coordinate after the
prime continuum has been cancelled jointly with the leading Gamma channel.
They must be paired before taking a sign.  In particular, a closing
port-Hamiltonian estimate would have to control, on the transported
complete radical complement, the single combined power

\[
 \boxed{
 \mathfrak P_{\rm bulk}
 +\mathcal P_D
 +\mathfrak b_{\Gamma,*}
 +\mathfrak M_U,}                                   \tag{55}
\]

where (mathfrak M_U) is the connection mismatch (36)--(37) and
(mathfrak b_{Gamma,*}) is the positive completed Gamma remainder of
106.127.  Neither (mathfrak P_{\rm bulk}) nor (mathcal P_D) may be
replaced by its absolute value: doing so destroys the common prime phase
and returns to the loss in 106.118.

Thus the connection calculation and the theta-boundary calculation meet at
one exact engineering object: a signed supply rate.  The still-unproved
statement is passivity of that supply rate on physical heat/hybrid rows,
not positivity of its individual bulk or boundary ports.

## 11. Result

The complete covariant cyclic calculation is

\[
 \boxed{
 \text{weighted cyclic cross}
 =-\text{weighted covariant perimeter}
  +\text{holonomy square}
  +\text{signed }h\text{-divergence}.}              \tag{56}
\]

For the physical flat translation connection the holonomy square is zero,
and the signed divergence is exactly the rate-variation channel which must
be combined with \(\delta\Lambda\), Gamma and the polar threshold.  The
product channel \(\Lambda*\Lambda\) does not remove the ratio or mixed
channels.

The canonical polar transport of the threshold evaluation line is also
flat.  Using it in place of the physical connection changes the generator,
and the exact signed price is (37), or (49) after differentiating the
complete radical anti-short.  The three-state calculation (44)--(45) shows
that this price can carry the entire negative surplus.

Therefore the weighted cyclic perimeter does **not** factor as a
nonnegative square on reducing heat/hybrid rows by connection algebra
alone.  The remaining possible theorem is a literal ordinary-prime--Gamma
domination of the signed connection mismatch after the exact radical
anti-short.  That is a new inequality; it is not supplied by holonomy,
coefficient positivity of \(j_2\), or threshold saturation.
