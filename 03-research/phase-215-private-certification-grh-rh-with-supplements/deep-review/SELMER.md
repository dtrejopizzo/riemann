# Deep audit of P55: Selmer and Ribet

Date: 2026-11-28. Source of lines: `04-papers/55-covolume-theorem-regular-families-of-twists/main.tex`. This record continues `04-selmer-hodge.md`. The paper was not modified.

## Current status after the passes

The pending items of the first tables were traced in §§6–14: G123/G45, Selmer and Ribet, odd classes, local loss, Fitting, norm, spherical chain, Higman and sums. **No omitted residual hypothesis is detected in Ribet.** There are literal errors (b) in the sentences on roots/generator of §6 and in the fixed polynomial for every element of inertia of §11.1. The corrections are explained there and do not change the bounds. The base level/e_c convention requires clarification and an explicit construction that preserves e_c; §11.2 provides a repair with the same N_ch, separate from the written construction. For this reason an indiscriminate (a) is not issued for the paper as it is written. The reconstructed arguments are graded individually, with their inputs from P49/P53/P54 and the data of P46.

## Obligations resolved in this pass

| Obligation | Verdict | Dependencies and scope |
|---|---|---|
| `pg:burnside`, 805–830 | **(a)** | Gives integral matrix image for each lattice, from the printed local hypotheses. |
| `pri:ribet-poly`, 2498; `pri:ribet-elt`, 2518 | **(a)** | The construction by Cayley–Hamilton is integral and works over O/p for p a non-unit, without the hypothesis p prime. |
| Main block of `pri:ribet`, 2605–2619 | **(a)** | Uses exactly the image M_r(O) of (1); the extraction of a block matrix is justified by means of matrix units. |
| Characters and gluing of `pri:ribet`, development 7199–7425 | **(a)** | Tied rows, common unit rows, separation with cost C, Fitting and extraction of the coefficient were reconstructed. What remains as an input is the triangular bound (7), not an unprinted residual separation hypothesis. |
| `pll:ribet`, 3408–3446 | **(a)** | Every class that obeys the relations comes from a crystalline class of a sublattice of a sum of the u_x. It does not require irreducibility. |
| `pse:A`, approx. 1600–1658 | **(a)** | Construction by ideles/Kummer/Chebotarev, also for ℓ=2. |
| `pse:restrict`, `pse:span`, `pse:mirror`, 1720–1843 | **(a)** | The strong condition ζ_*²−1 a unit is in the definition of Selmer datum, 995; ζ_*−1 is not enough. There is no division by 2. |
| `pse:tilting` and `pse:step`, 1847–1915 | **(a)** | The slope avoids at most 2n_i e+1 residues, simultaneously for all the powers of the uniformiser. |
| `pg:poly`, 1195–1255, Selmer assembly | **(a), under the local inputs already identified** | The descent uses non-normalised length to terminate, and then recovers the normalised length. The bound does not lose a ramification factor of the coefficient ring. |

This does **not** yet **certify pg:I, pg:II and pg:III in full**. The pending obligations are listed at the end; they are not accusations of falsity.

## 1. Where irreducibility is used, and why it holds to powers

In `pg:burnside`, the differences of eigenvalues of the inertia are units. The spectral projectors are therefore integral polynomials in u(s): the lattice, and not only the rational space, decomposes into lines. Frobenius permutes them transitively. After every extension of the residue field, a subrepresentation stable under s is a sum of those lines; transitivity forces it to be zero or everything. Burnside over the residue field and Nakayama in the finite module M_n(O) give the integral equality

`span_O{u(g)}=M_n(O)`.

That equality is not inferred from a mere irreducibility in characteristic zero. `pg:cyclic` verifies that the condition on eigenvalues survives removing the ℓ-primary part of the roots: since r is a power of 3 and p≡1 mod 3, a collision would force `x²+x+1` to be a power of a single prime; its valuation at 3 is exactly 1 and the number is >3, a contradiction. For ℓ equal to one of the primes of the level the other one is used. The check of the automorphic input that identifies those eigenvalues is a distinct obligation, `pga:G45`.

The integral equality implies its reduction modulo every power of the uniformiser. In the Ribet block, let d=r′ and m=#gen. The block rows evaluated at ρ_π form a module stable under left multiplication by M_d(O). Let L⊂O^(dm) be the module of the scalar rows that appear. By means of E_ij one isolates a row and places it in any position: every matrix with d rows in L is obtained from a tied block row. One chooses a basis of L by Smith, groups its dm rows into m blocks of d rows and obtains the matrix B₀ used by the paper. The length of the quotient O^(dm)/L is that of the dual annihilated in (K/O)^(dm), ≤b_ρ. Its determinant has exactly that valuation. There is no need to multiply b_ρ by d nor to suppose that a chosen rational lattice is canonical.

The normalisation by γ_π is valid because ρ_π(γ_π)=ζ_π I and ζ_π−1 is a unit. The normalising rows force the cocycle to vanish at γ_π. The existence of this scalar also implies that the matrices ρ_π(g)−1 generate M_d(O): from `(γ_π−1)g=(γ_π g−1)−(g−1)` one recovers all the matrices ρ_π(g).

## 2. Integral Ribet: construction and characters

