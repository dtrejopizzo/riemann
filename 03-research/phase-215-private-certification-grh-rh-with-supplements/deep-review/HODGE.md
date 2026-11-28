# Deep audit of P56: record of obligations

Date: 2026-11-28. Source: `04-papers/56-explicit-cup-exponents-local-galois-representations/main.tex`. The lines that follow refer to that `main.tex`. No paper was modified.

This record replaces the mere annotation “not reviewed” for the steps indicated. **It is not yet a verdict (a) on the whole of P56**, nor on the series. (a) means that the proof of the obligation identified was reconstructed; it is not used as a synonym for “I did not find a counterexample”. The internal dependencies traced and the external ones accepted are made explicit.

## Current status after the deep review

**(a) for the local chain of cup products, with the printed hypotheses:** T3, I2, I4, I5, SCC, scheme and the specialisations sparse/any/generic/tame/crys are reconstructed in §§1–6. It includes the small primes in the alternatives that admit them. **NM is sufficient, not necessary**; the counterexample to necessity is in the initial report. The application data is (a) under the data of P46 and M2/G4 of P55. The latter were subsequently collated with the primary sources and their uses in SELMER §§6,12. The sentences about pending items in the earlier passes are historical, replaced by §§5–6 and this status. The literal corrections of P55 indicated in SELMER §§6,11 persist; they do not belong to the local proof of P56. The global existence of the data of P46 belongs to the audit of that paper.

## Result of the first pass

| Obligation | Result of the review | Scope |
|---|---|---|
| `pkw:T3`, lines 7753–7782 | **(a)** | The tame annihilator is obtained with the printed exponent, under the printed hypotheses and the conventions of side/tame chart. Neither residual irreducibility nor a change of the lattice is used. |
| `pkw:Z`, `pkw:step`, `pkw:count` | **(a)** | The division by `z` is integral; it is not a division only in a rational period ring. |
| `pke:I2`, lines 4829–4844 | **(a)** | The deepening has cost `vℓ(n)+d_v+3a`, with the explicit convention `vℓ(0)=0`. It includes the levels and the negative integers indicated. |
| `pkh:I4`, lines 5793–5814 | **(a)** | The proof even gives `Σ((8a+1)n_i+3(W+1)r_i)`. The elimination of poles and the auxiliary division by ℓ were verified. |
| `pkg:I5`, lines 5180–5229 | **(a), for the local construction** | Radius, series, Taylor and the exact correction of the image were reconstructed. The cost is `κ+4δ`. |
| `pkd:scheme`, lines 6882–6992 | **(a), as a deduction from walk/rule** | The orders, shifts, costs and the two uses of the zero shift are verified. The final translation of safe paths into cocycles/cup products requires the separate review of the initial block `pkp:letters` and its construction of SCC. |

**Concrete pending item to close the main assertion on cup products:** reconstruct `pkp:letters` and its preceding lemmas, including the identification of SCC with vanishing of the cup product, and then review all the specialisations sparse/any/data, not only the arithmetic of their constants. That pending item is not identified with a failure of T3, I2 or I4. The rule `pkp:rule` and the formal assembly of `pkm:walk` were read; what remains in this pass is to close the cohomological block on which they depend.

## 1. T3: complete reconstruction of the descent

One works in `A=A_inf`, not in its field of fractions. `I_0(i)` is the ideal of scalars that uniformly lift all the parameters of the side; `J=I_0(i)+ℓ^(κ+1)A`. `pkm:zpow` (1711–1730) gives an integer ν with

`z^ν ∈ J`, `(ℓ−1)ν ≤ e(n₀+κ)`.

The hypothesis `n₀+κ+2<ℓ` implies ν<e. The polynomial that must kill the extension is **Q=q(X)(X−1)**, not q. The additional factor kills the trivial representation of parameters. The exactness of D_pcris in the potentially crystalline category allows it to be applied to `X_S` (`pkw:ext`). This explains exactly the `+1` of `m₀(deg q+1)`.

