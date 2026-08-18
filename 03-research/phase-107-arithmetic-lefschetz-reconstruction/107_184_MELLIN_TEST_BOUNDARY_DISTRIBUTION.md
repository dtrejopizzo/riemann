# 107.184 -- Mellin inversion turns the boundary channel into the prime distribution

## 1. Test space and transform

Let \(g\in C_c^\infty(\mathbb R)\), or more generally let \(g\) be a
Schwartz function with sufficient bilateral exponential decay.  Define
its bilateral Laplace--Mellin transform by

\[
 F_g(s)=\int_{\mathbb R}g(x)e^{sx}\,dx.
 \tag{1.1}
\]

For any vertical line in its strip of convergence,

\[
 g(x)={1\over2\pi i}\int_{\Re s=c}F_g(s)e^{-sx}\,ds.
 \tag{1.2}
\]

## 2. Finite-prime distribution

Take \(c>1\) and pair (1.1) with the finite boundary channel of
`107_182`:

\[
 \mathcal D_{\rm fin}(g)
 ={1\over2\pi i}\int_{\Re s=c}
 F_g(s)\left(-{\zeta'(s)\over\zeta(s)}\right)ds.
 \tag{2.1}
\]

Absolute convergence permits interchange with the Euler series.  Using
(1.2),

\[
 \boxed{
 \mathcal D_{\rm fin}(g)
 =\sum_{n\ge2}\Lambda(n)g(\log n)
 =\sum_p\sum_{k\ge1}\log p\,g(k\log p).}
 \tag{2.2}
\]

This is the exact prime-orbit distribution: \(k\log p\) is the length
of the \(k\)-fold orbit and \(\log p\) is its Lefschetz weight.

## 3. Completed distribution

Replacing the finite channel in (2.1) by `107_183` defines

\[
 \mathcal D_{\rm comp}(g;c)
 ={1\over2\pi i}\int_{\Re s=c}
 F_g(s)\left(-{\xi'(s)\over\xi(s)}\right)ds.
 \tag{3.1}
\]

The vertical decay of \(F_g\) and logarithmic vertical growth of the
completed logarithmic derivative make (3.1) a continuous distribution
on the stated test space.  Its decomposition is the prime distribution
(2.2) plus the Gamma and pole distributions.

Contour displacement, together with
\(\mathscr G_{\rm comp}(1-s)=-\mathscr G_{\rm comp}(s)\), gives the
spectral zero residues.  This is the standard explicit-formula
mechanism, now factored through the boundary Euler classes constructed
in `107_178`.

## 4. Result and geometric gap

The scalar test-function distribution required before constructing a
Green current is now complete:

\[
 \text{localized boundary class}
 \longrightarrow -\xi'/\xi
 \longrightarrow \mathcal D_{\rm comp}.
\]

This does not yet identify \(\mathcal D_{\rm comp}(g)\) with an
archimedean Green function on a global arithmetic surface.  Such an
identification must provide:

1. a Green current \(G_g\) whose trace against the boundary normal class
   is (3.1);
2. an algebraic finite-support component paired with it;
3. compatibility with convolution/involution of Weil tests;
4. the primitive self-pairing and radical identity.

## 5. Falsifier

For Gaussian Schwartz tests

\[
 g_{\mu,\sigma}(x)=e^{-(x-\mu)^2/(2\sigma^2)},
\]

the transform (1.1) is explicit.  The verifier independently computes
the vertical contour integral of a fixed prime-truncated boundary
channel and the corresponding prime-power sum in (2.2).  The prime
cutoff, contour, mesh, and three tests are fixed before evaluation.  Any
error above \(10^{-7}\) returns `VERDICT: NO`.