`pri:ribet-poly` works in a module over Λ[X] where X acts by **right multiplication by ρ₀**. This commutes with the left action of Λ; it does not require ρ₀ to be central. The ideal used there is two-sided. The ideal initially tied is only a left ideal, but `pri:ribet-elt` passes to the ideal of vanishing of all the traces, which is two-sided by cyclicity of the trace. This is the justification needed for the use of Cayley–Hamilton. Amitsur keeps integral coefficients and avoids dividing by factorials.

In the characters, forgetting the coordinates δ_v forces c(δ_v)=0 by the rows of generators. It is not a conclusion obtained by dividing by o_v(1). Those factors enter afterwards in the determinant of the rows of δ_v.

The simultaneous construction `prm:unit` does not divide by the differences of characters either. If w serves for the characters of E′, and m_j gives the unit rows for the new character, one replaces

`w → w+Σ_j(δ_ij−w_j)m_j`.

On the previous characters the added coefficients are zero; on the new one they correct the row to the unit. This induction is valid even when the characters are congruent modulo ℓ.

To separate afterwards the rows of the characters the q_e are indeed used, with values C on the character e and zero on the others. They are constructed because the product of differences **divides C**; it is not asserted that those differences are units. In the final matrix the rows of s carry CB_e, and those of δ_v carry o_v(1). Thus there appears exactly

`c_ch=C^(#s) Π_v o_v(1)`.

The quotient by the ideal of monomials not dividing X_J controls all the lower terms. `prm:coeff` proves by telescoping that an error ζ_e∈(n:X_<e), multiplied by the previous factors, is already in n. Therefore the coefficient of X_J is the product of the constants Γ_e(0), with the indicated factors of B₀, C and c_ch. There is no invalid inference from a single specialisation of the parameters.

The passage to K/O of `pri:divisible` uses that the relations make a cocycle determined by a finite number of values. Each cocycle then has finite order bounded by that of those values. If a torsion module has its p^M-torsion of length ≤b for a power of valuation >b, it cannot contain an element of greater order: a multiple would produce a cyclic submodule of length >b inside that torsion. This justifies the passage to the limit without presupposing finiteness of the divisible group.

## 3. The local step does not change the category of lattices

In `pll:ribet`, Y=⊕End_O(u_x) carries the action **by left multiplication**. Hence Y is a sum of copies of the u_x and belongs to C. With action by conjugation this assertion would be false; the text does not use conjugation.

The submodule S generated by `a(g)=(u_x(g)−1)_x` is stable since `g a(h)=a(gh)−a(g)`. It is finite free over the DVR. The relations of z define an equivariant map S→T/ℓ^M. It remains to check that a, viewed with values in S, is crystalline; it is not enough that it be a coboundary in Y. The paper proves it: the class of 1 in (Y/S)_Q is invariant, and the exactness of D_cris over a common extension E′ allows it to be lifted to an invariant section in B_cris⊗Y. The average over Γ/Γ′ is taken **in Qℓ-vector spaces**, where the index is invertible, even if ℓ divides it. Subtracting that section from 1 gives a period in B_cris⊗S that trivialises a. S is not divided by the index and no false integral section is promised.

This certifies the mechanism that connects the relations of Ribet with the class C_v. The numerical bound of the defect still depends on the cup-product result of P56, whose cohomological obligation was closed in sections 5–6 of `HODGE.md`.

## 4. Twists: small powers and ℓ=2

In `pse:A`, one chooses T that generates the class group and is disjoint from the prescribed inertias. The Kummer extensions by ℓ^N-th roots of T-units are unramified at those inertias. Chebotarev gives a prime of rational norm q≡1 mod ℓ^N where all those units are ℓ^N-th powers. The local character extends to ideles because it kills precisely the T-units. Antisymmetrising `θ(y/ȳ)` does not require dividing by 2: at distinct P and P̄ the normalised inertia still has value 1. Adjusting Frobenius by a power of that inertia makes λ(φ)=0 without leaving the prescribed open set.

`pse:mirror` uses ζ_*²−1 a unit to deduce Ψ=0 from the antisymmetry and the conjugation by γ_*. This is the substitute for a division by 2 and works at ℓ=2. The condition appears explicitly at 995, and (M5) implies that both ζ_*−1 and ζ_*²−1 are units. With M_n(O) one proves that the values of a primitive cocycle generate the whole of T/a, also when a is a small power; the proof uses matrix units, not only a rational argument. The restriction to the subgroup U is injective by Sah, with a scalar whose difference from 1 is a unit.

In `pse:tilting`, the auxiliary matrix acts on a free preimage of rank m of the finite module of values. The bad set consists of the residual roots of its monic characteristic polynomial: at most m. In the descent, m=2n_i; avoiding the union for all the exponents 1,…,e and the residue zero gives the printed threshold `#k>2n_i e+1`. Enlarging the residue field is a permitted unramified extension and does not increase the normalised lengths. The termination, by contrast, counts whole non-normalised length, as 1210–1213 explicitly clarifies.

## 5. Obligations still open for pg:I/II/III in full

They are not replaced by the phrase “too broad”. The following concrete steps require closure:

