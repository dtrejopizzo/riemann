# Phase 17 — SURF 2.0: isolating what geometry would need to produce (off-axis functionals, real structure)

Refines the SURF witness-variety program (phase 16) in light of the de Branges obstruction chain
(P22–P28). Instead of asking generally which Hilbert/Kreĭn space could carry the Weil form, it asks
the sharper question the chain isolated: what geometry would produce, independently of the zeros
(F-independently), (i) the off-axis evaluation functionals and their on-line/off-line signature,
and (ii) a resolvent obeying the de Branges difference-quotient identity. It builds a design
specification (SURF 2.0), then runs the SURF-A (geometric scaffolding) and SURF-B (operator)
triages against it.

## Results

- SURF-A target template: a finite Gram-matrix experiment fixes the required signature pattern (on-line blocks (1,0), off-line blocks (1,1)) that any candidate geometry must reproduce — established as the acceptance test, not itself a theorem about ζ.
- SURF-A, Part 1: the real-structure scaffolding (X, j) built from an involution with fixed locus the critical line reproduces the required signature/index pattern with **no reference to the actual zero ordinates** — **PROVED** F-independent and trivial to realize.
- SURF-A, Part 2: this same scaffolding is **γ-blind** — real ζ ordinates, random ordinates, and an arithmetic progression all give the identical signature once the on-line/off-line pattern is fixed — **PROVED**; the geometric scaffolding carries no arithmetic information, only the spectrum (operator) does.
- Consequence: SURF-A collapses into SURF-B — all nontrivial content is in the operator T, not the geometric scaffolding — **established conclusion** of the phase's first half.
- SURF-B: the real-structure constraint (T2) is tested against candidate operators and found to be a symmetry, not a positivity — its weak form (j permutes the spectrum as a set) holds unconditionally regardless of RH truth, and its strong form (j fixes each eigenvalue) is equivalent to RH itself — **PROVED**; the real structure supplies no new handle on the sign.
- Survey of literature operators (Connes scaling flow, Connes–Consani scaling site, canonical/de Branges systems) against criteria (T1)–(T4): each either reduces to the known Weil positivity (CAP) or requires the missing global Hodge index (SURF/Route 1) — **no crossing found**; consistent with, and sharpening, the standing CAP/SURF map.
- Overall verdict (pre-registered and realized): the symmetry-vs-positivity dichotomy — real-structure/canonical-system realizations cannot by themselves decide RH — is recommended as the phase's durable output (P29), in the "why RH resists" lineage.

## Documents

- `00-SURF-2.0-design.md` — internal design/roadmap refining the phase-16 SURF spec in light of P22–P28; defines SURF-A and SURF-B acceptance tests and pre-registered failure conditions.
- `01-SURF-A-triage.md` — the target Gram-signature template and the F-independence exam for geometric candidates.
- `02-involution.md` — the real-locus involution j(s) = 1 − s̄ and the Klein four-group of symmetries, set up without assuming an Arakelov metric.
- `03-route2-testbed.md` — the finite testbed showing the scaffolding is F-independent but γ-blind; the collapse of SURF-A into SURF-B.
- `04-SURF-B-resolvent.md` — the (T2) sign-handle test and the survey of candidate operators against (T1)–(T4).
- `experiments/` — supporting numerical scripts for each step's Gram-signature and involution computations.

## Relation to other phases

Directly refines phase 16's SURF witness-variety construction in light of results labeled P22–P28; its closing recommendation (a symmetry-vs-positivity structural theorem) extends the "why RH resists" results of phase 15 (P21) and phase 16.
