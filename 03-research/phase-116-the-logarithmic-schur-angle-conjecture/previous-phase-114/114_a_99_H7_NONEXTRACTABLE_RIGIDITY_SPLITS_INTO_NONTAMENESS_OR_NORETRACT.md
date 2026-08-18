# 114.a.99 — H7: nonextractable rigidity means nontameness or a nonretractable context

```
+-------------------------------------------------------------------------+
| SIGNATURE   Sigma(a)=(b o a o d) over all scalar sandwiches b,d.         |
| TAMENESS    A is tame iff Sigma is injective in every arity.              |
| CASE 1      Distinct bits with equal ambient signatures witness           |
|             failure of H7-TAME-PLANE.                                    |
| CASE 2      A separator exists ambiently but cannot pass through the       |
|             parity embedding: failure of H7-CONTEXT-RETRACT.              |
| THEOREM     TAME + CONTEXT-RETRACT forbids every rigid parity even move.   |
| RESULT      H7-NONEXTRACTABLE-RIGID is replaced by two exact gates.        |
+-------------------------------------------------------------------------+
```

## 1. The complete scalar-sandwich signature

For `a in A_(Y,X)` define

\[
 \Sigma(a)=\bigl(b\circ a\circ d\bigr)_
 {b\in A_{1,Y},\ d\in A_{X,1}}.                                    \tag{1.1}
\]

Haran's definition says exactly that `A` is tame when `Sigma` is injective
in every arity.  Thus for two intrinsically distinct decorations `D_0,D_1`
there are only two possibilities:

1. `Sigma(D_0)=Sigma(D_1)`.  This pair is an explicit witness that `A` is
   not tame.
2. Some scalar sandwich separates them.

The first possibility is not merely a difficult parity decoration: it
settles H7-TAME-PLANE negatively.

## 2. Retraction through an outer context

Let `C_i(a)` denote an operation obtained by inserting `a` into slot `i` of
a fixed typed multiplication/contraction context.  Say this occurrence is
**sandwich-retractable** if, for every scalar sandwich `b a d`, there are
outer scalar probes `B,D` such that

\[
 B\circ C_i(a)\circ D=b\circ a\circ d                               \tag{2.1}
\]

for all admissible `a`; the other slots are sent to their fixed neutral
values.  Direct sums and independent block contexts have this property by
zero/unit insertion (`a72`--`a73`).

> **H7-CONTEXT-RETRACT.** Every bit occurrence in a proposed nonlaminar
> parity context is sandwich-retractable, perhaps after a common refinement
> of cuts.

This is not assumed for arbitrary contraction/reuse contexts.

## 3. Tame-retract obstruction theorem

### Theorem 3.1

Let `A` be tame and let `D_0!=D_1`.  If an occurrence `C_i` is
sandwich-retractable, then

\[
 C_i(D_0)\ne C_i(D_1).                                                \tag{3.1}
\]

### Proof

Tameness gives `b,d` with `b D_0 d != b D_1 d`.  By retractability choose
`B,D` satisfying (2.1).  Equality of `C_i(D_0),C_i(D_1)` would remain equal
after the outer sandwich and contradict the chosen scalar inequality.  QED.

### Corollary 3.2

H7-TAME-PLANE plus H7-CONTEXT-RETRACT forbids the three rigid even moves
needed by the parity construction: each move changes a bit in a retractable
slot, which Theorem 3.1 detects.

## 4. Correct residual dichotomy

The gate called H7-NONEXTRACTABLE-RIGID in `a98` now splits into:

- **H7-NONTAME-WITNESS:** construct distinct `D_0,D_1` with identical full
  scalar-sandwich signatures; this refutes H7-TAME-PLANE and invalidates the
  scalar-promotion route of `a84`;
- **H7-NORETRACT-ENTANGLE:** construct an outer parity context which blocks
  every ambient separator, and prove it lacks a sandwich retraction even
  after all allowed cut refinements.

If neither exists, the parity route is eliminated.  If the first exists,
it does not by itself give prime torsion.  If the second exists, one must
still realize the fold-zero Smith endpoints and control macro closure.

This dichotomy is exhaustive by the definition of `Sigma`; it does not
assume RH or prime regularity.  H7-TAME-PLANE, H7-CONTEXT-RETRACT and the two
negative-witness gates remain open.  H7-PRIME-REG and row A remain open.

## 5. Verification scope

`114_a_99_h7_tame_retract_dichotomy_verify.py` exhausts finite operation
systems represented by scalar sandwich signatures, checks the tame/retract
implication and explicit failures when either hypothesis is removed, and
enforces all open-gate markers.  The general result is Theorem 3.1.

Primary source: Haran, [*New foundations for geometry*](https://arxiv.org/abs/1508.04636),
Definition 1.4.3 and Appendix A.2.2.

**Later resolution (`a104`).**  The H7-NONTAME-WITNESS branch occurs: the
mixed binary centre and Cartesian grid are distinct while all their scalar
sandwiches agree.  This resolves the tameness side of the dichotomy but,
as the theorem already warns, does not itself produce prime torsion or
decide H7-PRIME-REG.
