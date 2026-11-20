# POWER_HIGHPASS_015 — Uniform eventual positivity of a rational orbit of fixed dimension

Status: PROVED, independently reviewed in POWER_HIGHPASS_AUDIT_015.md. Positivity of the first members is not claimed, nor uniformity in the dimension. Papers untouched.

## 1. Antecedents and explicit difference

Consulted: the project rules, index/grid/crossword following the previous bridges; entries high-frequency/exterior A001 and high-prolate ROUND010A; COMMON_TRANSFER010, CONFLUENT_BRIDGE014 and SIGNED_TRANSFER014. Generic high-frequency coercivity and its limits on prolate blocks are already on record. Using it to declare all tests or a whole tail of prolate indices positive is not retried.

Here the different object is an EXACT rational orbit: keep N and its numerator space fixed and repeatedly apply Q(s)=s/(s+u). Its norm and frequency scale is identified, the WHOLE comb is controlled by a uniform time weight, and the eventual sign of that WHOLE N-dimensional orbit is proved. No arbitrary carrier condition is deduced from «large frequencies» without verifying it.

## 2. Theorem

Fix u>1; in this phase u=63/2. Let N>=1. For a nonzero real polynomial P, degP<N, define the causal function f_(k,P) by

    F_(k,P)(s)=[s/(s+u)]^k P(s)/(s+u)^N, k=0,1,2,... .

There is an integer K_N, depending on u and N but NOT on P, such that

    W[f_(k,P)]>0 for all k>=K_N and all P!=0,degP<N.   (EVENTUAL)

More precisely, uniformly in the numerators,

    Arch[f_(k,P)]/||f_(k,P)||² >=(1/2)log k−C_N,
    Comb[f_(k,P)]/||f_(k,P)||² ->0,
    Polar[f_(k,P)]/||f_(k,P)||² ->0.                      (U)

For a FIXED P, if r=N−degP>=1, one also obtains the complete asymptotic value

    W[f_(k,P)]/||f_(k,P)||²
       =(1/2)log k+log[u/(2pi)]−(1/2)psi(r−1/2)+o(1).    (ASYM)

No certificate campaign is needed and no information about spectral objects external to the form has been used.

## 3. Gram scaling allowing uniformity in ALL numerators

Write P(s)=Σ(j=0..N−1)a_j s^j and, for k>=1, b_j=a_j k^(j/2). This diagonal transformation is invertible for each k; hence an estimate uniform in b also covers numerators varying with k.

For 0<=eta<u/2, weighting the function by e^(eta y) amounts to evaluating F at s=−eta+i tau. Change tau=sqrt(k)x and put

    d_eta=u(u−2eta)>0,
    W_(k,eta)(x)=
      [(x²+eta²/k)/(x²+(u−eta)²/k)]^k
      [x²+(u−eta)²/k]^-N,
    B_(k,eta)(x)=Σ_j b_j(ix−eta/sqrt(k))^j.

Parseval gives EXACTLY

    k^(N−1/2)||e^(eta y)f_(k,P)||²
       =(1/2pi)∫ W_(k,eta)(x)|B_(k,eta)(x)|²dx.          (GRAM)

The matrices of this quadratic form converge, entrywise and in norm, to

    G_eta[b]=(1/2pi)∫ |x|^-2N exp(−d_eta/x²)
                             |Σ_j b_j(ix)^j|²dx.        (LIMIT)

Each G_eta is positive definite: its weight is positive for x!=0 and no nonzero polynomial can vanish almost everywhere. Since the dimension N is fixed, its smallest eigenvalue is strictly positive.

### Necessary domination, without assuming convergence of densities

Let y=x²+(u−eta)²/k. The quotient factor satisfies

    [(x²+eta²/k)/(x²+(u−eta)²/k)]^k
      =[1−d_eta/(ky)]^k<=exp(−d_eta/y).

On |x|<=1, the shifted monomials are uniformly bounded and exp(−d_eta/y)y^-N is bounded for y>0. This gives an integrable constant majorant on that interval. For |x|>=1, one uses quotient<=1 and the bound C_N|x|^(i+j−2N) for each entry i,j; since i,j<=N−1, the exponent is <=−2. It is integrable. Dominated convergence also yields L¹ convergence of EACH matrix density, not only of their integrals.

In particular, for fixed eta in (1/2,u/2), GRAM/LIMIT and positivity of G_0 give, uniformly in P for k large enough,

    ||e^(eta y)f_(k,P)||² <=C_(N,eta)||f_(k,P)||².        (WT)

