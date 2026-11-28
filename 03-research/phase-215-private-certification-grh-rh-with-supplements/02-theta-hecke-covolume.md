# Review of 49, 50, 53 and 54: theta, Hecke and covolume

Date: 2026-11-28. Source: `main.tex` of the local copy, not papers 47–48. The line references are those of the source file. It does not represent the opinion of the researchers mentioned by the author.

> **Update from the deep audit:** this file keeps the PRELIMINARY verdict. Its pending items are not the final state. See [THETA.md](deep-review/THETA.md), with incremental proofs and obligations. There the arithmetic instantiation of P50 (HE01) was closed, and the exact CM constant, the divisibility of P49 at all primes, the attained bound of P54 and the rank-one norm formula were reconstructed. A concrete failure of characters in P53 `pcu:product`, lines 3351–3360, and a functional failure in the Hilbert bounding of the slices were also corroborated. The character error and its impact are documented in [ERROR-53-CHARACTERS.md](deep-review/ERROR-53-CHARACTERS.md). The reconstructions do not certify each literal line nor GRH; THETA specifies the minor repairs and the normalisation obligations not yet collated.

## Preliminary scope and verdict

The review distinguishes the proof of a local result from the verification of all its automorphic antecedents. **I do not certify papers 49, 53 and 54 in full nor the conclusion GRH.** I have checked the algebraic structure of paper 50 and several concrete steps of the other three. For the statements whose full development I have not been able to check I give (c), and I specify which part remains pending; this does not mean that the proof is false nor that the manuscript necessarily omits that part.

| Question | Verdict | Exact scope |
|---|---|---|
| 50.1: `ph:thm` in `ph:eq-large` | (a) | Algebraic theorem under its printed hypotheses of §2.1; the deduction and its inequalities are verified. The inputs are checked in 50.2; this does not certify the arithmetic applications of 50.3. |
| 50.2: `ph:root`, `ph:count`, `ph:av` | (a) | The arguments of §3 supply these inputs and the numerical hypotheses of their internal application hold. |
| 50.3: range used afterwards | (c) | The cited statement and the result obtained coincide; the numerical substitutions being verified, the whole arithmetic construction of the data and the weak approximation of 49 remain uncertified. |
| 49.1: seesaw independent of the twist | (c) | The whole transfer of periods, convergence and descent of archimedean types not verified. |
| 49.2: conjugates and exact CS constant | (c) | The arithmetic of area factors in (C4) checked, conditional on the classical formula cited; the whole reciprocity and normalisation of the vacuum not certified. |
| 49.3: divisibility at all primes | (c) | The specific treatment of inert primes, the ramified prime and the level identified; not all the integrality arguments for the kernel verified. |
| 53–54.1: exchange and absolute constant | (c) | Not all the local and archimedean terms of `pcx:X` checked. |
| 53–54.2: injectivity and factorisation | (c) | The abstract injectivity of the triangle is indeed checked; not all the automorphic hypotheses that apply it. |
| 53–54.3: Gram and L-values of one lift | (c) | The identity of determinants verified conditional on `po:glue`; its automorphic antecedents remain. |
| 53–54.4: test form and attained valuation | (c) | The ultrametric deduction of `psm:attained` from its inputs verified; not all the inputs nor the orthogonality to false lifts. |

In the preliminary review no counterexample justifying (b) had been identified. This point was superseded by the failures of P53 documented in the update above; the following tables are kept as a record of the first stage.

## 50: mathematical checks

File: `04-papers/50-elementary-divisors-edge-hecke-operator/main.tex`.

### The statement actually proved

Lines 335–409, `ph:thm`. The ring is a valuation domain of characteristic zero, with (w^2=p), and the cycle has (N\ge2) even, (P=p^e\ge5), (q=P^N). The edge freeness condition `ph:eq-free` is required. The result controls the colength **truncated** by (p^j\Lambda):

\[
\operatorname{col}(\Lambda,Y\Lambda+p^j\Lambda)\mid p^l,
\quad l\le (3c_d+\theta j)|X||H||\mathcal B|.
\]

The paraphrase "small mean of elementary divisors" must keep the exceptional fraction (\theta) and the truncation. It is not a uniform bound independent of (j) for all the elementary divisors, nor does it by itself ensure that (Y) is invertible. This is a clarification of interpretation, not a failure of the printed theorem.

