# R170_866 — The multiplicatively compatible null line is exactly Lambda

## 0. Result

R170_865 shows that assigning independent variables to each route `(d,m)`
produces a huge null graph. Unique factorization requires an
additional compatibility: the same coefficient `a_d` must be used across all
routes starting at `d`. Once imposed, the complex changes
completely.

Define

\[
 \mathscr D_N:\mathbb R^N\oplus\mathbb R\longrightarrow\mathbb R^N,
 \qquad
 (\mathscr D_N(a,c))_k
 ={1\over\sqrt k}\left(\sum_{d\mid k}a_d-c\log k\right).   \tag{0.1}
\]

Then

\[
 \boxed{\ker\mathscr D_N=\mathbb R\,(\Lambda|_{[1,N]},1).} \tag{0.2}
\]

Hence the Laplacian

\[
 \boxed{\mathscr L_N:=\mathscr D_N^*\mathscr D_N\succeq0} \tag{0.3}
\]

has a unique null line, and that line is exactly von Mangoldt together
with the Chebyshev column. This nullity is not the universal graph of
R170_863: it uses the fact that `a_d` repeats coherently across all its multiples.

The two-scale operator version preserves that line at the base and its
normal jet is again the interior hyperbolic block
`A_raw-K_-`. R170_864 still applies: to reach the physical port one must
glue the Poisson cell before using the jet.

## 1. The convolution matrix is unitriangular

Let

