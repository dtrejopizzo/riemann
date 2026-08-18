# D.90 — Central torsor descent and the conormal half-density

## Status

**Typing correction (D.91).**  The conormal family and all covariance,
coisometry, half-density and loop calculations below are valid.  The Weil
Künneth comparison, however, is the linear character
\(\ell(\mathcal A(f\boxtimes\widetilde g))\), not the iterated quadratic
form \(B_{\rm nuc}(\mathcal AF,\mathcal AF)\) used in Section 5 as a landing
audit.  D.91 replaces that last comparison by the correctly polarized
one.

D.89 constructs the conormal Hilbertization for which addition pushforward
is a coisometry.  Its fixed-centre norm is not invariant under the
one-sided integer scaling action.  This note tests two repairs.

The naive repair, splitting \(U_n\) as
\(U_{\sqrt n}\otimes U_{\sqrt n}\), is binary-natural but not
coassociative.  It cannot define a symmetric monoidal coproduct.

There is a coherent repair using data already present in row B.  Replace
one fixed transverse Hilbert space by the family \(\mathcal K_{s,c}\)
whose normal weight is centred at \(u=c\).  The metric torsor translates
\(c\) by \(\log n\).  One-sided \(U_n\) is then a unitary arrow between
the corresponding fibres, addition pushforward is a coisometry in every
fibre, and its minimal Poisson extension is covariant.  Composition and
the loops \(mn=nm\) are strict because centre translations add.

The central character \(n^{-1/2}\) is realized by the positive conormal
half-density.  Its square root is canonical as a positive density and has
no loop sign.  A genuine complex half-form would introduce a metaplectic
\(\mathbb Z/2\)-choice, but no such choice is supplied by A--B--C and it is
not needed for the metric character.

This repair closes naturality of the trace Hilbertization.  It does not
close row D.  On the image of the minimal extension, the transverse defect
is zero and every primitive row-C test occurs.  The preparation Gram is
still exactly \(-4B_{\rm nuc}\), so \(J\)-contractivity there is precisely
the original inequality.

No RH or sign of \(B_{\rm nuc}\) is used.  The paper is not modified.

## 1. Why the half-scaling coproduct is not monoidal

In logarithmic notation let \(U_a\) denote translation by \(a\).  The
binary split suggested by the two rulings is
\[
 \Delta_{1/2}(U_a)=U_{a/2}\otimes U_{a/2}.               \tag{1.1}
\]
It makes addition pushforward natural:
\[
 \mathcal A(U_{a/2}\otimes U_{a/2})=U_a\mathcal A.       \tag{1.2}
\]
But
\[
\begin{aligned}
 (\Delta_{1/2}\otimes I)\Delta_{1/2}(U_a)
 &=U_{a/4}\otimes U_{a/4}\otimes U_{a/2},\\
 (I\otimes\Delta_{1/2})\Delta_{1/2}(U_a)
 &=U_{a/2}\otimes U_{a/4}\otimes U_{a/4}.                \tag{1.3}
\end{aligned}
\]
They are unequal for \(a\ne0\).

More generally a linear binary split
\[
 \Delta_c(a)=(ca,(1-c)a)                                 \tag{1.4}
\]
is coassociative only for \(c=0\) or \(c=1\).  Comparing the first and
third coordinates of the two triple splittings gives
\[
 c^2=c,\qquad (1-c)^2=1-c.                              \tag{1.5}
\]
The symmetric value \(c=1/2\) is excluded.

Thus \(U_{\sqrt n}\) should not be adjoined as a binary coproduct.  Arity
dependent equal splittings \(a/r\) also fail substitution coherence and
do not define a monoidal functor.

## 2. The central family of conormal Hilbert spaces

