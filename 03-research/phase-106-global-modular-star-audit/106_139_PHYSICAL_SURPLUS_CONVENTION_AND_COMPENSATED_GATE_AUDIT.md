# 106.139 — Physical-surplus convention and compensated-gate audit

## 1. Purpose

The boundary/KYP calculation and the original physical form are different
quadratic forms. This note fixes the convention once, tests the two fixed
Gamma-margin gates against the exact radical, and writes the nonlocal
quotient which remains after the complete anti-short.

The conclusions are as follows.

1. The original physical form is

   \[
   \mathfrak Q_{\rm phys}
   =\mathfrak P_{\rm PNT}+\mathfrak b_{\Gamma,*}.
   \]

   The connection-corrected KYP supply is a distinct form.
2. The gate obtained by spending a fixed fraction of Gamma,

   \[
   \mathfrak P_{\rm PNT}+\frac{499}{2000}
   \mathfrak b_{\Gamma,*}\geq0,
   \]

   is false on every nonconstant exact radical direction.
3. Adding the theta displacement energy produces the valid sufficient
   gate

   \[
   \mathfrak Q_{\rm suff}
   :=\mathfrak P_{\rm PNT}+2\mathfrak b_K
      +\frac{499}{2000}\mathfrak b_{\Gamma,*}.
   \]

   Nevertheless this gate is also strictly negative on every nonconstant
   exact radical direction. Therefore neither fixed-margin gate can be
   used before the **complete** radical anti-short, or on any merely finite
   radical short.
4. After the complete anti-short, a Schur-complement realization of either
   the original or the sufficient gate exists exactly when its canonical
   nonlocal transfer is contractive. Positivity of that block is therefore
   the desired sign, not a consequence of the already-proved Gamma
   absorption.

This note does not promote a numerical sign to a theorem. It isolates the
only quotient on which the heat/hybrid surplus can still be proved.

## 2. Sharp convention

For an even multiplier \(q\), put

\[
 J_u(q)=\int_{\mathbb R}K(x)K(x-u)
 |q(x)-q(x-u)|^2\,dx.                              \tag{1}
\]

The common PNT Stieltjes primitive of 106.138 is

\[
 \mathcal D(u)=
 \sum_{\log n\leq u}\frac{\Lambda(n)}{\sqrt n}
 -2(e^{u/2}-1),                                    \tag{2}
\]

and the convention used throughout this note is

\[
 \boxed{
 \mathfrak P_{\rm PNT}(q)
 =\mathfrak P_{\rm out}(q)+\mathfrak P_{\rm in}(q)
 =\int_{[0,\infty)}J_u(q)\,d\mathcal D(u).}       \tag{3}
\]

Equivalently,

\[
 \mathfrak P_{\rm PNT}(q)
 =\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
      J_{\log n}(q)
  -\int_0^\infty e^{u/2}J_u(q)\,du.               \tag{4}
\]

For an even nonnegative displacement density \(v\), write

\[
 \mathfrak b_v(q)=\int_0^\infty v(u)J_u(q)\,du.  \tag{5}
\]

In particular,

\[
 r_\Gamma(u)=\frac{e^{-5u/2}}{1-e^{-2u}},
 \qquad
 \mathfrak b_{\Gamma,*}=\mathfrak b_{r_\Gamma},
 \qquad
 \mathfrak b_K=\mathfrak b_{u\mapsto K(u)}.       \tag{6}
\]

The decomposition

\[
 \frac{e^{-u/2}}{1-e^{-2u}}
 -2\cosh(u/2)
 =r_\Gamma(u)-e^{u/2}                              \tag{7}
\]

then gives the original completed form

\[
 \boxed{
 \mathfrak Q_{\rm phys}(q)
 =\mathfrak P_{\rm PNT}(q)+\mathfrak b_{\Gamma,*}(q).}
                                                               \tag{8}
\]

By contrast, with \(F=hq\) and the physical Abel connection
\(\mathcal C\), the KYP supply is

\[
 \boxed{
 \mathfrak Q_{\rm KYP}(q)
 =\mathfrak Q_{\rm phys}(q)
  +2\operatorname {Re}\langle F,\mathcal CF\rangle_{\omega_K}.}
                                                               \tag{9}
\]

Equation (9) must not be substituted for (8) in the physical surplus.

## 3. The compensated sufficient gate

