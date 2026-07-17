# Phase 74 - Hilbert eigenline cancellation

**Opened:** 2026-07-16.

## Entry point

Phase 73 reduced the entire transformed compact branch of the Omega7 route to a single finite scalar
and expressed it, at E73.305, as an exact **Hilbert product rule**. Let

```text
d_j   = 2 pi n_j / L                         (mesh frequencies)
r_j   = q_a(j)                               (Cauchy row, off-line node a)
eta   = R_w xi_L = (I-P_w) xi_L              (projected eigenline of C_E xi = mu xi)
U^even_j = W^even_j - V^even_j / L
W^odd_j  = W(d_j) - W(-d_j)
A_{jb}   = 1/(2 i pi (n_b - n_j)),  A_{jj}=0  (skew mesh Hilbert matrix, A^T = -A)
```

The terminal identity to prove is:

```text
HPR-DIV:
  sum_j eta_j r_j U^even_j
+ sum_j W^odd_j r_j (A eta)_j
+ sum_j W^odd_j eta_j (A r)_j
= O_M(L^(-M))    for every M.
```

This is the last open object of the whole route. Everything upstream is closed or proved-equivalent:

```text
closed before entering this phase
---------------------------------
SFREQ / D2BV-K at natural height                       [E72.388-389]
finite Fourier tail absorbed into the nodal system     [E72.390-392]
outside high zero tail above T_L = e^L L^A             [E72.394]
maximal Cauchy block invertibility (incl. multiplicity)[E72.324-325]
critical-line polynomial control CRIT-POLY             [E72.327]
left coefficient Lambda_L = mu + e_pole - 2 kappa_*    [E72.328,330]
Cauchy-Schur projection formulation (NAT-PROJ)         [E72.396]
two-symbol Loewner normal form (TS-DIV)                [E73.293]
cell reconstruction from two symbols                   [E73.294]
final finite adjugate identity (FINAL-ETA-ADJ)         [E73.295]
closed spectral distribution (T^diag + T^off)          [E73.304]
Hilbert product rule (HPR)                             [E73.305]
```

and the equivalences

```text
HPR-DIV  <=>  closed spectral distribution  <=>  K-DIAGOFF  <=>  TS-DIV  <=>  FINAL-ETA-ADJ
```

are all proved and verified to roundoff (companion probes in Phase 73). If `HPR-DIV` holds, E72.396
gives off-line nodal suppression, E72.326 propagates it to `PW-Cauchy`, and the compact route
continues `SQB => CB => RNS => MC-NZ => NZ-MSD => scalar WRL => Omega7`. Since Omega7 is the Li-Keiper
statement `lambda_n >= 0`, which is equivalent to RH, `HPR-DIV` is the single remaining load-bearing
inequality of the program.

## Why a new phase (personal note - David)

> **Personal note.** From here on, whenever a phase reaches roughly 100-150 documents, or whenever
> something genuinely warrants starting fresh, we open a new phase. Reading 300 documents inside a
> single phase is too much and one loses focus -- that was the lesson of Phases 72 (396 entries) and
> 73 (305 entries). Even though it feels like we are in the last phase(s), close to a complete proof,
> the rule still applies: Phase 74 caps at about E74.150 and continues as Phase 75 if needed.

## Phase 74 objective

Prove the signed three-way cancellation `HPR-DIV` **analytically**, using only:

1. the pole-even CCM eigenline equation `C_E xi = mu xi`;
2. the mesh / Fourier structure of the skew Hilbert matrix `A`;
3. the explicit closed Gamma-prime symbols `W, V, U`;

with **no zero-location input** and respecting the non-circularity kill-tests below.

## The load-bearing idea of this phase

The two-symbol form of E73.293,

```text
TS-DIV:  q [ M_{W^even} - (1/(iL)) Lambda_{W^odd}^{full} ] eta = O_M(L^(-M)),
```

and the product-rule form `HPR-DIV` are **the same operator**. Writing `M_F = diag(F)` and using
`A^T = -A`, the two Hilbert-divergence terms consolidate exactly:

