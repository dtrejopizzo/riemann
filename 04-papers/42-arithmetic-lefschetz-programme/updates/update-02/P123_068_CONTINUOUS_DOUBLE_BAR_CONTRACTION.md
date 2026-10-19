# P123.068 — Continuous contraction of the augmented double bar

Status: PROVED for twisted modules, finite direct sums and bounded
complexes of these objects. This upgrades the augmentation comparison of P123.067 from an
algebraic quasi-isomorphism to a continuous chain-homotopy equivalence.

Augment the horizontal double bar of P123.067 by placing
C_s(A,M tensor_A N) at horizontal degree r=-1. Retain s>=0. Let d be
the horizontal augmented boundary and let delta=(-1)^r d_v, including
the negative sign on the augmented column. Then

    d²=delta²=0, d delta+delta d=0.

The total augmented complex, with degree r+s, is the shifted mapping
cone of the augmentation, with these sign conventions. Each total
degree still has finitely many terms since r>=-1 and s>=0.

The explicit horizontal free-module contraction in P123.067 gives a
continuous h_0 raising r by one, preserving s, and satisfying
d h_0+h_0 d=1. Normalize it by h=h_0 d h_0. Then

    d h+h d=1, h²=0.

Indeed d h_0 and h_0 d are complementary idempotents. In particular
d h_0² d=(d h_0)(h_0 d)=0, proving h²=0, and the other identities follow
from idempotence. All maps remain continuous and retain their bidegrees.

Set A_0=1+delta h. Since delta h lowers s by one, its inverse is the
degreewise finite expression

    A_0^-1=sum_(j>=0)(-delta h)^j.

On a summand with vertical degree s the sum stops after j=s. This is
a continuous inverse on every total degree; no uniform infinite-series
estimate or change of totalization is needed. Direct calculation using
d delta=-delta d and h d=1-d h gives

    (d+delta) A_0=A_0 d.

Thus the full perturbed differential is A_0 d A_0^-1. Its contraction is

    H=A_0 h A_0^-1=h A_0^-1,
    (d+delta)H+H(d+delta)=1,

where the second expression for H uses h²=0. Every identity is an exact
identity of continuous maps between the complete total-degree spaces.

Consequently the augmentation has continuously contractible mapping
cone. It is a chain-homotopy equivalence in the category of continuous
complexes: writing the cone contraction in its two summand blocks gives
a continuous reverse chain map and the two homotopies. On the cone,
boundaries equal kernels and are closed; restriction of H to each kernel
is a continuous section of the boundary. No such closed-boundary claim
is made for the individual Hochschild complexes themselves.

Rotating the double bar gives the same result for the other augmentation.
Combined with the continuous rotation of P123.067, this supplies the
continuous derived cyclic comparison for two twisted modules, and for
their finite direct sums by taking the componentwise contractions.

## Extension to the entire bounded twisted-complex category

Use homological internal degrees i,j for bounded complexes K,L, with
lower bounds i_min,j_min. The augmented double-bar terms now have
indices (r,s,i,j), total degree r+s+i+j. Each total degree is a finite
direct sum: i,j are bounded and r>=-1,s>=0. The horizontal contraction
is defined componentwise on the twisted direct-sum terms and preserves
s,i,j. No compatibility of that initial contraction with the internal
differentials is assumed.

Order the total differential as

    D=d_h+(-1)^r d_v+(-1)^(r+s) d_K
                               +(-1)^(r+s+i) d_L.

Endpoint actions in the augmented column use its balanced tensor;
the displayed signs also apply at r=-1. Bimodule linearity of d_K,d_L
makes all unsigned differentials commute on distinct directions, so
with these signs d_h²=delta²=d_h delta+delta d_h=0, where delta is the
sum of the last three terms. Use the normalized horizontal h above.

On every summand define the nonnegative filtration weight

    w=s+(i-i_min)+(j-j_min).

The map h preserves w. Every term of delta lowers w by exactly one:
the vertical term lowers s, and the internal terms lower i or j.
Therefore (delta h)^(w+1)=0 on that summand. The same finite inverse
and conjugation computation as above now applies with this larger
delta. In a fixed total degree w is bounded over its finitely many
summands, so the inverse and resulting contraction are continuous maps
on the declared complete total-degree space.

Consequently both double-bar augmentations for every pair K,L in
P123.064 have continuously contractible cones. Their rotations use the
Koszul block sign (-1)^((r+i)(s+j)), obtained by exchanging blocks of
those total degrees. Checking each of the four boundary directions
shows it is a chain map. The resulting zigzag gives a continuous
chain-homotopy equivalence between the two derived diagonal complexes
of K star L and L star K. This includes the shifts and cones already
present in that bounded category; it is not restricted to objects with
zero internal differential.

The initial contractions depend on chosen free-term presentations.
The augmentation maps and double-bar rotation are natural; their being
homotopy equivalences does not require the chosen homotopy inverses to
be strictly natural. Higher shadow coherence still needs its appropriate
multi-bar comparison, not an assertion of strict naturality for those
choices.

The construction uses right freeness of the terms and bounded internal
degrees. It makes no claim for arbitrary unbounded objects or infinite
product totalizations. It closes the topological augmentation gap for
the bounded category of P123.064. It does not produce a determinant,
nuclear trace target, geometric localization or algebra-extension
excision. Those requirements of A remain separate from this homotopy.
