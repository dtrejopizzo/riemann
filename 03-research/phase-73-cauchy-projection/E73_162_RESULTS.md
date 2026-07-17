# E73.162 results - coefficient-defect smoke test

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_162_coeff_defect_probe.py
```

Purpose:

```text
Test the COEFF-DEF formulation from E73.162 in finite coordinates.
```

The script does not use ambient source projection as the theorem.  It builds:

```text
P_{A,K}:      fixed primitive rational basis, r=0,1,2 plus d^2 Cauchy terms;
S_{A,K}:      fixed source rational basis, r=0,1,2,3 plus d^2,d^4 Cauchy terms;
B_L(A,K):     coefficient action obtained by expressing (H_L-mu_L I)P_{A,K}
              in S_{A,K};
s_A:          source coefficient vector for S_A.
```

Then it measures:

```text
imageRel  = how well (H-mu)P lands in S_{A,K};
coeffRel  = coefficient residual of s_A against Image B_L;
meshRel   = ambient mesh residual after lifting the coefficient primitive;
expPair   = e^(alpha L)|<xi,residual>|.
```

Output:

```text
E73.162 coefficient-defect smoke test
Builds coefficient action B_L by expressing (H-mu)P in the fixed rational source basis.
This is a numerical coordinate test, not the symbolic partial-fraction proof.
 lam     L   dim sRank     sCond aRank     aCond imageRel       bRe srcCoord   coeffRel    meshRel    expPair
   8   4.159    25    15   6.8e+09     7   2.2e+09  4.0e-06    0.200  4.8e-12    2.1e-07    6.3e-04    2.7e-10
   8   4.159    25    15   6.8e+09     7   2.2e+09  4.0e-06    0.200  3.5e-12    1.0e-05    3.5e-02    3.9e-12
   8   4.159    25    15   6.8e+09     7   2.2e+09  4.0e-06    0.200  8.8e-12    7.9e-06    3.4e-02    9.1e-09
  10   4.605    29    16   4.7e+09     7   1.9e+08  1.9e-07    0.200  5.2e-12    5.4e-07    8.1e-04    2.8e-11
  10   4.605    29    16   4.7e+09     7   1.9e+08  1.9e-07    0.200  2.7e-12    2.2e-05    4.7e-02    4.4e-13
  10   4.605    29    16   4.7e+09     7   1.9e+08  1.9e-07    0.200  1.6e-12    2.0e-05    3.7e-02    8.7e-10
  12   4.970    33    17   8.3e+09     7   1.1e+09  1.8e-06    0.200  1.4e-11    1.9e-07    1.4e-03    2.8e-11
  12   4.970    33    17   8.3e+09     7   1.1e+09  1.8e-06    0.200  2.0e-12    1.0e-05    7.3e-02    3.3e-13
  12   4.970    33    17   8.3e+09     7   1.1e+09  1.8e-06    0.200  6.0e-12    1.0e-05    7.6e-02    1.2e-09
  14   5.278    37    17   7.0e+09     8   7.0e+09  9.5e-06    0.200  1.5e-11    3.1e-06    1.7e-03    6.3e-10
  14   5.278    37    17   7.0e+09     8   7.0e+09  9.5e-06    0.200  1.0e-11    1.4e-04    8.7e-02    1.0e-11
  14   5.278    37    17   7.0e+09     8   7.0e+09  9.5e-06    0.200  4.0e-12    1.1e-04    7.5e-02    1.9e-08
  16   5.545    41    17   6.4e+09     8   4.7e+08  1.8e-04    0.200  2.0e-10    4.3e-07    1.8e-03    8.2e-10
  16   5.545    41    17   6.4e+09     8   4.7e+08  1.8e-04    0.200  1.5e-10    2.4e-05    8.5e-02    1.2e-11
  16   5.545    41    17   6.4e+09     8   4.7e+08  1.8e-04    0.200  3.7e-10    2.0e-05    9.0e-02    2.7e-08
```

Reading:

```text
1. The source itself is represented in the fixed source basis to machine
   precision: srcCoord is about 1e-12--1e-10.

2. The coupled action (H-mu)P lands in the source basis with imageRel
   about 1e-7--1e-4 on these small windows.  This reproduces the finite-width
   LOCAL-FIN signal from E73.016.

3. The coefficient source residual against Image B_L is small:
   coeffRel is about 1e-7--1e-4.

4. The ambient mesh residual can be much larger, up to about 9e-2.  This is
   not a contradiction; the source/source-action bases are ill-conditioned
   and contain xi-invisible components.  It confirms why ambient norm image
   membership was the wrong theorem.

5. The scalar residual expPair remains tiny in the tested rows, matching the
   E73.020/E73.158 scalar-invisible image observations.
```

Status:

```text
validated numerically: coefficient-level source-in-image is plausible;
not proved: B_L was computed by mesh least squares, not symbolic partial fractions;
next: construct B_L by exact rational partial-fraction identities and separate
      endpoint slots before any mesh projection.
```

