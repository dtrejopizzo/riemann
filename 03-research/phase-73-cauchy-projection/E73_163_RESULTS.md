# E73.163 results - canonical coefficient-defect audit

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_163_canonical_coeff_defect_probe.py
```

Output:

```text
E73.163 canonical coefficient-defect probe
Uses one cauchy0 column per critical node; source coefficients are exact Pi entries.
 lam     L   dim sR     sCond aR pR     pCond imageRel srcChk principal coeffRel endpoint cauchy0      rat   meshRel   expPair
   8   4.159    25 15   6.8e+09  7  6   4.0e+06  4.0e-06 9.8e-17   9.8e-02  9.8e-02  5.8e-03  9.8e-02  1.8e-03   9.0e-01   3.2e-10
   8   4.159    25 15   6.8e+09  7  6   4.0e+06  4.0e-06 5.0e-17   5.9e-01  5.9e-01  1.4e-02  5.9e-01  1.6e-03   3.0e+00   3.9e-12
   8   4.159    25 15   6.8e+09  7  6   4.0e+06  4.0e-06 1.4e-16   6.2e-01  6.2e-01  9.9e-03  6.2e-01  2.0e-03   2.8e+00   9.0e-09
  10   4.605    29 16   4.7e+09  7  7   3.0e+08  1.9e-07 1.1e-16   2.1e-01  2.1e-01  3.5e-03  2.1e-01  2.3e-03   2.1e+00   5.0e-11
  10   4.605    29 16   4.7e+09  7  7   3.0e+08  1.9e-07 6.2e-17   6.1e-01  6.1e-01  8.5e-03  6.1e-01  2.0e-03   7.1e+00   4.5e-13
  10   4.605    29 16   4.7e+09  7  7   3.0e+08  1.9e-07 1.5e-16   2.9e-01  2.9e-01  4.1e-03  2.9e-01  2.7e-03   4.0e+00   8.6e-10
  12   4.970    33 17   8.3e+09  7  7   1.8e+09  1.8e-06 9.9e-17   2.0e-01  2.0e-01  4.3e-04  2.0e-01  2.2e-03   7.4e-01   3.0e-11
  12   4.970    33 17   8.3e+09  7  7   1.8e+09  1.8e-06 1.8e-16   7.5e-01  7.5e-01  8.2e-04  7.5e-01  1.5e-03   2.7e+00   3.2e-13
  12   4.970    33 17   8.3e+09  7  7   1.8e+09  1.8e-06 1.4e-16   6.0e-01  6.0e-01  5.6e-04  6.0e-01  1.6e-03   1.1e+00   1.1e-09
  14   5.278    37 17   7.0e+09  8  8   7.2e+09  9.5e-06 9.8e-17   4.8e-01  4.8e-01  2.1e-03  4.8e-01  3.5e-03   1.3e+00   6.3e-10
  14   5.278    37 17   7.0e+09  8  8   7.2e+09  9.5e-06 1.6e-16   6.5e-01  6.5e-01  1.3e-03  6.5e-01  2.1e-03   3.8e+00   1.0e-11
  14   5.278    37 17   7.0e+09  8  8   7.2e+09  9.5e-06 1.3e-16   5.9e-01  5.9e-01  3.1e-03  5.9e-01  2.6e-03   1.1e+00   1.9e-08
  16   5.545    41 17   6.4e+09  8  8   4.8e+08  1.8e-04 1.0e-16   1.3e-01  1.3e-01  2.9e-02  1.3e-01  2.0e-03   3.0e+01   8.1e-10
  16   5.545    41 17   6.4e+09  8  8   4.8e+08  1.8e-04 1.7e-16   7.1e-01  7.1e-01  6.3e-02  7.1e-01  3.4e-03   9.2e+01   1.2e-11
  16   5.545    41 17   6.4e+09  8  8   4.8e+08  1.8e-04 1.4e-16   6.6e-01  6.7e-01  3.2e-02  6.6e-01  2.3e-03   4.7e+01   2.7e-08
```

Reading:

```text
1. `srcChk` is machine-size, so the canonical coefficients really represent
   the source exactly.

2. The principal coefficient residual is large: `principal` and `cauchy0`
   are often 0.2--0.7.  Thus the strong coefficient-image theorem from
   E73.162 is false in canonical coordinates.

3. The endpoint and higher rational residuals are small by comparison:
   endpoint about 4e-4--6e-2 and rat about 1e-3--4e-3.

4. The scalar weighted pairing `expPair` remains tiny.  The obstruction is
   therefore not endpoint clutter; it is a canonical cauchy0 scalar
   cancellation.
```

Conclusion:

```text
E73.162's small coefficient residual was caused by redundant r=0 coordinates.
After canonicalization, the remaining theorem is exactly scalar smallness of
the canonical cauchy0 defect.
```

