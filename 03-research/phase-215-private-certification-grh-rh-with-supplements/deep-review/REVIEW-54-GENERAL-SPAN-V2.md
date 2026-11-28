# Paper 54: general spanning, V2 review

Text: `04-papers/54-covolume-theorem-one-theta-lift-hecke-l-values/main.tex`, working version of 28-11-2026. The manuscript was not modified. This review covers **po:span/psp:main/psv:main in general rank**, not only the rank-one case `psu:arch`, and does not replace its proof by `auxcore` of 53. Lines 4673–7108 were read in full, together with the proof of non-vanishing of the carrier 2544–2687 and its properties 2528–2542. `ppe:main` in general is reviewed in a separate report by the theta review.

## Updated verdict: character failure in the printed version

**(b) The literal proof of po:span is not established.** During the final cross-check with the theta review and the overall review it was identified that the definition `νflat=ν'' υ^m/χ'` of 2695 (repeated at 7584) contains a factor υ^m that the later applications omit. The first incompatible equality of the third exchange is 2732; within the proof audited here, the first failing line is **6448**, which attributes to νflat υ^m the weight a=m−μ1. The printed definition gives a=2m−μ1.

This has a checkable consequence stronger than a discrepancy of names. Changing the source character from a=m−μ1 to a=2m−μ1 multiplies the action of U(S) by det(h)^(−m). Hence the printed identity H5 must carry that extra factor. In the integral that defines F⁰(1), the intended integrand had central weight zero (u3=(0;3m)+u1+u2); the actual integrand carries det(h)^(−m). Under the compact centre of U(2m,m), h↦zh, there appears z^(−3m²), non-trivial because m>0. The integral is absolutely convergent and Haar invariant, so that **F⁰(1)=0**, contradicting the assertion F⁰(1)≠0 of the proof. This does not prove po:span false; it identifies why its literal proof fails.

**Repair sufficient for this branch:** define νflat=ν''/χ', without υ^m. Then α=νflat υ^m again has weight m−μ1 and H5, the reproduction and the final inequality below are restored without changing any bound. `psv:char` does not change: α° is computed directly as b/ν'', not through νflat. The check of the remaining applications pte/ptf/pfq and of the L-value belongs to the report of the theta review, and is not presupposed here.

The rest of this report constitutes **(a) for the repaired deduction, conditional on the common inputs identified in §6** and the functional precisions of §7. The collation of the normalisation of the splitting of 49 remains recorded in `REVIEW-PHASE49-V2.md`; it is not turned into a proved result by being cited. Before the final cross-check H5 had been verified under the weight asserted at 6448: this update expressly corrects that boundary and takes precedence over any unconditional reading of the following paragraphs.

## 1. Approximation and sizes, psp 4673–5276

The chain `avg → decay → pack → hommin → prodtheta → sparse → sparse2 → isol → approx → main` was reconstructed.

* The Fock identification used in `avg` gives a scalar intertwining operator. Its coefficient on the vacuum is a positive Gaussian integral; the lower bound for that scalar allows division. No volume factor was lost: a unit vacuum and a Gaussian measure of mass 1 are used.
* `decay` applies Cauchy–Schwarz after dilating the homogeneous polynomial of degree d; the mass of the majorant is ≤exp(n)||v||². The inequality |y|²≤2||σ||²(|x|²+|σx+y|²) delivers the power 2n of decay. The case n=0 is separate.
* In `hommin`, the Euclidean dual is 2ε·different⁻¹Λ; Banaszczyk's bound for the last minimum produces a short rational basis. A non-zero homomorphism has non-zero image on some vector of that basis. This gives the separation used for the lattice sum, with the denominator fnN_d written in the text.
* The finite average modulo π_M² removes exactly the terms not divisible by π_M². Since |τ(π_M²)|=M, the separation obtained grows with M, not with sqrt(M). In the application M≥b²⁰ and product of minima ≥b⁻¹³ give the required separation; d≤b^(3/2), q=2n_*.
* `prodtheta` does not introduce an unknown positive constant: the product theta·conjugate(theta) cancels the global phase. `psq:thetanorm` 5476–5512 proves it by Parseval and normalisation of the vacuum.
* In `isol`, there is no need to select a measurable family of approximants: one approximant is fixed and the continuous function obtained by rotation is integrated. The projection by rotation and H3 produce the bound (4b^{n_*}+1)δ.

