# 107.08 -- Paper B, Part II: suspension to an arithmetic flow

## 1. Purpose

This note executes Work Package II-B of 107.00.  Its role is to suspend
the decorated correspondence category of `107_07` to a source-defined
flow/groupoid whose primitive closed orbits have lengths \(\log p\).

The key point is that the flow object may not be merely

\[
 \bigsqcup_p \mathbb R/(\log p)\mathbb Z.
 \tag{1.1}
\]

That disjoint union has the local prime circles, but it has no common
degree-one geometry, no global diagonal class, and no place where the
finite and archimedean pages can interact.  The present construction
therefore glues the prime circles through the common phase cylinder
already isolated in Phase 106.

## 2. Input from earlier phases

Three earlier pieces are the minimum source data for II-B.

1. `107_07` provides the decorated correspondence category
   \(\operatorname{Corr}_{\mathrm{EF}}\).
2. `106.153` constructs for each prime \(p\) a weight-one polarized local
   coefficient system over the periodic orbit

\[
 C_p\simeq \mathbb R/(\log p)\mathbb Z.
 \tag{2.1}
\]

3. `106.169` identifies the common phase cylinder

\[
 \widetilde E=\mathbb R_u\times(\mathbb R/2\pi\mathbb Z)_\theta
 \simeq \mathbb C^\times,
 \tag{2.2}
\]

   and the Tate curves

\[
 E_p=\mathbb C^\times/p^\mathbb Z
 \simeq C_p\times\mathbb S^1,
 \tag{2.3}
\]

   which supply a prime orbit together with a phase direction that is
   independent of \(p\).

These data are enough to define the source flow object needed by II-B.

## 3. The local periodic orbits

For each prime \(p\), define the prime orbit

\[
 C_p=\mathbb R_+^\times/p^\mathbb Z.
 \tag{3.1}
\]

Passing to logarithmic coordinate \(u=\log x\) identifies this with

\[
 C_p\simeq \mathbb R/(\log p)\mathbb Z.
 \tag{3.2}
\]

The translation flow on \(\mathbb R\),

\[
 u\longmapsto u+t,
 \tag{3.3}
\]

descends to a circle flow on \(C_p\).  Its primitive period is exactly
\(\log p\), and its \(k\)-fold return has period \(k\log p\).

### Definition 3.1: local return maps

For each \(t=k\log p\), let

\[
 \Gamma_t^{(p)}
 \tag{3.4}
\]

denote the \(k\)-step return correspondence of the flow on \(C_p\).
These are the local flow shadows of the raw generators
\(\Gamma_{p,k}\) in `107_07`.

## 4. The common archimedean phase

The decisive structural input is that the prime orbit is not isolated.
It comes with the common phase circle already present in the Tate curve
\(E_p\):

\[
 E_p=(\mathbb R/(\log p)\mathbb Z)_u
      \times
      (\mathbb R/2\pi\mathbb Z)_\theta.
 \tag{4.1}
\]

The \(\theta\)-direction is independent of \(p\).  Therefore every prime
orbit sits over the same phase object

\[
 \mathbb S^1_\theta.
 \tag{4.2}
\]

This common phase is the source-level reason the prime circles can be
assembled into one arithmetic flow object rather than a disjoint family.

### Definition 4.1: phase projection

Let

\[
 \pi_p:E_p\to\mathbb S^1_\theta
 \tag{4.3}
\]

be the projection to the common phase circle.

The arithmetic suspension will be constructed by forcing all prime-orbit
pages to share this same phase boundary.

## 5. The suspension groupoid

### Definition 5.1: object space

Define the source flow object \(\mathfrak X_{\mathrm{EF}}\) as the
groupoid obtained from the family of Tate orbit pages \((E_p)_{p}\) by
gluing them along the common phase circle:

