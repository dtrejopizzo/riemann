# Round 013 B — Direct computation of λ_max(A_τ): the all-profile cell operator fails at T = 1.5 for Λ itself, and its budget under cΛ

Target (★): λ_A(T) ≥ 0 for every T. Notation of ROUND_012_A §3: λ = e^T, N = λ², v_n = 2Λ(n)/√n, m(τ) = Re ψ(¼+iτ/2) − log π,
and the explicit self-adjoint cell operator on L²[−T,T] (f extended by 0 outside)
  A_τ f(x) = ½ Σ_{n<N} v_n cos(τ log n) [f(x+log n) + f(x−log n)],
with Proposition 3.1 of 012A: sup over real profiles β of P^{ρ_β}_T(τ) = λ_max(A_τ), so (1.2)_κ for all profiles at all
τ ≥ Ω_lo = 2πN(1+δ) ⟺ λ_max(A_τ) ≤ m(τ) − κ there. Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.
Everything in this memo is NUMERICAL.

## 0. Corpus check

Index rows read: P211-11C, P211-12A (the object λ_max(A_τ) is defined there, not computed), P211-11A/11B (two-block
Schur NUMERICAL decisions — a different object, the gauge-quotient form, not A_τ). No entry computes λ_max(A_τ)
directly; this is the next concrete step named at the end of ROUND_012_A ("compute λ_max(A_τ) on [1.1,3]·2πN for
T ≤ 3"). Not a sign step, not a retried route.

## 1. Discretisation (tools/A_tau_lmax.py)

Galerkin method in the orthonormal half-range sine basis e_k(x) = sin(kπ(x+T)/2T)/√T, k = 1..Nb (same basis as
tools/galerkin_mp.py), Nb = 400 throughout. The shift-and-restrict operator Sh(s)f(x) = f(x+s)·1_{[−T,T]}(x) (f
continued by 0 outside [−T,T]) has the exact closed-form matrix element
  ⟨e_j, Sh(s)e_k⟩ = (1/2T)[I(a_j−a_k, (a_j−a_k)T − a_k s) − I(a_j+a_k, (a_j+a_k)T + a_k s)],
  I(c,d) = (sin(cU+d) − sin(cL+d))/c (or (U−L)cos d if c = 0), a_j = jπ/2T, [L,U] = [−T,T] ∩ [−T−s, T−s],
from sin A sin B = ½[cos(A−B) − cos(A+B)] integrated over the overlap of the two translated supports. Since
Sh(s)* = Sh(−s) exactly (both sides equal ∫ f(y)g(y−s)dy with f supported in [−T,T]), the operator Sh(log n)+Sh(−log n)
is exactly self-adjoint and its Galerkin matrix in e_1..e_Nb is symmetric up to floating-point rounding only — no
grid/interpolation artifact, no ad hoc symmetrisation. By Rayleigh–Ritz the Galerkin λ_max(Nb) is a lower bound for
the true λ_max(A_τ) on L²[−T,T], increasing monotonically to it as Nb → ∞.

**Discarded alternative.** A first version used a uniform nodal grid with linear-interpolation shift matrices
(piecewise-linear basis); symmetrised a posteriori, it gave a margin that grew more NEGATIVE without bound as the
grid was refined (M = 400/600/800 at T = 1.5: margin −0.084/−0.353/−0.450) — a genuine divergence, not slow
convergence, from high-frequency aliasing of the shift-by-interpolation. It is not used below.

**Convergence check (NUMERICAL).** At fixed τ, λ_max(Nb) for T = 0.8 is converged to 13 digits already at Nb = 200
(1.0961368952446786/.._446786/.._4717 at Nb 200/400/600); at T = 1.5 it rises 3.598→3.606→3.611→3.613→3.615 over
Nb = 150,300,400,500,600 with shrinking increments (geometric ratio ≈ 0.6–0.7), i.e. Nb = 400 is within ≈ 0.003 of the
extrapolated limit on a value ≈ 3.6; at T = 3.0 the sequence Nb = 200/400/600 gives λ_max = 5.991421/5.992022/5.992274,
margin 0.11492/0.11432/0.11407 (converged to the third decimal). Nb = 400 is used for every reported value below.

**τ-grid.** Fine region [Ω_lo, Ω_lo+0.15(Ω_hi−Ω_lo)] at step ≤ 1/(10T) (where every prior round locates the
minimiser), capped at 1500 points (so the achieved fine step can exceed the target for large T — reported honestly
as `fine_step`, equal to the target except at T = 2.5/3.0 where it is 0.177/0.482, i.e. 4.4×/14.5× coarser than
1/(10T)), plus a coarse pass of 400 points over the whole range [Ω_lo, 2πN·3] to check for a deeper minimum
elsewhere. λ_max(τ) oscillates on a scale of a few target-steps (adjacent grid points 2–3 apart in τ can differ by
0.3–0.5 in the margin: §2.1 found this the hard way, see below), so the top 12 grid candidates are each polished by a
*local* bounded search of half-width 3×(1/10T) only — a first version used a window of 2% of the whole range and let
Brent's method drift from the true minimum to an unrelated, worse local minimum several target-steps away (caught by
comparing against tools/packet_margin.py's single-profile minimiser for T=2, which must sit above the all-profile
minimum pointwise and did not at first).

