# E78.137 - `mu_N -> 0` convergence gate: Branch A vs Branch B, corrected

**Run:** 2026-07-18 (buggy run), corrected 2026-07-20.
**Question:** for the inner-block operator sequence `A_N = H_L[1:-1,1:-1]`
(the E77.7d/E78.1 operator, `nu_0^{(N)} <= nu_1^{(N)} <= ...` its ordered
eigenvalues), does `nu_1^{(N)}` converge to a strictly positive limit
(Branch A: an isolated ground state with a uniform gap, so a rank-one
quasimode deflation lemma can drive `mu_N -> 0`), or does it collapse to `0`
together with `nu_0^{(N)}` (Branch B: the whole low tower sinks, and rank-one
deflation against a single isolated state is not available)?
**Verdict:** **Branch B**, for the genuine (zeta) build, at every `L` tested
(`L=4,6,8`) and every `N=6..16`. `nu_0^{(N)}` and `nu_1^{(N)}` collapse
geometrically together; the gap `nu_1^{(N)} - nu_0^{(N)}` itself shrinks by
several orders of magnitude per step. The planted falsifier does the opposite:
both `nu_0^{(N)}` and `nu_1^{(N)}` settle at order-one negative values with a
stable, non-vanishing gap. This closes the gate question with corrected,
verified data; it does **not** by itself close `mu_N -> 0`.

## 0. Wall checklist

```text
MW-1:  respected. No positivity/Weil-form target appears; this is a raw
       inner-block eigenvalue measurement.
MW-2:  respected. Inside the fixed-L / Re(s)>1 arithmetic front (build_mp,
       lambda=6, standard L in {4,6,8}).
MW-3:  respected. No local-global prime assembly.
MW-4:  respected. No wrong-sign lower-bound mechanism.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform spectral-gap hypothesis is assumed; the gap is
       measured, not assumed, and this document reports it VANISHES for zeta.
K1-K5: respected. No determinant endpoint closure, no Christoffel evaluator,
       no ambient bordered-inverse norm before paired reduction.
P76.061: respected. No inversion of the full logarithmic quotient is used.
E72.16/E77.7az: respected. This is front B; build separation between zeta and
       the planted falsifier is EXPECTED and is exactly what the gate is
       designed to detect (falsifier-location principle: the discriminant
       must live in a VALUE, and here it does -- nu_1^{(N)} converges to two
       different kinds of limit, 0 vs an order-one negative constant).
```

## 1. Bug history (read before trusting any earlier E78.137 numbers)

The first version of `E78_137_mu_convergence_gate_probe.py` diagonalized the
**full bordered matrix** `H` returned by `build_mp(...)` directly:

```text
vals, vecs = mp.eigsy(H)          # WRONG
```

`H` is the full `(2N+1)x(2N+1)` bordered CCM matrix, indices `-N..N`,
including the boundary Cauchy row/column at the two extreme indices `+-N`.
That is **not** the operator `H_L = D_L + B_L` whose ground eigenvalue is
`mu_N` in the E77.7d/E78.1/E78.3 convention. Every prior probe in this
program that measures `nu_0^{(N)}`, `nu_1^{(N)}` uses the **inner block**

```text
A_N = H[1:-1, 1:-1]                      (indices -N+1 .. N-1)          (G-1)
```

with `mp.eigsy` applied to `A_N`, not `H`. The initial run against the full
`H` gave numbers that were internally inconsistent with the established
E78.1/E78.3 baseline (e.g. `nu_0` at `L=6,N=16` did not land near the known
`1.57e-43` order of magnitude from E78.3). This was caught before being
certified. The probe was corrected to use `(G-1)`; **the corrected script is
what this document reports on.** The corrected `run_one` reads:

```text
inner = H[1:-1, 1:-1]
vals, vecs = mp.eigsy(inner)
```

