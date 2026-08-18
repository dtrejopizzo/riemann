# 106.68 — The maximal anti-short and tail-distance gate

## Purpose and verdict

Every proper finite prime head is strictly negative on the exact Riemann
radical, so the ordinary lower short over that radical is unbounded below
(106.63).  The opposite operation is nevertheless well defined: for a
vector in the radical complement, maximize the finite-head defect over all
radical corrections.  This note derives that maximal anti-short exactly.

The construction has genuine content.  It removes from the omitted tail
the component which can be synthesized by exact radical gradients, and a
small numerical test shows that three radical directions already repair
the Gamma-only four-zero diagnostic.  It does not yield an automatic sign.
The anti-short is

\[
\boxed{B_S=A_Q-(T_{\rm tail})_{/\mathcal R},}        \tag{1}
\]

so it is always below the unknown complete quotient form \(A_Q\).  No
general inertia theorem makes it nonnegative.  If an off-line orbit exists,
the interpolation falsifier has \(A_Q<0\), hence also \(B_S<0\) for every
head.  Positivity of a fixed anti-short would therefore prove RH, but is a
strictly stronger assertion than RH in abstract operator theory.

## 1. Block setup

Work in the centered even multiplier space, so the constant state has
already been removed.  Let

\[
A(q,s)=\mathscr E_K(q,s)-\frac12\langle q,s\rangle_{\mu_K}             \tag{2}
\]

be the complete defect.  Let \(\mathcal R\) be the closed span of the
centered exact radical modes

\[
r_j=K^{(2j)}/K-4^{-j},\qquad j\ge1,                  \tag{3}
\]

and put \(Q=\mathcal R^\perp\).  Polarization of the complete radical
identity gives

\[
\boxed{A(r,f)=0\qquad(r\in\mathcal R)}              \tag{4}
\]

for every vector in the common form domain.  Hence, in the decomposition
\(Q\oplus\mathcal R\),

\[
A=\begin{pmatrix}A_Q&0\\0&0\end{pmatrix}.          \tag{5}
\]

Let \(S\) be a retained set of prime-power atoms, with the complete Gamma
channel always retained.  The omitted positive tail is

\[
T_S(q,s)=\sum_{m\notin S}\frac{\Lambda(m)}{\sqrt m}
 \int_{\mathbb R}K(x)K(x-\log m)
 \overline{\Delta_{\log m}q(x)}
 \Delta_{\log m}s(x)\,dx.                           \tag{6}
\]

Thus

\[
A_S=A-T_S.                                          \tag{7}
\]

For every proper finite head and every nonconstant radical direction,
106.63 proves

\[
A_S(r,r)=-T_S(r,r)<0.                               \tag{8}
\]

## 2. Exact maximal anti-short

For \(q\in Q\), define

\[
\boxed{B_S(q)=\sup_{r\in\mathcal R}A_S(q+r,q+r).}  \tag{9}
\]

Introduce the tail feature map

\[
V_Sq=\left(
 \sqrt{\frac{\Lambda(m)}{\sqrt m}K(x)K(x-\log m)}
 \Delta_{\log m}q(x)
 \right)_{m\notin S},                              \tag{10}
\]

so that \(T_S(q,s)=\langle V_Sq,V_Ss\rangle\).  Let
\(P_{V_S\mathcal R}\) denote orthogonal projection onto
\(\overline{V_S\mathcal R}\).

### Theorem 1 — Tail-distance formula

For every \(q\in Q\) in the form domain,

\[
\boxed{
\begin{aligned}
B_S(q)
&=A_Q(q)-\inf_{r\in\mathcal R}T_S(q+r)\\
&=A_Q(q)-
 \|(I-P_{V_S\mathcal R})V_Sq\|^2.                 \tag{11}
\end{aligned}}                                      
\]

In particular, if

\[
(T_S)_{/\mathcal R}(q)
:=\inf_{r\in\mathcal R}T_S(q+r),                   \tag{12}
\]

then (1) holds as a quadratic-form identity.

#### Proof

By (4) and (7),

\[
A_S(q+r)=A_Q(q)-T_S(q+r).                           \tag{13}
\]

Taking the supremum in \(r\) gives the first line of (11).  The second is
the Hilbert-space distance formula

\[
\inf_{r\in\mathcal R}\|V_Sq+V_Sr\|^2
=\operatorname {dist}
 (-V_Sq,\overline{V_S\mathcal R})^2.               \tag{14}
\]

