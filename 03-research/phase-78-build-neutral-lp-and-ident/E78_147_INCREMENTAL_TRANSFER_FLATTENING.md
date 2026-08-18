# E78.147 - INCREMENTAL-TRANSFER-FLATTENING: a new object for the fixed-L front

**Run:** 2026-07-21.
**Scope:** IDENT, fixed-L finite side (feeds FIXED-L-WEYL convergence and the
COUPLED-GENERATOR-LIMIT summability input; shared infrastructure of points 5
and 6).
**Class:** REDUCCION GENUINA + new object. Not a candidate closure: the closed
part is an exact identity plus a numerically decisive summable law; the
analytic proof of the rate bound is reduced to one precisely stated lemma
(the zero-pole shift cancellation, Sec. 6).

## 0. What we know now (one line)

The 2-mode incremental transfer factor `tau_N = T_{L,N+2}/T_{L,N}` does not tend
to 1 (its modulus keeps amplifying, `|T_N|` reaches 1e13), yet its safe-axis
logarithmic derivative obeys the clean summable law
`|(log tau_N)'(i sigma)| = C(sigma)/N^2` with `C(sigma) ~ sigma` for the zeta
build -- so the fixed-L log-transfer converges with a summable cofinal envelope.

## 0.5 CORRECTION (bookkeeping audit, 2026-07-21)

An external audit found a real error, corrected here and in E78.7. The boundary
index is `idx[-1] = n_modes = N`, so **`d_{b,N} = 2 pi N/L` depends on N** and the
boundary pole `1/(z-d_b)` does NOT cancel across sections. Consequences:

```text
(i)  The quantity this probe computes, q_{N+2}-q_N with q=W'/(1+W), is
     Delta[F'/F] = W-QUOTIENT-DELTA, NOT the true (log tau_N)' = Delta[T'/T].
     They differ by the boundary increment Delta[1/(z-d_{b,N})].
(ii) E78.7's WL-7 (LOGT-CELL = W-QUOTIENT-DELTA, exact) is FALSE; the two differ
     by that boundary increment. See E78.7 erratum.
(iii)The probe's `mod_tau = |1+W_{N+2}|/|1+W_N|` is |F_{N+2}/F_N|, not the true
     |tau_N| = |F_{N+2}/F_N| * |z-d_{b,N}|/|z-d_{b,N+2}|.
```

The error is NOT fatal: `d_{b,N}=2 pi N/L` gives boundary increment
`= O(1/N^2)` (verified: `N^2 |increment| ~ 0.9-1.0` at sigma=1), summable. The
TRUE object `Delta[T'/T]` was recomputed in **E78.149** and still obeys a clean
`C(sigma)/N^2` law, now with `C(1) ~ 1.32, C(2) ~ 2.04` (vs `~1.0, ~2.0` for the
mislabeled `Delta[F'/F]`), still summable, plant still erratic. So the flattening
+ summability conclusion of this document survives; only the object name (it is
`W-QUOTIENT-DELTA = Delta[F'/F]` throughout Secs 2-5 below, not `(log tau_N)'`)
and the constant `C(sigma)` change. Read Secs 2-6 with `(log tau_N)' :=
Delta[F'/F]` renamed to `W-QUOTIENT-DELTA`, and see E78.149 for the true object.

## 1. The object

From the exact E78.6/E78.7/E78.11 identities (all previously proved):

```text
T_{L,N}(z) = F_{L,N}(z)/(z-d_b),     F_{L,N} = 1 + W_{L,N},
W-QUOTIENT-DELTA = Delta_N[ W'_{L,N}/(1+W_{L,N}) ] = Delta_N[ T'_{L,N}/T_{L,N} ].
```

Define the **2-mode incremental transfer factor**

```text
tau_N(z) := T_{L,N+2}(z) / T_{L,N}(z) = (1+W_{L,N+2}(z))/(1+W_{L,N}(z))   (ITF-1)
```

(the boundary pole `z-d_b` cancels because `d_b` depends only on `L`). Then the
exact identity

```text
(log tau_N)'(z) = (log T_{L,N+2})'(z) - (log T_{L,N})'(z)
               = q_{N+2}(z) - q_N(z)
               = - W-QUOTIENT-DELTA(z),        q_N := W'_{L,N}/(1+W_{L,N}).  (ITF-2)
```