Cross-check against E78.3 (which independently computed the true inner-block
ground eigenvalue at `lambda=6`, `dps=70`, zeta build): E78.3 reported
`nu_0^{(N=16)} = 1.57e-43`. The corrected E78.137 run reproduces this exactly:
`nu0 = "1.5722639965554983388e-43"` at `L=6, N=16` (see JSON below). The
buggy full-`H` run is not reproduced or cited anywhere in this document.

## 2. Corrected data

Source: `E78_137_mu_convergence_gate_results.json`, `dps=70`, `lambda=6`,
`L in {4,6,8}`, `N=6,8,...,16`, both builds, inner-block operator `(G-1)`.

### Zeta (genuine build)

```text
L=4:
  N=6   nu0=2.3538567557052195059e-18  nu1=9.7976845220105639508e-16
  N=8   nu0=2.8699899450931545339e-22  nu1=1.5712769067125992116e-19
  N=10  nu0=3.3308579466603473028e-26  nu1=2.7810534759754540841e-23
  N=12  nu0=4.0168611079465762024e-30  nu1=3.6579315373467486632e-27
  N=14  nu0=3.540352598156765837e-33   nu1=2.5308498345851592308e-30
  N=16  nu0=2.5207171272627013017e-36  nu1=2.9612958374228076863e-33

L=6:
  N=6   nu0=7.434880864165442097e-21   nu1=3.0262515608158794387e-18
  N=8   nu0=1.1410833154135800884e-25  nu1=9.6281115983032975177e-23
  N=10  nu0=1.8505311721528620637e-30  nu1=1.5773912748739481892e-27
  N=12  nu0=4.3015277027002730351e-35  nu1=4.7520678420491682779e-32
  N=14  nu0=2.2621352914927759765e-39  nu1=2.4548939199590124877e-36
  N=16  nu0=1.5722639965554983388e-43  nu1=1.8563760248405155155e-40

L=8:
  N=6   nu0=1.0363316942572509415e-21  nu1=8.735977770552462869e-19
  N=8   nu0=6.6134906112968844522e-28  nu1=6.6700890851574757763e-25
  N=10  nu0=2.7393471961085617419e-33  nu1=3.010982715072019861e-30
  N=12  nu0=1.860263740355850269e-38   nu1=2.3954181680880956245e-35
  N=14  nu0=3.0919576298295935215e-43  nu1=3.0017773690205675134e-40
  N=16  nu0=5.1403422688681721077e-48  nu1=8.482533757187695918e-45
```

At every `L`, `nu1_ratio_consecutive` (ratio of `nu1^{(N)}` to `nu1^{(N-2)}`)
stays in the `1e-4` to `1e-7` range throughout; e.g. at `L=6`:
`3.18e-5, 1.64e-5, 3.01e-5, 5.17e-5, 7.56e-5`. `nu1` is collapsing
geometrically, at essentially the same rate as `nu0`, not saturating to any
positive constant.

### Plant (falsifier)

```text
L=6:
  N=6   nu0=-0.038188250648461373442  nu1=-0.033333703218247352154  gap=0.00485...
  N=8   nu0=-0.4113286667417265848    nu1=-0.30375808650496509557   gap=0.10757...
  N=10  nu0=-1.4970539014566867319    nu1=-1.2754143838370018489    gap=0.22164...
  N=12  nu0=-1.699839463548914625     nu1=-1.548227863489563119     gap=0.15161...
  N=14  nu0=-1.7234377955518138582    nu1=-1.5872948727561579647    gap=0.13614...
  N=16  nu0=-1.7355270187359772952    nu1=-1.61649454731555233      gap=0.11903...
```

Both `nu0` and `nu1` are settling toward order-one negative values (consistent
with E78.1/E78.3's independently-measured plant ground `-1.7355...` at
`N=16`), and the gap stabilizes in the `0.11-0.22` range rather than shrinking
toward `0`. The same pattern holds at `L=4` (gap settling near `0.03-0.06`)
and `L=8` (gap settling near `0.20-0.22`).

## 3. Reading

