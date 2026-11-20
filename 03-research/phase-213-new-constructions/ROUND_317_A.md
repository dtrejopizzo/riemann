# Cut at the root by two successive order-one convolutions

Let c_t=b_t*1 and C_t(v)=Σ_(m≤v)c_t(m); keep B_t for the summatory function of b_t. For any D=x^o(1), q=⌊D⌋+1, there are explicit signed weights g(n) such that

    C_t(x)+Σ_(D<n≤√x)g(n) C_t(x/n) = O_ε(x^(1/2+ε))

uniformly for 0≤t≤2. The one-sided integrated ceiling of 292 for B_t is also valid as a criterion equivalent to the sign with C_t. Hence in this single-balance criterion the retained dilations have arguments between √x and x/D. For the original balance B_t the same truncation is obtained using two types of intermediate balances, B_t and C_t. No estimate for the divisor problem is used.

**What C counts.** Its local factors are c_t(p)=1−2u_p and c_t(p^e)=(1−u_p)²=cos²(t log p) for all e≥2. In particular,

    c₀(n)=(−3)^(#{p≡2 mod 3: p divides n exactly once}).

This includes the prime 2. The series of C is G_t²L(s−it,χ)L(s+it,χ)/ζ(s) by 292. Under RH the same Mellin proof of 292 with a single power of the reciprocal gives |C_t(x)|≪_ε x^(1/2+ε) uniformly on [1,2]. Given an exterior zero, the numerator remains nonzero for almost every frequency and one can localize a smooth positive average that preserves that pole. There are no real poles in s>1/2. Landau's one-sided argument of 292 proves the converse with the average of the positive parts of C_t. This equivalence is for the family in frequency; it is not attributed to the explicit row t=0 by itself.

**Order-one sieve.** Write a=(μ 1_[1,D])*(δ₁−qδ_q) as a Dirichlet sequence and g=1*a. Then g(1)=1, g(n)=0 for 2≤n≤D and Σ|a(d)|≤(1+q)D. For any v,

    |Σ_(n≤v)g(n)| = |Σ_(d≤D)μ(d)(⌊v/d⌋−q⌊v/(qd)⌋)| ≤ qD.

Indeed, each difference of floors is a residue between 0 and q−1. This v-independent ceiling replaces the power error of 316. If F is the summatory function of b_t or c_t and f its coefficients, both satisfy |f(m)|≪_ε m^ε by the local values. For X≤x and V=√x, the exact exchange of 311 gives

    |Σ_(X/V<n≤X)g(n)F(X/n)| ≤ 2qD Σ_(m≤V)|f(m)| ≪_ε x^(1/2+ε).

The subpower losses in D,q can be absorbed into any ε. We apply this only for X=x or x/d with d≤qD, so X/V>D for large x.

**Closing the two identities.** Define I_F(X)=Σ_(D<n≤X/V)g(n)F(X/n). Let U be the summatory function of the coefficients of D_t(s)ζ(s)², with uniform root ceiling by 309. Since g*c_t=a*(1*c_t), the full mean of C at X is Σ_d a(d)U(X/d), of size O_ε(x^(1/2+ε)). Removing the tail proves C_t(X)+I_C(X)=O_ε(x^(1/2+ε)), also at the required X=x/d. For B, the same exact convolution gives the mean Σ_d a(d) C_t(x/d). Substituting the identities for C at those points, absorbing Σ|a(d)|=x^o(1), gives

    B_t(x)+I_B(x)+Σ_d a(d) I_C(x/d)=O_ε(x^(1/2+ε)).

All the summatory functions inside the two I are evaluated at arguments ≥√x and <x/D. The one-type criterion requires an integrated floor for I_C; the two-type one requires that floor for the written combination. Neither of these floors follows from bounding the residues of the divisions.

**Cross-check with the corpus.** Round 049 already confined two factors near the root in a different smoothed sum, using finite inversion over divisibility rows and quadrature control. Finite inversion is also classical here. The specific gain over 316 is the elementary and uniform bound for the tail of the ordinary summatory functions of 292 via the intermediate balance c_t, with a pointwise identity in x, with no new sign for the remaining stretch.
