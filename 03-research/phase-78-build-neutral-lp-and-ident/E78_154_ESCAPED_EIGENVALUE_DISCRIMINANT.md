# E78.154 - The escaped eigenvalue: M_N structure and the point-6 discriminant

**Run:** 2026-07-21.
**Scope:** IDENT / point 6. Diagnoses M_N (E78.153) sign/support; isolates a
sharp build discriminant.
**Class:** REDUCCION GENUINA + discriminant lead.

## 0. CORRECTION (2026-07-21, same day) -- retract the "single stable avatar"

The trajectory probe E78.155 and a direct spectrum listing REFUTE this
document's central narrative (Sec 3, "a single escaped eigenvalue at a stable
location ~ -50, avatar of the true zero"). The truth:

```text
- The FARTHEST eigenvalue of K_N is at +1673 -> +3748 (GROWING, not stable at
  -50), and it contributes ~2 sigma/(sigma^2 + 1673^2) ~ negligibly to the
  transfer -- it is NOT the driver of anything.
- For zeta N=12 (mesh radius 19.3), 21 of 23 eigenvalues of K_N lie OUTSIDE the
  mesh, in a near-symmetric cloud {+-21,+-25,+-30,+-38,+-42,+-50,+-66,+-99,+-216}
  PLUS the one asymmetric outlier +2558. Because c is tiny, the rank-one term
  (1/c) x q^T reshapes the ENTIRE spectrum -- it does NOT create one isolated
  point. The M_N peak near -50 is part of this symmetric cloud, not an avatar.
- c_N oscillates in sign and is NOT geometrically -> 0 (E78.155:
  3.9e-7, -4.6e-9, 1.3e-7, 2.2e-9, -2e-10, 3.6e-10); it stays SMALL (~1e-7..1e-10)
  but not monotone.
```

So Sec 3's "escaped eigenvalue = avatar of the zero" and Sec 4's "concrete
1-outlier problem" are RETRACTED. What SURVIVES (independently verified):

```text
- BOUND=TRUE=5.4/N^2 summable for zeta (E78.153) -- solid;
- M_N * x single-signed for zeta vs sign-mixed for plant -- solid discriminant;
- |c| small for zeta (~1e-7..1e-10) vs O(10) for plant -- solid.
```

The correct picture: for zeta, c small => the whole K_N spectrum is pushed into
a near-symmetric cloud OUTSIDE the mesh; the summability of BOUND_N is a
difference-of-two-clouds phenomenon (nu_N vs nu_{N+2}), NOT a single outlier. The
honest open problem is therefore harder than Sec 4 claimed. See E78.155 for the
corrected trajectories. Read Secs 3-4 below only through this correction.

## 1. What was measured

For `M_N(x) = (nu_N - nu_{N+2})((-inf,x])` and `BOUND_N = int |M_N| w`
(E78.153), probe `E78_154` reports, per step and build: the sign structure
(`M_N * x` single-signed?), the interior vs edge split of the bound mass
(`X_old = 2 pi (N-2)/L`), and the peak of `|M_N|`.

## 2. Result

```text
build  N->N+2   BOUND    Mx>0 frac   edge frac   peak|M| @ x        (X_old)
zeta   8->10    0.0815   1.00        1.00        2.0 @ -39.19       (10.52)
zeta  10->12    0.0544   1.00        1.00        2.0 @ -49.77       (14.03)
zeta  12->14    0.0378   1.00        1.00        2.0 @ -49.97       (17.53)
zeta  14->16    0.0282   1.00        1.00        2.0 @ -51.49       (21.04)
zeta  16->18    0.0212   1.00        1.00        2.0 @ -53.94       (24.55)
plant  8->10    1.7068   0.740       0.013       1.0 @ -16.79       (10.52)
plant 10->12    0.3230   0.559       0.040       1.0 @ -22.60       (14.03)
plant 12->14    0.0360   0.579       0.154       1.0 @ -28.34       (17.53)
plant 14->16    0.0167   0.705       0.410       1.0 @ -32.79       (21.04)
plant 16->18    0.0052   0.696       0.512       1.0 @ -36.00       (24.55)
```

## 3. Reading -- a sharp structural discriminant