```text
  sum_j W^odd_j r_j (A eta)_j + sum_j W^odd_j eta_j (A r)_j
= r^T M_{W^odd} A eta - r^T A M_{W^odd} eta
= r^T [ M_{W^odd}, A ] eta,
```

and the commutator is the Loewner divided-difference matrix

```text
[ M_{W^odd}, A ]_{jb} = (W^odd_j - W^odd_b) / (2 i pi (n_b - n_j)) = DD_{W^odd}(j,b),
```

whose off-diagonal equals `-(1/(iL)) Lambda_{W^odd}^{full}` off-diagonal and whose diagonal is zero.
Together with the diagonal mass term `r^T M_{U^even} eta`, and using `U^even = W^even - (1/(iL))F'`
(E73.293 eq. 4), the consolidated operator has diagonal `U^even` and off-diagonal `DD_{W^odd}` --
**identical to the TS-DIV operator**. Hence:

```text
E74.1 (bridge identity, to be re-derived and re-verified in-phase):
  HPR-DIV total = r^T ( M_{U^even} + DD_{W^odd} ) eta = TS-DIV.
```

This is not new mathematics -- it is the exact bridge between E73.293 and E73.305. **Its value is that
it re-exposes the Hilbert matrix `A` that the two-symbol form had absorbed.** The two-symbol form is a
dead end for a norm/row estimate (E73.293 §5: the center is a signed coupling, not a single-symbol
estimate). But `A` is a *Hilbert transform on the mesh*, and Hilbert transforms have a decisive
analytic property that a raw Loewner matrix hides: **Cauchy kernels are quasi-eigenvectors of the
Hilbert transform.** That is the lever Phase 74 opens.

### Lever A -- corrected finite-mesh Hilbert action

The continuous Hilbert transform of a one-sided Cauchy kernel `1/(x - a)` with `Im a != 0` is
`(-/+) i/(x - a)` (sign set by the half-plane of `a`). The Cauchy row `r_j = q_a(j)` is the mesh
sample of such a kernel, but E74.1-E74.3 show that the naive finite analogue

```text
A r_a = c_a r_a + small
```

is false.  The actual finite identity is stronger and more precise:

```text
A r_beta = H_beta r_beta,
H_beta(n)= -i/(2 pi) sum_{m != n}[1/(m-n)-1/(m-beta)].
```

Thus the Cauchy line is invariant under `A` only after allowing multiplication by the explicit
finite harmonic symbol `H_beta`.  The corrected normal form is

```text
HPR =
<r_beta, M_U eta> + <r_beta, M_W (A+M_{H_beta}) eta>.       (HS-NF)
```

This is now the live Phase 74 object.  Any proof must derive the smallness of this signed pairing
from the pole-even eigenline equation; it cannot use a constant Hilbert eigenvalue.

### Lever B -- second-order Hilbert / Tricomi calculus (fallback)

If the first-order collapse leaves a stubborn remainder, use the discrete Tricomi / Cotlar identity
`A^2 = -1/4 + K_smooth` and the commutator hierarchy `[A, [A, M_W]] ~ M_{W''}`-smoothing to rewrite

```text
DD_{W^odd} = [M_{W^odd}, A] = A M_{W^odd} A + (smoothing) + (endpoint rank-one),
```

pairing `(A r)` with `(A eta)`. Combined with Lever A this puts the Cauchy collapse on *both* factors
and moves the whole estimate onto the eigenline-controlled quantities `A eta` and `A r`.

## Milestone ladder

Each milestone is one `E74.x` document plus a companion probe, in the Phase 72/73 style
(state -> exact identity -> numerical certification -> status). Probes reuse the existing harness
exactly as `E73_305_hilbert_product_rule_probe.py` does:
`E71_9_relative_arch_background_probe.build` (builds `H_L`),
`E73_223_coefficient_ball_budget.cauchy_rows` / `.projector` (Cauchy row `r` and projector `P_w`),
`E73_224_weight_amplification_budget.weight` (the `W` / `V` weights), and
`E72_396_cauchy_projection_probe.GAMMAS` (the critical-line node set).

