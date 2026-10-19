# P123.107 — Convergence of the full normal relative determinant germ

Status: PROVED-IN-REPOSITORY for each compact
multiplicative Bruhat test on Q_q^*, with the normal cutoff of P123.042.
The limit is local in the determinant variable. Global meromorphic
continuation, multiplicativity and the arithmetic RR comparison are not
inferred from this result.

## 1. Symbols and the nonlinear bulk counterterm

Retain phi, K, ell, a_(k,chi), and the exact blocks A_(L,chi) of
P123.106. Let X be the finite set consisting of the trivial character
and all characters with any nonzero coefficient. Set h=|X| and

    A=max_(chi in X) sum_(k=-K)^K |a_(k,chi)|,
    f_chi(w)=sum_(k=-K)^K a_(k,chi) w^k,
    mu_(chi,r)=constant_coefficient(f_chi(w)^r).

If A=0 all determinants below equal one, so assume A>0. Both the
ordinary shift and the central-ball shift in P123.106 are contractions,
being compressions of a unitary normal dilation. Thus
||A_(L,chi)||<=A and |mu_(chi,r)|<=A^r.

For |z|A<1 define the holomorphic function, with log(1)=0,

    b_phi(z)=sum_(chi in X) integral_0^(2pi)
                   log(1+z f_chi(exp(i theta))) dtheta/(2pi)
       =sum_(r>=1) (-1)^(r+1) z^r [sum_chi mu_(chi,r)]/r.   (1)

The equality follows from uniform absolute convergence on smaller
disks. This bulk counterterm depends on the entire valuation symbol,
not just its constant coefficient or first trace.

## 2. Every power has a stabilized boundary correction

The dimension of block chi is n_chi=L+1-c(chi), including c(1)=0.
For nontrivial chi, its matrix is the constant-coefficient band matrix
with symbol f_chi. For the trivial block the entries are the same away
from the last K+1 positions, and its right-end pattern is independent
of L after indexing from that endpoint. This follows directly from the
powers of S_L in P123.106. Every matrix has bandwidth at most K.

Fix r>=1 and put w_r=(r+1)K+1. Expanding a diagonal entry of the r-th
power as a sum of length-r matrix paths shows that it equals
mu_(chi,r) whenever its index is at distance at least w_r from both
ends. Such a path cannot reach either a truncated end or the modified
central-ball entries. For n_chi>2w_r, the remaining left and right
boundary contributions depend only on those fixed endpoint patterns,
and not on the interval length. Therefore

    d_(L,chi,r)=Tr(A_(L,chi)^r)-n_chi mu_(chi,r)              (2)

is independent of L as soon as n_chi>2w_r.

There is also the bound, uniform in L>=ell,

    |d_(L,chi,r)|<=4w_r A^r.                               (3)

For n_chi>2w_r only at most 2w_r diagonal entries differ from the bulk;
each difference is at most 2A^r by the operator norm bound. If the
interval is shorter, the same estimate holds since n_chi<=2w_r. This
also treats powers long enough to see both endpoints.

For the full normal compression A_L=E A(phi) E define

    C_(L,r)=Tr(A_L^r)-(L+1)sum_chi mu_(chi,r).

Using (2), this is sum_chi[d_(L,chi,r)-c(chi)mu_(chi,r)]. Thus

    |C_(L,r)|<=h(4w_r+ell)A^r,                             (4)

and for each r it has an eventual exact value C_r. A sufficient
stabilization condition is L+1-ell>2w_r. The conductor term is retained
in this formula; replacing every block size by L+1 would lose it.

## 3. Holomorphic convergence with an explicit tail bound

Define the finite-cutoff renormalized determinant

    Delta_(L,phi)(z)
        =det(1+z A_L) exp(-(L+1)b_phi(z)).                  (5)

In the disk |z|A<1 its logarithm with value zero at zero is

    log Delta_(L,phi)(z)
       =sum_(r>=1) (-1)^(r+1) z^r C_(L,r)/r.               (6)

For any R with RA<1, (4) bounds these series uniformly on |z|<=R
by a summable series, since w_r grows linearly in r. Eventual exact
stabilization for every r then proves locally uniform convergence to

    Delta_phi(z)=exp(sum_(r>=1) (-1)^(r+1) z^r C_r/r).       (7)

This is a holomorphic, nonvanishing germ with Delta_phi(0)=1.
If m is any integer such that L+1-ell>2w_r for every r<=m, then

    sup_(|z|<=R) |log Delta_(L,phi)(z)-log Delta_phi(z)|
       <=2h sum_(r>m) (4w_r+ell)(RA)^r/r.                  (8)

This bound tends to zero as L increases. Thus convergence controls all
higher traces and has a quantitative remainder; it is not inferred
from the convergence of the first derivative alone.

## 4. Recovery of the whole local trace and the unit result

For r=1 the exact block trace from P123.106 gives

    C_1=-sum_chi c(chi)a_(0,chi)
                        +sum_(k!=0) q^(-|k|/2) a_(k,1).

Hence (log Delta_phi)'(0)=C_1. Multiplication by log q recovers the
full unit plus off-unit local packet with the normalization of
P123.042. Both signs of valuation and the central-ball term are included.

If K=0, then b_phi(z)=sum_chi log(1+z a_(0,chi)) and (5)–(7)
reduce exactly to the stabilized product of P123.105. Refining a unit
level for a fixed test adds only zero symbols, so (1), (5) and (7)
are unchanged. The matrices depend only on L=M+N, so changing M,N
with the same sum changes neither the construction nor its limit.

Convolution star takes the finite matrices to their adjoints and
conjugates the constant terms in (1). Consequently the limiting germ
satisfies Delta_(phi^*)(z)=conjugate(Delta_phi(conjugate z)).

## 5. Exact scope for A

This proves existence and cutoff convergence of the complete local
normal relative determinant germ for every compact multiplicative
Bruhat test, with a specified nonlinear counterterm and the prescribed
first logarithmic trace. The finite valuation/unit supports are fixed
in the estimates; uniform passage to larger test completions is not
claimed without additional bounds.

The result does not prove multiplicativity of the relative germ under
general convolution-unitization products: mixed-sign cutoff defects
can contribute a determinant anomaly. Nor does it identify this scalar
germ with the mixed diagonal determinant line or its arithmetic metric.
Tangential coupling, that anomaly/comparison, higher diagonal homology
and multi-stratum RR remain requirements for full A.
