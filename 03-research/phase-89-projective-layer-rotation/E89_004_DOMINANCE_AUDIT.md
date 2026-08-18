# E89.004 - Endpoint dominance audit

## 1. Exact residue decomposition at the endpoint

At `z=i`, decompose the endpoint numerator into the nearest even and odd
spectral residues.  The multiprecision values are

```text
outer modes  even resonant term              odd resonant term
4            3.73e1+2.61e2 i                -4.07e1+5.80 i
6            1.28e3+1.34e4 i                -1.20e3+1.14e2 i
8            1.24e6+1.75e7 i                -1.23e6+8.76e4 i.        (1.1)
```

The magnitude ratios `odd/even` are approximately

```text
0.156,
0.090,
0.070.                                                (1.2)
```

The regular complement changes the displayed sum but not the observed
dominant parity.

## 2. Reading

The absolute resonant terms grow rapidly, while the odd-to-even projective
ratio decreases.  This is exactly the situation covered by E89.001:
absolute cascade size is irrelevant once a single residue dominates the
normalized safe profile.

The table is not a proof of cofinal dominance.  It supplies a falsifiable
quantitative target:

```text
DOM-E:
sup_{z in K}
 |lambda_E R(z)
   /[(h_z^eff p_E)(p_E^Tb^eff)]| ->0                 (2.1)
```

on every safe compact `K`, together with one derivative and a nonvanishing
condition for the dominant profile.

## 3. Final endpoint-layer ledger

```text
proved algebraically:
  nested parity Feshbach structure;
  scalar eigenvalue cancellation;
  scalar boundary-overlap cancellation;
  lifted-line rotation current, including Schur-row transport;

supported by the endpoint audit:
  even projective dominance;

open:
  DOM-E;
  matched-width existence;
  PROFILE-ROTATION-RDI.
```
