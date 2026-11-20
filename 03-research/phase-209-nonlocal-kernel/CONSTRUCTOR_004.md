# CONSTRUCTOR_004 — Denormalised coprime cross terms at the critical parameter

2026-10-18. **PROVED using Theorem 1 of ANTICORRELATION_003** (punctured geometric concavity, approved in AUDIT_003). Final review of this note: AUDIT_004. No zeros are used. The node remains OPEN.

## 0. New reason with respect to the index and scope

Consulted again: the entries L2_012, Helson, Tate/Poisson, SPEC005, INV_C and the mixture/covariance searches of the index, grid and crossword. Also CONSTRUCTOR_002 and ANTICORRELATION_003.

Positivity of |ζ|², an AFE, a Helson norm or the homogeneous positivity of theta is not retried. The exact difference is this: **the covariance between coprime divisors has vanishing principal counterterm**, so its Mellin denormalisation already converges at α=1/4 and keeps strict sign without continuation. This uses the concavity of τ=θ−1 and an exact cancellation of the limit of divisibility densities. It was not in the generic computation of CONSTRUCTOR_002, which treated G₀ without separating its vanishing entries.

It is a result about arithmetic cross terms. It is not yet quadratic positivity of the operator of the node, nor an effective kernel in height space. The PSD of a covariance matrix is not counted as the new result: the new result of this round is **strict sign of a denormalised cross term convergent at the critical parameter**, with an exact formula and genuine dependence on both indices.

## 1. Definition and exact asymptotics at zero

Let θ, τ and q_y be as in CONSTRUCTOR_002. For coprime d,e≥2, l=de and

`B_y(d,e)=τ(y)Cov_y(X_d,X_e)`

`          =τ(d²e²y)−τ(d²y)τ(e²y)/τ(y)`.

By ANTICORRELATION_003, `B_y(d,e)<0` for all y>0.

**Lemma 1 (PROVED).** For fixed coprime d,e, y↓0,

`B_y(d,e)=−(1−1/d)(1−1/e)/(1−√y)+O_{d,e}(y^(−M)exp(−c_{d,e}/y))`,

for some constants c>0 and finite M. In particular

`B_y(d,e)=−(1−1/d)(1−1/e)+O_{d,e}(√y)`.

**Proof.** Put r=√y. Poisson gives, for fixed k,

`τ(k²y)=1/(kr)−1+O_k(r^(−1)exp(−π/(k²y)))`.

Substitute the three factors; τ(y)~1/r allows dividing without problems for small y. The exact algebraic part is

`(1/(der)−1)−[(1/(dr)−1)(1/(er)−1)]/(1/r−1)`

`=−[(d−1)(e−1)/(de)]/(1−r)`.

The remainder is still exponential with a fixed power of y. ∎

As y→∞, `B_y=O_{d,e}(exp(−c'_{d,e} y))`, since τ(k²y)~2exp(−πk²y) and `τ(d²y)τ(e²y)/τ(y)` decays with exponent π(d²+e²−1)>0.

**Why the critical computation changes.** The general term `G₀(d,e)=(gcd(d,e)−1)/(de)` is zero for coprime d,e. The part `y^(−1/2)G₀` that forced renormalisation in CONSTRUCTOR_002 disappears exactly, not by a bound.

## 2. A genuine Mellin sign at α=1/4

I define

`A_α(d,e)=−∫_0^∞ y^(α−1) B_y(d,e)dy`, `(d,e)=1`, d,e≥2.

**Theorem 2 (PROVED).** For all α>0 and each coprime pair d,e≥2,

`0<A_α(d,e)<∞`.

In particular A_(1/4) exists as a strictly positive ordinary integral. There is no analytic continuation or subtraction of a counterterm in this claim.

**Proof.** Lemma 1 gives integrability at zero for α>0; exponential decay gives integrability at infinity. The sign is strict at each scale by punctured concavity. ∎

This keeps the sign when **denormalising**, which was the loss identified in CONSTRUCTOR_002. This property has only been recovered on the coprime cross terms; not on the whole matrix.

## 3. Genuine dependence on two indices, even after integrating

**Theorem 3 (PROVED).** For all α>0,

`A_α(3,10)>A_α(2,15)>0`,

although both pairs have product 30. Hence A_α is not of the form w(de).

**Proof.** Let f(x)=logτ(exp x), strictly concave. The pairs

`log(4y),log(225y)` and `log(9y),log(100y)`

have the same sum, and the second is strictly closer to the midpoint. Strict concavity implies

`τ(9y)τ(100y)>τ(4y)τ(225y)`.

The term τ(900y) of B_y is the same for both pairs and τ(y)>0. Thus `−B_y(3,10)>−B_y(2,15)>0` for each y. Integrate. ∎

The difference is structural with respect to the w(mn) of the main term of Gonek. Neither Gonek nor its error is used. **It is not inferred** from this theorem that a height representation of A_α lies outside every effective algebra after restrictions: that operator is not yet identified.

## 4. Exact Mellin and weight d^(−1/2)e^(−1/2)

Fix 0<α<1/2. Let

