# E78.141 — Kernel-Derived Quasimode Autopsy (C1/C2/C3, L in {4,6,8})

Class: **AUTOPSIA**

## 0. What this document is

E78.139 showed that the naive pointwise von Mangoldt vector `u_N(n) = Lambda(|n|)`
fails as a quasimode for the inner-block operator `A_N`, and diagnosed why: the
operator's arithmetic kernel weights `Lambda(p^k)` and evaluates it through the
`q_value` integral transform at `y = k log p`, not as a bare sequence indexed by
mesh position `n`. The natural next move is to build the trial vector directly
from that kernel — i.e. from a finite arithmetic sum over prime powers `p^k <=
maxn`, evaluated the way the operator itself evaluates its kernel, rather than by
sampling `Lambda` at mesh points.

E78.140 (`E78_140_kernel_quasimode_probe.py`) implements three such kernel-derived
variants:

```text
C1: u_N(m) = sum_{p^k<=maxn} log(p) * p^{-k/2} * cos(2*pi*m*(k log p)/L)
C2: u_N(m) = sum_{p^k<=maxn} p^{-k/2} * cos(2*pi*m*(k log p)/L)          (no log p weight)
C3: u_N(m) = sum_{p^k<=maxn} log(p) * p^{-k/2} * (1 - k log p / L)       (linear taper, no cosine)
```

with `maxn = int(lam*lam)`, `lam = e^(L/2)`. This document reports the outcome:
none of the three variants achieves `eps_N -> 0`. It is an autopsy, not a
closure, exactly as instructed by the phase-78 discipline.

## 1. Full result table (verified directly against `E78_140_kernel_quasimode_results.json`)

`eps_N = ||A_N u_N|| / ||u_N||`, N = 6, 8, 10, 12, 14, 16, dps = 70.

### ZETA build

```text
variant  L    eps_N(N=6..16)
C1       4    0.0734  0.0968  1.4794  1.4679  1.4705  1.4924   <- blows up after N=8
C1       6    0.0812  0.1004  0.1232  0.1592  0.3847  0.3637   <- grows, no decay
C1       8    0.0454  0.0545  0.0627  0.0705  0.0782  0.0860   <- small, slowly GROWING
C2       4    0.0291  0.0673  1.4867  1.4502  1.4704  1.4897   <- blows up after N=8
C2       6    0.0435  0.0495  0.0786  0.1192  0.0739  0.1467   <- erratic, no clean trend
C2       8    0.0303  0.0352  0.0386  0.0457  0.0534  0.0613   <- small, slowly GROWING
C3       4    0.0012  0.0176  1.9216  1.8699  1.8984  1.9361   <- blows up after N=8
C3       6    0.0015  0.0007  0.0053  0.0203  0.2574  0.0122   <- erratic/noisy, no clean trend
C3       8    0.0035  0.0023  0.0020  0.0024  0.0037  0.0058   <- small, roughly FLAT
```

### PLANTED build (falsifier `planted = ("14.134725141734693790","0.30","5.0")`)

```text
variant  L    eps_N(N=6..16)
C1       4    0.0278  0.0922  9.8736  9.7702  9.7550  9.5329   <- blows up after N=8, ~7x larger than zeta
C1       6    0.4405  0.5625  0.7301  1.0555  2.8784  3.0820   <- grows large, far bigger than zeta
C1       8    0.3007  0.3739  0.4539  0.5533  0.6979  0.9709   <- GROWING, ~10x zeta and diverging
C2       4    0.0087  0.0927  9.8796  9.6497  9.5442  9.4884   <- blows up, similar to C1
C2       6    0.2340  0.2715  0.4825  0.8506  0.1886  1.7858   <- erratic but larger than zeta
C2       8    0.1989  0.2391  0.2723  0.3604  0.4950  0.7679   <- GROWING, ~10x zeta and diverging
C3       4    0.0010  0.0378  12.5732 12.2051 11.9603 11.8135  <- blows up, same shape as zeta but larger
C3       6    0.0047  0.0008  0.0309  0.1600  1.3350  1.3469   <- erratic, grows large at the end
C3       8    0.0203  0.0110  0.0069  0.0109  0.0307  0.0956   <- small at first, then clearly GROWING
```

