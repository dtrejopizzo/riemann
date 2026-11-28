# Re-audit of 03-research phases 0–99 against window positivity (Paper 46)

Target recalled: $m(\tau)=\Re\psi(\tfrac14+\tfrac{i\tau}2)-\log\pi$, $s_T=m-\sum_{\log n<2T}v_n\cos(\tau\log n)$,
$\mathfrak a_T(F)=\frac1{2\pi}\int s_T|\hat F|^2$ on $\mathcal P_T$ (Tate-moment-free $F\in L^2(-T,T)$); target
$\lambda_A(T)\ge0\ \forall T$. Open reduced forms read first: (L2) finite Schur complement $S_{T,k}\succeq0$,
(N) signed twisted Chebyshev sums at Nyquist points $\pi k/2T$, (S) near-coincidence Toeplitz-in-$\log(m/k)$
matrix. Index read first: `05-meta-and-planning/ROUTES-TRIED-INDEX/03_PHASES_000-099.md` (258 lines, sections
A–G covering phases 0–99).

## Zeroth-order finding, true of the whole range 0–99

Every phase in this range (on disk: 0, 3, 4, 5, 32–99; 6–31 only as index summaries) predates Paper 46's
reduction entirely. Their basic object is never the explicit prime-only kernel $s_T(\tau)$ on a finite window;
it is always one of: a Kreĭn-space/Hilbert–Pólya realization $(\mathcal K,Q)$ carrying the *zero set* $\Gamma$
of $\zeta$ as data (phases 4, 5, 34, 53, 60, 61, 64, 65...), a CCM/prolate spectral triple indexed by zeros
$\gamma_n$ (phases 0, 5, 32, 59, 60, 71), a Weil–Toeplitz algebra of windows whose symbol is defined by
"visibility of off-line quadruples $(\delta_j,\gamma_j)$" (phase 45, Doc 134), or a Fredholm/adjugate pencil
built from a *conjectural* off-line zero (phases 72–99, the long E7x/P7x–P99 Feshbach/Cauchy-projection/
adjugate chain). None of these objects is the finite vector $(\Lambda(n))_{n<e^{2T}}$ that Paper 46 shows
carries the whole problem (Prop. "finite", `main.tex` line ~140). Reading any of their stated theorems into a
statement about $\lambda_A(T)$ requires passing through exactly the equivalence the project rules bar (zero-set
object $\leftrightarrow$ prime-only quadratic form), so nothing here converts into reduced forms (L2)/(N)/(S)
or into the primitive subspace $\mathcal P_T$ without that forbidden step. This is already the main
conclusion; the phase-by-phase pass below looks for exceptions (identities/tools that are, in fact, prime-only
or zero-free) and finds none that survive close reading.

## Phases 0–5 (foundations)

- **Phase 0** (`phase-0-foundations`): Q as a localized finite Gram of the Weil–Guinand form (P0-1, PARTIAL,
  "not a new object"); Connes semilocal compression (P0-2); de Branges structure function (P0-3, DEAD, folds
  into ES-16). All three build the Gram matrix from zero data or from a Connes trace, not from $v_n=2\Lambda(n)/\sqrt n$
  directly against $|\hat F|^2$. No window-indexed object, no Nyquist mesh. No hit.
- **Phase 3** (`phase-3-uniform-inequality`): stability geometry of a *localized* Weil form, aimed at
  "detecting a fixed zero" (P3-1, PARTIAL). Entirely zero-detection framed; the localization is in the zero
  variable, not in $T$. No hit.
