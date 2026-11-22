# POWER_UNIFORM_STRIP_060 — Uniform contour and sign cone of order n³ log³n

Status: PROVED, independent review approved in POWER_UNIFORM_STRIP_AUDIT_060.md. Papers untouched.

## 1. Results and scope

Fix u=63/2. For n≥1 let q_n be the smallest integer q≥1 such that 2^q≥n+1, and define

    J(n)=10^12 (n q_n)^3.

For EVERY nonzero real polynomial P of degree<n, EVERY integer j≥J(n) and

    F(s)=Q(s)^j P(s)/(s+u)^n, Q(s)=s/(s+u),
    ρ(z)=z^(2j)P(iz)P(−iz)/(u²+z²)^(n+j),

it is proved that

    ∫_R |ρ(x+3i)|dx <2∫_R ρ(x)dx,                      (STRIP3)
    W[F] > ||F||².                                      (CONE)

The constant of STRIP3 is independent of n and of P. The integer q_n is O(log(n+1)); the threshold is O(n³ log³n). Since q_n≤n, the simpler polynomial threshold j≥10^12 n^6 also suffices.

Not claimed: sign for j<J(n), sufficiency of a quadratic cone for all numerators, or global closure. The result NECESSITY059 only required p≥2 for a uniform STRIP and does not contradict this larger threshold.

## 2. Corpus and specific difference

Consulted the project rules, ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; reread HIGHPASS015, JOINT_SCALE016, QUADRATIC/QUADRATIC_EXPLICIT017, INVERSE_COEFFICIENT054 and EFFECTIVE_HIGHPASS054. 015 already offers eventuality at fixed dimension; 054 makes it effective at variable dimension at the cost of a very large constant D_n. 016 prevents uniformizing in n the separate exponential time norms; it does not prevent STRIP for the joint density.

The new difference is to control derivatives of an amplitude WITHOUT the causal phase via orthogonal polynomials of the exact Student weight. Absolute monomial coefficients are not used for the Taylor segment. The coarse bound D_n of 054 is used only for the TAIL of that series, with truncation degree chosen in advance. The degrees grow under differentiation and are accounted for explicitly. No norm of a generator restricted to a finite space is exponentiated, and the Student weight is not globally replaced by a Gaussian.

## 3. Orthogonal polynomials of the exact Student weight

Let M=n+j, j≥n+8 and

    w(y)=(1+y²/j)^−M.

The scalar product is ∫p conjugate(q)w. All necessary moments up to degree n+3 exist, since M>n+3+1/2. By Gram–Schmidt on 1,y,y²,... one obtains monic polynomials p_k, of parity k.

The operator

    L=−(j+y²)∂²+2(M−1)y∂
      =−w^−1 ∂[(j+y²)w∂]

is symmetric on these polynomials. The integration-by-parts boundaries vanish by the decay of the weight. It preserves degree and its leading coefficient is

    λ_k=k(2M−k−1).

Symmetry and orthogonality imply Lp_k=λ_k p_k, as in the polynomial lemmas 049. If p_k=y^k+c_k y^(k−2)+..., comparing the degree-(k−2) coefficient gives

    c_k=−j k(k−1)/[2(2M−2k+1)].

The three-term recurrence, by orthogonality and parity, is

    y p_k=p_(k+1)+β_k p_(k−1),
    β_k=||p_k||²/||p_(k−1)||²
       =c_k−c_(k+1)
       =j k(2M−k)/[(2M−2k+1)(2M−2k−1)].              (REC)

For 1≤k≤n+2, j≥n+8 ensures 2M−2k−1≥2j−5≥j and M≤2j. Therefore

    0<β_k≤4k.

In the orthonormal basis, multiplication by y is the sum of a degree-raising and a degree-lowering operator, with coefficients √β. For any S of degree d≤n+1,

    ||yS||_w≤4√(d+1)||S||_w.                            (MULT)

Also, expanding R of degree<n in the eigenpolynomials of L gives

    ∫(j+y²)|R′|²w≤λ_(n−1)||R||_w²,
    ||R′||_w²≤3n||R||_w².                              (DER)

The factor j of the differential form is not lost in this last step.

## 4. Exact first derivative of the amplitude without phase

For a COMPLEX polynomial p of degree<n, define the function holomorphic in |Imz|<u

    H(z)=z^j p(z)/(u²+z²)^((n+j)/2).

