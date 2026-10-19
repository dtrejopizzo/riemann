# Phase 13 — The ω-class structure of ζ's multiplicative chaos

Rather than continuing to attack the open frontier found at the end of phase 12 head-on, this phase pursues a
structural question flagged as valuable independently of any route toward the main target: why do the ω-class
(number-of-distinct-prime-factors) exponents from an earlier phase's machinery reproduce the k² moment
exponents of ζ's multiplicative chaos? The results here are explicitly presented as RH-independent mathematics.

## Results
- Rigorous identity: for squarefree n, d_k(n)² = (k²)^{ω(n)}, so the k² moment exponent is literally the square of the per-prime ω-weight; via Selberg–Delange asymptotics for Σ z^{ω(n)}/n, this explains why the ω-class fingerprint, the moment exponents, and the chaos exponents are one and the same object viewed three ways. PROVED (the algebraic identity and its asymptotic consequence), with numerical confirmation of the Selberg–Delange exponent tracking z (subject to the usual slow finite-N drift).
- Dictionary linking the chaos parameter β to an ω-weight z=β², identifying the subcritical (β<1), freezing (β_c=1), and supercritical (β>1) regimes with typical, neutral, and large-deviation behavior of ω(n) respectively (Erdős–Kac / Sathe–Selberg). PROVED (the correspondence) — a new structural identification connecting multiplicative-chaos extreme-value theory to classical large-deviation theory of ω(n).
- Assessment of contribution to open frontiers: this result clarifies the diagonal (leading-order) term of the supercritical moment problem but does not touch its off-diagonal (CFKRS constant) part, which remains open; it does not touch the separate, generational "new discreteness" question. ARGUED (scope statement), explicitly not a proof of RH and not claimed as one.
- M13.2: the FHK leading term max log|ζ| ~ log log T is recovered as 2V where V is the Selberg variance, realized exactly at the freezing point β_c=1 ⟺ z_c=1, with numerical confirmation of the variance scaling and the max/2V ratio converging toward 1 as the prime range grows. ARGUED/NUMERICAL (structural explanation, RH-independent).
- M13.3: both the FHK leading and subleading terms (log log T − ¾ log log log T) are recovered heuristically by modeling the ω-class prime hierarchy as a branching random walk with log log T levels and the universal Bramson correction, with equal per-level variance verified numerically across prime levels. ARGUED (heuristic structural derivation via the branching-random-walk analogy, not a new proof of the rigorous FHK result, which is cited to its proper source).

## Documents
- `RESULT-omega-class-structure-of-chaos.md` — the full phase writeup: rigorous core, dictionary, candid framing, and milestones M13.1–M13.3.
- `experiments/M13_1_omega_k2_structure.py` — verification of the d_k(n)²=(k²)^ω(n) identity and the Selberg–Delange exponent fit.
- `experiments/M13_2_fhk_from_freezing.py` — the Selberg-variance / FHK leading-term computation.
- `experiments/M13_3_brw_subleading.py` — the branching-random-walk level-variance check and subleading-term derivation.

## Relation to other phases
Explains, independently of the RH-directed chain, why the ω-class machinery referenced from an earlier phase's Arc (P2–P5) reproduces the moment exponents studied in phase 12's multiplicative-chaos route; proposes a candidate standalone paper on this RH-independent connection; leaves the off-diagonal moment problem (phase 12's landing point) and any new-discreteness idea as separate, open items.
