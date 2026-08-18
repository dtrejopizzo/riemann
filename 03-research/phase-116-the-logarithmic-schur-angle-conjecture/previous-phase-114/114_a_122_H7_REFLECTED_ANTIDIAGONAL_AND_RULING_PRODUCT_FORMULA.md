# 114.a.122 — H7: the reflected anti-diagonal needs a ruling product formula

```
+------------------------------------------------------------------------+
| MAP         i:Y^reg -> Y is induced chartwise by A -> Reg_Z(A).        |
| WARNING     Picard injectivity on literal Y does not imply it after     |
|             restriction to the reflected closed pro-subscheme.          |
| EXACT       Need injectivity of i^* on the external anti-sector, or a    |
|             two-coordinate product formula on Y^reg.                    |
| PAYOFF      Either route proves delta_pr injective and closes both       |
|             descent gates a116/a121.                                    |
| LIMIT       Neither reflected Picard faithfulness nor the product formula|
|             is proved here.                                             |
+------------------------------------------------------------------------+
```

## 1. Literal and reflected external classes

Let

\[
 Y=X\times_SX,qquad i:Y^{\rm reg}\longrightarrow Y                 \tag{1.1}
\]

be the literal Haran square and the regular reflection of `a109`--`a110`.
Chartwise, (1.1) is contravariant to the quotient

\[
 A\longrightarrow\operatorname{Reg}_{\mathbb Z}(A).                  \tag{1.2}
\]

Thus `i` behaves as a closed restriction, not as a retraction.  The two
projections and the diagonal factor through `Y^reg`, but no morphism
`Y->Y^reg` splitting (1.1) has been constructed.

For the prime curve classes `L_p`, define the literal and reflected maps

\[
 \delta_{\rm lit}(a)=\bigotimes_p
 (p_1^*L_p\otimes p_2^*L_p^{-1})^{a_p},
 \qquad
 \delta_{\rm reg}=i^*\delta_{\rm lit}.                                \tag{1.3}
\]

At the unit-torsor level, (1.3) is unconditional.  At the completed level,
the right side is the regular lattice realization of `a110`--`a112`.

## 2. Why the old U3/LD route is not sufficient by itself

The criterion `a16` concerns the Cech nerve `X^[n]` of `X->S`.  Its
hypotheses H7-U3 and H7-LD would prove that `delta_lit` is injective.  They do
not imply injectivity of the composite `i^* delta_lit`: pullback of line
bundles along a closed immersion is not generally faithful.

This is a logical issue independent of whether H7-U3/LD are eventually
proved.  If `f:G->H` is injective and `r:H->K` has a kernel meeting `f(G)`,
then `rf` is not injective.  The diagonal gives no rescue because

\[
 \Delta^*\delta_{\rm reg}(a)=1                                       \tag{2.1}
\]

for every `a`; it is designed to annihilate the anti-sector.

### Definition 2.1 (reflected Picard faithfulness)

The missing extra statement is

> **H7-REFL-PIC.** The pullback
> `i^*:Pic_tor(Y)->Pic_tor(Y^reg)` is injective on
> `delta_lit(direct-sum_p Z L_p)`.

Then H7-U3 + H7-LD + H7-REFL-PIC imply injectivity of `delta_reg`.  A direct
proof of `delta_reg` remains preferable and bypasses all three hypotheses.

Concretely, on a reflected affine cover, H7-REFL-PIC says that the pulled
transition cocycle of (1.3) is a coboundary of reflected local units only when
all `a_p` vanish.  This is a finite-stage unit equation, not a formal
consequence of regular reflection.

## 3. The two-coordinate product-formula route

There is a more geometric sufficient statement.  On the prime presentation
lattice set

\[
 d_i\left(\sum_{p,j}m_{p,j}D_{p,j}\right)
 =\sum_pm_{p,i}\log p.                                                 \tag{3.1}
\]

> **H7-RULING-PF.** If a prime-generated completed Cartier divisor on
> `Y^reg` is principal, then both numbers in (3.1) vanish separately.

This is the product formula expected on a proper two-ruling geometry.  It is
strictly stronger than diagonal degree: diagonal pullback sees only
`d_1+d_2`, while H7-RULING-PF keeps the two coordinates.

### Theorem 3.1

H7-RULING-PF implies that `delta_reg` is injective.

### Proof

If `delta_reg(a)=1`, the corresponding principal presentation has degrees

\[
 (d_1,d_2)=(A,-A),\qquad A=\sum_pa_p\log p.                            \tag{3.2}
\]

H7-RULING-PF gives `A=0`.  Unique factorization then gives every `a_p=0`.
QED.

On the anti-sector, this is exact: the only possible kernel already has the
form (3.2) by `a112`.  Therefore it suffices to construct either ruling
degree on principal divisors; the other is its negative after diagonal
pullback.

## 4. Consequence for the live route

The correct implication chain is now

\[
 \begin{matrix}
 \text{H7-U3 + H7-LD + H7-REFL-PIC}\\
 \text{or H7-RULING-PF}\\
 \text{or direct }\delta_{\rm reg}\text{ faithfulness}
 \end{matrix}
 \Longrightarrow
 \begin{matrix}
 B_{\rm RR}\text{ descends (`a116`)}\\
 h_{\rm ray}\text{ descends (`a121`).}
 \end{matrix}                                                        \tag{4.1}
\]

This corrects every use of bare H7-U3/LD as a sufficient condition after
regular reflection.  It does not decide H7-REFL-PIC or H7-RULING-PF, does not
construct the Green excess, and does not close row A or RH.

## 5. Verification scope

`114_a_122_h7_reflected_antidiagonal_verify.py` checks the composite-kernel
logic, the exact degree pair `(A,-A)`, unique-factorization detection and the
scope markers.  The scheme-theoretic direction of (1.1) is the quotient/spec
duality of `a109`--`a110`.

**Later boundary reduction (`a128`--`a129`).**  The finite-chart candidate
`p_2/p_1` does not disprove H7-RULING-PF: its correction is not a unit on
Haran's real ball.  It cancels all finite valuations and leaves precisely a
mixed archimedean boundary class.  Thus the live form of the product formula
is H7-ARCH-BDRY, independence of those residual classes.
