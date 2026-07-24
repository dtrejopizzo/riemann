# P76.066 - Weyl-disk reading of SAFE-LIMIT-POINT

## 1. The reformulation

P76.065 left the phase at:

```text
SAFE-LIMIT-POINT:
among l2 solutions of the infinite rectangular CCM equation, the condition
r_{z_0}v=1 selects a unique safe Cauchy transform, namely that of k_L.
```

This is not a bespoke lemma.  It is a **Weyl limit-point statement** for the
semi-infinite CCM system, and the scalar already isolated at P76.054,

```text
theta_N(z)=r(z)w/r(z)g,                          (NSC-5)
```

is a **Weyl m-function** of the bordered system: the normalized directional
response of the canonical solution pair `(g,w)`.  In Weyl theory:

```text
limit-point case
 <=> the l2 solution normalized by one linear functional is unique
 <=> the finite-section Weyl disks contract to a point
 <=> the canonical-solution energy S_N=sum_j|g_j(z)|^2 diverges,
     with disk radius comparable to 1/S_N.
```

Three consequences of adopting this frame:

1. `SAFE-LIMIT-POINT` becomes an instance of a classical, heavily developed
   dichotomy with checkable criteria (Carleman-type divergence conditions,
   positive-commutator/Kato-Putnam arguments, subordinacy theory).
2. The **bordered ambient-norm catastrophe of P76.061 is explained**, not
   just avoided: Weyl-disk geometry is projective/directional and invisible
   to ambient inverse norms.  An ambient bound of `1e27` next to a true safe
   error of `0.066` is precisely what limit-point geometry looks like when
   measured with the wrong (ambient) instrument.
3. The displacement law RDP-1 of P76.057,

   ```text
   D_r M-M D_c=-(2/L)(s_r 1_c^T-1_r s_c^T),
   ```

   is an **exact rank-two commutator identity** - the standing hypothesis of
   Kato-Putnam/Mourre absence-of-eigenvalue theorems.  The continuum
   antecedent is classical: the finite Hilbert transform has purely
   absolutely continuous spectrum and no eigenvalues (Koppelman-Pincus),
   and the Hilbert matrix likewise (Magnus, Rosenblum).  The CCM mesh
   operator is a discretized finite Hilbert transform plus diagonal; the
   needed absence-of-l2-kernel statement is the discrete version of a
   1959 theorem, not new territory.

## 2. The probe

`P76_066_weyl_disk_probe.py` measures, on nested finite sections of one
multiprecision build (template P76.018), for the zeta build and the planted
off-line falsifier:

```text
S_N        = ||x_N||^2, energy of the canonical bordered inner solution;
1/S_N      = Weyl-disk radius proxy;
shellMass  = fraction of ||x_N||^2 carried by the outer Fourier shell.
```

Limit-point signature: `S_N` grows without bound and the residual mass
escapes to the shell (consistent with P76.062).

## 3. Numerical result (run at dps 70, lam 6, nested sections N=6..12)

```text
-- zeta
 N        S_N          radius~1/S_N   shellMass(k=2)   S_N/S_(N-1)
 6     10622022.0   9.4144036e-8   0.00165555          0.0
 7   1.1217991e+9  8.9142519e-10    9.8779e-5      105.611
 8  1.1507286e+13  8.6901464e-14   3.52694e-6      10257.9
 9  2.5916378e+12  3.8585639e-13   5.23243e-8     0.225217
10  5.0460433e+13  1.9817507e-14   1.4559e-11      19.4705
11  4.5158592e+15   2.214418e-16  4.79469e-11      89.4931
12  1.6815742e+21  5.9468087e-22  3.48109e-12     372371.0
-- planted (gamma=14.13..., beta=0.30, strength=5.0)
 N        S_N          radius~1/S_N   shellMass(k=2)   S_N/S_(N-1)
 6     0.41749409      2.3952435     0.845119          0.0
 7     0.36967431      2.7050839     0.766713      0.88546
 8      51.916581    0.019261669     0.832349      140.439
 9     0.81179905      1.2318319     0.602111    0.0156366
10      6.2428033     0.16018445     0.464304      7.69008
11      16.466282    0.060730164     0.475354      2.63764
12      279.90961   0.0035725819     0.109528       16.999
```

## 4. Reading (recorded honestly, including a revised prediction)

1. **The zeta build shows the limit-point signature, strongly.**  `S_N`
   climbs fourteen orders of magnitude over seven sections (with a parity
   dip at N=9); the disk-radius proxy falls to `6e-22`; the interior mass
   dominates (shell mass falls to `3e-12`).  This is what a contracting
   Weyl disk looks like.

2. **The planted falsifier does NOT show the clean signature.**  `S_N`
   stays erratic and bounded within `0.4 - 3e2`; the radius proxy stalls
   near `1e-2 - 1`; and the residual mass is pinned at the shell
   (`0.1 - 0.85`) instead of escaping inward.  The off-line plant behaves
   like a near-l2 kernel direction - a bound state trying to exist.

3. **Revised prediction.**  The entry expectation ("both builds diverge;
   arithmetic lives only in IDENT") is *not* what the probe returned.  The
   limit-point RATE itself appears arithmetic-sensitive: the off-line
   divisor slows the disk contraction by ~19 orders of magnitude at N=12.
   This is consistent with the phase-71 detector philosophy (stall vs
   error->0), and it upgrades LP from "stability layer with no arithmetic
   content" to "the quantitative discriminant may already live in the
   contraction rate".  The LP/IDENT split of P76.067 stands, but with this
   caveat recorded: LP divergence per se may hold for both builds
   (the falsifier's S_N does drift upward), while the RATE separates them.
   Phase 77 must decide which of the two carries the arithmetic:
   the rate (then LP quantitative) or the identification (then IDENT).

## 5. Status

```text
proved:    theta_N is the Weyl m-function of the bordered CCM system
           (renaming of NSC-5; no new mathematics claimed);
observed:  rank-two displacement = Kato-Putnam commutator hypothesis;
observed:  zeta sections contract the Weyl disk to 6e-22 while the
           planted build stalls near 4e-3 - a 19-order separation;
open:      LIMIT-POINT for the semi-infinite CCM system (see P76.067);
probe:     P76_066_weyl_disk_probe.py (S_N growth, shell escape).
```
