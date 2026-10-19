# BIBLIO_CHECK_001 — bibliographic verification, phases 200–205 and Paper 47

Sources: memos from `03-research/phase-200-sign-object/`, `phase-201-untried-families/`,
`phase-204-refd-tractability/`, `phase-205-composing-object/` and `04-papers/47-row-d-dual-certificates/main.tex`.
Method: web search (arXiv, Project Euclid, Wiley, Springer, EUDML, Zenodo API, author pages). When possible I downloaded the
PDF and read the statement: Karnik–Romberg–Davenport (arXiv 2006.00427), Eberwein (Zenodo 23177438), the "two thirds"
preprint, and the Zenodo API for Ziad.

Verdicts: **CONFIRMED** / **CONFIRMED-WITH-CORRECTION** / **NOT FOUND** / **MISATTRIBUTED**.
"IN P47" means the source appears in `main.tex` (cite or text).

---

## Summary (≤300 words)

Almost all citations are correct. **P47 must be corrected at these points:**

1. **`\bibitem{BoasKac1945}`: the volume is wrong.** It says Duke Math. J. **11**. The correct one is **12** (1945), 189–206.
2. **`\bibitem{ZiadDH}`: the author's name is missing.** It says "Ziad" and should say **T. Ziad (Tariq Ziad)**. DOI
   10.5281/zenodo.23145454 is the concept DOI and resolves correctly; the version is 23145455.
3. **`\bibitem{DavenportHeilbronn1936}`: it mixes two papers into a single entry.** They should be split.
   Part I (pp. 181–185): Hurwitz ζ(s,a) with a rational ≠ ½, 1. Part II (pp. 307–312): Epstein with h > 1.
   lem:shape-epstein should cite part II. In rem:FDH the usage is acceptable because it cites DH only for the existence
   of zeros off the line. For the mod 5 example it is worth adding Titchmarsh §10.25.
4. **Priority and overlap, must cite and delineate.** prop:WT, cor:H1minus and prop:H have close precedents published
   on Zenodo in 2026:
   - **B. W. de Andrade Silva, Zenodo 20694588 (15-06-2026).** Polar term 2|C⟩⟨C|−2|S⟩⟨S|, rank-one secular equations
     ⟨C,(B_e−λ)^{-1}C⟩ = −½, and "B_e has a single negative eigenvalue."
   - **L. Eberwein, Zenodo 23177438 (Oct. 2026).** Inertia identity ν(W) = π(I)+ν(S)−1 via a 2×2 matrix at the poles
     (Haynsworth), table of "fake worlds" (DH, Beurling, Epstein), and DH with negative index.
   rem:FDH and thm:noimport/rem:conjunctions must cite Eberwein as RELATED. They are not duplicates: P47 certifies with
   intervals, proves for all T, and works by sectors with the Tate condition.
5. **Outside P47, in a memo:** TOOLS_204U_001 writes the Karnik–Romberg–Davenport constant (Thm 3) as log(50c/π+25).
   The original says **log(100c/π + 25)**. It must be corrected before bringing A∞-sup into P47.
6. **Outside P47, in a memo:** the bound |Σ_{k≤y,(k,e)=1} μ(k)/k| ≤ 1 from P3_SMOOTH_B1 could not be attributed to a
   specific statement by Ramaré. Ramaré 2014 (Acta Arith. 165) gives 2.4(q/φ(q))/log(x/q). It remains UNVERIFIED.

Spira 1994, Hamburger 1921, Landau–Widom 1980, Slepian–Pollak 1961, Mori15 (2^{−2904}) and Kaczorowski–Perelli are confirmed.

---

## 1. Table of sources

