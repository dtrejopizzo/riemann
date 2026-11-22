# An Energy Decomposition of the Riemann Hypothesis: the Off-Line Energy I, its Integral Representation, and Structural Barriers

The paper studies the off-line energy I = Σ b_j². Here ρ = 1/2 + b + iγ runs over the off-line zeros of ζ, one per quadruple. RH is equivalent to finiteness (I < ∞) together with purity (I < ∞ ⇒ I = 0). The paper proves exact identities and bounds for I and its truncation E(T), and discusses why standard methods do not reach finiteness.

## What the paper proves or observes

- Theorem 2.1: E(T) = Σ_{γ≤T} b² ≪ T/log T, unconditionally, from Selberg's density theorem.
- Theorem 3.1: an exact Green–Littlewood identity expressing E(T) through the area integral of log|ζ| over the right half-strip, the constant 1/8 and a boundary term of size O(log T).
- Theorem 4.2: the Cesàro-averaged integral always has a limit in [−π/8, +∞], and this limit equals πI − π/8.
- Theorem 5.1: RH ⇒ (m < ∞) ⇒ I < ∞ ⇒ Lindelöf ⇒ density hypothesis. No converse is known.
- Section 6: Theorem 6.3 is the energy version of the conditional dichotomy of Paper 30 (sequential self-approximation implies I ∈ {0, ∞}). Theorem 6.5 and Proposition 6.6 prove unconditional anti-recurrence: when 0 < I < ∞, the good shifts near an off-line zero form a bounded set. Corollary 6.8: if I < ∞, self-approximation is equivalent to RH.
- Theorem 7.3: an exact boundary-flux identity on the critical line. It gives no new bound: the flux bound of Corollary 7.4 recovers Littlewood's.
- Section 8: barriers for zero-density bounds, the Littlewood–Jensen–mollifier argument (under an additional tail hypothesis (T2)) and sign-blind moment bounds. Remark 8.7 (isotropy of the Dirichlet energy) is heuristic.
- Theorem 9.2: the mollified second moment is at least 1 + δ for every divisor-bounded mollifier of length T^θ with θ ≤ 1/2 − δ. The rate log((1−θ)/θ) is weaker than the known value 1/θ for the optimal mollifier. Proposition 9.6: for θ ≥ 1/2 the same method gives only the trivial bound for the mollifier μ·1_[1,X]. Proposition 9.7 relates the long range to a bilinear-range hypothesis.
- Theorem 10.2: zeros of the heat-flow functions H_t, t ∈ [0, 1], are counted in unit windows with a bound O(log γ), by a short self-contained proof (known for t ≤ 1/2).
- Section 11 is a heuristic classification of detection methods and contains no theorems.

## Known and new

Theorem 2.1 and Theorem 4.5 follow in a few lines from Selberg's and Littlewood's work and may be folklore. The dichotomy under self-approximation is Paper 30's, here extended from the count m to the energy I. For 0 < t ≤ 1/2 the unit-window bound with an absolute constant independent of t is Theorem 1.5(iv) of Polymath 2019 (refining Ki–Kim–Lee, Theorems 1.3 and 1.4); Theorem 10.2 adds the range 1/2 < t ≤ 1 and a short self-contained proof. The mollifier lower bound over the whole divisor-bounded class has not been located in the literature.

## Relation to other papers

Extends Paper 30 (Definition 2.1, Theorem 2.3) from m to the energy I.

## Files

- [main.tex](main.tex): LaTeX source.
- [energy-decomposition.pdf](energy-decomposition.pdf): compiled paper, 30 pages.
