# 114.a.89 — H7: the full fixed two-level relation lattice is total mass

> **Correction made during the same construction.**  The first draft kept
> only `2x2` checkerboards and incorrectly called row/column margins
> invariant.  The contextual-zero `K2,2` of `a81` disproves that: its row
> margins are nonzero.  The theorem below includes the cancellation contexts
> from both rulings and replaces the retracted margin-lattice claim.

```
+-------------------------------------------------------------------------+
| GRID        A fixed two-level bilateral core is an integer table B.      |
| RULING 1    Contextual cancellation generates U_0 tensor Z^c, where U_0 |
|             is the zero-sum row lattice.                                |
| RULING 2    Transpose cancellation generates Z^r tensor V_0.            |
| QUOTIENT    Z^(rxc)/(U_0 tensor Z^c + Z^r tensor V_0) is Z.              |
| INVARIANT   The only invariant in this fixed-grid sector is total signed |
|             strand mass.                                                |
| RESULT      The relation lattice is saturated at every prime.           |
| OPEN        Nested contexts that change/overlap several incidence grids. |
+-------------------------------------------------------------------------+
```

## 1. Fixed-grid signed tables

Fix `r` left parent blocks and `c` right parent blocks in one displayed
two-level bilateral incidence grid.  After collecting parallel signed
strands, a presentation is an integer table

\[
 B=(b_{ij})\in L\otimes R,
 \qquad L=\mathbb Z^r,\quad R=\mathbb Z^c.                            \tag{1.1}
\]

Let `epsilon_L:L->Z` and `epsilon_R:R->Z` be coordinate summation and put

\[
 U_0=\ker\epsilon_L,\qquad V_0=\ker\epsilon_R.                        \tag{1.2}
\]

The total signed strand mass is

\[
 \tau=\epsilon_L\otimes\epsilon_R:L\otimes R\longrightarrow\mathbb Z.
                                                                         \tag{1.3}
\]

## 2. What the two cancellation generators actually impose

Relabel the first-ruling cancellation pair onto two left blocks `i,i'`.
Putting it in an arbitrary signed right context `v in R` gives

\[
 (e_i-e_{i'})\otimes v\sim0.                                         \tag{2.1}
\]

These relations generate `U_0 tensor R`.  Applying the transposed
second-ruling cancellation in an arbitrary signed left context gives

\[
 w\otimes(f_j-f_{j'})\sim0,                                         \tag{2.2}
\]

which generates `L tensor V_0`.  Both are instances of Haran's general
sandwich formula (A.2.9); the Cartesian index/sign rule is (10.18)--(10.19).

Thus the full relation subgroup inside a **fixed two-level table** is

\[
 J=U_0\otimes R+L\otimes V_0.                                       \tag{2.3}
\]

Every generator in (2.3) has total mass zero.  Conversely, every
cancellation-context image that stays in this fixed grid has a zero-sum
factor in the ruling where the generator occurs, hence lies in (2.3).
This last fixed-grid qualification is essential: a general macro context
may change cuts and leave the single-table model.

The `2x2` checkerboard

\[
 (e_i-e_{i'})\otimes(f_j-f_{j'})                                    \tag{2.4}
\]

is only the intersection of the two families, not the whole relation
lattice.  In particular the `K2,2` contextual zero of `a81` is
`(e_1-e_2) tensor (f_1+f_2)` and belongs to the first summand of (2.3)
despite having nonzero row margins.  This is the precise error corrected
from the first draft.

## 3. Exact quotient and saturation

### Theorem 3.1 (total-mass normal form)

The sequence

\[
 0\longrightarrow J\longrightarrow L\otimes R
   \overset{\tau}{\longrightarrow}\mathbb Z\longrightarrow0         \tag{3.1}
\]

is exact.  Equivalently, two signed fixed-grid tables are related by the
two contextual cancellation families if and only if they have the same
total signed mass.

### Proof

Equations (2.1)--(2.2) give `J subset ker(tau)`.  Quotienting first by
`U_0 tensor R` replaces `L` by `L/U_0 ~= Z`; quotienting then by the image
of `L tensor V_0` replaces `R` by `R/V_0 ~= Z`.  Hence

\[
 (L\otimes R)/J
 \cong(L/U_0)\otimes(R/V_0)
 \cong\mathbb Z.                                                     \tag{3.2}
\]

Under this isomorphism the quotient map is exactly `tau`.  QED.

An elementary normal-form proof chooses base blocks `r,c`: relations (2.1)
move every row to row `r`, and (2.2) move every remaining column to column
`c`; the result is `tau(B) E_(r,c)`.

### Corollary 3.2 (all-prime saturation)

`J` is saturated for every prime.  If `pB in J`, then
`0=tau(pB)=p tau(B)` in `Z`, so `tau(B)=0` and Theorem 3.1 gives `B in J`.

## 4. The minimal tests from a81 and a88

The signed `K2,2` table of `a81` is

\[
 K=\begin{pmatrix}1&1\\-1&-1\end{pmatrix}
  =(e_1-e_2)\otimes(f_1+f_2)\in J,                                  \tag{4.1}
\]

so its contextual vanishing is recovered exactly.

The two unsigned three-strand tables of `a88` are

\[
 B_0=\begin{pmatrix}1&0\\0&2\end{pmatrix},\qquad
 B_1=\begin{pmatrix}0&1\\1&1\end{pmatrix}.                          \tag{4.2}
\]

Both have total mass three, so Theorem 3.1 relates them.  Their difference
is the checkerboard (2.4), but checkerboards alone would not have presented
the full fixed-grid quotient.

## 5. Exact remaining gate

Theorem 3.1 closes prime saturation for every single fixed two-level
incidence grid, of arbitrary size and with arbitrary signed multiplicities.
It does **not** identify the quotient of nested colored trees: macro contexts
can change the cut, create several overlapping tables, and then return to
the original external arity.  The remaining gate is

> **H7-NESTED-CONTEXT-SAT.** Prove that the compatible total-mass normal
> forms on all fixed grids glue across cut changes without introducing a
> nonsaturated relation, or construct a genuine nested counterexample.

This is narrower than H7-MARGINAL-COMPLETE as stated in `a88`: ordinary
row/column margins are not invariants.  The correct local invariant is total
mass, and the unresolved information is carried by how several grid charts
overlap.  H7-NESTED-CONTEXT-SAT, H7-PRIME-REG and row A remain open.

## 6. Verification scope

`114_a_89_h7_two_level_marginal_verify.py` verifies the primary context
formulas; computes both ruling relation families; proves by exact normal
reduction that their quotient is total mass for all tables in broad finite
boxes; checks saturation; and reproduces the `a81` and `a88` examples.  It
also contains a regression guard forbidding the retracted row/column-margin
claim.

Primary sources: Haran, [*Geometry over F1*](https://arxiv.org/abs/1709.05831),
equations (10.16)--(10.21); Haran, [*New foundations for geometry*](https://arxiv.org/abs/1508.04636),
Appendix A.2.9.
