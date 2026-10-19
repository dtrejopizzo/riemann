# R170_868 — Universal factor-through theorem for the divisor defect

## 0. Result

R170_867 concluded that the missing port had to contain a
linear component that did not factor through

\[
 \mathscr D_N(a,c)={(a*\mathbf1)-c\log\over\sqrt\cdot}.    \tag{0.1}
\]

Within the same coefficient space, no such component exists.

**Theorem.** Let `Y` be any vector space and let

\[
 \ell:\mathbb R^N\oplus\mathbb R\longrightarrow Y         \tag{0.2}
\]

be linear. If

\[
 \ell(\Lambda|_{[1,N]},1)=0,                              \tag{0.3}

then there exists a unique linear map

\[
 Q:\mathbb R^N\longrightarrow Y                           \tag{0.4}

such that

\[
 \boxed{\ell=Q\mathscr D_N.}                              \tag{0.5}

Hence every linear extension preserving the arithmetic null line is
automatically a graph extension of the R170_867 class. It cannot
produce the first-order exterior block.

The new piece must abandon at least one of these three conditions:

1. using only the coefficient space `(a,c)`;
2. depending linearly on those coefficients;
3. annihilating the line `(Lambda,1)` by itself.

The option compatible with R170_862 is to enlarge the null vector by a
physical boundary coordinate `beta_T(f)` and require a joint
cancellation, not the separate vanishing of each new row.

## 1. Surjectivity and quotient

R170_866 proves that

\[
 \ker\mathscr D_N=K_N:=\mathbb R(\Lambda,1),               \tag{1.1}
\]

and that `mathscr D_N` has rank `N`; hence it is surjective. The first
isomorphism theorem gives

\[
 (\mathbb R^N\oplus\mathbb R)/K_N
 \simeq\mathbb R^N                                        \tag{1.2}

via the map induced by `mathscr D_N`.

Every linear map annihilating `K_N` descends to the quotient (1.2), and
therefore factors through `mathscr D_N`. This is the whole idea of the
theorem.

## 2. Explicit proof

For `v in R^N`, choose `x=(a,c)` with `mathscr D_Nx=v` and define

\[
 Qv:=\ell x.                                                \tag{2.1}

If `x'` is another preimage, `x-x' in ker mathscr D_N=K_N`; by (0.3),
`ell(x-x')=0`. Hence (2.1) is well defined. It is linear and satisfies

\[
 Q\mathscr D_Nx=\ell x.                                    \tag{2.2}

Surjectivity of `mathscr D_N` gives uniqueness of `Q`. QED.

The proof holds unchanged for topological output spaces if `ell`
and a right section of `mathscr D_N` are continuous; in finite dimension
this is automatic.

## 3. Consequence for positive extensions

Let a finite linear extension be

\[
 \mathscr E_N(a,c)
 =\bigl(\mathscr D_N(a,c),\ell_1(a,c),\ldots,\ell_r(a,c)\bigr).
                                                                    \tag{3.1}
\]

If the line `K_N` remains in `ker mathscr E_N`, each `ell_j` annihilates
`K_N`. By the theorem there exist `Q_j` with `ell_j=Q_j mathscr D_N`. Then

\[
 \mathscr E_N=\begin{pmatrix}I\\Q_1\\\vdots\\Q_r\end{pmatrix}
               \mathscr D_N,                              \tag{3.2}
\]

and

\[
 \mathscr E_N^*\mathscr E_N
 =\mathscr D_N^*
  \left(I+\sum_jQ_j^*Q_j\right)\mathscr D_N.              \tag{3.3}

Thus every finite linear positive extension with the same null line only
changes the normal metric. This result includes tails, reflections,
PC copies, and any number of auxiliary variables eliminated
linearly, as long as the total map remains linear in `(a,c)` and
each new row vanishes on the line.

## 4. Operator version

Tensor with a physical space `mathcal H`. Let

\[
 \boldsymbol\ell:
 (\mathbb R^N\oplus\mathbb R)\otimes\mathcal H
 \longrightarrow\mathcal Y                                \tag{4.1}
\]

be linear and suppose

\[
 \boldsymbol\ell((\Lambda,1)\otimes F)=0
 \quad\text{for all }F\in\mathcal H.                    \tag{4.2}

Since

\[
 \ker(\mathscr D_N\otimes I)
 =K_N\otimes\mathcal H,                                    \tag{4.3}

the same quotient argument yields

\[
 \boxed{\boldsymbol\ell
 =\boldsymbol Q(\mathscr D_N\otimes I).}                   \tag{4.4}

The statement remains valid on the algebraic core. Extending it to
completions requires controlling closures and domains, but no domain
issue can create a finite linear row that violates the factorization on
the core.

## 5. Boundary-augmented repair

To escape the theorem, enlarge the domain by a boundary space `B_T`:

\[
 \widehat E_N=(\mathbb R^N\oplus\mathbb R)\otimes\mathcal H
               \oplus B_T.                                \tag{5.1}

Look for a null vector of the form

\[
 \widehat e_T(f)=((\Lambda,1)\otimes f,\beta_T(f)),        \tag{5.2}

where `beta_T(f)` contains the exterior--Tate port. A new row

\[
 \widehat\ell(x,b)=\ell_{\rm ar}(x)+\ell_{\rm bd}(b)       \tag{5.3}

can annihilate (5.2) via the cancellation

\[
 \ell_{\rm ar}((\Lambda,1)\otimes f)
 =-\ell_{\rm bd}(\beta_T(f)),                              \tag{5.4}

without `ell_ar` separately annihilating the arithmetic line. Then the
factor-through theorem does not apply to `ell_ar`.

To close R170_862 one additionally needs:

\[
 (e_T,\partial_-\widehat{\mathbb L}_T\widehat e_T(f))
 =\mathfrak W_K(f)+\Theta_{\rm ext}(f),                    \tag{5.5}

with a positive form whose base fiber annihilates both the boundary anchor and
the extended arithmetic line.

Equations (5.2)--(5.5) specify the unique linear way out of the no-go:
the arithmetic and the port must vanish **jointly**, not as two
separate null rows.

## 6. Relation to minimality

The coordinate `beta_T(f)` must depend on the first-contact vector; otherwise
the construction would again become a coefficient identity
valid on positive windows. The weak equation supplies the available
linear data:

\[
 PAf=\rho_fb,\qquad Q_eAf=\ell_f.                           \tag{6.1}

Hence the minimal candidate for `beta_T(f)` must be built from
`(rho_f,ell_f)` and the causal dual `(h,q)`, preserving the gauge-invariant
combination of R170_859. That dependence makes the extension pass
filter F1: no analogous null coordinate exists for an eigenvector with a
positive eigenvalue.

It has not yet been proved that this data satisfies (5.4) in a
positive form; that is precisely the remaining exterior law.

## 7. Status

```text
D_N surjective with ker=R(Lambda,1)                       INHERITED FROM R170_866
every linear row annihilating the line factors through D_N  PROVED
every linear positive extension is a metric change         PROVED
tensor version on the core                                 PROVED
non-factored component in the same space                   IMPOSSIBLE
boundary-augmented enlargement with joint cancellation      NECESSARY
construction of beta_T(f) and a positive form                OPEN
exterior law / VIR--LB / D                                  OPEN
```