The branch of the denominator is the positive one on the real line; it exists on the whole strip because Re(u²+z²)>0 there. Set a=u√j and R(y)=y^(n−1)p(a/y). The change τ=a/y on both half-lines gives

    ||H||_(L²(R))²=a^(1−2n)||R||_w².

Differentiating and making the same change gives exactly

    ||H′||²=a^(−1−2n)||A_(n,j)R||_w²,
    A_(n,j)R=y²R′+yR−M y³R/(j+y²).                     (GEN)

This is conjugation by the unitary half-density change: the real translation generator is −(y²∂+y)/a. The norm identity is verified on each half-line; the constant phase or sign factors there do not affect the norm.

From MULT applied twice to R′ and three times to R, and from DER,

    ||y²R′||_w≤28(n+2)^(3/2)||R||_w,
    ||yR||_w≤4(n+2)^(3/2)||R||_w,
    ||M y³R/(j+y²)||_w≤128(n+2)^(3/2)||R||_w.

In the last step M/j≤2. One obtains the loose bound

    ||H′|| ≤ [200(n+2)^(3/2)/(u√j)]||H||,
    j≥n+8.                                             (FIRST)

It is a first-derivative inequality with the exact rational weight, not a Gaussian approximation nor an assumed estimate for the full translation.

## 5. Coarse height-15 bound for a single amplitude

It is necessary to distinguish a complex amplitude from the density of the product. The STRIP054 bound for a generic product is NOT identified without proof with ||H(·+15i)||².

Instead the SINGLE evaluation of INVERSE_COEFFICIENT054 is used: with H_0=∫|R(y)|²w(y)dy and C_n=9n²9^n,

    |R(Y)|²≤C_n H_0 Σ_(r=0)^(n−1)|Y|^(2r).

Exactly,

    |H(z)|²=a^(−2n+2)|z|^(2(n+j−1))|R(a/z)|²
                         /|u²+z²|^(n+j).

For j≥10000n², each term of SINGLE is a scalar density 017 with parameters N′=r+1, k′=j+n−1−r. Its integral over Imz=±15 is ≤5 times its real integral. The case N′=1 was justified in EFFECTIVE_HIGHPASS054§3 by WR11 and Cauchy; it is not inherited without proof from the condition N′≥2.

The moments M_r=∫y^(2r)w(y)dy satisfy ΣM_r≤2n! by 054. The powers of a cancel exactly as there. Therefore, for EVERY complex p of degree<n,

    ||H(·±15i)||²≤D_n||H||²,
    D_n=10C_n n!=10n²9^(n+1)n!.                        (COARSE)

The causal time norms of the original problem were not separated. COARSE is an estimate of an amplitude without phase in frequency and is derived directly from SINGLE and the scalar diagonals.

## 6. Cauchy in L² and Taylor tail

For |η|≤15, write N(η)=∫|H(x+iη)|²dx. Differentiating and integrating by parts produces

    N″(η)=4∫|H′(x+iη)|²dx≥0.

All boundaries vanish by the rational decay; H and its derivatives are square-integrable uniformly on closed substrips. Convexity and COARSE at both ends imply N(η)≤D_n N(0), without requiring real coefficients or symmetry of H.

For complex ζ with |ζ|≤15, real translation in x does not change the norm; thus

    ||H(·+ζ)||≤√D_n||H||.

The map ζ→H(·+ζ) is holomorphic with values in L² inside the strip. This can be verified directly with pointwise Cauchy and uniform domination of the tail |x|→∞. Cauchy and Minkowski give for each r≥0

    ||H^(r)||/r!≤√D_n 15^−r||H||.

Therefore, at height η=±3, the Taylor tail from index L satisfies

    ||Σ_(r≥L)(iη)^r H^(r)/r!||
      ≤(5/4)√D_n 5^−L||H||.                            (TAYLOR-TAIL)

Convergence is in L². This bound is not deduced by repeating FIRST indefinitely.

## 7. Finite Taylor segment, with controlled growing degrees

Let q=q_n and fix BEFORE estimating

    L=20nq, j≥10^12(nq)^3.

The definition of q gives n≤3^q. Using n!≤n^n, n²≤3^(2q), 10<27 and 9^(n+1)=3^(2n+2), one obtains

    D_n<3^(nq+2q+2n+5)≤3^(10nq).

The last inequality holds for all n,q≥1: its difference is 9nq−2q−2n−5, minimal at q=1 and there equal to 7(n−1). Thus TAYLOR-TAIL is less than

    (5/4)3^(5nq)5^(−20nq)||H||
      <(5/4)3^(−15nq)||H|| <||H||/100.                 (TAIL-SMALL)