\[
 (U_Na)_k:=\sum_{d\mid k}a_d.                              \tag{1.1}

Order the coordinates by the integer `1,2,...,N`. In row `k`, only
divisors `d<=k` appear, and the coefficient of `a_k` is one. Hence
`U_N` is lower triangular with diagonal one:

\[
 \det U_N=1.                                               \tag{1.2}

Its inverse is the Möbius-truncated convolution,

\[
 (U_N^{-1}b)_k=\sum_{d\mid k}\mu(d)b_{k/d}.                \tag{1.3}

The diagonal factor `k^{-1/2}` of (0.1) is invertible and does not change kernels.

## 2. Null-line theorem

**Theorem 2.1.** For every `N>=1`, (0.2) holds.

**Proof.** `mathscr D_N(a,c)=0` is equivalent to

\[
 U_Na=c\,(\log k)_{k\le N}.                                \tag{2.1}

Since `U_N` is invertible,

\[
 a=c\,U_N^{-1}\log.                                       \tag{2.2}

The Möbius identity

\[
 \mu*\log=\Lambda                                         \tag{2.3}

gives `a=c Lambda` on `[1,N]`. Conversely,
`Lambda*1=log` proves that every multiple `(cLambda,c)` lies in the kernel.
QED.

In particular,

\[
 \dim\ker\mathscr L_N=1.                                  \tag{2.4}

The normalization `c=1` selects a single vector, not an affine section of
a large kernel.

## 3. Precise difference from R170_863

In R170_863, each `x_{d,m}` could vary independently and

\[
 \partial(x,y)=Bx-y.                                       \tag{3.1}

Here `x` is restricted to the multiplicatively compatible subspace

\[
 \mathcal C_{\rm mult}
 :=\left\{x_{d,m}={a_d\over\sqrt{dm}}\text{ for some }a\right\},
                                                                    \tag{3.2}
\]

and the column `y` to the line

\[
 \mathcal C_{\log}
 :=\left\{y_k={c\log k\over\sqrt k}:c\in\mathbb R\right\}.
                                                                    \tag{3.3}
\]

The restriction of `partial` to
`mathcal C_mult direct-sum mathcal C_log` is exactly `mathscr D_N`.
The dimensions are `N+1 -> N`; the surjectivity of `U_N` leaves the
smallest possible kernel, of dimension one.

This compatibility is not decorative. It expresses that `Lambda(d)` belongs
to the Euler factor `d` and cannot be chosen anew for each complement
`m`. It is the multiplicative interaction that was lost when the routes were
treated as independent edges.

## 4. Rigidity against modifications

For a sequence `a` normalized with column `c=1`,

\[
 \|\mathscr D_N(a,1)\|^2
 =\sum_{k\le N}{|(a*\mathbf1)(k)-\log k|^2\over k}.        \tag{4.1}

Thus

\[
 \boxed{
 \|\mathscr D_N(a,1)\|=0
 \Longleftrightarrow a(k)=\Lambda(k)\quad(k\le N).}        \tag{4.2}
\]

This does not use mere support or nonnegativity. Any finite interior
modification produces strictly positive energy at the first multiple
where it differs, and inversion (1.3) recovers the full defect.

The law is compatible as `N` increases: the null lines project
into one another and determine the full sequence `Lambda`.

## 5. Operator tensorization

Let `mathcal H` be a common core. For data `(a,c)` and `F in mathcal H`,
define

\[
\begin{aligned}
 (\boldsymbol{\mathscr D}_{N}(r,q)((a,c)\otimes F))_k
 :={}&{1\over\sqrt k}\sum_{d\mid k}a_d
   \tau_{\log d/r+\log(k/d)/q}F\\
 &-c\,{r\over q}{\log k\over\sqrt k}
   \tau_{\log k/q}F.                                      \tag{5.1}
\end{aligned}

At the base,

\[
 \boldsymbol{\mathscr D}_{N}(1,1)((\Lambda,1)\otimes F)=0
 \quad\text{for every }F.                                 \tag{5.2}

Moreover, if (5.2) holds for every `F` and distinct translations are read
fiber by fiber, Theorem 2.1 forces `(a,c)` to belong to the line
`R(Lambda,1)`.

The operator Laplacian

\[
 \boldsymbol{\mathscr L}_N(r,q)
 :=\boldsymbol{\mathscr D}_N(r,q)^*
   \boldsymbol{\mathscr D}_N(r,q)\succeq0                 \tag{5.3}
\]

has at `(1,1)` the null subspace

\[
 \mathbb R(\Lambda,1)\otimes\mathcal H.                   \tag{5.4}

The infinite degeneracy in `F` is physical; the arithmetic direction is
unique.

## 6. Normal jet and mandatory gluing

Differentiating (5.1) in the antidiagonal direction gives

\[
 \boxed{
 \partial_-\boldsymbol{\mathscr D}_{N}(1,1)
 ((\Lambda,1)\otimes F)
 =(\mathcal A^{\rm raw}_{M,N}-K_-)_{\le N}F,}              \tag{6.1}

for any `M>=N`; the divisors `d<=N` are already all that is needed
in the interior fibers.

As in R170_863, the first derivative of the energy (5.3) vanishes in the
kernel and the second jet is the square of (6.1). This does not sign the
port.

Furthermore, R170_864 proves that (6.1) is not an independent physical
normal: the Poisson face contributes `-K_-` and the gluing leaves `-A_raw`
with the other PC faces. Hence the null line must be extended to the
glued PC complex, not paired directly with (6.1).

## 7. What has been built and what remains

For the first time, a finite positive object has been built with these three
simultaneous properties:

1. its arithmetic null direction is unique;
2. that direction is exactly `(Lambda,1)`;
3. the construction is compatible across all cutoffs `N`.

This repairs the fatal defect of R170_863. Two steps still remain:

* extending the null line to the Poisson, reflected, polar and Tate cells without
  turning the whole PC into a weight-blind nullity;
* identifying the mixed block of that extension with
  `mathfrak W_K+Theta_ext` and obtaining the second positive orientation of
  R170_862.

The new obligation is concrete: build a positive extension of the
Laplacian `mathscr L_N` to the R170_856 ledger whose nullity retains dimension
one in the arithmetic coordinate and whose boundary is the combined port.

## 8. Status

```text
multiplicative compatibility x_{d,m}=a_d/sqrt(dm)         IMPOSED
U_N:a -> a*1 unitriangular and invertible                  PROVED
ker D_N = R (Lambda,1)                                     PROVED
L_N=D_N^*D_N >=0 with unique null line                      PROVED
rigidity against every interior modification               PROVED
uniform compatibility as N varies                          PROVED
tensorization and normal jet A_raw-K_-                      PROVED
positive extension to the glued PC complex                  OPEN
exterior law / VIR--LB / D                                 OPEN
```
