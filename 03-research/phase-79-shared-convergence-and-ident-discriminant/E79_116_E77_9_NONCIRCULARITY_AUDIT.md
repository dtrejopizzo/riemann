# E79.116 - E77.9 non-circularity audit of the surviving mechanism

**Scope:** whole-program audit (the E77.9 milestone, carried into phase 79).
**Class:** AUDITORIA. Closes the E77.9 open item at audit grade.

## 0. What this document can and cannot close

E77.9 requires auditing the surviving mechanism against `K1-K5` (E72.7), the
zero-filter gate (E72.16, refined by E77.7az), and the walls `MW-1..MW-6`
(NO-GO-LIST). It is marked "required before any closure claim".

Two candid scope limits, stated up front:

```text
1. There is NO closure claim to audit. Almost every link in the chain is
   open. What is audited here is the ROUTE -- the objects the program
   intends to prove and the arguments it intends to use -- not a proof.
2. An audit of a route is PROVISIONAL. Each item must be re-audited when
   the corresponding step is actually proved, because a proof can violate
   a gate that its statement does not.                                  (116-1)
```

Within those limits this document is complete: every live object in the
chain is checked against every gate, and the exposures are named.

## 1. The gates, as written

```text
K1 inverse smuggling      -- construction uses C_x^{-1}b_x, Riesz projections
                             of the UNKNOWN low spectral island, or the
                             endpoint resolvent.
K2 local inverse          -- C_x^{-1} expanded as a sum over prime-place
                             inverses (the phase-65 additive Green mistake).
K3 absolute ceiling       -- bounding sum |cell_{p,k}| BEFORE cancellation.
K4 point-local kernel     -- a Christoffel/Jacobi kernel made into an
                             evaluator at a zeta zero.
K5 endpoint identity      -- limiting object identified with the arithmetic
                             target using ONLY a scalar determinant.

E72.16  any annihilation by scalar Mellin limits must produce a nonzero
        analytic zero-filter whose divisor contains the off-critical zeta
        divisor. Admissible ONLY if built from finite CCM data without
        using zero locations or Xi as input.
E77.7az CONVERGENCE claims must be build-neutral; DISCRIMINANT claims
        require separation but may not use zero LOCATION.

MW-1/MW-4 no reduction to positivity.
MW-2/MW-3 no per-prime / local-to-global assembly.
MW-5      no dependence on the arithmetic-site package.
MW-6      no uniform-spectral-gap statement that is RH-equivalent.        (116-2)
```

## 2. Audit table

```text
object                          K1  K2  K3  K4  K5  E72.16  MW    verdict
LP-A1 FESHBACH-RITZ-ENVELOPE    !   OK  OK  OK  OK  OK      OK    EXPOSED (K1)
LP-A2(a) safe-row separation    OK  OK  OK  OK  OK  OK      OK    CLEAN (proved)
LP-A2(b) Schur regularization   OK  OK  OK  OK  !   OK      OK    EXPOSED (K5)
LP-A2(c) pencil compatibility   X   OK  OK  OK  OK  X       OK    INADMISSIBLE
LP-A2(d) normalized l2 class    see s.4                           SPLIT
LP-A2(e) simplicity at mu_L     X   OK  OK  OK  OK  X       OK    INADMISSIBLE
LP-A2(f) disk-intersection      OK  OK  OK  OK  OK  OK      OK    CLEAN (open)
IDENT E77.6 cofinal diagonal    OK  OK  OK  OK  OK  OK      OK    CLEAN (proved)
IDENT GAP-Z                     OK  OK  !   OK  OK  OK      !     EXPOSED (K3,MW-6)
IDENT DISCRIMINANT              OK  OK  OK  OK  OK  OK      OK    CLEAN (open)
IDENT OUTER-LIMIT (point 7)     OK  OK  OK  OK  OK  OK      OK    CLEAN (cond.)
K_N spectral shift (E78.152)    OK  OK  OK  OK  OK  OK      OK    CLEAN (proved)
3-way decomposition (E78.157)   OK  OK  OK  OK  OK  OK      OK    CLEAN (proved)
MESH, BND bounds                OK  OK  OK  OK  OK  OK      OK    CLEAN (proved)
RDP-SHELL                       OK  OK  OK  OK  OK  OK      OK    CLEAN (open)
PROLATE + WEIL-TAIL             OK  OK  OK  OK  OK  OK      !     EXPOSED (MW-1)
SAFE-PROLATE-BRIDGE / SR-SAFE   OK  OK  OK  OK  OK  OK      !     EXPOSED (MW-1)
Omega7 (Li-Keiper)              see s.5                           STRUCTURAL
```

