# D.39 — Quarter-phase repair and the Meyer `Fourier J` no-go

## Status

This note answers two precise questions left by D.38.

1. Replacing the Crofoot unit `C` by `D=iC` repairs invariance of the
   Crofoot-aligned Poisson graph and induces `-i` on the algebraic quotient.
   It does not give a polarization for the fixed Tate form and supplies no
   trace-compatible Hilbertization.
2. Meyer's global multiplier `A=Fourier J` commutes with scaling and is
   unitary on the critical Hilbert line, but it does not preserve
   `mathcal H_-` or `Z mathcal H_cap`.  Its exact maximal one-step domains
   are described below.

No zero location, Weil sign or RH is used.

## 1. The quarter-phase graph calculation

Let `C:H_1 -> H_2` be unitary and retain the Crofoot-aligned relation

\[
 R_C=\{(x,Cx):x\in H_1\}.                            \tag{1.1}
\]

Put

\[
 D=iC,
 \qquad
 \mathbb J_D(x,y)=(-D^*y,Dx).                        \tag{1.2}
\]

The general defect formula of D.38 gives

\[
 \Delta_{D,C}=D+CD^*C
 =iC+C(-iC^*)C=0.                                   \tag{1.3}
\]

Thus `mathbb J_D(R_C)=R_C`.  More explicitly,

\[
 \mathbb J_D(x,Cx)=(ix,iCx)=\iota_C(ix).             \tag{1.4}
\]

For the quotient coordinate `q_C(a,b)=b-Ca`,

\[
 \begin{aligned}
 q_C\mathbb J_D(a,b)
 &=Da+C D^*b\\
 &=iCa-i b\\
 &=-i(b-Ca).
 \end{aligned}                                      \tag{1.5}
\]

Hence the induced algebraic operator is exactly

\[
 \overline{\mathbb J}_D=-i.                         \tag{1.6}
\]

This part of the proposed repair is correct.

## 2. Failure of the Tate polarization

Transport the second factor by `C^*`.  Then `C=1`, the relation is the
diagonal, and the Crofoot--Tate skew-Hermitian form is

\[
 \Omega((x,y),(x',y'))
 =\langle x,y'\rangle-\langle y,x'\rangle.           \tag{2.1}
\]

The quarter-phase operator becomes

\[
 \mathbb J_i(x,y)=(iy,ix).                           \tag{2.2}
\]

For either convention on which slot of the Hilbert product is linear,
direct substitution yields

\[
 \Omega(\mathbb J_i v,\mathbb J_i w)=-\Omega(v,w).  \tag{2.3}
\]

Thus `mathbb J_i` is anti-symplectic for both real components
`Re Omega` and `Im Omega`.  It fails the Weil-operator identity

\[
 \omega(Jv,Jw)=\omega(v,w).                          \tag{2.4}
\]

Moreover, the associated diagonal expression is

\[
 \Omega(v,\mathbb J_i v)
 =\pm i\bigl(\|x\|^2-\|y\|^2\bigr),                 \tag{2.5}
\]

with the harmless overall sign determined by the inner-product convention.
Its real part is zero and its imaginary part is a split form.  Neither is a
positive-definite Hodge metric.

There is a second structural obstruction.  The diagonal relation is
Lagrangian for (2.1).  Quotienting the whole doubled space by a Lagrangian
does not inherit a symplectic form; symplectic reduction would use
`R_C^perp/R_C`, which is zero here.  Therefore (1.6) by itself does not
produce the nondegenerate Tate pairing required on the Meyer cokernel.

We conclude:

> The substitution `C -> iC` repairs precisely the algebraic graph
> invariance.  It destroys compatibility with the fixed pre-quotient Tate
> form and does not construct a positive or trace-compatible
> polarization.

The scalar `-i` commutes with scaling, but commutation alone supplies
neither the Hilbert norm nor equality of Hilbert and nuclear traces.

## 3. Mellin multiplier of Meyer's `A=Fourier J`

Use Meyer's conventions

\[
 (Jf)(x)=x^{-1}f(x^{-1}),
 \qquad
 (\mathcal Ff)(y)=\int_{\mathbb R}f(x)e^{2\pi ixy}\,dx,             \tag{3.1}
\]

on even functions, and

\[
 \widehat f(s)=\int_0^\infty f(x)x^s\,d^*x.          \tag{3.2}
\]

For an initial strip in which Fubini is valid and then by meromorphic
continuation,

\[
 \widehat{\mathcal Ff}(s)
 =\gamma(s)\widehat f(1-s),                          \tag{3.3}
\]

where

\[
 \boxed{
 \gamma(s)
 =2(2\pi)^{-s}\Gamma(s)\cos\frac{\pi s}{2}
 =\pi^{1/2-s}
   \frac{\Gamma(s/2)}{\Gamma((1-s)/2)}.}             \tag{3.4}
\]

Since `widehat{Jf}(s)=widehat f(1-s)`, the scaling multiplier of

\[
 A=\mathcal FJ                                         \tag{3.5}
\]

is exactly

\[
 \boxed{\widehat{Af}(s)=\gamma(s)\widehat f(s).}     \tag{3.6}
\]

This proves directly that `A` commutes with every scaling `lambda_t`, since
`widehat{lambda_t f}(s)=t^s widehat f(s)`.

The functional identity

\[
 \gamma(s)\gamma(1-s)=1                              \tag{3.7}
\]

shows that `A^{-1}=J mathcal F`.  On `Re(s)=1/2`, conjugation and (3.7)
give

\[
 |\gamma(1/2+i\tau)|=1.                              \tag{3.8}
\]

Thus `A` is a unitary scaling multiplier on the critical `L^2` model.  This
Hilbert-line assertion must not be confused with preservation of Meyer's
nuclear Frechet spaces.