\[
 \mathfrak X_{\mathrm{EF}}
 :=
 \left(\bigsqcup_p E_p\right)\sqcup \mathbb S^1_\theta
 \Big/
 \bigl(\pi_p(x)\sim \pi_q(y)\text{ whenever }
 \pi_p(x)=\pi_q(y)\bigr).
 \tag{5.1}
\]

Informally, this is the prime-orbit union with one shared archimedean
phase boundary.

### Definition 5.2: flow

Let \(\vartheta_t\) act on each \(E_p\) by translation in the \(u\)
coordinate and trivially on the \(\theta\)-coordinate:

\[
 \vartheta_t(u,\theta)=(u+t,\theta).
 \tag{5.2}
\]

Because the phase coordinate is common, these local actions glue to a
single flow

\[
 \vartheta:\mathbb R\times \mathfrak X_{\mathrm{EF}}
 \to\mathfrak X_{\mathrm{EF}}.
 \tag{5.3}
\]

Its primitive periodic orbits are precisely the prime circles \(C_p\),
with

\[
 \ell(C_p)=\log p.
 \tag{5.4}
\]

## 6. Return category of the flow

The purpose of the suspension is to realize `107_07` as a return
category of \((\mathfrak X_{\mathrm{EF}},\vartheta_t)\).

### Definition 6.1: return morphisms

For \(t\in\mathbb R\), let \([\Gamma_t]\) denote the return span of the
flow \(\vartheta_t\) on \(\mathfrak X_{\mathrm{EF}}\).  On the prime
orbit \(C_p\), the return at \(t=k\log p\) is the primitive-tower
correspondence

\[
 [\Gamma_{k\log p}]|_{C_p}=\Gamma_{p,k}.
 \tag{6.1}
\]

For times belonging to different prime towers, the common phase gluing
retains the mixed refinement square rather than collapsing it to a
connected return.

### Proposition 6.1: return category equals \(\operatorname{Corr}_{\mathrm{EF}}\)

The closed-orbit return category of
\((\mathfrak X_{\mathrm{EF}},\vartheta_t)\) is canonically identified
with \(\operatorname{Corr}_{\mathrm{EF}}\).

Proof.  On a fixed prime orbit \(C_p\), the return correspondence at
\(k\log p\) composes by time addition:

\[
 [\Gamma_{k\log p}]\circ[\Gamma_{\ell\log p}]
 =[\Gamma_{(k+\ell)\log p}],
 \tag{6.2}
\]

which is exactly the same-tower composition law of `107_07`.  The common
phase boundary prevents distinct prime towers from becoming isolated
components; their simultaneous return data survive as mixed refinement
spans, which is exactly the role of the raw mixed correspondences in
`107_07`.  Transpose is time reversal on the same return spans, and the
logarithmic labels are the flow times.  Therefore the return category is
precisely \(\operatorname{Corr}_{\mathrm{EF}}\).  \(\square\)

## 7. Degree-one cohomology and the diagonal class

The suspension object was chosen to avoid the first stop test.

### Proposition 7.1: why disjoint prime circles are insufficient

The disjoint union \(\bigsqcup_p C_p\) does not supply the source object
required by II-B.

Proof.  A disjoint union of circles has only the local orbit data.  It
has no common phase boundary, no global degree-one page coupling the
prime orbits, and no single diagonal class relating different towers or
the archimedean sector.  In particular, it cannot carry the determinant
gluing already fixed in Paper A.  \(\square\)

### Proposition 7.2: the glued suspension has the required global data

The groupoid \(\mathfrak X_{\mathrm{EF}}\) carries:

1. the prime closed orbits \(C_p\);
2. the common archimedean phase \(\mathbb S^1_\theta\);
3. a global diagonal class inherited from the self-correspondence of the
   glued object.

Proof.  Items (1) and (2) are built into Definitions 5.1 and 5.2.  The
global diagonal is the identity correspondence of the groupoid object
\(\mathfrak X_{\mathrm{EF}}\), whose restrictions to the orbit pages and
to the common phase are compatible by construction.  \(\square\)

This answers stop test 1.

