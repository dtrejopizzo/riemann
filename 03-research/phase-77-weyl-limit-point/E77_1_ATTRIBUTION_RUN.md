# E77.1 - Attribution run

**Run:** 2026-07-18.

## 1. Statement

This run asks where the arithmetic discrimination first appears in the
Phase-76 endpoint.  On nested central sections of one maximum-size build,
measure

```text
S_N       = ||x_N||^2,
radius_N  = 1/S_N,
shellMass = (mass in the two outer coordinates at each end)/S_N,
ratio_N   = S_N/S_(N-1),
log S_k   = a_N + c_N k,  6 <= k <= N.
```

Here `x_N` is exactly the canonical bordered inner solution of P76.066.
The alternatives are:

```text
Outcome A: planted S_N also diverges, but much more slowly than zeta;
Outcome B: planted S_N saturates, so the plant produces an l2 bound state.
```

No ambient norm of a bordered inverse is measured.  The only injected
divisor data are the explicitly declared planted falsifiers.

## 2. Run specification

```text
builder:   P76_002_mp_entry_audit.build_mp
nesting:   one N=16 build per case, central principal sections N=6,...,16
lambda:    6
dps:       50
gamma:     14.134725141734693790
strength:  5.0
beta:      0.10, 0.20, 0.30, 0.40
shell:     width 2 at both ends of the canonical inner solution
```

Command:

```bash
python3 E77_1_attribution_probe.py --max-modes 16 --dps 50
```

The machine-readable complete output is in
`E77_1_attribution_results.json` and `E77_1_attribution_results.tsv`.

## 3. Complete numerical table

`c_N` is the least-squares slope using all rows from 6 through `N`.

### zeta

| N | S_N | 1/S_N | shellMass | ratio | c_N |
|---:|---:|---:|---:|---:|---:|
| 6 | 1.0622022e+07 | 9.4144036e-08 | 1.6555496e-03 | - | - |
| 7 | 1.1217991e+09 | 8.9142519e-10 | 9.8779040e-05 | 1.0561070e+02 | - |
| 8 | 1.1507286e+13 | 8.6901464e-14 | 3.5269422e-06 | 1.0257885e+04 | 6.9477808 |
| 9 | 2.5916378e+12 | 3.8585639e-13 | 5.2324309e-08 | 2.2521712e-01 | 4.6450416 |
| 10 | 5.0460433e+13 | 1.9817507e-14 | 1.4558984e-11 | 1.9470480e+01 | 3.8492653 |
| 11 | 4.5158592e+15 | 2.2144180e-16 | 4.7946934e-11 | 8.9493073e+01 | 3.7140286 |
| 12 | 1.6815742e+21 | 5.9468087e-22 | 3.4810881e-12 | 3.7237082e+05 | 4.6421888 |
| 13 | 1.9170442e+19 | 5.2163639e-20 | 4.9386705e-14 | 1.1400295e-02 | 4.2692301 |
| 14 | 5.4860456e+21 | 1.8228066e-22 | 1.9138637e-18 | 2.8617210e+02 | 4.1876736 |
| 15 | 2.6080226e+22 | 3.8343226e-23 | 1.9422471e-17 | 4.7539208 | 4.0027701 |
| 16 | 5.1279177e+23 | 1.9501093e-24 | 8.5946028e-20 | 1.9662090e+01 | 3.8553646 |

### planted beta=0.10

| N | S_N | 1/S_N | shellMass | ratio | c_N |
|---:|---:|---:|---:|---:|---:|
| 6 | 2.4636595e+01 | 4.0590024e-02 | 6.7342474e-01 | - | - |
| 7 | 2.0340987e+01 | 4.9161822e-02 | 6.8224482e-01 | 8.2564117e-01 | - |
| 8 | 1.9679001e+02 | 5.0815587e-03 | 9.2177102e-01 | 9.6745554 | 1.0389521 |
| 9 | 5.9995502e-01 | 1.6667916 | 7.0194210e-01 | 3.0487067e-03 | -8.8759014e-01 |
| 10 | 5.2316497 | 1.9114430e-01 | 5.3160766e-01 | 8.7200699 | -6.6225511e-01 |
| 11 | 1.4320163e+01 | 6.9831606e-02 | 5.1801703e-01 | 2.7372175 | -3.5941696e-01 |
| 12 | 6.0851066e+03 | 1.6433566e-04 | 1.2344234e-01 | 4.2493276e+02 | 4.3566966e-01 |
| 13 | 2.1340306e+02 | 4.6859685e-03 | 3.1893013e-02 | 3.5069732e-02 | 4.5144854e-01 |
| 14 | 6.7363079e+02 | 1.4844927e-03 | 1.0192014e-02 | 3.1566127 | 5.0534875e-01 |
| 15 | 8.4977936e+01 | 1.1767761e-02 | 7.4018976e-03 | 1.2614913e-01 | 3.9229944e-01 |
| 16 | 1.6099723e+03 | 6.2112871e-04 | 4.8407095e-03 | 1.8945768e+01 | 4.4651259e-01 |

