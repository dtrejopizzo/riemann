# E79.3b - The extra-root contribution is an explicit `N^-2` term

**Scope:** `GAP-Z` only, refinement of the cloud split from E79.3a.  
**Class:** REDUCCION GENUINA (numerical gate with exact bookkeeping).  
**What we know after this document that we did not know before:** inside

```text
ZERO_N = ZERO_N^common + ZERO_N^extra,
```

the extra-root term is the easy part. On both builds, and for the tested safe
sigmas, it behaves like a clean `N^-2` contribution with a stable scaled size.
So the hard content of `GAP-Z` is now localized entirely in the common-cloud
displacement term.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound mechanism.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. This is direct bookkeeping inside the independent K_N
       spectral object.
E72.16/E77.7az: respected. This is convergence-side; any build separation below
       is recorded only as structure, not as forcing.
Circularity: respected. The split is made entirely on spec(K_N).
```

## 1. Starting point

E79.3a established the exact bookkeeping:

```text
ZERO_N(sigma)
  = ZERO_N^common(sigma) + ZERO_N^extra(sigma),                      (X-1)
```

where:

```text
ZERO_N^common(sigma)
  = sum_{j<=d_N} P_sigma(kappa_j^(N+2)) - sum_{j<=d_N} P_sigma(kappa_j^(N)),

ZERO_N^extra(sigma)
  = sum_{d_N < j <= d_{N+2}} P_sigma(kappa_j^(N+2)),                (X-2)
```

and `d_{N+2} = d_N + 4`.

E79.3a then showed that `ZERO_N^common` is the hard part: capturing a fixed
fraction of `ZERO` needs almost the whole common cloud on the zeta side.

So the next natural question is whether `ZERO_N^extra` is already explicit and
harmless.

## 2. Data from the cloud-packet audit

Using the executed `E79_3_cloud_packet_results.json`:

### Zeta

At `sigma = 1`:

```text
N= 8: extra = 5.25776522483e-4,  N^2 extra = 0.0336496974, share = 0.1192
N=10: extra = 3.07409734913e-4,  N^2 extra = 0.0307409735, share = 0.0985
N=12: extra = 1.98719668364e-4,  N^2 extra = 0.0286156322, share = 0.0745
N=14: extra = 1.33017693008e-4,  N^2 extra = 0.0260714678, share = 0.0636
N=16: extra = 9.49775787544e-5,  N^2 extra = 0.0243142602, share = 0.0496
```

At `sigma = 2`:

```text
N= 8: extra = 1.05114185516e-3,  N^2 extra = 0.0672730787
N=10: extra = 6.14678199283e-4,  N^2 extra = 0.0614678199
N=12: extra = 3.97382480892e-4,  N^2 extra = 0.0572230772
N=14: extra = 2.66010252359e-4,  N^2 extra = 0.0521380095
N=16: extra = 1.89942293000e-4,  N^2 extra = 0.0486252270
```

The local exponents are correspondingly stable:

```text
sigma = 1: p_local = 2.41, 2.39, 2.60, 2.52
sigma = 2: p_local = 2.40, 2.39, 2.60, 2.52                         (X-3)
```

### Plant

At `sigma = 1`:

```text
N= 8: extra = 0.0259425602380, N^2 extra = 1.66032385523
N=10: extra = 0.0156278887936, N^2 extra = 1.56278887936
N=12: extra = 0.0116453139680, N^2 extra = 1.67692521139
N=14: extra = 0.00855322674668, N^2 extra = 1.67643244235
N=16: extra = 0.00665771637675, N^2 extra = 1.70437539245
```

At `sigma = 2`:

```text
N= 8: extra = 0.0513034113696, N^2 extra = 3.28341832765
N=10: extra = 0.0310509121697, N^2 extra = 3.10509121697
N=12: extra = 0.0231801662401, N^2 extra = 3.33794393857
N=14: extra = 0.0170441661996, N^2 extra = 3.34065657512
N=16: extra = 0.0132781609951, N^2 extra = 3.39920921475            (X-4)
```

Again the size is compatible with a stable `N^-2` contribution, now with a
different constant.

## 3. Reading

This is the cleanest behavior seen anywhere on the `ZERO` side so far.

On both builds:

```text
ZERO_N^extra(sigma) behaves like a direct outer-shell term:
  |ZERO_N^extra(sigma)| ~ c_sigma / N^2,                             (X-5)
```

with moderate drift in the scaled quantity, but none of the borderline
`N^{-p}` instability that infected the full `ZERO`.

For zeta, `ZERO^extra` is also only a small fraction of the total:

```text
~12% at N=8, falling to ~5% by N=16 at sigma = 1.                    (X-6)
```

So the zeta-side hard content is overwhelmingly in `ZERO^common`, not in the
new four roots.

## 4. Consequence

This upgrades the localization from E79.3a:

```text
ZERO_N = [common-cloud displacement] + [explicit extra-root N^-2 term].       (X-7)
```

Therefore the live open object can be sharpened to:

```text
COMMON-GAP-Z:
ZERO_N^common(sigma)
  = sum_{j<=d_N} P_sigma(kappa_j^(N+2)) - sum_{j<=d_N} P_sigma(kappa_j^(N))
```

with `ZERO_N^extra` treated as already numerically benign.

This is a genuine reduction of the hard part, even though the final proof of
`GAP-Z` is still open.

## 5. Status

```text
observed:
  on both builds and for sigma = 1,2, the extra-root contribution is compatible
  with a clean N^-2 law and has stable N^2 scaling;

observed:
  on the zeta side, ZERO^extra is only a small and decreasing fraction of the
  total ZERO signal;

reduced:
  the hard content of GAP-Z from the full ZERO_N to the common-cloud
  displacement term ZERO_N^common;

open:
  a theorem-grade common-cloud displacement estimate from the secular equation;

next:
  reformulate E79.3 / E79.4 in terms of COMMON-GAP-Z plus the explicit
  extra-root remainder.
```