| # | Source | Verified citation | URL | IN P47 | Verdict |
|---|---|---|---|---|---|
| 1 | Karnik–Romberg–Davenport | S. Karnik, J. Romberg, M. A. Davenport, «Improved bounds for the eigenvalues of prolate spheroidal wave functions and discrete prolate spheroidal sequences», Appl. Comput. Harmon. Anal. 55 (2021) 97–128; arXiv:2006.00427 | https://arxiv.org/abs/2006.00427 | no | CONFIRMED-WITH-CORRECTION (constant, §2.1) |
| 2 | Landau 1993 | H. J. Landau, «On the density of phase-space expansions», IEEE Trans. Inform. Theory 39(4) (1993) 1152–1156 | (cited as [29] in KRD) | no | CONFIRMED |
| 3 | Landau–Widom 1980 | H. J. Landau, H. Widom, «Eigenvalue distribution of time and frequency limiting», J. Math. Anal. Appl. 77 (1980) 469–481 | — | **yes** (bibitem correct) | CONFIRMED |
| 4 | Eremenko–Novikov | A. Eremenko, D. Novikov, «Oscillation of Fourier integrals with a spectral gap», J. Math. Pures Appl. 83 (2004) 313–365 (PNAS 101 (2004) announcement) | https://www.math.purdue.edu/~eremenko/dvi/novik1011.pdf | no | CONFIRMED |
| 5 | Mitkovski–Poltoratski | M. Mitkovski, A. Poltoratski, «Pólya sequences, Toeplitz kernels and gap theorems», Adv. Math. 224 (2010) 1057–1070 | https://www.researchgate.net/publication/24167140 | no | MISATTRIBUTED journal (the memo says "Acta Math. 2010"), §2.3 |
| 6 | Kaczorowski–Perelli | J. Kaczorowski, A. Perelli, «On the structure of the Selberg class, I: 0≤d≤1», Acta Math. 182 (1999) 207–241 | https://link.springer.com/article/10.1007/BF02392574 | no | CONFIRMED (with nuance, §2.4) |
| 7 | Hamburger 1921 | H. Hamburger, «Über die Riemannsche Funktionalgleichung der ζ-Funktion» (Erste Mitteilung), Math. Z. 10 (1921) 240–254, doi 10.1007/BF01211612 | https://link.springer.com/article/10.1007/BF01211612 | **yes** | CONFIRMED |
| 8 | Hedenmalm–Lindqvist–Seip | H. Hedenmalm, P. Lindqvist, K. Seip, «A Hilbert space of Dirichlet series and systems of dilated functions in L²(0,1)», Duke Math. J. 86 (1997) 1–37 | projecteuclid 10.1215/S0012-7094-97-08601-4 | no | CONFIRMED |
| 9 | Boas–Kac | R. P. Boas Jr., M. Kac, «Inequalities for Fourier transforms of positive functions», Duke Math. J. **12** (1945) 189–206 | http://projecteuclid.org/euclid.dmj/1077472970 | **yes** | CONFIRMED-WITH-CORRECTION (volume 11 → 12) |
| 10 | Robbin–Salamon | J. Robbin, D. Salamon, «The spectral flow and the Maslov index», Bull. London Math. Soc. 27 (1995) 1–33 | https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/blms/27.1.1 | no | CONFIRMED |
| 11 | Simon 1976 | B. Simon, «The bound state of weakly coupled Schrödinger operators in one and two dimensions», Ann. Physics 97 (1976) 279–288 | https://www.sciencedirect.com/science/article/abs/pii/0003491676900385 | no (P47 cites Simon 2005, Trace Ideals; correct) | CONFIRMED |
| 12 | Moreira 2017 | J. Moreira, «Monochromatic sums and products in ℕ», Ann. of Math. 185 (2017) 1069–1090 | annals v185 n3 p10 | no | CONFIRMED |
| 13 | Bergelson–Moreira | V. Bergelson, J. Moreira, «Ergodic theorem involving additive and multiplicative groups of a field and {x+y,xy} patterns», ETDS 37(3) (2017) 673–692; and «Measure preserving actions of affine semigroups and {x+y,xy} patterns», ETDS (online 2016) | https://people.math.osu.edu/bergelson.1/BM_Affine.pdf | no | CONFIRMED (there are two papers: specify which one) |
| 14 | Cohen–Rothblum | J. E. Cohen, U. G. Rothblum, «Nonnegative ranks, decompositions, and factorizations of nonnegative matrices», Linear Algebra Appl. 190 (1993) 149–168 | doi 10.1016/0024-3795(93)90224-C | no | CONFIRMED |
| 15 | Vavasis | S. A. Vavasis, «On the complexity of nonnegative matrix factorization», SIAM J. Optim. 20 (2009) 1364–1377 | doi 10.1137/070709967 | no | CONFIRMED |
| 16 | Moitra | A. Moitra, «An almost optimal algorithm for computing nonnegative rank», SIAM J. Comput. 45(1) (2016) 156–173 (SODA 2013 version) | dblp journals/siamcomp/Moitra16 | no | CONFIRMED (unify year: 2016 journal, 2013 SODA) |
| 17 | Yannakakis | M. Yannakakis, «Expressing combinatorial optimization problems by linear programs», J. Comput. System Sci. 43 (1991) 441–466 | https://www.sciencedirect.com/science/article/pii/002200009190024Y | no | CONFIRMED |
| 18 | Mond–Smith–van Straten | D. Mond, J. Smith, D. van Straten, «Stochastic factorizations, sandwiched simplices and the topology of the space of explanations», Proc. R. Soc. Lond. A 459 (2003) 2821–2845 | — | no | CONFIRMED |
| 19 | Kubjas–Robeva–Sturmfels | K. Kubjas, E. Robeva, B. Sturmfels, «Fixed points of the EM algorithm and nonnegative rank boundaries», Ann. Statist. 43(1) (2015) 422–461 | doi 10.1214/14-AOS1282 | no | CONFIRMED |
| 20 | Padrol–Pfeifle | A. Padrol, J. Pfeifle, «Polygons as sections of higher-dimensional polytopes», Electron. J. Combin. 22(1) (2015) P1.24; arXiv:1404.2443 | https://arxiv.org/abs/1404.2443 | no | CONFIRMED (hexagon: xc 5 or 6) |
| 21 | Bateman–Grosswald | P. T. Bateman, E. Grosswald, «On Epstein's zeta function», Acta Arith. 9 (1964) 365–373 | https://eudml.org/doc/207491 | no | CONFIRMED; threshold **4πe^{−γ} = 7.0556**, not 7.0236 (Q2_DEGREE2 already corrected by AUDIT_200_Q2) |
| 22 | Spira 1994 | R. Spira, «Some zeros of the Titchmarsh counterexample», Math. Comp. 63 (1994) 747–748 | ftp.math.utah.edu toc mathcomp1990 | **yes** | CONFIRMED |
| 23 | Lagarias–Suzuki | J. C. Lagarias, M. Suzuki, «Riemann hypothesis for certain integrals of Eisenstein series», J. Number Theory 118 (2006) 98–122; arXiv math/0412039 | https://arxiv.org/abs/math/0412039 | no | CONFIRMED |
| 24 | Davenport–Heilbronn 1936 | H. Davenport, H. Heilbronn, «On the zeros of certain Dirichlet series», J. London Math. Soc. 11 (1936), I: 181–185; II: 307–312 (doi 10.1112/jlms/s1-11.4.307) | https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/jlms/s1-11.4.307 | **yes** | CONFIRMED-WITH-CORRECTION (split the parts, §2.6) |
| 25 | Kapranov–Schiffmann–Vasserot | M. Kapranov, O. Schiffmann, E. Vasserot, «The spherical Hall algebra of Spec(ℤ)», arXiv:1202.4073 | https://arxiv.org/abs/1202.4073 | no | CONFIRMED (note: 1201.6185 is «The Hall algebra of a curve») |
| 26 | Pavesi | L. E. Pavesi, «Prime-shift operators on Björner's complex of squarefree integers: …Toeplitz–Hankel pipeline for the Guinand–Weil explicit formula», Zenodo 22823015 (18-09-2026) | https://zenodo.org/records/22823015 | no | CONFIRMED (unrefereed) |
| 27 | Mori15 | R. Mori, «Weil positivity on the window of width log 15», Zenodo doi 10.5281/zenodo.23281236 (paper VIII, release v1.6.x) | https://github.com/moriryota/prolate-weil-bounds/releases/tag/v1.6.0 | **yes** | CONFIRMED (Q(f) ≥ 2^{−2904}‖f‖², f ∈ C² with support in [−½log15, ½log15]; P47 uses 2^{−2904}, matches) |
| 28 | Ziad (ZiadDH) | T. Ziad, «Localized constrained Weil forms: near-degeneracy and a Davenport–Heilbronn first kernel», Zenodo, concept doi 10.5281/zenodo.23145454 (version 23145455, 07-10-2026) | https://zenodo.org/records/23145455 | **yes** | CONFIRMED-WITH-CORRECTION (add first name) |
| 29 | van der Geer–Schoof | G. van der Geer, R. Schoof, «Effectivity of Arakelov divisors and the theta divisor of a number field», Selecta Math. (N.S.) 6 (2000) 377–398; arXiv math/9802121 | doi 10.1007/PL00001393 | no | CONFIRMED |
| 30 | Faltings–Hriljac | G. Faltings, «Calculus on arithmetic surfaces», Ann. of Math. 119 (1984) 387–424; P. Hriljac, «Heights and Arakelov's intersection theory», Amer. J. Math. 107 (1985) 23–38 | — | no | CONFIRMED (arithmetic Hodge index on surfaces) |
| 31 | Connes 1976 | A. Connes, «Classification of injective factors. Cases II₁, II_∞, III_λ, λ≠1», Ann. of Math. 104 (1976) 73–115 | https://annals.math.princeton.edu/1976/104-1/p04 | no | CONFIRMED |
| 32 | Cheeger–Gromov | J. Cheeger, M. Gromov, «L₂-cohomology and group cohomology», Topology 25 (1986) 189–215 | — | no | CONFIRMED |
| 33 | Tarski–Seidenberg | A. Tarski, *A Decision Method for Elementary Algebra and Geometry*, RAND 1948 / UC Press 1951; A. Seidenberg, Ann. of Math. 60 (1954) 365–374 | — | no | CONFIRMED (classical; correct use in AUDIT_201_SPEC) |
| 34 | Slepian–Pollak / Landau–Pollak | Slepian–Pollak, BSTJ 40 (1961) 43–63; Landau–Pollak II, BSTJ 40 (1961) 65–84; III, BSTJ 41 (1962) 1295–1336 | https://archive.org/details/bstj40-1-43 | **yes** (SlepianPollak1961) | CONFIRMED |
| 35 | Bonami–Karoui | A. Bonami, A. Karoui, «Uniform bounds of prolate spheroidal wave functions and eigenvalues decay», C. R. Math. Acad. Sci. Paris 352 (2014) 229–234 | http://www.numdam.org/articles/10.1016/j.crma.2014.01.004/ | no | CONFIRMED (upper bounds of ψ_{n,c}) |
| 36 | Ramaré | O. Ramaré, «Explicit estimates on the summatory functions of the Möbius function with coprimality restrictions», Acta Arith. 165 (2014) 1–10; also «Some elementary explicit bounds for two mollifications of the Moebius function», Funct. Approx. 49 (2013) 229–240 | https://eudml.org/doc/279409 | no | **NOT FOUND** in the form "≤ 1" (§2.7) |
| 37 | Wu–Sprung | H. Wu, D. W. L. Sprung, «Riemann zeros and a fractal potential», Phys. Rev. E 48 (1993) 2595 | https://journals.aps.org/pre/abstract/10.1103/PhysRevE.48.2595 | no | CONFIRMED |
| 38 | Burnol | J.-F. Burnol, «Paley–Wiener spaces with vanishing conditions and Painlevé VI transcendents», J. Funct. Anal. 260 (2011) 3222–3251; arXiv:1008.0617 | https://arxiv.org/abs/1008.0617 | no | CONFIRMED |