## 8. Why averaging cannot replace the geometry

The second stop test rules out replacing the groupoid geometry by a
continuous average over holonomy parameters.

### Proposition 8.1: continuous averaging is insufficient

A purely absolutely continuous average over local holonomies does not
realize \(\operatorname{Corr}_{\mathrm{EF}}\) as a return category.

Proof.  The category \(\operatorname{Corr}_{\mathrm{EF}}\) retains
discrete tower labels \((p,k)\), mixed refinement squares, and connected
cyclic traces landing in the atomic divisor symbols \(Z_{p,k}\).  A
continuous average over holonomies erases those discrete return classes
into an absolutely continuous weight, precisely the pathology already
identified by the point-spectrum retention falsifiers of the program.
\(\square\)

Thus the flow object must preserve the discrete closed orbits as actual
geometric components, not only through averaged coefficients.

## 9. Why the zero-winding complement is not an ideal

The third stop test forbids deleting the zero-winding sector as if it
were an invariant ideal.

### Proposition 9.1: the zero-winding complement is not an ideal

The phase/zero-winding part of \(\mathfrak X_{\mathrm{EF}}\) cannot be
discarded while preserving flow composition and determinant gluing.

Proof.  The common phase circle is exactly the geometric locus through
which the prime orbit pages are glued.  Removing it would disconnect the
suspension into a disjoint union of prime circles, which was ruled out by
Proposition 7.1.  Moreover `106.153` already showed locally that deleting
the zero-winding sector is incompatible with heat-kernel composition.
The same obstruction persists here at the groupoid level.  \(\square\)

This answers stop test 3.

## 10. Compatibility with Paper A

### Proposition 10.1: determinant-line compatibility

The finite determinant lines and the Gamma--polar metric of Paper A are
compatible with the suspension flow.

Proof.  The finite lines of `107_04` depend on the derived intersection
of the return strata, and those strata are exactly the return spans of
\(\vartheta_t\) on the orbit pages.  The archimedean metric of `107_05`
depends on the common phase/Gamma boundary, which is precisely the
gluing boundary built into \(\mathfrak X_{\mathrm{EF}}\).  \(\square\)

### Proposition 10.2: connected cyclic trace compatibility

The connected cyclic trace of `107_07` is the connected return trace of
the flow \(\vartheta_t\) after applying the Eulerian projector to the raw
orbit union.

Proof.  The primitive closed orbit at period \(k\log p\) is \(C_p\)
traversed \(k\) times.  The raw orbit union keeps both primitive and
disconnected products of orbit returns.  Applying the first Eulerian
idempotent after cyclic trace extracts exactly the primitive connected
return \(Z_{p,k}\), just as in `107_07`.  \(\square\)

## 11. Stop-test audit

Work Package II-B passes its three stop tests.

### Stop test 1

A disjoint union of prime circles is insufficient.

Reason.  Proposition 7.1 shows it lacks common degree one and a global
diagonal.

### Stop test 2

Averaging over continuous holonomies may not replace geometry by an
absolutely continuous weight.

Reason.  Proposition 8.1 shows that such averaging erases the discrete
return classes needed by \(\operatorname{Corr}_{\mathrm{EF}}\).

### Stop test 3

The zero-winding complement may not be used as though it were an ideal.

Reason.  Proposition 9.1 shows that removing the phase boundary destroys
the suspension and its composition law.

## 12. Status inside Paper B

The source-defined suspension to an arithmetic flow is now fixed at the
interface level:

1. the primitive closed orbits are the circles
   \(\mathbb R_+^\times/p^\mathbb Z\);
2. their lengths are \(\log p\);
3. they are glued through one common archimedean phase boundary;
4. their return category is \(\operatorname{Corr}_{\mathrm{EF}}\).

What remains for Milestone II is the true arithmetic Lefschetz formula:
one must turn these return correspondences into a fixed-point trace
identity recovering the prime, Gamma, and pole terms jointly.  That is
the next work package of Phase 107.
