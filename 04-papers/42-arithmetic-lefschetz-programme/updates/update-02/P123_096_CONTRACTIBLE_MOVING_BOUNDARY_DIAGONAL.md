# P123.096 — Continuous contraction of the moving boundary diagonal

Status: PROVED-IN-REPOSITORY for the completed
twisted Hochschild bar over the compact boundary corner. The comparison
with the full-source diagonal is not inferred from degree-zero Morita
identities alone.

## 1. External action on the corner

Let Y=B_q and B=C(Y). For an external parameter a let
alpha_a(h)(y)=h(a_T^-1 y). This is the action induced on the cutoff
corner: first beta_a carries e_c to e_(c_a), and the partial isometry
V_(c,c_a) of P123.090 carries that corner back to e_c. In the rank-one
orbit frames, the resulting scalar function is exactly alpha_a(h).
Thus this automorphism is compatible with the declared cutoff transport.

The compact boundary Y is a homogeneous space G/K_q of an abelian
group. A translation either fixes every point (a in K_q) or has no
fixed points (a not in K_q). Indeed fixation of gK_q implies
agK_q=gK_q, hence a in K_q by commutativity.

## 2. The entire completed bar

More generally, let Y be compact Hausdorff and alpha the automorphism
of C(Y) induced by a homeomorphism with no fixed points. Put
M=_1 B_alpha, with right action m.b=m alpha(b). Consider

    C_n=M tensorhat_pi B^(tensorhat_pi n), n>=0,

and the Hochschild boundary

    d(m tensor a_1 tensor ... tensor a_n)
      =m alpha(a_1) tensor a_2 tensor ... tensor a_n
       +sum_(j=1)^(n-1) (-1)^j m tensor ... tensor a_j a_(j+1)
                                                   tensor ...
       +(-1)^n a_n m tensor a_1 tensor ... tensor a_(n-1).

The boundary in degree zero is zero. These are Banach spaces and
continuous operators in each degree, with the sup/projective norms.

For b in B define the insertion operator

    h_b(m tensor a_1 tensor ... tensor a_n)
       =sum_(j=0)^n (-1)^j m tensor a_1 tensor ... tensor a_j
                              tensor b tensor a_(j+1) ... tensor a_n.

It has norm at most (n+1)||b||. Expanding d h_b+h_b d, adjacent
interior products cancel pairwise because B is commutative; the two
uncancelled end terms give

    d h_b+h_b d = L_(alpha(b)-b),                            (1)

where L multiplies the M coefficient. In degree zero this is just
d(m tensor b)=m alpha(b)-bm, fixing the sign convention.

## 3. Finite continuous Bezout identity and contraction

At each y there exists b in C(Y) with alpha(b)(y)!=b(y), since
continuous functions separate y from its distinct translated point.
Compactness supplies finitely many b_i such that

    D(y)=sum_i |alpha(b_i)(y)-b_i(y)|^2 >0  for all y.

Set c_i=conjugate(alpha(b_i)-b_i)/D, a continuous function. Then
sum_i c_i(alpha(b_i)-b_i)=1. Left coefficient multiplication L_(c_i)
commutes with d, since both endpoint actions and all coefficients
commute. Thus

    H=sum_i L_(c_i) h_(b_i)
    satisfies dH+Hd=1,                                     (2)

with the explicit degreewise bound
||H:C_n->C_(n+1)|| <= (n+1)sum_i ||c_i|| ||b_i||.
Equations (1)–(2) are proved on elementary tensors and extend by
continuity to the completions. No closure-only or weak exactness is used.

The completed complex is therefore continuously contractible. Its
boundary images are closed kernels, and H restricted to each kernel
is a continuous linear right inverse to the preceding boundary. In
particular it is exact even in the linearly split sense relevant to
P123.066, not merely in a weaker strict-exact interpretation.

## 4. Consequence for the boundary determinant domain

For a not in K_q, the entire corner diagonal C_*(B,B_(alpha_a)) is
homotopy equivalent to zero, which is a bounded perfect complex. Thus
this particular diagonal has the zero perfect representative and the
unit determinant line in the perfect homotopy/derived category.
The unbounded bar terms themselves have not been declared finite
projective. This conclusion uses the explicit contraction to zero.

At a in K_q, alpha_a=identity and the finite Bezout construction fails:
all alpha_a(b)-b vanish. There the degree-zero homology is B itself,
and (2) cannot hold. Higher diagonal homology and the normal determinant
on that fixed sector require a separate calculation. This identifies
the precise parameter sector where the remaining contribution can lie.

There is no inference here of uniform parameter bounds near K_q; the
denominator D may approach zero. Consequently this contraction alone
does not construct a distributional family across that locus, nor a
global regularized determinant. Full-source derived transport, strata
gluing and the arithmetic mixed RR remain necessary for row A.
