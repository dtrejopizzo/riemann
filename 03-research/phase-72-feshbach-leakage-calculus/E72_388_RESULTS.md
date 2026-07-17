# E72.388 Results - SFREQ second variation

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_388_sfreq_second_variation_probe.py
```

## Output

```text
E72.388 SFREQ second-variation probe
 lam    L      V2          V2scaled    T=e^L      V2/T
   6   3.584   4.497e+01   3.885e-02       36.0   1.249e+00
   8   4.159   2.323e+02   7.650e-02       64.0   3.630e+00
  10   4.605   5.577e+02   9.050e-02      100.0   5.577e+00
  12   4.970   5.740e+02   5.338e-02      144.0   3.986e+00
  14   5.278   1.452e+03   8.542e-02      196.0   7.409e+00
```

## Reading

The scaled second variation

```text
V2 / (e^((c+sigma)L)L^3)
```

stays stable in the tested windows.  This supports `SV-K` from E72.388 with a small polynomial power.

At height `T=e^L`, `V2/T` is already only polynomial-size.  At the theorem-level height

```text
T=e^L L^A,
```

the extra factor `L^A` absorbs this contribution.

## Status

```text
validated: second-variation scale for the actual packet;
validated: natural-height SFREQ tail is polynomial and can be damped by L^A;
proved in E72.388: SFREQ follows from SV-K;
open: prove D2BV-K/SV-K uniformly from packet identities.
```
