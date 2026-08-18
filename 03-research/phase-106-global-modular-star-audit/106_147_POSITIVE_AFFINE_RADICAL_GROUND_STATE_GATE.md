# 106.147 — Positive affine radicals and the scalar ground-state gate

## 1. Purpose and result

The complete Riemann radical contains a positive family which is not visible
in a basis of centered derivatives.  For (y\geq0), put

\[
 G_y(x)={K(x-y)+K(x+y)\over2},
 \qquad
 v_y(x)={G_y(x)\over K(x)}.
 \tag{1}
\]

Every (v_y) is strictly positive.  Moreover, (G_y) is an exact Weil
radical because

\[
 \widehat G_y(z)=\cos(yz)\Xi(z).
 \tag{2}
\]

This note tests whether this positive family supplies the missing scalar
ground state for the radically shorted operator.  There is an exact answer.

1.  The positive multiplier (v_y) satisfies the affine threshold equation

    \[
      Lv_y={1\over2}\{v_y-\cosh(y/2)\}.
      \tag{3}
    \]

2.  Picone transformation by (v_y) gives an exact positive edge energy,
    but the constant term in (3) becomes a negative variance of precisely
    the same sharp order:

    \[
      QW(Kq,Kq)
      =\mathscr D_y(q/v_y)
       -{\cosh^2(y/2)\over2}
        \mathrm{Var}_{\nu_y}(q/v_y).
      \tag{4}
    \]

3.  For every nonzero centered multiplier, the variance in (4) is strictly
    positive.  Convexly mixing the positive affine radicals therefore does
    not produce a Hilbert-square factorization; it mixes exact copies of the
    same unresolved sharp Poincare inequality.
4.  No nonzero positive threshold supersolution in the operator domain can
    remove this defect.  Invariance of the probability measure gives an
    immediate contradiction after integration.  A nonintegrable comparison
    state can evade that contradiction only through a nonzero boundary
    flux, which must then remain in the certificate.

Thus the scalar Doob--Picone and scalar passive zero-energy impedance classes
are exhausted.  The remaining admissible class is a matrix- or
operator-valued, globally signed realization formed after the complete
radical anti-short and retaining the literal ordinary-prime, Gamma, and pole
channels jointly.

No zero-location statement is used below.

## 2. Setup

Let

\[
 h(x)=\cosh(x/2),
 \qquad c_K={1\over2},
 \qquad
 d\mu_K(x)={h(x)K(x)\over c_K}\,dx.
 \tag{5}
\]

Let \(\mathfrak j\) be the symmetric edge measure of the complete
ordinary-prime--Gamma generator (L), so that

\[
 \mathscr E_K(f,g)
 ={1\over2}\iint
 \overline{f(x)-f(t)}\{g(x)-g(t)\}
 \,d\mathfrak j(x,t)
 =\langle f,Lg\rangle_{\mu_K}.
 \tag{6}
\]

The full-kernel identity and its polarization are

\[
 QW(Kf,Kg)
 =\mathscr E_K(f,g)
  -{1\over2}\mathrm{Cov}_{\mu_K}(f,g).
 \tag{7}
\]

Initially all Picone calculations are made with a compactly supported smooth
multiplier.  This avoids imposing a global form-domain condition on the
positive comparison function (v_y), whose tail ratio can grow rapidly.
The resulting identities extend to every common core on which both sides
are finite.

## 3. The affine threshold equation

### Theorem 1 — Positive affine radical

For every real (y\geq0),

\[
 \boxed{
 v_y>0,
 \qquad
 \mu_K(v_y)=h(y),
 \qquad
 Lv_y={1\over2}\{v_y-h(y)\}}
 \tag{8}
\]

in the weak sense on the smooth compact core.

#### Proof

Strict positivity follows from (K>0).  Hyperbolic addition and evenness of
(K) give