1. **pg:I:** verify `pga:G123` and `pga:G45` against the primary theorems in the printed normalisations, including the Speh constituents and absence of monodromy at the chosen level; then `pga:trace` and `pga:weights` for the normalising twist. The argument `pg:I` from G1–G4/L was read and the deductions of M4 and the formula for the Selmer constant were reconstructed. It was checked that χ=ε_ℓ⁻¹ (332): confusing the two would produce a false error in the exponent t′ of `pg:beta`.
2. **pg:II(c):** the integral input (IM), 1925–1940, must coincide and be proved in P54 for the absolute values and Euler factors written. The Selmer existence (IIa,b) does not by itself prove the bound of L-values. It remains to verify `pse:stick` from IM and the common choice of roots for all the systems.
3. **pg:III:** the triangular hypothesis (7) of `pri:ribet` must be certified by means of `pri:fitt-triangle`, the odd modules `pod:odd`, the Kummer triangle `pku:triangle` and its finite detector. The theorem of Ribet does not by itself eliminate these inputs.
4. **pg:III → denominators:** reconstruct `pri:norm` and its development `prm:normb`, and verify the exact identity of the level operator with the integral pairing, including stabilisers. Proving an element of the algebra of traces is not enough for this automorphic application.
5. **Local loss:** the SCC/cup product obligation of P56 was closed in HODGE §§5–6. It remains to check the final sum of defects for all the summands, without replacing a length by an exponent. The local step `pll:ribet` and the integral duality no longer remain as generic pending items.


## 6. New pass: level types, normalisations and two false but repairable sentences