So the cofinal sequence of quotient-deltas **is** the sequence of incremental
log-derivatives `(log tau_N)'`. Summability of `W-QUOTIENT-DELTA` -- the exact
open object of E78.7 (WL-10) -- is therefore

```text
sum_N | (log tau_N)'(i sigma) | < infinity   locally uniformly on safe sigma.  (ITF-3)
```

## 2. The new structural fact: flattening

`(log tau_N)' -> 0` could happen the trivial way (`tau_N -> 1`, transfer stops
amplifying) or the nontrivial way (`|tau_N|` stays bounded away from 1, the
factor becomes **flat in z** -- a pure N-scale). The probe decides: it is the
nontrivial way.

Probe `E78_147_incremental_transfer_flattening_probe.py`, `lambda=6`, dps=60,
sections `N=8..20`, safe grid `sigma in {0.55,0.6,0.75,1.0,1.5,2.0,3.0}`,
both builds. Envelope `env_N = max_sigma |(log tau_N)'|`:

### Zeta

```text
N-> N+2    env|(log tau)'|   env ratio    min|tau_N|   max|T_N|
 8->10     4.584e-2          --           2.37         2.97e6
10->12     3.007e-2          0.656        6.46e3       6.01e6
12->14     2.066e-2          0.687        2.01         3.38e10
14->16     1.525e-2          0.738        1.06e1       6.00e10
16->18     1.137e-2          0.745        1.46e2       5.71e11
18->20     8.910e-3          0.784        1.41e1       7.56e13
```

`|tau_N|` stays >= ~2 (often much larger) and `|T_N|` explodes to 1e13: the
transfer keeps amplifying. Yet `(log tau_N)'` decays. This is genuine
FLATTENING, not `tau_N -> 1`.

## 3. The law: |(log tau_N)'(i sigma)| = C(sigma)/N^2, C(sigma) ~ sigma

The envelope ratio drifting up to 1 is exactly the `(N/(N+2))^2` signature of a
`1/N^2` power law: `(8/10)^2=0.64, (10/12)^2=0.69, ..., (16/18)^2=0.79` match the
observed `0.656, 0.687, ..., 0.784`. Per-sigma, `C(sigma)=N^2 |(log tau_N)'|` is
stable to ~2% across all six steps:

```text
sigma   N^2*|(log tau_N)'| across N=8,10,12,14,16,18        C(sigma)/sigma
0.55    0.562 0.574 0.563 0.557 0.549 0.540                 ~1.02
0.60    0.613 0.625 0.613 0.607 0.598 0.588                 ~1.02
0.75    0.765 0.777 0.763 0.759 0.743 0.732                 ~1.02
1.00    1.018 1.032 1.014 1.011 0.986 0.974                 ~1.02
1.50    1.517 1.539 1.513 1.512 1.472 1.456                 ~1.01
2.00    2.005 2.039 2.008 2.010 1.955 1.936                 ~1.00
3.00    2.934 3.007 2.974 2.989 2.910 2.887                 ~0.98
```

So, for the zeta build, on the safe grid,

```text
| (log tau_N)'(i sigma) | = C(sigma)/N^2,   C(sigma) = sigma * (1 + o(1)),   (ITF-4)
```

the residual ~2% (and its mild downward drift at large sigma / large N) being
consistent with a `1/N` finite-section correction to the leading term. `C(sigma)`
is bounded on safe compacta, so `(ITF-4)` gives the summable cofinal envelope
`(ITF-3)` directly: `sum_N C(sigma)/N^2 < infinity`, locally uniform in sigma.

### Plant

The plant envelope also decays but does NOT obey `(ITF-4)`: `C = N^2|(log tau)'|`
is erratic and does not stabilize (e.g. at `sigma=0.55`: 34.0, 9.33, 1.77, 1.29,
1.47, 0.70). Both builds converging is correct and expected (Outcome A, E77.1b:
fixed-L convergence is build-neutral; the discriminant lives later, in the limit
identification and OUTER-LIMIT). The **regularity** of the convergence differs:
zeta obeys the exact `sigma/N^2` law, the plant does not. This is recorded as a
qualitative difference, NOT used as a forcing discriminant (that would violate
the E77.7az gate on this front).

