# R166_702: Position-tuned and prime-replacement discrete Beurling systems (grid cell 5G)

Pure mathematics, no numerics. Inputs: R164_201 (Theorem L, L*, Lemma W), R164_503 (off-lattice; §3 prime-side cap,
§4.2 smearing ⇒ branch points), R163_803 (Theorem C), R163_101, 00-references/beurling-dmv. Gate 1, Row D and (★_cell) stay **OPEN**.

## Status table

| # | Statement | Label |
|---|---|---|
| 1 | Replacement class 𝓡(S,η): a new zero of ζ_𝒫 = ζ·Π at Re s = β (not a zero of ζ) needs Σ_{p∈S} p^{−β} = ∞ or Σ_{p∈S} p′^{−β} = ∞ | PROVED (§1.1) |
| 2 | In 𝓡, a new zero at β > ½ costs counting error ≳ x^{β−ε} (θ ≥ β > ½): worse than Theorem C | ARGUED (upper-bound heuristic of the brief made into a lower bound only modulo cancellation among the per-prime sawtooth terms; §1.2). Consistent with R164_503 item 5 (prime-side cap at ½) |
| 3 | "A shifted prime is a fractional multiplicity": true only for the density (s = 1) and for \|t\| ≪ 1/\|log u\|; false as a Dirichlet-series identity | PROVED (§2.1) |
| 4 | **Lemma PT (local Besicovitch defect).** For any finite integer configuration of copies at q_p·u_i (u_i > 0), the defect ε_p(s) = U_p(s) − p^a, U_p(s) = Σ_i n_i u_i^{−s}, satisfies M_t\|ε_p(σ+it)\|² = (n_1 − p^a)² + Σ_{u_i≠1} n_i² u_i^{−2σ} ≥ ‖p^a‖² | PROVED (§2.2) |
| 5 | **Corollary (lattice rounding is optimal).** Among all position-tuned configurations at q_p, the local mean-square defect is minimized by putting every copy at q_p with n_1 = nearest integer to p^a; any position shift strictly increases it (a copy shifted by a tiny η adds ≈ 1, not ≈ ε²) | PROVED (§2.2) |
| 6 | The brief's hope "the linear term vanishes identically" | **FALSE**: tuning kills ε_p(1) (the density) only; the linear chaos L(s) = Σ_p ε_p(s) p^{−a−w} keeps coefficients of mean square ≥ ‖p^a‖² (item 4) |
| 7 | **Theorem PT (barrier).** Position-tuned systems have counting-error exponent ≥ (1−θ)/2 ≥ 1/3 for θ ≤ 1/3, the same barrier as L* | ARGUED (§3; exact gap = the gap of L* plus a Montgomery–Vaughan spacing condition). The power form "exponent > θ" is PROVED only for configurations that are lattice-type (𝒦_θ); for genuinely off-lattice tuned configurations it is ARGUED |
| 8 | Problem 6 below 1/3 (Paper 48) | **OPEN**; position tuning is not a counterexample mechanism (item 5–7) |
| 9 | Falsifiers ζ_θ, Theorem L, Hilberdink/Révész | all consistent (§4) |

**Decision.** Position tuning is closed negative at the local level (PROVED) and at the global level with the L* gap (ARGUED).
It does not give θ < 1/3. It is the "position" version of R164_503 §4.2 (smearing), now with p-dependent shifts.

## 1. Prime replacement 𝓡(S, η)

Primes p ∈ S replaced by p′ = p e^{η_p}, all other rational primes kept, multiplicity one. ζ_𝒫 = ζ·Π, Π = ∏_{p∈S}(1−p^{−s})/(1−p′^{−s}).

### 1.1 Zero creation needs divergence (PROVED)
For σ > 0 each factor is holomorphic and non-zero. |log(1−z)| ≤ 2|z| for |z| ≤ ½. If Σ_{p∈S}(p^{−β}+p′^{−β}) < ∞, then
Σ|log(1−p^{−s})| + |log(1−p′^{−s})| converges uniformly on Re s ≥ β, so Π is holomorphic and zero-free there; the strip zeros of ζ_𝒫
in Re s ≥ β are those of ζ. ∎ So a new zero at β needs #S(x) (or #S′(x)) ≠ O(x^{β−δ}) for every δ > 0 — **not** small η (the brief's
condition Σ|η_p| log p p^{−σ} = ∞ is the condition for the *difference* series; at fixed s the factor ratio is 1 + O(|η_p||s|p^{−σ}),
so both conditions are needed: S of counting exponent ≥ β, and η_p not summably small against it).

### 1.2 The cost in N (ARGUED)
N_𝒫 = Σ over the S-free integers ν and S′-products: each p ∈ S contributes a density change x·η_p/p (absorbed in ρ) and a
sawtooth fluctuation of size O(1) at scale x/p. With #S(x) ≥ x^{β−ε}, the sum of ≥ x^{β−ε} sawtooth terms ψ(x/p) − ψ(x/p′) is of
size x^{β−ε} unless they cancel; random-sign heuristics give x^{(β−ε)/2}·(…) only if the phases decorrelate, but the pairs
(p, p′) are tied to the zero-producing phase η_p ∝ cos(γ log p − φ), which correlates them. No lower bound is proved. Either way the
mechanism is prime-side (ψ_𝒫 = ψ + Σ_{S} …), and R164_503 §3 (ARGUED) caps all prime-side constructions at x^{½+o(1)}. So 𝓡 cannot
beat ½, a fortiori not 1/3. **ARGUED.**

## 2. Position tuning at the Theorem C lattice

