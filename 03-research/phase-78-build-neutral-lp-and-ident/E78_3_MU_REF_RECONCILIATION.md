# E78.3 - Reconciliation of the E78.1/E78.2 flag against Outcome A

**Run:** 2026-07-18.
**Question:** does the plant's stable order-one intra-section ground gap
(E78.1 section 4) contradict Outcome A (E77.1b: operational LP, hence
`BTG-DIV-L`/`S_N(mu_L)->infinity`, holds for both builds)?
**Verdict:** No. The flag rests on a conflation of two different gaps. Once the
correct gap is identified, it is already proved in the existing ledger
(E77.7g) to close to zero for both builds. Outcome A and the E77.7az gate are
**not** overturned. The genuinely open question was already on record as
`RITZ-BRACKET` / `LOW-MODE-BTG` (E77.7g-7ak) and is not a new crisis.

## 1. The two different gaps

Let `A_N(mu) = H_L[I_N,I_N] - mu I` with eigenpairs `(nu_j^{(N)}, u_j^{(N)})`,
ordered increasingly, and let `mu_L = inf spec(H_L)`.

```text
INTRA-GAP:   g_N = nu_1^{(N)} - nu_0^{(N)}          (gap between the two
                                                       lowest Ritz values of
                                                       one finite section);

FLOOR-GAP:   delta_N = nu_0^{(N)} - mu_L             (distance from the
                                                       finite ground Ritz
                                                       value to the true
                                                       infinite-volume floor).
```

These are unrelated quantities in general. `E78.1` measured `g_N` and found it
stable at order one for the plant (`g_N ~ 0.11-0.15`, `N=6..16`) and collapsing
geometrically for zeta. Section 6 of E78.1 then reasoned: "a stable order-one
gap [...] means the finite resolvent `A_N(mu_L)^{-1}` stays bounded" -- but the
resolvent norm at `mu_L` is controlled by `delta_N`, not by `g_N`:

```text
||A_N(mu_L)^{-1}|| = 1/dist(mu_L, spec(A_N)) = 1/delta_N.
```

`g_N` order-one and `delta_N -> 0` are simultaneously possible: the whole
bottom of the finite spectrum can sit at a stable distance from its own
second level while still sliding, as a block, toward the true floor `mu_L`.

## 2. delta_N -> 0 is already proved, for both builds

This is not new numerics. `E77.7g` section 4 already proved, from the
`H_L=D_L+B_L` compact-resolvent theorem of `E77.7d`:

```text
mu_R = lambda_min(P_R H_L P_R)  decreases monotonically to  mu_L,   mu_L <= mu_R,
```

for any compact-resolvent self-adjoint `H_L`. `E77.7d` proved compact
resolvent for **both** the zeta and the planted operator (the `D_L+B_L`
decomposition and the Dirichlet-test diagonal bound do not use the build).
Hence `delta_N = nu_0^{(N)} - mu_L -> 0` monotonically for the plant exactly as
for zeta. `E78.1`'s flag implicitly assumed the opposite (a stable floor
distance); that assumption was never justified and is not what E78.1 measured.

So there is **no proof, and no numerical evidence, that `A_N(mu_L)^{-1}` stays
bounded for the plant.** The stable `g_N` is compatible with, and irrelevant
to, `delta_N -> 0`.

## 3. Probe: does the ground sequence itself behave consistently with this?

`E78_3_mu_ref_reconciliation_probe.py` (P76.002 `build_mp`, `lambda=6`,
`dps=70`, `N=6..20`, both builds) computes the true inner-block ground
eigenvalue `nu_0^{(N)}` (mixed parity -- the global section minimum, not
parity-separated) at each `N`, together with the coupling
`c_0=|<u_0^{(N)},b_N>|`.

### Zeta

```text
N   6   nu0 = 7.43e-21
N   8   nu0 = 1.14e-25
N  10   nu0 = 1.85e-30
N  12   nu0 = 4.30e-35
N  14   nu0 = 2.26e-39
N  16   nu0 = 1.57e-43
N  18   nu0 = 2.36e-47
N  20   nu0 = 4.62e-51
```

Monotone decrease to `0` across eight sections, exponent dropping by roughly
4-5 decades per 2 modes. Clean, unambiguous convergence `nu_0^{(N)} -> mu_L=0`.

### Plant

```text
N    6   nu0 = -0.038188
N    8   nu0 = -0.411329
N   10   nu0 = -1.497054
N   12   nu0 = -1.699839
N   14   nu0 = -1.723438
N   16   nu0 = -1.735527
N   18   nu0 = -1.740140
N   20   nu0 = -1.748323
```