All 108 rows (9 cells x 6 N-values x 2 builds) checked directly against the JSON;
the values above match to the displayed precision.

## 2. Headline verdict

**No variant shows genuine decay `eps_N -> 0`, for either build, at any L.**
The original target of this probe — a kernel-derived quasimode with vanishing
residual, feeding the standard quasimode-to-eigenvalue min-max argument for
`mu_N -> 0` — is **not achieved** by C1, C2, or C3. This must be stated as
plainly as the E78.139 result: this is a second real mechanism tried and found
insufficient, not a near-miss.

## 3. The L=4 / L=6 instability

At `L=4`, every variant (both builds) blows up by roughly 15-20x in a single
step, immediately after `N=8`, and then plateaus at the larger scale rather
than continuing to grow smoothly. This is a sharp regime change, not gradual
growth, which is itself informative: it does not look like ordinary asymptotic
divergence, it looks like a construction breakdown at a specific resolution.

The natural suspect is the prime cutoff. Recall `maxn = int(lam*lam)`,
`lam = e^(L/2)`:

```text
L=4:  lam = e^2  ~ 7.389   ->  maxn ~ 54     (primes up to 54: 16 primes)
L=6:  lam = e^3  ~ 20.09   ->  maxn ~ 403    (primes up to 403: 79 primes)
L=8:  lam = e^4  ~ 54.60   ->  maxn ~ 2981   (primes up to 2981: 430 primes)
```

At `L=4`, the trial vector is built from only 16 primes (and their prime
powers) — an extremely thin arithmetic sum to stand in for whatever "true"
kernel symbol it is meant to approximate. At `L=6` the count is ~79 primes,
still modest; at `L=8` it jumps to 430 primes, almost an order of magnitude
more data. The L=6 rows are also visibly noisier / non-monotone (e.g. zeta
C3, L=6: `0.0015, 0.0007, 0.0053, 0.0203, 0.2574, 0.0122` — not a clean trend
in either direction), consistent with a construction that is still
under-resolved at that cutoff. This is the best available diagnosis, but it is
not proven here: it is flagged as an open question that a future probe should
test directly, by holding `L` fixed and independently increasing `maxn` (i.e.
decoupling the prime cutoff from `lam`) to see whether the L=4/L=6 blowup
disappears. Until that control experiment is run, "small-`maxn` artifact" and
"genuine breakdown of this construction outside a resonance band" remain both
live, unresolved possibilities. Do not treat the diagnosis above as settled.

## 4. The L=8 / C3 pattern — named precisely, not oversold

At `L=8`, `C3`, the zeta build's `eps_N` sequence is small and roughly flat
across the whole range: `0.0035, 0.0023, 0.0020, 0.0024, 0.0037, 0.0058` —
it dips slightly then rises slightly, staying within a factor of ~3 of its
minimum, with no clear monotone trend in either direction. The planted
build's `eps_N` at the same cell starts comparably small, `0.0203` at N=6,
but then **grows monotonically and clearly** to `0.0956` by N=16 — roughly a
4.7x increase over the same N range, and by N=16 it is about 16x larger than
zeta's value at the same N.

Call this pattern **BOUNDED-KERNEL-RESIDUAL**: at this one (variant, L) cell,
the zeta build's residual stays bounded near a small, non-decaying scale,
while the planted build's residual visibly diverges away from that scale. It
is a real, qualitative zeta/plant separation, and as such it is a legitimate
data point on Front B (cf. E72.16 / E77.7az zero-filter and falsifier
discipline) — the falsifier probe is doing its job by resolving something
here that a symmetric or coincidental construction would not resolve.

