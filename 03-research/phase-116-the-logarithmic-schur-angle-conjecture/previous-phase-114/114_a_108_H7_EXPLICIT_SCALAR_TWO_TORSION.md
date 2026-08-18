# 114.a.108 — H7: the signed arithmetic plane has explicit scalar 2-torsion

```
+------------------------------------------------------------------------+
| ELEMENT     kappa=(1,-1)_1 o (1,1)_2^t in P_(1,1).                    |
| TORSION     Swapping the two middle wires gives kappa=-kappa, hence     |
|             2 kappa=0.                                                  |
| NONZERO     The universal infinitesimal map sends kappa to the nonzero  |
|             class tau in (C Omega)_(1,1)[2].                            |
| VERDICT     H7-PRIME-REG and H7-AUG-FLAT are FALSE at p=2.              |
| SCOPE       The literal square survives; its completed regular-lattice  |
|             route does not include the pulled-back denominator 2.       |
+------------------------------------------------------------------------+
```

## 1. The scalar class

Let

\[
 P=F(\mathbb Z)_1\otimes_{F\{\pm1\}}F(\mathbb Z)_2             \tag{1.1}
\]

be the full commutative involutive `F`-ring plane.  In its two rulings set

\[
 s_1=(1,-1)_1\in P_{[1],[2]},\qquad
 c_2=(1,1)_2^t\in P_{[2],[1]},                                \tag{1.2}
\]

and define

\[
 \kappa=s_1\circ c_2\in P_{[1],[1]}.                          \tag{1.3}
\]

The fold to `F(Z)` sends `kappa` to `1-1=0`; thus it lies in the scalar
augmentation kernel from `a102`.

## 2. The exact two-torsion identity

Let `sigma` be the transposition of the two middle wires.  It belongs to the
common structural base and satisfies `sigma^2=id`.  Moreover

\[
 s_1\circ\sigma=(-1,1)_1=-s_1,
 \qquad \sigma\circ c_2=c_2.                                  \tag{2.1}
\]

Consequently

\[
 \kappa=s_1\circ\sigma\circ\sigma\circ c_2
        =(-s_1)\circ c_2=-\kappa.                              \tag{2.2}
\]

The first ruling makes every operation set an abelian group, with the common
scalar `-1` acting as additive inverse.  Hence

\[
 2\kappa=\kappa+_{(1)}\kappa=0.                               \tag{2.3}
\]

This calculation uses only a structural permutation and signed
distributivity; it already holds in the full signed pushout before any
localization.

## 3. Nonvanishing by the universal infinitesimal target

Let

\[
 \Omega_C=C\Omega(F(\mathbb Z)/F\{\pm1\}),\qquad
 H=F(\mathbb Z)\Pi\Omega_C.                                   \tag{3.1}
\]

Because `F(Z)` is totally commutative and `Omega_C` is a commutative module,
`H` is a commutative involutive `F`-ring.  The unit section and universal
relative derivation give compatible ruling maps

\[
 x_1\longmapsto(x,0),\qquad x_2\longmapsto(x,dx),              \tag{3.2}
\]

and therefore a map `J_12:P->H`.

The base component of `J_12(kappa)` is zero.  Its module component is

\[
 (1,-1)\circ d(1,1)^t=[1,-1|1]=\tau.                          \tag{3.3}
\]

By Theorem 3.1 of `a107`,

\[
 (\Omega_C)_{1,1}simeq
 \left(\bigoplus_p\mathbb Z d_p\right)^{\oplus2}
 \oplus\mathbb Z/2\,\tau,                                    \tag{3.4}
\]

and `tau` is the nonzero generator of the last summand.  Thus

\[
 J_{12}(\kappa)=(0,\tau)\ne0,                                 \tag{3.5}
\]

so `kappa` itself is nonzero in `P`.

### Theorem 3.1 (explicit torsion)

The scalar arithmetic plane contains a nonzero element `kappa` with
`2 kappa=0`.

## 4. Consequences for the live A route

### Corollary 4.1

Multiplication by the first-ruling prime `2` is not injective even on
`P_(1,1)`.  Therefore:

\[
 \boxed{\text{H7-AUG-FLAT is false and H7-PRIME-REG is false.}} \tag{4.1}
\]

Indeed `kappa` is nonzero, lies in `ker(nabla)`, and is killed by `2`.
Equivalently, `(E_cancel:2)` strictly contains `E_cancel`.

### Corollary 4.2

The projection of the arithmetic curve's denominator `2` to the square is
not a universally regular denominator in Haran's sense.  Hence the
Section-11 completed fraction-lattice pullback required in `a63` cannot be
constructed by H7-PB-REG/H7-PRIME-REG; that conditional route is now closed
negatively, not merely left open.

This does **not** destroy Haran's literal fiber-product square, its prime
rulings, contact sheaves, unit torsors or the abstract `Pic_tor` bigrade.
It says that the desired completed Cartier/lattice theory cannot treat the
pulled-back prime `2` as regular on the unmodified signed structure sheaf.
Any surviving G-7 construction must therefore do one of the following:

1. use a divisor/cycle theory not requiring universal regularity;
2. modify or derive the structure sheaf while proving that the `Lambda(2)`
   contact is retained; or
3. quotient the torsion only with a proof that all required incidences,
   degrees, sections and gauge descend.

No such repair is supplied here.  Row A and a4-strong remain open, and this
result does not assert RH.

Primary source for the infinitesimal construction and differential
presentation: Haran, [*New foundations for geometry*](https://arxiv.org/abs/1508.04636),
Sections 7.5--7.8.

## 5. Verification scope

`114_a_108_h7_explicit_scalar_two_torsion_verify.py` checks the typed
wire-swap calculation, fold zero, the exact `Z/2` cocycle detecting `tau`,
and the logical consequences for injectivity and flatness.  The verifier is
symbolic; no finite search or numerical approximation supports the theorem.