---

## 2. Notes: what the memo says and what the source says

### 2.1 Karnik–Romberg–Davenport (TOOLS_204U_001, upper bound of A∞)
- **What the memo says** (TOOLS_204U_001 l. 214–216): #{ε < λ_k < 1−ε} ≤ (2/π²) log(**50**c/π + 25) log(5/(ε(1−ε))) + 7.
  The memo itself asks for the constants to be verified.
- **What the source says.** I read the PDF of arXiv:2006.00427. **Theorem 3** (continuous PSWFs, any c > 0, ε ∈ (0,½))
  says #{k : ε < λ̃_k < 1−ε} ≤ (2/π²) log(**100**c/π + 25) · log(5/(ε(1−ε))) + 7.
  The convention for c is the same as the memo uses: there are ≈ 2c/π eigenvalues near 1. For DPSS, Thm 1 gives
  (2/π²) log(4N) log(4/(ε(1−ε))), and Thm 2 gives (2/π²) log(100NW+25) log(5/(ε(1−ε))).
- **Correction.** Where it says 50c/π it should say 100c/π. In the memo's final bound, n₋(𝔪_T) ≤ ⌈2Tt₀/π⌉ + 8 + (2/π²)·log(16Tt₁+25)·log(170T),
  it must say log(100Tt₁/π + 25) ≈ log(31.8·Tt₁ + 25). The order O(log²T) does not change. P47's lem:archcount uses only
  the lower bound and does not depend on this. If A∞-sup enters P47, the bibitem must carry the correct constant.

