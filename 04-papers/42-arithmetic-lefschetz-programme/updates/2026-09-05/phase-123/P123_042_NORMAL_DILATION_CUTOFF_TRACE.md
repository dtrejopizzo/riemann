# P123.042 — Actual normal dilation and its finite-rank relative trace

Date: 2026-09-05. Status: PROVED for the local operator and eventual
relative-trace identity below. The common global shadow and its mixed
Riemann–Roch comparison remain open.

## 1. Normal representation and a genuine finite-rank cutoff

Use the self-dual additive measure and character of P123.034 on Q_p.
On H=L²(Q_p), define the unitary representation

    D_x v(z)=|x|_p^(-1/2) v(z/x),   x in Q_p^*.

It satisfies D_x D_y=D_xy and D_x^*=D_(x^-1). For a compactly supported
locally constant multiplicative test a, D(a)=integral a(x)D_x d^*x
is bounded and preserves convolution and involution. Here vol(Z_p^*)
for d^*x is log p, as in P123.032–034.

Let P_M multiply by 1_(p^-M Z_p), and let Q_N be the Fourier projection
onto frequencies p^-N Z_p. Its additive kernel is

    Q_N(z,w)=p^N 1_(p^N Z_p)(z-w).

Take integers M,N with L=M+N>=0. Since the position ball is a union
of p^N Z_p cosets, P_M and Q_N commute. Thus E_MN=P_M Q_N is an
orthogonal projection of rank p^L, onto functions supported on the
position ball and constant on these cosets. Taking M=N tending to
infinity gives a strong approximation to the identity.

## 2. Exact normal trace, before any limiting operation

The kernel of E_MN D_x is

    |x|_p^(1/2) p^N 1_(p^-M Z_p)(z)
                         1_(p^N Z_p)(z-xw).

The finite-rank trace is its diagonal integral. This can also be checked
directly on the normalized indicator basis of the p^L position cosets;
no distributional diagonal of the identity is being used. Consequently

    Tr(E_MN D_x)
      = |x|_p^(1/2) min(p^L, |1-x|_p^-1),       (2.1)

with the minimum interpreted as p^L at x=1. Indeed the diagonal
integration domain is the intersection of p^-M Z_p and
(1-x)^-1 p^N Z_p. Its measure is the smaller of their measures.

For x outside Z_p^*, |1-x|_p>=1; hence for every L>=0 (2.1) is already
the exact normal factor |x|_p^(1/2)/|1-x|_p. In particular x=p^k u,
k!=0, gives p^(-|k|/2), with no asymptotic error.

The cutoff operators themselves are not a representation. Composition
belongs to D, before applying E_MN; we make no multiplicativity claim
for a -> E_MN D(a).

## 3. The identity divergence is explicit

For probability Haar du on U=Z_p^*, put

    I_L = integral_U min(p^L, |1-u|_p^-1) du.

For L=0 it equals 1. For L>=1 the shell v_p(1-u)=0 has measure
(p-2)/(p-1); each shell r>=1 has measure p^-r, and
vol(1+p^L Z_p)=p^-L/(1-p^-1). Therefore

    I_L=(p-2)/(p-1)+(L-1)+p/(p-1)=L+1.          (3.1)

This includes p=2: the first shell then has measure zero.

Choose a unit level ell>=1 such that a(u)=a(1) on 1+p^ell Z_p.
For L>=ell, subtracting a(1) in the unit integral removes every place
where the minimum differs from |1-u|_p^-1. Equations (2.1)–(3.1) give
the exact, eventually constant expression

    Tr(E_MN D(a)) - (L+1)(log p)a(1)
      = integral_(v_p(x)!=0) a(x) |x|_p^(1/2)/|1-x|_p d^*x
        + (log p) integral_U (a(u)-a(1))/|1-u|_p du.   (3.2)

Interchanging the finite-rank trace and the group integral is justified
by compact support, boundedness of D_x, and the finite rank of E_MN.
The last unit integral is an ordinary convergent integral since its
numerator vanishes on a neighborhood of 1.

## 4. Comparison with the prescribed Fourier distribution

Given an external test f on H_S, set a(x)=f(j_p(x)). This is a compact
multiplicative Bruhat test: compact real-log support bounds v_p(x),
and the finite unit level supplies local constancy. Then a(1)=f(1).
The right side of (3.2) is precisely the off-unit plus unit packet of
P123.032–033. By the local distribution calculation in P123.034, it is

    <-F(log|y|_p), G_a(1-y)>,
    G_a(x)=|x|_p^(-1/2)a(x), extended by zero near x=0.

Thus that normalization is now realized by an actual unitary normal
action and a finite-rank relative trace, rather than only by matching
a formal Jacobian. The counterterm is (L+1)log p, not L log p; dropping
the constant 1 would change the unit packet by (log p)f(1).

For S contained in T and p old, j_(T,p) projects to j_(S,p). Hence
restriction of P_ST f to Q_p^* is exactly a again, and all operators
and relative traces in (3.2) coincide on these charts. This is local
compatibility, not yet a sum over all boundary strata.

## 5. What this supplies to the common-carrier construction

P123.041 supplies the integrated tangential orbit trace and its log p
volume. This note supplies the normal representation, its cutoff trace,
and the required identity subtraction. Our choice vol(U)=log p already
includes that orbit factor; it must not be multiplied by log p again.

To combine these as one operator on the semilocal source requires the
associated normal coefficient construction over H_S/K_(S,p), compatible
cutoffs and a localization statement. Restriction f -> f compose j_p
does not preserve convolution from H_S to K_(S,p), so D(a) alone is
not a representation of the full external test algebra. Induction over
the compact tangential quotient is the next necessary operation.

Higher-zero strata, the integral contact comparison, the archimedean
term and the global mixed shadow are not proved by this local identity.
No positivity or full A/B/C/D closure is asserted.
