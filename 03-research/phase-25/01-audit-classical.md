# Phase 25-A — Systematic Literature Audit: Fifteen Mechanisms

For each mechanism: who studied it, what is known, why it fails for a lower bound on bⱼ,
what would be required. Format: Literature / Analysis / RH Relevance / Verdict.

---

## Mechanism 1: Korobov–Vinogradov zero-free region

**Literature.** Vinogradov (1958), Korobov (1958), Richert (1967), Ford (2002):
$$\text{No zero of }\zeta\text{ with }\Re(s) > 1 - \frac{c}{(\log|t|)^{2/3}(\log\log|t|)^{1/3}}.$$

**Analysis.** This gives bⱼ ≤ 1/2 − c/(log γⱼ)^{2/3} — an **upper** bound.
No lower bound on bⱼ is contained in or derivable from this region.
The region describes how close zeros can approach Re(s)=1, not how far they must be from Re(s)=1/2.

**RH Relevance.** None for a lower bound on bⱼ.

**Verdict.** Dead end (wrong direction). ✓ known.

---

## Mechanism 2: Selberg density theorem

**Literature.** Selberg (1946), Ingham (1940), Huxley (1972), Montgomery (1971), Jutila (1977):
$$N(\sigma, T) \ll T^{A(1-\sigma)}(\log T)^B, \quad A \leq 12/5 \text{ (best known)}.$$

**Analysis.** N(σ,T) counts zeros with Re(ρ) ≥ σ, not individual displacements. It says off-line zeros are rare (exponentially rare as σ→1) but does not force any individual bⱼ ≥ F(γⱼ). A single zero with bⱼ = e^{-10^{100}} is compatible with all density theorems.

**RH Relevance.** None for individual bⱼ lower bound.

**Verdict.** Dead end. ✓ known.

---

## Mechanism 3: Levinson-Conrey zero-on-line proportion

**Literature.** Hardy (1914): infinitely many zeros on line. Hardy-Littlewood (1921): N₀(T) ~ T log T. Selberg (1942): N₀(T) ≫ T log T. Levinson (1974): ≥ 1/3. Conrey (1989): ≥ 2/5. Bui-Conrey-Young (2011): ≥ 41%.

**Analysis.** These results bound the proportion of zeros ON the line. They say nothing about the displacement of zeros that are OFF the line.

**RH Relevance.** None for a lower bound on bⱼ.

**Verdict.** Dead end. ✓ known.

---

## Mechanism 4: Deuring-Heilbronn zero repulsion

**Literature.** Deuring (1933), Heilbronn (1934): for L-functions of real characters, if β₁ = 1-δ is a Siegel zero, then all other real zeros β₂ satisfy β₂ ≤ 1 - c/(δ log q). Bombieri (1965): repulsion lemma. Linnik (1944): repulsion from the 1-line.

**Analysis.** This repulsion concerns zeros near Re(s)=1 (Siegel zeros). No analogue is known for zeros near Re(s)=1/2. The repulsion mechanism is powered by the Euler product structure near Re(s)=1, and the Paley-Wiener barrier (Phases 22-23) shows this machinery does not reach into Re(s)∈(1/2,1). There is no known "anti-Siegel" repulsion away from the critical line.

**RH Relevance.** None for a lower bound on bⱼ.

**Verdict.** Dead end (wrong spectral region). ✓ known.

---

## Mechanism 5: Weil explicit formula / Guinand-Weil positivity

**Literature.** Weil (1952): RH ⟺ W(f*f̃) ≥ 0. Bombieri (1990): survey. Burnol (2001, 2004): adelic scattering. Li (1997): λ_n > 0 criterion.

**Analysis.** The Weil positivity criterion is equivalent to RH. Our program (PLAN-RH-MAXIMAL.md) established:
- Forced negativity (Link A): IF bⱼ > 0, THEN λ_min(Q_X) ≤ -c(σ,J)·bⱼ². This gives bⱼ² ≤ |λ_min|/c — an **upper** bound on bⱼ from |λ_min(Q)|.
- For a lower bound on bⱼ we would need λ_min(Q_X) ≤ -F for some F independent of bⱼ. This would come from an unconditional lower bound on the negativity of Q, which is RH-equivalent (LB).

**RH Relevance.** Wall W4-RSRP: the fundamental obstacle is proving (LB). No lower bound on bⱼ emerges without (LB).

**Verdict.** Known wall (W4-RSRP / (LB)). This is the program's main wall. ✓ named.

---

## Mechanism 6: de Branges canonical systems / chain condition

**Literature.** de Branges (1961, 1968): Hilbert spaces of entire functions H(E). de Branges (1986, 1992, 2005): claimed proofs of RH via chain conditions (not accepted). Dym-McKean (1976): canonical systems. Remling (2011): inverse spectral theory.

**Analysis.** de Branges spaces H(E) have a "chain condition": H(E₁) ⊂ H(E₂) iff the inclusions are isometric. RH would follow if the de Branges spaces associated to ξ form a canonical chain. The chain condition is a QUALITATIVE binary condition. It does not quantify the displacement bⱼ for off-line zeros. No version of the de Branges approach produces a lower bound on bⱼ.