`Z_α=2π^(−α)Γ(α)ζ(2α)`

and

`J_α(d,e)=∫_0^∞ y^(α−1)[τ(d²y)τ(e²y)/τ(y)−(1/(de))y^(−1/2)]dy`.

The second integral converges: at zero the bracket is O(1); at infinity the subtracted tail is integrable for α<1/2. No sign is attributed to it.

The regularised Mellin identity of theta is

`∫_0^∞ y^(α−1)[τ(k²y)−k^(−1)y^(−1/2)]dy=Z_α k^(−2α)`.

It is obtained by change of variable and the elementary continuation formula of the Mellin of τ, splitting the integral at 1. There is no sum over zeros.

Since l=de and the counterterms are **identical**, they subtract exactly and one gets

`A_α(d,e)=J_α(d,e)−Z_α(de)^(−2α)>0`.                       (1)

At α=1/4:

`A_(1/4)(d,e)=J_(1/4)(d,e)−[2π^(−1/4)Γ(1/4)ζ(1/2)]/√(de)>0`.

Thus an exact term with weight **1/√(de)** appears without losing the sign of the total cross term. The integral J is not the conductor-1 gamma of the node and the scalar Z does not replace it: identifying the Γ factors by resemblance would not prove the link.

Inequality (1) is a true statement between two explicit quantities. It is not claimed to be the node rewritten nor that its margin dominates a gamma deficit on all tests.

## 5. What remains unpaid: diagonal and same prime

If gcd(d,e)>1, then G₀(d,e)>0 and

`τ(y)Cov_y(X_d,X_e)~y^(−1/2)G₀(d,e)`.

The ordinary integral at α=1/4 diverges positively. Hence the coprime cross terms cannot be assembled with the diagonal into a critical PSD matrix via the same integral without renormalising.

For a finite family of prime powers, the blocks **between distinct primes** have all their cross terms finite and negative after denormalising; the blocks of a single prime need the counterterms of CONSTRUCTOR_002. This is the exact split, not a claim about the number of modes of the node.

One can form a finite Laplacian with weights A_(1/4)>0 and energy `Σ A(d,e)|a_d−a_e|²≥0`; but its diagonal would be a new assignment. **It is not proposed as a certificate**: proving that this diagonal is the required archimedean/polar part would be the whole pending link. This manoeuvre is not counted as an obtained sign object.

## 6. O1 gates

1. **SOS/P1:** (1) requires no pointwise identity μ₀−S_T nor pays Γ via a constant. It does not literally fall under thm:sos. Nor is it an exact factorisation of Q_T; overcoming P1 for the link is not claimed.
2. **BR/W₂:** the BR tests and remainders were not built. This kernel of pairs of divisors is not identified with P36-4 nor with the relaxed set W₂. ρ1‴ is not used.
3. **Specificity:** removing indices from a fixed kernel keeps the sign of the remaining indices; that is NOT changing the Gaussian law to the law with a prime removed. For that modified law neither inheritance nor failure of the anticorrelation has been proved here. Completeness enters the observable identities and the marginal of the next section. The cross sign alone does not pass the falsifier.
4. **Effective domain:** A is defined for coprime pairs of integer indices, not as an operator K(t,t′) on all of PW_T. A realisation producing Q_T and the diagonal/same-prime blocks is missing. There is no conclusion about the full domain, odd part or polar part.

## 7. Mixture of scales: an additional exact cancellation at σ>1

Let α=σ/2>1/2 and

`μ_α(dy)=τ(y)y^(α−1)dy/Z_α`.

It is a probability. Mixing P_y(N=n) against μ_α, the marginal is

`P_α(N=n)=|n|^(−2α)/(2ζ(2α))`, n≠0.

By the complete Euler product, the variables `Y_p=v_p(|N|)` are independent geometric in this marginal. If p≠q, the total covariance formula gives the exact cancellation

`−E_{μ_α}Cov_y(Y_p,Y_q)=Cov_{μ_α}(r_p(y),r_q(y))>0`,

`r_p(y)=E_yY_p=Σ_{j≥1}q_y(p^j)`.

The right-hand side has a genuine two-scale representation:

`(1/2)∫∫[r_p(y)−r_p(z)][r_q(y)−r_q(z)] μ_α(dy)μ_α(dz)`.

Its sign is also seen directly: strict concavity of f implies that each q_y(d) is strictly decreasing in y; hence so is each r_p and both difference factors have the same sign for y≠z. The integrabilities follow from the second moment of log|N| under the zeta law with σ>1 and conditional Jensen.

For a finite family of primes and coefficients a_p one obtains the exact quadratic identity

`Σ_p |a_p|² p^(−σ)/(1−p^(−σ))²`

`=E_{μ_α}Var_y(Σ a_pY_p)+Var_{μ_α}(Σ a_pr_p(y))`.

Both right-hand forms are PSD, but the cross entries of the first are negative and those of the second positive; they cancel **by Eulerian independence**, not by an abstract norm. Deleting a prime keeps a conditioned zeta law with independence on the remaining primes; to require all the original observables one must name the completeness identity that is lost. The cancellation of two surviving primes alone is not specific to total completeness.

