# P123.089 — A covariant full-label normal boundary representation

Status: PROVED-IN-REPOSITORY on the two-prime
boundary. Includes a finite normal-cutoff comparison for external
parameters fixing the boundary quotient; full distributional descent
and a determinant-valued comparison are not asserted.

## 1. One representation on the covering boundary and normal space

Write Z=Z_q, V=L2(Q_q), and D_u v(w)=|u|_q^(-1/2)v(w/u), as in
P123.042. On H=L2(Z,dmu_q;V) define

    (S_gamma F)(z)=D_gamma F(gamma^-1 z),
    sigma(x)=sum_gamma M_(x_gamma|Z) S_gamma.

The series converges in operator norm with ||sigma(x)||<=p_0(x).
The S_gamma are unitary, form a representation of Gamma, and satisfy
S_gamma M_f S_gamma^-1=M_(alpha_gamma f). Consequently sigma is a
unital star representation of the boundary restriction of A, preserving
the full crossed-product multiplication.

For an external idele a=(a_infinity,a_p,a_q), a_infinity>0, let a_T
act on Z by its real and p coordinates. Define

    (R_a F)(z)=D_(a_q) F(a_T^-1 z).                           (1)

The boundary measure is invariant under a_T. Thus R is a unitary
representation of the external group before quotienting by Gamma.
It is strongly continuous, as follows first on compact continuous
tangential functions and dense continuous vectors for D, and then
by density and unitarity. Commutativity of all the dilations gives

    R_a sigma(x) R_a^-1=sigma(beta_a(x)),
    R_gamma=sigma(U_gamma)  for diagonal gamma in Gamma.      (2)

In particular Pi(x,a)=sigma(x)R_a satisfies

    Pi(x,a)Pi(y,b)=Pi(x beta_a(y),ab),
    Pi(x,a)*=Pi(beta_(a^-1)(x*),a^-1).                        (3)

If a'=delta a, then Pi(x,a')=Pi(x U_delta,a), exactly the gauge
identification for twisted coefficient representatives. This is gauge
compatibility, not a claim that R_gamma acts as identity on H.

## 2. Relation to the full-label fields and the external cocycle

Choose s:B_q->Z as in P123.088. The unitary orbit decomposition with
normal change of frame is

    (UF)(y,delta)=D_delta^-1 F(delta s(y)),
    U:H -> L2(B_q;ell2(Gamma) tensor V).

Unitarity follows from the fundamental-domain integral formula and
unitarity of every D_delta. Direct substitution gives

    U sigma(x) U^-1 = pi_y(x) tensor 1_V,                     (4)

where pi is precisely P123.088, not a different scalar representation.
Define the measurable, uniquely determined c(a,y) in Gamma by

    a_T^-1 s(y)=c(a,y) s(a_T^-1 y).

Its cocycle identity is c(ab,y)=c(a,y)c(b,a_T^-1 y). In these coordinates

    (U R_a U^-1 xi)(y,delta)
       =D_(a_q c(a,y)) xi(a_T^-1 y,delta c(a,y)).              (5)

Indeed D_delta^-1 D_(a_q) D_(delta c)=D_(a_q c). Formula (5)
exhibits in one expression the external base translation, orbit-index
permutation and normal action. It proves their compatibility with (4)
without presuming that the covering representation is already the
quotient induced representation.

## 3. Actual trace comparison on the fixed-boundary sector

Suppose the external parameter fixes B_q. Equivalently there is a
gamma_0 in Gamma with

    gamma_0 a_infinity=1,   gamma_0 a_p=1.

To see the nontrivial implication, fixation of even one quotient point
means a_T^-1 z=gamma z; cancellation of its nonzero real and p
coordinates gives this condition. The real coordinate makes gamma_0
unique. In this case c(a,y)=gamma_0 for every y and the normal action
in (5) is n=gamma_0 a_q. Write
(P_gamma xi)(delta)=xi(delta gamma). Then

    U Pi(x,a) U^-1=(pi_y(x) P_(gamma_0)) tensor D_n.

For x in J_W and a finite normal projection E=E_MN of rank q^L,
the fiberwise compression is trace class almost everywhere, with
integrable trace norm bounded by q^L j_00(x). Its integrated fiber
trace is

    integral_(B_q) Tr((1 tensor E) U Pi(x,a) U^-1
                                      (1 tensor E)) dy
       = Tr(E D_n E) integral_(Z_q) x_(gamma_0) dmu_q.        (6)

Indeed the diagonal of pi(x)P_(gamma_0) is
x_(gamma_0)(delta s(y)); all other labels miss that diagonal.
P123.088 supplies trace-norm integrability, and P123.087 integrates
this diagonal by periodization. Using the exact finite-cutoff formula,
equation (6) becomes

    |n|_q^(1/2) min(q^L,|1-n|_q^-1) T_(q,a)(x).             (7)

For n!=1 this is eventually exactly
|n|_q^(1/2)/|1-n|_q times T_(q,a)(x). Thus the full-label twisted
boundary functional and its normal factor from P123.086 now occur
as a trace of a specified covariant representation and cutoff.
At n=1 the actual factor is q^L; no finite pointwise value is assigned.

## 4. Remaining scope

The trace in (6) is an integrated fiber trace. It is not an ordinary
trace on the full direct-integral Hilbert space. When a moves B_q,
the operator in (5) is not decomposable over that base, so (6) cannot
be applied to it. Integrating external tests, controlling the resulting
operator kernel and matching quotient descent with P123.043–087 are
still required for a full distributional comparison.

This step constructs the joint normal/full-label action and identifies
its fixed-boundary trace, including exact gauge and star identities.
It does not establish a determinant line or the mixed RR of row A.
