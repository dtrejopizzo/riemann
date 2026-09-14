# P122 -- Lions--Magenes and `mu`-transmission audit of Gate R

## Status

`IMPORTED + PROVED APPLICATION`.

The endpoint space is the classical Lions--Magenes space
`H^(1/2)_00`.  The exact interval calculation below shows that, for the
smooth Tate source, membership is equivalent to cancellation of its
boundary trace.  Boutet de Monvel/Hormander--Grubb transmission theory
organizes such boundary conditions but does not supply the missing
condition for a sharply truncated translation.  Gate R is therefore not a
regularity theorem waiting to be quoted; it is the desired trace-matching
law itself.

## 1. Imported boundary-space facts

Lions and Magenes identify the critical interpolation/zero-extension space

\[
 H^{1/2}_{00}(I)
 =[L^2(I),H^1_0(I)]_{1/2,2}                       \tag{1.1}
\]

as the proper subspace of `H^(1/2)(I)` whose zero extension belongs to
`H^(1/2)(R)`.  The original reference is J.-L. Lions and E. Magenes,
*Non-Homogeneous Boundary Value Problems and Applications*, Vol. I,
Springer, 1972, Chapters 1 and 11:

<https://link.springer.com/book/10.1007/978-3-642-65161-8>.

For pseudodifferential operators, the classical transmission property and
its `mu`-transmission extension specify which weighted boundary spaces are
preserved and give Fredholm/regularity and Green formulas.  The applicable
primary modern source is G. Grubb, *Fractional Laplacians on domains, a
development of Hormander's theory of mu-transmission pseudodifferential
operators*, Adv. Math. 268 (2015), 478--528:

<https://arxiv.org/abs/1310.0951>.

Grubb's later boundary-condition treatment explicitly allows local and
nonlocal boundary operators on the `mu`-transmission spaces:

<https://arxiv.org/abs/1403.7140>.

These are imported framework results.  No claim of novelty is made for the
space or calculus.

## 2. Exact one-dimensional norm identity

Let `I=(0,L)`, let `u in H^(1/2)(I)`, and denote its zero extension by
`e_0u`.  Directly splitting the Gagliardo integral into `I x I` and the two
cross-boundary regions gives

\[
 \boxed{
 [e_0u]_{H^{1/2}(\mathbb R)}^2
 =[u]_{H^{1/2}(I)}^2
 +2\int_0^L|u(x)|^2
   \left({1\over x}+{1\over L-x}\right)dx.}        \tag{2.1}
\]

Indeed

\[
 \int_{-\infty}^0{dy\over(x-y)^2}={1\over x},
 \qquad
 \int_L^\infty{dy\over(y-x)^2}={1\over L-x}.      \tag{2.2}
\]

Equation (2.1) proves in this setting the concrete characterization

\[
 H^{1/2}_{00}(I)
 =\left\{u\in H^{1/2}(I):
 \int_0^L{|u(x)|^2\over\operatorname {dist}(x,\partial I)}dx
 <\infty\right\}.                                  \tag{2.3}
\]

For a function continuous at an endpoint, (2.3) forces its trace there to
vanish.  Conversely, a smooth function vanishing at both endpoints obeys
the weighted condition.

## 3. Application to a causal activation seam

At `t_n=-T+log n`, the newly activated summand is, in the local coordinate
`x=t-t_n`,

\[
 \mathbf1_{x>0}n^{-1/2}r_\varepsilon(-T+x).        \tag{3.1}
\]

Its right trace is

\[
 n^{-1/2}c(e^{-T/2}+\varepsilon e^{T/2}).          \tag{3.2}
\]

By (2.1), (3.1) is locally `H^(1/2)` across the seam only if (3.2)
vanishes.  For `T>log 2`, this is equivalent to `c=0`.

Hence, on the Tate line,

\[
 \boxed{
 \text{critical Lions--Magenes transmission across one activation seam}
 \quad\Longleftrightarrow\quad c=0.}               \tag{3.3}
\]

This recovers P122.019 with the exact critical trace space, rather than
only the jump obstruction.

## 4. Why the imported calculi do not prove Gate R

The Grubb calculus assumes that the operator symbol has the appropriate
transmission parity and then describes solutions in a boundary space with
the corresponding trace behavior.  Our operator

\[
 f(t)\longmapsto\mathbf1_{I_T}(t-a)f(t-a)           \tag{4.1}
\]

is a sharply truncated translation: a Fourier integral/shift operation,
not a local classical pseudodifferential operator satisfying the standard
transmission hypothesis at the newly created interior seam.

One can cut the interval at that seam and use boundary calculus on the two
pieces.  Then the extra condition needed to recover global `H^(1/2)` is
exactly matching of the two traces, i.e. (3.3).  The calculus proves the
regularity **after** this transmission condition is imposed; it does not
derive the condition from the scalar first-contact equation.

Thus the literature gives neither a hidden proof nor an impossibility
theorem for a richer source system.  It gives the correct formulation and
shows that the current Gate-R wording can be sharpened to:

> construct, before first contact, a source boundary relation whose
> horizontal sections lie in `H^(1/2)_00` at every Euler activation seam.

On the first-contact Tate line, that structural relation would force `c=0`.
Without such a relation, invoking “Calderon regularity” or
“mu-transmission” assumes the missing boundary matching.

```text
critical zero-extension space H^(1/2)_00       IMPORTED
exact weighted interval norm                    PROVED-IN-REPOSITORY
Tate seam is transmissible iff c=0              PROVED-IN-REPOSITORY
truncated translation covered automatically     FALSE
boundary calculus derives trace matching        FALSE
source-defined matching relation                OPEN
```
