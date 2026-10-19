# R170_865 — Audit of the incidence anchor

> **Repair R170_866.** The no-go of this memo affects the space with
> independent coordinates `x_{d,m}`. R170_866 imposes the multiplicative
> compatibility that was omitted: a single coordinate `a_d` is repeated across all
> multiples `dm`. The homogenized map
> `(a,c) mapsto a*1-c log` is unitriangular and its kernel is exactly
> `R(Lambda,1)`. This yields a canonical positive anchor of dimension
> one, not the universal graph refuted here.

## 0. Verdict

R170_863 contains correct identities:

* `Delta=partial^*partial>=0`;
* the vector with columns `Lambda` and `log` is in its kernel;
* with the column `log` frozen, that nullity characterizes
  `Lambda|_[1,N]` by Möbius;
* its hyperbolic jet is `A_raw-K_-`.

However, the chosen complex has

\[
 \partial=[B,-I],                                         \tag{0.1}
\]

where `B` sums the routes `(d,m)` over the fiber `dm=k`. Due to the
copy `-I`, `partial` is surjective and

\[
 \ker\partial=\{(x,Bx):x\in\mathbb R^{\mathcal P}\}.       \tag{0.2}

Thus nullity is the universal graph of `B`, not a rigidity produced
by positivity. For any coefficient `a`, the vector

\[
 (x^a,y^a),\qquad y^a_k={(a*\mathbf1)(k)\over\sqrt k},      \tag{0.3}

is equally null. The specificity of `Lambda` appears only by separately
fixing `y_k=log k/sqrt k`.

The construction is a faithful and useful presentation of the divisor
identity, but it does not create the exterior null anchor of R170_862. The
missing Green map remains equivalent to the original Tate defect.

## 1. Matrix form

Let

\[
 B:C_{\rm pair}\longrightarrow C_0,\qquad
 (Bx)_k=\sum_{dm=k}x_{d,m}.                                \tag{1.1}
\]

Then the space of R170_863 is

\[
 C_1=C_{\rm pair}\oplus C_0,\qquad
 \partial(x,y)=Bx-y.                                       \tag{1.2}
\]

For each `v in C0`,

\[
 \partial(0,-v)=v,                                        \tag{1.3}
\]

so that

\[
 \operatorname{Ran}\partial=C_0,\qquad H_0(\partial)=0.    \tag{1.4}

Moreover, `partial(x,y)=0` if and only if `y=Bx`, proving (0.2).
There is no homology class that selects `e_Lambda` among the other
null vectors.

## 2. Laplacian and pseudoinverse

The Laplacian on `C1` is positive, but that positivity is universal:

\[
 \Delta=\partial^*\partial
 =\begin{pmatrix}B^*B&-B^*\\-B&I\end{pmatrix}.             \tag{2.1}

On `C0`,

\[
 \partial\partial^*=BB^*+I\succeq I.                      \tag{2.2}

Hence there exists a canonical Green inverse

\[
 \partial^\dagger
 =\partial^*(BB^*+I)^{-1}.                                 \tag{2.3}

This formula depends only on the divisor graph, not on `Lambda`. For
any normal `v in C0`, `partial partial^dagger v=v`. The existence of
an algebraic Green map imposes no sign and nullifies no coordinate of
the port.

If tensored with `L2`, (2.1)--(2.3) still hold fiber by fiber. Compactness,
causality, or physical compression may introduce domains and
boundaries, but they do not turn algebraic surjectivity into arithmetic
rigidity.

## 3. Exact scope of Möbius rigidity

R170_863(3.2)--(3.3) freezes the second column at

\[
 y^{\log}_k={\log k\over\sqrt k}.                          \tag{3.1}

Within the affine section

\[
 \Sigma_{\log}:=C_{\rm pair}\times\{y^{\log}\},           \tag{3.2}

the intersection with `ker partial` requires `Bx=y^log`. If moreover `x` has
the repeated form `x_{d,m}=a(d)/sqrt{dm}`, Möbius gives

\[
 a(d)=\Lambda(d)\quad(d\le N).                             \tag{3.3}

This is correct and specifically arithmetic. But the section
`Sigma_log` was imposed from outside; the positive form `Delta` does not
distinguish it from

\[
 \Sigma_a=C_{\rm pair}\times\{y^a\}.                      \tag{3.4}

Thus (3.3) merely restates the uniqueness of the solution of
`a*1=log`; it adds no law about the first-contact vector.

## 4. The first jet and the loss of orientation

For the two-scale deformation, `partial e_Lambda(1,1;F)=0` and

\[
 \partial_-\partial e_\Lambda
 =(\mathcal A^{\rm raw}-K_-)_{\le N}F.                    \tag{4.1}

The energy `||partial e||^2` has zero first derivative for a purely
differential reason:

\[
 {d\over ds}\|v(s)\|^2\big|_{v(0)=0}=0.                   \tag{4.2}

This holds for any curve passing through the origin, with no arithmetic
involved. The second jet is the squared norm of (4.1), which loses the
orientation.

The incidence Dirac preserves (4.1), but is indefinite. Hence the
complex reproduces exactly the already audited dichotomy: positivity with
loss of the first jet, or first jet with loss of order.

## 5. The PC gluing does not repair the rigidity

R170_864 correctly glues the `K_-` face and recovers the full PC normal.
That gluing is necessary to avoid repeating R170_855, but it does not change (0.2).
The full PC identity is an exact ledger; its residual Laplacian would be
zero by construction for all data satisfying the corresponding operator
identity.

To turn `e_Lambda` into the bordered null anchor of R170_862, one would
have to prove that the exterior--Tate physical section is exactly the section
`Sigma_log` selected by the full positive form. That statement is
equivalent to

\[
 \mathfrak W_K(f)+\Theta_{\rm ext}(f)=0.                   \tag{5.1}

The incidence complex does not imply it.

## 6. What tool does survive

Even though it does not close, the construction retains two rigorous
uses:

1. it offers route coordinates in which incomplete fibers and `K`
   faces can be audited without losing divisors;
2. it provides the explicit orthogonal projector onto the
   arithmetic graph:

\[
 P_{\ker\partial}=I-\partial^*(BB^*+I)^{-1}\partial.       \tag{6.1}

Applying (6.1) to a candidate port allows one to measure exactly its defect
relative to the divisor gluing. But proving that this exterior defect
vanishes remains the sought-after law.

## 7. Status

```text
identities and jets of R170_863                            CORRECT
partial=[B,-I] is surjective                              PROVED
ker partial is the universal graph y=Bx                   PROVED
positivity of Delta selects Lambda                         FALSE
section y=log plus Möbius selects Lambda                   PROVED
pseudoinverse/algebraic Green                               BUILT / WEIGHT-BLIND
incidence anchor closes the exterior port                   REFUTED
gluing-defect projector (6.1)                               TOOL
exterior law / VIR--LB / D                                 OPEN
```
