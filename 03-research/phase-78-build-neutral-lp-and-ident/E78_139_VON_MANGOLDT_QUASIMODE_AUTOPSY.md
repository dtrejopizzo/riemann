# E78.139 - Von Mangoldt pointwise quasimode: autopsy

**Run:** probe executed 2026-07-18/19, results read and verified 2026-07-20.
**Question:** does the naive pointwise von Mangoldt vector `u_N(n) =
Lambda(|n|)` (zero-padded at non-prime-powers) on the mesh `d_n = 2 pi n / L`
serve as an approximate zero-energy eigenvector of the inner-block operator
`A_N = H_L[1:-1,1:-1]`, i.e. does `eps_N = ||A_N u_N|| / ||u_N|| -> 0`?
**Verdict:** **NO.** For both the genuine (zeta) and planted-falsifier
builds, at every tested `L in {4,6,8}` and `N=6..16`, `eps_N` grows or
stabilizes at order one; it never shows decay. This is a genuine negative
result for the construction as posed. The failure is diagnosed (not proved)
to come from a basis mismatch: the operator's own arithmetic kernel samples
`Lambda` at points `y = k log(p)` inside a continuous integral transform
(`q_value`), not at the mesh index `n` itself; a bare pointwise-in-`n`
sequence does not respect that structure. This document is an autopsy: it
closes this specific attempt and names the next candidate object. It does
not close `mu_N -> 0`.

## 0. Wall checklist

```text
MW-1:  respected. No positivity/Weil-form target appears; this is a raw
       Rayleigh-residual measurement of a trial vector against A_N.
MW-2:  respected. Inside the fixed-L / Re(s)>1 arithmetic front (build_mp,
       lambda=6, L in {4,6,8}), reusing E78.137's corrected inner-block
       convention verbatim.
MW-3:  respected. No local-global prime assembly; Lambda(n) is used only as
       a candidate trial-vector coefficient, and the failure of that trial
       is exactly what is reported.
MW-4:  respected. No wrong-sign lower-bound mechanism is invoked or assumed.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform spectral-gap hypothesis is assumed or used;
       this document is orthogonal to E78.137's Branch-A/B gap question --
       it tests a candidate quasimode vector, not the spectral tower.
K1-K5: respected. No determinant endpoint closure, no Christoffel evaluator,
       no ambient bordered-inverse norm before paired reduction.
P76.061: respected. No inversion of the full logarithmic quotient is used.
E72.16/E77.7az: respected as a DISCIPLINE note, not as a finding here -- see
       section 4: this attempt does NOT exhibit build separation (both
       builds fail similarly), so the falsifier-location principle has
       nothing to say yet about this route. Nothing here is forced into a
       discriminant narrative.
LP-side: this document is PURELY front B (IDENT / mu_N -> 0 chain). It says
       nothing about, and does not touch, LP-side neutrality (front A /
       E78.6-E78.98 material) at all.
```

## 1. The construction and the negative result

**Object.** For each `(L, N)` and each build, `build_mp` (P76.002, reused
verbatim) returns the full bordered CCM matrix `H` on index set
`-N..N`; `A_N = H[1:-1,1:-1]` is the inner block on `-N+1..N-1` (the E77.7d /
E78.1 / E78.137-corrected operator convention -- never the full bordered `H`).
The trial vector `u_N` is built directly on the inner index set: for inner
index `m`, `u_N(m) = Lambda(|m|)` (the von Mangoldt function, zero at every
non-prime-power, `log p` at `p^k`), with `u_N(0) = 0`. Measured:

```text
eps_N      = ||A_N u_N|| / ||u_N||                 (Rayleigh-type residual)
rayleigh_N = <u_N, A_N u_N>| / ||u_N||^2            (Rayleigh quotient)
```

against `N = 6, 8, 10, 12, 14, 16`, `L in {4, 6, 8}`, both the zeta build and
the `PLANTED = ("14.134725141734693790", "0.30", "5.0")` falsifier build, at
`dps=70`, `lambda=6`. Source: `E78_138_quasimode_probe.py` (script) and
`E78_138_quasimode_results.json` (data, both already on disk from a prior
session, cross-checked before writing this document).

