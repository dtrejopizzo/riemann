# Phase 121 -- active-contact pole-complexity no-go

## Status

The hoped-for density closure was:

\[
 \text{finite active primes + quarter-Gamma ladder}
 \Longrightarrow O_T(R)\text{ critical poles}.              \tag{0.1}
\]

This note proves that (0.1) cannot follow from the active current.  At a
fixed support radius, the active Euler current is an entire Dirichlet
polynomial.  Every nontrivial critical pole sits in the analytically
continued inactive tail, with unchanged residue.  Identifying that tail
with the finite-channel/Gamma boundary is exactly equality-state annular
transport.  Thus pole complexity remains a valid terminal strategy, but
not a consequence of finite contact complexity.

## 1. Exact active/tail split

Fix `T` and put `X=e^(2T)`.  Define

\[
 D_X(s)=\sum_{n<X}{\Lambda(n)\over n^s},             \tag{1.1}
\]

an entire exponential polynomial, and on any zero-free open set define

\[
 R_X(s)=-{\zeta'\over\zeta}(s)-D_X(s).               \tag{1.2}
\]

Let `K` be any entire compact-source transform.  Then

\[
 -{\zeta'\over\zeta}(s)K(s)=D_X(s)K(s)+R_X(s)K(s).  \tag{1.3}
\]

### Proposition 1.1 -- all critical residues are tail residues

If `rho` is a simple nontrivial zero of `zeta`, then

\[
 \operatorname {Res}_{s=\rho}D_X(s)K(s)=0,
 \qquad
 \operatorname {Res}_{s=\rho}R_X(s)K(s)=-K(\rho).  \tag{1.4}
\]

#### Proof

`D_XK` is entire.  The logarithmic derivative has principal part
`-1/(s-rho)` at a simple zero, and subtracting an entire function does not
alter it.  QED.

The same statement, with multiplicity, holds at every zero.  Consequently
the active contact operator contains **zero** of the pole-support
information required by density F2.  All of that information is in `R_X`.

## 2. Why the Gamma ladder does not change the conclusion

The quarter-Gamma logarithmic derivative has poles on one arithmetic
half-line, with counting function `O(R)`.  Adding it to `D_XK` therefore
produces a meromorphic object of pole complexity `O_T(R)`.  This fact is
unconditional but irrelevant to the critical residues in (1.4): the
Gamma poles are disjoint from the nontrivial zeta divisor and cannot
cancel them without an identity involving `R_XK`.

Thus an equality

\[
 R_XK_F=\text{active-prime/Gamma/Tate current}       \tag{2.1}
\]

on a global meromorphic domain would indeed imply that the active critical
support of `K_F` is `O_T(R)`, and the already proved density-F2 theorem
would force `F=0`.  But (2.1) is not the finite-window zero-mode equation.
The latter identifies only the restriction of the symmetric current to
the physical window.

## 3. Exact location of the missing implication

In the causal physical picture, `R_XK_F` is the transform of the incoming
history generated outside the window by inactive divisor depths.  V94
(451)--(455) shows that localization of the global commutator equals the
active current plus precisely this incoming history.  V94 (441)/(446)
states that its annular amplitude vanishes.

Therefore

\[
 \boxed{
 \text{global }O_T(R)\text{ pole complexity of the first-contact current}
 \quad\Longleftrightarrow\quad
 \text{critical sparsity of the inactive tail},}             \tag{3.1}
\]

and the implication from the local equation to the right side is the
remaining annular source theorem.  Replacing `R_X` by the absolutely
convergent Euler tail in `Re(s)>1` does not solve this: continuation to the
critical line is exactly where the poles of (1.4) appear.

## 4. Consequence for candidate design

Counting the active prime channels, the Gamma states or the rank of their
local Hankel observables can never by itself prove density F2.  A surviving
candidate must act on the analytically continued inactive tail and prove
that a first-contact state makes its critical residue support subdense.
Equivalently, it must provide a source-defined continuation law for the
incoming history.  No finite-channel dimension count supplies that law.

This is a no-go for (0.1), not for the density endgame itself.  The exact
terminal statement remains

\[
 P_T\mathscr A_TF=0
 \Longrightarrow
 \#\{\rho=\tfrac12+i\gamma:\ |\gamma|\le R,
                         K_F(i\gamma)\ne0\}=o(R\log R).       \tag{4.1}
\]

No change to paper 42 follows.