### Algebra of the deduction

* `ph:near`, lines 449–481: the diagonal form can be obtained by finite operations in a valuation domain; a DVR is not required. The independence modulo the maximal ideal of the columns of (Q) and of the selected columns of (U) is proved by applying the left inverse (R). The module to which Nakayama is applied is finitely generated, even if the ring is not noetherian.
* `ph:fact`, lines 543–552: the transposition and the order are correct. The relation (\mathsf b\rho({}^tg)={}^t\rho(g)\mathsf b), together with the diagonal commutation of (\Delta) and (\mathsf b), produces exactly (A(1\otimes\mathsf b)).
* `ph:null`, lines 554–576: the jet argument uses CRT and the count of the reduced monomials. The condition on the number of points gives independence as well as generation. If an infinite set (Z) is allowed in the statement, it suffices to take a finite subset of the required size.
* `ph:depth`, lines 578–629: the forms (z_v(y)^{P^j}) recover all the coordinates (y_{ac}). The determinants employed are not zero because their terms are distinct monomials. The sum of weights of the monomials gives the bound (c_d|\mathcal B|).
* `ph:ends`, lines 631–651: the passage from possibly non-discrete valuations to integer exponents is valid: one counts how many integers (\delta\ge0) satisfy (t_i\nmid w^\delta), that is, a rounding up. Discreteness of the valuation is not being assumed.