### 2.2 Landau 1993
- **What the memo says:** λ_{⌈2c/π⌉}(c) ≤ ½.
- **What the source says.** KRD (cited as [29], Landau, IEEE Trans. IT 39(4) 1152–1156) attributes to Landau
  λ_{⌊2c/π⌋−1} ≥ ½ ≥ λ_{⌈2c/π⌉}, with indices starting from 0. Matches the memo. CONFIRMED. It is in the memo but not in P47.

### 2.3 Mitkovski–Poltoratski (MULT_GAUGE_001, M.3)
- **What the memo says** (l. 68): "Mitkovski–Poltoratski gap theorem (CITED, Acta Math. 2010)."
- **What the source says.** The 2010 paper on gaps is «Pólya sequences, Toeplitz kernels and gap theorems», **Adv. Math.**
  224 (2010) 1057–1070. It solves the Pólya–Levinson problem and shows it equivalent to a version of Beurling's gap
  problem for measures. The gap radius is described using the Beurling–Malliavin interior density. I did not find
  either paper in Acta Math. 2010. Poltoratski's Annals 2012 gap theorem is by Poltoratski alone.
- **Correction.** The correct journal is Adv. Math. Also, M.3's use (zeros with density ~(log R)/2π → ∞ ⇒ gapped
  measures exist) needs the "BM density" form of the gap and not just the average density. It is ARGUED in the memo
  and should remain so. Not in P47.

