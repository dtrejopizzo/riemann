# 107.151 -- Middle tolerance cohomology for a bounded three-term complex

## 1. Result

The tolerance formalism used by Connes--Consani in 2022 for the
cokernel of a bounded two-term complex extends canonically to the middle
term of a three-term complex.  This removes the formal quotient
obstruction to defining \(H^1\) on a square, provided that its Cech
complex is realized inside Eilenberg--MacLane modules.

Let

\[
 A^0\xrightarrow{d_0}A^1\xrightarrow{d_1}A^2,
 \qquad d_1d_0=0,
 \tag{1.1}
\]

be a complex of abelian groups and let \(E^0\subset HA^0\) be a bounded
\(\mathbb S[\pm1]\)-submodule.  Put

\[
 Z^1:=\ker(Hd_1:HA^1\longrightarrow HA^2).
 \tag{1.2}
\]

For every finite pointed set \(F\), define a relation on \(Z^1(F)\) by

\[
 x\,\mathcal R_F\,y
 \quad\Longleftrightarrow\quad
 x-y=Hd_0(e)\quad\text{for some }e\in E^0(F).
 \tag{1.3}
\]

Then

\[
 H^1_{\rm tol}(E^0\to HA^1\to HA^2):=(Z^1,\mathcal R)
 \tag{1.4}
\]

is a tolerant \(\mathbb S[\pm1]\)-module.

## 2. Proof

Reflexivity follows from \(0\in E^0(F)\).  Symmetry follows because
\(E^0\) is stable under multiplication by \(-1\).  No transitivity is
asserted or required.

For a pointed map \(u:F\to F'\), the Eilenberg--MacLane structure map
pushes divisors forward by summing on fibres.  Naturality of \(Hd_0\)
gives

\[
 u_*(x-y)=Hd_0(u_*e).
\]

Since \(E^0\) is a submodule, \(u_*e\in E^0(F')\); hence every structure
map preserves \(\mathcal R\).  The same argument proves compatibility
with the \(\mathbb S[\pm1]\)-action.  Finally \(d_1d_0=0\) ensures that
related cocycles remain in \(Z^1\).  Thus (1.4) is an object of the
Connes--Consani category of tolerant sphere modules.

## 3. Functoriality and invariance

A morphism of complexes

\[
 (f^0,f^1,f^2):(A^\bullet,d)\longrightarrow(B^\bullet,\delta)
\]

with \(Hf^0(E^0)\subseteq F^0\) induces

\[
 H^1_{\rm tol}(f): (Z_A^1,\mathcal R_A)
 \longrightarrow (Z_B^1,\mathcal R_B).
\]

Indeed, \(f^1\) maps cocycles to cocycles and

\[
 f^1(x-y)=f^1d_0(e)=\delta_0f^0(e).
\]

Composition and identities are inherited from the chain maps.  If all
\(f^i\) are isomorphisms and \(Hf^0(E^0)=F^0\), the induced morphism is
an isomorphism of tolerant modules.  Consequently every dimension
defined intrinsically from the tolerant module is invariant under
isomorphism of the bounded complex.  It cannot suffer the Yoshitomi
failure of a numerical rank that is not an isomorphism invariant of its
module.

## 4. Recovery of ordinary cohomology

If \(E^0=HA^0\), then \(Hd_0(E^0)=H(\operatorname{im}d_0)\) is a subgroup
of \(HA^1\).  Relation (1.3) is then transitive and

\[
 (Z^1/\mathcal R)(1_+)
 =
 \ker d_1/\operatorname{im}d_0.
\]

Thus the construction recovers ordinary middle cohomology whenever the
classical quotient exists.  For a proper bounded submodule, transitivity
may fail; retaining the tolerance relation records this failure instead
of adding its transitive closure and manufacturing spurious classes.

## 5. Exact remaining condition for the square

This theorem does not yet define \(H^1\) of the Scaling Site square.
It reduces that task to one geometric construction:

\[
 \boxed{\text{construct its Cech terms and differentials as a complex
 of bounded submodules of Eilenberg--MacLane modules.}}
\]

The 2018 tropical Cech complex lived in idempotent semimodules, where
subtraction and (1.3) are unavailable.  The 2022 arithmetic-curve
construction does live in the required abelian ambient modules, but its
extension to the square has not been published.  Therefore the formal
middle-cohomology operation is now available; the sheaf-level lift of
the square remains open.  By 107_164 that lift cannot be obtained by
additively linearizing reduced Newton polygons: it must retain enriched
unreduced monomial support and tropicalize only afterward.
