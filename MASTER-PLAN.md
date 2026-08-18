# Riemann Program — Master Plan

**Author:** David Alejandro Trejo Pizzo · `dtrejopizzo@gmail.com`
**Updated:** 2026-08-18
**Scope:** What the repository contains, how it is organized, the candid status, and the only
routes that remain open.

> **Governing principle: absolute candor.** *A false victory would be worse than a failure.*
> No proof of RH has been found. This plan records what is done, what is proved, and what is left.

---

## PART 0 — What the repository contains

The work is two empirical layers feeding one theoretical program:

- **Research Programs 1–9** ([`01-context/`](01-context/)) — nine computational research
  programs (627 tasks): resonance detection, the ω-class program, inverse-spectral
  positivity, and the localized Weil detector. The descriptive/empirical base.
- **Program 10** ([`03-research/`](03-research/)) — the research phases (currently through
  phase 76).
- **The papers** ([`04-papers/`](04-papers/)) — 36 publishable papers
  ([`04-papers/README.md`](04-papers/README.md)).
- **Foundations** ([`02-foundations/`](02-foundations/)) — the validated engine, zero data, and
  precision validation that everything imports.
- **Meta/planning** ([`05-meta-and-planning/`](05-meta-and-planning/)).

The full narrative is [`COMPLETE-PROGRAM-SUMMARY.md`](COMPLETE-PROGRAM-SUMMARY.md); the one-picture
map is [`00-MAP.md`](00-MAP.md); the registry of failures is [`NO-GO-LIST.md`](NO-GO-LIST.md).

---

## PART 1 — The scientific bottom line

**Arc A (ω-class).** Descriptively rich (the ω-decomposition, phase coordination, the Liouville
parity anomaly, the GEV hierarchy) but it did **not beat convexity** (α_B ≈ 0.42 vs Bourgain's
0.31), and the proof chain was circular (target stronger than Lindelöf) and blocked by the parity
problem. The headline "phase transition" of the large-value work was refuted by canonical
re-verification.

**Arc B / the localized Weil program.** The targeted Weil quadratic form is the first observable
with genuine detection power for off-line zeros (P7: forced negativity). The program then showed,
across the Kreĭn realization (P8), the anatomy (P9/P10), and the finite-defect analysis
(P16/P17), that the negative index κ = #(off-line zeros) is the whole content: RH ⟺ κ = 0.

**Where RH lives (the deepest result).** κ is *global*, *one-sided* (an upper bound), and
*orthogonal to all symmetry data* (real structure, resolvent, spectrum). Every historical
approach has abundant symmetry data but cannot reach the scarce sign — which is why they all
stall at the same wall. This is the master quantifier: RH asks to cross from "on average" to
"without exception," and no current argument form does so.

**The CCM and structural threads (Phases 29–61).** The Connes–Consani–Moscovici trace, the
Hodge/Spec-ℤ construction attempts (incl. Deninger leafwise-Hodge), the Weil–Toeplitz algebra,
and the wall-as-object attack all map the wall precisely and prove it is not crossed by existing
tools. The missing object is a cohomology over Spec ℤ with the zeros as Frobenius eigenvalues —
the Connes–Consani arithmetic site — which is RH-equivalent by construction and unbuilt.

**Phases 62–76: from wall-mapping to a single named input.** Phases 62–63 sharpened the master
wall to its most precise statement yet (NG-62/NG-63: no J-linear, gapped-Frobenius realization on
the ζ window). Phases 64–69 then pivoted from Weil positivity to the one live candidate not on
that wall — CAND-1, the Connes–Consani–Moscovici zeta spectral triples, whose operators are
self-adjoint by construction, so the open question becomes operator *convergence*, not
positivity (Phase 64 reclassified the route; Phases 65–69 pursued signature-continuity,
rank-one escape, a quantum q-index, and a GLT/Toeplitz symbol, closing each sub-attempt with a
precise no-go while sharpening the terminal object Ω7). Phase 70 connected Ω7 to the
de Bruijn–Newman/Lee–Yang picture (RH ⟺ Λ=0). Phases 71–76 then built a concrete finite
convergence architecture (CAND-1/CCM stable-divisor convergence, Feshbach leakage calculus,
Cauchy projection, Hilbert eigenline cancellation, arithmetic numerator divisibility, and the
normalized-adjugate arithmetic lock) that, distilled together with the closed-wall geography of
Phases 0–63, shaped the fifteen-step **arithmetic Pick positivity (ARP-P)** chain of paper **36**
(`04-papers/36-obstruction-ledger/`). Fourteen of the fifteen ARP-P steps are proved; the
remaining one reduces, by a chain of proved equivalences, to the classical **Li–Keiper
criterion** $\lambda_n\ge0$ for all $n$ (equivalently the terminal-defect positivity $\Omega_7$).
The program therefore now has a complete, candid reduction of RH to one classical, named,
RH-equivalent input — sharper than "the missing object is a cohomology over Spec ℤ," but still
not a proof: $\Omega_7$ carries the full difficulty of RH.