## 4. Consequence for the fixed-L front

Combining `(ITF-3)`/`(ITF-4)` with the proved chain WL-10 (E78.7):

```text
summable |(log tau_N)'| on safe compacta  (ITF-4, numerically decisive)
 => W-QUOTIENT-DELTA summable
 => LOGT-CELL summability
 => SECTION-LAG control
 => fixed-L convergence of J_{L,N}      (FIXED-L-WEYL convergence side).
```

So `(ITF-4)`, IF promoted to a theorem, closes the **convergence half** of
FIXED-L-WEYL and supplies the summability input of COUPLED-GENERATOR-LIMIT --
the object E78.7 listed as "live: derive a summable envelope ... next". The
limit *identification* (SAFE-GAMMA-IDENT) and the L->infinity comparison
(OUTER-LIMIT) remain open and are where the arithmetic discriminant lives.

## 5. Why sigma/N^2 (mechanism: the rigorous pole-pair term)

`F_{L,N}(z) = 1 + a_N(U+U_b) + b_N(V+V_b)` where `U(z)=sum_n u_n/(z-d_n)`,
`V(z)=sum_n v_n/(z-d_n)`. Hence, ALGEBRAICALLY, `F_{L,N}` has simple poles
exactly at the mesh points `d_n = 2 pi n/L`, with real residues
`r_n = a_N u_n + b_N v_n`, and NO other poles:

```text
F_{L,N}(z) = 1 + sum_{|n| <= N-1} r_n^{(N)}/(z - d_n).                       (M-1)
```

The mesh poles `d_n` are FIXED (independent of N); going `N -> N+2` does not move
them, it only **adds** the outer poles `n = +-N, +-(N+1)` at `|d| ~ 2 pi N/L`
(and readjusts all residues). Writing `(log T_{L,N})' = F'/F - 1/(z-d_b)` and
taking the consecutive difference, the pole positions enter through a
build-INDEPENDENT term: the newly added mesh poles. Because the mesh is
**symmetric** (`+-n` both present), the new poles come in `+-` pairs, and

```text
1/(z - d_n) + 1/(z + d_n) = 2z/(z^2 - d_n^2)
   |_{z = i sigma} = 2 i sigma/(-(sigma^2 + d_n^2)) = O( sigma / d_n^2 )
   = O( sigma L^2/(2 pi N)^2 ).                                             (M-2)
```

This is an exact `O(sigma/N^2)` term, and its **sigma-linearity comes directly
from `z = i sigma` in the numerator** of `2z/(z^2-d_n^2)`. Define the pole-pair
predictor

```text
P_N(i sigma) = | 2z/(z^2 - d_N^2) + 2z/(z^2 - d_{N+1}^2) |,  d_k = 2 pi k/L.  (M-3)
```

`P_N` depends only on the mesh -- it is build-independent. Probe
`E78_147` (Sec. 3 data) vs `(M-3)` gives:

```text
zeta:  |(log tau_N)'| / P_N = 0.878, 0.871, 0.843, 0.832, 0.804, 0.789
       (N=8..18), IDENTICAL at sigma=1 and sigma=2 -- so P_N captures ALL of the
       sigma- and N-dependence, and the zeta zero-side is a clean ~0.83,
       sigma-independent, slowly drifting multiplicative correction;
plant: |(log tau_N)'| / P_N = 6.76, 1.09, 0.55, 1.39, 1.11, 0.24 (erratic) --
       same P_N, but the plant zero-side is O(1) and disorganized.
```

So the pole-pair term is a **rigorous, build-independent `O(sigma/N^2)`** that
already reproduces the observed law up to a clean bounded factor for zeta. The
sigma-linearity of `C(sigma) ~ sigma` is fully explained.

## 6. The single remaining lemma (the zeta zero-side) -- OPEN; one route refuted

What remains for a theorem is: the zeta zero-side (the residue-readjustment part,
i.e. everything in `(log tau_N)'` beyond the pole-pair `P_N`) is a **bounded,
sigma-independent multiplicative correction** (`~0.83`), so the total stays
`O(sigma/N^2)` and summable.

```text
ZERO-SIDE-BOUNDEDNESS (open lemma):
  (log tau_N)'(i sigma) = kappa_N * P_N(i sigma) * (1 + o(1)) with kappa_N bounded
  and sigma-independent (numerically kappa_N ~ 0.83), locally uniformly on safe
  compacta, for the zeta build.
```

