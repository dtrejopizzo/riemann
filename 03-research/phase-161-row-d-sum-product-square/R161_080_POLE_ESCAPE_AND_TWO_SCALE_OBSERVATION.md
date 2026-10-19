# R161_080 — Pole escape and a two-scale exterior observation

## 1. Why the weak limit alone does not observe a Gamma pole

R161_079 constructs a distributional limit. To test whether it controls the exterior residues of R161_047, fix a>0, k!=0 and R>T, and consider

    h_R(t)=-k exp(at) 1_(t<-R).

Its Laplace transform, initially for Re z<a, is

    H_R(z)=k exp((z-a)R)/(z-a).                         (1.1)

Therefore Res_(z=a) H_R=k for every R. Nevertheless h_R tends to zero locally as a distribution and

    ||h_R||_2^2=|k|^2 exp(-2aR)/(2a) -> 0.             (1.2)

Thus neither the weak convergence just constructed nor even ordinary L2 convergence makes this meromorphic residue continuous. These are elementary test functions, not claimed physical first-contact solutions. This does not prove independence from the full arithmetic system.

The same phenomenon survives smoothness: choose smooth chi equal to 1 on (-infinity,-1] and 0 on [0,infinity), and put h_R^sm(t)=-k exp(at)chi(t+R). Its difference from h_R is compactly supported, so its Laplace transform has the same residue. For every nonnegative integer j,

    ||partial_t^j h_R^sm||_2=O_(a,j,chi,k)(exp(-aR)).    (1.3)

Indeed h_R^sm(t)=exp(-aR)b(t+R) for the fixed smooth function b(u)=-k exp(au)chi(u), whose derivatives are square integrable. Even convergence in all these Sobolev norms does not control the residue.

## 2. Abel observation and noncommuting limits

For a function whose integral exists, define

    B_epsilon(h)=-epsilon integral_R exp(-(a-epsilon)t)h(t)dt,
    0<epsilon<a.

This is evaluation from the convergent side multiplied by minus the distance to the pole. Formula (1.1) gives exactly

    B_epsilon(h_R)=k exp(-epsilon R).                  (2.1)

Consequently

    lim_(epsilon->0) lim_(R->infinity) B_epsilon(h_R)=0,
    lim_(R->infinity) lim_(epsilon->0) B_epsilon(h_R)=k.

A simultaneous limit retains the full coefficient k only if epsilon R tends to zero. If epsilon R tends to c>0 it observes k exp(-c), and if epsilon R tends to infinity it loses the coefficient completely. No sign or arithmetic cancellation is involved in this loss.

## 3. Finite observation requires a second, larger scale

For L>R define the truncated observation

    B_(epsilon,L)(h_R)
      =-epsilon integral_(-L)^0 exp(-(a-epsilon)t)h_R(t)dt
      =k[exp(-epsilon R)-exp(-epsilon L)].             (3.1)

Recovering k in this escaping-tail model requires both

    epsilon R -> 0,       epsilon L -> infinity.       (3.2)

In particular L/R must tend to infinity: an observation window merely proportional to the escape scale cannot recover the coefficient in that regime. This is a necessary diagnostic for the model, not an asserted relation between the actual PC cutoffs. For the physical problem one must first identify which spatial tails each cutoff discards.

## 4. A quantitative extraction estimate, with its hypothesis exposed

Suppose an actual exterior function has a decomposition

    v(t)=-k exp(at)1_(t<-T)+r(t),

where r is supported in (-infinity,0] and satisfies

    C_a(r)=integral_(-infinity)^0 exp(-at)|r(t)|dt<infinity.

For L>T and 0<epsilon<a, direct integration and the triangle inequality give

    |B_(epsilon,L)(v)-k|
      <= |k|[1-exp(-epsilon T)+exp(-epsilon L)]
           +epsilon C_a(r).                           (4.1)

The last term follows from exp(epsilon t)<=1 for t<=0. Thus epsilon->0 and epsilon L->infinity recover k with a proved error, provided the weighted remainder hypothesis holds. For moving remainders one additionally needs epsilon C_a(r) to tend to zero.

This is a conditional extraction estimate, not a decomposition established for the physical defect. Other exponential modes may need subtraction before C_a(r) is finite. A meromorphic continuation alone does not imply this absolute weighted bound. Endpoint distributions also need distributional treatment rather than being inserted into the integral as functions.

## 5. Consequence for the current construction

R161_047 already located the residues outside the window; this note quantifies why weak or unweighted Hilbert convergence cannot retrieve them. R161_079 must therefore not be followed by a bare exchange of limits and Gamma-residue extraction. A valid use requires an additional weighted remainder estimate such as the hypotheses of (4.1), or direct uniform control of meromorphic germs near the pole.

Even such extraction would compute the residue, not annihilate it. The new arithmetic equality-state identity remains missing. This calculation does not supply that identity and does not justify the blanket exclusion of all linear approaches in R161_067 section 3.

Status: exact escape formulas, smooth Sobolev example and conditional two-scale extraction bound proved. No physical residue vanishing, scattering gate, or closure of D is claimed.
