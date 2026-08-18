# Strip Poisson kernel formula

## Purpose

`178_STRIP_POISSON_BOUNDARY_NO_GO.md` records that strip Poisson cannot
close the log-derivative route unless \(\xi'/\xi\) is already holomorphic in
the strip.  `179_STRIP_GREEN_POLE_DEFECT_DECOMPOSITION.md` records the local
pole defect.  This note supplies the explicit strip Poisson kernel and the
conditional integral formula.

`177_UNCONDITIONAL_SIGMA_GT_1_POSITIVITY.md` leaves the exact strip target
\[
  \Re{\xi'\over\xi}(s)\ge0
  \qquad\left({1\over2}<\Re s\le1\right).
\tag{1}
\]

This note tests whether (1) can be reduced to boundary data by a
Poisson/Green formula in the vertical strip
\[
  \mathcal S=\left\{s=\sigma+it:\ {1\over2}<\sigma<1\right\}.
\]

The conclusion is a precise gate:

- if \(\xi'/\xi\) is already holomorphic in \(\mathcal S\), then strip
  Poisson reduces (1) to vertical boundary data;
- if there is a zero of \(\xi\) in \(\mathcal S\), the Green/pole term has
  negative real part on one side of the pole and destroys positivity
  locally;
- therefore a boundary-only proof must also prove absence of interior poles.
  That absence is exactly the RH-strength content isolated in `175`.

So the strip Poisson route is valid as a conditional representation, but it
does not close A1/Omega7 unless the no-interior-pole theorem is proved
independently from Euler--Gamma data.

## Boundary values on the vertical sides

Put
\[
  q(s)={\xi'\over\xi}(s),
  \qquad
  u(s)=\Re q(s).
\]

On the critical line, away from zeros, the functional equation
\[
  \xi(s)=\xi(1-s)
\]
gives
\[
  q(s)=-q(1-s).
\tag{2}
\]

Using the reality symmetry
\[
  \xi(\overline s)=\overline{\xi(s)},
\]
for \(s=1/2+it\) we have
\[
  1-s=\overline s,
  \qquad
  q(1-s)=q(\overline s)=\overline{q(s)}.
\]

Thus
\[
  q(1/2+it)=-\overline{q(1/2+it)}
\]
and hence
\[
  \boxed{
  \Re q(1/2+it)=0
  }
\tag{3}
\]
at every nonzero boundary point.

On the right boundary \(\sigma=1\), `177` gives the one-sided positive
limit inherited from the unconditional half-plane:
\[
  \boxed{
  \Re q(1+it)\ge0
  }
\tag{4}
\]
where the value is understood by continuation at regular points and by the
standard limiting convention at \(s=1\) for the completed logarithmic
derivative.  The pole of \(\zeta\) is cancelled inside \(\xi\), so \(q\) is
regular at \(s=1\).

## Conditional Poisson theorem in the strip

Assume for the moment that \(q\) is holomorphic in \(\mathcal S\).  Then
\[
  u(s)=\Re q(s)
\]
is harmonic in \(\mathcal S\).  It has at most logarithmic growth in the
vertical direction from the standard completed Euler--Gamma expression, so
the infinite-strip Poisson representation is admissible by exhaustion with
rectangles and letting the horizontal sides tend to infinity.

Let \(a=1/2\), \(b=1\), \(L=b-a=1/2\), and \(x=\sigma-a\in(0,L)\).  For a
harmonic function in the strip \(a<\sigma<b\), the Poisson representation is
\[
  u(\sigma,t)
  =
  \int_{-\infty}^{\infty}
  P_L(x,t-\tau)\,u(a,\tau)\,d\tau
  +
  \int_{-\infty}^{\infty}
  P_L(L-x,t-\tau)\,u(b,\tau)\,d\tau,
\tag{5}
\]
with positive kernel
\[
  P_L(x,y)=
  {1\over 2L}\,
  {\sin(\pi x/L)\over
  \cosh(\pi y/L)-\cos(\pi x/L)}.
\tag{6}
\]

Using (3) and (4), (5) gives
\[
  u(\sigma,t)
  =
  \int_{-\infty}^{\infty}
  P_{1/2}(1-\sigma,t-\tau)\,u(1,\tau)\,d\tau
  \ge0.
\tag{7}
\]

Therefore:

\[
  \boxed{
  \hbox{zero-free strip }1/2<\Re s<1
  \quad+\quad
  \Re q(1+it)\ge0
  \Longrightarrow
  \Re q(s)\ge0\hbox{ in the strip.}
  }
\tag{8}
\]

This is a useful representation, but the first hypothesis is exactly the
support statement that the project is trying to prove.

## Green correction when poles are present

Now suppose \(\xi\) has a zero
\[
  \rho=\beta+i\gamma,
  \qquad
  {1\over2}<\beta<1,
\]
of multiplicity \(m\).  Then
\[
  q(s)={m\over s-\rho}+h(s)
\tag{9}
\]
near \(\rho\), with \(h\) holomorphic.

Taking real parts,
\[
  \Re {m\over s-\rho}
  =
  m\,{\sigma-\beta\over(\sigma-\beta)^2+(t-\gamma)^2}.
\tag{10}
\]

For points with \(t=\gamma\) and \(\sigma<\beta\),
\[
  \Re {m\over \sigma+i\gamma-\rho}
  =
  -{m\over \beta-\sigma}
  \longrightarrow -\infty
  \qquad(\sigma\uparrow\beta).
\tag{11}
\]

Thus every interior zero with \(\beta>1/2\) forces
\[
  \Re q(s)<0
\]
arbitrarily close to the pole from the left.  No positive boundary term on
\(\sigma=1\), and no zero boundary value on \(\sigma=1/2\), can remove this
local negative divergence.

Equivalently, the Green representation in a rectangle
\[
  \mathcal S_R=\left\{1/2<\sigma<1,\ |t|<R\right\}
\]
has the schematic form
\[
  u(s)
  =
  \hbox{Poisson boundary contribution}
  +
  \sum_{\rho\in\mathcal S_R}
  m_\rho\Re {1\over s-\rho}
  +
  \hbox{regular harmonic correction},
\tag{12}
\]
with the same local principal part (10).  The pole term is not
sign-preserving in the strip: it is positive to the right of \(\rho\) and
negative to the left of \(\rho\).

## Exact logical status

The strip Poisson idea therefore gives the following equivalence-level
normal form:
\[
\begin{array}{c}
q=\xi'/\xi\hbox{ holomorphic in }\mathcal S
\\
+\ \Re q(1/2+it)=0
\\
+\ \Re q(1+it)\ge0
\end{array}
\quad\Longrightarrow\quad
\Re q(s)\ge0\quad(s\in\mathcal S).
\tag{13}
\]

But
\[
  q\hbox{ holomorphic in }\mathcal S
  \Longleftrightarrow
  \xi\hbox{ has no zeros in }1/2<\Re s<1.
\tag{14}
\]

By the functional equation, (14) is equivalent to RH.  Hence (13) is not an
independent proof of the strip target; it is the Poisson representation of
the same RH-strength theorem after the hard support assertion has already
been supplied.

The no-go is local and unavoidable:
\[
  \rho\in\mathcal S
  \quad\Longrightarrow\quad
  \inf_{s\to\rho,\ \Re s<\Re\rho}
  \Re{\xi'\over\xi}(s)=-\infty.
\tag{15}
\]

Therefore a viable Poisson/Green closure must produce a new theorem of one
of the following forms:

1. an Euler--Gamma proof that the Green pole sum in \(\mathcal S\) is empty;
2. an Euler--Gamma positive representation of \(q\) in the strip, which
   automatically excludes poles;
3. a compact A1 proof that bypasses the strip and gives Li positivity
   directly.

## Relation to A1

The strip formula does not improve the compact A1 budget
\[
  K_n(T_n)+{3\over4}\lambda_n^{\rm arch}\ge0
  \qquad(n\ge8)
\]
by itself.  It only rewrites the global Toeplitz/Schoenberg target of
`172`--`174`.

If a non-circular Euler--Gamma theorem proves the holomorphic strip
positivity in (1), then `175` gives RH and Li closes Omega7.  If the goal is
to close the compact A0/A1 assembly specifically, one still needs the
stronger Toeplitz margin of `164` or a direct A1 signed-core proof.

## Status

Closed as a Poisson/Green audit.

The route is conditionally positive but circular unless it includes an
independent no-interior-pole theorem.  A1 remains open.
