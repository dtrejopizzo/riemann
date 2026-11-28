# Mathematical review of papers 43 to 58

> **HISTORICAL RECORD OF THE FIRST PASS.** Its pending items and global verdicts do not represent the current state. The second audit resolved numerous points and proved a character failure in the proof of 53. Consult the [updated status](../deep-review/STATUS.md), [error 53](../deep-review/ERROR-53-CHARACTERS.md) and the certificates of 46 linked from README. The text below is kept for traceability; it must not be cited as the current final conclusion.


Papers 47 and 48 excluded. Consolidated report of verdicts, junctions and mathematical connections.


## Verdict of the mathematical review

Date: 28 November 2026. Local copy of the repository at commit `97fb4e78d5a858baa926829a42336ae3b914e59a`; individual hashes in `evidence/sources.json`. Papers 47 and 48 were excluded from the reading. The work was done on the LaTeX and the records indicated, not on a remote version that could change during the review.

**The review does not certify the proof of GRH/RH of the series. Nor did it produce a confirmed counterexample to its main theorems.** There are concrete arguments that were checked and central steps that remain **(c), not verified**, with their locators and the check needed to resolve them. Most of those steps have a written proof in the manuscript: the limit is that of this audit, not a claim that the author has omitted every proof.

The verdicts follow the requested scheme:

- **(a) correct as written**, within the scope that is specified. When an implication is verified from lemmas, it is stated expressly that not all of its antecedents were certified.
- **(b) incorrect**, with a proved first failure. No defensible (b) was obtained for the main theorems. Points of precision in data or formulation are identified separately.
- **(c) not verified**, indicating the exact step and what remains to be checked. It is not equivalent to "false", nor to "correct because no error was found".

### Central results

| Block | Result of this review |
|---|---|
| 46, equivalence between positivity in all windows and RH | **(a)**. The explicit formula, form domain and construction of the negative primitive test in 45 were checked. |
| 46, bounds up to `(log 5)/2` | **(c)**. The reduction to inertia can be checked; executable certificates and matrices are missing to validate the reported numbers. |
| 46, window `2.8022` | **(c)**. Z2 and the published bound Z3 were collated; the filter and the 17 verifications are not reproduced. Z1 was not independently certified. |
| 43 | **(c)** globally. Decomposition of the group, radial symbol and stabilisation checked; complete Hochschild computation, signature and completion not certified. |
| 44 | **(a)** for the two main composition/contact theorems examined, with their range; no automatic approval of all the secondary results. |
| 45 | **(a)** for comparison with the explicit formula, radial normalisation and primitive criterion. Those results have classical antecedents. |
| 50 | **(a)** for the algebraic theorem with its hypotheses and its internal inputs; **(c)** for certifying in full its application to all the later automorphic data. |
| 49 | **(c)** for global seesaw, exact constant in all the conjugates and complete divisibility. There are partial steps that were checked. |
| 51–52 | **(c)** for complete second moment, local estimates and multiplicities. Several constants, reductions and range closures were verified. |
| 53–54 | **(c)** for complete exchange, automorphic chain, one-lift formula and minimal-valuation test. Algebra of injectivity and of determinant compression checked. |
| 55 | **(c)** for complete global existence of twists, Ribet/Selmer and odd classes. The irreducibility is indeed made explicit; duality and sum of losses were checked in the reductions indicated. |
| 56 | **(c)** for the complete integral theorems. Substitutions and NM were verified in the application; NM is not a necessary condition for every vanishing, and the text does not formulate such an equivalence. |
| Junctions | Central entries of the table of 46 collated with explicit degrees of coverage; **(c)** for certifying all the transitive imports and their applications. |
| Novelty and connections | Antecedents and a proposed quantitative connection identified; neither global priority nor the birth of a new field is certified. |

### Observations that allow the manuscript to be improved

1. **Paper 46, line 1766:** `omega_-` must be at least `2A=5.88394705…` for the specified cut. `5.8839` may be a decimal summary, but not a literal upper bound. The certificate must keep exact values or directed roundings. The bounds for the two tails are numerically consistent; this does not certify the inertia.
2. **Paper 51, line 3961:** the absorption `f·2^(3−k)≤b^-10` needs a relation between k and `log b`, in addition to the bounds listed locally. The relation comes from the admissible data; it would be advisable to include it when isolating the lemma. No contradiction was found in the current application.
3. **Paper 50:** its conclusion is one of truncated colength, with exceptional term `θj`. Presenting it as a uniform bound on all the elementary divisors would lose an essential part of the statement.
4. **Paper 56:** "for every ℓ" does not remove the conditions on weights, windows and distribution of letters. NM is a sufficient condition of the generic argument, not a necessary characterisation of vanishing. The report offers an example of positive rank that distinguishes the two concepts.

Objections that would be unfair to this version were also discarded: the residual irreducibility of 55 is indeed written; 51 does treat the extension of the comparison to inert places and closes the range of coranks; the corrected constant `3x^35` of 54 does reach 46; and the difference between the lattices of 49 and 51 does have a proposed transport.

### Reading of the proposed connection

The idea that deserves to be isolated is to convert divisibility of theta coefficients into a one-sided bound on primes, by comparing the size of many forms with a lower limit for their covolume. The second moment guarantees almost full rank; the CM periods, the twists and the Selmer groups must make the two counts compatible.

The series acknowledges that the automorphic route and its mathematics are attributed to Levent Alpoge, while the organisation into three theorems and its presentation in this series are due to the author of the manuscripts. The names of specialists supplied by the author were used to define the tasks of the specialised reviews; none of those researchers took part in or endorsed this review.

A describable line of research would be **slope methods for automorphic lattices and theta divisibility**. It is a proposal for a programme, not a declaration of a new discipline. The chapter on connections gives concrete intermediate results that could be validated and developed without depending on RH.

### Method and material scope

The work consisted of a main review and three specialised reviews: theta/Hecke/covolume; second moment/trace and connections; Selmer/integral Hodge. There were cross re-readings of the positive verdicts and of the examples. The review does not reproduce an exhaustive line-by-line refereeing of all the manuscripts nor the complete formal Lean construction.

The inventory contains 14 sources, 1910 shared labels and 3526 explicit internal references with the keys recognised by the script. Those numbers include repetitions and volume 58; **they are not a number of verified theorems**. The tables of the chapters explain exactly what was collated. The references that are not individualised remain (c).

The certificates of the finite windows were not executed because they were not located in the artefacts examined. The review's own checks of constants use multiple precision without intervals and are identified as consistency, not as certification. The large-scale Lean archive was not recompiled. The papers and the untracked file `06-alpoge-verification/README-mio.md` remained intact.

### Priorities for closing the review

The global certification requires resolving several independent pieces of work, not only correcting the two editorial details: supplying the reproducible inertias of 46; completing the audit of periods and divisibility of 49; certifying the local systems and the uniform main term of 51–52; checking exchange and test forms of 53–54; closing Selmer and odd classes of 55; and verifying the central integral lemmas of 56. The chapters indicate their precise labels. Only afterwards can a complete semantic comparison of the junctions support a verdict on the whole chain.


## Paper 46 Weil form and numerical certificates

Review of the three points requested, on the local `main.tex` identified in `evidence/sources.json`. The line numbers correspond to that file, not to pages of the PDF. **(a)** means argument checked within the scope indicated; **(b)**, located failure; **(c)**, step not verified. A conclusion (c) does not assert that the statement is false.

| Point | Verdict | Reason |
|---|---|---|
| Positivity of `W_T` for every T equivalent to RH | **(a)** | Explicit formula, density in form norm and negative primitive test of paper 45. |
| Bounds `10^-18` and `2.5·10^-12` | **(c)** | Justifiable method of reduction; matrices and a certified run establishing their inertias are missing. |
| Facts Z1–Z3 | Z2 and the bound of Z3: **(a)**; certification of Z1: **(c)** | Z2 was collated with the primary source; the coefficients of Z3 coincide with the published formulation. The certification of the first zero and its isolation was not reproduced. |
| Bound up to `T=2.8022` and use of Z1–Z3 in it | **(c)** | The filter and its 17 verifications are reported, not developed or reproduced. |

### Equivalence with RH

The definitions are in paper 46, lines 248–316, and the proof of `thm:all-support` at 5460–5505. With the transform `Fhat(τ)=∫F(t)e^{iτt}dt`, the symbol is

`m(τ)=Re ψ(1/4+iτ/2)−log π`,

and each prime power carries `2Λ(n)/sqrt(n)` in the cosine symbol. The explicit formula for an autocorrelation gives

`W_T(F)=Σρ Φ_F(ρ) overline(Φ_F(1−barρ))`.

The polar term is `2Re(A overline B)`, not `|A|²+|B|²`. Under RH each summand is `|Φ_F(ρ)|²`. For smooth real tests the formula is at lines 260–271; the complexification is valid because the cross sum for two real tests is real on pairing conjugate zeros.

The extension to `D_T` does not require assuming a priori convergence of the sum for every rough test: the density in weighted norm of `lem:form-density` (457–487) and the positivity for differences make the transforms a Cauchy sequence in `ell²`. Convergence in `L²(-T,T)` identifies each coordinate. The argument of contraction of the support followed by mollification proves the density; the continuity of the moments and the logarithmic growth of `m` give continuity of the form.

For the converse I reviewed the concrete proof of paper 45, `thm:sufficiency`, lines 1403–1559. A zero off the line produces an orbit of four points `±z0,±bar z0`. A polynomial annihilates the other zeros of bounded height and the points `±i/2`; a convolution power of a bump controls the tail. The adjustment with `α+βz0²`, possible because `Im(z0²)≠0`, makes the orbit contribute `−4m0`. The tail is `O(4^-N)` with constants independent of N, since `Σ m(z)/(1+|z|)²<∞`. The tests constructed are real, primitive and compactly supported. A sufficiently large window contains the support and has negative form. The support depends on N: it is not claimed that a prefixed window detects all the zeros.