Legend: `OK` no exposure; `!` real exposure, route still admissible if the
named condition is respected; `X` gate violated, object inadmissible as a
proof step.

## 3. Findings that change the route

### 3.1 A2(c) and A2(e) are inadmissible, not merely unproved

Both subclauses are pinned to `mu_L`, and E78.1/E78.2 showed the pinned
quantities reduce to the `mu_L`-location/gap discriminant
(`mu_L ~ 0` zeta, `~ -1.74` plant). By E77.7az they are DETECTORS on the LP
side, where the claim is a CONVERGENCE claim and must be build-neutral.

They additionally have K1 exposure: `mu_L` is exactly the unknown endpoint,
so any quantity evaluated at `mu_L` is evaluated at the unknown low spectral
island.

```text
CONSEQUENCE: A2(c) and A2(e) must not appear as steps in the LP proof.
E78's "KEY CORRECTION" already says the build-neutral-by-nature claim was
WRONG for the mu_L-pinned subclauses. This audit records the stronger form:
they are not repairable in place, and A2(f) must be assembled from the
mu-FREE remnant (a) plus NEUTRAL-GROUND-CAUCHY, as E78 already prescribes.
```

**This is a deficit, not a saving.** E77.7aj requires the interface theorem
to CONTAIN pencil compatibility (its clause 3) and simplicity/nonvanishing
at `mu_L` (its clause 5). The requirement is untouched by this audit; only
the available realization is removed. Either A2(f) is re-derived without
them (E78's bet, NOT DONE -- hence item 7 OPEN), or `mu`-FREE REPLACEMENTS
must be built, and none exist. See E79.117 s.4.

### 3.2 GAP-Z: K3 exposure in the E79.3 edge budget

The E79.3 chain arrived at an "edge budget" (E79.3g/3h): `N|ZERO^common|` is
numerically explained by `[active edge width ~ cN] x [one shell ~ const/N^2]`.
That is a sum of absolute shell contributions **before cancellation** -- the
K3 shape exactly.

E79.3k then found the active edge is essentially sign-coherent, i.e. there is
no short-range cancellation to exploit.

```text
CONSEQUENCE: the edge budget is admissible as a DIAGNOSTIC of why the
exponent sits near 1. It is NOT admissible as an upper bound in a proof of
GAP-Z. Any future GAP-Z argument that bounds |ZERO| by summing shell
magnitudes is K3-blocked and must be rejected on sight.               (116-3)
```

This is the sharpest practical output of the audit: it rules out the shape
of argument that ~60 documents of the E79.3 chain were implicitly circling.

### 3.3 GAP-Z: MW-6 exposure, defused by build-neutrality

GAP-Z is a uniformity statement (summable in `N`, locally uniformly in
`sigma`). MW-6 says a uniform spectral-gap statement of that shape is
RH-equivalent. The defence is structural and must be preserved:

```text
GAP-Z is required to hold for BOTH builds. The plant HAS an off-line zero
and must still satisfy GAP-Z. A statement satisfied by a build with an
off-line zero cannot be RH-equivalent.                                (116-4)
```

```text
CONSEQUENCE (audit rule): any proposed proof of GAP-Z that uses a
build-discriminating input immediately loses this defence and collapses
onto MW-6. Build-neutrality is not a stylistic preference here; it is the
only thing keeping GAP-Z off the wall.
```

### 3.4 MW-2/MW-3 are clean, and structurally so

The arithmetic enters the mechanism only through `x_j = (A_N^{-1} b)_j` and
the absolutely convergent Euler data on `Re(s) > 1` (P76.039, theorem-grade).
There is no per-prime decomposition and no local-to-global assembly anywhere
in the surviving route. `K2` is clean for the same reason.

This is the one part of the program that is robustly off its wall.

### 3.5 E72.16: the Xi in OUTER-LIMIT is not a zero-filter

OUTER-LIMIT identifies the fixed-L limit with `2 Xi'/Xi`, which uses `Xi`.
The gate forbids using `Xi` **as an input to manufacture the divisor**.

```text
Here Xi appears as the TARGET of an identification on Re(s) > 1, reached
through absolutely convergent Euler data, and no zero location is used.
The plant's failure is detected by arithmetic mismatch (E77.6: 10.98-50.47),
not by evaluating anything at a zero.                                 (116-5)
```

Verdict: admissible. But the audit rule is that the identification must stay
on `Re(s) > 1` -- the moment any step evaluates the identification at or near
a zero, E72.16 and K4 both fire.

### 3.6 The planted control is not a K4 violation

`planted=(gamma, beta, strength)` builds a known off-line zero by
construction. That is a zero location, and it is known.

```text
It is used ONLY as a falsifier control -- to check that the plant fails
where it must. It never enters the forcing step for zeta. That is the
legitimate use and it stays legitimate as long as no quantity computed
from the plant's known gamma is transported into the zeta argument. (116-6)
```

No current object does that. Flagged for re-audit on any future
cross-build construction.

## 4. A2(d) / point 2: the two options split on K1

This is the finding most likely to change what gets worked on next.

E78.151 reduced point 2's existence clause to a single scalar residue
`alpha_mu = ell(P_mu b)`, with two routes:

```text
(i)  alpha_mu non-vanishing  -- the c_0 lower bound (E78.145/146), known hard;
(ii) projective convergence  -- P_N b_N / ell_N(P_N b_N) converges in the safe
     Cauchy topology EVEN IF the residue -> 0.                        (116-7)
```

The audit separates them on non-circularity, not only on difficulty:

```text
Option (i) uses P_mu, the Riesz projection at the TRUE mu_L -- a Riesz
projection of the unknown low spectral island. That is the K1 shape as
written in E72.7.  ==> K1-EXPOSED.

Option (ii) asks only that a DIRECTION computed from finite sections
converge. No projection at the unknown endpoint, no endpoint resolvent.
==> K1-CLEAN.                                                          (116-8)
```

```text
CONSEQUENCE: option (ii) is preferred on TWO independent grounds --
it sidesteps the known-hard c_0 bound AND it is the only one of the two
that clears K1. Option (i) should be treated as archived, not as a
fallback.
```

The known obstruction to (ii) is unchanged and is not a gate issue: E78.1
shows the zeta ground gap collapses geometrically to 0, so the
one-dimensional-cluster formulation of `P_N` is not obviously stable. That is
a mathematical problem, not a circularity problem.

## 5. Omega7 and MW-1: the structural question

The chain terminates in `Omega7 = Li-Keiper lambda_n >= 0`, a positivity
statement equivalent to RH. MW-1/MW-4 say positivity routes are dead.

The program's answer, which this audit records rather than invents, is the
CAND-1 position established in phase 71: the spectrum is real **by algebra**,
and the RH content is carried by **operator convergence**, not by a
positivity bound. Positivity is the CONCLUSION, derived from SR-SAFE; it is
never the METHOD.

```text
Audit rule (the single most important one in this document):
no step ANYWHERE in the chain may be discharged by proving an inequality
of positivity type. The moment a link is closed by a positivity argument,
the chain re-enters MW-1/MW-4 and the whole route is dead.             (116-9)
```

Two downstream objects are exposed here and must be watched:

```text
- PROLATE + WEIL-TAIL: "Weil" is a positivity functional. The pairing must
  be used as an identity/tail-matching device, NOT as a positivity bound.
- SAFE-PROLATE-BRIDGE / SR-SAFE: the bridge to Omega7 is where a positivity
  argument would be most tempting and least visible.
```

Both are OPEN and neither has a proposed proof, so nothing is violated yet.
They are the highest-risk MW-1 sites in the program and should carry this
flag explicitly when they are attacked.

## 6. Status

```text
proved     : nothing (this is an audit).
closed     : E77.9 at AUDIT GRADE for the current route.
found      : A2(c), A2(e) INADMISSIBLE (not merely unproved) -- K1 + E77.7az;
             E79.3 edge budget is K3-blocked as a proof device;
             GAP-Z's MW-6 defence rests entirely on build-neutrality;
             point 2 option (i) is K1-EXPOSED, option (ii) is K1-CLEAN;
             MW-2/MW-3/K2 robustly clean (arithmetic only via Re(s)>1);
             OUTER-LIMIT's use of Xi is admissible but must stay on Re(s)>1.
open       : re-audit is REQUIRED for each item when its step is proved;
             PROLATE/WEIL-TAIL and SAFE-PROLATE-BRIDGE carry live MW-1 risk.
next       : the audit does not advance any proof. It constrains which
             arguments are allowed. See E79.117 for the updated ledger.
```

## 7. Consequence

E77.9 is closed at audit grade. The route as it currently stands does not
violate any gate, **provided** four rules are respected going forward:

```text
R1. A2(c) and A2(e) never appear as proof steps; A2(f) assembles from the
    mu-free remnant only.
R2. No GAP-Z argument may bound |ZERO| by a sum of shell magnitudes (K3).
R3. No GAP-Z argument may use a build-discriminating input (MW-6).
R4. No link anywhere is discharged by a positivity inequality (MW-1/MW-4).
```

Rules R1-R4 are the operative output of this document. They are worth more
than the audit verdict itself, because each one forbids a specific class of
argument that the program has already shown a tendency to drift toward.
