# 106.130 — Multiplicative cells and the cutoff-commutator gate

## Purpose and verdict

This note tests the proposed factorization of the cluster curvature by
multiplicative two-cells and a trace-zero commutator.  There are two exact
positive calculations:

1. the arithmetic coefficient
   \(j_2=\delta\Lambda+\Lambda*\Lambda=\mu*\log^2\) is the positive
   curvature of the multiplicative divisor cells; and
2. for a flat commuting translation connection, the square of its
   Laplacian is exactly the sum of the squared parallelogram second
   differences.

Neither calculation proves the physical cluster inequality.  The flat-cell
identity leaves the negative first-order term \(-L/2\), and the physical
theta sandwich is not a representation of the translation semigroup.  Its
nonzero holonomy is precisely the intermediate-position defect of 106.54.

There is also a cutoff obstruction to the proposed commutator removal.  The
full Riesz projection \(P=P_J(L)\) commutes with \(L\), but not with the
finite-cutoff operator \(L_{\varepsilon,N}\).  Hence

\[
 \operatorname {Tr}P[L_{\varepsilon,N},Y_{\varepsilon,N}]
 =\operatorname {Tr}([P,L_{\varepsilon,N}]Y_{\varepsilon,N}),
\tag{1}
\]

which need not vanish.  If instead one uses a spectral projection of the
cutoff operator, the cutoff operator itself has arbitrarily small tail
Rayleigh quotients and therefore has no \(1/2\) spectral floor.  Thus the
commutator cannot be discarded on either side of the cutoff without a new
uniform theorem.

This is an exact gate for this factorization, not a no-go for a genuinely
joint full-limit identity.

## 1. Exact arithmetic cell curvature

Let \(F(n)=(\log n)^2\).  Since \(\mu\) is supported on squarefree
integers,

\[
 j_2(n)=(\mu*F)(n).
\tag{2}
\]

The values are

\[
\boxed{
\begin{aligned}
 j_2(p^a)&=(2a-1)(\log p)^2,\\
 j_2(p^aq^b)&=2\log p\log q\qquad(p\ne q),\\
 j_2(n)&=0\qquad\text{if \(n\) has at least three distinct primes.}
\end{aligned}}
\tag{3}
\]

### Proposition 1 — Divisor-cell realization

For a prime tower, the first multiplicative difference of \(F\) is

\[
 F(p^a)-F(p^{a-1})=(2a-1)(\log p)^2.
\tag{4}
\]

For distinct primes, the square

\[
 \{p^{a-1}q^{b-1},p^aq^{b-1},p^{a-1}q^b,p^aq^b\}
\]

has mixed difference

\[
\begin{aligned}
 &F(p^aq^b)-F(p^{a-1}q^b)-F(p^aq^{b-1})
   +F(p^{a-1}q^{b-1})\\
 &\hspace{35mm}=2\log p\log q.
\end{aligned}
\tag{5}
\]

All third mixed differences vanish.  Equations (4)--(5) prove (3), hence
the cell weights are nonnegative.

This is a coefficient theorem.  It does not say that the corresponding
translation operator is positive after the scalar and the intermediate
theta position have been inserted.

## 2. What the flat Hodge calculation actually proves

Let \(U_a\) be commuting unitary translations on an abelian group, let
\(D_a=U_a-I\), and take a finite family of nonnegative weights \(w_a\).
Define

\[
 L_0=\sum_a w_aD_a^*D_a.
\tag{6}
\]

### Theorem 2 — Exact parallelogram identity

For every vector in the common domain,

\[
\boxed{
 \langle f,L_0^2f\rangle
 =\sum_{a,b}w_aw_b\|D_aD_bf\|^2.}
\tag{7}
\]

Consequently,

\[
\boxed{
 \langle f,(L_0^2-\tfrac12L_0)f\rangle
 =\sum_{a,b}w_aw_b\|D_aD_bf\|^2
  -\frac12\sum_aw_a\|D_af\|^2.}
\tag{8}
\]