What would be needed: a quantitative version of the chain condition that gives a measure of "how much" the chain fails, with that measure being ≥ f(bⱼ). No such quantitative version exists.

**RH Relevance.** Structural direction (Phase 3 of PLAN-RH-MAXIMAL.md), but does not address bⱼ lower bounds.

**Verdict.** Known wall (structural, not bⱼ-quantitative). ✓ named.

---

## Mechanism 7: Beurling-Nyman criterion

**Literature.** Beurling (1955), Nyman (1950), Báez-Duarte (2003, 2005), Burnol (2003): RH ⟺ d = 0 where d = inf_{f ∈ K} ‖1_{[0,1]} − f‖_L²(0,1).

**Analysis.** The criterion is a reformulation of RH, not a proof strategy. Under Hypothesis D, d > 0. Can one bound d from below in terms of bⱼ? In principle yes (d ≥ something depending on bⱼ), but this would just be ANOTHER formulation of the same problem, not a proof of bⱼ ≥ F(γⱼ).

**RH Relevance.** Circular: bounding d from below is equivalent to lower-bounding bⱼ.

**Verdict.** Dead end (circular reformulation). ✓ known.

---

## Mechanism 8: Selberg trace formula / spectral interpretation

**Literature.** Selberg (1956): trace formula for compact Riemann surfaces. Patterson (1975), Hejhal (1976): Selberg zeta function Z_Γ(s). Ihara (1966): p-adic analogues. Connes (1996, 1999): adelic trace formula.

**Analysis.** The Selberg zeta function Z_Γ(s) for arithmetic groups has all zeros on Re(s)=1/2 because they are eigenvalues of the Laplacian (self-adjoint). This is RH for Z_Γ. However, this is a DIFFERENT function from the Riemann ζ. There is no known spectral realization of the Riemann zeta function (Hilbert-Pólya problem).

If a spectral realization existed, it would give all zeros on the line (qualitatively), not a lower bound on bⱼ.

**RH Relevance.** Structural direction (Hilbert-Pólya / Connes program), but even if successful it would give qualitative RH, not a lower bound on bⱼ.

**Verdict.** Known wall (Hilbert-Pólya spectral realization). ✓ named.

---

## Mechanism 9: Bohr almost-periodicity

**Literature.** Bohr (1914-1921): Dirichlet series almost-periodic for Re(s) > σ_a. Kronecker (1884): simultaneous approximation of log p by rationals.