Retain \(t=x+y\), \(u=x-y\), and \(C_s\) from D.89.  For every
\(c\in\mathbb R\), define
\[
 \|F\|_{\mathcal K_{s,c}}^2
 ={C_s\over2}\int_{\mathbb R^2}
 (1+(x-y-c)^2)^s|F(x,y)|^2dxdy.                         \tag{2.1}
\]
The same sharp trace proof, translated in \(u\), gives a coisometry
\[
 \mathcal A_c=\mathcal A:
 \mathcal K_{s,c}\longrightarrow L^2(\mathbb R).         \tag{2.2}
\]
Its adjoint/minimal extension is
\[
 \boxed{
 (\mathcal A_c^\dagger a)
 \left({t+u\over2},{t-u\over2}\right)
 ={2\over C_s}{a(t)\over(1+(u-c)^2)^s},}                 \tag{2.3}
\]
and
\[
 \mathcal A_c\mathcal A_c^\dagger=I.                    \tag{2.4}
\]

Let \(S_a^{(1)}=S_a\otimes I\).  A direct change of variables proves
\[
 S_a^{(1)}:\mathcal K_{s,c}\xrightarrow{\sim}
 \mathcal K_{s,c+a}                                      \tag{2.5}
\]
unitarily, and the diagrams
\[
\begin{CD}
 \mathcal K_{s,c} @>{S_a^{(1)}}>> \mathcal K_{s,c+a}\\
 @V{\mathcal A_c}VV @VV{\mathcal A_{c+a}}V\\
 L^2(\mathbb R) @>{S_a}>> L^2(\mathbb R)
\end{CD}                                                   \tag{2.6}
\]
and
\[
 S_a^{(1)}\mathcal A_c^\dagger
 =\mathcal A_{c+a}^\dagger S_a                           \tag{2.7}
\]
commute.

Because
\[
 S_b^{(1)}S_a^{(1)}=S_{a+b}^{(1)},                       \tag{2.8}
\]
the family (2.1) is a strict action groupoid over the affine centre torsor
\(\mathbb R\).  For \(a=\log n\), this is exactly the additive invariant
carried by the metric torsor \(\mathcal T_n\):
\[
 \nu_\infty(\mathcal T_{mn})
 =\nu_\infty(\mathcal T_m)+\nu_\infty(\mathcal T_n).     \tag{2.9}
\]
No square-root correspondence is introduced.

## 3. Conormal half-density and the central weight

The change of variables (1.1) has
\[
 dx\,dy={1\over2}dt\,du.                                 \tag{3.1}
\]
The conormal line is oriented by \(du\).  Its positive half-density
\[
 |du|^{1/2}                                               \tag{3.2}
\]
is canonical: positive real densities have a unique positive square root.
On returning from the logarithmic coordinate to the multiplicative
coordinate, central normalization acts on half-densities by
\[
 w_{1/2}(n)
 =\exp\left(-{1\over2}\nu_\infty(\mathcal T_n)\right)
 =n^{-1/2}.                                               \tag{3.3}
\]
This is exactly the metric character already constructed in row B.

The coherence is strict:
\[
 w_{1/2}(mn)=w_{1/2}(m)w_{1/2}(n),                       \tag{3.4}
\]
and for the commutative loop \(mn=nm\),
\[
 S_{\log m}^{(1)}S_{\log n}^{(1)}
 =S_{\log n}^{(1)}S_{\log m}^{(1)},\qquad
 w_{1/2}(m)w_{1/2}(n)=w_{1/2}(n)w_{1/2}(m).              \tag{3.5}
\]
Hence its holonomy is \(+1\).

A complex half-form, rather than the positive density (3.2), would require
a lift of the conormal structure group to the metaplectic double cover.
Changing the lift changes a loop by a sign.  The spherical symmetry and
the positive metric torsor do not choose one of these two lifts.  Moreover
assigning the ruling swap a phase whose square is \(-1\) would not preserve
the symmetric braiding without an additional parity object.  Such a sign
cannot be used as an existing source of row-D positivity.

## 4. Extension over periodic Yoneda and Künneth