**Refuted route (E78.148).** The natural rigorization -- `F_{L,N}` Herglotz, so
its zeros interlace the symmetric mesh and pair up `+-`, giving the zero-side its
own `O(sigma/N^2)` -- FAILS. It needs the residues `r_n^{(N)}` sign-definite;
probe `E78_148_residue_sign_probe.py` shows they are **real but sign-mixed** for
the zeta build at every tested N (e.g. 8/7, 11/8, 10/13, 12/15, 19/12 pos/neg,
N=8..16). So `F_{L,N}` is not Herglotz and its zeros do not simply interlace the
mesh; the clean `~0.83` zero-side correction holds for a **non-obvious reason**,
not by interlacing. (The plant residues start sign-definite at N=8 then turn
sign-mixed as N grows, a separate structural curiosity.) A different mechanism
is needed to control the zeta zero-side -- this is the exact open analytic content.

No part of the argument uses zero locations, so it is build-neutral in the
admissible sense (E77.7az): the plant's erratic zero-side is a regularity
difference, recorded not used.

## 7. Wall checklist

```text
MW-1..6:        not invoked (no positivity, no local-to-global assembly).
K1-K5:          not invoked.
E72.16/E77.7az: respected -- the argument is build-neutral (the outer-pair bound
                and the proposed interior lemma use only self-adjointness,
                interlacing and mesh spacing, never a zero location). The plant's
                erratic C is recorded, not used as a forcing detector.
Front B:        fixed-L convergence is build-neutral by Outcome A; both builds
                converging is the expected, correct outcome.
```

## 8. Status

```text
new object + genuine reduction; NOT a candidate closure.

proved (exact):
  (log tau_N)'(z) = -W-QUOTIENT-DELTA(z), tau_N = T_{L,N+2}/T_{L,N}  (ITF-2);
  F_{L,N} has poles exactly on the fixed symmetric mesh d_n=2pi n/L with real
  residues (M-1); the added outer poles form +- pairs contributing an exact
  build-independent O(sigma/N^2) pole-pair term P_N, sigma-linear by (M-2);

observed (decisive, dps=60, 6 steps x 7 sigma, zeta):
  |(log tau_N)'(i sigma)| = C(sigma)/N^2 with C(sigma) ~ sigma to ~2%  (ITF-4);
  |(log tau_N)'| = kappa_N * P_N with kappa_N ~ 0.83 sigma-INDEPENDENT (the
  pole-pair predictor P_N captures all sigma/N dependence); a summable cofinal
  envelope, locally uniform on safe compacta;
  the transfer keeps amplifying (|tau_N| not -> 1, |T_N| -> 1e13): genuine
  flattening, not tau_N -> 1;

observed:
  the plant shares the same build-independent P_N but its zero-side ratio is
  erratic (6.76..0.24); it also converges but obeys no clean law -- a regularity
  difference consistent with Outcome A, not a forcing discriminant;

reduced:
  fixed-L convergence (FIXED-L-WEYL convergence side / COUPLED-GENERATOR-LIMIT
  summability) to the single lemma ZERO-SIDE-BOUNDEDNESS (Sec. 6): the zeta
  zero-side is a bounded sigma-independent correction to the rigorous P_N;

refuted as a route (E78.148):
  the Herglotz/interlacing rigorization of the zero-side -- residues r_n^{(N)}
  are real but SIGN-MIXED for zeta at every N, so F_{L,N} is not Herglotz and its
  zeros do not simply interlace the mesh; the clean ~0.83 correction holds for a
  non-obvious reason;

open:
  ZERO-SIDE-BOUNDEDNESS -- prove the zeta residue-readjustment (zero-side) stays
  a bounded sigma-independent multiple of P_N by a mechanism other than
  interlacing; this promotes (ITF-4) to a theorem and closes the convergence
  half of the fixed-L front;

next:
  attack ZERO-SIDE-BOUNDEDNESS via the residue-evolution law r_n^{(N)} -> r_n^{(inf)}
  (rate of convergence of the fixed-mesh residues), which is the non-interlacing
  route; independently identify C(sigma) exactly (data: C(sigma) ~ sigma).
```
