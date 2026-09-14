# P3 formal specification and theorem-by-theorem audit

Status: construction specification. Clauses marked **proved** refer to paper
42; clauses marked **missing** are not to be promoted to hypotheses silently.

## 1. Why P3 must be layered

The rank-one contact lines are shared by zeta, function-field curves and
Dedekind zeta functions. They are necessary provenance but cannot themselves
imply positivity. Accordingly P3 is separated into:

- `P3_loc`: invariant local contact and self-dual metric data;
- `P3_dag`: both orientations in a dagger category;
- `P3_glue`: a canonical archimedean attachment of all local lines;
- `P3_pol`: a positive trace and a unitary dilation making the primitive
  attachment a compression.

The desired Hodge identity is a theorem to be proved from these data, not an
axiom of P3.

## 2. P3_loc — invariant local skeleton

Let `V_f` be the set of finite places. For every `v in V_f` and `j>=1`, P3
contains an object `Gamma_(v,j)` and a perfect contact complex `L_(v,j)`.
It must satisfy:

1. **Place resolution.** The label is `(v,j)` and is not replaced by the
   integer `N(v)^j`.
2. **Frobenius coherence.** Within a place,

       Gamma_(v,i) o Gamma_(v,j) = Gamma_(v,i+j).

   Products involving different places retain both labels.
3. **Derived provenance.** `L_(v,j)` is obtained by derived contact with the
   unit section, not appended to prescribe a coefficient.
4. **Rank-one determinant block.** With `ell_v=log N(v)`, the reduced local
   pairing is

       K_v(i,j) = ell_v * 1_i * 1_j.

5. **Central metric.** The positive self-dual character is

       w_(v,j) = N(v)^(-j/2),

   so the normalized iterate coefficient is
   `ell_v N(v)^(-j/2)`.
6. **Indecomposability.** One geometric place gives one contact line. A direct
   sum of two characters at the same place has local rank two and fails this
   clause.

For `Spec Z`, `v=p` and `(v,j) <-> p^j`; thus the existing objects
`Gamma_(p^j)` give this package without changing their construction.

## 3. P3_dag — orientations and adjoints

P3 must enlarge the positive semigroup category to contain two orientations
`Gamma_(v,j)^+` and `Gamma_(v,j)^-`, with

    (Gamma_(v,j)^+)^dagger = Gamma_(v,j)^-,
    (ab)^dagger = b^dagger a^dagger.

The self-dual metric must make dagger isometric. On the analytic realization,
`Gamma_(p,j)^+` acts by dilation `U_(p^j)` and the opposite orientation is
the conjugate under `J h(x)=x^-1 h(x^-1)`.

This is stronger than merely writing both terms in the explicit formula. The
two must be objects and morphisms in one dagger category whose positive trace
is defined before the nuclear supertrace comparison.

## 4. P3_glue — the archimedean reservoir

Put `D=-i d/dt` on the logarithmic line and

    A = N + 1/4

on the Hardy space `H^2(S^1)`, where `N e_n=n e_n`, `n>=0`. Define the
Fourier-side operator

    (W_infty F)_n^(hat)(tau)
      = (tau/2) /
        sqrt((n+1/4)((n+1/4)^2+(tau/2)^2)) * F^(hat)(tau).

The digamma series gives the exact, unconditional Gram identity

    ||W_infty F||^2
      = (1/2pi) integral g_Gamma(tau)|F^(hat)(tau)|^2 dtau,

    g_Gamma(tau)
      = Re psi(1/4+i tau/2)-psi(1/4)
      = sum_(n>=0) (tau/2)^2 /
          ((n+1/4)((n+1/4)^2+(tau/2)^2)) >= 0.

Thus the positive Gamma reservoir already has an explicit square root which
does not use zeta zeros or the sign of `B_nuc`. Moreover

    log pi-psi(1/4) = log pi+gamma+pi/2+3log 2 = m_0,

so

    g_Gamma(tau)-m_0
      = Re psi(1/4+i tau/2)-log pi,

exactly the negative of the forced archimedean multiplier in paper 42.

The quarter-twisted Hardy module is now derived from the common phase circle,
without matching the Gamma factor:

- even real-place sector: division of the Mellin variable by `2`;
- unique central half-density: evaluation at `s=1/2`;
- hence the canonical offset `(1/2)/2=1/4` and monodromy `i`.

Indeed `|z|^s=(z conjugate(z))^(s/2)` and holomorphic polarization retains
`z^(s/2)`. At the self-dual character `s=1/2` this is `z^(1/4)`. The Hurwitz
determinant of the resulting positive Hardy spectrum gives both `m_0` and
the Gamma reservoir. This is Lemma `quartertwisteddeterminant` in paper 42.

The same geometry packages every place tower into

    C_p=p^(-1/2)V_(log p),
    O_p=sqrt(1-p^(-1))(I-C_p)^(-1),

with

    O_p^*O_p-I
      =sum_(j>=1)p^(-j/2)(V_(j log p)+V_(-j log p)).

All `C_n` have the simultaneous isometric dilation
`V_(log n) tensor S_(log n)` on the common half-density carrier, followed by
one bilateral unitary dilation. Thus P3_dag and the cross-place carrier are
now explicit. What is not yet proved is that the derived common-phase pushout
has only the two polar obstructions and satisfies the global Green identity.