Monotone decrease (consistent with the E77.7g Ritz theorem), decelerating from
`N=10` to `N=18` (successive decrements `0.2028, 0.0236, 0.0121, 0.0046`) but
**not cleanly geometric**: the `N=18->20` decrement (`0.0082`) is larger than
the `N=16->18` decrement (`0.0046`). A naive Aitken extrapolation on the raw
mixed-parity sequence is correspondingly unstable (running estimates:
`-1.746, -1.727, -1.748, -1.743, -1.730`, not settling).

## 4. What this does and does not establish

```text
established:  delta_N -> 0 for the plant is already a proved fact of the
              ledger (E77.7g), independent of this probe; the E78.1 flag's
              premise (stable floor distance) has no support, proved or
              numerical;
established:  the raw ground sequence for the plant is monotone decreasing
              through N=20, consistent with (not contradicting) convergence
              to some finite mu_L;
not established: a clean asymptotic/geometric regime for the plant ground
              sequence at N<=20 -- the decrement reversal at N=18->20 shows
              the section sizes reached here are not yet in the regime where
              naive extrapolation is reliable;
not established: whether the coupling c_0=|<u_0^{(N)},b_N>| stays bounded
              away from 0 as N->infinity. Measured values fluctuate at order
              one without a visible decay trend (0.034, 1.92, 0.34, 0.16,
              0.039, 0.067, 0.075, 0.032 for N=6..20) but this is eight data
              points on a fluctuating sequence, not a proof of a positive
              lower bound.
```

The genuine open question -- does `c_0` stay bounded below, giving
`S_N(mu_L) ~ c_0^2/delta_N^2 -> infinity` since `delta_N -> 0` is already
proved -- is exactly the object the ledger already named: `LOW-MODE-BTG(K)`
and its certified-bracket form `RITZ-BRACKET` / `BRACKETED-LOW-MODE-BTG`
(E77.7g-E77.7h), reset as the live BTG object in `E77.7ak`
(`SHELL-RESIDUAL-CANCELLATION` and its downstream chain). This document adds
no new open object; it removes a spurious one.

## 5. Verdict on the E77.7az gate and the phase-77 closure

**Not reopened.** The E78.1/E78.2 flag rested on treating the intra-section
gap `g_N` as a proxy for the floor-gap `delta_N`. Once separated, `delta_N->0`
is already a proved theorem (E77.7g) that does not distinguish the builds --
exactly the falsifier-neutral content Outcome A requires. The plant's stable
`g_N` and the projective-transfer defect plateau (E78.2) remain valid,
interesting, correctly-computed numbers, but they measure a different
quantity (the shape/gap of the finite section, and the raw `mu=0` vs
`mu=mu_L` pencil mismatch, respectively) than the one that would be needed to
overturn Outcome A. Item 4 and item 2 (E78.1, E78.2) remain refuted as
build-neutral forcing routes for the reasons already given there (their
build-discriminating content is real and disqualifies them under E72.16) --
that conclusion is independent of this note and stands.

## 6. Probes

```text
E78_3_mu_ref_reconciliation_probe.py
E78_3_mu_ref_reconciliation_results.json
```

All numbers above were read from the executed probe's JSON output at
`dps=70`, `lambda=6`, `N=6,8,...,20`.

## 7. Status

```text
resolved:  the E78.1/E78.2 flag (possible Outcome-B evidence) is a
           conflation of intra-section gap with floor-to-limit gap;
proved (cited, not reproved): delta_N=nu_0^{(N)}-mu_L -> 0 monotonically for
           any compact-resolvent H_L (E77.7g), hence for both builds;
observed:  plant ground sequence decreases monotonically through N=20 but is
           not yet in a clean asymptotic regime (decrement reversal at
           N=18->20); naive Aitken extrapolation on it is unreliable;
observed:  plant coupling c_0 fluctuates at order one with no visible decay
           trend through N=20 (not a proof of nonvanishing);
not reopened: E77.7az attribution gate and the Phase-77 closure stand;
live (unchanged): LOW-MODE-BTG(K) / RITZ-BRACKET / the E77.7ak
           SHELL-RESIDUAL-CANCELLATION downstream chain, now flagged (per
           E77.7az section 6) to be re-derived in a build-neutral form;
refuted (unchanged, from E78.1/E78.2): item 4 and item 2 as build-neutral
           interface subclauses.
```
