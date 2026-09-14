# P123.087 — Boundary periodization and a weighted operator comparison

Date: 2026-09-06. Status: PROVED-IN-REPOSITORY on a single-zero
two-prime boundary, for integrable scalar coefficients and external
Bruhat tests. This compares actual weighted normal compressions with
the coefficient boundary trace. It is not a correspondence functor
on the full mixed category or a determinant-valued RR theorem.

## 1. Periodization with the source measure

Take Z_q=R times Q_p^*, with coordinates (t,x), measure dt d^*x,
unit Haar mass one, and Gamma=<p,q> acting by

    gamma.(t,x)=(t+log gamma,gamma x).

The action is free and proper. Indeed, if a compact set and its gamma
translate meet, bounded p-adic valuations bound v_p(gamma); bounded
real coordinates then bound v_q(gamma). Only finitely many gamma occur.
First normalize v_p(x) to zero by a power of p, and then reduce t
modulo log q by a power of q. A measurable fundamental domain is

    D_q={0<=t<log q, x in Z_p^*}.

Its translates tile Z_q up to null boundaries. The quotient B_q is the
compact mapping torus in P123.041, with total measure log q. For h in
L1(Z_q), define

    Ph([z])=sum_(gamma in Gamma) h(gamma z).                    (1)

The absolute sum is finite almost everywhere by Tonelli on D_q, and

    ||Ph||_(L1(B_q))<=||h||_(L1(Z_q)),
    integral_(B_q) Ph=integral_(Z_q) h.                        (2)

This constructs the quotient density, rather than identifying a
covering-space integral with a quotient integral without periodization.

There is an explicit nonnegative compact cutoff with Pc=1. Choose
theta in C_c^infinity(R), theta>=0, with
sum_(n in Z) theta(t+n log q)=1, and set

    c(t,x)=theta(t) 1_(Z_p^*)(x).

For any x, exactly one p exponent in (1) places x in Z_p^*; the
remaining q sum is the theta partition. Hence Pc=1 and integral c=log q.
Such theta is obtained by taking a nonnegative bump whose translates
cover R and dividing by its strictly positive periodic translate sum.
The cutoff extends to a compact coefficient in J_W by multiplication
by 1_(Z_q)(x_q). It therefore lies in the trace domain of P123.085.

## 2. Weighted trace-class compressions for L1 quotient densities

Use the induced normal representation and regular fundamental section
of P123.043, now at q. For an external Bruhat test f and the finite
normal cutoff E=E_MN, L=M+N>=0, write

    B_L(f)=E R(f) E.

Its matrix kernel K_L(f;y,z) is smooth in the two real coordinates
and factors through a finite quotient of the tangential unit variables.
The smooth extension/Fourier argument of P123.043 gives a rank-one
expansion whose coefficient absolute sum, times the supremum norms
of both vectors, is finite. This stronger form follows by using the
bounded Fourier exponentials on a larger interval, the finite unit
indicator basis and the finite normal basis.

Let a be any complex L1 function on B_q. Put r=|a|^(1/2) and
s=phase(a)|a|^(1/2), assigning phase zero where a=0. Define C_(L,a)(f)
by the kernel

    r(y) K_L(f;y,z) s(z).                                    (3)

This is well-defined and trace class without assuming the multiplication
operators by r or s bounded. In fact, applying them to the bounded
vectors in the preceding rank-one expansion gives L2 vectors; the
trace norm of each term is bounded by its coefficient times the two
sup norms times ||a||_1. Thus the transformed series converges in
trace norm and defines (3), independently of its series presentation.
The diagonal trace formula follows from that same absolutely summable
series:

    Tr C_(L,a)(f)=integral_(B_q) a(y) tr K_L(f;y,y) dy.         (4)

The assignment a -> C_(L,a) need not be linear with this sandwich
choice; its trace in (4) is linear and continuous in a. No unbounded
operator product is being declared trace class without this construction.

## 3. Actual comparison with the integrable coefficient trace

The diagonal fiber trace in the chosen section is constant in y:

    kappa_L(f)=integral_(K_q) f(k) Tr(E D_k) dk,
    tr K_L(f;y,y)=kappa_L(f).

This uses abelianity of the external group and the kernel calculation
of P123.043. For a=Ph, equations (2) and (4) now give the operator
identity at the level of traces

    Tr C_(L,Ph)(f)=kappa_L(f) integral_(Z_q) h.                (5)

In particular take h to be the restriction of the identity coefficient
of x in J_W. Its integral is exactly tau_q(x), so (5) compares the
same declared coefficient trace domain with an actual trace-class
normal compression. No boundedness of Ph is needed.

If ell is a unit constancy level of f restricted to K_q near identity,
P123.042–043 give, for every L>=ell,

    kappa_L(f)-(L+1)f(1)=W_q(f)/(log q).

Consequently the eventual weighted relative trace is

    Tr C_(L,Ph)(f) -(L+1)f(1) integral h
         = (integral h)/(log q) W_q(f).                       (6)

For the explicit cutoff c with Pc=1, the sandwich is the original
B_L(f), integral c=log q, and (6) is exactly its unweighted relative
character W_q(f). Any other integrable cutoff with periodization one
gives the same quotient density, operator and relative character.
This accounts for the logarithmic factor through the actual quotient
measure. It does not insert that factor as a chosen normalization of h.

## 4. What this adds and what it does not identify

This supplies a distributional external test pairing, including the
normal identity counterterm, for each integrable boundary density.
It avoids the invalid procedure of integrating the pointwise fixed-label
traces of P123.086 with ambient Haar: the external test is integrated
in R(f) before the trace is taken. Formula (6) is continuous in the
L1 boundary density and in the usual Bruhat test topology for f.

For a general crossed-product coefficient x, this construction uses
only h=x_1 restricted to Z_q. It does not identify all label-dependent
twisted shadows of P123.086 with the induced operator representation.
Nor is periodization asserted to preserve coefficient multiplication,
and the sandwich in (3) is not a convolution representation in a.
Therefore mixed composition, a full correspondence realization and its
determinant/RR comparison still require additional construction. The
proved bridge is the integrable scalar boundary-density sector (5)–(6).