**Analysis.** For Re(s) > 1/2, ζ(s) is almost periodic (in Bohr's sense). If ζ(ρⱼ) = 0 with Re(ρⱼ) = σⱼ > 1/2, then by almost-periodicity there exist arbitrarily large T such that ζ(σⱼ + i(γⱼ+T)) ≈ 0. This shows the zero "reappears" approximately. But it gives no lower bound on bⱼ — it is valid for ANY bⱼ > 0.

**RH Relevance.** None for a lower bound on bⱼ.

**Verdict.** Dead end. ✓ known.

---

## Mechanism 10: Baker's theorem / linear forms in logarithms

**Literature.** Baker (1966, 1975): |β₀ + β₁ log α₁ + … + βₙ log αₙ| ≥ exp(−C(n)B^n log A₁…Aₙ log B) for non-zero linear forms, with αᵢ algebraic and βᵢ integers.

**Analysis.** Baker's theorem gives lower bounds for linear forms in logarithms of ALGEBRAIC numbers. The zeros of ζ are transcendental (presumably), and their imaginary parts γⱼ are not known to have any algebraic structure. Baker's method does not apply to transcendental quantities in general. Even if applied, Baker-type bounds give lower bounds for NONZERO linear combinations, which is the wrong kind of lower bound.

**RH Relevance.** None.

**Verdict.** Dead end (wrong category of objects). ✓ new diagnosis.

---

## Mechanism 11: Arithmetic geometry / Weil-Deligne for function fields

**Literature.** Weil (1948): RH for curves over finite fields. Deligne (1974): Weil conjectures (Riemann hypothesis for varieties). Proof uses: Lefschetz trace formula, Poincaré duality, hard Lefschetz, Hodge index theorem.

**Analysis.** For curves C over F_q, ζ_C(s) has zeros on Re(s)=1/2 because the proof uses intersection theory on the surface C×C (specifically the Castelnuovo-Severi inequality). The proof is QUALITATIVE (all zeros exactly on the line), not quantitative in bⱼ. There is no analogue for number fields that would give bⱼ ≥ F(γⱼ). The function field proof requires the FINITENESS of F_q, which has no analogue over ℤ.

**RH Relevance.** Deep structural template but no quantitative consequence for bⱼ.

**Verdict.** Known wall (function field ↔ number field gap). ✓ named.

---

## Mechanism 12: Turán power sum method

**Literature.** Turán (1948, 1953): power sum method; if ∑ bₙzₙᵏ ≠ 0 for many k, then the bₙ are "large." Turán-Montgomery lemma.

**Analysis.** Turán's method gives a lower bound for the maximum of a Dirichlet polynomial over a range. Applied to ζ, it gives statements like: if ζ(s) is small on a region, then a certain prime sum is large. This produces omega theorems (lower bounds for ψ(x)-x), not lower bounds for bⱼ.

**RH Relevance.** None for a lower bound on bⱼ.

**Verdict.** Dead end (gives omega theorems, not bⱼ bounds). ✓ known.

---

## Mechanism 13: Littlewood omega theorems

**Literature.** Littlewood (1914): ψ(x)−x = Ω±(x^{1/2} log log log x). Ingham (1936): ψ(x)−x = Ω±(x^{σ₀-ε}) if ζ has a zero with Re(ρ)=σ₀.

**Analysis.** Ingham's omega theorem says: IF bⱼ > 0, THEN |ψ(x)−x| = Ω(x^{1/2+bⱼ-ε}). Combined with KV upper bound |ψ(x)−x| ≤ x·exp(−c(log x)^{3/5}):

The omega term x^{1/2+bⱼ-ε} is COMPATIBLE with the KV bound since for bⱼ ∈ (0,1/2):
$$x^{1/2+b_j-\varepsilon} \ll x^{1-\varepsilon} \ll xe^{-c(\log x)^{3/5}}$$
for all large x (since x^{-\varepsilon} ≫ e^{-c(\log x)^{3/5}}). No contradiction, no lower bound on bⱼ.

**RH Relevance.** Phase 22 already established this compatibility (Theorem 22-B.3 / 23-B). ✓ confirmed.

**Verdict.** Known wall. ✓ confirmed.

---

## Mechanism 14: Large sieve and exponential sums

**Literature.** Montgomery (1971), Gallagher (1967): large sieve inequality ∑_q∑_{χ mod q}|∑_n a_n χ(n)|² ≤ (Q²+N)‖a‖². van der Corput (1921), Weyl (1916): exponential sum bounds.

**Analysis.** The large sieve gives density results on zeros (N(σ,T) bounds). Exponential sum methods underlie KV. Neither gives lower bounds on individual bⱼ — they all bound COUNTS or AVERAGES, not individual displacements.

**RH Relevance.** None for a lower bound on bⱼ.

**Verdict.** Dead end. ✓ known.

---

## Mechanism 15: Montgomery pair correlation / GUE statistics

**Literature.** Montgomery (1973): pair correlation of zeros on the critical line conjectured to be 1−(sin πx/πx)². Hejhal (1994), Odlyzko (1987): numerical evidence. Rudnick-Sarnak (1996): n-level correlations. Keating-Snaith (2000): moments via random matrices.

**Analysis.** The pair correlation describes spacings between zeros ON the critical line. It has been partially proved by Montgomery (1973) for certain test functions. Off-line zeros ρⱼ do not appear in the pair correlation of on-line zeros. Could an off-line zero distort the pair correlation of nearby on-line zeros? In principle yes (there might be a "repulsion" term in the correlation function), but no theorem of this form is known. This would be a new result (not classical).

**RH Relevance.** Potentially interesting (new direction), but: (a) pair correlation results are currently only conditional on GRH; (b) even if proved, they would give information about ON-LINE zero distribution, not a lower bound on bⱼ.

**Verdict.** Dead end for bⱼ lower bounds. Pair correlation ≠ off-line displacement. ✓ new diagnosis.

---

## Summary of the audit

| Mechanism | Direction for bⱼ | Status |
|-----------|-----------------|--------|
| KV zero-free region | Upper bound only | Dead end |
| Density theorems | Statistical, not individual | Dead end |
| Levinson-Conrey | On-line proportion, not bⱼ | Dead end |
| Deuring-Heilbronn | Near Re(s)=1, wrong region | Dead end |
| Weil positivity | Fundamental wall W4-RSRP | Known wall |
| de Branges | Qualitative only | Known wall |
| Beurling-Nyman | Circular reformulation | Dead end |
| Selberg trace / Hilbert-Pólya | Spectral interpretation needed | Known wall |
| Bohr almost-periodicity | No bⱼ information | Dead end |
| Baker's theorem | Wrong category | Dead end |
| Weil-Deligne (function fields) | Qualitative, no number field analogue | Known wall |
| Turán method | Omega theorems, not bⱼ bounds | Dead end |
| Littlewood omega | Compatible with any bⱼ < 1/2 | Known wall |
| Large sieve / exponential sums | Count/average bounds | Dead end |
| Montgomery pair correlation | On-line statistics, not bⱼ | Dead end |

**Conclusion**: No classical or near-classical mechanism produces a lower bound on bⱼ. The audit is exhaustive at the level of known tools.

Two new structural observations emerge from this audit and deserve further development:
1. The de Bruijn–Newman connection (Mechanism 16, Phase 25-B).
2. The Kreĭn–Langer + Laguerre–Pólya class structure (Phase 25-C).