Set

\[
 \theta_*:=\frac{499}{2000},
 \qquad 1-\theta_*=\frac{1501}{2000}.              \tag{10}
\]

The pointwise theorem of 106.135 says

\[
 2K(u)<(1-\theta_*)r_\Gamma(u)\qquad(u>0).         \tag{11}
\]

Consequently the form

\[
 \mathfrak m_K(q)
 :=(1-\theta_*)\mathfrak b_{\Gamma,*}(q)
   -2\mathfrak b_K(q)                              \tag{12}
\]

is nonnegative. It is strictly positive for every nonconstant analytic
multiplier in the form domain: (11) is strict for every displacement, and
\(J_u(q)\) cannot vanish for almost every \(u>0\) unless \(q\) is constant.

Define

\[
 \boxed{
 \mathfrak Q_{\rm suff}(q)
 :=\mathfrak P_{\rm PNT}(q)
   +2\mathfrak b_K(q)
   +\theta_*\mathfrak b_{\Gamma,*}(q).}            \tag{13}
\]

Then the exact comparison is

\[
 \boxed{
 \mathfrak Q_{\rm phys}(q)-\mathfrak Q_{\rm suff}(q)
 =\mathfrak m_K(q)\geq0.}                         \tag{14}
\]

Thus \(\mathfrak Q_{\rm suff}\geq0\) is a valid sufficient condition for
the original surplus. It is weaker than the earlier fixed-margin gate

\[
 \mathfrak Q_{\rm old}
 =\mathfrak P_{\rm PNT}+\theta_*\mathfrak b_{\Gamma,*},
                                                               \tag{15}
\]

because \(\mathfrak Q_{\rm old}\leq\mathfrak Q_{\rm suff}\).

There is also an exact connection form of (13).  Put

\[
 \mathfrak D_K(q)
 :=\int_{\mathbb R}(K*K)(x)K(x)|q(x)|^2\,dx.
 \tag{15a}
\]

Equation (20) of 106.135 gives

\[
 2\mathfrak b_K(q)
 =2\mathfrak D_K(q)
  -2\operatorname {Re}\langle F,\mathcal CF\rangle_{\omega_K}.
 \tag{15b}
\]

Hence

\[
 \boxed{
 \mathfrak Q_{\rm suff}
 =\mathfrak P_{\rm PNT}
  -2\operatorname {Re}\langle F,\mathcal CF\rangle_{\omega_K}
  +2\mathfrak D_K+\theta_*\mathfrak b_{\Gamma,*}.}
 \tag{15c}
\]

The connection appears here with the sign opposite to the augmented KYP
supply (9).  Thus (15c) is a useful exact nonlocal coordinate, but it is
not the positive factorization of 106.135 and cannot inherit its sign.
The exact radical falsifier below rules out a global square before
anti-shorting; after complete anti-shorting, a positive-square
factorization is exactly the contractivity problem in Section 5.

## 4. Exact radical falsifier

Let \(r\) be a nonconstant vector in the exact Riemann radical. The full
kernel identity gives

\[
 \mathfrak Q_{\rm phys}(r)=0.                     \tag{16}
\]

The Gamma-remainder displacement density is strictly positive for every
\(u>0\), so

\[
 \mathfrak b_{\Gamma,*}(r)>0.                     \tag{17}
\]

Equations (15)--(17) give

\[
 \boxed{
 \mathfrak Q_{\rm old}(r)
 =-(1-\theta_*)\mathfrak b_{\Gamma,*}(r)<0.}       \tag{18}
\]

Likewise, (12), (14), and (16) give

\[
 \boxed{
 \mathfrak Q_{\rm suff}(r)=-\mathfrak m_K(r)<0.} \tag{19}
\]

This is an exact obstruction, not a numerical one. If only a finite
radical space \(\mathcal R_J\) has been shorted, choose a nonzero radical
combination orthogonal to \(\mathcal R_J\). Equations (18)--(19) remain
valid. Hence neither gate can close a finite-short staircase uniformly.
They become admissible questions only after projection onto

\[
 \mathscr C=(\mathbf 1\oplus\mathcal R)^\perp.     \tag{20}
\]

## 5. Exact nonlocal quotient after complete anti-shorting

Let \(Q\) be the orthogonal projection onto \(\mathscr C\). Introduce
closed gradients by

