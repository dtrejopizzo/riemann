# Candidate: a non-abelian harmonic polarization theorem

## Status

**The literal parabolic-Higgs formulation below is rejected after the type
audit in `P3_NONABELIAN_MOMENT_MAP_AUDIT.md`.**  It remains useful as the
motivation for the correctly typed Bogomolny/Hilbert-quiver formulation, but
its claimed rank-one-place stability lemma is false as a reduction principle:
it omits mixed analytic subobjects.  No global square is claimed.

A semantic audit of phases
1--120 and papers 1--42 found no occurrence of Hitchin equations, harmonic
bundles, Higgs bundles, non-abelian Hodge theory, Hermitian--Einstein metrics
or parabolic stability.  The construction is designed to attack the exact
remaining equation (5.3), not to replace it by another scalar inequality.

## 1. Why the carrier must be non-abelian

The finite Euler--Gamma determinant supplies the exact scalar connection

```
d log D_T = Z_T ds,
```

but its Hermitian determinant metric is flat.  Every radial positive
regularization changes the coefficient of `Z_T`.  A non-abelian connection
can keep its determinant connection fixed while carrying nonzero trace-free
curvature:

```
tr F_A = 0,                 F_A + [Phi,Phi^{dagger_h}] = 0.
```

Thus the already forced Green coefficient may remain untouched, while the
commutator term supplies a genuine bulk square.

## 2. The source-defined star Higgs object

For a finite active place set `S_T`, use the doubled slit domain of the common
field `Z_F(t,zeta)` from the causal primitive-storage construction.  Define a
star object with:

* one central quarter-Gamma/Tate vertex `E_infty`;
* one rank-one leg `L_p` for every place `p in S_T`;
* the two opposite parabolic flags at the compact-potential ends, fixed by
  `M_-` and `M_+`;
* a nilpotent residue on the `p`-leg at every exterior jump `p^(2j)`, of
  length `sqrt(log p) p^(-j/4)`;
* determinant connection equal to the already constructed quarter
  determinant connection;
* leg-to-centre arrows equal to the Frobenius jump traces (4.66)--(4.67),
  before comparison with `B_nuc`.

The prime labels are places, not norms.  Mixed composites are paths through
the centre rather than new residues.  Their cancellation is imposed by the
complex moment equation, which is the already proved zero-residual Green
identity, not by deleting them from a positive Gram.

## 3. The originally proposed theorem (not established)

### Non-abelian harmonic polarization theorem

For every finite `S_T`, the source-defined quarter-twisted star Higgs object
has the following properties.

1. **Arithmetic stability.** Every proper saturated Higgs subobject compatible
   with both Tate flags has strictly negative parabolic slope.
2. **Canonical harmonic metric.** The determinant-normalized energy functional
   has a unique minimizer `h_T`; equivalently, `h_T` solves the real moment
   equation on the doubled slit domain with the prescribed jump residues and
   Tate boundary flags.
3. **Primitive Green identity.** If `F=L_0G`, the Dirac--Higgs operator of
   `(E_T,Phi_T,h_T)` has canonical solution `U_G` and

   ```
   ||D_(A_T,Phi_T) U_G||^2
     = -B_nuc,T(L_0G,L_0G).
   ```

4. **Inactive-place compatibility.** Adding a place with `log p >= 2T_0`
   adds a stable orthogonal leg whose residue has zero trace on sources
   supported in `[-T_0,T_0]`; the primitive energy is unchanged.

Items 2--4 would give the finite global square, exact compact-support
stabilization, the cofinal limit and row (d).

## 4. The genuinely new lemma

The theorem must not import stability as a hypothesis.  Its arithmetic core
is the following statement.

### Rejected rank-one-place stability lemma

Let `W` be a saturated invariant subobject of the star object.  Then either:

* `W` misses the central Gamma line, in which case every nonzero prime leg in
  `W` contributes a strictly negative jump weight; or
* `W` contains the central line, in which case compatibility with both Tate
  flags forces the quotient to contain the two quarter boundary directions,
  whose parabolic contribution is strictly larger than the degree carried by
  the omitted prime legs.

Equality would require one invariant line to contain simultaneously the two
Tate flags and all place residues.  Unique factorization and the
incommensurability of the Bohr spectra `(2 pi/log p) Z` forbid this unless the
subobject is the whole object.

This statement does not classify all invariant subobjects.  In the correctly
typed Hilbert quiver, every primitive analytic test generates a mixed
subobject, and its numerical weight is the row-(d) quadratic form.  Coordinate
place subobjects therefore do not suffice.

## 5. Non-circular proof programme

The construction succeeds only in this order:

1. write the star object, residues, determinant and parabolic degrees solely
   from the Gamma/Frobenius/Tate data;
2. prove the rank-one-place stability lemma by classifying invariant
   subobjects;
3. minimize the explicit determinant-normalized energy and prove coercivity
   directly (no appeal to row (d), no square root of `A_T`);
4. derive the Dirac--Higgs Green formula and compare its boundary terms with
   the already fixed equation (5.3).

The comparison is last.  No metric parameter may be selected by matching
`B_nuc`.

## 6. Kill conditions

The candidate dies without repair if any of the following occurs:

1. a proper invariant subobject has nonnegative parabolic slope;
2. the harmonic energy is noncoercive after determinant normalization;
3. the Green boundary term differs from (5.3) by any finite or Maslov
   remainder;
4. the shifted rank-two Euler pair remains stable in the same construction.

The fourth test is structural: the shifted pair should split into two
competing invariant subobjects and fail strict stability.  Davenport--Heilbronn
has no rank-one place-residue decomposition and therefore does not define the
input object.  Dedekind zeta does define it place by place; success would, as
it should, extend to GRH for number fields.

## 7. Exact next proof

Do not begin with a PDE existence theorem.  First compute the parabolic degree
of an arbitrary invariant subobject and prove the rank-one-place stability
lemma.  This is finite algebra plus the Bohr-frequency separation already
proved in the phase.  If stability fails, it produces an explicit invariant
subobject and kills the route before any analytic investment.  If it holds,
the real moment equation becomes the first genuinely new global sign
mechanism in the programme.
