# E73.212 - Entry certificate package

Date: 2026-07-14.

## 1. Purpose

This note packages the entry-radius work E73.209--E73.211 into the exact
finite certificate needed by the bordered Krawczyk route.

## 2. Inputs

From E73.208--E73.209, the Krawczyk matrix budget is implied by:

```text
|H_mn-H_0,mn| <= r_entry,
r_entry <= epsH/dim.
```

For the tested windows this requires roughly:

```text
lambda=8:   r_entry <= L^-56.26,
lambda=10:  r_entry <= L^-51.93,
lambda=12:  r_entry <= L^-48.94.
```

## 3. Special-function part

E73.210 shows that the digamma/polygamma tail can be enclosed by Bernoulli
asymptotics:

```text
D_1(R,omega)=1/2[psi(R+1/2)-psi(R+1/4-iomega/2)],
D_2(R,omega)=1/4 psi_1(R+1/4-iomega/2).
```

With `R=80` and `K=12`, the resulting radius is already about `10^7` times
below `r_entry` in the tested windows.  E73.216 shows that choosing `K=16`
raises the allowed sector constant to about `10^17`, so `K=16` is the preferred
proof-facing setting.

## 4. Finite elementary part

E73.211 audits the finite elementary pieces:

```text
R_elem + R_WR_head + R_prime.
```

Even a crude `80`-decimal rounding model leaves about `10^39--10^40` slack
relative to `r_entry`.

E73.215 replaces this audit model by native complex-ball propagation for the
finite elementary operations.  The resulting ball radii are around
`L^-138--L^-156`, far below both the target and the special-function radius.

## 5. Finite-entry theorem

**Theorem 212.1 (entry certificate, finite-window).**  In the tested
finite windows, suppose the closed entry engine is implemented with complex
ball arithmetic such that:

```text
1. elementary finite sums are propagated by the E73.215 ball rules;
2. the digamma tail uses R=80 and K=16 Bernoulli remainder enclosures;
3. the final entry ball radius is bounded by the sum of the component radii.
```

Then the entry balls satisfy the per-entry targets of E73.209, hence the
matrix interval satisfies the `epsH` budget of E73.208, hence the bordered
Krawczyk eigenline certificate is available for those finite windows.

*Proof.*  The operator-radius implication is E73.209.  The admissible `epsH`
values are computed by the Krawczyk inequality of E73.208.  E73.210 bounds the
non-elementary digamma tail below the target, E73.229 proves the sector
Bernoulli remainder bound in the finite windows, and E73.216 gives `10^17`
sector-constant slack at `K=16`.  E73.215 bounds the finite elementary ball
radius still further below the target.  Summing the component radii gives
`|H_mn-H_0,mn|<=r_entry`.  The Krawczyk conclusion follows from E73.204. `QED`

## 6. Status

```text
proved: logical package from entry radii to bordered eigenline certificate;
implemented: native ball propagation for finite elementary entry pieces;
finite-window closed: Bernoulli sector lemma proved in E73.229;
uniform-open: control the same sector constant in growing windows.
```
