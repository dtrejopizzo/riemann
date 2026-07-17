# E73.298 - Curvature rank audit

Date: 2026-07-16.

## 1. Purpose

E73.297 rewrites the endpoint as the balanced curvature identity

```text
CURV-ABEL:
int_0^L K_L(t) q[Q_t''+alpha_L(t)J]R_wxi_L dt
=O_M(L^(-M)).
```

The next tempting shortcut is that the signed row family

```text
y -> q[Q_y''+alpha_L(y)J]R_w
```

might be controlled by only a few modes.  This note tests that shortcut.
It is not a proof attempt; it is an anti-tautology audit against the
low-moment and low-rank failures of E72.94 and E72.95.

## 2. Probe

For each `lambda`, Cauchy height, and row, the companion script samples

```text
M_y=q[Q_y''+alpha_L(y)J]R_w
```

on 96 points in `(0,L)`, forms the sampled row matrix, and reports:

```text
r90, r99, r999      numerical ranks for 90%, 99%, 99.9% row energy;
tail4, tail8        row-family energy not captured by the first 4/8 modes;
scalarProj4/8       residual of the actual scalar y -> M_y xi_L after
                    projecting through the first 4/8 row singular modes.
```

## 3. Result

There is mild row-family compressibility in some channels, but not a uniform
few-mode scalar mechanism.

Representative obstructions:

```text
lambda=12, gamma=21.02, row=1:
  r999=18, scalarProj8=9.16e-01.

lambda=20, gamma=21.02, row=0:
  r999=12, scalarProj8=7.50e-01.

lambda=20, gamma=21.02, row=1:
  r999=12, scalarProj8=7.63e-01.
```

Even where the row family has a small `tail8`, the scalar direction
`xi_L` can sit largely outside the leading sampled row modes.  Thus a
rank-4 or rank-8 curvature reduction would not force `CURV-ABEL`.

## 4. Relation to earlier no-gos

This is the curvature analogue of the Phase 72 audits:

```text
E72.94: low moments do not explain finite-band root transport;
E72.95: phi is not aligned with span{xi,h,1}.
```

E73.298 adds:

```text
the balanced curvature endpoint is not explained by a fixed few-mode
row singular reduction.
```

The failure is useful because it keeps the endpoint honest.  The curvature
identity is a signed full-kernel orthogonality statement, not a low-rank
certificate in disguise.

## 5. Status

```text
rejected: fixed few-mode curvature rank forcer;
kept:     CURV-ABEL as the clean analytic endpoint;
open:     prove the signed full-kernel pairing with K_L from the explicit
          Gamma-prime/eigenline structure.
```
