# P122 — minimal specification of a genuine row-D object

## Status

`SPECIFICATION`, not a construction and not a proof of row D.

The audit shows that the phase-121 parabolic/oriented carriers already
encode the defect but do not provide its conservation law.  It also shows
that A/B/C scalar data cannot functorially recover the missing
antisymmetric coordinate.  A genuine D must therefore be a pre-supertrace
mixed intersection object, not another operator factorization.

## 1. Carrier and objects

For each finite support window `T`, D must provide a stable topological
category `D_T` containing:

* two ruling objects `F_0,F_1`;
* mixed classes `M_f` for compactly supported test sources with both Tate
  evaluations defined;
* oriented local objects `Gamma_(p^k)^+` and `Gamma_(p^k)^-` before their
  scalar trace;
* an archimedean object carrying the exact Gamma distribution;
* restriction functors `D_S -> D_T` for `S<T` and a cofinal category.

The category must not be defined using positivity, the kernel, or the
spectral decomposition of `Delta_T`.

## 2. Operations

D must have, before comparison with `B_nuc`:

1. a mixed product or bivariant composition;
2. a duality/Rosati involution which does not identify the two causal
   orientations;
3. a degree/supertrace functor;
4. numerical equivalence defined as the radical of intersections with all
   objects, not only the two rulings;
5. a primitive subspace defined by orthogonality to `F_0,F_1`;
6. exact local-to-global reciprocity including the archimedean object.

## 3. Normalizations forced by A/B/C

The comparison functor must send the local oriented pair to the finite
terms with weights

\[
 {\log p\over p^{k/2}}
\]

and send the archimedean object to the exact Fourier finite-part Gamma
term.  It must retain cross-place phases and the coherent degree port.  Its
primitive condition must become

\[
 \widehat f(0)=\widehat f(1)=0.
\]

Only after all operations above are defined may one prove

\[
 (M_f,M_g)_D=B_{\rm nuc}(f,g).                        \tag{3.1}
\]

Defining the left side by (3.1) is forbidden.

## 4. The new theorem D must supply

One of the following genuinely geometric statements is required:

### D-Hodge

The numerical real space has exactly one positive direction, represented
by the ruling plane; hence

\[
 (M,M)_D\le0
\]

for every primitive mixed class.

### D-Riemann--Roch/effectivity

There is an effective cone and a Riemann--Roch inequality whose quadratic
term is the mixed self-intersection, with an equality classification strong
enough to exclude a nonzero primitive null class.

### D-oriented equality law

There is a source-defined pre-scalar transport on every object whose global
reciprocity forces the antisymmetric critical conormal class of a primitive
equality state to vanish.  It must be defined for all sources and proved
independently of `Delta_T>=0`.

The third version is analytically sufficient but, by P122.005, cannot be
obtained from row-C scalar data alone.

## 5. Required falsifiers

Before comparison (3.1), the construction must answer:

* **port swap:** what datum changes sign and why is it canonically oriented?
* **Davenport--Heilbronn:** which missing Euler/reciprocity axiom makes the
  object fail there?
* **shifted pair:** why does `xi(s+a)xi(s-a)` fail the same axiom?
* **function fields:** which standard surface intersection object is
  recovered?
* **Dedekind zeta:** does the construction extend?  If yes, the claimed
  theorem would also imply the corresponding GRH and must say so.

## 6. Acceptance test

A D candidate is accepted for proof work only if:

```text
carrier + operations + orientations + restriction
are constructed without B_nuc positivity;
an independent theorem proves Hodge/RR/oriented reciprocity;
the candidate fails a non-Euler explicit-formula model before comparison;
comparison with B_nuc is proved last.
```

At present no repository object satisfies this specification.  The closest
objects are the phase-121 oriented parabolic/K2/Rees carriers; they satisfy
parts of the carrier and local-normal requirements but fail the independent
global reciprocity/equality theorem.

## 7. Constructed finite-place subobject after P122.013--P122.017

There is now a literal finite-place subobject, still not a full D:

\[
 D^{\rm fin}_{T,\mathrm{sf}}
 =\bigl(
 L^\infty(\mathbb T^{S_T})\rtimes_\alpha\mathbb R,
 \tau_{S_T},D_\alpha,P_+,c_{S_T},
 \{L_p,L_p^\vee\}_{p\in S_T}
 \bigr).                                                  \tag{7.1}
\]

Here `alpha` is the logarithmic Kronecker flow, `tau` its canonical
semifinite trace, `D_alpha` its generator, `P_+` the Hardy spectral
projection, `c_(S_T)` the product of the relative Euler scatterings, and
`L_p` the local graph-determinant line constructed in P122.013.

Its exact status against Sections 1--3 is:

| required datum | status in `(7.1)` | evidence |
|---|---|---|
| all active prime powers | constructed | logarithmic derivative of `c_(S_T)` |
| weights `(log p)p^(-k/2)` | constructed | flow grading plus local Euler series |
| two causal orientations | constructed | Hardy polarization and dual line |
| port-swap sign | constructed | `L_p <-> L_p^vee` |
| cross-place phase before trace | constructed | full torus algebra and irrational flow |
| ordinary determinant line | impossible | P122.016, Theorem 1.1 |
| semifinite determinant class | constructed | P122.016, Theorem 3.1 |
| local positive rank-one curvature | constructed | P122.013 |
| algebraic tame/CC interpretation | refuted for this loop pair | P122.015, Proposition 2.2 |
| nonzero primary K1 index | refuted | P122.017, Section 4.1 |
| nondecomposable cross-prime determinant cocycle | refuted for the native cocycle | P122.017, Theorem 2.1 |
| archimedean Gamma object | missing from `(7.1)` | `b_infinity` is not in the Bohr algebra |
| both Tate conditions | not coupled | present only in the external primitive compression |
| global degree/supertrace comparison | partial | finite Euler logarithmic derivative only |
| Hodge/RR/equality theorem | missing | decisive open theorem |

Thus the phrase “construct D” has been reduced from an unspecified global
geometry to one explicit extension problem.  A full object must enlarge
(7.1) by a relative correspondence `E_(infinity,T)` whose left boundary is
the semifinite Bohr module and whose right boundary is the quarter-Gamma
Calderon module.  Its relative cocycle must contain `b_infinity`, descend
the two Tate constraints, and prove equality-state anomaly cancellation.

Merely adding the already known Gamma Gram column to (7.1) is not this
extension: P122.014 proves that its virtual determinant curvature is exactly
`q_T`, so the required semipositivity would be row (d) itself.

## 8. Proof-bearing two-gate interface

P122.019--P122.020 sharpen the equality-law part of the specification.  It
is sufficient for the relative correspondence to prove, on a source-defined
horizontal/null family larger than the equality radical and hence for
equality states as a consequence:

1. a critical Calderon trace theorem placing the completed incoming current
   in `H^(1/2)(I_T)`;
2. a horizontal gluing theorem under which zero incoming trace identifies
   two distinct active prime fibres before scalar supertrace.

The first property kills the Tate forcing by its explicit integer-activation
jumps.  The second kills the remaining homogeneous state by unequal local
Frobenius normalizations on the first causal cell.  Together with P122.002
they imply row (d), so neither may be postulated only on the radical: both
must be independently proved structural theorems of the constructed
correspondence.  P122.021 further proves that the first item is not generic
determinant regularity: sharp finite-window translation destroys the
endpoint class unless an additional transmission condition cancels its
jump.

## 9. Archimedean relative determinant after P122.022

The full Gamma scattering is not an ordinary restricted unitary.  P122.022
separates its universal Stirling chirp and proves that the residual
scattering differs from one by an `H^1` function.  It therefore constructs
the relative archimedean determinant datum

\[
 D^{\rm rel}_\infty
 =(P_+,q_\infty P_+q_\infty^*,L^{\rm det}_\infty,
   \phi_{\rm St}).
\]

Together with `(7.1)` and the quarter-oscillator background, this supplies
a determinant skeleton on both the finite and infinite sides.  It does not
supply the correspondence morphism between them: the symmetric mixed
cocycle still vanishes by parity, and sharp-window transmission remains
open.

## 10. Affine integer refinement after P122.024

The separate finite/infinite determinant skeleton admits a common
source-side refinement on `ell^2(N_0)`.  The Euler Hamiltonian `H=log(k+1)`,
quarter-Gamma oscillator `A_(1/4)=exp(H)-3/4`, additive successor `S` and
multiplicative isometries `V_p` satisfy

\[
 V_pS=S^pV_p,
 \qquad e^{-\beta H}V_pe^{\beta H}=p^{-\beta}V_p.
\]

Residue-class decomposition of `A_a` and Gauss multiplication give an
exact determinant connection anomaly `-log p`.  Hence both `log p` and the
half-density are now sourced inside one noncommutative arithmetic carrier.
The ordinary Fock-defect no-go is unchanged, and no theorem yet transports
this affine anomaly to the finite-window Gates R or S.

P122.025 performs that finite-window test.  The natural integer cutoff
preserves `V_pS=S^pV_p` exactly, and finite residue determinants have no
`log p` normal anomaly; the latter comes from the `a`-dependent zeta
dimension `1/2-a` only at the infinite Gamma end.  A further relative
finite/infinite transgression is therefore required before the affine
carrier can act on first contact.

P122.027 adds a finite alternative to the cofinal anomaly.  The positive
successor differential `S^*HS-H` integrates from the Gamma vacuum `1` to
its Frobenius image `p` with energy `log p`; modular half-density then gives
every `(log p)p^(-j/2)`.  The resulting path vectors have cross-prime Gram
`log min(p,q)`.  This is useful pre-scalar incidence data, but its ordinary
positive Gram contains mixed terms absent from row C.  A valid D must place
those overlaps in a graded causal transgression, not delete them by
orthogonalizing the primes.
