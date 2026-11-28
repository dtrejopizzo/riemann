# Fixed window 2.8022: certificate located and run

Date of this check: 2026-11-28. Scope: locate and check the certificate of 17 verifications cited by paper 46, without searching for or optimising the endpoint T. Papers 47/48 were not consulted. The audit of the analytic bridge of the research notes is carried out separately in the main review: this document does not turn the running of the code into an automatic certification of the functional inequality.

## Result replacing the earlier incomplete search

**The certificate exists, is public and runs successfully.** The earlier assertion that the file was missing must be withdrawn. The search limited to the papers did not find the code because it is in the research tree:

- File: `03-research/phase-213-new-constructions/verify_periodic_pivot_280.py`, 81 lines, 3368 bytes.
- Earlier analytic proof and adaptation: `03-research/phase-213-new-constructions/ROUND_195_A.md:3897–3903` and `:5167`.
- Corresponding statement: `04-papers/46-row-d-sign-radial-intersection-form/main.tex:1914–1930`.
- Public revision consulted: `97fb4e78d5a858baa926829a42336ae3b914e59a`.
- [Public file pinned to that revision](https://github.com/dtrejopizzo/riemann/blob/97fb4e78d5a858baa926829a42336ae3b914e59a/03-research/phase-213-new-constructions/verify_periodic_pivot_280.py).
- Local and remote SHA256 identical: `2a3dbca06c75e6e7557978263997f146d50aa96259a43f7ce77a7fff46adff68`.

The decisive search was `rg -l --hidden`, excluding `.git`, the directories 47/48 and these reports, with the expression `120110026807|120122483651|2673507086718`. It found the script, ROUND_195_A, papers 46/58 and ROUTES-MASTER-INDEX. The recursive GitHub API reported an untruncated tree; the raw file of the indicated revision was downloaded and compared byte by byte with the local one.

## Run and content of the 17 verifications

It was run directly, without editing it:

```sh
python3 03-research/phase-213-new-constructions/verify_periodic_pivot_280.py
```

Environment: python-flint 0.9.0; Arb precision 192 bits fixed by the code itself, line 5. Exit code 0; the 17 checks emitted PASS. Parameters coinciding exactly with paper 46: T=14011/5000, U=57/20, R=2014985964, b=13, m=9115062736, H=2673507086718, G=3000000000000 and N=120122483651. No search for parameters was carried out.

| # | Line of the script | Label and inequality checked | Result |
|---|---:|---|---|
| 1 | 21 | `prime enumeration range`: exp(2U)<300 | PASS |
| 2 | 49 | `positive symmetric weights`: the 2048 integer weights are positive and symmetric | PASS |
| 3 | 52 | `all continuous Schur rows`: each upper row is strictly smaller than 19.486 times its weight | PASS |
| 4 | 53 | `support`: T+(b+1)(m+48)/H<U and 2U<13/2 | PASS |
| 5 | 55 | `archimedean margin`: log(R/(2π))−1/R−1/(2R²)−19.486>1/10 | PASS |
| 6 | 56 | `global low floor`: ψ(1/4)−logπ−19.486>−26 | PASS |
| 7 | 57 | `spectral regions`: G≤2H, H<G and 2R<H | PASS |
| 8 | 62 | `mask band edge`: v<1 and the two quantities written exceed 7a/2 | PASS |
| 9 | 70–71 | `polar and signed low band versus gain`: logarithmic gain exceeds polar cost and 2logJ by more than 10; polar cost positive | PASS |
| 10 | 72 | `denominator floor`: m arcosh(2/a−1)<120110026806 | PASS |
| 11 | 73 | `low mask positive`: a<1/2 and m arcosh(2/a−1)−log4>2logJ | PASS |
| 12 | 74 | `cutoff prefactor`: 2·16·exp(19/4)·25/(2π)<10⁵ | PASS |
| 13 | 75 | `cutoff tail ratio`: H+2.718N<G | PASS |
| 14 | 76 | `low correction`: log(10⁹)+loglog(3+G)−Nlog2.718<−120110026808 | PASS |
| 15 | 78 | `series converges`: z=m/cosh²b<1 | PASS |
| 16 | 80 | `high correction`: high=2z²⁵/(1−z)<1/2 and high·10⁹log(3+G)<1/1000 | PASS |
| 17 | 81 | `reserved density`: 1/(80π)>1/1000 | PASS |

The expressions a, v, J, cost and gain are defined in lines 58–69. The Arb comparisons certify strict separation of intervals; an undecided comparison is not treated as PASS. `unique_fmpz()` requires the floors and ceilings used to be a unique integer.

## What the Schur part does prove, without extrapolating a mesh

This part can be justified directly from the code. Let h=2U/2048 and w the positive function constant on the cells, extended by 0 outside the window. For each prime power q=p^k, the code obtains d=floor(log(q)/h) and c=ceil(10⁸log(p)/sqrt(q)). A point x of cell i translated by log(q) belongs, except for boundaries of measure zero, to cell i+d or i+d+1. Hence the maximum of the two neighbouring weights of line 36 is a valid bound **on the whole cell**, not only at the nodes. If the translate leaves the window the weight 0 is used. The symmetry of w identifies the bound for negative translations with the reflection of the positive one, line 41.

The enumeration of primes by division up to isqrt(p) is exact. All the relevant powers are enumerated: exp(2U)<300, and those with shift greater than or equal to the number of cells do not contribute in L². The bound on each coefficient is upwards. Line 52 checks by integer arithmetic the 2048 Schur inequalities. Consequently, the symmetric operator of translations by prime powers, with coefficients log(p)/sqrt(q) in both orientations, has norm≤19.486 on that window.

The 70 preliminary iterations only produce a candidate for the weights. No hypothesis of convergence or optimality of those iterations is used: positivity, symmetry and the final inequality are checked afterwards. **Verdict (a) for this Schur bound as the certificate implements it.**

## Analytic bridge that must accompany the certificate

ROUND_195_A:3897–3903 first describes T=14/5 and earlier parameters. Line 5167 replaces the parameters and the exponent by the current ones and asserts that the same proof is preserved. This location is substantially different from an absence of proof or code.

To certify the universal inequality of paper 46 it is necessary to verify, in addition to the 17 numerical results, these concrete obligations in the earlier formulas 179/190/192/193 of the notes:

1. Definition of the entire multiplier of exponential type, its non-negative mask and the reciprocal polynomial truncated at degree 24; justification of the support T+(b+1)(m+48)/H and of the factor J=25(2m)^24.
2. Passage from the leakage of Fourier mass to the Chebyshev gain, with the factors 1/10, 26, 4, 80 and the Plancherel normalisation.
3. Identification of B with the Chebyshev denominator and translation of check 10 into the exponential bound for B.
4. Construction of the cutoff with N uniforms; error density of exterior zeros and constant 10⁹log(3+G), based on Z2/Z3. The quotient 2.718 and the prefactor of check 12 only verify the numerical hypotheses of that estimate.
5. High tail of the mask≤2z²⁵/(1−z)(H/|τ|)^50, sign on the atoms, reserve 1/(80π) and complete coverage of spectral regions.
6. Extension from smooth functions to the closed domain of the form and monotonicity by inclusion of supports.

The main review examines these obligations. **Status of this document: numerical run and Schur proved; complete functional inference conditional on the closure of that bridge.** This is not a verdict of falsity of the bound nor an allegation of an absent certificate.

## Z1: primary source and independent check of the exact datum used

Paper 46:1788–1791 needs only: there exists a simple zero in 1/2+i[14.13,14.14] and there are no other non-trivial zeros with 0<Imρ≤21. The version for negative heights is deduced by conjugation. It does not require the additional decimals printed.

[Platt–Trudgian, The Riemann hypothesis is true up to 3·10¹²](https://arxiv.org/pdf/2004.09765), Theorem 1 and §2, pages 2–3, was consulted directly. The theorem gives the scope; the methodological description explains that they count sign changes and collate them with the total number by means of Turing. Equality between the number of intervals with sign change and the total number of zeros **with multiplicity** implies simplicity: each interval contributes at least one unit and a multiple zero would consume more. The theorem on RH by itself, without this counting argument, would not justify simplicity. This article does not print a table with the first two ordinates; a non-existent table is not attributed to it.

As a separate check of the precise part of Z1 the following was run, also at 192 bits:

```python
from flint import acb, arb, ctx
ctx.prec = 192
rho = acb.zeta_zero(1)
assert arb(1413)/100 < rho.imag < arb(707)/50
assert rho.real == arb(1)/2
assert arb(21).zeta_nzeros() == 1
```

The three assertions pass. Result for the first ordinate:

`[14.1347251417346937904572519835624702707842571156992431757 +/- 1.77e-56]`.

N(21) returns the exact integer 1. This number counts the critical strip, not only the zeros already located on the line. Existence of the isolated zero and N(21)=1 suffice for uniqueness and simplicity. The semantics was collated with the primary sources of the program: [FLINT documentation on zeros](https://flintlib.org/doc/acb_dirichlet.html) and [counting function N(t)](https://flintlib.org/doc/acb_dirichlet/acb_dirichlet_zeta_nzeros.html). This is a check of Z1 at height 21, not a search for the endpoint of the window. An independent second check carried out the same verification.

**Verdict (a) on the mathematical content of Z1 used.** The direct historical consultation of the original Rosser–Yohe–Schoenfeld 1968 was not completed here; for that reason not every page of that reference is taken as collated. The preceding confirmation does not depend on attributing to it results that were not read.

## Subsequent closure of the bridge

The functional bridge was reconstructed in the main review and reviewed independently by the theta review. See [WINDOW-28022-BRIDGE.md](WINDOW-28022-BRIDGE.md). The 17 checks, together with that argument and Z1–Z3, do give the universal inequality on the declared window. The conditional status of the preceding historical sections is superseded by this closure. Paper 46 reports the result without developing that argument: for a self-contained reading it must incorporate or cite precisely these annexes and the program.

## Second independent review of the analytic bridge

After the first delivery `WINDOW-28022-BRIDGE.md` of the main review was read in full and collated with ROUND_172_A,173_A,175_A,178_A,179_A,190_A,192_A; with the initial construction of ROUND_193_A; and with ROUND_195_A:3897–3903,5167. No substantial failure was found in this reconstruction. The following checks were redone, not inferred from the PASS result:

- **Signed spectral identity.** The pairing β↔1−β replaces the real exponentials by cosh(δt); the trimmed correction reproduces the same datum on the differences of both supports. The cutoff is 1 up to 6.5 and 2U=5.7. The summable bound on the corrections and the logarithmic growth of their density justify the exchange for smooth tests. Hence the exact subtraction between W(f) and W(g) does produce the factor 1−Q² against the same measure, without presupposing that this measure is positive.
- **Entire filter.** The even series of cosh eliminates the branch of the root. The inequality |Re sqrt(1−(x+iy)²)|≤sqrt(1+y²) controls the type; multiplying by the polynomial of degree m/2+24 costs exactly (m+48)(b+1)/H. The real bound on Q allows Paley–Wiener in L². The inverse transform is a distribution of compact support; convolving it with a smooth test preserves smoothness and the declared support.
- **Reciprocal coefficients.** The roots r_i∈(0,a) give the product ∏(1−v/(1−r_i))⁻¹. Its coefficients are sums of complete monomials, dominated by the multinomial expansion of (Σ_i(1−r_i)⁻¹)^j, whence c_j≤m^j. On 0≤u≤a, J=25(2m)^24 dominates the sum; on a≤u≤1 the truncation has positive sign and does not exceed the reciprocal. The two regions prove 0≤Q²≤1 globally. The tail begins precisely at degree 25, whence the power 50, not 48.
- **Leakage.** In the strip of the proof of 179, Re cos(x+iy)=cos(x)cosh(y)≥cos(x)|sinh(y)|=|Im sin(x+iy)|. Thus the auxiliary function is bounded without a hidden growth hypothesis. On the edges its argument is real exterior. The integral of J over [−A,A] includes exactly the weight 2d of each interior frequency; the denominator of η as written is obtained, also for complex f.
- **Pole and gain.** u(i/2)≤0; |1−u(i/2)|≤2 and |u(i/2)|≤(b+2)/(2H²) with these parameters. The Chebyshev bound at the negative argument introduces arcosh(1+(b+2)/(H²a)), without an additional factor 2. The factor m appears after squaring the Chebyshev of degree m/2. The polar cost 4exp(T) is a valid bound by Cauchy–Schwarz. From the two gain inequalities with margin 10 one deduces rigorously gain−polar_cost−26J²>2, since both polar_cost and J² are ≤exp(gain_log−10), and J≥1.
- **Two tails and normalisation.** The low correction is a density with respect to dτ, which is why it costs 2πexp(−D−2) in units of ‖f‖². The high reserve is a density with respect to dτ and is at least 1/(80π), using Q²≥1/2. H≥G/2 guarantees that it exists throughout the range where it is used. The inequality 2π/e²<1 allows the low tail to be subtracted from the more than 2B kept while still leaving more than B, with B>exp(−D). The same reserve was not counted twice.

**Precision about endpoints in the unit count.** To count zeros in [j,j+1), the quotient N(j+1)−N(j) could omit a zero located exactly at j. There is no need to assume absence of such zeros. For j≥3 use N(j+1)−N(j−1), which includes the complete interval with multiplicities. If M(t)=t/(2π)log(t/(2πe))+7/8 and E(t)=0.137logt+0.443loglogt+1.588, Z3 gives

`N(j+1)−N(j−1) ≤ log(j+1)/π + 2E(j+1) < 4log(3+j)`.

The last inequality follows from loglog(j+1)≤log(j+1) and log(3+j)≥log6. The constant 100 used in the bridge keeps an ample margin. The small heights are covered by Z1, and the negative ones by conjugation. This precision avoids a tacit hypothesis about integer heights without altering any numerical check.

For the grouping of tails, at most four unit intervals cover l≤|τ−γ|<l+1. The inequality log(3+|j|)≤log(3+|τ|)+log(3+l) follows even allowing for the additional shift of the endpoints, since (3+|τ|)(3+l)≥5+|τ|+l. The sums bounded in the bridge give a cost ≤4·10⁷[2log(3+|τ|)+2log3+3], smaller than 10⁹log(3+|τ|). The factor 2.718⁻ᴺ can be extracted uniformly in the low region because only zeros with |γ|>G correct, and G−H>2.718N.

**Updated verdict:** the fixed-window inequality is **reconstructed correctly with the research annexes, Z1–Z3 and the certificate run**, subject to the conventions and to the closure of the domain already audited for paper 46. It must not be reformulated as "paper 46 contains by itself this whole proof": its lines 1914–1930 report the result without developing this bridge. The precision about counting endpoints above is an explicit repair of the exposition, not a change of hypotheses or of parameters.

Bibliographic complement on Z1 reported by the spanning review: [historical Arb 2.23 documentation of acb_dirichlet](https://arblib.org/acb_dirichlet.html) specifies that N(t) counts multiplicities; it is a primary source additional to the current FLINT documentation.