The first derivatives are also controlled without a fictitious fixed dimension. If H belongs to the class (n,j),

    H′(z)=z^(j−1)[j u²p+z(u²+z²)p′−n z²p]
                         /(u²+z²)^((n+j+2)/2).

The bracketed numerator has degree ≤n+1<n+3. Therefore H′ belongs to the class (n+3,j−1). After r derivatives the class (n+3r,j−r) is used, never the original.

For 0≤r<L, one has j−r≥j/2 and j−r≥n+3r+8. Also n+3r+2≤63nq. FIRST at each step gives a norm ratio less than

    200(63nq)^(3/2)√2/(u√j)<1/100.

For example √63<8, √2<2 and √j≥10^6(nq)^(3/2) reduce the comparison to 201600/31500000<1/100. One obtains ||H^(r)||≤100^−r||H|| for r≤L. Hence the Taylor segment at height ±3 has norm less than or equal to

    Σ_(r=0)^(L−1)(3/100)^r/r! ·||H||
       ≤exp(3/100)||H||≤(100/97)||H||.

Adding TAIL-SMALL produces

    ||H(·±3i)|| <(100/97+1/100)||H||
                    <(11/10)||H||.                     (AMP3)

This is the point that recovers the cancellations of the polynomial in norm. The large constant D_n paid only for the Taylor tail, whose start L grows like n logn; it did not multiply the segment that determines AMP3.

## 8. Full density and uniform STRIP

For the real numerator P of the problem, take p(z)=P(iz) in the definition of H. Let H#(z)=overline(H(overline z)). Then EXACTLY

    ρ(z)=H(z)H#(z).

On the line, ρ(x)=|H(x)|². On the shifted line the product is not confused with a square: Cauchy gives

    ∫|ρ(x+3i)|dx
      ≤||H(·+3i)||·||H(·−3i)||
      <(121/100)||H||²<2∫ρ(x)dx.

This proves STRIP3 for all numerators simultaneously. The same argument even allows complex coefficients with the corresponding sesquilinear product; CONE is stated only for the required real class.

## 9. Full form: ARCH, infinite comb and polar

Shifting the contour of the rational density, analytic in |Imz|<u, and using STRIP3 implies

    |c_F(t)|≤2exp(−3|t|)||F||².

For t<0 the lower strip is used. The vertical edges tend to zero by the at least quadratic decay of ρ. Therefore the WHOLE comb satisfies, with Λ(m)≤m,

    |Comb[F]|/||F||²
      ≤4Σ_(m≥2)Λ(m)m^(−7/2)
      ≤4Σ_(m≥2)m^(−5/2)
      ≤7/(3√2)<2.                                       (COMB)

The last sum is bounded by its first term plus the integral from 2; no infinite cosine symbol is summed and no contacts are omitted.

MULT applied to R in inverse frequency gives ∫y²|R|²w≤16n∫|R|²w. Thus

    E_F[τ^−2]≤16n/(u²j)≤1/(10000u²),

since the current threshold implies j≥160000n. Jensen, Cauchy and the symbol bound of 017 give

    ARCH[F]/||F||²
      ≥−(1/2)log Eτ^−2−log(2π)−√(Eτ^−2)−Eτ^−2/2
      ≥log(100u/(2π))−1>4.                              (ARCH)

Indeed π<4, 100u/8>243=3^5>exp5 and the inverse penalty is <1.

The POLAR bound of EFFECTIVE_HIGHPASS054§7 was already proved for ALL j≥10000n², without using its huge sign threshold. Therefore it applies here and gives

    |Polar[F]|<||F||².                                  (POLAR)

Combining ARCH, COMB and POLAR in the SAME norm proves W[F]>(4−2−1)||F||²=||F||², proving CONE.

## 10. Scope

The huge cutoff 054 is replaced by an explicit cone of growth n³ log³n, valid for ALL numerators of dimension n. The contour bound is uniform and was obtained keeping the amplitude without phase and the exact product of the density; 016 is not evaded by assuming a uniform weighted causal norm.

The interior j<J(n) remains undecided. No global positivity is derived from the recurrences 016/036, no uniform quadratic cone for all P is claimed and no time window T of Paper 46 is extended. There were no numerical campaigns nor parameter selection by floating-point eigenvalues. Papers untouched.
