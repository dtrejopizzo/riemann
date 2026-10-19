# P123.118 — A continuous contraction of the completed higher smooth diagonal

Status: PROVED-IN-REPOSITORY by the explicit chain
construction below, for the normalized completed Hochschild complex of
S(Y) in P123.101–102. This is a result about that boundary algebra, not
a full mixed arithmetic diagonal or a bimodule-perfectness assertion.

## 1. The statement

Let S=S(Y) and C_n=S tensorhat_pi (S/C1)^(tensorhat_pi n), with its
normalized Hochschild boundary b. There are continuous S-linear maps

    pi:C_* -> S[0] direct_sum S dt[1],
    s:S[0] direct_sum S dt[1] -> C_*,
    H_n:C_n -> C_(n+1)

such that pi s=1 and

    b H+H b=1-s pi.                                      (1)

Here pi_0=s_0=identity, pi_1(m tensor [f])=m Df dt,
s_1(h dt)=h/(i tau_0) chi_0^-1 tensor [chi_0], and all other
components of pi and s vanish. The target has zero differential.
Consequently

    H_0(C)=S,  H_1(C)=S dt,  H_n(C)=0 for n>=2,            (2)

as topological homology. Every boundary image is closed and has a
continuous linear right inverse on that image. The proof below supplies
polynomial estimates for each degree; finite-level exactness alone is
not used to infer (1) after completion.

## 2. Fourier chains are group chains with a free S coefficient

Write the character group L additively in this proof, and denote its
character functions by the same symbols when no confusion results.
For a normalized Fourier tensor, separate its total character:

    eta_0 tensor [eta_1] tensor ... tensor [eta_n]
       <-> (eta_0 eta_1 ... eta_n) tensor [eta_1|...|eta_n]. (3)

The right-hand bracket is the normalized inhomogeneous group bar of
L with trivial complex coefficients. Its boundary drops the first or
last argument and alternately combines adjacent arguments. Expanding
the Hochschild boundary proves (3) intertwines the boundaries; the
first factor on the right is unchanged. Degenerate entries equal to
the identity are zero.

Both (3) and its inverse extend continuously to the weighted Fourier
completions: W(product eta_i)<=product W(eta_i), and W(eta^-1)=W(eta).
For example the inverse bound on output factor weights with exponent m
is W(total)^m product_(i>=1) W(eta_i)^(2m). Thus it suffices to construct
polynomially bounded contractions on group bar basis elements. Extend
those contractions S-linearly in the total-character coordinate.

## 3. Finite-level transfer to one infinite cyclic subgroup

Let L_N contain the characters whose unit part is trivial on N_N.
It contains Z chi_0, where chi_0 has frequency tau_0=2pi/log q, and

    L_N/(Z chi_0) = (U/N_N)^hat =: K_N.

The finite group has order m_N<=c_N, with c_N=p^N (and c_0=1).
For each k in K_N choose its representative s(k) with frequency in
[0,tau_0), with s(0)=0. These representatives have W(s(k))<=C c_N.
For g in L_N put r(g)=g-s(g mod Z chi_0), an element of Z chi_0.
Then r(g+h)=r(g)+h for h in Z chi_0.

Use normalized homogeneous bar simplices [g_0,...,g_n], modulo
simultaneous translation, with boundary the alternating vertex deletion.
The conversion from inhomogeneous arguments takes cumulative sums
0,g_1,g_1+g_2,...,g_1+...+g_n. Define

    t_N[g_0,...,g_n]
       =(1/m_N) sum_(k in K_N)
          [r(g_0+s(k)),...,r(g_n+s(k))]                   (4)

in the homogeneous bar coinvariants of Z chi_0. It is a chain map.
It is independent of the simultaneous-translation representative:
adding a in L_N permutes k to k+a_bar, and
s(k)+a-s(k+a_bar) lies in Z chi_0. This translates all vertices of
the corresponding output simplex by the same subgroup element.
The subgroup inclusion i_N satisfies t_N i_N=identity.

There is an explicit homotopy from i_N t_N to identity. For each k
put x_j=g_j+s(k), y_j=r(g_j+s(k)). The usual prism

    P_k[g_0,...,g_n]
       =sum_(j=0)^n (-1)^j [x_0,...,x_j,y_j,...,y_n]

satisfies b P_k+P_k b=[y_0,...,y_n]-[x_0,...,x_n].
This identity follows by deleting vertices: the interior deletions
cancel in pairs and the two end terms remain. Set

    V_N=-(1/m_N) sum_k P_k.

It follows that b V_N+V_N b=1-i_N t_N. The same permutation and
subgroup-translation argument proves V_N well-defined on coinvariants.
Consecutive repeated vertices make every prism summand degenerate,
so it also descends to the normalized complex.

## 4. An explicit cyclic bar contraction with linear size bounds

Identify Z chi_0 with the integers. Let T be the cellular chain
complex of the oriented integer line: vertices v_j and edges e_j
from j to j+1. Map its vertices and edges into the homogeneous bar
by i(v_j)=[j], i(e_j)=[j,j+1]. Define a chain map p from that bar
to T: p_0[j]=v_j, p_1[a,b] is the oriented unit-edge path from a to b,
and p_n=0 for n>=2. It is a chain map because paths add:
path(a,c)=path(a,b)+path(b,c). Also p i=1.

Construct a translation-equivariant homotopy J before coinvariants.
Set J_0=0. For a simplex sigma=[j_0,...,j_n], n>=1, put

    z_sigma=sigma-i p(sigma)-J_(n-1) b(sigma),
    J_n(sigma)=cone_(j_0)(z_sigma),                       (5)

