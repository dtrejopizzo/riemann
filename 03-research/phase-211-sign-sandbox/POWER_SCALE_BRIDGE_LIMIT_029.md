# POWER_SCALE_BRIDGE_LIMIT_029 — Scope of the cone of growing rates

Status: PROVED obstruction to approximation by positive mixtures of normalized densities. Full proof reviewed and APPROVED in POWER_SCALE_AUDIT_029.md. It refutes neither W nor other bridges. Papers untouched.

## Corpus and difference

Consulted routes index, grid and crossword; read SCALAR_BRIDGE017 and JOINT_SCALE016. The obstruction of centred weights016 keeps u fixed and lets N/u² grow. The present obligation is different: determine whether the new domain u>=C sqrt(N), for a fixed C>0, can replace ALL the atoms of the bridge017 through positive approximation of densities. A concentration bound of the whole cone is proved, not a claim about signs of W nor a prohibition of other representations.

## 1. Uniform spectral height

For N>=1,k>=0 and u>0 the normalized spectral probability density is

    p_(N,k,u)(tau)=1/[u B(k+1/2,N−1/2)]
       ·(tau/u)^(2k)/[1+(tau/u)²]^(N+k).

At tau=0 the usual limit is taken when k=0. Its maximum is at tau²/u²=k/N. Define h_N(k)=u sup p_(N,k,u), allowing real k>=0 only to prove the comparison. For k>0,

    d log h_N(k)/dk
      =psi(k+N)−psi(k+1/2)+log[k/(k+N)].

By convexity of (x+t)^−2 on each interval [j−1/2,j+1/2], for x>1/2,

    psi'(x)=sum_(j>=0)(x+j)^−2
       <=int_(-1/2)^infinity(x+t)^−2dt=1/(x−1/2).

Integrating between k+1/2 and k+N proves

    d log h_N(k)/dk
      <=log[(k+N−1/2)/(k+N)]<0.

Continuity on reaching k0 gives

    sup p_(N,k,u)<=Gamma(N)/[u sqrt(pi) Gamma(N−1/2)].

If G has gamma density with parameter N−1/2, the ratio of gamma functions is E sqrt(G). Cauchy–Schwarz gives E sqrt(G)<=sqrt(EG)=sqrt(N−1/2)<sqrtN. Thus for ALL N,k,

    sup p_(N,k,u)<sqrtN/[u sqrt(pi)].                    (HEIGHT)

No asymptotic estimate nor sweep in N or k is used.

## 2. Quantitative obstruction of the positive cone

Fix C>0 and restrict to u>=C sqrtN. By HEIGHT,

    p_(N,k,u)(tau)<=1/[C sqrt(pi)].

Every normalized positive mixture, finite or integral, satisfies the same bound by Tonelli. On I=[−C/8,C/8] its mass is at most1/(4sqrt(pi))<1/4.

By contrast fix u0=63/2 and consider the target density p_(M,0,u0), an atom allowed by the bridge017. For M>=2,

    E tau²=u0²/(2M−3).

Choose an integer M such that 2M−3>256u0²/C². Chebyshev gives

    int_(outside I) p_(M,0,u0)<1/4,
    int_I p_(M,0,u0)>3/4.

Hence, for every normalized positive mixture q of the domain u>=C sqrtN,

    ||p_(M,0,u0)−q||_L1
       >=abs(int_I[p_(M,0,u0)−q])>1/2.                 (GAP)

The same conclusion rules out approximations by non-normalized cones whose mass tends to1: normalizing them would preserve any supposed L1 limit. The use of an interval avoids inferring an L1 obstruction from values at a single point.

## 3. Exact scope relative to the target

The positivity to be proved for all N with u>=C sqrtN is a real and infinite region of the parameter table. GAP proves that it is NOT enough to automatically transfer the positive density bridge017 to that restricted region. There are admissible atoms of fixed rate that cannot be approximated in L1 by that cone.

It is not claimed that the positivity of that region is useless, that an identity with additional structure is impossible nor that W has negative values. Nor are other kinds of approximation, extrapolation or direct control excluded. The global target still requires new information for large N/u² and for the corresponding arithmetic cancellations.
