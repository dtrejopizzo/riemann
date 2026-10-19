# R170_863 — Null anchor of divisor incidence

> **Audit R170_865.** The identities, the positivity of the Laplacian and
> the equivalence with `a=Lambda` when the column `y=log` is kept fixed
> are correct. However, since `partial=[B,-I]` is surjective, its
> kernel is the universal graph `y=Bx`; nullity is not by itself a
> new positive law nor a canonical anchor of the physical port.
> R170_865 downgrades this construction to a faithful presentation of the
> divisor identity. Extending it to the port with positivity remains
> exactly the open problem, not a consequence of the Laplacian.

> **Correction R170_864 (Poisson gluing).** The anchor and the normal jet
> `(A_raw-K_-)_{<=N}` built here are correct for the hyperbolic
> cell. That jet cannot be sent in isolation to the physical port:
> the Poisson--`X` cell contributes `-K_-` with the orientation that cancels
> the whole Chebyshev jet. R170_864 builds the glued ledger. The missing
> Green map must act on the full PC normal, not on (7.3)
> as written.

## 0. Result

The exact identity

\[
 \sum_{d\mid k}\Lambda(d)=\log k                              \tag{0.1}
\]

does admit a realization as the null vector of a finite positive form.
For `M>=N`, one constructs an incidence complex whose paths are the
pairs `(d,m)` with `dm=k<=N`. The arithmetic vector formed by the weights
`Lambda(d)` and `log k` belongs exactly to the kernel of its Laplacian.

This construction satisfies three difficult conditions:

* it uses all divisors and the exact values of `Lambda`;
* it is uniform: the same law holds for every `N`;
* it fails for every nontrivial interior modification of `Lambda`.

However, the first antidiagonal jet of the hyperbola is normal to the
kernel, and the positive Laplacian only sees it at second order. For this reason the
constructed anchor does not yet close R170_862: a Green formula is
missing that identifies the linear boundary jet with the full exterior defect.

## 1. Finite incidence complex

Fix integers `M>=N>=1`. Let

\[
 \mathcal P_{M,N}^{\rm int}
 :=\{(d,m):1\le d\le M,\ 1\le m\le N,\ dm\le N\},          \tag{1.1}
\]

\[
 C_1:=\mathbb R^{\mathcal P_{M,N}^{\rm int}}
       \oplus\mathbb R^{\{1,\dots,N\}},
 \qquad
 C_0:=\mathbb R^{\{1,\dots,N\}}.                          \tag{1.2}
\]

Write an element of `C1` as `(x,y)`, with coordinates `x_{d,m}` and
`y_k`. Define

\[
 \boxed{
 (\partial_{M,N}(x,y))_k
 :=\sum_{dm=k}x_{d,m}-y_k.}                                \tag{1.3}
\]

Since `k<=N<=M`, every divisor `d|k` and its complement `m=k/d`
appear in (1.3). There is no incomplete fiber in the interior block.

The incidence Laplacian is

\[
 \boxed{\Delta_{M,N}:=\partial_{M,N}^*\partial_{M,N}\succeq0.}
                                                                    \tag{1.4}
\]

## 2. The von Mangoldt anchor

Define `e_Lambda in C1` by

\[
 x_{d,m}^{\Lambda}:={\Lambda(d)\over\sqrt{dm}},
 \qquad
 y_k^{\Lambda}:={\log k\over\sqrt k}.                     \tag{2.1}
\]

Then, on fiber `k`,

\[
 (\partial e_\Lambda)_k
 ={1\over\sqrt k}
 \left(\sum_{d\mid k}\Lambda(d)-\log k\right)=0.          \tag{2.2}
\]

Therefore

\[
 \boxed{e_\Lambda\in\ker\partial_{M,N}
       =\ker\Delta_{M,N}.}                                 \tag{2.3}
\]

This is a nullity inside the positive form (1.4). R170_865 clarifies
its scope: because of the free column `y`, the kernel is a universal graph;
the arithmetic lies in externally fixing `y_k=log k/sqrt k`, not in any
rigidity intrinsic to the Laplacian.

## 3. Arithmetic rigidity

For a real sequence `a(d)` with `a(1)=0`, define `e_a` by replacing
`Lambda(d)` with `a(d)` while keeping `y_k=log k/sqrt k`. Then

\[
 (\partial e_a)_k
 ={(a*\mathbf1)(k)-\log k\over\sqrt k}.                    \tag{3.1}
\]

Thus

\[
 \boxed{
 e_a\in\ker\Delta_{M,N}
 \Longleftrightarrow
 (a*\mathbf1)(k)=\log k\quad(1\le k\le N).}               \tag{3.2}
\]

By Möbius inversion,

\[
 (3.2)\Longleftrightarrow a(k)=\Lambda(k)quad(1\le k\le N).
                                                                    \tag{3.3}
\]

In particular, every nonzero finite modification within `[1,N]` takes
the anchor out of the kernel. For DH/DMV coefficients there is no
positive relation (2.3) with the same `log k` side. This provides exactly the
F3 selectivity that was missing from the abstract Tate port.

## 4. Operator version over the window

Let `mathcal H=L2(R)` or a common core of smooth functions. Tensor the
complex with `mathcal H`. For `F in mathcal H`, define