The family (2.1) acts only on the flat Hilbert coefficient constructed in
D.88.  For an ordered extremal pair \(e_\alpha\boxtimes e_\beta\), set
\[
 \mathfrak K_{s,c}(\alpha,\beta)
 =\mathbb C(e_\alpha\boxtimes e_\beta)
 \widehat\otimes\mathcal K_{s,c}.                        \tag{4.1}
\]
Cartesian extremal bases give orthogonal sums, principal translations act
on the first factor by the identity, and \(\mathcal T_n\) translates the
centre as in (2.5).  Therefore (4.1) is functorial for the linearized
periodic Yoneda category and its integer scalar action.

This is the coherent version of D.89(3.3).  Equal half-translations are
unnecessary: the relative centre records on which ruling the integer
scalar was applied.  Applying it to the second ruling translates \(c\) in
the opposite direction.  Exchanging rulings sends
\[
 (u,c)\longmapsto(-u,-c),                                \tag{4.2}
\]
an isometry of the family.  Thus the symmetric Künneth constraint is
preserved at the family level.

## 5. Arithmetic Gram and the missing \(J\)-contraction

For \(F\in\mathcal K_{s,c}\), put \(f=\mathcal A_cF\).  After imposing the
two Tate moments on \(f\), the D.86 preparation gives
\[
 \boxed{
 \langle\mathcal Qf,J\mathcal Qg\rangle
 =-4B_{\rm nuc}(f,g).}                                   \tag{5.1}
\]
The right side is the full stabilized expression
\[
\begin{aligned}
 B_{\rm nuc}(f,g)
 ={}&\sum_p(\log p)\sum_{k\ne0}p^{-|k|/2}
       \langle f,S_{k\log p}g\rangle\\
 &+m_0\langle f,g\rangle
 -\langle\partial_\infty f,\partial_\infty g\rangle,     \tag{5.2}
\end{aligned}
\]
so every \(p^k\) and Gamma is unchanged by the centre descent or the
half-density.

The coisometry (2.2) is a positive Hilbert statement:
\[
 \|\mathcal A_cF\|_2\le\|F\|_{\mathcal K_{s,c}}.          \tag{5.3}
\]
The desired arithmetic statement is the different inequality
\[
 \|C^{1/2}z(f)\|^2\le\|r_0(f)\|^2.                       \tag{5.4}
\]
No functorial implication goes from (5.3) to (5.4).

Indeed, for every \(f\in L^2(\mathbb R)\),
\[
 F=\mathcal A_c^\dagger f
 \quad\Longrightarrow\quad
 \mathcal A_cF=f,\qquad
 \|F\|_{\mathcal K_{s,c}}=\|f\|_2,                       \tag{5.5}
\]
and the transverse trace defect is zero.  In particular, every smooth
compact primitive \(f\) occurs in the minimal-extension image.  Restricting
(5.4) to (5.5) is exactly row D on the whole primitive source.

Thus defining a quotient norm on the output by
\[
 \|f\|_{\rm quot}
 =\inf_{\mathcal A_cF=f}\|F\|_{\mathcal K_{s,c}}
 =\|f\|_2                                                  \tag{5.6}
\]
does not hide or prove the sign: it recovers only the ordinary Hilbert
norm, not the \(J\)-contractive preparation norm.

## 6. Conclusion

The continuous half-scaling idea has a coherent realization, but not as a
coproduct.  The metric torsor translates a family of conormal Hilbert
spaces, and the positive half-density produces the existing
\(n^{-1/2}\) character with trivial loop sign.  Addition pushforward and
its minimal extension are dagger-covariant in this family.

This completes naturality of the transverse landing without enlarging the
arithmetic correspondence semigroup.  It supplies no new \(J\)-positive
channel: on the coisometric minimal-extension image the construction is
identical to the original primitive row-C source, and (5.4) remains the
row-D inequality.
