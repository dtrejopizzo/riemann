# E72.189 -- D-ASRP moment diagnostic

**Date:** 2026-07-09.
**Role:** identify what controls the pure diagonal ASRP estimate for the recommended margin `m_*=0.03`.

## 0. Question

E72.188 recommends:

```text
m_*=0.03,
D-ASRP-0.03:
Tr(G_0^2)+Tr(G_1^2)<0.9409.
```

This diagnostic asks whether the pure energy is governed by low moment structure of the two blocks.

## 1. Output

The companion script:

```text
E72_189_dasrp_moment_probe.py
```

reports:

```text
E72.189 D-ASRP moment probe
margin m*=0.03; reports pure G energy and low moments
 lam    L dim   D  G0sq  G1sq  Gsum  H0    S0/H0  H1    S1/H1
  12  4.97  32  60 0.565 0.333 0.898 1.282   0.229 0.468  -0.313
  16  5.55  40  66 0.457 0.337 0.794 1.042   0.234 0.470  -0.325
  20  5.99  48  72 0.403 0.332 0.735 0.922   0.237 0.440  -0.414
  24  6.36  56  78 0.373 0.368 0.741 0.850   0.235 0.467  -0.496
  28  6.66  64  84 0.296 0.340 0.636 0.734   0.311 0.436  -0.477
  32  6.93  72  90 0.319 0.174 0.492 0.673   0.157 0.258  -0.222
  36  7.17  80  94 0.306 0.342 0.648 0.698   0.234 0.411  -0.599
worst_Gdiag=0.898 at lambda=12
```

Here:

```text
Hj=Tr(K_j^2),
Sj/Hj=(||K_j^+||_HS^2-||K_j^-||_HS^2)/||K_j||_HS^2.
```

## 2. Reading

The worst pure energy is:

```text
lambda=12, G0sq+G1sq=0.898.
```

The recommended target:

```text
0.9409
```

has real margin.

The two blocks have stable roles:

```text
K0: larger mass, positive asymmetry;
K1: smaller mass, negative asymmetry.
```

The D-ASRP proof can therefore target a coupled low-moment estimate rather than the full mixed cycle
first:

```text
Tr(G_0^2)+Tr(G_1^2)<0.9409.
```

The data suggest that this is essentially a one-block energy theorem plus a finite initial check; the
maximum occurs at the first stable window.

## 3. Next target

Search for a scalar majorant:

```text
g_{j,D}^2(t) <= P_j(t)
```

where `P_j` has low degree or a simple Chebyshev-positive form, and prove:

```text
Tr P_0(K_0)+Tr P_1(K_1)<0.9409.
```

This would reduce D-ASRP to pure block moment inequalities.
