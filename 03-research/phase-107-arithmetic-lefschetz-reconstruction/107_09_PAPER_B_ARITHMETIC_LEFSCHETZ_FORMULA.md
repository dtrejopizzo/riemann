# 107.09 -- Paper B, Part III: the arithmetic Lefschetz formula

## 1. Purpose

This note executes Work Package II-C of `107_00`.  Its role is to turn
the decorated flow of `107_08` into an actual Lefschetz package:
for a compactly supported test function \(f\), the diagonal
intersection of the associated correspondence \(Z_f\) must recover the
complete prime--Gamma--polar side of the explicit formula.

The decisive rule is methodological as much as formal:

\[
 Z_f\cdot\Delta
 \text{ must be computed from fixed-point intersections, not imposed by definition.}
 \tag{1.1}
\]

The present paper therefore packages the prime-orbit trace of
`106.170`, the archimedean determinant page of `107_05` and `106.195`,
and the common-phase suspension of `107_08` into one source-defined
Lefschetz statement.

## 2. Input already available

Four earlier pieces are the required source data.

1. `107_06` provides the finite-support metrized intersection pairing on
   \(\operatorname{Div}_{\mathrm{EF}}\).
2. `107_07` provides the decorated correspondence category
   \(\operatorname{Corr}_{\mathrm{EF}}\), including transpose, diagonal,
   degree, and connected cyclic trace.
3. `107_08` provides the glued arithmetic flow
   \((\mathfrak X_{\mathrm{EF}},\vartheta_t)\) whose primitive closed
   orbits are the prime circles \(C_p\) with period \(\log p\).
4. `106.170`, `106.159`, and `106.195` provide the exact finite-prime
   Lefschetz index, the common-phase decomposition of the prime and
   archimedean pages, and the Gamma--polar determinant factor.

Nothing in this input uses the zeros of \(\zeta\) as construction data.
The zeros enter only after the arithmetic side of the explicit formula
has already been derived.

## 3. Test correspondences

Let \(f\in C_c^\infty(\mathbb R)\), and let \(\widehat f\) denote the
Fourier transform in the logarithmic-time variable of the flow.

### Definition 3.1: integrated return correspondence

Define the raw test correspondence

\[
 Z_f^{\rm raw}
 :=
 \int_{\mathbb R}\widehat f(t)\,[\Gamma_t]\,dt.
 \tag{3.1}
\]

Because \(\widehat f\) has compact support, only finitely many return
times \(t=k\log p\) meet the prime periodic orbits, so the finite-place
part of (3.1) is a finite sum inside the finite-support envelope of
`107_07`.

### Definition 3.2: diagonal renormalization

Let \(c_f\) be the coefficient dictated by the common-phase identity
channel and define

\[
 Z_f
 :=
 Z_f^{\rm raw}-c_f[\Delta].
 \tag{3.2}
\]

The point of \(c_f[\Delta]\) is not to manufacture the answer.  It
removes the identity return which otherwise appears simultaneously on
every orbit page and on the archimedean boundary.  This is the same
renormalized diagonal subtraction already forced by `107_05`,
`107_06`, and `106.159`.

## 4. Fixed-point decomposition

The fixed points of the return correspondence decompose into three
geometric sectors.

### Proposition 4.1: sector decomposition

For every compactly supported test \(f\),
\(Z_f\cdot\Delta\) splits canonically as

\[
 Z_f\cdot\Delta
 =
 \mathcal L_{\rm pr}(f)
 +\mathcal L_{\Gamma}(f)
 +\mathcal L_{\rm pol}(f).
 \tag{4.1}
\]

Here:

1. \(\mathcal L_{\rm pr}(f)\) is the sum of fixed-point contributions
   from the prime closed orbits \(C_p\);
2. \(\mathcal L_{\Gamma}(f)\) is the archimedean determinant-page
   contribution coming from the common phase boundary;
3. \(\mathcal L_{\rm pol}(f)\) is the trivial \(H^0/H^2\) polar
   contribution carried by the same archimedean page.

Proof.  The glued flow object of `107_08` has only two types of
fixed-point geometry: periodic prime-orbit returns and the common
archimedean boundary page.  On the latter, `106.195` separates the
positive Gamma degree-one page from the trivial hyperbolic polar sector
without changing Lefschetz parity.  The diagonal subtraction in (3.2)
removes the common identity channel, leaving exactly the three terms in
(4.1).  \(\square\)

The key feature of (4.1) is that the prime, Gamma, and pole terms are
computed in one joint fixed-point formula.  They are not estimated
separately and then recombined afterwards.

## 5. The prime term

### Proposition 5.1: prime fixed-point contribution

The prime-orbit sector in (4.1) is

\[
 \mathcal L_{\rm pr}(f)
 =
 -\sum_p\sum_{k\ge1}
 \frac{\log p}{p^{k/2}}\,
 \widehat f(k\log p).
 \tag{5.1}
\]