Let ξ be the tame root of order e and a its reduction. Since e is prime to ℓ, the elements `a^k`, `1≤k<e`, are distinct. The reduction of Q is monic and non-zero. Hence the number of bad indices `Q(a^k)=0` is at most `deg q+1`, even with multiple roots. If k is good, `Q(ξ^k)` is a unit of A.

The induction invariant is

`ℓ^t z^k ∈ J`, `k<e`, `t+m₀ b(k)≤κ`,

with b(k) the number of bad indices between 1 and k. A good step reduces k by one at no cost by means of `pkw:step`. A bad step uses `pkm:lower(i)` and costs `vℓ(k)+1≤m₀`, since `k<e≤ℓ^m₀`. The cost can be increased to the integer m₀ without losing membership in the ideal. At k=0 one obtains `ℓ^κ ∈ J` and, writing `ℓ^κ=s+ℓ^(κ+1)b`, it follows that `ℓ^κ(1−ℓb)=s∈I_0`. The unit `1−ℓb` gives `ℓ^κ∈I_0`. **It is not necessary that I be finitely generated, nor is an unjustified version of Nakayama needed.**

In particular, e=1 causes ν=0 and does not require a bad step. For ℓ=2 the numerical hypotheses of T3 are empty if the parameters are non-negative; T3 does not by itself provide a non-empty bound at ℓ=2. This is not an omission: the other cases of the crystalline theorem use the general annihilators, not T3. No hidden hypothesis `ℓ≠2` appears in the descent.

### Why the good step is integral

`pkw:Z` (7680–7710) starts from `x∈N∩M_inf` and produces

`z⁻¹ Σ_j Q_j s₀^j x ∈ M_inf`.

The action of s₀ preserves M_inf, the parameters, E and the letters. The retraction implies that the coefficients of x in the basis of the frame are in S. For a form μ, the conjugate forms satisfy an exact relation because Q kills the action of inertia on D_pcris; the constants of values are in the unramified subfield and s₀ fixes them. On the other hand, for b∈S_B one has `s₀b−b∈zB⁺`, using `ℓ^k b=λ+zw`, λ∈Λ. The test of coefficients of the frame gives `E^(4a)s_j∈zB⁺` for each coefficient s_j∈A of the sum.

The passage from B⁺ to A is made by `pkl:intdiv` (3919): if ν is not divisible by ℓ and divides `E−ℓβ`, the divisibility by ν of an element of A in B⁺ already holds in A. It is applied with ν=z and β=1. Then E is cancelled because `(E)=ker θ` is prime and `θ(z)≠0`: if `E^h s=zq`, primality gives E|q, and one cancels successively. **It is not assumed that z is prime.**

For the version in J, `pkm:J-basic(iv)` gives a unique u∈S such that the lifts of all the c have projection `(ℓ^t z^k−ru)ε_i(c)`, r=ℓ^(κ+1). It is essential that u be uniform in c. One writes u=w+zv with w∈Λ; `Q(1)=0` eliminates w. Applying Z one obtains a scalar of I whose difference from `Q(ξ^k)ℓ^t z^(k−1)` belongs to rA. This proves precisely the step required in J.

### Obligations of the infrastructure that were traced

