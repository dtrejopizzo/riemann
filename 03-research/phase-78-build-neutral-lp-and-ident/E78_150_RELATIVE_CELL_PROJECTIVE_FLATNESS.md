# E78.150 - RELATIVE CELL-PROJECTIVE FLATNESS: the point-6 discriminant object

**Run:** 2026-07-21.
**Scope:** IDENT / SAFE-GAMMA-IDENT (point 6).
**Class:** REFORMULATION (NOT a forcing reduction -- see Sec 0.1 correction).

## 0.1 CORRECTION (2026-07-21, joint audit)

The framing below overstates the result. The implication `(PF-10)` is true, but
it is NOT a *smaller* theorem when `A^Gamma_{L,N}` is defined by integrating the
target `g^Gamma` (i.e. `A^Gamma = exp(int g^Gamma)`). In that case, on nested
holomorphic domains `K compact-in V_1 compact-in V`, projective-oscillation
smallness and derivative-defect smallness are **locally equivalent** (both
directions by integration + Borel-Caratheodory + Cauchy):

```text
pOsc_V(|F_{L,N}/A^Gamma_{L,N}|) -> 0   <=>   sup_K |F'/F - g^Gamma| -> 0.
```

So `CELL-PROJECTIVE-FLAT -> 0` is a holomorphic REFORMULATION of
`SAFE-GAMMA-IDENT`, not an independent forcing mechanism. It becomes genuine new
content ONLY if `A^Gamma_{L,N}` (and a modulus estimate for it) is obtained
INDEPENDENTLY -- as an exact cell determinant, a Schur-complement quotient, or a
boundary-integral/finite-product representation that does not already contain the
derivative identity. Cf. P76.039's own caution that `(ET-3) CELL-TRACE` "must not
be used" until the exact cell-smoothed Schur symbol is derived first. This
document is therefore reclassified as a useful reformulation; the hard point-6
content is the INDEPENDENT construction of the cell/Gamma object. See E78.151.
**Attribution:** the reduction and the projective-flatness lemma in this note
come from the program author's audit of the E78.147 chain (external contribution,
2026-07-21). Recorded, checked, and integrated here.

## 0. What we know now (one line)

`SAFE-GAMMA-IDENT-CORE` follows from a single POSITIVE object with no phase and
no derivative in it: the modulus of the relative residual `F_{L,N}/A^Gamma_{L,N}`
must become constant-up-to-scalar on a 2-D complex collar. Holomorphic rigidity
supplies the phase and the derivative for free.

## 1. Why a new object (raw flattening is build-neutral)

E78.147/E78.149 established that the raw incremental flattening
(`W-QUOTIENT-DELTA` / `LOGT-CELL` summable, `~C(sigma)/N^2`) holds for BOTH
builds. Confirmed again by a 1-D modulus check on `E78_8_w_denominator_results`:
`osc_sigma log|F_{N+2}/F_N|` decays for zeta (0.068, 0.044, 0.030) AND for the
plant (0.171, 0.016, 0.006). So raw flattening drives fixed-L convergence
(build-neutral, correct under Outcome A) but is NOT the arithmetic discriminant
of point 6. The discriminant must be the residual of `F_{L,N}` **relative to the
exact Gamma/cell object**, where the plant is required to fail.

## 2. The projective oscillation and the flatness lemma

Fix `L`, a safe compact `K subset (1/2, infinity)`, `K_i = { i sigma : sigma in K }`,
and a bounded simply connected complex neighborhood `V` with `K_i compact-in V`.
For a positive function `u` on `V`,

```text
pOsc_V(u) := inf_{c in R} sup_{z in V} | log u(z) - c |
           = (1/2) osc_{z in V} log u(z).                                 (PO)
```

`pOsc_V` forgets every nonzero scalar amplitude -- exactly the information the
logarithmic derivative also forgets.

```text
LEMMA (holomorphic projective flatness).
For every K_i compact-in V there is C_{K,V} < infinity such that every zero-free
holomorphic R on V satisfies
      sup_{z in K_i} | R'(z)/R(z) | <= C_{K,V} * pOsc_V(|R|).             (PF-1)
Hence if zero-free holomorphic R_N satisfy pOsc_V(|R_N|) -> 0, then
R_N'/R_N -> 0 uniformly on K_i.
```

**Proof.** `V` simply connected, `R` zero-free => a holomorphic branch
`h = log R` exists on `V`. Put `omega = osc_V Re h = osc_V log|R|`. Cover `K_i`
by finitely many disks `D(a_j, r_j/2)` with `closure D(a_j, 2 r_j) subset V`. On
one such disk (`a=a_j, r=r_j`) set `c = (sup_V Re h + inf_V Re h)/2` and
`g = h - c - i Im h(a)`. Then `g' = h'`, `|Re g| <= omega/2` on `V`, and
`|g(a)| <= omega/2`. Borel-Caratheodory on `D(a, 2r)` gives
`sup_{D(a,r)} |g| <= C_0 omega`; Cauchy's estimate then gives
`sup_{D(a, r/2)} |h'| = sup |g'| <= (2 C_0/r) omega`. Max over the finite cover
gives `sup_{K_i} |h'| <= C_{K,V} osc_V log|R|`. Since `h' = R'/R`, this is
`(PF-1)`. QED.

