# 115.06 — Axiom 4 closes on the ruling sector, and exposes the missing canonical class

## Verdict

With

\[
 h^1_t:=h^\vee_t\ (\text{dual-lattice theta}),
 \qquad
 h^2_t:=h^0_t(-D,-E),
\]

**all four axioms of `thm:mixedsectionforcing` hold on the ruling sector.**
The Euler characteristic comes out exact:

\[
 h^0_t-h^1_t+h^2_t=(\log2)^2N_t=\tfrac{t^2}{2}B_{\rm int}(D,D)+O(t),
\]

verified to \(1.3\times10^{-26}\) per dimension — machine zero.

But the same computation exposes a real tension: the **Künneth** assignment,
which is the natural one for a product, gives a different \(h^1\) and the
wrong \(\chi\).  Nothing constructed so far decides between them, because
row (a) builds **no canonical class**.

## 1. Why \(h^2=0\), and why axiom 3 was mis-diagnosed

`115_05` withdrew the claim that axiom 1 fails.  The same fact settles
axiom 3, and shows my `115_05` §4 worry was itself confused.

For \(D,E\) of positive degree, \(-D,-E\) have negative degree, so
\(m_t=\lfloor e^{-ta}\rfloor=0\), \(r(0)=0\), the lattice is \(\{0\}\) and

\[
 h^2_t:=h^0_t(-D,-E)=\log1=0 .
\]

Axiom 3 (\(h^2(D)=h^0(-D)\)) therefore holds **by definition, with both sides
vanishing**.  `115_05` §4 argued it was false by comparing \(h^0(-D)\) with
\(h^\vee\) — but \(h^\vee\) is not \(h^2\).  They are different objects:

* \(h^\vee\) is the **dual-lattice** theta; it is what Poisson summation
  produces and what appears in the Riemann–Roch identity;
* \(h^2\) is \(h^0\) of the **anti-effective** class; it vanishes.

Conflating them was the error.  And this is classically right: on a surface
\(H^2(X,L)\) vanishes for \(L\) effective of positive degree.

## 2. The forced value of \(h^1\)

The Riemann–Roch requirement determines \(h^1\) once \(h^2\) is known.  From
\(h^0-h^1+h^2=\tfrac{t^2}{2}q\) and the proved \(h^0-h^\vee=\tfrac{t^2}{2}q\),

\[
 h^1=h^2+h^\vee .
\]

With \(h^2=0\) this gives \(h^1=h^\vee\).  And that is not an ad-hoc fit: in
the arithmetic-curve theory \(h^1\) **is** the dual-lattice theta, since
Serre duality there is Poisson summation.  We are importing curve-type Serre
duality, which is exactly what the two-term identity of `115_04` already was.

Numerically, per dimension: \(h^0=0.4809954460\),
\(h^1=h^\vee=0.0005424321\), \(h^2=0\), \(\chi=0.4804530139=(\log2)^2\). ✓

## 3. The tension: Künneth disagrees

`thm:cotangentKunneth` gives \(V_{m,n}\simeq V_m\otimes V_n\) — the square is
a **product**, so its middle cohomology ought to come from the Künneth cross
terms, not from a curve-type dual:

\[
 H^1=(H^0\otimes H^1)\oplus(H^1\otimes H^0).
\]

For the symmetric factorization \(\sigma_1=\sigma_2=\sigma^{1/2}\) this gives
\(h^{01}=h^{10}=N_t\log\vartheta(1)\), so

| assignment | \(h^1\) per dimension | \(\chi\) per dimension |
|---|---|---|
| curve-type, \(h^1=h^\vee\) | \(0.0005424\) | \(0.4804530=(\log2)^2\) ✓ |
| Künneth, \(h^1=h^{01}+h^{10}\) | \(0.1658030\) | \(0.3151924\) ✗ |

Discrepancy \(2\log\vartheta(1)-\log\vartheta(\sigma^{-1})=0.1652606\ldots\)
per dimension.

## 4. What the discrepancy is

A surface-type \(h^1\) needs a **dualizing class**; a curve-type one needs only
the dual lattice.  Row (a) has the second and not the first.  Searching
`row-a-deligne-nuclear.tex` and `row-a-intrinsic-periodic.tex` turns up no
canonical sheaf, no Serre duality, no \(\omega\): the objects \(\Omega_m\),
\(\Omega_{m,n}\) of `eq:cotangentSpaces` are cotangent spaces of the **code
envelope**, not a dualizing sheaf on \(\mathscr Y_{\mathbb S}\).

This is the same gap that axiom 3 hides.  Axiom 3 as stated in
`thm:mixedsectionforcing` is \(h^2(D)=h^0(-D)\), which presumes a **trivial**
canonical class; the classical statement would be \(h^2(D)=h^0(K-D)\).  So:

> **Axioms 3 and 4 are one missing ingredient, not two: the canonical class of
> the square.**

That is why the ordering matters.  Attempting the mixed extension before
settling it would build on an \(h^1\) chosen because it makes \(\chi\) come
out, not because it is forced.

## 5. Candid scope

On the ruling sector the conclusion of `thm:mixedsectionforcing` is
**elementary**: `eq:rulingquotient` gives \(B_{\rm int}\) signature \((1,1)\),
so \(q(D,D)\le0\) when \(\deg D=0\) is immediate.  §2 therefore proves no new
inequality.  What it establishes is that the theta-on-code-lattices recipe
reproduces a *complete* Riemann–Roch and effectivity package, with the right
constant and no free parameters, on a sector where the answer is
independently known.  That is a validation of the machinery and the
precondition for extending it — not a step toward RH by itself.

## 6. Classification

* \(h^2_t=0\) on the effective cone; axiom 3 holds with both sides vanishing:
  **PROVED**.
* `115_05` §4's claim that axiom 3 is false: **WITHDRAWN** (it compared
  \(h^\vee\) with \(h^0(-D)\); those are different objects).
* \(h^1=h^2+h^\vee\) forced by RR, hence \(h^1=h^\vee\): **PROVED**.
* All four axioms on the ruling sector: **PROVED**, interior reading of strict
  effectivity.
* Künneth disagreement \(0.1652606\ldots\) per dimension: **COMPUTED**.
* The canonical class of \(\mathscr Y_{\mathbb S}\): **DOES NOT EXIST** in
  row (a) as constructed; required to adjudicate §3.
* Mixed classes: **OPEN**.
* Row D: **OPEN**.

## 7. Next

Two items, in order:

1. **The canonical class.**  Either construct a dualizing object in
   \(\operatorname{Perf}_{IDN}\), or prove the curve-type assignment is forced
   (for instance by showing the square's cohomological dimension collapses in
   the relevant range, which \(h^2=0\) makes plausible).
2. **The mixed classes** — extend one lattice-with-metric family from the
   ruling sector to the \(D_f\).
