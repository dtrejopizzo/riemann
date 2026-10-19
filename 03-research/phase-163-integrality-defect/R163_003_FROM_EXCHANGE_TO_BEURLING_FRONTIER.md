# R163_003 — From the canonical exchange to the Beurling θ<½ frontier

**Status:** reduction observation (review) + target formulation. RH is not asserted.

## 1. What q_E exactly is

By the explicit formula, in u=log x,

```
dΠ_ζ = (smooth part: pole + Γ) − Σ_{ρ on the line} (…) − Σ_{quartets} (…),
```

and the quartet term is, term by term, `−q_E` (R163_001 §2). That is: **q_E is the off-line part
of the explicit formula**. "Property 2" (ζ's exact arithmetic forces q_E=0) is, therefore,
literally the statement "ζ's explicit formula has no off-line component," i.e. RH (row 7 of the map,
wall E1). The exchange adds no content: it reorganizes the explicit formula. This does not invalidate
R163_001/002 (correct tools), but it fixes that the novelty must lie in **how** one proves that the
growing component of dΠ_ζ − (smooth) is zero, not in its restatement.

## 2. Equivalent restatement in the language of Beurling systems

The growing component e^{(½+β)u} of dΠ_ζ − (smooth) is zero ⟺ ψ(x) = x + O(x^{½+ε}).

On the integer side, ζ has N(x) = ⌊x⌋ = x + O(1): the most regular Beurling system possible
(θ = 0). The literature (in `00-references/beurling-dmv`) establishes:

- **DMV (2006):** for every θ ∈ (½,1) there exist systems with N(x) = ρx + O(x^θ) and primes with
  de la Vallée Poussin error (RH fails, zeros approaching Re s = 1). Integer regularity with θ > ½
  does **not** control the zeros.
- **Broucke (arXiv 2409.10051):** density estimates N(α,T) for θ-regular systems in the range
  α > (1+θ)/2, optimal at least for θ > ½; explicit open question: if a_j ≡ 1, can the Euler product or
  multiplicativity be exploited to improve it.
- **Broucke–Debruyne–Vindas (2004.11501):** systems with RH and extreme oscillation in N(x); the
  Bateman–Diamond problem on exponents α*(β), β*(α) open except at the extremes.

**The DMV method needs θ > ½.** Nothing in these references builds a system with N(x) = ρx + O(x^θ),
θ < ½, and zeros with Re s > ½.

## 3. Target (frontier θ<½)

> **(BF_θ)** Does there exist, for some θ < ½, a Beurling system with N(x) = ρx + O(x^θ) whose zeta
> has a zero with Re s > ½?

A useful dichotomy for the programme:

- If **no** such system exists for any θ < ½ (i.e. integer error < √x ⇒ Beurling RH), then ℤ (θ=0) gives RH. The
  piece to be created is then a stability theorem "integer regularity below √x ⇒ zeros on the
  line," uniform over the Beurling class; it is a **class** statement that ζ satisfies with margin
  (θ=0 ≪ ½), so it escapes the "isolated ζ" wall (Paper 48, W1/W3) and Theorem M (it is not per-window).
- If it **does** exist for every θ > 0 (or for θ = 0 with bounded error but no lattice), then
  N's regularity is not enough and all that remains is the **exact lattice rigidity** N(x)=⌊x⌋ (which
  does force ℕ and the ordinary primes): the discontinuity between "O(1)" and "exactly ⌊x⌋."

Both branches are falsifiable and neither is on the map (cells 5G/5H, integrality × families row).
Falsifiers: Epstein (not Beurling: no Euler), DH (no Euler), deletion/κ (is N(x) θ-regular with θ<½?
— check), M_m (not Beurling), R162_2901 Thm B (positive Beurling, but with what θ? — compute).

## 4. CORRECTION (R163_190)

- §1: q_E is not "exactly the off-line part": it is (Σ_b e^{bu} − Σ_a e^{au})/u, i.e. the off-line
  term with reversed sign **plus** that of the double zeros inserted on the line. The conclusion
  (property 2 ⟺ RH) stands.
- §2: the claim "no reference builds θ<½ with zeros off the line" is **FALSE**. Broucke
  (2409.10051 §6.1) uses ζ_θ(s)=ζ((s−θ)/(1−θ)): in the extended Beurling class it gives N=(1−θ)x+O(x^θ) and zeros at
  Re s=(1+θ)/2>½ for every θ∈(0,1). (BF_θ) has answer YES in the extended class; branch 1 is false there.
- Only **(BF_θ^disc)** survives: discrete systems (integer multiplicities). Zhang (2007) gives
  discrete examples with error √x·exp(c(log x)^{2/3}), just above the threshold. New falsifier: ζ_θ.
