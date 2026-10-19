# P123.109 — The coupled induced relative determinant and its chart compatibility

Status: PROVED-IN-REPOSITORY for scalar external
Bruhat tests in the induced single-zero normal representation of
P123.043, at each finite semilocal set containing q. The determinant
is a holomorphic germ. Its geometric RR identification remains open.

## 1. Operator-valued normal blocks of the actual induced action

Fix S and the normal place q. In the regular fundamental section of
P123.043 write y=(t,v), 0<=t<a=log q, with v in the product of the
other compact unit factors. Let H_tan be L2 of this section with its
quotient measure. For an external Bruhat test F, its induced kernel is

    A_F(y,z)=sum_k integral_(U_q)
                 F(s(y) j_q(q^k u) s(z)^-1) D_(q^k u) du.  (1)

Only finitely many k occur, uniformly in y,z; let |k|<=K contain them.
Choose ell so that F has unit level U_(q,ell) in the normal unit variable.
For every unit character chi of conductor at most ell define T_(k,chi)
on H_tan by the scalar kernel

    integral_(U_q) F(s(y) j_q(q^k u) s(z)^-1)chi(u)^-1 du.  (2)

These operators are trace class. Their unit-coordinate dependence
factors through a finite quotient, and on its finitely many matrix
entries the kernel is smooth on a neighborhood of the closed real
square. A smooth extension to a larger torus gives an absolutely
trace-norm-summable double Fourier rank-one expansion, exactly as in
P123.043. The resulting bounds use finitely many derivatives of F on
its fixed support and fixed unit level.

Fourier decomposition in the normal unit action turns E R(F) E into
the blocks of P123.106 with every scalar a_(k,chi) replaced by T_(k,chi).
For chi!=1 this is

    B_(L,chi)=I tensor T_(0,chi)
       +sum_(k=1)^K [T_n^k tensor T_(k,chi)
                          +(T_n*)^k tensor T_(-k,chi)],
    n=L+1-c(chi).                                         (3)

For chi=1 replace T_n by the central-ball shift S_L of that note.
This follows from the actual kernel (1), not from a tensor-product
assumption on F. In particular the operators T_(k,chi) are not assumed
to commute. The cutoff blocks are trace class on the finite sum of
copies of H_tan.

## 2. Trace-ideal estimates for every power

Let X contain the finitely many active unit characters, including the
trivial one, and set

    A=max_chi sum_k ||T_(k,chi)||,
    B=max_chi sum_k ||T_(k,chi)||_1.

If A=0 there is nothing to prove. Otherwise A<=B<infinity. Define the
trace-class operator Laurent polynomial and its bulk power trace by

    P_chi(w)=sum_k w^k T_(k,chi),
    mu_(chi,r)=Tr_Htan(constant_coefficient(P_chi(w)^r)).    (4)

The order of the products in this coefficient is retained. Summing
products with one trace norm and the remaining operator norms gives
|mu_(chi,r)|<=B A^(r-1).

The same bound holds for the absolute trace of each diagonal operator
entry of B_(L,chi)^r. Indeed, if J_i inserts H_tan into its i-th normal
coordinate, then ||B_(L,chi)J_i||_1<=B: each normal shift column has
norm at most one. Since ||B_(L,chi)||<=A, the trace norm of
J_i* B_(L,chi)^r J_i is at most B A^(r-1).

The finite-band path argument of P123.107 now applies with operator
coefficients. Put w_r=(r+1)K+1. Interior diagonal entries equal the
operator constant coefficient in (4), and the endpoint patterns stabilize
once n>2w_r. For the full compression B_L(F)=E R(F)E it follows that

    C_(L,r)=Tr(B_L(F)^r)-(L+1)sum_chi mu_(chi,r)

has an eventual exact value C_r(F), and uniformly for L>=ell,

    |C_(L,r)|<=|X|(4w_r+ell) B A^(r-1).                    (5)

Only the at most 2w_r endpoint entries can differ from bulk in a long
block; the short-block case has at most that many entries altogether.
The conductor dimension correction is again -c(chi)mu_(chi,r).
No scalar commutativity is used in this stabilization or bound.

## 3. A convergent determinant of the coupled representation

For |z|A<1 define

    b_F(z)=sum_chi integral_0^(2pi)
                  log det_Htan(1+z P_chi(exp(i theta))) dtheta/(2pi)
          =sum_(r>=1) (-1)^(r+1)z^r [sum_chi mu_(chi,r)]/r. (6)

The logarithm is its germ at zero. The trace-ideal bounds justify the
Fredholm determinant and the absolutely convergent power expansion.
Equations (5)–(6) prove locally uniform convergence

    det(1+z B_L(F)) exp(-(L+1)b_F(z))
         -> Delta_(S,q,F)(z)
          =exp(sum_(r>=1) (-1)^(r+1)z^r C_r(F)/r).          (7)

This is a nonvanishing holomorphic germ with value one at zero.
If L+1-ell>2w_r for all r<=m, its logarithmic error on |z|<=R<1/A
is bounded by

    2|X| B sum_(r>m) (4w_r+ell) R^r A^(r-1)/r.            (8)

Thus convergence controls the actual induced normal/tangential operator,
with a quantitative tail estimate on each fixed test domain.

## 4. The first derivative is exactly the existing local character

Taking diagonal traces of (2) and summing chi at k=0 gives

    b_F'(0)=sum_chi Tr(T_(0,chi))=a F(1).

Here the finite Fourier sum evaluates the normal unit variable at one,
and s(y) s(y)^-1=1; integration over the section supplies its volume a.
The exact relative trace in P123.043 therefore gives

    (log Delta_(S,q,F))'(0)
       =Tr B_L(F)-(L+1)(log q)F(1)=W_q(F)                 (9)

for sufficiently large L. Unlike the separate scalar normal germ, this
identity already includes the tangential quotient normalization through
the coupled representation. It does not insert log q as a chosen power
of a scalar determinant.

## 5. Exact semilocal compatibility on the prescribed pullback tests

For S contained in T and F_T=F compose pi_TS, P123.043 proves an
isometry J_ST with B_(T,L)(F_T)=J_ST B_(S,L)(F) J_ST*. Thus every
positive power has exactly the same trace, and every finite-cutoff
Fredholm determinant agrees. Dividing the power traces by L+1 and
using (5) identifies their bulk coefficients:

    sum_chi mu_(T,chi,r)=sum_chi mu_(S,chi,r).

Their stabilized constants C_r agree as well. Equations (6)–(7) give

    b_(T,F_T)=b_(S,F),
    Delta_(T,q,F_T)=Delta_(S,q,F).                           (10)

These identities compose on chart triples, since the original isometries
and scalar pullbacks do. They concern exactly the normalized scalar
pullbacks of P123.023/P123.043, not unproved full coefficient functors.
Unitary changes of section with the cutoff transported preserve the
same power traces, bulk coefficients and germ by the same argument.

## 6. Remaining scope

This proves the coupled local induced determinant germ, its prescribed
logarithmic derivative and its semilocal compatibility for the existing
scalar test transitions. It is no longer merely a tensor product of two
separately assigned scalar determinants.

It does not identify the coupled composition anomaly with the geometric
biextension, show that every required mixed diagonal is represented by
these operators, or provide the intrinsic arithmetic metric and RR
equality. Higher diagonal homology and multi-stratum gluing also remain
open. Therefore the complete row A is not closed by (7)–(10).
