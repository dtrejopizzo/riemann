# R161_077 — The continuum action modulo its lower-endpoint Tate term

## 1. Exact finite arithmetic continuum

Use right shifts V_b, L_M and C_N from R161_076. For compact smooth f with integral exp(u/2)f(u)du=0, define

    J_f(x)=integral_(-infinity)^x exp(u/2)f(u)du.

J_f vanishes outside [-T,T]. Changing variables in each finite summand gives

    C_N L_M f(t)=exp(-t/2) sum_(2<=n<=M)
                      Lambda(n) J_f(t+log N-log n),          (1.1)

    C_N L_M* f(t)=exp(-t/2) sum_(2<=n<=M)
                      Lambda(n)/n J_f(t+log N+log n).        (1.2)

No infinite interchange is used. For |t|<=K, the first sum contains only n<=N exp(K+T), while the second contains only n<=exp(K+T)/N. Thus both stabilize as M grows; M>=N exp(K+T), N>=1 is sufficient. In particular (1.2) vanishes throughout [-K,K] when log N>=K+T.

These are limits of the finite continuum actions. They do not by themselves identify the improper integral C_N L_infinity* f: its lower-endpoint limit requires separate control.

## 2. Lower cutoff and a rank-one ambiguity

For any locally integrable h define, with a<t+log N,

    C_(N,a)h(t)=exp(-t/2) integral_a^(t+log N) exp(y/2)h(y)dy.

For fixed a,b and t in an interval on which both upper endpoints exceed a,b,

    C_(N,a)h(t)-C_(N,b)h(t)
       =exp(-t/2) integral_a^b exp(y/2)h(y)dy.                (2.1)

The difference lies exactly on the negative Tate line. Let Pi_K project L2(-K,K) orthogonally off exp(+-t/2). If h is locally L2, (2.1) implies

    Pi_K C_(N,a)h=Pi_K C_(N,b)h.                             (2.2)

Hence the projected continuum action has a canonical meaning using any sufficiently low finite anchor, even when the unprojected improper integral is unknown. This is a quotient statement; it does not supply a canonical full-space L2 representative.

## 3. Application to the physical Weil limit

For compact smooth f, A_M f is L2 and its integral from minus infinity in C_N exists by Cauchy–Schwarz with exp(y/2). On any fixed finite interval, A_M f eventually equals A_loc f by R161_076. Fix an anchor a<-K+log N. For all sufficiently large M,

    Pi_K C_N A_M f
      =Pi_K C_(N,a) A_M f
      =Pi_K C_(N,a) A_loc f.                                (3.1)

The first equality removes the lower-tail scalar; the second uses local stabilization on the interval from a to K+log N. Together with raw finite synthesis stabilization this proves, for each fixed N,

    Pi_K(S_N-C_N)A_M f
      -> Pi_K[S_N A_loc f-C_(N,a)A_loc f],                   (3.2)

with eventual equality, independent of the anchor after projection.

This resolves the fixed-N continuum-domain obstruction after primitive projection on smooth compact sources. It uses only the actual physical limit, not a meromorphic zero symbol. Formula (3.1) itself does not require f to be primitive; primitivity was used for the stronger unprojected arithmetic stabilization in Section 1.

## 4. What remains after taking the quotient

The removed scalar is not proved zero. It must be restored and controlled if a full exterior or Hardy representative is required. Moreover (3.2) is for fixed N: the subsequent N limit still samples an expanding spatial interval. This calculation proves neither a bound uniform in N nor annihilation on a first-contact radical. Extension from compact smooth sources to the first-contact form domain also requires continuity of the operators involved in the chosen limit topology.

The quotient identity is therefore usable as a rigorously defined finite stage. Closure still needs a theorem for its N-dependent exterior remainder and the corresponding Tate normalization.

Status: exact finite arithmetic formulas and canonical projected continuum action proved; fixed-N projected physical limit proved; global scattering and D open.