\[
 \int_{\mathbb R}h(x)K(x-y)\,dx=c_Kh(y),
 \qquad
 \int_{\mathbb R}h(x)K(x+y)\,dx=c_Kh(y).
 \tag{9}
\]

Consequently

\[
 \mu_K(v_y)
 ={1\over c_K}\int h(x)G_y(x)\,dx=h(y).
 \tag{10}
\]

Equation (2) implies that (G_y) vanishes at every zero of \(\Xi\), with
the required multiplicities.  Hence it is polarized-orthogonal for the
completed Weil form:

\[
 QW(G_y,Ks)=0
 \tag{11}
\]

for every compact core multiplier (s).  Substitute (G_y=Kv_y) in
(7).  Equations (10)--(11) give

\[
 \langle v_y,Ls\rangle_{\mu_K}
 ={1\over2}
 \langle v_y-h(y),s\rangle_{\mu_K}.
 \tag{12}
\]

Self-adjointness of (L) proves the weak equation in (8).  \(\square\)

The forcing in (8) is not an error term.  It is forced by stationarity:
the right side has zero \(\mu_K\)-mean, as every vector in the range of a
conservative generator must.

## 4. Exact positive-affine Picone identity

Define the probability measure

\[
 d\nu_y(x)={v_y(x)\over h(y)}\,d\mu_K(x),
 \tag{13}
\]

and, for a compact core amplitude (a), define

\[
 \mathscr D_y(a)
 ={1\over2}\iint
 v_y(x)v_y(t)|a(x)-a(t)|^2
 \,d\mathfrak j(x,t).
 \tag{14}
\]

### Theorem 2 — Affine ground-state representation

For every compact core multiplier (q), with (a=q/v_y),

\[
 \boxed{
 QW(Kq,Kq)
 =\mathscr D_y(a)
  -{h(y)^2\over2}\mathrm{Var}_{\nu_y}(a).}
 \tag{15}
\]

#### Proof

The jump Picone identity, integrated against \(\mathfrak j\), is

\[
 \mathscr E_K(q)
 =\mathscr D_y(q/v_y)
  +\int {Lv_y\over v_y}|q|^2\,d\mu_K.
 \tag{16}
\]

Using (8),

\[
 \mathscr E_K(q)-{1\over2}\|q\|_{\mu_K}^2
 =\mathscr D_y(a)
  -{h(y)\over2}\int v_y|a|^2\,d\mu_K.
 \tag{17}
\]

The pole term in (7) adds

\[
 {1\over2}|\mu_K(q)|^2
 ={1\over2}\left|\int v_ya\,d\mu_K\right|^2.
 \tag{18}
\]

Since \(v_y\,d\mu_K=h(y)d\nu_y\), the sum of the last terms in
(17)--(18) is

\[
 -{h(y)^2\over2}
 \left{
  \int|a|^2\,d\nu_y
  -\left|\int a\,d\nu_y\right|^2
 \right}.
 \tag{19}
\]

Equations (17)--(19) prove (15).  \(\square\)

For (y=0), one has (v_0=1), (h(0)=1), and (15) is the original
full-kernel Doob--variance identity.  Varying (y) does not deform the
target.  It conjugates the same sharp inequality by a positive affine
radical.

## 5. The defect is strict on the physical complement

Let

\[
 \mathscr C=(\mathbf1\oplus\mathcal R)^\perp
 \subset L^2(\mu_K).
 \tag{20}
\]

### Theorem 3 — No positive affine radical removes the variance

If (0\ne q\in\mathscr C) belongs to the common core, then for every
(y\geq0),

\[
 \boxed{
 \mathrm{Var}_{\nu_y}(q/v_y)>0.}
 \tag{21}
\]

#### Proof

The measures \(\nu_y\) and \(\mu_K\) have strictly positive densities on
the whole real line.  If the variance in (21) vanished, then
(q/v_y=c) almost everywhere for a constant (c).  Thus (q=cv_y).
But (q\perp1) and (8) gives

