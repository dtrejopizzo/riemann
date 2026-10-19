# S3: analytic number theory and Fourier analysis around positivity (survey of )

Scope: BRIEF.md, domain S3. Sources: the arXiv API (it rate-limits after about 15 queries) and OpenAlex (30 queries), plus abstracts of the most relevant items.
Index checked before writing: 05_LITERATURE (L01–L68), 05b (L69–L85), AUDIT_B, AUDIT_PHASE193, README (BARRIER_001, INV_*), 04_PHASES (Hamburger R162_2601c, Broucke ζ_θ R163_101, Thm O).
 Row D is treated as its own target.

Labels: P = PROVED (refereed), P* = PROVED (preprint), C = CONDITIONAL, H = HEURISTIC/numerical.
The "missing-object" properties are the BRIEF's 1–4: (1) the object reads the actual values of Λ; (2) it couples small primes with the global FE; (3) it is not linear, not a cone, not a certificate, not an identity; (4) it carries a built-in positivity.

## (c) Ranked possible missing objects (honest verdicts)

None of the items scanned has all four properties. Ranked by how close they come:

1. **Rankin–Selberg / "positivity of prime terms" explicit-formula method.** Sources: S. D. Miller, "The highest-lowest zero and other applications of positivity" (Duke 2002, math/0112196); Chenevier–Lannes and Chenevier–Taïbi (1802.05066, 1907.08783, Lachaussée 2011.08237); Odlyzko–Poitou–Serre discriminant bounds; Pierre 2410.12922 (conductors); Trudgian et al. 2610.16010; Omar 2002.
   - *Mechanism:* pick a test g ≥ 0 with ĝ ≥ 0. The prime side of the explicit formula is Σ Λ_{π×π̄}(n) g(log n) ≥ 0, because Rankin–Selberg coefficients are nonnegative. This leaves inequalities between the archimedean term and the zeros. The prime values enter only through their sign.
   - *Properties:* it fails (1), because nonnegative Beurling systems satisfy the same inequalities. It fails (2), because everything is linear in Λ. It has (4).
   - *Index status:* KNOWN. AUDIT_B §2 (Delsarte/OPS LP), PHASE193 row 76 (Cohn–Elkies, Odlyzko direction), dlVP cap in phase 151.
   - *Structural note:* the direction is the opposite of row D. Row D needs a lower bound on archimedean minus comb. The OPS method bounds archimedean versus zeros after dropping the comb. Dropping the comb is free for row D only where the comb is ≤ 0 on the test, and on 𝒫_T it is not.
   - *Possible first theorem (low value, recorded so it is not lost):* a "Rankin–Selberg window lemma". Its content is the triangle/Schur pairing for c_F of the twisted ζ(s+iα)ζ(s−iα)ζ(s)² family, the 3-4-1 analogue on 𝒫_T. This is already capped (dlVP, phase 151). Do not retry without a new reason.
2. **Selberg-class rigidity.** Sources: Kaczorowski–Perelli (structure IV, Cramér applications, degree <2); Soundararajan "Strong multiplicity one for the Selberg class" (2004); Dobner 2005.05142 (Newman for the extended Selberg class).
   - *Properties:* it has (1) and (2). The coefficients and the FE are used non-linearly through the classification of degree-1 functions and the Hamburger theorem. It fails (4): there is no sign.
   - *Index status:* KNOWN. Hamburger rigidity R162_2601c, Thm O R163_1001, BARRIER_D1_001, W3′.
   - *Dobner:* his result needs no information about the zeros. It gives Λ_dBN ≥ 0, which is the opposite direction (L21).
3. **Fourier interpolation with zeros of ζ.** Sources: Bondarenko–Radchenko–Seip 2005.02996; Lysen 2509.17600; KNS-type uniqueness pairs.
   - *Mechanism:* a duality between interpolation bases and Dirichlet-series kernels that satisfy an FE, with coefficients coming from modular integrals of the theta group.
   - *Properties:* it has (2). The global FE is used non-locally, through Knopp abundance. It fails (1) and (4). The zeros are inputs, not outputs.
   - *Index status:* KNOWN (L30, AUDIT_B Theorems B use the BRS nodes).
4. **de Branges / RKHS Fourier optimization.** Sources: Carneiro et al. 2109.10844 and 2408.01186 (sign uncertainty with de Branges spaces); Carneiro–Milinovich–Soundararajan pair correlation 2310.01913; Quesada-Herrera 2411.05095; Chirre 2005.02393 (SDP primes in APs).
   - *Mechanism:* extremizers come from reproducing kernels of the de Branges space attached to a symmetry type.
   - *Properties:* the constraints are linear on the zero side, and the objects are dual certificates (thm:Z). They fail (1)–(3).
   - *Index status:* KNOWN (L53–L54, PHASE193 row 78). Verdict: KNOWN.
5. **Integer-mass Fourier quasicrystals as Lee–Yang sections.** Source: Wei 2610.10652 (2026, P*). Every positive-integer-mass FQ is a real section of an effective Lee–Yang cycle, and the section matrix has positive maximal minors.
   - *Properties:* this is a built-in positivity (4) driven by integrality. However, the explicit-formula pair (zeros, Λ-comb) is not a positive measure on both sides, so the theorem does not apply. Integrality sits under W3′ (integer-frequency blindness).
   - *Index status:* KNOWN family (L30, L60, Kurasov–Sarnak). The specific paper is NOT IN INDEX.
   - *Verdict:* KNOWN (family). Low value. Worth one line in 05b.

Verdict: **no NEW-CANDIDATE** in S3. One gap is structural. Every positivity result in this domain that uses prime values does so either through their sign (Rankin–Selberg) or through rigidity with no sign (Selberg class). No item combines the two. That combination is exactly properties (1)+(2)+(4), and the literature does not supply it.

## (b) Deep-read notes (abstract or full-text level)

- **Rodgers–Tao 1801.05914 (P); Polymath15 1904.12438 (P); Platt–Trudgian (P); 2610.12803 (C, Λ≤0.1396); Planat 2609.37164, 2610.18214 (P*, certified barriers).** The heat-flow dynamics of zeros is comb-blind: everything happens on the ξ side. KNOWN (L21, L51).
- **GORZ 1902.07321 (P), 1910.01227; Farmer 2008.07206 ("not a plausible route"); Banerjee 2609.14295 (Jensen–Pólya survey 2026); Liu–Mao (L75).** Hyperbolicity is proved only for large n or d. The Taylor coefficients of ξ do not read Λ locally. KNOWN (L22, L50, L75).
- **Michalowski 2602.20313 (PF order 5 fails).** KNOWN (L49).
- **Kurasov–Sarnak 2004.05678; Olevskii–Ulanovskii 2009.12810; Gonçalves 2312.11185 (classification of summation formulas via Hermite–Biehler/de Branges); Vedana 2608.10121 (strip); Favorov series; Alon–Kummer–Kurasov–Vinzant.** These require positive or discrete measures on both sides. The ζ explicit formula has a signed comb. KNOWN (L30, L60).
- **Gonçalves–Oliveira e Silva–Ramos 2003.10771; Cohn–Gonçalves 2210.01684 (low-degree); Lee 2608.15415 (quasimodular A_+(d) bound, 2026); Carneiro 2006.00959, 2408.01186.** Sign uncertainty bounds a radius, not a quadratic form. KNOWN (PHASE193 row 78).
- **Miller math/0112196 (P, Duke).** Rankin–Selberg nonnegativity plus the explicit formula forces a low zero below a universal height for every L-function. This is the most "prime-sign + FE" result found, but it uses the sign only. See (c) item 1.
- **Chenevier 1802.05066 (P, automorphic Hermite–Minkowski), 1907.08783.** The explicit formula for π×π' with nonnegative prime terms. Positivity is quadratic in the family (π⊗π̄), not in Λ_ζ. For ζ alone the family is {1}, so the method collapses to the OPS LP.
- **Zhang, "Beurling primes with RH and with large oscillation" (Math. Ann. 2006); Diamond–Montgomery–Vorhauer (Math. Ann. 2005); Broucke 2409.10051 and zero-density work (2023, 2025); Révész 2202.01837, 2209.01689 (Carlson-type zero density); Pintz 2025; Hilberdink.**
  - Beurling systems with RH exist (Zhang). Beurling systems with zeros arbitrarily close to σ=1 also exist (DMV).
  - Both kinds share the same smooth counting properties. So any criterion that reads only regularity or density of the comb cannot decide row D.
  - This re-confirms the falsifier class (A8, F3:ζ_θ). KNOWN.
- **Kaczorowski–Perelli (2002 IV, Cramér); Soundararajan SMO 2004.** See (c) item 2. KNOWN.
- **BRS 2005.02996; Lysen 2509.17600.** See (c) item 3.
- **Carneiro et al. 2109.10844, 2310.01913, 2404.08380; Quesada-Herrera 2411.05095; Chirre 2602.06199.** Fourier optimization under GRH for prime gaps, PAC and least non-residue. All of it is conditional, on the zero side, and in the opposite direction.
- **Alpöge–Furman, Lamzouri, Pratt et al. (mollifiers 2508.11108).** Proportions come from a quadratic form plus a mollifier. They read Λ only through mean values, so they are comb-generic in the main term. KNOWN (L52, L62).
- **Connes math/0703392; Booker 1308.3067 ("L-functions as distributions"); Morán Ledezma 2311.08519; R. Meyer math/0311468; Shi 2609.04908.** Reformulations. KNOWN (L05, L58, L15).
- **Sibisi 0810.4820; Burnol 2002 (lower bound in NB approximation).** KNOWN (L11, L18).

## (a) Scanned items (455 unique titles; the table is unfiltered and includes off-topic search hits, which are IRRELEVANT)