---

## PART 1B — Phases 77–119: a second independent reduction

Phases 77–106 pushed the ARP-P/$\Omega_7$ architecture to its limit: thirty phases of exact
finite algebra closing every accessible sub-gate, with no crossing (see `00-MAP.md` Part 13).
Phase 107 then pivoted to a structurally different construction — imitating Weil's own 1948 proof
for curves over finite fields directly over $\mathrm{Spec}\,\mathbb Z$ (rows a–d), rather
than continuing to push ARP-P forward.

That programme (`00-MAP.md` Part 14) built rows (a)–(c) as paper **42**
(`04-papers/42-arithmetic-lefschetz-programme/`), and proved row (d) equivalent to RH **twice**,
independently:

- **Phase 113, algebraically.** Inside the Schwartz-data class $\mathcal D$, requirement d3
  (Riemann–Roch's quadratic growth) is proved **impossible** — three independent obstructions
  (O1: scaling-stable effective cone; O2: infinite mutual intersection, with the exponent $1/2$
  encoding the critical line directly; O3: no spectral gap). The remaining input, effectivity
  $(E^\circ)$, is then proved equivalent to RH in both directions.
- **Phase 118, analytically.** Derived and verified against real zeros of $\zeta$, to relative
  precision $5\times10^{-11}$–$2\times10^{-9}$: $\langle A_TF,F\rangle=\sum_\rho
  h(\gamma_\rho)$. Row (d) **is** localized Weil positivity — the same wall, reached by the
  explicit formula instead of Riemann–Roch.

Along the way, phase 117 killed the one conjecture paper 42 had used to complete row (d)
conditionally (the Logarithmic Schur Angle Conjecture): its source-model route has best constant
$c_N<1$ at every threshold, decaying, Galerkin-bounded from above (one-sided-robust); and the
conjecture itself is falsified against the paper's own audit table.

**This is the second full reduction the programme now has**, alongside the Li–Keiper/ARP-P
reduction of Part 1. Both are candid, neither is a proof, and both cross-check each other in the
sense that two unrelated constructions land on statements each provably as hard as RH.

**What phase 119 opened, and what remains genuinely unbuilt.** The corpus's own audit
(`03-research/THE_BACKWARD_MAP.md`, `03-research/AUDIT_CONSOLIDATED.md`) distinguishes what is
*proved impossible* from what is merely *unbuilt*. Three objects are unbuilt but not excluded: a
construction with the required quadratic growth (a4); a space carrying an integral lattice
structure compatible with the row-(c) pairing (a-new/b4); and whether a quadratic Riemann–Roch can
exist over $\mathrm{Spec}\,\mathbb Z$ **at all**, independent of anything built here (R16).
Phase 119 itself pivots away from positivity entirely, asking what a finite compression of the
Weil form certifies *unconditionally* (its inertia via Sylvester's law, its moments from the prime
side) — gated on a Davenport–Heilbronn separation test that has not yet been run. See
[`OPTIONS.md`](OPTIONS.md) for the complete, file-cited options list, including a family of open
targets the audit found that are **not** equivalent to RH and were never closed:
$m<\infty$ (any unconditional bound on the off-line quadruple count — verdict "unreachable with
cataloged techniques," not proved impossible), $m<\infty\Rightarrow m=0$ (via LP-112, verdict
"without precedent" after an exhaustive literature search), and a self-labelled
"RH-neutral, doable now" boundary-triple classification that has simply never been attempted.

---

## PART 2 — Repository organization (done)

The repository has been ordered and put into English:

```
riemann/
├── README.md   EXPLANATION.md
├── 00-README.md   00-MAP.md   MASTER-PLAN.md   COMPLETE-PROGRAM-SUMMARY.md   NO-GO-LIST.md
├── 00-references/   01-context/ (RP 1–9)   02-foundations/
├── 03-research/ (Program 10: phases 0–76)   04-papers/ (36 publishable papers)
├── 05-meta-and-planning/
```

Front-door and per-phase summary documents are English; folder names are English; some granular
phase working notes remain in their original Spanish as the raw research record.

---

## PART 3 — What is proved (unconditional ledger)

A standalone, RH-independent base (full list in `COMPLETE-PROGRAM-SUMMARY.md §9`):

- Forced negativity (P7); unconditional truncation control (P9, exponential stability of the
  localized form under small-prime data).
- The DH null result with onset bound N* ≳ 10¹⁴ (P3).
- The bridge theorem κ(Q) = neg.ind(H_C) (P8/Phase 26).
- The balance law İ = −2κ(t) − D(t) under the DBN flow, RH ⟺ I(0⁺)=0; and E(T)=Σ(β−½)² ≪ T/log T
  — the first unconditional second-order result (Phase 54).
- Local purity decidable: single-prime H ⟺ |α|=√p (Phase 44) — the discriminant is purity, not
  multiplicativity.
- The two-prime (and n-prime) Weil-positivity theorem (Phase 45).
- ~18 further unconditional theorems across Phases 44–59 (logistic index law, semilocal
  positivity with archimedean term, the tensor index identity, the pinned-moment identity, the
  ceiling theorem, RvM-t).

---

## PART 4 — The only route still open

Post-Phase-76, the state above (the Hilbert–Pólya/Connes–Consani object, the adelic Maslov
index) has been superseded by a single, precisely named open input, reached independently via
the ARP-P architecture of paper **36** (`04-papers/36-obstruction-ledger/`):

1. **The Li–Keiper criterion, $\Omega_7$.** ARP-P (the fifteen-step arithmetic Pick/Nevanlinna
   chain) is proved equivalent to RH; fourteen of its fifteen steps are closed. The sole
   remaining step reduces to the terminal-defect positivity $\delta_N\ge0$ for all $N$,
   equivalently $\lambda_n\ge0$ for all $n$ — the classical Li–Keiper criterion. This is not a
   new discovery: it is where an independently constructed architecture, after its own internal
   difficulty audit, terminates. It is candidly RH-hard: $\Omega_7\iff$ RH, so proving it is
   exactly as hard as RH, and every attempted closure of $\Omega_7$ so far (Phases 64–76) has
   landed back on one of the structural walls (MW-1 through MW-6) catalogued in
   [`NO-GO-LIST.md`](NO-GO-LIST.md).
2. **Calibrated sub-RH targets** — reducing the log exponent in the unconditional finite bottom;
   the per-window arithmetic evaluation beating Montgomery–Vaughan (GAP-141.G1); the standalone
   B2 conjecture (new RH-independent mathematics). These remain genuinely sub-RH and are where
   new unconditional mathematics could still come from without confronting $\Omega_7$ head-on.

Route 1 is, candidly, exactly as hard as RH — but it is now a single, sharply named target
instead of a diffuse map of walls, and the whole apparatus (Steps 1–15, the H0–H8 hierarchy
for the open step, and the $\Omega_1$–$\Omega_7$ difficulty-localization chain) is available for
outside attack, with the falsification harness in the paper's companion code.

**Route 3 (added post-Phase-119).** Row (d) of the arithmetic-Lefschetz reduction (Part 1B) is
the same kind of target as Route 1 — proved equivalent to RH, twice, independently — so it carries
the same candid warning. What is different in kind, and therefore what [`OPTIONS.md`](OPTIONS.md)
should be read for, are the several sub-targets the phase-119 audit found that were **never shown
equivalent to RH**: a quadratic-growth construction (a4), an integral-lattice space (a-new/b4),
the existence question for quadratic Riemann–Roch over $\mathrm{Spec}\,\mathbb Z$ (R16), and
independently, from the wider audit, Diana L8, "Lemma 108," Conjecture $\mathbf C_B$, LP-112,
GAP-157.A, and the untried boundary-triple classification for the CCM operator family. These are
where new unconditional mathematics is most likely to still be reachable without confronting RH's
full difficulty head-on.

---

## PART 5 — Guardrails (learned the hard way)

1. **No circular targets.** Never aim at a bound stronger than Lindelöf as a "step."
2. **One validated engine** (`02-foundations/`), cross-checked against mpmath.
3. **Track N-dependence** for every numerical claim; a single N is not a result.
4. **DH is the control**, run in parallel; a real ζ-signature must *fail* on L_DH.
5. **Conditional ≠ unconditional.**
6. **Report negatives** and **audit adversarially** — the program's self-corrections (W_λ ≥ 0,
   the logistic ¬RH branch, the phase-60 duality withdrawal) were caught only by audits with a
   control that fails when it should. Pre-register, keep code runnable.