| Block | Verification carried out |
|---|---|
| A1, 2999; A7, 3096 | Regularity at ℓ of `A[X]/(ℓX−E)`, reduction modulo ℓ and intersection `A∩ℓ^n A_max=(ℓ,E)^n`. Closure of `(δ)` with ℓ∤δ: noetherianity of A is not presumed. |
| A5/A6, 3179/3195 | S-linear coordinates over A by means of `(ℓ,z)`-adic approximations and separation; the finite rank argument uses those coordinates, not a basis of finite size of the whole of A. |
| A2–A4, 3259–3320 | Contraction by Frobenius, control of denominators and approximation; the monic division in the variable E/ℓ maintains integrality. |
| A8, 3365 | Extension of S-linear maps to B⁺; the bicommutant S_B makes them S_B-linear. The property with scalars K′ uses approximation modulo E^n. |
| `pkf:key`, 2804 | The minimal support argument is applied over the residue field of the valuation after normalising one coordinate to 1. The Ax–Sen–Tate approximation and the separation by coordinates contradict `det Q≡0 mod ℓ`. A congruence is not replaced by an equality of invariants. |
| `pkf:frame-pm`, 2845; `pkf:main`, 2868 | From the saturation and the divisibilities one obtains `QQ′=τ^(2a)`, `UZ=E^(2a)Q`, `YZ=E^(2a)` and the frame. The matrices correspond to the original lattice L. |
| `pkn:frame`, 2130; `pkl:std`, 3593 | The test of coefficients and the cancellation of τ identify M_inf with the free module of the frame and `std_l=φ^l M_inf`. |
| `pkl:valret`, 3718; `pkl:R`, 3837 | The retraction is defined respecting all the relations, preserves the filtrations and commutes with the projection of parameters. An arbitrary retraction is not applied to coefficients without checking its relations. |
| `pkl:G0`, 3977; `pkm:lower`, 1668 | The quotient by zτ remains integral; the cyclotomic identity produces the cost `vℓ(k)+1`. At ℓ=2 the final term has strictly greater valuation thanks to v(π)>0. |
| `pkm:zpow`, 1711 | The least exponent that works on all the letters is chosen. Frobenius and the descent of level give `a≤floor((a+e(n₀+κ))/ℓ)`; this is the source of the initial inequality. |

