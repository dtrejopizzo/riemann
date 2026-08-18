# Row (d): monoidal Hardy realization of the archimedean character

## Status

This note proves the previously missing categorical comparison for the
archimedean place.  The oscillator boundary module is the even Hardy
dilation representation, and its ordinary nuclear character is exactly
Meyer's Fourier--archimedean kernel away from the single finite-part point.
The construction is monoidal and zero-free.  The remaining comparison is
the finite-prime/primitive coupling.

## 1. Even Hardy dilation

Let

\[
 H^2_{\rm ev}=\overline{\operatorname{span}}\{z^{2k}:k\ge0\}
\]

inside the Hardy space of the disk.  For `x>1` define

\[
 T_xz^{2k}=x^{-2k}z^{2k}.                             \tag{1}
\]

Then `T_x` is positive trace class and

\[
 T_xT_y=T_{xy}.                                       \tag{2}
\]

Thus `x -> T_x` is a genuine monoidal representation of the multiplicative
semigroup `(1,infinity)`.

Take two identical copies and write `Pi_infty(x)=T_x direct-sum T_x`.

### Proposition 1.1

For every `x>1`,

\[
 \operatorname{Tr}\Pi_\infty(x)
 =\frac{2}{1-x^{-2}}
 =\frac{x}{x-1}+\frac{x}{x+1}.                       \tag{3}
\]

### Proof

Sum the two geometric eigenvalue series.  The final equality is elementary.

## 2. Equality with the Fourier--archimedean distribution

Away from `x=1`, row (c) has

\[
 W_\infty(h)=\int_0^\infty
 h(x)\left(\frac1{|1-x|}+\frac1{1+x}\right)dx,       \tag{4}
\]

with the Fourier finite part used only at `x=1`.

### Theorem 2.1

If `h` is compactly supported in `(1,infinity)`, then

\[
 W_\infty(h)
 =\operatorname{Tr}\left(
   \int_1^\infty h(x)\Pi_\infty(x)\,d^\times x
                         \right).                    \tag{5}
\]

The operator integral is trace class and the same formula is compatible
with multiplicative convolution.

### Proof

On a compact set separated from one, (3) is bounded.  Tonelli for the
positive and negative parts, or dominated convergence for a general smooth
`h`, interchanges trace and integral.  Since `dx=x d^times x`, (3) turns
the right side into

\[
 \int h(x)\left(\frac1{x-1}+\frac1{x+1}\right)dx,
\]

which is (4) on `x>1`.  Equation (2) gives

\[
 \Pi_\infty(h_1\star h_2)
 =\Pi_\infty(h_1)\Pi_\infty(h_2)
\]

whenever the supports remain in the semigroup chart; extension follows by
the usual nondegenerate integrated representation.

For support in `(0,1)`, Tate conjugation `x -> x^{-1}` supplies the second
chart.  Gluing the two charts still requires the prescribed Fourier finite
part at the identity; no arbitrary constant is introduced here.

## 3. Central normalization and the oscillator

The centrally normalized representation is

\[
 \Pi_{\infty,1/2}(x)=x^{-1/2}\Pi_\infty(x).           \tag{6}
\]

Its two copies have eigenvalues

\[
 x^{-(2k+1/2)},\qquad k\ge0.                          \tag{7}
\]

Writing `x=e^r`, the heat trace in one copy is

\[
 \sum_{k\ge0}e^{-(2k+1/2)r}
 =\frac{e^{-r/2}}{1-e^{-2r}},                         \tag{8}
\]

which is exactly the density of the Gamma translation energy in
`114_d_17_ARCHIMEDEAN_OSCILLATOR_BOUNDARY_MODULE.md`.

Consequently the oscillator operator there is not an appended analytic
model: after identifying its basis with `z^{2k}`, it is the infinitesimal
generator

\[
 2N+\frac12
\]

of the monoidal Hardy dilation (6).

## 4. Correct arithmetic orbit vectors

The cyclic vector `1` has orbit under the adjoints of the resolvent-normalized
dilations described by the even Szego kernels.  For a prime power `n`, the
relevant parameter is

\[
 y_n=n^{-2},                                          \tag{9}
\]

not `n^{-1}` if one works in the even Hardy coordinate.  The normalized
kernel is

\[
 k_n(w)=\frac{\sqrt{1-y_n^2}}{1-y_nw},                \tag{10}
\]

and its nonconstant tail has squared norm `n^{-4}`.  Hence the uniform
contraction estimate strengthens to

\[
 \sum_p\sum_{j\ge1}p^{-4j}
 =\sum_p\frac1{p^4-1}<1.                              \tag{11}
\]

All Lorentzian Szego and Tate-doubling arguments of the preceding two notes
apply verbatim with this sharper parameter.  This replacement is forced by
the actual character (3), and should be used in the final mixed space.

## 5. What is now compared and what is not

Proved:

1. monoidal composition `T_xT_y=T_xy`;
2. exact archimedean character on both open Tate charts;
3. exact central oscillator heat density;
4. a zero-free Hardy source for the archimedean Green Gram.

Not yet proved:

1. extension of (5) through `x=1` with the precise Fourier finite-part
   constant as a determinant of the Hardy boundary extension;
2. a single mixed section object combining this representation with the
   derived finite contacts;
3. identification of its two-ruling primitive form with `B_nuc`.

The remaining finite-part constant is rank two/polar data; the hard part is
the signed finite-prime coupling.  No positivity assertion about
`B_nuc` has been used in this comparison.