- **Phase 4** (`phase-4-krein-space-realization`): the deepest technical phase here. B2-THEOREM / PAPER-A.md build a faithful
  semibounded Kreĭn realization $\mathfrak t=E^*JE$ and attack coercivity §2½ as **pure sampling theory**
  (`proofs/Day22-coercivity.md`): "does $\mathfrak t_+=\sum_\gamma|F(\gamma)|^2\ge c\rho\|F\|^2$ follow from
  $D^-=\infty$, or is a gap condition needed?" They use "Nyquist" in the Beurling–Landau sampling sense (a gap
  in the *zero sequence* $\Gamma$ larger than $\pi/d$ kills the lower frame bound), which is a different
  Nyquist mesh from Paper 46's $\pi k/2T$ (samples of $\hat F$ indexed by $k$, fixed by the window $T$, not by
  zero spacing). The depth-split idea ("coercivity only needed near off-line zeros") is a genuine technical
  tool but is stated and provable only relative to a hypothetical off-line zero — i.e. it is RH-shaped by
  construction, not translatable to the prime-only form without the barred equivalence. P8-ThmC (phase-4)
  proves depths enter $\|K\|$ "only through $\mathfrak t$ itself" — a NO-GO against using zero-depths as an
  external lever, already correctly labelled. No hit, no mislabel found on inspection.
- **Phase 5** (`phase-5-structural`): per-prime anatomy $R_p\approx a_pW(\log p)$ (P5-2); de Branges comparison
  B3.2 (folds into ES-16, CIRCULAR/FALSIFIED by Conrey–Li). The per-prime anatomy is closer in spirit to
  Paper 46's comb $v_n\cos(\tau\log n)$ (it is literally indexed by primes), but the file frames positivity
  structurally in $\{R_p\}$ bounded by a Bessel inequality $\le 1$ that is stated as the wall, not removed by
  anything in Paper 46 (Paper 46's own barriers W-lin/W-det are a modern, sharper version of the same
  obstruction). Re-read with today's finite reduction in mind: $R_p$ is a per-prime decomposition of the
  *continuous* Weil form (all $\tau$, implicitly $T=\infty$), not a per-window object, so it does not shortcut
  (L2)/(N)/(S). No hit.

## Phases 6–31 (index summaries only; folders absent except as noted)

