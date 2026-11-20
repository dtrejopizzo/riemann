# POSITIVE_ASSOCIATION_002 — Strict association of divisibility under theta

2026-10-18. Independent proof to audit CONSTRUCTOR_002.
**PROVED / partial positive tool. No sign of the node proved.**

## Corpus and attribution

Targeted searches in the index for geometric convexity of theta, association and divisibility correlations did not identify this formulation. Nearby items: SPEC005 (C-hom, generic theta-Bochner), R183_008 (semilocal gcd Gram), R11_2_ORIGIN (polar/origin). The explicit difference: the generic PSD of a covariance is not used, but rather the sign of each cross correlation; the theta quotient has degree zero; the sign can break for the measure corresponding to a removed Euler factor. This allows examining the corollary, without reopening the earlier routes as a proof of the node.

Theta convexity is classical, not new: primary source communicated and verified, Faulhuber–Steinerberger, arXiv:1601.02972, Theorem 2.3, https://arxiv.org/html/1601.02972 . An elementary self-contained proof is given below so as not to depend on a citation from memory. No novelty of the association corollary in the literature is claimed.

## 1. Strict geometric convexity of theta

Let θ(y)=Σ_{n∈ℤ} exp(−π y n²), y>0; h(x)=log θ(e^x). Then h''(x)>0.

Proof for y=e^x≥1. Under the discrete Gaussian probability μ_y(n)=exp(−π y n²)/θ(y), write m=E(n²). Absolute differentiation of the series gives

    h''(x)=π² y² Var(n²)−π y m.

One has E(n⁴)≥m, hence Var(n²)≥m(1−m). Moreover θ≥1 and, with q=e^(−π)<1/20,

    0<m≤2 Σ_{n≥1} n² q^(n²)≤2 Σ_{n≥1} n² q^n
       =2q(1+q)/(1−q)³ < 840/6859 < 1/2.

Hence h''≥π y m [π y(1−m)−1]>0, since π/2>1. For y≤1, Poisson θ(y)=y^(−1/2)θ(1/y) implies h(x)=−x/2+h(−x), hence h''(x)=h''(−x)>0. ∎

Poisson is used effectively to transfer the sign from y≥1 to y≤1; no generic norm is symmetrised.

## 2. Correlation of two divisibilities

For integers d,e≥2, let I_d(n)=1_{d|n}, taking d|0. Its probability under μ_y is q_d(y)=θ(d²y)/θ(y). For ℓ=lcm(d,e),

    C_y(d,e)=Cov_μy(I_d,I_e)
       =θ(ℓ²y)/θ(y)−θ(d²y)θ(e²y)/θ(y)² >0.

Proof. With x=log y, a=2log d>0 and b=2log e>0,

    h(x+a+b)+h(x)−h(x+a)−h(x+b)
       =∫_0^a ∫_0^b h''(x+u+v) dv du >0.

Exponentiating,

    θ((de)²y)θ(y)>θ(d²y)θ(e²y).

Since ℓ≤de and θ is decreasing, θ(ℓ²y)≥θ((de)²y). The strict inequality above proves C_y(d,e)>0. ∎

The sign is not the PSD of the covariance matrix: PSD holds for every probability, while an individual cross covariance can be negative.

## 3. A prime deletion breaks the cross sign

Let p be prime and μ_y^(p) the probability proportional to exp(−π y n²) on n∈ℤ with p∤n. Its normalisation is

    Z_p(y)=θ(y)−θ(p² y)>0.

For d coprime to p,

    q_d^(p)(y)=[θ(d²y)−θ(p²d²y)]/Z_p(y).

Let d,e≥2 be coprime to each other and to p. As y→∞,

    Z_p(y)=2e^(−π y)(1+o(1)),
    q_d^(p)(y)=e^(−π(d²−1)y)(1+o(1)),
    q_de^(p)(y)=e^(−π((de)²−1)y)(1+o(1)).

Since

    ((de)²−1)−(d²+e²−2)=(d²−1)(e²−1)>0,

it follows that

    Cov_μy^(p)(I_d,I_e)
       =−e^(−π(d²+e²−2)y)(1+o(1))<0

for all sufficiently large y. Explicit example: p=5, d=2, e=3. No numerical threshold is required for the proved asymptotic claim.

This conditioning really corresponds to the removed factor: for Re s>1,

    ∫_0^∞ Z_p(y)y^(s/2−1)dy
       =2π^(−s/2)Γ(s/2)ζ(s)(1−p^(−s)).

The identity follows by termwise integration over positive integers not divisible by p. The mass at zero has been lost, but here it is proved that this loss changes the sign of a correlation; that sign is not attributed to the polar term of Q_T.

## 4. Exact scope

There is an independent positive result specific to an arithmetic distribution with Poisson: all the cross covariances above are strictly positive and a concrete prime deletion makes them negative. The object is not just a generic norm. Even so:

- It is a statement about Gaussian divisibility, not yet about the Λ coefficients of the node.
- The variable y and the indices d,e are not automatically Mellin heights t,t′; the translation remains to be done.
- No identity or domination of Q_T by these correlations has been proved. Signed weights and logarithmic derivatives may lose positivity.
- The limit y↓0 is C_y(d,e)→(gcd(d,e)−1)/(de); for coprime d,e, the strict positivity sits in a small correction that must not be discarded.
- The sign failure was proved for a complete conditioning and large y, not for every p,T nor for every window of the node.

**Partial positive result PROVED; link with Q_T OPEN.** This note offers a concrete sign to audit, without declaring the O1 goal or the final sign fulfilled.

## 5. Independent check of the origin: decisive limit of the positive result

**PROVED.** The atom n=0 explains a positive rank-one contribution. Let p₀=μ_y({0})=1/θ(y), μ_y^*=μ_y conditioned on n≠0, and r_d=E_μy* I_d. The law of total covariance gives exactly

    C_y(d,e)=(1−p₀) C_y^*(d,e)
       +p₀(1−p₀)(1−r_d)(1−r_e).

The last term is a positive rank-one matrix. On finite coefficients a_d with Σ_d a_d(1−r_d)=0, its contribution to Σ a_d conjugate(a_e)C_y(d,e) vanishes and only the conditioned covariance remains, whose PSD is generic.

For coprime d,e greater than 1, also C_y^*(d,e)<0 for large y: the same asymptotics of §3 hold without excluding multiples of p. Hence the sign change of the deletion does not by itself identify a complete Euler effect; removing only the origin already destroys the cross association. The proof of §2 remains an exact positive result, but it does not establish that the useful sign survives the removal of the origin mode.

**There is no proved identification between this rank one and the polar term of Q_T.** Until it is constructed, it cannot be claimed either that the cosh orthogonal kills it automatically. R11_2_ORIGIN already requires controlling this point before turning a property of the theta origin into a mechanism for the node.

Corrected scope conclusion: the association positive result exists and is specific to the complete theta distribution; the claim that it provides a new arithmetic sign for the polar orthogonal remains **OPEN, with no evidence for now**. Do not use the failure after deleting p as sufficient proof of an evasion of the origin barrier.
