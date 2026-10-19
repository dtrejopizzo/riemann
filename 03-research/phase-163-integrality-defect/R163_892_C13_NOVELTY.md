# R163_892 — External novelty check for Theorem C (R163_803, discrete C_{1/3})

Editor pass; web search (arXiv, Google-indexed). No , no numerics.

## Verdict
**No unconditional discrete construction with N-exponent β < ½ and Beurling zeta zeros with real part > ½ was found.** The closest prior art is **conditional on RH** and covers a **disjoint** parameter region. Theorem C appears to be new. Before any priority claim, still do a full-text check of Diamond–Zhang §17 and of the papers citing 2309.01567.

## Closest prior art
**Broucke–Debruyne–Révész, "Some examples of well-behaved Beurling number systems", arXiv:2309.01567 (v2, 26 Jun 2024).** I read the full text (pdftotext).
- Thm 1.1: [α,β]-systems exist for all α ∈ [0,1), β ∈ [½,1). This is unconditional and uses discretization via Thm 1.2 (Broucke–Vindas).
- p. 4: discretizing a continuous system "can only control the integers up to O(x^{1/2+ε})". Their §5: "one has to construct a discrete example right from the start".
- **Thm 1.3 (assume RH):** [½,β]-systems exist for 0 ≤ β < ½ (primes P ∪ P^{1/β}). [α,β]-systems exist for ½ < α < 2/3 and 2α/(α+2) ≤ β < ½ (they delete a random subsequence of the rational primes and add P_D and P^{1/β}).
  - Under RH, α > ½ with β < ½ already forces a failure of the Beurling RH in their systems. So the qualitative statement "β < ½ ⇏ Beurling RH" is in the literature, **conditional on RH**.
- They state that adding primes to P cannot give α > ½ with β < ½. They also remark that an unconditional β < ½ example is hard, because for integer-defined systems "we cannot yet prove α < 1".

**How Theorem C differs.**
1. It is **unconditional**. Hardy/Selberg zeros of ζ on Re w = ½ map to Re s = (1+θ)/2, and any off-line ζ-zeros map further right. The system is not built on (P,N) as a template; it rescales via the points p^{k/(1−θ)}, uses Witt/necklace exponents, and rounds at random independently over rational p.
2. The parameter region is new even compared with the conditional results. Take θ = β ∈ (1/3,½) and α ≥ (1+θ)/2. BDR need β ≥ 2α/(α+2) = 2(1+θ)/(5+θ) at α = (1+θ)/2, and this is > ½ for θ > 1/3. So no (α,β) pair of Theorem C lies in BDR's Thm 1.3 region.
3. Theorem C gives the zero set exactly (an affine image of the zeros of ζ), not just an exponent.

## Other items checked
- Hilberdink, "Well-behaved Beurling primes and integers" (J. Number Theory 2005): every discrete system has max{α,β} ≥ ½. This is consistent with Theorem C (α ≥ (1+θ)/2 > ½).
- Hilberdink–Neamah, "Some examples of discrete and continuous Beurling prime systems" (ResearchGate 363100564, 2022), and "Examples of Beurling prime systems" (Math. Slovaca 67(2), 2017). These pose the [α,β] existence problems that Broucke–Vindas arXiv:2102.08478 (Math. Z. 307 (2024) 62) answered. Nothing with β < ½ is unconditional.
- Broucke, "On zero-density estimates for Beurling zeta functions", arXiv:2409.10051: optimality of α > (1+θ)/2 only for θ > ½ (already in the local corpus). Révész arXiv:2207.00665, arXiv:2211.08716, and Broucke–Debruyne–Vindas arXiv:2004.11501 (Adv. Math. 370) contain no discrete example with β < ½.
- Diamond–Zhang, *Beurling Generalized Numbers* (AMS SURV 213), Ch. 17 "Optimality of the dlVP remainder term". Its sections are "discrete random approximation", "g-primes satisfying RH" and "large oscillation". These concern prime-side optimality and the DMV method (integer error ≥ x^{½}). I only saw the table of contents; the full text was not accessed.
- Generic searches ("discrete Beurling N(x)=x+O(x^θ) θ<½ zeros", "[α,β]-systems β<½ unconditional 2025/2026") found no 2025–2026 paper with an unconditional β < ½ construction. arXiv:2602.21616 is unrelated (frames). Hilberdink–Lapidus (math/0410270, fractal strings) is not relevant to β < ½.

## Recommended wording for any write-up
"First unconditional discrete [α,β]-systems with β < ½ (β ∈ (1/3,½), up to ε), and first examples of any kind, conditional or not, in the region β < 2α/(α+2). Cf. Broucke–Debruyne–Révész arXiv:2309.01567 Thm 1.3, which is conditional on RH." Cite BDR §5's remark that discrete examples must be built "right from the start". Keep the audit pass's ε-caveat (θ′ = θ + ε).

Residual: a full-text check of Diamond–Zhang §17 and of the works citing 2309.01567 (Google Scholar) before submission.
