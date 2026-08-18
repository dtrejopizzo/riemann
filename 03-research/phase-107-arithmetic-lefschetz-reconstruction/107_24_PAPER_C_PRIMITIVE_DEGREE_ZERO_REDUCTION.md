# 107.24 -- Paper C, Part XII: primitive degree-zero reduction on the candidate polarization

## 1. Purpose

`107_23` isolates the integrability side of Route A, but the next audit
item of `107_12` is A3:

\[
 \deg(\overline M_f)=0.
 \tag{1.1}
\]

The present note reduces that requirement to an explicit intersection
calculation on the candidate surface \(\mathcal X_T^{(1)}\).  Its goal
is to show that the degree-zero condition is not an extra slogan added
after the fact: it is the primitive projection naturally forced by the
two-ruling geometry already built into `107_15` and `107_16`.

The output is a polarization candidate \(H_T^{(1)}\), a generatorwise
degree functional, and a precise reduction theorem:

\[
 \deg_{H_T^{(1)}}\bigl(\widehat{\mathcal M}_{f,T}^{0,{\rm cand}}\bigr)=0
 \quad\Longleftrightarrow\quad
 \text{one explicit scalar relation among visible coefficients.}
 \tag{1.2}
\]

This closes the abstract gap between the normalization protocol of
`107_22` and the degree-zero audit of `107_11`.

## 2. Inputs

This note uses five earlier components.

1. `107_15` gives the candidate surface \(\mathcal X_T^{(1)}\) and the
   realized generators
   \(F_{{\rm v},T}^{(1)},F_{{\rm h},T}^{(1)},\Delta_T^{(1)},
   \Gamma_{p,k,T}^{(1)},Z_{\infty,T}^{(1)}\).
2. `107_16` gives the compactified square and the two ruling boundary
   divisors from which the natural polarization must be built.
3. `107_22` gives the primitive-correction protocol
   \(\widehat{\mathcal M}_{f,T}^{0,{\rm cand}}\).
4. `107_23` reduces the metric side to a finite chartwise audit.
5. `107_11` states the exact degree-zero obligation for the future
   realization map.

## 3. Why the polarization is forced by the square geometry

The candidate surface \(\mathcal X_T^{(1)}\) comes from a regularized
closure inside a compactified square.  Therefore the first degree-one
object cannot be arbitrary.

### Definition 3.1: candidate polarization class

Define the candidate polarization divisor on \(\mathcal X_T^{(1)}\) by

\[
 H_T^{(1)}
 :=
 F_{{\rm v},T}^{(1)}+F_{{\rm h},T}^{(1)}.
 \tag{3.1}
\]

This is the minimal symmetric choice compatible with:

1. the two-ruling geometry of the square;
2. transpose symmetry between the two factors;
3. the need for a visible degree-one carrier not concentrated in only
   one ruling direction.

### Proposition 3.2: \(H_T^{(1)}\) is the first non-arbitrary polarization candidate

Among divisor classes already visible in the current Phase 107
construction, \(H_T^{(1)}\) is the unique minimal class simultaneously
seeing both ruling directions and preserving transpose symmetry.

Proof.  `107_15` gives only the two ruling divisors, the diagonal, the
prime-power graph transforms, and the archimedean component as
canonical generators.  A polarization built from only one ruling would
break the symmetry between the two factors.  A polarization centered on
the diagonal or on individual packet graphs would already depend on the
very correspondence data whose degree is meant to be measured.  The sum
of the two rulings is therefore the first symmetric ambient choice.
\(\square\)

This is enough for a reduction theorem, even though ampleness is not yet
proved.

## 4. Generatorwise degree bookkeeping

At the candidate level, degree with respect to \(H_T^{(1)}\) is a linear
functional on visible divisor classes.

### Definition 4.1: candidate degree functional

For a divisor class \(D\) on \(\mathcal X_T^{(1)}\), define

\[
 \deg_{H_T^{(1)}}(D)
 :=
 D\cdot H_T^{(1)}
 =
 D\cdot F_{{\rm v},T}^{(1)}
 +
 D\cdot F_{{\rm h},T}^{(1)}.
 \tag{4.1}
\]

Whenever we speak below of degree, this is the candidate degree
functional to be used.

### Definition 4.2: visible generator degrees

Introduce the symbols

\[
 d_\Delta(T):=\Delta_T^{(1)}\cdot H_T^{(1)},
 \qquad
 d_\infty(T):=Z_{\infty,T}^{(1)}\cdot H_T^{(1)},
 \tag{4.2}
\]