### 2.4 Kaczorowski–Perelli 1999
- **What the memo says** (SPEC_004, COSH_DEFECT): in the Selberg class, degree 1 + conductor 1 + pole at 1 ⇒ L = ζ.
- **What the source says.** Acta Math. 182 (1999) 207–241. It classifies 0 ≤ d ≤ 1: there are no elements with
  0 < d < 1, and those with d = 1 are L(s+iθ, χ) with χ primitive. With conductor 1 this becomes ζ(s+iθ), and the pole
  at s = 1 forces θ = 0. CONFIRMED.
- **Nuance.** The hypothesis includes the Euler product and Ramanujan's axioms (Selberg axioms). P47's rem:conjunctions
  uses Hamburger and not Kaczorowski–Perelli, which is correct for a Dirichlet series over ℕ with ζ's functional
  equation. No bibitem is needed.

### 2.5 Spira 1994 (IN P47, rem:FDH)
- Math. Comp. 63 (1994), no. 208, 747–748. The title is confirmed. Several secondary sources (search; Balanzario–Sánchez-Ortiz,
  Math. Comp. 76 (2007) 2045–2049) attribute to Spira the zero 0.808517… + 85.699348…i in the critical strip. P47's
  bibitem is correct. AUDIT_200_CERTDH_001's recommendation (C1) is already applied: DH for existence, Spira for the
  value. Eberwein (Zenodo 23177438, §11.4) reproduces the same zero and a second one at 0.650830+114.163343i, and gives
  κ in closed form: κ = (√(10−2√5)−2)/(√5−1) = 0.28407… P47 can cite that closed form.

### 2.6 Davenport–Heilbronn 1936, parts I and II (IN P47)
- **What each part says** (matching secondary sources: arXiv 2005.00941, arXiv 1204.6297, Wiley):
  - **Part I**, J. London Math. Soc. 11 (1936) 181–185: the Hurwitz ζ(s,a) with a rational ≠ ½, 1, and also the
    transcendental case, has infinitely many zeros in σ > 1.
  - **Part II**, J. London Math. Soc. 11 (1936) 307–312: the Epstein ζ_Q of a binary form with class number h > 1 has
    zeros in σ > 1, and hence off the line.
  - The "DH" mod 5 function is the one Titchmarsh exposes in §10.25. The existence of zeros in σ > 1 comes from DH's
    method. The zeros in ½ < σ < 1 are proved by Voronin and others, and were computed by Spira.
- **In P47.** The bibitem merges both parts ("181–185 and 307–312"). It is acceptable, but it is better to split into
  `DH1936a` and `DH1936b`. lem:shape-epstein uses part II for Q = x²+5y² (h = 2), and that is correct. rem:FDH uses DH
  for "existence of such zeros." That is correct if it refers to zeros off the line in general (in σ > 1). Suggestion:
  "zeros off the line, in σ > 1 \cite{DH1936}, and in the strip (Spira's value \cite{Spira1994}; cf. \cite[§10.25]{Titchmarsh1986})."
- **The memo DH_TRANSFER_001** (l. 73) attributes to Voronin the infinitely many zeros in ½ < σ < 1. That is correct
  (Voronin 1980), but the full citation is missing: S. M. Voronin, Izv. Akad. Nauk SSSR 44 (1980). I did not verify it
  in detail and it is not in P47.

