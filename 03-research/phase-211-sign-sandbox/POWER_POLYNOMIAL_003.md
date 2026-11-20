# POWER_POLYNOMIAL_003 — Polynomial coordinates and exact dilations

Status: PROVED identities. OPEN uniform sign. The certificate for degrees 0,1,2 by rational arithmetic is being computed separately in `signo`; it is not duplicated here. Papers untouched.

Antecedents: the project rules/index/grid/crossword consulted in POWER_BRIDGE_002. The Pick reduction and matrix elimination are known. Explicit difference: the bridge now proved allows fixing a single ladder 32+n; here its full form is written in a Jacobi basis with exact measures and dilations. The aim is to keep polynomial cancellations, without claiming that new coordinates imply a sign.

## 1. Exact form on polynomials

Let h(y)=exp(-63y/2)P(exp(-y))1_(y>0), P real. Put z=exp(-y) and

    <P,Q>_J=∫_0^1 z^62 P(z)Q(z) dz,
    D_n P(z)=P(z/n).

Then ||h||²=<P,P>_J and the comb is exactly

    Comb[P]=−2 Σ(n>=2)Lambda(n)n^-32 <P,D_nP>_J.             (C)

P(z/n) is not extended by zero nor is its domain cut: for the autocorrelation one evaluates h(y+log n), and y>0 already satisfies both restrictions. The polar term is exactly

    Polar[P]=2 (∫_0^1 z^30 P(z)dz)(∫_0^1 z^31 P(z)dz).       (P)

If P=Σp_i z^i, the archimedean part has matrix

    A_ij=[psi((32+i)/2)+psi((32+j)/2)−2log pi]/[2(63+i+j)].  (A)

Thus C+P+A reproduces the kernel of POWER_CONE_001 in coefficients of the images h, without zeta factors. The images of the data rho have coefficients p_i=c_i zeta(32+i); the diagonal transformation is invertible and positive.

## 2. Explicit Jacobi basis

Let q_j be the monic orthogonal polynomials for z^62 dz. By Rodrigues,

    q_j(z) = z^-62 /[j! C_j] d^j/dz^j [z^(62+j)(z-1)^j],
    C_j=binom(62+2j,j),
    ||q_j||²_J=1/[(63+2j) C_j²].

First cases:

    q0=1,                         norm²=1/63,
    q1=z−63/64,                  norm²=1/(65·64²),
    q2=z²−64z/33+4032/4290,       norm²=1/(67·2145²).

The orthonormal basis is e_j=sqrt(63+2j) C_j q_j. Using monomials numerically is not advisable: their near-cancellations near z=1 disappear in this exact normalisation.

For r>-1, integration by parts in Rodrigues gives

    ∫_0^1 z^r q_j(z)dz = (r-62)_(j) /[C_j (r+1)(r+2)...(r+j+1)],

where (x)_(j)=x(x-1)...(x-j+1). It applies to r=30,31 and gives all polar moments as rational products. Each polar diagonal is positive because both moments have sign (-1)^j; that does not imply positivity of the full polar matrix.

## 3. Matrix of the dilations

In any finite degree d, D_n preserves polynomials of degree ≤d and is triangular in the basis q_j, with diagonal n^-j. If q_j(z)=Σ_l a_jl z^l,

    <q_i,D_n q_j>_J = Σ(k,l) a_ik a_jl n^-l /(63+k+l).       (D)

All factors except the arithmetic sums are rational. After summing Λ(n)n^-32, each entry uses exclusively the values −zeta'(32+l)/zeta(32+l). Hence this coordinatisation creates no new arithmetic information: it organises exactly the same matrix.

First images, useful for checking implementations:

    D_n q0=q0,
    D_n q1=n^-1 q1+(63/64)(n^-1−1)q0.

Although the eigenvalues n^-j are positive and ≤1, D_n is not self-adjoint for z^62dz. It cannot be replaced by a positive contraction. The off-diagonal term of D_n q1 already shows this in degree one; diagonalising dilations and forgetting the metric would lose the sign.

## 4. Concrete test that this representation allows

For d=2, form A by (A), C by (D) and P by the two rational moment vectors. Conjugate by the matrix of q0,q1,q2 and then by their exact norms. The sign certificate must be applied to the FULL sum. Neither the positive polar diagonals nor the eigenvalues of D_n are certificates. The entries can be reduced to rationals, gamma, log pi, log2 and three Dirichlet sums with signed remainders, as the independent computation `signo` is doing.

For increasing degrees, the additional falsifiable target is to find a shape estimate in the basis e_j that controls the blocks of C+P against A without losing the cancellations of the triangular term D_n. No such inequality has been obtained here. The demonstrated advantage is exactness of coordinates and normalisation; no new proof of the sign is claimed.
