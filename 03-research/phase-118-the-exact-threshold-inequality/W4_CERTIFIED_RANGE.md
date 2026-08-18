# W4 — how far the interval-certified positivity of `A_T` reaches past `T = log 2`

Workstream W4, phase 118. All claims below are labelled **[measured]** (I ran
it), **[derived]** (I computed it from definitions/other measured facts) or
**[reported]** (it is stated in `main.tex` / the certificate directory and I
did not re-derive it, only located and read it). Floating point is used only
for exploration; every certificate-grade claim is Arb interval arithmetic.

## 0. Faithful summary of what `row_d_log2` actually proves

I read every file in
`04-papers/42-arithmetic-lefschetz-programme/certificates/row_d_log2/`
(`README.md`, both `*_CERTIFICATE.md` notes, the manifest, and all six
scripts) plus the corresponding passage of `main.tex`
(`§subsec:primitiveendpoints`, `thm:certifiedendpoints`).

**This is not the SPEC.md Schur-threshold machinery run in interval
arithmetic.** It is an independent, hand-built construction (phase 114, older
than phase 118) that proves positivity of the *actual infinite-dimensional*
operator `A_T` on the full space `P_T` directly, at two specific endpoints:
`T = (1/2)log 3` (D.77) and `T = log 2` (D.85), by nesting. It never forms
`rowd_threshold.py`'s `S_E`, `Z_E`, `b_E`, `A_0^dagger`; it uses a completely
different finite-dimensional reduction (cellwise Legendre polynomials, not
piecewise-constant) with closed-form exponential/digamma kernels, and proves
every stated inequality with Arb balls, not floats. **The mechanism is,
however, exactly the two-piece shape SPEC's task description guessed**: a
positive gap on a finite-dimensional projected subspace, plus a rigorous bound
on the complement — see §4 below for the precise correspondence and where it
differs from the guess.

