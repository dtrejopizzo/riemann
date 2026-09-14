# P123.046 — One generic Hilbert realization for all finite boundary charts

Date: 2026-09-05. Status: PROVED for the explicit unitary identifications
and finite-place cutoff character on one Hilbert space. This is not yet
an excisive categorical shadow or its nuclear comparison.

## 1. Convert the normal half-density to multiplicative Haar

Retain G=H_S and K_p=Q_p^* with Haar dk_p=counting times probability
unit Haar, as used in induction in P123.043. With additive Haar dx
normalized by vol(Z_p)=1, put c_p=1-p^-1. Then

    dk_p = dx/(c_p |x|_p).

Since {0} has additive measure zero, the map

    T_p:L²(Q_p,dx) -> L²(Q_p^*,dk_p),
    (T_p v)(x)=sqrt(c_p |x|_p) v(x)

is unitary. Direct substitution into the definition of D_a gives

    T_p D_a T_p^-1 w(x)=w(a^-1 x).                 (1.1)

Thus the uncut normal representation is the multiplicative regular
representation. Its information about the zero boundary is retained
by the additive/Fourier cutoffs, not by an additional L² summand at zero.
This distinction is necessary when transporting a relative trace.

## 2. Identify every induced chart with the same regular representation

Let H_p be the induced space in P123.043. For phi in L²(G,dg), define
U_p phi by the following formula for its fiber, for x!=0:

    (U_p phi)(g)(x)
       = phi(g j_p(x))/sqrt(c_p |x|_p).            (2.1)

This is interpreted as an equality of measurable sections up to null
sets, using the quotient integral formula, not as point evaluation of
an arbitrary L² class at a fixed point. Changing g to g j_p(a) gives
exactly D_a^-1 on the fiber, so the required equivariance holds.

The quotient integral formula proves

    ||U_p phi||²
      = integral_(G/K_p) integral_(K_p)
                       |phi(s(y)k)|² dk dy
      = ||phi||².

Conversely, multiplying an equivariant fiber section by
sqrt(c_p|x|_p) reconstructs a measurable function at s(y)j_p(x);
equivariance makes the reconstruction independent of representatives.
This gives the inverse and proves surjectivity. Left translation gives

    U_p lambda_G(h)=rho_p(h) U_p,
    U_p lambda_G(f)=R_p(f) U_p.                   (2.2)

For any p,q the chart transition U_q U_p^-1 is unitary and intertwines
the full external action. These transitions compose exactly on triples.
Geometrically (2.1) is the half-density version of the common generic
orbit identification G times_(K_p) Q_p^* = G in P123.044.

## 3. Transport all normal cutoffs onto that common space

Write E_p,MN for the fiberwise projection in the fundamental section
of P123.043 and set

    C_p,MN = U_p^-1 E_p,MN U_p

on L²(G). It is an orthogonal projection, generally of infinite rank.
The trace-class operators of P123.043 become

    C_p,MN lambda_G(f) C_p,MN.

Their relative traces satisfy, for L=M+N sufficiently large for the
unit level of f,

    Tr(C_p,MN lambda_G(f) C_p,MN)
       - (L+1)(log p) f(1) = W_p(f).              (3.1)

The projections depend on p, its additive Fourier geometry, and the
specified fundamental section. They must not be identified just because
the uncut representations are unitarily equivalent. Equation (3.1)
shows explicitly how different boundary functionals can arise from
the same regular representation with different geometric cutoffs.

## 4. A finite-place relative character without duplicating the Hilbert space

For a finite subset P of S_f, choose cutoffs with L_p beyond each required
unit level. The finite sum

    B_P(f)=sum_(p in P) C_p,M_pN_p lambda_G(f) C_p,M_pN_p

is a trace-class operator on the single space L²(G). Linearity of the
ordinary trace and (3.1) yield the exact equality

    Tr B_P(f) - f(1) sum_(p in P)(L_p+1)log p
       = sum_(p in P) W_p(f).                    (4.1)

No orthogonality or commutation of different C_p is required or claimed.
In particular B_P is not asserted to be a compression by their sum,
nor a representation. The convolution representation is lambda_G;
B_P is the explicit regularization operation applied to it.

For S contained in T, pullback J_ST on the regular spaces is an isometry
with probability Haar on the new units. Formula (2.1) intertwines it
with the induced-space pullback in P123.043, since j_(T,p) projects to
j_(S,p), c_p is unchanged, and the extra coordinates are integrated with
probability measure. The transported old-prime compressions therefore
have the same chart intertwining identities and relative traces.

For a global test of finite unit level and real-log support [-R,R],
P123.032–033 restrict nonzero finite-place contributions to the finite
set consisting of its ramified unit primes and primes p<=exp(R).
One can choose S containing that set and apply (4.1) there. This is a
testwise finite construction. It does not assert convergence of an
infinite sum of cutoff operators for a fixed cutoff size.

## 5. Consequence for the remaining descent problem

The local normal representations no longer need to be glued as unrelated
Hilbert spaces: they already have the same generic realization, with
explicit coherent unitaries. What still must descend is the regularization
data and its relative character through the rapid source sequences of
P123.045. Unitary equivalence of uncut representations alone is insufficient
to prove this, because it does not identify their different cutoffs.

Equation (4.1) constructs the finite-place scalar packet on one actual
external representation. It does not show that B_P is the image of a
single source localization operation, give its value on the multiple-zero
complement, or identify it with the integral contact determinant, mixed RR,
the archimedean term or the nuclear spectral realization. Those remain
load-bearing requirements. No positivity or completed row is asserted.