### planted beta=0.20

| N | S_N | 1/S_N | shellMass | ratio | c_N |
|---:|---:|---:|---:|---:|---:|
| 6 | 3.4728428e-01 | 2.8794854 | 7.3282050e-01 | - | - |
| 7 | 2.7639702e-01 | 3.6179841 | 8.0610222e-01 | 7.9588116e-01 | - |
| 8 | 1.2873919e+02 | 7.7676425e-03 | 9.1668780e-01 | 4.6577634e+02 | 2.9577001 |
| 9 | 7.1565750e-01 | 1.3973165 | 6.4025656e-01 | 5.5589716e-03 | 8.3128795e-01 |
| 10 | 5.8640044 | 1.7053193e-01 | 4.9147719e-01 | 8.1938699 | 6.6042520e-01 |
| 11 | 1.5538844e+01 | 6.4354852e-02 | 4.9213794e-01 | 2.6498691 | 6.5647656e-01 |
| 12 | 8.3956975e+02 | 1.1910863e-03 | 1.1429594e-01 | 5.4030387e+01 | 1.0121810 |
| 13 | 7.6332336e+01 | 1.3100608e-02 | 3.0591579e-02 | 9.0918397e-02 | 8.7622666e-01 |
| 14 | 2.5151285e+04 | 3.9759401e-05 | 7.4951314e-03 | 3.2949712e+02 | 1.1408707 |
| 15 | 7.8339039e+01 | 1.2765028e-02 | 7.4336906e-03 | 3.1147132e-03 | 8.9855374e-01 |
| 16 | 2.7013119e+02 | 3.7019050e-03 | 5.4831717e-03 | 3.4482321 | 7.8180394e-01 |

### planted beta=0.30

| N | S_N | 1/S_N | shellMass | ratio | c_N |
|---:|---:|---:|---:|---:|---:|
| 6 | 4.1749409e-01 | 2.3952435 | 8.4511920e-01 | - | - |
| 7 | 3.6967431e-01 | 2.7050839 | 7.6671252e-01 | 8.8545997e-01 | - |
| 8 | 5.1916581e+01 | 1.9261669e-02 | 8.3234943e-01 | 1.4043871e+02 | 2.4115616 |
| 9 | 8.1179905e-01 | 1.2318319 | 6.0211101e-01 | 1.5636604e-02 | 6.9397184e-01 |
| 10 | 6.2428033 | 1.6018445e-01 | 4.6430390e-01 | 7.6900846 | 6.1964589e-01 |
| 11 | 1.6466282e+01 | 6.0730164e-02 | 4.7535401e-01 | 2.6376423 | 6.4844412e-01 |
| 12 | 2.7990961e+02 | 3.5725819e-03 | 1.0952826e-01 | 1.6998957e+01 | 8.9280505e-01 |
| 13 | 6.7947200e+01 | 1.4717310e-02 | 3.1252154e-02 | 2.4274693e-01 | 8.0224369e-01 |
| 14 | 3.0092608e+03 | 3.3230752e-04 | 8.2368411e-03 | 4.4288224e+01 | 9.5921340e-01 |
| 15 | 8.9753306e+01 | 1.1141651e-02 | 7.9079972e-03 | 2.9825699e-02 | 7.9521990e-01 |
| 16 | 2.2033134e+02 | 4.5386189e-03 | 5.7256582e-03 | 2.4548549 | 7.1044379e-01 |

### planted beta=0.40

| N | S_N | 1/S_N | shellMass | ratio | c_N |
|---:|---:|---:|---:|---:|---:|
| 6 | 6.4094275e-01 | 1.5602017 | 6.1386763e-01 | - | - |
| 7 | 4.8768463e-01 | 2.0505055 | 6.4355823e-01 | 7.6088641e-01 | - |
| 8 | 3.3728770e+01 | 2.9648280e-02 | 7.6962858e-01 | 6.9161027e+01 | 1.9815832 |
| 9 | 8.7065294e-01 | 1.1485633 | 5.7776721e-01 | 2.5813362e-02 | 5.1553474e-01 |
| 10 | 6.3488562 | 1.5750869e-01 | 4.4872156e-01 | 7.2920631 | 5.1657541e-01 |
| 11 | 1.6699482e+01 | 5.9882096e-02 | 4.6557161e-01 | 2.6303135 | 5.8123384e-01 |
| 12 | 1.4109004e+02 | 7.0876726e-03 | 1.0907623e-01 | 8.4487672 | 7.7069613e-01 |
| 13 | 6.4622168e+01 | 1.5474566e-02 | 3.3335567e-02 | 4.5802077e-01 | 7.2034402e-01 |
| 14 | 6.9456091e+02 | 1.4397585e-03 | 1.0079459e-02 | 1.0748029e+01 | 8.0713825e-01 |
| 15 | 9.9228930e+01 | 1.0077706e-02 | 8.8096975e-03 | 1.4286570e-01 | 7.0116140e-01 |
| 16 | 2.0662727e+02 | 4.8396323e-03 | 6.1635398e-03 | 2.0823289 | 6.4482519e-01 |

