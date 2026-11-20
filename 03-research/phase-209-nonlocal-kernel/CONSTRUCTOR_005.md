# CONSTRUCTOR_005 — Exact positive completion of −R_α

2026-10-18. Pure mathematics. **PROVED, favourable final audit in AUDIT_005 §11:** for 0<α<1/2, the renormalised kernel **−R_α is positive definite on every finite family of distinct divisors d≥2**, not only between distinct primes. An exact decomposition of its diagonal, same-prime blocks and cross terms is built. **No link with Q_T has been proved. Row D remains OPEN.**

## 0. Corpus check and written new reason

Read: the project rules, README209 and audits, ROUTES-TRIED-INDEX index (README, recent 209 entries and families), residues 06, P1_BBSTAR, SPEC005, master grid and crossword. Additional targeted search: `renormal.*covarian`, `masa faltante`, `Haar.*theta`, `Mellin.*profini`, `gcd.*zeta`, `covarian.*renormal`. This identity was not identified in the consulted entries; this is not a declaration of global priority.

Clashes: R183_008 (semilocal gcd Gram), Helson/Bohr, SPEC005 C-hom, P1 and certificates of the form itself. **Exact new reason:** the already defined kernel R is kept; it is not replaced by a favourable Gram. An algebraic covariance identity and the Mellin of a *signed difference* of masses produce its renormalised diagonal and prove **−R**, with prefixed sign, as a PSD sum. The key positivity is `−2π^(−α)Γ(α)ζ(2α)>0` on 0<2α<1, obtained without zeros. The profinite space is used only to prove positivity of an explicit matrix on finitely many divisors; the Bohr lift is not proposed as a source of sign for Q_T.

The difference with respect to CONSTRUCTOR_002 is that there R=I+H had signed H without control. Here the comparison identity is changed, keeping exactly R and all its counterterms. The difference with respect to a generic norm is the **explicit equality with the previously fixed renormalised kernel**, not the mere existence of some root.

## 1. Definitions kept

`τ(y)=Σ_{n∈Z\{0}}exp(−πn²y)`, `c(y)=y^(−1/2)`.

`q_d(y)=τ(d²y)/τ(y)`, `X_d(N)=1_{d|N}` under `P_y(N=n)=exp(−πn²y)/τ(y)`.

For d,e≥2 and l=lcm(d,e):

`B_y(d,e)=τ(y)[q_l(y)−q_d(y)q_e(y)]`,

`G_1(d,e)=1/l−1/(de)`,

`D_y(d,e)=c(y)G_1(d,e)−B_y(d,e)`.

For 0<α<1/2:

`R_α(d,e)=∫_0^∞ y^(α−1)[B_y(d,e)−c(y)G_1(d,e)]dy`.

Entrywise convergence was proved in CONSTRUCTOR_002: the bracket is O(1) at zero and O(y^(−1/2)) at infinity. The same subtraction scheme is fixed; a diagonal is not changed at will.

Write s=2α∈(0,1) and

`Z_α=2π^(−α)Γ(α)ζ(2α)`.

**Elementary sign:** ζ(s)<0 for 0<s<1, since the alternating series η(s)=Σ_{n≥1}(−1)^(n−1)n^(−s) is positive and `ζ(s)=η(s)/(1−2^(1−s))`. Hence **Z_α<0**. Only a real value is used, no information about zeros.

## 2. The arithmetic space: geometric laws on finite valuations

Let S be any finite set of primes. For t>0, I define P_t on `(v_p)_{p∈S}∈N_0^S` by independence and

`P_t(v_p=j)=(1−p^(−t))p^(−tj)`.

For d supported on S, `E_t X_d=d^(−t)` and `E_t X_dX_e=lcm(d,e)^(−t)`. The laws are compatible when enlarging S, but the proof only uses finite sets.

For a divisibility polynomial

`A(N)=Σ_{d∈E}a_d X_d(N)`, E finite,

I define `μ_t(A)=E_t A=Σ a_d d^(−t)`. In particular μ_1 is the uniform divisibility mean (Haar on profinite cylinders).

**Warning:** P_s for s<1 is not a normalisable zeta probability on the positive integers. It is a law on the finitely many observed valuations. An infinite product is not interchanged with a divergent series of integers.

## 3. Exact algebraic identity before integrating

I define a signed functional on the finite algebra of divisibility observables:

`ν_y(H)=c(y)E_1H−τ(y)E_yH`.

It is not claimed that ν_y is positive; in fact D_y may be indefinite when mixing several primes. A global measure ν_y on the integers is not needed.

**Lemma 1 (PROVED).** For all A of finite support,

`D_y(A):=Σ conjugate(a_d)a_e D_y(d,e)`

`=ν_y(|A−μ_1(A)|²)+τ(y)|E_yA−μ_1(A)|²`.             (2)

**Proof.** The left-hand side is `c Var_1(A)−τ Var_y(A)`. Expand the first right-hand term:

`ν_y(|A−μ_1|²)=c Var_1(A)−τ[Var_y(A)+|E_yA−μ_1|²]`.

