# S1 — Weil positivity and the explicit-formula / trace-formula school (survey )

Surveyor S1. Brief: `BRIEF.md`. Index checked: `05-meta-and-planning/ROUTES-TRIED-INDEX/` (README, 05_LITERATURE L01–L68,
05b L69–L85, SURVEY_MODERN_UNTRIED).

Method. arXiv API returned 429 from the sandbox after a few calls; the sweep used OpenAlex (30 queries: Weil positivity /
criterion / quadratic functional / explicit formula positivity, Connes, Connes–Consani, CCM prolate, semilocal, Sonine,
Burnol, Suzuki screw, Li/Keiper, Bombieri–Lagarias, Yoshida, Lagarias, Meyer, Goldfeld, spectral triples, arithmetic/scaling
site, BC-system, windowed certificates). 1004 distinct works returned, 835 kept after removing homonyms (materials science
"zeta potential", "screw dislocation", Siegel–Weil, etc.), listed in §A. About 25 were read at abstract+ depth (§B);
corpus grep done for every §B item.

Overall verdict, honest: **no item in this school is the missing object.** The school splits into (i) reformulations
(Connes trace formula, CC archimedean place, CCM prolate/spectral triples, Suzuki screw/de Branges, Li/Keiper,
Toeplitz–Hankel), all already in the index; (ii) fixed-window numerical certificates, which are dual certificates
(thm:Z class) — but the frontier has moved and must be recorded; (iii) unrefereed "proofs" (Zenodo), all of which
reduce to an unproved positivity step.

## B. Deep-read notes (most relevant first)

| # | Item | Status | Mechanism | Props (1–4 of BRIEF) | In index? | Verdict |
|---|---|---|---|---|---|---|
| B1 | R. Mori, *Weil positivity on the window of width log 15*, Zenodo 10.5281/zenodo.23281235; certificate code zenodo 23092422, github moriryota/prolate-weil-bounds, moriryota/weil-log15 | CLAIMED, Arb-certified, unrefereed ("external certificate, not formal proof") | Q(f) ≥ 2^{-2904}‖f‖² for all C² f on [−½log15, ½log15]; Liu's bounded-comparison framework + prolate defect bound + new Schur weight for the prime operator; finite matrix of size 832 per parity; margins 2.4e−70 (even), 4e−66 (odd), total error < 5e−94. Prior paper: ½log12. Prime 13 enters. | 1 yes (uses actual Λ), 2 no, 3 no (certificate), 4 no | **NOT in corpus/index** (grep 23281235, moriryota: 0) | KNOWN class (dual certificate / thm:Z), but **frontier datum**: half-width ½log15 ≈ 1.354 > Liu 17/16 > Paper 46 ½log5. Must be added to index and Paper 46 related work. Note margins ~e^{−4πμ}: consistent with Mori's own upper bound (B2). |
| B2 | R. Mori, *A μ^{9/2} log μ upper bound for windowed Weil forms*, Zenodo 23175060 (v3) | CLAIMED, PROVED-style, unrefereed | Unconditional upper bound λ_min(λ) ≤ 3.5e24 μ^{9/2} log μ e^{−4πμ} (50 ≤ μ ≤ 10⁴), ≤ 7.6e24 μ⁵(log μ)³ e^{−4πμ} ∀μ≥50, μ=λ²; prolate test vectors, Prüfer phase, non-stationary phase. Upper bounds only. | none (no sign) | NOT in corpus | KNOWN (matches thm:finZ / near-kernel λ≈2.5e−22 at T=1 phenomenon); useful as quantitative ceiling for any certificate method. |
| B3 | Guo Chen, *Prolate leakage and near-zero spectral clusters of the semilocal Weil operator*, Zenodo 23297284 | CLAIMED, unrefereed | For A_λ on L²([λ⁻¹,λ],du/u) (archimedean + all prime powers ≤ λ² + poles): ≥ m eigenvalues in [−δ,δ], δ ≲ λ^{4m+17/2}e^{−πλ²}; test vectors = summation map u^{1/2}Σf(nu) of prolates with f(0)=f̂(0)=0; exact residual identity from explicit formula + Poisson. Localizes on both sides of 0, no positivity assumed. | 2 partly (Poisson summation = global FE coupling), no sign | 1 corpus hit only | KNOWN (CCM 2024 L06/L39 mechanism, multiplicity version). Relevant as a NO-GO quantifier: any positivity proof must resolve m clustered eigenvalues at scale e^{−πλ²}. |
| B4 | J. N. Ibbotson, *Certified Weil positivity past log 19…*, Zenodo 21257072 | CLAIMED, Arb LDLᵀ, unrefereed | PD on **finite raised-cosine taper families** only (not full space) with autocorrelation support past log 19 | 1 yes, 3 no | NOT in corpus | KNOWN (finite-family certificate; weaker than full-window). IRRELEVANT for the frontier. |
| B5 | A. Senke, *Exact finite Gram closure … window (−77/64, 77/64)*, Zenodo 22871383 | CLAIMED, exact GMP Gram residuals, unrefereed | Full window half-width 1.203 (> 17/16), primes 2..11 incl. 8, 9; cellwise Schur + Binet tail + dyadic transfer | 1 yes, 3 no | NOT in corpus | KNOWN class; frontier datum (superseded by B1 if B1 holds). |
| B6 | R. C. Angelone, localized Weil positivity up to μ ≤ 5.001 / ½log3 / ½log5, Zenodo 22287510 & companions | CLAIMED, peer-verification protocol | Arb even/odd + Schur complement | 3 no | NOT in corpus | KNOWN (overlaps Paper 46 ½log5). |
| B7 | S. Eid, *Five-rung coercivity ladder up to 1.12 log 2*; *Quartic character mod 5* (Zenodo 21326836 & co.) | CLAIMED | Coercivity ladder; for χ mod 5 one-page proof on prime-free window ½log2 with constant 1/5, "quantifiably fails for ζ"; at ½log7 symbol indefinite but compressed form ≈ 8e−5 > 0 | 1 partly | NOT in corpus | KNOWN (prime-free window = archimedean-only, CC 2021 L39). The χ-mod-5 near-null mode built from primes vanishing at the zeros is the same near-kernel phenomenon as h*. |
| B8 | T. A. Ziad, *Localized constrained Weil forms: near-degeneracy and a Davenport–Heilbronn first kernel*, Zenodo 23145454 | CLAIMED, interval-certified | ζ odd sector at ½log7: 0 < λ₁ < 5.0e−19; **Davenport–Heilbronn**: positive for small support, exactly admissible negative witness at a = 9/5, so first loss scale in (½log2, 9/5); "first-kernel theorem" at a crossing | **1: this is a falsifier datum for comb-generic methods** (DH has functional equation, no Euler product) | NOT in corpus | KNOWN-adjacent / useful: an explicit falsifier family complementary to our Beurling/cΛ falsifiers — any proposed carrier must fail for DH at a ≤ 9/5. Recommend adding to index as falsifier test. |
| B9 | Z. Elston, *Weil positivity on finite windows across L-functions*, Zenodo 23163863 | CLAIMED/NUMÉRICO | Arb windows 2.38, 2.6, 2.99 (convention to check); two-sided brackets for functions without Euler product; Rédei L(5,29) vs L(χ5)L(χ29) indistinguishable | 1: the matched-pair observation says the window minimum sees only local invariants at this resolution | NOT in corpus | KNOWN; the matched pair is a small falsifier-style datum for "reads the comb" (prop. 1). |
| B10 | Tao Lin, *Structural lemmas for the first-prime window*, Zenodo 21807497; *Range of a finite-scale method…* | CLAIMED, part Lean 4 | J,E ∈ Q[τ]; rational absorption V + P₂ ≥ 0.69V; Weil constant c_L acts as global negative diagonal shift | none new | NOT in corpus | KNOWN (Paper 46 Theorem A territory). |
| B11 | Kramarenko-Byrd, restricted Weil forms series (Zenodo 19560981 & co.) | CLAIMED | threshold turn-on lemma, existence of minimisers, continuity of m(a), first-touch theorem | none (structure) | NOT in corpus | KNOWN (λ_A continuity = Paper 46 lem:contA; first-touch = phase 156/162). |
| B12 | X. Zhu, *A conditional lower bound for windowed Weil forms from sampling on the zeros*, arXiv 2608.24827 | CONDITIONAL | lower bound via frame/sampling on zeros | uses zeros | COVERED (L14) | KNOWN (zero information, cor:void). |
| B13 | M. Suzuki, *Weil's quadratic form via the screw function*, arXiv 2606.09096; *Hilbert space derived from the Weil distribution* (CJM 2025) ; Matsumoto–Suzuki M-functions | PROVED / CONDITIONAL | screw function g; localized positivity small t | 2 yes (screw = full FE), 3 reformulation | COVERED (L12, L36–L38) | KNOWN. |
| B14 | Connes–Consani, *Weil positivity and trace formula, the archimedean place* (Selecta 2021); *Spectral triples and ζ-cycles* (2023); CCM *Zeta zeros and prolate wave operators* (2024); *Zeta spectral triples* (2511.22755); Connes–van Suijlekom (2511.23257); CCM *q-series and the moment problem associated to local factors* (2024) | PROVED (archimedean / semilocal statements) | archimedean positivity on [λ⁻¹,λ] via prolate; semilocal trace formula | 2 partial (archimedean only, place by place), 4 yes but archimedean only | COVERED L05–L10, L39, L40, L42 | KNOWN. The q-series/moment paper (2024): check — corpus coverage of "moment problem associated to local factors" not separately listed; it is local-factor-only (place by place) so fails prop. 2. |
| B15 | Taira–Willems–Wrochna, *Large eigenvalues of the Connes–Moscovici operator*, arXiv 2609.32639 | PROVED (refereeable math) | logarithmic Weyl law, Bohr–Sommerfeld via WKB for P = −∂(x²−1)∂ − 4π²x² | none | NOT in corpus | IRRELEVANT for sign (archimedean spectral asymptotics); log in index as L41-family tool. |
| B16 | Bombieri 2000 (Milan J.), *Remarks on Weil's quadratic functional*; Bombieri–Lagarias 1999; Yoshida 1992 | PROVED (small support) | local positivity near 0 support via archimedean dominance | 4 only for small support | COVERED L01–L03 | KNOWN. No growing-support extension found in 2000–2026 literature other than certificates. |
| B17 | Burnol (Sonine spaces 2002; Two complete and minimal systems 2008; explicit formula/propagator 1998); X.-J. Li (prolate, Sonine, 2011; spectral interpretation 2010; orthogonal projection 2016) | PROVED / reformulation | Sonine/de Branges spaces, co-Poisson | 2 yes (co-Poisson = FE), no sign | COVERED L11, L34 | KNOWN. |
| B18 | Kamiya–Suzuki, *An attempt to interpret the Weil explicit formula from Beurling's spectral theory*, JNT 2011 (10.1016/j.jnt.2010.11.006); T. A. Wong, *Lower bounds for Weil's explicit formula via Selberg's trace formula* (thesis 2016); van Frankenhuijsen, *Weil positivity* (CUP 2014 chapter); Goldfeld 1994 spectral interpretation; Dye 2018 numerics for elliptic-curve L | reformulation / analogue | spectral synthesis; Selberg-side analogue | none | Kamiya, Wong NOT in corpus; others thin | KNOWN-family (L31 Selberg analogue; L05 spectral). Low. |
| B19 | Ueoka et al., *Local Toeplitz–Hankel criterion*, Zenodo 21762260; Li/Keiper numerics (Maślanka, Coffey, Arias de Reyna, Voros, Sekatskii, Schuster 2025 limitations, Fabbian 2026) | reformulation | Li coefficients' second differences | 3/4 no | COVERED L04 (family) | KNOWN, closed family. |
| B20 | Zenodo 2025–26 "proof" corpus (Benamara, Velez, Prodromov, Geiger "even dominance", Desogus L69, Ye "trace-compatible", Aksman L80, Shen "arithmetic bosonization", Kulik L56, Berenji, …) | unrefereed claims | each reduces to an unproved global positivity / identity step (e.g. Ye: "if … realized by a functorial Hilbert-space norm identity then Q ≥ 0") | — | partly L69, L80, L81 | KNOWN (L81 family). No hidden valid mechanism found at abstract depth. |

## C. Ranked "possible missing-object" section

None of the items has properties 1–4 simultaneously. Ranking by usefulness to row D, not by closeness to the object:

1. **Frontier update (B1 Mori ½log15, B5 Senke 77/64, B2 upper bound).** Not the object (dual-certificate class). Action:
   add to ROUTES-TRIED-INDEX (new L-entries) and Paper 46 related work; never claim a frontier beyond ½log15 without
   checking. Concrete first theorem we could attempt: none for the sign; an audit of Mori's certificate conventions
   (C² vs our L², primitive vs pole-neutral class) against def:PD, eq:nuw.
2. **Davenport–Heilbronn negative witness at a = 9/5 (B8).** A falsifier with functional equation but no Euler product,
   at an explicit window. First theorem to attempt: *any candidate carrier must be shown to fail on DH at a ≤ 9/5* —
   adopt as a mandatory falsifier test next to Beurling/cΛ/small-primes-deleted (sharpens BRIEF prop. 1 into a checkable
   test that also covers "reads the FE").
3. **Prolate-leakage clusters (B3) + Mori upper bound (B2).** Quantitative NO-GO data: ≥ m eigenvalues within
   e^{−πλ²}-scale of 0. Any positivity mechanism must have resolution e^{−πλ²}; first theorem: show a proposed carrier's
   built-in positivity (prop. 4) has slack ≤ e^{−4πμ}, else it is falsified by these test vectors.
4. **Chen's exact residual identity (B3)** — explicit formula + Poisson on summation-map images. It couples all primes with
   the global FE through Poisson summation (prop. 2 yes), but it is an exact identity (prop. 3 fails). Possible use:
   rewriting Π(T) on summation-map images of h*. Low.
5. **CCM q-series / moment problem for local factors (B14).** Place-by-place; fails prop. 2. Low.

**NEW-CANDIDATE: none.** Items new to the corpus but KNOWN in class: B1, B2, B3(partial), B4–B11, B15, B18 (Kamiya–Suzuki, Wong).

## A. Scanned items (OpenAlex sweep, 835 after homonym filter; year | authors | title | DOI)