### What exactly fails when passing to α=1/4

μ_α ceases to be a probability: its mass at zero diverges like `∫ y^(α−3/2)dy`. The total covariance formula with that normalised measure does not exist at α=1/4. It is not continued as an identity of PSD forms.

**But the individual denormalised cross terms of Theorem 2 do continue as ordinary integrals** because their G₀ is zero. Thus the global PSD mixture breaks at the normalisation/diagonal, while the anticorrelation sign between coprime divisors survives at the critical weight. This is the new and exact distinction allowing work on the cross terms without announcing a Helson-norm transport from σ>1.

## 8. Next link to build

The usable datum is A_(1/4): strict sign, ordinary convergence, two-index dependence and explicit Mellin term 1/√(de). What remains is to obtain from the same object the **renormalised diagonal** and the realisation in the domain of the node, with the correct archimedean and polar sector.

It has not been proved that summing the cross terms pays those terms. Nor has it been proved that a favourable diagonal can be chosen. The positive result of this note is the critical cross term and the mixture identity at σ>1, not the closure of O1 or D.

## 9. All powers of two primes: the critical cross term also converges

The following extension keeps p,q fixed and distinct. **It does not interchange a sum over all primes with Mellin.**

**Lemma 4 (PROVED).** For y≤1/4, c=y^(−1/2)≥2 and coprime integers d,e≥2,

`0<−B_y(d,e)≤min(3/2, 2c/(de))`.

**Proof.** Comparing the decreasing Gaussian sum with its integral gives `τ(k²y)≤c/k`. Poisson gives `τ(k²y)≥c/k−1`. In particular τ(y)≥c−1. By the sign already proved,

`−B=τ(d²y)τ(e²y)/τ(y)−τ(d²e²y)`

`≤c²/[de(c−1)]−(c/(de)−1)=1+c/[de(c−1)]≤3/2`.

Also `−B≤τ(d²y)τ(e²y)/τ(y)≤2c/(de)`. ∎

For distinct primes p≠q, let

`B_y^val(p,q)=τ(y)Cov_y(v_p(|N|),v_q(|N|))=Σ_{j,k≥1}B_y(p^j,q^k)`.

The sums converge for each y>0 and all their terms are negative. Taking `J=ceil(log_p c)`, `K=ceil(log_q c)`, the rectangle j≤J,k≤K contributes O_pq(log²c), and outside it the bound `2c p^(−j)q^(−k)` gives geometric tails O_pq(1). Hence

`0<−B_y^val(p,q)=O_pq(1+log²(1/y))` as y↓0.

When y≥1,

`−B_y^val(p,q)≤[Σ_j τ(p^(2j)y)][Σ_k τ(q^(2k)y)]/τ(y)`

`≤C_pq exp[−π(p²+q²−1)y]`.

The last bound follows from the Gaussian domination of both sums by their first term and `τ(y)≥2exp(−πy)`.

**Theorem 5 (PROVED).** For all α>0 and each fixed pair of distinct primes,

`A_α^val(p,q)=−∫_0^∞ y^(α−1)B_y^val(p,q)dy`

`=Σ_{j,k≥1}A_α(p^j,q^k)∈(0,∞)`.

The equality is Tonelli on nonnegative terms. In particular, **the cross term of two complete prime factors has strict sign and ordinary integral at α=1/4**, not only each truncation in powers.

For 0<α<1/2, formula (1) also sums without ambiguity:

`A_α^val(p,q)=J_α^val(p,q)−Z_α/[(p^(2α)−1)(q^(2α)−1)]`,

`J_α^val(p,q):=Σ_{j,k≥1}J_α(p^j,q^k)`.

Absolute convergence of this last sum follows from `J=A+Z_α(de)^(−2α)`, the positive convergence of ΣA and the two geometric series. At α=1/4 the explicit term is

`−Z_(1/4)/[(√p−1)(√q−1)]`.

Multiplying by log p·log q exactly the critical local factors `log p/(√p−1)` and `log q/(√q−1)` appear. They are not summed here over all p,q; that global tail remains pending.

## 10. Two limits that must not disappear when integrating

- Denormalising by τ cancels the outer factor, but the quotient `τ(d²y)τ(e²y)/τ(y)` **remains**. Only one part of (1) is classical Mellin; the whole kernel is not.
- Theorem 3 proves that A is not w(de) on the domain of all coprime integers. If restricted to pairs of powers of distinct primes, the product determines both factors up to order; on that set any symmetric kernel can be labelled by the product. Do not use that labelling as proof of reduction nor of evasion of Gonek: the effective realisation in heights remains indispensable.

A_α has positive entries; this **does not claim PSD of its matrix**. Nor is the critical B with renormalised diagonal PSD, by the negative sign of its cross terms. The theorems of this note only support the sign and integrability claims explicitly stated.

**Final review AUDIT_004:** theorems accepted with the declared scope;
the distinction between removing indices and changing the law by deletion corrected.
No objections to the proofs of this note remain pending.
