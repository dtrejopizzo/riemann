# Row (d): the equality case requires no additional conjecture

## Status

This note proves that once the primitive Hodge sign is established, its
equality case follows rigorously from the already constructed row-(c)
comparison and the unconditional zero-counting asymptotic.  Thus the only
remaining row-(d) obligation is the sign/contraction itself.

## Theorem

Assume that

\[
 B_{\rm nuc}(f,f)\le0
 \quad\text{for every }f\in\mathcal T^0.              \tag{1}
\]

Then equality in (1) holds only for `f=0`.

## Proof

By Weil's criterion, (1) implies RH.  The spectral character identity of
row (c), with the two polar terms removed by
`hat f(0)=hat f(1)=0`, is then

\[
 B_{\rm nuc}(f,f)
 =-\sum_\rho m_\rho
   \left|\widehat f(\rho)\right|^2.                   \tag{2}
\]

All terms on the right are nonpositive.  Equality forces

\[
 \widehat f(\tfrac12+i\gamma)=0                      \tag{3}
\]

for every nontrivial zero `1/2+i gamma`, with multiplicity irrelevant for
the argument.

In logarithmic coordinates `F(t)=e^{t/2}f(e^t)`, the function

\[
 \mathcal F_F(z)=\int_{\mathbb R}F(t)e^{izt}dt        \tag{4}
\]

is entire of finite exponential type by Paley--Wiener, and (3) says that it
vanishes at every ordinate `gamma`.  A nonzero entire function of finite
exponential type has `O(R)` zeros in `|z|<=R`: this follows directly from
Jensen's formula and the bound `log|F_F(z)|<=C+tau|z|`.

On the other hand the Riemann--von Mangoldt formula, which is unconditional,
gives, with multiplicities,

\[
 N(R)=\frac{R}{2\pi}\log\frac{R}{2\pi e}+O(\log R).  \tag{5}
\]

We must not silently replace multiplicity by distinctness.  Under RH the
classical Littlewood bound for the argument of zeta gives

\[
 m(\tfrac12+i\gamma)
 =O\left(\frac{\log\gamma}{\log\log\gamma}\right).    \tag{6}
\]

(Apply the RH bound for `S(T)` to the jump of the zero-counting function
across an interval shrinking to `gamma`.)  Combining (5) and (6), the
number of distinct ordinates up to `R` is at least
`c R log log R`, which is not `O(R)`.  Hence (4) must be identically zero.
Fourier injectivity gives `F=0` and therefore `f=0`.

The use of zeros here is logically downstream of (1): it proves uniqueness
after RH has already been derived and does not enter the construction of the
Hodge sign.
