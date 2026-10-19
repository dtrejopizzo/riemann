# R183.005 — Arithmetic interference of the first crossings

## 0. Result

Minimal propagation \(\log m\ge 2T\) does not make the exterior channels orthogonal. Two different rough integers can satisfy

\[
             |\log(m/n)|<2T=\log q,                 \tag{0.1}
\]

so their translated copies of a width-\(2T\) test interfere. The correct decomposition is a Gram matrix indexed by quotients \(m/n\). This computation prevents a false closure of R183.004 and locates the arithmetic information not yet used.

## 1. Exact interference formula

Let \(D_a f(t)=f(t+\log a)\). For \(h\in L^2(-T,T)\), define

\[
 c_h(v)=\int_{\mathbb R}h(t)\overline{h(t-v)}\,dt.  \tag{1.1}
\]

For a finite family \((z_m)\), unitarity of the translations gives

\[
 \boxed{
 \left\|\sum_m z_mD_mh\right\|_2^2
   =\sum_{m,n}z_m\overline{z_n}\,
          c_h\!\left(\log{n\over m}\right).}       \tag{1.2}
\]

The matrix

\[
 G_h(m,n)=c_h\!\left(\log{n\over m}\right)         \tag{1.3}
\]

is positive semidefinite because it is the Gram matrix of \((D_mh)_m\). Since \(c_h\) vanishes outside \([-2T,2T]\),

\[
 G_h(m,n)=0\quad\text{if}\quad {n\over m}\notin[q^{-1},q]. \tag{1.4}
\]

But (1.4) does not force \(m=n\). For \(q=5\), for instance, \(m=5,n=7\) belong to \(M_{S(5)}\) and \(7/5\in(1,5)\). Hence the off-diagonal block is real and cannot be dismissed.

## 2. Inserting the comb and Möbius

For the rough comb and its inverse, the coefficients are

\[
 a_m={1\over\sqrt m},\qquad
 b_m={\mu(m)\over\sqrt m}.                          \tag{2.1}
\]

In every finite truncation, (1.2) produces

\[
 \|E_S^{[R]}h\|^2
 =\sum_{\substack{m,n\in M_S\\m,n\le R}}
 {1\over\sqrt{mn}},c_h\!\left(\log{n\over m}\right),       \tag{2.2}
\]

\[
 \|M_S^{[R]}h\|^2
 =\sum_{\substack{m,n\in M_S\\m,n\le R}}
 {\mu(m)\mu(n)\over\sqrt{mn}},c_h\!\left(\log{n\over m}\right). \tag{2.3}
\]

The support reduces both sums to the hyperbolic corridor

\[
                    q^{-1}<n/m<q,                  \tag{2.4}
\]

but gives them no relative sign. Their diagonal parts differ exactly on
the squarefree integers: in (2.2) the weight is \(1/m\), while
in (2.3) it is \(\mu(m)^2/m\). Hence not even the diagonal cancels
term by term. The off-diagonal terms carry the arithmetic
orientation \(\mu(m)\mu(n)\).

## 3. Parametrization by greatest common divisor

Write

\[
             m=da,\qquad n=db,\qquad (a,b)=1.       \tag{3.1}
\]

Then the autocorrelation argument depends only on the reduced fraction:

\[
       \log(n/m)=\log(b/a),                         \tag{3.2}
\]

while the Möbius weight keeps the common fiber \(d\):

\[
 {\mu(da)\mu(db)\over d\sqrt{ab}}.                 \tag{3.3}
\]

Hence the Möbius interference is organized exactly as

\[
 \boxed{
 \sum_{\substack{(a,b)=1\\q^{-1}<b/a<q}}
 {c_h(\log(b/a))\over\sqrt{ab}}
 \sum_{\substack{d:\ da,db\in M_S}}
 {\mu(da)\mu(db)\over d}.}                         \tag{3.4}
\]

With finite cutoffs, the interior sum is further restricted by
\(d\le R/\max(a,b)\). Fiber (3.4) is the exact arithmetic coordinate that a
first-crossing factorization must preserve. It is not determined by the
gap \(m\ge q\) alone.

## 4. Where Poisson must act

R183.004's factorization

\[
                  u_S=M_S^\vee E_S                 \tag{4.1}
\]

reflects one of the two families before recombining them. In the norm
expansion, this replaces a matrix like (2.2) by a cross form between (2.2)
and (2.3), with Poisson's two boundary terms. The sign cannot come from
the positivity of \(G_h\) alone, because any choice of coefficients
produces a positive Gram matrix. It must come from an exact cancellation of
fibers (3.4) against:

1. Poisson's term at zero;
2. Poisson's integral term;
3. the reflection \(a/b\leftrightarrow b/a\).

The first two are exactly the two Tate moments. That is why they must be
imposed **after** forming the full interference matrix, not path by path.

The source identity that would close the argument now has a checkable
form. For each truncation there must exist a matrix \(Z_{q,h}^{[R]}\), built
from differences between the fibers \((d,a,b)\) and their Poisson
reflections, such that

\[
 \boxed{
 \|Qu_SC_hE_R\|_{\rm HS}^2-
 \|QC_hE_R\|_{\rm HS}^2
 =\|Z_{q,h}^{[R]}\|_{\rm HS}^2+\varepsilon_R(h),}  \tag{4.2}
\]

with \(\varepsilon_R(h)\to0\) in the trace regularization. Here \(E_R\) is
R183.002's Hilbert--Schmidt cutoff, not the comb \(E_S\). The notation
distinguishes the two objects.

## 5. Scope audit

Equality (1.2) and parametrization (3.4) are exact. They do not prove the
sign of (4.2). Their contribution is to rule out the naive orthogonal
decomposition and to fix the minimal level at which the square must be
built: pairs of paths with the same reduced quotient and coherent sum
over the common factor \(d\).

This level is finer than R170.878: there, the Möbius loop is kept as an
exterior operator; here, its interference is expanded after coupling it with
the Poisson reflection. It also explains why estimating each term loses
Theorem M's margin.

## 6. Logical status

* Gram matrix of quotients (1.2)--(1.4): **PROVED**.
* Persistence of interference between different rough integers: **PROVED**.
* Comb and Möbius expansions (2.2)--(2.3): **PROVED** at finite cutoff.
* Decomposition by reduced fraction (3.4): **PROVED** at finite cutoff.
* Orthogonality by first crossing: **REFUTED**.
* Poisson--Tate cancellation of fibers (3.4): **OPEN**.
* Finite square (4.2): **OPEN**.
* Row D: **OPEN**.