#### Proof

The operators \(D_a,D_a^*,D_b,D_b^*\) commute.  Therefore

\[
 \langle f,D_a^*D_aD_b^*D_bf\rangle=\|D_aD_bf\|^2.
\]

Summing gives (7), and subtracting one half of (6) gives (8). \(\square\)

Formula (8) pinpoints the missing sign.  In Fourier coordinates,

\[
 \ell(\xi)=\sum_aw_a|e^{ia\xi}-1|^2,
\tag{9}
\]

and (8) has multiplier \(\ell(\xi)(\ell(\xi)-1/2)\).  Since
\(\ell(0)=0\) and \(\ell\) is continuous, every nontrivial flat model has
nonzero frequencies with \(0<\ell(\xi)<1/2\).  The positive two-cell
square is fourth order at low frequency, whereas the negative edge energy
is second order.  No flat Hodge identity can absorb the latter.

Grouping the terms in (7) by \(a+b=\log(mn)\) produces the product
coefficient \(\Lambda*\Lambda\).  Expanding the same norms also produces
the difference displacements \(a-b=\log(m/n)\).  These are the ratio
channels of 106.50; cell positivity does not remove them.

## 3. The theta sandwich has nonzero cell holonomy

In the physical \(L^2(dx)\) coordinate, an oriented off-diagonal move is

\[
 T_s=M_\eta U_sM_\eta,
 \qquad \eta^2=\frac{c_KK}{h}.
\tag{10}
\]

It is not a representation of the translation group.  Directly,

\[
 (T_sT_tf)(x)
 =\eta(x)\eta(x+s)^2\eta(x+s+t)f(x+s+t),
\tag{11}
\]

and hence

\[
\boxed{
 [T_s,T_t]f(x)
 =\eta(x)\eta(x+s+t)
  \{\eta(x+s)^2-\eta(x+t)^2\}f(x+s+t).}
\tag{12}
\]

Thus the multiplicative parallelogram has nonzero holonomy.  Summing (11)
over moves yields exactly the already established sandwich defect

\[
 M_\eta H^2M_\eta-T^2
 =M_\eta H(1-\eta^2)HM_\eta\ge0.
\tag{13}
\]

The primitive \(j_2\) cells belong to the first term of (13).  The physical
two-step walk is obtained only after subtracting the positive term on the
right.  Therefore declaring the primitive cells to be a positive summand
in the physical curvature has the wrong lower-bound direction.

## 4. Radical saturation test

Let

\[
 \widetilde r_j=r_j-\mu_K(r_j),\qquad r_j=K^{(2j)}/K.
\]

The full generator satisfies

\[
 L\widetilde r_j=\frac12\widetilde r_j,
\qquad
 L(L-\tfrac12)\widetilde r_j=0.
\tag{14}
\]

Suppose a global operator identity had the form

\[
 L(L-\tfrac12)=C^*C+J+[L,Y]+R,
 \qquad J,R\ge0.
\tag{15}
\]

Taking the expectation in a radical eigenvector kills the commutator and
the left side.  Hence (15) forces

\[
 C\widetilde r_j=0,qquad J^{1/2}\widetilde r_j=0,
 \qquad R^{1/2}\widetilde r_j=0.
\tag{16}
\]

The natural parallelogram cells do not have this property.  For example,
as \(x\to+\infty\), the first theta atom gives

\[
 r_1(x)=\frac{K''(x)}{K(x)}
       =4\pi^2e^{4x}(1+o(1)).
\tag{17}
\]

For every \(a,b>0\),

\[
 D_aD_br_1(x)
 =4\pi^2e^{4x}(e^{4a}-1)(e^{4b}-1)(1+o(1)),
\tag{18}
\]

which is nonzero.  Centering does not change a second difference.  Thus an
independent positive cell operator cannot occur in (15).  It must first be
shorted by the radical or cancelled by the theta/Gamma/polar defect.  Mere
orthogonality of the cluster to the radical does not perform that
cancellation inside the operator product.