```text
E74.1  Bridge identity.  HPR-DIV = r^T (M_{U^even} + DD_{W^odd}) eta = TS-DIV, via A^T=-A.
       Re-verify to roundoff against the E73.305 probe.  Pure algebra; exposes A.

E74.2  Corrected Cauchy Hilbert action.  Compute A r_beta in closed form on the mesh n_j and prove
       A r_beta=H_beta r_beta with H_beta explicit.  This replaces the false constant-eigenvalue
       heuristic.

E74.3  Harmonic-symbol normal form.  Rewrite HPR-DIV as
         <r_beta, M_U eta> + <r_beta, M_W(A+M_{H_beta})eta>.
       Probe verifies this is exactly HPR.  The "one-sided symbol collapse" is rejected.

E74.4  Eigenline kill of the harmonic-symbol expression.  Feed C_E xi = mu xi in the transformed form
         (mu + e_pole) G_x = T_W02[xi] - T_WR[xi] - T_Prime[xi]   (E72.317)
       to show eta annihilates
         <r_beta, M_U eta> + <r_beta, M_W(A+M_{H_beta})eta>
       up to the already-closed CRIT-POLY nodal data G_x(i gamma) (E72.327).

E74.5  Schur branch formula.  Reduce the harmonic-symbol scalar to the exact
       two-dimensional identity
         QH(I-P)xi=(mu I-QHQ^*G^{-1})Qxi.
       This does not prove smallness; it exposes the branch object whose
       suppression must be derived without assuming Qxi is small.

E74.6  Branch no-go audit.  Compare E74.5 with E73.188/E73.240/E73.266/E73.296.
       Verdict: the branch identity is exact but already rejected as a forcer.
       Return to the allowed Directional Cell Eigenline Cancellation target.

E74.7  Cell divisibility probe.  Test whether Q_w eta=0 creates a finite
       Laplace/Cauchy divisibility factor in B(y)=qQ_yeta before applying F_L.

E74.5  Defect-vector budget.  Prove the rho_a-correction pairings are O(L^B e^(-Re a . L)) -- the
       same exponential-vs-polynomial budget as NAT-PROJ, but now for an EXPLICIT geometric vector
       instead of the opaque projection.  Most likely close-or-falsify point of the phase.

E74.6  Lever B fallback: Tricomi second-order form.  Prove the discrete Tricomi identity for
       DD_{W^odd} (= A M_{W^odd} A + smoothing + endpoint rank-one); combine with E74.2 so the
       Cauchy collapse acts on both A r and A eta.  Only if E74.3/E74.5 stall.

E74.7  Falsifiers.  Re-run every positive identity with (i) a random symbol replacing W (must NOT
       cancel) and (ii) the Davenport-Heilbronn / planted off-line-zero harness (cancellation MUST
       fail detectably).  Live-detector discipline inherited from E71.2.

E74.8  Non-circularity audit.  Audit the surviving mechanism against the kill-tests below.  Required
       before any closure claim.

E74.9  Assembly.  Restate HPR-DIV => NAT-PROJ => PW-Cauchy => ... => scalar WRL => Omega7 with the
       new input in place, marking exactly which quantifiers (uniformity in a, in the window W_L,
       in L) the proof supplies.

E74.18 (if closed) Certification pass.  Extend the E73.213-229 interval / ball arithmetic to the
       new identity for a certified finite window plus the asymptotic-regime statement.
```

## Non-circularity kill-tests (a proof MUST respect all)

From `E72_7_NONCIRCULAR_VARIATIONAL_GATE.md`, `E72_16_ZERO_FILTER_GATE.md`, and the
`E72.2 / E72.5` audits, plus the `NO-GO-LIST.md` master walls:

```text
K1  no inverse smuggling: do not build any primitive from C_x^{-1} b, Riesz projections of the
    unknown low island, or the endpoint resolvent.  Correctors come from k_lambda / pole shorting /
    prolate-Sonin calculus only.
K2  no local inverse smuggling: do not expand C_x^{-1} as a sum over prime-place inverses
    (Phase 65 additive-Green error).
K3  no absolute ceiling: do not bound sum_j |term_j| before cancellation (Phase 67 incoherent
    ceiling -> returns to the PNT ceiling).  HPR-DIV is a SIGNED cancellation by construction.
K4  no point-local kernel evaluated at a zeta zero (Phase 32).
K5  no endpoint identification from the scalar determinant alone (corrected D9 error, Phase 65).

ZERO-FILTER GATE (E72.16): any proof of the annihilation must NOT manufacture an analytic filter
    whose divisor contains the off-critical zeta divisor.  Admissible only if built from finite
    CCM / prolate data without using zero locations or Xi as input.  The only sanctioned mechanism
    is Option C: a finite-CCM symmetry forcing SIGNED cancellation among maximal-real-part zero
    resonances -- exactly the shape of HPR-DIV.

EIGENLINE DISCIPLINE: cannot assume k_x -> xi_x.  Smallness must be DERIVED from C_E xi = mu xi.

TAIL DISCIPLINE (E72.331): tails are controlled only AFTER applying the combined functional Lcal;
    a pointwise finite Fourier tail bound is false at polynomial cutoff.  Use signed/directional
    commutator forms, never absolute row sums.

MASTER WALLS (NO-GO-LIST): no reduction back to a positivity statement (MW-1 Weil positivity /
    MW-4 wrong-sign), no per-prime or local-to-global assembly (MW-2 arithmetic propagation /
    MW-3 Hasse-Minkowski).  CAND-1 / the CCM route was chosen precisely to sit OFF MW-1.
```

## Exit criteria

The phase ends when either

- **(a)** `HPR-DIV` is proved -- the Omega7 chain then fires end to end; or
- **(b)** a theorem-grade falsifier shows the Hilbert-eigenline mechanism cannot force the
  cancellation, with an autopsy naming the next finite object (the Phase 72/73 discipline).

## Documents