In `approx` 5188–5233, the minima give (5b^{3/2})⁻¹/²(5b²⁴)⁻¹/²≥b⁻¹³. The sparse error b⁻²⁰ⁿ multiplies the integral bounded by bⁿ I_{u3}; the result is exactly

    |F(gh)−F⁰(h)| ≤ 2b^(−19n_*) |F⁰(1)| |h|^(6n_*).

H5 and H3 give F⁰(1)=I_{u3} φ°(g1)||v||²≠0. At 5235–5252, B=b^{n_*}>10 and (4B+1)·2<B²≤B¹⁹ contradict the final bound. The numerical inequality needed has room to spare and holds uniformly in the declared range.

## 2. P and H1–H3, psq 5277–5722

The proof of P uses a transvection associated with a short vector that is isotropic by integrality and product of norms. The triangular decomposition is determined by the principal minors p_k=1−2 Re(t)Σ_{i≤k}s_i|v_i|². The weight factor is bounded by exp(2Aη)(1+η Im z)⁻¹/². The periodicity comes from the purely imaginary level p; Schwarz on the disc/cylinder contradicts the peak character, since exp(2−2π)<1/2. The levels of the two applications are ±sqrt(−d) and ±M sqrt(−d); π_M divides M and hence the available invariance implies the necessary one.

For H1–H3 the following were checked: GB is open, G∩B=T; the function of minors φ_u is defined because the minor of the positive block does not vanish; the diagonal rotation has strictly positive weights on the relevant triangular coordinates, and hence kills all the non-constant Taylor monomials. The coefficient of the discrete series is φ_u by the vector of minimal K-type and the argument of the cone of K-types. The reproduction H3 is Fubini plus the average over the torus; it does not require a new formal degree constant.

`psq:degree` 5527–5563 gives d_P≤7fmb≤b^(3/2), using f≤x¹², m≤2sqrt(x), b≥x²⁶. `psq:unitvac` 5568–5593 explains correctly that the global scalar c of the vacuum is absorbed by κ|c|²=1, not that each arbitrary realisation comes automatically normalised.

## 3. R in the whole range M'>2n, psr 5741–6227

The proof by neighbours of lattices was verified: an x∈L'\L with πx∈L gives L₁=L_x+Ox self-dual, a neighbour of L, and reduces d(L,L') by at least 1. For each hyperplane H there are at most q₀ isotropic lines different from L/H in the Hermitian plane H♯/H. Thus N=q₀(qⁿ−1)/(q−1) and #ball(k)≤(N+1)^k.

The local sums are bounded by ε_v≤3.6q_w⁻³/²≤.28 at split places and ε_v≤1.8q_w⁻¹≤.2 at inert ones. In the second case q_w=q_v²≥9; the series over primes converge. A finite number of factors R_v close to 1 and a tail whose sum of ε_v is ≤1/3 show injectivity of R. **It is not required that the global sum of all the ε_v be <1**, which would be an invalid inference in variable degree; the text avoids that inference.

`psr:SW/Egrowth` 5990–6062 extends the Siegel–Weil application to the positive definite target and M'>2n. The additional argument for the sum of absolute values is necessary and is present: f_Φ≤cf₀ on P(A)\G(A), translation controlled by exterior norms, reduction to representatives of norms bounded by a power of the height. No attempt is made to deduce the growth of the absolute sum from the growth of the sum with signs.

`psr:rallis` 6064–6133 follows doubling/unfolding with absolute integrability. The point of injective support is indispensable and is obtained from sharpness at a place of the non-empty modulus. R only needs A≠0: it does not use the exact absolute value of A. In `vanish`, orthogonality to rapidly decreasing functions, Fubini and the absolutely convergent series give ||R(κ*ψ)||²=0; continuity and injectivity of R give κ*ψ=0.

`psr:R` 6146–6227 is finite linear algebra: the intersection of kernels of the L_{p,i} is contained in kerℓ. The finite classes and the stability of Q under the real compact group annihilate the complete lift, not only its values at representatives. δ_ι is sharp, A₀=tι and A₀ι=1. There is no requirement of uniformity in the coefficients a_{p,i}(g): the later proof only requires their existence and independence of ψ.