Add the second term. It is an identity of complex numbers and their moduli; no sign has been used. ∎

The point of this comparison is that the centre μ_1 is constant in y. The Gaussian mean is not subtracted inside the signed functional when integrating.

## 4. Mellin of the mass defect: exact sign and formula

**Lemma 2 (PROVED).** For k≥1 and 0<α<1/2,

`∫_0^∞ y^(α−1)[c(y)/k−τ(k²y)]dy=−Z_α k^(−2α)`.       (3)

**Proof.** For k=1, Poisson gives `c−τ=1−c τ(1/y)`, which is O(1) at zero and O(c) at infinity. The integral converges. Splitting at y=1 and comparing with the elementary continuation of `∫ τ(y)y^(α−1)dy` from α>1/2 gives `−Z_α`. That continuation can also be taken as the definition of the regularised Mellin: the subtracted terms coincide exactly. For general k change u=k²y; the bracket becomes `u^(−1/2)−τ(u)` and k^(−2α) appears. ∎

For an observable H of the finite algebra, expand it as a finite combination of X_k, including X_1=1. Since `ν_y(X_k)=c/k−τ(k²y)`, one obtains

`∫_0^∞ y^(α−1)ν_y(H)dy=−Z_α E_sH`, s=2α.            (4)

Each integral in this expansion converges absolutely; ν_y need not be positive before integrating. If H≥0 on the finite valuations, the right-hand side is nonnegative. This is the source of sign that was missing when analysing the signed difference.

## 5. PSD completion of the whole renormalised kernel

**Theorem 3 (PROVED).** For 0<α<1/2 and A=Σ a_dX_d of finite support,

`−R_α(A)= (−Z_α) E_s|A−μ_1(A)|²`

`          +∫_0^∞ y^(α−1)τ(y)|E_yA−μ_1(A)|²dy ≥0`.   (5)

**Proof.** Integrate (2). The first integral is (4) applied to H=|A−μ_1|². The second converges: at zero, for each fixed d, `q_d=1/d+O_d(√y)`, so the difference of means is O_A(√y), and the integrand without power is O_A(√y). At infinity, q_d is bounded and τ decays exponentially. Both right-hand forms have a sign by `−Z_α>0` and positivity of P_s. ∎

For distinct indices d≥2, the form is **positive definite**. If the first term were zero, A=μ_1(A) on all finite valuation patterns, since P_s gives them positive probability. At N=1 one obtains μ_1=0. Evaluating successively at the indices of E in increasing order, `A(d)=Σ_{e∈E,e|d}a_e` forces by induction each a_d=0. Hence a nonzero coefficient vector gives a strictly positive first term.

### Completely explicit kernel

I define

`H_s(d,e)=lcm(d,e)^(−s)−d^(−s)/e−e^(−s)/d+1/(de)`,

`Π_α(d,e)=∫_0^∞ y^(α−1)τ(y)[q_d(y)−1/d][q_e(y)−1/e]dy`.

Then

`−R_α=(−Z_α)H_s+Π_α`.                               (6)

Moreover,

`H_s=G_s+v_s v_s*`,

`G_s(d,e)=lcm(d,e)^(−s)−(de)^(−s)`,

`v_s(d)=d^(−s)−d^(−1)`.

G_s is the covariance of the indicators under P_s and Π_α is the explicit Gram of their Gaussian deviations from the Haar mean. Thus

`−R_α=(−Z_α)G_s+(−Z_α)v_s v_s*+Π_α`,                 (7)

with three identified PSD forms and no remaining signed term.

**Critical case α=1/4:** s=1/2, `−Z_α=−2π^(−1/4)Γ(1/4)ζ(1/2)>0`. The identity pays exactly the diagonal and the same-prime blocks of the kernel R that was already defined. It does not identify that gamma-zeta scalar with the archimedean part of Q_T.

## 6. Previous block result, now explained and strengthened

The following argument was found before (5) and serves as an independent control for powers of one prime.

Punctured concavity implies q_y(p)<1/p. Poisson gives, for u>0,

`τ(u)−τ(p²u)<u^(−1/2)(1−1/p)`.

Indeed the defect with respect to the right-hand side is

`u^(−1/2)[τ(1/u)−p^(−1)τ(1/(p²u))]<0`.

Hence the Gaussian masses of each valuation shell,

`w_j=τ(p^(2j)y)−τ(p^(2j+2)y)`,

are strictly dominated by `c(1−1/p)p^(−j)`, the masses of cP_1. For any observable of one valuation, the unnormalised covariance is

`mass·Var(A)=min_z Σ_j mass_j|A_j−z|²`.

This expression increases when each mass increases; hence D_y≥0 on each block of one prime, before integrating. It is strict for non-constant observables. For several primes, that mass domination may fail and D_y is not PSD at each scale. **Identity (5) uses the positivity of the integrated Mellin of ν, not a false pointwise domination.**

## 7. Link with the cross terms and with the Euler product

For powers of distinct primes, G_s(d,e)=0 because lcm=de. By (7), the positive critical cross terms of −R computed in CONSTRUCTOR_004 are