The projection need not have a preimage in \(\mathcal R\); an optimizing
sequence suffices.  Cauchy--Schwarz in the tail feature space makes the
supremum finite even when \(T_S|_{\mathcal R}\) has no spectral gap.
\(\square\)

## 3. Formula using only the retained head

Although (11) displays the omitted tail, the same number is determined by
the retained form and the exact radical.  Put

\[
C_S(r,s)=-A_S(r,s)=T_S(r,s),qquad r,s\in\mathcal R,                  \tag{15}
\]

and define the cross functional

\[
\ell_{S,q}(r)=A_S(q,r)=-T_S(q,r).                   \tag{16}
\]

Then

\[
\boxed{
B_S(q)=A_S(q)+\|\ell_{S,q}\|_{C_S^*}^2,}           \tag{17}
\]

where

\[
\|\ell\|_{C_S^*}^2
=\sup_{r\ne0}\frac{|\ell(r)|^2}{C_S(r,r)}.         \tag{18}
\]

Indeed, (17) is completion of the square in

\[
A_S(q+r)=A_S(q)+2\operatorname {Re}\ell_{S,q}(r)-C_S(r,r).          \tag{19}
\]

For \(\mathcal R_M=\operatorname {span}\{r_1,\ldots,r_M\}\), let

\[
G_{M,ij}=-A_S(r_i,r_j),qquad
b_{M,i}=A_S(r_i,q).                                  \tag{20}
\]

When \(G_M\) is invertible, the finite anti-short is

\[
\boxed{B_{S,M}(q)=A_S(q)+b_M^*G_M^{-1}b_M,}         \tag{21}
\]

and

\[
B_{S,M}(q)\nearrow B_S(q).                           \tag{22}
\]

Thus the maximal anti-short is computable *in principle* from a finite
prime head, the Gamma/variance form and the known theta kernel \(K\).  It
is not a finite-dimensional certificate: evaluating (17) exactly requires
the infinite radical dual norm, including its closure and conditioning.
Formula (21) gives certified lower bounds only when its integrals and Gram
inverse are themselves enclosed rigorously.

## 4. The Gamma maximal-negative proposal

For the Gamma-only head, write

\[
A_\Gamma(q)=\mathscr E_\Gamma(q)
-\frac12\|q\|_{L^2(\mu_K)}^2                       \tag{22a}
\]

on the centered space.  The complete radical identity gives

\[
\boxed{A_\Gamma|_{\mathcal R}=-\mathscr E_p|_{\mathcal R}<0.}        \tag{22b}
\]

Thus a particularly sharp possible closure is:

> **Gamma maximal-negative theorem.**  The closed radical
> \(\mathcal R\) is a maximal negative subspace for \(A_\Gamma\).

In the anti-short coordinate, this statement is exactly

\[
\boxed{B_\Gamma(q)=\sup_{r\in\mathcal R}A_\Gamma(q+r)\ge0
\qquad(q\in Q).}                                    \tag{22c}
\]

### Proposition 2 — Maximal negativity would close the full quotient

If (22c) holds, then \(A_Q\ge0\).

#### Proof

For every \(r\in\mathcal R\), radical invariance and positivity of the
literal prime energy give

\[
\begin{aligned}
A_Q(q)=A(q+r)
&=A_\Gamma(q+r)+\mathscr E_p(q+r)\\
&\ge A_\Gamma(q+r).
\end{aligned}                                       \tag{22d}
\]

Take the supremum in \(r\) and use (22c).  \(\square\)

This is a valid route to RH.  It remains to determine whether the proposed
maximality can be proved rather than inferred from the sign pattern of an
unrelated Fourier multiplier.

### 4.1 The exact Picone potential

Let \(f=Kq\), and let \(\mathcal D_\Gamma\) be the translation-invariant
Gamma jump form

\[
\mathcal D_\Gamma(f)
=\int_0^\infty g(u)\int_{\mathbb R}
 |f(x)-f(x-u)|^2\,dx\,du.                            \tag{22e}
\]

Denote its associated operator by \(D_\Gamma\).  The exact Picone identity
and \(c_K=1/2\) give, for centered \(q\),

\[
\boxed{
A_\Gamma(q)
=\mathcal D_\Gamma(f)
 -\int_{\mathbb R}
 \left\{
 \frac{(D_\Gamma K)(x)}{K(x)}+\frac{h(x)}{K(x)}
 \right\}|f(x)|^2\,dx.}                            \tag{22f}
\]

For a noncentered multiplier, the right side receives the additional
positive rank-one term

\[
2\left|\int h(x)f(x)\,dx\right|^2.                  \tag{22g}
\]