## 4. H5 and carrier, pss 6241–6573 and pte 2544–2687

The quadratic derived action is obtained by commutators with the Heisenberg algebra. The torus-weight argument restricts the non-compact operators to second-order derivatives that annihilate the polynomials used. The compact operators are computed directly. The identities of minors are the identities of replacing one column by another already present.

For H5 one factorises P=P⁺P⁻ in disjoint variables. The two realisations of the action differ by a character det^k of the connected unitary group; the total weight on the torus determines k. The coefficients are exactly ||P⁺||²m_{w⁺} and ||P⁻||²conjugate(m_{−λ}), whence

    c_P(h,1)=||P||² m_{u2}(h) conjugate(m_{u3}(h)).

u3=(0;3m)+u1+u2 and the integrability threshold were verified. This does not presuppose an arbitrary phase between the representations.

Non-zero carrier: the Witt decomposition has an integral matrix of determinant −1; the Fourier coefficient H=1 selects M_uM_u*=1, a single rational orbit of U(V). The unfolding removes the rational quotient. Compact invariance gives a sum over finite cosets. The support of the vacuum in the mixed model forces Y integral, hence Y∈K_V; only one coset remains. The non-zero archimedean slice is chosen with invertible matrix by density. The elements of the unipotent radical allow all the Heisenberg translates of the slice Λ≠0. The final non-vanishing can be justified by Parseval as in §7. The rapid decay uses the exchange `pte:carrier` and invertible support; the existence of the non-trivial tame character is available in the data, and is not deduced from the spanning result itself.

## 5. Data and weights of psv 6593–7108

The order o reverses the fixed order within each block. The formula for row lengths was read in that order; the conditions of initial and final segment of the minors were not interchanged.