Concretely, at `T = log 2` (`e^{2T}=4`, contacts `n=2,3` only — the "two-contact
mesh"):

- **Mesh**: `[-T,T]` split into 96 cells (pattern `d·20, e·8, d·20, d·20, e·8,
  d·20` with `d,e` chosen so cell boundaries land exactly on `±(2T-log3)`,
  i.e. the shift-by-`log3` mesh symmetry used by D.77/D.79), each carrying
  the 10 orthonormal Legendre polynomials of degree `0..9`. Total dimension
  `960`; reflection splits it into even/odd parity blocks of dimension `480`
  each.
- **Finite block (`P`)**: a spectral-gap-style Arb congruence proves
  `P A_T P + |v1><v1| + |v2><v2| >= 0.5 P` (even) and `P A_T P + |vo><vo| >=
  0.05 P` (odd), for three fixed, exactly-stored low modes `v1,v2,vo`.
- **Complement (`Q = 1-P`)**: closed exponential Grams plus a degree-9 Taylor
  remainder give `Q A_T Q > 1.5396358725 Q` and `||Q A_T P||^2 <
  0.000365731342`, hence a Schur gap `> 0.4659` (even high block) and `>
  0.0497` (odd complement).
- **The one genuinely delicate direction**: `v1`'s Rayleigh quotient is only
  known to be `> -1.746475e-6` (i.e. it could be slightly negative in the
  finite calculation). It is rescued not by a spectral gap but by a
  **positive-capacity argument**: the Gamma channel's positive high-frequency
  tail, evaluated via digamma resolvents on `B=320.5` (`"first 160 gamma
  resolvents"` plus an exact `B/4` tail lemma, D.76), is shown in the Fourier
  domain to dominate `v1`'s small negative Rayleigh defect. This is the step
  that produces the headline margin `8.6338e-8`.
- **Final assembly** (`114_d_85_two_level_endpoint_budget_verify.py`,
  standard library, `Decimal` at 80 digits) recombines four enclosures into
  the theorem.

This is an **endpoint theorem**, not a claim that row (d) is closed: it
certifies `A_T >= 0` on the *whole* `P_T` (not a Galerkin truncation) for
every `0 < T <= log 2`, nothing more.

## 1. Reproduction [measured]

**SHA-256 pins** — all five load-bearing files verify against the manifest
(`114_d_84_...py`, `114_d_85_fixed_vector_...py`, `114_d_85_capacity_...py`,
`114_d_85_two_level_...py`, `114_d_85_LOG2_..._CERTIFICATE.md`): **all OK**.

**Tier 1** (`114_d_85_two_level_endpoint_budget_verify.py`, standard library
only) reproduces every quoted number exactly:

```
big-block gap lower:              0.46597814251161183846...
v2/complement gap lower:          0.00203369728246969981...
capacity threshold / lower:       1.21106727883961186698... / 1.83281360220952728854e-6
final capacity margin:            8.63386022095124852109e-8
odd complement / final lower:     0.04975274401048942490... / 8.13856175478998041797e-6
```
Runtime: **0.109 s**.

**Tier 2** (recomputes the Arb enclosures; requires `python-flint`, run with
`PYTHONPATH=<repo>/03-research/phase-118-the-exact-threshold-inequality/vendor/rowd-flint`,
each command exactly as pinned in the manifest). I launched all eight
manifest-pinned invocations in sequence on this machine. Findings:

- Step 1 (`D84_DEG=9 D84_HIGH_GAP=1 ...114_d_84...py`) completed in
  **14 m 18.9 s** and printed `RITZ even: first=-1.7464746199529791e-06,
  next=0.0020336972824375531` — matching the certificate's quoted
  `even_rayleigh_defect_upper = 1.746475e-6` and `v2 > 0.0020336972824697` to
  the digits shown, and `PASS lifted even: ... gap > 0.5 ... disk=[0.999999999...
  +/- 5.24e-30]`, confirming the even high-block/lifted-gap claim.
- Step 2 (`D84_ODD_GAP=1`) was still running when this report was finalised.
  I did not block indefinitely on the full 8-step chain (steps 3–6 are the
  much smaller `114_d_85_fixed_vector_analytic_verify.py` single-mode
  computations, step 7 is the capacity integral, step 8 is Tier 1 again) —
  see below for an independent, complete reproduction of step 7.
- **Step 7 (the capacity integral) I reproduced independently and completely**,
  because `W4_capacity_precision_test.py` (surviving draft, reviewed — it is
  a byte-identical copy of `114_d_85_capacity_arb_prototype.py` except that
  `ctx.prec` and `NINT` are read from environment variables instead of
  hard-coded) *is* that step. At the pinned defaults (`prec=192`,
  `NINT=2000`) it reproduces
  `directed normalized delta[0,20] lower = 1.270846203583086805...` and
  `directed capacity threshold upper = 1.211067278839611866984...`
  — matching the certificate's `delta_h > 1.27084620358308` /
  `threshold < 1.2111` exactly — and prints `PASS`. Runtime: **1 m 53.0 s**
  on this machine.

**Candid status**: Tier 1 and the SHA-256 pins are fully reproduced (fast).
Tier 2's step 1 and step 7 are fully reproduced independently, with matching
numbers to displayed precision. The full 8-step Tier-2 chain is expensive
(step 1 alone: ~14 min at 512-bit precision on a 480-dimensional Arb
congruence) and was not driven to completion inside this report — I am
reporting exactly what finished, not extrapolating a total. Nothing in the
partial run disagrees with the pinned numbers.

## 2. What limits the endpoint to `log 2`

### (a) Degree / dimension of the finite reduction — [reported + derived]

The finite space is fixed by design at 96 cells × Legendre degree 9 = 960
total dimensions (480 per parity). The filename `..._degree23_...` and the
`D84_DEG` environment variable show the certificate's author *tried* a
degree-23 upgrade path, but the manifest's pinned commands all pass
`D84_DEG=9` — the actual proof uses degree 9. I did not re-run degree 23
myself (a single degree-9 parity block already costs ~14 minutes at 512-bit
precision; degree 23 would cost dramatically more and requires re-deriving
the Taylor-remainder constants for the new degree — out of scope for a
sensitivity sweep). **I cannot report a measured failure point for dimension
possibly wasn't the binding constraint at log 2**: nothing in the certificate
suggests degree 9 was pushed to its limit; it looks like a design choice that
had comfortable room (see (e)).

### (b) Tail bound on the Gamma channel — [measured + derived]

There are two different "tails" here, and only one is a genuine adjustable
cutoff:

- The Robin-resonance sum over `b_j = 2j+1/2` is truncated at `j=160`
  (`DEPTH=160`), but the remainder beyond it is controlled by an **exact**
  identity (D.76: `sum_{j>=160} E_{b_j} >= (B/4) E_B`, `B=320.5`) — this is
  not a numerically-tuned cutoff, it is a proven inequality, so "how far can
  you push it" doesn't apply the way it does to a Taylor truncation.
- The one truly adjustable numerical knob in the chain is the **directed
  Riemann lower sum for the capacity integral** (`NINT` in
  `114_d_85_capacity_arb_prototype.py` / `W4_capacity_precision_test.py`),
  which lower-bounds `delta_h` on `[0,20]`. I swept it (`W4_capacity_precision_test.py`,
  `W4_NINT=...`, `W4_PREC=192` fixed):

  ```
  NINT   50  100  120 140 160 180 185  186 187 188  189  190  195  200 ... 2000(pinned)
  result FAIL FAIL FAIL FAIL FAIL FAIL FAIL FAIL FAIL FAIL  ?   PASS PASS PASS ... PASS
  ```
  Exact crossover: **fails at `NINT=188`, passes at `NINT=190`** (189
  untested due to a background timeout, but bracketed). The pinned value is
  `NINT=2000`, i.e. **more than 10x** the minimum needed — a comfortable
  safety margin, not a value pushed to its limit.

### (c) Number of prime-power contacts — [measured]

`W4_contact_counts.py` (new script, uses `rowd_assembly.prime_powers_upto`
unmodified):

```
log2 (certified endpoint)   T=0.69315  e^2T=4.0000  contacts=[2, 3]        count=2
(1/2)log5 (next threshold)  T=0.80472  e^2T=5.0000  contacts=[2, 3, 4]     count=3
(1/2)log7                   T=0.97296  e^2T=7.0000  contacts=[2, 3, 4, 5]  count=4
(1/2)log8                   T=1.03972  e^2T=8.0000  contacts=[2, 3, 4, 5, 7]     count=5
(1/2)log9                   T=1.09861  e^2T=9.0000  contacts=[2, 3, 4, 5, 7, 8]  count=6
```
Two contacts at `log2`, growing to three at the very next threshold. This
tracks directly with §3: the retracted `(1/2)log5` attempt needed a `V_200`
space (200 "columns", vs 96 cells here) split into three sub-blocks `D5 ⊕
S163 ⊕ Y30`, i.e. the finite reduction needed to at least double, and the
proof got more complicated, not just bigger.

### (d) Arithmetic precision — [measured]

Same sweep, varying `ctx.prec` at the pinned `NINT=2000`:

```
prec   32   33-38  39   40   48   53  ...  192 (pinned)
result FAIL FAIL   PASS PASS PASS PASS ... PASS
```
Exact crossover: **fails at `prec=38`, passes at `prec=39`** (at 32-38 bits
the failure is a genuine arithmetic one — the `assert bracket > 0` inside
`directed_r_lower` fails because the digamma-resolvent bracket can't be
proven positive at that precision, not just a looser final margin). The
pinned value is `192` bits, i.e. **~5x** the minimum needed, and note `39`
bits is *less* than IEEE double precision's 53-bit mantissa. **Precision is
emphatically not the bottleneck** — a double-precision-grade ball arithmetic
would already almost suffice for this sub-step.

### (e) Sheer thinness of the margin — [derived, from measured Tier-1 numbers]

Given (b) and (d) both show >5x-10x safety factors, the real answer is (e).
Decomposing the headline `8.63386022095e-8`:

```
capacity = 1.8328136022095...e-6
ell_eff  = 1.746475000000...e-6   (= 1.746475e-6 + 4.441e-24/0.0003, second term negligible)
margin   = capacity - ell_eff = 8.6339e-8
```
Both quantities are themselves tiny (~1.7-1.8e-6) with a **~4.94% relative
margin** between them (`capacity/ell_eff - 1 = 0.04944`) — not an
astronomically fine-tuned cancellation at that level. The absolute smallness
of `8.6e-8` comes from squaring/rescaling by `h=0.0012`
(`capacity = h^2 delta/(1-h delta)`), and `h = g - eta` with `g=0.0015` the
two-level Feshbach complement gap chosen for the near-null direction `v1`.
So the real source of thinness is `g=0.0015` — a *designed* safety choice
built from `mu2=0.00203...` (v2's Rayleigh value) and the big-block gap
`0.466` via the two-level Feshbach quadratic — which is itself small because
`v1` is a genuine near-null direction of `A_T` (Rayleigh value only
`-1.7e-6` to `+1.7e-6` at this resolution). **This is a real mathematical
fact about the operator, not a numerical artifact**, and it is the same
phenomenon SPEC.md documents independently for the Schur-threshold `lam_min_norm`
(§3 below ties these together).

## 3. Attempted extension past `log 2`

**The very next threshold, `T = (1/2)log 5`, was already attempted — and
explicitly retracted — before phase 118 existed.** `main.tex` §3905-4010
(`main.tex:3905` onward, "The audited next endpoint") records it in full:

- A `V_200` Legendre space (200 dimensions) with a coercive complement bound
  `Q A_T Q > 0.218 Q`.
- Inside `V_200`, an exact nested decomposition `V_200 = D5 ⊕ S163 ⊕ Y30`,
  with directed Schur-complement lower enclosures on each block (all `> 0`).
- **The gap**: the sufficient test for the whole space needs the *coupling*
  of the 5-dimensional `D5` block to the rest of the complement —
  `kappa = ||A_{QS} A_{SS}^{-1/2}||^2` and
  `C_D = A_{DQ} - A_{DS} A_{SS}^{-1} A_{SQ}` — and the required inequalities
  `kappa < 0.218` and `K_D - (0.218-kappa)^{-1} C_D C_D^* > 0` were **never
  computed**. Quoting `main.tex:4000`: *"Neither inequality follows from the
  five-column calculation."*
- `main.tex:6202` and the `row_d_log2/README.md` both state plainly:
  `T=(1/2)log5` is **not** certified and no artifact claims it.

This is not a numerical failure (unlike (b)/(d) above, nothing there
suggests `V_200` or the block sizes were pushed to a precision/discretization
limit) — it is an **incomplete proof**: two specific cross-terms were never
derived. Redoing them requires the same kind of closed-form Legendre/Bessel
work as D.77/D.79/D.85, which is a multi-note undertaking (three phase-114
notes for the log2 endpoint alone), not a parameter sweep. I judge this is
not achievable at research-grade rigor inside this session, and I am
reporting that rather than producing a weaker, unrigorous substitute.

**What I did instead**: floating-point (non-certified, diagnostic only, per
SPEC Rules) checks using the *unmodified* SPEC Schur-threshold machinery
(`rowd_threshold.threshold_blocks`/`schur_target`), via the surviving draft
scripts (reviewed, and cross-checked — `W4_near_null_structure.py`'s
recovered minimizer eigenvalue matches `schur_target`'s reported
`lam_min_norm` to machine precision, so the scripts are computing what they
claim to):

- `W4_next_thresholds_probe.py`: `lam_min_norm` stays **positive** (no sign
  of a violation) at every step through `(13,16)` (i.e. `T` up to
  `(1/2)log16 = 2log2 ≈ 1.386`), at refinements 4 through 32, decreasing
  under refinement at every step (consistent with SPEC §2's criticality
  finding, not a new one — I did not rerun the refinement-limit question,
  which is W1's).
- `W4_near_null_structure.py` / `W4_near_null_parity_scan.py`: the
  near-null corona direction at steps `(4,5)`, `(5,7)`, `(8,9)`, `(9,11)`,
  `(11,13)` is overwhelmingly **even parity** (`even_frac ≈ 1.0000` at 4 of
  5 steps checked) and concentrates near the *outer edge of the annulus*
  (`peak_t` close to `T_new`, not `T_old`), with only 5-17% of its L2 mass
  inside the old core. This is qualitatively the same picture as the
  certified `v1` at `log2` (a near-null, even, boundary-concentrated mode) —
  suggesting every subsequent threshold needs its *own* bespoke
  capacity-style rescue for a new near-null mode, not a mechanical repeat of
  a single argument.

I found **no floating-point evidence of a sign violation** at any threshold
tested (which would have refuted row (d) outright) — this is a negative
result worth stating plainly: nothing here contradicts RH.

## 4. Does the log-2 mechanism have room to extend?

SPEC's guess — "a positive gap on an explicitly projected finite-dimensional
subspace plus a rigorous bound on the complement" — is correct for the
*coarse* structure (`P`/`Q` split, §0), but incomplete: the genuinely hard
part is not the `P`/`Q` split (that gap, `>0.4659`/`>0.0497`, is comfortable
by every measure in §2) but a **second-level reduction inside `P`** onto a
single near-null direction (`v1`), rescued by an exact positive-capacity
identity specific to that direction and that window. That is exactly the
mechanism SPEC's own §2 diagnosis (`lam_min_norm -> 0` under refinement,
"the proof must be an identity... no estimate that loses a constant factor
can work") predicts is necessary — and it is what the certificate's authors
actually built, independently, via a different (Legendre/Arb) route than
`rowd_threshold.py`'s Schur target.

**Does it have room to extend?** Structurally yes — nothing in the technique
is intrinsically capped at `log 2`. But each new threshold requires, from
scratch:
1. A new coercive complement bound `Q A_T Q >= alpha Q` for a *larger* mesh
   (dimension grows with contact count, §2(c): 2 contacts at `log2`, 3 at
   `(1/2)log5`, 4 at `(1/2)log7`, ...).
2. Identifying the *new* near-null direction(s) the enlarged corona
   introduces (§3's float diagnostics suggest there is at least one new
   even, boundary-concentrated one at every threshold checked).
3. A fresh capacity-style argument for each such direction — which is what
   the retracted `(1/2)log5` attempt got stuck trying to do, on cross-terms
   that were never completed.

So the mechanism is not exhausted mathematically, but it is **not a
mechanical extension either** — SPEC §0's exactness of the step (`old core
carries over with no correction`) removes re-verification of the *old*
core, but it does nothing to shrink the *new* work at each threshold, which
is what actually dominates the effort (three phase-114 notes for `log2`
alone, and an incomplete fourth for `(1/2)log5`).

**Connection to RESUME.md (d) and (c-NEW):**
- (d)'s finding — `lambda_min(A_0)` (the SPEC threshold-Schur core block)
  decaying toward 0 under refinement — is the Schur-formalism's version of
  the same phenomenon the certificate had to work around with the capacity
  argument for `v1`. It says any proof strategy that tries to bound the
  penalty `b_E^* A_0^dagger b_E` by a *generic* operator-norm estimate
  (rather than an exact identity) is doomed, which is consistent with why
  the certificate needed a bespoke capacity lemma rather than a generic
  spectral-gap argument.
- (c-NEW)'s open question — whether `lam_min_norm` truly `-> 0+` or to a
  positive limit — does not change today's answer (the `log2` certificate
  does not depend on it; it never uses `rowd_threshold.py`'s formalism). But
  it is directly relevant to *how hard future thresholds will be*: if the
  true limit is `0`, the analogue of `g=0.0015`/margin-`8.6e-8` at `log2`
  should be expected to shrink further at later thresholds (harder, not
  easier, bespoke capacity arguments each time); if it converges to a
  positive limit, the per-threshold work is bounded rather than escalating.
  I did not resolve this (it is W1's question) — I only note that it bears
  directly on the *practical* (not mathematical) extensibility of the
  log-2 mechanism.

## 5. Strongest unconditional, interval-certified theorem

**`A_T >= 0` for all `0 < T <= log 2`.**

This is exactly `thm:certifiedendpoints` / `cor:certifiedinitialinterval` of
`04-papers/42-arithmetic-lefschetz-programme/main.tex`, backed by
`certificates/row_d_log2/`. I did **not** improve on `X = log 2` — see §3.

**Reproduction** (from
`04-papers/42-arithmetic-lefschetz-programme/certificates/row_d_log2/`):

```
# Tier 1 (fast, no dependencies) — recombines certified enclosures:
python3 114_d_85_two_level_endpoint_budget_verify.py                    # 0.109 s

# Tier 2 (recomputes the Arb enclosures; needs python-flint):
FLINT=<repo>/03-research/phase-118-the-exact-threshold-inequality/vendor/rowd-flint
D84_DEG=9 D84_HIGH_GAP=1 PYTHONPATH=$FLINT python3 114_d_84_log2_degree23_projected_gap_arb_verify.py   # 14m19s [measured, this run]
D84_DEG=9 D84_ODD_GAP=1  PYTHONPATH=$FLINT python3 114_d_84_log2_degree23_projected_gap_arb_verify.py   # [launched; see §1]
                         PYTHONPATH=$FLINT python3 114_d_85_fixed_vector_analytic_verify.py
D85_VECTOR=2             PYTHONPATH=$FLINT python3 114_d_85_fixed_vector_analytic_verify.py
D85_VECTOR=odd           PYTHONPATH=$FLINT python3 114_d_85_fixed_vector_analytic_verify.py
D85_GENERIC_BOUNDS=1     PYTHONPATH=$FLINT python3 114_d_85_fixed_vector_analytic_verify.py
                         PYTHONPATH=$FLINT python3 114_d_85_capacity_arb_prototype.py                   # 1m53s [measured, this run]
                         python3 114_d_85_two_level_endpoint_budget_verify.py
```

**Runtime**: Tier 1, 0.109 s. Tier 2, per-step measured where completed
(step 1: 14m19s; the capacity step, reproduced independently via
`W4_capacity_precision_test.py` at pinned settings: 1m53s); the full 8-step
chain was still running at report time and likely totals on the order of
30-60 minutes on this machine (**this total is an estimate, not a
measurement** — I am reporting only the two steps I actually timed to
completion).

**What would be needed to push past `log 2`**: complete the two missing
cross-term bounds (`kappa = ||A_{QS}A_{SS}^{-1/2}||^2 < 0.218` and
`K_D - (0.218-kappa)^{-1}C_D C_D^* > 0`) for the already-attempted
`(1/2)log5` endpoint (`main.tex` `eq:logfivecomplement` through
`eq:logfivegershgorin`, `main.tex:3905-4010`) — i.e. finish the fourth
phase-114-style note the earlier attempt left incomplete. That is a
substantial hand-derivation (closed-form Legendre/Bessel/digamma work
comparable to D.77+D.79+D.85 combined), not a numerical sweep; nothing found
in this workstream shortcuts it.

## Files

- `scripts/W4_contact_counts.py` — new; §2(c).
- `scripts/W4_capacity_precision_test.py` — surviving draft, reviewed and
  reused as-is (confirmed byte-identical to the certificate's capacity
  script modulo env-var parameterization); used for §1, §2(b), §2(d).
- `scripts/W4_next_thresholds_probe.py`, `W4_near_null_structure.py`,
  `W4_near_null_parity_scan.py` — surviving drafts, reviewed (cross-checked
  `W4_near_null_structure.py`'s recovered eigenvalue against
  `schur_target`'s `lam_min_norm`: matched to machine precision), reused
  as-is; used for §3.
- Did not modify `rowd_assembly.py` or `rowd_threshold.py`.
- Did not modify anything in `04-papers/` or `certificates/row_d_log2/`; all
  work there was read-only reproduction.
