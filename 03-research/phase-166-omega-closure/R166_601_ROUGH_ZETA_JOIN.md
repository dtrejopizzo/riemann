# R166_601 — The rough-zeta join: ζ_{≥X}, Legendre, and the twisted zero sum

Status: **CLOSED NEGATIVE (E1 / identification).** No label changes.
Inputs: R166_190 (Ronda 9: (G), (N)), R166_501 Thm A, R166_405, R166_103 §(β), R164_501 Prop 4, R163_801 Thm 3, R164_401 Thm R.

## Status table

| # | Statement | Label |
|---|---|---|
| 1 | ζ_{≥X}(s) = A_X(s)ζ(s), A_X(s) := ∏_{p<X}(1−p^{−s}) = Σ_{d∣P} μ(d)d^{−s} (finite, entire) | PROVED |
| 2 | Φ(x,X) = Σ_{d∣P} μ(d)⌊x/d⌋ = ρ_X x + E_X(x), E_X(x) = −Σ_{d∣P} μ(d){x/d}, period P, |E_X| ≤ 2^{π(X)−1} | PROVED (Legendre) |
| 3 | Mean of E_X over a period is 0 for X > 2 | PROVED |
| 4 | Identity ℰ_X(ρ*) = −ρ_X/(ρ*−1) for all X is equivalent to A_X(ρ*)ζ(ρ*) = 0, i.e. to ζ(ρ*) = 0 | PROVED (tautological, E1) |
| 5 | Perron for Φ(x,X) has **no** zero sum: the twisted sum Σ_ρ A_X(ρ)x^ρ/ρ does not occur | PROVED |
| 6 | Zeros of ζ enter rough-integer counting only through ψ_{≥X} = ψ − (window), i.e. via −ζ′_{≥X}/ζ_{≥X} = −ζ′/ζ − Σ_{p<X} log p/(p^s−1): window-affine | PROVED |
| 7 | Rough-system Beurling family (θ_N = 0 for every X) contradicts an off-line zero | FALSE as a mechanism: consistent with any zero set; Hilberdink-type constraint satisfied by the Ω(x^{1/2}) of ψ | ARGUED (cited Hilberdink 2005) |
| 8 | Isolation of ρ* through the weights A_X(ρ) | Moot (item 5); independently, no isolation: log|A_X(β+iγ)| behaves like a random walk of variance ≍ Σ p^{−2β}, comparable for β = ½ and β = β* | ARGUED |

## 1. Exact identities (task 1)

Let P = ∏_{p<X} p, ρ_X = A_X(1) = ∏_{p<X}(1−1/p).

(1a) Legendre: Φ(x,X) = #{n ≤ x : p∣n ⇒ p ≥ X} = Σ_{d∣P} μ(d)⌊x/d⌋ = ρ_X x − Σ_{d∣P} μ(d){x/d}.
(1b) Mean: ∫_0^P {x/d}dx/P = ½, so mean E_X = −½Σ_{d∣P}μ(d) = 0 when P > 1. So c_X = 0; no adjustment needed.
(1c) Mellin. For Re s > 1, ζ_{≥X}(s) = s∫_1^∞ Φ(x,X)x^{−s−1}dx. Inserting (1a) termwise and using, for each d,
 s∫_1^∞ ⌊x/d⌋ x^{−s−1}dx = d^{−s}·s∫_{1/d}^∞ ⌊y⌋ y^{−s−1}dy = d^{−s}ζ(s) (since ⌊y⌋ = 0 on [1/d,1)),
gives ζ_{≥X} = Σ_{d∣P}μ(d)d^{−s}ζ(s) = A_X ζ, valid by continuation for Re s > 0 (with ζ(s) = s/(s−1) − s∫_1^∞{y}y^{−s−1}dy). Equivalently
 ℰ_X(s) := ∫_1^∞ E_X x^{−s−1}dx = A_X(s)ζ(s)/s − ρ_X/(s−1).
Hence "ℰ_X(ρ*) = −ρ_X/(ρ*−1)" ⟺ A_X(ρ*)ζ(ρ*) = 0 ⟺ ζ(ρ*) = 0 (A_X vanishes only on Re s = 0). **The whole X-family is ζ(ρ*) = 0 multiplied by a known finite Dirichlet polynomial. Tautological (E1).** Note also ℰ_X(ρ*) → 0 as X→∞ only because ρ_X → 0; no independent bound on Mellin transforms of bounded periodic mean-zero functions at Re s > 0 can contradict it, because ℰ_X is literally A_Xζ/s − ρ_X/(s−1), whose value at a zero of ζ is forced.

