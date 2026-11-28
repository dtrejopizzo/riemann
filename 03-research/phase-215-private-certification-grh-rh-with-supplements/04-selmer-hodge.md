# Specialised verdict: papers 55 and 56

Review date: 28 November 2026. Texts: `04-papers/55-covolume-theorem-regular-families-of-twists/main.tex` (8200 lines) and `04-papers/56-explicit-cup-exponents-local-galois-representations/main.tex` (8380 lines), local working copy. The line references refer to those files, abbreviated P55 and P56. 47 and 48 were not read.

## Update: the deep audit replaces the pending items of this initial report

The body below keeps the first review as a historical record. **Do not use its (c) verdicts for lack of reading as the current verdict.** The later reconstruction is in [HODGE](deep-review/HODGE.md) and [SELMER](deep-review/SELMER.md).

| Question | Current verdict and scope |
|---|---|
| P56: local bound, all ℓ and tame case | **(a)** under the printed hypotheses; HODGE §§1–6 reconstructs the integral and cohomological chain. |
| P56: NM | **(a)** as a sufficient condition; **it is not necessary**, by the example below. |
| P55: Selmer, Ribet modulo powers, local loss and odd classes | **(a)** for the obligations reconstructed in SELMER §§1–10,12–14, under their explicit inputs. No residual irreducibility is missing in Ribet. |
| P55: literally written proof of all the inputs | **(b)** in concrete sentences of §6 and §11.1 of SELMER; they are not counterexamples to the main theorem. There are local corrections of equal cost. |
| P55: base level and e_c | Discrepancy of formulation and obligation of preservation; SELMER §11.2 gives an explicit repair with the same bound. That repair is not presented as text already written. |
| Sum over all primes | **(a)** as arithmetic assembly; SELMER §14. |

The verdicts concerning the kernel, exchange and Rallis inputs are read together with the audits of P49/P53/P54. None of them certifies by itself the global deduction of GRH.

## Record of the first review

**Global result: (c), not verified in its entirety.** This review does not establish a counterexample to the main theorems of these two papers. Nor does it certify their complete proofs. It does check several reductions, discards an over-general objection about irreducibility and delimits the results that would remain to be verified independently. A reduction that is correct assuming its lemmas does not constitute a verdict (a) on the final theorem.

Two senses of "missing" are distinguished below: an argument absent from the manuscript and a check that this audit has not yet completed. In the points (c) that follow, the manuscript normally **does contain** proofs of the lemmas indicated; what is pending is to validate them, not their mere existence. This verdict is not attributed to any of the mathematicians mentioned by the author.

## Answers to the questions on P55

| Question | Verdict | Concrete pending step or result checked |
|---|---|---|
| Existence for every prime, `pg:I`, `pg:II`, `pg:III` | **(c)** | `pg:I` depends on the transfer and on the local check in `pga:G123`/`pga:G45`; `pg:II` on the descent `pse:step` and on the polynomials of L-values `pse:stick`; `pg:III` on the trace modules and the realisation by auxiliary operators. A check of all those proofs and of all the external theorems with their hypotheses has not been completed. |
| Step Selmer → congruences modulo powers of ℓ | **(c)** for the complete argument; **(a)** for the observation that the required irreducibility is explicit | `pri:ribet(1)` requires that the image of the block generate the whole matrix algebra. This hypothesis need not be added as if it were omitted. The whole construction of the determinants of linked rows and its automorphic realisation remain to be certified. |
| Local loss `pg:loss` | **(c)** | The reduction by duality can be checked; the numerical exponent depends on P56, `pki:crys`, and on the tame case. |
| Odd classes `pg:odd` | **(c)** | Neither the annihilator `pod:annih` nor the Euler descent that transforms annihilation into length with the declared constant has been certified. |
| Sum over all primes | **(a) as an arithmetic reduction conditional on the declared bounds**; **(c)** as an unconditional consequence of the series | The sum of the local term and the change of units from valuation to logarithm are well posed and are checked below. The bound for `C_odd` and the local bounds are not certified by that sum. |

### 1. Residual irreducibility is not a tacit hypothesis

P55, definition `pg:def-summand`, lines 563–585, requires in (M4) that for every sufficiently defined stable lattice the `u(g)` generate `M_n(O)`. The text explains its interpretation in lines 586–589. The exact version `pri:ribet`, lines 2565–2588, requires it again in (1), for the block `rho_pi`.

The lemma `pg:burnside`, lines 805–830, gives a pertinent and correct argument under its hypotheses:

1. The eigenvalues of inertia are distinct modulo the maximal ideal; the differences are units and the spectral projectors are integral.
2. The lattice decomposes into its eigenlines.
3. Frobenius permutes those lines in a complete cycle.
4. A subspace stable after any residual extension is a sum of eigenlines and stable under that cycle: it is zero or everything.
5. Burnside over the residue field and Nakayama over `O` give the integral generation of the matrix algebra.
6. `phi^n` preserves each line and commutes with the cycle, so it is scalar.

This check does not use that ℓ is large: it uses that ℓ is different from the residue characteristic of the auxiliary place and that the eigenvalues are incongruent. The strategy of two level primes, so as to be able to choose the other one when ℓ coincides with one of them, appears expressly in `pg:rem-primes`, lines 475–487. It remains to certify that **all** the automorphic systems used have the necessary labels and local types: that refers to `pga:G123`, `pga:G45` and to the selection of labels. It is not correct to replace that task by the assertion "Ribet needs irreducibility and here it is not assumed".

### 2. What was checked of the twist argument

The lemmas on roots of unity `pg:roots1` and `pg:roots`, lines 922–990, have a coherent mechanism: the evaluation valuation is compared with the Gauss valuation; the contribution of roots of the polynomial on circles of radius `rho_h` is counted; the average truncated by 1 produces a point with no loss greater than `delta`; the variables are specialised successively. In the reduction of powers `1≤j≤m`, choosing the root of greatest valuation of `(1+Y)^j-(1+x)` guarantees `v(Y)≥v(x)/j`, and does not presuppose `j` prime to ℓ. This aspect does cover small primes.

The lemma `pg:minor`, lines 1068–1100, explains why the maximal minors control the length of a kernel modulo `ℓ^M`. The formula `sum min(M,v(d_i))` and the passage to the group with coefficients `K/O` when the length is less than `M` are correct. The rest of the existence of the useful specialisation depends on the descent of Selmer groups: `pse:mirror` (1780–1840), `pse:step` (1872 and following), and on `pse:stick` (2051 and following). **That dependence has not been verified in full.** In particular, verifying the specialisation of polynomials is not enough to conclude the Selmer bound: one must first prove that there exists a point where the minors have the required valuation.

### 3. Local loss: reduction checked, exponent pending

P55 `pll:D2`, lines 3314–3358, does not limit itself to citing an integral form of Bloch–Kato: it writes a proof by lengths. Its steps are appropriate:

- The image of `H_f^1(T)` in `H^1(T/ℓ^m)` is `H_f^1(T)/ℓ^m`, because the preimage of a rational subspace is saturated.
- Its length is `m(h_f-h_0)+len H^0(T/ℓ^m)`.
- The tangent dimensions of a de Rham representation and of its Tate dual add up to `[F:Q_ℓ] rank(T)`.
- The local Euler characteristic and Tate duality give that the two orthogonal images have complementary lengths.

This supports `pll:dual` (3360–3394), without by itself converting a rational Bloch–Kato bound into the new integral bound of the paper.

The mechanism of `pll:ribet`, lines 3408–3446, is also checked. One takes `Y=⊕End(u_x)` with **left multiplication**, not with the action by conjugation. For that reason `Y` is a sum of copies of the original representations. The submodule generated by `(u_x(g)-1)_x` is stable, and the relations allow one to define the morphism to `T/ℓ^M`. The rational exactness of `D_cris` on the representations that become crystalline over a common extension shows that the cocycle in that submodule is crystalline. The choice of the left action is essential and is made correctly.

What is not certified is the new bound of `pll:exponent`, lines 3487–3507, taken from P56. The final classification of `pg:loss` remains (c).

### 4. Odd classes and ℓ=2

`pg:odd` (1373–1380), `pri:odd` (2313–2327) and `pod:odd` (4382–4404) have the same structure: for `e≠0` they concern cocycles anti-invariant under complex conjugation with cyclotomic local condition, and for `e=0` homomorphisms unramified everywhere. The second formulation makes explicit `chi^e = Z_ℓ(-e)` and that the coefficient ring contains the values of the Dirichlet characters.

The manuscript does not apply without explanation an Euler systems result valid only for odd ℓ. `pod:rem-two`, lines 4406–4416, separates the primes `ℓ≤(N+t+3)^2`, using annihilators and detecting points, from the larger ones, where it applies the descent. This answers the objection of formal coverage of ℓ=2, but does not prove the result: `pod:annih` (4879 and following), `pod:detect` (4511 and following), and the descent of the later sections must be verified. In this review those three steps are not certified. There is no counterexample established here.

