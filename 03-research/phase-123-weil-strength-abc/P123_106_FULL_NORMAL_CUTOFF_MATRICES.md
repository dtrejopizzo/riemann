# P123.106 — Exact normal cutoff matrices including nonunit dilations

Status: PROVED-IN-REPOSITORY for every compact
multiplicative Bruhat test on Q_q^*. This computes the finite normal
determinants; their renormalized limit is a further step.

Use counting measure on valuations and probability unit Haar. Let phi
be supported on valuations |k|<=K and invariant under U_ell in its unit
argument, with ell>=1. Define

    a_(k,chi)=integral_U phi(q^k u)chi(u)^-1 du,
    A(phi)=sum_k integral_U phi(q^k u) D_(q^k u) du.

Only finitely many chi, of conductor <=ell, have nonzero coefficients.
Write E=E_MN, L=M+N>=ell, r=q^-1/2 and b=sqrt(1-q^-1).

## 1. Nontrivial unit characters give ordinary finite shifts

For a nontrivial chi of conductor c, use normalized shell functions
supported on q^j U with angular value chi(u), for

    -M <= j <= N-c.

These form the chi-isotypic part of the cutoff range, of dimension
n_chi=L-c+1. Local constancy modulo q^N holds precisely when N-j>=c;
on deeper shells the character averages to zero in the central coset.
Unit dilation acts by chi(u)^-1, so A(phi)'s unit Fourier coefficient
on this subspace is exactly a_(k,chi).

Normal dilation D_q carries the normalized shell at j to that at j+1.
Let T_n be the shift e_j->e_(j+1) for j<n-1 and e_(n-1)->0. For any
k>=1, compression of D_(q^k) is T_n^k: a shell shifted out of the
retained interval has zero projection, and positive shifts do not return.
Negative powers compress to (T_n*)^k by adjoints. Consequently the block is

    A_(L,chi)=a_(0,chi) I
       +sum_(k=1)^K [a_(k,chi) T_(n_chi)^k
                           +a_(-k,chi) (T_(n_chi)*)^k].     (1)

This is an exact finite Toeplitz matrix, not a compression assumed to
preserve all products.

## 2. The trivial character has an explicit central-ball boundary

For the trivial character use normalized indicators of the shells
j=-M,...,N-1, followed by the normalized indicator v_N of q^N Z_q.
There are L+1 vectors. Define S_L on this ordered orthonormal basis by

    S_L e_j=e_(j+1) for 0<=j<L-1,
    S_L e_(L-1)=b e_L,
    S_L e_L=r e_L.                                         (2)

The penultimate coefficient is the inner product of the normalized
shell q^N U with v_N, namely b. The last is the inner product of
v_(N+1)=D_q v_N with v_N, namely r. These facts prove S_L=E D_q E
on this block.

For positive k, the compression of D_(q^k) is S_L^k as well. A shell
that ends at j+k<N stays a shell; if j+k>=N its projection onto v_N
has coefficient b r^(j+k-N). Also v_N is carried to v_(N+k), whose
projection coefficient is r^k. These are exactly the entries of S_L^k.
Negative powers again follow by adjoints. The complete trivial block is

    A_(L,1)=a_(0,1)I
       +sum_(k=1)^K [a_(k,1)S_L^k+a_(-k,1)(S_L*)^k].       (3)

The weights in (2) retain the actual additive normal cutoff and its
half-density normalization. Replacing this block by an ordinary
truncated shift would lose its nonunit diagonal trace.

## 3. Full determinant and recovery of the prescribed trace

All unit-isotypic blocks are orthogonal and invariant under the cutoff
and A(phi). The blocks with zero coefficients contribute determinant one.
Therefore the exact finite-rank Fredholm determinant is

    det(1+z E A(phi) E)
       =det(1+z A_(L,1))
                    product_(chi!=1) det(1+z A_(L,chi)).     (4)

This includes arbitrary finite combinations of positive and negative
valuation shifts. It reduces to P123.105 when K=0.

The positive powers of T_n have trace zero. The matrix S_L is triangular
with only one nonzero diagonal entry r, so Tr(S_L^k)=r^k for k>=1;
the same trace holds for adjoints. Taking the trace of (1) and (3) gives

    Tr(E A(phi) E)
       =(L+1)sum_chi a_(0,chi)-sum_chi c(chi)a_(0,chi)
                     +sum_(k!=0) q^(-|k|/2) a_(k,1).       (5)

Since sum_chi a_(0,chi)=phi(1), subtracting (L+1)phi(1) recovers
the unit conductor contribution of P123.105 and every off-unit term
of P123.042. Multiplication by log q gives that note's multiplicative
Haar normalization. Thus (4) has the required full local trace as its
renormalized first logarithmic derivative.

## 4. Product limitations and the next estimate

The formulas for positive powers do not imply multiplicativity for
mixed signs: T_n T_n* and T_n* T_n have different endpoint defects,
and (2) has its additional central-ball term. Those are actual boundary
corrections to products and must enter higher logarithmic traces.

Equation (4) supplies a finite-matrix starting point for all those
traces, rather than assuming a counterdeterminant from the first trace.
Its stabilized determinant limit, coupling to the tangential induced
operator and identification with the geometric/arithmetic RR determinant
are not yet proved here. Full row A remains open.