## 2. Resolution of the "paradox" (task 2)

The brief's proposed identity E_X(x) = Σ_ρ A_X(ρ)x^ρ/ρ + … is **not** correct. Perron applied to ζ_{≥X}(s)x^s/s picks up residues at **poles** of the integrand: s = 1 (gives ρ_X x) and s = 0 (A_X(0)ζ(0) = 0 for X > 2). Zeros of ζ are zeros of the integrand, not poles; they contribute nothing. The exact Φ has no x^ρ terms, and no truncated Perron formula for Φ has any either; the bounded remainder E_X is the Perron remainder (Voronoi/Fourier series of {y}), not a zero sum. This is the same reason ⌊x⌋ = Σ_{n≤x}1 carries no information about ζ's zeros, while ψ(x) = Σ Λ(n) does: zeros enter counting functions only through ζ′/ζ or 1/ζ.

The rough object that does see zeros is ψ_{≥X}(x) = Σ_{n≤x, p∣n⇒p≥X} Λ(n) = ψ(x) − Σ_{p<X, p^k≤x} log p, whose explicit formula is ψ's zero sum minus a finite window term: x − Σ_ρ x^ρ/ρ − (window) + …. Its weights are 1, not A_X(ρ); the X-dependence is affine in the window Λ. This is R166_103 §(β): −ζ′_{≥X}/ζ_{≥X} = 𝒯^new, nothing beyond it. Under R166_501 Thm A, this lands in (1.1).

## 3. The Beurling/sieve angle (where it stops)

- For each X, the X-rough integers form a discrete Beurling system with N_X(x) = ρ_X x + O(2^{π(X)}) (θ_N = 0) and ψ-error equal to ζ's (minus a window). Hilberdink-type theorems (integer-valued N and ψ errors cannot both be O(x^α), α < ½) are satisfied for every X by the unconditional ψ(x) − x = Ω_±(x^{1/2}log log log x) (Littlewood). There is no contradiction for any zero configuration with β* < 1. The family in X adds nothing: the N-side is controlled by Legendre (zero-blind), the ψ-side by ζ (X-independent up to a window).
- Ranges. Legendre is nontrivial only for x ≫ 2^{π(X)}log X, i.e. u = log x/log X ≳ X/log²X, where Buchstab's ω(u) = e^{−γ}+O(e^{−u}) and both descriptions read Φ ≈ ρ_X x. The dependence of ρ_X on the primes is Mertens', where an off-line zero contributes a relative O(X^{β*−1}) term. But ρ_X is an exact finite product, so there is nothing for it to contradict. In the sieve range (u bounded) the error in Φ(x,X) ~ xω(u)/log X does depend on zeros via π(t), t ∈ [X,x]. However, Legendre's bound is useless there (2^{π(X)} ≫ x), so the two never compete.
- **Stop (precise):** every statement derived from Legendre is a consequence of ζ = Σn^{−s} together with the finite Euler factors. It holds whatever the zero set is (it is identity 1), so it fails requirement (G)/R166_501: it does not use Λ beyond the window in a non-affine way. The only object that does use Λ on p ≥ X is ψ_{≥X}, which is affine in the window and gives back (1.1).

## 4. Falsifier checks

- M_m (ζ × rational R, non-atomic density β_m): the rough family A_X ζ R exists formally, but its coefficients are not 0/1 and the counting error is not bounded periodic. So the separator (N) is formally satisfied. This is vacuous, because for ζ itself the identity carries no zero information. A separator attached to an empty mechanism proves nothing.
- f_t (no Euler product): no rough family. Same remark.
- Internal falsifier: replace ζ by any Dirichlet series with 0/1 coefficients and a finite-Euler-factor sieve. Legendre-type identities hold verbatim and never mention zeros. That confirms the information content is nil.

## 5. Cells

- **4F** (rough-integer / Legendre positivity): CLOSED, E1. The identity is tautological (items 1–4).
- **5G** (twisted zero sums Σ A_X(ρ)x^ρ/ρ): CLOSED. The object does not exist (item 5). The correct object ψ_{≥X} is window-affine = R166_103 𝒯^new.
- **7F** (Beurling family in X, θ_N = 0): CLOSED. It is consistent with all zero sets (item 7), and there is no isolation (item 8).

Record for the master grid: "rough-zeta join: ζ_{≥X} = A_Xζ; Legendre zero-blind; zeros enter only via ζ′/ζ ⇒ (1.1). NO-GO."
