# P123.031 — continuous ideal traces extend, but local Jacobians do not glue

Date: 2026-09-05. Status: PROVED for the trace-extension theorem and
the explicit chart counterexample. The external nuclear trace comparison
remains OPEN.

## 1. The rapid kernel ideal has an approximate identity

Use A,D,e,i from P123.030 and K=ker e. Choose a net of compactly
supported continuous functions u in C_0(X_S), 0<=u<=1, converging to
1 uniformly on every compact subset. Regard u as a coefficient at the
identity group label. Then p_k(u)<=1 for every k.

For b=sum_g f_g U_g in K, the coefficients of ub and bu are
u f_g and f_g alpha_g(u), respectively. Each converges uniformly to
f_g for fixed g. Their differences are bounded by 2||f_g||, so
weighted summability and finite-tail approximation give

    ub -> b,   bu -> b,  in every rapid seminorm.

This is a bounded two-sided approximate identity in the stated Frechet
sense; it is not convergence of u to 1 in A.

## 2. Extension theorem

Let tau:K -> C be any continuous linear trace, meaning
 tau(kl)=tau(lk) for k,l in K. Then it is central under multiplication
by all a in A:

    tau(ak)=tau(ka),   a in A, k in K.

Indeed ua lies in K, so tau((ua)k)=tau(k(ua)). The left side tends to
tau(ak), using u(ak)->ak. The right side tends to tau(ka), using
ku->k and continuity of multiplication by a.

Let pi=id-i e:A -> K. Define the split-relative extension

    tau_tilde(a)=tau(pi(a)).

It is continuous, restricts to tau, and vanishes on i(D). To check
cyclicity, write a=i(d)+k and b=i(c)+l. Since D is commutative,
their commutator is [k,l]+[i(d),l]+[k,i(c)]. All three terms are in K
and have trace zero by the trace property and the preceding centrality.
Thus tau_tilde is a trace on A. It is the unique linear extension
vanishing on i(D); arbitrary continuous functionals on the commutative
quotient D can be added to obtain other traces.

This theorem addresses insertion of units for traces continuous on the
whole K. It does not establish that a particular nuclear or cutoff trace
has that domain and continuity. Moreover a nonzero extension vanishing
on 1 is not a positive functional: positivity on a unital star algebra
and tau_tilde(1)=0 would force it to vanish by Cauchy-Schwarz.
No geometric effectivity is obtained from this extension.

## 3. A local continuous trace with an explicit free identity parameter

For positive S-units g != 1 set

    w_S(g)=1/|1-g|_S.

The product norm |g|_S is 1, so this agrees with the off-identity
half-density Jacobian in P123.006, equation (5.3). The rational product
formula gives |1-g|_S>=1: outside S, g is a unit and |1-g|_v<=1.
Thus 0<w_S(g)<=1. Choose any real constant c and set w_S(1)=c.
Then

    tau_(S,c)(b)=sum_g w_S(g) f_g(0),  b in K,

is continuous, bounded by max(1,|c|) p_0(b). Evaluation at the additive
origin is an algebra homomorphism from K to the commutative scalar label
algebra, because all gauge dilations fix 0. Hence this functional is a
trace. Also w_S(g^-1)=w_S(g), giving compatibility with the involution.

The arbitrary c makes the limitation explicit: this construction does
not determine the physically renormalized identity contribution. Its
extension from section 2 is a trace of the internal gauge algebra, not
Meyer's external idele-class character.

## 4. Failure of naive chart compatibility away from the identity

Take S={infinity,2}, T={infinity,2,3}, and g=4. Choose f in C_c(X_S)
with f(0)=1. The repaired embedding sends f to f tensor 1_Z3, which
still has value 1 at the origin. But

    w_S(4)=1/3,    w_T(4)=1/(3*(1/3))=1.

Therefore tau_(T,c') j_ST(f U_4) != tau_(S,c)(f U_4), independently
of both identity parameters. The canonical split extensions cannot
fix this mismatch because they agree with the original traces on K.

A scalar label correction is also not automatically a repair. The
ratio w_T(g)/w_S(g)=|1-g|_3^-1 is 1 at g=2 and 3 at g=4. It is not
a multiplicative character. If a unital algebra map rescales U_g by
r(g), the identity U_2^2=U_4 forces r(4)=r(2)^2, which these ratios
(and their reciprocals) violate. Thus simply rescaling the existing
chart homomorphism cannot enforce this trace equality.

This is a failure of naive compatibility for the additive fixed-point
Jacobian traces, not a refutation of semilocal trace formulas: quotient
strata, external dynamics and renormalization are additional data there.
The next C comparison must construct those operations and their transition
law rather than identify the local trace family with a glued character.