## 2. Results

### 2.1 Base case (Λ, δ = 0.1)

| T | τ_min | τ_min/2πN | λ_max(A_τ_min) | m(τ_min) | margin m−λ_max | eigvector: centre mass / edge mass / eff. length |
|---|---|---|---|---|---|---|
| 0.8 | 36.684 | 1.179 | 1.0961 | 1.7644 | **0.6683** | 0.198 / 0.505 / 1.52 (2T=1.6) |
| 1.0 | 54.566 | 1.175 | 1.8502 | 2.1615 | **0.3113** | 0.241 / 0.508 / 1.97 (2T=2.0) |
| 1.5 | 140.434 | 1.113 | 3.6106 | 3.1069 | **−0.5037** | 0.264 / 0.411 / 2.90 (2T=3.0) |
| 2.0 | 416.858 | 1.215 | 3.9219 | 4.1949 | **0.2730** | 0.327 / 0.264 / 3.61 (2T=4.0) |
| 2.5 | 1268.804 | 1.361 | 5.0526 | 5.3080 | **0.2554** | 0.432 / 0.222 / 4.51 (2T=5.0) |
| 3.0 | 2819.236 | 1.112 | 5.9920 | 6.1063 | **0.1143** | 0.540 / 0.108 / 4.71 (2T=6.0) |

(centre mass = fraction of ‖eigenvector‖² on |x| ≤ T/3, edge mass = fraction on |x| ≥ 2T/3, eff. length = support
between the 2.5% and 97.5% quantiles of the squared eigenvector, on a 801-point evaluation grid from the Nb=400
coefficients.) A consistency check: at every τ_min tabulated, the mollified-indicator value P^{ind}_T(τ_min) (via
tools/packet_margin.py) is strictly below λ_max(A_τ_min) — e.g. at T=1.5, P^{ind}_T = −1.2399 < 3.6106 — as it must be
by Proposition 3.1 (λ_max is the sup over all profiles, including ind).