This lemma is elementary and complete. It is the mechanism that turns a
modulus-only, 2-D condition into log-derivative control.

## 3. The reduction theorem

Let `g^Gamma_{L,N}` be the EXACT holomorphic Gamma-prime/cell core to be compared
with `F'_{L,N}/F_{L,N}` (the coupled cell object of P76.040 / E78.98, NOT the
inadmissible hard Euler truncation). Pick `z_* in V` and its zero-free primitive

```text
A^Gamma_{L,N}(z) = exp( integral_{z_*}^{z} g^Gamma_{L,N}(zeta) d zeta ).    (PF-4)
```

Define the RELATIVE CELL RESIDUAL and the positive object

```text
R_{L,N}(z) = F_{L,N}(z) / A^Gamma_{L,N}(z),                                 (PF-5)
CELL-PROJECTIVE-FLAT_{L,N}(V) := pOsc_V( | F_{L,N} / A^Gamma_{L,N} | ).     (PF-9)
```

```text
THEOREM. If F_{L,N} is zero-free on V for large N and
      CELL-PROJECTIVE-FLAT_{L,N}(V) -> 0,                                   (PF-6)
then  sup_{z in K_i} | F'_{L,N}/F_{L,N} - g^Gamma_{L,N} | -> 0,             (PF-7)
and, restoring the explicit moving boundary pole (E78.149: 1/(z-d_{b,N}),
d_{b,N}=2piN/L, O(1/N) with O(1/N^2) increments) and the E78.98 exterior term,
SAFE-GAMMA-IDENT-CORE holds uniformly on K.
```

**Proof.** By `(PF-4)-(PF-5)`, `R'/R = F'/F - (A^Gamma)'/A^Gamma = F'/F -
g^Gamma`. Apply the Lemma to `R_{L,N}`: `(PF-6)` gives `sup_{K_i} |R'/R| -> 0`,
i.e. `(PF-7)`. The boundary and exterior terms are explicit and (E78.149)
summable, so the holomorphic core identity yields the safe-axis identity. QED.

So the proved implication is

```text
CELL-PROJECTIVE-FLAT_{L,N}(V) -> 0   ==>   SAFE-GAMMA-IDENT-CORE.           (PF-10)
```

## 4. Why this is genuinely different from E78.9

E78.9 asks to prove a signed cancellation between two huge complex terms
(`Delta W'/(1+W_N)` vs the mixed term). `(PF-6)` asks only that the **modulus**
of one ratio become constant-up-to-scalar on a 2-D complex collar. It contains
no phase estimate and no derivative estimate; it allows `F_{L,N}` to grow
arbitrarily with N; it kills any scalar amplitude `C_{L,N}` automatically. The
phase and derivative return for free by the Lemma. The 2-D collar is essential:
on the line `z=i sigma` alone a function can have constant modulus and wildly
varying phase (a holomorphic exponential hides all its variation in the phase on
a line); the collar rules that out.

## 5. Live open object and where the plant must fail

```text
RELATIVE-CELL-PROJECTIVE-FLATNESS (open, load-bearing):
   pOsc_V( | F_{L,N} / A^Gamma_{L,N} | ) -> 0   on a 2-D safe collar V,
   for the zeta build; and it must FAIL for the planted build.
```

This is now a positive, phase-free, derivative-free target -- cleaner than the
E78.9 linear-mixed cancellation. It is NOT yet proved. Two concrete next steps:

```text
1. Locate/assemble the exact g^Gamma_{L,N} (P76.040 / E78.98 coupled cell object)
   and its primitive A^Gamma_{L,N}; verify (PF-8) F'/F - g^Gamma numerically on K_i.
2. Compute CELL-PROJECTIVE-FLAT_{L,N}(V) on a genuine 2-D collar V (not just the
   1-D axis), both builds, and test: zeta -> 0, plant bounded away from 0.
```

## 6. Wall checklist

```text
MW-1..6:        not invoked (no positivity, no local-to-global assembly).
K1-K5:          not invoked (no ambient bordered inverse norm; no determinant
                endpoint identification; the residual is a holomorphic ratio).
E72.16/E77.7az: the RELATIVE residual is exactly where build separation is
                REQUIRED (Front B / IDENT), so a build-discriminating outcome
                here is admissible and intended, unlike the build-neutral raw
                flattening of E78.147/E78.149.
```

## 7. Status

```text
proved (complete implication):
  LEMMA (PF-1) holomorphic projective flatness (Borel-Caratheodory + Cauchy);
  THEOREM (PF-10): CELL-PROJECTIVE-FLAT_{L,N}(V) -> 0 => SAFE-GAMMA-IDENT-CORE;

integrated:
  the boundary-pole correction (E78.149, d_{b,N}=2piN/L) is folded in as an
  explicit summable term; raw flattening shown build-neutral, hence the RELATIVE
  residual F/A^Gamma is adopted as the point-6 discriminant object;

open (load-bearing):
  RELATIVE-CELL-PROJECTIVE-FLATNESS -- pOsc_V(|F/A^Gamma|) -> 0 for zeta and
  FAIL for the plant, on a 2-D safe collar;

next:
  (1) assemble exact g^Gamma / A^Gamma from P76.040/E78.98;
  (2) 2-D collar probe of CELL-PROJECTIVE-FLAT for both builds.
```