| Year | Authors | Title | DOI |
|---|---|---|---|
| 1990 |  William Jay Sweet  |  The Metaplectic Case of the Weil-Siegel Formula  |  https://doi.org/10.13016/m27940w22  |
| 1991 |  Александр Семенович Холево  |  Conditionally positive-definite functions in quantum probability theory  |  https://doi.org/10.1007/bf01095976  |
| 1992 |  Louis de Branges  |  The convergence of Euler products  |  https://doi.org/10.1016/0022-1236(92)90103-p  |
| 1992 |  Yuval Z. Flicker  |  On the Symmetric Square: Applications of a Trace Formula  |  https://doi.org/10.1090/s0002-9947-1992-1041045-0  |
| 1993 |  Leonid Positselski  |  Nonhomogeneous quadratic duality and curvature  |  https://doi.org/10.1007/bf01087537  |
| 1993 |  R. Ranga Rao  |  On some explicit formulas in the theory of Weil representation  |  https://doi.org/10.2140/pjm.1993.157.335  |
| 1994 |  Dorian M. Goldfeld  |  A spectral interpretation of Weil's explicit formula  |  https://doi.org/10.1007/bfb0074041  |
| 1994 |  Louis de Branges  |  Quantization of the Gamma Function  |  https://doi.org/10.1007/978-1-4684-7415-2_2  |
| 1994 |  Ronald F. Probstein  |  Appendix B: Symbols  |  https://doi.org/10.1002/0471725137.app2  |
| 1994 |  Xian‐Jin Li  |  Hilbert spaces of entire functions and polynomials orthogonal on the unit circle  |  https://doi.org/10.4310/maa.1994.v1.n1.a3  |
| 1996 |  Christopher Towse  |  Weierstrass points on cyclic covers of the projective line  |  https://doi.org/10.1090/s0002-9947-96-01649-2  |
| 1996 |  Masanori Morishita  |  A Mean Value Theorem in Adele Geometry  |    |
| 1996 |  S. J. E. Radford, George Reiland, Bill Shillue  |  Site Test Interferometer  |  https://doi.org/10.1086/133745  |
| 1996 |  Yoichi Motohashi  |  A trace formula for the Picard group, I  |  https://doi.org/10.3792/pjaa.72.183  |
| 1997 |  Alain Connes A  |  Trace formula in noncommutative Geometry and the zeros of the Riemann zeta function  |  https://doi.org/10.5802/jedp.516  |
| 1997 |  Alain Connes A  |  Trace formula on the Adele Class Space and Weil Positivity  |  https://doi.org/10.4310/cdm.1997.v1997.n1.a1  |
| 1997 |  Éric Leichtnam, Paolo Piazza  |  The $b$-pseudodifferential calculus on Galois coverings and a higher Atiyah-Patodi-Singer index theorem  |  https://doi.org/10.24033/msmf.382  |
| 1997 |  Simon M. Veitch  |  Land Use Decisions and Site Selection: a GIS-based Method  |  https://doi.org/10.1007/978-1-5041-2869-8_33  |
| 1998 |  Alain Connes A  |  Trace formula in noncommutative geometry and the zeros of the Riemann zeta function  |  https://doi.org/10.48550/arxiv.math/9811068  |
| 1998 |  Gordon D. Simons, Yi‐Ching Yao  |  Approximating the inverse of a symmetric positive definite matrix  |  https://doi.org/10.1016/s0024-3795(98)10038-1  |
| 1998 |  Jean-François Burnol  |  The Explicit Formula and a Propagator  |  https://doi.org/10.48550/arxiv.math/9809119  |
| 1998 |  Jean-François Burnol  |  The Explicit Formula in simple terms  |  https://doi.org/10.48550/arxiv.math/9810169  |
| 1998 |  Jens Frankē  |  Harmonic analysis in weighted L2-spaces  |  https://doi.org/10.1016/s0012-9593(98)80015-3  |
| 1998 |  Michael McQuillan  |  Diophantine approximations and foliations  |  https://doi.org/10.1007/bf02698862  |
| 1998 |  Rolf‐Peter Holzapfel  |  Zeta dimension formula for picard modular cusp forms of neat natural congruence subgroups  |  https://doi.org/10.1007/bf02942561  |
| 1998 |  Takahiro Kume  |  Calculation of traces of theta series by means of the Weil representation  |  https://doi.org/10.1215/kjm/1250518060  |
| 1998 |  Tonghai Yang  |  An Explicit Formula for Local Densities of Quadratic Forms  |  https://doi.org/10.1006/jnth.1998.2258  |
| 1999 |  Alain Connes A  |  Trace formula in noncommutative geometry and the zeros of the Riemann zeta function  |  https://doi.org/10.1007/s000290050042  |
| 1999 |  Enrico Bombieri, Jeffrey C. Lagarias  |  Complements to Li's Criterion for the Riemann Hypothesis  |  https://doi.org/10.1006/jnth.1999.2392  |
| 1999 |  Gerd Laures  |  THE TOPOLOGICAL q-EXPANSION PRINCIPLE  |  https://doi.org/10.1016/s0040-9383(98)00019-6  |
| 1999 |  Jeffrey C. Lagarias  |  On a positivity property of the Riemann ξ-function  |  https://doi.org/10.4064/aa-89-3-217-234  |
| 1999 |  Joachim Hilgert, Karl‐Hermann Neeb  |  Positive definite spherical functions on Olshanskii domains  |  https://doi.org/10.1090/s0002-9947-99-02184-4  |
| 1999 |  Jorge Jiménez Urroz  |  Non-trivial Zeroes for Quadratic Twists of Hasse–Weil L-Functions  |  https://doi.org/10.1006/jnth.1999.2391  |
| 1999 |  Kazuya Katô, Nobushige Kurokawa, Takeshi Saito  |  Algebraic number theory  |  https://doi.org/10.1090/mmono/186/05  |
| 1999 |  Nicholas Katz, Peter Sarnak  |  Zeroes of zeta functions and symmetry  |  https://doi.org/10.1090/s0273-0979-99-00766-1  |
| 1999 |  Paula Beazley Cohen  |  A C * -dynamical system with Dedekind zeta partition function and spontaneous symmetry breaking  |  https://doi.org/10.5802/jtnb.236  |
| 1999 |  Sumio Yamada  |  Weil-Peterson [Petersson] convexity of the energy functional on classical and universal Teichmüller spaces  |  https://doi.org/10.4310/jdg/1214425025  |
| 1999 |  Tilmann Gneiting  |  On the Derivatives of Radial Positive Definite Functions  |  https://doi.org/10.1006/jmaa.1999.6434  |
| 1999 |  Tilmann Gneiting  |  Radial Positive Definite Functions Generated by Euclid's Hat  |  https://doi.org/10.1006/jmva.1998.1800  |
| 1999 |  W. Glunt, T. L. Hayden, Charles R. Johnson  |  Positive definite completions and determinant maximization  |  https://doi.org/10.1016/s0024-3795(98)10211-2  |
| 1999 |  Yuval Z. Flicker  |  Stable Bi-Period Summation Formula and Transfer Factors  |  https://doi.org/10.4153/cjm-1999-033-9  |
| 2000 |  Jean-François Burnol  |  Sur les formules explicites I : analyse invariante  |  https://doi.org/10.1016/s0764-4442(00)01687-6  |
| 2000 |  Jonathan Michael Borwein, David M. Bradley, Richard E. Crandall  |  Computational strategies for the Riemann zeta function  |  https://doi.org/10.1016/s0377-0427(00)00336-8  |
| 2000 |  Masahito Hayashi, Fuminori Sakaguchi  |  Subnormal operators regarded as generalized observables and compound-system-type normal extension related to $  |    |
| 2000 |  Stefano Stramigioli, Bernhard M. Maschke, Catherine Bidard  |  A Hamiltonian formulation of the dynamics of spatial mechanisms using Lie Groups and Screw Theory  |    |
| 2001 |  Aleksandar Ivić  |  On some conjectures and results for the Riemann zeta-function and Hecke series  |  https://doi.org/10.4064/aa99-2-2  |
| 2001 |  Jean-François Burnol  |  Quaternionic gamma functions and their logarithmic derivatives as spectral functions  |  https://doi.org/10.4310/mrl.2001.v8.n2.a9  |
| 2001 |  Jean-François Burnol  |  Sur certains espaces de Hilbert de fonctions entières, liés à la transformation de Fourier et aux fonctions L   |  https://doi.org/10.1016/s0764-4442(01)02036-5  |
| 2001 |  Philippe Biane, Jim Pitman, Marc Yor  |  Probability laws related to the Jacobi theta and Riemann zeta functions, and Brownian excursions  |  https://doi.org/10.1090/s0273-0979-01-00912-0  |
| 2001 |  Serge Lang  |  Explicit Formulas for Regularized Products and Series  |  https://doi.org/10.1007/978-1-4614-6325-2_4  |
| 2002 |  Georg Illies  |  Cramer functions and Guinand equations  |  https://doi.org/10.4064/aa105-2-1  |
| 2002 |  Jean-François Burnol  |  Sur les « espaces de Sonine » associés par de Branges à la transformation de Fourier  |  https://doi.org/10.1016/s1631-073x(02)02546-3  |
| 2002 |  Paul Ressel, Werner J. Ricker  |  Vector-valued positive definite functions, the Berg-Maserick theorem, and applications  |  https://doi.org/10.7146/math.scand.a-14375  |
| 2002 |  Sami Omar  |  Note on the Contribution of Low Zeros to Weil's Explicit Formula for Minimal Discriminants  |  https://doi.org/10.1112/s1461157000000656  |
| 2002 |  Serge Lang  |  Comments on non-references in Weil's works  |  https://doi.org/10.1515/dmvm-2002-0024  |
| 2002 |  Werner Mueller, Birgit Speh, Erez Lapid  |  On the absolute convergence of the spectral side of the Arthur trace formula for GL(n)  |  https://doi.org/10.48550/arxiv.math/0211030  |
| 2003 |  Daniele Guido, Tommaso Isola  |  Dimensions and singular traces for spectral triples, with applications to fractals  |  https://doi.org/10.1016/s0022-1236(03)00230-1  |
| 2003 |  Gerald H. Cliff, David McNeilly, Fernando Szechtman  |  Clifford and Mackey theory for Weil representations of symplectic groups  |  https://doi.org/10.1016/s0021-8693(03)00068-1  |
| 2003 |  Goran Golo, Arjan J. van der Schaft, Stefano Stramigioli  |  Hamiltonian Formulation of Planar Beams  |  https://doi.org/10.1016/s1474-6670(17)38882-1  |
| 2003 |  Jean-François Burnol  |  Des équations de Dirac et de Schrödinger pour la transformation de Fourier  |  https://doi.org/10.1016/s1631-073x(03)00223-1  |
| 2003 |  Jorge Stolfi, Luiz Henrique de Figueiredo  |  An Introduction to Affine Arithmetic  |  https://doi.org/10.5540/tema.2003.04.03.0297  |
| 2003 |  Juha‐Pekka Hotanen  |  Multidimensional site description of peatlands drained for forestry  |  https://doi.org/10.14214/sf.512  |
| 2003 |  Matthew A. Papanikolas, Niranjan Ramachandran  |  A Weil–Barsotti formula for Drinfeld modules  |  https://doi.org/10.1016/s0022-314x(02)00047-1  |
| 2003 |  Max Karoubi, Charles A. Weibel  |  Algebraic and real K-theory of Real varieties  |  https://doi.org/10.1016/s0040-9383(02)00069-1  |
| 2003 |  Robin de Jong  |  Arakelov invariants of Riemann surfaces  |  https://doi.org/10.48550/arxiv.math/0312357  |
| 2003 |  Siman Wong  |  Moments of the rank of elliptic curves  |  https://doi.org/10.48550/arxiv.math/0303369  |
| 2003 |  Stephen Samuel Gelbart, Stephen D. Miller  |  Riemann’s zeta function and beyond  |  https://doi.org/10.1090/s0273-0979-03-00995-9  |
| 2004 |  Alexandru Buium  |  Geometry of Fermat adeles  |  https://doi.org/10.1090/s0002-9947-04-03715-8  |
| 2004 |  Arjan J. van der Schaft  |  Port-Hamiltonian Systems: Network Modeling and Control of Nonlinear Physical Systems  |  https://doi.org/10.1007/978-3-7091-2774-2_9  |
| 2004 |  David Rodney Heath-Brown  |  The Average Analytic Rank of Elliptic Curves  |  https://doi.org/10.1215/s0012-7094-04-12235-3  |
| 2004 |  James Milne, Niranjan Ramachandran  |  Integral motives and special values of zeta functions  |  https://doi.org/10.1090/s0894-0347-04-00458-8  |
| 2004 |  K. Maślanka  |  An Explicit Formula Relating Stieltjes Constants and Li's Numbers  |  https://doi.org/10.48550/arxiv.math/0406312  |
| 2004 |  K. Maślanka  |  Li's criterion for the Riemann hypothesis - numerical approach  |    |
| 2004 |  R.S. de Jong  |  Explicit Arakelov geometry  |    |
| 2004 |  Salahoddin Shokranian  |  Twisted Trace Formula for Hecke Correspondences  |  https://doi.org/10.22323/1.013.0023  |
| 2004 |  Victor S. Miller  |  The Weil Pairing, and Its Efficient Calculation  |  https://doi.org/10.1007/s00145-004-0315-8  |
| 2004 |  Werner Ehm, Tilmann Gneiting, Donald Richards  |  Convolution roots of radial positive definite functions with compact support  |  https://doi.org/10.1090/s0002-9947-04-03502-0  |
| 2004 |  Xian‐Jin Li  |  Explicit formulas for Dirichlet and Hecke $L$-functions  |  https://doi.org/10.1215/ijm/1258138394  |
| 2005 |  Alan L. Carey, John Phillips, Adam Rennie  |  The local index formula in semifinite Von Neumann algebras I: Spectral flow  |  https://doi.org/10.1016/j.aim.2005.03.011  |
| 2005 |  Alan S. Edelman, Per‐Olof Persson  |  Numerical Methods for Eigenvalue Distributions of Random Matrices  |  https://doi.org/10.48550/arxiv.math-ph/0501068  |
| 2005 |  Francis Brown  |  Li's criterion and zero-free regions of L -functions  |  https://doi.org/10.1016/j.jnt.2004.07.016  |
| 2005 |  Germán Sierra  |  The Riemann zeros and the cyclic renormalization group  |  https://doi.org/10.1088/1742-5468/2005/12/p12006  |
| 2005 |  Jeffrey C. Lagarias  |  Zero spacing distributions for differenced L-functions  |  https://doi.org/10.4064/aa120-2-4  |
| 2005 |  Jørgen Ruud, Olav Gisle Tveiten  |  Measuring on Large-Scale Read-Intensive Web sites  |    |
| 2005 |  Maria Alessandra Ragusa, Atsushi Tachikawa  |  PARTIAL REGULARITY OF THE MINIMIZERS OF QUADRATIC FUNCTIONALS WITH VMO COEFFICIENTS  |  https://doi.org/10.1112/s002461070500699x  |
| 2005 |  Mark W. Coffey  |  New results on the Stieltjes constants: Asymptotic and exact evaluation  |  https://doi.org/10.1016/j.jmaa.2005.06.048  |
| 2005 |  Mark W. Coffey  |  Polygamma theory, the Li/Keiper constants, and validity of the Riemann Hypothesis  |  https://doi.org/10.48550/arxiv.math-ph/0507042  |
| 2005 |  Martin Tompa, Nan Li, Timothy L. Bailey  |  Assessing computational tools for the discovery of transcription factor binding sites  |  https://doi.org/10.1038/nbt1053  |
| 2005 |  Ming Kang, Qigang Ye, Hongwen Huang  |  Genetic Consequence of Restricted Habitat and Population Decline in Endangered Isoetes sinensis (Isoetaceae)  |  https://doi.org/10.1093/aob/mci277  |
| 2005 |  Muharem Avdispahić, Lejla Smajlović  |  Explicit formula for a fundamental class of functions  |  https://doi.org/10.36045/bbms/1133793345  |
| 2005 |  Ralf Meyer  |  On a representation of the idele class group related to primes and zeros of L-functions  |  https://doi.org/10.1215/s0012-7094-04-12734-4  |
| 2005 |  Robin de Jong  |  Arakelov invariants of Riemann surfaces  |    |
| 2005 |  Robin de Jong  |  Arakelov invariants of Riemann surfaces  |  https://doi.org/10.4171/dm/190  |
| 2005 |  Takeshi Hirai, Etsuko Hirai  |  Positive definite class functions on a topological group and characters of factor representations  |  https://doi.org/10.1215/kjm/1250281995  |
| 2006 |    |    |  https://doi.org/10.1090/bull/2006-43-02  |
| 2006 |  Ali E. Özlük, C. Snyder  |  On the One-Level Density Conjecture for Quadratic Dirichlet L-Functions  |  https://doi.org/10.4153/cjm-2006-034-9  |
| 2006 |  Andrew H. Knightly, Charles H. Li  |  A relative trace formula proof of the Petersson trace formula  |  https://doi.org/10.4064/aa122-3-5  |
| 2006 |  Andrew Merchant, Michael Tausz, Stefan K. Arndt  |  Cyclitols and carbohydrates in leaves and roots of 13 Eucalyptus species suggest contrasting physiological res  |  https://doi.org/10.1111/j.1365-3040.2006.01577.x  |
| 2006 |  Benoît Jacob  |  Bost-Connes type systems for function fields  |  https://doi.org/10.48550/arxiv.math/0602554  |
| 2006 |  David Brydges, Anna Talarczyk  |  Finite range decompositions of positive-definite functions  |  https://doi.org/10.1016/j.jfa.2006.03.008  |
| 2006 |  Gérard Letac, Hélène Massam  |  Extremal rays and duals for cones of positive definite matrices with prescribed zeros  |  https://doi.org/10.1016/j.laa.2006.03.017  |
| 2006 |  Jean-François Burnol  |  Spacetime Causality in the Study of the Hankel Transform  |  https://doi.org/10.1007/s00023-006-0274-8  |
| 2006 |  Kiran S. Kedlaya  |  Fourier transforms and $p$-adic ‘Weil II’  |  https://doi.org/10.1112/s0010437x06002338  |
| 2006 |  Pedro Freitas  |  A LI-TYPE CRITERION FOR ZERO-FREE HALF-PLANES OF RIEMANN'S ZETA FUNCTION  |  https://doi.org/10.1112/s0024610706022599  |
| 2006 |  Sergio A Albeverio, Christof Cebulla  |  Müntz formula and zero free regions for the Riemann zeta function  |  https://doi.org/10.1016/j.bulsci.2006.03.002  |
| 2006 |  Yuri I. Manin  |  The notion of dimension in geometry and algebra  |  https://doi.org/10.1090/s0273-0979-06-01081-0  |
| 2007 |  Alain Connes A, Caterina Consani B, Matilde Marcolli  |  Noncommutative geometry and motives: The thermodynamics of endomotives  |  https://doi.org/10.1016/j.aim.2007.03.006  |
| 2007 |  Alain Connes A, Caterina Consani B, Matilde Marcolli  |  The Weil proof and the geometry of the adeles class space  |  https://doi.org/10.48550/arxiv.math/0703392  |
| 2007 |  Alan L. Carey, Adam Rennie, Александр Андреевич Седаев  |  The Dixmier trace and asymptotics of zeta functions  |  https://doi.org/10.1016/j.jfa.2007.04.011  |
| 2007 |  Benoît Jacob  |  Bost–Connes type systems for function fields  |  https://doi.org/10.4171/jncg/4  |
| 2007 |  Caterina Consani B  |  Noncommutative geometry and motives (a quoi servent les endomotifs?)  |  https://doi.org/10.48550/arxiv.0711.0477  |
| 2007 |  Caterina Consani B, Matilde Marcolli  |  Archimedean cohomology revisited  |  https://doi.org/10.1007/978-3-8348-0352-8_5  |
| 2007 |  Erik Christensen, Cristina S. Ivan, Michel L. Lapidus  |  Dirac operators and spectral triples for some fractal sets built on curves  |  https://doi.org/10.1016/j.aim.2007.06.009  |
| 2007 |  Fumihiro Satō  |  Quadratic maps and non-prehomogeneous local functional eqations  |  https://doi.org/10.14992/00008658  |
| 2007 |  Germán Sierra  |  H=xp with interaction and the Riemann zeros  |  https://doi.org/10.1016/j.nuclphysb.2007.03.049  |
| 2007 |  Jack Hardisty  |  Assessment of Tidal Current Resources: Case Studies of Estuarine and Coastal Sites  |  https://doi.org/10.1177/0958305x0701800204  |
| 2007 |  Jean-François Burnol  |  Entrelacement de co-Poisson  |  https://doi.org/10.5802/aif.2268  |
| 2007 |  Jeffrey C. Lagarias  |  Li coefficients for automorphic L -functions  |  https://doi.org/10.5802/aif.2311  |
| 2007 |  Marcelo Laca, Nadia S. Larsen, Sergey Neshveyev  |  Phase transition in the Connes–Marcolli $\mathrm{GL}_2$-system  |  https://doi.org/10.4171/jncg/12  |
| 2007 |  Mark W. Coffey  |  The theta-Laguerre calculus formulation of the Li/Keiper constants  |  https://doi.org/10.1016/j.jat.2006.10.006  |
| 2007 |  Michael Angelo B. Promentilla, Takahisa Furuichi, Kazuei Ishii  |  A fuzzy analytic network process for multi-criteria evaluation of contaminated site remedial countermeasures  |  https://doi.org/10.1016/j.jenvman.2007.03.013  |
| 2007 |  Philippe Flajolet, Linas Vepštas  |  On differences of zeta values  |  https://doi.org/10.1016/j.cam.2007.07.040  |
| 2007 |  Stephanie Barr, Leigh, Katharine E., Dunbar, Brian H.  |  Green schools that teach: identifying attributes of whole-school sustainability  |  https://doi.org/10.25675/3.021229  |
| 2008 |  C.M. Hayman  |  The Weil conjectures  |    |
| 2008 |  Frédéric Paugam  |  Spectral symmetries of zeta functions  |  https://doi.org/10.48550/arxiv.0803.0199  |
| 2008 |  Gabriele Nebe  |  Finite Weil representations and associated Hecke algebras  |  https://doi.org/10.1016/j.jnt.2008.09.015  |
| 2008 |  Germán Sierra  |  A quantum mechanical model of the Riemann zeros  |  https://doi.org/10.1088/1367-2630/10/3/033016  |
| 2008 |  Giedrius Alkauskas  |  Integral transforms of the Minkowski question mark function  |    |
| 2008 |  Jean-François Burnol  |  Two complete and minimal systems associated with the zeros of the Riemann zeta function  |  https://doi.org/10.5802/jtnb.434  |
| 2008 |  Kristine Ey  |  On the Representation of Pn-positive definite Functions and Applications  |    |
| 2008 |  Krystian Eitner, Uwe Koch, Tomasz Gawęda  |  Self-concerted hydrophobicity scale based on the ACDlogP of a combination of 8000 tripeptides and its applicat  |    |
| 2008 |  Marcelo Laca, Nadia S. Larsen, Sergey Neshveyev  |  On Bost–Connes type systems for number fields  |  https://doi.org/10.1016/j.jnt.2008.09.008  |
| 2008 |  Mark W. Coffey  |  Asymptotic estimation of 𝜉⁽²ⁿ⁾(1/2): On a conjecture of Farmer and Rhoades  |  https://doi.org/10.1090/s0025-5718-08-02167-4  |
| 2008 |  Mark W. Coffey  |  New results concerning power series expansions of the Riemann xi function and the Li/Keiper constants  |  https://doi.org/10.1098/rspa.2007.0212  |
| 2008 |  Oswaldo Velásquez Castañón  |  Sur la répartition des zéros de certaines fonctions méromorphes liées à la fonction zêta de Riemann  |  https://doi.org/10.70675/e388472ez2d29z4d0ez981ezc345cc65dc17  |
| 2009 |  Adrian R. Kitson  |  On the zero-point energy of elliptic-cyliindrical and spheroidal boundaries : a thesis presented in partial fu  |    |
| 2009 |  Alain Connes A, Caterina Consani B, Matilde Marcolli  |  The Weil Proof and the Geometry of the Adelès Class Space  |  https://doi.org/10.1007/978-0-8176-4745-2_8  |
| 2009 |  Corinna C. Maass  |  Dynamics of levitated granular gases  |    |
| 2009 |  Corinna C. Maass  |  Dynamik levitierter granularer Gase  |    |
| 2009 |  Fumio Hiai, Dėnes Petz  |  Riemannian metrics on positive definite matrices related to means  |  https://doi.org/10.1016/j.laa.2009.01.025  |
| 2009 |  Giedrius Alkauskas  |  Generating and zeta functions, structure, spectral and analytic properties of the moments of the Minkowski que  |  https://doi.org/10.2140/involve.2009.2.121  |
| 2009 |  Giedrius Alkauskas  |  THE MOMENTS OF MINKOWSKI QUESTION MARK FUNCTION: THE DYADIC PERIOD FUNCTION  |  https://doi.org/10.1017/s0017089509990152  |
| 2009 |  Mark W. Coffey  |  Summation properties of the ηj and Li constants  |  https://doi.org/10.1016/j.cam.2009.02.034  |
| 2009 |  Nils R. Scheithauer  |  The Weil Representation of and Some Applications  |  https://doi.org/10.1093/imrn/rnn166  |
| 2009 |  Norihiko Minami  |  Meromorphicity of some deformed multivariable zeta functions for $F_1$-schemes  |  https://doi.org/10.48550/arxiv.0910.3879  |
| 2009 |  Philippe Lebacque, Zykin, Alexey  |  On logarithmic derivatives of zeta functions in families of global fields  |    |
| 2009 |  Richard J. Szabo, Alessandro Valentino  |  Ramond-Ramond Fields, Fractional Branes and Orbifold Differential K-Theory  |  https://doi.org/10.1007/s00220-009-0975-1  |
| 2009 |  Sami Omar, Kamel Mazhouda  |  The Li criterion and the Riemann hypothesis for the Selberg class II  |  https://doi.org/10.1016/j.jnt.2009.08.012  |
| 2009 |  Scott A. Wolpert  |  The Weil–Petersson metric geometry  |  https://doi.org/10.4171/055-1/2  |
| 2009 |  Stephen Lichtenbaum  |  The Weil-étale topology for number rings  |  https://doi.org/10.4007/annals.2009.170.657  |
| 2010 |  Alain Connes A, Caterina Consani  |  Schemes over 𝔽 1 and zeta functions  |  https://doi.org/10.1112/s0010437x09004692  |
| 2010 |  Alain Connes A, Caterina Consani B  |  From monoids to hyperstructures: in search of an absolute arithmetic  |  https://doi.org/10.1515/9783110226133.147  |
| 2010 |  Dariusz Cichoń, Jan Stochel, Franciszek Hugon Szafraniec  |  Extending positive definiteness  |  https://doi.org/10.1090/s0002-9947-2010-05268-7  |
| 2010 |  Donal F. Connon  |  Some possible approaches to the Riemann Hypothesis via the Li/Keiper constants  |  https://doi.org/10.48550/arxiv.1002.3484  |
| 2010 |  Goele Cornelissen, K. Landsman, Walter D. van Suijlekom  |  The flashes of insight never came for free : interview with Alain Connes  |    |
| 2010 |  Hung M. Bui, Micah B. Milinovich, N. Ng  |  A note on the gaps between consecutive zeros of the Riemann zeta-function  |  https://doi.org/10.1090/s0002-9939-2010-10443-4  |
| 2010 |  Jan Hendrik Bruinier, Stephen S. Kudla, Tonghai Yang  |  Faltings heights of big CM cycles and derivatives of L-functions  |  https://doi.org/10.48550/arxiv.1008.1669  |
| 2010 |  Jan Hendrik Bruinier, Tonghai Yang  |  CM values of automorphic Green functions on orthogonal groups over totally real fields  |  https://doi.org/10.48550/arxiv.1004.3720  |
| 2010 |  Jean Bellissard, Matilde Marcolli, Kamran Reihani  |  Dynamical Systems on Spectral Metric Spaces  |  https://doi.org/10.48550/arxiv.1008.4617  |
| 2010 |  Manfréd M. Fischer  |  A spatial Mankiw–Romer–Weil model: theory and evidence  |  https://doi.org/10.1007/s00168-010-0384-6  |
| 2010 |  Mark W. Coffey  |  Polygamma theory, the Li/Keiper constants and the Li criterion for the Riemann hypothesis  |  https://doi.org/10.1216/rmj-2010-40-6-1841  |
| 2010 |  Philip E. Hoggan  |  How specific exponential type orbitals recently became a viable basis set choice in NMR shielding tensor calcu  |  https://doi.org/10.48550/arxiv.1010.5425  |
| 2010 |  Sami Omar, Saber Bouanani  |  Li's criterion and the Riemann hypothesis for function fields  |  https://doi.org/10.1016/j.ffa.2010.09.004  |
| 2010 |  Shandra Devi Ridhmadhantia  |  Analisis pengaruh surprise earning announcement terhadap return saham dan dividend payout dengan uji beda posi  |    |
| 2010 |  Siegfried Böcherer, Neil Dummigan, Rainer Schulze‐Pillot  |  Yoshida lifts and Selmer groups  |  https://doi.org/10.48550/arxiv.1012.5817  |
| 2010 |  Steven Spallone  |  Stable Trace Formulas and Discrete Series Representations  |  https://doi.org/10.48550/arxiv.1010.4897  |
| 2010 |  Xian‐Jin Li  |  A spectral interpretation for the explicit formula in the theory of prime numbers  |  https://doi.org/10.1007/s11425-009-0215-3  |
| 2011 |  Anton A. Gerasimov, Dimitri Lebedev, Сергей Викторович Облезин  |  Archimedean $L$-factors and topological field theories I  |  https://doi.org/10.4310/cntp.2011.v5.n1.a2  |
| 2011 |  Charles Knessl, Mark W. Coffey  |  An asymptotic form for the Stieltjes constants 𝛾_{𝑘}(𝑎) and for a sum 𝑆ᵧ(𝑛) appearing under the Li criterion  |  https://doi.org/10.1090/s0025-5718-2011-02497-x  |
| 2011 |  Denis-Charles Cisinski, Gonçalo Tabuada  |  LEFSCHETZ AND HIRZEBRUCH-RIEMANN-ROCH FORMULAS VIA NONCOMMUTATIVE MOTIVES  |    |
| 2011 |  Denis-Charles Cisinski, Gonçalo Tabuada  |  Lefschetz and Hirzebruch-Riemann-Roch formulas via noncommutative motives  |  https://doi.org/10.48550/arxiv.1111.0257  |
| 2011 |  Joachim Mahnkopf  |  Conjugation of Hilbert modular forms and trace formula  |  https://doi.org/10.48550/arxiv.1102.2316  |
| 2011 |  Juan Arias de Reyna  |  Asymptotics of Keiper-Li coefficients  |  https://doi.org/10.7169/facm/1317045228  |
| 2011 |  Kamel Mazhouda  |  The Saddle-Point Method and the Li Coefficients  |  https://doi.org/10.4153/cmb-2011-016-6  |
| 2011 |  Matilde Marcolli, Jorge Plazas, R. Sujatha  |  Introduction to motives  |  https://doi.org/10.4171/008-1/2  |
| 2011 |  Michel R. P. Planat, Patrick Solé, Sami Omar  |  Riemann hypothesis and quantum mechanics  |  https://doi.org/10.1088/1751-8113/44/14/145203  |
| 2011 |  Norihiko Minami  |  ON THE CONNES-CONSANI-SOULE TYPE ZETA FUNCTION FOR $\mathbb{F}_{1}$-SCHEMES (Transformation Groups and Surgery  |    |
| 2011 |  Rick K. Beatson, Wolfgang zu Castell, Yuan Xu  |  A Pólya criterion for (strict) positive definiteness on the sphere  |  https://doi.org/10.48550/arxiv.1110.2437  |
| 2011 |  Sergio A Albeverio, Claudio Cacciapuoti  |  The Riemann zeta in terms of the dilogarithm  |  https://doi.org/10.48550/arxiv.1101.4786  |
| 2011 |  Steven J. Miller, Siman Wong  |  Moments of the Rank of Elliptic Curves  |  https://doi.org/10.4153/cjm-2011-037-7  |
| 2011 |  Steven Spallone  |  ON THE TRACE FORMULA APPROACH TO DISCRETE SERIES MULTIPLICITIES (Automorphic forms, trace formulas and zeta fu  |    |
| 2011 |  Tobias Finis, Erez Lapid, Werner Müller  |  On the spectral side of Arthur's trace formula --- absolute convergence  |  https://doi.org/10.4007/annals.2011.174.1.5  |
| 2011 |  Xian‐Jin Li  |  ON THE EXPLICIT FORMULA IN THE THEORY OF PRIME NUMBERS  |  https://doi.org/10.1142/s1793042112500327  |
| 2011 |  Xian‐Jin Li  |  Prolate spheroidal wave functions, Sonine spaces, and the Riemann zeta function  |  https://doi.org/10.1016/j.jmaa.2011.11.068  |
| 2011 |  Yuichi Kamiya, Masatoshi Suzuki  |  An attempt to interpret the Weil explicit formula from Beurling's spectral theory  |  https://doi.org/10.1016/j.jnt.2010.11.006  |
| 2011 |  範彦 南  |  On the Connes-Consani-Soule type zeta function for F1-schemes (変換群と手術理論--RIMS研究集会報告集)  |    |
| 2012 |  ALBAIYAT, ABDULKHALE  |  On the Extension of the Bessel Functions of the First Kind with Applications to some Mathematical Integrals an  |    |
| 2012 |  Andrew Droll  |  Variations of Li's criterion for an extension of the Selberg class  |    |
| 2012 |  Andrew H. Knightly, C. Li  |  Kuznetsov’s trace formula and the Hecke eigenvalues of Maass forms  |  https://doi.org/10.1090/s0065-9266-2012-00673-3  |
| 2012 |  Brian Charlesworth  |  The Effects of Deleterious Mutations on Evolution at Linked Sites  |  https://doi.org/10.1534/genetics.111.134288  |
| 2012 |  Brian Conrad  |  Weil and Grothendieck approaches to adelic points  |  https://doi.org/10.4171/lem/58-1-3  |
| 2012 |  Charles H. Li, Andrew H. Knightly  |  Kuznetsov's trace formula and the Hecke eigenvalues of Maass forms  |  https://doi.org/10.48550/arxiv.1202.0189  |
| 2012 |  Dominique Guillot, Bala Rajaratnam  |  Retaining positive definiteness in thresholded matrices  |  https://doi.org/10.1016/j.laa.2012.01.013  |
| 2012 |  Eric M. Thompson, Laurie Gaskins Baise, Yasuo Tanaka  |  A taxonomy of site response complexity  |  https://doi.org/10.1016/j.soildyn.2012.04.005  |
| 2012 |  Hafedh Herichi, Michel L Lapidus  |  Riemann zeros and phase transitions via the spectral operator on fractal strings  |  https://doi.org/10.1088/1751-8113/45/37/374005  |
| 2012 |  Kamel Mazhouda  |  On the Li coefficients for the Dirichlet $$L$$ -functions  |  https://doi.org/10.1007/s00605-012-0436-3  |
| 2012 |  Masatoshi Suzuki  |  A canonical system of differential equations arising from the Riemann zeta-function (Functions in Number Theor  |    |
| 2012 |  Mauro Spera  |  THE RIEMANN ZETA FUNCTION AS AN EQUIVARIANT DIRAC INDEX  |  https://doi.org/10.1142/s0219887812500715  |
| 2012 |  Sergio A Albeverio, Claudio Cacciapuoti  |  The Riemann zeta in terms of the dilogarithm  |  https://doi.org/10.1016/j.jnt.2012.06.002  |
| 2012 |  Shamgar Gurevich, Ronny Hadani  |  The Weil representation in characteristic two  |  https://doi.org/10.1016/j.aim.2012.03.008  |
| 2012 |  Stefan Gerhold  |  Can There Be an Explicit Formula for Implied Volatility?  |  https://doi.org/10.2139/ssrn.2179924  |
| 2012 |  Stephen Obrochta, Hiroko Miyahara, Yūsuke Yokoyama  |  A re-examination of evidence for the North Atlantic “1500-year cycle” at Site 609  |  https://doi.org/10.1016/j.quascirev.2012.08.008  |
| 2012 |  Sug Woo Shin  |  Abelian varieties and Weil representations  |  https://doi.org/10.2140/ant.2012.6.1719  |
| 2012 |  Tim, Vladimir Dokchitser  |  ELLIPTIC CURVES WITH ALL QUADRATIC TWISTS OF POSITIVE RANK  |    |
| 2012 |  Zhiyong Yu  |  Equivalent cost functionals and stochastic linear quadratic optimal control problems  |  https://doi.org/10.1051/cocv/2011206  |
| 2012 |  正俊 鈴木  |  A canonical system of differential equations arising from the Riemann zeta-function  |  https://doi.org/10.48550/arxiv.1204.1827  |
| 2013 |  Abhishek Saha  |  On ratios of Petersson norms for Yoshida lifts  |  https://doi.org/10.1515/forum-2013-0093  |
| 2013 |  Alina Bucur, Kiran S. Kedlaya  |  An application of the effective Sato-Tate conjecture  |  https://doi.org/10.48550/arxiv.1301.0139  |
| 2013 |  Amin Espah Borujeni, Anirudh S. Channarasappa, Howard M. Salis  |  Translation rate is controlled by coupled trade-offs between site accessibility, selective RNA unfolding and s  |  https://doi.org/10.1093/nar/gkt1139  |
| 2013 |  Andrew R. Booker, M. Krishnamurthy  |  Weil's Converse Theorem with Poles  |  https://doi.org/10.1093/imrn/rnt127  |
| 2013 |  Chien‐Hao Liu, Shing–Tung Yau  |  A mathematical theory of D-string world-sheet instantons, I: Compactness of the stack of $Z$-semistable Fourie  |  https://doi.org/10.48550/arxiv.1302.2054  |
| 2013 |  Dave Anderson, Sam Payne  |  Operational K-theory  |  https://doi.org/10.48550/arxiv.1301.0425  |
| 2013 |  Jayce Robert Getz, P. Edward Herman  |  A nonabelian trace formula  |  https://doi.org/10.48550/arxiv.1312.3611  |
| 2013 |  Karim Belabas, Eduardo Friedman  |  Computing the residue of the Dedekind zeta function  |  https://doi.org/10.48550/arxiv.1305.0035  |
| 2013 |  Mahesh Agarwal, Krzysztof Klosin  |  Yoshida lifts and the Bloch–Kato conjecture for the convolution L -function  |  https://doi.org/10.1016/j.jnt.2013.01.009  |
| 2013 |  Masatoshi Suzuki  |  A family of deformations of the Riemann xi-function  |  https://doi.org/10.4064/aa157-3-1  |
| 2013 |  Matthew C. Lettington  |  A trio of Bernoulli relations, their implications for the Ramanujan polynomials and the special values of the   |  https://doi.org/10.4064/aa158-1-1  |
| 2013 |  Matthew J. Gursky, Jeff Viaclovsky  |  Rigidity and stability of Einstein metrics for quadratic curvature functionals  |  https://doi.org/10.1515/crelle-2013-0024  |
| 2013 |  Rosario Gennaro, Craig Gentry, Bryan Jeffery Parno  |  Quadratic Span Programs and Succinct NIZKs without PCPs  |  https://doi.org/10.1007/978-3-642-38348-9_37  |
| 2013 |  Sarah Chisholm, Alyson Deines, Линг Лонг  |  ρ — Adic Analogues of Ramanujan Type Formulas for 1/π  |  https://doi.org/10.3390/math1010009  |
| 2013 |  Sergey K. Sekatskii  |  An arithmetic interpretation of generalized Li's criterion  |  https://doi.org/10.48550/arxiv.1305.1421  |
| 2013 |  Sergey K. Sekatskii  |  Generalized Bombieri - Lagarias' theorem and generalized Li's criterion  |  https://doi.org/10.48550/arxiv.1304.7895  |
| 2013 |  Shunsuke Yamana  |  The Siegel–Weil formula for unitary groups  |  https://doi.org/10.2140/pjm.2013.264.235  |
| 2013 |  Soma Purkait  |  Explicit application of Waldspurger’s theorem  |  https://doi.org/10.1112/s1461157013000144  |
| 2013 |  Tim Adamo, Michael Groechenig  |  Moduli stacks of maps for supermanifolds  |  https://doi.org/10.4310/atmp.2013.v17.n6.a3  |
| 2013 |  Wolfgang Martin Wieland  |  Hamiltonian spinfoam gravity  |  https://doi.org/10.1088/0264-9381/31/2/025002  |
| 2013 |  Yang‐Hui He, Vishnu Jejjala, Djordje Minić  |  On the Physics of the Riemann Zeros  |  https://doi.org/10.1088/1742-6596/462/1/012036  |
| 2013 |  Симагин Дмитрий Николаевич, Литовка Юрий Владимирович  |  Процесс получения наномодифицированных цинковых покрытий с повышенной равномерностью  |    |
| 2014 |  Alan L. Carey, Victor Gayral, Jessica Phillips  |  Spectral Flow for Nonunital Spectral Triples  |  https://doi.org/10.4153/cjm-2014-042-x  |
| 2014 |  André Voros  |  Zeta functions over zeros of Zeta functions and an exponential-asymptotic view of the Riemann Hypothesis  |  https://doi.org/10.48550/arxiv.1403.4558  |
| 2014 |  Anne‐Marie Aubert, Tomasz Przebinda  |  A reverse engineering approach to the Weil representation  |  https://doi.org/10.2478/s11533-014-0428-8  |
| 2014 |  Fabio Cipriani, Daniele Guido, Tommaso Isola  |  Spectral triples for the Sierpinski gasket  |  https://doi.org/10.1016/j.jfa.2014.02.013  |
| 2014 |  Giuseppe Iurato  |  The early historical roots of Lee-Yang theorem  |  https://doi.org/10.48550/arxiv.1410.6450  |
| 2014 |  Hernán Charosky, María Inés Vásquez, Nicolás Dassen  |  Complaint as Positive Energy: The Experience of "The Worst Bureaucratic Procedure of My Life" Contest in Boliv  |  https://doi.org/10.18235/0010601  |
| 2014 |  Johanna F. Ziegel  |  Convolution roots and differentiability of isotropic positive definite functions on spheres  |  https://doi.org/10.1090/s0002-9939-2014-11989-7  |
| 2014 |  John Cloutier  |  Simulation and Control of a Ball Screw System Actuated by a Stepper Motor with Feedback  |    |
| 2014 |  Koen Thas  |  Hyperfield extensions, characteristic one and the Connes-Consani plane connection  |  https://doi.org/10.48550/arxiv.1407.0607  |
| 2014 |  Konrad Pilch  |  Noncommutative geometry methods in number theory.  |    |
| 2014 |  Machiel van Frankenhuijsen  |  Weil positivity  |  https://doi.org/10.1017/cbo9781107238992.006  |
| 2014 |  Marco Maculan  |  Height on GIT quotients and Kempf-Ness theory  |  https://doi.org/10.48550/arxiv.1411.6786  |
| 2014 |  Marco Matassa  |  Non-commutative integration for spectral triples associated to quantum groups  |    |
| 2014 |  Ming-Hsuan Kang, Wen-Ching Winnie Li  |  Zeta functions of complexes arising from PGL(3)  |  https://doi.org/10.1016/j.aim.2013.12.033  |
| 2014 |  Niranjan Ramachandran  |  Zeta functions, Grothendieck groups, and the Witt ring  |  https://doi.org/10.1016/j.bulsci.2014.11.004  |
| 2014 |  Paul Fili, Charles L. Samuels  |  On the non-Archimedean metric Mahler measure  |  https://doi.org/10.48550/arxiv.1408.5084  |
| 2014 |  Sami Omar, Raouf Ouni, Kamel Mazhouda  |  On the Li Coefficients for the Hecke L-functions  |  https://doi.org/10.1007/s11040-014-9141-x  |
| 2014 |  Sergey K. Sekatskii  |  First applications of generalized Li's criterion to study the Riemann zeta-function zeroes location  |  https://doi.org/10.48550/arxiv.1404.7276  |
| 2014 |  Sergey K. Sekatskii  |  Generalized Bombieri–Lagarias’ Theorem and Generalized Li’s Criterion with its Arithmetic Interpretation  |  https://doi.org/10.1007/s11253-014-0940-9  |
| 2014 |  Sezen Bozyiğit, Erdem Akkan  |  Linking Universities to the Target Market via Web Sites: A Content Analysis of Turkish Private Universities’ W  |  https://doi.org/10.1016/j.sbspro.2014.07.070  |
| 2015 |  Adrian Barquero-Sanchez, Riad Masri  |  The Chowla–Selberg formula for abelian CM fields and Faltings heights  |  https://doi.org/10.1112/s0010437x15007629  |
| 2015 |  Alain Connes A, Caterina Consani B  |  Geometry of the arithmetic site  |  https://doi.org/10.48550/arxiv.1502.05580  |
| 2015 |  Alain Connes A, Caterina Consani B  |  The Scaling Site  |    |
| 2015 |  Alain Connes A, Caterina Consani B  |  The scaling site  |  https://doi.org/10.1016/j.crma.2015.09.027  |
| 2015 |  Alain Connes A, Caterina Consani B  |  The Scaling Site  |  https://doi.org/10.48550/arxiv.1507.05818  |
| 2015 |  Aline Suter, Tobias Johannes Dietrich, Matthias Maier  |  MR findings associated with positive distraction of the hip joint achieved by axial traction  |  https://doi.org/10.1007/s00256-015-2099-3  |
| 2015 |  Eugene Ha, Victor Kasatkin  |  Fredholm modules and the Beilinson-Bloch regulator  |  https://doi.org/10.48550/arxiv.1509.02864  |
| 2015 |  Francis Brown, Sami Omar  |  Li's criterion for Epstein zeta functions, generalization of Kronecker's limit formula and the Gauss problem  |  https://doi.org/10.1016/j.jnt.2015.06.008  |
| 2015 |  Guilherme França, André LeClair  |  Transcendental equations satisfied by the individual zeros of Riemann $\zeta$, Dirichlet and modular $L$-funct  |  https://doi.org/10.4310/cntp.2015.v9.n1.a1  |
| 2015 |  Jayce Robert Getz, P. Edward Herman  |  A nonabelian trace formula  |  https://doi.org/10.1186/s40687-015-0025-x  |
| 2015 |  José L. Strapasson  |  Implementação de potenciais arbitrários na Simulação Direta de Monte Carlo  |    |
| 2015 |  Katrina Honigs  |  Derived Equivalent Varieties and their Zeta Functions  |    |
| 2015 |  Koen Thas  |  A taste of Weil theory in characteristic one  |  https://doi.org/10.48550/arxiv.1507.06480  |
| 2015 |  Li Xian  |  On Weil's explicit formula  |    |
| 2015 |  Magnus Goffeng, Bram Mesland  |  Spectral triples and finite summability on Cuntz–Krieger algebras  |  https://doi.org/10.4171/dm/487  |
| 2015 |  Marcus Robinson, Irena Swanson  |  Explicit Hilbert–Kunz functions of 2 × 2 determinantal rings  |  https://doi.org/10.2140/pjm.2015.275.433  |
| 2015 |  Marek Bożejko, Wojciech Bożejko  |  Generalized Gaussian processes and relations with random matrices and positive definite functions on permutati  |  https://doi.org/10.1142/s0219025715500204  |
| 2015 |  Nathan C. Ryan, Gonzalo Tornaría  |  Formulas for central values of twisted spin 𝐿-functions attached to paramodular forms  |  https://doi.org/10.1090/mcom/2988  |
| 2015 |  Nugzar Makhaldiani  |  Hadronization and solvable models of renormdynamics of QCD  |  https://doi.org/10.22323/1.225.0040  |
| 2015 |  Peter J. Forrester, Anthony Mays  |  Finite-size corrections in random matrix theory and Odlyzko’s dataset for the Riemann zeros  |  https://doi.org/10.1098/rspa.2015.0436  |
| 2015 |  Raf Cluckers, Georges Comte, François Loeser  |  NON-ARCHIMEDEAN YOMDIN–GROMOV PARAMETRIZATIONS AND POINTS OF BOUNDED HEIGHT  |  https://doi.org/10.1017/fmp.2015.4  |
| 2015 |  Shanjian Tang  |  Dynamic Programming for General Linear Quadratic Optimal Stochastic Control with Random Coefficients  |  https://doi.org/10.1137/140979940  |
| 2015 |  Ted Chinburg, G. Pappas, M. J. Taylor  |  Higher adeles and non-abelian Riemann–Roch  |  https://doi.org/10.1016/j.aim.2015.03.030  |
| 2015 |  Werner Mueller  |  Asymptotics of automorphic spectra and the trace formula  |  https://doi.org/10.48550/arxiv.1509.06645  |
| 2015 |  Zhichao Miao, Éric Westhof  |  A Large-Scale Assessment of Nucleic Acids Binding Site Prediction Programs  |  https://doi.org/10.1371/journal.pcbi.1004639  |
| 2015 |  Zineb Hassainia  |  Dynamique des tourbillons pour quelques modèles de transport non-linéaires  |    |
| 2016 |  Adam Bzowski, Paul L. McFadden, Kostas Skenderis  |  Scalar 3-point functions in CFT: renormalisation, beta functions and anomalies  |  https://doi.org/10.1007/jhep03(2016)066  |
| 2016 |  Adeline Serckx, Marie‐Claude Huynen, Roseline Beudels-Jamar  |  Bonobo nest site selection and the importance of predictor scales in primate ecology  |  https://doi.org/10.1002/ajp.22585  |
| 2016 |  Aleksey Zinger  |  The Determinant Line Bundle for Fredholm Operators: Construction, Properties, and Classification  |  https://doi.org/10.7146/math.scand.a-23687  |
| 2016 |  Alina Bucur, Kiran S. Kedlaya  |  An application of the effective Sato-Tate conjecture  |  https://doi.org/10.1090/conm/663/13349  |
| 2016 |  André Voros  |  Simplifications of the Keiper/Li approach to the Riemann Hypothesis  |  https://doi.org/10.48550/arxiv.1602.03292  |
| 2016 |  Andrew Corbett  |  A proof of the refined Gan–Gross–Prasad conjecture for non-endoscopic Yoshida lifts  |  https://doi.org/10.1515/forum-2015-0164  |
| 2016 |  Anthony W. Knapp, Anthony W. Knapp  |  Chapter VI. Reinterpretation with Adeles and Ideles  |  https://doi.org/10.3792/euclid/9781429799928-6  |
| 2016 |  Babak Modami  |  Asymptotics of a class of Weil–Petersson geodesics and divergence of Weil–Petersson geodesics  |  https://doi.org/10.2140/agt.2016.16.267  |
| 2016 |  Chen Fang, Hongming Weng, Xi Dai  |  Topological nodal line semimetals  |  https://doi.org/10.1088/1674-1056/25/11/117106  |
| 2016 |  Eleonora Cinti, Juan Dávila, Manuel A. del Pino  |  Solutions of the fractional Allen–Cahn equation which are invariant under screw motion  |  https://doi.org/10.1112/jlms/jdw033  |
| 2016 |  Fritz Kleinschroth, John Robert Healey, Sylvie Gourlet‐Fleury  |  Effects of logging on roadless space in intact forest landscapes of the Congo Basin  |  https://doi.org/10.1111/cobi.12815  |
| 2016 |  Hale Çetinay, Fernando A. Kuipers, Ali Nezih GÜVEN  |  Optimal siting and sizing of wind farms  |  https://doi.org/10.1016/j.renene.2016.08.008  |
| 2016 |  Hashem Zoubi, Klemens Hammerer  |  Optomechanical multimode Hamiltonian for nanophotonic waveguides  |  https://doi.org/10.1103/physreva.94.053827  |
| 2016 |  James S. Milne  |  The Riemann hypothesis over finite fields: from Weil to the present day  |  https://doi.org/10.4310/iccm.2016.v4.n2.a4  |
| 2016 |  Jørgen Ellegaard Andersen, Sergei Gukov, Du Pei  |  The Verlinde formula for Higgs bundles  |  https://doi.org/10.48550/arxiv.1608.01761  |
| 2016 |  José Ignacio Burgos Gil, Walter Gubler, Philipp Jell  |  Differentiability of non-archimedean volumes and non-archimedean Monge-Ampère equations (with an appendix by R  |  https://doi.org/10.48550/arxiv.1608.01919  |
| 2016 |  Koen Thas  |  The Connes–Consani plane connection  |  https://doi.org/10.1016/j.jnt.2016.03.007  |
| 2016 |  L. E. Reichl  |  Index  |  https://doi.org/10.1002/9783527690497.index  |
| 2016 |  Mara Trübner, Johanna F. Ziegel  |  Derivatives of isotropic positive definite functions on spheres  |  https://doi.org/10.1090/proc/13561  |
| 2016 |  Patrick Kühn  |  Analytic theory of L-functions: explicit formulae, gaps between zeros and generative computational methods  |  https://doi.org/10.5167/uzh-126347  |
| 2016 |  Rahul Krishna  |  Relative Trace Formula for SO₂ × SO₃ and the Waldspurger Formula  |  https://doi.org/10.7916/d8fb52xb  |
| 2016 |  Sami Omar, Saber Bouanani  |  Li's criterion and the Riemann hypothesis for function fields II  |  https://doi.org/10.1016/j.ffa.2016.11.010  |
| 2016 |  Shaomin Liu, Ziwei Xu, Lisheng Song  |  Upscaling evapotranspiration measurements from multi-site to the satellite pixel scale over heterogeneous land  |  https://doi.org/10.1016/j.agrformet.2016.04.008  |
| 2016 |  Shuguo Wang, Xin Li, Yong Ge  |  Validation of Regional-Scale Remote Sensing Products in China: From Site to Network  |  https://doi.org/10.3390/rs8120980  |
| 2016 |  Stefan Kahler  |  Characterizations of Orthogonal Polynomials and Harmonic Analysis on Polynomial Hypergroups  |    |
| 2016 |  Tian An Wong  |  Explicit Formulae and Trace Formulae  |    |
| 2016 |  Tian An Wong  |  Lower bounds for Weil's Explicit Formula via Selberg's Trace Formula  |    |
| 2016 |  Xian‐Jin Li  |  An orthogonal projection related to the Riemann zeta-function  |  https://doi.org/10.1016/j.jmaa.2016.09.041  |
| 2017 |  Ahmed Arafat Hassan Mohammed  |  Mathematical Developments on Isotropic Positive Definite Functions on Spheres  |  https://doi.org/10.6035/14104.2017.420980  |
| 2017 |  Alain Connes A, Caterina Consani B  |  Geometry of the scaling site  |  https://doi.org/10.1007/s00029-017-0313-y  |
| 2017 |  Andreas Colliander, Thomas J. Jackson, Rajat Bindlish  |  Validation of SMAP surface soil moisture products with core validation sites  |  https://doi.org/10.1016/j.rse.2017.01.021  |
| 2017 |  Arie Blom  |  Cyclic theory of Lie algebroids  |    |
| 2017 |  Aurélien Sagnier  |  An arithmetic site of Connes-Consani type for imaginary quadratic fields with class number 1  |  https://doi.org/10.48550/arxiv.1703.10521  |
| 2017 |  Aurélien Sagnier  |  An arithmetic site of Connes-Consany type for imaginary quadratic fields with class number 1  |  https://doi.org/10.70675/215d95d2z957cz4388z99e5zbc6f7e5c88f4  |
| 2017 |  Aurélien Sagnier  |  Un site arithmétique de type connes-consani pour les corps quadratiques imaginaires de nombre de classes 1  |    |
| 2017 |  Bernard Mans, Min Sha, Igor E. Shparlinski  |  On Functional Graphs of Quadratic Polynomials  |  https://doi.org/10.1080/10586458.2017.1391725  |
| 2017 |  Bruce C. Berndt, Armin Straub  |  Ramanujan's Formula for $\zeta(2n+1)$  |    |
| 2017 |  Bruno Iochum  |  Spectral Geometry  |  https://doi.org/10.48550/arxiv.1712.05945  |
| 2017 |  Dimitar Jetchev, Christopher M. Skinner, Xin Wan  |  The Birch and Swinnerton–Dyer formula for elliptic curves of analytic rank one  |  https://doi.org/10.4310/cjm.2017.v5.n3.a2  |
| 2017 |  Gene S. Kopp  |  Indefinite Theta Functions and Zeta Functions  |    |
| 2017 |  Hohto Bekki  |  Relative Hecke's integral formula for an arbitrary extension of number fields  |  https://doi.org/10.48550/arxiv.1712.08392  |
| 2017 |  Kamel Mazhouda  |  On the $\tau $-Li coefficients for automorphic $L$-functions  |  https://doi.org/10.1216/rmj-2017-47-6-1987  |
| 2017 |  Kevin Broughan  |  Weil's Explicit Formula, Inequality and Conjectures  |  https://doi.org/10.1017/9781108178266.011  |
| 2017 |  Lin Zhao  |  Spherical and Spheroidal Harmonics: Examples and Computations  |    |
| 2017 |  Matilde Marcolli, Gonçalo Tabuada  |  Bost–Connes systems, categorification, quantum statistical mechanics, and Weil numbers  |  https://doi.org/10.4171/jncg/11-1-1  |
| 2017 |  Ming-Lun Hsieh, Kenichi Namikawa  |  Inner product formula for Yoshida lifts  |  https://doi.org/10.1007/s40316-017-0088-8  |
| 2017 |  Nobushige Kurokawa, Hidekazu Tanaka  |  Absolute zeta functions and the automorphy  |  https://doi.org/10.2996/kmj/1509415235  |
| 2017 |  Palle E. T. Jørgensen, Feng Tian  |  Positive definite (p.d.) functions vs p.d. distributions  |  https://doi.org/10.48550/arxiv.1712.07264  |
| 2017 |  Pilar Báyer  |  The Riemann hypothesis: The great pending challenge  |  https://doi.org/10.7203/metode.8.8903  |
| 2017 |  Ralf Schmidt  |  Archimedean aspects of Siegel modular forms of degree 2  |  https://doi.org/10.1216/rmj-2017-47-7-2395  |
| 2017 |  Raymond Aschheim, Carlos Castro Perelman, Klee Irwin  |  The search for a Hamiltonian whose energy spectrum coincides with the Riemann zeta zeroes  |  https://doi.org/10.1142/s0219887817501092  |
| 2017 |  Ricardo Pérez-Marco  |  Notes on the Riemann Hypothesis  |  https://doi.org/10.48550/arxiv.1707.01770  |
| 2017 |  Santhosh Karnik, Zhihui Zhu, Michael B. Wakin  |  The fast Slepian transform  |  https://doi.org/10.1016/j.acha.2017.07.005  |
| 2017 |  Tetsuo Mohri, Ying Chen, Masanori Kohyama  |  Mechanical properties of Fe-rich Si alloy from Hamiltonian  |  https://doi.org/10.1038/s41524-017-0012-4  |
| 2017 |  Walter Gubler, Julius Hertel  |  Local Heights of Toric Varieties over Non-archimedean Fields  |  https://doi.org/10.5802/pmb.15  |
| 2018 |  Anne-Maria Ernvall-Hytönen, Almasa Odžak, Medina Sušić  |  On Asymptotic Behavior of Generalized Li Coefficients  |  https://doi.org/10.11650/tjm/180407  |
| 2018 |  Daniel Moreno‐Fernández, Juan Gabriél Álvarez‐González, Roque Rodríguez‐Soalleiro  |  National-scale assessment of forest site productivity in Spain  |  https://doi.org/10.1016/j.foreco.2018.03.016  |
| 2018 |  Dye, Nathanael  |  Numerical Verification of Weil Positivity for Elliptic Curve L-functions  |  https://doi.org/10.5281/zenodo.19099121  |
| 2018 |  Fumihiro Satō  |  The Maass Zeta Functions Attached to Positive Definite Quadratic Forms  |  https://doi.org/10.2969/aspm/02110409  |
| 2018 |  Helmut Maier, Michael Th. Rassias  |  Explicit estimates of sums related to the Nyman–Beurling criterion for the Riemann Hypothesis  |  https://doi.org/10.1016/j.jfa.2018.06.022  |
| 2018 |  J. Steffen Müller, Corinna Stumpe  |  Archimedean local height differences on elliptic curves  |  https://doi.org/10.48550/arxiv.1807.04153  |
| 2018 |  Kazuya Katô  |  $p$-adic Hodge theory and values of zeta functions of modular forms  |  https://doi.org/10.24033/ast.639  |
| 2018 |  Masao Tsuzuki  |  Relative trace formulas for unitary hyperbolic spaces  |  https://doi.org/10.1215/21562261-2017-0025  |
| 2018 |  Peter Zeiner  |  Coincidence site lattices and coincidence site modules  |    |
| 2018 |  Pilar Báyer  |  La hipòtesi de Riemann: El gran repte pendent  |  https://doi.org/10.7203/metode.0.8903  |
| 2018 |  Raffaele Carlone, Michele Correggi, Lorenzo Tentarelli  |  An introduction to the two-dimensional Schrödinger equation with nonlinear point interactions  |  https://doi.org/10.17586/2220-8054-2018-9-2-187-195  |
| 2018 |  Rajendra Bhatia, Tanvi Jain, Yongdo Lim  |  On the Bures–Wasserstein distance between positive definite matrices  |  https://doi.org/10.1016/j.exmath.2018.01.002  |
| 2019 |  Aprameyo Pal, Carlos de Vera‐Piquero  |  Pullbacks of Saito-Kurokawa Lifts and a Central Value Formula for Degree 6 $L$-Series  |  https://doi.org/10.4171/dm/719  |
| 2019 |  Arul Shankar, Anders Södergren, Nicolas Templier  |  SATO–TATE EQUIDISTRIBUTION OF CERTAIN FAMILIES OF ARTIN -FUNCTIONS  |  https://doi.org/10.1017/fms.2019.18  |
| 2019 |  Benoı̂t Collins, Michael J. Magee, Doron Puder  |  Automorphism-invariant positive definite functions on free groups  |  https://doi.org/10.48550/arxiv.1906.01518  |
| 2019 |  D. Merlini, Sala Massimo, Sala Nicoletta  |  A numerical comment on the 'tiny' oscillations and a heuristic 'conjecture'  |  https://doi.org/10.48550/arxiv.1903.06233  |
| 2019 |  D. Merlini, Sala Massimo, Sala Nicoletta  |  Analysis of a Complex approximation to the Li-Keiper coefficients around the K Function  |  https://doi.org/10.48550/arxiv.1907.01903  |
| 2019 |  Daniel Hudson  |  K-theory correspondences and the Fourier-Mukai transform  |    |
| 2019 |  G Corona-Patricio, Ulrich Kuhl, Fabrice Mortessagne  |  Localisation and transport in bidimensional random models with separable Hamiltonians  |  https://doi.org/10.1088/1367-2630/ab2fd9  |
| 2019 |  J. Steffen Müller, Corinna Stumpe  |  Archimedean local height differences on elliptic curves  |  https://doi.org/10.4064/aa180714-7-12  |
| 2019 |  Jiangwei Xue, Chia‐Fu Yu  |  Trace formulas for the norm one group of totally definite quaternion algebras  |  https://doi.org/10.48550/arxiv.1909.11858  |
| 2019 |  Lin Weng  |  Stability and arithmetic  |  https://doi.org/10.2969/aspm/05810225  |
| 2019 |  Peter J. Cho, Jeong-Ho Park  |  Dirichlet characters and low-lying zeros of L-functions  |  https://doi.org/10.1016/j.jnt.2019.12.001  |
| 2019 |  Tian An Wong  |  Refinements of the trace formula for GL(2)  |  https://doi.org/10.48550/arxiv.1910.03733  |
| 2019 |  Toby Gee, Olivier Taïbi  |  Arthur’s multiplicity formula for GSp 4 and restriction to Sp 4  |  https://doi.org/10.5802/jep.99  |
| 2019 |  Ulrik Enstad, Mads S. Jakobsen, Franz Luef  |  Time-frequency analysis on the adeles over the rationals  |  https://doi.org/10.1016/j.crma.2018.12.004  |
| 2019 |  Walter Gubler, Philipp Jell, Klaus Künnemann  |  Continuity of Plurisubharmonic Envelopes in Non-Archimedean Geometry and Test Ideals  |  https://doi.org/10.5802/aif.3296  |
| 2019 |  Yiannis Sakellaridis  |  Relative Functoriality and Functional Equations via Trace Formulas  |  https://doi.org/10.1007/s40306-018-0295-7  |
| 2019 |  Zhi Qi  |  On the Fourier Transform of Regularized Bessel Functions on Complex Numbers and Beyond Endoscopy Over Number F  |  https://doi.org/10.1093/imrn/rnz205  |
| 2020 |  Alain Connes A, Caterina Consani B  |  Segal’s Gamma rings and universal arithmetic  |  https://doi.org/10.1093/qmath/haaa042  |
| 2020 |  Arghya Chattopadhyay, Parikshit Dutta, Suvankar Dutta  |  Matrix model for Riemann zeta via its local factors  |  https://doi.org/10.1016/j.nuclphysb.2020.114996  |
| 2020 |  Bharat Raj Jaiswal  |  Steady Stokes flow of a non-Newtonian Reiner-Rivlin fluid streaming over an approximate liquid spheroid  |  https://doi.org/10.24132/acm.2020.587  |
| 2020 |  Centro Tecnol&, V. S. Barbosa, #243  |  A Gneiting-Like Method for Constructing Positive Definite Functions on Metric Spaces  |  https://doi.org/10.3842/sigma.2020.117  |
| 2020 |  Devarshi Mukherjee  |  Topological Invariants for Non-Archimedean Bornological Algebras  |  https://doi.org/10.53846/goediss-8247  |
| 2020 |  Eric Canton  |  Berkovich log discrepancies in positive characteristic  |  https://doi.org/10.4310/pamq.2020.v16.n5.a5  |
| 2020 |  Hidekazu Tanaka  |  GAMMA FACTORS OF ZETA FUNCTIONS AS ABSOLUTE ZETA FUNCTIONS  |  https://doi.org/10.2206/kyushujm.74.441  |
| 2020 |  Huan Xiao  |  Recurrence relations of Li coefficients  |  https://doi.org/10.48550/arxiv.2006.13103  |
| 2020 |  Jamshid Derakhshan  |  Model Theory of Adeles and Number Theory  |  https://doi.org/10.48550/arxiv.2007.09237  |
| 2020 |  Jayce Robert Getz  |  A summation formula for the Rankin-Selberg monoid and a nonabelian trace formula  |  https://doi.org/10.1353/ajm.2020.0035  |
| 2020 |  Lucian M. Ionescu  |  From Periods to Anabelian Geometry and Quantum Amplitudes  |  https://doi.org/10.4236/apm.2020.105014  |
| 2020 |  Masatoshi Suzuki  |  Integral operators arising from the Riemann zeta function  |  https://doi.org/10.2969/aspm/08410399  |
| 2020 |  Maximilian Benker, Lukas Furtner, Thomas Semm  |  Utilizing uncertainty information in remaining useful life estimation via Bayesian neural networks and Hamilto  |  https://doi.org/10.1016/j.jmsy.2020.11.005  |
| 2020 |  Nathaniel Butler, Heath Emerson, Tyler Schulz  |  Dirac-Schr\"odinger operators and the irrational torus  |    |
| 2020 |  Ramy Rashad, Federico Califano, Arjan J. van der Schaft  |  Twenty years of distributed port-Hamiltonian systems: a literature review  |  https://doi.org/10.1093/imamci/dnaa018  |
| 2020 |  Rubén Gómez González, Vicente Garzó  |  First-Order Contributions to the Partial Temperatures in Dilute Binary Granular Suspensions  |  https://doi.org/10.1007/978-3-030-55973-1_42  |
| 2020 |  Sébastien Boucksom, Gubler, Walter, Martin, Florent  |  Non-Archimedean volumes of metrized nef line bundles  |  https://doi.org/10.48550/arxiv.2011.06986  |
| 2020 |  Takuki Tomita  |  The absolute Euler product representation of the absolute zeta function for a torsion free Noetherian $\mathbb  |  https://doi.org/10.48550/arxiv.2012.10486  |
| 2020 |  Walter Gubler  |  Differentiability of non-archimedean volumes and non-archimedean Monge–Ampère equations\n (with an appendix by  |  https://doi.org/10.14231/ag-2020-005  |
| 2021 |  Alain Connes A  |  Noncommutative Geometry, the Spectral Standpoint  |  https://doi.org/10.1017/9781108854399.003  |
| 2021 |  Alain Connes A, Caterina Consani B  |  Weil positivity and trace formula the archimedean place  |  https://doi.org/10.1007/s00029-021-00689-4  |
| 2021 |  Alain Connes A, Henri Moscovici  |  Prolate spheroidal operator and Zeta  |  https://doi.org/10.48550/arxiv.2112.05500  |
| 2021 |  Balodis, Kristaps John  |  Unitary Schwartz Forms & the Weil Representation  |    |
| 2021 |  Daniel S. Freed  |  The Atiyah–Singer index theorem  |  https://doi.org/10.1090/bull/1747  |
| 2021 |  L. Bonora  |  Perturbative and Non-Pertrubative Trace Anomalies  |  https://doi.org/10.3390/sym13071292  |
| 2021 |  L. Bonora  |  Perturbative and non-pertrubative trace anomalies  |  https://doi.org/10.48550/arxiv.2107.07918  |
| 2021 |  Masatoshi Suzuki  |  Hamiltonians arising from L-functions in the Selberg class  |  https://doi.org/10.1016/j.jfa.2021.109116  |
| 2021 |  Milad Bahadori, Kimmo U. Jarvinen, Tilen Marc  |  Speed Reading in the Dark: Accelerating Functional Encryption for Quadratic Functions with Reprogrammable Hard  |  https://doi.org/10.46586/tches.v2021.i3.1-27  |
| 2021 |  Sébastien Boucksom, Walter Gubler, Florent Martin  |  Non-Archimedean volumes of metrized nef line bundles  |  https://doi.org/10.46298/epiga.2021.6908  |
| 2021 |  Takuki Tomita  |  The absolute Euler product representation of the absolute zeta function for a torsion free Noetherian F1-schem  |  https://doi.org/10.1016/j.jnt.2021.08.009  |
| 2021 |  Xiang Li, Shaomin Liu, Xiaofan Yang  |  Upscaling Evapotranspiration from a Single-Site to Satellite Pixel Scale  |  https://doi.org/10.3390/rs13204072  |
| 2021 |  Yi Zhou, Yang Yang, Changxing Zhu  |  Numerical Analysis of Thermophoresis of a Charged Spheroidal Colloid in Aqueous Media  |  https://doi.org/10.3390/mi12020224  |
| 2022 |  A. Yu. Savin, Elmar Schrohe  |  Local index formulae on noncommutative orbifolds and equivariant zeta functions for the affine metaplectic gro  |  https://doi.org/10.1016/j.aim.2022.108624  |
| 2022 |  Adam J. Ostaszewski, Ν. H. Bingham  |  The Steinhaus-Weil property III: Weil topologies  |  https://doi.org/10.5644/sjm.17.02.01  |
| 2022 |  Afonso S. Bandeira, Nikolaus Doppelbauer, Dmitriy Kunisky  |  Dual bounds for the positive definite functions approach to mutually unbiased bases  |  https://doi.org/10.1007/s43670-022-00033-7  |
| 2022 |  Alain Connes A, Caterina Consani B  |  Cyclic theory and the pericyclic category  |  https://doi.org/10.48550/arxiv.2208.08339  |
| 2022 |  Alain Connes A, Caterina Consani B  |  Riemann-Roch for $\overline{\text{Spec}\mathbb Z}$  |  https://doi.org/10.48550/arxiv.2205.01391  |
| 2022 |  Alain Connes A, Henri Moscovici  |  The UV prolate spectrum matches the zeros of zeta  |  https://doi.org/10.1073/pnas.2123174119  |
| 2022 |  Aleksander Horawa  |  Motivic Action on Coherent Cohomology of Hilbert Modular Varieties  |  https://doi.org/10.1093/imrn/rnac126  |
| 2022 |  André Voros  |  From asymptotic to closed forms for the Keiper/Li approach to the Riemann Hypothesis  |  https://doi.org/10.48550/arxiv.2204.01036  |
| 2022 |  Andreia Faria‐Pereira, Vanessa A. Morais  |  Synapses: The Brain’s Energy-Demanding Sites  |  https://doi.org/10.3390/ijms23073627  |
| 2022 |  Andriy V. Bondarenko, Danylo Radchenko, Kristian Seip  |  Fourier Interpolation with Zeros of Zeta and L-Functions  |  https://doi.org/10.1007/s00365-022-09599-w  |
| 2022 |  Ben Kane, Daejun Kim, Srimathi Varadharajan  |  Explicit class number formulas for Siegel–Weil averages of ternary quadratic forms  |  https://doi.org/10.1090/tran/8814  |
| 2022 |  Grigori V. Rozenblum  |  Eigenvalues of singular measures and Connes’ noncommutative integration  |  https://doi.org/10.4171/jst/401  |
| 2022 |  Huayi Chen, Atsushi Moriwaki  |  Hilbert-Samuel formula and positivity over adelic curves  |  https://doi.org/10.48550/arxiv.2207.02033  |
| 2022 |  Joshua F. Lieber, Yuri I. Manin, Matilde Marcolli  |  Bost–Connes Systems and F1-structures in Grothendieck Rings, Spectra, and Nori Motives  |  https://doi.org/10.1017/9781108877855.006  |
| 2022 |  K. Maślanka  |  Analytic Extension of Keiper-Li Coefficients  |  https://doi.org/10.48550/arxiv.2211.08993  |
| 2022 |  Kai Köhler  |  Analytic torsion forms for fibrations by projective curves  |  https://doi.org/10.48550/arxiv.2208.14370  |
| 2022 |  Marcell Gaál, Szilárd Gy. Révész  |  Integral comparisons of nonnegative positive definite functions on LCA groups  |  https://doi.org/10.1007/s00209-022-03055-y  |
| 2022 |  Masatoshi Suzuki  |  An inverse problem for a class of lacunary canonical systems with diagonal Hamiltonian  |  https://doi.org/10.2748/tmj.20210816  |
| 2022 |  Masatoshi Suzuki  |  The screw line of the Riemann zeta-function and its applications  |  https://doi.org/10.48550/arxiv.2209.04658  |
| 2022 |  Paolo Dolce, Roberto Gualdi  |  Numerical equivalence of ℝ-divisors and Shioda–Tate formula for arithmetic varieties  |  https://doi.org/10.1515/crelle-2021-0081  |
| 2022 |  Suming An, Prajay Patel, Cong Liu  |  Computational Aspects of Single-Molecule Kinetics for Coupled Catalytic Cycles: A Spectral Analysis  |  https://doi.org/10.1021/acs.jpca.2c02153  |
| 2022 |  Wolfgang Erb  |  Graph signal interpolation with positive definite graph basis functions  |  https://doi.org/10.1016/j.acha.2022.03.005  |
| 2022 |  Yanbo Fang  |  Critical Fubini-Study metrics over non-archimedean fields  |  https://doi.org/10.48550/arxiv.2212.02486  |
| 2022 |  Yang‐Hui He, Vishnu Jejjala, Djordje Minić  |  Eigenvalue Density, Li's Positivity, and the Critical Strip  |  https://doi.org/10.56725/instemm.v1is1.23  |
| 2022 |  Zongmin Liu  |  Exact Finite Li-Jet Indistinguishability for Riemann–Xi Type Functions  |  https://doi.org/10.5281/zenodo.21778284  |
| 2023 |  Alain Connes A, Caterina Consani B  |  BC-system, absolute cyclotomy and the quantized calculus  |  https://doi.org/10.4171/emss/64  |
| 2023 |  Alain Connes A, Caterina Consani B  |  Riemann-Roch for the ring $\mathbb Z$  |  https://doi.org/10.48550/arxiv.2306.00456  |
| 2023 |  Alain Connes A, Caterina Consani B  |  Spectral triples and $\zeta$-cycles  |  https://doi.org/10.4171/lem/1049  |
| 2023 |  Alexei A. Deriglazov  |  Lagrangian and Hamiltonian formulations of asymmetric rigid body, considered as a constrained system  |  https://doi.org/10.1088/1361-6404/ace80d  |
| 2023 |  Andrea Blason, Michele Fabrizio  |  Unified role of Green's function poles and zeros in correlated topological insulators  |  https://doi.org/10.1103/physrevb.108.125115  |
| 2023 |  Angel Alfredo Moran Ledezma  |  A probabilistic interpretation of Weil's explicit sums and arithmetic spectral measures  |  https://doi.org/10.48550/arxiv.2311.08519  |
| 2023 |  Antoine Ducros, Ehud Hrushovski, François Loeser  |  Non-Archimedean integrals as limits of complex integrals  |  https://doi.org/10.1215/00127094-2022-0052  |
| 2023 |  Bernhard M. Maschke, Arjan J. van der Schaft  |  Linear Boundary Port-Hamiltonian Systems with Implicitly Defined Energy  |  https://doi.org/10.48550/arxiv.2305.13772  |
| 2023 |  Branden Thornhill-Miller, Anaëlle Camarda, Maxence Mercier  |  Creativity, Critical Thinking, Communication, and Collaboration: Assessment, Certification, and Promotion of 2  |  https://doi.org/10.3390/jintelligence11030054  |
| 2023 |  Chao Li  |  From sum of two squares to arithmetic Siegel–Weil formulas  |  https://doi.org/10.1090/bull/1786  |
| 2023 |  F. Alberto Grünbaum, Brian D. Vasquez Campos, Jorge Passamani Zubelli  |  Matrix bispectrality and noncommutative algebras: Beyond the prolate spheroidals  |  https://doi.org/10.4171/lem/1053  |
| 2023 |  Georgios D. Floros, Ioanna Mylona  |  Bipolar Disorder and Gaming Disorder—Compatible or Incompatible Diagnoses?  |  https://doi.org/10.3390/jcm12196251  |
| 2023 |  Jean‐Christophe Graz, Patrícia Rocha Lemos, Andréia Galvão  |  Do Labour Standards Improve Employment Relationships in Global Production Networks? A Cross-sector Study in Br  |  https://doi.org/10.15173/glj.v14i2.5088  |
| 2023 |  Jing‐Shan Zhao, Han-Lin Sun, Haoyang Li  |  Screw Dynamics of a Multibody System by a Schoenflies Manipulator  |  https://doi.org/10.3390/app13179732  |
| 2023 |  Jun Yang  |  Von Neumann Dimensions and Trace Formulas I: Limit Multiplicities  |  https://doi.org/10.48550/arxiv.2306.02999  |
| 2023 |  Justin Trias  |  Universal Weil module  |  https://doi.org/10.2140/pjm.2023.323.359  |
| 2023 |  Kai Köhler  |  Analytic torsion forms for fibrations by projective curves  |  https://doi.org/10.1007/s00209-023-03379-3  |
| 2023 |  Masatoshi Suzuki  |  Analytic theories around the simplest screw  |  https://doi.org/10.48550/arxiv.2308.11860  |
| 2023 |  Masatoshi Suzuki  |  Aspects of the screw function corresponding to the Riemann zeta‐function  |  https://doi.org/10.1112/jlms.12785  |
| 2023 |  Masatoshi Suzuki  |  Li coefficients as norms of functions in a model space  |  https://doi.org/10.1016/j.jnt.2023.05.007  |
| 2023 |  Masatoshi Suzuki  |  On the screw function of the Riemann zeta function (Analytic Number Theory and Related Topics)  |    |
| 2023 |  Masatoshi Suzuki, Masatoshi Suzuki  |  Aspects of the screw function corresponding to the Riemann zeta‐function  |    |
| 2023 |  Mercedes Orús–Lacort, Román Orús, Christophe Jouis  |  Analyzing Riemann's hypothesis  |  https://doi.org/10.17352/amp.000083  |
| 2023 |  Mingchen Xia  |  Operations on transcendental non-Archimedean metrics  |  https://doi.org/10.48550/arxiv.2312.17150  |
| 2023 |  R. C. McPhedran, Scott, Tony, C., Aude Maignan  |  Comments on and Extensions to Criteria of Keiper and Li for the Riemann Hypothesis  |  https://doi.org/10.1145/3637529.3637530  |
| 2023 |  R. C. McPhedran, Tony C. Scott, Aude Maignan  |  The Keiper-Li Criterion for the Riemann Hypothesis and Generalized Lambert Functions  |  https://doi.org/10.1145/3637529.3637530  |
| 2023 |  Rakheon Kim, Mohsen Pourahmadi, Tanya P. Garcia  |  Positive-definite thresholding estimators of covariance matrices with zeros  |  https://doi.org/10.1016/j.jmva.2023.105186  |
| 2023 |  Roberto Longo  |  Signal Communication and Modular Theory  |  https://doi.org/10.1007/s00220-023-04794-7  |
| 2023 |  Yang Zhong, Hongyu Yu, Mao Su  |  Transferable equivariant graph neural networks for the Hamiltonians of molecules and solids  |  https://doi.org/10.1038/s41524-023-01130-4  |
| 2023 |  Yûsuke Okuyama  |  A dynamical system over a non-archimedean field  |  https://doi.org/10.48550/arxiv.2310.01052  |
| 2024 |  Alain Connes A, Caterina Consani B  |  Knots, Primes and the adele class space  |  https://doi.org/10.48550/arxiv.2401.08401  |
| 2024 |  Alain Connes A, Caterina Consani B  |  On the metaphysics of $\mathbb{F}_{1}$  |  https://doi.org/10.4171/rlm/1036  |
| 2024 |  Alain Connes A, Caterina Consani B, Henri Moscovici  |  On q-series and the moment problem associated to local factors  |  https://doi.org/10.48550/arxiv.2403.01247  |
| 2024 |  Alain Connes A, Caterina Consani B, Henri Moscovici  |  Zeta zeros and prolate wave operators  |  https://doi.org/10.1007/s43034-024-00388-z  |
| 2024 |  Anne-Maria Ernvall-Hytönen, Almasa Odžak, Lejla Smajlović  |  Variants of the Li-Type Criteria for the Generalized Riemann Hypothesis  |  https://doi.org/10.1007/978-3-031-52163-8_8  |
| 2024 |  Daniel Disegni, Yifeng Liu  |  A $p$-adic arithmetic inner product formula  |  https://doi.org/10.1007/s00222-024-01243-7  |
| 2024 |  Daniele Dorigoni, Mehregan Doroudiani, Joshua Drewitt  |  Non-holomorphic modular forms from zeta generators  |  https://doi.org/10.1007/jhep10(2024)053  |
| 2024 |  Danny Allen, Kyle Bonetta-Martin, Elizabeth Codling  |  The Riemann Hypothesis  |  https://doi.org/10.24382/n49k-c482  |
| 2024 |  Holger Kammeyer, Steffen Kionke  |  Gassmann triples with special cycle types and applications  |  https://doi.org/10.1017/s0013091524000579  |
| 2024 |  H.T. Zhou, Xingdong Wang  |  Research on Spatial Siting of Transmission and Substation  |  https://doi.org/10.53964/jia.2024006  |
| 2024 |  Ismail Abouamal  |  Transition of type in the von Neumann algebras associated to the Connes-Marcolli $GSp_4$-system  |  https://doi.org/10.48550/arxiv.2403.03932  |
| 2024 |  J. J. Rodríguez-Vega, O. F. Casas-Sánchez  |  Explicit formula in a imaginary quadratic number field  |  https://doi.org/10.48550/arxiv.2401.09634  |
| 2024 |  Jawher Khmiri  |  A note on the screw line function on function fields  |  https://doi.org/10.71352/ac.57.363  |
| 2024 |  Jawher Khmiri  |  Variations of Voros–Li Coefficients on Function Fields  |  https://doi.org/10.1556/314.2024.00017  |
| 2024 |  Jorge Martín-Morales  |  Counting points with Riemann-Roch formulas  |  https://doi.org/10.48550/arxiv.2402.18193  |
| 2024 |  Joyce Weil, Ronica Nicole Rooks, Emily E. Leonard  |  Older Adults and Gentrification: The Positive Role of Social Policy  |  https://doi.org/10.1017/s0714980824000333  |
| 2024 |  Kajtaz H. Bllaca, Kamel Mazhouda, Takashi Nakamura  |  Li coefficients and the quadrilateral zeta function  |  https://doi.org/10.4153/s0008439524000250  |
| 2024 |  Kartik G. Waghmare, Victor M. Panaretos  |  The positive-definite completion problem  |  https://doi.org/10.1090/tran/9194  |
| 2024 |  LA ROSA, Alfio Fabio  |  Arithmetic Applications of the Trace Formula and Asymptotic Orthogonality of Tempered Representations  |    |
| 2024 |  Liudmyla Kryvonos, Edward Barry Saff  |  On a problem of E. Meckes for the unitary eigenvalue process on an arc  |  https://doi.org/10.1007/s13324-024-00919-w  |
| 2024 |  M. S. Maniuk, А. В. Коротун, В. И. Рева  |  Plasmonic resonances in the chain of spheroidal metallic nanoparticles on the dielectric substrate  |  https://doi.org/10.5488/cmp.27.43701  |
| 2024 |  Manuel K. -H. Müller  |  Modular forms for the Weil representation induced from isotropic subgroups  |  https://doi.org/10.1016/j.jnt.2024.04.005  |
| 2024 |  Manuel K. -H. Müller  |  The basis problem for modular forms for the Weil representation  |  https://doi.org/10.48550/arxiv.2407.01205  |
| 2024 |  Markus Lohmayer, Giuseppe Capobianco, Sigrid Leyendecker  |  Exergetic port-Hamiltonian systems for multibody dynamics  |  https://doi.org/10.1007/s11044-024-10038-w  |
| 2024 |  Mounir Hajli  |  On the regularized products of some Dirichlet series  |  https://doi.org/10.48550/arxiv.2401.03645  |
| 2024 |  Nathaniel Butler, Heath Emerson, Tyler Schulz  |  Zeta functions and topology of Heisenberg cycles for linear ergodic flows  |  https://doi.org/10.4171/ggd/763  |
| 2024 |  Nikolaj Glazunov  |  On the arithmetic and algebraic properties of Minkowski balls and spheres  |  https://doi.org/10.48550/arxiv.2407.12048  |
| 2024 |  Pedro Pinheiro‐Chagas, Clara Sava‐Segal, Serdar Akkol  |  Spatiotemporal dynamics of successive activations across the human brain during simple arithmetic processing  |  https://doi.org/10.1523/jneurosci.2118-22.2024  |
| 2024 |  R. C. McPhedran  |  Sandwiching the Riemann hypothesis  |  https://doi.org/10.48550/arxiv.2407.00060  |
| 2024 |  Roman Urban  |  Feynman formulas for qp- and pq-quantization of some Vladimirov type time-dependent Hamiltonians on finite ade  |  https://doi.org/10.1007/s13324-024-00965-4  |
| 2024 |  Sophie Chopinet  |  Graft steatosis in liver transplantation : from diagnosis to preventions of reperfusion injury  |    |
| 2024 |  Tchamitchian Pierre  |  Explicit lower bounds on the conductors of elliptic curves and abelian varieties over number fields  |  https://doi.org/10.48550/arxiv.2410.12922  |
| 2024 |  Tian An Wong  |  Zeroes of Rankin-Selberg $L$-functions and the trace formula  |  https://doi.org/10.48550/arxiv.2405.02998  |
| 2024 |  Timothy Stroschein  |  Prolate Spheroidal Wave Functions and the Accuracy and Dimensionality of Spectral Analysis  |  https://doi.org/10.48550/arxiv.2409.16584  |
| 2024 |  Tuoping Du  |  On the arithmetic inner product formula and central derivatives of L-functions  |  https://doi.org/10.48550/arxiv.2412.00688  |
| 2024 |  Ulrich Tehrani  |  Conditional Stationarity and Positive Curvature of the Spectral Trace at the Critical Line  |  https://doi.org/10.5281/zenodo.20440671  |
| 2024 |  W. Riley Casper, F. Alberto Grünbaum, Milen T. Yakimov  |  Matrix Valued Discrete–Continuous Functions with the Prolate Spheroidal Property and Bispectrality  |  https://doi.org/10.1007/s00220-023-04909-0  |
| 2024 |  Yoshiyasu Ozeki  |  Explicit bounds on torsion of CM abelian varieties over p-adic fields with values in Lubin–Tate extensions  |  https://doi.org/10.2140/pjm.2024.330.171  |
| 2024 |  Yueke Hu, Ian Petrow, Matthew P. Young  |  A generalized PGL(2) Petersson/Bruggeman-Kuznetsov formula for analytic applications  |  https://doi.org/10.48550/arxiv.2411.05672  |
| 2025 |  Alain Connes A, Walter D. van Suijlekom  |  Quadratic Forms, Real Zeros and Echoes of the Spectral Action  |  https://doi.org/10.1007/s00220-025-05493-1  |
| 2025 |  Alberto Enciso B, Gunther A. Uhlmann, Michał Wrochna  |  The Dirichlet-to-Neumann map on asymptotically anti-de Sitter spaces and holography  |  https://doi.org/10.48550/arxiv.2512.03587  |
| 2025 |  Andrei T. Patrascu  |  Categorical Grothendieck–Riemann–Roch, Integrability, and Non-Perturbative String Theory  |  https://doi.org/10.2139/ssrn.5606681  |
| 2025 |  Andrew Phillips  |  The Gross-Zagier formula on singular moduli for Shimura curves  |  https://doi.org/10.48550/arxiv.2509.11553  |
| 2025 |  Chen, Guo  |  Noncommutative geometry and the Riemann Hypothesis: a survey of ten papers in Connes's program (1998—2026)  |  https://doi.org/10.5281/zenodo.17885822  |
| 2025 |  CHOI, JONGMIN  |  Multi–Zero Dynamic Curvature Framework for the Riemann Zeta Zeros Two–Body and Three–Body Instability Mechanis  |  https://doi.org/10.5281/zenodo.17695373  |
| 2025 |  Claudia Alfes‐Neumann, Paul Kiefer, Jan Mazáč  |  Measures, Modular Forms, and Summation Formulas of Poisson Type  |  https://doi.org/10.1007/s00220-025-05313-6  |
| 2025 |  de Frutos, Fernando  |  A Quantum Dissipative Framework for the Riemann Hypothesis: Explicit-Formula Equivalence, Dirichlet-Form Posit  |  https://doi.org/10.5281/zenodo.17762484  |
| 2025 |  de Frutos, Fernando  |  The Universal Arithmetic Laplacian for the Riemann Zeta Function: Weil's Explicit Formula, Functional Equation  |  https://doi.org/10.5281/zenodo.17849501  |
| 2025 |  Dow, Jeremy  |  The Prime–Resonance Operator II: Proof of Equivalence via Localized Sign Definiteness  |  https://doi.org/10.5281/zenodo.17605171  |
| 2025 |  Dow, Jeremy  |  The Prime–Resonance Operator VIII: Explicit-Formula Equivalence and Completion of the Programme  |  https://doi.org/10.5281/zenodo.17625338  |
| 2025 |  DURAND, SERGE  |  Horizon A Formal Spectral Architecture for the Riemann Hypothesis  |  https://doi.org/10.5281/zenodo.17944490  |
| 2025 |  E. A. Reis  |  Hilbert–Pólya via de Branges and the Weyl m-Function: Vertical Convolution and the Riemann Hypothesis  |  https://doi.org/10.1590/scielopreprints.13340  |
| 2025 |  F. Alberto Grünbaum  |  Time and Band Limiting: From the Early Days to the Present  |  https://doi.org/10.37394/23202.2025.24.31  |
| 2025 |  Faizuddin Ahmed, Edilberto  Oliveira Silva  |  Nonrelativistic Quantum Dynamics in a Twisted Screw Spacetime  |  https://doi.org/10.3390/universe11120391  |
| 2025 |  Fernandez, Alexis  |  An Archimedean Proof of the Riemann Hypothesis via Centered Weil–Toeplitz Positivity  |  https://doi.org/10.5281/zenodo.17548213  |
| 2025 |  Gabriel Bengochea, Manuel Duarte Ortigueira, Fernando Arroyo-Cabañas  |  On the Inversion of the Mellin Convolution  |  https://doi.org/10.3390/math13030432  |
| 2025 |  HI-AI  |  AN EXAMINATION OF THE INTERRELATIONS BETWEEN MODULAR DYNAMICS, SPACETIME THERMODYNAMICS, QUANTUM COMPLEXITY, A  |  https://doi.org/10.5281/zenodo.17606376  |
| 2025 |  Jean-Pierre Ramis, Françoise Richard-Jung, J. Thomann  |  New eigenfunctions for the negative part of the Connes–Moscovici prolate spectrum  |  https://doi.org/10.5802/crmath.780  |
| 2025 |  Jirô Akahori, Norio Konno, Rikuki Okamoto  |  Absolute zeta functions for zeta functions of quantum walks  |  https://doi.org/10.1007/s11128-025-05018-8  |
| 2025 |  Johannes Nicaise, Peter Scholze, Michael Temkin  |  Non-Archimedean Geometry and Applications  |  https://doi.org/10.4171/owr/2025/29  |
| 2025 |  Jonathan Beardsley  |  The Eilenberg-MacLane Spectrum of \mathbb{F}_1  |  https://doi.org/10.48550/arxiv.2508.01524  |
| 2025 |  Khalkhali, Masoud, Pagliaroli, Nathan  |  Bootstrapping Noncommutative Geometry with Dirac Ensembles  |    |
| 2025 |  Kohji Matsumoto, Masatoshi Suzuki  |  M-functions and screw functions: Applications to Goldbach's problem and zeros of the Riemann zeta-function  |  https://doi.org/10.1016/j.jnt.2025.09.013  |
| 2025 |  Leonhard Schuster  |  On the limitations of Li's criterion for Riemann Hypothesis  |  https://doi.org/10.5281/zenodo.18055740  |
| 2025 |  Leung, Chi Ho, Philip E. Paré  |  Bayesian Safety Guarantees for Port-Hamiltonian Systems with Learned Energy Functions  |  https://doi.org/10.48550/arxiv.2512.24493  |
| 2025 |  Malamutmann, Eugen  |  Fejér–heat generators and Lipschitz control for the Weil quadratic functional  |  https://doi.org/10.5281/zenodo.17853581  |
| 2025 |  Malamutmann, Eugen  |  Operator Methods for the Weil Criterion: Q3  |  https://doi.org/10.5281/zenodo.17527098  |
| 2025 |  Masatoshi Suzuki  |  On the Hilbert space derived from the Weil distribution  |  https://doi.org/10.4153/s0008414x25101739  |
| 2025 |  Masatoshi Suzuki, Masatoshi Suzuki  |  M-functions and screw functions: applications to Goldbach's problem and zeros of the Riemann zeta-function  |    |
| 2025 |  Michael Pycraft Hughes  |  The Multi-Conductivity Clausius–Mossotti Factor as an Electrophysiology Rosetta Stone: Dielectrophoresis, Memb  |  https://doi.org/10.3390/mi16111200  |
| 2025 |  Michela Dianetti, Lucy Elvis  |  emotion, disequilibrium and attentive compassion  |  https://doi.org/10.12957/childphilo.2025.89714  |
| 2025 |  Minzi Chen, Gordon Heier  |  On positive semi-definite holomorphic sectional curvature with many zeroes  |  https://doi.org/10.4310/cag.250802001848  |
| 2025 |  Mohamed Haj Yousef  |  Non-Commutative Geometric Foundations for the Emergence of Spatial Dimensions and Physical Structures from Com  |  https://doi.org/10.20944/preprints202509.2573.v1  |
| 2025 |  Nathanael Dov Chwojko  |  Hirzebruch Riemann Roch Theorem  |    |
| 2025 |  Renato Spigler  |  A Brief Survey on the Riemann Hypothesis and Some Attempts to Prove It  |  https://doi.org/10.3390/sym17020225  |
| 2025 |  Renato Spigler  |  Another proof of the validity of Keiper–Li’s criterion to prove the Riemann hypothesis  |  https://doi.org/10.1080/10652469.2025.2517721  |
| 2025 |  Roberta Spallone  |  Arithmetic, geometry, and measurements in the Baroque building site  |  https://doi.org/10.36253/tribelon-3791  |
| 2025 |  Ryan Cardwell  |  Type Consumption in Paley-Wiener Spaces: A Conditional Reduction of the Riemann Hypothesis  |  https://doi.org/10.5281/zenodo.18103774  |
| 2025 |  Shekhar Suman  |  Asymptotic of Li coefficients and proof of the Riemann hypothesis  |  https://doi.org/10.13140/rg.2.2.27817.04962  |
| 2025 |  Timothy McGirl  |  A Self-Adjoint Operator for Riemann Zeros via φ-Weighted Toeplitz Positivity  |  https://doi.org/10.5281/zenodo.18057717  |
| 2025 |  Vasil Dinev Penchev  |  Philosophical and mathematical reflection on Riemann's hypothesis. II The ontomathematical proof of Riemann's   |  https://doi.org/10.2139/ssrn.5244354  |
| 2025 |  Vasil Dinev Penchev  |  Philosophical and mathematical reflection on Riemann’s hypothesis. II The ontomathematical proof of Riemann’s   |  https://doi.org/10.31235/osf.io/vkwtm_v1  |
| 2025 |  Vasil Dinev Penchev  |  Philosophical and mathematical reflection on Riemann’s hypothesis. II The ontomathematical proof of Riemann’s   |  https://doi.org/10.33774/coe-2025-cc579  |
| 2025 |  Vasil Dinev Penchev  |  Primes are KS fundamentally random (but in Hilbert arithmetic, not in the standard mathematics)  |  https://doi.org/10.2139/ssrn.5329093  |
| 2025 |  Virginia S. Kiryakova, Jordanka Paneva-Konovska  |  Generalized Erdélyi-Kober Fractional Integrals and Images of Special Functions  |  https://doi.org/10.3390/fractalfract9090567  |
| 2025 |  Vladimer Khasia  |  Linear Programming Bounds for the Riemann Zeta Function via the Geometry of Prime Logarithms  |  https://doi.org/10.5281/zenodo.18050349  |
| 2025 |  Y, jqh  |  A Parameter-Free Reconstruction toward the Riemann Hypothesis  |  https://doi.org/10.5281/zenodo.17522071  |
| 2025 |  Y. Shimizu  |  Proof of the Riemann Hypothesis  |  https://doi.org/10.20944/preprints202505.2110.v1  |
| 2025 |  Y. Shimizu  |  Proof of the Riemann Hypothesis  |  https://doi.org/10.20944/preprints202505.2110.v2  |
| 2025 |  Y. Shimizu  |  Proof of the Riemann Hypothesis  |  https://doi.org/10.20944/preprints202505.2110.v3  |
| 2025 |  Yubo Jin, Dongwen Liu, Binyong Sun  |  Archimedean period relations for Rankin-Selberg convolutions  |  https://doi.org/10.1016/j.aim.2025.110393  |
| 2025 |  Zhi Qi  |  On the Effective Non-vanishing of Hecke--Maass $L$-functions at Special Points  |  https://doi.org/10.48550/arxiv.2507.14566  |
| 2025 |  Zongmin Liu  |  Exact Finite Li-Jet Indistinguishability for Riemann–Xi Type Functions  |  https://doi.org/10.5281/zenodo.21778283  |
| 2026 |  Aaron Woffinden  |  Prime–Boundary Synchrony for the Riemann Zeta Function: Certified Instruments for a Weil-Positivity Program  |  https://doi.org/10.5281/zenodo.22065904  |
| 2026 |  Ahmad Al Mohder  |  GROUND-STATE NEGATIVITY OF TRUNCATED CONNES-VAN SUIJLEKOM FORMS FOR DIRICHLET L-FUNCTIONS.  |  https://doi.org/10.5281/zenodo.21851907  |
| 2026 |  Ahmed Benadiel  |  A Structural Proof of the Riemann Hypothesis via a Positive Self-Adjoint Trace Operator  |  https://doi.org/10.5281/zenodo.18644228  |
| 2026 |  AJ McDermott  |  An N = 1 zero-sum criterion in the Connes-Consani-Moscovici construction  |  https://doi.org/10.5281/zenodo.20651101  |
| 2026 |  Akira Oguri, Masashi Hashimoto, Yoshimichi Teratani  |  Three-body Fermi-liquid corrections for Andreev transport through quantum dots  |  https://doi.org/10.1103/ll4l-hxsl  |
| 2026 |  Akiva Groskin  |  A Conditional Reduction of the Riemann Hypothesis to Even Dominance of the Weil Quadratic Form  |  https://doi.org/10.5281/zenodo.21910402  |
| 2026 |  Akiva Groskin  |  A finite Guinand-Weil dictionary and archimedean tail order for the truncated Weil quadratic form  |    |
| 2026 |  Akiva Groskin  |  A finite Guinand-Weil dictionary and archimedean tail order for the truncated Weil quadratic form  |  https://doi.org/10.48550/arxiv.2607.02828  |
| 2026 |  Akiva Groskin  |  A finite Guinand-Weil dictionary and archimedean tail order for the truncated Weil quadratic form  |  https://doi.org/10.5281/zenodo.21124802  |
| 2026 |  Akiva Groskin  |  A finite Guinand-Weil dictionary and archimedean tail order for the truncated Weil quadratic form  |  https://doi.org/10.5281/zenodo.21124803  |
| 2026 |  Akiva Groskin  |  A finite Guinand-Weil dictionary and archimedean tail order for the truncated Weil quadratic form  |  https://doi.org/10.5281/zenodo.21146461  |
| 2026 |  Akiva Groskin  |  A finite Guinand-Weil dictionary and archimedean tail order for the truncated Weil quadratic form  |  https://doi.org/10.5281/zenodo.21911012  |
| 2026 |  Akiva Groskin  |  A matrix-valued von Mangoldt measure in the finite Connes-van Suijlekom path  |  https://doi.org/10.5281/zenodo.21242028  |
| 2026 |  Akiva Groskin  |  A matrix-valued von Mangoldt measure in the finite Connes-van Suijlekom path  |  https://doi.org/10.5281/zenodo.21242029  |
| 2026 |  Akiva Groskin  |  A matrix-valued von Mangoldt measure in the finite Connes-van Suijlekom path  |  https://doi.org/10.5281/zenodo.21612746  |
| 2026 |  Akiva Groskin  |  High-Precision Approximation of Riemann Zeros via the Truncated Weil Form  |  https://doi.org/10.48550/arxiv.2605.20224  |
| 2026 |  Akiva Groskin  |  High-Precision Approximation of Riemann Zeros via the Truncated Weil Form  |  https://doi.org/10.5281/zenodo.19546514  |
| 2026 |  Akiva Groskin  |  High-Precision Approximation of Riemann Zeros via the Truncated Weil Form  |  https://doi.org/10.5281/zenodo.20156914  |
| 2026 |  Akiva Groskin  |  High-Precision Approximation of Riemann Zeros via the Truncated Weil Form  |  https://doi.org/10.5281/zenodo.20931069  |
| 2026 |  Akiva Groskin  |  High-Precision Galerkin Experiments on the Connes–van Suijlekom Truncated Weil Form, with an Out-of-Sample Emp  |  https://doi.org/10.5281/zenodo.20150435  |
| 2026 |  Akiva Groskin  |  High-Precision Galerkin Experiments on the Connes–van Suijlekom Truncated Weil Form, with an Out-of-Sample Emp  |  https://doi.org/10.5281/zenodo.20153365  |
| 2026 |  Akiva Groskin  |  Structural Properties of the Connes–van Suijlekom Truncated Weil Minimizer: Sobolev Scaling, Multi-Zero Univer  |  https://doi.org/10.5281/zenodo.19546515  |
| 2026 |  Akiva Groskin  |  Structural Properties of the Connes–van Suijlekom Truncated Weil Minimizer: Sobolev Scaling, Multi-Zero Univer  |  https://doi.org/10.5281/zenodo.19655106  |
| 2026 |  Alain Connes A, Caterina Consani B  |  The Absolute Twistor Line and the Geometry of $\overline{\text{Spec}\, \mathbf Z}$  |  https://doi.org/10.48550/arxiv.2609.00299  |
| 2026 |  Alain Connes A, Caterina Consani B, Henri Moscovici  |  Zeta spectral triples  |  https://doi.org/10.4171/elm/37/3  |
| 2026 |  Alexandar Balevsky  |  Non-Circular Projection Undemonstrability of the Riemann Hypothesis  |  https://doi.org/10.5281/zenodo.20367105  |
| 2026 |  Alexandre Couret, InterIA Mathematical Collective, Thomas Ingles  |  A Modular Analytic Framework for the Riemann Hypothesis (T1′–T4)  |  https://doi.org/10.5281/zenodo.18802768  |
| 2026 |  Alexanja Senke  |  Exact Finite Gram Closure for Weil Positivity on the Fixed Test-Function Window (-77/64, 77/64) — Restricted I  |  https://doi.org/10.5281/zenodo.22871383  |
| 2026 |  Alfred Yang  |  A Spectral-Variational Bridge to Weil Positivity Fourth-Moment Amplification and a Local-Stability Criterion f  |  https://doi.org/10.13140/rg.2.2.10388.67201  |
| 2026 |  Alizer Wong, Heng Cui, Yi Tan  |  Eureka: Task-Conditioned Meta-Agent Orchestration for Scientific Discovery  |  https://doi.org/10.48550/arxiv.2608.19047  |
| 2026 |  Andrés Chirre, Blas Molero Ravines  |  Explicit conditional bounds for $ζ(s)$ at the edge of the critical strip  |  https://doi.org/10.48550/arxiv.2602.06199  |
| 2026 |  Antonio Bonelli  |  The Kaleidoscopic Filter: Exact $\mathcal{O}(1)$ Formula for $P_k(n)$, The Exact Riemann Zeta Zeroes, Berry-Ke  |  https://doi.org/10.5281/zenodo.20990674  |
| 2026 |  Antonio Bonelli  |  The Kaleidoscopic Filter: Exact $\mathcal{O}(1)$ Formula for $P_k(n)$, The Exact Riemann Zeta Zeroes, Berry-Ke  |  https://doi.org/10.5281/zenodo.20990675  |
| 2026 |  Ariel Fernando Martini  |  A Hilbert-Pólya Approach to the Riemann Hypothesis via Cartan Torsion and the Weil Positivity Criterion  |  https://doi.org/10.5281/zenodo.20634319  |
| 2026 |  Ariel Fernando Martini  |  Hahn-Banach Separation and the Local-to-Global Gap in the Weil Criterion: Theoretical Notes  |  https://doi.org/10.5281/zenodo.20655427  |
| 2026 |  Ariel Fernando Martini  |  Spectral Stability and Asymptotic Limits of the Prime-Perturbed Cartan–Torsion Operator  |  https://doi.org/10.5281/zenodo.20634901  |
| 2026 |  Ariel Fernando Martini  |  The Hilbert–Pólya Programme via Cartan Torsion Geometry: A Complete Treatment of the Spectral Approach to the   |  https://doi.org/10.5281/zenodo.20673839  |
| 2026 |  Arkava Ganguly, Ankur Gupta  |  Shape-dependence of electrophoretic mobility: an AI-assisted derivation  |  https://doi.org/10.48550/arxiv.2604.11771  |
| 2026 |  Arkava Ganguly, Ankur Gupta  |  Shape-dependence of electrophoretic mobility: an AI-assisted perturbation analysis  |  https://doi.org/10.1017/jfm.2026.11948  |
| 2026 |  Axel Abdel Rahamane MEGHEZZI  |  Certified Finite-Support Weil Positivity Across the First Prime-Power Threshold  |  https://doi.org/10.5281/zenodo.22050466  |
| 2026 |  Blas Salvador Molero Ravines  |  Explicit conditional bounds for 𝐿(𝑠, 𝜒) and 𝜁(𝑠) at the edge of the critical strip  |    |
| 2026 |  Boduen Wang  |  Structural Transfer and Operational Stability at the Critical Locus of the Bost–Connes System  |  https://doi.org/10.2139/ssrn.7277062  |
| 2026 |  Borros Arneth  |  A PIHR Consistent-Limit Approach to the Riemann Hypothesis From Prime-Weighted Screw Functions to Self-Adjoint  |  https://doi.org/10.2139/ssrn.7329678  |
| 2026 |  Borros Arneth  |  Finite-Euler Energy Contraction and a One-Sided Laplace Criterion for the Riemann Hypothesis  |  https://doi.org/10.2139/ssrn.7540859  |
| 2026 |  Breno Wilson de Andrade Silva  |  Computer-Assisted Proofs of Even-Simplicity for Three Finite Galerkin Weil Forms  |  https://doi.org/10.5281/zenodo.20887027  |
| 2026 |  Breno Wilson de Andrade Silva  |  Quadrature sensitivity of deep spectra of truncated Weil forms, with corrections to two recent computational n  |  https://doi.org/10.5281/zenodo.20650145  |
| 2026 |  Breno Wilson de Andrade Silva  |  Quadrature sensitivity of deep spectra of truncated Weil forms, with corrections to two recent computational n  |  https://doi.org/10.5281/zenodo.20650146  |
| 2026 |  Brice Pouly  |  Poisson laws and arithmetic clusters for rare multiplicative patterns  |  https://doi.org/10.5281/zenodo.22877399  |
| 2026 |  Byoungwoo Lee  |  Finite-Rank Prime-Edge Transmission and Adaptive Continuation for Localized Weil Comparisons  |  https://doi.org/10.5281/zenodo.22342605  |
| 2026 |  Carlee Toddes, Kevin N Bai, Isabel E Halperin  |  Social agency buffers pain sensitivity during a critical window following spared nerve injury  |  https://doi.org/10.64898/2026.07.15.738734  |
| 2026 |  Carlos Alberto Terêncio de Bastos  |  A Mirror-Global-Period Approach to the Weil Criterion for the Riemann Zeta Function  |  https://doi.org/10.5281/zenodo.18510860  |
| 2026 |  Carter, John  |  Computational Verification of the Connes-Consani Adele Class Space Framework for the Riemann Hypothesis: Weil   |  https://doi.org/10.5281/zenodo.20436593  |
| 2026 |  Chen Gong, Jit Wu Yap  |  Non-Archimedean Rigidity and Uniformity for Common Preperiodic Points  |  https://doi.org/10.48550/arxiv.2607.19252  |
| 2026 |  Claude  |  vonjensen95/zeta-toeplitz-rigidity: v1.0.0 — initial release  |  https://doi.org/10.5281/zenodo.21781658  |
| 2026 |  Clifford Keeble  |  The Fibonacci Spectral Ladder: Hopf Fibre Decomposition of the Zeta Spectrum on S³/2I  |  https://doi.org/10.5281/zenodo.19004257  |
| 2026 |  Daichi Tanaka  |  Explicit Construction of Maass Wave Forms and Their Petersson Inner Products  |  https://doi.org/10.48550/arxiv.2601.21588  |
| 2026 |  Daniel Toupin  |  Proof of the Birch and Swinnerton-Dyer Conjecture for Rank ≤ 1 via Spectral Methods  |  https://doi.org/10.5281/zenodo.18241267  |
| 2026 |  darreal44, djoubertthot  |  darreal44/riemann-weil-phenomenology: v1.0 — Certified quorum theorem + companion notes  |  https://doi.org/10.5281/zenodo.22215278  |
| 2026 |  Dav Shen  |  Arithmetic Bosonization and Weil Positivity  |  https://doi.org/10.5281/zenodo.22684345  |
| 2026 |  Dav Shen  |  Arithmetic Bosonization and Weil Positivity  |  https://doi.org/10.5281/zenodo.22694750  |
| 2026 |  de Andrade Silva, Breno Wilson  |  Simple zeros and parity interlacing for the negative Connes–Moscovici prolate spectrum  |  https://doi.org/10.5281/zenodo.20626649  |
| 2026 |  Dean Kulik  |  Operator-Theoretic and Computational Realizations of the Riemann Hypothesis  |  https://doi.org/10.5281/zenodo.21143337  |
| 2026 |  Dean Kulik  |  Operator-Theoretic and Computational Realizations of the Riemann Hypothesis Expanded  |  https://doi.org/10.5281/zenodo.21144643  |
| 2026 |  Dean Kulik  |  Operator-Theoretic Factorizations and the Positivity Constraints of Spectral Measures  |  https://doi.org/10.5281/zenodo.21251898  |
| 2026 |  Dean Kulik  |  The NEXUS-RH Framework: Arithmetic-Moment Stieltjes Pipeline and the Spectral Resolution of Riemann Zeros  |  https://doi.org/10.5281/zenodo.21154897  |
| 2026 |  Dimitar Prodromov  |  A Deterministic Spectral Proof of the Riemann Hypothesis via Weil Positivity, Li Criterion Asymptotics, and Ca  |  https://doi.org/10.5281/zenodo.22148892  |
| 2026 |  Djilali Benamara  |  The Riemann Hypothesis: A Complete Proof via Noncommutative Geometry and the Weil Positivity Criterion  |  https://doi.org/10.5281/zenodo.21195521  |
| 2026 |  Dustin Clausen  |  Weil-Moore anima  |  https://doi.org/10.48550/arxiv.2605.11950  |
| 2026 |  E. F. Perez-Eugenio  |  Jones index of prime endomorphisms in the Bost–Connes system  |  https://doi.org/10.5281/zenodo.19216301  |
| 2026 |  E. F. Perez-Eugenio  |  Jones index of prime endomorphisms in the Bost–Connes system: higher invariants, fusion rules, and logarithmic  |  https://doi.org/10.5281/zenodo.19500604  |
| 2026 |  E. F. PEREZ-EUGENIO  |  Paper IV — Jones index of prime endomorphisms in the Bost-Connes system  |    |
| 2026 |  E. M. Abdullah  |  The Chain: Hurwitz Convergence from Finite Primes to Zeta Zeros via the Connes–van Suijlekom Construction  |  https://doi.org/10.5281/zenodo.18917408  |
| 2026 |  E. M. Abdullah  |  The Twist: Spectral Isolation of Zeta as the Least Twisted L-Function  |  https://doi.org/10.5281/zenodo.19121248  |
| 2026 |  El Bouazzaoui TAYB  |  The Connes–Weil–KMS Principle: A Thermodynamic Proof of the Riemann Hypothesis — From the Stability Law of Ari  |  https://doi.org/10.5281/zenodo.20699992  |
| 2026 |  El Bouazzaoui TAYB  |  The Dyadic Structure of L L-Functions: From Spin to Primes and Beyond  |  https://doi.org/10.5281/zenodo.20514601  |
| 2026 |  El Bouazzaoui TAYB  |  The Dyadic Structure of L L-Functions: From Spin to Primes and Beyond  |  https://doi.org/10.5281/zenodo.20515565  |
| 2026 |  El Bouazzaoui TAYB  |  Windowed Quadratic Structures for the Zeta Function: Construction of the Weil Spectral Kernel, Comparison with  |  https://doi.org/10.5281/zenodo.22043962  |
| 2026 |  Elias De Jesus  |  Single-Factor Heights, Two-Factor Domination An Obstruction to a Canonical A ⪰ 2M in the Arithmetic Recorder G  |  https://doi.org/10.5281/zenodo.21111609  |
| 2026 |  Estevam Son Park  |  Discretizing the Archimedean place in the spectral realization of the Riemann zeta function  |  https://doi.org/10.5281/zenodo.19465777  |
| 2026 |  Felipe Gonçalves  |  A Classification of Fourier Summation Formulas and Crystalline Measures  |  https://doi.org/10.1007/s00365-026-09793-0  |
| 2026 |  Filipe Bastos  |  A Proof of the Riemann Hypothesis  |  https://doi.org/10.5281/zenodo.18804633  |
| 2026 |  Fiona Mcgeough  |  Global Coercivity of Explicit–Formula Residuals A Rigidity Theorem for the Riemann Hypothesis  |  https://doi.org/10.5281/zenodo.18155978  |
| 2026 |  Frank Morales  |  Two Spectral Approaches to the Riemann Hypothesis: A Comparative Analysis of Connes' Adelic Framework and the   |  https://doi.org/10.5281/zenodo.19900935  |
| 2026 |  Frederic David Blum  |  Emergent Spectral Geometry I: Arithmetic Symmetry Classification of the Bost-Connes System  |  https://doi.org/10.5281/zenodo.18929298  |
| 2026 |  Frederic David Blum  |  Information-Geometric Confinement of Riemann Zeros: Spectral Rigidity from Fisher Quantization on the Bures Ma  |  https://doi.org/10.5281/zenodo.19354342  |
| 2026 |  Frederic David Blum  |  Phase Structure of Fisher Information at Riemann Zeros  |  https://doi.org/10.5281/zenodo.19387248  |
| 2026 |  Frederic David Blum  |  Scale-Resolved Weil Positivity  |  https://doi.org/10.5281/zenodo.23229270  |
| 2026 |  Fu-Tsun Wei  |  $v$-adic Chowla-Selberg formula over function fields  |  https://doi.org/10.48550/arxiv.2609.23287  |
| 2026 |  Gereon Kraemer  |  The Riemann Hypothesis as Fixed-Point Theorem on S²  |  https://doi.org/10.5281/zenodo.20552635  |
| 2026 |  Giacomo Fabbian  |  Explicit positivity ranges for Li coefficients from partial verifications of the Riemann hypothesis  |  https://doi.org/10.5281/zenodo.22839422  |
| 2026 |  Guilherme Vedana  |  Classification of Fourier summation formulas on a horizontal strip  |  https://doi.org/10.48550/arxiv.2608.10121  |
| 2026 |  Guo Chen  |  A Dirichlet-Form Rewriting of the Weil Explicit Formula and an Unconditional Hilbert–Pólya Candidate  |  https://doi.org/10.5281/zenodo.19951231  |
| 2026 |  Guo Chen  |  Prolate Leakage and Near-Zero Spectral Clusters of the Semilocal Weil Operator  |  https://doi.org/10.5281/zenodo.23297284  |
| 2026 |  Guo Chen  |  Referee Report on *The Three Gates: A Rooted-Operator Approach to Weil Positivity*  |  https://doi.org/10.5281/zenodo.22892645  |
| 2026 |  Henning Wunderlich  |  Finite-radius Jensen and relative-entropy formulations of the Balazard--Saias--Yor criterion  |  https://doi.org/10.48550/arxiv.2610.10584  |
| 2026 |  Huan Xiao  |  Attack on the Riemann Hypothesis II  |  https://doi.org/10.20944/preprints202409.1294.v2  |
| 2026 |  Jaideep Sai Padhi  |  Sign patterns of real powers of infinite products: resolution of four conjectures of Schlosser and Zhou  |  https://doi.org/10.48550/arxiv.2609.22324  |
| 2026 |  James Norman Ibbotson  |  Certified Weil Positivity Past log 19, an Explicit Envelope-Exclusion Region, and Jensen Hyperbolicity to Degr  |  https://doi.org/10.5281/zenodo.21256882  |
| 2026 |  James Norman Ibbotson  |  Certified Weil Positivity Past log 19, an Explicit Envelope-Exclusion Region, and Jensen Hyperbolicity to Degr  |  https://doi.org/10.5281/zenodo.21257072  |
| 2026 |  Jan Vybíral  |  A counterexample to a conjecture on positive positive-definite functions  |  https://doi.org/10.1016/j.jco.2026.102097  |
| 2026 |  Jean Lauro Muller  |  A Spectral Reduction of the Riemann Hypothesis via the Weil Quadratic Form and Prolate Approximations  |  https://doi.org/10.5281/zenodo.22050543  |
| 2026 |  Jennifer Johnson­-Leung, Nina Rupert  |  An Explicit Theta Lift to Siegel Paramodular Forms  |  https://doi.org/10.1007/978-3-032-11183-8_10  |
| 2026 |  JONGMIN CHOI  |  V112 — A Carathéodory‑Toeplitz Reformulation of the Riemann Hypothesis via Li Coefficients  |  https://doi.org/10.5281/zenodo.19840408  |
| 2026 |  JONGMIN CHOI  |  V112_1 — A Carathéodory‑Toeplitz Reformulation of the Riemann Hypothesis via Li Coefficients  |  https://doi.org/10.5281/zenodo.19840454  |
| 2026 |  JONGMIN CHOI  |  V112_2 — A Carathéodory‑Toeplitz Reformulation of the Riemann Hypothesis via Li Coefficients  |  https://doi.org/10.5281/zenodo.19840473  |
| 2026 |  JONGMIN CHOI  |  V112_3 — A Carathéodory‑Toeplitz Reformulation of the Riemann Hypothesis via Li Coefficients  |  https://doi.org/10.5281/zenodo.19840486  |
| 2026 |  JONGMIN CHOI  |  V158_2 — Microscopic Shielding Obstructions in the de Bruijn–Newman Flow and Weil–Connes Positivity  |  https://doi.org/10.5281/zenodo.20055708  |
| 2026 |  JONGMIN CHOI  |  V165 — Detecting Spurious Positivity in Finite Models of the Weil Criterion  |  https://doi.org/10.5281/zenodo.20281397  |
| 2026 |  JONGMIN CHOI  |  V165_1 — A Spectrum‑Blind Finite Approximation Scheme for Weil Positivity  |  https://doi.org/10.5281/zenodo.20281465  |
| 2026 |  JONGMIN CHOI  |  V165_2 — A Conditional Spectrum-Blind Finite Approximation Framework for Weil Positivity  |  https://doi.org/10.5281/zenodo.20281475  |
| 2026 |  JONGMIN CHOI  |  V167 — A Compact‑Support Certificate Framework for Weil Positivity and a Paley‑Wiener Bottleneck for the Riema  |  https://doi.org/10.5281/zenodo.20286680  |
| 2026 |  JONGMIN CHOI  |  V167_1 — A Compact‑Support Certificate Framework for Weil Positivity: Finite Schur Certificates and a Paley‑Wi  |  https://doi.org/10.5281/zenodo.20286822  |
| 2026 |  JONGMIN CHOI  |  V167_2 — A Compact‑Support Certificate Framework for Weil Positivity: Finite Schur Certificates and a Paley‑Wi  |  https://doi.org/10.5281/zenodo.20286846  |
| 2026 |  JONGMIN CHOI  |  V167_3 — A Compact‑Support Certificate Framework for Weil Positivity: Finite Schur Certificates and a Paley‑Wi  |  https://doi.org/10.5281/zenodo.20287371  |
| 2026 |  JONGMIN CHOI  |  V183 — Function‑Field Riemann Hypothesis as a Blueprint: A Long‑Term Research Map for Explicit‑Formula Positiv  |  https://doi.org/10.5281/zenodo.20573750  |
| 2026 |  JONGMIN CHOI  |  V184 — Weil Positivity as a Missing Arithmetic Hodge Index Subject: A Route‑Pruning and Frontier‑Mapping Docum  |  https://doi.org/10.5281/zenodo.20574448  |
| 2026 |  JONGMIN CHOI  |  V185 — The Arithmetic Site Square and the Missing Hodge‑Ready Intersection Theory: A Failure Map for a Number‑  |  https://doi.org/10.5281/zenodo.20581245  |
| 2026 |  JONGMIN CHOI  |  V186 — Same Weil Form, Failed Determinant Lift, and a Paley‑Wiener Density Obstruction: A Technical Note for t  |  https://doi.org/10.5281/zenodo.20581258  |
| 2026 |  JONGMIN CHOI  |  V192.16 — A Local Obstruction to p‑adic Sonin Compression and Positive‑Commutator Approaches to Weil Positivit  |  https://doi.org/10.5281/zenodo.20696553  |
| 2026 |  JONGMIN CHOI  |  V193.1 — From Spherical Square Roots to Krein Polarization: Obstruction Maps for Positive‑Spectral Approaches   |  https://doi.org/10.5281/zenodo.20696694  |
| 2026 |  JONGMIN CHOI  |  V196.1 — An ACS‑0 Correspondence Carrier for Weil's Explicit Formula: Degree‑Zero Projection, Admissible Regul  |  https://doi.org/10.5281/zenodo.20697233  |
| 2026 |  JONGMIN CHOI  |  V196.2 — An ACS‑0 Correspondence Carrier for Weil's Explicit Formula: Degree‑Zero Projection, Admissible Regul  |  https://doi.org/10.5281/zenodo.20697251  |
| 2026 |  JONGMIN CHOI  |  V200.1 — Primitive Weil Positivity: Verified Certificates, a Sufficient Criterion for the Riemann Hypothesis,   |  https://doi.org/10.5281/zenodo.20697579  |
| 2026 |  JONGMIN CHOI  |  V200.2 — Primitive Weil Positivity: Verified Certificates, a Sufficient Criterion for the Riemann Hypothesis,   |  https://doi.org/10.5281/zenodo.20697617  |
| 2026 |  JONGMIN CHOI  |  V212 — An Interval‑Certified Finite Schur Certificate at L = 0.75, T = 54  |  https://doi.org/10.5281/zenodo.20698971  |
| 2026 |  Jordan Gabriel Farrell  |  A Curvature-Homology Proof of the Riemann Hypothesis  |  https://doi.org/10.33774/coe-2026-058cc  |
| 2026 |  Jordan Gabriel Farrell  |  A Curvature-Homology Proof of the Riemann Hypothesis  |  https://doi.org/10.33774/coe-2026-058cc-v2  |
| 2026 |  Joseph Berenji  |  Projectivity of the Adele Class Space and the Proof of the Riemann Hypothesis  |  https://doi.org/10.5281/zenodo.21912196  |
| 2026 |  Kai Ma  |  Weil–Bombieri Explicit-Formula Positivity: A Detailed Conditional (Axiomatic) Derivation of the Riemann Hypoth  |  https://doi.org/10.5281/zenodo.21418852  |
| 2026 |  Kerym Makraini  |  Convergence, Density, and Final Weil Positivity Paper 4  |  https://doi.org/10.13140/rg.2.2.28156.91527  |
| 2026 |  Kerym Makraini  |  Convergence, Density, and Final Weil Positivity Paper 4  |  https://doi.org/10.5281/zenodo.19357524  |
| 2026 |  Komeil Karimi poor  |  Localized Weil Positivity and Rooted-Operator Induction for the Riemann Hypothesis  |  https://doi.org/10.5281/zenodo.23121658  |
| 2026 |  Kouichi Taira, Max Willems, Michał Wrochna  |  Large eigenvalues of the Connes-Moscovici operator  |  https://doi.org/10.48550/arxiv.2609.32639  |
| 2026 |  Krische  |  Towards an Explicit Hilbert–Pólya Operator  |  https://doi.org/10.5281/zenodo.20689543  |
| 2026 |  Kunal Tyagi  |  Products of the per-prime Tate curves of absolute geometry carry no correspondence calculus for the Weil expli  |  https://doi.org/10.5281/zenodo.22171136  |
| 2026 |  Lange, Julien  |  The compression defect of a discrete-sine Galerkin section: an exact reflection identity, a window-truncation   |  https://doi.org/10.5281/zenodo.22239567  |
| 2026 |  Lauri Elias Rainio  |  The Last Lemma: What Proving the Riemann Hypothesis Concretely Requires  |  https://doi.org/10.5281/zenodo.19484169  |
| 2026 |  Leonhard Schuster  |  The Asymptotic Resolution Dichotomy in Li's criterion  |  https://doi.org/10.5281/zenodo.19476050  |
| 2026 |  Leung, Chi Ho, Philip E. Paré  |  Port-Transversal Barriers: Graph-Theoretic Safety for Port-Hamiltonian Systems  |  https://doi.org/10.48550/arxiv.2603.26578  |
| 2026 |  Levent Alpöge, Ralph Furman  |  Beyond Nine Loops: From Computational Depth to Representational Jurisdiction  |  https://doi.org/10.48550/arxiv.2608.13637  |
| 2026 |  Logan Eberwein  |  The truncated Weil quadratic form: inertia, visibility, structural measurements, and no-go theorems for the Ri  |  https://doi.org/10.5281/zenodo.23177437  |
| 2026 |  Luca Eliseo Pavesi  |  Hankel-rank structure and pairing thresholds in the Guinand--Weil explicit formula: an operational reformulati  |  https://doi.org/10.5281/zenodo.22820901  |
| 2026 |  Luca Eliseo Pavesi  |  (Status: Submitted) The Klein orbit of the Riemann zeros: Hadamard gaps, the geometry of the off-line contribu  |  https://doi.org/10.5281/zenodo.22869683  |
| 2026 |  Luis Morató de Dalmases  |  SGUP-600cell: Complete Spectral Unification of Fundamental Physics and Mathematics  |  https://doi.org/10.5281/zenodo.19765603  |
| 2026 |  Lukas Geiger  |  A Conditional Proof of the Riemann Hypothesis via Even Dominance of the Weil Quadratic Form  |  https://doi.org/10.5281/zenodo.19764771  |
| 2026 |  Lukas Geiger  |  A Conditional Proof of the Riemann Hypothesis via Even Dominance of the Weil Quadratic Form  |  https://doi.org/10.5281/zenodo.20011910  |
| 2026 |  Lukas Geiger  |  A Conditional Reduction of the Riemann Hypothesis to Even Dominance of the Weil Quadratic Form  |  https://doi.org/10.5281/zenodo.20291994  |
| 2026 |  Lukas Geiger  |  A Conditional Reduction of the Riemann Hypothesis to Even Dominance of the Weil Quadratic Form  |  https://doi.org/10.5281/zenodo.20358727  |
| 2026 |  Lukas Geiger  |  A Conditional Reduction of the Riemann Hypothesis to Even Dominance of the Weil Quadratic Form  |  https://doi.org/10.5281/zenodo.20396370  |
| 2026 |  Lukas Geiger  |  A Conditional Reduction of the Riemann Hypothesis to Even Dominance of the Weil Quadratic Form  |  https://doi.org/10.5281/zenodo.20479145  |
| 2026 |  Lukas Geiger  |  A Conditional Reduction of the Riemann Hypothesis to Even Dominance of the Weil Quadratic Form  |  https://doi.org/10.5281/zenodo.20687544  |
| 2026 |  Lukas Geiger  |  NE-B Failure as Hilbert-Pólya Detection: Universality of the v2.0 Weil Quadratic Form on the Selberg Zeta Func  |  https://doi.org/10.5281/zenodo.19962588  |
| 2026 |  Lukas Geiger  |  The Riemann Hypothesis: A Direct Proof via Even Dominance of the Weil Quadratic Form  |  https://doi.org/10.5281/zenodo.19764772  |
| 2026 |  Lukas Geiger  |  The Spectral Zookeeper: A Conditional Reduction toward the Riemann Hypothesis via Spectral Microcluster Closur  |  https://doi.org/10.5281/zenodo.20396399  |
| 2026 |  Lukas Geiger  |  The Spectral Zookeeper: A Conditional Reduction toward the Riemann Hypothesis via Spectral Microcluster Closur  |  https://doi.org/10.5281/zenodo.20479223  |
| 2026 |  M I Aksman, Mikhail I Aksman  |  Combined RH Program (Full) Combined Research Program on the Riemann Hypothesis Structural Identity via Arithme  |  https://doi.org/10.13140/rg.2.2.17409.21606  |
| 2026 |  M I Aksman, Mikhail I Aksman  |  Structural Identity Program for Weil's Explicit Formula A Structural Identity Program for Weil's Explicit Form  |  https://doi.org/10.13140/rg.2.2.19204.90245  |
| 2026 |  Marco Desogus  |  Supplementary Computational Material for the article The Three Gates: A Rooted-Operator Approach to Weil Posit  |  https://doi.org/10.5281/zenodo.22799712  |
| 2026 |  Marco Desogus  |  The Three Gates — A Rooted-Operator Approach to Weil Positivity  |  https://doi.org/10.5281/zenodo.22779410  |
| 2026 |  Marco Desogus  |  The Three Gates: A Rooted-Operator Approach to Weil Positivity  |  https://doi.org/10.48550/arxiv.2609.20367  |
| 2026 |  Marko Kostić  |  Almost Periodic Functions and Integro-Differential-Difference Equations in Locally Convex Spaces  |  https://doi.org/10.1201/9781003797531  |
| 2026 |  marsh, Brandon, Amasarac, Eluriah, KeyDjinn, Tiwoven, Eidolon  |  The Marsh-Feagans Spectral Algebra and the Riemann Hypothesis: A Partial Resolution via Pseudo-Hermitian Opera  |  https://doi.org/10.5281/zenodo.19394013  |
| 2026 |  Masatoshi Suzuki  |  Weil's quadratic form via the screw function  |  https://doi.org/10.48550/arxiv.2606.09096  |
| 2026 |  Mesut Ismail  |  Heat-flow lifetimes and windowed Weil positivity: a quantitative dictionary  |  https://doi.org/10.5281/zenodo.21464143  |
| 2026 |  Mesut Ismail  |  Off-line zeros of the Riemann xi-function: a constraint network, an exactly solved four-body collision, an ene  |  https://doi.org/10.5281/zenodo.21938686  |
| 2026 |  Mhamed Zineddine, Ray Zawdovski  |  Gaussian Spectral Packets for the Riemann Zeta Function: Exact Local Detection, Prime-Side Reconstruction, and  |  https://doi.org/10.20944/preprints202610.1267.v1  |
| 2026 |  Michael Allan Bahtaji  |  On the Riemann Hypothesis: An Analytic, Spectral, and Weil-Positivity Framework  |  https://doi.org/10.5281/zenodo.23102417  |
| 2026 |  Michael I Aksman  |  A Structural Identity Program for Weil's Explicit Formula via Arithmetic Special Cycles  |  https://doi.org/10.5281/zenodo.21724093  |
| 2026 |  Michael I Aksman  |  APERY PERIODS AND OPERATOR POSITIVITY ´ The Structural Equivalence of the Vorton Hessian and Weil's Explicit F  |  https://doi.org/10.5281/zenodo.21941904  |
| 2026 |  Michael I Aksman  |  THE RIEMANN HYPOTHESIS AS A STABILITY THEOREM Weil Positivity, Arakelov Intersections, and the Arithmetic Vacu  |  https://doi.org/10.5281/zenodo.21935732  |
| 2026 |  Michel L. Lapidus, Matthew Overduin  |  Distributional Fractional Taylor Series and Interpretation of the Fractal and Number-Theoretic Explicit Formul  |  https://doi.org/10.48550/arxiv.2609.22759  |
| 2026 |  Michel R. P. Planat  |  Morse Topology, Zero Products, and Elliptic Prime Crossings  |  https://doi.org/10.48550/arxiv.2609.27962  |
| 2026 |  Mikhail I Aksman  |  THE STRUCTURAL EQUIVALENCE OF 3D NAVIER-STOKES REGULARITY AND THE RIEMANN HYPOTHESIS A Vorton-Filament Realiza  |  https://doi.org/10.13140/rg.2.2.22630.79683  |
| 2026 |  Ming Ng  |  The Archimedean place is a blurred interval at infinity  |  https://doi.org/10.48550/arxiv.2609.09117  |
| 2026 |  Mohamed Makraini  |  Spectral Properties of the Truncated Weil Operator & Numerical Verication of Weil Positivity Version V.1.0.0  |  https://doi.org/10.13140/rg.2.2.32485.56805  |
| 2026 |  Muhamad Fouad  |  Zeta-Minimizer Theorem: Variational Emergence of Primes, Zeta, and Stratified Geometries from Helical Optimiza  |  https://doi.org/10.20944/preprints202602.0006.v1  |
| 2026 |  Muhamad Fouad  |  Zeta-Minimizer Theorem: Variational Emergence of Primes, Zeta, and Stratified Geometries from Helical Optimiza  |  https://doi.org/10.20944/preprints202602.0006.v2  |
| 2026 |  Muhammad Aidil Amry  |  Rigorous Ball Arithmetic and Bandwidth Calibrated Spectral Analysis of the Guinand Weil Operator Framework  |  https://doi.org/10.5281/zenodo.22998759  |
| 2026 |  Murilo Corato-Zanarella  |  First explicit reciprocity law for unitary Friedberg--Jacquet periods  |    |
| 2026 |  Nic Johns  |  Positive solutions of the explicit formula for ζ(s): near-criticality and uniqueness  |  https://doi.org/10.5281/zenodo.23197915  |
| 2026 |  Nic Johns  |  Sharpness and uniqueness for positive solutions of the explicit formula for ζ(s)  |  https://doi.org/10.5281/zenodo.23238100  |
| 2026 |  Nikita Kalinin, Ernesto Lupercio, Mikhail Shkolnikov  |  Residues of a tropical zeta function for convex domains  |  https://doi.org/10.48550/arxiv.2604.21709  |
| 2026 |  Nikolaj Glazunov  |  On non-Archimedean quantum mathematics and non-Archimedean (quantum) computation  |    |
| 2026 |  Oğuzhan Özbay  |  Mean-Square Convergence of the Sharp Spectral Cutoff for the von Mangoldt Function  |  https://doi.org/10.5281/zenodo.23382197  |
| 2026 |  Oleg Glushkov  |  Reproducibility Package for Numerical and Formal Diagnostics of a Compactly Supported Bombieri–Weil Positivity  |  https://doi.org/10.5281/zenodo.22133100  |
| 2026 |  Oliver Tuma  |  Finite Weil Windows: Euler Boundary Geometry, Hyperbolic Parity, and Smoothed Prime Errors  |  https://doi.org/10.5281/zenodo.23297024  |
| 2026 |  Oliver Tuma  |  From Möbius Mollification to Screw Positivity  |  https://doi.org/10.5281/zenodo.23046576  |
| 2026 |  Owen Schnider  |  On the nontrivial zeros of the Riemann zeta function  |  https://doi.org/10.5281/zenodo.19034365  |
| 2026 |  Paolo Arnaudo, Cristoforo Iossa, Robin Karlsson  |  OPE = QNM  |  https://doi.org/10.48550/arxiv.2607.24909  |
| 2026 |  Paul Chun-Kit Lee  |  The Archimedean Principle: Why Physics and Number Theory Share a Logical Architecture (Paper 70, Constructive   |  https://doi.org/10.5281/zenodo.18750991  |
| 2026 |  Paulo Marcelo Paulek Paulek Paulo  |  SPINOR REPRESENTATION OF THE ADELE CLASS SPACE AND THE RIEMANN HYPOTHESIS  |  https://doi.org/10.5281/zenodo.19583005  |
| 2026 |  Pavel Kramarenko-Byrd  |  A Finite-Window Operator Form of the Weil Explicit Formula: Trivial-Pole Boundary Terms and the Restricted Wei  |  https://doi.org/10.5281/zenodo.20078978  |
| 2026 |  Pavel Kramarenko-Byrd  |  Finite-Window Continuation and Root Stiffness in Restricted Weil Positivity  |  https://doi.org/10.5281/zenodo.19560981  |
| 2026 |  Pavel Kramarenko-Byrd  |  Restricted Weil Forms: Constraints, Negative Index, and Certified Sign  |  https://doi.org/10.5281/zenodo.22885924  |
| 2026 |  Pavel Kramarenko-Byrd  |  Restricted Weil Positivity at the Prime-Free Boundary and a Local Prime-Active Extension  |  https://doi.org/10.5281/zenodo.19520557  |
| 2026 |  Pavel Kramarenko-Byrd  |  The Critical-Line Amplitude p^{−r/2} as a KMS State at β = 1/2  |  https://doi.org/10.5281/zenodo.19322537  |
| 2026 |  Payam Danesh  |  A Proposal Framework for the Riemann Hypothesis  |  https://doi.org/10.2139/ssrn.6726739  |
| 2026 |  Pedro Caceres  |  Cross-Energy of Dirichlet Partial Sums PART VII: Weil Positivity as a Prime Cross-Energy  |  https://doi.org/10.5281/zenodo.23070556  |
| 2026 |  Peter Murphy  |  What a Weil-type geometric proof of the Riemann Hypothesis must supply: an obstruction map from machine-checke  |  https://doi.org/10.5281/zenodo.23369683  |
| 2026 |  Peter Murphy  |  What a Weil-type geometric proof of the Riemann Hypothesis must supply: an obstruction map from machine-checke  |  https://doi.org/10.5281/zenodo.23374028  |
| 2026 |  Piotr Ogonowski  |  Protected Reconstruction from Codazzi Defects: Equianharmonic Quantization and a Minimal Standard-Model Carrie  |    |
| 2026 |  Radu-Daniel Derscariu  |  A Finite-Dimensional Model for the Truncated Frobenius Operators of the Bost–Connes System  |  https://doi.org/10.5281/zenodo.20510120  |
| 2026 |  Rainer Andreas Mittermeier  |  An RH-Independent Conductor-23 Operator Architecture for the Riemann–Weil Problem: Positive Hilbert Host, Arit  |  https://doi.org/10.5281/zenodo.20531258  |
| 2026 |  Rainer Andreas Mittermeier  |  Compact Weil Event Cells from Suzuki's Screw Function: Parity Polarization, Exact Enclosures, and Uniform Gram  |  https://doi.org/10.5281/zenodo.22687243  |
| 2026 |  Rainer Andreas Mittermeier  |  Prime-Power Checkpoints for Suzuki's Riemann Zeta Screw Function: Rigorous Positivity Certificate through q =   |  https://doi.org/10.5281/zenodo.21838881  |
| 2026 |  Rainer Andreas Mittermeier  |  Prime-power checkpoints for the Riemann zeta screw function: Plastic-Constant Convexity and Legendre--Mangoldt  |  https://doi.org/10.5281/zenodo.21790972  |
| 2026 |  Rainer Andreas Mittermeier  |  Recovery-Selected Weil Rectangles: A Sparse Criterion for the Post-Certificate Riemann-Hypothesis Tail  |  https://doi.org/10.5281/zenodo.22857939  |
| 2026 |  Rainer Andreas Mittermeier  |  Understanding the Riemann Hypothesis: From the primes through Riemann's zeros and Suzuki's screw function to M  |  https://doi.org/10.5281/zenodo.21933783  |
| 2026 |  Renjie Guo, Sadia Riaz, Wajiha Bushra  |  Some New Subclasses of Bi-Univalent Functions Related to Quantum Calculus  |  https://doi.org/10.3390/math14050911  |
| 2026 |  Rivis Stefano  |  A formal proof of the Riemann Hypothesis  |  https://doi.org/10.5281/zenodo.19230303  |
| 2026 |  Rivis Stefano  |  A formal proof of the Riemann Hypothesis - Extended Version  |  https://doi.org/10.5281/zenodo.19230280  |
| 2026 |  Rivis Stefano  |  A formal proof of the Riemann Hypothesis v2  |  https://doi.org/10.5281/zenodo.19261480  |
| 2026 |  Robert Sherwood  |  Suzuki Localized Weil Form Research Compendium for The Riemann Hypothesis  |  https://doi.org/10.5281/zenodo.21922673  |
| 2026 |  Roberto Carlo Angelone  |  A Peer-Verification Protocol for a Computer-Assisted Localized Weil Positivity Theorem Candidate through μ=5.0  |  https://doi.org/10.5281/zenodo.22287510  |
| 2026 |  Roberto Carlo Angelone  |  A Rigorous Computer-Assisted Positivity Certificate for the Localized Weil Quadratic Form up to a = (1/2) log   |  https://doi.org/10.5281/zenodo.22105736  |
| 2026 |  Roberto Carlo Angelone  |  Certified Positivity of the Localized Weil Quadratic Form up to Support Radius Half the Logarithm of 3  |  https://doi.org/10.5281/zenodo.22062590  |
| 2026 |  rodrigo javier vidal  |  The Modular KMS Automorphism on Hyperfinite Von Neumann Factors: A Rigorous Algebraical Proof of the Riemann H  |  https://doi.org/10.5281/zenodo.20666635  |
| 2026 |  Ronnie Andrews  |  Empirical Falsification of Convergence Rate Predictions for the Connes-Consani-Moscovici Zeta Spectral Triple  |  https://doi.org/10.5281/zenodo.20427673  |
| 2026 |  Ronnie Andrews  |  Independent Reproduction and Convergence Analysis of the Connes-Consani-Moscovici Zeta Spectral Triple  |  https://doi.org/10.5281/zenodo.20427499  |
| 2026 |  Ronnie Andrews  |  Source Code: A Quantitative Convergence Law for the Connes-Consani-Moscovici Zeta Spectral Triple  |  https://doi.org/10.5281/zenodo.21015111  |
| 2026 |  Ronnie Andrews  |  Source Code: Empirical Falsification of Convergence Rate Predictions for the CCM Zeta Spectral Triple  |  https://doi.org/10.5281/zenodo.20427675  |
| 2026 |  Ronnie Andrews  |  Source Code: Independent Reproduction and Convergence Analysis of the CCM Zeta Spectral Triple  |  https://doi.org/10.5281/zenodo.20427501  |
| 2026 |  Ryan C. Chen  |  Co-rank 1 arithmetic Siegel–Weil I: local non-Archimedean  |  https://doi.org/10.1007/s00222-026-01444-2  |
| 2026 |  Ryan Henderson  |  Kernel-Positivity of Laplace Registers, Blagouchine--Royen Measures, and the Weil/de Branges Explicit-Formula   |  https://doi.org/10.5281/zenodo.19636675  |
| 2026 |  Ryota Mori  |  A μ^{9/2} log μ upper bound for windowed Weil forms  |  https://doi.org/10.5281/zenodo.23175060  |
| 2026 |  Ryota Mori  |  Weil positivity on a window of width log 5: a formal proof in Lean 4  |  https://doi.org/10.5281/zenodo.23034001  |
| 2026 |  Ryota Mori  |  Weil positivity on a window of width log 5: Lean formalization  |  https://doi.org/10.5281/zenodo.23031522  |
| 2026 |  Ryota Mori  |  Weil positivity on the window of width log 15  |  https://doi.org/10.5281/zenodo.23281235  |
| 2026 |  Ryota Mori  |  Weil positivity on the window of width log 15: certificate data  |  https://doi.org/10.5281/zenodo.23281175  |
| 2026 |  Sajad Salami  |  Weighted, GIT and Néron--Tate heights on genus-two moduli and Jacobians  |  https://doi.org/10.48550/arxiv.2610.13850  |
| 2026 |  Salem Eid  |  Certified Convex Positivity for the Pole-Inclusive Weil Form at the Prime-Free Endpoint  |  https://doi.org/10.5281/zenodo.21704682  |
| 2026 |  Salem Eid  |  Certified Weil Positivity Beyond the First Prime Threshold: A Five-Rung Coercivity Ladder up to 1.12 log 2  |  https://doi.org/10.5281/zenodo.21720801  |
| 2026 |  Salem Eid  |  Windowed Weil Positivity and the Frame Bound of Dirichlet Zeros: The Quartic Character Modulo Five  |  https://doi.org/10.5281/zenodo.21326836  |
| 2026 |  Sardar Dilbag Singh Khalsa  |  1% Proof of Riemann Hypothesis: An Explicit Li–Kernel Reduction of the Riemann Hypothesis  |  https://doi.org/10.5281/zenodo.18726796  |
| 2026 |  Seer Kai  |  Li Coefficients and the Riemann Hypothesis: Structural Results and Quantitative Improvements (v51-final)  |  https://doi.org/10.57760/sciencedb.35186  |
| 2026 |  Seif Eldin Ahmed Sayed Mohamed  |  A Rigorous Non-Circular Spectral Architecture for the Riemann Hypothesis: Main Paper and Three Complementary A  |  https://doi.org/10.5281/zenodo.22164496  |
| 2026 |  Shekhar Suman  |  Asymptotic of Li coefficients and proof of the Riemann hypothesis  |  https://doi.org/10.6084/m9.figshare.30987823  |
| 2026 |  Shekhar Suman  |  Asymptotic of Li coefficients and proof of the Riemann hypothesis  |  https://doi.org/10.6084/m9.figshare.31009927  |
| 2026 |  Shekhar Suman  |  Asymptotic of Li coefficients and proof of the Riemann hypothesis  |  https://doi.org/10.6084/m9.figshare.31016266  |
| 2026 |  Shekhar Suman  |  Asymptotic of Li coefficients and proof of the Riemann hypothesis  |  https://doi.org/10.6084/m9.figshare.31017844  |
| 2026 |  Shekhar Suman  |  Asymptotic of Li coefficients and proof of the Riemann hypothesis  |  https://doi.org/10.6084/m9.figshare.31023880  |
| 2026 |  Shekhar Suman  |  Li coefficients and proof of the Riemann hypothesis  |  https://doi.org/10.6084/m9.figshare.31000300  |
| 2026 |  Shekhar Suman  |  On the Asymptotics of Li coefficients and Proof of the Riemann Hypothesis  |  https://doi.org/10.13140/rg.2.2.10579.03362  |
| 2026 |  Shekhar Suman  |  On the Asymptotics of Li Coefficients and proof of the Riemann Hypothesis  |  https://doi.org/10.13140/rg.2.2.12824.05121  |
| 2026 |  Shekhar Suman  |  On the Asymptotics of Li Coefficients and proof of the Riemann Hypothesis  |  https://doi.org/10.13140/rg.2.2.15701.08167  |
| 2026 |  Shekhar Suman  |  On the Asymptotics of Li Coefficients and proof of the Riemann Hypothesis  |  https://doi.org/10.13140/rg.2.2.20288.60163  |
| 2026 |  Shekhar Suman  |  On the Asymptotics of Li Coefficients and Proof of the Riemann Hypothesis  |  https://doi.org/10.6084/m9.figshare.31079419  |
| 2026 |  Shekhar Suman  |  On the Asymptotics of Li Coefficients and Proof of the Riemann Hypothesis....  |  https://doi.org/10.6084/m9.figshare.31081426  |
| 2026 |  Shekhar Suman  |  On the Asymptotics of Li Coefficients and Proof of the Riemann Hypothesis....  |  https://doi.org/10.6084/m9.figshare.31082152  |
| 2026 |  Shekhar Suman  |  On the Asymptotics of Li coefficients and Proof of the Riemann Hypothesis  |  https://doi.org/10.6084/m9.figshare.31249744  |
| 2026 |  Simon Velez  |  A Proof of the Riemann Hypothesis by Positivity of the Completed Arithmetic Weil Kernel  |  https://doi.org/10.5281/zenodo.21144565  |
| 2026 |  Singh Ripudaman  |  A Physical Proof of the Riemann Hypothesis via the Hilbert–Pólya Spectral Realisation and the Bost–Connes Stat  |  https://doi.org/10.5281/zenodo.20298131  |
| 2026 |  Sueda Senturk Avci  |  Fourier coefficients of Eisenstein series and explicit computations of Whittaker functionals  |    |
| 2026 |  Sun H  |  基于阿代尔类空间迹公式与本质自伴狄拉克算子的黎曼临界线定理 Riemann Critical Line Theorem via Trace Formulas on Adele Class Spaces and Essen  |  https://doi.org/10.5281/zenodo.20848987  |
| 2026 |  Syaza Afrina Muhamad Sani, Mohamad Ridhuan Abdullah, Hasniza Ibrahim  |  Reliability and Validity Analysis of the Instrument Measuring Instructional Strategies, Algebraic Thinking, an  |  https://doi.org/10.31436/ijes.v14i1.657  |
| 2026 |  T.A. Ziad  |  Localized Constrained Weil Forms: Near-Degeneracy and a Davenport-Heilbronn First Kernel  |  https://doi.org/10.5281/zenodo.23145454  |
| 2026 |  Taebong Kim, Youngsik Hong, Minsik Kim  |  A Numerical Realization of Suzuki's Weil-Quadratic-Form Operator: The Archimedean Spectral Law, its Universali  |  https://doi.org/10.48550/arxiv.2607.24830  |
| 2026 |  Tao Lin  |  Structural Lemmas for the First-Prime Window of the Weil Quadratic Form  |  https://doi.org/10.5281/zenodo.21807497  |
| 2026 |  Tao Lin  |  The Range of a Finite-Scale Weil Positivity Method: Success in the First Prime Window and Termination in the S  |  https://doi.org/10.5281/zenodo.21856509  |
| 2026 |  Taotao Wang, Chonghe Zhao, ShengLi Zhang  |  SemDHT: Certified Semantic Discovery for Peer-to-Peer Agent Networks over Exact-Key DHTs  |    |
| 2026 |  The Clankers  |  Split Support Geometry on the Absolute Arithmetic Curve: Universal Zero Fibres, Arithmetic Curves, and Frobeni  |  https://doi.org/10.5281/zenodo.20822444  |
| 2026 |  Thierry Marechal  |  A Four-Domain Bridge for the Riemann Hypothesis  |  https://doi.org/10.5281/zenodo.19139156  |
| 2026 |  Thierry Marechal  |  A Spectral Program for the Riemann Hypothesis  |  https://doi.org/10.5281/zenodo.19139270  |
| 2026 |  Thierry Marechal  |  Gaussian Diagonal Dominance for Explicit Formulas in Analytic Number Theory  |  https://doi.org/10.5281/zenodo.19219924  |
| 2026 |  Tiago Barbosa Dias Maciel  |  A Computational and Critical Analysis of the Cesàro Regularization Approach to the Riemann Hypothesis  |  https://doi.org/10.5281/zenodo.20573179  |
| 2026 |  Tim Wong  |  A finite-scale audit of the Connes-Consani-Moscovici zeta spectral triples construction  |  https://doi.org/10.5281/zenodo.22046560  |
| 2026 |  Timothy Stroschein, Davide Castaldo, Markus Reiher  |  Ground- and excited-state energies with analytic errors and short time evolution on a quantum computer  |  https://doi.org/10.1103/zy63-92c4  |
| 2026 |  Tongbing Huang  |  A Same-Source Separation Principle for the Weil--Barner Explicit Formula of the Riemann Zeta Function  |  https://doi.org/10.5281/zenodo.21245893  |
| 2026 |  Tosho Lazarov Karadzhov  |  An Arithmetic-Fluctuation Hilbert–Pólya Mechanism: Canonical Principal-Response Mode Closure  |  https://doi.org/10.5281/zenodo.21630053  |
| 2026 |  Tosho Lazarov Karadzhov  |  Paper A0: Terminal Target and Dependency Ledger for the Completed Weil Positivity Program  |  https://doi.org/10.5281/zenodo.21688934  |
| 2026 |  Ulrich Tehrani  |  From Local Curvature to the Weil Functional: An Explicit Construction  |  https://doi.org/10.5281/zenodo.19106992  |
| 2026 |  Ulrich Tehrani  |  Positive Curvature of the Spectral Trace at the Critical Line  |  https://doi.org/10.5281/zenodo.19665790  |
| 2026 |  Ulrich Tehrani  |  Unconditional Negativity of the Second-Moment Bias and Off-Line Robustness  |  https://doi.org/10.5281/zenodo.20792123  |
| 2026 |  Vikram Hatti  |  Exact Negative-Branch Exhaustion for the Pulled-Back Weil Form  |  https://doi.org/10.5281/zenodo.21880255  |
| 2026 |  Vikram Hatti  |  RH Toolkit 4w: Weil Pullback Identification in the Extracted Arithmetic Interface  |  https://doi.org/10.5281/zenodo.20606505  |
| 2026 |  W. Riley Casper  |  Binomial prolate spheroidal functions, Pascal matrices, and arithmetic of elliptic curves  |  https://doi.org/10.1073/pnas.2529171123  |
| 2026 |  Win Eka Rahadyani, Munadi, Yoga Prihatin  |  Development of an Interactive Google Sites-Based E-Module for Mathematical Literacy in Social Arithmetic  |  https://doi.org/10.33394/mpm.v14i1.19615  |
| 2026 |  Xuefeng Zhu  |  A conditional lower bound for windowed Weil forms from sampling on the zeros of ζ  |  https://doi.org/10.48550/arxiv.2608.24827  |
| 2026 |  Yan Ge  |  Optimal differentiability of isotropic positive definite functions on even-dimensional spheres  |  https://doi.org/10.48550/arxiv.2608.26092  |
| 2026 |  Yang Lei, Taotao Li  |  Mellin space reflections, modularity of elliptic Gamma functions and beyond  |  https://doi.org/10.48550/arxiv.2608.24083  |
| 2026 |  Yang Liu¹  |  Structural Construction of the Uniqueness Statement for the Riemann Hypothesis A Chain Map between the Additiv  |  https://doi.org/10.21203/rs.3.rs-11291222/v1  |
| 2026 |  Yaoming Shi  |  Construction of Finite Hilbert--Pólya Matrices from Weil's Explicit Formula  |  https://doi.org/10.48550/arxiv.2609.04908  |
| 2026 |  Ying Ye  |  Arithmetic Dirac Packets, Fargues-Fontaine Slopes, and Weil Positivity: A Conditional Spectral Route Toward th  |  https://doi.org/10.5281/zenodo.20944900  |
| 2026 |  Ying Ye  |  Arithmetic Dirac Packets, Fargues-Fontaine Slopes, and Weil Positivity: A Conditional Spectral Route Toward th  |  https://doi.org/10.5281/zenodo.20945166  |
| 2026 |  Ying Ye  |  Operator Traces, Prime-Power Weights, and a Trace-Compatible Weil Positivity Theorem  |  https://doi.org/10.5281/zenodo.20997605  |
| 2026 |  Ying Ye  |  Screw Functions, de Branges Spaces, and Zeta Spectral Triples: A Spectral-Geometric Approach to RH and GRH  |  https://doi.org/10.5281/zenodo.20998511  |
| 2026 |  Ying Ye  |  Spectral Flow and Categorified Index for Higher-Dimensional Prime-Torus Packets over the Scaling Site  |  https://doi.org/10.5281/zenodo.20944515  |
| 2026 |  Ying Ye  |  Spectral-Geometric Program of the Riemann and Grand Riemann Hypotheses  |  https://doi.org/10.5281/zenodo.21269192  |
| 2026 |  Ying Ye  |  Uniform Convergence of Regularized Determinants for Zeta Spectral Triples: Toward Global Weil Positivity and t  |  https://doi.org/10.5281/zenodo.20998326  |
| 2026 |  Yoshiki Ueoka, Nagi, Akari  |  A Local Toeplitz--Hankel Criterion Equivalent to the Riemann Hypothesis  |  https://doi.org/10.5281/zenodo.21762260  |
| 2026 |  Yuchen Liu, Swaraj Pande  |  On positivity of the limit F-signature  |  https://doi.org/10.48550/arxiv.2605.16636  |
| 2026 |  Yuchen Pei  |  Robinson-Schensted algorithms and quantum stochastic double product integrals  |  https://doi.org/10.82444/warw.33705028  |
| 2026 |  Zac Elston  |  Weil positivity on finite windows across L-functions: certified windows, a pre-registered decay law, and an un  |  https://doi.org/10.5281/zenodo.23163863  |
| 2026 |  Zeraoulia Rafik  |  Uniform Beta Smoothing of Widder Sums for the Riemann ξ-Function and a Schur–Triple Application to Simple Crit  |  https://doi.org/10.5281/zenodo.22801366  |
| 2026 |  Zeraoulia Rafik  |  Uniform Beta Smoothing ofWidder Sums for the Riemann ξ-Function and a Schur–Triple Application to Simple Criti  |  https://doi.org/10.20944/preprints202609.1018.v2  |
| 2026 |  松本耕二, Kohji Matsumoto, 正俊 鈴木  |  M-functions and screw functions: applications to Goldbach's problem and zeros of the Riemann zeta-function  |    |
| 2026 |  正俊 鈴木, Masatoshi Suzuki  |  Aspects of the screw function corresponding to the Riemann zeta‐function  |    |