\[
 d_{p,k}(T):=\Gamma_{p,k,T}^{(1)}\cdot H_T^{(1)},
 \qquad
 d_{\rm v}(T):=F_{{\rm v},T}^{(1)}\cdot H_T^{(1)},
 \qquad
 d_{\rm h}(T):=F_{{\rm h},T}^{(1)}\cdot H_T^{(1)}.
 \tag{4.3}
\]

These are not all numerically computed yet.  They are the exact finite
list of degree data that must be checked to discharge A3 at level \(T\).

## 5. Symmetry constraints on the degree data

Even before the full surface is proved, the square geometry forces some
equalities.

### Proposition 5.1: ruling symmetry

One must have

\[
 d_{\rm v}(T)=d_{\rm h}(T).
 \tag{5.1}
\]

Proof.  \(H_T^{(1)}\) is symmetric under exchange of the two factors,
and the two ruling divisors are interchanged by the same transpose
symmetry.  Therefore their degrees against \(H_T^{(1)}\) coincide.
\(\square\)

### Proposition 5.2: packet degrees depend only on visible order

For a fixed visible order \(n=p^k\), the degree of a packet-refined
graph contribution depends only on \(n\), not on the rooted packet
label.

Proof.  `107_20` and `107_21` show that rooted labels contribute only
norm-one refinements to the local determinant package off the diagonal.
The degree functional is measured against the ambient polarization
\(H_T^{(1)}\), which is built from the two rulings and not from a rooted
character label.  Hence the visible degree bookkeeping is order-based,
not packet-based.  \(\square\)

This is the degree analogue of the packetwise determinant descent.

## 6. Degree of a finite-support realized divisor

Let

\[
 D_{f,T}
 =
 \sum_{(p,k)\in S_T} a_{p,k}(f)\,\Gamma_{p,k,T}^{(1)}
 +a_\Delta(f)\,\Delta_T^{(1)}
 +a_{\rm v}(f)\,F_{{\rm v},T}^{(1)}
 +a_{\rm h}(f)\,F_{{\rm h},T}^{(1)}
 +a_\infty(f)\,Z_{\infty,T}^{(1)}
 \tag{6.1}
\]

as in `107_22`.

### Proposition 6.1: explicit degree formula

The candidate degree of \(D_{f,T}\) is

\[
 \deg_{H_T^{(1)}}(D_{f,T})
 =
 \sum_{(p,k)\in S_T} a_{p,k}(f)\,d_{p,k}(T)
 +a_\Delta(f)\,d_\Delta(T)
 +a_\infty(f)\,d_\infty(T)
 +a_{\rm v}(f)\,d_{\rm v}(T)
 +a_{\rm h}(f)\,d_{\rm h}(T).
 \tag{6.2}
\]

Proof.  This is immediate from bilinearity of the intersection pairing
with respect to the fixed divisor \(H_T^{(1)}\).  \(\square\)

### Corollary 6.2: degree-zero is one scalar visible constraint

The condition

\[
 \deg_{H_T^{(1)}}(D_{f,T})=0
 \tag{6.3}
\]

is equivalent to one explicit scalar linear relation among the visible
coefficients \(a_{p,k}(f),a_\Delta(f),a_\infty(f),a_{\rm v}(f),
a_{\rm h}(f)\).

This is already a substantial reduction of A3.

## 7. Primitive correction revisited

`107_22` defines a primitive correction coefficient by dividing the
degree of the raw class by the self-intersection of the polarization.
We now tie that recipe to the explicit degree formula above.

### Definition 7.1: corrected primitive coefficient

Assume

\[
 h_T:=H_T^{(1)}\cdot H_T^{(1)}\neq 0.
 \tag{7.1}
\]

Then define

\[
 c_T(f)
 :=
 \frac{\deg_{H_T^{(1)}}(D_{f,T})}{h_T}.
 \tag{7.2}
\]

### Definition 7.2: primitive projected divisor

Set

\[
 D_{f,T}^{0,{\rm cand}}
 :=
 D_{f,T}-c_T(f)\,H_T^{(1)}.
 \tag{7.3}
\]

This is the divisor-level shadow of the metrized correction protocol of
`107_22`.

### Theorem 7.3: formal primitive degree-zero identity

Assuming \(h_T\neq0\), one has

\[
 \deg_{H_T^{(1)}}\bigl(D_{f,T}^{0,{\rm cand}}\bigr)=0.
 \tag{7.4}
\]

