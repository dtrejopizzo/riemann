# E79.3a - The common cloud packet must be almost the whole cloud

**Scope:** `GAP-Z` only, cloud-level reformulation step after E79.2.  
**Class:** AUTOPSIA theorem-grade of the "small cofinal packet" hope.  
**What we know after this document that we did not know before:** once the
naive finite near-origin packet is discarded, the next natural hope is that a
moderately growing packet of roots ordered by `|kappa|` captures most of
`ZERO`. On the zeta side this is still false in any narrow sense: to recover a
fixed fraction of `ZERO`, the packet must already occupy almost the entire
common cloud. So the live E79.3 object is not a thin cofinal packet; it is a
whole-cloud displacement problem.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound mechanism.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. This is a direct cloud decomposition of the independent K_N
       spectral object, before endpoint identification.
E72.16/E77.7az: respected. This is convergence-side; any build separation below
       is recorded only as structure, not as forcing.
Circularity: respected. Everything is computed from spec(K_N), independent of
       the target arithmetic derivative.
```

## 1. Starting point

E79.2 refuted the fixed finite packet route:

```text
the first few roots closest to the origin freeze quickly and contribute
essentially nothing to ZERO on the zeta side.                           (C-1)
```

So the next honest question is:

```text
if we let the packet width grow with N, does a reasonably small cofinal packet
capture a fixed fraction of ZERO, or does one need almost the whole cloud?     (C-2)
```

## 2. Probe

Companion files:

```text
E79_3_cloud_packet_probe.py
E79_3_cloud_packet_results.json
```

For each step `N -> N+2`, let

```text
spec(K_N)     = {kappa_j^(N)}     sorted by increasing |kappa|,
spec(K_{N+2}) = {kappa_j^(N+2)}   sorted by increasing |kappa|.       (C-3)
```

Since `K_{N+2}` has four more roots than `K_N`, write:

```text
ZERO_N(sigma)
  = ZERO_N^common(sigma) + ZERO_N^extra(sigma),                       (C-4)

ZERO_N^common(sigma)
  = sum_{j<=d_N} P_sigma(kappa_j^(N+2)) - sum_{j<=d_N} P_sigma(kappa_j^(N)),

ZERO_N^extra(sigma)
  = sum_{d_N < j <= d_{N+2}} P_sigma(kappa_j^(N+2)),                 (C-5)
```

where `d_N = dim K_N = 2N-1`.

Then define the cumulative common packet

```text
ZERO_N^(<=m;common)(sigma)
  = sum_{j<=m} P_sigma(kappa_j^(N+2)) - sum_{j<=m} P_sigma(kappa_j^(N)).      (C-6)
```

The probe asks for the minimal `m` such that

```text
|ZERO_N^(<=m;common)(sigma)| >= theta |ZERO_N(sigma)|,               (C-7)
```

for thresholds `theta in {0.5, 0.9, 0.99}`.

## 3. Result: on the zeta side, the packet must be almost the whole common cloud

At `sigma = 1`, zeta gives:

```text
N= 8: dim=15, total=0.00441146, common=0.00388569, extra=5.26e-4,
      m50 = 13, m90 = none

N=10: dim=19, total=0.00311967, common=0.00281226, extra=3.07e-4,
      m50 = 16, m90 = 19

N=12: dim=23, total=0.00266839, common=0.00246967, extra=1.99e-4,
      m50 = 19, m90 = 23

N=14: dim=27, total=0.00209015, common=0.00195713, extra=1.33e-4,
      m50 = 23, m90 = 27

N=16: dim=31, total=0.00191376, common=0.00181878, extra=9.50e-5,
      m50 = 25, m90 = 30
```

So on the zeta side:

```text
to capture 50% of ZERO, the packet already needs about 80%-85% of the
full common cloud;

to capture 90% of ZERO, one needs essentially the entire common cloud.         (C-8)
```

This is not a thin cofinal packet in any reasonable sense.

## 4. Plant behaves differently, but does not rescue a packet reduction

At `sigma = 1`, the planted build gives:

```text
N= 8: dim=15, total=-0.187814, common=-0.213757, extra=0.025943, m50=1, m90=1
N=10: dim=19, total= 0.008731, common=-0.006896, extra=0.015628, m50=1, m90=1
N=12: dim=23, total= 0.012073, common= 0.000427, extra=0.011645, m50=1, m90=none
N=14: dim=27, total= 0.007364, common=-0.001189, extra=0.008553, m50=8, m90=none
N=16: dim=31, total= 0.007745, common= 0.001087, extra=0.006658, m50=none, m90=none
```

The planted side is structurally unstable in a different way:

```text
- sometimes the first root already dominates the total;
- sometimes the common cloud has the wrong sign and the extra four roots carry
  most of the total;
- sometimes no common-prefix packet reaches even 50% of |ZERO|.               (C-9)
```

So the planted side also rejects any clean packet law, just for a different
reason than zeta.

## 5. Consequence

The stronger packet-level reduction is now also gone.

What E79.2 showed:

```text
not a fixed finite near-origin packet.                                         (C-10)
```

What this document adds:

```text
not even a narrow cofinal packet ordered by |kappa|.                           (C-11)
```

On the zeta side, the packet needed to capture a fixed fraction of `ZERO`
already occupies almost all of the common cloud; on the plant side, the packet
picture is unstable because the extra four roots and the common cloud compete
in sign and size.

Therefore the honest live E79.3 object is:

```text
a whole-cloud displacement estimate for ZERO_N,
possibly split into:
  common-cloud displacement + explicit extra-root contribution.                (C-12)
```

This is more precise than the previous README wording. It names the exact
decomposition that survives the packet autopsies.

## 6. Status

```text
proved by probe:
  on the zeta side, a packet ordered by |kappa| must already occupy almost the
  whole common cloud to capture a fixed fraction of ZERO;

proved by probe:
  the exact decomposition ZERO = common-cloud part + explicit extra-root part
  is the correct packet-level bookkeeping for N -> N+2;

observed:
  on the planted side, the extra-root contribution can dominate, and the common
  packet picture is not even sign-stable;

refuted:
  the hope that E79.3 can be reduced to a narrow cofinal packet of roots;

open:
  a genuine whole-cloud displacement theorem, or an explicit common-cloud +
  extra-root estimate from the secular equation;

next:
  reformulate E79.3 as a cloud-level statement and attack the extra-root term
  separately from the common-cloud displacement.
```
