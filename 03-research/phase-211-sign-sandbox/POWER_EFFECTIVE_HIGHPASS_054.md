# POWER_EFFECTIVE_HIGHPASS_054 — Explicit variable-dimension cutoff for the complete form

Status: PROVED, independent review approved in POWER_EFFECTIVE_HIGHPASS_AUDIT_054.md. It does not require evaluating the gigantic integer of the cutoff. Papers untouched.

## 1. Statement and difference

Fix u=63/2 and Q(s)=s/(s+u). For each integer n≥1 define the explicit integers

    C_n=9n²9^n,
    D_n=10C_n n!,
    A_n=6C_n n n!,
    K(n)=max{10000n², A_n·3^(4D_n+20)}.

For EVERY non-zero real polynomial P of degree<n, F0=P/(s+u)^n and EVERY integer j≥K(n), we prove

    W[Q^jF0] > ||Q^jF0||².                              (EFFECTIVE)

The cutoff grows very fast; it is not claimed to be polynomial nor is it optimized. The new datum is that it is given by explicit integer operations and covers ALL numerators simultaneously at variable dimension.015 already proved eventuality at fixed dimension without this cutoff. The present argument avoids a non-effective Gram limit: it uses INVERSE_COEFFICIENT054, an explicit uniform bound in inverse frequency, and the audited SCALAR contour017 applied to positive diagonals. It does not separate two exponential norms of dimension n nor contradict the obstruction016.

Consulted the ROUTES-TRIED-INDEX index, grid R162_2300_MASTER_GRID, CROSSWORD-TO-D and the antecedents described in INVERSE_COEFFICIENT054. The contour method017, the symbol bound of017 and the eventuality015 are not presented as new. The change of object and the new effective inequality are COEFF054 and its integration with the exact moments of this memo.

## 2. Explicit inverse-frequency moments

For j≥n, put a=u√j, R(y)=y^(n−1)P(ia/y),

    w(y)=(1+y²/j)^−(n+j),
    H=∫|R(y)|²w(y)dy,
    M_r=∫y^(2r)w(y)dy.

INVERSE_COEFFICIENT054 proves

    ||Q^jF0||²=a^(1−2n)H/(2π),
    (Σ|coef R|)²≤C_nH.                                 (COEFF)

For integers0≤r≤n−1, one has the effective bound

    M_r≤Γ(r+1/2),   Σ_(r=0)^(n−1)M_r≤2n!.              (MOMENTS)

Proof. The exact beta integral is

    M_r=j^(r+1/2)Γ(r+1/2)Γ(b)/Γ(b+r+1/2),
    b=n+j−r−1/2.

For r≥1, h=r+1/2≥1. If T has Gamma density with parameter b, Jensen gives Γ(b+h)/Γ(b)=E[T^h]≥b^h. Since b≥j+1/2 for r≤n−1, it follows that M_r≤Γ(r+1/2). Jensen is not applied with a concave power.

For r=0 another direction is needed: Cauchy on the gamma integrals gives

    Γ(x+1)²≤Γ(x+1/2)Γ(x+3/2)=(x+1/2)Γ(x+1/2)².

Thus Γ(x+1/2)/Γ(x)≥x/√(x+1/2)≥√(x−1/2). Take x=n+j−1/2: the ratio Γ(n+j)/Γ(n+j−1/2) is at least√(n+j−1)≥√j, which proves M_0≤√π.

Finally Γ(r+1/2)=√π(2r)!/(4^r r!)<2r!, because binom(2r,r)≤4^r and√π<2. Summing r!≤(n−1)! over n terms gives MOMENTS.

For the additional moment r=n, needed later, its parameter b is j−1/2, which is LESS than j. The previous bound is not inherited. If j≥10000n², Jensen with h=n+1/2 gives

    M_n≤Γ(n+1/2)[j/(j−1/2)]^(n+1/2).

The logarithm of the factor is bounded by(n+1/2)/(2j−1)<1/100. By exp(1/100)≤100/99<3 one obtains

    Σ_(r=1)^n M_r ≤3Σ_(r=1)^nΓ(r+1/2) <6n n!.         (EXTRA)

The case n=1 is included: it only uses the branch r0 and the explicit factor of r=n.

## 3. Scalar endpoint N'=1 in the contour