\[
\begin{aligned}
 \|G_pq\|^2
   &=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
        J_{\log n}(q),\\
 \|G_{\Gamma,*}q\|^2
   &=\mathfrak b_{\Gamma,*}(q),\\
 \|G_Kq\|^2&=\mathfrak b_K(q),\\
 \|G_0q\|^2&=\int_0^\infty e^{u/2}J_u(q)\,du.
\end{aligned}                                      \tag{21}
\]

The original and sufficient positive source maps are

\[
 G_{\rm phys}q=G_pq\oplus G_{\Gamma,*}q,           \tag{22}
\]

and

\[
 G_{\rm suff}q
 =G_pq\oplus\sqrt{\theta_*}G_{\Gamma,*}q
       \oplus\sqrt2G_Kq.                           \tag{23}
\]

On the corresponding gradient ranges define the canonical transfers

\[
 T_{\rm phys}(G_{\rm phys}Qq)=G_0Qq,
 \qquad
 T_{\rm suff}(G_{\rm suff}Qq)=G_0Qq.              \tag{24}
\]

The positive Gamma-remainder channel has every displacement, so the only
common null vectors are constants; after (20), both maps are well defined.
Their exact gains are

\[
\boxed{
 \|T_{\rm phys}\|^2
 =\sup_{0\ne q\in\mathscr C}
 {\displaystyle\int_0^\infty e^{u/2}J_u(q)\,du
  \over
  \displaystyle\sum_{n\ge2}\Lambda(n)n^{-1/2}J_{\log n}(q)
       +\mathfrak b_{\Gamma,*}(q)},}              \tag{25}
\]

and

\[
\boxed{
 \|T_{\rm suff}\|^2
 =\sup_{0\ne q\in\mathscr C}
 {\displaystyle\int_0^\infty e^{u/2}J_u(q)\,du
  \over
  \displaystyle\sum_{n\ge2}\Lambda(n)n^{-1/2}J_{\log n}(q)
       +2\mathfrak b_K(q)
       +\theta_*\mathfrak b_{\Gamma,*}(q)}.}      \tag{26}
\]

Therefore

\[
 \boxed{
 \mathfrak Q_{\rm phys}\geq0\text{ on }\mathscr C
 \iff \|T_{\rm phys}\|\leq1,}                    \tag{27}
\]

and

\[
 \boxed{
 \mathfrak Q_{\rm suff}\geq0\text{ on }\mathscr C
 \iff \|T_{\rm suff}\|\leq1.}                    \tag{28}
\]

This is the exact nonlocal quotient. No sign has been assigned in
(25)--(28).

## 6. Schur-complement audit

On a finite heat or hybrid row, let

\[
 A_+=G_{\rm suff}^*G_{\rm suff},
 \qquad B_0=G_0^*G_0.                             \tag{29}
\]

Then

\[
 \mathfrak Q_{\rm suff}[q]=\langle q,(A_+-B_0)q\rangle.       \tag{30}
\]

The canonical block realization is

\[
 \mathbb S=
 \begin{pmatrix}
 A_+&G_0^*\\
 G_0&I
 \end{pmatrix}.                                   \tag{31}
\]

Its Schur complement with respect to the lower-right identity is precisely
\(A_+-B_0\). Hence

\[
 \boxed{
 \mathbb S\succeq0
 \iff A_+-B_0\succeq0
 \iff \|T_{\rm suff}\|\leq1.}                    \tag{32}
\]

The same statement on the closed range is Douglas factorization:
\(G_0=T G_{\rm suff}\) with \(\|T\|\leq1\) exists if and only if
\(B_0\preceq A_+\). Thus (31) is an exact Schur-complement realization,
but it is not positive for free. Proving its positivity is already the
sufficient surplus theorem. The Gamma absorption of 106.135 proves the
separate KYP identity (9); it does not prove (32).

## 7. Relation with the literal staircase

For the completed radical-conditioned residual \(q_J^*\) of
106.89--106.92,

\[
 \boxed{
 G_J-\delta_J
 =\mathfrak Q_{\rm phys}(q_J^*).}                 \tag{33}
\]

Moreover,

\[
 \mathfrak C_J(Y)=\frac{\tau_{d+1}(Y)}{\tau_d(Y)}
 \mathrel{\nearrow} G_J.                          \tag{34}
\]

