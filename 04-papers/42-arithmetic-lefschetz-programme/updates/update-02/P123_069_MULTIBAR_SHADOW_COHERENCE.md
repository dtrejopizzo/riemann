# P123.069 — Multibar coherence of the continuous derived source shadow

Status: PROVED in the continuous chain-homotopy category
for bounded twisted complexes. This does not supply the determinant or
nuclear target demanded by the full row-A contract.

For a finite ordered cyclic list K_1,...,K_m of bounded twisted complexes,
take the completed cyclic multibar with terms

    K_1 tensor_pi A^tensor r_1 tensor_pi ...
                       tensor_pi K_m tensor_pi A^tensor r_m,
    r_j>=0.

The jth bar differential merges along the interval from K_j to K_(j+1),
with the cyclic convention K_(m+1)=K_1. Include all internal differentials.
Order the blocks as displayed and use the usual Koszul totalization signs.
Commuting left/right module actions imply that different unsigned bar
directions commute; the totalization signs make the total differential
square zero. Bounded internal degrees and nonnegative r_j ensure finitely
many summands in every total degree. Every term and map is continuous
in the completed projective topology.

Give block j total degree d_j=deg(K_j)+r_j. Rotation of the first block
to the end has sign

    (-1)^(d_1(d_2+...+d_m)).

It is a chain map by the same direction-by-direction sign calculation
as P123.067–068. Applying m successive rotations is identity: every
pair of block degrees occurs twice in the accumulated exponent. More
generally, two decompositions of the same block permutation have the
same Koszul sign, since that sign counts the same inverted pairs.
These are literal continuous chain identities on the common multibar.

An augmentation of a noncyclic interval bar composes its neighboring
modules by their completed balanced tensor. The resulting object remains
a bounded twisted complex by P123.064. Its augmented cone has the
horizontal contraction used in P123.068. Perturb by all remaining bar
directions and all internal differentials. The nonnegative weight given
by the sum of the other bar lengths plus all shifted internal degrees
decreases under every perturbation term and is preserved by the chosen
horizontal homotopy. Thus the same finite inverse constructs a continuous
contraction of that cone. Each such interval augmentation is therefore
a continuous chain-homotopy equivalence.

Augmenting two adjacent intervals in either order gives the same map
under the tensor associator: both maps balance the same adjacent actions
and multiply the same factors. This can be checked in bar degree zero;
both augmentations vanish in a positive degree of either collapsed
interval. Disjoint interval augmentations likewise commute. These
identities extend by density and remain compatible with block rotation.

It follows that the pairwise cyclic comparison of P123.068 is coherent
under associative composition in the continuous chain-homotopy category.
Indeed all routes are represented on the same finite multibar, where
the rotation and augmentation diagrams commute. The augmentation arrows
are invertible in that category, so their inverses preserve those
commuting diagrams. The conclusion uses the canonical augmentation
maps; it does not assert that a chosen explicit contracting homotopy
is strictly natural.

The empty insertion of a tensor unit is handled by the ordinary bar
unit augmentation and insertion of 1. The same contraction shows that
inserting or removing such a unit agrees with the unit maps of P123.064
in the homotopy category. Thus finite composition, cyclic rotation and
the tensor unit have compatible comparison maps on this declared domain.

This gives a coherent continuous derived source shadow with values in
the homotopy category of the displayed Fréchet complexes. It establishes
neither a perfect determinant target nor a nuclear trace realization.
In particular it does not turn arbitrary homotopy-equivalent complexes
into finite-dimensional objects, establish algebra-extension excision,
or construct the mixed Riemann--Roch equality. Those remain the substantive
target and geometry requirements of A.5–A.9.