Full reading of `pga:G123`, `pga:depth0`, `pga:parahoric`, `pga:G45` (3677–3986), `pga:trace`, `pga:weights` (4217–4284), `pax:sign` and `pax:conv` (6594–6665). The application of Moy–Prasad 6.7 to the pro-unipotent radical of the parahoric is really an assertion of isomorphism on invariants for admissible representations; it must not be confused with only the surjectivity of a Jacquet map for an arbitrary compact. The primary source is [Moy–Prasad, Jacquet functors and unrefined minimal K-types, pp.115–117](https://www.e-periodica.ch/cntmng?pid=com-001%3A1996%3A71%3A%3A10). In the passage of characters by blocks, ψ≠1 separates the inertial supports; the only component of the Jacquet module with the whole ψ support in the first block is Π₁⊗Π₂. This justifies concluding that the factors are spherical after the twist and that N=0. N=0 is not inferred only from the inertia being semisimple.

The choice of s in `pax:sign` gives an integer exponent: substituting s≡(N−1−n+m)/2 mod1 into e=(m−1)/2−a−s+(N−n)/2 one obtains e≡0 mod1. The infinitesimal entries of σ are in Z+(n−m)/2, and after the twist in Z+(N−1)/2. The polarisation can be changed by δ(E/E⁺), which is trivial on restriction via the norm; it does not change the Galois representation over E. In G1 the equality of exponents of q is exactly −s+(N−1)/2−e=(n−m)/2+a. In `trace`, n=r+t is even and qᵗ/β=q^((t−r)/2)(μ⁰θ)⁻¹. In `weights`, the shift is (t−r)/2, not its opposite, because χ is the inverse of the cyclotomic character. The arithmetic verification of the high/low weights and of the number of negative ones closes M2, conditional on the published theorems of existence and compatibility and on the theta input (L).

### 6.1 G4: norm of finite fields not defined in general — (b) for that justification

First incorrect sentence: lines 3946–3949, “since the norm F_{q^n}^×→F_{q^d}^× is surjective”, with d=lcm(d_k). A squarefree label of degree n can have factors of degrees 2 and 3: n=5,d=6. There is no inclusion F_{q^6}⊂F_{q^5}, nor that norm. In rank a power of 3 it also occurs: n=9, degrees 2 and 7, d=14. P46 3661–3673 permits these labels; it only requires that at least one place above each p have a primitive label, not that all have one.

**Scope and precise repair:** the statement calls s a generator of the tame inertia. If this means a topological generator of its pro-prime-to-p quotient, θ_d(s) is a generator of F_{q^d}^× by definition of the quotient, without recourse to θ_n. Compatible fractional uniformisers are chosen; for d_k|d, the power (q^d−1)/(q^{d_k}−1) of θ_d(s) is θ_{d_k}(s), and the Green parametrisation uses these same projections and the same ω. It suffices to delete the non-existent norm and use d, as `depth0` already does. If one required only that θ_n(s) be a generator, that condition would indeed be insufficient: q=13,n=3,d=2 and the seventh power of a tame generator keeps θ₃ a generator, but loses the factor 7 of the order of θ₂. That seventh power is not a tame topological generator, and so it is not a counterexample to the statement with the stronger condition. It is not asserted here that the substantive G4 is false.

### 6.2 M3: order of the roots — (b) for line 883, with a repair at no cost

Line 883 asserts that at every chosen place the rescaled roots have order dividing p_i^r−1. This is deduced only for factors whose degrees divide r; not for the general labels of P46. A primitive factor of degree 2, in odd rank r, has order p²−1 which does not divide pʳ−1. Multiplying it by z∈F_p^× does not eliminate the component of order outside p−1. It can be accompanied by an irreducible factor of degree r−2 and satisfy the exclusion of roots in F_p; at other places the primitive labels required by good are chosen.

The bound M3 written afterwards **is indeed recovered**: a root of a factor of degree d_k≤r has order dividing p_i^{d_k}−1 (the rescaling by F_p^× preserves this). If vℓ(ω−1)>0, its order is a power of ℓ and ℓ divides p_i^{d_k}−1, which divides #GL_{rt}(F_{p_i}), and therefore N_ch. There follow vℓ(ω−1)≤1/(ℓ−1)≤1 and vℓ(det(R(γ)−1))≤r·vℓ(N_ch), exactly the printed constant. The Burnside/M4 step uses a primitive place, where d_k=r, and does not have this defect. Nor does the argument M5 change, which uses that same primitive place. They are errors of proof *as written*, repairable by available elementary arguments; not a refutation of pg:I, III or GRH.

## 7. Closure of the odd module: `pod:odd` — (a), under the printed definitions

The complete chain 4382–5258 was reconstructed, including the detector, the components, the Voronoi congruence, the Gauss sums, the annihilator and the descent for large ℓ. Neither residual irreducibility nor a main conjecture is used. The points that need to be checked for the proof really to cover ℓ=2 and ramified coefficients are these:

- `pod:cft`: U_S^(M) requires nothing outside S, and so its index is indeed finite. The local formula is M·#μ_M(K_v)·|M|_v⁻¹. On then imposing units outside S and principal ideles, the factor h_K appears in addition. The detector uses K=Q(μ_{Nℓ²}); the induction on the exponent first kills Mz and converts the restriction to G_K into a homomorphism. Thus the same points serve for every ν, not only a fixed ν. The size M≤y⁵ gives ≤y²⁰ points.
- `pod:split`: the transfer employs b(u,g)=u[c,g]u⁻¹ and not idempotents divided by φ(N). The sum of characters equals φ(N) on the trivial coset; comparing h and chc introduces the factor 4. Hence passing from the odd components to the original class only requires multiplying by 4φ(N), even at ℓ=2.
- `pod:X`: the convolution matrix T has eigenvalues 2Σχβ for the odd parity, and 2(−1)^e for the other. The former do not vanish, by the functional equation at −e (e≥1, also for imprimitive characters). The adjugate proves divisibility in the ring of values, without inverting the eigenvalue. The two integers 1+N and 1+2N ensure (S1) for each prime. The Voronoi congruence comes from expanding modulo (Nm)² and dividing an identity in a torsion-free ring; it does not divide in O/ℓ^ν. The choice of w in (S2) is independent of m, a fact necessary for the subtraction in `thetadiv`.
- weak `pod:stick`: the Gauss ratio G(a+b)/(G(a)G(b)) is fixed by inertia, so that its valuation is an integer. For t≠0 both G(t) and p/G(t) have positive valuation, so that the valuation is strictly between 0 and 1. This proves that S is injective and allows the exponent m_c(x) to be parametrised exactly, without invoking a stronger Stickelberger congruence that is not cited.
- `pod:J`: the distribution quotient has valuation zero at all the primes above p by the Hermite identity, is a unit away from p and has all archimedean norms equal to 1; Kronecker gives a root of unity. The congruence J6 results from reducing characters of order q modulo a prime above q. It does not require q to be large.
- `pod:artin` and `annih`: the factors 2(a^e−1) kill respectively the real contribution and the contribution above ℓ. For the annihilator one takes z′=2X²z; if 4X²z≠0, Sah forces a Frobenius that detects z′. The family J and the divisibility `thetadiv` contradict its non-vanishing. One obtains 4X², without dividing by 2 or by a^e−1. In `thetadiv`, 1−ℓ^eψ(ℓ) is a unit, and e≥1 justifies transferring the congruence from level n−1 to level n.
- `pod:KS`: the roots y(x) are arbitrary but the quotient F_g is in μ_{ℓ^n}. The changes of shifts disappear by distribution; this makes Λ_S(F_g) satisfy the cocycle rule with exponent e+1. For KS3, the inertia identity compares W₁ and W_{γ⁻¹}; both are roots of unity that reduce to 1 at the appropriate place, and their quotient belongs to μ_{ℓ^n}. Since q≠ℓ, that quotient is exactly 1. A q-primary root of unity is not erroneously identified with 1 before the ℓ-primary quotient is formed.
- `pod:recl` admits ramified O: V=Oκ(τ), killed by ℓ, is taken as an F_ℓ-vector space. The coordinates used for Hilbert 90 are not presupposed O-linear. The final sum is in mV because each coefficient s_i kills a non-zero element and hence belongs to the maximal ideal m. φ(Nℓ)−t is a unit and forces κ(τ)=0.
- `pod:koly`: if m=vℓ(X)+1 detectors are missing, each set of ≤m primes admits a non-zero class of ℓ-torsion trivial there. The descending induction on i preserves tightness and produces an unramified ℓ^iκ_S; KS3 contradicts the choice of a Frobenius that detects ℓ^{i+1}κ_S. At the end θ=0 modulo ℓ^m contradicts vℓ(X)=m−1. The contradiction remains valid for ramified O, since ℓ^{m−1}X′∈ℓ^mO would imply X′∈ℓO, X′ being a unit.

For ℓ≤y² only the annihilator and the uniform detector are used; the descent that divides by residual units is reserved for ℓ>y²>N+e+3. The product c_odd=(Π_{0<e<t}16φ(N)X_e²)^{y²⁰}h_E has the announced length and size. The substitution of data N≤x¹⁵, r≈x⁵ gives log c_odd≤x⁴⁰⁷≤x⁸⁰⁰. This closes `pg:odd` and its contribution to the global sum; it does not yet close the triangle of even classes nor the norm operator.

## 8. Closure of the even triangle and of `pku:main` — (a) from standard finite duality

Lines 5297–5818 were read and reconstructed. The external inputs are local duality, global reciprocity and Greenberg–Wiles for finite modules, expressed as D1–D4; not an assertion of existence of classes special to the problem.

The modification ε⁺=ε·η of the cyclotomic character is trivial on all complex conjugations. At ℓ=2 its image falls in 1+4Z₂ because μ₄⊂E. This permits the pro-cyclic generator used in the local terms above ℓ. The quotient G_F/G_ν has ℓ-Sylow generated by ≤2 elements, also at ℓ=2; it is not falsely asserted that it is always cyclic.

The Kummer relations are obtained by restricting dual classes to G_ν and extending by zero outside it. It is not promised that that extension is a global cocycle: the definition of relation only asks for additivity on G_ν and the conjugation law. The reciprocity with the test cocycles is derived from the exact local annihilators in S₀; choosing T=S₀ avoids uncontrolled extra terms.

In `pku:torsion` the primes that detect all the non-zero dual residual classes on G_ν are selected by Chebotarev. There remain at most ℓ² classes inflated from G_F/G_ν. Greenberg–Wiles, with **ordinary H⁰** at the real places, contributes ℓ⁻¹ at each of the r_F real places and of the k fixed primes, ≤1 above ℓ and ℓ at each relaxed prime. It gives ℓ^(#P−k−r_F+3) for M[ℓ]. The passage to H¹(M)[ℓ] adds only a factor ℓ: the image in H¹(M/M[ℓ]) comes from the boundary of H⁰(M/ℓM). In the kernel, the lift to M[ℓ] preserves the conditions because the H_v act trivially and M[ℓ]→M is injective; here it would be incorrect to use only exactness of cohomology without verifying the local conditions.

The dual image in (M^∨)^P is exactly the annihilator B^⊥: reciprocity gives inclusion and the ratio of two Greenberg–Wiles formulas gives equality of sizes. On restricting to X=M[ℓ]^P, one obtains #r(B^⊥)=ℓ^#P/#B[ℓ]≥ℓ^(k+r_F−4). That restriction depends only on the reductions of the Kummer maps; hence there are at least k+r_F−4 independent reductions, not merely abstract dual classes. Since r_F≥576, one lies outside any family of k previous maps.

`pku:triangle` uses those maps for equal exponents e, then the separating polynomial Π_{k≠e}(conj_a·power(ε(a)⁻¹)−ε(a)^k). On the additive values this kills all the different exponents without dividing by their differences; the product of differences divides the budgeted power ℓ^((t′−1)h₀). The antisymmetrisation in u introduces 2, and the passage of the test cocycle from E to F introduces another 2. The exact loss is 4Π(ε(a)^e−ε(a)^k), which divides ℓ^(hh₀). For large ℓ, h₀=0 because all those factors and 4 are units. For small ℓ the detector of §7 has ≤h²⁰ points and gives the cost h²²h₀. No false uniform bound is used for the number of detectors when ℓ>h².

The test cocycle 2z⁺ over F vanishes at the real places and on D_v∩ker ε⁺ at ℓ because its value is that of z⁺(g²), with g²∈G_E. The reciprocity of κ_j leaves only the term j: the earlier ones vanish by the hypotheses on z, the later ones by the conditions imposed on the Frobenius elements when they are chosen. Thus the triangular property (iii) is proved for every O/ℓ^ν, passing to additive coordinates Z/ℓ^ν that separate points, without supposing O unramified. This closure together with §7 eliminates the even/odd obligations of the triangular hypothesis of Ribet; it remains to verify the Fitting algebra and the norm operator.

## 9. Fitting algebra and deformed norm

**Fitting 2393–2471: (a).** The duality over O/p separates points of the finite-length module Oⁿ/Φ⁻¹N. In `fitt-cost`, the quotient of duals by the preimage of W is exactly F(N)/(F(N)∩W), even if z does not generate Oⁿ. A composition series of the annihilator gives a factor π per row added. The identity a·Fitt(N+Rv)⊂Fitt(N) comes from multilinearity and from the vanishing of terms with two rows proportional to v, not from a supposed inclusion of ideals without a factor. In the triangle, each step costs CX_j; at the end one passes to X=0 only after adding mR^s. One recovers d∈Fitt(T) with d(0)=fC^#s. The bound b+(#I+#s)v(C) and the coefficient X_I are exact.

**Induction of the norm 7434–7505: (a), under `oneplace` and the printed Higman operator.** It is important to maintain the assertion for all S and all i≥#S. For each j∈S one uses S\{j}; only then is invariance proved under each factor Γ_j, and therefore under Γ. The identity Σk⁻¹Ψk=c₀ converts that right invariance into a factorisation through Nm. It is not necessary that Ψ or the operators Y_S commute with the Hecke algebra; only the N_S and δ′ do so, and those are the only changes of order used.

**`pri:norm` 2977–3052: (a) from `oneplace`.** The relation t₀−X_jr₀ is killed by pairing the coefficients of S and S∪{j}; Nm_jt₀=0 and ∂_jt₀≡Nm_jr₀. In the consequence it is applied to u=Ψ(d₁l), whose norm is c₀d₁l. All the coefficients except the top one vanish by the hypothesis d_Sy=0. The error is a multiple of ℓ^ν/(2n!), and the divisibility required by (n₀c₀²)^(#J+1) allows that factor to be cancelled without concluding integrality from an unjustified rational congruence.

**`oneplace` 2901–2975: algebra reconstructed; exact pending item in the local dictionary.** The transfer of the coordinate k₁₁ of the stabiliser of a line is det: for each coefficient of the sum Tr L(λ)Tr′ there appear the logs of the factors of the permutation of cosets. The shift of λ produces −Nm_j. For the third property, B(1) has K₁-invariant image; inserting Higman gives c₀B(1)=L(1)ΨB(1). The vanishing δ′NmZ=0 is obtained first in characteristic zero; dividing by #K₁ there does not introduce a division in the lattice. It remains to close the input `pri:dict(b,d)`, concretely `pax:Ueig` and `pax:toproot`, and the integral construction of the Higman operator and of the pairing in `pax:ss-forms`/`pax:ss-pairing`. Therefore this block does not yet certify the complete theorem of denominators.

**Base level 7527–7588:** the twisted action ρ(u)=Πψ_w(det u_w)·right(k′_u) is independent of the lifts, preserves J_O and cancels the inverse factor of the theta kernel. At Q the lower triangular matrix transforms the upper block T^(1) by a⁻¹ and produces χ_O=ψ(det a)⁻¹. At the chosen places the datum T≡ι₀ is fixed by the subgroup that fixes the first columns. These computations are correct; membership in the category of inertias of all the systems of this base level needs in addition `prm:label`/`prm:inertia` and the local dictionary cited above.

## 10. Dictionary U and spherical chain: additional closure

`pax:Ueig`, `pri:dict(b,d)` and the elementary proof `pay:chain` (6317–6417 and 6710–7086) were reconstructed. **(a) in the ranges n≥3 used here, under the local–global compatibility already declared.** For n=2 the proof of Ueig formally invokes a parahoric of blocks (1,0); that step is replaced by the immediate fact that a spherical representation of GL₁ does not admit a ramified character on O_F^×. This does not affect the range n≥6 used by the proof of denominators.

The parahoric line with ramified character is unique: in the Bruhat decomposition P\G/P there are two cosets, and the second would require a ramified character in the cuspidal support of the spherical factor. The q^(n−1) classes of I₁dI₁ and the factor δ_P(d)^(1/2)=q^((1−n)/2) give U=q^((n−1)/2)Π₁(π). The projection e onto the unique ramified line commutes with Frobenius, and the cyclicity of the trace justifies tr((γ−1)g p(φ))=p(μ)tr((γ−1)g) even though g does not preserve that line.

For the spherical chain, the count of hyperplanes gives q^j preimages if e₁ does not belong to the subspace and zero if it does. The duality L↦L* produces the second recurrence with q^(n−i−1), and U′ is really the adjoint after inserting the average M over I₁. The following identity was checked:

`c (z_c,x)(q^(n+1)−1)=P(qc)(x,x)`, with z_c=((P−P(c))/(X−c))(U)x.

If P(c)=P(qc)=0, U′z_c=q^(n−1)c⁻¹z_c and (z_c,x)=0; by adjunction z_c is orthogonal to all the A(U)x and, in particular, to itself. This proves the cancellation of each consecutive root without supposing U normal. The induction cancels the complete segment, and the stability of span{x₀,…,x_n} under U′ allows one to pass from R(U)x=0 to the adjoint identity bar R(U′)x=0. This is exactly the identity necessary for the orthogonality of `toproot`, not only a scalar divisibility of polynomials. The symmetry P(y)=0 ⇐ P(y′)=0 with y·bar y′=q^(N−1) comes from the adjoint T_i* and the central character; together with the strict bound of `chain(i)` it completes all the intermediate roots. Thus the local input pending in §9 is closed, without using Tadić as a substitute for the proof.

## 11. Closure of Higman and pairing; failure of scope in base level

**Higman and pairing (6045–6268): (a) with the lattice and norm of P49/P53.** J₀ is free by the principal level lemma of P46; Γ acts freely on each fibre of the double cosets. Multiplying by an indicator of representatives of Γ′ and summing its conjugates produces 1 at the free level. Averaging over H=J_O/J₀, without dividing by #H, produces Ψ at the base level with sum of conjugates c₀=#H. The translations are integral in the gauges and c₀|N_ch by inclusion in GL_{rt}. The stabilisers inject into H. The pointwise computation of the pairing uses the integer Gram matrix and the polynomial identity tρ(g)Gρ(tg⁻¹)=G; once the gauges are cancelled, each term is integral, and multiplying by N_ch eliminates all the stabilisers. The review of P53 collated 9770–9804: the lattice and the norm are precisely the standard tensor restriction, without an additional change of scale. This closes the Higman/pairing pending item of §9.

### 11.1 Fixed polynomial for all the elements of inertia — (b), first line 2271

`pri:BL(c)` asserts `o_w(ρ_x(s))(ρ_x(s)−1)=0` **for s∈I_w**, o_w being the fixed polynomial of the images of the roots of the label. It is repeated at the end of Step 5, 6556–6560. It is proved only for a normalised tame generator γ; at γᵃ the roots are the powers ξᵃ. For example, for a root ζ of order greater than 3 and linear label X−ζ, s=γ² gives (ζ²−ζ)(ζ²−1)≠0. Semisimplicity does not convert those roots into a set stable under all powers.

The application of `pri:columns` 2855–2865 only needs the polynomial at a generator δ_v, so that this pointwise defect can be corrected there at no cost. For all s one must use o_{w,s} with roots evaluated at s. **P56 7962–7985 already formulates this dependence correctly** by means of M_s and q_s; the same error is not attributed to it. But the other question of scope that follows is not fixed merely by changing s.

### 11.2 Scope of “base level” and preservation of the type e_c — discrepancy of formulation; explicit repair

Textual chain checked:

1. `prm:def-level` 7527–7543 defines F(O) by J_O and χ_O, **without** the condition e_cy=y. At a chosen place J_O fixes the first r′ columns and leaves the block GL_{t′} free. On F(O) the group G_c acts through ρ, with all the permitted types.
2. `prm:label` 7606 requires explicitly **e_cy=y≠0**. It is that hypothesis which allows one to assert that the first block has rescaled type σ_c. Its proof is correct under that hypothesis.
3. `pri:BL(c)` 2265–2273 quantifies, by contrast, over **every system … occurring in base level with principal level at U**, without limiting to e_cF(O). The sentence (a), e_cF(O) consists of forms of base level, does not impose that restriction on F(O).
4. The proof 6467–6471 begins `By Lemma prm:label(b), Π_w^{K(1)} contains ... σ_{tilde f_k}`. If F(O) is read as in the statement, this is the first application that requires the additional hypothesis e_c. However, the introduction of the subsection pax:ss-BL (6430–6437) declares explicitly that there “base level” means in addition fixed by e_c; under that clarification the use does satisfy the hypothesis. The discrepancy between formulations is recorded, not a definitive failure of this application.
5. In `pri:III` 3094–3098 Y is effectively replaced by the set of **all** the systems of eigenvalues that occur in base level with principal level at the w_j, and BL(c) is applied to that Y. `pri:columns` then needs a common polynomial o_w, of the roots of c, that kills the inertia of each u_x. That uniformity is not deduced from the written hypotheses.

No global automorphic system contradicting the conclusion of pg:III has been constructed here, and it is not asserted that it is false. The clarification of 6430 permits a consistent restricted reading; it remains to verify the preservation of that restriction in the operators of the proof of denominators. The natural repair would be to restrict all the spaces of operators and Y to the type e_c; it must be verified that the integral Higman operators and the deformed norm are preserved on that lattice with the same constant. Ψ is not a Hecke operator and its construction by means of coset representatives does not declare commutation with G_c. Projecting it by e_c can introduce denominators and it has not been shown that they are already covered by N_ch. Alternatively one would have to construct common inertia polynomials for all the types present, and justify the degrees used in P56; it is not enough to declare that they exist because the types are finite.

Therefore the local/algebraic closures of §§7–10 must not be summarised as unconditional certification of pg:III. The global pending item is now a concrete obligation at a junction, not breadth of reading.


**Reconstructed repair of the preservation of e_c, with the same bound N_ch.** At the free level J₁ of 6045–6070 there acts D=Π_{w chosen}GL_n(F_w), in addition to Γ of the auxiliary places; the actions commute because their supports are disjoint. D preserves the level character at Q, also disjoint, and the integral gauges. Starting from the same indicator Ψ₁ with Σ_{k∈Γ′}k⁻¹Ψ₁k=1, define

`Ψ_D=Σ_{d∈D} d⁻¹ Ψ₁ d`.

Then Ψ_D is integral, commutes with D and satisfies Σ_{k∈Γ′}k⁻¹Ψ_Dk=#D. Since it commutes with D it preserves the H-invariant subspace of the level J_O and the components of σ_c for the twisted action of the block GL_{r′}; therefore it preserves e_cF(O) and its intersection with the integral lattice, without applying a projector e_c to the values. One can take c₀=#D in place of #H: by n≤rt, #D divides N_ch, and all the estimates of `pri:norm` and `pri:III` only use c₀|N_ch. The Hecke operators and the translations at auxiliary places also preserve e_c. With this explicit substitution and reading Y in e_cF(O) as 6430 indicates, the obligation of preservation is resolved without changing β_ℓ. This repair is not the operator written in the paper; it is distinguished from certifying its original construction literally. It is a remediable ambiguity/omission, not evidence that the strategy of denominators fails.

## 12. Collation of G123/G45 with primary sources

The primary formulations were collated, not only the bibliography of the paper:

- [Labesse, *Changement de base CM et séries discrètes*, Corollaire 5.3, pp.42–44](https://webusers.imj-prg.fr/~michael.harris/CBCM.pdf): gives the conjugate-self-dual discrete constituents and the compatibility at split and unramified places. Condition (*) holds for U∞ compact; the real degree ≥2 appears explicitly. These are the hypotheses used here. The passage to Speh and the algebraic twist were reconstructed in §6.
- [BLGGT, *Potential automorphy and change of weight*, Thm.2.1.1, pp.33–34](https://virtualmath1.stanford.edu/~rltaylor/pa3.pdf): contains semisimple existence, the weights and the compatibility including N away from ℓ. At ℓ, that statement only gives identity under Iwahori and crystallinity if it is spherical. P55 recognises the restriction and does not improperly use this part for the ramified tame level.
- [BLGGT, *Local-global compatibility for l=p, II*, Thm.1.1 and §1](https://www.ma.imperial.ac.uk/~tsg/Index_files/localglobalII.pdf): the relation ≺ is asserted without Shin-regularity; the latter is required only for the general equality. The definition of ≺ compares partial sums of sizes of blocks. If the automorphic parameter has N=0, all those sizes are 1, and ≺ forces N=0 also on the Galois side. This is exactly the use in P55, and so the possible lack of Shin-regularity does not open a gap in G4.

**Result:** no absent external hypothesis of residual irreducibility, large ℓ or Fontaine–Laffaille was detected in G123/G45. The automorphy lifting conditions of other sections of BLGGT are not conditions of its Thm.2.1.1. The distinction is maintained from the incorrect sentences on generators and roots pointed out in §§6,11.

## 13. IM54 → twisting55, reconstruction of the junction

Reading and reconstruction of P54 1798–2085 and P55 1925–2088. **(a) for the deductions from the kernel inputs of P49, Rallis and exchange 53; identity of statements confirmed in the range applied.** The independent audit of Rallis/exchange belongs to the reviews of P53/P54; here it is checked that IM does not add an unjustified hypothesis in the specialisation.

For z≥2, the expansion of `pex:points` uses a finite set of ideles x_{c,a} depending on Q, not on θ. The sum of points absorbs the twist by θ(x)⁻¹; the quadratic norm gives θ(x_p x_p′⁻¹) multiplying a coefficient independent of θ. The stabilisers divide N_z; n_p² eliminates the denominators of the kernel and (NmQ)^(1−2z) is a unit at the ℓ that are used. Integrality requires the two embeddings j and j∘c, exactly as the pairing of §11. The constant n_p may depend on p=(ν,z) and does not require an explicit bound: v₀=vℓ(F(1)) is cancelled afterwards.

The case ℓ=d is not omitted: `pex:dint` scales the variable by d. The limit v(x(P))≥−2/(d−1) for d-torsion in the formal group gives v(g″(0))>−2. The derivatives of order ≥3 come from x and are integral. Hence the jets of degree k become integral on multiplying by d^k, with k fixed by the weight; the new n_p remains independent of Q and θ. This computation depends on the curve/integral model of P49, not on a tacit assumption d∤ℓ.

For z=1, `pex:E1` applies exchange 53 with N=a=2,b=0,e=1 and μ=c≥1. The matched data are exactly χ_θ∘det, because the character of the exchange is the inverse. The compact projector onto invariants transforms x into κP_c: the space of polynomials of that type is a line by density of U(2) and evaluation at invertible matrices. κ≠0 because the constant side of the exchange is non-zero. The archimedean types do not change with θ, so that κ and C₁ are independent of the twist. Thus F(θ)/F(1)=NmQ·ρ_p(θ)².

In `pex:IM1(b)`, expanding the datum in δ_y and translating it to δ₁ cancels χ_θ(det y) with λ_θ(det ŷ)⁻¹. The remaining twist is θ(det(hŷ)); on multiplying by the conjugate one obtains another finite sum of characters with integral coefficients. To increase the modulus by an unramified prime, evaluating the Hecke polynomial of the vacuum at α⁻¹ selects the matrices of rank 2. Integrating the translations contributes (1−α⁻¹)(1−qα⁻¹), with α⁻¹=q⁻¹a. Its quadratic norm gives exactly the factors for e=0,1. The absolute value of an L-value is not replaced by an algebraic expression without proving it: it is obtained from the period and the exchange identity.

In P55, the polynomial P_Y is evaluated only at ℓ^N-th roots of unity. The difference between the restriction to the line and the product of Euler polynomials is divisible by (1+X)^(ℓ^N)−1, monic, over the ℓ-adic algebraic integers. The valuation of the error at v(y)=ρ is ≥Nρ and exceeds β_Y+s₀ρ. The linear Euler factors have unit leading coefficient and cost ≤ρ each. The common choice of roots avoids the residual zeros for the finitely many systems and all the exponents j≤m. Finally v(Fθ)=v₀+(m_IM+1)v(rθ), with NmQ a unit; taking the positive part gives the inequality used in II(c). The omitted factors are those of M in numerator and denominator, and Q only in the numerator; for a genuinely ramified twist at each Q the latter are already trivial. The moduli enlarged with θ unramified there are used solely in the distribution relation, where the explicit factors do appear.

## 14. Closure of the local sum and of the sum over primes

**(a), as an assembly under the inputs and repairs identified.** In 3513–3523 the cases (b),(c) use floor(log_ℓ h³)+1≤m and x_c≤t; in (d), floor(u)≤u gives 10⁵(ρ floor(2λ/(kt))m+floor(ρm/(kx))λ)≤3·10⁵ρmλ/(kx). The length of case (d) is not multiplied again by the rank. The sum 3535–3540 uses Σ_v[E_v:Q_ℓ]=2f and Σ_c rk(L_c)/x_c=r′+t′/t≤2r′; hence exactly r′loc_ℓ. For ℓ>2b, ℓ∤M, λ_ℓ=0 and the defect is zero.

In `pg:sums` 493–534, Σv_ℓ(n)logℓ=log n controls N_ch as well as h₁ and C_odd. The quantity λ includes the factorial and a window of length 60h³, with multiplicity h³: its sum is ≤3b log b. The part of M is ≤22b log b, giving 10⁸f(m/k)b log b. The bound of C_odd is now supported by §7, and not as an unreviewed premise of the first report. The remaining terms ≤x¹⁰⁰⁰ are absorbed using b≥x^(10¹²). Finally m²≤4x and (log b)²≥8·10⁸ give the budget fa(log b)³/(mk), with a=xb. The factor logℓ in the junction with P46 is present; normalised valuations are not summed as if they were logarithms.