## 4. Exact action on `mathcal H_-`

Mellin transformation identifies `mathcal H_-` with the entire functions
which are Schwartz on every vertical line.  The multiplier (3.4) has
simple poles at

\[
 0,-2,-4,\ldots                                      \tag{4.1}
\]

and simple zeros at

\[
 1,3,5,\ldots.                                       \tag{4.2}
\]

Stirling estimates show that `gamma(s)` and all its derivatives have only
polynomial growth on every vertical line away from the finitely located
poles.  Consequently the maximal one-step domain in `mathcal H_-` is

\[
 \boxed{
 \mathcal D_-(A)=
 \{f\in\mathcal H_-:\widehat f(-2n)=0
       \text{ for every }n\ge0\}.}                  \tag{4.3}
\]

For `f in mathcal D_-(A)`, the zeros cancel the simple poles and `Af` again
belongs to `mathcal H_-`.  Conversely, entireness of `widehat{Af}` forces
all the vanishings in (4.3).  In particular,

\[
 A(\mathcal H_-)\not\subseteq\mathcal H_-.           \tag{4.4}
\]

Similarly,

\[
 \mathcal D_-(A^{-1})=
 \{f\in\mathcal H_-:\widehat f(1+2n)=0
       \text{ for every }n\ge0\}.                  \tag{4.5}
\]

The domain (4.3) is a proper closed infinite-codimension subspace because
all evaluations are continuous.  It is not invariant under arbitrary
iteration of `A`: demanding `A^k f in mathcal H_-` for all `k` forces
`widehat f` to vanish to every order at `s=0`, hence `f=0`.  Therefore no
nonzero subspace carrying `A` as an everywhere-defined automorphism arises
from this pole cancellation.

## 5. Exact action on the Poisson range

Write

\[
 R=Z\mathcal H_\cap\subset\mathcal H_-.              \tag{5.1}
\]

Meyer's range theorem characterizes `h in R` by entireness, vertical
Schwartz decay, and the two divisibility conditions

\[
 \frac{\widehat h(s)}{\zeta(s)}\in\mathcal S
 \quad(\mathrm{Re}\,s\ge1/2),
 \qquad
 \frac{\widehat h(s)}{\zeta(1-s)}\in\mathcal S
 \quad(\mathrm{Re}\,s\le1/2).                  \tag{5.2}
\]

Multiplication by `gamma(s)` preserves both conditions wherever it is
holomorphic, because it has only polynomial vertical growth.  On the left
half-plane its only obstruction is again (4.1).  Hence the exact maximal
one-step domain in the Poisson range is

\[
 \boxed{
 \mathcal D_R(A)=
 \{h\in Z\mathcal H_\cap:
       \widehat h(-2n)=0\text{ for every }n\ge0\},}  \tag{5.3}
\]

and

\[
 A h\in Z\mathcal H_\cap
 \quad\Longleftrightarrow\quad h\in\mathcal D_R(A). \tag{5.4}
\]

Thus `A` does not preserve the full Poisson relation subspace.

### Explicit source counterexample

Let

\[
 g(x)=\left(x^2-\frac23x^4\right)e^{-x^2},           \tag{5.5}
\]

extended evenly to `mathbb R`.  Then

\[
 g(0)=0,
 \qquad
 \mathcal Fg(0)=\int_{\mathbb R}g(x)\,dx=0,          \tag{5.6}
\]

because

\[
 \int_{\mathbb R}x^2e^{-x^2}\,dx=\frac{\sqrt\pi}{2},
 \qquad
 \int_{\mathbb R}x^4e^{-x^2}\,dx=\frac{3\sqrt\pi}{4}.             \tag{5.7}
\]

Hence `g in mathcal H_cap` and `h=Zg in R`.  But

\[
 \widehat g(0)
 =\int_0^\infty
 \left(x-\frac23x^3\right)e^{-x^2}\,dx
 =\frac16.                                          \tag{5.8}
\]

Since `zeta(0)=-1/2`, analytic continuation of
`widehat h(s)=zeta(s)widehat g(s)` gives

\[
 \widehat h(0)=-\frac1{12}\ne0.                     \tag{5.9}
\]

The factor `gamma(s)` has a pole at zero.  Therefore

\[
 \widehat{Ah}(s)=\gamma(s)\widehat h(s)              \tag{5.10}
\]

has a pole at zero, so

\[
 Ah\notin\mathcal H_-,
 \qquad Ah\notin Z\mathcal H_\cap.                 \tag{5.11}
\]

This is an exact counterexample, not a numerical test.

## 6. No induced operator on the Meyer cokernel

An everywhere-defined continuous operator on

\[
 \mathcal H_-^0=\mathcal H_-/Z\mathcal H_\cap       \tag{6.1}
\]

obtained from `A` requires

\[
 A(\mathcal H_-)\subseteq\mathcal H_-,
 \qquad
 A(Z\mathcal H_\cap)\subseteq Z\mathcal H_\cap.     \tag{6.2}
\]

Equations (4.4) and (5.11) disprove both inclusions.  Hence Meyer's
`Fourier J`, despite commuting with scaling and being unitary on the
critical `L^2` line, does not descend to the row-C odd quotient.

Combining Sections 1--2 and 3--6 gives the precise no-go:

> The finite quarter-phase produces the desired scalar complex structure
> only on an algebraic graph quotient, where it is incompatible with the
> fixed Tate symplectic form.  The natural global scaling-equivariant
> operator `Fourier J` has the correct critical-line unitarity but fails to
> preserve both the ambient Meyer Frechet space and its Poisson relation
> subspace.  Neither construction supplies the missing Tate/trace-compatible
> polarization of row D.

This leaves row D open and yields no assertion about RH.
