# 114.a.93 — H7: the typed parity incidence has an exact `Z/2` Smith obstruction

```
+-------------------------------------------------------------------------+
| MATRIX      Six part-vertices by four even-parity triples.               |
| SMITH       diag(1,1,1,2); cokernel Z^2 direct-sum Z/2.                  |
| WITNESS     z=(1,1,1,1,1,1) is not an integral incidence boundary.       |
| DOUBLE      2z is the sum of all four parity columns.                     |
| MOD 2       Sum the three coordinate-1 vertices: even columns vanish,     |
|             while z maps to 1.                                           |
| FRAGILITY   Adding any one odd-parity triple changes all Smith factors to 1.|
| OPEN        Is the Haran macro closure parity-preserving or does it add an |
|             odd column/equivalent move?                                  |
+-------------------------------------------------------------------------+
```

## 1. The exact incidence matrix

Order the six vertices by

\[
 (1,0),(1,1),(2,0),(2,1),(3,0),(3,1)
\]

and the four columns by `000,011,101,110`.  The incidence matrix of the
typed diagram from `a92` is

\[
 A=
 \begin{pmatrix}
 1&1&0&0\\
 0&0&1&1\\
 1&0&1&0\\
 0&1&0&1\\
 1&0&0&1\\
 0&1&1&0
 \end{pmatrix}.                                                       \tag{1.1}
\]

Every column has one vertex in each part; every row has degree two.

### Theorem 1.1 (Smith obstruction)

The nonzero Smith factors of `A` are

\[
 1,1,1,2.                                                            \tag{1.2}
\]

Consequently

\[
 \operatorname{coker}A\cong\mathbb Z^2\oplus\mathbb Z/2.            \tag{1.3}
\]

### Proof

Unit entries give the first Smith factor one; elementary elimination gives
three unit pivots.  The rank is four, and a full-rank minor has determinant
`+/-2`, while every full-rank minor is even.  Hence the fourth determinantal
divisor is two and (1.2) follows.  The executable verifier computes the
complete exact Smith form and all maximal minors.  QED.

## 2. A concrete order-two class

Let

\[
 z=(1,1,1,1,1,1)^t.                                                  \tag{2.1}
\]

Summing all four columns of (1.1) gives

\[
 A(1,1,1,1)^t=2z.                                                    \tag{2.2}
\]

On the other hand `z` is not in the integral image.  Indeed define

\[
 \omega(x)=x_{(1,1)}+x_{(2,1)}+x_{(3,1)}\pmod2.                      \tag{2.3}
\]

Every even-parity column contains zero or two coordinate-`1` vertices, so
`omega A=0`.  But `omega(z)=3=1 mod 2`.  Thus the class of `z` is nonzero
and has exact order two in the cokernel.

Equivalently, the rational equation `Ax=z` has the unique solution on the
column span

\[
 x=(1/2,1/2,1/2,1/2)^t,                                              \tag{2.4}
\]

and no integral solution.  This is the lattice shadow of the missing
perfect matching in `a91`.

## 3. One odd edge kills the obstruction

There are four odd-parity triples.  Adjoin the incidence column of any one
of them to `A`.  The resulting matrix still has rank four, but its nonzero
Smith factors are

\[
 1,1,1,1.                                                            \tag{3.1}
\]

The mod-two explanation is immediate: an odd triple has one or three
coordinate-`1` vertices, so `omega` evaluates to one on its column.  The
functional (2.3) no longer descends to the cokernel.

Thus the exact closure question has a binary answer:

- if all macro moves incident to this skeleton preserve even parity, the
  incidence lattice has genuine 2-torsion;
- if the closure supplies one odd column or an integral combination with
  odd `omega`, this particular obstruction disappears.

## 4. Relation to H7-PRIME-REG

Theorem 1.1 is **not yet a counterexample in the Haran operation set**.
Matrix `A` records the ancestry incidence of the typed finite-set diagram,
not the complete relation matrix of its equivalence-ideal component.
Additional sandwich contexts may add columns, and an additive cokernel class
must still be realized by actual endpoints of a macro path.

The exact next gates are:

1. **H7-PARITY-ENDPOINTS:** turn (2.2) into typed operations `F,G` and a
   macro path `2F~2G`;
2. **H7-PARITY-PRESERVE:** prove every additional incident macro move has
   `omega=0`, or find one with `omega=1` and kill the candidate;
3. **H7-PARITY-SEPARATE:** if parity is preserved, prove `F not~G` using
   the descended `omega` invariant on the full component.

Only the conjunction of these steps would refute 2-PRIME-REG.  Conversely,
an odd macro move disposes of this minimal candidate but does not by itself
prove global prime regularity.

H7-PARITY-ENDPOINTS/PRESERVE/SEPARATE, H7-PRIME-REG and row A remain open.

## 5. Verification scope

`114_a_93_h7_parity_smith_verify.py` constructs (1.1), computes its exact
Smith normal form and all rank-four minors, verifies (2.2)--(2.4), and checks
all four odd-column extensions.  It enforces that no Haran torsion claim is
made.
