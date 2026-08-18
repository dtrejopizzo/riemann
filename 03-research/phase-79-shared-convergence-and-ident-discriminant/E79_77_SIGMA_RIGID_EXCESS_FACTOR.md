# E79.77 - The frontier mismatch is carried by a sigma-rigid excess factor

**Scope:** `GAP-Z` only, mesoscopic collapse behind the E79.76 ratio rule.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** on the
genuine tradeoff rows, each frontier candidate carries an almost sigma-rigid
signed excess factor relative to `ZERO^extra`. So the frontier mismatch is not
an arbitrary two-sigma max; it is already the absolute value of one mesoscopic
scalar.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Pure bookkeeping on E79.69/E79.76 packet data.
E72.16/E77.7az: respected. Convergence-side structure only.
Circularity: respected. No endpoint identity is imported.
```

## 1. Starting point

E79.76 reduced the genuine tradeoff rows to a scalar law on the 2-point
frontier:

```text
choose the higher-surcharge point iff Delta_mismatch / Delta_surcharge > 1.  (77-1)
```

The next candid question is whether `Delta_mismatch` itself already comes from
one simpler quantity.

For a frontier candidate `S`, define its signed excess factor against the
reconstructed `ZERO^extra` target by

```text
eps_sigma(S) := packet_sigma(S) / extra_sigma - 1.                        (77-2)
```

If `eps_1(S)` and `eps_2(S)` are essentially the same number, then the two-sigma
mismatch has already collapsed to

```text
mismatch(S) = |eps(S)| + o(1),                                            (77-3)
```

with one mesoscopic scalar `eps(S)`.

## 2. Probe

Companion files:

```text
E79_77_sigma_rigid_excess_factor_probe.py
E79_77_sigma_rigid_excess_factor_results.json
```

The probe reconstructs the same `ZERO^extra` values used in E79.69 and, on the
E79.76 frontier rows, records for each candidate:

```text
- eps_1  = packet_sigma1 / extra_sigma1 - 1,
- eps_2  = packet_sigma2 / extra_sigma2 - 1,
- rigidity defect = |eps_1 - eps_2|.                                     (77-4)
```

## 3. Result

On every genuine tradeoff row, the frontier candidates are already sigma-rigid
to high accuracy:

```text
N=10:
  pair   eps_1 = 0.02896, eps_2 = 0.03000
  suffix eps_1 = 0.00739, eps_2 = 0.00682

N=12:
  triple eps_1 = 0.54730, eps_2 = 0.54719
  pair   eps_1 = 0.02353, eps_2 = 0.02372

N=16:
  triple eps_1 = 0.70561, eps_2 = 0.70564
  pair   eps_1 = 0.03606, eps_2 = 0.03607.                               (77-5)
```

So the rigidity defect is tiny:

```text
|eps_1 - eps_2| <= about 1e-3 on the mild row N=10,
|eps_1 - eps_2| <= about 2e-4 on N=12,
|eps_1 - eps_2| <= about 3e-5 on N=16.                                   (77-6)
```

In particular, each frontier candidate is already described by one signed
overshoot scalar:

```text
packet_sigma(S) ~= (1 + eps(S)) extra_sigma                              (77-7)
```

simultaneously at both audited sigmas.

## 4. Reading

This is the missing mesoscopic collapse behind E79.76.

The frontier mismatch is not best thought of as a max over two unrelated safe
samples. On the tradeoff rows it is already measuring one sigma-rigid excess
factor:

```text
mismatch(S) ~= |eps(S)|.                                                 (77-8)
```

So `Delta_mismatch` itself is approximately

```text
Delta_mismatch ~= |eps(L)| - |eps(H)|,                                   (77-9)
```

with `eps` intrinsic to the packet, not to the sampled sigma.

This is exactly the kind of collapse we needed: one mesoscopic scalar is now
carrying the whole mismatch side of the frontier rule.

## 5. Consequence

After E79.77 the live selector is cleaner again:

```text
1. reduce to the 2-point frontier;
2. attach to each point one sigma-rigid excess scalar eps(S);
3. choose the higher-surcharge point iff the reduction in |eps| pays for the
   extra surcharge at unit rate.                                         (77-10)
```

So the open burden is no longer to explain `Delta_mismatch` as a two-sigma
artifact. The real burden is now:

```text
why the common-cloud / extra-root coupling trades reduction in |eps|
against surcharge at exchange rate 1.                                    (77-11)
```

## 6. Status

```text
proved by probe:
  on the genuine frontier rows, each candidate already has an almost
  sigma-independent signed excess factor eps relative to ZERO^extra;

reduced:
  the mismatch side of E79.76 from a two-sigma max to one mesoscopic scalar
  |eps(S)| attached to each frontier packet;

clarified:
  Delta_mismatch is approximately the drop in |eps| across the frontier;

open:
  derive the unit exchange rate between |eps|-reduction and surcharge cost;

next:
  inspect whether the surcharge increment itself can also be written as the
  change of a packet-level excess/complexity scalar, so that E79.76 becomes a
  one-variable balance law.
```
