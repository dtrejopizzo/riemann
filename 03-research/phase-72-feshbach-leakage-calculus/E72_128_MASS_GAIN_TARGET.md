# E72.128 -- Mass gain target

**Date:** 2026-07-09.
**Role:** isolate the final scalar estimate left by the minimal mass gate.

## 0. Minimal endpoint

By E72.127, after the Cauchy tail and bounded flux estimates, the only remaining post-main estimate is:

```text
MG:
sup_{tau_j<=T}|m_xY_x(tau_j)| -> 0.
```

Here:

```text
m_x
 = 1_H^TW_HB_xC_E^(-1)B_x^*P_H(2/(L sqrt(x)))L_{k_x},
```

and `Y_x(tau_j)` is the finite post-main packet.

Equivalently:

```text
m_xY_x(tau_j)
 = 1_H^TW_HB_xC_E^(-1)B_x^*P_HZ_x^{pm}(tau_j),
```

the total mass of the shorted post-main cofactor.

## 1. Exact target

The new pure statement is:

```text
Mass gain:
1_H^TW_HB_xC_E^(-1)B_x^*P_HZ_x^{pm}(tau_j) -> 0             (MG)
```

uniformly for finite root-height windows.

This is not a general prime-discrepancy estimate.  It is the zero-frequency leakage after the full
chain:

```text
post-main endpoint discrepancy
-> integrated Loewner commutator L_{k_x}
-> projection to the Feshbach complement
-> shorting by C_E^(-1)
-> even physical-band mass.
```

## 2. Expected scale

The raw norm estimate gives only:

```text
||m_x||||Y_x|| = O(1),
```

which is not enough.  The data instead show a genuine mass gain:

```text
|m_xY_x(tau_j)| = o(1).
```

The plausible finite theorem is a logarithmic gain:

```text
|m_xY_x(tau_j)| = O(1/L).                                  (LMG)
```

This is exactly the amount needed by E72.127, and is weaker than the bad-subspace projection
orthogonality of E72.116.

## 3. Diagnostic

The companion script:

```text
E72_128_mass_gain_scale_probe.py
```

reports:

```text
max|mass|,
L max|mass|,
L^2 max|mass|,
max mass/(||m||||Y||),
||m||sqrt(x)L.
```

Representative output:

```text
E72.128 mass gain scale probe
 lam   L roots  max|mass|   L*mass   L^2*mass  mass/(||m||||Y||)  ||m||sqrtxL
   6  3.58     3  9.332e-02 3.344e-01  1.198e+00         1.285e-01    4.210e-01
   8  4.16     4  4.973e-02 2.068e-01  8.601e-01         8.404e-02    3.639e-01
  10  4.61     3  4.051e-02 1.865e-01  8.591e-01         8.166e-02    2.843e-01
  12  4.97     4  2.100e-02 1.044e-01  5.186e-01         3.939e-02    2.935e-01
  14  5.28     4  1.601e-02 8.450e-02  4.460e-01         5.199e-02    1.748e-01
  16  5.55     5  1.688e-02 9.360e-02  5.190e-01         4.889e-02    1.680e-01
```

The data are compatible with at least `(LMG)` and possibly with the stronger scale
`|m_xY_x(tau_j)|=O(L^(-2))` in these windows.

## 4. Status

```text
proved: scalar WRL now needs only MG beyond CGE-K and ROP;
reduced: MG is the mass of the shorted post-main cofactor;
open:   prove the logarithmic mass gain LMG from the finite CCM root equation.
```
