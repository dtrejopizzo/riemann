# P123.056 — Faithful realization of the semilocal relative coefficients

Date: 2026-09-05. Status: PROVED by explicit finite-rank approximations.
This resolves the coefficient-faithfulness requirement in P123.055.

## 1. Local finite-place approximations

In E_p write f=f(0)chi_p+r, where r(0)=0 and r is multiplicatively
integrable. Let A_N={x:-N<=v_p(x)<=N}. Partition this compact open set
into finitely many compact open cells refining valuation shells, with
mesh tending to zero as N grows. Let Q_N r be its multiplicative Haar
cell averages, extended by zero outside A_N. Define

    F_p,N f=f(0)chi_p+Q_N(f-f(0)chi_p).

This is finite rank, preserves evaluation at zero, and has Bruhat output.
Its residual L¹ norm is at most that of r. Its supremum norm is at most
|f(0)|+||r||_infinity<=3||f||_infinity. Therefore

    nu_p(F_p,N f)<=3 nu_p(f).

For each Bruhat test, the residual is compactly supported away from zero
and locally constant, so F_p,N f=f for sufficiently fine and large N.
Uniform boundedness and density prove F_p,N f -> f in E_p for all f.

Every scalar coefficient of F_p,N is a finite linear combination of
evaluation at zero and integrals of f against finite measures supported
on compact cells away from zero. In particular these coefficient
functionals are continuous on C_0(Q_p) with its supremum norm, even
though their bounds need not be uniform in N.

## 2. Real finite-rank approximations

For mesh h=1/N, put centers t_j=jh and cells
I_j=[t_j-h/2,t_j+h/2]. Let l_j(t)=max(1-|t-t_j|/h,0) be the triangular
hat at t_j. Define

    F_infinity,N g(t)
       =sum_(|j|<=N²) l_j(t) h^-1 integral_(I_j) g(u)du.

This has finite rank and compactly supported continuous output. Such
outputs belong to E_infinity by smooth compact approximation. The hats
sum to at most one, giving the supremum bound ||F_N g||<=||g||.
Their integrals are h. On a cell and its hat support, |t-u|<=3h/2, so

    integral (1+|t|)^d |F_N g(t)|dt
       <= (5/2)^d integral (1+|u|)^d |g(u)|du.

Thus F_N is uniformly bounded in each m_d. For a smooth compact test,
cell averaging and hat interpolation converge uniformly with support
in a fixed compact set, hence converge in every m_d. Density gives
convergence for all E_infinity. Its scalar coefficients are integrations
against finite compactly supported measures, continuous in the C_0 norm.

## 3. Tensor approximation detects every coefficient

Tensor these maps over the finitely many places to obtain finite-rank
operators F_S,N on E_S of P123.055. Their projective pi_d bounds are
uniform in N for each d, by sections 1–2. They converge to identity on
elementary tensors, and hence on E_S by density and those bounds.

Let rho_S:E_S -> C_0(X_S^+) be coefficient realization. Each coordinate
functional of F_S,N is a finite sum of products of the finite measures
and evaluations above. Thus it equals integration of rho_S(f) against
a finite product measure. The equality holds first on elementary tensors
and then on the completion, since both sides are continuous there.

If rho_S(f)=0, every such coordinate is zero and F_S,N f=0 for all N.
Taking the limit in E_S gives f=0. Therefore rho_S is injective.

This proof uses approximations adapted to the declared relative norms;
it does not assume that arbitrary completed projective tensor products
of injective maps remain injective.

## 4. Consequences for the semilocal crossed algebra

Coefficientwise realization now gives an injective continuous star
homomorphism from T_S into the original rapid C_0 crossed algebra on
X_S^+. Continuity follows from ||rho_S(f)||_infinity<=pi_d(f), and
injectivity follows at each Gamma label. Multiplication agrees because
the realization intertwines the actual dilation action.

The chart maps j_ST of P123.055 realize exactly the original coefficient
maps adding product chi_ell on old labels. Hence the semilocal relative
algebras are actual source subalgebras with their specified stronger
topologies, not merely abstract algebras with a possibly nonfaithful
coefficient map. This does not assert that their images are closed in
the weaker original rapid topology.

The remaining comparisons are with the two-prime integrable extension,
its cyclic transgression and the external Fourier relative character.
Faithful coefficients alone do not establish those trace identities,
integral diagonal contacts, mixed RR or the global D sign.