### 2.7 Ramaré (P3_SMOOTH_B1_001 l. 162)
- **What the memo says:** |Σ_{k≤y,(k,e)=1} μ(k)/k| ≤ 1, "CITED, Ramaré; verify source."
- **What I found.** Ramaré, Acta Arith. 165 (2014) 1–10, proves |Σ_{d≤x,(d,q)=1} μ(d)/d| ≤ 2.4·(q/φ(q))/log(x/q) for
  x > q ≥ 1. The abstract and introduction mention a previous uniform bound of 1. In the literature this is attributed
  to Granville–Soundararajan and it also appears in Ramaré, Funct. Approx. 49 (2013). The unrestricted bound
  |Σ_{d≤x} μ(d)/d| ≤ 1 is classical and elementary. **I could not locate the exact statement with (k,e)=1 and constant
  1.** Verdict NOT FOUND. Until it is verified, it should be replaced by the version 2.4(q/φ(q))/log(x/q), or by the
  trivial bound of the form |m_q(x)| ≤ ∏_{p|q}(1−1/p)^{-1}·… The memo's result is ARGUED and is not in P47.

### 2.8 Bateman–Grosswald and Lagarias–Suzuki
- B–G, Acta Arith. 9 (1964) 365–373: gives the proofs of two theorems announced by Chowla–Selberg on real zeros of the
  Epstein zeta function. Lagarias–Suzuki (JNT 118 (2006) 98–122) prove that the constant term of the Eisenstein series
  has real zeros if and only if y > 4πe^{−γ} = 7.0555…, and relate that threshold to the B–G criterion, whose leading
  term is y* = 4πe^{−γ}. The figure 7.0236 from Q2_DEGREE2_001 (l. 16, 182, 310, 335) is **wrong**. AUDIT_200_Q2_001
  already corrected it, but Q2_DEGREE2 still has the old figure and a "†". Not in P47.

### 2.9 Boas–Kac (IN P47; P4_SIGNPATTERN)
- **What the memo says:** in dimension 1, every continuous positive-definite function supported on [−2T,2T] is an
  autocorrelation f∗f̃ with f supported on [−T,T]. That is why the LP with ĉ ≥ 0 coincides with def:PD.
- **What the source says.** Boas–Kac 1945 (Duke 12, 189–206) proves that representation on ℝ. Krein 1940 gives the
  continuous version and Rudin shows it fails in dimension ≥ 2. CONFIRMED. **P47's bibitem has the wrong volume
  (11 → 12).**

### 2.10 The rest
- **Eremenko–Novikov:** SPEC_011 C3's statement matches the abstract (Logan's conjecture: if f̂ = 0 on (−a,a), the
  lower density of sign changes is ≥ a/π). CONFIRMED.
- **Hedenmalm–Lindqvist–Seip:** the "cyclicity / Bohr lift" usage corresponds to the Dirichlet ℋ² framework and to
  dilations in L²(0,1). CONFIRMED.
- **Robbin–Salamon:** the crossing form and spectral flow are in BLMS 27 (1995). AUDIT_204_TRACT_D cites it correctly.
- **Simon 1976:** Ann. Phys. 97, necessary and sufficient conditions for a bound state with small λ in 1D/2D. Matches
  the "weak coupling" usage.
- **Moreira and Bergelson–Moreira:** the data are correct. Bergelson–Moreira has two papers in ETDS; the memos must
  state which one they cite.
- **Yannakakis, Cohen–Rothblum, Vavasis, Moitra:** match AUDIT_201_SPEC_001. Yannakakis was "from the auditor's
  memory" and is now verified: JCSS 43 (1991) 441–466. Moitra: unify as SIAM J. Comput. 45 (2016) (SODA 2013).
- **Mond–Smith–van Straten, Kubjas–Robeva–Sturmfels, Padrol–Pfeifle:** CONFIRMED. The corrected attribution in
  AUDIT_201 (nonnegative-rank boundaries, hexagons with xc 5 or 6) is correct.
- **Kapranov–Schiffmann–Vasserot:** 1202.4073 is «The spherical Hall algebra of Spec(ℤ)». In that work the Eisenstein
  functional equation comes out of the Hall algebra of lattices, and FAMILIES_A_001 uses it that way. Correct.
- **Pavesi:** exists, Zenodo, 18-09-2026, unrefereed.
- **van der Geer–Schoof, Faltings–Hriljac, Connes 1976, Cheeger–Gromov, Tarski–Seidenberg:** classical, verified, and
  the memos use them correctly.