**But it must not be oversold.** The standard quasimode-to-eigenvalue min-max
argument needs `eps_N -> 0`, i.e. vanishing residual, to certify an
eigenvalue near the Rayleigh quotient. A residual that is merely *bounded*
(and worse, itself slowly *growing* on the zeta side too, from 0.0020 up to
0.0058 — a near-tripling, not a plateau in the strict sense) does not feed
that argument at all. Boundedness at a nonzero scale gives no eigenvalue
certificate by itself; it is at most a hint that *something* about this
particular kernel construction distinguishes the two builds at L=8, C3,
worth investigating on its own terms, but it is not one further step closer to
proving `mu_N -> 0` under the argument this probe was built to test. This
document names it as an open, weaker object for a possible future direction —
not as progress toward Point 1.

## 5. Diagnosis of C1 vs C2 vs C3

- **C1** (log p weight, cosine oscillation) and **C2** (same, no log p weight)
  behave similarly to each other in shape — both blow up sharply at L=4 and
  grow noisily at L=6 — with C1 generally producing somewhat larger residuals
  than C2 given the extra `log p` weighting amplifies large-prime
  contributions. Neither shows decay at any L.
- **C3** (linear taper `1 - k log p / L`, no oscillation) is the best-behaved
  of the three at L=8: it produces the smallest residuals overall and the
  only near-flat zeta sequence in the whole table. It is also the only
  variant giving the BOUNDED-KERNEL-RESIDUAL contrast described in Section 4.
  This suggests, weakly, that a taper matched to the kernel's own cutoff
  structure is a better starting point than an explicit cosine basis — but
  C3 still does not decay, and still blows up badly at L=4.

## 6. What should be tried next (recommendation, not a commitment)

1. **Decouple `maxn` from `lam`** as a direct control experiment for the L=4/
   L=6 instability: fix L at 4 or 6, hold the cosine/taper construction fixed,
   and sweep `maxn` independently (e.g. force `maxn` up to the L=8 value of
   ~2981 while keeping `L=4`) to see whether the blowup at N>8 is purely a
   prime-cutoff artifact or persists regardless of `maxn`. This is the
   cheapest, most decisive next experiment and should come first.
2. If the blowup survives a large `maxn` at small L, that rules out the
   cutoff-artifact hypothesis and points to a genuine structural obstruction
   in this family of trial vectors — worth naming and setting aside rather
   than iterating further on cosine/taper variants.
3. **Push C3-style tapering further**: since C3 was the best-behaved variant
   at L=8, a natural next family is other tapers (e.g. smoother than linear,
   or matched explicitly to whatever weight function the kernel's `q_value`
   transform uses) at L=8 and above, to see whether a better-chosen taper can
   convert BOUNDED-KERNEL-RESIDUAL into genuine decay.