**Zeta.** `Mx>0 frac = 1.0` (so `M_N * x >= 0` everywhere: `M_N` is odd-like,
increasing through 0 -- this is exactly why `BOUND = TRUE`, the Stieltjes
integrand `M_N * 4 sigma x/(x^2+sigma^2)^2` is single-signed). `edge frac = 1.0`:
ALL the bound mass sits OUTSIDE the mesh. `peak|M| = 2.0` at `x ~ -40..-54`, far
beyond the mesh radius `X_old ~ 10..25`. This is an **escaped eigenvalue** of
`K_N = D + (1/c) x q^T`: for zeta `c = F_N(infinity) = 1 - sum x_j` is TINY
(E78.152: 1e-9..1e-7), so the rank-one term dominates and one eigenvalue leaves
the mesh, sitting at a roughly STABLE location `~ -50`. It is separated from the
mesh continuum -- an isolated spectral point of the limiting object.

**Plant.** `Mx>0 frac ~ 0.56..0.74` (`M_N` is SIGN-MIXED, 26-44% opposite), mass
mostly INTERIOR (`edge frac` grows 0.01->0.51 but never dominated by an outlier),
`peak|M| = 1.0` tracking the moving mesh edge `~ -2 pi N/L` (no escape, since
`c = O(10)`).

```text
ZETA:  c -> 0  =>  isolated ESCAPED eigenvalue (~ -50, stable), M_N*x single-signed,
                   bound tight and = TRUE ~ 5.4/N^2.
PLANT: c = O(1) =>  no escape, M_N sign-mixed, interior mass, bound loose/erratic.
```

The escaped eigenvalue is the operator-theoretic avatar of the true zero: `c->0`
is the near-singularity `F_N(infinity)->0`, and it produces one isolated spectral
point detached from the arithmetic mesh. The planted (off-line) build has no such
detachment. This is build-discriminating and lives in IDENT, where separation is
required (E77.7az-admissible).

## 4. Consequence: the two point-6 sub-targets, sharpened

```text
(i) SUMMABILITY (convergence half): BOUND_N is dominated by the escaped-eigenvalue
    region. Route: the escaped eigenvalue kappa_esc(N) of K_N (rank-one escape,
    kappa_esc ~ (q^T x)/c to leading order) sits at a stable location; the pair
    (kappa_esc(N), kappa_esc(N+2)) nearly coincides, and its residual contribution
    to M_N, integrated against the decaying kernel w ~ 1.3/x^2 (interior maximizer)
    down to w ~ sigma/|x|^3 at the outlier, gives BOUND_N ~ 5.4/N^2. Proving this
    is now a CONCRETE 1-outlier problem, not a full cancellation.

(ii) DISCRIMINANT (arithmetic identification): the ESCAPE ITSELF (c -> 0 and the
    resulting isolated eigenvalue) is the clean build separator -- present for
    zeta, absent for the plant. Equivalently, single-signedness of M_N*x
    (tightness BOUND=TRUE) holds for zeta and fails for the plant. This is the
    first sharp, structural (not merely rate-based) point-6 discriminant lead.
```

## 5. Cross-links

`c = 1 - sum_j x_j = F_N(infinity)`; `c -> 0` for zeta is the same near-singularity
that drives the huge transfer scale `|T_N|` (E78.11) and the collapsing ground gap
`nu_0 -> 0` (E78.137). The escaped eigenvalue of `K_N` is the `T`-representation
avatar of that collapse. The bottom-mode coupling `c_0` (E78.145) and this escape
are two facets of the same isolated spectral point.

## 6. Wall checklist

```text
MW-1..6, K1-K5: not invoked (Krein-type spectral shift; no positivity/assembly).
E72.16/E77.7az: the escape/single-signedness discriminant lives in IDENT, where
   build separation is REQUIRED; recorded as the load-bearing lead for point-6
   identification, admissible on this front.
Circularity: nu_N and K_N built from (D,x,q,c); no target integrated (E78.150 trap
   avoided).
```

## 7. Status

```text
observed (decisive):
  zeta: isolated escaped eigenvalue of K_N (~ -50, stable, from c->0), M_N*x
        single-signed, BOUND=TRUE~5.4/N^2 summable, all mass at the outlier;
  plant: no escape (c=O(1)), M_N sign-mixed, interior mass, bound loose;
reduced:
  point-6 convergence half -> control of the single escaped-eigenvalue pair
  (concrete 1-outlier estimate, not a full cancellation);
  point-6 discriminant -> the ESCAPE / single-signedness of M_N*x, present for
  zeta and absent for the plant (first sharp structural separator);
open:
  (i) prove BOUND_N = O(N^{-2}) from the escaped-eigenvalue trajectory;
  (ii) prove the escape (c->0 / isolated kappa_esc) is exactly what SAFE-GAMMA-
       IDENT requires and that the plant provably lacks it;
next:
  track kappa_esc(N) and c_N trajectories; test kappa_esc as the isolated
  spectral point identifying the zeta limit.
```