Proof.  By bilinearity,

\[
 \deg_{H_T^{(1)}}\bigl(D_{f,T}^{0,{\rm cand}}\bigr)
 =
 \deg_{H_T^{(1)}}(D_{f,T})-c_T(f)\,h_T.
 \tag{7.5}
\]

Substituting Definition 7.1 gives zero.  \(\square\)

### Corollary 7.4: `107_22` is the unique linear primitive correction for \(H_T^{(1)}\)

Among linear corrections by multiples of the candidate polarization, the
normalization protocol of `107_22` is the unique one forcing degree zero
with respect to \(H_T^{(1)}\).

Proof.  If
\(D_{f,T}-\lambda(f)H_T^{(1)}\) has degree zero, then
\(\deg_{H_T^{(1)}}(D_{f,T})-\lambda(f)h_T=0\).  Since \(h_T\neq0\),
\(\lambda(f)=c_T(f)\).  \(\square\)

This shows that the primitive projection is not arbitrary bookkeeping.

## 8. Generatorwise reduction of A3

Theorem 7.3 is still formal until the degree data are checked.  But it
already reduces A3 to a finite list of concrete tasks.

### Checklist 8.1: finite degree-zero audit at level \(T\)

To discharge A3 for all tests with support in \(S_T\), it is enough to
verify:

1. \(h_T\neq0\);
2. the generator degrees \(d_{p,k}(T),d_\Delta(T),d_\infty(T),
   d_{\rm v}(T),d_{\rm h}(T)\) exist in the chosen target category;
3. the metrized realization of `107_22` respects the divisor-level
   primitive projection of Definition 7.2.

After that, degree zero for every \(f\) follows by the explicit formula
of Proposition 6.1.

### Proposition 8.2: A3 is reduced to finitely many visible intersection numbers

At fixed support level \(T\), the degree-zero audit of `107_12` reduces
to finitely many generator-vs-polarization intersections.

Proof.  The visible support set \(S_T\) is finite, and the realized
divisor \(D_{f,T}\) is a linear combination of finitely many generators.
Proposition 6.1 expresses the degree as a finite linear combination of
their intersections with \(H_T^{(1)}\).  \(\square\)

This is the degree counterpart of the chartwise reduction achieved in
`107_23`.

## 9. Compatibility with the future Picard/Jacobian realization

### Proposition 9.1: degree-zero on divisors is the exact precursor of degree-zero in \(\widehat{\operatorname{Pic}}^0\)

If the candidate metrized realization of `107_22` respects the divisor
class correction
\(D_{f,T}\mapsto D_{f,T}^{0,{\rm cand}}\), then A3 of `107_11` is
reduced to the divisor-level degree calculation of this note.

Proof.  `107_11` asks for
\(\deg(\overline M_f)=0\) relative to the chosen polarization.  Once the
metrized realization functor preserves tensor products and divisor-level
primitive correction, the target degree-zero statement is the image of
the divisor-level identity (7.4).  \(\square\)

This moves the burden from abstract Picard language back to explicit
visible geometry.

## 10. What is now closed

This note closes the next structural gap after `107_23`.

1. the candidate polarization is now fixed explicitly as the symmetric
   sum of the two rulings;
2. the degree of every visible finite-support divisor is written as one
   explicit linear functional;
3. the primitive correction protocol of `107_22` is proved to be the
   unique linear correction forcing degree zero with respect to that
   polarization;
4. the Route A degree-zero audit A3 is reduced to finitely many visible
   generator-vs-polarization intersection calculations.

## 11. What remains open

This note still does not finish Part III-B or the E1 branch.

1. It does not prove \(h_T\neq0\) on an actually constructed regular
   proper surface.
2. It does not numerically compute the generator degrees
   \(d_{p,k}(T),d_\Delta(T),d_\infty(T),d_{\rm v}(T),d_{\rm h}(T)\).
3. It does not prove the realized metrized Picard class respects the
   divisor-level primitive projection.
4. It does not prove the exact-kernel identity of `107_11`.
5. It does not prove the terminal identity of `107_13`.

## 12. Next technical front

The next proof-bearing move is now to identify the generator-vs-
polarization intersections on \(\mathcal X_T^{(1)}\) from the actual
two-ruling compactified-square geometry, starting with \(h_T\neq0\) and
the ruling/diagonal degrees.  That is the first concrete step from the
formal degree-zero reduction here to a fully verified A3.
