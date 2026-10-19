# P123.117 — The composition correction as a normalized graph Gram kernel

Status: PROVED-IN-REPOSITORY on sufficiently small
fixed external Bruhat test domains, using P123.109–111. This constructs
an analytic metric tied to the existing composition cocycle. It does not
identify the arithmetic determinant line or prove the Weil sign.

## 1. Normalize the graph of the actual represented operator

For the induced representation R and cutoff E=E_L, work on E H and
(1-E)H. For a small test F put

    a_F=1+E R(F)E,        c_F=(1-E)R(F)E,
    Y_F=c_F a_F^-1.                                      (1)

The identity in a_F is the identity of E H. On a fixed domain assume
the operator coefficient norm used in P123.110 is less than rho<1/4.
Then a_F is invertible with ||a_F^-1|| <= (1-rho)^-1, uniformly in L.
The operator c_F is Hilbert–Schmidt by P123.111 and so is Y_F.
The image of E H under 1+R(F) is the graph of Y_F: its two components
are a_F v and c_F v, and a_F v can be used as the new coordinate.
Thus (1) follows from the source representation and its actual
compression; it is not a separately selected positive form.

## 2. Exact finite-cutoff identity for two tests

Write A_L(F,G) for the finite-cutoff correction in P123.110, namely

    det(1+E R(F diamond G)E) / [det a_F det a_G],
    F diamond G=F+G+F*G.

The represented convolution and involution give

    1+E R(F^* diamond G)E = a_F^* a_G+c_F^* c_G
                           =a_F^*(1+Y_F^*Y_G)a_G.

All factors differ from identity by trace-class operators where a
Fredholm determinant is taken. Multiplicativity therefore yields

    A_L(F^*,G)=det(1+Y_F^*Y_G).                           (2)

In particular

    A_L(F^*,F)=det(1+Y_F^*Y_F)>=1.                        (3)

This is the composition correction itself, after normalizing the
escaping graph. It differs from the unnormalized h of P123.115.
Both have the same quadratic Levi form at zero, because
Y_(tF)=t c_F+O(t^2) in Hilbert–Schmidt norm.

## 3. Convergence as a positive endpoint Fredholm determinant

For the diagonal pair (F^*,F), let c_F^*c_F=W_L d W_L^* with fixed
positive trace-class endpoint matrix d, as in P123.115. By the
rectangular determinant identity, (3) is also

    det(1+K_L),
    K_L=d^1/2 W_L^* a_F^-1 a_F^{-*} W_L d^1/2.           (4)

Here a_F^{-*} means (a_F^*)^-1. The middle factor is positive and
converges in operator norm by the endpoint-resolvent argument of
P123.110. Since d^1/2 is Hilbert–Schmidt, K_L converges in trace norm
to a positive trace-class K_infinity. In particular

    h_hat(F):=A(F^*,F)=det(1+K_infinity)>=1,               (5)
    log h_hat(F) <= (1-rho)^-2 Tr d.

Convergence is locally uniform on fixed finite-dimensional test slices.
For mixed tests, the same resolvent estimates give (2) in the limit:

    K(F,G):=A(F^*,G)=lim_L det(1+Y_F^*Y_G).               (6)

All products and logarithms are taken in a common small neighborhood;
convolution may enlarge support, and that enlarged finite domain is
included before applying the uniform estimates. Unlike P123.115, (5)
is asserted here only in the neighborhood where the inverse exists
uniformly and the relative determinant germs have been constructed.

## 4. A positive-definite kernel, with an explicit finite-cutoff realization

For Hilbert–Schmidt maps Y from E H to (1-E)H, consider

    Psi(Y)=(1,Y, exterior^2 Y, exterior^3 Y,...)

in the Hilbert direct sum of the corresponding Hilbert–Schmidt map
spaces. Its squared norm is

    sum_k ||exterior^k Y||_HS^2 = det(1+Y^*Y)<infinity.

To justify this without an extra finiteness assumption, first truncate
in singular vectors. The finite-dimensional exterior-power identity
is the expansion of the determinant by principal minors. Its diagonal
terms are the elementary symmetric sums of the squared singular values;
these increase to a finite sum bounded by exp(||Y||_HS^2). Mixed
inner products then converge by Cauchy–Schwarz, or equivalently by
trace-norm continuity of Y_F^*Y_G and of its determinant. Thus

    <Psi(Y_F),Psi(Y_G)>=det(1+Y_F^*Y_G),                   (7)

with the inner product conjugate linear in its first variable.
For any finite tests F_i and complex scalars z_i, (7) implies

    sum_(i,j) conjugate(z_i) z_j A_L(F_i^*,F_j)>=0.

Passing to the finite matrix limit in (6) proves the same inequality
for A(F_i^*,F_j). This supplies a positive-definite analytic kernel on
the declared small test neighborhood. If desired its Hilbert space is
constructed directly: take the formal span of symbols [F], give it
inner product <[F],[G]>=A(F^*,G), quotient by zero norm, and complete.
This is a consequence of the represented operator identity (2), not
an assumption of positivity of the arithmetic intersection pairing.

## 5. Exact relation to the relative determinant and its metric

P123.110 and adjoint compatibility give

    Delta_(F^* diamond F)(1)
       = |Delta_F(1)|^2 h_hat(F).                         (8)

The left side is therefore positive real near zero. Equivalently it
is the limit of the actual positive finite-cutoff determinants

    det(E(1+R(F))^*(1+R(F))E)
             exp(-2(L+1) Re b_F(1)),                    (9)

where the determinant is on E H. The bulk identity here is
b_(F^* diamond F)=2 Re b_F, from the symbol product and adjoint.
Equation (9) retains the nonlinear counterterm; no raw infinite
Hilbert determinant is asserted.

Thus h_hat^-1 defines a metric on the trivial analytic line that is
explicitly linked to the composition cocycle. The potential log h_hat
is plurisubharmonic on finite-dimensional test slices: at finite L,
Y_F is holomorphic and (7) realizes h_hat_L as the squared norm of a
nonzero holomorphic vector, whose constant component is 1. More
explicitly its Levi form in direction U is

    ||(1+Y_F Y_F^*)^-1/2 (dY_F[U])
                          (1+Y_F^*Y_F)^-1/2||_HS^2>=0.

This follows from the differentiation in P123.116, with the holomorphic
map Y_F in place of its linear map X_F. The mixed determinant kernels
converge locally uniformly on a complexified pair of test slices by
P123.110. Cauchy differentiation there justifies passage of these Levi
forms to the limit, rather than differentiating a merely pointwise
real limit. At zero the limiting Levi form is B(U,V^*).

## 6. Compatibility and the remaining arithmetic distinction

The prescribed semilocal pullbacks preserve A by P123.110; hence they
preserve (6), (5) and (8), with exact triple compatibility. The same
holds for section changes with unitarily transported cutoffs. This
constructs a normalized graph metric and positive kernel compatible
with the already proved analytic composition law.

It does not give a multiplicative isometry for an arithmetic line,
identify this line with the mixed diagonal determinant, or prove that
its curvature is the trace-product intersection. At zero its curvature
is still the anomaly energy. The local normal counterexample P123.112
therefore still excludes using that curvature kernel unchanged as a
convolution-stable numerical radical. Nor does kernel positivity in
(6) assert positivity of Weil's distinct quadratic form. The geometric
RR comparison, ruling metric and global strata remain necessary.
