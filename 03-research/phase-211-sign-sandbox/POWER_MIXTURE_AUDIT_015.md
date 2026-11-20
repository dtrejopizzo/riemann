# POWER_MIXTURE_AUDIT_015 — Complete geometric identity and convergence in form norm

Status: PROVED identities, indices and convergence for u>1; does not prove the sign of its components. Papers untouched.

## 1. Exact index of the finite remainder

Fix v>=u>1/2 and a causal rational function f0, with all its rates>=u and numerator of degree less than the denominator. Write

    H(s)=(s+u)/(s+v), fv=H f0,
    R0=u²/v², a=1-R0,
    Q(s)=s/(s+u), q(tau)=|Q(i tau)|²=tau²/(u²+tau²).

The exact scalar identity is |H|²=R0/(1-aq). The result of PRIME_TRANSFER014 is equivalent to

    W[fv]=R0 W[f0]+a W[Q fv].

The filters Q,H commute. Iterating this result gives, for EVERY integer K>=0,

    W[fv]=R0 sum_(k=0)^K a^k W[Q^k f0]
              +a^(K+1)W[Q^(K+1)fv].                    (FIN)

The remainder contains the TARGET function fv, not only f0. It can also be checked via |H|²=R0 sum_(k0..K)(aq)^k+(aq)^(K+1)|H|² and the corresponding polar identity. Each finite equality holds with all contacts: the functions are causal rational with positive rate and the comb converges absolutely.

## 2. Strong space and convergence of the remainder

For the infinite step the sufficient hypothesis u>1 is used here. Choose1/2<eta<u/2 and0<s<1/2, and take the norm

    ||f||_(eta,s)=||e^(eta y)f(y)1_(y>0)||H^s(R).

Every causal rational function with rates>=u belongs to this space: after weighting, its rational transform has poles with rates>=u-eta>0 and tailO(1/|tau|), sufficient for H^s when s<1/2. Absence of a time jump at0 is not assumed.

The weighted multiplier Q is

    Q(-eta+i tau)=(-eta+i tau)/(u-eta+i tau).

Its modulus is<=1 on the whole line and<1 for every finite tau, because eta<u/2. For fixed f, Parseval and dominated convergence in the integral with weight(1+tau²)^s give

    ||Q^k f||_(eta,s)->0,
    ||Q^k f||_(eta,s)<=||f||_(eta,s).

The weighting identities are applied to causal rational functions with exponential decay, so no norm estimate has been assumed beforehand to justify the shifted line.

The COMPLETE form W is continuous bilinear on this space. The gamma part is controlled by log(2+|tau|)<=C_s(1+tau²)^s, after multiplying by the bounded Lipschitz function e^(-eta max(y,0)). The weighted correlation decays like e^(-eta t), so sum2Lambda(q)q^(-eta-1/2) converges and controls the comb. The two polar moments are continuous because eta>1/2. Hence W[Q^k f]->0 and remains uniformly bounded.

Applying this to fv in FIN eliminates the remainder. One obtains the ABSOLUTELY convergent identity

    W[fv]=R0 sum_(k>=0) a^k W[Q^k f0].                  (INF)

The weights R0 a^k are nonnegative and sum to1, but the summands of W may have both signs. The vectors were not normalized. For a mixture of Rayleigh quotients one must additionally introduce the squared norms of the vectors, which also satisfy their own mixture identity.

The restriction u>1 is not cosmetic for this proof: if1/2<u<sqrt(1/2), the polar multiplier of Q is -1/(4u²-1), of modulus>1, and an infinite expansion of the complete form may fail for large a. The finite identities remain correct, but INF is not extended to all u>1/2 without another stability hypothesis.

## 3. All new poles as a single mixture of high-pass powers

From f0=P/(s+u)^n to f=P/prod_j(s+v_j), v_j>=u>1, set a_j=1-u²/v_j² and R0j=1-a_j. All filters use the SAME Q. Iterating INF and Fubini give

    W[f]=sum_(k>=0) w_k W[Q^k f0],
    w_k=(prod_j R0j)sum_(k1+...+kn=k)prod_j a_j^(kj),
    sum_k w_k t^k=prod_j R0j/(1-a_j t), sum_k w_k=1.

Absolute convergence requires no assumed sign: each operator H_j has weighted norm<=1, and the terms Q^k f0 are uniformly bounded in the above strong norm; the total of the positive weights is1. This justifies the interchanges of the finite series by factors and infinite ones by degrees.

For a FIXED dimension n, an inequality W[Q^k f0]>=0 for ALL k and ALL numeratorsP of degree<n would transport the sign to all rates>=u. Proving it for a single P or for some k is not enough. The functions Q^k f0 lie in the confluent spaces of n+k poles and have numerator s^kP, with a zero of order k.

## 4. What the identity contributes and what it does not

This expansion is an identity of filters and forms, compatible with the scope of prop:opcalc. It creates no arithmetic compensation. The sign obligation is now explicit on rational subspaces with prescribed zeros; proving it would be the additional inequality and not a consequence of changing coordinates.

For the archimedean part there is an immediate finite result: reweighting by q, increasing in |tau|, gives

    Rayleigh_ARCH(Q^(k+1)f0)>=Rayleigh_ARCH(Q^k f0).

The comparison is strict for a nonzero vector and extends to the ordered eigenvalues of these subspaces by min--max on the SAME space of numeratorsP. That monotonicity is not claimed for W nor for AP.

Eventual uniform positivity of W on the whole family Q^k V_n is a separate goal. The natural frequency scaling is sqrt(k), but a uniform statement must control simultaneously all coefficientsP, the quotient of the weighted norm, the moments and the comb. An argument only for the top-degree term of P is not uniform when that coefficient vanishes or depends on k. This note does not assume that future result.
