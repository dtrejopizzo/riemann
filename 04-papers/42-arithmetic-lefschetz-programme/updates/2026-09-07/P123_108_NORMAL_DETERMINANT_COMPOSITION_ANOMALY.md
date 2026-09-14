# P123.108 — The normal determinant composition law and its nonzero anomaly

Date: 2026-09-07. Status: PROVED-IN-REPOSITORY for compact multiplicative
Bruhat tests near zero, with fixed finite valuation and unit supports.
The correction is an explicit boundary determinant limit. It is not
identified with the geometric biextension or arithmetic RR correction.

## 1. Finite-cutoff composition retains an endpoint defect

Use the probability-unit/counting-valuation convolution of P123.106.
For tests f,g put h=f+g+f*g, so 1+A(h)=(1+A(f))(1+A(g)) before
compression. Write

    F_L=E A(f) E,   G_L=E A(g) E,
    D_L=E A(f*g)E-F_L G_L=E A(f)(1-E)A(g)E.

Thus 1+E A(h)E=(1+F_L)(1+G_L)+D_L. Take f,g small enough that
their block norm bounds from P123.107 are each less than 1/4. All
inverses below and the relative germs evaluated at z=1 are then defined;
the bound for h is less than 1/4+1/4+1/16<1. The finite determinant
identity is

    det(1+E A(h)E)
       =det(1+F_L)det(1+G_L)
          det(1+(1+G_L)^-1(1+F_L)^-1 D_L).                 (1)

For each unit character the Laurent symbols satisfy
1+h_chi(w)=(1+f_chi(w))(1+g_chi(w)). On these small disks the logarithms
with value zero at f=g=0 add, so the bulk counterterm of P123.107 obeys
b_h(1)=b_f(1)+b_g(1). It cancels exactly from the ratio in (1).

## 2. A fixed-size boundary formula for the anomaly

Fix the finite character set and let K_f,K_g bound the valuation
supports. Set w=K_f+K_g+2. The block matrices in P123.106 show that,
once every block length exceeds 4w, D_L has both row and column support
in the first and last w coordinates of each active block. To check
this, away from those coordinates multiplication is the full Laurent
convolution and the missing outside paths do not occur. The trivial
character's modified entries also lie within that width. Its endpoint
patterns, as well as those of the other blocks, are independent of L.

Let W_L insert these endpoint coordinates, in a fixed order, into the
cutoff range. There is therefore a finite matrix d, independent of
large L, with

    D_L=W_L d W_L*.

The matrix d has separate left and right endpoint blocks. The finite
determinant in (1), by the elementary rectangular determinant identity,
equals

    det(1+B_L d),
    B_L=W_L*(1+G_L)^-1(1+F_L)^-1 W_L.                     (2)

The matrices B_L converge entrywise to a finite matrix B_infinity.
Indeed expand both inverses as Neumann series. Each term
W_L*G_L^r F_L^s W_L is bounded by ||G_L||^r ||F_L||^s, uniformly
in L. At each fixed r,s its entries stabilize: paths of bounded total
length see only a fixed endpoint neighborhood, and cannot connect the
two endpoints once the block is long enough. The double geometric
bound justifies taking the limit term by term. It also proves local
uniform convergence as f,g vary in a smaller such norm neighborhood
within fixed supports. This constructs B_infinity by a convergent
endpoint path series, rather than an unspecified limiting operator.

It follows that the exact relative composition law is

    Delta_h(1)=Delta_f(1)Delta_g(1) A(f,g),
    A(f,g)=det(1+B_infinity d).                             (3)

Here Delta is the germ constructed in P123.107, evaluated in the
stated neighborhood. This is a finite-dimensional determinant of
analytic endpoint series. It is independent of enlarging a unit level
for the fixed tests, since the added zero-symbol blocks contribute one.

## 3. The anomaly is genuinely nontrivial

Choose any nontrivial unit character chi of conductor c. Such characters
exist also for q=2 by choosing a sufficiently fine unit level. Let f_+
be the test supported on qU with value chi(u), and f_- the analogous
test on q^-1 U. Unit Fourier orthogonality means only the chi block
is active. On its n=L-c+1 dimensional range,

    E A(s f_+)E=s T_n,    E A(t f_-)E=t T_n*,
    E A(s f_+*t f_-)E=st I.

Both single-shift relative determinants equal one: their finite
determinants are one by nilpotence, and their bulk logarithmic constant
terms vanish. For h=s f_++t f_-+st(f_+*f_-), the matrix 1+E A(h)E
has diagonal 1+st and adjacent off-diagonals s,t. Its determinant d_n
satisfies

    d_0=1, d_1=1+st,
    d_n=(1+st)d_(n-1)-st d_(n-2),
    d_n=sum_(j=0)^n (st)^j.

The recurrence follows by expansion along the last row. Its symbol
factors as (1+sw)(1+t w^-1), so its bulk counterterm is again zero
near s=t=0. Consequently

    A(s f_+,t f_-)=1/(1-st)                                (4)

for |st|<1 in the germ neighborhood. Thus ignoring D_L would give
an incorrect multiplicativity assertion. The example uses actual
compact locally constant tests, not delta distributions.

## 4. Associativity and the precise next comparison

Write f diamond g=f+g+f*g. Associativity follows from multiplication
of 1+A(f), and all Delta germs are nonzero near zero. Applying (3)
twice proves the cocycle identity wherever all terms are in the common
germ neighborhood:

    A(f,g) A(f diamond g,k)
       =A(g,k) A(f,g diamond k).                            (5)

The identity is also an identity of germs. Hence the correction has
the coherence demanded by associative composition. This is not a
proof that it equals the correction in a source-defined determinant
line or biextension: that identification still needs construction.

The result supplies the general local normal composition law, including
a computable, nonzero endpoint anomaly and its associativity. Coupling
it to the tangential action, comparing it with the mixed diagonal and
its arithmetic metric, and gluing all strata remain necessary for A.
