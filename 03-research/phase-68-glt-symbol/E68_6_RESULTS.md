# E68.6 -- auditing the audit: the detector is gauge-FRAGILE, not broken

**Date:** 2026-07-07.
**Script:** [E68_6_audit_the_audit.py](E68_6_audit_the_audit.py).
**Role:** re-audit E68.5's "false negatives" claim -- was it a detector failure or an artifact of the
naive full-band average (edge contamination)?

## Finding (min of sigma_A - sigma_P for zeta; ground truth ind_- = 0)

```
          trim0     trim4
t0=30    -1.461    -0.692   (still negative)
t0=50    -3.975    -1.687   (still negative)
t0=100   +0.040    -0.001   (-> ~0, marginal)
t0=200   +0.050    -0.000   (-> ~0, marginal)
t0=400   -5.806    -2.453   (still negative)
```

## Balanced conclusion (correcting both E68.5 and the reflex)

- Edge contamination is real but **secondary**: trimming corners reduces the negatives (e.g. -5.8 ->
  -2.5) but does NOT remove them at t0=30,50,400. So E68.5 was not pure artifact.
- But the detector is **not broken**: at t0=100,200 the clean (trimmed) margin is `~ 0` -- zeta
  correctly TOUCHES zero (marginal). The earlier `+0.04` was partly edge-inflation; the honest value is
  a touch at 0, which is *more* consistent with the de Branges marginality.

So the honest status is: the band symbol is **gauge-fragile, not gauge-uniform**. It is faithful where
the non-Toeplitz part is benign (t0~100,200: marginal 0, correct) and unreliable where it is not
(t0=30,50,400). Root cause: the operator is not Toeplitz.

## Net for the program

```
robust, gauge-uniform : ind_-(A_N - P_lambda) = 0 <=> RH   (E67.9; the real object)
faithful at some gauges: band symbol sigma_A - sigma_P (validated at t0~100; fragile elsewhere)
retracted             : "symbol >= 0 for all gauges" as a rigorous reformulation
```

The foundations detector doc is re-scoped (gauge-fragile, use at validated gauges; robust statement =
exact index). Phase 68 closes here: the symbol gave a genuine local picture (Omega_7 = envelope vs
prime peak near theta~pi/2, marginal touch) but is not a gauge-uniform object. Phase 69 returns to the
gauge-robust exact signed index as the object for the forcer.