## 5. P3_pol — the one genuinely new morphism

For a finite place-iterate set `S`, let `C_S` be the positive sum of its
rank-one contact lines together with the constant/Tate load. The
operator-valued pushout of phase 106 supplied a useful source template, but
the central-weight audit rejects its attachment. P3 requires a rebuilt
canonical attachment

    a_S : C_S -> H_Gamma

obtained by gluing the local Frobenius torsors through their common
archimedean phase. Its Gamma gradient must use the normalized positive-carrier
factor `sqrt(g_Gamma)`. For `q=p^j`, its Tate amplitude must be
`sqrt((log p)q^(-1/2)/c_p)`, not the phase-106 amplitude proportional to
`q^(-1/2)`. Its matrix is computed from the gluing before comparison with
`B_nuc`.

The non-circular target is a unitary dilation: construct positive Hilbert
objects `E_S,F_S`, a unitary `U_S:E_S->F_S`, and independently defined
orthogonal projections `P_S,Q_S` such that

    a_S = P_S U_S Q_S.

Then `a_S` is a contraction for categorical reasons. Its defect

    1-a_S a_S^dagger = W_S W_S^dagger

is automatically positive and is the candidate finite primitive norm. Only
afterwards may row (c) be used to identify that defect with
`D_out-y_N y_N^*` and hence with `-B_nuc` on the primitive subspace.

Requiring `||a_S||<=1` without constructing this dilation is just row (d) in
operator language and is rejected.

## 6. Audit of paper 42

| clause | status | evidence / exact gap |
|---|---|---|
| place-resolved labels on `Spec Z` | **proved after reindexing** | `p^j` uniquely recovers `(p,j)` |
| faithful Frobenius composition | **proved** | Thm. `rowbcompose` |
| derived cyclotomic contact | **proved** | `derivedWittContact`, Thm. `rowbcontact` |
| determinant degree `log p` | **proved** | `contactdegreeagain` |
| unique central character `p^(-j/2)` | **proved** | `Tatecharacter`, `centralLocalCoefficient` |
| nuclear realization and two trace orientations | **proved analytically** | `Rfunctor`, `Wfinplus`, `Wfinminus` |
| dagger/unitary realization of the central semigroup | **proved analytically** | Lemma `commonhalfdensitydilation`; one simultaneous bilateral dilation for all `C_n` |
| positive trace / Rosati form | **missing** | the constructed completed trace is a supertrace, not a positive trace |
| exact Gamma square root | **proved analytically here** | digamma series above |
| geometric derivation of the quarter twist | **proved at the phase/metric interface** | holomorphic polarization of the self-dual character gives `z^(1/4)`; Lemma `quartertwisteddeterminant` |
| positive phase-preserving finite pushout | **source template only** | corrected 106.198 has the right Gamma multiplier but the wrong central finite mass |
| compatible Hilbert direct limit | **proved for the rejected source pushouts** | 106.199; 106.205 proves this absolutely continuous completion cannot receive CCM resonances faithfully |
| place-coherent physical tower | **proved analytically** | Thm. `placepoissonfactorization`; one strict contraction per place generates all physical iterates |
| canonical cross-place carrier | **proved analytically** | common half-density dilation; distinct primes act in the same translation space |
| forced Green source | **proved analytically** | Lemma `GammaMarkovResolution` gives exactly the digamma Green on an exponential translation carrier |
| comparison of the complete cross-place attachment with forced Green | **missing** | the common carrier must still be wired through the D.247 four-port colligation; a shared ambient Hilbert space alone is not the comparison theorem |
| unitary dilation of the complete primitive attachment | **missing and decisive** | requires the derived pushout Green identity, not merely the local Sz.-Nagy dilations |

Therefore `P3_loc`, the physical place towers, their simultaneous dilation,
the quarter twist and the forced cross-place Green carrier are constructed.
The remaining finite theorem is sharply isolated: form their derived pushout
and prove that local acyclicity leaves exactly the two polar modes, so Green's
formula has no extra boundary/Maslov term. Only after this finite identity is
proved does the resonant nuclear/derived cofinal completion enter.

## 7. Counterexample audit

- **Function-field curve:** `P3_loc` holds. The analogue of `P3_pol` is
  supplied by polarized finite-dimensional `H^1`; this is the calibration
  model.
- **Dedekind zeta:** `P3_loc` holds and `P3_pol` is unknown; a successful
  invariant construction should yield GRH.
- **Shifted pair:** its local package is the direct sum of characters
  `N(v)^(+aj)` and `N(v)^(-aj)` and has rank two, so it fails
  indecomposability before positivity is considered.
- **Davenport–Heilbronn:** its logarithmic coefficients are not the
  determinant degrees of a positive place-indexed rank-one package.

## 8. Single remaining finite gate

Construct the derived pushout of the acyclic return cones over the common
quarter-twisted Hardy carrier. Prove algebraically that its adjoint cokernel
is exactly `span(e^(-t/2),e^(t/2))`, and prove the Green identity with no
Maslov/boundary remainder. The identities already established then turn this
directly into the `{2,3,4}` polarization theorem. No further Galerkin sweep
is part of the proof.