`(−Z_α)v_s(d)v_s(e)+Π_α(d,e)`.

Both terms are entrywise positive, since v_s(d)>0 on 0<s<1 and `q_d−1/d<0` by punctured concavity. This reproduces their sign without assigning an artificial Laplacian diagonal.

For powers of the same prime, G_s is exactly the covariance of its geometric distribution with parameter p^(−s). Thus the completion is not only entrywise: it gives the correct covariance blocks within the same formula.

Identity (5) uses arithmetic of all integers and their divisibility densities; P_s incorporates the Euler product over the observed primes. **Specificity for Q_T not obtained:** §10 proves that removing finitely many primes produces a conditioned law that keeps this positivity, with another mass and another theta. The formula does not prove that the positivity of Q_T for conductor 1 transfers nor identifies which term of the link would fail. The computation of that link is still necessary.

## 8. Domain and scope: what was achieved, what was not

An **exact positive completion of the renormalised arithmetic kernel −R_α on c_00 of divisors** was obtained, with all modes of that algebraic space included. Its Hilbert completion can be defined via (5), but a non-compact height operator in the domain required by O1 has not yet been built.

It is not claimed that the norm so defined is equivalent to a prefixed coefficient norm, nor that an infinite series over all primes belongs to the domain. A global sum is not integrated without tail control.

No map U_T from the tests of the node has been identified such that `Q_T(F)=−R_(1/4)(U_TF)+positive remainder`, nor an equivalent proved domination. The geometric covariance, the term v_s and Π_α are not by definition the gamma, the comb and the pole of the paper. They are not labelled so by analogy.

Hence the auxiliary goal of this round **is resolved**: sign of R (negative definite) and genuine positive completion of the kept object. The main goal D remains active. The concrete residue is a realisation of (7) on the tests F, with exact identity of the terms and domain/tails, linking this distinct object to Q_T without introducing its square root nor assuming its sign.

## 9. Programme gates

- **thm:sos:** (5) does not pay the pointwise comb by μ₀−S_T nor ask the archimedean part for a constant. It does not fall under that statement by form. Nor has a def:PD certificate for Q_T been built.
- **P1:** the positive identity corresponds to R, an object defined independently by a renormalised integral; not to an abstract root of Q_T. If U_T is proposed, its link must be proved, not its abstract existence.
- **W₂/BR:** the tests/remainders of those schemes have not been built. The kernel on integer indices is not presented as an effective height kernel by mere renaming.
- **Functional equation:** Poisson intervenes in convergence and in the complete Mellin; no asymptotic Gonek identity is used nor is a remainder suppressed.
- **Polar sector:** the appearance of the rank one v_s is explicit. It has not been proved that it corresponds to cosh(x/2); it is neither eliminated nor identified without a map.

**Final status: PSD COMPLETION PROVED for −R_α (0<α<1/2), favourable final audit. Link with Q_T and row D: OPEN, active work.**

## 10. Specificity test: the completion also survives deleting primes

Let P>1 be squarefree, `δ_P=∏_{p|P}(1−1/p)` and

`τ_P(y)=Σ_{n≠0,(n,P)=1}exp(−πn²y)=Σ_{a|P}μ(a)τ(a²y)`.

Its main mass is δ_P c(y); the constant term disappears because `Σ_{a|P}μ(a)=0`. For indices d,e coprime to P, we define q_d^P, B_y^P as before using τ_P and

`R_α^P(d,e)=∫_0^∞ y^(α−1)[B_y^P(d,e)−δ_P c(y)G_1(d,e)]dy`.

The integrals converge for 0<α<1/2: at zero the cancellation is even exponential; at infinity the tail y^(−1/2) suffices. The centre μ_1 is still Σa_d/d on the surviving indices.

For `ν_y^P=δ_P c E_1^P−τ_P E_y^P`, where P_t^P fixes v_p=0 for p|P and keeps the other geometrics, inclusion–exclusion and (3) give

`∫_0^∞ y^(α−1)ν_y^P(X_k)dy`

`=−Z_α k^(−s)∏_{p|P}(1−p^(−s))=−Z_α^P E_s^P X_k`,

`Z_α^P:=Z_α∏_{p|P}(1−p^(−s))<0`, `(k,P)=1`.

Repeating exactly Lemma 1:

`−R_α^P(A)=(−Z_α^P)E_s^P|A−μ_1(A)|²`

`            +∫_0^∞ y^(α−1)τ_P(y)|E_y^P A−μ_1(A)|²dy ≥0`.

It is positive definite on finite families of distinct indices d≥2 coprime to P. Indicators containing deleted primes vanish in this law and are not counted as strict directions.

**Result of the test:** the complete auxiliary positivity is **inherited by every finite deletion** with its corresponding theta and density. The theorem of §5 remains valid and independent, but its sign alone does not separate the conductor-1 form from the falsifier. The extra premise of the link must use the full self-dual FE of θ_Z and the identity of its archimedean part/pole; this PSD completion is not enough.

This conclusion is not used as a general NO-GO: a specific link that fails for τ_P could still serve. It must be built explicitly, including the self-duality defect, instead of being inferred from (5).
