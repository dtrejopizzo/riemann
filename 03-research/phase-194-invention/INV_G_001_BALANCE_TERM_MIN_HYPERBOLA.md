# INV_G_001 — The balance term M(n) = Σ_{de=n} min(d,e): Dirichlet series, inversion, sign test (track G)

Track G.


## 0. Corpus / index check
- ROUTES-TRIED-INDEX: "hyperbola" only as R161_002 tail (DEAD, nonnegative telescoping divisor-hyperbola weights; sign only at terminal jump). min(d,n/d) only in INV_D_001/INV_E_001 as OPEN residue. C3 identity (README l.110, Div+Near, E_M(N)) is the nearest relative.
- INV_C_001: X-term ∫F e^{−|u|/2} > 0 (Near, CA_M_001). This kernel reappears below (§1.3): the balance term is a Near-type object.
- Grid/crossword: no hit for min-kernel divisor sums. New reason: the object (M as a PD-kernel divisor sum after σ^{*−1}*L) is the declared residue of INV_E_001, never analysed.

## 1. Dirichlet series of M (PROVED)
1.1 Layer-cake: min(d,e) = Σ_{k≥1} 1[d≥k]1[e≥k], hence for Re s > 2
  D_M(s) := Σ M(n) n^{−s} = Σ_{k≥1} ζ_{≥k}(s)²,  ζ_{≥k}(s) = Σ_{m≥k} m^{−s}.
  Equivalent: 2Σ_d d^{1−s}ζ_{≥d}(s) − ζ(2s−1) (INV_E_001). Sum of squares of incomplete zetas: not an Euler product.
1.2 Hyperbola form: M(n) = σ(n) − Σ_{d|n, d>√n}(d − n/d), i.e. D_M = ζ(s)ζ(s−1) − (hyperbola tail).
1.3 Positive-definite form. min(d,e) = √(de)·e^{−|log d − log e|/2}, and e^{−|u|/2} has Fourier transform 1/(¼+ξ²) > 0. Hence
  M(n) n^{−½} = (1/2π)∫ σ_{2iξ}(n) n^{−iξ} dξ/(¼+ξ²),
  D_M(s) = (1/2π)∫_ℝ ζ(s−½+iξ) ζ(s−½−iξ) dξ/(¼+ξ²)   (Re s > 3/2).
  For real s = σ > 3/2: D_M(σ) = (1/2π)∫|ζ(σ−½+iξ)|² dξ/(¼+ξ²) > 0. Shifting ξ across the poles ±i/2 of the kernel produces ζ(s)ζ(s−1) (the σ part) plus the remainder = −tail of 1.2. So "Mellin of min(1,x)" = the kernel 1/(¼+ξ²), and convexity of min at d = e is exactly the cusp of e^{−|u|/2}, i.e. positive-definiteness.

## 2. Push through σ^{*−1}*L; contribution to 𝔞_T (PROVED, bookkeeping)
c_M := σ^{*−1}*(M·log) has Dirichlet series −D_M′(s)/(ζ(s)ζ(s−1)) =
  −(1/2π)∫ ∂_s[ζ(s−½+iξ)ζ(s−½−iξ)] / [ζ(s)ζ(s−1)] dξ/(¼+ξ²).
Contribution to 𝔞_T on 𝒫_T (from INV_E_001 §3):
  𝔞_T^{(M)}(g) = −½ Σ_{n<e^{2T}} n^{−½}(1+n)^{−1} F(log n) c_M(n),  with c_H + c_M = 2Λ(1+n).
σ^{*−1} = μ*(μ·id) changes sign (σ^{*−1}(p) = −(1+p)); Exact: c_M(p) = 2 log p, c_M(p²) = (2+p)2log p − 2(1+p)log p = 2 log p (PROVED); so on prime powers M contributes only O(log p), while c_H(p) = 2p log p carries the bulk of 2Λ(1+n). c_M is not multiplicative and has no closed Euler form; its sign on general n is not controlled by any inequality of §3.

## 3. (ℕ,+,·) inequalities at d ≈ n/d and their fate
- (I1) M ≥ 0, D_M(σ) > 0 (sum of squares, 1.1/1.3). (I2) convexity: M(n) ≤ τ(n)√n, equality iff only balanced pairs. (I3) hyperbola symmetry d↔n/d: M = 2Σ_{d<√n} d + [n square]√n.
- Under σ^{*−1}*L: (I1) becomes ratios ζ(s−½±iξ)/ζ(s)ζ(s−1) — no coefficient positivity survives (the denominators carry μ). (I2) maps to −2ζ′(s−½)ζ(s−½)/(ζ(s)ζ(s−1)), a half-shifted log-derivative mixing walls at ½ and 0,1: sign-indefinite. (I3) is linear, inherits μ*(μ·id).
- Theorem G1 (NO-GO, class 𝓒_G). Class 𝓒_G: inequalities derived from (a) the PD kernel e^{−|log d/e|/2} (equivalently convexity of min), (b) layer-cake/hyperbola rearrangements, (c) Dirichlet algebra incl. σ^{*−1} and L. Every ingredient uses only that d,e range over a multiplicative semigroup of reals ≥1 with a counting function; all identities 1.1–2 hold verbatim for any Beurling generalized-integer system (with σ, M, ζ replaced by their Beurling analogues). Hence any sign conclusion in 𝓒_G is comb-generic and is blocked by thm:shape (B″) of Paper 46 (Beurling systems where the corresponding 𝔞_T-sign fails exist, CITED there). PROVED modulo the CITED B″ input.
- The positive part (I1) in the form ∫ F e^{−|u|/2} is the INV_C_001 X-term / Near (CA_M_001): the balance term re-enters as Near. "Arch_T − Near-comb ≥ 0 on 𝒫_T" is 𝔞_T ≥ 0 rewritten: REF-D.

## 4. Verdict
- PROVED: 1.1 (sum of squares of incomplete zetas), 1.2, 1.3 (PD integral representation; min-convexity = PD of e^{−|u|/2}), §2 identity.
- NO-GO (class 𝓒_G): no signed term from min-convexity / hyperbola symmetry survives σ^{*−1}*L; any such term would be comb-generic (B″).
- REF-D: the sign statement after inversion (= Near vs Arch).
- Residue M(n) of INV_E_001: CLOSED. Do not retry min/hyperbola balance with σ-inversion. A non-comb-generic sign must use an input that fails for Beurling systems (e.g. additive structure m = kn + r of ℕ itself, not only (·) and real logs).