Consequently the exact finite crossing remains

\[
 \tau_{d+1}(Y)>\delta_J\tau_d(Y)                  \tag{35}
\]

for some finite literal prime cutoff. Replacing (33) by
\(\mathfrak Q_{\rm suff}(q_J^*)\geq0\) would be a sufficient but strictly
stronger assertion, and (19) proves that it is incompatible with every
finite radical short.

## 8. Floating-point falsification diagnostics

The script

    python3 tools/physical_sufficient_gate_diagnostic.py

uses the literal prime powers and a common displacement grid. On

\[
 q_{\gamma_1}(x)=\frac{\cos(\gamma_1x)}{\cosh(x/2)},
 \qquad \gamma_1=14.134725\ldots,                  \tag{36}
\]

the stable double-precision values at \(dx=10^{-3}\), \(x_{\max}=4\) are

\[
\begin{array}{c|r}
\mathfrak Q_{\rm phys}/\|q_{\gamma_1}\|^2& 0.2733958\ldots\\
\mathfrak Q_{\rm old}/\|q_{\gamma_1}\|^2&-0.1094824\ldots\\
\mathfrak Q_{\rm suff}/\|q_{\gamma_1}\|^2&0.1442128\ldots
\end{array}                                        \tag{37}
\]

Thus the old fixed-margin gate already fails on the first exact
mean-periodic mode. These values are diagnostic, not interval-certified.

The second script

    python3 tools/sufficient_gate_zero_span_diagnostic.py --span 8

performs weighted QR on the first critical-line modes. It finds a stable
negative eigenvalue about \(-2.84\times10^{-2}\) for
\(\mathfrak Q_{\rm suff}\) on the first four-mode span, while the original
physical form has a positive diagnostic margin about \(6.40\times10^{-2}\).

This is not merely an optimizer-dependent observation.  The fixed integer
combination

\[
 q_*(x)=\frac{
  4\cos(\gamma_1x)-15\cos(\gamma_2x)
  +16\cos(\gamma_3x)-5\cos(\gamma_4x)}{\cosh(x/2)}
 \tag{38}
\]

lies in the complete radical complement by 106.41--106.43.  Running the
same calculation at four mesh sizes gives

\[
\begin{array}{c|r|r|r|r}
 dx&\|q_*\|^2&\mathfrak Q_{\rm phys}(q_*)&
 \mathfrak Q_{\rm suff}(q_*)&
 \mathfrak Q_{\rm suff}(q_*)/\|q_*\|^2\\ \hline
 0.0040&46.0478787807&3.1715933377&-1.3038177331&-0.0283143929\\
 0.0020&46.0478787807&3.1745008900&-1.3017883043&-0.0282703208\\
 0.0010&46.0478787807&3.1754096671&-1.3010990400&-0.0282553524\\
 0.0005&46.0478787807&3.1755453793&-1.3010182049&-0.0282535969
\end{array}                                             \tag{39}
\]

The fixed vector and the large negative margin make (38) a natural target
for an outward-interval falsification certificate.  Table (39) is still a
floating-point diagnostic: the zero ordinates, theta truncation, spatial
tails, prime tail, and quadrature error have not yet been enclosed.
Therefore the compensated gate should not be adopted on the complete
anti-short without that finite interval audit; current diagnostics indicate
that it is too strong there.

## 9. Exact audit of a row-adaptive Gamma reserve

The failure of the fixed reserve suggests allowing its coefficient to
depend on the complete anti-shorted heat/hybrid row.  This does not create
a weaker intermediate target.

Put

\[
 w_\Gamma(u):=r_\Gamma(u)-2K(u)>0,
 \qquad
 \mathfrak W:=\mathfrak b_{w_\Gamma},
 \qquad
 \mathfrak B:=\mathfrak P_{\rm PNT}+2\mathfrak b_K.
 \tag{40}
\]

Then the physical form has the exact split

\[
 \boxed{\mathfrak Q_{\rm phys}=\mathfrak B+\mathfrak W.}
 \tag{41}
\]

Let \(E\subset\mathscr C\) be a finite-dimensional completely
anti-shorted heat or hybrid row.  The matrix \(W_E\) of
\(\mathfrak W|_E\) is positive definite: its displacement density is
strictly positive and its only null vectors are constants, which do not
belong to \(\mathscr C\).  Define the optimal row-adaptive loss by