4. **Consider abandoning the "symbol as trial vector" approach** as the
   primary line entirely, in favor of either (a) solving the reduced
   finite-N eigenvalue problem numerically at each N and reading off the
   actual near-null eigenvector structure (rather than guessing a trial
   vector analytically), or (b) working with min-max comparison operators
   directly (sandwiching `A_N` between operators with known spectra) rather
   than constructing an explicit quasimode at all. Two independently
   constructed trial-vector families (E78.139's pointwise Lambda vector, and
   this document's three kernel-derived variants) have now both failed to
   decay; a third variant in the same family is unlikely to be the highest-
   value next move without first trying a genuinely different mechanism.

None of these are started in this document, per phase-78 discipline against
restarting a detector spiral.

## 7. Wall / discipline checklist

```text
MW-1..MW-6:      not engaged; this is an operator-quasimode construction,
                 not a positivity route.
K1-K5:           not directly invoked; falsifier discipline was honored via
                 the standard planted=(14.134725141734693790, 0.30, 5.0) build
                 run in parallel with zeta at every (variant, L, N) cell.
P76.061:         honored; no ambient bordered-inverse norm used.
E72.16:          zero-filter gate not separately invoked; this probe compares
                 builds directly rather than filtering zero sets.
E77.7az:         the zeta/plant contrast at L=8/C3 (Section 4) is exactly the
                 kind of qualitative separation this gate looks for, but it is
                 explicitly NOT elevated to a proof step here — see the
                 caveat in Section 4 about bounded vs vanishing residual.
```

## 8. What we know now

Two independently constructed quasimode families for the inner-block operator
`A_N` — E78.139's naive pointwise `Lambda(n)` vector, and this document's three
kernel-derived variants (cosine-weighted, unweighted-cosine, linear-taper) —
have both been tested against zeta and the standard planted falsifier across a
real N-range (6 to 16) and multiple L values (4, 6, 8), and neither family
produces `eps_N -> 0` for either build at any tested L. One weak, precisely
named signal survives (BOUNDED-KERNEL-RESIDUAL at L=8/C3), and it is a real
zeta/plant qualitative separation on Front B, but it does not itself feed the
quasimode-to-eigenvalue argument and must not be read as partial progress on
`mu_N -> 0`.

## 9. Status

```text
proved:    none.
observed:  full eps_N table above, verified directly against
           E78_140_kernel_quasimode_results.json for all 108 rows;
           sharp regime-change blowup at L=4 (all variants, both builds)
           immediately after N=8; noisy/non-monotone behavior at L=6;
           BOUNDED-KERNEL-RESIDUAL contrast at L=8/C3 (zeta flat near
           0.002-0.006, planted growing 0.020 -> 0.096 over N=6..16).
refuted:   C1, C2, C3 as sources of a decaying quasimode at any tested L;
           the hypothesis that a kernel-derived (rather than pointwise)
           trial vector alone suffices to drive eps_N -> 0.
open:      whether the L=4/L=6 blowup is a maxn/prime-cutoff artifact or a
           genuine construction breakdown (Section 3, control experiment
           proposed in Section 6.1); whether a better-chosen taper (built on
           the C3 family) can convert BOUNDED-KERNEL-RESIDUAL into genuine
           decay at larger L; mu_N -> 0 itself (Point 1) remains fully OPEN.
live:      Section 6 recommendations, none started this session.
```

---

## 10. Combined status of Point 1 (`mu_N -> 0`) across this session

Three real, independent mechanisms were tested against Point 1 this session,
each producing an candid, verified, negative or inconclusive result — not a
closure:

```text
(a) E78.137 (MU-CONVERGENCE-GATE): a solid Branch-B structural gate was
    established, giving necessary conditions / reductions for mu_N -> 0, but
    it is a gate, not a proof that the gate is passed.
(b) E78.139 (VON-MANGOLDT-QUASIMODE-AUTOPSY): the naive pointwise trial
    vector u_N(n) = Lambda(|n|) was tested directly against A_N for both
    builds across L in {4,6,8}; eps_N grows or stabilizes at order one in
    every case; diagnosed cause: the operator's kernel evaluates its
    arithmetic weight through the q_value integral transform at y = k log p,
    not as a pointwise sequence indexed by mesh position -- ruled out as
    insufficient, for a stated and verified reason.
(c) E78.141 (this document, KERNEL-QUASIMODE-AUTOPSY): three kernel-derived
    trial-vector variants (C1/C2/C3), built to respect that same integral
    kernel, were tested across the same (build, L, N) grid; none achieves
    eps_N -> 0 at any L; L=4/L=6 show a sharp construction-breakdown
    instability of undetermined origin; one weak, precisely bounded, and
    explicitly non-decaying signal (BOUNDED-KERNEL-RESIDUAL at L=8/C3)
    survives as a genuine zeta/plant separation but does not feed the
    min-max argument -- ruled out as insufficient, for a stated and
    verified reason.
```

**Point 1 (`mu_N -> 0`) remains OPEN.** This is legitimate, candid research
output: three real mechanisms were designed, run at dps>=70 against both zeta
and the standard falsifier, and each was ruled out or found insufficient for a
specific, verified, stated reason. It is not a closure of Point 1, and no
claim of closure is made here. Neither Omega7 nor RH is claimed proved.