- **Bonami–Karoui:** CRAS 352 (2014). Gives uniform bounds of ψ_{n,c} and of the decay. K3_GAMMA's "‖ψ_k‖²_∞ ≲ √c" is a
  paraphrase: the explicit bounds depend on n and c. Before bringing constants into P47, the exact statement must be read.
  Remains CONFIRMED as to the existence of the result.
- **Wu–Sprung:** PRE 48 (1993) 2595. «Inverse scattering, the coupling constant spectrum and the Riemann hypothesis»
  (hep-th/0111067) is by **N. N. Khuri**, Math. Phys. Anal. Geom. 5 (2002) 1–63 (verified on arXiv). FAMILIES_B_001
  l. 129 and 407 attributes it to Wu–Sprung: **MISATTRIBUTED**.

- **Burnol:** arXiv 1008.0617 = J. Funct. Anal. 260 (2011). Contains the μ function, the Krein system, and the
  Painlevé VI transcendents. CONFIRMED.

---

## 3. Duplicates: new PROVED results from P47 (batch 200–205)

Searches: "Weil positivity window", "truncated Weil quadratic form inertia", "Davenport–Heilbronn Weil form window",
"Epstein zeta Weil positivity", "negative eigenvalues window Weil archimedean", "inertia identity 2×2 poles". Relevant hits:

- **[E] L. Eberwein**, «The truncated Weil quadratic form: inertia, visibility, structural measurements, and no-go theorems for the
  Riemann Hypothesis», Zenodo doi 10.5281/zenodo.23177438; GitHub loganeberwein6/Logan-Eberwein-RH-Weil-Window).
  I read the PDF. §2 "Result 1": with α = aᵀI⁻¹a, β = bᵀI⁻¹b, γ = aᵀI⁻¹b and S = [[α, γ−1],[γ−1, β]], ν(W) = π(I)+ν(S)−1
  holds (Haynsworth). Positivity ⟺ π(I) ≤ 1 and S ⪰ 0. §10.2 is a table of "fake-world barriers": DH (functional
  equation + Dirichlet form), Beurling DMV (Euler + PNT) and Epstein h > 1. §11.4: DH, negative index on the zero side,
  numerical (floats).
- **[S] B. W. de Andrade Silva**, «A scalar Herglotz criterion for the even-simplicity hypothesis in the localized Weil quadratic
  form», Zenodo 20694588 (15-06-2026). Polar term 2|C⟩⟨C|−2|S⟩⟨S| with C = cosh(x/2), S = sinh(x/2). "B_e has a single
  negative eigenvalue (the Perron ground of the pole-free part)." Secular equations ⟨C,(B_e−λ)^{-1}C⟩ = −½ and
  ⟨S,(B_o−λ)^{-1}S⟩ = +½. The verification is numerical for concrete parameters.
- **[Z] Zhu**, arXiv:2608.24827: already in the bib. Covers the Landau–Widom decay and the two bounds. Does not cover
  DH, Epstein, or the inertia.
- **[ZD] Ziad**, Zenodo 23145454: already in the bib. Restricted negative witness for DH at a = 9/5.
- **[A] L. Alpöge, R. Furman**, «More than two thirds of the zeta zeros are simple and on the critical line», arXiv 2608.13637.
  Uses Sylvester's law of inertia on a finite compression of the Weil form. Their results "hold for
  Davenport–Heilbronn and Epstein" as insensitivity to o(N) zeros off the line.
- **[GH] GitHub AlexanderEastwood/riemann PR #56** (23-09-2026): numerical diagnosis of DH's detection window, without
  a certificate.
- **[CC] Connes–Consani**, Selecta 2021 (in the bib): the archimedean part stops being positive shortly after log 2.