\[
 \kappa_E
 :=\sup_{0\ne q\in E}
   \frac{[-\mathfrak B(q)]_+}{\mathfrak W(q)}
 =\max\left\{0,-\lambda_{\min}
 \bigl(W_E^{-1/2}B_EW_E^{-1/2}\bigr)\right\}.
 \tag{42}
\]

### Proposition 3 --- Adaptive reserve equals the physical surplus

For every such row,

\[
 \boxed{
 \kappa_E\le1
 \quad\Longleftrightarrow\quad
 B_E+W_E\succeq0
 \quad\Longleftrightarrow\quad
 \mathfrak Q_{\rm phys}\ge0\text{ on }E.}
 \tag{43}
\]

If \((E_j)\) is a heat-form-core exhaustion of \(\mathscr C\), then

\[
 \boxed{
 \sup_j\kappa_{E_j}\le1
 \quad\Longleftrightarrow\quad
 \mathfrak Q_{\rm phys}\ge0\text{ on }\mathscr C.}
 \tag{44}
\]

#### Proof

For \(q\in E\), (41) is nonnegative exactly when

\[
 -\mathfrak B(q)\le\mathfrak W(q).
\]

If the left side is nonpositive there is no restriction; otherwise this
is precisely the quotient in (42) being at most one.  Conjugating the
matrix inequality \(B_E+W_E\succeq0\) by \(W_E^{-1/2}\) gives the spectral
formula in (42), proving (43).  If (44) holds, (43) gives nonnegativity on
the union of the rows, and closedness of the physical form extends it to
their form-core closure.  The converse follows by restriction. \(\square\)

The test is sharp against both known boundary mechanisms.  Before the
complete anti-short, every nonconstant exact radical vector satisfies

\[
 \mathfrak B(r)=-\mathfrak W(r),
 \tag{45}
\]

and hence saturates \(\kappa=1\).  Conversely, if a post-short vector
satisfies

\[
 \mathfrak Q_{\rm phys}(q)=-\delta\|q\|^2,
 \qquad \delta>0,
\]

then

\[
 \frac{-\mathfrak B(q)}{\mathfrak W(q)}
 =1+\frac{\delta\|q\|^2}{\mathfrak W(q)}>1.
 \tag{46}
\]

Thus heat localization cannot average away a subthreshold direction: its
row-adaptive gain remains larger than one as the heat row concentrates on
that direction.

There is a tempting but invalid strengthening.  If \(B_-\) denotes the
negative part of \(B\), the inequality \(B_-\preceq W\) implies
\(B+W\succeq0\), but the converse is false because the positive part of
\(B\) can compensate through noncommuting directions.  The exact matrices

\[
 B=\begin{pmatrix}-1&0\\0&1\end{pmatrix},
 \qquad
 W=\begin{pmatrix}2&2/5\\2/5&1/10\end{pmatrix}
 \tag{47}
\]

satisfy

\[
 \det W=\frac1{25}>0,
 \qquad
 \det(B+W)=\frac{47}{50}>0,
 \qquad
 \det(W-B_-)=-\frac3{50}<0.
 \tag{48}
\]

Therefore a proof based on separate domination of the operator negative
part would impose a genuinely stronger and false abstract inference.  The
only exact adaptive statement is (43), which is the canonical contraction
already isolated in (27).

## 10. Result

The sharp convention is now fixed:

\[
 \mathfrak Q_{\rm phys}
 =\mathfrak P_{\rm out}+\mathfrak P_{\rm in}
  +\mathfrak b_{\Gamma,*}.
\]

The \(499/2000\) gate and its \(2\mathfrak b_K\)-compensated variant are
valid sufficient comparisons, but exact radical saturation prevents either
from closing any finite-short staircase. The latter has an exact Schur
realization only in the taut but useful sense (32): its positivity is the
contractivity being sought.

Accordingly the force-bearing heat/hybrid statement remains the unit-gain
bound (25), equivalently the literal surplus (33). Future estimates must
act on that complete nonlocal quotient; neither the KYP form nor a fixed
Gamma margin may be substituted for it.  A row-adaptive Gamma fraction
does not weaken this statement: its optimal constant is exactly the
generalized eigenvalue (42), and the bound \(\kappa_E\le1\) is precisely
the physical surplus on that row.
