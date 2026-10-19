# Alpöge–Furman–Connes audit for row (d)

Status: strategic audit, not a theorem and not evidence for row (d).

## 1. What the Alpöge–Furman result actually changes

The paper compresses the Weil Hermitian form to a critically sampled
time–frequency system. On the zero side, an on-line distinct zero contributes
a positive rank-one block, while an off-line pair contributes a Hermitian
block of signature `(1,1)`. On the prime side, the argument evaluates the
trace and Hilbert–Schmidt norm unconditionally. A rank–trace inequality then
gives at least `2/3` simple zeros on the line and `5/6` distinct zeros; the
Montgomery–Taylor window raises these to about `0.6725` and `0.83625`.

This is not a positivity proof and it does not weaken the logical force of
Weil positivity. It is a sharp use of the *indefinite* form. The paper's own
optimization shows that trace plus Hilbert–Schmidt information at bandwidth
one has a ceiling near `0.682`. The transcript also explains why the
unconditional higher moments are unavailable in the support range needed by
the same architecture.

Consequences for phase 120:

- reproducing a trace/HS inequality is not new geometric input;
- its Gabor compression is an excellent finite falsifier for P3;
- a partial P3 estimate should yield an additional inequality on the
  Lorentzian off-line blocks and could first improve `0.6725`;
- exact P3 must eliminate every negative block, not merely improve its
  density.

The claim that Alpöge–Furman simply "decided not to pursue positivity" is too
coarse. Their campaign tested several positivity constructions, found them
equivalent or underdetermined, and the successful published branch instead
used inertia. That history is useful as a catalogue of circularity modes,
not as a no-go theorem against an independently constructed Hodge object.

## 2. The logical point about positivity

Global Weil positivity on the full test class is equivalent to RH. Therefore
we should not say that this analytic positivity is weaker than RH. The viable
claim is different: a geometric theorem may prove the positivity without
assuming it. This is exactly the role of Hodge index/Rosati positivity in
Weil's proof over finite fields.

The operational distinction is:

    circular: define the norm from the negative part of B_nuc;
    geometric: construct the norm and its Gram matrix first, then prove that
               its intersection pairing equals -B_nuc on degree zero.

For every concrete finite-support `f`, the first computation must be possible
without inspecting `B_nuc(f,f)` and without fitting a scalar to it.

## 3. What arXiv:2606.06604 actually supplies

Connes–Consani construct an absolute `F_1`-arithmetic curve with stalk

    F_1[T^{Z[1/p]_+}]

at `p`, perfected under the `p`-Frobenius. Locality selects the relevant
place. Over the complex numbers the nontrivial local points are torsors under
`W_p=Q_p^x` and `W_infty=C^x`. The archimedean quotient is

    E_p = C^x / p^Z = C_p x S^1,

where the real periodic orbit `C_p` has length `log p`, while the phase circle
is independent of `p`. The outlook also maps logarithmic Gauss-valuation
profiles to convex piecewise-affine sections on the scaling site.

This supplies credible raw material for:

- place labels that are not collapsed by their norms;
- local Frobenius/Witt towers;
- a real structure and hence a possible dagger;
- a common archimedean carrier through which distinct places can interact;
- tropical section data which might support an independently positive
  reference metric.

It does **not** yet supply an intersection product, a positive Rosati trace,
a quadratic Riemann–Roch theorem, or the Hodge inequality required for row
(d). We must not cite it as if it did.

## 4. Concrete Connes gate

For each active place `p`, let the local contact line come from the perfected
stalk and let its real orbit have period `log p`. Use the common phase circle
of the `E_p` to form a fibered or correspondence product between different
places. Complex conjugation supplies the first dagger candidate. Push the
resulting metric/determinant pairing to the common phase circle and compute
its Fourier multiplier.

The candidate survives only if all of the following occur without a fitted
parameter:

1. the diagonal local block is exactly `log p * 1 1^t`;
2. the cross-place block is nonzero and functorial under Frobenius iteration;
3. after half-density normalization and removal of the two Tate directions,
   its multiplier is exactly

       log pi - Re psi(1/4 + i tau/2);

4. the resulting primitive norm is an explicit positive Gram before it is
   compared with the nuclear Lefschetz form.

The quarter shift in the digamma spectrum is especially diagnostic. It must
come canonically from the real structure, half-density and Tate directions;
choosing it to match the Gamma factor would be circular.

## 5. Gates and milestones

### Gate 0 — invariant indexing

Rebuild the finite package on `(place, iterate)` labels. Curves, zeta and
Dedekind zeta then have rank one per place; the shifted pair has rank two; DH
has no compatible positive place package.

### Gate 1 — calibration at `{2,3}`

At `T=log 2`, only contacts `2` and `3` are active. Positivity is already
certified, so this gate tests provenance and normalization only. Compute the
Connes-derived Gram first, then compare it with the forced Gamma matrix and
the certified margins.

### Gate 2 — first discovery at `{2,3,4}`

At `T=(1/2)log 5`, contacts `2,3,4` are active and paper 42 explicitly leaves
the endpoint open. The repeated iterate `4=2^2` tests coherence inside one
place simultaneously with cross-place mixing. An exact independently derived
Hodge identity here would be a new result.

### Gate 3 — quantitative bridge beyond two thirds

Compress the candidate norm in the Alpöge–Furman Gabor system. Isolate the extra
matrix inequality contributed by P3 beyond trace and HS norm. If approximate,
translate its defect into an explicit proportion bound; if exact, prove the
absence of Lorentzian off-line blocks in that compression.

### Gate 4 — cofinal theorem

Prove compatibility, closability, density and convergence as finite
place-iterate sets exhaust all contacts. No collection of finite gates,
including Gate 2, replaces this step.

## 6. Present best hypothesis

The most plausible missing object is not the direct sum of local `Tor_1`
lines. It is a metrized correspondence obtained by gluing the perfected local
Frobenius torsors through their common archimedean phase, with the Green term
appearing as the determinant anomaly of that gluing. Local rank one supplies
the Euler contact; the shared phase supplies cross-prime mixing; real
structure supplies the dagger; the determinant anomaly must supply the Gamma
kernel.

This hypothesis is strong but falsifiable at Gate 1. Its first calculation is
the Fourier multiplier of the common-phase determinant, not a positivity
inequality.