**Result -- zeta build, L=4** (`eps_N`, `N=6..16`):
```text
0.43932848841698263154  ->
0.39450037555163841632  ->
1.6045363829714218355   ->
2.2284211098600008496   ->
2.6349899048163710364   ->
2.7195002878753603802
```
i.e. `0.439 -> 0.395 -> 1.605 -> 2.228 -> 2.635 -> 2.720`: a small initial dip
followed by sustained, large growth. The same qualitative shape (dip then
growth to order one or more, never decay) holds at `L=6` (`0.183 -> 0.254 ->
1.101 -> 0.932 -> 0.949 -> 1.273`) and `L=8` (`0.231 -> 0.371 -> 2.050 ->
1.423 -> 1.113 -> 1.155`).

**Result -- planted build.** Same qualitative pattern, larger magnitude:
`L=4`: `1.452 -> 0.787 -> 1.570 -> 2.249 -> 2.663 -> 2.745`.
`L=6`: `0.031 -> 0.336 -> 6.846 -> 5.296 -> 4.417 -> 4.495`.
`L=8`: `0.904 -> 1.756 -> 13.463 -> 9.184 -> 6.730 -> 6.757`.
The plant grows to larger absolute values than zeta at `L=6,8` (up to
`eps_N ~ 13.46` at `L=8, N=10`), but the qualitative behavior -- growth or
order-one stabilization, no decay -- is the same as zeta's.

**No decay anywhere.** Across all 6 (build, L) combinations and all `N`
tested, `eps_N` never trends toward `0`. It is not merely slow convergence
or a large constant with visible decay onset; the `eps_ratio_consecutive`
values in the JSON show `eps_N` still growing or oscillating at `N=14->16`
in most cells (e.g. zeta `L=4`: ratio `1.032` at the last step -- still
growing, not yet turning over).

## 2. The N=14/N=16 coincidence (verified, not a bug)

In every `(build, L)` cell, `norm_u` and `rayleigh_N` are bit-identical
between `N=14` and `N=16`, while `eps_N` differs. This was checked and is
mathematically correct, not an artifact:

- `Lambda(14) = Lambda(15) = 0` (neither 14 nor 15 is a prime power), so
  going from the `N=14` inner index range (`-13..13`) to `N=16`
  (`-15..15`) adds zero new nonzero mass to `u_N`.
- `entry(m, n, L, lam)` (the CCM matrix-entry function, P76.002) depends
  only on `(m, n, L, lam)`, not on the section size `N`. So the submatrix
  of `A_N` restricted to `|m|, |n| <= 13` is literally identical between the
  `N=14` and `N=16` builds.
- Consequently `<u_N, A_N u_N>` and `||u_N||`, both computed entirely over
  the (unchanged) nonzero support of `u_N`, are identical at `N=14` and
  `N=16`. `rayleigh_N` and `norm_u` inherit this exactly.
- `eps_N = ||A_N u_N|| / ||u_N||` uses the FULL `||A_N u_N||`, including the
  new rows at `|m| in {14, 15}` that pick up nonzero off-diagonal
  contributions from the old (unchanged) nonzero components of `u_N` even
  though `u_N` itself gained no new mass there. So `eps_N` correctly still
  changes between `N=14` and `N=16`, and it does (`2.6350 -> 2.7195` at
  zeta `L=4`). This is recorded here explicitly so it is not mistaken for a
  bug in a future session.

## 3. Diagnosis: why this specific ansatz fails

The operator's own construction gives a direct clue. From
`P76_002_mp_entry_audit.py::entry`, the arithmetic contribution to a matrix
entry `entry(m, n, L, lam)` is

