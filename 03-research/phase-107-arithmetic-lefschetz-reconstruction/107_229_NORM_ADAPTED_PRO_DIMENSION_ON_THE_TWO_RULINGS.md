# 107.229 -- A norm-adapted pro-dimension on the two rulings

## 1. Failure of the rectangular depth levels

The levels of 107_154 use

\[
 M_p(A,R)=\{0\}\cup
 \{c p^j:1\leq c\leq A,\ p\nmid c,\ |j|\leq R\}
\]

and have rank

\[
 d_p(A,R)=1+(A-\lfloor A/p\rfloor)(2R+1).
 \tag{1.1}
\]

For fixed \(A\), their normalization by the published periodic scale
is therefore

\[
 p^{-R}d_p(A,R)\longrightarrow0.
 \tag{1.2}
\]

On two rulings, even allowing independent depths, one similarly has

\[
 p^{-R}q^{-S}d_p(A,R)d_q(B,S)\longrightarrow0
 \qquad(R,S\to\infty).
 \tag{1.3}
\]

Thus 107_154 is a valid exhaustive filtration of the stalk, but it is
not adapted to the continuous-dimension normalization of the periodic
Riemann--Roch theorem. Exhaustiveness alone did not control density.

## 2. The norm-adapted level

At the normalized point \(\lambda=1\) of \(C_p\), the published
filtration bounds the \(p\)-adic norm of a slope. A compact real slope
window supplies the second bound. For \(A\in\mathbb Q_{>0}\), define

\[
 N_p(A,R)=
 \{x\in\mathbb Z[1/p]_{+}:x\leq A,\ |x|_p\leq p^R\}.
 \tag{2.1}
\]

### Proposition 2.1

One has the exact equality

\[
 N_p(A,R)=p^{-R}\mathbb Z\cap[0,A]
 \tag{2.2}
\]

and hence

\[
 \#N_p(A,R)=\lfloor Ap^R\rfloor+1.
 \tag{2.3}
\]

### Proof

If \(x\in\mathbb Z[1/p]\) and \(|x|_p\leq p^R\), its reduced
denominator divides \(p^R\), so \(x=a/p^R\) for some integer \(a\).
The real inequalities are exactly \(0\leq a\leq Ap^R\). The converse
is immediate. \(\square\)

Consequently

\[
 A\leq p^{-R}\#N_p(A,R)\leq A+p^{-R},
 \tag{2.4}
\]

so the normalized density exists and equals \(A\).

At another point \(\lambda\in[1,p]\), the factor \(1/\lambda\) in the
published norm only rescales the compact window. It does not change the
exponential normalization or the argument above.

## 3. Exact Frobenius covariance

The norm-adapted levels are not invariant at fixed \((A,R)\), nor
should they be. For \(R\geq1\), multiplication and division by \(p\)
give exact equalities

\[
 pN_p(A,R)=N_p(pA,R-1),
 \qquad
 p^{-1}N_p(A,R)=N_p(A/p,R+1).
 \tag{3.1}
\]

Thus Frobenius remains a map between levels, now with the real and
nonarchimedean bounds transformed together. This is the norm-adapted
replacement for the rectangular inclusions of 107_154.

## 4. Two-ruling cofinal limit

For primes \(p,q\), positive rational windows \(A,B\), and independent
depths \(R,S\), put

\[
 N_{p,q}(A,B;R,S)=N_p(A,R)\times N_q(B,S).
 \tag{4.1}
\]

Let \(L_{p,q}(A,B;R,S)\) be the free abelian group on these rays and
let \(E_{p,q}(A,B;R,S;1)\) be its coefficient-\(\ell^1\) ball of
radius one. By the primitive-ray lemma of 107_152,

\[
 \dim_{\mathbb S[\pm1]}E_{p,q}(A,B;R,S;1)
 =\#N_{p,q}(A,B;R,S).
 \tag{4.2}
\]

### Theorem 4.1 (cofinal pro-dimension)

For every cofinal net with \(R,S\to\infty\),

