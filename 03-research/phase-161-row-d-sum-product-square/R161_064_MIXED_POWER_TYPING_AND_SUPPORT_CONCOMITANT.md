# R161_064 — Correctly typed mixed power and the support concomitant

## 1. Correction forced by the collar theorem

The crossed Tate current of R161_009 is not the Tate projection of `Z_Nf`.  It is the Tate projection of the
adjoint pullback of the source-dependent product port:

    y_N=Z_N* g_N,          Tau_T P_T y_N=j_N.                 (1.1)

Thus any boundary-power identity containing the proved collar must be polarized between the first-contact source
`f` and `y_N`; a diagonal identity in `f` has the wrong type.  With

    A f=r+ell,       r=Tau_TP_TAf,       ell=(I-P_T)Af,        (1.2)

radicality gives exactly

    Re<Af,y_N>=Re<r,j_N>+Re<ell,(I-P_T)y_N>.                  (1.3)

Adding the exterior functional-equation defect `d=w-Af` reconstructs

    Re<y_N,w>
      =Re<r,j_N>+Re<ell,(I-P_T)y_N>+Re<d,y_N>.                (1.4)

This is R161_022--R161_023.  Hence changing the alternating Green form to its Hermitian polarization fixes the
diagonal obstruction but, after correct typing, does not yet create a vanishing.

## 2. A canonical finite ordering defect

Let `P=P_T`, `Q=I-P`, and let `S` be any finite causal synthesis.  For vectors `g,w` on the common core define

    K_P(S;g,w)
      :=<Pg,PSw>-<PS*g,Pw>.                                  (2.1)

Since `P=P*`, direct insertion of `I=P+Q` yields

    boxed:
    K_P(S;g,w)
      =<Pg,PSQw>-<Qg,SPw>.                                   (2.2)

Equivalently, in commutator notation,

    K_P(S;g,w)=<g,PSQw>-<Qg,SPw>,                             (2.3)

after the harmless outer projections are restored.  Formula (2.2) is the exact support concomitant: it consists
only of the two off-diagonal causal blocks and vanishes if the physical projection is removed.

Ordinary adjointness gives

    <g,Sw>=<S*g,w>,                                          (2.4)

so no full-space ordering defect exists.  Any new reciprocity capable of closing D must therefore be a statement
about (2.2), not about (2.4).

## 3. Tate-placement audit

Refine `P=Pi+Tau`.  The second term of (2.2) splits as

    <Qg,S Pi w>+<Qg,S Tau w>,                                (3.1)

and the corresponding refinement of the first term has the reflected two blocks.  This decomposition alone does
**not** identify either `Tau` term with the collar `j=Tau PZ* g`; in (3.1), `Tau` acts on `w` before synthesis,
whereas the proved collar has `Tau` after the adjoint synthesis.  Moving `Tau` through `S` creates another finite
support commutator.

The desired interpretation would be:

- the `Pi` pairing is the admissible radical test;
- the `Tau` pairing is the crossed collar `Re<v,j>`;
- the remaining `Q` pairing is the true exterior reciprocity.

but it has to be established by the literal `(PC-ren)` expansion; it is not a consequence of the projection
algebra.  Thus the Tate placement, not only the exterior sign, remains part of (4.2).

## 4. Exact finite target

For `S=Z_N=S_N^ren`, take the separated product port `g_N(f)` and the corrected functional-equation vector
`w_N(f)`.  Define the real support power

    C_(M,N,T)(f):=Re K_(P_T)(Z_N;g_N,w_N).                    (4.1)

The identity that would close D now has a unique noncircular form:

    boxed:
    C_(M,N,T)(f)
      =epsilon Re<v_f,j_(M,N,T)(f)>
       +D_(M,N,T)^Gamma(f)
       +1/2 ||P_R^ext C_log g_(M,N,T)+epsilon g_(M,N,T)||^2
       +o_(M,N)(1),                                         (4.2)

while the two oriented finite `(PC-ren)` equations must prove

    C_(M,N,T)(f)=o_(M,N)(1)                                (4.3)

on a first-contact radical.  R161_032 converts the first term of (4.2) to `||r||^2`; the Gamma term is
nonnegative by the already proved pole/collar construction.  Equations (4.2)--(4.3) would therefore force the
compressed scattering square to vanish.

The acceptance criterion is strict: (4.2) must be obtained by expanding the two off-diagonal blocks in (2.2)
with `E_N` in the history slot and the covariant derivative of `C_N` in the current slot.  If the expansion instead
recombines to `<g_N,Z_Nw_N>`, it is the tautology of R161_023 and fails the criterion.

## 5. What is proved and what remains

The exact new reduction is (2.2): it supplies a finite support-commutator candidate.  The equality (4.2) and its first-contact
annihilation (4.3) have not yet been derived from `(PC-ren)`; writing them as definitions would be circular.

- correct mixed typing of the Tate collar: **proved**;
- exact support concomitant (2.2): **proved**;
- identification of its finite-rank block with the crossed collar: **open**;
- positive expansion (4.2): **open**;
- first-contact annihilation (4.3) from the two finite PC orientations: **open**;
- row D: **open**.