### 5. The sum of losses, with all the units

P55 defines, lines 416–433,

`lambda_ℓ = v_ℓ((2b)! · (∏_{b-30h³<n≤b+30h³} n)^{h³})`,

`loc_ℓ = 4f·10^6 (m/k) (b v_ℓ(M)+lambda_ℓ)`.

For any finite set of primes `T`, the product formula applied to **a fixed positive integer** gives

`Σ_T lambda_ℓ log ℓ ≤ log((2b)!) + 60 h^6 log(b+30h³) ≤ 3b log b`,

with the size separations of the data. Likewise `Σ_T b v_ℓ(M)log ℓ ≤ b log M ≤22b log b`. Hence the factor `4·10^6·(3+22)=10^8` of `pg:sums` (520–522) is correct.

The contribution `2^{-ℓ}` is summable, and the terms that are valuations of `N_ch`, `C_odd` and `h_1` are summed as logarithms of those integers. In the end, the absorption of the local term into the budget reduces to

`2·10^8 m² ≤ x (log b)²`,

which is obtained from `m²≤4x` and `(log b)²≥8·10^8` (P55, 525–533). One must not sum the individual uniform bound without keeping the finite support or the factorial structure: that structure is precisely what allows the sum.

This computation is a verification of the **arithmetic reduction**, not of the prior existence of the integer `C_odd` with the required size.

## Answers to the questions on P56

| Question | Verdict | Scope |
|---|---|---|
| Main exponent without FL restriction, for every ℓ | **(c)** | The numerical deduction of `pki:crys` from its central propositions has been reviewed; not all the lemmas on lattices, frames and walks on which they depend are certified. |
| NM: necessary and sufficient | **(a)** for the identification of its role as a sufficient hypothesis in the reduction and for its arithmetic verification in the application; **(c)** for the complete generic proposition | The paper does not assert an "if and only if". NM is not necessary for the defect to vanish; an example is given below. |
| Potentially crystalline tame case | **(c)** | The passage of the exponents and the specialisation to the data fit; the certification of the tame killer `pkw:T3` and its inputs is pending. |
| Novelty | **(c)** | The fine form of the bound is a candidate for a contribution; neither priority nor validity is established by limited bibliographic comparison. |
| Consistency with FL | **Compatible in the subcases checked; (c) as a complete comparison of categories and local conditions** | The vanishing when `lambda=0` agrees with what is expected; P55 itself does not use FL as a substitute for its integral proof. |

### 6. The main assertion is more restricted than the abbreviated title

`pki:crys` (552–623) does not say that any pair of crystalline representations of arbitrary weights has the announced exponent. It requires (S1)–(S4), opposite windows, that the letters read thickness, and few low jumps or the alternative case `U'⊆[-eta,0]`. In particular, "every ℓ" does not eliminate the geometric hypotheses on the distribution of weights and embeddings.

The deduction distinguishes:

- `ℓ≤Q`: `pki:sparse` is used with `J=floor(log_ℓ h³)`, low radius `2G`, `vartheta=2K`, `M=K`.
- `ℓ>Q`, `lambda≥h³`: `pki:any` is used, and one obtains `b+delta<Kℓ²` and `2(G+delta)<Kℓ`.
- `ℓ>Q`, `lambda<h³`: `pki:generic` is used with `a=2(lambda+1)`.

In the last case the result is directly a **defect length**, not necessarily an exponent that kills each class with that same constant divided by the rank. P55 expressly keeps this distinction in `pll:exponent`. The illicit exchange "length per rank → uniform exponent" was not found here.

The complete check must still cover `pkf:main` (2868), the deepening theorems `pke:I2` (4829), `pkh:I4` (5793) and the scheme `pkd:scheme` (6882), with their dependencies. They are written proofs, but this audit has not certified each one. In particular, checking the inequalities 570–623 without checking those results does not verify the theorem.

### 7. NM: what it means and where it is used

The definition of NM in P56, 380–382, excludes **non-zero** multiples of ℓ in three intervals around `0`, `b_z` and `-b_z`, of radius `n`. The lemma `pkc:free`, 6310–6321, uses exactly that exclusion so that the costs of the level-zero steps are zero in an unramified chart. The conventional value of the cost function at `y=0` is zero; it is not being asserted that the ordinary valuation of 0 is zero.

In the application `lambda<h³`, lines 600–607:

1. If ℓ divided an integer in `(b-30h³,b+30h³]`, the power `h³` of that factor would force `lambda≥h³`.
2. With `a=2(lambda+1)` one has `n=6(a+eta+W)<13h³`.
3. Every non-zero multiple of ℓ has absolute value at least `ℓ>198G`, so it lies outside the low interval and the intervals around `±(G+delta)`.
4. The intervals around `±(b+delta)` lie inside the enlarged factorial interval above, because `delta+n<30h³`.

Thus NM is checked in **both** classes of letters, thick and thin; it is not presupposed without control for `G`.

NM is not necessary for the conclusion of zero defect. An example of positive rank: `F=Q_23`, `U=U'={0}`, `L=Z_23` trivial, `a=2`, `eta=1`, `W=0`, `b_z=20` in all the letters. Here `e=f=1`, `ℓ≥5`, `eta≥1`, the two windows contain 0 and there are no jumps in `[-a,0)=[-2,0)`. One has `b+W+eta=21≤(23-3)·2=40` and `6(a+eta+W)=18<20`. NM fails because `y=23` is non-zero, divisible by 23 and at distance 3 from 20. Thus all the other hypotheses of `pki:generic(i)` are satisfied. The crystalline representations with all their weights zero are unramified, and so are their lattices. For any equivariant pairing modulo `23^m` between those lattices and `L`, choose an inertia element `g` whose cyclotomic character is `-1` modulo 23. Equivariance gives `(epsilon(g)-1)b_psi(y,l)=0`; the factor is a unit, so the pairing to `Z/23^m(1)` is zero. Consequently the defect here is zero, although NM fails. This example refutes **the interpretation of NM as a necessary condition**, not the one-sided statement of `pki:generic`.

### 8. Tame case and Tate dual

P56 `pki:tame` (464–474) and its repetition `pkc:tame` (6629–6638) impose `F=Q_ℓ`, `e_0=lcm_{1≤i≤r}(ℓ^i-1)`, uniform polynomials `K(s)` and the membership of the dual in the class with `K^{-1}(s)=K(s^{-1})`. The inequality `ℓ>b+6(W+eta)+r²(N+1)²+2` is part of the hypothesis.

The deduction of 6643–6681 keeps the costs: `e_0≤ℓ^{r²}`, a polynomial of degree `≤N²` for the dual tensor, `kappa=r²(N+1)²`, and a total walk cost bounded by `3kappa+150(eta+W+1)`. The choice of `K^{-1}` is important: applying the same polynomial directly to the dual without inverting inertia would be incorrect. The text does make the inversion.

The application to P55, `pkd:data(iv)`, 7224–7281, uses `N=(r+t)r=6r²`, `eta=h²+1`, `W=4t`, `delta_j=j Delta+h-2t` and `p_i≥b^{10}`. The required bound is less than `2b`, so the separation `p_i≥b^{10}` gives the range. `L_c^*∈C(U',K^{-1})` is also made explicit; no omission of this hypothesis has been found in the junction.

The uncertified part is the proof of `pkw:T3`, lines 7753 and following, which obtains the integral annihilation of the cokernel from inertia and from the monic polynomial, together with the preparation of the tame charts. The arithmetic of the exponent, even if conditionally correct, does not replace that proof.

## Junctions: identity of the input versus proof of the input