**Minimum margin: −0.5037 at T = 1.5.** The all-profile operator form of (1.2) — the exact condition (HR)(a) needs —
is **violated at T = 1.5 for the unmollified Λ itself** (not merely for some cΛ with c > 1): λ_max(A_τ) exceeds m(τ)
by about half a unit at the bottom of the scanned range, over the whole fine region (the minimiser sits essentially
at the left edge of the fine window, as in every previous round). T = 0.8, 1.0, 2.0, 2.5, 3.0 all show a comfortably
positive margin. The trend is **not monotone in T**: 0.668 → 0.311 → **−0.504** → 0.273 → 0.255 → 0.114. The isolated
sign change between T=1.0 and T=2.0 coincides with the window (log 7, log 54] in which the comb (comb(T) in the
script) picks up a cluster of prime powers with comparatively large weight (n = 8,9,11,13,16,17,19 enter between
T=1 and T=1.5, each contributing v_n ∈ [0.35, 1.45]); no single term is responsible (removing any one leaves the
margin negative — not re-verified by a falsifier run below, flagged as a next step). This is an ARGUED reading of
NUMERICAL data, not a proof of anything about T = 1.5 specifically.

Comparison with the single-profile margins of 011C/012A (≈ 0.34–0.36 for the mollified indicator, T = 2–4.5): the
all-profile margin at T = 2.0 (0.273) is smaller than the single-profile minimum there (0.341, recomputed here with
tools/packet_margin.py for the cross-check above) — consistent with λ_max ≥ P^ρ_T pointwise for every profile ρ, so
the all-profile infimum must be ≤ any single-profile infimum. This relation (not equality) is the only check available
without an independent solver; it was violated by the first (buggy) run of this script (see §1) and used to catch
the bug.

### 2.2 Eigenvector shape (NUMERICAL, answer to the owner's question)

The maximiser is, at every T tested, a **long packet spanning nearly the whole window** (effective length
0.79–0.98 of 2T), never a short bump — consistent with the necessity direction of ROUND_012_A §4.2 (short packets
cannot be the extremiser). Its internal shape **changes qualitatively with T**:
- Small T (0.8, 1.0): mass concentrated **near the two edges** of [−T,T] (edge mass ≈ 0.50–0.51, more than double the
  centre mass ≈ 0.20–0.24) — the maximiser looks like two bumps near ±T with a weaker middle.
- Mid T (1.5, 2.0): the two masses cross (edge 0.41→0.26, centre 0.26→0.33): the profile is becoming more uniform.
- Large T (2.5, 3.0): mass concentrated in the **centre** (centre mass 0.43→0.54, edge mass 0.22→0.11): the
  maximiser is now closer to a single bulk packet with decaying tails, the opposite shape from small T.
No qualitative change of shape is visible exactly at the T = 1.5 sign failure; the violation is not obviously carried
by an edge effect or a centre effect specifically — it is a joint effect of the then-small window combined with the
newly entered mid-size prime powers (§2.1).

### 2.3 Budget under cΛ (falsifier (a), T = 2.0 and T = 3.0)

| T | c = 1.00 | c = 1.05 | c = 1.10 |
|---|---|---|---|
| 2.0 | 0.2730 | 0.0769 | **−0.1192** |
| 3.0 | 0.1143 | **−0.1853** | −0.4849 |

