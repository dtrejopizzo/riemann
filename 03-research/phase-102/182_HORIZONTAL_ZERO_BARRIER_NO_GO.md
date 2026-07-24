# Horizontal zero-barrier no-go

## Purpose

`176_HORIZONTAL_XI_MODULUS_MONOTONICITY_GATE.md` rewrites the global
half-plane target as
\[
  \partial_\sigma\log|\xi(\sigma+it)|\ge0
  \qquad(\sigma>1/2).
\tag{1}
\]

`178_STRIP_POISSON_BOUNDARY_NO_GO.md`--`180_STRIP_POISSON_KERNEL_FORMULA.md`
show that favorable vertical boundary data do not imply (1) unless the strip
is already zero-free.  This note records the same obstruction directly at
the level of horizontal modulus monotonicity.

The conclusion is a local barrier theorem: a single zero off the critical
line produces an infinite downward wall for
\(\log|\xi(\sigma+it)|\) along a horizontal line.  Therefore no proof based
only on symmetry, subharmonicity, boundary averages, or bounded correction
terms can establish (1).  A successful proof must either exclude the zero or
produce a genuinely singular Euler--Gamma mechanism that cancels its local
barrier without assuming it absent.

## Local factorization near an off-line zero

Let
\[
  \rho=\beta+i\gamma,\qquad {1\over2}<\beta<1,
\]
be a zero of \(\xi\) of multiplicity \(m\).  Since \(\xi\) is entire, in a
small disk around \(\rho\)
\[
  \xi(s)=(s-\rho)^m a(s),
\tag{2}
\]
where \(a\) is holomorphic and \(a(\rho)\ne0\).

On the horizontal line \(t=\gamma\), put \(s=\sigma+i\gamma\).  Then
\[
  \log|\xi(\sigma+i\gamma)|
  =
  m\log|\sigma-\beta|
  +
  \log|a(\sigma+i\gamma)|.
\tag{3}
\]

For \(\sigma\ne\beta\),
\[
  \partial_\sigma\log|\xi(\sigma+i\gamma)|
  =
  {m\over \sigma-\beta}
  +
  \partial_\sigma\log|a(\sigma+i\gamma)|.
\tag{4}
\]

The second term is bounded in a sufficiently small closed punctured
neighborhood of \(\rho\), because \(a\) is nonvanishing there.  Hence there
exists \(\delta>0\) such that
\[
  \partial_\sigma\log|\xi(\sigma+i\gamma)|<0
  \qquad(\beta-\delta<\sigma<\beta).
\tag{5}
\]

Moreover
\[
  \partial_\sigma\log|\xi(\sigma+i\gamma)|
  \longrightarrow-\infty
  \qquad(\sigma\uparrow\beta).
\tag{6}
\]

Thus any zero with \(\beta>1/2\) forces a strict local failure of the target
(1) inside the right half of the critical strip.

## Integral form of the barrier

For
\[
  \beta-\delta<\sigma_1<\sigma_2<\beta,
\]
equation (3) gives
\[
\begin{aligned}
  \log|\xi(\sigma_2+i\gamma)|
  -
  \log|\xi(\sigma_1+i\gamma)|
  &=
  m\log{\beta-\sigma_2\over\beta-\sigma_1}  \\
  &\quad+
  \log{|a(\sigma_2+i\gamma)|\over|a(\sigma_1+i\gamma)|}.
\end{aligned}
\tag{7}
\]

As \(\sigma_2\uparrow\beta\), the first term tends to \(-\infty\), while the
second term remains bounded.  Hence
\[
  \log|\xi(\sigma_2+i\gamma)|
  <
  \log|\xi(\sigma_1+i\gamma)|
\tag{8}
\]
for all \(\sigma_2\) sufficiently close to \(\beta\) from the left.

This is stronger than the pointwise pole-defect statement: it shows that the
horizontal modulus must decrease before reaching the zero.  A monotonicity
proof cannot repair this with any bounded harmonic, Poisson, or averaging
correction.

## Boundary and subharmonic principles cannot remove the barrier

The functional equation gives the horizontal symmetry
\[
  |\xi(1/2+u+it)|=|\xi(1/2-u+it)|.
\tag{9}
\]
But symmetry only says that the critical line is a stationary symmetry axis
where regular; it does not make the axis a minimum along every horizontal
line.

Likewise, \(\log|\xi|\) is subharmonic.  Its Riesz mass is supported at the
zeros of \(\xi\).  Subharmonicity controls two-dimensional averages, while
(1) is a one-dimensional monotonicity theorem.  The mass at \(\rho\) creates
the logarithmic wall (3), and the wall is exactly what invalidates a
boundary-only argument.

Therefore the following inference is invalid:
\[
  \hbox{functional-equation symmetry}
  \quad+\quad
  \hbox{subharmonicity or positive boundary averages}
  \quad\Longrightarrow\quad
  \partial_\sigma\log|\xi|\ge0.
\tag{10}
\]

It becomes valid only after the interior zero mass in
\({1\over2}<\Re s<1\) has been excluded or after a new singular positive
mechanism is proved to dominate it.

## Relation to the log-derivative and A1 gates

Differentiating (3) gives exactly the pole defect from
`179_STRIP_GREEN_POLE_DEFECT_DECOMPOSITION.md`:
\[
  \Re{\xi'\over\xi}(\sigma+i\gamma)
  =
  {m\over\sigma-\beta}+O(1).
\tag{11}
\]

Thus the following three statements are the same obstruction in different
coordinates:

1. the pole defect \(m\Re(s-\rho)^{-1}\) has a negative lobe to the left of
   \(\rho\);
2. the horizontal modulus \(\log|\xi(\sigma+i\gamma)|\) has an infinite
   downward barrier as \(\sigma\uparrow\beta\) from the left;
3. the disk Carathéodory/Toeplitz object would have an interior singularity,
   impossible for a true positive boundary measure.

For the compact A1 route, this means that a proof cannot be a bounded
post-processing of boundary signs.  It must retain the pole, Gamma and
prime terms in a signed global pairing until the off-line barrier is
excluded or neutralized.

## Exact status

Closed as a no-go and target normal form.  A1 remains open.

The live theorem in this coordinate is:
\[
  \boxed{
  \partial_\sigma\log|\xi(\sigma+it)|\ge0
  \qquad(\sigma>1/2,\ t\in\mathbb R)
  }
\]
proved from Euler--Gamma data without assuming absence of zeros in the
strip.  The barrier theorem above shows precisely what such a proof must
overcome.
