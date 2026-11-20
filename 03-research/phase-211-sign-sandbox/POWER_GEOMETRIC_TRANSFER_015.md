# POWER_GEOMETRIC_TRANSFER_015 — Exact positive mixture, normalization and strong convergence at every fixed order

Status: PROVED (infinite identity and normalization, all N>=1 and u>1). It is not by itself a sign proof. The complementary eventual-positivity result is in POWER_HIGHPASS_015. Papers untouched.

## 1. Corpus, scope and difference

Consulted index/grid/crossword searching for high-pass, highpass, resolvent powers, positive/geometric mixture and one-pole iteration; reviewed POWER_SIGNED_TRANSFER_014 §9 and the independent one-pole derivation of the case analysis. The filter structure and the rational identities have antecedents; the new difference is to prove the infinite expansion with convergence in a topology where the FULL form is continuous, and to obtain normalized weights that sum exactly to one. L2 density is not used as a substitute for continuity of the form.

Fix u>1. This restriction ensures that there exists eta with 1/2<eta<u/2. The value of the phase is u=63/2. This infinite convergence is not claimed for every u>1/2: in part of that range the polar multiplier of the orbit may grow. The FINITE identities of 014 keep their earlier scope u>1/2.

## 2. Exact iteration of one pole

Let N>=1, P real of degree <N, v>=u, and

    F0(s)=P(s)/(s+u)^N,
    Fv(s)=P(s)/[(s+u)^{N-1}(s+v)],
    Q(s)=s/(s+u), rho=u²/v², a=1-rho.

Write h_k for the function with transform Q^k F0, and g_{k,v} for the one with transform Q^k Fv. The complete one-pole identity proves, for each K>=0,

    W[fv]=rho Σ_{k=0}^K a^k W[h_k]+a^{K+1}W[g_{K+1,v}]. (FIN)

The residual term is the orbit of the TARGET fv, not that of f0. In transforms,

    h_k(s)=s^kP(s)/(s+u)^{N+k},
    g_{K+1,v}(s)=s^{K+1}P(s)/[(s+u)^{N+K}(s+v)].

Proof: changing only the pole v of g_{k,v} to u keeps the same factor rho and produces h_k; the gain summand is g_{k+1,v}. Iterate W[g_{k,v}]=rho W[h_k]+a W[g_{k+1,v}]. This identity also holds for the squared L2 norm.

## 3. A topology that controls the WHOLE form

Choose 0<t<1/2 and 1/2<eta<u/2. For causal functions, extended by zero to the negative half-axis, use

    ||f||_X²=||f||_{H^t(R)}²+||exp(eta y)f||_2².

Every proper rational datum with rates >=u belongs to X, even if it has a jump at the origin: its transform decays at least like 1/|tau|, and t<1/2 suffices.

The form W is continuous on X. Indeed:

* |m(tau)|<=C_t(1+tau²)^t controls the archimedean part.
* The polar moments satisfy |A(f)|<=||f||_eta/sqrt(2eta-1), |B(f)|<=||f||_eta/sqrt(2eta+1).
* The autocorrelation satisfies |c_f(logq)|<=||f||_2||f||_eta q^-eta. Hence the absolute comb is bounded by 2Σ_{q>=2}Lambda(q)q^{-eta-1/2}||f||_2||f||_eta, whose series converges because eta>1/2.

Thus |W[f]|<=C_X||f||_X², and by polarization the bilinear form is continuous. Neither the polar nor the infinite comb is lost in this choice of norm.

## 4. The high-pass orbit converges strongly to zero

On the Fourier axis,

    |Q(i tau)|²=tau²/(u²+tau²)<=1,

with strict inequality for every finite tau. On the shifted Laplace line s=-eta+i tau,

    |Q(-eta+i tau)|²=(eta²+tau²)/[(u-eta)²+tau²]<1,

since eta<u/2. Plancherel on that line represents the time-weighted norm. Dominated convergence in both norms proves, for every rational datum f considered,

    Q^k f ->0 strongly in X.

The operators Q^k are moreover contractions of X. In particular h_k,g_{k,v}->0 in X and W[g_{k,v}]->0. This result holds for ALL fixed orders N and all proper numerators; it requires neither that P vanish at the origin nor higher temporal regularity.

## 5. Infinite mixture and exact normalization

Passing to the limit in (FIN),

    W[fv]=rho Σ_{k>=0} a^k W[h_k],
    ||fv||²=rho Σ_{k>=0}a^k||h_k||².                     (MIX)

Both series converge absolutely. For W, it suffices that |W[h_k]|<=C_X||f0||_X² and Σ rho a^k=1; for the norm, the summands are nonnegative and the residue converges to zero. If v=u, only the term k=0 remains.

For nonzero P, all h_k are nonzero. The weights

    pi_k=rho a^k||h_k||²/||fv||²

are nonnegative and sum exactly to one. Hence

    W[fv]/||fv||²=Σ_{k>=0}pi_k W[h_k]/||h_k||².           (RAY)

The sum of the weighted absolute values also converges. This is a mixture of QUADRATIC QUOTIENTS; it does not identify fv with a sum of functions nor authorize ignoring cross terms of arbitrary superpositions.

## 6. All poles: complete homogeneous weights

For rates v_1,...,v_N>=u, f0=P/(s+u)^N and f=P/Π_j(s+v_j), set rho_j=u²/v_j², a_j=1-rho_j. The filters (s+u)/(s+v_j) commute with Q and are contractions both in H^t and in the weighted norm of §3. Applying (MIX) successively, using absolute convergence, gives

    W[f]=Σ_{k>=0}w_k W[Q^k f0],
    ||f||²=Σ_{k>=0}w_k||Q^k f0||²,                       (MULTI)

where

    Σ_{k>=0}w_k z^k=Π_j rho_j/(1-a_j z),
    w_k=(Π_j rho_j)Σ_{k_1+...+k_N=k}Π_j a_j^{k_j}.

The weights w_k are nonnegative and Σw_k=1. The passage to multiple sums is legitimate because all forms of the filtered orbits are uniformly bounded by C_X||f0||_X². The generator can also be verified directly on the Fourier axis:

    |(s+u)/(s+v_j)|²=rho_j/[1-a_j|Q(s)|²], s=i tau.

The polar is incorporated by the complete finite identity before passing to the limit; its sign is not deduced from a positive spectral measure.

The normalized weights for the quotient of f are w_k||Q^k f0||²/||f||² and sum to one. Thus, positivity of the WHOLE high-pass orbit Q^k V_N would be sufficient for all N poles >=u. Sufficiency does not presuppose the sign of those blocks.

## 7. Valid monotonicity and the remaining node

For a fixed numerator, the archimedean quotient of h_k is nondecreasing: the change k->k+1 reweights the spectral probability by tau²/(u²+tau²), increasing in |tau|, and the positive covariance with m is applied. The polar does not have that property: exactly

    Polar[h_k]=[-1/(4u²-1)]^k Polar[h_0].

Each prime correlation contains an oscillating cosine; monotonicity of the FULL quotient in k has not been proved. No sign rule is obtained by summing only coefficients Lambda>=0.

POWER_HIGHPASS_015 proves by another argument that, for each fixed N, the full blocks Q^k V_N are uniformly positive for k sufficiently large. Consequently, for each fixed order only a FINITE segment of the orbit can obstruct the sufficient condition of (MULTI). No universal effective endpoint of that segment is available here, nor has its sign been verified for all N. The exact mixture, the normalization and the control of the tail are proved tools; positivity of the missing initial blocks remains the arithmetic node.