Setting (R163_803): a = θ/(1−θ), w = (s−θ)/(1−θ), q_p = p^{1/(1−θ)}, so q_p^{−s} = p^{−a−w}. Target weight p^a at q_p.
Tuned configuration: integer copies n_i at q_p u_{p,i}. Then the linear part of log ζ_𝒫 is Σ_p U_p(s) p^{−a−w}
= P(w) + L(s), P(w) = Σ_p p^{−w}, L(s) = Σ_p ε_p(s) p^{−a−w}.

### 2.1 Fractional multiplicity by position (PROVED, item 3)
A copy at q u contributes u^{−s} to U_p. At s = 1 this is 1/u ∈ (0,1): any fraction, e.g. u = 1/{p^a} gives ε_p(1) = 0 with
n = ⌊p^a⌋ + one shifted copy. But u^{−σ−it} = u^{−σ}e^{−it log u} rotates once |t| ≳ 1/|log u|; here |log u| = |log{p^a}| is not small,
so the "fraction" holds on a bounded t-range only. Counting error at x is governed by t up to x^{c}. ∎

### 2.2 Lemma PT and the optimality of lattice rounding (PROVED, items 4–5)
U_p(σ+it) − p^a = (n_1 − p^a) + Σ_{u_i ≠ 1} n_i u_i^{−σ} e^{−it log u_i} (merge equal u_i). This is a finite almost-periodic polynomial
with distinct frequencies; by Parseval for Bohr–Besicovitch means, M_t|·|² = (n_1−p^a)² + Σ n_i² u_i^{−2σ}. Since n_1 ∈ ℤ,
(n_1 − p^a)² ≥ ‖p^a‖², and the remaining terms are ≥ 0, with equality iff no copy is shifted and n_1 is a nearest integer. ∎
A copy shifted by tiny η contributes ≈ 1 to the mean square: shifting makes the defect worse, not better.

## 3. Theorem PT (ARGUED)
Heuristic barrier: L(σ+it) is a generalized Dirichlet series with coefficients of local mean square ≥ ‖p^a‖² p^{−2a}·p^{−2Re w}. If the
frequency sets {log q_p u_{p,i}} are uniformly separated on the relevant scale, Montgomery–Vaughan gives
(1/T)∫_T^{2T}|L|² ≍ Σ_p M|ε_p|² p^{−2a−2Re w}, which diverges exactly for Re w ≤ ½ − a, i.e. σ ≤ θ + (1−θ)(½−a) = (1−θ)/2.
Then ζ_𝒫 = ζ(w)·(higher terms)·e^{L} cannot have the polynomial growth required by N − ρx = O(x^{θ′}) (R164_503 item 1) for
θ′ < (1−θ)/2, giving exponent ≥ (1−θ)/2 ≥ 1/3 when θ ≤ 1/3.
**Exact gaps.** (G1) a mean-square bound for L does not by itself bound e^{L} from below in mean (cancellation with ζ(w) and the
higher chaos must be excluded) — this is the L* gap of R164_201 §3.5 in Dirichlet-series form; (G2) spacing: copies with tiny shifts
create frequency pairs at distance |log u| ≪ 1/T, where MV gives only the merged (worse, i.e. larger) coefficient — harmless for the
lower bound direction but must be written out. Power-form version: for tuned configurations that coincide with lattice ones,
Theorem L applies (PROVED); for genuinely shifted ones, Theorem L's Franel test ψ(X/p) no longer sees the shifted mass and no
PROVED replacement is given here.

## 4. Falsifier checks
- **ζ_θ.** U_p ≡ p^a (constant, non-integer): impossible for integer configurations since the Besicovitch mean of U_p is n_1 ∈ ℤ.
  Lemma PT is exactly the discreteness obstruction; ζ_θ is excluded. ✔
- **Theorem L.** Tuned systems are outside 𝒦_θ; Lemma PT shows they are no better than 𝒦_θ locally. Consistent. ✔
- **Theorem C, θ > 1/3.** Σ_p‖p^a‖²p^{−2a} < ∞ for a > ½: the barrier (1−θ)/2 < θ is inactive. Consistent. ✔
- **Hilberdink 2005 / Révész.** θ < ½ forces ψ-exponent ≥ ½; the tuned systems keep the ζ(w)-zeros at Re s = (1+θ)/2 > ½ (L
  converges in L² at Re w = ½ since Σ p^{−1−2a} < ∞). Consistent. ✔
- **R164_503 §4.2.** p-independent smearing ⇒ branch points (PROVED there); p-dependent tuning avoids branch points (each
  U_p(s) is attached to a single p) but pays item 4. Consistent and complementary. ✔

## Ledger
| id | item | status |
|---|---|---|
| R166.702a | Lemma 1.1 (replacement zeros need divergent S) | PROVED |
| R166.702b | Lemma PT + lattice-rounding optimality | PROVED |
| R166.702c | "linear term vanishes identically" under tuning | REFUTED (PROVED) |
| R166.702d | Theorem PT, exponent ≥ (1−θ)/2 | ARGUED; gaps G1 (= L* gap), G2 (spacing) |
| R166.702e | 𝓡 class costs θ ≥ β | ARGUED (no lower bound on sawtooth cancellation) |
| O166.702 | Problem 6 below 1/3 | OPEN; mechanism must be integer-side and non-rescaled (R164_503 §4.3) |

## Grid cell 5G (append to R162_2300 master grid)
`5G | position-tuned & prime-replacement Beurling | Lemma PT PROVED: local Besicovitch defect ≥ ‖p^a‖², lattice rounding optimal, shifts make it worse; "linear term vanishes" REFUTED; replacement zeros need #S ≥ x^{β−ε} PROVED; barriers (1−θ)/2 (tuned) and β (replacement) ARGUED; Problem 6 < 1/3 OPEN; no label change | R166_702`