## 4. Fit summary

| case | S_6 | S_16 | S_16/S_6 | c, N=6..16 | c, N=11..16 |
|---|---:|---:|---:|---:|---:|
| zeta | 1.06220e+07 | 5.12792e+23 | 4.82763e+16 | 3.85536 | 3.04628 |
| beta=0.10 | 2.46366e+01 | 1.60997e+03 | 6.53488e+01 | 0.44651 | 0.34135 |
| beta=0.20 | 3.47284e-01 | 2.70131e+02 | 7.77839e+02 | 0.78180 | 0.37028 |
| beta=0.30 | 4.17494e-01 | 2.20331e+02 | 5.27747e+02 | 0.71044 | 0.38136 |
| beta=0.40 | 6.40943e-01 | 2.06627e+02 | 3.22380e+02 | 0.64483 | 0.39704 |

For zeta, slopes on successive fixed windows are:

```text
N=6..10:  3.84927
N=8..12:  4.50631
N=10..14: 4.53621
N=11..16: 3.04628
```

Thus the fitted exponent is strongly positive but is not stable on the
available range.  Calling `c=3.85536` an asymptotic exponent would exceed
the evidence.

At selected common endpoints, the energy separation `S_N(zeta)/S_N(plant)`
is:

| N | beta=0.10 | beta=0.20 | beta=0.30 | beta=0.40 |
|---:|---:|---:|---:|---:|
| 12 | 2.76343e+17 | 2.00290e+18 | 6.00756e+18 | 1.19184e+19 |
| 14 | 8.14399e+18 | 2.18122e+17 | 1.82305e+18 | 7.89858e+18 |
| 16 | 3.18510e+20 | 1.89831e+21 | 2.32737e+21 | 2.48172e+21 |

The separation grows monotonically with beta at N=12 and N=16, but not
at N=14.  The candid finite-range statement is therefore that deeper
plants usually increase the endpoint separation, not that separation is
monotone in beta for every section.

## 5. Candid reading and verdict

1. Zeta has overwhelming contraction: `S_16=5.13e23` and
   `1/S_16=1.95e-24`.  Its energy is nonmonotone at N=9 and N=13, so the
   contraction exponent has not stabilized.
2. Every planted case has a positive full-range and tail slope.  Between
   N=6 and N=16, endpoint energy grows by factors from `65` to `778`.
   Also, all four shell masses fall to approximately `0.005`.  These facts
   weigh against clean saturation on this range.
3. The plant data remain violently oscillatory.  For example beta=0.20
   rises to `2.52e4` at N=14 and falls to `78.3` at N=15.  Neither a single
   endpoint nor an unconstrained log-linear fit distinguishes divergence
   from a resonant bounded sequence with large finite-section spikes.

**E77.1 verdict:** the observed evidence favors **Outcome A** (slow planted
divergence) over Outcome B, but the A/B attribution remains **ambiguous**
at N<=16.  Outcome B is not supported by a visible saturation plateau;
Outcome A is not established because no monotone envelope or stable
positive growth exponent is yet visible.

Consequently E77.7 is not licensed by this run.  The README's next
milestone under the provisional A reading is E77.2 (discrete
Koppelman-Pincus), but it remains gated by the following E77.1b check.

## 6. E77.1b required to disambiguate

Run nested sections through N=18 and, if feasible, N=20 at dps>=50, with:

```text
same four beta values and strength 5.0;
strength controls 2.5 and 10.0;
at least two additional lambda values;
even/odd subsequence fits and block minima over consecutive sections;
fits on fixed-width moving windows, with precision replication at dps 70;
the independent DH-type build from the phase-61 cache.
```

Decision rule: A requires increasing even and odd lower envelopes (or a
stable positive block-minimum exponent) across the enlarged range.  B
requires a stable bounded envelope under increased N and precision, not
merely another downward oscillation.

## 7. Status

```text
proved:    no LP or IDENT theorem is proved by this numerical run;
observed:  zeta S_N reaches 5.13e23 and radius reaches 1.95e-24 at N=16;
observed:  all planted full/tail fits are positive and shellMass falls,
           favoring A over B on the measured range;
observed:  the zeta contraction exponent is not stable in N;
observed:  beta separation is monotone at N=12 and N=16, not at N=14;
open:      asymptotic divergence versus saturation of planted S_N;
open:      LP, IDENT, and the radical-tail estimates;
verdict:   A favored but ambiguous; execute E77.1b before E77.2;
probe:     E77_1_attribution_probe.py, dps 50, nested N=6..16.
```
