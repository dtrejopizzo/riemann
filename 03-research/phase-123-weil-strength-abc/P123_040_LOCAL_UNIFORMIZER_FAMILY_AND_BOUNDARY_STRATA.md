# P123.040 — local-uniformizer correspondences and their boundary strata

Date: 2026-09-05. Status: CONSTRUCTED for the refined arithmetic family,
its lattice comparison, chart maps and codimension-one fixed loci.
The full stratified trace/shadow theorem remains OPEN.

## 1. Retain the unit coordinates needed by C

P123.038 used a_S(n)=(1;n,...,n). This is a valid external family and
has the required lattice index. But its unit coordinates do not in general
agree with the local-idele embeddings j_p used in P123.032. Define instead

    b_S(n)=(1 at infinity; p^v_p(n) at each p in S_f),

with S containing all prime factors of n. Then b_S(m)b_S(n)=b_S(mn),
and b_S(p^k) is exactly the idele supported at p used by the finite-place
packet. Normalizing gives

    h_S^loc(n)=(1/n; p^v_p(n)/n at each p in S_f).   (1.1)

The finite entries of (1.1) are units. They are usually not all 1.
The family E_n^loc=E_(beta_(b_S(n))) therefore supplies the actual
prime uniformizer classes while retaining the repaired completed tensor
law E_m^loc tensor E_n^loc ~= E_(mn)^loc and Tate modulus 1/n.

The two families have the same finite lattice image:

    b_S(n)L_S=nL_S,

because n/p^v_p(n) is a p-adic unit in each coordinate. Their finite
lattice index cannot distinguish them, whereas nonradial scalar tests
can. Thus the lattice determinant alone must not be used to identify
their external characters.

## 2. Coherent chart realization for this arithmetic family

For S contained in T with the prime factors of n already in S,
(1.1) in the new coordinates has value 1/n. Consequently

    pi_TS(h_T^loc(n))=h_S^loc(n)

for the normalized projections of P123.023. Its global inverse-limit
class is exactly the product of the local prime uniformizer classes.
The compatible normalized coefficient action of that note therefore
applies, including its unit factors.

There is also a direct presentation-level chart map. A gauge lift of
b_S(n) is gamma b_S(n), gamma in Gamma_S^+. Send it to gamma b_T(n).
At each added place this has value gamma, a unit, so it preserves 1_Zp.
The coefficient map j_ST consequently intertwines the two actions.
Send a gauge arrow labelled delta to the same label delta. These maps
preserve multiplication of n and of the gauge labels and compose on
chart triples. P123.019's tensor and gauge formulas then give coherent
maps on this arithmetic gauge-generated category.

This is a specified arithmetic chart functor, not the assertion that
P123.020's universal lift L_ST sends b_S(n) to b_T(n). It does not:
that universal lift adds n, while the new canonical arithmetic lift
adds 1. The normalized inverse-limit action and the arithmetic
presentation above keep the distinction explicit.

## 3. Transport the cotangent cube with the necessary unit maps

Write c_S(n) for the coordinatewise multiplier p^v_p(n) on L_S, and
u_S(n)=n/c_S(n), a unit in product Z_p. These are multiplicative in n.
Define the actual-action complex

    D_(S,n)=[L_S --c_S(n)--> L_S].

The chain map

    [L_S --n--> L_S] -> D_(S,n),
    degree -1: u_S(n),   degree 0: id,              (3.1)

is an isomorphism because c_S(n)u_S(n)=n. Composing with P123.038's
C_n comparison gives a specified quasi-isomorphism from the integral
cotangent complex to the lattice complex of the refined action.

For n=md, transport the cotangent divisor map (id,m) through (3.1).
Its map D_(S,d) -> D_(S,n) is

    degree -1: u_S(m),   degree 0: multiplication by m.

These maps commute on every divisor face because u_S is multiplicative.
They are NOT the bare maps (id,c_S(m)) supplied by multiplying by the
finite uniformizer alone: they include its canonical unit correction.
Both descriptions have the same image lattices, but forgetting this
unit correction would destroy the stated natural cotangent comparison.
Projection of finite coordinates commutes with all these maps. Added
coordinates are acyclic when their primes do not divide n.

Thus the full primitive total-cofiber cube, not only its group order,
is transported to the refined external family. Its values remain Z/p
for prime powers and zero for mixed n.

## 4. Construct the single-zero boundary orbit

Fix p in S_f and take the stratum

    Z_(S,p)={x_p=0; x_v!=0 for v!=p; x_infinity>0}

of the additive carrier X_S. Normalize the valuations at the finite
places other than p by the corresponding S-units. The remaining group
is p^Z. This gives the explicit orbit model

    Gamma_S^+ backslash Z_(S,p)
      ~= [R times product_(ell in S_f minus {p}) Z_ell^*]/Z,

where the residual integer j acts by

    (t,(v_ell)) -> (t+j log p,(p^j v_ell)).          (4.1)

The real coordinate is logarithmic. The residual action is free and
proper because its real displacement is j log p. The quotient is a
compact mapping torus. With dt and probability Haar on the compact
unit factors, its volume is log p, using 0<=t<log p as a fundamental
region. This conclusion concerns the individual stratum, not properness
of the action on a union of strata or on all X_S.

## 5. Prime-power support is visible in the fixed-locus equations

A class in this stratum is fixed by b_S(n) only if there is
 gamma in Gamma_S^+ with b_S(n)x=gamma x. Since the real coordinate
is nonzero and the real entry of b_S(n) is 1, necessarily gamma=1.
Every nonzero finite coordinate ell!=p then forces

    ell^v_ell(n)=1.

Since S contains the prime factors of n, this is equivalent to n=p^k
(or n=1). Conversely b_S(p^k) fixes the whole stratum pointwise.
Its action in the transverse Q_p coordinate is multiplication by p^k.
The local half-density fixed-point Jacobian for k!=0 is therefore

    |p^k|_p^(1/2)/|1-p^k|_p=p^(-|k|/2).

The orbit volume log p and this normal factor are exactly the two
geometric factors in the finite-place packet. For a mixed n, none of
the single-zero finite strata is fixed. Strata with several zero
coordinates can still be fixed; their contributions have not been
shown to vanish by this calculation.

More generally, the idele with x in Q_p^* at p and 1 elsewhere fixes
this stratum and acts by x on its transverse coordinate. For x=p^k u,
its normalized coordinates are real p^-k, p-unit u, and other unit
coordinates p^-k, exactly as in P123.032. This realizes the full local
parameter, including its unit dependence, on the same stratum. The
singularity at x=1 still requires the Fourier normalization of P123.034
and its comparison with the eventual source trace.

## 6. What this adds, and the trace still to construct

The carrier now has a coherent arithmetic family with the correct
nonradial unit data, the same integral primitive contact cube, and
explicit boundary orbits whose fixed-locus equations select prime powers.
The factors log p and p^(-|k|/2) have separate orbit-volume and transverse
origins on those strata.

This does NOT yet prove that a Hilbert-space trace is the product of
those factors. A positive-dimensional fixed stratum has tangential
excess; restricting the kernel of its identity operator to the diagonal
is not automatically a finite trace. The common shadow must perform
that localization/regularization, control the multiple-zero strata,
and compare its integrated action with the nuclear representation.
The mapping-torus volume is geometric data for that theorem, not a
replacement for it. Integral determinant compatibility, mixed RR,
effectivity and the global D sign remain required.
