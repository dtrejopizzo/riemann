# Paper 46: closure of the pure analytic blocks

Date: 2026-11-28. Source: `04-papers/46-row-d-sign-radial-intersection-form/main.tex`. Full reading of 248–1598, 1783–1908 and 1930–2454; certificates 1598–1782 in NUMERICS-46 and its cross-review. The references below are lines of that source, not PDF pages. "a" validates the mathematical statement indicated; explicit errata are classified separately. A result conditional on the arithmetic input is not turned into an unconditional proof of RH.

## Verdicts on the author's questions

1. **(a)** The equivalence between positivity of the complete form on all windows and RH: explicit formula, Weil criterion, real/complex step and density of the form kernel are compatible. See the all-support development of ANALYTIC and report 01. It is not an equivalence between positivity on a fixed window and RH. Nor are primitive and complete positivity on a window interchangeable without the polar Schur.
2. **(a), by independent reproduction**, the four bounds at T=log(5)/2 and their extension by monotonicity; NUMERICS-46 and NUMERICS-46-CROSS-REVIEW contain the certificates. The original description without a program does not replace these certificates. The certified success uses preconditioned congruence and Gershgorin; it is not claimed that the naive interval factorisation passed.
3. Z1–Z3 and their use in `thm:margin/cor:margin1`: **(a)** for the final bounds, with a minor precision explained below. The use for T=2.8022 belongs to the separate WINDOW-28022 report; it is not duplicated here.

## Obligations reconstructed

| Lines / labels | Verdict | Effective check |
|---|---|---|
| 248–333, comparison, eq:W | a except erratum 277 | Factor 1/(2π), mass v_n=2Λ(n)/√n, pole 2AB and signs coincide; boundary contacts have zero autocorrelation. |
| 335–417, lem:K, thm:S, thm:A | a | Digamma expansion gives K; φ(x)=Σx/[a_k(x+4a_k²)] is complete Bernstein; tail integral and jump form with factors 1/4 and 1/2 checked. The quadratic conditions of Kprim are not unduly identified with A=B=0. |
| 420–455, cor:mono, lem:mbounds | a for inequalities | The upper bound is also proved directly by concavity of φ and Jensen on the space of the first three Dirichlet sines: ∫φ(τ²)|Fhat|²/(2π)≤φ(∫τ²|Fhat|²/(2π))≤φ((3π/2T)²). Two moments leave dimension≥1. There is no need to decide the exact numbering of Song–Vondraček for this conclusion. Binet remainder by integration by parts≤1/(2|z|). |
| 457–557, form-density, monoT, compact, contA | a | Contraction of support and approximation in log weight; correction by two functions with independent moments; Fourier tail and Hilbert–Schmidt kernel in a band give compactness; semicontinuity and contraction give continuity of minima. |
| 559–704, prop:weak, gbounds, D1, D1W, O | a | Boas–Kac with complex root of half support; finite cone separation by means of Cesàro means; independence of moments through boundary terms; tightness by coercive symbol; limit of dense restrictions. The non-attainment uses a non-zero entire transform and the singularity K/2 at zero. |
| 705–817, W, lem:W, P, roughEF | a for identities and variation | Annihilator of the moment kernel, witnesses of the two signs, normalisation by means of the moment kernel; regularising convolution of support T+ε and dominated convergence of the sum over zeros. |
| 818–1028, F1, T0, T, T2, hybrid, E, M, TAY | a for bounds | Separation between periodicity of atoms and non-periodic prime contacts; monotone caps; approximation of atoms with uniform control of variation; L1 density by uniqueness of Laplace; Taylor with second derivative and monotone terms at the left endpoint. The informal cost rule c^(-1/2) is not interpreted as universal complexity. |
| 1029–1219, Z, Zexh, finZ, KEP1/2/dich | a | Densities and atoms complete the explicit formula exactly. In Zexh the boundary atom is kept; positive denominator outside 2T≥log2; cuts around finitely many contacts have arbitrarily small L1 cost. In finZ, an absolutely continuous measure with local transform equal to a finite sum would have countable support: contradiction. A bounded exterior perturbation produces a continuum of Krein solutions when margin>0. |
| 1220–1360, arch, nodes, parity, zeroext, strict | a for mechanisms and results | Jump K>0 gives positivity improving; two moments force sign changes; equality of minima on two supports forces all the moments of uf(u) to zero and then F=0 by Weierstrass. The short positivity invoked from Yoshida is also covered by the stronger certificate NUMERICS-46. The precise page of Yoshida has not been collated here. |
| 1361–1598, Onat, Al, Alband, Cheb, parityschur, polarcap, mult | a | Complete non-attainment; equivalence strict margin/flat certificate; unique increasing envelope; Stieltjes integral without boundary; inversion on the complement of the kernel and indispensable rank condition; polar capacity formula; coercivity on multipliers and compact separation of moment vectors. |
| 1930–2067, coer-decomp/K1/sector/K/tail/w/poinc | a | Dimension 2k−2, truncated exponentials in the log domain, factor 1 per pair of blocks, cancellation of the first exponential by Tate; double Poincaré by sine expansion and sum Σ1/[n²(n²−4)]<1/3. |
| 2068–2102, coer-A | a for the bound; b local 2094 | Paley–Wiener division by s²+a uses both Tate zeros, H² with vanishing traces; main inequality correct despite an inexact location of the maximum for small R (below). |
| 2112–2191, coer-lowpass/B | a | cosh/sinh interpolant matches value and derivative at the centre; L2 remainder≤cosh²(r)r⁴/6 by Cauchy–Schwarz; layer-cake integration with ε′≥0; θ*>r for 0<r≤1; primitive Φ verified by differentiation. |
| 2198–2370, coer-prime/L1/schur, inertiatower, firstcontact | a for structural inequalities | Fibres of the shift are paths of length ceil(2T/ell); Schur by Riesz on the coercive block; Rayleigh bounds respect the reversal of sign when λS<0; first contact by continuity and compactness. Rounded tabulated values are not independent certificates of this review. |
| 2371–2403, ladder | a | K(a,b) has pole 1/((a−1)b)+1/(a(b−1)) and factor (a+b−1) correct. C1 approximation in x=e^(−y), Fourier error O(ε/(1+|τ|)), moments and prime series dominated; matrices of all degrees sufficient. |
| 2405–2409, finite comparisons | c | The text itself says without proof; there is no certificate here for four arbitrary exponents nor thirteen poles with multiplicities. They are not used in ladder nor in the subsequent deduction. |
| 2411–2428, all-degree-gram | a conditional | The input dirichlet-input gives zeros on the line by means of the functional equation; only then does conjugation turn the product into a squared modulus. Paired Hadamard and convergence O(γ^-2) correct. Its condition is not proved by this proposition. |

