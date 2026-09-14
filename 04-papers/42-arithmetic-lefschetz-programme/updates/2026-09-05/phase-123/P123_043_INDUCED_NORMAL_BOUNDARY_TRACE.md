# P123.043 — Induced normal boundary action and its relative character

Date: 2026-09-05. Status: PROVED for the single-zero finite-place
normal model. This couples P123.041 and P123.042 in one representation
of the external convolution algebra. Global localization is still open.

## 1. The coefficient bundle and full external action

Write G=H_S, K=K_(S,p), Y=G/K, a=log p, with the Haar measures of
P123.041: vol(Y)=a and dk=counting times probability unit Haar.
Identify K with Q_p^*. Let V=L²(Q_p) carry D_x from P123.042.
The induced Hilbert space consists of measurable equivariant functions

    F(gk)=D_k^-1 F(g),
    ||F||²=integral_Y ||F(s(y))||² dy < infinity.

Here s is a measurable section; unitarity of D makes the norm independent
of its choice. This is the L² space of the associated normal coefficient
bundle. Left translation defines

    (rho(h)F)(g)=F(h^-1 g).

It preserves equivariance and norm, and is a strongly continuous unitary
representation. For completeness, continuity follows first on sections
continuous with compact support inside a trivializing real interval,
with locally constant compact unit dependence and fiber vectors in a
dense continuous-vector subspace of D. Translation is continuous there;
these sections are dense and all translations have norm one.

For an external Bruhat test f put R(f)=integral_G f(h)rho(h) dh.
Fubini gives R(f*g)=R(f)R(g), R(f*)=R(f)* and ||R(f)||<=||f||_1.
Thus no convolution-preserving restriction G -> K is needed.

## 2. Kernel in an explicit fundamental section

Use coordinates G=R times U_p times V_S, where
V_S=product_(ell!=p) Z_ell^*. Representatives

    s(t,v)=(t;1,v),    0<=t<a, v in V_S

give a fundamental section up to a null seam. Its measure is dt dv.
For y,z in this section, the kernel of R(f) is the bounded fiber operator

    A_f(y,z)=integral_K f(s(y) k s(z)^-1) D_k dk.       (2.1)

Indeed set h=s(y)k s(z)^-1 in the group integral. Equivariance gives
F(h^-1 s(y))=F(s(z)k^-1)=D_k F(s(z)). The quotient integral formula
then proves (2.1), initially on dense bounded sections and then by
boundedness. Only finitely many valuations of k contribute, uniformly
for t_y,t_z in [0,a], because f has compact real support.

## 3. Normal compression produces a trace-class operator

In this section let E act fiberwise as E_MN of P123.042, with L=M+N>=0.
This is an orthogonal projection on the induced space, generally of
infinite total rank: the base remains continuous. Nevertheless

    B_MN(f)=E R(f) E

is trace class. Here is a direct proof rather than a formal diagonal
prescription. Its kernel is E_MN A_f(y,z) E_MN, with values in matrices
on the p^L-dimensional normal range. Dependence on v_y,v_z factors
through a finite quotient of V_S, because f has a uniform unit level
and D_k is independent of these variables. The operator kills the
orthogonal complement of functions constant on those finite cosets.

Each remaining matrix kernel in t_y,t_z is smooth on a neighborhood
of the closed square [0,a]²: the finite valuation sum in (2.1) remains
finite on a slightly larger square, and all derivatives act on f.
Extend it smoothly with compact support to a larger square and then
periodically to a larger torus. Its double Fourier coefficients decay
faster than any power in both indices. The associated rank-one operator
series is absolutely summable in trace norm. Restricting both variables
back to [0,a] is bounded compression, so trace class follows on the
original interval as well. This proof requires no periodic matching
across the section seam.

The same absolutely convergent series proves the diagonal trace formula.
Since G is abelian, s(y)k s(y)^-1=k, and thus

    Tr B_MN(f)=a integral_K f(k) Tr(E_MN D_k E_MN) dk
      =a sum_(j in Z) integral_(U_p)
         f(j_p(p^j u)) |p^j|_p^(1/2)
                     min(p^L, |1-p^j u|_p^-1) du.     (3.1)

We used Tr(E_MN D_k E_MN)=Tr(E_MN D_k), justified by finite rank.
The factor a arises once, from the tangential quotient volume.

## 4. The relative character is exactly the local Fourier packet

Let ell>=1 be a unit level for x -> f(j_p(x)) near x=1. P123.042
applied to (3.1) gives, for every L>=ell,

    Tr B_MN(f) - (L+1)(log p)f(1) = W_p(f),           (4.1)

where W_p is the Fourier-normalized local distribution of P123.034.
Explicitly the right side is

    (log p) sum_(j!=0) p^(-|j|/2)
                   integral_(U_p) f(j_p(p^j u)) du
      + (log p) integral_(U_p)
                   (f(j_p(u))-f(1))/|1-u|_p du.

This is eventual equality for each test, not merely an asymptotic
estimate. It realizes the packet as the relative trace of compressions
of one convolution-preserving external representation. The compressed
assignment B_MN itself need not preserve convolution. The identity
subtraction in (4.1) is a scalar functional, not an assertion that an
uncut operator difference has been proved trace class.

The construction is not invalidated by using a fundamental section.
A change s'(y)=s(y)c(y), c(y) in K, changes fiber coordinates by the
unitary D_c(y)^-1. Transporting E with this coordinate change produces
the same geometric compression and trace. Even if a fresh constant
cutoff is chosen in the new frame, its diagonal normal trace is the
same, since all D_c commute with D_k. The trace-class argument above
is asserted for the stated regular fundamental section and its unitary
transports; no regularity assertion for an arbitrary new measurable
cutoff is needed.

## 5. Exact semilocal compatibility

For S contained in T and p in S, pi_TS:G_T -> G_S maps K_T
isomorphically to K_S and preserves its normal representation D.
Pullback of equivariant functions defines an isometry J_ST of induced
spaces, using probability Haar on the new compact unit fibers. In the
fundamental sections above it simply forgets the new unit coordinates,
so E_T J_ST=J_ST E_S.

Integrating the new units first shows

    R_T(P_ST f)=J_ST R_S(f) J_ST*,
    B_T,MN(P_ST f)=J_ST B_S,MN(f) J_ST*.

Indeed new-unit averaging is the orthogonal projection onto the image
of J_ST; on that image the remaining action is exactly rho_S. Hence
both the finite-cutoff traces and their counterterms agree. Pullbacks,
isometries, compressions and relative characters compose on chart
triples without additional constants.

## 6. The remaining localization obligation

The normal bundle model now has an actual external representation and
the required finite-place relative character. The missing step is no
longer to multiply a tangential volume by a formal normal Jacobian.

It remains to obtain this model through an excision/localization map
from the repaired common source, and to control intersections of boundary
strata and the archimedean contribution. A direct sum of the present
models does not by itself prove such localization: it could omit or
double-count higher-zero contributions. Comparison with the integral
primitive contact and its determinant must also use that same source.
The result supplies no global positivity statement for row D.
