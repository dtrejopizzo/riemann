# E101.056 - Radical dual-test completion

The abstract completion principle below is a coordinate for the directional
tail continuity already isolated in E80.008 and E82.004.  It is not, by
itself, a new theorem.  Sections 3--5 and 8--9 include the corrections forced
by the subsequent non-duplication audit.

## 1. Operator setting

Let `X` be a source space, `Y` a test space, and

```text
Q_B:X->Y^*                                             (1.1)
```

the bilinear Weil operator associated with a build `B`.  Let `C_N` be a
finite coefficient space and choose extraction and synthesis maps

```text
P_N:X->C_N,
J_N:C_N->X,
P_NJ_N=I,
Pi_N=J_NP_N.                                        (1.2)
```

Let `R_N:Y^*->Y_N^*` be the finite row restriction.  The finite rectangular
block is

```text
M_(B,N)=R_N Q_B J_N.                                  (1.3)
```

For a safe observation point `z`, let `p_(B,N,z)` be the dual row of
E101.046, so

```text
p_(B,N,z)M_(B,N)=q_(B,N,z).                          (1.4)
```

Lift the row to a finite test functional

```text
phi_(B,N,z)=R_N^*p_(B,N,z) in Y.                     (1.5)
```

Let `k=E(h)` be the fixed Riemann kernel.  Its transform is the completed
Riemann function.  The arithmetic build `Z` satisfies the unconditional
radical identity

```text
Q_Z(k,phi)=0                                         (1.6)
```

for every admissible test `phi`.

## 2. Exact finite radical-transfer identity

### Theorem 2.1

For every build `B`, cutoff `N`, and safe `z`,

```text
q_(B,N,z)P_Nk
=Q_B(k,phi_(B,N,z))
 -Q_B((I-Pi_N)k,phi_(B,N,z)).                        (2.1)
```

### Proof

Equations (1.2)--(1.4) give

```text
q_(B,N,z)P_Nk
=p_(B,N,z)R_NQ_BJ_NP_Nk
=Q_B(Pi_Nk,phi_(B,N,z)).                             (2.2)
```

Now use `Pi_Nk=k-(I-Pi_N)k` and bilinearity. `QED`

For the arithmetic build, equation (1.6) reduces (2.1) to

```text
q_(Z,N,z)P_Nk
=-Q_Z((I-Pi_N)k,phi_(Z,N,z)).                        (2.3)
```

This is the exact source of the desired small quantity.  It is not a sign
estimate and does not use a zero location.

If

```text
alpha_N=ell P_Nk!=0,
k_N=P_Nk/alpha_N,                                    (2.4)
```

then E101.046 gives the normalized boundary identity

```text
B_y(z)-c_zk_N
=Q_Z((I-Pi_N)k,phi_(Z,N,z))/alpha_N.                (2.5)
```

Thus the synthesis projection `Pi_N`, the coefficient extraction `P_N` and
the normalization `alpha_N` cannot be merged into one symbol.

## 3. Why the controlled build separates

Let `P` be obtained by adding one off-line quartet to the divisor while the
kernel `k` is kept fixed.  In the spectral representation,

```text
Q_P(k,phi)
=Q_Z(k,phi)
 +sum_(rho in quartet) K(rho)Phi_phi(rho),            (3.1)
```

where `K` is the transform of `k`.  Since `K=Xi` for the original arithmetic
kernel,

```text
Q_P(k,phi)
=sum_(rho in quartet)Xi(rho)Phi_phi(rho).             (3.2)
```

The inserted points are not zeros of the original `Xi`, so this expression is
not identically zero on the whole admissible test space.  If the lifted dual
tests have a limit `phi_z`, then

```text
lim_N q_(P,N,z)P_Nk
=sum_(rho in quartet)Xi(rho)Phi_(phi_z)(rho)          (3.3)
```

provided the tail term in (2.1) tends to zero.  Nothing here proves that the
particular limiting test avoids the kernel of the quartet functional.  The
nonvanishing of (3.3) for the actual limit is a separate discriminating
statement and may contain the full remaining difficulty.

Thus the same completion theorem may be build-neutral while its consequence
is discriminating because the radical identity is true for `Z` and false for
`P`.

## 4. The completion topology must be fixed in advance

It would be circular to define a seminorm by

```text
||phi||=|Q_Z((I-Pi_N)k,phi)|.                         (4.1)
```

Smallness in that seminorm is exactly the desired scalar conclusion.  The
test topology must instead be defined independently of the single source
`k`.

Let `S_rad` be a source class containing

```text
the prolate differences E(h_lambda-h);
the Gamma-prime endpoint sources;
the complete signed Fourier collars;
one safe derivative of each source.                  (4.2)
```

Equip `S_rad` with a norm assembled only from independently stated source
quantities:

```text
physical right-endpoint weighted moments;
zero-mass bounded variation at the left endpoint;
bilateral signed coefficient norms of the complete Fourier collar;
one fixed source derivative.                         (4.3)
```

The first two components are the quantities of E101.053.  The external
functions `U_z,V_z` of E101.051 depend on the dual row, the cutoff and the
build; they cannot occur in a fixed source norm.  They are coordinates of a
functional in the dual space, not coordinates of the source itself.

Let `T_rad=S_rad^*` be the dual test topology.  Its definition is independent
of the arithmetic divisor and of the particular finite boundary vector.

## 5. Radical-dual-completion theorem