| Junction | Identity/range checked | Validity of the input |
|---|---|---|
| P46 `au:regular` → P55 `pg:main` + `pg:sums` | Yes, in the reduction of P55 535–545. R1 comes from (a); R2 uses the inverse quotient and `|·|_iota=ℓ^{-v}`; R3 uses `beta(ℓ)=(beta_ℓ+v_ℓ(h_1))log ℓ`. `log ℓ` is not omitted. | (c), because of the dependencies of `pg:main` and `pg:odd`. |
| P46 R3(i),(ii) → P55 `pg:def-den`, `pg:main(c),(d)` | The false lifts are defined place by place and orthogonality is asked for at all those places. The contribution `h_1` is added to the bound of principal pairs. P46 4895–4912 and P55 394–411, 438–458, 460–473. | Coherent reduction; the whole construction of the operator remains to be certified. |
| P55 `pg:loss` → `pll:main` → `pll:exponent` | The first bound is by dual defect of `L_c^*`, not of `L_c`; the factor `[E_v:Q_ℓ]` and `x_main=1`, `x_e=t` are present. | (c), exponent coming from P56. |
| P55 `pll:exponent(a–d)` → P56 proof after `pki:crys` | The exponents `10^4 floor(2lambda/Q)(floor(log_ℓ h³)+1)`, `10^4 floor(2lambda/Q)m`, the tame case and the caveat of length without exponent coincide. P55 3487–3507; P56 624–636. | (c) for the central theorems. |
| P55 (M2) → P56 `pkd:data(i–iii)` | Correct algebraic check: the dual has jumps `-u-1`; `delta_j=jDelta+h-2t`, width `4t`, radius `h²+1` contain the jumps and the low multiplicity bound is kept. | Conditional on the representations of P55 actually satisfying (M2). |
| P55 tame types → P56 `pkd:data(iv)` → `pki:tame` | `N=6r²`, the uniform polynomials and the inversion `K^{-1}` coincide. The range in `p_i` suffices. | (c), tame killer and automorphic origin of types pending. |
| P56 generic → application of `pki:crys(d)` | NM is derived from `lambda<h³`, with independent control of the letters of weight G. | (a) for the verification of hypotheses and the inequalities; (c) for the whole proof of `pki:generic`. |
| P55 → P54, input (IM) for L-values | P55 explicitly points to P54 §3.1, and `pse:stick` is the point that uses it. This review does not certify (IM) nor its normalisation; it belongs to the specialised audit of P54. | (c). |

The dependence P55↔P56 **does not by itself show a logical circularity**: P56 imports definitions, the elementary bound rank→defect and properties of representations from P55; it returns the local exponent. To denounce a cycle one must exhibit that one of those inputs of P55 depends on the exponent, not only that the two papers cite each other.

## Novelty and limited bibliographic comparison

The candidate contribution of P56 is the sensitivity of an **integral bound for the compatibility defect modulo ℓ^m** to the distribution of weights and to the scarcity of thick letters, instead of only to the largest weight. P55 explains why this matters to it: it wants a saving proportional to `m/k` after summing over places and primes. That connection with a global budget of denominators is an identifiable idea, although its complete mathematical validity remains pending.

It is not new, in itself, to study crystalline lattices outside the Fontaine–Laffaille range nor torsion representations for ℓ=2. Pertinent primary sources:

- Fontaine–Laffaille, *Construction de représentations p-adiques* (1982), [original text](https://www.numdam.org/item/10.24033/asens.1437.pdf).
- Tong Liu, *Torsion p-adic Galois representations and a conjecture of Fontaine* (2007), [publication](https://www.numdam.org/item/?id=ASENS_2007_4_40_4_633_0).
- Tong Liu, *A note on lattices in semi-stable representations*, [preprint](https://arxiv.org/abs/0709.4523).
- Caruso–Liu, *Some bounds for ramification of p^n-torsion semi-stable representations*, [preprint](https://arxiv.org/abs/0805.4227), [authors' text](https://www.math.purdue.edu/~tongliu/pub/bound2.pdf).
- *Torsion representations arising from (phi, G-hat)-modules*, [preprint](https://arxiv.org/abs/1202.1858), whose scope includes p=2.

Those references do not automatically verify the exponent of this manuscript. Nor does the absence of an identical bound in a limited search demonstrate priority. The exact comparison requires identifying torsion categories, maps and local conditions, and then deriving or excluding an equivalent bound. P55 `pll:FL`, 3467–3479, acknowledges that it does not use the Fontaine–Laffaille route as a substitute. In the range where `lambda=0`, the conclusion of vanishing agrees with the expectation of integral exactness, without that certifying the cases of large weights.

## Scope of the Lean records

Only the README of `06-alpoge-verification` was inspected. It contains declarations of compilation and of axioms, and expressly distinguishes compilation from mathematical review. The compilation was not repeated, the whole Lean file was not inspected, nor was a declaration-by-declaration correspondence with P55/P56 established. Hence that README is not used to change any of the (c) verdicts above to (a).

## Priority checks to close this verdict

1. Certify `pkw:T3`, `pke:I2`, `pkh:I4` and `pkd:scheme`, including integrality, constants and compatibility of the lattices defined by orders.
2. Certify the automorphic transfer and the local types of `pga:G123`/`pga:G45`, checking the exact hypotheses of the results cited.
3. Certify `pse:step` and the input of P54 in `pse:stick`, not only the lemma of specialisation at roots of unity.
4. Certify `pod:annih`, the number of detecting points and the Euler descent with its dependence on ℓ=2.
5. Only after those verifications, raise the correct final accounting of losses to a verdict on the existence of regular families for all admissible data.
