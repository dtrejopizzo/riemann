# Phase 24 — lower bounds for b_j and local rigidity of log|ζ|

Given a hypothetical off-line zero ρ_j = (1/2+b_j)+iγ_j, phase 24 asks the
converse question to phase 22-23's upper bounds: is there any argument
forcing a *lower* bound b_j ≥ F(γ_j), and does the local shape of
log|ζ(1/2+it)| near t = γ_j conflict with known rigorous results (Selberg's
central limit theorem, extreme-value results, moment asymptotics)? Four
methods are audited to their exact limit; no numerics are used.

## Results
- Proposition 24-A.1: comparing the defect D_j(x) with the unconditional
  Korobov-Vinogradov error term produces no lower bound on b_j, because the
  unconditional on-line-zero contribution ψ₀(x)-x = O(x^{1/2}(log x)²)
  always dominates D_j(x) = O(x^{1/2+b_j}) for any b_j — the defect's signal
  is buried under on-line noise. **PROVED (negative)**.
- Jensen/Hadamard evaluation at t = γ_j also fails to give a lower bound:
  the point 1/2+iγ_j sits exactly on the boundary of the relevant disk, so
  Jensen's formula does not apply, and moment methods localize the
  contribution to O(b_j), too weak to isolate a bound.
- Proposition 24-B.2 / Corollary 24-B.3: the renormalized local profile of
  log|ζ| induced by an off-line orbit, in rescaled coordinates u =
  (t-γ_j)/b_j, converges to a universal, deterministic Lorentzian shape
  P(u) = log(1+u²), independent of b_j to leading order. **PROVED** (new
  positive geometric result).
- That universal profile is shown to be geometrically submerged under the
  fluctuations of the log-correlated field model and so produces no
  incompatibility. **Negative** as a route to excluding the defect.
- Inventory (§1 of doc 03) of rigorous unconditional results on log|ζ(1/2
  +it)| (Selberg CLT, Ramachandra/Titchmarsh upper bounds, Titchmarsh and
  Radziwiłł-Soundararajan deep-minima results, Harper/Soundararajan/
  Arguin-Bovier-Kistler moment and extreme-value results): **none** gives
  an unconditional pointwise lower bound on log|ζ| at an arbitrary point,
  so none restricts b_j (Proposition 24-C.1). **PROVED (negative)**.
- Proposition 24-C.2 (interference dilemma): even a hypothetical lower
  bound would be confounded by the nearest on-line zero, making it
  impossible to isolate the off-line zero's contribution without
  understanding the joint distribution of on-line and off-line zeros.
- Overall: phase 24 is a systematic triple negative result (no lower bound
  on b_j is obtainable by any of the methods tried), with one durable
  positive byproduct — the universal Lorentzian local profile.

## Documents
- `00-setup.md` — the three b_j-decay regimes and the central question.
- `01-lower-bounds-bj.md` — audit of methods for a lower bound on b_j
  (explicit formula, Hadamard+Jensen, moments), all negative.
- `02-local-profile.md` — derivation of the universal renormalized
  Lorentzian local profile P(u) = log(1+u²) (Proposition 24-B.2).
- `03-rigorous-chaos.md` — inventory of rigorous results on log|ζ| and the
  final compatibility/interference propositions, plus the frank assessment
  and summary table.

## Relation to other phases
Continues phases 22-23's study of Hypothesis D; confirms that the
spectral/analytic routes are exhausted and explicitly hands off the only
remaining route — analytic uniqueness of the Euler product forcing zeros
onto the critical line (Wall W4-RSRP) — to phase 25.
