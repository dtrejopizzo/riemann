# E78.1 - Ground-state simplicity at mu_L: parity structure, the dead
# Perron-Frobenius route, and the build-discriminating gap (autopsy of item 4)

**Run:** 2026-07-18.
**Target:** interface subclause (e) / Fable-5 item 4 --
`dim ker(H_L - mu_L) = 1` and `r(z0) e_L != 0`, required build-neutrally.
**Verdict:** item 4 as posed does **not** close build-neutrally. Simplicity with
isolation at `mu_L` is a build-DISCRIMINATING property; the Perron-Frobenius
mechanism proposed for it does not exist for either build. This document proves
the two structural facts, records the discriminating spectral data, and names
the corrected object.

## 1. What item 4 asked for and why it looked tractable

E77.7f closed `mu_L = inf spec(H_L)` as an isolated eigenvalue of finite
multiplicity (compact resolvent from `H_L = D_L + B_L`, `D_L(n)=log(1+|n|)+O_L(1)
-> +infinity`, `B_L` bounded self-adjoint). Subclause (e) asks that this ground
eigenvalue be **simple** and that the safe Cauchy row not annihilate the ground
vector. The natural mechanism is Perron-Frobenius: if a diagonal gauge
`D in {+-1}` makes the off-diagonal part `B_L` single-signed (nonpositive), then
`exp(-t H_L)` is positivity improving, the ground state is simple, and its
eigenvector is nodeless -- which would also force `r(z0) e_L != 0` generically.

This note tests that mechanism against the actual operator, using the P76.002
`build_mp` infrastructure verbatim (zeta build + the standard planted falsifier
`("14.134725141734693790","0.30","5.0")`), at `lambda=6`, `dps=70..90`.

## 2. Proved: parity decomposition

The CCM entry satisfies, from the `q_value` symbol `(sin(d_m y)-sin(d_n y))/(pi(n-m))`
with `d_n = 2 pi n / L`,

```text
entry(-m,-n) = entry(m,n)                       (P-1)
```

(under `n -> -n` both the numerator sine differences and the denominator `(n-m)`
change sign, cancelling; the diagonal `2(1-y/L)cos(d_n y)` is even). Hence `H_L`
commutes with the flip `J: (Jv)_n = v_{-n}`, `J^2 = I`, and

```text
spec(H_L) = spec(H_L|even) cup spec(H_L|odd),                (P-2)
```

with `H_L|even`, `H_L|odd` the exact compressions to the symmetric/antisymmetric
bases (E78.1b builds these blocks explicitly). Every statement below is read in
this decomposition. The probe verifies `(P-1)` to working precision and the block
reduction reproduces the full spectrum.

## 3. Proved: the Perron-Frobenius route is dead for both builds

An exact off-diagonal sign census (E78.1, strictly-upper entries):

```text
zeta :  N=4  pos=36  neg=0    N=6  pos=78  neg=0
        N=8  pos=136 neg=0    N=10 pos=206 neg=4
plant:  N=4  pos=32  neg=4    N=6  pos=40  neg=38
        N=8  pos=71  neg=65   N=10 pos=139 neg=71
```

Two independent obstructions follow.

```text
(a) ZETA: off-diagonals are (essentially) all POSITIVE. Bottom-of-spectrum
    Perron-Frobenius requires off-diagonals <= 0 (so that -H has nonnegative
    off-diagonals). Positive off-diagonals are the WRONG sign for the ground
    state -- they are the PF sign for the TOP of the spectrum, not mu_L.
    Moreover a uniformly-positive off-diagonal pattern on >= 3 modes admits NO
    diagonal +-1 gauge to nonpositive off-diagonals: that would require
    D_a D_b = -1 for all pairs, impossible past two indices (bipartite
    obstruction). Verified: gauge_balanced = False at every N.

(b) PLANT: off-diagonals are genuinely MIXED sign (e.g. 40/38 at N=6). A mixed
    sign pattern is gauge-balanceable only if its signed graph has no
    frustrated cycle; the probe finds it is NOT balanced at any N
    (violations 40/78 at N=6, etc.).
```

