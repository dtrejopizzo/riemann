# P123.057 — Comparison with the integrable source and its transgression

Status: PROVED for S_f={p,q}. This identifies two
constructed source domains and their trace operations; comparison with
the external Fourier character remains open.

## 1. A continuous inclusion into the earlier integrable domain

For f in E_S of P123.055 define b(t)=f(t,0,0) and i=f-chi_p chi_q b.
On an elementary tensor f=g tensor u tensor v these give

    b=g u(0)v(0),
    i(t,x_p,0)=g(t)v(0)(u(x_p)-chi_p(x_p)u(0)),
    i(t,0,x_q)=g(t)u(0)(v(x_q)-chi_q(x_q)v(0)).

The local relative norms therefore imply

    M_d(b)<=m_d(g)nu_p(u)nu_q(v),
    N_d(i)<=2 m_d(g)nu_p(u)nu_q(v),
    ||i||_infinity<=2||g||_infinity nu_p(u)nu_q(v).

Taking sums of tensor decompositions and their projective infimum gives
the same estimates with a fixed constant times pi_d(f). On the dense
tensor test domain, i lies in I_c and b in B_c. Hence these maps extend
to the completions I_int and B_int, not merely to measurable functions
with finite integrals.

Applying the estimates labelwise gives a continuous map

    T_{p,q} -> A_int,    f -> (i,b),
    A_kd(i,b)<=C P_kd(f).                        (1.1)

Both coefficient realizations agree with f, so P123.056 proves this map
injective. The product and star agree in the original rapid source;
thus (1.1) is an injective star homomorphism. No surjectivity onto the
weaker integrable domain is claimed.

## 2. The source extension and section agree

Evaluation at both zeros gives a continuous surjective homomorphism

    T_{p,q} -> B_int.

Here the real moment completion and rapid Gamma labels are exactly those
defining B_int. The section b -> b tensor chi_p tensor chi_q is continuous
and is the same linear section used in P123.049–053. Let K_rel be the
kernel. Then

    0 -> K_rel -> T_{p,q} -> B_int -> 0

is a strict linearly split extension mapping into the integrable extension
of P123.051, by the inclusion K_rel -> I_int, (1.1) and identity on B_int.
The diagram preserves the sections, and consequently preserves their
multiplication defects omega exactly. Thus the two constructions attach
the quotient to the ideal by the same source operation.

## 3. Identify the boundary traces as relative coefficient functionals

For f in K_rel, evaluation at both finite zeros vanishes. The boundary
trace formulas become, taking the identity Gamma coefficient,

    tau_q(f)=(integral_R tensor R_p tensor ev_q)(f_1),
    tau_p(f)=(integral_R tensor ev_p tensor R_q)(f_1). (3.1)

For instance the subtraction in R_p has coefficient f_1(t,0,0)=0,
so its relative integral equals the ordinary convergent boundary integral.
The equality holds first on tensor tests and then by continuity on K_rel.
Thus the relative coefficient operations are the actual source traces
on this kernel, not an independently assigned scalar substitute.

On the full T_{p,q}, the right sides of (3.1) instead give the linear
extensions a -> tau_v(a-s(pi(a))). They vanish on the chosen section
but need not be traces there. Their cyclic defect is precisely the
attaching transgression already computed in P123.050–051.

In particular the formulas

    c_q(x,y)=-tau_B(delta_p(x)y),
    c_p(x,y)=-tau_B(delta_q(x)y),
    (log p)c_q(x,y)+(log q)c_p(x,y)=-eta(xy-yx)

hold for the quotient of this same relative source extension, with its
actual lifted multiplication. External covariance and lift actions agree
under (1.1), since all maps are the identical coefficient dilations.

## 4. What has been joined

The semilocal relative source is now faithfully realized inside the
two-prime integrable source. Their quotient, section, attaching defect
and boundary traces agree, and hence their transgression identities agree.
This removes the domain-comparison obligation left in P123.055–056.

What remains is comparison of these source operations with the integrated
normal/Fourier relative character of P123.043–046. In particular (3.1)
is a trace on an internal crossed-product ideal, whereas W_p is an
external-test distribution; identifying them still requires a represented
source operation with the stated trace identity. Integral contact and
mixed RR must use that same operation. No full row is closed here.
