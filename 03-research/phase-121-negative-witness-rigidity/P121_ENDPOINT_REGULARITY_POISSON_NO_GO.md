# P121 -- endpoint regularity does not by itself produce the Poisson lift

## Status

This note audits a possible continuation of the sub-half-Sobolev radical
bootstrap.  The proposed continuation was

```text
first-contact radical
 -> bounded/log-Hölder (or even BV) regularity on the finite window
 -> Dirichlet--Jordan Poisson summation
 -> equality of the two Meyer half-lifts
 -> compact Poisson-range rigidity
 -> no first contact.
```

The middle implication is false at the required global type.  Finite-window
regularity controls the physical source on a compact multiplicative annulus;
the Meyer half-lift contains a Möbius tail accumulating at the multiplicative
origin.  Controlling that tail is the already isolated oriented divisibility
problem, not a consequence of endpoint regularity.

No claim about the global square is made here.

## 1. The tempting local argument

Let `g` be supported in a compact multiplicative annulus

\[
                 0<a\le x\le b<\infty .             \tag{1.1}
\]

For a physical first-contact vector, phase 121 proves sub-half-Sobolev
regularity of its zero extension.  It is tempting to seek stronger bounded,
log-Hölder, or bounded-variation regularity from the logarithmic-Laplacian
equation and then invoke a low-regularity Poisson theorem.

Such regularity would be useful for the *finite-window* source.  It does not
control the global inverse of the Zeta sum.

## 2. Exact support calculation for the Möbius half-lift

The first Meyer half-lift is forced algebraically by Möbius inversion:

\[
 f_>(x)=Z^{-1}g(x)=\sum_{n\ge1}\mu(n)g(nx).          \tag{2.1}
\]

For each fixed `x>0` the sum is finite, but (1.1) gives the exact active
range

\[
             {a\over x}\le n\le {b\over x}.         \tag{2.2}
\]

Consequently `f_>` vanishes for `x>b`, but in general it does **not** vanish
on any interval `(0,epsilon)`.  As `x` tends to zero, the number of terms in
(2.1) tends to infinity.  Thus compact support of `g` in logarithmic
coordinates does not give compact support, BV control, or a Dini bound for
the global half-lift at the multiplicative origin.

This is not an endpoint technicality: it is the arithmetic tail.

## 3. Mellin identification of the missing estimate

Where the initial Dirichlet series converges, Mellin transformation of
(2.1) gives

\[
                  \widehat f_>(s)={G(s)\over\zeta(s)}. \tag{3.1}
\]

Therefore any global regularity assertion strong enough to place `f_>` in
Meyer's common Poisson source must in particular make the apparent poles of
(3.1) removable.  At a critical zero `rho` this requires

\[
                         G(\rho)=0.                 \tag{3.2}
\]

For the first-contact source, (3.2) is exactly the oriented critical
divisibility/F2 condition of
`P121_CRITICAL_NEGATIVE_HALF_RESIDUE_GATE.md` and
`P121_GLOBAL_SQUARE_CLOSURE_MAP.md`.

Hence a proof of global BV, Dini, Schwartz, or Meyer-source regularity for
`f_>` cannot be inferred from finite-window regularity of `g`: at the
critical divisor it already contains the terminal theorem.

## 4. Why ordinary Poisson summation does not repair the type mismatch

Dirichlet--Jordan Poisson summation can be applied to a function whose
global additive behavior satisfies its hypotheses.  In the present
problem the regular object under consideration is `g` on the annulus,
whereas Poisson summation must be applied to the inverse source `f_>` in
(2.1).  Regularity of `g` on `[a,b]` gives no uniform variation estimate for
the growing Möbius sums (2.2).

Equivalently, the second half-lift

\[
 f_<(g)=\mathcal F Z^{-1}\mathscr Jg                 \tag{4.1}
\]

cannot be identified with `f_>(g)` by applying a local Poisson formula to
`g`.  Their equality is precisely the range criterion v94 (304)--(306).

The stronger statement remains valid and useful: if the zero extension of
the *physical radical itself* is `C_c^\infty`, translation-jet exclusion
already gives zero.  What fails here is the proposed shortcut

\[
  \text{finite-window BV of }g
  \quad\Longrightarrow\quad
  f_>(g)=f_<(g).                                     \tag{4.2}
\]

## 5. Consequence for the live attack

The half-Sobolev boundary threshold is not the terminal obstruction.
Crossing it all the way to a smooth compact translation vector would close
first contact, but merely obtaining bounded, log-Hölder, BV, or Dini
regularity on the physical annulus does not control the Möbius tail.

The remaining admissible target stays unchanged:

\[
 P_T\mathscr A_TF=0
 \quad\Longrightarrow\quad
 K_F(\rho-\tfrac12)=0
 \text{ on a superlinear critical family},          \tag{5.1}
\]

or equivalently a source-defined equality-state law which controls (2.1)
at `x=0` without defining that control by division through `zeta`.

### Audit verdict

```text
finite-window sub-half Sobolev regularity          PROVED
finite-window bounded/BV regularity                NOT NEEDED FOR THIS AUDIT
local regularity implies global Meyer half-lift    FALSE
Möbius tail at x=0 equals oriented divisibility    PROVED BY (2.1)--(3.2)
global square                                      OPEN
```