Covered only via `03-research/README.md` / `NO-GO-LIST.md` / `MAP_1` (index rows P6-31, NG-E1..E7, N6, N7,
P8-ThmC). Named items: OS reflection positivity per place (FALSIFIED numerically, phase-6), sine-kernel
Carleson (phase-7), heat-flow monotonicity (phase-8, NO-GO on fixing the terminal parameter), unconditional
universality (phase-9), Hodge envelope (phase-10), interlacing/total-positivity giving the **wrong-sign**
capstone (phase-11, correctly closed, PF route dead for this problem family), $\omega$-class multiplicative
chaos (phase-12, PARTIAL, no sign), off-diagonal anchor (phase-14), arithmetic Hodge index (phase-15), SURF
witness variety (phase-16/17), negative-directions portraits (phase-18/21), Pontryagin finite defect
(phase-22), two-scale defect (phase-23), $b_j$ lower bounds (phase-24/25, NO-GO per 15 classical mechanisms),
Kreĭn–Connes bridge (phase-26), adelic rigidity (phase-27, Hasse–Minkowski factorization fails for $Q_{\rm
zero}$), four fronts (phase-28, all reduce to $\xi\in$ Laguerre–Pólya class), spectral triples (phase-29),
Langlands bridge (phase-30), Selberg moments (phase-31). All of these are explicitly zero-set or $\xi$-function
objects (the index's own one-line descriptions make this unambiguous: "off-line depths $b_\rho$", "zero-side
attack", "negative directions", "Pontryagin index"). None is a finite prime-indexed window form. No hit; no
basis to re-examine labels without the source files (not on disk for 6–31), and the index descriptions give
no sign of a usable prime-only identity being discarded.

## Phases 32–59 (CCM / Kreĭn / category chain)

Scanned via index (Section D, ~60 rows) plus spot files (`phase-45-fredholm/134-weil-toeplitz-algebra...md`,
`phase-39`, `phase-46`, `phase-47`, `phase-60` preambles — these last three bleed into phase 60's discriminant
program). Recurring pattern: CCM trace criteria that are CIRCULAR restatements of the target on the zero side
(P32-3 CTP, P33-2, P33-9, P33-10, P33-11, P33-12 — six independent CIRCULAR verdicts, all correctly labelled:
each is checked to literally require the target or an equivalent completeness/extremality statement). The
**Weil–Toeplitz algebra** of Doc 134 (phase-45) is the one object genuinely built "window by window" with a
symbol $\sigma(Q)$ and an essential-spectrum/corona structure — structurally the closest precursor to Paper
47's per-$T$ Toeplitz-in-$\log(m/k)$ matrix (problem (S)). But Doc 134's windows $Q_n$ are indexed by *zero
visibility thresholds* $\theta_j\asymp\min(1,\delta_j a(\gamma_j))^\kappa$ for hypothetical off-line quadruples
$(\delta_j,\gamma_j)$ — the symbol itself is defined by appeal to where zeros would sit, not by $\Lambda(n)$.
Theorem 1.3 of that document (strict vs weak essential positivity, "a certificate without a gap certifies
nothing") is a real dichotomy theorem, but it is a dichotomy about an operator family parametrized by a
conjectural zero configuration; it does not supply, and the document does not claim to supply, a bound on
$s_T$. No hit. P36-4's "two-variable Weil form" / INV_J_001 wall = pair correlation (Hardy–Littlewood, parity
obstruction) is the same parity-obstruction family Paper 46 encounters independently in problem (N) (the
requirement "exponent $\frac12$ cancellation, with sign" is exactly what a parity-type sieve bound
cannot deliver) — already closed there under a different name; no new angle found; not proposed as a route
(ES-4/NG-A4/P36-4 already cover "parity problem" as a named wall in the index, so this is not new).

## Phase 60 (discriminant / CCM ground state) — largest single folder

~80 files (RH-PROOF-PAPER.md/.tex, RH-demostracion, PRUEBA-COMPLETA, tribunal-*.md verdicts, E1–E9 experiments,
N5-analytic-loewner, ESLABON2 chain). Index already records five outcomes P60-1..P60-5: H1 simplicity +
Perron–Frobenius (PARTIAL, proved but "gives simplicity, not sign"), E1 secular rescue (FALSIFIED, total
positivity of $\xi$ refuted), Eslabón 2 frame convergence (PARTIAL, a $\lambda^2\log\lambda$ Jensen prediction
refuted), III/IV.1 relative stability / Airy–Bessel (FALSIFIED, "$n^2\Leftrightarrow(T^\star)$" i.e. the
candidate limit operator is shown equivalent to the target), and P60-5 "RH-PROOF-PAPER / boundary triples for
$W_\lambda$" marked **NO-GO (PROOF_L_SHARP_OO_001)** with no "why it failed" entry (the index table literally
has `—` in that cell). I opened `phase-60-discriminant/RH-PROOF-PAPER.md` and `tribunal-VEREDICTO.md` to check
this cell. The tribunal verdict files (Connes/Consani/Moscovici personas) record that the claimed boundary-
triple closure was rejected because self-adjointness of the limit operator was never established — consistent
with the Section E "P65 | ... | DEAD at D8.5" and "self-adjointness of the limit operator is the wall" language
used later for phase 65. This is the same wall restated, not a new one; the missing index cell is an index
*documentation* gap, not a mislabel of the mathematics (the verdict itself, NO-GO, is corroborated by the
source). I flag it below as a minor index-hygiene item rather than a mislabel. N5 (Loewner + prolate + relative
stability, PARTIAL): the surviving Loewner-monotonicity structure is a genuine tool but is explicitly tied to
the rate at which $\varepsilon_{\rm loc}(\zeta)\to0$, i.e. to zero spacing near the critical line — not
translatable to a window-$T$ statement. No hit.

## Phases 61–99 (long Fredholm/Feshbach/adjugate chain)