This equivalence does not prove that the form is positive. It is compatible with the later automorphic proof remaining unverified. The classical antecedent is [Connes–Consani, appendix C, with attribution to Yoshida](https://arxiv.org/html/2006.13771).

### Certificates in the window of log 5

The first step that I cannot certify is paper 46, lines **1616–1617**: the ball enclosures would give the four bounds and the programme is not reproduced. The text develops the reduction, but the table of pivots (1772–1783) is the result that has to be proved, not a substitute for the computational proof.

The proposition `prop:lowercert` (1695–1732) has a correct functional justification: on the complement of the first Legendre functions the operator is bounded below by `q_Y>0`; the Schur complement is dominated by the matrix `R`; the inertia of the border with `c=0` subtracts exactly one negative direction; with `c=−1/2` and `c=+1/2` one recovers, respectively, the even and odd polar terms. The estimates by means of the trace of the compression of the band-limiting operator are also sufficient as a method.

To complete the numerical verification the following are needed:

1. Exact values or intervals with directed rounding for `T`, `s_infty`, nodes, weights, entries and tail bounds.
2. Code of the quadrature and proof of the analytic bound for the remainder that it actually implements.
3. Certified matrices or a reproducible generator of them, with the four values of μ.
4. Verifications of `q_Y>0`, invertibility of the change of basis, sign of the border block and all the pivots of the Schur complement, including the contributions of the tails.

The notebook of paper 58 does not contain the identifying parameters of these certificates: `193.13`, `640` or `120110026807`. Its README declares expressly that it contains small consistency checks, not a proof of the theorems in their range. I did not run those checks as a substitute for the missing inertias.

The script `evidence/check_constants_46.py` reproduces **with multiple precision, without intervals**, these consistencies:

| Quantity | Approximate value |
|---|---|
| `240T` | `193.132549492092…` |
| `A` | `2.94197352522362…` |
| `m(240)−A` | `0.700787608327198…` |
| `Lambda*_280` | `4.4046093678·10^-20` |
| `Lambda*_330` | `3.8625471440·10^-70` |

The last two are consistent with the printed bounds `4.5·10^-20` and `3.9·10^-70`; they do not certify the matrices. There is a necessary editorial correction in the data of line 1766: if `omega_-` is employed as the upper bound defined at 1688, then `omega_-≥2A=5.88394705…`; **the decimal `5.8839` is not a valid upper bound**. As a rounded summary it is admissible; as a literal constant of the certificate it must be replaced by an upward bound. It is not inferred from this that the spectral bounds are false. Likewise `c_*=193.13` is only an abbreviated presentation of `240T`, not its exact value.

### Zeros and larger window

Z2 (1795–1796) uses a height smaller than that of [Platt–Trudgian, theorem 1](https://arxiv.org/pdf/2004.09765): `3·10^12 < 3 000 175 332 800`. This reduction of height is correct and does not assume global RH.

The coefficients and range of Z3 (1797–1798) were collated with Rosser's formulation as reproduced in the article of [Faber–Kadiri](https://www.cs.uleth.ca/~kadiri/articles/New-Bounds-for-Psi-Math-Comp-Faber-Sept2013.pdf). For `N(t)` defined with `γ≤t`, the non-strict version of the inequality is also obtained by taking right limits at the heights of zeros. The step `N(t)≤t log t/(2π)` for `t≥21` is correct: the printed lower difference is positive at 21 and increasing. The Stieltjes integration of `lem:zerosum` keeps the boundary term with the correct sign; discarding it increases the bound.

Z1 (1790–1794) asserts simplicity and non-existence of other zeros up to 21, as well as an interval for the first ordinate. It is consistent with the classical values, but I have not reconstructed the count and isolation from the original certificates: **(c)** for that independent verification. Evaluating `ζ(1/2+it)` numerically would not suffice to rule out omitted zeros off the line.

In `thm:margin` (1864–1890), Z1 eliminates the first pair, Z2 converts the contributions of intermediate height into squares and the count controls the rest by absolute value. It is an argument for an **upper bound** on the minimal form, not a lower bound. There is no valid deduction of positivity from that upper bound tending to zero, and the text does not make one there.

For the **lower** bound at 2.8022, the first pending step is **1915–1930**, `eq:power-window`: a compact filter, 2048 continuous Schur rows and 17 verifications are announced; their formulas and execution are missing. Z1–Z3 by themselves do not allow the exponent `120110026807` to be checked. The section declares that no other claim of the paper depends on this bound; its lack of certification does not by itself refute the automorphic chain.


## Review of 49, 50, 53 and 54: theta, Hecke and covolume

Date: 2026-11-28. Source: `main.tex` of the local copy, not papers 47–48. The line references are those of the source file. It does not represent the opinion of the researchers mentioned by the author.

### Scope and verdict

The review distinguishes the proof of a local result from the verification of all its automorphic antecedents. **I do not certify papers 49, 53 and 54 in full nor the GRH conclusion.** I have checked the algebraic structure of paper 50 and several concrete steps of the other three. For the statements whose complete development I have not been able to check I give (c), and I specify which part remains pending; this does not mean that the proof is false nor that the manuscript necessarily omits that part.

| Question | Verdict | Exact scope |
|---|---|---|
| 50.1: `ph:thm` in `ph:eq-large` | (a) | Algebraic theorem under its printed hypotheses of §2.1; the deduction and its inequalities are verified. The inputs are checked in 50.2; this does not certify the arithmetic applications of 50.3. |
| 50.2: `ph:root`, `ph:count`, `ph:av` | (a) | The arguments of §3 supply these inputs and the numerical hypotheses of their internal application hold. |
| 50.3: range used afterwards | (c) | The cited statement and the result obtained coincide; with the numerical substitutions verified, the whole arithmetic construction of the data and the weak approximation of 49 remain uncertified. |
| 49.1: seesaw independent of the twist | (c) | Not verified: the whole transfer of periods, convergence and descent of archimedean types. |
| 49.2: conjugates and exact CS constant | (c) | The arithmetic of area factors in (C4) checked, conditional on the classical formula cited; the whole reciprocity and normalisation of the vacuum not certified. |
| 49.3: divisibility at all primes | (c) | The specific treatment of inert primes, the ramified prime and level identified; not all the integrality arguments for the kernel verified. |
| 53–54.1: exchange and absolute constant | (c) | Not all the local and archimedean terms of `pcx:X` checked. |
| 53–54.2: injectivity and factorisation | (c) | The abstract injectivity of the triangle is indeed checked; not all the automorphic hypotheses that apply it. |
| 53–54.3: Gram and L-values of one lift | (c) | The identity of determinants verified conditionally on `po:glue`; its automorphic antecedents remain. |
| 53–54.4: test form and valuation attained | (c) | The ultrametric deduction of `psm:attained` from its inputs verified; not all the inputs nor the orthogonality to false lifts. |

I have not identified in this review a counterexample that would justify (b). I do not convert the lack of a complete audit into an accusation of absence of proof.

### 50: mathematical checks

File: `04-papers/50-elementary-divisors-edge-hecke-operator/main.tex`.

#### The statement actually proved

Lines 335–409, `ph:thm`. The ring is a valuation domain of characteristic zero, with (w^2=p), and the cycle has (N\ge2) even, (P=p^e\ge5), (q=P^N). The freeness condition on the edges `ph:eq-free` is required. The result controls the colength **truncated** by (p^j\Lambda):

\[
\operatorname{col}(\Lambda,Y\Lambda+p^j\Lambda)\mid p^l,
\quad l\le (3c_d+\theta j)|X||H||\mathcal B|.
\]

The paraphrase "small mean of elementary divisors" must keep the exceptional fraction (\theta) and the truncation. It is not a uniform bound independent of (j) for all the elementary divisors, nor does it by itself ensure that (Y) is invertible. This is a point of interpretation, not a failure of the printed theorem.

#### Algebra of the deduction

* `ph:near`, lines 449–481: the diagonal form can be obtained by finite operations in a valuation domain; a DVR is not required. The independence modulo the maximal ideal of the columns of (Q) and of the selected columns of (U) is proved by applying the left inverse (R). The module to which Nakayama is applied is finitely generated, even if the ring is not noetherian.
* `ph:fact`, lines 543–552: the transposition and the order are correct. The relation (\mathsf b\rho({}^tg)={}^t\rho(g)\mathsf b), together with the diagonal commutation of (\Delta) and (\mathsf b), produces exactly (A(1\otimes\mathsf b)).
* `ph:null`, lines 554–576: the jet argument uses CRT and the count of the reduced monomials. The condition on the number of points gives independence in addition to generation. If an infinite set (Z) is allowed in the statement, it suffices to take a finite subset of the required size.
* `ph:depth`, lines 578–629: the forms (z_v(y)^{P^j}) recover all the coordinates (y_{ac}). The determinants employed are non-zero because their terms are distinct monomials. The sum of weights of the monomials gives the bound (c_d|\mathcal B|).
* `ph:ends`, lines 631–651: the passage from the possibly non-discrete valuations to integer exponents is valid: one counts how many integers (\delta\ge0) satisfy (t_i\nmid w^\delta), that is, a rounding up. Discreteness of the valuation is not being assumed.

At lines 706–749 one obtains (A'={}^td'Zd). The congruence of the average gives (\mathcal A\mathcal B\equiv p^{2Nc_0}\pmod{w^c}), not (p^{Nc_0}): the second factor comes from (\mathsf b\mathsf b'=p^{Nc_0}). The text keeps both factors. Finally

\[
\det d'\det d\mid w^{\lambda+\lambda'}\mid p^{\max(\lambda,\lambda')},
\]

by (w^2=p), and this produces the final coefficient (3c_d). No factor 2 is missing in that last conversion.

#### The three inputs

**Root** (`pe:root`, lines 925–1025). The substitution constructs a polynomial (\bar\Phi) over (R/w^{\lambda+1}R) of degree (q\nu'), with non-zero leading coefficient. For each representative of (\mathbb F_q) it is divisible by a power ((t-a_r)^\nu). The differences (a_r-a_{r'}) are units; hence these factors are comaximal and their monic product divides (\bar\Phi). The degree argument remains valid even though the quotient ring has zero divisors, precisely because the divisor is monic. One concludes (\nu\le\nu'). There is no need to introduce a field hypothesis at this step.

**Count** (`pe:count`, lines 1230–1251). The delicate point is the volume of `pe:vol`, lines 1120–1171, which uses interlacing, the Jacobian (P^{kN}\Delta(\sigma)), and the Euler product. The factor obtained is

\[
\prod_{l=1}^k\frac{q-1}{q^l-1}=[G:I]^{-1}.
\]

The packing construction in `pe:flag` transforms the count of monomials of fixed degree into a volume of dimension (kN), using a thickness of size one; a set of volume zero is not being compared directly with its number of points. The hypothesis (24Nk^2cP^{2r}\le\theta n) implies (x\le\theta/2\le1/2), whence (e^x\le1+2x\le1+\theta).

**Averaging** (`pe:avg` and `pe:av`, lines 1259–1328 and 1430–1500). The average is constructed algebraically by means of traces, not by dividing by the order of a finite group that might be a non-unit. In (S1), the limit (d+k\le q) is sufficient: a homogeneous form of degree between 2 and (q) does not disappear on reducing modulo (X_v^q-X_v); the monomials of degree (q) that reduce to degree 1 do not cancel with terms of degree 1 of the same homogeneous form. The submodule (U^+) is finitely generated because the algebra (\mathcal S_d) is the image of a finite free module and there are finitely many initial vectors. Thus its use as a free module in the trace is legitimate over a valuation domain. The weight estimates in `pe:wd` keep the error (2c), sufficient for the threshold (c^*=3kc).

#### Internal range and application to 49

Lines 1505–1517 verify explicitly, from `ph:eq-large`, the conditions of `count`, `av` and `near`. In particular

\[
P^{N/2}=\sqrt q\ge n^2>Nk(N/2+2)n+n+k,
\quad 24Nk^2(5Nc_0)P^{2r}\le\theta n.
\]

The application of lines 1519–1531 uses (n=a=xb), (r=\lceil\log_pm\rceil), (P=p^{o_0}), (N=o/o_0), (\theta=(m^2f)^{-1}). Its two verifications are (q\ge a^4) and ((Nk\log q/\theta)^5P^{3r}\le b\le a). The conclusion (3c_d\le12A_{\mathfrak l}/(mp)) has the correct factor because (A_{\mathfrak l}=aN/2).

The arithmetic part of lines 767–831 uses, in addition, weak approximation, freeness of (J), the identification of all the factors of the representation and the parity of the places of the cycle. I have read that reduction and not found a contradiction; I have not certified here the antecedents of 49 that provide these data. For that reason the question about **all** the later applications keeps (c).

### 49: precise location of what is pending

File: `04-papers/49-short-forms-theorem-theta-lifts-complex-multiplication/main.tex`.

**Seesaw.** The result `au:seesaw` of 46 allows the chain datum (\Psi) to depend on the twist, but not (c_{\rm ss}). Nor does it assert non-vanishing of the two sides. In 49, `ps:onestep` (3983 ff.) reduces the transfer to a single orbit; stages (3), (5), (6) are referred expressly to `pk:vanish`, `pk:coarse`, `pk:fine`. It would not be legitimate to point to those referrals as gaps without checking their targets. What is missing in this review is to verify those targets, the absolute convergence on exchanging integrals and sums, and the assembly that keeps the scalar independent of the twist.

**CS constant.** In `ps:conj` (3845), the requirement is exactly (|t_\sigma|^2=\Omega^{-1}). `pk:conj` (5433) uses (t_\sigma=\sigma(\varpi_{\rm vac}/\mathsf u)c_\psi/\Omega_\sigma). The proof of (C4), lines 5304–5340, does not confine itself to citing an equality "up to an algebraic number": it constructs (\mathsf u^{12h}=\prod_i\mu_i^{12}\Delta(\Lambda_i)) and asserts the exact identity of areas. I checked the combination of factors shown: from (\operatorname{area}|\Delta|^{1/6}=4\pi^2\operatorname{Im}\tau|\eta|^4) and from the average (c_{CS}-\log(2\sqrt d)) there results (2\pi^2e^{c_{CS}}/\sqrt d), as written. I did not check the starting formula against the full text of Chowla–Selberg, nor all the transports of differentials, the unit at 2 (`pf:CS`, 6911), and the reciprocity `pf:recip` (7111). For that reason I do not certify the final exact constant.

**Divisibility.** `pa:count` (2522) expressly distinguishes the ramified prime (p=d), with additional deduction (\frac12\sum_\tau\mathrm{ded}_0(\tau)), and limits the jets to the nested Schur columns. The substitution by new directions of 2557 ff. gives the factor (\varpi^B\prod\det(g_{\tau,h})^{\kappa_\tau(h)}); the three classes of congruences (a)–(c) cover the pairs of heights (h=1), (h\ge2,h'=1), (h,h'\ge2). This combinatorial control does not by itself prove that the real kernel has the required normal form. There remain to be verified `pa:kernel`, the treatment of 2 and of the primes of the level, and `pl:level`. The level (N) is treated separately in `pa:level` (3169): it must not be confused with an application of the Hecke theorem of 50.

### 53–54: what is checked and what is not

**Exchange.** In 53 `pcx:X`, lines 1772–1795, one requires (a=b+2e\), (q=q_V+q_{V'}\), (2q+2\le N\), (N\le2\mu_\tau+2q\), non-trivial modulus and character with non-trivial tame part at each chosen prime. The scalar has (|c|^2=C L_*(\mathfrak m,\nu,e)); it cannot be replaced by a universal constant independent of the character. The independence asserted corresponds to (C) and to the vector (x). The transposition of splitting indices in `pcx:eq-dict` (1809 ff.) is indeed exact from the two printed definitions. I have not audited the whole computation of (C), nor the complete proof of `pcx:X`; the classical Rallis formula does not replace that verification.

**Injectivity.** `pc:tri-inj` (53, 557–580) is a correct argument of linear algebra, with the hypotheses (T1)–(T3) of `pc:triangle`. It does not divide by (\sigma_{i,n}) to prove injectivity, so it does not incur circularity when deducing afterwards that those scalars are non-zero. What is pending is the automorphic realisation `pc:tri` (1248) and the first lift: it is not enough to verify the abstract triangle to certify `au:inj` or `au:factor` of 46.

**One lift.** In 54, `po:ss-proof` (1134–1164), (\Delta_j) is the determinant of the comparison operator **compressed** to the space of lifts. The identity

\[
\det(\Theta^*\Theta)\det(\operatorname{pr}_{\mathrm{im}\Theta}U|_{\mathrm{im}\Theta})
=\det(\Theta^*U\Theta)
\]

is correct for an injective (\Theta): it is obtained by writing (\Theta=QR), with (Q) isometric and (R) invertible. It does not require (U) to preserve the image. The equations of `po:glue` and `po:exchange` then give the power (H_j(\vartheta)^{d_j}) used by 46. I have not checked all the inputs of `po:glue`, including the generating products, the false forms and the three exchanges. Global verdict (c).

**Valuation attained.** `psm:attained` (54, 8249–8296) constructs (t=M^{12f}c_{{\rm vac},y}\prod B(l_\tau)^2). The choice of a coefficient of minimal valuation in a combination with integral coefficients is valid and goes in the correct direction. The use of the ultrametric inequality does not allow equality of an individual valuation to be inferred: it gives exactly the one-sided inequality declared. The twelve-factor theorem `psm:twelve` and all the inputs of the construction of the coefficients remain pending. `psu:small` (9118) uses in addition integrality and orthogonality of the test form; I have not certified the latter.

**Archimedean bound.** `psu:arch` (9217) cancels (a_\sigma(z)B(z)) between a principal pair and a flat one of equal rank. The cancellation works if (CL), stated immediately before, has the same (a_\sigma(z)) for both pairs. The final proof of the inequality is correct conditionally on (CL), on the norm formula and on the size bounds; I have not verified the whole of theorem 9.1 of 53 which establishes (CL). The factorial factor of `psu:normL` must be kept: the highest-weight vector has norm 1 and the Fock monomial has squared norm (\prod l_\tau!).

### Junctions reviewed

| Junction | Result of the comparison |
|---|---|
| 50 `ph:thm` → appendix of 49, lines 8639–8655 | Same range, same (c_d), same term (\theta j) and same three inputs. |
| 50, lines 844–847 → 49 `pa:eldiv`, lines 3156–3164 | Same (12A_{\mathfrak l}/(mp)+j_0/(m^2f)), same (j_0\ge0), same truncated colength. |
| 54 `psu:small` → 54 `po:small` | (fmb/k+3x^{35}) is preserved; the initial statement already incorporates the corrected constant. |
| 54 `po:small` → 46 `au:hecke`, lines 4992 ff. | 46 expressly mentions the constant (3x^{35}), not the earlier version. |
| 54 `po:ss-proof` → 46 `au:onelift`, lines 4965–4980 | The compression, power (d_j), denominators and the possibility of absorbing a twist-independent factor into (C_j) coincide. |
| 53 exchange → alternative convention of 54/55 | The declared dictionary is an interchange of indices, without factor; not all the later concrete substitutions were verified. |
| 53 triangle → 46 `au:factor` | Depends in addition on the equality of multiplicities of 51; not certified by this report. |

This table **is not an exhaustive audit of every citation** in the four manuscripts. The junctions not listed, including the whole dependence on 55 for regular families, remain (c).

### Literature and novelty

The Chowla–Selberg identity is earlier: [Chowla–Selberg, *On Epstein’s Zeta-function* (1967)](https://doi.org/10.1515/crll.1967.227.86). The general theory of regularised Siegel–Weil and Rallis is also earlier: [Gan–Qiu–Takeda, arXiv:1207.4709](https://arxiv.org/abs/1207.4709). These located sources corroborate antecedents and do not certify the particular normalisations of these manuscripts.

The most sharply delimited candidate for an autonomous contribution in the block reviewed is the theorem of 50: an integral average compatible with a Frobenius cycle and a count of defects which control colengths of edge operators. The connection proposed in 49 and 54 between exact CM periods, integral jets at all primes and determinant bounds is a concrete research architecture. Its bibliographic novelty and its global validity are not established by this review. There is no basis here for asserting that a new field has already been created or that this architecture proves RH.

### Requested matrix of the inputs of 46

**Concordance of the statement** is deliberately separated from **validity of the proof**. "Coincides" means that the conditions indicated are preserved on comparing the passages pointed to; it is not equivalent to certifying all the antecedents. For `inj`, `factor`, `hecke` no integral literal comparison of all the appendices was carried out.

| Input of 46 | Concordance examined | Proof and range |
|---|---|---|
| `au:seesaw` (4314) | 49 §5.1.7 develops the result; the datum may depend on (\vartheta), the scalar may not; the absence of any assertion of non-vanishing is preserved. | (c): transfer of the orbit, exchanges and complete assembly pending. |
| `au:divis` (4368) | Coincides with 49, appendix 8533–8555: exception (N), ramified moduli, (\ell\nmid\mathrm NQ), (2mfb), (j_\ell=\lceil2mfa/\ell\rceil); it is not asserted that (Y_{\mathfrak l}) preserves the ramified subspace. | (c): the algebraic component of 50 is reviewed; the normal form of the kernels, the level and the assembly of all the classes of primes are not. |
| `au:count` (3900) | Coincides with `pa:count` and `pa:schur`: minors of the first (h) columns or Schur entries, (B\ge1), heights (<n'), loss (fn'^3(1+\log_pB)), and extra term (e=0) for (p=d). | (c): coverage of the congruences of directions reviewed; not the whole proof of normal form and standard monomial theory. |
| `au:kernel` (4497) | Coincides with 49 appendix 8570: (0\le j<m), every conjugate, (\exp(x^{50}+\mathrm{rs}_j/2)). | (c): depends on reciprocity, exact CS constant and explicit comparison of (C_0\) with the data. |
| `au:restrict` (4516) | Coincides with 49 appendix 8580: squared norm, loss (x^{70}), gain (-\sum n_\tau\log N). | (c) for the complete result; checked the step of 49, 3830–3841, **given** integral branching: (|\sigma\bar\pi_N|^2=N) and (c_{\rm br}^2\le L^{6L}\le e^{x^{70}}). The construction of branching remains to be certified. |
| `au:expansion` (4532) | Coincides with 49 appendix 8587: finite support, integrality only outside (N\mathrm NQ), and bound (e^{x^{60}}) only for trivial twist. | (c): the elimination of the gluing and the count of coefficients were not reviewed in full. |
| `au:equiv` (4584) | Coincides with 49 appendix 8604: tame character, (\beta_\vartheta(u)\in K^\circ), action by right translation. Dependence on (\vartheta) is allowed. | (c): integrality of each local component of (\beta_\vartheta(u)) and compatibility with the gluing remain to be certified. |
| `au:shortbasis` (4427) | Coincides with 49 appendix 8558 and proof 3587–3622: (c_0) positive integer in the different, bound (6c_0(fn)^2). | (a), checked: elementary transference with dimension (2fn), dual of ((2/c_0)L) contained in (L), and selection of (n) (E)-independent vectors. The result asks for a basis over (E), not an integral basis of the module (L). |
| `au:inj` (4794) | 53 identifies the deduction with `pc:tri-inj` and the automorphic triangle. A literal comparison of all the antecedents was not certified. | (c) globally; (a) the abstract argument `pc:tri-inj`, keeping (T1)–(T3). |
| `au:factor` (4850) | 46 preserves (m)-fold twists, exponents (\vartheta^j), power (-\dim\mathcal T) of the factor of ratios and Gram quotients. A complete collation of the construction of each ratio with 53 is missing. | (c): requires automorphic triangle, adjoint law and equality of multiplicities (M+), in addition to injectivity. |
| `au:aux` (4878) | Coincides with 53 appendix 16275: (\gamma(1)=1), non-vanishing, (m)-fold twists, integrality outside (Q), squared norm (e^{2x_1^2b^2}). | (c): `pc:auxcore` (1616) explicitly provides the intermediate bound (e^{2x^{201}b^2}) and generators (e^{x^{99}b^2}); not all the twists of the second lattice of lifts were certified. |
| `au:onelift` (4965) | Concordance checked with 54 §2.6: compressed operator, (Delta_j\ne0), power (d_j), constant independent of the twist; see the detail above. | (c) globally; identity of determinants correct given `po:glue` and `po:exchange`. |
| `au:hecke` (4991) | 46 preserves the regular-family hypothesis and cites the corrected constant (3x^{35}) of 54. Not all the ratios of its product were collated in full. | (c): CL of 53, sharpness inputs, orthogonality of test forms and regularity conditions imported from 55 are missing. |

The additional check of `au:shortbasis` uses the following. If (\lambda_1(\Lambda^*)\ge\rho), Minkowski gives a primitive vector of (\Lambda) of length (\le m/\rho); projecting orthogonally to that vector and proceeding by induction gives covering radius (\le m^2/\rho). The vectors of length (\le3m^2/\rho) span the real space. For the hermitian lattice (L=E^n\cap g\widehat{\mathcal O}_E^n), unimodular, a non-zero vector has squared norm at least (f), by total positivity and integrality of (h(y,y)). Since (c_0\) belongs to the different, the Euclidean dual of ((2/c_0)L) is contained in (L). Taking (m=2fn), (\rho=1) and multiplying by (c_0/2) gives exactly (6c_0(fn)^2). No ineffective constant intervenes.

### Second critical review of the scope of (a) in 50

There are no hypotheses literally called (H1)–(Hn) in this version of the file. So that the verdict does not hide context, this is the reconstructed list of assumptions. The three inputs do not replace the structural conditions on the operator.

| Hypothesis | Source | How it enters or is checked |
|---|---|---|
| Valuation domain of characteristic 0, (p\) non-unit, (w^2=p) | 335–337 | Allows finite diagonalisation, cancellation, Kummer and reduction modulo powers of (w). Neither DVR nor noetherianity is assumed. |
| (W) local, residue field (\mathbb F_q) | 337 | Gives classes with unit differences and surjective reduction of (GL_k(W)). |
| (N\ge2) even, (e\ge1), (P=p^e\ge5), (q=P^N), cyclic homomorphisms (\iota_s) with congruence modulo (p) | 337–348 | It is a structural hypothesis, not a conclusion of root/count/av. It implies (\iota_s(\mathfrak m_W)\subseteq p\mathcal O), with the argument of the unit factor (1-y^{q-1}). |
| (k\ge2), (n\ge1), (0<2r\le k), (r) integer, alternating standard/dual representations | 350–358 | Used in depth, interlacing, count and parabolic block. |
| (X,H) finite, edge maps, representatives (t(\varkappa)^{-1}K_r=\varkappa), (u(e)\in GL_H(\mathcal O)) | 374–380 | Necessary to have two restrictions and to use (u(e)^{-1}) in the almost-inverse. The cases of empty sets have empty/trivial conclusion. |
| Freeness `ph:eq-free` | 381–383 | Makes the parametrisation of inverted edges bijective. It is not deduced from the three inputs; it is verified separately in the automorphic application, 823–831. |
| (f\) linear, (Yf=fA), (\Lambda=f(\mathcal F_X)) | 401–403 | Allows the colength of the abstract operator to be transferred to the image module, which does not have to be free. |
| (0<\theta\le1), (n^4\le q), ((Nk\log q/\theta)^5P^{3r}\le n) | 397–400 | Implies all the additional numerical inequalities for the three inputs, as is checked at 1505–1517. |
| `ph:root`, `ph:count`, `ph:av` and the inclusion `ph:AinC` | 661–703 | The three propositions are proved in §3; `ph:AinC` is also proved, at 1027–1051, using root. It is not a fourth external input without proof. |

I have checked again the places that usually introduce hidden hypotheses: the degree over the ring with nilpotents in root (the divisor is monic), the finite generation of (U^+) in the average (it comes from the finite algebra (\mathcal S_d), not from noetherianity), Nakayama in `ph:near` (finitely generated module), and the count of roundings of valuations in `ph:ends`. I have not obtained a concrete correction to (a) for the algebraic formulation in this context. The result applied to all the global data of 49 remains (c); the three inputs do not by themselves prove the freeness of edges, the weak approximation or the arithmetic normalisation.


## Mathematical review of papers 51 and 52

Date: 28 November 2026. Sources examined: the local `main.tex` of 51 and 52, the corresponding statements and applications of 46 and the map 57. The line numbers refer to those sources, not to the PDFs. Neither 47 nor 48 was read.

**Global verdict: (c), not verified.** The complete proof of the second moment and of its three local inputs has not been certified. Important reductions, algebraic constants and several junction points were indeed checked. No counterexample was found that would allow the main theorem to be classified as (b). The partial verifications that follow must not be raised to an approval of the approximately 17,000 lines of the two files.

The authorities named by the author did not take part in this review. This is a review devoted to automorphic analysis and trace formulas.

### Verdicts by question

| Question | Verdict | Step that remains uncertified |
|---|---|---|
| Second moment `au:moment`, uniform in rank and with exact constant | **(c)** | Complete construction and estimates of the coefficients/Bessel, especially `pbe:ds`, `pbp:main`, and the local inputs `pbm:inputs`; see P51:2331, 6801, 3890 and P52:926, 4192, 4223. |
| Main term by Siegel and Poisson with all its constants | **(c)** for the complete result; several reductions **(a)** indicated below | The Siegel inequality for the squares of orbital sums, `pff:S`, is not certified merely by verifying the formula for representation of numbers or the formal cancellation of constants. |
| Remaining terms and exhaustiveness of the count | **(c)** for the geometric bounds; **(a)** for the closure of the range, conditional on the stated pillars | `pbg:main`, `pbc:C1`, `pbc:C2`, `pbs:S`, `pbo:O1` remain to be certified in full. There is no evident omitted range of corank greater than `n^3`: the text contains an explicit reduction. |
| Equality of multiplicities and attribution | **(c)** for the complete proof; scope and attribution made precise below | The bounds for the kernel and the archimedean orbital identity `pbr:main` remain to be verified in full. The assertion used has cuspidal projection and specific parameters; it is not a general invariance of the whole spectrum. |

In this table, "remains to be certified" identifies the scope of the review. It does not assert that those steps lack a proof in the manuscript: their proofs are written and require an additional audit.

### Second moment and the constant of the main term

P46:4692–4706, `au:moment`, asks for

\[
\sum_{s\in\overline G}\|P^*\varrho(s)P\|_{HS}^2
\le (1+9b^{-4})\frac{D_X^2}{\deg\,\operatorname{mass}_r}.
\]

P51:180–195 reproduces the same three statements; `pb:thmB`, P51:1112–1128, deduces them from `pb:est` and the comparison of multiplicities. The norm is Hilbert–Schmidt. It must not be confused with the operator norm, for which the passage to spanning would have another content.

The need for a main constant close to one is real. If the images of an isometric map are distributed in a subspace of dimension `d/C`, a second moment with constant `C` can still be compatible with that concentration. For that reason a bound with an arbitrary absolute constant does not replace the one written.

**Check (a), conditional reduction of L2.** At P51:3994–4026, if one accepts (R), (F), (S), the sieve theorem and the bounds (C0), (C1), the final factors are

\[
(1+b^{-6})\left[(1+b^{-9})^2(1+b^{-6})+b^{-10}\right]
\le 1+b^{-4}.
\]

This holds for `b≥1000`; the terms other than one are of order `b^{-6}`, much smaller than `b^{-4}`. The factor `b^{-6k#A}` is recovered from the error term using `#A≤f`. There is no hidden loss of an absolute factor in this last deduction.

**Check (a), cancellations of C0.** At P51:3925–3963, `pbm:const`, taking `n=ρ+1`, `r=k+2ρ+1`, `v=(2/rd_E)^f`, the identities of exponents

\[
\tfrac12-k-n-2\rho(\rho+k)
=\rho-(2\rho+1)(k+\rho+\tfrac12),
\]

\[
k+n+2\rho(\rho+k)
=1+(2\rho+1)k+\rho(2\rho+1).
\]

are verified. They are precisely the exponents of `rd_E` and `2`. The identity of compact volumes used there is obtained directly from `vol U(j)=∏_{a=1}^j 2π^a/(a−1)!`. With the masses and the covolume indicated accepted, there remains the scalar inequality

\[
\mathsf L\le(1+b^{-9})(1-N^{-k})^f.
\]

It is incorrect to describe the main term as an exact equality without correction: the text keeps `L` and `(1−N^{-k})^{-f}`, and absorbs their deviation into the explicit margin.

**Inherited size hypothesis that should be made explicit.** The last estimate of (C0), P51:3961, uses `f·2^{3−k}≤b^{−10}`. It is not deduced from the inequalities listed in the heading of `pbm:const` by themselves: with `k,n,f` fixed, increasing `b` preserves their upper bounds and makes that inequality fail. In the admissible data the additional information `k≥x⁵/2` and `x≥(log b)¹⁰⁰` is indeed available, and it guarantees it. A sufficient local condition is `k≥20 log b+4`, together with `f≤b/1000`. This does not refute the application to the data of the paper, but the assertion of sufficiency of an isolated list of parameters must incorporate that condition or cite the inherited bounds explicitly. The algebraic cancellations verified above do not depend on this observation; the numerical closure of C0 does.

The exact ratio of masses is at P51:1336–1357, `pb:massratio`. It is compatible with the factor `2^{1-lf}` of Gan–Hanke–Yu for the unimodular genus in the unramified case: the global factor 2 cancels in the ratio, but `2^{-f}` does not. See propositions 4.4–4.5 of [Gan, Hanke and Yu, *On an exact mass formula of Shimura*](https://web.math.princeton.edu/~jonhanke/Web-02/Mass-Formula-of-Shimura/shimura-mass.pdf). This check does not replace the audit of each identification of lattices that allows that formula to be applied.

### Poisson, Siegel and the local inputs

**(a), one-sided Poisson lemma `pbm:poisson`, P51:3661–3684.** In the adelic group used, the periodisation of a non-negative integrable function has Fourier coefficients `c_L^{-1} F̂(η)`. If the absolute sum of those coefficients is infinite the bound is trivial. If it is finite, it represents a continuous function, equal almost everywhere to the periodisation and bounded by that sum. Lower semicontinuity on the finite set of points allows zero to be approached through points of almost-everywhere equality. This proves the inequality with the factor `1/c_L` as written. It does not require pointwise equality of a classical Poisson formula for an arbitrary function.

**Checks of Siegel normalisation.** P52:5442–5460 correctly obtains the products of additive measures of covolume one:

\[
\operatorname{covol}(\mathcal O_E\subset\mathbb C^f)
=2^{-f}|D_E|^{1/2},\qquad
\operatorname{vol}(\widehat{\mathcal O}_E)=2^f|D_E|^{-1/2}.
\]

It also uses `|D_E|=|D_{E^+}|²` when `E/E^+` is unramified at the finite places. P52:5504–5513 correctly computes the archimedean density

\[
\int_{\mathbb C^k}\delta(|x|^2-a)\,dx
=\frac{\pi^k a^{k-1}}{(k-1)!},\quad a>0.
\]

It is deduced by differentiating the volume of the ball of radius `√a`; no additional factor 2 appears.

The Siegel–Weil theorem that the manuscript invokes is expressed with a measure **of mass one** on the compact unitary quotient, P52:5426–5440. It would not be correct to insert without compensation a Tamagawa measure of mass 2. The original cited is [Weil, *Sur la formule de Siegel dans la théorie des groupes classiques*](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5988-11511_2006_Article_BF02391774.pdf). This review did not certify the whole translation of its theorem 5 into the Weil representation and the characters of the manuscript; that point remains (c).

**Concrete limit of the review:** even accepting that translation and the two measures above, the passage from the formula of representations to `pff:S`, with separation of fibres, weights and pairs of terms, remains to be proved. That work is at P52:4279–4556. The computation of the density does not by itself prove the second-moment inequality. The bounds for the real and finite systems depend on the lemmas of descent, depth, frequencies and sum of layers, P52:708–871 and their later proofs; they have not been certified in full.

### The range of the count of pairs

An objection that is **not** justified by the version examined is to assert that the author only counts `l≤n³` and forgets all the other coranks. The closure of the range is written in `pbe:rank(c)`, P51:2941–2955:

\[
1\le\mathsf d,\qquad
\mathsf d^2\le(2/M)^{2if}b^{2n^3f},\qquad M/2\ge b^{18}
\ \Longrightarrow\ 18i\le n^3.
\]

Since `l≤i+1`, it follows that `l≤n³` in the range of the manuscript. This deduction is **(a) conditional** on the gain (G), on the limit of the gauge and on the integrality that gives `d≥1`.

The passage from (C1) and (C2) to (C), P51:6632–6659, is also correct as a reduction. Two terms are sent to the same pair `(t,L_{γγ′})`; the square of the bound for one term gives `b^{4000n^6(l+1)f}`, which is at most `b^{kf/4}` because `l+1≤2n³` and `k≥512000n⁹`. The weighted sum over the lattices then applies (C2).

The points still open in this review are the proof of (G) by means of cuts and indices (`pbg:main`, P51:8176), the count of frames of (C1) (`pbc:C1`, P51:8468) and the height and sum of sublattices of (C2) (`pbc:C2`, P51:8769). The coverage of non-near pairs and of non-concordant blocks uses in addition the truncation and the vanishing of amplitudes; that whole argument has not been certified. Hence it is not appropriate to assert that the complete count is correct, but neither is it appropriate to point to an omitted range without first refuting those reductions.

### Multiplicities and attribution

`pm:main`, P51:4299, is a comparison with:

- a comparison datum of hermitian spaces and identified levels;
- discrete-series parameters with separation at least `500n³+10n⁵` between coordinates of different signs;
- even real degree `f`;
- a supercuspidal test component at a split finite place.

`pm:mult`, P51:4331–4343, is then applied to the idempotent `e_0`; an irreducible label at one place provides the cuspidal component by Green's property (G). The equality is for the multiplicities of characters of the specified Hecke algebra, in the projected spaces, with fixed archimedean types. The sentence without these conditions, "groups isometric at all finite places have the same multiplicities", is too broad.

The comparison of stable classes `pm:classes`, P51:4729–4777, explains why the parity appears: the product of the signs that one wishes to change is `(-1)^{f(q−q′)}`. The argument uses global norms and the hermitian local-global principle; it is not obtained from a mere identification of the finite adelic points. The sum of orbital integrals at P51:4819–4836 employs in addition `pm:arch(b)`. The complete proof of the latter is referred to `pbr:main`, P51:5122 and following; it was not certified in this review. The global bounds that justify the trace of the kernel without truncation also remain pending.

The broad attribution to Labesse is reasonable as an antecedent of comparison and stability. It was **not** verified that the exact proposition of P51 is a literal citation of a theorem of his, and the manuscript should not present it so. [Labesse, *Changement de base CM et séries discrètes*](https://webusers.imj-prg.fr/~michael.harris/CBCM.pdf), introduction and theorems 5.4–5.5, imposes hypotheses of non-ramification at inert places for his results on multiplicity one and stability. P51 announces, by contrast, a specific proof by direct comparison and also cites the simple formula of Flicker–Kazhdan. Those distinctions must not be eliminated.

### Junctions checked

| Junction | Result of the comparison |
|---|---|
| P51 `pb:thmB` → P46 `au:moment` | Same three limits, same factors `5b^{-4}` and `1+9b^{-4}`, and same normalisation of `D_X²/(deg mass_r)`. Checked as a statement. |
| P52 `pfr:R` → P51 `pbm:inputs(R)` | Mass `(1+b^{-10})/deg_τ`, weights and decay coincide. The identification of the upper form with the Gram form, necessary for Siegel, appears in P52 (R-b) and at P51:3898–3900. |
| Real hypotheses of P52 → use in P51 | P52 requires `ρ≥10⁸`, in addition to other bounds (H0)–(H5). P51:4033–4038 and P52:958–964 expressly mention that condition and its satisfaction by the data. `n≥100` is not enough, but the use is not limited to that condition. The complete verification of (H1)–(H5) remains (c). |
| P52 `pff:F` → P51 `pbm:inputs(F)` | Mass `(1+b^{-6})b^{-6k#A}`, weights, exponent and denominator coincide. The system depends on the intermediate group `Z(A,d)`, not only on `T`. |
| P52 `pff:S` → P51 `pbm:inputs(S)` | The factors `r_*²`, `(1+b^{-6})a_*`, the set of distinct values of `t` and the condition of using the same finite form of (F) coincide. `T` must also contain the non-unitary places of the base; this is written in both. |
| P51 `pm:mult` → P46 `au:mult` | P46 asks in addition for the complete spherical algebra, not only the split places. P51:5021–5030, `pm:rem-full`, expressly extends the identity to inert places; for that reason there is no discrepancy of scope in this version. |
| Lattice of P51 → lattice of P49/P46 | They are not identical. P51:1027–1110, `pb:lattice`, offers a transport by an adele of norm one and unitary conjugation of the Poincaré maps. The invariance of the Hilbert–Schmidt norms under that transport is indeed checked; the complete identification of the original data of P49 is left to the audit of that paper. |
| P51 → P53 | The comparison of multiplicities is a relevant input for the chain. This review did not certify all the applications in P53 nor all the reproductions in its appendices. Status (c), with no concrete discrepancy proved here. |

The reciprocity of citations 51↔52 does not by itself prove circularity: the text separates the identities of coordinates and measures, used by 52, from the L2 estimate that returns to 51. To certify absence of cycles one has to follow the proofs of those base lemmas; the design of dependencies was checked, not its whole transitive expansion.

### Work needed to change the verdicts

To pass from (c) to (a) three independent and reproducible verifications are needed: one of `pbe:ds` and of the stationary period `pbp:main`; another of the local systems (R), (F), (S), especially of the separation of fibres and of all the uniform estimates; and another of the trace kernel and the orbital integrals of `pbr:main`. For the count, it is advisable to issue separate certificates for (G), (C1) and (C2) with the parameter inequalities included. The reductions already checked indicate which constants must be preserved and avoid repeating objections that the current version does treat.


## Specialised verdict: papers 55 and 56

Date of review: 28 November 2026. Texts: `04-papers/55-covolume-theorem-regular-families-of-twists/main.tex` (8200 lines) and `04-papers/56-explicit-cup-exponents-local-galois-representations/main.tex` (8380 lines), local working copy. The line references refer to those files, abbreviated P55 and P56. Neither 47 nor 48 was read.

**Global result: (c), not verified in its entirety.** This review does not establish a counterexample to the main theorems of these two papers. Nor does it certify their complete proofs. It does check several reductions, discards an overly general objection about irreducibility and delimits the results that would remain to be verified independently. A reduction that is correct assuming its lemmas does not constitute a verdict (a) on the final theorem.

Two senses of "missing" are distinguished below: an argument absent from the manuscript and a check that this audit has not yet completed. In the (c) points that follow, the manuscript normally **does contain** proofs of the lemmas indicated; what is pending is to validate them, not their mere existence. This verdict is not attributed to any of the mathematicians mentioned by the author.

### Answers to the questions on P55

| Question | Verdict | Concrete pending step or result checked |
|---|---|---|
| Existence for every prime, `pg:I`, `pg:II`, `pg:III` | **(c)** | `pg:I` depends on the transfer and on the local check in `pga:G123`/`pga:G45`; `pg:II` on the descent `pse:step` and on the polynomials of L-values `pse:stick`; `pg:III` on the trace modules and the realisation by auxiliary operators. A check of all those proofs and of all the external theorems with their hypotheses has not been completed. |
| Passage Selmer → congruences modulo powers of ℓ | **(c)** for the complete argument; **(a)** for the observation that the required irreducibility is explicit | `pri:ribet(1)` requires the image of the block to generate the whole matrix algebra. This hypothesis does not have to be added as if it were omitted. The whole construction of the determinants of linked rows and its automorphic realisation remain to be certified. |
| Local loss `pg:loss` | **(c)** | The reduction by duality can be checked; the numerical exponent depends on P56, `pki:crys`, and on the tame case. |
| Odd classes `pg:odd` | **(c)** | Neither the annihilator `pod:annih` nor the Euler descent that transforms annihilation into length with the declared constant has been certified. |
| Sum over all the primes | **(a) as an arithmetic reduction conditional on the declared bounds**; **(c)** as an unconditional consequence of the series | The sum of the local term and the change of units from valuation to logarithm are well posed and are checked below. The bound for `C_odd` and the local bounds are not certified by that sum. |

#### 1. The residual irreducibility is not a tacit hypothesis

P55, definition `pg:def-summand`, lines 563–585, requires in (M4) that for every sufficiently defined stable lattice the `u(g)` generate `M_n(O)`. The text explains its interpretation at lines 586–589. The exact version `pri:ribet`, lines 2565–2588, requires it again in (1), for the block `rho_pi`.

The lemma `pg:burnside`, lines 805–830, gives a pertinent and correct argument under its hypotheses:

1. The eigenvalues of inertia are distinct modulo the maximal ideal; the differences are units and the spectral projectors are integral.
2. The lattice decomposes into its eigenlines.
3. Frobenius permutes those lines in a complete cycle.
4. A subspace stable after any residual extension is a sum of eigenlines and stable under that cycle: it is zero or everything.
5. Burnside over the residue field and Nakayama over `O` give the integral generation of the matrix algebra.
6. `phi^n` preserves each line and commutes with the cycle, so it is scalar.

This check does not use that ℓ is large: it uses that ℓ is different from the residue characteristic of the auxiliary place and that the eigenvalues are incongruent. The strategy of two level primes, so as to be able to choose the other one when ℓ coincides with one of them, appears expressly in `pg:rem-primes`, lines 475–487. It remains to certify that **all** the automorphic systems that are used have the necessary labels and local types: that refers to `pga:G123`, `pga:G45` and to the selection of labels. It is not correct to replace that task by the assertion "Ribet needs irreducibility and here it is not assumed".

#### 2. What was checked of the twists argument

The lemmas on roots of unity `pg:roots1` and `pg:roots`, lines 922–990, have a coherent mechanism: the evaluation valuation is compared with the Gauss valuation; the contribution of roots of the polynomial on circles of radius `rho_h` is counted; the average truncated by 1 produces a point with no loss greater than `delta`; the variables are specialised successively. In the reduction of powers `1≤j≤m`, choosing the root of greatest valuation of `(1+Y)^j-(1+x)` guarantees `v(Y)≥v(x)/j`, and does not presuppose `j` prime to ℓ. This aspect does cover small primes.

The lemma `pg:minor`, lines 1068–1100, explains why the maximal minors control the length of a kernel modulo `ℓ^M`. The formula `sum min(M,v(d_i))` and the passage to the group with coefficients `K/O` when the length is less than `M` are correct. The rest of the existence of the useful specialisation depends on the descent of Selmer groups: `pse:mirror` (1780–1840), `pse:step` (1872 and following), and on `pse:stick` (2051 and following). **That dependence has not been verified in full.** In particular, it is not enough to verify the specialisation of polynomials to conclude the Selmer bound: first one has to prove that there exists a point where the minors possess the required valuation.

#### 3. Local loss: reduction checked, exponent pending

P55 `pll:D2`, lines 3314–3358, does not confine itself to citing an integral form of Bloch–Kato: it writes a proof by lengths. Its steps are appropriate:

- The image of `H_f^1(T)` in `H^1(T/ℓ^m)` is `H_f^1(T)/ℓ^m`, because the preimage of a rational subspace is saturated.
- Its length is `m(h_f-h_0)+len H^0(T/ℓ^m)`.
- The tangent dimensions of a de Rham representation and of its Tate dual add up to `[F:Q_ℓ] rank(T)`.
- The local Euler characteristic and Tate duality give that the two orthogonal images have complementary lengths.

This supports `pll:dual` (3360–3394), without by itself converting a rational Bloch–Kato bound into the new integral bound of the paper.

The mechanism of `pll:ribet`, lines 3408–3446, is also checked. One takes `Y=⊕End(u_x)` with **multiplication on the left**, not with the action by conjugation. For that reason `Y` is a sum of copies of the original representations. The submodule generated by `(u_x(g)-1)_x` is stable, and the relations allow the morphism to `T/ℓ^M` to be defined. The rational exactness of `D_cris` on the representations that become crystalline over a common extension shows that the cocycle in that submodule is crystalline. The choice of the left action is essential and is made correctly.

What is not certified is the new bound of `pll:exponent`, lines 3487–3507, taken from P56. The final classification of `pg:loss` remains (c).

#### 4. Odd classes and ℓ=2

`pg:odd` (1373–1380), `pri:odd` (2313–2327) and `pod:odd` (4382–4404) have the same structure: for `e≠0` it is a matter of cocycles anti-invariant under complex conjugation with cyclotomic local condition, and for `e=0` of homomorphisms unramified everywhere. The second formulation makes explicit `chi^e = Z_ℓ(-e)` and that the coefficient ring contains the values of the Dirichlet characters.

The manuscript does not apply without explanation a result on Euler systems valid only for odd ℓ. `pod:rem-two`, lines 4406–4416, separates the primes `ℓ≤(N+t+3)^2`, using annihilators and detector points, from the larger ones, where it applies the descent. This answers the objection of formal coverage of ℓ=2, but does not prove the result: `pod:annih` (4879 and following), `pod:detect` (4511 and following), and the descent of the later sections must be verified. In this review those three steps are not certified. There is no counterexample established here.

#### 5. The sum of losses, with all the units

P55 defines, lines 416–433,

`lambda_ℓ = v_ℓ((2b)! · (∏_{b-30h³<n≤b+30h³} n)^{h³})`,

`loc_ℓ = 4f·10^6 (m/k) (b v_ℓ(M)+lambda_ℓ)`.

For any finite set of primes `T`, the product formula applied to **a fixed positive integer** gives

`Σ_T lambda_ℓ log ℓ ≤ log((2b)!) + 60 h^6 log(b+30h³) ≤ 3b log b`,

with the size separations of the data. Likewise `Σ_T b v_ℓ(M)log ℓ ≤ b log M ≤22b log b`. Hence the factor `4·10^6·(3+22)=10^8` of `pg:sums` (520–522) is correct.

The contribution `2^{-ℓ}` is summable, and the terms that are valuations of `N_ch`, `C_odd` and `h_1` are summed as logarithms of those integers. At the end, the absorption of the local term into the budget reduces to

`2·10^8 m² ≤ x (log b)²`,

which is obtained from `m²≤4x` and `(log b)²≥8·10^8` (P55, 525–533). The individual uniform bound must not be summed without keeping the finite support or the factorial structure: that structure is precisely what allows the sum.

This computation is a verification of the **arithmetic reduction**, not of the prior existence of the integer `C_odd` with the required size.

### Answers to the questions on P56

| Question | Verdict | Scope |
|---|---|---|
| Main exponent without FL restriction, for every ℓ | **(c)** | The numerical deduction of `pki:crys` from its central propositions has been reviewed; not all the lemmas on lattices, frames and walks on which they depend are certified. |
| NM: necessary and sufficient | **(a)** for the identification of its role as a sufficient hypothesis in the reduction and for its arithmetic verification in the application; **(c)** for the complete generic proposition | The paper does not assert an "if and only if". NM is not necessary for the defect to vanish; an example is given below. |
| Tame potentially crystalline case | **(c)** | The passage of the exponents and the specialisation to the data fit; the certification of the tame killer `pkw:T3` and its inputs is pending. |
| Novelty | **(c)** | The fine form of the bound is a candidate for a contribution; neither priority nor validity is established by a limited bibliographic comparison. |
| Consistency with FL | **Compatible in the subcases checked; (c) as a complete comparison of categories and local conditions** | The vanishing when `lambda=0` agrees with what is expected; P55 itself does not use FL as a substitute for its integral proof. |

#### 6. The main assertion is more restricted than the abbreviated title

`pki:crys` (552–623) does not say that any pair of crystalline representations of arbitrary weights has the announced exponent. It requires (S1)–(S4), opposite windows, that the letters read thickness, and few low jumps or the alternative case `U'⊆[-eta,0]`. In particular, "every ℓ" does not remove the geometric hypotheses on the distribution of weights and embeddings.

The deduction distinguishes:

- `ℓ≤Q`: `pki:sparse` is used with `J=floor(log_ℓ h³)`, low radius `2G`, `vartheta=2K`, `M=K`.
- `ℓ>Q`, `lambda≥h³`: `pki:any` is used, and one obtains `b+delta<Kℓ²` and `2(G+delta)<Kℓ`.
- `ℓ>Q`, `lambda<h³`: `pki:generic` is used with `a=2(lambda+1)`.

In the last case the result is directly a **length of defect**, not necessarily an exponent that kills each class with that same constant divided by the rank. P55 expressly keeps this distinction in `pll:exponent`. The illicit interchange "length by rank → uniform exponent" was not found here.

The complete check must still cover `pkf:main` (2868), the deepening theorems `pke:I2` (4829), `pkh:I4` (5793) and the scheme `pkd:scheme` (6882), with their dependencies. They are written proofs, but this audit has not certified each one. In particular, checking the inequalities 570–623 without checking those results does not verify the theorem.

#### 7. NM: what it means and where it is used

The definition of NM in P56, 380–382, excludes **non-zero** multiples of ℓ in three intervals around `0`, `b_z` and `-b_z`, of radius `n`. The lemma `pkc:free`, 6310–6321, uses exactly that exclusion so that the costs of the steps of level zero are zero in an unramified chart. The conventional value of the cost function at `y=0` is zero; it is not being asserted that the ordinary valuation of 0 is zero.

In the application `lambda<h³`, lines 600–607:

1. If ℓ divided an integer in `(b-30h³,b+30h³]`, the power `h³` of that factor would force `lambda≥h³`.
2. With `a=2(lambda+1)` one has `n=6(a+eta+W)<13h³`.
3. Every non-zero multiple of ℓ has absolute value at least `ℓ>198G`, so it lies outside the low interval and outside the intervals around `±(G+delta)`.
4. The intervals around `±(b+delta)` lie inside the enlarged factorial interval above, because `delta+n<30h³`.

Thus NM is checked in **both** classes of letters, thick and thin; it is not presupposed without control for `G`.

NM is not necessary for the conclusion of zero defect. An example of positive rank: `F=Q_23`, `U=U'={0}`, `L=Z_23` trivial, `a=2`, `eta=1`, `W=0`, `b_z=20` in all the letters. Here `e=f=1`, `ℓ≥5`, `eta≥1`, the two windows contain 0 and there are no jumps in `[-a,0)=[-2,0)`. One has `b+W+eta=21≤(23-3)·2=40` and `6(a+eta+W)=18<20`. NM fails because `y=23` is non-zero, divisible by 23 and at distance 3 from 20. Thus all the other hypotheses of `pki:generic(i)` are satisfied. The crystalline representations with all their weights zero are unramified, and so are their lattices. For any equivariant pairing modulo `23^m` between those lattices and `L`, let us choose an element of inertia `g` whose cyclotomic character takes the value `-1` modulo 23. Equivariance gives `(epsilon(g)-1)b_psi(y,l)=0`; the factor is a unit, so the pairing to `Z/23^m(1)` is zero. Consequently the defect here is zero, even though NM fails. This example refutes **the interpretation of NM as a necessary condition**, not the one-sided statement of `pki:generic`.

#### 8. Tame case and Tate dual

P56 `pki:tame` (464–474) and its repetition `pkc:tame` (6629–6638) impose `F=Q_ℓ`, `e_0=lcm_{1≤i≤r}(ℓ^i-1)`, uniform polynomials `K(s)` and the membership of the dual in the class with `K^{-1}(s)=K(s^{-1})`. The inequality `ℓ>b+6(W+eta)+r²(N+1)²+2` is part of the hypothesis.

The deduction of 6643–6681 keeps the costs: `e_0≤ℓ^{r²}`, a polynomial of degree `≤N²` for the dual tensor, `kappa=r²(N+1)²`, and a total walk cost bounded by `3kappa+150(eta+W+1)`. The choice of `K^{-1}` is important: applying the same polynomial directly to the dual without inverting inertia would be incorrect. The text does make the inversion.

The application to P55, `pkd:data(iv)`, 7224–7281, uses `N=(r+t)r=6r²`, `eta=h²+1`, `W=4t`, `delta_j=j Delta+h-2t` and `p_i≥b^{10}`. The bound required is smaller than `2b`, so the separation `p_i≥b^{10}` gives the range. `L_c^*∈C(U',K^{-1})` is also made explicit; no omission of this hypothesis has been found in the junction.

The uncertified part is the proof of `pkw:T3`, lines 7753 and following, which obtains the integral annihilation of the cokernel from inertia and from the monic polynomial, together with the preparation of the tame charts. The arithmetic of the exponent, even if conditionally correct, does not replace that proof.

### Junctions: identity of the input versus proof of the input

| Junction | Identity/range checked | Validity of the input |
|---|---|---|
| P46 `au:regular` → P55 `pg:main` + `pg:sums` | Yes, in the reduction of P55 535–545. R1 comes from (a); R2 uses the inverse quotient and `|·|_iota=ℓ^{-v}`; R3 uses `beta(ℓ)=(beta_ℓ+v_ℓ(h_1))log ℓ`. `log ℓ` is not omitted. | (c), because of the dependencies of `pg:main` and `pg:odd`. |
| P46 R3(i),(ii) → P55 `pg:def-den`, `pg:main(c),(d)` | The false lifts are defined place by place and orthogonality is required for all those places. The contribution `h_1` is added to the bound for principal pairs. P46 4895–4912 and P55 394–411, 438–458, 460–473. | Coherent reduction; the whole construction of the operator remains to be certified. |
| P55 `pg:loss` → `pll:main` → `pll:exponent` | The first bound is by dual defect of `L_c^*`, not of `L_c`; the factor `[E_v:Q_ℓ]` and `x_main=1`, `x_e=t` are present. | (c), exponent coming from P56. |
| P55 `pll:exponent(a–d)` → P56 proof after `pki:crys` | The exponents `10^4 floor(2lambda/Q)(floor(log_ℓ h³)+1)`, `10^4 floor(2lambda/Q)m`, the tame case and the reservation of length without exponent coincide. P55 3487–3507; P56 624–636. | (c) for the central theorems. |
| P55 (M2) → P56 `pkd:data(i–iii)` | Correct algebraic check: the dual has jumps `-u-1`; `delta_j=jDelta+h-2t`, width `4t`, radius `h²+1` contain the jumps and the bound for low multiplicity is preserved. | Conditional on the representations of P55 actually satisfying (M2). |
| P55 tame types → P56 `pkd:data(iv)` → `pki:tame` | `N=6r²`, the uniform polynomials and the inversion `K^{-1}` coincide. The range in `p_i` suffices. | (c), tame killer and automorphic origin of types pending. |
| P56 generic → application of `pki:crys(d)` | NM is derived from `lambda<h³`, with independent control of the letters of weight G. | (a) for the verification of hypotheses and the inequalities; (c) for the whole proof of `pki:generic`. |
| P55 → P54, input (IM) for L-values | P55 explicitly points to P54 §3.1, and `pse:stick` is the point that uses it. This review does not certify (IM) nor its normalisation; it belongs to the specialised audit of P54. | (c). |

The dependence P55↔P56 **does not by itself show a logical circularity**: P56 imports definitions, the elementary bound rank→defect and properties of representations from P55; it returns the local exponent. To denounce a cycle one has to exhibit that one of those inputs of P55 depends on the exponent, not only that the two papers cite each other.

### Novelty and limited bibliographic comparison

The candidate contribution of P56 is the sensitivity of an **integral bound for the defect of compatibility modulo ℓ^m** to the distribution of weights and to the scarcity of thick letters, instead of only to the largest weight. P55 explains why it matters to it: it wants a saving proportional to `m/k` after summing over places and primes. That connection with a global budget of denominators is an identifiable idea, although its complete mathematical validity remains pending.

It is not new, by itself, to study crystalline lattices outside the Fontaine–Laffaille range nor torsion representations for ℓ=2. Pertinent primary sources:

- Fontaine–Laffaille, *Construction de représentations p-adiques* (1982), [original text](https://www.numdam.org/item/10.24033/asens.1437.pdf).
- Tong Liu, *Torsion p-adic Galois representations and a conjecture of Fontaine* (2007), [publication](https://www.numdam.org/item/?id=ASENS_2007_4_40_4_633_0).
- Tong Liu, *A note on lattices in semi-stable representations*, [preprint](https://arxiv.org/abs/0709.4523).
- Caruso–Liu, *Some bounds for ramification of p^n-torsion semi-stable representations*, [preprint](https://arxiv.org/abs/0805.4227), [authors' text](https://www.math.purdue.edu/~tongliu/pub/bound2.pdf).
- *Torsion representations arising from (phi, G-hat)-modules*, [preprint](https://arxiv.org/abs/1202.1858), whose scope includes p=2.

Those references do not automatically verify the exponent of this manuscript. Nor does the absence of an identical bound in a limited search prove priority. The exact comparison requires identifying torsion categories, maps and local conditions, and then deriving or excluding an equivalent bound. P55 `pll:FL`, 3467–3479, acknowledges that it does not use the Fontaine–Laffaille path as a substitute. In the range where `lambda=0`, the conclusion of vanishing agrees with the expectation of integral exactness, without that certifying the cases of large weights.

### Scope of the Lean records

Only the README of `06-alpoge-verification` was inspected. It contains declarations of compilation and of axioms, and expressly distinguishes compilation from mathematical review. The compilation was not repeated, the whole Lean archive was not inspected, and no declaration-by-declaration correspondence with P55/P56 was established. Hence that README is not used to change any of the (c) above to (a).

### Priority checks for closing this verdict

1. Certify `pkw:T3`, `pke:I2`, `pkh:I4` and `pkd:scheme`, including integrality, constants and compatibility of the lattices defined by orders.
2. Certify the automorphic transfer and the local types of `pga:G123`/`pga:G45`, checking the exact hypotheses of the results cited.
3. Certify `pse:step` and the input of P54 in `pse:stick`, not only the lemma of specialisation at roots of unity.
4. Certify `pod:annih`, the number of detector points and the Euler descent with its dependence on ℓ=2.
5. Only after those verifications, raise the correct final bookkeeping of losses to a verdict on the existence of regular families for all the admissible data.


## Junctions between the papers

The table of inputs at the end of the automorphic section of paper 46 (5055–5095) is covered by the matrix below and the specific checks linked. **The whole network of transitive imports is not certified.** The concordance of the imported statement is distinguished from the proof of the statement and from the fulfilment of its hypotheses in each application. A mutual citation does not prove circularity; textual coincidence does not prove its absence either.

### Inputs listed by paper 46

| Input | Origin | Concordance checked | Verdict of global validity |
|---|---|---|---|
| `au:seesaw` | 49 | The scalar is independent of the twist; the chain datum may depend on it. | (c), the whole transfer and integration remain to be certified. |
| `au:divis` | 49, 50 | Level exception, truncation and loss of colength are maintained; invariance of the ramified subspace under each Hecke operator is not asserted. | (c); algebraic argument of 50 reviewed separately. |
| `au:count` | 49 | The nested columns and the additional deduction at the ramified prime are preserved. | (c), normal form of the kernel and assembly. |
| `au:kernel` | 49 | Every conjugate and the exponential bound with `rs_j/2`. | (c), exact CM normalisation and reciprocity. |
| `au:restrict` | 49 | Squared norm, loss `x^70` and level term. | (c), integral branching pending. |
| `au:expansion` | 49 | Integrality outside the level and conductor; size bound for trivial twist. | (c), gluing and count. |
| `au:equiv` | 49 | Tame character and right translation preserved. | (c), local integrality of the translation. |
| `au:shortbasis` | 49 | Basis over E, not necessarily an integral basis; constant `6c_0(fn)^2`. | (a) for the geometry-of-numbers lemma under its hypotheses. |
| `au:moment` | 51, 52 | Three bounds and constant `1+9b^-4` coincide. | (c), complete local estimates and uniformity pending. |
| `au:mult` | 51 | The assumptions of separation and projection are present; `pm:rem-full` covers inert places. | (c), orbital identity and global justification of the trace. |
| `au:inj` | 53, 54 | Triangle and first lift identified; no integral literal comparison of all its inputs was made. | (c), automorphic realisation; abstract triangle correct. |
| `au:factor` | 53, 54, 51 | m-fold twists and powers are preserved; depends on the same comparison of multiplicities. | (c), exchange, factors and all the substitutions. |
| `au:aux` | 53 | Origin identified in `pc:twistreduct`; integral comparison of hypotheses pending. | (c). |
| `au:regular` | 55, 56, 54 | R1–R3, factors `log ℓ`, denominators and false lifts collated. | (c), Selmer, integral exponents and odd classes. |
| `au:onelift` | 54, 53 | Compressed determinant, power `d_j` and twist-independent factors coincide. | (c), `po:glue` and its antecedents. |
| `au:hecke` | 54, 53 | `3x^35` already propagated, not the old version; rest of the applications of CL pending. | (c), integral test and comparison of norms. |

The details and locators are in [theta and Hecke](../02-theta-hecke-covolume.md), [spanning](../03-spanning.md) and [Selmer and Hodge](../04-selmer-hodge.md).

### Junctions that require special care

**Range from 50 to 49.** The equality of the cited statement includes the exceptional fraction and the term `θj`. A truncated colength cannot be replaced by a uniform bound on all the elementary divisors. The numerical substitutions were verified; the arithmetic realisation of all the data remains (c).

**Lattices of 49 and 51.** They are not literally the same lattice. The manuscript acknowledges this and provides adelic transport and unitary conjugation (`pb:lattice` of 51, 1027–1110; `au:two-lattices` of 46). The invariance of Hilbert–Schmidt norms under that transport is correct. Checking it does not by itself certify all the data of the original construction of 49.

**52 to 51.** The range includes `ρ≥10^8` and conditions H0–H5. The weaker condition `n≥100` would not be sufficient, but the current version mentions and verifies the larger size in the data. (R), (F), (S) use the same measures, masses and weights; the complete audit of H1–H5 and of their proofs remains (c).

**56 to 55.** The text carefully distinguishes annihilating exponent from length of the defect: in a generic case only the latter is obtained. The duals, changes of weights and inversion `K(s^-1)` of tame types are present. NM is verified from `λ<h^3` in the application examined. The loss of hypotheses that reading only the title "without Fontaine–Laffaille restriction" would suggest was not found.

**43–45 to 46.** The explicit formula and the primitive criterion do coincide, according to [the review of the Weil framework](../07-rows-a-b-c.md). Those inputs are used to interpret the form and the converse of the criterion; they do not contribute the positivity that the automorphic chain aims to prove.

### Reproducible inventory and limits

`evidence/audit_sources.py` generates:

- `sources.json`: SHA-256 hashes, paths and number of lines of the fourteen sources 43–46, 49–58, with 47–48 excluded.
- `shared_statements.json`: text and locator of environments with shared labels.
- `textual_junctions.tsv`: equality after removing labels and normalising spaces.
- `internal_citations.tsv`: explicit bibliographic references with keys P43–P56 or Paper43–Paper56, with 47–48 excluded. It does not detect keys with alternative names such as `Companion`.

The coincidence of labels is only a navigation aid: generic labels can name different results. The macros can also change meaning between files. For that reason a `True` in the TSV **is not a verdict (a)**, and a `False` is not a mathematical failure. The differences of the main automorphic inputs between 46 and 58 were inspected: those observed are substitutions of external citations by internal references, not proved changes of constant or range.

**Status of all the junctions not individualised in the tables:** (c), not verified. What is pending is to compare the complete statement, its transitive definitions and the verification of hypotheses at the place of application. The inventory does not replace that work. I do not claim to have reviewed semantically each of the thousands of references in these manuscripts.

To close the network a note per import is needed, with origin, target, correspondence of symbols, measures, lattices, range and proof of the hypotheses of application. The notes above cover the central inputs that 46 lists; they are not enough to certify the GRH conclusion.


## Mathematical connections and research programme

The central pattern proposed by the series is to convert **divisibility of theta coefficients into a one-sided inequality on primes**, by comparing short forms, spanning of almost all of a space, and a lower limit for its covolume. It is a concrete connection and one capable of producing independent problems. In this review it was not proved that this connection closes the proof of GRH, nor that it constitutes a new field by itself.

The difficulty of RH does not logically force its solution to invent a new branch. A new and valid combination of known tools could also solve it. The productive question is what exact bridge the work contributes, which of its pieces are proved, and which results survive if the conclusion about RH is withdrawn.

Internal sources: P57 `main.tex`, particularly lines 100–120, 485–640 and 833–843; collation with the statements of P46 and the specific review of P51/52. The references to "the proposal" describe the argument of the manuscript, not a theorem certified by this report.

### The proposed mechanism

The first conceptual chain is

\[
\text{Frobenius on CM and local divisibility}
\longrightarrow\text{integral and small theta coefficients}
\longrightarrow\text{lattices of automorphic forms}.
\]

The second chain attempts to compare those lattices in two ways:

\[
\begin{array}{c}
\text{seesaw and bounds for all the conjugates}\to\text{upper bound for volumes},\\
\text{L-values, congruences, twists and product formula}\to\text{lower bound}.
\end{array}
\]

The second moment of the Poincaré map must guarantee that the first way reaches a proportion `1−O(b^{-2})` of the dimension. The comparison cancels a common main quantity `H_main`. The remaining imbalance is identified with `R_{d,q}(x)`; a one-sided analytic criterion aims to convert its bound into absence of zeros.

The potentially distinctive point is, therefore, **to make the local arithmetic of theta coincide quantitatively with an error in the distribution of primes**, after cancelling large main terms in determinants. Listing many specialities does not establish that bridge: it is established by the identities, the independence with respect to the twist, the uniform ranks and the final errors.

P57:100–112 says expressly that rows A–C do not enter that deduction and that no Hodge index theorem for those objects is constructed there. For that reason it is not appropriate to present the mechanism as a geometric proof of the sign of the adelic intersection. It is an automorphic and arithmetic route to the sign, reinterpreted afterwards in the Weil framework.

### Which connections already exist

| Connection | Antecedent | What the series would have to add |
|---|---|---|
| Adelic spaces, explicit formula and zeros | [Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*](https://arxiv.org/abs/math/9811068) interprets explicit formulas by means of a noncommutative trace. | Precise additional objects or properties; the association "adeles + trace + RH" is not new. |
| CM theta, algebraic coefficients and Hecke L-values | [Bannai–Kobayashi, *Algebraic theta functions and p-adic interpolation of Eisenstein-Kronecker numbers*](https://arxiv.org/abs/math/0610163) constructs and studies that bridge. | Simultaneous divisibility, non-ordinary cases, exact constants and uniformity required by 49/54; it is not enough to cite the existence of the classical bridge. |
| Masses of hermitian lattices and L-values | [Gan–Hanke–Yu, *On an exact mass formula of Shimura*](https://web.math.princeton.edu/~jonhanke/Web-02/Mass-Formula-of-Shimura/shimura-mass.pdf) gives exact formulas with local factors. | The combination with the moments, the growth of rank and a complete count of measures. |
| Archimedean growth, finite information and arithmetic slopes | The slope method has systematic antecedents; see [Bost, *Evaluation maps, slopes, and algebraicity criteria*](https://ems.press/books/standalone/21/408). | The concrete realisation by means of Poincaré maps and theta chains, with the error on primes as residual quantity. The similarity with slopes is conceptual, not a checked application of a theorem of Bost. |
| Automorphic comparison between unitary forms | [Labesse, *Changement de base CM et séries discrètes*](https://webusers.imj-prg.fr/~michael.harris/CBCM.pdf) develops base change, stability and multiplicity under precise conditions. | The exact comparison for the chosen spaces and projectors, or a valid independent proof. |

The bibliographic search carried out identifies antecedents, but it is not an exhaustive priority search. "I did not find an identical result" does not certify novelty.

### What would be a specific contribution if validated

1. **A uniform second-moment theorem with main constant one.** P51 requires simultaneous growth of the rank, weight, field and level. If it is proved with all those parameters and with an error tending to zero, it would be a concrete result that can be studied without mentioning RH. The review of P51/52 validates some reductions, not the complete theorem.
2. **A multivariable divisibility law with Frobenius action on the CM places.** The distinctive content would be the exact formula for the exponents and its control at each prime, not only the existence of divisibility of theta coefficients.
3. **A covolume principle with a choice of twist depending on each prime.** It must explain why several integral realisations control one and the same global object, how their losses add up and why incompatible lattices are not mixed.
4. **A proved cancellation between those two laws that leaves a recognisable sum over primes.** This is the most important connection for the RH objective. A formal identity between symbols does not prove it: it requires that both sides measure the same forms, the same lattices, the same norms and the same range of parameters.
5. **An integral local treatment outside the Fontaine–Laffaille range.** If the exponents of cup products of P56 are correct in all the generality claimed, it would be an independent contribution. Its validity is decided in the review of P56; it cannot be inferred from the formal success of the chain.

These points are candidates for new results, not results that this report declares established.

### An abstract principle that can indeed be isolated

There is an elementary piece that makes the error budget visible. Let `V` be a hermitian space of dimension `d`. Suppose that `s` linearly independent vectors are constructed, with `s≥(1−ε)d`, whose squared norm is at most

\[
\exp(H-mR+E_S).
\]

By Hadamard, the logarithm `c` of their Gram determinant satisfies

\[
c\le s(H-mR+E_S).
\]

Suppose also a lower bound, for that same family and its same integral data,

\[
c+2\delta\ge d(H-E_C).
\]

Then, by exact substitution and rearrangement,

\[
s mR\le (s-d)H+sE_S+dE_C+2\delta.
\]

This is a checked algebraic implication. It is a conditional model; it does not certify that the automorphic hypotheses of the manuscript hold. It shows three aspects that any development must preserve:

- `ε` must be small relative to the magnitude of `H`; omitting `(s−d)H` is illegitimate, in particular if `H` can be negative.
- The index `δ` is a quantitative loss and does not disappear by calling the forms "integral" after a normalisation.
- A constant in the norm for each lift, dimension or place can become a large term after taking logarithms and determinants.

The language of "semistability" must be used with precision. The bound of the manuscript for families of almost full rank does not automatically prove a slope inequality for **all** subspaces and sublattices. To obtain a complete theory of slopes those additional properties have to be formulated and proved.

### Programme that allows progress even if the proof of RH remains open

| Project | Concrete result to be required | Test of success |
|---|---|---|
| CM model of small dimension | Divisibility formula for one theta and one inert prime, with period and lattice fixed | Exact examples and a local proof that includes all the denominators; separate ordinary and supersingular primes. |
| A single theta exchange | Seesaw identity with explicit measures and computed constant | Check in a non-zero case that both sides and their changes under twist coincide. |
| A single determinant | Relation between a Gram and L-values, with saturation indices | Verify both the complex equality and the valuation at each exceptional prime. |
| Second moment in fixed rank | Estimate with exact main term for a family of levels or weights | Compare the constant of mass, formal degree and covolume before pursuing total uniformity. |
| Passage to growing rank | Theorem with explicit error functions in all the parameters | A book of inequalities showing that the final margin remains positive in the required range. |
| Local-to-global twists | Abstract theorem converting a family of local conditions into a bound for a global index | Finiteness, compatibility of the lattices and summability of losses proved, without assuming a non-existent common basis. |
| Modular formalisation | Lemmas on norms, Gram, local products and parameter domains | Each final result carries an inventory of axioms and of analytic inputs; compiling a conditional implication is not equivalent to proving its hypotheses. |

A useful presentation of that programme would be "slope methods for automorphic lattices and theta divisibility". It is a **proposed description of a line of work**, not the name of a new recognised discipline nor a claim of priority. Its value would be measured by reproducible independent theorems, examples and additional applications.

### Attribution and boundary of what is proved

P57:833–843 attributes to Levent Alpoge the mathematics organised by the three theorems and the path to the zero-free half-plane; it attributes to the series its organisation, names and writing into papers. This report preserves that attribution as the author himself declares it. It does not verify here the external authorship nor the claim, also present in that passage, that a complete formal proof of GRH exists.

Therefore, the series' own contribution that can be described without exceeding the evidence is the **expository architecture and the attempt to make a Weil framework compatible with that automorphic route**. The priority of each additional construction and the mathematical validity of the final bridge require the particular reviews. A promising connection can guide research even when one of the theorems it intended to use turns out to be incorrect; to develop that connection it is advisable to reformulate the failed theorem explicitly, keep the valid pieces and measure what weaker conclusion they allow.


## Papers 43 44 and 45 Weil framework

The radial identification of row C with the explicit formula has the correct signs and normalisation. The family of measures of row B satisfies its main laws of composition and contact. **Paper 43 is not verified in full**, in particular its topological computation of Hochschild complexes. These conclusions do not validate the automorphic deduction of RH: paper 46 itself excludes 43–45 from that deduction.

### Paper 43

There is no single main theorem: the introduction contains `introA`, `introH`, `introB`, `introC` and `introD`, in addition to results on completion and determinant. The global verdict requested is **(c)**, not verified in full.

| Assertion | Verdict and scope |
|---|---|
| Decomposition `A_S^×=Γ_S×ker φ`, identification of `C_S` and homomorphic section | **(a)**, `thm:split`, line 777; normalising each finite valuation produces a unique representative, and the section preserves products. |
| Convolution of smeared objects | **(a)** for the formal identity given the definition; it does not prove a geometric theory of intersections over Spec Z. |
| Hochschild computation `thm:shadow`, line 2800 | **(c)**: it remains to verify completely the continuous comparison of the crossed product with the Koszul complex (`prop:crossed`), the local contractions and their compatibility with the completed tensor products. |
| Formula for the symbol in the radial component | **(a)**: the finite geometric integrals and the digamma identity give the symbol used in 45. |
| Formula for all the components, non-degeneracy, signature and completion | **(c)** as a whole: the audit of the ramified characters, the dual density arguments and all the topological assertions of completion has not been completed. |
| Stabilisation on increasing S | **(a)**: `thm:chartcomp` and `thm:colimtrace`, 5242–5335, for the system of projections defined in the text. |
| Limits of rulings, determinant and Riemann–Roch pairing | **(c)** as a whole; not all their auxiliary results were verified. There is no verdict of falsity here. |

The precise pending step in `thm:shadow(a)` is at lines 2841–2849: `prop:crossed` is applied in the category of complete spaces with the tempered action. To validate this result one has to verify continuity and estimates of the comparison maps and homotopies on the spaces actually defined; an algebraic equivalence is not enough. `thm:excision-input` (1678) and `thm:kunneth` (1765) were inspected: they contain arguments, they are not inputs assumed without proof. I have not proved that their constructions are incorrect, nor completed the audit of all their topological dependencies. For that reason the verdict is (c), not (b).

For the stabilisation a direct check can indeed be given. A new prime `ℓ` contributes

`(log ℓ) Σ(k≠0) ℓ^{−|k|/2} F(δ_S(ℓ^{−k}))`.

On the units, the regularised integrand is zero because the inflation is constant in the new coordinate. If `log ℓ` exceeds the radius of the support, each remaining term is zero. The limit is therefore an eventual stabilisation of values, not a spectral convergence of operators nor an unlimited interchange of series.

The relation with the literature must be formulated result by result. The Weil distribution and its reading as a trace are not new: [Connes](https://arxiv.org/abs/math/9811068) develops the geometric realisation of the explicit formula; [Meyer](https://arxiv.org/abs/math/0312305) computes homology of adelic crossed products, with objects that must be distinguished from the algebra and the twisted coefficients of this paper. The semilocal twisted computation proposed here is not automatically identified with Meyer's result, but its bibliographic priority has not been established either. **Novelty of the exact Hochschild package: (c)**. The text acknowledges the logical independence between its two constructions and that the link of coinvariants with the local density is not an identification with Hochschild homology (introduction, 140–151).

### Paper 44

For the two main theorems expressly formulated as `introA` and `introB`, the verdict is **(a)** under the hypotheses indicated; this verdict is not automatically extended to each secondary result of the paper.

The crucial definition is `Frob_n=μ_(c_n K_P(n))`, with `P(n)⊂S_f` and probability Haar measure. The representatives and supports are computed at 1153–1200. Since the convolution of two Haar measures of cosets in this abelian group is the Haar measure of the product coset, and `P(mn)=P(m)∪P(n)`, one obtains `Frob_m*Frob_n=Frob_mn`. The constant modulus `1/n` recovers n. The semigroup inverse keeps A and replaces r by `1/r`; the product with the adjoint is `μ_KA`, not always the unit. Thus non-existent inverses are not introduced.

The argument of non-existence of continuous interpolation (`rem:nointerp`, 1232–1260) is also correct. Projecting at a prime `p≠q` gives a point mass at `1/q` at time `log q`. The convolution roots and continuity force point masses for all times. A continuous homomorphism from the connected interval to the totally disconnected group `Z_p^×` is constant, and the law forces it to be 1, a contradiction.

For the contact (`thm:frobcontact`, 1441–1510), the support condition eliminates all the layers except `p^k` if `n=p^k`. The density on that layer is `p^{-k/2}` and its local volume is `log p`, giving exactly `Λ(n)n^{-1/2}h(1/n)`. For n with two prime factors no layer remains. At the real place, the finite coordinates of `j_infty(x)` are 1; hence the indicator requires `s^N | n−1` at each prime foreign to P(n). With Haar measure `dx/(2|x|)` and the positive real support, the change `x=e^{-t}` gives `1/(4sinh(t/2))`. This factor is compatible with the statement, without a lost factor 2.

The hypothesis `P(n)⊂S_f` is active throughout the section, from 1149; it is not missing in the theorem even though reference is made to the definition. Nor can the contact of functions be replaced by `T(Frob_n)` as a value on a measure: the text itself explains the lack of a continuous weak extension. The Frobenius terminology is an analogy of composition, not a realisation of an endomorphism of a curve.

**Novelty:** the contact coefficients are those of Weil; they are not new. The laws of cosets are consequences of Haar measure and inverse semigroups. There may be a useful particular presentation of the semilocal semigroup and its obstructions, but priority of that formulation has not been proved. Compare with [Connes–Consani–Marcolli](https://arxiv.org/abs/math/0703392), where the action of idele classes is already connected with correspondences and positivity.

### Paper 45

**(a)** for the comparison theorem `thm:comparison` and the radial normalisation requested; **(a)** for `thm:sufficiency`, the primitive criterion used by 46. Not all the later results on radicals are certified by this conclusion.

The change of variable has an important convention: `Γ_h(w)=h(−log|w|_S)`, so that `λ_−(Γ_h)=Φ_h(1)` and `λ_+(Γ_h)=Φ_h(0)` (523–525). Inverting those labels is by itself harmless in the symmetric term, but they must be kept in the individual identities.

In `lem:radial-trace` (582–634), the real term is

`W_infty(Γ_h)=(γ+log(4π))h(0)+∫₀∞ [e^{−t/2}/(1−e^{−2t})][h(t)+h(−t)−2h(0)e^{−t/2}]dt`.

To check the constant, substituting `u=2t` in the symbol gives

`J(τ)=ψ(1/2)−Re ψ(1/4+iτ/2)`.

Since `ψ(1/2)=−γ−2log2`, the result is `logπ−Re ψ(1/4+iτ/2)`, exactly **−m(τ)** of paper 46. The kernel K of 45 is half of the K of 46, since the former multiplies the sum `h(t)+h(−t)`; this is not a discrepancy of normalisation.

I reviewed the contour argument of `lem:contour` and `thm:EF` (772–981). The symmetry transforms the integral on the line −1 into the negative of that on the line 2, which is why `1/(πi)` appears, not `1/(2πi)`. On parametrising the critical line, the factor 1/2 of the gamma logarithmic derivative returns `1/(2π)` in the real integral. The Euler term contributes `−Λ(n)/sqrt(n)` for each `h(±log n)`. The heights chosen avoid the zeros and make the horizontal edges disappear. The compact support makes the prime sum finite.

On subtracting the terms, one obtains

`T_lim(Γ_h)=Φ_h(0)+Φ_h(1)−Σρ Φ_h(ρ)`.

The Mellin product for `F*G†` is `Φ_F(s) overline(Φ_G(1−bar s))`; thus the hermitian formula and the real formula imported by 46 also coincide. Adding `c h(0)` does alter the formula: the value c=0 depends on the normalisation previously chosen, it is not selected by an independent geometric principle.

**Novelty:** it is a verification of compatibility of normalisations and an exposition of the classical explicit formula; not a new explicit formula. The direct antecedents include [Connes–Consani, appendices B, C and E](https://arxiv.org/html/2006.13771), [Meyer, spectral interpretation](https://arxiv.org/abs/math/0412277) and [Burnol, local terms and conductor operator](https://arxiv.org/abs/math/9902080). The explicit construction of even and odd tests may have expository value, but the mechanism of interpolating zeros and damping the tail is correctly attributed to Yoshida/Connes–Consani.

### Junctions of rows A B C with the form of 46

| Junction | Check |
|---|---|
| 43 `thm:chartcomp`, `thm:colimtrace` → 45 `prop:colimit` | **(a)** in the radial case and under the support restrictions indicated. |
| 43 `lem:radialtrace` → 45 `lem:radial-trace` | **(a)**, inversion of the profile compensated by the symmetry of the sums and of the kernel. |
| 44 radial algebra → 45 convolution and moments | **(a)**, Haar measure of the compact group normalised to 1. |
| 45 `thm:EF`, `thm:comparison` → 46 `comparison`, `eq:W` | **(a)**, sign, `2π`, conjugation and polar term compatible. |
| 45 `thm:sufficiency` → 46 `thm:all-support` | **(a)**; each test constructed fits in some window, not necessarily one fixed in advance. |

There is no proved junction between a geometric Hochschild positivity and the positivity of `W_T`: 43 does not assert such a result and 46 does not use it. That absence is not a logical error of the declared chain; it limits the interpretation of "carrying Weil's proof to Spec Z".


## Scope of the Lean records

**Verdict (c): this review does not certify the complete formalisation nor the correspondence between it and the papers.** The local records are documentary evidence of a reported compilation, not a compilation repeated during this audit.

`06-alpoge-verification/README.md`, `scripts/AxiomCheck.lean`, `source-metadata/Statements.lean`, `source-metadata/MainTheorems.lean` and `results/axioms.log` were read. The file `README-mio.md`, which appeared untracked by Git at the start, was neither modified nor used.

The log contains `riemannHypothesis : RiemannHypothesis` and reports only `propext`, `Classical.choice` and `Quot.sound` for five main theorems. The check script does ask for `#print axioms` on those names. `Statements.lean` expresses zeros of zeta excluding even negative integers, a zero-free half-plane for Dirichlet characters except for the pole, and zeros of L in the open strip. Those formulas have the scope that their names suggest at the level of the visible expressions.

This does not yet establish:

1. That the transitive definitions of zeta, L and `RiemannHypothesis` of the compiled environment are exactly those expected; `Statements.lean` imports Mathlib and does not contain that whole environment.
2. That the log corresponds to the totality of the source tree and to the binaries whose chain of trust is meant to be verified.
3. That each human statement of 49–56 is a faithful translation of a formal declaration, with the same constants and hypotheses.
4. That a formal proof of the final result automatically validates a different prose proof of the same result.

The README describes an archive of approximately 175,000 modules and a large-scale compilation. That archive was not downloaded or rebuilt in this task. Nor were `lake build` or an independent kernel run. For that reason "Lean verified" is not reported as a result of this work.

The next useful check would be a bidirectional map between the central statements of each paper and exact Lean declarations, including their definitions and the transitive tree of dependencies. This task is different from reviewing the logs and different from auditing the human proofs, which was the main assignment.