```text
E74.1-E74.3  Bridge identity and Lever A first audit.
             Result: bridge OK; constant quasi-eigenvector false.

E74.2        Closed finite-mesh Hilbert action on Cauchy rows.
             Result: A r_beta=H_beta r_beta, exact to roundoff.

E74.3        Harmonic-symbol normal form.
             Result: HPR=<r,M_U eta>+<r,M_W(A+H_beta)eta>, exact to roundoff.

E74.4        Harmonic row equals the CCM operator row.
             Result: K_HS=rH_L at row level, exact to roundoff.

E74.5        Exact 2x2 Schur branch formula.
             Result: HPR components are entries of
             (mu I-QHQ^*G^{-1})Qxi; smallness still open.

E74.6        Branch no-go and return to the cell target.
             Result: E74.5 duplicates the already rejected rank-two detector;
             the live object is F_L[y -> qQ_y(I-P)xi].

E74.7        Cell divisibility probe target.
             Result: simple raw divisibility is rejected; endpoints vanish but
             moments do not.  The Gamma-prime functional must be used coupled.

E74.8        Eigenline-specific cancellation.
             Result: generic ker(Q) vectors do not cancel; only eta=(I-P)xi_L
             cancels.  The next target is an explicit non-pseudoinverse
             coborder for qH_L(I-P).

E74.9        Harmonic left-coborder audit.
             Result: adding q_jH_beta_j and q_jA to the primitive module can
             improve row-norm fits, but it cannot by itself improve the scalar
             obstruction because every Y(H_L-mu_LI) term pairs to zero with
             xi_L.  Direct primitive-span enlargement is rejected as a closure
             mechanism.  The live target is now a named residual-slot theorem:
             rho=Y(H_L-mu_LI)+R with Rxi_L=O_M(L^-M).

E74.10       Residual-slot closure ledger.
             Result: states RSLOT-O7 and the exact implication chain
             RSLOT-O7 => HPR-DIV => NAT-PROJ => PW-Cauchy => scalar WRL
             => Omega7, with the non-circularity rules made explicit.

E74.11       Algebraic quotient bridge.
             Result: the direct raw-cauchy0 bridge is rejected
             (bridgeRel usually 0.8--1.1), but the APR residual is numerically
             close to the abstract cauchy0 quotient in trusted windows
             (small quotMiss).  The surviving object is a quotient-lift
             residual, not the raw cauchy0 coefficient vector.

E74.12       Named residual formula.
             Result: defines the quotient-lift residual slot QLIFT_L and the
             new target QLIFT-DIV; proof still requires an explicit
             partial-fraction basis for C_L cap M_L.

E74.13       Residual pairing estimate target.
             Result: isolates the remaining scalar theorem as a three-coordinate
             signed cauchy0 quotient estimate.  Current probes support
             eigenline specificity but do not prove the estimate.

E74.14       Certification and falsifiers.
             Result: random ker(Q) vectors and random symbols fail to cancel
             by L^16--L^20 relative to the zeta/eigenline scalar.  DH/planted
             controls remain pending in the current finite-cell harness.

E74.15       Conditional assembly.
             Result: records the conditional closure theorem and honest
             endpoint.  Phase 74 has not closed Omega7; it has reduced the
             live theorem to exact quotient basis + QLIFT-DIV.

E74.16       Arbitrary-precision audit of the directional scalar.
             Result: the scalar survives after the eigen-equation residual is
             reduced from double precision to roughly 1e-81; it is not solely
             an eigensolver artifact.

E74.17       Exact Schur-transfer identity and quotient no-go.
             Result: QH(I-P)xi = (mu I-QHQ*(QQ*)^-1)Qxi exactly.  The transfer
             is numerically polynomially conditioned, so HPR-DIV returns to
             CAUCHY-EIG-LOC rather than a quotient-lift theorem.  This entry
             supersedes the E74.15 proposed next move.

E74.18       Schur-transfer invariants and compression criterion.
             Result: T is similar to mu I-G^(-1/2)QHQ*G^(-1/2).  On resolved
             windows the compression spectrum is approximately L and T/L is
             approximately -I.  The proof obligation is the non-circular
             two-dimensional estimate CAUCHY-COMP plus Gram bounds.

E74.19       Truncation/compression audit.
             Result: stable compression begins when d_max exceeds the critical
             height.  The limiting coefficient couples an archimedean part
             near 0.15--0.28 with a prime part near 0.70--0.85.

E74.20       Exact Feshbach block equation.
             Result: ordinary gap perturbation gives only fixed-order
             localization.  The live all-orders mechanism is an iterated
             Cauchy/Gamma regularity bootstrap BOOT-CELL(r).

E74.21       Cauchy-jet bootstrap no-go.
             Result: only the first resolvent value is superpolynomially
             small; confluent jets of orders 2--5 are not.  The cancellation
             is nodal and CAUCHY-EIG-LOC reduces to the finite numerator
             divisor theorem CRIT-NUM-DIV / CCM-CRIT-INTERP.

E74.22       Critical root-transport identity and probe.
             Result: CAUCHY-EIG-LOC is equivalent, under polynomial derivative
             separation, to superpolynomial locking of finite Weyl roots onto
             the critical zeta divisor.

E74.23       Planted off-line nodal falsifier.
             Result: zeta locks at roundoff, while the planted control gives
             normalized Cauchy values 1e-2--1e-1 and visible root shifts.

E74.24       Endpoint autopsy.
             Result: names CCM-ROOT-LOCK / a quantitative stable-divisor
             theorem as the irreducible live endpoint and records the rejected
             quotient, regularity, and generic-gap routes.

E74.25       Euler/Gamma error-formula audit.
             Result: the exact transformed formula exists, but its admissible
             signed remainder is precisely TPW/scalar WRL.  No independent
             superpolynomial error estimate is obtained; the irreducible
             finite object is EG_LOCK_L(gamma).

E74.26       Davenport--Heilbronn nodal falsifier.
             Result: on resolved meshes the off-line node remains near 0.20
             and the ground floor is negative; the failure is stable under
             quadrature and mesh refinement.

E74.27       Final research ledger.
             Result: Omega7 remains open.  The post-E74.17 program ends in a
             theorem-grade autopsy naming EG_LOCK / CCM-ROOT-LOCK as the
             irreducible missing arithmetic identity.
```
