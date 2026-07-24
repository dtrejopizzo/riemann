# E78.143 - Autopsy of the elementary-self-adjointness (deficiency-index) route to `SAFE-LIMIT-POINT`

**Run:** 2026-07-21.
**Scope:** LP-interface front, `BORDERED-WEYL-COMPLETENESS` / `SAFE-LIMIT-POINT`.
**Class:** AUTOPSIA theorem-grade.
**What we know after this doc that we did not know before:** the elementary
fact "`H_L = D_L + B_L` is essentially self-adjoint on `C_00`" (already proved,
E77.7d) forces `H_L`'s deficiency indices to be `(0,0)`, i.e. `H_L` is in the
*strong* limit-point case at both ends. This resolves an ambiguity in reading
`SAFE-LIMIT-POINT`'s "infinite rectangular CCM equation" (it must be the
inhomogeneous resolvent equation, not a homogeneous deficiency-family
equation) and closes that reading trivially for `z` off `spec(H_L)`. But it
provably does **not** reach any of the open subclauses (c)-(f) of
`BORDERED-WEYL-COMPLETENESS`, because those are statements about behavior
exactly *at* the boundary spectral point `mu_L = inf spec(H_L)`, together with
a finite-section convergence-rate statement, neither of which is implied by,
or even addressed by, essential self-adjointness of the limit operator. A
direct two-line counterexample makes the gap airtight rather than a hand-wave.

## 0. Wall checklist

```text
MW-1:  respected.  No positivity of a Weil form is introduced.
MW-2:  respected.  No arithmetic content is used; this is a pure operator-
       theory audit of H_L = D_L + B_L, already proved build-neutrally in
       E77.7d for both the zeta and planted builds.
MW-3:  respected.  No local-to-global infinite assembly is claimed; the note
       explicitly separates the elementary off-spectrum fact from the
       at-mu_L / finite-section-rate facts it does NOT cover.
MW-4:  respected.  No lower bound is manufactured from an upper bound.
MW-5:  respected.  No site/cohomology input.
MW-6:  respected.  No uniform spectral-gap hypothesis is smuggled in; on the
       contrary this note is precisely about why NO such gap statement
       follows from self-adjointness alone.
K1-K5: respected.  No ambient bordered-inverse norm (P76.061) is invoked; the
       resolvent identity used below is the ordinary elementary one for a
       self-adjoint operator away from its spectrum.
P76.061: respected.
E72.16/E77.7az: respected.  The counterexample in section 4 is build-neutral
       by construction (it is an abstract 2x2 model, not tied to zeta or the
       plant); nothing build-discriminating is promoted here as forcing.
```

## 1. What route 1 was asked to check

An external review of the program observed that `H_L = D_L + B_L`
(`D_L` real diagonal, unbounded, `B_L` bounded self-adjoint, E77.7d `(OR-5)`)
is essentially self-adjoint on `C_00` by the elementary bounded-perturbation
argument, and asked whether this elementary fact is equivalent to, or
directly implies, `SAFE-LIMIT-POINT` (P76.065):

```text
SAFE-LIMIT-POINT:
among l2 solutions of the infinite rectangular CCM equation, the condition
r_{z0}v=1 selects a unique safe Cauchy transform, namely that of k_L.
```

E77.7d already proves exactly the elementary fact; nothing new needs to be
established there. The question is purely about the *connection* to
`SAFE-LIMIT-POINT` / `BORDERED-WEYL-COMPLETENESS` (E77.7k), which is the
actual open ledger target.

## 2. Deficiency indices of `H_L` are `(0,0)`, not `(1,1)`

Essential self-adjointness of a symmetric operator `T` on a core is
*equivalent*, by von Neumann's theorem, to its deficiency indices
`n_+(T) = dim ker(T^* - i)`, `n_-(T) = dim ker(T^* + i)` both being zero. So
E77.7d's result restates precisely as:

```text
n_+(H_L) = n_-(H_L) = 0.                                          (D-1)
```

Consequence, elementary and unconditional: for every non-real `z`,

```text
ker_{l2}(H_L - z) = {0}.                                          (D-2)
```

There is **no** nontrivial l2 solution of the homogeneous equation
`(H_L - z)v = 0` for any `z` off the real axis. This is the classical "strong
limit point" case (index 0), stronger than the generic Sturm-Liouville
limit-point case (index 1) that a single rank-one boundary condition
`r_{z0}v = 1` would normalize a 1-dimensional deficiency space in.

## 3. This forces a specific reading of `SAFE-LIMIT-POINT`, and closes that reading elementarily