Complementary primary source for Boas–Kac: [Ehm–Gneiting–Richards, 2004 article, institutional abstract](https://pure.psu.edu/en/publications/convolution-roots-of-radial-positive-definite-functions-with-comp/), confirms a complex L2 root with half support. The complex character is sufficient in prop:weak; a real root is not imposed without proof.

## First defective lines and repair

**277, (b) literal.** `2 Re(a conjugate(b′))` is not a Hermitian form in two vectors: it is neither sesquilinear nor does it satisfy Hermitian symmetry. On the vectors (1,0),(0,1) it gives 2 in one order and 0 in the reverse. The correct expression is `a conjugate(b′)+b conjugate(a′)`. Its diagonal is exactly 2Re(a conjugate(b)), which is the expression used in eq:W. It does not invalidate the quadratic forms or the subsequent real polarisations.

**2094, (b) literal.** The maximum over 0≤x≤R² is not at (2R²−a)/3 when R²<a/2. Permitted example: r=0.1,a=0.0025,R=0.01; the point is negative. The bound used remains true: y=x+a belongs to [0,R²+a], and y²(R²+a−y)≤4(R²+a)^3/27. Dividing by R² gives exactly M_R. This repair changes no constant and does not restrict R; the numerical application R=2 already satisfies the interior condition.

**1896–1899, precision and not a refutation.** With the true value of γ1, ε9=0.0156613114…<0.01567 is true. But the preceding assertion that only 14.13≤γ1≤14.14 is used is not enough for that decimal: γ1≥14.13 only gives ε9≤0.0157505828. One can use ε≤0.016 and keep 0.5−ε≥0.484, exactly the subsequent denominator. Hence cor:margin1 stands with constant 4·10^9 and exponent 15.449 using only the announced interval. The script Z1 also certifies the more precise value, if one wishes to keep 0.01567.

## Z1–Z3: margin, without presupposing RH

Z1 is certified independently by `evidence/verify_Z1_margin_46.py` and `Z1_margin_46_arb.json`: Arb at 256 bits encloses rho1=1/2+14.13472514173469…i and returns N(21)=1 exactly. The counting function counts ALL zeros with multiplicity; hence it is simple and there is no other zero with 0<Im≤21. Primary source: [Arb 2.23 documentation acb_dirichlet](https://arblib.org/acb_dirichlet.html), entries zeta_zero and zeta_nzeros. Simplicity is not inferred merely from an approximation to the root.

Z2 allows non-negative terms only up to H_PT; above that the text uses |β|<1/2 and absolute value with factor e^T. Z3 is used in integration by parts for Σp(H), p≥2; the factor 2 adds the two halves of the ordinates. The hypotheses of roughEF are satisfied: k≥5 produces a transform O(|τ|^(4−k)), integrable log weight, and the same bound Σp verifies absolute convergence of the sum over zeros. RH has not been used for the unverified tail.

In cor:margin1, k=ceil(21T/e), k≥8. For fixed k, ε decreases in T; at left endpoints T=(k−1)e/21, with C=eγ1/(21√2)>9/8, the derivative of the logarithm with respect to k is
`2 log(k/[C(k−1)])−1/(k−1)−2/(2k−1)<0` for k≥9.
The case k=8 and the endpoint k=9 suffice. The final constant using 0.484 is 3.9632451423·10^9<3.97·10^9. The high tail is smaller than 10^-70 of the first. The support, the cancellations of poles and of the first pair of zeros, the upper limit and the decrease of the margin were reconstructed; this does not prove positivity.

## Real pending items and scope

No structural analytic obligation remains open in the pure blocks read, except the two comparisons expressly without proof at 2405–2409. The illustrative roundings of thresholds and tables which are not the certificates requested remain without separate certification; the corresponding structural bounds are indeed reconstructed. The bibliographic exactness of some numberings of classical sources is not equivalent to a gap in the alternative proofs given above. The arithmetic chain that supplies dirichlet-input is judged in the other ledgers and retains its defect identified in P53: this review does not repair it.
