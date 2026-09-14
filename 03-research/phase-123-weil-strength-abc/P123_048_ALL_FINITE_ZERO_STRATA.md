# P123.048 — All finite zero strata and their strict source filtration

Date: 2026-09-05. Status: PROVED for the stratum presentations and
completed filtration below. No regularized-shadow spectral sequence or
vanishing of its higher-stratum terms is asserted.

## 1. A uniform presentation of every zero-coordinate stratum

Write P=S_f and r=|P|. For J contained in P let Z_J be the subspace of
X^+ with x_p=0 exactly for p in J. The stratum J=empty is the generic
orbit of P123.044. For nonempty J, divide first by the subgroup generated
by P\J, normalizing the valuations of the nonzero coordinates to zero.
The remaining presentation is

    [Z_J/Gamma] ~= [B_J/Gamma_J],
    B_J=R times product_(ell notin J) Z_ell^*,
    Gamma_J=product_(p in J) p^Z.                  (1.1)

For gamma in Gamma_J the action on B_J is

    (t,(u_ell)) -> (t+log gamma,(gamma u_ell)).    (1.2)

All displayed finite multipliers are units, since ell is outside J.
The valuation normalization is unique and locally continuous. Retaining
the residual action proves (1.1) on objects and arrows, not only orbits.

Choose p_0 in J. Its subgroup p_0^Z acts freely and properly because it
translates t by integer multiples of a_0=log p_0. Its quotient

    Y_J,p0 = B_J/p_0^Z

is a compact mapping torus. The residual group
Gamma_(J\{p0}) ~= Z^(|J|-1) acts by the transformations (1.2). Thus

    [Z_J/Gamma] ~= [Y_J,p0 / Z^(|J|-1)].          (1.3)

Pulling the right action groupoid back along B_J -> Y_J,p0 recovers a
unique p_0 deck exponent for each lifted arrow, exactly as in P123.047.
This proves the second reduction explicitly. Different choices of p_0
give presentations of the same original groupoid; no preferred zero
coordinate is part of the original source.

For |J|=1 the residual group is trivial and this is the compact boundary
orbit already used. For |J|>=2 a higher-rank return action remains. When
J=P and |P|=2 it is precisely the irrational rotation model of P123.047.

## 2. Compact-transversal algebra for every stratum

The quotient of dt times probability unit Haar gives Y_J,p0 invariant
measure of mass a_0. Divide it by a_0 to obtain probability measure mu_J.
All residual actions preserve this measure, since they are commuting
translations of B_J. Define the finite-sum transformation algebra

    B_J,alg = C(Y_J,p0) crossed_alg Z^(|J|-1).

If z=sum_n f_n V^n, its identity-coefficient functional is

    tau_J(z)=integral f_0 dmu_J,
    tau_J(z* z)=sum_n integral |f_n|² dmu_J.       (2.1)

The crossed multiplication and invariance of mu_J prove cyclicity as
in P123.047. The measure has full support, so the trace is faithful on
this algebra. It extends continuously to the specified completion with
seminorms sum_n ||f_n|| exp(k||n||_1). This provides explicit nonzero
trace-bearing transversal models for all finite-zero strata.

These normalized traces depend on a measure convention. Their comparison
under a change of transversal and their value in the intended relative
shadow are not supplied by normalization alone. Likewise the displayed
transversal completion is not asserted to be automatically equivalent to
the original height-weighted source completion.

## 3. Closed zero-count filtration in the original space

Let

    F_k={x in X^+: at least k finite coordinates vanish},
    F_0=X^+, F_(r+1)=empty,
    L_k=F_k\F_(k+1)=disjoint_union_(|J|=k) Z_J.

Each F_k is closed and invariant. Inside L_k, every Z_J is both open
and closed: near its point the coordinates outside J remain nonzero,
and exactly k zeros then forces the zero set to stay J. Therefore

    A(L_k) ~= direct_sum_(|J|=k) A(Z_J)           (3.1)

for the finite direct sum of the original rapid crossed products.
This decomposition is of a layer, not of the whole space; it does not
remove the attaching information between successive layers.

## 4. Strict rapid extension at each layer

The commuting projections E_i of P123.045 restrict to C_0(F_k): replacing
a coordinate by zero stays inside F_k, and multiplying by chi_i restores
vanishing at infinity in that coordinate. Their norms are at most one.
On C_0(F_k) form

    Q_(k+1)=sum_(|J|>=k+1)
                 product_(i in J) E_i product_(i notin J)(1-E_i).

Its expanded terms evaluate only points of F_(k+1), and its restriction
to that subset is the identity, by the same zero-coordinate evaluation
argument as in P123.045. Thus it defines a bounded linear extension

    e_(k+1): C_0(F_(k+1)) -> C_0(F_k),
    ||e_(k+1)|| <= 3^r.

Explicitly, expand Q_(k+1) in products E_I and apply each term to g by
evaluating g with the I coordinates set to zero and multiplying by
product_(i in I) chi_i. All those evaluations are in F_(k+1).
This also proves directly that the extension is continuous and vanishes
at infinity on F_k; no unchosen extension theorem is needed.

Coefficientwise extension has the same bound for every rapid seminorm.
Consequently, for every k=0,...,r,

    0 -> A(L_k) -> A(F_k) -> A(F_(k+1)) -> 0      (4.1)

is a strict exact sequence of Fréchet star algebras with a continuous
linear splitting. The last sequence has zero quotient. Restriction and
inclusion are equivariant; the chosen splittings are not asserted to be
equivariant or multiplicative. The kernel identification is extension
by zero from the relatively open layer L_k.

Combining (3.1) and (4.1) now gives all finite-zero layers and all source
extensions connecting them in the actual rapid topology. P123.045 is
the special cut separating the first two layers from F_2.

## 5. The remaining comparison has a complete list of finite layers

For a fixed semilocal set S, no finite-zero stratum is left unspecified
by (1.3), and none is omitted from (4.1). The missing result is an
excisive realization of the desired relative shadow on this filtration,
with its actual connecting maps and trace contributions. Nonzero algebras
and the traces (2.1) do not imply a particular Weil contribution, and
do not justify declaring higher layers zero.

The first-layer normal cutoff character is P123.043–046. It must now be
compared with the same shadow through (4.1), including the generic layer
and all higher layers. Integral contact compatibility, the real-zero
boundary, chart changes and the D sign remain part of the full objective.
