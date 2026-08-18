# 114.a.94 — H7: fold-zero parity differences still have exact `Z/2`

```
+-------------------------------------------------------------------------+
| CORRECTION  Relation columns must preserve the fold; raw incidence       |
|             columns from a93 do not.                                    |
| COLUMNS     011-000, 101-000, 110-000 all have zero total in each part.  |
| SMITH       Their 6x3 matrix has factors 1,1,2.                          |
| WITNESS     w=(-1,1;-1,1;-1,1), with B(1,1,1)=2w but w not in im B.      |
| MOD 2       omega=sum of the three coordinate-1 entries detects w.       |
| FRAGILITY   One odd-parity difference changes the factors to 1,1,1.      |
| OPEN        Realize the three even replacements as actual macro paths.    |
+-------------------------------------------------------------------------+
```

## 1. From ancestry columns to relation differences

The incidence matrix `A` of `a93` has a `Z/2` Smith factor, but each of its
columns has total mass three.  A column of a relation matrix must instead be
the difference between two presentations with the same diagonal fold.

Fix the base triple `e_0=000` and write `a_e` for the six-component
incidence column of a triple `e`.  Use the three even-parity differences

\[
 b_1=a_{011}-a_{000},\quad
 b_2=a_{101}-a_{000},\quad
 b_3=a_{110}-a_{000}.                                                \tag{1.1}
\]

Every `b_i` has total zero in each of the three parts separately.  Thus it
passes the fold-preservation test that the raw columns did not.

In the row order of `a93`, the resulting matrix is

\[
 B=\begin{pmatrix}
 0&-1&-1\\
 0& 1& 1\\
-1& 0&-1\\
 1& 0& 1\\
-1&-1& 0\\
 1& 1& 0
\end{pmatrix}.                                                       \tag{1.2}
\]

## 2. Exact fold-zero obstruction

### Theorem 2.1

The Smith factors of `B` are

\[
 1,1,2.                                                              \tag{2.1}
\]

Hence its image is not saturated at the prime two.

### Proof

The matrix has rank three.  Unit entries and a unit `2x2` minor give the
first two Smith factors.  Every `3x3` minor is even and one has determinant
`+/-2`, so the third factor is two.  QED.

Define

\[
 w=(-1,1,-1,1,-1,1)^t.                                              \tag{2.2}
\]

Then

\[
 B(1,1,1)^t=2w.                                                     \tag{2.3}
\]

Let `omega` sum the entries at `(1,1),(2,1),(3,1)` modulo two.  Each
column of `B` changes two of the three coordinates and hence has
`omega=0`, while `omega(w)=3=1`.  Therefore `w` is not in the integral
image.  The equation `Bx=w` has the unique rational solution
`x=(1/2,1/2,1/2)`.

This is an exact fold-compatible `2w in im(B), w notin im(B)` pattern.

## 3. Odd closure still kills it

Adjoin any one difference `a_e-a_000` with `e` of odd parity.  The extended
matrix has Smith factors

\[
 1,1,1.                                                              \tag{3.1}
\]

Indeed `omega(a_e-a_000)=1`.  Thus the obstruction survives precisely while
the available replacement moves remain parity-even.

## 4. Remaining macro realization

Theorem 2.1 fixes the main typing defect of the raw `a93` matrix, but still
does not prove a Haran collision.  Its columns are **candidate** differences
of ancestry presentations.  One must show that the full sandwich graph
contains paths

\[
 P_{000}\sim P_{011},\qquad
 P_{000}\sim P_{101},\qquad
 P_{000}\sim P_{110}                                                \tag{4.1}
\]

whose induced fold-zero difference vectors are exactly (1.1), while no
incident macro path produces an odd-parity difference.

If (4.1) is realized, equation (2.3) supplies the linear shadow of a
2-divisible endpoint collision.  It remains additionally necessary to lift
`w` to actual endpoints and prove that the mod-two `omega` invariant
descends through every macro context in their component.

The exact gates are now:

1. **H7-EVEN-MOVES:** realize the three paths (4.1);
2. **H7-ODD-MOVE:** decide whether contextual closure supplies any odd
   replacement;
3. **H7-PARITY-ENDPOINTS:** lift (2.3) from the relation lattice to an
   actual pair `2F~2G`;
4. **H7-PARITY-SEPARATE:** prove `F not~G`, if no odd move exists.

No torsion class in the Haran quotient is asserted here.  These gates,
H7-PRIME-REG and row A remain open.

## 5. Verification scope

`114_a_94_h7_fold_zero_parity_verify.py` checks fold preservation, exact
Smith factors and maximal minors, the explicit witness (2.2)--(2.3), and
all four odd extensions.  It enforces the macro-realization disclaimer.