* α°=υ^{m/2−j}; a''+a°=n/2−κ_j. The parity m, k even and r odd makes the exponents integers.
* The polynomials of K° use only negative columns and initial segments of o. They give u°positive=−a°, u°negative=n°−a°+ell⁻. They are non-zero and form a finite space stable under U(V°)_∞.
* The datum Ψ° is literally δ_ι modulo π_M², without scale or additional level. n°=5r−9m−1>2r. The other application has rank(Wflat)=6m+1>2rank(S)=6m.
* The conjugate of y has weight u=−Λ^K(varsigma). The differentiation of the convolution is legitimate by integrability of all the derivatives of the coefficient; the conjugation Y↦−εY*ε is respected.
* The F_i have weight u''; substituting the row lengths and a''+a° one obtains u''+u°=u both in positive and in negative coordinates.
* Both u, u° are dominant, of gap ≥300n_* and entries ≤5b. The applications of R and of isol use exactly these weights.
* `psv:split` 7010–7043 places α(det x)⁻¹ once only in the factor tildeW; the factor Wflat has characters (1,υ^m). That assignment is the one that produces u1=(−Δ';6m+1). There is no duplication of the source character.

## 6. Imports and absence of circle

The branch reviewed uses the local models and compatibility of sums of 49; the coefficients of discrete series, integrability and formal degree of 49/51; sharpness, doubling, growth and reduction of 53; and the exchanges/carrier/identification F_i of the earlier part of 54. Their constants are not recomputed here as though they were independent of those results. The respective reviews must be incorporated into the global verdict.

In particular, the formula R is proved by Siegel–Weil in convergent range and a series of translates; **it does not use** po:span, the covolume theorem nor the final non-vanishing of L₀. The non-zero carrier has a Fourier proof independent of the exchange scalars. H5 is local representation theory and comparison of weights. No circle was found in these dependencies.

## 7. Two sufficient local functional precisions

1. **psv:c, around 6806**, says that the smooth vectors are Schwartz functions in a Schrödinger model. That identification needs the representation with respect to which smoothness is taken to be specified; it does not follow automatically for any unitary subgroup. It is not used: take E=Schwartz in the general version of `pss:coefs(a)`. The polynomial-Gaussian has C∞ orbit in Schwartz by the explicit argument of `pss:carrier` 6530–6548; the fixed action and theta are continuous on Schwartz. The same holomorphy results, with exactly the same weight. The same justifies the parallel step of `psv:F`.

2. **pte:carriernz, final paragraph 2680–2686**, calls closed the kernel of all the translated theta functionals in the irreducible Hilbert space. Theta is not by itself a continuous functional on L². For the Schwartz slice Λ, `psq:thetanorm` suffices: the integral of |theta(rho(w)Λ)|² over W_I(F)\W_I(A) is ||Λ||²>0 (or a positive scalar if a non-normalised realisation is used). Hence not all the translates can vanish. This proof avoids the unnecessary topological assertion and does not change constants: only non-vanishing is required.

These are proved local repairs, not failures of the spanning statement. The global dossier must keep the distinction between the literal text and this additional justification.

## 8. Documentary closure of SW and propagation of the defect

The primary source [Weil, Acta113 (1965)](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5988-11511_2006_Article_BF02391774.pdf) was downloaded and read, temporary local copy `/tmp/weil-spanning.pdf`, extraction `/tmp/weil-spanning.txt`. In addition p41 was inspected visually to resolve the fractions badly recognised by OCR. P41: Hermitian case I₂, ε=1/2. No38/p55: condition B m>2n+4ε−2. Proposition8/pp75–76: convergence if the index r_T=0 or m−r_T>n+2ε−1. Theorem5/pp76–77: positive invariant measure of mass 1, absolute convergence, one place with U(0) non-empty and local transitivity on each U(i); then I=E. These hypotheses correspond to 53:909–925/952–958.

In both applications of R, T is positive definite, so that r_T=0; the ranks are 6m+1>6m and 5r−9m−1>2r. A split place exists (in particular those of the modulus π_M²), and there matrices of rank n with isotropic image are chosen; transitivity is the extension of isometries/Witt in the split case. Weil's mass-1 normalisation is transformed exactly into the factor vol([U(T)]) written in 53. For R it only matters that the global factor and c' are non-zero. The additional absolute growth is psr:Egrowth, already reconstructed, and is not an omitted hypothesis of the classical theorem. **The import of SW needed for this branch is collated; no separate (c) remains for that range.** The identification of the model/splitting remains the common input from 49, not an uncertainty about Weil's range.

Literal propagation of the defective νflat to volume 58: definitions in `58*/main.tex` lines 51272 and 56151. In 54 the two definitions are at 2695 and 7584. They must be corrected in a coordinated way; altering the assertion H5 is not enough. For the central defect one can fix a single archimedean place and put h=z·1_{3m}; the additional character is z^(−3m²), so that there is no cancellation between distinct places. Absolute integrability allows translation by that compact centre and forces F⁰(1)=z^(−3m²)F⁰(1), hence F⁰(1)=0.

## 9. Final coordinated note

Update after reading `../review-v2/REVIEW-SPLITTING-V2.md` §§6–7 and receiving the closure of pte/ptf/pfq/KS from the theta review:

* **Current text: (b).** It keeps νflat with the superfluous factor υ^m. Consequently the literal proof uses an F⁰(1) that equals zero; see the central computation of the first section. The current text is not certified as though the correction were already incorporated.
* **Proof reconstructed with νflat=ν''/χ': (a), in the audited scope.** psp, psq, psr, pss, psv in general have been closed; the two Schwartz/Parseval precisions are proved here. The theta review closed the imports pte/ptf/pfq/KS with the same corrected definition. No independent mathematical obligation of those sections remains unresolved for po:span.
* **SW of 53: (a) for the imports needed here.** The primary source, hypotheses, range and mass were collated in §8; no regularised formula outside the range of convergence is being invoked.
* **Splitting of 49: historical pending item withdrawn for the reconstruction.** The coordinated report identifies, by means of Chan, the RV index with the Gaussian of the norm and, by means of Murase, the generators and the compatibility with sums/doubling. The supplement preserves the representation, not only its projective class; hence the computations of weights, character factors and normalisations of the present review can be used. The impossibility of reading the original pages of Kudla remains as a bibliographic limitation, not as an undetermined mathematical phase.

This (a) refers to a mathematical check carried out and reconstructed by hand, not to a formalisation in Lean nor to an automatic certification of every line of the repository. The principal distinction is concrete: the printed text requires correcting the two definitions of νflat in 54 and their propagation to 58, whereas the corrected spanning deduction has already been reconstructed with its constants.