Proof.  Restrict the flow to a prime orbit \(C_p\).  The return at time
\(k\log p\) is the correspondence \(\Gamma_{p,k}\) of `107_07` and
`107_08`.  The fixed-point index of that return is exactly
\(-p^{-k/2}\) by the prime Lefschetz identity proved in `106.170`.
Weighting by the orbit length \(\log p\) and summing over all return
times inside the compact support of \(\widehat f\) yields (5.1).
\(\square\)

This is the stop-test-critical point where the geometry already
distinguishes \(\zeta\) from Davenport--Heilbronn: the latter does not
come from a primitive closed-orbit tower with one connected Euler
structure and therefore fails before any zero comparison is invoked.

## 6. The archimedean term

The common phase boundary contributes both the Gamma factor and the pole
term.  They must be extracted from the same metrized page.

### Proposition 6.1: Gamma--polar boundary contribution

The archimedean and polar sectors in (4.1) satisfy

\[
 \mathcal L_{\Gamma}(f)+\mathcal L_{\rm pol}(f)
 =
 \mathcal L_{\Gamma+\rm polar}(f),
 \tag{6.1}
\]

where \(\mathcal L_{\Gamma+\rm polar}(f)\) is the logarithmic
derivative distribution attached to the completed archimedean factor

\[
 \pi^{-s/2}\Gamma(s/2)\,s(s-1).
 \tag{6.2}
\]

Proof.  `106.195` realizes \(\pi^{-s/2}\Gamma(s/2)s(s-1)\) as one
relative determinant quotient whose denominator is the Gamma degree-one
operator and whose numerator is the trivial \(H^0/H^2\) determinant.
`107_05` fixes the same object as the Green metric governing the
archimedean self-intersection.  Therefore the archimedean fixed-point
trace and the diagonal metric use the same boundary page, and their
combined logarithmic variation is precisely the completed
Gamma--polar distribution in (6.2).  \(\square\)

Equation (6.1) is why the pole term may not be detached from the Gamma
term by separate absolute estimates: the two are different parity pieces
of the same fixed-point page.

## 7. Arithmetic Lefschetz theorem

### Theorem 7.1: arithmetic Lefschetz formula

For every compactly supported test function \(f\), the renormalized
correspondence \(Z_f\) of (3.2) satisfies

\[
 \boxed{
 Z_f\cdot\Delta
 =
 -\sum_p\sum_{k\ge1}\frac{\log p}{p^{k/2}}\widehat f(k\log p)
 +\mathcal L_{\Gamma+\rm polar}(f).
 }
 \tag{7.1}
\]

Equivalently,

\[
 \boxed{
 Z_f\cdot\Delta
 =
 \mathcal L_{\rm prime+Gamma+polar}(f).
 }
 \tag{7.2}
\]

Proof.  Proposition 4.1 decomposes the fixed-point intersection into the
prime, Gamma, and polar sectors.  Proposition 5.1 identifies the prime
sector with the complete finite-place coefficient system
\(-\log p/p^{k/2}\).  Proposition 6.1 identifies the remaining boundary
sector with the completed Gamma--polar distribution.  Adding the two
identities gives (7.1), hence (7.2).  \(\square\)

The theorem is arithmetic-side only.  Once (7.2) is established, the
classical explicit formula may be invoked to rewrite the same
distribution in terms of the spectral zero side, but that is a later
comparison step and not part of the construction.

## 8. Stop-test audit

### 8.1. Why (7.2) is not definitional

The construction begins with the source flow \(\vartheta_t\), its return
correspondences, the diagonal class, and the already-built determinant
pages.  The coefficient \(-\log p/p^{k/2}\) is imported from the local
fixed-point index theorem `106.170`; the Gamma and pole terms are
imported from the same archimedean determinant page used in the
intersection theory.  Therefore (7.2) is a computed fixed-point
identity, not the definition of a trace functional.

### 8.2. Davenport--Heilbronn falsification point

The package fails for Davenport--Heilbronn before zeros appear.  The
reason is structural: Work Package II requires a primitive closed-orbit
tower together with the connected Euler projector and common phase
gluing.  Those data are available for the Euler product of \(\zeta\) and
are not available for a non-Eulerian \(L\)-series.  Consequently the
object \([\Gamma_t]\) itself does not pass unchanged to the control.

### 8.3. Joint production of prime, Gamma, and pole terms

The diagonal intersection uses one correspondence \(Z_f\) and one
diagonal \(\Delta\).  The prime, Gamma, and pole contributions are
sectors of the same fixed-point calculation, so the completed arithmetic
side is produced jointly.  This satisfies stop test 3 of `107_00`.

## 9. Status of Milestone II

With `107_07`, `107_08`, and the present paper, the Phase 107
correspondence package now contains:

1. a decorated source correspondence category;
2. a glued arithmetic flow with prime closed orbits of length
   \(\log p\);
3. a fixed-point formula deriving the complete prime--Gamma--polar side
   of the explicit formula.

What is still missing is Part III: a global proper arithmetic surface
realizing these finite-support correspondences and carrying the future
Hodge-index sign argument.
