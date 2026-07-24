# E79.2 - The near-origin packet does not carry `ZERO`

**Scope:** `GAP-Z` only, second milestone of Phase 79.  
**Class:** AUTOPSIA theorem-grade of the naive near-origin reduction.  
**What we know after this document that we did not know before:** the natural
first guess for `GAP-Z` is wrong. On the zeta side, the few roots of `K_N`
closest to the origin stabilize extremely fast and contribute essentially
nothing to `ZERO`; the whole observed `ZERO` signal is carried by the
complementary cloud/tail. So the problem is not "track the first few roots near
0". Any honest root-displacement route must either use a much wider cofinal
packet or control the cloud collectively.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound mechanism.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. This is a direct split of the independent K_N spectral object.
E72.16/E77.7az: respected. This is a convergence-side inquiry, so only
       build-neutral consequences count as closure. Any zeta/plant separation
       below is recorded only as structure, not as forcing.
Circularity: respected. The split is made at the level of spec(K_N), before any
       arithmetic endpoint identification.
```

## 1. The candidate reduction under audit

Phase 79 set

```text
ZERO_N(sigma)
  = sum_{kappa in spec K_{N+2}} P_sigma(kappa)
  - sum_{kappa in spec K_N}     P_sigma(kappa),                        (N-1)

P_sigma(a) = 2 sigma/(a^2+sigma^2).                                   (N-2)
```

The first natural hope for `E79.2` was:

```text
maybe ZERO_N is already carried by the roots closest to the origin, because
the Poisson kernel P_sigma(a) decays like 1/a^2.                       (N-3)
```

If true, one could reduce `GAP-Z` to tracking a fixed finite packet of
near-origin roots.

This document tests exactly that hope.

## 2. Probe

Companion file:

```text
E79_2_near_origin_zero_probe.py
E79_2_near_origin_zero_results.json
```

Setup:

```text
- lambda = 6,
- dps = 60,
- maxN = 18,
- both builds,
- sigma in {0.55, 1, 2, 3}.
```

For each step `N -> N+2`, the probe sorts `spec(K_N)` and `spec(K_{N+2})` by
absolute value and defines, for each packet size `m`,

```text
ZERO_N^near(m;sigma)
  = sum_{j<=m} P_sigma(kappa_j^{(N+2)})
  - sum_{j<=m} P_sigma(kappa_j^{(N)}),                               (N-4)

ZERO_N^tail(m;sigma)
  = ZERO_N(sigma) - ZERO_N^near(m;sigma).                            (N-5)
```

This is not yet a canonical pairing theorem. It is a prior numerical gate:
does a fixed near-origin packet explain most of `ZERO`, or not?

## 3. First observation: the near-origin zeta roots freeze almost completely

On the zeta side, the roots closest to `0` quickly stabilize to:

```text
N=10: +-14.134725141734695, +-21.022039658..., +-25.010858516..., ...
N=12: +-14.134725141734695, +-21.022039638..., +-25.010857580..., ...
N=14: +-14.134725141734695, +-21.022039638771556, +-25.01085758014569, ...
N=16: same to displayed precision
N=18: same to displayed precision
```

So the very first roots are not wandering appreciably once `N` is modest.

## 4. Result at `sigma = 1`: the near-origin packet does not carry `ZERO`

### Zeta

Using the first `m=8` roots on each side:

```text
N= 8: total = 0.00441146161408, near8 = 8.62004538872e-5,  tail8 = 0.00432526116019
N=10: total = 0.00311967333856, near8 = 3.72090431639e-6,  tail8 = 0.00311595243424
N=12: total = 0.00266839222435, near8 = 3.91129383093e-9,  tail8 = 0.00266838831305
N=14: total = 0.00209014597783, near8 = 7.51403695614e-13, tail8 = 0.00209014597708
N=16: total = 0.00191375639527, near8 = 4.76384745016e-18, tail8 = 0.00191375639527
```

In relative terms:

```text
|near8/total|:
N= 8: 1.95e-2
N=10: 1.19e-3
N=12: 1.47e-6
N=14: 3.59e-10
N=16: 2.49e-15
```

So on the zeta side the fixed near-origin packet contributes essentially
nothing beyond the earliest step. The full `ZERO` is carried by the
complementary tail/cloud.

### Plant

At the same `m=8`:

```text
N= 8: total = -0.187814467254, near8 = -0.21018858278,   tail8 = 0.0223741155255
N=10: total =  0.0087314478509, near8 = -0.0106794326071, tail8 = 0.0194108804581
N=12: total =  0.0120726608506, near8 = -0.00301773880457, tail8 = 0.0150903996551
N=14: total =  0.00736404224019, near8 = -0.00373888983088, tail8 = 0.0111029320711
N=16: total =  0.00774455723221, near8 = -0.00117119025331, tail8 = 0.00891574748552
```

Here the near-origin packet does affect the answer, but not in a stabilizing
way: it can even have the opposite sign to the total. So even on the plant side
the fixed near-origin packet is not a clean carrier of `ZERO`.

## 5. Consequence

The simplest candidate reduction of `E79.2` is false:

```text
"ZERO is basically the first few roots near the origin"
```

is not an admissible reading of the data.

The zeta side is especially decisive: the closest roots freeze, while `ZERO`
stays at size `~ N^{-p}` with `p` just above `1`. Therefore:

```text
the moving content of ZERO is NOT concentrated in any fixed finite
near-origin packet.                                                     (N-6)
```

This is a genuine structural result, not just a failed heuristic.

## 6. What survives for the live route

This autopsy does **not** refute a root-displacement route altogether. It
refines it.

What remains possible is:

```text
1. a cofinal near-origin packet whose width grows with N;
2. a collective cloud-displacement theorem for a whole symmetric block;
3. a direct secular-equation estimate on the difference-of-clouds without
   reducing first to finitely many frozen roots.
```

In other words, `E79.3` can still live, but only in a genuinely cloud-level
form.

## 7. Status

```text
proved by probe:
  on the zeta side, the first few roots of K_N closest to the origin stabilize
  extremely fast and their contribution to ZERO becomes negligible;

proved by probe:
  the fixed finite near-origin packet (tested at m=8, with the wider packet
  data recorded in the companion JSON) does not carry the observed ZERO signal;

observed:
  on the plant side, the near-origin packet can contribute with the opposite
  sign and does not form a clean carrier either;

refuted:
  the naive E79.2 reduction "track only the first few roots near the origin";

open:
  whether a cofinal growing packet or a collective cloud estimate turns ZERO
  into a tractable displacement sum;

next:
  reformulate E79.3 at the cloud level, not at the level of a fixed finite
  near-origin packet.
```