Here u>1 is exactly what allows choosing such eta; this condition is not presumed for u merely larger than 1/2.

## 4. Archimedean part: log k plus a bounded block

The symbol satisfies m(tau)=log(|tau|/(2pi))+o(1) as |tau| grows and |m(tau)−log(2+|tau|)|<=C. For x!=0,

    m(sqrt(k)x)−(1/2)log k ->log(|x|/(2pi)).

The corresponding GRAM matrices, inserting this multiplier, also converge. To justify this near x=0, |m(sqrt(k)x)−(1/2)log k| is bounded by C+|log y| with y=x²+u²/k, using the comparability between |x|+2/sqrt(k) and sqrt(y). Multiplying by exp(−u²/y)y^-N keeps a bounded majorant. On |x|>=1, C+log|x| suffices, integrable against |x|^-2.

Thus the Arch matrix minus (1/2)log k times the norm matrix converges to the finite logarithmic form defined by LIMIT. Comparing their norms with the smallest positive eigenvalue of G_0 proves the first inequality of U, uniformly in b and hence in ALL numerators P.

## 5. Each contact vanishes and the complete tail is dominated

For fixed t>0, the correlation is the integral of the unweighted matrix density of §3 against exp(i sqrt(k)xt). This density converges in L¹ to that of LIMIT. By the Riemann–Lebesgue lemma,

    sup_(P!=0) |c_f(k,P)(t)|/||f_(k,P)||² ->0.           (RL)

In detail, the limit density is subtracted in L¹, and the remaining limit is the Fourier transform of an L¹ function at frequency sqrt(k)t; this is done for the N² entries and compared with G_0. RL is not applied without controlling the variation of the density with k.

WT and shifted Cauchy–Schwarz give simultaneously

    |c_f(k,P)(log q)|/||f_(k,P)||² <=C_(N,eta)q^-eta.

Since eta>1/2, Σ(q>=2)2Lambda(q)q^(-eta−1/2) converges. A finite segment, where RL is uniform, is separated from the tail, which is uniformly dominated by this series. This proves that the COMPLETE comb divided by the norm tends to zero uniformly in P. No favourable sign of any contact is assumed.

## 6. The polar term decays exponentially, even uniformly in P

At the moments s=±1/2,

    Q(−1/2)Q(1/2)=−1/[4(u²−1/4)].

Hence Polar[f_(k,P)]=[−1/(4u²−1)]^k Polar[f_(0,P)]. For u=63/2 the factor is −1/3968.

In b coordinates, the initial coefficients are a_j=k^(-j/2)b_j. The two evaluations P(±1/2) are functionals uniformly bounded in b for k>=1; the initial denominators are constants. Hence |Polar[f_(0,P)]|<=C_N||b||². By §3, ||f_(k,P)||²>=c_N k^(1/2−N)||b||² for large k. The uniform bound follows:

    |Polar[f_(k,P)]|/||f_(k,P)||²
       <=C_N k^(N−1/2)(4u²−1)^-k ->0.

u>1 has been used, so 4u²−1>1. This conclusion is not extrapolated to small rates.

## 7. Explicit constant for fixed P

Let D=degP, r=N−D and a_D its leading coefficient. The lower terms vanish after the appropriate scaling. The normalized limit density is proportional to |x|^-2r exp(−u²/x²). Integrating with t=u²/x² gives

    ||f_(k,P)||² ~ |a_D|² k^(1/2−r)
                    u^(1−2r)Γ(r−1/2)/(2pi),
    E log|x|=log u−(1/2)psi(r−1/2).

Combining this with §§4–6 gives ASYM. For the same P, the ratio of weighted norms also has the limit

    ||e^(eta y)f_(k,P)||²/||f_(k,P)||²
       ->[u/(u−2eta)]^(r−1/2),

consistent with WT. These are scaling identities of this rational orbit, not additional regularity hypotheses.

## 8. Scope for the geometric transfer

EVENTUAL controls the whole tail k>=K_N for each FIXED initial dimension N, with all numerators and all contacts. This is a sign result, not only a mixing identity. It can serve as a terminal condition when studying the geometric sums of SIGNED/GEOMETRIC_TRANSFER015.

It does not prove the sign of the first k, nor give K_N uniform as N grows, nor show that positivity of the tail implies positivity of the original mixture. That inference would need to control precisely the initial contributions and their weights. The property is compatible with a form having negative directions outside these tails; it is not presented as closure of the sign on all blocks.
