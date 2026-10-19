# Phase 12 — Log-correlated fields, the meta-obstruction, and the moment problem

After earlier phases confirmed a "wrong-sign capstone" (every unconditional handle found so far is a
positivity, giving lower bounds, while the target needs an upper constraint), this phase tries a mechanism
whose native output is an unconditional upper bound without resting on a positivity: the theory of
log-correlated fields and multiplicative chaos, connected to ζ via S(T)=arg ζ(½+it) being a log-correlated
field. It follows this route through several milestones, finds it genuinely escapes the capstone, discovers a
second distinct obstruction, attempts to bridge it, and ends with a candid assessment of what was actually
established.

## Results
- M12.1–M12.2: S(T) is confirmed log-correlated in real-zero data (fitted covariance constant 0.0465 vs. predicted 1/(2π²)=0.0507), and an exact dictionary links the regularized Hodge gap from an earlier phase to the extreme normalized slope of S(T). NUMERICAL / PROVED (the dictionary identity).
- M12.4 (decisive capstone test): the log-correlated/multiplicative-chaos upper bound on a field extreme is a pure first-moment/union-bound argument, using no PSD matrix or positivity certificate — the first mechanism in the programme to genuinely escape the wrong-sign capstone. PROVED/ARGUED.
- M12.3: pricing this mechanism against the actual target reveals a second, distinct obstruction (named N7, the "probabilistic–deterministic barrier"): the union-bound machinery controls statistics of zeros over an ensemble of heights, not the deterministic off-line zero count of the one function ζ; it describes, but does not force. ARGUED (new obstruction identified).
- M12.5: a derandomization bridges N7 in mechanism — the probabilistic union count equals the explicit-formula prime-sum large-value count, bounded by the large sieve, which is deterministic, upper-direction, and not a positivity (numerically the truncated prime sum tracks S(T) with correlation rising from 0.79 to 0.89 as the truncation grows). PROVED (the identity)/ARGUED (mechanism correctness).
- M12.6–M12.7: the moment method is shown sharp in the accessible regime (via rational independence of {log p}), and the extreme/freezing behavior is traced to a Diophantine near-resonance question about prime logarithms; Baker's theorem on linear forms in logarithms is the right deterministic mechanism but is quantitatively far too weak, pivoting the target to the additive energy of {log p} (the same moment-growth exponent k² studied under an earlier phase's ω-class machinery). ARGUED, with explicit numerical near-resonance example.
- M12.9: the supercritical/freezing bound is identified as exactly the (open, unconditional for k≥3) moment problem for ζ's moments — a different, independently open problem, not an RH-equivalence. Candid overall verdict: the full Phase-12 chain is mechanism-correct (each link deterministic, upper-direction, non-positivity) but is a heuristic connection, not a rigorous reduction — several links (the log-correlated picture, the derandomization, and especially the final "extreme control ⟹ no off-line zeros" step) are not proved as theorems. ARGUED/OPEN — explicitly not a proof or reduction.
- M12.10: a correction is recorded downgrading an earlier overclaim; a conceptual map of known "absence of zeros" mechanisms (positivity, counting/density, finite computation, statistics) is built, showing none reaches "none, for all T, deterministically" without being the capstone again. ARGUED (conceptual map, not an impossibility proof).
- M12.11: a genuine attempt to close N7 using Littlewood's lemma (an exact deterministic identity linking ∫log|ζ| to off-line zero counts) is carried through; it is shown to give only a zero-density bound (few off-line zeros), not absence, because a single off-line zero's O(1) contribution is dwarfed by the integral's natural growth with T — closing the gap would require RH-strength control already. NO-GO (for this specific closure attempt), not a general impossibility claim.

## Documents
- `PLAN-RH-PHASE12-log-correlated-upper-bounds.md` — rationale for the log-correlated/multiplicative-chaos route.
- `M12-VERDICT-capstone-escaped-new-barrier.md` — milestones M12.1–M12.7, the capstone-escape finding and N7.
- `M12.8-verdict-freezing-live-frontier.md`, `M12.9-verdict-moment-problem-candid-status.md` — the freezing/moment-problem landing and the candid heuristic-vs-theorem assessment.
- `M12.10-the-meta-obstruction.md` — the corrected conceptual map of absence-of-zeros mechanisms.
- `M12.11-N7-closure-attempt-littlewood.md` — the Littlewood's-lemma attempt and its precise shortfall.
- `experiments/` — supporting numerical scripts for the covariance fit, moment computations, and near-resonance search.

## Relation to other phases
Continues the "wrong-sign capstone" narrative from phases 0–11 (the cohomological turn, phase 10, and hyperbolicity, phase 11), being the first route found to escape it; links its extreme/freezing frontier to the ω-class moment-growth machinery referenced as built in an earlier phase (P2–P5); the moment-problem frontier it lands on is picked up by phase 13.
