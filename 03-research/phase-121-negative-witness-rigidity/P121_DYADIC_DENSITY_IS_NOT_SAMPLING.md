# P121 -- dyadic two-thirds density is uniqueness, not sampling

## Status

The unconditional two-thirds theorem gives a superlinear family of simple
critical zeros in every dyadic ordinate window.  This is enough for the
Cartwright *uniqueness* descent already used in phase 121 once all the
corresponding values of `K_F` are known to vanish.  It does not give a
coercive sampling inequality capable of proving that vanishing from an
energy balance.

The distinction is not technical.  This note proves that even the correct
dyadic asymptotic

\[
 \#(\Gamma\cap(R,2R])\asymp R\log R                         \tag{1.1}
\]

is compatible with failure of every lower Paley--Wiener sampling bound.
Consequently the two-thirds theorem, Riemann--von Mangoldt counting and a
global horizontal-displacement moment cannot by themselves close F2.

## 1. What the two-thirds theorem actually supplies

Theorem A of the 2026 rank--trace paper states, in the notation used there,

\[
 N_{0}^{s}(R,2R)\ge (2/3-o(1))N(R,2R).              \tag{1.2}
\]

Together with Riemann--von Mangoldt this gives (1.1) for the set of simple
critical ordinates.  It is a statement in windows whose length is
comparable with their height.  It gives neither a bounded-gap theorem nor a
lower frame bound on a fixed Paley--Wiener space.

The phase-121 Cartwright argument uses only the following consequence:
if an entire function of fixed exponential type vanishes on all of
`Gamma`, then it is zero.  F2 needs a different implication: a signed
first-contact balance would have to force those values to vanish.  Replacing
that implication by a sampling inequality requires a positive constant
`A_T` such that

\[
 A_T\|K\|_{L^2(\mathbb R)}^2
 \le \sum_{\gamma\in\Gamma}|K(\gamma)|^2            \tag{1.3}
\]

for every `K in PW_T` (with the usual harmless local weights if required).
Dyadic counting does not imply (1.3).

## 2. A countermodel with the exact counting scale

### Theorem 2.1 -- superlinear dyadic density without stable sampling

For every `T>0` there is a discrete set `Gamma subset R` such that

\[
 \#(\Gamma\cap(R,2R])\asymp R\log R                 \tag{2.1}
\]

as `R to infinity`, but `Gamma` is not a sampling set for `PW_T`.  In fact
there are unit vectors `K_j in PW_T` with

\[
 \sum_{\gamma\in\Gamma}|K_j(\gamma)|^2\longrightarrow0. \tag{2.2}
\]

#### Proof

Choose disjoint gaps

\[
 I_j=(x_j-L_j,x_j+L_j),\qquad x_j=2^{2j},\quad
 L_j=x_j^{1/2}.                                     \tag{2.3}
\]

Outside the gaps, partition the line into unit cells.  In the cell near an
integer `m`, place `M_m=ceil(log(3+|m|))` distinct points inside an interval
of length `exp(-|m|)` around the cell centre.  Place no points in the gaps,
and reflect the construction about zero.

The unpunctured count in `(R,2R]` is comparable with `R log R`.  Every such
dyadic window loses only `o(R)` unit cells to the gaps: the largest relevant
gap has length `O(sqrt R)`, and the earlier gaps have total length
`O(sqrt R)`.  Thus the deleted count is `O(sqrt R log R)=o(R log R)`.
This proves (2.1), uniformly for all sufficiently large `R`.

Choose a nonzero `K in PW_T` whose inverse Fourier transform is smooth and
compactly supported strictly inside `[-T,T]`, and normalize `||K||_2=1`.
Then for every `N`

\[
 |K(x)|\le C_N(1+|x|)^{-N}.                         \tag{2.4}
\]

Set `K_j(x)=K(x-x_j)`.  Translation preserves `PW_T` and its `L2` norm.
Every point of `Gamma` is at distance at least `L_j` from `x_j`.  Using
(2.4), the polynomial growth of the number of points per unit cell and then
choosing `N>3` gives

\[
 \sum_{\gamma\in\Gamma}|K_j(\gamma)|^2
 \ll_N \sum_{|m-x_j|\ge L_j}
       \log(3+|m|)(1+|m-x_j|)^{-2N}
 \longrightarrow0.                                \tag{2.5}
\]

Thus no positive lower sampling constant exists.  QED.

### Corollary 2.2

Neither a positive dyadic proportion nor the stronger asymptotic scale
`R log R` converts the critical family into a stable observer of `PW_T`.
Any proof of (1.3) needs genuinely local separation/coverage information
not contained in the two-thirds theorem.

## 3. Why horizontal displacement energy does not repair the defect

An estimate for the off-line horizontal energy constrains a second set of
points and their distances from the critical line.  It supplies no lower
frame bound for the critical sample operator.  In the countermodel above
one may attach an empty off-line set, so every horizontal energy bound holds
while (2.2) still fails.  More generally, an upper bound on an off-line
sampling operator cannot create the missing lower bound in (1.3).

At first contact the zero-side identity has the schematic form

\[
 0=\sum_{\gamma\in\Gamma_{\rm crit}}|K_F(\gamma)|^2
       +\mathcal E_{\rm off}(K_F).                  \tag{3.1}
\]

The second term is signed.  Counting the first family and bounding the
size of the second does not force the first sum to vanish unless one can
compare both terms through a stable sampling/interpolation theorem.  Such a
comparison is precisely additional information; it is not a consequence
of (1.2).

## 4. Consequence for F2

The two-thirds result remains useful in exactly one place:

\[
 K_F(i\gamma)=0\ \hbox{for every simple critical }\gamma
 \quad\Longrightarrow\quad K_F\equiv0.             \tag{4.1}
\]

That is the already proved F3 descent.  It cannot supply the preceding F2
arrow

\[
 \text{first contact}\quad\Longrightarrow\quad
 K_F(i\gamma)=0.                                   \tag{4.2}
\]

The rank--trace theorem is therefore not a route from density to the global
square.  Any surviving proof must still produce an oriented equality-state
law before scalar cancellation.  No paper-42 change follows from this
no-go.