where cone_a prepends a to every simplex and passes to normalization.
Induction gives b z_sigma=0. For n=1 this uses b(sigma-i p sigma)=0;
for n>=2 it follows from the already established identity in degree
n-1 and b^2=0. The cone identity b cone_a+cone_a b=identity in
positive degrees therefore yields b J_n(sigma)=z_sigma. Hence

    b J+J b=1-i p.                                       (6)

All vertices used in (5) stay in the interval between the smallest and
largest original vertices. If its diameter is D, the sum of absolute
coefficients of J_1(sigma) is at most 1+D. For n>=2 it is at most
1+(n+1) times the corresponding bound in degree n-1. Thus it is
bounded by C_n(1+D), with C_n depending only on n. Equivariance follows
because unit paths and cones commute with integer translation.

After taking Z coinvariants, T is C in degrees zero and one, with
zero differential. Compose (4)–(6) to obtain a finite-level homotopy

    h^(N)=V_N+i_N J t_N,
    b h^(N)+h^(N)b=1-s p^(N).                            (7)

The inclusion s in degree one is the class [chi_0], independent of N.
The degree-one projection p^(N)[g] equals tau(g)/tau_0. Indeed average
r(g+s(k))-r(s(k)) over k. In frequencies the representatives s(k)
and s(k+g_bar) cancel by permutation, leaving tau(g). Thus (7)
uses the same degree-one projection at every level.

## 5. Polynomial estimates independent of the chosen finite level

For an inhomogeneous n-simplex sigma=[g_1|...|g_n], take the least
level N containing its arguments and put R=product_i W(g_i)>=1.
Its maximum conductor c_N is at most R. Its cumulative frequencies
have absolute value bounded by sum_i |tau(g_i)|. In the prism, the
added representatives have frequencies bounded by tau_0 and conductor
at most c_N. All differences of its vertices consequently have weight
at most C_n R. Averaging over m_N terms introduces no growth of the
sum of absolute coefficients, since every term has coefficient 1/m_N.

In t_N the resulting integer vertices have diameter at most
C_n(1+sum_i |tau(g_i)|)<=C_n R. The line contraction in section 4
uses at most C_n R in total absolute coefficients, and all its vertex
differences have weight at most C_n R. Consequently for each degree n
and weight exponent m, the group-bar output seminorm satisfies

    ||h^(N)_n(sigma)||_m <= C_(n,m) R^((n+1)m+1).          (8)

More generally if sigma is already at a larger level N, the same
bound holds with R replaced by a constant times
c_N(1+sum_i |tau(g_i)|). This version permits applying the contraction
to finite sums whose terms arose from earlier contractions. Importantly,
the bound is polynomial in the level conductor, not exponential in it.

## 6. Assemble levels without assuming compatible level homotopies

The choices of coset representatives in (4) need not give compatible
h^(N) under refinements. Using h^(N) on each input independently would
therefore not by itself prove a global chain homotopy. Instead assemble
it recursively on the normalized inhomogeneous Fourier basis.

Start with H_0=0 and the degree-one map H_1 of P123.102, expressed in
the coordinates (3). It has b H_1=1-s p_1, with p_1[g]=tau(g)/tau_0,
polynomial bounds, and its output remains in the level of its input.
For n>=2 and basis sigma at its least level N define

    z_sigma=sigma-H_(n-1)b(sigma),
    H_n(sigma)=h^(N)_n(z_sigma).                          (9)

The induction identity and p_1 b_2=0 imply b z_sigma=0. Each summand
remains in L_N, since multiplication, powers, the fixed chi_0, and
all previous constructions preserve that level. In degree n>=2 the
projection in (7) is zero. Therefore

    b H_n(sigma)=z_sigma,
    b H_n+H_(n-1)b=identity,                              (10)

without any compatibility assumption on the different h^(N).

For clarity, continuity of this recursive construction follows from a
stronger finite-support induction. For each fixed n there is an exponent
A_n and constant C_n such that H_n(sigma) has total absolute coefficient
sum <=C_n R^A_n and every output argument has weight <=C_n R^A_n,
where R=product_i W(g_i). P123.102 supplies this assertion for n=1.
The boundary has n+1 terms of product weight at most R, so the induction
hypothesis supplies polynomial bounds for z_sigma. Its level conductor
is at most R. Apply the larger-level version of (8) termwise: integer
paths, vertex differences and coefficient sums again have bounds by a
fixed power of R. This proves the assertion for n. In particular, for
every n,m there is a finite B(n,m) such that

    ||H_n(sigma)||_m <= C_(n,m) product_i W(g_i)^B(n,m).    (11)

Thus H_n extends continuously to the weighted ell1 projective limit
in each degree. Multiplication by the total coefficient in (3) is
continuous, so the S-linear extension gives the asserted maps on C_n.
The identities on dense finite Fourier tensors extend by continuity.

## 7. Topological homology and exact scope

Equations (1) and (10) now hold on the completed complex. For n>=2,
ker b_n=im b_(n+1), and H_n restricted to ker b_n is a continuous
right inverse to b_(n+1). These images are closed because b_n is
continuous. In degree one, im b_2=ker pi_1 as in P123.102, again with
a continuous right inverse. This proves (2) and the chain-homotopy
comparison with the bounded finite free S-module complex S[0]+S dt[1].

The comparison maps pi and s preserve finite unit levels and use the
same physical differential dt on every level. The chosen H is not
asserted natural for every map; its existence establishes the completed
comparison. In particular this does not construct a finite projective
resolution of S as an S tensorhat S bimodule. That stronger diagonal
perfectness, the full smooth orbit Morita transport, gluing across all
arithmetic strata and identification of the resulting determinant and
metric with mixed RR remain separate requirements. No full A/B/C/D row
or global sign is concluded.
