# 114.a.95 — H7: commutativity kills the undecorated parity `Z/2`

```
+-------------------------------------------------------------------------+
| SYMMETRY    Each bare two-element cut has an internal S_2 swap.           |
| SOURCE      Isomorphic tree data are equivalent by (10.14).               |
| PARITY      Flipping one coordinate sends H_even to H_odd.                |
| RELATION    The fold-zero swap column is e_(p,1)-e_(p,0).                 |
| SMITH       Adding any one swap to the a94 matrix changes 1,1,2 to 1,1,1. |
| INVARIANT   omega evaluates to 1 on the swap and does not descend.         |
| VERDICT     The undecorated parity candidate is not a Haran obstruction.   |
| OPEN        Rigidify all three bits compatibly with fold and macro moves.   |
+-------------------------------------------------------------------------+
```

## 1. The missing isomorphism relations

The finite-set diagram of `a92` labels each two-element part by `0,1`, but
the bare Haran tree data do not remember those names.  Equation (10.14)
identifies isomorphic data, and a binary addition vertex permits its two
children to be interchanged.

Thus the undecorated skeleton carries the coordinate-flip action

\[
 (\mathbb Z/2)^3\curvearrowright\mathbb F_2^3.                       \tag{1.1}
\]

Flipping an odd number of coordinates interchanges even and odd parity.
In particular the distinction used by `omega` in `a93`--`a94` is not
intrinsic to the unlabeled presentation.

## 2. Exact Smith correction

Let `B` be the fold-zero `6x3` even-difference matrix of `a94`.  For part
`p in {1,2,3}`, the linear shadow of its internal swap is

\[
 s_p=e_{(p,1)}-e_{(p,0)}.                                            \tag{2.1}
\]

It preserves the part total and therefore the diagonal fold.

### Theorem 2.1

For every `p`, the matrix `[B|s_p]` has nonzero Smith factors

\[
 1,1,1.                                                              \tag{2.2}
\]

Hence any one undecorated coordinate swap kills the factor two of `a94`.

### Proof

The first two unit factors of `B` remain.  A `3x3` minor involving `s_p`
has determinant `+/-1`, so the third determinantal divisor becomes one.
Exact computation for all three parts is included in the verifier.  QED.

The mod-two invariant gives the same conclusion:

\[
 \omega(s_p)=1.                                                      \tag{2.3}
\]

Therefore `omega` cannot descend through the commutativity/isomorphism
relation of the bare skeleton.

## 3. Consequence for the parity route

The undecorated typed diagram of `a92`, even with the fold-zero Smith
calculation of `a94`, does **not** yield H7-PARITY-SEPARATE.  Its proposed
separating functional is destroyed by a relation already present before
arbitrary sandwich closure is considered.

This disposes of the minimal bare parity candidate, analogously to how
`a81` disposed of the bare `K2,2` torsion candidate, although for a different
reason: here an internal commutativity automorphism supplies the odd move.

The only surviving parity variant must satisfy

> **H7-PARITY-RIGID.** Decorate the `0` and `1` blocks in each of the three
> parts by intrinsically nonisomorphic typed subtrees, so no allowed
> commutativity/cut move exchanges them; simultaneously preserve a common
> diagonal fold and realize the three even replacement paths of `a94`.

Rigidifying by arbitrary external labels is not allowed: the decoration
must be part of the Haran operation and survive the quotient.  Distinct
subtree arities or colors are possible candidates, but they can change the
fold or reintroduce block extraction covered by `a72`--`a75`.

H7-PARITY-RIGID is open.  The undecorated parity route is closed negatively;
H7-PRIME-REG and row A remain open.

## 4. Verification scope

`114_a_95_h7_parity_swap_verify.py` checks the source commutativity marker,
the action of all coordinate flips on parity, exact Smith forms after each
swap column, and failure of `omega` to descend.  It enforces the negative
scope and the open rigidification gate.