Therefore **neither build admits the sign-definiteness that Perron-Frobenius
needs.** The mechanism the planner hoped would deliver item 4 does not exist.
This is a structural fact about `B_L = -(1/pi)[diag(S_L), K]` (E77.7d): the symbol
`S_L` is an oscillating almost-periodic function, so its divided differences
-- the off-diagonal entries -- carry no fixed sign, and no gauge repairs this.

Note (MW-audit): this is **not** MW-1. MW-1 forbids routing through Weil
explicit-formula positivity of the arithmetic quadratic form; the object here is
the elementary matrix-entry sign pattern of `B_L`, a different quantity. The
result is a *negative* one (no positivity is available), so it cannot smuggle a
positivity of the wrong sign either.

## 4. Observed: the ground state is simple at every finite N, but its
##            isolation is build-discriminating

Parity-resolved lowest eigenvalues (E78.1b, dps=90):

```text
ZETA           even0        odd0         even1
  N=6      5.68e-23     2.74e-20     3.80e-18
  N=8      3.68e-28     2.65e-25     1.09e-22
  N=10     8.93e-33     7.87e-30     3.57e-27
  N=12     2.40e-37     2.24e-34     1.41e-31
  N=14     1.71e-41     2.16e-38     1.30e-35

PLANT          even0        odd0
  N=6     -0.12008954  -0.09732395
  N=8     -0.72043013  -0.50259469
  N=10    -1.643986    -1.4642943
  N=12    -1.7094594   -1.5639954
  N=14    -1.7241457   -1.5873388
  N=16    -1.7400187   -1.6266881
```

At every finite `N` the global ground eigenvalue is nondegenerate (the even
bottom is strictly below the odd bottom for both builds). But the LIMIT is
opposite in the two builds. The global ground gap `g_N` and its section ratio
(E78.1c, dps=70):

```text
ZETA :  N=12 g=2.237e-34   N=14 g=2.162e-38 (ratio 9.66e-5)
                            N=16 g=2.118e-42 (ratio 9.80e-5)
PLANT:  N=12 g=0.14546     N=14 g=0.13681   (ratio 0.9405)
                            N=16 g=0.11333   (ratio 0.8284)
```

```text
DICHOTOMY:
- zeta:  every low eigenvalue (both sectors, several indices) collapses to 0
         GEOMETRICALLY; g_N/g_{N-2} ~ 1e-4. By min-max
         (lambda_k(P_N H P_N) decreasing to lambda_k(H), valid since compact
         resolvent gives empty essential spectrum) this drives mu_L -> 0 with a
         VANISHING ground gap.
- plant: even-sector ground converges to an isolated ~ -1.73, odd-sector ground
         to ~ -1.59; g_N/g_{N-2} ~ 0.85, ORDER ONE. The ground state is simple
         AND isolated with an order-one gap.
```

The collapse rates differ by roughly four orders of magnitude and the pattern is
robust across `N = 6..16` at `dps = 70..90`; it is consistent with the E77.7f
data to `N = 18` (zeta ground gap `3.84e-46` at `N=18`, still collapsing; plant
gap `O(0.1)`).

## 5. Reading: item 4 is not build-neutral; the gap is a detector

E77.7f established the identity that the ground-gap collapse **is** the LP
endpoint:

```text
gap at mu_L -> 0  <=>  S_N(mu_L) -> infinity  <=>  Weyl disks contract  <=>  LP.
```

Section 4 shows this holds for zeta and fails for the plant. Consequently:

```text
1. Simplicity-with-isolation at mu_L is BUILD-DISCRIMINATING. It is a clean
   isolated simple ground state for the plant and a degenerating (gap -> 0)
   ground point for zeta. So subclause (e) as posed is NOT the falsifier-neutral
   object the SAFE-DISK-IDENT decomposition assumed it to be.

2. The discriminating quantity is exactly the ground-state gap = the LP/BTG
   divergence signature. Being order-one build-discriminating, it is -- by the
   E77.7az / E72.16 gate -- a DETECTOR, not an admissible forcing mechanism. It
   carries surplus zero-location content beyond any build-neutral LP statement.

3. Item 4 therefore cannot be driven to a build-neutral theorem of the form
   "dim E_L = 1 with a spectral gap." The Perron-Frobenius route is dead
   (section 3) and the isolation the argument would need is precisely the
   build-discriminating quantity (section 4).
```