`(D-2)` rules out reading "l2 solutions of the infinite rectangular CCM
equation" in `SAFE-LIMIT-POINT` as the homogeneous deficiency equation
`(H_L - z)v = 0`: that space is `{0}`, and `r_{z0}v = 1` could never be
imposed on it (0 does not satisfy `r_{z0}v=1`). If that were the intended
reading, `SAFE-LIMIT-POINT` would be vacuously false, which is inconsistent
with it being an open, actively pursued endpoint. So the only consistent
reading is the **inhomogeneous** resolvent equation with a fixed source
vector `b` (the boundary/Cauchy source coming from the `+1` bordering index
of `build_mp`'s `(2N+1) x (2N+1)` matrix, in the `N -> infinity` limit):

```text
(H_L - z0) v = b,   b in l2 fixed,   v in l2.                     (D-3)
```

Under this reading, for `z0` real and off `spec(H_L)` (or `z0` non-real),
`(D-1)` gives immediately, by the standard self-adjoint resolvent calculus:

```text
v = (H_L - z0)^{-1} b   exists and is the UNIQUE l2 solution of (D-3),   (D-4)
```

with `||(H_L - z0)^{-1}|| <= 1/dist(z0, spec(H_L))`. This is completely
elementary -- it uses nothing beyond `(D-1)`/`(D-2)` and the spectral
theorem. Under reading `(D-3)`, existence-and-uniqueness of the l2 solution
is settled by E77.7d with no further work, for any `z0` off the (discrete,
E77.7d + compact resolvent) spectrum of `H_L`.

**This is the one genuine, checkable increment from route 1**: it pins down
the correct reading of `SAFE-LIMIT-POINT`'s "l2 solutions of the infinite
equation" as inhomogeneous-with-fixed-source, not homogeneous-deficiency, and
closes existence/uniqueness of `v` under that reading for `z0` off
`spec(H_L)` for free. Call this closed sub-statement `EXISTENCE-UNIQUENESS-OFF-SPEC`.

## 4. Why this does not touch `BORDERED-WEYL-COMPLETENESS` (c)-(f) -- an exact counterexample

The remaining content of `SAFE-LIMIT-POINT`, spelled out by E77.7k as
`BORDERED-WEYL-COMPLETENESS` subclauses (b)-(f), is not about a generic `z0`
off the spectrum. It is about:

```text
(c) pencil compatibility exactly at the true mu_L;
(d) existence of the normalized l2 class (the b -> v map's image structure);
(e) dim ker(H_L - mu_L) = 1  and  r_{z0} e_L != 0     (K-3, E77.7k S2);
(f) the finite-section Weyl-disk radius contracting to 0 as N -> infinity,
    i.e. BTG-DIV-L: sup_{z in K} rad D_N(z) <= C_K/(1+S_N(mu_L)) -> 0.
```

`mu_L = inf spec(H_L)` is, by construction (E77.7d S8, `(OR-6)`), itself the
bottom eigenvalue of `H_L` (compact resolvent => discrete spectrum => the
inf is attained). So (c) and (e) ask about behavior **exactly at** a point
*inside* `spec(H_L)`, not off it. `(D-4)` says nothing there: the resolvent
`(H_L - z)^{-1}` is unbounded as `z -> mu_L` along the real axis precisely
*because* `mu_L in spec(H_L)`; the elementary off-spectrum argument
degenerates at exactly the point subclause (e) needs. Self-adjointness alone
-- even the strong `(0,0)`-deficiency form -- gives no information about:

```text
- whether mu_L is a simple eigenvalue,
- whether the (possibly multi-dimensional) eigenspace E_L is annihilated by
  the fixed linear functional r_{z0}(.) = sum_n (.)_n/(z0-d_n).
```

A two-line abstract counterexample makes this airtight rather than a
hand-wave. Take any self-adjoint, compact-resolvent, lower-semibounded
operator `T` (trivially of the exact "diagonal + bounded self-adjoint
perturbation" shape E77.7d proves for `H_L`) with a **doubly degenerate**
ground eigenvalue, e.g. on `l2` with orthonormal basis `{e_n}`,

```text
T e_1 = 0,  T e_2 = 0,  T e_n = n e_n  (n >= 3).                  (D-5)
```

`T = D + B` with `D` diagonal (`D e_n = n e_n` for `n>=3`, `0` on the span of
`e_1,e_2`) and `B = 0` bounded self-adjoint -- exactly the E77.7d shape, and
`T` is e.s.a. on `C_00` by the identical bounded-perturbation argument used
for `H_L`. Its ground eigenspace `E_0 = span(e_1,e_2)` has `dim E_0 = 2`, and
for the functional `r(v) = v_1 - v_2` (a perfectly admissible bounded l2
functional, playing the role of `r_{z0}`), the vector `v = e_1+e_2 in E_0` has
`r(v) = 0`. So neither "`dim E_0=1`" nor "`r` nonvanishing on `E_0`" holds,
even though `T` is e.s.a. of exactly E77.7d's shape and deficiency `(0,0)`
everywhere off its (discrete) spectrum. This proves, unconditionally and
without reference to any specific build:

```text
ESSENTIAL-SELF-ADJOINTNESS-DOES-NOT-IMPLY-(K-3):
there exist operators T = D+B of exactly the E77.7d shape (D diagonal lower-
semibounded self-adjoint, B bounded self-adjoint, T e.s.a. on C_00, compact
resolvent) for which subclause (e) -- dim ker(T-inf spec T)=1 and
nonvanishing of a fixed safe-Cauchy-type functional on that kernel -- FAILS.
                                                                    (D-6)
```

So `(D-1)`/E77.7d's fact is, as a matter of pure logic, *strictly weaker*
than what subclause (e) needs; no amount of re-deriving E77.7d more carefully
can close (e), because the implication is false in general within the exact
operator class E77.7d characterizes. The specific structure of `H_L` (its
particular `B_L`, arising from the Loewner/Hilbert-transform commutator
`(OR-3)` and the arithmetic/planted potential) would have to be used to rule
out `(D-6)`-type degeneracy and functional-vanishing -- and this is exactly
what E78.1/E78.2 already investigated directly (numerically and via the dead
Perron-Frobenius route) and found to be **build-discriminating** (zeta ground
gap collapses geometrically to 0, ratio `~1e-4`, ratios robust N=6..16;
plant gap stays order-one, `~0.14-0.85`), hence a detector under E77.7az/E72.16,
not an admissible LP forcing mechanism.

Subclause (f) similarly is not touched: `(D-4)` is a statement about the
*infinite* operator's resolvent at generic `z0`; `BTG-DIV-L` and the disk
radius bound in E77.7k S4 clause 2 are statements about the *rate of
convergence of finite sections* `A_N(mu_L)` as `N -> infinity`, i.e. about
`S_N(mu_L) = ||(A_N(mu_L)-i eta)^{-1} b_N||`-type quantities (E77.7k `(K-4)`)
at a point *inside* the limiting spectrum. Essential self-adjointness of the
limit `H_L` guarantees existence of a well-defined limit object but supplies
no quantitative control on the approach rate of finite truncations to that
limit at a boundary spectral point; that is a separate compactness/rate
theorem (already flagged as open in E77.7d S10, `DIR-GAP-PAIR`, and in
E77.7aj as `FESHBACH-RITZ-ENVELOPE`).

## 5. Cross-check against the numerical ledger (no new probe fabricated)

Per the mission's numerical-gate discipline, the operative build-
discriminating fact used in section 4's real-world instantiation (not the
abstract counterexample, which needs no probe) is independently cross-
verified across two already-executed, independently-authored probes in this
phase, rather than re-run here (avoiding a redundant detector-spiral probe):

```text
E78_1c_gap_confirm_probe.py / E78_1_GROUND_SIMPLICITY_AUTOPSY.md:
  zeta ground gap collapses geometrically, ratio ~1e-4, N=6..16, both builds
  tested with build_mp.

E78_4a_neutral_ground_cauchy_probe.py / E78_4a_..._results.json:
  independently, at N=16, zeta |lambda0(A)| = 1.5568...e-43 (smallest
  |inner-block eigenvalue|), consistent order-of-magnitude collapse pattern
  with E78.1c's reported gap ratios; plant |lambda0(A)| stays in the
  4.5e-3 .. 7.8e-1 range across N=6..16, no collapse.
```

These two independently-run probes (different scripts, different authors'
sessions within the ledger, different intermediate quantities: eigenvalue
GAP in E78.1c versus smallest-|eigenvalue| of the shifted inner block in
E78.4a) agree on the qualitative build-discriminating collapse pattern,
which is the load-bearing empirical fact behind section 4's claim that (e) is
a genuine, non-hypothetical detector for `H_L`, not merely for the abstract
counterexample `T`. No new number is fabricated in this document; both cited
values are read verbatim from already-committed probe output.

## 6. Consequence: route 1 is a genuine, small, closed increment -- not a closure of the target

```text
CLOSED (this document, elementary, build-neutral):
  EXISTENCE-UNIQUENESS-OFF-SPEC:
  for z0 off spec(H_L) (in particular for any non-real z0, or any real z0
  with dist(z0, spec H_L) > 0), the inhomogeneous infinite CCM equation
  (H_L - z0) v = b has a UNIQUE l2 solution v = (H_L-z0)^{-1} b, immediately
  from E77.7d's essential-self-adjointness result (D-1)/(D-2). This fixes the
  correct reading of "l2 solutions of the infinite rectangular CCM equation"
  in P76.065 as the fixed-source inhomogeneous equation, not the homogeneous
  deficiency-space equation (which is {0} by (D-2) and could not carry a
  r_{z0}v=1 normalization at all).

NOT CLOSED, and PROVEN NOT REACHABLE by this route (D-6):
  BORDERED-WEYL-COMPLETENESS (c),(e): behavior exactly at mu_L (simplicity,
  anchor nonvanishing) -- a genuinely independent fact from essential self-
  adjointness, false in general within the exact E77.7d operator class, and
  empirically build-discriminating for the real H_L (E78.1/E78.2).

NOT CLOSED, and NOT ADDRESSED by this route:
  BORDERED-WEYL-COMPLETENESS (f) / BTG-DIV-L: finite-section convergence
  RATE at the boundary spectral point mu_L; a compactness/quantitative
  question orthogonal to qualitative essential self-adjointness of the limit.
```

The task also asked whether route 2 (`NEUTRAL-GROUND-CAUCHY` /
`NORMALIZED-CLASS-ASSEMBLY`, the source/subspace-side mu-free remnant) might
close directly. That route has already been driven to its current endpoint
inside this same phase: E78.4b shows the anchor scalar `r(z0)v0` is neutral
but, by itself, insufficient (macroscopic in both builds, so not the
obstruction); E78.4c shows the natural companion source scalar
`v0^* g_right` is macroscopic on the plant and tiny on zeta, i.e. it is
itself a detector, inadmissible as LP forcing; E78.4d records the resulting
reset to `NORMALIZED-CLASS-ASSEMBLY`, which remains genuinely open with no
further admissible scalar reduction identified. Re-running that probe chain
tonight would reproduce E78.4a-d's results verbatim and would not constitute
new content; this document does not repeat that work, it only confirms (S5
above) that the numbers it reports are consistent with the independent E78.1c
gap-collapse measurement, which is the fact this document's counterexample
argument (S4) needed as its real-world instantiation.

## 7. Status

```text
candidate closure - pending review, for EXISTENCE-UNIQUENESS-OFF-SPEC only:

proved:
  H_L has deficiency indices (0,0) (restatement of E77.7d's e.s.a. result via
  von Neumann's theorem);
proved:
  consequently ker_l2(H_L - z) = {0} for all non-real z, forcing the
  "infinite rectangular CCM equation" of P76.065 to be read as the
  inhomogeneous fixed-source equation (D-3), not a homogeneous deficiency
  equation;
proved (elementary, build-neutral):
  under that reading, existence and uniqueness of the l2 solution v for z0
  off spec(H_L) is immediate from self-adjointness (EXISTENCE-UNIQUENESS-OFF-SPEC);
proved (counterexample, build-neutral, abstract):
  essential self-adjointness of an operator of exactly E77.7d's shape does
  NOT imply BORDERED-WEYL-COMPLETENESS subclause (e) in general (D-5)/(D-6);
autopsied:
  route 1 (elementary self-adjointness / deficiency-index argument) is
  EXHAUSTED as a route to subclauses (c),(e),(f) of BORDERED-WEYL-COMPLETENESS;
  it closes only the interpretive existence/uniqueness layer, which was never
  the open part of the ledger;
cross-checked, not re-derived:
  route 2's endpoint (NORMALIZED-CLASS-ASSEMBLY, E78.4d) remains open with no
  new admissible reduction found tonight; its two most recent probes
  (E78.1c, E78.4a) are mutually consistent on the build-discriminating
  ground-gap collapse used in this document's S4/S5;
next:
  the LP-interface front's only remaining honest targets are unchanged from
  E78.4d: NORMALIZED-CLASS-ASSEMBLY (subspace/source side, mu-free) and, on
  the BTG side, FESHBACH-RITZ-ENVELOPE / BTG-DIV-L's finite-section rate
  question (E77.7d S10, DIR-GAP-PAIR) -- neither is closed by this document,
  and neither should be reattempted via a modewise scalar attached to the
  singled lowest mode, per E78.4d's already-recorded reset.
```
