# Phase 183 — Connes-Consani semilocal sufficiency

The phase formalizes and tests Connes-Consani's Conjecture 4.1 (*The Scaling
Hamiltonian*, arXiv:1910.14368): the claim that a semilocal framework built
from the place set S(q) = {∞} ∪ {p < q} should suffice to prove Weil
positivity for test functions supported on (q^{-1/2}, q^{1/2}). The published
conjecture states only that the framework "suffices," without naming an
operator or a weaker auxiliary inequality; the phase names one (a co-Poisson
compression operator and a "Sonin" decomposition) and tries, over three
rounds, to prove or refute its sufficiency.

## Results
- Theorem 1 (exact rough-integer gap): if m is coprime to every prime below
  q and m > 1, then m ≥ q, i.e. log m ≥ 2T — the arithmetic fact that
  explains Connes-Consani's choice of place set. **PROVED**.
- Theorem 2 (window triangularity of the compressed co-Poisson operator),
  and the general statement that formalized sufficiency for every q is
  exactly equivalent to row D, while a pre-spectral factorization of the
  compression remains unresolved. **PROVED** (gap and triangularity);
  **OPEN** (prespectral factorization).
- Sonin-route synthesis (round 1-2, R183_028): an exact identity
  E_S = Son + R_{S,T} is proved for every admissible S; the entire Sonin
  mechanism is a **NO-GO** (infinite negative index) once any positive
  fraction of Son is sacrificed except η = 0; a relative-bound-0 theorem
  localizes exactly how much slack exists; the symmetrized kernel ε is
  proved **not positive definite**, correcting an earlier reading; and
  Connes-Consani's claimed single negative direction is shown to live in a
  different (ξ-type) metric than L². A two-edge model gives the exact prime
  term with factor log p (**PROVED**, model). The archimedean-only
  mechanism is found (non-certified numerically) to add directions only
  beyond T ≈ 0.60/0.80, matching an independently known threshold.
- Round 3 synthesis (R183_033): a scaling-law theorem (029 Thm A) upgrades
  the semilocal identity to hold unconditionally, decomposing
  Son_S - Son_∞ into an exact prime term plus controlled remainders
  (**PROVED**); a gap theorem shows no negative direction exists for
  S = S(T) up to T = ½log5, citing Paper 46 (**PROVED**); numerically
  (not certified) the gap appears to persist up to T ≈ 0.80-0.90 with
  super-exponential decay; a "gap requirement" theorem shows that any
  bounded-inertia positive-multiplier decomposition valid for all T must
  have its density concentrate on the zeros (**PROVED**, under RH as
  hypothesis for one direction only). Several intermediate conjectures
  (global (E'), modulation invariance) are downgraded to **HEURISTIC** or
  shown **FALSE**.
- Overall editorial verdict: the Connes-Consani mechanism is a genuine,
  certifiable mechanism only in a bounded archimedean window (T ≲ 0.80);
  beyond that every tested version (entire Sonin, uniform-fraction Sonin,
  frequency multiplier, semilocal Sonin) is either **NO-GO** or reduces to
  an exact restatement of row D with an extra structural condition that no
  known construction satisfies (the positive part would have to "know" the
  zeros without using them). Row D is **OPEN**; no sign is established for
  all T.

## Documents
- `R183_001_FORMALIZATION_AND_ROUGH_GAP.md` — formalizes the conjecture,
  proves the rough-integer gap and window triangularity (Theorems 1-2).
- `R183_002` through `R183_016` — successive constructions and audits:
  restricted Hilbert-Schmidt contraction, semilocal return operator,
  Poisson-Möbius-Wiener-Hopf analysis, first-crossing interference, GCD-fiber
  Laurent bridge, positive Laurent family and kernel tests, a white-light
  residue NO-GO, Laurent tangent normalization, superposed central tangent
  defect, rough-tail observability, type audits, and trace-anomaly/trace-
  class/operator-order analyses leading into the Sonin route.
- `R183_017` through `R183_028` (`R183_028_SYNTHESIS_SONIN_ROUTE.md`) —
  the Sonin-decomposition route: construction, NO-GO, semilocal Sonin space,
  partial multiplier, relative bound, literature inventory, Lemma L1, an
  archimedean-band Szegő falsifier, reviews, and the round 1-2 synthesis.
- `R183_029` through `R183_033` (`R183_033_SYNTHESIS_ROUND3.md`) — round 3:
  the estimate for E', an inertia/gap-requirement theorem for the first
  semilocal window, reviews, and the final synthesis.

## Relation to other phases
Cites and is checked against Paper 46's thm:log5A and the TK ceiling
identified in phase 155; the super-exponential gap behavior found here is
read as the Sonin-side manifestation of that same ceiling. No sign result
is produced beyond the certified window; the route is left open with a
precisely stated necessary condition for any further attempt.