The external inputs used are the classical statements P1–P3, P5–P6 printed at 2260–2298: structure of the Fontaine rings, crystalline and filtered comparison, Ax–Sen–Tate and invariants of C(j). No attempt was made to reprove those classical theorems. The primary reference of Colmez, §III.1–2 and §III.4, identifies B_max and B_cris for crystalline representations and allows one to verify that those rings are used here and not a different ring of convergence: [Colmez, author's text](https://webusers.imj-prg.fr/~pierre.colmez/iwasawa-deRham.pdf). For the filtered comparison: [Fontaine, Exposé III](https://www.numdam.org/item/AST_1994__223__113_0.pdf). They are standard mathematical dependencies, not certificates of the new numerical limits.

## 2. I2: costs of deepening

Lines 4480–4848 were read in full. Three potentially delicate points are resolved:

1. **Values at level a.** `K_a` is the field of fractions of the ring generated by K′, S_B and `φ^(−a)S`. If f is S-linear, `f′=φ^(−a)fφ^a` is also S-linear, even though `φ^(−a)S` is not contained in S. The equality uses `φ^a(S)⊂S`. On eliminating a common denominator, A8(c) proves `pke:valret`; any B_dR⁺-submodule is preserved, in particular all the filtrations. `pke:values` obtains μ_a(x)∈K_a by means of a non-zero coordinate κ_j over the denominator: it does not presuppose what it must prove.
2. **n≠0 and all primes.** The identity `δX=ω′^n−1` has `δ=zτ`; δ is a unit in B_dR⁺ at each level, but not in A. The integral divisibility is established before that unit is used. For n<0 one uses `ω^(−k)−1=−ω^(−k)(ω^k−1)`. The valuation of the power grows exactly by vℓ(n), because `v(θ(ω−1))≥v(π)+1/(ℓ−1)>1/(ℓ−1)`; this includes ℓ=2. The additional cost `d_v+3a` covers the different and the comparison of θ with θ_a. One obtains `p_a | υX−ℓ^cost`.
3. **n=0.** It is not treated by means of a false valuation of zero. One averages over `ℓ^cost` Kummer translations, with cost=d_v+3a≥a. The sum of roots of unity leaves exactly the powers z^k with ℓ^a|k; their values are in K′. Tate then gives a constant value modulo Fil¹.

For n≠0, if μ_a(x)=γ+y, y∈Fil^n, the operation `D=ℓ^cost x−υδ⁻¹(gx−x)` cancels the leading coefficient of y. The retraction preserves the new congruence. Moreover, by G0 and the stability of the orders, D and its retraction have the required cost for **all** the orders already acquired. The composition does not destroy them. The induction `pke:A` eliminates a pair (a,n) of maximal height n, avoiding the presupposition that the pairs can be applied in an arbitrary order. Finally, the adjustment by `ℓ^(e′−e−Σcost)` produces exactly the desired projection in I2.

## 3. I4: length, few low weights and the constant

Lines 5270–5820 were read in full, including the part of `pkh:div` that lay outside a truncated output. A length is not derived from a mere annihilator: the number of generators of the ℓ-torsion is also controlled.

`pkh:lead` chooses a minor of **maximal absolute value** among a finite number of minors. Cramer gives coefficients in O_C. They are lifted to A and retracted to S. Reducing S modulo E leaves Λ, of rank f over Zℓ. Hence `fn+1` vectors admit a primitive relation with one coefficient equal to 1. This explains the factor f and the use of the multiplicity of the weight u; it does not simply count the number of distinct weights.

In `pkh:div`, from `ℓx−w` with increased depth it is not illegitimately concluded that x has that integral depth. One first constructs `w′=E^(−ℓ^a)Aw`, with A an operator of cost zero; the a-free condition ensures that it exists. The identity `E^(ℓ^a)−p_a=ℓr` gives `m=rw′−(Ax−x)` in the integral module of order c. Only **afterwards**, already knowing that `x−m` belongs to the required ambient module, is ℓ cancelled in the filtration conditions of B_dR⁺, where ℓ is a unit. This is a valid cancellation.

`pkh:len(iv)` shows that a quotient killed by ℓ^t and with ℓ-torsion of dimension ≤m has length ≤tm. It is proved by induction even if initially it was not assumed finitely generated. The preceding primitive relations establish exactly that dimension bound.

The elimination of poles contributes `a n_i`. The cost at level zero in a negative window is ≤`(a+1)n_i`: for far weights NM eliminates all the multiples; for the low ones Legendre is used. At level one the cost is `3(W+1)r_(i−1)+6a n_(i−1)`, because the only valuation costs are zero, also for y=0 by the explicit convention. The sum over the permutation of letters gives

`Σ_i [(8a+1)n_i+3(W+1)r_i] ≤ 11Σ_i[n_i(a+1)+r_i(W+1)]`.

The published bound 11 needs no additional loss. NM is used for the sufficiency of these steps; its necessity is not deduced here. The counterexample to the necessity of NM recorded in `04-selmer-hodge.md` remains valid and does not refute I4.

## 4. I5 and the scheme: local closure and remaining cohomological obligation

To avoid treating `pkd:scheme` as a black box, lines 4860–5235 and 6730–6995 were read. In I5, the ring of series is not informally identified with B⁺: `pkg:Shat` constructs an injection into Λ[[T]], T=z/ℓ, and proves `∩ z^n S_B=0`. The series of `pkg:series` uses that separation to eliminate a remainder; it does not need that remainder to tend to zero in a norm that was not controlled. The parameter `X_l=z^(ℓ^l)/ℓ²` belongs to ℓ·Shat precisely because `ℓ^l≥3`.

The simultaneous approximation of V and V⁻¹ costs twice `2δ`. The columns of M and of `ℓ^(4δ)−MM′` have constant values modulo E^A and generate a module that contains `ℓ^(4δ)S^d`. From there comes **4δ**, without a constant depending on the rank. The extraction of the coefficient of degree N of a monic polynomial gives the correct projection modulo E^A; the correction of the error uses the annihilator ℓ^κ on the letter of origin. The final result has projection exactly `ℓ^(κ+4δ)c`, not only a congruence.

In scheme the following were verified separately:

- The conditions `(C)` cover all the deepening steps, since the orders coincide for levels greater than l.
- The requirement `s_i=0 or s_i<β_i` excludes the weights that would prevent obtaining orders ρ_(−η).
- In a long gap, I5 is applied to the negative-window side of the pivot; the weights of the intermediate letters are bounded by ω, with `N<β_pivot≤A`.
- Transporting by φ^t gives depth 1 before the pivot and 0 between the pivot and the cut. The only steps added are `(a,0)`, t<a<l, with cost 3a because the chart is unramified.
- At the pivot, the critical inequality of rule is `A+min(η−u,0)≥1`; it results from u≤A and η≥1. Away from the pivot one obtains 1+0.
- The zero shift of the previous cut is used **twice**: for the pure annihilator in I5 and for `rule_(l,0)`. It cannot be deleted from the hypotheses.
- The final exponent of walk is `e+e′+κ=2e*+κ`.

The reading of the assembly of walk confirms the telescoping by Frobenius and the separation of moves. What remains in this pass is to reconstruct from its definition the SCC criterion and the prior proof that these moves produce the zero cup product. **Next action:** begin with 650–820 (`pkp:def-pairing`, safe pairs, SCC, `pkp:letters`), trace the operator φ−1 on the residual module and check the integrality of the coboundary, before raising the partial verdict to an (a) for the main theorem.

## 5. Second pass: closure of SCC, cup products and walk

**Update subsequent to the preceding sections: the cohomological obligation indicated there was closed.** `pkp:AS` (915–986), the full proof of `pkp:pairing` (1001–1071), `pkp:letters` (1074–1086), `pkp:cut` and `walk-arith` (1131–1186), `pkm:walk` (1368–1398) and `pkc:cup` (6323–6354) were read and reconstructed. Verdict on these steps: **(a)**.

The check does not consist in citing the word “cup”. In M=W(C^flat)/ℓ^m(1), Artin–Schreier–Witt makes φ−1 surjective. If `(φ−1)d` has all its first m components in the maximal ideal of the tilt, then d differs from a constant of Z/ℓ^m(1) by a small element. The constant is unique because `F_ℓ∩m^flat=0`. This is proved coordinate by coordinate and does not use ℓ odd.

For the two points x,x′ and the intermediaries w,w′, one chooses y with

`(φ−1)y = <w,φx′−w′> + <x,w′−x′>`.

The cochain f printed at 1009 satisfies two identities, verified by expanding the coboundary:

- `(φ−1)f(g)` is the signed sum of the four pairings that define the safe moves;
- `ℓ^(e₁+e₂+κ) P(α(g),gα′(h)) = <gx−x,g(hx′−x′)> + (df)(g,h)`.

The additional terms belong to the small part. Writing `f(g)=k(g)+δ(g)` with k constant and δ small converts the second equality into an **exact** equality with dk: a small constant is zero. A small term is not discarded merely because it has positive valuation.

The continuity of k is also proved: near 1 the cocycles and the action on the lattices are zero modulo ℓ^m, and the continuity of the first m Witt coordinates makes f small. By uniqueness, k=0 there. The coboundary equation then implies that k is locally constant on the whole of Γ′. An arbitrary solution of Artin–Schreier is not used as if it were automatically continuous in g.

The restriction to Γ′ does not lose a power of ℓ: corestriction after restriction multiplies by the index, which is prime to ℓ by the definition of chart. The class is ℓ^m-torsion; by Bézout its vanishing on Γ′ implies its vanishing on Γ. Finally `pkc:cup` uses explicitly Hilbert 90 and the Kummer sequence to inject `H²(Γ,μ_(ℓ^m))` into `H²(Γ,Qbar_ℓ^×)`. Hence SCC does imply the coboundary in the finite coefficients required by the local defect of P55.

The letters do not interact because P comes from an O-bilinear form: `P(ζv,v′)=P(v,ζv′)`. If their letters are distinct, their Teichmüller difference is a unit and P(v,v′)=0. The final application of walk introduces no factors for the number of letters. The three inequalities of `walk-arith` were verified separating a<l, a=l, a>l, and their cases with d=0.

**Updated status:** `pkd:scheme` is certified with its conclusion SCC, not only as a conditional deduction from an unreviewed cohomological rule. To close the whole main theorem of P56 there remain the specialisations `sparse`, `any`, `generic`, `tame` and `data` with all their ranges and with the identity of the classes of lattices in P55. Some numerical conversions are already recorded in the initial report; their complete tracing and assembly into a single verdict are missing.

## 6. Third pass: the specialisations and their global scope

`pkt:add` and `pkt:I3` (4166–4440) were reconstructed: membership in the integral module is proved before adding orders; the inequality is required for **u+u′≤v**, not only equality. The test of Hodge forms proves that condition with the weights that actually occur. The form of the dual extension has term `ℓ^m φ+aψ`; its equivariance uses precisely the defect cocycle of ψ. The symmetric case of the rule contains g applied to the move of the second side, as the coboundary identity requires.

The assemblies `pkc:generic` (6460–6590), `pkc:tame` (6629–6690), `pkd:sparse` (7050–7119), `pkd:any` (7124–7188), `pki:crys` (552–623), `pkj:chart` and its proof (5840–6150), and `pkd:data` (7190–7295) were read in full. Results:

| Result | Verdict of this pass | Precision |
|---|---|---|
| `pki:sparse` / `pkd:sparse` | **(a)** | The three requirements K,C,G of scheme are verified, and the range ℓ=2 falls in the alternative of constant sign, not in the long gap. |
| `pki:any` / `pkd:any` | **(a)** | The cuts have distance ≤2; the only non-flat configuration has pivot 0 and requires `G+7K≤floor(b/ℓ)`. The inequality N<b and the cost `22K+3` follow from it. |
| `pki:generic` | **(a), as a sufficient criterion** | The argument of few low weights and the normalised length are verified; NM is not declared necessary. |
| `pki:tame` | **(a)** | The polynomials in K(s₀) and K(s₀⁻¹) are used in the correct sense for L and for the dual of the tensor. |
| `pki:crys` | **(a)** | Uniform deduction of the four criteria under S1–S4 and the definition of letters reading thickness. |
| `pkj:chart` | **(a), under the cited data of P46** | The prime-to-ℓ roots, both directions of the ratios, the constancy of the sign at primes of the conductor and the transfer of sparseness are checked. |
| `pkd:data` | **(a), under M2/G4 and the cited data** | The weights of the dual are −u−1, and the tame class of the dual uses K⁻¹. It does not by itself certify that the automorphic representations of P55 satisfy M2/G4. |

### Checks that make the uniformity valid

**Sparse.** The distance between cuts is ≤2J+1, even if there are no thick letters. If a configuration is not flat, there is a unique interior thick pivot and its distance to the previous cut is J+1. With `κ=4ϑ+(J+1)M`, `e*=8ϑ+6(J+1)M`, the exponent of scheme is `20ϑ+13(J+1)M`, smaller than the published one. In the ramified alternative of constant sign I5 is not invoked. The valuation cost is summed over two intervals of radius ≤3η, not over a window of size b.

**Any.** With q=floor(b/ℓ), the shift is max(q−7K,0), and κ=14K. If the successor is thin, kill-J suffices; if it is thick, `(ℓ−3)(7K+q)>b+M`. The deepening budget is `62K+6 lgℓ(2(b+M))`, which with κ gives exactly e*. The remaining long gap has A=b+V and δ=2K. No different configuration of signs is omitted.

**Generic.** The choice of V depends only on L, before Y and the pairing are chosen. This is indispensable for bounding the length of the quotient by the orthogonal of **the whole of** C(U). In the negative window the check at level one is divided exhaustively into: weight of L low; weight of L far and weight of Y low; both far. In the last case the windows have opposite signs and `|u+u′|≤W`, which gives the sum of orders ≥1. The length over Zℓ is divided by `[O:Zℓ]=len_Zℓ(O/ℓ)`; it is not confused with the residue degree or with the ramification index.

**Tame.** `e₀≤ℓ^(r²)` and the polynomials that kill the three sides have degrees ≤N, ≤N and ≤N²; κ=r²(N+1)² covers each `r²(deg q+1)`. The chart uses ζ=1, so that it does not need to enlarge O to contain all the roots of its residue degree. The gap step uses a=0 and NM because all the integers examined have absolute value <ℓ. The result has no hidden dependence on the rank of Y.

**Uniform.** For ℓ≤Q, the thickness condition provides either an unramified chart with ℓ≥7 or constant sign; sparse is employed with radius 2G. For ℓ>Q and λ≥h³ any is employed. For λ<h³ the product included in λ excludes the multiples of ℓ in `(b−30h³,b+30h³]`; those of the low window are excluded by `ℓ>198G`. Thus one obtains NM with a=2(λ+1). If λ<floor(h/5), the separation of negative weights excludes `[-a,0)`. If not, `K≥W+1` and the bound I4 gives the published length. In the first two ranges, the rank bound of Z_f of P55 converts exponent into length; in the third the length is kept directly. One does not multiply again by the rank in case (d).

**Chart.** Away from the conductor, a letter determines the restriction to E_v because that field is unramified and generated by μ_(ℓ^f−1). At a prime of the conductor, the letters do not need to distinguish thin embeddings: these are absorbed into the radius 2G. For ℓ|q₀, the hypothetical equality of opposite signs contradicts the valuation of `(1+sqrt(−d))/2`; for ℓ=d, it contradicts `d≡q₀/2−1 mod q₀`. Sparseness is transferred with the inverse order of the three points if the reading R⁻ is used. The clauses `q₀` a multiple of 18480, `d≡q₀/2−1`, `q₁=q₀·3l₀(s)2^s`, `27s<l₀(s)`, the definition of sparse and (D5) were checked in P46 (P46, 2888–2971). It is not asserted here that the global existence of the data of P46 was reproved.

**Conclusion of local scope:** the deep mathematical obligations of P56 that were left open in the first report now have a reconstruction up to the uniform bound and its conditional application to the summands. No failed line was found in that local chain. The link not yet certified globally is the premise of P55 that identifies the automorphic lattices with the classes and weights used here (M2, G4 and base level), together with the existence and other properties of the data of P46, which belong to their respective audits. This conclusion does not prove GRH: it certifies the local segment indicated under those premises.

## 7. Novelty and primary comparison with Fontaine–Laffaille

**Absolute novelty: (c), not certified by this search.** The same theorem of explicit exponents of cup products, with the dependence on windows, letters and thickness of P56, was not identified in the primary sources collated. This does not prove priority. The potentially novel component that can be isolated is the quantitative calculation that translates separation of weights and a few bad indices into integral cost of annihilation, and then into the summable local loss of P55. Its concrete construction is reconstructed above; it is not necessary to declare that a completely different theory was created in order to describe it.

The integral theory beyond Fontaine–Laffaille already existed. [Fontaine–Laffaille, *Construction de représentations p-adiques*, §§6–8](https://www.numdam.org/item/10.24033/asens.1437.pdf) studies full faithfulness and filtered modules in its ranges of weights. [Liu, *Torsion p-adic Galois representations and a conjecture of Fontaine*, Thm.1.0.1 and introduction](https://www.numdam.org/item/ASENS_2007_4_40_4_633_0.pdf) gives the crystalline/semistable characterisation by all the torsion quotients of bounded weights without the Fontaine–Laffaille restriction. [Liu, *Filtration associated to torsion semi-stable representations*, introduction](https://www.math.purdue.edu/~tongliu/pub/filtrationnew.pdf) studies filtrations and rigidity of the Hodge–Tate type under sufficiently deep congruences, without restricting ramification or weights. [Caruso–Liu, *Some bounds for ramification of p^n-torsion semi-stable representations*](https://arxiv.org/abs/0805.4227) gives explicit ramification bounds for p odd, as a function of n, e and the range of weights. Those objects and conclusions are distinct from the cup product of P56; they do not replace its proof.

**Compatibility with FL:** no contradiction was found. For the overlap used in P55, ℓ≥4b+2 and ℓ∤q₁dM, the weights are in [−2b,2b], an interval of length ≤ℓ−2 that contains 0; the local base is unramified. The conclusion of zero loss is derived here from P56 and duality, not from asserting that any congruence of crystalline lattices is automatically controlled by FL full faithfulness. P55 3470–3480 declares explicitly that it does not use this latter route and that it would be necessary to formulate the integral statements on subquotients. That caution is correct: a comparison of categories in a common range is not by itself a proof of the annihilator of a cup product. The coincidence in that overlap is a check of compatibility and of hypotheses, not a second independent proof by FL.
