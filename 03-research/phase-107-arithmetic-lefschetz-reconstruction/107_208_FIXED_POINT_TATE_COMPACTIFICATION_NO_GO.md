# 107.208 -- The fixed germ cannot be added to the Tate quotient as an ordinary compactification

## 1. The tempting construction

`107_207` realizes the local Euler determinant at the trivial fixed
point \(0\in\mathbb C\).  Connes--Consani's proper complex orbit is

\[
 E_p=\mathbb C^\times/p^{\mathbb Z}.
 \tag{1.1}
\]

The most direct globalization attempt is to retain the fixed point and
form either

\[
 \mathbb C/p^{\mathbb Z}
 \quad\text{or}\quad
 \mathbb P^1(\mathbb C)/p^{\mathbb Z}.
 \tag{1.2}
\]

This attempt fails topologically before any sheaf or intersection is
chosen.

## 2. Orbit-closure obstruction

### Theorem 2.1

For every prime \(p\), the coarse quotient
\(\mathbb C/p^{\mathbb Z}\) is not \(T_1\), hence is not Hausdorff and
cannot be a compact Riemann surface or a proper complex analytic space.
The same holds for \(\mathbb P^1(\mathbb C)/p^{\mathbb Z}\).

### Proof

The orbit of \(1\) is

\[
 \mathcal O(1)=\{p^n:n\in\mathbb Z\}.
\]

It is not closed in \(\mathbb C\), because \(p^{-n}\to0\), while
\(0\notin\mathcal O(1)\).  If the coarse quotient were \(T_1\), the
singleton containing the image of \(\mathcal O(1)\) would be closed.
Its inverse image under the quotient map would then be the nonclosed
set \(\mathcal O(1)\), a contradiction.

On \(\mathbb P^1\), the same orbit accumulates at both \(0\) and
\(\infty\).  The identical inverse-image argument applies. \(\square\)

The group action also fails properness: both fixed points have infinite
stabilizer \(p^{\mathbb Z}\).  Passing from a coarse quotient to the
quotient stack records that stabilizer but does not produce an ordinary
proper curve.

## 3. No boundary can be appended to the existing Tate curve

### Theorem 3.1

There is no Hausdorff compactification \(j:E_p\hookrightarrow X\) in
which \(j(E_p)\) is a proper dense open subset.

### Proof

The Tate curve \(E_p\) is already compact.  Its continuous image in a
Hausdorff space is compact and therefore closed.  If that image is also
dense, it equals \(X\).  Thus the boundary \(X\setminus E_p\) is empty.
\(\square\)

Consequently, the fixed point supporting the ideal sequence of
`107_207` cannot be added as an ordinary boundary point of the Tate
curve.

## 4. Exact consequence

The local geometric determinant remains valid, but its globalization
cannot be

\[
 \text{retain }0\quad+\quad\text{take the ordinary }p^{\mathbb Z}
 \text{ quotient}.
\]

Any surviving construction must change category.  The available
possibilities are now sharply limited to a quotient stack/groupoid with
infinite isotropy, a relative degeneration whose central fiber contains
the fixed section, or a boundary/nearby-cycles formalism that pushes the
cotangent class before taking the Tate quotient.  Each option still
needs its own proper pushforward and Hodge theorem.

This no-go does not exclude those alternatives and does not reject the
absolute Connes--Consani curve itself.  It closes only the ordinary
Hausdorff compactification route left open in `107_207`.

## 5. Falsifier

`107_208_fixed_point_tate_compactification_no_go.py` uses five actual
primes and interval bounds for the orbit sequences.  It can return
`NO` if the orbit of \(1\) fails to enter every prescribed neighborhood
of a fixed point, or if the purported boundary is introduced without
destroying closedness of the compact Tate source.