Indeed, the first subtraction in (22f) is the potential term in the
zero-extension Picone formula, while

\[
\frac12\|q\|_{\mu_K}^2
=\frac1{2c_K}\int\frac hK|f|^2
=\int\frac hK|f|^2.                                \tag{22h}
\]

Formula (22f) is the exact obstruction to the naive Phase-15 argument.
The form \(\mathcal D_\Gamma\) is Fourier diagonal, but the Picone
potential

\[
V_K(x)=\frac{D_\Gamma K(x)+h(x)}{K(x)}              \tag{22i}
\]

is nonconstant and retains the full theta ground state.  Therefore
\(A_\Gamma\) is not multiplication by

\[
\Psi(t)=\operatorname {Re}\psi(1/4+it/2)-\log\pi.  \tag{22j}
\]

The discrepancy can be certified without numerics.  For large \(j\), the
Phase-15 multiplier form on the physical radical test

\[
f_j=Kr_j=K^{(2j)}-4^{-j}K                         \tag{22k}
\]

is positive.  Its Fourier transform is a degree-\(2j\) polynomial times
\(\Xi(t)\).  The negative multiplier band is bounded by
\(|t|<r_0\), while on any fixed interval
\([R,R+\delta]\) with \(R>r_0\),
\(\Psi(t)|\Xi(t)|^2\) is positive except at isolated points.  The positive
contribution grows like \(R^{4j}\), whereas the absolute negative
contribution is \(O(r_0^{4j})\).  Hence the former dominates for large
\(j\).  In contrast, the exact Riemann identity (22b) says

\[
A_\Gamma(r_j)=-\mathscr E_p(r_j)<0
\quad\text{for every }j.                            \tag{22l}
\]

Thus the Fourier-band density of the physical radical does not prove
maximal negativity for the Doob--Picone form.  A proof of (22c) must
control the nonconstant potential (22i), or equivalently the complete
tail-distance projection in (11).  No closed-graph theorem removes that
term.

## 5. Inertia audit

In finite dimension, if \(-T_S|_{\mathcal R}\) is invertible, the
Haynsworth formula gives

\[
\operatorname {Inertia}(A_S)
=\operatorname {Inertia}(-T_S|_{\mathcal R})
 +\operatorname {Inertia}(B_S).                    \tag{23}
\]

The first term is negative, not positive.  Hence (23) supplies no sign for
\(B_S\).

The failure is already visible in dimension two.  On
\(Q\oplus\mathcal R\), take

\[
A=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
T=\begin{pmatrix}2&0\\0&1\end{pmatrix}.           \tag{24}
\]

Then \(A\ge0\), \(\mathcal R=\ker A\), and

\[
A_S=A-T=\begin{pmatrix}-1&0\\0&-1\end{pmatrix},
\qquad B_S=-1.                                      \tag{25}
\]

Therefore positivity of the complete quotient does not imply positivity
of any fixed anti-short by abstract operator theory.

Conversely, (11) gives

\[
\boxed{B_S\ge0\quad\Longrightarrow\quad A_Q\ge0.} \tag{26}
\]

So a positive fixed-head anti-short would be a valid, but potentially
strictly stronger, RH certificate.

## 6. Cofinal heads

If \(S_N\uparrow\{m:\Lambda(m)>0\}\), then

\[
0\le (T_{S_N})_{/\mathcal R}(q)
\le T_{S_N}(q)\longrightarrow0                     \tag{27}
\]

for every fixed vector in the full form domain.  Hence

\[
\boxed{B_{S_N}(q)\nearrow A_Q(q).}                  \tag{28}
\]

The monotonicity follows because enlarging the retained head decreases the
tail form and therefore its short.  Equation (28) shows the precise logical
status:

* positivity of one fixed \(B_S\) is stronger than the complete floor;
* positivity only after taking the cofinal limit is exactly the original
  complete floor, not a reduction of it.

## 7. Gamma-only four-zero diagnostic

Take \(S=\varnothing\), meaning that Gamma is retained and every literal
prime-power atom belongs to the tail.  Use the exact complement vector

\[
q_4(x)=\frac{
 \cos(\gamma_1x)-2\cos(\gamma_2x)
 +2\cos(\gamma_3x)-\cos(\gamma_4x)}{\cosh(x/2)}.    \tag{29}
\]

The raw Gamma defect is negative.  Applying (21) with the first centered
radicals gives the following floating-point diagnostic:

\[
\begin{array}{c|r|r}
M&(T_S)_{/\mathcal R_M}(q_4)&B_{S,M}(q_4)\\ \hline
0&0.09911464&-0.00976766\\
1&0.09645111&-0.00710413\\
2&0.08977737&-0.00043039\\
3&0.08172604&+0.00762094\\
4&0.07419994&+0.01514704
\end{array}                                         \tag{30}
\]

The \(m\le1000\) prime-power-head approximation to the complete defect is
\(0.08934697\).  Thus the finite radical
correction repairs this particular Gamma-only falsifier by dimension three.
The result is stable under the displayed weighted correlation solve, but
it is not interval-certified.  It is evidence that the anti-short differs
materially from merely testing the finite head on \(Q\); it is not evidence
for a uniform sign on all complement vectors.

### 7.1 Growing zero-mode spans

The maximal-negative proposal must be tested with the radical dimension
and the complement dimension growing independently.  A weighted QR in
\(L^2(\mu_K)\), with every raw radical column normalized before QR, gives
the following minimum anti-short values.  The entries in parentheses are
the numbers of negative eigenvalues in the displayed zero-mode span.

\[
\begin{array}{c|rrrrrr}
\text{zero modes}\backslash M&2&4&6&8&10&12\\ \hline
4&-.020344\ (1)&-.006111\ (1)& .004135\ (0)& .010550\ (0)&
 .014541\ (0)& .017103\ (0)\\
10&-.239350\ (4)&-.238286\ (4)&-.237397\ (4)&-.236754\ (4)&
-.236298\ (4)&-.235972\ (3)\\
20&-.316147\ (9)&-.316073\ (9)&-.316003\ (9)&-.315946\ (9)&
-.315900\ (9)&-.315862\ (9)\\
40&-.360312\ (22)&-.360307\ (22)&-.360302\ (22)&-.360297\ (22)&
-.360293\ (22)&-.360290\ (22).
\end{array}                                         \tag{30a}
\]

The radical-basis orthogonality error is \(8.1\times10^{-15}\); after the
zero modes are projected onto each finite radical complement, the largest
combined-basis error in the displayed run is \(8.9\times10^{-12}\).  The
smallest diagonal of the preconditioned radical QR at \(M=12\) is
\(0.188\), and the largest eigenvalue of the Gamma form on that radical
block is \(-0.0644\).  Thus (30a) is not caused by an obvious raw-Gram
inversion or by loss of the required negative sign on the finite radical.

The experiment has a precise interpretation.  A fixed four-mode span is
repaired by six radical directions, consistent with (30).  But a fixed
low-degree radical space does not control a growing zero-mode span: many
negative directions persist and the lowest value barely moves.  This does
not refute maximality of the *complete* infinite radical, because the
radical dimension may have to grow with the spectral span.  It does rule
out treating the density of low-degree radical polynomials as a uniform
closed-graph estimate without proving quantitative conditioning.

## 8. Exact off-line falsifier

The off-line interpolation test survives every maximal anti-short.

### Theorem 2 — Anti-shorting cannot absorb an off-line channel

If an off-line zero orbit exists, then for every retained head \(S\) there
is \(q\in Q\) such that

\[
\boxed{B_S(q)<0.}                                   \tag{31}
\]

#### Proof

By 106.37 and the exact projection argument of 106.64, an off-line orbit
produces \(q\in Q\) with \(A_Q(q)<0\).  Since the tail short is
nonnegative, (11) gives

\[
B_S(q)=A_Q(q)-(T_S)_{/\mathcal R}(q)
\le A_Q(q)<0.                                       \tag{32}
\]

\(\square\)

Thus a proof of \(B_S\ge0\) from the literal finite-head data would
exclude every off-line orbit and prove the desired quotient floor.  No
inertia theorem or maximization identity supplies that sign for free.

## 9. Reproduction and status

Run

```bash
cd 03-research/phase-106-global-modular-star-audit
python3 tools/maximal_antishort_diagnostic.py \
  --dx 0.001 --head 1000 --radicals 12 --zero-span 40
```

The script uses analytic theta-derivative recurrences and NumPy linear
algebra.  It is diagnostic, not an outward-interval proof.

The maximal anti-short is an exact new coordinate, and the Gamma-only test
shows why it merits separation from the failed ordinary short.  Its
sharpest version is the Gamma maximal-negative theorem (22c).  Proving that
theorem with the exact Picone potential would give a valid RH closure by
Proposition 2.  The Phase-15 Fourier-band argument does not prove it, and
the growing-span diagnostic shows that no fixed low-degree radical block
approximates it uniformly.  Deriving the sign from general inertia, or
passing immediately to the cofinal limit (28), would only restate the
complete quotient problem.