The proposed theorem is the following.

```text
RADICAL-DUAL-COMPLETION:

For one nonempty compact safe interval K, the lifted rows
phi_(B,N,z)=R_N^*p_(B,N,z)
form a locally bounded family in T_rad, with one z derivative.

||(I-Pi_N)k||_(S_rad)->0,
where k is represented by the complete signed prolate, Gamma-prime and
Fourier recombination used in the radical identity.                       (5.1)
```

The source in (5.1) is not split into a positive interior and a small tail.
Its prolate, Gamma-prime and Fourier-collar components are taken in the
single signed norm (4.3).  Uniqueness of a weak limit is not needed for the
tail estimate and is not included in the completion hypothesis.

### Theorem 5.1

Assume RADICAL-DUAL-COMPLETION and the unconditional radical identity (1.5).
Then the complete paired radical residual in E101.045 tends to zero locally
uniformly on `K` with one safe derivative.  Hence DIRECTIONAL-IDENT follows.

### Proof

Weak boundedness in `T_rad` and strong convergence of the recombined source
tail in `S_rad` give

```text
Q_Z((I-Pi_N)k,phi_(Z,N,z))->0                        (5.2)
```

locally uniformly with one derivative.  Apply the exact identity (2.1) to
the complete recombined representation of `k` before separating any
magnitude.  The full-source term is exactly
`Q_Z(k,phi_(Z,N,z))` and vanishes by (1.5).  What remains is (5.2).  E101.045
identifies this scalar with the normalized boundary-to-model error, proving
DIRECTIONAL-IDENT. `QED`

The proof is one-way.  It uses compactness on a source class, not convergence
of one preselected scalar.

## 6. Relation to the previous radical-tail cut

The earlier cut was

```text
RT-0  prolate in-band;
RT-1  represented Gamma-prime source;
RT-2  Fourier collar;
RT-3  shifted leakage and matched current.           (6.1)
```

This cut is useful for exact formulas but dangerous for estimates: each
piece can be large while their sum is small.  RADICAL-DUAL-COMPLETION changes
the order of work:

```text
first define one source norm for the recombined object;
then prove dual weak compactness;
only afterward use RT-0--RT-3 to verify the norm.     (6.2)
```

The target is no longer four separate vanishing statements.

## 7. Finite realization through displacement

E101.051 gives, for an external column with mesh point `d`,

```text
p_zm(d)=-a[U_z(d)-s(d)V_z(d)].                       (7.1)
```

Thus every external action of the lifted test is encoded by two rational
functions.  Define their exterior Hardy generating pair by

```text
H_(N,z)^U(w)=sum_(j>=1)U_z(d_(N+j))w^j,
H_(N,z)^V(w)=sum_(j>=1)V_z(d_(N+j))w^j,              (7.2)
```

together with the reflected negative-frequency pair.  The signed collar
pairing is the coefficient pairing of (7.2) with the corresponding source
generating functions.

The first concrete suggestion was

```text
HARDY-DUAL-BOUND:
  H_(N,z)^U and H_(N,z)^V are locally bounded in H^infinity
  after the matched-current normalization, while the recombined source
  collars tend to zero in H^1.                       (7.3)
```

E101.057 proves that (7.3) is false in general: the first dual moments create
logarithmic boundary singularities.  Exact moment subtraction, `H2` pairing
and radial `H1` duality remain possible finite coordinates.  None is promoted
before comparison with E72.316, E72.391 and the earlier scalar WRL.

## 8. Corrected novelty-gate audit

```text
N1  finite before the cofinal limit:                          pass;
N2  finite CCM plus absolute Euler--Gamma inputs:             pass;
N3  actual limiting test detects the controlled radical
    defect:                                                   open;
N4  no positivity, zero location, endpoint inverse, or
    absolute cell ceiling:                                    pass;
N5  source-space compactness implies the scalar one way, but
    the abstract obligation duplicates directional tail
    continuity:                                               fail as novelty. (8.1)
```

The radical identity supplies a valid arithmetic distinction, but (3.3) is
not forced merely because the quartet functional is nonzero somewhere on the
test space.  Moreover the abstract bounded-functional argument is the theorem
schema of E80.008.  New content can only be a specific finite estimate for
the actual dual rows and the complete recombined source.

## 9. Precise next questions

```text
RDC-1  choose a source topology independent of N,z,p_z and the build;

RDC-2  derive an exact finite dual formula on the complete exterior current,
       without splitting collar and far regions;

RDC-3  prove the resulting normalized dual bound and source-tail convergence
       with the exponential scales from E72.316 made explicit;

RDC-4  prove, rather than infer by genericity, the response of the actual
       limiting test to the inserted quartet.             (9.1)
```

The first three are a specific realization of the old directional-continuity
obligation unless they introduce a new finite cancellation.  `RDC-4` is the
only explicitly build-discriminating clause and remains open.

## 10. Status

```text
proved:
  exact finite radical-transfer identity;
  explicit model-separation formula for an inserted quartet;
  RADICAL-DUAL-COMPLETION implies DIRECTIONAL-IDENT;

rejected:
  a source-dependent seminorm that merely names the paired residual;
  separate absolute estimates on RT-0--RT-3;

open:
  RADICAL-DUAL-COMPLETION;
  a non-duplicating finite completion estimate;
  RDC-1--RDC-4;
  MATCHED-CURRENT-IDENT and Omega7.
```