\[
 0=\mu_K(q)=c\,h(y).
 \tag{22}
\]

Since (h(y)>0), one has (c=0), contrary to (q\ne0).  \(\square\)

Let \(\alpha\) be any probability measure on the parameter (y) for
which the following integrals are finite.  Averaging (15) gives

\[
 \boxed{
 QW(Kq,Kq)
 =\int\mathscr D_y(q/v_y)\,d\alpha(y)
 -{1\over2}\int h(y)^2
  \mathrm{Var}_{\nu_y}(q/v_y)\,d\alpha(y).}
 \tag{23}
\]

For every nonzero (q\in\mathscr C), the second integral is strictly
positive.  Thus no convex mixture of positive affine radicals yields a
sum-of-squares proof.  Dropping its variance term is a strict, invalid
strengthening; proving that the first integral dominates it is exactly the
physical surplus in an averaged coordinate.

Signed mixing can cancel the defect only by assigning negative weights to
some positive edge forms.  It therefore leaves the scalar passive class and
enters the globally signed IQC class isolated by 106.143--106.146.

## 6. No positive operator-domain threshold state

The preceding calculation gives the explicit obstruction for the natural
theta translates.  There is also a general stationary obstruction.

### Theorem 4 — Conservative-generator obstruction

There is no nonzero (v\geq0) in the operator domain of (L) satisfying

\[
 Lv\geq{1\over2}v
 \tag{24}
\]

weakly.  In particular, there is no positive operator-domain solution of
(Lv=v/2).

#### Proof

Because (L1=0) and (L) is self-adjoint,

\[
 \langle1,Lv\rangle_{\mu_K}
 =\langle L1,v\rangle_{\mu_K}=0.
 \tag{25}
\]

On the other hand, (24) and positivity give

\[
 \langle1,Lv\rangle_{\mu_K}
 \geq{1\over2}\int v\,d\mu_K>0,
 \tag{26}
\]

a contradiction.  \(\square\)

A scalar ground-state representation of (L-1/2) with nonnegative local
potential would require precisely such a positive supersolution.  A
positive comparison function outside the operator domain can avoid Theorem
4 only by carrying a nonzero boundary flux in the integration-by-parts
identity.  That flux is then load-bearing and cannot be declared zero by
passivity.  In the explicit admissible family (1), the same obstruction is
already visible without taking a boundary limit: it is the positive affine
forcing (h(y)), and Theorem 2 converts it into the negative variance.

This is the scalar Dirichlet-to-Neumann consequence.  A scalar passive
zero-energy realization based on a positive threshold profile would either
produce an operator-domain supersolution, forbidden by Theorem 4, or a
nonvanishing boundary supply.  It cannot by itself factor the compressed
operator (P(L-1/2)P) as (Q^*Q).

## 7. Surviving construction class

The positive affine radical family is the maximal natural scalar repair of
the sign-changing centered radical:

* every (v_y) is strictly positive;
* every numerator (Kv_y) is an exact theta radical;
* its mean and threshold forcing are explicit;
* its Picone transform retains the complete literal ordinary-prime--Gamma
  edge measure.

Nevertheless, its forcing produces the strict variance defect (21), and
positive averaging cannot cancel it.  Together with the signed
operator-valued connection gate of 106.129, this leaves the following
sharp dichotomy.

1. A scalar positive ground state has positive conductances but an
   unavoidable affine/polar variance defect.
2. A centered operator-valued ground state removes the affine forcing but
   has a signed radical-correlation connection.

Therefore the remaining construction must be globally nondecomposable and
matrix- or operator-valued.  It must combine ordinary
\(\Lambda(p^k)\), the complete Gamma remainder, and the pole after the
complete radical anti-short, before a Hilbert norm or Schur complement is
estimated.  The global chord constraints of 106.145--106.146 supply its
correct domain, but the required compressed arithmetic sign is not a scalar
Doob or scalar impedance consequence.