\[
 \lim p^{-R}q^{-S}
 \dim_{\mathbb S[\pm1]}E_{p,q}(A,B;R,S;1)=AB.
 \tag{4.3}
\]

More precisely,

\[
 0\leq
 p^{-R}q^{-S}\#N_{p,q}-AB
 \leq A q^{-S}+B p^{-R}+p^{-R}q^{-S}.
 \tag{4.4}
\]

### Proof

Write

\[
 p^{-R}\#N_p=A+\epsilon_R,
 \qquad
 q^{-S}\#N_q=B+\eta_S,
\]

where \(0\leq\epsilon_R\leq p^{-R}\) and
\(0\leq\eta_S\leq q^{-S}\) by (2.4). Multiplication gives (4.4),
whose right side tends to zero independently of the relative rates of
\(R\) and \(S\). \(\square\)

The theorem also applies to the two rulings over one prime by taking
\(p=q\) and keeping \(R,S\) independent.

## 5. Exact comparison with the published one-ruling \(H^0\)

The full proof of periodic RR in Connes--Consani, *Geometry of the
Scaling Site*, arXiv:1603.03191, Lemma 6.19 and Theorem 6.20, gives a
stronger exact control. For \(\alpha\in H_p\), \(\alpha>0\), and all
sufficiently large \(n\),

\[
 \mathrm{tdim}\,H^0(\alpha\{1\})^{p^n}
 =\alpha p^n-p+1.
 \tag{5.1}
\]

At the same window and depth, (2.3) gives

\[
 \#N_p(\alpha,n)=\alpha p^n+1.
 \tag{5.2}
\]

Thus the discrepancy is exactly

\[
 \#N_p(\alpha,n)
 -\mathrm{tdim}\,H^0(\alpha\{1\})^{p^n}=p,
 \tag{5.3}
\]

and vanishes after normalization:

\[
 p^{-n}\left|#N_p-operatorname{tdim}H^0\right|
 =p^{1-n}\longrightarrow0.
 \tag{5.4}
\]

Therefore the norm-adapted support density is not merely of the correct
order: on every published special-divisor control it computes exactly
the continuous dimension in the limit,

\[
 \lim_{n\to\infty}p^{-n}\#N_p(\alpha,n)
 =\mathrm{cdim}\,H^0(\alpha\{1\})=\alpha.
 \tag{5.5}
\]

This validates one ruling. It does not prove that taking products of
the support sets computes the covering dimension of a section module
on the square.

## 6. What is constructed

This supplies all of the following without a conjectural dimension
formula:

1. a filtration derived from simultaneous real and \(p\)-adic slope
   bounds;
2. exact Frobenius covariance between its levels;
3. an exact normalized \(\mathbb S[\pm1]\)-dimension at mass one;
4. a two-ruling limit independent of every cofinal path.

It is the first nonzero pro-dimension on the Phase 107 square levels.
The rectangular filtration of 107_154 gives zero under the same
normalization.

## 7. Scope and next gate

The number \(AB\) is a slope-window density. This note does **not**
identify it with
\(\mathrm{tdim}\,H^0(D)^{p^R}\), because that requires the
piecewise-affine divisor inequalities, singularity positions, and
topology of the actual section module. It also does not construct
\(H^1\), RR, an intersection product, or the global square.

The next gate is now geometric and exact: for a divisor \(D\) on a
periodic product, describe its finite-level section space as a
polyhedral family inside the norm-adapted slope lattice and prove that
its normalized covering dimension has a cofinal limit. A mere count of
rays will not satisfy that gate.

## 8. Exact verifier

107_229_norm_adapted_pro_dimension.py enumerates actual rational slope
sets for the primes \(2,3,5,7,11\), checks (2.2), the two Frobenius
equalities, the rectangular zero-density control, and the error bound
along diagonal and strongly unbalanced cofinal paths. It also checks
the exact discrepancy (5.3) on published special-divisor controls.
Mutating either
the real or \(p\)-adic cutoff makes one of these checks return NO.