(τ_min essentially unchanged by c, since the minimiser location is controlled by the archimedean side m(τ) and by
which comb terms are present, both c-independent to leading order; only λ_max scales up with c.) The crossing
point c*(T) (margin = 0) is between 1.05 and 1.10 at T = 2.0, and between 1.00 and 1.05 at T = 3.0 — i.e. the
all-profile budget shrinks with T even faster than the single-profile budget of ROUND_012_A §5 (there c* ≈ 1.09 at
T=2, ≈1.04 at T=4.5): here the budget is already exhausted by c ≈ 1.02–1.03 at T = 3.0, since T=3.0 is already
margin-positive only by 0.114 at c=1 (compare 012A's 0.355 flat margin for the single ind profile at the same T).
As required by the falsifier test: this is a size statement about cΛ for c ≠ 1 and is expected to fail there; it
is not used as a sign argument for c = 1.

## 3. What this does and does not show

NUMERICAL only; proves nothing about (★) or about (1.2). It computes, for the first time, the actual object
Proposition 3.1 of ROUND_012_A identifies as equivalent to the all-profile form of the packet bound, at six values
of T with a convergence-checked, non-aliased discretisation. The headline finding — λ_max(A_τ) > m(τ) at T = 1.5 for
the true Λ-comb, by about half a unit, immediately above the plunge — means the all-profile sufficient route to
(HR)(a) via (1.2) cannot be uniform in T even before touching cΛ: it fails at a point in the middle of the certified
single-profile range (012A Theorem 2.2 proves the *cos²*-profile instance up to T=2.64), confirming that the gap
between "some profile works" and "every profile works" (the content of Proposition 3.1) is not a technicality — the
all-profile condition genuinely fails on part of the certified-safe range for a single profile. No conclusion about
λ_A(T) itself: A_τ is one cell of W_T, and (HR)(a)/(1.2) is used here as a *sufficient* route to a piece of the
argument, not as a necessary one; its local failure at T=1.5 only closes that particular route there, consistent with
and extending ROUND_012_A's own NO-GOs for a uniform proof via the packet bound.

## Falsifier note

(a) cΛ: computed in §2.3 (budget shrinks with T, crossing between c=1.0 and 1.1 already at T=2–3); the quantity is
expected and shown to fail for c > c*(T), and (more strikingly) to already fail at c = 1 at an isolated T. (b) a_P: not
run this round (next step). (c) Beurling system with the same block masses: not run; comb(T) depends only on the
multiset {(log p, v_n)}, so a Beurling system reproducing the same masses at the same log-points reproduces λ_max(A_τ)
exactly — this computation by itself cannot distinguish ℕ from such a system (as already noted in 012A §5). (d) finite
modification of the weights: not run this round.

## Result

NUMERICAL. Computed λ_max(A_τ) and the margin m(τ)−λ_max(A_τ) on the high range for T = 0.8,1.0,1.5,2.0,2.5,3.0 with
a convergence-checked Galerkin discretisation (Nb=400 sine basis, exact closed-form shift matrix elements). Minimum
margin over the six values: **−0.5037 at T = 1.5** (all-profile condition fails there for Λ itself); all other T
tested give a positive margin (0.11–0.67), non-monotone in T. Eigenvector is always a long packet spanning most of
the window, shifting from edge-concentrated (small T) to centre-concentrated (large T). Budget under cΛ: crosses zero
between c=1.05–1.10 at T=2.0, between c=1.00–1.05 at T=3.0 (tighter than the single-profile budget of 012A).

### What was proved
Nothing (NUMERICAL round); the discretisation method (exact sine-basis Galerkin matrix elements for the
shift-and-restrict operator, Rayleigh–Ritz monotonicity) is a reusable tool (tools/A_tau_lmax.py).

### What failed and why
The all-profile condition λ_max(A_τ) ≤ m(τ)−κ, needed by Proposition 3.1 of 012A for the all-profile form of (1.2),
fails at T=1.5 (margin −0.50) for the unmollified Λ, and its budget under cΛ closes already by c ≈ 1.02–1.08 at
T=2–3 — tighter than the single-profile budget. A first discretisation (nodal grid + linear-interpolation shift) was
abandoned: it diverged under refinement (aliasing), caught by comparing against the exact sine-basis Galerkin method
with Rayleigh–Ritz monotonicity. A first version of the τ-scan silently returned a wrong (too large) margin at T=2.0
because Brent's local refinement window was too wide for the oscillation scale of λ_max(τ); caught by cross-checking
against the known single-profile minimiser location and value (tools/packet_margin.py), which must lie above the
all-profile curve everywhere.

### Next concrete step
Scan a finer T-grid around T ∈ [1.2, 1.8] to locate the width of the T=1.5 violation window and check whether it is a
single isolated dip or part of a wider band; run falsifiers (b) a_P and (d) finite weight changes at T=1.5 to see
whether the violation survives them (per the mandatory falsifier test, if it survives all four classes (a)-(d)
unchanged the finding is likely an artifact of the method rather than of ℕ, since a sign step must distinguish from
Beurling systems, which class (c) cannot do here).
