# Euler product positive-weight audit

## Question

Can A1 be proved directly from the positivity of the Euler-product weights
\(\Lambda(m)\)?

In the half-plane \(\Re s>1\),
\[
  -{\zeta'\over\zeta}(s)
  =
  \sum_{m\ge2}{\Lambda(m)\over m^s},
]
and the coefficients \(\Lambda(m)\) are nonnegative. This is the most
tempting source of positivity.

## Direct obstruction

The Li prime kernel is not positive:
\[
  L_{n-1}^{(1)}(\log m)
\]
changes sign many times in the transition and oscillatory ranges. Therefore
\[
  \sum_m{\Lambda(m)\over m}L_{n-1}^{(1)}(\log m)
\]
is not a positive-weight integral of a positive test.

The pole subtraction is essential:
\[
  \lambda_n^{\rm prime}
  =
  \lim_{\varepsilon\downarrow0}
  \left[
  \sum_{k=1}^n {n\choose k}{(-1)^{k-1}\over\varepsilon^k}
  -
  \sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
  L_{n-1}^{(1)}(\log m)
  \right].
\]

The first term is not a positive measure term. It is the renormalizing pole
needed to give the prime sum a boundary value.

## Continuation obstruction

The positive Euler-product measure lives only in the half-plane of absolute
convergence. Moving to the Li boundary requires adding:

- the pole at \(s=1\);
- the Gamma factor;
- the functional-equation reflection;
- the paired boundary prescription.

These pieces form a signed current. Analytic continuation preserves the
identity, but it does not preserve the elementary positivity of the
Euler-product coefficients.

## Exact no-go class

The following class cannot close A1:
\[
  \hbox{positive Euler-product weights}
  +
  \hbox{absolute or pointwise control of the Laguerre kernel}.
\]

It fails because the Laguerre test is signed and because the pole/Gamma
renormalization is not a positive local correction.

This no-go eliminates only direct coefficient positivity. It does not
eliminate a global Euler--Gamma identity in which the signed pieces recombine
before any estimate.

## Live replacement

The replacement target is a positive boundary measure for the completed
object, not for the raw Euler product:
\[
  {\xi'\over\xi}\left({1\over2}+z\right)
  =
  A z+
  \int_{\mathbb R}
  \left({1\over z-it}+{1\over z+it}\right)d\mu(t),
  \qquad \mu\ge0.
\]

If \(\mu\ge0\) is constructed from the full Euler--Gamma package, then A1
closes. Positivity of the raw Euler-product weights alone does not construct
this \(\mu\).

## Status

The direct positive-weight route is eliminated. The global completed
positive-measure route remains open.
