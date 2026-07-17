# E72.145 -- Positive relative mode alignment

**Date:** 2026-07-09.
**Role:** search for explicit structure in the low-rank PSD certificate.

## 0. Motivation

E72.144 shows that only two or three positive relative modes are enough to certify:

```text
dist(K_rel,PSD)<1.
```

To make the certificate explicit, those positive directions should be identified without solving a
full spectral problem.  The first audit compares them with simple physical-band candidates:

```text
mass,
d^2,
d^4,
d^6,
edge,
center.
```

All candidates are projected to the even Feshbach complement and then normalized in the model energy
metric.

## 1. Diagnostic

The companion script:

```text
E72_145_positive_mode_alignment_probe.py
```

reports the correlations between the top three positive relative eigenvectors and the candidate
directions.

Representative output:

```text
E72.145 positive mode alignment probe
 lam   L  topEig   mode  bestCand  bestCorr  mass  d2  d4  d6  edge center
   8  4.16   0.569      1     mass     0.195  0.20  0.15  0.13  0.11  0.09  0.01
  10  4.61   0.495      1     mass     0.207  0.21  0.14  0.11  0.10  0.08  0.04
  12  4.97   0.463      1     mass     0.124  0.12  0.11  0.09  0.08  0.06  0.00
  14  5.28   0.398      1     mass     0.038  0.04  0.02  0.02  0.02  0.01  0.00
  16  5.55   0.371      1     mass     0.182  0.18  0.15  0.12  0.11  0.08  0.01
  18  5.78   0.347      1       d2     0.052  0.05  0.05  0.04  0.04  0.03  0.00
```

The correlations are too low to support a simple mass/moment/edge rank-3 certificate.  The positive
PSD approximant must be adapted to the arithmetic kernel itself.

## 2. Status

```text
rejected: simple physical moment candidates for the top positive relative modes;
kept:     rank-3 PSD-DIST is alive, but its directions are arithmetic-kernel adapted.
```