QUADRATIC_EXPLICIT017 proves for u=63/2, N'≥2 and k'≥10000N'² that the scalar density

    ρ_(N',k')(z)=z^(2k')/(u²+z²)^(N'+k')

satisfies ∫|ρ(x+15i)|dx≤5∫ρ(x)dx. N'=1 needs to be justified separately.

INTERIOR017§2 proves for H_k(s)=s^k/(s+u)^(k+1), ALL k≥0,

    ||exp(15t)h_k||²≤11||h_k||².

To keep its elementary content visible: if a0=u−15=33/2, b0=15 and c_k=binom(2k,k)/4^k, Plancherel and the binomial expansion give

    N_k(15)=(1/(2a0))Σ_(l=0)^k c_(k−l)c_l(b0²/a0²)^l,
    N_k(0)=c_k/(2u).

Vandermonde gives c_(k−l)c_l≤c_k, hence N_k(15)/N_k(0)≤u a0/(a0²−b0²)=11. The norm with weight exp(−15t) is smaller than the unweighted norm, by causality.

At z=x+15i, ρ_(1,k)(z)=H_k(−15+ix)H_k(15−ix). Cauchy and Plancherel produce

    ∫|ρ_(1,k)(x+15i)|dx
      ≤2π||exp(15t)h_k||||exp(−15t)h_k||
      ≤√11∫ρ_(1,k)(x)dx <4∫ρ_(1,k)(x)dx.

Hence the bound5 is also valid for N'=1. This separation of norms is used ONLY for the scalar endpoint of dimension1, where there is an already proved bound uniform in k; it is not applied to the general numerators of dimension n.

## 4. Complete contour: polynomial product and exact norm

For real P, the complete density is

    ρ(z)=z^(2j)P(iz)P(−iz)/(u²+z²)^(n+j)
        =(−1)^(n−1)a^(−2n+2)
          z^(2(j+n−1))R(a/z)R(−a/z)/(u²+z²)^(n+j).

The sign is essential for the identity; on the real line R(y)R(−y)=(−1)^(n−1)|R(y)|². For the complex modulus, COEFF gives

    |R(Y)R(−Y)|≤C_nH max(1,|Y|^(2n−2))
                  ≤C_nHΣ_(r=0)^(n−1)|Y|^(2r).

For j≥10000n², each remaining term is a scalar density with

    N'=r+1, k'=j+n−1−r, N'+k'=n+j.

One has k'≥j≥10000N'². Applying the contour5 of017 and the endpoint of§3, and keeping all scale factors, gives

    ∫|ρ(x+15i)|dx
      ≤5C_nH a^(−2n+2)Σ_r a^(2r)∫ρ_(r+1,j+n−1−r)(x)dx.

The same change x=a/y proves EXACTLY

    ∫ρ_(r+1,j+n−1−r)(x)dx=a^(−2r−1)M_r.

Thus the powers of a cancel before normalizing. Since ∫ρ(x)dx=a^(1−2n)H, MOMENTS proves

    ∫|ρ(x+15i)|dx / ∫ρ(x)dx
        ≤5C_nΣ_rM_r ≤10C_n n!=D_n.                    (STRIP)

STRIP is uniform over ALL P and ALL j≥10000n². The constant depends on n; it is not confused with a uniform temporal norm independent of n, refuted in016.

## 5. The whole arithmetic comb, with summable tail

ρ is rational, analytic in |Imz|<u, and decays at least like|z|^−2 in each closed strip. Shifting the contour up to Imz=15, with the vertical edges tending to zero, gives for t≥0

    |c_(Q^jF0)(t)| ≤D_n exp(−15t)||Q^jF0||².

No supposed pointwise symbol of the infinite comb is used. With Λ(q)≤q and summing ALL integers q≥2,

    |Comb|/||Q^jF0||²
      ≤2D_nΣ_(q≥2)Λ(q)q^(−31/2)
      ≤2D_nΣ_(q≥2)q^−14
      ≤2D_n·2^−14(1+2/13)<D_n.                         (COMB)

The series converges absolutely and keeps all contacts, including primes and prime powers. The loss from replacing Λ by q is paid by the later cutoff; no favourable sign is attributed to any atom.

## 6. Inverse moment and ARCH with explicit cutoff

On the real line, COEFF implies |R(y)|²≤C_nHΣ_(r=0)^(n−1)y^(2r). Multiplying by y²w and using EXTRA gives

    E_(Q^jF0)[τ^−2]
      =(1/(u²j)) ∫y²|R(y)|²w/H
      ≤A_n/(u²j),    A_n=6C_n n n!.                    (INVERSE)

If j≥K(n), then

    E[τ^−2]≤u^−2 3^(−4D_n−20).

The elementary symbol bound of017 is

    m(τ)≥log(|τ|/(2π))−1/|τ|−1/(2τ²).

Jensen for log and Cauchy produce

    ARCH/||Q^jF0||²
      ≥−(1/2)log Eτ^−2−log(2π)−√(Eτ^−2)−Eτ^−2/2
      ≥log(u/(2π))+(2D_n+10)log3−1/u−1/(2u²)
      >2D_n+9.                                        (ARCH)

Here u>2π, log3>1 and1/u+1/(2u²)<1. All are elementary inequalities; K(n), whose exponent is an explicit integer, is not evaluated.

## 7. Complete polar

From COEFF and evaluating R at±2ia, one obtains

    |P(1/2)P(−1/2)|≤C_nH.

Indeed the power(2a)^(2n−2) of the bound on R cancels exactly with the prefactor of P, and2a>1. Thus

    |Polar[Q^jF0]|/||Q^jF0||²
      ≤(4π/u)C_n[u²/(u²−1/4)]^n j^(n−1/2)3968^−j
      <C_n exp(n)j^n3968^−j.                           (POLAR-RAW)

For j≥10000n² this last expression is less than1: logC_n<6n (use log9<3 and logn≤n−1), logj≤√j, n√j≤j/100 and7n≤7j/10000. Since log3968>1, the logarithm of the majorant is less than

    7n+n logj−j ≤7j/10000+j/100−j<0.

Also4π/u<1 and u²/(u²−1/4)<exp1, which justify POLAR-RAW without discarding its sign. Hence

    |Polar|<||Q^jF0||².                                 (POLAR)

## 8. Conclusion and scope

ARCH, COMB and POLAR refer to the SAME function and same norm. Adding them with the adverse orientations gives

    W[Q^jF0]/||Q^jF0||² > (2D_n+9)−D_n−1=D_n+8>1,

proving EFFECTIVE. No cross term of the numerator is omitted: all were included in the product R(Y)R(−Y) and in COEFF before the diagonal bounds.

An explicit variable-dimension cutoff was obtained for the WHOLE rational orbit, although its size is enormous. This does not prove the indices j<K(n), does not prove positivity of the complete table and does not determine a new time window T. The effective novelty does not replace the interior arithmetic obligations still pending. Papers untouched.