| link | year | first author | title |
|---|---|---|---|
| arXiv: |  |  |  |
| https://doi.org/10.24033/ast.639 | 2018 | Kazuya Katô | $p$-adic Hodge theory and values of zeta functions of modular forms |
| https://openalex.org/W7132081422 | 2024 | Yakup Çetin | 2014-2023 YILLARI ARASINDA TÜRKİYE'DE KONUT ÜRETİMİNİN KONUT SAHİPLİĞİNE ETKİSİNİN İNCELENMESİ |
| arXiv:1206.6973v1 | 2012 | Vincent Brugidou | A 2-variable power series approach to the Riemann hypothesis |
| arXiv:2610.18214v1 | 2026 | Michel Planat | A certified classical-strip comparison for the de Bruijn-Newman constant |
| https://doi.org/10.48550/arxiv.2606.29615 | 2026 | Sofia de la Cerda | A Characterization of the Cumulants as Continuous Moment-Based Statistics |
| arXiv:2312.11185v3 | 2023 | Felipe Gonçalves | A classification of Fourier summation formulas and crystalline measures |
| https://doi.org/10.1007/s00365-026-09793-0 | 2026 | Felipe Gonçalves | A Classification of Fourier Summation Formulas and Crystalline Measures |
| https://doi.org/10.48550/arxiv.2504.02741 | 2025 | Gonçalves, Felipe | A Complete Classification of Fourier Summation Formulas on the real line |
| arXiv:math/0509468v1 | 2005 | S. Gerhold | A Computer Proof of Turan's Inequality |
| arXiv:2610.12803v1 | 2026 | Cetin Hakimoglu-Brown | A conditional bound $Λ\le0.13963$ for the de Bruijn--Newman constant |
| https://doi.org/10.48550/arxiv.2501.03970 | 2025 | Marcus Appleby | A Constructive Approach to Zauner's Conjecture via the Stark Conjectures |
| arXiv:2312.00459v2 | 2023 | Franklin H. Cho | A continuous-wave and pulsed X-band electron spin resonance spectrometer operating in ultra-high vacuum for the study of low dimensional spin ensembles |
| https://doi.org/10.4171/cmh/202 | 2010 | Jerzy Kaczorowski | A converse theorem for Dirichlet $L$-functions |
| https://doi.org/10.48550/arxiv.2306.02872 | 2023 | Creech, Steven | A converse theorem in half-integral weight |
| https://doi.org/10.5281/zenodo.21945295 | 2026 | Akihiro Koide | A Counterexample to an Off-Axis Wiener Criterion for the Laguerre–Pólya Class and a Corrected Jensen Correlation Kernel |
| https://doi.org/10.5281/zenodo.19025598 | 2026 | Ulrich Tehrani | A Curvature Decomposition of the Explicit Formula for the Riemann Zeta Function |
| https://doi.org/10.48550/arxiv.2605.03679 | 2026 | Torgeir Keun Lysen | A discrete Hardy uncertainty principle |
| arXiv:2505.14947v1 | 2025 | Tianhong Zhao | A finite dimensional trace formula |
| https://doi.org/10.1090/s0002-9939-2010-10546-4 | 2010 | Pei-Chu Hu | A formula for the discriminant of number fields |
| https://doi.org/10.1017/s0004972708000300 | 2008 | A. Javtokas | A JOINT UNIVERSALITY THEOREM FOR PERIODIC HURWITZ ZETA-FUNCTIONS |
| https://doi.org/10.1006/aima.2001.2066 | 2002 | Jean-François Burnol | A Lower Bound in an Approximation Problem Involving the Zeros of the Riemann Zeta Function |
| https://doi.org/10.5281/zenodo.18510860 | 2026 | Carlos Alberto Terêncio de Bastos | A Mirror-Global-Period Approach to the Weil Criterion for the Riemann Zeta Function |
| https://doi.org/10.5802/aif.3600 | 2023 | Takis Konstantopoulos | A new class of solutions to the van Dantzig problem, the Lee–Yang property, and the Riemann hypothesis |
| arXiv:2510.11061v1 | 2025 | A. Dudko | A new description of uniformly spread discrete sets |
| https://doi.org/10.11650/twjm/1500404572 | 2006 | Muharem Avdispahić | A NEW EXPLICIT FORMULA FOR THE FUNDAMENTAL CLASS OF FUNCTIONS |
| https://doi.org/10.48550/arxiv.1703.08194 | 2017 | Madeline Locus Dawsey | A new formula for Chebotarev densities |
| https://doi.org/10.1007/s40993-017-0093-7 | 2017 | Madeline Locus Dawsey | A new formula for Chebotarev Densities |
| https://doi.org/10.48550/arxiv.1902.00441 | 2019 | Stefan Steinerberger | A Nonlocal Functional Promoting Low-Discrepancy Point Sets |
| https://doi.org/10.7169/facm/1261157810 | 2009 | G. Monti Bragadin | A note on Hecke's functional equation and the Selberg class |
| https://doi.org/10.1090/s0002-9939-2010-10443-4 | 2010 | Hung M. Bui | A note on the gaps between consecutive zeros of the Riemann zeta-function |
| https://doi.org/10.1007/s13398-012-0094-2 | 2012 | Eric Dubon | A note on the real projection of the zeros of partial sums of Riemann zeta function |
| arXiv:2105.05386v1 | 2021 | Young-One Kim | A note on the zeros of Jensen polynomials |
| https://doi.org/10.1090/s0025-5718-08-02091-7 | 2008 | Reinier Bröker | A 𝑝-adic algorithm to compute the Hilbert class polynomial |
| arXiv:2609.38965v1 | 2026 | Bo Lin | A positive-conservative Fourier optimization method for ground states of Bose--Einstein condensates with higher-order interactions |
| arXiv:2311.08519v1 | 2023 | Ángel Alfredo Morán Ledezma | A probabilistic interpretation of Weil's explicit sums and arithmetic spectral measures |
| arXiv:2005.05142v2 | 2020 | Alexander Dobner | A proof of Newman's conjecture for the extended Selberg class |
| https://doi.org/10.6084/m9.figshare.32573832 | 2026 | Russell Grant | A Proof Program for the Riemann Hypothesis |
| https://doi.org/10.5281/zenodo.17762484 | 2025 | de Frutos, Fernando | A Quantum Dissipative Framework for the Riemann Hypothesis: Explicit-Formula Equivalence, Dirichlet-Form Positivity, and the Universal Arithmetic Laplacian |
| https://doi.org/10.1556/314.2021.00019 | 2021 | R\'ev\'esz, Szil\'ard Gy. | A Riemann-von Mangoldt-type formula for the distribution of Beurling primes |
| https://doi.org/10.1556/314.2021.00019 | 2021 | Szilárd Gy. Révész | A Riemann–von Mangoldt-Type Formula for the Distribution of Beurling Primes |
| https://doi.org/10.1016/j.jfa.2019.108292 | 2019 | Akash Anand | A solution to the Cauchy dual subnormality problem for 2-isometries |
| https://doi.org/10.48550/arxiv.1407.4216 | 2014 | Kohji Matsumoto | A survey on the theory of universality for zeta and $L$-functions |
| https://doi.org/10.5281/zenodo.20031980 | 2026 | Frank Morales | A Unified Spectral Framework for the Riemann Hypothesis and Deterministic AI Governance Arithmetic Spectral Theory, the L-EFM Proof of RH, the Discovery of Λ, and the H2E Sheri From Lossless Prime-Indexed Systems to Zero-Error Capacity and Sovereign Multimodal AI Safety |
| https://doi.org/10.48550/arxiv.2404.05186 | 2024 | Chan-Ho Kim | A user's guide to Beilinson-Kato's zeta elements |
| https://doi.org/10.1006/jmaa.2000.6971 | 2000 | Ν. H. Bingham | Abelian, Tauberian, and Mercerian Theorems for Arithmetic Sums |
| https://doi.org/10.25560/49454 | 2017 | Pedro Ascencio | Adaptive observer design for parabolic partial differential equations |
| https://doi.org/10.5281/zenodo.22812117 | 2026 | Alexandre Dumas | Adjacent-Shift Proper Position for Jensen Polynomials |
| https://doi.org/10.48550/arxiv.1904.04051 | 2019 | Christopher J. Fewster | Algebraic Quantum Field Theory -- an introduction |
| https://doi.org/10.48550/arxiv.1805.07741 | 2018 | Tatyana Preobrazhenskaya | Almost all of the zeros of the Riemann zeta-function are on the critical line |
| arXiv:2211.16856v2 | 2022 | Sergii Favorov | Almost periodic distributions and crystalline measures |
| https://doi.org/10.5281/zenodo.18916081 | 2026 | Daland Montgomery | An Admissible Test Function for the Connes Trace Formula from the Spectral Data of A_F |
| https://doi.org/10.2206/kyushujm.72.35 | 2018 | Keiju Sono | AN APPLICATION OF GENERALIZED MOLLIFIERS TO THE RIEMANN ZETA-FUNCTION |
| arXiv:1802.05066v1 | 2018 | Gaëtan Chenevier | An automorphic generalization of the Hermite-Minkowski theorem |
| https://doi.org/10.48550/arxiv.1611.10325 | 2016 | Youness Lamzouri | An effective universality theorem for the Riemann zeta function |
| arXiv:1305.2458v1 | 2013 | Zev Rosengarten | An Erdos-Turan Inequality For Compact Simply-Connected Semisimple Lie Groups |
| https://doi.org/10.48550/arxiv.1309.0055 | 2013 | George Csordás | An Exact Level-Nine Counterexample to a Theta-Derivative Turán Conjecture |
| https://doi.org/10.2140/ant.2017.11.1135 | 2017 | Jesse Thorner | An explicit bound for the least prime ideal in the Chebotarev density theorem |
| https://doi.org/10.5802/aif.3274 | 2019 | Jeoung-Hwan Ahn | An explicit upper bound for the least prime ideal in the Chebotarev density theorem |
| https://doi.org/10.1017/fms.2023.22 | 2023 | Andrew R. Booker | An extension of Venkatesh’s converse theorem to the Selberg class |
| https://doi.org/10.48550/arxiv.1608.07887 | 2016 | Dimitar K. Dimitrov | An extremal problem related to generalizations of the Nyman-Beurling and Báez-Duarte criteria |
| https://doi.org/10.5281/zenodo.19359304 | 2026 | Gregory Villines | AN IMPROVED ZERO PROPORTION BOUND FOR THE RIEMANN ZETA FUNCTION |
| https://doi.org/10.4064/aa230324-20-11 | 2024 | Frederik Broucke | An omega-result for Beurling generalized integers |
| https://doi.org/10.2139/ssrn.7337578 | 2026 | Nicholas G. Polson | An ε-Approximation of ξ(1/2 + s) |
| arXiv:2408.09563v2 | 2024 | Sergii Favorov | Analogues of Fourier quasicrystals for a strip |
| https://doi.org/10.13140/rg.2.2.28509.54247 | 2021 | Xiao‐Jun Yang | Analysis of the Riemann zeta function |
| https://doi.org/10.5167/uzh-126347 | 2016 | Patrick Kühn | Analytic theory of L-functions: explicit formulae, gaps between zeros and generative computational methods |
| https://doi.org/10.4007/annals.2013.178.2.6 | 2013 | Paolo Giulietti | Anosov flows and dynamical zeta functions |
| https://doi.org/10.48550/arxiv.1203.0904 | 2012 | Paolo Giulietti | Anosov Flows and Dynamical Zeta Functions |
| https://doi.org/10.5281/zenodo.21941904 | 2026 | Michael I Aksman | APERY PERIODS AND OPERATOR POSITIVITY ´ The Structural Equivalence of the Vorton Hessian and Weil's Explicit Functional |
| https://doi.org/10.1007/s00013-025-02140-y | 2025 | S. Favorov | Application of Meyer’s theorem on quasicrystals to exponential polynomials and Dirichlet series |
| https://doi.org/10.1090/s0002-9939-02-06542-5 | 2002 | Jerzy Kaczorowski | Applications of a theorem of H. Cramér to the Selberg class |
| arXiv:math-ph/0105010v2 | 2001 | Benji N. Fisher | Applications of Group Cohomology to the Classification of Fourier-Space Quasicrystals |
| https://openalex.org/W2523448557 | 2012 | Jingsong Chai | Archimedean Derivatives and Rankin-Selberg integrals |
| arXiv:1809.10293v1 | 2018 | Biwei Jiang | Are the silicate crystallinities of oxygen-rich evolved stars related to their mass loss rates? |
| https://doi.org/10.5281/zenodo.18408673 | 2026 | Nigel Stafford Paltoo | Arithmetic Band Structure and a Canonical Trace Formula for the Riemann Zeta Function |
| https://doi.org/10.5281/zenodo.20945166 | 2026 | Ying Ye | Arithmetic Dirac Packets, Fargues-Fontaine Slopes, and Weil Positivity: A Conditional Spectral Route Toward the Riemann Hypothesis |
| https://openalex.org/W1906541009 | 2006 | Terence Tao | Arithmetic progressions and the primes |
| https://doi.org/10.1016/j.jnt.2023.10.007 | 2023 | Giulia Cesana | Asymptotic equidistribution for partition statistics and topological invariants |
| https://doi.org/10.1017/cbo9780511542923.004 | 2009 | Dorian M. Goldfeld | Automorphic forms and L–functions forSL(2, ℤ) |
| https://doi.org/10.1090/s0894-0347-2014-00784-0 | 2014 | Wei Zhang | Automorphic period and the central value of Rankin-Selberg L-function |
| arXiv:2608.23691v2 | 2026 | Stephen Chung | Autonomous Mathematical Discovery in an Open-World Multi-Agent Environment |
| arXiv:2011.08237v2 | 2020 | Guillaume Lachaussée | Autour de l'énumération des représentations automorphes cuspidales algébriques de ${\rm GL}_n$ sur $\mathbb{Q}$ de conducteur $&gt;1$ |
| arXiv:1710.10362v1 | 2017 | Emanuel Carneiro | Bandlimited approximations and estimates for the Riemann zeta-function |
| https://doi.org/10.2139/ssrn.6992163 | 2026 | Nicholas G. Polson | Barnes Beta Distributions and the Riemann Xi Function |
| https://doi.org/10.48550/arxiv.2002.03879 | 2020 | Bogdan Ion | Bernoulli Operators and Dirichlet Series |
| https://doi.org/10.1016/j.aim.2020.107240 | 2020 | Frederik Broucke | Beurling integers with RH and large oscillation |
| https://doi.org/10.1007/s00208-005-0638-2 | 2005 | Harold George Diamond | Beurling primes with large oscillation |
| https://doi.org/10.1007/s00208-006-0051-5 | 2006 | Wen-Bin Zhang | Beurling primes with RH and Beurling primes with large oscillation |
| arXiv:2107.10611v1 | 2021 | Wayne M. Lawton | Bohr Almost Periodic Sets of Toral Type |
| https://doi.org/10.1007/s00209-021-02820-9 | 2021 | Andrés Chirre | Bounding the log-derivative of the zeta-function |
| https://doi.org/10.4064/aa106-3-2 | 2003 | Sofiène Bessassi | Bounds for the degrees of CM-fields of class number one |
| https://doi.org/10.48550/arxiv.1508.07682 | 2015 | David Zywina | Bounds for the Lang-Trotter conjectures |
| https://doi.org/10.1090/s0025-5718-01-01373-4 | 2001 | Ana-Cecilia de la Maza | Bounds for the smallest norm in an ideal class |
| https://doi.org/10.1007/s00365-026-09787-y | 2026 | Antonio J. Durán | Brenke Polynomials with Real Zeros and the Riemann Hypothesis |
| https://doi.org/10.4310/cms.2016.v14.n1.a5 | 2015 | Houman Owhadi | Brittleness of Bayesian inference and new Selberg formulas |
| https://doi.org/10.1007/jhep10(2020)138 | 2020 | Cynthia A Keeler | BTZ one-loop determinants via the Selberg zeta function for general spin |
| https://doi.org/10.5281/zenodo.22050466 | 2026 | Axel Abdel Rahamane MEGHEZZI | Certified Finite-Support Weil Positivity Across the First Prime-Power Threshold |
| https://doi.org/10.48550/arxiv.2609.23108 | 2026 | Jake Langham | Channel confinement mollifies roll wave instabilities |
| arXiv:2609.16111v1 | 2026 | Lorenz Eberhardt | Classification of c=1 CFTs |
| arXiv:2608.10121v2 | 2026 | Guilherme Vedana | Classification of Fourier summation formulas on a horizontal strip |
| https://openalex.org/W1544917614 | 2016 | Thomas Oliver | Classification of Low Degree L-Data |
| https://doi.org/10.2140/ent.2025.4.217 | 2025 | Mathilde Gerbelli-Gauthier | Cohomology of Fuchsian groups and Fourier interpolation |
| arXiv:2609.37164v2 | 2026 | Michel Planat | Collective Contraction in the de Bruijn--Newman Heat Flow: Off-Zero Logarithmic Derivatives and Certified Barrier Refinements |
| https://openalex.org/W2823506231 | 2018 | Gregory Debruyne | Complex Tauberian theorems and applications to Beurling generalized primes |
| https://doi.org/10.1016/s0377-0427(00)00336-8 | 2000 | Jonathan Michael Borwein | Computational strategies for the Riemann zeta function |
| https://doi.org/10.21914/anziamj.v46i0.940 | 2005 | D. H. Klein | Computational studies of the shear flow behaviour of a model for nematic liquid crystalline polymers |
| https://doi.org/10.1090/s0025-5718-2010-02373-7 | 2010 | Andrew V. Sutherland | Computing Hilbert class polynomials with the Chinese remainder theorem |
| arXiv:1305.0035v1 | 2013 | Karim Belabas | Computing the residue of the Dedekind zeta function |
| https://doi.org/10.48550/arxiv.2410.22711 | 2024 | Neea Palojärvi | Conditional estimates for $L$-functions in the Selberg class II |
| https://doi.org/10.1112/blms.70360 | 2026 | Tianyu Zhao | Conditional estimates on the argument of Dirichlet L‐functions with applications to low‐lying zeros |
| https://doi.org/10.1016/j.jnt.2011.10.001 | 2011 | Marco Adamo Seveso | Congruences and rationality of Stark–Heegner points |
| arXiv:2609.04908v1 | 2026 | Yaoming Shi | Construction of Finite Hilbert--Pólya Matrices from Weil's Explicit Formula |
| https://doi.org/10.1007/s40993-019-0181-y | 2019 | Tadashi Miyazaki | Converse theorems for automorphic distributions and Maass forms of level N |
| https://doi.org/10.4310/pamq.2005.v1.n2.a6 | 2005 | James Cogdell | Converse Theorems, Functoriality, and Applications |
| https://doi.org/10.4310/mrl.2018.v25.n4.a5 | 2018 | Evan P. Dummit | Counting $G$-extensions by discriminant |
| https://doi.org/10.5802/jtnb.492 | 2008 | Christian Röttger | Counting invertible matrices and uniform distribution |
| arXiv:2509.17600v2 | 2025 | Torgeir Keun Lysen | Critical and asymmetric Fourier uniqueness pairs |
| https://doi.org/10.48550/arxiv.1105.1177 | 2011 | J. Brian Conrey | Critical zeros of Dirichlet $L$-functions |
| https://doi.org/10.48550/arxiv.1607.03288 | 2016 | J. Brian Conrey | Critical zeros of lacunary L-functions |
| https://doi.org/10.48550/arxiv.1410.2433 | 2014 | Hung M. Bui | Critical zeros of the Riemann zeta-function |
| https://doi.org/10.5281/zenodo.23070556 | 2026 | Pedro Caceres | Cross-Energy of Dirichlet Partial Sums PART VII: Weil Positivity as a Prime Cross-Energy |
| https://doi.org/10.2172/1233245 | 2015 | Los Alamos National Lab. (LANL), Los Alamos, NM (United States) | Crystalline and Crystalline International Disposal Activities |
| https://doi.org/10.5565/publmat6712310 | 2022 | Yves Meyer | Crystalline measures in two dimensions |
| https://doi.org/10.3934/dcds.2022160 | 2022 | Mi-Ho Giga | Crystalline surface diffusion flow for graph-like curves |
| https://openalex.org/W4415935442 | 2025 | Jérémy Dousselin | Cubic fields, mollifying method and class number |
| https://doi.org/10.5281/zenodo.20544075 | 2026 | Sterling Dudley Hayden | Degree-4 Jensen Polynomials of the Riemann Xi Function Are Hyperbolic |
| arXiv:0810.4820v1 | 2008 | Sibusiso Sibisi | Densities, Laplace Transforms and Analytic Number Theory |
| https://doi.org/10.48550/arxiv.2306.07475 | 2023 | Anshul Adve | Density criteria for Fourier uniqueness phenomena in $\mathbf{R}^d$ |
| https://doi.org/10.1112/mtk.12156 | 2022 | Szilárd Gy. Révész | Density estimates for the zeros of the Beurling ζ function in the critical strip |
| https://doi.org/10.48550/arxiv.2603.17334 | 2026 | Tianyu Zhao | Density results for $r$-gaps between zeros of the Riemann zeta-function |
| arXiv:2405.01907v1 | 2024 | Paolo Boggiatto | Detecting quasicrystals with quadratic time-frequency distributions |
| arXiv:math/0204098v1 | 2002 | Ilia Krasikov | Dicrete Analogues of the Laguerre Inequality |
| https://doi.org/10.2422/2036-2145.2006.4.06 | 2009 | Andrea Bonfiglioli | Dirichlet problem with Lp-boundary data in contractible domains of Carnot groups |
| https://doi.org/10.48550/arxiv.2605.23079 | 2026 | Torgeir Keun Lysen | Discrete Pauli pairs |
| arXiv:1907.08783v1 | 2019 | Gaëtan Chenevier | Discrete series multiplicities for classical groups over Z and level 1 algebraic cusp forms |
| https://doi.org/10.1016/j.jat.2014.03.006 | 2014 | Eugenijus Buivydas | Discrete universality theorems for the Hurwitz zeta-function |
| https://doi.org/10.48550/arxiv.2012.09045 | 2020 | Szilárd Gy. Révész | Distribution of Beurling primes and zeroes of the Beurling zeta function I. Distribution of the zeroes of the zeta function of Beurling |
| arXiv:1904.12438v2 | 2019 | D. H. J. Polymath | Effective approximation of heat flow evolution of the Riemann $ξ$ function, and a new upper bound for the de Bruijn-Newman constant |
| https://doi.org/10.56725/instemm.v1is1.23 | 2022 | Yang‐Hui He | Eigenvalue Density, Li's Positivity, and the Critical Strip |
| arXiv:2303.03201v3 | 2023 | Lior Alon | Every real-rooted exponential polynomial is the restriction of a Lee-Yang polynomial |
| https://doi.org/10.48550/arxiv.2301.05673 | 2023 | Frauke M. Bleher | Explicit Approximations to Class Field Towers |
| https://doi.org/10.2140/ant.2011.5.495 | 2011 | Reinier Bröker | Explicit CM theory for level 2-structures on abelian surfaces |
| arXiv:2602.06199v2 | 2026 | Andrés Chirre | Explicit conditional bounds for $ζ(s)$ at the edge of the critical strip |
| https://openalex.org/W7221733000 | 2026 | Blas Salvador Molero Ravines | Explicit conditional bounds for 𝐿(𝑠, 𝜒) and 𝜁(𝑠) at the edge of the critical strip |
| arXiv:1608.02296v2 | 2016 | Tian An Wong | Explicit formulas for the spectral side of the trace formula of SL(2) |
| https://doi.org/10.1112/tlm3.70013 | 2025 | Linda Frey | Explicit height estimates for CM curves of genus 2 |
| arXiv:2410.12922v3 | 2024 | Tchamitchian Pierre | Explicit lower bounds on the conductors of elliptic curves and abelian varieties over number fields |
| https://doi.org/10.1017/s0004972723000308 | 2023 | Ethan Simpson Lee | EXPLICIT MERTENS’ THEOREMS FOR NUMBER FIELDS |
| https://doi.org/10.1090/s0002-9939-09-10075-8 | 2009 | Vorrapan Chandee | Explicit upper bounds for 𝐿-functions on the critical line |
| https://doi.org/10.4153/cjm-2001-045-5 | 2001 | Stéphane Louboutin | Explicit Upper Bounds for Residues of Dedekind Zeta Functions and Values ofL-Functions ats= 1, and Explicit Lower Bounds for Relative Class Numbers of CM-Fields |
| https://doi.org/10.1007/s40993-023-00472-8 | 2023 | Neelam Kandhil | Explicit upper bounds on the average of Euler–Kronecker constants of narrow ray class fields |
| https://doi.org/10.1090/mcom3031 | 2015 | Loïc Grenié | Explicit versions of the prime ideal theorem for Dedekind zeta functions under GRH |
| https://doi.org/10.1016/j.jnt.2011.09.002 | 2012 | Habiba Kadiri | Explicit zero density theorems for Dedekind zeta functions |
| https://doi.org/10.1016/j.aim.2014.04.007 | 2014 | Emanuel Carneiro | Extremal functions in de Branges and Euclidean spaces |
| https://openalex.org/W7218144066 | 2026 | Tolibjon Ismoilov | Extremal Problems in Fourier Analysis and Applications to Number Theory |
| https://openalex.org/W2259816231 | 2009 | Emanuel Carneiro | Extremality, symmetry and regularity issues in harmonic analysis |
| https://doi.org/10.14288/1.0080078 | 2009 | Mariah Hamel | Fourier analytic applications to number theory |
| arXiv:2505.15994v1 | 2025 | Roni Edwin | Fourier inequalities and sign uncertainty |
| arXiv:2002.11627v2 | 2020 | Martin Stoller | Fourier interpolation from spheres |
| arXiv:2005.02996v3 | 2020 | Andriy Bondarenko | Fourier interpolation with zeros of zeta and $L$-functions |
| https://doi.org/10.1007/s00365-022-09599-w | 2022 | Andriy V. Bondarenko | Fourier Interpolation with Zeros of Zeta and L-Functions |
| arXiv:2411.05095v1 | 2024 | Emily Quesada-Herrera | Fourier optimization and consequences of the generalized Riemann hypothesis |
| https://doi.org/10.1007/978-3-031-97857-9_15 | 2026 | Oscar E. Quesada-Herrera | Fourier Optimization and Consequences of the Generalized Riemann Hypothesis |
| arXiv:2310.01913v2 | 2023 | Emanuel Carneiro | Fourier optimization and Montgomery's pair correlation conjecture |
| https://doi.org/10.1090/mcom/3990 | 2024 | Emanuel Carneiro | Fourier optimization and Montgomery’s pair correlation conjecture |
| https://doi.org/10.48550/arxiv.2502.05106 | 2025 | Das, Mithun Kumar | Fourier optimization and pair correlation problems |
| https://doi.org/10.4171/cmh/467 | 2019 | Emanuel Carneiro | Fourier optimization and prime gaps |
| https://doi.org/10.1093/qmath/haab041 | 2021 | Andrés Chirre | Fourier Optimization and Quadratic Forms |
| https://openalex.org/W7216691330 | 2025 | ANTONIO PEDRO DE AZEVEDO BEZERRA VITOR RAMOS | Fourier Optimization, de Branges Spaces, and Zeros of L-functions |
| arXiv:2404.08380v2 | 2024 | Emanuel Carneiro | Fourier optimization, the least quadratic non-residue, and the least prime in an arithmetic progression |
| arXiv:2403.08659v3 | 2024 | Wayne M Lawton | Fourier Quasicrystals on $\mathbb R^n$ |
| arXiv:2610.10652v1 | 2026 | Dongsheng Wei | Fourier quasicrystals with positive integer masses are sections of Lee-Yang cycles |
| arXiv:2009.12810v1 | 2020 | Alexander Olevskii | Fourier quasicrystals with unit masses |
| https://doi.org/10.15407/mag21.01.04 | 2025 | Aleksei Kulikov | Fourier Uniqueness and Non-Uniqueness Pairs |
| https://doi.org/10.4171/9ecm/40 | 2026 | Danylo Radchenko | Fourier uniqueness pairs and interpolation formulas |
| https://doi.org/10.48550/arxiv.2608.13468 | 2026 | Andriy Bondarenko | Fourier-invariant functions with dense zero sets |
| https://doi.org/10.2139/ssrn.7345198 | 2026 | Nicholas G. Polson | From Gamma Mixtures to Gamma Convolutions: Thorin Measures and the Riemann Xi Function |
| https://doi.org/10.5281/zenodo.19106992 | 2026 | Ulrich Tehrani | From Local Curvature to the Weil Functional: An Explicit Construction |
| https://doi.org/10.1090/bull/1813 | 2023 | Henry Cohn | From sphere packing to Fourier interpolation |
| https://doi.org/10.5802/aif.2714 | 2012 | Pierre Dèbes | Galois Covers and the Hilbert-Grunwald Property |
| https://doi.org/10.1016/j.jnt.2006.05.001 | 2006 | John W. Jones | Galois number fields with small root discriminant |
| arXiv:2307.13498v2 | 2023 | Lior Alon | Gap distributions of Fourier quasicrystals via Lee-Yang polynomials |
| https://doi.org/10.5281/zenodo.19219924 | 2026 | Thierry Marechal | Gaussian Diagonal Dominance for Explicit Formulas in Analytic Number Theory |
| https://doi.org/10.1090/s0002-9947-2013-05716-9 | 2013 | Emanuel Carneiro | Gaussian subordination for the Beurling-Selberg extremal problem |
| https://doi.org/10.1090/s0002-9947-07-04261-4 | 2007 | Anne de Roton | Généralisation du critère de Beurling-Nyman pour l’hypothèse de Riemann |
| https://doi.org/10.15407/mag20.03.02 | 2024 | S. Favorov | Generalized Fourier Quasicrystals, Almost Periodic Sets, and Zeros of Dirichlet Series |
| arXiv:2006.00959v3 | 2020 | Emanuel Carneiro | Generalized sign Fourier uncertainty |
| https://doi.org/10.1007/s00184-026-01042-5 | 2026 | Mduduzi Maphosa | Goodness-of-fit tests for the Dirichlet distribution |
| arXiv:2503.19567v1 | 2025 | Peter Boyvalenkov | Growth of masses of crystalline measures |
| https://doi.org/10.4064/aa190210-22-5 | 2020 | Gregory Debruyne | Halász's theorem for Beurling generalized numbers |
| https://doi.org/10.5281/zenodo.22820901 | 2026 | Luca Eliseo Pavesi | Hankel-rank structure and pairing thresholds in the Guinand--Weil explicit formula: an operational reformulation of the Weil positivity criterion |
| https://doi.org/10.1007/s00526-022-02308-2 | 2022 | Mateusz Kwaśnicki | Harmonic extension technique for non-symmetric operators with completely monotone kernels |
| https://doi.org/10.7169/facm/1229442622 | 2006 | Jerzy Kaczorowski | Hecke's theory and the Selberg class |
| https://doi.org/10.1112/blms.70095 | 2025 | Shanlin Huang | Heisenberg uniqueness pairs and the wave equation |
| https://doi.org/10.48550/arxiv.2607.17159 | 2026 | Zhiqiang Wan | Heisenberg Uniqueness Pairs for a Hyperbola Branch: Supercritical Nonuniqueness for Shifted Lattice Crosses |
| arXiv:2407.11184v1 | 2024 | Lior Alon | Higher Dimensional Fourier Quasicrystals from Lee-Yang Varieties |
| https://doi.org/10.1016/j.aam.2019.06.005 | 2019 | Xingwei Wang | Higher order Turán inequalities for combinatorial sequences |
| https://doi.org/10.1090/s0002-9939-2010-10515-4 | 2010 | Dimitar K. Dimitrov | Higher order Turán inequalities for the Riemann $\xi$-function |
| https://doi.org/10.2140/ant.2014.8.1733 | 2014 | Daniel Fiorilli | Highly biased prime number races |
| arXiv:2109.10844v3 | 2021 | Emanuel Carneiro | Hilbert spaces and low-lying zeros of L-functions |
| https://doi.org/10.1590/scielopreprints.13340 | 2025 | E. A. Reis | Hilbert–Pólya via de Branges and the Weyl m-Function: Vertical Convolution and the Riemann Hypothesis |
| https://doi.org/10.55094/holistence.183 | 2024 | David Eugene Smith | Hıstory of Modern Mathematics |
| https://doi.org/10.48550/arxiv.2606.23535 | 2026 | Ingemar Bengtsson | How Stark units enter SIC overlaps |
| arXiv:2303.10562v2 | 2023 | Federica Pompa | Impact of nuclear matrix element calculations for current and future neutrinoless double beta decay searches |
| https://doi.org/10.48550/arxiv.2207.13898 | 2022 | Hamid Naderiyan | Improved Bounds For Some Asymptotic Formulas for Counting Words in Shift Spaces |
| https://doi.org/10.48550/arxiv.2502.03464 | 2025 | Robert J. Lemke Oliver | Improving the trivial bound for $\ell$-torsion in class groups |
| https://doi.org/10.48550/arxiv.2610.04972 | 2026 | Yanxin Liu | Infinite log-concavity of the Taylor coefficients of the Riemann xi-function |
| arXiv:2412.08552v3 | 2024 | Deepshikha Mishra | Integral representation and functional inequalities involving generalized polylogarithm |
| arXiv:2008.07206v2 | 2020 | David W. Farmer | Jensen polynomials are not a plausible route to proving the Riemann Hypothesis |
| arXiv:1910.01227v3 | 2019 | Michael Griffin | Jensen Polynomials for the Riemann Xi Function |
| arXiv:1902.07321v2 | 2019 | Michael Griffin | Jensen polynomials for the Riemann zeta function and other sequences |
| https://doi.org/10.4171/8ecm/23 | 2023 | Robert J. Berman | Kähler–Einstein metrics and Archimedean zeta functions |
| https://doi.org/10.5281/zenodo.19636675 | 2026 | Ryan Henderson | Kernel-Positivity of Laplace Registers, Blagouchine--Royen Measures, and the Weil/de Branges Explicit-Formula Criterion |
| https://doi.org/10.1016/j.na.2021.112722 | 2021 | Salvador Moll | Kobayashi–Warren–Carter type systems with nonhomogeneous Dirichlet boundary data for crystalline orientation |
| https://doi.org/10.1090/tran/9081 | 2023 | Xingwei Wang | Laguerre inequalities and complete monotonicity for the Riemann Xi-function and the partition function |
| https://doi.org/10.5666/kmj.2009.49.2.355 | 2009 | Jae-Hyun Yang | Langlands Functoriality Conjecture |
| https://openalex.org/W64285022 | 2014 | Sergei Nikolaevich Preobrazhenskii | Large proportion of the zeros of the Riemann zeta function on the critical line |
| arXiv:1508.05870v2 | 2015 | Jeffrey Stopple | Lehmer pairs revisited |
| arXiv:1308.3067v2 | 2013 | Andrew R. Booker | L-functions as distributions |
| https://doi.org/10.1007/s10231-026-01726-9 | 2026 | Takashi Nakamura | L-functions with the Lindelöf and Riemann hypotheses and trivial zeros at even negative integers |
| https://doi.org/10.1016/j.jnt.2023.05.007 | 2023 | Masatoshi Suzuki | Li coefficients as norms of functions in a model space |
| https://openalex.org/W2247947454 | 2011 | Matthew Chasse | Linear preservers and entire functions with restricted zero loci |
| arXiv:2508.08407v1 | 2025 | Samuel Reid | Local Factorization of p-adic Gamma Sums |
| https://doi.org/10.1112/s0010437x2000706x | 2020 | Erez Lapid | Local Rankin–Selberg integrals for Speh representations |
| arXiv:2610.16010v1 | 2026 | Timothy S. Trudgian | Low Lying Zeros of Dedekind Zeta Functions |
| arXiv:1503.06655v1 | 2015 | Luca Brandolini | Low-discrepancy sequences for piecewise smooth functions on the two-dimensional torus |
| https://doi.org/10.48550/arxiv.2309.15872 | 2023 | Anup Biswanath Dixit | Lower bound on height of algebraic numbers and low lying zeros of the Dedekind zeta-function |
| https://doi.org/10.1090/s0025-5718-2010-02403-2 | 2010 | Amalia Pizarro-Madariaga | Lower bounds for the Artin conductor |
| https://doi.org/10.48550/arxiv.2512.10686 | 2025 | Raphaël Lachièze-Rey | Maximal rigidity of random measure and uniqueness pairs: stealthy processes, quasicrystals and periodicity |
| https://doi.org/10.1007/s00220-025-05313-6 | 2025 | Claudia Alfes‐Neumann | Measures, Modular Forms, and Summation Formulas of Poisson Type |
| https://doi.org/10.53846/goediss-4777 | 2014 | M. A. Falkenberg | Metal Impurity Redistribution in Crystalline Silicon for Photovoltaic Application |
| arXiv:2608.15414v1 | 2026 | Fethi Bencherki | Minimax optimal dual control of positive systems: an exact solution for scalar input-sign uncertainty |
| https://doi.org/10.1090/conm/796/16005 | 2024 | Håvard Damm-Johnsen | Modular algorithms for Gross–Stark units and Stark–Heegner points |
| https://doi.org/10.48550/arxiv.math/0007203 | 2000 | Dinakar Ramakrishnan | Modularity of the Rankin-Selberg L-series, and multiplicity one for SL(2) |
| arXiv:math/0303369v1 | 2003 | Siman Wong | Moments of the rank of elliptic curves |
| https://doi.org/10.1007/s40687-019-0199-8 | 2019 | Kyle Pratt | More than five-twelfths of the zeros of $$\zeta $$ are on the critical line |
| https://openalex.org/W2995688135 | 2019 | Dirk Zeindler | More than five-twelfths of the zeros of ζ are on the critical line |
| https://doi.org/10.48550/arxiv.2609.27962 | 2026 | Michel R. P. Planat | Morse Topology, Zero Products, and Elliptic Prime Crossings |
| https://doi.org/10.1142/s1664360722300043 | 2022 | Yoshikazu Giga | Motion by crystalline-like mean curvature: A survey |
| https://doi.org/10.1093/imrn/rnac126 | 2022 | Aleksander Horawa | Motivic Action on Coherent Cohomology of Hilbert Modular Varieties |
| arXiv:2302.07464v1 | 2023 | Wayne M. Lawton | Multidimensional Fourier Quasicrystals I. Sufficient Conditions |
| https://doi.org/10.48550/arxiv.2306.10425 | 2023 | Alex Cowan | Murmurations and explicit formulas |
| arXiv:2003.10771v4 | 2020 | Felipe Gonçalves | New Sign Uncertainty Principles |
| https://doi.org/10.48550/arxiv.2407.12746 | 2024 | Szilárd Gy. Révész | New zero-density estimates for the Beurling $ζ$ function |
| https://doi.org/10.4064/aa240719-3-6 | 2025 | J. Pintz | New zero-density estimates for the Beurling zeta function |
| https://doi.org/10.4064/sm240507-2-8 | 2024 | S. Favorov | Non-negative crystalline and Poisson measures in the Euclidean space |
| https://doi.org/10.71352/ac.39.459 | 2013 | Wen-Bin Zhang | Normalization of Beurling generalized primes with Riemann Hypothesis |
| https://doi.org/10.1112/s1461157000000656 | 2002 | Sami Omar | Note on the Contribution of Low Zeros to Weil's Explicit Formula for Minimal Discriminants |
| arXiv:1301.3158v2 | 2013 | Jeffrey Stopple | Notes on Low discriminants and the generalized Newman conjecture |
| https://doi.org/10.5281/zenodo.19099121 | 2018 | Dye, Nathanael | Numerical Verification of Weil Positivity for Elliptic Curve L-functions |
| arXiv:1910.13715v1 | 2019 | Jing-Jing Huang | On a generalization of a theorem of Popov |
| https://doi.org/10.2140/pjm.2022.320.177 | 2022 | Ian Wagner | On a new class of Laguerre–Pólya type functions with applications in number theory |
| https://openalex.org/W2808485643 | 2018 | Sébastien Darses | On a probabilistic Nyman-Beurling criterion |
| arXiv:math/0311468v3 | 2003 | Ralf Meyer | On a representation of the idele class group related to primes and zeros of L-functions |
| arXiv:2605.23884v1 | 2026 | Jan Mazáč | On almost periodicity in crystalline measures |
| https://doi.org/10.1016/j.jnt.2019.01.016 | 2019 | Ajit Bhand | On Dirichlet series attached to quasimodular forms |
| https://doi.org/10.3390/math13010048 | 2024 | Antanas P Laurincikas | On Discrete Shifts of Some Beurling Zeta Functions |
| https://doi.org/10.3390/axioms15050345 | 2026 | Antanas P Laurincikas | On Functional Independence of Beurling Zeta-Functions |
| arXiv:2403.17803v1 | 2024 | Emanuel Carneiro | On Littlewood's estimate for the modulus of the zeta function on the critical line |
| https://openalex.org/W4300907877 | 2016 | Patrick Kühn | On mean values of mollifiers and L-functions associated to primitive cusp forms |
| https://doi.org/10.48550/arxiv.2501.12526 | 2025 | Martin Čech | On optimality of mollifiers |
| https://doi.org/10.1112/jlms.70358 | 2025 | João P. G. Ramos | On Pauli pairs and Fourier uniqueness problems |
| https://openalex.org/W7110487236 | 2024 | Sousa, M. | ON PAULI PAIRS AND FOURIER UNIQUENESS PROBLEMS |
| https://doi.org/10.1112/s1461157000001224 | 2006 | Takakazu Satoh | On Polynomial Interpolations related to Verheul Homomorphisms |
| https://doi.org/10.14492/hokmj/1607936537 | 2020 | Ramūnas Garunkštis | On primeness of the Selberg zeta-function |
| arXiv:2003.10765v2 | 2020 | Felipe Gonçalves | On regularity and mass concentration phenomena for the sign uncertainty principle |
| https://doi.org/10.48550/arxiv.2108.10238 | 2021 | Oscar E. Quesada-Herrera | On the $q$-analogue of the pair correlation conjecture via Fourier optimization |
| https://doi.org/10.1007/978-3-0348-8303-0_4 | 2001 | Bas Edixhoven | On the André-Oort Conjecture for Hilbert Modular Surfaces |
| https://doi.org/10.1007/s00222-021-01088-4 | 2022 | Yifeng Liu | On the Beilinson–Bloch–Kato conjecture for Rankin–Selberg motives |
| https://doi.org/10.1051/cocv/2023047 | 2023 | Angkana Rüland | On the energy scaling behaviour of singular perturbation models with prescribed dirichlet data involving higher order laminates |
| https://doi.org/10.48550/arxiv.2110.15929 | 2021 | Angkana Rüland | On the Energy Scaling Behaviour of Singular Perturbation Models with Prescribed Dirichlet Data Involving Higher Order Laminates |
| https://doi.org/10.1023/a:1021761421232 | 2003 | Dinakar Ramakrishnan | On the Exceptional Zeros of Rankin–Selberg L-Functions |
| https://doi.org/10.2140/pjm.2014.271.243 | 2014 | Jeremy A. Rouse | On the existence of large degree Galois representations for fields of small discriminant |
| https://doi.org/10.1515/forum-2023-0344 | 2024 | András Bíró | On the geometric trace of a generalized Selberg trace formula |
| https://doi.org/10.4153/s0008414x25101739 | 2025 | Masatoshi Suzuki | On the Hilbert space derived from the Weil distribution |
| https://doi.org/10.7169/facm/1801 | 2019 | Giamila Zaghloul | On the linear twist of degree $1$ functions in the extended Selberg class |
| https://doi.org/10.1090/s0025-5718-2013-02681-6 | 2013 | Mark W. Coffey | On the log-concavity of a Jacobi theta function |
| https://doi.org/10.4064/aa126-1-2 | 2007 | Anne de Roton | On the mean square of the error term for an extended Selberg class |
| https://doi.org/10.7169/facm/1229618750 | 2007 | Laurent Habsieger | On the Nyman-Beurling criterion for the Riemann hypothesis |
| https://doi.org/10.48550/arxiv.2608.12315 | 2026 | Brad Rodgers | On the optimal constant in the Montgomery-Vaughan weighted Hilbert inequality |
| arXiv:2602.20313v2 | 2026 | Wojciech Michalowski | On the Pólya Frequency Order of the de Bruijn--Newman Kernel: Certified Failure at Order Five |
| https://doi.org/10.1017/s1446788712000225 | 2012 | Aleksandar Ivić | ON THE RANKIN–SELBERG ZETA FUNCTION |
| https://doi.org/10.1017/s1446788712000225 | 2012 | Ivić Aleksandar | ON THE RANKIN–SELBERG ZETA-FUNCTION |
| https://doi.org/10.4064/aa104-2-1 | 2002 | Jerzy Kaczorowski | On the structure of the Selberg class, IV: basic invariants |
| https://doi.org/10.4007/annals.2011.173.3.4 | 2011 | Jerzy Kaczorowski | On the structure of the Selberg class, VII: 1<d<2 |
| https://doi.org/10.48550/arxiv.2607.20041 | 2026 | Keita Nakai | On the value distribution of the Riemann zeta-function with general shifts |
| https://doi.org/10.1070/im8463 | 2016 | Irina Sergeevna Rezvyakova | On the zeros of linear combinations of L-functions of degree two on the critical line. Selberg's approach |
| https://doi.org/10.1016/j.jnt.2016.01.026 | 2016 | Siegfred Baluyot | On the zeros of Riemann's zeta-function on the critical line |
| https://doi.org/10.3390/axioms13030145 | 2024 | Andrius Geštautas | On Universality of Some Beurling Zeta-Functions |
| https://doi.org/10.3390/math12030459 | 2024 | Antanas P Laurincikas | On Value Distribution of Certain Beurling Zeta-Functions |
| https://doi.org/10.4064/aa221223-15-2 | 2023 | Frederik Broucke | On zero-density estimates and the PNT in short intervals for Beurling generalized numbers |
| https://doi.org/10.2422/2036-2145.202410_003 | 2025 | Frederik Broucke | On zero-density estimates for Beurling zeta functions |
| https://doi.org/10.5281/zenodo.18193426 | 2026 | David Thomson | Operator Package 6: Riemann Hypothesis Proof Program: Identification, Determinant Closure, and Positivity Fork for the Riemann Function Operators Series |
| https://doi.org/10.5281/zenodo.21143337 | 2026 | Dean Kulik | Operator-Theoretic and Computational Realizations of the Riemann Hypothesis |
| https://doi.org/10.5281/zenodo.21144643 | 2026 | Dean Kulik | Operator-Theoretic and Computational Realizations of the Riemann Hypothesis Expanded |
| https://doi.org/10.48550/arxiv.2511.14736 | 2025 | Chirre, Andrés | Optimal bounds for sums of bounded arithmetic functions |
| https://doi.org/10.48550/arxiv.2609.15329 | 2026 | Andrew Pearce‐Crump | Optimising Selberg's method for critical zeros |
| arXiv:1902.06330v3 | 2019 | Dan Romik | Orthogonal polynomial expansions for the Riemann xi function |
| https://doi.org/10.48550/arxiv.2202.01837 | 2022 | Szilárd Gy. Révész | Oscillation of the remainder term in the prime number theorem of Beurling, "caused by a given zeta-zero" |
| https://doi.org/10.1093/imrn/rnac274 | 2022 | Szilárd Gy. Révész | Oscillation of the Remainder Term in the Prime Number Theorem of Beurling, “Caused by a Given ζ-Zero” |
| https://doi.org/10.48550/arxiv.2501.14545 | 2025 | Siegfred Baluyot | Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions of Simple Zeros and Critical Zeros |
| https://doi.org/10.5281/zenodo.22037309 | 2026 | Michael Sarnowski | Paper 134AL: The Mellin–Wright Sufficiency Barrier and Relative Hermite Positivity in the Riemann Xi Jensen Hierarchy Smooth log-concave counterexamples, exact Beta–Sonine safe laws, and the all-order multiplier-factorization target |
| https://doi.org/10.5281/zenodo.22062819 | 2026 | Michael Sarnowski | Paper 134AU: Target-Root-Free Hermite Cells and Coefficient-Derived Center-Spread Normalization in the Riemann ξ Jensen Hierarchy Unknown-child-root isolation, interval-domain critical-data corridors, and the remaining small-shift high-degree obstruction |
| https://doi.org/10.5281/zenodo.22072947 | 2026 | Michael Sarnowski | Paper 134AZ: Global Logarithmic-Gap Coordinates and the All-Order Normal-Family Bridge in the Riemann ξ Jensen Hierarchy Global simple-root coordinates, normalized negative-root probability simplices, and the remaining all-order extension theorem |
| https://doi.org/10.5281/zenodo.22082170 | 2026 | Michael Sarnowski | Paper 134BB: Hankel-Only Spectral-Shift Closure and the Theta-Secant Pick Kernel in the Riemann ξ Jensen Hierarchy A one-family moment criterion, automatic recovery of the beta double lock, and an exact theta-kernel proof target |
| arXiv:2507.16029v3 | 2025 | Lior Alon | Periodic Hypersurfaces and Lee-Yang Polynomials |
| https://doi.org/10.2140/apde.2023.16.2327 | 2023 | João P. G. Ramos | Perturbed interpolation formulae and applications |
| https://doi.org/10.48550/arxiv.2410.04557 | 2024 | Danylo Radchenko | Perturbed lattice crosses and Heisenberg uniqueness pairs |
| https://doi.org/10.1007/s40993-018-0103-4 | 2018 | Kyle Pratt | Perturbed moments and a longer mollifier for critical zeros of $$\zeta $$ ζ |
| https://doi.org/10.33774/coe-2025-4bm72 | 2025 | Vasil Dinev Penchev | Philosophical and mathematical reflection on Riemann’s hypothesis. I Reframing in Hilbert arithmetic |
| https://doi.org/10.2139/ssrn.5244354 | 2025 | Vasil Dinev Penchev | Philosophical and mathematical reflection on Riemann's hypothesis. II The ontomathematical proof of Riemann's hypothesis in Hilbert arithmetic |
| https://doi.org/10.31235/osf.io/vkwtm_v1 | 2025 | Vasil Dinev Penchev | Philosophical and mathematical reflection on Riemann’s hypothesis. II The ontomathematical proof of Riemann’s hypothesis in Hilbert arithmetic |
| https://doi.org/10.5281/zenodo.19665790 | 2026 | Ulrich Tehrani | Positive Curvature of the Spectral Trace at the Critical Line |
| arXiv:2608.15415v2 | 2026 | Seewoo Lee | Positive quasimodular forms and the sign uncertainty principle |
| https://doi.org/10.5281/zenodo.22013011 | 2026 | Akihiro Koide | Positive-Definite Correlation Hierarchies, Zero Strips, and Derivative de Bruijn–Newman Constants |
| https://doi.org/10.5281/zenodo.21529688 | 2026 | Kianming(Jianming) Wang | Prime-Coordinate Analysis: Foundations, Measure Theory, Operator Structure, and Arithmetic Geometry |
| arXiv:2005.02393v3 | 2020 | Andrés Chirre | Primes in arithmetic progressions and semidefinite programming |
| https://doi.org/10.5565/publmat6311906 | 2018 | Jean‐François Lafont | Primitive geodesic lengths and (almost) arithmetic progressions |
| https://doi.org/10.1090/s0273-0979-01-00912-0 | 2001 | Philippe Biane | Probability laws related to the Jacobi theta and Riemann zeta functions, and Brownian excursions |
| arXiv:2607.19026v1 | 2026 | Oleg Szehr | Projected Inner-Function Dynamics and Crystalline Measures of Meyer-Blaschke type |
| https://doi.org/10.20944/preprints202505.2110.v2 | 2025 | Y. Shimizu | Proof of the Riemann Hypothesis |
| https://doi.org/10.1016/j.jnt.2010.06.014 | 2010 | Rikard Olofsson | Properties of the Beurling generalized primes |
| arXiv:math/0310384v2 | 2003 | Joshua N. Cooper | Quasirandom Arithmetic Permutations |
| https://openalex.org/W7115100055 | 2025 | Pimm, Joshua | Real-analytic modular forms for Gamma_0(N) and their L-series |
| https://doi.org/10.48550/arxiv.1502.06844 | 2014 | Yaoming Shi | Real-rooted Pólya-like approximations to the Riemann Xi-function |
| https://doi.org/10.5281/zenodo.22133100 | 2026 | Oleg Glushkov | Reproducibility Package for Numerical and Formal Diagnostics of a Compactly Supported Bombieri–Weil Positivity Test |
| https://doi.org/10.1016/j.laa.2014.08.001 | 2014 | Harald Woracek | Reproducing kernel almost Pontryagin spaces |
| https://doi.org/10.5802/jtnb.1182 | 2022 | Ming-Lun Hsieh | Restriction of Eisenstein series and Stark–Heegner points |
| https://doi.org/10.48550/arxiv.1804.10043 | 2018 | Nicholas G. Polson | Riemann, Thorin, van Dantzig Pairs, Wald Couples and Hadamard Factorisation |
| https://doi.org/10.1090/s0273-0979-03-00995-9 | 2003 | Stephen Samuel Gelbart | Riemann’s zeta function and beyond |
| https://doi.org/10.1016/j.indag.2022.08.002 | 2022 | Athanasios Sourmelidis | Riemann-type functional equations |
| https://doi.org/10.3792/pjaa.97.016 | 2021 | Shin-ya Koyama | Rigidity of Euler products |
| https://doi.org/10.1109/tcns.2024.3372143 | 2024 | Spencer Hutchinson | Safe Pricing Mechanisms for Distributed Resource Allocation With Bandit Feedback |
| https://doi.org/10.1007/jhep11(2022)143 | 2022 | Nathan Benjamin | Scalar modular bootstrap and zeros of the Riemann zeta function |
| https://doi.org/10.5281/zenodo.23229270 | 2026 | Frederic David Blum | Scale-Resolved Weil Positivity |
| https://doi.org/10.1137/120897250 | 2014 | Michael Goldman | Scaling Law and Reduced Models for Epitaxially Strained Crystalline Films |
| https://doi.org/10.52843/meta-mat.7nh919 | 2025 | Laure Giovangigli | Scattering from a random thin coating of nanoparticles: the Dirichlet case |
| https://doi.org/10.1021/acsami.6c03558 | 2026 | Pavel N. Zolotarev | Search for Low-Periodic Substructures in Crystalline Solids: A Novel Approach |
| https://doi.org/10.1021/acs.cgd.5b01695 | 2016 | Pavel N. Zolotarev | Searching New Crystalline Substrates for OMBE: Topological and Energetic Aspects of Cleavable Organic Crystals |
| arXiv:2309.12806v1 | 2023 | Alessandro Languasco | Sequences of integers generated by two fixed primes |
| https://doi.org/10.1007/s13373-014-0057-3 | 2014 | Paul Leo Butzer | Seven pivotal theorems of Fourier analysis, signal analysis, numerical analysis and number theory: their interconnections |
| https://doi.org/10.1016/j.jnt.2016.03.002 | 2016 | Sergio Astudillo | Sharp lower bounds for regulators of small-degree number fields |
| arXiv:2606.02299v1 | 2026 | Tolibjon Ismoilov | Sharp sign uncertainty for trigonometric polynomials |
| arXiv:1601.05551v3 | 2016 | Shuoming An | Shortcuts to adiabaticity by counterdiabatic driving for trapped-ion displacement in phase space |
| arXiv:2408.01186v1 | 2024 | Emanuel Carneiro | Sign uncertainty and de Branges spaces |
| arXiv:2210.01684v3 | 2022 | Henry Cohn | Sign uncertainty principles and low-degree polynomials |
| https://openalex.org/W195872951 | 2006 | Stéphane Louboutin | Some explicit upper bounds for residues of zeta functions of number fields taking into account the behavior of the prime 2(Analytic Number Theory) |
| https://doi.org/10.1090/s0002-9947-2010-04886-x | 2010 | Emanuel Carneiro | Some extremal functions in Fourier analysis. II |
| https://doi.org/10.2969/aspm/04910367 | 2019 | Wolfgang Schwarz | Some highlights from the history of probabilistic number theory |
| arXiv:2605.10766v2 | 2026 | Sergii Favorov | Some properties of Fourier quasicrystals and measures on a strip |
| https://openalex.org/W7115356238 | 2024 | Pushnitski, Alexander; id_orcid 0000-0001-5622-7210 | Spectral asymptotics for a family of arithmetical matrices and connection to Beurling primes |
| https://doi.org/10.33774/coe-2025-s9m7d-v3 | 2025 | Diego Muguet de Magalhães | Spectral Coherence and Geometric Reformulation of the Riemann Hypothesis via Torsion-Free Vector Waves |
| arXiv:2509.14953v3 | 2025 | Oleg Szehr | Spectral Criteria for Uniqueness Pairs of Unitary Transforms |
| https://doi.org/10.5281/zenodo.19655488 | 2026 | Leandro de Oliveira | Spectral Identification of the Zeta D'Alembertian: The Exact Coeficient cn = 1, the Weyl Limit-Point Condition, and Completeness via Beurling Density |
| https://doi.org/10.1007/s11117-026-01207-6 | 2026 | B. V. Rajarama Bhat | Spectral radii for subsets of Hilbert $$C^*$$-modules and spectral properties of positive maps |
| arXiv:2106.01715v1 | 2021 | Alain Connes | Spectral Triples and Zeta-Cycles |
| https://doi.org/10.5287/ora-v0nv5y1dk | 2014 | Thomas Hudson | Stability and regularity of defects in crystalline solids |
| arXiv:2410.08682v2 | 2024 | Alexander Ulanovskii | Stability of shifts, interpolation, and crystalline measures |
| arXiv:2004.05678v1 | 2020 | Pavel Kurasov | Stable polynomials and crystalline measures |
| https://doi.org/10.5821/dissertation-2117-105573 | 2016 | Daniele Casazza | Stark-Heegner points and p-adic L-functions |
| https://doi.org/10.9734/jamcs/2024/v39i11861 | 2024 | Daniele Lattanzi | Statistical Distributions of Prime Number Gaps |
| https://doi.org/10.5281/zenodo.21927640 | 2026 | Akihiro Koide | Strict Log-Concavity of the Laguerre Quantity for the Riemann Xi Kernel: Resolution of Csordas' Open Problem 4.14 |
| https://doi.org/10.4153/cmb-2004-046-0 | 2004 | K. Soundararajan | Strong Multiplicity One for the Selberg Class |
| arXiv:math/9707237v1 | 1997 | Emmanuel Kowalski | Sur le rang de J_0(q) |
| https://doi.org/10.5281/zenodo.21922673 | 2026 | Robert Sherwood | Suzuki Localized Weil Form Research Compendium for The Riemann Hypothesis |
| https://doi.org/10.1023/a:1017537415688 | 2001 | Farshid Hajir | Tamely Ramified Towers and Discriminant Bounds for Number Fields |
| arXiv:2106.07073v3 | 2021 | Serhii Favorov | Temperate distributions with locally finite support and spectrum on Euclidean spaces |
| https://doi.org/10.4236/apm.2026.169032 | 2026 | Michael Mark Anthony | Terminal Cycles of Name-Sum Maps, a Minimal Language for the Collatz Map, and the Weave of a Binomial Expansion |
| arXiv:math/0305114v1 | 2003 | D. R. Heath-Brown | The average analytic rank of elliptic curves |
| https://doi.org/10.48550/arxiv.2512.18677 | 2025 | David Berghaus | The basis functions of Fourier interpolation |
| arXiv:1602.08545v3 | 2016 | Zhenghua Xu | The Bernstein inequality for slice regular polynomials |
| https://doi.org/10.48550/arxiv.1702.04579 | 2017 | Jacob Carruth | The Beurling-Selberg Box Minorant Problem via Linear Programming Bounds |
| https://doi.org/10.48550/arxiv.2209.01689 | 2022 | Szilárd Gy. Révész | The Carlson-type zero-density theorem for the Beurling zeta function |
| https://doi.org/10.1112/jlms.70110 | 2025 | Szilárd Gy. Révész | The Carlson‐type zero‐density theorem for the Beurling ζ function |
| https://doi.org/10.2139/ssrn.6986400 | 2026 | Nicholas G. Polson | The Comet Kernel and a Thorin Bridge to Xi |
| arXiv:2401.01121v1 | 2024 | Serhii Favorov | The crystalline measure that is not a Fourier Quasicrystal |
| arXiv:1801.05914v5 | 2018 | Brad Rodgers | The De Bruijn-Newman constant is non-negative |
| https://doi.org/10.20944/preprints202604.1513.v1 | 2026 | Avi Gershon | The De Bruijn-Newman Constant Is Zero |
| https://doi.org/10.4007/annals.2010.172.1559 | 2010 | Manjul Bhargava | The density of discriminants of quintic rings and fields |
| https://doi.org/10.22215/etd/2017-11742 | 2017 | Graeme Turner | The Discriminant and Conductor of Bicyclic Quartic Fields |
| https://doi.org/10.1093/qmath/hat060 | 2014 | Stephen Lester | THE DISTRIBUTION OF THE LOGARITHMIC DERIVATIVE OF THE RIEMANN ZETA-FUNCTION |
| https://doi.org/10.48550/arxiv.2607.14981 | 2026 | Moritz Doll | The divisor of the twisted Selberg zeta function |
| https://doi.org/10.48550/arxiv.1410.6450 | 2014 | Giuseppe Iurato | The early historical roots of Lee-Yang theorem |
| https://doi.org/10.4213/im9664e | 2026 | Irina Sergeevna Rezvyakova | The Epstein zeta-function contains a positive proportion of non-trivial zeros on the critical line |
| arXiv:2607.28931v2 | 2026 | Shin-ya Koyama | The Fine-Structure Hierarchy of Prime Biases and the Universal Dominance of $-1 \pmod N$ |
| https://doi.org/10.7146/math.scand.a-15066 | 2008 | Christian Berg | The fixed point for a transformation of Hausdorff moment sequences and iteration of a rational function |
| arXiv:2412.05485v1 | 2024 | Roni A. Edwin | The Gauss Circle Problem and Fourier Quasicrystals |
| https://doi.org/10.1016/j.jfa.2011.09.021 | 2011 | Ian D. Morris | The generalised Berger–Wang formula and the spectral radius of linear cocycles |
| arXiv:2609.03736v2 | 2026 | Andrew Salmon | The half-rate linear programming bound for binary codes is $\frac12-\frac1π$ |
| https://doi.org/10.2140/ent.2025.4.67 | 2025 | Elias Caeiro | The Heegner–Stark theorem and Stark–Heegner points |
| arXiv:math/0112196v1 | 2001 | Stephen D. Miller | The Highest-Lowest Zero and other Applications of Positivity |
| arXiv:1106.4348v3 | 2011 | Jeffrey C. Lagarias | The Integral of the Riemann xi-function |
| arXiv:2609.14295v2 | 2026 | Koustav Banerjee | The Jensen--Pólya program and inequalities for arithmetic sequences |
| https://doi.org/10.5281/zenodo.19394013 | 2026 | marsh, Brandon, Amasarac, Eluriah, KeyDjinn, Tiwoven, Eidolon | The Marsh-Feagans Spectral Algebra and the Riemann Hypothesis: A Partial Resolution via Pseudo-Hermitian Operator Theory, Narrow-Band Weil Positivity, and the Gershgorin-Gabor Framework |
| https://doi.org/10.1307/mmj/20226271 | 2024 | Szilárd Gy. Révész | The Method of Pintz for the Ingham Question About the Connection of Distribution of ζ-Zeroes and Order of the Error in the PNT in the Beurling Context |
| https://openalex.org/W7120458778 | 2025 | Francisco de Mello Calderaro | The Nyman-Beurling theory on Hardy spaces : relationship between zeta-zeros, density and orthogonality in H² |
| https://doi.org/10.1016/j.jnt.2026.06.013 | 2026 | Tianyu Zhao | The positivity technique and low-lying zeros of Dirichlet L-functions |
| https://doi.org/10.5281/zenodo.17625338 | 2025 | Dow, Jeremy | The Prime–Resonance Operator VIII: Explicit-Formula Equivalence and Completion of the Programme |
| https://doi.org/10.4064/aa132-2-5 | 2008 | M. Urrutia Mera | The q-Mellin transform of automorphic forms and converse theorems |
| https://doi.org/10.48550/arxiv.2009.02640 | 2020 | Artur Kawalec | The recurrence formulas for primes and non-trivial zeros of the Riemann zeta function |
| arXiv:2407.20379v4 | 2024 | W. Riley Casper | The restricted discrete Fourier transform |
| https://doi.org/10.14445/22315373/ijmtt-v72i1p101 | 2026 | Frantz Olivier | The Riemann Hypothesis: A Symmetrical Transportation Overlay by a Gauge Point that Reveals the Compress States of the Golden Ratio |
| arXiv:2405.05834v3 | 2024 | Thuan Quang Tran | The Riemann hypothesis and dynamics of Backtracking New Q-Newton's method |
| https://doi.org/10.1214/20-aop1433 | 2020 | Eero Saksman | The Riemann zeta function and Gaussian multiplicative chaos: Statistics on the critical line |
| https://doi.org/10.11144/javeriana.10554.54742 | 2021 | Sebastián Carrillo Santana | The Riemann zeta function and tate's thesis |
| https://doi.org/10.1007/s00208-023-02574-1 | 2023 | Péter L. Erdős | The sequence of prime gaps is graphic |
| https://doi.org/10.48550/arxiv.2607.06285 | 2026 | Jan Hendrik Bruinier | The Siegel-Weil formula in geometry and arithmetic |
| https://doi.org/10.5281/zenodo.18854320 | 2026 | Daniel Santiago | The Sieve Firewall - The True Reimann Hypothesis Solved |
| https://doi.org/10.5281/zenodo.20174501 | 2026 | Frank Morales | The Sieve of Eratosthenes: A Complete Python Tutorial with Spectral Quantification of Prime Theorems |
| https://doi.org/10.5281/zenodo.22181598 | 2026 | FORTUNATO ZAMPAGLIONE | The signed Turan-Jacobi recurrence and the sign-propagation lemma for the Hankel tower of the Riemann xi coefficients |
| https://doi.org/10.12921/cmst.2011.17.01.87-92 | 2011 | Marek Wolf | The Skewes Number for Twin Primes: Counting Sign Changes of π 2(x) – C2Li2(x) |
| https://doi.org/10.4007/annals.2004.160.185 | 2004 | Philippe Michel | The subconvexity problem for Rankin–Selberg L-functions and equidistribution of Heegner points |
| https://doi.org/10.5281/zenodo.19211032 | 2026 | Thierry Marechal | The Transverse Localization Obstruction and the Restricted Weil Path: Why θeff (k) ≥ c > 0 Fails, and What Replaces It in the Spectral Program for the Riemann Hypothesis |
| https://doi.org/10.48550/arxiv.2301.04390 | 2023 | Adam J. Harper | The typical size of character and zeta sums is $o(\sqrt{x})$ |
| https://doi.org/10.48550/arxiv.2604.24900 | 2026 | Adem Limani | The Uncertainty Principle in Harmonic Analysis -- Lecture Notes on Selected Topics |
| https://doi.org/10.65157/cicsm.2025.001 | 2025 | Bouchaib Bahbouhi | The Unified Prime Equation and the Z Constant: A Constructive Path Toward the Riemann Hypothesis |
| arXiv:math/0703392v1 | 2007 | Alain Connes | The Weil proof and the geometry of the adeles class space |
| https://doi.org/10.2139/ssrn.7320139 | 2026 | Nicholas G. Polson | Thorin Measures and the Reciprocal Xi Function |
| https://doi.org/10.5281/zenodo.21247201 | 2026 | Patrick Devlin | Threshold Enhancements at the Zeta Zeros in a Dilate-Frame Distance Diagnostic |
| https://doi.org/10.1007/s00041-026-10250-6 | 2026 | Denis Zelent | Time-frequency Localization in the Fourier Symmetric Sobolev Space |
| arXiv:2606.01040v1 | 2026 | Wayne M Lawton | Topological and Diophantine properties of lattice subset projections |
| https://doi.org/10.5281/zenodo.22181679 | 2026 | FORTUNATO ZAMPAGLIONE | Transfer of the Turan property under the upper binomial (Pascal) map: the pointwise implication is false, the global one is a cooperative identity |
| https://doi.org/10.5281/zenodo.21968915 | 2026 | Jeffery Huckstead | Triangular n Postmaster Research Volume I v0.6: RH-Open Proof Spine and Branch Atlas Prime and polar entry equations, exact 7/8 lemma, Lighthouse gates, uniformity contract, rejected-hypothesis register, and RH firewall |
| https://doi.org/10.1006/jnth.2001.2724 | 2002 | David Solomon | Twisted Zeta-Functions and Abelian Stark Conjectures |
| https://doi.org/10.5486/pmd.2011.5067 | 2011 | Harold George Diamond | Two results on Beurling generalized numbers |
| https://doi.org/10.1007/s13324-017-0173-9 | 2017 | Palle E. T. Jørgensen | Unbounded operators in Hilbert space, duality rules, characteristic projections, and their applications |
| https://doi.org/10.3390/w18080901 | 2026 | Mahmoud M. Kazem | Uncertainty-Aware Groundwater Potential Mapping in Arid Basement Terrain Using AHP and Dirichlet-Based Monte Carlo Simulation: Evidence from the Sudanese Nubian Shield |
| https://doi.org/10.1007/s11139-021-00435-6 | 2021 | Stephan Ramon Garcia | Unconditional explicit Mertens’ theorems for number fields and Dedekind zeta residue bounds |
| https://openalex.org/W4226159075 | 2021 | Nikos Mantzakouras | Unconditional representations of the Euler-Mascheroni constant and the Bernoulli numbers via the Taylor coefficients of the Riemann ξ-function, and a hierarchy of exact relations at the central point |
| https://doi.org/10.48550/arxiv.2311.06947 | 2023 | Robert J. Lemke Oliver | Uniform exponent bounds on the number of primitive extensions of number fields |
| https://doi.org/10.48550/arxiv.2604.12997 | 2026 | Ricardo Motta | Uniqueness and non-uniqueness pairs for the fractional Laplacian |
| https://doi.org/10.1016/j.jnt.2013.05.015 | 2013 | Guy Henniart | Uniqueness of Rankin–Selberg products |
| arXiv:2006.07610v2 | 2020 | S. Yu. Favorov | Uniqueness Theorems for Fourier Quasicrystals and Temperate Distributions with Discrete Support |
| https://doi.org/10.48550/arxiv.2609.07080 | 2026 | Jiong Yang | Upper bounds for arithmetic functions over polynomial values via Chebotarev--Sato--Tate distributions |
| https://doi.org/10.2140/pjm.2015.277.241 | 2015 | Siman Wong | Upper bounds of root discriminant lower bounds |
| https://openalex.org/W3208928924 | 2004 | Marcel Arndt | Upscaling from Atomistic Models to Higher Order Gradient Continuum Models for Crystalline Solids |
| https://doi.org/10.5281/zenodo.20573750 | 2026 | JONGMIN CHOI | V183 — Function‑Field Riemann Hypothesis as a Blueprint: A Long‑Term Research Map for Explicit‑Formula Positivity and Finite Toeplitz Models |
| https://doi.org/10.5281/zenodo.20574448 | 2026 | JONGMIN CHOI | V184 — Weil Positivity as a Missing Arithmetic Hodge Index Subject: A Route‑Pruning and Frontier‑Mapping Document for the Riemann Hypothesis |
| https://doi.org/10.5281/zenodo.20697233 | 2026 | JONGMIN CHOI | V196.1 — An ACS‑0 Correspondence Carrier for Weil's Explicit Formula: Degree‑Zero Projection, Admissible Regularization, and an Ultralocal Sign Sector |
| https://doi.org/10.1017/fms.2025.10116 | 2025 | Igor Pak | Vanishing of Schubert coefficients via the effective Hilbert nullstellensatz |
| https://doi.org/10.3390/math6120289 | 2018 | Matt Visser | Variants on Andrica’s Conjecture with and without the Riemann Hypothesis |
| arXiv:2608.14261v1 | 2026 | Angélique Campaniello | Wave Transport in Fourier Quasicrystals Revealed by Water Waves |
| https://doi.org/10.5281/zenodo.23034001 | 2026 | Ryota Mori | Weil positivity on a window of width log 5: a formal proof in Lean 4 |
| https://doi.org/10.5281/zenodo.21326836 | 2026 | Salem Eid | Windowed Weil Positivity and the Frame Bound of Dirichlet Zeros: The Quartic Character Modulo Five |
| https://doi.org/10.1090/tran/7809 | 2019 | Dimitar K. Dimitrov | Wronskians of Fourier and Laplace transforms |
| https://doi.org/10.48550/arxiv.2211.06264 | 2022 | Dickinson, George | Zeros of Dirichlet $L$-functions near the critical line |
| https://doi.org/10.1112/mtk.12239 | 2024 | George Dickinson | Zeros of dirichlet L‐functions near the critical line |
| https://doi.org/10.1016/j.jnt.2024.12.005 | 2025 | Keiju Sono | Zeros of Dirichlet L-functions on the critical line |
| https://doi.org/10.4064/aa-93-1-37-52 | 2000 | Peter Bauer | Zeros of Dirichlet L-series on the critical line |
| https://doi.org/10.48550/arxiv.2311.10285 | 2023 | Jérémy Dousselin | Zeros of linear combinations of Dirichlet $L$-functions on the critical line |
| https://doi.org/10.1016/j.jnt.2011.10.002 | 2011 | Shaoji Feng | Zeros of the Riemann zeta function on the critical line |
| https://doi.org/10.48550/arxiv.2409.01350 | 2024 | Ashay Burungale | Zeta elements for elliptic curves and applications |
| https://doi.org/10.48550/arxiv.2606.08848 | 2026 | Federico Pellarin | Zeta functions over curves |
| https://doi.org/10.1007/s00222-023-01203-7 | 2023 | Kentaro Nakamura | Zeta morphisms for rank two universal deformations |