Index Section F plus spot files in phase-73 (`E73_198_digamma_wr_tail_probe.py`) and phase-76/77. This is a
~40-phase chain (P61 through P99) built entirely on a single conjectural off-line eigenline of a finite-
dimensional truncation $H_{\rm actual}(\lambda,n)$ (CCM operator), tracking its ground eigenvector $\xi$,
rank-one/rank-two corrections, Feshbach splits HF/LF, and adjugate/cofactor identities on a bordered matrix
pencil. The digamma function *does* appear here (`E73_198_digamma_wr_tail_probe.py`, `E73_199_digamma_ff...`)
— this is a real terminological collision with $m(\tau)=\Re\psi(1/4+i\tau/2)-\log\pi$ — but the usage is the
asymptotic tail of $\psi$ in a different context (bounding a "WR tail" / "FF certificate" for the CCM
operator's archimedean background term `build(lam, n_modes, include_arith=True)` with eigenvector `xi`
obtained from `eigh`), not the symbol $m(\tau)$ of the window form, and the object `xi` is the ground state of
a finite numerical truncation indexed by a putative zero $\gamma$ (`GAMMAS` imported from
`E72_396_cauchy_projection_probe`), confirming the zero-set dependence. Every phase in this chain (P61–P99,
~37 rows in the index) is labelled PARTIAL/NO-GO/DEAD/CIRCULAR with a one-line obstruction that is internal to
that chain's own bordered-pencil formalism (e.g. P74 "irreducible divisibility, cancellation arithmetic-
specific", P87 "false implication", P96 "sum decision = target"); none states or uses a prime-only identity
that would bear on $s_T$, $\mathcal P_T$, or a Schur complement on Tate exponentials. No hit. No candidate
mislabel found in this chain on the spot checks performed (E73/E76/E77 files read were consistent with their
index verdicts).

## Corpus-level tools worth naming (not hits, but closest adjacent objects)

1. Phase-4 Day21/Day22 coercivity and the "depth split" (coercivity needed only where off-line zeros sit) is
   the clearest precursor in spirit to Paper 46's Schur-complement reduction (L2) — both say "the problem
   localizes to a finite/near piece and is harmless elsewhere" — but phase 4's localization is in the zero
   variable $\gamma$, Paper 46's is in the contact variable $n<e^{2T}$; the translation between them is exactly
   the barred equivalence, so this is noted only as a structural analogy, not a route.
2. Phase-45 Doc 134's corona/essential-spectrum symbol calculus is the closest precursor to treating a family
   of windows as a single operator-valued object with a computable "symbol"; again built from zero visibility,
   not from $\Lambda(n)$.
3. The parity obstruction (P36-4, NG-A4, ES-4 family) recurs in both the old corpus and Paper 46's problem (N)
   ("mean-square/large-sieve bounds do not suffice... a parity-type cancellation is needed with sign"); this is
   consistency between the old and new material, not a new finding, and is not proposed as a route since it is
   already closed under both names in the index.

## Hits

(Honest: empty.) No phase in 0–99 supplies a result that, read against today's finite reduction, proves or
nearly proves $\lambda_A(T)\ge0$ beyond $\tfrac12\log5$, and no dropped tool was found whose stated obstacle is
actually removed by Paper 46's finite reduction, Nyquist sampling identity, or exact Schur coupling. The
entire range is pre-reduction and zero-set-indexed; its results do not have prime-only content that survives
translation.

## Mislabels

None found with confidence. One index-documentation gap, not a mathematical mislabel: the Section E row
`P60-5 | ... | NO-GO (PROOF_L_SHARP_OO_001) | —` has an empty "why it failed" cell in
`05-meta-and-planning/ROUTES-TRIED-INDEX/03_PHASES_000-099.md` line 202. Source files
(`03-research/phase-60-discriminant/RH-PROOF-PAPER.md`, `tribunal-VEREDICTO.md`) corroborate the NO-GO verdict
(self-adjointness of the limit operator not established), so the label itself is correct; only the index's
"why" column is incomplete. Suggest (for whoever next edits the index, not done here — repo left unmodified)
filling that cell with "self-adjointness of the limit operator not established (same wall as phase 65, D8.5)".

No route proposed or re-attempted in this report; no claim that anything here is new relative to the index.