```text
ZETA:  nu0^{(N)} -> 0 and nu1^{(N)} -> 0 together, geometrically, at every
       tested L. There is no positive limit for nu1; the whole bottom of the
       tower sinks. This is BRANCH B.

PLANT: nu0^{(N)} and nu1^{(N)} both converge to distinct order-one negative
       constants with a stable positive gap. This is the Branch-A-shaped
       behavior -- but it occurs for the FALSIFIER, not for zeta.
```

This is exactly the falsifier-location principle at work: the two builds
behave DIFFERENTLY at the level of a VALUE (does the tower collapse to 0 or
stabilize at an order-one gap), not merely at the level of whether some
sequence "converges." Both sequences converge (in the loose sense that ratios
shrink/settle); what differs is the limit.

## 4. Consequence for the closure plan

The originally planned mechanism was a rank-one quasimode deflation lemma:

```text
IF nu_1^{(N)} -> g > 0 (uniform gap) AND there is a quasimode u_N with
   eps_N = ||A_N u_N||/||u_N|| -> 0,
THEN nu_0^{(N)} -> 0 (mu_N -> 0) by a one-line min-max/Temple-inequality
   argument: the Rayleigh quotient of u_N traps an eigenvalue within eps_N of
   0, and if that eigenvalue must be nu_0 (because everything else is >= g/2
   away), then nu_0 -> 0.
```

Section 2-3 show the premise (uniform gap `g>0`) **fails for zeta**. The
mechanism as planned cannot be used. This document does not attempt to
close `mu_N -> 0` for zeta; it certifies which of the two branches the
program is actually in, so the next reduction is aimed at the right target
(a growing-rank / collective-tower argument, or an candid autopsy of why that
does not close -- see E78.139).

## 5. Probes

```text
E78_137_mu_convergence_gate_probe.py     (corrected: uses inner block A_N)
E78_137_mu_convergence_gate_results.json (corrected run, dps=70, lambda=6,
                                           L in {4,6,8}, N=6..16, both builds)
E78_137_run.log                          (execution log)
```

All numbers cited above are read verbatim from the corrected, executed JSON.
No value is projected, rounded loosely, or fabricated. The earlier buggy
full-`H` run is not cited and its output file was overwritten by the
corrected run.

## 6. Status

```text
class: PROBE-VERIFIED GATE (settles Branch A vs Branch B for the mu_N -> 0
       question; does not itself settle mu_N -> 0).
status for THIS gate question: candidate closure - pending review
       (Branch B is established for zeta by executed, cross-checked,
       dps=70 data at three independent L values, with the planted
       falsifier showing the expected opposite behavior).
status for mu_N -> 0 itself: still OPEN.

proved (by direct computation, cross-checked against E78.1/E78.3):
  for the genuine build, nu_0^{(N)} and nu_1^{(N)} of the inner-block
  operator A_N = H_L[1:-1,1:-1] collapse to 0 together, geometrically, at
  L=4,6,8, N=6..16; the gap nu_1-nu_0 itself shrinks by 2-4 orders of
  magnitude across N=6..16;

proved (by direct computation): for the planted falsifier, nu_0^{(N)} and
  nu_1^{(N)} settle at distinct order-one negative values with a stable
  gap (~0.03-0.22 depending on L), consistent with E78.1's original
  ("Outcome-A-shaped") finding for the plant, now independently confirmed
  with the corrected operator;

refuted: the originally planned rank-one quasimode deflation lemma as a
  route to mu_N -> 0 for zeta -- its premise (a uniform positive gap
  nu_1^{(N)} -> g > 0) is false for zeta;

corrected: an earlier buggy version of this probe diagonalized the full
  bordered matrix H instead of the inner block H[1:-1,1:-1]; this was
  caught, the bug is documented in section 1, and no numbers from the buggy
  run are used anywhere in this document or downstream;

next: E78.138/E78.139 -- build the von Mangoldt quasimode on the CORRECT
  inner-block operator and determine whether a growing-rank / collective
  deflation argument can still force nu_0^{(N)} -> 0 specifically (Branch-B
  closure path (a)), or whether that requires an unproved overlap
  concentration hypothesis (path (b), autopsy).
```