```python
maxn = int(lam * lam)
for p in primes_upto(maxn):
    lp = mp.log(p)
    pm, exponent = p, 1
    while pm <= maxn:
        arith += lp * mp.power(pm, mp.mpf("-0.5")) * q(exponent * lp)
        pm *= p
        exponent += 1
```
where `q(y) = q_value(m, n, L, y)` is a continuous sine/cosine kernel
(discrete-Hilbert-transform-shaped: `(sin(2 pi m y/L) - sin(2 pi n y/L)) /
(pi(n-m))` off-diagonal, `2(1-y/L)cos(2 pi n y/L)` on-diagonal). The key
fact: `Lambda(p^k) = log p` enters the operator not as a coefficient indexed
by the mesh position `n`, but weighted by `p^{-k/2}` and evaluated as an
ARGUMENT to the continuous kernel `q`, at the point `y = k log(p) = log(p^k)`
-- i.e. at the LOGARITHM of the prime power, which is an essentially
irrational, unevenly-spaced point on `[0, L]` (mod the kernel's implicit
periodicity), not at the integer mesh index `k` or `p^k` itself. This is
consistent with `H_L`'s documented structure (E77.7d: `H_L = D_L + B_L`,
diagonal `~ log(1+|n|)`, off-diagonal built from a discrete Hilbert
transform of an almost-periodic prime symbol): the "prime symbol" that the
operator is almost-periodic IN is a function of the continuous variable `y`
sampled at `{log p^k}`, not a sequence indexed by the integer mesh position
`n`.