\[
 \begin{aligned}
 x_{d,m}^{\Lambda}(F)
   &={\Lambda(d)\over\sqrt{dm}}\tau_{\log(dm)}F,\\
 y_k^{\Lambda}(F)
   &={\log k\over\sqrt k}\tau_{\log k}F.
 \end{aligned}                                             \tag{4.1}
\]

All paths in a fiber end at the same translation. By
(0.1),

\[
 \boxed{(\partial_{M,N}\otimes I)e_\Lambda(F)=0}           \tag{4.2}
\]

for every `F`. The form

\[
 \mathcal E_{M,N}(X)
 :=\|(\partial_{M,N}\otimes I)X\|_{C_0\otimes\mathcal H}^2
                                                                    \tag{4.3}
\]

is positive and contains the null subspace
`{e_Lambda(F):F in mathcal H}`.

Compression to a window does not break (4.2) if it is applied after summing
each complete fiber. Inserting `P_T` between the `(d,m)` factors can
create boundary routes and is not authorized in (4.2).

## 5. Two-scale deformation

To preserve both legs before recombining, set

\[
 \begin{aligned}
 x_{d,m}(r,q;F)
 &:={\Lambda(d)\over\sqrt{dm}}
   \tau_{\log d/r+\log m/q}F,\\
 y_k(r,q;F)
 &:={r\over q}{\log k\over\sqrt k}
   \tau_{\log k/q}F.
 \end{aligned}                                             \tag{5.1}
\]

At `(r,q)=(1,1)`, (5.1) returns to (4.1), so that

\[
 \partial e_\Lambda(1,1;F)=0.                              \tag{5.2}
\]

Moreover, upon summing the fibers, `partial e_Lambda(r,q;F)` is exactly the
interior block of

\[
 H_{M,N}(r,q)F=L_M(r)S_N(q)F-K_N(r,q)F.                    \tag{5.3}
\]

Its antidiagonal derivative at the base is

\[
 \boxed{
 \partial_-\bigl(\partial e_\Lambda(r,q;F)\bigr)|_{1,1}
 =\bigl(\mathcal A^{\rm raw}_{M,N}-K_-\bigr)_{\le N}F.}    \tag{5.4}
\]

For `M>=N`, the right-hand side preserves the first jet even though the
base value is zero. This is the incidence version of `H_-=A_raw-K_-` from
R170_856.

## 6. Why the Laplacian loses the first jet

Consider the positive energy

\[
 E(r,q;F):=\|\partial e_\Lambda(r,q;F)\|^2.                \tag{6.1}
\]

By (5.2),

\[
 E(1,1;F)=0,
 \qquad
 \partial_-E(1,1;F)=0.                                    \tag{6.2}
\]

The first nontrivial information is of second order:

\[
 \partial_-^2E(1,1;F)
 =2\| (\mathcal A^{\rm raw}-K_-)_{\le N}F\|^2\ge0.         \tag{6.3}
\]

Thus the Laplacian produces a Hermitian square and loses the orientation
of jet (5.4). Retaining (5.4) by means of the incidence Dirac

\[
 \mathbb D_\partial=
 \begin{pmatrix}0&\partial^*\\\partial&0\end{pmatrix}     \tag{6.4}
\]

preserves orientation, but `mathbb D_partial` is indefinite. This is
the same dichotomy found in R170_854 and R170_861, now within the
exact arithmetic complex.

## 7. Relation to the bordered null anchor

R170_862 called for an arithmetic null vector inside a positive form. Equation
(2.3) constructs it. What is still missing is for the mixed block between the
anchor `e_Lambda` and the image of the contact vector to have jet

\[
 \mathfrak W_K(f)+\Theta_{\rm ext}(f).                     \tag{7.1}

The Laplacian alone cannot do this: between two vectors of its kernel, its
first jet vanishes tautologically, while (5.4) lives in the normal space
`C0 tensor mathcal H`. A Green map is needed

\[
 \mathfrak G_T:C_0\otimes\mathcal H
 \longrightarrow (\text{exterior--Tate port})^*          \tag{7.2}

such that

\[
 \boxed{
 \mathfrak G_T\bigl((\mathcal A^{\rm raw}-K_-)_{\le N}f\bigr)
 =\mathfrak W_K(f)+\Theta_{\rm ext}(f),}                   \tag{7.3}

after adding the tails `k>N`, the reflected orientation and the
polar continuum of R170_856.

Equation (7.3) describes the hyperbolic cell, but it is not yet an admissible
closure target. R170_864 shows that the Poisson--`X` normal must be glued
first, which eliminates `K_-`, together with the reflected orientation. The
anchor already exists; the missing piece is the Green map from the normal
derivative of the **glued PC complex** to the full physical port.

## 8. Status

```text
divisor incidence complex                                 BUILT
Laplacian Delta=partial*partial >=0                        PROVED
e_Lambda belongs to the kernel                            PROVED
rigidity: nullity equivalent to a=Lambda in [1,N]         PROVED
operator version e_Lambda(F) null                         PROVED
normal jet = (A_raw-K_-)_{<=N}F                           PROVED
positive energy only sees the square of the jet           PROVED
Green map of the isolated hyperbolic cell, (7.3)          INADMISSIBLE
Green map of the glued PC complex                          OPEN R170_864
exterior law / VIR--LB / D                                OPEN
```
