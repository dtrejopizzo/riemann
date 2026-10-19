# R161_076 — A physical local Weil limit, and the unresolved Poisson product

## 1. Local convergence without meromorphic continuation

Fix f in C_c^infinity(-T,T). Use right shifts V_b f(t)=f(t-b), and write

    L_M=sum_(2<=n<=M) Lambda(n)n^(-1/2)V_(log n),
    A_M=mathcal M-L_M-L_M*,

where mathcal M is the Gamma multiplier of R161_001. This A_M agrees with that note's symmetric prime sum, regardless of the opposite tau convention there.

For |t|<=K, a shifted source f(t +/- log n) can be nonzero only when log n<=K+T. Therefore A_M f stabilizes exactly on every compact interval once M>=exp(K+T). There is a well-defined physical distribution A_loc f, and

    A_M f -> A_loc f in D'(R),

with eventual equality of the restrictions, not merely weak convergence. The Gamma term is fixed throughout. On (-T,T), stabilization occurs at M>=exp(2T), reproducing the compressed Weil form.

No equation A_loc f=0 follows from this construction. In particular the meromorphically zero symbol from R161_075 is not its definition.

## 2. A safe weighted norm

For eta>1/2 let X_eta=L2(R,exp(-2eta|t|)dt). For b>T,

    ||V_b f||_(X_eta)=exp(-eta b)||exp(-eta t)f||_2,
    ||V_(-b) f||_(X_eta)=exp(-eta b)||exp(eta t)f||_2.

Consequently, for M>exp(T),

    ||(L_infinity-L_M)f||_(X_eta)
       <=||exp(-eta t)f||_2
          sum_(n>M) Lambda(n)n^(-1/2-eta),

and analogously for the opposite shifts. Since Lambda(n)<=log n, both tails converge to zero. For smooth compact f the Gamma multiplier gives an L2 vector, hence an X_eta vector. Thus A_M f converges in X_eta to the same A_loc f.

This proves an actual global weighted limit without an assumption about zeros. The weight allows exponential growth; this result supplies neither unweighted L2 membership nor a tempered Fourier transform for A_loc f.

## 3. Raw Poisson composition needs a moving spatial region

In the phase convention put S_N h(t)=sum_(n<=N)n^(-1/2)h(t+log n). To evaluate S_N A_M f for |t|<=K requires A_M f up to t=K+log N. A sufficient stabilization condition is

    M>=N exp(K+T).                              (3.1)

Under (3.1), S_N A_M f=S_N A_loc f on [-K,K]. For fixed N this is elementary local convergence. It gives no limit as N tends to infinity, since the region examined by S_N expands with N. Replacing moving M,N by the stabilized interior cutoff exp(2T) is invalid.

## 4. The continuum term is more demanding

R161_003 defines, on compact inputs,

    C_N h(t)=exp(-t/2)
       integral_(-infinity)^(t+log N) exp(y/2)h(y)dy.

Unlike S_N, this expression samples an infinite left tail even for fixed N. Membership in X_eta for eta>1/2 does not ensure that the integral exists. For example

    h(y)=1_(y<0) exp(-y/2)

belongs to every such X_eta, while exp(y/2)h(y)=1 on the negative half-line, so its continuum integral diverges. This example concerns continuity on the ambient space; it is not an assertion about A_loc f.

Thus the proved X_eta convergence cannot by itself justify C_N A_M f -> C_N A_loc f, nor the renormalized product (S_N-C_N)A_loc f. The source's primitive moments cannot simply be substituted for the weighted moments of A_loc f.

## 5. Precise surviving construction task

The physical Weil limit is now defined independently of the meromorphic zero symbol. To construct its Poisson product, one must prove convergence of the combined renormalized expression on these particular vectors, or define a regularized continuum action with a justified matching theorem. The discrete and continuum divergences may cancel; separate divergence is not an impossibility result for their combined action.

The next required estimate is tail cancellation for (S_N-C_N)A_M f on a stated joint cutoff and domain, retaining the reflected contribution. Equating it to a zero commutator before that estimate would reproduce the gap in R161_018.

## Status

Proved for compact smooth sources: exact local stabilization of A_M f; X_eta convergence for eta>1/2; sufficient cutoff relation (3.1); insufficiency of that weighted space for the continuum action. Open: the renormalized product limit on first-contact sources and the equality-state detector annihilation. D remains open.