## 5. Exact range of a trace-zero commutator

The following finite-dimensional statement is the decisive algebraic
audit for every finite Riesz block.

### Theorem 3 — Spectral-diagonal obstruction

Let \(L=\sum_\alpha\alpha E_\alpha\) be self-adjoint with finite discrete
spectrum.  An operator \(A\) is of the form \([L,Y]\) only if

\[
 E_\alpha AE_\alpha=0\qquad\text{for every \(\alpha\)}.
\tag{19}
\]

Conversely, (19) is sufficient, and one may take

\[
 Y=\sum_{\alpha\ne\beta}
 \frac{E_\alpha AE_\beta}{\alpha-\beta}.
\tag{20}
\]

If \(A=A^*\), then \(Y^*=-Y\).

#### Proof

Sandwiching \([L,Y]\) by \(E_\alpha\) gives zero, proving necessity.
For (20), its \((\alpha,\beta)\) block satisfies
\((\alpha-\beta)Y_{\alpha\beta}=A_{\alpha\beta}\), while the diagonal
blocks vanish.  This proves sufficiency and the adjoint statement.
\(\square\)

In particular, after subtracting proposed positive pieces
\(S=C^*C+J\), the spectral diagonal is

\[
 E_\lambda\{L(L-\tfrac12)-S\}E_\lambda
 =\lambda(\lambda-\tfrac12)E_\lambda-E_\lambda SE_\lambda.
\tag{21}
\]

For \(0<\lambda<1/2\), (21) is strictly negative.  It cannot be a
commutator plus a nonnegative remainder.  Consequently the mixed, ratio,
Gamma and polar channels can be declared an \(L\)-commutator only after
their complete spectral diagonal has independently been shown to vanish.
That diagonal assertion is the cluster inequality itself, not an algebraic
consequence of commutation.

## 6. The cutoff/projection dichotomy

There are two possible projections, and neither makes the commutator
automatic.

### 6.1. Full Riesz projection

Let \(P=P_J(L)\).  Then \([P,L]=0\), but generally
\([P,L_{\varepsilon,N}]\ne0\).  Finite-rank cyclicity gives the exact shell

\[
\boxed{
 \operatorname {Tr}P[L_{\varepsilon,N},Y_{\varepsilon,N}]
 =\operatorname {Tr}([P,L_{\varepsilon,N}]Y_{\varepsilon,N}).}
\tag{22}
\]

Graph convergence on the finite-dimensional range of \(P\) can make
\([P,L_{\varepsilon,N}]\) small.  It does not make (22) small unless one
also proves a reciprocal uniform bound on \(Y_{\varepsilon,N}\).  Such a
bound is unavailable here: 106.55 proves that the primitive prime
\(j_2\) term and the intermediate-position defect diverge separately and
cancel only at common cutoff.  A finite nonzero limit of (22), a
commutator anomaly, is therefore not excluded.

More precisely, with \(Q=I-P\), put

\[
 A_{\varepsilon,N}=QL_{\varepsilon,N}P
 =Q(L_{\varepsilon,N}-L)P.
\]

If \(Y_{\varepsilon,N}\) is skew-adjoint, block multiplication gives

\[
\boxed{
 \left|\operatorname {Tr}([P,L_{\varepsilon,N}]
 Y_{\varepsilon,N})\right|
 \le2\|A_{\varepsilon,N}\|_{\rm HS}
       \|QY_{\varepsilon,N}P\|_{\rm HS}.}
\tag{22a}
\]

Thus the sufficient cutoff condition is the product limit in (22a), not
merely graph convergence of \(L_{\varepsilon,N}P\).  If one instead uses
the canonical Sylvester inverse of the *full* \(\operatorname {ad}_L\) on
an isolated cluster, the fixed spectral separation bounds the second
factor and the shell vanishes.  In that choice, however, Theorem 3 moves
only the off-diagonal block: the untouched block diagonal is exactly the
quantity in (26).  Hence controlling the anomaly does not by itself supply
the missing sign.