In lines 706–749 one obtains (A'={}^td'Zd). The congruence of the average gives (\mathcal A\mathcal B\equiv p^{2Nc_0}\pmod{w^c}), not (p^{Nc_0}): the second factor comes from (\mathsf b\mathsf b'=p^{Nc_0}). The text keeps both factors. Finally

\[
\det d'\det d\mid w^{\lambda+\lambda'}\mid p^{\max(\lambda,\lambda')},
\]

by (w^2=p), and this produces the final coefficient (3c_d). No factor 2 is missing in that last conversion.

### The three inputs

**Root** (`pe:root`, lines 925–1025). The substitution constructs a polynomial (\bar\Phi) over (R/w^{\lambda+1}R) of degree (q\nu'), with non-zero leading coefficient. For each representative of (\mathbb F_q) it is divisible by a power ((t-a_r)^\nu). The differences (a_r-a_{r'}) are units; hence these factors are comaximal and their monic product divides (\bar\Phi). The degree argument remains valid even though the quotient ring has zero divisors, precisely because the divisor is monic. One concludes (\nu\le\nu'). There is no need to introduce a field hypothesis in this step.

**Count** (`pe:count`, lines 1230–1251). The delicate point is the volume of `pe:vol`, lines 1120–1171, which uses interlacing, the Jacobian (P^{kN}\Delta(\sigma)), and the Euler product. The factor obtained is

\[
\prod_{l=1}^k\frac{q-1}{q^l-1}=[G:I]^{-1}.
\]

The packing construction in `pe:flag` transforms the count of monomials of fixed degree into a volume of dimension (kN), using a thickness of size one; a set of volume zero is not being compared directly with its number of points. The hypothesis (24Nk^2cP^{2r}\le\theta n) implies (x\le\theta/2\le1/2), whence (e^x\le1+2x\le1+\theta).

**Averaging** (`pe:avg` and `pe:av`, lines 1259–1328 and 1430–1500). The average is constructed algebraically by means of traces, not by dividing by the order of a finite group that might be a non-unit. In (S1), the limit (d+k\le q) is sufficient: a homogeneous form of degree between 2 and (q) does not disappear on reduction modulo (X_v^q-X_v); the monomials of degree (q) that reduce to degree 1 do not cancel with terms of degree 1 of the same homogeneous form. The submodule (U^+) is finitely generated because the algebra (\mathcal S_d) is the image of a finite free module and there are finitely many initial vectors. Thus its use as a free module in the trace is legitimate over a valuation domain. The weight estimates in `pe:wd` keep the error (2c), sufficient for the threshold (c^*=3kc).

### Internal range and application to 49

Lines 1505–1517 verify explicitly, from `ph:eq-large`, the conditions of `count`, `av` and `near`. In particular

\[
P^{N/2}=\sqrt q\ge n^2>Nk(N/2+2)n+n+k,
\quad 24Nk^2(5Nc_0)P^{2r}\le\theta n.
\]

The application of lines 1519–1531 uses (n=a=xb), (r=\lceil\log_pm\rceil), (P=p^{o_0}), (N=o/o_0), (\theta=(m^2f)^{-1}). Its two verifications are (q\ge a^4) and ((Nk\log q/\theta)^5P^{3r}\le b\le a). The conclusion (3c_d\le12A_{\mathfrak l}/(mp)) has the correct factor because (A_{\mathfrak l}=aN/2).

The arithmetic part of lines 767–831 uses, in addition, weak approximation, freeness of (J), the identification of all the factors of the representation and the parity of the places of the cycle. I have read that reduction and found no contradiction; I have not certified here the antecedents of 49 that provide these data. For that reason the question on **all** the later applications keeps (c).

## 49: precise location of what is pending

File: `04-papers/49-short-forms-theorem-theta-lifts-complex-multiplication/main.tex`.

**Seesaw.** The result of 46 `au:seesaw` allows the chain datum (\Psi) to depend on the twist, but not (c_{\rm ss}). Nor does it assert non-vanishing of the two sides. In 49, `ps:onestep` (3983 ff.) reduces the transfer to a single orbit; stages (3), (5), (6) are expressly referred to `pk:vanish`, `pk:coarse`, `pk:fine`. It would not be legitimate to flag those referrals as gaps without checking their destinations. What is missing in this review is to verify those destinations, the absolute convergence on exchanging integrals and sums, and the assembly that keeps the scalar independent of the twist.

**CS constant.** In `ps:conj` (3845), the requirement is exactly (|t_\sigma|^2=\Omega^{-1}). `pk:conj` (5433) uses (t_\sigma=\sigma(\varpi_{\rm vac}/\mathsf u)c_\psi/\Omega_\sigma). The proof of (C4), lines 5304–5340, does not limit itself to citing an equality "up to an algebraic number": it constructs (\mathsf u^{12h}=\prod_i\mu_i^{12}\Delta(\Lambda_i)) and asserts the exact identity of areas. I checked the combination of factors shown: from (\operatorname{area}|\Delta|^{1/6}=4\pi^2\operatorname{Im}\tau|\eta|^4) and from the average (c_{CS}-\log(2\sqrt d)) there results (2\pi^2e^{c_{CS}}/\sqrt d), as written. I did not check the starting formula against the full text of Chowla–Selberg, nor all the transports of differentials, the unit at 2 (`pf:CS`, 6911), and the reciprocity `pf:recip` (7111). For that reason I do not certify the final exact constant.

**Divisibility.** `pa:count` (2522) expressly distinguishes the ramified prime (p=d), with additional deduction (\frac12\sum_\tau\mathrm{ded}_0(\tau)), and limits the jets to the nested Schur columns. The substitution by new directions of 2557 ff. gives the factor (\varpi^B\prod\det(g_{\tau,h})^{\kappa_\tau(h)}); the three classes of congruences (a)–(c) cover the pairs of heights (h=1), (h\ge2,h'=1), (h,h'\ge2). This combinatorial control does not by itself prove that the real kernel has the required normal form. It remains to verify `pa:kernel`, the treatment of 2 and of the primes of the level, and `pl:level`. The level (N) is treated separately in `pa:level` (3169): it must not be confused with an application of the Hecke theorem of 50.

## 53–54: what is checked and what is not

**Exchange.** In 53 `pcx:X`, lines 1772–1795, one requires (a=b+2e\), (q=q_V+q_{V'}\), (2q+2\le N\), (N\le2\mu_\tau+2q\), non-trivial modulus and character with non-trivial tame part at each chosen prime. The scalar has (|c|^2=C L_*(\mathfrak m,\nu,e)); it cannot be replaced by a universal constant independent of the character. The independence asserted corresponds to (C) and to the vector (x). The transposition of splitting indices in `pcx:eq-dict` (1809 ff.) is indeed exact from the two printed definitions. I have not audited the whole computation of (C), nor the complete proof of `pcx:X`; the classical Rallis formula does not replace that verification.

**Injectivity.** `pc:tri-inj` (53, 557–580) is a correct linear algebra argument, with the hypotheses (T1)–(T3) of `pc:triangle`. It does not divide by (\sigma_{i,n}) to prove injectivity, so it does not incur circularity when it is afterwards deduced that those scalars are not zero. What is pending is the automorphic realisation `pc:tri` (1248) and the first lift: verifying the abstract triangle is not enough to certify `au:inj` or `au:factor` of 46.

**One lift.** In 54, `po:ss-proof` (1134–1164), (\Delta_j) is the determinant of the comparison operator **compressed** to the space of lifts. The identity

\[
\det(\Theta^*\Theta)\det(\operatorname{pr}_{\mathrm{im}\Theta}U|_{\mathrm{im}\Theta})
=\det(\Theta^*U\Theta)
\]

is correct for an injective (\Theta): it is obtained by writing (\Theta=QR), with (Q) isometric and (R) invertible. It does not require that (U) preserve the image. The equations of `po:glue` and `po:exchange` then give the power (H_j(\vartheta)^{d_j}) that 46 uses. I have not checked all the inputs of `po:glue`, including the generating products, the false forms and the three exchanges. Global verdict (c).

**Attained valuation.** `psm:attained` (54, 8249–8296) constructs (t=M^{12f}c_{{\rm vac},y}\prod B(l_\tau)^2). The choice of a coefficient of minimal valuation in a combination with integral coefficients is valid and has the correct sense. The use of the ultrametric inequality does not allow one to infer equality of an individual valuation: it gives exactly the one-sided inequality declared. The twelve-factor theorem `psm:twelve` and all the inputs of the construction of the coefficients remain pending. `psu:small` (9118) uses in addition integrality and orthogonality of the test form; I have not certified the latter.

**Archimedean bound.** `psu:arch` (9217) cancels (a_\sigma(z)B(z)) between a principal pair and a flat one of equal rank. The cancellation works if (CL), stated immediately before, has the same (a_\sigma(z)) for both pairs. The final proof of the inequality is correct conditional on (CL), on the norm formula and on the size bounds; I have not verified the whole of theorem 9.1 of 53 which establishes (CL). The factorial factor of `psu:normL` must be kept: the highest weight vector has norm 1 and the Fock monomial has squared norm (\prod l_\tau!).

## Junctions reviewed

| Junction | Result of the comparison |
|---|---|
| 50 `ph:thm` → appendix of 49, lines 8639–8655 | Same range, same (c_d), same term (\theta j) and same three inputs. |
| 50, lines 844–847 → 49 `pa:eldiv`, lines 3156–3164 | Same (12A_{\mathfrak l}/(mp)+j_0/(m^2f)), same (j_0\ge0), same truncated colength. |
| 54 `psu:small` → 54 `po:small` | (fmb/k+3x^{35}) is kept; the initial statement already incorporates the corrected constant. |
| 54 `po:small` → 46 `au:hecke`, lines 4992 ff. | 46 expressly mentions the constant (3x^{35}), not the earlier version. |
| 54 `po:ss-proof` → 46 `au:onelift`, lines 4965–4980 | The compression, power (d_j), denominators and the possibility of absorbing a twist-independent factor into (C_j) coincide. |
| 53 exchange → alternative convention of 54/55 | The declared dictionary is an exchange of indices, without factor; not all the later concrete substitutions were verified. |
| 53 triangle → 46 `au:factor` | Depends in addition on the equality of multiplicities of 51; not certified by this report. |

This table **is not an exhaustive audit of every citation** of the four manuscripts. The junctions not listed, including the whole dependence on 55 for regular families, remain (c).

## Literature and novelty

The Chowla–Selberg identity is prior: [Chowla–Selberg, *On Epstein’s Zeta-function* (1967)](https://doi.org/10.1515/crll.1967.227.86). The general theory of regularised Siegel–Weil and Rallis is also prior: [Gan–Qiu–Takeda, arXiv:1207.4709](https://arxiv.org/abs/1207.4709). These located sources corroborate antecedents and do not certify the particular normalisations of these manuscripts.

The most clearly delimited candidate for an autonomous contribution in the block reviewed is the theorem of 50: an integral average compatible with a Frobenius cycle and a count of defects that control colengths of edge operators. The connection proposed in 49 and 54 between exact CM periods, integral jets at all primes and determinant bounds is a concrete research architecture. Its bibliographic novelty and its global validity are not established by this review. There is no basis here for asserting that a new field has already been created or that this architecture proves RH.

## Requested matrix of the inputs of 46

**Concordance of the statement** is deliberately separated from **validity of the proof**. "Coincides" means that the conditions indicated are kept on comparing the passages indicated; it is not equivalent to certifying all the antecedents. For `inj`, `factor`, `hecke` no complete literal comparison of all the appendices was carried out.

| Input of 46 | Concordance examined | Proof and range |
|---|---|---|
| `au:seesaw` (4314) | 49 §5.1.7 develops the result; the datum may depend on (\vartheta), the scalar may not; the absence of any assertion of non-vanishing is kept. | (c): transfer of the orbit, exchanges and complete assembly pending. |
| `au:divis` (4368) | Coincides with 49, appendix 8533–8555: exception (N), ramified moduli, (\ell\nmid\mathrm NQ), (2mfb), (j_\ell=\lceil2mfa/\ell\rceil); it is not asserted that (Y_{\mathfrak l}) preserves the ramified subspace. | (c): the algebraic component of 50 is reviewed; the normal form of the kernels, the level and the assembly of all the classes of primes are not. |
| `au:count` (3900) | Coincides with `pa:count` and `pa:schur`: minors of the first (h) columns or Schur entries, (B\ge1), heights (<n'), loss (fn'^3(1+\log_pB)), and extra term (e=0) for (p=d). | (c): coverage of the congruences of directions reviewed; not the whole proof of normal form and standard monomial theory. |
| `au:kernel` (4497) | Coincides with 49 appendix 8570: (0\le j<m), every conjugate, (\exp(x^{50}+\mathrm{rs}_j/2)). | (c): depends on reciprocity, exact CS constant and explicit comparison of (C_0\) with the data. |
| `au:restrict` (4516) | Coincides with 49 appendix 8580: squared norm, loss (x^{70}), gain (-\sum n_\tau\log N). | (c) for the complete result; the step of 49, 3830–3841, checked **given** integral branching: (|\sigma\bar\pi_N|^2=N) and (c_{\rm br}^2\le L^{6L}\le e^{x^{70}}). The branching construction remains to be certified. |
| `au:expansion` (4532) | Coincides with 49 appendix 8587: finite support, integrality only outside (N\mathrm NQ), and bound (e^{x^{60}}) only for trivial twist. | (c): the elimination of the gluing and the count of coefficients were not reviewed in full. |
| `au:equiv` (4584) | Coincides with 49 appendix 8604: tame character, (\beta_\vartheta(u)\in K^\circ), action by right translation. Dependence on (\vartheta) is allowed. | (c): integrality of each local component of (\beta_\vartheta(u)) and compatibility with the gluing remain to be certified. |
| `au:shortbasis` (4427) | Coincides with 49 appendix 8558 and proof 3587–3622: (c_0) positive integer in the different, bound (6c_0(fn)^2). | (a), checked: elementary transference with dimension (2fn), dual of ((2/c_0)L) contained in (L), and selection of (n) (E)-independent vectors. The result asks for a basis over (E), not an integral basis of the module (L). |
| `au:inj` (4794) | 53 identifies the deduction with `pc:tri-inj` and the automorphic triangle. A literal comparison of all the antecedents was not certified. | (c) global; (a) the abstract argument `pc:tri-inj`, keeping (T1)–(T3). |
| `au:factor` (4850) | 46 keeps (m)-fold twists, exponents (\vartheta^j), power (-\dim\mathcal T) of the ratio factor and Gram quotients. A complete collation of the construction of each ratio with 53 is missing. | (c): requires automorphic triangle, adjoint law and equality of multiplicities (M+), in addition to injectivity. |
| `au:aux` (4878) | Coincides with 53 appendix 16275: (\gamma(1)=1), non-vanishing, (m)-fold twists, integrality outside (Q), squared norm (e^{2x_1^2b^2}). | (c): `pc:auxcore` (1616) explicitly provides the intermediate bound (e^{2x^{201}b^2}) and generators (e^{x^{99}b^2}); not all the twists of the second lattice of lifts were certified. |
| `au:onelift` (4965) | Concordance checked with 54 §2.6: compressed operator, (Delta_j\ne0), power (d_j), twist-independent constant; see detail above. | (c) global; identity of determinants correct given `po:glue` and `po:exchange`. |
| `au:hecke` (4991) | 46 keeps the regular family hypothesis and cites the corrected constant (3x^{35}) of 54. Not all the ratios of its product were collated in full. | (c): CL of 53, sharpness inputs, orthogonality of test forms and regularity conditions imported from 55 are missing. |

The additional check of `au:shortbasis` uses the following. If (\lambda_1(\Lambda^*)\ge\rho), Minkowski gives a primitive vector of (\Lambda) of length (\le m/\rho); projecting orthogonally to that vector and proceeding by induction gives covering radius (\le m^2/\rho). The vectors of length (\le3m^2/\rho) span the real space. For the hermitian lattice (L=E^n\cap g\widehat{\mathcal O}_E^n), unimodular, a non-zero vector has squared norm at least (f), by total positivity and integrality of (h(y,y)). Since (c_0\) belongs to the different, the Euclidean dual of ((2/c_0)L) is contained in (L). Taking (m=2fn), (\rho=1) and multiplying by (c_0/2) gives exactly (6c_0(fn)^2). No ineffective constant intervenes.

## Second critical review of the scope of (a) in 50

There are no hypotheses literally called (H1)–(Hn) in this version of the file. So that the verdict does not hide context, this is the reconstructed list of assumptions. The three inputs do not replace the structural conditions on the operator.

| Hypothesis | Source | How it enters or is checked |
|---|---|---|
| Valuation domain of characteristic 0, (p\) non-unit, (w^2=p) | 335–337 | Allows finite diagonalisation, cancellation, Kummer and reduction modulo powers of (w). Neither DVR nor noetherianity is assumed. |
| (W) local, residue field (\mathbb F_q) | 337 | Gives classes with unit differences and surjective reduction of (GL_k(W)). |
| (N\ge2) even, (e\ge1), (P=p^e\ge5), (q=P^N), cyclic homomorphisms (\iota_s) with congruence modulo (p) | 337–348 | It is a structural hypothesis, not a conclusion of root/count/av. It implies (\iota_s(\mathfrak m_W)\subseteq p\mathcal O), with the argument of the unit factor (1-y^{q-1}). |
| (k\ge2), (n\ge1), (0<2r\le k), (r) integer, alternating standard/dual representations | 350–358 | Used in depth, interlacing, counting and the parabolic block. |
| (X,H) finite, edge maps, representatives (t(\varkappa)^{-1}K_r=\varkappa), (u(e)\in GL_H(\mathcal O)) | 374–380 | Necessary in order to have two restrictions and to use (u(e)^{-1}) in the near-inverse. The cases of empty sets have empty/trivial conclusion. |
| Freeness `ph:eq-free` | 381–383 | Makes the parametrisation of inverted edges bijective. It is not deduced from the three inputs; it is verified separately in the automorphic application, 823–831. |
| (f\) linear, (Yf=fA), (\Lambda=f(\mathcal F_X)) | 401–403 | Allows the colength to be transferred from the abstract operator to the image module, which need not be free. |
| (0<\theta\le1), (n^4\le q), ((Nk\log q/\theta)^5P^{3r}\le n) | 397–400 | Implies all the additional numerical inequalities for the three inputs, as checked in 1505–1517. |
| `ph:root`, `ph:count`, `ph:av` and the inclusion `ph:AinC` | 661–703 | The three propositions are proved in §3; `ph:AinC` is also proved, in 1027–1051, using root. It is not a fourth unproved external input. |

I have checked again the places that usually introduce hidden hypotheses: the degree over the ring with nilpotents in root (the divisor is monic), the finite generation of (U^+) in the average (it comes from the finite algebra (\mathcal S_d), not from noetherianity), Nakayama in `ph:near` (finitely generated module), and the count of roundings of valuations in `ph:ends`. I have not obtained a concrete correction to (a) for the algebraic formulation in this context. The result applied to all the global data of 49 remains (c); the three inputs do not by themselves prove the edge freeness, the weak approximation or the arithmetic normalisation.
