# E72.329 -- Minimal transformed theorem for Phase 72

**Purpose.** Consolidate E72.311--E72.328 into one proof-facing theorem. This is the current minimal
endpoint for the transformed Cauchy/packet route to Mellin spectral divisibility.

## 1. Objects

Let

```text
G_x(z):=(1-e^(zL))C_x(iz),
C_x(w)=sum_m xi_m/(w-d_m).
```

Let `Z(w)=xi(1/2+w)` be the shifted completed zeta function, and let zero representatives be chosen
modulo `w ~ -w`.

The transformed packet equation is:

```text
Lambda_L G_x(z)
= sum_{w in Div(Z)/+-} Pair_z(w)
   - Lcal(B_z^tail),                                  (1)
```

where

```text
Lambda_L=mu+e_pole-2kappa_L.
```

The paired kernel is explicit from E72.321:

```text
Pair_z(w)
= G_x(w)/(w^2-z^2)
   [ w(1+e^(zL))(1-e^(-wL))
     + z(1-e^(zL))(1+e^(-wL)) ],
```

with removable Hermite values at `z=w`.

## 2. Closed structural inputs

The following parts are already proved in E72.311--E72.328:

```text
REM:
finite mesh and kinematic poles are removable.

CELL:
the transformed cell kernel has the complete-mesh Green form, with explicit finite tail.

ABEL:
the combined model/WR/prime transform reduces to the packet zero sum plus endpoint scalar.

PAIR:
the G_x(z)-coefficient cancels under the +- zero-pair symmetry.

ZCB:
maximal-real-part off-line clusters have invertible leading Cauchy blocks, including multiplicity.

CRIT:
critical-line nodal values are polynomially bounded in fixed active windows.
```

## 3. Remaining analytic gates

The transformed route now needs only:

```text
GAP/LCOEF:
|Lambda_L| >= cL^a, with a>0.

UREM-POLY:
sup_{z in K}|Rem_T^M(z)| <= C_{K,T}L^B,
where `Rem_T^M` is the finite packet remainder outside the chosen zero window.
```

Here `K` is any fixed compact shifted strip used in `PW-Cauchy`.

`GAP/LCOEF` is zero-free and closed by E72.330 from the pole-even gap. E72.331--E72.333 show why the
finite Fourier tail must be kept in signed spectral form, and E72.332 shows why outside zeros require a
contour formulation. E72.334 unifies both into one finite remainder contour estimate `UREM-POLY`.
E72.338 corrects the next gate: absolute `PACK-SMOOTH` is too strong, so the proof-facing target is
paired oscillatory smoothness `POSC`.

## 4. The theorem

### Theorem 72.329

Assume the pole-even gap and `UREM-POLY` in fixed compact shifted strips. Then:

```text
PW-Cauchy:
sup_{z in K}|G_x(z)| <= C_KL^B.
```

Consequently:

```text
PW-Cauchy
=> SQB
=> CB
=> RNS
=> MC-NZ
=> NZ-MSD
=> fixed-height compact-root HPAC decay.
```

Together with the already recorded transport/source/bordered-minor gates of Phase 72, this supplies
the Mellin spectral divisibility needed for scalar WRL annihilation.

### Proof

Use descending induction over positive real parts of off-line shifted zeros in a fixed zero window.

1. For a maximal positive real-part cluster, E72.324--E72.325 give invertibility of the leading
   Cauchy/Hermite block. `UREM-POLY` and lower-cluster terms are polynomial errors.
   Therefore all maximal-cluster nodal Hermite values of `G_x` are exponentially suppressed.

2. Remove that cluster and repeat. Since the window contains finitely many zeros counted with
   multiplicity, the induction terminates. This proves `OFF-NODAL`.

3. E72.327 gives `CRIT-POLY`.

4. E72.326 applies equation (1), in its finite-remainder form: `OFF-NODAL + CRIT-POLY + UREM-POLY`,
   divided by
   `GAP/LCOEF`, gives `PW-Cauchy` on `K`.

5. E72.314--E72.312 and E72.311 give the implication chain from `PW-Cauchy` to `NZ-MSD`, hence the
   compact-root HPAC decay.

`QED`

## 5. What remains outside this theorem

The theorem does not yet prove RH. It isolates the remaining proof obligations:

```text
1. prove `POSC` for the finite packet contour, hence `UREM-POLY`;
2. connect fixed-height compact-root HPAC decay to full scalar WRL through the existing Phase 72
   source, transport, and bordered-minor gates.
```

The important progress is that the hard off-line exponential block is no longer open: it is forced by
the Cauchy-block theorem once the two tail estimates are polynomial.

## 6. Status

```text
proved: structural transformed route plus GAP/LCOEF;
open:   POSC/UREM-POLY and the already known final transport-to-WRL gates.
```