| P47 result | Closest hit | Verdict | Comment |
|---|---|---|---|
| lem:shape-epstein (Epstein x²+5y², negative on P_T ∀T ≥ 1.59, cosh decomposition) | [E] §10.2 (Epstein as a "fake world," no window computation); [A] | **RELATED** | I found no window certificate for Epstein nor the decomposition Λ_Q = ½(Λ_K+Λ_ψ)+Λ_cosh. It is worth citing [E] for the falsifier idea. |
| rem:FDH (DH negative ∀T ≥ 9/5, certified witness) | [ZD] (already cited, −6.169e−9 at 9/5); [E] §11.4 (numerical, zero side); [GH] | **RELATED** (priority for the value at 9/5 belongs to Ziad, and P47 already acknowledges it) | The propagation to all T ≥ 9/5 via lem:monoT and the 7000-bit certificate do not appear elsewhere. Add [E] as an independent reproduction of the zero side. |
| rem:shape-additive (additivity under products) | — | **NOT FOUND as a statement; it is folklore** | It is the linearity of the explicit formula in −L′/L, conductor, and Γ. It should be called "standard" without claiming novelty. |
| thm:noimport | [E] §10.2 "fake-world barriers (methods that see only X)"; already in Paper 46 | **RELATED (strong)** | Same pattern: a method that sees only X cannot distinguish the fake world. P47 formalizes it via lem:transfer with (iii) conditioned on κ_T ≠ 0. [E] must be cited. |
| rem:conjunctions (Hamburger ⇒ no falsifier) | [E] (keeps/loses table); classical Hamburger | **RELATED** | Cite [E]. |
| prop:WT (inertia by sectors via the resolvent, a(h)=1/q) | [S] (rank-one secular equation with the same C, S); [E] §2 (Haynsworth, 2×2 polar matrix) | **RELATED (strong; partial priority of [S] and [E])** | P47 uses the same Schur/Haynsworth machinery. The novelty is the closed form by sector with χ_par and the closed form with domain. [S] and [E] must be cited and delineated. |
| cor:H1minus (the even sector has one negative direction) | [S]: "B_e has a single negative eigenvalue" (numerical) | **RELATED (near-duplicate in statement, not in proof)** | [S] asserts it with numerical verification. P47 proves it. [S] must be cited. |
| prop:H (even inertia across all windows) | [S], [E] | **RELATED** | Neither proves it for all T. |
| lem:archcount (≈4T archimedean negative directions) | [CC] (the archimedean part is not positive beyond log 2); [E] l. 1476 ("archimedean weight ω(t) negative") | **RELATED** | I found no count n₋ ≥ ⌈2Tt₀/π⌉−1. Cite [CC] as qualitative precedent. |
| rem:inertiatower | [E] §2 (inertia of W via I and S) | **RELATED (weak)** | — |
| rem:sosatoms (square of the comb with rational atoms) | — | **NOT FOUND** | — |

**Conclusion on duplicates.** There is no strict DUPLICATE. There are two overlaps that require citation: [S], Zenodo
20694588, for prop:WT and cor:H1minus, and [E], Zenodo 23177438, for prop:WT, thm:noimport, rem:conjunctions and
rem:FDH. Both are unrefereed preprints from 2026, preceding this batch. They must be added to the bib and noted in
ROUTES-TRIED-INDEX as literature.

## 4. Concrete corrections for P47

1. `BoasKac1945`: "\textbf{11}" → "\textbf{12}".
2. `ZiadDH`: "Ziad" → "T.~Ziad". Optional: "version doi 10.5281/zenodo.23145455".
3. `DavenportHeilbronn1936`: split into I (181–185, Hurwitz) and II (307–312, Epstein h>1). lem:shape-epstein → II.
   rem:FDH: add \cite[§10.25]{Titchmarsh1986}.
4. New bibitems: `Silva2026` (Zenodo 20694588) and `Eberwein2026` (Zenodo 23177438). Cite them in prop:WT, cor:H1minus,
   thm:noimport, rem:conjunctions and rem:FDH.
5. rem:shape-additive: declare it "standard," without claiming novelty.
6. If A∞-sup (TOOLS_204U) enters: bibitem KRD (ACHA 55 (2021) 97–128, Thm 3) with log(100c/π+25), and Landau 1993
   (IEEE IT 39, 1152–1156).

## 5. Corrections in memos (not P47)
- MULT_GAUGE_001 l. 68: "Acta Math. 2010" → "Adv. Math. 224 (2010) 1057–1070".
- Q2_DEGREE2_001: 7.0236 → 7.0556 = 4πe^{−γ}.
- P3_SMOOTH_B1_001 l. 162: Ramaré's bound "≤ 1" with coprimality remains UNVERIFIED. Use 2.4(q/φ(q))/log(x/q) (Acta Arith. 165).
- FAMILIES_B_001 l. 129/407: hep-th/0111067 is by N. N. Khuri (MPAG 5 (2002) 1–63), not Wu–Sprung.
- TOOLS_204U_001 l. 216: 50c/π → 100c/π.
