# P123.030 — completed split Amitsur resolution over rapid scalar labels

Date: 2026-09-05. Status: PROVED for the completed module complex and
chart compatibility specified here. This is not integral descent or a
trace-class correspondence equivalence.

## 1. Change of base explicitly declared

For every finite semilocal chart S, let A=A_S^u and let D=C_S^rapid be
its unital scalar rapid label algebra. P123.019 supplies maps

    i:D -> A,  e:A -> D,  e i=id,

where i inserts constant coefficients and e evaluates coefficients at
the added point infinity. They are continuous unital algebra maps, with
p_k(i d)=p_k(d) and p_k(e a)<=p_k(a). In particular e is a D-bimodule
map for the D-actions induced by i, even though i(D) need not be central.

This base is D, not Z[T,T^-1] and not its uncompleted complex version.
Thus the following result does not assert topological flatness over the
polynomial base of P123.029.

## 2. Completed complex and contraction

Let N be a complete Frechet left D-module with a jointly continuous
unital action. Set C^(-1)=N. For r>=0 define C^r as the Hausdorff
completion of

    A tensor ... tensor A tensor N  (r+1 copies of A)

with the projective topology and all adjacent D-balancing relations.
Equivalently take the completed projective tensor of the Frechet factors
and divide by the closed span of these relations. This simultaneous
quotient fixes the convention without requiring an unproved iterated
balanced-tensor associativity theorem.

The augmentation inserts 1 before N. The differential d:C^r -> C^(r+1)
is the alternating sum of inserting 1 in each of the r+2 positions
among the A factors, including the position immediately before N.
Insertion identities imply d^2=0 on elementary tensors and hence on
the completion by continuity.

Define h:C^0 -> N by

    h(a tensor n)=e(a)n.

For r>=1 define h:C^r -> C^(r-1) by

    h(a_0 tensor a_1 tensor ... tensor a_r tensor n)
      = i(e(a_0))a_1 tensor ... tensor a_r tensor n.

The D-bimodule property of e proves balancing at the first slot; the
remaining balancing relations are preserved directly. Continuity follows
from p_k(i(e(a_0))a_1)<=p_k(a_0)p_k(a_1) and continuity of the action
on N. Thus these maps extend to the Hausdorff completions.

Since e(1)=1, applying h to the first insertion gives the identity.
Every other insertion cancels with the corresponding term of d h.
Consequently

    h d + d h = id,   and h d=id on C^(-1).

These are identities of continuous D-linear maps. The completed
augmented complex is therefore split exact. More precisely d h is a
continuous projection onto ker d: the homotopy identity gives d h x=x
for x in ker d, and d^2=0 puts its image in ker d. Hence each image
of d is closed and complemented. This proves strict exactness in the
specified Frechet topology, rather than only density of images.

## 3. Chart compatibility

For S contained in T, let k_ST:D_S -> D_T insert the old group labels,
and let j_ST:A_S -> A_T be the coefficient embedding of P123.020.
The coefficient formula f+c -> f tensor 1_Rnew+c shows

    e_T j_ST = k_ST e_S,    j_ST i_S=i_T k_ST.

For a continuous k_ST-linear map N_S -> N_T of the declared modules,
tensoring these maps yields continuous maps of the simultaneous
balanced quotients. They commute with every insertion and with h.
Thus the contraction is coherent on chart triples whenever the module
maps are. No direct-limit identification of all global idele classes
is needed or asserted.

## 4. Trace and integral boundaries

This gives completed module resolutions over D on all finite charts.
It does not identify A tensor_D A with A or make the two-sided induction
of P123.028 strong monoidal. A resolution is additional data, not an
isomorphism of its first term with the diagonal.

It also does not automatically restrict to the old kernel ideal
K=ker e, the sector in which earlier traces were defined. Insertion of
the unit leaves K, and h uses e on its first factor; e vanishes on K.
Therefore a trace on K cannot simply be applied termwise to this entire
resolution without a separate admissible trace domain and comparison.
This is a concrete remaining A.5/C requirement.

Finally all coefficients here are complex. The construction cannot
recover the finite integral torsion from P123.025–026. An integral model
and a compatible determinant/shadow comparison remain necessary.
No effectivity, mixed RR or sign theorem is inferred from split exactness.