### 6.2. Cutoff spectral projection

Let instead \(P_{\varepsilon,N}\) commute with
\(L_{\varepsilon,N}\).  The trace in (22) is then zero, but the cutoff
operator has no \(1/2\) tail floor.

### Lemma 4 — Fixed cutoffs have vanishing tail Rayleigh quotient

For fixed \(\varepsilon>0\) and \(N<\infty\),

\[
 \inf_{f\perp1}
 \frac{\langle f,L_{\varepsilon,N}f\rangle}{\|f\|^2}=0.
\tag{23}
\]

#### Proof

All retained displacements satisfy \(|s|\le A_{\varepsilon,N}<\infty\),
and their total measure is finite.  The jump rate is

\[
 c_s(x)=\frac{c_KK(x+s)}{h(x)}.
\]

The double-exponential decay of \(K\) gives

\[
 \sup_{|s|\le A_{\varepsilon,N}}c_s(x)\longrightarrow0
 \qquad(x\to+\infty).
\tag{24}
\]

Choose two smooth bumps in a unit interval translated to \(R\), with
coefficients adjusted to have \(\mu_K\)-mean zero, and normalize their
\(L^2(\mu_K)\) norm.  Detailed balance bounds their jump energy by the
maximum total rate on the support and its fixed displacement
neighborhood.  By (24), the Rayleigh quotient tends to zero as
\(R\to\infty\). \(\square\)

Thus the finite cutoff necessarily has spectral mass below \(1/2\) after
the constant is removed.  A positive finite-cutoff factorization of
\(L_{\varepsilon,N}(L_{\varepsilon,N}-1/2)\) cannot hold on its entire
centered space.

## 7. What can still survive in the full limit

A genuinely joint full-limit correction is not ruled out.  It would have
to prove both of the following statements for every finite full-generator
Riesz projection \(P\):

1. **commutator-anomaly control**

   \[
   \operatorname {Tr}([P,L_{\varepsilon,N}]
   Y_{\varepsilon,N})\longrightarrow0,
   \tag{25}
   \]

   or compute its nonzero limit with the correct sign; and

2. **spectral-diagonal compensation**: after the primitive cell square,
   the intermediate-position square (13), all prime diagonal terms, the
   Gamma potential, the pole and the threshold subtraction are combined,
   the surviving diagonal block is nonnegative.

Equivalently, if \(S_{\varepsilon,N}\ge0\) denotes the *shorted* physical
cell square and

\[
 A_{\varepsilon,N}
 =L_{\varepsilon,N}^2-\frac12L_{\varepsilon,N}
  -S_{\varepsilon,N},
\]

the missing theorem is not the existence of an off-diagonal solution of a
Sylvester equation.  It is

\[
\boxed{
 \liminf_{\varepsilon\downarrow0,\,N\to\infty}
 \operatorname {Tr}(P A_{\varepsilon,N})\ge0,}
\tag{26}
\]

with every term kept at the same cutoff.  Theorem 3 shows that all
off-diagonal blocks of \(A_{\varepsilon,N}\) may be moved into a
commutator; (26) is exactly the block which no commutator can move.

## 8. Conclusion

Proved here:

* the exact positive multiplicative-cell realization of \(j_2\);
* the exact flat parallelogram identity;
* the theta-sandwich cell holonomy;
* the radical saturation obstruction to an independent positive cell
  summand;
* the spectral-diagonal characterization of the range of \(\operatorname
  {ad}_L\);
* the full-projection/cutoff-projection dichotomy.

Not proved: the spectral-diagonal compensation (26).  The proposed
``positive cells plus trace-zero commutator'' argument does not close it:
the cells overcount the physical walk, and the cutoff commutator has a
potentially nonvanishing projection shell.  Any successful continuation
must estimate that shell jointly with the intermediate theta defect and
the Gamma--polar completion; it cannot discard it by cyclicity.
