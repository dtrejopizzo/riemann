# P123.072 — Relative diagonal on the full bounded twisted category

Status: CONSTRUCTED with continuous cyclic comparison
in the chain-homotopy category. Determinant/nuclear realization and
geometric descent remain open.

Let e:A -> D be scalar-label projection, with e beta=e for every
external twist beta. There is a dg functor F_e from P123.064 to bounded
finite free D-bimodule complexes: it sends every E_beta to D and an
intertwiner given by right multiplication by v to multiplication by e(v).
The matrix differential squares to zero because e is multiplicative.
Composition is preserved for the same reason. Since

    e(x beta(y))=e(x)e(y),

the functor preserves the completed tensor composition and its unit,
with the finite-rank free identifications already proved. It preserves
shifts and cones. This is a scalar quotient functor on the stated objects,
not the failed two-sided induction asserting A tensor_R A=A.

For K in this category there is a continuous natural chain map

    q_K:C_*(A,K) -> C_*(D,F_e K),

given by e on every bar factor and on every twisted-module coefficient.
Intertwining the endpoint actions follows from e beta=e. Intertwining
the internal differential follows by applying e to its matrix entries.
Define the relative diagonal to be the explicit mapping fiber

    S_rel(K)=Cone(q_K)[-1].

Every total-degree space is complete, as the sums are finite in the
declared bounded internal/bar totalization. The construction is functorial
on continuous chain maps and homotopies. For an individual twisted module
q_K has the chain section given by j on all factors, and the fiber is
homotopy equivalent to the split kernel in P123.071.

For a general complex, that section need not commute with its differential.
Indeed a differential entry v can differ from j e(v) by an ideal element.
This is why the mapping fiber, rather than an assumed split kernel
decomposition of the whole complex, is used here. At each chain degree
the scalar projection is still linearly split; no differential splitting
is inferred from it.

To compare S_rel(K star L) and S_rel(L star K), apply e to every factor
of the double-bar constructions over A and D. These maps commute exactly
with the canonical augmentations and Koszul block rotations. Taking
mapping fibers gives a zigzag between the two relative diagonals.
Its augmentation arrows are continuous chain-homotopy equivalences:
both components are such equivalences by P123.068, and a commuting square
with homotopy-equivalent vertical maps induces a homotopy equivalence
on mapping fibers. This last statement follows by applying the mapping
cone construction to that square; the cone of the induced map is built
from the two contractible vertical cones and is contractible by the
finite two-step perturbation argument of P123.068.

For three or more factors use the common multibar of P123.069. Applying
e commutes with all its rotations and interval augmentations. The same
mapping-fiber argument proves associative, cyclic and unit coherence
in the homotopy category. Thus relative subtraction is compatible with
the stable source operations, without choosing a scalar subtraction
separately for each arithmetic label.

The relative target remains a homotopy category of generally unbounded
Fréchet complexes. This result does not prove that S_rel(K) is perfect,
nuclear or scalar trace class, and does not establish its restriction to
geometric strata or a mixed Riemann--Roch determinant. It removes the
restriction of P123.071 to individual twists while keeping the actual
remaining A.5–A.9 requirements explicit.