The E78.138 trial vector instead builds `u_N(n) = Lambda(|n|)`: it treats
the mesh INDEX `n` itself as if it were the prime-power argument (as if
asking "is the `n`-th mesh point a prime power," rather than "what is the
kernel's response at the point `y = log(prime power)`"). These are
different objects whenever `n` is not itself equal to some `log(p^k)`, which
is generically always (the mesh points `d_n = 2 pi n/L` are evenly spaced in
`n`; the arithmetic kernel's natural sample points `log(p^k)` are not evenly
spaced and do not coincide with the integer mesh grid at all, except by
coincidence for the smallest primes). So `u_N` as built is very unlikely to
be even approximately aligned with the operator's own eigendirections tied
to the prime side of the symbol -- the observed order-one, non-decaying
`eps_N` is consistent with this basis mismatch.

This diagnosis is offered as a REASONED CANDIDATE explanation, checked
against the operator's own on-record formula, not as a proven cause of the
failure. No independent numerical test isolating this specific mismatch
(e.g. comparing against a kernel-sampled trial vector) was run in this
session; that is exactly the next open step (section 4 below).

## 4. Falsifier note

E72.16/E77.7az's falsifier-location principle expects build separation
(zeta vs. plant differing at the level of a VALUE) when a route is actually
resolving something real. Here it does not apply yet: **both builds fail in
qualitatively the same way** -- growth or order-one stabilization of
`eps_N`, no decay, for zeta AND for the plant, at every `L`. The plant's
`eps_N` values run somewhat larger in absolute terms (up to `~13.46` vs.
zeta's `~2.72`), but the shape of the curve (small early value, then a jump
to order one or more, then a slower drift) is the same for both. This
attempt has not reached the point where the discriminant-in-a-value
principle would even have something to say; recording that honestly here so
it is not later mis-cited as a build-separation finding.

## 5. Combined status of Point 1 (`mu_N -> 0`)

Two genuine deliverables exist so far on this line, and they should not be
conflated:

```text
(a) E78.137 (SOLID): the Branch-A/B gate. For zeta, the inner-block tower's
    two lowest eigenvalues nu_0^{(N)}, nu_1^{(N)} collapse to 0 TOGETHER,
    geometrically, at every tested L -- Branch B, not Branch A. This is a
    real structural finding, cross-checked against E78.1/E78.3, and it
    correctly rules out the originally planned rank-one quasimode-deflation
    lemma (which needs an isolated ground state with a uniform positive
    gap -- false for zeta).

(b) E78.139 (THIS DOCUMENT, autopsy, not proof): the natural next tool for
    a Branch-B world -- a von Mangoldt quasimode used to drive a Rayleigh
    residual to 0 directly -- fails in its first, most direct form (bare
    pointwise sampling u_N(n) = Lambda(|n|)). The failure is diagnosed,
    with reasoning tied to the operator's own on-record kernel formula, as
    a basis mismatch: the operator's arithmetic term samples Lambda at
    y = k log(p) through a continuous integral kernel, not at the mesh
    index n directly.
```

**`mu_N -> 0` (Point 1) remains OPEN.** Neither (a) nor (b) closes it; (a)
narrows which mechanism could possibly work (ruling out isolated-state
deflation), and (b) narrows what a viable quasimode object must look like
(ruling out bare pointwise `Lambda(n)` sampling). No false-victory claim is
made here; per this program's own standing principle, a correctly-executed
autopsy that narrows the search is a complete and valid deliverable in its
own right, distinct from (and not a substitute for) a closure.

## 6. Next object (named, not built)

The next probe should NOT reuse `u_N(n) = Lambda(|n|)`. It should instead
build a trial vector derived from the SAME integral/kernel machinery the
operator itself uses, e.g. one of:

```text
(i)   u_N(m) built by evaluating the same q_value(m, n, L, y) kernel at the
      arithmetic sample points y = k log(p) (i.e. push the "sampling at
      log(prime power)" step into the trial vector's OWN construction,
      instead of sampling Lambda at the mesh index m);

(ii)  a discretized version of the archimedean+arithmetic symbol itself
      (the full per-entry construction in P76_002's entry(), specialized to
      a single frequency or a small band) used directly as the trial
      vector, rather than a hand-built coefficient sequence;

(iii) a Mellin/spectral combination of Lambda(p^k) p^{-k/2} weighted by the
      L-dependent kernel factors that already appear in entry()'s arith
      sum, so that u_N inherits the operator's own weighting p^{-k/2}
      rather than an unweighted log p.
```

Any of these should be built as a new, explicitly named probe (not folded
into this autopsy) and re-measured for `eps_N -> 0` before any claim about
`mu_N -> 0` is revisited.

## 7. Probes

```text
E78_138_quasimode_probe.py            (already on disk; builds u_N(n) =
                                        Lambda(|n|), computes eps_N,
                                        rayleigh_N against A_N)
E78_138_quasimode_results.json        (already on disk; dps=70, lambda=6,
                                        L in {4,6,8}, N=6..16, both builds)
```

No new script was written for this document; it is a read-and-diagnose
autopsy of an already-executed, already-verified probe. All numbers cited
above are read verbatim from `E78_138_quasimode_results.json`.

## 8. Status

```text
class: AUTOPSIA (theorem-grade negative result + reasoned diagnosis; NOT a
       reduction, NOT a closure).
status: this specific quasimode construction (bare pointwise Lambda(|n|)
        sampling) is REFUTED as a route to eps_N -> 0, for both builds, at
        L in {4,6,8}, N=6..16, by direct dps=70 computation.
status for mu_N -> 0: still OPEN. Two deliverables stand: E78.137 (solid
        structural gate, Branch B) and E78.139 (this autopsy, narrows the
        required quasimode structure but proves no positive result).

proved (by direct computation, cross-checked against the JSON):
  eps_N does not decay for either build, at any tested L, over N=6..16;
  it grows or stabilizes at order one throughout;

proved (by direct computation): the N=14/N=16 identical-value coincidence
  in norm_u and rayleigh_N is exactly explained by Lambda(14)=Lambda(15)=0
  together with entry()'s N-independence -- not a bug;

diagnosed, not proved: the failure traces to a basis mismatch between the
  trial vector's pointwise-in-mesh-index sampling of Lambda and the
  operator's own kernel, which samples Lambda at y = k log(p) inside a
  continuous integral transform;

refuted: this attempt does NOT exhibit build separation between zeta and
  the planted falsifier -- both fail in a qualitatively similar,
  order-growing way, so no discriminant narrative is drawn here;

next: build one of the kernel-derived trial-vector candidates in section 6
  as a new, separately-named probe, and re-measure eps_N before any further
  claim about mu_N -> 0.
```