This does not refute item 4 for the plant (where it holds); it refutes the
requirement -- that item 4 be a **build-neutral** subclause of the LP interface.
The neutral content survives only in the weaker, gauge-free form named below.

## 6. Flag for Fable-5 (not adjudicated here)

The plant's order-one-stable ground gap (section 4) means `S_N(mu_L^plant)` need
not diverge at the plant's **own** `mu_L ~ -1.73` -- the finite resolvent
`A_N(mu_L)^{-1}` stays bounded because the gap does not close. That is
Outcome-B-flavored evidence (plant failing canonical-energy divergence at its
true spectral bottom), in tension with Outcome A (E77.1b). The E77.6/E77.7f
"plant S_N diverges slowly" measurement used a frozen surrogate `mu_ref = -1.744`
sitting *below* the converging even bottom (`-1.71 -> -1.74`), so its growth is a
below-spectrum artifact, not divergence at `mu_L`. This is recorded as **data for
review**; per the session's binding constraint the settled E77.7az gate is not
reopened here.

## 7. Corrected next object (build-neutral remnant)

What remains admissibly build-neutral is not simplicity but the gauge-free
nonvanishing/existence pair, stated without any isolation or sign hypothesis:

```text
NEUTRAL-GROUND-CAUCHY:
for the finite sections, the safe Cauchy row r(z0) does not annihilate the
lowest-mode subspace, i.e. the projected anchor r(z0) P_{E_N} is nonzero, with a
lower bound uniform in N that uses NO build-discriminating gap. This is the only
part of subclause (e) that can enter LP as forcing; the simplicity/isolation
part is a detector and must be carried by IDENT instead.
```

The interface assembly (subclause f) must therefore be re-derived from
`NEUTRAL-GROUND-CAUCHY` + the build-neutral separation of Cauchy rows (E77.7aj,
subclause a), NOT from a simple isolated `mu_L`.

## 8. Probes

```text
E78_1_ground_simplicity_probe.py     (sign census, gauge test, dps=70)
E78_1b_low_spectrum_probe.py         (parity blocks, low spectrum, dps=90)
E78_1c_gap_confirm_probe.py          (gap ratios N=12..16, dps=70)
E78_1_ground_simplicity_results.json (consolidated verified numbers)
```

All numbers cited above were read from executed probe output; no value is
projected or fabricated.

## 9. Status

```text
proved:    parity decomposition H_L = H_even (+) H_odd via J:(Jv)_n=v_{-n}  (P-1);
proved:    Perron-Frobenius route dead -- no diagonal +-1 gauge makes B_L
           single-signed; zeta off-diagonals uniformly positive (wrong sign),
           plant mixed; neither gauge-balanced;
observed:  ground state nondegenerate at every finite N for both builds;
observed:  ground-gap dichotomy -- zeta gap collapses geometrically (ratio
           ~1e-4), plant gap order-one stable (ratio ~0.85), 4 orders apart,
           robust N=6..16, consistent with E77.7f to N=18;
refuted:   item 4 (simplicity + isolation at mu_L) as a BUILD-NEUTRAL subclause
           -- it is build-discriminating and hence a detector under E77.7az;
           the PF mechanism proposed for it does not exist;
flagged:   plant order-one gap => possible plant BTG non-divergence at its own
           mu_L (Outcome-B-flavored); recorded as data for Fable-5, gate not
           reopened;
open:      NEUTRAL-GROUND-CAUCHY (gauge-free nonvanishing, uniform in N without a
           build-discriminating gap) as the only admissibly build-neutral
           remnant of subclause (e); interface assembly (f) to be re-derived from
           it plus E77.7aj.
```
