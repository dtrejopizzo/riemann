# E73.166 results - projector moment audit

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_166_projector_moment_probe.py
```

Output:

```text
E73.166 projector moment probe
Compares Ker(T_L) with simple two-dimensional moment spaces.
 lam     L    null_svals                 best      resid  prevKer  prevRan    all
   8   4.159        6.1e-06,4.5e-09   1,phase  5.95e-01      nan      nan 1,phase:5.95e-01 1,1/g:6.00e-01 1,g:6.74e-01 1,cg:6.74e-01
  10   4.605        7.9e-06,1.4e-09     1,1/g  3.47e-01 5.83e-01 4.76e-01 1,1/g:3.47e-01 1,g:4.56e-01 1,cg:4.56e-01 1,g2:5.08e-01
  12   4.970        6.9e-06,1.1e-09   1,phase  6.20e-01 5.03e-01 4.11e-01 1,phase:6.20e-01 1,1/g:6.37e-01 1,cg:6.72e-01 1,g:6.72e-01
  14   5.278        1.7e-05,9.8e-11     1,1/g  4.15e-01 6.92e-01 5.65e-01 1,1/g:4.15e-01 1,g:4.32e-01 1,cg:4.32e-01 1,g2:4.58e-01
  16   5.545        4.1e-06,6.2e-09   1,phase  5.98e-01 6.31e-01 5.15e-01 1,phase:5.98e-01 1,1/g:6.51e-01 1,alt:6.88e-01 1,cg:7.04e-01
  20   5.991        5.4e-06,6.8e-10     1,1/g  6.07e-01 7.08e-01 5.78e-01 1,1/g:6.07e-01 1,g:6.41e-01 1,cg:6.41e-01 1,g2:6.59e-01
  24   6.356        8.4e-06,4.3e-10     1,1/g  4.46e-01 5.91e-01 4.83e-01 1,1/g:4.46e-01 1,g:5.15e-01 1,cg:5.15e-01 1,g2:5.55e-01
  32   6.931        7.1e-06,9.5e-10     1,1/g  3.90e-01 4.46e-01 3.64e-01 1,1/g:3.90e-01 1,g:4.80e-01 1,cg:4.80e-01 1,g2:5.29e-01
```

Reading:

```text
1. The two null singular values from E73.165 are stable near 1e-5 and 1e-9.

2. No simple moment space fits Ker(T_L).  Best residuals are 0.35--0.70.

3. The kernel and range change noticeably with L, so the projector is not a
   fixed height-moment projector.
```

Conclusion:

```text
The rank-three projector is real, but its range/kernel are operator-dependent.
The endpoint remains CANON-PROJ-CRIT-DIV with finite projector P_bad,L.
```

